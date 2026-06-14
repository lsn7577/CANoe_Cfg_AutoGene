# Knowledge Base FAQ

## General

### Q: What is this knowledge base?
A: A long-term maintained structured knowledge base of Vector CANoe 12.0 / 15.0 (and future 17/18) help documentation. It is optimized for agent use: exact symbol indexes, scenario routing, BM25 candidate retrieval, and structured grounding. The calling agent performs semantic understanding and answer synthesis.

### Q: What's the data schema?
A: Each page is a JSON file with these fields: `page_type` (function/method/event/selector/concept/notes), `name`, `syntax`, `description`, `parameters`, `return`, `example`, `availability`, `selectors`, plus page-type-specific fields. A rendered `.md` is also written alongside.

### Q: How is the data extracted?
A: Vector's HTML help (CHM-extracted) is parsed by template-aware parsers in `scripts/extract/v2/` (or `scripts/extract/v3/` for new versions). v15 uses MadCap/HTML5 templates; v12 uses flat tables. See `docs/CHM_ACQUISITION.md` for adding new versions.

## Indexing & Retrieval

### Q: How do I rebuild the index?
A: `python -m retriever.build` (takes 12-14 seconds for 10K docs).

### Q: Why are some v15 CAPL functions missing return values?
A: The v15 parser relies on `MadCap:targetName` divs which are missing in some CHM extracts. The `scripts/patches/v15_simple.py` workaround now extracts return types directly from signature syntax (improved from 35.3% to 48.1% coverage as of 2026-06-08). Note: as of 2026-06-10 the v2 parser has been fixed (`01_vector_parser.py:detect_page_type()`) so new extractions will not need this patch.

### Q: Why are v12 parameters sparse?
A: This was a parser bug. Fixed by `scripts/patches/v12_params.py` (now 81.3% coverage, was 3.9%). The v2 parser was also updated so new extractions don't need this patch.

### Q: Why does Panel have 0% code blocks?
A: Panel documentation describes UI controls (GUI components), not APIs. The "code-like" content is property names, symbol references, and configuration groups. We capture these in the new `property_references` field (62.3% coverage as of 2026-06-08).

## Adding Knowledge

### Q: How do I add a single doc?
A: `python -m retriever.add_knowledge add ./my_doc.json` - stages to `extras/` and indexes.

### Q: How do I add a directory of docs?
A: `python -m retriever.add_knowledge add-dir ./my_docs/`

### Q: How do I add a new CANoe version (e.g. v18)?
A: 1) Acquire `CANoeCANalyzer_v18.chm` (see `docs/CHM_ACQUISITION.md`)
2) Extract: `7z x CANoeCANalyzer_v18.chm -o../chm_extract_v18`
3) Run: `python scripts/extract/v3/run_all.py --version v18 --chm-root ../chm_extract_v18`
4) Rebuild: `python -m retriever.build`
5) Refresh agent_kb views: `python agent_kb/build_manifest.py`
6) (Optional) Update `knowledge/latest` junction: `rmdir knowledge\latest && mklink /J knowledge\latest knowledge\v18` (admin required on Windows)

### Q: How do I add a new topic (e.g. Security)?
A: 1) Create `knowledge/v15/security/structured/` (and per-version)
2) Add to `retriever/config.py` KNOWN_TOPICS
3) Add extraction driver or use `extras/team/` for hand-curated docs
4) Rebuild index

## Troubleshooting

### Q: `rank_bm25 is not installed` error
A: `python -m pip install -r requirements.txt` (use the SAME python that runs `python -m retriever.build`)

### Q: Why is my new doc not found in search?
A: 1) Check `artifacts/manifest.json` has it: `python -m retriever.serve --info`
2) Try query: `python -m retriever.serve --query "your doc name"`
3) If still missing, check page_type is one of: function/method/event/selector/concept

### Q: How do I measure retrieval quality?
A: Run `python -m retriever.tests.test_smoke` for basic smoke tests.
For real precision@k evaluation, use `python -m retriever.serve --query "..." --top-n 5` and manually check.

### Q: Why does `manifest.json` show `vector_backend: disabled`?
A: That is the expected default. This project is now agent-first: BM25 returns candidate pages and grounded facts, then the agent decides semantic relevance.

### Q: Do I need HuggingFace, torch, sentence-transformers, or chromadb?
A: No for the default workflow. They are only needed if you explicitly enable optional local vector search with `python -m retriever.build --with-vector`.
