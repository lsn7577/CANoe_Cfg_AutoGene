# CANoe_Cfg_AutoGene 当前架构说明

更新时间：2026-06-18  
工程根目录：`E:/Canoe_Gene/CANoe_Cfg_AutoGene`

## 1. 工程定位

`CANoe_Cfg_AutoGene` 是一个面向 Vector CANoe 自动化测试工程的生成工作流。它以 Excel 测试用例模板为输入，结合 DBC/A2L/CDD/CFG 等源文件、结构化 CANoe/CAPL 知识库和外部 LLM CAPL authoring agent，生成可审查的 CANoe 配置计划、CAPL Test Module、质量报告、修正包和运行 manifest。

当前工程的交付边界是“可追踪生成链路 + 可审查中间产物”。真实 CANoe `.cfg` 二进制序列化和 CAPL 实机编译必须通过 Vector CANoe COM Automation 或项目专属 adapter 执行；工作流会把未执行的外部验证标记为 `skipped`、`manual_required`、`unavailable` 或 `failed`，不会伪造实机通过。

## 2. 顶层目录职责

```text
CANoe_Cfg_AutoGene/
  README.md
  CHANGELOG.md
  CANoeCANalyzer.chm
  ci/
    run_checks.py
    run_checks.bat
  docs/
    ARCHITECTURE_CURRENT.md
    CANOE_GENE_FUNCTIONAL_DESIGN_REPORT.md
    WORKSPACE_STRUCTURE_AND_WORKFLOW_EVALUATION.md
  knowledge_base/
    agent_kb/
    artifacts/
    knowledge/
    retriever/
    workflow_kb/
  templates/
    canoe_test_case_template/
  workflows/
    canoe_auto_generation_burr/
  generated_projects/        # 本地运行产物，已忽略，不应提交
```

长期资产是 `knowledge_base/`、`templates/`、`workflows/`、`docs/` 和 `ci/`。`generated_projects/` 是可再生成输出目录，清理时可删除；`.omx/`、`__pycache__/` 和测试缓存也不属于工程资产。

## 3. 核心分层

### 3.1 输入模板层

- `templates/canoe_test_case_template/CANoe自动化测试用例模板.xlsx` 是测试人员维护入口。
- `templates/canoe_test_case_template/template_field_mapping.json` 是 Excel 字段和枚举的 canonical 来源。
- `workflows/canoe_auto_generation_burr/template_field_mapping.json` 只保存到模板 canonical mapping 的指针，由 `validate_template_contract` 校验。

### 3.2 Canonical IR 层

- `canonical_ir.py` 提供中文 Excel 展示字段到稳定英文 ID 的映射。
- 当前 workflow 仍兼容历史中文字段，但新增逻辑应优先使用 canonical ID，避免 Excel 展示名直接扩散到业务逻辑。
- 下一步架构目标是让 Excel/Web/API 都只作为 input adapter，内部统一使用 canonical test case IR。

### 3.3 Source Model 层

- `source_parser.py` 是独立的 DBC/A2L/CDD/CFG parser 模块。
- DBC 解析优先使用 `cantools`，不可用时回退 regex。
- A2L 解析 characteristic、measurement、COMPU_METHOD 和部分访问权限。
- CDD 解析 protocol service、DID、SID alias、data object 等轻量诊断语义。
- CFG 解析 CANoe version、文件引用和已挂载资源。

`--strict-source-validation` 会把缺失源文件或对象解析失败从 warning 升级为 error，进入修正流程。

### 3.4 知识库与证据层

- `knowledge_base/knowledge/` 保存 v12/v15 CANoe/CAPL 结构化页面。
- `knowledge_base/agent_kb/` 提供 symbol lookup、scenario matching 和 agent-facing index。
- `knowledge_base/retriever/` 提供默认 BM25 + grounding，向量检索为可选实验能力。
- `knowledge_base/workflow_kb/` 保存 workflow action contract、generation patterns、retrieval profiles、validation rules 和 packs。

工作流按 profile 隔离知识检索：`canoe_config` 面向 CFG/COM Automation，`capl_authoring` 面向 CAPL/XCP/diagnostics，避免 CAPL agent 混入 CFG 生成知识。

### 3.5 Burr Workflow 编排层

主入口：`workflows/canoe_auto_generation_burr/canoe_workflow.py`

当前 Burr graph 由 14 个 action 和 19 条 transition 组成，`workflow_profile.json` 与 Python 中的 `ACTION_REGISTRY` / `TRANSITION_SPECS` 通过 `validate_workflow_profile.py` 校验一致。

```text
load_test_case_template
  -> validate_template_contract
  -> parse_source_files
  -> validate_test_cases
  -> retrieve_evidence
  -> analyze_test_coverage
  -> validate_evidence_gate
  -> generate_canoe_config
  -> evaluate_canoe_config
  -> generate_capl_script
  -> evaluate_capl_script
  -> package_outputs

失败分支：
  validate_template_contract / validate_test_cases /
  validate_evidence_gate / evaluate_canoe_config / evaluate_capl_script
  -> plan_repair
  -> generate_canoe_config | generate_capl_script | emit_test_case_corrections
```

### 3.6 CANoe 配置生成层

