from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple


ROOT = Path(__file__).resolve().parents[2]
WORKFLOW_DIR = Path(__file__).resolve().parent
PROFILE_PATH = WORKFLOW_DIR / "workflow_profile.json"

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from workflows.canoe_auto_generation_burr import canoe_workflow  # noqa: E402


def _load_profile() -> Dict[str, Any]:
    return json.loads(PROFILE_PATH.read_text(encoding="utf-8"))


def _profile_transitions(profile: Dict[str, Any]) -> List[Tuple[str, str, str]]:
    out = []
    for item in profile.get("transitions", []):
        source = item[0]
        target = item[1]
        condition = item[2] if len(item) > 2 else ""
        out.append((source, target, condition))
    return out


def _code_transitions() -> List[Tuple[str, str, str]]:
    return [
        (source, target, condition or "")
        for source, target, condition in canoe_workflow.TRANSITION_SPECS
    ]


def main() -> int:
    profile = _load_profile()
    profile_actions = {item.get("id") for item in profile.get("actions", [])}
    code_actions = set(canoe_workflow.ACTION_REGISTRY.keys())
    missing_in_code = sorted(profile_actions - code_actions)
    missing_in_profile = sorted(code_actions - profile_actions)

    profile_transition_set = set(_profile_transitions(profile))
    code_transition_set = set(_code_transitions())
    transition_missing_in_code = sorted(profile_transition_set - code_transition_set)
    transition_missing_in_profile = sorted(code_transition_set - profile_transition_set)

    dangling_transition_actions = sorted({
        action
        for transition in profile_transition_set
        for action in transition[:2]
        if action not in code_actions
    })
    report = {
        "profile": str(PROFILE_PATH),
        "action_count": len(code_actions),
        "transition_count": len(code_transition_set),
        "missing_in_code": missing_in_code,
        "missing_in_profile": missing_in_profile,
        "transition_missing_in_code": transition_missing_in_code,
        "transition_missing_in_profile": transition_missing_in_profile,
        "dangling_transition_actions": dangling_transition_actions,
        "status": "pass",
    }
    if any(report[key] for key in [
        "missing_in_code",
        "missing_in_profile",
        "transition_missing_in_code",
        "transition_missing_in_profile",
        "dangling_transition_actions",
    ]):
        report["status"] = "fail"
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
