"""Version-parameterized extraction pipeline for new CANoe versions (v17, v18, ...).

Usage:
    python scripts/extract/v3/run_all.py --version v17 --chm-root ../chm_extract_v17
"""
import os, sys, json, time, argparse
from importlib import util as importlib_util
from pathlib import Path

# This script lives at scripts/extract/v3/run_all.py
# The reusable parsers live at scripts/extract/v2/
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))     # .../scripts/extract/v3
PARSER_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), "v2")  # .../scripts/extract/v2
ROOT = Path(__file__).resolve().parents[3]


def _load_module(name, path):
    spec = importlib_util.spec_from_file_location(name, path)
    mod = importlib_util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _safe_filename(name):
    bad = set("/:\\*?" + chr(34) + "<>|")
    name = "".join("_" if c in bad else c for c in name)
    name = " ".join(name.split()).strip()
    if not name:
        name = "unnamed"
    return name[:200]


def _walk_concept(src_root, dst_root, cp, rm, kind="Panel"):
    n_ok = n_err = 0
    if not os.path.isdir(src_root):
        return 0, 0
    os.makedirs(dst_root, exist_ok=True)
    for root, dirs, files in os.walk(src_root):
        rel = os.path.relpath(root, src_root)
        sub = "" if rel == "." else rel.replace("\\\\", "/")
        sub_out = os.path.join(dst_root, sub) if sub else dst_root
        os.makedirs(sub_out, exist_ok=True)
        for f in files:
            if not f.lower().endswith(".htm"):
                continue
            fp = os.path.join(root, f)
            try:
                rec = cp.parse_concept_page(fp, kind=kind)
                if "error" in rec:
                    n_err += 1
                    continue
                name = rec.get("name") or f.replace(".htm", "")
                fname = _safe_filename(name)
                with open(os.path.join(sub_out, fname + ".json"), "w", encoding="utf-8") as ff:
                    json.dump(rec, ff, indent=2, ensure_ascii=False)
                with open(os.path.join(sub_out, fname + ".md"), "w", encoding="utf-8") as ff:
                    ff.write(rm.render_page_md(rec))
                n_ok += 1
            except Exception:
                n_err += 1
    return n_ok, n_err


def extract_capl(capl_src, capl_dst, kb_root, version, vp, rm):
    if not os.path.isdir(capl_src):
        print("[capl] source not found: " + capl_src)
        return None
    print("[capl] walking " + capl_src + " -> " + capl_dst)
    os.makedirs(capl_dst, exist_ok=True)
    n_ok = n_err = 0
    cats = {}
    for cat in sorted(os.listdir(capl_src)):
        cat_dir = os.path.join(capl_src, cat)
        if not os.path.isdir(cat_dir):
            continue
        cat_out = os.path.join(capl_dst, cat)
        os.makedirs(cat_out, exist_ok=True)
        cats[cat] = []
        for root, _, files in os.walk(cat_dir):
            for f in files:
                if not f.lower().endswith(".htm"):
                    continue
                fp = os.path.join(root, f)
                try:
                    rec = vp.parse_page(fp, cat)
                    if "error" in rec:
                        n_err += 1
                        continue
                    name = rec.get("name") or f.replace(".htm", "")
                    fname = _safe_filename(name)
                    with open(os.path.join(cat_out, fname + ".json"), "w", encoding="utf-8") as ff:
                        json.dump(rec, ff, indent=2, ensure_ascii=False)
                    with open(os.path.join(cat_out, fname + ".md"), "w", encoding="utf-8") as ff:
                        ff.write(rm.render_page_md(rec))
                    cats[cat].append(dict(name=name, file=fname + ".json", page_type=rec.get("page_type", "")))
                    n_ok += 1
                except Exception:
                    n_err += 1
    idx = dict(
        metadata=dict(topic="capl", version=version, schema_version="2.0"),
        json_count=n_ok,
        subcategory_count=len(cats),
        categories=dict((c, len(v)) for c, v in cats.items()),
    )
    with open(os.path.join(kb_root, version, "capl", "_index.json"), "w", encoding="utf-8") as ff:
        json.dump(idx, ff, indent=2, ensure_ascii=False)
    return dict(ok=n_ok, errors=n_err, categories=len(cats))


