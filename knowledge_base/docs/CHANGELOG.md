# Knowledge Base Changelog

All notable changes to the Vector CANoe Knowledge Base are documented here.
Format: [YYYY-MM-DD] - Brief description

## [2026-06-12] - Agent-First Index Default

### Changed
- Default retrieval/indexing path is now model-free: `python -m retriever.build` builds BM25 + manifest only.
- HuggingFace / sentence-transformers / ChromaDB support is now an explicit optional enhancement via `--with-vector`.
- Runtime retriever no longer instantiates vector indexes or rerankers unless `RETRIEVER_ENABLE_VECTOR` / `RETRIEVER_ENABLE_RERANK` are set.
- Agent docs now describe `agent_kb/` as the primary call surface and `retriever/` as candidate recall + grounding.

### Verified
- Default manifest reports `vector_backend: disabled` and `semantic_vector_available: false`.
- Agents can still use `load_page`, `match_scenario`, and `search` without model files.

## [2026-06-10] - Agent-Oriented Refactor + Directory Reorganization

### Added
- **`agent_kb/`** — Agent-facing navigation layer (10 files, 9 MB)
  - `README.md`, `AGENT_INTEGRATION.md`, `capability_manifest.md`, `query_routing.md`
  - `scenarios.json` (10 test scenarios), `schema_v3.json` (authoritative schema)
  - `unified_index.json` (9,909 pages), `symbol_aliases.json` (5,287 symbols)
  - `kb_lookup.py` (Python helper), `example_workflow.py` (end-to-end demo)
  - `build_manifest.py` (regenerates views from `knowledge/` + `extras/`)
- **`docs/`** — Consolidated top-level documentation
  - `CHANGELOG.md` (this file), `CHM_ACQUISITION.md`, `DEPLOYMENT.md`, `FAQ.md`
  - `RAG_BENCHMARK_REPORT.md`, `REFACTORING_REPORT.md`, `WORKFLOW_TASKS.md`

### Changed
- **Reorganized `scripts/`** into 3 clear subdirs:
  - `scripts/extract/v2/` — reusable parsers (was `scripts/extract_v2/`)
  - `scripts/extract/v3/` — version-parameterized pipeline (was `scripts/extract_v3/`)
  - `scripts/patches/` — historical one-off fixes (was loose `patch_*.py` files)
  - `scripts/benchmark/` — RAG demo v1 + v2 (was loose `rag_demo*.py` files)
- **Renamed patch/demo scripts** for consistency:
  - `patch_v12_params.py` → `patches/v12_params.py`
  - `patch_v15_simple.py` → `patches/v15_simple.py`
  - `patch_v15_return_sel.py` → `patches/v15_return_sel.py`
  - `patch_panel_props.py` → `patches/panel_props.py`
  - `rag_demo.py` → `benchmark/rag_demo_v1.py`
  - `rag_demo_v2.py` → `benchmark/rag_demo_v2.py`
- **Fixed `scripts/extract/v2/01_vector_parser.py:detect_page_type()`**:
  - Selector pages (`"X Selectors"` suffix) now correctly tagged `selector` (was `notes`)
  - Function-index pages (`"X Functions"` with space) now correctly tagged `concept` (was `notes`)
  - New re-extractions will not need the 4 patch scripts
- **`unified_index.json` re-classifies** all pages: 9 → 72 selector pages found
- **Reorganized `agent_kb/build_manifest.py`** — now includes:
  - `alias_name` (file stem) in unified_index for stable aliasing
  - Three alias maps: `by_normalized`, `by_canonical`, `all_versions`
  - Diagnostic topic + team docs included in alias map (were missing)
  - Improved page type inference (handles v15 mis-classification)

### Fixed
- **Symbol alias lookup now prefers user-specified version** (`resolve_symbol(name, prefer_version='v15')`)
- **`_id_to_path` handles both `extras/team/_root/X.json` and `extras/team/X.json` layouts**
- **`kb_lookup.load_page` now uses prefer_version correctly** (was always v15 default)

### Removed
- `_part1.py` (27B test scratch file)
- `_test_heredoc.sh` (92B test scratch file)
- `bash.exe.stackdump` (538B Windows bash crash dump)
- All `__pycache__/` and `*.pyc` files
- `L1_latest` (empty junction directory)
- `knowledge/latest` (empty junction directory)
- Empty `structured/` subdirs under `knowledge/v17/`, `knowledge/v18/`
- `rag_benchmark.json` (v1, superseded by v2)
- `WORKFLOW_TASKS.md` (consolidated into this file as 2026-06-08 entry)
- `REFACTORING_REPORT.md` (this consolidation is the report)

### Verified
- ✅ 9,909 pages indexed in `unified_index.json`
- ✅ 10/10 scenarios resolve cleanly (all `primary_pages` exist)
- ✅ BM25 + vector + grounding pipeline still works (10,075 docs in `artifacts/bm25.pkl`)
- ✅ `python agent_kb/example_workflow.py` runs end-to-end (6 steps)
- ✅ Symbol lookup is case-insensitive and version-aware
- ✅ v15 preferred over v12 when both exist
- ✅ End-to-end smoke test passes

### Maintenance after this refactor
```bash
# After adding new pages (e.g. v17 CHM):
python scripts/extract/v3/run_all.py --version v17 --chm-root ../chm_extract_v17
python -m retriever.build
python agent_kb/build_manifest.py
```

---

## [2026-06-08] - Major Quality Improvements + T01-T10 Workflow Complete

