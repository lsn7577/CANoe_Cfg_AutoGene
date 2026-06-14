"""Agent-first retriever: BM25 candidate recall + structured grounding.

Typical use:

    from retriever.retriever import HybridRetriever
    retr = HybridRetriever.build_from_disk()    # one-time load
    hits = retr.retrieve("how to send a CAN frame", version="v15")

The retriever is read-only at runtime; add new documents via
`retriever.ingest.ingest_files()` or `retriever.ingest.ingest_dir()`.
Semantic vector search and reranking are optional enhancements and are disabled
by default so agents can do semantic understanding themselves.
"""

from __future__ import annotations
import json
import time
from pathlib import Path
from typing import List, Dict, Any, Optional

from .config import (ROOT, ARTIFACTS_DIR, KNOWLEDGE_DIR, KNOWN_VERSIONS,
                     RetrievalConfig, get_config)
from .bm25_index import BM25Index
from .classifier import classify, QueryKind
from .fusion import rrf_fuse, Reranker
from .grounding import Grounding


def _display_path(path: Path) -> str:
    try:
        path = Path(path).resolve().relative_to(ROOT)
    except ValueError:
        path = Path(path)
    return path.as_posix()


class HybridRetriever:
    def __init__(self, knowledge_dir: Path, artifacts_dir: Path,
                 cfg: Optional[RetrievalConfig] = None):
        self.knowledge_dir = knowledge_dir
        self.artifacts_dir = artifacts_dir
        self.cfg = cfg or get_config()
        self.grounding = Grounding(knowledge_dir.parent)
        self.bm25: Optional[BM25Index] = None
        self.vector: Optional[Any] = None
        self.rerank: Optional[Reranker] = None
        self._loaded = False

    # ---------- construction ----------
    @classmethod
    def build_from_disk(cls, knowledge_dir: Path = KNOWLEDGE_DIR,
                        artifacts_dir: Path = ARTIFACTS_DIR,
                        cfg: Optional[RetrievalConfig] = None
                        ) -> "HybridRetriever":
        retr = cls(knowledge_dir, artifacts_dir, cfg)
        bm25_path   = artifacts_dir / "bm25.pkl"
        bm25 = BM25Index.load(bm25_path) if bm25_path.exists() else None
        if bm25 is None:
            print("[retriever] No BM25 index found - run `python -m retriever.build`")

        vector = None
        if retr.cfg.embedding.enabled:
            from .vector_index import VectorIndex

            vector = VectorIndex(
                persist_dir=str(artifacts_dir / "chroma"),
                model_name=retr.cfg.embedding.model_name,
                device=retr.cfg.embedding.device,
            )
            if not vector.semantic_available():
                vector = None

        rerank = None
        if retr.cfg.rerank.enabled:
            rerank = Reranker(
                model_name=retr.cfg.rerank.model_name,
                enabled=True,
                device="cpu",
            )
        retr.bm25, retr.vector, retr.rerank = bm25, vector, rerank
        retr._loaded = True
        return retr

    # ---------- main entry ----------
    def retrieve(self, query: str,
                 version: str = "v15",
                 topic: Optional[str] = None,
                 page_type: Optional[str] = None,
                 top_n: int = 8) -> List[Dict[str, Any]]:
        assert self._loaded, "Call HybridRetriever.build_from_disk() first"
        if not self.bm25:
            return []
        kind = classify(query)
        where = {}
        if topic == "extras":
            where["version"] = "extras"
        elif version and version in KNOWN_VERSIONS:
            where["version"] = version
        if topic and topic != "extras":
            where["topic"] = topic
        if page_type:
            where["page_type"] = page_type

        t0 = time.perf_counter()
        cand = self._first_stage(query, kind, where)
        t1 = time.perf_counter()

        # Rerank
        if self.rerank and self.rerank.available:
            cand = self.rerank.rerank(query, cand, top_n=top_n)
        else:
            cand = cand[:top_n]
        t2 = time.perf_counter()

        # Ground
        for d in cand:
            self.grounding.ground(d)
        t3 = time.perf_counter()

        for d in cand:
            d["_meta"] = {
                "route": kind,
                "recall_ms": round((t1 - t0) * 1000, 1),
                "rerank_ms": round((t2 - t1) * 1000, 1),
                "ground_ms": round((t3 - t2) * 1000, 1),
                "total_ms":  round((t3 - t0) * 1000, 1),
            }
        return cand

    # ---------- internals ----------
    def _first_stage(self, query: str, kind: QueryKind,
                     where: Dict[str, Any]) -> List[Dict[str, Any]]:
        bm_top = self.cfg.bm25_top_k
        fused_top = self.cfg.fused_top_k

        if kind == "exact":
            bm = self.bm25.search(query, k=bm_top if where else fused_top)
            return self._filter_where(bm, where)[:fused_top]

        if kind == "semantic":
            if not self._has_semantic_vector():
                return self._bm25_fallback(query, where, bm_top, fused_top)
            vec_top = self.cfg.vector_top_k
            vec = self.vector.search(query, k=vec_top, where=where or None)
            bm = self._filter_where(self.bm25.search(query, k=bm_top), where)
            return rrf_fuse(bm, vec, k=self.cfg.rrf_k)[:fused_top]

        # hybrid
        if not self._has_semantic_vector():
            return self._filter_where(self.bm25.search(query, k=bm_top), where)[:fused_top]
        vec_top = self.cfg.vector_top_k
        bm  = self._filter_where(self.bm25.search(query, k=bm_top), where)
        vec = self.vector.search(query, k=vec_top, where=where or None)
        return rrf_fuse(bm, vec, k=self.cfg.rrf_k)[:fused_top]

    def _has_semantic_vector(self) -> bool:
        return bool(self.vector and self.vector.semantic_available())

    def _bm25_fallback(self, query: str, where: Dict[str, Any],
                       bm_top: int, fused_top: int) -> List[Dict[str, Any]]:
        fallback_queries = self._fallback_queries(query)
        if fallback_queries:
            first = self._filter_where(self.bm25.search(fallback_queries[0], k=bm_top), where)
            if first:
                return first[:fused_top]
        queries = fallback_queries + [query]
        ranked = [
            self._filter_where(self.bm25.search(q, k=bm_top), where)
            for q in queries
        ]
        ranked = [r for r in ranked if r]
        if not ranked:
            return []
        return rrf_fuse(*ranked, k=self.cfg.rrf_k)[:fused_top]

    @staticmethod
    def _fallback_queries(query: str) -> List[str]:
        q = (query or "").lower()
        out: List[str] = []
        send_terms = ("send", "transmit", "output", "发", "发送", "输出")
        frame_terms = ("frame", "message", "报文", "帧")
        if ("can" in q and any(term in q for term in frame_terms)
                and any(word in q for word in send_terms)):
            out.extend(["output (CAN)", "output CAN frame"])
        if ("panel" in q or "面板" in q) and "gauge" in q:
            out.extend(["Analog Gauge", "panel gauge"])
        return out

    def _filter_where(self, docs: List[Dict[str, Any]],
                      where: Dict[str, Any]) -> List[Dict[str, Any]]:
        if not where:
            return docs
        return [d for d in docs if self._matches_where(d, where)]

    @staticmethod
    def _matches_where(doc: Dict[str, Any], where: Dict[str, Any]) -> bool:
        meta = doc.get("meta") or {}
        for key, expected in where.items():
            if doc.get(key, meta.get(key)) != expected:
                return False
        return True

    # ---------- diagnostics ----------
    def info(self) -> Dict[str, Any]:
        return {
            "knowledge_dir": _display_path(self.knowledge_dir),
            "artifacts_dir": _display_path(self.artifacts_dir),
            "bm25_docs": len(self.bm25.docs) if self.bm25 else 0,
            "vector_count": self.vector.count() if self.vector else 0,
            "vector_backend": self.vector.backend() if self.vector else "disabled",
            "semantic_vector_available": self.vector.semantic_available() if self.vector else False,
            "rerank_backend": self.rerank.backend() if self.rerank else "disabled",
        }
