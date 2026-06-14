# Agent-First Retriever

`retriever/` provides candidate recall and grounding for the Vector CANoe
knowledge base. The default path is model-free: BM25 returns candidate pages,
then `grounding.py` reloads the source JSON and exposes canonical facts for the
calling agent to synthesize.

Use `agent_kb/` first for scenario routing, exact symbol lookup, and agent
protocol rules. Use this package when you need free-form candidate search, an
HTTP endpoint, an MCP tool surface, or index rebuilds.

## Default Workflow

```powershell
# Rebuild the default BM25 index and manifest.
python -m retriever.build

# Run one query from the CLI.
python -m retriever.serve --query "setSignal" --version v15 --top-n 3

# Start the interactive REPL.
python -m retriever.serve

# Run smoke tests.
python -m retriever.tests.test_smoke
```

The default build writes:

- `artifacts/bm25.pkl`
- `artifacts/manifest.json`

No embedding model, vector database, or reranker is required by default.

## Python API

```python
from retriever.retriever import HybridRetriever

retr = HybridRetriever.build_from_disk()
hits = retr.retrieve(
    "how to send a CAN frame",
    version="v15",
    topic="capl",
    top_n=5,
)

for hit in hits:
    facts = hit["grounded_facts"]
    print(facts["source"], facts["syntax"], facts["description"])
```

Each hit includes `_meta` timing and route information plus `grounded_facts`
extracted from the source page.

## Main Modules

| File | Purpose |
| --- | --- |
| `build.py` | Builds BM25 and optional vector artifacts from `knowledge/` and `extras/`. |
| `retriever.py` | Main `HybridRetriever` orchestration. |
| `bm25_index.py` | BM25 index wrapper and persistence. |
| `classifier.py` | Lightweight query route classification: exact, semantic, hybrid. |
| `grounding.py` | Reloads source JSON and extracts canonical facts. |
| `serve.py` | CLI, REPL, and small HTTP `/search` server. |
| `mcp_server.py` | Optional MCP tool surface. |
| `ingest.py` | Incremental add/remove helpers for knowledge files. |
| `add_knowledge.py` | CLI wrapper for staging project/team documents. |
| `vector_index.py` | Optional vector backend, disabled unless explicitly enabled. |

## HTTP API

```powershell
python -m retriever.serve --serve --port 8765
```

Query:

```text
http://127.0.0.1:8765/search?q=setSignal&version=v15&topic=capl&top_n=5
```

The response is JSON containing the same hit objects returned by
`HybridRetriever.retrieve()`.

## MCP Surface

```powershell
python -m retriever.mcp_server
```

If the MCP SDK is installed, this exposes:

- `search_canoe(query, version, topic, page_type, top_n)`
- `canoe_info()`
- `canoe_add(paths)`
- `canoe_remove(doc_id)`

Without the MCP SDK, the module remains importable and the `tool_*` functions
can be called directly from Python.

## Optional Vector Mode

Vector search is an explicit opt-in path for local embedding experiments.

```powershell
$env:RETRIEVER_ENABLE_VECTOR = "1"
python -m retriever.build --with-vector --embedding-model BAAI/bge-m3
python -m retriever.serve --query "panel gauge binding"
```

Optional reranking can be enabled separately:

```powershell
$env:RETRIEVER_ENABLE_RERANK = "1"
$env:RETRIEVER_RERANK_MODEL = "BAAI/bge-reranker-base"
```

If optional dependencies or model files are unavailable, keep the default BM25
path.

## Adding Knowledge

Use `agent_kb/build_manifest.py` and `retriever.build` after adding source
pages. For team/project notes, stage JSON files through the helper:

```powershell
python -m retriever.add_knowledge schema
python -m retriever.add_knowledge add .\my_team_doc.json
python -m retriever.add_knowledge add-dir .\internal_docs
python -m retriever.build
```

Team/project documents live under `extras/` and can be searched with
`topic="extras"`.

## Grounding Rules

- Treat search hits as candidates.
- Use `grounded_facts` or load the source page before using syntax,
  parameters, selectors, properties, examples, or return values.
- Prefer exact symbol lookup through `agent_kb.kb_lookup.load_page()` when the
  API name is known.
- Keep project overrides from `extras/team/` separate from generic Vector facts
  until synthesis.

## Verification

Run the standard checks after code or index changes:

```powershell
python scripts\validate_kb.py
python tests_integration\test_agent_retrieval_contract.py
python -m retriever.tests.test_smoke
python -m compileall agent_kb retriever scripts tests_integration
```

The expected default manifest reports `vector_backend: disabled` and
`semantic_vector_available: false`.