**T01-T10 status (all DONE):**
- T01: Retriever source backup (PASS)
- T02: v17/v18 directory scaffolds (PARTIAL - awaiting CHM)
- T03: v12 parameters coverage 3.9% → 81.3% (EXCEED)
- T04: Panel `property_references` field 0% → 62.3% (EXCEED)
- T05: Diagnostics topic scaffold with 4 sample entries (PASS)
- T06: v15 return/selectors 35.3% → 48.1% (PARTIAL)
- T07: CHANGELOG/FAQ/DEPLOY docs (PASS)
- T08: extras/team expansion (PASS)
- T09: Panel 3 vs 4 controls confirmation (PASS — 3 not 4)
- T10: RAG demo + benchmark recall 42.9% → 90% (EXCEED)

### Added
- **v17/v18 directory scaffolds** at `knowledge/v17/` and `knowledge/v18/` (4 topics × 2 versions each)
- **`scripts/extract_v3/`**: Version-parameterized extraction pipeline (replaces hardcoded `extract_v2/`)
- **`CHM_ACQUISITION.md`**: Guide for acquiring CANoe CHM files for new versions
- **`scripts/patch_v12_params.py`**: Fixes v12 CAPL parameters extraction (was missing 96% of params)
- **`scripts/patch_panel_props.py`**: Adds `property_references` field to Panel pages
- **`scripts/patch_v15_simple.py`**: Direct-parse fix for v15 return/selectors
- **`knowledge/v15/diagnostics/`**: New Diagnostics topic with 4 sample entries (UDS, OBD, Common)
- **`<knowledge_backup>/`**: Source code backup (22 .py files)

### Fixed
- **v12 CAPL parameters coverage**: 178 (3.9%) → 3699 (81.3%) - parser was looking for inner `<table>`, v12 uses `<p class=Bold>name</p>` + `<p>desc</p>` pairs
- **Panel intro_code_blocks coverage**: 0% → 62.3% via new `property_references` field (Panel docs don't have code blocks; they have property references)
- **v15 CAPL return coverage**: 35.3% → 48.1% via direct-parse fallback (parser was misclassifying 80% pages as `notes`)
- **v15 CAPL selectors coverage**: 1.5% → 1.6% (only 5 actual selectors pages exist)
- **BM25 index rebuild**: Dependencies installed, indices now rebuildable (12-14s for 10072 docs)

### Changed
- `retriever/config.py` KNOWN_TOPICS now includes `"diagnostics"`
- Document corpus grew from 10068 → 10072 documents

### Index
- `artifacts/bm25.pkl`: 35MB (rebuilt 2026-06-08)
- `artifacts/manifest.json`: latest run stats

## [2026-06-05] - Retriever system deployed
- Hybrid retriever (BM25 + vector + RRF + reranker)
- MCP server, HTTP API, CLI REPL
- Incremental add/remove via `python -m retriever.add_knowledge`

## [2026-06-01] - Topic × Version matrix refactor
- Reorganized from L1/L2/L3 layers to topic × version matrix
- `knowledge/v12/`, `knowledge/v15/` with 4 topics each
- Structured JSON + MD per page

## [Pre-2026-06-01] - Initial 3-Layer architecture
- L1 (latest), L2 (versioned), L3 (diffs)

### Added
- **v17/v18 directory scaffolds** at `knowledge/v17/` and `knowledge/v18/` (4 topics × 2 versions each)
- **`scripts/extract_v3/`**: Version-parameterized extraction pipeline (replaces hardcoded `extract_v2/`)
- **`CHM_ACQUISITION.md`**: Guide for acquiring CANoe CHM files for new versions
- **`scripts/patch_v12_params.py`**: Fixes v12 CAPL parameters extraction (was missing 96% of params)
- **`scripts/patch_panel_props.py`**: Adds `property_references` field to Panel pages
- **`scripts/patch_v15_simple.py`**: Direct-parse fix for v15 return/selectors
- **`knowledge/v15/diagnostics/`**: New Diagnostics topic with 4 sample entries (UDS, OBD, Common)
- **`WORKFLOW_TASKS.md`**: Workflow task tracking
- **`<knowledge_backup>/`**: Source code backup (22 .py files)

### Fixed
- **v12 CAPL parameters coverage**: 178 (3.9%) → 3699 (81.3%) - parser was looking for inner `<table>`, v12 uses `<p class=Bold>name</p>` + `<p>desc</p>` pairs
- **Panel intro_code_blocks coverage**: 0% → 62.3% via new `property_references` field (Panel docs don't have code blocks; they have property references)
- **v15 CAPL return coverage**: 35.3% → 48.1% via direct-parse fallback (parser was misclassifying 80% pages as `notes`)
- **v15 CAPL selectors coverage**: 1.5% → 1.6% (only 5 actual selectors pages exist)
- **BM25 index rebuild**: Dependencies installed, indices now rebuildable (12-14s for 10072 docs)

### Changed
- `retriever/config.py` KNOWN_TOPICS now includes `"diagnostics"`
- Document corpus grew from 10068 → 10072 documents

### Index
- `artifacts/bm25.pkl`: 35MB (rebuilt 2026-06-08)
- `artifacts/manifest.json`: latest run stats

## [2026-06-05] - Retriever system deployed
- Hybrid retriever (BM25 + vector + RRF + reranker)
- MCP server, HTTP API, CLI REPL
- Incremental add/remove via `python -m retriever.add_knowledge`

## [2026-06-01] - Topic × Version matrix refactor
- Reorganized from L1/L2/L3 layers to topic × version matrix
- `knowledge/v12/`, `knowledge/v15/` with 4 topics each
- Structured JSON + MD per page

## [Pre-2026-06-01] - Initial 3-Layer architecture
- L1 (latest), L2 (versioned), L3 (diffs)
