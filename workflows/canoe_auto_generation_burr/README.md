# CANoe Auto Generation Burr Workflow

This package contains the executable Burr workflow for CANoe test-project
generation. The current architecture overview is maintained in
`../../docs/ARCHITECTURE_CURRENT.md`.

## Purpose

The workflow turns the maintained Excel test-case template into traceable CANoe
generation artifacts:

1. Parse Excel project, channel, strategy, and test-step sheets.
2. Validate template fields against the canonical mapping.
3. Parse declared DBC/A2L/CDD/CFG source files.
4. Validate test-case rows and source-object references.
5. Retrieve grounded CANoe/CAPL/team-rule evidence from `knowledge_base`.
6. Analyze requirement, feature, domain, source, and evidence coverage.
7. Gate CAPL API evidence.
8. Generate a CANoe configuration plan and COM Automation script.
9. Evaluate CANoe configuration through the Vector/CANoe adapter boundary.
10. Generate CAPL through a KB-indexed LLM planner/fixer loop.
11. Run CAPL static lint and optional CANoe/vTESTstudio compile feedback.
12. Package outputs or emit correction workbooks, Markdown, repair plans, and
    HTML reports.

The workflow does not hand-write Vector's private `.cfg` serialization format.
It delegates real CFG SaveAs/load/compile work to CANoe COM Automation when
`--canoe-validation-mode automated` is used on a machine where CANoe is
available.

## Files

```text
workflows/canoe_auto_generation_burr/
  canoe_workflow.py              # Burr actions, transitions, CLI
  workflow_profile.json          # Profile checked against executable graph
  validate_workflow_profile.py   # profile-vs-code consistency check
  action_contract_sync.py        # workflow_kb/profile/registry consistency helper
  canonical_ir.py                # Chinese display fields -> stable field IDs
  source_parser.py               # DBC/A2L/CDD/CFG parsers
  vector_canoe_adapter.py        # CFG generation and CAPL compile adapter boundary
  capl_lexer_lint.py             # local CAPL lexer/static lint
  correction_workbook.py         # blocked-run correction XLSX/Markdown
  html_report.py                 # run_report.html generation
  run_retention.py               # generated run cleanup policies
  agents/
    capl_authoring_agent.py      # planner/fixer payloads and command adapter
    claude_code_capl_agent.py    # Claude Code CLI adapter
    llm_agent_config.json        # agent prompt/config defaults
```

## Current Graph

`workflow_profile.json` currently validates against 14 Burr actions and 19
transitions:

```text
load_test_case_template -> validate_template_contract -> parse_source_files
-> validate_test_cases -> retrieve_evidence -> analyze_test_coverage
-> validate_evidence_gate -> generate_canoe_config -> evaluate_canoe_config
-> generate_capl_script -> evaluate_capl_script -> package_outputs
```

Failure edges from template/test/evidence/config/CAPL gates enter
`plan_repair`, which either retries config/CAPL generation or emits correction
outputs via `emit_test_case_corrections`.

## Run

From the repository root:

```powershell
python -m workflows.canoe_auto_generation_burr.canoe_workflow `
  --excel .\templates\canoe_test_case_template\CANoe自动化测试用例模板.xlsx `
  --out .\generated_projects\EQ07_workflow_test `
  --capl-authoring-mode llm `
  --canoe-validation-mode disabled
```

Outputs are written to `generated_projects/<project>/runs/<run_id>`. The base
output directory keeps `latest_run_manifest.json`.

Useful options:

```powershell
# Fail on missing declared DBC/A2L/CDD files or unresolved used objects.
python -m workflows.canoe_auto_generation_burr.canoe_workflow `
  --excel .\templates\canoe_test_case_template\CANoe自动化测试用例模板.xlsx `
  --out .\generated_projects\EQ07 `
  --strict-source-validation

# Require manual CANoe review instead of treating external validation as disabled.
python -m workflows.canoe_auto_generation_burr.canoe_workflow `
  --excel .\templates\canoe_test_case_template\CANoe自动化测试用例模板.xlsx `
  --out .\generated_projects\EQ07 `
  --canoe-validation-mode manual

# Run automated CANoe CFG/CAPL validation where Vector CANoe COM is available.
python -m workflows.canoe_auto_generation_burr.canoe_workflow `
  --excel .\templates\canoe_test_case_template\CANoe自动化测试用例模板.xlsx `
  --out .\generated_projects\EQ07 `
  --canoe-validation-mode automated `
  --capl-compile-max-attempts 5
```

## CAPL Authoring Agent

`generate_capl_script` uses a two-role external CAPL authoring protocol:

- Planner runs once and returns immutable `golden_ir`.
- Fixer runs in the compile loop with exactly three changing inputs:
  `golden_ir`, current complete CAPL source, and the latest compile error log.

Default command:

```powershell
$env:CANOE_GENE_CAPL_AGENT_COMMAND = 'python -m workflows.canoe_auto_generation_burr.agents.claude_code_capl_agent "{payload}" "{response}"'
$env:CANOE_GENE_CLAUDE_CODE_COMMAND = 'claude.cmd'
```

Per-role overrides:

- `CANOE_GENE_CAPL_PLANNER_COMMAND`
- `CANOE_GENE_CAPL_FIXER_COMMAND`

Compile override:

- `CANOE_GENE_CAPL_COMPILE_COMMAND`

The compile override must write JSON to `{report}`. Passing reports use
`{"status": "pass", "message": "..."}`. Failing reports use `{"status":
"failed", "message": "compiler diagnostics..."}`.

## Validation

Preferred check bundle from the repository root:

```powershell
python .\ci\run_checks.py
```

Direct checks:

```powershell
python -B .\knowledge_base\workflow_kb\validate_workflow_kb.py
python -B .\workflows\canoe_auto_generation_burr\validate_workflow_profile.py
python -m unittest `
  workflows.canoe_auto_generation_burr.test_cdd_parser `
  workflows.canoe_auto_generation_burr.test_cfg_parser `
  workflows.canoe_auto_generation_burr.test_vector_canoe_adapter `
  workflows.canoe_auto_generation_burr.test_retrieval_profiles `
  workflows.canoe_auto_generation_burr.test_capl_authoring_agent `
  workflows.canoe_auto_generation_burr.test_claude_code_capl_agent
```

## Extension Points

- Replace `source_parser.py` parsers with team-owned DBC/A2L/CDD parsers.
- Extend `knowledge_base/workflow_kb/retrieval_profiles/` when adding new
  knowledge scopes.
- Bind generated `CanoeGene_*` CAPL stubs to project-specific XCP and
  diagnostics libraries.
- Extend `vector_canoe_adapter.py` for project-specific CANoe load/compile
  reporting.
- Keep `workflow_profile.json` synchronized with every action/transition
  change.
