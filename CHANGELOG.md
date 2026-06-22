# Changelog

## 2026-06-22

### Added

- `workflows/canoe_auto_generation_burr/canonical_ir.py`: 中文 Excel
  字段到稳定英文 canonical ID 的映射。新代码优先使用 canonical ID。
- `workflows/canoe_auto_generation_burr/source_parser.py`: DBC
  （`cantools` 优先 + regex 回退）、A2L、CDD、CFG 独立 parser 模块。
  `canoe_workflow` 内的内嵌 parser 改为优先调用此处。
- `workflows/canoe_auto_generation_burr/capl_lexer_lint.py`: 增强的 CAPL
  静态 lint，覆盖 headers、变量块、testcase 计数、废弃 API、括号、缺失
  分号、重复 testcase、空函数体、event handler 检查。
- `workflows/canoe_auto_generation_burr/correction_workbook.py`: 阻塞
  运行时的 `.xlsx` 修正工作簿（红/黄高亮）和 Markdown 错误清单。
- `workflows/canoe_auto_generation_burr/html_report.py`: 自包含的
  `run_report.html`（summary cards、覆盖率、修正、repair、artifact 链接）。
- `workflows/canoe_auto_generation_burr/run_retention.py`: 数量 + 时长
  双策略运行目录清理，永不删除 `latest_run_manifest.json` 所指运行。
- `workflows/canoe_auto_generation_burr/action_contract_sync.py`: 校验
  `burr_actions/*.json` / `workflow_profile.json` /
  `ACTION_REGISTRY` / `TRANSITION_SPECS` 三处 action 契约的一致性。
- `workflows/canoe_auto_generation_burr/agents/claude_code_capl_agent.py`:
  Claude Code CLI 适配器，封装 payload/response、JSON Schema 约束、
  命令解析、模型/超时/extra_args 注入。
- `workflows/canoe_auto_generation_burr/test_claude_code_capl_agent.py`:
  Claude Code agent 的 split command、fixer 协议、payload 路径等单测。
- `ci/run_checks.py`: 本地 CI 验证入口，跑 `validate_workflow_profile`、
  `validate_workflow_kb`、全量 `py_compile`、`test_retrieval_profiles`。

### Changed

- `workflows/canoe_auto_generation_burr/canoe_workflow.py`:
  - 移除旧的 `_capl_authoring_mode` / `_capl_string` / `_capl_numeric` /
    `_duration_from_text` / `_render_capl_*` / `_deterministic_capl_render`
    等 CAPL 内联渲染函数。
  - 新增 `_capl_compile_max_attempts`、`_compile_error_log`、
    `_classify_external_failure`、`_mount_capl_into_cfg`、typed-rule
    加载、KB 检索 profile 解析等辅助函数。
  - 测试用例类型规则从代码改为从
    `knowledge_base/workflow_kb/validation_rules/test_case_field_rules.json`
    加载；新增类型无需修改 Python。
  - `generate_capl_script` 接入 LLM Planner/Fixer 双角色协议与 CANoe COM
    编译反馈循环。
- `workflows/canoe_auto_generation_burr/vector_canoe_adapter.py`:
  - 新增 `compile_capl`：外部命令覆盖、CANoe COM 编译回退
    （`Configuration.RunCompilation` / `Configuration.Compile` /
    `$canoe.CAPL.Compile()`）、`DIALOG_SUPPRESSOR` 弹窗抑制后台作业。
  - 新增 `write_cfg_verify_script`：CFG 装载并核对挂载数量。
  - `SaveAs` / `Save` 改为 try/catch 链式回退。
  - 新增 `CANOE_GENE_CAPL_COMPILE_COMMAND`、
    `CANOE_GENE_CAPL_COMPILE_TIMEOUT_SECONDS` 等环境变量。
- `workflows/canoe_auto_generation_burr/agents/capl_authoring_agent.py`:
  - 重写为 Planner / Fixer 双角色协议。
  - 角色命令优先级：env > JSON override > JSON backend > default。
  - Planner 一次执行，产出不可变 `golden_ir`；Fixer 仅以
    `golden_ir` + 完整 CAPL + 最近一次编译日志为输入。
- `workflows/canoe_auto_generation_burr/test_capl_authoring_agent.py` 与
  `test_vector_canoe_adapter.py`: 新增空 stdout/stderr、超时、
  planner/fixer 分发、CANoe COM 编译入口、CFG 验证脚本等单测。

### Validation

- `py -3.9 ci/run_checks.py` → 4/4 通过：
  - `validate_workflow_profile.py` (14 action / 19 transition)
  - `validate_workflow_kb.py` (30 references)
  - `py_compile` (20 files)
  - `test_retrieval_profiles.py` (2 tests)
- `py -3.9 -m unittest discover -s workflows/canoe_auto_generation_burr
  -p "test_*.py"` → 26/26 通过 (1.93 s)

## 2026-06-18

### Changed

- Added `docs/ARCHITECTURE_CURRENT.md` as the current architecture source of
  truth for the workspace, workflow graph, module boundaries, generated
  artifacts, cleanup policy, and validation commands.
- Updated the root README and workflow README to use the current
  `E:\Canoe_Gene\CANoe_Cfg_AutoGene` layout, relative commands, current module
  list, 14-action / 19-transition Burr graph, LLM planner/fixer CAPL authoring,
  and CI check entry point.
- Marked the older design/evaluation reports as historical and pointed them to
  the current architecture document.
- Added `generated_projects/` to `.gitignore`; workflow outputs are
  reproducible local run artifacts and should not be committed.

### Cleanup

- Removed local `generated_projects/` run files and Python `__pycache__/`
  directories from the workspace. One empty generated run directory may remain
  temporarily if held open by another process; it contains no files and is
  ignored by Git.

### Validation

- `python ci/run_checks.py`

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
