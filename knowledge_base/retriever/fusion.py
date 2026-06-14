"""Reciprocal Rank Fusion (RRF) and optional Cross-Encoder reranking."""

from __future__ import annotations
from collections import defaultdict
from importlib import metadata
import os
import re
from typing import List, Dict, Any, Iterable

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


def rrf_fuse(*ranked_lists: Iterable[Dict[str, Any]],
             k: int = 60) -> List[Dict[str, Any]]:
    """Reciprocal Rank Fusion over N ranked lists (each item must have 'id')."""
    scores: Dict[str, float] = defaultdict(float)
    payload: Dict[str, Dict[str, Any]] = {}
    for lst in ranked_lists:
        for rank, item in enumerate(lst, 1):
            doc_id = item["id"]
            scores[doc_id] += 1.0 / (k + rank)
            payload.setdefault(doc_id, item)
    fused = sorted(payload.values(),
                   key=lambda d: scores[d["id"]], reverse=True)
    for d in fused:
        d["rrf_score"] = scores[d["id"]]
    return fused


class Reranker:
    """Optional Cross-Encoder reranker. Falls back to identity if unavailable."""

    def __init__(self, model_name: str = "",
                 enabled: bool = True, device: str = "cpu"):
        self.enabled = enabled
        self.model_name = model_name
        self.device = device
        self._ce = None
        if enabled and model_name:
            try:
                CrossEncoder = _load_cross_encoder()
                kwargs = {"device": device}
                if os.environ.get("RETRIEVER_ALLOW_MODEL_DOWNLOAD") != "1":
                    kwargs["local_files_only"] = True
                try:
                    self._ce = CrossEncoder(model_name, **kwargs)
                except TypeError:
                    kwargs.pop("local_files_only", None)
                    self._ce = CrossEncoder(model_name, **kwargs)
            except Exception:
                self._ce = None

    @property
    def available(self) -> bool:
        return self._ce is not None

    def rerank(self, query: str,
               docs: List[Dict[str, Any]],
               top_n: int = 8) -> List[Dict[str, Any]]:
        if not docs:
            return []
        if self._ce is None:
            return docs[:top_n]
        # Cross-encoder needs (query, document) pairs
        def _text(d):
            return d.get("text") or d.get("embed_text") or d.get("name", "")
        pairs = [(query, _text(d)) for d in docs]
        try:
            scores = self._ce.predict(pairs)
        except Exception:
            return docs[:top_n]
        for d, s in zip(docs, scores):
            d["rerank_score"] = float(s)
        docs.sort(key=lambda d: d.get("rerank_score", 0.0), reverse=True)
        return docs[:top_n]

    def backend(self) -> str:
        return "cross-encoder" if self._ce is not None else "passthrough"


def _load_cross_encoder():
    if not _torch_runtime_ok():
        raise ImportError("PyTorch >= 2.1 is required for sentence-transformers")
    from sentence_transformers import CrossEncoder
    return CrossEncoder
