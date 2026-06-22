#!/usr/bin/env python3
"""CI check runner for the CANoe_Cfg_AutoGene project.

Runs all validation checks and reports a summary. Exits 0 if all checks pass,
1 if any check fails.

Usage:
    python ci/run_checks.py

Checks performed:
    1. validate_workflow_profile.py  — workflow profile schema validation
    2. validate_workflow_kb.py       — knowledge base integrity validation
    3. py_compile on all .py files   — syntax check
    4. test_retrieval_profiles.py    — retrieval profile tests
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

ROOT = Path(__file__).resolve().parents[1]

WORKFLOW_DIR = ROOT / "workflows" / "canoe_auto_generation_burr"
KB_DIR = ROOT / "knowledge_base" / "workflow_kb"

VALIDATE_PROFILE = WORKFLOW_DIR / "validate_workflow_profile.py"
VALIDATE_KB = KB_DIR / "validate_workflow_kb.py"
TEST_RETRIEVAL = WORKFLOW_DIR / "test_retrieval_profiles.py"


# ---------------------------------------------------------------------------
# Check runner
# ---------------------------------------------------------------------------


def _run_check(name: str, cmd: List[str]) -> Tuple[bool, str]:
    """Run a single check via subprocess.

    Args:
        name: Human-readable check name.
        cmd: Command list to execute.

    Returns:
        Tuple of (passed: bool, output: str).
    """
    try:
        env = os.environ.copy()
        env["PYTHONPATH"] = str(ROOT) + os.pathsep + env.get("PYTHONPATH", "")
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=str(ROOT),
            env=env,
            timeout=300,
        )
        output = result.stdout.strip()
        if result.stderr.strip():
            output = f"{output}\n{result.stderr.strip()}" if output else result.stderr.strip()
        return result.returncode == 0, output
    except subprocess.TimeoutExpired:
        return False, f"Check '{name}' timed out after 300 seconds."
    except FileNotFoundError as exc:
        return False, f"Check '{name}' failed to start: {exc}"
    except Exception as exc:
        return False, f"Check '{name}' encountered an error: {exc}"


def _collect_python_files() -> List[Path]:
    """Collect all .py files under the workflow directory."""
    if not WORKFLOW_DIR.exists():
        return []
    return sorted(WORKFLOW_DIR.rglob("*.py"))


def main() -> int:
    """Run all CI checks and print a summary.

    Returns:
        0 if all checks pass, 1 if any check fails.
    """
    checks: List[Tuple[str, List[str]]] = []

    # Check 1: validate_workflow_profile.py
    checks.append((
        "validate_workflow_profile.py",
        [sys.executable, str(VALIDATE_PROFILE)],
    ))

    # Check 2: validate_workflow_kb.py
    checks.append((
        "validate_workflow_kb.py",
        [sys.executable, str(VALIDATE_KB)],
    ))

    # Check 3: py_compile on all .py files in workflow dir
    py_files = _collect_python_files()
    compile_cmd = [sys.executable, "-m", "py_compile"] + [str(f) for f in py_files]
    checks.append((
        f"py_compile ({len(py_files)} files)",
        compile_cmd,
    ))

    # Check 4: test_retrieval_profiles.py
    checks.append((
        "test_retrieval_profiles.py",
        [sys.executable, str(TEST_RETRIEVAL)],
    ))

    # Run all checks
    results: List[Tuple[str, bool, str]] = []
    for name, cmd in checks:
        print(f"\n{'=' * 60}")
        print(f"Running: {name}")
        print(f"Command: {' '.join(cmd)}")
        print(f"{'=' * 60}")
        passed, output = _run_check(name, cmd)
        if output:
            print(output)
        status = "PASS" if passed else "FAIL"
        print(f"[{status}] {name}")
        results.append((name, passed, output))

    # Print summary
    print(f"\n{'=' * 60}")
    print("CI CHECK SUMMARY")
    print(f"{'=' * 60}")
    all_passed = True
    for name, passed, _output in results:
        status = "PASS" if passed else "FAIL"
        print(f"  [{status}] {name}")
        if not passed:
            all_passed = False

    total = len(results)
    passed_count = sum(1 for _, p, _ in results if p)
    failed_count = total - passed_count
    print(f"\nTotal: {total}  |  Passed: {passed_count}  |  Failed: {failed_count}")
    print(f"{'=' * 60}")

    if all_passed:
        print("All checks passed!")
        return 0
    else:
        print("Some checks failed!")
        return 1


if __name__ == "__main__":
    sys.exit(main())
