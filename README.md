# CANoe_Gene Workspace

This workspace contains the knowledge base, Excel test-case template, and Burr
workflow used to generate CANoe automated test project artifacts.

See `CHANGELOG.md` for the latest workflow changes.

## Directory Map

```text
F:/Canoe_Gene/
  CANoeCANalyzer.chm
  knowledge_base/
  templates/
  workflows/
  generated_projects/
  docs/
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
  repair plans, and final manifests.

- `docs/`  
  Workspace-level architecture and evaluation reports.

## Generated Outputs

- `generated_projects/`  
  Workflow run outputs. These are reproducible artifacts and can be regenerated
  from the template and workflow.

## Current Main Workflow

```powershell
cd F:\Canoe_Gene
python -m workflows.canoe_auto_generation_burr.canoe_workflow `
  --excel F:\Canoe_Gene\templates\canoe_test_case_template\CANoe自动化测试用例模板.xlsx `
  --out F:\Canoe_Gene\generated_projects\EQ07_workflow_test `
  --capl-authoring-mode llm_with_fallback `
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
- `<project>.cfg.plan.json`: CANoe configuration generation plan.
- `<project>.cfg.generate.ps1`: CANoe COM Automation script for CFG SaveAs.
- `<project>_TestModule.can`: generated CAPL test module.
- `capl_script_plan.json`: CAPL authoring plan, evidence refs, coverage summary,
  adapter gaps, and LLM/fallback result.

## Key Maintenance Commands

```powershell
# Rebuild the Excel template
& "C:\Users\Administrator\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe" `
  F:\Canoe_Gene\templates\canoe_test_case_template\build_template.mjs

# Validate workflow knowledge references
python F:\Canoe_Gene\knowledge_base\workflow_kb\validate_workflow_kb.py

# Validate workflow_profile.json against the executable Burr graph
python F:\Canoe_Gene\workflows\canoe_auto_generation_burr\validate_workflow_profile.py

# Compile workflow Python files
python -m compileall F:\Canoe_Gene\workflows\canoe_auto_generation_burr
```

Useful workflow flags:

- `--strict-source-validation`: missing or unresolved DBC/A2L/CDD semantics
  become blocking errors and produce `repair_plan.json`.
- `--canoe-validation-mode disabled|manual|automated`: controls the Vector
  CANoe external validation adapter. Disabled/manual never claim CANoe compile
  success.
- `--capl-authoring-mode deterministic|llm|llm_with_fallback`: controls CAPL
  generation. `llm_with_fallback` writes an external-agent payload and falls
  back to the deterministic renderer when no agent is configured.
- `--tracking`: enables Burr local tracking for action-level debugging.

## CAPL Authoring Agent

The CAPL generation step can call an external KB-indexed LLM agent without
giving it access to the whole repository or full knowledge base. Set
`CANOE_GENE_CAPL_AGENT_COMMAND` to a command that reads a JSON payload and writes
a JSON response:

```powershell
$env:CANOE_GENE_CAPL_AGENT_COMMAND = 'python F:\tools\capl_agent.py "{payload}" "{response}"'
```

The workflow writes `capl_authoring_payload.json` and expects the command to
write `capl_authoring_response.json`:

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

If the command is not configured and `--capl-authoring-mode llm_with_fallback`
is used, the workflow records the unavailable agent in `capl_script_plan.json`
and uses the deterministic renderer.

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

`F:/Canoe_Gene/templates/canoe_test_case_template/template_field_mapping.json`
