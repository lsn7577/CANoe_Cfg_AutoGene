# CANoe Knowledge Base — Capability Manifest

> **Auto-generated** by `agent_kb/build_manifest.py`.
> Last build: 2026-06-10
> **This is the first file an agent should read** to understand what the knowledge base contains.

## 1. Scope

The knowledge base is a structured corpus extracted from the official Vector CANoe
help documentation, plus hand-curated team documentation. It is intended to ground
LLM agents in factual Vector CANoe API and tooling knowledge — reducing hallucinations
when answering questions or generating code. The default access pattern is
agent-first: use exact indexes and BM25 candidates, then let the calling agent
perform semantic interpretation over grounded facts.

**NOT in scope** (consult other sources):
- Vector hardware manuals (VN16xx, VT63xx, etc.)
- Third-party tools (CANalyzer Pro, INCA, etc.)
- Customer-specific ECU specifications
- AUTOSAR standard specification (BSW/ASW layer spec)

## 2. Versions Covered

| Version | Status | Pages | Source |
|---------|:------:|------:|--------|
| **v15** (CANoe 15.0) | ✅ Complete | 5,174 | `knowledge/v15/` |
| **v12** (CANoe 12.0) | ✅ Complete | 4,730 | `knowledge/v12/` |
| v17 | 🟡 Scaffolded | 0 | `knowledge/v17/` (CHM not yet acquired) |
| v18 | 🟡 Scaffolded | 0 | `knowledge/v18/` (CHM not yet acquired) |
| **extras** (team) | ✅ Hand-curated | 5 | `extras/team/` |

**Default version to use**: v15 (latest; widely deployed in industry; majority of EQ07 fleet).

## 3. Topics Covered

| Topic | Purpose | v15 pages | v12 pages | Examples |
|-------|---------|----------:|----------:|----------|
| **capl** | CAPL programming language (functions, methods, events, selectors) | 4,951 | 4,487 | `setSignal`, `on message`, `sysvar::*` |
| **panel** | Panel Designer (UI controls for the runtime) | 69 | 83 | `Button`, `Switch/Indicator`, `LED Control` |
| **dbc** | CANeds DBC editor (database keywords, attributes) | 150 | 160 | `BO_`, `SG_`, `BA_DEF_`, attributes |
| **xcp** | XCP CAPL functions (calibration protocol) | 17 | 17 | `xcpConnect`, `xcpActivate` |
| **diagnostics** | UDS / KWP2000 / OBD (synthetic) | 4 | 0 | `DiagSetSession`, `0x27 SecurityAccess` |
| **team** | Internal coding standards, gotchas, CI (hand-curated) | 5 | — | `setSignalDword` wrapper, Jenkins pipeline |

