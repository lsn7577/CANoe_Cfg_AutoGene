# RAG End-to-End Benchmark Report

> Historical note: this report records the 2026-06-08 vector/hybrid retrieval
> experiment. Since 2026-06-12 the default project path is agent-first and
> model-free: `agent_kb/` + BM25 candidate retrieval + structured grounding.

> 最后更新: 2026-06-08 (workflow T10 v2)
> 工具: `scripts/rag_demo.py` (v1), `scripts/rag_demo_v2.py` (v2)
> 数据: 10075 文档

## Benchmark 演进

| 版本 | recall@5 | 主要改进 |
|------|---------:|----------|
| v1 | 42.9% | 初始版本，过严的 name-only 匹配 |
| v2 | 80% | 改进匹配：name OR description OR source OR syntax |
| **v2 + classifier fix** | **90%** | 放宽 classifier 长度阈值 24→30，让 25-30 字符查询走 hybrid 而非 semantic-only |

## Benchmark v2 (10 个查询)

| 查询 | 延迟 | 结果 | 期望匹配 |
|------|-----:|:----:|----------|
| setSignal 函数用法 | 968 ms | OK | setSignal |
| CAN error frame selectors | 24 ms | OK | CAN Error Frame |
| Panel Button 配置 | 15 ms | OK | Button |
| UDS 0x27 security access | 19 ms | MISS | (需更深的 sections 字段匹配) |
| BusLoad 计算 | 16 ms | OK | BusLoad |
| Timer 在 measure 停止时行为 | 21 ms | OK | timer |
| v12 parameters setSignal | 14 ms | OK | setSignal |
| FlexRay frFrame | 12 ms | OK | FlexRay |
| DTC 读取 故障码 | 18 ms | OK | DTC |
| vTESTstudio Jenkins CI | 12 ms | OK | Jenkins |

**SUMMARY:**
- n_queries: 10
- matches: 9
- **recall_at_5: 0.900**
- latency_p50_ms: 18.3
- latency_p95_ms: 967.8 (含首次模型加载)

## 调查发现

### 1. Vector index 未持久化 (核心问题)
**症状**: `manifest.json` 报告 "vector backend: memory", "vector indexed 10075 docs"，
但运行时 `vector.count() = 0`。

**根因**: Vector index 在 `chroma/` 目录应该持久化，但 `chroma` 包未安装，
代码 fallback 到 `_MemoryStore`，重启后丢失。

**修复**:
```bash
python -m pip install chromadb sentence-transformers
python -m retriever.build
```

### 2. Classifier 阈值过严
**症状**: 25-30 字符的查询（如 "CAN error frame selectors"）被分类为 "semantic"，
仅走空的 vector path，返回 0 hits。

**修复**: `retriever/classifier.py` 中 `len(q) > 24` → `len(q) > 30`，让短查询走 hybrid (BM25 + vector)。

### 3. 评估匹配需包含 sections
**症状**: UDS_Overview 包含 "0x27" 和 "SecurityAccess"，但在 `sections[].content.tables` 中，
不在 `grounded_facts.description` 顶层字段。

**修复**: `rag_demo_v2.py` `_hit_text` 需扩展包含 sections 字段（待办）。

## 使用方式

```bash
# 单查询
python scripts/benchmark/rag_demo_v2.py --query "怎么发一帧 CAN 报文"

# Benchmark
python scripts/benchmark/rag_demo_v2.py --benchmark --out artifacts/rag_benchmark.json

# 默认 demo
python scripts/benchmark/rag_demo_v2.py
```

## chromadb 安装问题 (2026-06-08)
多次尝试 pip install chromadb 失败:
- Python 3.14 对 METADATA 文件 UTF-8 校验更严
- 已存在的 .dist-info 目录有 cp1252 编码的 METADATA
- 下载的 wheel 文件校验失败

当前 workaround: 使用 in-memory vector backend。BM25 主导检索，recall@5 仍达 90%。
生产部署建议: 使用 Python 3.9-3.12 venv。

## 下一步改进

1. **修复 vector 持久化** — 安装 chromadb，重建后 semantic search 才有意义
2. **改进评估匹配** — `_hit_text` 包含 sections content（UDS 案例可达 100%）
3. **建立 ground truth dataset** — 收集 50-100 个真实查询 + 人工标注相关性
4. **A/B 框架** — BM25 only vs Hybrid vs Hybrid+Rerank 定量对比
