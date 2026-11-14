---
title: Send Events
url: https://platform.claude.com/docs/en/api/typescript/beta/sessions/events/send
---

# Send Events

- Signature: `client.beta.sessions.events.send(sessionID: string, params: EventSendParams, options?: RequestOptions): BetaManagedAgentsSendSessionEvents`
- Endpoint: `POST /v1/sessions/{session_id}/events`
- Beta header: `anthropic-beta: managed-agents-2026-04-01`

## Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsSendSessionEvents = await client.beta.sessions.events.send(
  "sesn_011CZkZAtmR3yMPDzynEDxu7",
  {
    events: [
      { content: [{ text: "Where is my order #1234?", type: "text" }], type: "user.message" }
    ]
  }
);

console.log(betaManagedAgentsSendSessionEvents.data);
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
    }
  ]
}
```

## Parameters

```ts
sessionID: string; // path parameter

interface EventSendParams {
  /** Events to send to the `session`. */
  events: Array<BetaManagedAgentsEventParams>;
  /** This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

## Returns

```ts
/** Events that were successfully sent to the session. */
interface BetaManagedAgentsSendSessionEvents {
  /** Sent events */
  data?: Array<BetaManagedAgentsUserMessageEvent | BetaManagedAgentsUserInterruptEvent | BetaManagedAgentsUserToolConfirmationEvent | BetaManagedAgentsUserCustomToolResultEvent | BetaManagedAgentsUserDefineOutcomeEvent | BetaManagedAgentsUserToolResultEvent | BetaManagedAgentsSystemMessageEvent>;
}
```

## Types

```ts
type BetaManagedAgentsEventParams = BetaManagedAgentsUserMessageEventParams | BetaManagedAgentsUserInterruptEventParams | BetaManagedAgentsUserToolConfirmationEventParams | BetaManagedAgentsUserCustomToolResultEventParams | BetaManagedAgentsUserDefineOutcomeEventParams | BetaManagedAgentsUserToolResultEventParams | BetaManagedAgentsSystemMessageEventParams;

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

/** Parameters for sending a user message to the session. */
interface BetaManagedAgentsUserMessageEventParams {
  type: "user.message";
  /** Array of content blocks for the user message. */
  content: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsRedactedBlock>;
}

/** Parameters for sending an interrupt to pause the agent. */
interface BetaManagedAgentsUserInterruptEventParams {
  type: "user.interrupt";
  /** If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread. */
  session_thread_id?: string | null;
}

/** Parameters for confirming or denying a tool execution request. */
interface BetaManagedAgentsUserToolConfirmationEventParams {
  type: "user.tool_confirmation";
  /** The confirmation result: 'allow' or 'deny'. */
  result: "allow" | "deny";
  /** The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list?sdk_languages=typescript#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field. */
  tool_use_id: string; // minLength: 1, maxLength: 128
  /** Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'. */
  deny_message?: string | null; // maxLength: 10000
}

/** Parameters for providing the result of a custom tool execution. */
interface BetaManagedAgentsUserCustomToolResultEventParams {
  type: "user.custom_tool_result";
  /** The id of the `agent.custom_tool_use` event this result corresponds to. It is also listed in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list?sdk_languages=typescript#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field. */
  custom_tool_use_id: string; // minLength: 1, maxLength: 128
  /** The result content returned by the tool. */
  content?: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsSearchResultBlock>;
  /** Whether the tool execution resulted in an error. */
  is_error?: boolean | null;
}

/** Parameters for defining an outcome the agent should work toward. The agent begins work on receipt. */
interface BetaManagedAgentsUserDefineOutcomeEventParams {
  type: "user.define_outcome";
  /** What the agent should produce. This is the task specification. */
  description: string;
  /** How to grade the outcome. Text or file reference. */
  rubric: BetaManagedAgentsFileRubricParams | BetaManagedAgentsTextRubricParams;
  /** Eval→revision cycles before giving up. Default 3, max 20. */
  max_iterations?: number | null; // format: int32
}

/** Parameters for providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server. */
interface BetaManagedAgentsUserToolResultEventParams {
  type: "user.tool_result";
  /** The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list?sdk_languages=typescript#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field. */
  tool_use_id: string; // minLength: 1, maxLength: 128
  /** The result content returned by the tool. */
  content?: Array<BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsSearchResultBlock>;
  /** Whether the tool execution resulted in an error. */
  is_error?: boolean | null;
}

/** Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages. */
interface BetaManagedAgentsSystemMessageEventParams {
  type: "system.message";
  /** System content blocks to append. Text-only. */
  content: Array<BetaManagedAgentsSystemContentBlock>;
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

/** Rubric referenced by a file uploaded via the Files API. */
interface BetaManagedAgentsFileRubricParams {
  type: "file";
  /** ID of the rubric file. */
  file_id: string;
}

/** Rubric content provided inline as text. */
interface BetaManagedAgentsTextRubricParams {
  type: "text";
  /** Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters. */
  content: string; // maxLength: 262144
}

interface BetaManagedAgentsSystemContentBlock {
  type: "text";
  /** The text content. */
  text: string; // minLength: 1
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
```
