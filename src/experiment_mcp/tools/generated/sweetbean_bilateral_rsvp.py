"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '9a04bbe883a72d693c0a1284e848186e6b832ab839cff662581988484f0eaff7'
__exp_qualname__ = 'sweetbean.stimulus.BilateralRSVP'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_bilateral_rsvp'
TOOL_DESCRIPTION = 'Call this tool at SweetBean trial-definition time (step 3 of the pipeline) when you need a bilateral RSVP (rapid serial visual presentation) stimulus — two simultaneous left/right item streams with optional target/distractor decoration. The tool returns a handle string for a BilateralRSVP stimulus object that you pass into a SweetBean Trial or Block. Use it for attentional-blink, dual-stream, and divided-attention paradigms where each display position shows an independent token sequence.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "background": {\n      "default": "#000000",\n      "description": "CSS background color for the display. Defaults to \'#000000\'.",\n      "type": "string"\n    },\n    "choices": {\n      "default": "ALL",\n      "description": "Allowed keyboard keys during the RSVP. \'ALL\' allows any key; \'NO_KEYS\' disables responding during the stream (collect response afterward). Can also be a list of key strings or a Variable handle. Defaults to \'ALL\'.",\n      "oneOf": [\n        {\n          "type": "string"\n        },\n        {\n          "items": {\n            "type": "string"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "color": {\n      "default": "#ffffff",\n      "description": "Default CSS glyph/foreground color for all tokens. Defaults to \'#ffffff\'.",\n      "type": "string"\n    },\n    "distractor_color": {\n      "description": "CSS color for distractor decoration. Single CSS string, list, or Variable handle.",\n      "oneOf": [\n        {\n          "type": "string"\n        },\n        {\n          "items": {\n            "type": "string"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "distractor_html": {\n      "description": "Optional HTML template for distractor tokens (same {{content}} templating as targets). Single string, list, or Variable handle.",\n      "oneOf": [\n        {\n          "type": "string"\n        },\n        {\n          "items": {\n            "type": "string"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "distractor_index": {\n      "description": "Zero-based index/indices of distractor token(s). If omitted, defaults to the same value(s) as target_index. Integer, list, or Variable handle.",\n      "oneOf": [\n        {\n          "type": "integer"\n        },\n        {\n          "items": {\n            "type": "integer"\n          },\n          "type": "array"\n        },\n        {\n          "type": "string"\n        }\n      ]\n    },\n    "distractor_shape": {\n      "description": "Decoration shape for distractor(s): \'circle\', \'square\', \'underline\', or \'none\'. Single value, list, or Variable handle.",\n      "oneOf": [\n        {\n          "enum": [\n            "circle",\n            "square",\n            "underline",\n            "none"\n          ],\n          "type": "string"\n        },\n        {\n          "items": {\n            "type": "string"\n          },\n          "type": "array"\n        },\n        {\n          "type": "string"\n        }\n      ]\n    },\n    "distractor_side": {\n      "description": "Stream(s) containing distractor(s). If omitted, the plugin infers the opposite side from target_side for each item. \'left\'|\'right\', list, or Variable handle.",\n      "oneOf": [\n        {\n          "enum": [\n            "left",\n            "right"\n          ],\n          "type": "string"\n        },\n        {\n          "items": {\n            "type": "string"\n          },\n          "type": "array"\n        },\n        {\n          "type": "string"\n        }\n      ]\n    },\n    "duration": {\n      "description": "SweetBean alias for trial_duration (ms). If both are set, duration takes effect. Prefer trial_duration for clarity.",\n      "oneOf": [\n        {\n          "type": "integer"\n        },\n        {\n          "type": "string"\n        }\n      ]\n    },\n    "end_on_response": {\n      "default": false,\n      "description": "If true, the trial ends immediately when the participant presses a key. Maps to the underlying jsPsych plugin\'s response_ends_trial. Boolean or Variable handle. Defaults to false.",\n      "oneOf": [\n        {\n          "type": "boolean"\n        },\n        {\n          "type": "string"\n        }\n      ]\n    },\n    "isi": {\n      "default": 0,\n      "description": "Inter-stimulus interval in milliseconds between successive tokens. Integer or Variable handle. Defaults to 0.",\n      "oneOf": [\n        {\n          "type": "integer"\n        },\n        {\n          "type": "string"\n        }\n      ]\n    },\n    "left": {\n      "description": "Content list for the left stream, e.g. [\'O\',\'Q\',\'X\',...]. May be a handle string for a SweetBean Variable that evaluates to such a list.",\n      "oneOf": [\n        {\n          "items": {\n            "type": "string"\n          },\n          "type": "array"\n        },\n        {\n          "type": "string"\n        }\n      ]\n    },\n    "mask_html": {\n      "description": "HTML string shown during each ISI (e.g. \'\\u2022\' as a visual mask). Omit to leave the ISI blank.",\n      "type": "string"\n    },\n    "right": {\n      "description": "Content list for the right stream. Same format as `left`.",\n      "oneOf": [\n        {\n          "items": {\n            "type": "string"\n          },\n          "type": "array"\n        },\n        {\n          "type": "string"\n        }\n      ]\n    },\n    "side_effects": {\n      "description": "Optional list of SweetBean SideEffect definitions for updating global state (e.g. score counter) at trial end. Each element is a SideEffect config object.",\n      "items": {\n        "type": "object"\n      },\n      "type": "array"\n    },\n    "stimulus_duration": {\n      "default": 100,\n      "description": "Milliseconds each token is displayed on screen. Integer or Variable handle. Defaults to 100.",\n      "oneOf": [\n        {\n          "type": "integer"\n        },\n        {\n          "type": "string"\n        }\n      ]\n    },\n    "target_color": {\n      "description": "CSS color for target decoration (border/underline color when shape != \'none\'; glyph color when shape == \'none\'). Single CSS string, list, or Variable handle.",\n      "oneOf": [\n        {\n          "type": "string"\n        },\n        {\n          "items": {\n            "type": "string"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "target_html": {\n      "description": "Optional HTML template for target tokens. If it contains {{content}} or {CONTENT}, it wraps the stream glyph; otherwise it fully overrides the token display. Single string, list, or Variable handle.",\n      "oneOf": [\n        {\n          "type": "string"\n        },\n        {\n          "items": {\n            "type": "string"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "target_index": {\n      "default": 0,\n      "description": "Zero-based index of the target token within its stream. Can be an integer, a list of integers (multiple targets), or a Variable handle. Defaults to 0.",\n      "oneOf": [\n        {\n          "type": "integer"\n        },\n        {\n          "items": {\n            "type": "integer"\n          },\n          "type": "array"\n        },\n        {\n          "type": "string"\n        }\n      ]\n    },\n    "target_shape": {\n      "default": "circle",\n      "description": "Visual decoration around the target: \'circle\', \'square\', \'underline\', or \'none\' (color-only). Can be a single value, list, or Variable handle. Defaults to \'circle\'.",\n      "oneOf": [\n        {\n          "enum": [\n            "circle",\n            "square",\n            "underline",\n            "none"\n          ],\n          "type": "string"\n        },\n        {\n          "items": {\n            "type": "string"\n          },\n          "type": "array"\n        },\n        {\n          "type": "string"\n        }\n      ]\n    },\n    "target_side": {\n      "default": "left",\n      "description": "Which stream contains the target: \'left\', \'right\', a list of those strings (one per target), or a Variable handle. Defaults to \'left\'.",\n      "oneOf": [\n        {\n          "enum": [\n            "left",\n            "right"\n          ],\n          "type": "string"\n        },\n        {\n          "items": {\n            "type": "string"\n          },\n          "type": "array"\n        },\n        {\n          "type": "string"\n        }\n      ]\n    },\n    "token_box_size": {\n      "default": "18vmin",\n      "description": "CSS size of each token bounding box (width and height). Defaults to \'18vmin\'.",\n      "type": "string"\n    },\n    "token_font_size": {\n      "default": "10vmin",\n      "description": "CSS font size for token glyphs. Defaults to \'10vmin\'.",\n      "type": "string"\n    },\n    "token_padding": {\n      "default": "0.25em 0.45em",\n      "description": "CSS padding inside each token box. Defaults to \'0.25em 0.45em\'.",\n      "type": "string"\n    },\n    "trial_duration": {\n      "description": "Hard cutoff for the entire RSVP trial in milliseconds. The trial ends at this time even if the stream has not finished. Integer or Variable handle. Omit for no hard cutoff.",\n      "oneOf": [\n        {\n          "type": "integer"\n        },\n        {\n          "type": "string"\n        }\n      ]\n    }\n  },\n  "required": [\n    "left",\n    "right"\n  ],\n  "type": "object"\n}\n\nNotes:\n- `distractor_index` silently defaults to the same value(s) as `target_index` when omitted — this mirrors the upstream default in the constructor, not a jsPsych default.\n- `distractor_side` defaults to the **opposite** of `target_side` (inferred by the plugin) when omitted; only supply it to override that inference.\n- `end_on_response` is a SweetBean convenience alias; it is converted to `response_ends_trial` in the jsPsych payload — do not pass both.\n- `duration` and `trial_duration` are aliases for the same jsPsych parameter; if you set `duration`, it overwrites `trial_duration`. Avoid setting both.\n- All timing values (`stimulus_duration`, `isi`, `trial_duration`, `duration`) are in **milliseconds**.\n- Target/distractor `*_shape`, `*_color`, `*_html`, `*_index`, and `*_side` params accept scalars **or** lists; when lists, they broadcast element-wise across multiple target/distractor items. Lengths must be consistent.\n- `choices="NO_KEYS"` is useful when you want to collect a response in a separate subsequent trial rather than during the RSVP stream itself.\n- The response data written to jsPsych includes `bean_key`, `bean_rt`, and `bean_any_hit` (true if any target was hit).'
TOOL_PARAMETERS = { 'properties': { 'background': { 'default': '#000000',
                                  'description': 'CSS background color for the '
                                                 "display. Defaults to '#000000'.",
                                  'type': 'string'},
                  'choices': { 'default': 'ALL',
                               'description': 'Allowed keyboard keys during the RSVP. '
                                              "'ALL' allows any key; 'NO_KEYS' "
                                              'disables responding during the stream '
                                              '(collect response afterward). Can also '
                                              'be a list of key strings or a Variable '
                                              "handle. Defaults to 'ALL'.",
                               'oneOf': [ {'type': 'string'},
                                          { 'items': {'type': 'string'},
                                            'type': 'array'}]},
                  'color': { 'default': '#ffffff',
                             'description': 'Default CSS glyph/foreground color for '
                                            "all tokens. Defaults to '#ffffff'.",
                             'type': 'string'},
                  'distractor_color': { 'description': 'CSS color for distractor '
                                                       'decoration. Single CSS string, '
                                                       'list, or Variable handle.',
                                        'oneOf': [ {'type': 'string'},
                                                   { 'items': {'type': 'string'},
                                                     'type': 'array'}]},
                  'distractor_html': { 'description': 'Optional HTML template for '
                                                      'distractor tokens (same '
                                                      '{{content}} templating as '
                                                      'targets). Single string, list, '
                                                      'or Variable handle.',
                                       'oneOf': [ {'type': 'string'},
                                                  { 'items': {'type': 'string'},
                                                    'type': 'array'}]},
                  'distractor_index': { 'description': 'Zero-based index/indices of '
                                                       'distractor token(s). If '
                                                       'omitted, defaults to the same '
                                                       'value(s) as target_index. '
                                                       'Integer, list, or Variable '
                                                       'handle.',
                                        'oneOf': [ {'type': 'integer'},
                                                   { 'items': {'type': 'integer'},
                                                     'type': 'array'},
                                                   {'type': 'string'}]},
                  'distractor_shape': { 'description': 'Decoration shape for '
                                                       "distractor(s): 'circle', "
                                                       "'square', 'underline', or "
                                                       "'none'. Single value, list, or "
                                                       'Variable handle.',
                                        'oneOf': [ { 'enum': [ 'circle',
                                                               'square',
                                                               'underline',
                                                               'none'],
                                                     'type': 'string'},
                                                   { 'items': {'type': 'string'},
                                                     'type': 'array'},
                                                   {'type': 'string'}]},
                  'distractor_side': { 'description': 'Stream(s) containing '
                                                      'distractor(s). If omitted, the '
                                                      'plugin infers the opposite side '
                                                      'from target_side for each item. '
                                                      "'left'|'right', list, or "
                                                      'Variable handle.',
                                       'oneOf': [ { 'enum': ['left', 'right'],
                                                    'type': 'string'},
                                                  { 'items': {'type': 'string'},
                                                    'type': 'array'},
                                                  {'type': 'string'}]},
                  'duration': { 'description': 'SweetBean alias for trial_duration '
                                               '(ms). If both are set, duration takes '
                                               'effect. Prefer trial_duration for '
                                               'clarity.',
                                'oneOf': [{'type': 'integer'}, {'type': 'string'}]},
                  'end_on_response': { 'default': False,
                                       'description': 'If true, the trial ends '
                                                      'immediately when the '
                                                      'participant presses a key. Maps '
                                                      'to the underlying jsPsych '
                                                      "plugin's response_ends_trial. "
                                                      'Boolean or Variable handle. '
                                                      'Defaults to false.',
                                       'oneOf': [ {'type': 'boolean'},
                                                  {'type': 'string'}]},
                  'isi': { 'default': 0,
                           'description': 'Inter-stimulus interval in milliseconds '
                                          'between successive tokens. Integer or '
                                          'Variable handle. Defaults to 0.',
                           'oneOf': [{'type': 'integer'}, {'type': 'string'}]},
                  'left': { 'description': 'Content list for the left stream, e.g. '
                                           "['O','Q','X',...]. May be a handle string "
                                           'for a SweetBean Variable that evaluates to '
                                           'such a list.',
                            'oneOf': [ {'items': {'type': 'string'}, 'type': 'array'},
                                       {'type': 'string'}]},
                  'mask_html': { 'description': 'HTML string shown during each ISI '
                                                "(e.g. '•' as a visual mask). Omit to "
                                                'leave the ISI blank.',
                                 'type': 'string'},
                  'right': { 'description': 'Content list for the right stream. Same '
                                            'format as `left`.',
                             'oneOf': [ {'items': {'type': 'string'}, 'type': 'array'},
                                        {'type': 'string'}]},
                  'side_effects': { 'description': 'Optional list of SweetBean '
                                                   'SideEffect definitions for '
                                                   'updating global state (e.g. score '
                                                   'counter) at trial end. Each '
                                                   'element is a SideEffect config '
                                                   'object.',
                                    'items': {'type': 'object'},
                                    'type': 'array'},
                  'stimulus_duration': { 'default': 100,
                                         'description': 'Milliseconds each token is '
                                                        'displayed on screen. Integer '
                                                        'or Variable handle. Defaults '
                                                        'to 100.',
                                         'oneOf': [ {'type': 'integer'},
                                                    {'type': 'string'}]},
                  'target_color': { 'description': 'CSS color for target decoration '
                                                   '(border/underline color when shape '
                                                   "!= 'none'; glyph color when shape "
                                                   "== 'none'). Single CSS string, "
                                                   'list, or Variable handle.',
                                    'oneOf': [ {'type': 'string'},
                                               { 'items': {'type': 'string'},
                                                 'type': 'array'}]},
                  'target_html': { 'description': 'Optional HTML template for target '
                                                  'tokens. If it contains {{content}} '
                                                  'or {CONTENT}, it wraps the stream '
                                                  'glyph; otherwise it fully overrides '
                                                  'the token display. Single string, '
                                                  'list, or Variable handle.',
                                   'oneOf': [ {'type': 'string'},
                                              { 'items': {'type': 'string'},
                                                'type': 'array'}]},
                  'target_index': { 'default': 0,
                                    'description': 'Zero-based index of the target '
                                                   'token within its stream. Can be an '
                                                   'integer, a list of integers '
                                                   '(multiple targets), or a Variable '
                                                   'handle. Defaults to 0.',
                                    'oneOf': [ {'type': 'integer'},
                                               { 'items': {'type': 'integer'},
                                                 'type': 'array'},
                                               {'type': 'string'}]},
                  'target_shape': { 'default': 'circle',
                                    'description': 'Visual decoration around the '
                                                   "target: 'circle', 'square', "
                                                   "'underline', or 'none' "
                                                   '(color-only). Can be a single '
                                                   'value, list, or Variable handle. '
                                                   "Defaults to 'circle'.",
                                    'oneOf': [ { 'enum': [ 'circle',
                                                           'square',
                                                           'underline',
                                                           'none'],
                                                 'type': 'string'},
                                               { 'items': {'type': 'string'},
                                                 'type': 'array'},
                                               {'type': 'string'}]},
                  'target_side': { 'default': 'left',
                                   'description': 'Which stream contains the target: '
                                                  "'left', 'right', a list of those "
                                                  'strings (one per target), or a '
                                                  'Variable handle. Defaults to '
                                                  "'left'.",
                                   'oneOf': [ { 'enum': ['left', 'right'],
                                                'type': 'string'},
                                              { 'items': {'type': 'string'},
                                                'type': 'array'},
                                              {'type': 'string'}]},
                  'token_box_size': { 'default': '18vmin',
                                      'description': 'CSS size of each token bounding '
                                                     'box (width and height). Defaults '
                                                     "to '18vmin'.",
                                      'type': 'string'},
                  'token_font_size': { 'default': '10vmin',
                                       'description': 'CSS font size for token glyphs. '
                                                      "Defaults to '10vmin'.",
                                       'type': 'string'},
                  'token_padding': { 'default': '0.25em 0.45em',
                                     'description': 'CSS padding inside each token '
                                                    "box. Defaults to '0.25em 0.45em'.",
                                     'type': 'string'},
                  'trial_duration': { 'description': 'Hard cutoff for the entire RSVP '
                                                     'trial in milliseconds. The trial '
                                                     'ends at this time even if the '
                                                     'stream has not finished. Integer '
                                                     'or Variable handle. Omit for no '
                                                     'hard cutoff.',
                                      'oneOf': [ {'type': 'integer'},
                                                 {'type': 'string'}]}},
  'required': ['left', 'right'],
  'type': 'object'}
