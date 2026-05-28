<!-- Copyright 2026 Anthropic PBC -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# Picking the Right Model

Workshop materials. Not maintained and not accepting contributions.

This folder contains the materials for the **Picking the Right Model** workshop at the Code with Claude conference. The goal of the session is to show how Claude Code can leverage a SKILL to help you (a) **audit** an existing LLM evaluation suite for reliability issues, and (b) **sweep** that eval across models and inference parameters (extended thinking, effort) to find the best quality-per-dollar and quality-per-second configuration for your task.

## What's in here

```
cwc-workshop/
├── README.md                         # you are here
├── TAU_BENCH_SETUP.md                # fallback eval install guide (see below)
└── .claude/skills/eval-audit-and-sweep/
    ├── SKILL.md                      # entrypoint; routes to the two phases
    └── references/
        ├── audit.md                  # Phase 1: eval health checklist
        ├── sweep.md                  # Phase 2: grid, instrumentation, plotting
        └── tau2-bench.md             # sweep specifics for tau2-bench
```

## The two phases

### Phase 1: Audit (take-home)

A sweep is only as trustworthy as the eval underneath it. `references/audit.md` is a checklist of the common "gotchas" in task design, harness design, metrics hygiene, and grader design (including LLM-judge biases) that quietly erode an eval's ability to give you a high-signal verdict on which model is actually better for your use case. It distills what we cover in the slides into something actionable and framework-agnostic, intended for you to take back and point at **your own** eval suites after the conference.

To run it later, open Claude Code in your eval repo (with this skill installed) and paste:

> Use the eval-audit-and-sweep skill to audit this eval suite. Walk through task design, harness design, metrics hygiene, and grader design, cite specific files and task IDs, and offer to fix anything small you find.

### Phase 2: Sweep (live exercise)

`references/sweep.md` describes how to wrap any eval in a model x thinking x effort grid, instrument per-cell pass rate / cost / latency, and produce three comparison plots plus a one-sentence recommendation. This is what we will build together live during the workshop.

## How to run the live exercise

### Option A: You brought your own eval

Copy `.claude/skills/eval-audit-and-sweep/` into your eval's repo (or launch Claude Code from this folder and `--add-dir` your eval). Then open Claude Code there and paste:

> Use the eval-audit-and-sweep skill on this repo. Skip the audit and go straight to the sweep. Find the eval entrypoint, patch in the thinking and effort knobs, confirm the model list and trial count with me, then run the full grid and generate the plots.

### Option B: You don't have an eval handy

Use Sierra's **tau2-bench** (airline domain) as a stand-in.

**Step 1: Install.** Open Claude Code in this folder and paste:

> Read TAU_BENCH_SETUP.md and follow the instructions in the file.

**Step 2: Run the sweep.** Once the smoke test passes, `cd tau2-bench`, open Claude Code there, and paste the prompt below:

**NOTE**: For the sake of time, instead of running all 50 tasks in the benchmark, we use a difficulty-stratified 20-task subset of tau2-bench airline (ranked by Haiku baseline pass rate across 3 trials).

> Use the eval-audit-and-sweep skill. Skip the audit for now and do a sweep for this eval (taubench airline).

The skill's tau2-bench companion file means Claude already knows:

- which 20 stratified airline `--task-ids` to use,
- exactly where to patch `llm_agent.py` to inject `thinking` / `output_config.effort` via env vars,
- how to read pass rate, `agent_cost`, output tokens, and generation time from `results.json`,
- and how to emit `sweep_tokens.png`, `sweep_cost.png`, and `sweep_latency.png`.


## Requirements

- Claude Code
- An `ANTHROPIC_API_KEY`
- For Option B: Python 3.12 or 3.13 and `git`
