"""Action contract synchronisation and validation for CANoe_Gene.

This module validates consistency across the three sources of action contract
information:

1. ``knowledge_base/workflow_kb/burr_actions/*.json`` — declarative action contracts
2. ``workflows/canoe_auto_generation_burr/workflow_profile.json`` — executable workflow profile
3. ``canoe_workflow.ACTION_REGISTRY`` / ``TRANSITION_SPECS`` — Python implementation

The long-term goal is to make ``burr_actions/*.json`` the single source of
truth and auto-generate the other two.  This module provides the validation
infrastructure and mapping table to move towards that goal incrementally.

Usage::

    python -m workflows.canoe_auto_generation_burr.action_contract_sync
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple


ROOT = Path(__file__).resolve().parents[2]
WORKFLOW_DIR = Path(__file__).resolve().parent
WORKFLOW_KB_DIR = ROOT / "knowledge_base" / "workflow_kb"
BURR_ACTIONS_DIR = WORKFLOW_KB_DIR / "burr_actions"
PROFILE_PATH = WORKFLOW_DIR / "workflow_profile.json"

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# -- Mapping: burr_action ID -> ACTION_REGISTRY key(s) --
# This table documents the relationship between the high-level burr_actions
# contracts and the actual Python action implementations.  As the codebase
# evolves, this mapping should be kept in sync.
BURR_ACTION_TO_REGISTRY_MAP: Dict[str, List[str]] = {
    "parse_test_case": ["load_test_case_template"],
    "classify_intent": ["validate_template_contract", "parse_source_files", "validate_test_cases"],
    "retrieve_evidence": ["retrieve_evidence", "analyze_test_coverage", "validate_evidence_gate"],
    "plan_project": ["generate_canoe_config", "evaluate_canoe_config"],
    "generate_artifacts": ["generate_capl_script", "evaluate_capl_script"],
    "repair_or_review": ["plan_repair", "emit_test_case_corrections"],
    "package_project": ["package_outputs"],
}


def _load_burr_actions() -> Dict[str, Dict[str, Any]]:
    """Load all burr_actions/*.json files keyed by their id field."""
    actions: Dict[str, Dict[str, Any]] = {}
    if not BURR_ACTIONS_DIR.exists():
        return actions
    for path in sorted(BURR_ACTIONS_DIR.glob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            action_id = data.get("id", path.stem)
            actions[action_id] = data
        except Exception:
            continue
    return actions


def _load_profile() -> Dict[str, Any]:
    if PROFILE_PATH.exists():
        return json.loads(PROFILE_PATH.read_text(encoding="utf-8"))
    return {}


def _load_registry() -> Tuple[Set[str], List[Tuple[str, str, str]]]:
    """Import ACTION_REGISTRY and TRANSITION_SPECS from canoe_workflow."""
    from workflows.canoe_auto_generation_burr import canoe_workflow

    action_keys = set(canoe_workflow.ACTION_REGISTRY.keys())
    transitions = [
        (source, target, condition or "")
        for source, target, condition in canoe_workflow.TRANSITION_SPECS
    ]
    return action_keys, transitions


def validate_burr_actions_internal(burr_actions: Dict[str, Dict[str, Any]]) -> List[str]:
    """Validate internal consistency of burr_actions contracts."""
    issues: List[str] = []
    action_ids = set(burr_actions.keys())
    for action_id, contract in burr_actions.items():
        # Check required fields
        for field in ("id", "reads", "writes"):
            if field not in contract:
                issues.append(f"burr_action '{action_id}' missing required field '{field}'")
        # Check transition targets reference valid action IDs
        for transition in contract.get("transitions", []):
            target = transition.get("to", "") if isinstance(transition, dict) else ""
            if target and target not in action_ids:
                issues.append(
                    f"burr_action '{action_id}' has transition to unknown action '{target}'"
                )
        # Check gates reference valid gate names (non-empty strings)
        for gate in contract.get("gates", []):
            if not isinstance(gate, str) or not gate.strip():
                issues.append(f"burr_action '{action_id}' has empty gate entry")
    return issues


def validate_burr_to_registry_mapping(
    burr_actions: Dict[str, Dict[str, Any]],
    registry_keys: Set[str],
) -> List[str]:
    """Validate that all registry actions are covered by burr_action mappings."""
    issues: List[str] = []
    mapped_registry_keys: Set[str] = set()
    for registry_keys_list in BURR_ACTION_TO_REGISTRY_MAP.values():
        mapped_registry_keys.update(registry_keys_list)
    unmapped = sorted(registry_keys - mapped_registry_keys)
    for key in unmapped:
        issues.append(f"ACTION_REGISTRY key '{key}' is not mapped to any burr_action")
    # Check that mapped keys exist in registry
    for burr_id, keys in BURR_ACTION_TO_REGISTRY_MAP.items():
        if burr_id not in burr_actions:
            issues.append(f"burr_action '{burr_id}' in mapping table but not found in burr_actions/*.json")
        for key in keys:
            if key not in registry_keys:
                issues.append(f"burr_action '{burr_id}' maps to '{key}' but it is not in ACTION_REGISTRY")
    return issues


def validate_profile_actions(profile: Dict[str, Any], registry_keys: Set[str]) -> List[str]:
    """Validate that profile actions match the registry."""
    issues: List[str] = []
    profile_action_ids = {item.get("id") for item in profile.get("actions", [])}
    missing_in_code = sorted(profile_action_ids - registry_keys)
    missing_in_profile = sorted(registry_keys - profile_action_ids)
    for key in missing_in_code:
        issues.append(f"Profile action '{key}' is not in ACTION_REGISTRY")
    for key in missing_in_profile:
        issues.append(f"ACTION_REGISTRY key '{key}' is not in profile actions")
    return issues


def validate_profile_transitions(profile: Dict[str, Any], registry_keys: Set[str]) -> List[str]:
    """Validate that profile transitions reference valid actions."""
    issues: List[str] = []
    for entry in profile.get("transitions", []):
        source = entry[0] if len(entry) > 0 else ""
        target = entry[1] if len(entry) > 1 else ""
        if source not in registry_keys:
            issues.append(f"Profile transition source '{source}' is not a valid action")
        if target not in registry_keys:
            issues.append(f"Profile transition target '{target}' is not a valid action")
    return issues


def run_full_validation() -> Dict[str, Any]:
    """Run all validation checks and return a report."""
    burr_actions = _load_burr_actions()
    profile = _load_profile()
    registry_keys, _ = _load_registry()

    burr_internal = validate_burr_actions_internal(burr_actions)
    mapping_issues = validate_burr_to_registry_mapping(burr_actions, registry_keys)
    profile_action_issues = validate_profile_actions(profile, registry_keys)
    profile_transition_issues = validate_profile_transitions(profile, registry_keys)

    all_issues = burr_internal + mapping_issues + profile_action_issues + profile_transition_issues
    return {
        "burr_action_count": len(burr_actions),
        "registry_action_count": len(registry_keys),
        "profile_action_count": len(profile.get("actions", [])),
        "burr_internal_issues": burr_internal,
        "mapping_issues": mapping_issues,
        "profile_action_issues": profile_action_issues,
        "profile_transition_issues": profile_transition_issues,
        "total_issues": len(all_issues),
        "status": "pass" if not all_issues else "fail",
    }


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    report = run_full_validation()
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
