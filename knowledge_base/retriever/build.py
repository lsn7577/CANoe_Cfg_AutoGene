"""One-shot build script. Walks knowledge/ (+ extras/) and builds BM25.

Re-run safely: indices are rebuilt from scratch each time. For incremental
updates, use `ingest.py` instead. Vector embeddings are an optional enhancement
behind `--with-vector`; the default index is model-free and agent-first.
"""

from __future__ import annotations
import argparse
import json
import time
from pathlib import Path

from .config import ROOT, ARTIFACTS_DIR, KNOWLEDGE_DIR, EXTRAS_DIR, get_config
from .preprocess import iter_documents, all_default_roots, stats
from .bm25_index import BM25Index


def _display_path(path: Path) -> str:
    try:
        path = Path(path).resolve().relative_to(ROOT)
    except ValueError:
        path = Path(path)
    return path.as_posix()


def build(roots=None, artifacts_dir: Path = ARTIFACTS_DIR,
          force: bool = True, with_vector: bool = False,
          embedding_model: str | None = None) -> dict:
    cfg = get_config()
    if with_vector:
        cfg.embedding.enabled = True
        cfg.embedding.model_name = embedding_model or cfg.embedding.model_name or "BAAI/bge-m3"
    roots = roots or all_default_roots()
    arts = Path(artifacts_dir)
    arts.mkdir(parents=True, exist_ok=True)

    t0 = time.perf_counter()
    docs = list(iter_documents(roots))
    t1 = time.perf_counter()
    print(f"[build] discovered {len(docs)} documents in {t1 - t0:.1f}s")
    print(f"[build] stats: {stats(docs)}")

    # ---- BM25 ----
    bm25_path = arts / "bm25.pkl"
    if force and bm25_path.exists():
        bm25_path.unlink()
    bm25 = BM25Index(docs)
    bm25.save(bm25_path)
    t2 = time.perf_counter()
    print(f"[build] BM25 indexed {len(bm25.docs)} docs in {t2 - t1:.1f}s")

    # ---- Optional vector enhancement ----
    vector_info = {
        "embedding_model": None,
        "vector_enabled": False,
        "vector_requested": bool(with_vector),
        "vector_backend": "disabled",
        "vector_count": 0,
        "semantic_vector_available": False,
    }
    t3 = t2
    if with_vector:
        from .vector_index import VectorIndex

        vector = VectorIndex(
            persist_dir=str(arts / "chroma"),
            model_name=cfg.embedding.model_name,
            device=cfg.embedding.device,
        )
        print(f"[build] optional vector backend: {vector.backend()}")
        if not vector.semantic_available():
            if force and vector.count() > 0:
                vector.reset()
            vector_info.update({
                "embedding_model": cfg.embedding.model_name,
                "vector_backend": "unavailable",
            })
            print("[build] optional vector skipped: semantic model unavailable")
        else:
            if force and vector.count() > 0:
                # Drop & recreate for clean rebuild.
                vector.reset()
            n = vector.add(docs, batch=cfg.embedding.batch_size)
            vector_info.update({
                "embedding_model": cfg.embedding.model_name,
                "vector_enabled": True,
                "vector_backend": vector.backend(),
                "vector_count": vector.count(),
                "semantic_vector_available": vector.semantic_available(),
            })
            print(f"[build] optional vector indexed {n} docs")
        t3 = time.perf_counter()

    # ---- Manifest ----
    manifest = {
        "schema_version": "0.1.0",
        "built_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "roots": [_display_path(r) for r in roots],
        "n_docs": len(docs),
        "stats": stats(docs),
        **vector_info,
    }
    (arts / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    t4 = time.perf_counter()
    print(f"[build] DONE in {t4 - t0:.1f}s. Manifest at {_display_path(arts / 'manifest.json')}")
    return manifest


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--art",  default=str(ARTIFACTS_DIR))
    ap.add_argument("--kb",   default=str(KNOWLEDGE_DIR))
    ap.add_argument("--extras", default=str(EXTRAS_DIR))
    ap.add_argument("--no-force", action="store_true",
                    help="Append to existing indices instead of rebuilding")
    ap.add_argument("--with-vector", action="store_true",
                    help="Also build optional semantic vector index (requires local model or allowed download)")
    ap.add_argument("--embedding-model", default=None,
                    help="Embedding model to use with --with-vector")
    args = ap.parse_args()
    build(
        roots=[Path(args.kb), Path(args.extras)],
        artifacts_dir=Path(args.art),
        force=not args.no_force,
        with_vector=args.with_vector,
        embedding_model=args.embedding_model,
    )
