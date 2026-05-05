"""Auto-generated index. Do not edit by hand.

Will be rewritten by the (future) `scripts/generate_tools.py` on every
successful run, mirroring `psyneulink_mcp.tools.generated.__init__`.
On a fresh clone (no regen yet) the modules tuple is empty and
``register_all`` is a safe no-op so the server boots without any
generated surface present.
"""

from __future__ import annotations

from typing import Any

ALL: tuple[Any, ...] = ()


def register_all(mcp: Any) -> None:
    """Register every generated tool module with ``mcp``."""
    for module in ALL:
        module.register(mcp)
