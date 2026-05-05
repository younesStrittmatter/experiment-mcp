"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'def2688441e3595b48a6502bcb8beb4441c7ffb1aa9022c10dec718e80b69bf8'
__exp_qualname__ = 'sweetbean.stimulus.Generic'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_generic'
TOOL_DESCRIPTION = 'Call this tool to create a SweetBean stimulus backed by any jsPsych plugin that does not have a dedicated SweetBean wrapper (step 3 of the pipeline, after SweetPea has produced a trial sequence). Pass the jsPsych plugin name as `type` and any plugin-specific kwargs; the result is a stimulus handle you can assemble into a Trial and then a Block. Do NOT use this when the goal is to run the experiment through a language-model simulator — use a typed stimulus (Fixation, Text, etc.) instead.\n\nParameters (JSON Schema):\n{\n  "additionalProperties": {\n    "description": "Any additional jsPsych plugin parameter accepted by the plugin named in `type`. Values may be literals or SweetBean CodeVariable handle strings for trial-by-trial variation driven by a SweetPea sequence."\n  },\n  "properties": {\n    "duration": {\n      "description": "Display duration in milliseconds. Mapped internally to jsPsych\'s `trial_duration` field. Omit to use the plugin\'s default (usually wait for response).",\n      "type": "number"\n    },\n    "side_effects": {\n      "default": [],\n      "description": "Optional list of SweetBean side-effect handle strings (e.g. data-logging actions) to attach to this stimulus. Omit if not needed.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "type": {\n      "description": "jsPsych plugin name (e.g. \'jsPsychHtmlKeyboardResponse\'). Required. The matching <script> plugin tag must be added manually to the generated HTML file \\u2014 the tool does not inject it. See https://www.jspsych.org/v7/plugins/list-of-plugins/ for available plugin names.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "type"\n  ],\n  "type": "object"\n}\n\nNotes:\n- `type` is unconditionally required; the constructor raises ValueError if omitted.\n- This stimulus is explicitly unsupported for language-model execution (`Experiment.run_on_language`). It will likely crash or produce garbage output in that path. Use only for HTML/JS export (`Experiment.to_html`, `Experiment.to_js`).\n- The plugin script is NOT injected automatically into generated HTML. The caller must add the corresponding `<script src="...">` tag, e.g. via `sweetbean_build_html_from_files` or manual post-processing.\n- A one-time `warnings.warn` fires on first instantiation (per process) and again the first time a new plugin `type` value is seen. These are non-fatal and informational; suppress with `warnings.filterwarnings` if needed.\n- `duration` (milliseconds) is a special alias: it is stored under both the generic key and as `trial_duration` in the jsPsych arg dict. Do not pass `trial_duration` directly alongside `duration` — the field will be duplicated.\n- All other kwargs are forwarded verbatim to jsPsych as plugin parameters. Use SweetBean `CodeVariable` handles (strings) as values when a parameter should vary trial-by-trial according to a SweetPea-generated sequence.'
TOOL_PARAMETERS = { 'additionalProperties': { 'description': 'Any additional jsPsych plugin parameter '
                                           'accepted by the plugin named in `type`. '
                                           'Values may be literals or SweetBean '
                                           'CodeVariable handle strings for '
                                           'trial-by-trial variation driven by a '
                                           'SweetPea sequence.'},
  'properties': { 'duration': { 'description': 'Display duration in milliseconds. '
                                               "Mapped internally to jsPsych's "
                                               '`trial_duration` field. Omit to use '
                                               "the plugin's default (usually wait for "
                                               'response).',
                                'type': 'number'},
                  'side_effects': { 'default': [],
                                    'description': 'Optional list of SweetBean '
                                                   'side-effect handle strings (e.g. '
                                                   'data-logging actions) to attach to '
                                                   'this stimulus. Omit if not needed.',
                                    'items': {'type': 'string'},
                                    'type': 'array'},
                  'type': { 'description': 'jsPsych plugin name (e.g. '
                                           "'jsPsychHtmlKeyboardResponse'). Required. "
                                           'The matching <script> plugin tag must be '
                                           'added manually to the generated HTML file '
                                           '— the tool does not inject it. See '
                                           'https://www.jspsych.org/v7/plugins/list-of-plugins/ '
                                           'for available plugin names.',
                            'type': 'string'}},
  'required': ['type'],
  'type': 'object'}
TOOL_NOTES = '- `type` is unconditionally required; the constructor raises ValueError if omitted.\n- This stimulus is explicitly unsupported for language-model execution (`Experiment.run_on_language`). It will likely crash or produce garbage output in that path. Use only for HTML/JS export (`Experiment.to_html`, `Experiment.to_js`).\n- The plugin script is NOT injected automatically into generated HTML. The caller must add the corresponding `<script src="...">` tag, e.g. via `sweetbean_build_html_from_files` or manual post-processing.\n- A one-time `warnings.warn` fires on first instantiation (per process) and again the first time a new plugin `type` value is seen. These are non-fatal and informational; suppress with `warnings.filterwarnings` if needed.\n- `duration` (milliseconds) is a special alias: it is stored under both the generic key and as `trial_duration` in the jsPsych arg dict. Do not pass `trial_duration` directly alongside `duration` — the field will be duplicated.\n- All other kwargs are forwarded verbatim to jsPsych as plugin parameters. Use SweetBean `CodeVariable` handles (strings) as values when a parameter should vary trial-by-trial according to a SweetPea-generated sequence.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.Generic
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
    def create_generic(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to create a SweetBean stimulus backed by any jsPsych plugin that does not have a dedicated SweetBean wrapper (step 3 of the pipeline, after SweetPea has produced a trial sequence).'
        return _impl(args or {})
