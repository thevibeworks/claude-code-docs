---
title: Optimizing for cost and intelligence
url: https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence
description: Balance cost and intelligence on the Claude Platform, with measured results for prompt caching, effort, model choice, output caps, and multi-model strategies.
---

The most capable model can be too expensive at scale, and the least expensive model can fall short on quality. The Claude Platform gives you direct control over that tradeoff. You choose the model, the effort level, and the architecture for each request, which lets you place a workload almost anywhere on the cost-to-intelligence frontier.

Cost and intelligence are usually pictured as a frontier where one buys the other. The first group of levers on this page moves a workload toward that frontier by cutting cost without touching quality; only the second group moves along it:

<Frame>
  ![Schematic of the cost-to-intelligence frontier: one arrow cuts spend at the same quality, the other trades quality for cost](https://platform.claude.com/docs/images/cost-intel/frontier.svg)
</Frame>

The levers come in two kinds:

* **Free wins** cut spend without touching quality: prompt caching, token hygiene, a prompt audit against the model you are running, [batch processing](https://platform.claude.com/docs/en/build-with-claude/batch-processing) at 50% off for work that can wait up to 24 hours, and [workspace spend limits](https://platform.claude.com/docs/en/api/rate-limits#setting-lower-limits-for-workspaces) as the backstop.
* **Tradeoffs** exchange cost for intelligence: model choice, effort, output caps and session budgets, an elapsed-time clock, and multi-model architectures.

Each lever comes with measured results and the rule for when it pays. In Anthropic's measurements, prompt caching was usually the largest lever. The multi-model levers are narrower; a second model was measured in two shapes, an advisor and an orchestrator.

## Start here

Match your situation to a row.

| Your situation                                   | Do this                                                                                                                                        | Where                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Any workload, any model                          | Turn on prompt caching and trim unneeded tokens; both are free                                                                                 | [Cache repeated context](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#cache-repeated-context) · [Trim tokens](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#trim-input-and-context-tokens) |
| A person waits between turns                     | Count the gaps between your requests, then pick the cache duration from the table in that section                                              | [Pick the cache duration](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#pick-the-cache-duration)                                                                                                                                           |
| Costs are too high; quality is fine              | Try lower effort on the model you use now                                                                                                      | [Tune effort](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#tune-effort)                                                                                                                                                                   |
| You are not on the latest model                  | Upgrade; in Anthropic's measurements each newer model solved at least as many tasks as the one before it, usually for less per solved task     | [Upgrade the model](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#upgrade-the-model)                                                                                                                                                       |
| You are choosing or switching models             | Compare on cost per completed task, not per token                                                                                              | [Compare models](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#compare-models-on-cost-per-task)                                                                                                                                            |
| High-volume work with outputs you can check      | Try Claude Haiku 5.5 first                                                                                                                     | [Compare models](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#compare-models-on-cost-per-task)                                                                                                                                            |
| Quality isn't good enough                        | If you lowered effort, restore it; otherwise try the next tier up at its default effort                                                        | [Tune effort](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#tune-effort) · [Compare models](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#compare-models-on-cost-per-task)                  |
| Attempts end with `stop_reason: max_tokens`      | Raise `max_tokens` to 64,000: in Anthropic's tests only 2 of about 14,000 turns were longer, and cost per solved task stayed about the same    | [Set budgets](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#set-budgets-and-output-caps)                                                                                                                                                   |
| You can check outputs (tests, a verifier)        | Run at `low` effort and re-run failures at `high`: in Anthropic's tests, about 40% lower cost than everything at `high`, at the same pass rate | [Re-run failures](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#re-run-failures-at-higher-effort)                                                                                                                                          |
| Agent loops with a few very costly runs          | Set a Claude Managed Agents session budget and a workspace spend limit                                                                         | [Set budgets](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#set-budgets-and-output-caps)                                                                                                                                                   |
| You want agent runs to finish sooner             | Tell the model time matters and show it the elapsed time: 7% to 47% less time in Anthropic's tests, for a few points of score                  | [Show the model elapsed time](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#show-the-model-elapsed-time)                                                                                                                                   |
| A lower-cost model stalls only on hard decisions | Try an advisor. It can help only when your model consults it; first price its model alone at low effort and measure the consult rate           | [Advisor strategy](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#advisor-strategy-escalate-hard-decisions)                                                                                                                                 |
| The work exceeds one context window              | Split the work and hand the parts to lower-cost models                                                                                         | [Orchestrator strategy](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#orchestrator-strategy-delegate-bulk-work)                                                                                                                            |

These results are Anthropic-internal ([Benchmarks referenced](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs)) and directional, not guarantees, so measure on your own workload with the [four-step method](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#measure-on-your-own-workload).

## Cut spend without losing quality

Prompt caching, token hygiene, batch processing, and a prompt audit against your current model all lower what you pay without lowering output quality. Two caveats apply: batch processing trades latency for its discount, and context editing, a token-hygiene lever, cost more than it saved on the short run measured in this section and changed nothing on the long one.

### Cache repeated context

#### Why caching comes first

Turn on [prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) before any other lever, because every turn of an agentic task resends the entire growing conversation: system prompt, tool definitions, and every prior turn.

* A 40-turn task sends its first turn 40 times, so task cost grows with roughly the square of turn count.
* Caching does not stop the resending, but each resend costs about a tenth as much (a twentieth on Claude Opus 5.5 and Claude Sonnet 5.5, a fortieth on Claude Fable 5.1 and Claude Mythos 5.1) and processes faster.
* The prefix is billed at the [cache-read rate](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#pricing) instead of the input price, and each turn pays the 1.25x cache-write rate only for what is new.

**What good looks like.**

* Over a full day of real traffic, agent loops read a median 84% of their input from the cache, and the top 10% of them, coding or not, read 94% or more[17](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs).
* Deep in a task, a well-built loop pays full price on under 1% of its input.
* Below about 80%, look for something breaking the cache (see [What breaks the cache](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#what-breaks-the-cache)).

Across Anthropic's measured runs, cache reads are routinely the largest single component of task cost, making caching worth more than most model-choice decisions. Anthropic priced the DeepResearch Bench II[7](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs) runs with and without caching:

<Frame>
  ![Chart, DeepResearch Bench II: caching cuts Fable 5.1 from $37.94 USD to $6.89 USD per task; Sonnet 5, $3.20 USD to $1.18 USD](https://platform.claude.com/docs/images/cost-intel/caching-repriced.svg)
</Frame>

The cache's default lifetime is 5 minutes and an agent loop's turns are seconds apart, so the discount applies to most tokens on every turn. The caching chart's runs read 84% to 90% of their input tokens from the cache.

Pricing other runs' recorded token counts the same way, with each model at its default effort, gives the average token cost per task without caching (none of these runs was made with caching off):

| Benchmark                                                                                                                                                                                                                                                                                                   | Model             | Without caching                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ------------------------------- |
| SWE-bench Pro[3](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs)                                                                                                                                                                                         | Claude Opus 5.5   | 3.3 times the cost with caching |
| SWE-bench Pro                                                                                                                                                                                                                                                                                               | Claude Sonnet 5.5 | 3.1 times the cost with caching |
| Claude Managed Agents task set[25](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs), whose sessions are short                                                                                                                                             | Claude Haiku 5.5  | 1.7 times the cost with caching |
| A small agent that triages bug reports ([Trim input and context tokens](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#trim-input-and-context-tokens))[16](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs) | Claude Sonnet 5.5 | 7.3 times the cost with caching |

The saving varies with how many turns a task takes, because shorter loops re-read less.

<Note>
  On Claude Haiku 5.5, [compact a long session](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#manage-the-context-lifecycle) at a task boundary, before its requests pass 100,000 prompt tokens. A request whose prompt is over 100,000 tokens pays 5 times as much for each of its tokens, output included. Cache reads and cache writes count toward the 100,000 tokens, so a request with a large cached prefix can still be over. See [Long context pricing](https://platform.claude.com/docs/en/about-claude/pricing#long-context-pricing).
</Note>

#### Pick the cache duration

If your loop waits on a person between turns, use the [1-hour cache duration](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#1-hour-cache-duration) once about 1 turn in 20 follows a pause between 5 minutes and an hour and few gaps run over an hour. On Claude Fable 5.1, Claude Opus 5.5, and Claude Sonnet 5.5, keeping the 5-minute cache warm can cost less.

The 1-hour duration costs more to write (2x the input price instead of 1.25x). A miss on either duration bills the whole prefix at the write price instead of the read price.

Anthropic measured a small agent that triages bug reports ([Trim input and context tokens](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#trim-input-and-context-tokens)) with pauses inserted before some turns to simulate a person's delay[16](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs). Accuracy stayed within run-to-run noise at every setting measured. Anthropic also measured extra requests that keep the 5-minute cache warm (keep-alive requests).

To decide, count the gaps between consecutive requests in a conversation, and find your row in the following table:

| Your gaps between requests                                                                                 | Model                                 | Use                                                      |
| ---------------------------------------------------------------------------------------------------------- | ------------------------------------- | -------------------------------------------------------- |
| Turns arrive seconds apart                                                                                 | Any                                   | 5-minute default                                         |
| About 1 gap in 20 or more falls between 5 minutes and an hour, and few gaps run over an hour               | Any                                   | 1-hour duration                                          |
| Gaps over an hour are common: about 60% or more of your pauses longer than 5 minutes also run past an hour | Any                                   | 5-minute default                                         |
| Only 1 or 2 gaps in 20 fall between 5 minutes and an hour, and none lasts more than about half an hour     | Claude Opus 5.5 and Claude Sonnet 5.5 | 5-minute cache kept warm, instead of the 1-hour duration |
| A pause comes before every turn                                                                            | Claude Opus 5.5 and Claude Sonnet 5.5 | 1-hour duration                                          |
| Pauses run for minutes                                                                                     | Claude Fable 5.1                      | 5-minute cache kept warm, instead of the 1-hour duration |
| Pauses run toward an hour                                                                                  | Claude Fable 5.1                      | 1-hour duration                                          |

On Claude Haiku 5.5, use the "Any" rows. Keep-alive requests were not measured on it. By list prices, not by measurement, each one costs twice as much relative to the input price as on Claude Opus 5.5 and Claude Sonnet 5.5: Claude Haiku 5.5 reads the cache at the standard 0.1x, those two at 0.05x.

**Why, row by row.**

* **Any model.**

  * **Turns arrive seconds apart.** No pauses: the default cost about 19% less than the 1-hour setting on Claude Sonnet 5.5, about 15% to 18% less on Claude Opus 5.5.
  * **About 1 gap in 20 or more.** The break-even, worked out from token counts, is about 1 turn in 30 on Claude Sonnet 5.5 and Claude Opus 5.5.
  * **Gaps over an hour are common.** On any model, a gap over an hour expires both durations, and the 1-hour setting then re-writes the prefix at its higher write price.

* **Claude Opus 5.5 and Claude Sonnet 5.5**, whose cache reads cost 0.05x the input price.

  * **Only 1 or 2 gaps in 20.** At default effort, keep-alive requests cost 8% to 13% less than the 1-hour duration on Claude Opus 5.5, 8% to 16% less on Claude Sonnet 5.5.
  * **A pause comes before every turn.** On Claude Opus 5.5 and Claude Sonnet 5.5, keep-alive requests cost a few percent more than the 1-hour duration at 6-minute pauses and over 50% more at 45-minute pauses.

* **Claude Fable 5.1**, whose [cache reads](https://platform.claude.com/docs/en/about-claude/pricing#prompt-caching) cost 0.025x the input price.

  * **Pauses run for minutes.** On Claude Fable 5.1, keep-alive requests[19](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs) cost 13% to 20% less than the 1-hour cache, with 10% of turns paused and with a 6-minute pause before every turn.
  * **Pauses run toward an hour.** On Claude Fable 5.1, only with a 45-minute pause before every turn did the 1-hour cache win, by about $0.12 USD on a session of 5 bug reports.

The following chart plots cost per session against the share of paused turns on Claude Sonnet 5.5:

<Frame>
  ![Line chart: cost per triage session by share of turns after a pause; the 1-hour cache is cheaper past about 1 turn in 30](https://platform.claude.com/docs/images/cost-intel/cache-ttl-sonnet-5-5.svg)
</Frame>

The following chart adds the 5-minute cache kept warm by keep-alive requests, on Claude Fable 5.1, Claude Opus 5.5, and Claude Sonnet 5.5:

<Frame>
  ![Cost charts: keep-alive beats the 1-hour cache on Fable 5.1 where plotted; on Opus 5.5 and Sonnet 5.5 only if few turns pause](https://platform.claude.com/docs/images/cost-intel/cache-keepalive-sonnet-5-5.svg)
</Frame>

**What to know.**

* The 1-in-20 rule leaves a margin over the break-even of about 1 turn in 30. At 1 turn in 20 the 5-minute and the 1-hour setting cost about the same on Claude Sonnet 5.5, within run-to-run variation; at 1 turn in 10 the 5-minute setting cost 54% more (reference 16).
* On models other than Claude Sonnet 5.5 and Claude Opus 5.5, prices put the break-even in the same range: every current model uses the same cache-write multipliers, and every model but Claude Fable 5.1, Claude Mythos 5.1, Claude Opus 5.5, and Claude Sonnet 5.5 the same read price.
* The Claude Opus 5.5 and Claude Sonnet 5.5 keep-alive figures come from requests sent with `max_tokens: 1`. Whether a `max_tokens: 0` request refreshes an existing cache entry was not measured on Claude Opus 5.5 (reference 16).

To keep the cache warm:

1. Take the previous request, set `max_tokens` to 0, and drop `stream` if it was set. Do not change a byte of the prefix.
2. Re-send the request's headers with its body. Without the original request's `anthropic-beta` header, the beta-gated fields in the replayed body are rejected.
3. Send it within 4 minutes of the previous request's start, and every 4 minutes after that, until the next turn arrives or the session ends. Count from the request's start, because the [cache's 5-minute lifetime](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#how-prompt-caching-works) runs from there.

That is the [pre-warming request](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#pre-warming-the-cache): it refreshes the cache's lifetime, returns no output, and costs little more than the cache read. Once the cache has expired, the next request, keep-alive or not, re-writes the prefix at the cache write price[16](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs).

A `max_tokens: 0` request is rejected in the following cases:

* The request sets `thinking.type: "enabled"` (the default adaptive thinking on Claude Fable 5.1 is fine), structured outputs, or a forced tool choice ([its limitations](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#limitations)). On those workloads, buy the 1-hour duration instead.
* The request carries the top-level `compaction` parameter, so don't re-send a compaction request from [compaction on demand](https://platform.claude.com/docs/en/build-with-claude/compaction-on-demand) as a keep-alive request.

<CodeGroup exclude="shell:CLI, python, typescript, csharp, go, java, php, ruby">
  ```bash cURL
  # Within 4 minutes of the last request's start (time spent generating counts
  # against the cache's lifetime), re-send that request with max_tokens set to
  # 0, dropping stream (a max_tokens: 0 request cannot stream). Send the same
  # headers as the original request, including any anthropic-beta header.
  jq '.max_tokens = 0 | del(.stream)' last_request.json | \
    curl https://api.anthropic.com/v1/messages \
      -H "x-api-key: $ANTHROPIC_API_KEY" \
      -H "anthropic-version: 2023-06-01" \
      -H "content-type: application/json" \
      --data-binary @-
  ```
</CodeGroup>

#### Turn on caching

Setup takes little work. [Automatic caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#automatic-caching) places breakpoints for you; otherwise, the [Claude API skill](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/claude-api-skill) that ships with Claude Code can add caching to an existing integration from one prompt:

Let Claude Code add caching for you

```text
/claude-api add prompt caching to this integration
```

On the code that produced these measurements, the skill put one breakpoint on the system block and one on each of the two most recent user turns; [Explicit cache breakpoints](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#explicit-cache-breakpoints) explains where to place them.

#### What breaks the cache

Keep per-request text in the newest user turn, after the last cache breakpoint, and make every cache-invalidating change at a natural break, such as the first request after a compaction. The cache is a byte-exact prefix match over the request in order (tools, then system prompt, then messages), so a change anywhere invalidates everything after it.

The stakes are highest on Claude Fable 5.1 and Claude Mythos 5.1, where a break re-writes the prefix at 1.25x the input price instead of reading it at 0.025x. The following table gives what one broken turn costs on a 100,000-token prefix, computed from list prices with the 5-minute cache, not measured:

| Model                                  | One broken turn | The read instead | Compared with the read |
| -------------------------------------- | --------------- | ---------------- | ---------------------- |
| Claude Fable 5.1 and Claude Mythos 5.1 | $1.25 USD       | $0.025 USD       | 50 times               |
| Claude Opus 5.5                        | $0.50 USD       | $0.02 USD        | 25 times               |
| Claude Sonnet 5.5                      | $0.25 USD       | $0.01 USD        | 25 times               |

On the other current models it costs 12.5 times the read.

**What to do.**

* Put nothing that changes per request, such as a timestamp or a queue position, ahead of the stable prefix: it turns every request into a full cache write. In a measurement on an earlier model, a 25-token status line at the front of the system prompt made a run of a small agent that triages bug reports ([Trim input and context tokens](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#trim-input-and-context-tokens)) cost more than running with caching off[18](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs).
* The [prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#what-invalidates-the-cache) page lists the changes that invalidate the cache, such as a change to [`effort`](https://platform.claude.com/docs/en/build-with-claude/effort), the thinking configuration, the system prompt, or a tool definition. Changing the output format invalidates the cache for that conversation (see [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs#prompt-modification-and-token-costs)).
* On the most recent models, change instructions with a [mid-conversation system message](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages), a `{"role": "system"}` message appended to `messages`, instead of editing the top-level `system` field: the cached prefix stays intact. Check that page for which models support it. A per-message effort change leaves the cached prefix intact too, but on fewer models: [Change effort mid-conversation](https://platform.claude.com/docs/en/build-with-claude/effort#changing-effort-mid-conversation) lists them.
* After a cache-invalidating change, confirm cache reads have not dropped; if they have, [cache diagnostics](https://platform.claude.com/docs/en/build-with-claude/cache-diagnostics) shows where the prefix diverged.

Anthropic measured the timing of a change on an earlier model, on the triage agent's long sessions[18](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs). In that measurement, sessions cost more when an effort change and an added tool were made mid-session, or on the request that triggered the compaction, than when the same two changes were made on the first request after compaction. Accuracy was within run-to-run noise in every case.

The sessions with no changes cost more than the sessions changed after compaction, but not because of caching. They ran at the default effort throughout and two compacted a second time, while the others started at low effort (reference 18):

<Frame>
  ![Bar chart, cost per triage session: $0.81 USD no changes, $0.95 USD mid-session, $0.92 USD at compaction, $0.75 USD after](https://platform.claude.com/docs/images/cost-intel/compaction-timing.svg)
</Frame>

### Trim input and context tokens

Most agent requests carry tokens that never influence the answer. Trimming them rarely costs output quality, although not every lever here saved money when measured. Two places to look:

* **Input trimming.**

  * [Dynamic filtering](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool#dynamic-filtering) in the web fetch tool keeps boilerplate out of fetched pages.
  * [Image resizing](https://platform.claude.com/docs/en/build-with-claude/vision#evaluate-image-size) right-sizes vision inputs.
  * [Tool search with deferred loading](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool) loads tool definitions only when needed (measured later in this section).
  * [Programmatic tool calling](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling) lets Claude run several tool calls from code so only the filtered result enters the context; its documentation reports 24% fewer input tokens on agentic search benchmarks, with a higher score.
  * [Manage tool context](https://platform.claude.com/docs/en/agents-and-tools/tool-use/manage-tool-context) compares tool search, programmatic tool calling, prompt caching, and context editing.

* **Context lifecycle.** [Context editing](https://platform.claude.com/docs/en/build-with-claude/context-editing) clears stale tool results, and [automatic compaction](https://platform.claude.com/docs/en/build-with-claude/compaction-threshold) with its threshold stops long loops from carrying their whole history forward.

The levers interact with the cache and each other, so judge them by net effect, and use [cache diagnostics](https://platform.claude.com/docs/en/build-with-claude/cache-diagnostics) to confirm your cached prefix survives each change.

In measurements on an earlier model[28](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs), Anthropic ran them on an issue-triage agent working through 20 real bug reports with screenshots from a public repository, and on a longer variant of the same job with 2.6 times the tokens. With caching on, input trimming (image resizing and tool search) cut the cost of both runs further.

#### Defer unused tool definitions

Every tool definition attached to a request is input on every turn, and a few MCP servers add up to hundreds of them.

In a measurement on an earlier model[27](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs), Anthropic ran the triage agent with its own two tools plus a catalog of real tool definitions from public MCP servers, for a total of up to 502 tools, loading all of them or marking the extras `defer_loading` behind [tool search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool):

<Frame>
  ![Line chart: with all tools loaded, run cost rises from $0.55 USD to $1.02 USD at 502 tools; tool search keeps it at $0.56 USD](https://platform.claude.com/docs/images/cost-intel/tool-search.svg)
</Frame>

* With every definition loaded, the run cost rose as the catalog grew, tracking the schema tokens on each request.
* With tool search, the run cost stayed flat at every catalog size.
* Accuracy was in the same range either way, and the model never called a wrong tool, so at this scale the catalog costs money, not correctness.
* On the same earlier model, with a public GitHub MCP server attached through the [MCP connector](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector), deferring its toolset (`default_config: {defer_loading: true}`) cut the run cost at the same accuracy.

#### Keep data files out of the prompt

When the model has to compute over a table, upload it with the [Files API](https://platform.claude.com/docs/en/build-with-claude/files) and let the model query it with [code execution](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool) instead of pasting it in. Anthropic asked 25 aggregate questions[15](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs) (sums, filtered counts, group-bys, and a date filter) over a 1,862-row public CSV, with the answers computed by pandas:

<Frame>
  ![Scatter chart: file uploaded with code execution, 25 of 25 correct at $0.40 USD; pasted into the prompt, 7 of 25 at $5.01 USD](https://platform.claude.com/docs/images/cost-intel/data-files.svg)
</Frame>

Pasted into the prompt, the table is about 91,000 input tokens on every request, and Claude Sonnet 5 answered 7 of 25 questions correctly. Uploaded, with code execution, it answered all 25, and the run cost about a twelfth as much. Claude Opus 5 showed the same pattern. Neither approach used prompt caching.

#### Manage the context lifecycle

The context levers only pay on a session long enough to need them:

<Frame>
  ![Bar chart by run length: context editing adds 73% on the short run; compaction saves 32% and pruning 39% on the long](https://platform.claude.com/docs/images/cost-intel/hygiene.svg)
</Frame>

Anthropic measured these levers on an earlier model[28](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs):

* On the 20-issue run the levers saved little or nothing, and context editing made the run cost more.
* On the long run the prune and compaction both cut the cost, while context editing changed nothing.
* The prune is a few lines you write yourself: at each task boundary, replace large stale tool results with a one-line extract.
* The prune caches well because the edits sit at the tail of the conversation, where the next task adds new content anyway.
* Run-wide, the prune and context editing cache about equally well. If you use context editing, [clear in a few large batches](https://platform.claude.com/docs/en/build-with-claude/context-editing#context-editing-and-prompt-caching).

<Note>
  On Claude Fable 5.1, Claude Opus 5.5, Claude Sonnet 5.5, and Claude Haiku 5.5, rewriting an earlier tool result [invalidates every thinking block after it](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#prefix-check), so use compaction instead. The prune was measured on an earlier model without [preserved thinking](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking); on these four models, [context editing](https://platform.claude.com/docs/en/build-with-claude/context-editing) and [compaction](https://platform.claude.com/docs/en/build-with-claude/compaction) run on the server and don't invalidate thinking blocks.
</Note>

The prune, adapted from the triage agent's code:

```python
import re

PRUNED = "[pruned at issue boundary]"


def prune_task_boundary(messages, tool_name_by_id, threshold=2000):
    """Call once per task boundary. Replaces large, stale search results with a one-line extract."""
    for message in messages:
        if message["role"] != "user" or not isinstance(message["content"], list):
            continue
        for block in message["content"]:
            if not (isinstance(block, dict) and block.get("type") == "tool_result"):
                continue
            if tool_name_by_id.get(block.get("tool_use_id")) != "search_issues":
                continue
            result_text = block.get("content")
            if not isinstance(result_text, str) or len(result_text) <= threshold:
                continue
            if result_text.startswith(PRUNED):
                continue  # already pruned on an earlier boundary
            # cap single-line results so the extract stays short
            first_line = result_text.split("\n", 1)[0].strip()[:200]
            refs = re.findall(r"#(\d+)", result_text)[:5]
            extract = f"{PRUNED} {first_line}"
            if refs:
                extract += " kept refs: " + " ".join("#" + r for r in refs)
            block["content"] = extract
```

### Batch work that can wait

Route every request no one is waiting on through the [Batch API](https://platform.claude.com/docs/en/build-with-claude/batch-processing), and keep the interactive path for the rest. The Batch API takes 50% off every token of a request, including cached ones, in exchange for results arriving any time within 24 hours.

* Batching is the second-largest free lever after caching for unattended agent work: evaluation runs, backfills, and scheduled jobs such as a recurring run of the issue-triage agent from the [token-trimming measurement](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#trim-input-and-context-tokens).
* Batching combines with everything on this page except interactivity, but is not available for Claude Managed Agents sessions, which are interactive by design (see [Claude Managed Agents pricing](https://platform.claude.com/docs/en/about-claude/pricing#claude-managed-agents-pricing)).

### Audit prompts against the current model

Audit prompts against the model you run now, and again whenever you change models: it is a free win.

* Each model generation responds to prompts differently, so a prompt accumulates text written for a model you no longer use.
* The usual case is over-specific instruction added to compensate for an older model: "verify twice," "be maximally thorough," a mandatory step-by-step procedure, or a hand-rolled reasoning scratchpad.
* A newer model follows such instructions to the letter, producing extra tool rounds and extra writing, so the bill goes up with no gain in accuracy.

The audit is one command. The [Claude API skill](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/claude-api-skill) that ships with Claude Code has a `prompt-audit` command that reads a project's prompts and request code and reports what was written for a different model:

Let Claude Code audit your prompts for you

```text
/claude-api prompt-audit
```

This shortened excerpt shows the command run against a support-desk prompt and request code containing those patterns:

```text wrap
$ claude
> /claude-api prompt-audit

10 findings. The three that matter most:

1. budget_tokens returns a 400 on Opus 5 (support_agent.py:10). This code
   does not run against its own target model. Everything else here is
   quality; this one is an outage.
2. The prompt contains two live contradictions. Line 15 says confirm before
   every refund, line 17 says process every eligible refund immediately.
   Line 19 asks for a complete recap *and* a three-sentence maximum.
3. The reasoning scaffold and the 6-step script fight the model rather than
   steer it. <scratchpad> + "reason step by step" is now a request
   parameter, not prose; the mandatory 6-step procedure plus "investigate
   fully even when the ticket looks simple" forces four tool calls on a
   "where's my package" ticket.
...
-After any refund or escalation, verify twice before submitting: re-fetch
-the order, re-check every figure in your reply against the fresh lookup,
-and review the reply a second time for errors.
+Before submitting a refund or an escalation, re-fetch the order and confirm
+every figure in your reply matches the fresh lookup.
```

The command then proposes its edits as a diff (one hunk shown) and lists what it deliberately left alone: the refund window, the tone requirement, and the quality bar. You review a patch, not a rewrite.

Anthropic measured the effect on a support-desk evaluation[14](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs), across two migrations between earlier models:

<Frame>
  ![Scatter chart, support-desk evaluation: the old prompt costs more on the new model; audited, it is cheaper and as accurate](https://platform.claude.com/docs/images/cost-intel/prompt-audit.svg)
</Frame>

* From Claude Opus 4.8 to Claude Opus 5, prompts written for the older model cost more per ticket on the newer model, for no change in accuracy.
* Running the audit over the same prompts made Claude Opus 5 both cheaper than the unaudited version and more accurate, a gain outside the noise.
* From Claude Sonnet 4.6 to Claude Sonnet 5, the audit cut the cost per ticket at the same accuracy.

The two kinds of stale text have different costs:

<Frame>
  ![Bar charts per legacy pattern: over-obeyed instructions cost money; broken settings and contradictory rules cost accuracy](https://platform.claude.com/docs/images/cost-intel/prompt-audit-patterns.svg)
</Frame>

* Instructions the new model follows too literally cost money: removing "verify twice" cut Claude Opus 5's cost per ticket, and removing "be maximally thorough" cut it almost as much.
* Text that no longer fits the model costs accuracy instead: a retired thinking setting, contradictory rules, and a hand-rolled scratchpad that conflicts with the model's own thinking each restored accuracy on Claude Opus 5 when removed.

The same patterns tend to appear in tool descriptions and skills, which are worth auditing too.

## Trade cost against intelligence

These levers set where a single model sits between cost and intelligence: model choice, effort, re-running failures at a higher setting, the budgets and caps it works within, and whether it can see how much time has passed. If you are a model or two behind, upgrade first ([Upgrade the model](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#upgrade-the-model)); otherwise, start with an effort sweep on your current model ([Tune effort](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#tune-effort)). From lowest to highest cost and capability, the current models are Claude Haiku 5.5, Claude Sonnet 5.5, Claude Opus 5.5, and Claude Fable 5.1 (the frontier model); [Models overview](https://platform.claude.com/docs/en/models/overview) has the full lineup and prices.

### Compare models on cost per task

Compare models on cost per completed task, not per token, because you pay for completed tasks. For most agent workloads, start with Claude Opus 5.5 at its default effort (`medium`).

A more capable model can finish a task with less work, which can offset much of the per-token premium. Anthropic measured this on the SWE-bench Pro[3](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs) subset, whose scores are not comparable to the public leaderboard, priced as a customer is billed:

<Frame>
  ![Scatter chart, SWE-bench Pro: Claude Opus 5.5 at low effort matches Sonnet 5.5's default for about 7% more per solved task](https://platform.claude.com/docs/images/cost-intel/cost-per-task-sonnet-5-5.svg)
</Frame>

The following table lists the results:

| Benchmark                                                                                                                                       | Model             | Effort             | Score                                                                             | Cost                                                                                                    |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ------------------ | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| SWE-bench Pro[3](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs) subset                      | Claude Sonnet 5.5 | `high` (default)   | 87.6% of tasks solved                                                             | $0.11 USD per solved task                                                                               |
| SWE-bench Pro subset                                                                                                                            | Claude Opus 5.5   | `low`              | 87.4% of tasks solved                                                             | $0.12 USD per solved task                                                                               |
| SWE-bench Pro subset                                                                                                                            | Claude Opus 5.5   | `medium` (default) | 92.8% of tasks solved                                                             | $0.22 USD per solved task                                                                               |
| SWE-bench Pro subset                                                                                                                            | Claude Fable 5.1  | `high` (default)   | 92.3% of tasks solved (a single run)                                              | $1.19 USD per solved task                                                                               |
| Internal agentic-coding benchmark[11](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs)        | Claude Opus 5.5   | `medium` (default) | 86.6%                                                                             | $0.84 USD per attempt                                                                                   |
| Internal agentic-coding benchmark                                                                                                               | Claude Fable 5.1  | `medium`           | 84.2% (a single run)                                                              | $2.68 USD per attempt                                                                                   |
| GPQA Diamond[9](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs)                              | Claude Haiku 5.5  | `medium` (default) | 85% accuracy, compared with 91% for each of Claude Opus 5.5 and Claude Sonnet 5.5 | About a twentieth of Claude Opus 5.5's cost per correct answer and about a tenth of Claude Sonnet 5.5's |
| Claude Managed Agents task set[25](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs), 79 tasks | Claude Haiku 5.5  | `medium`           | 93% of attempts passed (a single run)                                             | About $0.011 USD per passed attempt                                                                     |

**What to do.**

* Start with Claude Opus 5.5 at its default effort: on the SWE-bench Pro subset it matched Claude Fable 5.1 at its default, inside run-to-run noise, for about a fifth of the cost per solved task. Opus 5.5 and Fable 5.1 both largely saturate the SWE-bench Pro subset. Use Claude Fable 5.1 for demanding reasoning and long-horizon agentic work, or when your evals on Claude Opus 5.5 at higher effort still fall short.
* At the other end, Claude Haiku 5.5 suits high-volume and latency-sensitive work with checkable outputs.
* Price every candidate in cost per completed task on your own traffic, including Claude Opus 5.5 at its default effort and the frontier model at reduced effort. Each of Claude Opus 5.5's token prices, cache reads included, is twice Claude Sonnet 5.5's, but on the SWE-bench Pro subset Opus 5.5 at `low` solved about the same share of tasks as Sonnet 5.5 at its default, inside run-to-run noise, for about 7% more per solved task.
* The ranking flips by workload, and no price list tells you which way, so measure it on your own workload. On long research loops, Claude Fable 5.1 can do more work, not less, and so cost more per task (DeepResearch Bench II[7](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs)).
* Price the tail of your workload, not the median: compare models on the hardest tenth of your tasks, not the typical one.

The bill is decided by the tasks the cheaper model fails, because a failed task still bills its tokens, then the retry, then whatever the failure costs downstream. The tail is also where the money goes even when nothing fails. On a 20-problem WideSearch[1](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs) run, two problems carried 43% of the spend:

<Frame>
  ![Bar chart of 20 WideSearch problems ranked by cost: the top two carry 43% of spend and the cheapest half 10%](https://platform.claude.com/docs/images/cost-intel/tail.svg)
</Frame>

The [multi-model strategies](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#combine-models) exist to spend frontier intelligence on that tail without paying frontier rates for the rest.

### Upgrade the model

If you are a model or two behind, the cheapest lever is the model string. In Anthropic's measurements, each newer model solved at least as many tasks as the one before it, usually for less per solved task. The chart plots recent Claude models on the SWE-bench Pro[3](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs) subset, where every model ran through the same test setup, and on Terminal-Bench 3[20](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs); the table lists what each upgrade changed:

<Frame>
  ![Charts: on SWE-bench Pro, Opus 5.5 and Sonnet 5.5 cut cost per solved task most; on Terminal-Bench 3, Opus drops to $28 USD](https://platform.claude.com/docs/images/cost-intel/upgrade-ladder-sonnet-5-5.svg)
</Frame>

| Benchmark                                                                                                                             | Upgrade                              | Effort                                  | Score                                                             | Cost                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ | --------------------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| SWE-bench Pro[3](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs) subset            | Claude Sonnet 4.6 to Claude Sonnet 5 | Default                                 | 5 more points                                                     | 16% less per solved task                                                                         |
| SWE-bench Pro subset                                                                                                                  | Claude Sonnet 5 to Claude Sonnet 5.5 | Default                                 | About 10 more points                                              | 87% less per solved task; 85% less at Claude Sonnet 5's prices                                   |
| SWE-bench Pro subset                                                                                                                  | Claude Opus 5 to Claude Opus 5.5     | Default: `high` to `medium`             | About the same: 91.9% to 92.8% of tasks solved                    | 78% less per solved task; about 69% less at Claude Opus 5's prices                               |
| SWE-bench Pro subset                                                                                                                  | Claude Fable 5 to Claude Fable 5.1   | Default                                 | About the same score                                              | 43% less per solved task                                                                         |
| DeepResearch Bench II[7](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs)           | Claude Fable 5 to Claude Fable 5.1   | `high`                                  | 2 to 3 more points on the 21 tasks where no attempt was cut short | 46% more per task on all 50 tasks                                                                |
| DeepResearch Bench II                                                                                                                 | Claude Fable 5 to Claude Fable 5.1   | `low`                                   | 2 to 3 more points on the 21 tasks where no attempt was cut short | 94% more per task on all 50 tasks                                                                |
| Terminal-Bench 3[20](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs)               | Claude Opus 4.7 to Claude Opus 4.8   | `high`                                  | From 7% to 15% of tasks solved                                    | From $183 USD to $63 USD per solved task                                                         |
| Terminal-Bench 3                                                                                                                      | Claude Opus 4.8 to Claude Opus 5     | `high`                                  | From 15% to 41% of tasks solved                                   | From $63 USD to $28 USD per solved task, a 56% saving                                            |
| Claude Managed Agents task set[25](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs) | Claude Haiku 4.5 to Claude Haiku 5.5 | As served; `medium` on Claude Haiku 5.5 | From 62% to 93% of attempts passed, one run per model             | From $0.041 USD to about $0.010 USD in token cost per attempt; about 84% less per passed attempt |

**When it pays.**

* Where older models already solve most tasks, the cost of each attempt decides the saving: on the SWE-bench Pro subset, Claude Opus 5.5 scores about the same as Claude Opus 5 for 78% less per solved task.
* Where older models mostly fail, the pass rate decides the saving: on Terminal-Bench 3[20](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs), the upgrade from Claude Opus 4.8 to Claude Opus 5 raises tasks solved from 15% to 41% and costs 56% less per solved task.
* Measure the upgrade on your own workload before assuming it saves. The saving is not guaranteed: on DeepResearch Bench II[7](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs), Claude Fable 5.1 costs more per task than Claude Fable 5 because the new model does more work per task there, although the input and output prices are the same and the cache read is 4x cheaper.
* Compare on cost per solved task, not per token: the same text costs about 30% more tokens on Claude 4.7 and later models, so a per-token comparison makes the newer models look more expensive by construction.

### Tune effort

Sweep effort on your own workload before you add a second model. Lower effort costs less and is often faster, and how much accuracy it gives up depends on the task: on long-horizon coding, effort bought accuracy, and on research tasks it bought a lot in one measurement and nothing in another. The [`effort`](https://platform.claude.com/docs/en/build-with-claude/effort) parameter governs how much thinking, tool calling, and self-verification the model does; `high` is the default on most models, and `medium` on Claude Opus 5.5 and Claude Haiku 5.5.

The following table lists Anthropic's measurements on two benchmarks with current models; scores and costs are not comparable between the two benchmarks. Costs are per task, not per solved task as in [Compare models on cost per task](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#compare-models-on-cost-per-task). Each score pools two runs on SWE-bench Pro and three on DeepResearch Bench II, unless its cell says otherwise:

| Benchmark                                                                                                                   | Model            | Effort             | Score                                | Cost per task |
| --------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------ | ------------------------------------ | ------------- |
| SWE-bench Pro[3](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs) subset  | Claude Opus 5.5  | `low`              | 87.4% of tasks solved                | $0.11 USD     |
| SWE-bench Pro subset                                                                                                        | Claude Opus 5.5  | `medium` (default) | 92.8% of tasks solved                | $0.21 USD     |
| SWE-bench Pro subset                                                                                                        | Claude Opus 5.5  | `high`             | 95.3% of tasks solved                | $0.29 USD     |
| SWE-bench Pro subset                                                                                                        | Claude Opus 5.5  | `xhigh`            | 96.7% of tasks solved (a single run) | $0.74 USD     |
| DeepResearch Bench II[7](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs) | Claude Fable 5.1 | `low`              | Rubric score 66%                     | $4.48 USD     |
| DeepResearch Bench II                                                                                                       | Claude Fable 5.1 | `high` (default)   | Rubric score 65%                     | $6.89 USD     |

The following chart plots accuracy against cost per task for Claude Opus 5.5 on the SWE-bench Pro[3](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs) subset:

<Frame>
  ![Line chart of accuracy against cost per task by effort: steep from low to high for Claude Opus 5.5 on SWE-bench Pro](https://platform.claude.com/docs/images/cost-intel/effort-sweep-opus-5-5-swe-bench-pro.svg)
</Frame>

The following chart plots rubric score against cost per task for Claude Fable 5.1 on DeepResearch Bench II[7](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs):

<Frame>
  ![Line chart, DeepResearch Bench II, rubric score against cost per task: on Fable 5.1 higher effort bought no score, only cost](https://platform.claude.com/docs/images/cost-intel/effort-limit-repriced.svg)
</Frame>

**What to do.**

* Sweep two or three effort levels on a sample of your own traffic, each in a separate session: changing top-level effort mid-session [invalidates the cache](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#cache-repeated-context) and distorts the comparison. The curve is the baseline any multi-model strategy must beat ([step 2 of measuring on your own workload](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#measure-on-your-own-workload)).
* On long-horizon coding, effort is a real tradeoff, which [re-running failures at higher effort](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#re-run-failures-at-higher-effort) turns back into a saving. At `medium`, Claude Sonnet 5.5 scored about 7 points lower than at its default, `high`, on the SWE-bench Pro[3](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs) subset for about 59% of the cost per task (2 runs each), and scored 62.7% compared with 77.8% on the internal agentic-coding benchmark[11](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs) (1 attempt per task).
* At `xhigh` and `max`, Claude Sonnet 5.5 can start its own rounds of review after it finishes a task, which takes more time and tokens. To keep that work on the task, add the prompt under "Thoroughness at `xhigh` and `max` effort" in [Prompting Claude Sonnet 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5#steer-initiative-and-scope) to your system prompt.
* On research tasks, measure the model you ship. Claude Fable 5.1 scored nearly the same from `low` to `high` on DeepResearch Bench II; Claude Opus 5.5 scored 13.3 points lower at `low` than at `medium` on DRACO[21](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs). The two results come from different models on different benchmarks, so they show that the answer varies, not why.
* At `low`, Claude Opus 5.5's typical task took 84% less time than at `medium` on DRACO[21](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs), 30% less on HLE[22](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs), and 47% less on an internal set of physics problems[23](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs), and it scored 13.3, 3.4, and 14.0 points lower (3, 3, and 4 attempts per task).
* On an internal defect-search benchmark for work larger than one context window[8](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs), Claude Fable 5.1 took 15.2, 17.5, and 19.9 hours per run at `low`, `medium`, and `high` (3 runs each). To save time, also compare lower effort with the two changes in [Show the model elapsed time](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#show-the-model-elapsed-time): `low` effort saved more time, and the changes kept more of the score.

### Re-run failures at higher effort

When a task's outcome is checkable, the cheapest policy on the effort curve is not a fixed setting: run every task at a low setting and re-run only the failures at a higher one.

Anthropic computed this policy task by task from the Claude Opus 5.5 effort runs on the SWE-bench Pro[3](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs) subset in [Tune effort](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#tune-effort):

<Frame>
  ![Chart, SWE-bench Pro, Opus 5.5: low or medium effort with failures re-run at high matches any fixed effort for less than high](https://platform.claude.com/docs/images/cost-intel/escalation-opus-5-5.svg)
</Frame>

In the following table, the re-run costs count the failed cheap attempts:

| Policy                              | Tasks solved | Cost per task   |
| ----------------------------------- | ------------ | --------------- |
| `low`, failures re-run at `high`    | About 97%    | About $0.17 USD |
| `medium`, failures re-run at `high` | About 97%    | About $0.24 USD |
| Everything at `high`                | 95.3%        | $0.29 USD       |

* At `low`, 13% of tasks failed. With those re-run at `high`, the pass rate was slightly higher than with everything at `high`, for a little over half the cost.
* Use this policy for the saving, not the lift. Most of the small lift is the second attempt: re-running the failures of one `high` run at `high` scores about the same, for more money.

Two conditions apply. First, you need a failure signal (here, the benchmark's own tests); a checker that passes bad work lets those failures through. Second, every first-pass failure takes two runs' worth of wall-clock time, so the saving is paid for in latency on the failures.

### Set budgets and output caps

Two controls do two different jobs: a session budget caps what one Claude Managed Agents session can spend, and `max_tokens` caps the length of one response. Set each where it applies, with a [workspace spend limit](https://platform.claude.com/docs/en/api/rate-limits#setting-lower-limits-for-workspaces) as the final backstop.

* **Session budgets on Claude Managed Agents** are a hard stop on spend. A [session budget](https://platform.claude.com/docs/en/managed-agents/budgets) is a dollar cap on one session's [list cost](https://platform.claude.com/docs/en/managed-agents/budgets#how-list-cost-is-measured), which the platform meters for tokens, web searches, and session running time.
* At the cap, or a fraction past it, the session pauses with `stop_reason: budget_reached`; raising the budget resumes it. It is platform-enforced and works on any model with a list price. Deployments apply the same budget to each session they start.
* **`max_tokens`** caps a single response, invisibly to the model, so lowering it does not make the model economize. The turns that needed the room are discarded and still billed. Retrying capped attempts rarely helps: at the same cap most of them fail again, and at a higher one you also pay for the wasted attempt.
* Set `max_tokens` to 64,000 for agentic work, or to 128,000, the maximum, when a single cut-off attempt is costly. [Stream responses](https://platform.claude.com/docs/en/build-with-claude/streaming) that large, treat [`stop_reason: max_tokens`](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons#max-tokens) as a failure, and save money with effort, which the model can see.

The following table shows what each model solved and what a solved task cost at each cap on an internal repository-task benchmark[12](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs), one attempt per task, each model at its default effort. The rows at 16,384 average two runs, and the other rows are one run each:

| Model            | `max_tokens` | Attempts ended by the cap | Tasks solved | Cost per solved task     |
| ---------------- | ------------ | ------------------------- | ------------ | ------------------------ |
| Claude Opus 5.5  | 16,384       | 25%                       | 57.6%        | $5.38 USD at list prices |
| Claude Opus 5.5  | 64,000       | 0%                        | 75.6%        | $5.38 USD at list prices |
| Claude Opus 5.5  | 128,000      | 0%                        | 68.9%        | $5.94 USD at list prices |
| Claude Fable 5.1 | 16,384       | 43%                       | 36.3%        | $21.37 USD as billed     |
| Claude Fable 5.1 | 64,000       | 0%                        | 58.5%        | $21.53 USD as billed     |
| Claude Fable 5.1 | 128,000      | 1%                        | 60.0%        | $21.74 USD as billed     |

**Claude Opus 5.5 at 64,000 and 128,000:** No attempt was cut off at either cap, so the cap does not explain why these two rows differ in tasks solved or in cost per solved task. Each row is one run.

Compare the caps within each model. The two models were run a month apart, and their costs are priced on different bases.

On the internal repository tasks[12](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs), almost every turn finishes far below a 16,384-token cap. The rare long turn is what a higher cap buys:

<Frame>
  ![Dot plot of per-turn output for Opus 5.5 and Fable 5.1: medians a few hundred tokens, longest 61k and 128k, against the caps](https://platform.claude.com/docs/images/cost-intel/max-tokens-ladder-opus-5-5.svg)
</Frame>

Ask for shorter answers. Output tokens cost five times input tokens on Claude Haiku 5.5, Claude Sonnet 5.5, Claude Opus 5.5, and Claude Fable 5.1, and in an agent loop every token the model writes comes back as input on every later turn, so you pay for a long answer again and again.

In a measurement on an earlier model[26](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs), Anthropic ran a small agent that triages bug reports ([Trim input and context tokens](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#trim-input-and-context-tokens)) under three final-answer instructions, three runs each, with the same model and tools:

* The original asked for two lines.
* The shorter variant asked for one.
* The longer variant asked for a memo with six headed sections.

The following chart plots the cost per run of each format:

<Frame>
  ![Bar chart: one-line format $0.49 USD per run, original two-line format $0.57 USD, memo $1.40 USD, all 78% to 85% correct](https://platform.claude.com/docs/images/cost-intel/output-format.svg)
</Frame>

All three scored within run-to-run noise of each other against the correct labels, so the formats differ in what you pay far more than in what they get right. Ask for the answer you will read, not the one that looks thorough.

### Show the model elapsed time

To make an agent finish sooner and cost less, tell it that time matters, and show it the elapsed time on every request. In Anthropic's measurement, the two changes cut the time of a single Claude Opus 5.5 agent at `medium` effort by 47% and its cost by 60% on the typical (median) DRACO[21](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs) research task, and its average score was 4.1 points lower.

On HLE[22](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs) and an internal physics set[23](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs), the typical task took 14% and 7% less time, and the physics score was 3.0 points lower. Lowering effort to `low` saved more time and cost than the changes did, and lost more score (reference 21). Check the score on your own tasks before you adopt the changes.

For working code, see the Claude Cookbook recipe [Multi-agent teams under latency pressure and budgets](https://github.com/anthropics/claude-cookbooks/blob/main/patterns/agents/latency_multi_agent.ipynb), which applies both changes to a team of agents. To say that time matters in the system prompt instead, see [Time signals for multiagent harnesses](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5#time-signals-for-multi-agent-harnesses).

The following chart also plots a team, whose lead agent rarely started helpers, and a single agent at `low` effort:

<Frame caption="With both changes, a single agent took 47% less time on the typical DRACO task, and its average score was 4.1 points lower.">
  ![Scatter and bar charts, DRACO, HLE, and the physics set: the changes save the most time on DRACO, for a few points of score](https://platform.claude.com/docs/images/cost-intel/time-awareness.svg)
</Frame>

## Combine models

Tune one model before you add a second: sweep effort on your current model first, because most workloads end there, and if the sweep shows a gap, price the stronger model alone at low effort. Build a pairing only if it beats the single model's whole curve of score against spend. The multi-model results on this page were judged against the same model at lower effort and against the next model down running alone, which is the comparison to run on your own workload.

The following table compares the two strategies:

| Strategy         | Control flow                                          | Frontier model's role               | Fits                                                                                                                      | Frontier cost scales with             |
| ---------------- | ----------------------------------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| **Advisor**      | Smaller model runs the loop, escalates on demand      | Consulted for plans and corrections | Serial work that is hard in spots, such as a coding agent's many turns between a few real decisions                       | How often the executor gets stuck     |
| **Orchestrator** | Frontier model runs the loop, delegates the bulk work | Plans, dispatches, and synthesizes  | Work that fans out across genuinely independent files, documents, or cases, especially more than one context window of it | How hard the pieces are to coordinate |

### Advisor strategy: escalate hard decisions

An advisor can help only when the executor consults it.

In Anthropic's measurements on current models, the one pairing whose executor consulted often, on a coding benchmark, scored 1.7 points higher than the executor alone at the same effort, at the edge of run-to-run noise, for about 2.1 times the cost. Where the executor rarely or never consulted, the pairing scored within run-to-run noise of the executor alone, or lower.

To turn it on, add the [advisor tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool), a beta feature, to your request. On Claude Managed Agents, [give the session an advisor](https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration#give-the-session-an-advisor). For Claude Code, see [escalating hard decisions with the advisor tool](https://code.claude.com/docs/en/advisor).

<Frame>
  ![Diagram of the advisor strategy: an executor model runs the main loop and calls a Claude Fable 5.1 advisor on demand](https://platform.claude.com/docs/images/model-routing-advisor-strategy.svg)
</Frame>

The following table compares each pairing with its executor alone at the same effort:

| Benchmark                                                                                                                                | Score                                                                      | Cost                                                                       | Advisor consulted                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Internal agentic-coding benchmark[11](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs) | 90.1%, 1.7 points over the executor alone, at the edge of run-to-run noise | $2.92 USD per attempt, about 2.1 times the executor alone                  | About 1.4 times per attempt; 4% of attempts received no advice                           |
| GPQA Diamond[9](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs)                       | Within run-to-run noise of the executor alone                              | 12% more per question for Claude Haiku 5.5, 25% more for Claude Sonnet 5.5 | On none of the 198 questions, in two runs each; no system prompt asked for consultations |
| Chartography[13](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs)                      | 61.7, 7 points below the executor alone and beyond run-to-run noise        | About the same as the executor alone                                       | On 1 of 300 tasks                                                                        |

* **Internal agentic-coding benchmark.** Claude Opus 5.5 at `high`, with a Claude Fable 5.1 advisor.
* **GPQA Diamond.** Claude Haiku 5.5 or Claude Sonnet 5.5 at each model's default (`medium` and `high`), with a Claude Opus 5.5 advisor.
* **Chartography.** Claude Opus 5.5 at `low`, with a Claude Fable 5.1 advisor.

The advisor can only hand over capability the executor lacks: on GPQA Diamond, Claude Sonnet 5.5 alone tied Claude Opus 5.5 alone at 91% with refusals counted as wrong, but only because Opus 5.5 refused six biology questions per run compared with Sonnet 5.5's one. On the questions each answered, Opus 5.5 led by about 2 points.

On the coding benchmark, the pairing's gain is at the edge of run-to-run noise, and it lands about on Claude Opus 5.5's own effort curve, so the advisor bought about what more effort does. The following chart plots the pairing against that curve and Claude Fable 5.1's from August:

<Frame>
  ![Coding benchmark: Opus 5.5 at high with a Fable 5.1 advisor gains 1.7 points for 2.1 times the cost, near its effort curve](https://platform.claude.com/docs/images/cost-intel/internal-coding-advisor-opus-5-5.svg)
</Frame>

**What to do.**

* Measure the consult rate on your own tasks. The advisor tool's definition, about 1,000 prompt tokens per request, adds cost even when the executor never consults. With [prompt caching](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#cache-repeated-context), a multi-turn agent loop pays for the definition at the cache-read price after the first request, so this overhead matters most for short, single-request tasks.
* If the executor rarely consults, see [Prompting for coding and agent tasks](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool#prompting-for-coding-and-agent-tasks) for system prompts that ask for consultations, and measure again after you add one. On 20 SWE-bench Pro[3](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs) problems, the suggested prompt made no clear difference for Claude Sonnet 5.5.
* Restore the executor's effort if the consult rate collapses. In measurements on earlier models, one pairing that consulted on most tasks at the default effort consulted on few when effort was lowered, and then scored below the executor alone at its default effort (SWE-bench Pro[3](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs)).
* Recheck at every model release, because releases move both the capability gap and the price ratio.

### Orchestrator strategy: delegate bulk work

Delegation saved money in only two situations, in measurements with workers on Claude Sonnet 5, an earlier model:

* Routine work with a long cost tail (an easy slice of BrowseComp[4](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs))
* Work larger than one context window (an internal defect-search benchmark[8](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs))

When the work is one dependent chain, or fits in a single context without a long cost tail, the orchestrator's model alone at lower effort came out ahead in every case measured, also on earlier models (the harder BrowseComp set and DeepWideSearch[6](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs)); independent external work reports the same pattern[5](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs).

To build an orchestrator, use [multiagent orchestration](https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration) in Claude Managed Agents: configure an orchestrator agent and worker agents that it can call, each with its own model.

<Frame>
  ![Diagram of the orchestrator strategy: a frontier model fans subtasks out to three lower-cost worker models](https://platform.claude.com/docs/images/model-routing-orchestrator-strategy.svg)
</Frame>

The [Model selection matrix](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model#model-selection-matrix) lists Claude Haiku 5.5 for sub-agent tasks; before you use it as a worker, [measure it on your own workload](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#measure-on-your-own-workload).

The following chart plots the defect-search benchmark's configurations by cost and score:

<Frame>
  ![Chart, defect-search benchmark: the orchestrator costs about half of Fable 5.1 alone at any effort and scores 10 to 12 points below](https://platform.claude.com/docs/images/cost-intel/corpus-pareto.svg)
</Frame>

**What to do.**

* **Routine work with a long cost tail:** measure this case first, for accuracy as well as cost. The measurement behind it covers only problems that the delegated configuration answered correctly in every run (reference 4).
* **Work larger than one context window:** delegate partitions to workers. Lowering effort cannot help, because the bill is the reading itself: on the defect-search benchmark[8](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs), Claude Fable 5.1 alone cost $468 USD to $552 USD per run across its three effort settings and took 15 to 20 hours. With earlier-model workers, delegation cost less and finished sooner, for a lower score.

## Measure on your own workload

Measure on your own workload: the numbers on this page reflect list prices at the time of measurement and will drift as models and prices change, and your escalation rate, how cleanly tasks split, and transcript length move them too. The method stays the same:

1. Pull a few tasks from production logs, weighted like real traffic, and [write outcome checks](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests) for each: tests pass, ticket closed, row count correct. Record cost per task beside the score.
2. Baseline the model tiers across effort levels, not only the default, and plot score against spend. A multi-model configuration must beat the single model's whole curve.
3. If the curve shows a gap effort can't close, add the multi-model strategy that fits and re-run the suite.
4. Run the winner in shadow on a traffic slice before cutover, then keep the suite running.

**How to price a task.** Each response's `usage` has five priced token counts. Price each at its own rate: uncached input, 5-minute and 1-hour cache writes at 1.25x and 2x the input price, cache reads, and output. Sum them across the task's requests (the [Usage and Cost API](https://platform.claude.com/docs/en/manage-claude/usage-cost-api) reports the aggregate). On Claude Haiku 5.5, price each request at the rates for its prompt length, counting cache reads and writes (see [Long context pricing](https://platform.claude.com/docs/en/about-claude/pricing#long-context-pricing)).

The following example computes one request's cost at Claude Opus 5.5's list prices. Change the three prices for another model:

<CodeGroup exclude="shell:cURL, shell:CLI">
  <CodeGroupItem language="cURL">
    This calculation needs more logic than a single shell command. Use the [Claude SDK](https://platform.claude.com/docs/en/cli-sdks-libraries/overview) to run it.
  </CodeGroupItem>

  <CodeGroupItem language="CLI">
    This calculation needs more logic than a single shell command. Use the [Claude SDK](https://platform.claude.com/docs/en/cli-sdks-libraries/overview) to run it.
  </CodeGroupItem>

  ```python Python
  INPUT_PER_MTOK = 4.00  # Claude Opus 5.5
  # 0.05x the input price on Claude Opus 5.5; the multiplier differs by model
  CACHE_READ_PER_MTOK = 0.20
  OUTPUT_PER_MTOK = 20.00

  client = anthropic.Anthropic()
  response = client.messages.create(
      model="claude-opus-5-5",
      max_tokens=1024,
      messages=[{"role": "user", "content": "Hello, Claude"}],
  )
  usage = response.usage
  cache_writes = usage.cache_creation
  writes_1h = cache_writes.ephemeral_1h_input_tokens if cache_writes else 0
  writes_5m = cache_writes.ephemeral_5m_input_tokens if cache_writes else 0
  cost = (
      usage.input_tokens * INPUT_PER_MTOK
      # 1-hour cache writes bill at 2x the input price, 5-minute at 1.25x; reads at the cache-read price.
      + writes_1h * INPUT_PER_MTOK * 2.0
      + writes_5m * INPUT_PER_MTOK * 1.25
      + (usage.cache_read_input_tokens or 0) * CACHE_READ_PER_MTOK
      + usage.output_tokens * OUTPUT_PER_MTOK
  ) / 1_000_000
  print(f"Request cost: ${cost:.6f}")
  ```

  ```typescript TypeScript
  const INPUT_PER_MTOK = 4.0; // Claude Opus 5.5
  const CACHE_READ_PER_MTOK = 0.2; // 0.05x the input price on Claude Opus 5.5; the multiplier differs by model
  const OUTPUT_PER_MTOK = 20.0;

  const client = new Anthropic();
  const response = await client.messages.create({
    model: "claude-opus-5-5",
    max_tokens: 1024,
    messages: [{ role: "user", content: "Hello, Claude" }]
  });
  const usage = response.usage;
  const cost =
    (usage.input_tokens * INPUT_PER_MTOK +
      (usage.cache_creation?.ephemeral_1h_input_tokens ?? 0) * INPUT_PER_MTOK * 2 + // 1-hour cache write
      (usage.cache_creation?.ephemeral_5m_input_tokens ?? 0) * INPUT_PER_MTOK * 1.25 + // 5-minute cache write
      (usage.cache_read_input_tokens ?? 0) * CACHE_READ_PER_MTOK + // cache read
      usage.output_tokens * OUTPUT_PER_MTOK) /
    1_000_000;
  console.log(`Request cost: $${cost.toFixed(6)}`);
  ```

  ```csharp C#
  const double InputPerMtok = 4.00; // Claude Opus 5.5
  const double CacheReadPerMtok = 0.20; // 0.05x the input price on Claude Opus 5.5; the multiplier differs by model
  const double OutputPerMtok = 20.00;

  AnthropicClient client = new();
  var response = await client.Messages.Create(
      new MessageCreateParams
      {
          Model = Model.ClaudeOpus5_5,
          MaxTokens = 1024,
          Messages = [new UserMessageParam { Content = "Hello, Claude" }],
      }
  );
  var usage = response.Usage;
  double cost =
      (
          usage.InputTokens * InputPerMtok
          + (usage.CacheCreation?.Ephemeral1hInputTokens ?? 0) * InputPerMtok * 2.00 // 1-hour cache write
          + (usage.CacheCreation?.Ephemeral5mInputTokens ?? 0) * InputPerMtok * 1.25 // 5-minute cache write
          + (usage.CacheReadInputTokens ?? 0) * CacheReadPerMtok // cache read
          + usage.OutputTokens * OutputPerMtok
      ) / 1_000_000;
  Console.WriteLine($"Request cost: ${cost:F6}");
  ```

  ```go Go
  const (
  	inputPerMTok     = 4.00 // Claude Opus 5.5
  	cacheReadPerMTok = 0.20 // 0.05x the input price on Claude Opus 5.5; the multiplier differs by model
  	outputPerMTok    = 20.00
  )

  // ...
  	client := anthropic.NewClient()

  	response, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
  		Model:     anthropic.ModelClaudeOpus5_5,
  		MaxTokens: 1024,
  		Messages: []anthropic.MessageParam{
  			anthropic.NewUserMessage(anthropic.NewTextBlock("Hello, Claude")),
  		},
  	})
  	if err != nil {
  		log.Fatal(err)
  	}

  	usage := response.Usage
  	cost := (float64(usage.InputTokens)*inputPerMTok +
  		float64(usage.CacheCreation.Ephemeral1hInputTokens)*inputPerMTok*2.00 + // 1-hour cache write
  		float64(usage.CacheCreation.Ephemeral5mInputTokens)*inputPerMTok*1.25 + // 5-minute cache write
  		float64(usage.CacheReadInputTokens)*cacheReadPerMTok + // cache read
  		float64(usage.OutputTokens)*outputPerMTok) / 1_000_000
  	fmt.Printf("Request cost: $%.6f\n", cost)
  ```

  ```java Java
  static final double INPUT_PER_MTOK = 4.00; // Claude Opus 5.5
  static final double CACHE_READ_PER_MTOK = 0.20; // 0.05x the input price on Claude Opus 5.5; the multiplier differs by model
  static final double OUTPUT_PER_MTOK = 20.00;

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      Message response = client.messages().create(MessageCreateParams.builder()
          .model(Model.CLAUDE_OPUS_5_5)
          .maxTokens(1024)
          .addUserMessage("Hello, Claude")
          .build());

      Usage usage = response.usage();
      long writes1h = usage.cacheCreation().map(CacheCreation::ephemeral1hInputTokens).orElse(0L);
      long writes5m = usage.cacheCreation().map(CacheCreation::ephemeral5mInputTokens).orElse(0L);
      double cost = (usage.inputTokens() * INPUT_PER_MTOK
          + writes1h * INPUT_PER_MTOK * 2.00 // 1-hour cache write
          + writes5m * INPUT_PER_MTOK * 1.25 // 5-minute cache write
          + usage.cacheReadInputTokens().orElse(0L) * CACHE_READ_PER_MTOK // cache read
          + usage.outputTokens() * OUTPUT_PER_MTOK) / 1_000_000;
      IO.println("Request cost: $%.6f".formatted(cost));
  }
  ```

  ```php PHP
  const INPUT_PER_MTOK = 4.00; // Claude Opus 5.5
  const CACHE_READ_PER_MTOK = 0.20; // 0.05x the input price on Claude Opus 5.5; the multiplier differs by model
  const OUTPUT_PER_MTOK = 20.00;

  $client = new Client();
  $response = $client->messages->create(
      model: 'claude-opus-5-5',
      maxTokens: 1024,
      messages: [['role' => 'user', 'content' => 'Hello, Claude']],
  );
  $usage = $response->usage;
  $cost = (
      $usage->inputTokens * INPUT_PER_MTOK
      + ($usage->cacheCreation?->ephemeral1hInputTokens ?? 0) * INPUT_PER_MTOK * 2.00 // 1-hour cache write
      + ($usage->cacheCreation?->ephemeral5mInputTokens ?? 0) * INPUT_PER_MTOK * 1.25 // 5-minute cache write
      + ($usage->cacheReadInputTokens ?? 0) * CACHE_READ_PER_MTOK // cache read
      + $usage->outputTokens * OUTPUT_PER_MTOK
  ) / 1_000_000;
  printf("Request cost: \$%.6f\n", $cost);
  ```

  ```ruby Ruby
  INPUT_PER_MTOK = 4.00 # Claude Opus 5.5
  CACHE_READ_PER_MTOK = 0.20 # 0.05x the input price on Claude Opus 5.5; the multiplier differs by model
  OUTPUT_PER_MTOK = 20.00

  client = Anthropic::Client.new
  response = client.messages.create(
    model: Anthropic::Model::CLAUDE_OPUS_5_5,
    max_tokens: 1024,
    messages: [{ role: "user", content: "Hello, Claude" }]
  )
  usage = response.usage
  cost = (
    usage.input_tokens * INPUT_PER_MTOK +
    usage.cache_creation&.ephemeral_1h_input_tokens.to_i * INPUT_PER_MTOK * 2.00 + # 1-hour cache write
    usage.cache_creation&.ephemeral_5m_input_tokens.to_i * INPUT_PER_MTOK * 1.25 + # 5-minute cache write
    usage.cache_read_input_tokens.to_i * CACHE_READ_PER_MTOK + # cache read
    usage.output_tokens * OUTPUT_PER_MTOK
  ) / 1_000_000
  puts format("Request cost: $%.6f", cost)
  ```
</CodeGroup>

**What to check.**

* **Cache-read share.** In agent loops most input tokens should be cache reads. If `cache_read_input_tokens` is small next to `input_tokens` plus `cache_creation_input_tokens`, check that caching is engaged and that the prefix stays the same between requests.
* **Advisor tool and compaction.** When the [advisor tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool#usage-and-billing) or [compaction](https://platform.claude.com/docs/en/build-with-claude/compaction-threshold#understanding-usage) is enabled, some tokens are reported only in `usage.iterations` and not in the top-level totals. Sum over `usage.iterations` instead, and price `advisor_message` entries at the advisor model's rates.

The following table lists the levers in the order to try them. The figures are from Anthropic's own tests; each linked section and its references give the model and the method:

| Lever                                       | Saving in Anthropic's tests                                                                                                   | Quality cost                                                                       | Latency                                                                                                                          | Where                                                                                                                                                                           |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Prompt caching                              | Cost cut by a factor of 2.7 to 5.5 on a research agent, and by 83% to 86% on a small triage agent                             | None                                                                               | Faster                                                                                                                           | [Cache repeated context](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#cache-repeated-context)                                   |
| 1-hour cache duration                       | With 1 turn in 10 after a pause, the 5-minute default cost 54% more; with 1 in 20, about the same                             | None                                                                               | Stayed warm after a pause[16](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs) | [Pick the cache duration](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#pick-the-cache-duration)                                 |
| Input trimming                              | A further 21% to 26% off a small triage agent's bill                                                                          | None                                                                               | Neutral                                                                                                                          | [Trim input and context tokens](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#trim-input-and-context-tokens)                     |
| Prune stale tool results at task boundaries | 39% on a long agent task; nothing on short ones. On the models named in that section, use compaction instead                  | None measured                                                                      | Neutral                                                                                                                          | [Manage the context lifecycle](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#manage-the-context-lifecycle)                       |
| Tool search                                 | 45% with 500 tool definitions attached; 20% from deferring a GitHub MCP server's toolset                                      | None                                                                               | Neutral                                                                                                                          | [Trim input and context tokens](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#trim-input-and-context-tokens)                     |
| Data files through code execution           | 92% on a data task of 25 questions, with prompt caching off                                                                   | A gain: 25 of 25 correct instead of 7                                              | Faster                                                                                                                           | [Trim input and context tokens](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#trim-input-and-context-tokens)                     |
| Batch API                                   | 50%                                                                                                                           | None                                                                               | Results within 24 hours                                                                                                          | [Batch work that can wait](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#batch-work-that-can-wait)                               |
| Prompt audit against the current model      | 14% on both model upgrades tested                                                                                             | None; a gain on one                                                                | Faster (fewer tool rounds)                                                                                                       | [Audit prompts against the current model](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#audit-prompts-against-the-current-model) |
| Upgrade the model                           | Usually less per solved task: up to 87% less on a coding benchmark                                                            | None; a gain on most                                                               | Neutral                                                                                                                          | [Upgrade the model](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#upgrade-the-model)                                             |
| Lower effort                                | On long coding tasks, `medium` cost about 30% to 52% less than `high`, and `low` about two thirds less                        | Up to 15 points lower, depending on the task; none on one research agent           | Faster                                                                                                                           | [Tune effort](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#tune-effort)                                                         |
| Re-run failures                             | About 40% less than running everything at `high`, at the same pass rate or slightly better                                    | None                                                                               | A second attempt on the tasks that fail                                                                                          | [Re-run failures at higher effort](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#re-run-failures-at-higher-effort)               |
| Ask for shorter answers                     | About 13% less, from 39% fewer output tokens                                                                                  | None                                                                               | Faster                                                                                                                           | [Set budgets and output caps](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#set-budgets-and-output-caps)                         |
| Raising `max_tokens`                        | None: cost per solved task stayed about the same                                                                              | A gain: up to 22 points more tasks solved on one coding benchmark; none on another | Neutral                                                                                                                          | [Set budgets and output caps](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#set-budgets-and-output-caps)                         |
| Advisor                                     | None: about 2.1 times the cost of the model alone, on a coding benchmark                                                      | On coding, a small gain that may be chance; on chart reading, a loss               | About 1.4 extra calls per attempt, on coding                                                                                     | [Advisor strategy](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#advisor-strategy-escalate-hard-decisions)                       |
| Orchestrator                                | About half the cost of the orchestrator's model alone, on work larger than one context window; on routine work, measure first | 10 to 12 points lower on that work                                                 | Much faster on that work                                                                                                         | [Orchestrator strategy](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#orchestrator-strategy-delegate-bulk-work)                  |

### Automate the search with the Claude API skill

Run the [Claude API skill](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/claude-api-skill)'s `cost-optimize` command before you search for savings. It profiles where your tokens go and applies the levers in order, caching first:

Let Claude Code find savings for you

```text
/claude-api cost-optimize
```

Then run the `hillclimb` command in the directory that holds your evaluation:

Let Claude Code run the search for you

```text
/claude-api hillclimb
```

Anthropic measured the first lever of `cost-optimize` and two searches on tau2-bench retail[24](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs), all on earlier models. The cache breakpoints that `cost-optimize` produced cut cost per task, and the pass rate fell by less than the spread of identical runs.

A search found a cheaper configuration by lowering effort and moving down a model tier. Its pass rate stayed inside the band set before the search by a fraction of a task, and ended below the stricter floor the search used for its own verdicts. A second search, started from the lower-cost model at its default effort, kept nothing. Reference 24 has the figures and what each search cost to run.

The following chart plots every step of the first search:

<Frame caption="One search on earlier models, step by step. The effort and model changes produced the savings; the prompt edits brought no durable gain.">
  ![Scatter chart, tau2-bench retail: each search step from Claude Opus 5; Sonnet 5 at low is 61% cheaper within 2 points](https://platform.claude.com/docs/images/cost-intel/hillclimb.svg)
</Frame>

Two settings determine whether you can trust the search's answer:

* **Hold out a split the search never reads.** The search judges adoption there, so confirmation catches a change that fits only the tasks the search saw, as it did the prompt edits (reference 24).
* **Repeat the baseline before the first change.** Identical runs of one starting configuration differed by several tasks in these measurements (reference 24). The repeats give the search's adoption gate a noise bar.

## Benchmarks referenced

Except where a reference says otherwise, measurements are Anthropic-internal runs of these benchmarks. Unless noted, costs are USD at the list prices in effect when each benchmark ran; Claude Sonnet 5 figures use $2 USD and $10 USD per million input and output tokens. Claude Sonnet 5.5 figures from the September 24, 2026, runs use the same input and output prices and its current cache-read price, $0.10 USD per million tokens, rather than its launch price of $0.20 USD, applied to each run's recorded token counts. Those runs used a pre-release build of Claude Sonnet 5.5, and no attempt in them was answered by a fallback model. Charts labeled "notional USD" price each request's token counts at those rates rather than reporting invoices.

1. **WideSearch:** Wong et al., "WideSearch: Benchmarking Agentic Broad Info-Seeking," arXiv:2508.07999, 2025. Broad web-research tasks graded on a many-row table's completeness and accuracy; 200 problems, 3 runs per configuration, run August 1 to 2, 2026. With Claude Fable 5 on this benchmark, DeepWideSearch (reference 6), BrowseComp (reference 4), and GDPval (reference 2), `low` effort gave up 1 to 3 points for a third to a half off the cost per task, `medium` matched the default's accuracy at about 70% to 87% of its cost, and the default bought nothing measurable over `medium` on any of the four. The cost-concentration chart is a separate 20-problem run, 3 runs per problem, run August 3 to 4, 2026, costed from per-request billing records. It covers 59 of the 60 runs. The sixtieth, billed $10.91 USD of the $432.31 USD total, has no cost recorded with its result and is not included.

2. **GDPval:** OpenAI, "GDPval: Evaluating AI Model Performance on Real-World Economically Valuable Tasks," 2025. Knowledge-work deliverables graded against task rubrics; a 210-task run of the released gold set, one attempt per task, run August 2, 2026. A Claude model grades, so absolute scores may differ from published results.

3. **SWE-bench Pro:** Scale AI, "SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?", 2025.

   * **What was measured:** A 482-problem subset selected for compatibility with Anthropic's evaluation harness; scores are not comparable to the public leaderboard. They are also not comparable to the SWE-bench Pro results in the Claude Opus 5.5 system card, which come from runs at `max` effort on a different problem set.
   * **How priced:** Costs on this subset are priced as a customer's organization is metered: each request's prior prompt as a cache read and its new tokens as a 5-minute cache write, from the runs' own usage records, checked against a customer ledger.
   * **Claude Opus 5.5 runs:** Claude Opus 5.5 figures average two runs at `low`, `medium` (its default), and `high`, and use one run at `xhigh`, all run September 19 to 20, 2026, with the same 16,384-token cap per turn as the August Claude Opus 5 runs; the cap cut off 2 `xhigh` attempts and none at other settings. Measured against `high`, Claude Opus 5.5 scored about 2.5 points lower at its default, `medium`, for about 70% of the cost per task, and about 8 points lower at `low` for about a third of the cost; `xhigh` scored about 1.4 points higher for 2.5 times the cost of `high`. The ratios come from unrounded costs.
   * **The 478 problems:** The Opus 5.5 runs used a version of the benchmark whose grading containers can reach only internal package mirrors. That version drops one problem whose test needs a live website, and on three more the reference solution fails there, so Opus 5.5 comparisons, and the Claude Fable 5.1 figures set beside them, use the remaining 478 problems.
   * **Claude Sonnet 5.5 runs:** Claude Sonnet 5.5 ran the same version of the benchmark: two runs at its default, `high`, and two at `medium`, all on September 24, 2026, with the same 16,384-token cap per turn, which cut off none of its attempts. Its figures use the 478 problems, and so do the Claude Sonnet 5 figures set beside them, counted over those problems from their August runs.
   * **Claude Opus 5 runs:** The Claude Opus 5 SWE-bench Pro figures in [Upgrade the model](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#upgrade-the-model) and in this reference average two runs at its default effort and use one run at `low`, all run August 4, 2026.
   * **Advisor, Claude Sonnet 5 pairings:** The Claude Sonnet 5 executor pairings with a Claude Opus 5 advisor behind the consult-rate examples in [Advisor strategy](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#advisor-strategy-escalate-hard-decisions) ran on this subset through the same test setup: the pairing at the default effort was run twice (August 7 and August 8, 2026, a run and an exact replication), the low-effort pairing once (August 8, 2026), and, ten days later, Claude Sonnet 5 alone twice at its default effort (77.4%, the baseline for both pairings).
   * **Advisor, Claude Sonnet 5.5 consult check:** The Claude Sonnet 5.5 consult check cited in [Advisor strategy](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#advisor-strategy-escalate-hard-decisions) ran one attempt on each of 20 of the 478 problems, on September 24, 2026, with a Claude Opus 5.5 advisor through the advisor tool. Four configurations ran: `high` and `xhigh`, each with and without the advisor tool documentation's suggested system prompt for coding tasks. At its default effort, `high`, Claude Sonnet 5.5 did not consult the advisor on any of the 20 problems, with or without the prompt. At `xhigh`, it consulted on 3 of the 20 problems without the prompt and 4 with it, each time on its attempts with the most turns.
   * **Escalation figures:** Escalation figures come task by task from the Opus 5.5 runs: `low` first, then `high` on its failures, solved 96.4% to 97.5% across run pairings for about $0.17 USD; `medium` first, 96.0% to 97.1% for about $0.24 USD; `high` re-run on its own failures, 96.9% for $0.31 USD; everything at `high`, 94.8% to 95.8% for $0.29 USD.
   * **Compare models:** The Claude Fable 5.1 figure in [Compare models](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#compare-models-on-cost-per-task) comes from one run on the same subset at the default effort, run August 26, 2026: counted over the 478 problems, it solved 92.3% for $1.19 USD per solved task. That section's chart and its Claude Opus 5.5 and Claude Sonnet 5.5 figures pool the two runs at each setting plotted, all counted over the 478 problems: Claude Opus 5.5 at `low`, `medium`, and `high`, and Claude Sonnet 5.5 at `medium` and `high`.
   * **Compare models, work per task:** In those figures, Claude Opus 5.5 at `low` did less work on each task than Claude Sonnet 5.5 at its default: a little over half of Sonnet 5.5's output tokens and a little over a third of its cache reads. At their defaults, Opus 5.5 at `medium` solved about 5 percentage points more than Sonnet 5.5 for about twice the cost. At that setting it did slightly more work per task than Sonnet 5.5.
   * **Upgrade the model, runs:** The Claude Fable 5 point in Upgrade the model pools three runs at the default effort, run August 26, 2026, priced as a customer's organization is metered. The upgrade ladder counts every model over the 478 problems, each at its shipped defaults. It uses one run per model except Opus 5, Opus 5.5, Sonnet 5, and Sonnet 5.5 (two runs each) and Fable 5 (the three runs described above). The Opus 4.7, Opus 4.8, Sonnet 4.6, and Sonnet 5 runs ran August 17 to 19, 2026, and the Opus 5 runs on August 4, all in one harness and organization; the Opus 5.5 and Sonnet 5.5 runs are the ones described earlier in this reference.
   * **Upgrade the model, cost per solved task:** Claude Opus 5 costs 21% more per solved task than Claude Opus 4.8 when those Claude Opus 5 runs are compared with one Claude Opus 4.8 run at its shipped defaults from the August 17 to 19 series, counted over the same 478 problems; the chart's SWE-bench Pro panel shows neither Claude Opus 4.7 nor Claude Opus 4.8. In the same measurements, priced as a customer is billed, Claude Opus 5 solves 12 more points of tasks than Claude Opus 4.8 at that 21% more per solved task, Claude Opus 4.8 solves the same share of tasks as Claude Opus 4.7 for 14% less per solved task, and Claude Opus 5 at `low` effort beats Claude Opus 4.8's default on this benchmark for about 30% of its cost per solved task.
   * **Upgrade the model, prices:** Claude Sonnet 5's saving over Claude Sonnet 4.6 in Upgrade the model comes from its lower per-token price, which more than offsets the extra tokens it uses per task. Claude Sonnet 5.5 charges the same as Claude Sonnet 5 for everything but cache reads, which cost half as much. Claude Opus 5.5's token prices are lower than Claude Opus 5's, most of all for cache reads. Like Claude Sonnet 5, the frontier tier gained through price: most of Claude Fable 5.1's saving is the lower cache-read price.
   * **Cost without caching, priced from recorded token counts:** Anthropic also re-priced the recorded token counts of the Claude Opus 5.5 and Claude Sonnet 5.5 runs described earlier in this reference, over the 478 problems, for the caching factors in [Why caching comes first](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#why-caching-comes-first); it made no run with caching off.
   * **The factors, by model:** Each factor is the token cost with every input token at the input price, output tokens unchanged, divided by the cost priced as a customer's organization is metered: for Claude Opus 5.5, 3.3 at `medium`, 2.4 at `low`, 3.8 at `high`, and 5.4 at `xhigh` (one run); for Claude Sonnet 5.5, with cache reads at $0.10 USD per million tokens, 3.1 at `high` and 2.4 at `medium`, or 2.8 at `high` at the launch price of $0.20 USD. Unlike the caching chart's runs, these incurred no web-search fees, and a task's first request is priced as a cache write.

4. **BrowseComp:** Wei et al., "BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents," OpenAI, 2025. Effort figures use a 500-problem cut, one to three runs per setting, run August 3, 2026, with the default point pooling two runs from July 26 to 27, 2026. The measurement of routine work with a long cost tail in [Orchestrator strategy](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#orchestrator-strategy-delegate-bulk-work) uses 10 problems that the model reliably solved on its own when the protocol was fixed, from a 26-problem slice, 50 delegated runs (5 per problem; August 1 to 2, 2026) and 70 runs of the model alone (50 from August 2 to 3, 2026; 20 archived from July 12 to 13 and August 1, 2026), $6.45 USD compared with $11.99 USD per run in expectation; delegated figures carry a measurement band of about 20%. The 10 problems are those on which the delegated configuration, a Claude Fable 5 orchestrator with one Claude Sonnet 5 worker, was right in all 5 runs and Claude Fable 5 alone in both archived runs; the delegated runs are those same runs, and only Claude Fable 5 alone was run again on the ten. Over its 70 runs, archived and new, Claude Fable 5 alone was right in 68. On those problems the delegated configuration cost about half as much as Claude Fable 5 alone on average (the $6.45 USD and $11.99 USD given earlier) and about a third as much at the 90th percentile ($12 USD compared with $33 USD per run), and its most expensive run cost $42 USD compared with $84 USD; that $84 USD run was also wrong. On the full, harder BrowseComp set, Claude Fable 5 alone reached the accuracy of the orchestrator configuration measured on that set at 22% to 30% lower cost.

5. **Agent-architecture scaling:** Kim et al., "Towards a Science of Scaling Agent Systems," arXiv:2512.08296, 2025. Independent external study, cited only for the direction of the finding on when delegation does not pay, not for any figure.

6. **DeepWideSearch:** "DeepWideSearch: Benchmarking Depth and Width in Agentic Information Seeking," arXiv:2510.20168, 2025. The 220 questions span 15 domains, each combining many-row collection with multi-hop retrieval; measured on the benchmark's standing row set, 3 runs per configuration, run August 2, 2026 (the single-worker team point ran July 26 to 27, 2026). With Claude Fable 5, `low` effort matched an orchestrator with a Claude Sonnet 5 worker at 29% lower cost, and took 4.5 minutes per problem, compared with 7.9 minutes at the default.

7. **DeepResearch Bench II:** Li et al., "DeepResearch Bench II: Diagnosing Deep Research Agents via Rubrics from Expert Report," arXiv:2601.08536, 2026.

   * **What was measured:** Its 132 research tasks across 22 domains are graded against expert-derived binary rubrics. Measured on a 50-task subset stratified across all themes, one attempt per task, 3 runs per setting, on [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview) with the platform's own web search and fetch tools (August 26 to 27, 2026).
   * **How scored:** Scored on the 33 tasks no configuration refused, with attempts the production safety classifiers cut short removed. Claude Opus 4.6 judges under the benchmark's rubric protocol; the original uses a different judge, and an Anthropic judge may favor the house style.
   * **Scores:** Scores are each model's mean on the 33-task basis with its own pre-empted tasks removed; on the 21 of the 33 tasks where no configuration had an attempt cut short, Claude Fable 5.1 holds a 2-to-3-point lead over Claude Fable 5 at every effort level and both models are flat across effort.
   * **How priced:** Costs are priced as a customer's organization is metered: each request's prior prompt as a cache read and its new tokens as a 5-minute cache write, a session's first request keeping the cache read it got, from the runs' own usage records, plus the platform's web-search fees. Each cost per task is a 50-task run's cost divided by 50, with the attempts that were cut short included, averaged over the three runs.
   * **Results, Claude Fable 5:** Claude Fable 5 cost $2.30 USD per task at `low` and $4.71 USD at `high`, priced the same way; the percentages in [Upgrade the model](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#upgrade-the-model) come from unrounded costs.
   * **Results, Claude Opus 5:** Claude Opus 5 at its default effort ran on the same surface and subset, three runs, on August 28, 2026: 68.8% on the raw 50 tasks, 70.8% on the 33-task basis, and 71.1% on the 21-task set, at $6.28 USD per task ($23.72 USD without caching); none of its attempts was cut short by the safety classifiers, under a safeguards deployment newer than the one the other models ran under.
   * **Compare models:** The research comparison in [Compare models](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#compare-models-on-cost-per-task) rests on these figures: Claude Fable 5.1 at `low` scored 10 points above Claude Sonnet 5 on the 33-task basis (66% against 56%) at about four times the cost per task over all 50 tasks ($4.48 USD against $1.18 USD); Claude Opus 5 at its default, whose scores and cost are given earlier in this reference, scored above Claude Fable 5.1 at its default, which scored 65% on the 33-task basis and cost $6.89 USD per task over all 50 tasks, so on research, Claude Fable 5.1 earns its price only at `low`.
   * **Caching chart:** The caching chart re-prices the same requests with every input token at the uncached rate.
   * **Not measured:** Claude Sonnet 5.5 was not measured on this benchmark.

8. **Corpus defect sweep:** Anthropic-internal, for work larger than one context window: a 21.6-million-token corpus from 14 public Python package sources with 130 planted defects and deterministic grading; protocol fixed before the runs and internally reviewed; three runs per configuration. Every configuration ran on Claude Managed Agents. The charted team configuration is one in which the Claude Fable 5.1 orchestrator ran the whole sweep inside the platform at its documented limit of 25 concurrent Claude Sonnet 5 workers, run August 30, 2026; its three runs scored F1 0.764, 0.825, and 0.791 after the extras audit (raw 0.751, 0.821, and 0.781) for $225 USD, $234 USD, and $283 USD. The team configuration cost about half as much as Claude Fable 5.1 alone at `low`, `medium`, or `high` (47% to 55% less), scored 10 to 12 points below it, and took about 2.3 hours per run, compared with 15 to 20 hours. The team configuration read about 560 million cached tokens per run, nearly all of them at Claude Sonnet 5's cache-read rate. That is about one and a half times the roughly 365 million that Claude Fable 5.1 read alone. Claude Fable 5.1 alone at `high` effort still holds peak accuracy, at about 2.2 times the team configuration's cost, so delegation here buys most of the accuracy, not all of it. The configuration with Claude Sonnet 5 alone ran August 3 to 4, 2026; the configurations with Claude Fable 5.1 alone ran August 24 to 25, 2026, under the platform's launch serving settings, three seeds per effort setting, on the same corpus build. The sandbox image carried installed copies of part of the corpus, and Claude Fable 5.1's final assembly step compared against them in 7 of 9 runs; re-grading without those additions moved the affected seeds by up to 3 points. Absolute F1 is specific to this corpus build, not comparable across benchmarks; configuration comparisons are like for like.

9. **GPQA Diamond:** Rein et al., "GPQA: A Graduate-Level Google-Proof Q\&A Benchmark," 2023. The 198-question Diamond subset, model-graded against reference answers, advisor tokens metered per request. Claude Haiku 5.5 and Claude Sonnet 5.5, each alone and with a Claude Opus 5.5 advisor, and Claude Opus 5.5 alone ran two runs per configuration on October 7, 2026, all with [server-side fallback](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#server-side-fallback) off, at each model's default effort, and with refusals counted as wrong. A platform safety check refused one biology question per run on Claude Haiku 5.5 and Claude Sonnet 5.5 alone, one in two runs on Haiku 5.5 with the advisor, none on Sonnet 5.5 with the advisor, and six per run on Opus 5.5, which scored 91% with them counted as wrong and 93.5% on the questions it answered. Claude Haiku 5.5 alone scored 85%, 6 points below Opus 5.5. The advisor configurations added the tool without a prompt asking for consultations, and neither executor called the advisor on any question. The pairings scored 0.5 points (Claude Haiku 5.5) and 1.0 points (Claude Sonnet 5.5) above the executor alone, both within run-to-run noise.

10. **DeepSWE:** Datacurve, "DeepSWE: Measuring Frontier Coding Agents on Original, Long-Horizon Engineering Tasks," arXiv:2607.07946, 2026. The set has 113 original tasks across five languages with program-based verifiers. Pairings are two runs each, run August 7, 2026, with advisor tokens metered per request, and used a client-side advisor loop rather than the advisor tool, with identical accounting. Single-model effort sweeps are single runs priced from token counts, a cache-aware approximation. Costs per task are run totals divided by 113. On this benchmark a low-effort Claude Sonnet 5 executor with an advisor scored 23 points above the same executor alone.

11. **Internal agentic-coding benchmark:**

    * **What was measured:** Anthropic-internal: 370 repository tasks graded by the repositories' own tests. The API figures were measured with a plain API agent and a 128,000-token output cap, one run per configuration: Opus 5 alone at the default effort August 9 to 10, 2026, and at `low` and `medium` August 10, 2026; Claude Fable 5.1 alone at five explicitly set effort values August 20, 2026 (the chart shows three of them); and the pairing August 24 to 25, 2026.
    * **August runs:** The August runs had five attempts per task for the pairing and the Claude Opus 5 control and one for the other points.
    * **How priced:** Costs are per attempt. Costs are priced as a customer's organization is metered: each agent-loop request's prior prompt as a cache read and its new tokens as a 5-minute cache write, from the runs' own usage records, and each advisor call, which uses no cache, from its recorded tokens, all at list prices.
    * **Claude Opus 5.5 alone:** Claude Opus 5.5 alone ran on all 370 tasks, September 19 to 20, 2026: at its default effort (`medium`) and at `high` with five attempts per task, and at `low` and `xhigh` with one (369 of 370 scored at each, after a setup-check failure). Claude Opus 5.5 alone solved 74.8% of attempts at `low` for $0.35 USD per attempt, 86.6% at `medium` for $0.84 USD, 88.4% at `high` for $1.38 USD, and 91.1% at `xhigh` for $4.11 USD.
    * **Claude Opus 5.5 with a Claude Fable 5.1 advisor, runs:** The Claude Opus 5.5 executor at `high` with the released Claude Fable 5.1 as advisor (the August runs used a pre-release snapshot) ran five attempts per task on the same dates; one task failed its setup check, so 1,845 attempts were scored. The 279 attempts in which the advisor was turned away under load were re-run, and attempts whose consults timed out were kept, as in August.
    * **Claude Fable 5.1 alone:** For comparison, the released Claude Fable 5.1 alone at `high`, its default, scored 85.7% (317 of 370 tasks), one attempt per task on October 7, 2026.
    * **Consultations:** The August pairing averaged about two advisor consultations per attempt; the Claude Opus 5.5 pairing requested 1.39 and received 1.35.
    * **Claude Opus 5.5 with a Claude Fable 5.1 advisor, results:** The Claude Opus 5.5 pairing scored 90.1% at $2.92 USD per attempt: compared with Claude Opus 5.5 at its default, `medium`, that is 3.5 points for about 3.5 times the money. The latency cost is the consultations themselves: about one or two extra frontier-model calls per task, each on the task's critical path. With the Claude Opus 5.5 executor, the advice saved almost no executor cost: $1.36 USD per attempt compared with $1.38 USD for Claude Opus 5.5 alone at `high`, while the consultations cost $1.55 USD.
    * **August pairing:** In August, with a Claude Opus 5 executor and a Claude Fable 5.1 advisor, the executor spent $1.26 USD less per attempt than Claude Opus 5 alone at its default, and the consultations cost $2.47 USD, so that saving paid for about half of the advice. That August pairing was the most accurate configuration measured at the time, at $6.21 USD per attempt.
    * **Claude Sonnet 5.5 alone, runs:** Claude Sonnet 5.5 alone ran on all 370 tasks on September 24, 2026, at its default effort (`high`) and at `medium`, one attempt per task, with the same 128,000-token output cap, which cut off none of its attempts. All 370 were scored at `medium`, and 369 of 370 at `high`, after a setup-check failure. Its costs are priced as a customer's organization is metered.
    * **Claude Sonnet 5.5 alone, results:** With no advisor, Claude Sonnet 5.5 scored 77.8% at its default, `high`, for $0.33 USD per attempt, about 9 points below Claude Opus 5.5 at its default for about two fifths of the cost; at `medium`, it scored 62.7% for $0.16 USD. At `medium`, Claude Sonnet 5.5 scored about 15 points lower than at its default, `high`, for about 48% of the cost per attempt.
    * **Compare models:** In [Compare models](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#compare-models-on-cost-per-task), Claude Opus 5.5 at its default cost under a third as much per attempt as Claude Fable 5.1 at `medium`, which is a single run.

12. **Internal repository-task benchmark (cap measurement):**

    * **What was measured:** A separate Anthropic-internal set of about 130 repository tasks, run August 20, 2026 (Claude Fable 5.1) and September 19, 2026 (Claude Opus 5.5, at its default effort, `medium`), with a plain API agent loop, one attempt per task.
    * **How priced:** Cost per solved task is priced as a customer is billed, with a 5-minute prompt cache, for Claude Fable 5.1, and at list prices from the token counts its runs recorded for Claude Opus 5.5.
    * **Claude Fable 5.1 runs:** The Claude Fable 5.1 runs are 135 tasks per cap at the default effort set explicitly: the 16,384-token figure averages two runs (36.3% on both); the 64,000 and 128,000 figures are single runs (58.5% and 60.0%). Five problems drew a safety refusal in all four runs and count as failures.
    * **Claude Opus 5.5 runs:** The Claude Opus 5.5 16,384-token figure averages two runs (134 and 135 tasks scored), and its 64,000 and 128,000 figures are single runs (135 tasks each); two attempts in each 16,384-token run and one in each of the 64,000- and 128,000-token runs ended in a safety refusal and count as failures. Claude Opus 5.5 solved 57.6% at 16,384 (58.2% and 57.0%), 75.6% at 64,000, and 68.9% at 128,000. None of its attempts was cut off at 64,000 or 128,000, so the cap does not explain the difference between those two runs.
    * **Attempts the cap ended:** Only 1 of the 66 Claude Opus 5.5 attempts that the 16,384-token cap ended, and 9 of the 117 Claude Fable 5.1 attempts, still passed.
    * **Cost per attempt:** Cost per attempt was $3 USD at 16,384 and $4 USD at 64,000 for Claude Opus 5.5, at list prices, and $8 USD and $13 USD for Claude Fable 5.1, as a customer is billed.
    * **SWE-bench Pro cap figures:** The SWE-bench Pro cap figures are one Claude Fable 5.1 run per cap at the default effort, run August 26, 2026, on a 100-problem subset stratified from reference 3's 482-problem set, not comparable to its scores; at the default effort the runs at 16,384 and at 64,000 each solved 94 of the 100 problems.
    * **Turn length:** The per-turn distributions in the section's dot plot come from the Claude Opus 5.5 and Claude Fable 5.1 runs at 128,000: no Opus 5.5 turn reached the cap (the longest was about 61,000 tokens, and 0.56% of its turns exceeded 16,384), and one Fable 5.1 turn reached 128,000 (0.46% of its turns exceeded 16,384). With the cap at 128,000, 2 of Claude Fable 5.1's 14,331 turns were longer than 64,000 tokens, and no Claude Opus 5.5 turn was.

13. **Chartography:** Surge AI, "Chartography," 2026.

    * **What was measured:** The complete released 100-question set, measured August 6 and 9, 2026 (Claude Opus 5 alone) and September 20, 2026 (Claude Opus 5.5), with Anthropic's implementation on Claude Managed Agents (standard cloud sandbox; advisor configurations use the Managed Agents advisor).
    * **How scored:** Claude Sonnet 4.6 grades instead of the reference judge and the benchmark runs with tools, so scores compare across configurations here but not to the published leaderboard. They are also not comparable to the Chartography results in the Claude Opus 5.5 system card, which use a different grader and run at `max` effort. Two runs per configuration (three for Claude Opus 5.5), pooled; run-to-run spreads were up to 10 points.
    * **How priced:** Costs are what a customer running the agent routinely is billed: each chart's first request reads the agent's shared system prompt and tools from the cache, as it does when another session of the same agent ran in the previous 5 minutes. A chart run on its own costs about $0.03 USD more with Claude Opus 5 or Claude Opus 5.5 and about $0.12 USD more with Claude Fable 5.1. The August figures are re-priced this way from the runs' usage records. Costs exclude sandbox time, which added under 1% to the August runs.
    * **Claude Fable 5.1 alone, August runs:** The runs of Claude Fable 5.1 alone are from August 24, 2026, under the platform's launch serving settings, two runs per setting; six attempts hit the 15-minute session cap and score 0, and two charts per run were answered by Claude Opus 5 after a safety refusal.
    * **Claude Opus 5 with a Claude Fable 5.1 advisor:** The Claude Opus 5 low-effort executor with a Claude Fable 5.1 advisor ran twice on August 30, 2026, under the same settings (63.0 and 67.0, mean 65.0, at $0.47 USD a chart; the advisor was consulted on 88% of tasks in each run, and 4 of its 219 replies came from Claude Opus 5 instead, each after a production safety filter stopped the advisor's own reply). That pairing matched Claude Fable 5.1 alone at `medium` within run-to-run noise (65.0 compared with 67.5) at about 1.8 times the cost per task: a consult that fires on most tasks costs more than running the stronger model itself.
    * **Claude Opus 5.5 runs:** Claude Opus 5.5 ran at `low`, with server-side fallback off and a safety classifier judging every tool call: three runs alone (70, 68, and 68) and three with a Claude Fable 5.1 advisor configured (59, 63, and 63), in which it consulted the advisor on 1 of 300 tasks.
    * **Results at `low` effort:** On this chart-reading benchmark, Claude Opus 5.5 at `low` scored 68.7 for about $0.03 USD a chart, against 62.5 for $0.15 USD from Claude Fable 5.1 at `low` and 49 for $0.16 USD from Claude Opus 5 at `low`.
    * **Claude Fable 5.1 alone, October runs:** For comparison with the Claude Opus 5.5 pairing, Claude Fable 5.1 alone at `high`, its default, was run three times on October 7, 2026, with the same implementation and platform settings as the Claude Opus 5.5 runs: 82, 79, and 79, a mean of 80.0.
    * **Consult rate:** The consult-rate comparison for the earlier pairings comes from rerunning the same configurations on the Messages API with a container tool set, August 10 to 11, 2026.

14. **Support-desk prompt-audit evaluation:**

    * **What was measured:** An Anthropic-constructed set of 44 support tickets with deterministic grading, run in early August 2026 and reported on August 8, 2026, under six system prompts, each adding to the same clean prompt one pattern common in prompts written for Claude Opus 4.8 and Claude Sonnet 4.6.
    * **The chart:** Each chart point is one of three cases (older model, newer model on the same prompt, newer model after the audit) averaged over the six prompts and 44 tickets.
    * **Results, Claude Opus 5:** On Claude Opus 5, the prompts written for Claude Opus 4.8 cost 36% more per ticket than they did on Claude Opus 4.8, for no change in accuracy. After the audit they cost 14% less on Claude Opus 5 than before it (from the unrounded means; the chart's rounded costs, 3.43 and 2.93 US cents per ticket, give 14.6%), and Claude Opus 5 resolved 97% of tickets correctly, up from 92%. By pattern, on Claude Opus 5: removing "verify twice" cut the cost per ticket by a third, and removing "be maximally thorough" cut it almost as much; removing the retired thinking setting, the contradictory rules, and the hand-rolled scratchpad each restored 7 to 11 points of accuracy.
    * **Results, Claude Sonnet 5:** On the Claude Sonnet 4.6 to Claude Sonnet 5 migration, the audit took 14% off the cost per ticket at the same accuracy.
    * **Caveats:** The Opus 5 accuracy gain has a 95% confidence interval of 3 to 8 points; the Sonnet accuracy differences are within noise.

15. **Data-file question set:** An Anthropic-constructed set of 25 aggregate questions over a 1,862-row slice of a public liquor-sales CSV, with ground truth computed by pandas and exact-match grading, run on Claude Sonnet 5 and Claude Opus 5 with thinking disabled (the in-context arm cannot complete at the default), a 4,000-token output cap, and no prompt caching, three runs per configuration, run August 19, 2026. The file arm uploads the CSV through the Files API and uses the `code_execution_20260120` tool. The in-context arm's three Claude Sonnet 5 runs answered 6, 7, and 7 of the 25 questions correctly; the chart's label and the text give their mean, 6.67, to the nearest question, and the chart's point is drawn at the mean, 26.7%.

16. **Cache duration measurement:**

    * **What was measured:** The 20-issue triage job from [Trim input and context tokens](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#trim-input-and-context-tokens), run on Claude Sonnet 5 on August 23, 2026, and on Claude Opus 5.5 on September 19 and 20, 2026, at its default effort (`medium`) and at `high`, on the Messages API with the same harness (for Claude Opus 5.5, a port of it that sends the same request bodies), the Claude Opus 5.5 cells with `max_tokens` raised to 4,096, with pauses inserted before a randomly chosen share of turns (none, 5%, 10%, and every turn at 6 minutes on all 20 issues on both models, plus every turn at 2 minutes on Claude Sonnet 5; 20-minute and 45-minute pauses on a 5-issue subset on both models). The Claude Opus 5.5 figures on this page cover both effort levels.
    * **Other models and dates:** Claude Opus 5's keep-alive figures below come from the same job on August 23, 2026, with `max_tokens` raised to 4,096, on the same schedules except the 2-minute and 45-minute pauses. Claude Sonnet 5.5 ran the same measurement as Claude Sonnet 5 (the same pause schedules and three cache settings, three runs per cell), with the ported harness used for Claude Opus 5.5, at its default effort, `high`, on September 24, 2026.
    * **How scored and priced:** Three runs per cell, cost computed from each response's `usage` fields at list prices (for Claude Opus 5.5, $4 USD input, $5 USD 5-minute write, $8 USD 1-hour write, $0.20 USD cache read, and $20 USD output per million tokens; Claude Sonnet 5 ran on an Anthropic-internal organization whose usage is metered the same way as a customer organization's), accuracy against the same gold labels.
    * **How run and priced, Claude Sonnet 5.5:** Claude Sonnet 5.5 set `max_tokens` to 4,096 on session requests and to 1 on keep-alive requests, ran on an Anthropic-internal organization whose usage is metered the same way as a customer organization's, and is priced at its current list prices ($2 USD input, $2.50 USD 5-minute write, $4 USD 1-hour write, $0.10 USD cache read, and $10 USD output per million tokens). Apart from the higher `max_tokens`, which no turn reached, one input differs from the Claude Sonnet 5 runs: the job's one animated GIF was sent as a PNG of its first frame, the only frame the API uses ([Vision](https://platform.claude.com/docs/en/build-with-claude/vision)), and the two count as the same number of input tokens.
    * **Break-even:** The break-even is about 3.3% of turns on Claude Sonnet 5 and 3.1% to 3.2% on Claude Opus 5.5: the median of each session's break-even share, computed by the cost model from that session's turn-by-turn context sizes, over all 45 Claude Sonnet 5 twenty-issue sessions and the 36 Claude Opus 5.5 twenty-issue sessions at each effort level (every pause schedule run on the full job, under all three cache settings, three runs each; the 5-issue cells are not in it). The break-even on Claude Sonnet 5.5 is about 3.1% of turns, the median over its 45 twenty-issue sessions. The cache duration chart plots these Claude Sonnet 5.5 sessions, three per point.
    * **5-minute and 1-hour settings, Claude Sonnet 5 and Claude Opus 5.5:** In the 5% cell the 5-minute and 1-hour settings tied on Claude Sonnet 5, because that draw's pauses fell on small prefixes; on Claude Opus 5.5 they nearly tied. On Claude Sonnet 5, at its cache-read price of $0.20 USD per million tokens, a session cost $0.60 USD, $0.69 USD, and $0.99 USD on the 5-minute setting with no pauses, 5%, and 10% of turns paused, and $0.70 USD, $0.70 USD, and $0.71 USD on the 1-hour setting.
    * **Keep-alive requests, Claude Sonnet 5 and Claude Opus 5:** Anthropic measured keep-alive requests that refresh the 5-minute cache on Claude Sonnet 5 and Claude Opus 5 on August 23, 2026, and on Claude Opus 5.5 in the runs above, always sent with `max_tokens: 1`. On Claude Sonnet 5 they cost 7.7% less than the 1-hour setting with 5% of turns paused and about the same with 10%; on Claude Opus 5 no difference was measurable at either share; on both they cost more with a pause of 6 minutes or more before every turn. So on those two models the setting to use is the 1-hour duration, not keep-alive requests.
    * **Keep-alive requests, Claude Opus 5.5:** On Claude Opus 5.5 keep-alive requests cost 8% to 18% less than the 1-hour setting with 5% and 10% of turns paused (8% to 13% less at its default effort, `medium`, and 10% to 18% less at `high`; about 10% to 15% once between-session noise is removed by re-billing each keep-alive session's own tokens at 1-hour cache prices), and more with a pause before every turn: 4% to 6% more at 6 minutes, 9% to 10% at 20 minutes, and 56% to 58% at 45 minutes.
    * **Requests with `max_tokens: 0`, Claude Opus 5.5:** Anthropic's pre-launch API tests on Claude Opus 5.5 show that a `max_tokens: 0` request writes the cache and that the next request reads it; whether such a request refreshes an existing entry was not measured on Opus 5.5.
    * **5-minute and 1-hour settings, Claude Sonnet 5.5:** With 5% of turns paused the 5-minute setting cost 5% more than the 1-hour setting on average (2% less to 12% more across the three runs), which is within run-to-run variation: that draw's pauses fell on small prefixes, as on Claude Sonnet 5, and re-billing each 5-minute session's own tokens at 1-hour cache prices gives about 1% more. With 10% paused it cost 54% more (36% to 73% more). With no pauses, the 5-minute setting cost 19% less than the 1-hour setting on average (3% to 32% less across the three runs; the 1-hour setting's higher write price predicts about 20%), and 21% to 24% less in every run with 2-minute pauses.
    * **Keep-alive requests, Claude Sonnet 5.5:** Keep-alive requests cost 16% less than the 1-hour setting on average with 5% of turns paused (13% to 20% less across the three runs) and 8% less with 10% (3% to 10% less), and cost more with a pause of 6 minutes or more before every turn. With 5% and 10% of turns paused, the pauses lasted 6 to 32 minutes on Claude Sonnet 5.5 and on Claude Opus 5.5. Re-billing each keep-alive session's own tokens at 1-hour cache prices, as for Claude Opus 5.5 above, gives 15% to 16% less at 5% paused and about 10% less at 10%, and with a pause before every turn 7% more at 6 minutes, 9% to 10% more at 20 minutes, and 66% to 73% more at 45 minutes. The 6-minute figures leave out run 3, in which 2 of that session's 39 keep-alive requests timed out: the cache expired before those two turns, the session wrote 214,000 tokens to the cache against 80,000 to 85,000 in runs 1 and 2, and it cost 38% more than run 3's 1-hour session.
    * **Keep-alive requests, Claude Sonnet 5.5, by run:** Comparing each run's keep-alive session with the same run's 1-hour session instead, keep-alive cost from about the same to 10% more at 6 minutes (runs 1 and 2; 4% more on their average), from about the same to 16% more at 20 minutes, and 64% to 80% more at 45 minutes.
    * **Keep-alive requests, Claude Sonnet 5.5, sample size:** The keep-alive chart's 6-minute points average runs 1 and 2 for all three settings. Each cell is three sessions (two for the 6-minute figures above). With no pauses, keep-alive sends no extra requests and so matches the 5-minute setting, yet the two differed by as much as 23% within a single run, so a difference of a few percent in a three-run average is not a clear effect.
    * **Caching off and on, Claude Sonnet 5:** On Claude Sonnet 5, the same job was run with caching off and with caching on, three runs each on August 19, 2026, with `max_tokens` at 700: $3.36 USD against $0.57 USD a session on average, a saving of 83%.
    * **Priced from recorded token counts, Claude Sonnet 5.5:** Anthropic also re-priced the recorded token counts of the three Claude Sonnet 5.5 sessions with the 5-minute cache and no pauses for the caching figure in [Why caching comes first](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#why-caching-comes-first); it made no run with caching off on Claude Sonnet 5.5. Each of these three sessions is one conversation of 40 requests over the job's 20 issues. At list prices as of October 12, 2026, the sessions cost $0.51 USD each on average, from the usage fields, against $3.70 USD with every input token at the input price and output tokens unchanged: a saving of 86% (86% to 87% across the three sessions), or a factor of 7.3. At the launch cache-read price of $0.20 USD the saving is 82%, so the rise over the Claude Sonnet 5 figure comes from the lower cache-read price.
    * **Priced from recorded token counts, Claude Opus 5.5:** Re-priced the same way, the three Claude Opus 5.5 sessions at its default effort, `medium`, with the 5-minute cache and no pauses cost $1.02 USD each on average against $6.93 USD, a saving of 85%, or a factor of 6.8; Anthropic made no run with caching off on Claude Opus 5.5, and the model used thinking in 79% of requests.
    * **How thinking was set, two sets of runs only:** The requests of the three Claude Sonnet 5.5 sessions with the 5-minute cache and no pauses set no thinking option, so thinking was left at the model's default, and the model used it in 38% of requests. The requests of the Claude Sonnet 5 runs with caching off and with caching on also set no thinking option, so thinking was left at the model's default, and the model used it in 41 of 121 requests with caching off and 40 of 120 with caching on.
    * **Latency after a pause:** On Claude Sonnet 5 and Claude Opus 5, the turn after a pause kept its warm-cache latency on the 1-hour setting. Claude Opus 5.5's time to first token after a pause was not measured. Claude Sonnet 5.5's time to first token after a pause was not measured.

17. **Cache-read share in production:** Aggregated first-party Claude API usage for the 14 days ending August 23, 2026, direct API product only, Anthropic-internal organizations excluded, no organization identified. An organization-day counts as an agent loop when its requests carry tool definitions and tool results, its prompts hold 9 or more prior tool calls on average, caching was used, and it made at least 10 such requests (the API has no conversation identifier, so this stands in for conversation length): 303,003 organization-days across 106,487 organizations, median cache-read share 84.2% of all input tokens, upper quartile 91.7%. Use-case labels (the organization's declared use case, or otherwise its classified one) cover 74% of those organization-days and 99% of their tokens; about 72% of coding organization-days read 80% or more. The top decile of organization-days reads 95.9% or more for coding and 94.2% to 94.8% for support, research, data, and other agents. The request-level split at 25 or more prior tool calls comes from a six-hour sample: coding 92% read, 7% write, under 1% uncached.

18. **Compaction timing and status-line measurements:**

    * **What was measured:** The triage agent's long variant from [Trim input and context tokens](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#trim-input-and-context-tokens), run August 24, 2026, on Claude Sonnet 5 with the 5-minute cache, cost from the usage fields at list prices, five sessions per arm: a no-change arm at the default effort throughout ($0.81 USD per session), and two arms that start at low effort and make the same two cache-breaking changes, a switch to the default effort and one added tool, either mid-session at requests 12 and 17 ($0.95 USD) or together on the first request after the first compaction ($0.75 USD).
    * **Fourth arm:** A fourth arm of six sessions, run August 25, 2026, made the same two changes on the request that triggered the first compaction ($0.92 USD per session): that request's summarization pass wrote the 81,000-token context to the cache instead of reading it, so that pass cost $0.21 USD against $0.04 USD for the same pass in the boundary arm.
    * **Compaction:** Sessions first compacted at request 21 to 25 (16 of the 21 sessions at request 22), once the prompt passed the 80,000-token compaction trigger, and two no-change sessions compacted a second time near the end. The boundary arm's lower total than the no-change arm reflects its low-effort requests before the change and those second compactions rather than caching: the two arms' re-write costs differ by under $0.01 USD.
    * **Mid-session arm:** The mid-session arm paid $0.23 USD per session in cache re-writes; the difference between the mid-session and boundary arms was $0.20 USD with a 95% confidence interval of $0.11 USD to $0.29 USD. In the mid-session arm, the effort change and the added tool rewrote 39,000 and 60,000 cached tokens. One of its sessions ran cheap ($0.82 USD) after its model mis-called the search tool following compaction and got empty results; it is included, and without it the arm averages $0.98 USD.
    * **Accuracy and cache reads:** Accuracy averaged 14.2 of 20 labels in each August 24 arm and 14.7 in the August 25 arm; cache reads were 91% of prompt tokens with no changes, 85% mid-session, 91% at the boundary, and 86% with the changes on the triggering request.
    * **Separate measurement, status line:** A separate measurement on the 20-issue triage job from [Trim input and context tokens](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#trim-input-and-context-tokens), run August 18, 2026, also on Claude Sonnet 5 with the 5-minute cache, priced the same way, three runs per arm: with a 25-token status line at the front of the system prompt, a run cost $4.24 USD on average ($4.12 USD to $4.47 USD across the three runs) and read nothing from the cache; with the same line at the end of the newest user turn, after the last cache breakpoint, a run cost $0.59 USD ($0.55 USD to $0.61 USD). The first is more than the same job cost with caching off. A later re-run with the same configuration gave $4.28 USD and $0.61 USD.

19. **Cache duration measurement on Claude Fable 5.1:** The same 20-issue triage job and harness as reference 16, with `max_tokens` raised to 4,096, run August 23 and August 26, 2026, on the Claude Fable 5.1 launch snapshot at its launch prices ($10 USD input, $12.50 USD 5-minute write, $20 USD 1-hour write, $0.25 USD cache read, $50 USD output per million tokens), three settings per schedule: the 5-minute cache, the 1-hour cache, and the 5-minute cache kept warm by a `max_tokens: 0` request on the unchanged prefix every 4 minutes, timed from the previous request's start (the August 23 runs sent keep-alive requests with `max_tokens: 1`; in the August 26 cells reported here, every answered keep-alive request refreshed the cache and its response reported no output tokens). Schedules: no pauses, 10% of turns, and every turn at 6 minutes on all 20 issues, and 45-minute pauses on the 5-issue subset; three runs per cell (six for the August 26 keep-alive cell with 45-minute pauses), cost computed from each response's `usage` fields at list prices, accuracy against the same gold labels (12 to 18 exact labels of 20). Per-session means on August 26 for the 5-minute, 1-hour, and keep-alive settings: no pauses $2.42 USD, $3.09 USD, $2.29 USD; 10% paused $4.50 USD, $2.96 USD, $2.36 USD; every turn $22.89 USD, $3.01 USD, $2.62 USD; the August 23 cells agree within 6%. The 45-minute figures ($1.68 USD, $0.59 USD, and $0.71 USD per 5-issue session) are from later sessions of August 26: that day's first set of sessions was cut off when its machine was shut down, and the second was affected by a fault in the service and is set aside. The third set gives the 5-minute and 1-hour figures; its three keep-alive sessions sent each keep-alive request once, lost requests to rate-limit refusals, and are not in the mean. The keep-alive figure is the mean of six further sessions that sent any refused keep-alive request again within two seconds. The August 23 runs gave $1.67 USD, $0.58 USD, and $0.70 USD. The break-even between the 5-minute and 1-hour settings is 3.1% of turns, the same measure as reference 16. Claude Fable 5.1's cache read costs 0.025x the input price while its cache writes keep the standard multipliers, so a keep-alive request that re-reads the prefix is cheap and the 1-hour duration's write premium is the larger bill, except with 45-minute pauses, where the keep-alive requests cost more than the premium.

20. **Terminal-Bench 3:** the public terminal-agent benchmark's 74 tasks, run on [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview) with two custom tools, a shell and a file editor that the evaluation harness runs in each task's own container, in place of the platform's built-in tools, and otherwise at the platform's default settings for external accounts, two runs per model at `high` effort, August 27 to 28, 2026. These runs used Terminal-Bench version 3.0, and their scores are not comparable with the public Terminal-Bench leaderboard or with the Terminal-Bench 4.0 results in the Claude Opus 5.5 system card, which come from runs in Claude Code at `max` effort. Each task's time limits are 2.5 times the benchmark's own, which gives the agent between 75 minutes and 20 hours per task (5 hours for the median task), and each task gets three times the memory it specifies, from 6 GiB to 96 GiB, with extra memory for the 12 tasks that run helper services. The agent had no general internet access: its containers could reach an internal package mirror, a short list of download sites including GitHub and the Python Package Index, and a few sites specific to some tasks, and eight of the tasks had no network access at all. Scores are raw pass rates over the 148 attempts per model; single runs swing by 5 to 11 points. Costs are what a customer would be billed at list prices, re-priced request by request from the runs' usage records with the 5-minute cache lifetime. Claude Opus 4.7, Claude Opus 4.8, and Claude Opus 5 each spend $8 USD to $15 USD per task. Claude Opus 4.7 ended 11 of its 148 attempts at its output cap.

21. **DRACO:** Perplexity, "DRACO: a Cross-Domain Benchmark for Deep Research Accuracy, Completeness, and Objectivity," arXiv:2602.11685, 2026.

    * **What was measured:** Its 100 research tasks across 10 domains are graded against expert-written rubrics of about 40 weighted criteria each, and the score is the weighted share of criteria met, from 0 to 100.
    * **Configurations:** Every configuration ran on the Claude API with Claude Opus 5.5, the default adaptive thinking, the production safety classifiers on, and `max_tokens` at 128,000 with streaming: a single agent at `medium` effort (the model's default) and at `low`, the single agent at `medium` with the sentence and the clock, and a team at `medium` with and without them. The team is a lead agent that can start helper agents of the same model through a tool, with no cap on their number.
    * **The sentence:** The two changes are a sentence and a clock. The sentence, "Time matters here: do not spend time that can be avoided, and the earlier a correct result is obtained, the better.", goes at the end of the task in the agent's first `user` message, after a blank line, and at the end of each helper's brief.
    * **The clock:** The clock is the elapsed time in whole seconds, such as `[elapsed 252s]`, added before every request, including the first, to the end of the newest `user` message: in its own text block after the task on the first request, and at the end of the last tool result's text, after a blank line, when the message carries tool results. Earlier clocks stay in place, so the cached prefix still matches on the next request. Every agent in a team reads the same clock, and the system prompt doesn't change.
    * **In the measured runs:** The measured runs used this wording and format. Their clock started at the first token of the first response rather than at the start of the task. In the measured team runs, a helper's report reached the lead in a separate message after the clock, not inside the last tool result.
    * **When:** Each configuration made three attempts at each task, with a four-hour limit per attempt, run September 24, 2026, and all configurations of a set started together.
    * **Tools:** The agents used search and fetch tools that the evaluation harness hosts over an Anthropic web index, and Python and a shell in a sandbox with no network access. Those tools set part of the time, and yours will run at a different speed, so the page gives time as a ratio between configurations, not in minutes.
    * **How timed:** Time is the wall-clock time of an attempt, from its first request to the end of the last request by any agent, including tool runs, averaged over a task's attempts. A typical-task figure is the median, over tasks, of each task's ratio between two configurations.
    * **How priced:** Each task's cost is its requests priced at Claude Opus 5.5's public list prices, with prompt caching billed as it would be for a customer who sets a cache breakpoint at the end of each request and uses the 5-minute cache lifetime. Each request reads the previous request's prompt from the cache and writes the rest. An attempt's first request, and any request that starts more than 5 minutes after the one before it, writes its whole prompt. Costs cover model tokens only; the harness's tools add no charges.
    * **How scored:** All intervals are 95% bootstrap intervals over tasks, and score changes are paired differences over tasks. Claude Opus 5 grades the answers, so Claude Opus 5.5 doesn't grade its own work, and each answer's score averages five judging runs.
    * **Caveats:** A production safety classifier stopped three attempts in each configuration, all on one task, and those attempts score 0; leaving that task out changes no finding. The runs also passed each agent's tool use through an Anthropic-internal safety check that customer requests don't have, which adds an unmeasured amount of time to each request in every configuration. On DRACO, the single agent without the changes made about twice as many requests, and the team about a third more, so the check probably makes the DRACO time savings look slightly larger.
    * **Results, single agent:** Results for [Show the model elapsed time](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#show-the-model-elapsed-time): with the changes, the single agent took 47% less time at a 60% lower cost on the typical task, its average cost fell from $1.13 USD to $0.44 USD per task, and its score was 4.1 points lower (95% interval 2.9 to 5.2 lower).
    * **Results, lower effort:** Lowering the single agent's effort saved more time and cost than the changes did, and lost more score. At `low` effort, it scored 13.3 points lower on DRACO, 3.4 on HLE, and 14.0 on the physics set than at `medium`, and the typical task took 84%, 30%, and 47% less time. With the changes at `medium` effort, it scored 9.2, 2.5, and 11.0 points higher than at `low`, and the typical task took longer than at `low` by a factor of 1.2 to 3.2.
    * **Results, team, helpers:** The team's lead rarely started helpers. Without the changes, it started a helper in only 5 of 300 attempts on DRACO, 13 of 1,479 on HLE, and none of 280 on the physics set.
    * **Results, team:** So the team results mostly show the lead agent working alone, with the team's own instructions and tools, and Anthropic has no measurement of the changes on a team that works in parallel. Without the changes, the team already took about half the single agent's time on the typical DRACO task, and scored 3.3 points lower (95% interval 2.1 to 4.6 lower). With the changes, the team took 17% less time at a 20% lower cost on the typical DRACO task, and scored 1.6 points lower (95% interval 0.3 to 2.8 lower).
    * **Not measured:** Anthropic didn't measure the changes on Claude Managed Agents.

22. **HLE:** Phan et al., "Humanity's Last Exam," arXiv:2501.14249, 2025. Expert-written questions with exact answers, graded against the reference answers. Measured on the first 500 questions of the September 10, 2025, release, images included, with the benchmark's own sources blocked from search, and the same setup as reference 21. Each configuration made three attempts at each question, run September 24, 2026. Claude Opus 5 compares each answer with the reference answer, using the benchmark's published judge prompt, and the majority of three judgings counts. The scores cover 493 questions in every configuration. For five of the others, the grading request was over the judge's 1M-token limit, and the other two are left out because the run of the single agent without the changes stopped before three of its attempts on them finished. Time and cost ratios cover 492 questions for the single agent and 491 for the team, because one or two questions have no timing. A production safety classifier stopped 3% to 4% of each configuration's attempts, and those attempts score 0; leaving them out changes no finding. Results for [Show the model elapsed time](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#show-the-model-elapsed-time): with the changes, the single agent took 14% less time at a 9% lower cost on the typical question. With the Claude Opus 5 judge, its score showed no clear change (0.9 points lower, 95% interval 2.5 lower to 0.7 higher). With a second grader, Claude Opus 4.6, its score was 1.9 points lower (95% interval 0.2 to 3.7 lower). Average time fell further than the typical question's: average time fell 43% and average cost 37%, because the changes cut a few very long questions short. The team's time on the typical question changed by 3% or less, and its score didn't change clearly.

23. **Physics set:** An internal set of 70 research-level physics problems, adapted from the public CritPt benchmark: Zhu et al., "Probing the Critical Point (CritPt) of AI Reasoning: a Frontier Physics Research Benchmark," arXiv:2509.26574, 2025. Expert reviewers corrected the problem statements. Claude Opus 4.6 grades each answer with partial credit, using the set's grading prompt, against expert reference solutions that aren't public, so the scores can't be compared with published results. The score is the mean grade over a problem's attempts, averaged over problems, in points out of 100. Measured on all 70 problems, four attempts per problem, run September 24, 2026. Every agent had a Python tool, a shell, and a file editor in a sandbox container with no network access, and no search or fetch tools. No safety classifier stopped an attempt on the physics set. Otherwise the setup is that of reference 21. Results for [Show the model elapsed time](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#show-the-model-elapsed-time): with the changes, the single agent took 7% less time at a 4% lower cost on the typical problem, and its score was 3.0 points lower (95% interval 0.4 to 5.6 lower). The team's time on the typical problem changed by 3% or less, and its score didn't change clearly. The single agent's average time fell 14%. The single agent's whole average time saving comes from one problem, on which the agent without the changes ran code for about half an hour per attempt; without that problem, its average time is about the same with and without the changes.

24. **tau2-bench retail:** Barres et al., "τ²-Bench: Evaluating Conversational Agents in a Dual-Control Environment," arXiv:2506.07982, 2025.

    * **What was measured:** The retail domain's 114 tasks ran on the public harness against the Claude API, with Claude Haiku 4.5 as the simulated user, Claude Sonnet 5 as the natural-language judge, and prompt caching on; the tasks were split into 57 search and 57 held-out.
    * **When:** The two searches ran on September 6, 2026, driven by the Claude API skill's `hillclimb` command. The caching before-and-after pair ran on September 8, 2026.
    * **How scored:** In the searches, the starting points and the confirmed configuration are the mean of three held-out runs, kept steps were judged on two runs, and other candidates were scored on one or two runs. The caching pair: three runs each on all 114 tasks with only the harness's cache breakpoints toggled, the configuration the `cost-optimize` command produced in an earlier run. Held-out numbers are on 57 tasks the search never read.
    * **How priced:** Cost per task prices the agent's and the simulated user's token counts at list prices (Claude Opus 5 $5 USD and $25 USD, Claude Sonnet 5 $2 USD and $10 USD per million input and output tokens, cache reads and writes at their published rates) and excludes the judge; percent changes come from unrounded costs; the monthly figure is the agent's tokens alone, $0.135 USD and $0.047 USD per task, times 10,000. At 10,000 conversations a month, that is about $1,350 USD before the first search and $470 USD after.
    * **Caveats:** These measurements ran on the previous Claude Opus and Claude Sonnet models: the caching pair ran on Claude Sonnet 5, the second search started from Claude Sonnet 5, and the first search went from Claude Opus 5 to Claude Sonnet 5. Claude Fable 5.1 was not measured on this benchmark.
    * **Caching pair:** The pair ran on Claude Sonnet 5 at the default effort. The public harness, as shipped, sends the whole conversation uncached on every turn. The cached configuration has one breakpoint on the system prompt and one on the latest message. Both searches ran with that caching on. Cost per task went from $0.223 USD uncached to $0.062 USD cached, a 72% saving, and the pass rate from 79.2% to 76.0%. Identical cached runs of that configuration ranged from 85 to 93 of 114 across days. Every cached run scored at or below every uncached run, but the gap of under 4 tasks sits inside the spread of identical cached runs, so the accuracy change is too small to measure at this sample size.
    * **How the search ran.** The `hillclimb` command asks four questions, presents a plan, and waits for approval before it spends anything. In the first search, the plan left the user simulator, grader, caching, temperature, and tasks unchanged. The last of the four questions began: `One pass over the full set is 114 cases x 1 rep on claude-opus-5, roughly 22 minutes.` Each round, the search proposes one change and runs the full set. It keeps the change only when the number moved and the predicted mechanism shows in the usage data. It stops when three rounds in a row bring nothing, then confirms the winner on fresh runs.
    * **First search, result.** The search cut cost per task by 61% while holding the pass rate within a 2-point band set before the search: from Claude Opus 5 at the default effort ($0.142 USD a task, 76.0% passed) to Claude Sonnet 5 at `low` with one cost-neutral prompt edit ($0.055 USD, 74.3%). The search cost $179 USD in evaluation runs and $228 USD in its own tokens.
    * **First search, start: Claude Opus 5, default effort.** 76.0% at $0.142 USD. Three identical runs spanned 43 to 44 of 57. The search set the floor 2 points under, at 74.0%, and rounded it up to 43 of 57 (75.4%) for its verdicts.
    * **First search, step 1, effort to `low`: kept.** 77.2% on the two runs that kept it, 77.8% on a three-run confirm after the search, at $0.119 USD, 17% cheaper. The search's own status line reads, in part: `two runs held-out 42 and 46, mean 44.0 >= floor 43; cost mean $0.1187 <= gate $0.1208; mechanism confirmed (output tokens -34% with calls flat)`.
    * **First search, step 2, Claude Sonnet 5 at `low`: kept.** 75.4% at $0.055 USD, 61% cheaper.
    * **First search, step 3, a prompt edit (look the customer's orders up after login instead of asking for an order ID): kept on selection, then did not hold.** 79.8% on two runs; 74.3% on three fresh runs. The search left it in as cost-neutral: the freed turn became another lookup turn.
    * **First search, step 4, a prompt edit (transfer to a human only when asked): rejected and reverted.** 71.9%. It fixed the 3 cases it targeted and broke 10 others with a generic "say what you can and can't do" template.
    * **First search, step 5, a prompt edit: not run.** Its predicted gain of 0.5 tasks was under the search's 2-task adoption gate.
    * **First search, confirm: Claude Sonnet 5 at `low` with the step-3 prompt, three fresh runs.** 74.3% at $0.055 USD, inside the 2-point band by 0.14 of a task, 1 task in 57 under the start, and below the 43-of-57 floor the search registered. This configuration's five runs spanned 42 to 46, wider than the start's 43 to 44.
    * **First search, what it showed.** The effort and model levers produced the savings, and each one's mechanism confirmed it. The prompt lever produced real behavior changes but no durable gain. On this workload, the number of turns and the cached prefix each turn re-reads set the cost per task, not the wording.
    * **Second search.** It started from Claude Sonnet 5 at the default effort with caching on: 79.5% at $0.062 USD on the held-out half, with three runs spanning 42 to 47 of 57, so the floor was 45 of 57 (78.9%). Identical runs of a starting configuration differed by up to 5 tasks in 57 here. The second search kept nothing. Effort at `low`, two prompt edits, and both together each scored 77.2%, under the floor, and saved 10% to 14%, short of the search's 15% cost gate. A prompt edit for accuracy scored 79.8% on two runs and 73.7% on three fresh runs, and was reverted. The search took about 19 evaluation runs and $120 USD.

25. **Claude Managed Agents task set:**

    * **What was measured:** An Anthropic-internal set of 79 scripted agent tasks in eight areas, including memory, multi-agent, and long-context work, run as [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview) sessions in which the test answers every tool call. Each task ran five times per model.
    * **Runs:** The figures are from one run per model on October 7, 2026, graded that day. In three more runs of the same tasks on October 8 and 9, 2026, Claude Haiku 5.5 passed 91% to 93% of attempts, and in one more run on October 8, Claude Haiku 4.5 passed 63%.
    * **How scored:** An attempt passed only if the grader, Claude Sonnet 4.6, grading once, marked every line of the task's checklist as met, so pass rates depend on the grader. On all but one task, a separate call, shown the tool results in full, graded the line that checks the files and messages the agent wrote through its tools against those results.
    * **How priced:** Costs are token costs at list prices with 5-minute prompt caching, priced request by request, and exclude session runtime.
    * **Results, token prices and cost:** Claude Haiku 4.5 did not cache 80% of its requests: each had a prompt of about 4,100 tokens or fewer, and its minimum cacheable prompt length is 4,096 tokens (512 for Claude Haiku 5.5). From Claude Haiku 4.5 to Claude Haiku 5.5, token prices fell by up to 90%, and the token cost of the 79 tasks fell by about 75%. The token cost fell less than the prices because about 5% of Claude Haiku 5.5's requests had prompts over 100,000 tokens, which pay higher prices ([Long context pricing](https://platform.claude.com/docs/en/about-claude/pricing#long-context-pricing)), and they carried 73% of its cost.
    * **Thinking:** Anthropic set Claude Haiku 5.5's effort to `medium` and sent no thinking setting or output limit for either model, so thinking was left to Claude Managed Agents' own settings for each model. Claude Haiku 5.5 used thinking in 59% of requests, and Claude Haiku 4.5 in 22%. The comparison is of each model as served, not at equal settings.
    * **Cost without caching, priced from recorded token counts:** Anthropic also re-priced the recorded token counts of Claude Haiku 5.5's October 7 run for the caching factor in [Why caching comes first](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#why-caching-comes-first); it made no run with caching off, and Claude Managed Agents applies prompt caching itself, so the factor compares two prices for the same requests, not two settings.
    * **The factor:** The factor, 1.7, is the run's token cost with every input token at the input price, output tokens unchanged, divided by its token cost with each session priced by itself: each request's prior prompt as a cache read and its new tokens as a 5-minute cache write. Each request is priced for its own prompt length in both costs, so the 87 requests over 100,000 tokens pay the higher prices in both. On the token counts as recorded, which this guide's costs for the run use, the factor is 1.9, because the five attempts of a task ran side by side and read each other's cache entries.
    * **Why the factor is low:** The factor is low because the sessions are short, a median of 4 requests: most input tokens arrive as tool results on the second or third request and are read from the cache only once or twice. Eight long-context tasks hold three quarters of the cost. A second run, on October 8, also gives 1.7.

26. **Answer-format measurement:**

    * **What was measured:** The 20-issue triage job from [Trim input and context tokens](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#trim-input-and-context-tokens), run on Claude Sonnet 5 with prompt caching on and no thinking setting in the request, so thinking was left at the model's default, under three final-answer instructions, three runs per instruction.
    * **Two-line instruction:** The original asked for two lines: `4. Finish with exactly two lines: LABEL: <one of: bug-confirmed, needs-more-info, duplicate-candidate, feature-request, upstream-issue, perf, ui-polish> SUMMARY: <one or two sentences for the engineering team>`
    * **One-line instruction:** The shorter variant asked for one: `4. Finish with exactly one line in this form: DECISION | LABEL | REASON where DECISION is one of: triage-now, needs-info, close-duplicate; LABEL is one of: bug-confirmed, needs-more-info, duplicate-candidate, feature-request, upstream-issue, perf, ui-polish; REASON is one clause under 15 words. Output nothing after that line.`
    * **Memo instruction:** The longer variant asked for a memo with six headed sections: problem summary, evidence, duplicate check, recommended label, next steps, and confidence.
    * **Also in the instructions as sent:** As sent, the two-line instruction also said "Be concise." and the memo instruction "Be thorough and explicit."
    * **When:** The two-line and one-line instructions ran on August 18, 2026, with `max_tokens` at 700, and the memo instruction on August 19, 2026, with `max_tokens` at 3,000. No response reached its cap.
    * **How scored and priced:** Figures are the mean of the three runs at Claude Sonnet 5's list prices, and accuracy is exact match against the gold labels.
    * **Results:** The one-line answer used 39% fewer output tokens than the two-line original and cost 13% less per run (from the unrounded means; the chart's rounded costs, $0.49 USD and $0.57 USD, give 14%). The memo used six times the output tokens of the two-line original and cost 2.8 times the one-line answer.
    * **Thinking:** About half of the responses included thinking, and its tokens are counted in the output tokens.

27. **Tool search measurement:**

    * **What was measured:** The 20-issue triage job from [Trim input and context tokens](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#trim-input-and-context-tokens), run on Claude Sonnet 5 on August 19, 2026, with prompt caching on and no thinking setting in the request, so thinking was left at the model's default, three runs per configuration. The agent had its own two tools plus real tool definitions from public MCP servers, for a total of 7, 17, 52, 102, 252, or 502 tools, with every definition loaded or with the added ones marked `defer_loading` behind tool search.
    * **How scored and priced:** Figures are the mean of the three runs at Claude Sonnet 5's list prices, and accuracy is exact match against the gold labels.
    * **Results:** With every definition loaded, the run cost rose from $0.55 USD at 7 tools to $1.02 USD at 502 tools, nearly double. With tool search it was $0.55 USD to $0.56 USD at every catalog size, 45% less at 502 tools (from the chart's rounded costs, $0.56 USD and $1.02 USD; the unrounded means give 45.6%). Every run answered 15 to 18 of the 20 issues correctly, with or without tool search.
    * **Caveats:** No run called a tool from the catalog or the tool search tool: the agent's own two tools were always loaded, and every tool call went to one of them. The measurement shows what carrying unused definitions costs, not whether tool search finds a tool when one is needed.
    * **Separate measurement:** In a separate measurement on the same model and date, with a public GitHub MCP server attached through the MCP connector and no catalog, three runs with the server's toolset deferred cost 20% less than three runs without ($0.56 USD and $0.70 USD per run), and the three runs of each arm answered 17, 16, and 16 issues correctly. The requests in this separate measurement included no tool search tool. With the toolset loaded, each run called one of the server's tools, `issue_read`, 3 or 4 times; with it deferred, no run called any of the server's tools.

28. **Input trimming and context lifecycle measurements:**

    * **What was measured:** The 20-issue triage job from [Trim input and context tokens](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#trim-input-and-context-tokens) and its long variant, run on Claude Sonnet 5 on August 19, 2026 (dated in UTC), three runs per setting, with no thinking setting in the request, so thinking was left at the model's default; about 3 in 10 responses included thinking.
    * **The chart:** The chart in [Manage the context lifecycle](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#manage-the-context-lifecycle) compares four settings on each job: the job with prompt caching and input trimming (image resizing and tool search) on, and the same with one lever added, which is context editing, compaction, or the prune. The chart counts a change of under 10% as no change.
    * **Lever settings:** The lever settings differed between the two jobs: context editing cleared at least 2,000 tokens once the prompt passed 20,000 on the 20-issue job, and at least 40,000 once it passed 50,000 on the long one, keeping the three most recent tool uses, and compaction triggered at 50,000 input tokens on the 20-issue job and 80,000 on the long one.
    * **How priced:** Each cost is the mean of the three runs, from the responses' usage fields at Claude Sonnet 5's list prices, with cache writes at $2.50 USD and cache reads at $0.20 USD per million tokens.
    * **Results, input trimming:** A fifth setting, prompt caching with no input trimming, cost $0.57 USD a run on the 20-issue job and $1.38 USD on the long one, so input trimming took 26% off the first and 21% off the second. Against the same 20-issue job with caching off, which cost $3.36 USD a run (reference 16), prompt caching and input trimming together saved 88% (the unrounded means give 87.5%).
    * **Results, 20-issue run:** On the 20-issue run, where the job with no lever cost $0.42 USD a run, context editing cost 73% more, compaction ran once near the end of each run and cost 7% less, and the prune rewrote nothing, because no search result was over its 2,000-character threshold.
    * **Results, long run:** On the long run, where the job with no lever cost $1.09 USD a run, the prune cost 39% less, compaction 32% less, and context editing 4% more.
    * **Cache reads, long runs:** In the long runs with the prune, 89% of prompt tokens were read from the cache on the first request after a task boundary and 81% on the other requests. Over the whole of the long runs, 85% of prompt tokens were read from the cache with the prune and 85% with context editing, against 95% with no lever.

## Next steps

<CardGroup cols={2}>
  <Card title="Prompt caching" icon="database" href="https://platform.claude.com/docs/en/build-with-claude/prompt-caching">
    The largest free win on this page: setup, lifetimes, and diagnostics.
  </Card>

  <Card title="Effort" icon="gauge" href="https://platform.claude.com/docs/en/build-with-claude/effort">
    Trade intelligence for latency and cost within a single model.
  </Card>

  <Card title="Choosing the right model" icon="settings" href="https://platform.claude.com/docs/en/about-claude/models/choosing-a-model">
    Evaluate capability, speed, and cost across the Claude model family.
  </Card>

  <Card title="Session budgets" icon="coins" href="https://platform.claude.com/docs/en/managed-agents/budgets">
    Put a hard dollar cap on a Managed Agents session.
  </Card>

  <Card title="Pricing" icon="dollar-sign" href="https://platform.claude.com/docs/en/about-claude/pricing">
    See current per-token pricing for every Claude model.
  </Card>

  <Card title="Cookbook: cost optimization on the Claude API" icon="book" href="https://platform.claude.com/cookbook/cost-optimization-cost-optimization">
    Apply these levers one at a time to a working agent in a runnable notebook, with cost per task after each step.
  </Card>

  <Card title="Webinar: Building on the Claude Platform" icon="play" href="https://www.anthropic.com/webinars/building-on-the-claude-platform-claude-fable-5-and-model-orchestration-patterns">
    Watch a walkthrough of the advisor and orchestrator patterns.
  </Card>
</CardGroup>
