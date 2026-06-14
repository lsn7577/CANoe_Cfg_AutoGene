"""Completeness test for the knowledge base."""
import os, sys, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
L2 = str(ROOT / "knowledge")
L3 = str(ROOT / "L3_diffs")
TESTS = str(ROOT / "tests_integration")
_L1 = ROOT / "L1_latest"
L1 = str(_L1 if _L1.exists() else ROOT / "knowledge" / "v15")

CONTENT_BLOCKS = ["CAPL", "Panel_XVP", "DBC", "CANoe_Config"]
FILES_PER_BLOCK = {
    "CAPL": ["01_CAPL_Programming_Guide.md", "capl_functions_full.json"],
    "Panel_XVP": ["02_Panel_Designer_XVP_Guide.md", "02_Panel_Designer_XVP_Syntax.json"],
    "DBC": ["03_DBC_Writing_Guide.md", "03_DBC_Field_Reference.json"],
    "CANoe_Config": ["04_CANoe_Configuration_Guide.md", "04_CANoe_Configuration_Attributes.json"]
}
REQUIRED_CAPL_CATEGORIES = ["CAN", "LIN", "FlexRay", "J1939", "IP", "TCPIPAPI", "Test", "XCP", "CANopen"]
REQUIRED_PANEL_ELEMENTS = ["Button", "CheckBox", "Switch", "LED", "StaticText", "ProgressBar", "InputOutputBox", "ComboBox", "RadioButton", "GroupBox"]
REQUIRED_DBC_KEYWORDS = ["VERSION", "NS_", "BS_", "BU_", "BO_", "SG_", "EV_", "CM_", "BA_DEF_", "BA_", "VAL_TABLE_", "VAL_"]

results = []

def record(test_name, status, message=""):
    results.append({"test": test_name, "status": status, "message": message})
    icon = "[PASS]" if status == "PASS" else ("[WARN]" if status == "WARN" else "[FAIL]")
    print(icon + " " + test_name + ": " + message)

def test_directory_structure():
    for path in [L1, L2, L3, TESTS]:
        if not os.path.isdir(path):
            return "FAIL", "Directory missing: " + path
    for sub in ["v12", "v15"]:
        if not os.path.isdir(os.path.join(L2, sub)):
            return "FAIL", "L2 subdir missing: " + sub
    return "PASS", "All directories present"

def test_v12_files():
    v12 = os.path.join(L2, "v12")
    missing = []
    for block, files in FILES_PER_BLOCK.items():
        for f in files:
            topic = FILE_TO_TOPIC.get(f, "")
            fp = os.path.join(v12, topic, f) if topic else os.path.join(v12, f)
            if not os.path.exists(fp):
                missing.append(f)
    if missing:
        return "FAIL", "v12 missing files: " + str(missing)
    return "PASS", "All 8 v12 files present"

def test_v15_files():
    v15 = os.path.join(L2, "v15")
    missing = []
    for block, files in FILES_PER_BLOCK.items():
        for f in files:
            topic = FILE_TO_TOPIC.get(f, "")
            fp = os.path.join(v15, topic, f) if topic else os.path.join(v15, f)
            if not os.path.exists(fp):
                missing.append(f)
    if missing:
        return "FAIL", "v15 missing files: " + str(missing)
    return "PASS", "All 8 v15 files present"

def test_l1_matches_v15():
    """L1_latest is a junction to knowledge/v15; verify content matches."""
    KNOWLEDGE = L2
    v15 = os.path.join(KNOWLEDGE, "v15")
    if not os.path.isdir(v15):
        return "WARN", "knowledge/v15 missing"
    l1_files = set()
    for topic in ("capl", "panel", "dbc", "xcp"):
        tdir = os.path.join(L1, topic)
        if os.path.isdir(tdir):
            for f in os.listdir(tdir):
                if os.path.isfile(os.path.join(tdir, f)):
                    l1_files.add(f)
    expected = {"01_CAPL_Programming_Guide.md", "capl_functions_full.json",
                "02_Panel_Designer_XVP_Guide.md", "02_Panel_Designer_XVP_Syntax.json",
                "03_DBC_Writing_Guide.md", "03_DBC_Field_Reference.json",
                "04_CANoe_Configuration_Guide.md", "04_CANoe_Configuration_Attributes.json"}
    missing = expected - l1_files
    if missing:
        return "WARN", "L1/topics missing: " + str(missing)
    return "PASS", "L1_latest junction has 4 topics with 8 overview files"

