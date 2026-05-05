# experiment-mcp

A passive MCP server that wraps **SweetPea** (factorial-design library)
and **SweetBean** (declarative experiment DSL → jsPsych) as LLM-friendly
tools, with auto-generated tool descriptions for evolving APIs.

Symmetric with [`psyneulink-mcp`](../psyneulink-mcp/CLAUDE.md): same
kind of wrapper, different domain library. Read that file for the
canonical shape; this file documents what's different here.

## Working with Claude on this project

Same collaboration norms as the rest of the workspace (see
[`../AGENTS.md`](../AGENTS.md) §"Working with Claude"):

- **Surface better tools.** When something is being done the long way,
  point out the faster idiom — slash commands, skills, subagents,
  hooks, MCP, the right model for the job.
- **Suggest, don't silently do.** Mention idiomatic improvements
  briefly so I can choose.
- **Flag anti-patterns.** Especially anything that violates the
  separation-of-concerns or modularity rules below.
- **Be concrete.** Prefer "use `/skill X` instead of …" over generic
  advice.

## Repo role (lock this down)

Passive MCP server wrapping SweetPea + SweetBean. No LLM at runtime.
Reads from `cogsci-knowledge` (currently `psyneulink-corpus`) for
`tasks/`, `effects/`, and `datasets/`. Will eventually expose tools
like:

- `compile_task(task_id) → SweetBean source` — read a `TaskSpec` from
  the corpus, run it through the `psyneulink-psyche` SweetBean adapter,
  return the program string + a handle to the compiled object.
- `run_task(task_id, n_subjects=, mode='sim'|'human') → Dataset` — run
  the compiled program (sim mode = SweetBean's offline simulator;
  human mode = export jsPsych payload) and return a PSYCHE-shaped
  Dataset (handle).
- `validate_dataset(dataset, task_spec) → ValidationReport` — round-
  trip an arbitrary Dataset against the TaskSpec it claims to satisfy.

**None of these tools exist yet.** The scaffold lands the bones; the
tool surface lands once `psyneulink-psyche` Phase 1 t6 ships the
schemas they consume. See "Filling in the bones" below.

## Hard rules (separation of concerns)

Cross-repo writes and runtime imports are forbidden. The polyrepo rule
in [`../AGENTS.md`](../AGENTS.md) §"Separation of concerns is pure"
applies in full; concretely for this repo:

- **Never imports `psyneulink-mcp`, `psyneulink-agent`, `psyneulink-ui`,
  `psyneulink-psyche`** at runtime. PSYCHE schemas reach this repo as
  YAML through `corpus.py` (read via `gh`); when that pattern needs the
  Pydantic models, the right move is to import them inside a tool body
  behind try/except, not at module top level. (PSYCHE is listed as a
  dev-only dep so adapter-roundtrip tests can use it locally.)
- **Never imports `sweetpea` or `sweetbean` at module top level.** Both
  go inside individual tool implementations behind `try/except
  ImportError` so the bare server install (no `experiments` extra)
  still boots and `tools/list` still answers `[]`.
- **Reads from `cogsci-knowledge` only via `gh`** (see `corpus.py`).
  Never edits a file in that repo. Never clones it. Never has a
  filesystem assumption about it.
- **Never writes from server code** to any other repo, with one
  sanctioned exception: the auto-issue write path in `corpus.py`
  (`open_feedback_issue`, `find_existing_feedback_issue`), called
  fire-and-forget by `feedback_publisher.py` to mirror runtime captures
  into GitHub issues. Same carve-out as the sibling — see
  `psyneulink-mcp/CLAUDE.md` §Feedback loop.
- The (future) generator and the runtime feedback publisher are the
  only sanctioned writers, and both write only via `gh` — never by
  editing checked-in files.

## Modularity (cross-link)

From [`../AGENTS.md`](../AGENTS.md) §"Modularity is a hard rule":

> Removing the experiment stack must not break the modeling stack's
> tests. Removing the modeling stack must not break the experiment
> stack's tests.

For this repo concretely: a fresh clone of `experiment-mcp` plus the
sibling-path PSYCHE dep must `uv sync` and pass tests with no
`psyneulink-mcp`, no `psyneulink-agent`, and no `psyneulink-ui`
present. If a test requires the modeling stack, the test belongs in
the modeling stack. The integration surface between the two is
**only** PSYCHE-shaped artifacts in `cogsci-knowledge`.

## Multi-repo dev sessions

