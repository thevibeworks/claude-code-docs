---
title: Session budgets
url: https://platform.claude.com/docs/en/managed-agents/budgets
description: Cap a session's spend with a hard dollar budget enforced at public list rates.
---

A session budget is an optional hard spend ceiling you set when you [create a session](https://platform.claude.com/docs/en/managed-agents/sessions). The platform continuously prices everything the session consumes at public list rates (the session's **list cost**) and stops issuing new model requests once that cost reaches the budget. The request in flight when the cap is crossed still finishes, so the final list cost can land [a fraction past the budget](https://platform.claude.com/docs/en/managed-agents/budgets#when-a-session-reaches-its-budget). A session at its budget pauses and goes [idle](https://platform.claude.com/docs/en/managed-agents/session-operations#session-statuses) rather than terminating; changing or removing the budget resumes its work automatically. Deployments accept the same budget and apply it to each session they start; see [Budgets on deployments](https://platform.claude.com/docs/en/managed-agents/budgets#budgets-on-deployments).

<Note>
  Managed Agents API requests require the `managed-agents-2026-04-01` beta header, except memory store endpoints, which use `agent-memory-2026-07-22` instead. The SDK sets the correct beta header automatically. See [Beta headers](https://platform.claude.com/docs/en/api/beta-headers#endpoint-specific-headers).
</Note>

## Set a budget at session creation

Pass the optional `budget` field when you create the session:

<CodeGroup>
  ```bash cURL
  session=$(curl -fsSL https://api.anthropic.com/v1/sessions \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    -H "content-type: application/json" \
    -d @- <<EOF
  {
    "agent": "$AGENT_ID",
    "environment_id": "$ENVIRONMENT_ID",
    "budget": {
      "type": "limit",
      "max_list_cost": {"amount": "2500", "currency": "USD"}
    }
  }
  EOF
  )
  SESSION_ID=$(jq -r '.id' <<< "$session")
  ```
</CodeGroup>

The `budget` object has two fields:

* `type` is always `"limit"`.
* `max_list_cost` is the cap itself: `amount` is a whole number of US cents written as a string with no leading zeros (`"2500"` is $25.00 and `"50"` is 50 cents) and must be greater than zero. Decimal forms such as `"25.00"` are rejected. The amount is a string rather than a number so no float rounding is ever applied to it. `currency` is an uppercase ISO-4217 currency code; `USD` is the only supported currency.

A budget can only be attached when the session is created. Adding a budget to an existing session that doesn't have one is rejected with a 400 error. A budgeted session's cap can be [changed](https://platform.claude.com/docs/en/managed-agents/budgets#change-the-budget) or [removed](https://platform.claude.com/docs/en/managed-agents/budgets#remove-the-budget) at any time.

## How list cost is measured

The platform prices what the session consumes, continuously, at public list rates:

* **Model tokens**, at each served model's list price
* **Web searches**, at $10 per 1,000 searches
* **Session running time**, at $0.08 per hour

This running dollar total is the session's **list cost**, and it is what the budget compares against. List cost is not your contracted price: if your organization has negotiated discounts, the session reaches its cap when the list-price total does, and your billed spend might be lower than the cap.

Enforcement uses the exact, unrounded list cost. The `list_cost` figures reported on the session and its events are whole cents, rounded to the nearest cent, so a reported figure can read up to half a cent either side of the exact amount enforcement uses.

## When a session reaches its budget

The cap is enforced between model requests, not mid-request. Before each model request, the platform checks the session's consumed list cost, and once that total reaches the cap every thread pauses before its next request. The request that carried the total past the cap was admitted while the session was still under it and runs to completion, so a paused session's recorded `list_cost` reads at or a fraction past `max_list_cost`: a session capped at `"50"` (50 cents) can pause with a `list_cost` of `"53"`. This is expected, not a billing error, and the overshoot is bounded by one model request per thread. Treat the budget as a bound on new work rather than an exact stopping point, and size the cap with that one-request margin in mind.

A session that reaches its budget goes idle with a `stop_reason` of `budget_reached`; it is not terminated, and its history and sandbox are preserved like any other idle session's. On the [event stream](https://platform.claude.com/docs/en/managed-agents/events-and-streaming) you'll see, in order:

1. A `session.thread_status_idle` event with a `stop_reason` of `budget_reached` as each thread pauses.
2. A [`session.usage`](https://platform.claude.com/docs/en/managed-agents/budgets#monitor-spend) event with the session's cumulative usage and list cost.
3. A `session.status_idle` event with a `stop_reason` of `budget_reached`. The usage event always immediately precedes this idle event.

A thread whose final request both crosses the cap and completes its turn reports `end_turn` on its own `session.thread_status_idle` event while the session still reports `budget_reached`; treat the session-level `stop_reason` as the signal that the session paused at its budget.

### Events accepted at the cap

While the session is at or over its budget, it accepts only events that settle work already in progress:

* `user.tool_confirmation`
* `user.tool_result`
* `user.custom_tool_result`
* `user.interrupt`

Any event that would start new work, such as `user.message`, is rejected with a 400 error naming this list. Settled results are recorded without triggering a new model request; the session stays paused at its budget.

A `user.interrupt` sent while the session is paused at its budget (all threads paused at the cap) is accepted and ignored: it does not appear in the event list and changes nothing. Change or remove the budget to continue.

## Resume a session at its budget

Change or remove the budget with a session update. An accepted update resumes the session's paused work automatically; no further client action is needed.

### Change the budget

Update the session with a new `max_list_cost`. The new value can be higher or lower than the current cap, but it must be strictly greater than the session's consumed list cost; otherwise the update is rejected with a 400 error: `budget.max_list_cost must be greater than the session's consumed list cost`. Because the consumed cost usually sits [a fraction past the old cap](https://platform.claude.com/docs/en/managed-agents/budgets#when-a-session-reaches-its-budget) when the session pauses, base the new value on the session's reported `usage.list_cost`, not on the old `max_list_cost`. Set it a cent or more above that figure: the reported value is rounded and can sit a fraction below the exact consumed cost the check uses.

<CodeGroup>
  ```bash cURL
  curl -sS --fail-with-body "https://api.anthropic.com/v1/sessions/$SESSION_ID" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    -H "content-type: application/json" \
    -d @- <<'EOF'
  {
    "budget": {
      "type": "limit",
      "max_list_cost": {"amount": "4000", "currency": "USD"}
    }
  }
  EOF
  ```
</CodeGroup>

### Remove the budget

Set `budget` to `null` to remove the cap entirely. The session's paused work resumes, and the resulting `session.updated` event carries `budget` set to `null`.

<CodeGroup>
  ```bash cURL
  curl -sS --fail-with-body "https://api.anthropic.com/v1/sessions/$SESSION_ID" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -H "anthropic-beta: managed-agents-2026-04-01" \
    -H "content-type: application/json" \
    -d '{"budget": null}'
  ```
</CodeGroup>

<Warning>
  Removing a session's budget is one-way: a session whose budget has been removed cannot be given a new one. To keep a cap on the session, change the budget instead.
</Warning>

## Monitor spend

The session object carries its `budget` and a `usage` object with the tracked spend: `usage.list_cost` is the session's consumed list cost, and `usage.active_seconds` is the running time its runtime cost is priced on. On a session paused at `budget_reached`, expect `usage.list_cost` to read at or a fraction past `max_list_cost`: the [request that crossed the cap](https://platform.claude.com/docs/en/managed-agents/budgets#when-a-session-reaches-its-budget) finished before the pause. Session-level `active_seconds` counts overlapping activity from concurrent threads once. Thread retrieval responses carry the same two fields on the thread's own `usage`, priced per thread. Per-thread figures are rounded independently and exclude the session's running-time cost, so they don't sum exactly to the session's `list_cost`; the session figure is the one the budget is enforced against.

The `session.usage` event is a snapshot of the session's cumulative usage and tracked list cost. It carries the session's token totals, `list_cost`, `active_seconds`, `server_tool_use` request counts (`web_search_requests`, priced into list cost per request, and `web_fetch_requests`, which reads `0` because web fetch requests carry no per-request charge and aren't metered), and an echo of the session's `budget`, or `null` when the session has none. It appears in the events list and the session stream. The session emits one immediately before it goes idle, whatever the stop reason, so a session that reaches its budget always emits one immediately before the budget-reached idle event.

For reading usage from the stream and the session object, see [Tracking usage](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#tracking-usage).

## Budgets in multiagent sessions

A [multiagent](https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration) session has a single budget shared across all of its threads; there are no per-thread caps. Each thread's consumption is priced at its own served model, and threads pause independently as the shared cap is reached. [Advisor](https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration#give-the-session-an-advisor) consultations count against the same budget, priced at the advisor model's rates. One thread can pause at `budget_reached` while another finishes its in-flight request.

A pending ask outranks the cap: a session with one thread waiting on `requires_action` and another paused at `budget_reached` reports `requires_action` at the session level. The pending request still needs an answer, and answering it is a [settle event](https://platform.claude.com/docs/en/managed-agents/budgets#events-accepted-at-the-cap) the budget doesn't block.

## Budgets on deployments

A [deployment](https://platform.claude.com/docs/en/managed-agents/scheduled-deployments) accepts the same `budget` object when you create or update it:

```json
{
  "budget": {
    "type": "limit",
    "max_list_cost": { "amount": "2000", "currency": "USD" }
  }
}
```

The cap is copied onto each session the deployment starts, so it bounds each run separately rather than the deployment's cumulative spend. Changing the deployment's budget applies to sessions the deployment starts afterward, not to sessions already running. Unlike a session, a deployment's budget can be cleared with `null` and set again later. See [Set a budget on each run](https://platform.claude.com/docs/en/managed-agents/scheduled-deployments#set-a-budget-on-each-run).

## Models without a list price

A budget can only track consumption the platform can price. Creating a budgeted session whose agent, or any agent or advisor on its [multiagent roster](https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration), uses a model with no public list price is rejected with a 400 error stating that no list price is available for the model.

If a budgeted session's usage comes to include a model with no list price, the budget can no longer measure the session's spend: the session can pause with a `stop_reason` of `budget_reached`, and changing the budget is rejected. Remove the budget to resume the session.

## Error reference

Budget-related requests are rejected in the following cases:

| Condition                                                                                                                                                                                                                                   | Status |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| A work-starting event (for example, `user.message`) is sent while the session is at or over its budget; the error names the [accepted settle events](https://platform.claude.com/docs/en/managed-agents/budgets#events-accepted-at-the-cap) | 400    |
| The budget is set to a value at or below the session's consumed list cost                                                                                                                                                                   | 400    |
| A budget is added to a session created without one, or re-added after removal                                                                                                                                                               | 400    |
| `amount` is not a whole number of cents (for example, `"25.00"`), is zero or negative, or `currency` is not `USD`                                                                                                                           | 400    |
| A budgeted create references a model with [no public list price](https://platform.claude.com/docs/en/managed-agents/budgets#models-without-a-list-price)                                                                                    | 400    |

<Note>
  Session budgets are hard caps in US dollars (written in cents) on a single session, enforced by the platform. They are distinct from the Messages API's [task budgets](https://platform.claude.com/docs/en/build-with-claude/task-budgets), which are advisory, token-denominated budgets the model uses to self-regulate within one agentic loop.
</Note>
