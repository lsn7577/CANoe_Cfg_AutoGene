"""Vector-template-aware HTML parser for MadCap-flavored help docs.

Recognizes Vector CANoe/CAPL/other help page templates and produces a
structured dict per page with these keys:
  page_type    : function | method | event | selector | concept | notes
  name         : page title (SystemTitle from h1, falls back to <title>)
  category     : pass-through category (set by caller)
  title        : same as name (kept for clarity)
  source       : absolute path of the source HTM file
  syntax       : list[str] - C/CAPL signature lines from <p class="Syntax">
  description  : list[str] - paragraph text (clean, no code/tables)
  parameters   : list[{name, type, description}] - from parameters table
  return       : str - return-value description (concatenated paragraphs)
  example      : {description: [str], code: str} - from example section
  availability : list[list[str]] - version matrix rows
  selectors    : list[{name, link?, row?}] - from selectors section
  note         : list[str] - any Note callouts
  complexity   : str - O(...) if present
  tables       : list[list[list[str]]] - for concept/notes pages
"""
import os, re, json
from lxml import html as lxml_html


# Section target names -> logical names
SECTION_TARGETS = {
    "DIVCAPLFunctionSyntax": "function_syntax",
    "DIVCAPLMethodSyntax": "method_syntax",
    "DIVCAPLDescription": "description",
    "DIVCAPLComplexity": "complexity",
    "DIVCAPLParameters": "parameters",
    "DIVCAPLReturnValues": "return_values",
    "DIVCAPLExample": "example",
    "DIVCAPLAvailability": "availability",
    "DIVCAPLSelectors": "selectors",
    "DIVCAPLSelectorDescription": "selector_description",
}


def clean_text(s):
    """Normalize whitespace, collapse runs of spaces/tabs to a single space."""
    if s is None:
        return ""
    if not isinstance(s, str):
        s = str(s)
    s = s.replace(chr(9), " ").replace(chr(13), " ")
    s = re.sub(r"[ ]+", " ", s)
    s = s.replace(chr(0xa0), " ").replace(chr(0x200b), "")
    s = re.sub(r"\s+", " ", s).strip()
    return s


def load_html(filepath):
    """Read a Vector help file (typically Windows-1252) and return an lxml tree."""
    with open(filepath, "rb") as f:
        raw = f.read()
    raw = re.sub(rb"<\?xml[^?]+\?>", b"", raw)
    try:
        html_str = raw.decode("windows-1252", errors="ignore")
    except Exception:
        html_str = raw.decode("utf-8", errors="ignore")
    return lxml_html.fromstring(html_str)


def get_title(tree):
    """Get the page title from h1 > span.SystemTitle, falling back to <title>."""
    sys_titles = tree.xpath(".//span[@class=\"SystemTitle\"]")
    if sys_titles:
        return clean_text("".join(sys_titles[0].itertext()))
    title_nodes = tree.xpath("//title/text()")
    if title_nodes:
        return clean_text(title_nodes[0])
    return ""


def find_sections(tree):
    """Return dict: section_targetName -> lxml div element.

    lxml lowercases the MadCap namespace attribute to madcap:targetname,
    so we check both forms to be safe.
    """
    sections = {}
    for div in tree.xpath(".//div"):
        target = div.get("MadCap:targetName") or div.get("madcap:targetname")
        if target and target in SECTION_TARGETS:
            sections[target] = div
    return sections


def extract_paragraphs_from_div(elem, skip_class_substrings=()):
    """Extract <p> text from a div (recursively, but not through tables)."""
    if elem is None:
        return []
    out = []
    seen = set()
    p_elems = []

    def walk(e):
        for child in e:
            if child.tag == "p":
                p_elems.append(child)
            elif child.tag == "div":
                walk(child)

    walk(elem)
    for p in p_elems:
        cls = p.get("class", "")
        if any(sub in cls for sub in skip_class_substrings):
            continue
        t = clean_text(p.text_content())
        if t and t not in seen:
            seen.add(t)
            out.append(t)
    return out


def extract_signature_lines(elem):
    """Extract C/CAPL signature lines from <p class="Syntax">."""
    if elem is None:
        return []
    out = []
    seen = set()
    for p in elem.xpath(".//p"):
        cls = p.get("class", "")
        if "Syntax" in cls:
            t = clean_text(p.text_content())
            if t and t not in seen:
                seen.add(t)
                out.append(t)
    return out


def extract_parameters(elem):
    """Extract parameter table as list of {name, type, description}.

    Skips rows that contain a nested table (sub-struct definitions).
    """
    if elem is None:
        return []
    tables = elem.xpath(".//table")
    if not tables:
        return []
    nested_under = set()
    for t in tables:
        parent = t.getparent()
        while parent is not None and parent.tag != "body":
            if parent.tag == "table":
                nested_under.add(id(t))
                break
            parent = parent.getparent()
    tbl = None
    for t in tables:
        if id(t) not in nested_under:
            tbl = t
            break
    if tbl is None:
        return []
    rows = tbl.xpath(".//tr")
    if not rows:
        return []
    params = []
    for row in rows:
        if row.xpath(".//table"):
            continue
        cells = row.xpath("./th|./td")
        if not cells:
            cells = row.xpath(".//th|.//td")
        if not cells:
            continue
        cell_texts = [clean_text(c.text_content()) for c in cells]
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


