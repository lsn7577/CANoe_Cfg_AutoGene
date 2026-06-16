# CANoe_Gene Workspace

This workspace contains the knowledge base, Excel test-case template, and Burr
workflow used to generate CANoe automated test project artifacts.

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
  workflow knowledge contracts.

- `templates/canoe_test_case_template/`  
  Maintained Excel test-case template, shared field mapping, and generator
  script.

- `workflows/canoe_auto_generation_burr/`  
  Apache Burr workflow implementation for parsing the Excel template and
  producing structured test cases, source models, CANoe configuration plans,
  CAPL test module source, evaluation reports, repair plans, and final
  manifests.

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
  --out F:\Canoe_Gene\generated_projects\EQ07_workflow_test
```

Each run is isolated under `generated_projects/<project>/runs/<run_id>`. The
base output directory keeps `latest_run_manifest.json` as a pointer to the most
recent run.

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
- `--tracking`: enables Burr local tracking for action-level debugging.

## Shared Template Mapping

Excel dropdown values and Burr workflow validation enums share one source:

`F:/Canoe_Gene/templates/canoe_test_case_template/template_field_mapping.json`
