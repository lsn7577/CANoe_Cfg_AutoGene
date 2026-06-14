"""Patch v15 CAPL return/selectors coverage (T06).

Two issues addressed:

1. RETURN (35.3% coverage): Many functions have return type in syntax
   (e.g. 'dword a429CalcBitLength(...)') but the parser doesn't extract it.
   Fix: extract first token of syntax as return type if return is empty.

2. SELECTORS (1.5% coverage): Selector pages (e.g. CAPLfunctionErrorFrameSelectors.htm)
   use a flat format with 164+ <p class=Table> paragraphs alternating
   name/desc/type, with NO DIVCAPLSelectors div. Fix: detect selector pages
   by title and extract from the flat pattern.

Usage: python scripts/patch_v15_return_sel.py [--dry-run] [--limit N]
"""
import os, sys, json, re, argparse
from pathlib import Path
from lxml import html as lxml_html
from importlib import util as importlib_util

ROOT = Path(__file__).resolve().parents[2]
PARSER_DIR = ROOT / "scripts" / "extract" / "v2"
V15_SRC = Path(os.environ.get(
    "CANOE_V15_CAPL_DIR",
    ROOT / "chm_extract_v15" / "CANoeCANalyzer" / "Topics" / "CAPLFunctions",
))
V15_DST = ROOT / "knowledge" / "v15" / "capl" / "structured"

sys.path.insert(0, str(PARSER_DIR))
spec = importlib_util.spec_from_file_location("vp", PARSER_DIR / "01_vector_parser.py")
vp = importlib_util.module_from_spec(spec)
spec.loader.exec_module(vp)


def extract_return_from_syntax(syntax_list):
    """If function has syntax like 'dword foo(long a)', extract 'dword' as return."""
    if not syntax_list:
        return []
    first = syntax_list[0].strip()
    # Match: TYPE FUNC_NAME(...)
    m = re.match(r"\s*(void|int|long|dword|byte|word|char|float|double|qword|int64|int32|int16|int8|uint|uint64|uint32|uint16|uint8|bool|struct\s+\w+|enum\s+\w+)\s+(\w+)\s*\(", first)
    if m:
        return [m.group(1)]
    return []


def extract_selectors_from_flat(tree):
    """Extract selectors from flat <p class=Table> pattern: name/desc/type repeating."""
    ps = tree.xpath('//p[@class="Table"]')
    if len(ps) < 6:  # not enough = probably not a flat selector page
        return []
    selectors = []
    # Pattern: name, desc, type, [empty], name, desc, type, ...
    i = 0
    while i + 2 < len(ps):
        name = ''.join(ps[i].itertext()).strip()
        desc = ''.join(ps[i+1].itertext()).strip() if i+1 < len(ps) else ""
        type_ = ''.join(ps[i+2].itertext()).strip() if i+2 < len(ps) else ""
        # Skip empty names or pure headings
        if not name or len(name) > 80 or name.startswith('Note'):
            i += 1
            continue
        # Skip if name looks like a type (word, dword, int, etc.)
        if name.lower() in ('void', 'int', 'long', 'dword', 'byte', 'word', 'char', 'float', 'double', 'qword', 'int64'):
            i += 1
            continue
        sel = {"name": name}
        if desc and desc != name:
            sel["description"] = desc
        if type_ and type_ not in (name, desc):
            sel["type"] = type_
        selectors.append(sel)
        i += 3  # skip name, desc, type; optionally skip empty at next
    return selectors


def is_selector_page(filepath, tree):
    """Detect if a page is a 'Selectors' page (flat format)."""
    name = os.path.basename(filepath).lower()
    if "selector" in name:
        return True
    h1 = tree.xpath('//h1')
    if h1 and "selector" in h1[0].text_content().lower():
        return True
    return False


def patch_file(filepath, category):
    """Re-parse and patch return + selectors."""
    try:
        tree = vp._load_html(filepath)
    except Exception:
        return None
    rec = vp.parse_page(filepath, category)
    if "error" in rec:
        return rec

    # Patch 1: return from syntax
    if not rec.get("return") and rec.get("syntax") and rec.get("page_type") == "function":
        ret = extract_return_from_syntax(rec["syntax"])
        if ret:
            rec["return"] = ret

    # Patch 2: selectors from flat page
    if is_selector_page(filepath, tree) and not rec.get("selectors"):
        sels = extract_selectors_from_flat(tree)
        if sels:
            rec["selectors"] = sels

    return rec


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--limit", type=int, default=0)
    args = p.parse_args()
    if not os.path.isdir(V15_SRC):
        print("ERROR: v15 source not found:", V15_SRC)
        return
    if not os.path.isdir(V15_DST):
        print("ERROR: v15 dst not found:", V15_DST)
        return

    pre_total = pre_ret = pre_sel = 0
    for cat in os.listdir(V15_DST):
        cd = os.path.join(V15_DST, cat)
        if not os.path.isdir(cd): continue
        for f in os.listdir(cd):
            if not f.endswith(".json"): continue
            pre_total += 1
            try:
                with open(os.path.join(cd, f), "r", encoding="utf-8") as ff:
                    r = json.load(ff)
                if r.get("return"): pre_ret += 1
                if r.get("selectors"): pre_sel += 1
            except Exception:
                pass
    pr = round(pre_ret/pre_total*100, 1) if pre_total else 0
    ps = round(pre_sel/pre_total*100, 1) if pre_total else 0
    print("[BEFORE] total=" + str(pre_total) + " return=" + str(pre_ret) + " (" + str(pr) + "%) selectors=" + str(pre_sel) + " (" + str(ps) + "%)")

    new_total = upd_ret = upd_sel = 0
    files = []
    for cat in os.listdir(V15_SRC):
        cat_src = os.path.join(V15_SRC, cat)
        if not os.path.isdir(cat_src): continue
        for root, _, fs in os.walk(cat_src):
            for f in fs:
                if f.lower().endswith(".htm"): files.append((cat, os.path.join(root, f)))
    print("Source files:", len(files))

    for i, (cat, fp) in enumerate(files):
        if args.limit and i >= args.limit: break
        rec = patch_file(fp, cat)
        if rec is None or "error" in rec: continue
        new_total += 1
        safe_name = re.sub(r"[/\:*?\"<>|]", "_", rec.get("name", "unnamed"))[:200] or "unnamed"
        existing = os.path.join(V15_DST, cat, safe_name + ".json")
        if not os.path.exists(existing): continue
        try:
            with open(existing, "r", encoding="utf-8") as ff: old = json.load(ff)
            changed = False
            if rec.get("return") and not old.get("return"):
                old["return"] = rec["return"]
                upd_ret += 1
                changed = True
            if rec.get("selectors") and not old.get("selectors"):
                old["selectors"] = rec["selectors"]
                upd_sel += 1
                changed = True
            if changed and not args.dry_run:
                with open(existing, "w", encoding="utf-8") as ff:
                    json.dump(old, ff, indent=2, ensure_ascii=False)
        except Exception:
            pass
    print("[AFTER patch] updated_return=" + str(upd_ret) + " updated_selectors=" + str(upd_sel))


if __name__ == "__main__":
    main()
