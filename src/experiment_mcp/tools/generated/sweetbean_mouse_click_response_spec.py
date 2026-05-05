"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '9481f57dbd5e9fbf53f41ed42fbd41a4b2a3c0523907d5d10cc5dac7047a7fec'
__exp_qualname__ = 'sweetbean.MouseClickResponseSpec'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_mouse_click_response_spec'
TOOL_DESCRIPTION = 'Call this tool in step 3 of the SweetBean pipeline — after SweetPea has produced a trial sequence and you are wiring stimuli and responses into SweetBean trials — to declare that participants respond by clicking the mouse. Pass the returned spec to a SweetBean stimulus or trial constructor as the response argument. Use it instead of KeyboardPressResponseSpec whenever the experiment requires spatial or point-and-click interaction.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "correct_target_ids": {\n      "default": null,\n      "description": "Subset of target_ids treated as correct for feedback or scoring. Omit (null) when correctness is not evaluated for this response.",\n      "oneOf": [\n        {\n          "items": {\n            "type": "string"\n          },\n          "type": "array"\n        },\n        {\n          "type": "null"\n        }\n      ]\n    },\n    "max_responses": {\n      "default": 1,\n      "description": "How many clicks to capture before the spec considers the response complete. Use null for unlimited (capture all clicks until the trial ends by other means).",\n      "oneOf": [\n        {\n          "minimum": 1,\n          "type": "integer"\n        },\n        {\n          "type": "null"\n        }\n      ]\n    },\n    "record_click_x": {\n      "default": true,\n      "description": "Record the viewport X coordinate of each click in trial data when the runtime supports it.",\n      "type": "boolean"\n    },\n    "record_click_y": {\n      "default": true,\n      "description": "Record the viewport Y coordinate of each click in trial data when the runtime supports it.",\n      "type": "boolean"\n    },\n    "response_ends_trial": {\n      "default": true,\n      "description": "Whether capturing a valid click immediately ends the trial. Set false to keep the trial running after the first response (e.g. multi-click tasks).",\n      "type": "boolean"\n    },\n    "target_ids": {\n      "default": [],\n      "description": "IDs of stimuli that are clickable. When empty, the entire scene is a hit target (full-screen click detection over all rendered layers).",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\nThe `kind` field is always `"mouse_click"` and must not be passed — the template sets it. `record_click_x`, `record_click_y`, and `response_ends_trial` are marked `_PROMPT_SILENT` upstream, meaning they are intentionally hidden from interactive prompts; leave them at defaults unless there is a specific reason to change them. When `target_ids` is empty, every rendered stimulus layer is clickable, so omitting it is appropriate for full-screen click tasks. `correct_target_ids` must be a subset of `target_ids` (or empty) — passing IDs not in `target_ids` will not raise an error at construction time but will silently never score as correct at runtime.'
TOOL_PARAMETERS = { 'properties': { 'correct_target_ids': { 'default': None,
                                          'description': 'Subset of target_ids treated '
                                                         'as correct for feedback or '
                                                         'scoring. Omit (null) when '
                                                         'correctness is not evaluated '
                                                         'for this response.',
                                          'oneOf': [ { 'items': {'type': 'string'},
                                                       'type': 'array'},
                                                     {'type': 'null'}]},
                  'max_responses': { 'default': 1,
                                     'description': 'How many clicks to capture before '
                                                    'the spec considers the response '
                                                    'complete. Use null for unlimited '
                                                    '(capture all clicks until the '
                                                    'trial ends by other means).',
                                     'oneOf': [ {'minimum': 1, 'type': 'integer'},
                                                {'type': 'null'}]},
                  'record_click_x': { 'default': True,
                                      'description': 'Record the viewport X coordinate '
                                                     'of each click in trial data when '
                                                     'the runtime supports it.',
                                      'type': 'boolean'},
                  'record_click_y': { 'default': True,
                                      'description': 'Record the viewport Y coordinate '
                                                     'of each click in trial data when '
                                                     'the runtime supports it.',
                                      'type': 'boolean'},
                  'response_ends_trial': { 'default': True,
                                           'description': 'Whether capturing a valid '
                                                          'click immediately ends the '
                                                          'trial. Set false to keep '
                                                          'the trial running after the '
                                                          'first response (e.g. '
                                                          'multi-click tasks).',
                                           'type': 'boolean'},
                  'target_ids': { 'default': [],
                                  'description': 'IDs of stimuli that are clickable. '
                                                 'When empty, the entire scene is a '
                                                 'hit target (full-screen click '
                                                 'detection over all rendered layers).',
                                  'items': {'type': 'string'},
                                  'type': 'array'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = 'The `kind` field is always `"mouse_click"` and must not be passed — the template sets it. `record_click_x`, `record_click_y`, and `response_ends_trial` are marked `_PROMPT_SILENT` upstream, meaning they are intentionally hidden from interactive prompts; leave them at defaults unless there is a specific reason to change them. When `target_ids` is empty, every rendered stimulus layer is clickable, so omitting it is appropriate for full-screen click tasks. `correct_target_ids` must be a subset of `target_ids` (or empty) — passing IDs not in `target_ids` will not raise an error at construction time but will silently never score as correct at runtime.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.MouseClickResponseSpec
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
    def create_mouse_click_response_spec(args: dict[str, Any] | None = None) -> Any:
        'Call this tool in step 3 of the SweetBean pipeline — after SweetPea has produced a trial sequence and you are wiring stimuli and responses into SweetBean trials — to declare that participants respond by clicking the mouse.'
        return _impl(args or {})