- `generate_canoe_config` 不手写 Vector 私有 `.cfg` 二进制格式。
- 有 base CFG 时，优先复制/保留模板并生成 CANoe COM Automation 脚本。
- 无 base CFG 时，输出 `.cfg.plan.json`、`.cfg.generate.ps1` 和 layout manifest。
- `vector_canoe_adapter.prepare_cfg_generation()` 负责生成/执行 CANoe COM Automation 路径。
- `evaluate_canoe_config` 调用 `vector_canoe_adapter.validate_config()`，按 `disabled|manual|automated` 返回外部验证状态。

### 3.7 CAPL 生成与编译闭环

- `generate_capl_script` 默认走 `llm` authoring 模式。
- `agents/capl_authoring_agent.py` 定义 planner/fixer payload、响应校验和外部命令调用。
- `agents/claude_code_capl_agent.py` 是 Claude Code CLI adapter。
- Planner 生成不可变 `golden_ir`；Fixer 在编译循环中只接收 `golden_ir`、当前完整 CAPL 源码和最新编译错误。
- `capl_lexer_lint.py` 提供本地 CAPL lexer/static lint。
- `vector_canoe_adapter.compile_capl()` 支持外部 compile hook 或内置 CANoe COM 编译脚本。
- `quality_gate=release` 会禁止未绑定的 `CanoeGene_*` adapter stub 通过。

### 3.8 报告、修正与产物生命周期

- `html_report.py` 生成 `run_report.html`。
- `correction_workbook.py` 生成 `test_case_corrections.xlsx` 和 `test_case_corrections.md`。
- `run_retention.py` 支持按数量和天数清理历史 run，且不会删除 `latest_run_manifest.json` 指向的 run。
- 本次工程清理已删除本地 `generated_projects/` 运行产物和所有 `__pycache__/`，并把 `generated_projects/` 加入 `.gitignore`。

## 4. 当前主要输出

每次运行写入：

```text
generated_projects/<project>/runs/<run_id>/
```

主要产物：

| 文件 | 说明 |
| --- | --- |
| `template_contract_report.json` | Excel 字段/枚举契约校验 |
| `source_models.json` | DBC/A2L/CDD/CFG 解析摘要 |
| `structured_test_cases.json` | 结构化测试用例 IR |
| `test_case_correction_items.json` | 输入或语义修正项 |
| `evidence_bundle.json` | CAPL/API/团队规范证据包 |
| `coverage_report.json` | 需求、功能、领域、证据覆盖 |
| `<project>.cfg.plan.json` | CANoe 配置计划 |
| `<project>.cfg.generate.ps1` | CANoe COM Automation 脚本 |
| `<project>.cfg` 或 `<project>.cfg.todo.json` | base CFG 复制/生成结果或待生成计划 |
| `<project>_TestModule.can` | CAPL Test Module |
| `capl_script_plan.json` | CAPL authoring、证据、coverage、compile loop 计划 |
| `capl_compile_attempt_*.json/.ps1` | 自动编译尝试报告/脚本 |
| `run_report.html` | 本次运行摘要报告 |
| `final_package_manifest.json` | 成功 manifest |
| `blocked_manifest.json` | 阻塞 manifest |
| `repair_plan.json` | 修复计划 |

## 5. 验证命令

推荐从仓库根目录执行：

```powershell
python ci/run_checks.py
```

该脚本当前覆盖：

1. `validate_workflow_profile.py`
2. `knowledge_base/workflow_kb/validate_workflow_kb.py`
3. `py_compile` 编译 workflow Python 文件
4. `test_retrieval_profiles.py`

更深入的单元测试可按需运行：

```powershell
python -m unittest `
  workflows.canoe_auto_generation_burr.test_cdd_parser `
  workflows.canoe_auto_generation_burr.test_cfg_parser `
  workflows.canoe_auto_generation_burr.test_vector_canoe_adapter `
  workflows.canoe_auto_generation_burr.test_retrieval_profiles `
  workflows.canoe_auto_generation_burr.test_capl_authoring_agent `
  workflows.canoe_auto_generation_burr.test_claude_code_capl_agent
```

## 6. 当前风险和下一步

| 风险 | 当前处理 | 下一步 |
| --- | --- | --- |
| 真实 CANoe 环境不可用时无法证明 `.cfg`/`.can` 实机通过 | 状态显式标为 skipped/manual/unavailable/failed | 在 CANoe 工作站跑 automated 模式并固化报告 |
| LLM CAPL authoring 依赖外部命令 | adapter 写入 payload/response/diagnostics | 为团队环境固定 `CANOE_GENE_CAPL_AGENT_COMMAND` |
| DBC/A2L/CDD parser 仍偏轻量 | 名称和部分语义可离线校验 | 接入团队级 parser 或 Vector 导出数据 |
| `canoe_workflow.py` 仍偏大 | 已拆出 source parser、lint、report、retention、agent adapter | 继续拆分 input adapter、evidence gate、renderer、repair |
| 历史 run 可能膨胀 | `run_retention.py` 和 `.gitignore` 已到位 | 在 CLI/CI 中显式调用 retention 策略 |

## 7. 维护原则

1. 新增字段先改 canonical mapping，再改模板、校验和 renderer。
2. 新增 workflow action 后必须同步 `workflow_profile.json`，并运行 profile 校验。
3. 新增 CAPL API 用法必须能回溯到 `evidence_bundle.json`。
4. 未执行真实 CANoe 的路径不得宣称外部验证成功。
5. `generated_projects/` 是可再生成产物，不提交、不作为长期事实来源。
