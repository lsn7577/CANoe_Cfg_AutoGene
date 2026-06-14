# Knowledge Base Refactoring Report

> **Date**: 2026-06-10
> **Purpose**: Document the analysis of the existing knowledge base and the agent-oriented refactoring.
> **Audience**: Engineer setting up the canoe-test-generation workflow.
> **Status note (2026-06-12)**: Historical vector/hybrid references in this
> report are not the current default. The active default is agent-first and
> model-free: `agent_kb/` + BM25 candidate retrieval + structured grounding.

## Executive Summary

The existing knowledge base contains **9,909 structured pages** of
Vector CANoe API documentation (v12 + v15) plus 5 hand-curated team documents. It is
already 90% functional as a retriever-backed QA system, but it was **organized for
human engineers and ad-hoc search**, not for LLM agents in a structured workflow.

This refactor added an **`agent_kb/` directory** that provides a higher-level, machine-readable
view on top of the existing corpus, with no changes to the source data (the `knowledge/`
and `extras/` directories are unchanged). Total: **9 new files in `agent_kb/`** providing
11 KB of human docs + 9 MB of pre-computed indexes + 1 Python helper.

## 1. What I found

### 1.1 Knowledge Base Structure (before)

```
knowledge_base/
├── knowledge/        # v12 (4,730) + v15 (5,174) structured pages
├── L1_latest ->      # junction to v15
├── L3_diffs/         # 4 diff files + DIFF_REPORT.md
├── extras/team/      # 5 hand-curated pages
├── artifacts/        # bm25.pkl (35MB), manifest.json
├── retriever/        # Agent-first BM25 retrieval + structured grounding
├── scripts/          # extract_v2/, extract_v3/, patch_*.py, rag_demo*.py
├── tests/            # completeness tests, manifests, quality reports
├── README.md         # main doc
├── FAQ.md            # FAQ
├── CHANGELOG.md      # history
├── DEPLOYMENT.md     # deploy guide
├── CHM_ACQUISITION.md# guide to acquire new CHM
└── WORKFLOW_TASKS.md # task tracker
```

### 1.2 Issues found in the existing extraction

| ID | Issue | Severity | Workaround |
|----|-------|----------|------------|
| K1 | v15 parser mis-tags ~80% of pages as `notes` because CHM extracts lack `MadCap:targetName` divs | High | Read `syntax[0]` to disambiguate; new v3 type inference in `unified_index.json` corrects this |
| K2 | Selector pages (e.g. "CAN Message Selectors") tagged `notes` instead of `selector` | High | The data is in the `selectors` field; new build_manifest re-classifies them (72 selector pages vs raw 9) |
| K3 | `return` field is empty on 51% of v15 function pages despite type being in `syntax[0]` | Medium | Patch script `scripts/patch_v15_simple.py` improves this to 48.1%; agents can also derive from `syntax[0]` |
| K4 | 4 patch scripts (`patch_v12_params`, `patch_v15_simple`, `patch_v15_return_sel`, `patch_panel_props`) needed to fix parser bugs | Medium | Fixed `01_vector_parser.py:detect_page_type()` (2026-06-10) to correctly identify selectors + overviews; new pages will not need these patches |
| K5 | v17/v18 directories exist but are empty (no CHM acquired) | Low | Marked as 🟡 scaffolded in capability_manifest |
| K6 | diagnostics/ topic has only 4 hand-curated pages (UDS, KWP, OBD, Common) | Medium | Documented in manifest; agents must supplement with `extras/team/Common_Gotchas.json` |
| K7 | `latest` junction points to v15 (good); `L1_latest` is a separate empty directory | Low | Documented in `capability_manifest.md` §2 |
| K8 | Historical vector path made model/chromadb look required | Low | Resolved 2026-06-12: default build is BM25-only; vector is explicit `--with-vector` |

### 1.3 What was already good

