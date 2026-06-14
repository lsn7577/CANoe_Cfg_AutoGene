"""Centralised configuration for the agent-facing retriever pipeline."""

from __future__ import annotations
from dataclasses import dataclass, field
import os
from pathlib import Path

# Repository layout
ROOT = Path(__file__).resolve().parent.parent
KNOWLEDGE_DIR = ROOT / "knowledge"
EXTRAS_DIR = ROOT / "extras"            # user-added knowledge lives here
ARTIFACTS_DIR = ROOT / "artifacts"
ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)


@dataclass
class EmbeddingConfig:
    enabled: bool = False
    model_name: str = ""
    device: str = "cpu"
    batch_size: int = 32
    normalize: bool = True


@dataclass
class RerankConfig:
    enabled: bool = False
    model_name: str = ""
    top_n: int = 8


@dataclass
class RetrievalConfig:
    bm25_top_k: int = 60
    vector_top_k: int = 60
    fused_top_k: int = 20
    rrf_k: int = 60
    embedding: EmbeddingConfig = field(default_factory=EmbeddingConfig)
    rerank: RerankConfig = field(default_factory=RerankConfig)


KNOWN_TOPICS = {"capl", "panel", "dbc", "xcp", "diagnostics", "team", "extras"}
KNOWN_VERSIONS = {"v12", "v15"}

DEFAULT_SUBCATEGORY = {
    "function": "Functions",
    "method": "Methods",
    "event": "Events",
    "selector": "Selectors",
    "concept": "Concepts",
}


def get_config() -> RetrievalConfig:
    embedding_enabled = _env_flag("RETRIEVER_ENABLE_VECTOR")
    rerank_enabled = _env_flag("RETRIEVER_ENABLE_RERANK")
    return RetrievalConfig(
        embedding=EmbeddingConfig(
            enabled=embedding_enabled,
            model_name=(
                os.environ.get("RETRIEVER_EMBEDDING_MODEL", "BAAI/bge-m3")
                if embedding_enabled else ""
            ),
            device=os.environ.get("RETRIEVER_EMBEDDING_DEVICE", "cpu"),
        ),
        rerank=RerankConfig(
            enabled=rerank_enabled,
            model_name=(
                os.environ.get("RETRIEVER_RERANK_MODEL", "BAAI/bge-reranker-base")
                if rerank_enabled else ""
            ),
        ),
    )


def _env_flag(name: str) -> bool:
    return os.environ.get(name, "").strip().lower() in {"1", "true", "yes", "on"}
