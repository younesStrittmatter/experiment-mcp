"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '8287e1cc74575c425f34ab61af0b3308d4df473c8e2fe5cda68c5ef09fa44ac0'
__exp_qualname__ = 'sweetbean.stimulus.Foraging'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_foraging'
TOOL_DESCRIPTION = 'Call this tool in step 3 of the SweetBean pipeline to create a visual foraging stimulus where participants click target items among distractors. Pass either concrete ItemSpec lists or TimelineVariable handle strings (from SweetPea sampling) for `targets` and `distractors`; the result is a Foraging stimulus handle to pass into a SweetBean Block constructor.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "arena_size_vmin": {\n      "default": 92,\n      "description": "Side length of the centered square arena in vmin units.",\n      "type": "number"\n    },\n    "background": {\n      "default": "#000000",\n      "description": "Arena background CSS color. Default is black.",\n      "type": "string"\n    },\n    "color": {\n      "default": "#ffffff",\n      "description": "Default foreground CSS color for text and borders. Default is white.",\n      "type": "string"\n    },\n    "distractors": {\n      "description": "Distractor items: same ItemSpec structure as targets. May be empty list or omitted.",\n      "oneOf": [\n        {\n          "items": {\n            "type": "object"\n          },\n          "type": "array"\n        },\n        {\n          "type": "string"\n        }\n      ]\n    },\n    "duration": {\n      "description": "SweetBean convenience alias for trial_duration (mirrors RSVP convention). Takes precedence over trial_duration if both are supplied.",\n      "type": "integer"\n    },\n    "end_when_found": {\n      "default": true,\n      "description": "Automatically end the trial once all targets are collected.",\n      "type": "boolean"\n    },\n    "grid_cols": {\n      "description": "Number of columns for grid placement. Inferred from total item count if omitted.",\n      "type": "integer"\n    },\n    "grid_rows": {\n      "description": "Number of rows for grid placement. Inferred from total item count if omitted.",\n      "type": "integer"\n    },\n    "min_gap_vmin": {\n      "default": 2.5,\n      "description": "Minimum pairwise spacing between item centers in vmin units.",\n      "type": "number"\n    },\n    "overlay_pool": {\n      "description": "Pool of overlay symbols or colors sampled per item unless the ItemSpec provides an explicit color. Omit to use plugin defaults.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "placement_inset_vmin": {\n      "default": 6,\n      "description": "Inner safety margin from arena edges in vmin units.",\n      "type": "number"\n    },\n    "position_mode": {\n      "default": "random",\n      "description": "Global placement policy for items that do not supply an explicit pos field. \'random\' = non-overlapping random; \'grid\' = structured grid; \'circle\' = ring layout.",\n      "enum": [\n        "random",\n        "grid",\n        "circle"\n      ],\n      "type": "string"\n    },\n    "randomize_positions": {\n      "default": true,\n      "description": "Jitter positions within grid cells or along the ring for grid/circle modes.",\n      "type": "boolean"\n    },\n    "response_ends_trial": {\n      "default": false,\n      "description": "If true, any qualifying response ends the trial even if not all targets are collected.",\n      "type": "boolean"\n    },\n    "ring_radius_vmin": {\n      "default": 30,\n      "description": "Radius in vmin units for circle placement mode.",\n      "type": "number"\n    },\n    "rotation_pool": {\n      "description": "Pool of rotation degrees (integers) sampled per item unless the ItemSpec provides rotationDeg. Omit to use plugin defaults.",\n      "items": {\n        "type": "integer"\n      },\n      "type": "array"\n    },\n    "seed": {\n      "description": "Integer seed for deterministic placement and pool sampling.",\n      "type": "integer"\n    },\n    "show_star_feedback": {\n      "default": false,\n      "description": "Show a brief star animation on successful target clicks.",\n      "type": "boolean"\n    },\n    "side_effects": {\n      "description": "Optional SweetBean SideEffect definitions for updating global state (e.g., cumulative score, trial counter).",\n      "type": "object"\n    },\n    "star_color": {\n      "default": "#f6b500",\n      "description": "CSS color for the star feedback animation.",\n      "type": "string"\n    },\n    "targets": {\n      "description": "Target items: a list of ItemSpec dicts or a handle string for a TimelineVariable. Each ItemSpec must define exactly one of {html, text, shape, src} plus optional styling/placement fields (color, rotationDeg, size, fontSize, id, attrs, pos).",\n      "oneOf": [\n        {\n          "items": {\n            "type": "object"\n          },\n          "type": "array"\n        },\n        {\n          "type": "string"\n        }\n      ]\n    },\n    "token_box_size": {\n      "default": "12vmin",\n      "description": "Default token box size as a CSS value (e.g., \'12vmin\').",\n      "type": "string"\n    },\n    "token_font_size": {\n      "default": "10vmin",\n      "description": "Default font size for text tokens as a CSS value (e.g., \'10vmin\').",\n      "type": "string"\n    },\n    "trial_duration": {\n      "description": "Hard timeout in milliseconds. If null and end_when_found=true, trial ends when all targets are collected.",\n      "type": "integer"\n    },\n    "triggers": {\n      "description": "Event-to-action mapping, e.g. {\\"on_all_targets_collected\\": \\"end_trial\\"}. Defaults (when omitted) to ending the trial when all targets are collected \\u2014 pass {} to disable all triggers.",\n      "type": "object"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- `triggers` silently defaults to `{"on_all_targets_collected": "end_trial"}` when omitted or None — pass an explicit empty dict `{}` to suppress all triggers.\n- `duration` overrides `trial_duration` when both are provided; prefer `duration` for SweetBean pipelines to stay consistent with RSVP.\n- `overlay_pool` and `rotation_pool` are silently dropped if empty or None; the plugin falls back to its own defaults.\n- All spatial parameters (arena_size_vmin, placement_inset_vmin, min_gap_vmin, ring_radius_vmin) are in vmin units, not pixels.\n- Item-level `pos` in an ItemSpec bypasses `position_mode` for that specific item only.\n- Each ItemSpec must define exactly one content field: html, text, shape, or src — mixing multiple content fields in one item is undefined.\n- Language/LLM simulation mode is not supported; this stimulus raises NotImplementedError if used in run_on_language pipelines.\n- window.jsPsychForaging must be available in the browser bundle; ensure the @sweet-jspsych/plugin-foraging script is included when calling to_html.'
TOOL_PARAMETERS = { 'properties': { 'arena_size_vmin': { 'default': 92,
                                       'description': 'Side length of the centered '
                                                      'square arena in vmin units.',
                                       'type': 'number'},
                  'background': { 'default': '#000000',
                                  'description': 'Arena background CSS color. Default '
                                                 'is black.',
                                  'type': 'string'},
                  'color': { 'default': '#ffffff',
                             'description': 'Default foreground CSS color for text and '
                                            'borders. Default is white.',
                             'type': 'string'},
                  'distractors': { 'description': 'Distractor items: same ItemSpec '
                                                  'structure as targets. May be empty '
                                                  'list or omitted.',
                                   'oneOf': [ { 'items': {'type': 'object'},
                                                'type': 'array'},
                                              {'type': 'string'}]},
                  'duration': { 'description': 'SweetBean convenience alias for '
                                               'trial_duration (mirrors RSVP '
                                               'convention). Takes precedence over '
                                               'trial_duration if both are supplied.',
                                'type': 'integer'},
                  'end_when_found': { 'default': True,
                                      'description': 'Automatically end the trial once '
                                                     'all targets are collected.',
                                      'type': 'boolean'},
                  'grid_cols': { 'description': 'Number of columns for grid placement. '
                                                'Inferred from total item count if '
                                                'omitted.',
                                 'type': 'integer'},
                  'grid_rows': { 'description': 'Number of rows for grid placement. '
                                                'Inferred from total item count if '
                                                'omitted.',
                                 'type': 'integer'},
                  'min_gap_vmin': { 'default': 2.5,
                                    'description': 'Minimum pairwise spacing between '
                                                   'item centers in vmin units.',
                                    'type': 'number'},
                  'overlay_pool': { 'description': 'Pool of overlay symbols or colors '
                                                   'sampled per item unless the '
                                                   'ItemSpec provides an explicit '
                                                   'color. Omit to use plugin '
                                                   'defaults.',
                                    'items': {'type': 'string'},
                                    'type': 'array'},
                  'placement_inset_vmin': { 'default': 6,
                                            'description': 'Inner safety margin from '
                                                           'arena edges in vmin units.',
                                            'type': 'number'},
                  'position_mode': { 'default': 'random',
                                     'description': 'Global placement policy for items '
                                                    'that do not supply an explicit '
                                                    "pos field. 'random' = "
                                                    "non-overlapping random; 'grid' = "
                                                    "structured grid; 'circle' = ring "
                                                    'layout.',
                                     'enum': ['random', 'grid', 'circle'],
                                     'type': 'string'},
                  'randomize_positions': { 'default': True,
                                           'description': 'Jitter positions within '
                                                          'grid cells or along the '
                                                          'ring for grid/circle modes.',
                                           'type': 'boolean'},
                  'response_ends_trial': { 'default': False,
                                           'description': 'If true, any qualifying '
                                                          'response ends the trial '
                                                          'even if not all targets are '
                                                          'collected.',
                                           'type': 'boolean'},
                  'ring_radius_vmin': { 'default': 30,
                                        'description': 'Radius in vmin units for '
                                                       'circle placement mode.',
                                        'type': 'number'},
                  'rotation_pool': { 'description': 'Pool of rotation degrees '
                                                    '(integers) sampled per item '
                                                    'unless the ItemSpec provides '
                                                    'rotationDeg. Omit to use plugin '
                                                    'defaults.',
                                     'items': {'type': 'integer'},
                                     'type': 'array'},
                  'seed': { 'description': 'Integer seed for deterministic placement '
                                           'and pool sampling.',
                            'type': 'integer'},
                  'show_star_feedback': { 'default': False,
                                          'description': 'Show a brief star animation '
                                                         'on successful target clicks.',
                                          'type': 'boolean'},
                  'side_effects': { 'description': 'Optional SweetBean SideEffect '
                                                   'definitions for updating global '
                                                   'state (e.g., cumulative score, '
                                                   'trial counter).',
                                    'type': 'object'},
                  'star_color': { 'default': '#f6b500',
                                  'description': 'CSS color for the star feedback '
                                                 'animation.',
                                  'type': 'string'},
                  'targets': { 'description': 'Target items: a list of ItemSpec dicts '
                                              'or a handle string for a '
                                              'TimelineVariable. Each ItemSpec must '
                                              'define exactly one of {html, text, '
                                              'shape, src} plus optional '
                                              'styling/placement fields (color, '
                                              'rotationDeg, size, fontSize, id, attrs, '
                                              'pos).',
                               'oneOf': [ { 'items': {'type': 'object'},
                                            'type': 'array'},
                                          {'type': 'string'}]},
                  'token_box_size': { 'default': '12vmin',
                                      'description': 'Default token box size as a CSS '
                                                     "value (e.g., '12vmin').",
                                      'type': 'string'},
                  'token_font_size': { 'default': '10vmin',
                                       'description': 'Default font size for text '
                                                      'tokens as a CSS value (e.g., '
                                                      "'10vmin').",
                                       'type': 'string'},
                  'trial_duration': { 'description': 'Hard timeout in milliseconds. If '
                                                     'null and end_when_found=true, '
                                                     'trial ends when all targets are '
                                                     'collected.',
                                      'type': 'integer'},
                  'triggers': { 'description': 'Event-to-action mapping, e.g. '
                                               '{"on_all_targets_collected": '
                                               '"end_trial"}. Defaults (when omitted) '
                                               'to ending the trial when all targets '
                                               'are collected — pass {} to disable all '
                                               'triggers.',
                                'type': 'object'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- `triggers` silently defaults to `{"on_all_targets_collected": "end_trial"}` when omitted or None — pass an explicit empty dict `{}` to suppress all triggers.\n- `duration` overrides `trial_duration` when both are provided; prefer `duration` for SweetBean pipelines to stay consistent with RSVP.\n- `overlay_pool` and `rotation_pool` are silently dropped if empty or None; the plugin falls back to its own defaults.\n- All spatial parameters (arena_size_vmin, placement_inset_vmin, min_gap_vmin, ring_radius_vmin) are in vmin units, not pixels.\n- Item-level `pos` in an ItemSpec bypasses `position_mode` for that specific item only.\n- Each ItemSpec must define exactly one content field: html, text, shape, or src — mixing multiple content fields in one item is undefined.\n- Language/LLM simulation mode is not supported; this stimulus raises NotImplementedError if used in run_on_language pipelines.\n- window.jsPsychForaging must be available in the browser bundle; ensure the @sweet-jspsych/plugin-foraging script is included when calling to_html.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.Foraging
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
    def create_foraging(args: dict[str, Any] | None = None) -> Any:
        'Call this tool in step 3 of the SweetBean pipeline to create a visual foraging stimulus where participants click target items among distractors.'
        return _impl(args or {})
