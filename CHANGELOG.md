# Changelog

## 2026-06-16

### Added

- Added CANoe CFG generation support through the official CANoe COM Automation path.
  - Generates `<project>.cfg.generate.ps1` beside each workflow run.
  - Opens a discovered/base CFG when available, mounts DBC/CDD/A2L/DLL inputs where COM interfaces support them, and delegates final `.cfg` serialization to CANoe `Configuration.SaveAs`.
  - Keeps base CFG copy fallback because CANoe `.cfg` internals are proprietary and version-specific.
- Added scoped workflow knowledge profiles:
  - `canoe_config` exposes only CANoe configuration, CFG, and COM automation facts.
  - `capl_authoring` exposes CAPL/XCP/diagnostics facts and blocks CFG/COM automation topics.
- Added local CANoe COM automation knowledge pages and workflow pack metadata under `knowledge_base/`.
- Added `analyze_test_coverage` to the Burr workflow.
  - Produces `coverage_report.json`.
  - Reports requirement, feature, domain, source-model, and CAPL evidence coverage.
  - Preserves multiple requirement IDs for repeated rows under the same test case ID.
- Added an external CAPL authoring agent boundary.
  - Controlled by `--capl-authoring-mode deterministic|llm|llm_with_fallback`.
  - Uses `CANOE_GENE_CAPL_AGENT_COMMAND` when configured.
  - Writes `capl_authoring_payload.json` and expects `capl_authoring_response.json`.
  - Falls back to the deterministic renderer in `llm_with_fallback` mode.
- Added regression tests for CDD parsing, CFG parsing/source discovery, CANoe adapter script generation, retrieval profile isolation, coverage reporting, and the CAPL authoring agent adapter.

### Changed

- `generate_canoe_config` now emits COM automation metadata, CFG generation plans, and automation scripts instead of treating CFG output as only a TODO plan.
- `generate_capl_script` now consumes `coverage_report` and records authoring mode, profile, evidence refs, coverage summary, and fallback/agent result in `capl_script_plan.json`.
- Workflow profile metadata now includes the coverage analysis action and CAPL authoring mode.
- Template mapping and template builder now include CAPL authoring modes.
- Documentation now describes external CAPL authoring agent command placeholders and response schema.

### Validation

- `python -m unittest workflows.canoe_auto_generation_burr.test_cdd_parser workflows.canoe_auto_generation_burr.test_cfg_parser workflows.canoe_auto_generation_burr.test_vector_canoe_adapter workflows.canoe_auto_generation_burr.test_retrieval_profiles workflows.canoe_auto_generation_burr.test_capl_authoring_agent`
- `python -B workflows\canoe_auto_generation_burr\validate_workflow_profile.py`
- `python -m compileall workflows\canoe_auto_generation_burr`
- `python knowledge_base\workflow_kb\validate_workflow_kb.py`
- Sample workflow runs completed with `E:\Canoe_Gene\TempleFile` inputs.

### Known Limits

- Automated CANoe `SaveAs` and CAPL compilation were not run against a live Vector project in this change set.
- Without `CANOE_GENE_CAPL_AGENT_COMMAND`, `llm_with_fallback` mode intentionally records the unavailable external agent and uses the deterministic CAPL renderer.
- Generated workflow outputs under `generated_projects/` and Excel `.xlsx` binaries are excluded from the committed source changes.
