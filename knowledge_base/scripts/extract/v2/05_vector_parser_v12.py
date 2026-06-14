"""Vector v12 help parser (flat-table template).

v12 used a different HTML structure than v15. Each function page is a flat
<table> with <th>label</th> + <td>content</td> rows. We map known labels
to the same logical fields used by the v15 parser:

  Syntax     -> rec["syntax"]   (from <p class="TableSyntax">)
  Method     -> rec["syntax"]   (merged)
  Function   -> rec["description"]
  Parameters -> rec["parameters"] (from inner <table>)
  Return\xa0Values -> rec["return"]
  Example    -> rec["example"]
  Availability -> rec["availability"]
  Selectors  -> rec["selectors"]
"""
import os, re, json
from lxml import html as lxml_html


# Label -> logical field (lowercase, normalized to handle \xa0)
def _norm(s):
    if s is None:
        return ""
    s = s.replace(chr(0xa0), " ").replace(chr(0x200b), "")
    s = re.sub(r"\s+", " ", s).strip().lower()
    return s


LABEL_MAP = {
    "syntax": "syntax",
    "method": "method_syntax",
    "function": "description",
    "description": "description",
    "parameters": "parameters",
    "return values": "return",
    "return value": "return",
    "example": "example",
    "availability": "availability",
    "selectors": "selectors",
    "complexity": "complexity",
    "note": "note",
}


def _load_html(filepath):
    with open(filepath, "rb") as f:
        raw = f.read()
    raw = re.sub(rb"<\?xml[^?]+\?>", b"", raw)
    try:
        html_str = raw.decode("windows-1252", errors="ignore")
    except Exception:
        html_str = raw.decode("utf-8", errors="ignore")
    return lxml_html.fromstring(html_str)


def _clean(s):
    if s is None:
        return ""
    s = s.replace(chr(9), " ").replace(chr(13), " ")
    s = re.sub(r"[ ]+", " ", s)
    s = s.replace(chr(0xa0), " ").replace(chr(0x200b), "")
    s = re.sub(r"\s+", " ", s).strip()
    return s


def _get_title_v12(tree):
    sys_titles = tree.xpath(".//span[@class=\"SystemTitle\"]")
    if sys_titles:
        return _clean("".join(sys_titles[0].itertext()))
    title_nodes = tree.xpath("//title/text()")
    if title_nodes:
        return _clean(title_nodes[0])
    return ""


def _find_main_table(tree):
    """Find the v12 main content table (TableStyle_vTable)."""
    for tbl in tree.xpath(".//body//table"):
        cls = tbl.get("class", "")
        if "vTable" in cls and "MasterPage" not in cls and "Toolbar" not in cls:
            return tbl
    return None


def _find_label_rows(tbl):
    """Yield (label, td_elem) for each row where first th/cell is a known label.

    Also yields ("_example", td) for rows where the first cell is empty but
    the content cell contains a TableSourceCode paragraph (v12 puts examples
    in such unlabeled rows).
    """
    rows = tbl.xpath(".//tr")
    for row in rows:
        ths = row.xpath("./th|./td")
        if len(ths) < 2:
            continue
        label = _norm(ths[0].text_content())
        if label in LABEL_MAP:
            yield label, ths[1]
        elif label == "" and ths[1].xpath(".//p[@class=\"TableSourceCode\"]"):
            yield "_example", ths[1]


def _extract_syntax_v12(td):
    """Extract signature from <p class="TableSyntax">."""
    out = []
    seen = set()
    for p in td.xpath(".//p"):
        cls = p.get("class", "")
        if "TableSyntax" in cls or "Syntax" in cls:
            t = _clean(p.text_content())
            if t and t not in seen:
                seen.add(t)
                out.append(t)
    return out


def _extract_params_v12(td):
    """Extract parameters from inner <table>."""
    inner = td.xpath(".//table")
    if not inner:
        return []
    rows = inner[0].xpath(".//tr")
    params = []
    for row in rows:
        if row.xpath(".//table"):
            continue
        cells = row.xpath(".//th|.//td")
        cell_texts = [_clean(c.text_content()) for c in cells]
        cell_texts = [c for c in cell_texts if c]
        if not cell_texts:
            continue
        if len(cell_texts) == 2:
            params.append({"name": cell_texts[0], "type": "", "description": cell_texts[1]})
        elif len(cell_texts) == 3:
            params.append({"name": cell_texts[0], "type": cell_texts[1], "description": cell_texts[2]})
        else:
            params.append({"name": cell_texts[0], "type": "", "description": " ".join(cell_texts[1:])})
    return params


def _extract_description_v12(td):
    """Extract description paragraphs (non-code, non-table content)."""
    out = []
    seen = set()
    for p in td.xpath(".//p"):
        cls = p.get("class", "")
        if "TableSyntax" in cls or "TableSourceCode" in cls or "TableHead" in cls or "TableSymbolHead" in cls:
            continue
        t = _clean(p.text_content())
        if t and t not in seen:
            seen.add(t)
            out.append(t)
    return out


