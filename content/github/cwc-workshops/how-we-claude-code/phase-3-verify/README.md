<!-- Copyright 2026 Anthropic PBC -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# Verifiable React

A small Vite + React todo app built around one idea: **every piece of the app
should be trivially verifiable by an AI agent at runtime**, not just by a human
reading code or a test suite running offline.

The design is built on a simple principle: verification is *runtime observation
at the surface* — you run the thing, drive it, read what it actually shows.
Tests and typechecks are CI's job; a verifier's job is to confirm the real
artifact behaves. This app bakes that philosophy into its architecture.

```
bun install
bun run dev          # app on http://localhost:5199
                     # dashboard on http://localhost:5199/verify
bun run verify       # run the full verification matrix headlessly (vitest + jsdom)
bun run typecheck
```

## The six ideas

### 1. The DOM is the machine-readable surface

Every component emits `data-verify-*` attributes describing its state:

```html
<section data-verify-unit="TodoApp" data-verify-total="3"
         data-verify-done="1" data-verify-active="2" data-verify-filter="all">
```

Verifiers and agents read **the DOM contract**, not React internals. That keeps
the surface stable across refactors — you can rewrite the internals freely as
long as the contract holds. See `src/verify/core/contract.ts` and the
`verifyAttrs()` helper.

### 2. Verifiable units declare fixtures + invariants

Each component/feature registers a **VerifiableUnit** (`src/verify/specs/`):

- a **Zod schema** for its props
- **fixtures** — named, reproducible render configurations (with optional
  imperative `act()` steps to drive interaction)
- **invariants** — predicates that must hold over the mounted DOM

Fixtures marked `probe: true` are adversarial edge cases. A unit with zero probe
fixtures has only replayed the happy path.

### 3. Isolated render targets: `/verify/:unit/:fixture`

Every unit × fixture gets a deep-linkable route that mounts *only that unit* in
known state, with no app shell. Append `?chrome=0` for a clean screenshot. An
agent (or Playwright) navigates here, observes, reads the result.

### 4. Pluggable verifiers

Verifiers (`src/verify/verifiers/`) are independent of components. Each one
inspects a mounted unit and returns structured `Check`s:

| verifier | checks |
|---|---|
| `schema` | props match the Zod schema |
| `invariants` | the unit's declared predicates hold |
| `dom-contract` | `data-verify-*` attributes are present and self-identifying |
| `a11y` | buttons named, inputs labeled, images have alt |

Adding a new kind of verification (visual diff, perf budget, i18n) is: add a
file, register it, done. No component changes.

### 5. `window.__verify` — the agent handle

A structured, versioned API for machine consumers:

```js
__verify.manifest()       // every unit × fixture × verifier
__verify.current()        // structured result for what's mounted
await __verify.runAll()   // run the full matrix, return results
```

The dashboard at `/verify` is just a human rendering of the same data. Agent and
human see the same truth.

### 6. One verdict taxonomy, three consumers

`PASS | FAIL | BLOCKED | SKIP`, checks as `ok ✅ | fail ❌ | warn ⚠️ | probe 🔍`.
The same `runFixture()` code path is called by:

- the **dashboard** ("Run all" button → verdict grid)
- the **agent** (`window.__verify.runAll()`)
- **CI** (`bun run verify` → vitest matrix)

`BLOCKED` (couldn't observe) is deliberately distinct from `FAIL` (observed and
wrong). When in doubt, the runner fails — a false PASS ships bugs, a false FAIL
costs one more look.

## File layout

```
src/
  features/todos/          the actual app (emits data-verify-* contracts)
  verify/
    core/
      types.ts             VerifiableUnit, Fixture, Invariant, Verifier, Verdict
      contract.ts          data-verify-* helpers
      registry.ts          central unit & verifier registry
      runner.ts            mount → act → verify → verdict
    verifiers/             pluggable: schema, invariants, dom-contract, a11y
    specs/                 one .verify.ts per unit (the central /verify dir)
    harness/
      handle.ts            window.__verify
      Dashboard.tsx        /verify
      UnitPage.tsx         /verify/:unit/:fixture
      Report.tsx           structured result rendering
    matrix.test.ts         the CI path: run every unit×fixture, assert verdicts
```

## Try it with an agent

1. `bun run dev`
2. Tell an AI agent (or Playwright): "Open `/verify`, run
   `window.__verify.manifest()`, pick a unit, navigate to its route, and
   confirm `window.__verify.current().verdict === 'PASS'`."
3. Break something — e.g. remove `data-verify-total` from `TodoApp.tsx` — and
   watch the `dom-contract` and `counts-add-up` checks fail with a precise
   diagnosis, in the dashboard AND in `bun run verify` AND at
   `window.__verify`.

## Things deliberately demonstrated

- `TodoStats/inconsistent-counts` is a **probe that is DESIGNED to fail** — it
  proves the framework catches lies, not just confirms truths.
- `todos.feature/whitespace-submit` drives the real form with whitespace and
  asserts the count didn't change — a behavioral probe at the feature surface.
- Every unit is required (by `matrix.test.ts`) to have at least one probe
  fixture — you can't ship a unit that only tests the happy path.
