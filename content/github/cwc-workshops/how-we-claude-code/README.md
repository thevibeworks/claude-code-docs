<!-- Copyright 2026 Anthropic PBC -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# How We Claude Code

> **Workshop sample.** Not maintained and not accepting contributions.

A three-phase walkthrough of an AI-assisted product development workflow —
from an open-ended idea, to a written spec, to a set of design explorations,
to a runnable React app whose components are verifiable at runtime.

Phases 1 and 2 ship as **prompts only** (`PROMPT.MD` in each folder) — run
them yourself to reproduce the spec and design explorations. Phase 3 is the
fully built artifact.

## Phases

| Phase | What it is |
|---|---|
| [`phase-1-exploration/`](phase-1-exploration) | An interview-driven brainstorm that produces a product spec for a no-account, link-based bill-splitting app. |
| [`phase-2-planning/`](phase-2-planning) | Four divergent visual design directions for the spec, each rendered as static HTML mockups for side-by-side comparison. |
| [`phase-3-verify/`](phase-3-verify) | A separate Vite + React todo app demonstrating a **verifiable component architecture**: every unit declares fixtures, invariants, and a machine-readable DOM contract that an agent (or CI) can observe at runtime. |

## Running phase 3

```sh
cd phase-3-verify
bun install
bun run dev          # app on http://localhost:5199, dashboard at /verify
bun run verify       # run the verification matrix headlessly
bun run typecheck
```

See [`phase-3-verify/README.md`](phase-3-verify/README.md) for the full design
write-up, and [`phase-3-verify/docs/verification.html`](phase-3-verify/docs/verification.html)
for an in-depth tour of how the verification system works.
