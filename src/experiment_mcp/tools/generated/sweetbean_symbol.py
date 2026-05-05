"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '60f3d316eea2df415f6ff37ac87476c39b06eb85c88cc48391ee61913ede9cfb'
__exp_qualname__ = 'sweetbean.stimulus.Symbol'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_symbol'
TOOL_DESCRIPTION = 'Call this tool in Step 3 of the pipeline to define a canvas-drawn geometric-shape stimulus for a jsPsych trial. Use it when the trial should display one or more shapes (circle, ring, rectangle, triangle, cross) — rendered via the jsPsychSymbol plugin — and you need control over shape geometry, fill color, texture, timing, and keyboard/mouse response collection. The tool returns a SweetBean Symbol stimulus object (handle string) that you pass into a SweetBean Trial or Block.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "allow_mouse": {\n      "default": false,\n      "description": "If true, a mouse click counts as a valid response. Default false.",\n      "type": "boolean"\n    },\n    "background": {\n      "default": "transparent",\n      "description": "Page background CSS color (e.g. \'white\', \'#f0f0f0\'). Default \'transparent\'.",\n      "type": "string"\n    },\n    "canvas_height": {\n      "default": 600,\n      "description": "Canvas height in pixels.",\n      "type": "integer"\n    },\n    "canvas_width": {\n      "default": 800,\n      "description": "Canvas width in pixels.",\n      "type": "integer"\n    },\n    "choices": {\n      "description": "Allowed keyboard keys. Omit or pass [] for no keys (timeout-only); pass [\'ALL_KEYS\'] or the string \'ALL\' to accept any key. A single-element list is also valid. Normalized at construction time.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "color": {\n      "description": "Broadcast CSS fill color applied to any item that does not already specify \'color\'. Also applied to the fast-path single item when \'shape\' is used. Ignored when \'items\' is a Variable handle.",\n      "type": "string"\n    },\n    "correct_key": {\n      "description": "Expected correct response key (case-insensitive). Copied into trial data; enables \'bean_correct\' boolean in the response data. Omit if correctness scoring is not needed.",\n      "type": "string"\n    },\n    "duration": {\n      "description": "Trial timeout in milliseconds (maps to plugin key trialDuration). Omit for no timeout.",\n      "type": "integer"\n    },\n    "items": {\n      "description": "List of shape dicts to draw. Each dict must have \'shape\' (one of: \'circle\', \'ring\', \'rectangle\', \'triangle\', \'cross\') plus shape-specific size fields (e.g. radius for circle; width+height for rectangle; side for triangle; armLen+armWidth for cross; innerRadius+outerRadius for ring). Optional per-item fields: x, y (position px relative to center), z (draw order), rotation (deg clockwise), alpha (0..1), blend (compositing op string), color (CSS), texture (dict), stroke (CSS color), strokePx (int). If items is a SweetPea/SweetBean Variable, supply its handle string instead.",\n      "items": {\n        "type": "object"\n      },\n      "type": "array"\n    },\n    "response_ends_trial": {\n      "default": true,\n      "description": "If true, the trial ends immediately on the first valid response. Default true.",\n      "type": "boolean"\n    },\n    "shape": {\n      "description": "Fast-path shortcut. If set and \'items\' is empty or omitted, creates a single-item list with this shape. Ignored when \'items\' is provided. One of: \'circle\', \'ring\', \'rectangle\', \'triangle\', \'cross\'.",\n      "type": "string"\n    },\n    "side_effects": {\n      "description": "SweetBean side-effects configuration dict (e.g. timeline variable writes). Omit unless you need side-effect hooks.",\n      "type": "object"\n    },\n    "texture": {\n      "description": "Broadcast texture dict applied to any item that does not already specify \'texture\'. Must have a \'type\' field (\'stripes\' or \'noise\') plus type-specific fields. \'stripes\': bar (int px period), duty (float 0..1), angle (float deg), phase (int px), colors ([str,str]). \'noise\': cell (int px block size), seed (int), colors ([str,str]), mix (float 0..1). Ignored when \'items\' is a Variable handle.",\n      "properties": {\n        "type": {\n          "enum": [\n            "stripes",\n            "noise"\n          ],\n          "type": "string"\n        }\n      },\n      "required": [\n        "type"\n      ],\n      "type": "object"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- Use either `items` (full list of shape dicts) OR `shape` (fast-path single shape), not both. If both are supplied, `items` wins and `shape` is ignored.\n- `color` and `texture` broadcast only to **concrete Python lists**. When `items` is a SweetPea/SweetBean Variable handle string, broadcasting is skipped entirely to avoid incorrect compile-time assumptions — set color/texture inside the Variable\'s dicts instead.\n- `choices` accepts a plain array of strings in the schema, but the runtime also handles the special string values "ALL" / "ALL_KEYS" → normalized to "ALL_KEYS", and null/empty → normalized to []. If passing via the MCP, prefer an explicit list such as ["f", "j"].\n- `duration` maps to the plugin key `trialDuration`, not `duration` — do not confuse with a generic delay.\n- Response data fields written by this stimulus: `bean_key`, `bean_rt`, `bean_onset`, `bean_offset`, `bean_n_items`, and optionally `bean_correct` (only when `correct_key` is set).\n- `canvas_width` / `canvas_height` are the drawing surface, not the page viewport. The page background is controlled separately via `background`.\n- Shape sizes are in pixels; positions (`x`, `y`) are relative to canvas center (0,0), not top-left.'
TOOL_PARAMETERS = { 'properties': { 'allow_mouse': { 'default': False,
                                   'description': 'If true, a mouse click counts as a '
                                                  'valid response. Default false.',
                                   'type': 'boolean'},
                  'background': { 'default': 'transparent',
                                  'description': 'Page background CSS color (e.g. '
                                                 "'white', '#f0f0f0'). Default "
                                                 "'transparent'.",
                                  'type': 'string'},
                  'canvas_height': { 'default': 600,
                                     'description': 'Canvas height in pixels.',
                                     'type': 'integer'},
                  'canvas_width': { 'default': 800,
                                    'description': 'Canvas width in pixels.',
                                    'type': 'integer'},
                  'choices': { 'description': 'Allowed keyboard keys. Omit or pass [] '
                                              'for no keys (timeout-only); pass '
                                              "['ALL_KEYS'] or the string 'ALL' to "
                                              'accept any key. A single-element list '
                                              'is also valid. Normalized at '
                                              'construction time.',
                               'items': {'type': 'string'},
                               'type': 'array'},
                  'color': { 'description': 'Broadcast CSS fill color applied to any '
                                            'item that does not already specify '
                                            "'color'. Also applied to the fast-path "
                                            "single item when 'shape' is used. Ignored "
                                            "when 'items' is a Variable handle.",
                             'type': 'string'},
                  'correct_key': { 'description': 'Expected correct response key '
                                                  '(case-insensitive). Copied into '
                                                  "trial data; enables 'bean_correct' "
                                                  'boolean in the response data. Omit '
                                                  'if correctness scoring is not '
                                                  'needed.',
                                   'type': 'string'},
                  'duration': { 'description': 'Trial timeout in milliseconds (maps to '
                                               'plugin key trialDuration). Omit for no '
                                               'timeout.',
                                'type': 'integer'},
                  'items': { 'description': 'List of shape dicts to draw. Each dict '
                                            "must have 'shape' (one of: 'circle', "
                                            "'ring', 'rectangle', 'triangle', 'cross') "
                                            'plus shape-specific size fields (e.g. '
                                            'radius for circle; width+height for '
                                            'rectangle; side for triangle; '
                                            'armLen+armWidth for cross; '
                                            'innerRadius+outerRadius for ring). '
                                            'Optional per-item fields: x, y (position '
                                            'px relative to center), z (draw order), '
                                            'rotation (deg clockwise), alpha (0..1), '
                                            'blend (compositing op string), color '
                                            '(CSS), texture (dict), stroke (CSS '
                                            'color), strokePx (int). If items is a '
                                            'SweetPea/SweetBean Variable, supply its '
                                            'handle string instead.',
                             'items': {'type': 'object'},
                             'type': 'array'},
                  'response_ends_trial': { 'default': True,
                                           'description': 'If true, the trial ends '
                                                          'immediately on the first '
                                                          'valid response. Default '
                                                          'true.',
                                           'type': 'boolean'},
                  'shape': { 'description': "Fast-path shortcut. If set and 'items' is "
                                            'empty or omitted, creates a single-item '
                                            'list with this shape. Ignored when '
                                            "'items' is provided. One of: 'circle', "
                                            "'ring', 'rectangle', 'triangle', 'cross'.",
                             'type': 'string'},
                  'side_effects': { 'description': 'SweetBean side-effects '
                                                   'configuration dict (e.g. timeline '
                                                   'variable writes). Omit unless you '
                                                   'need side-effect hooks.',
                                    'type': 'object'},
                  'texture': { 'description': 'Broadcast texture dict applied to any '
                                              'item that does not already specify '
                                              "'texture'. Must have a 'type' field "
                                              "('stripes' or 'noise') plus "
                                              "type-specific fields. 'stripes': bar "
                                              '(int px period), duty (float 0..1), '
                                              'angle (float deg), phase (int px), '
                                              "colors ([str,str]). 'noise': cell (int "
                                              'px block size), seed (int), colors '
                                              '([str,str]), mix (float 0..1). Ignored '
                                              "when 'items' is a Variable handle.",
                               'properties': { 'type': { 'enum': ['stripes', 'noise'],
                                                         'type': 'string'}},
                               'required': ['type'],
                               'type': 'object'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- Use either `items` (full list of shape dicts) OR `shape` (fast-path single shape), not both. If both are supplied, `items` wins and `shape` is ignored.\n- `color` and `texture` broadcast only to **concrete Python lists**. When `items` is a SweetPea/SweetBean Variable handle string, broadcasting is skipped entirely to avoid incorrect compile-time assumptions — set color/texture inside the Variable\'s dicts instead.\n- `choices` accepts a plain array of strings in the schema, but the runtime also handles the special string values "ALL" / "ALL_KEYS" → normalized to "ALL_KEYS", and null/empty → normalized to []. If passing via the MCP, prefer an explicit list such as ["f", "j"].\n- `duration` maps to the plugin key `trialDuration`, not `duration` — do not confuse with a generic delay.\n- Response data fields written by this stimulus: `bean_key`, `bean_rt`, `bean_onset`, `bean_offset`, `bean_n_items`, and optionally `bean_correct` (only when `correct_key` is set).\n- `canvas_width` / `canvas_height` are the drawing surface, not the page viewport. The page background is controlled separately via `background`.\n- Shape sizes are in pixels; positions (`x`, `y`) are relative to canvas center (0,0), not top-left.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.Symbol
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
    def create_symbol(args: dict[str, Any] | None = None) -> Any:
        'Call this tool in Step 3 of the pipeline to define a canvas-drawn geometric-shape stimulus for a jsPsych trial.'
        return _impl(args or {})