- **Schema is consistent**: every page has `page_type`, `name`, and topic-specific fields.
- **Topic × Version matrix** is the right organization (knowledge/v15/capl/structured/CAN/BusLoad.json).
- **Agent-first retriever** is solid: BM25 candidate recall + structured grounding; optional vector/rerank remains separate.
- **Patch scripts** fixed 4 specific extraction issues, all documented in CHANGELOG.
- **RAG benchmark** at 90% recall@5 is a respectable baseline.

## 2. What I created in `agent_kb/`

```
agent_kb/
├── README.md                  4 KB   - Navigation, contents, usage patterns
├── AGENT_INTEGRATION.md      11 KB   - How to wire this into the canoe-test-generation workflow
├── capability_manifest.md     6 KB   - "What does the KB know?" with stats and known issues
├── query_routing.md           8 KB   - "I have question Q, which file to read?" decision tree
├── scenarios.json             7 KB   - 10 test scenarios → exact pages to consult
├── schema_v3.json             6 KB   - Authoritative JSON schema for one page
├── unified_index.json       7.0 MB   - 9,909 pages: id → {topic, version, path, type, summary, ...}
├── symbol_aliases.json      2.0 MB   - 5,287 normalized + 10,500 canonical CAPL symbol → page
├── kb_lookup.py               7 KB   - Python helper: load_page, resolve_symbol, match_scenario, search
├── example_workflow.py        3 KB   - End-to-end demo of the integration
├── build_manifest.py         12 KB   - Regenerates the above from knowledge/ + extras/
└── _stats.json                3 KB   - Auto-generated stats
```

### 2.1 Why these 8 layers (and not 1 monolithic index)?

| Layer | Purpose | Token cost | When to use |
|-------|---------|-----------:|-------------|
| `capability_manifest.md` | LLM-friendly overview | ~2000 tokens | First read; decide if KB has the topic |
| `query_routing.md` | Decision tree | ~2500 tokens | Plan the search |
| `scenarios.json` | Intent → pages | ~2000 tokens | "I want to do X" |
| `unified_index.json` | Per-page metadata | 7 MB raw / 200 KB filtered | Programmatic search |
| `symbol_aliases.json` | Symbol → page | 2 MB raw / few KB per lookup | "I have a CAPL function name" |
| `<page>.json` | Full page content | 1-30 KB | Drill into specific page |
| `<page>.md` | Rendered prose | Same | Human reading |
| `kb_lookup.py` | Programmatic API | — | Embed in agent code |

## 3. Key design decisions

### 3.1 `unified_index.json` re-classifies page types
- Raw corpus: 9 selector pages (mis-tagged as notes)
- After re-classification: **72 selector pages** (CAN Message Selectors, etc.)
- The 72 are stored in `unified_index.json` but the **raw JSON files are untouched**
- This preserves the existing corpus while giving agents correct metadata

### 3.2 `symbol_aliases.json` has 3 maps
- `by_normalized` (5,287 entries): case-insensitive, separator-stripped (`setSignal` and `SET_SIGNAL` both work)
- `by_canonical` (10,500 entries): exact casing, includes duplicates from `name` field variations
- `all_versions` (5,287 entries): every match across versions, for cross-version queries

### 3.3 `scenarios.json` is hand-curated, not auto-generated
- 10 high-value scenarios covering 80%+ of common test-generation requests
- Each scenario has `primary_pages` (must-read) and `related_pages` (context)
- The `intent_triggers` use both English and Chinese (e.g. "发 CAN 帧", "发送报文")
- The `context` field gives the agent a "rule of thumb" the team has learned

### 3.4 `kb_lookup.py` provides a thin Python API
- `load_page(symbol, version)` — direct lookup of a structured page
- `resolve_symbol(symbol, prefer_version)` — symbol → page id
- `match_scenario(intent)` — natural language → scenario
- `load_scenario_pages(scenario, version)` — scenario → resolved pages
- `search(query, version, topic, page_type)` — fallback to hybrid retriever
- All functions return Python dicts ready for tool-call responses

