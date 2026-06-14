"""Extract all v15 CAPL documentation into structured JSON + per-function MD.

Pipeline:
  1. Walk CAPLFunctions/<category>/**/*.htm
  2. For each file: parse with Vector template-aware parser
  3. Write per-function:
       L2/v15/capl/structured/<CATEGORY>/<name>.json   (structured data)
       L2/v15/capl/structured/<CATEGORY>/<name>.md     (rendered markdown)
  4. Write per-category aggregate:
       L2/v15/capl/<CATEGORY>.json     (list of all functions in that category)
  5. Write top-level index:
       L2/v15/capl/_index.json         (metadata + category list)
"""
import argparse
import os, sys, json, re, time
from importlib import util as importlib_util
from pathlib import Path


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = Path(__file__).resolve().parents[3]


def _load_module(name, path):
    spec = importlib_util.spec_from_file_location(name, path)
    mod = importlib_util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _safe_filename(name):
    """Sanitize a name for use as a filename."""
    name = re.sub(r"[/\:*?\"<>|]", "_", name)
    name = re.sub(r"\s+", " ", name).strip()
    if not name:
        name = "unnamed"
    return name[:200]


def _walk_capl_files(root):
    """Yield (filepath, category, subdir_relative) tuples."""
    if not os.path.isdir(root):
        return
    for cat in sorted(os.listdir(root)):
        cat_dir = os.path.join(root, cat)
        if not os.path.isdir(cat_dir):
            continue
        for r, dirs, fs in os.walk(cat_dir):
            for f in fs:
                if f.lower().endswith(".htm"):
                    fp = os.path.join(r, f)
                    rel = os.path.relpath(fp, cat_dir)
                    yield fp, cat, rel


def main():
    ap = argparse.ArgumentParser(description="Extract v15 CAPL docs into structured JSON/MD")
    ap.add_argument("--capl-src", default=os.environ.get("CANOE_V15_CAPL_DIR", ""))
    ap.add_argument("--output-root", default=str(ROOT / "knowledge" / "v15" / "capl"))
    args = ap.parse_args()
    capl_src = args.capl_src
    output_root = args.output_root
    if not capl_src:
        print("ERROR: --capl-src is required, or set CANOE_V15_CAPL_DIR")
        return 1
    if not os.path.isdir(capl_src):
        print("ERROR: source not found:", capl_src)
        return 1

    parser = _load_module("vp", os.path.join(SCRIPT_DIR, "01_vector_parser.py"))
    renderer = _load_module("rm", os.path.join(SCRIPT_DIR, "02_render_md.py"))
    struct_root = os.path.join(output_root, "structured")
    os.makedirs(struct_root, exist_ok=True)
    categories = {}  # cat -> list of {name, file, page_type}
    errors = []
    total = 0
    start = time.time()
    for fp, cat, rel in _walk_capl_files(capl_src):
        total += 1
        try:
            rec = parser.parse_page(fp, cat)
            if "error" in rec:
                errors.append((fp, rec["error"]))
                continue
            name = rec.get("name") or os.path.basename(fp).replace(".htm", "")
            fname = _safe_filename(name)
            cat_struct_dir = os.path.join(struct_root, cat)
            os.makedirs(cat_struct_dir, exist_ok=True)
            json_path = os.path.join(cat_struct_dir, fname + ".json")
            md_path = os.path.join(cat_struct_dir, fname + ".md")
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(rec, f, indent=2, ensure_ascii=False)
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(renderer.render_page_md(rec))
            categories.setdefault(cat, []).append({
                "name": name,
                "file": os.path.basename(fp),
                "page_type": rec.get("page_type", "notes"),
                "json": os.path.relpath(json_path, output_root),
                "md": os.path.relpath(md_path, output_root),
            })
        except Exception as e:
            errors.append((fp, str(e)))

    # Per-category aggregate
    for cat, funcs in categories.items():
        funcs.sort(key=lambda x: x["name"].lower())
        cat_data = {
            "category": cat,
            "function_count": len(funcs),
            "functions": funcs,
        }
        with open(os.path.join(output_root, cat + ".json"), "w", encoding="utf-8") as f:
            json.dump(cat_data, f, indent=2, ensure_ascii=False)
    # Top-level index
    elapsed = time.time() - start
    idx = {
        "metadata": {
            "title": "CAPL Functions Index (Vector CANoe 15.0) - structured",
            "version": "15.0",
            "source": "Vector CANoe 15.0 Help - CAPLFunctions",
            "total_files": total,
            "total_errors": len(errors),
            "elapsed_seconds": round(elapsed, 2),
            "extracted_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        },
        "categories": {
            cat: {
                "function_count": len(funcs),
                "functions": [f["name"] for f in funcs],
            }
            for cat, funcs in sorted(categories.items())
        },
    }
    with open(os.path.join(output_root, "_index.json"), "w", encoding="utf-8") as f:
        json.dump(idx, f, indent=2, ensure_ascii=False)
    print("[OK] Wrote " + str(len(categories)) + " categories, " + str(total) + " files in " + str(round(elapsed, 1)) + "s")
    if errors:
        print("[WARN] " + str(len(errors)) + " errors (first 5):")
        for fp, err in errors[:5]:
            print("  " + fp + ": " + err)
    # Quick quality summary
    by_type = {}
    for funcs in categories.values():
        for f in funcs:
            by_type[f["page_type"]] = by_type.get(f["page_type"], 0) + 1
    print("Page types:", by_type)


if __name__ == "__main__":
    sys.exit(main() or 0)
