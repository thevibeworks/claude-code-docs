---
title: List Events
url: https://platform.claude.com/docs/en/api/php/beta/sessions/events/list
---

# List Events

`$client->beta->sessions->events->list(string sessionID, ?\Datetime createdAtGt, ?\Datetime createdAtGte, ?\Datetime createdAtLt, ?\Datetime createdAtLte, ?int limit, ?Order order, ?string page, ?list<string> types, ?list<AnthropicBeta> betas, ?string workspaceID): PageCursor<ManagedAgentsSessionEvent>`

**GET** `/v1/sessions/{session_id}/events`

List Events

## Parameters

- `sessionID: string`

- `createdAtGt?:optional \Datetime`

  Return events created after this time (exclusive). Compared against the event's `processed_at` value.

- `createdAtGte?:optional \Datetime`

  Return events created at or after this time (inclusive). Compared against the event's `processed_at` value.

- `createdAtLt?:optional \Datetime`

  Return events created before this time (exclusive). Compared against the event's `processed_at` value.

- `createdAtLte?:optional \Datetime`

  Return events created at or before this time (inclusive). Compared against the event's `processed_at` value.

- `limit?:optional int`

- `order?:optional Order`

  Sort direction for results, ordered by the event's `processed_at`. Defaults to `asc` (chronological).

- `page?:optional string`

  Opaque pagination cursor from a previous response's `next_page`.

