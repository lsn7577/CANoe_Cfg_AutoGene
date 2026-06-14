# Vector CANoe 知识库 (Knowledge Base)

> 长期维护的 Vector CANoe 12.0 / 15.0 帮助文档结构化知识库
> 适用对象：CANoe 配置工程师、CAPL 开发工程师、DBC 工程师、测试工程师、**Agent / LLM 工作流**

> **🤖 如果你是 LLM Agent**：从 [`agent_kb/`](./agent_kb/) 入手 —— 那是面向 agent 的导航层、索引和查询工具。
> 否则，直接进入 [`knowledge/`](./knowledge/) 目录使用。
> 默认工作流不需要 HuggingFace、向量模型或本地模型文件；语义理解由调用它的 agent 完成。
> 完整历史见 [`docs/CHANGELOG.md`](./docs/CHANGELOG.md)。

---

## 1. 推荐使用方式 (Recommended)

### For LLM Agents 🤖
进入 [`agent_kb/`](./agent_kb/) —— 该目录提供了：
- [`capability_manifest.md`](./agent_kb/capability_manifest.md)：能力清单
- [`rules_doc.md`](./agent_kb/rules_doc.md)：agent 检索协议
- [`rules_policy.md`](./agent_kb/rules_policy.md)：机器可读 JSON 检索策略 / answer gate
- [`query_routing.md`](./agent_kb/query_routing.md)：查询路由
- [`scenarios.json`](./agent_kb/scenarios.json)：10 个常见测试场景 → 必读页面
- [`unified_index.json`](./agent_kb/unified_index.json)：9,909 页面索引
- [`symbol_aliases.json`](./agent_kb/symbol_aliases.json)：CAPL 符号 → 页面
- [`kb_lookup.py`](./agent_kb/kb_lookup.py)：Python 助手 (`load_page` / `match_scenario` / `search`)
- [`AGENT_INTEGRATION.md`](./agent_kb/AGENT_INTEGRATION.md)：如何接入工作流

### For Humans 👤
**直接进入 [`knowledge/`](./knowledge/) 目录使用。**

```
knowledge/
├── README.md             # 详细使用说明
├── _index.json           # 顶层索引
├── v12/                  # CANoe 12.0 完整版
└── v15/                  # CANoe 15.0 完整版
    ├── capl/             #   CAPL 函数 (5025 文档)
    ├── panel/            #   Panel Designer (70 文档)
    ├── dbc/              #   CANeds DBC (150 文档)
    ├── xcp/              #   XCP CAPL (17 文档)
    └── diagnostics/      #   UDS/KWP/OBD (4 文档，合成)
```

详细结构见 [`knowledge/README.md`](./knowledge/README.md)

---

## 2. 🤖 Agent 优先使用方式 (Agent Quick Start)

如果你在 canoe-test-generation workflow 中集成 LLM agent，**从 [`agent_kb/`](./agent_kb/) 入手**：

```python
# 1. 直接加载
import sys
from pathlib import Path
sys.path.insert(0, str(Path.cwd()))
from agent_kb.kb_lookup import load_page, match_scenario, search

# 2. "我有 CAPL 函数名" → 加载
page = load_page("setSignal", version="v15")
print(page["syntax"], page["description"])

# 3. "我有自然语言意图" → 场景匹配
scenarios = match_scenario("wait for signal to reach 1500 RPM")
for sc in scenarios[:1]:
    print(sc["id"], "->", sc["context"])

# 4. 自由搜索：BM25 候选召回 + 结构化事实 grounding，理解交给 agent
hits = search("怎么发一帧 CAN 报文", version="v15", top_n=3)
for h in hits:
    print(h["grounded_facts"]["name"], h["grounded_facts"]["syntax"])
```

完整集成文档：[`agent_kb/AGENT_INTEGRATION.md`](./agent_kb/AGENT_INTEGRATION.md)

---

## 3. 完整目录 (Full Directory)