def extract_availability(elem):
    """Extract availability/version matrix as list of rows-of-cells."""
    if elem is None:
        return []
    tables = elem.xpath(".//table")
    if not tables:
        text = clean_text(elem.text_content())
        return [text] if text else []
    out = []
    for tbl in tables:
        for row in tbl.xpath(".//tr"):
            cells = row.xpath(".//th|.//td")
            cell_texts = [clean_text(c.text_content()) for c in cells]
            cell_texts = [c for c in cell_texts if c]
            if cell_texts:
                out.append(cell_texts)
    return out


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


def extract_example(elem):
    """Extract example: descriptive paragraphs + source code blocks."""
    if elem is None:
        return {"description": [], "code": ""}
    desc = []
    code_lines = []
    seen_desc = set()
    for p in elem.xpath(".//p"):
        cls = p.get("class", "")
        t = clean_text(p.text_content())
        if not t:
            continue
        if "TableSourceCode" in cls:
            raw = _text_with_br(p)
            for line in raw.split(chr(10)):
                code_lines.append(line)
        elif "TableSymbolHead" in cls:
            if t not in seen_desc:
                seen_desc.add(t)
                desc.append(t)
        elif "Table" in cls:
            if t not in seen_desc:
                seen_desc.add(t)
                desc.append(t)
    while code_lines and not code_lines[-1].strip():
        code_lines.pop()
    code = chr(10).join(code_lines)
    return {"description": desc, "code": code}


def extract_selectors(elem):
    """Extract selectors: try table rows first, then <a href> link list."""
    if elem is None:
        return []
    out = []
    seen = set()
    tables = elem.xpath(".//table")
    if tables:
        nested_under = set()
        for t in tables:
            parent = t.getparent()
            while parent is not None and parent.tag != "body":
                if parent.tag == "table":
                    nested_under.add(id(t))
                    break
                parent = parent.getparent()
        tbl = None
        for t in tables:
            if id(t) not in nested_under:
                tbl = t
                break
        if tbl is not None:
            for row in tbl.xpath(".//tr"):
                cells = row.xpath(".//th|.//td")
                cell_texts = [clean_text(c.text_content()) for c in cells]
                cell_texts = [c for c in cell_texts if c]
                if cell_texts:
                    key = tuple(cell_texts)
                    if key not in seen:
                        seen.add(key)
                        out.append({"row": cell_texts})
    for p in elem.xpath(".//p"):
        for a in p.xpath(".//a"):
            txt = clean_text(a.text_content())
            href = a.get("href", "")
            if txt and href and txt not in seen:
                seen.add(txt)
                out.append({"name": txt, "link": href})
    return out


def extract_description(elem):
    """Extract description: list of plain paragraphs (text only)."""
    return extract_paragraphs_from_div(
        elem,
        skip_class_substrings=("TableSourceCode", "Syntax", "TableSymbolHead")
    )


def detect_page_type(title, sections, tree):
    """Classify the page based on title and which sections are present.

    Improved v3 logic (2026-06-10):
    - Selector pages: any page whose title ends with "Selectors" (and has no syntax)
      is a selector page, not notes/concept. This fixes the v15 issue where
      CAN Message Selectors / CAN Error Frame Selectors were tagged 'notes'.
    - Overview / function-list pages: title ends with "Functions" + " " in title
      -> concept (function index page).
    """
    title_lower = (title or "").lower().strip()
    if title_lower.startswith("on "):
        return "event"
    if "DIVCAPLMethodSyntax" in sections and "DIVCAPLFunctionSyntax" not in sections:
        return "method"
    if "DIVCAPLFunctionSyntax" in sections:
        return "function"
    if "DIVCAPLMethodSyntax" in sections:
        return "method"
    # Selector detection: page ends with "Selectors" (or " Selector")
    if title_lower.endswith("selectors") or title_lower.endswith("selector"):
        return "selector"
    # Example selector pages
    if title_lower.startswith("example: selector") or title_lower.startswith("example selector"):
        return "selector"
    if "selectors" in title_lower and "example" in title_lower:
        return "selector"
    # Overview / function-index pages
    if "overview" in title_lower:
        return "concept"
    if "function" in title_lower and "overview" in title_lower:
        return "concept"
    # "X CAPL Functions" / "X Functions" -> function index
    if title_lower.endswith("functions") and " " in title_lower:
        return "concept"
    return "notes"


