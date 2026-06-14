# Integrating the Knowledge Base with the CANoe Test Generation Workflow

> **Audience**: Engineer building the canoe-test-generation workflow.
> **Goal**: Make the KB the **single source of truth** for Vector CANoe API
> facts, used by every agent in the pipeline (intake planner, scenario
> expander, code generator, validator, etc.).

## TL;DR — Three access patterns

Before wiring tools, treat [`rules_doc.md`](./rules_doc.md)
as the required protocol and [`rules_policy.md`](./rules_policy.md)
as the machine-readable answer gate.

| Need | Pattern | When |
|------|---------|------|
| "I need the exact page for a CAPL symbol" | `kb_lookup.load_page(name, version)` | Code generator knows `setSignal`, `output`, etc. |
| "The user said X in natural language" | `kb_lookup.match_scenario(text)` + `load_scenario_pages` | Intent classification |
| "I need candidate pages for free-form text" | `kb_lookup.search(query, ...)` or `retriever.retrieve(...)` | Free-form Q&A, validation |
| "I need stats / what's available" | `capability_manifest.md` or `kb_lookup` for index | Planning, capability checks |

## Recommended wiring in your workflow

### 1) Workflow manifest registration

```yaml
# In your workflow's tools section:
tools:
  canoe_kb_lookup:
    type: python_module
    module: agent_kb.kb_lookup
    functions:
      - resolve_symbol
      - load_page
      - match_scenario
      - load_scenario_pages
      - search
  canoe_kb_search:
    type: http
    url: http://127.0.0.1:8765/search
    method: GET
    params: [q, version, topic, page_type, top_n]
```

### 2) Tool definitions (for the LLM agent)

```python
TOOL_DEFS = [
    {
        "name": "kb_load_page",
        "description": "Load the structured JSON for a CAPL symbol. Returns syntax, parameters, return, example, availability. Use this when you have a specific CAPL function name.",
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {"type": "string", "description": "CAPL function/method/event name (e.g. 'setSignal', 'output', 'on message')"},
                "version": {"type": "string", "enum": ["v12", "v15", "v17", "v18"], "default": "v15"},
            },
            "required": ["symbol"],
        },
    },
    {
        "name": "kb_match_scenario",
        "description": "Match a natural-language intent to a known test scenario. Returns the scenario id and the list of primary/related pages to consult.",
        "parameters": {
            "type": "object",
            "properties": {
                "intent": {"type": "string", "description": "User's request in natural language (English or Chinese)"},
            },
            "required": ["intent"],
        },
    },
    {
        "name": "kb_search",
        "description": "Free-form candidate search across the entire knowledge base. Returns grounded facts (canonical syntax/parameters). Use this when the user asks a question that doesn't match a known scenario; the agent performs semantic interpretation.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string"},
                "version": {"type": "string", "default": "v15"},
                "topic": {"type": "string", "enum": ["capl", "panel", "dbc", "xcp", "diagnostics"]},
                "page_type": {"type": "string", "enum": ["function", "method", "event", "selector", "concept"]},
                "top_n": {"type": "integer", "default": 5},
            },
            "required": ["query"],
        },
    },
    {
        "name": "kb_capability_check",
        "description": "Check whether the knowledge base has any page related to a topic. Returns true/false + count of matching pages.",
        "parameters": {
            "type": "object",
            "properties": {
                "topic": {"type": "string"},
            },
            "required": ["topic"],
        },
    },
]
```

### 3) Tool implementations (Python)

```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path.cwd()))
from agent_kb.kb_lookup import (
    resolve_symbol, load_page, match_scenario, load_scenario_pages, search
)
import json

def tool_kb_load_page(symbol: str, version: str = "v15") -> str:
    """For the LLM: returns a clean, LLM-friendly summary."""
    page = load_page(symbol, version=version)
    if page is None:
        return f"NOT FOUND: {symbol} (in {version})"
    pid = resolve_symbol(symbol, version=version) or f"{version}::unknown::{symbol}"
    bits = [f"=== {pid} ===", f"type: {page.get('page_type')}"]
    for k in ("syntax", "description", "parameters", "return", "example", "availability"):
        v = page.get(k)
        if v:
            s = json.dumps(v, ensure_ascii=False)[:1200]
            bits.append(f"{k}: {s}")
    if page.get("sections"):
        for s in page["sections"][:5]:
            ps = s.get("content", {}).get("paragraphs", [])
            if ps:
                bits.append(f"section '{s.get('heading')}': {' '.join(ps)[:200]}")
    return "\n".join(bits)


def tool_kb_match_scenario(intent: str) -> str:
    matches = match_scenario(intent)
    if not matches:
        return f"No known scenario matches {intent!r}. Try kb_search."
    out = []
    for sc in matches[:3]:
        out.append(f"## {sc['id']}: {sc['title']}")
        out.append(f"context: {sc['context']}")
        res = load_scenario_pages(sc, version="v15")
        for p in res["primary"]:
            d = p["data"]
            syn = d.get("syntax", [""])[0]
            desc = (d.get("description") or [""])[0]
            out.append(f"  - {p['id']}: {syn[:100]}")
            out.append(f"      {desc[:150]}")
        if res["missing"]:
            out.append(f"  (missing primary pages: {res['missing']})")
    return "\n".join(out)


def tool_kb_search(query: str, version: str = "v15", topic: str = None,
                   page_type: str = None, top_n: int = 5) -> str:
    hits = search(query, version=version, topic=topic,
                  page_type=page_type, top_n=top_n)
    if not hits:
        return "No results."
    out = [f"Found {len(hits)} hits for {query!r}:"]
    for h in hits:
        g = h.get("grounded_facts", {})
        out.append(f"- [{h.get('id')}] {g.get('name')} ({g.get('page_type')})")
        out.append(f"  syntax: {g.get('syntax','')[:150]}")
        if g.get("description"):
            out.append(f"  desc: {g['description'][:200]}")
    return "\n".join(out)
```

