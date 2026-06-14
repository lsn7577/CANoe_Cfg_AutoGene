# Knowledge Base Deployment Guide

## Hardware Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| CPU | 4 cores | 8+ cores |
| RAM | 4 GB | 8 GB |
| Disk | 5 GB | 10 GB SSD |
| GPU | — | Not required |

## Software Requirements

- Python 3.9+ (tested with 3.14)
- pip packages:
  ```
  pip install -r requirements.txt
  # Optional MCP:
  pip install mcp
  # For re-extraction:
  pip install lxml beautifulsoup4
  ```

## Environment Setup

```bash
# 1. Clone or copy this knowledge_base directory
# 2. Install Python deps
python -m pip install -r requirements.txt

# 3. Build default model-free index (BM25 + manifest)
cd <knowledge_base>
python -m retriever.build

# 4. Verify
python -m retriever.serve --query "setSignal" --version v15 --top-n 3
```

## Running the Services

### CLI REPL
```bash
python -m retriever.serve
```
Interactive Q&A mode. Type `:info` for index stats, `:quit` to exit.

### One-shot query
```bash
python -m retriever.serve --query "CAN error frame" --version v15 --top-n 5
```

### HTTP API server
```bash
python -m retriever.serve --serve --port 8765

# In another terminal:
curl "http://127.0.0.1:8765/search?q=setSignal&version=v15&top_n=3"
```

### MCP server (for Claude/Cursor integration)
```bash
python -m retriever.mcp_server
```
Then configure your MCP client to connect via stdio. Available tools: `search_canoe`, `canoe_info`, `canoe_add`, `canoe_remove`.

## Production Checklist

- [ ] Python 3.9+ installed
- [ ] All pip packages installed
- [ ] `python -m retriever.build` completed successfully
- [ ] `artifacts/bm25.pkl` exists (35MB)
- [ ] `artifacts/manifest.json` shows correct doc count
- [ ] Smoke test passed: `python -m retriever.serve --query "setSignal"` returns results
- [ ] `<knowledge_backup>/` exists with source code
- [ ] Git initialized (optional but recommended)
- [ ] HTTP API exposed via reverse proxy (nginx/Caddy) if needed
- [ ] MCP server reachable for agent integrations

## Optional Vector Enhancement

The default deployment is agent-first and does not use HuggingFace models. Only
enable local semantic vectors for explicit experiments:

```bash
python -m pip install -r requirements-optional.txt
$env:RETRIEVER_ALLOW_MODEL_DOWNLOAD = "1"
python -m retriever.build --with-vector --embedding-model BAAI/bge-m3
$env:RETRIEVER_ENABLE_VECTOR = "1"
$env:RETRIEVER_EMBEDDING_MODEL = "BAAI/bge-m3"
```

## Performance Tuning

Edit `retriever/config.py`:
```python
@dataclass
class RetrievalConfig:
    bm25_top_k: int = 60
    fused_top_k: int = 20
```

## Monitoring

The system has no built-in monitoring. Quick health check:
```bash
# 1. Check indices exist
ls -la artifacts/

# 2. Check doc count
python -c "import json; print(json.load(open('artifacts/manifest.json'))['n_docs'])"

# 3. Spot check
python -m retriever.serve --query "setSignal" --top-n 1
```

## Backup Strategy

| Component | Frequency | Method |
|-----------|-----------|--------|
| `knowledge/` JSON data | Daily | rsync to NAS/S3 |
| `artifacts/bm25.pkl` | On rebuild | Same as knowledge |
| `extras/team/` internal docs | On edit | Git commit |
| `retriever/` source code | On change | Git commit |
| `scripts/extract/v2/` | On change | Git commit |
| `scripts/extract/v3/` | On change | Git commit |
| `scripts/patches/` | On change | Git commit |
| `scripts/benchmark/` | On change | Git commit |
| `agent_kb/` (incl. pre-built indexes) | On rebuild | Git commit |

Keep source backups outside the active workspace, for example `<knowledge_backup>/`.

## Disaster Recovery

1. Restore `knowledge/` from latest snapshot
2. Restore `artifacts/` (or rebuild: `python -m retriever.build`)
3. Restore `extras/` and `retriever/` from Git
4. Verify: `python -m retriever.tests.test_smoke`
