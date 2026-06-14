# extract_v3 — Version-Parameterized Extraction Pipeline

> Created 2026-06-08 (workflow T02)
> Replaces the version-hardcoded `extract_v2/` with a single `run_all.py` that takes `--version` and `--chm-root` arguments.

## Why v3?

Older extraction scripts had hardcoded paths like:
```python
V15_CAPL_DIR = Path("../chm_extract_v15/CANoeCANalyzer/Topics/CAPLFunctions")
```
Adding a new version required copying 8 files and editing constants. v3 unifies everything into one script.

## Usage

```bash
# 1. Acquire CHM (see CHM_ACQUISITION.md)
# 2. Extract CHM with hh.exe or 7-Zip
hh.exe -decompile ../chm_extract_v17 CANoeCANalyzer_v17.chm
# or:
7z x CANoeCANalyzer_v17.chm -o../chm_extract_v17

# 3. Run pipeline
python scripts/extract/v3/run_all.py \
    --version v17 \
    --chm-root ../chm_extract_v17

# 4. Rebuild index
python -m retriever.build

# 5. Switch latest
# Linux/Mac: ln -sfn v17 knowledge/latest
# Windows (admin): rmdir knowledge\latest && mklink /J knowledge\latest knowledge\v17
```

## Arguments

| Flag | Required | Default | Description |
|------|:--------:|---------|-------------|
| `--version` | ✓ | — | e.g. `v17`, `v18`, `v18sp3` |
| `--chm-root` | ✓ | — | CHM-extracted root (must contain `CANoeCANalyzer/Topics/CAPLFunctions` and/or `VectorToolsEnvironment/Topics/PanelDesigner`) |
| `--kb-root` | ✗ | `<knowledge_base>/knowledge` | Knowledge base root |
| `--topics` | ✗ | `capl panel dbc xcp` | Topics to extract |
| `--parser-template` | ✗ | `v15` | `v15` (HTML5/MadCap) or `v12` (CHM flat-table) |

## Directory Layout Required in CHM-Root

```
chm_extract_v17/
├── CANoeCANalyzer/Topics/CAPLFunctions/  (CAPL source)
│   ├── CAN/
│   ├── Diagnostics/
│   ├── ...
│   └── XCP/
├── VectorToolsEnvironment/Topics/PanelDesigner/  (Panel source)
│   ├── Elements/
│   ├── General/
│   └── ...
└── CANeds/Topics/  (DBC source)
    ├── Document/
    ├── messages/
    └── ...
```

## Output

```
knowledge/v17/
├── _index.json
├── capl/
│   ├── _index.json
│   └── structured/
│       ├── CAN/
│       │   ├── setSignal.json
│       │   └── setSignal.md
│       └── ...
├── panel/...
├── dbc/...
└── xcp/...
```

## Rollback / Diff

After extraction, generate version diff vs the previous latest:

```bash
# (future: python scripts/diff/compare.py --v-prev v15 --v-new v17)
# Output: L3_diffs/diff_*_v15_to_v17.json
```
