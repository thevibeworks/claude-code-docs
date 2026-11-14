---
title: Create a Message Batch
url: https://platform.claude.com/docs/en/api/typescript/messages/batches/create
---

# Create a Message Batch

- Signature: `client.messages.batches.create(params: BatchCreateParams, options?: RequestOptions): MessageBatch`
- Endpoint: `POST /v1/messages/batches`

Send a batch of Message creation requests.

The Message Batches API can be used to process multiple Messages API requests at once. Once a Message Batch is created, it begins processing immediately. Batches can take up to 24 hours to complete.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing?sdk_languages=typescript)

## Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const messageBatch = await client.messages.batches.create({
  requests: [
    {
      custom_id: "my-custom-id-1",
      params: {
        max_tokens: 1024,
        messages: [{ content: "Hello, world", role: "user" }],
        model: "claude-opus-5-5"
      }
    }
  ]
});

console.log(messageBatch.id);
```

## Example response (200)

```json
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "archived_at": "2024-08-20T18:37:24.100435Z",
  "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
  "created_at": "2024-08-20T18:37:24.100435Z",
  "ended_at": "2024-08-20T18:37:24.100435Z",
  "expires_at": "2024-08-20T18:37:24.100435Z",
  "processing_status": "in_progress",
  "request_counts": {
    "canceled": 10,
    "errored": 30,
    "expired": 10,
    "processing": 100,
    "succeeded": 50
  },
  "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
  "type": "message_batch"
}
```

## Parameters

```ts
interface BatchCreateParams {
  /** List of requests for prompt completion. Each is an individual request to create a Message. */
  requests: Array<Request>; // minItems: 1, maxItems: 100000
  /** The user profile ID to attribute the requests in this batch to. Use when acting on behalf of a party other than your organization. Applies to every request in the batch; an individual request whose `user_profile_id` body field conflicts with this header is errored. */
  user_profile_id?: string; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

## Returns

```ts
interface MessageBatch {
  /** Object type. For Message Batches, this is always `"message_batch"`. */
  type: "message_batch";
  /** Unique object identifier. The format and length of IDs may change over time. */
  id: string;
  /** RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable. */
  archived_at: string | null; // format: date-time
  /** RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated. */
  cancel_initiated_at: string | null; // format: date-time
  /** RFC 3339 datetime string representing the time at which the Message Batch was created. */
  created_at: string; // format: date-time
  /** RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends. Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired. */
  ended_at: string | null; // format: date-time
  /** RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation. */
  expires_at: string; // format: date-time
  /** Processing status of the Message Batch. */
  processing_status: "in_progress" | "canceling" | "ended";
  /** Tallies requests within the Message Batch, categorized by their status. Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch. */
  request_counts: MessageBatchRequestCounts;
  /** URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends. Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests. */
  results_url: string | null;
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

- `EnforcedSpendLimitReachedError` (HTTP status 429, error code `enforced_spend_limit_reached`)

  The organization has crossed the monthly API usage threshold of its API tier.

## Types

````ts
interface Request {
  /** Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order. Must be unique for each request within the Message Batch. */
  custom_id: string; // minLength: 1, maxLength: 64, pattern: ^[a-zA-Z0-9_-]{1,64}$
  /** Messages API creation parameters for the individual request. See the [Messages API reference](https://platform.claude.com/docs/en/api/messages?sdk_languages=typescript) for full documentation on available parameters. */
  params: Params;
}

interface MessageBatchRequestCounts {
  /** Number of requests in the Message Batch that have been canceled. This is zero until processing of the entire Message Batch has ended. */
  canceled: number; // default: 0
  /** Number of requests in the Message Batch that encountered an error. This is zero until processing of the entire Message Batch has ended. */
  errored: number; // default: 0
  /** Number of requests in the Message Batch that have expired. This is zero until processing of the entire Message Batch has ended. */
  expired: number; // default: 0
  /** Number of requests in the Message Batch that are processing. */
  processing: number; // default: 0
  /** Number of requests in the Message Batch that have completed successfully. This is zero until processing of the entire Message Batch has ended. */
  succeeded: number; // default: 0
}

interface Params {
  /** The maximum number of tokens to generate before stopping. Note that our models may stop _before_ reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate. Set to `0` to populate the [prompt cache](https://platform.claude.com/docs/en/build-with-claude/prompt-caching?sdk_languages=typescript#pre-warming-the-cache) without generating a response. Different models have different maximum values for this parameter.  See [models](https://platform.claude.com/docs/en/about-claude/models/overview?sdk_languages=typescript) for details. */
  max_tokens: number; // minimum: 0
  /**
   * Input messages.
   *
   * Our models are trained to operate on alternating `user` and `assistant` conversational turns. When creating a new `Message`, you specify the prior conversational turns with the `messages` parameter, and the model then generates the next `Message` in the conversation. Consecutive `user` or `assistant` turns in your request will be combined into a single turn.
   *
   * Each input message must be an object with a `role` and `content`. You can specify a single `user`-role message, or you can include multiple `user` and `assistant` messages.
   *
   * If the final message uses the `assistant` role, the response content will continue immediately from the content in that message. This can be used to constrain part of the model's response. This is called prefill. On models that don't support prefill, creating a message that ends with a partial `assistant` response returns a 400 error. See [Prefill not supported](https://platform.claude.com/docs/en/api/errors?sdk_languages=typescript#prefill-not-supported).
   *
   * Example with a single `user` message:
   *
   * ```json
   * [{"role": "user", "content": "Hello, Claude"}]
   * ```
   *
   * Example with multiple conversational turns:
   *
   * ```json
   * [
   *   {"role": "user", "content": "Hello there."},
   *   {"role": "assistant", "content": "Hi, I'm Claude. How can I help you?"},
   *   {"role": "user", "content": "Can you explain LLMs in plain English?"},
   * ]
   * ```
   *
   * Example with a partially-filled response from Claude, for models that support prefill:
   *
   * ```json
   * [
   *   {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
   *   {"role": "assistant", "content": "The best answer is ("},
   * ]
   * ```
   *
   * Each input message `content` may be either a single `string` or an array of content blocks, where each block has a specific `type`. Using a `string` for `content` is shorthand for an array of one content block of type `"text"`. The following input messages are equivalent:
   *
   * ```json
   * {"role": "user", "content": "Hello, Claude"}
   * ```
   *
   * ```json
   * {"role": "user", "content": [{"type": "text", "text": "Hello, Claude"}]}
   * ```
   *
   * See [input examples](https://platform.claude.com/docs/en/build-with-claude/working-with-messages?sdk_languages=typescript).
   *
   * Note that if you want to include a [system prompt](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices?sdk_languages=typescript#give-claude-a-role), you can use the top-level `system` parameter.
   *
   * There is a limit of 100,000 messages in a single request.
   */
  messages: Array<MessageParam>;
  /** The model that will complete your prompt. See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options. */
  model: Model;
  /** Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request. */
  cache_control?: CacheControlEphemeral | null;
  /** Container identifier for reuse across requests. */
  container?: MessageCreateParamsContainer | null;
  /** Request-level diagnostics. Supply `previous_message_id` to have the response include `diagnostics.cache_miss_reason` explaining any prompt-cache divergence from that prior request. */
  diagnostics?: DiagnosticsParam | null;
  /** Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used. */
  inference_geo?: string | null;
  /** An object describing metadata about the request. */
  metadata?: Metadata;
  /** Configuration options for the model's output, such as the output format. */
  output_config?: OutputConfig;
  /** Determines whether to use priority capacity (if available) or standard capacity for this request. Anthropic offers different levels of service for your API requests. See [service-tiers](https://platform.claude.com/docs/en/api/service-tiers?sdk_languages=typescript) for details. */
  service_tier?: "auto" | "standard_only";
  /** The inference speed mode for this request. `"fast"` enables high output-tokens-per-second inference. Some models require the `fast-mode-2026-02-01` beta header for any `speed` value. See [fast mode](https://platform.claude.com/docs/en/build-with-claude/fast-mode?sdk_languages=typescript) for which models. */
  speed?: "standard" | "fast" | null;
  /** Custom text sequences that will cause the model to stop generating. Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`. If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence. */
  stop_sequences?: Array<string>;
  /** Whether to incrementally stream the response using server-sent events. When `true`, SDKs return a raw event stream. In the TypeScript, Python and Ruby SDKs, the recommended way to stream is `messages.stream()`. It sets `stream` for you and accumulates the events into the final message. See [Streaming with SDKs](https://platform.claude.com/docs/en/build-with-claude/streaming?sdk_languages=typescript#streaming-with-sdks) for an example in each language. */
  stream?: boolean;
  /** System prompt. A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices?sdk_languages=typescript#give-claude-a-role). */
  system?: string | Array<TextBlockParam>;
  /** Configuration for Claude's thinking. With `{"type": "adaptive"}`, Claude decides when and how much to think. With `{"type": "enabled"}` (manual extended thinking), you set a `budget_tokens` of at least 1,024. Thinking tokens count toward your `max_tokens` limit. Which `type` values are accepted, and what happens when you omit `thinking`, depend on the model. See [thinking](https://platform.claude.com/docs/en/build-with-claude/thinking?sdk_languages=typescript#configuring-thinking) for each model's behavior. */
  thinking?: ThinkingConfigParam;
  /** How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all. */
  tool_choice?: ToolChoice;
  /**
   * Definitions of tools that the model may use.
   *
   * If you include `tools` in your API request, the model may return `tool_use` content blocks that represent the model's use of those tools. You can then run those tools using the tool input generated by the model and then optionally return results back to the model using `tool_result` content blocks.
   *
   * There are two types of tools: **client tools** and **server tools**. The behavior described below applies to client tools. For [server tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools?sdk_languages=typescript), see their individual documentation as each has its own behavior (e.g., the [web search tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool?sdk_languages=typescript)).
   *
   * Each tool definition includes:
   *
   * * `name`: Name of the tool.
   * * `description`: Optional, but strongly-recommended description of the tool.
   * * `input_schema`: [JSON schema](https://json-schema.org/draft/2020-12) for the tool `input` shape that the model will produce in `tool_use` output content blocks.
   *
   * For example, if you defined `tools` as:
   *
   * ```json
   * [
   *   {
   *     "name": "get_stock_price",
   *     "description": "Get the current stock price for a given ticker symbol.",
   *     "input_schema": {
   *       "type": "object",
   *       "properties": {
   *         "ticker": {
   *           "type": "string",
   *           "description": "The stock ticker symbol, e.g. AAPL for Apple Inc."
   *         }
   *       },
   *       "required": ["ticker"]
   *     }
   *   }
   * ]
   * ```
   *
   * And then asked the model "What's the S&P 500 at today?", the model might produce `tool_use` content blocks in the response like this:
   *
   * ```json
   * [
   *   {
   *     "type": "tool_use",
   *     "id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
   *     "name": "get_stock_price",
   *     "input": { "ticker": "^GSPC" }
   *   }
   * ]
   * ```
   *
   * You might then run your `get_stock_price` tool with `{"ticker": "^GSPC"}` as an input, and return the following back to the model in a subsequent `user` message:
   *
   * ```json
   * [
   *   {
   *     "type": "tool_result",
   *     "tool_use_id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
   *     "content": "259.75 USD"
   *   }
   * ]
   * ```
   *
   * Tools can be used for workflows that include running client-side tools and functions, or more generally whenever you want the model to produce a particular JSON structure of output.
   *
   * See our [guide](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview?sdk_languages=typescript) for more details.
   */
  tools?: Array<ToolUnion>;
}

type MessageParam = UserMessageParam | AssistantMessageParam | SystemMessageParam;

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

interface CacheControlEphemeral {
  type: "ephemeral";
  /**
   * The time-to-live for the cache control breakpoint.
   *
   * This may be one the following values:
   *
   * - `5m`: 5 minutes
   * - `1h`: 1 hour
   *
   * Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching?sdk_languages=typescript) for details.
   */
  ttl?: "5m" | "1h";
}

type MessageCreateParamsContainer = ContainerParams | string | null;

interface DiagnosticsParam {
  /** The `id` (`msg_...`) from this client's previous /v1/messages response. The server compares that request's prompt fingerprint against this one and returns `diagnostics.cache_miss_reason` when the prompt-cache prefix could not be reused. Pass `null` on the first turn to opt in without a prior message to compare. */
  previous_message_id?: string | null; // maxLength: 256
}

interface Metadata {
  /** An external identifier for the user who is associated with the request. This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number. */
  user_id?: string | null; // maxLength: 512
}

interface OutputConfig {
  /** How much effort the model should put into its response. Higher effort levels may result in more thorough analysis but take longer. Valid values are `low`, `medium`, `high`, `xhigh`, or `max`. */
  effort?: "low" | "medium" | "high" | "xhigh" | "max" | null;
  /** A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs?sdk_languages=typescript) */
  format?: JSONOutputFormat | null;
}

interface TextBlockParam {
  type: "text";
  text: string; // minLength: 1
  /** Create a cache control breakpoint at this content block. */
  cache_control?: CacheControlEphemeral | null;
  citations?: Array<TextCitationParam> | null;
}

type ThinkingConfigParam = ThinkingConfigEnabled | ThinkingConfigDisabled | ThinkingConfigBetweenTools | ThinkingConfigAdaptive;

type ToolChoice = ToolChoiceAuto | ToolChoiceAny | ToolChoiceTool | ToolChoiceNone;

type ToolUnion = Tool | ToolBash20250124 | CodeExecutionTool20250522 | CodeExecutionTool20250825 | CodeExecutionTool20260120 | CodeExecutionTool20260521 | BrowserToolset20260801 | MemoryTool20250818 | ComputerToolset20260801 | ToolTextEditor20250124 | ToolTextEditor20250429 | ToolTextEditor20250728 | WebSearchTool20250305 | WebFetchTool20250910 | WebSearchTool20260209 | WebFetchTool20260209 | WebFetchTool20260309 | WebSearchTool20260318 | WebFetchTool20260318 | ToolSearchToolBm25_20251119 | ToolSearchToolRegex20251119;

interface UserMessageParam {
  content: MessageContentParam;
  role: "user";
}

interface AssistantMessageParam {
  content: MessageContentParam;
  role: "assistant";
}

interface SystemMessageParam {
  content: string | Array<TextBlockParam>;
  role: "system";
}

type MessageContentParam = string | Array<ContentBlockParam>;

type ContentBlockParam = TextBlockParam | ImageBlockParam | DocumentBlockParam | SearchResultBlockParam | ThinkingBlockParam | RedactedThinkingBlockParam | ToolUseBlockParam | ToolResultBlockParam | ServerToolUseBlockParam | WebSearchToolResultBlockParam | WebFetchToolResultBlockParam | CodeExecutionToolResultBlockParam | BashCodeExecutionToolResultBlockParam | TextEditorCodeExecutionToolResultBlockParam | ToolSearchToolResultBlockParam | ContainerUploadBlockParam;

interface ImageBlockParam {
  type: "image";
  source: Base64ImageSource | URLImageSource | FileImageSource;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: CacheControlEphemeral | null;
  /** Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field. */
  transformations?: ImageTransformationsParam | null;
}

interface DocumentBlockParam {
  type: "document";
  source: Base64PDFSource | PlainTextSource | ContentBlockSource | URLPDFSource | FileDocumentSource;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: CacheControlEphemeral | null;
  citations?: CitationsConfigParam | null;
  context?: string | null; // minLength: 1
  title?: string | null; // minLength: 1, maxLength: 500
}

interface SearchResultBlockParam {
  type: "search_result";
  content: Array<TextBlockParam>;
  source: string;
  title: string;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: CacheControlEphemeral | null;
  citations?: CitationsConfigParam;
}

interface ThinkingBlockParam {
  type: "thinking";
  /** The `signature` value of this thinking block, exactly as returned by the API in a previous response. Used to verify that the block was generated by Claude. Thinking blocks must be passed back unmodified and in their original order; a modified block results in a 400 `invalid_request_error`. */
  signature: string;
  /** The `thinking` text of this block as returned by the API. */
  thinking: string;
}

interface RedactedThinkingBlockParam {
  type: "redacted_thinking";
  /** The `data` value of this redacted thinking block, exactly as returned by the API in a previous response. Opaque and encrypted; pass it back unchanged. */
  data: string;
}

interface ToolUseBlockParam {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  input: Record<string, unknown>;
  name: string; // minLength: 1, maxLength: 200
  /** Create a cache control breakpoint at this content block. */
  cache_control?: CacheControlEphemeral | null;
  caller?: DirectCaller | ServerToolCaller | ServerToolCaller20260120;
  /** For a toolset member tool_use, the toolset family this member belongs to. */
  toolset_name?: string | null; // minLength: 1, maxLength: 64, pattern: ^[a-zA-Z0-9_-]+$
}

interface ToolResultBlockParam {
  type: "tool_result";
  tool_use_id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Create a cache control breakpoint at this content block. */
  cache_control?: CacheControlEphemeral | null;
  content?: string | Array<TextBlockParam | ImageBlockParam | SearchResultBlockParam | DocumentBlockParam | ToolReferenceBlockParam | BrowserStateBlockParam>;
  is_error?: boolean;
  /** For a toolset member tool_result, the toolset family of the paired tool_use. */
  toolset_name?: string | null; // minLength: 1, maxLength: 64, pattern: ^[a-zA-Z0-9_-]+$
}

interface ServerToolUseBlockParam {
  type: "server_tool_use";
  id: string; // pattern: ^srvtoolu_[a-zA-Z0-9_]+$
  input: Record<string, unknown>;
  name: "web_search" | "web_fetch" | "code_execution" | "bash_code_execution" | "text_editor_code_execution" | "tool_search_tool_regex" | "tool_search_tool_bm25";
  /** Create a cache control breakpoint at this content block. */
  cache_control?: CacheControlEphemeral | null;
  caller?: DirectCaller | ServerToolCaller | ServerToolCaller20260120;
}

interface WebSearchToolResultBlockParam {
  type: "web_search_tool_result";
  content: WebSearchToolResultBlockParamContent;
  tool_use_id: string; // pattern: ^srvtoolu_[a-zA-Z0-9_]+$
  /** Create a cache control breakpoint at this content block. */
  cache_control?: CacheControlEphemeral | null;
  caller?: DirectCaller | ServerToolCaller | ServerToolCaller20260120;
}

interface WebFetchToolResultBlockParam {
  type: "web_fetch_tool_result";
  content: WebFetchToolResultErrorBlockParam | WebFetchBlockParam;
  tool_use_id: string; // pattern: ^srvtoolu_[a-zA-Z0-9_]+$
  /** Create a cache control breakpoint at this content block. */
  cache_control?: CacheControlEphemeral | null;
  caller?: DirectCaller | ServerToolCaller | ServerToolCaller20260120;
}

interface CodeExecutionToolResultBlockParam {
  type: "code_execution_tool_result";
  content: CodeExecutionToolResultBlockParamContent;
  tool_use_id: string; // pattern: ^srvtoolu_[a-zA-Z0-9_]+$
  /** Create a cache control breakpoint at this content block. */
  cache_control?: CacheControlEphemeral | null;
}

interface BashCodeExecutionToolResultBlockParam {
  type: "bash_code_execution_tool_result";
  content: BashCodeExecutionToolResultErrorParam | BashCodeExecutionResultBlockParam;
  tool_use_id: string; // pattern: ^srvtoolu_[a-zA-Z0-9_]+$
  /** Create a cache control breakpoint at this content block. */
  cache_control?: CacheControlEphemeral | null;
}

interface TextEditorCodeExecutionToolResultBlockParam {
  type: "text_editor_code_execution_tool_result";
  content: TextEditorCodeExecutionToolResultErrorParam | TextEditorCodeExecutionViewResultBlockParam | TextEditorCodeExecutionCreateResultBlockParam | TextEditorCodeExecutionStrReplaceResultBlockParam;
  tool_use_id: string; // pattern: ^srvtoolu_[a-zA-Z0-9_]+$
  /** Create a cache control breakpoint at this content block. */
  cache_control?: CacheControlEphemeral | null;
}

interface ToolSearchToolResultBlockParam {
  type: "tool_search_tool_result";
  content: ToolSearchToolResultErrorParam | ToolSearchToolSearchResultBlockParam;
  tool_use_id: string; // pattern: ^srvtoolu_[a-zA-Z0-9_]+$
  /** Create a cache control breakpoint at this content block. */
  cache_control?: CacheControlEphemeral | null;
}

/** A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory. */
interface ContainerUploadBlockParam {
  type: "container_upload";
  file_id: string;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: CacheControlEphemeral | null;
}

interface Base64ImageSource {
  type: "base64";
  data: string; // format: byte
  media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp";
}

interface URLImageSource {
  type: "url";
  url: string;
}

interface FileImageSource {
  type: "file";
  file_id: string;
}

interface ImageTransformationsParam {
  /** What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down. */
  oversized_image?: "downsize" | "error";
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

interface ContentBlockSource {
  type: "content";
  content: string | Array<ContentBlockSourceContent>;
}

interface URLPDFSource {
  type: "url";
  url: string;
}

interface FileDocumentSource {
  type: "file";
  file_id: string;
}

interface CitationsConfigParam {
  enabled?: boolean;
}

type ContentBlockSourceContent = TextBlockParam | ImageBlockParam;

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

type WebSearchToolResultBlockParamContent = Array<WebSearchResultBlockParam> | WebSearchToolRequestError;

interface WebSearchResultBlockParam {
  type: "web_search_result";
  encrypted_content: string;
  title: string;
  url: string;
  page_age?: string | null;
}

interface WebSearchToolRequestError {
  type: "web_search_tool_result_error";
  error_code: WebSearchToolResultErrorCode;
}

type WebSearchToolResultErrorCode = "invalid_tool_input" | "unavailable" | "max_uses_exceeded" | "too_many_requests" | "query_too_long" | "request_too_large";

interface WebFetchToolResultErrorBlockParam {
  type: "web_fetch_tool_result_error";
  error_code: WebFetchToolResultErrorCode;
}

interface WebFetchBlockParam {
  type: "web_fetch_result";
  content: DocumentBlockParam;
  /** Fetched content URL */
  url: string;
  /** ISO 8601 timestamp when the content was retrieved */
  retrieved_at?: string | null;
}

type WebFetchToolResultErrorCode = "invalid_tool_input" | "url_too_long" | "url_not_allowed" | "url_not_in_prior_context" | "url_not_accessible" | "unsupported_content_type" | "too_many_requests" | "max_uses_exceeded" | "unavailable" | "content_too_large";

type CodeExecutionToolResultBlockParamContent = CodeExecutionToolResultErrorParam | CodeExecutionResultBlockParam | EncryptedCodeExecutionResultBlockParam;

interface CodeExecutionToolResultErrorParam {
  type: "code_execution_tool_result_error";
  error_code: CodeExecutionToolResultErrorCode;
}

interface CodeExecutionResultBlockParam {
  type: "code_execution_result";
  content: Array<CodeExecutionOutputBlockParam>;
  return_code: number;
  stderr: string;
  stdout: string;
}

/** The output and exit code of Python code that Claude ran with the code execution tool, with standard output in encrypted form, sent back in a later request. */
interface EncryptedCodeExecutionResultBlockParam {
  type: "encrypted_code_execution_result";
  content: Array<CodeExecutionOutputBlockParam>;
  encrypted_stdout: string;
  return_code: number;
  stderr: string;
}

type CodeExecutionToolResultErrorCode = "invalid_tool_input" | "unavailable" | "too_many_requests" | "execution_time_exceeded";

interface CodeExecutionOutputBlockParam {
  type: "code_execution_output";
  file_id: string;
}

interface BashCodeExecutionToolResultErrorParam {
  type: "bash_code_execution_tool_result_error";
  error_code: BashCodeExecutionToolResultErrorCode;
}

interface BashCodeExecutionResultBlockParam {
  type: "bash_code_execution_result";
  content: Array<BashCodeExecutionOutputBlockParam>;
  return_code: number;
  stderr: string;
  stdout: string;
}

type BashCodeExecutionToolResultErrorCode = "invalid_tool_input" | "unavailable" | "too_many_requests" | "execution_time_exceeded" | "output_file_too_large";

interface BashCodeExecutionOutputBlockParam {
  type: "bash_code_execution_output";
  file_id: string;
}

interface TextEditorCodeExecutionToolResultErrorParam {
  type: "text_editor_code_execution_tool_result_error";
  error_code: TextEditorCodeExecutionToolResultErrorCode;
  error_message?: string | null;
}

interface TextEditorCodeExecutionViewResultBlockParam {
  type: "text_editor_code_execution_view_result";
  content: string;
  file_type: "text" | "image" | "pdf";
  num_lines?: number | null;
  start_line?: number | null;
  total_lines?: number | null;
}

interface TextEditorCodeExecutionCreateResultBlockParam {
  type: "text_editor_code_execution_create_result";
  is_file_update: boolean;
}

interface TextEditorCodeExecutionStrReplaceResultBlockParam {
  type: "text_editor_code_execution_str_replace_result";
  lines?: Array<string> | null;
  new_lines?: number | null;
  new_start?: number | null;
  old_lines?: number | null;
  old_start?: number | null;
}

type TextEditorCodeExecutionToolResultErrorCode = "invalid_tool_input" | "unavailable" | "too_many_requests" | "execution_time_exceeded" | "file_not_found";

interface ToolSearchToolResultErrorParam {
  type: "tool_search_tool_result_error";
  error_code: ToolSearchToolResultErrorCode;
  error_message?: string | null;
}

interface ToolSearchToolSearchResultBlockParam {
  type: "tool_search_tool_search_result";
  tool_references: Array<ToolReferenceBlockParam>;
}

type ToolSearchToolResultErrorCode = "invalid_tool_input" | "unavailable" | "too_many_requests" | "execution_time_exceeded";

/** Tool reference block that can be included in tool_result content. */
interface ToolReferenceBlockParam {
  type: "tool_reference";
  tool_name: string; // minLength: 1, maxLength: 256, pattern: ^[a-zA-Z0-9_-]{1,256}$
  /** Create a cache control breakpoint at this content block. */
  cache_control?: CacheControlEphemeral | null;
}

/** The caller's browser state after a browser toolset member call — the full inventory of open tabs, which tab is active, and any side effects (tabs opened, download state changes) the call produced. At most one per `tool_result`, only on a non-error result answering a browser toolset member `tool_use`. The server renders the model-visible text from it; the model never sees the raw fields. */
interface BrowserStateBlockParam {
  type: "browser_state";
  /** All tabs open in the browser after this call — the full inventory, not a delta. May be empty. Whenever non-empty, exactly one entry carries `active: true`. */
  tabs: Array<BrowserStateTabEntry>; // maxItems: 100
  /** Create a cache control breakpoint at this content block. */
  cache_control?: CacheControlEphemeral | null;
  /** Tabs opened and download state changes during this call. "Nothing to report" is expressed by omitting the field, never by an empty list. */
  state_changes?: Array<BrowserStateChange> | null; // minItems: 1, maxItems: 200
}

interface BrowserStateTabEntry {
  /** The caller-assigned identifier for this tab, unique within the inventory. */
  tab_id: string; // minLength: 1, maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$
  /** The title of the page the tab is showing. May be empty. */
  title: string; // maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$
  /** The URL of the page the tab is showing. May be empty. */
  url: string; // maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$
  /** Whether this tab is the active tab after this call. Whenever `tabs` is non-empty, exactly one entry is marked `active: true`. */
  active?: boolean;
}

type BrowserStateChange = BrowserStateChangeTabOpened | BrowserStateChangeDownloadStarted | BrowserStateChangeDownloadCompleted | BrowserStateChangeDownloadFailed;

/** A tab this call's execution opened that remains open at its end — the creation delta of the `tabs` inventory, not an event log. Carries only the `tab_id`; the tab's `title` and `url` live on its `tabs` entry, which must include the same `tab_id`. A tab opened during a failed call gets no deferred `tab_opened`; it simply appears in the next result's `tabs` inventory. */
interface BrowserStateChangeTabOpened {
  type: "tab_opened";
  /** The `tab_id` of the opened tab, present in `tabs`. */
  tab_id: string; // minLength: 1, maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$
}

/** A file download that started during this call. */
interface BrowserStateChangeDownloadStarted {
  type: "download_started";
  /** The caller-assigned identifier for this download, stable across the state changes reporting it. */
  download_id: string; // minLength: 1, maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$
  /** The final post-redirect URL the download was served from. */
  url: string; // maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$
}

/** A file download that finished during this call, reported with the same `download_id` as its `download_started` — or without a prior `download_started`, when the download finished during the call that started it (at most one state change per `download_id` per result). */
interface BrowserStateChangeDownloadCompleted {
  type: "download_completed";
  /** The caller-assigned identifier for this download, stable across the state changes reporting it. */
  download_id: string; // minLength: 1, maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$
  /** The final post-redirect URL the download was served from. */
  url: string; // maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$
  /** Where the executor saved the file, on the executor's filesystem. Only included when another tool in the same environment can read the file at that path. */
  path?: string | null; // maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$
  /** The completed download's size. */
  size_bytes?: number | null; // minimum: 0
}

/** A file download that failed — or was cancelled — during this call. */
interface BrowserStateChangeDownloadFailed {
  type: "download_failed";
  /** The caller-assigned identifier for this download, stable across the state changes reporting it. */
  download_id: string; // minLength: 1, maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$
  /** The final post-redirect URL the download was served from. */
  url: string; // maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$
  /** The failure or cancellation detail, when known. */
  error?: string | null; // maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$
}

/** Container parameters with skills to be loaded. */
interface ContainerParams {
  /** Container id */
  id?: string | null;
  /** List of skills to load in the container */
  skills?: Array<SkillParams> | null; // maxItems: 20
}

interface SkillParams {
  /** Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined) */
  type: "anthropic" | "custom";
  /** Skill ID */
  skill_id: string; // minLength: 1, maxLength: 64
  /** Skill version or 'latest' for most recent version */
  version?: string; // minLength: 1, maxLength: 64
}

interface JSONOutputFormat {
  type: "json_schema";
  /** The JSON schema of the format */
  schema: Record<string, unknown>;
}

type TextCitationParam = CitationCharLocationParam | CitationPageLocationParam | CitationContentBlockLocationParam | CitationWebSearchResultLocationParam | CitationSearchResultLocationParam;

interface CitationCharLocationParam {
  type: "char_location";
  cited_text: string;
  document_index: number; // minimum: 0
  document_title: string | null; // minLength: 1, maxLength: 500
  end_char_index: number;
  start_char_index: number; // minimum: 0
}

interface CitationPageLocationParam {
  type: "page_location";
  cited_text: string;
  document_index: number; // minimum: 0
  document_title: string | null; // minLength: 1, maxLength: 500
  end_page_number: number;
  start_page_number: number; // minimum: 1
}

interface CitationContentBlockLocationParam {
  type: "content_block_location";
  /** The full text of the cited block range, concatenated. Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns. */
  cited_text: string;
  document_index: number; // minimum: 0
  document_title: string | null; // minLength: 1, maxLength: 500
  /** Exclusive 0-based end index of the cited block range in the source's `content` array. Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`. */
  end_block_index: number;
  /** 0-based index of the first cited block in the source's `content` array. */
  start_block_index: number; // minimum: 0
}

interface CitationWebSearchResultLocationParam {
  type: "web_search_result_location";
  cited_text: string;
  encrypted_index: string;
  title: string | null; // minLength: 1, maxLength: 512
  url: string; // minLength: 1
}

interface CitationSearchResultLocationParam {
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

interface ThinkingConfigEnabled {
  type: "enabled";
  /** Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality. Must be ≥1024 and less than `max_tokens`. See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking?sdk_languages=typescript) for details. */
  budget_tokens: number; // minimum: 1024
  /** Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. The default depends on the model; see [Controlling thinking display](https://platform.claude.com/docs/en/build-with-claude/thinking?sdk_languages=typescript#controlling-thinking-display). */
  display?: "summarized" | "omitted" | null;
}

interface ThinkingConfigDisabled {
  type: "disabled";
}

interface ThinkingConfigBetweenTools {
  type: "between_tools";
}

interface ThinkingConfigAdaptive {
  type: "adaptive";
  /** Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. The default depends on the model; see [Controlling thinking display](https://platform.claude.com/docs/en/build-with-claude/thinking?sdk_languages=typescript#controlling-thinking-display). */
  display?: "summarized" | "omitted" | null;
}

/** The model will automatically decide whether to use tools. */
interface ToolChoiceAuto {
  type: "auto";
  /** Whether to disable parallel tool use. Defaults to `false`. If set to `true`, the model will output at most one tool use. */
  disable_parallel_tool_use?: boolean;
}

/** The model will use any available tools. */
interface ToolChoiceAny {
  type: "any";
  /** Whether to disable parallel tool use. Defaults to `false`. If set to `true`, the model will output exactly one tool use. */
  disable_parallel_tool_use?: boolean;
}

/** The model will use the specified tool with `tool_choice.name`. */
interface ToolChoiceTool {
  type: "tool";
  /** The name of the tool to use. */
  name: string;
  /** Whether to disable parallel tool use. Defaults to `false`. If set to `true`, the model will output exactly one tool use. */
  disable_parallel_tool_use?: boolean;
}

/** The model will not be allowed to use tools. */
interface ToolChoiceNone {
  type: "none";
}

interface Tool {
  type?: "custom" | null;
  /** [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input. This defines the shape of the `input` that your tool accepts and that the model will produce. */
  input_schema: InputSchema;
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: string; // minLength: 1, maxLength: 128, pattern: ^[a-zA-Z0-9_-]{1,128}$
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: CacheControlEphemeral | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  /** Description of what this tool does. Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema. */
  description?: string;
  /** Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers. */
  eager_input_streaming?: boolean | null;
  input_examples?: Array<Record<string, unknown>>;
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
}

interface ToolBash20250124 {
  type: "bash_20250124";
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "bash";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: CacheControlEphemeral | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  input_examples?: Array<Record<string, unknown>>;
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
}

interface CodeExecutionTool20250522 {
  type: "code_execution_20250522";
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "code_execution";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: CacheControlEphemeral | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
}

interface CodeExecutionTool20250825 {
  type: "code_execution_20250825";
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "code_execution";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: CacheControlEphemeral | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
}

/** A `tools` entry for the code execution tool, version `code_execution_20260120`. It adds REPL state persistence to version `code_execution_20250825`. REPL state persistence applies with programmatic tool calling. With it, the Python interpreter state, such as variable bindings, persists across requests that reuse the container. See the [code execution tool guide](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool?sdk_languages=typescript#tool-versions) to learn what each tool version adds. */
interface CodeExecutionTool20260120 {
  type: "code_execution_20260120";
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "code_execution";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: CacheControlEphemeral | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
}

/** Code execution tool with REPL state persistence. */
interface CodeExecutionTool20260521 {
  type: "code_execution_20260521";
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "code_execution";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: CacheControlEphemeral | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
}

/** The browser toolset: a single `tools[]` entry (carrying no `name`) that declares the browser tool family. The model is served the family's tool with any members disabled via `configs` removed from its schema. */
interface BrowserToolset20260801 {
  type: "browser_toolset_20260801";
  /** Create a cache control breakpoint at this content block. */
  cache_control?: CacheControlEphemeral | null;
  /** Sparse per-member overrides, keyed by member name. Absent, null, and {} are equivalent; a member's defaults apply wherever its key is absent. */
  configs?: BrowserToolsetConfigs | null;
}

interface MemoryTool20250818 {
  type: "memory_20250818";
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "memory";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: CacheControlEphemeral | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  input_examples?: Array<Record<string, unknown>>;
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
}

/** The computer toolset: a single `tools[]` entry (carrying no `name`) that declares the computer tool family. The model is served the family's tool with any members disabled via `configs` removed from its schema. Every member is enabled by default, zoom included. The single-tool options `display_number` and `enable_zoom` are not fields of a toolset entry — it carries only `type`, `configs`, and `cache_control`; zoom is controlled via `configs.zoom.enabled`. */
interface ComputerToolset20260801 {
  type: "computer_toolset_20260801";
  /** Create a cache control breakpoint at this content block. */
  cache_control?: CacheControlEphemeral | null;
  /** Sparse per-member overrides, keyed by member name. Absent, null, and {} are equivalent; a member's defaults apply wherever its key is absent. */
  configs?: ComputerToolsetConfigs | null;
}

interface ToolTextEditor20250124 {
  type: "text_editor_20250124";
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "str_replace_editor";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: CacheControlEphemeral | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  input_examples?: Array<Record<string, unknown>>;
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
}

interface ToolTextEditor20250429 {
  type: "text_editor_20250429";
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "str_replace_based_edit_tool";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: CacheControlEphemeral | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  input_examples?: Array<Record<string, unknown>>;
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
}

interface ToolTextEditor20250728 {
  type: "text_editor_20250728";
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "str_replace_based_edit_tool";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: CacheControlEphemeral | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  input_examples?: Array<Record<string, unknown>>;
  /** Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file. */
  max_characters?: number | null; // minimum: 1
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
}

interface WebSearchTool20250305 {
  type: "web_search_20250305";
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "web_search";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`. */
  allowed_domains?: Array<string> | null;
  /** If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`. */
  blocked_domains?: Array<string> | null;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: CacheControlEphemeral | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  /** Maximum number of times the tool can be used in the API request. */
  max_uses?: number | null; // minimum: 1
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
  /** Parameters for the user's location. Used to provide more relevant search results. */
  user_location?: UserLocation | null;
}

interface WebFetchTool20250910 {
  type: "web_fetch_20250910";
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "web_fetch";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** List of domains to allow fetching from */
  allowed_domains?: Array<string> | null;
  /** List of domains to block fetching from */
  blocked_domains?: Array<string> | null;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: CacheControlEphemeral | null;
  /** Citations configuration for fetched documents. Citations are disabled by default. */
  citations?: CitationsConfigParam | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  /** Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs. */
  max_content_tokens?: number | null; // minimum: 1
  /** Maximum number of times the tool can be used in the API request. */
  max_uses?: number | null; // minimum: 1
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
  /** Which sources contribute to the set of URLs the tool may fetch. Omitted means every source. */
  url_sources?: WebFetchURLSources | null;
}

interface WebSearchTool20260209 {
  type: "web_search_20260209";
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "web_search";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`. */
  allowed_domains?: Array<string> | null;
  /** If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`. */
  blocked_domains?: Array<string> | null;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: CacheControlEphemeral | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  /** Maximum number of times the tool can be used in the API request. */
  max_uses?: number | null; // minimum: 1
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
  /** Parameters for the user's location. Used to provide more relevant search results. */
  user_location?: UserLocation | null;
}

interface WebFetchTool20260209 {
  type: "web_fetch_20260209";
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "web_fetch";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** List of domains to allow fetching from */
  allowed_domains?: Array<string> | null;
  /** List of domains to block fetching from */
  blocked_domains?: Array<string> | null;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: CacheControlEphemeral | null;
  /** Citations configuration for fetched documents. Citations are disabled by default. */
  citations?: CitationsConfigParam | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  /** Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs. */
  max_content_tokens?: number | null; // minimum: 1
  /** Maximum number of times the tool can be used in the API request. */
  max_uses?: number | null; // minimum: 1
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
  /** Which sources contribute to the set of URLs the tool may fetch. Omitted means every source. */
  url_sources?: WebFetchURLSources | null;
}

/** Web fetch tool with use_cache parameter for bypassing cached content. */
interface WebFetchTool20260309 {
  type: "web_fetch_20260309";
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "web_fetch";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** List of domains to allow fetching from */
  allowed_domains?: Array<string> | null;
  /** List of domains to block fetching from */
  blocked_domains?: Array<string> | null;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: CacheControlEphemeral | null;
  /** Citations configuration for fetched documents. Citations are disabled by default. */
  citations?: CitationsConfigParam | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  /** Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs. */
  max_content_tokens?: number | null; // minimum: 1
  /** Maximum number of times the tool can be used in the API request. */
  max_uses?: number | null; // minimum: 1
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
  /** Which sources contribute to the set of URLs the tool may fetch. Omitted means every source. */
  url_sources?: WebFetchURLSources | null;
  /** Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources. */
  use_cache?: boolean;
}

interface WebSearchTool20260318 {
  type: "web_search_20260318";
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "web_search";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`. */
  allowed_domains?: Array<string> | null;
  /** If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`. */
  blocked_domains?: Array<string> | null;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: CacheControlEphemeral | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  /** Maximum number of times the tool can be used in the API request. */
  max_uses?: number | null; // minimum: 1
  /** How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn. */
  response_inclusion?: "full" | "excluded";
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
  /** Parameters for the user's location. Used to provide more relevant search results. */
  user_location?: UserLocation | null;
}

interface WebFetchTool20260318 {
  type: "web_fetch_20260318";
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "web_fetch";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** List of domains to allow fetching from */
  allowed_domains?: Array<string> | null;
  /** List of domains to block fetching from */
  blocked_domains?: Array<string> | null;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: CacheControlEphemeral | null;
  /** Citations configuration for fetched documents. Citations are disabled by default. */
  citations?: CitationsConfigParam | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  /** Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs. */
  max_content_tokens?: number | null; // minimum: 1
  /** Maximum number of times the tool can be used in the API request. */
  max_uses?: number | null; // minimum: 1
  /** How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn. */
  response_inclusion?: "full" | "excluded";
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
  /** Which sources contribute to the set of URLs the tool may fetch. Omitted means every source. */
  url_sources?: WebFetchURLSources | null;
  /** Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources. */
  use_cache?: boolean;
}

interface ToolSearchToolBm25_20251119 {
  type: "tool_search_tool_bm25_20251119" | "tool_search_tool_bm25";
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "tool_search_tool_bm25";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: CacheControlEphemeral | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
}

interface ToolSearchToolRegex20251119 {
  type: "tool_search_tool_regex_20251119" | "tool_search_tool_regex";
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "tool_search_tool_regex";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: CacheControlEphemeral | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
}

interface InputSchema {
  type: "object";
  properties?: Record<string, unknown> | null;
  required?: Array<string> | null;
}

interface ComputerToolsetConfigs {
  /** `type`'s config overrides. */
  type?: ComputerTypeConfig | null;
  /** `cursor_position`'s config overrides. */
  cursor_position?: ComputerCursorPositionConfig | null;
  /** `double_click`'s config overrides. */
  double_click?: ComputerDoubleClickConfig | null;
  /** `hold_key`'s config overrides. */
  hold_key?: ComputerHoldKeyConfig | null;
  /** `key`'s config overrides. */
  key?: ComputerKeyConfig | null;
  /** `left_click`'s config overrides. */
  left_click?: ComputerLeftClickConfig | null;
  /** `left_click_drag`'s config overrides. */
  left_click_drag?: ComputerLeftClickDragConfig | null;
  /** `left_mouse_down`'s config overrides. */
  left_mouse_down?: ComputerLeftMouseDownConfig | null;
  /** `left_mouse_up`'s config overrides. */
  left_mouse_up?: ComputerLeftMouseUpConfig | null;
  /** `middle_click`'s config overrides. */
  middle_click?: ComputerMiddleClickConfig | null;
  /** `mouse_move`'s config overrides. */
  mouse_move?: ComputerMouseMoveConfig | null;
  /** `right_click`'s config overrides. */
  right_click?: ComputerRightClickConfig | null;
  /** `screenshot`'s config overrides. */
  screenshot?: ComputerScreenshotConfig | null;
  /** `scroll`'s config overrides. */
  scroll?: ComputerScrollConfig | null;
  /** `triple_click`'s config overrides. */
  triple_click?: ComputerTripleClickConfig | null;
  /** `wait`'s config overrides. */
  wait?: ComputerWaitConfig | null;
  /** `zoom`'s config overrides. */
  zoom?: ComputerZoomConfig | null;
}

interface ComputerTypeConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface ComputerCursorPositionConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface ComputerDoubleClickConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface ComputerHoldKeyConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface ComputerKeyConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface ComputerLeftClickConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface ComputerLeftClickDragConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface ComputerLeftMouseDownConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface ComputerLeftMouseUpConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface ComputerMiddleClickConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface ComputerMouseMoveConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface ComputerRightClickConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface ComputerScreenshotConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface ComputerScrollConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface ComputerTripleClickConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface ComputerWaitConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface ComputerZoomConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface UserLocation {
  type: "approximate";
  /** The city of the user. */
  city?: string | null; // minLength: 1, maxLength: 255
  /** The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user. */
  country?: string | null; // minLength: 2, maxLength: 2
  /** The region of the user. */
  region?: string | null; // minLength: 1, maxLength: 255
  /** The [IANA timezone](https://nodatime.org/TimeZones) of the user. */
  timezone?: string | null; // minLength: 1, maxLength: 255
}

interface WebFetchURLSources {
  /** Which client tools' results contribute fetchable URLs: "all", "none", or an only or except list of client tool names from tools[]. */
  client_tool_results?: WebFetchURLSourceAll | WebFetchURLSourceNone | WebFetchURLSourceOnly | WebFetchURLSourceExcept;
  /** Which server tools' results contribute fetchable URLs: "all", "none", or an only or except list of server tool names from tools[]; only web_search and web_fetch results ever contribute. */
  server_tool_results?: WebFetchURLSourceAll | WebFetchURLSourceNone | WebFetchURLSourceOnly | WebFetchURLSourceExcept;
  /** Whether URLs in user messages are fetchable: "all" or "none". */
  user_input?: WebFetchURLSourceAll | WebFetchURLSourceNone;
}

/** The `url_sources` variant under which a source contributes in full: every result of the tool filter's source, or all user input. */
interface WebFetchURLSourceAll {
  type: "all";
}

/** The `url_sources` variant under which a source contributes nothing: no result of the tool filter's source, or no user input. */
interface WebFetchURLSourceNone {
  type: "none";
}

/** The tool filter variant under which only the named tools' results contribute. */
interface WebFetchURLSourceOnly {
  type: "only";
  tools: Array<WebFetchURLSourceToolReference>;
}

/** The tool filter variant under which every result but the named tools' contributes. */
interface WebFetchURLSourceExcept {
  type: "except";
  tools: Array<WebFetchURLSourceToolReference>;
}

/** One entry of a tool filter's `tools`: it must name a tool declared in this request's `tools[]`. */
interface WebFetchURLSourceToolReference {
  type: "tool_reference";
  name: string;
}

interface BrowserToolsetConfigs {
  /** `type`'s config overrides. */
  type?: BrowserTypeConfig | null;
  /** `close_tab`'s config overrides. */
  close_tab?: BrowserCloseTabConfig | null;
  /** `double_click`'s config overrides. */
  double_click?: BrowserDoubleClickConfig | null;
  /** `file_upload`'s config overrides. */
  file_upload?: BrowserFileUploadConfig | null;
  /** `find`'s config overrides. */
  find?: BrowserFindConfig | null;
  /** `form_input`'s config overrides. */
  form_input?: BrowserFormInputConfig | null;
  /** `get_page_text`'s config overrides. */
  get_page_text?: BrowserGetPageTextConfig | null;
  /** `hold_key`'s config overrides. */
  hold_key?: BrowserHoldKeyConfig | null;
  /** `hover`'s config overrides. */
  hover?: BrowserHoverConfig | null;
  /** `javascript_exec`'s config overrides. */
  javascript_exec?: BrowserJavascriptExecConfig | null;
  /** `key`'s config overrides. */
  key?: BrowserKeyConfig | null;
  /** `left_click`'s config overrides. */
  left_click?: BrowserLeftClickConfig | null;
  /** `left_click_drag`'s config overrides. */
  left_click_drag?: BrowserLeftClickDragConfig | null;
  /** `left_mouse_down`'s config overrides. */
  left_mouse_down?: BrowserLeftMouseDownConfig | null;
  /** `left_mouse_up`'s config overrides. */
  left_mouse_up?: BrowserLeftMouseUpConfig | null;
  /** `list_tabs`'s config overrides. */
  list_tabs?: BrowserListTabsConfig | null;
  /** `middle_click`'s config overrides. */
  middle_click?: BrowserMiddleClickConfig | null;
  /** `mouse_move`'s config overrides. */
  mouse_move?: BrowserMouseMoveConfig | null;
  /** `navigate`'s config overrides. */
  navigate?: BrowserNavigateConfig | null;
  /** `new_tab`'s config overrides. */
  new_tab?: BrowserNewTabConfig | null;
  /** `read_console`'s config overrides. */
  read_console?: BrowserReadConsoleConfig | null;
  /** `read_network`'s config overrides. */
  read_network?: BrowserReadNetworkConfig | null;
  /** `read_page`'s config overrides. */
  read_page?: BrowserReadPageConfig | null;
  /** `right_click`'s config overrides. */
  right_click?: BrowserRightClickConfig | null;
  /** `screenshot`'s config overrides. */
  screenshot?: BrowserScreenshotConfig | null;
  /** `scroll`'s config overrides. */
  scroll?: BrowserScrollConfig | null;
  /** `scroll_to`'s config overrides. */
  scroll_to?: BrowserScrollToConfig | null;
  /** `switch_tab`'s config overrides. */
  switch_tab?: BrowserSwitchTabConfig | null;
  /** `triple_click`'s config overrides. */
  triple_click?: BrowserTripleClickConfig | null;
  /** `wait`'s config overrides. */
  wait?: BrowserWaitConfig | null;
  /** `zoom`'s config overrides. */
  zoom?: BrowserZoomConfig | null;
}

interface BrowserTypeConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface BrowserCloseTabConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface BrowserDoubleClickConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface BrowserFileUploadConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface BrowserFindConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface BrowserFormInputConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface BrowserGetPageTextConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface BrowserHoldKeyConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface BrowserHoverConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface BrowserJavascriptExecConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface BrowserKeyConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface BrowserLeftClickConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface BrowserLeftClickDragConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface BrowserLeftMouseDownConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface BrowserLeftMouseUpConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface BrowserListTabsConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface BrowserMiddleClickConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface BrowserMouseMoveConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface BrowserNavigateConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface BrowserNewTabConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface BrowserReadConsoleConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface BrowserReadNetworkConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface BrowserReadPageConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface BrowserRightClickConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface BrowserScreenshotConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface BrowserScrollConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface BrowserScrollToConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface BrowserSwitchTabConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface BrowserTripleClickConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface BrowserWaitConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface BrowserZoomConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}
````
