"""Agent retrieval-contract tests.

These tests verify that the model-free, agent-first retrieval protocol is
usable end to end:

  semantic intent -> deterministic routing -> constrained candidate search
  -> grounded facts -> answer gate

Run:
    python tests_integration/test_agent_retrieval_contract.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Callable, Dict, List, Tuple


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

from agent_kb.kb_lookup import (  # noqa: E402
    load_page,
    load_scenario_pages,
    match_scenario,
    resolve_symbol,
    search,
)
from retriever.retriever import HybridRetriever  # noqa: E402


Result = Tuple[str, str]
TEST_RESULTS: List[Dict[str, str]] = []
PROTOCOL_PATH = "agent_kb/rules_doc.md"
POLICY_PATH = "agent_kb/rules_policy.md"


def record(test_name: str, status: str, message: str = "") -> None:
    TEST_RESULTS.append({"test": test_name, "status": status, "message": message})
    icon = "[PASS]" if status == "PASS" else ("[WARN]" if status == "WARN" else "[FAIL]")
    print(f"{icon} {test_name}: {message}")


def load_json(rel: str) -> Dict:
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def test_contract_files_present() -> Result:
    required = [
        PROTOCOL_PATH,
        POLICY_PATH,
    ]
    missing = [p for p in required if not (ROOT / p).exists()]
    if missing:
        return "FAIL", "missing: " + ", ".join(missing)
    contract = (ROOT / PROTOCOL_PATH).read_text(encoding="utf-8")
    required_phrases = ["Required Retrieval Order", "Answer Gate", "Grounded synthesis"]
    absent = [p for p in required_phrases if p not in contract]
    if absent:
        return "FAIL", "contract missing sections: " + ", ".join(absent)
    return "PASS", "contract and policy files present"


def test_policy_schema_and_relative_paths() -> Result:
    policy = load_json(POLICY_PATH)
    metadata = policy.get("metadata") or {}
    if metadata.get("default_mode") != "agent_first_bm25_grounded":
        return "FAIL", "unexpected default_mode"
    if metadata.get("model_dependency") != "none":
        return "FAIL", "default policy should not require a model"
    required = {"tool_order", "query_plan_schema", "search_constraints", "answer_gate"}
    missing = required - set(policy)
    if missing:
        return "FAIL", "policy missing keys: " + ", ".join(sorted(missing))
    bad_paths = []
    for tool in policy["tool_order"]:
        surface = str(tool.get("surface", ""))
        if ":" in surface[:3] or surface.startswith(("/", "\\")):
            bad_paths.append(surface)
    if bad_paths:
        return "FAIL", "absolute paths found: " + ", ".join(bad_paths)
    gate = policy["answer_gate"]
    if not gate.get("generated_api_calls_require_loaded_page"):
        return "FAIL", "answer gate does not require loaded pages for generated API calls"
    return "PASS", f"{len(policy['tool_order'])} tools, model-free default"


def test_default_index_is_model_free() -> Result:
    manifest = load_json("artifacts/manifest.json")
    if manifest.get("vector_backend") != "disabled":
        return "FAIL", f"vector_backend should be disabled, got {manifest.get('vector_backend')}"
    if manifest.get("vector_count") != 0:
        return "FAIL", f"vector_count should be 0, got {manifest.get('vector_count')}"
    if manifest.get("semantic_vector_available"):
        return "FAIL", "semantic_vector_available should be false"
    info = HybridRetriever.build_from_disk().info()
    if info.get("vector_backend") != "disabled":
        return "FAIL", f"runtime vector backend should be disabled, got {info}"
    return "PASS", f"bm25_docs={info.get('bm25_docs')}, vector_backend=disabled"


def test_symbol_exact_lookup_gate() -> Result:
    pid = resolve_symbol("setSignal", prefer_version="v15")
    page = load_page("setSignal", version="v15")
    if not pid or not pid.startswith("v15::"):
        return "FAIL", f"setSignal did not resolve to v15: {pid}"
    if not page:
        return "FAIL", "setSignal page did not load"
    syntax = page.get("syntax") or []
    if not syntax or "setsignal" not in " ".join(str(s).lower() for s in syntax):
        return "FAIL", "setSignal syntax not grounded"
    return "PASS", f"{pid} -> {syntax[0][:90]}"


def test_scenario_routing_send_can() -> Result:
    matches = match_scenario("怎么发送报文，写一个 CAN 发送测试")
    if not matches:
        return "FAIL", "no scenario matched"
    first = matches[0]
    if first.get("id") != "send_can_frame":
        return "FAIL", f"expected send_can_frame, got {first.get('id')}"
    pages = load_scenario_pages(first, version="v15")
    primary_ids = [p["id"] for p in pages["primary"]]
    if "v15::capl::CAN::output (CAN)" not in primary_ids:
        return "FAIL", "send_can_frame primary page did not load output (CAN)"
    return "PASS", "send_can_frame -> output (CAN)"


def test_constrained_search_can_send() -> Result:
    hits = search("怎么发一帧 CAN 报文", version="v15", topic="capl", top_n=3)
    if not hits:
        return "FAIL", "no hits"
    top_source = hits[0].get("grounded_facts", {}).get("source", "")
    if "output (CAN)" not in top_source:
        return "FAIL", f"expected output (CAN), got {top_source}"
    meta = hits[0].get("_meta", {})
    if meta.get("route") != "semantic":
        return "WARN", f"top hit is correct but route was {meta.get('route')}"
    return "PASS", f"top={top_source}, route={meta.get('route')}"


def test_panel_concept_search() -> Result:
    hits = search("面板 Gauge 控件", version="v15", topic="panel", top_n=3)
    if not hits:
        return "FAIL", "no hits"
    top_source = hits[0].get("grounded_facts", {}).get("source", "")
    if "Analog Gauge" not in top_source:
        return "FAIL", f"expected Analog Gauge, got {top_source}"
    return "PASS", f"top={top_source}"


def test_team_override_pages_available() -> Result:
    required = ["Common_Gotchas", "CAPL_Internal_Coding_Standards", "CI_Pipeline_Reference"]
    missing = []
    for symbol in required:
        pid = resolve_symbol(symbol, prefer_version="extras")
        page = load_page(symbol, version="extras")
        if not pid or not page:
            missing.append(symbol)
    if missing:
        return "FAIL", "missing team docs: " + ", ".join(missing)
    return "PASS", "team override docs resolve through aliases"


def test_answer_gate_for_generated_code() -> Result:
    policy = load_json(POLICY_PATH)
    gate = policy["answer_gate"]
    required_true = [
        "all_symbols_must_be_resolved_or_marked_unknown",
        "generated_api_calls_require_loaded_page",
        "syntax_must_come_from_grounded_facts",
        "parameters_must_come_from_grounded_facts",
        "team_overrides_checked_for_code_generation",
        "search_hits_require_page_loading_before_fact_use",
    ]
    not_true = [k for k in required_true if gate.get(k) is not True]
    if not_true:
        return "FAIL", "answer gate missing: " + ", ".join(not_true)
    return "PASS", "answer gate blocks ungrounded generated code"


def test_combined_signal_test_retrieval() -> Result:
    query = "setSignal wait for signal match CAPL test"
    scenario_ids = {s.get("id") for s in match_scenario(query)}
    required = {"set_signal_value", "wait_for_signal_condition"}
    if not required.issubset(scenario_ids):
        return "FAIL", f"missing scenarios: {sorted(required - scenario_ids)}"

    set_page = load_page("setSignal", version="v15")
    wait_page = load_page("TestWaitForSignalMatch", version="v15")
    team_page = load_page("canSetSignalDword", version="extras")
    if not set_page or not wait_page or not team_page:
        return "FAIL", "combined flow did not load exact symbol + wait API + team wrapper"

    wait_syntax = " ".join(wait_page.get("syntax") or [])
    team_name = str(team_page.get("name") or "")
    if "TestWaitForSignalMatch" not in wait_syntax:
        return "FAIL", "wait API syntax not grounded"
    if "setSignalDword" not in team_name:
        return "FAIL", "team override wrapper not grounded"
    return "PASS", "scenario + exact symbols + team override loaded"


def test_combined_diagnostics_retrieval() -> Result:
    matches = match_scenario("UDS 0x27 SecurityAccess diagSendRequest 诊断会话")
    if not matches or matches[0].get("id") != "uds_diag_session":
        return "FAIL", f"unexpected diagnostics scenario: {[m.get('id') for m in matches[:3]]}"

    pages = load_scenario_pages(matches[0], version="v15")
    ids = {p["id"] for p in pages["primary"]}
    required = {
        "v15::diagnostics::UDS::UDS_Overview",
        "v15::diagnostics::UDS::SecurityAccess_DID",
        "v15::capl::Diagnostics::diagSendRequest",
    }
    if not required.issubset(ids):
        return "FAIL", f"missing diagnostics pages: {sorted(required - ids)}"

    hits = search("diagSendRequest UDS", version="v15", topic="capl", top_n=5)
    sources = [h.get("grounded_facts", {}).get("source", "") for h in hits]
    if not any("diagSendRequest" in source for source in sources):
        return "FAIL", "constrained diagnostics search did not surface diagSendRequest"
    return "PASS", "diagnostics scenario pages + constrained search grounded"


def test_combined_panel_binding_retrieval() -> Result:
    matches = match_scenario("Panel Button 绑定符号 panel control")
    if not matches or matches[0].get("id") != "panel_button_binding":
        return "FAIL", f"unexpected panel scenario: {[m.get('id') for m in matches[:3]]}"

    pages = load_scenario_pages(matches[0], version="v15")
    primary_ids = {p["id"] for p in pages["primary"]}
    if "v15::panel::Elements::Button" not in primary_ids:
        return "FAIL", "Button page not loaded from panel scenario"

    hits = search("面板 Gauge 控件", version="v15", topic="panel", top_n=3)
    if not hits:
        return "FAIL", "panel constrained search returned no hits"
    top_source = hits[0].get("grounded_facts", {}).get("source", "")
    team_page = load_page("panelGauges", version="extras")
    if "Analog Gauge" not in top_source or not team_page:
        return "FAIL", f"panel gauge grounding incomplete: {top_source}"
    return "PASS", "panel scenario + concept search + team gauge override grounded"


TESTS: List[Tuple[str, Callable[[], Result]]] = [
    ("T001 contract files present", test_contract_files_present),
    ("T002 policy schema and relative paths", test_policy_schema_and_relative_paths),
    ("T003 default index is model-free", test_default_index_is_model_free),
    ("T004 exact symbol lookup gate", test_symbol_exact_lookup_gate),
    ("T005 scenario routing send CAN", test_scenario_routing_send_can),
    ("T006 constrained search CAN send", test_constrained_search_can_send),
    ("T007 panel concept search", test_panel_concept_search),
    ("T008 team override pages available", test_team_override_pages_available),
    ("T009 answer gate for generated code", test_answer_gate_for_generated_code),
    ("T010 combined signal-test retrieval", test_combined_signal_test_retrieval),
    ("T011 combined diagnostics retrieval", test_combined_diagnostics_retrieval),
    ("T012 combined panel-binding retrieval", test_combined_panel_binding_retrieval),
]


def main() -> int:
    print("=" * 70)
    print("AGENT RETRIEVAL CONTRACT TEST")
    print("=" * 70)
    for name, fn in TESTS:
        try:
            status, message = fn()
        except Exception as exc:
            status, message = "FAIL", f"{type(exc).__name__}: {exc}"
        record(name, status, message)

    pass_count = sum(1 for r in TEST_RESULTS if r["status"] == "PASS")
    warn_count = sum(1 for r in TEST_RESULTS if r["status"] == "WARN")
    fail_count = sum(1 for r in TEST_RESULTS if r["status"] == "FAIL")
    total = len(TEST_RESULTS)
    overall = "PASS" if fail_count == 0 else "FAIL"

    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Total tests:  {total}")
    print(f"PASS:         {pass_count}")
    print(f"WARN:         {warn_count}")
    print(f"FAIL:         {fail_count}")
    print(f"[OVERALL] {overall}")

    report_path = ROOT / "tests_integration" / "agent_retrieval_contract_report.json"
    report_path.write_text(
        json.dumps(
            {
                "metadata": {
                    "title": "Agent Retrieval Contract Test Report",
                    "total": total,
                    "pass": pass_count,
                    "warn": warn_count,
                    "fail": fail_count,
                    "overall": overall,
                },
                "results": TEST_RESULTS,
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    print("Report saved to: " + report_path.relative_to(ROOT).as_posix())
    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
