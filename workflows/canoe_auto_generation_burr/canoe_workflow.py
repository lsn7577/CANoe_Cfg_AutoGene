from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
import zipfile
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple
from xml.etree import ElementTree as ET

from burr.core import ApplicationBuilder, State, action, default, expr


ROOT = Path(__file__).resolve().parents[2]
WORKFLOW_DIR = Path(__file__).resolve().parent
DEFAULT_TEMPLATE = ROOT / "templates" / "canoe_test_case_template" / "CANoe自动化测试用例模板.xlsx"
DEFAULT_OUTPUT = ROOT / "generated_projects" / "canoe_auto_generation"
FIELD_MAPPING_PATH = ROOT / "templates" / "canoe_test_case_template" / "template_field_mapping.json"
WORKFLOW_FIELD_MAPPING_POINTER = WORKFLOW_DIR / "template_field_mapping.json"
WORKFLOW_KB_DIR = ROOT / "knowledge_base" / "workflow_kb"
DEFAULT_TRACKING_PROJECT = "canoe_auto_generation"

PROJECT_SHEET = "工程参数配置"
CASE_SHEET = "测试用例"


def _load_field_mapping() -> Dict[str, Any]:
    return json.loads(FIELD_MAPPING_PATH.read_text(encoding="utf-8"))


FIELD_MAPPING = _load_field_mapping()
OPERATION_TYPES = set(FIELD_MAPPING["operation_types"])
CONDITION_TYPES = set(FIELD_MAPPING["condition_types"])
RESULT_TYPES = set(FIELD_MAPPING["result_types"])
COMPARE_OPERATOR_MAP = FIELD_MAPPING["compare_operator_mapping"]


def _workflow_retrieval_profile(profile_id: str) -> Dict[str, Any]:
    path = WORKFLOW_KB_DIR / "retrieval_profiles" / f"{profile_id}.json"
    if path.exists():
        data = json.loads(path.read_text(encoding="utf-8"))
    else:
        data = {"id": profile_id}
    data.setdefault("id", profile_id)
    data["profile_path"] = str(path)
    return data


def _json_default(value: Any) -> str:
    return str(value)


def _as_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value).strip()


def _as_int(value: Any, default_value: int = 0) -> int:
    text = _as_text(value)
    if not text:
        return default_value
    try:
        return int(float(text))
    except ValueError:
        return default_value


def _normalize_bool_yes(value: Any) -> bool:
    return _as_text(value) in {"是", "启用", "true", "True", "1", "yes", "YES"}


def _ensure_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


def _write_json(path: Path, data: Any) -> str:
    _ensure_dir(path.parent)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, default=_json_default), encoding="utf-8")
    return str(path)


def _read_text_best_effort(path: Path) -> str:
    for encoding in ("utf-8-sig", "utf-8", "gb18030", "latin-1"):
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue
    return path.read_text(encoding="utf-8", errors="replace")


def _file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _make_run_id(excel: Path) -> str:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    try:
        digest = _file_sha256(excel)[:8]
    except OSError:
        digest = "noinput"
    return f"{timestamp}_{digest}"


def _state_output_root(state: State) -> Path:
    return Path(state.get("output_root") or DEFAULT_OUTPUT)


def _strategy_value(project_config: Dict[str, Any], key: str, default_value: str = "") -> str:
    return _as_text(project_config.get("strategy", {}).get(key)) or default_value


def _strict_source_validation(state: State, project_config: Dict[str, Any]) -> bool:
    if "strict_source_validation" in state:
        return bool(state.get("strict_source_validation"))
    return _normalize_bool_yes(_strategy_value(project_config, "启用源文件严格校验", "否"))


def _canoe_validation_mode(state: State, project_config: Dict[str, Any]) -> str:
    explicit = _as_text(state.get("canoe_validation_mode")).lower()
    if explicit in {"disabled", "manual", "automated"}:
        return explicit
    value = _strategy_value(project_config, "CANoe 实机编译校验", "否")
    if value == "是":
        return "automated"
    if value == "按需":
        return "manual"
    return "disabled"


def _safe_name(value: Any, default_value: str = "Item") -> str:
    text = _as_text(value) or default_value
    text = text.replace("::", "_").replace(".", "_")
    text = re.sub(r"[^A-Za-z0-9_]", "_", text)
    text = re.sub(r"_+", "_", text).strip("_")
    if not text:
        text = default_value
    if text[0].isdigit():
        text = f"_{text}"
    return text


def _column_index(cell_ref: str) -> int:
    letters = re.sub(r"[^A-Z]", "", cell_ref.upper())
    value = 0
    for ch in letters:
        value = value * 26 + (ord(ch) - ord("A") + 1)
    return value - 1


def _xml_ns(tag: str) -> str:
    return f"{{http://schemas.openxmlformats.org/spreadsheetml/2006/main}}{tag}"


def _rel_ns(tag: str) -> str:
    return f"{{http://schemas.openxmlformats.org/package/2006/relationships}}{tag}"


def _office_rel_ns(tag: str) -> str:
    return f"{{http://schemas.openxmlformats.org/officeDocument/2006/relationships}}{tag}"


def _read_shared_strings(zf: zipfile.ZipFile) -> List[str]:
    try:
        root = ET.fromstring(zf.read("xl/sharedStrings.xml"))
    except KeyError:
        return []
    strings: List[str] = []
    for si in root.findall(_xml_ns("si")):
        parts = []
        for t in si.iter(_xml_ns("t")):
            parts.append(t.text or "")
        strings.append("".join(parts))
    return strings


def _read_workbook_sheets(zf: zipfile.ZipFile) -> Dict[str, str]:
    workbook = ET.fromstring(zf.read("xl/workbook.xml"))
    rels = ET.fromstring(zf.read("xl/_rels/workbook.xml.rels"))
    rel_targets = {}
    for rel in rels.findall(_rel_ns("Relationship")):
        rel_id = rel.attrib.get("Id")
        target = rel.attrib.get("Target", "")
        if rel_id and target:
            normalized = target.lstrip("/")
            if not normalized.startswith("xl/"):
                normalized = "xl/" + normalized
            rel_targets[rel_id] = normalized
    out = {}
    sheets = workbook.find(_xml_ns("sheets"))
    if sheets is None:
        return out
    for sheet in sheets.findall(_xml_ns("sheet")):
        name = sheet.attrib.get("name", "")
        rid = sheet.attrib.get(_office_rel_ns("id"), "")
        if name and rid in rel_targets:
            out[name] = rel_targets[rid]
    return out


def _read_sheet_rows(zf: zipfile.ZipFile, sheet_path: str, shared_strings: List[str]) -> List[List[Any]]:
    root = ET.fromstring(zf.read(sheet_path))
    rows: List[List[Any]] = []
    sheet_data = root.find(_xml_ns("sheetData"))
    if sheet_data is None:
        return rows
    for row in sheet_data.findall(_xml_ns("row")):
        row_idx = int(row.attrib.get("r", len(rows) + 1)) - 1
        while len(rows) <= row_idx:
            rows.append([])
        values = rows[row_idx]
        for cell in row.findall(_xml_ns("c")):
            ref = cell.attrib.get("r", "")
            col_idx = _column_index(ref)
            while len(values) <= col_idx:
                values.append("")
            ctype = cell.attrib.get("t", "")
            value_node = cell.find(_xml_ns("v"))
            if ctype == "inlineStr":
                text_node = cell.find(f"{_xml_ns('is')}/{_xml_ns('t')}")
                value: Any = text_node.text if text_node is not None else ""
            elif value_node is None:
                value = ""
            elif ctype == "s":
                index = int(value_node.text or "0")
                value = shared_strings[index] if 0 <= index < len(shared_strings) else ""
            else:
                raw = value_node.text or ""
                try:
                    value = float(raw) if "." in raw else int(raw)
                except ValueError:
                    value = raw
            values[col_idx] = value
    max_len = max((len(row) for row in rows), default=0)
    return [row + [""] * (max_len - len(row)) for row in rows]


def read_xlsx_tables(path: Path) -> Dict[str, List[List[Any]]]:
    with zipfile.ZipFile(path) as zf:
        shared_strings = _read_shared_strings(zf)
        sheets = _read_workbook_sheets(zf)
        return {
            name: _read_sheet_rows(zf, sheet_path, shared_strings)
            for name, sheet_path in sheets.items()
        }


def _find_header_indexes(rows: List[List[Any]], required_headers: Iterable[str]) -> List[int]:
    required = {_as_text(h) for h in required_headers}
    indexes = []
    for idx, row in enumerate(rows):
        values = {_as_text(v) for v in row}
        if required.issubset(values):
            indexes.append(idx)
    return indexes


def _rows_to_dicts(
    rows: List[List[Any]],
    header_idx: int,
    expected_headers: Optional[List[str]] = None,
    max_rows: int = 200,
) -> List[Dict[str, Any]]:
    header = [_as_text(v) for v in rows[header_idx]]
    if expected_headers:
        header = expected_headers + header[len(expected_headers):]
    data: List[Dict[str, Any]] = []
    blank_streak = 0
    for row in rows[header_idx + 1: header_idx + 1 + max_rows]:
        values = list(row) + [""] * max(0, len(header) - len(row))
        item = {header[i]: values[i] for i in range(min(len(header), len(values))) if header[i]}
        meaningful = any(_as_text(v) for k, v in item.items() if k not in {"填写检查"})
        if not meaningful:
            blank_streak += 1
            if blank_streak >= 20:
                break
            data.append(item)
            continue
        blank_streak = 0
        data.append(item)
    return data


def parse_template(path: Path) -> Tuple[Dict[str, Any], List[Dict[str, Any]], Dict[str, Any]]:
    sheets = read_xlsx_tables(path)
    if PROJECT_SHEET not in sheets:
        raise ValueError(f"missing sheet: {PROJECT_SHEET}")
    if CASE_SHEET not in sheets:
        raise ValueError(f"missing sheet: {CASE_SHEET}")

    project_rows = sheets[PROJECT_SHEET]
    case_rows = sheets[CASE_SHEET]

    basic_indexes = _find_header_indexes(project_rows, ["配置项", "填写值", "是否必填", "填写说明"])
    strategy_indexes = _find_header_indexes(project_rows, ["策略项", "填写值", "是否必填", "填写说明"])
    if not basic_indexes or not strategy_indexes:
        raise ValueError("project sheet must contain basic config and strategy tables")
    basic_rows = _rows_to_dicts(project_rows, basic_indexes[0], max_rows=20)
    strategy_rows = _rows_to_dicts(project_rows, strategy_indexes[0], max_rows=20)

    channel_indexes = _find_header_indexes(project_rows, ["通道ID", "启用", "总线类型", "CANoe通道名"])
    if not channel_indexes:
        raise ValueError("project sheet must contain channel mount table")
    channel_rows = _rows_to_dicts(project_rows, channel_indexes[0], max_rows=80)

    case_indexes = _find_header_indexes(case_rows, ["用例ID", "步骤序号", "操作类型", "条件类型", "结果类型"])
    if not case_indexes:
        raise ValueError("test case sheet must contain test case step table")
    test_steps = _rows_to_dicts(case_rows, case_indexes[0], max_rows=500)
    test_steps = [
        row for row in test_steps
        if _as_text(row.get("用例ID")) or _as_text(row.get("操作类型")) or _as_text(row.get("步骤序号"))
    ]

    basic = {
        _as_text(row.get("配置项")): row.get("填写值")
        for row in basic_rows
        if _as_text(row.get("配置项"))
    }
    strategy = {
        _as_text(row.get("策略项")): row.get("填写值")
        for row in strategy_rows
        if _as_text(row.get("策略项"))
    }
    channels = [
        row for row in channel_rows
        if _as_text(row.get("通道ID")) or _as_text(row.get("CANoe通道名"))
    ]

    project_config = {
        "basic": basic,
        "channels": channels,
        "enabled_channels": [row for row in channels if _normalize_bool_yes(row.get("启用"))],
        "strategy": strategy,
    }
    raw = {
        "template_path": str(path),
        "sheets": list(sheets.keys()),
        "project_rows": len(project_rows),
        "test_case_rows": len(test_steps),
    }
    return project_config, test_steps, raw


def _source_files_from_state(state: State, project_config: Dict[str, Any]) -> Dict[str, List[str]]:
    basic = project_config.get("basic", {})
    channels = project_config.get("enabled_channels", [])
    def collect(key: str, state_key: str, channel_key: str) -> List[str]:
        values = []
        from_state = state.get(state_key, []) or []
        if isinstance(from_state, str):
            from_state = [from_state]
        values.extend([_as_text(v) for v in from_state if _as_text(v)])
        basic_value = _as_text(basic.get(key))
        if basic_value:
            values.append(basic_value)
        for ch in channels:
            value = _as_text(ch.get(channel_key))
            if value:
                values.append(value)
        return sorted(set(values))
    sources = {
        "requirements": collect("测试需求文件路径", "requirements_path", "测试需求文件路径"),
        "dbc": collect("默认 DBC 文件路径", "dbc_paths", "DBC路径"),
        "a2l": collect("默认 A2L 文件路径", "a2l_paths", "A2L路径"),
        "cdd": collect("默认 CDD 文件路径", "cdd_paths", "CDD路径"),
        "dll": collect("默认 DLL 文件路径", "dll_paths", "DLL路径"),
    }
    if not sources["dll"]:
        sources["dll"] = _discover_sibling_paths(sources, "*.dll")
    cfg_values = collect("默认 CFG 文件路径", "cfg_paths", "CFG路径")
    for key in ("基础 CANoe CFG 路径", "CANoe CFG 文件路径", "默认 CANoe CFG 文件路径"):
        value = _as_text(basic.get(key))
        if value:
            cfg_values.append(value)
    for ch in channels:
        for key in ("CANoe CFG路径", "CANoe CFG 路径", "CFG文件路径"):
            value = _as_text(ch.get(key))
            if value:
                cfg_values.append(value)
    if not cfg_values:
        cfg_values = _discover_cfg_paths(sources, _as_text(basic.get("项目代号")), _as_text(basic.get("工程名称")))
    sources["cfg"] = sorted(set(cfg_values))
    return sources


def _discover_sibling_paths(source_files: Dict[str, List[str]], pattern: str) -> List[str]:
    dirs = set()
    for kind in ("dbc", "a2l", "cdd"):
        for value in source_files.get(kind, []):
            path = Path(_as_text(value)).expanduser()
            if path.is_absolute() and path.exists():
                dirs.add(path.parent)
    return sorted({str(path) for directory in dirs for path in directory.glob(pattern)})


