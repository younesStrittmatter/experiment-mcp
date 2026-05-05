"""Auto-generated. Do not edit by hand. Regen via scripts/generate_tools.py."""

from __future__ import annotations

import json
from typing import Any

import sweetbean as sb

from experiment_mcp import handles
from experiment_mcp.feedback import captured_tool

__source_sha256__ = '37c8e013661b2daa9ff710c382e8c7461ab4a8b04cfbfc81f133898c844d0110'
__exp_qualname__ = 'sweetbean.stimulus.Gabor'
__exp_kind__ = 'class'
__exp_root__ = 'sweetbean'
__generated_by__ = 'claude_cli@sonnet'

TOOL_NAME = 'create_gabor'
TOOL_DESCRIPTION = 'Call this tool in step 3 of the pipeline — after SweetPea has generated a trial sequence — to create a Gabor patch stimulus for psychophysics experiments. It instantiates a `sweetbean.stimulus.Gabor` object that renders one or more Gabor patches on a jsPsych canvas and collects keyboard or mouse responses; pass the returned handle to `sweetbean_block` to assemble a block. Use `TimelineVariable` handles for `patches` when patch geometry varies per SweetPea-sampled trial.\n\nParameters (JSON Schema):\n{\n  "properties": {\n    "allow_mouse": {\n      "default": true,\n      "description": "If true, a mouse click selects the nearest patch center.",\n      "type": "boolean"\n    },\n    "bg_gray": {\n      "default": 0.5,\n      "description": "Background mean luminance in [0..1]. 0.5 is mid-gray.",\n      "type": "number"\n    },\n    "canvas_height": {\n      "default": 600,\n      "description": "Canvas height in pixels.",\n      "type": "integer"\n    },\n    "canvas_width": {\n      "default": 800,\n      "description": "Canvas width in pixels.",\n      "type": "integer"\n    },\n    "duration": {\n      "description": "SweetBean convenience alias for trial_duration; copied into trial_duration during build. Use one or the other, not both.",\n      "type": "integer"\n    },\n    "end_on_response": {\n      "default": true,\n      "description": "If true, the trial ends immediately after a valid response.",\n      "type": "boolean"\n    },\n    "gamma": {\n      "default": 1,\n      "description": "Gamma correction exponent applied to luminance. 1.0 means no correction.",\n      "type": "number"\n    },\n    "keymap_to_patch_index": {\n      "additionalProperties": {\n        "type": "integer"\n      },\n      "description": "Explicit key-to-patch-index map, e.g. {\\"f\\": 0, \\"j\\": 1}. If omitted, the plugin infers a side-based mapping for arrow keys.",\n      "type": "object"\n    },\n    "patches": {\n      "description": "Patch list for this trial. Either a concrete array of patch descriptor dicts (see notes for fields) or a handle string for a TimelineVariable that evaluates per trial. Omit or pass [] for an empty canvas.",\n      "oneOf": [\n        {\n          "items": {\n            "properties": {\n              "contrast": {\n                "description": "Michelson contrast in [0..1].",\n                "type": "number"\n              },\n              "label": {\n                "description": "Arbitrary tag copied into trial data.",\n                "type": "string"\n              },\n              "orientation_deg": {\n                "description": "Orientation in degrees [0..180).",\n                "type": "number"\n              },\n              "phase_deg": {\n                "description": "Phase in degrees [0..360).",\n                "type": "number"\n              },\n              "sf_cpd": {\n                "description": "Spatial frequency in cycles per degree. Requires px_per_deg on the stimulus.",\n                "type": "number"\n              },\n              "sf_cpp": {\n                "description": "Spatial frequency in cycles per pixel. Mutually exclusive with sf_cpd.",\n                "type": "number"\n              },\n              "sigma_deg": {\n                "description": "Gaussian sigma in degrees. Requires px_per_deg on the stimulus.",\n                "type": "number"\n              },\n              "sigma_px": {\n                "description": "Gaussian sigma in pixels. Mutually exclusive with sigma_deg.",\n                "type": "number"\n              },\n              "size_px": {\n                "description": "Square draw size in pixels. Defaults to ~6*sigma_px if omitted.",\n                "type": "integer"\n              },\n              "x_px": {\n                "description": "X center in pixels, relative to canvas center.",\n                "type": "number"\n              },\n              "y_px": {\n                "description": "Y center in pixels, relative to canvas center.",\n                "type": "number"\n              }\n            },\n            "type": "object"\n          },\n          "type": "array"\n        },\n        {\n          "description": "Handle string for a TimelineVariable whose value is a patch list.",\n          "type": "string"\n        }\n      ]\n    },\n    "px_per_deg": {\n      "description": "Pixels per visual degree. Required to use sigma_deg or sf_cpd in any patch. Omit if all patches use pixel-based fields only.",\n      "type": "number"\n    },\n    "response_keys": {\n      "description": "Allowed keyboard keys. Defaults to [\\"ArrowLeft\\", \\"ArrowRight\\"] if omitted. Override to use custom keys like [\\"f\\", \\"j\\"].",\n      "items": {\n        "type": "string"\n      },\n      "type": "array"\n    },\n    "side_effects": {\n      "description": "Optional list of SweetBean SideEffect definitions for updating global state (e.g., score counter) after this trial.",\n      "items": {\n        "type": "object"\n      },\n      "type": "array"\n    },\n    "timeout_ms": {\n      "description": "Alias for trial_duration; takes precedence over trial_duration if both are provided.",\n      "type": "integer"\n    },\n    "trial_duration": {\n      "description": "Hard trial timeout in milliseconds. Omit for no forced timeout. Overridden by timeout_ms if both are set.",\n      "type": "integer"\n    }\n  },\n  "required": [],\n  "type": "object"\n}\n\nNotes:\n- Each patch must specify exactly one of sf_cpp or sf_cpd, and exactly one of sigma_px or sigma_deg; degree-based fields (sf_cpd, sigma_deg) silently produce incorrect output if px_per_deg is not set on the stimulus.\n- timeout_ms wins over trial_duration when both are provided; duration is a third alias that is copied into trial_duration — avoid providing more than one of the three.\n- Null/None optional fields are stripped before the plugin sees them, so the plugin\'s own defaults take effect; this means omitting a field and explicitly passing null are equivalent.\n- The type field is set internally to "jsPsychGaborArray" and must not be passed by the agent.\n- Language/LLM simulation mode is not supported; calling run_on_language on an Experiment containing this stimulus raises NotImplementedError.\n- The browser IIFE bundle must expose window.jsPsychGaborArray = PluginClass before the experiment runs; the emitted config is declarative and relies on that shim.\n- side_effects typing in the signature is Dict but the docstring says list — pass an array of SideEffect-shaped objects.'
TOOL_PARAMETERS = { 'properties': { 'allow_mouse': { 'default': True,
                                   'description': 'If true, a mouse click selects the '
                                                  'nearest patch center.',
                                   'type': 'boolean'},
                  'bg_gray': { 'default': 0.5,
                               'description': 'Background mean luminance in [0..1]. '
                                              '0.5 is mid-gray.',
                               'type': 'number'},
                  'canvas_height': { 'default': 600,
                                     'description': 'Canvas height in pixels.',
                                     'type': 'integer'},
                  'canvas_width': { 'default': 800,
                                    'description': 'Canvas width in pixels.',
                                    'type': 'integer'},
                  'duration': { 'description': 'SweetBean convenience alias for '
                                               'trial_duration; copied into '
                                               'trial_duration during build. Use one '
                                               'or the other, not both.',
                                'type': 'integer'},
                  'end_on_response': { 'default': True,
                                       'description': 'If true, the trial ends '
                                                      'immediately after a valid '
                                                      'response.',
                                       'type': 'boolean'},
                  'gamma': { 'default': 1,
                             'description': 'Gamma correction exponent applied to '
                                            'luminance. 1.0 means no correction.',
                             'type': 'number'},
                  'keymap_to_patch_index': { 'additionalProperties': { 'type': 'integer'},
                                             'description': 'Explicit '
                                                            'key-to-patch-index map, '
                                                            'e.g. {"f": 0, "j": 1}. If '
                                                            'omitted, the plugin '
                                                            'infers a side-based '
                                                            'mapping for arrow keys.',
                                             'type': 'object'},
                  'patches': { 'description': 'Patch list for this trial. Either a '
                                              'concrete array of patch descriptor '
                                              'dicts (see notes for fields) or a '
                                              'handle string for a TimelineVariable '
                                              'that evaluates per trial. Omit or pass '
                                              '[] for an empty canvas.',
                               'oneOf': [ { 'items': { 'properties': { 'contrast': { 'description': 'Michelson '
                                                                                                    'contrast '
                                                                                                    'in '
                                                                                                    '[0..1].',
                                                                                     'type': 'number'},
                                                                       'label': { 'description': 'Arbitrary '
                                                                                                 'tag '
                                                                                                 'copied '
                                                                                                 'into '
                                                                                                 'trial '
                                                                                                 'data.',
                                                                                  'type': 'string'},
                                                                       'orientation_deg': { 'description': 'Orientation '
                                                                                                           'in '
                                                                                                           'degrees '
                                                                                                           '[0..180).',
                                                                                            'type': 'number'},
                                                                       'phase_deg': { 'description': 'Phase '
                                                                                                     'in '
                                                                                                     'degrees '
                                                                                                     '[0..360).',
                                                                                      'type': 'number'},
                                                                       'sf_cpd': { 'description': 'Spatial '
                                                                                                  'frequency '
                                                                                                  'in '
                                                                                                  'cycles '
                                                                                                  'per '
                                                                                                  'degree. '
                                                                                                  'Requires '
                                                                                                  'px_per_deg '
                                                                                                  'on '
                                                                                                  'the '
                                                                                                  'stimulus.',
                                                                                   'type': 'number'},
                                                                       'sf_cpp': { 'description': 'Spatial '
                                                                                                  'frequency '
                                                                                                  'in '
                                                                                                  'cycles '
                                                                                                  'per '
                                                                                                  'pixel. '
                                                                                                  'Mutually '
                                                                                                  'exclusive '
                                                                                                  'with '
                                                                                                  'sf_cpd.',
                                                                                   'type': 'number'},
                                                                       'sigma_deg': { 'description': 'Gaussian '
                                                                                                     'sigma '
                                                                                                     'in '
                                                                                                     'degrees. '
                                                                                                     'Requires '
                                                                                                     'px_per_deg '
                                                                                                     'on '
                                                                                                     'the '
                                                                                                     'stimulus.',
                                                                                      'type': 'number'},
                                                                       'sigma_px': { 'description': 'Gaussian '
                                                                                                    'sigma '
                                                                                                    'in '
                                                                                                    'pixels. '
                                                                                                    'Mutually '
                                                                                                    'exclusive '
                                                                                                    'with '
                                                                                                    'sigma_deg.',
                                                                                     'type': 'number'},
                                                                       'size_px': { 'description': 'Square '
                                                                                                   'draw '
                                                                                                   'size '
                                                                                                   'in '
                                                                                                   'pixels. '
                                                                                                   'Defaults '
                                                                                                   'to '
                                                                                                   '~6*sigma_px '
                                                                                                   'if '
                                                                                                   'omitted.',
                                                                                    'type': 'integer'},
                                                                       'x_px': { 'description': 'X '
                                                                                                'center '
                                                                                                'in '
                                                                                                'pixels, '
                                                                                                'relative '
                                                                                                'to '
                                                                                                'canvas '
                                                                                                'center.',
                                                                                 'type': 'number'},
                                                                       'y_px': { 'description': 'Y '
                                                                                                'center '
                                                                                                'in '
                                                                                                'pixels, '
                                                                                                'relative '
                                                                                                'to '
                                                                                                'canvas '
                                                                                                'center.',
                                                                                 'type': 'number'}},
                                                       'type': 'object'},
                                            'type': 'array'},
                                          { 'description': 'Handle string for a '
                                                           'TimelineVariable whose '
                                                           'value is a patch list.',
                                            'type': 'string'}]},
                  'px_per_deg': { 'description': 'Pixels per visual degree. Required '
                                                 'to use sigma_deg or sf_cpd in any '
                                                 'patch. Omit if all patches use '
                                                 'pixel-based fields only.',
                                  'type': 'number'},
                  'response_keys': { 'description': 'Allowed keyboard keys. Defaults '
                                                    'to ["ArrowLeft", "ArrowRight"] if '
                                                    'omitted. Override to use custom '
                                                    'keys like ["f", "j"].',
                                     'items': {'type': 'string'},
                                     'type': 'array'},
                  'side_effects': { 'description': 'Optional list of SweetBean '
                                                   'SideEffect definitions for '
                                                   'updating global state (e.g., score '
                                                   'counter) after this trial.',
                                    'items': {'type': 'object'},
                                    'type': 'array'},
                  'timeout_ms': { 'description': 'Alias for trial_duration; takes '
                                                 'precedence over trial_duration if '
                                                 'both are provided.',
                                  'type': 'integer'},
                  'trial_duration': { 'description': 'Hard trial timeout in '
                                                     'milliseconds. Omit for no forced '
                                                     'timeout. Overridden by '
                                                     'timeout_ms if both are set.',
                                      'type': 'integer'}},
  'required': [],
  'type': 'object'}
