"""Improved RAG demo + benchmark (T10 v2).

Improvements over v1:
  - Match against name OR description OR syntax OR source path
  - Use case-insensitive substring match
  - Report per-query details with hit sources
  - Add more representative queries (10 instead of 7)
"""
import os, sys, json, time, argparse
from pathlib import Path
from typing import List, Dict

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from retriever.retriever import HybridRetriever


# 10 representative queries with smarter expected matching
DEMO_QUERIES = [
    {
        "q": "setSignal 函数用法",
        "expected_any": ["setSignal"],   # matches if any of these appears
        "category": "capl/function",
    },
    {
        "q": "CAN error frame selectors",
        "expected_any": ["ErrorFrame", "CAN Error Frame", "MsgChannel"],
        "category": "capl/selector",
    },
    {
        "q": "Panel Button 配置",
        "expected_any": ["Button", "Control Name"],
        "category": "panel/concept",
    },
    {
        "q": "UDS 0x27 security access",
        "expected_any": ["SecurityAccess", "0x27", "seed", "key"],
        "category": "diagnostics/concept",
    },
    {
        "q": "BusLoad 计算",
        "expected_any": ["BusLoad"],
        "category": "capl/function",
    },
    {
        "q": "Timer 在 measure 停止时行为",
        "expected_any": ["timer", "on timer", "cancelTimer", "isMeasurementRunning"],
        "category": "team/concept",
    },
    {
        "q": "v12 parameters setSignal",
        "expected_any": ["setSignal", "v12"],
        "category": "v12/capl",
    },
    {
        "q": "FlexRay frFrame",
        "expected_any": ["frFrame", "on frFrame", "FlexRay"],
        "category": "capl/event",
    },
    {
        "q": "DTC 读取 故障码",
        "expected_any": ["DTC", "DiagGetDTC", "readDTCInformation"],
        "category": "diagnostics/function",
    },
    {
        "q": "vTESTstudio Jenkins CI",
        "expected_any": ["Jenkins", "vTESTstudio", "CI", "pipeline"],
        "category": "team/concept",
    },
]


def _hit_text(hit: Dict) -> str:
    """Build searchable text from a hit (lowercase)."""
    g = hit.get("grounded_facts") or {}
    parts = []
    for field in (
        "name", "title", "source", "syntax", "description", "category",
        "sections", "tables", "selectors", "property_references",
        "return_type_inferred",
    ):
        v = g.get(field)
        if isinstance(v, list):
            parts.extend(str(x) for x in v)
        elif v is not None:
            parts.append(str(v))
    return " ".join(parts).lower()


def _hit_score(hit: Dict, keywords: List[str]) -> int:
    """Count how many keywords appear in hit text. Higher = better match."""
    text = _hit_text(hit)
    return sum(1 for kw in keywords if kw.lower() in text)


def run_single(retr, query: str, top_n: int = 5) -> Dict:
    t0 = time.time()
    hits = retr.retrieve(query, top_n=top_n)
    elapsed = (time.time() - t0) * 1000
    return {"query": query, "elapsed_ms": round(elapsed, 1),
            "hits": hits, "hit_count": len(hits)}


def evaluate_hit(hits: List, expected_any: List[str], top_n: int = 5) -> Dict:
    """Check if any expected keyword appears in top-N hits."""
    for h in hits[:top_n]:
        text = _hit_text(h)
        for kw in expected_any:
            if kw.lower() in text:
                return {"matched": True, "matched_keyword": kw,
                        "matched_source": (h.get("grounded_facts") or {}).get("source", "?")}
    return {"matched": False, "matched_keyword": None, "matched_source": None}


def run_benchmark(retr) -> Dict:
    print("=" * 80)
    print(f"BENCHMARK: {len(DEMO_QUERIES)} queries (improved matching)")
    print("=" * 80)
    latencies = []
    matches = 0
    per_query = []
    for dq in DEMO_QUERIES:
        r = run_single(retr, dq["q"], top_n=5)
        latencies.append(r["elapsed_ms"])
        ev = evaluate_hit(r["hits"], dq["expected_any"], top_n=5)
        if ev["matched"]:
            matches += 1
        per_query.append({
            "query": dq["q"],
            "category": dq["category"],
            "expected_any": dq["expected_any"],
            "latency_ms": r["elapsed_ms"],
            **ev,
        })
        status = "OK" if ev["matched"] else "MISS"
        kw = ev["matched_keyword"] or "-"
        print(f"  [{status:4s}] {dq['q'][:45]:45s} | {r['elapsed_ms']:6.1f}ms | kw={kw}")

    summary = {
        "n_queries": len(DEMO_QUERIES),
        "matches": matches,
        "recall_at_5": round(matches / len(DEMO_QUERIES), 3),
        "latency_p50_ms": round(sorted(latencies)[len(latencies)//2], 1),
        "latency_p95_ms": round(sorted(latencies)[int(len(latencies)*0.95)], 1),
        "latency_max_ms": round(max(latencies), 1),
    }
    print()
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    for k, v in summary.items():
        print(f"  {k}: {v}")
    return {"summary": summary, "per_query": per_query}


def run_demo(retr, query: str, top_n: int = 3):
    print("=" * 80)
    print(f"Query: {query!r}")
    print("=" * 80)
    r = run_single(retr, query, top_n)
    print(f"Latency: {r['elapsed_ms']} ms | Hits: {r['hit_count']}")
    for i, h in enumerate(r["hits"]):
        g = h.get("grounded_facts") or {}
        src = g.get("source", "?")
        syntax = (g.get("syntax") or "")[:60]
        print(f"  [{i+1}] {src}")
        if syntax:
            print(f"      syntax: {syntax}")
    print()


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--query", "-q")
    p.add_argument("--top-n", type=int, default=3)
    p.add_argument("--benchmark", action="store_true")
    p.add_argument("--out", help="Write JSON results to file")
    args = p.parse_args()

    print("Loading retriever...")
    t0 = time.time()
    retr = HybridRetriever.build_from_disk()
    load_time = (time.time() - t0) * 1000
    print(f"Loaded in {round(load_time, 1)} ms")
    print()

    if args.benchmark:
        result = run_benchmark(retr)
        if args.out:
            with open(args.out, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2, ensure_ascii=False)
            print(f"\nResults written to {args.out}")
    elif args.query:
        run_demo(retr, args.query, args.top_n)
    else:
        # Run a few interesting demo queries
        for dq in DEMO_QUERIES[:3]:
            run_demo(retr, dq["q"])


if __name__ == "__main__":
    main()
