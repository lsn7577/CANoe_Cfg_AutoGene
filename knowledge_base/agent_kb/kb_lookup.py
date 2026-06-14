"""Convenience helpers for agents to read the knowledge base.

Three main functions:
  - resolve_symbol(name)         -> returns the .json file path for a CAPL symbol
  - load_page(name, version)     -> returns the parsed JSON dict for a page
  - search(query, version, ...)  -> uses BM25 candidate retrieval + grounding

Usage:
    cd <knowledge_base>
    python -c "from agent_kb.kb_lookup import resolve_symbol, load_page; \
        p = load_page('setSignal', 'v15'); print(p.get('syntax'), p.get('description'))"
    # or:
    python agent_kb/kb_lookup.py setSignal v15
"""
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT = Path(__file__).resolve().parent.parent
ALIASES_PATH = ROOT / "agent_kb" / "symbol_aliases.json"
SCENARIOS_PATH = ROOT / "agent_kb" / "scenarios.json"
KNOWLEDGE = ROOT / "knowledge"
EXTRAS = ROOT / "extras"

# Lazy-load aliases (5MB JSON)
_ALIASES = None


def _aliases() -> Dict[str, Any]:
    global _ALIASES
    if _ALIASES is None:
        _ALIASES = json.loads(ALIASES_PATH.read_text(encoding="utf-8"))
    return _ALIASES


def resolve_symbol(symbol: str, prefer_version: str = "v15") -> Optional[str]:
    """Return the page id (e.g. 'v15::capl::CAN::BusLoad') for a CAPL symbol.

    Lookup is case-insensitive (normalized).  If `prefer_version` is set and
    the symbol exists in multiple versions, prefer that one.
    """
    a = _aliases()
    norm = "".join(c for c in symbol.lower() if c.isalnum() or c == "_")
    # First try: get all candidate pages and prefer the requested version
    versions_list = a.get("all_versions", {}).get(norm, [])
    if prefer_version:
        for pid in versions_list:
            if pid.startswith(f"{prefer_version}::"):
                return pid
    # Fall back to default normalized resolution
    if norm in a["by_normalized"]:
        return a["by_normalized"][norm]
    if symbol in a["by_canonical"]:
        return a["by_canonical"][symbol]
    if symbol.lower() in a["by_canonical"]:
        return a["by_canonical"][symbol.lower()]
    return None


def _id_to_path(page_id: str) -> Path:
    parts = page_id.split("::")
    if len(parts) == 3 and parts[0] == "extras":
        parts = [parts[0], parts[1], "_root", parts[2]]
    if len(parts) != 4:
        raise ValueError(f"invalid page id: {page_id}")
    ver, topic, sub, name = parts
    if ver == "extras":
        # extras layout: extras/<topic>/<sub>/<name>.json  OR  extras/<topic>/<name>.json
        # Try with sub first, then without
        for candidate in [
            EXTRAS / topic / sub / f"{name}.json",
            EXTRAS / topic / f"{name}.json",
        ]:
            if candidate.exists():
                return candidate
        return EXTRAS / topic / sub / f"{name}.json"  # default
    return KNOWLEDGE / ver / topic / "structured" / sub / f"{name}.json"


def load_page(symbol: str, version: str = "v15") -> Optional[Dict[str, Any]]:
    """Resolve a CAPL symbol to its structured JSON dict, preferring `version`."""
    a = _aliases()
    # First, try the user's preferred version
    if version in KNOWN_VERSIONS:
        norm = "".join(c for c in symbol.lower() if c.isalnum() or c == "_")
        versions_list = a.get("all_versions", {}).get(norm, [])
        for pid in versions_list:
            if pid.startswith(f"{version}::"):
                path = _id_to_path(pid)
                if path.exists():
                    return json.loads(path.read_text(encoding="utf-8"))
    # Fall back to default resolver
    pid = resolve_symbol(symbol, prefer_version=version)
    if pid is None:
        return None
    path = _id_to_path(pid)
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def search(query: str, version: str = "v15", topic: Optional[str] = None,
           page_type: Optional[str] = None, top_n: int = 5) -> List[Dict[str, Any]]:
    """Agent-first retrieval: BM25 candidates plus structured grounding.

    For high-volume agents, prefer load_page() for known symbols (faster, exact).
    Free-form understanding is expected to happen in the calling agent.
    """
    from retriever.retriever import HybridRetriever
    retr = HybridRetriever.build_from_disk()
    return retr.retrieve(query, version=version, topic=topic, page_type=page_type, top_n=top_n)


def match_scenario(query: str) -> List[Dict[str, Any]]:
    """Match a natural-language intent to one or more known test scenarios.

    Returns a list of scenarios sorted by trigger-overlap. Each entry is the
    full scenario dict from scenarios.json.
    """
    if not SCENARIOS_PATH.exists():
        return []
    data = json.loads(SCENARIOS_PATH.read_text(encoding="utf-8"))
    q_lower = query.lower()
    matches = []
    for sc in data.get("scenarios", []):
        score = 0
        for trig in sc.get("intent_triggers", []):
            if trig.lower() in q_lower:
                score += 2
            elif any(w in q_lower for w in trig.lower().split()):
                score += 1
        if score > 0:
            matches.append((score, sc))
    matches.sort(key=lambda x: -x[0])
    return [sc for _, sc in matches]


def load_scenario_pages(scenario: Dict[str, Any], version: str = "v15") -> Dict[str, Any]:
    """Resolve all primary_pages of a scenario into actual page dicts.

    Returns: {"primary": [...], "related": [...], "missing": [page_id, ...]}
    """
    result = {"primary": [], "related": [], "missing": []}
    for pid in scenario.get("primary_pages", []):
        d = _load_page_by_id(pid)
        if d:
            result["primary"].append({"id": pid, "data": d})
        else:
            result["missing"].append(pid)
    for pid in scenario.get("related_pages", []):
        d = _load_page_by_id(pid)
        if d:
            result["related"].append({"id": pid, "data": d})
    return result


def _load_page_by_id(page_id: str) -> Optional[Dict[str, Any]]:
    try:
        path = _id_to_path(page_id)
    except ValueError:
        return None
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


# ---------- CLI ----------

KNOWN_VERSIONS = {"v12", "v15", "v17", "v18"}


def _print_page(data: Dict[str, Any], pid: str) -> None:
    # Force UTF-8 stdout on Windows
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    print(f"=== {pid} ===")
    for k in ("page_type", "syntax", "description", "parameters", "return", "example", "availability"):
        v = data.get(k)
        if v:
            s = str(v)[:600]
            print(f"  {k}: {s}")


def main(argv: List[str]) -> int:
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    if len(argv) >= 2 and argv[0] == "search":
        q = argv[1]
        ver = argv[2] if len(argv) > 2 else "v15"
        hits = search(q, version=ver, top_n=5)
        for h in hits:
            g = h.get("grounded_facts", {})
            print(f"  [{h.get('id')}]  {g.get('name')}  ({g.get('page_type')})")
            print(f"     {g.get('description', '')[:120]}")
        return 0
    # symbol lookup
    sym = argv[0]
    ver = argv[1] if len(argv) > 1 else "v15"
    pid = resolve_symbol(sym, prefer_version=ver)
    if not pid:
        print(f"NOT FOUND: {sym}")
        return 1
    print(f"Resolved {sym!r} -> {pid}")
    data = load_page(sym, version=ver)
    if data is None:
        print(f"  (file not found at expected path)")
        return 1
    _print_page(data, pid)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