Same rule as the sibling: if a chat opened in this repo discovers it
needs to author changes across more than one of the polyrepo siblings
in one sitting, **stop and ask the user to open a new Cursor chat at
the parent workspace folder** (`~/Documents/code/AutoGrad/psyneulink-ai/`).
That folder is the correct workspace for multi-repo dev sessions; its
`AGENTS.md` covers the conventions. The shell sandbox restricts writes
to the workspace root; cross-repo writes from this sub-repo workspace
force a permission prompt for every shell call into a sibling. Don't
work around it with `required_permissions: ["all"]` — switch
workspaces once, work freely thereafter.

This is *not* the same as forbidden cross-repo coupling. A multi-repo
dev session produces independent commits in independent repos that
each respect the boundary.

## The generator pattern

Mirrors `psyneulink-mcp` 1:1 except for the introspection seam, which is
multi-root (sweetpea + sweetbean) instead of single-root.

1. **Seeds:** `generator/seeds.txt` lists what to wrap, using the same
   four directives as the sibling — `import-walk:`, `symbol:`,
   `package:`, `method:`. The committed file walks the top-level
   packages plus `sweetbean.stimulus` / `sweetbean.stimulus_spec` /
   `sweetbean.response_spec` / `sweetbean.block` / `sweetbean.experiment`
   submodules and pulls in user-facing methods (`Experiment.compile`,
   `Experiment.to_html`, `Experiment.run_on_language`,
   `CrossBlock.draw_design_graph`, …).
2. **Introspection** (`generator/introspection.py`) resolves each
   directive against the live wrapped libraries. Exception subclasses
   are filtered out automatically — agents don't construct `*Error`
   classes. Default `root_modules` is `("sweetpea", "sweetbean")`;
   override per-call if you want a narrower walk.
3. **LLM call** (`generator/adapters/`) sends a per-symbol prompt
   built from `generator/prompts.py`. The default adapter shells out
   to the local `claude` CLI in `--print --json-schema` mode (uses
   the user's Claude Max subscription via the CLI's local OAuth — no
   API key needed). The Anthropic API adapter is an opt-in fallback.
   Adapter selection is env-only via `$EXPERIMENT_MCP_LLM_ADAPTER`.
4. **Module rendering** (`generator/template.py`) emits one Python
   file per symbol into `src/experiment_mcp/tools/generated/`.
   Modules are namespaced by root (`sweetpea_block.py` vs
   `sweetbean_block.py`) so the two libraries' identical class names
   never collide. Each module imports its symbol's root package as
   the canonical short alias (`sp` / `sb`).
5. **Re-run** when SweetPea / SweetBean updates land. Source-hash
   skip means unchanged symbols don't re-hit the LLM. Review the
   diff in PR.

Build-time codegen, not runtime. The server itself never talks to an
LLM.

### Regenerating the auto layer

```bash
uv run experiment-mcp-generate                 # full regen, real LLM
uv run experiment-mcp-generate --dry-run       # placeholder ToolSpecs (CI sanity)
uv run experiment-mcp-generate --only Experiment,CrossBlock
uv run experiment-mcp-generate --rerender      # re-template from on-disk metadata,
                                                # no LLM call
```

Default adapter is `claude_cli`. Override the model with
`$EXPERIMENT_MCP_CLAUDE_MODEL` (default: `sonnet`); the per-call
timeout with `$EXPERIMENT_MCP_CLAUDE_TIMEOUT_S` (default: 300s).

### Source installs of SweetPea + SweetBean (NOT PyPI)

`pyproject.toml` pins both wrapped libraries to upstream Git branches
via `[tool.uv.sources]`:

```toml
sweetpea  = { git = "https://github.com/sweetpea-org/sweetpea-py", branch = "master" }
sweetbean = { git = "https://github.com/AutoResearch/sweetbean",   branch = "main"   }
```

This is intentional and symmetric with how `psyneulink-mcp` pulls
`psyneulink` from the upstream `devel` branch — PyPI lags both repos
by months in practice. The first `uv lock` after a fresh clone takes
~30s while uv clones both repos; subsequent ones are instant.
SweetPea's SAT-solver C extensions (`pycryptosat`, `pycmsgen`,
`pyunigen`) compile on first sync but cache between runs.

Do **not** "fix" the asymmetry between sweetpea (`master`) and
sweetbean (`main`) — those are the actual default branches upstream.

## Tool surface

- `tools/generated/` — auto-generated SweetPea / SweetBean wrappers
  (empty until the generator lands).
- `tools/curated/` — hand-authored tools (empty until Phase 2 t6e).

