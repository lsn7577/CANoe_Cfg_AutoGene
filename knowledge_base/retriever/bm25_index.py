"""BM25 index over the knowledge base, with incremental-add support."""

from __future__ import annotations
import pickle
import re
from pathlib import Path
from typing import List, Dict, Any, Iterable, Tuple

try:
    from rank_bm25 import BM25Okapi
except ImportError:
    BM25Okapi = None

try:
    import jieba
    _TOKEN = lambda s: [t for t in jieba.cut_for_search(s) if t.strip()]
except ImportError:
    _TOKEN = lambda s: re.findall(r"[A-Za-z_]\w*|[一-龥]+|\d+", s)


def tokenize(text: str) -> List[str]:
    return _TOKEN(text or "")


def _norm_doc(d: Dict[str, Any]) -> Tuple[str, str]:
    """Combine fields for BM25 corpus. Boost name strongly via repetition."""
    name = d.get("name", "") or ""
    pt   = d.get("page_type", "")
    embed = d.get("embed_text", "") or ""
    return (d["id"], (name + " ") * 3 + " " + pt + " " + embed)


class BM25Index:
    """Wraps a BM25Okapi index with an aligned id list for incremental updates."""

    def __init__(self, docs: List[Dict[str, Any]] = None):
        self.docs: List[Dict[str, Any]] = list(docs or [])
        self._id_set = {d["id"] for d in self.docs}
        self._corpus_tokens: List[List[str]] = []
        self._bm25 = None
        if self.docs:
            self._rebuild()

    # ---- public API ----
    def add(self, docs: List[Dict[str, Any]]):
        new = [d for d in docs if d["id"] not in self._id_set]
        if not new:
            return 0
        self.docs.extend(new)
        self._id_set.update(d["id"] for d in new)
        # Tokens for the new docs
        new_tokens = [tokenize(_norm_doc(d)[1]) for d in new]
        self._corpus_tokens.extend(new_tokens)
        if self._bm25 is None:
            self._rebuild()
        else:
            # BM25Okapi needs full corpus to build; do an in-place append
            # by extending its internal structures
            self._bm25.corpus = self._bm25.corpus + new_tokens
            self._bm25.doc_len  = self._bm25.doc_len + [len(t) for t in new_tokens]
            self._bm25.doc_freq = self._bm25.doc_freq  # unchanged by corpus add
            self._bm25.idf      = self._bm25._calculate_idf()  # recalc idf
            self._bm25.doc_freq = [0] * len(self._bm25.idf)
            for tokens in self._bm25.corpus:
                seen = set()
                for t in tokens:
                    if t in self._bm25.idf and t not in seen:
                        self._bm25.doc_freq[self._bm25.idf[t]] += 1
                        seen.add(t)
        return len(new)

    def remove(self, doc_id: str) -> int:
        idx = next((i for i, d in enumerate(self.docs) if d["id"] == doc_id), -1)
        if idx < 0:
            return 0
        del self.docs[idx]
        self._id_set.discard(doc_id)
        self._rebuild()
        return 1

    def search(self, query: str, k: int = 20) -> List[Dict[str, Any]]:
        if not self._bm25 or not self.docs:
            return []
        toks = tokenize(query)
        if not toks:
            return []
        scores = self._bm25.get_scores(toks)
        order = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:k]
        return [{**self.docs[i], "bm25_score": float(scores[i])}
                for i in order if scores[i] > 0]

    def save(self, path: Path):
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(pickle.dumps({
            "docs": self.docs,
            "tokens": self._corpus_tokens,
        }))

    @classmethod
    def load(cls, path: Path) -> "BM25Index":
        path = Path(path)
        blob = pickle.loads(path.read_bytes())
        obj = cls.__new__(cls)
        obj.docs = blob["docs"]
        obj._id_set = {d["id"] for d in obj.docs}
        obj._corpus_tokens = blob["tokens"]
        obj._rebuild_from_tokens()
        return obj

    # ---- internal ----
    def _rebuild(self):
        self._corpus_tokens = [tokenize(_norm_doc(d)[1]) for d in self.docs]
        self._rebuild_from_tokens()

    def _rebuild_from_tokens(self):
        if BM25Okapi is None:
            raise RuntimeError("rank_bm25 is not installed. Run: pip install rank_bm25")
        self._bm25 = BM25Okapi(self._corpus_tokens) if self._corpus_tokens else None