def _extract_text_v12(td):
    """Extract all <p> text concatenated."""
    out = []
    for p in td.xpath(".//p"):
        t = _clean(p.text_content())
        if t:
            out.append(t)
    return "\n".join(out)


def _text_with_br(elem):
    """Get text content of elem, treating <br/> as newline boundary."""
    if elem is None:
        return ""
    parts = []
    def walk(e):
        if e.tag == "br":
            parts.append(chr(10))
            return
        text = e.text
        if text:
            parts.append(text)
        for child in e:
            walk(child)
            if child.tail:
                parts.append(child.tail)
    walk(elem)
    return "".join(parts)


def _extract_example_v12(td):
    """Extract example: description paragraphs + code blocks."""
    desc = []
    code_lines = []
    seen = set()
    for p in td.xpath(".//p"):
        cls = p.get("class", "")
        t = _clean(p.text_content())
        if "TableSourceCode" in cls:
            raw = _text_with_br(p)
            for line in raw.split(chr(10)):
                code_lines.append(line)
        elif "TableSyntax" in cls or "TableHead" in cls or "TableSymbolHead" in cls:
            continue
        elif t and t not in seen:
            seen.add(t)
            desc.append(t)
    while code_lines and not code_lines[-1].strip():
        code_lines.pop()
    return {"description": desc, "code": chr(10).join(code_lines)}


def _extract_availability_v12(td):
    out = []
    for tbl in td.xpath(".//table"):
        for row in tbl.xpath(".//tr"):
            cells = row.xpath(".//th|.//td")
            cell_texts = [_clean(c.text_content()) for c in cells]
            cell_texts = [c for c in cell_texts if c]
            if cell_texts:
                out.append(cell_texts)
    if not out:
        t = _clean(td.text_content())
        if t:
            out.append([t])
    return out


def _extract_selectors_v12(td):
    out = []
    for tbl in td.xpath(".//table"):
        for row in tbl.xpath(".//tr"):
            cells = row.xpath(".//th|.//td")
            cell_texts = [_clean(c.text_content()) for c in cells]
            cell_texts = [c for c in cell_texts if c]
            if cell_texts:
                out.append({"row": cell_texts})
    for p in td.xpath(".//p"):
        for a in p.xpath(".//a"):
            txt = _clean(a.text_content())
            href = a.get("href", "")
            if txt and href:
                out.append({"name": txt, "link": href})
    return out


def parse_v12_page(filepath, category=""):
    """Parse a v12 Vector help file (flat-table template)."""
    try:
        tree = _load_html(filepath)
    except Exception as e:
        return {"error": "parse_failed: " + str(e), "source": str(filepath)}
    title = _get_title_v12(tree)
    tbl = _find_main_table(tree)
    rec = {
        "page_type": "function",
        "name": title,
        "category": category,
        "title": title,
        "source": str(filepath),
        "syntax": [],
        "description": [],
        "parameters": [],
        "return": "",
        "example": {"description": [], "code": ""},
        "availability": [],
        "selectors": [],
        "note": [],
        "complexity": "",
    }
    if tbl is None:
        # Concept/notes page
        rec["page_type"] = "notes" if not title.lower().startswith("on ") else "event"
        # Collect paragraphs
        body = []
        seen = set()
        for p in tree.xpath(".//body//p"):
            cls = p.get("class", "")
            if cls in ("StructurePath", "MenuPath", "Footer"):
                continue
            t = _clean(p.text_content())
            if t and t not in seen:
                seen.add(t)
                body.append(t)
        rec["description"] = body
        return rec
    # Detect event page
    title_lower = title.lower().strip()
    if title_lower.startswith("on "):
        rec["page_type"] = "event"
    # Walk labeled rows
    for label, td in _find_label_rows(tbl):
        if label == "_example":
            rec["example"] = _extract_example_v12(td)
            continue
        field = LABEL_MAP[label]
        if field == "syntax" or field == "method_syntax":
            for s in _extract_syntax_v12(td):
                if s not in rec["syntax"]:
                    rec["syntax"].append(s)
        elif field == "description":
            rec["description"] = _extract_description_v12(td)
        elif field == "parameters":
            rec["parameters"] = _extract_params_v12(td)
        elif field == "return":
            rec["return"] = _extract_text_v12(td)
        elif field == "example":
            rec["example"] = _extract_example_v12(td)
        elif field == "availability":
            rec["availability"] = _extract_availability_v12(td)
        elif field == "selectors":
            rec["selectors"] = _extract_selectors_v12(td)
        elif field == "complexity":
            rec["complexity"] = _extract_text_v12(td)
        elif field == "note":
            n = _extract_text_v12(td)
            if n:
                rec["note"].append(n)
        elif label == "_example":
            rec["example"] = _extract_example_v12(td)
    return rec


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python 05_vector_parser_v12.py <htm_file> [category]")
        sys.exit(1)
    fp = sys.argv[1]
    cat = sys.argv[2] if len(sys.argv) > 2 else ""
    rec = parse_v12_page(fp, cat)
    print(json.dumps(rec, indent=2, ensure_ascii=False))
