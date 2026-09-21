---
title: Events
url: https://platform.claude.com/docs/en/api/php/beta/sessions/events
---

# Events

## List Events

`$client->beta->sessions->events->list(string sessionID, ?\Datetime createdAtGt, ?\Datetime createdAtGte, ?\Datetime createdAtLt, ?\Datetime createdAtLte, ?int limit, ?Order order, ?string page, ?list<string> types, ?list<AnthropicBeta> betas, ?string workspaceID): PageCursor<ManagedAgentsSessionEvent>`

**GET** `/v1/sessions/{session_id}/events`

List Events

### Parameters

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

### Returns

- `class ManagedAgentsSessionEvent`

  - `class ManagedAgentsUserMessageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Array of content blocks comprising the user message.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsUserInterruptEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class ManagedAgentsUserToolConfirmationEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `Result result`

      UserToolConfirmationResult enum

    - `string toolUseID`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `?string denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

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

      A timestamp in RFC 3339 format

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

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.custom_tool_result` by `custom_tool_use_id`, so clients do not send it back.

  - `class ManagedAgentsAgentMessageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Array of text blocks comprising the agent response.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsAgentThinkingEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

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

      A timestamp in RFC 3339 format

    - `?EvaluatedPermission evaluatedPermission`

      AgentEvaluatedPermission enum

    - `?ManagedAgentsAgentToolEvaluation evaluation`

      Names the resolved permission_policy that produced evaluated_permission, and under auto carries the judgement. Open union: clients must tolerate unknown variants.

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.tool_confirmation` by `tool_use_id`, so clients do not send it back.

  - `class ManagedAgentsAgentMCPToolResultEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string mcpToolUseID`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

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

      A timestamp in RFC 3339 format

    - `?EvaluatedPermission evaluatedPermission`

      AgentEvaluatedPermission enum

    - `?ManagedAgentsAgentToolEvaluation evaluation`

      Names the resolved permission_policy that produced evaluated_permission, and under auto carries the judgement. Open union: clients must tolerate unknown variants.

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.tool_confirmation` or `user.tool_result` by `tool_use_id`, so clients do not send it back.

  - `class ManagedAgentsAgentToolResultEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

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

      A timestamp in RFC 3339 format

    - `?string fromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class ManagedAgentsAgentThreadMessageSentEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string toSessionThreadID`

      Public `sthr_` ID of the thread the message was sent to.

    - `?string toAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class ManagedAgentsAgentThreadContextCompactedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsSessionErrorEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `Error error`

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsSessionStatusRescheduledEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsSessionStatusRunningEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsSessionStatusIdleEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `StopReason stopReason`

  - `class ManagedAgentsSessionStatusTerminatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsSessionThreadCreatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the callable agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

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

      A timestamp in RFC 3339 format

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

      A timestamp in RFC 3339 format

    - `string result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `ManagedAgentsSpanModelUsage usage`

      Token usage for a single model request.

  - `class ManagedAgentsSpanModelRequestStartEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsSpanModelRequestEndEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `?bool isError`

      Whether the model request resulted in an error.

    - `string modelRequestStartID`

      The id of the corresponding `span.model_request_start` event.

    - `ManagedAgentsSpanModelUsage modelUsage`

      Token usage for a single model request.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsSpanOutcomeEvaluationOngoingEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

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

      A timestamp in RFC 3339 format

    - `Rubric rubric`

      Rubric for grading the quality of an outcome.

  - `class ManagedAgentsSessionDeletedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsSessionThreadStatusRunningEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that started running.

  - `class ManagedAgentsSessionThreadStatusIdleEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

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

      A timestamp in RFC 3339 format

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

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      Set by the server to the subagent thread this result was routed to. Omitted when it was routed to the primary thread.

  - `class ManagedAgentsSessionThreadStatusRescheduledEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that is retrying.

  - `class BetaManagedAgentsSessionUpdatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?BetaManagedAgentsSessionAgent agent`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `?BetaManagedAgentsBudgetLimit budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

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

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsSessionUsageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `ManagedAgentsSessionUsageSnapshot usage`

      Point-in-time snapshot of a session's cumulative usage.

    - `?BetaManagedAgentsBudgetLimit budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

### Example

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

#### Response (200)

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

## Send Events

`$client->beta->sessions->events->send(string sessionID, list<ManagedAgentsEventParams> events, ?list<AnthropicBeta> betas, ?string workspaceID): ManagedAgentsSendSessionEvents`

**POST** `/v1/sessions/{session_id}/events`

Send Events

### Parameters

- `sessionID: string`

- `events: list<ManagedAgentsEventParams>`

  Events to send to the `session`.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class ManagedAgentsSendSessionEvents`

  - `?list<Data> data`

    Sent events

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsSendSessionEvents = $client->beta->sessions->events->send(
  'sesn_011CZkZAtmR3yMPDzynEDxu7',
  events: [
    [
      'content' => [['text' => 'Where is my order #1234?', 'type' => 'text']],
      'type' => 'user.message',
    ],
  ],
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsSendSessionEvents);
```