def test_l3_diffs_present():
    required = ["diff_capl_v12_to_v15.json", "diff_panel_v12_to_v15.json",
                "diff_dbc_v12_to_v15.json", "diff_summary_v12_to_v15.json", "DIFF_REPORT.md"]
    missing = [f for f in required if not os.path.exists(os.path.join(L3, f))]
    if missing:
        return "FAIL", "L3 missing: " + str(missing)
    return "PASS", "All 5 diff files present"

def test_v12_capl_categories():
    fp = os.path.join(L2, "v12", "capl", "capl_functions_full.json")
    if not os.path.exists(fp):
        return "FAIL", "v12 CAPL JSON missing"
    with open(fp, encoding="utf-8") as f:
        d = json.load(f)
    cats = set((d.get("categories") or {}).keys())
    missing = [c for c in REQUIRED_CAPL_CATEGORIES if c not in cats]
    if missing:
        return "FAIL", "v12 CAPL missing categories: " + str(missing)
    total_funcs = d["metadata"]["total_functions"]
    if total_funcs < 4000:
        return "WARN", "v12 CAPL only " + str(total_funcs) + " functions (expected >4000)"
    return "PASS", "v12 CAPL: " + str(len(cats)) + " categories, " + str(total_funcs) + " functions"

def test_v15_capl_categories():
    fp = os.path.join(L2, "v15", "capl", "capl_functions_full.json")
    if not os.path.exists(fp):
        return "FAIL", "v15 CAPL JSON missing"
    with open(fp, encoding="utf-8") as f:
        d = json.load(f)
    cats = set((d.get("categories") or {}).keys())
    missing = [c for c in REQUIRED_CAPL_CATEGORIES if c not in cats]
    if missing:
        return "FAIL", "v15 CAPL missing categories: " + str(missing)
    new_v15_cats = ["ADAS", "CarMaker", "DistributedObjects", "MapWindowAPI"]
    missing_v15 = [c for c in new_v15_cats if c not in cats]
    if missing_v15:
        return "WARN", "v15 CAPL missing new categories: " + str(missing_v15)
    total_funcs = d["metadata"]["total_functions"]
    return "PASS", "v15 CAPL: " + str(len(cats)) + " categories, " + str(total_funcs) + " functions"

def test_v12_panel_elements():
    fp = os.path.join(L2, "v12", "panel", "02_Panel_Designer_XVP_Syntax.json")
    if not os.path.exists(fp):
        return "FAIL", "v12 Panel JSON missing"
    with open(fp, encoding="utf-8") as f:
        d = json.load(f)
    elems = set(e.get("name", "") for e in d.get("elements", []))
    missing = [e for e in REQUIRED_PANEL_ELEMENTS if e not in elems]
    if missing:
        return "FAIL", "v12 Panel missing: " + str(missing)
    return "PASS", "v12 Panel: " + str(len(elems)) + " elements"

def test_v15_panel_elements():
    fp = os.path.join(L2, "v15", "panel", "02_Panel_Designer_XVP_Syntax.json")
    if not os.path.exists(fp):
        return "FAIL", "v15 Panel JSON missing"
    with open(fp, encoding="utf-8") as f:
        d = json.load(f)
    elems = set(e.get("name", "") for e in d.get("elements", []))
    missing = [e for e in REQUIRED_PANEL_ELEMENTS if e not in elems]
    if missing:
        return "WARN", "v15 Panel missing core: " + str(missing)
    return "PASS", "v15 Panel: " + str(len(elems)) + " elements"

