from __future__ import annotations

import json
import os
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional


COMMAND_ENV = "CANOE_GENE_CAPL_AGENT_COMMAND"
PLANNER_COMMAND_ENV = "CANOE_GENE_CAPL_PLANNER_COMMAND"
FIXER_COMMAND_ENV = "CANOE_GENE_CAPL_FIXER_COMMAND"
TIMEOUT_ENV = "CANOE_GENE_CAPL_AGENT_TIMEOUT_SECONDS"

_CONFIG_PATH = Path(__file__).resolve().parent / "llm_agent_config.json"
_CONFIG_CACHE: Optional[Dict[str, Any]] = None
_WORKFLOW_DIR = Path(__file__).resolve().parent


def _safe_text(value: Any) -> str:
    return "" if value is None else str(value).strip()


def _load_llm_agent_config() -> Dict[str, Any]:
    """Load the LLM agent JSON config file (cached after first read)."""
    global _CONFIG_CACHE
    if _CONFIG_CACHE is not None:
        return _CONFIG_CACHE
    if _CONFIG_PATH.exists():
        try:
            _CONFIG_CACHE = json.loads(_CONFIG_PATH.read_text(encoding="utf-8"))
        except Exception:
            _CONFIG_CACHE = {}
    else:
        _CONFIG_CACHE = {}
    return _CONFIG_CACHE


def _resolve_command_template(template: str) -> str:
    """Resolve {workflow_dir} placeholder in a command template."""
    return template.replace("{workflow_dir}", str(_WORKFLOW_DIR))


def _command_for_role(role: str) -> str:
    """Resolve the command string for a given role.

    Priority (highest first):
    1. Environment variable (CANOE_GENE_CAPL_PLANNER_COMMAND / FIXER_COMMAND / AGENT_COMMAND)
    2. JSON config file role-specific override (planner/fixer.command_template_override)
    3. JSON config file backend command_template for the role's configured backend
    4. JSON config file default_backend's command_template
    """
    env_key = {"planner": PLANNER_COMMAND_ENV, "fixer": FIXER_COMMAND_ENV}.get(role, COMMAND_ENV)
    env_value = os.environ.get(env_key, "").strip()
    if env_value:
        return env_value
    env_generic = os.environ.get(COMMAND_ENV, "").strip()
    if env_generic:
        return env_generic

    config = _load_llm_agent_config()
    role_config = config.get(role, {}) if isinstance(config.get(role), dict) else {}

    override = _safe_text(role_config.get("command_template_override"))
    if override:
        return _resolve_command_template(override)

    backend_name = _safe_text(role_config.get("backend")) or _safe_text(config.get("default_backend"))
    if backend_name:
        backends = config.get("backends", {})
        backend = backends.get(backend_name, {}) if isinstance(backends, dict) else {}
        template = _safe_text(backend.get("command_template"))
        if template:
            return _resolve_command_template(template)

    return ""


def _timeout_for_role(role: str, default_timeout: int) -> int:
    """Resolve the timeout for a given role.

    Priority: env var > role override > backend timeout > default.
    """
    raw = os.environ.get(TIMEOUT_ENV, "").strip()
    if raw:
        try:
            return max(1, int(raw))
        except ValueError:
            pass

    config = _load_llm_agent_config()
    role_config = config.get(role, {}) if isinstance(config.get(role), dict) else {}
    role_override = role_config.get("timeout_seconds_override")
    if role_override is not None:
        try:
            return max(1, int(role_override))
        except (ValueError, TypeError):
            pass

    backend_name = _safe_text(role_config.get("backend")) or _safe_text(config.get("default_backend"))
    if backend_name:
        backends = config.get("backends", {})
        backend = backends.get(backend_name, {}) if isinstance(backends, dict) else {}
        backend_timeout = backend.get("timeout_seconds")
        if backend_timeout is not None:
            try:
                return max(1, int(backend_timeout))
            except (ValueError, TypeError):
                pass

    return default_timeout


def _trim_text(value: Any, limit: int = 1200) -> str:
    text = "" if value is None else str(value)
    text = text.replace("\r", " ").strip()
    return text[:limit]