Live SweetPea / SweetBean / Dataset objects flow through the in-process
handle registry in `handles.py`. Unlike the sibling — which has a
PNL-specific class-name resolver baked into `resolve_in` — the
registry here is **deliberately polymorphic**: SweetPea `Block` /
`Factor`, SweetBean `Trial` / `Stimulus` / `Block`, raw jsPsych dicts,
pandas frames, and PSYCHE `Dataset` instances all coexist behind the
same handle protocol. No domain-library imports happen in
`handles.py`; class-name auto-resolution can be added later if a
concrete pain point emerges.

## Feedback loop

Same shape as the sibling. Three streams will feed the generator:

- **Auto-captured runtime errors** (local JSONL). `captured_tool` (in
  `feedback.py`) wraps every registered tool — generated or curated —
  and logs args + traceback to `feedback/pending/issues.jsonl` before
  re-raising any exception.
- **Agent-reported issues** (local JSONL). A future
  `report_tool_issue` curated tool will let the agent flag problems
  that didn't crash but are still wrong.
- **Human-reported issues** (GitHub Issues on `cogsci-knowledge`).
  Humans file `feedback`-labeled issues; the MCP never writes to
  GitHub apart from the runtime auto-mirror; the generator pulls
  these via `gh issue list` at regen time.

Local entries share a common envelope (`source`, `tool_name`,
`tool_layer`, `domain_versions`, `server_version`, `timestamp`,
`payload`). The logger swallows its own exceptions — feedback breakage
must never turn a normal tool error into a server crash.

The local feedback path is overridable via
`EXPERIMENT_MCP_FEEDBACK_PATH`. The corpus repo is overridable via
`EXPERIMENT_MCP_CORPUS_REPO` (default: `younesStrittmatter/psyneulink-corpus`,
flips to `cogsci-knowledge` in Phase 5 `t-rename` — keep in lockstep
with `psyneulink_mcp.corpus.CORPUS_REPO_DEFAULT`). Auto-issue
publishing is opt-out via `EXPERIMENT_MCP_AUTO_FILE_ISSUES=0`.

## Stack

- `uv` for deps and venvs
- `pyproject.toml` only (no setup.py, no requirements.txt)
- `mcp` (FastMCP) for the server
- `ruff` for lint+format
- `pytest` for tests
- MCP Inspector for manual testing

## Conventions

- Python 3.10+ (default interpreter pinned to 3.12 via `.python-version`,
  matching the sibling).
- Type hints everywhere.
- Tool descriptions written for LLMs: focus on WHEN to call, not just
  what.
- Every tool gets at least one pytest test (curated tools when written,
  generated tools as part of the generator's emitted module).
- Generator output is reviewed before commit.

## Workflow

1. `uv run experiment-mcp` to start the server (stdio).
2. `npx @modelcontextprotocol/inspector uv run experiment-mcp` for the
   inspector (when there are tools to inspect).
3. `uv run pytest` for tests.
4. `uv run experiment-mcp-generate` (or `uv run python
   scripts/generate_tools.py`) to regenerate the auto layer. Default
   adapter is `claude_cli`; see "Regenerating the auto layer" above.

## Filling in the bones

Future work — pointers, not prescriptions:

- **`tools/curated/compile.py`** — first real tool. Reads a TaskSpec
  out of `cogsci-knowledge` via `corpus.py`, runs it through the
  PSYCHE SweetBean adapter (`psyneulink-psyche/adapters/sweetbean.py`,
  Phase 2 t6c), returns `(jsPsych source, handle)`. Wrap with
  `@captured_tool(mcp, layer="curated")`.
- **`tools/curated/run.py`** — second real tool. Wraps SweetBean's
  offline simulator (sim mode) and exports a jsPsych payload (human
  mode). Returns a PSYCHE Dataset (handle).
- **`tools/curated/validate.py`** — third real tool. Round-trips an
  arbitrary Dataset against the TaskSpec it claims to satisfy.
- **`tools/curated/feedback.py`** — `report_tool_issue` escape hatch
  (mirror `psyneulink-mcp/src/psyneulink_mcp/tools/curated/feedback.py`).
- **Real regen:** the dry-run pipeline is wired and tested; the next
  step is a real `uv run experiment-mcp-generate` to fill the 130+
  generated tool modules in `tools/generated/`. Review the diff
  before merging.
- **Roadmap issue:** see this repo's open `roadmap`-labeled issues for
  the canonical Phase 2 t6e plan and current status.
- **Parent context:** [`../AGENTS.md`](../AGENTS.md) for the workspace
  rules; [`../PLAN.md`](../PLAN.md) for the cross-repo roadmap.
