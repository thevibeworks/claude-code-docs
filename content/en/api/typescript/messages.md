---
title: Messages
url: https://platform.claude.com/docs/en/api/typescript/messages
---

# Messages

## Create a Message

- Signature: `client.messages.create(params: MessageCreateParams, options?: RequestOptions): Message | Stream<RawMessageStreamEvent>`
- Endpoint: `POST /v1/messages`

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

The Messages API can be used for either single queries or stateless multi-turn conversations.

Learn more about the Messages API in our [user guide](https://platform.claude.com/docs/en/get-started?sdk_languages=typescript)

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const message = await client.messages.create({
  max_tokens: 1024,
  messages: [{ content: "Hello, world", role: "user" }],
  model: "claude-opus-5-5"
});

console.log(message.id);
```

### Example response (200)

```json
{
  "id": "msg_013Zva2CMHLNnXjNJJKqJ2EF",
  "container": {
    "id": "container_011CpZohnwH4vuy7gazohgSP",
    "expires_at": "2019-12-27T18:11:19.117Z",
    "skills": [
      {
        "skill_id": "pdf",
        "type": "anthropic",
        "version": "latest"
      }
    ]
  },
  "content": [
    {
      "citations": null,
      "text": "Hi! My name is Claude.",
      "type": "text"
    }
  ],
  "diagnostics": null,
  "model": "claude-opus-5-5",
  "role": "assistant",
  "stop_details": null,
  "stop_reason": "end_turn",
  "stop_sequence": null,
  "type": "message",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_creation_input_tokens": 2051,
    "cache_read_input_tokens": 2051,
    "inference_geo": "global",
    "input_tokens": 2095,
    "output_tokens": 503,
    "output_tokens_details": {
      "thinking_tokens": 0
    },
    "server_tool_use": {
      "web_fetch_requests": 2,
      "web_search_requests": 0
    },
    "service_tier": "standard",
    "speed": "standard"
  }
}
```

### Parameters

````ts
// This page declares each type one time, in the first method that uses it.

interface MessageCreateParams {
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
  /** The user profile ID to attribute this request to. Use when acting on behalf of a party other than your organization. */
  user_profile_id?: string; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
````

### Returns

- When `stream` is `false` or omitted: `Message`
- When `stream` is `true`: `Stream<RawMessageStreamEvent>`

````ts
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

type RawMessageStreamEvent = RawMessageStartEvent | RawMessageDeltaEvent | RawMessageStopEvent | RawContentBlockStartEvent | RawContentBlockDeltaEvent | RawContentBlockStopEvent;
````

### Errors

Any method can also return the general [HTTP errors](https://platform.claude.com/docs/en/api/errors?sdk_languages=typescript).

On a streaming call, the errors listed below apply when the API rejects the request before the stream starts. An error partway through the stream can arrive as a more general error type. To identify it, use its error code, if it has one, not its type.

- `AvailableToolsLimitExceededError` (HTTP status 400, error code `available_tools_limit_exceeded`)

  The tools available after a message exceed a limit on their number or their size.

- `ClaudeCodeKeyCreatorNotMemberError` (HTTP status 400, error code `claude_code_key_creator_not_member`)

  The API key belongs to the Claude Code workspace, and the user who created it is no longer a member of the organization or of that workspace.

- `ClaudeCodeVersionTooOldError` (HTTP status 400, error code `claude_code_version_too_old`)

  The request comes from a Claude Code version older than the minimum that the requested model or the organization requires. Update Claude Code, then retry.

- `CMEKKeyDisabledError` (HTTP status 400, error code `cmek_key_disabled`)

  The workspace's customer-managed encryption key is disabled or revoked. Re-enable the key, then retry.

- `CMEKKeyNetworkBlockedError` (HTTP status 400, error code `cmek_key_network_blocked`)

  The key management service's network access controls blocked the request to the workspace's customer-managed encryption key. The key itself may be healthy.

- `CompactionBlockAmbiguousError` (HTTP status 400, error code `compaction_block_ambiguous`)

  `messages` holds more than one `compaction` block with content. Send only the block the conversation returned last.

- `CompactionBlockMisplacedError` (HTTP status 400, error code `compaction_block_misplaced`)

  The `compaction` block is not the first block of the conversation, or is in a `system` message.

- `CompactionContentMismatchError` (HTTP status 400, error code `compaction_content_mismatch`)

  The `compaction` block's `content` differs from the text its `signature` recorded.

- `CompactionIncompleteTurnError` (HTTP status 400, error code `compaction_incomplete_turn`)

  The compaction request ends on an `assistant` turn that is not finished.

- `CompactionNothingToSummarizeError` (HTTP status 400, error code `compaction_nothing_to_summarize`)

  `messages` holds no `user` or `assistant` content to summarize or adopt.

- `CompactionSignatureInvalidError` (HTTP status 400, error code `compaction_signature_invalid`)

  The `compaction` block's `signature` does not verify.

- `CompactionTooManyToolReferencesError` (HTTP status 400, error code `compaction_too_many_tool_references`)

  The conversation references more distinct tools than a `compaction` block can record.

- `CompactionToolChangesMismatchError` (HTTP status 400, error code `compaction_tool_changes_mismatch`)

  The `compaction` block's `tool_changes` differs from what was returned with the block.

- `OrganizationOnHoldError` (HTTP status 400, error code `organization_on_hold`)

  Anthropic has disabled the organization for trust and safety reasons. An organization disabled for any other reason, such as billing, does not get this code. `appeal_url`, when present, is where the organization can appeal.

- `RequestBodyEncodingInvalidError` (HTTP status 400, error code `request_body_encoding_invalid`)

  The request body is not valid for its `Content-Encoding`.

- `RequestBodyEncodingUnsupportedError` (HTTP status 400, error code `request_body_encoding_unsupported`)

  The request's `Content-Encoding` is not supported.

- `ThreadAlreadyContinuedError` (HTTP status 400, error code `thread_already_continued`)

  The response that `previous_message_id` names has already been continued, and each response can be continued only once. Continue from the Thread's most recent response `id`.

- `ThreadContinueInFlightError` (HTTP status 400, error code `thread_continue_in_flight`)

  Another request is still continuing from the same `previous_message_id`. Wait for it to complete and continue from its response `id`, or replay the full conversation with `thread: {"type": "create"}`.

- `ThreadFingerprintMismatchError` (HTTP status 400, error code `thread_fingerprint_mismatch`)

  A field that must stay the same across a Thread's turns differs from the value stored with the Thread; the message names each such field. Send the stored values, or replay the full conversation with `thread: {"type": "create"}` to change them.

- `ThreadUnsupportedRequestError` (HTTP status 400, error code `thread_unsupported_request`)

  The request combines `thread` with a request field or an organization setting that Threads do not support; `unsupported`, when present, names it. Send the full conversation without `thread`, or change that field.

- `ToolNameConflictError` (HTTP status 400, error code `tool_name_conflict`)

  A tool made available in `messages` takes a name that an available tool of another kind, or of another MCP server, already holds.

- `ToolReferenceUnresolvedError` (HTTP status 400, error code `tool_reference_unresolved`)

  A tool change or MCP tool listing references a tool or MCP server that is not defined at that position in the conversation.

- `ThreadNotFoundError` (HTTP status 404, error code `thread_not_found`)

  No usable Thread state was found for `previous_message_id`. Replay the full conversation with `thread: {"type": "create"}` to start a new Thread.

- `SkillReadBlockedUndecryptableError` (HTTP status 409, error code `skill_read_blocked_undecryptable`)

  A custom skill the request names is stored under an encryption key state the workspace cannot currently decrypt.

- `RequestBodyTooLargeAfterDecodingError` (HTTP status 413, error code `request_body_too_large_after_decoding`)

  The compressed request body exceeds the request size limit once decoded.

- `EnforcedSpendLimitReachedError` (HTTP status 429, error code `enforced_spend_limit_reached`)

  The organization has crossed the monthly API usage threshold of its API tier.

- `RampLimitExceededError` (HTTP status 429, error code `ramp_limit_exceeded`)

  The request would exceed a ramp limit, which caps how fast usage can grow. Retry after the time in the `retry-after` header.

- `CMEKKeyUnreachableError` (HTTP status 503, error code `cmek_key_unreachable`)

  The workspace's customer-managed encryption key could not be reached. Retry the request; if this continues, check that the key is available in your key management service, or contact Anthropic support.

- `CompactionUnavailableError` (HTTP status 529, error code `compaction_unavailable`)

  The compaction could not be completed for a transient server reason. Retry the request.

### Types

```ts
type MessageParam = UserMessageParam | AssistantMessageParam | SystemMessageParam;

/** The model that will complete your prompt. See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options. */
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

/** Container identifier for reuse across requests. */
type MessageCreateParamsContainer = ContainerParams | string | null;

/** Request-level diagnostics. Currently carries the previous response id for prompt-cache divergence reporting. */
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

/** Configuration for Claude's thinking. With `{"type": "adaptive"}`, Claude decides when and how much to think. With `{"type": "enabled"}` (manual extended thinking), you set a `budget_tokens` of at least 1,024. Thinking tokens count toward your `max_tokens` limit. Which `type` values are accepted, and what happens when you omit `thinking`, depend on the model. See [thinking](https://platform.claude.com/docs/en/build-with-claude/thinking?sdk_languages=typescript#configuring-thinking) for each model's behavior. */
type ThinkingConfigParam = ThinkingConfigEnabled | ThinkingConfigDisabled | ThinkingConfigBetweenTools | ThinkingConfigAdaptive;

