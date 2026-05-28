<!-- Copyright 2026 Anthropic PBC -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# τ-bench setup (for attendees without an eval)

Sierra's open-source benchmark for agentic tool use. The maintained repo is `sierra-research/tau2-bench` (the original `tau-bench` repo is marked outdated by Sierra); cloning it gets you the current τ³ task set with fixed airline/retail domains. The CLI is still `tau2`. An agent talks to a simulated user over multiple turns, calls domain tools (look up reservations, change flights, issue refunds), and is scored pass/fail on whether the final database state matches the goal. The `airline` domain is small enough to run a 20-task slice in roughly 5-10 minutes per model, which makes it a good stand-in eval for the sweep exercise.

If you already have your own eval, skip this file entirely and point the `eval-audit-and-sweep` skill at your code instead.

> **If you're letting Claude Code run this setup for you:** Claude, before executing anything below, use the `AskUserQuestion` tool to confirm the user's preferences in one shot:
> 1. Installer (`pip` in a fresh venv, or `uv`), so you run the matching commands and prefix `tau2` with `uv run` if needed.
> 2. Where to clone the repo (default: a `tau2-bench/` subfolder of the current directory).
>
> Detect the operating system from the environment rather than asking; you already have it.
>
> Then adapt the commands below to those answers rather than running them verbatim.
>
> Checkpoints to surface as you go:
> - **Python version.** Run `python3 --version` first. `pyproject.toml` permits 3.12 and 3.13, but 3.13 removed `audioop` from the stdlib and tau2's base install imports it unconditionally; prefer 3.12 when available, and if you end up on 3.13 you MUST also `pip install audioop-lts` after `pip install -e .` (see "Known gotchas" below). If `python3` isn't in 3.12/3.13, don't reach for a new install yet: list every interpreter the user already has (`which -a python3`, `uv python list`, `pyenv versions`) and pick whichever satisfies the constraint with the fewest workarounds. The existing environment is data, not an obstacle. If nothing qualifies and you do download a new interpreter, verify it actually runs (`python3.12 --version`) before building on it. Downloaded binaries can be blocked by OS security policy, corporate endpoint tooling, or quarantine flags, and the failure (SIGKILL, exit 137) won't explain why.
> - **API key handling.** Don't ask the user to paste their key into chat, and don't `echo`/`printf` it to a file: that leaks it into your transcript. Don't ask whether `ANTHROPIC_API_KEY` is exported either — check programmatically: `python3 -c "import os; print('set' if os.environ.get('ANTHROPIC_API_KEY') else 'missing')"`. If `set`, write it into `.env` with a small Python snippet that reads the env var and does a string replace on the placeholder (never print the value). If `missing`, copy `.env.example` to `.env` and tell the user to edit that line themselves; do not offer to read it from any other location.
> - **Don't tail `results.json` for progress.** tau2 creates the results file up-front with `"simulations": []` and only writes entries once the whole run finishes. If you background the run, wait for the process to exit (e.g. `until ! pgrep -f "tau2 run" > /dev/null; do sleep 3; done`) before inspecting results. Stdout is also heavily buffered, so a `tail -f` of the captured output will look silent for minutes. This applies in the foreground too: even a 1-task smoke test prints nothing for 1-2 minutes before the metrics panel appears. Don't assume the process is hung.
> - **Shell state doesn't persist between Bash calls in most harnesses.** `cd` into the repo sticks (working directory is preserved), but `source .venv/bin/activate` does NOT carry across separate tool invocations. Either chain every command with `&&` after `source .venv/bin/activate`, or call the venv binaries by absolute path (`.venv/bin/pip`, `.venv/bin/tau2`). Running `pip install` or `tau2` without re-activating will hit the system Python and fail confusingly.

## Prerequisites

- Python 3.12 or 3.13 (hard requirement from `pyproject.toml`; check with `python3 --version`)
- An `ANTHROPIC_API_KEY`
- `git`

## Install

Use a fresh virtualenv so tau2's pinned dependencies don't fight with whatever else is in your global Python:

```bash
git clone https://github.com/sierra-research/tau2-bench
cd tau2-bench
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

If pip prints a red `ERROR: pip's dependency resolver...` block about unrelated packages, ignore it; the install succeeded as long as the last line reads `Successfully installed ... tau2-1.0.0`.

### If you picked `uv` instead of `pip`

Run `uv sync` in place of the venv + `pip install -e .` above. Then stay in `uv` for everything downstream.

Tools that manage their own environment (`uv`, `poetry`, `hatch`, `conda`) are not interchangeable with tools that mutate whatever's active (`pip`, `conda install`). Mixing them silently installs into the wrong place, and the failure surfaces later as an import error, not at install time.

Concretely, with `uv`:
- `uv add <package>` for dependencies (persists in the lockfile, survives `uv sync`), not bare `pip install`.
- `uv run tau2 ...` or `uv run python ...` for execution, not bare `python` or `tau2`.
- Verify the dep is reachable from the same entrypoint you'll actually use: `uv run python -c "import X"`, not whichever `python3` your shell resolves.

The general principle: install and execute through the same path, and verify through that path too. A package that imports fine in one environment proves nothing about another.

### Python 3.13: install `audioop-lts`

If your active interpreter is 3.13, run:

```bash
pip install audioop-lts
```

