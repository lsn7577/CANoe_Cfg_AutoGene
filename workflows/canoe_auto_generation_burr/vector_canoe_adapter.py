from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Any, Dict


VALIDATION_MODES = {"disabled", "manual", "automated"}


def _normalize_mode(mode: str) -> str:
    value = (mode or "disabled").strip().lower()
    return value if value in VALIDATION_MODES else "disabled"


def is_available() -> Dict[str, Any]:
    """Return CANoe COM availability without starting CANoe."""
    script = (
        "$progIds=@('CANoe.Application','CANoe.Application.12');"
        "foreach($p in $progIds){"
        "  if([type]::GetTypeFromProgID($p,$false)){ Write-Output $p; exit 0 }"
        "};"
        "exit 1"
    )
    try:
        completed = subprocess.run(
            ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", script],
            check=False,
            capture_output=True,
            text=True,
            timeout=15,
        )
    except Exception as exc:
        return {"available": False, "reason": f"PowerShell COM probe failed: {exc}"}
    if completed.returncode == 0:
        prog_id = completed.stdout.strip().splitlines()[0] if completed.stdout.strip() else "CANoe.Application"
        return {"available": True, "prog_id": prog_id, "reason": "CANoe COM ProgID is registered."}
    detail = (completed.stderr or completed.stdout or "").strip()
    return {"available": False, "reason": detail or "CANoe COM ProgID is not registered."}


def _powershell_literal(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def write_cfg_automation_script(plan: Dict[str, Any], plan_path: Path, output_cfg: Path, script_path: Path) -> Dict[str, Any]:
    """Write a CANoe COM script that lets CANoe serialize the real .cfg."""
    script_path.parent.mkdir(parents=True, exist_ok=True)
    plan_path = plan_path.resolve()
    output_cfg = output_cfg.resolve()
    major = 12
    target = str(plan.get("target_canoe_version") or "")
    digits = "".join(ch if ch.isdigit() else " " for ch in target).split()
    if digits:
        major = int(digits[0])

    content = f"""param(
  [string]$PlanPath = {_powershell_literal(str(plan_path))},
  [string]$OutputCfg = {_powershell_literal(str(output_cfg))}
)
$ErrorActionPreference = 'Stop'

function Test-PathText([string]$PathValue) {{
  return -not [string]::IsNullOrWhiteSpace($PathValue) -and (Test-Path -LiteralPath $PathValue)
}}

function Invoke-Optional([scriptblock]$Block, [string]$What) {{
  try {{
    & $Block
    Write-Host "[ok] $What"
  }} catch {{
    Write-Host "[skip] $What :: $($_.Exception.Message)"
  }}
}}

$plan = Get-Content -LiteralPath $PlanPath -Raw -Encoding UTF8 | ConvertFrom-Json
$canoe = New-Object -ComObject CANoe.Application
$canoe.Visible = $false

try {{
  if (Test-PathText $plan.base_cfg_template) {{
    $canoe.Open($plan.base_cfg_template, $false, $false)
  }} else {{
    $canoe.New($false, $false)
  }}

  $config = $canoe.Configuration
  $general = $config.GeneralSetup

  foreach ($dbc in @($plan.mounted_files.dbc)) {{
    if (Test-PathText $dbc) {{
      Invoke-Optional {{ $general.DatabaseSetup.Databases.Add($dbc) | Out-Null }} "add DBC $dbc"
    }}
  }}

  foreach ($cdd in @($plan.mounted_files.cdd)) {{
    if (Test-PathText $cdd) {{
      $network = 'CAN'
      if ($plan.channels -and $plan.channels.Count -gt 0 -and $plan.channels[0].'CANoe通道名') {{
        $network = [string]$plan.channels[0].'CANoe通道名'
      }}
      Invoke-Optional {{ $general.DiagnosticsSetup.DiagDescriptions.Add($network, $cdd, '') | Out-Null }} "add diagnostic description $cdd"
    }}
  }}

  foreach ($a2l in @($plan.mounted_files.a2l)) {{
    if (Test-PathText $a2l) {{
      Invoke-Optional {{ $general.XCPSetup.ECUs.Add($a2l, 'XCP') | Out-Null }} "add XCP ECU $a2l"
    }}
  }}

  foreach ($dll in @($plan.mounted_files.dll)) {{
    if (Test-PathText $dll) {{
      Invoke-Optional {{ $config.CLibraries.Add($dll) | Out-Null }} "add C library $dll"
    }}
  }}

  foreach ($capl in @($plan.test_modules.source)) {{
    if (Test-PathText $capl) {{
      Invoke-Optional {{ $config.UserFiles.Add($capl) | Out-Null }} "add CAPL/user file $capl"
    }}
  }}

  $parent = Split-Path -Parent $OutputCfg
  if ($parent -and -not (Test-Path -LiteralPath $parent)) {{
    New-Item -ItemType Directory -Path $parent | Out-Null
  }}

  Invoke-Optional {{ $config.SaveAs($OutputCfg, {major}, 0, $false) }} "save cfg via SaveAs"
  if (-not (Test-Path -LiteralPath $OutputCfg)) {{
    $config.Save($OutputCfg, $false)
  }}
}} finally {{
  if ($canoe) {{
    $canoe.Quit()
  }}
}}
"""
    script_path.write_text(content, encoding="utf-8")
    return {
        "script": str(script_path),
        "plan": str(plan_path),
        "output_cfg": str(output_cfg),
        "target_major": major,
        "status": "script_written",
    }


def prepare_cfg_generation(plan: Dict[str, Any], plan_path: Path, output_cfg: Path, script_path: Path, mode: str = "disabled") -> Dict[str, Any]:
    """Prepare, and optionally run, official CANoe COM based CFG generation."""
    script_info = write_cfg_automation_script(plan, plan_path, output_cfg, script_path)
    availability = is_available()
    result = {
        "mode": _normalize_mode(mode),
        "strategy": "canoe_com_automation",
        "availability": availability,
        **script_info,
    }
    if result["mode"] != "automated":
        result["status"] = "script_ready"
        result["message"] = "COM automation script generated; execution skipped because mode is not automated."
        return result
    if not availability["available"]:
        result["status"] = "unavailable"
        result["message"] = f"CANoe COM automation unavailable: {availability['reason']}"
        return result
    completed = subprocess.run(
        ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(script_path)],
        check=False,
        capture_output=True,
        text=True,
        timeout=180,
    )
    result["stdout"] = completed.stdout.strip()
    result["stderr"] = completed.stderr.strip()
    result["returncode"] = completed.returncode
    result["status"] = "generated" if completed.returncode == 0 and output_cfg.exists() else "failed"
    result["message"] = "CANoe COM automation completed." if result["status"] == "generated" else "CANoe COM automation did not produce the target cfg."
    return result


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
    if path and path.exists() and cfg_artifact.get("generation_mode") in {"base_cfg_copy", "canoe_com_automation"}:
        return {
            "mode": mode,
            "status": "pass",
            "message": "CANoe CFG artifact exists. Full semantic validation still requires loading it in CANoe.",
            "artifact": str(path),
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
