# Scripts

> All scripts that build / maintain / measure the knowledge base.

## Layout

```
scripts/
├── extract/
│   ├── v2/                  # Template-aware parsers (v15 MadCap, v12 flat-table)
│   │   ├── 01_vector_parser.py        # v15 MadCap CAPL function/event/method/selector
│   │   ├── 02_render_md.py            # JSON → Markdown
│   │   ├── 03_extract_v15_structured.py   # v15 CAPL driver
│   │   ├── 04_extract_structured.py   # Generic CAPL driver
│   │   ├── 05_vector_parser_v12.py    # v12 flat-table CAPL parser
│   │   ├── 06_concept_parser.py       # Panel / DBC concept page parser
│   │   ├── 07_extract_concept.py      # Panel / DBC concept driver
│   │   └── run_all.py                 # v12 + v15 full pipeline (v2 entry point)
│   └── v3/
│       ├── README.md
│       └── run_all.py                 # Version-parameterized pipeline (NEW versions)
├── patches/                  # One-off fixes for known extraction bugs
│   ├── v12_params.py         # v12 parameters coverage 3.9% → 81.3% (already applied)
│   ├── v15_simple.py         # v15 return/selectors 35.3% → 48.1% (already applied)
│   ├── v15_return_sel.py     # v15 return/selectors alternative patch
│   └── panel_props.py        # Panel property_references field (already applied)
└── benchmark/                # RAG demo + benchmark
    ├── rag_demo_v1.py        # Original (recall@5 = 42.9%) — kept for history
    └── rag_demo_v2.py        # Improved (recall@5 = 90%) — current
```

## Common workflows

### Re-extract existing v12/v15 (rarely needed)

```bash
python scripts/extract/v2/run_all.py
```

This calls `03_extract_v15_structured.py` for v15 CAPL, then runs v12 + concept
extractors. Output goes to `knowledge/v12/` and `knowledge/v15/`.

### Extract a NEW CANoe version (v17, v18, ...)

```bash
# 1. Acquire CHM and extract to disk (see CHM_ACQUISITION.md at repo root)
# 2. Run the parameterized pipeline
python scripts/extract/v3/run_all.py \
    --version v17 \
    --chm-root ../chm_extract_v17

# 3. Refresh retriever indices
python -m retriever.build

# 4. Refresh agent_kb views
python agent_kb/build_manifest.py
```

The v3 pipeline reuses the v2 parsers (no code duplication). It auto-detects
`CANoeCANalyzer/Topics/CAPLFunctions/`, `VectorToolsEnvironment/Topics/PanelDesigner/`,
and `CANeds/Topics/` under the chm-root.

### Re-run a patch (rarely needed; patches are already applied in-place)

```bash
python scripts/patches/v12_params.py
python scripts/patches/v15_simple.py
python scripts/patches/panel_props.py
```

These patches are historical. The v2 parser has been fixed (2026-06-10) so
that **new extractions will not need them**. They are kept only as a safety net
in case anyone wants to re-process the raw CHM HTM files.

### Run the RAG benchmark

```bash
python scripts/benchmark/rag_demo_v2.py --benchmark
```

Output: `artifacts/rag_benchmark.json`. See `RAG_BENCHMARK_REPORT.md` (now
in `docs/`) for the historical 42.9% → 90% progression.

## Status (2026-06-10)

- ✅ `extract/v2/` — 8 scripts, fully working, all 4 known bugs fixed in `01_vector_parser.py:detect_page_type()`
- ✅ `extract/v3/` — 1 script, ready for v17+ versions (just need CHM)
- ⚠️  `patches/` — historical; safe to re-run but not needed
- ✅ `benchmark/` — current state: recall@5 = 90%, latency p50 = 18ms

See [CHANGELOG.md](../CHANGELOG.md) for the complete history.
