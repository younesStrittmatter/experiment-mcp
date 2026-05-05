"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '9d27f1cef85efaf4f1e5028a94eccf64f952b84817305b4e1a239ed5620a6121'
__exp_qualname__ = 'sweetpea.Block'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_block'
TOOL_DESCRIPTION = 'Call this tool to construct the base SweetPea Block configuration object — the core data structure that holds a factorial design, its crossing scheme, and constraints before trial sequences are sampled. This sits at step 1 of the SweetPea pipeline: after declaring Factors (via sweetpea_factor tools), pass them here to build the Block handle that downstream tools (e.g. sweetpea_synthesize_trials, sweetpea_experiment_run) consume. NOTE: Block is abstract; prefer sweetpea_fully_cross_block or sweetpea_multiple_cross_block for direct use — call this only when you have a concrete subclass need or when instructed by a higher-level tool.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "constraints": {\n      "default": [],\n      "description": "List of Constraint handle strings (e.g. from sweetpea_exclude, sweetpea_at_least_k_in_a_row, sweetpea_minimum_trials) that restrict valid trial sequences. Pass an empty array if no constraints are needed.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "crossings": {\n      "description": "List of crossings, where each crossing is a list of Factor handle strings whose level combinations should be fully crossed. Each factor handle must also appear in \'design\'. Continuous factors are not allowed in any crossing.",\n      "items": {\n        "items": {\n          "type": "string"\n        },\n        "type": "array"\n      },\n      "type": "array"\n    },\n    "design": {\n      "description": "Ordered list of Factor handle strings (as returned by sweetpea_factor tools) that define all independent variables in the experiment, including both basic and derived factors.",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "require_complete_crossing": {\n      "description": "When true, every combination of levels in the crossing must appear at least once per sample. Set false to allow partial crossings (e.g. when some combinations are excluded).",\n      "type": "boolean"\n    },\n    "who": {\n      "description": "A short label identifying the caller or block name, used only in error/validation messages (e.g. \'CrossBlock\', \'my_experiment\'). Does not affect sampling behavior.",\n      "type": "string"\n    }\n  },\n  "required": [\n    "design",\n    "crossings",\n    "constraints",\n    "require_complete_crossing",\n    "who"\n  ],\n  "type": "object"\n}\n\nNotes:\nBlock is an abstract class — it cannot be instantiated directly and will raise TypeError at runtime. Concrete subclasses (CrossBlock, MultipleCrossBlock, etc.) call super().__init__() with these same arguments; those are the tools agents should reach for. Continuous factors (ContinuousFactor) are silently separated from the discrete design list and stored separately; they cannot appear in any crossing. The \'who\' string appears only in validation error messages and has no effect on the produced Block or trial samples. Validation runs eagerly in __init__: factor/crossing consistency, derived-level dependencies, and constraint compatibility are all checked before the Block handle is returned — expect RuntimeError if the design is inconsistent.'
TOOL_PARAMETERS = { 'properties': { 'constraints': { 'default': [],
                                   'description': 'List of Constraint handle strings '
                                                  '(e.g. from sweetpea_exclude, '
                                                  'sweetpea_at_least_k_in_a_row, '
                                                  'sweetpea_minimum_trials) that '
                                                  'restrict valid trial sequences. '
                                                  'Pass an empty array if no '
                                                  'constraints are needed.',
                                   'items': {'type': 'string'},
                                   'type': 'array'},
                  'crossings': { 'description': 'List of crossings, where each '
                                                'crossing is a list of Factor handle '
                                                'strings whose level combinations '
                                                'should be fully crossed. Each factor '
                                                "handle must also appear in 'design'. "
                                                'Continuous factors are not allowed in '
                                                'any crossing.',
                                 'items': { 'items': {'type': 'string'},
                                            'type': 'array'},
                                 'type': 'array'},
                  'design': { 'description': 'Ordered list of Factor handle strings '
                                             '(as returned by sweetpea_factor tools) '
                                             'that define all independent variables in '
                                             'the experiment, including both basic and '
                                             'derived factors.',
                              'items': {'type': 'string'},
                              'type': 'array'},
                  'require_complete_crossing': { 'description': 'When true, every '
                                                                'combination of levels '
                                                                'in the crossing must '
                                                                'appear at least once '
                                                                'per sample. Set false '
                                                                'to allow partial '
                                                                'crossings (e.g. when '
                                                                'some combinations are '
                                                                'excluded).',
                                                 'type': 'boolean'},
                  'who': { 'description': 'A short label identifying the caller or '
                                          'block name, used only in error/validation '
                                          "messages (e.g. 'CrossBlock', "
                                          "'my_experiment'). Does not affect sampling "
                                          'behavior.',
                           'type': 'string'}},
  'required': [ 'design',
                'crossings',
                'constraints',
                'require_complete_crossing',
                'who'],
  'type': 'object'}
TOOL_NOTES = "Block is an abstract class — it cannot be instantiated directly and will raise TypeError at runtime. Concrete subclasses (CrossBlock, MultipleCrossBlock, etc.) call super().__init__() with these same arguments; those are the tools agents should reach for. Continuous factors (ContinuousFactor) are silently separated from the discrete design list and stored separately; they cannot appear in any crossing. The 'who' string appears only in validation error messages and has no effect on the produced Block or trial samples. Validation runs eagerly in __init__: factor/crossing consistency, derived-level dependencies, and constraint compatibility are all checked before the Block handle is returned — expect RuntimeError if the design is inconsistent."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.Block
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
    def create_block(args: dict[str, Any] | None = None) -> Any:
        'Call this tool to construct the base SweetPea Block configuration object — the core data structure that holds a factorial design, its crossing scheme, and constraints before trial sequences are sampled.'
        return _impl(args or {})