def main():
    p = argparse.ArgumentParser(description="Extract structured data from a CANoe CHM-extracted directory")
    p.add_argument("--version", required=True, help="e.g. v17, v18")
    p.add_argument("--chm-root", required=True, help="Path to CHM-extracted root directory")
    p.add_argument("--kb-root", default=str(ROOT / "knowledge"))
    p.add_argument("--topics", nargs="+", default=["capl", "panel", "dbc", "xcp"])
    p.add_argument("--parser-template", choices=["v15", "v12"], default="v15")
    args = p.parse_args()
    print("[extract_v3] version=" + args.version + " chm_root=" + args.chm_root + " kb_root=" + args.kb_root)
    print("[extract_v3] topics=" + str(args.topics) + " template=" + args.parser_template)
    start = time.time()
    if args.parser_template == "v15":
        vp = _load_module("vp", os.path.join(PARSER_DIR, "01_vector_parser.py"))
    else:
        vp = _load_module("vp", os.path.join(PARSER_DIR, "05_vector_parser_v12.py"))
    cp = _load_module("cp", os.path.join(PARSER_DIR, "06_concept_parser.py"))
    rm = _load_module("rm", os.path.join(PARSER_DIR, "02_render_md.py"))
    stats = {}
    if "capl" in args.topics:
        s = extract_capl(
            os.path.join(args.chm_root, "CANoeCANalyzer", "Topics", "CAPLFunctions"),
            os.path.join(args.kb_root, args.version, "capl", "structured"),
            args.kb_root, args.version, vp, rm,
        )
        if s:
            stats["capl"] = s
    if "panel" in args.topics:
        panel_src = os.path.join(args.chm_root, "VectorToolsEnvironment", "Topics", "PanelDesigner")
        panel_dst = os.path.join(args.kb_root, args.version, "panel", "structured")
        if os.path.isdir(panel_src):
            n_ok, n_err = _walk_concept(panel_src, panel_dst, cp, rm, kind="Panel")
            stats["panel"] = dict(ok=n_ok, errors=n_err)
    if "dbc" in args.topics:
        dbc_src = os.path.join(args.chm_root, "CANeds", "Topics")
        dbc_dst = os.path.join(args.kb_root, args.version, "dbc", "structured")
        if os.path.isdir(dbc_src):
            n_ok, n_err = _walk_concept(dbc_src, dbc_dst, cp, rm, kind="DBC")
            stats["dbc"] = dict(ok=n_ok, errors=n_err)
    if "xcp" in args.topics:
        xcp_src = os.path.join(args.chm_root, "CANoeCANalyzer", "Topics", "CAPLFunctions", "XCP")
        xcp_dst = os.path.join(args.kb_root, args.version, "xcp", "structured")
        if os.path.isdir(xcp_src):
            n_ok, n_err = _walk_concept(xcp_src, xcp_dst, cp, rm, kind="XCP")
            stats["xcp"] = dict(ok=n_ok, errors=n_err)
    elapsed = time.time() - start
    NL = chr(10)
    print(NL + "[extract_v3] DONE in " + str(round(elapsed, 1)) + "s")
    print("[extract_v3] stats: " + json.dumps(stats, indent=2))
    print(NL + "[extract_v3] NEXT STEPS:")
    print("  1. Run: python -m retriever.build")
    print("  2. Update L1_latest -> knowledge/" + args.version + "/")
    print("  3. Add diff: scripts/diff/ --v-prev v15 --v-new " + args.version)


if __name__ == "__main__":
    main()