def _subprocess_text_options() -> Dict[str, Any]:
    return {"text": True, "errors": "replace"}


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


def build_planner_payload(
    structured_test_case: Dict[str, Any],
    project_config: Dict[str, Any],
    canoe_config_plan: Dict[str, Any],
    evidence_bundle: Dict[str, Any],
    coverage_report: Dict[str, Any],
    profile: Dict[str, Any],
) -> Dict[str, Any]:
    payload = build_payload(
        structured_test_case,
        project_config,
        canoe_config_plan,
        evidence_bundle,
        coverage_report,
        profile,
    )
    payload.update({
        "role": "planner",
        "task": "Translate the immutable Excel-derived test-case model into a stable CAPL authoring IR.",
        "hard_constraints": [
            "Produce only the golden_ir; do not generate CAPL code.",
            "The golden_ir must preserve the project, channels, test cases, operations, conditions, expected results, required CAPL APIs, and assertions.",
            "The golden_ir will be read-only in the compile-fix loop.",
            "Do not use CANoe CFG, COM Automation, or other blocked topics.",
            "Do not invent CAPL APIs that are absent from evidence_pages.",
        ],
        "output_schema": {
            "golden_ir": {
                "project": "object",
                "channels": "array",
                "cases": "array",
                "capl_api_plan": "array of CAPL APIs or adapter bindings required by the cases",
                "assertions": "array of expected checks/verdict semantics",
                "branching": "array of logical branches or empty array",
                "evidence_refs": "array of page_id or symbol strings",
            }
        },
    })
    return payload


MAX_CAPL_SOURCE_CHARS = 60000
MAX_ERROR_LOG_CHARS = 8000


