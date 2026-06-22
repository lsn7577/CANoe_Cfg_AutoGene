"""Enhanced CAPL static lint module.

This module provides regex-based static analysis for generated CAPL source files.
It goes beyond simple brace counting by checking headers, variable blocks,
testcase counts, deprecated APIs, parenthesis balance, missing semicolons,
duplicate testcase names, empty bodies, and event handler correctness.

Each check is implemented as a standalone function for maintainability.
The main entry point ``lint_capl_source`` aggregates all results.
"""

from __future__ import annotations

import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Dict, List


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------


@dataclass
class CaplLintIssue:
    """A single lint issue found in a CAPL source file.

    Attributes:
        severity: ``"error"`` or ``"warning"``.
        line: 1-based line number where the issue was detected.
        column: 1-based column number (0 if not applicable).
        message: Human-readable description of the issue.
    """

    severity: str
    line: int
    column: int
    message: str

    def to_dict(self) -> Dict[str, Any]:
        """Return a plain-dict representation (for JSON serialisation)."""
        return asdict(self)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _read_text(path: Path) -> str:
    """Read a file with multiple encoding fallbacks."""
    for encoding in ("utf-8-sig", "utf-8", "gb18030", "latin-1"):
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue
    return path.read_text(encoding="utf-8", errors="replace")


def _strip_comment(line: str) -> str:
    """Remove ``//`` line comments from *line* (block comments are not handled)."""
    idx = line.find("//")
    if idx != -1:
        line = line[:idx]
    return line.rstrip()


def _line_has_trailing_brace_or_comment(raw_line: str) -> bool:
    """Return True if *raw_line* ends with ``{``, ``}``, or a comment."""
    stripped = raw_line.rstrip()
    if not stripped:
        return True
    if stripped.endswith("{") or stripped.endswith("}"):
        return True
    if stripped.endswith("//") or "//" in stripped:
        return True
    if stripped.endswith("*/"):
        return True
    return False


# ---------------------------------------------------------------------------
# Individual checks — each returns a list of CaplLintIssue
# ---------------------------------------------------------------------------


def check_header(text: str) -> List[CaplLintIssue]:
    """Ensure the source contains the 'Generated for CANoe' header (error)."""
    issues: List[CaplLintIssue] = []
    if "Generated for CANoe" not in text:
        issues.append(CaplLintIssue("error", 1, 0, "Missing 'Generated for CANoe' header"))
    return issues


def check_variables_block(text: str) -> List[CaplLintIssue]:
    """Ensure the source has a ``variables {`` block (error)."""
    issues: List[CaplLintIssue] = []
    if not re.search(r"\bvariables\s*\{", text):
        issues.append(CaplLintIssue("error", 1, 0, "Missing 'variables { ... }' block"))
    return issues


def check_brace_balance(text: str) -> List[CaplLintIssue]:
    """Verify that ``{`` and ``}`` counts are balanced (error)."""
    issues: List[CaplLintIssue] = []
    open_count = text.count("{")
    close_count = text.count("}")
    if open_count != close_count:
        issues.append(CaplLintIssue(
            "error", 1, 0,
            f"Unbalanced braces: {open_count} opening vs {close_count} closing",
        ))
    return issues


def check_testcase_count(text: str, expected_cases: int) -> List[CaplLintIssue]:
    """Verify testcase count matches *expected_cases* (error)."""
    issues: List[CaplLintIssue] = []
    testcase_count = len(re.findall(r"\btestcase\s+[A-Za-z_][A-Za-z0-9_]*\s*\(", text))
    if testcase_count != expected_cases:
        issues.append(CaplLintIssue(
            "error", 1, 0,
            f"Testcase count mismatch: expected {expected_cases}, got {testcase_count}",
        ))
    return issues


def check_unverified_api(text: str) -> List[CaplLintIssue]:
    """Ensure no ``TODO_UNVERIFIED_API`` placeholder remains (error)."""
    issues: List[CaplLintIssue] = []
    for lineno, line in enumerate(text.splitlines(), 1):
        if "TODO_UNVERIFIED_API" in line:
            col = line.index("TODO_UNVERIFIED_API") + 1
            issues.append(CaplLintIssue(
                "error", lineno, col,
                "Unverified API placeholder 'TODO_UNVERIFIED_API' found",
            ))
    return issues