def _discover_cfg_paths(source_files: Dict[str, List[str]], project_code: str = "", project_name: str = "") -> List[str]:
    dirs = set()
    for kind in ("dbc", "a2l", "cdd"):
        for value in source_files.get(kind, []):
            path = Path(_as_text(value)).expanduser()
            if path.is_absolute() and path.exists():
                dirs.add(path.parent)
    candidates = sorted({cfg for directory in dirs for cfg in directory.glob("*.cfg")})
    if not candidates:
        return []
    preferred_stems = {
        _safe_name(value).lower()
        for value in (project_code, project_name)
        if _as_text(value)
    }
    preferred = [path for path in candidates if path.stem.lower() in preferred_stems]
    if len(preferred) == 1:
        return [str(preferred[0])]
    if len(candidates) == 1:
        return [str(candidates[0])]
    return []


def _resolve_declared_path(path_text: str, template_path: Path) -> Dict[str, Any]:
    raw = _as_text(path_text)
    if not raw:
        return {"declared": raw, "resolved": "", "exists": False, "candidates": []}
    path = Path(raw).expanduser()
    candidates = [path] if path.is_absolute() else [
        template_path.parent / path,
        ROOT / path,
        Path.cwd() / path,
    ]
    seen = []
    for candidate in candidates:
        resolved = candidate.resolve()
        if resolved not in seen:
            seen.append(resolved)
        if resolved.exists():
            return {
                "declared": raw,
                "resolved": str(resolved),
                "exists": True,
                "candidates": [str(item) for item in seen],
            }
    fallback = seen[0] if seen else path
    return {
        "declared": raw,
        "resolved": str(fallback),
        "exists": False,
        "candidates": [str(item) for item in seen],
    }


def _parse_dbc_file(path: Path) -> Dict[str, Any]:
    try:
        from . import source_parser
        result = source_parser.parse_dbc(path)
        if result.get("status") != "error":
            return result
    except Exception:
        pass
    text = _read_text_best_effort(path)
    messages: Dict[str, Dict[str, Any]] = {}
    current: Optional[Dict[str, Any]] = None
    for line in text.splitlines():
        msg_match = re.match(r"^\s*BO_\s+(\d+)\s+([A-Za-z_][A-Za-z0-9_]*)\s*:\s+(\d+)\s+(\S+)", line)
        if msg_match:
            frame_id, name, dlc, transmitter = msg_match.groups()
            current = {
                "id": int(frame_id),
                "name": name,
                "dlc": int(dlc),
                "transmitter": transmitter,
                "signals": {},
            }
            messages[name] = current
            continue
        sig_match = re.match(r"^\s*SG_\s+([A-Za-z_][A-Za-z0-9_]*)\s+(?:[Mm]\s+)?(?::|m\d+\s*:)", line)
        if sig_match and current is not None:
            signal = sig_match.group(1)
            current["signals"][signal] = {"name": signal, "message": current["name"]}
    signals = {
        f"{message['name']}.{signal_name}": signal
        for message in messages.values()
        for signal_name, signal in message.get("signals", {}).items()
    }
    return {
        "messages": messages,
        "signals": signals,
        "message_count": len(messages),
        "signal_count": len(signals),
    }


def _parse_a2l_file(path: Path) -> Dict[str, Any]:
    try:
        from . import source_parser
        result = source_parser.parse_a2l(path)
        if result.get("status") != "error":
            return result
    except Exception:
        pass
    text = _read_text_best_effort(path)
    characteristics = sorted(set(re.findall(r"/begin\s+CHARACTERISTIC\s+([^\s]+)", text, flags=re.IGNORECASE)))
    measurements = sorted(set(re.findall(r"/begin\s+MEASUREMENT\s+([^\s]+)", text, flags=re.IGNORECASE)))
    return {
        "characteristics": characteristics,
        "measurements": measurements,
        "characteristic_count": len(characteristics),
        "measurement_count": len(measurements),
    }


def _parse_cfg_file(path: Path) -> Dict[str, Any]:
    try:
        from . import source_parser
        result = source_parser.parse_cfg(path)
        if result.get("status") != "error":
            return result
    except Exception:
        pass
    text = _read_text_best_effort(path)
    header = next((line.strip() for line in text.splitlines() if line.startswith(";CANoe Version")), "")
    version = ""
    match = re.search(r"^Version:\s*(.+)$", text, flags=re.MULTILINE)
    if match:
        version = match.group(1).strip()
    references = []
    quoted_paths = re.findall(r"<VFileName\b[^>]*>\s*\d*(?:\s+base=cfg)?\s+\"([^\"]*)\"", text)
    quoted_paths.extend(re.findall(r"<VFileName\b[^>]*\bname=\"([^\"]*)\"", text))
    for item in quoted_paths:
        value = item.strip()
        if not value:
            continue
        suffix = Path(value).suffix.lower().lstrip(".") or "unknown"
        references.append({
            "path": value,
            "kind": suffix,
            "basename": Path(value).name,
        })
    mounted_files: Dict[str, List[str]] = {}
    for ref in references:
        mounted_files.setdefault(ref["kind"], []).append(ref["path"])
    return {
        "header": header,
        "version": version,
        "file_references": references,
        "mounted_files": {key: sorted(set(values)) for key, values in mounted_files.items()},
        "reference_count": len(references),
        "line_count": text.count("\n") + 1,
    }


def _parse_xml_attrs(attr_text: str) -> Dict[str, str]:
    return {
        key: value
        for key, _quote, value in re.findall(r"([A-Za-z_][A-Za-z0-9_.:-]*)\s*=\s*(['\"])(.*?)\2", attr_text)
    }


def _xml_blocks(text: str, tag: str) -> Iterable[Tuple[Dict[str, str], str]]:
    pattern = rf"<{tag}\b([^>]*)>(.*?)</{tag}>"
    for match in re.finditer(pattern, text, flags=re.IGNORECASE | re.DOTALL):
        yield _parse_xml_attrs(match.group(1)), match.group(2)


def _xml_element_attrs(text: str, tag: str) -> Iterable[Dict[str, str]]:
    yielded = set()
    for attrs, _body in _xml_blocks(text, tag):
        marker = tuple(sorted(attrs.items()))
        yielded.add(marker)
        yield attrs
    for attr_text in re.findall(rf"<{tag}\b([^>]*)/>", text, flags=re.IGNORECASE | re.DOTALL):
        attrs = _parse_xml_attrs(attr_text)
        marker = tuple(sorted(attrs.items()))
        if marker not in yielded:
            yield attrs


def _xml_texts(block: str, tag: str) -> List[str]:
    return [
        re.sub(r"\s+", " ", value).strip()
        for value in re.findall(rf"<{tag}\b[^>]*>(.*?)</{tag}>", block, flags=re.IGNORECASE | re.DOTALL)
        if re.sub(r"\s+", " ", value).strip()
    ]


def _normalize_cdd_name(value: str) -> str:
    text = re.sub(r"\s+", " ", value).strip()
    text = re.sub(r"^\(\$[0-9A-Fa-f]+\)\s*", "", text)
    text = re.split(r"\s+-\s+|\s+\(", text, maxsplit=1)[0].strip()
    return text


def _cdd_sid_aliases(value: str) -> List[str]:
    if not value:
        return []
    try:
        number = int(value, 10)
    except ValueError:
        return []
    hex_text = f"{number:X}"
    return [str(number), hex_text, f"0x{hex_text}", f"${hex_text}"]


def _cdd_name_aliases(*values: str) -> List[str]:
    aliases = set()
    for value in values:
        text = _as_text(value)
        if not text:
            continue
        aliases.add(text)
        normalized = _normalize_cdd_name(text)
        if normalized:
            aliases.add(normalized)
    return sorted(aliases)


def _parse_cdd_file(path: Path) -> Dict[str, Any]:
    try:
        from . import source_parser
        result = source_parser.parse_cdd(path)
        if result.get("status") != "error":
            return result
    except Exception:
        pass
    text = _read_text_best_effort(path)
    service_entries: List[Dict[str, Any]] = []
    service_aliases = set()
    for attrs, block in _xml_blocks(text, "PROTOCOLSERVICE"):
        names = _xml_texts(block, "TUV")
        quals = _xml_texts(block, "QUAL")
        req_block = next((child for _child_attrs, child in _xml_blocks(block, "REQ")), "")
        pos_block = next((child for _child_attrs, child in _xml_blocks(block, "POS")), "")
        req_sid = next(
            (
                comp_attrs.get("v", "")
                for comp_attrs in _xml_element_attrs(req_block, "CONSTCOMP")
                if comp_attrs.get("spec", "").lower() == "sid"
            ),
            "",
        )
        pos_sid = next(
            (
                comp_attrs.get("v", "")
                for comp_attrs in _xml_element_attrs(pos_block, "CONSTCOMP")
                if comp_attrs.get("spec", "").lower() == "sid"
            ),
            "",
        )
        aliases = set(_cdd_name_aliases(*(names + quals)))
        aliases.update(_cdd_sid_aliases(req_sid))
        service_aliases.update(alias.lower() for alias in aliases)
        service_entries.append({
            "id": attrs.get("id", ""),
            "oid": attrs.get("oid", ""),
            "name": _normalize_cdd_name(names[0]) if names else "",
            "display_name": names[0] if names else "",
            "qualifier": quals[0] if quals else "",
            "request_sid": req_sid,
            "positive_response_sid": pos_sid,
            "aliases": sorted(aliases),
            "functional": attrs.get("func", ""),
            "physical": attrs.get("phys", ""),
            "response_on_physical": attrs.get("respOnPhys", ""),
            "response_on_functional": attrs.get("respOnFunc", ""),
        })

    did_entries: List[Dict[str, Any]] = []
    did_aliases = set()
    for attrs, block in _xml_blocks(text, "DID"):
        did_number = attrs.get("n", "")
        names = _xml_texts(block, "TUV")
        quals = _xml_texts(block, "QUAL")
        aliases = set(_cdd_name_aliases(*(names + quals)))
        aliases.update(_cdd_sid_aliases(did_number))
        did_aliases.update(alias.lower() for alias in aliases)
        data_objects = []
        for data_attrs, data_block in _xml_blocks(block, "DATAOBJ"):
            data_names = _xml_texts(data_block, "TUV")
            data_quals = _xml_texts(data_block, "QUAL")
            data_objects.append({
                "name": _normalize_cdd_name(data_names[0]) if data_names else "",
                "qualifier": data_quals[0] if data_quals else "",
                "dtref": data_attrs.get("dtref", ""),
            })
        did_entries.append({
            "id": attrs.get("id", ""),
            "oid": attrs.get("oid", ""),
            "number": did_number,
            "hex": f"0x{int(did_number):X}" if did_number.isdigit() else "",
            "name": _normalize_cdd_name(names[0]) if names else "",
            "display_name": names[0] if names else "",
            "qualifier": quals[0] if quals else "",
            "aliases": sorted(aliases),
            "data_objects": data_objects,
        })

    legacy_names = set(re.findall(r"<SHORT-NAME>\s*([^<]+?)\s*</SHORT-NAME>", text, flags=re.IGNORECASE))
    legacy_names.update(re.findall(r'\b(?:SERVICE|Service|service)\s*=\s*"([^"]+)"', text))
    legacy_names.update(re.findall(r'\b(?:qualifier|Qualifier|name|Name)\s*=\s*"([A-Za-z_][A-Za-z0-9_./:-]*)"', text))
    service_aliases.update(name.strip().lower() for name in legacy_names if name.strip())
    services = sorted({alias for alias in service_aliases if alias})
    return {
        "services": services,
        "service_entries": service_entries,
        "service_count": len(service_entries) or len(services),
        "did_entries": did_entries,
        "did_aliases": sorted(did_aliases),
        "did_count": len(did_entries),
        "parser_note": "Lightweight Candela CDD parser for protocol services, DID names, aliases, SID values, and data objects.",
    }


def _parse_declared_sources(
    source_files: Dict[str, List[str]],
    template_path: Path,
    strict: bool,
) -> Tuple[Dict[str, Any], List[Dict[str, Any]], str]:
    parsers = {
        "dbc": _parse_dbc_file,
        "a2l": _parse_a2l_file,
        "cdd": _parse_cdd_file,
        "cfg": _parse_cfg_file,
    }
    source_models: Dict[str, Any] = {}
    issues: List[Dict[str, Any]] = []
    for kind, paths in source_files.items():
        model = {"kind": kind, "files": [], "status": "not_declared"}
        for path_text in paths or []:
            resolved = _resolve_declared_path(path_text, template_path)
            file_entry = {
                "declared": resolved["declared"],
                "resolved": resolved["resolved"],
                "exists": resolved["exists"],
                "status": "missing" if not resolved["exists"] else "parsed",
            }
            if not resolved["exists"]:
                issues.append({
                    "severity": "error" if strict else "warning",
                    "category": "source_model",
                    "source_kind": kind,
                    "message": f"{kind.upper()} source file not found: {resolved['declared']}",
                    "resolved": resolved["resolved"],
                })
            elif kind in parsers:
                try:
                    file_entry["model"] = parsers[kind](Path(resolved["resolved"]))
                except Exception as exc:
                    file_entry["status"] = "parse_error"
                    file_entry["error"] = str(exc)
                    issues.append({
                        "severity": "error" if strict else "warning",
                        "category": "source_model",
                        "source_kind": kind,
                        "message": f"{kind.upper()} source parse failed: {resolved['declared']}: {exc}",
                    })
            else:
                file_entry["status"] = "declared"
            model["files"].append(file_entry)
        if not model["files"]:
            model["status"] = "not_declared"
        elif any(item["status"] == "parsed" for item in model["files"]):
            model["status"] = "parsed" if all(item["status"] == "parsed" for item in model["files"]) else "partial"
        elif any(item["status"] == "declared" for item in model["files"]):
            model["status"] = "declared" if all(item["status"] == "declared" for item in model["files"]) else "partial"
        elif any(item["status"] == "parse_error" for item in model["files"]):
            model["status"] = "parse_error"
        else:
            model["status"] = "missing"
        source_models[kind] = model
    status = "fail" if any(item["severity"] == "error" for item in issues) else (
        "warn" if issues else "pass"
    )
    return source_models, issues, status


def _source_model_loaded(source_models: Dict[str, Any], kind: str) -> bool:
    return any(item.get("status") == "parsed" for item in source_models.get(kind, {}).get("files", []))


def _object_parts(object_name: str) -> List[str]:
    text = _as_text(object_name).replace("::", ".")
    return [part for part in re.split(r"[./]", text) if part]