- `types?:optional list<string>`

  Filter by event type. Values match the `type` field on returned events (for example, `user.message` or `agent.tool_use`). Omit to return all event types.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `class ManagedAgentsSessionEvent`

  - `class ManagedAgentsUserMessageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Array of content blocks comprising the user message.

    - `?\Datetime processedAt`

      Timestamp when the agent finished processing this message.

  - `class ManagedAgentsUserInterruptEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `?\Datetime processedAt`

      Timestamp when the interrupt was processed.

    - `?string sessionThreadID`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class ManagedAgentsUserToolConfirmationEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `Result result`

      The confirmation result: 'allow' or 'deny'.

    - `string toolUseID`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `?string denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `?\Datetime processedAt`

      Timestamp when the confirmation was processed.

    - `?string sessionThreadID`

      Set by the server to the subagent thread this confirmation was routed to. Omitted when it was routed to the primary thread.

  - `class ManagedAgentsUserCustomToolResultEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string customToolUseID`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

    - `?\Datetime processedAt`

      Timestamp when this result was processed.

    - `?string sessionThreadID`

      Set by the server to the subagent thread this result was routed to. Omitted when it was routed to the primary thread.

  - `class ManagedAgentsAgentCustomToolUseEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string name`

      Name of the custom tool being called.

    - `\Datetime processedAt`

      Timestamp when this tool use was processed.

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.custom_tool_result` by `custom_tool_use_id`, so clients do not send it back.

  - `class ManagedAgentsAgentMessageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Array of text blocks comprising the agent response.

    - `\Datetime processedAt`

      Timestamp when this response was generated.

  - `class ManagedAgentsAgentThinkingEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when this thinking was produced.

  - `class ManagedAgentsAgentMCPToolUseEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string mcpServerName`

      Name of the MCP server providing the tool.

    - `string name`

      Name of the MCP tool being used.

    - `\Datetime processedAt`

      Timestamp when this event was processed.

    - `?ManagedAgentsAgentEvaluatedPermission evaluatedPermission`

      The evaluated permission policy for this tool invocation.

    - `?ManagedAgentsAgentToolEvaluation evaluation`

      Which resolved permission_policy produced evaluated_permission: always_allow, always_ask, or auto (with the server's per-invocation judgement). Absent only when the server refused the call before any policy applied (for example, the named tool is not enabled in the session); such a refusal has evaluated_permission deny. An event recorded before this field existed reads as the arm its evaluated_permission implies (always_allow for allow, always_ask for ask).

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.tool_confirmation` by `tool_use_id`, so clients do not send it back.

  - `class ManagedAgentsAgentMCPToolResultEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string mcpToolUseID`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `\Datetime processedAt`

      Timestamp when this event was processed.

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `class ManagedAgentsAgentToolUseEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string name`

      Name of the agent tool being used.

    - `\Datetime processedAt`

      Timestamp when this event was processed.

    - `?ManagedAgentsAgentEvaluatedPermission evaluatedPermission`

      The evaluated permission policy for this tool invocation.

    - `?ManagedAgentsAgentToolEvaluation evaluation`

      Which resolved permission_policy produced evaluated_permission: always_allow, always_ask, or auto (with the server's per-invocation judgement). Absent only when the server refused the call before any policy applied (for example, the named tool is not enabled in the session); such a refusal has evaluated_permission deny. An event recorded before this field existed reads as the arm its evaluated_permission implies (always_allow for allow, always_ask for ask).

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.tool_confirmation` or `user.tool_result` by `tool_use_id`, so clients do not send it back.

  - `class ManagedAgentsAgentToolResultEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when this event was processed.

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to.

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `class ManagedAgentsAgentThreadMessageReceivedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `string fromSessionThreadID`

      Public `sthr_` ID of the thread that sent the message.

    - `\Datetime processedAt`

      Timestamp when the message was received.

    - `?string fromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class ManagedAgentsAgentThreadMessageSentEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `\Datetime processedAt`

      Timestamp when the message was sent.

    - `string toSessionThreadID`

      Public `sthr_` ID of the thread the message was sent to.

    - `?string toAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class ManagedAgentsAgentThreadContextCompactedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when compaction was processed.

  - `class ManagedAgentsSessionErrorEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `Error error`

    - `\Datetime processedAt`

      Timestamp when the error occurred.

  - `class ManagedAgentsSessionStatusRescheduledEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp of status change.

  - `class ManagedAgentsSessionStatusRunningEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp of status change.

  - `class ManagedAgentsSessionStatusIdleEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp of status change.

    - `StopReason stopReason`

  - `class ManagedAgentsSessionStatusTerminatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp of status change.

  - `class ManagedAgentsSessionThreadCreatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the callable agent the thread runs.

    - `\Datetime processedAt`

      Timestamp when the thread was created.

    - `string sessionThreadID`

      Public `sthr_` ID of the newly created thread.

  - `class ManagedAgentsSpanOutcomeEvaluationStartEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      Timestamp when outcome evaluation started.

  - `class ManagedAgentsSpanOutcomeEvaluationEndEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string explanation`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeEvaluationStartID`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      Timestamp when outcome evaluation ended.

    - `string result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `ManagedAgentsSpanModelUsage usage`

      Aggregate token usage for this evaluation cycle. Sums across all grader model requests within the cycle.

  - `class ManagedAgentsSpanModelRequestStartEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when the model request started.

  - `class ManagedAgentsSpanModelRequestEndEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `?bool isError`

      Whether the model request resulted in an error.

    - `string modelRequestStartID`

      The id of the corresponding `span.model_request_start` event.

    - `ManagedAgentsSpanModelUsage modelUsage`

      Token usage for this model request.

    - `\Datetime processedAt`

      Timestamp when the model request completed.

  - `class ManagedAgentsSpanOutcomeEvaluationOngoingEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      Timestamp when this heartbeat was emitted.

  - `class ManagedAgentsUserDefineOutcomeEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string description`

      What the agent should produce. Copied from the input event.

    - `?int maxIterations`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `string outcomeID`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `\Datetime processedAt`

      Timestamp when the outcome was accepted.

    - `Rubric rubric`

      How to grade the outcome. File rubrics are currently resolved to their text content; clients should handle both variants.

  - `class ManagedAgentsSessionDeletedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when the session was deleted.

  - `class ManagedAgentsSessionThreadStatusRunningEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      Timestamp of the status transition.

    - `string sessionThreadID`

      Public sthr_ ID of the thread that started running.

  - `class ManagedAgentsSessionThreadStatusIdleEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      Timestamp of the status transition.

    - `string sessionThreadID`

      Public sthr_ ID of the thread that went idle.

    - `StopReason stopReason`

  - `class ManagedAgentsSessionThreadStatusTerminatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      Timestamp of the status transition.

    - `string sessionThreadID`

      Public sthr_ ID of the thread that terminated.

  - `class BetaManagedAgentsUserToolResultEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

    - `?\Datetime processedAt`

      Timestamp when this result was processed.

    - `?string sessionThreadID`

      Set by the server to the subagent thread this result was routed to. Omitted when it was routed to the primary thread.

  - `class ManagedAgentsSessionThreadStatusRescheduledEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      Timestamp of the status transition.

    - `string sessionThreadID`

      Public sthr_ ID of the thread that is retrying.

  - `class BetaManagedAgentsSessionUpdatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when the update was applied.

    - `?BetaManagedAgentsSessionAgent agent`

      The session's effective agent configuration after the update. Present only when the update changed `agent` (tools or mcp_servers); when present it is the full materialised snapshot, not a diff.

    - `?BetaManagedAgentsBudgetLimit budget`

      The session's budget after the update: the new budget when set or replaced, or null when the update removed it. Present only when the update changed the budget.

    - `?array<string,string> metadata`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `?string title`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsSystemMessageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<BetaManagedAgentsSystemContentBlock> content`

      System content blocks. Text-only.

    - `?\Datetime processedAt`

      Timestamp when this system message was processed.

  - `class BetaManagedAgentsSessionUsageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when the snapshot was taken.

    - `ManagedAgentsSessionUsageSnapshot usage`

      The session's cumulative usage at the snapshot time.

    - `?BetaManagedAgentsBudgetLimit budget`

      The session's configured budget at the snapshot time, or null when the session has no budget.

## Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->sessions->events->list(
  'sesn_011CZkZAtmR3yMPDzynEDxu7',
  createdAtGt: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  createdAtGte: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  createdAtLt: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  createdAtLte: new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
  limit: 0,
  order: 'asc',
  page: 'page',
  types: ['string'],
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($page);
```

### Response (200)

```json
{
  "data": [
    {
      "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message",
      "processed_at": "2026-03-15T10:00:00Z"
    },
    {
      "id": "sevt_011CZkZHPq1jCdq5lbRTjiVnz",
      "content": [
        {
          "text": "Let me look up order #1234 for you.",
          "type": "text"
        }
      ],
      "processed_at": "2026-03-15T10:00:00Z",
      "type": "agent.message"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```
