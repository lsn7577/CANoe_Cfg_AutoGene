from __future__ import annotations

import argparse
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional


CLAUDE_COMMAND_ENV = "CANOE_GENE_CLAUDE_CODE_COMMAND"
CLAUDE_MODEL_ENV = "CANOE_GENE_CLAUDE_CODE_MODEL"
CLAUDE_EFFORT_ENV = "CANOE_GENE_CLAUDE_CODE_EFFORT"
CLAUDE_TIMEOUT_ENV = "CANOE_GENE_CLAUDE_CODE_TIMEOUT_SECONDS"
CLAUDE_EXTRA_ARGS_ENV = "CANOE_GENE_CLAUDE_CODE_EXTRA_ARGS"

_CONFIG_PATH = Path(__file__).resolve().parent / "llm_agent_config.json"
_CONFIG_CACHE: Optional[Dict[str, Any]] = None


def _load_config() -> Dict[str, Any]:
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


def _config_cli_options() -> Dict[str, Any]:
    config = _load_config()
    return config.get("claude_code_cli_options", {}) if isinstance(config.get("claude_code_cli_options"), dict) else {}


def _safe_text(value: Any) -> str:
    return "" if value is None else str(value).strip()


def _timeout_seconds() -> int:
    raw = os.environ.get(CLAUDE_TIMEOUT_ENV, "").strip()
    if raw:
        try:
            return max(1, int(raw))
        except ValueError:
            pass
    config_timeout = _config_cli_options().get("timeout_seconds")
    if config_timeout is not None:
        try:
            return max(1, int(config_timeout))
        except (ValueError, TypeError):
            pass
    return 900


def _json_dumps(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2)


def _response_schema(role: str) -> Dict[str, Any]:
    if role == "planner":
        return {
            "type": "object",
            "additionalProperties": True,
            "required": ["golden_ir"],
            "properties": {
                "golden_ir": {
                    "type": "object",
                    "additionalProperties": True,
                    "required": ["project", "cases", "capl_api_plan", "assertions", "branching", "evidence_refs"],
                    "properties": {
                        "project": {"type": "object"},
                        "channels": {"type": "array"},
                        "cases": {"type": "array"},
                        "capl_api_plan": {"type": "array"},
                        "assertions": {"type": "array"},
                        "branching": {"type": "array"},
                        "evidence_refs": {"type": "array"},
                    },
                }
            },
        }
    return {
        "type": "object",
        "additionalProperties": True,
        "required": ["capl_source", "capl_script_plan"],
        "properties": {
            "capl_source": {"type": "string", "minLength": 1},
            "capl_script_plan": {
                "type": "object",
                "additionalProperties": True,
                "required": ["assumptions", "adapter_gaps", "used_evidence_refs", "cases"],
                "properties": {
                    "assumptions": {"type": "array"},
                    "adapter_gaps": {"type": "array"},
                    "used_evidence_refs": {"type": "array"},
                    "cases": {"type": "array"},
                    "fix_summary": {"type": "array"},
                },
            },
        },
    }


def build_prompt(payload: Dict[str, Any]) -> str:
    role = str(payload.get("role") or "authoring")
    capl_static_lint_contract = (
        "CAPL static-lint contract: capl_source must include literal text 'Generated for CANoe', "
        "must include a variables block, must have balanced braces, must contain exactly one "
        "CAPL testcase function per golden_ir/input case, must not contain TODO_UNVERIFIED_API, "
        "and any output(...) call requires a prior declaration like 'message MessageType msg_MessageType;' "
        "with output(msg_MessageType)."
    )
    if role == "planner":
        role_instruction = (
            "You are the Planner. Run once outside the repair loop. "
            "Translate the Excel-derived test cases into an immutable golden_ir. "
            "Do not generate CAPL source. Preserve project, channels, cases, operations, "
            "conditions, expected assertions, branching semantics, required APIs, and evidence refs."
        )
    elif role == "fixer":
        role_instruction = (
            "You are the Fixer. Run inside the compile-repair loop. "
            "Use only the immutable_golden_ir, current_complete_code, and latest_compile_error_log "
            "inside prompt_parts. Make the smallest CAPL source edit that resolves the latest compile "
            "error while preserving golden_ir semantics. Do not retain historical errors."
        )
    else:
        role_instruction = (
            "You are the CAPL authoring agent. Generate a complete CANoe CAPL test module from the "
            "provided scoped payload and evidence pages."
        )

    return "\n".join([
        "Return exactly one JSON object. Do not include markdown fences, prose, comments, or trailing text.",
        role_instruction,
        "Respect every hard_constraint in the payload.",
        capl_static_lint_contract,
        "If project-specific bindings are absent, describe them in adapter_gaps instead of inventing unsupported APIs.",
        "For capl_script_plan.cases, include one entry per golden_ir/input case and include that case's steps.",
        "Payload JSON:",
        _json_dumps(payload),
    ])


def _split_command_spec(value: str) -> List[str]:
    return shlex.split(value, posix=(os.name != "nt"))


