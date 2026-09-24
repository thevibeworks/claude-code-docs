---
title: Optimizing for cost and intelligence
url: https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence
description: Balance cost and intelligence on the Claude Platform, with measured results for prompt caching, effort, model choice, budgets, and multi-model strategies.
---

When a workload moves from prototype to production, cost becomes a first-class design constraint. The most capable model can be too expensive at scale, and the least expensive model can fall short on quality. Managing cost well means understanding how each cost lever affects output quality, because some levers trade against quality and some don't. The Claude Platform gives you direct control over that tradeoff. You choose the model, the effort level, and the architecture for each request, which lets you place a workload almost anywhere on the cost-to-intelligence frontier.

Cost and intelligence are usually pictured as a frontier where one buys the other. The first group of levers on this page moves a workload toward that frontier by cutting cost without touching quality; only the second group moves along it:

![Schematic of the cost-to-intelligence frontier: one arrow cuts spend at the same quality, the other trades quality for cost](https://platform.claude.com/docs/images/cost-intel-frontier.png)

The levers come in two kinds:

* **Free wins** cut spend without touching quality: prompt caching, token hygiene, a prompt audit against the model you are running, [batch processing](https://platform.claude.com/docs/en/build-with-claude/batch-processing) at 50% off for work that can wait up to 24 hours, and [workspace spend limits](https://platform.claude.com/docs/en/api/rate-limits#setting-lower-limits-for-workspaces) as the backstop.
* **Tradeoffs** exchange cost for intelligence: model choice, effort, output caps and task budgets, an elapsed-time clock, and multi-model architectures.

Each lever comes with measured results and the rule for when it pays. In Anthropic's measurements, prompt caching was the largest lever by a wide margin: it cut agent-loop cost by a factor of 2.7 to 5.3 on this guide's benchmarks and cut a small triage agent's bill by 83%, or 88% with input trimming added. The multi-model levers are narrower; a second model paid off in two shapes, an advisor and an orchestrator.

## Start here

Match your situation to a row.

| Your situation                                   | Do this                                                                                                                                                                                                                                                                                                                                                                                                      | Where                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Any workload, any model                          | Turn on prompt caching and trim unneeded tokens; both are free                                                                                                                                                                                                                                                                                                                                               | [Cache repeated context](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#cache-repeated-context) · [Trim tokens](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#trim-input-and-context-tokens) |
| A person waits between turns                     | Use the 1-hour cache duration once about 1 turn in 20 follows a pause between 5 minutes and an hour and few gaps run over an hour. On Claude Fable 5.1, keep the 5-minute cache warm while pauses run minutes, and buy the 1-hour duration when pauses run toward an hour. On Claude Opus 5.5, keep the 5-minute cache warm instead when only a turn or two in 20 follow a pause of up to about half an hour | [Pick the cache duration](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#pick-the-cache-duration)                                                                                                                                           |
| Costs are too high; quality is fine              | Sweep effort down on your current model                                                                                                                                                                                                                                                                                                                                                                      | [Tune effort](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#tune-effort)                                                                                                                                                                   |
| You are not on the latest model                  | Upgrade; in Anthropic's measurements each newer model solved at least as many tasks as the one before it, usually for less per solved task                                                                                                                                                                                                                                                                   | [Upgrade the model](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#upgrade-the-model)                                                                                                                                                       |
| You are choosing or switching models             | Compare on cost per completed task, not per token                                                                                                                                                                                                                                                                                                                                                            | [Compare models](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#compare-models-on-cost-per-task)                                                                                                                                            |
| Quality isn't good enough                        | If you lowered effort, restore it; otherwise try the next tier up at `low` effort                                                                                                                                                                                                                                                                                                                            | [Tune effort](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#tune-effort) · [Compare models](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#compare-models-on-cost-per-task)                  |
| Attempts end with `stop_reason: max_tokens`      | Raise `max_tokens`; 64,000 covered all but 2 of 14,000 turns measured at the default effort, and 128,000 cost nothing extra per solved task                                                                                                                                                                                                                                                                  | [Set budgets](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#set-budgets-and-output-caps)                                                                                                                                                   |
| You can check outputs (tests, a verifier)        | Run everything at low effort and re-run failures at `high`; on the coding benchmark measured, the pass rate held at about half the cost                                                                                                                                                                                                                                                                      | [Re-run failures](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#re-run-failures-at-higher-effort)                                                                                                                                          |
| Agent loops with a few very costly runs          | Set a task budget (beta; check the support table for which models), a Claude Managed Agents session budget, and a workspace spend limit                                                                                                                                                                                                                                                                      | [Set budgets](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#set-budgets-and-output-caps)                                                                                                                                                   |
| You want agent runs to finish sooner             | Tell the model that time matters, and show it the elapsed time; on DRACO, HLE, and an internal physics set, runs took 33% to 69% less time at a 28% to 54% lower cost per task, with scores up to 1.9 points lower                                                                                                                                                                                           | [Show the model elapsed time](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#show-the-model-elapsed-time)                                                                                                                                   |
| A lower-cost model stalls only on hard decisions | Add a frontier advisor. It pays off when priced well above the executor and actually consulted, so first price the advisor's model alone at low effort and measure the consult rate                                                                                                                                                                                                                          | [Advisor strategy](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#advisor-strategy-escalate-hard-decisions)                                                                                                                                 |
| The work exceeds one context window              | Delegate partitions to cheaper workers                                                                                                                                                                                                                                                                                                                                                                       | [Orchestrator strategy](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#orchestrator-strategy-delegate-bulk-work)                                                                                                                            |

These results are Anthropic-internal ([Benchmarks referenced](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs)) and directional, not guarantees, so measure on your own workload with the [four-step method](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#measure-on-your-own-workload).

## Cut spend without losing quality

Prompt caching, token hygiene, batch processing, and a prompt audit against your current model all lower what you pay without lowering output quality. Two caveats apply: batch processing trades latency for its discount, and context editing, a token-hygiene lever, cost more than it saved in the run measured in this section.

### Cache repeated context

#### Why caching comes first

Turn on [prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) before any other lever, because every turn of an agentic task resends the entire growing conversation: system prompt, tool definitions, and every prior turn. A 40-turn task sends its first turn 40 times, so task cost grows with roughly the square of turn count. Caching does not stop the resending, but each resend costs about a tenth as much and processes faster: the prefix is billed at the [cache-read rate](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#pricing), a tenth of the input price, and each turn pays the 1.25x cache-write rate only for what is new.

**What good looks like.** Over a full day of real traffic, agent loops read a median 84% of their input from the cache, and the top 10% of harnesses, coding or not, read 94% or more[17](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs). Deep in a task, a well-built loop pays full price on under 1% of its input. Below about 80%, look for something breaking the cache (see [What breaks the cache](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#what-breaks-the-cache)).

Across Anthropic's measured runs, cache reads are routinely the largest single component of task cost, making caching worth more than most model-choice decisions. Anthropic priced the DeepResearch Bench II[7](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs) runs with and without caching:

![Dumbbell chart, DeepResearch Bench II: with caching, Claude Fable 5.1 falls from $37.94 to $7.12 per task and Claude Sonnet 5 from $3.20 to $1.20](https://platform.claude.com/docs/images/cost-intel-caching.png)

The cache's default lifetime is 5 minutes and an agent loop's turns are seconds apart, so the discount applies to most tokens on every turn. The caching chart's runs read 79% to 90% of their input tokens from the cache. The saving varies with episode depth, because shorter loops re-read less, but caching stayed the largest single lever on every model and benchmark measured.

#### Pick the cache duration

If your loop waits on a person between turns, use the [1-hour cache duration](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#1-hour-cache-duration). It costs more to write (2x the input price instead of 1.25x). A miss on either duration bills the whole prefix at the write price instead of the read price, so the longer duration pays off once a few turns per session follow a pause between 5 minutes and an hour.

To decide, count the gaps between consecutive requests in a conversation:

* More than about 1 gap in 20 falls between 5 minutes and an hour, and gaps over an hour are rare: use the 1-hour duration. On Claude Opus 5.5, when only 1 or 2 gaps in 20 fall in that range and none lasts more than about half an hour, keep the 5-minute cache warm instead, with the keep-alive requests described below.
* Turns arrive seconds apart: stay on the 5-minute default. When nothing paused, it cost 15% less than the 1-hour setting on Claude Sonnet 5 and about 15% to 18% less on Claude Opus 5.5.
* Gaps over an hour are common: stay on the default. A gap over an hour expires both durations, and the 1-hour setting then re-writes the prefix at its higher write price, so it loses on each of those gaps. Of your pauses longer than 5 minutes, if about 60% or more also run past an hour, stay on the default; the 1-hour duration pays only when at least about 40% of long pauses end within the hour.

Anthropic measured the triage job from [Trim input and context tokens](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#trim-input-and-context-tokens) with pauses inserted before some turns to simulate a person's delay[16](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs). On Claude Sonnet 5 and Claude Opus 5.5, the 1-hour cache became the cheaper setting once about 1 turn in 30 followed a pause, so the 1-in-20 rule leaves a margin, and the gap widens quickly past the crossover because every paused turn on the 5-minute setting re-writes the whole prefix. Every current model uses the same cache-write multipliers, and every model but Claude Fable 5.1, Claude Mythos 5.1, and Claude Opus 5.5 the same read price, so the crossover is in the same range on the other models; Fable 5.1 is the case covered next. Accuracy stayed within run-to-run noise in every cell. The turn after a pause kept its warm-cache latency on the 1-hour setting (measured on Claude Sonnet 5 and Claude Opus 5, not on Claude Opus 5.5). The following chart plots cost per session against the share of paused turns on Claude Sonnet 5:

![Line chart: cost per triage session by share of turns after a pause; the 1-hour cache is cheaper past about 1 turn in 30](https://platform.claude.com/docs/images/cost-intel-cache-ttl.png)

Anthropic also measured extra requests that keep the 5-minute cache warm. On Claude Sonnet 5 they cost about 8% less than the 1-hour duration when 1 turn in 20 followed a pause, but about the same at 2 in 20; on Claude Opus 5, the previous Opus model, they saved nothing measurable. With a pause of 6 minutes or more before every turn they cost more on both models. Because the Claude Sonnet 5 saving was gone by 2 turns in 20, use the 1-hour duration instead on Claude Sonnet 5 and Claude Opus 5.

On Claude Fable 5.1 the cheapest setting is a different one. Its [cache read](https://platform.claude.com/docs/en/about-claude/pricing#prompt-caching) costs 0.025x the input price ($0.25 per million tokens) while its cache writes keep the standard multipliers, so a keep-alive request that re-reads the prefix is cheap and the 1-hour duration's write premium is the larger bill. Anthropic measured the triage job on Claude Fable 5.1 with the same three settings[19](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs). Keeping the 5-minute cache warm cost 13% to 20% less per session than the 1-hour cache whenever pauses ran for minutes; only with pauses near 45 minutes did the 1-hour cache win, by about 12 cents a session. On Claude Fable 5.1, keep the 5-minute cache warm while a person is away for minutes, and buy the 1-hour duration when pauses run toward an hour:

![Cost charts: keep-alive beats the 1-hour cache at every point on Fable 5.1; on Opus 5.5 and Sonnet 5 only if few turns pause](https://platform.claude.com/docs/images/cost-intel-cache-keepalive-opus-5-5.png)

On Claude Opus 5.5, whose cache read costs 0.05x the input price, keep-alive requests cost 8% to 13% less than the 1-hour duration when 5% or 10% of turns followed a pause of 6 to 32 minutes (at the default effort, `medium`; 10% to 18% less at `high`), but more with a pause before every turn: about 4% to 6% more at 6-minute pauses, rising to over 50% more at 45-minute pauses. So on Claude Opus 5.5, keep the 5-minute cache warm when only a turn or two in 20 follow a pause of up to about half an hour, and otherwise follow the list at the start of this section. These measurements sent keep-alive requests with `max_tokens: 1`. For the `max_tokens: 0` request described next, Anthropic's pre-launch API tests on Claude Opus 5.5 show that it writes the cache and that the next request reads it; whether it refreshes an existing entry was not measured on Opus 5.5.

To keep the cache warm, send the previous request again with `max_tokens` set to 0 within 4 minutes of the previous request's start, and every 4 minutes after that, dropping `stream` if it was set. Count from the request's start, not its response's end: the [cache's 5-minute lifetime](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#how-prompt-caching-works) runs from the start of the request that wrote or refreshed the entry, so time the response spent generating counts against it. That is the [pre-warming request](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#pre-warming-the-cache): it refreshes the cache's lifetime, generates nothing, and bills only the cache read. Do not change a byte of the prefix, and do not use `max_tokens: 1`, which samples a token for no reason. Re-send the request's headers as well as its body: if your requests carry an `anthropic-beta` header (for a [task budget](https://platform.claude.com/docs/en/build-with-claude/task-budgets), say), the keep-alive request needs the same header, or the beta-gated fields in the replayed body are rejected. A `max_tokens: 0` request is rejected when the request sets `thinking.type: "enabled"` (the default adaptive thinking on Claude Fable 5.1 is fine), structured outputs, or a forced tool choice ([its limitations](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#limitations)); on those workloads, buy the 1-hour duration instead. A `max_tokens: 0` request is also rejected when it carries the top-level `compaction` parameter, so don't re-send a compaction request from [compaction on demand](https://platform.claude.com/docs/en/build-with-claude/compaction-on-demand) as a keep-alive request.

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

Setup takes little work. [Automatic caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#automatic-caching) places breakpoints for you; otherwise, the [Claude API skill](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/claude-api-skill) that ships with Claude Code can add caching to an existing integration from one prompt. The following excerpt shows the skill adding it to the harness that produced these measurements:

```text wrap
$ claude
> /claude-api add prompt caching to this integration

Done. Prompt caching is now wired into the harness. Two changes:

- build_system() now adds cache_control: {"type": "ephemeral"} to the
  system block. Since the API renders tools -> system -> messages, this
  one breakpoint caches the entire static prefix -- the full tool array
  plus the system prompt.
- apply_moving_cache_breakpoints() strips any stale markers, then marks
  the last content block of the two most recent user turns. The older
  marker is the read point matching the prefix the previous request
  cached; the newer one extends the cache for the next request.

That's 3 breakpoints total, under the limit of 4.
...
```

Those breakpoint placements follow the standard pattern in [Explicit cache breakpoints](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#explicit-cache-breakpoints).

#### What breaks the cache

Several things can break your cache during a task. Anything that changes per request, such as a timestamp or a queue position, placed ahead of the stable prefix turns every request into a full cache write: on the triage run in [Trim input and context tokens](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#trim-input-and-context-tokens), a 25-token status line at the front of the system prompt cost $4.24 per run instead of $0.59, more than running with caching off. Keep per-request text in the newest user turn.

The cache is a byte-exact prefix match over the request in order (tools, then system prompt, then messages), so a change anywhere invalidates everything after it. Changing [`effort`](https://platform.claude.com/docs/en/build-with-claude/effort) or the thinking configuration between requests invalidates the cache from that point onward, and on some models the tools and system prompt ahead of it as well; any edit to the system prompt invalidates the cache from that point onward; setting or changing an output format invalidates the cache for the whole conversation; adding, removing, or reordering a tool definition invalidates all of it. The [prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#what-invalidates-the-cache) page lists these cases, apart from the output format, which [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs#prompt-modification-and-token-costs) covers. On the most recent models, change instructions with a [mid-conversation system message](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages), a `{"role": "system"}` message appended to `messages`, instead of editing the top-level `system` field: the cached prefix stays intact. Check that page for which models support it. On models that support it, a [per-message effort change](https://platform.claude.com/docs/en/build-with-claude/effort#change-effort-mid-conversation-beta) leaves the cached prefix intact too. The stakes are highest on Claude Fable 5.1 and Claude Mythos 5.1, where a break re-writes the prefix at 1.25x the input price instead of reading it at 0.025x. On a 100,000-token prefix, one broken turn there costs $1.25 instead of $0.03, 50 times the read; on Claude Opus 5.5 it costs $0.50 instead of $0.02, 25 times, and on the other current models 12.5 times.

Anthropic measured this on the triage agent's long sessions[18](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs). An effort change and an added tool made mid-session rewrote 39,000 and 60,000 cached tokens, and those sessions cost $0.95 per session. The same two changes on the first request after compaction cost $0.75, and on the request that triggered the compaction $0.92, because the compaction's summarization pass then re-processed the 81,000-token context at the cache-write price: that summarization pass cost $0.21, against $0.04 when the same changes came one request later, with accuracy within run-to-run noise in every arm:

![Bar chart, cost per triage session: $0.81 no changes, $0.95 mid-session changes, $0.92 on the compaction request, $0.75 after](https://platform.claude.com/docs/images/cost-intel-compaction-timing.png)

Changing a [task budget](https://platform.claude.com/docs/en/build-with-claude/task-budgets) partway through invalidates any cached prefix that contains the budget value, so set it once, on the first request. Every [context editing](https://platform.claude.com/docs/en/build-with-claude/context-editing#context-editing-and-prompt-caching) pass invalidates the prefix from the point it clears and the next request pays to re-cache everything after it, so clear in a few large batches rather than many small ones. On Claude Fable 5.1 and Claude Mythos 5.1 each of these costs 50 times the read price per token, so they matter most there. Make every cache-invalidating change at natural breaks, then confirm cache reads have not dropped; if they have, [cache diagnostics](https://platform.claude.com/docs/en/build-with-claude/cache-diagnostics) shows where the prefix diverged.

### Trim input and context tokens

Most agent requests carry tokens that never influence the answer. Trimming them rarely costs output quality, although not every lever here saved money when measured. Two places to look:

* **Input trimming.** [Dynamic filtering](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool#dynamic-filtering) in the web fetch tool keeps boilerplate out of fetched pages, [image resizing](https://platform.claude.com/docs/en/build-with-claude/vision#evaluate-image-size) right-sizes vision inputs, and [tool search with deferred loading](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool) loads tool definitions only when needed (measured later in this section). [Programmatic tool calling](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling) lets Claude run several tool calls from code so only the filtered result enters the context; its documentation reports 24% fewer input tokens on agentic search benchmarks, with a higher score. [Manage tool context](https://platform.claude.com/docs/en/agents-and-tools/tool-use/manage-tool-context) compares tool search, programmatic tool calling, prompt caching, and context editing.
* **Context lifecycle.** [Context editing](https://platform.claude.com/docs/en/build-with-claude/context-editing) clears stale tool results, and [automatic compaction](https://platform.claude.com/docs/en/build-with-claude/compaction-threshold) with its threshold stops long loops from carrying their whole history forward.

The levers interact with the cache and each other, so judge them by net effect, and use [cache diagnostics](https://platform.claude.com/docs/en/build-with-claude/cache-diagnostics) to confirm your cached prefix survives each change. Anthropic measured them on an issue-triage agent working through 20 real bug reports with screenshots from a public repository, and on a longer variant of the same job with 2.6 times the tokens. With caching on, input trimming (image resizing and tool search) took a further 26% off the short run and 21% off the long one.

#### Defer unused tool definitions

Every tool definition attached to a request is input on every turn, and a few MCP servers add up to hundreds of them. Anthropic ran the triage agent with its own two tools plus a catalog of real tool definitions from public MCP servers, for a total of up to 502 tools, loading all of them or marking the extras `defer_loading` behind [tool search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool):

![Line chart: with all tools loaded, run cost rises from $0.55 to $1.02 at 502 tools; with tool search it stays at $0.56](https://platform.claude.com/docs/images/cost-intel-tool-search.png)

With every definition loaded, the run cost nearly doubled as the catalog grew, tracking the schema tokens on each request. With tool search it stayed flat at every catalog size, 45% less at 502 tools. Accuracy was 15 to 18 of 20 in every cell either way, and the model never called a wrong tool, so at this scale the catalog costs money, not correctness. The same holds for tools that come through the [MCP connector](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector): with a public GitHub MCP server attached, deferring its toolset (`default_config: {defer_loading: true}`) cut the run 20% at the same accuracy.

#### Keep data files out of the prompt

When the model has to compute over a table, upload it with the [Files API](https://platform.claude.com/docs/en/build-with-claude/files) and let the model query it with [code execution](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool) instead of pasting it in. Anthropic asked 25 aggregate questions[15](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs) (sums, filtered counts, group-bys, and a date filter) over a 1,862-row public CSV, with the answers computed by pandas:

![Scatter chart: with the file uploaded and code execution, 25 of 25 correct at $0.40; pasted into the prompt, 6 of 25 at $5.01](https://platform.claude.com/docs/images/cost-intel-data-files.png)

Pasted into the prompt, the table is about 91,000 input tokens on every request, and Claude Sonnet 5 answered 6 of 25 questions correctly. Uploaded, with code execution, it answered all 25, and the run cost about a twelfth as much. Claude Opus 5 showed the same pattern.

#### Manage the context lifecycle

The context levers only pay on a session long enough to need them:

![Bar chart by run length: context editing adds 74% on the short run; compaction saves 32% and pruning 39% on the long](https://platform.claude.com/docs/images/cost-intel-hygiene.png)

On the 20-issue run they saved nothing, and context editing cost 74% more. On the long run the prune saved 39% and compaction 32%, while context editing changed nothing. The prune is a few lines you write yourself: at each task boundary, replace large stale tool results with a one-line extract. It caches well because the edits sit at the tail of the conversation, where the next task adds new content anyway: 89% cache reads on the first request after a boundary and 81% on the requests between boundaries. Run-wide, the prune and context editing cache about equally well. The prune is cheaper because context editing rewrites content mid-task that the prune deletes (about two thirds of the gap) and because it keeps the context about half the size (the other third). If you use context editing, [clear in a few large batches](https://platform.claude.com/docs/en/build-with-claude/context-editing#context-editing-and-prompt-caching). The prune, adapted from the harness:

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

The [Batch API](https://platform.claude.com/docs/en/build-with-claude/batch-processing) takes 50% off every token of a request, including cached ones, in exchange for results arriving any time within 24 hours. Route every request no one is waiting on through a batch, and keep the interactive path for the rest. Batching is the second-largest free lever after caching for unattended agent work: evaluation runs, backfills, and scheduled jobs such as a recurring run of the issue-triage agent from the [token-trimming measurement](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#trim-input-and-context-tokens). It combines with everything on this page except interactivity, but is not available for Claude Managed Agents sessions, which are interactive by design (see [Claude Managed Agents pricing](https://platform.claude.com/docs/en/about-claude/pricing#claude-managed-agents-pricing)).

### Audit prompts against the current model

Each model generation responds to prompts differently, so a prompt accumulates text written for a model you no longer use. The usual case is over-specific instruction added to compensate for an older model: "verify twice," "be maximally thorough," a mandatory step-by-step procedure, or a hand-rolled reasoning scratchpad. A newer model follows these to the letter, producing extra tool rounds and extra writing, so the bill goes up with no gain in accuracy. Auditing prompts against the model you run now, and again whenever you change models, is a free win.

The audit is one command. The [Claude API skill](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/claude-api-skill) that ships with Claude Code has a `prompt-audit` command that reads a project's prompts and request code and reports what was written for a different model. This shortened excerpt shows it run against a support-desk prompt and request code containing those patterns:

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

The effect is measurable. On a support-desk evaluation[14](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs), prompts written for Claude Opus 4.8 cost 36% more per ticket on Claude Opus 5 for no change in accuracy. Running the audit over the same prompts made Opus 5 both cheaper than the unaudited version (by 14%) and more accurate (97% of tickets, up from 92%, a gain outside the noise). On the Claude Sonnet 4.6 to Claude Sonnet 5 migration, the audit took 14% off at the same accuracy:

![Scatter chart, support-desk evaluation: the old prompt costs more on the new model; audited, it is cheaper and as accurate](https://platform.claude.com/docs/images/cost-intel-prompt-audit.png)

The two kinds of stale text have different costs. Instructions the new model follows too literally cost money: removing "verify twice" cut Opus 5's cost per ticket by a third, and removing "be maximally thorough" almost as much. Text that no longer fits the model costs accuracy instead: a retired thinking setting, contradictory rules, and a hand-rolled scratchpad that conflicts with the model's own thinking each restored 7 to 11 points on Opus 5 when removed:

![Bar charts per legacy pattern: over-obeyed instructions cost money; broken settings and contradictory rules cost accuracy](https://platform.claude.com/docs/images/cost-intel-prompt-audit-patterns.png)

The same patterns tend to appear in tool descriptions and skills, which are worth auditing too.

## Trade cost against intelligence

These levers set where a single model sits between cost and intelligence: model choice, effort, re-running failures at a higher setting, the budgets and caps it works within, and whether it can see how much time has passed. Start with an effort sweep on your current model ([Tune effort](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#tune-effort)). From lowest to highest cost and capability, the current models are Claude Haiku 4.5, Claude Sonnet 5, Claude Opus 5.5, and Claude Fable 5.1 (the frontier model); [Models overview](https://platform.claude.com/docs/en/models/overview) has the full lineup and prices.

### Compare models on cost per task

Price lists are written per token, and per token the frontier model looks expensive: Claude Fable 5.1's per-token price is several times Claude Sonnet 5's. You pay for completed tasks, though, so compare models on cost per completed task. A more capable model finishes a task with less work: fewer turns, less searching, less re-reading of its own context, and less backtracking. The per-token premium is often overwhelmed by doing less of everything.

Anthropic measured this on the SWE-bench Pro[3](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs) subset, priced as a customer is billed:

![Scatter chart, SWE-bench Pro: Claude Opus 5.5 at its default matches Claude Fable 5.1's default for about a fifth of the cost](https://platform.claude.com/docs/images/cost-intel-cost-per-task-opus-5-5.png)

Claude Fable 5.1 at `low` effort solved 88.6% of tasks for $0.54 per solved task, against 77.4% for $0.84 from Claude Sonnet 5 at its default: 11 more points for 35% less per solved task, despite a per-token price five times higher. It does not always win, though. On the same subset, which Claude Opus 5.5 and Claude Fable 5.1 both largely saturate and whose scores are not comparable to the public leaderboard, Opus 5.5 at its default, `medium`, matched Fable 5.1 at its default (92.8% against 92.3%, inside run-to-run noise) for about a fifth of the cost per solved task ($0.22 against $1.19). At `low`, Opus 5.5 solved 87.4% for $0.12. These figures use the 478 problems described in reference 3. And on long research loops the frontier model does more work, not less: on DeepResearch Bench II[7](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs), Fable 5.1 at `low` scored 10 points above Sonnet 5 (66% against 56%) at about four times the cost per task ($4.66 against $1.20), because it runs a longer research loop over a larger context. Claude Opus 5 at its default scored 71% on the same basis for $6.71 per task, above Fable 5.1 at its default (65% for $7.12), so on research too Fable 5.1 earns its price only at `low`.

For most agent workloads, start with Claude Opus 5.5 at its default effort (`medium`), and use Claude Fable 5.1 for demanding reasoning and long-horizon agentic work, or when your evals on Claude Opus 5.5 at higher effort still fall short. On the SWE-bench Pro subset, Opus 5.5 at its default matched Fable 5.1 at its default for about a fifth of the cost per solved task, as noted earlier. On the coding benchmark in [Advisor strategy](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#advisor-strategy-escalate-hard-decisions), it scored 86.6% against 84.2% for Fable 5.1 at `medium` (a single Fable 5.1 run), for under a third of the cost per attempt ($0.84 against $2.68). On Chartography[13](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs), a chart-reading benchmark, Opus 5.5 at `low` scored 68.7 for about $0.03 a chart, against 62.5 for $0.15 from Fable 5.1 at `low` and 49 for $0.16 from Claude Opus 5 at `low`. At the other end, Claude Haiku 4.5 answered GPQA Diamond[9](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs) questions at about a fifth of Claude Opus 5.5's cost per question, with 63% accuracy compared with 92% for Opus 5.5, and fell much further behind on long coding tasks. It fits high-volume work with checkable outputs, not long agentic loops.

The ranking flips by workload, and no price list tells you which way. Price every candidate in cost per completed task on your own traffic, including Claude Opus 5.5 at its default effort and the frontier model at reduced effort.

Price the tail of your workload, not the median: compare models on the hardest tenth of your tasks, not the typical one. On the typical task every model looks similar and the cheapest looks best, but the bill is decided by the tasks the cheaper model fails, because a failed task still bills its tokens, then the retry, then whatever the failure costs downstream. The tail is also where the money goes even when nothing fails. On a 20-problem WideSearch[1](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs) run, two problems carried 43% of the spend:

![Bar chart of 20 WideSearch problems ranked by cost: the top two carry 43% of spend and the cheapest half 10%](https://platform.claude.com/docs/images/cost-intel-tail.png)

The [multi-model strategies](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#combine-models) exist to spend frontier intelligence on that tail without paying frontier rates for the rest.

### Upgrade the model

If you are a model or two behind, the cheapest lever is the model string. Anthropic ran recent Claude Opus, Claude Sonnet, and Claude Fable models through the same harness on the SWE-bench Pro[3](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs) subset, each at its shipped defaults and priced at list rates, and ran the Opus line again on Terminal-Bench 3[20](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs):

![Two charts of cost per solved task against tasks solved: on SWE-bench Pro every model solves most tasks and the upgrade steps are small; on Terminal-Bench 3 the Opus ladder falls from $183 to $63 to $28 per solved task](https://platform.claude.com/docs/images/cost-intel-upgrade-ladder.png)

Anthropic prices Claude Opus 4.7, Opus 4.8, and Opus 5 identically per token, so any difference among them comes from how much work each model does per task: priced as a customer is billed, Claude Opus 4.8 solves the same share of tasks as Claude Opus 4.7 for 14% less per solved task, and Claude Opus 5 then solves 12 more points of tasks at 21% more per solved task. Claude Opus 5 at `low` effort beats Opus 4.8's default on this benchmark for about 30% of its cost per solved task, so the cheapest upgrade is the new model at a lower setting. Sonnet 5's saving comes from its lower per-token price, which more than offsets the extra tokens it uses per task compared with Sonnet 4.6: 15% less per solved task for 5 more points. The frontier tier gained the same way: Claude Fable 5.1 matches Claude Fable 5's score for 43% less per solved task, most of it the lower cache-read price. That direction is not guaranteed: on DeepResearch Bench II[7](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs) the same upgrade costs 41% more per task at `high` (79% more at `low`) for its 2 to 3 extra points on the tasks clean in every arm (reference 7), because the new model does more work per task there. The input and output prices are the same and the cache read is 4x cheaper, so measure the upgrade on your own workload before assuming it saves.

On harder work the gap widens. On Terminal-Bench 3[20](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs), where the tasks are hard enough that pass rate rather than tokens sets the bill, Claude Opus 4.7, Opus 4.8, and Opus 5 each spend $8 to $15 per task but solve 7%, 15%, and 41% of tasks, so cost per solved task falls from $183 to $63 to $28 up the ladder. The 21% premium Claude Opus 5 carries over Opus 4.8 on the saturated coding subset becomes a 56% saving on Terminal-Bench 3, where the older model mostly fails: the more your workload defeats the old model, the more the upgrade saves per result.

Compare on cost per solved task, not per token: the same text costs about 30% more tokens on Claude Opus 4.7 and later, so a per-token comparison makes the newer models look more expensive by construction.

### Tune effort

Effort is the most direct way to tune a model to your task. The `effort` parameter governs how much thinking, tool calling, and self-verification the model does, and `high`, the default on most models, suits demanding tasks; Claude Opus 5.5 defaults to `medium`. Cost scales with all that activity; accuracy scales only with the part your task needs. Below the model's ceiling, the highest effort levels pay for depth the task never uses.

On the research and knowledge-work benchmarks (WideSearch[1](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs), DeepWideSearch[6](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs), BrowseComp[4](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs), and GDPval[2](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs), all with Claude Fable 5), the curve of accuracy against cost is nearly flat: `low` gave up 1 to 3 points for a third to a half off the cost per task, `medium` matched the default's accuracy at about 70% to 87% of its cost, and the default bought nothing measurable over `medium` on any of the four. On DeepWideSearch, `low` also matched an orchestrator with a Claude Sonnet 5 worker at 29% lower cost: lowering effort beat an architecture change.

Lower effort settings are often faster, which matters when latency is the constraint. In these runs, `low` took 4.5 minutes per problem on DeepWideSearch, compared with 7.9 minutes at the default. On the [corpus benchmark](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#orchestrator-strategy-delegate-bulk-work), whose input does not fit in any single context window, Fable 5.1 took 15.2, 17.5, and 19.9 hours per episode at `low`, `medium`, and `high`.

Long-horizon coding is where effort genuinely buys accuracy. On SWE-bench Pro[3](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs), measured against `high`, Claude Opus 5.5 scored about 2.5 points lower at its default, `medium`, for about 70% of the cost, and about 8 points lower at `low` for about a third of the cost; `xhigh` scored about 1.4 points higher for 2.5 times the cost of `high`: a real tradeoff, which [re-running failures at higher effort](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#re-run-failures-at-higher-effort) turns back into a saving. This chart plots accuracy against cost for the research and knowledge-work benchmarks and for SWE-bench Pro:

![Line charts of accuracy against cost by effort: nearly flat for Fable 5 on research work, steep for Opus 5.5 on SWE-bench Pro](https://platform.claude.com/docs/images/cost-intel-effort-sweep-opus-5-5.png)

Two consequences follow. First, draw this curve for your own workload before you add a second model: in these internal measurements, a multi-model configuration that looked cheaper than the default single model cost more than that same model at lower effort. Second, this curve is the single-model baseline any multi-model strategy must beat, so [step 2 of measuring on your own workload](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#measure-on-your-own-workload) baselines across effort levels.

Hard work does not automatically need high effort. On DeepResearch Bench II[7](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs), Claude Fable 5.1 scored nearly the same at `low`, `medium`, and `high` while the cost per task rose from $4.66 to $7.12, so raising the effort in this case does not increase the quality of the output noticeably; on the 21 tasks clean in every arm (reference 7), Claude Fable 5 was flat across effort too, though the chart's 33-task basis, which drops each model's own cut-short attempts, shows it climbing. Measure the curve on the model you ship, not the one you measured last:

![Line chart of rubric score against cost per task on DeepResearch Bench II: on Claude Fable 5.1 higher effort bought no score, only cost](https://platform.claude.com/docs/images/cost-intel-effort-limit.png)

The task description alone does not reveal which kind of workload you have, so sweep two or three effort levels on a sample of your own traffic and read the answer off the curve. Test each level in a separate session: changing top-level effort mid-session invalidates the cache (see [Cache repeated context](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#cache-repeated-context)) and distorts the comparison. For parameter details, see [Effort](https://platform.claude.com/docs/en/build-with-claude/effort).

### Re-run failures at higher effort

When a task's outcome is checkable, the cheapest policy on the effort curve is not a fixed setting: run every task at a low setting and re-run only the failures at a higher one.

Anthropic computed this policy task by task from the effort runs on the SWE-bench Pro[3](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs) subset in [Tune effort](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#tune-effort). With Claude Opus 5.5 at `low`, 13% of tasks failed; with those re-run at `high`, about 97% passed for about $0.17 each, against 95.3% for $0.29 running everything at `high`: a slightly higher pass rate for a little over half the cost, counting the failed cheap attempts. Starting at `medium` instead solved about 97% for about $0.24. Most of the small lift is the second attempt (re-running the failures of one `high` run at `high` scores about the same, for more money), so use this policy for the saving, not the lift:

![Chart, SWE-bench Pro, Opus 5.5: low or medium effort with failures re-run at high matches any fixed effort for less than high](https://platform.claude.com/docs/images/cost-intel-escalation-opus-5-5.png)

Two conditions apply. First, you need a failure signal (here, the benchmark's own tests); a checker that passes bad work lets those failures through. Second, every first-pass failure takes two runs' worth of wall-clock time, so the saving is paid for in latency on the failures.

### Set budgets and output caps

Most agentic task runs are cheap, but a minority spend many times the median cost on searching, re-verifying, and over-testing. A [task budget](https://platform.claude.com/docs/en/build-with-claude/task-budgets) targets that tail. The model sees a live token countdown for the whole task and self-regulates, trimming low-value searches, skipping redundant verification, and wrapping up instead of spiraling.

Anthropic measured pass rate and cost per task on SWE-bench Pro[3](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs) with Claude Fable 5.1 as the budget tightened:

![Line chart on SWE-bench Pro: pass@1 falls a few points as task budgets tighten while cost per task drops by 44% to 58%](https://platform.claude.com/docs/images/cost-intel-budget-pareto.png)

A generous budget cut cost per task 44% for about 3 points of pass rate, at the edge of run-to-run noise, and the tightest allowed budget cut it 58% for 6 points. Budgets bought efficiency here, at a price in pass rate that grows as the budget tightens.

Three controls do three different jobs. A task budget saves money, because the model sees it. `max_tokens` is a safety cap: lowering it cut cost per attempt without lowering cost per solved task. On Claude Managed Agents, a session budget is the hard dollar stop behind both. Set all three: a task budget, a high `max_tokens`, and a session cap for the run you never want on a bill, with a [workspace spend limit](https://platform.claude.com/docs/en/api/rate-limits#setting-lower-limits-for-workspaces) as the final backstop.

* **Task budgets** are in beta (beta header `task-budgets-2026-03-13`) on the most recent models; check the [support table](https://platform.claude.com/docs/en/build-with-claude/task-budgets#feature-support) for which. Start near your loop's 90th-percentile token usage, then tighten ([Choosing a budget](https://platform.claude.com/docs/en/build-with-claude/task-budgets#choosing-a-budget) shows how to collect that distribution). Budgets below the current 20,000-token floor are rejected, and very tight budgets can produce refusal-like behavior. Set the budget once, on the first request, because a mid-task change [invalidates the cache](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#cache-repeated-context). The budget is advisory, steering the model rather than stopping it, so verify adherence on your workload.
* **`max_tokens`** caps a single response, invisibly to the model, so lowering it does not make the model economize. The turns that needed the room are discarded and still billed. On an internal repository-task benchmark[12](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs), a 16,384-token cap ended about a quarter of Claude Opus 5.5's attempts and 43% of Claude Fable 5.1's, each at its default effort. Only 1 of the 66 capped Opus 5.5 attempts and 9 of the 117 capped Fable attempts still passed. Capped runs spent less per attempt but bought proportionally fewer solves, so cost per solved task was about the same as at 64,000 (on Fable 5.1, $21 against $22; on Opus 5.5, within 1%). At 64,000, 2 of about 14,000 Claude Fable 5.1 turns at its default effort were still cut off (no Claude Opus 5.5 turn was), and Fable 5.1 solved 58.5% of tasks instead of 36.3% (on a separate cut of the SWE-bench Pro[3](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs) subset, described in reference 12, no difference: 94 of 100 at either cap). Retrying capped attempts rarely helps: at the same cap most of them fail again, and at a higher one you also pay for the wasted attempt. Set `max_tokens` to 64,000 for agentic work, or to 128,000, the maximum, when a single cut-off attempt is costly; at 128,000 Fable 5.1 solved 60.0% for the same cost per solved task. [Stream responses](https://platform.claude.com/docs/en/build-with-claude/streaming) that large, treat [`stop_reason: max_tokens`](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons#max-tokens) as a failure, and save money with effort and task budgets, which the model can see.
* **Session budgets on Claude Managed Agents** are the hard stop. A [session budget](https://platform.claude.com/docs/en/managed-agents/budgets) is a dollar cap on one session at list rates for tokens, searches, and session time. At the cap, the session pauses with `stop_reason: budget_reached`; raising the budget resumes it. It is platform-enforced, works on any model with a list price, including models where task budgets are not yet available, and combines with the advisory task budget. Deployments apply the same field to every run.

Ask for shorter answers. Output tokens cost five times input tokens on Claude Sonnet 5, and in an agent loop every token the model writes comes back as input on every later turn, so you pay for a long answer again and again. Anthropic ran the triage job under three final-answer instructions, three runs each, with the same model and tools. The original asked for two lines:

```text wrap
4. Finish with exactly two lines:
LABEL: <one of: bug-confirmed, needs-more-info, duplicate-candidate, feature-request, upstream-issue, perf, ui-polish>
SUMMARY: <one or two sentences for the engineering team>
```

The shorter variant asked for one:

```text wrap
4. Finish with exactly one line in this form:
DECISION | LABEL | REASON
where DECISION is one of: triage-now, needs-info, close-duplicate; LABEL is one of: bug-confirmed, needs-more-info, duplicate-candidate, feature-request, upstream-issue, perf, ui-polish; REASON is one clause under 15 words. Output nothing after that line.
```

The longer variant asked for a memo with five headed sections: problem summary, evidence, duplicate check, recommended label, and next steps. For one issue, a queued prompt that never sends after a skipped question, the first two answers were:

```text wrap
LABEL: bug-confirmed
SUMMARY: When a user submits a new prompt instead of answering an agent's pending question, the question is cancelled/skipped but the new prompt remains stuck in "QUEUED" state indefinitely since it's waiting on a response to the now-cancelled question; the queued prompt should be processed immediately after cancellation.
```

```text wrap
triage-now | bug-confirmed | Clear repro steps show prompt queues indefinitely after cancelled question.
```

![Bar chart: one-line format $0.49 per run, original two-line format $0.57, memo $1.40, all 78% to 85% correct](https://platform.claude.com/docs/images/cost-intel-output-format.png)

The one-line answer used 39% fewer output tokens than the two-line original and cost 14% less per run. The memo used six times the output tokens and cost 2.8 times the one-line answer. All three scored within run-to-run noise of each other against the gold labels, so the formats differ in what you pay far more than in what they get right. Ask for the answer you will read, not the one that looks thorough.

At the lower `max_tokens` cap both models spend less per attempt but solve proportionally fewer tasks, so cost per solved task barely moves:

![Bar charts, Opus 5.5 and Fable 5.1: a 16k max\_tokens cap costs less per attempt than 64k but about the same per solved task](https://platform.claude.com/docs/images/cost-intel-max-tokens-saving-opus-5-5.png)

Almost every turn finishes far below either cap. The rare long turn is what the higher cap buys:

![Dot plot of per-turn output for Opus 5.5 and Fable 5.1: medians a few hundred tokens, longest 61k and 128k, against the caps](https://platform.claude.com/docs/images/cost-intel-max-tokens-ladder-opus-5-5.png)

### Show the model elapsed time

A model in an agent loop can't see a clock. A [task budget](https://platform.claude.com/docs/en/build-with-claude/task-budgets) shows it how many tokens are left, but by default nothing in the request shows it how long the work has taken. Two small changes give it that signal. Add a two-sentence instruction to the system prompt that says time matters, and from the second request on, send the elapsed time before each of the model's turns.

Anthropic measured both changes together with Claude Fable 5.1 at `high` effort, on two public benchmarks, DRACO[21](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs) and HLE[22](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs), and on an internal set of 70 research-level physics problems, adapted from the public CritPt benchmark[23](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs). This page calls that set the physics set. Each of the three ran in two shapes: a single agent, and a team in which a lead agent starts helper agents of the same model that work in parallel. A score change counts as inside the margin when its 95% interval stays within a limit that Anthropic set before the runs: 1.5 points on DRACO and 2.5 points on HLE. The following chart plots score against cost per task for each configuration. A second row of bars gives each configuration's time as a ratio to the single agent at `high` effort, without retry waits. A third row gives the score change that both changes make, with its 95% interval:

![Charts, DRACO, HLE, and the physics set: both changes cut each setup's cost and time, and its score moves by under 2 points](https://platform.claude.com/docs/images/cost-intel-time-awareness.png)

**With a team of agents.** A team does more work than a single agent, so by default it costs more. On DRACO, the team cost 4.0 times as much as the single agent and took about as long (95% interval 12% less to 13% more). With the instruction and the clock on every agent, the team finished in 33% less time at a 54% lower cost per task. Its score was 1.5 points lower (95% interval 0.9 to 2.1 lower), and the far end of that interval, 2.1 points lower, is past the 1.5-point margin. On HLE, the team finished in 51% less time at a 54% lower cost per task. Its score was 1.7 points lower (95% interval 0.3 to 3.1 lower), and the far end of that interval, 3.1 points lower, is past the 2.5-point margin. On the physics set[23](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs), the team finished in 39% less time. Its cost per task was 28% lower, and that saving depends on how often the prompt cache expired between requests. With no expiry, it would be 23%. Its score was 0.2 points higher (95% interval 1.5 lower to 2.0 higher).

On DRACO, the lead started a median of 4 helpers per attempt, so the DRACO result shows a team working in parallel. On HLE and the physics set, the lead started a median of 0 helpers, so at least half of those team runs had only the lead agent. Those team results mostly show the lead agent's own behavior, not the effect of parallel helpers.

**With a single agent.** On the physics set[23](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs), the same changes cut a single agent's time by 34% and its cost per task by 34%. Its score was 0.2 points lower (95% interval 2.5 lower to 2.1 higher). On the physics set, a lower effort level saved cost but not clearly time. At `medium` effort, the single agent cost 37% less per task than at `high`, and its time was 9% less (95% interval 30% less to 16% more). It scored 3.4 points lower (95% interval 0.4 to 6.8 lower), and the interval reaches close to zero. With both changes at `high` effort, the single agent took 27% less time than at `medium` effort (95% interval 5% less to 44% less). Its cost per task was 6% more (95% interval 12% less to 27% more), and its score was 3.2 points higher (95% interval 0.1 lower to 6.5 higher).

On HLE, the same changes cut a single agent's time by 54% and its cost per task by 48%. Its score was 1.1 points lower (95% interval 2.6 lower to 0.3 higher), and the far end of that interval, 2.6 points lower, is just past the 2.5-point margin. At `medium` effort, the single agent cost 43% less per task than at `high`, took 39% less time, and scored 1.3 points lower (95% interval 2.8 lower to 0.1 higher). With both changes at `high` effort, the single agent took 25% less time than at `medium` effort (95% interval 12% less to 35% less). Its cost per task was 9% less (95% interval 21% less to 6% more), and its score was 0.2 points higher (95% interval 1.3 lower to 1.7 higher).

On DRACO, the same changes cut a single agent's time by 69% and its cost per task by 49%. Its score was 1.9 points lower (95% interval 1.1 to 2.8 lower), and the far end of that interval, 2.8 points lower, is past the 1.5-point margin. At `medium` effort, the single agent cost 25% less per task than at `high`, took 30% less time, and scored 0.7 points lower (95% interval 0.1 to 1.3 lower). With both changes at `high` effort, the single agent took 53% less time than at `medium` effort (95% interval 42% less to 63% less), and its cost per task was 31% less (95% interval 28% less to 35% less). Its score was 1.2 points lower (95% interval 0.5 to 1.9 lower), and the far end of that interval, 1.9 points lower, is past the 1.5-point margin.

On all three sets, both changes at `high` effort saved more time than `medium` effort did. On HLE and the physics set, there was no clear difference in cost, and on DRACO the cost was lower. The score was about the same on HLE. On the physics set it was 3.2 points higher, but that interval includes zero, so the difference isn't clear. So for a single agent, the clock saves more time than a lower effort level does. On DRACO, though, the single agent with both changes scored 1.2 points lower than at `medium` effort (95% interval 0.5 to 1.9 lower).

**When to use it.**

* Use both changes when an agent's time matters and a small score change is acceptable. On every configuration measured, they cut the time and cost per task, for teams and for single agents.
* Check score on your own tasks before you adopt them. On DRACO, the score was 1.5 points lower for a team and 1.9 points lower for a single agent. On HLE, it was 1.7 points lower for a team and 1.1 points lower for a single agent. On the physics set, neither score change was clearly different from zero.
* If you're already thinking about a lower effort level to save time, compare it with the clock. A single agent with both changes at `high` effort took less time than at `medium` effort: 53% less on DRACO, 25% less on HLE, and 27% less on the physics set. Its cost per task was 31% lower on DRACO, with no clear difference on HLE and the physics set.

**How to add it.** Put this instruction at the start of every agent's system prompt:

```text wrap
Time matters here: do not spend time that can be avoided, and the earlier a correct result is obtained, the better. The elapsed time so far is shown before each of your turns.
```

The second sentence tells the model that the clock messages exist. The first request carries no clock, and the measured runs used exactly this wording.

Then, before each request after an agent's first, append a [mid-conversation system message](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages) that gives the elapsed time in whole seconds, such as `Elapsed time: 412 seconds`. Count from the start of the task, not from the start of the agent. In a team, every agent reads the same clock, so the first clock a helper sees already counts the time the team spent before the helper started. In a tool loop, put the message right after the `user` message that carries the tool results, as [Placement after tool results](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#placement-after-tool-results) shows. If you send the agent a new `user` message instead, put the clock after that message.

Leave earlier clock messages where they are. Each one becomes part of the conversation history, so the cached prefix still matches on the next request (see [Combining with prompt caching](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#combining-with-prompt-caching)). Anthropic measured these plain system messages, which stay visible to the model. A [turn-scoped system message](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#turn-scoped-system-messages) would show the model only the newest clock, and Anthropic didn't measure that form.

The following example runs one agent's tool loop with both changes. It adds the clock after tool results, and it handles client tools only:

```python
import time

import anthropic

client = anthropic.Anthropic()

TIME_MATTERS = (
    "Time matters here: do not spend time that can be avoided, and the earlier a "
    "correct result is obtained, the better. The elapsed time so far is shown before "
    "each of your turns."
)


def run_agent(task, system, tools, run_tool, started_at=None):
    """Run one agent's tool loop. In a team, pass the lead's started_at to every helper."""
    if started_at is None:
        # Wall-clock seconds, so helpers in other processes can share the lead's start time.
        started_at = time.time()
    messages = [{"role": "user", "content": task}]
    while True:
        # Stream because a 128,000-token cap is too large for a non-streaming request.
        with client.messages.stream(
            model="claude-fable-5-1",
            max_tokens=128000,
            cache_control={"type": "ephemeral"},
            system=TIME_MATTERS + "\n\n" + system,
            tools=tools,
            messages=messages,
        ) as stream:
            response = stream.get_final_message()
        messages.append({"role": "assistant", "content": response.content})
        if response.stop_reason != "tool_use":
            return response
        results = [
            {
                "type": "tool_result",
                "tool_use_id": block.id,
                "content": run_tool(block.name, block.input),
            }
            for block in response.content
            if block.type == "tool_use"
        ]
        messages.append({"role": "user", "content": results})
        # A system message must follow a user turn, so the clock goes after the tool results.
        elapsed = int(time.time() - started_at)
        messages.append(
            {"role": "system", "content": f"Elapsed time: {elapsed} seconds"}
        )
```

Claude Fable 5.1 supports mid-conversation system messages. The [list of supported models](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages) covers the others. On a model without them, such as Claude Sonnet 5, you can put the same line in a text block after the last `tool_result` block in the `user` turn. Anthropic measured only the system-message form.

On Claude Managed Agents, you can send a [`system.message` event](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#sending-system-messages) with a tool result or a user message. The message applies to that turn and every later turn. So turns that follow the platform's built-in tools, such as web search, see the last clock you sent, not the current time. A `system.message` also reaches only the session's primary thread. In a [multiagent session](https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration), that is the coordinator's thread, so the worker agents never see a clock that you send this way. To show the current time before every turn, and to every agent in a team, run the agent loop yourself on the Messages API.

## Combine models

Multi-model architectures fit workloads whose task complexity varies enough that different steps are best served by different models. When your traffic mixes routine work that a smaller model handles reliably with harder steps that need frontier capability, splitting the work keeps frontier intelligence where it matters while most tokens bill at smaller-model rates. When a workload lacks that mix, because its difficulty is uniform or it is one dependent chain, a single well-tuned model is usually the better choice. Each strategy section gives the rule for telling the two cases apart.

Two strategies cover most workloads, and they differ in which model holds the main loop:

| Strategy         | Control flow                                          | Frontier model's role               | Fits                                                                                                                      | Frontier cost scales with             |
| ---------------- | ----------------------------------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| **Advisor**      | Smaller model runs the loop, escalates on demand      | Consulted for plans and corrections | Serial work that is hard in spots, such as a coding agent's many turns between a few real decisions                       | How often the executor gets stuck     |
| **Orchestrator** | Frontier model runs the loop, delegates the bulk work | Plans, dispatches, and synthesizes  | Work that fans out across genuinely independent files, documents, or cases, especially more than one context window of it | How hard the pieces are to coordinate |

### Advisor strategy: escalate hard decisions

In the advisor strategy, a lower-cost executor model runs the agent loop and performs most turns. When it hits a decision that needs deeper judgment, such as choosing an approach or recovering from a failure, it calls a higher-intelligence advisor model for strategic guidance, then continues. Most tokens are billed at executor rates, and only the occasional consultations at advisor rates.

To use it, add the [advisor tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool) to your request. This beta feature runs the whole strategy server-side in one `/v1/messages` request: the executor emits a tool call, Anthropic runs the advisor inference, and the executor continues with the advice; you write no orchestration code. On Claude Managed Agents, [give the session an advisor](https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration#give-the-session-an-advisor) by adding an `advisor` entry to the agent's `multiagent` roster; the session's primary thread consults it the same way. Claude Code supports it too; see [escalating hard decisions with the advisor tool](https://code.claude.com/docs/en/advisor).

![Diagram of the advisor strategy: an executor model runs the main loop and calls a Claude Fable 5.1 advisor on demand](https://platform.claude.com/docs/images/model-routing-advisor-strategy.png)

**What sets the payoff.** The advisor sees the task only through the executor's calls, so two things decide how much it helps.

The first is the gap between the models. The advisor can only hand over capability the executor lacks: on GPQA Diamond[9](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs) a Claude Haiku 4.5 executor gained a great deal from a Claude Opus 5 advisor, a Claude Sonnet 5 executor gained a few points, and a frontier executor almost nothing.

The second, and the fragile one, is whether the executor actually asks (the consult rate). An executor at low effort can stop detecting that it is stuck: a pairing that consults on most tasks at the default effort can fall to consulting on almost none when effort is lowered, and then scores below the executor alone. The rate also varies by task: on DeepSWE[10](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs) a low-effort Sonnet 5 executor kept asking and gained 23 points; on SWE-bench Pro[3](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs) the same executor stopped. When the executor does ask, it recovers much of the gap. Across the pairings in the following chart whose executor kept asking, the advisor closed at least half the gap to the stronger model (the coding pairing beat the stronger model outright), and you pay for the stronger model only on the consultations, which is what makes the cost cases possible:

![Bar chart of six advisor pairings, Claude Fable 5.1 as the advisor where it applies: gap available versus gain realized, labeled with consult rates, which the gains track](https://platform.claude.com/docs/images/cost-intel-advisor-mechanism.png)

The consult rate responds to prompting. With only the tool's built-in description, executors under-call, especially on coding work, so the [advisor tool documentation](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool#prompting-for-coding-and-agent-tasks) gives a system prompt that asks for one call before substantive work and one before finishing, about two to three calls per task. The coding pairing measured next ran at that cadence with Claude Opus 5 as the executor, about two consultations on every task; with Claude Opus 5.5 as the executor it asked for advice about 1.4 times per attempt, and 4% of its attempts received no advice. That page also covers nudging an under-calling executor and capping calls client-side to bound cost. So watch the consult rate: prompt for it, measure it, and restore the executor's effort if it collapses.

**When it pays on cost.** An advisor saves money when a few short consultations, billed at the advisor's rate, replace running the advisor's model for the whole task. That works best when the advisor's model is priced well above the executor's, so the most cost-effective configuration is a frontier advisor over a mid-tier executor. A pairing at the top of the range can recover part of the advice's cost, because advice also saves executor tokens: an executor told the right approach explores fewer dead ends. In the coding pairing below with a Claude Opus 5 executor, that saving paid for about half of the advice: the executor spent $1.26 less per attempt than Opus 5 alone at its default, and the consultations cost $2.47. With a Claude Opus 5.5 executor, the advice saved almost no executor cost: $1.36 per attempt against $1.38 for Opus 5.5 alone at `high`, while the consultations cost $1.55.

On an internal agentic-coding benchmark[11](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs), run with a plain API agent, a Claude Opus 5.5 executor at `high` with a Claude Fable 5.1 advisor scored 90.1% at $2.92 per attempt. That is 1.7 points over Opus 5.5 alone at `high`, the executor's own setting, a gap at the edge of run-to-run noise with five attempts per task, for about 2.1 times the money; against Opus 5.5 at its default, `medium`, it is 3.5 points for about 3.5 times the money. It lands about on Opus 5.5's own effort curve, so the advisor buys about what more effort does: Opus 5.5 alone at `xhigh` scored 91.1% for $4.11 per attempt (one attempt per task). In August, a Claude Fable 5.1 advisor over a Claude Opus 5 executor was the most accurate configuration measured, at $6.21 per attempt, a little over twice what the Opus 5.5 pairing costs. The chart plots the Opus 5.5 pairing against Opus 5.5's own effort curve and Claude Fable 5.1's from August:

![Coding benchmark: Opus 5.5 at high with a Fable 5.1 advisor gains 1.7 points for 2.1 times the cost, near its effort curve](https://platform.claude.com/docs/images/cost-intel-internal-coding-advisor-opus-5-5.png)

An earlier measurement through [Claude Code's advisor mode](https://code.claude.com/docs/en/advisor) also ranked its advisor pairing above both of its models alone. Read the Claude Opus 5.5 result as a shape to test on your workload: the advisor buys a few points for about twice what the executor costs alone. A wider capability gap does not guarantee a better deal. The latency cost is the consultations themselves: about one or two extra frontier-model calls per task on this benchmark, each on the task's critical path.

**When the stronger model alone is the better step.** Where a workload's accuracy responds to effort, compare the pairing with the advisor's model alone at a reduced setting before building it: the advisor is paid for only on tasks that need it, but a consult that fires on most tasks costs more than running the stronger model itself. On Chartography[13](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs), a Claude Opus 5.5 executor at `low`, given a Claude Fable 5.1 advisor, consulted it on 1 of 300 tasks and scored 61.7, 7 points below Opus 5.5 alone and beyond run-to-run noise, at about the same cost; in August, a Claude Opus 5 executor consulted on nearly every task, and that pairing matched Fable 5.1 alone at `medium` within run-to-run noise (65.0 against 67.5) at about 1.8 times the cost per task. Measure your own consult rate first: if the executor asks on most of its tasks, you are paying advisor rates across the whole workload, and running the advisor's model itself is the cheaper way to the same score.

Whatever the pairing, first price the advisor's model alone at low effort; that is the baseline to beat. Recheck at every model release, because releases move both the capability gap and the price ratio.

**When it fits.** The advisor strategy suits workloads where turns are mostly mechanical but an excellent plan matters: coding agents, computer use, and multistep research pipelines. It fits poorly when every turn genuinely needs frontier capability, when there is nothing to plan (single-turn Q\&A), or when your executor is already close to the advisor's capability.

### Orchestrator strategy: delegate bulk work

In the orchestrator strategy, the frontier model holds the loop. It decomposes the task, dispatches subtasks to lower-cost worker models, and merges their results. The orchestrator's own transcript stays short because workers absorb the token-heavy exploration, so most tokens are billed at worker rates while the plan and synthesis still come from the frontier model.

To build one, use [multiagent orchestration](https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration) in Claude Managed Agents: configure a coordinator agent (the orchestrator) and a roster of worker agents, each with its own model. For a complete working example with a frontier coordinator and Claude Sonnet 5 workers, see the Claude Cookbook recipe [Coordinator pattern: big models for planning, small models for execution](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/CMA_plan_big_execute_small.ipynb).

![Diagram of the orchestrator strategy: a Claude Fable 5.1 orchestrator fans subtasks out to three Claude Sonnet 5 workers](https://platform.claude.com/docs/images/model-routing-orchestrator-strategy.png)

This pattern saves wall-clock time when workers can run in parallel: on the corpus benchmark[8](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs), an episode took about 2.3 hours with the coordinator running the platform's documented limit of 25 concurrent workers, compared with 15 to 20 hours solo. It saved money in only two measured situations. On work a single model could handle alone, the same model at lower effort was cheaper every time.

When workers run in parallel, a time instruction and an elapsed-time clock can shorten the run. On DRACO[21](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs), a team of same-model agents with the instruction and the clock finished in 33% less time at a 54% lower cost per task, and scored 1.5 points lower. Every agent in that team had the instruction and the clock. Anthropic didn't measure the clock with lower-cost workers. On Claude Managed Agents, the clock reaches only the coordinator, so the workers never see it. Anthropic didn't measure a team in which only the coordinator has the clock. The coordinator's clock is also current only on turns that follow your own tool results or messages. [Show the model elapsed time](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#show-the-model-elapsed-time) has the recipe for an agent loop that you run on the Messages API.

**Case 1: insurance against the cost tail on routine work.** A frontier model running alone occasionally spirals on a routine problem it would normally solve. Because you cannot tell in advance which those will be, a few such runs dominate the bill. A coordinator that hands routine work to a lower-cost worker caps that tail, because any spiraling now happens at worker rates.

Anthropic measured this on a deliberately easy slice of BrowseComp[4](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs) (10 problems the solo model reliably solves; 50 delegated and 70 solo runs). A Claude Fable 5 coordinator with one Claude Sonnet 5 worker cost about half as much as Claude Fable 5 alone on average and about a third as much at the 90th percentile ($12 compared with $33), and the solo model's single most expensive run, at $84, was also wrong:

![Dot plot, BrowseComp routine slice: delegated runs cost about half of Claude Fable 5 alone on average, a third at the 90th percentile](https://platform.claude.com/docs/images/cost-intel-tail-insurance.png)

Delegation paid on the routine, normally solvable share of the work, the opposite of the intuition that workers are for hard problems. On the full, harder BrowseComp set, the economics reversed. If your traffic has a long cost tail on routine tasks, this is the orchestrator case to measure first.

**Case 2: work larger than one context window.** A solo model must work through an input that large serially, one context window at a time, paying to re-read its own state on every pass. Workers each read their own partition, in parallel and at worker rates. Reading-heavy work that still fits in one context window is a model-choice problem, not a delegation problem: on reading cost alone, the orchestrator comes out ahead only when no single context can hold the work.

Anthropic built a benchmark for this case[8](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs): a 21.6-million-token corpus of 14 public Python packages with 130 planted defects, too large for any context window. Lowering effort cannot help, because the bill is the corpus read itself: Claude Fable 5.1 solo cost $468 to $552 per episode across the three effort settings, and only its accuracy moved. The coordinator configuration, a Claude Fable 5.1 lead over 25 Claude Sonnet 5 workers, cost about half as much as those settings (47% to 55% less) and scored 10 to 12 points below them, in about 2.3 hours per episode against 15 to 20, while beating a Claude Sonnet 5 solo baseline outright:

![Chart, corpus benchmark: the coordinator costs about half as much as Fable 5.1 solo at any effort, about 12 points below its best](https://platform.claude.com/docs/images/cost-intel-corpus-pareto.png)

The token accounting shows the scale of the reading: the coordinator configuration read about 560 million cached tokens per episode, about one and a half times the solo model's roughly 365 million, nearly all of them at Claude Sonnet 5's cache-read rate, and still cost about half as much overall. Fable 5.1 at `high` effort still holds peak accuracy, at about 2.2 times the coordinator configuration's cost, so delegation here buys most of the accuracy, not all of it.

**When delegation doesn't pay.** An orchestrator buys something only when there is bulk to hand off: many independent pieces, ideally too many for one context window. When the work is one dependent chain, or fits in a single context, the orchestrator pays for a plan, a handoff, and a merge that a single model gets for free. In every such case measured, the coordinator's model alone at lower effort came out ahead.

The boundary is task difficulty, not the benchmark: on the full, harder BrowseComp[4](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs) set, Claude Fable 5 alone reached the coordinator configuration's accuracy at 22% to 30% lower cost. Independent external work reports the same pattern[5](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#refs). If the work is one chain, fits in one context without a long cost tail, or a single model at lower effort already meets your bar, don't build an orchestrator.

### Choose between the strategies

Most cases come down to one question: does the work split into independent pieces, or is it one answer reached through a chain of dependent steps? The [strategy table](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#combine-models) maps the two answers to the two strategies.

If you are unsure, don't build anything yet:

1. Sweep effort on your current model first. It is the cheapest experiment on this page, and most workloads end there.
2. If the sweep shows a gap, price the stronger model alone at low effort. That is the number an advisor pairing has to beat, and the pairings on this page that beat it were the ones whose executor actually consulted.

The multi-model results on this page were judged against the same model at lower effort and against the next model down running alone. That is the comparison to run on your own workload, and why the first step is an effort sweep.

When you do add an advisor, it is a tool definition rather than a rearchitecture.

## Measure on your own workload

The numbers on this page reflect list prices at the time of measurement and will drift as models and prices change. Your escalation rate, how cleanly tasks split, and transcript length move them too. The method stays the same:

1. Pull a few tasks from production logs, weighted like real traffic, and [write outcome checks](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests) for each: tests pass, ticket closed, row count correct. Record cost per task beside the score: price the five priced token counts in each response's `usage` at their own rates (uncached input, 5-minute and 1-hour cache writes at 1.25x and 2x the input price, cache reads, and output), summed across the task's requests (the [Usage and Cost API](https://platform.claude.com/docs/en/manage-claude/usage-cost-api) reports the aggregate).
2. Baseline the model tiers across effort levels, not only the default, and plot score against spend. A multi-model configuration must beat the single model's whole curve.
3. If the curve shows a gap effort can't close, add the multi-model strategy that fits and re-run the suite.
4. Run the winner in shadow on a traffic slice before cutover, then keep the suite running.

The following example computes one request's step 1 cost at Claude Opus 5.5's list prices:

<CodeGroup>
  ```bash cURL
  # Per-million-token prices from the pricing page; change these three for another model.
  INPUT_PER_MTOK=4.00 # Claude Opus 5.5
  CACHE_READ_PER_MTOK=0.20 # 0.05x the input price on Claude Opus 5.5; the multiplier differs by model
  OUTPUT_PER_MTOK=20.00

  response=$(curl --fail-with-body -sS https://api.anthropic.com/v1/messages \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "content-type: application/json" \
    -d '{
      "model": "claude-opus-5-5",
      "max_tokens": 1024,
      "messages": [{"role": "user", "content": "Hello, Claude"}]
    }')

  cost=$(jq -r --argjson in_price "$INPUT_PER_MTOK" --argjson read_price "$CACHE_READ_PER_MTOK" --argjson out_price "$OUTPUT_PER_MTOK" '
    .usage
    | (.input_tokens * $in_price
       + (.cache_creation.ephemeral_1h_input_tokens // 0) * $in_price * 2.00  # 1-hour cache write
       + (.cache_creation.ephemeral_5m_input_tokens // 0) * $in_price * 1.25  # 5-minute cache write
       + (.cache_read_input_tokens // 0) * $read_price                   # cache read
       + .output_tokens * $out_price) / 1e6
  ' <<<"$response")
  printf 'Request cost: $%.6f\n' "$cost"
  ```

  ```bash CLI
  # Per-million-token prices from the pricing page; change these three for another model.
  INPUT_PER_MTOK=4.00 # Claude Opus 5.5
  CACHE_READ_PER_MTOK=0.20 # 0.05x the input price on Claude Opus 5.5; the multiplier differs by model
  OUTPUT_PER_MTOK=20.00

  USAGE=$(ant messages create \
    --model claude-opus-5-5 \
    --max-tokens 1024 \
    --message '{role: user, content: "Hello, Claude"}' \
    --transform usage)

  COST=$(jq -r --argjson in_price "$INPUT_PER_MTOK" --argjson read_price "$CACHE_READ_PER_MTOK" --argjson out_price "$OUTPUT_PER_MTOK" '
    (.input_tokens * $in_price
      + (.cache_creation.ephemeral_1h_input_tokens // 0) * $in_price * 2.00  # 1-hour cache write
      + (.cache_creation.ephemeral_5m_input_tokens // 0) * $in_price * 1.25  # 5-minute cache write
      + (.cache_read_input_tokens // 0) * $read_price                   # cache read
      + .output_tokens * $out_price) / 1e6
  ' <<<"$USAGE")
  printf 'Request cost: $%.6f\n' "$COST"
  ```

  ```python Python
  # Per-million-token prices from the pricing page; change these three for another model.
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
  // Per-million-token prices from the pricing page; change these three for another model.
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
  // Per-million-token prices from the pricing page; change these three for another model.
  const double InputPerMtok = 4.00; // Claude Opus 5.5
  const double CacheReadPerMtok = 0.20; // 0.05x the input price on Claude Opus 5.5; the multiplier differs by model
  const double OutputPerMtok = 20.00;

  AnthropicClient client = new();
  var response = await client.Messages.Create(
      new MessageCreateParams
      {
          Model = Model.ClaudeOpus5_5,
          MaxTokens = 1024,
          Messages = [new() { Role = Role.User, Content = "Hello, Claude" }],
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
  // Per-million-token prices from the pricing page; change these three for another model.
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
  // Per-million-token prices from the pricing page; change these three for another model.
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
  // Per-million-token prices from the pricing page; change these three for another model.
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
  # Per-million-token prices from the pricing page; change these three for another model.
  INPUT_PER_MTOK = 4.00 # Claude Opus 5.5
  CACHE_READ_PER_MTOK = 0.20 # 0.05x the input price on Claude Opus 5.5; the multiplier differs by model
  OUTPUT_PER_MTOK = 20.00

  client = Anthropic::Client.new
  response = client.messages.create(
    model: "claude-opus-5-5",
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

In agent loops most input tokens should be cache reads; if `cache_read_input_tokens` is small next to `input_tokens` plus `cache_creation_input_tokens`, check that caching is engaged and that the prefix stays the same between requests. When the [advisor tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool#usage-and-billing) or [compaction](https://platform.claude.com/docs/en/build-with-claude/compaction-threshold#understanding-usage) is enabled, some tokens are reported only in `usage.iterations` and not in the top-level totals, so sum over `usage.iterations` instead, pricing `advisor_message` entries at the advisor model's rates.

The following table lists the levers in the order to try them:

| Lever                                       | Saving in these runs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Quality cost                                                          | Latency                               | Where                                                                                                                                                                           |
| ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Prompt caching                              | Cost cut by a factor of 2.7 to 5.3 on agent loops; 83% on the triage run                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | None                                                                  | Faster                                | [Cache repeated context](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#cache-repeated-context)                                   |
| 1-hour cache duration                       | Cheaper than the 5-minute default once about 1 turn in 20 follows a pause between 5 minutes and an hour and few gaps run over an hour, except on Claude Fable 5.1, where keeping the 5-minute cache warm is cheaper while pauses run minutes and the 1-hour duration wins when pauses run toward an hour, and on Claude Opus 5.5, where keeping the 5-minute cache warm is cheaper when only a turn or two in 20 follow a pause of up to about half an hour; with no pauses the default cost 15% less on Claude Sonnet 5 and about 15% to 18% less on Claude Opus 5.5 | None                                                                  | Stays warm after a pause              | [Pick the cache duration](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#pick-the-cache-duration)                                 |
| Input trimming                              | A further 5 percentage points on the triage run                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | None                                                                  | Neutral                               | [Trim input and context tokens](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#trim-input-and-context-tokens)                     |
| Prune stale tool results at task boundaries | 39% on the long triage run (compaction 32%); nothing on short loops                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | None measured                                                         | Neutral                               | [Trim input and context tokens](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#trim-input-and-context-tokens)                     |
| Tool search                                 | 45% with 500 tool definitions attached; 20% with a GitHub MCP server                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | None                                                                  | Neutral                               | [Trim input and context tokens](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#trim-input-and-context-tokens)                     |
| Data files through code execution           | 92% on a 25-question data task                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | A gain, 25 of 25 instead of 6 of 25                                   | Faster                                | [Trim input and context tokens](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#trim-input-and-context-tokens)                     |
| Batch API                                   | 50%                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | None                                                                  | Results within 24 hours               | [Batch work that can wait](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#batch-work-that-can-wait)                               |
| Prompt audit against the current model      | 14% on both migrations measured                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | None; a gain on one                                                   | Faster (fewer tool rounds)            | [Audit prompts against the current model](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#audit-prompts-against-the-current-model) |
| Upgrade the model                           | Opus 4.8 to Opus 5: 12 more points at 21% more per solved task (Opus 5 at `low` beats Opus 4.8 for about 30% of the cost); Sonnet 4.6 to Sonnet 5: 15% less per solved task, 5 more points; Fable 5 to Fable 5.1: 43% less per solved task at about the same score                                                                                                                                                                                                                                                                                                    | A gain                                                                | Neutral                               | [Upgrade the model](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#upgrade-the-model)                                             |
| Lower effort                                | Knowledge work: `medium` 13% to 31%, `low` a third to a half; long coding: `medium` about 30% and `low` about two thirds, both against `high`                                                                                                                                                                                                                                                                                                                                                                                                                         | 1 to 3 points on knowledge work, 2 to 8 on long coding                | Faster                                | [Tune effort](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#tune-effort)                                                         |
| Re-run failures                             | About 40% against running everything at `high`, at the same pass rate or slightly better                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | None                                                                  | Two runs on the tasks that fail       | [Re-run failures at higher effort](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#re-run-failures-at-higher-effort)               |
| Task budget                                 | 44% to 58%                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 3 to 6 points                                                         | Faster                                | [Set budgets and output caps](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#set-budgets-and-output-caps)                         |
| Ask for shorter answers                     | 39% of output tokens, 14% of cost on the triage run                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | None                                                                  | Faster                                | [Set budgets and output caps](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#set-budgets-and-output-caps)                         |
| Raising `max_tokens`                        | None per solved task, but more tasks solved                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Gains of up to 22 points on the internal set; none on the public pair | Neutral                               | [Set budgets and output caps](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#set-budgets-and-output-caps)                         |
| Advisor                                     | Depends on the capability gap and the consult rate; the coding pairing scored 1.7 points over Claude Opus 5.5 alone at `high` for about 2.1 times the price, about what more effort buys; with Claude Opus 5.5, the chart-reading pairing almost never consulted the advisor and scored 7 points below Opus 5.5 alone                                                                                                                                                                                                                                                 | A gain on coding, a loss on chart reading                             | About one or two extra calls per task | [Advisor strategy](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#advisor-strategy-escalate-hard-decisions)                       |
| Orchestrator                                | About half against the frontier model, both beyond one context window and on routine tails (the latter measured on Claude Fable 5)                                                                                                                                                                                                                                                                                                                                                                                                                                    | 10 to 12 points below the frontier model                              | Much faster on large inputs           | [Orchestrator strategy](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#orchestrator-strategy-delegate-bulk-work)                  |

## Benchmarks referenced

Except where a reference says otherwise, measurements are Anthropic-internal runs of these benchmarks. Unless noted, costs are USD at the list prices in effect when each benchmark ran; Claude Sonnet 5 figures use $2 and $10 per million input and output tokens. Charts labeled "notional USD" price each request's token counts at those rates rather than reporting invoices.

1. **WideSearch:** Wong et al., "WideSearch: Benchmarking Agentic Broad Info-Seeking," arXiv:2508.07999, 2025. Broad web-research tasks graded on a many-row table's completeness and accuracy; 200 problems, 3 runs per configuration, run August 1 to 2, 2026. The cost-concentration chart is a separate 20-problem run, 3 runs per problem, run August 3 to 4, 2026, costed from per-request billing records.
2. **GDPval:** OpenAI, "GDPval: Evaluating AI Model Performance on Real-World Economically Valuable Tasks," 2025. Knowledge-work deliverables graded against task rubrics; a 210-task run of the released gold set, one attempt per task, run August 2, 2026. A Claude model grades, so absolute scores may differ from published results.
3. **SWE-bench Pro:** Scale AI, "SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?", 2025. A 482-problem subset selected for compatibility with Anthropic's evaluation harness; scores are not comparable to the public leaderboard. They are also not comparable to the SWE-bench Pro results in the Claude Opus 5.5 system card, which come from runs at `max` effort on a different problem set. Claude Opus 5.5 figures average two runs at `low`, `medium` (its default) and `high`, and use one run at `xhigh`, all run September 19 to 20, 2026, with the same 16,384-token cap per turn as the August Claude Opus 5 runs; the cap cut off 2 `xhigh` attempts and none at other settings. The Opus 5.5 runs used a version of the benchmark whose grading containers can reach only internal package mirrors. That version drops one problem whose test needs a live website, and on three more the reference solution fails there, so Opus 5.5 comparisons, and the Claude Fable 5.1 figures set beside them, use the remaining 478 problems. The Claude Opus 5 SWE-bench Pro figures in [Upgrade the model](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#upgrade-the-model) and the [advisor pairings chart](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#advisor-strategy-escalate-hard-decisions) average two runs at its default effort and use one run at `low`, all run August 4, 2026. Escalation figures come task by task from the Opus 5.5 runs: `low` first, then `high` on its failures, solved 96.4% to 97.5% across run pairings for about $0.17; `medium` first, 96.0% to 97.1% for about $0.24; `high` re-run on its own failures, 96.9% for $0.31; everything at `high`, 94.8% to 95.8% for $0.29. Costs on this subset are priced as a customer's organization is metered: each request's prior prompt as a cache read and its new tokens as a 5-minute cache write, from the runs' own usage records, checked against a customer ledger; the evaluation organization's own metering, which until September 10, 2026, billed cache reads in 8,192-token blocks for Claude Opus 5, Claude Fable 5, Claude Opus 4.7, and Claude Opus 4.8, gave figures 1.4 to 1.8 times higher for those models' runs; for Claude Fable 5.1, Claude Sonnet 5, and Claude Sonnet 4.6 the two differ by at most about 9%, and for the Claude Opus 5.5 figures they agree within 3% at each effort setting. The Claude Sonnet 5 executor pairings on the advisor chart come from the same measurement series on this subset: the Sonnet-plus-Opus 5 pairing was run twice (August 7 and August 8, 2026, a run and an exact replication), the low-effort pairing once (August 8, 2026), and Claude Sonnet 5 alone twice (77.4%, the baseline for both Pro rows). The Claude Fable 5 point in Upgrade the model is the mean of three runs at the default effort, run August 26, 2026, priced the same way. The Claude Fable 5.1 task-budget figures are one run per budget (two at 35,000 tokens) on the same subset at the default effort, run August 26, 2026, with an unbudgeted run the same day (92.1%, $1.10 per task) as the baseline; an earlier set at `low` effort, run August 21, 2026, scored 88.6% unbudgeted at $0.48 per task. The [Compare models](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#compare-models-on-cost-per-task) comparison pairs that single run with the two pooled Claude Sonnet 5 runs from the same subset; at Fable 5.1's default effort the pair reads the other way, 41% more per solved task than Sonnet 5. The upgrade ladder is one run per model at its shipped defaults (two each for Opus 5 and Sonnet 5, and the Fable 5 point as described above), the Opus and Sonnet runs the same week in one harness and organization.
4. **BrowseComp:** Wei et al., "BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents," OpenAI, 2025. Effort figures use a 500-problem cut, one to three runs per setting, run August 3, 2026, with the default point pooling two runs from July 26 to 27, 2026. The cost-insurance chart uses 10 reliably solved problems from a 26-problem slice, 50 delegated runs (August 1 to 2, 2026) and 70 solo runs (50 from August 2 to 3, 2026; 20 archived from July 12 to 13 and August 1, 2026), $6.45 compared with $11.99 per run in expectation; delegated figures carry a measurement band of about 20%.
5. **Agent-architecture scaling:** Kim et al., "Towards a Science of Scaling Agent Systems," arXiv:2512.08296, 2025. Independent external study, cited only for the direction of the finding on when delegation does not pay, not for any figure.
6. **DeepWideSearch:** "DeepWideSearch: Benchmarking Depth and Width in Agentic Information Seeking," arXiv:2510.20168, 2025. The 220 questions span 15 domains, each combining many-row collection with multi-hop retrieval; measured on the benchmark's standing row set, 3 runs per configuration, run August 2, 2026 (the single-worker team point ran July 26 to 27, 2026).
7. **DeepResearch Bench II:** Li et al., "DeepResearch Bench II: Diagnosing Deep Research Agents via Rubrics from Expert Report," arXiv:2601.08536, 2026. Its 132 research tasks across 22 domains are graded against expert-derived binary rubrics; measured on a 50-task subset stratified across all themes, one attempt per task, 3 runs per setting, on [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview) with the platform's own web search and fetch tools (August 26 to 27, 2026); scored on the 33 tasks no configuration refused, with attempts the production safety classifiers cut short removed; costs are what a customer is billed, the platform's requests plus web-search fees. Scores are each model's mean on the 33-task basis with its own pre-empted tasks removed; on the 21 tasks clean in every arm, Claude Fable 5.1 holds a 2-to-3-point lead over Claude Fable 5 at every effort level and both models are flat across effort. The caching chart re-prices the same requests with every input token at the uncached rate. Claude Opus 4.6 judges under the benchmark's rubric protocol; the original uses a different judge, and an Anthropic judge may favor the house style. Claude Opus 5 at its default effort ran on the same surface and subset, three runs, on August 28, 2026: 68.8% on the raw 50 tasks, 70.8% on the 33-task basis, and 71.1% on the 21-task set, at $6.71 per task ($23.72 without caching); none of its attempts was cut short by the safety classifiers, under a safeguards deployment newer than the one the other models ran under.
8. **Corpus defect sweep:** Anthropic-internal, for work larger than one context window: a 21.6-million-token corpus from 14 public Python package sources with 130 planted defects and deterministic grading; protocol fixed before the runs and internally reviewed; three runs per configuration. Every configuration ran on Claude Managed Agents. The charted team configuration is a run in which the Claude Fable 5.1 coordinator ran the whole sweep inside the platform at its documented limit of 25 concurrent Claude Sonnet 5 workers, run August 30, 2026; its three episodes scored F1 0.764, 0.825, and 0.791 after the extras audit (raw 0.751, 0.821, and 0.781) for $225, $234, and $283. The Claude Sonnet 5 solo configuration ran August 3 to 4, 2026; the Claude Fable 5.1 solo configurations ran August 24 to 25, 2026, under the platform's launch serving settings, three seeds per effort setting, on the same corpus build. The sandbox image carried installed copies of part of the corpus, and Claude Fable 5.1's final assembly step compared against them in 7 of 9 episodes; re-grading without those additions moved the affected seeds by up to 3 points. Absolute F1 is specific to this corpus build, not comparable across benchmarks; configuration comparisons are like for like.
9. **GPQA Diamond:** Rein et al., "GPQA: A Graduate-Level Google-Proof Q\&A Benchmark," 2023. The 198-question Diamond subset, two runs per configuration, run August 7, 2026 (Claude Opus 5.5: September 19, 2026), model-graded against reference answers, advisor tokens metered per request. A platform safety check refused two biology questions on the Claude Sonnet 5 executors, and one of them also on Claude Opus 5; excluding them changes no comparison by more than one point. Claude Opus 5.5's 92% comes from two runs that set `fallbacks: "default"` to opt into [server-side fallback](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#server-side-fallback), with any attempt that still ended in a refusal counted as wrong. In each run the safety check flagged six biology questions, Claude Opus 5 answered five of them through the fallback, and the sixth still ended in a refusal. Opus 5.5's cost per question includes those fallback answers. Without counting refusals as wrong, these runs score 93%, because the grader still assigns an answer option to a refused attempt, usually the correct one. With refusals counted as wrong, Claude Opus 5's runs score 91% (one refusal per run), as do two Claude Opus 5.5 runs with fallback off, in which Opus 5.5 refused five or six biology questions per run.
10. **DeepSWE:** Datacurve, "DeepSWE: Measuring Frontier Coding Agents on Original, Long-Horizon Engineering Tasks," arXiv:2607.07946, 2026. The set has 113 original tasks across five languages with program-based verifiers. Pairings are two runs each, run August 7, 2026, with advisor tokens metered per request, and used a client-side advisor loop rather than the advisor tool, with identical accounting. Single-model effort sweeps are single runs priced from token counts, a cache-aware approximation. Costs per task are run totals divided by 113.
11. **Internal agentic-coding benchmark:** Anthropic-internal: 370 repository tasks graded by the repositories' own tests. The API figures were measured with a 128,000-token output cap, one run per configuration: Opus 5 alone at the default effort August 9 to 10, 2026, and at `low` and `medium` August 10, 2026; Claude Fable 5.1 alone at five explicitly set effort values August 20, 2026 (the chart shows three of them); and the pairing August 24 to 25, 2026. Claude Opus 5.5 alone ran on all 370 tasks, September 19 to 20, 2026: at its default effort (`medium`) and at `high` with five attempts per task, and at `low` and `xhigh` with one (369 of 370 scored at each, after a setup-check failure). The Claude Opus 5.5 executor at `high` with the released Claude Fable 5.1 as advisor (the August runs used a pre-release snapshot) ran five attempts per task on the same dates; one task failed its setup check, so 1,845 attempts were scored. The 279 attempts in which the advisor was turned away under load were re-run, and attempts whose consults timed out were kept, as in August. The August runs had five attempts per task for the pairing and the Claude Opus 5 control and one for the other points. The August pairing averaged about two advisor consultations per attempt; the Claude Opus 5.5 pairing requested 1.39 and received 1.35. Costs are per attempt. Costs are priced as a customer's organization is metered: each agent-loop request's prior prompt as a cache read and its new tokens as a 5-minute cache write, from the runs' own usage records, and each advisor call, which uses no cache, from its recorded tokens, all at list prices. The Claude Code figures are runs of the same tasks from July 8 to 23, 2026, one run per configuration, costs approximate.
12. **Internal repository-task benchmark (cap measurement):** A separate Anthropic-internal set of about 130 repository tasks, run August 20, 2026 (Claude Fable 5.1) and September 19, 2026 (Claude Opus 5.5, at its default effort, `medium`), with a plain API agent loop, one attempt per task. The Claude Fable 5.1 runs are 135 tasks per cap at the default effort set explicitly: the 16,384-token figure averages two runs (36.3% on both); the 64,000 and 128,000 figures are single runs (58.5% and 60.0%). Six problems drew a safety refusal in every run and count as failures. The Claude Opus 5.5 16,384-token figure averages two runs (134 and 135 tasks scored), and its 64,000 and 128,000 figures are single runs (135 tasks each); two attempts in each 16,384-token run ended in a safety refusal and count as failures. The SWE-bench Pro cap figures are one Claude Fable 5.1 run per cap at the default effort, run August 26, 2026, on a 100-problem subset stratified from reference 3's 482-problem set, not comparable to its scores; the two caps scored the same at the default. The chart's per-turn distributions come from the Claude Opus 5.5 and Claude Fable 5.1 runs at 128,000: no Opus 5.5 turn reached the cap (the longest was about 61,000 tokens, and 0.56% of its turns exceeded 16,384), and one Fable 5.1 turn reached 128,000 (0.46% of its turns exceeded 16,384).
13. **Chartography:** Surge AI, "Chartography," 2026. The complete released 100-question set, measured August 6 and 9, 2026 (Claude Opus 5 alone) and September 20, 2026 (Claude Opus 5.5), with Anthropic's implementation on Claude Managed Agents (standard cloud sandbox; advisor configurations use the Managed Agents advisor). Claude Sonnet 4.6 grades instead of the reference judge and the benchmark runs with tools, so scores compare across configurations here but not to the published leaderboard. They are also not comparable to the Chartography results in the Claude Opus 5.5 system card, which use a different grader and run at `max` effort. Two runs per configuration (three for Claude Opus 5.5), pooled; run-to-run spreads were up to 10 points. Costs are what a customer running the agent routinely is billed: each chart's first request reads the agent's shared system prompt and tools from the cache, as it does when another session of the same agent ran in the previous 5 minutes. A chart run on its own costs about $0.03 more with Claude Opus 5 or Claude Opus 5.5 and about $0.12 more with Claude Fable 5.1. The August figures are re-priced this way from the runs' usage records; the evaluation organization's own metering, which until September 10, 2026, billed Claude Opus 5's cache reads in 8,192-token blocks, overstated Claude Opus 5's costs. Costs exclude sandbox time, which added under 1% to the August runs. The Claude Fable 5.1 solo runs are from August 24, 2026, under the platform's launch serving settings, two runs per setting; six attempts hit the 15-minute session cap and score 0, and two charts per run were answered by Claude Opus 5 after a safety refusal. The Claude Opus 5 low-effort executor with a Claude Fable 5.1 advisor ran twice on August 30, 2026, under the same settings (63.0 and 67.0, mean 65.0, at $0.47 a chart; the advisor was consulted on 88% of tasks in each run, and 4 of its 219 replies came from Claude Opus 5 instead, each after a production safety filter stopped the advisor's own reply). Claude Opus 5.5 ran at `low`, with server-side fallback off and a safety classifier judging every tool call: three runs alone (70, 68, and 68) and three with a Claude Fable 5.1 advisor configured (59, 63, and 63), in which it consulted the advisor on 1 of 300 tasks. The consult-rate comparison for the earlier pairings comes from rerunning the same configurations on the Messages API with a container tool set, August 10 to 11, 2026.
14. **Support-desk prompt-audit evaluation:** An Anthropic-constructed set of 44 support tickets with deterministic grading, run in early August 2026 and reported on August 8, 2026, under six system prompts, each adding to the same clean prompt one pattern common in prompts written for Claude Opus 4.8 and Claude Sonnet 4.6. Each chart point is one of three cases (older model, newer model on the same prompt, newer model after the audit) averaged over the six prompts and 44 tickets. The Opus 5 accuracy gain has a 95% confidence interval of 3 to 8 points; the Sonnet accuracy differences are within noise.
15. **Data-file question set:** An Anthropic-constructed set of 25 aggregate questions over a 1,862-row slice of a public liquor-sales CSV, with ground truth computed by pandas and exact-match grading, run on Claude Sonnet 5 and Claude Opus 5 with thinking disabled (the in-context arm cannot complete at the default), a 4,000-token output cap, and no prompt caching, three runs per configuration, run August 19, 2026. The file arm uploads the CSV through the Files API and uses the `code_execution_20260120` tool.
16. **Cache duration measurement:** The 20-issue triage job from [Trim input and context tokens](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#trim-input-and-context-tokens), run on Claude Sonnet 5 on August 23, 2026, and on Claude Opus 5.5 on September 19 and 20, 2026, at its default effort (`medium`) and at `high`, on the Messages API with the same harness (for Claude Opus 5.5, a port of it that sends the same request bodies), the Claude Opus 5.5 cells with `max_tokens` raised to 4,096, with pauses inserted before a randomly chosen share of turns (none, 5%, 10%, and every turn at 6 minutes on all 20 issues on both models, plus every turn at 2 minutes on Claude Sonnet 5; 20-minute and 45-minute pauses on a 5-issue subset on both models). Claude Opus 5's keep-alive figures below come from the same job on August 23, 2026, with `max_tokens` raised to 4,096, on the same schedules except the 2-minute and 45-minute pauses. Three runs per cell, cost computed from each response's `usage` fields at list prices (for Claude Opus 5.5, $4 input, $5 5-minute write, $8 1-hour write, $0.20 cache read, and $20 output per million tokens; Claude Sonnet 5 ran on an Anthropic-internal organization whose usage is metered the same way as a customer organization's), accuracy against the same gold labels. The Claude Opus 5.5 figures on this page cover both effort levels. The crossover is about 3.3% of turns on Claude Sonnet 5 and 3.1% to 3.2% on Claude Opus 5.5: the median of each session's break-even share, computed by the cost model from that session's turn-by-turn context sizes, over all 45 Claude Sonnet 5 twenty-issue sessions and the 36 Claude Opus 5.5 twenty-issue sessions at each effort level (every pause schedule run on the full job, under all three cache settings, three runs each; the 5-issue cells are not in it). In the 5% cell the 5-minute and 1-hour settings tied on Claude Sonnet 5, because that draw's pauses fell on small prefixes; on Claude Opus 5.5 they nearly tied. The page's 1-in-20 rule sits above the measured crossover. Claude Opus 5.5's time to first token after a pause was not measured. Anthropic measured keep-alive requests that refresh the 5-minute cache on Claude Sonnet 5 and Claude Opus 5 on August 23, 2026, and on Claude Opus 5.5 in the runs above, always sent with `max_tokens: 1`. On Claude Sonnet 5 they cost 7.7% less than the 1-hour setting with 5% of turns paused and about the same with 10%; on Claude Opus 5 no difference was measurable at either share; on both they cost more with a pause of 6 minutes or more before every turn. On Claude Opus 5.5 they cost 8% to 18% less than the 1-hour setting with 5% and 10% of turns paused (about 10% to 15% once between-session noise is removed by re-billing each keep-alive session's own tokens at 1-hour cache prices), and more with a pause before every turn: 4% to 6% more at 6 minutes, 9% to 10% at 20 minutes, and 56% to 58% at 45 minutes. Keep-alive saved more on Claude Opus 5.5 because each keep-alive request re-reads the prefix at the cache-read price: 0.05x the input price, against 0.1x on Claude Sonnet 5 and Claude Opus 5; Claude Opus 5's sessions, re-billed at Claude Opus 5.5's prices, show nearly the same savings as Claude Opus 5.5. Anthropic's pre-launch API tests on Claude Opus 5.5 show that a `max_tokens: 0` request writes the cache and that the next request reads it; whether such a request refreshes an existing entry was not measured on Opus 5.5. On Claude Fable 5.1, at 0.025x, keep-alive was cheaper even with a pause before every turn, except at 45-minute pauses (reference 19).
17. **Cache-read share in production:** Aggregated first-party Claude API usage for the 14 days ending August 23, 2026, direct API product only, Anthropic-internal organizations excluded, no organization identified. An organization-day counts as an agent loop when its requests carry tool definitions and tool results, its prompts hold 9 or more prior tool calls on average, caching was used, and it made at least 10 such requests (the API has no conversation identifier, so this stands in for conversation length): 303,003 organization-days across 106,487 organizations, median cache-read share 84.2% of all input tokens, upper quartile 91.7%. Use-case labels (the organization's declared use case, or otherwise its classified one) cover 74% of those organization-days and 99% of their tokens; coding organizations supply 87% of agentic input tokens and read a median 88.5% (90.9% at 25 or more prior tool calls), upper quartile 93.4%, with about 72% of coding organization-days at 80% or more; support, research, and data agents read 84% to 85%. The top decile of organization-days reads 95.9% or more for coding and 94.2% to 94.8% for support, research, data, and other agents. The request-level split at 25 or more prior tool calls comes from a six-hour sample: coding 92% read, 7% write, under 1% uncached. Unlabeled organizations, mostly small, read a median 11%. Organization-days with no tool definitions read a median 34.6%. An independent query over the same window that reconstructs conversations of 10 or more requests, rather than scoring organization-days, puts the median at 90.2%; the difference is scope, not data.
18. **Compaction timing measurement:** The triage agent's long variant from [Trim input and context tokens](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#trim-input-and-context-tokens), run August 24, 2026, on Claude Sonnet 5 with the 5-minute cache, cost from the usage fields at list prices, five sessions per arm: a no-change arm at the default effort throughout ($0.81 per session), and two arms that start at low effort and make the same two cache-breaking changes, a switch to the default effort and one added tool, either mid-session at requests 12 and 17 ($0.95) or together on the first request after the first compaction ($0.75). A fourth arm of six sessions, run August 25, 2026, made the same two changes on the request that triggered the first compaction ($0.92 per session): that request's summarization pass wrote the 81,000-token context to the cache instead of reading it, so that pass cost $0.21 against $0.04 for the same pass in the boundary arm. Sessions first compacted at request 21 to 25 (16 of the 21 sessions at request 22), once the prompt passed the 80,000-token compaction trigger, and two no-change sessions compacted a second time near the end. The boundary arm's lower total than the no-change arm reflects its low-effort requests before the change and those second compactions rather than caching: the two arms' re-write costs differ by under a cent. The mid-session arm paid $0.23 per session in cache re-writes; the difference between the mid-session and boundary arms was $0.20 with a 95% confidence interval of $0.11 to $0.29. One mid-session session ran cheap ($0.82) after its model mis-called the search tool following compaction and got empty results; it is included, and without it the arm averages $0.98. Accuracy averaged 14.2 of 20 labels in each August 24 arm and 14.7 in the August 25 arm; cache reads were 91% of prompt tokens with no changes, 85% mid-session, 91% at the boundary, and 86% with the changes on the triggering request.
19. **Cache duration measurement on Claude Fable 5.1:** The same 20-issue triage job and harness as reference 16, run August 23 and August 26, 2026, on the Claude Fable 5.1 launch snapshot at its launch prices ($10 input, $12.50 5-minute write, $20 1-hour write, $0.25 cache read, $50 output per million tokens), three settings per schedule: the 5-minute cache, the 1-hour cache, and the 5-minute cache kept warm by a `max_tokens: 0` request on the unchanged prefix every 4 minutes, timed from the previous request's start (the August 23 runs sent keep-alive requests with `max_tokens: 1`; in the August 26 cells reported here, every keep-alive request refreshed the cache and billed no output). Schedules: no pauses, 10% of turns, and every turn at 6 minutes on all 20 issues, and 45-minute pauses on the 5-issue subset; three runs per cell (six for the August 26 keep-alive cell with 45-minute pauses), cost computed from each response's `usage` fields at list prices, accuracy against the same gold labels (12 to 17 exact labels of 20). Per-session means on August 26 for the 5-minute, 1-hour, and keep-alive settings: no pauses $2.42, $3.09, $2.29; 10% paused $4.50, $2.96, $2.36; every turn $22.89, $3.01, $2.62; the August 23 cells agree within 6%. The 45-minute figures ($1.68, $0.59, and $0.71 per 5-issue session) are from a clean re-run on August 26 after a cache-billing incident spoiled that day's first cells; the August 23 runs gave $1.67, $0.58, and $0.70. The crossover between the 5-minute and 1-hour settings is 3.1% of turns, the same measure as reference 16.
20. **Terminal-Bench 3:** the public terminal-agent benchmark's 74 tasks, run on [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview) with two custom tools, a shell and a file editor that the evaluation harness runs in each task's own container, in place of the platform's built-in tools, and otherwise at the platform's default settings for external accounts, two runs per model at `high` effort, August 27 to 28, 2026. These runs used Terminal-Bench version 3.0, and their scores are not comparable with the public Terminal-Bench leaderboard or with the Terminal-Bench 4.0 results in the Claude Opus 5.5 system card, which come from runs in Claude Code at `max` effort. Each task's time limits are 2.5 times the benchmark's own, which gives the agent between 75 minutes and 20 hours per task (5 hours for the median task), and each task gets three times the memory it specifies, from 6 GiB to 96 GiB, with extra memory for the 12 tasks that run helper services. The agent had no general internet access: its containers could reach an internal package mirror, a short list of download sites including GitHub and the Python Package Index, and a few sites specific to some tasks, and eight of the tasks had no network access at all. Scores are raw pass rates over the 148 attempts per model; single runs swing by 5 to 11 points. Costs are what a customer would be billed at list prices, re-priced request by request from the runs' usage records with the 5-minute cache lifetime. Claude Opus 4.7 ended 11 of its 148 attempts at its output cap.
21. **DRACO:** Perplexity, "DRACO: a Cross-Domain Benchmark for Deep Research Accuracy, Completeness, and Objectivity," arXiv:2602.11685, 2026. Its 100 research tasks across 10 domains are graded against expert-written rubrics, and the score is the benchmark's normalized score. Every configuration ran on the Claude API with Claude Fable 5.1, the default adaptive thinking, the production safety classifiers on, and `max_tokens` at 128,000: a single agent at `high` and at `medium` effort, the single agent at `high` with the instruction and the clock, and a team at `high` with and without them. The team is a lead agent that starts helper agents of the same model through a tool, with no cap on their number. On DRACO, the lead started a median of 4 helpers per attempt. Each configuration made three attempts at each task, run September 8 to 10, 2026. An attempt that hit the four-hour limit was run again, and the new attempt counts. The only attempts left out are all 3 attempts at one task for the single agent at `medium` effort, so that configuration covers 99 tasks. That task timed out on every attempt, in the original run and in the re-run. Scoring those 3 attempts as 0, as the benchmark's own scoring would, affects only the two comparisons with `medium` effort. The score change at `medium` effort against `high` moves from 0.7 to 1.7 points lower, and the score change with both changes against `medium` effort moves from 1.2 to 0.2 points lower. The agents used a search tool and a fetch tool that the evaluation harness hosts over a pinned web index. Those tools set part of the time, and yours will run at a different speed, so the page gives time as a ratio between configurations, not in minutes. Time is the wall-clock time per task, from the first request to the last request on any agent, minus the estimated time spent waiting to retry requests after rate-limit or overload errors. Those errors came from the test account's shared limits. All configurations of a set started together. The slower ones finished hours later, so part of their time ran under different load. Each task's cost is its requests priced at public list prices, with prompt caching billed as it would be for a customer who sets a cache breakpoint at the end of each request and uses the 5-minute cache lifetime, for model tokens only. The harness's tools add no charges. Score changes are paired differences over tasks, with 95% bootstrap intervals. A change counts as inside the margin when its interval stays within 1.5 points on DRACO and 2.5 points on HLE. Anthropic set those margins before the runs. Claude Opus 5 grades the answers. Against each set's own grader, Opus 5 scored 1.9 to 2.4 points higher on DRACO, 2.2 to 2.9 points lower on HLE (Opus 5 graded 495 of the 500 questions, and the benchmark's grader graded all 500), and 1.3 to 2.0 points lower on the physics set, whose own grader also uses the expert reference solutions, in every configuration. The two graders agree on the direction of every change.
22. **HLE:** Phan et al., "Humanity's Last Exam," arXiv:2501.14249, 2025. Expert-written questions with exact answers, graded against the reference answers. Measured on the first 500 questions, with the benchmark's own sources blocked from search, and the same setup as reference 21. Each configuration made three attempts at each question, run September 8 to 10, 2026. Claude Opus 5 compares each answer with the reference answer, with adaptive thinking on, as it is by default. The judge graded 495 of the 500 questions in every configuration, and the scores cover those 495. For the other 5, the grading request was over the judge's 1M-token limit. An attempt that hit the four-hour limit was run again, and the new attempt counts, so every configuration has all 1,500 attempts. Scoring the 5 ungraded questions as 0, as the benchmark's own scoring would, changes no finding.
23. **Physics set:** An internal set of 70 research-level physics problems, adapted from the public CritPt benchmark: Zhu et al., "Probing the Critical Point (CritPt) of AI Reasoning: a Frontier Physics Research Benchmark," arXiv:2509.26574, 2025. Expert reviewers corrected the problem statements. Claude Opus 5 grades each answer against expert reference solutions that aren't public, so the scores can't be compared with published results. The score is the mean grade over a problem's attempts, averaged over problems. Measured on all 70 problems, four attempts per problem, run September 8 to 9, 2026. Every agent had a Python tool, a shell, and a file editor in a sandbox container with no network access, and no search or fetch tools. Otherwise the setup is that of reference 21. No score margin was set for the physics set before the runs, so the page gives its score changes with their 95% intervals and doesn't describe them as inside a margin.

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

  <Card title="Task budgets" icon="clock" href="https://platform.claude.com/docs/en/build-with-claude/task-budgets">
    Give agent loops a token countdown they self-regulate against.
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
