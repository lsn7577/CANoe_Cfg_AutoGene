# Query Routing — Where to Look for What

> **Purpose**: Given a question, this document tells the agent exactly which file(s) to read.
> Use it as a **decision tree** before falling back to full search.

## 0. Global decision tree

```
Is the question about a SPECIFIC named symbol/API/function?
  ├── YES → Read symbol_aliases.json  ──►  get page path  ──►  read .json
  └── NO  ↓

Is the question about a CONCEPT/EXPLANATION (not a specific call)?
  ├── YES → Use retriever.serve or kb_lookup.search for candidate pages, then read grounded facts
  └── NO  ↓

Is the question about a VERSION DIFFERENCE (v12 vs v15)?
  └── YES → Read L3_diffs/DIFF_REPORT.md and diff_summary_v12_to_v15.json
```

## 1. By Domain

### 1.1 CAPL function call: "How do I call X(...)?"

| Question pattern | Where to look |
|------------------|---------------|
| "How do I set a CAN signal value?" | `knowledge/v15/capl/structured/SignalAccess/setSignal.json` (or `setSignalFloat`, etc.) |
| "How to send a CAN frame?" | `knowledge/v15/capl/structured/CAN/output (CAN).json` |
| "How to subscribe to a CAN message?" | `knowledge/v15/capl/structured/CAN/on message.json` |
| "How to use sysvars?" | `knowledge/v15/capl/structured/SystemVariables/` |
| "How to write a test case?" | `knowledge/v15/capl/structured/Test/` (e.g., `TestWaitForSignalMatch.json`) |
| "How to use XCP calibration?" | `knowledge/v15/xcp/structured/` |
| "FlexRay / LIN / Ethernet APIs?" | `knowledge/v15/capl/structured/{FlexRay,LIN,IP,...}/` |
| "obsolete / deprecated functions?" | `knowledge/v15/capl/structured/Obsolete/` |
| "non-bus-specific utilities (math, I/O)?" | `knowledge/v15/capl/structured/Other/` |

### 1.2 CAPL selector: "What selectors are available for X?"

| Question pattern | Where to look |
|------------------|---------------|
| "CAN message selectors (ID, DLC, RTR, TIME, ...)" | `knowledge/v15/capl/structured/CAN/CAN Message Selectors.json` (note: page_type=notes, see K2) |
| "CAN error frame selectors" | `knowledge/v15/capl/structured/CAN/CAN Error Frame Selectors.json` |
| "timer.* selectors" | `knowledge/v15/capl/structured/Other/Timer Selectors.json` (if present) |
| "DiagRequest/Response selectors" | `knowledge/v15/capl/structured/Diagnostics/` |
| "sysvar.* selectors" | `knowledge/v15/capl/structured/SystemVariables/` |

> Note: many of these "selectors" pages are mis-tagged as `notes`; the actual data is
> in the `selectors` field as a list of `{name, description, type}`. Read it directly.

### 1.3 CAPL event: "What event fires when X happens?"

| Question pattern | Where to look |
|------------------|---------------|
| "On CAN message receive" | `knowledge/v15/capl/structured/CAN/on message.json` |
| "On key press in panel" | `knowledge/v15/capl/structured/Other/on key.json` |
| "On timer expiry" | `knowledge/v15/capl/structured/Other/on timer.json` |
| "On bus-off / error frame" | `knowledge/v15/capl/structured/CAN/on errorFrame.json` |
| "On signal change" | `knowledge/v15/capl/structured/CAN/on signal.json` |
| "On env-var change" | `knowledge/v15/capl/structured/Other/on envVar.json` |
| "On measurement start/stop" | `knowledge/v15/capl/structured/Other/on start.json`, `on stop.json` |

### 1.4 Panel Designer (UI / HMI)

| Question pattern | Where to look |
|------------------|---------------|
| "What controls exist?" | `knowledge/v15/panel/structured/Elements/` (33 controls) |
| "How to configure Button?" | `knowledge/v15/panel/structured/Elements/Button.json` |
| "How to access Panel from CAPL?" | `knowledge/v15/panel/structured/General/Access Panels using CAPL Functions.json` |
| "Ribbon / Window layout?" | `knowledge/v15/panel/structured/{Ribbon,Windows}/` |
| "How to bind a symbol to a control?" | `knowledge/v15/panel/structured/General/Displaying assigned Symbols.json` |

### 1.5 DBC (database editor)

| Question pattern | Where to look |
|------------------|---------------|
| "What keywords are available?" | `knowledge/v15/dbc/structured/Glossar/Glossary.json` + `menus/` |
| "How to add a new signal attribute?" | `knowledge/v15/dbc/structured/object_attributes/` |
| "Signal description syntax" | `knowledge/v15/dbc/structured/signal_descriptions/` |
| "Tab pages for multi-frame signals" | `knowledge/v15/dbc/structured/tab_pages/` |

