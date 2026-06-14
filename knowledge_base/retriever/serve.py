"""CLI / API for interactive retrieval.

Usage:
    python -m retriever.serve                      # interactive REPL
    python -m retriever.serve --query "setSignal"  # one-shot
    python -m retriever.serve --serve              # start a tiny HTTP API
"""

from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
from typing import List, Dict, Any

from .config import ARTIFACTS_DIR, KNOWLEDGE_DIR, KNOWN_VERSIONS
from .retriever import HybridRetriever


def _format_hit(d: Dict[str, Any], i: int) -> str:
    g = d.get("grounded_facts", {})
    src = g.get("source", d.get("id", "?"))
    name = g.get("name", "")
    pt = d.get("page_type", d.get("meta", {}).get("page_type", ""))
    score = d.get("rerank_score", d.get("rrf_score",
              d.get("vector_score", d.get("bm25_score", 0))))
    desc = (g.get("description") or "").replace("\n", " ")[:120]
    meta = d.get("_meta", {})
    return (f"[{i}] {src}\n"
            f"     {name}  ({pt})  score={score:.4f}  "
            f"{meta.get('route','?'):7s}  {meta.get('total_ms',0):.1f}ms\n"
            f"     {desc}...")


def run_query(retr: HybridRetriever, q: str, version: str,
              topic: str | None, top_n: int) -> List[Dict[str, Any]]:
    hits = retr.retrieve(q, version=version, topic=topic, top_n=top_n)
    print(f"\nQuery: {q!r}  (version={version}, topic={topic})")
    print(f"Route: {hits[0]['_meta']['route'] if hits else '-'}  "
          f"hits: {len(hits)}")
    for i, h in enumerate(hits, 1):
        print(_format_hit(h, i))
    return hits


def repl(retr: HybridRetriever, version: str, topic: str | None, top_n: int):
    print("Agent-first retriever REPL  (Ctrl-C to exit, empty line to skip)")
    print(f"Default: version={version}, topic={topic or '*'}, top_n={top_n}")
    while True:
        try:
            q = input("\nQ> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not q:
            continue
        if q.startswith(":"):
            # command
            if q == ":info":
                print(json.dumps(retr.info(), indent=2))
            continue
        run_query(retr, q, version, topic, top_n)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--query",  default=None)
    ap.add_argument("--version", default="v15", choices=list(KNOWN_VERSIONS))
    ap.add_argument("--topic",  default=None)
    ap.add_argument("--top-n",  type=int, default=8)
    ap.add_argument("--art",    default=str(ARTIFACTS_DIR))
    ap.add_argument("--kb",     default=str(KNOWLEDGE_DIR))
    ap.add_argument("--serve",  action="store_true",
                    help="Start a tiny HTTP server on --port")
    ap.add_argument("--port",   type=int, default=8765)
    args = ap.parse_args()

    retr = HybridRetriever.build_from_disk(
        knowledge_dir=Path(args.kb), artifacts_dir=Path(args.art))
    print("Info:", json.dumps(retr.info(), indent=2))

    if args.serve:
        from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
        from urllib.parse import urlparse, parse_qs

        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                u = urlparse(self.path)
                if u.path != "/search":
                    self.send_error(404); return
                qs = parse_qs(u.query)
                q       = qs.get("q", [""])[0]
                ver     = qs.get("version", [args.version])[0]
                topic   = qs.get("topic",   [None])[0]
                top_n   = int(qs.get("top_n", [args.top_n])[0])
                hits = retr.retrieve(q, version=ver, topic=topic, top_n=top_n)
                body = json.dumps(hits, ensure_ascii=False, indent=2).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
            def log_message(self, *_): pass

        srv = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
        print(f"Serving on http://127.0.0.1:{args.port}/search?q=...")
        try:
            srv.serve_forever()
        except KeyboardInterrupt:
            srv.shutdown()
        return

    if args.query:
        run_query(retr, args.query, args.version, args.topic, args.top_n)
    else:
        repl(retr, args.version, args.topic, args.top_n)


if __name__ == "__main__":
    main()