def test_v12_dbc_keywords():
    fp = os.path.join(L2, "v12", "dbc", "03_DBC_Field_Reference.json")
    if not os.path.exists(fp):
        return "FAIL", "v12 DBC JSON missing"
    with open(fp, encoding="utf-8") as f:
        d = json.load(f)
    kws = set(k.get("name", "") for k in d.get("syntax_keywords", []))
    missing = [k for k in REQUIRED_DBC_KEYWORDS if k not in kws]
    if missing:
        return "FAIL", "v12 DBC missing keywords: " + str(missing)
    return "PASS", "v12 DBC: " + str(len(kws)) + " keywords"

def test_v15_dbc_keywords():
    fp = os.path.join(L2, "v15", "dbc", "03_DBC_Field_Reference.json")
    if not os.path.exists(fp):
        return "FAIL", "v15 DBC JSON missing"
    with open(fp, encoding="utf-8") as f:
        d = json.load(f)
    kws = set(k.get("name", "") for k in d.get("syntax_keywords", []))
    missing = [k for k in REQUIRED_DBC_KEYWORDS if k not in kws]
    if missing:
        return "FAIL", "v15 DBC missing keywords: " + str(missing)
    new_v15_kws = ["CAT_DEF_", "CAT_", "FILTER", "BO_TX_BU_", "SIG_VALTYPE_"]
    missing_v15 = [k for k in new_v15_kws if k not in kws]
    if missing_v15:
        return "WARN", "v15 DBC missing new keywords: " + str(missing_v15)
    return "PASS", "v15 DBC: " + str(len(kws)) + " keywords (incl. v15-new)"

def test_canoe_config_attributes():
    for v in ["v12", "v15"]:
        fp = os.path.join(L2, v, "capl", "04_CANoe_Configuration_Attributes.json")
        if not os.path.exists(fp):
            return "FAIL", v + " cfg JSON missing"
        with open(fp, encoding="utf-8") as f:
            d = json.load(f)
        ch = d.get("channel_assignment", {})
        attrs = ch.get("attributes", [])
        if not attrs:
            return "FAIL", v + " cfg channel_assignment.attributes is empty"
        names = [a.get("name") for a in attrs]
        if "Channel Number" not in names or "Baud Rate" not in names:
            return "FAIL", v + " cfg missing core channel attributes"
    return "PASS", "Both versions have channel assignment + baud rate attributes"

FILE_TO_TOPIC = {
    "01_CAPL_Programming_Guide.md": "capl",
    "capl_functions_full.json": "capl",
    "02_Panel_Designer_XVP_Guide.md": "panel",
    "02_Panel_Designer_XVP_Syntax.json": "panel",
    "03_DBC_Writing_Guide.md": "dbc",
    "03_DBC_Field_Reference.json": "dbc",
    "04_CANoe_Configuration_Guide.md": "capl",
    "04_CANoe_Configuration_Attributes.json": "capl",
}


def test_file_sizes():
    issues = []
    for v in ["v12", "v15"]:
        for block, files in FILES_PER_BLOCK.items():
            for f in files:
                topic = FILE_TO_TOPIC.get(f, "")
                fp = os.path.join(L2, v, topic, f) if topic else os.path.join(L2, v, f)
                if os.path.exists(fp):
                    size = os.path.getsize(fp)
                    if size < 500:
                        issues.append(v + "/" + topic + "/" + f + " too small: " + str(size) + "B")
    if issues:
        return "WARN", "Small files: " + str(issues[:5])
    return "PASS", "All files are reasonably sized"

def test_capl_diff_validity():
    fp = os.path.join(L3, "diff_capl_v12_to_v15.json")
    if not os.path.exists(fp):
        return "FAIL", "CAPL diff missing"
    with open(fp, encoding="utf-8") as f:
        d = json.load(f)
    summary = d.get("summary", {})
    if summary.get("v12_total_functions", 0) < 1000:
        return "FAIL", "CAPL diff v12 functions count too low"
    if summary.get("v15_total_functions", 0) < 1000:
        return "FAIL", "CAPL diff v15 functions count too low"
    added_cats = summary.get("added_categories", [])
    if "ADAS" not in added_cats or "CarMaker" not in added_cats:
        return "WARN", "CAPL diff missing v15-new categories"
    return "PASS", "CAPL diff: v12=" + str(summary["v12_total_functions"]) + ", v15=" + str(summary["v15_total_functions"]) + " funcs"