```
knowledge_base/
├── agent_kb/                 # 🤖 Agent-facing navigation layer (9 MB)
│   ├── README.md
│   ├── AGENT_INTEGRATION.md
│   ├── capability_manifest.md
│   ├── rules_doc.md
│   ├── rules_policy.md
│   ├── query_routing.md
│   ├── scenarios.json
│   ├── schema_v3.json
│   ├── unified_index.json
│   ├── symbol_aliases.json
│   ├── kb_lookup.py
│   ├── example_workflow.py
│   └── build_manifest.py
│
├── knowledge/                 # ★ 主目录: 结构化知识库 (109 MB)
│   ├── README.md
│   ├── _index.json
│   ├── v12/                       # CANoe 12.0 (4,730 页)
│   │   ├── capl/  panel/  dbc/  xcp/
│   ├── v15/                       # CANoe 15.0 (5,174 页)
│   │   ├── capl/  panel/  dbc/  xcp/  diagnostics/
│   ├── v17/                       # 脚手架 (0 页，待 CHM)
│   │   ├── capl/  panel/  dbc/  xcp/
│   └── v18/                       # 脚手架 (0 页，待 CHM)
│       ├── capl/  panel/  dbc/  xcp/
│
├── extras/team/               # 团队手工文档 (5 个 JSON)
│   ├── canSetSignalDword.json
│   ├── CAPL_Internal_Coding_Standards.json
│   ├── CI_Pipeline_Reference.json
│   ├── Common_Gotchas.json
│   └── panelGauges.json
│
├── L3_diffs/                  # v12 ↔ v15 版本差异 (5 个文件)
│
├── artifacts/                 # 重建的索引 (35 MB)
│   ├── bm25.pkl
│   └── manifest.json
│
├── scripts/                   # ★ 提取与处理脚本 (148 KB)
│   ├── README.md
│   ├── extract/
│   │   ├── v2/                    # 可复用 parsers (v15 MadCap + v12 flat-table)
│   │   │   ├── 01_vector_parser.py
│   │   │   ├── 02_render_md.py
│   │   │   ├── 03_extract_v15_structured.py
│   │   │   ├── 04_extract_structured.py
│   │   │   ├── 05_vector_parser_v12.py
│   │   │   ├── 06_concept_parser.py
│   │   │   ├── 07_extract_concept.py
│   │   │   └── run_all.py
│   │   └── v3/                    # 版本参数化 pipeline
│   │       ├── README.md
│   │       └── run_all.py
│   ├── patches/                   # 历史性一次性修复
│   │   ├── v12_params.py
│   │   ├── v15_simple.py
│   │   ├── v15_return_sel.py
│   │   └── panel_props.py
│   └── benchmark/                 # RAG 演示与基准
│       ├── rag_demo_v1.py
│       └── rag_demo_v2.py
│
├── retriever/                 # Agent-first BM25 retriever + grounding (vector optional)
│   ├── README.md
│   ├── retriever.py
│   ├── preprocess.py
│   ├── bm25_index.py
│   ├── vector_index.py           # optional; not used by default
│   ├── fusion.py                 # RRF + optional rerank helpers
│   ├── grounding.py
│   ├── classifier.py
│   ├── build.py
│   ├── ingest.py
│   ├── add_knowledge.py
│   ├── serve.py
│   ├── mcp_server.py
│   ├── config.py
│   └── tests/test_smoke.py
│
├── docs/                      # ★ 项目文档 (合并所有顶层 .md)
│   ├── CHANGELOG.md
│   ├── FAQ.md
│   ├── DEPLOYMENT.md
│   ├── CHM_ACQUISITION.md
│   ├── RAG_BENCHMARK_REPORT.md
│   ├── REFACTORING_REPORT.md
│   └── WORKFLOW_TASKS.md
│
└── tests_integration/         # 完整性测试 (1.3 MB)
    ├── test_completeness.py
    ├── manifest_v12.json
    ├── manifest_v15.json
    ├── structured_quality_report.json
    └── completeness_test_report.json
```

---

## 4. 4 大主题 (Topics)

