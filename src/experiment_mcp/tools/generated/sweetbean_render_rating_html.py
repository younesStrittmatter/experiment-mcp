"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'adfbf523f81a8c1d370943e57130d403c720226e703dec9e94ea4bf893df738a'
__exp_qualname__ = 'sweetbean.stimulus.render_rating_html'
__exp_kind__ = 'function'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'render_rating_html'
TOOL_DESCRIPTION = 'Call this tool when composing a SweetBean HTML stimulus that needs an inline N-point rating bar — e.g., to display a pre-filled confidence indicator alongside a stimulus image, or to render an empty response bar inside a `GenericStimulus`. Returns an HTML string (not a handle) suitable for direct embedding in another stimulus\'s `stimulus` argument or in a larger HTML composition. Fits between SweetPea sequence generation and SweetBean trial/block construction: call it while building stimulus HTML strings before passing them to `Stimulus` or `GenericStimulus`.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "label": {\n      "default": null,\n      "description": "Optional caption rendered above the pip row. Omit or pass null for no label.",\n      "type": [\n        "string",\n        "null"\n      ]\n    },\n    "n_points": {\n      "description": "Total number of pips in the rating bar. Must be between 1 and 10 inclusive.",\n      "maximum": 10,\n      "minimum": 1,\n      "type": "integer"\n    },\n    "value": {\n      "description": "Number of filled pips (0-indexed: first `value` pips filled). Pass null for response-mode appearance (all pips empty, awaiting participant input).",\n      "type": [\n        "integer",\n        "null"\n      ]\n    }\n  },\n  "required": [\n    "value",\n    "n_points"\n  ],\n  "type": "object"\n}\n\nNotes:\nvalue=null renders all pips empty (intended for response mode where the participant has not yet responded); value=0 also renders all pips empty but is semantically "zero filled". n_points outside 1–10 raises a validation error. The returned HTML is a raw string, not a handle — pass it directly as a string argument rather than as a handle reference. Pure-literal implementation means it is safe to call inside a SweetBean FunctionVariable (Transcrypt-compatible), but the output is static HTML — it does not wire up any jsPsych response listeners on its own.'
TOOL_PARAMETERS = { 'properties': { 'label': { 'default': None,
                             'description': 'Optional caption rendered above the pip '
                                            'row. Omit or pass null for no label.',
                             'type': ['string', 'null']},
                  'n_points': { 'description': 'Total number of pips in the rating '
                                               'bar. Must be between 1 and 10 '
                                               'inclusive.',
                                'maximum': 10,
                                'minimum': 1,
                                'type': 'integer'},
                  'value': { 'description': 'Number of filled pips (0-indexed: first '
                                            '`value` pips filled). Pass null for '
                                            'response-mode appearance (all pips empty, '
                                            'awaiting participant input).',
                             'type': ['integer', 'null']}},
  'required': ['value', 'n_points'],
  'type': 'object'}
TOOL_NOTES = 'value=null renders all pips empty (intended for response mode where the participant has not yet responded); value=0 also renders all pips empty but is semantically "zero filled". n_points outside 1–10 raises a validation error. The returned HTML is a raw string, not a handle — pass it directly as a string argument rather than as a handle reference. Pure-literal implementation means it is safe to call inside a SweetBean FunctionVariable (Transcrypt-compatible), but the output is static HTML — it does not wire up any jsPsych response listeners on its own.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.render_rating_html
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
    def render_rating_html(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when composing a SweetBean HTML stimulus that needs an inline N-point rating bar — e.g., to display a pre-filled confidence indicator alongside a stimulus image, or to render an empty response bar inside a `GenericStimulus`.'
        return _impl(args or {})