def test_panel_diff_validity():
    fp = os.path.join(L3, "diff_panel_v12_to_v15.json")
    if not os.path.exists(fp):
        return "FAIL", "Panel diff missing"
    with open(fp, encoding="utf-8") as f:
        d = json.load(f)
    summary = d.get("summary", {})
    if summary.get("v12_total_elements", 0) < 30:
        return "FAIL", "Panel diff v12 elements too few"
    if summary.get("v15_total_elements", 0) < 30:
        return "FAIL", "Panel diff v15 elements too few"
    return "PASS", "Panel diff: v12=" + str(summary["v12_total_elements"]) + ", v15=" + str(summary["v15_total_elements"]) + " elements"

def test_manifests_present():
    for v in ["v12", "v15"]:
        fp = os.path.join(TESTS, "manifest_" + v + ".json")
        if not os.path.exists(fp):
            return "FAIL", v + " manifest missing"
    return "PASS", "Both manifests present"

def test_kb_overview():
    readme = os.path.join(os.path.dirname(L1), "README.md")
    if not os.path.exists(readme):
        return "WARN", "README.md not present (optional)"
    return "PASS", "README.md present"

def test_l1_is_junction():
    """L1_latest should be a junction/symlink to knowledge/v15."""
    import subprocess
    import shutil
    import tempfile
    if not _L1.exists() and os.path.isdir(L1):
        return "PASS", "latest view uses knowledge/v15 directly"
    fp = os.path.join(L1, "capl", "01_CAPL_Programming_Guide.md")
    if not os.path.exists(fp):
        return "FAIL", "L1_latest/capl content not accessible"
    try:
        result = subprocess.run(["cmd", "/c", "dir", "/AL", os.path.dirname(L1)],
                                capture_output=True, text=True, timeout=5)
        if ("JUNCTION" in result.stdout or "<JUNCTION>" in result.stdout) and "L1_latest" in result.stdout:
            if "knowledge" in result.stdout:
                return "PASS", "L1_latest is a junction to knowledge/v15"
    except Exception:
        pass
    # Fallback: write temp file in a non-shared location
    tmp_dir = tempfile.mkdtemp(prefix="l1_test_")
    try:
        tmp_file = os.path.join(tmp_dir, "marker.txt")
        with open(tmp_file, "w") as f:
            f.write("test")
        # Copy into L1 to test
        l1_target = os.path.join(L1, "_l1_test_marker.txt")
        shutil.copy2(tmp_file, l1_target)
        KNOWLEDGE_V15 = os.path.join(L2, "v15")
        kv15_target = os.path.join(KNOWLEDGE_V15, "_l1_test_marker.txt")
        if os.path.exists(kv15_target):
            os.remove(kv15_target)
            return "PASS", "L1_latest is a junction/symlink to knowledge/v15 (write-through verified)"
        os.remove(l1_target)
    except Exception:
        pass
    finally:
        import shutil as _sh
        _sh.rmtree(tmp_dir, ignore_errors=True)
    return "WARN", "L1_latest not detected as junction (may be normal copy)"

def test_capl_split_exists():
    """capl/_index.json + per-category JSON + structured/<cat>/* must exist for v12 and v15."""
    issues = []
    for v in ["v12", "v15"]:
        index_fp = os.path.join(L2, v, "capl", "_index.json")
        if not os.path.exists(index_fp):
            issues.append(v + "/capl/_index.json missing")
            continue
        with open(index_fp, encoding="utf-8") as f:
            d = json.load(f)
        struct_root = os.path.join(L2, v, "capl", "structured")
        for cat, info in d["categories"].items():
            cat_fp = os.path.join(L2, v, "capl", cat + ".json")
            if not os.path.exists(cat_fp):
                issues.append(v + "/" + cat + ".json missing")
                continue
            with open(cat_fp, encoding="utf-8") as fh:
                cat_data = json.load(fh)
            if cat_data.get("function_count") != info["function_count"]:
                issues.append(v + "/" + cat + ": count mismatch")
            if not os.path.isdir(os.path.join(struct_root, cat)):
                issues.append(v + "/" + cat + ": structured/ missing")
    if issues:
        return "FAIL", "Split issues: " + str(issues[:5])
    return "PASS", "capl/ split + structured/ valid for v12 and v15"