/** How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all. */
type ToolChoice = ToolChoiceAuto | ToolChoiceAny | ToolChoiceTool | ToolChoiceNone;

type ToolUnion = Tool | ToolBash20250124 | CodeExecutionTool20250522 | CodeExecutionTool20250825 | CodeExecutionTool20260120 | CodeExecutionTool20260521 | BrowserToolset20260801 | MemoryTool20250818 | ComputerToolset20260801 | ToolTextEditor20250124 | ToolTextEditor20250429 | ToolTextEditor20250728 | WebSearchTool20250305 | WebFetchTool20250910 | WebSearchTool20260209 | WebFetchTool20260209 | WebFetchTool20260309 | WebSearchTool20260318 | WebFetchTool20260318 | ToolSearchToolBm25_20251119 | ToolSearchToolRegex20251119;

/** Information about the container used in the request (for the code execution tool) */
interface Container {
  /** Identifier for the container used in this request */
  id: string;
  /** The time at which the container will expire. */
  expires_at: string; // format: date-time
  /** Skills loaded in the container */
  skills: Array<ContainerSkill> | null;
}

type ContentBlock = TextBlock | ThinkingBlock | RedactedThinkingBlock | ToolUseBlock | ServerToolUseBlock | WebSearchToolResultBlock | WebFetchToolResultBlock | CodeExecutionToolResultBlock | BashCodeExecutionToolResultBlock | TextEditorCodeExecutionToolResultBlock | ToolSearchToolResultBlock | ContainerUploadBlock;

/** Request-level diagnostics: why the prompt cache could not fully reuse the prefix of the request named by `diagnostics.previous_message_id`. */
interface Diagnostics {
  /** Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed. */
  cache_miss_reason: CacheMissReason | null;
}

/** Structured information about a refusal. */
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

interface RawMessageStartEvent {
  type: "message_start";
  message: Message;
}

interface RawMessageDeltaEvent {
  type: "message_delta";
  delta: Delta;
  /** Billing and rate-limit usage. Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems. Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response. For example, `output_tokens` will be non-zero, even for an empty string response from Claude. Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`. */
  usage: MessageDeltaUsage;
}

interface RawMessageStopEvent {
  type: "message_stop";
}

interface RawContentBlockStartEvent {
  type: "content_block_start";
  content_block: TextBlock | ThinkingBlock | RedactedThinkingBlock | ToolUseBlock | ServerToolUseBlock | WebSearchToolResultBlock | WebFetchToolResultBlock | CodeExecutionToolResultBlock | BashCodeExecutionToolResultBlock | TextEditorCodeExecutionToolResultBlock | ToolSearchToolResultBlock | ContainerUploadBlock;
  index: number;
}

interface RawContentBlockDeltaEvent {
  type: "content_block_delta";
  delta: RawContentBlockDelta;
  index: number;
}

interface RawContentBlockStopEvent {
  type: "content_block_stop";
  index: number;
}

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

/** Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field. */
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

/** One open browser tab reported in a `browser_state` block's `tabs` inventory. `tab_id` is the caller-assigned identifier for the tab; `title` and `url` describe the page the tab is currently showing and may be empty strings (a blank tab legitimately has both empty). `active` marks the tab that is active after this call; whenever `tabs` is non-empty, exactly one entry is marked. */
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

/** Specification for a skill to be loaded in a container. */
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