#### Response (200)

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
    }
  ]
}
```

## Stream Events

`$client->beta->sessions->events->stream(string sessionID, ?list<BetaManagedAgentsDeltaType> eventDeltas, ?list<AnthropicBeta> betas, ?string workspaceID): ManagedAgentsStreamSessionEvents`

**GET** `/v1/sessions/{session_id}/events/stream`

Stream Events

### Parameters

- `sessionID: string`

- `eventDeltas?:optional list<BetaManagedAgentsDeltaType>`

  When set, this connection also receives streaming deltas (`event_start`, `event_delta`) while an event is being produced, before the event itself arrives. Deltas are best-effort; when the final event is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no final event — its terminal `span.model_request_end` closes the preview. Accepts one or more event types to preview and may be repeated: `agent.message` streams `content_delta` fragments; `agent.thinking` is start-only — a signal that the agent has begun extended thinking, concluded by the `agent.thinking` event itself. Only previews of the requested event types are sent.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class ManagedAgentsStreamSessionEvents`

  - `class ManagedAgentsUserMessageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Array of content blocks comprising the user message.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsUserInterruptEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class ManagedAgentsUserToolConfirmationEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `Result result`

      UserToolConfirmationResult enum

    - `string toolUseID`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `?string denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

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

      A timestamp in RFC 3339 format

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

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.custom_tool_result` by `custom_tool_use_id`, so clients do not send it back.

  - `class ManagedAgentsAgentMessageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Array of text blocks comprising the agent response.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsAgentThinkingEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

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

      A timestamp in RFC 3339 format

    - `?EvaluatedPermission evaluatedPermission`

      AgentEvaluatedPermission enum

    - `?ManagedAgentsAgentToolEvaluation evaluation`

      Names the resolved permission_policy that produced evaluated_permission, and under auto carries the judgement. Open union: clients must tolerate unknown variants.

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.tool_confirmation` by `tool_use_id`, so clients do not send it back.

  - `class ManagedAgentsAgentMCPToolResultEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string mcpToolUseID`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

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

      A timestamp in RFC 3339 format

    - `?EvaluatedPermission evaluatedPermission`

      AgentEvaluatedPermission enum

    - `?ManagedAgentsAgentToolEvaluation evaluation`

      Names the resolved permission_policy that produced evaluated_permission, and under auto carries the judgement. Open union: clients must tolerate unknown variants.

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.tool_confirmation` or `user.tool_result` by `tool_use_id`, so clients do not send it back.

  - `class ManagedAgentsAgentToolResultEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

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

      A timestamp in RFC 3339 format

    - `?string fromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class ManagedAgentsAgentThreadMessageSentEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string toSessionThreadID`

      Public `sthr_` ID of the thread the message was sent to.

    - `?string toAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class ManagedAgentsAgentThreadContextCompactedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsSessionErrorEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `Error error`

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsSessionStatusRescheduledEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsSessionStatusRunningEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsSessionStatusIdleEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `StopReason stopReason`

  - `class ManagedAgentsSessionStatusTerminatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsSessionThreadCreatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the callable agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

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

      A timestamp in RFC 3339 format

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

      A timestamp in RFC 3339 format

    - `string result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `ManagedAgentsSpanModelUsage usage`

      Token usage for a single model request.

  - `class ManagedAgentsSpanModelRequestStartEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsSpanModelRequestEndEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `?bool isError`

      Whether the model request resulted in an error.

    - `string modelRequestStartID`

      The id of the corresponding `span.model_request_start` event.

    - `ManagedAgentsSpanModelUsage modelUsage`

      Token usage for a single model request.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsSpanOutcomeEvaluationOngoingEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

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

      A timestamp in RFC 3339 format

    - `Rubric rubric`

      Rubric for grading the quality of an outcome.

  - `class ManagedAgentsSessionDeletedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsSessionThreadStatusRunningEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that started running.

  - `class ManagedAgentsSessionThreadStatusIdleEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

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

      A timestamp in RFC 3339 format

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

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      Set by the server to the subagent thread this result was routed to. Omitted when it was routed to the primary thread.

  - `class ManagedAgentsSessionThreadStatusRescheduledEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that is retrying.

  - `class BetaManagedAgentsSessionUpdatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?BetaManagedAgentsSessionAgent agent`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `?BetaManagedAgentsBudgetLimit budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `?array<string,string> metadata`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `?string title`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsStartEvent`

    - `Type type`

    - `BetaManagedAgentsStartEventPreview event`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

  - `class BetaManagedAgentsDeltaEvent`

    - `Type type`

    - `BetaManagedAgentsDeltaContent delta`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

    - `string eventID`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

  - `class BetaManagedAgentsSystemMessageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<BetaManagedAgentsSystemContentBlock> content`

      System content blocks. Text-only.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsSessionUsageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `ManagedAgentsSessionUsageSnapshot usage`

      Point-in-time snapshot of a session's cumulative usage.

    - `?BetaManagedAgentsBudgetLimit budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsStreamSessionEvents = $client
  ->beta
  ->sessions
  ->events
  ->streamStream(
  'sesn_011CZkZAtmR3yMPDzynEDxu7',
  eventDeltas: [BetaManagedAgentsDeltaType::AGENT_MESSAGE],
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsStreamSessionEvents);
```

#### Response (200)

```json
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
}
```

## Domain types

### Beta Managed Agents Agent Auto Evaluated Permission