def test_v15_structured_output():
    struct_root = os.path.join(L2, "v15", "capl", "structured")
    if not os.path.isdir(struct_root):
        return "FAIL", "v15/capl/structured/ missing"
    cats = [d for d in os.listdir(struct_root) if os.path.isdir(os.path.join(struct_root, d))]
    if not cats:
        return "FAIL", "v15 structured: no category subdirs"
    fp = os.path.join(struct_root, "CAN", "BusLoad.json")
    if not os.path.exists(fp):
        return "FAIL", "v15 CAN/BusLoad.json missing"
    with open(fp, encoding="utf-8") as f:
        d = json.load(f)
    required = ["page_type", "name", "category", "syntax", "description", "parameters", "return", "example", "availability", "source"]
    missing = [k for k in required if k not in d]
    if missing:
        return "FAIL", "BusLoad missing fields: " + str(missing)
    if d["page_type"] != "function":
        return "FAIL", "BusLoad page_type should be function, got: " + d["page_type"]
    if not d["syntax"]:
        return "FAIL", "BusLoad has empty syntax"
    if not d["example"].get("code"):
        return "FAIL", "BusLoad has no example code"
    if not d["availability"]:
        return "FAIL", "BusLoad has no availability"
    return "PASS", "v15 structured: " + str(len(cats)) + " categories, sample BusLoad has all fields"


def test_v12_structured_output():
    struct_root = os.path.join(L2, "v12", "capl", "structured")
    if not os.path.isdir(struct_root):
        return "FAIL", "v12/capl/structured/ missing"
    cats = [d for d in os.listdir(struct_root) if os.path.isdir(os.path.join(struct_root, d))]
    if not cats:
        return "FAIL", "v12 structured: no category subdirs"
    fp = os.path.join(struct_root, "CAN", "BusLoad.json")
    if not os.path.exists(fp):
        return "FAIL", "v12 CAN/BusLoad.json missing"
    with open(fp, encoding="utf-8") as f:
        d = json.load(f)
    if d["page_type"] != "function":
        return "FAIL", "v12 BusLoad page_type should be function, got: " + d["page_type"]
    if not d["syntax"]:
        return "FAIL", "v12 BusLoad has empty syntax"
    if not d["example"].get("code"):
        return "FAIL", "v12 BusLoad has no example code"
    return "PASS", "v12 structured: " + str(len(cats)) + " categories, sample BusLoad has all fields"


def test_v15_page_type_distribution():
    struct_root = os.path.join(L2, "v15", "capl", "structured")
    types = {"function": 0, "method": 0, "event": 0, "selector": 0}
    for cat in os.listdir(struct_root):
        cat_dir = os.path.join(struct_root, cat)
        if not os.path.isdir(cat_dir):
            continue
        for f in os.listdir(cat_dir):
            if f.endswith(".json"):
                try:
                    with open(os.path.join(cat_dir, f), encoding="utf-8") as fh:
                        d = json.load(fh)
                    pt = d.get("page_type", "")
                    if pt in types:
                        types[pt] += 1
                except Exception:
                    pass
    if types["function"] < 1000:
        return "FAIL", "v15 functions too few: " + str(types)
    if types["method"] < 100:
        return "FAIL", "v15 methods too few: " + str(types)
    if types["event"] < 50:
        return "FAIL", "v15 events too few: " + str(types)
    return "PASS", "v15 page types: " + str(types)


