"""Optional vector index: ChromaDB-backed, with metadata filtering.

Falls back to an in-memory cosine index when ChromaDB / sentence-transformers
are not available. The default build path does not instantiate this module;
agents use BM25 + structured grounding unless vector mode is explicitly enabled.
"""

from __future__ import annotations
import math
import os
import pickle
import re
import threading
from importlib import metadata
from pathlib import Path
from typing import List, Dict, Any, Optional

_BACKEND = None  # "chroma" or "memory"
_BACKEND_LOCK = threading.Lock()


def _try_chroma():
    try:
        import chromadb  # noqa: F401
        from chromadb.utils import embedding_functions  # noqa: F401
        return True
    except Exception:
        return False


def _try_st():
    if not _torch_runtime_ok():
        return False
    try:
        from sentence_transformers import SentenceTransformer  # noqa: F401
        return True
    except Exception:
        return False


def _torch_runtime_ok():
    try:
        version = metadata.version("torch")
    except metadata.PackageNotFoundError:
        return False
    match = re.match(r"^(\d+)\.(\d+)", version)
    if not match:
        return False
    major, minor = int(match.group(1)), int(match.group(2))
    return (major, minor) >= (2, 1)


class _MemoryStore:
    """Tiny in-memory cosine store for fallback mode."""

    def __init__(self, dim=1024):
        self.dim = dim
        self.ids, self.texts, self.metas, self.vectors = [], [], [], []

    def add(self, ids, texts, metas, vectors):
        for i, t, m, v in zip(ids, texts, metas, vectors):
            self.ids.append(i)
            self.texts.append(t)
            self.metas.append(m or {})
            self.vectors.append(self._l2(v))

    def _l2(self, v):
        n = math.sqrt(sum(x * x for x in v)) or 1.0
        return [x / n for x in v]

    def _match(self, where, meta):
        if not where:
            return True
        for k, val in where.items():
            if meta.get(k) != val:
                return False
        return True

    def query(self, qvec, k, where):
        qn = self._l2(qvec)
        scored = []
        for i, v in enumerate(self.vectors):
            if not self._match(where, self.metas[i]):
                continue
            s = sum(a * b for a, b in zip(qn, v))
            scored.append((1 - s, i))
        scored.sort()
        out_ids, out_docs, out_meta, out_dist = [], [], [], []
        for dist, i in scored[:k]:
            out_ids.append(self.ids[i])
            out_docs.append(self.texts[i])
            out_meta.append(self.metas[i])
            out_dist.append(dist)
        return [out_ids], [out_docs], [out_meta], [out_dist]

    def clear(self):
        self.ids, self.texts, self.metas, self.vectors = [], [], [], []

    def to_dict(self):
        return {
            "dim": self.dim,
            "ids": self.ids,
            "texts": self.texts,
            "metas": self.metas,
            "vectors": self.vectors,
        }

    @classmethod
    def from_dict(cls, data):
        store = cls(dim=int(data.get("dim") or 1024))
        store.ids = list(data.get("ids") or [])
        store.texts = list(data.get("texts") or [])
        store.metas = list(data.get("metas") or [])
        store.vectors = list(data.get("vectors") or [])
        return store