### 4) MCP server alternative

If your workflow uses MCP, the existing retriever already exposes a server:

```bash
python -m retriever.mcp_server   # exposes search_canoe, canoe_info, canoe_add, canoe_remove
```

To expose the new helpers, extend [retriever/mcp_server.py](../retriever/mcp_server.py) — the
`tool_*` functions are already designed to be wrapped.

## Agent pipeline integration — where to call what

```
┌────────────────────────────────────────────────────────────────────────┐
│  canoe-test-generation workflow                                       │
│                                                                        │
│  1. Intent classification                                              │
│     └─► tool_kb_match_scenario(user_request)                           │
│         Returns: scenario_id + primary pages + context                 │
│                                                                        │
│  2. Test plan generation                                               │
│     └─► tool_kb_load_page(...)  for each CAPL function in the plan    │
│         Returns: syntax, parameters, return, example, availability     │
│                                                                        │
│  3. CAPL code generation                                               │
│     └─► tool_kb_load_page(...)  to get exact API signatures           │
│         tool_kb_load_page(...)  for any nested function call           │
│                                                                        │
│  4. Validation / hallucination check                                   │
│     └─► tool_kb_load_page(...)  for every CAPL function in the        │
│         generated code; verify the signature is in the KB.             │
│         tool_kb_search(...)  for "is this API valid in v15?"            │
│                                                                        │
│  5. Version-specific adaptations                                       │
│     └─► Read L3_diffs/DIFF_REPORT.md for v12 vs v15 differences       │
└────────────────────────────────────────────────────────────────────────┘
```

## Conventions for the agent

0. **Follow the retrieval contract** — semantic understanding must become a structured query plan, then deterministic lookups, then constrained search, then grounded synthesis.
1. **Default to v15** unless the user specifies v12 or it's a legacy project.
2. **Prefer `load_page` over `search`** when you have a symbol — it's exact, fast (no embedding), and you get the canonical facts directly.
3. **Use scenarios for intent matching** — they're 10 high-precision lookups that beat free-form search for the common cases.
4. **Read both `.json` and `.md`**. The `.json` has structured fields (parameters, availability); the `.md` has the rendered prose that the LLM can quote in its answer.
5. **Always check `extras/team/` for project conventions** before generating code. The team's coding standards override Vector's defaults.
6. **Don't trust `page_type: notes`** — it can be a selector page or function index. Check `syntax[0]` and `selectors[]` directly.

## Anti-patterns

- ❌ Don't iterate 10K JSON files looking for a function — use the alias index.
- ❌ Don't write CAPL syntax from memory — always verify against `load_page`.
- ❌ Don't use `page_type` as a search filter without first reading the manifest.
- ❌ Don't query both `v12` and `v15` simultaneously without understanding the diff (read L3_diffs first).

## Performance notes

- `load_page` is **~1ms** (file read + JSON parse). Use it freely.
- `match_scenario` is **~5ms** (small JSON, keyword matching). Use it as first pass.
- `search` is BM25 candidate retrieval plus grounding. Use it when exact symbol/scenario lookup does not apply; the calling agent should read the returned facts and decide relevance.
- For high-throughput agents, consider preloading the alias index into memory once and using `_ALIASES` directly (it's a 5MB dict, fits easily in RAM).

## Example agent turn (how a typical interaction looks)

```
USER: "I need a CAPL test that waits for the EngineSpeed signal to reach 1500 RPM, then verifies it stays in range for 3 seconds."

AGENT:
  Step 1: tool_kb_match_scenario("wait for signal match in range")
          -> "wait_for_signal_condition" with 2 primary pages
  
  Step 2: tool_kb_load_page("TestWaitForSignalMatch", "v15")
          -> syntax: long TestWaitForSignalMatch(Signal aSignal, float aCompareValue);
                     + 4 more forms
  
  Step 3: tool_kb_load_page("TestWaitForSignalInRange", "v15")
          -> syntax: long TestWaitForSignalInRange(Signal aSignal, float aLow, float aHigh, dword aTimeout);
  
  Step 4: tool_kb_load_page("extras::team::setSignalDword", "v15")
          -> team wrapper to use for setting the test value
  
  Step 5: tool_kb_load_page("extras::team::Common_Gotchas", "v15")
          -> check for gotchas on signal in range

  Then synthesize the CAPL test code using ONLY the verified syntax.
```