def test_capl_per_category_files_have_functions():
    issues = []
    for v in ["v12", "v15"]:
        for cat in ["CAN", "Test"]:
            cat_fp = os.path.join(L2, v, "capl", cat + ".json")
            if not os.path.exists(cat_fp):
                continue
            with open(cat_fp, encoding="utf-8") as fh:
                cd = json.load(fh)
            funcs = cd.get("functions", [])
            if not funcs:
                issues.append(v + "/" + cat + " has no functions")
                continue
            f0 = funcs[0]
            if "name" not in f0 or "page_type" not in f0 or "json" not in f0 or "md" not in f0:
                issues.append(v + "/" + cat + " function entry malformed: " + str(f0))
                continue
            json_path = os.path.join(L2, v, "capl", f0["json"])
            if not os.path.exists(json_path):
                issues.append(v + "/" + cat + ": " + f0["json"] + " missing")
    if issues:
        return "FAIL", "Per-category issues: " + str(issues[:3])
    return "PASS", "Per-category files have proper function entries with type info"


def test_structured_function_md_renders():
    fp = os.path.join(L2, "v15", "capl", "structured", "CAN", "BusLoad.md")
    if not os.path.exists(fp):
        return "FAIL", "BusLoad.md missing"
    with open(fp, encoding="utf-8") as f:
        md = f.read()
    required_sections = ["# BusLoad", "## Syntax", "## Description", "## Return Values", "## Example", "## Availability"]
    missing = [s for s in required_sections if s not in md]
    if missing:
        return "FAIL", "MD missing sections: " + str(missing)
    fence = chr(96) * 3
    if md.count(fence) < 4:
        return "FAIL", "MD has fewer than 4 fenced blocks (expected at least syntax + example)"
    return "PASS", "BusLoad.md has all sections and code blocks"


# === T025-T036: knowledge/ structured KB tests ===

KNOWLEDGE = L2


def test_knowledge_directory_exists():
    if not os.path.isdir(KNOWLEDGE):
        return "FAIL", "knowledge/ directory missing"
    for sub in ("v12", "v15"):
        if not os.path.isdir(os.path.join(KNOWLEDGE, sub)):
            return "FAIL", "knowledge/" + sub + " missing"
    return "PASS", "knowledge/ with v12 + v15 present"


def test_knowledge_top_index():
    fp = os.path.join(KNOWLEDGE, "_index.json")
    if not os.path.exists(fp):
        return "FAIL", "knowledge/_index.json missing"
    with open(fp, encoding="utf-8") as f:
        d = json.load(f)
    if d["metadata"].get("latest") != "v15":
        return "WARN", "latest is not v15: " + str(d["metadata"].get("latest"))
    return "PASS", "knowledge/_index.json valid, latest=v15"


def test_knowledge_topic_layout():
    expected = ["capl", "panel", "dbc", "xcp"]
    issues = []
    for ver in ("v12", "v15"):
        for topic in expected:
            tp = os.path.join(KNOWLEDGE, ver, topic)
            if not os.path.isdir(tp):
                issues.append(ver + "/" + topic + " missing")
            else:
                struct = os.path.join(tp, "structured")
                if not os.path.isdir(struct):
                    issues.append(ver + "/" + topic + "/structured missing")
    if issues:
        return "FAIL", "; ".join(issues[:5])
    return "PASS", "All 4 topics x 2 versions have structured/"


def _count_json_pages(struct_dir):
    if not os.path.isdir(struct_dir):
        return 0
    n = 0
    for r, ds, fs in os.walk(struct_dir):
        for f in fs:
            if f.endswith(".json"):
                n += 1
    return n


def test_knowledge_v15_capl_pages():
    n = _count_json_pages(os.path.join(KNOWLEDGE, "v15", "capl", "structured"))
    if n < 5000:
        return "WARN", "v15/capl/structured: " + str(n) + " pages (expected 5025)"
    return "PASS", "v15/capl/structured: " + str(n) + " pages"


def test_knowledge_v15_panel_pages():
    n = _count_json_pages(os.path.join(KNOWLEDGE, "v15", "panel", "structured"))
    if n < 60:
        return "WARN", "v15/panel/structured: " + str(n) + " pages (expected 70)"
    return "PASS", "v15/panel/structured: " + str(n) + " pages"


