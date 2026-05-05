"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '6357cdd4076723d99d1293e344d58c267beed11c3a392d67c9d541f8cc64ca9e'
__exp_qualname__ = 'sweetbean.stimulus.Bandit'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_bandit'
TOOL_DESCRIPTION = 'Call this tool when building a multi-armed bandit reinforcement-learning trial in SweetBean — typically step 3 of the pipeline, after SweetPea has generated a trial sequence and you need a clickable stimulus that records which arm was chosen and its payout. Returns a Bandit stimulus handle that can be passed to a SweetBean Trial, wired to SweetPea-sampled factor levels via CodeVariable or FunctionVariable if payouts vary across trials.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "bandits": {\n      "default": [],\n      "description": "Ordered list of bandit arm definitions. Each entry specifies the visual color of the arm and the payout recorded when it is chosen. The grid layout is computed automatically from N.",\n      "items": {\n        "properties": {\n          "color": {\n            "description": "Any valid CSS color value (e.g. \'red\', \'#ff0000\', \'rgb(255,0,0)\') used to outline the bandit square.",\n            "type": "string"\n          },\n          "value": {\n            "description": "Payout or label recorded as `value` in jsPsych data when this bandit is chosen.",\n            "oneOf": [\n              {\n                "type": "number"\n              },\n              {\n                "type": "string"\n              }\n            ]\n          }\n        },\n        "required": [\n          "color",\n          "value"\n        ],\n        "type": "object"\n      },\n      "type": "array"\n    },\n    "duration": {\n      "default": null,\n      "description": "Maximum display time in milliseconds before the trial auto-advances. Pass null (default) to wait indefinitely until the participant clicks a bandit.",\n      "type": [\n        "integer",\n        "null"\n      ]\n    },\n    "side_effects": {\n      "default": null,\n      "description": "Optional side-effect configuration passed to the underlying HtmlChoice. Pass null if no side effects are needed.",\n      "type": [\n        "object",\n        "null"\n      ]\n    },\n    "time_after_response": {\n      "default": 2000,\n      "description": "Extra display time in milliseconds after the participant clicks, used for the slot-machine reveal animation. Defaults to 2000 ms.",\n      "type": "integer"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- `bandits` defaults to an empty list; a Bandit with no arms renders but records nothing useful — always supply at least two entries for a real task.\n- `value` in each bandit dict can be a number (typical payout) or a string label; the type is preserved in jsPsych data as-is.\n- Recorded `choice` / `bean_response` is **0-indexed** even though the LLM headless simulator prompts the model with 1-indexed labels — do not add 1 when reading output data.\n- CSS custom properties `--slotmachine-time` and `--slotmachine-time-after` (each ≈ `time_after_response / 2`) are injected automatically via `on_load`; do not set them manually.\n- Grid layout (rows × cols) is derived automatically from `len(bandits)` — no layout parameter is exposed.\n- To vary payouts trial-by-trial from a SweetPea sequence, wrap the `bandits` list in a SweetBean `FunctionVariable` or `CodeVariable` before passing it here rather than passing a static list.'
TOOL_PARAMETERS = { 'properties': { 'bandits': { 'default': [],
                               'description': 'Ordered list of bandit arm definitions. '
                                              'Each entry specifies the visual color '
                                              'of the arm and the payout recorded when '
                                              'it is chosen. The grid layout is '
                                              'computed automatically from N.',
                               'items': { 'properties': { 'color': { 'description': 'Any '
                                                                                    'valid '
                                                                                    'CSS '
                                                                                    'color '
                                                                                    'value '
                                                                                    '(e.g. '
                                                                                    "'red', "
                                                                                    "'#ff0000', "
                                                                                    "'rgb(255,0,0)') "
                                                                                    'used '
                                                                                    'to '
                                                                                    'outline '
                                                                                    'the '
                                                                                    'bandit '
                                                                                    'square.',
                                                                     'type': 'string'},
                                                          'value': { 'description': 'Payout '
                                                                                    'or '
                                                                                    'label '
                                                                                    'recorded '
                                                                                    'as '
                                                                                    '`value` '
                                                                                    'in '
                                                                                    'jsPsych '
                                                                                    'data '
                                                                                    'when '
                                                                                    'this '
                                                                                    'bandit '
                                                                                    'is '
                                                                                    'chosen.',
                                                                     'oneOf': [ { 'type': 'number'},
                                                                                { 'type': 'string'}]}},
                                          'required': ['color', 'value'],
                                          'type': 'object'},
                               'type': 'array'},
                  'duration': { 'default': None,
                                'description': 'Maximum display time in milliseconds '
                                               'before the trial auto-advances. Pass '
                                               'null (default) to wait indefinitely '
                                               'until the participant clicks a bandit.',
                                'type': ['integer', 'null']},
                  'side_effects': { 'default': None,
                                    'description': 'Optional side-effect configuration '
                                                   'passed to the underlying '
                                                   'HtmlChoice. Pass null if no side '
                                                   'effects are needed.',
                                    'type': ['object', 'null']},
                  'time_after_response': { 'default': 2000,
                                           'description': 'Extra display time in '
                                                          'milliseconds after the '
                                                          'participant clicks, used '
                                                          'for the slot-machine reveal '
                                                          'animation. Defaults to 2000 '
                                                          'ms.',
                                           'type': 'integer'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- `bandits` defaults to an empty list; a Bandit with no arms renders but records nothing useful — always supply at least two entries for a real task.\n- `value` in each bandit dict can be a number (typical payout) or a string label; the type is preserved in jsPsych data as-is.\n- Recorded `choice` / `bean_response` is **0-indexed** even though the LLM headless simulator prompts the model with 1-indexed labels — do not add 1 when reading output data.\n- CSS custom properties `--slotmachine-time` and `--slotmachine-time-after` (each ≈ `time_after_response / 2`) are injected automatically via `on_load`; do not set them manually.\n- Grid layout (rows × cols) is derived automatically from `len(bandits)` — no layout parameter is exposed.\n- To vary payouts trial-by-trial from a SweetPea sequence, wrap the `bandits` list in a SweetBean `FunctionVariable` or `CodeVariable` before passing it here rather than passing a static list.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.Bandit
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
    def create_bandit(args: dict[str, Any] | None = None) -> Any:
        'Call this tool when building a multi-armed bandit reinforcement-learning trial in SweetBean — typically step 3 of the pipeline, after SweetPea has generated a trial sequence and you need a clickable stimulus that records which arm was chosen and its payout.'
        return _impl(args or {})
