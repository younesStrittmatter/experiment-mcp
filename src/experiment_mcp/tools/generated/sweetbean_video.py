"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '036c5cb5416df6575073b11d6cab3feb4c9ed3059442d42e85d743b2471f922d'
__exp_qualname__ = 'sweetbean.stimulus.Video'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_video'
TOOL_DESCRIPTION = 'Call this tool in step 3 of the pipeline — after SweetPea has sampled a trial sequence and you need a video stimulus that collects a keyboard response. Use it when a trial requires playing a video clip (e.g., a visual prime, a video vignette, or a motion stimulus) before capturing a keypress. Returns a SweetBean Video stimulus object handle that can be passed to a Trial or Block constructor.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "autoplay": {\n      "default": true,\n      "description": "Start playback automatically when the trial begins. Browser autoplay policies often require muted=true.",\n      "type": "boolean"\n    },\n    "choices": {\n      "description": "Accepted keypress(es), e.g. [\\"f\\",\\"j\\"]. Pass \\"ALL\\" to accept any key, \\"NO_KEYS\\" to disable keyboard response entirely.",\n      "oneOf": [\n        {\n          "items": {\n            "type": "string"\n          },\n          "type": "array"\n        },\n        {\n          "enum": [\n            "ALL",\n            "NO_KEYS"\n          ],\n          "type": "string"\n        }\n      ]\n    },\n    "controls": {\n      "default": false,\n      "description": "Show native browser video controls (play/pause, scrub bar). Disable for stimulus presentation to prevent participant interaction.",\n      "type": "boolean"\n    },\n    "correct_key": {\n      "default": "",\n      "description": "The correct response key for accuracy scoring. Optional; leave empty if no correct answer applies.",\n      "type": "string"\n    },\n    "duration": {\n      "description": "Maximum time in milliseconds the trial runs. Alias for trial_duration. If omitted and trial_ends_after_video is true, the trial ends when the video finishes.",\n      "type": "integer"\n    },\n    "height": {\n      "description": "Display height of the video in pixels. Omit to use the video\'s native height.",\n      "type": "integer"\n    },\n    "muted": {\n      "default": true,\n      "description": "Mute audio. Must be true in most browsers for autoplay to work. Set to false only when audio is required and autoplay restrictions are handled externally.",\n      "type": "boolean"\n    },\n    "side_effects": {\n      "description": "Handle strings for SweetBean SideEffect objects produced by prior tool calls. Used to update global state (e.g., running score, trial counter) on each trial response.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "stimulus": {\n      "description": "Video source URL(s) or path(s). Provide multiple formats of the same video (e.g., .mp4, .ogg, .webm) as a list to maximize cross-browser compatibility. A bare string is automatically wrapped in a list.",\n      "oneOf": [\n        {\n          "type": "string"\n        },\n        {\n          "items": {\n            "type": "string"\n          },\n          "type": "array"\n        }\n      ]\n    },\n    "trial_ends_after_video": {\n      "default": true,\n      "description": "If true, the trial ends automatically when the video finishes playing, regardless of duration.",\n      "type": "boolean"\n    },\n    "width": {\n      "description": "Display width of the video in pixels. Omit to use the video\'s native width.",\n      "type": "integer"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- `stimulus` is practically required — jsPsych will throw a runtime error if it is missing, but the tool accepts None to support declarative/template-driven flows where the value is wired in later via a SweetPea data variable.\n- `muted` defaults to `true` because most browsers block autoplay with audio. If your experiment needs audio, set `muted=false` AND ensure the browser autoplay policy is satisfied (e.g., preceded by a user-interaction trial).\n- `duration` and `trial_ends_after_video` interact: if both are set, whichever fires first ends the trial.\n- Internally `duration` is remapped to `trial_duration` in the jsPsych payload; do not pass `trial_duration` directly.\n- `choices` accepts the strings `"ALL"` or `"NO_KEYS"` as special sentinels, not just arrays — pass them as bare strings, not single-element arrays.\n- When passing SweetPea-sampled level values as `stimulus`, wrap them in a SweetBean `DataVariable` handle so the runtime resolves them per-trial rather than as a constant.'
TOOL_PARAMETERS = { 'properties': { 'autoplay': { 'default': True,
                                'description': 'Start playback automatically when the '
                                               'trial begins. Browser autoplay '
                                               'policies often require muted=true.',
                                'type': 'boolean'},
                  'choices': { 'description': 'Accepted keypress(es), e.g. ["f","j"]. '
                                              'Pass "ALL" to accept any key, "NO_KEYS" '
                                              'to disable keyboard response entirely.',
                               'oneOf': [ { 'items': {'type': 'string'},
                                            'type': 'array'},
                                          { 'enum': ['ALL', 'NO_KEYS'],
                                            'type': 'string'}]},
                  'controls': { 'default': False,
                                'description': 'Show native browser video controls '
                                               '(play/pause, scrub bar). Disable for '
                                               'stimulus presentation to prevent '
                                               'participant interaction.',
                                'type': 'boolean'},
                  'correct_key': { 'default': '',
                                   'description': 'The correct response key for '
                                                  'accuracy scoring. Optional; leave '
                                                  'empty if no correct answer applies.',
                                   'type': 'string'},
                  'duration': { 'description': 'Maximum time in milliseconds the trial '
                                               'runs. Alias for trial_duration. If '
                                               'omitted and trial_ends_after_video is '
                                               'true, the trial ends when the video '
                                               'finishes.',
                                'type': 'integer'},
                  'height': { 'description': 'Display height of the video in pixels. '
                                             "Omit to use the video's native height.",
                              'type': 'integer'},
                  'muted': { 'default': True,
                             'description': 'Mute audio. Must be true in most browsers '
                                            'for autoplay to work. Set to false only '
                                            'when audio is required and autoplay '
                                            'restrictions are handled externally.',
                             'type': 'boolean'},
                  'side_effects': { 'description': 'Handle strings for SweetBean '
                                                   'SideEffect objects produced by '
                                                   'prior tool calls. Used to update '
                                                   'global state (e.g., running score, '
                                                   'trial counter) on each trial '
                                                   'response.',
                                    'items': {'type': 'string'},
                                    'type': 'array'},
                  'stimulus': { 'description': 'Video source URL(s) or path(s). '
                                               'Provide multiple formats of the same '
                                               'video (e.g., .mp4, .ogg, .webm) as a '
                                               'list to maximize cross-browser '
                                               'compatibility. A bare string is '
                                               'automatically wrapped in a list.',
                                'oneOf': [ {'type': 'string'},
                                           { 'items': {'type': 'string'},
                                             'type': 'array'}]},
                  'trial_ends_after_video': { 'default': True,
                                              'description': 'If true, the trial ends '
                                                             'automatically when the '
                                                             'video finishes playing, '
                                                             'regardless of duration.',
                                              'type': 'boolean'},
                  'width': { 'description': 'Display width of the video in pixels. '
                                            "Omit to use the video's native width.",
                             'type': 'integer'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- `stimulus` is practically required — jsPsych will throw a runtime error if it is missing, but the tool accepts None to support declarative/template-driven flows where the value is wired in later via a SweetPea data variable.\n- `muted` defaults to `true` because most browsers block autoplay with audio. If your experiment needs audio, set `muted=false` AND ensure the browser autoplay policy is satisfied (e.g., preceded by a user-interaction trial).\n- `duration` and `trial_ends_after_video` interact: if both are set, whichever fires first ends the trial.\n- Internally `duration` is remapped to `trial_duration` in the jsPsych payload; do not pass `trial_duration` directly.\n- `choices` accepts the strings `"ALL"` or `"NO_KEYS"` as special sentinels, not just arrays — pass them as bare strings, not single-element arrays.\n- When passing SweetPea-sampled level values as `stimulus`, wrap them in a SweetBean `DataVariable` handle so the runtime resolves them per-trial rather than as a constant.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.Video
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
    def create_video(args: dict[str, Any] | None = None) -> Any:
        'Call this tool in step 3 of the pipeline — after SweetPea has sampled a trial sequence and you need a video stimulus that collects a keyboard response.'
        return _impl(args or {})