| Topic | v12 文档数 | v15 文档数 | 描述 |
|-------|----------:|----------:|------|
| **capl** | 4,487 | 4,951 | CAPL 编程语言：函数/方法/事件/选择器/说明 |
| **panel** | 83 | 69 | Panel Designer：控件/菜单/工具/功能 |
| **dbc** | 160 | 150 | CANeds DBC 编辑器：关键字/属性/对象 |
| **xcp** | 17 | 17 | XCP CAPL 函数 (来自 capl/XCP) |
| **diagnostics** | — | 4 | UDS / KWP2000 / OBD (合成) |

> 注：上面的数字来自 `agent_kb/unified_index.json`（应用了页面类型修正）。
> `tests_integration/manifest_v15.json` 显示原始提取器计数（5018 capl, 70 panel, 150 dbc, 17 xcp）。

---

## 5. 5 种页面类型 (Page Types)

1. `function` - CAPL 函数 (e.g. `setSignal`, `on message`)
2. `method` - CAPL 方法 (e.g. `msg.id`, `timer.time`)
3. `event` - CAPL 事件 (e.g. `on key`, `on errorFrame`)
4. `selector` - CAPL 选择器 (e.g. `*::CAPL_DLL`)
5. `concept` - 概念页 (Panel 控件、DBC 编辑功能)

> 历史问题：v15 parser 曾把 ~80% 页面误分类为 `notes`。已在 `scripts/extract/v2/01_vector_parser.py:detect_page_type()` 中修复 (2026-06-10)。
> 修正后共识别 72 个 `selector` 页（vs 原始 9 个）。见 `agent_kb/unified_index.json`。

---

## 6. 数据格式 (Data Format)

每个页面输出两个文件：
- **`<name>.json`**：结构化记录，含字段 `page_type`, `name`, `syntax`, `description`, `parameters`, `return`, `example`, `availability`, ...
- **`<name>.md`**：渲染后的 Markdown

---

## 7. 长期维护 (Maintenance)

### 7.1 重建全部内容（仅在 CHM 源变化时）

```bash
# 完整 v12 + v15 重建
python scripts/extract/v2/run_all.py

# 重建默认检索索引（BM25，无模型依赖）
python -m retriever.build

# 重建 agent_kb 视图
python agent_kb/build_manifest.py
```

### 7.2 添加新版本 (e.g. v17)

```bash
# 1. 获取 CHM (见 docs/CHM_ACQUISITION.md)
# 2. 解压
7z x CANoeCANalyzer_v17.chm -o../chm_extract_v17
# 3. 运行 v3 参数化 pipeline
python scripts/extract/v3/run_all.py --version v17 --chm-root ../chm_extract_v17
# 4. 重建索引 + 视图
python -m retriever.build
python agent_kb/build_manifest.py
```

### 7.3 可选向量增强（默认不启用）

默认索引用 `agent_kb/` 结构化索引和 `artifacts/bm25.pkl`，不下载也不加载模型。
只有明确需要本地语义向量实验时才执行：

```bash
python -m pip install -r requirements-optional.txt
python -m retriever.build --with-vector --embedding-model BAAI/bge-m3
```

运行时也必须显式设置 `RETRIEVER_ENABLE_VECTOR=1` 才会尝试加载向量索引。

### 7.4 部署 + 监控

见 [`docs/DEPLOYMENT.md`](./docs/DEPLOYMENT.md)。

---

## 8. 版本迁移历史 (Migration History)

完整历史见 [`docs/CHANGELOG.md`](./docs/CHANGELOG.md)。要点：

| 日期 | 变更 |
|------|------|
| 2026/06/10 | Agent 导航层 (`agent_kb/`) + 目录重组 (`docs/`, `scripts/extract/`, `scripts/patches/`, `scripts/benchmark/`, `tests_integration/`) + 移除无用文件 + 修复 v15 parser 页面分类 bug |
| 2026/06/08 | T01-T10 workflow 完成：v12 parameters 3.9%→81.3%、Panel `property_references`、RAG 基准 42.9%→90% |
| 2026/06/01 | 引入 `scripts/extract_v2/` 模板感知结构化提取器；重组为 `knowledge/` topic × version 矩阵 |
| (pre) | 初始 3-Layer 架构 (L1/L2/L3) |