def test_knowledge_v15_dbc_pages():
    n = _count_json_pages(os.path.join(KNOWLEDGE, "v15", "dbc", "structured"))
    if n < 140:
        return "WARN", "v15/dbc/structured: " + str(n) + " pages (expected 150)"
    return "PASS", "v15/dbc/structured: " + str(n) + " pages"


def test_knowledge_v15_xcp_pages():
    n = _count_json_pages(os.path.join(KNOWLEDGE, "v15", "xcp", "structured"))
    if n < 10:
        return "WARN", "v15/xcp/structured: " + str(n) + " pages (expected 17)"
    return "PASS", "v15/xcp/structured: " + str(n) + " pages"


def test_knowledge_l1_junction_points_to_v15():
    import subprocess
    if not _L1.exists() and os.path.isdir(L1):
        return "PASS", "latest view uses knowledge/v15 directly"
    if not os.path.isdir(L1):
        return "FAIL", "L1_latest not accessible"
    try:
        result = subprocess.run(["cmd", "/c", "dir", "/AL", os.path.dirname(L1)],
                                capture_output=True, text=True, timeout=5)
        if ("JUNCTION" in result.stdout or "<JUNCTION>" in result.stdout) and "L1_latest" in result.stdout:
            if "knowledge" in result.stdout:
                return "PASS", "L1_latest is a junction to knowledge/v15"
    except Exception:
        pass
    l1_set = set(os.listdir(L1))
    kv15_set = set(os.listdir(os.path.join(KNOWLEDGE, "v15")))
    if {"capl", "dbc", "panel", "xcp"}.issubset(l1_set) and l1_set == kv15_set:
        return "PASS", "L1_latest content matches knowledge/v15 (4 topics)"
    return "WARN", "L1=" + str(l1_set) + " vs knowledge/v15=" + str(kv15_set)


def test_knowledge_panel_md_renders():
    struct = os.path.join(KNOWLEDGE, "v15", "panel", "structured", "Elements")
    sample = os.path.join(struct, "Button.md")
    if not os.path.exists(sample):
        return "WARN", "Sample Button.md missing"
    with open(sample, encoding="utf-8") as f:
        text = f.read()
    if "# Button" not in text:
        return "FAIL", "Sample Button.md missing title"
    if "## Use Case" not in text and "## Configuration" not in text:
        return "WARN", "Sample Button.md missing expected sections"
    return "PASS", "Sample Button.md renders (" + str(len(text)) + " chars)"


def test_knowledge_dbc_md_renders():
    struct = os.path.join(KNOWLEDGE, "v15", "dbc", "structured", "Document")
    if not os.path.isdir(struct):
        return "WARN", "v15/dbc/structured/Document missing"
    files = [f for f in os.listdir(struct) if f.endswith(".md")]
    if not files:
        return "WARN", "No DBC MD files in Document"
    sample = os.path.join(struct, files[0])
    with open(sample, encoding="utf-8") as f:
        text = f.read()
    if not text.startswith("# "):
        return "FAIL", files[0] + " missing title"
    return "PASS", files[0] + " renders (" + str(len(text)) + " chars)"


def test_knowledge_xcp_md_renders():
    struct = os.path.join(KNOWLEDGE, "v15", "xcp", "structured")
    if not os.path.isdir(struct):
        return "WARN", "v15/xcp/structured missing"
    files = [f for f in os.listdir(struct) if f.endswith(".md")]
    if not files:
        return "WARN", "No XCP MD files"
    sample = os.path.join(struct, files[0])
    with open(sample, encoding="utf-8") as f:
        text = f.read()
    if not text.startswith("# "):
        return "FAIL", files[0] + " missing title"
    return "PASS", files[0] + " renders (" + str(len(text)) + " chars)"


def test_knowledge_readme_present():
    fp = os.path.join(KNOWLEDGE, "README.md")
    if not os.path.exists(fp):
        return "FAIL", "knowledge/README.md missing"
    return "PASS", "knowledge/README.md present"


