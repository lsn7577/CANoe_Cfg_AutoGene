"""Incremental ingestion: add new documents to the agent-first BM25 index.

Usage:
    python -m retriever.ingest path/to/new_doc.json
    python -m retriever.ingest path/to/folder
    python -m retriever.ingest --remove <doc_id>

Each new file should be either:
  * a JSON file matching the existing schema (page_type, name, ...), or
  * a directory laid out as <root>/<topic>/<file>.json (extras layout)
"""

from __future__ import annotations
import argparse
import json
from pathlib import Path
from typing import List, Dict, Any

from .config import ARTIFACTS_DIR, KNOWLEDGE_DIR, EXTRAS_DIR, KNOWN_TOPICS
from .preprocess import iter_documents
from .bm25_index import BM25Index
def _existing_doc_ids(bm25: BM25Index) -> set:
    ids = {d["id"] for d in (bm25.docs if bm25 else [])}
    return ids


def ingest_files(paths: List[Path], artifacts_dir: Path = ARTIFACTS_DIR,
                 knowledge_dir: Path = KNOWLEDGE_DIR,
                 extras_dir: Path = EXTRAS_DIR) -> Dict[str, int]:
    """Drop the given JSON files into extras/ (in original location) and
    add them to the BM25 index. If a file is *inside* knowledge/ already,
    just re-index it (idempotent: skip if id already present)."""
    paths = [Path(p) for p in paths]
    # Decide where each file "lives" semantically
    external_paths = [p for p in paths if not str(p).startswith(str(knowledge_dir))]

    # Stage external files into extras/ preserving their relative layout
    for p in external_paths:
        rel = p.name  # default: just copy flat
        # If user passed a path that already looks like <topic>/<file>.json
        parts = p.parts
        if len(parts) >= 2 and parts[-2] in KNOWN_TOPICS:
            rel = str(Path(parts[-2]) / p.name)
        target = extras_dir / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists():
            target.write_bytes(p.read_bytes())

    # Collect candidate docs
    bm25_path   = artifacts_dir / "bm25.pkl"
    bm25 = BM25Index.load(bm25_path) if bm25_path.exists() else BM25Index([])
    seen = _existing_doc_ids(bm25)
    roots = [knowledge_dir, extras_dir] if extras_dir.exists() else [knowledge_dir]
    new_docs: List[Dict[str, Any]] = []
    for d in iter_documents(roots):
        if d["id"] in seen:
            continue
        new_docs.append(d)
    if not new_docs:
        return {"added": 0, "skipped": 0}

    # BM25 add
    bm25.add(new_docs)
    bm25.save(bm25_path)

    return {"added": len(new_docs), "skipped": 0}


def remove_doc(doc_id: str, artifacts_dir: Path = ARTIFACTS_DIR) -> int:
    bm25_path = artifacts_dir / "bm25.pkl"
    bm25 = BM25Index.load(bm25_path) if bm25_path.exists() else None
    n1 = bm25.remove(doc_id) if bm25 else 0
    if bm25:
        bm25.save(bm25_path)
    return n1


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*", help="Files or directories to ingest")
    ap.add_argument("--remove", help="Doc id to remove from indices")
    ap.add_argument("--art", default=str(ARTIFACTS_DIR))
    ap.add_argument("--kb",  default=str(KNOWLEDGE_DIR))
    ap.add_argument("--extras", default=str(EXTRAS_DIR))
    args = ap.parse_args()
    if args.remove:
        n = remove_doc(args.remove, Path(args.art))
        print(f"removed: {n}")
    else:
        result = ingest_files(args.paths, Path(args.art),
                              Path(args.kb), Path(args.extras))
        print(json.dumps(result, indent=2))
