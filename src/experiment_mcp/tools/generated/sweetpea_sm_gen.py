"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'b8b33ec62940798283654c520f7902f8babd511857abbd69fcbb3090c2e53622'
__exp_qualname__ = 'sweetpea.SMGen'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_sm_gen'
TOOL_DESCRIPTION = 'Call this tool to instantiate an SMGen sampling-strategy object when you have a MultiCrossBlockRepeat block and want to sample trial sequences without SAT solving. Pass the returned handle to a synthesis tool (e.g. `sweetpea_gen`) as the `sampling_strategy` argument. SMGen is faster than SAT-based strategies but only works on single-crossing, unconstrained blocks.\n\nParameters (JSON Schema):\n{\n  "properties": {},\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nHard restrictions — SMGen will exit with an error if: (1) the block is not a MultiCrossBlockRepeat (plain CrossBlock is unsupported); (2) the block has more than one crossing; (3) the block carries any AtMostKInARow, AtLeastKInARow, ExactlyK, Exclude, or Pin constraints; (4) within_block_count ≠ trials_per_sample (i.e. repeated-block configurations). SMGen handles minimum_trials / level-weighting internally by duplicating levels, so that case is fine. No constructor arguments are needed; the class is a stateless strategy object.'
TOOL_PARAMETERS = {'properties': {}, 'required': [], 'type': 'object'}
TOOL_NOTES = 'Hard restrictions — SMGen will exit with an error if: (1) the block is not a MultiCrossBlockRepeat (plain CrossBlock is unsupported); (2) the block has more than one crossing; (3) the block carries any AtMostKInARow, AtLeastKInARow, ExactlyK, Exclude, or Pin constraints; (4) within_block_count ≠ trials_per_sample (i.e. repeated-block configurations). SMGen handles minimum_trials / level-weighting internally by duplicating levels, so that case is fine. No constructor arguments are needed; the class is a stateless strategy object.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.SMGen
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
    def create_sm_gen(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to instantiate an SMGen sampling-strategy object when you have a MultiCrossBlockRepeat block and want to sample trial sequences without SAT solving.'
        return _impl(args or {})
