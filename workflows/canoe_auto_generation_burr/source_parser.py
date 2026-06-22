"""Enhanced source file parser module.

Provides parsers for DBC, A2L, CDD, and CFG files used in the CANoe workflow.
The DBC parser tries ``cantools`` first for rich structured data and falls back
to regex-based parsing when ``cantools`` is not installed.

All parsers return a dict with a ``"parser"`` field indicating which backend
was used (``"cantools"`` or ``"regex"`` or ``"xml_regex"``).
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple
from xml.etree import ElementTree as ET

# ---------------------------------------------------------------------------
# Optional dependency: cantools
# ---------------------------------------------------------------------------

try:
    import cantools  # type: ignore[import-untyped]

    _HAS_CANTOOLS = True
except Exception:  # pragma: no cover — depends on environment
    # Catch ImportError, AttributeError, and any other runtime issue
    # (e.g. cantools requires python-can which may be missing/ incompatible).
    _HAS_CANTOOLS = False


# ---------------------------------------------------------------------------
# Helpers (mirrored from canoe_workflow.py for standalone operation)
# ---------------------------------------------------------------------------


def _read_text_best_effort(path: Path) -> str:
    """Read *path* trying common encodings, falling back to lossy decode."""
    for encoding in ("utf-8-sig", "utf-8", "gb18030", "latin-1"):
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue
    return path.read_text(encoding="utf-8", errors="replace")


def _as_text(value: Any) -> str:
    """Convert *value* to a clean string, handling float-to-int edge cases."""
    if value is None:
        return ""
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value).strip()


# ---------------------------------------------------------------------------
# XML helpers (for CDD parsing)
# ---------------------------------------------------------------------------


def _parse_xml_attrs(attr_text: str) -> Dict[str, str]:
    """Extract attribute key-value pairs from an XML tag's attribute string."""
    return {
        key: value
        for key, _quote, value in re.findall(
            r"([A-Za-z_][A-Za-z0-9_.:-]*)\s*=\s*(['\"])(.*?)\2", attr_text,
        )
    }


def _xml_blocks(text: str, tag: str) -> Iterable[Tuple[Dict[str, str], str]]:
    """Yield ``(attributes, inner_text)`` for each ``<tag>…</tag>`` block."""
    pattern = rf"<{tag}\b([^>]*)>(.*?)</{tag}>"
    for match in re.finditer(pattern, text, flags=re.IGNORECASE | re.DOTALL):
        yield _parse_xml_attrs(match.group(1)), match.group(2)


def _xml_element_attrs(text: str, tag: str) -> Iterable[Dict[str, str]]:
    """Yield attribute dicts for both paired and self-closing ``<tag>`` elements."""
    yielded: Set[Tuple[Tuple[str, str], ...]] = set()
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
    """Extract trimmed text content of all ``<tag>`` children inside *block*."""
    return [
        re.sub(r"\s+", " ", value).strip()
        for value in re.findall(
            rf"<{tag}\b[^>]*>(.*?)</{tag}>", block, flags=re.IGNORECASE | re.DOTALL,
        )
        if re.sub(r"\s+", " ", value).strip()
    ]


def _normalize_cdd_name(value: str) -> str:
    """Normalise a CDD display name: strip hex prefixes and trailing qualifiers."""
    text = re.sub(r"\s+", " ", value).strip()
    text = re.sub(r"^\(\$[0-9A-Fa-f]+\)\s*", "", text)
    text = re.split(r"\s+-\s+|\s+\(", text, maxsplit=1)[0].strip()
    return text


def _cdd_sid_aliases(value: str) -> List[str]:
    """Generate decimal / hex / 0x / $ aliases for a SID value."""
    if not value:
        return []
    try:
        number = int(value, 10)
    except ValueError:
        return []
    hex_text = f"{number:X}"
    return [str(number), hex_text, f"0x{hex_text}", f"${hex_text}"]


def _cdd_name_aliases(*values: str) -> List[str]:
    """Build a sorted list of name aliases (raw + normalised)."""
    aliases: Set[str] = set()
    for value in values:
        text = _as_text(value)
        if not text:
            continue
        aliases.add(text)
        normalized = _normalize_cdd_name(text)
        if normalized:
            aliases.add(normalized)
    return sorted(aliases)


# ---------------------------------------------------------------------------
# DBC parsing
# ---------------------------------------------------------------------------


def _parse_dbc_regex(path: Path) -> Dict[str, Any]:
    """Parse a DBC file using regex (fallback when cantools is unavailable)."""
    text = _read_text_best_effort(path)
    messages: Dict[str, Dict[str, Any]] = {}
    current: Optional[Dict[str, Any]] = None
    for line in text.splitlines():
        msg_match = re.match(
            r"^\s*BO_\s+(\d+)\s+([A-Za-z_][A-Za-z0-9_]*)\s*:\s+(\d+)\s+(\S+)", line,
        )
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
        sig_match = re.match(
            r"^\s*SG_\s+([A-Za-z_][A-Za-z0-9_]*)\s+(?:[Mm]\s+)?(?::|m\d+\s*:)", line,
        )
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
        "parser": "regex",
    }


