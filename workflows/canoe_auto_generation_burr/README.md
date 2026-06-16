# CANoe Auto Generation Burr Workflow

This workflow is derived from:

- `C:/Users/Administrator/Documents/Obsidian Vault/Canoe自动生成工作流.canvas`
- `F:/Canoe_Gene/templates/canoe_test_case_template/CANoe自动化测试用例模板.xlsx`

It turns the Excel test-case template into a Burr state machine that follows
the user's agent flow:

1. Test case inspection
2. Structured test case output or correction items
3. Source model parsing for DBC/A2L/CDD inputs
4. Knowledge evidence retrieval from `agent_kb`
5. Evidence gate validation
6. CANoe configuration generation plan
7. CANoe configuration evaluation
8. CAPL test module source generation
9. CAPL static lint and external validation adapter evaluation
10. Repair plan or final package output

The current implementation is intentionally adapter-friendly. It performs
template contract validation, lightweight source semantic checks, KB evidence
gating, conservative CAPL rendering, static lint, and explicit Vector/CANoe
external-validation status reporting. Real binary CFG rendering and automated
CANoe/vTESTstudio compilation are still project-specific adapter hooks; the
workflow reports them as `skipped`, `manual_required`, or `failed`, never as
successful unless the adapter actually performs the work.

## Files

```text
workflows/canoe_auto_generation_burr/
  canoe_workflow.py            # Burr actions and graph builder
  vector_canoe_adapter.py      # CANoe validation/compile adapter boundary
  validate_workflow_profile.py # profile-vs-code consistency check
  workflow_profile.json        # Graph/state/action contract summary
  template_field_mapping.json  # Excel field names and enumerations
```

## Run

```powershell
cd F:\Canoe_Gene
python -m workflows.canoe_auto_generation_burr.canoe_workflow `
  --excel F:\Canoe_Gene\templates\canoe_test_case_template\CANoe自动化测试用例模板.xlsx `
  --out F:\Canoe_Gene\generated_projects\EQ07
```

Outputs are written to `F:\Canoe_Gene\generated_projects\EQ07\runs\<run_id>`.
The base output directory keeps `latest_run_manifest.json`.

Useful options:

```powershell
# Fail if declared DBC/A2L/CDD files are missing or cannot resolve used objects
python -m workflows.canoe_auto_generation_burr.canoe_workflow `
  --excel F:\Canoe_Gene\templates\canoe_test_case_template\CANoe自动化测试用例模板.xlsx `
  --out F:\Canoe_Gene\generated_projects\EQ07 `
  --strict-source-validation

# Require manual CANoe review instead of treating external validation as disabled
python -m workflows.canoe_auto_generation_burr.canoe_workflow `
  --excel F:\Canoe_Gene\templates\canoe_test_case_template\CANoe自动化测试用例模板.xlsx `
  --out F:\Canoe_Gene\generated_projects\EQ07 `
  --canoe-validation-mode manual

# Prefer an external KB-indexed CAPL LLM agent, but fall back to deterministic rendering
python -m workflows.canoe_auto_generation_burr.canoe_workflow `
  --excel F:\Canoe_Gene\templates\canoe_test_case_template\CANoe自动化测试用例模板.xlsx `
  --out F:\Canoe_Gene\generated_projects\EQ07 `
  --capl-authoring-mode llm_with_fallback
```

## External CAPL Authoring Agent

`generate_capl_script` can delegate CAPL writing to an external LLM agent through
`CANOE_GENE_CAPL_AGENT_COMMAND`. The workflow writes
`capl_authoring_payload.json`, runs the command, then reads
`capl_authoring_response.json`.

Command placeholders:

- `{payload}`: JSON request path.
- `{response}`: JSON response path that the external agent must write.

The response must contain:

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

Modes:

- `deterministic`: use the built-in conservative renderer only.
- `llm`: require the external agent; failures flow into CAPL evaluation.
- `llm_with_fallback`: try the external agent, then use the deterministic renderer
  if the agent is unavailable or fails validation.

The workflow can be imported by another application:

```python
from workflows.canoe_auto_generation_burr.canoe_workflow import build_application

app = build_application({
    "test_case_excel_path": r"F:\Canoe_Gene\templates\canoe_test_case_template\CANoe自动化测试用例模板.xlsx",
    "output_root": r"F:\Canoe_Gene\generated_projects\EQ07",
})
result = app.run(halt_after=["package_outputs", "emit_test_case_corrections"])
```

## Validation

```powershell
python -B F:\Canoe_Gene\knowledge_base\workflow_kb\validate_workflow_kb.py
python -B F:\Canoe_Gene\workflows\canoe_auto_generation_burr\validate_workflow_profile.py
python -B -m workflows.canoe_auto_generation_burr.canoe_workflow `
  --excel F:\Canoe_Gene\templates\canoe_test_case_template\CANoe自动化测试用例模板.xlsx `
  --out F:\Canoe_Gene\generated_projects\EQ07_workflow_test
```

## Extension Points

- Replace `generate_canoe_config` or `vector_canoe_adapter.py` with a real
  CANoe CFG renderer/validator.
- Replace lightweight source parsers with team-owned DBC/A2L/CDD parsers.
- Extend `retrieve_evidence` when new Excel operation/condition/result types
  require additional CAPL APIs or team rules.
- Bind the `CanoeGene_*` CAPL adapter stubs to project-specific XCP and
  diagnostics libraries.
- Extend `evaluate_capl_script` with CANoe/vTESTstudio compilation and coverage
  checks.
- Extend `template_field_mapping.json` when the Excel template changes.