TOOL_NOTES = '- `distractor_index` silently defaults to the same value(s) as `target_index` when omitted — this mirrors the upstream default in the constructor, not a jsPsych default.\n- `distractor_side` defaults to the **opposite** of `target_side` (inferred by the plugin) when omitted; only supply it to override that inference.\n- `end_on_response` is a SweetBean convenience alias; it is converted to `response_ends_trial` in the jsPsych payload — do not pass both.\n- `duration` and `trial_duration` are aliases for the same jsPsych parameter; if you set `duration`, it overwrites `trial_duration`. Avoid setting both.\n- All timing values (`stimulus_duration`, `isi`, `trial_duration`, `duration`) are in **milliseconds**.\n- Target/distractor `*_shape`, `*_color`, `*_html`, `*_index`, and `*_side` params accept scalars **or** lists; when lists, they broadcast element-wise across multiple target/distractor items. Lengths must be consistent.\n- `choices="NO_KEYS"` is useful when you want to collect a response in a separate subsequent trial rather than during the RSVP stream itself.\n- The response data written to jsPsych includes `bean_key`, `bean_rt`, and `bean_any_hit` (true if any target was hit).'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.BilateralRSVP
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
    def create_bilateral_rsvp(args: dict[str, Any] | None = None) -> Any:
        'Call this tool at SweetBean trial-definition time (step 3 of the pipeline) when you need a bilateral RSVP (rapid serial visual presentation) stimulus — two simultaneous left/right item streams with optional target/distractor decoration.'
        return _impl(args or {})
