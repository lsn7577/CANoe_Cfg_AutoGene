"""Concept-page extraction driver for Panel / DBC sources.

Walks the source root recursively, parses each .htm with the concept
parser, and emits per-file {json,md} plus a per-subcategory aggregate and a
global _index.json.
"""
import os
import sys
import json
import re
import time
from importlib import util as importlib_util


def _load_module(name, path):
    spec = importlib_util.spec_from_file_location(name, path)
    mod = importlib_util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _safe_filename(name):
    name = re.sub(r"[/\:\*\?\"<>|]", "_", name)
    name = re.sub(r"\s+", " ", name).strip()
    if not name:
        name = "unnamed"
    return name[:200]


def _find_subcategory(rel_path, source_layout="standard"):
    """Determine subcategory from relative path.

    For source_layout="standard", strip a leading Topics/ segment and use
    the next directory as subcategory. For source_layout="flat", use the
    parent directory of the file.
    """
    parts = rel_path.replace("\\", "/").split("/")
    if source_layout == "standard" and parts and parts[0].lower() == "topics":
        parts = parts[1:]
    if not parts:
        return ""
    if len(parts) >= 2:
        return parts[0]
    return ""


def run(src_root, output_root, category, version_label, source_layout="standard",
        parser_path=None, renderer_path=None):
    if parser_path is None:
        here = os.path.dirname(os.path.abspath(__file__))
        parser_path = os.path.join(here, "06_concept_parser.py")
    if renderer_path is None:
        renderer_path = os.path.join(here, "02_render_md.py")
    parser = _load_module("cp", parser_path)
    renderer = _load_module("rm", renderer_path)
    struct_root = os.path.join(output_root, "structured")
    os.makedirs(struct_root, exist_ok=True)
    by_subcat = {}
    errors = []
    total = 0
    start = time.time()
    if not os.path.isdir(src_root):
        print("[" + version_label + "] src_root not found: " + src_root)
        return {"total": 0, "errors": 0, "elapsed": 0}
    for r, dirs, fs in os.walk(src_root):
        for f in fs:
            if not f.lower().endswith(".htm"):
                continue
            fp = os.path.join(r, f)
            rel = os.path.relpath(fp, src_root)
            subcat = _find_subcategory(rel, source_layout)
            total += 1
            try:
                rec = parser.parse_concept_page(fp, category, subcat)
                if "error" in rec:
                    errors.append((fp, rec["error"]))
                    continue
                name = rec.get("name") or os.path.basename(fp).replace(".htm", "")
                fname = _safe_filename(name)
                subcat_dir = subcat or "_root"
                cat_struct = os.path.join(struct_root, subcat_dir)
                os.makedirs(cat_struct, exist_ok=True)
                json_path = os.path.join(cat_struct, fname + ".json")
                md_path = os.path.join(cat_struct, fname + ".md")
                with open(json_path, "w", encoding="utf-8") as fj:
                    json.dump(rec, fj, indent=2, ensure_ascii=False)
                with open(md_path, "w", encoding="utf-8") as fm:
                    fm.write(renderer.render_page_md(rec))
                by_subcat.setdefault(subcat_dir, []).append({
                    "name": name,
                    "file": os.path.basename(fp),
                    "page_type": rec.get("page_type", "concept"),
                    "json": os.path.relpath(json_path, output_root),
                    "md": os.path.relpath(md_path, output_root),
                })
            except Exception as e:
                errors.append((fp, str(e)))
    for subcat, items in by_subcat.items():
        items.sort(key=lambda x: x["name"].lower())
        with open(os.path.join(output_root, subcat + ".json"), "w", encoding="utf-8") as f:
            json.dump({
                "category": category,
                "subcategory": subcat,
                "page_count": len(items),
                "pages": items,
            }, f, indent=2, ensure_ascii=False)
    elapsed = time.time() - start
    idx = {
        "metadata": {
            "title": category + " (" + version_label + ") - structured",
            "category": category,
            "version": version_label,
            "source": src_root,
            "total_files": total,
            "total_errors": len(errors),
            "elapsed_seconds": round(elapsed, 2),
            "extracted_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        },
        "subcategories": {
            sc: {"page_count": len(items), "pages": [it["name"] for it in items]}
            for sc, items in sorted(by_subcat.items())
        },
    }
    with open(os.path.join(output_root, "_index.json"), "w", encoding="utf-8") as f:
        json.dump(idx, f, indent=2, ensure_ascii=False)
    print("[" + version_label + " " + category + "] Wrote " + str(len(by_subcat)) + " subcategories, " + str(total) + " files in " + str(round(elapsed, 1)) + "s; errors=" + str(len(errors)))
    if errors:
        print("  First 3 errors:")
        for fp, err in errors[:3]:
            print("    " + fp + ": " + err)
    return {"total": total, "errors": len(errors), "elapsed": elapsed}


if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python 07_extract_concept.py SRC_ROOT OUT_ROOT CATEGORY VERSION [LAYOUT]")
        sys.exit(1)
    src = sys.argv[1]
    out = sys.argv[2]
    cat = sys.argv[3]
    ver = sys.argv[4]
    layout = sys.argv[5] if len(sys.argv) > 5 else "standard"
    run(src, out, cat, ver, source_layout=layout)
