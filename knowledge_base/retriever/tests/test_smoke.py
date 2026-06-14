"""Smoke tests for the agent-first retriever.

Run:
    cd <knowledge_base>
    python -m retriever.tests.test_smoke

These tests cover exact / hybrid / natural-language fallback routes and
cross-version recall.
"""

from __future__ import annotations
import json
import sys
import time
from pathlib import Path
from typing import List, Dict, Any

from ..retriever import HybridRetriever


TEST_QUERIES: List[Dict[str, Any]] = [
    # ---- exact (BM25 only) ----
    {"q": "setSignal",              "ver": "v15", "topic": "capl",
     "expect": "SetSignal",         "kind": "exact"},
    {"q": "output (CAN)",           "ver": "v15", "topic": "capl",
     "expect": "output",            "kind": "exact"},
    {"q": "on message",             "ver": "v15", "topic": "capl",
     "expect": "on message",        "kind": "exact"},
    {"q": "a429CalcBitLength",      "ver": "v15", "topic": "capl",
     "expect": "a429CalcBitLength", "kind": "exact"},

    # ---- mixed-language / fuzzy BM25 ----
    {"q": "v15 setSignal 函数",     "ver": "v15", "topic": "capl",
     "expect": "SetSignal",         "kind": "hybrid"},

    # ---- cross-version: expect v12 somewhere in the top-K ----
    {"q": "setSignal",              "ver": None, "topic": "capl",
     "expect": "SetSignal",         "kind": "exact",
     "check_v12_present": True},

    # ---- user-added extras ----
    {"q": "setSignalDword",         "ver": "v15", "topic": "extras",
     "expect": "setSignalDword",    "kind": "exact"},
    {"q": "panel gauge binding",    "ver": "v15", "topic": "extras",
     "expect": "Panel Gauge",       "kind": "hybrid"},

    # ---- natural-language fallback (no vector required) ----
    {"q": "how to send a CAN frame","ver": "v15", "topic": "capl",
     "expect": "output",            "kind": "semantic"},
    {"q": "怎么发一帧 CAN 报文",      "ver": "v15", "topic": "capl",
     "expect": "output",            "kind": "semantic"},
    {"q": "面板 Gauge 控件",         "ver": "v15", "topic": "panel",
     "expect": "Gauge",             "kind": "semantic"},

    # ---- DBC ----
    {"q": "DBC attribute definition", "ver": "v15", "topic": "dbc",
     "expect": "Field_Reference",   "kind": "hybrid"},
]


def run():
    base = Path(__file__).resolve().parents[2]
    retr = HybridRetriever.build_from_disk(
        knowledge_dir=base / "knowledge",
        artifacts_dir=base / "artifacts")
    info = retr.info()
    print(json.dumps(info, indent=2))
    has_semantic_vector = info.get("semantic_vector_available", False)
    print(f"\noptional vector backend: {info['vector_backend']} "
          f"({info['vector_count']} docs, semantic={has_semantic_vector})")
    print()

    n_pass, n_total, n_skip = 0, 0, 0
    latencies = []
    for tc in TEST_QUERIES:
        n_total += 1
        if tc.get("needs_semantic_vector") and not has_semantic_vector:
            n_skip += 1
            print(f"[SKIP    ]  ---.--ms  {tc['q']!r:42s} (optional semantic vector disabled)")
            continue

        t0 = time.perf_counter()
        hits = retr.retrieve(tc["q"], version=tc["ver"],
                             topic=tc.get("topic"), top_n=5)
        dt = (time.perf_counter() - t0) * 1000
        latencies.append(dt)

        if not hits:
            print(f"[FAIL    ] {dt:6.1f}ms  {tc['q']!r:42s} -> (no hits)")
            continue

        top = hits[0]
        top_source = top.get("grounded_facts", {}).get("source", "")
        route = top.get("_meta", {}).get("route", "?")

        ok = tc["expect"].lower() in top_source.lower()
        if tc.get("check_v12_present"):
            has_v12 = any(
                "v12" in h.get("grounded_facts", {}).get("source", "")
                for h in hits)
            ok = ok and has_v12

        status = "PASS" if ok else "FAIL"
        n_pass += int(ok)
        print(f"[{status:8s}] {dt:6.1f}ms  {tc['q']!r:42s}  "
              f"route={route:8s} top={top_source}")

    print()
    if latencies:
        latencies.sort()
        p50 = latencies[len(latencies) // 2]
        p95 = latencies[int(len(latencies) * 0.95)]
        print(f"latency: p50={p50:.1f}ms  p95={p95:.1f}ms  "
              f"max={latencies[-1]:.1f}ms  (n={len(latencies)})")
    print(f"\n{n_pass}/{n_total} passed ({n_skip} skipped)")
    return 0 if n_pass + n_skip == n_total else 1


if __name__ == "__main__":
    sys.exit(run())
