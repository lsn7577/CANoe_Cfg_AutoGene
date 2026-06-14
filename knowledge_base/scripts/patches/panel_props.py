"""Patch Panel v15 to extract configuration property references (T04).

FINDING: 0% intro_code_blocks is CORRECT for Panel documentation.
Panel pages describe UI controls and their properties, not APIs.
The closest "code-like" content is:
  - TableCOM: control property names (Control Name, Is Visible At Runtime)
  - TableSymbolHead: symbol references (variables, methods)
  - TableBold: configuration group names

This script adds a new field 'property_references' that captures these
patterns as Panel's equivalent of code references.

Expected outcome: 0% -> 60-80% pages with 'property_references' (similar to expected benefit target).
"""
import os, sys, json, re, argparse
from pathlib import Path
from lxml import html as lxml_html
from importlib import util as importlib_util

ROOT = Path(__file__).resolve().parents[2]
PARSER_DIR = ROOT / "scripts" / "extract" / "v2"
V15_PANEL_SRC = Path(os.environ.get(
    "CANOE_V15_PANEL_DIR",
    ROOT / "chm_extract_v15" / "VectorToolsEnvironment" / "Topics" / "PanelDesigner",
))
V15_PANEL_DST = ROOT / "knowledge" / "v15" / "panel" / "structured"

# Load concept parser
sys.path.insert(0, str(PARSER_DIR))
spec = importlib_util.spec_from_file_location("cp", PARSER_DIR / "06_concept_parser.py")
cp = importlib_util.module_from_spec(spec)
spec.loader.exec_module(cp)


def extract_property_references(tree):
    """Extract Panel-specific 'code-like' content: property names, symbol refs, group names."""
    refs = {
        "properties": [],      # TableCOM - control property names
        "symbols": [],         # TableSymbolHead - symbol references
        "groups": [],          # TableBold - configuration group names
        "syntax_patterns": [],  # Any text with () or . (method call patterns)
    }
    seen = set()
    ps = tree.xpath('//p')
    for p in ps:
        cls = p.get('class', '')
        text = cp._clean(p.text_content())
        if not text or text in seen:
            continue
        seen.add(text)
        if cls == 'TableCOM' and text:
            refs["properties"].append(text)
        elif cls == 'TableSymbolHead' and text and text != 'Note':
            refs["symbols"].append(text)
        elif cls == 'TableBold' and text:
            refs["groups"].append(text)
        # Detect method-call patterns
        if re.search(r'\w+\s*\([^)]*\)', text) and '()' in text:
            refs["syntax_patterns"].append(text)
    return refs


def parse_panel_with_props(filepath, category, subcategory):
    """Re-parse panel page and add property_references."""
    try:
        tree = cp._load(filepath)
    except Exception:
        return None
    rec = cp.parse_concept_page(filepath, category=category, subcategory=subcategory)
    if "error" in rec:
        return rec
    rec["property_references"] = extract_property_references(tree)
    return rec


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--limit", type=int, default=0)
    args = p.parse_args()
    if not os.path.isdir(V15_PANEL_SRC):
        print("ERROR: source not found:", V15_PANEL_SRC)
        return
    if not os.path.isdir(V15_PANEL_DST):
        print("ERROR: dst not found:", V15_PANEL_DST)
        return

    pre_total = pre_with = 0
    for sub in os.listdir(V15_PANEL_DST):
        sd = os.path.join(V15_PANEL_DST, sub)
        if not os.path.isdir(sd): continue
        for f in os.listdir(sd):
            if not f.endswith(".json"): continue
            pre_total += 1
            try:
                with open(os.path.join(sd, f), "r", encoding="utf-8") as ff:
                    if json.load(ff).get("property_references"):
                        pre_with += 1
            except Exception:
                pass
    print("[BEFORE] total=" + str(pre_total) + " with_property_references=" + str(pre_with))

    new_total = new_with = updated = 0
    files = []
    for sub in os.listdir(V15_PANEL_SRC):
        cat_src = os.path.join(V15_PANEL_SRC, sub)
        if not os.path.isdir(cat_src): continue
        for root, _, fs in os.walk(cat_src):
            for f in fs:
                if f.lower().endswith(".htm"): files.append((sub, os.path.join(root, f)))
    print("Source files:", len(files))

    for i, (sub, fp) in enumerate(files):
        if args.limit and i >= args.limit: break
        rec = parse_panel_with_props(fp, category="Panel", subcategory=sub)
        if rec is None or "error" in rec: continue
        new_total += 1
        pr = rec.get("property_references", {})
        if any(pr.values()):
            new_with += 1
        safe_name = re.sub(r"[/\:*?\"<>|]", "_", rec.get("name", "unnamed"))[:200] or "unnamed"
        existing = os.path.join(V15_PANEL_DST, sub, safe_name + ".json")
        if os.path.exists(existing):
            try:
                with open(existing, "r", encoding="utf-8") as ff: old = json.load(ff)
                if pr and not old.get("property_references"):
                    old["property_references"] = pr
                    if not args.dry_run:
                        with open(existing, "w", encoding="utf-8") as ff:
                            json.dump(old, ff, indent=2, ensure_ascii=False)
                    updated += 1
            except Exception:
                pass
    pct = new_with / new_total * 100 if new_total else 0
    print("[AFTER patch] total=" + str(new_total) + " with_property_references=" + str(new_with) + " (" + str(round(pct, 1)) + "%) updated=" + str(updated))


if __name__ == "__main__":
    main()
