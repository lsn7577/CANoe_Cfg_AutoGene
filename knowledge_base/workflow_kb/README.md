# Workflow KB

`workflow_kb` is the extensibility layer for Burr-based CANoe test generation.
It does not replace `knowledge/`, `agent_kb/`, or `retriever/`.

- `knowledge/` is the authoritative extracted Vector CANoe documentation.
- `agent_kb/` is the agent-facing lookup and routing layer.
- `workflow_kb/` is the workflow contract layer: state schemas, action
  contracts, packs, generation patterns, and validation gates.

## Design Goal

The Burr graph should stay small and stable while the knowledge base and
workflow behavior evolve through configuration. New domains should be added as
packs. New workflow steps should be added as action contracts. Generated output
must be traceable to an evidence bundle.

## Directory Layout

```text
workflow_kb/
  workflow_manifest.json
  schemas/
  burr_actions/
  packs/
  retrieval_profiles/
  generation_patterns/
  validation_rules/
  indexes/
  validate_workflow_kb.py
```

## How Burr Should Use This Layer

1. Load `workflow_manifest.json`.
2. Register action contracts from `burr_actions/`.
3. Load enabled packs from `packs/*/pack.json`.
4. Build a graph profile by enabling pack-defined scenarios, retrieval
   profiles, generation patterns, and validation rules.
5. Persist the Burr run with:
   - workflow manifest version
   - enabled pack ids and versions
   - knowledge snapshot id
   - evidence bundle id

## Stable State Keys

The default workflow uses these state keys:

- `raw_test_case`
- `test_case_ir`
- `intent_profile`
- `retrieval_plan`
- `evidence_bundle`
- `project_spec`
- `generated_artifacts`
- `validation_report`
- `repair_plan`
- `final_package`

Action implementations should read and write only the keys declared in their
contract. This keeps the graph replayable and easy to extend.

## Adding A New Domain Pack

Create `packs/<domain>/pack.json` and optional companion files:

```text
packs/<domain>/
  pack.json
  scenarios.json
  retrieval_profile.json
  validation_rules.json
  examples/
  tests/
```

Then add the new pack path to `workflow_manifest.json`. Run:

```powershell
python workflow_kb\validate_workflow_kb.py
```

## Adding A New Burr Action

1. Add `burr_actions/<nn>_<action_id>.json`.
2. Declare `reads`, `writes`, gates, and transitions.
3. Register it in `workflow_manifest.json`.
4. Add a replay fixture under the relevant pack's `tests/` directory.

Do not put CAPL syntax, project-specific wrappers, or CANoe facts directly in
the Burr action code. Retrieve them through `agent_kb` and record them in
`evidence_bundle`.

## Gate Rules

Before packaging a CANoe project, the workflow must pass:

- every generated CAPL API call has evidence
- the requested CANoe version is named and checked
- team overrides have been loaded when code is generated
- all required artifacts in `project_spec` are present
- unresolved facts are either repaired or explicitly marked as assumptions

