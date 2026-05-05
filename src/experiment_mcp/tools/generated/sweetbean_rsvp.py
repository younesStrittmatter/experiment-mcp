"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '2ceb22a874d112e1a0df190ffd3d9fad4506da11f9f103001ebf17b80953e9e9'
__exp_qualname__ = 'sweetbean.stimulus.RSVP'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_rsvp'
TOOL_DESCRIPTION = 'Call this tool at step 3 of the pipeline — after SweetPea has sampled a trial sequence and you have stream content arrays — to create a multi-stream Rapid Serial Visual Presentation (RSVP) stimulus that wraps the `jsPsychRsvp` plugin. Pass the result (along with other stimuli) to `sweetbean_block` to build a trial block, then compile to HTML. The tool returns a SweetBean RSVP stimulus object (handle string) ready for use in a Block.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "background": {\n      "default": "#000000",\n      "description": "CSS background color for the RSVP screen. Default \\"#000000\\".",\n      "type": "string"\n    },\n    "choices": {\n      "default": "ALL",\n      "description": "Allowed keys during RSVP. \\"ALL\\" permits any key; \\"NO_KEYS\\" disables responses during stream; or pass an array of key strings such as [\\"f\\",\\"j\\"]. Default \\"ALL\\".",\n      "oneOf": [\n        {\n          "type": "string"\n        },\n        {\n          "items": {\n            "type": "string"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "color": {\n      "default": "#ffffff",\n      "description": "Default text/border color when no per-item color is supplied. Default \\"#ffffff\\".",\n      "type": "string"\n    },\n    "correct_keys": {\n      "description": "Comma-separated keys used for per-target hit scoring, e.g. \\"f,j\\". Optional.",\n      "type": "string"\n    },\n    "decorate_distractors": {\n      "default": false,\n      "description": "Whether to render distractor decorations. Default false.",\n      "type": "boolean"\n    },\n    "decorate_targets": {\n      "default": true,\n      "description": "Whether to render target decorations (ignored when target_shape is \\"none\\"). Default true.",\n      "type": "boolean"\n    },\n    "direction": {\n      "default": "row",\n      "description": "Stream layout direction: \\"row\\" = side-by-side, \\"column\\" = stacked. Default \\"row\\".",\n      "enum": [\n        "row",\n        "column"\n      ],\n      "type": "string"\n    },\n    "distractor_color": {\n      "default": "#888888",\n      "description": "Default distractor border/underline color (or glyph color if shape is \\"none\\"). Default \\"#888888\\".",\n      "type": "string"\n    },\n    "distractor_color2": {\n      "description": "Per-item distractor color override; falls back to distractor_color when not set. CSS string or array / Variable handle strings.",\n      "oneOf": [\n        {\n          "type": "string"\n        },\n        {\n          "items": {\n            "type": "string"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "distractor_html": {\n      "description": "Per-item HTML for distractors. Same {{content}} templating as target_html. String or array / Variable handle strings.",\n      "oneOf": [\n        {\n          "type": "string"\n        },\n        {\n          "items": {\n            "type": "string"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "distractor_index": {\n      "description": "Convenience: position(s) of distractors. Integer or array of integers / Variable handle strings. Auto-copies from target_index if both distractors and distractor_index are omitted.",\n      "oneOf": [\n        {\n          "type": "integer"\n        },\n        {\n          "items": {\n            "oneOf": [\n              {\n                "type": "integer"\n              },\n              {\n                "type": "string"\n              }\n            ]\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "distractor_shape": {\n      "default": "none",\n      "description": "Default decoration shape for distractors. Default \\"none\\".",\n      "enum": [\n        "circle",\n        "square",\n        "underline",\n        "none"\n      ],\n      "type": "string"\n    },\n    "distractor_side": {\n      "description": "Convenience: stream id(s) for distractors. String or array / Variable handle strings.",\n      "oneOf": [\n        {\n          "type": "string"\n        },\n        {\n          "items": {\n            "type": "string"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "distractor_stroke": {\n      "default": "2px",\n      "description": "CSS outline/underline thickness for distractors. Default \\"2px\\".",\n      "type": "string"\n    },\n    "distractors": {\n      "description": "Explicit distractor list. Each item may include: stream_id, index, label, shape, color, stroke, padding, html, style, className.",\n      "items": {\n        "type": "object"\n      },\n      "type": "array"\n    },\n    "duration": {\n      "description": "SweetBean alias for trial_duration. If both are set, trial_duration wins.",\n      "type": "integer"\n    },\n    "end_on_response": {\n      "default": false,\n      "description": "If true, RSVP ends immediately on the first valid keypress (mapped to plugin\'s response_ends_trial). Default false.",\n      "type": "boolean"\n    },\n    "gap": {\n      "default": "6rem",\n      "description": "CSS gap between streams. Default \\"6rem\\".",\n      "type": "string"\n    },\n    "isi": {\n      "default": 0,\n      "description": "Inter-stimulus interval in ms between tokens (SOA = stimulus_duration + isi). Default 0.",\n      "type": "integer"\n    },\n    "mask_html": {\n      "description": "Optional HTML shown during the ISI (e.g., \\"\\u2022\\"). Default null.",\n      "type": "string"\n    },\n    "record_timestamps": {\n      "default": true,\n      "description": "If true, per-token onset/offset times are recorded in data[\\"schedule\\"]. Default true.",\n      "type": "boolean"\n    },\n    "response_window": {\n      "description": "Time window in ms for scoring target hits. Null = unlimited. Default null.",\n      "type": "integer"\n    },\n    "side_effects": {\n      "description": "Optional side-effect dict passed through at runtime.",\n      "type": "object"\n    },\n    "stimulus_duration": {\n      "default": 100,\n      "description": "Milliseconds each token is shown. Default 100.",\n      "type": "integer"\n    },\n    "stream_order": {\n      "description": "Comma-separated DOM order of stream IDs, e.g. \\"left,right\\". Auto-filled when there are exactly two streams in row layout.",\n      "type": "string"\n    },\n    "streams": {\n      "description": "Per-trial stream specs. Preferred form: [{\\"id\\": \\"left\\", \\"items\\": [\\"O\\", \\"Q\\", ...]}, {\\"id\\": \\"right\\", \\"items\\": [\\"1\\", \\"2\\", ...]}]. Items must be pure content (letters/digits) \\u2014 do NOT embed shape names or colors here. SweetPea Variable handle strings may appear as individual items.",\n      "items": {\n        "type": "object"\n      },\n      "type": "array"\n    },\n    "target_color": {\n      "description": "Per-item target color (CSS string or array). When target_shape is \\"none\\" this colors the glyph text itself rather than a border. Variable handle strings accepted.",\n      "oneOf": [\n        {\n          "type": "string"\n        },\n        {\n          "items": {\n            "type": "string"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "target_html": {\n      "description": "Per-item HTML for targets. If it contains {{content}} or {CONTENT} the stream item text is injected; otherwise used as a full override. String or array / Variable handle strings.",\n      "oneOf": [\n        {\n          "type": "string"\n        },\n        {\n          "items": {\n            "type": "string"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "target_index": {\n      "description": "Convenience: position(s) of targets in their streams. Integer or array of integers / Variable handle strings. Broadcast by the plugin.",\n      "oneOf": [\n        {\n          "type": "integer"\n        },\n        {\n          "items": {\n            "oneOf": [\n              {\n                "type": "integer"\n              },\n              {\n                "type": "string"\n              }\n            ]\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "target_shape": {\n      "default": "none",\n      "description": "Default decoration shape for targets. Default \\"none\\".",\n      "enum": [\n        "circle",\n        "square",\n        "underline",\n        "none"\n      ],\n      "type": "string"\n    },\n    "target_side": {\n      "description": "Convenience: stream id(s) for target(s), e.g. \\"left\\"/\\"right\\"/custom. String or array of strings / Variable handle strings.",\n      "oneOf": [\n        {\n          "type": "string"\n        },\n        {\n          "items": {\n            "type": "string"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "target_stroke": {\n      "default": "3px",\n      "description": "CSS outline/underline thickness for targets. Default \\"3px\\".",\n      "type": "string"\n    },\n    "targets": {\n      "description": "Explicit target list. Each item may include: stream_id, index, label, response_window, correct_keys, shape, color, stroke, padding, html, style, className.",\n      "items": {\n        "type": "object"\n      },\n      "type": "array"\n    },\n    "token_box_size": {\n      "default": "18vmin",\n      "description": "CSS size of the fixed square token box (prevents layout wobble when borders appear). Default \\"18vmin\\".",\n      "type": "string"\n    },\n    "token_font_size": {\n      "default": "10vmin",\n      "description": "CSS font size for the glyph inside each token box. Default \\"10vmin\\".",\n      "type": "string"\n    },\n    "token_padding": {\n      "default": "0.25em 0.45em",\n      "description": "CSS inner padding used by outlined/underlined shapes. Default \\"0.25em 0.45em\\".",\n      "type": "string"\n    },\n    "trial_duration": {\n      "description": "Hard stop in ms; if omitted the trial ends after the last token + ISI. Use `duration` as an alias.",\n      "type": "integer"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n• `streams` should contain **pure content** (letters, digits); never embed shape names, colors, or HTML inside stream items — those belong in target/distractor parameters.\n• `end_on_response` (bool) is silently remapped to the plugin\'s `response_ends_trial`; do not pass `response_ends_trial` directly.\n• `duration` is a SweetBean alias for `trial_duration`; if you set both, `trial_duration` takes effect.\n• `stream_order` is auto-filled when there are exactly two streams in `direction="row"` — only specify it explicitly when you need a non-default order or have more than two streams.\n• When `distractor_index` **and** `distractors` are both omitted, `distractor_index` is automatically set to `target_index` — useful for same-position distractor/target designs but may be surprising if you want no-distractor trials.\n• `target_color` with `target_shape="none"` colors the **glyph text** itself, not a border or outline.\n• No normalization is applied to SweetPea Variable handle strings — they pass through to the plugin untouched, so you can wire SweetPea factor levels directly into any parameter that accepts a Variable.\n• Recorded response data includes `bean_key`, `bean_rt`, and `bean_any_hit` (true if any target was hit) in addition to the standard jsPsych fields.\n• All timing values (`stimulus_duration`, `isi`, `trial_duration`, `response_window`) are in **milliseconds**.'
TOOL_PARAMETERS = { 'properties': { 'background': { 'default': '#000000',
                                  'description': 'CSS background color for the RSVP '
                                                 'screen. Default "#000000".',
                                  'type': 'string'},
                  'choices': { 'default': 'ALL',
                               'description': 'Allowed keys during RSVP. "ALL" permits '
                                              'any key; "NO_KEYS" disables responses '
                                              'during stream; or pass an array of key '
                                              'strings such as ["f","j"]. Default '
                                              '"ALL".',
                               'oneOf': [ {'type': 'string'},
                                          { 'items': {'type': 'string'},
                                            'type': 'array'}]},
                  'color': { 'default': '#ffffff',
                             'description': 'Default text/border color when no '
                                            'per-item color is supplied. Default '
                                            '"#ffffff".',
                             'type': 'string'},
                  'correct_keys': { 'description': 'Comma-separated keys used for '
                                                   'per-target hit scoring, e.g. '
                                                   '"f,j". Optional.',
                                    'type': 'string'},
                  'decorate_distractors': { 'default': False,
                                            'description': 'Whether to render '
                                                           'distractor decorations. '
                                                           'Default false.',
                                            'type': 'boolean'},
                  'decorate_targets': { 'default': True,
                                        'description': 'Whether to render target '
                                                       'decorations (ignored when '
                                                       'target_shape is "none"). '
                                                       'Default true.',
                                        'type': 'boolean'},
                  'direction': { 'default': 'row',
                                 'description': 'Stream layout direction: "row" = '
                                                'side-by-side, "column" = stacked. '
                                                'Default "row".',
                                 'enum': ['row', 'column'],
                                 'type': 'string'},
                  'distractor_color': { 'default': '#888888',
                                        'description': 'Default distractor '
                                                       'border/underline color (or '
                                                       'glyph color if shape is '
                                                       '"none"). Default "#888888".',
                                        'type': 'string'},
                  'distractor_color2': { 'description': 'Per-item distractor color '
                                                        'override; falls back to '
                                                        'distractor_color when not '
                                                        'set. CSS string or array / '
                                                        'Variable handle strings.',
                                         'oneOf': [ {'type': 'string'},
                                                    { 'items': {'type': 'string'},
                                                      'type': 'array'}]},
                  'distractor_html': { 'description': 'Per-item HTML for distractors. '
                                                      'Same {{content}} templating as '
                                                      'target_html. String or array / '
                                                      'Variable handle strings.',
                                       'oneOf': [ {'type': 'string'},
                                                  { 'items': {'type': 'string'},
                                                    'type': 'array'}]},
                  'distractor_index': { 'description': 'Convenience: position(s) of '
                                                       'distractors. Integer or array '
                                                       'of integers / Variable handle '
                                                       'strings. Auto-copies from '
                                                       'target_index if both '
                                                       'distractors and '
                                                       'distractor_index are omitted.',
                                        'oneOf': [ {'type': 'integer'},
                                                   { 'items': { 'oneOf': [ { 'type': 'integer'},
                                                                           { 'type': 'string'}]},
                                                     'type': 'array'}]},
                  'distractor_shape': { 'default': 'none',
                                        'description': 'Default decoration shape for '
                                                       'distractors. Default "none".',
                                        'enum': [ 'circle',
                                                  'square',
                                                  'underline',
                                                  'none'],
                                        'type': 'string'},
                  'distractor_side': { 'description': 'Convenience: stream id(s) for '
                                                      'distractors. String or array / '
                                                      'Variable handle strings.',
                                       'oneOf': [ {'type': 'string'},
                                                  { 'items': {'type': 'string'},
                                                    'type': 'array'}]},
                  'distractor_stroke': { 'default': '2px',
                                         'description': 'CSS outline/underline '
                                                        'thickness for distractors. '
                                                        'Default "2px".',
                                         'type': 'string'},
                  'distractors': { 'description': 'Explicit distractor list. Each item '
                                                  'may include: stream_id, index, '
                                                  'label, shape, color, stroke, '
                                                  'padding, html, style, className.',
                                   'items': {'type': 'object'},
                                   'type': 'array'},
                  'duration': { 'description': 'SweetBean alias for trial_duration. If '
                                               'both are set, trial_duration wins.',
                                'type': 'integer'},
                  'end_on_response': { 'default': False,
                                       'description': 'If true, RSVP ends immediately '
                                                      'on the first valid keypress '
                                                      "(mapped to plugin's "
                                                      'response_ends_trial). Default '
                                                      'false.',
                                       'type': 'boolean'},
                  'gap': { 'default': '6rem',
                           'description': 'CSS gap between streams. Default "6rem".',
                           'type': 'string'},
                  'isi': { 'default': 0,
                           'description': 'Inter-stimulus interval in ms between '
                                          'tokens (SOA = stimulus_duration + isi). '
                                          'Default 0.',
                           'type': 'integer'},
                  'mask_html': { 'description': 'Optional HTML shown during the ISI '
                                                '(e.g., "•"). Default null.',
                                 'type': 'string'},
                  'record_timestamps': { 'default': True,
                                         'description': 'If true, per-token '
                                                        'onset/offset times are '
                                                        'recorded in data["schedule"]. '
                                                        'Default true.',
                                         'type': 'boolean'},
                  'response_window': { 'description': 'Time window in ms for scoring '
                                                      'target hits. Null = unlimited. '
                                                      'Default null.',
                                       'type': 'integer'},
                  'side_effects': { 'description': 'Optional side-effect dict passed '
                                                   'through at runtime.',
                                    'type': 'object'},
                  'stimulus_duration': { 'default': 100,
                                         'description': 'Milliseconds each token is '
                                                        'shown. Default 100.',
                                         'type': 'integer'},
                  'stream_order': { 'description': 'Comma-separated DOM order of '
                                                   'stream IDs, e.g. "left,right". '
                                                   'Auto-filled when there are exactly '
                                                   'two streams in row layout.',
                                    'type': 'string'},
                  'streams': { 'description': 'Per-trial stream specs. Preferred form: '
                                              '[{"id": "left", "items": ["O", "Q", '
                                              '...]}, {"id": "right", "items": ["1", '
                                              '"2", ...]}]. Items must be pure content '
                                              '(letters/digits) — do NOT embed shape '
                                              'names or colors here. SweetPea Variable '
                                              'handle strings may appear as individual '
                                              'items.',
                               'items': {'type': 'object'},
                               'type': 'array'},
                  'target_color': { 'description': 'Per-item target color (CSS string '
                                                   'or array). When target_shape is '
                                                   '"none" this colors the glyph text '
                                                   'itself rather than a border. '
                                                   'Variable handle strings accepted.',
                                    'oneOf': [ {'type': 'string'},
                                               { 'items': {'type': 'string'},
                                                 'type': 'array'}]},
                  'target_html': { 'description': 'Per-item HTML for targets. If it '
                                                  'contains {{content}} or {CONTENT} '
                                                  'the stream item text is injected; '
                                                  'otherwise used as a full override. '
                                                  'String or array / Variable handle '
                                                  'strings.',
                                   'oneOf': [ {'type': 'string'},
                                              { 'items': {'type': 'string'},
                                                'type': 'array'}]},
                  'target_index': { 'description': 'Convenience: position(s) of '
                                                   'targets in their streams. Integer '
                                                   'or array of integers / Variable '
                                                   'handle strings. Broadcast by the '
                                                   'plugin.',
                                    'oneOf': [ {'type': 'integer'},
                                               { 'items': { 'oneOf': [ { 'type': 'integer'},
                                                                       { 'type': 'string'}]},
                                                 'type': 'array'}]},
                  'target_shape': { 'default': 'none',
                                    'description': 'Default decoration shape for '
                                                   'targets. Default "none".',
                                    'enum': ['circle', 'square', 'underline', 'none'],
                                    'type': 'string'},
                  'target_side': { 'description': 'Convenience: stream id(s) for '
                                                  'target(s), e.g. '
                                                  '"left"/"right"/custom. String or '
                                                  'array of strings / Variable handle '
                                                  'strings.',
                                   'oneOf': [ {'type': 'string'},
                                              { 'items': {'type': 'string'},
                                                'type': 'array'}]},
                  'target_stroke': { 'default': '3px',
                                     'description': 'CSS outline/underline thickness '
                                                    'for targets. Default "3px".',
                                     'type': 'string'},
                  'targets': { 'description': 'Explicit target list. Each item may '
                                              'include: stream_id, index, label, '
                                              'response_window, correct_keys, shape, '
                                              'color, stroke, padding, html, style, '
                                              'className.',
                               'items': {'type': 'object'},
                               'type': 'array'},
                  'token_box_size': { 'default': '18vmin',
                                      'description': 'CSS size of the fixed square '
                                                     'token box (prevents layout '
                                                     'wobble when borders appear). '
                                                     'Default "18vmin".',
                                      'type': 'string'},
                  'token_font_size': { 'default': '10vmin',
                                       'description': 'CSS font size for the glyph '
                                                      'inside each token box. Default '
                                                      '"10vmin".',
                                       'type': 'string'},
                  'token_padding': { 'default': '0.25em 0.45em',
                                     'description': 'CSS inner padding used by '
                                                    'outlined/underlined shapes. '
                                                    'Default "0.25em 0.45em".',
                                     'type': 'string'},
                  'trial_duration': { 'description': 'Hard stop in ms; if omitted the '
                                                     'trial ends after the last token '
                                                     '+ ISI. Use `duration` as an '
                                                     'alias.',
                                      'type': 'integer'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '• `streams` should contain **pure content** (letters, digits); never embed shape names, colors, or HTML inside stream items — those belong in target/distractor parameters.\n• `end_on_response` (bool) is silently remapped to the plugin\'s `response_ends_trial`; do not pass `response_ends_trial` directly.\n• `duration` is a SweetBean alias for `trial_duration`; if you set both, `trial_duration` takes effect.\n• `stream_order` is auto-filled when there are exactly two streams in `direction="row"` — only specify it explicitly when you need a non-default order or have more than two streams.\n• When `distractor_index` **and** `distractors` are both omitted, `distractor_index` is automatically set to `target_index` — useful for same-position distractor/target designs but may be surprising if you want no-distractor trials.\n• `target_color` with `target_shape="none"` colors the **glyph text** itself, not a border or outline.\n• No normalization is applied to SweetPea Variable handle strings — they pass through to the plugin untouched, so you can wire SweetPea factor levels directly into any parameter that accepts a Variable.\n• Recorded response data includes `bean_key`, `bean_rt`, and `bean_any_hit` (true if any target was hit) in addition to the standard jsPsych fields.\n• All timing values (`stimulus_duration`, `isi`, `trial_duration`, `response_window`) are in **milliseconds**.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.RSVP
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
    def create_rsvp(args: dict[str, Any] | None = None) -> Any:
        'Call this tool at step 3 of the pipeline — after SweetPea has sampled a trial sequence and you have stream content arrays — to create a multi-stream Rapid Serial Visual Presentation (RSVP) stimulus that wraps the `jsPsychRsvp` plugin.'
        return _impl(args or {})
