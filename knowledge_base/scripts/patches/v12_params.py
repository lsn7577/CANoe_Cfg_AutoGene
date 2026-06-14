"""Patch v12 CAPL parameters extraction (T03).

Root cause: 05_vector_parser_v12.py _extract_params_v12() only looks for
parameters in an inner <table>, but v12 actually uses alternating
<p class=Bold>name</p> + <p>description</p> pairs.
"""
import os, sys, json, re, argparse
from pathlib import Path
from lxml import html as lxml_html

ROOT = Path(__file__).resolve().parents[2]
PARSER_DIR = ROOT / "scripts" / "extract" / "v2"
V12_SRC = Path(os.environ.get(
    "CANOE_V12_CAPL_DIR",
    ROOT / "chm_extract_v12" / "CANoeCANalyzer" / "Topics" / "CAPLFunctions",
))
V12_DST = ROOT / "knowledge" / "v12" / "capl" / "structured"

sys.path.insert(0, str(PARSER_DIR))
from importlib import util as iu
sp = iu.spec_from_file_location("vp", PARSER_DIR / "05_vector_parser_v12.py")
vp = iu.module_from_spec(sp)
sp.loader.exec_module(vp)


def clean(s):
    if s is None: return ""
    s = s.replace(chr(9), " ").replace(chr(13), " ")
    s = re.sub(r"[ ]+", " ", s)
    s = s.replace(chr(0xa0), " ").replace(chr(0x200b), "")
    s = re.sub(r"\s+", " ", s).strip()
    return s


def extract_params_fixed(td):
    params = []
    for tbl in td.xpath(".//table[not(ancestor::table)]"):
        for row in tbl.xpath(".//tr"):
            if row.xpath(".//table"): continue
            cells = [clean(c.text_content()) for c in row.xpath(".//th|.//td")]
            cells = [c for c in cells if c]
            if not cells: continue
            if len(cells) == 2: params.append(dict(name=cells[0], type="", description=cells[1]))
            elif len(cells) == 3: params.append(dict(name=cells[0], type=cells[1], description=cells[2]))
            else: params.append(dict(name=cells[0], type="", description=" ".join(cells[1:])))
    if params: return params
    name = None
    for p in td.xpath(".//p"):
        cls = p.get("class", "")
        text = clean(p.text_content())
        if not text: continue
        is_bold = "Bold" in cls or "TableHead" in cls or "TableSymbolHead" in cls
        if is_bold: name = text
        elif name is not None:
            params.append(dict(name=name, type="", description=text))
            name = None
    if name is not None and (not params or params[-1].get("name") != name):
        params.append(dict(name=name, type="", description=""))
    return params


def parse_v12_fixed(fp, cat):
    with open(fp, "rb") as f: raw = f.read()
    raw = re.sub(rb"<\?xml[^?]+\?>", b"", raw)
    try: html_str = raw.decode("windows-1252", errors="ignore")
    except Exception: html_str = raw.decode("utf-8", errors="ignore")
    tree = lxml_html.fromstring(html_str)
    main = vp._find_main_table(tree)
    if main is None: return None
    rec = {}
    rec["page_type"] = "function"
    rec["name"] = vp._get_title_v12(tree)
    rec["category"] = cat
    rec["source"] = fp
    rec["syntax"] = []
    rec["description"] = []
    rec["parameters"] = []
    rec["return"] = []
    rec["example"] = dict(description=[], code="")
    rec["availability"] = []
    rec["selectors"] = []
    rec["note"] = []
    for label, td in vp._find_label_rows(main):
        if label == "_example":
            rec["example"]["code"] = vp._extract_text_v12(td)
            continue
        target = vp.LABEL_MAP.get(label, label)
        if target == "syntax": rec["syntax"] = vp._extract_syntax_v12(td)
        elif target == "description": rec["description"] = vp._extract_description_v12(td)
        elif target == "parameters": rec["parameters"] = extract_params_fixed(td)
        elif target == "return":
            t = vp._extract_text_v12(td)
            rec["return"] = [t] if t else []
        elif target == "example": rec["example"]["code"] = vp._extract_text_v12(td)
        elif target == "availability": rec["availability"] = [vp._extract_text_v12(td)]
        elif target == "selectors": rec["selectors"] = [vp._extract_text_v12(td)]
    if not rec["name"]:
        rec["name"] = os.path.basename(fp).replace(".htm", "")
    return rec


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--limit", type=int, default=0)
    args = p.parse_args()
    if not os.path.isdir(V12_SRC):
        print("ERROR: source not found:", V12_SRC)
        return
    if not os.path.isdir(V12_DST):
        print("ERROR: dst not found:", V12_DST)
        return
    pre_total = pre_with = 0
    for cat in os.listdir(V12_DST):
        cd = os.path.join(V12_DST, cat)
        if not os.path.isdir(cd): continue
        for f in os.listdir(cd):
            if not f.endswith(".json"): continue
            pre_total += 1
            try:
                with open(os.path.join(cd, f), "r", encoding="utf-8") as ff:
                    if json.load(ff).get("parameters"): pre_with += 1
            except Exception: pass
    pct = pre_with / pre_total * 100 if pre_total else 0
    print("[BEFORE] total=" + str(pre_total) + " with_params=" + str(pre_with) + " (" + str(round(pct, 1)) + "%)")
    new_total = new_with = updated = 0
    files = []
    for cat in os.listdir(V12_SRC):
        cat_src = os.path.join(V12_SRC, cat)
        if not os.path.isdir(cat_src): continue
        for root, _, fs in os.walk(cat_src):
            for f in fs:
                if f.lower().endswith(".htm"): files.append((cat, os.path.join(root, f)))
    print("Source files:", len(files))
    for i, (cat, fp) in enumerate(files):
        if args.limit and i >= args.limit: break
        try: rec = parse_v12_fixed(fp, cat)
        except Exception: continue
        if rec is None: continue
        new_total += 1
        if rec.get("parameters"): new_with += 1
        safe_name = re.sub(r"[/\:*?<>|]", "_", rec["name"])[:200] or "unnamed"
        existing = os.path.join(V12_DST, cat, safe_name + ".json")
        if os.path.exists(existing):
            try:
                with open(existing, "r", encoding="utf-8") as ff: old = json.load(ff)
                if rec.get("parameters") and not old.get("parameters"):
                    old["parameters"] = rec["parameters"]
                    if not args.dry_run:
                        with open(existing, "w", encoding="utf-8") as ff: json.dump(old, ff, indent=2, ensure_ascii=False)
                    updated += 1
            except Exception: pass
    pct2 = new_with / new_total * 100 if new_total else 0
    print("[AFTER patch] total=" + str(new_total) + " with_params=" + str(new_with) + " (" + str(round(pct2, 1)) + "%) updated=" + str(updated))


if __name__ == "__main__": main()
