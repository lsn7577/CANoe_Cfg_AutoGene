"""End-to-end RAG demo + benchmark for Vector CANoe Knowledge Base (T10).

Usage:
    python scripts/rag_demo.py [--query Q] [--top-n 5] [--benchmark]

Without --query: runs a built-in benchmark suite.
Without --benchmark: runs a single demo query.
"""
import os, sys, json, time, argparse
from pathlib import Path
from typing import List, Dict

# Ensure repo root is on path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from retriever.retriever import HybridRetriever


DEMO_QUERIES = [
    {
        "q": "setSignal 函数用法",
        "expected_topic": "capl",
        "expected_version": "v15",
        "expected_name": "setSignal",
    },
    {
        "q": "CAN error frame selectors",
        "expected_topic": "capl",
        "expected_version": "v15",
        "expected_name": "ErrorFrame",  # partial match OK
    },
    {
        "q": "Panel Button 配置",
        "expected_topic": "panel",
        "expected_version": "v15",
        "expected_name": "Button",
    },
    {
        "q": "UDS 0x27 security access",
        "expected_topic": "diagnostics",
        "expected_version": "v15",
        "expected_name": "SecurityAccess",  # should hit UDS_Overview
    },
    {
        "q": "BusLoad 计算",
        "expected_topic": "capl",
        "expected_version": "v15",
        "expected_name": "BusLoad",
    },
    {
        "q": "Timer 在 measure 停止时行为",
        "expected_topic": "team",  # should hit Common_Gotchas
        "expected_version": "extras",
        "expected_name": "Gotchas",
    },
    {
        "q": "v12 parameters",
        "expected_topic": "capl",
        "expected_version": "v12",
        "expected_name": "setSignal",  # v12 setSignal
    },
]


def run_single_query(retr, query: str, version: str = None, top_n: int = 3) -> Dict:
    """Run a single query, return result with timing."""
    t0 = time.time()
    hits = retr.retrieve(query, version=version, top_n=top_n)
    elapsed = (time.time() - t0) * 1000  # ms
    return {"query": query, "version": version, "top_n": top_n,
            "elapsed_ms": round(elapsed, 1), "hits": hits, "hit_count": len(hits)}


def format_hit(hit: Dict, idx: int) -> str:
    g = hit.get("grounded_facts", {})
    src = g.get("source", "unknown")
    syntax = (g.get("syntax") or [""])[0][:60] if g.get("syntax") else ""
    desc = g.get("description", "")
    if isinstance(desc, list):
        desc = " ".join(desc)[:100]
    return f"  [{idx+1}] {src}\n      syntax: {syntax}\n      desc: {desc}..."


def run_demo(retr, query: str, version: str = None, top_n: int = 3):
    """Run a single demo query and pretty-print."""
    print("=" * 70)
    print(f"Query: {query!r}")
    if version:
        print(f"Version filter: {version}")
    print("=" * 70)
    result = run_single_query(retr, query, version, top_n)
    print(f"Latency: {result['elapsed_ms']} ms | Hits: {result['hit_count']}")
    for i, h in enumerate(result["hits"]):
        print(format_hit(h, i))
    print()


def run_benchmark(retr) -> Dict:
    """Run benchmark on DEMO_QUERIES, measure latency + recall@5."""
    print("=" * 70)
    print(f"BENCHMARK: {len(DEMO_QUERIES)} queries")
    print("=" * 70)
    latencies = []
    hits_at_5 = 0
    expected_match = 0
    per_query = []

    for dq in DEMO_QUERIES:
        t0 = time.time()
        hits = retr.retrieve(dq["q"], top_n=5)
        elapsed = (time.time() - t0) * 1000
        latencies.append(elapsed)
        # Check if expected name appears in any hit (case-insensitive)
        _gf = lambda h: h.get("grounded_facts") or {}
        names = [(_gf(h).get("name") or "").lower() for h in hits]
        sources = [(_gf(h).get("source") or "").lower() for h in hits]
        all_text = " ".join(names + sources)
        matched = dq["expected_name"].lower() in all_text
        if matched:
            expected_match += 1
            hits_at_5 += 1
        per_query.append({"query": dq["q"], "latency_ms": round(elapsed, 1),
                         "expected": dq["expected_name"], "matched": matched})
        print(f"  {dq['q'][:50]:50s} | {elapsed:6.1f}ms | {'OK' if matched else 'MISS':4s} | expected {dq['expected_name']}")

    summary = {
        "n_queries": len(DEMO_QUERIES),
        "matches": expected_match,
        "recall_at_5": round(expected_match / len(DEMO_QUERIES), 3),
        "latency_p50_ms": round(sorted(latencies)[len(latencies)//2], 1),
        "latency_p95_ms": round(sorted(latencies)[int(len(latencies)*0.95)], 1),
        "latency_max_ms": round(max(latencies), 1),
    }
    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    for k, v in summary.items():
        print(f"  {k}: {v}")
    return {"summary": summary, "per_query": per_query}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--query", "-q", help="Single demo query")
    p.add_argument("--version", "-v", help="Version filter (v12, v15, etc.)")
    p.add_argument("--top-n", type=int, default=3, help="Number of hits (default 3)")
    p.add_argument("--benchmark", action="store_true", help="Run benchmark suite")
    p.add_argument("--out", help="Write JSON results to file")
    args = p.parse_args()

    print("Loading retriever...")
    t0 = time.time()
    retr = HybridRetriever.build_from_disk()
    load_time = (time.time() - t0) * 1000
    print(f"Loaded in {round(load_time, 1)} ms")
    print()

    result = None
    if args.benchmark:
        result = run_benchmark(retr)
    elif args.query:
        run_demo(retr, args.query, args.version, args.top_n)
    else:
        # Default: run a few interesting demo queries
        for dq in DEMO_QUERIES[:3]:
            run_demo(retr, dq["q"], dq.get("expected_version"), 3)

    if args.out and result:
        with open(args.out, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"\nResults written to {args.out}")


if __name__ == "__main__":
    main()