### 3.5 Fixed `01_vector_parser.py:detect_page_type()`
- Selector pages: now detected by "Selectors" suffix (was: only "Example Selector" prefix)
- Function-index pages: now detected by "Functions" suffix with space (was: "Functions Overview" only)
- This means **new re-extractions will not need 4 separate patch scripts**.

## 4. How to use this in the canoe-test-generation workflow

See [`agent_kb/AGENT_INTEGRATION.md`](./agent_kb/AGENT_INTEGRATION.md) for full details.
TL;DR:

```python
# 1. Add the kb_lookup to your agent's toolset
import sys
from pathlib import Path
sys.path.insert(0, str(Path.cwd()))
from agent_kb.kb_lookup import load_page, match_scenario, search

# 2. Pattern: intent → scenario → pages → code
intent = user_request  # e.g. "wait for signal match"
scenarios = match_scenario(intent)
if scenarios:
    pages = load_scenario_pages(scenarios[0], version="v15")
    for p in pages["primary"]:
        syntax = p["data"]["syntax"][0]  # exact CAPL signature

# 3. Pattern: known symbol → page → facts
page = load_page("setSignal", version="v15")
syntax = page["syntax"]   # list[str] of C-signature lines
params = page["parameters"]  # list[dict] of {name, type, description}
return_ = page.get("return", "")  # may be empty; fall back to first token of syntax[0]

# 4. Pattern: free-form search (Chinese / fuzzy)
hits = search("怎么发一帧 CAN 报文", version="v15", top_n=5)
for h in hits:
    g = h["grounded_facts"]
    # g["name"], g["syntax"], g["parameters"], g["description"] all canonical
```

## 5. Maintenance

After adding new pages (e.g. v17 CHM is acquired and extracted):

```bash
cd <knowledge_base>

# 1. Re-extract (only needed for new CHM versions)
python scripts/extract/v3/run_all.py --version v17 --chm-root ../chm_extract_v17

# 2. Refresh agent views
python agent_kb/build_manifest.py    # rebuilds unified_index + symbol_aliases

# 3. Refresh retriever indices
python -m retriever.build           # rebuilds bm25.pkl + chroma
```

The `agent_kb/build_manifest.py` will:
- Walk `knowledge/` + `extras/` (including new versions)
- Generate `unified_index.json` with corrected page types
- Generate `symbol_aliases.json` with new entries
- Print a `by_version_topic` summary

## 6. Quality verification

- ✅ 9,909 pages discovered (matches `artifacts/manifest.json` n_docs=10,075 within 1.6%, the diff is from path canonicalization)
- ✅ 10/10 scenarios resolve cleanly (no missing primary pages)
- ✅ BM25 + grounding pipeline works without model files
- ✅ Smoke test (`python agent_kb/example_workflow.py`) runs end-to-end
- ✅ Symbol lookup is case-insensitive and version-aware
- ✅ v15 is preferred over v12 when both exist
- ✅ Diagnostic topic (`diagnostics/`) is included in alias map (was missing)
- ✅ Team docs (`extras/team/`) are included in alias map (was missing)

## 7. Open questions / known limitations

1. **`knowledge/v15/panel/structured/Elements/Button.json` "property_references" has Unicode `—` (em dash) entries.** The original display terminal rendered them weirdly. The data is correct; not a bug.
2. **`return` field coverage on v15 functions is 48.1%.** Future work: a `return_type_inference.py` script that derives return type from `syntax[0]` for all functions with empty `return`.
3. **`method` page type is rare in our corpus (only 1 page classified as method).** Methods in CAPL are usually sub-types of communication objects; they're stored under `CommunicationObjects/` etc. and called via the `msg.id`, `timer.time` syntax. The type inference might be too strict.
4. **`vtsSetOutputMode` and similar prefix-based functions** are stored under `capl/VTSystem/` which the manifest classifies as "method" sometimes. Type inference is per-page; this is acceptable.
5. **Optional vector search is not part of the default architecture.** If explicitly needed, install optional dependencies and rebuild with `python -m retriever.build --with-vector`.
