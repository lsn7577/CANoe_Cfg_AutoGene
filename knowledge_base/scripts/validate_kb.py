"""Validate the knowledge base and agent-facing indexes.

Usage:
    python scripts/validate_kb.py
    python scripts/validate_kb.py --no-write
"""

from __future__ import annotations

import argparse
import json
import os
from collections import Counter
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple


ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = ROOT / "knowledge"
EXTRAS = ROOT / "extras"
AGENT_KB = ROOT / "agent_kb"
REPORT = ROOT / "tests_integration" / "kb_validation_report.json"

PAGE_TYPES = {"function", "method", "event", "selector", "concept", "notes"}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def iter_page_files() -> Iterable[Path]:
    if KNOWLEDGE.exists():
        for dirpath, dirnames, filenames in os.walk(KNOWLEDGE):
            dirnames[:] = [d for d in dirnames if not d.startswith(".")]
            if "structured" not in Path(dirpath).parts:
                continue
            for filename in filenames:
                if filename.endswith(".json") and not filename.startswith("_"):
                    yield Path(dirpath) / filename
    if EXTRAS.exists():
        for dirpath, dirnames, filenames in os.walk(EXTRAS):
            dirnames[:] = [d for d in dirnames if not d.startswith(".")]
            for filename in filenames:
                if filename.endswith(".json") and not filename.startswith("_"):
                    yield Path(dirpath) / filename


def page_id_to_path(page_id: str) -> Path | None:
    parts = page_id.split("::")
    if len(parts) == 3 and parts[0] == "extras":
        parts = [parts[0], parts[1], "_root", parts[2]]
    if len(parts) != 4:
        return None
    ver, topic, sub, name = parts
    if ver == "extras":
        candidates = [
            EXTRAS / topic / sub / f"{name}.json",
            EXTRAS / topic / f"{name}.json",
        ]
    else:
        candidates = [KNOWLEDGE / ver / topic / "structured" / sub / f"{name}.json"]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return candidates[0]


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


def validate_pages() -> Tuple[Dict[str, Any], List[Dict[str, str]], List[Dict[str, str]]]:
    errors: List[Dict[str, str]] = []
    warnings: List[Dict[str, str]] = []
    counts = Counter()
    coverage = Counter()
    by_version_topic = Counter()

    for path in iter_page_files():
        rel = path.relative_to(ROOT).as_posix()
        try:
            data = load_json(path)
        except Exception as exc:
            errors.append({"path": rel, "issue": f"invalid_json: {exc}"})
            continue
        if not isinstance(data, dict):
            errors.append({"path": rel, "issue": "page is not a JSON object"})
            continue

        page_type = str(data.get("page_type") or data.get("type") or "").lower()
        if page_type not in PAGE_TYPES:
            errors.append({"path": rel, "issue": f"invalid page_type: {page_type!r}"})
        if not has_text(data.get("name") or data.get("title")):
            errors.append({"path": rel, "issue": "missing name/title"})

        counts[page_type or "missing"] += 1
        parts = path.relative_to(ROOT).parts
        if len(parts) >= 3:
            by_version_topic["/".join(parts[:3])] += 1

        for field in (
            "syntax", "description", "parameters", "return", "example",
            "availability", "sections", "selectors", "property_references",
        ):
            if has_text(data.get(field)):
                coverage[field] += 1

        if page_type in {"function", "method"} and not has_text(data.get("syntax")):
            warnings.append({"path": rel, "issue": "function/method has no syntax"})
        if page_type == "selector" and not has_text(data.get("selectors")):
            warnings.append({"path": rel, "issue": "selector has no selectors"})

    total = sum(counts.values())
    cov_pct = {
        field: round(n / total * 100, 1) if total else 0.0
        for field, n in sorted(coverage.items())
    }
    summary = {
        "total_pages": total,
        "by_page_type": dict(counts),
        "coverage_pct": cov_pct,
        "by_version_topic_sample": dict(by_version_topic.most_common(20)),
    }
    return summary, errors, warnings


def validate_agent_indexes() -> Tuple[Dict[str, Any], List[Dict[str, str]], List[Dict[str, str]]]:
    errors: List[Dict[str, str]] = []
    warnings: List[Dict[str, str]] = []
    summary: Dict[str, Any] = {}

    unified_path = AGENT_KB / "unified_index.json"
    alias_path = AGENT_KB / "symbol_aliases.json"
    scenarios_path = AGENT_KB / "scenarios.json"

    page_ids = set()
    if unified_path.exists():
        unified = load_json(unified_path)
        pages = unified.get("pages", [])
        page_ids = {p.get("id") for p in pages if p.get("id")}
        missing_paths = []
        for p in pages:
            rel = p.get("path")
            if rel and not (ROOT / rel).exists():
                missing_paths.append(p.get("id", rel))
        if missing_paths:
            errors.append({"path": str(unified_path.relative_to(ROOT)), "issue": f"missing page paths: {missing_paths[:10]}"})
        summary["unified_pages"] = len(pages)
    else:
        errors.append({"path": "agent_kb/unified_index.json", "issue": "missing"})

    if alias_path.exists():
        aliases = load_json(alias_path)
        bad_aliases = []
        for section in ("by_normalized", "by_canonical"):
            for key, page_id in (aliases.get(section) or {}).items():
                if page_id not in page_ids:
                    bad_aliases.append(f"{section}:{key}->{page_id}")
                    if len(bad_aliases) >= 10:
                        break
            if len(bad_aliases) >= 10:
                break
        if bad_aliases:
            errors.append({"path": "agent_kb/symbol_aliases.json", "issue": f"aliases point to missing ids: {bad_aliases}"})
        summary["aliases_normalized"] = len(aliases.get("by_normalized") or {})
    else:
        errors.append({"path": "agent_kb/symbol_aliases.json", "issue": "missing"})

    if scenarios_path.exists():
        scenarios = load_json(scenarios_path).get("scenarios", [])
        missing_refs = []
        for scenario in scenarios:
            for field in ("primary_pages", "related_pages"):
                for ref in scenario.get(field) or []:
                    if ref.startswith("L3_diffs/"):
                        if not (ROOT / ref).exists():
                            missing_refs.append(f"{scenario.get('id')}:{ref}")
                        continue
                    path = page_id_to_path(ref)
                    if path is None or not path.exists():
                        missing_refs.append(f"{scenario.get('id')}:{ref}")
        if missing_refs:
            errors.append({"path": "agent_kb/scenarios.json", "issue": f"missing refs: {missing_refs[:10]}"})
        summary["scenarios"] = len(scenarios)
    else:
        warnings.append({"path": "agent_kb/scenarios.json", "issue": "missing"})

    return summary, errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-write", action="store_true", help="Do not write the JSON report")
    parser.add_argument("--report", default=str(REPORT), help="Report output path")
    args = parser.parse_args()

    page_summary, page_errors, page_warnings = validate_pages()
    index_summary, index_errors, index_warnings = validate_agent_indexes()
    errors = page_errors + index_errors
    warnings = page_warnings + index_warnings
    report = {
        "metadata": {
            "title": "Knowledge Base Validation Report",
            "schema_version": "1.0",
        },
        "summary": {
            "pages": page_summary,
            "agent_indexes": index_summary,
            "errors": len(errors),
            "warnings": len(warnings),
            "overall": "PASS" if not errors else "FAIL",
        },
        "errors": errors,
        "warnings": warnings[:200],
    }

    print(json.dumps(report["summary"], indent=2, ensure_ascii=False))
    if not args.no_write:
        out = Path(args.report)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"Report written to {out.relative_to(ROOT)}")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