def _parse_dbc_cantools(path: Path) -> Dict[str, Any]:
    """Parse a DBC file using cantools for rich signal metadata."""
    db = cantools.database.load_file(str(path))
    messages: Dict[str, Dict[str, Any]] = {}
    signals: Dict[str, Dict[str, Any]] = {}

    for msg in db.messages:
        msg_entry: Dict[str, Any] = {
            "id": msg.frame_id,
            "name": msg.name,
            "dlc": msg.length,
            "transmitter": msg.senders[0] if msg.senders else "",
            "signals": {},
        }
        for sig in msg.signals:
            sig_entry: Dict[str, Any] = {
                "name": sig.name,
                "message": msg.name,
                "start_bit": sig.start,
                "length": sig.length,
                "byte_order": sig.byte_order,
                "factor": sig.scale,
                "offset": sig.offset,
                "minimum": sig.minimum,
                "maximum": sig.maximum,
                "unit": sig.unit or "",
            }
            # Add value table if available
            if sig.choices:
                sig_entry["value_table"] = {
                    str(k): v for k, v in sig.choices.items()
                }
            else:
                sig_entry["value_table"] = {}
            msg_entry["signals"][sig.name] = sig_entry
            signals[f"{msg.name}.{sig.name}"] = sig_entry
        messages[msg.name] = msg_entry

    return {
        "messages": messages,
        "signals": signals,
        "message_count": len(messages),
        "signal_count": len(signals),
        "parser": "cantools",
    }


def parse_dbc(path: Path) -> Dict[str, Any]:
    """Parse a DBC file.

    Tries ``cantools`` first for rich metadata (signal start bits, lengths,
    factors, offsets, value tables). Falls back to regex parsing if cantools
    is not installed or fails.

    Args:
        path: Path to the ``.dbc`` file.

    Returns:
        Dict with ``messages``, ``signals``, ``message_count``,
        ``signal_count``, and ``parser`` fields.
    """
    if _HAS_CANTOOLS:
        try:
            return _parse_dbc_cantools(path)
        except Exception:
            # Fall back to regex on any cantools error
            pass
    return _parse_dbc_regex(path)


# ---------------------------------------------------------------------------
# A2L parsing
# ---------------------------------------------------------------------------


def parse_a2l(path: Path) -> Dict[str, Any]:
    """Parse an A2L file using regex.

    Extracts CHARACTERISTIC and MEASUREMENT entries. Also attempts to parse
    conversion formulas (COMPU_METHOD) and access permissions if present.

    Args:
        path: Path to the ``.a2l`` file.

    Returns:
        Dict with ``characteristics``, ``measurements``, counts,
        ``compu_methods``, and ``parser`` fields.
    """
    text = _read_text_best_effort(path)
    characteristics = sorted(
        set(re.findall(r"/begin\s+CHARACTERISTIC\s+([^\s]+)", text, flags=re.IGNORECASE))
    )
    measurements = sorted(
        set(re.findall(r"/begin\s+MEASUREMENT\s+([^\s]+)", text, flags=re.IGNORECASE))
    )

    # Parse COMPU_METHOD entries (conversion formulas)
    compu_methods: List[Dict[str, Any]] = []
    compu_pattern = re.compile(
        r"/begin\s+COMPU_METHOD\s+(\S+)\s+\"([^\"]*)\"\s+(\S+)\s+\"([^\"]*)\"\s+\"([^\"]*)\"",
        re.IGNORECASE,
    )
    for match in compu_pattern.finditer(text):
        compu_methods.append({
            "name": match.group(1),
            "long_identifier": match.group(2),
            "conversion_type": match.group(3),
            "format": match.group(4),
            "unit": match.group(5),
        })

    # Parse access permissions if present
    access_permissions: Dict[str, List[str]] = {}
    for match in re.finditer(
        r"/begin\s+FRAME\s+(\S+).*?/end\s+FRAME", text, re.IGNORECASE | re.DOTALL,
    ):
        frame_name = match.group(1)
        perms = re.findall(r"ACCESS_PERM\s+(\S+)", match.group(0))
        if perms:
            access_permissions[frame_name] = perms

    return {
        "characteristics": characteristics,
        "measurements": measurements,
        "characteristic_count": len(characteristics),
        "measurement_count": len(measurements),
        "compu_methods": compu_methods,
        "compu_method_count": len(compu_methods),
        "access_permissions": access_permissions,
        "parser": "regex",
    }


# ---------------------------------------------------------------------------
# CDD parsing
# ---------------------------------------------------------------------------


