"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '09f119a5c09aba2c52f290d453156957a2d60a6f3eafa04f8714ba24beecb7a4'
__exp_qualname__ = 'sweetpea.synthesize_trials'
__exp_kind__ = 'function'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'synthesize_trials'
TOOL_DESCRIPTION = 'Call this tool after constructing a SweetPea Block (via fully_cross_block or multiple_cross_block) to generate one or more concrete trial sequences that satisfy the block\'s crossing and constraints. The result — a list of trial-set dicts, or a participant-keyed dict of trial-set lists when LatinSquare counterbalancing is active — is what you pass to SweetBean stimulus/trial/block constructors to build a runnable jsPsych experiment.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "block": {\n      "description": "Handle string returned by a prior fully_cross_block or multiple_cross_block tool call. The runtime resolves this to a live SweetPea Block before dispatch.",\n      "type": "string"\n    },\n    "participants": {\n      "description": "Optional list of participant IDs for Latin Square counterbalancing. Only needed when the block contains a LatinSquare constraint and you want to solve for a subset of participants. When omitted and a LatinSquare is present, all participants are solved automatically.",\n      "items": {\n        "type": "integer"\n      },\n      "type": "array"\n    },\n    "samples": {\n      "default": 10,\n      "description": "Number of independent trial-set sequences to generate. Each sequence is one full crossing of the design satisfying all constraints. Defaults to 10.",\n      "minimum": 1,\n      "type": "integer"\n    },\n    "sampling_strategy": {\n      "default": "IterateGen",\n      "description": "Name of the sampling algorithm class to use. \'IterateGen\' (default) enumerates solutions deterministically; \'NonUniformGen\' uses Unigen for near-uniform SAT sampling; \'RandomGen\' uses random search; \'SMGen\' uses a SMT solver; \'ILPGen\' uses an ILP solver; \'UniGen\' is the underlying Unigen sampler.",\n      "enum": [\n        "IterateGen",\n        "NonUniformGen",\n        "RandomGen",\n        "SMGen",\n        "ILPGen",\n        "UniGen"\n      ],\n      "type": "string"\n    }\n  },\n  "required": [\n    "block"\n  ],\n  "type": "object"\n}\n\nNotes:\nReturn-type bifurcation: when no LatinSquare constraint is present the tool returns a List[dict] (list of trial-set dicts); when LatinSquare is active (auto-detected or via explicit `participants`) it returns Dict[int, List[dict]] keyed by participant ID. Downstream SweetBean tools expect the flat list form — if you used LatinSquare, index into the returned dict by participant ID before passing to SweetBean. Docstring claims the default sampling strategy is NonUniformGen but the actual source default is IterateGen; IterateGen is the correct default. The `sampling_strategy` parameter is passed as a class name string; the runtime resolves it to the corresponding SweetPea class before dispatch.'
TOOL_PARAMETERS = { 'properties': { 'block': { 'description': 'Handle string returned by a prior '
                                            'fully_cross_block or multiple_cross_block '
                                            'tool call. The runtime resolves this to a '
                                            'live SweetPea Block before dispatch.',
                             'type': 'string'},
                  'participants': { 'description': 'Optional list of participant IDs '
                                                   'for Latin Square counterbalancing. '
                                                   'Only needed when the block '
                                                   'contains a LatinSquare constraint '
                                                   'and you want to solve for a subset '
                                                   'of participants. When omitted and '
                                                   'a LatinSquare is present, all '
                                                   'participants are solved '
                                                   'automatically.',
                                    'items': {'type': 'integer'},
                                    'type': 'array'},
                  'samples': { 'default': 10,
                               'description': 'Number of independent trial-set '
                                              'sequences to generate. Each sequence is '
                                              'one full crossing of the design '
                                              'satisfying all constraints. Defaults to '
                                              '10.',
                               'minimum': 1,
                               'type': 'integer'},
                  'sampling_strategy': { 'default': 'IterateGen',
                                         'description': 'Name of the sampling '
                                                        'algorithm class to use. '
                                                        "'IterateGen' (default) "
                                                        'enumerates solutions '
                                                        'deterministically; '
                                                        "'NonUniformGen' uses Unigen "
                                                        'for near-uniform SAT '
                                                        "sampling; 'RandomGen' uses "
                                                        "random search; 'SMGen' uses a "
                                                        "SMT solver; 'ILPGen' uses an "
                                                        "ILP solver; 'UniGen' is the "
                                                        'underlying Unigen sampler.',
                                         'enum': [ 'IterateGen',
                                                   'NonUniformGen',
                                                   'RandomGen',
                                                   'SMGen',
                                                   'ILPGen',
                                                   'UniGen'],
                                         'type': 'string'}},
  'required': ['block'],
  'type': 'object'}
TOOL_NOTES = 'Return-type bifurcation: when no LatinSquare constraint is present the tool returns a List[dict] (list of trial-set dicts); when LatinSquare is active (auto-detected or via explicit `participants`) it returns Dict[int, List[dict]] keyed by participant ID. Downstream SweetBean tools expect the flat list form — if you used LatinSquare, index into the returned dict by participant ID before passing to SweetBean. Docstring claims the default sampling strategy is NonUniformGen but the actual source default is IterateGen; IterateGen is the correct default. The `sampling_strategy` parameter is passed as a class name string; the runtime resolves it to the corresponding SweetPea class before dispatch.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.synthesize_trials
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
    def synthesize_trials(args: dict[str, Any] | None = None) -> Any:
        "Call this tool after constructing a SweetPea Block (via fully_cross_block or multiple_cross_block) to generate one or more concrete trial sequences that satisfy the block's crossing and constraints."
        return _impl(args or {})
