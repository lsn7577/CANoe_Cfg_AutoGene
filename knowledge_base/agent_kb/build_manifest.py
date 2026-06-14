"""Build the agent-facing artifacts in this directory.

This script regenerates:
  - unified_index.json   : every page -> {topic, version, path, type, summary}
  - symbol_aliases.json  : CAPL function/method/event name -> page id
  - capability_manifest.md stats (the constants in it are also computed here)

Re-run after any change to knowledge/ or extras/ to keep views in sync.
Usage:
    cd <knowledge_base>
    python agent_kb/build_manifest.py
"""
import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Any

# Repo layout
ROOT = Path(__file__).resolve().parent.parent
KNOWLEDGE = ROOT / "knowledge"
EXTRAS = ROOT / "extras"
AGENT_KB = ROOT / "agent_kb"

# Known topic slugs at the top level
KNOWN_TOPICS = {"capl", "panel", "dbc", "xcp", "diagnostics"}
KNOWN_VERSIONS = {"v12", "v15", "v17", "v18"}


def display_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def walk_pages() -> List[Dict[str, Any]]:
    """Yield one record per page across the entire corpus (knowledge/ + extras/)."""
    pages = []
    # knowledge/<version>/<topic>/structured/<sub>/<name>.json
    for ver_dir in sorted(KNOWLEDGE.iterdir()):
        if not ver_dir.is_dir() or ver_dir.name.startswith("_") or ver_dir.name.startswith("."):
            continue
        ver = ver_dir.name
        if ver not in KNOWN_VERSIONS and ver != "latest":
            continue
        for topic_dir in sorted(ver_dir.iterdir()):
            if not topic_dir.is_dir():
                continue
            topic = topic_dir.name
            struct = topic_dir / "structured"
            if not struct.is_dir():
                continue
            for sub_dir in sorted(struct.iterdir()):
                if not sub_dir.is_dir():
                    continue
                sub = sub_dir.name
                for fp in sorted(sub_dir.iterdir()):
                    if fp.suffix != ".json" or fp.name.startswith("_"):
                        continue
                    pages.append(_build_page_record(ver, topic, sub, fp))
    # extras/<topic>/<sub>/<name>.json  OR  extras/<topic>/<name>.json
    for topic_dir in sorted(EXTRAS.iterdir()):
        if not topic_dir.is_dir():
            continue
        topic = topic_dir.name
        for fp in sorted(topic_dir.rglob("*.json")):
            if fp.name.startswith("_"):
                continue
            rel = fp.relative_to(topic_dir)
            sub = rel.parts[0] if len(rel.parts) > 1 else "_root"
            pages.append(_build_page_record("extras", topic, sub, fp))
    return pages


def _build_page_record(ver, topic, sub, fp: Path) -> Dict[str, Any]:
    try:
        data = json.loads(fp.read_text(encoding="utf-8"))
    except Exception:
        data = {}
    name = data.get("name") or data.get("title") or fp.stem
    page_type = _infer_page_type(data, fp)
    summary = _summarize(data)
    # Use file stem as alias_name (often more stable than JSON's "name" field
    # which can be set differently per pipeline run).
    alias_name = fp.stem
    return {
        "id": f"{ver}::{topic}::{sub}::{fp.stem}",
        "name": name,
        "alias_name": alias_name,
        "page_type": page_type,
        "topic": topic,
        "version": ver,
        "subcategory": sub,
        "path": str(fp.relative_to(ROOT)),
        "md_path": str((fp.with_suffix(".md")).relative_to(ROOT)) if fp.with_suffix(".md").exists() else None,
        "summary": summary,
        "syntax_first": _syntax_first(data),
        "source_kind": "extracted" if (ver in KNOWN_VERSIONS and topic in KNOWN_TOPICS)
                       else ("synthetic" if "synthetic" in (data.get("source") or "") else "hand_curated"),
    }


def _infer_page_type(data: Dict[str, Any], fp: Path) -> str:
    """Better page type inference: handles v15 mis-classification of selectors/overviews."""
    declared = (data.get("page_type") or "").lower()
    name = (data.get("name") or data.get("title") or fp.stem).strip()
    name_lower = name.lower()
    syntax = data.get("syntax")
    has_syntax = isinstance(syntax, list) and len(syntax) > 0

    # 1. Event pages: title starts with "on "
    if name_lower.startswith("on "):
        return "event"

    # 2. Concept: topic is panel/dbc (these are always concept pages in v15)
    #    Plus the topic-level rollup has page_type=concept+function_count (we leave it)

    # 3. Selector page heuristics: name contains "Selector" or "Selectors"
    if "selector" in name_lower and not has_syntax:
        return "selector"

    # 4. Function page: has actual syntax (not empty list)
    if has_syntax and not name_lower.endswith("functions"):
        return "function"

    # 5. Method: rare in our corpus; declared as method
    if declared == "method":
        return "method"

    # 6. Trust declared type otherwise
    if declared in ("function", "method", "event", "selector", "concept", "notes"):
        return declared

    # 7. Default
    return "notes"


