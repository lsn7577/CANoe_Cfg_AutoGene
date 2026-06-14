"""Generic structured extraction driver - parameterized by source root and output dir.

Usage:
  from importlib import util
  spec = util.spec_from_file_location("driver", path)
  driver = util.module_from_spec(spec); spec.loader.exec_module(driver)
  driver.run(src_root, output_root, source_label)
"""
import os, sys, json, re, time
from importlib import util as importlib_util


def _load_module(name, path):
    spec = importlib_util.spec_from_file_location(name, path)
    mod = importlib_util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _safe_filename(name):
    name = re.sub(r"[/\:*?\"<>|]", "_", name)
    name = re.sub(r"\s+", " ", name).strip()
    if not name:
        name = "unnamed"
    return name[:200]


def _walk_capl_files(root):
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


def run(src_root, output_root, source_label, parser_path, renderer_path, version_label):
    parser = _load_module("vp", parser_path)
    renderer = _load_module("rm", renderer_path)
    struct_root = os.path.join(output_root, "structured")
    os.makedirs(struct_root, exist_ok=True)
    categories = {}
    errors = []
    total = 0
    start = time.time()
    for fp, cat, rel in _walk_capl_files(src_root):
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
        with open(os.path.join(output_root, cat + ".json"), "w", encoding="utf-8") as f:
            json.dump({
                "category": cat,
                "function_count": len(funcs),
                "functions": funcs,
            }, f, indent=2, ensure_ascii=False)
    elapsed = time.time() - start
    idx = {
        "metadata": {
            "title": "CAPL Functions Index (" + version_label + ") - structured",
            "version": version_label,
            "source": source_label,
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
    by_type = {}
    for funcs in categories.values():
        for f in funcs:
            by_type[f["page_type"]] = by_type.get(f["page_type"], 0) + 1
    print("[" + version_label + "] Wrote " + str(len(categories)) + " categories, " + str(total) + " files in " + str(round(elapsed, 1)) + "s; types=" + str(by_type))
    if errors:
        print("[" + version_label + "] " + str(len(errors)) + " errors (first 3):")
        for fp, err in errors[:3]:
            print("  " + fp + ": " + err)
    return {"total": total, "errors": len(errors), "elapsed": elapsed, "by_type": by_type}


if __name__ == "__main__":
    # CLI: src_root output_root source_label version_label
    if len(sys.argv) < 5:
        print("Usage: python 04_extract_structured.py SRC_ROOT OUT_ROOT LABEL VERSION")
        sys.exit(1)
    run(sys.argv[1], sys.argv[2], sys.argv[3], os.path.join(os.path.dirname(__file__), "01_vector_parser.py"),
        os.path.join(os.path.dirname(__file__), "02_render_md.py"), sys.argv[4])
