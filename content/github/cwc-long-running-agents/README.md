# Harness Primitives for Long-Running Claude Agents

Claude Code's built-in [`/goal`](https://code.claude.com/docs/en/goal) command gives you a generator/evaluator loop out of the box: set a completion condition and a separate fast model checks it after every turn until it's met. This repo ships the same underlying primitives as short, readable [hooks](https://code.claude.com/docs/en/hooks) and a [subagent](https://code.claude.com/docs/en/sub-agents), so you can see how each mechanism works and assemble a harness tuned to your project. The patterns come from [Effective Harnesses for Long-Running Agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) (Nov 2025) and [Harness Design for Long-Running Application Development](https://www.anthropic.com/engineering/harness-design-long-running-apps) (Mar 2026). We recommend trying both the in-product features and a custom harness to see which fits your workflow.

| | In-product | Custom harness (this repo) |
|---|---|---|
| **What runs the loop** | [`/goal`](https://code.claude.com/docs/en/goal) | the [primitives below](#the-quality-loop) + a [loop you write](#running-the-loop) |
| **Who judges "done"** | a separate fast model checking your condition | your [`agents/evaluator.md`](./claude-code-config/.claude/agents/evaluator.md) with your prompt |
| **Where it works** | Claude Code interactive, [`-p`](https://code.claude.com/docs/en/headless), Remote Control | Claude Code, headless, or [Agent SDK](https://docs.claude.com/en/docs/claude-code/sdk) |

Three primitives form the quality loop:

- **Default-FAIL contract.** Every criterion starts `false`; the agent can't mark it passing without opening evidence first.
- **Fresh-context evaluator.** A separate agent with no Write/Edit tools grades the work from a context window that never saw the build.
- **Agent-maintained handoff.** The agent writes its own progress notes and commits to git so the next session picks up cleanly.

Two more operator-control hooks are included for when you want to watch or intervene. The same patterns translate directly to `PreToolUse`/`Stop` callbacks in the [Agent SDK](https://docs.claude.com/en/docs/claude-code/sdk).

> Built as the take-home for the Long-Running Agents station at Code with Claude 2026. **These are example ingredients, not a turnkey harness.** Event demo; not maintained and not accepting contributions.

## How to use this repo

**Read and cherry-pick.** Each primitive is one standalone file with no dependency on the others. The [quality-loop table](#the-quality-loop) below maps every one to its example here and its Agent SDK equivalent. Open the file, see how the mechanism works, copy what fits.

**Or copy all of them as a starting point.** In your project, run `claude` and paste:

> Clone github.com/anthropics/cwc-long-running-agents into /tmp, copy its `claude-code-config/.claude/` directory into this project's root, make the hook scripts executable, then walk me through what each hook and the evaluator subagent does and what I'll need to adapt for this project.

or do it yourself:

```bash
cp -r claude-code-config/.claude /path/to/your/project/
chmod +x /path/to/your/project/.claude/hooks/*.sh
```

Either way, this gives you all the examples wired into `.claude/` at once. Before relying on them: point `RESULTS_FILE` at your project's actual results file, adjust the evidence-file pattern in `track-read.sh`, and run `claude` from the directory that contains `.claude/` (hooks are not loaded when launching from a subdirectory).

**If you're on the Agent SDK,** this repo is a pattern reference. The shell hooks here translate one-to-one to `PreToolUse`/`Stop` callbacks. To scaffold an SDK agent from inside Claude Code, install the [`agent-sdk-dev` plugin](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/agent-sdk-dev) and ask Claude to build an agent that implements whichever of these primitives you want. For a hand-written starting point, see the [autonomous-coding quickstart](https://github.com/anthropics/claude-quickstarts/tree/main/autonomous-coding) or the [agent-sdk-workshop](https://github.com/anthropics/agent-sdk-workshop) curriculum.

## The quality loop

| Primitive | Claude Code example | Agent SDK equivalent | Enforcement |
|---|---|---|---|
| **Default-FAIL contract** | [`hooks/track-read.sh`](./claude-code-config/.claude/hooks/track-read.sh) + [`hooks/verify-gate.sh`](./claude-code-config/.claude/hooks/verify-gate.sh) | `PreToolUse` callback | hook |
| **Fresh-context evaluator** | [`agents/evaluator.md`](./claude-code-config/.claude/agents/evaluator.md) subagent (no Write/Edit) | [`evaluator_optimizer.ipynb`](https://github.com/anthropics/claude-cookbooks/blob/main/patterns/agents/evaluator_optimizer.ipynb) | you invoke it |
| **Agent-maintained handoff** | [`CLAUDE.md`](./claude-code-config/.claude/CLAUDE.md) + [`hooks/commit-on-stop.sh`](./claude-code-config/.claude/hooks/commit-on-stop.sh) | system prompt + `Stop` callback | convention + hook backstop |

### Default-FAIL contract

Agents will mark a feature "passing" after a unit test or a curl when the UI is visibly broken. Asking nicely in the prompt doesn't reliably stop this. The harness makes "done" structural. Every feature is a row in a `test-results.json` file you create in your project:

```json
{ "feature-1": { "passes": false }, "feature-2": { "passes": false } }
```

The only evidence that counts is a file matching the patterns in `track-read.sh` (screenshots, console logs, result files), and a `PreToolUse` hook denies any write to the results file unless the agent has first opened one with the Read tool. The agent can't claim success it hasn't observed. (The shipped hook is intentionally simple; see the comments in `verify-gate.sh` for the gaps a production version would close.)

### Fresh-context evaluator

The builder shouldn't grade its own work. After each feature, you (or your wrapper script) invoke a separate subagent (`agents/evaluator.md`) with no Write/Edit tools that reviews the diff and the screenshots from a context window that never saw the build, then returns `PASS` or `NEEDS_WORK` with specific findings. On `NEEDS_WORK` the findings become the next builder session's starting prompt, closing the build/evaluate/rebuild loop. Invoke it from your wrapper with `claude --agent evaluator -p "<review prompt>"`; what your loop does with the verdict is up to you.

### Agent-maintained handoff

A fresh session has no memory of what the previous one did, and when a long session fills its context window Claude Code summarizes the history, which loses detail. So the agent maintains the handoff itself: it scopes each session to one feature, writes to a structured `PROGRESS.md` as it works and re-reads it first thing on every restart, and `git add`s and commits at meaningful checkpoints so `git log` is a second record. `commit-on-stop.sh` is the backstop that catches whatever's still uncommitted at session end. This is the layer most sensitive to model capability; newer models drift less and self-scope better, so re-evaluate how much of `CLAUDE.md` you still need after each model release (see [Re-simplify on model upgrades](#going-further)).

A fourth core piece, a **rubric for subjective work**, isn't shipped here because it's project-specific; see [Going further](#going-further) for how to add one to the evaluator.

## Running the loop

Two ways to keep the build → evaluate → rebuild cycle going. `/goal` is built into Claude Code and works with or without this repo's primitives; the second path wires the contract file and your own `evaluator.md` directly into the loop.

### `/goal`: built-in completion checker

```
/goal every feature in PROGRESS.md is implemented, committed, and its tests pass
```

After every turn a separate fast model checks the condition and keeps the session going until it's met. One line, no contract file or hooks. Works the same in interactive Claude Code, [`claude -p`](https://code.claude.com/docs/en/headless), and Remote Control. See the docs for [writing an effective condition](https://code.claude.com/docs/en/goal#write-an-effective-condition) and how `/goal` [compares to `/loop` and Stop hooks](https://code.claude.com/docs/en/goal#compare-to-other-autonomous-workflows).

### Your `evaluator.md` as the gate

When you want the default-FAIL contract (`test-results.json` + `verify-gate`) enforcing evidence and your own evaluator prompt deciding `PASS`/`NEEDS_WORK`, the loop lives in your code. How depends on where you're running:

| Surface | How |
|---|---|
| **Claude Code** | custom [Stop hook](https://code.claude.com/docs/en/hooks#stop) runs the evaluator as a fresh `claude` process after each turn and blocks on anything but `PASS` |
| **Headless** ([`claude -p`](https://code.claude.com/docs/en/headless)) | wrapper script calls `claude --agent evaluator -p` between builds (example below) |
| [**Agent SDK**](https://docs.claude.com/en/docs/claude-code/sdk) | separate generator and evaluator `query()` calls; see [`evaluator_optimizer`](https://github.com/anthropics/claude-cookbooks/blob/main/patterns/agents/evaluator_optimizer.ipynb) |

```bash
while grep -q '"passes": false' test-results.json; do
  claude -p "Read PROGRESS.md and build the next unfinished feature per CLAUDE.md."
  VERDICT=$(claude --agent evaluator -p "Review the most recent commit against its spec.")
  [ "$(echo "$VERDICT" | head -1)" = "PASS" ] || echo "$VERDICT" > NEXT_FINDINGS.md
done
```

Each pass is a fresh context. Exit when the contract file has nothing left failing, a cycle makes no changes, or a budget is hit; `touch AGENT_STOP` to stop early. The builder writes `test-results.json` (verify-gate enforces evidence-read first) and the evaluator returns a separate verdict; have your wrapper write the contract on `PASS` instead if you want "all true" to mean "independently confirmed."

## Operator controls

Two more hooks for when you want to watch the loop run or intervene mid-stream:

| Hook | What it does |
|---|---|
| [`hooks/kill-switch.sh`](./claude-code-config/.claude/hooks/kill-switch.sh) | Halts every tool call while an `AGENT_STOP` file exists at the project root. |
| [`hooks/steer.sh`](./claude-code-config/.claude/hooks/steer.sh) | Surfaces the contents of `STEER.md` (project root) to the agent once and clears it, so you can redirect mid-run without restarting. |

## Watching it work

Everything the agent does lands on disk, so you can observe a long run from a terminal without any dashboard code:

```bash
watch -n 2 'tail -20 PROGRESS.md'                          # its own notes
watch -n 5 'git log --oneline -8'                          # work saved
watch -n 5 'find screenshots -name "*.png" | tail -5'      # what it sees
watch -n 2 'wc -l < .claude/.evidence-reads 2>/dev/null'   # evidence reads (resets to 0 after each gated write)
```

Run them in a `tmux` grid and you have a live view of every primitive.

## Going further

The next layer of patterns, each covered in depth in [Harness Design for Long-Running Application Development](https://www.anthropic.com/engineering/harness-design-long-running-apps):

| Pattern | What it adds | Reference |
|---|---|---|
| **Unattended loop** | Cap session length and have an outer script start the next one (pick next feature, build, evaluate, reset) | [Why naive implementations fall short](https://www.anthropic.com/engineering/harness-design-long-running-apps#why-naive-implementations-fall-short); [`ralph-loop`](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/ralph-loop) plugin |
| **Planner agent** | A first session that expands a one-line ask into a `BUILD_PLAN.md` the loop then runs against | [The architecture](https://www.anthropic.com/engineering/harness-design-long-running-apps#the-architecture) |
| **Sprint contracts** | Builder and evaluator agree per-feature on what "done" means and write it to a file the hook enforces | [The architecture](https://www.anthropic.com/engineering/harness-design-long-running-apps#the-architecture) and [Removing the sprint construct](https://www.anthropic.com/engineering/harness-design-long-running-apps#removing-the-sprint-construct) |
| **Grading rubrics** | Give the evaluator scoring principles (functionality, design, craft, originality) with few-shot examples instead of binary pass/fail | [Frontend design: making subjective quality gradable](https://www.anthropic.com/engineering/harness-design-long-running-apps#frontend-design-making-subjective-quality-gradable); [`frontend-design`](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/frontend-design) plugin |
| **Browser-verified evaluator** | Let the evaluator open the running app itself instead of trusting the builder's screenshots | [Frontend design](https://www.anthropic.com/engineering/harness-design-long-running-apps#frontend-design-making-subjective-quality-gradable) (Playwright MCP usage); add [`@playwright/mcp`](https://github.com/microsoft/playwright-mcp) or Claude in Chrome to `tools:` in `agents/evaluator.md` |
| **Re-simplify on model upgrades** | After each model release, comment out harness pieces one at a time and see what's still load-bearing | [What comes next](https://www.anthropic.com/engineering/harness-design-long-running-apps#what-comes-next); [Harnessing Claude's Intelligence](https://claude.com/blog/harnessing-claudes-intelligence) |
| **Hosted runtime** | Anthropic hosts the loop, sandbox, and scheduling so you don't run any of this yourself | [Claude Managed Agents](https://docs.claude.com/en/docs/managed-agents) |

---