### 1.6 Diagnostics (UDS/KWP/OBD)

| Question pattern | Where to look |
|------------------|---------------|
| "Send UDS request" | `knowledge/v15/diagnostics/structured/UDS/UDS_Overview.json` (look at `property_references.services` for SID list) |
| "0x27 SecurityAccess flow" | `knowledge/v15/diagnostics/structured/UDS/SecurityAccess_DID.json` |
| "Read DTCs" | `knowledge/v15/diagnostics/structured/OBD/` or `knowledge/v15/capl/structured/Diagnostics/` (DiagGetDTC functions) |
| "Common diagnostic functions" | `knowledge/v15/diagnostics/structured/Common/` |

### 1.7 Team / project conventions (most important for test generation!)

| Question pattern | Where to look |
|------------------|---------------|
| "Our coding standards" | `extras/team/CAPL_Internal_Coding_Standards.json` |
| "Common gotchas / pitfalls" | `extras/team/Common_Gotchas.json` |
| "CI pipeline / vTESTstudio / Jenkins" | `extras/team/CI_Pipeline_Reference.json` |
| "Our internal setSignalDword wrapper" | `extras/team/canSetSignalDword.json` |
| "Panel Gauges usage" | `extras/team/panelGauges.json` |

## 2. By Question Type

### "How do I...?" (how-to)
→ `capl/structured/<Category>/` (look for the function name; or use retriever search)
→ `panel/structured/General/` for UI how-tos

### "What is the syntax for X?"
→ `capl/structured/<Category>/<X>.json` — read `syntax` field
→ If empty, check `L3_diffs/` for version changes

### "What's the difference between v12 and v15?"
→ `L3_diffs/diff_summary_v12_to_v15.json` (high-level)
→ `L3_diffs/diff_capl_v12_to_v15.json` (per-function adds/removes)
→ `L3_diffs/PANEL_V12_VS_V15.md` (Panel elements comparison)

### "Why doesn't my code work?" (debugging)
→ `extras/team/Common_Gotchas.json` (most common EQ07 pitfalls)
→ `capl/structured/Other/` (utility functions; check return value handling)
→ Search retriever with symptom phrase

### "Generate a CAPL test for X"
→ `capl/structured/Test/` (Test* / ChkCreate_* / ChkStart_* functions)
→ `extras/team/CAPL_Internal_Coding_Standards.json` (naming + style rules)
→ `extras/team/CI_Pipeline_Reference.json` (CI integration)

### "Generate a Panel .xvp file"
→ `panel/structured/Elements/<Control>.json` (control properties)
→ `extras/team/panelGauges.json` (binding patterns)

### "Generate a DBC file"
→ `dbc/structured/Glossar/Glossary.json` (keyword reference)
→ `dbc/structured/menus/` (editor menus)
→ `L3_diffs/diff_dbc_v12_to_v15.json` (new keywords in v15)

## 3. Quick-lookup files (read first)

If you don't know where to start, **read these in order**:

1. [`rules_doc.md`](./rules_doc.md) — "what retrieval protocol must I follow?"
2. [`rules_policy.md`](./rules_policy.md) — machine-readable JSON answer gate
3. [`capability_manifest.md`](./capability_manifest.md) — "does the KB know about X?"
4. [`symbol_aliases.json`](./symbol_aliases.json) — "is X a known CAPL function? what's its page?"
5. [`unified_index.json`](./unified_index.json) — "give me all pages related to Y"
6. The retriever (`HybridRetriever.retrieve()`) — for fuzzy/Chinese candidate recall

## 4. Search tips

- Use **version** filter explicitly: `version="v15"` (default) avoids v12 hits.
- Use **topic** filter: `topic="capl"` keeps the search within CAPL functions only.
- Use **page_type** filter: `page_type="function"` excludes overviews and concept pages.
- BM25 is keyword-strong; works well for English CAPL identifiers (`setSignal`, `BusLoad`).
- Natural-language queries use BM25 candidate recall by default; the agent reads the returned grounded facts and performs semantic selection.
- Always read the rendered `.md` next to the `.json` for human-readable context.

## 5. Anti-patterns (do NOT do)

- ❌ Don't re-parse the raw CHM HTM files — use the structured JSON.
- ❌ Don't iterate all 10K JSON files to "find X" — use the retriever or unified_index.
- ❌ Don't trust `page_type: notes` pages for "is this a function" — check `syntax` field.
- ❌ Don't ignore `extras/team/` — it contains **project-specific overrides** the team agreed on.
- ❌ Don't fabricate CAPL syntax not in the KB — only use syntax strings from `syntax[]` field.