- `class ManagedAgentsAgentAutoEvaluatedPermission`

  - `class ManagedAgentsAgentAutoEvaluatedPermissionAllow`

    - `"allow" type`

  - `class ManagedAgentsAgentAutoEvaluatedPermissionAsk`

    - `"ask" type`

    - `string reasonCode`

      The judgement's grounds in registry-bound terms, for client branching and audit rather than end-user display. Open registry; currently "indeterminate" (no judgement was reached). Clients must tolerate values outside this set.

  - `class ManagedAgentsAgentAutoEvaluatedPermissionDeny`

    - `"deny" type`

    - `string reasonCode`

      The judgement's grounds in registry-bound terms. Open registry; currently "high_risk" (judged high-risk; the call does not run). Clients must tolerate values outside this set.

### Beta Managed Agents Agent Auto Evaluated Permission Allow

- `class ManagedAgentsAgentAutoEvaluatedPermissionAllow`

  - `"allow" type`

### Beta Managed Agents Agent Auto Evaluated Permission Ask

- `class ManagedAgentsAgentAutoEvaluatedPermissionAsk`

  - `"ask" type`

  - `string reasonCode`

    The judgement's grounds in registry-bound terms, for client branching and audit rather than end-user display. Open registry; currently "indeterminate" (no judgement was reached). Clients must tolerate values outside this set.

### Beta Managed Agents Agent Auto Evaluated Permission Deny

- `class ManagedAgentsAgentAutoEvaluatedPermissionDeny`

  - `"deny" type`

  - `string reasonCode`

    The judgement's grounds in registry-bound terms. Open registry; currently "high_risk" (judged high-risk; the call does not run). Clients must tolerate values outside this set.

### Beta Managed Agents Agent Custom Tool Use Event

- `class ManagedAgentsAgentCustomToolUseEvent`

  - `Type type`

  - `string id`

    Unique identifier for this event.

  - `array<string,mixed> input`

    Input parameters for the tool call.

  - `string name`

    Name of the custom tool being called.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `?string sessionThreadID`

    When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.custom_tool_result` by `custom_tool_use_id`, so clients do not send it back.

### Beta Managed Agents Agent MCP Tool Result Event

- `class ManagedAgentsAgentMCPToolResultEvent`

  - `Type type`

  - `string id`

    Unique identifier for this event.

  - `string mcpToolUseID`

    The id of the `agent.mcp_tool_use` event this result corresponds to.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `?list<Content> content`

    The result content returned by the tool.

  - `?bool isError`

    Whether the tool execution resulted in an error.

### Beta Managed Agents Agent MCP Tool Use Event

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

    A timestamp in RFC 3339 format

  - `?EvaluatedPermission evaluatedPermission`

    AgentEvaluatedPermission enum

  - `?ManagedAgentsAgentToolEvaluation evaluation`

    Names the resolved permission_policy that produced evaluated_permission, and under auto carries the judgement. Open union: clients must tolerate unknown variants.

  - `?string sessionThreadID`

    When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.tool_confirmation` by `tool_use_id`, so clients do not send it back.

### Beta Managed Agents Agent Message Event

- `class ManagedAgentsAgentMessageEvent`

  - `Type type`

  - `string id`

    Unique identifier for this event.

  - `list<Content> content`

    Array of text blocks comprising the agent response.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

### Beta Managed Agents Agent Thinking Event

- `class ManagedAgentsAgentThinkingEvent`

  - `Type type`

  - `string id`

    Unique identifier for this event.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

### Beta Managed Agents Agent Thread Context Compacted Event

- `class ManagedAgentsAgentThreadContextCompactedEvent`

  - `Type type`

  - `string id`

    Unique identifier for this event.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

### Beta Managed Agents Agent Thread Message Received Event

- `class ManagedAgentsAgentThreadMessageReceivedEvent`

  - `Type type`

  - `string id`

    Unique identifier for this event.

  - `list<Content> content`

    Message content blocks.

  - `string fromSessionThreadID`

    Public `sthr_` ID of the thread that sent the message.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `?string fromAgentName`

    Name of the callable agent this message came from. Absent when received from the primary agent.

### Beta Managed Agents Agent Thread Message Sent Event

- `class ManagedAgentsAgentThreadMessageSentEvent`

  - `Type type`

  - `string id`

    Unique identifier for this event.

  - `list<Content> content`

    Message content blocks.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `string toSessionThreadID`

    Public `sthr_` ID of the thread the message was sent to.

  - `?string toAgentName`

    Name of the callable agent this message was sent to. Absent when sent to the primary agent.

### Beta Managed Agents Agent Tool Evaluation

- `class ManagedAgentsAgentToolEvaluation`

  - `class ManagedAgentsAgentToolEvaluationAlwaysAllow`

    - `"always_allow" type`

  - `class ManagedAgentsAgentToolEvaluationAlwaysAsk`

    - `"always_ask" type`

  - `class ManagedAgentsAgentToolEvaluationAuto`

    - `"auto" type`

    - `ManagedAgentsAgentAutoEvaluatedPermission evaluatedPermission`

      The server's per-invocation judgement under the auto permission policy. Its type always equals the event's top-level evaluated_permission. Open union: clients must tolerate unknown variants.

### Beta Managed Agents Agent Tool Evaluation Always Allow

