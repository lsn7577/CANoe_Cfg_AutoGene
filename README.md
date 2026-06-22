# CANoe_Gene Workspace

This workspace contains the knowledge base, Excel test-case template, and Burr
workflow used to generate CANoe automated test project artifacts.

Current architecture details are maintained in
`docs/ARCHITECTURE_CURRENT.md`. The older reports in `docs/` remain useful as
historical evaluations, but the current source of truth is the code plus the
architecture document.

See `CHANGELOG.md` for the latest workflow changes.

## Directory Map

```text
CANoe_Cfg_AutoGene/
  CANoeCANalyzer.chm
  ci/
  docs/
  knowledge_base/
  templates/
  workflows/
  generated_projects/   # local regenerated outputs, git-ignored
```

## Environment Dependencies

Required to run the default workflow and knowledge-base checks:

- Windows with Python 3.9+.
- `burr` for the workflow state machine.
- `rank_bm25`, `jieba`, and `lxml` for the default model-free knowledge-base retriever.
- Git LFS when cloning the repository, because `CANoeCANalyzer.chm` and `knowledge_base/artifacts/bm25.pkl` are LFS-managed files.

Install the required Python packages with the same Python used to run the workflow:

```powershell
python -m pip install -r requirements.txt
```

Optional dependencies:

- Node.js is only needed when rebuilding `templates/canoe_test_case_template/CANoe自动化测试用例模板.xlsx`.
- Vector CANoe plus a project-specific adapter is only needed for real CFG loading or CAPL compilation. With `--canoe-validation-mode disabled`, the workflow does not require CANoe and reports external validation as skipped.
- `knowledge_base\requirements-optional.txt` is only for explicit vector/rerank/MCP experiments; the default path does not need embedding models.

## Long-Term Assets

- `knowledge_base/`  
  Vector CANoe/CAPL knowledge base, agent-facing indexes, retrieval tools, and
  workflow knowledge contracts. The workflow uses scoped profiles so CANoe CFG
  generation retrieves `canoe_config` facts, while CAPL authoring retrieves
  `capl_authoring` facts.

- `templates/canoe_test_case_template/`  
  Maintained Excel test-case template, shared field mapping, and generator
  script.

- `workflows/canoe_auto_generation_burr/`  
  Apache Burr workflow implementation for parsing the Excel template and
  producing structured test cases, source models, coverage reports, CANoe
  configuration plans/scripts, CAPL test module source, evaluation reports,
  correction workbooks, HTML run reports, repair plans, and final manifests.
  Supporting modules split out source parsing, CAPL lexer linting, report
  generation, run retention, canonical field IDs, and external CAPL agent
  adapters.

- `ci/`  
  Local validation entry points. `python ci/run_checks.py` validates the Burr
  profile, workflow knowledge references, Python syntax, and retrieval profile
  isolation.

- `docs/`  
  Workspace-level architecture and evaluation reports.

## Generated Outputs

- `generated_projects/`  
  Workflow run outputs. These are reproducible artifacts, are ignored by Git,
  and can be regenerated from the template and workflow.

## Current Main Workflow

```powershell
cd E:\Canoe_Gene\CANoe_Cfg_AutoGene
python -m workflows.canoe_auto_generation_burr.canoe_workflow `
  --excel .\templates\canoe_test_case_template\CANoe自动化测试用例模板.xlsx `
  --out .\generated_projects\EQ07_workflow_test `
  --capl-authoring-mode llm `
  --canoe-validation-mode disabled
```

Each run is isolated under `generated_projects/<project>/runs/<run_id>`. The
base output directory keeps `latest_run_manifest.json` as a pointer to the most
recent run.

Main generated artifacts include:

- `structured_test_cases.json`: parsed Excel test-case IR.
- `source_models.json`: lightweight DBC/A2L/CDD/CFG/DLL source model summary.
- `evidence_bundle.json`: CAPL API evidence retrieved through the active KB
  profile.
- `coverage_report.json`: requirement, feature, domain, source, and evidence
  coverage summary.
- `<project>.cfg`: copied base CFG or CANoe-generated CFG when automation runs.
- `<project>.cfg.todo.json`: configuration plan when no base/generated CFG is
  available.
- `<project>.cfg.plan.json`: CANoe configuration generation plan.
- `<project>.cfg.generate.ps1`: CANoe COM Automation script for CFG SaveAs.
- `<project>_TestModule.can`: generated CAPL test module.
- `capl_script_plan.json`: CAPL authoring plan, evidence refs, coverage summary,
  adapter gaps, and LLM agent result.
- `run_report.html`: HTML summary for human review.
- `test_case_corrections.xlsx` / `.md`: correction package when the run is
  blocked.

## Key Maintenance Commands

```powershell
# Rebuild the Excel template
node .\templates\canoe_test_case_template\build_template.mjs

# Validate workflow knowledge references
python .\knowledge_base\workflow_kb\validate_workflow_kb.py

# Validate workflow_profile.json against the executable Burr graph
python .\workflows\canoe_auto_generation_burr\validate_workflow_profile.py

# Compile workflow Python files
python -m compileall .\workflows\canoe_auto_generation_burr

# Run the project check bundle
python .\ci\run_checks.py
```

