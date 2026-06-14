# CANoe CHM 文件获取指南

> 用于采集 v17 / v18 / v18 SP3 等新版本的 CHM 源文件
> 创建时间: 2026-06-08 (workflow T02)

## 渠道

| 渠道 | 适用情况 | 步骤 |
|------|----------|------|
| **Vector 官网** | 正式客户 | https://www.vector.com/int/en/products/products-a-z/software/canoe/ — 登录后下载 |
| **公司软件门户** | 内网 | `\\corp\software-tools\Vector\` 或 IT 工单 |
| **本地 CHM 缓存** | 已装机 | `<CANoe_install>/Help/CANoeCANalyzer.chm` |
| **同事 U 盘** | 临时 | 注意杀毒软件可能误报 |

## 当前已知 CHM 来源

| 文件 | 版本 | 状态 |
|------|------|------|
| `../CANoeCANalyzer_v15.chm` | v15 | ✅ 可解压至 `../chm_extract_v15/` |
| `../chm_local/CANoeCANalyzer.chm` | 不详 | ⚠ 待确认版本号 |
| `../chm_extract_v12/` | v12 | ✅ 已用 |
| **缺失** | v16, v17, v18, v18 SP3 | ❌ 待获取 |

## 建议

1. **优先级**: v18 SP3 > v18 > v17 > v16
2. **存储**: 统一存到仓库同级的 CHM/source 目录，避免散落
3. **解压工具**: 推荐 `7-Zip` (无路径限制，Unicode 安全)
   ```bash
   7z x CANoeCANalyzer_v18.chm -o../chm_extract_v18
   ```
4. **解压后核对**: 
   - 必有 `CANoeCANalyzer/Topics/CAPLFunctions/`
   - 必有 `VectorToolsEnvironment/Topics/PanelDesigner/` (v15+)
   - 必有 `CANeds/Topics/` (v15+)
5. **解压后即可运行**:
   ```bash
   python scripts/extract/v3/run_all.py \
       --version v18 --chm-root ../chm_extract_v18
   ```

## 阻塞

当前沙箱内未找到 v17/v18 CHM，T02 只能完成：
- ✅ v17/v18 目录脚手架
- ✅ `extract_v3/run_all.py` 参数化 pipeline
- ⏸ 实际数据采集（需用户提供 CHM 文件）
