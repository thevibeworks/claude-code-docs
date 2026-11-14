---
title: List Session Thread Events
url: https://platform.claude.com/docs/en/api/typescript/beta/sessions/threads/events/list
---

# List Session Thread Events

- Signature: `client.beta.sessions.threads.events.list(threadID: string, params: EventListParams, options?: RequestOptions): PageCursor<BetaManagedAgentsSessionEvent>`
- Endpoint: `GET /v1/sessions/{session_id}/threads/{thread_id}/events`
- Beta header: `anthropic-beta: managed-agents-2026-04-01`

## Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaManagedAgentsSessionEvent of client.beta.sessions.threads.events.list(
  "sthr_011CZkZVWa6oJjw1rgXZpnBt",
  { session_id: "sesn_011CZkZAtmR3yMPDzynEDxu7" }
)) {
  console.log(betaManagedAgentsSessionEvent);
}
```

## Example response (200)

```json
{
  "data": [
    {
      "id": "sevt_011CZkZGPp1iBcp4kaQSihUm",
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
      "id": "sevt_011CZkZHPq1jCdq5mbRTjiVn",
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

## Parameters

```ts
threadID: string; // path parameter

interface EventListParams {
  session_id: string; // path parameter
  limit?: number; // query parameter, format: int32
  page?: string; // query parameter
  /** This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

## Returns

```ts
/** Union type for all event types in a session. */
type BetaManagedAgentsSessionEvent = BetaManagedAgentsUserMessageEvent | BetaManagedAgentsUserInterruptEvent | BetaManagedAgentsUserToolConfirmationEvent | BetaManagedAgentsUserCustomToolResultEvent | BetaManagedAgentsAgentCustomToolUseEvent | BetaManagedAgentsAgentMessageEvent | BetaManagedAgentsAgentThinkingEvent | BetaManagedAgentsAgentMCPToolUseEvent | BetaManagedAgentsAgentMCPToolResultEvent | BetaManagedAgentsAgentToolUseEvent | BetaManagedAgentsAgentToolResultEvent | BetaManagedAgentsAgentThreadMessageReceivedEvent | BetaManagedAgentsAgentThreadMessageSentEvent | BetaManagedAgentsAgentThreadContextCompactedEvent | BetaManagedAgentsSessionErrorEvent | BetaManagedAgentsSessionStatusRescheduledEvent | BetaManagedAgentsSessionStatusRunningEvent | BetaManagedAgentsSessionStatusIdleEvent | BetaManagedAgentsSessionStatusTerminatedEvent | BetaManagedAgentsSessionThreadCreatedEvent | BetaManagedAgentsSpanOutcomeEvaluationStartEvent | BetaManagedAgentsSpanOutcomeEvaluationEndEvent | BetaManagedAgentsSpanModelRequestStartEvent | BetaManagedAgentsSpanModelRequestEndEvent | BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent | BetaManagedAgentsUserDefineOutcomeEvent | BetaManagedAgentsSessionDeletedEvent | BetaManagedAgentsSessionThreadStatusRunningEvent | BetaManagedAgentsSessionThreadStatusIdleEvent | BetaManagedAgentsSessionThreadStatusTerminatedEvent | BetaManagedAgentsUserToolResultEvent | BetaManagedAgentsSessionThreadStatusRescheduledEvent | BetaManagedAgentsSessionUpdatedEvent | BetaManagedAgentsSystemMessageEvent | BetaManagedAgentsSessionUsageEvent | BetaManagedAgentsWorkflowRunCreatedEvent | BetaManagedAgentsWorkflowRunStatusEndedEvent | BetaManagedAgentsWorkflowRunPhaseStartedEvent | BetaManagedAgentsWorkflowRunPhaseEndedEvent | BetaManagedAgentsWorkflowRunStatusRunningEvent | BetaManagedAgentsWorkflowRunStatusIdleEvent | BetaManagedAgentsWorkflowRunErrorEvent;
```

## Types

```ts
type AnthropicBeta =
  | (string & {})
  | "computer-use-2024-10-22"
  | "computer-use-2025-01-24"
  | "output-128k-2025-02-19"
  | "mcp-client-2025-04-04"
  | "mcp-client-2025-11-20"
  | "dev-full-thinking-2025-05-14"
  | "interleaved-thinking-2025-05-14"
  | "code-execution-2025-05-22"
  | "context-1m-2025-08-07"
  | "context-management-2025-06-27"
  | "model-context-window-exceeded-2025-08-26"
  | "fast-mode-2026-02-01"
  | "output-300k-2026-03-24"
  | "user-profiles-2026-03-24"
  | "user-profiles-2026-08-18"
  | "user-profiles-2026-09-04"
  | "advisor-tool-2026-03-01"
  | "managed-agents-2026-04-01"
  | "dreaming-2026-04-21"
  | "thinking-token-count-2026-05-13"
  | "server-side-fallback-2026-06-01"
  | "server-side-fallback-2026-07-01"
  | "fallback-credit-2026-06-01"
  | "fallback-credit-2026-07-01"
  | "agent-memory-2026-07-22"
  | "mid-conversation-tool-changes-2026-07-01"
  | "compact-2026-01-12"
  | "computer-use-2025-11-24"
  | "mcp-tunnels-2026-06-22"
  | "structured-outputs-2025-11-13"
  | "task-budgets-2026-03-13"
  | "thinking-display-updates-2026-08-18"
  | "mid-conversation-output-config-2026-07-01"
  | "thinking-binding-controls-2026-08-01"
  | "mid-conversation-system-clear-at-2026-08-21"
  | "compact-2026-09-04"
  | "inline-tools-2026-09-15"
  | "mcp-client-2026-09-15"
  | "ce-plugins-2026-09-01"
  | "spend-limit-reads-2026-09-26"
  | "telemetry-destinations-2026-08-11"
  | "webhooks-2026-10-07"
  | "admin-user-sign-out-2026-10-08"
  | "message-threads-2026-08-12"
  | "analytics-usage-cost-2026-08-24"
  | "experimental-claude-tag-2026-10-21"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "message-batches-2024-09-24"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "prompt-caching-2024-07-31"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "pdfs-2024-09-25"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "token-counting-2024-11-01"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "token-efficient-tools-2025-02-19"
  /** @deprecated Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/files#migrate-from-files-api-2025-04-14 */
  | "files-api-2025-04-14"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "extended-cache-ttl-2025-04-11"
  /** @deprecated Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/skills-guide#migrate-from-skills-2025-10-02 */
  | "skills-2025-10-02"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "cache-diagnosis-2026-04-07"
  /** @deprecated This value is no longer needed. Remove it from your requests. */
  | "ce-user-management-2026-07-13";

/** A user message event in the session conversation. */
interface BetaManagedAgentsUserMessageEvent {
  type: "user.message";
  /** Unique identifier for this event. */
  id: string;
  /** Array of content blocks comprising the user message. */
  content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsRedactedBlock>;
  /** Timestamp when the agent finished processing this message. */
  processed_at?: string | null; // format: date-time
}

/** An interrupt event that pauses agent execution and returns control to the user. */
interface BetaManagedAgentsUserInterruptEvent {
  type: "user.interrupt";
  /** Unique identifier for this event. */
  id: string;
  /** Timestamp when the interrupt was processed. */
  processed_at?: string | null; // format: date-time
  /** If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread. */
  session_thread_id?: string | null;
}

/** A tool confirmation event that approves or denies a pending tool execution. */
interface BetaManagedAgentsUserToolConfirmationEvent {
  type: "user.tool_confirmation";
  /** Unique identifier for this event. */
  id: string;
  /** The confirmation result: 'allow' or 'deny'. */
  result: "allow" | "deny";
  /** The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list?sdk_languages=typescript#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field. */
  tool_use_id: string;
  /** Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'. */
  deny_message?: string | null; // maxLength: 10000
  /** Timestamp when the confirmation was processed. */
  processed_at?: string | null; // format: date-time
  /** Set by the server to the subagent thread this confirmation was routed to. Omitted when it was routed to the primary thread. */
  session_thread_id?: string | null;
}

/** Event sent by the client providing the result of a custom tool execution. */
interface BetaManagedAgentsUserCustomToolResultEvent {
  type: "user.custom_tool_result";
  /** Unique identifier for this event. */
  id: string;
  /** The id of the `agent.custom_tool_use` event this result corresponds to. It is also listed in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list?sdk_languages=typescript#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field. */
  custom_tool_use_id: string;
  /** The result content returned by the tool. */
  content?: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsSearchResultBlock>;
  /** Whether the tool execution resulted in an error. */
  is_error?: boolean | null;
  /** Timestamp when this result was processed. */
  processed_at?: string | null; // format: date-time
  /** Set by the server to the subagent thread this result was routed to. Omitted when it was routed to the primary thread. */
  session_thread_id?: string | null;
}

/** Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result. The client can send it as soon as this event arrives, without waiting for `session.status_idle`. */
interface BetaManagedAgentsAgentCustomToolUseEvent {
  type: "agent.custom_tool_use";
  /** Unique identifier for this event. */
  id: string;
  /** Input parameters for the tool call. */
  input: Record<string, unknown>;
  /** Name of the custom tool being called. */
  name: string;
  /** Timestamp when this tool use was processed. */
  processed_at: string; // format: date-time
  /** When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.custom_tool_result` by `custom_tool_use_id`, so clients do not send it back. */
  session_thread_id?: string | null;
}

/** An agent response event in the session conversation. */
interface BetaManagedAgentsAgentMessageEvent {
  type: "agent.message";
  /** Unique identifier for this event. */
  id: string;
  /** Array of text blocks comprising the agent response. */
  content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsRedactedBlock>;
  /** Timestamp when this response was generated. */
  processed_at: string; // format: date-time
}

/** Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier. */
interface BetaManagedAgentsAgentThinkingEvent {
  type: "agent.thinking";
  /** Unique identifier for this event. */
  id: string;
  /** Timestamp when this thinking was produced. */
  processed_at: string; // format: date-time
}

/** Event emitted when the agent invokes a tool provided by an MCP server. */
interface BetaManagedAgentsAgentMCPToolUseEvent {
  type: "agent.mcp_tool_use";
  /** Unique identifier for this event. */
  id: string;
  /** Input parameters for the tool call. */
  input: Record<string, unknown>;
  /** Name of the MCP server providing the tool. */
  mcp_server_name: string;
  /** Name of the MCP tool being used. */
  name: string;
  /** Timestamp when this event was processed. */
  processed_at: string; // format: date-time
  /** The evaluated permission policy for this tool invocation. */
  evaluated_permission?: BetaManagedAgentsAgentEvaluatedPermission;
  /** Which resolved permission_policy produced evaluated_permission: always_allow, always_ask, or auto (with the server's per-invocation judgement). Absent only when the server refused the call before any policy applied (for example, the named tool is not enabled in the session); such a refusal has evaluated_permission deny. An event recorded before this field existed reads as the arm its evaluated_permission implies (always_allow for allow, always_ask for ask). */
  evaluation?: BetaManagedAgentsAgentToolEvaluation;
  /** When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.tool_confirmation` by `tool_use_id`, so clients do not send it back. */
  session_thread_id?: string | null;
}

/** Event representing the result of an MCP tool execution. */
interface BetaManagedAgentsAgentMCPToolResultEvent {
  type: "agent.mcp_tool_result";
  /** Unique identifier for this event. */
  id: string;
  /** The id of the `agent.mcp_tool_use` event this result corresponds to. */
  mcp_tool_use_id: string;
  /** Timestamp when this event was processed. */
  processed_at: string; // format: date-time
  /** The result content returned by the tool. */
  content?: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsSearchResultBlock>;
  /** Whether the tool execution resulted in an error. */
  is_error?: boolean | null;
}

/** Event emitted when the agent invokes a built-in agent tool. */
interface BetaManagedAgentsAgentToolUseEvent {
  type: "agent.tool_use";
  /** Unique identifier for this event. */
  id: string;
  /** Input parameters for the tool call. */
  input: Record<string, unknown>;
  /** Name of the agent tool being used. */
  name: string;
  /** Timestamp when this event was processed. */
  processed_at: string; // format: date-time
  /** The evaluated permission policy for this tool invocation. */
  evaluated_permission?: BetaManagedAgentsAgentEvaluatedPermission;
  /** Which resolved permission_policy produced evaluated_permission: always_allow, always_ask, or auto (with the server's per-invocation judgement). Absent only when the server refused the call before any policy applied (for example, the named tool is not enabled in the session); such a refusal has evaluated_permission deny. An event recorded before this field existed reads as the arm its evaluated_permission implies (always_allow for allow, always_ask for ask). */
  evaluation?: BetaManagedAgentsAgentToolEvaluation;
  /** When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.tool_confirmation` or `user.tool_result` by `tool_use_id`, so clients do not send it back. */
  session_thread_id?: string | null;
}

/** Event representing the result of an agent tool execution. */
interface BetaManagedAgentsAgentToolResultEvent {
  type: "agent.tool_result";
  /** Unique identifier for this event. */
  id: string;
  /** Timestamp when this event was processed. */
  processed_at: string; // format: date-time
  /** The id of the `agent.tool_use` event this result corresponds to. */
  tool_use_id: string;
  /** The result content returned by the tool. */
  content?: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsSearchResultBlock>;
  /** Whether the tool execution resulted in an error. */
  is_error?: boolean | null;
}

/** Delivery event written to the target thread's input stream when an agent-to-agent message arrives. */
interface BetaManagedAgentsAgentThreadMessageReceivedEvent {
  type: "agent.thread_message_received";
  /** Unique identifier for this event. */
  id: string;
  /** Message content blocks. */
  content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsRedactedBlock>;
  /** Public `sthr_` ID of the thread that sent the message. */
  from_session_thread_id: string;
  /** Timestamp when the message was received. */
  processed_at: string; // format: date-time
  /** Name of the callable agent this message came from. Absent when received from the primary agent. */
  from_agent_name?: string | null;
}

/** Observability event emitted to the sender's output stream when an agent-to-agent message is sent. */
interface BetaManagedAgentsAgentThreadMessageSentEvent {
  type: "agent.thread_message_sent";
  /** Unique identifier for this event. */
  id: string;
  /** Message content blocks. */
  content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsRedactedBlock>;
  /** Timestamp when the message was sent. */
  processed_at: string; // format: date-time
  /** Public `sthr_` ID of the thread the message was sent to. */
  to_session_thread_id: string;
  /** Name of the callable agent this message was sent to. Absent when sent to the primary agent. */
  to_agent_name?: string | null;
}

/** Indicates that context compaction (summarization) occurred during the session. */
interface BetaManagedAgentsAgentThreadContextCompactedEvent {
  type: "agent.thread_context_compacted";
  /** Unique identifier for this event. */
  id: string;
  /** Timestamp when compaction was processed. */
  processed_at: string; // format: date-time
}

/** An error event indicating a problem occurred during session execution. */
interface BetaManagedAgentsSessionErrorEvent {
  type: "session.error";
  /** Unique identifier for this event. */
  id: string;
  error: BetaManagedAgentsUnknownError | BetaManagedAgentsModelOverloadedError | BetaManagedAgentsModelRateLimitedError | BetaManagedAgentsModelRequestFailedError | BetaManagedAgentsMCPConnectionFailedError | BetaManagedAgentsMCPAuthenticationFailedError | BetaManagedAgentsBillingError | BetaManagedAgentsCredentialHostUnreachableError | BetaManagedAgentsToolUseLimitReachedError | BetaManagedAgentsCompactionLimitReachedError | BetaManagedAgentsRepositoryAuthenticationError | BetaManagedAgentsRepositoryForbiddenError | BetaManagedAgentsRepositoryNotFoundError | BetaManagedAgentsRepositoryCheckoutError | BetaManagedAgentsRepositoryCloneError;
  /** Timestamp when the error occurred. */
  processed_at: string; // format: date-time
}

/** Indicates the session is recovering from an error state and is rescheduled for execution. */
interface BetaManagedAgentsSessionStatusRescheduledEvent {
  type: "session.status_rescheduled";
  /** Unique identifier for this event. */
  id: string;
  /** Timestamp of status change. */
  processed_at: string; // format: date-time
}

/** Indicates the session is actively running and the agent is working. */
interface BetaManagedAgentsSessionStatusRunningEvent {
  type: "session.status_running";
  /** Unique identifier for this event. */
  id: string;
  /** Timestamp of status change. */
  processed_at: string; // format: date-time
}

/** Indicates the agent has paused and is awaiting user input. */
interface BetaManagedAgentsSessionStatusIdleEvent {
  type: "session.status_idle";
  /** Unique identifier for this event. */
  id: string;
  /** Timestamp of status change. */
  processed_at: string; // format: date-time
  /** Structured information about why the session stopped. `null` when there is nothing more to report. */
  stop_details: BetaManagedAgentsSessionRefusalStopDetails | null;
  stop_reason: BetaManagedAgentsSessionEndTurn | BetaManagedAgentsSessionRequiresAction | BetaManagedAgentsSessionRetriesExhausted | BetaManagedAgentsSessionBudgetReached | BetaManagedAgentsSessionRefusal;
}

/** Indicates the session has terminated, either due to an error or completion. */
interface BetaManagedAgentsSessionStatusTerminatedEvent {
  type: "session.status_terminated";
  /** Unique identifier for this event. */
  id: string;
  /** Timestamp of status change. */
  processed_at: string; // format: date-time
}

/** Emitted when a child thread is created. Written to the parent thread's output stream so clients observing the session see child creation. */
interface BetaManagedAgentsSessionThreadCreatedEvent {
  type: "session.thread_created";
  /** Unique identifier for this event. */
  id: string;
  /** Name of the callable agent the thread runs. */
  agent_name: string;
  /** Timestamp when the thread was created. */
  processed_at: string; // format: date-time
  /** Public `sthr_` ID of the newly created thread. */
  session_thread_id: string;
  /** Identifier of the workflow run that created the thread, or `null` for any other thread. */
  workflow_run_id: string | null;
}

/** Emitted when an outcome evaluation cycle begins. */
interface BetaManagedAgentsSpanOutcomeEvaluationStartEvent {
  type: "span.outcome_evaluation_start";
  /** Unique identifier for this event. */
  id: string;
  /** 0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc. */
  iteration: number; // format: int32
  /** The `outc_` ID of the outcome being evaluated. */
  outcome_id: string;
  /** Timestamp when outcome evaluation started. */
  processed_at: string; // format: date-time
}

/** Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow. */
interface BetaManagedAgentsSpanOutcomeEvaluationEndEvent {
  type: "span.outcome_evaluation_end";
  /** Unique identifier for this event. */
  id: string;
  /** Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why. */
  explanation: string;
  /** 0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`. */
  iteration: number; // format: int32
  /** The id of the corresponding `span.outcome_evaluation_start` event. */
  outcome_evaluation_start_id: string;
  /** The `outc_` ID of the outcome being evaluated. */
  outcome_id: string;
  /** Timestamp when outcome evaluation ended. */
  processed_at: string; // format: date-time
  /** Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress. */
  result: string;
  /** Aggregate token usage for this evaluation cycle. Sums across all grader model requests within the cycle. */
  usage: BetaManagedAgentsSpanModelUsage;
}

/** Emitted when a model request is initiated by the agent. */
interface BetaManagedAgentsSpanModelRequestStartEvent {
  type: "span.model_request_start";
  /** Unique identifier for this event. */
  id: string;
  /** Timestamp when the model request started. */
  processed_at: string; // format: date-time
}

/** Emitted when a model request completes. */
interface BetaManagedAgentsSpanModelRequestEndEvent {
  type: "span.model_request_end";
  /** Unique identifier for this event. */
  id: string;
  /** Whether the model request resulted in an error. */
  is_error: boolean | null;
  /** The id of the corresponding `span.model_request_start` event. */
  model_request_start_id: string;
  /** Token usage for this model request. */
  model_usage: BetaManagedAgentsSpanModelUsage;
  /** Timestamp when the model request completed. */
  processed_at: string; // format: date-time
}

/** Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events. */
interface BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent {
  type: "span.outcome_evaluation_ongoing";
  /** Unique identifier for this event. */
  id: string;
  /** 0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`. */
  iteration: number; // format: int32
  /** The `outc_` ID of the outcome being evaluated. */
  outcome_id: string;
  /** Timestamp when this heartbeat was emitted. */
  processed_at: string; // format: date-time
}

/** Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference. */
interface BetaManagedAgentsUserDefineOutcomeEvent {
  type: "user.define_outcome";
  /** Unique identifier for this event. */
  id: string;
  /** What the agent should produce. Copied from the input event. */
  description: string;
  /** Evaluate-then-revise cycles before giving up. Default 3, max 20. */
  max_iterations: number | null; // format: int32
  /** Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list. */
  outcome_id: string;
  /** Timestamp when the outcome was accepted. */
  processed_at: string; // format: date-time
  /** How to grade the outcome. File rubrics are currently resolved to their text content; clients should handle both variants. */
  rubric: BetaManagedAgentsFileRubric | BetaManagedAgentsTextRubric;
}

/** Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session. */
interface BetaManagedAgentsSessionDeletedEvent {
  type: "session.deleted";
  /** Unique identifier for this event. */
  id: string;
  /** Timestamp when the session was deleted. */
  processed_at: string; // format: date-time
}

/** A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads. */
interface BetaManagedAgentsSessionThreadStatusRunningEvent {
  type: "session.thread_status_running";
  /** Unique identifier for this event. */
  id: string;
  /** Name of the agent the thread runs. */
  agent_name: string;
  /** Timestamp of the status transition. */
  processed_at: string; // format: date-time
  /** Public sthr_ ID of the thread that started running. */
  session_thread_id: string;
}

/** A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads. */
interface BetaManagedAgentsSessionThreadStatusIdleEvent {
  type: "session.thread_status_idle";
  /** Unique identifier for this event. */
  id: string;
  /** Name of the agent the thread runs. */
  agent_name: string;
  /** Timestamp of the status transition. */
  processed_at: string; // format: date-time
  /** Public sthr_ ID of the thread that went idle. */
  session_thread_id: string;
  /** Structured information about why the thread stopped. `null` when there is nothing more to report. */
  stop_details: BetaManagedAgentsSessionRefusalStopDetails | null;
  stop_reason: BetaManagedAgentsSessionEndTurn | BetaManagedAgentsSessionRequiresAction | BetaManagedAgentsSessionRetriesExhausted | BetaManagedAgentsSessionBudgetReached | BetaManagedAgentsSessionRefusal;
}

/** A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads. */
interface BetaManagedAgentsSessionThreadStatusTerminatedEvent {
  type: "session.thread_status_terminated";
  /** Unique identifier for this event. */
  id: string;
  /** Name of the agent the thread runs. */
  agent_name: string;
  /** Timestamp of the status transition. */
  processed_at: string; // format: date-time
  /** Public sthr_ ID of the thread that terminated. */
  session_thread_id: string;
}

/** Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server. */
interface BetaManagedAgentsUserToolResultEvent {
  type: "user.tool_result";
  /** Unique identifier for this event. */
  id: string;
  /** The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list?sdk_languages=typescript#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field. */
  tool_use_id: string;
  /** The result content returned by the tool. */
  content?: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsSearchResultBlock>;
  /** Whether the tool execution resulted in an error. */
  is_error?: boolean | null;
  /** Timestamp when this result was processed. */
  processed_at?: string | null; // format: date-time
  /** Set by the server to the subagent thread this result was routed to. Omitted when it was routed to the primary thread. */
  session_thread_id?: string | null;
}

/** A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads. */
interface BetaManagedAgentsSessionThreadStatusRescheduledEvent {
  type: "session.thread_status_rescheduled";
  /** Unique identifier for this event. */
  id: string;
  /** Name of the agent the thread runs. */
  agent_name: string;
  /** Timestamp of the status transition. */
  processed_at: string; // format: date-time
  /** Public sthr_ ID of the thread that is retrying. */
  session_thread_id: string;
}

/** Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn. */
interface BetaManagedAgentsSessionUpdatedEvent {
  type: "session.updated";
  /** Unique identifier for this event. */
  id: string;
  /** Timestamp when the update was applied. */
  processed_at: string; // format: date-time
  /** The session's effective agent configuration after the update. Present only when the update changed `agent` (tools or mcp_servers); when present it is the full materialised snapshot, not a diff. */
  agent?: BetaManagedAgentsSessionAgent | null;
  /** The session's budget after the update: the new budget when set or replaced, or null when the update removed it. Present only when the update changed the budget. */
  budget?: BetaManagedAgentsBudgetLimit | null;
  /** The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty. */
  metadata?: Record<string, string>;
  /** The session's new title. Present only when the update changed it. */
  title?: string | null;
}

/** A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn. */
interface BetaManagedAgentsSystemMessageEvent {
  type: "system.message";
  /** Unique identifier for this event. */
  id: string;
  /** System content blocks. Text-only. */
  content: Array<BetaManagedAgentsSystemContentBlock>;
  /** Timestamp when this system message was processed. */
  processed_at?: string | null; // format: date-time
}

/** Periodic snapshot of the session's cumulative usage and tracked list cost. */
interface BetaManagedAgentsSessionUsageEvent {
  type: "session.usage";
  /** Unique identifier for this event. */
  id: string;
  /** Timestamp when the snapshot was taken. */
  processed_at: string; // format: date-time
  /** The session's cumulative usage at the snapshot time. */
  usage: BetaManagedAgentsSessionUsageSnapshot;
  /** The session's configured budget at the snapshot time, or null when the session has no budget. */
  budget?: BetaManagedAgentsBudgetLimit | null;
}

/** A workflow run was created. A workflow run is background work that the session's agent starts. Emitted once per run, before the run's other `workflow_run.*` events. */
interface BetaManagedAgentsWorkflowRunCreatedEvent {
  type: "workflow_run.created";
  /** Unique identifier for this event. */
  id: string;
  /** Description that the agent gave the run, passed on as written, or `null` if it gave none. */
  description: string | null;
  /** Name that the agent gave the run, passed on as written, or a name that the server assigned. */
  name: string;
  /** The phases that the run's plan declares, in the plan's order. Can be empty. */
  phases: Array<BetaManagedAgentsWorkflowRunPhase>;
  /** Timestamp when this event was processed. */
  processed_at: string; // format: date-time
  /** Identifier of the run. The same value is on all of the run's `workflow_run.*` events. */
  workflow_run_id: string;
}

/** A workflow run ended. Emitted once per run, as the last of the run's `workflow_run.*` events. */
interface BetaManagedAgentsWorkflowRunStatusEndedEvent {
  type: "workflow_run.status_ended";
  /** Unique identifier for this event. */
  id: string;
  /** Timestamp when this event was processed. */
  processed_at: string; // format: date-time
  /** How the run ended. */
  result: BetaManagedAgentsWorkflowRunResult;
  /** Identifier of the run. The same value is on all of the run's `workflow_run.*` events. */
  workflow_run_id: string;
}

/** A workflow run's plan entered a phase. */
interface BetaManagedAgentsWorkflowRunPhaseStartedEvent {
  type: "workflow_run.phase_started";
  /** Unique identifier for this event. */
  id: string;
  /** Timestamp when this event was processed. */
  processed_at: string; // format: date-time
  /** Identifier of the run. The same value is on all of the run's `workflow_run.*` events. */
  workflow_run_id: string;
  /** Identifier of the phase, as in `phases` on the run's `workflow_run.created` event. */
  workflow_run_phase_id: string;
}

/** A workflow run's plan left a phase, or the run's end closed it. Emitted once for every `workflow_run.phase_started` event, before the run's `workflow_run.status_ended` event. The event does not say whether the plan finished the phase's work, or why it left. */
interface BetaManagedAgentsWorkflowRunPhaseEndedEvent {
  type: "workflow_run.phase_ended";
  /** Unique identifier for this event. */
  id: string;
  /** Identifier of the `workflow_run.phase_started` event that opened the phase. */
  phase_started_id: string;
  /** Timestamp when this event was processed. */
  processed_at: string; // format: date-time
  /** Identifier of the run. The same value is on all of the run's `workflow_run.*` events. */
  workflow_run_id: string;
  /** Identifier of the phase, as in `phases` on the run's `workflow_run.created` event. */
  workflow_run_phase_id: string;
}

/** A workflow run is running. Emitted when the run starts to execute, and each time it resumes after being idle. A run that starts idle emits `workflow_run.status_idle` first. */
interface BetaManagedAgentsWorkflowRunStatusRunningEvent {
  type: "workflow_run.status_running";
  /** Unique identifier for this event. */
  id: string;
  /** Timestamp when this event was processed. */
  processed_at: string; // format: date-time
  /** Identifier of the run. The same value is on all of the run's `workflow_run.*` events. */
  workflow_run_id: string;
}

/** A workflow run is idle. Emitted each time the run goes idle, whatever the cause. If the run ends while idle, no `workflow_run.status_running` comes between this event and its `workflow_run.status_ended`. */
interface BetaManagedAgentsWorkflowRunStatusIdleEvent {
  type: "workflow_run.status_idle";
  /** Unique identifier for this event. */
  id: string;
  /** Timestamp when this event was processed. */
  processed_at: string; // format: date-time
  /** Identifier of the run. The same value is on all of the run's `workflow_run.*` events. */
  workflow_run_id: string;
}

/** A workflow run met an error, or an error kept a run from being created. A run that ends with a `result.type` of `error` emits this event before its `workflow_run.status_ended`, with the same `error`. */
interface BetaManagedAgentsWorkflowRunErrorEvent {
  type: "workflow_run.error";
  /** Unique identifier for this event. */
  id: string;
  /** Why the run did not finish, or was not created. */
  error: BetaManagedAgentsWorkflowRunError;
  /** Timestamp when this event was processed. */
  processed_at: string; // format: date-time
  /** Identifier of the run that met the error, or `null` when the error kept a run from being created. */
  workflow_run_id: string | null;
}

/** Regular text content. */
interface BetaManagedAgentsTextBlock {
  type: "text";
  /** The text content. */
  text: string; // minLength: 1
}

/** Image content specified directly as base64 data or as a reference via a URL. */
interface BetaManagedAgentsImageBlock {
  type: "image";
  /** The source of the image data. */
  source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource;
}

/** Document content, either specified directly as base64 data, as text, or as a reference via a URL. */
interface BetaManagedAgentsDocumentBlock {
  type: "document";
  /** The source of the document data. */
  source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource;
  /** Additional context about the document for the model. */
  context?: string | null;
  /** The title of the document. */
  title?: string | null;
}

/** Placeholder for content withheld by Anthropic model policy. */
interface BetaManagedAgentsRedactedBlock {
  type: "redacted";
}

/** Base64-encoded image data. */
interface BetaManagedAgentsBase64ImageSource {
  type: "base64";
  /** Base64-encoded image data. */
  data: string; // minLength: 1
  /** MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp"). */
  media_type: string; // minLength: 1
}

/** Image referenced by URL. */
interface BetaManagedAgentsURLImageSource {
  type: "url";
  /** URL of the image to fetch. */
  url: string; // minLength: 1
}

/** Image referenced by file ID. */
interface BetaManagedAgentsFileImageSource {
  type: "file";
  /** ID of a previously uploaded file. */
  file_id: string; // minLength: 1
}

/** Base64-encoded document data. */
interface BetaManagedAgentsBase64DocumentSource {
  type: "base64";
  /** Base64-encoded document data. */
  data: string; // minLength: 1
  /** MIME type of the document (e.g., "application/pdf"). */
  media_type: string; // minLength: 1
}

/** Plain text document content. */
interface BetaManagedAgentsPlainTextDocumentSource {
  type: "text";
  /** The plain text content. */
  data: string; // minLength: 1
  /** MIME type of the text content. Must be "text/plain". */
  media_type: "text/plain";
}

/** Document referenced by URL. */
interface BetaManagedAgentsURLDocumentSource {
  type: "url";
  /** URL of the document to fetch. */
  url: string; // minLength: 1
}

/** Document referenced by file ID. */
interface BetaManagedAgentsFileDocumentSource {
  type: "file";
  /** ID of a previously uploaded file. */
  file_id: string; // minLength: 1
}

/** A block containing a web search result. */
interface BetaManagedAgentsSearchResultBlock {
  type: "search_result";
  /** Citation settings for this search result. */
  citations: BetaManagedAgentsSearchResultCitations;
  /** Array of text content blocks from the search result. */
  content: Array<BetaManagedAgentsSearchResultContent>;
  /** The URL source of the search result. */
  source: string; // minLength: 1
  /** The title of the search result. */
  title: string; // minLength: 1
}

interface BetaManagedAgentsSearchResultCitations {
  /** Whether citations are enabled for this search result. */
  enabled: boolean;
}

interface BetaManagedAgentsSearchResultContent {
  type: "text";
  /** The text content. */
  text: string; // minLength: 1
}

type BetaManagedAgentsAgentEvaluatedPermission = "allow" | "ask" | "deny";

type BetaManagedAgentsAgentToolEvaluation = BetaManagedAgentsAgentToolEvaluationAlwaysAllow | BetaManagedAgentsAgentToolEvaluationAlwaysAsk | BetaManagedAgentsAgentToolEvaluationAuto;

/** The resolved permission_policy was always_allow; accompanies evaluated_permission "allow". */
interface BetaManagedAgentsAgentToolEvaluationAlwaysAllow {
  type: "always_allow";
}

/** The resolved permission_policy was always_ask; accompanies evaluated_permission "ask". */
interface BetaManagedAgentsAgentToolEvaluationAlwaysAsk {
  type: "always_ask";
}

/** The resolved permission_policy was auto: the server judged this invocation individually. */
interface BetaManagedAgentsAgentToolEvaluationAuto {
  type: "auto";
  /** The server's judgement for this invocation. */
  evaluated_permission: BetaManagedAgentsAgentAutoEvaluatedPermission;
}

type BetaManagedAgentsAgentAutoEvaluatedPermission = BetaManagedAgentsAgentAutoEvaluatedPermissionAllow | BetaManagedAgentsAgentAutoEvaluatedPermissionAsk | BetaManagedAgentsAgentAutoEvaluatedPermissionDeny;

/** The server judged the invocation safe to execute without client approval. */
interface BetaManagedAgentsAgentAutoEvaluatedPermissionAllow {
  type: "allow";
}

/** The server reached no judgement; the invocation is held for client approval. */
interface BetaManagedAgentsAgentAutoEvaluatedPermissionAsk {
  type: "ask";
  /** The judgement's grounds in registry-bound terms, for client branching and audit rather than end-user display. Open registry; currently "indeterminate" (no judgement was reached). Clients must tolerate values outside this set. */
  reason_code: string; // maxLength: 64
}

/** The server judged the invocation high-risk, or reached no judgement and did not hold it for client approval (for example, because the organization is out of credits or has reached a spend limit); it does not execute and a synthetic error tool result is appended. */
interface BetaManagedAgentsAgentAutoEvaluatedPermissionDeny {
  type: "deny";
  /** The judgement's grounds in registry-bound terms. Open registry; currently "high_risk" (judged high-risk; the call does not run) and "indeterminate" (no judgement was reached; the call does not run). Clients must tolerate values outside this set. */
  reason_code: string; // maxLength: 64
}

/** An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone. */
interface BetaManagedAgentsUnknownError {
  type: "unknown_error";
  /** Human-readable error description. */
  message: string;
  /** What the client should do next. */
  retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal;
}

/** The model is currently overloaded. Emitted after automatic retries are exhausted. */
interface BetaManagedAgentsModelOverloadedError {
  type: "model_overloaded_error";
  /** Human-readable error description. */
  message: string;
  /** What the client should do next. */
  retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal;
}

/** The model request was rate-limited. */
interface BetaManagedAgentsModelRateLimitedError {
  type: "model_rate_limited_error";
  /** Human-readable error description. */
  message: string;
  /** What the client should do next. */
  retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal;
}

/** A model request failed for a reason other than overload or rate-limiting. */
interface BetaManagedAgentsModelRequestFailedError {
  type: "model_request_failed_error";
  /** Human-readable error description. */
  message: string;
  /** What the client should do next. */
  retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal;
}

/** Failed to connect to an MCP server. */
interface BetaManagedAgentsMCPConnectionFailedError {
  type: "mcp_connection_failed_error";
  /** Name of the MCP server that failed to connect. */
  mcp_server_name: string;
  /** Human-readable error description. */
  message: string;
  /** What the client should do next. */
  retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal;
}

/** Authentication to an MCP server failed. */
interface BetaManagedAgentsMCPAuthenticationFailedError {
  type: "mcp_authentication_failed_error";
  /** Name of the MCP server that failed authentication. */
  mcp_server_name: string;
  /** Human-readable error description. */
  message: string;
  /** What the client should do next. */
  retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal;
}

/** The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state. */
interface BetaManagedAgentsBillingError {
  type: "billing_error";
  /** Human-readable error description. */
  message: string;
  /** What the client should do next. */
  retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal;
}

/** An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit. */
interface BetaManagedAgentsCredentialHostUnreachableError {
  type: "credential_host_unreachable_error";
  /** ID of the affected credential. */
  credential_id: string;
  /** Human-readable error description. */
  message: string;
  /** What the client should do next. */
  retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal;
  /** ID of the vault containing the affected credential. */
  vault_id: string;
}

/** The turn stopped because the agent loop reached its limit on tool-use rounds (one model response that calls tools, plus running those tools, is one round), not because a request failed. The thread goes idle with `stop_reason: retries_exhausted` (a child thread then terminates); the next `user.message` starts a new turn. */
interface BetaManagedAgentsToolUseLimitReachedError {
  type: "tool_use_limit_reached_error";
  /** Human-readable error description. */
  message: string;
  /** What the client should do next. */
  retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal;
}

/** The turn stopped because the context was compacted the maximum number of times in a row without the model producing a message or a tool call, not because a request failed. The thread goes idle with `stop_reason: retries_exhausted` (a child thread then terminates); the next `user.message` starts a new turn. */
interface BetaManagedAgentsCompactionLimitReachedError {
  type: "compaction_limit_reached_error";
  /** Human-readable error description. */
  message: string;
  /** What the client should do next. */
  retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal;
}

/** The repository host rejected the credentials, or required credentials and received none. */
interface BetaManagedAgentsRepositoryAuthenticationError {
  type: "repository_authentication_error";
  /** Human-readable error description. */
  message: string;
  /** URL of the repository that could not be cloned. Null when it could not be identified. */
  repository_url: string | null;
  /** What the client should do next. Always `retrying`: the session keeps running without the repository. */
  retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal;
}

/** The repository host refused access to the repository. */
interface BetaManagedAgentsRepositoryForbiddenError {
  type: "repository_forbidden_error";
  /** Human-readable error description. */
  message: string;
  /** URL of the repository that could not be cloned. Null when it could not be identified. */
  repository_url: string | null;
  /** What the client should do next. Always `retrying`: the session keeps running without the repository. */
  retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal;
}

/** The repository host reported the repository as not found. */
interface BetaManagedAgentsRepositoryNotFoundError {
  type: "repository_not_found_error";
  /** Human-readable error description. */
  message: string;
  /** URL of the repository that could not be cloned. Null when it could not be identified. */
  repository_url: string | null;
  /** What the client should do next. Always `retrying`: the session keeps running without the repository. */
  retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal;
}

/** The requested branch or commit does not exist in the repository. */
interface BetaManagedAgentsRepositoryCheckoutError {
  type: "repository_checkout_error";
  /** Human-readable error description. */
  message: string;
  /** URL of the repository that could not be cloned. Null when it could not be identified. */
  repository_url: string | null;
  /** What the client should do next. Always `retrying`: the session keeps running without the repository. */
  retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal;
}

/** The repository could not be cloned. */
interface BetaManagedAgentsRepositoryCloneError {
  type: "repository_clone_error";
  /** Human-readable error description. */
  message: string;
  /** URL of the repository that could not be cloned. Null when it could not be identified. */
  repository_url: string | null;
  /** What the client should do next. Always `retrying`: the session keeps running without the repository. */
  retry_status: BetaManagedAgentsRetryStatusRetrying | BetaManagedAgentsRetryStatusExhausted | BetaManagedAgentsRetryStatusTerminal;
}

/** The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out. */
interface BetaManagedAgentsRetryStatusRetrying {
  type: "retrying";
}

/** This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt. */
interface BetaManagedAgentsRetryStatusExhausted {
  type: "exhausted";
}

/** The session encountered a terminal error and will transition to `terminated` state. */
interface BetaManagedAgentsRetryStatusTerminal {
  type: "terminal";
}

interface BetaManagedAgentsSessionRefusalStopDetails {
  type: "refusal";
  /** The policy category that triggered the refusal, or `null` when there is no named category. New values can be added over time. */
  category: "cyber" | "bio" | "frontier_llm" | "reasoning_extraction" | "general_harms" | null;
  /** Human-readable explanation of the refusal, or `null` when none is available. The wording can change, so do not parse it. */
  explanation: string | null;
}

/** The agent completed its turn naturally and is ready for the next user message. */
interface BetaManagedAgentsSessionEndTurn {
  type: "end_turn";
}

/** The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running. */
interface BetaManagedAgentsSessionRequiresAction {
  type: "requires_action";
  /** The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder. */
  event_ids: Array<string>;
}

/** The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`. */
interface BetaManagedAgentsSessionRetriesExhausted {
  type: "retries_exhausted";
}

/** The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget. */
interface BetaManagedAgentsSessionBudgetReached {
  type: "budget_reached";
}

/** The turn ended because the model's response was refused, for example by a safety classifier. */
interface BetaManagedAgentsSessionRefusal {
  type: "refusal";
}

interface BetaManagedAgentsSpanModelUsage {
  /** Tokens used to create prompt cache in this request. */
  cache_creation_input_tokens: number; // format: int32
  /** Tokens read from prompt cache in this request. */
  cache_read_input_tokens: number; // format: int32
  /** Input tokens consumed by this request. */
  input_tokens: number; // format: int32
  /** Output tokens generated by this request. */
  output_tokens: number; // format: int32
  /** Inference speed tier this request actually ran at. Mirrors `usage.speed` on /v1/messages. Only present when the fast-mode beta is active. */
  speed?: "standard" | "fast" | null;
}

/** Rubric referenced by a file uploaded via the Files API. */
interface BetaManagedAgentsFileRubric {
  type: "file";
  /** ID of the rubric file. */
  file_id: string;
}

/** Rubric content provided inline as text. */
interface BetaManagedAgentsTextRubric {
  type: "text";
  /** Rubric content. Plain text or markdown — the grader treats it as freeform text. */
  content: string;
}

interface BetaManagedAgentsSystemContentBlock {
  type: "text";
  /** The text content. */
  text: string; // minLength: 1
}

interface BetaManagedAgentsSessionUsageSnapshot {
  /** Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on. */
  active_seconds?: number; // format: double
  /** Tokens used to create prompt cache entries, broken down by cache TTL. */
  cache_creation?: BetaManagedAgentsCacheCreationUsage;
  /** Total tokens read from prompt cache. */
  cache_read_input_tokens?: number; // format: int32
  /** Total input tokens consumed across all turns. */
  input_tokens?: number; // format: int32
  /** Cumulative list cost of the session across all turns, priced at public list rates. */
  list_cost?: BetaMonetaryAmount;
  /** Total output tokens generated across all turns. */
  output_tokens?: number; // format: int32
  /** Cumulative server-executed tool usage across all turns. */
  server_tool_use?: BetaManagedAgentsServerToolUsage;
}

interface BetaManagedAgentsCacheCreationUsage {
  /** Tokens used to create 1-hour ephemeral cache entries. */
  ephemeral_1h_input_tokens?: number; // format: int32
  /** Tokens used to create 5-minute ephemeral cache entries. */
  ephemeral_5m_input_tokens?: number; // format: int32
}

interface BetaManagedAgentsServerToolUsage {
  /** Number of server-executed web fetch requests. */
  web_fetch_requests?: number; // format: int32
  /** Number of server-executed web search requests. */
  web_search_requests?: number; // format: int32
}

interface BetaManagedAgentsWorkflowRunPhase {
  /** Unique identifier for the phase. */
  id: string;
  /** Description that the agent gave the phase, passed on as written, or `null` if it gave none. */
  description: string | null;
  /** Name that the agent gave the phase, passed on as written. */
  name: string;
}

type BetaManagedAgentsWorkflowRunResult = BetaManagedAgentsWorkflowRunResultCompleted | BetaManagedAgentsWorkflowRunResultError | BetaManagedAgentsWorkflowRunResultStopped;

/** The run's plan, a program that the agent wrote, finished. This does not say whether the work succeeded. */
interface BetaManagedAgentsWorkflowRunResultCompleted {
  type: "completed";
}

/** The run failed or reached its time limit. */
interface BetaManagedAgentsWorkflowRunResultError {
  type: "error";
  /** Why the run did not finish. */
  error: BetaManagedAgentsWorkflowRunError;
}

/** The agent stopped the run. */
interface BetaManagedAgentsWorkflowRunResultStopped {
  type: "stopped";
}

type BetaManagedAgentsWorkflowRunError = BetaManagedAgentsTimeoutWorkflowRunError | BetaManagedAgentsProgramWorkflowRunError | BetaManagedAgentsUnknownWorkflowRunError | BetaManagedAgentsThreadLimitWorkflowRunError | BetaManagedAgentsMaxWorkflowRunsWorkflowRunError;

/** The run reached its time limit. */
interface BetaManagedAgentsTimeoutWorkflowRunError {
  type: "timeout_error";
  /** Short explanation written by the server. It never contains content from the run or its agents. */
  message: string;
}

/** The plan, a program that the agent wrote, failed, or the server refused it. */
interface BetaManagedAgentsProgramWorkflowRunError {
  type: "program_error";
  /** Short explanation written by the server. It never contains content from the run or its agents. */
  message: string;
}

/** A failure that has no type of its own. */
interface BetaManagedAgentsUnknownWorkflowRunError {
  type: "unknown_error";
  /** Short explanation written by the server. It never contains content from the run or its agents. */
  message: string;
}

/** The run exceeded the limit on the number of threads that a run can create. */
interface BetaManagedAgentsThreadLimitWorkflowRunError {
  type: "thread_limit_error";
  /** Short explanation written by the server. It never contains content from the run or its agents. */
  message: string;
}

/** No run was created, because the session was at its limit of open workflow runs, which are runs that have not ended. Only `workflow_run.error` carries this type. */
interface BetaManagedAgentsMaxWorkflowRunsWorkflowRunError {
  type: "max_workflow_runs_error";
  /** Short explanation written by the server. It never contains content from the run or its agents. */
  message: string;
}

interface BetaManagedAgentsSessionAgent {
  type: "agent";
  id: string;
  description: string | null;
  /** Execution principal snapshotted from the agent at session creation. Always present; `{"type": "service_account"}` when runs carry no customer-named principal. */
  execution_identity: BetaManagedAgentsExecutionIdentity;
  mcp_servers: Array<BetaManagedAgentsMCPServerURLDefinition>;
  /** Model identifier and configuration. */
  model: BetaManagedAgentsModelConfig;
  /** Resolved multiagent orchestration configuration. Null when the agent is single-threaded. */
  multiagent: BetaManagedAgentsSessionMultiagent | null;
  name: string;
  skills: Array<BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill>;
  system: string | null;
  tools: Array<BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool>;
  version: number; // format: int32
}

interface BetaManagedAgentsBudgetLimit {
  type: "limit";
  /** Maximum list cost the session may accrue. List price is used regardless of any negotiated discount, so the cap fires at or before the actual charge. */
  max_list_cost: BetaMonetaryAmount;
}

interface BetaMonetaryAmount {
  /** Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied. */
  amount: string; // pattern: ^(0|[1-9]\d*)$
  /** Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced. */
  currency: BetaCurrency;
}

type BetaCurrency = "USD";

type BetaManagedAgentsExecutionIdentity = BetaManagedAgentsAWSRoleExecutionIdentity | BetaManagedAgentsServiceAccountExecutionIdentity;

/** URL-based MCP server connection as returned in API responses. */
interface BetaManagedAgentsMCPServerURLDefinition {
  type: "url";
  name: string;
  url: string;
}

interface BetaManagedAgentsModelConfig {
  /** The model that will power your agent. See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options. */
  id: BetaManagedAgentsModel;
  /** How hard Claude works on each inference call. One of `low`, `medium`, `high`, `xhigh`, `max`. Always present; resolved to the per-model default at save time when not supplied. */
  effort?: BetaManagedAgentsEffortLow | BetaManagedAgentsEffortMedium | BetaManagedAgentsEffortHigh | BetaManagedAgentsEffortXhigh | BetaManagedAgentsEffortMax;
  /** Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo. */
  inference_geo?: string;
  /** Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Defaults to `standard`. Not all models support `fast`; invalid combinations are rejected at create time. */
  speed?: "standard" | "fast";
}

type BetaManagedAgentsSessionMultiagent = BetaManagedAgentsSessionMultiagentCoordinator | BetaManagedAgentsSessionMultiagent20261001;

/** A resolved Anthropic-managed skill. */
interface BetaManagedAgentsAnthropicSkill {
  type: "anthropic";
  skill_id: string;
  version: string;
}

/** A resolved user-created custom skill. */
interface BetaManagedAgentsCustomSkill {
  type: "custom";
  skill_id: string;
  version: string;
}

interface BetaManagedAgentsAgentToolset20260401 {
  type: "agent_toolset_20260401";
  configs: Array<BetaManagedAgentsAgentToolConfig>;
  /** Resolved default configuration for agent tools. */
  default_config: BetaManagedAgentsAgentToolsetDefaultConfig;
}

interface BetaManagedAgentsMCPToolset {
  type: "mcp_toolset";
  configs: Array<BetaManagedAgentsMCPToolConfig>;
  /** Resolved default configuration for all tools from an MCP server. */
  default_config: BetaManagedAgentsMCPToolsetDefaultConfig;
  mcp_server_name: string;
}

/** A custom tool as returned in API responses. */
interface BetaManagedAgentsCustomTool {
  type: "custom";
  description: string;
  /** JSON Schema for custom tool input parameters. */
  input_schema: BetaManagedAgentsCustomToolInputSchema;
  name: string;
}

/** An AWS IAM role principal as returned in API responses. */
interface BetaManagedAgentsAWSRoleExecutionIdentity {
  type: "aws_role";
  /** The IAM role's ARN. */
  role_arn: string;
}

/** The Anthropic-managed service account as returned in API responses. */
interface BetaManagedAgentsServiceAccountExecutionIdentity {
  type: "service_account";
}

type BetaManagedAgentsModel =
  /** Built for the most ambitious work in coding, enterprise workflows, and the sciences */
  | "claude-fable-5-2"
  /** Fastest model for high-volume, real-time tasks */
  | "claude-haiku-5-5"
  /** Efficient model for coding and agents */
  | "claude-sonnet-5-5"
  /** Powerful intelligence for coding, knowledge work, and long-running agents */
  | "claude-opus-5-5"
  /** Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows */
  | "claude-fable-5-1"
  /** Efficient model for coding and agents */
  | "claude-sonnet-5"
  /** Next generation of intelligence for the hardest knowledge work and coding problems */
  | "claude-fable-5"
  /** Powerful intelligence for long-running agents and coding */
  | "claude-opus-5"
  /** Powerful intelligence for long-running agents and coding */
  | "claude-opus-4-8"
  /** Powerful intelligence for long-running agents and coding */
  | "claude-opus-4-7"
  /** Powerful intelligence for long-running agents and coding */
  | "claude-opus-4-6"
  /** Best combination of speed and intelligence */
  | "claude-sonnet-4-6"
  | "claude-haiku-4-5"
  | "claude-haiku-4-5-20251001"
  /** Powerful intelligence for long-running agents and coding */
  | "claude-opus-4-5"
  /** Powerful intelligence for long-running agents and coding */
  | "claude-opus-4-5-20251101"
  /**
   * High-performance model for agents and coding
   * @deprecated Will reach end-of-life on November 30, 2026. Please migrate to claude-sonnet-5-5. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.
   */
  | "claude-sonnet-4-5"
  /**
   * High-performance model for agents and coding
   * @deprecated Will reach end-of-life on November 30, 2026. Please migrate to claude-sonnet-5-5. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.
   */
  | "claude-sonnet-4-5-20250929"
  | (string & {});

/** Low effort. Favors latency over reasoning depth. */
interface BetaManagedAgentsEffortLow {
  type: "low";
}

/** Medium effort. Balances latency and reasoning depth. */
interface BetaManagedAgentsEffortMedium {
  type: "medium";
}

/** High effort. Favors reasoning depth. */
interface BetaManagedAgentsEffortHigh {
  type: "high";
}

/** Extra-high effort. Not all models accept this level. */
interface BetaManagedAgentsEffortXhigh {
  type: "xhigh";
}

/** Maximum effort. Favors reasoning depth over latency. */
interface BetaManagedAgentsEffortMax {
  type: "max";
}

/** Resolved coordinator topology with full agent definitions for each roster member. */
interface BetaManagedAgentsSessionMultiagentCoordinator {
  type: "coordinator";
  /** Full `agent` definitions the coordinator may spawn as session threads. */
  agents: Array<BetaManagedAgentsSessionThreadAgent | BetaManagedAgentsAdvisor>;
}

/** Resolved multiagent configuration with three members, as copied to the `session` at creation. */
interface BetaManagedAgentsSessionMultiagent20261001 {
  type: "multiagent_20261001";
  /** Whether the session's primary thread can consult an advisor model. */
  advisor: BetaManagedAgentsMultiagentAdvisor;
  /** Whether the agent can spawn session threads. */
  subagents: BetaManagedAgentsSessionMultiagentSubagents;
  /** Whether the agent can start workflow runs. */
  workflows: BetaManagedAgentsSessionMultiagentWorkflows;
}

/** Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`. */
interface BetaManagedAgentsSessionThreadAgent {
  type: "agent";
  id: string;
  description: string | null;
  /** Execution principal snapshotted from the agent at session creation. Always present; `{"type": "service_account"}` when runs carry no customer-named principal. */
  execution_identity: BetaManagedAgentsExecutionIdentity;
  mcp_servers: Array<BetaManagedAgentsMCPServerURLDefinition>;
  /** Model identifier and configuration. */
  model: BetaManagedAgentsModelConfig;
  name: string;
  skills: Array<BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill>;
  system: string | null;
  tools: Array<BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool>;
  version: number; // format: int32
}

/** Platform advisor roster entry: a model the session's primary thread may consult mid-turn. */
interface BetaManagedAgentsAdvisor {
  type: "advisor";
  /** The advisor model id. */
  model: string;
}

type BetaManagedAgentsMultiagentAdvisor = BetaManagedAgentsMultiagentAdvisorEnabled | BetaManagedAgentsMultiagentAdvisorDisabled;

type BetaManagedAgentsSessionMultiagentSubagents = BetaManagedAgentsSessionMultiagentSubagentsEnabled | BetaManagedAgentsMultiagentSubagentsDisabled;

type BetaManagedAgentsSessionMultiagentWorkflows = BetaManagedAgentsSessionMultiagentWorkflowsEnabled | BetaManagedAgentsMultiagentWorkflowsDisabled;

/** The session's primary thread can consult `model` mid-turn. */
interface BetaManagedAgentsMultiagentAdvisorEnabled {
  type: "enabled";
  /** The advisor model id. */
  model: string;
}

/** The agent has no advisor. */
interface BetaManagedAgentsMultiagentAdvisorDisabled {
  type: "disabled";
}

/** The agent can start workflow runs. */
interface BetaManagedAgentsSessionMultiagentWorkflowsEnabled {
  type: "enabled";
  /** Whether a run's plan can define inline agents, which are not saved. */
  inline_agents: BetaManagedAgentsMultiagentInlineAgents;
  /** Full `agent` definitions of the predefined agents, which are saved agents that a run's plan can use. */
  predefined_agents: Array<BetaManagedAgentsSessionThreadAgent>;
}

/** The agent cannot start workflow runs. */
interface BetaManagedAgentsMultiagentWorkflowsDisabled {
  type: "disabled";
}

/** The agent can spawn session threads. */
interface BetaManagedAgentsSessionMultiagentSubagentsEnabled {
  type: "enabled";
  /** Whether the agent can define inline agents, which are not saved, when it spawns session threads. */
  inline_agents: BetaManagedAgentsMultiagentInlineAgents;
  /** Full `agent` definitions of the predefined agents, which are saved agents that this agent can spawn as session threads. */
  predefined_agents: Array<BetaManagedAgentsSessionThreadAgent>;
}

/** The agent cannot spawn session threads. */
interface BetaManagedAgentsMultiagentSubagentsDisabled {
  type: "disabled";
}

type BetaManagedAgentsMultiagentInlineAgents = BetaManagedAgentsMultiagentInlineAgentsEnabled | BetaManagedAgentsMultiagentInlineAgentsDisabled;

/** The agent can define inline agents. */
interface BetaManagedAgentsMultiagentInlineAgentsEnabled {
  type: "enabled";
}

/** The agent cannot define inline agents. */
interface BetaManagedAgentsMultiagentInlineAgentsDisabled {
  type: "disabled";
}

/** Resolved configuration for a specific MCP tool. */
interface BetaManagedAgentsMCPToolConfig {
  enabled: boolean;
  name: string;
  /** Permission policy for tool execution. */
  permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy;
}

interface BetaManagedAgentsMCPToolsetDefaultConfig {
  enabled: boolean;
  /** Permission policy for tool execution. */
  permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy;
}

interface BetaManagedAgentsCustomToolInputSchema {
  type: "object";
  properties?: Record<string, unknown> | null;
  required?: Array<string> | null;
}

/** Configuration for a specific agent tool. */
type BetaManagedAgentsAgentToolConfig = BetaManagedAgentsBashToolConfig | BetaManagedAgentsEditToolConfig | BetaManagedAgentsReadToolConfig | BetaManagedAgentsWriteToolConfig | BetaManagedAgentsGlobToolConfig | BetaManagedAgentsGrepToolConfig | BetaManagedAgentsWebFetchToolConfig | BetaManagedAgentsWebSearchToolConfig;

interface BetaManagedAgentsAgentToolsetDefaultConfig {
  enabled: boolean;
  /** Permission policy for tool execution. */
  permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy;
}

/** Configuration for the bash tool. */
interface BetaManagedAgentsBashToolConfig {
  type: "bash";
  enabled: boolean;
  name: "bash";
  /** Permission policy for tool execution. */
  permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy;
}

/** Configuration for the edit tool. */
interface BetaManagedAgentsEditToolConfig {
  type: "edit";
  enabled: boolean;
  name: "edit";
  /** Permission policy for tool execution. */
  permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy;
}

/** Configuration for the read tool. */
interface BetaManagedAgentsReadToolConfig {
  type: "read";
  enabled: boolean;
  name: "read";
  /** Permission policy for tool execution. */
  permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy;
}

/** Configuration for the write tool. */
interface BetaManagedAgentsWriteToolConfig {
  type: "write";
  enabled: boolean;
  name: "write";
  /** Permission policy for tool execution. */
  permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy;
}

/** Configuration for the glob tool. */
interface BetaManagedAgentsGlobToolConfig {
  type: "glob";
  enabled: boolean;
  name: "glob";
  /** Permission policy for tool execution. */
  permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy;
}

/** Configuration for the grep tool. */
interface BetaManagedAgentsGrepToolConfig {
  type: "grep";
  enabled: boolean;
  name: "grep";
  /** Permission policy for tool execution. */
  permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy;
}

/** Configuration for the web_fetch tool. */
interface BetaManagedAgentsWebFetchToolConfig {
  type: "web_fetch";
  enabled: boolean;
  name: "web_fetch";
  /** Permission policy for tool execution. */
  permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy;
  /** Which sources contribute URLs the tool may fetch, always in the object form. Null when not set, which allows every source. */
  url_sources: BetaManagedAgentsWebFetchURLSources | null;
  allowed_domains?: Array<string>;
  blocked_domains?: Array<string>;
  max_content_tokens?: number | null; // format: int32
}

/** Configuration for the web_search tool. */
interface BetaManagedAgentsWebSearchToolConfig {
  type: "web_search";
  enabled: boolean;
  name: "web_search";
  /** Permission policy for tool execution. */
  permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy;
  allowed_domains?: Array<string>;
  blocked_domains?: Array<string>;
  /** Approximate user location for search result localization. */
  user_location?: BetaManagedAgentsUserLocation | null;
}

/** Tool calls are automatically approved without user confirmation. */
interface BetaManagedAgentsAlwaysAllowPolicy {
  type: "always_allow";
}

/** Tool calls require user confirmation before execution. */
interface BetaManagedAgentsAlwaysAskPolicy {
  type: "always_ask";
}

/** The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit. */
interface BetaManagedAgentsAutoPolicy {
  type: "auto";
}

interface BetaManagedAgentsUserLocation {
  /** Location precision. Only "approximate" is supported. */
  type: "approximate";
  /** City name. */
  city?: string | null; // minLength: 1, maxLength: 255
  /** Two-letter ISO 3166-1 country code, uppercase. */
  country?: string | null; // pattern: ^[A-Z]{2}$
  /** Region or state name. */
  region?: string | null; // minLength: 1, maxLength: 255
  /** IANA timezone identifier, e.g. "America/Los_Angeles". */
  timezone?: string | null; // minLength: 1, maxLength: 255
}

interface BetaManagedAgentsWebFetchURLSources {
  /** Which custom tools' results contribute URLs that may be fetched. Null when not set, which allows every custom tool's results. */
  client_tool_results: BetaManagedAgentsWebFetchURLSourceToolFilter | null;
  /** Which of the web_search and web_fetch tools' results contribute URLs that may be fetched. Null when not set, which allows both. */
  server_tool_results: BetaManagedAgentsWebFetchURLSourceToolFilter | null;
  /** Whether URLs in the text of user messages may be fetched. Null when not set, which allows them. */
  user_input: BetaManagedAgentsWebFetchURLSourceUserInput | null;
}

type BetaManagedAgentsWebFetchURLSourceToolFilter = BetaManagedAgentsWebFetchURLSourceAll | BetaManagedAgentsWebFetchURLSourceNone | BetaManagedAgentsWebFetchURLSourceOnly | BetaManagedAgentsWebFetchURLSourceExcept;

type BetaManagedAgentsWebFetchURLSourceUserInput = BetaManagedAgentsWebFetchURLSourceAll | BetaManagedAgentsWebFetchURLSourceNone;

/** Every URL from this source may be fetched. This is the default. */
interface BetaManagedAgentsWebFetchURLSourceAll {
  type: "all";
}

/** This source contributes no URLs that may be fetched. */
interface BetaManagedAgentsWebFetchURLSourceNone {
  type: "none";
}

/** Only the named tools' results contribute URLs that may be fetched. */
interface BetaManagedAgentsWebFetchURLSourceOnly {
  type: "only";
  /** The tools whose results contribute. Between 1 and 128 entries, each with a different name. An empty list is rejected; use "none" to allow no tool's results. */
  tools: Array<BetaManagedAgentsWebFetchURLSourceToolReference>;
}

/** Every tool's results contribute URLs that may be fetched, except the named tools' results. */
interface BetaManagedAgentsWebFetchURLSourceExcept {
  type: "except";
  /** The tools whose results do not contribute. Between 1 and 128 entries, each with a different name. An empty list is rejected; use "all" to leave out no tool's results. */
  tools: Array<BetaManagedAgentsWebFetchURLSourceToolReference>;
}

interface BetaManagedAgentsWebFetchURLSourceToolReference {
  /** Must be "tool_reference". */
  type: "tool_reference";
  /** Name of the tool. Compared exactly, so upper and lower case letters are different. */
  name: string; // minLength: 1, maxLength: 128
}
```