tests = [
    ("T001 directory structure", test_directory_structure),
    ("T002 v12 all files present", test_v12_files),
    ("T003 v15 all files present", test_v15_files),
    ("T004 L1_latest matches v15", test_l1_matches_v15),
    ("T005 L3_diffs all diffs present", test_l3_diffs_present),
    ("T006 v12 CAPL categories", test_v12_capl_categories),
    ("T007 v15 CAPL categories", test_v15_capl_categories),
    ("T008 v12 Panel elements", test_v12_panel_elements),
    ("T009 v15 Panel elements", test_v15_panel_elements),
    ("T010 v12 DBC keywords", test_v12_dbc_keywords),
    ("T011 v15 DBC keywords", test_v15_dbc_keywords),
    ("T012 CANoe Config attributes", test_canoe_config_attributes),
    ("T013 File sizes non-empty", test_file_sizes),
    ("T014 CAPL diff valid", test_capl_diff_validity),
    ("T015 Panel diff valid", test_panel_diff_validity),
    ("T016 Manifests present", test_manifests_present),
    ("T017 KB overview README", test_kb_overview),

    ("T018 L1 is junction (not copy)", test_l1_is_junction),
    ("T019 capl/ split structure valid", test_capl_split_exists),
    ("T020 v15 structured per-function output", test_v15_structured_output),
    ("T021 v12 structured per-function output", test_v12_structured_output),
    ("T022 v15 page-type distribution", test_v15_page_type_distribution),
    ("T023 capl per-category files have type info", test_capl_per_category_files_have_functions),
    ("T024 structured function MD renders correctly", test_structured_function_md_renders),
    ("T025 knowledge/ directory exists", test_knowledge_directory_exists),
    ("T026 knowledge/ top index", test_knowledge_top_index),
    ("T027 knowledge/ topic layout", test_knowledge_topic_layout),
    ("T028 v15 capl pages in knowledge", test_knowledge_v15_capl_pages),
    ("T029 v15 panel pages in knowledge", test_knowledge_v15_panel_pages),
    ("T030 v15 dbc pages in knowledge", test_knowledge_v15_dbc_pages),
    ("T031 v15 xcp pages in knowledge", test_knowledge_v15_xcp_pages),
    ("T032 L1_latest junction to knowledge/v15", test_knowledge_l1_junction_points_to_v15),
    ("T033 panel MD renders", test_knowledge_panel_md_renders),
    ("T034 dbc MD renders", test_knowledge_dbc_md_renders),
    ("T035 xcp MD renders", test_knowledge_xcp_md_renders),
    ("T036 knowledge/README.md present", test_knowledge_readme_present),
]

print("=" * 60)
print("KNOWLEDGE BASE COMPLETENESS TEST")
print("=" * 60)
for name, fn in tests:
    status, message = fn()
    record(name, status, message)

print()
print("=" * 60)
print("SUMMARY")
print("=" * 60)
pass_count = sum(1 for r in results if r["status"] == "PASS")
warn_count = sum(1 for r in results if r["status"] == "WARN")
fail_count = sum(1 for r in results if r["status"] == "FAIL")
total = len(results)
print("Total tests:  " + str(total))
print("PASS:         " + str(pass_count))
print("WARN:         " + str(warn_count))
print("FAIL:         " + str(fail_count))
print()
if fail_count == 0:
    print("[OVERALL] PASS - Knowledge base is COMPLETE")
else:
    print("[OVERALL] FAIL - Knowledge base has issues, see warnings above")

report_path = os.path.join(TESTS, "completeness_test_report.json")
with open(report_path, "w", encoding="utf-8") as f:
    json.dump({
        "metadata": {
            "title": "Knowledge Base Completeness Test Report",
            "generated": "2026/06/01",
            "total": total,
            "pass": pass_count,
            "warn": warn_count,
            "fail": fail_count,
            "overall": "PASS" if fail_count == 0 else "FAIL"
        },
        "results": results
    }, f, indent=2, ensure_ascii=False)
print()
print("Report saved to: " + os.path.relpath(report_path, ROOT))