**Missing topics** (CHM doesn't have a dedicated section): test module library reference
(`TestSet*` / `ChkCreate_*` live under `capl/Test/`), Network Management (deprecated in v15).

## 4. Page Types (5 schema types)

| Type | Meaning | Example | Count |
|------|---------|---------|------:|
| `function` | CAPL function: `void foo(long x);` | `BusLoad`, `setSignal` | 8,102 |
| `method` | CAPL method: `msg.id;` (property-style) | `msg.id`, `timer.time` | 381 |
| `event` | CAPL event: `on message Msg { ... }` | `on key`, `on errorFrame` | 169 |
| `selector` | CAPL selector table page | `CAN Message Selectors` | 9 (⚠ under-classified — see §6) |
| `concept` | Explanatory / reference page (Panel control, DBC keyword) | `Button` (Panel) | 464 |
| `notes` | Unclassified (overview / tabular reference) | `CAN CAPL Functions` (overview) | 779 |

## 5. Field Coverage (per page type)

### CAPL function/event/method (v15)
| Field | Coverage | Notes |
|-------|---------:|-------|
| `description` | 95.7% | Very high |
| `syntax` | 82.9% | List of C-signature lines |
| `parameters` | 72.6% | List of `{name, type, description}` |
| `availability` | 84.8% | Version matrix rows |
| `example` | 54.5% | `{description, code}` |
| `return` | **48.1%** (post-patch) | Empty when not in source; can be derived from `syntax[0]` |
| `selectors` | 1.6% | Mostly empty; real selectors live on dedicated `selector` pages |

### Concept (v15)
| Field | Coverage | Notes |
|-------|---------:|-------|
| `intro` | varies (49% Panel, 94% DBC) | First paragraphs |
| `sections` | 12-81% | h2/h3 sectioned body |
| `intro_tables` / `intro_code_blocks` | 0-90% | Tabular / code fragments in intro |
| `property_references` (Panel only) | 62.3% | Control property names, symbol refs |

## 6. Known Quality Issues (read before relying on data)

| ID | Issue | Workaround |
|----|-------|------------|
| K1 | v15 parser misclassifies ~80% of pages as `notes` because v15 CHM extracts lack `MadCap:targetName` divs. | Use `category` + sub-folder to disambiguate. Look at `syntax[0]` to confirm a function page. |
| K2 | "CAN Message Selectors" / "CAN Error Frame Selectors" are tagged `notes` but are really `selector` pages. | Read `selectors` field; content is there. |
| K3 | v12 had `parameters` coverage of 3.9% originally; `scripts/patches/v12_params.py` brought it to 81.3%. | Trust `parameters` field; the patch is in-place. (As of 2026-06-10, the v2 parser is also fixed, so new extractions don't need this patch.) |
| K4 | Panel pages have **0% `intro_code_blocks`** — Panel docs describe UI, not code. | Use `property_references` field (62.3% coverage). |
| K5 | v15 `return` field empty on ~52% of functions despite having type in `syntax[0]`. | Read `syntax[0]` and parse the leading token as return type. |
| K6 | Vector path encoding shows replacement chars (`\udc94`) in some Panel `property_references`. | Strip non-printable chars before display. |
| K7 | diagnostics/ is **synthetic** (only 4 hand-curated pages). | Supplement with `extras/team/CAPL_Internal_Coding_Standards.json` and `Common_Gotchas.json`. |
| K8 | Semantic vector search is optional and disabled by default. | Use `agent_kb/` indexes plus BM25 (`artifacts/bm25.pkl`); enable vector mode only for explicit local embedding experiments. |
| K9 | Some `notes` pages contain huge tables that summarise many functions (e.g. `CAN CAPL Functions` lists all 67 CAN functions). | Read these as "function index" pages; the actual function pages are siblings. |
| K10 | `notes` type is ambiguous — could be: overview, function list, glossary, deprecated info. | Check `tables[]` content; multiple tables of name+description = function list. |

## 7. Authority and Provenance

- All `knowledge/v12/`, `knowledge/v15/` content is **derived from Vector's official CHM help**,
  processed by [`scripts/extract/v2/`](../scripts/extract/v2/) and (historically) patched by
  [`scripts/patches/`](../scripts/patches/). The v2 parser has been fixed (2026-06-10)
  so new extractions do not require the patches.
- All `extras/team/` content is **hand-curated by the EQ07 team** (the test case asks
  about). Treat as authoritative for the project, secondary for general CANoe questions.
- `diagnostics/` is **synthetic** (authored 2026-06-08 by workflow T05).
- `L3_diffs/` shows version-by-version changes; use to check if a v12 API still exists in v15.

## 8. How to extend

- **Add a single page** → put JSON in `extras/<topic>/<sub>/<name>.json`, then
  `python -m retriever.add_knowledge add <path>`.
- **Add a new version** → see [`docs/CHM_ACQUISITION.md`](../docs/CHM_ACQUISITION.md), then
  `python scripts/extract/v3/run_all.py --version vN --chm-root ../chm_extract_vN`.
- **Add a new topic** → see `retriever/README.txt` "Adding Knowledge" section.

## 9. Pointers for agents

- [`query_routing.md`](./query_routing.md) — "I have question Q, where do I look?"
- [`unified_index.json`](./unified_index.json) — `id → file path` lookup
- [`symbol_aliases.json`](./symbol_aliases.json) — CAPL function name → page
- [`schema_v3.json`](./schema_v3.json) — JSON shape of one page
