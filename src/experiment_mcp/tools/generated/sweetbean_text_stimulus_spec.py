"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '906a61f8aea43408228cf8816fad8d045c3b0c29256590a6dcee015961ac0c87'
__exp_qualname__ = 'sweetbean.TextStimulusSpec'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_text_stimulus_spec'
TOOL_DESCRIPTION = 'Call this tool in SweetBean experiment construction (step 3 of the pipeline) to define a text stimulus — a word, label, or sentence rendered on-screen during a trial. Pass the resulting handle to a Trial or Block constructor alongside response specs. Use it whenever a trial condition requires displaying text rather than an image or symbol.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "align": {\n      "description": "Text alignment inside the placement rectangle. Omit to use SweetBean\'s default of \'center\'.",\n      "enum": [\n        "left",\n        "center",\n        "right"\n      ],\n      "type": "string"\n    },\n    "color": {\n      "description": "CSS text color (e.g. \'white\', \'#ff0000\'). Defaults to \'white\' \\u2014 set explicitly if your background is also white.",\n      "type": "string"\n    },\n    "font_family": {\n      "description": "CSS font-family string (e.g. \'Arial, sans-serif\'). Omit to use SweetBean\'s default sans-serif.",\n      "type": "string"\n    },\n    "font_size_px": {\n      "description": "Font size in pixels. Omit to use SweetBean\'s default of 32px.",\n      "minimum": 1,\n      "type": "integer"\n    },\n    "text": {\n      "description": "Text content to render on screen.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "text"\n  ],\n  "type": "object"\n}\n\nNotes:\nThe `kind` field is always "text" and is not a settable parameter. `color` defaults to "white", not black — if your canvas background is also white the text will be invisible; set `color` explicitly in that case. `font_size_px`, `font_family`, and `align` are silently defaulted by SweetBean (32, sans-serif, center) only when omitted; passing `null` is not the same as omitting and may behave differently depending on SweetBean version.'
TOOL_PARAMETERS = { 'properties': { 'align': { 'description': 'Text alignment inside the placement '
                                            "rectangle. Omit to use SweetBean's "
                                            "default of 'center'.",
                             'enum': ['left', 'center', 'right'],
                             'type': 'string'},
                  'color': { 'description': "CSS text color (e.g. 'white', '#ff0000'). "
                                            "Defaults to 'white' — set explicitly if "
                                            'your background is also white.',
                             'type': 'string'},
                  'font_family': { 'description': 'CSS font-family string (e.g. '
                                                  "'Arial, sans-serif'). Omit to use "
                                                  "SweetBean's default sans-serif.",
                                   'type': 'string'},
                  'font_size_px': { 'description': 'Font size in pixels. Omit to use '
                                                   "SweetBean's default of 32px.",
                                    'minimum': 1,
                                    'type': 'integer'},
                  'text': { 'description': 'Text content to render on screen.',
                            'type': 'string'}},
  'required': ['text'],
  'type': 'object'}
TOOL_NOTES = 'The `kind` field is always "text" and is not a settable parameter. `color` defaults to "white", not black — if your canvas background is also white the text will be invisible; set `color` explicitly in that case. `font_size_px`, `font_family`, and `align` are silently defaulted by SweetBean (32, sans-serif, center) only when omitted; passing `null` is not the same as omitting and may behave differently depending on SweetBean version.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.TextStimulusSpec
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
    def create_text_stimulus_spec(args: dict[str, Any] | None = None) -> Any:
        'Call this tool in SweetBean experiment construction (step 3 of the pipeline) to define a text stimulus — a word, label, or sentence rendered on-screen during a trial.'
        return _impl(args or {})
