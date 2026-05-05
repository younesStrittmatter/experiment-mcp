"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetpea as sp

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = 'caccbf57c0d75fc1de0c47e69d68042c16f357c1d540dd93a7dcdc103aace422'
__exp_qualname__ = 'sweetpea.CMSGen'
__exp_kind__ = 'class'
__exp_root__ = 'sweetpea'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_cms_gen'
TOOL_DESCRIPTION = 'Call this tool at step 2 of the SweetPea pipeline — after you have built a crossing with `sweetpea.CrossBlock` (or similar) and need to draw one or more balanced trial sequences from it. CMSGen is an alternative uniform sampler to UniGen; prefer it when UniGen times out or produces biased samples on tightly constrained designs. Returns a SamplingResult handle whose sequences can be passed directly into SweetBean stimulus construction.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "block": {\n      "description": "Handle string for the SweetPea Block (e.g. from sweetpea_cross_block) whose trial sequences you want to sample.",\n      "type": "string"\n    },\n    "min_search": {\n      "default": false,\n      "description": "When true, enables minimum-search mode, which can reduce solve time on large designs at the cost of sampling diversity. Leave false unless the block is very large and sampling is slow.",\n      "type": "boolean"\n    },\n    "sample_count": {\n      "description": "Number of independent trial sequences to generate. Each sequence satisfies the block\'s full crossing.",\n      "minimum": 1,\n      "type": "integer"\n    }\n  },\n  "required": [\n    "block",\n    "sample_count"\n  ],\n  "type": "object"\n}\n\nNotes:\nCMSGen\'s `sample` is a static method that delegates entirely to `UniGen.sample(..., use_cmsgen=True)` — the class itself has no constructor arguments. The host template should call `CMSGen.sample(block, sample_count, min_search)` rather than instantiating the class. Metrics collection is always enabled (there is no option to disable it in the current API, per the TODO in the docstring). Requires the `pycmsgen` C extension, which is compiled on first `uv sync`; if the extension is absent the call will raise `ImportError`.'
TOOL_PARAMETERS = { 'properties': { 'block': { 'description': 'Handle string for the SweetPea Block '
                                            '(e.g. from sweetpea_cross_block) whose '
                                            'trial sequences you want to sample.',
                             'type': 'string'},
                  'min_search': { 'default': False,
                                  'description': 'When true, enables minimum-search '
                                                 'mode, which can reduce solve time on '
                                                 'large designs at the cost of '
                                                 'sampling diversity. Leave false '
                                                 'unless the block is very large and '
                                                 'sampling is slow.',
                                  'type': 'boolean'},
                  'sample_count': { 'description': 'Number of independent trial '
                                                   'sequences to generate. Each '
                                                   "sequence satisfies the block's "
                                                   'full crossing.',
                                    'minimum': 1,
                                    'type': 'integer'}},
  'required': ['block', 'sample_count'],
  'type': 'object'}
TOOL_NOTES = "CMSGen's `sample` is a static method that delegates entirely to `UniGen.sample(..., use_cmsgen=True)` — the class itself has no constructor arguments. The host template should call `CMSGen.sample(block, sample_count, min_search)` rather than instantiating the class. Metrics collection is always enabled (there is no option to disable it in the current API, per the TODO in the docstring). Requires the `pycmsgen` C extension, which is compiled on first `uv sync`; if the extension is absent the call will raise `ImportError`."


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sp.CMSGen
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
    def create_cms_gen(args: dict[str, Any] | None = None) -> Any:
        'Call this tool at step 2 of the SweetPea pipeline — after you have built a crossing with `sweetpea.CrossBlock` (or similar) and need to draw one or more balanced trial sequences from it.'
        return _impl(args or {})
