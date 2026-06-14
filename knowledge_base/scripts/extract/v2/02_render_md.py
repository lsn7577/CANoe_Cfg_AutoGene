"""Render a structured Vector page dict to clean Markdown.

Supports:
  - function/method/event/selector/notes pages (Vector CAPL template)
  - concept pages (Panel, DBC - h1 title + h2/h3 sections)
"""
import os, re, json


def _table_from_rows(rows):
    if not rows:
        return ""
    max_cols = max(len(r) for r in rows)
    out = []
    for i, row in enumerate(rows):
        cells = list(row) + [""] * (max_cols - len(row))
        cells = [str(c).replace("|", chr(92) + "|").replace(chr(10), " ") for c in cells]
        out.append("| " + " | ".join(cells) + " |")
        if i == 0 and max_cols > 0:
            out.append("|" + "|".join(["---"] * max_cols) + "|")
    return chr(10).join(out)
def _code_block(code, lang="c"):
    if not code:
        return ""
    return "```" + lang + chr(10) + code.rstrip() + chr(10) + "```"


def _is_footer_or_banner_table(tbl):
    if not tbl:
        return False
    joined = " | ".join([" ".join(r) for r in tbl])
    if "Vector Informatik" in joined and "Version" in joined:
        return True
    if len(tbl) == 1 and len(tbl[0]) == 1 and len(tbl[0][0]) < 80:
        if any(s in tbl[0][0] for s in ("Copyright", "Vector Informatik", "Version ")):
            return True
    return False


def _render_sections(sections, base_level=2):
    lines = []
    for sec in sections:
        heading = sec.get("heading", "")
        if not heading:
            continue
        lvl = sec.get("level", 2)
        h_level = min(base_level + max(0, lvl - 2), 6)
        lines.append("#" * h_level + " " + heading)
        lines.append("")
        content = sec.get("content", {})
        for p in content.get("paragraphs", []):
            lines.append(p)
            lines.append("")
        for tbl in content.get("tables", []):
            if not tbl or _is_footer_or_banner_table(tbl):
                continue
            lines.append(_table_from_rows(tbl))
            lines.append("")
        for code in content.get("code_blocks", []):
            lines.append(_code_block(code, "c"))
            lines.append("")
    return chr(10).join([l for l in lines if l is not None])


def render_page_md(rec):
    lines = []
    title = rec.get("name") or rec.get("title") or "Untitled"
    pt = rec.get("page_type", "notes")
    category = rec.get("category", "")
    subcategory = rec.get("subcategory", "")
    lines.append("# " + title)
    lines.append("")
    if category or subcategory:
        bits = []
        if category:
            bits.append("Category: `" + category + "`")
        if subcategory:
            bits.append("Subcategory: `" + subcategory + "`")
        bits.append("Type: `" + pt + "`")
        lines.append("> " + " | ".join(bits))
        lines.append("")
    if pt == "concept":
        intro = rec.get("intro") or []
        intro_tables = rec.get("intro_tables") or []
        intro_code = rec.get("intro_code_blocks") or []
        for p in intro:
            lines.append(p)
            lines.append("")
        for tbl in intro_tables:
            if not tbl or _is_footer_or_banner_table(tbl):
                continue
            lines.append(_table_from_rows(tbl))
            lines.append("")
        for code in intro_code:
            lines.append(_code_block(code, "c"))
            lines.append("")
        sections = rec.get("sections") or []
        sec_md = _render_sections(sections, base_level=2)
        if sec_md:
            lines.append(sec_md)
        return chr(10).join(lines).rstrip() + chr(10)
    syntax = rec.get("syntax") or []
    if syntax:
        lines.append("## Syntax")
        lines.append("")
        lines.append(_code_block(chr(10).join(syntax), "c"))
        lines.append("")
    desc = rec.get("description") or []
    if desc:
        lines.append("## Description")
        lines.append("")
        for p in desc:
            lines.append(p)
            lines.append("")
    params = rec.get("parameters") or []
    if params:
        lines.append("## Parameters")
        lines.append("")
        has_type = any(p.get("type") for p in params)
        if has_type:
            rows = [["Name", "Type", "Description"]]
        else:
            rows = [["Name", "Description"]]
        for p in params:
            if not has_type:
                rows.append([p.get("name", ""), p.get("description", "")])
            else:
                rows.append([p.get("name", ""), p.get("type", ""), p.get("description", "")])
        lines.append(_table_from_rows(rows))
        lines.append("")
    rv = rec.get("return") or ""
    if rv:
        lines.append("## Return Values")
        lines.append("")
        lines.append(rv)
        lines.append("")
    cx = rec.get("complexity") or ""
    if cx:
        lines.append("## Complexity")
        lines.append("")
        lines.append(cx)
        lines.append("")
    ex = rec.get("example") or {}
    ex_desc = ex.get("description") or []
    ex_code = ex.get("code") or ""
    if ex_desc or ex_code:
        lines.append("## Example")
        lines.append("")
        for d in ex_desc:
            lines.append(d)
            lines.append("")
        if ex_code:
            lines.append(_code_block(ex_code, "c"))
            lines.append("")
    avail = rec.get("availability") or []
    if avail:
        lines.append("## Availability")
        lines.append("")
        if all(isinstance(r, list) for r in avail):
            lines.append(_table_from_rows(avail))
        else:
            for r in avail:
                lines.append("- " + str(r))
        lines.append("")
    sels = rec.get("selectors") or []
    if sels and pt != "selector":
        lines.append("## Selectors")
        lines.append("")
        if isinstance(sels, list) and sels and isinstance(sels[0], dict):
            link_rows = []
            for s in sels:
                if "row" in s:
                    link_rows.append(s["row"])
                elif "name" in s:
                    link_rows.append([s.get("name", ""), s.get("link", "")])
            if link_rows:
                lines.append(_table_from_rows(link_rows))
                lines.append("")
        else:
            for s in sels:
                lines.append("- " + str(s))
                lines.append("")
    notes = rec.get("note") or []
    if notes:
        lines.append("## Notes")
        lines.append("")
        for n in notes:
            lines.append("> " + n)
            lines.append("")
    if pt == "selector" and sels and isinstance(sels[0], dict):
        for s in sels:
            if s.get("name"):
                lines.append("### " + s["name"])
                lines.append("")
                for d in s.get("description", []):
                    lines.append(d)
                    lines.append("")
                if s.get("code"):
                    lines.append(_code_block(s["code"], "c"))
                    lines.append("")
    if pt in ("notes", "concept"):
        tables = rec.get("tables") or []
        for tbl in tables:
            if not tbl or _is_footer_or_banner_table(tbl):
                continue
            lines.append(_table_from_rows(tbl))
            lines.append("")
    return chr(10).join(lines).rstrip() + chr(10)


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python 02_render_md.py <structured.json> [out.md]")
        sys.exit(1)
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        rec = json.load(f)
    md = render_page_md(rec)
    if len(sys.argv) > 2:
        with open(sys.argv[2], "w", encoding="utf-8") as f:
            f.write(md)
        print("Wrote", sys.argv[2])
    else:
        print(md)
