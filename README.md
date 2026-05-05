# experiment-mcp

A passive MCP server that wraps [SweetPea](https://sites.google.com/view/sweetpea-ai)
(factorial-design) and [SweetBean](https://autoresearch.github.io/sweetbean/)
(declarative experiment DSL → jsPsych) as LLM-friendly tools. The
runtime has **no** LLM dependency — tool descriptions will be committed
Python written by a build-time generator (when that lands in Phase 2 t6e).

Symmetric with [`psyneulink-mcp`](../psyneulink-mcp/), which wraps
PsyNeuLink. Same shape, different domain library. Both read from
`cogsci-knowledge` (currently `psyneulink-corpus`); both publish runtime
errors as GitHub issues; neither imports the other.

For the polyrepo architecture and the separation-of-concerns rules see
the parent workspace [`AGENTS.md`](../AGENTS.md) and this repo's
[`CLAUDE.md`](./CLAUDE.md). Per-repo roadmap status lives in this
repo's GitHub issues with the `roadmap` label.

## Status

**Phase 2 scaffold.** The directory tree, `pyproject.toml`,
session-handle registry, runtime feedback capture, corpus reader, and
auto-issue publisher are all in place and mirror the sibling. **Zero
MCP tools are registered yet** — the tool surface (`compile_task`,
`run_task`, `validate_dataset`) lands once `psyneulink-psyche` Phase 1
t6 ships the schemas they consume. See `plans/` and the open `roadmap`
issue for what's next.

## Quickstart

```sh
uv sync
uv run experiment-mcp --help
uv run pytest
```

`uv sync` installs the lean server (no `sweetpea`, no `sweetbean`).
Add the `experiments` extra once tools start importing them:

```sh
uv sync --extra experiments
```

## Layout (mirrors psyneulink-mcp)

```
src/experiment_mcp/
  server.py            FastMCP entry point (stdio + SSE), no tools yet
  handles.py           Session-scoped registry of live SweetPea / SweetBean / Dataset objects
  feedback.py          captured_tool wrapper + JSONL log (EXPERIMENT_MCP_FEEDBACK_PATH)
  feedback_publisher.py Fire-and-forget GitHub issue mirror, with dedup
  corpus.py            gh-CLI reader for tasks/, effects/, datasets/
  tools/curated/       Hand-authored tools (empty)
  tools/generated/     Generator output (empty)
generator/seeds.txt    Symbol selector for the future codegen
plans/                 In-flight per-repo plans
tests/test_smoke.py    Hermetic boot check (1 test)
```