def check_output_without_message(text: str) -> List[CaplLintIssue]:
    """If ``output(`` is used, a ``message <Type> <name>;`` declaration must exist (error)."""
    issues: List[CaplLintIssue] = []
    if "output(" in text and not re.search(
        r"\bmessage\s+[A-Za-z_][A-Za-z0-9_]*\s+[A-Za-z_][A-Za-z0-9_]*\s*;", text,
    ):
        issues.append(CaplLintIssue(
            "error", 1, 0,
            "output() is used but no CAPL message variable is declared",
        ))
    return issues


def check_paren_balance(text: str) -> List[CaplLintIssue]:
    """Warn about unmatched parentheses on a per-function basis (warning)."""
    issues: List[CaplLintIssue] = []
    # Split text into top-level function blocks by tracking brace depth.
    lines = text.splitlines()
    func_start_pattern = re.compile(
        r"^\s*(?:testcase\s+|on\s+\w+\s+|[A-Za-z_][A-Za-z0-9_ \t]*\s+) "
        r"[A-Za-z_][A-Za-z0-9_]*\s*\(",
    )
    current_func_start: int | None = None
    brace_depth = 0
    open_parens = 0
    close_parens = 0
    for idx, line in enumerate(lines):
        code = _strip_comment(line)
        if current_func_start is None:
            if func_start_pattern.match(code) or re.match(r"^\s*(?:testcase\s+|[A-Za-z_])", code) and "(" in code:
                # Heuristic: a line that looks like a function/testcase/on handler start
                if re.match(r"^\s*(testcase\s+|on\s+\w+|[A-Za-z_][A-Za-z0-9_]*\s+[A-Za-z_][A-Za-z0-9_]*)", code) and "(" in code:
                    current_func_start = idx + 1
                    brace_depth = 0
                    open_parens = 0
                    close_parens = 0
        if current_func_start is not None:
            open_parens += code.count("(")
            close_parens += code.count(")")
            brace_depth += code.count("{") - code.count("}")
            if brace_depth <= 0 and "{" in code:
                # Function body ended
                if open_parens != close_parens:
                    issues.append(CaplLintIssue(
                        "warning", current_func_start, 0,
                        f"Unmatched parentheses in function starting at line {current_func_start}: "
                        f"{open_parens} '(' vs {close_parens} ')'",
                    ))
                current_func_start = None
                brace_depth = 0
    return issues


def check_missing_semicolons(text: str) -> List[CaplLintIssue]:
    """Warn about statement lines that look like they're missing a semicolon (warning)."""
    issues: List[CaplLintIssue] = []
    for lineno, raw_line in enumerate(text.splitlines(), 1):
        code = raw_line.strip()
        if not code:
            continue
        # Skip preprocessor directives
        if code.startswith("#"):
            continue
        # Skip lines ending with {, }, or comments
        if _line_has_trailing_brace_or_comment(raw_line):
            continue
        # Skip lines that are just a closing paren or bracket
        if code in ("}", ")", "]", "});", ");"):
            continue
        # Skip control-flow keywords
        if re.match(r"^\s*(if|else|for|while|switch|case|default|do|break|continue|return)\b", code):
            if not code.endswith(";") and not code.endswith("{") and not code.endswith("}"):
                # return without semicolon — could be a void return
                if code.startswith("return") and not code.endswith(";"):
                    issues.append(CaplLintIssue(
                        "warning", lineno, len(code),
                        f"Statement may be missing a semicolon: '{code[:60]}'",
                    ))
            continue
        # Lines that contain assignment or function call
        looks_like_statement = (
            "=" in code
            or re.search(r"[A-Za-z_][A-Za-z0-9_]*\s*\(", code)
        )
        if looks_like_statement and not code.endswith(";"):
            # Skip lines that end with a comma (multi-line declarations)
            if code.endswith(","):
                continue
            issues.append(CaplLintIssue(
                "warning", lineno, len(code),
                f"Statement may be missing a semicolon: '{code[:60]}'",
            ))
    return issues