class VectorIndex:
    def __init__(self, persist_dir="artifacts/chroma",
                 model_name="",
                 device="cpu", dim_hint=1024):
        global _BACKEND
        self.persist_dir = persist_dir
        self.model_name = model_name
        self.device = device
        self._mem = None
        self._memory_path = Path(persist_dir).with_name("vector_memory.pkl")
        self._client = None
        self._coll = None
        self._embedder = None
        self._uses_hash_embedder = False

        if _try_chroma() and _try_st():
            with _BACKEND_LOCK:
                if _BACKEND is None:
                    _BACKEND = "chroma"
            try:
                self._init_chroma()
            except Exception:
                with _BACKEND_LOCK:
                    _BACKEND = "memory"
                self._client = None
                self._coll = None
                self._mem = self._load_memory_store(dim_hint)
                self._uses_hash_embedder = True
                self._embedder = self._hash_embedder
        else:
            with _BACKEND_LOCK:
                if _BACKEND is None:
                    _BACKEND = "memory"
            self._mem = self._load_memory_store(dim_hint)
            if _try_st():
                try:
                    self._init_st()
                except Exception:
                    self._uses_hash_embedder = True
                    self._embedder = self._hash_embedder
            else:
                self._uses_hash_embedder = True
                self._embedder = self._hash_embedder

    def _load_memory_store(self, dim_hint):
        if not self._memory_path.exists():
            return _MemoryStore(dim=dim_hint)
        try:
            data = pickle.loads(self._memory_path.read_bytes())
            return _MemoryStore.from_dict(data)
        except Exception:
            return _MemoryStore(dim=dim_hint)

    def _save_memory_store(self):
        if _BACKEND != "memory" or self._mem is None:
            return
        self._memory_path.parent.mkdir(parents=True, exist_ok=True)
        self._memory_path.write_bytes(pickle.dumps(self._mem.to_dict()))

    def _init_st(self):
        from sentence_transformers import SentenceTransformer
        kwargs = {"device": self.device}
        if os.environ.get("RETRIEVER_ALLOW_MODEL_DOWNLOAD") != "1":
            kwargs["local_files_only"] = True
        try:
            self._embedder = SentenceTransformer(self.model_name, **kwargs)
        except TypeError:
            kwargs.pop("local_files_only", None)
            self._embedder = SentenceTransformer(self.model_name, **kwargs)
        try:
            self._embedder.max_seq_length = 512
        except Exception:
            pass

    def _hash_embedder(self, texts):
        # Deterministic fallback (no model download) - for smoke tests
        out = []
        for t in texts:
            v = [0.0] * self._mem.dim
            for i, ch in enumerate(t):
                v[(i + ord(ch)) % self._mem.dim] += 1.0
            n = math.sqrt(sum(x * x for x in v)) or 1.0
            out.append([x / n for x in v])
        return out

    def embed(self, texts):
        if hasattr(self._embedder, "encode"):
            vecs = self._embedder.encode(
                list(texts), batch_size=32,
                normalize_embeddings=True, show_progress_bar=False)
            return [v.tolist() for v in vecs]
        return self._embedder(list(texts))

    def _init_chroma(self):
        import chromadb
        Path(self.persist_dir).mkdir(parents=True, exist_ok=True)
        self._client = chromadb.PersistentClient(path=self.persist_dir)
        try:
            self._coll = self._client.get_collection("canoe_kb")
        except Exception:
            self._coll = self._client.create_collection(
                name="canoe_kb", metadata={"hnsw:space": "cosine"})
        self._init_st()


    def add(self, docs, batch=128):
        if not docs:
            return 0
        ids, texts, metas = [], [], []
        for d in docs:
            ids.append(d["id"])
            texts.append(d["embed_text"])
            metas.append({
                "topic": d.get("topic", "extras"),
                "version": d.get("version", "extras"),
                "page_type": d.get("page_type", "concept"),
                "subcategory": d.get("subcategory", ""),
                "name": d.get("name", ""),
                "raw_json_path": d.get("raw_json_path", ""),
                "raw_md_path": d.get("raw_md_path", ""),
            })
        if _BACKEND == "chroma":
            vecs = self.embed(texts)
            for i in range(0, len(ids), batch):
                self._coll.add(
                    ids=ids[i:i+batch],
                    documents=texts[i:i+batch],
                    metadatas=metas[i:i+batch],
                    embeddings=vecs[i:i+batch],
                )
        else:
            vecs = self.embed(texts)
            self._mem.add(ids, texts, metas, vecs)
            self._save_memory_store()
        return len(ids)

    def count(self):
        if _BACKEND == "chroma":
            return self._coll.count()
        return len(self._mem.ids)

    def has(self, doc_id):
        if _BACKEND == "chroma":
            res = self._coll.get(ids=[doc_id])
            return bool(res["ids"])
        return doc_id in self._mem.ids

    def search(self, query, k=20, where=None):
        if _BACKEND == "chroma":
            qvec = self.embed([query])[0]
            res = self._coll.query(
                query_embeddings=[qvec],
                n_results=k, where=where,
                include=["metadatas", "documents", "distances"])
            out = []
            for i, doc_id in enumerate(res["ids"][0]):
                meta = res["metadatas"][0][i]
                out.append({
                    "id": doc_id,
                    "vector_score": 1 - res["distances"][0][i],
                    "text": res["documents"][0][i],
                    "embed_text": res["documents"][0][i],
                    "meta": meta,
                    **meta,
                })
            return out
        qvec = self.embed([query])[0]
        ids, docs, metas, dists = self._mem.query(qvec, k, where)
        return [
            {"id": ids[0][i], "vector_score": 1 - dists[0][i],
             "text": docs[0][i], "embed_text": docs[0][i],
             "meta": metas[0][i], **metas[0][i]}
            for i in range(len(ids[0]))
        ]

    def remove(self, doc_id):
        if _BACKEND == "chroma":
            try:
                self._coll.delete(ids=[doc_id])
                return 1
            except Exception:
                return 0
        try:
            idx = self._mem.ids.index(doc_id)
            for lst in (self._mem.ids, self._mem.texts,
                        self._mem.metas, self._mem.vectors):
                lst.pop(idx)
            self._save_memory_store()
            return 1
        except ValueError:
            return 0

    def backend(self):
        return _BACKEND or "memory"

    def reset(self):
        if _BACKEND == "chroma":
            try:
                self._client.delete_collection("canoe_kb")
            except Exception:
                pass
            self._coll = self._client.create_collection(
                name="canoe_kb", metadata={"hnsw:space": "cosine"})
            return
        if self._mem is not None:
            self._mem.clear()
        try:
            self._memory_path.unlink()
        except FileNotFoundError:
            pass

    def semantic_available(self):
        return not self._uses_hash_embedder