def parse_cdd(path: Path) -> Dict[str, Any]:
    """Parse a CDD (Candela Diagnostic Description) file using XML/regex.

    Extracts protocol services, DID entries, aliases, and SID values.

    Args:
        path: Path to the ``.cdd`` file.

    Returns:
        Dict with ``services``, ``service_entries``, ``did_entries``,
        counts, and ``parser`` fields.
    """
    text = _read_text_best_effort(path)
    service_entries: List[Dict[str, Any]] = []
    service_aliases: Set[str] = set()

    for attrs, block in _xml_blocks(text, "PROTOCOLSERVICE"):
        names = _xml_texts(block, "TUV")
        quals = _xml_texts(block, "QUAL")
        req_block = next(
            (child for _child_attrs, child in _xml_blocks(block, "REQ")), "",
        )
        pos_block = next(
            (child for _child_attrs, child in _xml_blocks(block, "POS")), "",
        )
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
    did_aliases: Set[str] = set()
    for attrs, block in _xml_blocks(text, "DID"):
        did_number = attrs.get("n", "")
        names = _xml_texts(block, "TUV")
        quals = _xml_texts(block, "QUAL")
        aliases = set(_cdd_name_aliases(*(names + quals)))
        aliases.update(_cdd_sid_aliases(did_number))
        did_aliases.update(alias.lower() for alias in aliases)
        data_objects: List[Dict[str, Any]] = []
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

    legacy_names = set(
        re.findall(r"<SHORT-NAME>\s*([^<]+?)\s*</SHORT-NAME>", text, flags=re.IGNORECASE)
    )
    legacy_names.update(re.findall(r'\b(?:SERVICE|Service|service)\s*=\s*"([^"]+)"', text))
    legacy_names.update(
        re.findall(
            r'\b(?:qualifier|Qualifier|name|Name)\s*=\s*"([A-Za-z_][A-Za-z0-9_./:-]*)"',
            text,
        )
    )
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
        "parser": "xml_regex",
    }


# ---------------------------------------------------------------------------
# CFG parsing
# ---------------------------------------------------------------------------


def parse_cfg(path: Path) -> Dict[str, Any]:
    """Parse a CANoe configuration (.cfg) file using regex.

    Extracts the CANoe version header, version string, and file references
    (databases, CAPL files, etc.) referenced by the configuration.

    Args:
        path: Path to the ``.cfg`` file.

    Returns:
        Dict with ``header``, ``version``, ``file_references``,
        ``mounted_files``, ``reference_count``, ``line_count``,
        and ``parser`` fields.
    """
    text = _read_text_best_effort(path)
    header = next(
        (line.strip() for line in text.splitlines() if line.startswith(";CANoe Version")),
        "",
    )
    version = ""
    match = re.search(r"^Version:\s*(.+)$", text, flags=re.MULTILINE)
    if match:
        version = match.group(1).strip()
    references: List[Dict[str, Any]] = []
    quoted_paths = re.findall(
        r"<VFileName\b[^>]*>\s*\d*(?:\s+base=cfg)?\s+\"([^\"]*)\"", text,
    )
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
        "mounted_files": {
            key: sorted(set(values)) for key, values in mounted_files.items()
        },
        "reference_count": len(references),
        "line_count": text.count("\n") + 1,
        "parser": "regex",
    }


# ---------------------------------------------------------------------------
# Dispatch
# ---------------------------------------------------------------------------

_PARSERS = {
    "dbc": parse_dbc,
    "a2l": parse_a2l,
    "cdd": parse_cdd,
    "cfg": parse_cfg,
}


def parse_source(path: Path, kind: str) -> Dict[str, Any]:
    """Dispatch to the appropriate parser based on *kind*.

    Args:
        path: Path to the source file.
        kind: One of ``"dbc"``, ``"a2l"``, ``"cdd"``, ``"cfg"``.

    Returns:
        Parsed result dict on success, or ``{"status": "error", "message": ...}``
        on failure (file not found, unknown kind, or parse exception).
    """
    if kind not in _PARSERS:
        return {
            "status": "error",
            "message": f"Unknown source kind: '{kind}'. Supported: {', '.join(sorted(_PARSERS))}",
        }
    if not path.exists():
        return {
            "status": "error",
            "message": f"Source file not found: {path}",
        }
    try:
        return _PARSERS[kind](path)
    except Exception as exc:
        return {
            "status": "error",
            "message": f"Failed to parse {kind.upper()} file '{path}': {exc}",
        }


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------


if __name__ == "__main__":
    import argparse
    import json
    import sys

    parser = argparse.ArgumentParser(description="Parse CANoe source files (DBC, A2L, CDD, CFG).")
    parser.add_argument("path", type=str, help="Path to the source file.")
    parser.add_argument("--kind", type=str, required=True, choices=["dbc", "a2l", "cdd", "cfg"],
                        help="Type of source file.")
    args = parser.parse_args()

    result = parse_source(Path(args.path), args.kind)
    print(json.dumps(result, ensure_ascii=False, indent=2, default=str))
    sys.exit(0 if result.get("status") != "error" else 1)
