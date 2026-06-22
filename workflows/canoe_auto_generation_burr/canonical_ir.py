"""Canonical IR field mapping for CANoe_Gene.

Maps Chinese Excel field names to stable English field IDs so that internal
code does not depend on display strings.  The Chinese names live only at the
input adapter boundary (template parser); all downstream modules use the
canonical IDs defined here.

Usage:
    from .canonical_ir import to_canonical, canonicalize_row, CANONICAL_FIELD_MAP

    canonical_row = canonicalize_row(excel_row)   # Chinese keys -> English keys
    field_id = to_canonical("CANoe通道名")          # -> "canoe_channel_name"
"""
from __future__ import annotations

from typing import Any, Dict


# -- Field name mapping: Chinese Excel display name -> stable English field ID --

CANONICAL_FIELD_MAP: Dict[str, str] = {
    # Project config — basic
    "工程名称": "project_name",
    "目标 CANoe 版本": "target_canoe_version",
    # Channel config
    "CANoe通道名": "canoe_channel_name",
    "仲裁波特率": "arbitration_baudrate",
    "数据波特率(CANFD)": "data_baudrate_canfd",
    "采样点%": "sample_point_percent",
    "总线类型": "bus_type",
    "DBC路径": "dbc_path",
    "A2L路径": "a2l_path",
    "CDD路径": "cdd_path",
    # Test case row fields
    "用例ID": "case_id",
    "需求ID": "requirement_id",
    "步骤序号": "step_number",
    "操作类型": "operation_type",
    "操作对象": "operation_target",
    "操作通道": "operation_channel",
    "操作值/参数": "operation_value",
    "条件类型": "condition_type",
    "条件对象": "condition_target",
    "条件期望值": "condition_expected_value",
    "结果类型": "result_type",
    "结果对象": "result_target",
    "结果期望值": "result_expected_value",
    # Strategy / flags
    "启用团队代码规范": "enable_team_coding_standards",
    "启用源文件严格校验": "enable_strict_source_validation",
    "CANoe 实机编译校验": "canoe_compile_validation",
    "测试报告格式": "test_report_format",
}

# Reverse map: English field ID -> Chinese display name (for back-translation)
REVERSE_FIELD_MAP: Dict[str, str] = {v: k for k, v in CANONICAL_FIELD_MAP.items()}

# -- Operation type canonical mapping --

CANONICAL_OPERATION_TYPES: Dict[str, str] = {
    "无操作": "no_op",
    "等待手动操作后确认": "wait_manual_confirm",
    "CAN报文发送": "can_message_send",
    "CAN报文停发": "can_message_stop",
    "CAN报文周期调整": "can_message_period_adjust",
    "CAN信号赋值": "can_signal_assign",
    "XCP标定量赋值": "xcp_calibration_assign",
    "诊断服务请求": "diagnostic_service_request",
}

# -- Condition type canonical mapping --

CANONICAL_CONDITION_TYPES: Dict[str, str] = {
    "无条件": "no_condition",
    "等待固定时间": "wait_fixed_time",
    "等待手动操作后确认": "wait_manual_confirm",
    "接收CAN报文发送": "receive_can_message",
    "接收CAN报文超时": "receive_can_message_timeout",
    "CAN信号变化": "can_signal_change",
    "观测量变化": "measurement_change",
    "诊断服务响应": "diagnostic_service_response",
}

# -- Result type canonical mapping --

CANONICAL_RESULT_TYPES: Dict[str, str] = {
    "无结果": "no_result",
    "接收CAN报文发送": "receive_can_message",
    "接收CAN报文超时": "receive_can_message_timeout",
    "CAN信号变化": "can_signal_change",
    "观测量变化": "measurement_change",
    "诊断服务响应": "diagnostic_service_response",
}


def to_canonical(chinese_name: str) -> str:
    """Convert a Chinese Excel field name to its canonical English ID.

    If the name is not in the mapping, it is returned unchanged (pass-through
    for already-canonical or unknown fields).
    """
    return CANONICAL_FIELD_MAP.get(chinese_name, chinese_name)


def to_display(canonical_id: str) -> str:
    """Convert a canonical English field ID back to its Chinese display name."""
    return REVERSE_FIELD_MAP.get(canonical_id, canonical_id)


def canonicalize_row(row: Dict[str, Any]) -> Dict[str, Any]:
    """Convert all keys in a row dict from Chinese display names to canonical IDs."""
    return {to_canonical(k): v for k, v in row.items()}


def canonicalize_operation_type(chinese_value: str) -> str:
    return CANONICAL_OPERATION_TYPES.get(chinese_value, chinese_value)


def canonicalize_condition_type(chinese_value: str) -> str:
    return CANONICAL_CONDITION_TYPES.get(chinese_value, chinese_value)


def canonicalize_result_type(chinese_value: str) -> str:
    return CANONICAL_RESULT_TYPES.get(chinese_value, chinese_value)
