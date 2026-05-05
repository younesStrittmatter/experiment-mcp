# tools/curated/

Hand-authored MCP tools live here. These are the tools whose *behaviour*
is too important to entrust to a regenerator — for example tools that
deliberately encode special cases learned from captured runtime
failures, or tools that orchestrate several SweetPea / SweetBean calls
in a way the introspector can't infer.

Symmetric with `psyneulink-mcp/src/psyneulink_mcp/tools/curated/`.

## Conventions

- One module per tool (or per closely related cluster of tools).
- Each module exposes `register(mcp)` and uses `@captured_tool(mcp,
  layer="curated", ...)` from `experiment_mcp.feedback` so runtime
  exceptions auto-capture into `feedback/pending/issues.jsonl`.
- Domain libraries (`sweetpea`, `sweetbean`) are imported **lazily
  inside the tool body**, behind `try/except ImportError`, so the
  server boots cleanly without the `experiments` extra installed.
- Live SweetPea / SweetBean / Dataset objects are stashed via
  `experiment_mcp.handles.register_handle` and returned to the agent
  as handle payloads, never as raw objects.

## Roadmap

The first curated tools to land (Phase 2 t6e) are likely:

- `compile_task(task_id) -> SweetBean source` — read a `TaskSpec` from
  `cogsci-knowledge`, run it through the `psyneulink-psyche` SweetBean
  adapter, return the program string + a handle to the compiled object.
- `run_task(task_id, n_subjects=, mode='sim'|'human') -> Dataset` — run
  the compiled program (sim mode = SweetBean's offline simulator;
  human mode = export jsPsych payload) and return a PSYCHE-shaped
  Dataset (handle).
- `validate_dataset(dataset, task_spec) -> ValidationReport` — round-
  trip an arbitrary Dataset against the TaskSpec it claims to satisfy.
- `report_tool_issue(...)` — agent-side feedback escape hatch.

None of these exist yet. See the repo's roadmap issues on GitHub for
status.
