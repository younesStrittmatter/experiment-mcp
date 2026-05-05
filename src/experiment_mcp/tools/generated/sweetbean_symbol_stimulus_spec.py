"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '3282c3ddb41c37c3eb4f2e9c18a65a99ed7a09c781ecbee124509982128d1792'
__exp_qualname__ = 'sweetbean.SymbolStimulusSpec'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_symbol_stimulus_spec'
TOOL_DESCRIPTION = 'Call this tool in SweetBean step (3) to define a geometric symbol stimulus — a shape rendered visually on screen — that can be wired into a Trial or Block. Use it after sampling a SweetPea trial sequence when your design calls for shape-based stimuli (e.g., Stroop-variant or visual search tasks). Returns a SymbolStimulusSpec handle passable to Trial or Block builder tools.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "color": {\n      "default": "#111111",\n      "description": "CSS color for symbol fill/stroke (e.g. \'#ff0000\', \'blue\'). Defaults to \'#111111\' (near-black).",\n      "type": "string"\n    },\n    "rotation_deg": {\n      "description": "Clockwise rotation in degrees. Omit to use 0\\u00b0 (upright). Useful for tilted-rectangle or rotated-cross variants.",\n      "type": "number"\n    },\n    "shape": {\n      "description": "Geometry to render. \'ring\' is a hollow circle; \'cross\' is a plus sign.",\n      "enum": [\n        "circle",\n        "ring",\n        "rectangle",\n        "triangle",\n        "cross"\n      ],\n      "type": "string"\n    },\n    "size_px": {\n      "description": "Symbol bounding-box size in pixels. Omit to use the renderer default of 160 px.",\n      "minimum": 1,\n      "type": "integer"\n    },\n    "stroke_color": {\n      "description": "Outline color as a CSS color string. Only meaningful for shapes that support a distinct stroke (e.g. \'ring\'). Omit to use no separate outline.",\n      "type": "string"\n    },\n    "stroke_width_px": {\n      "description": "Outline width in pixels. Omit to let the renderer pick a shape-specific default when a stroke is needed.",\n      "minimum": 0,\n      "type": "integer"\n    }\n  },\n  "required": [\n    "shape"\n  ],\n  "type": "object"\n}\n\nNotes:\n- Do NOT pass `kind`; it is fixed to "symbol" by the class and the host template sets it automatically.\n- `size_px` silently defaults to 160 px when omitted — set it explicitly if your experiment requires a specific visual angle.\n- `rotation_deg` silently defaults to 0 when omitted.\n- `stroke_color` and `stroke_width_px` are only visually meaningful for shapes that have a stroke variant (notably "ring"); they are accepted but ignored by filled shapes.\n- All color fields expect valid CSS color strings (hex, rgb(), named colors). Invalid strings are not validated at construction time and will silently produce incorrect renders in jsPsych.'
TOOL_PARAMETERS = { 'properties': { 'color': { 'default': '#111111',
                             'description': 'CSS color for symbol fill/stroke (e.g. '
                                            "'#ff0000', 'blue'). Defaults to '#111111' "
                                            '(near-black).',
                             'type': 'string'},
                  'rotation_deg': { 'description': 'Clockwise rotation in degrees. '
                                                   'Omit to use 0° (upright). Useful '
                                                   'for tilted-rectangle or '
                                                   'rotated-cross variants.',
                                    'type': 'number'},
                  'shape': { 'description': "Geometry to render. 'ring' is a hollow "
                                            "circle; 'cross' is a plus sign.",
                             'enum': [ 'circle',
                                       'ring',
                                       'rectangle',
                                       'triangle',
                                       'cross'],
                             'type': 'string'},
                  'size_px': { 'description': 'Symbol bounding-box size in pixels. '
                                              'Omit to use the renderer default of 160 '
                                              'px.',
                               'minimum': 1,
                               'type': 'integer'},
                  'stroke_color': { 'description': 'Outline color as a CSS color '
                                                   'string. Only meaningful for shapes '
                                                   'that support a distinct stroke '
                                                   "(e.g. 'ring'). Omit to use no "
                                                   'separate outline.',
                                    'type': 'string'},
                  'stroke_width_px': { 'description': 'Outline width in pixels. Omit '
                                                      'to let the renderer pick a '
                                                      'shape-specific default when a '
                                                      'stroke is needed.',
                                       'minimum': 0,
                                       'type': 'integer'}},
  'required': ['shape'],
  'type': 'object'}
TOOL_NOTES = '- Do NOT pass `kind`; it is fixed to "symbol" by the class and the host template sets it automatically.\n- `size_px` silently defaults to 160 px when omitted — set it explicitly if your experiment requires a specific visual angle.\n- `rotation_deg` silently defaults to 0 when omitted.\n- `stroke_color` and `stroke_width_px` are only visually meaningful for shapes that have a stroke variant (notably "ring"); they are accepted but ignored by filled shapes.\n- All color fields expect valid CSS color strings (hex, rgb(), named colors). Invalid strings are not validated at construction time and will silently produce incorrect renders in jsPsych.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.SymbolStimulusSpec
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
    def create_symbol_stimulus_spec(args: dict[str, Any] | None = None) -> Any:
        'Call this tool in SweetBean step (3) to define a geometric symbol stimulus — a shape rendered visually on screen — that can be wired into a Trial or Block.'
        return _impl(args or {})
