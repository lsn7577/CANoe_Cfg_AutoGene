"""Run directory retention manager.

Manages the lifecycle of CANoe configuration auto-generation run directories.
Implements two retention policies:

* **Count-based**: when the number of runs exceeds ``max_runs``, the oldest
  runs are deleted.
* **Age-based**: any run directory older than ``max_age_days`` is deleted.

The run referenced by ``latest_run_manifest.json`` is **never** deleted.
"""

from __future__ import annotations

import json
import re
import shutil
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

RUN_DIR_PATTERN = re.compile(
    r"^\d{8}_\d{6}_[0-9a-fA-F]{8}$"
)

LATEST_MANIFEST = "latest_run_manifest.json"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _as_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value).strip()


def _is_run_dir(name: str) -> bool:
    """Check if *name* matches the run directory pattern ``YYYYMMDD_HHMMSS_XXXXXXXX``."""

    return bool(RUN_DIR_PATTERN.match(name))


def _parse_run_timestamp(name: str) -> Optional[datetime]:
    """Extract a ``datetime`` from a run directory name.

    Returns ``None`` if the name does not match the expected pattern.
    """

    match = RUN_DIR_PATTERN.match(name)
    if not match:
        return None
    try:
        return datetime.strptime(name[:15], "%Y%m%d_%H%M%S")
    except ValueError:
        return None


def _read_latest_manifest(base_output_root: Path) -> Dict[str, Any]:
    """Read the latest run manifest file (if it exists)."""

    manifest_path = base_output_root / LATEST_MANIFEST
    if not manifest_path.exists():
        return {}
    try:
        return json.loads(manifest_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}


def _get_protected_run_id(base_output_root: Path) -> Optional[str]:
    """Return the run_id that must never be deleted (from the latest manifest)."""

    manifest = _read_latest_manifest(base_output_root)
    return _as_text(manifest.get("run_id")) or None


def _dir_size(path: Path) -> int:
    """Calculate the total size of a directory tree in bytes."""

    total = 0
    try:
        for entry in path.rglob("*"):
            if entry.is_file():
                try:
                    total += entry.stat().st_size
                except OSError:
                    pass
    except OSError:
        pass
    return total


def _runs_base(base_output_root: Path) -> Path:
    """Return the ``runs`` subdirectory under *base_output_root*."""

    return base_output_root / "runs"


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def list_runs(base_output_root: Path) -> List[Dict[str, Any]]:
    """List all run directories under ``base_output_root / "runs"``.

    Parameters
    ----------
    base_output_root
        The base output root directory.

    Returns
    -------
    list of dict
        Each dict contains:
        ``run_id``, ``path``, ``created_at``, ``size_bytes``, ``manifest_exists``.
        The list is sorted by directory name (oldest first).
    """

    runs_dir = _runs_base(base_output_root)
    if not runs_dir.exists():
        return []

    results: List[Dict[str, Any]] = []
    for entry in sorted(runs_dir.iterdir()):
        if not entry.is_dir() or not _is_run_dir(entry.name):
            continue
        ts = _parse_run_timestamp(entry.name)
        results.append({
            "run_id": entry.name,
            "path": str(entry),
            "created_at": ts.strftime("%Y-%m-%d %H:%M:%S") if ts else "",
            "size_bytes": _dir_size(entry),
            "manifest_exists": (entry / "final_package_manifest.json").exists()
            or (entry / "blocked_manifest.json").exists(),
        })

    return results


def cleanup_run(run_path: Path) -> bool:
    """Delete a run directory.

    Parameters
    ----------
    run_path
        Path to the run directory to delete.

    Returns
    -------
    bool
        ``True`` if the directory was deleted (or did not exist),
        ``False`` if deletion failed.
    """

    run_path = Path(run_path)
    if not run_path.exists():
        return True
    try:
        shutil.rmtree(run_path)
        return True
    except OSError:
        return False


def apply_retention(
    base_output_root: Path,
    max_runs: int = 20,
    max_age_days: int = 30,
) -> Dict[str, Any]:
    """Apply retention policies to run directories.

    Scans ``base_output_root / "runs"`` for run directories matching the
    pattern ``YYYYMMDD_HHMMSS_XXXXXXXX``.  Directories exceeding
    ``max_age_days`` or exceeding the ``max_runs`` count limit are deleted.

    The run referenced by ``latest_run_manifest.json`` is **never** deleted.

    Parameters
    ----------
    base_output_root
        The base output root directory.
    max_runs
        Maximum number of run directories to keep.  Defaults to ``20``.
    max_age_days
        Maximum age in days for a run directory.  Defaults to ``30``.

    Returns
    -------
    dict
        ``{"scanned": N, "deleted": M, "remaining": K, "deleted_paths": [...]}``
    """

    runs_dir = _runs_base(base_output_root)
    protected_id = _get_protected_run_id(base_output_root)

    if not runs_dir.exists():
        return {
            "scanned": 0,
            "deleted": 0,
            "remaining": 0,
            "deleted_paths": [],
        }

    # Collect all run directories sorted by name (oldest first)
    run_entries: List[tuple[str, Path, datetime]] = []
    for entry in sorted(runs_dir.iterdir()):
        if not entry.is_dir() or not _is_run_dir(entry.name):
            continue
        ts = _parse_run_timestamp(entry.name)
        if ts is None:
            continue
        run_entries.append((entry.name, entry, ts))

    scanned = len(run_entries)
    deleted_paths: List[str] = []
    now = datetime.now()
    age_threshold = now - timedelta(days=max_age_days)

    # Phase 1: Delete runs older than max_age_days (but not the protected run)
    survivors: List[tuple[str, Path, datetime]] = []
    for name, path, ts in run_entries:
        is_protected = protected_id is not None and name == protected_id
        if ts < age_threshold and not is_protected:
            if cleanup_run(path):
                deleted_paths.append(str(path))
            else:
                survivors.append((name, path, ts))
        else:
            survivors.append((name, path, ts))

    # Phase 2: If still too many runs, delete the oldest (but not the protected run)
    # survivors are already sorted oldest-first
    if len(survivors) > max_runs:
        excess = len(survivors) - max_runs
        to_delete = []
        for name, path, ts in survivors:
            if excess <= 0:
                break
            is_protected = protected_id is not None and name == protected_id
            if is_protected:
                continue
            to_delete.append((name, path, ts))
            excess -= 1

        for name, path, ts in to_delete:
            if cleanup_run(path):
                deleted_paths.append(str(path))
                survivors = [(n, p, t) for n, p, t in survivors if n != name]

    remaining = len(survivors)

    return {
        "scanned": scanned,
        "deleted": len(deleted_paths),
        "remaining": remaining,
        "deleted_paths": deleted_paths,
    }