TOOL_NOTES = '- Each patch must specify exactly one of sf_cpp or sf_cpd, and exactly one of sigma_px or sigma_deg; degree-based fields (sf_cpd, sigma_deg) silently produce incorrect output if px_per_deg is not set on the stimulus.\n- timeout_ms wins over trial_duration when both are provided; duration is a third alias that is copied into trial_duration — avoid providing more than one of the three.\n- Null/None optional fields are stripped before the plugin sees them, so the plugin\'s own defaults take effect; this means omitting a field and explicitly passing null are equivalent.\n- The type field is set internally to "jsPsychGaborArray" and must not be passed by the agent.\n- Language/LLM simulation mode is not supported; calling run_on_language on an Experiment containing this stimulus raises NotImplementedError.\n- The browser IIFE bundle must expose window.jsPsychGaborArray = PluginClass before the experiment runs; the emitted config is declarative and relies on that shim.\n- side_effects typing in the signature is Dict but the docstring says list — pass an array of SideEffect-shaped objects.'


def _impl(kwargs: dict[str, Any]) -> Any:
    target = sb.Gabor
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
    def create_gabor(args: dict[str, Any] | None = None) -> Any:
        'Call this tool in step 3 of the pipeline — after SweetPea has generated a trial sequence — to create a Gabor patch stimulus for psychophysics experiments.'
        return _impl(args or {})
