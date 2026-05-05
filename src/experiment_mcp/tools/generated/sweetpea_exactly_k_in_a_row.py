"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'e6d46e361768f2c735b4cf2633a65221a7f7d7b346143b2bbf97f55d9aeedd6a'
__exp_qualname__ = 'sweetpea.ExactlyKInARow'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_exactly_k_in_a_row'
TOOL_DESCRIPTION = 'Call this tool when designing a SweetPea experimental sequence and you need a specific factor level to appear in runs of *exactly* K consecutive trials — no more, no fewer. Use it at the constraint-definition stage (after declaring Factors and Levels, before calling CrossBlock). The result is a constraint object handle you pass into the `constraints` list of `CrossBlock`.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "k": {\n      "description": "The exact number of consecutive trials in which the specified level must appear whenever it appears at all. E.g. k=2 means every run of that level is exactly 2 trials long.",\n      "minimum": 1,\n      "type": "integer"\n    },\n    "level": {\n      "description": "Handle string referencing the level (or (Factor, Level) tuple) to constrain. Produced by a factor/level creation tool \\u2014 pass the handle string exactly as returned.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "k",\n    "level"\n  ],\n  "type": "object"\n}\n\nNotes:\n- If the level never appears in a trial sequence, the constraint is vacuously satisfied — it only fires when the level is present.\n- Contrast with `AtLeastKInARow` (runs of ≥ K) and `AtMostKInARow` (runs of ≤ K); use `ExactlyKInARow` only when you need the run length pinned precisely.\n- The constraint is enforced via SAT encoding; very large `k` values relative to total trial count may make the design unsatisfiable — check for `UnsatisfiableConstraintError` in the CrossBlock call.\n- Pass the returned handle into the `constraints` list of `CrossBlock`, not directly to any SweetBean tool.'
TOOL_PARAMETERS = { 'properties': { 'k': { 'description': 'The exact number of consecutive trials in '
                                        'which the specified level must appear '
                                        'whenever it appears at all. E.g. k=2 means '
                                        'every run of that level is exactly 2 trials '
                                        'long.',
                         'minimum': 1,
                         'type': 'integer'},
                  'level': { 'description': 'Handle string referencing the level (or '
                                            '(Factor, Level) tuple) to constrain. '
                                            'Produced by a factor/level creation tool '
                                            '— pass the handle string exactly as '
                                            'returned.',
                             'type': 'string'}},
  'required': ['k', 'level'],
  'type': 'object'}
TOOL_NOTES = '- If the level never appears in a trial sequence, the constraint is vacuously satisfied — it only fires when the level is present.\n- Contrast with `AtLeastKInARow` (runs of ≥ K) and `AtMostKInARow` (runs of ≤ K); use `ExactlyKInARow` only when you need the run length pinned precisely.\n- The constraint is enforced via SAT encoding; very large `k` values relative to total trial count may make the design unsatisfiable — check for `UnsatisfiableConstraintError` in the CrossBlock call.\n- Pass the returned handle into the `constraints` list of `CrossBlock`, not directly to any SweetBean tool.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.ExactlyKInARow
    resolved = handles.resolve_in(kwargs)
    result = target(**resolved)
    try:
        json.dumps(result)
    except (TypeError, ValueError):
        payload = handles.register_handle(result)
        handles.record_call(
            TOOL_NAME,
            kwargs,
            result_handle=payload.get('handle') if isinstance(payload, dict) else None,
            tool_layer="generated",
        )
        return payload
    handles.record_call(TOOL_NAME, kwargs, result_handle=None, tool_layer="generated")
    return result


def register(mcp: Any) -> None:
    @captured_tool(mcp, layer="generated", name=TOOL_NAME, description=TOOL_DESCRIPTION)
    def create_exactly_k_in_a_row(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when designing a SweetPea experimental sequence and you need a specific factor level to appear in runs of *exactly* K consecutive trials — no more, no fewer.'
        return _impl(args or {})
