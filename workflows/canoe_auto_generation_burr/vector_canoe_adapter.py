from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path
from typing import Any, Dict, Optional, Union


VALIDATION_MODES = {"disabled", "manual", "automated"}
CAPL_COMPILE_COMMAND_ENV = "CANOE_GENE_CAPL_COMPILE_COMMAND"
CAPL_COMPILE_TIMEOUT_ENV = "CANOE_GENE_CAPL_COMPILE_TIMEOUT_SECONDS"


def _safe_text(value: Any) -> str:
    return "" if value is None else str(value).strip()


def _subprocess_text_options() -> Dict[str, Any]:
    return {"text": True, "errors": "replace"}


def _normalize_mode(mode: str) -> str:
    value = (mode or "disabled").strip().lower()
    return value if value in VALIDATION_MODES else "disabled"


def _env_timeout_seconds(env_name: str, default: int) -> int:
    try:
        value = int(os.environ.get(env_name, "").strip() or default)
    except ValueError:
        return default
    return max(1, value)


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
            **_subprocess_text_options(),
            timeout=15,
        )
    except Exception as exc:
        return {"available": False, "reason": f"PowerShell COM probe failed: {exc}"}
    if completed.returncode == 0:
        stdout = _safe_text(completed.stdout)
        prog_id = stdout.splitlines()[0] if stdout else "CANoe.Application"
        return {"available": True, "prog_id": prog_id, "reason": "CANoe COM ProgID is registered."}
    detail = _safe_text(completed.stderr) or _safe_text(completed.stdout)
    return {"available": False, "reason": detail or "CANoe COM ProgID is not registered."}


