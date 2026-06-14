from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    manifest = load_json(ROOT / "workflow_manifest.json")
    refs = []
    refs.extend(manifest.get("packs", []))
    refs.extend(manifest.get("global_retrieval_profiles", []))
    refs.extend(manifest.get("global_generation_patterns", []))
    refs.extend(manifest.get("global_validation_rules", []))
    refs.extend(item.get("contract", "") for item in manifest.get("actions", []))
    missing = []
    invalid_json = []
    for rel in refs:
        if not rel:
            continue
        path = ROOT / rel
        if not path.exists():
            missing.append(rel)
            continue
        if path.suffix.lower() == ".json":
            try:
                load_json(path)
            except Exception as exc:
                invalid_json.append({"path": rel, "error": str(exc)})
    report = {
        "checked_refs": len([r for r in refs if r]),
        "missing": missing,
        "invalid_json": invalid_json,
        "status": "pass" if not missing and not invalid_json else "fail",
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())