/** A skill that was loaded in a container (response model). */
interface ContainerSkill {
  /** Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined) */
  type: "anthropic" | "custom";
  /** Skill ID */
  skill_id: string; // minLength: 1, maxLength: 64
  /** The resolved version: a skill version ID for custom skills. */
  version: string; // minLength: 1, maxLength: 64
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

interface ToolSearchToolResultError {
  type: "tool_search_tool_result_error";
  error_code: ToolSearchToolResultErrorCode;
  error_message: string | null;
}

interface ToolSearchToolSearchResultBlock {
  type: "tool_search_tool_search_result";
  tool_references: Array<ToolReferenceBlock>;
}

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

interface Delta {
  /** Information about the container used in this request. This will be non-null if a container tool (e.g. code execution) was used. */
  container: Container | null;
  /** Structured information about why model output stopped. This is `null` when the `stop_reason` has no additional detail to report. */
  stop_details: RefusalStopDetails | null;
  stop_reason: StopReason | null;
  stop_sequence: string | null;
}

interface MessageDeltaUsage {
  /** The cumulative number of input tokens used to create the cache entry. */
  cache_creation_input_tokens: number | null; // minimum: 0
  /** The cumulative number of input tokens read from the cache. */
  cache_read_input_tokens: number | null; // minimum: 0
  /** The cumulative number of input tokens which were used. */
  input_tokens: number | null; // minimum: 0
  /** The cumulative number of output tokens which were used. */
  output_tokens: number;
  /** Breakdown of output tokens by category. `output_tokens` remains the inclusive, authoritative total used for billing. This object provides a read-only decomposition for observability — for example, how many of the billed output tokens were spent on internal reasoning that may have been summarized before being returned to you. */
  output_tokens_details: OutputTokensDetails | null;
  /** The number of server tool requests. */
  server_tool_use: ServerToolUsage | null;
}

type RawContentBlockDelta = TextDelta | InputJSONDelta | CitationsDelta | ThinkingDelta | SignatureDelta;

interface TextDelta {
  type: "text_delta";
  text: string;
}

interface InputJSONDelta {
  type: "input_json_delta";
  partial_json: string;
}

interface CitationsDelta {
  type: "citations_delta";
  citation: CitationCharLocation | CitationPageLocation | CitationContentBlockLocation | CitationsWebSearchResultLocation | CitationsSearchResultLocation;
}

interface ThinkingDelta {
  type: "thinking_delta";
  /** The incremental `thinking` text for this content block. Concatenate the `thinking` values of successive `thinking_delta` events to assemble the block's full `thinking` value. */
  thinking: string;
}

interface SignatureDelta {
  type: "signature_delta";
  /** The `signature` for this thinking block: an opaque value used to verify that the block was generated by Claude when it is passed back to the API. Delivered in a `signature_delta` event just before the block's `content_block_stop` event. */
  signature: string;
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

/** Per-member configuration for `computer_toolset_20260801`: one optional field per member tool, keyed by the member name — the same name the member's `tool_use` blocks carry. Every member is an accepted key, and a member's defaults apply wherever its key is absent. Unknown keys are rejected: the field set is this toolset version's complete member set. */
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

/** `type`'s config overrides. */
interface ComputerTypeConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `cursor_position`'s config overrides. */
interface ComputerCursorPositionConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `double_click`'s config overrides. */
interface ComputerDoubleClickConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `hold_key`'s config overrides. */
interface ComputerHoldKeyConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `key`'s config overrides. */
interface ComputerKeyConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `left_click`'s config overrides. */
interface ComputerLeftClickConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `left_click_drag`'s config overrides. */
interface ComputerLeftClickDragConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `left_mouse_down`'s config overrides. */
interface ComputerLeftMouseDownConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `left_mouse_up`'s config overrides. */
interface ComputerLeftMouseUpConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `middle_click`'s config overrides. */
interface ComputerMiddleClickConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `mouse_move`'s config overrides. */
interface ComputerMouseMoveConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `right_click`'s config overrides. */
interface ComputerRightClickConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `screenshot`'s config overrides. */
interface ComputerScreenshotConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `scroll`'s config overrides. */
interface ComputerScrollConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `triple_click`'s config overrides. */
interface ComputerTripleClickConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `wait`'s config overrides. */
interface ComputerWaitConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `zoom`'s config overrides. */
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

/** Which sources contribute to the set of URLs web fetch may fetch. Each key is a tagged variant: `user_input` is `all` or `none`; the two tool filters are `all`, `none`, `only` (only the named tools' results) or `except` (every result but the named tools'). A named tool must be declared in this request's `tools[]`. */
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

/** Per-member configuration for `browser_toolset_20260801`: one optional field per member tool, keyed by the member name — the same name the member's `tool_use` blocks carry. Every member is an accepted key, and a member's defaults apply wherever its key is absent. Unknown keys are rejected: the field set is this toolset version's complete member set. */
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

/** `type`'s config overrides. */
interface BrowserTypeConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `close_tab`'s config overrides. */
interface BrowserCloseTabConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `double_click`'s config overrides. */
interface BrowserDoubleClickConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `file_upload`'s config overrides. */
interface BrowserFileUploadConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `find`'s config overrides. */
interface BrowserFindConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `form_input`'s config overrides. */
interface BrowserFormInputConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `get_page_text`'s config overrides. */
interface BrowserGetPageTextConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `hold_key`'s config overrides. */
interface BrowserHoldKeyConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `hover`'s config overrides. */
interface BrowserHoverConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `javascript_exec`'s config overrides. */
interface BrowserJavascriptExecConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `key`'s config overrides. */
interface BrowserKeyConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `left_click`'s config overrides. */
interface BrowserLeftClickConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `left_click_drag`'s config overrides. */
interface BrowserLeftClickDragConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `left_mouse_down`'s config overrides. */
interface BrowserLeftMouseDownConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `left_mouse_up`'s config overrides. */
interface BrowserLeftMouseUpConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `list_tabs`'s config overrides. */
interface BrowserListTabsConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `middle_click`'s config overrides. */
interface BrowserMiddleClickConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `mouse_move`'s config overrides. */
interface BrowserMouseMoveConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `navigate`'s config overrides. */
interface BrowserNavigateConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `new_tab`'s config overrides. */
interface BrowserNewTabConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `read_console`'s config overrides. */
interface BrowserReadConsoleConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `read_network`'s config overrides. */
interface BrowserReadNetworkConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `read_page`'s config overrides. */
interface BrowserReadPageConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `right_click`'s config overrides. */
interface BrowserRightClickConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `screenshot`'s config overrides. */
interface BrowserScreenshotConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `scroll`'s config overrides. */
interface BrowserScrollConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `scroll_to`'s config overrides. */
interface BrowserScrollToConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `switch_tab`'s config overrides. */
interface BrowserSwitchTabConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `triple_click`'s config overrides. */
interface BrowserTripleClickConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `wait`'s config overrides. */
interface BrowserWaitConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `zoom`'s config overrides. */
interface BrowserZoomConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}
```

## Count tokens in a Message

- Signature: `client.messages.countTokens(params: MessageCountTokensParams, options?: RequestOptions): MessageTokensCount`
- Endpoint: `POST /v1/messages/count_tokens`

Count the number of tokens in a Message.

The Token Count API can be used to count the number of tokens in a Message, including tools, images, and documents, without creating it.

Learn more about token counting in our [user guide](https://platform.claude.com/docs/en/build-with-claude/token-counting?sdk_languages=typescript)

### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const messageTokensCount = await client.messages.countTokens({
  messages: [{ content: "Hello, world", role: "user" }],
  model: "claude-opus-5-5"
});

console.log(messageTokensCount.input_tokens);
```

### Example response (200)

```json
{
  "input_tokens": 2095
}
```

### Parameters

````ts
interface MessageCountTokensParams {
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
  /** Configuration options for the model's output, such as the output format. */
  output_config?: OutputConfig;
  /** The inference speed mode for this request. `"fast"` enables high output-tokens-per-second inference. Some models require the `fast-mode-2026-02-01` beta header for any `speed` value. See [fast mode](https://platform.claude.com/docs/en/build-with-claude/fast-mode?sdk_languages=typescript) for which models. */
  speed?: "standard" | "fast" | null;
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
  tools?: Array<MessageCountTokensTool>;
  /** The user profile ID to attribute this request to. Use when acting on behalf of a party other than your organization. */
  user_profile_id?: string; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
````

### Returns

```ts
interface MessageTokensCount {
  /** The total number of tokens across the provided list of messages, system prompt, and tools. */
  input_tokens: number;
}
```

### Errors

Any method can also return the general [HTTP errors](https://platform.claude.com/docs/en/api/errors?sdk_languages=typescript).

- `AvailableToolsLimitExceededError` (HTTP status 400, error code `available_tools_limit_exceeded`)

  The tools available after a message exceed a limit on their number or their size.

- `ClaudeCodeKeyCreatorNotMemberError` (HTTP status 400, error code `claude_code_key_creator_not_member`)

  The API key belongs to the Claude Code workspace, and the user who created it is no longer a member of the organization or of that workspace.

- `CompactionBlockAmbiguousError` (HTTP status 400, error code `compaction_block_ambiguous`)

  `messages` holds more than one `compaction` block with content. Send only the block the conversation returned last.

- `CompactionBlockMisplacedError` (HTTP status 400, error code `compaction_block_misplaced`)

  The `compaction` block is not the first block of the conversation, or is in a `system` message.

- `CompactionContentMismatchError` (HTTP status 400, error code `compaction_content_mismatch`)

  The `compaction` block's `content` differs from the text its `signature` recorded.

- `CompactionNothingToSummarizeError` (HTTP status 400, error code `compaction_nothing_to_summarize`)

  `messages` holds no `user` or `assistant` content to summarize or adopt.

- `CompactionSignatureInvalidError` (HTTP status 400, error code `compaction_signature_invalid`)

  The `compaction` block's `signature` does not verify.

- `CompactionToolChangesMismatchError` (HTTP status 400, error code `compaction_tool_changes_mismatch`)

  The `compaction` block's `tool_changes` differs from what was returned with the block.

- `OrganizationOnHoldError` (HTTP status 400, error code `organization_on_hold`)

  Anthropic has disabled the organization for trust and safety reasons. An organization disabled for any other reason, such as billing, does not get this code. `appeal_url`, when present, is where the organization can appeal.

- `RequestBodyEncodingInvalidError` (HTTP status 400, error code `request_body_encoding_invalid`)

  The request body is not valid for its `Content-Encoding`.

- `RequestBodyEncodingUnsupportedError` (HTTP status 400, error code `request_body_encoding_unsupported`)

  The request's `Content-Encoding` is not supported.

- `ToolNameConflictError` (HTTP status 400, error code `tool_name_conflict`)

  A tool made available in `messages` takes a name that an available tool of another kind, or of another MCP server, already holds.

- `ToolReferenceUnresolvedError` (HTTP status 400, error code `tool_reference_unresolved`)

  A tool change or MCP tool listing references a tool or MCP server that is not defined at that position in the conversation.

- `RequestBodyTooLargeAfterDecodingError` (HTTP status 413, error code `request_body_too_large_after_decoding`)

  The compressed request body exceeds the request size limit once decoded.

- `EnforcedSpendLimitReachedError` (HTTP status 429, error code `enforced_spend_limit_reached`)

  The organization has crossed the monthly API usage threshold of its API tier.

- `CompactionUnavailableError` (HTTP status 529, error code `compaction_unavailable`)

  The compaction could not be completed for a transient server reason. Retry the request.

### Types

```ts
type MessageCountTokensTool = Tool | ToolBash20250124 | CodeExecutionTool20250522 | CodeExecutionTool20250825 | CodeExecutionTool20260120 | CodeExecutionTool20260521 | BrowserToolset20260801 | MemoryTool20250818 | ComputerToolset20260801 | ToolTextEditor20250124 | ToolTextEditor20250429 | ToolTextEditor20250728 | WebSearchTool20250305 | WebFetchTool20250910 | WebSearchTool20260209 | WebFetchTool20260209 | WebFetchTool20260309 | WebSearchTool20260318 | WebFetchTool20260318 | ToolSearchToolBm25_20251119 | ToolSearchToolRegex20251119;
```

## Errors

### AvailableToolsLimitExceededError

HTTP status 400, error code `available_tools_limit_exceeded`

- `class AvailableToolsLimitExceededError extends BadRequestError`

  The tools available after a message exceed a limit on their number or their size.

  - `errorCode: "available_tools_limit_exceeded"`

  - `details: AvailableToolsLimitExceededErrorDetails`

    - `error_code: "available_tools_limit_exceeded"`

### CompactionBlockAmbiguousError

HTTP status 400, error code `compaction_block_ambiguous`

- `class CompactionBlockAmbiguousError extends BadRequestError`

  `messages` holds more than one `compaction` block with content. Send only the block the conversation returned last.

  - `errorCode: "compaction_block_ambiguous"`

  - `details: CompactionBlockAmbiguousErrorDetails`

    - `error_code: "compaction_block_ambiguous"`

### CompactionBlockMisplacedError

HTTP status 400, error code `compaction_block_misplaced`

- `class CompactionBlockMisplacedError extends BadRequestError`

  The `compaction` block is not the first block of the conversation, or is in a `system` message.

  - `errorCode: "compaction_block_misplaced"`

  - `details: CompactionBlockMisplacedErrorDetails`

    - `error_code: "compaction_block_misplaced"`

### CompactionContentMismatchError

HTTP status 400, error code `compaction_content_mismatch`

- `class CompactionContentMismatchError extends BadRequestError`

  The `compaction` block's `content` differs from the text its `signature` recorded.

  - `errorCode: "compaction_content_mismatch"`

  - `details: CompactionContentMismatchErrorDetails`

    - `error_code: "compaction_content_mismatch"`

### CompactionIncompleteTurnError

HTTP status 400, error code `compaction_incomplete_turn`

- `class CompactionIncompleteTurnError extends BadRequestError`

  The compaction request ends on an `assistant` turn that is not finished.

  - `errorCode: "compaction_incomplete_turn"`

  - `details: CompactionIncompleteTurnErrorDetails`

    - `error_code: "compaction_incomplete_turn"`

### CompactionNothingToSummarizeError

HTTP status 400, error code `compaction_nothing_to_summarize`

- `class CompactionNothingToSummarizeError extends BadRequestError`

  `messages` holds no `user` or `assistant` content to summarize or adopt.

  - `errorCode: "compaction_nothing_to_summarize"`

  - `details: CompactionNothingToSummarizeErrorDetails`

    - `error_code: "compaction_nothing_to_summarize"`

### CompactionSignatureInvalidError

HTTP status 400, error code `compaction_signature_invalid`

- `class CompactionSignatureInvalidError extends BadRequestError`

  The `compaction` block's `signature` does not verify.

  - `errorCode: "compaction_signature_invalid"`

  - `details: CompactionSignatureInvalidErrorDetails`

    - `error_code: "compaction_signature_invalid"`

### CompactionTooManyToolReferencesError

HTTP status 400, error code `compaction_too_many_tool_references`

- `class CompactionTooManyToolReferencesError extends BadRequestError`

  The conversation references more distinct tools than a `compaction` block can record.

  - `errorCode: "compaction_too_many_tool_references"`

  - `details: CompactionTooManyToolReferencesErrorDetails`

    - `error_code: "compaction_too_many_tool_references"`

### CompactionToolChangesMismatchError

HTTP status 400, error code `compaction_tool_changes_mismatch`

- `class CompactionToolChangesMismatchError extends BadRequestError`

  The `compaction` block's `tool_changes` differs from what was returned with the block.

  - `errorCode: "compaction_tool_changes_mismatch"`

  - `details: CompactionToolChangesMismatchErrorDetails`

    - `error_code: "compaction_tool_changes_mismatch"`

### ThreadAlreadyContinuedError

HTTP status 400, error code `thread_already_continued`

- `class ThreadAlreadyContinuedError extends BadRequestError`

  The response that `previous_message_id` names has already been continued, and each response can be continued only once. Continue from the Thread's most recent response `id`.

  - `errorCode: "thread_already_continued"`

  - `details: ThreadAlreadyContinuedErrorDetails`

    - `error_code: "thread_already_continued"`

### ThreadContinueInFlightError

HTTP status 400, error code `thread_continue_in_flight`

- `class ThreadContinueInFlightError extends BadRequestError`

  Another request is still continuing from the same `previous_message_id`. Wait for it to complete and continue from its response `id`, or replay the full conversation with `thread: {"type": "create"}`.

  - `errorCode: "thread_continue_in_flight"`

  - `details: ThreadContinueInFlightErrorDetails`

    - `error_code: "thread_continue_in_flight"`

### ThreadFingerprintMismatchError

HTTP status 400, error code `thread_fingerprint_mismatch`

- `class ThreadFingerprintMismatchError extends BadRequestError`

  A field that must stay the same across a Thread's turns differs from the value stored with the Thread; the message names each such field. Send the stored values, or replay the full conversation with `thread: {"type": "create"}` to change them.

  - `errorCode: "thread_fingerprint_mismatch"`

  - `details: ThreadFingerprintMismatchErrorDetails`

    - `error_code: "thread_fingerprint_mismatch"`

### ThreadUnsupportedRequestError

HTTP status 400, error code `thread_unsupported_request`

- `class ThreadUnsupportedRequestError extends BadRequestError`

  The request combines `thread` with a request field or an organization setting that Threads do not support; `unsupported`, when present, names it. Send the full conversation without `thread`, or change that field.

  - `errorCode: "thread_unsupported_request"`

  - `details: ThreadUnsupportedRequestErrorDetails`

    - `error_code: "thread_unsupported_request"`

    - `unsupported?: Array<ThreadUnsupportedFeatureName> | null`

      Each entry names a request field or an organization setting that Threads do not support. On a value you do not recognize, send the full conversation without `thread`.

      - `"cache_control"`

      - `"context_management"`

      - `"fallbacks"`

      - `"hipaa"`

      - `"inference_hooks"`

      - `"thinking"`

### ToolNameConflictError

HTTP status 400, error code `tool_name_conflict`

- `class ToolNameConflictError extends BadRequestError`

  A tool made available in `messages` takes a name that an available tool of another kind, or of another MCP server, already holds.

  - `errorCode: "tool_name_conflict"`

  - `details: ToolNameConflictErrorDetails`

    - `error_code: "tool_name_conflict"`

### ToolReferenceUnresolvedError

HTTP status 400, error code `tool_reference_unresolved`

- `class ToolReferenceUnresolvedError extends BadRequestError`

  A tool change or MCP tool listing references a tool or MCP server that is not defined at that position in the conversation.

  - `errorCode: "tool_reference_unresolved"`

  - `details: ToolReferenceUnresolvedErrorDetails`

    - `error_code: "tool_reference_unresolved"`

### ThreadNotFoundError

HTTP status 404, error code `thread_not_found`

- `class ThreadNotFoundError extends NotFoundError`

  No usable Thread state was found for `previous_message_id`. Replay the full conversation with `thread: {"type": "create"}` to start a new Thread.

  - `errorCode: "thread_not_found"`

  - `details: ThreadNotFoundErrorDetails`

    - `error_code: "thread_not_found"`

### CompactionUnavailableError

HTTP status 529, error code `compaction_unavailable`

- `class CompactionUnavailableError extends OverloadedError`

  The compaction could not be completed for a transient server reason. Retry the request.

  - `errorCode: "compaction_unavailable"`

  - `details: CompactionUnavailableErrorDetails`

    - `error_code: "compaction_unavailable"`

## Messages › Batches

### Create a Message Batch

- Signature: `client.messages.batches.create(params: BatchCreateParams, options?: RequestOptions): MessageBatch`
- Endpoint: `POST /v1/messages/batches`

Send a batch of Message creation requests.

The Message Batches API can be used to process multiple Messages API requests at once. Once a Message Batch is created, it begins processing immediately. Batches can take up to 24 hours to complete.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing?sdk_languages=typescript)

#### Example request

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

#### Example response (200)

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

#### Parameters

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

#### Returns

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

#### Errors

Any method can also return the general [HTTP errors](https://platform.claude.com/docs/en/api/errors?sdk_languages=typescript).

- `ClaudeCodeKeyCreatorNotMemberError` (HTTP status 400, error code `claude_code_key_creator_not_member`)

  The API key belongs to the Claude Code workspace, and the user who created it is no longer a member of the organization or of that workspace.

- `CMEKKeyDisabledError` (HTTP status 400, error code `cmek_key_disabled`)

  The workspace's customer-managed encryption key is disabled or revoked. Re-enable the key, then retry.

- `OrganizationOnHoldError` (HTTP status 400, error code `organization_on_hold`)

  Anthropic has disabled the organization for trust and safety reasons. An organization disabled for any other reason, such as billing, does not get this code. `appeal_url`, when present, is where the organization can appeal.

- `EnforcedSpendLimitReachedError` (HTTP status 429, error code `enforced_spend_limit_reached`)

  The organization has crossed the monthly API usage threshold of its API tier.

#### Types

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
````

### Retrieve a Message Batch

- Signature: `client.messages.batches.retrieve(messageBatchID: string, params?: BatchRetrieveParams, options?: RequestOptions): MessageBatch`
- Endpoint: `GET /v1/messages/batches/{message_batch_id}`

This endpoint is idempotent and can be used to poll for Message Batch completion. To access the results of a Message Batch, make a request to the `results_url` field in the response.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing?sdk_languages=typescript)

#### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const messageBatch = await client.messages.batches.retrieve("message_batch_id");

console.log(messageBatch.id);
```

#### Example response (200)

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

#### Parameters

```ts
/** ID of the Message Batch. */
messageBatchID: string; // path parameter

interface BatchRetrieveParams {
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

#### Errors

Any method can also return the general [HTTP errors](https://platform.claude.com/docs/en/api/errors?sdk_languages=typescript).

- `ClaudeCodeKeyCreatorNotMemberError` (HTTP status 400, error code `claude_code_key_creator_not_member`)

  The API key belongs to the Claude Code workspace, and the user who created it is no longer a member of the organization or of that workspace.

- `OrganizationOnHoldError` (HTTP status 400, error code `organization_on_hold`)

  Anthropic has disabled the organization for trust and safety reasons. An organization disabled for any other reason, such as billing, does not get this code. `appeal_url`, when present, is where the organization can appeal.

### List Message Batches

- Signature: `client.messages.batches.list(params?: BatchListParams, options?: RequestOptions): Page<MessageBatch>`
- Endpoint: `GET /v1/messages/batches`

List all Message Batches within a Workspace. Most recently created batches are returned first.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing?sdk_languages=typescript)

#### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const messageBatch of client.messages.batches.list()) {
  console.log(messageBatch.id);
}
```

#### Example response (200)

```json
{
  "data": [
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
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

#### Parameters

```ts
interface BatchListParams {
  /** ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object. */
  after_id?: string; // query parameter
  /** ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object. */
  before_id?: string; // query parameter
  /** Number of items to return per page. Defaults to `20`. Ranges from `1` to `1000`. */
  limit?: number; // query parameter, minimum: 1, maximum: 1000
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

#### Errors

Any method can also return the general [HTTP errors](https://platform.claude.com/docs/en/api/errors?sdk_languages=typescript).

- `ClaudeCodeKeyCreatorNotMemberError` (HTTP status 400, error code `claude_code_key_creator_not_member`)

  The API key belongs to the Claude Code workspace, and the user who created it is no longer a member of the organization or of that workspace.

- `OrganizationOnHoldError` (HTTP status 400, error code `organization_on_hold`)

  Anthropic has disabled the organization for trust and safety reasons. An organization disabled for any other reason, such as billing, does not get this code. `appeal_url`, when present, is where the organization can appeal.

### Cancel a Message Batch

- Signature: `client.messages.batches.cancel(messageBatchID: string, params?: BatchCancelParams, options?: RequestOptions): MessageBatch`
- Endpoint: `POST /v1/messages/batches/{message_batch_id}/cancel`

Batches may be canceled any time before processing ends. Once cancellation is initiated, the batch enters a `canceling` state, at which time the system may complete any in-progress, non-interruptible requests before finalizing cancellation.

The number of canceled requests is specified in `request_counts`. To determine which requests were canceled, check the individual results within the batch. Note that cancellation may not result in any canceled requests if they were non-interruptible.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing?sdk_languages=typescript)

#### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const messageBatch = await client.messages.batches.cancel("message_batch_id");

console.log(messageBatch.id);
```

#### Example response (200)

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

#### Parameters

```ts
/** ID of the Message Batch. */
messageBatchID: string; // path parameter

interface BatchCancelParams {
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

#### Errors

Any method can also return the general [HTTP errors](https://platform.claude.com/docs/en/api/errors?sdk_languages=typescript).

- `ClaudeCodeKeyCreatorNotMemberError` (HTTP status 400, error code `claude_code_key_creator_not_member`)

  The API key belongs to the Claude Code workspace, and the user who created it is no longer a member of the organization or of that workspace.

- `OrganizationOnHoldError` (HTTP status 400, error code `organization_on_hold`)

  Anthropic has disabled the organization for trust and safety reasons. An organization disabled for any other reason, such as billing, does not get this code. `appeal_url`, when present, is where the organization can appeal.

### Delete a Message Batch

- Signature: `client.messages.batches.delete(messageBatchID: string, params?: BatchDeleteParams, options?: RequestOptions): DeletedMessageBatch`
- Endpoint: `DELETE /v1/messages/batches/{message_batch_id}`

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing?sdk_languages=typescript)

#### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const deletedMessageBatch = await client.messages.batches.delete("message_batch_id");

console.log(deletedMessageBatch.id);
```

#### Example response (200)

```json
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "type": "message_batch_deleted"
}
```

#### Parameters

```ts
/** ID of the Message Batch. */
messageBatchID: string; // path parameter

interface BatchDeleteParams {
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

#### Returns

```ts
interface DeletedMessageBatch {
  /** Deleted object type. For Message Batches, this is always `"message_batch_deleted"`. */
  type: "message_batch_deleted";
  /** ID of the Message Batch. */
  id: string;
}
```

#### Errors

Any method can also return the general [HTTP errors](https://platform.claude.com/docs/en/api/errors?sdk_languages=typescript).

- `ClaudeCodeKeyCreatorNotMemberError` (HTTP status 400, error code `claude_code_key_creator_not_member`)

  The API key belongs to the Claude Code workspace, and the user who created it is no longer a member of the organization or of that workspace.

- `OrganizationOnHoldError` (HTTP status 400, error code `organization_on_hold`)

  Anthropic has disabled the organization for trust and safety reasons. An organization disabled for any other reason, such as billing, does not get this code. `appeal_url`, when present, is where the organization can appeal.

### Retrieve Message Batch results

- Signature: `client.messages.batches.results(messageBatchID: string, params?: BatchResultsParams, options?: RequestOptions): JSONLDecoder<MessageBatchIndividualResponse>`
- Endpoint: `GET /v1/messages/batches/{message_batch_id}/results`

Streams the results of a Message Batch as a `.jsonl` file.

Each line in the file is a JSON object containing the result of a single request in the Message Batch. Results are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing?sdk_languages=typescript)

#### Example request

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

#### Parameters

```ts
/** ID of the Message Batch. */
messageBatchID: string; // path parameter

interface BatchResultsParams {
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

#### Returns

```ts
/** This is a single line in the response `.jsonl` file and does not represent the response as a whole. */
interface MessageBatchIndividualResponse {
  /** Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order. Must be unique for each request within the Message Batch. */
  custom_id: string;
  /** Processing result for this request. Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration. */
  result: MessageBatchResult;
}
```

#### Errors

Any method can also return the general [HTTP errors](https://platform.claude.com/docs/en/api/errors?sdk_languages=typescript).

- `ClaudeCodeKeyCreatorNotMemberError` (HTTP status 400, error code `claude_code_key_creator_not_member`)

  The API key belongs to the Claude Code workspace, and the user who created it is no longer a member of the organization or of that workspace.

- `CMEKKeyDisabledError` (HTTP status 400, error code `cmek_key_disabled`)

  The workspace's customer-managed encryption key is disabled or revoked. Re-enable the key, then retry.

- `OrganizationOnHoldError` (HTTP status 400, error code `organization_on_hold`)

  Anthropic has disabled the organization for trust and safety reasons. An organization disabled for any other reason, such as billing, does not get this code. `appeal_url`, when present, is where the organization can appeal.

#### Types

```ts
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
```

## Types

```ts
/** The tools available after a message exceed a limit on their number or their size. */
interface AvailableToolsLimitExceededErrorDetails {
  error_code: "available_tools_limit_exceeded";
}

/** Where to act: either a viewport coordinate or an element reference. */
type BrowserClickTarget = BrowserCoordinateTarget | BrowserRefTarget;

/** Close the tab with the given tab_id. */
interface BrowserCloseTabInput {
  /** The tab to close. */
  tab_id: string;
}

interface BrowserCloseTabToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Close the tab with the given tab_id. */
  input: BrowserCloseTabInput;
  name: "close_tab";
  toolset_name: "browser";
}

/** A point in the browser viewport, in viewport pixels (the same frame as a full-viewport screenshot). */
interface BrowserCoordinateTarget {
  type: "coordinate";
  /** Pixels from the left edge of the viewport. */
  x: number; // minimum: 0
  /** Pixels from the top edge of the viewport. */
  y: number; // minimum: 0
}

/** Double left-click at a viewport coordinate or on an element by reference. */
interface BrowserDoubleClickInput {
  /** Where to act: either a viewport coordinate or an element reference. */
  target: BrowserClickTarget;
  /** Optional modifier key chord to hold for the duration of this action (e.g. "shift", "ctrl+shift", "cmd+alt"). */
  modifiers?: string | null;
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BrowserDoubleClickToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Double left-click at a viewport coordinate or on an element by reference. */
  input: BrowserDoubleClickInput;
  name: "double_click";
  toolset_name: "browser";
}

/** Set the value of a file-input element to one or more files. The target must be an element reference; at least one of paths or document_ids is required. */
interface BrowserFileUploadInput {
  /** An element on the page, identified by a reference from a prior `read_page` or `find` result. References are scoped to the tab that produced them and become stale after navigation or a major re-render. */
  target: BrowserRefTarget;
  /** References to files the harness has staged, for deployments where the browser executor cannot read the caller's filesystem. */
  document_ids?: Array<string> | null; // minItems: 1
  /** File paths on the browser executor's filesystem. */
  paths?: Array<string> | null; // minItems: 1
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BrowserFileUploadToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Set the value of a file-input element to one or more files. The target must be an element reference; at least one of paths or document_ids is required. */
  input: BrowserFileUploadInput;
  name: "file_upload";
  toolset_name: "browser";
}

/** Find elements matching a natural-language description (e.g. "search bar", "add to cart button") and return up to 20 matches with element references. */
interface BrowserFindInput {
  /** Natural-language description of the element(s) to find. */
  query: string;
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BrowserFindToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Find elements matching a natural-language description (e.g. "search bar", "add to cart button") and return up to 20 matches with element references. */
  input: BrowserFindInput;
  name: "find";
  toolset_name: "browser";
}

/** Set the value of a form element (input, textarea, select, checkbox). Use a boolean for checkboxes, an option value or text for selects. */
interface BrowserFormInputInput {
  /** An element on the page, identified by a reference from a prior `read_page` or `find` result. References are scoped to the tab that produced them and become stale after navigation or a major re-render. */
  target: BrowserRefTarget;
  /** The value to set. */
  value: BrowserFormInputValue;
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BrowserFormInputToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Set the value of a form element (input, textarea, select, checkbox). Use a boolean for checkboxes, an option value or text for selects. */
  input: BrowserFormInputInput;
  name: "form_input";
  toolset_name: "browser";
}

type BrowserFormInputValue = string | number | boolean;

/** Return the page's visible text content as plain text, prioritizing article content. Suited to articles, documentation, and other text-heavy pages. */
interface BrowserGetPageTextInput {
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BrowserGetPageTextToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Return the page's visible text content as plain text, prioritizing article content. Suited to articles, documentation, and other text-heavy pages. */
  input: BrowserGetPageTextInput;
  name: "get_page_text";
  toolset_name: "browser";
}

/** Hold a key or key chord down for a duration, then release it. Uses the same key names and "+" chord syntax as the key action. */
interface BrowserHoldKeyInput {
  /** Seconds to hold the key down (maximum 30). */
  duration: number; // minimum: 0, maximum: 30
  /** The key or chord to hold. */
  text: string;
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BrowserHoldKeyToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Hold a key or key chord down for a duration, then release it. Uses the same key names and "+" chord syntax as the key action. */
  input: BrowserHoldKeyInput;
  name: "hold_key";
  toolset_name: "browser";
}

/** Move the cursor to a coordinate or element without clicking. */
interface BrowserHoverInput {
  /** Where to act: either a viewport coordinate or an element reference. */
  target: BrowserClickTarget;
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BrowserHoverToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Move the cursor to a coordinate or element without clicking. */
  input: BrowserHoverInput;
  name: "hover";
  toolset_name: "browser";
}

/** Execute JavaScript in the page context and return the value of the last expression. The code runs with access to the DOM, `window`, and page variables. Write the expression you want evaluated — do NOT use `return`. */
interface BrowserJavascriptExecInput {
  /** JavaScript to execute in the page context. */
  text: string;
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BrowserJavascriptExecToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Execute JavaScript in the page context and return the value of the last expression. The code runs with access to the DOM, `window`, and page variables. Write the expression you want evaluated — do NOT use `return`. */
  input: BrowserJavascriptExecInput;
  name: "javascript_exec";
  toolset_name: "browser";
}

/** Press a key or key chord. Use "+" to combine modifiers with a key (e.g. "ctrl+a", "cmd+shift+p") and space to sequence presses (e.g. "Backspace Backspace Delete"). Common names like "Return", "Tab", "Escape", "BackSpace" are supported. */
interface BrowserKeyInput {
  /** The key, chord, or space-separated sequence to press. */
  text: string;
  /** Number of times to repeat. Default 1. */
  repeat?: number | null; // minimum: 1, maximum: 100
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BrowserKeyToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Press a key or key chord. Use "+" to combine modifiers with a key (e.g. "ctrl+a", "cmd+shift+p") and space to sequence presses (e.g. "Backspace Backspace Delete"). Common names like "Return", "Tab", "Escape", "BackSpace" are supported. */
  input: BrowserKeyInput;
  name: "key";
  toolset_name: "browser";
}

/** Press at `from`, drag to `target`, release. Both must be coordinate targets. */
interface BrowserLeftClickDragInput {
  /** A point in the browser viewport, in viewport pixels (the same frame as a full-viewport screenshot). */
  from: BrowserCoordinateTarget;
  /** A point in the browser viewport, in viewport pixels (the same frame as a full-viewport screenshot). */
  target: BrowserCoordinateTarget;
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BrowserLeftClickDragToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Press at `from`, drag to `target`, release. Both must be coordinate targets. */
  input: BrowserLeftClickDragInput;
  name: "left_click_drag";
  toolset_name: "browser";
}

/** Left-click at a viewport coordinate or on an element by reference. */
interface BrowserLeftClickInput {
  /** Where to act: either a viewport coordinate or an element reference. */
  target: BrowserClickTarget;
  /** Optional modifier key chord to hold for the duration of this action (e.g. "shift", "ctrl+shift", "cmd+alt"). */
  modifiers?: string | null;
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BrowserLeftClickToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Left-click at a viewport coordinate or on an element by reference. */
  input: BrowserLeftClickInput;
  name: "left_click";
  toolset_name: "browser";
}

/** Press and hold the left mouse button at a viewport coordinate. Pair with left_mouse_up to perform a custom drag. */
interface BrowserLeftMouseDownInput {
  /** A point in the browser viewport, in viewport pixels (the same frame as a full-viewport screenshot). */
  target: BrowserCoordinateTarget;
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BrowserLeftMouseDownToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Press and hold the left mouse button at a viewport coordinate. Pair with left_mouse_up to perform a custom drag. */
  input: BrowserLeftMouseDownInput;
  name: "left_mouse_down";
  toolset_name: "browser";
}

/** Release the left mouse button at a viewport coordinate. */
interface BrowserLeftMouseUpInput {
  /** A point in the browser viewport, in viewport pixels (the same frame as a full-viewport screenshot). */
  target: BrowserCoordinateTarget;
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BrowserLeftMouseUpToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Release the left mouse button at a viewport coordinate. */
  input: BrowserLeftMouseUpInput;
  name: "left_mouse_up";
  toolset_name: "browser";
}

/** List all open tabs with each tab's tab_id, title, and URL. */
interface BrowserListTabsInput {}

interface BrowserListTabsToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** List all open tabs with each tab's tab_id, title, and URL. */
  input: BrowserListTabsInput;
  name: "list_tabs";
  toolset_name: "browser";
}

/** Middle-click at a viewport coordinate or on an element by reference. */
interface BrowserMiddleClickInput {
  /** Where to act: either a viewport coordinate or an element reference. */
  target: BrowserClickTarget;
  /** Optional modifier key chord to hold for the duration of this action (e.g. "shift", "ctrl+shift", "cmd+alt"). */
  modifiers?: string | null;
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BrowserMiddleClickToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Middle-click at a viewport coordinate or on an element by reference. */
  input: BrowserMiddleClickInput;
  name: "middle_click";
  toolset_name: "browser";
}

/** Move the pointer to a viewport coordinate without clicking. */
interface BrowserMouseMoveInput {
  /** A point in the browser viewport, in viewport pixels (the same frame as a full-viewport screenshot). */
  target: BrowserCoordinateTarget;
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BrowserMouseMoveToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Move the pointer to a viewport coordinate without clicking. */
  input: BrowserMouseMoveInput;
  name: "mouse_move";
  toolset_name: "browser";
}

/** Navigate to a URL, or go back/forward/reload in history. The protocol may be omitted (defaults to https://). */
interface BrowserNavigateInput {
  /** The URL to navigate to, or "back" / "forward" / "reload" for history navigation. */
  url: string;
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BrowserNavigateToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Navigate to a URL, or go back/forward/reload in history. The protocol may be omitted (defaults to https://). */
  input: BrowserNavigateInput;
  name: "navigate";
  toolset_name: "browser";
}

/** Open a new empty tab and return its tab_id. */
interface BrowserNewTabInput {}

interface BrowserNewTabToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Open a new empty tab and return its tab_id. */
  input: BrowserNewTabInput;
  name: "new_tab";
  toolset_name: "browser";
}

/** Return console output (log entries, errors, warnings) accumulated since the driver attached to the tab and since the last read, one line per entry. An empty result does not mean no traffic for a tab that predates attach. */
interface BrowserReadConsoleInput {
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BrowserReadConsoleToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Return console output (log entries, errors, warnings) accumulated since the driver attached to the tab and since the last read, one line per entry. An empty result does not mean no traffic for a tab that predates attach. */
  input: BrowserReadConsoleInput;
  name: "read_console";
  toolset_name: "browser";
}

/** Return the network requests (method, URL, status, MIME type, timing) recorded since the driver attached to the tab and since the last read, one line per entry. An empty result does not mean no traffic for a tab that predates attach. */
interface BrowserReadNetworkInput {
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BrowserReadNetworkToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Return the network requests (method, URL, status, MIME type, timing) recorded since the driver attached to the tab and since the last read, one line per entry. An empty result does not mean no traffic for a tab that predates attach. */
  input: BrowserReadNetworkInput;
  name: "read_network";
  toolset_name: "browser";
}

type BrowserReadPageFilter = "all" | "interactive";

/** Return a structured accessibility tree of the page (or the subtree rooted at `ref`), with element references like [ref_7] that can be used as targets on later actions. Output is capped at 50,000 characters — narrow with `ref` or a smaller `depth` when exceeded. */
interface BrowserReadPageInput {
  /** Maximum tree depth. Default 15. */
  depth?: number | null; // minimum: 1
  /** Which elements to include. Omitted: every visible element. "interactive": interactive elements only. "all": additionally includes off-viewport elements. */
  filter?: BrowserReadPageFilter | null;
  /** Element reference to read a subtree from. Omit to read from the page root. */
  ref?: string | null;
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BrowserReadPageToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Return a structured accessibility tree of the page (or the subtree rooted at `ref`), with element references like [ref_7] that can be used as targets on later actions. Output is capped at 50,000 characters — narrow with `ref` or a smaller `depth` when exceeded. */
  input: BrowserReadPageInput;
  name: "read_page";
  toolset_name: "browser";
}

/** An element on the page, identified by a reference from a prior `read_page` or `find` result. References are scoped to the tab that produced them and become stale after navigation or a major re-render. */
interface BrowserRefTarget {
  type: "ref";
  /** An element reference (e.g. "ref_7") returned by a prior `read_page` or `find` result. */
  ref: string;
}

/** Right-click at a viewport coordinate or on an element by reference. */
interface BrowserRightClickInput {
  /** Where to act: either a viewport coordinate or an element reference. */
  target: BrowserClickTarget;
  /** Optional modifier key chord to hold for the duration of this action (e.g. "shift", "ctrl+shift", "cmd+alt"). */
  modifiers?: string | null;
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BrowserRightClickToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Right-click at a viewport coordinate or on an element by reference. */
  input: BrowserRightClickInput;
  name: "right_click";
  toolset_name: "browser";
}

/** Capture the current browser viewport. */
interface BrowserScreenshotInput {
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BrowserScreenshotToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Capture the current browser viewport. */
  input: BrowserScreenshotInput;
  name: "screenshot";
  toolset_name: "browser";
}

type BrowserScrollDirection = "up" | "down" | "left" | "right";

/** Scroll at a viewport position. `target` must be a coordinate target. */
interface BrowserScrollInput {
  scroll_direction: BrowserScrollDirection;
  /** A point in the browser viewport, in viewport pixels (the same frame as a full-viewport screenshot). */
  target: BrowserCoordinateTarget;
  /** Scroll-wheel notches (1–10). Default 3. */
  scroll_amount?: number | null; // minimum: 1, maximum: 10
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

/** Scroll an element into view. */
interface BrowserScrollToInput {
  /** An element on the page, identified by a reference from a prior `read_page` or `find` result. References are scoped to the tab that produced them and become stale after navigation or a major re-render. */
  target: BrowserRefTarget;
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BrowserScrollToToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Scroll an element into view. */
  input: BrowserScrollToInput;
  name: "scroll_to";
  toolset_name: "browser";
}

interface BrowserScrollToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Scroll at a viewport position. `target` must be a coordinate target. */
  input: BrowserScrollInput;
  name: "scroll";
  toolset_name: "browser";
}

/** Make the tab with the given tab_id the active tab — the tab that actions without a tab_id apply to. */
interface BrowserSwitchTabInput {
  /** The tab to switch to. */
  tab_id: string;
}

interface BrowserSwitchTabToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Make the tab with the given tab_id the active tab — the tab that actions without a tab_id apply to. */
  input: BrowserSwitchTabInput;
  name: "switch_tab";
  toolset_name: "browser";
}

type BrowserToolUseBlock = BrowserNavigateToolUseBlock | BrowserListTabsToolUseBlock | BrowserNewTabToolUseBlock | BrowserSwitchTabToolUseBlock | BrowserCloseTabToolUseBlock | BrowserReadPageToolUseBlock | BrowserGetPageTextToolUseBlock | BrowserReadConsoleToolUseBlock | BrowserReadNetworkToolUseBlock | BrowserFindToolUseBlock | BrowserFormInputToolUseBlock | BrowserFileUploadToolUseBlock | BrowserScrollToToolUseBlock | BrowserScreenshotToolUseBlock | BrowserZoomToolUseBlock | BrowserLeftClickToolUseBlock | BrowserRightClickToolUseBlock | BrowserMiddleClickToolUseBlock | BrowserDoubleClickToolUseBlock | BrowserTripleClickToolUseBlock | BrowserHoverToolUseBlock | BrowserLeftClickDragToolUseBlock | BrowserLeftMouseDownToolUseBlock | BrowserLeftMouseUpToolUseBlock | BrowserMouseMoveToolUseBlock | BrowserScrollToolUseBlock | BrowserTypeToolUseBlock | BrowserKeyToolUseBlock | BrowserHoldKeyToolUseBlock | BrowserWaitToolUseBlock | BrowserJavascriptExecToolUseBlock;

/** Triple left-click at a viewport coordinate or on an element by reference (typically selects a line or paragraph). */
interface BrowserTripleClickInput {
  /** Where to act: either a viewport coordinate or an element reference. */
  target: BrowserClickTarget;
  /** Optional modifier key chord to hold for the duration of this action (e.g. "shift", "ctrl+shift", "cmd+alt"). */
  modifiers?: string | null;
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BrowserTripleClickToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Triple left-click at a viewport coordinate or on an element by reference (typically selects a line or paragraph). */
  input: BrowserTripleClickInput;
  name: "triple_click";
  toolset_name: "browser";
}

/** Type a literal string at the current focus. */
interface BrowserTypeInput {
  /** The text to type. */
  text: string;
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BrowserTypeToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Type a literal string at the current focus. */
  input: BrowserTypeInput;
  name: "type";
  toolset_name: "browser";
}

/** Pause for the given duration. */
interface BrowserWaitInput {
  /** Seconds to wait (maximum 30). */
  duration: number; // minimum: 0, maximum: 30
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BrowserWaitToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Pause for the given duration. */
  input: BrowserWaitInput;
  name: "wait";
  toolset_name: "browser";
}

/** Return a cropped screenshot of the given viewport region, scaled up for closer inspection — useful for small icons, buttons, or text. Coordinates are in the same viewport-pixel space as a full screenshot. */
interface BrowserZoomInput {
  /** [x0, y0, x1, y1] in viewport pixels. */
  region: Array<number>; // minItems: 4, maxItems: 4
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BrowserZoomToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Return a cropped screenshot of the given viewport region, scaled up for closer inspection — useful for small icons, buttons, or text. Coordinates are in the same viewport-pixel space as a full screenshot. */
  input: BrowserZoomInput;
  name: "zoom";
  toolset_name: "browser";
}

/** `messages` holds more than one `compaction` block with content. Send only the block the conversation returned last. */
interface CompactionBlockAmbiguousErrorDetails {
  error_code: "compaction_block_ambiguous";
}

/** The `compaction` block is not the first block of the conversation, or is in a `system` message. */
interface CompactionBlockMisplacedErrorDetails {
  error_code: "compaction_block_misplaced";
}

/** The `compaction` block's `content` differs from the text its `signature` recorded. */
interface CompactionContentMismatchErrorDetails {
  error_code: "compaction_content_mismatch";
}

/** The compaction request ends on an `assistant` turn that is not finished. */
interface CompactionIncompleteTurnErrorDetails {
  error_code: "compaction_incomplete_turn";
}

/** `messages` holds no `user` or `assistant` content to summarize or adopt. */
interface CompactionNothingToSummarizeErrorDetails {
  error_code: "compaction_nothing_to_summarize";
}

/** The `compaction` block's `signature` does not verify. */
interface CompactionSignatureInvalidErrorDetails {
  error_code: "compaction_signature_invalid";
}

/** The conversation references more distinct tools than a `compaction` block can record. */
interface CompactionTooManyToolReferencesErrorDetails {
  error_code: "compaction_too_many_tool_references";
}

/** The `compaction` block's `tool_changes` differs from what was returned with the block. */
interface CompactionToolChangesMismatchErrorDetails {
  error_code: "compaction_tool_changes_mismatch";
}

/** The compaction could not be completed for a transient server reason. Retry the request. */
interface CompactionUnavailableErrorDetails {
  error_code: "compaction_unavailable";
}

/** Get the current (x, y) pixel coordinate of the cursor. */
interface ComputerCursorPositionInput {}

interface ComputerCursorPositionToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Get the current (x, y) pixel coordinate of the cursor. */
  input: ComputerCursorPositionInput;
  name: "cursor_position";
  toolset_name: "computer";
}

/** Double-click the left mouse button at the specified (x, y) pixel coordinate, or the current cursor position if `coordinate` is omitted. */
interface ComputerDoubleClickInput {
  /** (x, y): x pixels from the left edge, y pixels from the top edge. */
  coordinate?: Array<number> | null; // minItems: 2, maxItems: 2
  /** Optional key combination to hold down during this action (e.g. "ctrl", "shift", "ctrl+shift"). */
  text?: string | null;
}

interface ComputerDoubleClickToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Double-click the left mouse button at the specified (x, y) pixel coordinate, or the current cursor position if `coordinate` is omitted. */
  input: ComputerDoubleClickInput;
  name: "double_click";
  toolset_name: "computer";
}

/** Hold down a key or key-combination for a specified duration. Uses the same key syntax as `key`. */
interface ComputerHoldKeyInput {
  /** Duration to hold the key, in seconds. */
  duration: number; // maximum: 300
  /** The key or key-combination to hold. */
  text: string;
}

interface ComputerHoldKeyToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Hold down a key or key-combination for a specified duration. Uses the same key syntax as `key`. */
  input: ComputerHoldKeyInput;
  name: "hold_key";
  toolset_name: "computer";
}

/** Press a key or key-combination on the keyboard. Use "+" to combine modifiers with a key (e.g. "ctrl+s", "alt+Tab", "ctrl+shift+Escape"). Key names are case-insensitive; common names like "Return", "Tab", "Escape", "Up", "Down", "Left", "Right", "Home", "End", "Page_Up", "Page_Down", "Delete", "BackSpace" are supported. */
interface ComputerKeyInput {
  /** The key or key-combination to press. */
  text: string;
  /** Number of times to repeat the key press. Default is 1. */
  repeat?: number | null; // minimum: 1, maximum: 100
}

interface ComputerKeyToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Press a key or key-combination on the keyboard. Use "+" to combine modifiers with a key (e.g. "ctrl+s", "alt+Tab", "ctrl+shift+Escape"). Key names are case-insensitive; common names like "Return", "Tab", "Escape", "Up", "Down", "Left", "Right", "Home", "End", "Page_Up", "Page_Down", "Delete", "BackSpace" are supported. */
  input: ComputerKeyInput;
  name: "key";
  toolset_name: "computer";
}

/** Click and drag the cursor from `start_coordinate` to `coordinate`. */
interface ComputerLeftClickDragInput {
  /** (x, y): x pixels from the left edge, y pixels from the top edge. */
  coordinate: Array<number>; // minItems: 2, maxItems: 2
  /** (x, y): x pixels from the left edge, y pixels from the top edge. */
  start_coordinate: Array<number>; // minItems: 2, maxItems: 2
  /** Optional key combination to hold down during this action (e.g. "ctrl", "shift", "ctrl+shift"). */
  text?: string | null;
}

interface ComputerLeftClickDragToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Click and drag the cursor from `start_coordinate` to `coordinate`. */
  input: ComputerLeftClickDragInput;
  name: "left_click_drag";
  toolset_name: "computer";
}

/** Click the left mouse button at the specified (x, y) pixel coordinate, or the current cursor position if `coordinate` is omitted. */
interface ComputerLeftClickInput {
  /** (x, y): x pixels from the left edge, y pixels from the top edge. */
  coordinate?: Array<number> | null; // minItems: 2, maxItems: 2
  /** Optional key combination to hold down during this action (e.g. "ctrl", "shift", "ctrl+shift"). */
  text?: string | null;
}

interface ComputerLeftClickToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Click the left mouse button at the specified (x, y) pixel coordinate, or the current cursor position if `coordinate` is omitted. */
  input: ComputerLeftClickInput;
  name: "left_click";
  toolset_name: "computer";
}

/** Press and hold the left mouse button at the current cursor position. */
interface ComputerLeftMouseDownInput {}

interface ComputerLeftMouseDownToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Press and hold the left mouse button at the current cursor position. */
  input: ComputerLeftMouseDownInput;
  name: "left_mouse_down";
  toolset_name: "computer";
}

/** Release the left mouse button. */
interface ComputerLeftMouseUpInput {}

interface ComputerLeftMouseUpToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Release the left mouse button. */
  input: ComputerLeftMouseUpInput;
  name: "left_mouse_up";
  toolset_name: "computer";
}

/** Click the middle mouse button at the specified (x, y) pixel coordinate, or the current cursor position if `coordinate` is omitted. */
interface ComputerMiddleClickInput {
  /** (x, y): x pixels from the left edge, y pixels from the top edge. */
  coordinate?: Array<number> | null; // minItems: 2, maxItems: 2
  /** Optional key combination to hold down during this action (e.g. "ctrl", "shift", "ctrl+shift"). */
  text?: string | null;
}

interface ComputerMiddleClickToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Click the middle mouse button at the specified (x, y) pixel coordinate, or the current cursor position if `coordinate` is omitted. */
  input: ComputerMiddleClickInput;
  name: "middle_click";
  toolset_name: "computer";
}

/** Move the cursor to a specified (x, y) pixel coordinate. Use this ONLY to hover without clicking; otherwise use a click action directly. */
interface ComputerMouseMoveInput {
  /** (x, y): x pixels from the left edge, y pixels from the top edge. */
  coordinate: Array<number>; // minItems: 2, maxItems: 2
}

interface ComputerMouseMoveToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Move the cursor to a specified (x, y) pixel coordinate. Use this ONLY to hover without clicking; otherwise use a click action directly. */
  input: ComputerMouseMoveInput;
  name: "mouse_move";
  toolset_name: "computer";
}

/** Click the right mouse button at the specified (x, y) pixel coordinate, or the current cursor position if `coordinate` is omitted. */
interface ComputerRightClickInput {
  /** (x, y): x pixels from the left edge, y pixels from the top edge. */
  coordinate?: Array<number> | null; // minItems: 2, maxItems: 2
  /** Optional key combination to hold down during this action (e.g. "ctrl", "shift", "ctrl+shift"). */
  text?: string | null;
}

interface ComputerRightClickToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Click the right mouse button at the specified (x, y) pixel coordinate, or the current cursor position if `coordinate` is omitted. */
  input: ComputerRightClickInput;
  name: "right_click";
  toolset_name: "computer";
}

/** Take a screenshot of the screen. */
interface ComputerScreenshotInput {}

interface ComputerScreenshotToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Take a screenshot of the screen. */
  input: ComputerScreenshotInput;
  name: "screenshot";
  toolset_name: "computer";
}

type ComputerScrollDirection = "up" | "down" | "left" | "right";

/** Scroll the screen at the specified (x, y) pixel coordinate, or the current cursor position if `coordinate` is omitted. Do NOT use PageUp/PageDown to scroll. */
interface ComputerScrollInput {
  /** Number of 'clicks' of the scroll wheel. */
  scroll_amount: number;
  scroll_direction: ComputerScrollDirection;
  /** (x, y): x pixels from the left edge, y pixels from the top edge. */
  coordinate?: Array<number> | null; // minItems: 2, maxItems: 2
  /** Optional key combination to hold down during this action (e.g. "ctrl", "shift", "ctrl+shift"). */
  text?: string | null;
}

interface ComputerScrollToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Scroll the screen at the specified (x, y) pixel coordinate, or the current cursor position if `coordinate` is omitted. Do NOT use PageUp/PageDown to scroll. */
  input: ComputerScrollInput;
  name: "scroll";
  toolset_name: "computer";
}

type ComputerToolUseBlock = ComputerKeyToolUseBlock | ComputerHoldKeyToolUseBlock | ComputerTypeToolUseBlock | ComputerCursorPositionToolUseBlock | ComputerMouseMoveToolUseBlock | ComputerLeftMouseDownToolUseBlock | ComputerLeftMouseUpToolUseBlock | ComputerLeftClickToolUseBlock | ComputerLeftClickDragToolUseBlock | ComputerRightClickToolUseBlock | ComputerMiddleClickToolUseBlock | ComputerDoubleClickToolUseBlock | ComputerTripleClickToolUseBlock | ComputerScrollToolUseBlock | ComputerWaitToolUseBlock | ComputerScreenshotToolUseBlock | ComputerZoomToolUseBlock;

/** Triple-click the left mouse button at the specified (x, y) pixel coordinate, or the current cursor position if `coordinate` is omitted. */
interface ComputerTripleClickInput {
  /** (x, y): x pixels from the left edge, y pixels from the top edge. */
  coordinate?: Array<number> | null; // minItems: 2, maxItems: 2
  /** Optional key combination to hold down during this action (e.g. "ctrl", "shift", "ctrl+shift"). */
  text?: string | null;
}

interface ComputerTripleClickToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Triple-click the left mouse button at the specified (x, y) pixel coordinate, or the current cursor position if `coordinate` is omitted. */
  input: ComputerTripleClickInput;
  name: "triple_click";
  toolset_name: "computer";
}

/** Type a string of text on the keyboard. */
interface ComputerTypeInput {
  /** The text to type. */
  text: string;
}

interface ComputerTypeToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Type a string of text on the keyboard. */
  input: ComputerTypeInput;
  name: "type";
  toolset_name: "computer";
}

/** Wait for a specified duration. */
interface ComputerWaitInput {
  /** Duration to wait, in seconds. */
  duration: number; // maximum: 300
}

interface ComputerWaitToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Wait for a specified duration. */
  input: ComputerWaitInput;
  name: "wait";
  toolset_name: "computer";
}

/** Take a screenshot of a rectangular region. Region coordinates are in the full-screenshot space (not physical display pixels). The crop is scaled up to fill the image budget so fine details become legible. */
interface ComputerZoomInput {
  /** (x0, y0, x1, y1): The region to capture. */
  region: Array<number>; // minItems: 4, maxItems: 4
}

interface ComputerZoomToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller: ToolUseCaller;
  /** Take a screenshot of a rectangular region. Region coordinates are in the full-screenshot space (not physical display pixels). The crop is scaled up to fill the image budget so fine details become legible. */
  input: ComputerZoomInput;
  name: "zoom";
  toolset_name: "computer";
}

/** The response that `previous_message_id` names has already been continued, and each response can be continued only once. Continue from the Thread's most recent response `id`. */
interface ThreadAlreadyContinuedErrorDetails {
  error_code: "thread_already_continued";
}

/** Another request is still continuing from the same `previous_message_id`. Wait for it to complete and continue from its response `id`, or replay the full conversation with `thread: {"type": "create"}`. */
interface ThreadContinueInFlightErrorDetails {
  error_code: "thread_continue_in_flight";
}

/** A field that must stay the same across a Thread's turns differs from the value stored with the Thread; the message names each such field. Send the stored values, or replay the full conversation with `thread: {"type": "create"}` to change them. */
interface ThreadFingerprintMismatchErrorDetails {
  error_code: "thread_fingerprint_mismatch";
}

/** No usable Thread state was found for `previous_message_id`. Replay the full conversation with `thread: {"type": "create"}` to start a new Thread. */
interface ThreadNotFoundErrorDetails {
  error_code: "thread_not_found";
}

type ThreadUnsupportedFeatureName = "cache_control" | "context_management" | "fallbacks" | "hipaa" | "inference_hooks" | "thinking";

/** The request combines `thread` with a request field or an organization setting that Threads do not support; `unsupported`, when present, names it. Send the full conversation without `thread`, or change that field. */
interface ThreadUnsupportedRequestErrorDetails {
  error_code: "thread_unsupported_request";
  /** Each entry names a request field or an organization setting that Threads do not support. On a value you do not recognize, send the full conversation without `thread`. */
  unsupported?: Array<ThreadUnsupportedFeatureName> | null;
}

/** A tool made available in `messages` takes a name that an available tool of another kind, or of another MCP server, already holds. */
interface ToolNameConflictErrorDetails {
  error_code: "tool_name_conflict";
}

/** A tool change or MCP tool listing references a tool or MCP server that is not defined at that position in the conversation. */
interface ToolReferenceUnresolvedErrorDetails {
  error_code: "tool_reference_unresolved";
}

/** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
type ToolUseCaller = DirectCaller | ServerToolCaller | ServerToolCaller20260120;

type ToolsetToolUseBlock = BrowserToolUseBlock | ComputerToolUseBlock | ToolUseBlock;
```