def _dbc_contains(source_models: Dict[str, Any], object_name: str, object_kind: str) -> Optional[bool]:
    if not _source_model_loaded(source_models, "dbc"):
        return None
    parts = _object_parts(object_name)
    if not parts:
        return None
    messages = set()
    signals = set()
    signal_pairs = set()
    for file_entry in source_models.get("dbc", {}).get("files", []):
        model = file_entry.get("model", {})
        for message_name, message in model.get("messages", {}).items():
            messages.add(message_name.lower())
            for signal_name in message.get("signals", {}):
                signals.add(signal_name.lower())
                signal_pairs.add((message_name.lower(), signal_name.lower()))
    if object_kind == "message":
        return parts[-1].lower() in messages
    if len(parts) >= 2:
        return (parts[-2].lower(), parts[-1].lower()) in signal_pairs
    return parts[-1].lower() in signals


def _a2l_contains(source_models: Dict[str, Any], object_name: str, object_kind: str) -> Optional[bool]:
    if not _source_model_loaded(source_models, "a2l"):
        return None
    name = (_object_parts(object_name) or [""])[-1].lower()
    values = set()
    key = "characteristics" if object_kind == "characteristic" else "measurements"
    for file_entry in source_models.get("a2l", {}).get("files", []):
        values.update(item.lower() for item in file_entry.get("model", {}).get(key, []))
    return name in values


def _cdd_contains(source_models: Dict[str, Any], object_name: str) -> Optional[bool]:
    if not _source_model_loaded(source_models, "cdd"):
        return None
    raw_name = _as_text(object_name)
    name = (_object_parts(raw_name) or [raw_name])[-1].lower()
    candidates = {name, _normalize_cdd_name(raw_name).lower()}
    for number in re.findall(r"(?:0x|\$)?([0-9A-Fa-f]{2,4})", raw_name):
        candidates.add(number.lower())
        candidates.add(f"0x{number}".lower())
        candidates.add(f"${number}".lower())
        try:
            candidates.add(str(int(number, 16)))
        except ValueError:
            pass
    values = set()
    for file_entry in source_models.get("cdd", {}).get("files", []):
        model = file_entry.get("model", {})
        values.update(item.lower() for item in model.get("services", []))
        values.update(item.lower() for item in model.get("did_aliases", []))
    return any(candidate in values for candidate in candidates if candidate)


def _first_parsed_source_entry(source_models: Dict[str, Any], kind: str) -> Dict[str, Any]:
    for item in source_models.get(kind, {}).get("files", []):
        if item.get("status") == "parsed":
            return item
    return {}


def _resolved_source_paths(source_models: Dict[str, Any], kind: str) -> List[str]:
    paths = []
    for item in source_models.get(kind, {}).get("files", []):
        if item.get("exists") and item.get("resolved"):
            paths.append(str(item["resolved"]))
    return sorted(set(paths))


def _add_issue(
    issues: List[Dict[str, Any]],
    severity: str,
    category: str,
    message: str,
    row: Optional[Dict[str, Any]] = None,
    field: Optional[str] = None,
) -> None:
    issues.append({
        "severity": severity,
        "category": category,
        "test_case_id": _as_text(row.get("用例ID")) if row else "",
        "step_no": _as_text(row.get("步骤序号")) if row else "",
        "field": field or "",
        "message": message,
    })


def _step_requires_dbc(step: Dict[str, Any]) -> bool:
    values = [
        _as_text(step.get("操作类型")),
        _as_text(step.get("条件类型")),
        _as_text(step.get("结果类型")),
    ]
    return any("CAN" in v for v in values)


def _step_requires_a2l(step: Dict[str, Any]) -> bool:
    values = [
        _as_text(step.get("操作类型")),
        _as_text(step.get("条件类型")),
        _as_text(step.get("结果类型")),
    ]
    return any("XCP" in v or "观测量" in v for v in values)


def _step_requires_cdd(step: Dict[str, Any]) -> bool:
    values = [
        _as_text(step.get("操作类型")),
        _as_text(step.get("条件类型")),
        _as_text(step.get("结果类型")),
    ]
    return any("诊断" in v for v in values)