def _powershell_literal(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


_DIALOG_SUPPRESSOR_PROLOGUE = r"""
# --- Dialog Suppressor: auto-close CANoe popup dialogs during COM operations ---
Add-Type @"
using System;
using System.Runtime.InteropServices;
public class Win32Dialog {
  [DllImport("user32.dll")]
  public static extern bool EnumWindows(EnumWindowsProc lpEnumFunc, IntPtr lParam);
  [DllImport("user32.dll")]
  public static extern int GetWindowText(IntPtr hWnd, System.Text.StringBuilder text, int count);
  [DllImport("user32.dll")]
  public static extern bool IsWindowVisible(IntPtr hWnd);
  [DllImport("user32.dll")]
  public static extern int GetWindowThreadProcessId(IntPtr hWnd, out int processId);
  [DllImport("user32.dll")]
  public static extern bool PostMessage(IntPtr hWnd, uint Msg, IntPtr wParam, IntPtr lParam);
  public delegate bool EnumWindowsProc(IntPtr hWnd, IntPtr lParam);
  public const uint WM_CLOSE = 0x0010;
}
"@

function Start-DialogSuppressor {
  $block = {
    $canoePids = @(Get-Process -Name "CANoe64","CANoe32" -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Id)
    if ($canoePids.Count -eq 0) { return }
    $stopwatch = [System.Diagnostics.Stopwatch]::StartNew()
    while ($stopwatch.ElapsedMilliseconds -lt 180000) {
      [Win32Dialog]::EnumWindows({
        param($hWnd, $lParam)
        if (-not [Win32Dialog]::IsWindowVisible($hWnd)) { return $true }
        $pid = 0
        [Win32Dialog]::GetWindowThreadProcessId($hWnd, [ref]$pid) | Out-Null
        if ($canoePids -notcontains $pid) { return $true }
        $sb = New-Object System.Text.StringBuilder 256
        [Win32Dialog]::GetWindowText($hWnd, $sb, 256) | Out-Null
        $title = $sb.ToString()
        if ($title -eq "" -or $title -eq "CANoe") { return $true }
        [Win32Dialog]::PostMessage($hWnd, [Win32Dialog]::WM_CLOSE, [IntPtr]::Zero, [IntPtr]::Zero) | Out-Null
        Write-Host "[dialog-suppressor] closed: $title"
        return $true
      }, [IntPtr]::Zero) | Out-Null
      Start-Sleep -Milliseconds 300
    }
  }
  $job = Start-Job -ScriptBlock $block
  Write-Host "[dialog-suppressor] started (PID $($job.Id))"
  return $job
}

function Stop-DialogSuppressor($job) {
  if ($job) {
    Stop-Job $job -ErrorAction SilentlyContinue
    Remove-Job $job -ErrorAction SilentlyContinue
    Write-Host "[dialog-suppressor] stopped"
  }
}
# --- End Dialog Suppressor ---
"""


def _dialog_suppressor_start() -> str:
    return "$dialogJob = Start-DialogSuppressor"


def _dialog_suppressor_stop() -> str:
    return "Stop-DialogSuppressor $dialogJob"


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

function Invoke-Fatal([scriptblock]$Block, [string]$What) {{
  try {{
    & $Block
    Write-Host "[ok] $What"
  }} catch {{
    Write-Host "[FATAL] $What :: $($_.Exception.Message)"
    throw "FATAL: $What failed: $($_.Exception.Message)"
  }}
}}

$plan = Get-Content -LiteralPath $PlanPath -Raw -Encoding UTF8 | ConvertFrom-Json
$canoe = New-Object -ComObject CANoe.Application
$canoe.Visible = $false
{_DIALOG_SUPPRESSOR_PROLOGUE}
{_dialog_suppressor_start()}

try {{
  if (Test-PathText $plan.base_cfg_template) {{
    $canoe.Open($plan.base_cfg_template, $false, $false)
  }} else {{
    $canoe.New($false, $false)
  }}

  $config = $canoe.Configuration
  $general = $config.GeneralSetup

  $hasBaseCfg = Test-PathText $plan.base_cfg_template

  foreach ($dbc in @($plan.mounted_files.dbc)) {{
    if (Test-PathText $dbc) {{
      if ($hasBaseCfg) {{
        Invoke-Optional {{ $general.DatabaseSetup.Databases.Add($dbc) | Out-Null }} "add DBC $dbc"
      }} else {{
        Invoke-Fatal {{ $general.DatabaseSetup.Databases.Add($dbc) | Out-Null }} "add DBC $dbc"
      }}
    }}
  }}

  $network = 'CAN'
  if ($plan.network_name) {{
    $network = [string]$plan.network_name
  }}

  foreach ($cdd in @($plan.mounted_files.cdd)) {{
    if (Test-PathText $cdd) {{
      if ($hasBaseCfg) {{
        Invoke-Optional {{ $general.DiagnosticsSetup.DiagDescriptions.Add($network, $cdd, '') | Out-Null }} "add diagnostic description $cdd"
      }} else {{
        Invoke-Fatal {{ $general.DiagnosticsSetup.DiagDescriptions.Add($network, $cdd, '') | Out-Null }} "add diagnostic description $cdd"
      }}
    }}
  }}

  foreach ($a2l in @($plan.mounted_files.a2l)) {{
    if (Test-PathText $a2l) {{
      if ($hasBaseCfg) {{
        Invoke-Optional {{ $general.XCPSetup.ECUs.Add($a2l, 'XCP') | Out-Null }} "add XCP ECU $a2l"
      }} else {{
        Invoke-Fatal {{ $general.XCPSetup.ECUs.Add($a2l, 'XCP') | Out-Null }} "add XCP ECU $a2l"
      }}
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

  $saved = $false
  try {{
    $config.SaveAs($OutputCfg, {major}, 0, $false) | Out-Null
    $saved = $true
    Write-Host "[ok] save cfg via SaveAs(path, major, 0, false)"
  }} catch {{
    Write-Host "[skip] SaveAs(path, major, 0, false) :: $($_.Exception.Message)"
  }}
  if (-not $saved) {{
    try {{
      $config.Save($OutputCfg, $false) | Out-Null
      $saved = $true
      Write-Host "[ok] save cfg via Save(path, false)"
    }} catch {{
      Write-Host "[skip] Save(path, false) :: $($_.Exception.Message)"
    }}
  }}
  if (-not $saved) {{
    throw "All SaveAs/Save methods failed; cannot produce target cfg."
  }}
}} finally {{
  {_dialog_suppressor_stop()}
  if ($canoe) {{
    try {{ $canoe.Quit() }} catch {{ }}
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
        **_subprocess_text_options(),
        timeout=180,
    )
    result["stdout"] = _safe_text(completed.stdout)
    result["stderr"] = _safe_text(completed.stderr)
    result["returncode"] = completed.returncode
    result["status"] = "generated" if completed.returncode == 0 and output_cfg.exists() else "failed"
    result["message"] = "CANoe COM automation completed." if result["status"] == "generated" else "CANoe COM automation did not produce the target cfg."
    return result


def write_cfg_verify_script(cfg_path: Path, plan: Dict[str, Any], script_path: Path) -> Dict[str, Any]:
    """Write a CANoe COM script that reopens a generated cfg and verifies mount counts.

    The script opens the cfg via ``CANoe.Application.Open``, reads the number of
    mounted Databases, DiagDescriptions, and XCP ECUs, then writes a JSON report
    comparing actual counts against the expected counts derived from *plan*.
    """
    script_path.parent.mkdir(parents=True, exist_ok=True)
    cfg_path = cfg_path.resolve()

    mounted = plan.get("mounted_files", {}) if plan else {}
    expected_dbc = len(mounted.get("dbc", []) or [])
    expected_cdd = len(mounted.get("cdd", []) or [])
    expected_a2l = len(mounted.get("a2l", []) or [])

    content = f"""param(
  [string]$CfgPath = {_powershell_literal(str(cfg_path))}
)
$ErrorActionPreference = 'Stop'

$expectedDbc = {expected_dbc}
$expectedCdd = {expected_cdd}
$expectedA2l = {expected_a2l}

function Write-VerifyReport([hashtable]$Report) {{
  $parent = Split-Path -Parent $CfgPath
  if (-not $parent) {{ $parent = $PWD.Path }}
  $reportPath = Join-Path $parent 'cfg_verify_report.json'
  $Report | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $reportPath -Encoding UTF8
  Write-Output $reportPath
}}

$canoe = $null
try {{
  if (-not (Test-Path -LiteralPath $CfgPath)) {{
    throw "CFG file not found: $CfgPath"
  }}

  $canoe = New-Object -ComObject CANoe.Application
  $canoe.Visible = $false
  $canoe.Open($CfgPath, $false, $false)

  $config = $canoe.Configuration
  $general = $config.GeneralSetup

  $dbcCount = 0
  try {{ $dbcCount = @($general.DatabaseSetup.Databases).Count }} catch {{ }}

  $cddCount = 0
  try {{ $cddCount = @($general.DiagnosticsSetup.DiagDescriptions).Count }} catch {{ }}

  $a2lCount = 0
  try {{ $a2lCount = @($general.XCPSetup.ECUs).Count }} catch {{ }}

  $dbcOk = ($dbcCount -ge $expectedDbc)
  $cddOk = ($cddCount -ge $expectedCdd)
  $a2lOk = ($a2lCount -ge $expectedA2l)
  $allOk = $dbcOk -and $cddOk -and $a2lOk

  Write-VerifyReport @{{
    status = $(if ($allOk) {{ 'pass' }} else {{ 'failed' }})
    cfg = $CfgPath
    databases_count = $dbcCount
    diag_descriptions_count = $cddCount
    xcp_ecus_count = $a2lCount
    expected_dbc = $expectedDbc
    expected_cdd = $expectedCdd
    expected_a2l = $expectedA2l
    dbc_ok = $dbcOk
    cdd_ok = $cddOk
    a2l_ok = $a2lOk
  }}
  exit 0
}} catch {{
  Write-VerifyReport @{{
    status = 'failed'
    cfg = $CfgPath
    error = $_.Exception.Message
    databases_count = 0
    diag_descriptions_count = 0
    xcp_ecus_count = 0
    expected_dbc = $expectedDbc
    expected_cdd = $expectedCdd
    expected_a2l = $expectedA2l
    dbc_ok = $false
    cdd_ok = $false
    a2l_ok = $false
  }}
  exit 1
}} finally {{
  {_dialog_suppressor_stop()}
  if ($canoe) {{
    try {{ $canoe.Quit() }} catch {{ }}
  }}
}}
"""
    script_path.write_text(content, encoding="utf-8")
    return {
        "script": str(script_path),
        "cfg": str(cfg_path),
        "expected_dbc": expected_dbc,
        "expected_cdd": expected_cdd,
        "expected_a2l": expected_a2l,
        "status": "script_written",
    }


def validate_config(cfg_artifact: Dict[str, Any], mode: str = "disabled", plan: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
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
        availability = is_available()
        if not availability["available"]:
            return {
                "mode": mode,
                "status": "manual_required",
                "message": (
                    f"CANoe CFG artifact exists but COM verification unavailable: {availability['reason']}. "
                    "Manual CANoe CFG review is required."
                ),
                "artifact": str(path),
            }
        verify_script_path = path.parent / "cfg_verify.ps1"
        write_cfg_verify_script(path, plan or {}, verify_script_path)
        try:
            completed = subprocess.run(
                ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(verify_script_path)],
                check=False,
                capture_output=True,
                **_subprocess_text_options(),
                timeout=180,
            )
        except subprocess.TimeoutExpired:
            return {
                "mode": mode,
                "status": "manual_required",
                "message": "CANoe COM verification timed out. Manual CFG review is required.",
                "artifact": str(path),
                "verify_script": str(verify_script_path),
            }
        verify_report: Dict[str, Any] = {}
        report_path = path.parent / "cfg_verify_report.json"
        if report_path.exists():
            try:
                verify_report = json.loads(report_path.read_text(encoding="utf-8-sig"))
            except Exception:
                verify_report = {}
        verify_status = _safe_text(verify_report.get("status")) or ("pass" if completed.returncode == 0 else "failed")
        dbc_count = int(verify_report.get("databases_count", 0) or 0)
        cdd_count = int(verify_report.get("diag_descriptions_count", 0) or 0)
        a2l_count = int(verify_report.get("xcp_ecus_count", 0) or 0)
        expected_dbc = int(verify_report.get("expected_dbc", 0) or 0)
        expected_cdd = int(verify_report.get("expected_cdd", 0) or 0)
        expected_a2l = int(verify_report.get("expected_a2l", 0) or 0)

        failures: list[str] = []
        if expected_dbc > 0 and dbc_count == 0:
            failures.append(f"expected {expected_dbc} DBC(s) but 0 databases mounted")
        if expected_cdd > 0 and cdd_count == 0:
            failures.append(f"expected {expected_cdd} CDD(s) but 0 diag descriptions mounted")
        if expected_a2l > 0 and a2l_count == 0:
            failures.append(f"expected {expected_a2l} A2L(s) but 0 XCP ECUs mounted")

        if verify_status == "failed" or failures:
            detail = "; ".join(failures) if failures else _safe_text(verify_report.get("error")) or "verification script reported failure"
            return {
                "mode": mode,
                "status": "failed",
                "message": f"CANoe COM verification failed: {detail}.",
                "artifact": str(path),
                "verify_script": str(verify_script_path),
                "verify_report": verify_report,
                "returncode": completed.returncode,
                "stdout": _safe_text(completed.stdout),
                "stderr": _safe_text(completed.stderr),
            }
        return {
            "mode": mode,
            "status": "pass",
            "message": (
                f"CANoe COM verification passed: {dbc_count} database(s), "
                f"{cdd_count} diag description(s), {a2l_count} XCP ECU(s) mounted."
            ),
            "artifact": str(path),
            "verify_script": str(verify_script_path),
            "verify_report": verify_report,
            "returncode": completed.returncode,
            "stdout": _safe_text(completed.stdout),
            "stderr": _safe_text(completed.stderr),
        }
    if not plan:
        return {
            "mode": mode,
            "status": "manual_required",
            "message": "Automated CANoe CFG validation could not verify mounts without a plan. Manual review is required.",
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


def _format_compile_command(command: str, capl_path: Path, report_path: Path, cfg_path: str = "") -> str:
    return command.format(
        capl=str(capl_path),
        report=str(report_path),
        cfg=cfg_path,
    )


def write_capl_compile_script(capl_path: Path, report_path: Path, script_path: Path, cfg_path: Optional[Path] = None) -> Dict[str, Any]:
    """Write a CANoe COM script that compiles configured CAPL nodes and emits JSON diagnostics."""
    script_path.parent.mkdir(parents=True, exist_ok=True)
    capl_path = capl_path.resolve()
    report_path = report_path.resolve()
    cfg_literal = _powershell_literal(str(cfg_path.resolve())) if cfg_path else "''"

    content = f"""param(
  [string]$CaplPath = {_powershell_literal(str(capl_path))},
  [string]$CfgPath = {cfg_literal},
  [string]$ReportPath = {_powershell_literal(str(report_path))}
)
$ErrorActionPreference = 'Stop'

function Write-CompileReport([hashtable]$Report) {{
  $parent = Split-Path -Parent $ReportPath
  if ($parent -and -not (Test-Path -LiteralPath $parent)) {{
    New-Item -ItemType Directory -Path $parent | Out-Null
  }}
  $Report | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $ReportPath -Encoding UTF8
}}

function Get-StringProperty($Object, [string]$Name) {{
  try {{
    $value = $Object.$Name
    if ($null -eq $value) {{ return '' }}
    return [string]$value
  }} catch {{
    return ''
  }}
}}

function Get-ResultCode($Object) {{
  try {{
    $value = $Object.Result
    if ($null -eq $value) {{ return $null }}
    return $value
  }} catch {{
    return $null
  }}
}}

function Invoke-ComMethodIfAvailable($Object, [string]$MethodName) {{
  if ($null -eq $Object) {{ return @{{ invoked = $false; value = $null; error = 'owner object is null' }} }}
  try {{
    $value = $Object.GetType().InvokeMember($MethodName, 'InvokeMethod', $null, $Object, @())
    return @{{ invoked = $true; value = $value; error = '' }}
  }} catch {{
    return @{{ invoked = $false; value = $null; error = $_.Exception.Message }}
  }}
}}

function Invoke-CaplCompilation($Application) {{
  $attempts = @()
  foreach ($candidate in @(
    @{{ owner = $Application.Configuration; name = 'RunCompilation'; surface = 'Configuration.RunCompilation' }},
    @{{ owner = $Application.Configuration; name = 'Compile'; surface = 'Configuration.Compile' }},
    @{{ owner = $Application.CAPL; name = 'Compile'; surface = 'CAPL.Compile' }}
  )) {{
    $result = Invoke-ComMethodIfAvailable $candidate.owner $candidate.name
    $attempts += @{{ surface = $candidate.surface; invoked = $result.invoked; error = $result.error }}
    if ($result.invoked) {{
      return @{{ surface = $candidate.surface; value = $result.value; attempts = $attempts }}
    }}
  }}
  throw "No supported CANoe CAPL compilation COM method was available. Tried Configuration.RunCompilation, Configuration.Compile, and CAPL.Compile."
}}

function Get-CompilationResultObject($Application) {{
  foreach ($candidate in @(
    @{{ owner = $Application.Configuration; name = 'GetCompilationResult'; surface = 'Configuration.GetCompilationResult' }}
  )) {{
    $result = Invoke-ComMethodIfAvailable $candidate.owner $candidate.name
    if ($result.invoked) {{
      return @{{ surface = $candidate.surface; value = $result.value }}
    }}
  }}
  try {{
    if ($null -ne $Application.Configuration.CompilationResult) {{
      return @{{ surface = 'Configuration.CompilationResult'; value = $Application.Configuration.CompilationResult }}
    }}
  }} catch {{ }}
  try {{
    if ($null -ne $Application.CAPL.CompileResult) {{
      return @{{ surface = 'CAPL.CompileResult'; value = $Application.CAPL.CompileResult }}
    }}
  }} catch {{ }}
  return @{{ surface = ''; value = $null }}
}}

function Open-CanoeConfiguration($Application, [string]$CfgPath) {{
  $attempts = @()
  try {{
    $Application.Open($CfgPath)
    return @{{ opened = $true; surface = 'Application.Open(cfg)'; attempts = $attempts }}
  }} catch {{
    $attempts += @{{ surface = 'Application.Open(cfg)'; error = $_.Exception.Message }}
  }}
  try {{
    $Application.Open($CfgPath, $true, $true)
    return @{{ opened = $true; surface = 'Application.Open(cfg, true, true)'; attempts = $attempts }}
  }} catch {{
    $attempts += @{{ surface = 'Application.Open(cfg, true, true)'; error = $_.Exception.Message }}
  }}
  return @{{ opened = $false; surface = ''; attempts = $attempts }}
}}

$canoe = $null
try {{
  if (-not (Test-Path -LiteralPath $CaplPath)) {{
    throw "CAPL file not found: $CaplPath"
  }}

  $canoe = New-Object -ComObject CANoe.Application
  $canoe.Visible = $false
  {_DIALOG_SUPPRESSOR_PROLOGUE}
  {_dialog_suppressor_start()}
  $warnings = @()

  if (-not [string]::IsNullOrWhiteSpace($CfgPath) -and (Test-Path -LiteralPath $CfgPath)) {{
    $openInfo = Open-CanoeConfiguration $canoe $CfgPath
    foreach ($attempt in @($openInfo.attempts)) {{
      if ($null -ne $attempt) {{
        $warnings += "$($attempt.surface): $($attempt.error)"
      }}
    }}
    if (-not $openInfo.opened) {{
      $warnings += "Unable to load configuration '$CfgPath'; creating a fresh configuration before compilation."
      $canoe.New($false, $false)
    }}
  }} else {{
    $warnings += "Configuration path missing; creating a fresh configuration before compilation."
    $canoe.New($false, $false)
  }}

  try {{
    $canoe.Configuration.UserFiles.Add($CaplPath) | Out-Null
  }} catch {{
    # The CAPL file may already be attached to the configuration. Compilation can still proceed.
  }}

  $compileInvocation = Invoke-CaplCompilation $canoe
  Start-Sleep -Seconds 3
  $compileResultInfo = Get-CompilationResultObject $canoe
  $compileResult = $compileResultInfo.value
  $errorMessage = Get-StringProperty $compileResult 'ErrorMessage'
  if ([string]::IsNullOrWhiteSpace($errorMessage)) {{
    $errorMessage = Get-StringProperty $compileResult 'Error'
  }}
  $nodeName = Get-StringProperty $compileResult 'NodeName'
  $sourceFile = Get-StringProperty $compileResult 'SourceFile'
  $resultCode = Get-ResultCode $compileResult
  $successText = Get-StringProperty $compileResult 'Success'

  $failed = -not [string]::IsNullOrWhiteSpace($errorMessage)
  if (-not [string]::IsNullOrWhiteSpace($successText)) {{
    try {{
      $failed = $failed -or (-not [System.Convert]::ToBoolean($successText))
    }} catch {{ }}
  }}
  if ($null -ne $resultCode) {{
    try {{
      $failed = $failed -or ([int]$resultCode -ne 0)
    }} catch {{
      $failed = $failed -or ([string]$resultCode -notin @('', '0', 'Success', 'Ok', 'OK'))
    }}
  }}

  if ($failed) {{
    $message = $errorMessage
    if ([string]::IsNullOrWhiteSpace($message)) {{
      $message = "CAPL compilation returned result code $resultCode."
    }}
    if ($warnings.Count -gt 0) {{
      $message = ($warnings -join ' | ') + " | " + $message
    }}
    Write-CompileReport @{{
      status = 'failed'
      message = $message
      result_code = $resultCode
      success = $successText
      node_name = $nodeName
      source_file = $sourceFile
      compile_surface = $compileInvocation.surface
      result_surface = $compileResultInfo.surface
      compile_attempts = $compileInvocation.attempts
      warnings = $warnings
      capl = $CaplPath
      cfg = $CfgPath
    }}
    exit 1
  }}

  Write-CompileReport @{{
    status = 'pass'
    message = 'CAPL compilation completed without reported errors.'
    result_code = $resultCode
    success = $successText
    node_name = $nodeName
    source_file = $sourceFile
    compile_surface = $compileInvocation.surface
    result_surface = $compileResultInfo.surface
    compile_attempts = $compileInvocation.attempts
    warnings = $warnings
    capl = $CaplPath
    cfg = $CfgPath
  }}
  exit 0
}} catch {{
  Write-CompileReport @{{
    status = 'failed'
    message = $_.Exception.Message
    warnings = @($warnings)
    capl = $CaplPath
    cfg = $CfgPath
  }}
  exit 1
}} finally {{
  {_dialog_suppressor_stop()}
  if ($canoe) {{
    try {{ $canoe.Quit() }} catch {{ }}
  }}
}}
"""
    script_path.write_text(content, encoding="utf-8")
    return {
        "script": str(script_path),
        "capl": str(capl_path),
        "cfg": str(cfg_path) if cfg_path else "",
        "report_file": str(report_path),
        "status": "script_written",
    }


def compile_capl(
    can_artifact: Dict[str, Any],
    mode: str = "disabled",
    cfg_artifact: Optional[Dict[str, Any]] = None,
    output_root: Optional[Union[str, Path]] = None,
    attempt: int = 0,
) -> Dict[str, Any]:
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
    if not path or not path.exists():
        return {
            "mode": mode,
            "status": "failed",
            "message": "Automated CANoe CAPL compilation requested but CAPL artifact is missing.",
            "artifact": str(path) if path else "",
        }
    command = os.environ.get(CAPL_COMPILE_COMMAND_ENV, "").strip()
    if command:
        root = Path(output_root) if output_root else path.parent
        root.mkdir(parents=True, exist_ok=True)
        report_path = root / f"capl_compile_attempt_{attempt or 1}.json"
        cfg_path = ""
        if cfg_artifact and cfg_artifact.get("path"):
            cfg_path = str(cfg_artifact.get("path"))
        timeout_s = _env_timeout_seconds(CAPL_COMPILE_TIMEOUT_ENV, 240)
        try:
            completed = subprocess.run(
                _format_compile_command(command, path, report_path, cfg_path),
                check=False,
                capture_output=True,
                **_subprocess_text_options(),
                shell=True,
                timeout=timeout_s,
            )
        except subprocess.TimeoutExpired as exc:
            return {
                "mode": mode,
                "status": "failed",
                "message": f"CAPL compile command timed out after {timeout_s} seconds.",
                "artifact": str(path),
                "cfg_artifact": cfg_path,
                "report_file": str(report_path),
                "returncode": None,
                "stdout": _safe_text(exc.stdout),
                "stderr": _safe_text(exc.stderr),
                "details": {"status": "failed", "message": "compile timeout", "timeout_seconds": timeout_s},
            }
        report: Dict[str, Any] = {}
        if report_path.exists():
            try:
                report = json.loads(report_path.read_text(encoding="utf-8"))
            except Exception as exc:
                report = {
                    "status": "failed",
                    "message": f"CAPL compile report is not valid JSON: {exc}",
                }
        status = str(report.get("status") or ("pass" if completed.returncode == 0 else "failed"))
        message = _safe_text(report.get("message")) or _safe_text(completed.stderr) or _safe_text(completed.stdout) or "CAPL compile command completed."
        return {
            "mode": mode,
            "status": status,
            "message": message,
            "artifact": str(path),
            "cfg_artifact": cfg_path,
            "report_file": str(report_path),
            "returncode": completed.returncode,
            "stdout": _safe_text(completed.stdout),
            "stderr": _safe_text(completed.stderr),
            "details": report,
        }
    root = Path(output_root) if output_root else path.parent
    root.mkdir(parents=True, exist_ok=True)
    report_path = root / f"capl_compile_attempt_{attempt or 1}.json"
    script_path = root / f"capl_compile_attempt_{attempt or 1}.ps1"
    cfg_path = None
    if cfg_artifact and cfg_artifact.get("path"):
        candidate = Path(str(cfg_artifact.get("path")))
        if candidate.exists():
            cfg_path = candidate
    script_info = write_capl_compile_script(path, report_path, script_path, cfg_path)
    availability = is_available()
    if not availability["available"]:
        return {
            "mode": mode,
            "status": "unavailable",
            "message": f"Automated CANoe CAPL compilation requested but unavailable: {availability['reason']}",
            "artifact": str(path),
            "script": script_info["script"],
            "report_file": script_info["report_file"],
        }
    timeout_s = _env_timeout_seconds(CAPL_COMPILE_TIMEOUT_ENV, 300)
    try:
        completed = subprocess.run(
            ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(script_path)],
            check=False,
            capture_output=True,
            **_subprocess_text_options(),
            timeout=timeout_s,
        )
    except subprocess.TimeoutExpired as exc:
        return {
            "mode": mode,
            "status": "failed",
            "message": f"CANoe CAPL COM compilation timed out after {timeout_s} seconds.",
            "artifact": str(path),
            "cfg_artifact": str(cfg_path) if cfg_path else "",
            "script": str(script_path),
            "report_file": str(report_path),
            "returncode": None,
            "stdout": _safe_text(exc.stdout),
            "stderr": _safe_text(exc.stderr),
            "details": {"status": "failed", "message": "compile timeout", "timeout_seconds": timeout_s},
        }
    report: Dict[str, Any] = {}
    if report_path.exists():
        try:
            report = json.loads(report_path.read_text(encoding="utf-8-sig"))
        except Exception as exc:
            report = {
                "status": "failed",
                "message": f"CAPL compile report is not valid JSON: {exc}",
            }
    status = str(report.get("status") or ("pass" if completed.returncode == 0 else "failed"))
    message = _safe_text(report.get("message")) or _safe_text(completed.stderr) or _safe_text(completed.stdout) or "CANoe CAPL COM compilation completed."
    return {
        "mode": mode,
        "status": status,
        "message": message,
        "artifact": str(path),
        "cfg_artifact": str(cfg_path) if cfg_path else "",
        "script": str(script_path),
        "report_file": str(report_path),
        "returncode": completed.returncode,
        "stdout": _safe_text(completed.stdout),
        "stderr": _safe_text(completed.stderr),
        "details": report,
    }