def check_duplicate_testcase_names(text: str) -> List[CaplLintIssue]:
    """Warn if the same testcase function name appears more than once (warning)."""
    issues: List[CaplLintIssue] = []
    seen: Dict[str, int] = {}
    for match in re.finditer(r"\btestcase\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(", text):
        name = match.group(1)
        lineno = text[:match.start()].count("\n") + 1
        if name in seen:
            issues.append(CaplLintIssue(
                "warning", lineno, match.start() - text.rfind("\n", 0, match.start()),
                f"Duplicate testcase name: '{name}' (first seen at line {seen[name]})",
            ))
        else:
            seen[name] = lineno
    return issues


def check_empty_testcase_bodies(text: str) -> List[CaplLintIssue]:
    """Warn if a testcase function has an empty body (warning)."""
    issues: List[CaplLintIssue] = []
    # Match testcase definition with its body
    pattern = re.compile(
        r"\btestcase\s+[A-Za-z_][A-Za-z0-9_]*\s*\([^)]*\)\s*\{(\s*)\}",
        re.DOTALL,
    )
    for match in pattern.finditer(text):
        lineno = text[:match.start()].count("\n") + 1
        issues.append(CaplLintIssue(
            "warning", lineno, 0,
            "Testcase has an empty body",
        ))
    # Also check for testcase with only whitespace/comments inside
    pattern2 = re.compile(
        r"\btestcase\s+([A-Za-z_][A-Za-z0-9_]*)\s*\([^)]*\)\s*\{",
    )
    for match in pattern2.finditer(text):
        brace_start = match.end() - 1  # position of '{'
        depth = 0
        i = brace_start
        body_content = ""
        while i < len(text):
            if text[i] == "{":
                depth += 1
            elif text[i] == "}":
                depth -= 1
                if depth == 0:
                    break
            else:
                body_content += text[i]
            i += 1
        # Remove comments from body content
        cleaned = re.sub(r"//[^\n]*", "", body_content)
        cleaned = re.sub(r"/\*.*?\*/", "", cleaned, flags=re.DOTALL)
        if not cleaned.strip():
            lineno = text[:match.start()].count("\n") + 1
            # Avoid duplicate if already caught by simple pattern
            already_reported = any(
                issue.line == lineno and "empty body" in issue.message
                for issue in issues
            )
            if not already_reported:
                issues.append(CaplLintIssue(
                    "warning", lineno, 0,
                    f"Testcase '{match.group(1)}' has an empty body (only comments/whitespace)",
                ))
    return issues


def check_event_handlers(text: str) -> List[CaplLintIssue]:
    """Warn if ``on message``/``on timer``/``on key`` lacks a following ``{`` (warning)."""
    issues: List[CaplLintIssue] = []
    pattern = re.compile(r"\bon\s+(message|timer|key)\b", re.IGNORECASE)
    for match in pattern.finditer(text):
        lineno = text[:match.start()].count("\n") + 1
        # Look forward from the match position for the next non-whitespace char
        pos = match.end()
        remaining = text[pos:]
        remaining_stripped = remaining.lstrip()
        # Skip the event parameter: identifiers, numbers, *, quoted chars/strings,
        # and parenthesised expressions (e.g. on key 'a', on message Msg1, on timer T1)
        param_pattern = re.compile(
            r"([A-Za-z_][A-Za-z0-9_]*"  # identifiers
            r"|\d+"                       # numbers
            r"|\*"                        # wildcard
            r"|'[^']*'"                   # single-quoted char
            r'|"[^"]*"'                   # double-quoted string
            r"|\([^)]*\))"                # parenthesised expression
            r"\s*",
        )
        id_match = param_pattern.match(remaining_stripped)
        if id_match:
            remaining_stripped = remaining_stripped[id_match.end():]
        remaining_stripped = remaining_stripped.lstrip()
        # Now check if the next meaningful character is '{'
        if not remaining_stripped.startswith("{"):
            issues.append(CaplLintIssue(
                "warning", lineno, 0,
                f"Event handler 'on {match.group(1)}' may be missing a handler body '{{'",
            ))
    return issues


