"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '3e4a576c35348bb778b30735648d9a57fd33c72b1ab63023713108137ccab5c3'
__exp_qualname__ = 'sweetbean.stimulus.InformedConsent'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_informed_consent'
TOOL_DESCRIPTION = 'Call this tool to insert an informed-consent screen at the start of an experiment — before any SweetPea-sequenced trials run. It produces a SweetBean stimulus that renders pre-built consent HTML and waits for the participant to press SPACE before advancing. The return value is a handle string representing an `InformedConsent` trial that can be placed at the front of a `Block` or `Experiment`.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "choices": {\n      "description": "Keys accepted to advance the trial. Defaults to [\\" \\"] (SPACE). Override only if you need a different confirmation key.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "correct_key": {\n      "description": "Key treated as the \'correct\' response for scoring purposes. Typically left empty for a consent screen.",\n      "type": "string"\n    },\n    "duration": {\n      "description": "Maximum display time in milliseconds before auto-advancing. Omit (null) to wait indefinitely for the SPACE key.",\n      "type": "integer"\n    },\n    "fit_to_viewport": {\n      "default": false,\n      "description": "If true, scales the consent HTML to fit one screen. Defaults to false \\u2014 consent text should scroll at natural font size.",\n      "type": "boolean"\n    },\n    "side_effects": {\n      "additionalProperties": true,\n      "description": "Dict of SweetBean side-effect callbacks (e.g. data-recording hooks) to attach to this trial.",\n      "type": "object"\n    },\n    "stimulus": {\n      "description": "Full HTML string to render as the consent form body. Build this with `from_sections` manually or supply arbitrary HTML. This is the primary required content.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "stimulus"\n  ],\n  "type": "object"\n}\n\nNotes:\nAuto-fit is intentionally off by default (`fit_to_viewport=False`); long consent text will scroll rather than shrink. The footer "Press SPACE to continue" copy is hardcoded in English — there is no `continue_text` parameter. To generate structured HTML from keyed research/consent fields (including the Princeton IRB layout), call `InformedConsent.from_sections(research_config=…, consent_config=…, style="princeton")` outside this tool and pass the resulting `.stimulus` attribute as the `stimulus` argument here. `choices` defaults to `[" "]` if omitted; do not set it to an empty list or the participant will be stuck.'
TOOL_PARAMETERS = { 'properties': { 'choices': { 'description': 'Keys accepted to advance the trial. '
                                              'Defaults to [" "] (SPACE). Override '
                                              'only if you need a different '
                                              'confirmation key.',
                               'items': {'type': 'string'},
                               'type': 'array'},
                  'correct_key': { 'description': "Key treated as the 'correct' "
                                                  'response for scoring purposes. '
                                                  'Typically left empty for a consent '
                                                  'screen.',
                                   'type': 'string'},
                  'duration': { 'description': 'Maximum display time in milliseconds '
                                               'before auto-advancing. Omit (null) to '
                                               'wait indefinitely for the SPACE key.',
                                'type': 'integer'},
                  'fit_to_viewport': { 'default': False,
                                       'description': 'If true, scales the consent '
                                                      'HTML to fit one screen. '
                                                      'Defaults to false — consent '
                                                      'text should scroll at natural '
                                                      'font size.',
                                       'type': 'boolean'},
                  'side_effects': { 'additionalProperties': True,
                                    'description': 'Dict of SweetBean side-effect '
                                                   'callbacks (e.g. data-recording '
                                                   'hooks) to attach to this trial.',
                                    'type': 'object'},
                  'stimulus': { 'description': 'Full HTML string to render as the '
                                               'consent form body. Build this with '
                                               '`from_sections` manually or supply '
                                               'arbitrary HTML. This is the primary '
                                               'required content.',
                                'type': 'string'}},
  'required': ['stimulus'],
  'type': 'object'}
TOOL_NOTES = 'Auto-fit is intentionally off by default (`fit_to_viewport=False`); long consent text will scroll rather than shrink. The footer "Press SPACE to continue" copy is hardcoded in English — there is no `continue_text` parameter. To generate structured HTML from keyed research/consent fields (including the Princeton IRB layout), call `InformedConsent.from_sections(research_config=…, consent_config=…, style="princeton")` outside this tool and pass the resulting `.stimulus` attribute as the `stimulus` argument here. `choices` defaults to `[" "]` if omitted; do not set it to an empty list or the participant will be stuck.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.InformedConsent
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
    def create_informed_consent(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to insert an informed-consent screen at the start of an experiment — before any SweetPea-sequenced trials run.'
        return _impl(args or {})