def _claude_command_prefix() -> List[str]:
    configured = os.environ.get(CLAUDE_COMMAND_ENV, "").strip()
    if configured:
        return _split_command_spec(configured)
    executable = shutil.which("claude.cmd") or shutil.which("claude") or "claude"
    return [executable]


def _split_extra_args() -> List[str]:
    extra = os.environ.get(CLAUDE_EXTRA_ARGS_ENV, "").strip()
    if not extra:
        extra = _safe_text(_config_cli_options().get("extra_args"))
    if not extra:
        return []
    return _split_command_spec(extra)


def build_claude_command(role: str) -> List[str]:
    command = _claude_command_prefix()
    command.extend([
        "-p",
        "--input-format",
        "text",
        "--output-format",
        "text",
        "--permission-mode",
        "dontAsk",
        "--tools",
        "",
        "--no-session-persistence",
        "--json-schema",
        json.dumps(_response_schema(role), ensure_ascii=False, separators=(",", ":")),
    ])
    model = os.environ.get(CLAUDE_MODEL_ENV, "").strip() or _safe_text(_config_cli_options().get("model"))
    if model:
        command.extend(["--model", model])
    effort = os.environ.get(CLAUDE_EFFORT_ENV, "").strip() or _safe_text(_config_cli_options().get("effort"))
    if effort:
        command.extend(["--effort", effort])
    command.extend(_split_extra_args())
    return command


def _strip_markdown_fence(text: str) -> str:
    value = text.strip()
    match = re.fullmatch(r"```(?:json)?\s*(.*?)\s*```", value, flags=re.DOTALL | re.IGNORECASE)
    return match.group(1).strip() if match else value


def _parse_json_object(text: str) -> Dict[str, Any]:
    value = _strip_markdown_fence(text)
    try:
        parsed = json.loads(value)
        if isinstance(parsed, dict):
            return parsed
    except json.JSONDecodeError:
        pass

    decoder = json.JSONDecoder()
    for index, char in enumerate(value):
        if char != "{":
            continue
        try:
            parsed, _ = decoder.raw_decode(value[index:])
        except json.JSONDecodeError:
            continue
        if isinstance(parsed, dict):
            return parsed
    raise ValueError("Claude output did not contain a JSON object.")


def extract_response(stdout: str) -> Dict[str, Any]:
    parsed = _parse_json_object(stdout)
    if "golden_ir" in parsed or "capl_source" in parsed:
        return parsed

    for key in ("result", "text", "content", "message"):
        value = parsed.get(key)
        if isinstance(value, dict):
            if "golden_ir" in value or "capl_source" in value:
                return value
            if isinstance(value.get("content"), str):
                return _parse_json_object(value["content"])
        if isinstance(value, str) and value.strip():
            return _parse_json_object(value)
        if isinstance(value, list):
            text_parts = []
            for item in value:
                if isinstance(item, dict) and isinstance(item.get("text"), str):
                    text_parts.append(item["text"])
                elif isinstance(item, str):
                    text_parts.append(item)
            if text_parts:
                return _parse_json_object("\n".join(text_parts))

    raise ValueError("Claude JSON wrapper did not contain a CAPL agent response.")


def run_agent(payload_path: Path, response_path: Path) -> Dict[str, Any]:
    payload = json.loads(payload_path.read_text(encoding="utf-8"))
    role = str(payload.get("role") or "authoring")
    prompt = build_prompt(payload)
    command = build_claude_command(role)
    completed = subprocess.run(
        command,
        input=prompt,
        check=False,
        capture_output=True,
        text=True,
        errors="replace",
        timeout=_timeout_seconds(),
    )
    stdout = _safe_text(completed.stdout)
    stderr = _safe_text(completed.stderr)
    if completed.returncode != 0:
        raise RuntimeError(
            "Claude Code exited with "
            f"{completed.returncode}: {stderr or stdout}"
        )
    try:
        response = extract_response(stdout)
    except (ValueError, json.JSONDecodeError) as exc:
        diag_path = response_path.parent / f"{response_path.stem}_raw_stdout.txt"
        try:
            diag_path.write_text(stdout[:50000], encoding="utf-8")
        except Exception:
            pass
        raise RuntimeError(
            f"Failed to extract CAPL agent response from Claude output: {exc}. "
            f"Raw stdout saved to {diag_path}. stdout length={len(stdout)}, "
            f"first 200 chars: {stdout[:200]}"
        ) from exc
    response_path.parent.mkdir(parents=True, exist_ok=True)
    response_path.write_text(_json_dumps(response), encoding="utf-8")
    return response


def main(argv: Optional[List[str]] = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")

    parser = argparse.ArgumentParser(description="Claude Code adapter for CANoe CAPL authoring payloads.")
    parser.add_argument("payload", help="Path to CAPL agent payload JSON.")
    parser.add_argument("response", help="Path where CAPL agent response JSON must be written.")
    args = parser.parse_args(argv)

    try:
        run_agent(Path(args.payload), Path(args.response))
    except Exception as exc:
        print(f"Claude Code CAPL agent failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
