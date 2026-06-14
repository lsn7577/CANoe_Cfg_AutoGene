"""Document preprocessing: scan JSON+MD pairs and build a unified record.

Supports four layouts (auto-detected):

  A. <root>/<version>/<topic>/structured/<sub>/<file>.json        (canonical)
  B. <root>/<version>/<topic>/<file>.json                         (topic-level rollup)
  C. <root>/<topic>/<file>.json                                   (extras / user docs)
  D. <root>/<topic>/<sub>/<file>.json                             (nested extras)

Field-shape aware: CAPL docs store description/syntax/parameters/availability
as LISTS, not strings. We normalise to a single string before embedding.
"""

from __future__ import annotations
import json
import re
from pathlib import Path
from typing import Iterator, Dict, Any, Optional, Iterable

from .config import ROOT, KNOWN_TOPICS, KNOWN_VERSIONS, EXTRAS_DIR, DEFAULT_SUBCATEGORY


# ---------- text normalisation ----------

def _as_text(v):
    """Convert any of str / list / dict into a single clean string."""
    if v is None:
        return ""
    if isinstance(v, str):
        return re.sub(r"\s+", " ", v).strip()
    if isinstance(v, (int, float)):
        return str(v)
    if isinstance(v, list):
        parts = []
        for item in v:
            if item is None:
                continue
            if isinstance(item, (str, int, float)):
                t = _as_text(item)
                if t:
                    parts.append(t)
            elif isinstance(item, dict):
                if "description" in item or "code" in item:
                    parts.append(_as_text(item.get("description", "")))
                    if item.get("code"):
                        parts.append("Code:\n" + _as_text(item["code"]))
                else:
                    parts.append(_as_text(json.dumps(item, ensure_ascii=False)))
            else:
                parts.append(_as_text(str(item)))
        return " ".join(parts).strip()
    if isinstance(v, dict):
        bits = []
        for k in ("description", "code", "title", "name", "text"):
            if k in v:
                bits.append(_as_text(v[k]))
        if not bits:
            bits.append(json.dumps(v, ensure_ascii=False))
        return " ".join(bits).strip()
    return _as_text(str(v))


def _as_code(v):
    """Extract code snippets from example/parameter structures."""
    if v is None:
        return ""
    if isinstance(v, str):
        return v
    if isinstance(v, dict):
        return _as_text(v.get("code", ""))
    if isinstance(v, list):
        return "\n".join(_as_code(x) for x in v if x)
    return _as_text(v)


# ---------- per-page-type embed text ----------

def _build_embed_text(data, page_type):
    name    = _as_text(data.get("name") or data.get("title"))
    desc    = _as_text(data.get("description") or data.get("intro") or data.get("summary"))
    syntax  = _as_text(data.get("syntax"))
    code    = _as_code(data.get("example"))
    body    = _as_text(data.get("body_md") or data.get("content") or data.get("body"))

    if page_type in ("function", "method", "event", "selector"):
        parts = [p for p in (name, desc,
                              ("Syntax: " + syntax) if syntax else "",
                              ("Example: " + code[:400]) if code else "") if p]
        return "\n".join(parts)[:1800]

    if page_type == "notes":
        return (body or desc or name)[:1800]

    base = body or desc or name
    return base[:1800]


# ---------- topic-level rollup enrichment ----------

def _enrich_overview(data):
    if not (isinstance(data.get("functions"), list) and data["functions"]):
        return data
    if data.get("description") or data.get("intro"):
        return data
    cat = data.get("category", data.get("name", ""))
    fns = data["functions"]
    names = [f.get("name", "") for f in fns if isinstance(f, dict)]
    synthesized = (
        (cat or "Overview") + " contains " + str(len(fns))
        + " functions. Members: " + ", ".join(n for n in names if n)[:1500]
    )
    out = dict(data)
    out["description"] = [synthesized]
    return out


# ---------- type inference ----------

def _infer_page_type(data, json_path):
    pt = data.get("page_type") or data.get("type")
    if pt:
        return str(pt).lower()
    if "functions" in data and "function_count" in data:
        return "concept"
    name = json_path.stem.lower()
    if name.startswith("on "):
        return "event"
    if name.endswith("()"):
        return "function"
    return "concept"


# ---------- layout detection ----------

def _classify_layout(parts, root_name):
    if (len(parts) >= 4 and parts[2] == "structured"
            and parts[0] in KNOWN_VERSIONS):
        return {"version": parts[0], "topic": parts[1], "sub": parts[3]}
    if (len(parts) == 3 and parts[0] in KNOWN_VERSIONS
            and parts[1] in KNOWN_TOPICS):
        return {"version": parts[0], "topic": parts[1], "sub": "__overview__"}
    if len(parts) == 2 and parts[0] in KNOWN_TOPICS:
        return {"version": "extras", "topic": parts[0], "sub": "User"}
    if len(parts) >= 3 and parts[0] in KNOWN_TOPICS:
        return {"version": "extras", "topic": parts[0], "sub": parts[1]}
    return {"version": "extras", "topic": "extras",
            "sub": root_name.replace("\\", "/")}


def _doc_id(version, topic, sub, stem):
    return version + "::" + topic + "::" + sub + "::" + stem


def _repo_relative(path: Path) -> str:
    """Return a stable repo-relative path when the source lives in this repo."""
    try:
        path = path.resolve().relative_to(ROOT)
    except ValueError:
        pass
    return path.as_posix()


# ---------- main entry ----------

def iter_documents(roots, require_md=False):
    for root in roots:
        if not root.exists():
            continue
        for json_path in root.rglob("*.json"):
            if json_path.name.startswith("_"):
                continue
            if require_md and not json_path.with_suffix(".md").exists():
                continue
            try:
                data = json.loads(json_path.read_text(encoding="utf-8"))
            except Exception:
                continue

            page_type = _infer_page_type(data, json_path)
            if page_type == "concept" and "function_count" in data:
                data = _enrich_overview(data)

            rel = json_path.relative_to(root)
            meta = _classify_layout(rel.parts, root.name)
            version, topic, sub = meta["version"], meta["topic"], meta["sub"]
            if not sub:
                sub = DEFAULT_SUBCATEGORY.get(page_type, "General")
            name = data.get("name") or data.get("title") or json_path.stem

            yield {
                "id":            _doc_id(version, topic, sub, json_path.stem),
                "name":          name,
                "page_type":     page_type,
                "topic":         topic,
                "version":       version,
                "subcategory":   sub,
                "embed_text":    _build_embed_text(data, page_type),
                "raw_json_path": _repo_relative(json_path),
                "raw_md_path":   _repo_relative(json_path.with_suffix(".md")),
                "raw":           data,
            }


def all_default_roots():
    from .config import KNOWLEDGE_DIR
    return [KNOWLEDGE_DIR, EXTRAS_DIR]


def stats(docs):
    from collections import Counter
    return {
        "by_version": dict(Counter(d["version"]   for d in docs)),
        "by_topic":   dict(Counter(d["topic"]     for d in docs)),
        "by_type":    dict(Counter(d["page_type"] for d in docs)),
    }
