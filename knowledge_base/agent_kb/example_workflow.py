"""End-to-end example: how a canoe-test-generation agent uses the KB.

Run with:
    cd <knowledge_base>
    python agent_kb/example_workflow.py
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

# Force UTF-8 stdout on Windows
import os
os.environ["PYTHONIOENCODING"] = "utf-8"
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

from agent_kb.kb_lookup import (
    load_page, resolve_symbol, match_scenario, load_scenario_pages, search
)


def banner(s):
    print()
    print("=" * 70)
    print(f"  {s}")
    print("=" * 70)


def main():
    banner("STEP 1: User intent comes in")
    user_intent = "I need a CAPL test that waits for EngineSpeed to reach 1500 RPM, then verifies it stays in range for 3 seconds."
    print(f"  USER: {user_intent}")

    banner("STEP 2: Match to known scenario")
    matches = match_scenario(user_intent)
    for sc in matches[:2]:
        print(f"  SCENARIO: {sc['id']} - {sc['title']}")
        print(f"    context: {sc['context']}")

    banner("STEP 3: Load primary + related pages")
    if matches:
        res = load_scenario_pages(matches[0], version="v15")
        for p in res["primary"]:
            d = p["data"]
            syn = (d.get("syntax") or ["(no syntax)"])[0]
            desc = (d.get("description") or ["(no description)"])[0][:150]
            print(f"  - {p['id']}")
            print(f"      syntax: {syn[:120]}")
            print(f"      desc:   {desc}")
        for p in res["related"][:3]:
            d = p["data"]
            syn = (d.get("syntax") or ["(no syntax)"])[0]
            print(f"  - {p['id']} (related)")
            print(f"      syntax: {syn[:120]}")

    banner("STEP 4: Direct symbol lookup (what the code generator needs)")
    for sym in ["TestWaitForSignalMatch", "TestWaitForSignalInRange", "setSignal"]:
        pid = resolve_symbol(sym, prefer_version="v15")
        page = load_page(sym, version="v15")
        if page:
            print(f"  {sym:30s} -> {pid}")
            syn = (page.get("syntax") or ["(no syntax)"])[0]
            print(f"    syntax: {syn[:140]}")
            params = page.get("parameters", [])
            if params:
                print(f"    params: {len(params)}: {', '.join(p.get('name','?') for p in params[:5])}")
            avail = page.get("availability", [])
            if avail:
                # First row of availability matrix usually lists product names
                print(f"    avail:  {avail[0] if avail else 'N/A'}")

    banner("STEP 5: Free-form search (for Q&A / verification)")
    q = "how to send a CAN message from CAPL"
    hits = search(q, version="v15", top_n=3)
    for h in hits:
        g = h.get("grounded_facts", {})
        print(f"  - [{h.get('id')}] {g.get('name')}  ({g.get('page_type')})")
        print(f"      {g.get('syntax','')[:120]}")
        print(f"      {g.get('description','')[:140]}")

    banner("STEP 6: Check team-specific overrides")
    for sym in ["CAPL_Internal_Coding_Standards", "Common_Gotchas", "CI_Pipeline_Reference"]:
        # Try extras version (load_page uses prefer_version='v15' by default)
        # For team docs, we need to use prefer_version="extras"
        from agent_kb.kb_lookup import resolve_symbol as _rs
        pid = _rs(sym, prefer_version="extras")
        if pid:
            from agent_kb.kb_lookup import _id_to_path
            import json as _json
            try:
                page = _json.loads(_id_to_path(pid).read_text(encoding="utf-8"))
                intro = (page.get("intro") or page.get("description") or ["(no intro)"])[0]
                print(f"  {sym} ({pid}): {intro[:150]}")
            except Exception as e:
                print(f"  {sym}: error - {e}")
        else:
            print(f"  {sym}: not found")

    banner("DONE - agent has all facts to generate the test")
    print("  The generated CAPL test should use ONLY the verified syntax,")
    print("  parameters, and return values from the pages loaded above.")


if __name__ == "__main__":
    main()
