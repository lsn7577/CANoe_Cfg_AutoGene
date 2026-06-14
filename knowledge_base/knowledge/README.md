# Vector CANoe 知识库 (Knowledge Base)

> 长期维护的 Vector CANoe 12.0 / 15.0 帮助文档结构化知识库
> 适用对象：CANoe 配置工程师、CAPL 开发工程师、DBC 工程师、测试工程师
> 架构：Topic × Version 矩阵，结构化优先 (structured-first)

---

## 1. 目录结构 (Directory Structure)

```
knowledge/
├── _index.json                 # 顶层索引
├── README.md                   # 本文件
├── latest -> v15/              # 软链接：指向最新版本
├── v12/                        # CANoe 12.0 版本
│   ├── capl/                   #   CAPL 函数 (4559 文档)
│   ├── panel/                  #   Panel Designer (84 文档)
│   ├── dbc/                    #   CANeds DBC 编辑器 (160 文档)
│   └── xcp/                    #   XCP CAPL 函数 (17 文档, 来自 capl/XCP)
└── v15/                        # CANoe 15.0 版本
    ├── capl/                   #   CAPL 函数 (5025 文档)
    ├── panel/                  #   Panel Designer (70 文档)
    ├── dbc/                    #   CANeds DBC 编辑器 (150 文档)
    └── xcp/                    #   XCP CAPL 函数 (17 文档)
```

每个 topic 目录下：
```
<topic>/
├── _index.json                 # topic 级别索引
├── overview.md                 # 人类可读的概览
├── <name>.json                 # topic 级数据 (如 capl_functions_full.json)
└── structured/                 # 结构化数据
    ├── <subcategory>/          #   一级子分类
    │   ├── <page>.json
    │   └── <page>.md
    └── ...
```

## 2. 4 大主题 (Topics)

| Topic | 内容 | v12 文件数 | v15 文件数 |
|-------|------|----------:|----------:|
| **capl** | CAPL 编程语言 (函数/方法/事件/选择器/说明) | 4,559 | 5,025 |
| **panel** | Panel Designer 控件 (Button/Gauge/...) | 84 | 70 |
| **dbc** | CANeds DBC 编辑器 (关键字/属性) | 160 | 150 |
| **xcp** | XCP CAPL 函数 (CAPL/XCP 子集) | 17 | 17 |

## 3. 数据格式 (Data Format)

每个结构化页面输出两个文件：
- `<name>.json`：结构化记录 (字段: page_type, name, syntax, description, parameters, ...)
- `<name>.md`：渲染后的 Markdown (人类可读)

5 种页面类型：
- `function`：CAPL 函数 (如 `on message`, `setSignal`)
- `method`：CAPL 方法 (如 `msg.id`, `timer.time`)
- `event`：CAPL 事件 (如 `on key`, `on errorFrame`)
- `selector`：CAPL 选择器 (如 `*::CAPL_DLL`)
- `concept`：概念页 (Panel/DBC 控件/编辑器功能)

## 4. 提取质量 (Extraction Quality)

### v15 数据 (5025 文档)
| Topic | Pages | 字段覆盖 |
|-------|------:|---------|
| capl | 5,018 | description 95.7%, syntax 82.9%, parameters 72.6%, example 54.5% |
| panel | 69 | intro 49.3%, sections 81.2%, intro_tables 33.3% |
| dbc | 150 | intro 94.0%, intro_tables 90.0% |
| xcp | 17 | description 100%, syntax 94.1%, parameters 94.1% |

### v12 数据 (4820 文档)
| Topic | Pages | 字段覆盖 |
|-------|------:|---------|
| capl | 4,552 | description 93.8%, syntax 90.8%, availability 89.4% |
| panel | 83 | intro 54.2%, sections 77.1%, intro_tables 36.1% |
| dbc | 160 | intro 87.5%, intro_tables 84.4% |
| xcp | 17 | description 94.1%, syntax 94.1% |

详细数据见 `../tests_integration/structured_quality_report.json`

## 5. 版本对比 (Version Comparison)

| Topic | v12 | v15 | Δ |
|-------|---:|---:|---:|
| capl categories | 41 | 44 | +3 (ADAS, CarMaker, MapWindowAPI) |
| panel subcategories | 8 | 8 | 0 (但内容有更新) |
| dbc subcategories | 14 | 13 | -1 (Tab pages 合并到 windows) |
| xcp pages | 17 | 17 | 0 |

详见 `../L3_diffs/DIFF_REPORT.md`

## 6. 长期维护 (Maintenance)

### 6.1 添加新版本 (e.g. v17, v18)

```bash
# 1. 解压新版本 CHM (7-Zip 推荐, Unicode 安全)
7z x CANoeCANalyzer_v17.chm -o../chm_extract_v17

# 2. 运行参数化 pipeline (不需要复制 v2 脚本 - v3 复用 v2 parser)
python scripts/extract/v3/run_all.py \
    --version v17 --chm-root ../chm_extract_v17

# 3. 重建检索索引
python -m retriever.build

# 4. 刷新 agent_kb 视图
python agent_kb/build_manifest.py
```
