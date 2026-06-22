# L3_diffs — CANoe 版本差异知识库

> **L3_diffs** 目录跟踪 CANoe **v12.0** 与 **v15.0** 之间的知识库差异，为工作流提供版本兼容性参考。

---

## 1. 目录简介

L3_diffs 是 CANoe 版本级知识库差异追踪目录。它记录了 CANoe v12.0（CHM 格式，基于 CANdb++）与 v15.0（CHM+HTML5，基于 CANeds + Vector Tools Environment）之间的 CAPL API、DBC 关键字、Panel Designer 控件等方面的变更。

工作流在生成 CAPL 代码时可以引用这些差异信息，当生成的代码使用了在版本间发生变更的 API 时，向用户发出警告。

---

## 2. 文件清单

| 文件 | 说明 |
|------|------|
| `diff_capl_v12_to_v15.json` | CAPL API 差异：v12 与 v15 之间新增、移除、变更的函数和类别 |
| `diff_dbc_v12_to_v15.json` | DBC 关键字差异：v12 与 v15 之间新增和废弃的 DBC 关键字 |
| `diff_panel_v12_to_v15.json` | Panel Designer 控件差异：v12 与 v15 之间新增和移除的控件 |
| `diff_summary_v12_to_v15.json` | 汇总摘要：各类别的统计数字（类别数、函数数、控件数、关键字数） |
| `DIFF_REPORT.md` | 人类可读的差异报告，以 Markdown 格式呈现完整对比结果 |
| `PANEL_V12_VS_V15.md` | Panel Designer 专项对比报告，详细列出 v12 与 v15 的控件差异 |

---

## 3. 生成方式

这些差异文件是从 **CHM 知识库重建** 过程中提取的：

1. **v12.0 知识库**：从原始 CHM 文件中解析 CAPL 函数列表、DBC 关键字定义、Panel Designer 控件清单
2. **v15.0 知识库**：从新版 CHM + HTML5 文件中解析相同维度数据
3. **差异比对**：对两个版本的结构化数据进行集合运算（交集、差集），生成新增项、移除项、变更项
4. **输出**：将差异结果序列化为 JSON（机器可读）和 Markdown（人类可读）两种格式

---

## 4. 使用方式

工作流在以下场景中引用 L3_diffs 数据：

### 4.1 CAPL 代码生成时的 API 兼容性检查

当生成的 CAPL 代码调用了某个函数时，工作流可以查阅 `diff_capl_v12_to_v15.json`：

- **v15 新增 API**：如果目标版本是 v12，应警告该 API 在 v12 中不存在
- **v12 已移除 API**：如果目标版本是 v15，应警告该 API 已被废弃，建议使用替代方案
- **类别变更**：如 ADAS、CarMaker、DistributedObjects、MapWindowAPI 是 v15 新增类别

### 4.2 DBC 文件兼容性检查

查阅 `diff_dbc_v12_to_v15.json`，当 DBC 文件中使用以下 v15 新增关键字时，如果目标环境是 v12 则需要警告：

- `BO_TX_BU_`
- `CAT_`
- `CAT_DEF_`
- `FILTER`
- `SIG_VALTYPE_`

### 4.3 Panel Designer 控件兼容性检查

查阅 `diff_panel_v12_to_v15.json`，当 Panel 配置中使用了以下 v12 已移除控件时，如果目标环境是 v15 则需要警告：

- `MethodCall`
- `NMControl`
- `NMControlRuntime`

### 4.4 编程式访问

```python
import json
from pathlib import Path

diff_dir = Path("knowledge_base/L3_diffs")
capl_diff = json.loads((diff_dir / "diff_capl_v12_to_v15.json").read_text(encoding="utf-8"))

# 检查某 API 是否在 v15 中被移除
removed_apis = capl_diff.get("removed_in_v15", [])
if api_name in removed_apis:
    print(f"警告: {api_name} 在 v15 中已被移除")
```

---

## 5. 重新生成

当新的 CANoe 版本发布时，按以下步骤重新生成差异文件：

1. **重建知识库**：使用知识库构建脚本分别解析新旧版本的 CHM/HTML5 文件，生成结构化的 JSON 知识库
2. **运行差异比对**：执行差异生成脚本，对新旧知识库进行集合比对
3. **输出文件**：将结果写入本目录下的 JSON 和 Markdown 文件
4. **更新版本号**：将文件名和内容中的版本号更新为新版本对（如 `v15_to_v16`）

```bash
# 示例：重新生成 v12 到 v15 的差异
python knowledge_base/tools/generate_version_diff.py \
    --old-version 12.0 \
    --new-version 15.0 \
    --output-dir knowledge_base/L3_diffs
```

> **注意**：差异生成脚本的具体路径和参数请参考知识库构建工具的最新文档。

---

## 6. 差异概览

以下是 v12.0 → v15.0 的主要差异统计（详见 `diff_summary_v12_to_v15.json`）：

| 维度 | v12.0 | v15.0 | 变化 |
|------|-------|-------|------|
| CAPL 类别数 | 41 | 44 | +3 |
| CAPL 函数总数 | 4,553 | 5,017 | +464 |
| Panel Designer 控件数 | 37 | 33 | -4 |
| DBC 关键字数 | 15 | 20 | +5 |

### v15 新增 CAPL 类别
- ADAS
- CarMaker
- DistributedObjects
- MapWindowAPI

### v12 已移除 CAPL 类别
- Availability

### v15 新增 DBC 关键字
- `BO_TX_BU_`、`CAT_`、`CAT_DEF_`、`FILTER`、`SIG_VALTYPE_`

### v12 已移除 Panel 控件
- `MethodCall`、`NMControl`、`NMControlRuntime`
