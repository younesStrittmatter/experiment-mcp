"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'b9dad0a79d8cbe724ffcbdfce53cea29be5f215a7bd50e1078989125a69233ae'
__exp_qualname__ = 'sweetbean.RectangleSpec'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_rectangle_spec'
TOOL_DESCRIPTION = 'Call this tool when constructing a SweetBean stimulus that needs explicit spatial placement within the jsPsych display area — for example, to position an image or text off-center, to restrict a stimulus to a sub-region, or to arrange multiple stimuli side-by-side. Returns a RectangleSpec handle that can be passed as the `spec` argument of a stimulus-creation tool. This tool belongs at step 3 of the pipeline, just before stimulus construction.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "height": {\n      "default": 1,\n      "description": "Height of the rectangle as a fraction of viewport height. 1.0 = full viewport height.",\n      "exclusiveMinimum": 0,\n      "maximum": 1,\n      "type": "number"\n    },\n    "width": {\n      "default": 1,\n      "description": "Width of the rectangle as a fraction of viewport width. 1.0 = full viewport width.",\n      "exclusiveMinimum": 0,\n      "maximum": 1,\n      "type": "number"\n    },\n    "x": {\n      "default": 0.5,\n      "description": "Horizontal center of the rectangle, normalized to viewport width. 0.0 = left edge, 1.0 = right edge, 0.5 = center.",\n      "maximum": 1,\n      "minimum": 0,\n      "type": "number"\n    },\n    "y": {\n      "default": 0.5,\n      "description": "Vertical center of the rectangle, normalized to viewport height. 0.0 = top edge, 1.0 = bottom edge, 0.5 = center.",\n      "maximum": 1,\n      "minimum": 0,\n      "type": "number"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nAll four coordinates are in normalized viewport units (0.0–1.0), not pixels or CSS units. x and y specify the CENTER of the rectangle, not its top-left corner — to place a half-width box flush to the left edge, use x=0.25, width=0.5. The defaults (x=0.5, y=0.5, width=1.0, height=1.0) produce a full-viewport-sized rectangle centered on the display, which is effectively no constraint; only create a RectangleSpec when you need something other than this default layout.'
TOOL_PARAMETERS = { 'properties': { 'height': { 'default': 1,
                              'description': 'Height of the rectangle as a fraction of '
                                             'viewport height. 1.0 = full viewport '
                                             'height.',
                              'exclusiveMinimum': 0,
                              'maximum': 1,
                              'type': 'number'},
                  'width': { 'default': 1,
                             'description': 'Width of the rectangle as a fraction of '
                                            'viewport width. 1.0 = full viewport '
                                            'width.',
                             'exclusiveMinimum': 0,
                             'maximum': 1,
                             'type': 'number'},
                  'x': { 'default': 0.5,
                         'description': 'Horizontal center of the rectangle, '
                                        'normalized to viewport width. 0.0 = left '
                                        'edge, 1.0 = right edge, 0.5 = center.',
                         'maximum': 1,
                         'minimum': 0,
                         'type': 'number'},
                  'y': { 'default': 0.5,
                         'description': 'Vertical center of the rectangle, normalized '
                                        'to viewport height. 0.0 = top edge, 1.0 = '
                                        'bottom edge, 0.5 = center.',
                         'maximum': 1,
                         'minimum': 0,
                         'type': 'number'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'All four coordinates are in normalized viewport units (0.0–1.0), not pixels or CSS units. x and y specify the CENTER of the rectangle, not its top-left corner — to place a half-width box flush to the left edge, use x=0.25, width=0.5. The defaults (x=0.5, y=0.5, width=1.0, height=1.0) produce a full-viewport-sized rectangle centered on the display, which is effectively no constraint; only create a RectangleSpec when you need something other than this default layout.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.RectangleSpec
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
    def create_rectangle_spec(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when constructing a SweetBean stimulus that needs explicit spatial placement within the jsPsych display area — for example, to position an image or text off-center, to restrict a stimulus to a sub-region, or to arrange multiple stimuli side-by-side.'
        return _impl(args or {})
