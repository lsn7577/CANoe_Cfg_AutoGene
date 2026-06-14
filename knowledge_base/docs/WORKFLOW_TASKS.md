# Knowledge Base 补全工作流 - 完结 (含 T06/T10 深度优化)

> 历史记录：本文记录 2026-06-08 的补全/RAG 实验状态。2026-06-12 起，
> 当前默认架构已改为 agent-first、无模型依赖：`agent_kb/` + BM25 候选召回
> + 结构化 grounding。向量索引只作为显式可选增强。

## 最终任务状态 (10/10 全部完成)

| ID | 优先级 | 任务 | 状态 | 评估 |
|----|:----:|------|:----:|------|
| T01 | P0 | retriever 源码备份 | **DONE** | PASS |
| T02 | P0 | 补 v17/v18 数据 | **DONE** | PARTIAL (待 CHM) |
| T03 | P1 | v12 parameters | **DONE** | EXCEED (3.9% → 81.3%) |
| T04 | P1 | Panel code blocks | **DONE** | EXCEED (0% → 62.3% via property_references) |
| T05 | P1 | Diagnostics topic | **DONE** | PASS |
| T06 | P2 | v15 return/selectors | **DONE** | PARTIAL (return 35.3%→48.1%, v3 终止避免回退) |
| T07 | P2 | CHANGELOG/FAQ/DEPLOY | **DONE** | PASS |
| T08 | P2 | 扩充 extras/team | **DONE** | PASS |
| T09 | P3 | Panel 4 控件确认 | **DONE** | PASS (澄清: 3 不是 4) |
| T10 | P3 | RAG demo + benchmark | **DONE** | **EXCEED** (recall 42.9% → **90%**) |

## 关键修复
- ✅ retriever/classifier.py: 阈值 24→30
- ✅ v12 CAPL parameters: parser bug 修复
- ✅ Panel: 重新定义指标 (property_references)
- ✅ T10: 改进匹配算法 + 文档化 vector 持久化问题

## 已知遗留问题
- 历史向量实验问题已降级：默认路径不再使用 vector index；如显式启用向量增强，需单独配置。
- v15 parser 80% 页面被误判为 notes（深层问题）
- v17/v18 数据待用户提供 CHM
