"""HTML run summary report generator.

Produces a self-contained, modern-looking HTML report summarising a CANoe
configuration auto-generation run.  The report includes summary cards,
test-case tables, correction tables, evidence/coverage sections, artifact
links, and a repair section (when the run is blocked).

The output file has **no external CSS/JS dependencies** — everything is
inlined so the report can be opened offline.
"""

from __future__ import annotations

import html
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List


# ---------------------------------------------------------------------------
# Color scheme
# ---------------------------------------------------------------------------

_BG = "#1a1a2e"
_CARD = "#16213e"
_ACCENT = "#0f3460"
_ERROR = "#e94560"
_SUCCESS = "#53d769"
_WARNING = "#ffd700"
_TEXT = "#e0e0e0"
_TEXT_DIM = "#8888aa"
_BORDER = "#252550"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _as_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value).strip()


def _escape(text: Any) -> str:
    return html.escape(_as_text(text), quote=False)


def _ensure_dir(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def _status_color(status: str) -> str:
    s = status.lower()
    if s in ("complete", "pass", "success", "ok"):
        return _SUCCESS
    if s in ("blocked", "blocked_for_corrections", "fail", "error"):
        return _ERROR
    if s in ("warn", "warning", "partial"):
        return _WARNING
    return _TEXT_DIM


def _status_label(status: str) -> str:
    s = status.lower()
    mapping = {
        "complete": "完成",
        "blocked_for_corrections": "已阻断（需修正）",
        "blocked": "已阻断",
        "pass": "通过",
        "fail": "失败",
        "warn": "警告",
        "warning": "警告",
        "partial": "部分完成",
        "success": "成功",
        "error": "错误",
    }
    return mapping.get(s, status)


def _get(state: Dict[str, Any], key: str, default: Any = None) -> Any:
    val = state.get(key, default)
    return val if val is not None else default


# ---------------------------------------------------------------------------
# Section builders
# ---------------------------------------------------------------------------

def _build_header(state_data: Dict[str, Any]) -> str:
    run_id = _as_text(_get(state_data, "run_id", "N/A"))
    status = _as_text(_get(state_data, "status", "unknown"))
    color = _status_color(status)
    label = _status_label(status)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    project_name = "CANoe_AutoTest_Project"
    structured = _get(state_data, "structured_test_case", {})
    if isinstance(structured, dict):
        project_name = _as_text(
            structured.get("project", {}).get("name", project_name)
        ) or project_name

    return f"""
    <header class="report-header">
        <div class="header-left">
            <h1>{_escape(project_name)}</h1>
            <div class="header-meta">
                <span class="meta-item"><span class="meta-label">Run ID</span> <code>{_escape(run_id)}</code></span>
                <span class="meta-item"><span class="meta-label">时间</span> {_escape(timestamp)}</span>
            </div>
        </div>
        <div class="status-badge" style="background:{color}; color:#1a1a2e;">
            {_escape(label)}
        </div>
    </header>
    """


def _build_summary_cards(state_data: Dict[str, Any]) -> str:
    structured = _get(state_data, "structured_test_case", {}) or {}
    cases = structured.get("cases", []) if isinstance(structured, dict) else []
    case_count = len(cases)
    step_count = sum(
        len(c.get("steps", [])) for c in cases if isinstance(c, dict)
    )

    corrections = _get(state_data, "correction_items", []) or []
    correction_count = len(corrections)

    evidence_bundle = _get(state_data, "evidence_bundle", {}) or {}
    capl_ev = (
        evidence_bundle.get("capl_evidence_coverage", {})
        if isinstance(evidence_bundle, dict)
        else {}
    )
    # Try coverage report first, then evidence bundle
    coverage_report = _get(state_data, "coverage_report", {}) or {}
    if isinstance(coverage_report, dict):
        capl_cov = coverage_report.get("capl_evidence_coverage", {})
        resolved = capl_cov.get("resolved_symbol_count", 0)
        required = capl_cov.get("required_symbol_count", 0)
    else:
        resolved = capl_ev.get("resolved_symbol_count", 0)
        required = capl_ev.get("required_symbol_count", 0)
    evidence_pct = f"{(resolved / required * 100):.0f}%" if required else "N/A"

    # Compile status
    cfg_artifact = _get(state_data, "cfg_artifact", {})
    capl_eval = _get(state_data, "capl_eval_report", {})
    compile_status = "N/A"
    if isinstance(capl_eval, dict) and capl_eval.get("compile_status"):
        compile_status = _as_text(capl_eval["compile_status"])
    elif isinstance(cfg_artifact, dict) and cfg_artifact.get("status"):
        compile_status = _as_text(cfg_artifact["status"])

    compile_color = _status_color(compile_status)

    cards = [
        ("测试用例", str(case_count), _ACCENT),
        ("步骤总数", str(step_count), _ACCENT),
        ("证据覆盖率", evidence_pct, _SUCCESS if "N/A" not in evidence_pct else _TEXT_DIM),
        ("修正项", str(correction_count), _ERROR if correction_count else _SUCCESS),
        ("编译状态", _status_label(compile_status), compile_color),
    ]

    card_html = "\n".join(
        f'<div class="summary-card">'
        f'<div class="card-value" style="color:{color}">{_escape(value)}</div>'
        f'<div class="card-label">{_escape(label)}</div>'
        f'</div>'
        for label, value, color in cards
    )

    return f'<section class="summary-section"><div class="card-grid">{card_html}</div></section>'


def _build_test_cases_table(state_data: Dict[str, Any]) -> str:
    structured = _get(state_data, "structured_test_case", {}) or {}
    cases = structured.get("cases", []) if isinstance(structured, dict) else []

    if not cases:
        return '<section class="content-section"><h2>测试用例</h2><p class="empty-msg">无测试用例数据</p></section>'

    rows_html: List[str] = []
    for case in cases:
        if not isinstance(case, dict):
            continue
        case_id = _escape(case.get("case_id", ""))
        req_id = _escape(case.get("requirement_id", "") or ", ".join(case.get("requirement_ids", [])))
        priority = _escape(case.get("priority", ""))
        step_count = len(case.get("steps", []))
        status_val = _as_text(case.get("status", "pending"))
        color = _status_color(status_val)
        rows_html.append(
            f'<tr>'
            f'<td>{case_id}</td>'
            f'<td>{req_id}</td>'
            f'<td>{priority}</td>'
            f'<td>{step_count}</td>'
            f'<td><span class="pill" style="background:{color}; color:#1a1a2e;">{_escape(_status_label(status_val))}</span></td>'
            f'</tr>'
        )

    return f"""
    <section class="content-section">
        <h2>📋 测试用例 ({len(cases)})</h2>
        <div class="table-wrap">
            <table>
                <thead><tr>
                    <th>用例ID</th><th>需求ID</th><th>优先级</th><th>步骤数</th><th>状态</th>
                </tr></thead>
                <tbody>{''.join(rows_html)}</tbody>
            </table>
        </div>
    </section>
    """


def _build_corrections_table(state_data: Dict[str, Any]) -> str:
    corrections = _get(state_data, "correction_items", []) or []

    if not corrections:
        return '<section class="content-section"><h2>🔧 修正项</h2><p class="empty-msg">无修正项 — 所有用例均通过校验</p></section>'

    # Sort: errors first, then warnings
    def _rank(item: Dict[str, Any]) -> int:
        sev = _as_text(item.get("severity")).lower()
        if sev == "error":
            return 0
        if sev == "warning":
            return 1
        return 2

    sorted_items = sorted(corrections, key=_rank)

    rows_html: List[str] = []
    for item in sorted_items:
        if not isinstance(item, dict):
            continue
        sev = _as_text(item.get("severity")).lower()
        color = _status_color(sev)
        rows_html.append(
            f'<tr>'
            f'<td><span class="pill" style="background:{color}; color:#1a1a2e;">{_escape(sev)}</span></td>'
            f'<td>{_escape(item.get("category", ""))}</td>'
            f'<td class="msg-cell">{_escape(item.get("message", ""))}</td>'
            f'<td>{_escape(item.get("test_case_id", ""))}</td>'
            f'</tr>'
        )

    return f"""
    <section class="content-section">
        <h2>🔧 修正项 ({len(corrections)})</h2>
        <div class="table-wrap">
            <table>
                <thead><tr>
                    <th>严重级别</th><th>类别</th><th>问题描述</th><th>用例ID</th>
                </tr></thead>
                <tbody>{''.join(rows_html)}</tbody>
            </table>
        </div>
    </section>
    """


def _build_evidence_section(state_data: Dict[str, Any]) -> str:
    evidence_bundle = _get(state_data, "evidence_bundle", {}) or {}
    pages = evidence_bundle.get("pages", []) if isinstance(evidence_bundle, dict) else []

    if not pages:
        return '<section class="content-section"><h2>🔬 证据链</h2><p class="empty-msg">无证据数据</p></section>'

    rows_html: List[str] = []
    for page in pages:
        if not isinstance(page, dict):
            continue
        symbol = _escape(page.get("symbol", ""))
        confidence = _as_text(page.get("confidence", ""))
        source = _escape(page.get("source", ""))
        conf_color = _SUCCESS if confidence == "high" else (_WARNING if confidence == "medium" else _ERROR)
        rows_html.append(
            f'<tr>'
            f'<td><code>{symbol}</code></td>'
            f'<td><span class="pill" style="background:{conf_color}; color:#1a1a2e;">{_escape(confidence)}</span></td>'
            f'<td>{source}</td>'
            f'</tr>'
        )

    return f"""
    <section class="content-section">
        <h2>🔬 证据链 ({len(pages)} pages)</h2>
        <div class="table-wrap">
            <table>
                <thead><tr>
                    <th>符号</th><th>置信度</th><th>来源</th>
                </tr></thead>
                <tbody>{''.join(rows_html)}</tbody>
            </table>
        </div>
    </section>
    """


def _build_coverage_section(state_data: Dict[str, Any]) -> str:
    coverage_report = _get(state_data, "coverage_report", {}) or {}
    if not isinstance(coverage_report, dict) or not coverage_report:
        return '<section class="content-section"><h2>📊 覆盖率</h2><p class="empty-msg">无覆盖率数据</p></section>'

    # Domain coverage
    domain_cov = coverage_report.get("domain_coverage", {})
    domain_steps = domain_cov.get("step_count_by_domain", {}) if isinstance(domain_cov, dict) else {}

    domain_items: List[str] = []
    for domain, count in sorted(domain_steps.items()):
        domain_items.append(
            f'<div class="cov-item">'
            f'<span class="cov-label">{_escape(domain)}</span>'
            f'<span class="cov-value">{count} steps</span>'
            f'</div>'
        )

    # Requirement coverage
    req_cov = coverage_report.get("requirement_coverage", {})
    covered_reqs = req_cov.get("covered_requirement_count", 0) if isinstance(req_cov, dict) else 0
    cases_without_req = req_cov.get("cases_without_requirement", []) if isinstance(req_cov, dict) else []

    # CAPL evidence coverage
    capl_cov = coverage_report.get("capl_evidence_coverage", {})
    resolved = capl_cov.get("resolved_symbol_count", 0) if isinstance(capl_cov, dict) else 0
    required_sym = capl_cov.get("required_symbol_count", 0) if isinstance(capl_cov, dict) else 0
    gap_count = capl_cov.get("gap_count", 0) if isinstance(capl_cov, dict) else 0

    # Risks
    risks = coverage_report.get("risks", [])
    risk_items: List[str] = []
    for risk in risks:
        if not isinstance(risk, dict):
            continue
        sev = _as_text(risk.get("severity")).lower()
        color = _status_color(sev)
        risk_items.append(
            f'<div class="risk-item">'
            f'<span class="pill" style="background:{color}; color:#1a1a2e;">{_escape(sev)}</span>'
            f'<span class="risk-msg">{_escape(risk.get("message", ""))}</span>'
            f'</div>'
        )

    return f"""
    <section class="content-section">
        <h2>📊 覆盖率分析</h2>
        <div class="cov-grid">
            <div class="cov-block">
                <h3>域覆盖</h3>
                {''.join(domain_items) if domain_items else '<p class="empty-msg">无域覆盖数据</p>'}
            </div>
            <div class="cov-block">
                <h3>需求覆盖</h3>
                <div class="cov-item"><span class="cov-label">已覆盖需求数</span><span class="cov-value">{covered_reqs}</span></div>
                <div class="cov-item"><span class="cov-label">无需求用例</span><span class="cov-value">{len(cases_without_req)}</span></div>
                <h3 style="margin-top:1rem;">CAPL 证据覆盖</h3>
                <div class="cov-item"><span class="cov-label">已解析符号</span><span class="cov-value">{resolved} / {required_sym}</span></div>
                <div class="cov-item"><span class="cov-label">缺口数</span><span class="cov-value">{gap_count}</span></div>
            </div>
        </div>
        {f'<div class="risk-list"><h3>⚠️ 风险项 ({len(risks)})</h3>{"".join(risk_items)}</div>' if risks else ''}
    </section>
    """


def _build_artifacts_section(state_data: Dict[str, Any]) -> str:
    artifacts: List[tuple[str, Any]] = [
        ("CFG 制品", _get(state_data, "cfg_artifact")),
        ("CAN 制品", _get(state_data, "can_artifact")),
        ("配置评估", _get(state_data, "config_eval_report")),
        ("CAPL 评估", _get(state_data, "capl_eval_report")),
        ("测试报告计划", _get(state_data, "test_report_plan")),
    ]

    output_root = _as_text(_get(state_data, "output_root", ""))

    items: List[str] = []
    for label, artifact in artifacts:
        if not artifact:
            continue
        if isinstance(artifact, dict):
            path = _as_text(artifact.get("path") or artifact.get("file") or artifact.get("output_file", ""))
            status = _as_text(artifact.get("status", ""))
        else:
            path = _as_text(artifact)
            status = ""
        if not path and output_root:
            # Just show the label with output root
            path = output_root
        color = _status_color(status) if status else _ACCENT
        status_pill = ""
        if status:
            status_pill = (
                f'<span class="pill" style="background:{color};'
                f' color:#1a1a2e;">{_escape(_status_label(status))}</span>'
            )
        items.append(
            f'<div class="artifact-item">'
            f'<span class="artifact-label">{_escape(label)}</span>'
            f'<code class="artifact-path">{_escape(path)}</code>'
            f'{status_pill}'
            f'</div>'
        )

    if not items:
        return '<section class="content-section"><h2>📦 制品</h2><p class="empty-msg">无制品数据</p></section>'

    return f"""
    <section class="content-section">
        <h2>📦 制品</h2>
        <div class="artifact-list">{''.join(items)}</div>
    </section>
    """


def _build_repair_section(state_data: Dict[str, Any]) -> str:
    repair_plan = _get(state_data, "repair_plan")
    status = _as_text(_get(state_data, "status", "")).lower()

    # Show repair section if blocked or if repair plan exists
    if not repair_plan and status not in ("blocked", "blocked_for_corrections"):
        return ""

    if not isinstance(repair_plan, dict):
        # repair_plan might be a file path
        if repair_plan:
            return f"""
            <section class="content-section repair-section">
                <h2>🛠️ 修复计划</h2>
                <div class="artifact-item">
                    <span class="artifact-label">修复计划文件</span>
                    <code class="artifact-path">{_escape(repair_plan)}</code>
                </div>
            </section>
            """
        return ""

    actions = repair_plan.get("actions", [])
    summary = _as_text(repair_plan.get("summary", ""))

    action_items: List[str] = []
    for action in actions:
        if isinstance(action, dict):
            action_items.append(
                f'<div class="action-item">'
                f'<span class="action-priority">{_escape(action.get("priority", ""))}</span>'
                f'<span class="action-desc">{_escape(action.get("description", action.get("action", "")))}</span>'
                f'</div>'
            )
        elif isinstance(action, str):
            action_items.append(f'<div class="action-item"><span class="action-desc">{_escape(action)}</span></div>')

    return f"""
    <section class="content-section repair-section">
        <h2>🛠️ 修复计划</h2>
        {f'<p class="repair-summary">{_escape(summary)}</p>' if summary else ''}
        {f'<div class="action-list">{"".join(action_items)}</div>' if action_items else '<p class="empty-msg">无具体修复动作</p>'}
    </section>
    """


# ---------------------------------------------------------------------------
# CSS
# ---------------------------------------------------------------------------

_CSS = f"""
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{
    background: {_BG};
    color: {_TEXT};
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans SC", "Microsoft YaHei", sans-serif;
    line-height: 1.6;
    padding: 1.5rem;
    max-width: 1200px;
    margin: 0 auto;
}}
.report-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: {_CARD};
    border: 1px solid {_BORDER};
    border-radius: 12px;
    padding: 1.5rem 2rem;
    margin-bottom: 1.5rem;
}}
.header-left h1 {{
    font-size: 1.5rem;
    color: {_TEXT};
    margin-bottom: 0.5rem;
}}
.header-meta {{
    display: flex;
    gap: 1.5rem;
    font-size: 0.85rem;
}}
.meta-label {{
    color: {_TEXT_DIM};
    margin-right: 0.3rem;
}}
.meta-item code {{
    background: {_ACCENT};
    padding: 0.15rem 0.4rem;
    border-radius: 4px;
    font-size: 0.8rem;
}}
.status-badge {{
    padding: 0.5rem 1.2rem;
    border-radius: 8px;
    font-weight: 700;
    font-size: 0.9rem;
    white-space: nowrap;
}}
.summary-section {{
    margin-bottom: 1.5rem;
}}
.card-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 1rem;
}}
.summary-card {{
    background: {_CARD};
    border: 1px solid {_BORDER};
    border-radius: 10px;
    padding: 1.2rem;
    text-align: center;
}}
.card-value {{
    font-size: 1.8rem;
    font-weight: 700;
    margin-bottom: 0.3rem;
}}
.card-label {{
    color: {_TEXT_DIM};
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}}
.content-section {{
    background: {_CARD};
    border: 1px solid {_BORDER};
    border-radius: 10px;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
}}
.content-section h2 {{
    font-size: 1.1rem;
    margin-bottom: 1rem;
    color: {_TEXT};
}}
.content-section h3 {{
    font-size: 0.95rem;
    margin-bottom: 0.6rem;
    color: {_TEXT_DIM};
}}
.table-wrap {{
    overflow-x: auto;
}}
table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 0.85rem;
}}
th {{
    text-align: left;
    padding: 0.6rem 0.8rem;
    color: {_TEXT_DIM};
    border-bottom: 2px solid {_BORDER};
    white-space: nowrap;
}}
td {{
    padding: 0.5rem 0.8rem;
    border-bottom: 1px solid {_BORDER};
}}
tr:hover td {{
    background: rgba(15, 52, 96, 0.3);
}}
.msg-cell {{
    max-width: 400px;
    word-break: break-word;
}}
.pill {{
    display: inline-block;
    padding: 0.15rem 0.6rem;
    border-radius: 12px;
    font-size: 0.75rem;
    font-weight: 600;
    text-transform: uppercase;
}}
.empty-msg {{
    color: {_TEXT_DIM};
    font-style: italic;
    padding: 0.5rem 0;
}}
.cov-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.5rem;
}}
.cov-block h3 {{
    margin-bottom: 0.5rem;
}}
.cov-item {{
    display: flex;
    justify-content: space-between;
    padding: 0.3rem 0;
    border-bottom: 1px solid {_BORDER};
    font-size: 0.85rem;
}}
.cov-label {{
    color: {_TEXT_DIM};
}}
.cov-value {{
    font-weight: 600;
}}
.risk-list {{
    margin-top: 1rem;
}}
.risk-item {{
    display: flex;
    align-items: center;
    gap: 0.6rem;
    padding: 0.4rem 0;
    font-size: 0.85rem;
}}
.risk-msg {{
    color: {_TEXT};
}}
.artifact-list {{
    display: flex;
    flex-direction: column;
    gap: 0.6rem;
}}
.artifact-item {{
    display: flex;
    align-items: center;
    gap: 0.8rem;
    padding: 0.5rem 0;
    border-bottom: 1px solid {_BORDER};
}}
.artifact-label {{
    color: {_TEXT_DIM};
    font-size: 0.85rem;
    min-width: 100px;
}}
.artifact-path {{
    color: {_ACCENT};
    background: {_BG};
    padding: 0.2rem 0.5rem;
    border-radius: 4px;
    font-size: 0.8rem;
    flex: 1;
    overflow-x: auto;
    white-space: nowrap;
}}
.repair-section {{
    border-color: {_ERROR};
}}
.repair-summary {{
    margin-bottom: 1rem;
    color: {_WARNING};
}}
.action-list {{
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}}
.action-item {{
    display: flex;
    align-items: center;
    gap: 0.8rem;
    padding: 0.5rem 0.8rem;
    background: {_BG};
    border-radius: 6px;
    font-size: 0.85rem;
}}
.action-priority {{
    background: {_ERROR};
    color: {_BG};
    padding: 0.1rem 0.5rem;
    border-radius: 4px;
    font-size: 0.75rem;
    font-weight: 700;
    white-space: nowrap;
}}
.action-desc {{
    color: {_TEXT};
}}
footer {{
    text-align: center;
    color: {_TEXT_DIM};
    font-size: 0.75rem;
    padding: 1rem 0;
}}
@media (max-width: 768px) {{
    .report-header {{ flex-direction: column; gap: 1rem; }}
    .cov-grid {{ grid-template-columns: 1fr; }}
    .header-meta {{ flex-direction: column; gap: 0.3rem; }}
}}
"""


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def generate_run_report(
    state_data: Dict[str, Any],
    output_path: Path,
) -> Dict[str, Any]:
    """Generate a self-contained HTML run summary report.

    Parameters
    ----------
    state_data
        Dictionary containing run information.  Expected keys: ``run_id``,
        ``status``, ``structured_test_case``, ``correction_items``,
        ``evidence_bundle``, ``coverage_report``, ``cfg_artifact``,
        ``can_artifact``, ``config_eval_report``, ``capl_eval_report``,
        ``repair_plan``, ``output_root``.
    output_path
        Destination ``.html`` file path.

    Returns
    -------
    dict
        ``{"path": str(output_path), "status": "generated"}``
    """

    output_path = Path(output_path)
    _ensure_dir(output_path)

    sections: List[str] = [
        _build_header(state_data),
        _build_summary_cards(state_data),
        _build_test_cases_table(state_data),
        _build_corrections_table(state_data),
        _build_evidence_section(state_data),
        _build_coverage_section(state_data),
        _build_artifacts_section(state_data),
        _build_repair_section(state_data),
    ]

    # Only include non-empty sections
    body_content = "\n".join(s for s in sections if s.strip())

    footer_ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    html_content = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CANoe 配置自动生成 — 运行报告</title>
    <style>{_CSS}</style>
</head>
<body>
{body_content}
<footer>CANoe Cfg AutoGene — 生成于 {_escape(footer_ts)}</footer>
</body>
</html>"""

    output_path.write_text(html_content, encoding="utf-8")

    return {
        "path": str(output_path),
        "status": "generated",
    }


def generate_quick_summary(state_data: Dict[str, Any]) -> str:
    """Return a one-line text summary of the run.

    Example
    -------
    >>> generate_quick_summary(state)
    'Run abc123: 5 cases, 12 steps, 2 corrections, status=complete'

    Parameters
    ----------
    state_data
        Dictionary containing run information.

    Returns
    -------
    str
        One-line summary string.
    """

    run_id = _as_text(_get(state_data, "run_id", "unknown"))
    status = _as_text(_get(state_data, "status", "unknown"))

    structured = _get(state_data, "structured_test_case", {}) or {}
    cases = structured.get("cases", []) if isinstance(structured, dict) else []
    case_count = len(cases)
    step_count = sum(
        len(c.get("steps", [])) for c in cases if isinstance(c, dict)
    )

    corrections = _get(state_data, "correction_items", []) or []
    correction_count = len(corrections)

    return (
        f"Run {run_id}: {case_count} cases, {step_count} steps, "
        f"{correction_count} corrections, status={status}"
    )
