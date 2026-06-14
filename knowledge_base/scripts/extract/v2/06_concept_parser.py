"""Generic concept-page parser for Vector help docs (Panel, DBC, etc.) - v2.

Walk in document order, partition body content at h2/h3 headings.
"""
import os, re, json
from lxml import html as lxml_html


def _clean(s):
    if s is None:
        return ""
    s = s.replace(chr(9), " ").replace(chr(13), " ")
    s = s.replace(chr(0xa0), " ").replace(chr(0x200b), "")
    s = re.sub(r"\s+", " ", s).strip()
    return s


def _text_with_br(elem):
    if elem is None:
        return ""
    parts = []
    def walk(e):
        if e.tag == "br":
            parts.append(chr(10))
            return
        if e.text:
            parts.append(e.text)
        for child in e:
            walk(child)
            if child.tail:
                parts.append(child.tail)
    walk(elem)
    s = "".join(parts)
    s = s.replace(chr(0xa0), " ").replace(chr(0x200b), "")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r" *\n *", "\n", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


def _load(filepath):
    with open(filepath, "rb") as f:
        raw = f.read()
    raw = re.sub(rb"<\?xml[^?]+\?>", b"", raw)
    try:
        html_str = raw.decode("windows-1252", errors="ignore")
    except Exception:
        html_str = raw.decode("utf-8", errors="ignore")
    return lxml_html.fromstring(html_str)


def _get_title(tree):
    sys_titles = tree.xpath(".//span[@class=\"SystemTitle\"]")
    if sys_titles:
        return _clean("".join(sys_titles[0].itertext()))
    h1 = tree.xpath(".//body//h1")
    if h1:
        return _clean("".join(h1[0].itertext()))
    title_nodes = tree.xpath("//title/text()")
    if title_nodes:
        return _clean(title_nodes[0])
    return ""


def _is_masterpage_div(elem):
    if elem is None or elem.tag != "div":
        return False
    cls = elem.get("class", "")
    if any(s in cls for s in ("MasterPage", "Toolbar", "Footer", "Header")):
        return True
    return False


def _walk_body_elements(body):
    skip_root_ids = set()
    for el in body.iter():
        if el is body:
            continue
        if _is_masterpage_div(el):
            skip_root_ids.add(id(el))
    for el in body.iter():
        if el is body:
            continue
        skip = False
        parent = el.getparent()
        while parent is not None:
            if id(parent) in skip_root_ids:
                skip = True
                break
            parent = parent.getparent()
        if skip:
            continue
        yield el


def _is_heading(elem):
    return elem is not None and elem.tag in ("h1", "h2", "h3", "h4")


def _table_to_rows(tbl):
    rows = []
    for tr in tbl.xpath(".//tr"):
        cells = tr.xpath(".//th|.//td")
        cell_texts = [_clean(c.text_content()) for c in cells]
        cell_texts = [c for c in cell_texts if c]
        if cell_texts:
            rows.append(cell_texts)
    return rows


def _collect_block(elements, start_idx, end_idx):
    paragraphs = []
    tables = []
    code_blocks = []
    seen_text = set()
    for el in elements[start_idx:end_idx]:
        if _is_heading(el):
            continue
        if el.tag == "p":
            cls = el.get("class", "")
            if any(s in cls for s in ("TableSourceCode", "TableSyntax")) or "code" in cls.lower():
                code = _text_with_br(el)
                if code:
                    code_blocks.append(code)
                continue
            if any(s in cls for s in ("StructurePath", "MenuPath", "Footer", "TableHead", "TableHeader", "TopicBodyHeader")):
                continue
            text = _clean(el.text_content())
            if not text or text in seen_text:
                continue
            seen_text.add(text)
            paragraphs.append(text)
        elif el.tag == "table":
            rows = _table_to_rows(el)
            if rows:
                tables.append(rows)
        elif el.tag == "pre":
            code = _text_with_br(el)
            if code:
                code_blocks.append(code)
    return {"paragraphs": paragraphs, "tables": tables, "code_blocks": code_blocks}


def parse_concept_page(filepath, category="", subcategory=""):
    try:
        tree = _load(filepath)
    except Exception as e:
        return {"error": "parse_failed: " + str(e), "source": str(filepath)}
    title = _get_title(tree)
    rec = {
        "page_type": "concept",
        "name": title,
        "category": category,
        "subcategory": subcategory,
        "title": title,
        "source": str(filepath),
        "intro": [],
        "intro_tables": [],
        "intro_code_blocks": [],
        "sections": [],
    }
    body = tree.xpath(".//body")
    if not body:
        return rec
    body = body[0]
    elements = list(_walk_body_elements(body))
    heading_positions = []
    for i, el in enumerate(elements):
        if _is_heading(el):
            heading_positions.append((i, el))
    if not heading_positions:
        block = _collect_block(elements, 0, len(elements))
        rec["intro"] = block["paragraphs"]
        rec["intro_tables"] = block["tables"]
        rec["intro_code_blocks"] = block["code_blocks"]
        return rec
    first_heading_idx = heading_positions[0][0]
    first_section_start = None
    for pos, el in heading_positions:
        if el.tag in ("h2", "h3", "h4"):
            first_section_start = pos
            break
    if first_section_start is not None:
        # Intro: from after h1 to first h2/h3
        block = _collect_block(elements, first_heading_idx + 1, first_section_start)
        rec["intro"] = block["paragraphs"]
        rec["intro_tables"] = block["tables"]
        rec["intro_code_blocks"] = block["code_blocks"]
    else:
        # No h2/h3: everything after h1 is the intro
        block = _collect_block(elements, first_heading_idx + 1, len(elements))
        rec["intro"] = block["paragraphs"]
        rec["intro_tables"] = block["tables"]
        rec["intro_code_blocks"] = block["code_blocks"]
    if first_section_start is not None:
        section_headings = [p for p in heading_positions if p[1].tag in ("h2", "h3", "h4") and p[0] >= first_section_start]
        for i, (pos, h) in enumerate(section_headings):
            heading_text = _clean(h.text_content())
            if not heading_text:
                continue
            end_pos = section_headings[i+1][0] if i+1 < len(section_headings) else len(elements)
            block = _collect_block(elements, pos + 1, end_pos)
            rec["sections"].append({
                "heading": heading_text,
                "level": int(h.tag[1]),
                "content": block,
            })
    return rec


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python concept_parser.py <htm_file> [category] [subcategory]")
        sys.exit(1)
    fp = sys.argv[1]
    cat = sys.argv[2] if len(sys.argv) > 2 else ""
    sub = sys.argv[3] if len(sys.argv) > 3 else ""
    rec = parse_concept_page(fp, cat, sub)
    print(json.dumps(rec, indent=2, ensure_ascii=False)[:5000])
