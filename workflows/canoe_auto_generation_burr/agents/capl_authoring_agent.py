from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path
from typing import Any, Dict, List


COMMAND_ENV = "CANOE_GENE_CAPL_AGENT_COMMAND"


def _trim_text(value: Any, limit: int = 1200) -> str:
    text = "" if value is None else str(value)
    text = text.replace("\r", " ").strip()
    return text[:limit]


def build_payload(
    structured_test_case: Dict[str, Any],
    project_config: Dict[str, Any],
    canoe_config_plan: Dict[str, Any],
    evidence_bundle: Dict[str, Any],
    coverage_report: Dict[str, Any],
    profile: Dict[str, Any],
) -> Dict[str, Any]:
    """Build the only context disclosed to the external CAPL authoring agent."""
    evidence_pages: List[Dict[str, Any]] = []
    for page in evidence_bundle.get("pages", []):
        evidence_pages.append({
            "symbol": page.get("symbol"),
            "page_id": page.get("page_id"),
            "name": page.get("name"),
            "page_type": page.get("page_type"),
            "syntax": page.get("syntax", []),
            "description": _trim_text(page.get("description")),
            "source": page.get("source"),
            "confidence": page.get("confidence"),
            "used_for": page.get("used_for", []),
        })
    return {
        "schema_version": "0.1.0",
        "agent": "KBIndexed_CAPLAuthoringAgent",
        "task": "Generate one CANoe CAPL test module from structured test cases.",
        "hard_constraints": [
            "Use only the provided evidence_pages and project/test-case payload.",
            "Do not use CANoe CFG, COM Automation, or other blocked topics.",
            "Do not invent CAPL APIs that are absent from evidence_pages.",
            "If project-specific XCP/diagnostic bindings are missing, use adapter gaps instead of fake APIs.",
            "Return JSON matching output_schema exactly enough for validation.",
        ],
        "retrieval_profile": {
            "id": profile.get("id"),
            "path": profile.get("profile_path"),
            "topic_filters": profile.get("topic_filters", []),
            "blocked_topic_filters": profile.get("blocked_topic_filters", []),
            "candidate_symbols": profile.get("candidate_symbols", []),
        },
        "project": structured_test_case.get("project", {}),
        "strategy": project_config.get("strategy", {}),
        "channels": structured_test_case.get("channels", []),
        "cases": structured_test_case.get("cases", []),
        "canoe_config_summary": {
            "project_name": canoe_config_plan.get("project_name"),
            "target_canoe_version": canoe_config_plan.get("target_canoe_version"),
            "mounted_files": canoe_config_plan.get("mounted_files", {}),
        },
        "coverage_report": coverage_report,
        "evidence_pages": evidence_pages,
        "output_schema": {
            "capl_source": "string: complete .can source",
            "capl_script_plan": {
                "assumptions": "array of strings",
                "adapter_gaps": "array of objects",
                "used_evidence_refs": "array of page_id or symbol strings",
                "cases": "array of per-case generation details",
            },
        },
    }


def _format_command(command: str, payload_path: Path, response_path: Path) -> str:
    return command.format(payload=str(payload_path), response=str(response_path))


def _validate_response(data: Dict[str, Any]) -> List[str]:
    issues = []
    if not isinstance(data.get("capl_source"), str) or not data.get("capl_source", "").strip():
        issues.append("response.capl_source must be a non-empty string")
    plan = data.get("capl_script_plan")
    if not isinstance(plan, dict):
        issues.append("response.capl_script_plan must be an object")
    else:
        for key in ("assumptions", "adapter_gaps", "used_evidence_refs", "cases"):
            if key in plan and not isinstance(plan[key], list):
                issues.append(f"response.capl_script_plan.{key} must be an array")
    return issues


def call_agent(payload: Dict[str, Any], output_root: Path, timeout_s: int = 180) -> Dict[str, Any]:
    """Invoke the configured external LLM CAPL authoring command.

    The command may use placeholders:
      {payload}  path to the JSON request
      {response} path where JSON response must be written
    """
    output_root.mkdir(parents=True, exist_ok=True)
    payload_path = output_root / "capl_authoring_payload.json"
    response_path = output_root / "capl_authoring_response.json"
    payload_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    command = os.environ.get(COMMAND_ENV, "").strip()
    if not command:
        return {
            "status": "unavailable",
            "message": f"{COMMAND_ENV} is not configured.",
            "payload_file": str(payload_path),
            "response_file": str(response_path),
        }

    try:
        completed = subprocess.run(
            _format_command(command, payload_path, response_path),
            check=False,
            capture_output=True,
            text=True,
            shell=True,
            timeout=timeout_s,
        )
    except Exception as exc:
        return {
            "status": "failed",
            "message": f"CAPL authoring agent command failed to start: {exc}",
            "payload_file": str(payload_path),
            "response_file": str(response_path),
        }

    if not response_path.exists():
        return {
            "status": "failed",
            "message": "CAPL authoring agent did not write a response JSON file.",
            "payload_file": str(payload_path),
            "response_file": str(response_path),
            "returncode": completed.returncode,
            "stdout": completed.stdout.strip(),
            "stderr": completed.stderr.strip(),
        }

    try:
        response = json.loads(response_path.read_text(encoding="utf-8"))
    except Exception as exc:
        return {
            "status": "failed",
            "message": f"CAPL authoring response is not valid JSON: {exc}",
            "payload_file": str(payload_path),
            "response_file": str(response_path),
            "returncode": completed.returncode,
            "stdout": completed.stdout.strip(),
            "stderr": completed.stderr.strip(),
        }

    issues = _validate_response(response)
    if issues:
        return {
            "status": "failed",
            "message": "CAPL authoring response failed schema validation.",
            "issues": issues,
            "payload_file": str(payload_path),
            "response_file": str(response_path),
            "returncode": completed.returncode,
            "stdout": completed.stdout.strip(),
            "stderr": completed.stderr.strip(),
        }

    return {
        "status": "generated",
        "message": "CAPL authoring agent generated a valid response.",
        "payload_file": str(payload_path),
        "response_file": str(response_path),
        "returncode": completed.returncode,
        "stdout": completed.stdout.strip(),
        "stderr": completed.stderr.strip(),
        "response": response,
    }
