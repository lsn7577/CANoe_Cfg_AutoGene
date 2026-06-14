"""Normalize known corpus quality risks in generated JSON pages.

This is intentionally conservative:
- CHM `source` values are made relative to the CHM extract root.
- Pages declared as function/method but shaped like overview/reference pages
  are reclassified as concept.
- Callable pages with missing syntax get an inferred syntax plus a
  `syntax_status` marker so consumers do not treat it as vendor-authored text.
"""

from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_ROOTS = (ROOT / "knowledge", ROOT / "extras")

CONCEPT_LIKE_RE = re.compile(
    r"(functions?|error codes?|selectors?|overview|classes?|class_|"
    r"enumeration|structs?|return values?|events? of|technical details|"
    r"socket options|concepts?|references|constants|access types|data types|"
    r"output level|message id|map window api|interaction layer|node layer|"
    r"test service library|specific language limitations|hardware configuration|"
    r"database support|input assistance|initialization|general tips|"
    r"symbolic identification|procedure|access mode|event handlers|"
    r"descriptions|properties|formats|states|examples?|differences|"
    r"requirements|creating|definition|declaration|reconfigure|scheduling|"
    r"unconditional|string literal|keyword|event procedure|event types|"
    r"media source|media sink|media property|checked objects|high observer|"
    r"access pgns|access multiple|define parameter groups|major media types|"
    r"stimulus generator|data source|syntax for|status)",
    re.IGNORECASE,
)


def iter_json_files(roots: Iterable[Path]) -> Iterable[Path]:
    for root in roots:
        if not root.exists():
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if not d.startswith(".")]
            for filename in filenames:
                if filename.endswith(".json"):
                    yield Path(dirpath) / filename


def has_text(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, list):
        return any(has_text(v) for v in value)
    if isinstance(value, dict):
        return any(has_text(v) for v in value.values())
    return True


def as_code(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        return as_code(value.get("code"))
    if isinstance(value, list):
        return "\n".join(as_code(v) for v in value if v)
    return str(value)


def normalize_source(value: Any) -> Tuple[Any, bool]:
    if not isinstance(value, str) or not value:
        return value, False
    normalized = value.replace("\\", "/")
    match = re.search(r"(chm_extract(?:_v\d+)?/.*)$", normalized, re.IGNORECASE)
    if match:
        normalized = match.group(1)
    else:
        normalized = re.sub(r"^[A-Za-z]:/+", "", normalized)
    return normalized, normalized != value


def normalize_source_fields(value: Any) -> Tuple[Any, int]:
    if isinstance(value, dict):
        changed = 0
        out = dict(value)
        for key, child in value.items():
            if key == "source":
                normalized, did_change = normalize_source(child)
                out[key] = normalized
                changed += int(did_change)
            else:
                normalized, child_changes = normalize_source_fields(child)
                out[key] = normalized
                changed += child_changes
        return out, changed
    if isinstance(value, list):
        changed = 0
        out = []
        for child in value:
            normalized, child_changes = normalize_source_fields(child)
            out.append(normalized)
            changed += child_changes
        return out, changed
    return value, 0


def is_concept_like(data: Dict[str, Any], path: Path) -> bool:
    name = str(data.get("name") or data.get("title") or path.stem)
    haystack = f"{name} {path.stem}"
    source = str(data.get("source") or "").replace("\\", "/").lower()
    if "/properties/" in source or "/concept" in source:
        return True
    return bool(CONCEPT_LIKE_RE.search(haystack))


def split_names(name: str) -> List[str]:
    parts = [p.strip() for p in re.split(r",|\bor\b", name) if p.strip()]
    return parts or [name.strip()]


def infer_syntax(data: Dict[str, Any], path: Path) -> Tuple[List[str], str]:
    name = str(data.get("name") or data.get("title") or path.stem).strip()
    if not name:
        return [], ""
    if name.lower().startswith("on "):
        return [name + " { ... }"], "inferred_event_name"

    code = as_code(data.get("example"))
    inferred: List[str] = []
    for candidate in split_names(name):
        if not re.match(r"^[A-Za-z_][A-Za-z0-9_]*$", candidate):
            continue
        pattern = re.compile(
            r"((?:[A-Za-z_][A-Za-z0-9_]*\s*\.\s*)?"
            + re.escape(candidate)
            + r"\s*\([^;\n{}]*\))",
            re.MULTILINE,
        )
        for match in pattern.finditer(code):
            syntax = re.sub(r"\s+", " ", match.group(1)).strip()
            if syntax and not syntax.endswith(";"):
                syntax += ";"
            if syntax and syntax not in inferred:
                inferred.append(syntax)
        if inferred:
            return inferred[:3], "inferred_from_example"

    params = data.get("parameters")
    if isinstance(params, list) and params:
        names = []
        for param in params:
            if isinstance(param, dict) and param.get("name"):
                names.append(str(param["name"]))
        if names:
            return [f"{name}({', '.join(names)});"], "inferred_from_parameters"

    if re.match(r"^[A-Za-z_][A-Za-z0-9_:]*(?:, [A-Za-z_][A-Za-z0-9_:]*)*$", name):
        return [f"{candidate}(...);" for candidate in split_names(name)], "placeholder_from_name"
    return [], ""


def normalize_page(path: Path, dry_run: bool = False) -> Tuple[bool, Dict[str, int]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        return False, {}

    changed = False
    stats = {"source": 0, "reclassified": 0, "syntax": 0, "unresolved": 0}

    normalized_data, source_changes = normalize_source_fields(data)
    if source_changes:
        data = normalized_data
        changed = True
        stats["source"] += source_changes

    page_type = str(data.get("page_type") or data.get("type") or "").lower()
    if page_type in {"function", "method"} and not has_text(data.get("syntax")):
        if is_concept_like(data, path):
            data.setdefault("original_page_type", page_type)
            data["page_type"] = "concept"
            changed = True
            stats["reclassified"] += 1
        else:
            syntax, status = infer_syntax(data, path)
            if syntax:
                data["syntax"] = syntax
                data["syntax_status"] = status
                changed = True
                stats["syntax"] += 1
            else:
                stats["unresolved"] += 1

    if changed and not dry_run:
        path.write_text(
            json.dumps(data, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    return changed, stats


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    totals = {"files": 0, "source": 0, "reclassified": 0, "syntax": 0, "unresolved": 0}
    unresolved_samples = []
    for path in iter_json_files(DEFAULT_ROOTS):
        try:
            changed, stats = normalize_page(path, dry_run=args.dry_run)
        except Exception:
            continue
        if changed:
            totals["files"] += 1
            for key in ("source", "reclassified", "syntax", "unresolved"):
                totals[key] += stats.get(key, 0)
        elif stats.get("unresolved"):
            totals["unresolved"] += stats["unresolved"]
        if stats.get("unresolved") and len(unresolved_samples) < 40:
            unresolved_samples.append(path.relative_to(ROOT).as_posix())
    print(json.dumps({
        "totals": totals,
        "unresolved_samples": unresolved_samples,
    }, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