def _estimate_tokens(text: str) -> int:
    """Rough token estimate: ~4 chars per token for mixed content."""
    if not text:
        return 0
    return max(1, len(text) // 4)


def _truncate_text(text: str, max_chars: int, label: str = "content") -> str:
    if not text or len(text) <= max_chars:
        return text
    half = max_chars // 2
    return (
        text[:half]
        + f"\n\n... [truncated: {label} exceeded {max_chars} chars, "
        + f"original {len(text)} chars] ...\n\n"
        + text[-half:]
    )


def build_fixer_payload(
    golden_ir: Dict[str, Any],
    current_code: str,
    compile_error_log: str,
    attempt: int,
    repeated_error_count: int = 0,
) -> Dict[str, Any]:
    truncated_code = _truncate_text(current_code, MAX_CAPL_SOURCE_CHARS, label="capl_source")
    truncated_errors = _truncate_text(compile_error_log, MAX_ERROR_LOG_CHARS, label="error_log")
    truncated = (
        len(current_code or "") > MAX_CAPL_SOURCE_CHARS
        or len(compile_error_log or "") > MAX_ERROR_LOG_CHARS
    )

    hard_constraints = [
        "The golden_ir is the only business specification and must not be changed.",
        "Use the latest compile_error_log only; do not infer or retain historical errors.",
        "Make the smallest code change that resolves the latest compile error.",
        "Do not add behavior that is absent from golden_ir.",
        "The returned capl_source must contain the literal header text 'Generated for CANoe'.",
        "The returned capl_source must contain a variables block.",
        "The returned capl_source must contain exactly one CAPL testcase function per golden_ir case.",
        "If capl_source uses output(), declare a CAPL message variable first, for example 'message MessageType msg_MessageType;', and call output() with that variable.",
        "Do not return TODO_UNVERIFIED_API placeholders.",
        "Return JSON matching output_schema exactly enough for validation.",
    ]
    if repeated_error_count > 0:
        hard_constraints.append(
            f"If repeated_error_count > 0, the same compile error has appeared {repeated_error_count} time(s) before. Consider a fundamentally different fix approach."
        )

    return {
        "schema_version": "0.1.0",
        "agent": "KBIndexed_CAPLFixerAgent",
        "role": "fixer",
        "task": "Minimally edit the current CAPL code so it compiles while preserving the immutable golden_ir semantics.",
        "attempt": attempt,
        "repeated_error_count": repeated_error_count,
        "hard_constraints": hard_constraints,
        "token_budget": {
            "estimated_tokens": _estimate_tokens(truncated_code) + _estimate_tokens(truncated_errors),
            "capl_source_chars": len(truncated_code or ""),
            "error_log_chars": len(truncated_errors or ""),
            "truncated": truncated,
        },
        "prompt_parts": [
            {
                "name": "immutable_golden_ir",
                "replaceable": False,
                "content": golden_ir,
            },
            {
                "name": "current_complete_code",
                "replaceable": True,
                "content": truncated_code,
            },
            {
                "name": "latest_compile_error_log",
                "replaceable": True,
                "content": truncated_errors,
            },
        ],
        "output_schema": {
            "capl_source": "string: complete .can source after the minimal fix",
            "capl_script_plan": {
                "assumptions": "array of strings",
                "adapter_gaps": "array of objects",
                "used_evidence_refs": "array of page_id or symbol strings",
                "cases": "array of per-case generation details",
                "fix_summary": "array of strings describing minimal edits",
            },
        },
    }


def _format_command(command: str, payload_path: Path, response_path: Path) -> str:
    return command.format(payload=str(payload_path), response=str(response_path))


def _validate_capl_response(data: Dict[str, Any]) -> List[str]:
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


def _validate_golden_ir(golden_ir: Dict[str, Any]) -> List[str]:
    """Strictly validate the golden_ir against the planner JSON Schema.

    Returns a list of issue strings (empty means valid).
    """
    issues: List[str] = []

    if not isinstance(golden_ir.get("project"), dict):
        issues.append("golden_ir.project must be an object")

    cases = golden_ir.get("cases")
    if not isinstance(cases, list):
        issues.append("golden_ir.cases must be an array")
    else:
        for idx, case in enumerate(cases):
            if not isinstance(case, dict):
                issues.append(f"golden_ir.cases[{idx}] must be an object")
            elif not case.get("case_id"):
                issues.append(f"golden_ir.cases[{idx}] must have a case_id field")

    if not isinstance(golden_ir.get("capl_api_plan"), list):
        issues.append("golden_ir.capl_api_plan must be an array")

    if not isinstance(golden_ir.get("assertions"), list):
        issues.append("golden_ir.assertions must be an array")

    if not isinstance(golden_ir.get("branching"), list):
        issues.append("golden_ir.branching must be an array")

    if not isinstance(golden_ir.get("evidence_refs"), list):
        issues.append("golden_ir.evidence_refs must be an array")

    channels = golden_ir.get("channels")
    if channels is not None and not isinstance(channels, list):
        issues.append("golden_ir.channels must be an array if present")

    return issues


def _validate_planner_response(data: Dict[str, Any]) -> List[str]:
    golden_ir = data.get("golden_ir")
    if not isinstance(golden_ir, dict) or not golden_ir:
        return ["response.golden_ir must be a non-empty object"]
    return _validate_golden_ir(golden_ir)


_MAX_DIAGNOSTIC_CHARS = 10000


def _save_planner_diagnostics(
    output_root: Path,
    result: Dict[str, Any],
    payload_path: Path,
    response_path: Path,
) -> None:
    """Persist planner failure diagnostics to a dedicated JSON file."""
    diagnostics: Dict[str, Any] = {
        "role": "planner",
        "status": result.get("status"),
        "message": result.get("message"),
        "issues": result.get("issues", []),
        "returncode": result.get("returncode"),
        "stdout": _safe_text(result.get("stdout"))[:_MAX_DIAGNOSTIC_CHARS],
        "stderr": _safe_text(result.get("stderr"))[:_MAX_DIAGNOSTIC_CHARS],
        "payload_file": str(payload_path),
        "response_file": str(response_path),
        "timestamp": datetime.now().isoformat(),
    }
    if response_path.exists():
        try:
            diagnostics["response_content"] = response_path.read_text(encoding="utf-8")[:_MAX_DIAGNOSTIC_CHARS]
        except Exception:
            diagnostics["response_content"] = "<unreadable>"
    diag_path = output_root / "capl_planner_diagnostics.json"
    diag_path.write_text(json.dumps(diagnostics, ensure_ascii=False, indent=2), encoding="utf-8")


def _call_role_agent(
    payload: Dict[str, Any],
    output_root: Path,
    role: str,
    response_validator,
    timeout_s: int = 180,
) -> Dict[str, Any]:
    """Invoke the configured external LLM CAPL command.

    The command may use placeholders:
      {payload}  path to the JSON request
      {response} path where JSON response must be written
    """
    output_root.mkdir(parents=True, exist_ok=True)
    payload_path = output_root / f"capl_{role}_payload.json"
    response_path = output_root / f"capl_{role}_response.json"
    payload_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    command = _command_for_role(role)
    if not command:
        env_name = {"planner": PLANNER_COMMAND_ENV, "fixer": FIXER_COMMAND_ENV}.get(role, COMMAND_ENV)
        result = {
            "status": "unavailable",
            "message": f"{env_name} or {COMMAND_ENV} is not configured.",
            "payload_file": str(payload_path),
            "response_file": str(response_path),
        }
        if role == "planner":
            _save_planner_diagnostics(output_root, result, payload_path, response_path)
        return result

    timeout_s = _timeout_for_role(role, timeout_s)
    try:
        completed = subprocess.run(
            _format_command(command, payload_path, response_path),
            check=False,
            capture_output=True,
            **_subprocess_text_options(),
            shell=True,
            timeout=timeout_s,
        )
    except Exception as exc:
        result = {
            "status": "failed",
            "message": f"CAPL authoring agent command failed to start: {exc}",
            "payload_file": str(payload_path),
            "response_file": str(response_path),
        }
        if role == "planner":
            _save_planner_diagnostics(output_root, result, payload_path, response_path)
        return result

    if not response_path.exists():
        result = {
            "status": "failed",
            "message": "CAPL authoring agent did not write a response JSON file.",
            "payload_file": str(payload_path),
            "response_file": str(response_path),
            "returncode": completed.returncode,
            "stdout": _safe_text(completed.stdout),
            "stderr": _safe_text(completed.stderr),
        }
        if role == "planner":
            _save_planner_diagnostics(output_root, result, payload_path, response_path)
        return result

    try:
        response = json.loads(response_path.read_text(encoding="utf-8"))
    except Exception as exc:
        result = {
            "status": "failed",
            "message": f"CAPL authoring response is not valid JSON: {exc}",
            "payload_file": str(payload_path),
            "response_file": str(response_path),
            "returncode": completed.returncode,
            "stdout": _safe_text(completed.stdout),
            "stderr": _safe_text(completed.stderr),
        }
        if role == "planner":
            _save_planner_diagnostics(output_root, result, payload_path, response_path)
        return result

    issues = response_validator(response)
    if issues:
        result = {
            "status": "failed",
            "message": "CAPL authoring response failed schema validation.",
            "issues": issues,
            "payload_file": str(payload_path),
            "response_file": str(response_path),
            "returncode": completed.returncode,
            "stdout": _safe_text(completed.stdout),
            "stderr": _safe_text(completed.stderr),
        }
        if role == "planner":
            _save_planner_diagnostics(output_root, result, payload_path, response_path)
        return result

    return {
        "status": "generated",
        "message": f"CAPL {role} agent generated a valid response.",
        "payload_file": str(payload_path),
        "response_file": str(response_path),
        "returncode": completed.returncode,
        "stdout": _safe_text(completed.stdout),
        "stderr": _safe_text(completed.stderr),
        "response": response,
    }


def call_agent(payload: Dict[str, Any], output_root: Path, timeout_s: int = 180) -> Dict[str, Any]:
    return _call_role_agent(payload, output_root, "authoring", _validate_capl_response, timeout_s)


def call_planner(payload: Dict[str, Any], output_root: Path, timeout_s: int = 180) -> Dict[str, Any]:
    return _call_role_agent(payload, output_root, "planner", _validate_planner_response, timeout_s)


def call_fixer(payload: Dict[str, Any], output_root: Path, timeout_s: int = 180) -> Dict[str, Any]:
    return _call_role_agent(payload, output_root, "fixer", _validate_capl_response, timeout_s)
