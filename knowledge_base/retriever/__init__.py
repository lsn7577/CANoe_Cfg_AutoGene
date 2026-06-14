"""Agent-first retriever for the Vector CANoe knowledge base.

Default path:
  - BM25 (exact / keyword candidate recall)
  - Structured-field grounding (anti-hallucination)

Optional vector search and reranking are available only when explicitly enabled.
Designed for incremental ingestion: new docs can be added without
rebuilding from scratch.
"""

__version__ = "0.1.0"
