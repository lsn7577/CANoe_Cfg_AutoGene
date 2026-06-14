"""Simple direct-parse patch for v15 return/selectors (T06 v2).

Root cause: v15 parser's find_sections() returns empty because v15 source HTM
files lack the expected MadCap:targetName divs. So parse_page() misclassifies
~80% of pages as 'notes' with empty syntax/return/selectors.

This patch takes a DIFFERENT approach: bypass parse_page() and directly
extract return/selectors from raw HTML using pattern matching.
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


def _load_html(filepath):
    with open(filepath, "rb") as f:
        raw = f.read()
    raw = re.sub(rb"<\?xml[^?]+\?>", b"", raw)
    try:
        html_str = raw.decode("utf-8", errors="ignore")
    except Exception:
        html_str = raw.decode("windows-1252", errors="ignore")
    return lxml_html.fromstring(html_str)


def direct_extract_return_selectors(filepath):
    """Bypass parse_page; directly extract return + selectors from HTML."""
    try:
        tree = _load_html(filepath)
    except Exception:
        return None
    name = os.path.basename(filepath)
    is_selector_page = "selector" in name.lower()

    # Strategy 1: For "function" pages, find return from signature
    # Look for first <p> with class=TableSyntax or first paragraph
    syntax_p = tree.xpath('//p[@class="TableSyntax"]')
    if not syntax_p:
        syntax_p = tree.xpath('//p[@class="Table"]')
    syntax_text = ""
    for p in syntax_p[:5]:
        text = "".join(p.itertext()).strip()
        if "(" in text and ")" in text:
            syntax_text = text
            break

    return_val = ""
    if syntax_text and not is_selector_page:
        m = re.match(r"\s*(\w+(?:\s+\w+)*)\s+(\w+)\s*\(", syntax_text)
        if m:
            rt = m.group(1)
            if rt.lower() not in ("void",) and rt not in ("if", "for", "while", "switch", "return"):
                return_val = rt

    # Strategy 2: For "selector" pages, extract name/desc/type triples
    selectors = []
    if is_selector_page:
        ps = tree.xpath('//p[@class="Table"]')
        i = 0
        while i + 2 < len(ps):
            n = "".join(ps[i].itertext()).strip()
            d = "".join(ps[i+1].itertext()).strip() if i+1 < len(ps) else ""
            t = "".join(ps[i+2].itertext()).strip() if i+2 < len(ps) else ""
            if not n or len(n) > 80 or n == "Note":
                i += 1
                continue
            if n.lower() in ("void", "int", "long", "dword", "byte", "word", "char", "float", "double"):
                i += 1
                continue
            sel = {"name": n}
            if d and d != n:
                sel["description"] = d
            if t and t not in (n, d):
                sel["type"] = t
            selectors.append(sel)
            i += 3

    return {"return": return_val, "selectors": selectors}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--limit", type=int, default=0)
    args = p.parse_args()

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
        ext = direct_extract_return_selectors(fp)
        if ext is None: continue
        new_total += 1
        # Match by source basename
        cat_dir = os.path.join(V15_DST, cat)
        if not os.path.isdir(cat_dir): continue
        existing = None
        src_basename = os.path.basename(fp).lower()
        for fname in os.listdir(cat_dir):
            if not fname.endswith(".json"): continue
            fpath = os.path.join(cat_dir, fname)
            try:
                with open(fpath, "r", encoding="utf-8") as fff:
                    r = json.load(fff)
                stored_src = os.path.basename(r.get("source", "")).lower()
                if stored_src == src_basename:
                    existing = fpath
                    break
            except Exception:
                pass
        if existing is None: continue
        try:
            with open(existing, "r", encoding="utf-8") as ff: old = json.load(ff)
            changed = False
            if ext["return"] and not old.get("return"):
                old["return"] = ext["return"]
                upd_ret += 1
                changed = True
            if ext["selectors"] and not old.get("selectors"):
                old["selectors"] = ext["selectors"]
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