Python 3.13 removed `audioop` from the stdlib. `tau2.voice.utils.audio_preprocessing` imports it unconditionally, and that module is pulled in by the base import chain (`tau2.cli` → `runner` → `evaluator` → `agent.base.streaming` → `voice.utils.audio_preprocessing`), so every `tau2 run` will crash with `ModuleNotFoundError: No module named 'audioop'` until the backport is installed. On 3.12 this is not needed.

### Known gotchas (especially on `uv`)

`uv` builds a **universal lock** across the full `requires-python` range and all optional extras, so a single broken dep anywhere in `pyproject.toml` breaks `uv sync` even if you'd never install that extra. Plain `pip install -e .` is much more forgiving and is the recommended fallback if any of this turns hairy.

The three failure modes I've hit, in order of how likely you are to see them:

1. **`requires-python = ">=3.12,<3.14"` + Python 3.13 active.** Some transitive deps (e.g. `aws-sdk-bedrock-runtime`) have no 3.13 wheel, so uv's 3.13 resolution split fails even when your active interpreter is 3.12. Fix: narrow the line to `">=3.12,<3.13"` in the local clone's `pyproject.toml`. Do NOT just pass `--python 3.12` — the universal lock still resolves for 3.13.

2. **Private PyPI mirror gates unapproved packages.** If your environment proxies PyPI (common in corporate setups) and you see `Because there are no versions of <package>` for something that clearly exists on public PyPI, the mirror is blocking it. Fastest path: if the package is in an unused extra (the `voice` extra is the usual culprit, e.g. `aws-sdk-bedrock-runtime`, `livekit-agents`), just delete that whole extra block from `pyproject.toml` and remove it from the `all = [...]` meta-extra. The airline domain doesn't need `voice`, `knowledge`, `gym`, or `experiments` to run the smoke test, only the base install.

3. **`livekit-agents>=1.5.0` has no win32 resolution.** Same mitigation: drop the `voice` extra.

If you end up editing `pyproject.toml`, also delete the stale `uv.lock` before re-running `uv sync`. Don't commit these edits — they're local workarounds, not upstream fixes.

### Configure your API key

```bash
cp .env.example .env
```

Open `.env` and replace `<your_key_here>` on the `ANTHROPIC_API_KEY=` line with your real key. You can leave the OpenAI / ElevenLabs / Deepgram / OpenRouter lines as-is; they aren't used in this workshop.

> **Claude:** check whether the key is reachable before doing anything else:
>
> ```bash
> python3 -c "import os; print('set' if os.environ.get('ANTHROPIC_API_KEY') else 'missing')"
> ```
>
> If `set`, write it in with a small Python snippet so the key never hits your transcript:
>
> ```bash
> python3 -c "
> import os
> key = os.environ['ANTHROPIC_API_KEY']
> with open('.env') as f: s = f.read()
> s = s.replace('ANTHROPIC_API_KEY=<your_key_here>', f'ANTHROPIC_API_KEY={key}')
> with open('.env','w') as f: f.write(s)
> "
> ```
>
> If `missing`, tell the user to open `.env` and replace `<your_key_here>` themselves, then continue. Don't go hunting for the key in shell profiles or credential stores.

τ²-bench routes model calls through LiteLLM, so Claude models are addressed as `anthropic/claude-<id>`.

## Smoke test (1 task, cheap)

Verify the wiring before the workshop:

```bash
tau2 run \
  --domain airline \
  --agent-llm anthropic/claude-haiku-4-5 \
  --user-llm anthropic/claude-haiku-4-5 \
  --num-tasks 1 \
  --num-trials 1
```

This takes 1-2 minutes and may sit quietly while the agent and simulated user exchange turns. **Success = the process exits cleanly and prints the `Agent Performance Metrics` panel.** `Average Reward` will be 0.0 or 1.0 depending on the task draw; either is fine for a smoke test, the point is that the wiring works. Only treat it as a failure if the process errors out or no metrics panel appears. Raw results are written to `data/simulations/<timestamp>_.../results.json`; run `tau2 view` to browse them interactively.

One-shot command to parse the newest results file without improvising paths:

```bash
python3 -c "import json,glob; p=sorted(glob.glob('data/simulations/*/results.json'))[-1]; d=json.load(open(p)); s=d['simulations'][0]; print('file:', p); print('reward:', s['reward_info']['reward']); print('termination:', s.get('termination_reason'))"
```

> **Claude, if you're running this in the background:** `tau2` buffers stdout, and `results.json` is created up-front with `"simulations": []` and only populated once the run finishes. Don't try to infer progress by tailing either one. Wait for the process to exit (e.g. `until ! pgrep -f "tau2 run" > /dev/null; do sleep 3; done` in a background task), then read the output file and `results.json`.

## Next step

Once the smoke test passes, open Claude Code in the `tau2-bench` directory and ask it to run the `eval-audit-and-sweep` skill. Phase 2 of that skill reads a tau2-bench-specific companion file, so it already knows where to patch the harness for thinking/effort, which 20 stratified airline tasks to use, and how to read results; it will build the full model x thinking x effort grid, run it across multiple trials, and produce the three comparison plots (pass rate vs output tokens, cost, and latency).


## Workshop run

This is the command the sweep will wrap. Swap `--agent-llm` for each cell in your grid; keep `--user-llm` fixed on Haiku so the simulated user is a constant.

```bash
tau2 run \
  --domain airline \
  --agent-llm anthropic/<MODEL_UNDER_TEST> \
  --user-llm anthropic/claude-haiku-4-5 \
  --num-tasks 20 \
  --num-trials 1
```