- `class ManagedAgentsAgentToolEvaluationAlwaysAllow`

  - `"always_allow" type`

### Beta Managed Agents Agent Tool Evaluation Always Ask

- `class ManagedAgentsAgentToolEvaluationAlwaysAsk`

  - `"always_ask" type`

### Beta Managed Agents Agent Tool Evaluation Auto

- `class ManagedAgentsAgentToolEvaluationAuto`

  - `"auto" type`

  - `ManagedAgentsAgentAutoEvaluatedPermission evaluatedPermission`

    The server's per-invocation judgement under the auto permission policy. Its type always equals the event's top-level evaluated_permission. Open union: clients must tolerate unknown variants.

### Beta Managed Agents Agent Tool Result Event

- `class ManagedAgentsAgentToolResultEvent`

  - `Type type`

  - `string id`

    Unique identifier for this event.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `string toolUseID`

    The id of the `agent.tool_use` event this result corresponds to.

  - `?list<Content> content`

    The result content returned by the tool.

  - `?bool isError`

    Whether the tool execution resulted in an error.

### Beta Managed Agents Agent Tool Use Event

- `class ManagedAgentsAgentToolUseEvent`

  - `Type type`

  - `string id`

    Unique identifier for this event.

  - `array<string,mixed> input`

    Input parameters for the tool call.

  - `string name`

    Name of the agent tool being used.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `?EvaluatedPermission evaluatedPermission`

    AgentEvaluatedPermission enum

  - `?ManagedAgentsAgentToolEvaluation evaluation`

    Names the resolved permission_policy that produced evaluated_permission, and under auto carries the judgement. Open union: clients must tolerate unknown variants.

  - `?string sessionThreadID`

    When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.tool_confirmation` or `user.tool_result` by `tool_use_id`, so clients do not send it back.

### Beta Managed Agents Base64 Document Source

- `class ManagedAgentsBase64DocumentSource`

  - `Type type`

  - `string data`

    Base64-encoded document data.

  - `string mediaType`

    MIME type of the document (e.g., "application/pdf").

### Beta Managed Agents Base64 Image Source

- `class ManagedAgentsBase64ImageSource`

  - `Type type`

  - `string data`

    Base64-encoded image data.

  - `string mediaType`

    MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

### Beta Managed Agents Billing Error

- `class ManagedAgentsBillingError`

  - `Type type`

  - `string message`

    Human-readable error description.

  - `RetryStatus retryStatus`

    What the client should do next in response to this error.

### Beta Managed Agents Credential Host Unreachable Error

- `class ManagedAgentsCredentialHostUnreachableError`

  - `Type type`

  - `string credentialID`

    ID of the affected credential.

  - `string message`

    Human-readable error description.

  - `RetryStatus retryStatus`

    What the client should do next in response to this error.

  - `string vaultID`

    ID of the vault containing the affected credential.

### Beta Managed Agents Document Block

- `class ManagedAgentsDocumentBlock`

  - `Type type`

  - `Source source`

    Union type for document source variants.

  - `?string context`

    Additional context about the document for the model.

  - `?string title`

    The title of the document.

### Beta Managed Agents Event Params

- `class ManagedAgentsEventParams`

  - `class ManagedAgentsUserMessageEventParams`

    - `Type type`

    - `list<Content> content`

      Array of content blocks for the user message.

  - `class ManagedAgentsUserInterruptEventParams`

    - `Type type`

    - `?string sessionThreadID`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class ManagedAgentsUserToolConfirmationEventParams`

    - `Type type`

    - `Result result`

      UserToolConfirmationResult enum

    - `string toolUseID`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `?string denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

  - `class ManagedAgentsUserCustomToolResultEventParams`

    - `Type type`

    - `string customToolUseID`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `class ManagedAgentsUserDefineOutcomeEventParams`

    - `Type type`

    - `string description`

      What the agent should produce. This is the task specification.

    - `Rubric rubric`

      Rubric for grading the quality of an outcome.

    - `?int maxIterations`

      Eval→revision cycles before giving up. Default 3, max 20.

  - `class ManagedAgentsUserToolResultEventParams`

    - `Type type`

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `class ManagedAgentsSystemMessageEventParams`

    - `Type type`

    - `list<BetaManagedAgentsSystemContentBlock> content`

      System content blocks to append. Text-only.

### Beta Managed Agents File Document Source

- `class ManagedAgentsFileDocumentSource`

  - `Type type`

  - `string fileID`

    ID of a previously uploaded file.

### Beta Managed Agents File Image Source

- `class ManagedAgentsFileImageSource`

  - `Type type`

  - `string fileID`

    ID of a previously uploaded file.

### Beta Managed Agents File Rubric

- `class ManagedAgentsFileRubric`

  - `Type type`

  - `string fileID`

    ID of the rubric file.

### Beta Managed Agents File Rubric Params

- `class ManagedAgentsFileRubricParams`

  - `Type type`

  - `string fileID`

    ID of the rubric file.

### Beta Managed Agents Image Block

- `class ManagedAgentsImageBlock`

  - `Type type`

  - `Source source`

    Union type for image source variants.

### Beta Managed Agents MCP Authentication Failed Error

- `class ManagedAgentsMCPAuthenticationFailedError`

  - `Type type`

  - `string mcpServerName`

    Name of the MCP server that failed authentication.

  - `string message`

    Human-readable error description.

  - `RetryStatus retryStatus`

    What the client should do next in response to this error.

### Beta Managed Agents MCP Connection Failed Error

- `class ManagedAgentsMCPConnectionFailedError`

  - `Type type`

  - `string mcpServerName`

    Name of the MCP server that failed to connect.

  - `string message`

    Human-readable error description.

  - `RetryStatus retryStatus`

    What the client should do next in response to this error.

### Beta Managed Agents Model Overloaded Error

- `class ManagedAgentsModelOverloadedError`

  - `Type type`

  - `string message`

    Human-readable error description.

  - `RetryStatus retryStatus`

    What the client should do next in response to this error.

### Beta Managed Agents Model Rate Limited Error

- `class ManagedAgentsModelRateLimitedError`

  - `Type type`

  - `string message`

    Human-readable error description.

  - `RetryStatus retryStatus`

    What the client should do next in response to this error.

### Beta Managed Agents Model Request Failed Error

- `class ManagedAgentsModelRequestFailedError`

  - `Type type`

  - `string message`

    Human-readable error description.

  - `RetryStatus retryStatus`

    What the client should do next in response to this error.

### Beta Managed Agents Plain Text Document Source

- `class ManagedAgentsPlainTextDocumentSource`

  - `Type type`

  - `string data`

    The plain text content.

  - `MediaType mediaType`

    MIME type of the text content. Must be "text/plain".

### Beta Managed Agents Redacted Block

- `class ManagedAgentsRedactedBlock`

  - `Type type`

### Beta Managed Agents Retry Status Exhausted

- `class ManagedAgentsRetryStatusExhausted`

  - `Type type`

### Beta Managed Agents Retry Status Retrying

- `class ManagedAgentsRetryStatusRetrying`

  - `Type type`

### Beta Managed Agents Retry Status Terminal

- `class ManagedAgentsRetryStatusTerminal`

  - `Type type`

### Beta Managed Agents Search Result Block

- `class ManagedAgentsSearchResultBlock`

  - `Type type`

  - `ManagedAgentsSearchResultCitations citations`

    Citation settings for a search result.

  - `list<ManagedAgentsSearchResultContent> content`

    Array of text content blocks from the search result.

  - `string source`

    The URL source of the search result.

  - `string title`

    The title of the search result.

### Beta Managed Agents Search Result Citations

- `class ManagedAgentsSearchResultCitations`

  - `bool enabled`

    Whether citations are enabled for this search result.

### Beta Managed Agents Search Result Content

- `class ManagedAgentsSearchResultContent`

  - `Type type`

  - `string text`

    The text content.

### Beta Managed Agents Send Session Events

- `class ManagedAgentsSendSessionEvents`

  - `?list<Data> data`

    Sent events

### Beta Managed Agents Session Budget Reached

- `class ManagedAgentsSessionBudgetReached`

  - `Type type`

### Beta Managed Agents Session Deleted Event

- `class ManagedAgentsSessionDeletedEvent`

  - `Type type`

  - `string id`

    Unique identifier for this event.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

### Beta Managed Agents Session End Turn

- `class ManagedAgentsSessionEndTurn`

  - `Type type`

### Beta Managed Agents Session Error Event

- `class ManagedAgentsSessionErrorEvent`

  - `Type type`

  - `string id`

    Unique identifier for this event.

  - `Error error`

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

### Beta Managed Agents Session Event

- `class ManagedAgentsSessionEvent`

  - `class ManagedAgentsUserMessageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Array of content blocks comprising the user message.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsUserInterruptEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class ManagedAgentsUserToolConfirmationEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `Result result`

      UserToolConfirmationResult enum

    - `string toolUseID`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `?string denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

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

      A timestamp in RFC 3339 format

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

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.custom_tool_result` by `custom_tool_use_id`, so clients do not send it back.

  - `class ManagedAgentsAgentMessageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Array of text blocks comprising the agent response.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsAgentThinkingEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

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

      A timestamp in RFC 3339 format

    - `?EvaluatedPermission evaluatedPermission`

      AgentEvaluatedPermission enum

    - `?ManagedAgentsAgentToolEvaluation evaluation`

      Names the resolved permission_policy that produced evaluated_permission, and under auto carries the judgement. Open union: clients must tolerate unknown variants.

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.tool_confirmation` by `tool_use_id`, so clients do not send it back.

  - `class ManagedAgentsAgentMCPToolResultEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string mcpToolUseID`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

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

      A timestamp in RFC 3339 format

    - `?EvaluatedPermission evaluatedPermission`

      AgentEvaluatedPermission enum

    - `?ManagedAgentsAgentToolEvaluation evaluation`

      Names the resolved permission_policy that produced evaluated_permission, and under auto carries the judgement. Open union: clients must tolerate unknown variants.

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.tool_confirmation` or `user.tool_result` by `tool_use_id`, so clients do not send it back.

  - `class ManagedAgentsAgentToolResultEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

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

      A timestamp in RFC 3339 format

    - `?string fromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class ManagedAgentsAgentThreadMessageSentEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string toSessionThreadID`

      Public `sthr_` ID of the thread the message was sent to.

    - `?string toAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class ManagedAgentsAgentThreadContextCompactedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsSessionErrorEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `Error error`

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsSessionStatusRescheduledEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsSessionStatusRunningEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsSessionStatusIdleEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `StopReason stopReason`

  - `class ManagedAgentsSessionStatusTerminatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsSessionThreadCreatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the callable agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

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

      A timestamp in RFC 3339 format

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

      A timestamp in RFC 3339 format

    - `string result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `ManagedAgentsSpanModelUsage usage`

      Token usage for a single model request.

  - `class ManagedAgentsSpanModelRequestStartEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsSpanModelRequestEndEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `?bool isError`

      Whether the model request resulted in an error.

    - `string modelRequestStartID`

      The id of the corresponding `span.model_request_start` event.

    - `ManagedAgentsSpanModelUsage modelUsage`

      Token usage for a single model request.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsSpanOutcomeEvaluationOngoingEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

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

      A timestamp in RFC 3339 format

    - `Rubric rubric`

      Rubric for grading the quality of an outcome.

  - `class ManagedAgentsSessionDeletedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsSessionThreadStatusRunningEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that started running.

  - `class ManagedAgentsSessionThreadStatusIdleEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

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

      A timestamp in RFC 3339 format

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

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      Set by the server to the subagent thread this result was routed to. Omitted when it was routed to the primary thread.

  - `class ManagedAgentsSessionThreadStatusRescheduledEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that is retrying.

  - `class BetaManagedAgentsSessionUpdatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?BetaManagedAgentsSessionAgent agent`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `?BetaManagedAgentsBudgetLimit budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

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

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsSessionUsageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `ManagedAgentsSessionUsageSnapshot usage`

      Point-in-time snapshot of a session's cumulative usage.

    - `?BetaManagedAgentsBudgetLimit budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

### Beta Managed Agents Session Requires Action

- `class ManagedAgentsSessionRequiresAction`

  - `Type type`

  - `list<string> eventIDs`

    The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

### Beta Managed Agents Session Retries Exhausted

- `class ManagedAgentsSessionRetriesExhausted`

  - `Type type`

### Beta Managed Agents Session Status Idle Event

- `class ManagedAgentsSessionStatusIdleEvent`

  - `Type type`

  - `string id`

    Unique identifier for this event.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `StopReason stopReason`

### Beta Managed Agents Session Status Rescheduled Event

- `class ManagedAgentsSessionStatusRescheduledEvent`

  - `Type type`

  - `string id`

    Unique identifier for this event.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

### Beta Managed Agents Session Status Running Event

- `class ManagedAgentsSessionStatusRunningEvent`

  - `Type type`

  - `string id`

    Unique identifier for this event.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

### Beta Managed Agents Session Status Terminated Event

- `class ManagedAgentsSessionStatusTerminatedEvent`

  - `Type type`

  - `string id`

    Unique identifier for this event.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

### Beta Managed Agents Session Thread Created Event

- `class ManagedAgentsSessionThreadCreatedEvent`

  - `Type type`

  - `string id`

    Unique identifier for this event.

  - `string agentName`

    Name of the callable agent the thread runs.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `string sessionThreadID`

    Public `sthr_` ID of the newly created thread.

### Beta Managed Agents Session Thread Status Idle Event

- `class ManagedAgentsSessionThreadStatusIdleEvent`

  - `Type type`

  - `string id`

    Unique identifier for this event.

  - `string agentName`

    Name of the agent the thread runs.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `string sessionThreadID`

    Public sthr_ ID of the thread that went idle.

  - `StopReason stopReason`

### Beta Managed Agents Session Thread Status Rescheduled Event

- `class ManagedAgentsSessionThreadStatusRescheduledEvent`

  - `Type type`

  - `string id`

    Unique identifier for this event.

  - `string agentName`

    Name of the agent the thread runs.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `string sessionThreadID`

    Public sthr_ ID of the thread that is retrying.

### Beta Managed Agents Session Thread Status Running Event

- `class ManagedAgentsSessionThreadStatusRunningEvent`

  - `Type type`

  - `string id`

    Unique identifier for this event.

  - `string agentName`

    Name of the agent the thread runs.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `string sessionThreadID`

    Public sthr_ ID of the thread that started running.

### Beta Managed Agents Session Thread Status Terminated Event

- `class ManagedAgentsSessionThreadStatusTerminatedEvent`

  - `Type type`

  - `string id`

    Unique identifier for this event.

  - `string agentName`

    Name of the agent the thread runs.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `string sessionThreadID`

    Public sthr_ ID of the thread that terminated.

### Beta Managed Agents Session Usage Snapshot

- `class ManagedAgentsSessionUsageSnapshot`

  - `?float activeSeconds`

    Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

  - `?BetaManagedAgentsCacheCreationUsage cacheCreation`

    Prompt-cache creation token usage broken down by cache lifetime.

  - `?int cacheReadInputTokens`

    Total tokens read from prompt cache.

  - `?int inputTokens`

    Total input tokens consumed across all turns.

  - `?BetaMonetaryAmount listCost`

    A monetary amount in a specific currency.

  - `?int outputTokens`

    Total output tokens generated across all turns.

  - `?BetaManagedAgentsServerToolUsage serverToolUse`

    Cumulative count of server-executed tool invocations, broken down by tool.

### Beta Managed Agents Span Model Request End Event

- `class ManagedAgentsSpanModelRequestEndEvent`

  - `Type type`

  - `string id`

    Unique identifier for this event.

  - `?bool isError`

    Whether the model request resulted in an error.

  - `string modelRequestStartID`

    The id of the corresponding `span.model_request_start` event.

  - `ManagedAgentsSpanModelUsage modelUsage`

    Token usage for a single model request.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

### Beta Managed Agents Span Model Request Start Event

- `class ManagedAgentsSpanModelRequestStartEvent`

  - `Type type`

  - `string id`

    Unique identifier for this event.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

### Beta Managed Agents Span Model Usage

- `class ManagedAgentsSpanModelUsage`

  - `int cacheCreationInputTokens`

    Tokens used to create prompt cache in this request.

  - `int cacheReadInputTokens`

    Tokens read from prompt cache in this request.

  - `int inputTokens`

    Input tokens consumed by this request.

  - `int outputTokens`

    Output tokens generated by this request.

  - `?Speed speed`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

### Beta Managed Agents Span Outcome Evaluation End Event

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

    A timestamp in RFC 3339 format

  - `string result`

    Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

  - `ManagedAgentsSpanModelUsage usage`

    Token usage for a single model request.

### Beta Managed Agents Span Outcome Evaluation Ongoing Event

- `class ManagedAgentsSpanOutcomeEvaluationOngoingEvent`

  - `Type type`

  - `string id`

    Unique identifier for this event.

  - `int iteration`

    0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

  - `string outcomeID`

    The `outc_` ID of the outcome being evaluated.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

### Beta Managed Agents Span Outcome Evaluation Start Event

- `class ManagedAgentsSpanOutcomeEvaluationStartEvent`

  - `Type type`

  - `string id`

    Unique identifier for this event.

  - `int iteration`

    0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

  - `string outcomeID`

    The `outc_` ID of the outcome being evaluated.

  - `\Datetime processedAt`

    A timestamp in RFC 3339 format

### Beta Managed Agents Stream Session Events

- `class ManagedAgentsStreamSessionEvents`

  - `class ManagedAgentsUserMessageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Array of content blocks comprising the user message.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsUserInterruptEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class ManagedAgentsUserToolConfirmationEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `Result result`

      UserToolConfirmationResult enum

    - `string toolUseID`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `?string denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

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

      A timestamp in RFC 3339 format

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

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.custom_tool_result` by `custom_tool_use_id`, so clients do not send it back.

  - `class ManagedAgentsAgentMessageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Array of text blocks comprising the agent response.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsAgentThinkingEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

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

      A timestamp in RFC 3339 format

    - `?EvaluatedPermission evaluatedPermission`

      AgentEvaluatedPermission enum

    - `?ManagedAgentsAgentToolEvaluation evaluation`

      Names the resolved permission_policy that produced evaluated_permission, and under auto carries the judgement. Open union: clients must tolerate unknown variants.

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.tool_confirmation` by `tool_use_id`, so clients do not send it back.

  - `class ManagedAgentsAgentMCPToolResultEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string mcpToolUseID`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

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

      A timestamp in RFC 3339 format

    - `?EvaluatedPermission evaluatedPermission`

      AgentEvaluatedPermission enum

    - `?ManagedAgentsAgentToolEvaluation evaluation`

      Names the resolved permission_policy that produced evaluated_permission, and under auto carries the judgement. Open union: clients must tolerate unknown variants.

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.tool_confirmation` or `user.tool_result` by `tool_use_id`, so clients do not send it back.

  - `class ManagedAgentsAgentToolResultEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

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

      A timestamp in RFC 3339 format

    - `?string fromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class ManagedAgentsAgentThreadMessageSentEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string toSessionThreadID`

      Public `sthr_` ID of the thread the message was sent to.

    - `?string toAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class ManagedAgentsAgentThreadContextCompactedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsSessionErrorEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `Error error`

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsSessionStatusRescheduledEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsSessionStatusRunningEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsSessionStatusIdleEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `StopReason stopReason`

  - `class ManagedAgentsSessionStatusTerminatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsSessionThreadCreatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the callable agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

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

      A timestamp in RFC 3339 format

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

      A timestamp in RFC 3339 format

    - `string result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `ManagedAgentsSpanModelUsage usage`

      Token usage for a single model request.

  - `class ManagedAgentsSpanModelRequestStartEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsSpanModelRequestEndEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `?bool isError`

      Whether the model request resulted in an error.

    - `string modelRequestStartID`

      The id of the corresponding `span.model_request_start` event.

    - `ManagedAgentsSpanModelUsage modelUsage`

      Token usage for a single model request.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsSpanOutcomeEvaluationOngoingEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

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

      A timestamp in RFC 3339 format

    - `Rubric rubric`

      Rubric for grading the quality of an outcome.

  - `class ManagedAgentsSessionDeletedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class ManagedAgentsSessionThreadStatusRunningEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that started running.

  - `class ManagedAgentsSessionThreadStatusIdleEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

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

      A timestamp in RFC 3339 format

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

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      Set by the server to the subagent thread this result was routed to. Omitted when it was routed to the primary thread.

  - `class ManagedAgentsSessionThreadStatusRescheduledEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that is retrying.

  - `class BetaManagedAgentsSessionUpdatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?BetaManagedAgentsSessionAgent agent`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `?BetaManagedAgentsBudgetLimit budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `?array<string,string> metadata`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `?string title`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsStartEvent`

    - `Type type`

    - `BetaManagedAgentsStartEventPreview event`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

  - `class BetaManagedAgentsDeltaEvent`

    - `Type type`

    - `BetaManagedAgentsDeltaContent delta`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

    - `string eventID`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

  - `class BetaManagedAgentsSystemMessageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<BetaManagedAgentsSystemContentBlock> content`

      System content blocks. Text-only.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `class BetaManagedAgentsSessionUsageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `ManagedAgentsSessionUsageSnapshot usage`

      Point-in-time snapshot of a session's cumulative usage.

    - `?BetaManagedAgentsBudgetLimit budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

### Beta Managed Agents System Message Event Params

- `class ManagedAgentsSystemMessageEventParams`

  - `Type type`

  - `list<BetaManagedAgentsSystemContentBlock> content`

    System content blocks to append. Text-only.

### Beta Managed Agents Text Block

- `class ManagedAgentsTextBlock`

  - `Type type`

  - `string text`

    The text content.

### Beta Managed Agents Text Rubric

- `class ManagedAgentsTextRubric`

  - `Type type`

  - `string content`

    Rubric content. Plain text or markdown — the grader treats it as freeform text.

### Beta Managed Agents Text Rubric Params

- `class ManagedAgentsTextRubricParams`

  - `Type type`

  - `string content`

    Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

### Beta Managed Agents Unknown Error

- `class ManagedAgentsUnknownError`

  - `Type type`

  - `string message`

    Human-readable error description.

  - `RetryStatus retryStatus`

    What the client should do next in response to this error.

### Beta Managed Agents URL Document Source

- `class ManagedAgentsURLDocumentSource`

  - `Type type`

  - `string url`

    URL of the document to fetch.

### Beta Managed Agents URL Image Source

- `class ManagedAgentsURLImageSource`

  - `Type type`

  - `string url`

    URL of the image to fetch.

### Beta Managed Agents User Custom Tool Result Event

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

    A timestamp in RFC 3339 format

  - `?string sessionThreadID`

    Set by the server to the subagent thread this result was routed to. Omitted when it was routed to the primary thread.

### Beta Managed Agents User Custom Tool Result Event Params

- `class ManagedAgentsUserCustomToolResultEventParams`

  - `Type type`

  - `string customToolUseID`

    The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `?list<Content> content`

    The result content returned by the tool.

  - `?bool isError`

    Whether the tool execution resulted in an error.

### Beta Managed Agents User Define Outcome Event

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

    A timestamp in RFC 3339 format

  - `Rubric rubric`

    Rubric for grading the quality of an outcome.

### Beta Managed Agents User Define Outcome Event Params

- `class ManagedAgentsUserDefineOutcomeEventParams`

  - `Type type`

  - `string description`

    What the agent should produce. This is the task specification.

  - `Rubric rubric`

    Rubric for grading the quality of an outcome.

  - `?int maxIterations`

    Eval→revision cycles before giving up. Default 3, max 20.

### Beta Managed Agents User Interrupt Event

- `class ManagedAgentsUserInterruptEvent`

  - `Type type`

  - `string id`

    Unique identifier for this event.

  - `?\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `?string sessionThreadID`

    If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

