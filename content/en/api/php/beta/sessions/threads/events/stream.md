---
title: Stream Session Thread Events
url: https://platform.claude.com/docs/en/api/php/beta/sessions/threads/events/stream
---

# Stream Session Thread Events

`$client->beta->sessions->threads->events->stream(string threadID, string sessionID, ?list<BetaManagedAgentsDeltaType> eventDeltas, ?list<AnthropicBeta> betas, ?string workspaceID): ManagedAgentsStreamSessionThreadEvents`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}/stream`

Stream Session Thread Events

## Parameters

- `sessionID: string`

- `threadID: string`

- `eventDeltas?:optional list<BetaManagedAgentsDeltaType>`

  When set, this connection also receives streaming deltas (`event_start`, `event_delta`) while an event is being produced, before the event itself arrives. Deltas are best-effort; when the final event is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no final event — its terminal `span.model_request_end` closes the preview. Accepts one or more event types to preview and may be repeated: `agent.message` streams `content_delta` fragments; `agent.thinking` is start-only — a signal that the agent has begun extended thinking, concluded by the `agent.thinking` event itself. Only previews of the requested event types are sent.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

## Returns

- `ManagedAgentsStreamSessionThreadEvents`

  - `ManagedAgentsUserMessageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Array of content blocks comprising the user message.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `ManagedAgentsUserInterruptEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `?string sessionThreadID`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `ManagedAgentsUserToolConfirmationEvent`

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

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `ManagedAgentsUserCustomToolResultEvent`

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

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `ManagedAgentsAgentCustomToolUseEvent`

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

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `ManagedAgentsAgentMessageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Array of text blocks comprising the agent response.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `ManagedAgentsAgentThinkingEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `ManagedAgentsAgentMCPToolUseEvent`

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

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `ManagedAgentsAgentMCPToolResultEvent`

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

  - `ManagedAgentsAgentToolUseEvent`

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

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `ManagedAgentsAgentToolResultEvent`

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

  - `ManagedAgentsAgentThreadMessageReceivedEvent`

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

  - `ManagedAgentsAgentThreadMessageSentEvent`

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

  - `ManagedAgentsAgentThreadContextCompactedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `ManagedAgentsSessionErrorEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `Error error`

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `ManagedAgentsSessionStatusRescheduledEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `ManagedAgentsSessionStatusRunningEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `ManagedAgentsSessionStatusIdleEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `StopReason stopReason`

  - `ManagedAgentsSessionStatusTerminatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `ManagedAgentsSessionThreadCreatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the callable agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public `sthr_` ID of the newly created thread.

  - `ManagedAgentsSpanOutcomeEvaluationStartEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `ManagedAgentsSpanOutcomeEvaluationEndEvent`

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

  - `ManagedAgentsSpanModelRequestStartEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `ManagedAgentsSpanModelRequestEndEvent`

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

  - `ManagedAgentsSpanOutcomeEvaluationOngoingEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `ManagedAgentsUserDefineOutcomeEvent`

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

  - `ManagedAgentsSessionDeletedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `ManagedAgentsSessionThreadStatusRunningEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that started running.

  - `ManagedAgentsSessionThreadStatusIdleEvent`

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

  - `ManagedAgentsSessionThreadStatusTerminatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that terminated.

  - `BetaManagedAgentsUserToolResultEvent`

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

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `ManagedAgentsSessionThreadStatusRescheduledEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `string sessionThreadID`

      Public sthr_ ID of the thread that is retrying.

  - `BetaManagedAgentsSessionUpdatedEvent`

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

  - `BetaManagedAgentsStartEvent`

    - `Type type`

    - `BetaManagedAgentsStartEventPreview event`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

  - `BetaManagedAgentsDeltaEvent`

    - `Type type`

    - `BetaManagedAgentsDeltaContent delta`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

    - `string eventID`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

  - `BetaManagedAgentsSystemMessageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<BetaManagedAgentsSystemContentBlock> content`

      System content blocks. Text-only.

    - `?\Datetime processedAt`

      A timestamp in RFC 3339 format

  - `BetaManagedAgentsSessionUsageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      A timestamp in RFC 3339 format

    - `ManagedAgentsSessionUsageSnapshot usage`

      Point-in-time snapshot of a session's cumulative usage.

    - `?BetaManagedAgentsBudgetLimit budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

## Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsStreamSessionThreadEvents = $client
  ->beta
  ->sessions
  ->threads
  ->events
  ->streamStream(
  'sthr_011CZkZVWa6oIjw0rgXZpnBt',
  sessionID: 'sesn_011CZkZAtmR3yMPDzynEDxu7',
  eventDeltas: [BetaManagedAgentsDeltaType::AGENT_MESSAGE],
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsStreamSessionThreadEvents);
```

### Response (200)

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
