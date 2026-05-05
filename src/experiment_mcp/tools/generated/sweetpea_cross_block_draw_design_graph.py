"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '785edbf2a875664f5658f1cc079981080b1cb68967dbba56ca8b087dea1fdda4'
__exp_qualname__ = 'sweetpea.CrossBlock.draw_design_graph'
__exp_kind__ = 'method'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'draw_design_graph'
TOOL_DESCRIPTION = 'Call this tool after constructing a CrossBlock (via the CrossBlock constructor tool) to render a visual graph of the experimental design — factors and their crossings. Use it during the SweetPea design phase (step 1 of the pipeline), before sampling a trial sequence, to inspect and debug factorial structure. The method has no return value; its effect is the rendered graph display.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "crossblock": {\n      "description": "Handle string for the CrossBlock instance whose design graph should be drawn \\u2014 the string returned by the CrossBlock constructor tool.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "crossblock"\n  ],\n  "type": "object"\n}\n\nNotes:\ndraw_design_graph() calls matplotlib (or a similar display backend) via dg.draw() as a side effect with no return value. In headless or server environments the display call may silently no-op, raise a display error, or write to a file depending on the backend configured — verify the runtime environment supports GUI output before relying on this tool. Do not call this after sampling or in the SweetBean phase; it is purely a design-time inspection aid.'
TOOL_PARAMETERS = { 'properties': { 'crossblock': { 'description': 'Handle string for the CrossBlock '
                                                 'instance whose design graph should '
                                                 'be drawn — the string returned by '
                                                 'the CrossBlock constructor tool.',
                                  'type': 'string'}},
  'required': ['crossblock'],
  'type': 'object'}
TOOL_NOTES = 'draw_design_graph() calls matplotlib (or a similar display backend) via dg.draw() as a side effect with no return value. In headless or server environments the display call may silently no-op, raise a display error, or write to a file depending on the backend configured — verify the runtime environment supports GUI output before relying on this tool. Do not call this after sampling or in the SweetBean phase; it is purely a design-time inspection aid.'


def _impl(kwargs: dict[str, Any]) -> Any:
    cls = sp.CrossBlock
    resolved = handles.resolve_in(kwargs)
    instance = resolved.pop('cross_block', None)
    if instance is None:
        raise TypeError(
            f"{TOOL_NAME} requires kwarg 'cross_block' "
            f"(handle returned by create_cross_block)."
        )
    if not isinstance(instance, cls):
        raise TypeError(
            f"{TOOL_NAME} got 'cross_block'={type(instance).__name__}, "
            f"expected CrossBlock."
        )
    result = instance.draw_design_graph(**resolved)
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
    def draw_design_graph(args: dict[str, Any] | None = None) -> Any:
        'Call this tool after constructing a CrossBlock (via the CrossBlock constructor tool) to render a visual graph of the experimental design — factors and their crossings.'
        return _impl(args or {})
