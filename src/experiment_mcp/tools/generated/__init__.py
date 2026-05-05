"""Auto-generated index. Do not edit by hand.

Rewritten by scripts/generate_tools.py on every successful run.
On a fresh clone (no regen yet) the modules tuple is empty and
register_all is a safe no-op.
"""

from __future__ import annotations

from typing import Any

ALL: tuple[Any, ...] = ()


def register_all(mcp: Any) -> None:
    """Register every generated tool module with ``mcp``."""
    for module in ALL:
        module.register(mcp)
