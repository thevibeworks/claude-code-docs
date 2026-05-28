# Morning brief — read this first

Dry run 11am. Everything ran overnight; data's on disk.

## Resource IDs (live in the workshop workspace)

| | id |
|---|---|
| environment | `env_01PSAtKYnL8cp5iFKw19bVyC` |
| 00-naive | `agent_011CakWtiBj8RBnEintfAudo` |
| 01-polish | `agent_011CamBhoctNW8KhhZodJUwT` |
| 02-diagram | `agent_011CamBhqAerHbpN9S4UJvin` |
| 03-qa-loop | `agent_011CamAdtU7Cqinh12FmWizt` |
| 04-model-swap | `agent_011CamAdujX6pjePDccWQytu` |

## Data on disk

- `runs-batch/<round>/<task>/` — all 50 decks, `output.pptx` + `render/slide-*.jpg` + `score.json`
- `runs-batch/SCORECARDS.txt` — full per-task table for every round

## Progression (10-task averages)

| Column | 00 | 01 polish | 02 diagram | 03 qa-loop | 04 model-swap |
|---|---|---|---|---|---|
| emojis | 13.0 | **0** | 0 | 0.4 | 1.8 |
| img% | 0 | 0 | **100** | 100 | 0 |
| jImage | 0.86 | 0.26 | **4.06** | 4.00 | 2.06 |
| shapes>20 | 1.9 | 0.8 | **0** | 0 | 3.6 |
| dense | 4.0 | 4.0 ⚠️ | 3.0 | 2.2 | 4.2 |
| jText | 4.22 | 4.28 | 4.22 | 4.32 | **4.88** |
| jLayout | 4.00 | 3.88 | 4.04 | 4.24 | **4.66** |
| jColor | 4.36 | 4.24 | 4.30 | 4.28 | **4.88** |
| coherence | 4.06 | 4.58 | 4.66 | 4.22 | 3.20 ⚠️ |
| font<14 | 4.1 | 5.0 | 4.0 | 4.5 | 4.3 — never moves, dead metric |

## One line per round

- **R1 polish** — emojis 13→0 clean; `dense` didn't move (grader counts all text, rule said body only). Slide-11 top-left.
- **R2 diagram** — img% 0→100, jImage 0.9→4.1, shapes>20→0. The visible win. Project R0 vs R2 JPGs side by side.
- **R3 qa-loop** — marginal (dense 3.0→2.2, jLayout +0.2). R2 was already clean. The trace is the show, not the scorecard.
- **R4 model-swap** — Opus+naive: highest jText/jLayout/jColor of any round, worst structure (img% 0, shapes>20 3.6, coherence tanks). Different lever, same eval, 5× cost.

## Gotchas

- **Use the `.env` key, not the shell key.** All commands go through `dotenv -o -e .env --` (the `-o` overrides). The npm scripts do this; bare `ant` does NOT — use `npm run ant -- ...`.
- Code structure: `parse-pptx.ts` (parsing) + `graders.ts` (declarative `GRADERS[]`, judge via `client.messages.parse()` + Zod) + `grader.ts` (~170-line harness).

## Uncommitted (presenter-local)

Parallel `--all` in start-session.ts · `dotenv -o` in package.json · stale-render fix in grader.ts · `id:` lines in all YAMLs · `src/batch.ts` (one-off) · the new agent YAMLs `01-polish`/`02-diagram`/`03-qa-loop`/`04-model-swap` · matplotlib in environment.yaml · this file.

## If you only have 30 min

Read WORKSHOP.md Section 3. Then open `runs-batch/00-naive/food/render/` next to `runs-batch/02-diagram/food/render/` in Finder — that's the visual you'll project.