### Beta Managed Agents User Interrupt Event Params

- `class ManagedAgentsUserInterruptEventParams`

  - `Type type`

  - `?string sessionThreadID`

    If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

### Beta Managed Agents User Message Event

- `class ManagedAgentsUserMessageEvent`

  - `Type type`

  - `string id`

    Unique identifier for this event.

  - `list<Content> content`

    Array of content blocks comprising the user message.

  - `?\Datetime processedAt`

    A timestamp in RFC 3339 format

### Beta Managed Agents User Message Event Params

- `class ManagedAgentsUserMessageEventParams`

  - `Type type`

  - `list<Content> content`

    Array of content blocks for the user message.

### Beta Managed Agents User Tool Confirmation Event

- `class ManagedAgentsUserToolConfirmationEvent`

  - `Type type`

  - `string id`

    Unique identifier for this event.

  - `Result result`

    UserToolConfirmationResult enum

  - `string toolUseID`

    The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `?string denyMessage`

    Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

  - `?\Datetime processedAt`

    A timestamp in RFC 3339 format

  - `?string sessionThreadID`

    Set by the server to the subagent thread this confirmation was routed to. Omitted when it was routed to the primary thread.

### Beta Managed Agents User Tool Confirmation Event Params

- `class ManagedAgentsUserToolConfirmationEventParams`

  - `Type type`

  - `Result result`

    UserToolConfirmationResult enum

  - `string toolUseID`

    The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `?string denyMessage`

    Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

### Beta Managed Agents User Tool Result Event Params

- `class ManagedAgentsUserToolResultEventParams`

  - `Type type`

  - `string toolUseID`

    The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `?list<Content> content`

    The result content returned by the tool.

  - `?bool isError`

    Whether the tool execution resulted in an error.
