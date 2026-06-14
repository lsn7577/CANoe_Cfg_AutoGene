"""Add new knowledge to the base.

Three sub-commands:

  1) add <files...>          Stage files into extras/ and index them
  2) add-dir <dir>           Walk a directory and ingest every *.json
  3) schema                  Print the schema spec for new documents

Examples:
    python -m retriever.add_knowledge schema
    python -m retriever.add_knowledge add ./my_team_doc.json
    python -m retriever.add_knowledge add-dir ./internal_docs/
"""

from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

from .ingest import ingest_files, remove_doc
from .config import EXTRAS_DIR, ARTIFACTS_DIR, ROOT


SCHEMA = {
    "function": {
        "required": ["page_type", "name", "syntax"],
        "optional": ["description", "parameters", "return",
                     "example", "availability", "selectors", "note"],
        "example": {
            "page_type": "function",
            "name": "myFunction",
            "syntax": ["int myFunction(int a, char* s);"],
            "description": ["What it does, in one or two short paragraphs."],
            "parameters": [{"name": "a", "type": "int",
                            "description": "first param"}],
            "return": ["int: 0 on success"],
            "example": {"description": ["Use case."],
                        "code": "myFunction(1, \"x\");"},
            "availability": [["Since CANoe 12.0"]],
        },
    },
    "method": {
        "required": ["page_type", "name", "syntax"],
        "optional": ["description", "parameters", "return", "example"],
        "example": {
            "page_type": "method",
            "name": "msg.id",
            "syntax": ["long msg.id;"],
            "description": ["Returns the CAN id of a message."],
        },
    },
    "event": {
        "required": ["page_type", "name", "syntax"],
        "optional": ["description", "parameters"],
        "example": {
            "page_type": "event",
            "name": "on message MsgName",
            "syntax": ["on message <MsgName> { ... }"],
            "description": ["Called when MsgName is received."],
        },
    },
    "selector": {
        "required": ["page_type", "name", "syntax"],
        "optional": ["description"],
    },
    "concept": {
        "required": ["page_type", "name", "description"],
        "optional": ["example"],
    },
}


def cmd_schema():
    print(json.dumps(SCHEMA, indent=2, ensure_ascii=False))
    print("\n# File layout for new documents\n")
    print("Place your JSON in one of these locations:")
    extras = EXTRAS_DIR.relative_to(ROOT)
    print(f"  {extras}/<topic>/<name>.json")
    print(f"  {extras}/<topic>/<sub>/<name>.json  (nested)")
    print()
    print("'topic' can be any of: capl, panel, dbc, xcp, or your own (will be tagged 'extras').")
    print("Run `python -m retriever.add_knowledge add <file>` to ingest.")


def cmd_add(paths):
    n = ingest_files([Path(p) for p in paths])
    print(json.dumps(n, indent=2))


def cmd_add_dir(directory):
    directory = Path(directory)
    if not directory.exists():
        print(f"Not found: {directory}", file=sys.stderr); sys.exit(1)
    paths = [p for p in directory.rglob("*.json") if not p.name.startswith("_")]
    n = ingest_files(paths)
    print(json.dumps({"discovered": len(paths), **n}, indent=2))


def cmd_remove(doc_id):
    n = remove_doc(doc_id)
    print(json.dumps({"removed": n}, indent=2))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("schema", help="Print JSON schema for new docs")
    p_add = sub.add_parser("add", help="Ingest one or more JSON files")
    p_add.add_argument("paths", nargs="+")
    p_dir = sub.add_parser("add-dir", help="Ingest all *.json under a directory")
    p_dir.add_argument("directory")
    p_rm = sub.add_parser("remove", help="Remove a doc from both indices")
    p_rm.add_argument("doc_id")
    args = ap.parse_args()

    if args.cmd == "schema":
        cmd_schema()
    elif args.cmd == "add":
        cmd_add(args.paths)
    elif args.cmd == "add-dir":
        cmd_add_dir(args.directory)
    elif args.cmd == "remove":
        cmd_remove(args.doc_id)


if __name__ == "__main__":
    main()
