"""Structured-field grounding: pull canonical facts from the source JSON
so the LLM sees ground truth (not embedding-space approximations)."""

from __future__ import annotations
import json
from pathlib import Path
from typing import Dict, Any, List
import re


def _as_text(v) -> str:
    if v is None:
        return ""
    if isinstance(v, str):
        return v.strip()
    if isinstance(v, list):
        return " ".join(str(x) for x in v if x).strip()
    if isinstance(v, dict):
        return json.dumps(v, ensure_ascii=False)
    return str(v)


def _as_code(v) -> str:
    if v is None:
        return ""
    if isinstance(v, str):
        return v
    if isinstance(v, dict):
        return _as_text(v.get("code", ""))
    if isinstance(v, list):
        return "\n".join(_as_code(x) for x in v if x)
    return _as_text(v)


def _limit(text: str, n: int) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    return text[:n]


def _table_text(table: Any) -> str:
    rows = []
    if not isinstance(table, list):
        return _as_text(table)
    for row in table:
        if isinstance(row, list):
            rows.append(" | ".join(_as_text(c) for c in row))
        else:
            rows.append(_as_text(row))
    return " ; ".join(r for r in rows if r)


def _sections_text(raw: Dict[str, Any], limit: int = 1400) -> str:
    parts: List[str] = []
    for sec in raw.get("sections") or []:
        if not isinstance(sec, dict):
            continue
        heading = sec.get("heading")
        if heading:
            parts.append(str(heading))
        content = sec.get("content") or {}
        for p in content.get("paragraphs") or []:
            parts.append(_as_text(p))
        for t in content.get("tables") or []:
            parts.append(_table_text(t))
        for code in content.get("code_blocks") or []:
            parts.append(_as_code(code))
        if len(" ".join(parts)) >= limit:
            break
    return _limit(" ".join(p for p in parts if p), limit)


def _top_tables_text(raw: Dict[str, Any], limit: int = 1000) -> str:
    parts = []
    for key in ("tables", "intro_tables"):
        for table in raw.get(key) or []:
            parts.append(_table_text(table))
            if len(" ".join(parts)) >= limit:
                return _limit(" ".join(parts), limit)
    return _limit(" ".join(parts), limit)


def _return_type_from_syntax(raw: Dict[str, Any]) -> str:
    syntax = raw.get("syntax")
    if not isinstance(syntax, list) or not syntax:
        return ""
    first = str(syntax[0]).strip()
    m = re.match(r"^([A-Za-z_][\w:\s\*&<>]*?)\s+[A-Za-z_]\w*\s*\(", first)
    if not m:
        return ""
    value = m.group(1).strip()
    return "" if value.lower() in {"if", "for", "while", "switch"} else value


def extract_facts(raw: Dict[str, Any], doc: Dict[str, Any]) -> Dict[str, Any]:
    """Pick only the fields that are safe for LLM consumption."""
    return_type = _as_text(raw.get("return")) or _return_type_from_syntax(raw)
    return {
        "name":         raw.get("name") or raw.get("title"),
        "page_type":    raw.get("page_type") or doc.get("page_type"),
        "syntax":       _as_text(raw.get("syntax"))[:600],
        "parameters":   _as_text(raw.get("parameters"))[:600],
        "return":       _as_text(raw.get("return"))[:400],
        "return_type_inferred": return_type[:120],
        "description":  _as_text(raw.get("description") or
                                  raw.get("intro") or
                                  raw.get("summary"))[:800],
        "sections":     _sections_text(raw),
        "tables":       _top_tables_text(raw),
        "selectors":    _as_text(raw.get("selectors"))[:1000],
        "property_references": _as_text(raw.get("property_references"))[:1000],
        "example_code": _as_code(raw.get("example"))[:800],
        "availability": _as_text(raw.get("availability"))[:200],
        "source":       (doc.get("version", "") + "/" + doc.get("topic", "")
                         + "/" + doc.get("subcategory", "")
                         + "/" + doc.get("name", "")),
    }


class Grounding:
    """Resolves a hit's `raw_json_path` and returns grounded facts."""

    def __init__(self, knowledge_dir: Path):
        self.root = knowledge_dir

    def _resolve_raw_path(self, raw_json_path: str) -> Path:
        raw_path = Path(raw_json_path or "")
        if raw_path.is_absolute():
            return raw_path
        candidates = [
            self.root / raw_path,
            self.root / "knowledge" / raw_path,
            self.root / "extras" / raw_path,
        ]
        for candidate in candidates:
            if candidate.exists():
                return candidate
        return candidates[0]

    def ground(self, doc: Dict[str, Any]) -> Dict[str, Any]:
        raw_path = self._resolve_raw_path(doc.get("raw_json_path", ""))
        if not raw_path.exists():
            doc["grounded_facts"] = extract_facts(doc.get("raw") or {}, doc)
            return doc
        try:
            raw = json.loads(raw_path.read_text(encoding="utf-8"))
        except Exception:
            raw = doc.get("raw") or {}
        doc["grounded_facts"] = extract_facts(raw, doc)
        return doc
