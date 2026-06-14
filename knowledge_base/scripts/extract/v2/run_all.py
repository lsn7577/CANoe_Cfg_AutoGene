"""Run the full v2 structured extraction pipeline for all topics and versions.

Writes directly to the knowledge/ folder organized by topic x version.

Steps:
  1. Extract v15 CAPL (MadCap template) -> knowledge/v15/capl/
  2. Extract v12 CAPL (flat-table template) -> knowledge/v12/capl/
  3. Extract v15 + v12 Panel (concept pages) -> knowledge/v{12,15}/panel/
  4. Extract v15 + v12 DBC (concept pages) -> knowledge/v{12,15}/dbc/
  5. Copy CAPL XCP subcategory to knowledge/v{12,15}/xcp/ (subset of CAPL)
  6. Regenerate knowledge/_index.json

Outputs:
  knowledge/v{12,15}/{capl,panel,dbc,xcp}/structured/...
  knowledge/v{12,15}/{capl,panel,dbc,xcp}/<topic>.json  (per-category summary)
  knowledge/v{12,15}/{capl,panel,dbc,xcp}/<overview>.md  (top-level overview)
  knowledge/_index.json
"""
import argparse
import os
import sys
import subprocess
import json
import time
import shutil
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parents[2]
DEFAULT_DEST = ROOT / "knowledge"


def _run(name, args):
    cmd = [sys.executable, str(SCRIPT_DIR / name)] + [str(a) for a in args]
    print("\n>>> " + " ".join(cmd))
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.stdout:
        print(r.stdout)
    if r.returncode != 0:
        print("FAILED:", r.stderr)
        return False
    return True


def _ensure_dir(p):
    os.makedirs(p, exist_ok=True)


def _regen_index(dest):
    """Regenerate knowledge/_index.json from current structured/ contents."""
    top = {
        "metadata": {
            "title": "Vector CANoe Knowledge Base",
            "schema_version": "2.0",
            "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "topics": ["capl", "panel", "dbc", "xcp"],
            "versions": ["v12", "v15"],
            "latest": "v15",
        },
        "versions": {},
    }
    for ver in ("v12", "v15"):
        vd = os.path.join(dest, ver)
        if not os.path.isdir(vd):
            continue
        top["versions"][ver] = {"topics": {}}
        for topic in ("capl", "panel", "dbc", "xcp"):
            td = os.path.join(vd, topic)
            if not os.path.isdir(td):
                continue
            struct = os.path.join(td, "structured")
            n = 0
            if os.path.isdir(struct):
                for r, ds, fs in os.walk(struct):
                    for f in fs:
                        if f.endswith(".json"):
                            n += 1
            sub = len([d for d in os.listdir(struct) if os.path.isdir(os.path.join(struct, d))]) if os.path.isdir(struct) else 0
            top["versions"][ver]["topics"][topic] = {"json_count": n, "subcategory_count": sub}
    with open(os.path.join(dest, "_index.json"), "w", encoding="utf-8") as f:
        json.dump(top, f, indent=2, ensure_ascii=False)
    print("Regenerated knowledge/_index.json")


def _copy_xcp_from_capl(dest, ver):
    """Copy CAPL XCP subcategory to xcp/structured for the given version."""
    src = os.path.join(dest, ver, "capl", "structured", "XCP")
    if not os.path.isdir(src):
        return
    dst = os.path.join(dest, ver, "xcp", "structured")
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    print(f"Copied XCP from {ver}/capl/structured/XCP/ to {ver}/xcp/structured/")


def _default_source(env_name, rel):
    return Path(os.environ.get(env_name, ROOT / rel))


def main():
    p = argparse.ArgumentParser(description="Run v12/v15 extraction into knowledge/")
    p.add_argument("--v15-root", default=_default_source("CANOE_V15_CHM_ROOT", "chm_extract_v15"))
    p.add_argument("--v12-root", default=_default_source("CANOE_V12_CHM_ROOT", "chm_extract_v12"))
    p.add_argument("--kb-root", default=DEFAULT_DEST)
    args = p.parse_args()

    dest = Path(args.kb_root)
    v15_root = Path(args.v15_root)
    v12_root = Path(args.v12_root)
    v15_panel = v15_root / "VectorToolsEnvironment" / "Topics" / "PanelDesigner"
    v15_dbc = v15_root / "CANeds" / "Topics"
    v15_capl = v15_root / "CANoeCANalyzer" / "Topics" / "CAPLFunctions"
    v12_panel = v12_root / "PanelDesigner" / "Topics"
    v12_dbc = v12_root / "CANeds" / "Topics"
    v12_capl = v12_root / "CANoeCANalyzer" / "Topics" / "CAPLFunctions"

    ok = True
    # 1. v15 CAPL
    ok &= _run("03_extract_v15_structured.py", [
        "--capl-src", v15_capl,
        "--output-root", dest / "v15" / "capl",
    ])
    # 2. v12 CAPL
    ok &= _run("04_extract_structured.py", [
        v12_capl, dest / "v12" / "capl",
        "v12 chm_extract CAPLFunctions", "v12",
    ])
    # 3. v15 + v12 Panel
    ok &= _run("07_extract_concept.py", [v15_panel, dest / "v15" / "panel", "Panel", "v15"])
    ok &= _run("07_extract_concept.py", [v12_panel, dest / "v12" / "panel", "Panel", "v12"])
    # 4. v15 + v12 DBC
    ok &= _run("07_extract_concept.py", [v15_dbc, dest / "v15" / "dbc", "DBC", "v15"])
    ok &= _run("07_extract_concept.py", [v12_dbc, dest / "v12" / "dbc", "DBC", "v12"])
    # 5. Copy XCP from CAPL
    _copy_xcp_from_capl(dest, "v12")
    _copy_xcp_from_capl(dest, "v15")
    # 6. Regenerate index
    _regen_index(dest)
    return ok


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