Useful workflow flags:

- `--strict-source-validation`: missing or unresolved DBC/A2L/CDD semantics
  become blocking errors and produce `repair_plan.json`.
- `--canoe-validation-mode disabled|manual|automated`: controls the Vector
  CANoe external validation adapter. Disabled/manual never claim CANoe compile
  success.
- `--capl-authoring-mode llm`: requires the external LLM agent path for CAPL
  generation. Planner/Fixer commands can be split with environment overrides.
- `--capl-compile-max-attempts N`: maximum Planner/Fixer compile-repair
  attempts inside `generate_capl_script`.
- `--quality-gate exploration|release`: release mode rejects unbound
  `CanoeGene_*` adapter stubs.
- `--tracking`: enables Burr local tracking for action-level debugging.

## Latest Validation

Run from the repository root:

```powershell
py -3.9 ci\run_checks.py
```

Last verified locally on 2026-06-22 (Python 3.9, `burr 0.40.2`):

- `validate_workflow_profile.py` → 14 actions / 19 transitions, profile 与代码一致。
- `validate_workflow_kb.py` → 30 references, 0 missing, 0 invalid JSON。
- `py_compile` → 20 个 `.py` 文件全部通过。
- `test_retrieval_profiles.py` → 2 个用例通过。
- `python -m unittest discover -s workflows/canoe_auto_generation_burr -p "test_*.py"` → 26/26 通过。

> `burr==0.40.2` 当前不支持 Python 3.14；推荐使用 `py -3.9`。

## CAPL Authoring Agent

The CAPL generation step can call an external KB-indexed LLM agent without
giving it access to the whole repository or full knowledge base. The repository
ships a Claude Code adapter at
`workflows/canoe_auto_generation_burr/agents/claude_code_capl_agent.py`:

```powershell
$env:CANOE_GENE_CAPL_AGENT_COMMAND = 'python -m workflows.canoe_auto_generation_burr.agents.claude_code_capl_agent "{payload}" "{response}"'
$env:CANOE_GENE_CLAUDE_CODE_COMMAND = 'claude.cmd'
```

`generate_capl_script` uses two roles. Planner runs once and returns immutable
`golden_ir`; Fixer runs in the compile loop and receives only `golden_ir`, the
current complete CAPL source, and the latest compile error log. Optional
`CANOE_GENE_CAPL_PLANNER_COMMAND` and `CANOE_GENE_CAPL_FIXER_COMMAND` override
the shared command per role.

Planner response:

```json
{
  "golden_ir": {
    "project": {},
    "channels": [],
    "cases": [],
    "capl_api_plan": [],
    "assertions": [],
    "branching": [],
    "evidence_refs": []
  }
}
```

Fixer response:

```json
{
  "capl_source": "complete .can source",
  "capl_script_plan": {
    "assumptions": [],
    "adapter_gaps": [],
    "used_evidence_refs": [],
    "cases": []
  }
}
```

If the command is not configured, the workflow records the unavailable agent in
`capl_script_plan.json` and emits an `llm_failed` CAPL artifact for evaluation.

The Claude Code adapter accepts these optional overrides:

- `CANOE_GENE_CLAUDE_CODE_MODEL`
- `CANOE_GENE_CLAUDE_CODE_EFFORT`
- `CANOE_GENE_CLAUDE_CODE_TIMEOUT_SECONDS`
- `CANOE_GENE_CLAUDE_CODE_EXTRA_ARGS`

To feed CANoe compile diagnostics back to Fixer, set automated validation. The
workflow writes and runs an internal PowerShell COM script that opens the
generated CFG when available, attaches the CAPL file, tries
`Configuration.RunCompilation`, `Configuration.Compile`, then
`$canoe.CAPL.Compile()`, and reads diagnostics from the available
compile-result COM object:

```powershell
python -m workflows.canoe_auto_generation_burr.canoe_workflow `
  --excel .\templates\canoe_test_case_template\CANoe自动化测试用例模板.xlsx `
  --out .\generated_projects\EQ07_workflow_test `
  --canoe-validation-mode automated `
  --capl-compile-max-attempts 5
```

`CANOE_GENE_CAPL_COMPILE_COMMAND` remains available as an override hook. When
set, it must write JSON to `{report}` with `status: "pass"` or `status:
"failed"`. Only the latest failed compile report is passed into the next Fixer
prompt.

## CANoe CFG Generation

The workflow does not hand-write Vector's private `.cfg` serialization format.
It discovers a base CFG when available, prepares a `.cfg.plan.json`, and emits a
PowerShell COM Automation script that opens CANoe, mounts supported DBC/CDD/A2L
and DLL inputs, then calls CANoe `Configuration.SaveAs`.

With `--canoe-validation-mode disabled`, the script is generated but not run.
Use `--canoe-validation-mode automated` only on a machine where CANoe COM
Automation is available and the project can be safely opened.

## Shared Template Mapping

Excel dropdown values and Burr workflow validation enums share one source:

`templates/canoe_test_case_template/template_field_mapping.json`