def extract_notes_concept(tree):
    """For concept/notes pages, extract title + body paragraphs + tables."""
    title = get_title(tree)
    body = []
    seen = set()
    for p in tree.xpath(".//body//p"):
        cls = p.get("class", "")
        if cls in ("StructurePath", "MenuPath", "Footer"):
            continue
        if "Table" in cls:
            continue
        t = clean_text(p.text_content())
        if t and t not in seen:
            seen.add(t)
            body.append(t)
    tables = []
    for tbl in tree.xpath(".//body//table[not(ancestor::table)]"):
        cls = tbl.get("class", "")
        if "MasterPage" in cls or "Toolbar" in cls or "Footer" in cls:
            continue
        rows = []
        for row in tbl.xpath(".//tr"):
            cells = [clean_text(c.text_content()) for c in row.xpath(".//th|.//td")]
            cells = [c for c in cells if c]
            if cells:
                rows.append(cells)
        if rows:
            tables.append(rows)
    return {"title": title, "paragraphs": body, "tables": tables}


def extract_selector_page(tree):
    """For selector pages, extract per-example {name, description, code}."""
    out = []
    for tbl in tree.xpath(".//table[contains(@class, \"TableStyle-vTableSymbol\")]"):
        head = tbl.xpath(".//p[@class=\"TableSymbolHead\"]")
        code = tbl.xpath(".//p[@class=\"TableSourceCode\"]")
        desc = []
        for p in tbl.xpath(".//p"):
            cls = p.get("class", "")
            if "TableSymbolHead" in cls or "TableSourceCode" in cls:
                continue
            t = clean_text(p.text_content())
            if t and t not in desc:
                desc.append(t)
        out.append({
            "name": clean_text(head[0].text_content()) if head else "",
            "description": desc,
            "code": chr(10).join(_text_with_br(c) for c in code) if code else "",
        })
    return out


def parse_page(filepath, category=""):
    """Main entry. Parse a Vector help file into a structured dict."""
    try:
        tree = load_html(filepath)
    except Exception as e:
        return {"error": "parse_failed: " + str(e), "source": str(filepath)}
    title = get_title(tree)
    sections = find_sections(tree)
    page_type = detect_page_type(title, sections, tree)
    rec = {
        "page_type": page_type,
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
    if page_type == "function":
        rec["syntax"] = extract_signature_lines(sections.get("DIVCAPLFunctionSyntax"))
        rec["description"] = extract_description(sections.get("DIVCAPLDescription"))
        rec["parameters"] = extract_parameters(sections.get("DIVCAPLParameters"))
        rv = sections.get("DIVCAPLReturnValues")
        if rv is not None:
            paragraphs = extract_description(rv)
            rec["return"] = "\n".join(paragraphs) if paragraphs else ""
        rec["example"] = extract_example(sections.get("DIVCAPLExample"))
        rec["availability"] = extract_availability(sections.get("DIVCAPLAvailability"))
    elif page_type == "method":
        rec["syntax"] = extract_signature_lines(sections.get("DIVCAPLMethodSyntax"))
        rec["description"] = extract_description(sections.get("DIVCAPLDescription"))
        rec["parameters"] = extract_parameters(sections.get("DIVCAPLParameters"))
        rv = sections.get("DIVCAPLReturnValues")
        if rv is not None:
            paragraphs = extract_description(rv)
            rec["return"] = "\n".join(paragraphs) if paragraphs else ""
        rec["example"] = extract_example(sections.get("DIVCAPLExample"))
        rec["availability"] = extract_availability(sections.get("DIVCAPLAvailability"))
    elif page_type == "event":
        rec["description"] = extract_description(sections.get("DIVCAPLDescription"))
        rec["selectors"] = extract_selectors(sections.get("DIVCAPLSelectors"))
        rec["example"] = extract_example(sections.get("DIVCAPLExample"))
        rec["availability"] = extract_availability(sections.get("DIVCAPLAvailability"))
    elif page_type == "selector":
        rec["selectors"] = extract_selector_page(tree)
    else:
        nc = extract_notes_concept(tree)
        rec["description"] = nc["paragraphs"]
        rec["tables"] = nc["tables"]
    return rec


def extract_name_from_filename(filename):
    """Extract a normalized function name from a CAPLfunctionXXX.htm filename."""
    base = filename.replace(".htm", "").replace(".html", "")
    m = re.match(r"CAPLfunctions?(\w+)", base)
    if m:
        n = m.group(1)
        if len(n) >= 2 and n[0].isupper() and n[1].islower():
            n = n[0].lower() + n[1:]
        return n
    m = re.match(r"CAPLSelector(\w+)", base)
    if m:
        return m.group(1)
    return base


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python 01_vector_parser.py <htm_file> [category]")
        sys.exit(1)
    fp = sys.argv[1]
    cat = sys.argv[2] if len(sys.argv) > 2 else ""
    rec = parse_page(fp, cat)
    print(json.dumps(rec, indent=2, ensure_ascii=False))