def _group_steps(test_case_rows: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    grouped: Dict[str, Dict[str, Any]] = {}
    for row in test_case_rows:
        case_id = _as_text(row.get("用例ID"))
        if not case_id:
            continue
        case = grouped.setdefault(case_id, {
            "case_id": case_id,
            "requirement_id": _as_text(row.get("需求ID")),
            "requirement_ids": set(),
            "feature": _as_text(row.get("功能点")),
            "name": _as_text(row.get("用例名称")),
            "priority": _as_text(row.get("优先级")),
            "automation": _as_text(row.get("自动化标记")),
            "preconditions": _as_text(row.get("前置条件")),
            "steps": [],
            "required_sources": set(),
        })
        requirement_id = _as_text(row.get("需求ID"))
        if requirement_id:
            case["requirement_ids"].add(requirement_id)
            if not case.get("requirement_id"):
                case["requirement_id"] = requirement_id
        required_sources = case["required_sources"]
        if _step_requires_dbc(row):
            required_sources.add("dbc")
        if _step_requires_a2l(row):
            required_sources.add("a2l")
        if _step_requires_cdd(row):
            required_sources.add("cdd")
        case["steps"].append({
            "step_no": _as_int(row.get("步骤序号")),
            "operation": {
                "type": _as_text(row.get("操作类型")),
                "channel": _as_text(row.get("操作通道")),
                "object": _as_text(row.get("操作对象")),
                "value": _as_text(row.get("操作值/参数")),
                "period_ms": _as_int(row.get("操作周期ms")),
                "duration_ms": _as_int(row.get("操作持续ms")),
            },
            "condition": {
                "type": _as_text(row.get("条件类型")),
                "object": _as_text(row.get("条件对象")),
                "operator": COMPARE_OPERATOR_MAP.get(_as_text(row.get("条件比较符")), _as_text(row.get("条件比较符"))),
                "expected": _as_text(row.get("条件期望值")),
                "timeout_ms": _as_int(row.get("条件超时ms")),
            },
            "expected_result": {
                "type": _as_text(row.get("结果类型")),
                "object": _as_text(row.get("结果对象")),
                "operator": COMPARE_OPERATOR_MAP.get(_as_text(row.get("结果比较符")), _as_text(row.get("结果比较符"))),
                "expected": _as_text(row.get("结果期望值")),
                "observe_ms": _as_int(row.get("结果观察窗口ms")),
            },
            "cleanup": _as_text(row.get("后置处理")),
            "notes": _as_text(row.get("备注")),
        })
    for case in grouped.values():
        case["steps"].sort(key=lambda step: step.get("step_no", 0))
        case["required_sources"] = sorted(case["required_sources"])
        case["requirement_ids"] = sorted(case["requirement_ids"])
    return grouped


def _write_structured_test_case(
    output_root: Path,
    project_config: Dict[str, Any],
    test_case_rows: List[Dict[str, Any]],
    correction_items: List[Dict[str, Any]],
) -> Tuple[Dict[str, Any], str]:
    grouped = _group_steps(test_case_rows)
    basic = project_config.get("basic", {})
    structured = {
        "schema_version": "0.1.0",
        "project": {
            "name": _as_text(basic.get("工程名称")) or "CANoe_AutoTest_Project",
            "code": _as_text(basic.get("项目代号")),
            "target_canoe_version": _as_text(basic.get("目标 CANoe 版本")) or "v15",
            "default_timeout_ms": _as_int(basic.get("默认超时 ms"), 5000),
        },
        "channels": project_config.get("enabled_channels", []),
        "strategy": project_config.get("strategy", {}),
        "cases": list(grouped.values()),
        "correction_items": correction_items,
    }
    path = output_root / "structured_test_cases.json"
    return structured, _write_json(path, structured)


def _operation_to_capl_hint(operation_type: str) -> List[str]:
    return {
        "CAN报文发送": ["message object", "output(msg)", "setTimer for periodic send"],
        "CAN报文停发": ["cancelTimer(periodic_send_timer)", "stop message schedule"],
        "CAN报文周期调整": ["setTimer(timer, new_period_ms)"],
        "CAN信号赋值": ["setSignal(signal, value)", "team wrapper when configured"],
        "XCP标定量赋值": ["xcpConnect", "xcpActivate", "A2L calibration write adapter"],
        "诊断服务请求": ["diagRequest", "diagSetParameter", "diagSendRequest"],
        "等待手动操作后确认": ["manual checkpoint", "testStepPass after confirmation"],
        "无操作": ["no-op"],
    }.get(operation_type, ["unknown operation"])


REQUIRED_SYMBOLS_BY_OPERATION = {
    "CAN报文发送": ["output (CAN)", "setTimer"],
    "CAN报文停发": ["cancelTimer"],
    "CAN报文周期调整": ["setTimer", "cancelTimer"],
    "CAN信号赋值": ["setSignal", "v15::capl::Test::SetSignal"],
    "XCP标定量赋值": ["xcpConnect", "xcpActivate", "xcpSetCalPage"],
    "诊断服务请求": ["diagSetTarget", "diagSetParameter", "diagSendRequest"],
    "等待手动操作后确认": ["TestCaseComment", "TestCaseFail"],
}

REQUIRED_SYMBOLS_BY_CONDITION = {
    "接收CAN报文发送": ["on message", "TestWaitForMessage"],
    "接收CAN报文超时": ["on message", "TestWaitForTimeout"],
    "CAN信号变化": ["TestWaitForSignalMatch", "TestWaitForSignalInRange"],
    "观测量变化": ["TestWaitForSignalMatch", "TestWaitForSignalInRange"],
    "诊断服务响应": ["diagGetParameter"],
    "等待手动操作后确认": ["TestCaseComment", "TestCaseFail"],
    "等待固定时间": ["TestWaitForTimeout"],
}

REQUIRED_SYMBOLS_BY_RESULT = {
    "接收CAN报文发送": ["on message", "TestWaitForMessage"],
    "接收CAN报文超时": ["TestWaitForTimeout"],
    "CAN信号变化": ["TestWaitForSignalMatch", "CheckSignalMatch"],
    "观测量变化": ["TestWaitForSignalMatch", "CheckSignalMatch"],
    "诊断服务响应": ["diagGetParameter"],
}


def _required_symbols_for_structured_case(case: Dict[str, Any]) -> List[str]:
    symbols: List[str] = []
    for step in case.get("steps", []):
        operation_type = step.get("operation", {}).get("type", "")
        condition_type = step.get("condition", {}).get("type", "")
        result_type = step.get("expected_result", {}).get("type", "")
        symbols.extend(REQUIRED_SYMBOLS_BY_OPERATION.get(operation_type, []))
        symbols.extend(REQUIRED_SYMBOLS_BY_CONDITION.get(condition_type, []))
        symbols.extend(REQUIRED_SYMBOLS_BY_RESULT.get(result_type, []))
    return sorted(set(symbols))


def _load_agent_kb_helpers():
    kb_root = ROOT / "knowledge_base"
    if str(kb_root) not in sys.path:
        sys.path.insert(0, str(kb_root))
    from agent_kb.kb_lookup import load_page, resolve_symbol, _load_page_by_id

    return load_page, resolve_symbol, _load_page_by_id


def _safe_first_text(value: Any) -> str:
    if isinstance(value, list):
        if not value:
            return ""
        return _as_text(value[0])
    return _as_text(value)


_KB_TOPICS = ("capl", "canoe_config", "com_automation", "cfg", "xcp", "diagnostics", "panel", "dbc")


def _page_topic(page_id: str, page: Dict[str, Any]) -> str:
    """Extract the knowledge-base topic category from a page_id or source path."""
    combined = f"{page_id or ''} {page.get('source', '') or ''} {page.get('page_type', '') or ''}".lower()
    for topic in _KB_TOPICS:
        if topic in combined:
            return topic
    return ""


def _page_matches_profile(page_id: str, page: Dict[str, Any], profile: Optional[Dict[str, Any]]) -> bool:
    """Check if a page's topic is allowed by the retrieval profile's topic filters."""
    if not profile:
        return True
    topic = _page_topic(page_id, page)
    if not topic:
        return True
    blocked = set(profile.get("blocked_topic_filters", []))
    allowed = set(profile.get("topic_filters", []))
    if topic in blocked:
        return False
    if allowed and topic not in allowed:
        return False
    return True


def _load_symbol_evidence(
    symbol: str,
    version: str,
    profile: Optional[Dict[str, Any]] = None,
) -> Tuple[Optional[Dict[str, Any]], Optional[Dict[str, Any]]]:
    load_page, resolve_symbol, load_page_by_id = _load_agent_kb_helpers()
    try:
        if "::" in symbol:
            page_id = symbol
            page = load_page_by_id(page_id)
        else:
            page_id = resolve_symbol(symbol, prefer_version=version)
            page = load_page(symbol, version=version) if page_id else None
    except Exception as exc:
        return None, {"symbol": symbol, "reason": f"lookup_error: {exc}"}
    if not page_id or not page:
        return None, {"symbol": symbol, "reason": "not_found"}
    if profile and not _page_matches_profile(page_id, page, profile):
        topic = _page_topic(page_id, page)
        return None, {
            "symbol": symbol,
            "reason": f"blocked_by_profile: topic '{topic}' is not allowed by profile '{profile.get('id', '')}'",
            "page_id": page_id,
        }
    evidence = {
        "symbol": symbol,
        "page_id": page_id,
        "name": page.get("name") or page.get("title") or symbol,
        "page_type": page.get("page_type", ""),
        "syntax": page.get("syntax", []),
        "description": _safe_first_text(page.get("description")),
        "source": page.get("source", ""),
        "confidence": "exact",
        "used_for": ["capl_generation", "validation"],
    }
    return evidence, None


def _team_evidence_pages(project_config: Dict[str, Any]) -> List[Dict[str, Any]]:
    strategy = project_config.get("strategy", {})
    enabled = _normalize_bool_yes(strategy.get("启用团队代码规范", "是"))
    if not enabled:
        return []
    team_docs = [
        ROOT / "knowledge_base" / "extras" / "team" / "CAPL_Internal_Coding_Standards.json",
        ROOT / "knowledge_base" / "extras" / "team" / "Common_Gotchas.json",
    ]
    pages = []
    for path in team_docs:
        if path.exists():
            data = json.loads(path.read_text(encoding="utf-8"))
            pages.append({
                "symbol": f"team::{path.stem}",
                "page_id": f"extras::team::_root::{path.stem}",
                "name": data.get("name") or path.stem,
                "page_type": data.get("page_type", "team"),
                "syntax": [],
                "description": _safe_first_text(data.get("description") or data.get("summary")),
                "source": str(path),
                "confidence": "team_override",
                "used_for": ["team_style", "validation"],
            })
    return pages


@action(
    reads=["structured_test_case", "project_config", "output_root"],
    writes=["evidence_bundle", "evidence_bundle_file", "evidence_status"],
)
def retrieve_evidence(state: State) -> Tuple[Dict[str, Any], State]:
    structured = state.get("structured_test_case", {})
    project_config = state.get("project_config", {})
    output_root = Path(state.get("output_root") or DEFAULT_OUTPUT)
    version = structured.get("project", {}).get("target_canoe_version") or "v15"
    profile = _workflow_retrieval_profile("capl_authoring")

    required_by_case = {}
    all_symbols = set()
    for case in structured.get("cases", []):
        symbols = _required_symbols_for_structured_case(case)
        required_by_case[case.get("case_id", "")] = symbols
        all_symbols.update(symbols)

    pages = []
    gaps = []
    for symbol in sorted(all_symbols):
        evidence, gap = _load_symbol_evidence(symbol, version, profile)
        if evidence:
            pages.append(evidence)
        if gap:
            gaps.append(gap)
    pages.extend(_team_evidence_pages(project_config))

    bundle = {
        "schema_version": "0.1.0",
        "status": "complete" if not gaps else "partial",
        "target_canoe_version": version,
        "retrieval_profile": profile["id"],
        "retrieval_profile_file": profile["profile_path"],
        "topic_filters": profile.get("topic_filters", []),
        "blocked_topic_filters": profile.get("blocked_topic_filters", []),
        "required_symbols_by_case": required_by_case,
        "pages": pages,
        "gaps": gaps,
    }
    bundle_file = _write_json(output_root / "evidence_bundle.json", bundle)
    result = {
        "evidence_bundle": bundle,
        "evidence_bundle_file": bundle_file,
        "evidence_status": bundle["status"],
    }
    return result, state.update(**result)


def _coverage_step_domains(step: Dict[str, Any]) -> List[str]:
    values = " ".join([
        _as_text(step.get("operation", {}).get("type")),
        _as_text(step.get("condition", {}).get("type")),
        _as_text(step.get("expected_result", {}).get("type")),
    ])
    domains = []
    if "CAN" in values:
        domains.append("can")
    if "XCP" in values or "观测量" in values:
        domains.append("xcp")
    if "诊断" in values:
        domains.append("diagnostics")
    if "手动" in values:
        domains.append("manual")
    if "固定时间" in values:
        domains.append("timing")
    return sorted(set(domains))


def _coverage_report_from_state(
    structured: Dict[str, Any],
    source_models: Dict[str, Any],
    evidence_bundle: Dict[str, Any],
    profile: Dict[str, Any],
) -> Dict[str, Any]:
    cases = list(structured.get("cases", []))
    risks: List[Dict[str, Any]] = []
    requirement_to_cases: Dict[str, List[str]] = defaultdict(list)
    cases_without_requirement = []
    feature_to_cases: Dict[str, List[str]] = defaultdict(list)
    domain_to_steps: Dict[str, int] = defaultdict(int)
    required_sources = set()
    adapter_heavy_steps = 0

    for case in cases:
        case_id = _as_text(case.get("case_id"))
        requirement_ids = case.get("requirement_ids") or []
        if not requirement_ids and _as_text(case.get("requirement_id")):
            requirement_ids = [_as_text(case.get("requirement_id"))]
        if not requirement_ids:
            cases_without_requirement.append(case_id)
        for requirement_id in requirement_ids:
            requirement_to_cases[_as_text(requirement_id)].append(case_id)
        feature = _as_text(case.get("feature")) or "未分类"
        feature_to_cases[feature].append(case_id)
        required_sources.update(case.get("required_sources", []))
        for step in case.get("steps", []):
            domains = _coverage_step_domains(step)
            for domain in domains:
                domain_to_steps[domain] += 1
            if {"xcp", "diagnostics"} & set(domains):
                adapter_heavy_steps += 1

    source_status = {
        kind: source_models.get(kind, {}).get("status", "not_declared")
        for kind in ("dbc", "a2l", "cdd", "cfg", "dll")
    }
    for kind in sorted(required_sources):
        if source_status.get(kind) not in {"parsed", "declared"}:
            risks.append({
                "severity": "warning",
                "category": "source_coverage",
                "message": f"{kind.upper()} is required by test steps but source model status is {source_status.get(kind, 'missing')}.",
            })

    if cases_without_requirement:
        risks.append({
            "severity": "warning",
            "category": "requirement_coverage",
            "message": "Some test cases have no requirement id.",
            "cases": cases_without_requirement,
        })

    gaps = list(evidence_bundle.get("gaps", []))
    if gaps:
        risks.append({
            "severity": "warning",
            "category": "capl_evidence",
            "message": "Some CAPL symbols do not have KB evidence.",
            "gap_count": len(gaps),
            "symbols": [gap.get("symbol") for gap in gaps if isinstance(gap, dict)],
        })

    if adapter_heavy_steps:
        risks.append({
            "severity": "info",
            "category": "adapter_binding",
            "message": "XCP or diagnostics steps require project adapter bindings before release use.",
            "step_count": adapter_heavy_steps,
        })

    status = "fail" if not cases else ("warn" if any(risk["severity"] == "warning" for risk in risks) else "pass")
    if not cases:
        risks.append({
            "severity": "error",
            "category": "test_case_coverage",
            "message": "No structured test cases are available for coverage analysis.",
        })

    required_symbols = evidence_bundle.get("required_symbols_by_case", {})
    all_required_symbols = sorted({
        symbol
        for symbols in required_symbols.values()
        for symbol in (symbols or [])
    })
    resolved_symbols = sorted({
        _as_text(page.get("symbol"))
        for page in evidence_bundle.get("pages", [])
        if _as_text(page.get("symbol"))
    })
    return {
        "schema_version": "0.1.0",
        "agent": "KBIndexed_TestCoverageAnalyzer",
        "retrieval_profile": profile["id"],
        "retrieval_profile_file": profile["profile_path"],
        "topic_filters": profile.get("topic_filters", []),
        "blocked_topic_filters": profile.get("blocked_topic_filters", []),
        "status": status,
        "case_count": len(cases),
        "step_count": sum(len(case.get("steps", [])) for case in cases),
        "requirement_coverage": {
            "covered_requirement_count": len(requirement_to_cases),
            "covered_requirement_ids": sorted(requirement_to_cases),
            "requirement_to_cases": {key: sorted(value) for key, value in sorted(requirement_to_cases.items())},
            "cases_without_requirement": cases_without_requirement,
        },
        "feature_coverage": {
            "feature_count": len(feature_to_cases),
            "feature_to_cases": {key: sorted(value) for key, value in sorted(feature_to_cases.items())},
        },
        "domain_coverage": {
            "step_count_by_domain": dict(sorted(domain_to_steps.items())),
            "required_sources": sorted(required_sources),
            "source_status": source_status,
        },
        "capl_evidence_coverage": {
            "required_symbol_count": len(all_required_symbols),
            "resolved_symbol_count": len(set(resolved_symbols)),
            "gap_count": len(gaps),
            "required_symbols": all_required_symbols,
            "resolved_symbols": resolved_symbols,
        },
        "risks": risks,
    }


@action(
    reads=["structured_test_case", "source_models", "evidence_bundle", "project_config", "output_root"],
    writes=["coverage_report", "coverage_report_file", "coverage_status"],
)
def analyze_test_coverage(state: State) -> Tuple[Dict[str, Any], State]:
    output_root = _state_output_root(state)
    profile = _workflow_retrieval_profile("capl_authoring")
    report = _coverage_report_from_state(
        state.get("structured_test_case", {}),
        state.get("source_models", {}),
        state.get("evidence_bundle", {}),
        profile,
    )
    report_file = _write_json(output_root / "coverage_report.json", report)
    result = {
        "coverage_report": report,
        "coverage_report_file": report_file,
        "coverage_status": report["status"],
    }
    return result, state.update(**result)


@action(
    reads=["evidence_bundle", "project_config", "output_root"],
    writes=["evidence_gate_status", "evidence_gate_report", "evidence_gate_report_file"],
)
def validate_evidence_gate(state: State) -> Tuple[Dict[str, Any], State]:
    bundle = state.get("evidence_bundle", {})
    project_config: Dict[str, Any] = state.get("project_config", {})
    output_root = _state_output_root(state)
    gate_enabled = _normalize_bool_yes(_strategy_value(project_config, "启用证据链校验", "是"))
    gaps = bundle.get("gaps", [])
    issues = []
    if gate_enabled and gaps:
        for gap in gaps:
            issues.append({
                "severity": "error",
                "category": "capl_api_evidence",
                "message": f"CAPL API evidence gap: {gap.get('symbol') or gap}",
                "detail": gap,
            })
    elif gaps:
        for gap in gaps:
            issues.append({
                "severity": "warning",
                "category": "capl_api_evidence",
                "message": f"Evidence gap recorded but gate disabled: {gap.get('symbol') or gap}",
                "detail": gap,
            })
    status = "fail" if any(item["severity"] == "error" for item in issues) else (
        "warn" if issues else "pass"
    )
    report = {
        "schema_version": "0.1.0",
        "status": status,
        "gate_enabled": gate_enabled,
        "evidence_status": bundle.get("status", "unknown"),
        "gap_count": len(gaps),
        "issues": issues,
    }
    report_file = _write_json(output_root / "evidence_gate_report.json", report)
    result = {
        "evidence_gate_status": status,
        "evidence_gate_report": report,
        "evidence_gate_report_file": report_file,
    }
    return result, state.update(**result)


@action(
    reads=["test_case_excel_path", "requirements_path", "dbc_paths", "a2l_paths", "cdd_paths"],
    writes=["raw_test_case", "project_config", "test_case_rows", "source_files"],
)
def load_test_case_template(state: State) -> Tuple[Dict[str, Any], State]:
    excel_path = Path(state.get("test_case_excel_path") or DEFAULT_TEMPLATE)
    project_config, rows, raw = parse_template(excel_path)
    source_files = _source_files_from_state(state, project_config)
    result = {
        "raw_test_case": raw,
        "project_config": project_config,
        "test_case_rows": rows,
        "source_files": source_files,
    }
    return result, state.update(**result)


@action(
    reads=["raw_test_case", "test_case_rows", "output_root"],
    writes=["template_contract_status", "template_contract_report", "template_contract_report_file"],
)
def validate_template_contract(state: State) -> Tuple[Dict[str, Any], State]:
    rows: List[Dict[str, Any]] = state.get("test_case_rows", [])
    output_root = _state_output_root(state)
    issues: List[Dict[str, Any]] = []
    if not FIELD_MAPPING_PATH.exists():
        issues.append({"severity": "error", "message": f"Canonical field mapping missing: {FIELD_MAPPING_PATH}"})
    if WORKFLOW_FIELD_MAPPING_POINTER.exists():
        pointer = json.loads(WORKFLOW_FIELD_MAPPING_POINTER.read_text(encoding="utf-8"))
        source = _as_text(pointer.get("source_of_truth"))
        if source and Path(source).resolve() != FIELD_MAPPING_PATH.resolve():
            issues.append({
                "severity": "error",
                "message": "Workflow template_field_mapping.json pointer does not reference the canonical mapping file.",
            })
    expected_columns = set(FIELD_MAPPING.get("test_case_columns", []))
    actual_columns = set(rows[0].keys()) if rows else expected_columns
    missing = sorted(expected_columns - actual_columns)
    if missing:
        issues.append({"severity": "error", "message": f"Excel test case columns missing from mapping contract: {missing}"})
    enum_sets = {
        "operation_types": OPERATION_TYPES,
        "condition_types": CONDITION_TYPES,
        "result_types": RESULT_TYPES,
    }
    for name, values in enum_sets.items():
        if not values:
            issues.append({"severity": "error", "message": f"Empty enum set: {name}"})
    status = "fail" if any(item["severity"] == "error" for item in issues) else "pass"
    report = {
        "schema_version": "0.1.0",
        "status": status,
        "canonical_mapping": str(FIELD_MAPPING_PATH),
        "workflow_pointer": str(WORKFLOW_FIELD_MAPPING_POINTER),
        "issues": issues,
    }
    report_file = _write_json(output_root / "template_contract_report.json", report)
    result = {
        "template_contract_status": status,
        "template_contract_report": report,
        "template_contract_report_file": report_file,
    }
    return result, state.update(**result)


@action(
    reads=["raw_test_case", "project_config", "source_files", "strict_source_validation", "output_root"],
    writes=["source_models", "source_model_file", "source_model_issues", "source_check_status"],
)
def parse_source_files(state: State) -> Tuple[Dict[str, Any], State]:
    raw = state.get("raw_test_case", {})
    project_config: Dict[str, Any] = state.get("project_config", {})
    source_files: Dict[str, List[str]] = state.get("source_files", {})
    output_root = _state_output_root(state)
    template_path = Path(raw.get("template_path") or state.get("test_case_excel_path") or DEFAULT_TEMPLATE)
    strict = _strict_source_validation(state, project_config)
    source_models, issues, status = _parse_declared_sources(source_files, template_path, strict)
    source_model_file = _write_json(output_root / "source_models.json", {
        "schema_version": "0.1.0",
        "status": status,
        "strict_source_validation": strict,
        "source_files": source_files,
        "models": source_models,
        "issues": issues,
    })
    result = {
        "source_models": source_models,
        "source_model_file": source_model_file,
        "source_model_issues": issues,
        "source_check_status": status,
    }
    return result, state.update(**result)


_TEST_CASE_RULES_CACHE: Optional[Dict[str, Any]] = None


def _load_test_case_rules() -> Dict[str, Any]:
    global _TEST_CASE_RULES_CACHE
    if _TEST_CASE_RULES_CACHE is not None:
        return _TEST_CASE_RULES_CACHE
    rules_path = WORKFLOW_KB_DIR / "validation_rules" / "test_case_field_rules.json"
    if rules_path.exists():
        _TEST_CASE_RULES_CACHE = json.loads(rules_path.read_text(encoding="utf-8"))
    else:
        _TEST_CASE_RULES_CACHE = {}
    return _TEST_CASE_RULES_CACHE


_SEMANTIC_CHECK_DISPATCH = {
    ("dbc", "message"): lambda models, target: _dbc_contains(models, target, "message"),
    ("dbc", "signal"): lambda models, target: _dbc_contains(models, target, "signal"),
    ("a2l", "characteristic"): lambda models, target: _a2l_contains(models, target, "characteristic"),
    ("a2l", "measurement"): lambda models, target: _a2l_contains(models, target, "measurement"),
    ("cdd", "service"): lambda models, target: _cdd_contains(models, target),
}

_SEMANTIC_CATEGORY = {
    ("dbc", "message"): "can_semantic",
    ("dbc", "signal"): "can_semantic",
    ("a2l", "characteristic"): "xcp_semantic",
    ("a2l", "measurement"): "xcp_semantic",
    ("cdd", "service"): "diagnostics_semantic",
}

_SEMANTIC_OBJECT_LABEL = {
    ("dbc", "message"): "报文",
    ("dbc", "signal"): "信号",
    ("a2l", "characteristic"): "标定量",
    ("a2l", "measurement"): "观测量",
    ("cdd", "service"): "诊断服务",
}

_SEMANTIC_SOURCE_LABEL = {"dbc": "DBC", "a2l": "A2L", "cdd": "CDD"}

_TYPE_KIND_LABEL = {"operation": "操作", "condition": "条件", "result": "结果"}


def _apply_typed_rule(
    issues: List[Dict[str, Any]],
    row: Dict[str, Any],
    type_value: str,
    type_kind: str,
    rules: Dict[str, Any],
    source_files: Dict[str, List[str]],
    source_models: Dict[str, Any],
    semantic_severity: str,
    target_field: str,
    expected_value_field: str = "",
) -> None:
    """Apply a typed rule (operation/condition/result) from the rule table to a row."""
    rule_set = rules.get(f"{type_kind}_rules", {})
    rule = rule_set.get(type_value)
    if not rule:
        return
    has_required = bool(rule.get("required_fields"))
    for field_name in rule.get("required_fields", []):
        if not _as_text(row.get(field_name)):
            _add_issue(issues, "error", type_kind, f"该{type_kind}类型需要填写{field_name}", row, field_name)
    if has_required and expected_value_field and not _as_text(row.get(expected_value_field)):
        _add_issue(issues, "warning", type_kind, f"建议填写{expected_value_field}", row, expected_value_field)
    source_kind = rule.get("source_kind")
    semantic_check = rule.get("semantic_check")
    if source_kind and semantic_check and has_required:
        if not source_files.get(source_kind):
            source_path_field = rule.get("source_path_field") or f"{source_kind.upper()}路径"
            _add_issue(issues, "error", source_kind, f"{type_kind}步骤需要 {source_kind.upper()} 路径", row, source_path_field)
        else:
            target = _as_text(row.get(target_field))
            if target:
                check_fn = _SEMANTIC_CHECK_DISPATCH.get((source_kind, semantic_check))
                if check_fn:
                    found = check_fn(source_models, target)
                    if found is False:
                        category = _SEMANTIC_CATEGORY.get((source_kind, semantic_check), "semantic")
                        source_label = _SEMANTIC_SOURCE_LABEL.get(source_kind, source_kind)
                        object_label = _SEMANTIC_OBJECT_LABEL.get((source_kind, semantic_check), "对象")
                        kind_label = _TYPE_KIND_LABEL.get(type_kind, type_kind)
                        message = f"{source_label} 中未找到{kind_label}{object_label}"
                        _add_issue(issues, semantic_severity, category, message, row, target_field)


@action(
    reads=[
        "raw_test_case",
        "project_config",
        "test_case_rows",
        "source_files",
        "source_models",
        "source_model_issues",
        "strict_source_validation",
        "output_root",
    ],
    writes=[
        "structured_test_case",
        "structured_test_case_file",
        "correction_items",
        "test_case_check_status",
    ],
)
def validate_test_cases(state: State) -> Tuple[Dict[str, Any], State]:
    rows: List[Dict[str, Any]] = state.get("test_case_rows", [])
    project_config: Dict[str, Any] = state.get("project_config", {})
    source_files: Dict[str, List[str]] = state.get("source_files", {})
    source_models: Dict[str, Any] = state.get("source_models", {})
    strict_sources = _strict_source_validation(state, project_config)
    semantic_severity = "error" if strict_sources else "warning"
    output_root = _state_output_root(state)
    issues: List[Dict[str, Any]] = list(state.get("source_model_issues", []))

    basic = project_config.get("basic", {})
    if not _as_text(basic.get("工程名称")):
        _add_issue(issues, "error", "project_config", "工程名称不能为空")
    if not _as_text(basic.get("目标 CANoe 版本")):
        _add_issue(issues, "error", "project_config", "目标 CANoe 版本不能为空")
    if not project_config.get("enabled_channels"):
        _add_issue(issues, "error", "project_config", "至少需要启用一个通信通道")

    for channel in project_config.get("enabled_channels", []):
        if not _as_text(channel.get("CANoe通道名")):
            _add_issue(issues, "error", "project_config", "启用通道缺少 CANoe通道名")
        if not _as_text(channel.get("仲裁波特率")):
            _add_issue(issues, "error", "project_config", "启用通道缺少仲裁波特率")
        if not _as_text(channel.get("采样点%")):
            _add_issue(issues, "warning", "project_config", "启用通道建议填写采样点%")
        if _as_text(channel.get("总线类型")) == "CANFD" and not _as_text(channel.get("数据波特率(CANFD)")):
            _add_issue(issues, "warning", "project_config", "CANFD 通道建议填写数据波特率")

    if not rows:
        _add_issue(issues, "error", "test_case", "测试用例表没有可解析的步骤行")

    requirement_ids = set()
    for row in rows:
        case_id = _as_text(row.get("用例ID"))
        requirement_id = _as_text(row.get("需求ID"))
        if requirement_id:
            requirement_ids.add(requirement_id)
        if not case_id:
            _add_issue(issues, "error", "test_case", "用例ID不能为空", row, "用例ID")
        if not _as_text(row.get("步骤序号")):
            _add_issue(issues, "error", "test_case", "步骤序号不能为空", row, "步骤序号")

        operation_type = _as_text(row.get("操作类型"))
        condition_type = _as_text(row.get("条件类型"))
        result_type = _as_text(row.get("结果类型"))
        if operation_type not in OPERATION_TYPES:
            _add_issue(issues, "error", "operation", f"未知操作类型: {operation_type}", row, "操作类型")
        if condition_type not in CONDITION_TYPES:
            _add_issue(issues, "error", "condition", f"未知条件类型: {condition_type}", row, "条件类型")
        if result_type not in RESULT_TYPES:
            _add_issue(issues, "error", "result", f"未知结果类型: {result_type}", row, "结果类型")

        rules = _load_test_case_rules()
        _apply_typed_rule(issues, row, operation_type, "operation", rules, source_files, source_models, semantic_severity, "操作对象")
        _apply_typed_rule(issues, row, condition_type, "condition", rules, source_files, source_models, semantic_severity, "条件对象", "条件期望值")
        _apply_typed_rule(issues, row, result_type, "result", rules, source_files, source_models, semantic_severity, "结果对象", "结果期望值")

    if state.get("requirements_path") and not requirement_ids:
        _add_issue(issues, "warning", "coverage", "提供了需求文件但测试用例未填写需求ID")

    structured, structured_path = _write_structured_test_case(output_root, project_config, rows, issues)
    has_error = any(item["severity"] == "error" for item in issues)
    has_warning = any(item["severity"] == "warning" for item in issues)
    status = "fail" if has_error else ("warn" if has_warning else "pass")
    correction_path = _write_json(output_root / "test_case_correction_items.json", issues)
    result = {
        "structured_test_case": structured,
        "structured_test_case_file": structured_path,
        "correction_items": issues,
        "test_case_correction_file": correction_path,
        "test_case_check_status": status,
    }
    return result, state.update(**result)


@action(
    reads=[
        "correction_items",
        "structured_test_case",
        "structured_test_case_file",
        "test_case_correction_file",
        "repair_plan",
        "repair_plan_file",
        "evidence_bundle",
        "coverage_report",
        "cfg_artifact",
        "can_artifact",
        "config_eval_report",
        "capl_eval_report",
        "run_id",
        "base_output_root",
        "output_root",
    ],
    writes=["final_outputs"],
)
def emit_test_case_corrections(state: State) -> Tuple[Dict[str, Any], State]:
    output_root = _state_output_root(state)
    base_output_root = Path(state.get("base_output_root") or output_root)
    correction_items = list(state.get("correction_items", []))
    structured = state.get("structured_test_case", {})
    repair_plan = state.get("repair_plan", {})
    if not correction_items and repair_plan.get("repair_items"):
        correction_items = repair_plan["repair_items"]
    final_outputs = {
        "status": "blocked_for_corrections",
        "run_id": state.get("run_id"),
        "output_root": str(output_root),
        "structured_test_case_file": state.get("structured_test_case_file"),
        "correction_file": state.get("test_case_correction_file"),
        "correction_count": len(correction_items),
        "repair_plan": state.get("repair_plan_file"),
        "repair_origin": repair_plan.get("origin", ""),
        "failure_category": repair_plan.get("failure_category", ""),
    }
    try:
        from . import correction_workbook
        wb_path = output_root / "test_case_corrections.xlsx"
        correction_workbook.generate_correction_workbook(correction_items, structured, wb_path)
        final_outputs["correction_workbook"] = str(wb_path)
        md_path = output_root / "test_case_corrections.md"
        correction_workbook.generate_correction_markdown(correction_items, structured, md_path)
        final_outputs["correction_markdown"] = str(md_path)
    except Exception:
        pass
    try:
        from . import html_report
        html_path = output_root / "run_report.html"
        state_for_report = {
            "run_id": state.get("run_id"),
            "status": "blocked_for_corrections",
            "structured_test_case": structured,
            "correction_items": correction_items,
            "evidence_bundle": state.get("evidence_bundle", {}),
            "coverage_report": state.get("coverage_report", {}),
            "cfg_artifact": state.get("cfg_artifact", {}),
            "can_artifact": state.get("can_artifact", {}),
            "config_eval_report": state.get("config_eval_report", {}),
            "capl_eval_report": state.get("capl_eval_report", {}),
            "repair_plan": repair_plan,
            "output_root": str(output_root),
        }
        html_report.generate_run_report(state_for_report, html_path)
        final_outputs["html_report"] = str(html_path)
        final_outputs["quick_summary"] = html_report.generate_quick_summary(state_for_report)
    except Exception:
        pass
    manifest_path = _write_json(output_root / "blocked_manifest.json", final_outputs)
    final_outputs["manifest"] = manifest_path
    if base_output_root != output_root:
        _write_json(base_output_root / "latest_run_manifest.json", {
            "run_id": state.get("run_id"),
            "output_root": str(output_root),
            "manifest": manifest_path,
        })
    result = {"final_outputs": final_outputs}
    return result, state.update(**result)


@action(
    reads=["structured_test_case", "project_config", "source_models", "evidence_bundle", "config_retry_count", "output_root"],
    writes=["canoe_config_plan", "cfg_artifact", "config_retry_count", "cfg_automation"],
)
def generate_canoe_config(state: State) -> Tuple[Dict[str, Any], State]:
    output_root = _state_output_root(state)
    structured = state.get("structured_test_case", {})
    project_config = state.get("project_config", {})
    source_models = state.get("source_models", {})
    project = structured.get("project", {})
    retry_count = _as_int(state.get("config_retry_count"), 0) + 1
    project_name = project.get("name", "CANoe_AutoTest_Project")
    cfg_source_entry = _first_parsed_source_entry(source_models, "cfg")
    cfg_source_path = Path(cfg_source_entry.get("resolved", "")) if cfg_source_entry.get("resolved") else None
    profile = _workflow_retrieval_profile("canoe_config")
    target_cfg_path = output_root / f"{project_name}.cfg"
    cfg_path = target_cfg_path if cfg_source_path else output_root / f"{project_name}.cfg.todo.json"
    cfg_plan_path = output_root / f"{project_name}.cfg.plan.json"
    cfg_automation_script_path = output_root / f"{project_name}.cfg.generate.ps1"
    layout_manifest_path = output_root / "canoe_project_layout_manifest.json"
    plan = {
        "schema_version": "0.1.0",
        "generator": "SubAgent2_Canoe工程配置专家",
        "target_canoe_version": project.get("target_canoe_version", "v15"),
        "project_name": project_name,
        "generation_mode": "canoe_com_automation_with_base_cfg_fallback" if cfg_source_path else "canoe_com_automation_plan",
        "retrieval_profile": profile["id"],
        "retrieval_profile_file": profile["profile_path"],
        "topic_filters": profile.get("topic_filters", []),
        "blocked_topic_filters": profile.get("blocked_topic_filters", []),
        "base_cfg_template": str(cfg_source_path) if cfg_source_path else _as_text(state.get("base_canoe_cfg_template")),
        "base_cfg_model": cfg_source_entry.get("model", {}),
        "official_generation_path": {
            "api_family": "CANoe COM Automation",
            "script": str(cfg_automation_script_path),
            "script_plan": str(cfg_plan_path),
            "execute_when": "canoe_validation_mode=automated",
            "fallback": "copy discovered/base cfg when present; otherwise emit a plan and script for CANoe to serialize",
        },
        "channels": structured.get("channels", []),
        "network_name": "CAN",
        "channel_display_name": _as_text(next(iter(structured.get("channels", [])), {}).get("CANoe通道名")) or "CAN",
        "mounted_files": {
            "dbc": sorted(set(_resolved_source_paths(source_models, "dbc")) | {_as_text(ch.get("DBC路径")) for ch in structured.get("channels", []) if _as_text(ch.get("DBC路径"))}),
            "a2l": sorted(set(_resolved_source_paths(source_models, "a2l")) | {_as_text(ch.get("A2L路径")) for ch in structured.get("channels", []) if _as_text(ch.get("A2L路径"))}),
            "cdd": sorted(set(_resolved_source_paths(source_models, "cdd")) | {_as_text(ch.get("CDD路径")) for ch in structured.get("channels", []) if _as_text(ch.get("CDD路径"))}),
            "dll": _resolved_source_paths(source_models, "dll"),
            "cfg": [str(cfg_source_path)] if cfg_source_path else [],
        },
        "source_model_status": {
            kind: model.get("status")
            for kind, model in source_models.items()
        },
        "test_modules": [
            {
                "name": f"{project.get('name', 'CANoe_AutoTest_Project')}_TestModule",
                "source": str(output_root / f"{project.get('name', 'CANoe_AutoTest_Project')}_TestModule.can"),
                "mount_strategy": "add as CAPL test module in generated or template CANoe configuration",
            }
        ],
        "evidence_status": state.get("evidence_bundle", {}).get("status", "unknown"),
        "notes": [
            "Official CFG generation is delegated to CANoe COM Automation; the workflow does not hand-write Vector's private .cfg serialization format.",
            "The generated PowerShell script opens a base cfg when available, mounts DBC/CDD/A2L/DLL inputs through COM APIs where supported, then asks CANoe to SaveAs the target cfg.",
            "Base CFG copy remains a fallback because some CANoe plugin object graphs are only safely preserved by CANoe itself.",
            "External Vector/CANoe validation is tracked separately by evaluate_canoe_config."
        ],
        "retry_count": retry_count,
    }
    from . import vector_canoe_adapter

    automation_plan_file = _write_json(cfg_plan_path, plan)

    validation_mode = _canoe_validation_mode(state, project_config)
    com_availability = vector_canoe_adapter.is_available()
    com_available = com_availability.get("available", False) if isinstance(com_availability, dict) else False

    cfg_generation_mode = validation_mode
    if cfg_generation_mode == "disabled" and com_available and cfg_source_path:
        cfg_generation_mode = "automated"

    cfg_automation = vector_canoe_adapter.prepare_cfg_generation(
        plan,
        Path(automation_plan_file),
        target_cfg_path,
        cfg_automation_script_path,
        mode=cfg_generation_mode,
    )
    plan["official_generation_path"]["automation_status"] = cfg_automation.get("status")
    plan["official_generation_path"]["availability"] = cfg_automation.get("availability")
    plan["official_generation_path"]["target_cfg"] = str(target_cfg_path)
    if not cfg_source_path and cfg_automation.get("status") == "generated":
        cfg_path = target_cfg_path
    layout_manifest = {
        "schema_version": "0.1.0",
        "project_name": plan["project_name"],
        "target_canoe_version": plan["target_canoe_version"],
        "directories": {
            "root": str(output_root),
            "capl": str(output_root),
            "reports": str(output_root / "reports"),
            "logs": str(output_root / "logs"),
        },
        "expected_artifacts": [
            str(cfg_path),
            str(cfg_plan_path),
            str(cfg_automation_script_path),
            str(output_root / f"{project.get('name', 'CANoe_AutoTest_Project')}_TestModule.can"),
            str(output_root / "test_report_plan.json"),
        ],
    }
    if cfg_source_path:
        _ensure_dir(cfg_path.parent)
        if cfg_automation.get("status") != "generated":
            shutil.copyfile(cfg_source_path, cfg_path)
        cfg_file = str(cfg_path)
        cfg_plan_file = _write_json(cfg_plan_path, plan)
    else:
        if cfg_automation.get("status") == "generated":
            cfg_file = str(cfg_path)
            cfg_plan_file = _write_json(cfg_plan_path, plan)
        else:
            cfg_file = _write_json(cfg_path, plan)
            cfg_plan_file = cfg_file
    layout_manifest_file = _write_json(layout_manifest_path, layout_manifest)
    result = {
        "canoe_config_plan": plan,
        "cfg_artifact": {
            "path": cfg_file,
            "plan": cfg_plan_file,
            "layout_manifest": layout_manifest_file,
            "kind": "canoe_cfg_file" if cfg_source_path else "canoe_cfg_generation_plan",
            "status": "generated",
            "generation_mode": (
                "canoe_com_automation"
                if cfg_automation.get("status") == "generated"
                else ("base_cfg_copy" if cfg_source_path else "canoe_com_automation_plan")
            ),
            "source_template": str(cfg_source_path) if cfg_source_path else "",
            "automation": cfg_automation,
        },
        "config_retry_count": retry_count,
        "cfg_automation": cfg_automation,
    }
    return result, state.update(**result)


@action(
    reads=["canoe_config_plan", "cfg_artifact", "project_config", "canoe_validation_mode"],
    writes=["config_eval_status", "config_eval_report"],
)
def evaluate_canoe_config(state: State) -> Tuple[Dict[str, Any], State]:
    plan = state.get("canoe_config_plan", {})
    project_config = state.get("project_config", {})
    validation_mode = _canoe_validation_mode(state, project_config)
    issues: List[Dict[str, str]] = []
    if not plan.get("channels"):
        issues.append({"severity": "error", "message": "CANoe config has no enabled communication channels"})
    for channel in plan.get("channels", []):
        if not _as_text(channel.get("CANoe通道名")):
            issues.append({"severity": "error", "message": "Channel misses CANoe channel name"})
    from . import vector_canoe_adapter

    external_validation = vector_canoe_adapter.validate_config(
        state.get("cfg_artifact", {}),
        mode=validation_mode,
        plan=state.get("canoe_config_plan", {}),
    )
    if external_validation["status"] == "failed":
        issues.append({"severity": "error", "message": external_validation["message"]})
    elif external_validation["status"] in {"skipped", "manual_required"}:
        issues.append({"severity": "info", "message": external_validation["message"]})
    status = "fail" if any(i["severity"] == "error" for i in issues) else "pass"
    report = {
        "schema_version": "0.1.0",
        "agent": "SubAgent4_Canoe工程评估专家",
        "status": status,
        "issues": issues,
        "cfg_artifact": state.get("cfg_artifact"),
        "external_validation": external_validation,
    }
    result = {
        "config_eval_status": status,
        "config_eval_report": report,
    }
    return result, state.update(**result)


def _capl_static_lint(path: Path, expected_cases: int) -> Dict[str, Any]:
    try:
        from . import capl_lexer_lint
        result = capl_lexer_lint.lint_capl_source(path, expected_cases)
        issues = []
        for item in result.get("issues", []):
            issues.append({
                "severity": item.get("severity", "warning"),
                "message": f"line {item.get('line', '?')}: {item.get('message', '')}",
            })
        return {
            "status": "fail" if any(i["severity"] == "error" for i in issues) else "pass",
            "issues": issues,
            "error_count": result.get("error_count", 0),
            "warning_count": result.get("warning_count", 0),
        }
    except Exception:
        text = path.read_text(encoding="utf-8", errors="replace")
        issues = []
        if "Generated for CANoe" not in text:
            issues.append({"severity": "error", "message": "missing generated CANoe version header"})
        if "variables" not in text:
            issues.append({"severity": "error", "message": "missing variables block"})
        if text.count("{") != text.count("}"):
            issues.append({"severity": "error", "message": "unbalanced braces"})
        testcase_count = len(re.findall(r"\btestcase\s+[A-Za-z_][A-Za-z0-9_]*\s*\(", text))
        if testcase_count != expected_cases:
            issues.append({
                "severity": "error",
                "message": f"testcase count mismatch: expected {expected_cases}, got {testcase_count}",
            })
        if "TODO_UNVERIFIED_API" in text:
            issues.append({"severity": "error", "message": "unverified API placeholder found"})
        if "output(" in text and re.search(r"\bmessage\s+[A-Za-z_][A-Za-z0-9_]*\s+[A-Za-z_][A-Za-z0-9_]*\s*;", text) is None:
            issues.append({"severity": "error", "message": "output() is used but no CAPL message variable is declared"})
        return {
            "status": "fail" if any(item["severity"] == "error" for item in issues) else "pass",
            "issues": issues,
        }


def _capl_coverage_summary(coverage_report: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "case_count": coverage_report.get("case_count", 0),
        "step_count": coverage_report.get("step_count", 0),
        "requirement_coverage": coverage_report.get("requirement_coverage", {}),
        "domain_coverage": coverage_report.get("domain_coverage", {}),
        "risk_count": len(coverage_report.get("risks", [])),
    }


def _capl_evidence_refs(evidence_bundle: Dict[str, Any]) -> List[Dict[str, Any]]:
    return [
        {
            "symbol": page.get("symbol"),
            "page_id": page.get("page_id"),
            "confidence": page.get("confidence"),
        }
        for page in evidence_bundle.get("pages", [])
    ]


def _capl_test_report_plan(structured: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "schema_version": "0.1.0",
        "format": structured.get("strategy", {}).get("测试报告格式", "HTML"),
        "cases": [
            {
                "case_id": case.get("case_id"),
                "requirement_id": case.get("requirement_id"),
                "requirement_ids": case.get("requirement_ids", []),
            }
            for case in structured.get("cases", [])
        ],
    }


def _capl_compile_max_attempts(state: State) -> int:
    explicit = _as_int(state.get("capl_compile_max_attempts"), 0)
    if explicit > 0:
        return explicit
    return max(1, _as_int(state.get("max_retries"), 4) + 1)


def _compile_error_log(compile_result: Dict[str, Any]) -> str:
    parts = [
        f"status: {compile_result.get('status', 'unknown')}",
        f"message: {compile_result.get('message', '')}",
    ]
    if compile_result.get("details"):
        parts.append("details: " + json.dumps(compile_result.get("details"), ensure_ascii=False, default=_json_default))
    if compile_result.get("stdout"):
        parts.append("stdout: " + _as_text(compile_result.get("stdout")))
    if compile_result.get("stderr"):
        parts.append("stderr: " + _as_text(compile_result.get("stderr")))
    return "\n".join(part for part in parts if part.strip())


def _write_capl_generation_outputs(
    output_root: Path,
    can_path: Path,
    report_path: Path,
    capl_source: str,
    plan: Dict[str, Any],
    structured: Dict[str, Any],
    renderer: str,
) -> Dict[str, Any]:
    _ensure_dir(can_path.parent)
    can_path.write_text(capl_source, encoding="utf-8")
    test_report_plan = _capl_test_report_plan(structured)
    _write_json(output_root / "capl_script_plan.json", plan)
    _write_json(report_path, test_report_plan)
    return {
        "capl_script_plan": plan,
        "can_artifact": {
            "path": str(can_path),
            "kind": "capl_test_module_source",
            "status": "generated",
            "renderer": renderer,
        },
        "test_report_plan": {
            "path": str(report_path),
            "kind": "test_report_plan",
            "status": "generated",
        },
    }


def _llm_capl_render(
    structured: Dict[str, Any],
    project_config: Dict[str, Any],
    canoe_config_plan: Dict[str, Any],
    evidence_bundle: Dict[str, Any],
    coverage_report: Dict[str, Any],
    profile: Dict[str, Any],
    output_root: Path,
    can_path: Path,
    report_path: Path,
    retry_count: int,
    coverage_report_file: str = "",
    validation_mode: str = "disabled",
    cfg_artifact: Optional[Dict[str, Any]] = None,
    max_compile_attempts: int = 1,
) -> Dict[str, Any]:
    from .agents import capl_authoring_agent
    from . import vector_canoe_adapter

    planner_payload = capl_authoring_agent.build_planner_payload(
        structured,
        project_config,
        canoe_config_plan,
        evidence_bundle,
        coverage_report,
        profile,
    )
    planner_result = capl_authoring_agent.call_planner(planner_payload, output_root)
    if planner_result.get("status") != "generated":
        return {"status": "failed", "agent_result": planner_result}

    golden_ir = planner_result.get("response", {}).get("golden_ir", {})
    current_code = ""
    compile_error_log = "Initial CAPL generation request. No previous compile error exists."
    attempts = []
    agent_result: Dict[str, Any] = {}
    response: Dict[str, Any] = {}
    capl_source = ""
    compile_result: Dict[str, Any] = {}

    error_hashes: List[str] = []
    for attempt in range(1, max(1, max_compile_attempts) + 1):
        error_hash = hashlib.md5(compile_error_log.encode("utf-8", errors="replace")).hexdigest()[:16]
        repeated_error_count = sum(1 for h in error_hashes if h == error_hash)
        error_hashes.append(error_hash)
        fixer_payload = capl_authoring_agent.build_fixer_payload(
            golden_ir,
            current_code,
            compile_error_log,
            attempt,
            repeated_error_count=repeated_error_count,
        )
        agent_result = capl_authoring_agent.call_fixer(fixer_payload, output_root)
        if agent_result.get("status") != "generated":
            return {
                "status": "failed",
                "agent_result": {
                    **agent_result,
                    "planner_result": {key: value for key, value in planner_result.items() if key != "response"},
                    "golden_ir": golden_ir,
                    "compile_loop_attempts": attempts,
                },
            }

        response = agent_result.get("response", {})
        capl_source = response.get("capl_source", "")
        current_code = capl_source
        _ensure_dir(can_path.parent)
        can_path.write_text(capl_source, encoding="utf-8")
        static_lint = _capl_static_lint(can_path, len(structured.get("cases", [])))
        if static_lint.get("status") != "pass":
            compile_result = {
                "status": "failed",
                "message": "CAPL authoring agent output failed static lint.",
                "details": static_lint,
            }
            attempts.append({
                "attempt": attempt,
                "status": compile_result["status"],
                "message": compile_result["message"],
                "source": "static_lint",
            })
            compile_error_log = _compile_error_log(compile_result)
            continue

        can_artifact = {
            "path": str(can_path),
            "kind": "capl_test_module_source",
            "status": "generated",
            "renderer": "llm_kb_indexed_authoring_agent",
        }
        compile_result = vector_canoe_adapter.compile_capl(
            can_artifact,
            mode=validation_mode,
            cfg_artifact=cfg_artifact,
            output_root=output_root,
            attempt=attempt,
        )
        attempts.append({
            "attempt": attempt,
            "status": compile_result.get("status"),
            "message": compile_result.get("message"),
            "source": "canoe_compile",
            "report_file": compile_result.get("report_file", ""),
        })
        if compile_result.get("status") == "pass":
            break
        if compile_result.get("status") in {"skipped", "manual_required", "unavailable"}:
            break
        compile_error_log = _compile_error_log(compile_result)

    if compile_result.get("status") not in {"pass", "skipped", "manual_required"}:
        return {
            "status": "failed",
            "agent_result": {
                **agent_result,
                "response": "<omitted>",
                "planner_result": {key: value for key, value in planner_result.items() if key != "response"},
                "golden_ir": golden_ir,
                "compile_loop_attempts": attempts,
                "compile_result": compile_result,
                "message": "CAPL authoring loop did not produce a compile-passing CAPL script.",
            },
        }

    response_plan = response.get("capl_script_plan", {})
    adapter_gaps = response_plan.get("adapter_gaps", [])
    plan = {
        "schema_version": "0.1.0",
        "agent": "KBIndexed_CAPLAuthoringAgent",
        "authoring_mode": "llm",
        "authoring_result": {key: value for key, value in agent_result.items() if key != "response"},
        "planner_result": {key: value for key, value in planner_result.items() if key != "response"},
        "golden_ir": golden_ir,
        "compile_loop": {
            "status": compile_result.get("status", "unknown"),
            "validation_mode": validation_mode,
            "max_attempts": max_compile_attempts,
            "attempt_count": len(attempts),
            "attempts": attempts,
            "latest_compile_result": compile_result,
        },
        "target_canoe_version": structured.get("project", {}).get("target_canoe_version", "v15"),
        "can_artifact": str(can_path),
        "evidence_status": evidence_bundle.get("status", "unknown"),
        "coverage_status": coverage_report.get("status", "unknown"),
        "coverage_report_file": coverage_report_file,
        "retrieval_profile": profile["id"],
        "retrieval_profile_file": profile["profile_path"],
        "topic_filters": profile.get("topic_filters", []),
        "blocked_topic_filters": profile.get("blocked_topic_filters", []),
        "renderer": "llm_kb_indexed_authoring_agent",
        "adapter_note_count": len(adapter_gaps),
        "adapter_notes": adapter_gaps,
        "assumptions": response_plan.get("assumptions", []),
        "used_evidence_refs": response_plan.get("used_evidence_refs", []),
        "coverage_summary": _capl_coverage_summary(coverage_report),
        "evidence_pages": _capl_evidence_refs(evidence_bundle),
        "cases": response_plan.get("cases", []),
        "retry_count": retry_count,
    }
    return {
        "status": "generated",
        **_write_capl_generation_outputs(
            output_root,
            can_path,
            report_path,
            capl_source,
            plan,
            structured,
            "llm_kb_indexed_authoring_agent",
        ),
    }


def _strict_llm_capl_failure(
    structured: Dict[str, Any],
    evidence_bundle: Dict[str, Any],
    coverage_report: Dict[str, Any],
    profile: Dict[str, Any],
    output_root: Path,
    can_path: Path,
    report_path: Path,
    retry_count: int,
    authoring_result: Dict[str, Any],
    coverage_report_file: str = "",
) -> Dict[str, Any]:
    project = structured.get("project", {})
    version = project.get("target_canoe_version", "v15")
    cases = structured.get("cases", [])
    lines = [
        "/*",
        f" * Generated for CANoe {version}.",
        " * CAPL LLM authoring failed in strict mode.",
        " * This is a placeholder skeleton — do not use in production.",
        "*/",
        "",
        "variables",
        "{",
        "}",
        "",
    ]
    placeholder_cases = []
    for case in cases:
        case_id = _as_text(case.get("case_id")) or "TC_UNKNOWN"
        func_name = re.sub(r"[^A-Za-z0-9_]", "_", case_id)
        lines.extend([
            f"testcase {func_name}()",
            "{",
            f"  /* Placeholder for {case_id} — LLM authoring unavailable */",
            "  TestCaseFail(\"CAPL LLM authoring unavailable; this testcase is a placeholder.\");",
            "}",
            "",
        ])
        placeholder_cases.append({
            "case_id": case_id,
            "steps": [{"step_no": 1, "note": "placeholder — LLM authoring unavailable"}],
            "authoring_status": "llm_failed",
        })
    capl_source = "\n".join(lines)
    plan = {
        "schema_version": "0.1.0",
        "agent": "KBIndexed_CAPLAuthoringAgent",
        "authoring_mode": "llm_failed",
        "authoring_result": authoring_result,
        "target_canoe_version": version,
        "can_artifact": str(can_path),
        "evidence_status": evidence_bundle.get("status", "unknown"),
        "coverage_status": coverage_report.get("status", "unknown"),
        "coverage_report_file": coverage_report_file,
        "retrieval_profile": profile["id"],
        "retrieval_profile_file": profile["profile_path"],
        "topic_filters": profile.get("topic_filters", []),
        "blocked_topic_filters": profile.get("blocked_topic_filters", []),
        "renderer": "llm_kb_indexed_authoring_agent",
        "adapter_note_count": 0,
        "adapter_notes": [],
        "coverage_summary": _capl_coverage_summary(coverage_report),
        "evidence_pages": _capl_evidence_refs(evidence_bundle),
        "cases": placeholder_cases,
        "retry_count": retry_count,
    }
    return _write_capl_generation_outputs(
        output_root,
        can_path,
        report_path,
        capl_source,
        plan,
        structured,
        "llm_kb_indexed_authoring_agent",
    )


@action(
    reads=["structured_test_case", "project_config", "canoe_config_plan", "cfg_artifact", "evidence_bundle", "coverage_report", "capl_retry_count", "capl_compile_max_attempts", "max_retries", "output_root", "canoe_validation_mode"],
    writes=["capl_script_plan", "can_artifact", "test_report_plan", "capl_retry_count"],
)
def generate_capl_script(state: State) -> Tuple[Dict[str, Any], State]:
    output_root = _state_output_root(state)
    structured = state.get("structured_test_case", {})
    project_config = state.get("project_config", {})
    evidence_bundle = state.get("evidence_bundle", {})
    coverage_report = state.get("coverage_report", {})
    canoe_config_plan = state.get("canoe_config_plan", {})
    validation_mode = _canoe_validation_mode(state, project_config)
    project = structured.get("project", {})
    retry_count = _as_int(state.get("capl_retry_count"), 0) + 1
    profile = _workflow_retrieval_profile("capl_authoring")
    can_path = output_root / f"{project.get('name', 'CANoe_AutoTest_Project')}_TestModule.can"
    report_path = output_root / "test_report_plan.json"

    llm_result = _llm_capl_render(
        structured,
        project_config,
        canoe_config_plan,
        evidence_bundle,
        coverage_report,
        profile,
        output_root,
        can_path,
        report_path,
        retry_count,
        state.get("coverage_report_file", ""),
        validation_mode=validation_mode,
        cfg_artifact=state.get("cfg_artifact", {}),
        max_compile_attempts=_capl_compile_max_attempts(state),
    )
    if llm_result.get("status") == "generated":
        result = {key: value for key, value in llm_result.items() if key != "status"}
        result["capl_retry_count"] = retry_count
        return result, state.update(**result)

    result = _strict_llm_capl_failure(
        structured,
        evidence_bundle,
        coverage_report,
        profile,
        output_root,
        can_path,
        report_path,
        retry_count,
        llm_result.get("agent_result", llm_result),
        state.get("coverage_report_file", ""),
    )
    result["capl_retry_count"] = retry_count
    return result, state.update(**result)


@action(
    reads=["capl_script_plan", "can_artifact", "structured_test_case", "project_config", "canoe_validation_mode", "cfg_artifact", "output_root", "quality_gate"],
    writes=["capl_eval_status", "capl_eval_report"],
)
def evaluate_capl_script(state: State) -> Tuple[Dict[str, Any], State]:
    plan = state.get("capl_script_plan", {})
    structured = state.get("structured_test_case", {})
    project_config = state.get("project_config", {})
    validation_mode = _canoe_validation_mode(state, project_config)
    quality_gate = _as_text(state.get("quality_gate")) or "exploration"
    issues: List[Dict[str, str]] = []
    authoring_mode = _as_text(plan.get("authoring_mode"))
    if authoring_mode == "llm_failed":
        issues.append({
            "severity": "error",
            "message": "CAPL LLM authoring did not produce a compilable test module — check capl_planner_diagnostics.json and capl_script_plan.json for details",
        })
        issues.append({"severity": "info", "message": "Placeholder CAPL skeleton was generated but is not usable for testing"})
        status = "fail"
        report = {
            "schema_version": "0.1.0",
            "agent": "SubAgent5_Canoe_CAPL脚本专家",
            "status": status,
            "issues": issues,
            "static_lint": {"status": "skipped", "issues": [], "reason": "llm_failed placeholder"},
            "external_compile": {"status": "skipped", "message": "Compilation skipped for llm_failed placeholder"},
            "can_artifact": state.get("can_artifact", {}),
        }
        result = {"capl_eval_status": status, "capl_eval_report": report}
        return result, state.update(**result)
    if not plan.get("cases"):
        issues.append({"severity": "error", "message": "CAPL plan has no test cases"})
    for case in plan.get("cases", []):
        if not case.get("steps"):
            issues.append({"severity": "error", "message": f"Case {case.get('case_id')} has no steps"})
    if quality_gate == "release":
        adapter_gaps = plan.get("adapter_notes", [])
        if adapter_gaps:
            issues.append({
                "severity": "error",
                "message": f"Release quality gate forbids CanoeGene_* adapter stubs: {len(adapter_gaps)} unbound adapter gap(s) remain",
            })
        can_artifact_check = state.get("can_artifact", {})
        can_path_check = Path(can_artifact_check.get("path", "")) if can_artifact_check.get("path") else None
        if can_path_check and can_path_check.exists():
            source_text = can_path_check.read_text(encoding="utf-8", errors="replace")
            if "CanoeGene_" in source_text:
                stub_funcs = sorted(set(re.findall(r"\bCanoeGene_[A-Za-z_][A-Za-z0-9_]*", source_text)))
                issues.append({
                    "severity": "error",
                    "message": f"Release quality gate forbids CanoeGene_* adapter stubs in CAPL source: {', '.join(stub_funcs)}",
                })
    can_artifact = state.get("can_artifact", {})
    can_path = Path(can_artifact.get("path", "")) if can_artifact.get("path") else None
    static_lint = {"status": "fail", "issues": [{"severity": "error", "message": "CAPL artifact path missing"}]}
    if can_path and can_path.exists():
        static_lint = _capl_static_lint(can_path, len(structured.get("cases", [])))
    issues.extend(static_lint["issues"])
    compile_loop = plan.get("compile_loop", {}) if isinstance(plan.get("compile_loop"), dict) else {}
    external_compile = compile_loop.get("latest_compile_result", {}) if isinstance(compile_loop.get("latest_compile_result"), dict) else {}
    if not external_compile:
        from . import vector_canoe_adapter

        external_compile = vector_canoe_adapter.compile_capl(
            can_artifact,
            mode=validation_mode,
            cfg_artifact=state.get("cfg_artifact", {}),
            output_root=_state_output_root(state),
        )
    if external_compile["status"] in {"failed", "unavailable"}:
        issues.append({"severity": "error", "message": external_compile["message"]})
    elif external_compile["status"] in {"skipped", "manual_required"}:
        issues.append({"severity": "info", "message": external_compile["message"]})
    status = "fail" if any(i["severity"] == "error" for i in issues) else "pass"
    report = {
        "schema_version": "0.1.0",
        "agent": "SubAgent5_Canoe_CAPL脚本专家",
        "status": status,
        "issues": issues,
        "static_lint": static_lint,
        "external_compile": external_compile,
        "can_artifact": can_artifact,
    }
    result = {
        "capl_eval_status": status,
        "capl_eval_report": report,
    }
    return result, state.update(**result)


def _report_issues(report: Dict[str, Any]) -> List[Dict[str, Any]]:
    return list(report.get("issues", [])) if isinstance(report, dict) else []


def _classify_external_failure(report: Dict[str, Any], key: str) -> Dict[str, Any]:
    """Classify an external validation/compile failure into a structured category.

    Replaces fragile string-matching with explicit failure categories:
    - env_missing: CANoe COM or tool not installed/registered
    - config_missing: command/env var not configured
    - timeout: compilation or validation timed out
    - code_error: syntax/compile/logic error in generated artifact
    - schema_violation: response failed schema validation
    - not_failed: status is not "failed" (actionable if retryable)
    - unknown: unclassified failure
    """
    external = report.get(key, {}) if isinstance(report, dict) else {}
    status = _as_text(external.get("status"))
    message = _as_text(external.get("message")).lower()
    issues = external.get("issues") or []
    issue_messages = " ".join(
        _as_text(i.get("message", "")).lower()
        for i in (issues if isinstance(issues, list) else [])
        if isinstance(i, dict)
    )
    all_report_issues = report.get("issues") or []
    all_issue_text = " ".join(
        _as_text(i.get("message", "")).lower()
        for i in (all_report_issues if isinstance(all_report_issues, list) else [])
        if isinstance(i, dict)
    )
    combined_text = f"{message} {issue_messages} {all_issue_text}"
    if status != "failed":
        if "unavailable" in combined_text or "not configured" in combined_text or "is not configured" in combined_text:
            return {"actionable_by_retry": False, "category": "config_missing"}
        return {"actionable_by_retry": True, "category": "not_failed"}
    if "unavailable" in combined_text or "not registered" in combined_text or "progid" in combined_text:
        return {"actionable_by_retry": False, "category": "env_missing"}
    if "not configured" in combined_text or "no command" in combined_text or "is not configured" in combined_text:
        return {"actionable_by_retry": False, "category": "config_missing"}
    if "timeout" in combined_text or "timed out" in combined_text:
        return {"actionable_by_retry": True, "category": "timeout"}
    if "schema validation" in combined_text or (isinstance(issues, list) and issues):
        return {"actionable_by_retry": True, "category": "schema_violation"}
    if "syntax" in combined_text or "compile" in combined_text or "error" in combined_text or "failed" in combined_text:
        return {"actionable_by_retry": True, "category": "code_error"}
    return {"actionable_by_retry": True, "category": "unknown"}


@action(
    reads=[
        "template_contract_status",
        "template_contract_report",
        "test_case_check_status",
        "correction_items",
        "evidence_gate_status",
        "evidence_gate_report",
        "config_eval_status",
        "config_eval_report",
        "capl_eval_status",
        "capl_eval_report",
        "config_retry_count",
        "capl_retry_count",
        "max_retries",
        "output_root",
    ],
    writes=["repair_plan", "repair_plan_file", "repair_next_action"],
)
def plan_repair(state: State) -> Tuple[Dict[str, Any], State]:
    output_root = _state_output_root(state)
    max_retries = _as_int(state.get("max_retries"), 2)
    config_retry_count = _as_int(state.get("config_retry_count"), 0)
    capl_retry_count = _as_int(state.get("capl_retry_count"), 0)
    repair_items: List[Dict[str, Any]] = []
    origin = "manual_review"
    next_action = "emit_test_case_corrections"
    failure_category = "none"

    if state.get("template_contract_status") == "fail":
        origin = "template_contract"
        repair_items.extend(_report_issues(state.get("template_contract_report", {})))
        next_action = "emit_test_case_corrections"
    elif state.get("test_case_check_status") == "fail":
        origin = "test_case_validation"
        repair_items.extend(state.get("correction_items", []))
        next_action = "emit_test_case_corrections"
    elif state.get("evidence_gate_status") == "fail":
        origin = "evidence_gate"
        repair_items.extend(_report_issues(state.get("evidence_gate_report", {})))
        next_action = "emit_test_case_corrections"
    elif state.get("config_eval_status") == "fail":
        origin = "canoe_config_evaluation"
        report = state.get("config_eval_report", {})
        repair_items.extend(_report_issues(report))
        failure_info = _classify_external_failure(report, "external_validation")
        failure_category = failure_info["category"]
        if config_retry_count < max_retries and failure_info["actionable_by_retry"]:
            next_action = "generate_canoe_config"
        else:
            next_action = "emit_test_case_corrections"
    elif state.get("capl_eval_status") == "fail":
        origin = "capl_evaluation"
        report = state.get("capl_eval_report", {})
        repair_items.extend(_report_issues(report))
        capl_plan = state.get("capl_script_plan", {}) if isinstance(state.get("capl_script_plan"), dict) else {}
        authoring_mode = _as_text(capl_plan.get("authoring_mode"))
        if authoring_mode == "llm_failed":
            failure_info = {"actionable_by_retry": False, "category": "llm_authoring_failed"}
        else:
            failure_info = _classify_external_failure(report, "external_compile")
        failure_category = failure_info["category"]
        if capl_retry_count < max_retries and failure_info["actionable_by_retry"]:
            next_action = "generate_capl_script"
        else:
            next_action = "emit_test_case_corrections"

    categories = defaultdict(int)
    for item in repair_items:
        categories[_as_text(item.get("category")) or _as_text(item.get("severity")) or "issue"] += 1
    plan = {
        "schema_version": "0.1.0",
        "status": "needs_repair",
        "origin": origin,
        "failure_category": failure_category,
        "next_action": next_action,
        "retry_budget": {
            "max_retries": max_retries,
            "config_retry_count": config_retry_count,
            "capl_retry_count": capl_retry_count,
        },
        "issue_summary": dict(sorted(categories.items())),
        "repair_items": repair_items,
        "recommended_actions": [
            "Fix Excel template fields or source file paths for template/test-case validation issues.",
            "Add or correct KB symbol aliases/pages for evidence gate failures.",
            "Provide a base CANoe CFG template or enable a real Vector automation hook for CFG validation.",
            "Provide project-specific XCP/diagnostic adapter bindings before treating adapter stubs as release CAPL.",
        ],
    }
    repair_plan_file = _write_json(output_root / "repair_plan.json", plan)
    result = {
        "repair_plan": plan,
        "repair_plan_file": repair_plan_file,
        "repair_next_action": next_action,
    }
    return result, state.update(**result)


def _mount_capl_into_cfg(state: State, output_root: Path) -> Optional[Dict[str, Any]]:
    """Re-generate the CFG with the CAPL test module mounted, if possible.

    Called from package_outputs after CAPL generation is complete. If CANoe COM
    is available and the CAPL file exists, this opens the base cfg (or the
    already-generated cfg), adds the CAPL file as a UserFile, and SaveAs the
    target cfg. This ensures the final .cfg contains the CAPL test module.
    """
    can_artifact = state.get("can_artifact", {})
    capl_path = can_artifact.get("path", "")
    if not capl_path or not Path(capl_path).exists():
        return None
    canoe_config_plan = state.get("canoe_config_plan", {})
    if not canoe_config_plan:
        return None
    cfg_artifact = state.get("cfg_artifact", {})
    cfg_path = cfg_artifact.get("path", "")
    if not cfg_path:
        return None
    try:
        from . import vector_canoe_adapter
        availability = vector_canoe_adapter.is_available()
        if not availability.get("available"):
            return {"status": "skipped", "reason": "CANoe COM not available"}
        canoe_config_plan = dict(canoe_config_plan)
        canoe_config_plan["test_modules"] = [
            {
                "name": Path(capl_path).stem,
                "source": str(Path(capl_path).resolve()),
                "mount_strategy": "add as CAPL test module",
            }
        ]
        script_path = output_root / "mount_capl_into_cfg.ps1"
        plan_file = output_root / "mount_capl_plan.json"
        _write_json(plan_file, canoe_config_plan)
        result = vector_canoe_adapter.prepare_cfg_generation(
            canoe_config_plan,
            plan_file,
            Path(cfg_path),
            script_path,
            mode="automated",
        )
        return result
    except Exception as exc:
        return {"status": "failed", "reason": str(exc)}


@action(
    reads=[
        "structured_test_case_file",
        "test_case_correction_file",
        "template_contract_report_file",
        "source_model_file",
        "evidence_bundle_file",
        "coverage_report_file",
        "evidence_gate_report_file",
        "cfg_artifact",
        "can_artifact",
        "test_report_plan",
        "config_eval_report",
        "capl_eval_report",
        "repair_plan_file",
        "run_id",
        "base_output_root",
        "output_root",
        "canoe_config_plan",
        "project_config",
    ],
    writes=["final_outputs"],
)
def package_outputs(state: State) -> Tuple[Dict[str, Any], State]:
    output_root = _state_output_root(state)
    base_output_root = Path(state.get("base_output_root") or output_root)
    final_outputs = {
        "status": "complete",
        "run_id": state.get("run_id"),
        "output_root": str(output_root),
        "structured_test_case_file": state.get("structured_test_case_file"),
        "correction_file": state.get("test_case_correction_file"),
        "template_contract_report_file": state.get("template_contract_report_file"),
        "source_model_file": state.get("source_model_file"),
        "evidence_bundle_file": state.get("evidence_bundle_file"),
        "coverage_report_file": state.get("coverage_report_file"),
        "evidence_gate_report_file": state.get("evidence_gate_report_file"),
        "cfg_artifact": state.get("cfg_artifact"),
        "can_artifact": state.get("can_artifact"),
        "test_report_plan": state.get("test_report_plan"),
        "config_eval_report": state.get("config_eval_report"),
        "capl_eval_report": state.get("capl_eval_report"),
        "repair_plan": state.get("repair_plan_file"),
    }
    capl_mount_info = _mount_capl_into_cfg(state, output_root)
    if capl_mount_info:
        final_outputs["capl_mount"] = capl_mount_info
    try:
        from . import html_report
        html_path = output_root / "run_report.html"
        state_for_report = {
            "run_id": state.get("run_id"),
            "status": "complete",
            "structured_test_case": state.get("structured_test_case", {}),
            "correction_items": state.get("correction_items", []),
            "evidence_bundle": state.get("evidence_bundle", {}),
            "coverage_report": state.get("coverage_report", {}),
            "cfg_artifact": state.get("cfg_artifact", {}),
            "can_artifact": state.get("can_artifact", {}),
            "config_eval_report": state.get("config_eval_report", {}),
            "capl_eval_report": state.get("capl_eval_report", {}),
            "repair_plan": state.get("repair_plan", {}),
            "output_root": str(output_root),
        }
        html_report.generate_run_report(state_for_report, html_path)
        final_outputs["html_report"] = str(html_path)
        final_outputs["quick_summary"] = html_report.generate_quick_summary(state_for_report)
    except Exception:
        pass
    try:
        from . import run_retention
        retention_info = run_retention.apply_retention(base_output_root)
        final_outputs["run_retention"] = retention_info
    except Exception:
        pass
    manifest_path = _write_json(output_root / "final_package_manifest.json", final_outputs)
    final_outputs["manifest"] = manifest_path
    if base_output_root != output_root:
        _write_json(base_output_root / "latest_run_manifest.json", {
            "run_id": state.get("run_id"),
            "output_root": str(output_root),
            "manifest": manifest_path,
        })
    result = {"final_outputs": final_outputs}
    return result, state.update(**result)


ACTION_REGISTRY = {
    "load_test_case_template": load_test_case_template,
    "validate_template_contract": validate_template_contract,
    "parse_source_files": parse_source_files,
    "validate_test_cases": validate_test_cases,
    "retrieve_evidence": retrieve_evidence,
    "analyze_test_coverage": analyze_test_coverage,
    "validate_evidence_gate": validate_evidence_gate,
    "plan_repair": plan_repair,
    "emit_test_case_corrections": emit_test_case_corrections,
    "generate_canoe_config": generate_canoe_config,
    "evaluate_canoe_config": evaluate_canoe_config,
    "generate_capl_script": generate_capl_script,
    "evaluate_capl_script": evaluate_capl_script,
    "package_outputs": package_outputs,
}

TRANSITION_SPECS = [
    ("load_test_case_template", "validate_template_contract", None),
    ("validate_template_contract", "plan_repair", "template_contract_status == 'fail'"),
    ("validate_template_contract", "parse_source_files", "template_contract_status != 'fail'"),
    ("parse_source_files", "validate_test_cases", None),
    ("validate_test_cases", "plan_repair", "test_case_check_status == 'fail'"),
    ("validate_test_cases", "retrieve_evidence", "test_case_check_status != 'fail'"),
    ("retrieve_evidence", "analyze_test_coverage", None),
    ("analyze_test_coverage", "validate_evidence_gate", None),
    ("validate_evidence_gate", "plan_repair", "evidence_gate_status == 'fail'"),
    ("validate_evidence_gate", "generate_canoe_config", "evidence_gate_status != 'fail'"),
    ("generate_canoe_config", "evaluate_canoe_config", None),
    ("evaluate_canoe_config", "plan_repair", "config_eval_status == 'fail'"),
    ("evaluate_canoe_config", "generate_capl_script", "config_eval_status != 'fail'"),
    ("generate_capl_script", "evaluate_capl_script", None),
    ("evaluate_capl_script", "plan_repair", "capl_eval_status == 'fail'"),
    ("evaluate_capl_script", "package_outputs", "capl_eval_status != 'fail'"),
    ("plan_repair", "generate_canoe_config", "repair_next_action == 'generate_canoe_config'"),
    ("plan_repair", "generate_capl_script", "repair_next_action == 'generate_capl_script'"),
    ("plan_repair", "emit_test_case_corrections", "repair_next_action == 'emit_test_case_corrections'"),
]


def _burr_transitions() -> List[Tuple[Any, ...]]:
    profile_path = WORKFLOW_DIR / "workflow_profile.json"
    if profile_path.exists():
        try:
            profile = json.loads(profile_path.read_text(encoding="utf-8"))
            transitions: List[Tuple[Any, ...]] = []
            for entry in profile.get("transitions", []):
                source = entry[0]
                target = entry[1]
                condition = entry[2] if len(entry) > 2 else None
                transitions.append((source, target, default if condition is None else expr(condition)))
            if transitions:
                return transitions
        except Exception:
            pass
    transitions = []
    for source, target, condition in TRANSITION_SPECS:
        transitions.append((source, target, default if condition is None else expr(condition)))
    return transitions


def build_application(
    initial_state: Optional[Dict[str, Any]] = None,
    app_id: Optional[str] = None,
    enable_tracking: bool = False,
    tracking_project: str = DEFAULT_TRACKING_PROJECT,
):
    initial = {
        "test_case_excel_path": str(DEFAULT_TEMPLATE),
        "output_root": str(DEFAULT_OUTPUT),
        "base_output_root": str(DEFAULT_OUTPUT),
        "run_id": "",
        "input_sha256": "",
        "requirements_path": "",
        "dbc_paths": [],
        "a2l_paths": [],
        "cdd_paths": [],
        "strict_source_validation": False,
        "canoe_validation_mode": "disabled",
        "capl_authoring_mode": "llm",
        "capl_compile_max_attempts": 5,
        "max_retries": 2,
        "config_retry_count": 0,
        "capl_retry_count": 0,
        "quality_gate": "exploration",
    }
    if initial_state:
        initial.update(initial_state)
    builder = (
        ApplicationBuilder()
        .with_actions(**ACTION_REGISTRY)
        .with_transitions(*_burr_transitions())
        .with_state(**initial)
        .with_entrypoint("load_test_case_template")
    )
    if app_id:
        builder = builder.with_identifiers(app_id=app_id)
    if enable_tracking:
        builder = builder.with_tracker("local", project=tracking_project)
    return builder.build()


def run_workflow(
    excel: Path,
    out: Path,
    max_retries: int = 2,
    run_id: Optional[str] = None,
    enable_tracking: bool = False,
    canoe_validation_mode: str = "disabled",
    capl_authoring_mode: str = "llm",
    capl_compile_max_attempts: int = 5,
    strict_source_validation: bool = False,
    quality_gate: str = "exploration",
) -> Dict[str, Any]:
    run_id = run_id or _make_run_id(excel)
    base_output_root = out
    run_output_root = base_output_root / "runs" / run_id
    input_hash = _file_sha256(excel) if excel.exists() else ""
    app = build_application({
        "test_case_excel_path": str(excel),
        "base_output_root": str(base_output_root),
        "output_root": str(run_output_root),
        "run_id": run_id,
        "input_sha256": input_hash,
        "max_retries": max_retries,
        "canoe_validation_mode": canoe_validation_mode,
        "capl_authoring_mode": capl_authoring_mode,
        "capl_compile_max_attempts": capl_compile_max_attempts,
        "strict_source_validation": strict_source_validation,
        "quality_gate": quality_gate,
    }, app_id=run_id, enable_tracking=enable_tracking)
    action, result, state = app.run(halt_after=["package_outputs", "emit_test_case_corrections"])
    return {
        "halted_at": action.name if hasattr(action, "name") else str(action),
        "result": result,
        "state": dict(state),
    }


def main(argv: Optional[List[str]] = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description="Run the CANoe Burr workflow scaffold.")
    parser.add_argument("--excel", default=str(DEFAULT_TEMPLATE), help="Path to the Excel test case template.")
    parser.add_argument("--out", default=str(DEFAULT_OUTPUT), help="Output directory.")
    parser.add_argument("--max-retries", type=int, default=2)
    parser.add_argument("--run-id", default="", help="Optional run id. Defaults to timestamp plus input hash.")
    parser.add_argument("--tracking", action="store_true", help="Enable Burr local tracking.")
    parser.add_argument(
        "--canoe-validation-mode",
        choices=["disabled", "manual", "automated"],
        default="disabled",
        help="Controls Vector/CANoe external validation adapter behavior.",
    )
    parser.add_argument(
        "--capl-authoring-mode",
        choices=["llm"],
        default="llm",
        help="Controls CAPL generation. CAPL is generated only by the external LLM agent.",
    )
    parser.add_argument(
        "--capl-compile-max-attempts",
        type=int,
        default=5,
        help="Maximum Planner/Fixer CAPL compile-repair attempts inside generate_capl_script.",
    )
    parser.add_argument(
        "--strict-source-validation",
        action="store_true",
        help="Treat missing/unresolved DBC/A2L/CDD semantic checks as errors.",
    )
    parser.add_argument(
        "--quality-gate",
        choices=["exploration", "ci", "release"],
        default="exploration",
        help="Quality gate strictness. release mode forbids CanoeGene_* adapter stubs.",
    )
    parser.add_argument("--json", action="store_true", help="Print full JSON result.")
    args = parser.parse_args(argv)

    result = run_workflow(
        Path(args.excel),
        Path(args.out),
        args.max_retries,
        run_id=args.run_id or None,
        enable_tracking=args.tracking,
        canoe_validation_mode=args.canoe_validation_mode,
        capl_authoring_mode=args.capl_authoring_mode,
        capl_compile_max_attempts=args.capl_compile_max_attempts,
        strict_source_validation=args.strict_source_validation,
        quality_gate=args.quality_gate,
    )
    final_outputs = result["state"].get("final_outputs", {})
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2, default=_json_default))
    else:
        print(f"halted_at={result['halted_at']}")
        print(json.dumps(final_outputs, ensure_ascii=False, indent=2, default=_json_default))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
