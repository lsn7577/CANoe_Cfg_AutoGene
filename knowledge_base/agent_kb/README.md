# Agent-Facing Knowledge Base Navigation

> **Purpose**: This directory provides an agent-friendly view of the entire CANoe knowledge base.
> The underlying structured data lives in [`knowledge/`](../knowledge/); use this directory as the **first lookup point** for any agent in the canoe-test-generation workflow.

## 📁 Contents

| File | Size | Purpose | When to consult |
|------|-----:|---------|-----------------|
| [`capability_manifest.md`](./capability_manifest.md) | 6 KB | High-level **what the KB knows** (topics, versions, coverage) | First step of any query — verify the KB has the answer |
| [`rules_doc.md`](./rules_doc.md) | 5 KB | Human-readable **agent retrieval protocol** | Before implementing an agent integration |
| [`rules_policy.md`](./rules_policy.md) | 5 KB | Machine-readable JSON retrieval rules and answer gate | For automated checks / agent runtime policy |
| [`unified_index.json`](./unified_index.json) | 6.7 MB | Machine-readable index of **every page** (id → topic/version/path/summary) | Programmatic lookup: "give me docs matching X" |
| [`query_routing.md`](./query_routing.md) | 6 KB | Decision tree: **"I have question Q, which part of the KB to read?"** | Before doing a search — direct file pointers save tokens |
| [`scenarios.json`](./scenarios.json) | 8 KB | **Common test-generation scenarios** → exact pages to consult | When the user wants to do "send CAN frame", "wait for signal", etc. |
| [`schema_v3.json`](./schema_v3.json) | 5 KB | Authoritative JSON schema for one page | When writing/validating new knowledge |
| [`symbol_aliases.json`](./symbol_aliases.json) | 1.8 MB | Symbol → page lookup (e.g., `setSignal` → `v15::capl::CAN::setSignal`) | When you have a CAPL function name and need its page |
| [`kb_lookup.py`](./kb_lookup.py) | 5 KB | Python helper — `resolve_symbol`, `load_page`, `match_scenario`, `search` | When embedding KB access in Python agent code |
| [`build_manifest.py`](./build_manifest.py) | 6 KB | Regenerates the artifacts above from `knowledge/` + `extras/` | After adding new pages, run to refresh views |

## 🧭 Recommended Workflow for Agents

```text
1. Read rules_doc.md                ──►  follow the required lookup order
2. Read capability_manifest.md  ──►  decide if KB has the topic
3. Read query_routing.md        ──►  find the candidate paths/files
4. Match user intent to scenarios.json
5. Load specific pages (kb_lookup.load_page)  ──►  read .json + .md
6. Fall back to: kb_lookup.search() or retriever.serve /search  ──►  get BM25 candidates + grounded facts
```

## 🔌 Programmatic Access (Most Common)

```python
# Quick start
import sys
from pathlib import Path
sys.path.insert(0, str(Path.cwd()))
from agent_kb.kb_lookup import (
    resolve_symbol,    # "setSignal" -> "v15::capl::CommunicationObjects::SetSignal"
    load_page,         # "setSignal", "v15" -> parsed JSON dict
    match_scenario,    # "how to send a CAN frame" -> [{'id': 'send_can_frame', ...}]
    load_scenario_pages, # scenario -> {'primary': [...], 'related': [...], 'missing': [...]}
    search,            # BM25 candidate retrieval + grounding; agent does semantic reasoning
)

# 1) I have a CAPL symbol name
page = load_page("setSignal", "v15")
print(page["syntax"], page["description"])

# 2) I have a natural-language intent
matches = match_scenario("wait for signal to match a value")
if matches:
    pages = load_scenario_pages(matches[0], version="v15")
    for p in pages["primary"]:
        print(p["id"], p["data"]["syntax"])

# 3) Free-form search
hits = search("如何用 sysvar:: 设置一个浮点信号", version="v15", top_n=5)
for h in hits:
    print(h["grounded_facts"]["name"], h["grounded_facts"]["syntax"])
```

## 🆚 knowledge/ vs agent_kb/

| Aspect | `knowledge/` (raw) | `agent_kb/` (this) |
|--------|--------------------|--------------------|
| Format | One JSON per page + .md render | Aggregated views |
| Granularity | Per-page | Per-collection / per-capability |
| Use | "What does this single page say?" | "What does the KB know about X?" |
| Authoritative? | ✅ Yes (source of truth) | ❌ No (derived; auto-regenerated) |

## 🔄 Maintenance

After adding pages to `knowledge/` or `extras/`:

```bash
cd <knowledge_base>
python agent_kb/build_manifest.py    # regenerate unified_index + aliases
python -m retriever.build            # rebuild default BM25 index
```

## 📊 Current Snapshot (rebuilt on every run)

- **9,909 pages** total (10,075 in BM25 index; the 166 missing are due to path canonicalization)
- **v15**: 5,174 pages, **v12**: 4,730 pages, **extras/team**: 5
- **Selector pages**: 72 (correctly classified, vs only 9 in raw corpus)
- **By type**: 8,447 functions, 752 notes, 468 concepts, 381 methods, 169 events, 72 selectors

> ⚠️ **Note**: The raw corpus has selector pages mis-tagged as `notes` (see capability_manifest §6 K2).
> The `unified_index.json` re-classifies them correctly based on the page name heuristic.
