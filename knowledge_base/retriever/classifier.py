"""Classify a user query into 'exact' / 'semantic' / 'hybrid'.

The classification is intentionally lightweight (regex + heuristics) so
we don't add a model call on the hot path.  For complex agents you can
swap this for an LLM-based router.
"""

from __future__ import annotations
import re
from typing import Literal

QueryKind = Literal["exact", "semantic", "hybrid"]

_CODE_CALL_RE = re.compile(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*\(")
_CAMEL_RE     = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
_VERSION_RE   = re.compile(r"\bv(12|15|16|17|18|19|20)\b", re.I)
_QUESTION_HINT = ("?", "？", "怎么", "如何", "怎样", "怎么用", "what is", "how",
                  "why", "when", "where", "which", "show me", "list")


def classify(query: str) -> QueryKind:
    q = (query or "").strip()
    if not q:
        return "semantic"

    # 1) Code-like or symbol query
    if _CODE_CALL_RE.search(q):
        return "exact"
    if _CAMEL_RE.match(q) and " " not in q and len(q) <= 40:
        return "exact"

    # 2) Short keyword string
    tokens = q.split()
    if len(tokens) <= 2 and all(_CAMEL_RE.match(t) for t in tokens):
        return "exact"

    # 3) Natural language question
    if any(h in q.lower() for h in _QUESTION_HINT):
        return "semantic"
    if len(q) > 30:
        return "semantic"

    return "hybrid"
