# Panel Designer: v12 vs v15 元素差异

> 验证日期: 2026-06-08 (workflow T09)
> 源: F:/EQ07/chm_extract/PanelDesigner/Topics/Elements (v12) vs F:/EQ07/chm_extract_v15/VectorToolsEnvironment/Topics/PanelDesigner/Elements (v15)

## 统计

| 版本 | 控件数 | 源 HTM 文件 |
|------|------:|------------|
| v12.0 | 37 | `PanelDesigner/Topics/Elements/PanelDesignerControls*.htm` |
| v15.0 | 33 | `VectorToolsEnvironment/Topics/PanelDesigner/Elements/PanelDesignerControls*.htm` |

**v15 缺失 3 个控件**（不是之前报告的 4 个 — 原 L3_diffs/diff_summary 报告中的空字符串是数据错误）：

| 缺失控件 | 原 v12 用途 | v15 替代 |
|----------|------------|----------|
| `MethodCall` | 调用 CAPL 方法的按钮 | 改用普通 Button + on mouseEvent 调用 |
| `NMControl` | 网络管理控制面板 | 移除 (CANoe 16+ 完全弃用 NM 工具集) |
| `NMControlRuntime` | NM 运行时控制 | 移除 (同上) |

## 推断原因

CANoe v15 起，Vector 重新组织了工具集：
- v12 使用 `PanelDesigner/` 独立工具
- v15 使用 `VectorToolsEnvironment/` 统一工具集
- v15 移除了 `NMControl*`（NM 工具集整体弱化，被 AUTOSAR NM 取代）
- v15 移除了 `MethodCall` 控件（功能被普通 Button + CAPL 回调替代）

## 知识库处理建议

1. ✅ v12 仍保留这 3 个控件的结构化数据（兼容历史项目）
2. ✅ v15 JSON 中**不**包含这 3 个（符合 v15 实际）
3. 📝 在 `extras/team/` 增加迁移指南："v12 → v15 Panel 迁移时如何替换 NMControl/MethodCall"
4. ⚠️  若团队项目仍使用 NM 工具，需在 `extras/team/` 单独记录 v12 NM Control 用法

## 结论

**v15 控件"减少"是 Vector 有意为之，非提取遗漏。** 知识库正确反映各版本实际情况。
