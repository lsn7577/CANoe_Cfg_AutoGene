from __future__ import annotations

from pathlib import Path
from typing import Any, Dict


VALIDATION_MODES = {"disabled", "manual", "automated"}


def _normalize_mode(mode: str) -> str:
    value = (mode or "disabled").strip().lower()
    return value if value in VALIDATION_MODES else "disabled"


def is_available() -> Dict[str, Any]:
    """Return conservative CANoe automation availability information.

    This adapter intentionally does not start CANoe. A real project can replace
    this function with COM-based discovery or a team-owned validation service.
    """
    try:
        import win32com.client  # type: ignore  # noqa: F401
    except Exception as exc:
        return {
            "available": False,
            "reason": f"Python win32com adapter is not available: {exc}",
        }
    return {
        "available": False,
        "reason": "win32com is importable, but CANoe automation is not configured for this workflow.",
    }


def validate_config(cfg_artifact: Dict[str, Any], mode: str = "disabled") -> Dict[str, Any]:
    mode = _normalize_mode(mode)
    path = Path(str(cfg_artifact.get("path", ""))) if cfg_artifact.get("path") else None
    if mode == "disabled":
        return {
            "mode": mode,
            "status": "skipped",
            "message": "Vector/CANoe CFG validation skipped because canoe_validation_mode=disabled.",
            "artifact": str(path) if path else "",
        }
    if mode == "manual":
        return {
            "mode": mode,
            "status": "manual_required",
            "message": "Manual CANoe CFG review/load is required; no automated Vector validation was executed.",
            "artifact": str(path) if path else "",
        }
    availability = is_available()
    if not availability["available"]:
        return {
            "mode": mode,
            "status": "failed",
            "message": f"Automated CANoe CFG validation requested but unavailable: {availability['reason']}",
            "artifact": str(path) if path else "",
        }
    return {
        "mode": mode,
        "status": "failed",
        "message": "Automated CANoe CFG validation adapter is present but no project-specific renderer is implemented.",
        "artifact": str(path) if path else "",
    }


def compile_capl(can_artifact: Dict[str, Any], mode: str = "disabled") -> Dict[str, Any]:
    mode = _normalize_mode(mode)
    path = Path(str(can_artifact.get("path", ""))) if can_artifact.get("path") else None
    if mode == "disabled":
        return {
            "mode": mode,
            "status": "skipped",
            "message": "Vector/CANoe CAPL compilation skipped because canoe_validation_mode=disabled.",
            "artifact": str(path) if path else "",
        }
    if mode == "manual":
        return {
            "mode": mode,
            "status": "manual_required",
            "message": "Manual CANoe/vTESTstudio CAPL compilation is required; no automated compile was executed.",
            "artifact": str(path) if path else "",
        }
    availability = is_available()
    if not availability["available"]:
        return {
            "mode": mode,
            "status": "failed",
            "message": f"Automated CANoe CAPL compilation requested but unavailable: {availability['reason']}",
            "artifact": str(path) if path else "",
        }
    return {
        "mode": mode,
        "status": "failed",
        "message": "Automated CAPL compilation adapter is present but no project-specific compile hook is implemented.",
        "artifact": str(path) if path else "",
    }