def check_deprecated_apis(text: str) -> List[CaplLintIssue]:
    """Warn if deprecated APIs like ``putValue()`` or ``getValue()`` are used (warning)."""
    issues: List[CaplLintIssue] = []
    deprecated_patterns = [
        (re.compile(r"\bputValue\s*\("), "putValue()"),
        (re.compile(r"\bgetValue\s*\("), "getValue()"),
    ]
    for pattern, api_name in deprecated_patterns:
        for match in pattern.finditer(text):
            lineno = text[:match.start()].count("\n") + 1
            col = match.start() - text.rfind("\n", 0, match.start())
            issues.append(CaplLintIssue(
                "warning", lineno, col,
                f"Deprecated API usage: '{api_name}' — consider using newer alternatives",
            ))
    return issues


def check_includes(text: str) -> List[CaplLintIssue]:
    """Warn if ``#include`` paths look like system paths (warning)."""
    issues: List[CaplLintIssue] = []
    include_pattern = re.compile(r'#include\s+[<"]([^>"]+)[>"]')
    for match in include_pattern.finditer(text):
        include_path = match.group(1)
        lineno = text[:match.start()].count("\n") + 1
        col = match.start() - text.rfind("\n", 0, match.start()) + 1
        # Warn if path uses angle brackets (system-style include)
        if text[match.start():match.end()].count(">") > 0 and text[match.start():match.end()].count("<") > 0:
            issues.append(CaplLintIssue(
                "warning", lineno, col,
                f"#include uses angle brackets (system-style): '{include_path}' — "
                "CAPL includes should typically use quotes for project-relative paths",
            ))
        # Warn if path looks like an absolute system path
        if re.match(r"^[A-Za-z]:[\\/]", include_path) or include_path.startswith("/"):
            issues.append(CaplLintIssue(
                "warning", lineno, col,
                f"#include uses an absolute path: '{include_path}' — "
                "prefer relative paths for portability",
            ))
    return issues


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------


def lint_capl_source(path: Path, expected_cases: int) -> Dict[str, Any]:
    """Run all static lint checks on a CAPL source file.

    Args:
        path: Path to the ``.can`` CAPL source file.
        expected_cases: Expected number of testcase definitions in the file.

    Returns:
        A dict with keys:

        - ``status``: ``"pass"`` if no errors, ``"fail"`` if any error exists.
        - ``issues``: List of issue dicts (each with severity, line, column, message).
        - ``error_count``: Number of error-severity issues.
        - ``warning_count``: Number of warning-severity issues.
    """
    text = _read_text(path)
    all_issues: List[CaplLintIssue] = []

    # Run all checks
    all_issues.extend(check_header(text))
    all_issues.extend(check_variables_block(text))
    all_issues.extend(check_brace_balance(text))
    all_issues.extend(check_testcase_count(text, expected_cases))
    all_issues.extend(check_unverified_api(text))
    all_issues.extend(check_output_without_message(text))
    all_issues.extend(check_paren_balance(text))
    all_issues.extend(check_missing_semicolons(text))
    all_issues.extend(check_duplicate_testcase_names(text))
    all_issues.extend(check_empty_testcase_bodies(text))
    all_issues.extend(check_event_handlers(text))
    all_issues.extend(check_deprecated_apis(text))
    all_issues.extend(check_includes(text))

    # Sort issues by line, then column, then severity (errors first)
    severity_order = {"error": 0, "warning": 1}
    all_issues.sort(key=lambda i: (i.line, i.column, severity_order.get(i.severity, 2)))

    error_count = sum(1 for i in all_issues if i.severity == "error")
    warning_count = sum(1 for i in all_issues if i.severity == "warning")

    return {
        "status": "fail" if error_count > 0 else "pass",
        "issues": [issue.to_dict() for issue in all_issues],
        "error_count": error_count,
        "warning_count": warning_count,
    }


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------


if __name__ == "__main__":
    import argparse
    import json
    import sys

    parser = argparse.ArgumentParser(description="Static lint for generated CAPL source files.")
    parser.add_argument("path", type=str, help="Path to the .can CAPL source file.")
    parser.add_argument("--expected-cases", type=int, default=0, help="Expected number of testcases.")
    args = parser.parse_args()

    result = lint_capl_source(Path(args.path), args.expected_cases)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(0 if result["status"] == "pass" else 1)