def _infer_type_from_name(stem: str) -> str:
    if stem.lower().startswith("on "):
        return "event"
    return "concept"


def _syntax_first(data: Dict[str, Any]) -> str:
    s = data.get("syntax")
    if isinstance(s, list) and s:
        return s[0][:200]
    return ""


def _summarize(data: Dict[str, Any]) -> str:
    """Generate a one-line summary from the most informative field."""
    for f in ("description", "intro"):
        v = data.get(f)
        if isinstance(v, list) and v:
            return " ".join(v)[:240]
        if isinstance(v, str) and v:
            return v[:240]
    s = data.get("syntax")
    if isinstance(s, list) and s:
        return s[0][:240]
    if data.get("sections"):
        secs = data["sections"]
        for s in secs:
            ps = s.get("content", {}).get("paragraphs", [])
            if ps:
                return ps[0][:240]
    return ""


# ---------- alias extraction ----------

_NAME_NORMALIZE_RE = re.compile(r"[^a-zA-Z0-9_]+")


def _normalize_name(s: str) -> str:
    return _NAME_NORMALIZE_RE.sub("", s or "").lower()


def build_symbol_aliases(pages: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Build a multi-faceted symbol lookup.

    Output schema:
      {
        "metadata": {...},
        "by_normalized": { "setsignal": "v15::capl::...", ... },
        "by_canonical": { "setSignal": "v15::capl::...", ... },
        "all_versions": { "setsignal": ["v12::...", "v15::..."], ... }
      }

    The "canonical" map uses the original casing from the source name (e.g. "setSignal").
    "by_normalized" lowercases + strips separators so lookups are case-insensitive.
    "all_versions" lists every page that matches a name (for cross-version queries).
    """
    # 1. Pass: collect all candidates
    by_norm: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    by_canon: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for p in pages:
        # Accept CAPL, XCP, diagnostics, AND team (extras/team/).
        # Also any topic that starts with "extras" (defensive).
        if p["topic"] not in ("capl", "xcp", "diagnostics", "team", "extras") and \
           not p.get("id", "").startswith("extras::"):
            continue
        # Use alias_name (file stem) preferentially - it's stable across pipeline runs
        # and matches what users will typically look up.
        n = p.get("alias_name") or p["name"]
        if not n:
            continue
        # Skip overview/list pages: their name usually contains "Functions" or "Overview" at end
        # - but we KEEP selector pages (e.g. "CAN Message Selectors") because they're queryable.
        nl = n.lower().strip()
        if (nl.endswith("functions") and " " in nl) or \
           nl.endswith("overview") or \
           nl == "new features" or \
           nl == "glossary":
            continue
        norm = _normalize_name(n)
        if not norm or len(norm) < 2:
            continue
        by_norm[norm].append(p)
        # canonical key keeps original casing (file stem keeps its canonical form)
        by_canon[n].append(p)
        # Also key by the lowercased original (for case-insensitive exact match)
        by_canon.setdefault(nl, []).append(p)
        # And key by the JSON's name field (in case it differs and is what users know)
        if p["name"] and p["name"] != n:
            by_norm.setdefault(_normalize_name(p["name"]), []).append(p)
            by_canon.setdefault(p["name"], []).append(p)
            by_canon.setdefault(p["name"].lower(), []).append(p)

    # 2. Pick best candidate for each
    def _pick(candidates: List[Dict[str, Any]]) -> str:
        # Prefer function/method/event over concept/notes/selector
        # Prefer v15 over v12 over v17 over v18 (latest stable is v15)
        # Prefer extras last
        def score(p):
            pt_score = {"function": 0, "method": 0, "event": 0, "selector": 1, "concept": 2, "notes": 3}.get(p["page_type"], 9)
            ver_score = -_ver_rank(p["version"])  # negate so higher version = lower number = preferred
            return (pt_score, ver_score)
        return sorted(candidates, key=score)[0]["id"]

    by_normalized = {k: _pick(v) for k, v in by_norm.items()}
    by_canonical = {k: _pick(v) for k, v in by_canon.items()}
    all_versions = {k: [p["id"] for p in v] for k, v in by_norm.items()}

    return {
        "metadata": {
            "title": "CAPL Symbol → Page Aliases",
            "generated_at": _now(),
            "schema_version": "3.0",
            "n_normalized": len(by_normalized),
            "n_canonical": len(by_canonical),
            "notes": "by_normalized: case-insensitive lookup. by_canonical: case-sensitive original. all_versions: every match (for cross-version diff).",
        },
        "by_normalized": by_normalized,
        "by_canonical": by_canonical,
        "all_versions": all_versions,
    }


def _ver_rank(v: str) -> int:
    return {"v18": 4, "v17": 3, "v15": 2, "v12": 1, "extras": 0}.get(v, -1)


def _get_page_type_for_id(pages, page_id: str) -> str:
    for p in pages:
        if p["id"] == page_id:
            return p["page_type"]
    return ""


# ---------- unified index builder ----------

def build_unified_index(pages: List[Dict[str, Any]]) -> Dict[str, Any]:
    by_topic = defaultdict(int)
    by_version = defaultdict(int)
    by_type = defaultdict(int)
    by_vt = defaultdict(int)
    for p in pages:
        by_topic[p["topic"]] += 1
        by_version[p["version"]] += 1
        by_type[p["page_type"]] += 1
        by_vt[f"{p['version']}::{p['topic']}"] += 1
    return {
        "metadata": {
            "title": "Unified Page Index (agent-facing)",
            "generated_at": _now(),
            "schema_version": "3.0",
            "total_pages": len(pages),
            "by_topic": dict(by_topic),
            "by_version": dict(by_version),
            "by_type": dict(by_type),
            "by_version_topic": dict(by_vt),
        },
        "pages": pages,
    }


def _now() -> str:
    import datetime
    return datetime.datetime.now().isoformat(timespec="seconds")


# ---------- stats for the manifest ----------

def compute_stats(pages: List[Dict[str, Any]]) -> Dict[str, Any]:
    by_vt = defaultdict(lambda: defaultdict(int))
    capl_cats = defaultdict(lambda: defaultdict(int))
    panel_cats = defaultdict(lambda: defaultdict(int))
    dbc_cats = defaultdict(lambda: defaultdict(int))
    for p in pages:
        by_vt[p["version"]][p["topic"]] += 1
        if p["topic"] == "capl":
            capl_cats[p["version"]][p["subcategory"]] += 1
        elif p["topic"] == "panel":
            panel_cats[p["version"]][p["subcategory"]] += 1
        elif p["topic"] == "dbc":
            dbc_cats[p["version"]][p["subcategory"]] += 1
    return {
        "by_version_topic": {v: dict(d) for v, d in by_vt.items()},
        "capl_cats": {v: dict(d) for v, d in capl_cats.items()},
        "panel_cats": {v: dict(d) for v, d in panel_cats.items()},
        "dbc_cats": {v: dict(d) for v, d in dbc_cats.items()},
    }


# ---------- main ----------

def main():
    print(f"[agent_kb] scanning {display_path(KNOWLEDGE)} + {display_path(EXTRAS)} ...")
    pages = walk_pages()
    print(f"[agent_kb] discovered {len(pages)} pages")

    # Unified index
    ui = build_unified_index(pages)
    ui_path = AGENT_KB / "unified_index.json"
    ui_path.write_text(json.dumps(ui, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[agent_kb] wrote {display_path(ui_path)} ({ui_path.stat().st_size // 1024} KB)")

    # Symbol aliases
    aliases = build_symbol_aliases(pages)
    alias_path = AGENT_KB / "symbol_aliases.json"
    alias_path.write_text(json.dumps(aliases, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[agent_kb] wrote {display_path(alias_path)} ({aliases['metadata']['n_normalized']} normalized, {aliases['metadata']['n_canonical']} canonical, {alias_path.stat().st_size // 1024} KB)")

    # Stats (for capability_manifest.md)
    stats = compute_stats(pages)
    stats_path = AGENT_KB / "_stats.json"
    stats_path.write_text(json.dumps(stats, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[agent_kb] wrote {display_path(stats_path)}")
    print(f"[agent_kb] by_version_topic: {stats['by_version_topic']}")


if __name__ == "__main__":
    main()
