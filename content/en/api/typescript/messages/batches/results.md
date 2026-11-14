---
title: Retrieve Message Batch results
url: https://platform.claude.com/docs/en/api/typescript/messages/batches/results
---

# Retrieve Message Batch results

- Signature: `client.messages.batches.results(messageBatchID: string, params?: BatchResultsParams, options?: RequestOptions): JSONLDecoder<MessageBatchIndividualResponse>`
- Endpoint: `GET /v1/messages/batches/{message_batch_id}/results`

Streams the results of a Message Batch as a `.jsonl` file.

Each line in the file is a JSON object containing the result of a single request in the Message Batch. Results are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing?sdk_languages=typescript)

## Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const stream = await client.messages.batches.results("message_batch_id");
for await (const messageBatchIndividualResponse of stream) {
  console.log(messageBatchIndividualResponse.custom_id);
}
```

## Parameters

```ts
/** ID of the Message Batch. */
messageBatchID: string; // path parameter

interface BatchResultsParams {
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

## Returns

```ts
/** This is a single line in the response `.jsonl` file and does not represent the response as a whole. */
interface MessageBatchIndividualResponse {
  /** Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order. Must be unique for each request within the Message Batch. */
  custom_id: string;
  /** Processing result for this request. Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration. */
  result: MessageBatchResult;
}
```

## Errors

Any method can also return the general [HTTP errors](https://platform.claude.com/docs/en/api/errors?sdk_languages=typescript).

- `ClaudeCodeKeyCreatorNotMemberError` (HTTP status 400, error code `claude_code_key_creator_not_member`)

  The API key belongs to the Claude Code workspace, and the user who created it is no longer a member of the organization or of that workspace.

- `CMEKKeyDisabledError` (HTTP status 400, error code `cmek_key_disabled`)

  The workspace's customer-managed encryption key is disabled or revoked. Re-enable the key, then retry.

- `OrganizationOnHoldError` (HTTP status 400, error code `organization_on_hold`)

  Anthropic has disabled the organization for trust and safety reasons. An organization disabled for any other reason, such as billing, does not get this code. `appeal_url`, when present, is where the organization can appeal.

## Types

````ts
type MessageBatchResult = MessageBatchSucceededResult | MessageBatchErroredResult | MessageBatchCanceledResult | MessageBatchExpiredResult;

interface MessageBatchSucceededResult {
  type: "succeeded";
  message: Message;
}

interface MessageBatchErroredResult {
  type: "errored";
  error: ErrorResponse;
}

interface MessageBatchCanceledResult {
  type: "canceled";
}

interface MessageBatchExpiredResult {
  type: "expired";
}

interface ErrorResponse {
  type: "error";
  error: ErrorObject;
  request_id: string | null;
}

type ErrorObject = InvalidRequestError | AuthenticationError | BillingError | PermissionError | NotFoundError | RateLimitError | GatewayTimeoutError | APIErrorObject | OverloadedError;

interface InvalidRequestError {
  /** The broad category of the error. */
  type: "invalid_request_error";
  /** A human-readable explanation of the error. Its wording can change, so don't match on it. */
  message: string; // default: Invalid request
}

interface AuthenticationError {
  /** The broad category of the error. */
  type: "authentication_error";
  /** A human-readable explanation of the error. Its wording can change, so don't match on it. */
  message: string; // default: Authentication error
}

interface BillingError {
  /** The broad category of the error. */
  type: "billing_error";
  /** A human-readable explanation of the error. Its wording can change, so don't match on it. */
  message: string; // default: Billing error
}

interface PermissionError {
  /** The broad category of the error. */
  type: "permission_error";
  /** A human-readable explanation of the error. Its wording can change, so don't match on it. */
  message: string; // default: Permission denied
}

interface NotFoundError {
  /** The broad category of the error. */
  type: "not_found_error";
  /** A human-readable explanation of the error. Its wording can change, so don't match on it. */
  message: string; // default: Not found
}

interface RateLimitError {
  /** The broad category of the error. */
  type: "rate_limit_error";
  /** A human-readable explanation of the error. Its wording can change, so don't match on it. */
  message: string; // default: Rate limited
}

interface GatewayTimeoutError {
  /** The broad category of the error. */
  type: "timeout_error";
  /** A human-readable explanation of the error. Its wording can change, so don't match on it. */
  message: string; // default: Request timeout
}

interface APIErrorObject {
  /** The broad category of the error. */
  type: "api_error";
  /** A human-readable explanation of the error. Its wording can change, so don't match on it. */
  message: string; // default: Internal server error
}

interface OverloadedError {
  /** The broad category of the error. */
  type: "overloaded_error";
  /** A human-readable explanation of the error. Its wording can change, so don't match on it. */
  message: string; // default: Overloaded
}

interface Message {
  /** Object type. For Messages, this is always `"message"`. */
  type: "message";
  /** Unique object identifier. The format and length of IDs may change over time. */
  id: string;
  /** Information about the container used in this request. This will be non-null if a container tool (e.g. code execution) was used. */
  container: Container | null;
  /**
   * Content generated by the model.
   *
   * This is an array of content blocks, each of which has a `type` that determines its shape.
   *
   * Example:
   *
   * ```json
   * [{"type": "text", "text": "Hi, I'm Claude."}]
   * ```
   *
   * If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.
   *
   * For example, if the input `messages` were:
   *
   * ```json
   * [
   *   {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
   *   {"role": "assistant", "content": "The best answer is ("}
   * ]
   * ```
   *
   * Then the response `content` might be:
   *
   * ```json
   * [{"type": "text", "text": "B)"}]
   * ```
   */
  content: Array<ContentBlock>;
  /** Request-level diagnostics. `null` when the request did not supply `diagnostics`, or when it did and no prompt-cache divergence was detected. */
  diagnostics: Diagnostics | null;
  /** The model that will complete your prompt. See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options. */
  model: Model;
  /** Conversational role of the generated message. This will always be `"assistant"`. */
  role: "assistant";
  /** Structured information about why model output stopped. This is `null` when the `stop_reason` has no additional detail to report. */
  stop_details: RefusalStopDetails | null;
  /**
   * The reason that we stopped.
   *
   * This may be one the following values:
   *
   * * `"end_turn"`: the model reached a natural stopping point
   * * `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
   * * `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
   * * `"tool_use"`: the model invoked one or more tools
   * * `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
   * * `"refusal"`: when streaming classifiers intervene to handle potential policy violations
   * * `"model_context_window_exceeded"`: we exceeded the model's context window
   *
   * In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.
   */
  stop_reason: StopReason | null;
  /** Which custom stop sequence was generated, if any. This value will be a non-null string if one of your custom stop sequences was generated. */
  stop_sequence: string | null;
  /** Billing and rate-limit usage. Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems. Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response. For example, `output_tokens` will be non-zero, even for an empty string response from Claude. Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`. */
  usage: Usage;
}

interface Container {
  /** Identifier for the container used in this request */
  id: string;
  /** The time at which the container will expire. */
  expires_at: string; // format: date-time
  /** Skills loaded in the container */
  skills: Array<ContainerSkill> | null;
}

type ContentBlock = TextBlock | ThinkingBlock | RedactedThinkingBlock | ToolUseBlock | ServerToolUseBlock | WebSearchToolResultBlock | WebFetchToolResultBlock | CodeExecutionToolResultBlock | BashCodeExecutionToolResultBlock | TextEditorCodeExecutionToolResultBlock | ToolSearchToolResultBlock | ContainerUploadBlock;

interface Diagnostics {
  /** Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed. */
  cache_miss_reason: CacheMissReason | null;
}

type Model =
  /** Built for the most ambitious work in coding, enterprise workflows, and the sciences */
  | "claude-fable-5-2"
  /** Built for the most demanding cybersecurity and life sciences research, available through verification programs */
  | "claude-mythos-5-2"
  /** Fastest model for high-volume, real-time tasks */
  | "claude-haiku-5-5"
  /** Efficient model for coding and agents */
  | "claude-sonnet-5-5"
  /** Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows */
  | "claude-fable-5-1"
  /** Powerful intelligence for coding, knowledge work, and long-running agents */
  | "claude-opus-5-5"
  /** Our most capable model for cybersecurity and biology research, available through trusted access programs */
  | "claude-mythos-5-1"
  /** Efficient model for coding and agents */
  | "claude-sonnet-5"
  /** Next generation of intelligence for the hardest knowledge work and coding problems */
  | "claude-fable-5"
  /** Most capable model for cybersecurity and biology research */
  | "claude-mythos-5"
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
   * New class of intelligence, strongest in coding and cybersecurity
   * @deprecated Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.
   */
  | "claude-mythos-preview"
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

interface RefusalStopDetails {
  type: "refusal";
  /**
   * The policy category that triggered the refusal. `null` when the refusal doesn't map to a named category.
   * - `"cyber"`: The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.
   * - `"bio"`: The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.
   * - `"frontier_llm"`: The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.
   * - `"reasoning_extraction"`: The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking?sdk_languages=typescript).
   * - `"general_harms"`: The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.
   */
  category: "cyber" | "bio" | "frontier_llm" | "reasoning_extraction" | "general_harms" | null;
  /** Human-readable explanation of the refusal. This text is not guaranteed to be stable. `null` when no explanation is available for the category. */
  explanation: string | null;
}

type StopReason = "end_turn" | "max_tokens" | "stop_sequence" | "tool_use" | "pause_turn" | "refusal" | "model_context_window_exceeded";

interface Usage {
  /** Breakdown of cached tokens by TTL */
  cache_creation: CacheCreation | null;
  /** The number of input tokens used to create the cache entry. */
  cache_creation_input_tokens: number | null; // minimum: 0
  /** The number of input tokens read from the cache. */
  cache_read_input_tokens: number | null; // minimum: 0
  /** The geographic region where inference was performed for this request. */
  inference_geo: string | null;
  /** The number of input tokens which were used. */
  input_tokens: number; // minimum: 0
  /** The number of output tokens which were used. */
  output_tokens: number; // minimum: 0
  /** Breakdown of output tokens by category. `output_tokens` remains the inclusive, authoritative total used for billing. This object provides a read-only decomposition for observability — for example, how many of the billed output tokens were spent on internal reasoning that may have been summarized before being returned to you. */
  output_tokens_details: OutputTokensDetails | null;
  /** The number of server tool requests. */
  server_tool_use: ServerToolUsage | null;
  /** If the request used the priority, standard, or batch tier. */
  service_tier: "standard" | "priority" | "batch" | null;
  /** The inference speed mode used for this request. */
  speed: "standard" | "fast" | null;
}

interface ContainerSkill {
  /** Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined) */
  type: "anthropic" | "custom";
  /** Skill ID */
  skill_id: string; // minLength: 1, maxLength: 64
  /** The resolved version: a skill version ID for custom skills. */
  version: string; // minLength: 1, maxLength: 64
}

type CacheMissReason = CacheMissModelChanged | CacheMissSystemChanged | CacheMissToolsChanged | CacheMissMessagesChanged | CacheMissPreviousMessageNotFound | CacheMissUnavailable;

/** A `cache_miss_reason` for a request whose `model` or `speed` differs from the previous request's. See the [cache diagnostics guide](https://platform.claude.com/docs/en/build-with-claude/cache-diagnostics?sdk_languages=typescript#cache-miss-reason-types) to learn what to change for each reason. */
interface CacheMissModelChanged {
  type: "model_changed";
  /** Approximate number of input tokens that would have been read from cache had the prefix matched the previous request. */
  cache_missed_input_tokens: number;
}

/** A `cache_miss_reason` for a request whose `system` differs from the previous request's. See the [cache diagnostics guide](https://platform.claude.com/docs/en/build-with-claude/cache-diagnostics?sdk_languages=typescript#cache-miss-reason-types) to learn what to change for each reason. */
interface CacheMissSystemChanged {
  type: "system_changed";
  /** Approximate number of input tokens that would have been read from cache had the prefix matched the previous request. */
  cache_missed_input_tokens: number;
}

/** A `cache_miss_reason` for a request whose `tools` differ from the previous request's, for example because tools were added, removed, or reordered. See the [cache diagnostics guide](https://platform.claude.com/docs/en/build-with-claude/cache-diagnostics?sdk_languages=typescript#cache-miss-reason-types) to learn what to change for each reason. */
interface CacheMissToolsChanged {
  type: "tools_changed";
  /** Approximate number of input tokens that would have been read from cache had the prefix matched the previous request. */
  cache_missed_input_tokens: number;
}

/** A `cache_miss_reason` for a request whose `messages` differ from the previous request's in an earlier entry, instead of only having entries appended. The `model`, `system`, and `tools` match. See the [cache diagnostics guide](https://platform.claude.com/docs/en/build-with-claude/cache-diagnostics?sdk_languages=typescript#cache-miss-reason-types) to learn what to change for each reason. */
interface CacheMissMessagesChanged {
  type: "messages_changed";
  /** Approximate number of input tokens that would have been read from cache had the prefix matched the previous request. */
  cache_missed_input_tokens: number;
}

/** A `cache_miss_reason` for when the API doesn't have a stored record of the request that `diagnostics.previous_message_id` references. This doesn't mean that this request changed. See the [cache diagnostics guide](https://platform.claude.com/docs/en/build-with-claude/cache-diagnostics?sdk_languages=typescript#cache-miss-reason-types) to learn what to change for each reason. */
interface CacheMissPreviousMessageNotFound {
  type: "previous_message_not_found";
}

/** A `cache_miss_reason` for when the API can't give a diagnosis. The request itself was processed normally. This includes a request whose `model`, `system`, and `tools` match the previous request's but whose other prompt-affecting parameters, such as `thinking` or `tool_choice`, differ. See the [cache diagnostics guide](https://platform.claude.com/docs/en/build-with-claude/cache-diagnostics?sdk_languages=typescript#cache-miss-reason-types) to learn what to change for each reason. */
interface CacheMissUnavailable {
  type: "unavailable";
}

interface CacheCreation {
  /** The number of input tokens used to create the 1 hour cache entry. */
  ephemeral_1h_input_tokens: number; // default: 0, minimum: 0
  /** The number of input tokens used to create the 5 minute cache entry. */
  ephemeral_5m_input_tokens: number; // default: 0, minimum: 0
}

interface OutputTokensDetails {
  /** Number of output tokens the model generated as internal reasoning, including the thinking-block delimiter tokens. Reflects the raw reasoning the model produced, not the (possibly shorter) summarized thinking text returned in the response body. It may differ from the model's exact generation count by a small number of tokens. Always ≤ `output_tokens`; `output_tokens - thinking_tokens` approximates the non-reasoning output. */
  thinking_tokens: number; // default: 0, minimum: 0
}

interface ServerToolUsage {
  /** The number of web fetch tool requests. */
  web_fetch_requests: number; // default: 0, minimum: 0
  /** The number of web search tool requests. */
  web_search_requests: number; // default: 0, minimum: 0
}

interface TextBlock {
  type: "text";
  /** Citations supporting the text block. The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`. */
  citations: Array<TextCitation> | null;
  text: string;
}

interface ThinkingBlock {
  type: "thinking";
  /** A value used to verify that this thinking block was generated by Claude when it is passed back to the API. This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact. See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking?sdk_languages=typescript) for details. */
  signature: string;
  /** The text of Claude's thinking process for this block. */
  thinking: string;
}

interface RedactedThinkingBlock {
  type: "redacted_thinking";
  /** The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content. Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation. See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking?sdk_languages=typescript#redacted-thinking-blocks) for details. */
  data: string;
}

interface ToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120; // default: {"type":"direct"}
  input: Record<string, unknown>;
  name: string; // minLength: 1
  /** For a toolset member tool_use, the toolset family. */
  toolset_name?: string | null; // minLength: 1, maxLength: 64, pattern: ^[a-zA-Z0-9_-]+$
}

interface ServerToolUseBlock {
  type: "server_tool_use";
  id: string; // pattern: ^srvtoolu_[a-zA-Z0-9_]+$
  caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120; // default: {"type":"direct"}
  input: Record<string, unknown>;
  name: "web_search" | "web_fetch" | "code_execution" | "bash_code_execution" | "text_editor_code_execution" | "tool_search_tool_regex" | "tool_search_tool_bm25";
}

interface WebSearchToolResultBlock {
  type: "web_search_tool_result";
  caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120; // default: {"type":"direct"}
  content: WebSearchToolResultBlockContent;
  tool_use_id: string; // pattern: ^srvtoolu_[a-zA-Z0-9_]+$
}

interface WebFetchToolResultBlock {
  type: "web_fetch_tool_result";
  caller: DirectCaller | ServerToolCaller | ServerToolCaller20260120; // default: {"type":"direct"}
  content: WebFetchToolResultErrorBlock | WebFetchBlock;
  tool_use_id: string; // pattern: ^srvtoolu_[a-zA-Z0-9_]+$
}

interface CodeExecutionToolResultBlock {
  type: "code_execution_tool_result";
  content: CodeExecutionToolResultBlockContent;
  tool_use_id: string; // pattern: ^srvtoolu_[a-zA-Z0-9_]+$
}

interface BashCodeExecutionToolResultBlock {
  type: "bash_code_execution_tool_result";
  content: BashCodeExecutionToolResultError | BashCodeExecutionResultBlock;
  tool_use_id: string; // pattern: ^srvtoolu_[a-zA-Z0-9_]+$
}

interface TextEditorCodeExecutionToolResultBlock {
  type: "text_editor_code_execution_tool_result";
  content: TextEditorCodeExecutionToolResultError | TextEditorCodeExecutionViewResultBlock | TextEditorCodeExecutionCreateResultBlock | TextEditorCodeExecutionStrReplaceResultBlock;
  tool_use_id: string; // pattern: ^srvtoolu_[a-zA-Z0-9_]+$
}

interface ToolSearchToolResultBlock {
  type: "tool_search_tool_result";
  content: ToolSearchToolResultError | ToolSearchToolSearchResultBlock;
  tool_use_id: string; // pattern: ^srvtoolu_[a-zA-Z0-9_]+$
}

/** Response model for a file uploaded to the container. */
interface ContainerUploadBlock {
  type: "container_upload";
  file_id: string;
}

/** Tool invocation directly from the model. */
interface DirectCaller {
  type: "direct";
}

/** Tool invocation generated by a server-side tool. */
interface ServerToolCaller {
  type: "code_execution_20250825";
  tool_id: string; // pattern: ^srvtoolu_[a-zA-Z0-9_]+$
}

interface ServerToolCaller20260120 {
  type: "code_execution_20260120";
  tool_id: string; // pattern: ^srvtoolu_[a-zA-Z0-9_]+$
}

type WebSearchToolResultBlockContent = WebSearchToolResultError | Array<WebSearchResultBlock>;

interface WebSearchToolResultError {
  type: "web_search_tool_result_error";
  error_code: WebSearchToolResultErrorCode;
}

interface WebSearchResultBlock {
  type: "web_search_result";
  encrypted_content: string;
  page_age: string | null;
  title: string;
  url: string;
}

type WebSearchToolResultErrorCode = "invalid_tool_input" | "unavailable" | "max_uses_exceeded" | "too_many_requests" | "query_too_long" | "request_too_large";

interface WebFetchToolResultErrorBlock {
  type: "web_fetch_tool_result_error";
  error_code: WebFetchToolResultErrorCode;
}

interface WebFetchBlock {
  type: "web_fetch_result";
  content: DocumentBlock;
  /** ISO 8601 timestamp when the content was retrieved */
  retrieved_at: string | null;
  /** Fetched content URL */
  url: string;
}

type WebFetchToolResultErrorCode = "invalid_tool_input" | "url_too_long" | "url_not_allowed" | "url_not_in_prior_context" | "url_not_accessible" | "unsupported_content_type" | "too_many_requests" | "max_uses_exceeded" | "unavailable" | "content_too_large";

interface DocumentBlock {
  type: "document";
  /** Citation configuration for the document */
  citations: CitationsConfig | null;
  source: Base64PDFSource | PlainTextSource;
  /** The title of the document */
  title: string | null;
}

interface CitationsConfig {
  enabled: boolean; // default: false
}

interface Base64PDFSource {
  type: "base64";
  data: string; // format: byte
  media_type: "application/pdf";
}

interface PlainTextSource {
  type: "text";
  data: string;
  media_type: "text/plain";
}

type CodeExecutionToolResultBlockContent = CodeExecutionToolResultError | CodeExecutionResultBlock | EncryptedCodeExecutionResultBlock;

interface CodeExecutionToolResultError {
  type: "code_execution_tool_result_error";
  error_code: CodeExecutionToolResultErrorCode;
}

interface CodeExecutionResultBlock {
  type: "code_execution_result";
  content: Array<CodeExecutionOutputBlock>;
  return_code: number;
  stderr: string;
  stdout: string;
}

/** The output and exit code of Python code that Claude ran with the code execution tool, with standard output in encrypted form. The API returns this block in place of `code_execution_result` when the code called the web search tool. See the [programmatic tool calling guide](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling?sdk_languages=typescript) to learn more about programmatic tool calling. */
interface EncryptedCodeExecutionResultBlock {
  type: "encrypted_code_execution_result";
  content: Array<CodeExecutionOutputBlock>;
  encrypted_stdout: string;
  return_code: number;
  stderr: string;
}

type CodeExecutionToolResultErrorCode = "invalid_tool_input" | "unavailable" | "too_many_requests" | "execution_time_exceeded";

interface CodeExecutionOutputBlock {
  type: "code_execution_output";
  file_id: string;
}

interface BashCodeExecutionToolResultError {
  type: "bash_code_execution_tool_result_error";
  error_code: BashCodeExecutionToolResultErrorCode;
}

interface BashCodeExecutionResultBlock {
  type: "bash_code_execution_result";
  content: Array<BashCodeExecutionOutputBlock>;
  return_code: number;
  stderr: string;
  stdout: string;
}

type BashCodeExecutionToolResultErrorCode = "invalid_tool_input" | "unavailable" | "too_many_requests" | "execution_time_exceeded" | "output_file_too_large";

interface BashCodeExecutionOutputBlock {
  type: "bash_code_execution_output";
  file_id: string;
}

interface TextEditorCodeExecutionToolResultError {
  type: "text_editor_code_execution_tool_result_error";
  error_code: TextEditorCodeExecutionToolResultErrorCode;
  error_message: string | null;
}

interface TextEditorCodeExecutionViewResultBlock {
  type: "text_editor_code_execution_view_result";
  content: string;
  file_type: "text" | "image" | "pdf";
  num_lines: number | null;
  start_line: number | null;
  total_lines: number | null;
}

interface TextEditorCodeExecutionCreateResultBlock {
  type: "text_editor_code_execution_create_result";
  is_file_update: boolean;
}

interface TextEditorCodeExecutionStrReplaceResultBlock {
  type: "text_editor_code_execution_str_replace_result";
  lines: Array<string> | null;
  new_lines: number | null;
  new_start: number | null;
  old_lines: number | null;
  old_start: number | null;
}

type TextEditorCodeExecutionToolResultErrorCode = "invalid_tool_input" | "unavailable" | "too_many_requests" | "execution_time_exceeded" | "file_not_found";

interface ToolSearchToolResultError {
  type: "tool_search_tool_result_error";
  error_code: ToolSearchToolResultErrorCode;
  error_message: string | null;
}

interface ToolSearchToolSearchResultBlock {
  type: "tool_search_tool_search_result";
  tool_references: Array<ToolReferenceBlock>;
}

type ToolSearchToolResultErrorCode = "invalid_tool_input" | "unavailable" | "too_many_requests" | "execution_time_exceeded";

interface ToolReferenceBlock {
  type: "tool_reference";
  tool_name: string; // minLength: 1, maxLength: 256, pattern: ^[a-zA-Z0-9_-]{1,256}$
}

type TextCitation = CitationCharLocation | CitationPageLocation | CitationContentBlockLocation | CitationsWebSearchResultLocation | CitationsSearchResultLocation;

interface CitationCharLocation {
  type: "char_location";
  cited_text: string;
  document_index: number; // minimum: 0
  document_title: string | null;
  end_char_index: number;
  file_id: string | null;
  start_char_index: number; // minimum: 0
}

interface CitationPageLocation {
  type: "page_location";
  cited_text: string;
  document_index: number; // minimum: 0
  document_title: string | null;
  end_page_number: number;
  file_id: string | null;
  start_page_number: number; // minimum: 1
}

interface CitationContentBlockLocation {
  type: "content_block_location";
  /** The full text of the cited block range, concatenated. Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns. */
  cited_text: string;
  document_index: number; // minimum: 0
  document_title: string | null;
  /** Exclusive 0-based end index of the cited block range in the source's `content` array. Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`. */
  end_block_index: number;
  file_id: string | null;
  /** 0-based index of the first cited block in the source's `content` array. */
  start_block_index: number; // minimum: 0
}

interface CitationsWebSearchResultLocation {
  type: "web_search_result_location";
  cited_text: string;
  encrypted_index: string;
  title: string | null; // maxLength: 512
  url: string;
}

interface CitationsSearchResultLocation {
  type: "search_result_location";
  /** The full text of the cited block range, concatenated. Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns. */
  cited_text: string;
  /** Exclusive 0-based end index of the cited block range in the source's `content` array. Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`. */
  end_block_index: number;
  /** 0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results. Counted separately from `document_index`; server-side web search results are not included in this count. */
  search_result_index: number; // minimum: 0
  source: string;
  /** 0-based index of the first cited block in the source's `content` array. */
  start_block_index: number; // minimum: 0
  title: string | null;
}
````
