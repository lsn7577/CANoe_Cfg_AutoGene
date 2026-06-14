"""MCP server: expose the agent-first retriever to any MCP-compatible agent.

Optional dependency.  The MCP SDK is NOT on PyPI in some environments.
To enable: `pip install mcp` (or install from the modelcontextprotocol repo).

Without the SDK, this module can still be imported and the tool functions
are usable directly from Python (see usage at the bottom).
"""

from __future__ import annotations
import json
import sys
from pathlib import Path
from typing import List, Dict, Any, Optional

try:
    from mcp.server.fastmcp import FastMCP  # type: ignore
    _HAS_MCP = True
except Exception:
    FastMCP = None
    _HAS_MCP = False

from .config import ARTIFACTS_DIR, KNOWLEDGE_DIR, KNOWN_VERSIONS
from .retriever import HybridRetriever
from .ingest import ingest_files, remove_doc


_RETR: Optional[HybridRetriever] = None
_MCP = None


def _get_retr() -> HybridRetriever:
    global _RETR
    if _RETR is None:
        _RETR = HybridRetriever.build_from_disk()
    return _RETR


# ---- Tool implementations (work with or without MCP SDK) ----

def tool_search_canoe(query: str, version: str = "v15",
                      topic: Optional[str] = None,
                      page_type: Optional[str] = None,
                      top_n: int = 5) -> List[Dict[str, Any]]:
    """Search the Vector CANoe knowledge base.

    Args:
        query: Natural-language query or CAPL function name.
        version: "v12" or "v15".
        topic: One of "capl" | "panel" | "dbc" | "xcp" | "extras", or omit for all.
        page_type: Filter by "function" | "method" | "event" | "selector" | "concept".
        top_n: Number of results (default 5).
    """
    if version not in KNOWN_VERSIONS:
        version = "v15"
    return _get_retr().retrieve(query, version=version, topic=topic,
                                page_type=page_type, top_n=top_n)


def tool_canoe_info() -> Dict[str, Any]:
    """Statistics about the current knowledge base indices."""
    return _get_retr().info()


def tool_canoe_add(paths: List[str]) -> Dict[str, Any]:
    """Add new knowledge to the base. Paths are JSON files or directories."""
    return ingest_files([Path(p) for p in paths])


def tool_canoe_remove(doc_id: str) -> Dict[str, int]:
    """Remove a document from both indices by its id."""
    n = remove_doc(doc_id)
    return {"removed": n}


# ---- MCP wiring (only if SDK is available) ----

if _HAS_MCP:
    _MCP = FastMCP("canoe-knowledge-base")

    @_MCP.tool()
    def search_canoe(query: str, version: str = "v15",
                     topic: Optional[str] = None,
                     page_type: Optional[str] = None,
                     top_n: int = 5) -> List[Dict[str, Any]]:
        return tool_search_canoe(query, version, topic, page_type, top_n)

    @_MCP.tool()
    def canoe_info() -> Dict[str, Any]:
        return tool_canoe_info()

    @_MCP.tool()
    def canoe_add(paths: List[str]) -> Dict[str, Any]:
        return tool_canoe_add(paths)

    @_MCP.tool()
    def canoe_remove(doc_id: str) -> Dict[str, int]:
        return tool_canoe_remove(doc_id)

    def main():
        _MCP.run()


if __name__ == "__main__":
    if _HAS_MCP:
        main()
    else:
        print("MCP SDK not installed. Falling back to direct call demo.")
        for q in ["setSignal", "panel gauge binding", "on message"]:
            print(f"\nQ: {q!r}")
            for h in tool_search_canoe(q, top_n=2):
                g = h.get("grounded_facts", {})
                print(f"  - {g.get('source'):60s} {(g.get('description') or '')[:80]}")
