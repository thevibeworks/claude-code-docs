---
title: Messages
url: https://platform.claude.com/docs/en/api/typescript/beta/messages
---

# Messages

## Create a Message

- Signature: `client.beta.messages.create(params: MessageCreateParams, options?: RequestOptions): BetaMessage | Stream<BetaRawMessageStreamEvent>`
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

const betaMessage = await client.beta.messages.create({
  max_tokens: 1024,
  messages: [{ content: "Hello, world", role: "user" }],
  model: "claude-opus-5-5"
});

console.log(betaMessage.id);
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
  "context_management": {
    "applied_edits": [
      {
        "cleared_input_tokens": 0,
        "cleared_tool_uses": 0,
        "type": "clear_tool_uses_20250919"
      }
    ]
  },
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
    "fallback_credit": {
      "status": {
        "type": "redeemed"
      }
    },
    "inference_geo": "global",
    "input_tokens": 2095,
    "iterations": [
      {
        "cache_creation": {
          "ephemeral_1h_input_tokens": 0,
          "ephemeral_5m_input_tokens": 0
        },
        "cache_creation_input_tokens": 0,
        "cache_read_input_tokens": 0,
        "input_tokens": 0,
        "model": "claude-fable-5-2",
        "output_tokens": 0,
        "type": "message"
      }
    ],
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
  },
  "input_transformations": [
    {
      "path": "path",
      "reason": "model_binding_mismatch",
      "type": "thinking_dropped"
    }
  ]
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
  messages: Array<BetaMessageParam>;
  /** The model that will complete your prompt. See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options. */
  model: Model;
  /** Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request. */
  cache_control?: BetaCacheControlEphemeral | null;
  /** Compaction configuration. When set on `POST /v1/messages`, the request is a compaction request: the conversation in `messages` is summarized and the response holds only the resulting `compaction` block (`stop_reason` `"compaction"`), which later requests send first in `messages` in place of the messages it summarizes. `POST /v1/messages/count_tokens` accepts this parameter and ignores it: the count it returns is for the conversation in `messages` as sent. Cannot be combined with `context_management`. */
  compaction?: BetaCompactionConfig | null; // beta header: compact-2026-09-04
  /** Container identifier for reuse across requests. */
  container?: BetaContainerParams | string | null;
  /** Context management configuration. This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not. */
  context_management?: BetaContextManagementConfig | null; // beta header: context-management-2025-06-27 or compact-2026-01-12
  /** Request-level diagnostics. Supply `previous_message_id` to have the response include `diagnostics.cache_miss_reason` explaining any prompt-cache divergence from that prior request. */
  diagnostics?: BetaDiagnosticsParam | null;
  /** The `fallback_credit_token` from a prior refusal's `stop_details`. When a preceding request was refused and returned a `fallback_credit_token`, pass that code here on the retry to have the retry's cache-creation tokens for the prefix that was warm on the refused model billed at the cache-read rate. Must be redeemed by the same organization and workspace, with the same request body (optionally extended by one appended `assistant` message whose content is the partial text — with any trailing whitespace stripped from the final text block — and paired server-tool blocks streamed before the refusal; the appended-assistant form is not available for requests with `output_format` set or forced `tool_choice`), on an eligible fallback model, on the same platform, and within 5 minutes of the refusal; a mismatch is a 400. A token minted mid-server-tool-loop whose partial content was continuable may only be redeemed with the appended-assistant form — if an exact-body retry is rejected with a 400 saying the token must be redeemed by continuing the partial response, retry with the appended-assistant form instead. When the appended-assistant form is used on a model that otherwise disallows assistant-turn prefill, this token also authorizes that one prefill. */
  fallback_credit_token?: string | BetaFallbackCreditTokenParam | null; // beta header: fallback-credit-2026-06-01 or fallback-credit-2026-07-01 or server-side-fallback-2026-06-01 or server-side-fallback-2026-07-01
  /** Opt-in server-side retry on one or more substitute models when the requested model declines for policy reasons. Tried in order: if the first entry also declines, the second is tried, and so on. Some models don't support fallbacks; on those models, a list of fallback models returns a 400 error. See [Server-side fallback](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback?sdk_languages=typescript#server-side-fallback). The string "default" requests the requested model's server-defined default fallback configuration. On a model that doesn't support fallbacks, the request runs on the requested model alone, so a declined request stays declined. */
  fallbacks?: BetaFallbacksParam | null; // beta header: server-side-fallback-2026-06-01 or server-side-fallback-2026-07-01
  /** Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used. */
  inference_geo?: string | null;
  /** MCP servers to be utilized in this request */
  mcp_servers?: Array<BetaRequestMCPServerURLDefinition>; // maxItems: 20, beta header: mcp-client-2025-04-04 or mcp-client-2025-11-20 or mcp-client-2026-09-15
  /** An object describing metadata about the request. */
  metadata?: BetaMetadata;
  /** Configuration options for the model's output, such as the output format. */
  output_config?: BetaOutputConfig;
  /** Determines whether to use priority capacity (if available) or standard capacity for this request. Anthropic offers different levels of service for your API requests. See [service-tiers](https://platform.claude.com/docs/en/api/service-tiers?sdk_languages=typescript) for details. */
  service_tier?: "auto" | "standard_only";
  /** The inference speed mode for this request. `"fast"` enables high output-tokens-per-second inference. Some models require the `fast-mode-2026-02-01` beta header for any `speed` value. See [fast mode](https://platform.claude.com/docs/en/build-with-claude/fast-mode?sdk_languages=typescript) for which models. */
  speed?: "standard" | "fast" | null;
  /** Custom text sequences that will cause the model to stop generating. Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`. If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence. */
  stop_sequences?: Array<string>;
  /** Whether to incrementally stream the response using server-sent events. When `true`, SDKs return a raw event stream. In the TypeScript, Python and Ruby SDKs, the recommended way to stream is `messages.stream()`. It sets `stream` for you and accumulates the events into the final message. See [Streaming with SDKs](https://platform.claude.com/docs/en/build-with-claude/streaming?sdk_languages=typescript#streaming-with-sdks) for an example in each language. */
  stream?: boolean;
  /** System prompt. A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices?sdk_languages=typescript#give-claude-a-role). */
  system?: string | Array<BetaTextBlockParam>;
  /** Configuration for Claude's thinking. With `{"type": "adaptive"}`, Claude decides when and how much to think. With `{"type": "enabled"}` (manual extended thinking), you set a `budget_tokens` of at least 1,024. Thinking tokens count toward your `max_tokens` limit. Which `type` values are accepted, and what happens when you omit `thinking`, depend on the model. See [thinking](https://platform.claude.com/docs/en/build-with-claude/thinking?sdk_languages=typescript#configuring-thinking) for each model's behavior. */
  thinking?: BetaThinkingConfigParam;
  /** Server-held conversation state (a Thread). `{"type": "create"}` asks the server to hold this conversation's state under the response's `id`; `{"type": "continue", "previous_message_id": ...}` resumes from a previous response so only the new turn's messages are sent. The response shape is unchanged. */
  thread?: BetaMessageThreadParam | null; // beta header: message-threads-2026-08-12
  /** How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all. */
  tool_choice?: BetaToolChoice;
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
  tools?: Array<BetaToolUnion>;
  /** Optional header to specify the beta version(s) you want to use. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** The user profile ID to attribute this request to. Use when acting on behalf of a party other than your organization. */
  user_profile_id?: string; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
  /**
   * Deprecated: Use `output_config.format` instead. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs?sdk_languages=typescript)
   *
   * A schema to specify Claude's output format in responses. This parameter will be removed in a future release.
   * @deprecated
   */
  output_format?: BetaJSONOutputFormat | null; // beta header: structured-outputs-2025-11-13
}
````

### Returns

- When `stream` is `false` or omitted: `BetaMessage`
- When `stream` is `true`: `Stream<BetaRawMessageStreamEvent>`

````ts
interface BetaMessage {
  /** Object type. For Messages, this is always `"message"`. */
  type: "message";
  /** Unique object identifier. The format and length of IDs may change over time. */
  id: string;
  /** Information about the container used in this request. This will be non-null if a container tool (e.g. code execution) was used. */
  container: BetaContainer | null;
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
  content: Array<BetaContentBlock>;
  /** Context management response. Information about context management strategies applied during the request. */
  context_management: BetaContextManagementResponse | null; // beta header: context-management-2025-06-27 or compact-2026-01-12
  /** Request-level diagnostics. `null` when the request did not supply `diagnostics`, or when it did and no prompt-cache divergence was detected. */
  diagnostics: BetaDiagnostics | null;
  /** The model that will complete your prompt. See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options. */
  model: Model;
  /** Conversational role of the generated message. This will always be `"assistant"`. */
  role: "assistant";
  /** Structured information about why model output stopped. This is `null` when the `stop_reason` has no additional detail to report. */
  stop_details: BetaRefusalStopDetails | null;
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
  stop_reason: BetaStopReason | null;
  /** Which custom stop sequence was generated, if any. This value will be a non-null string if one of your custom stop sequences was generated. */
  stop_sequence: string | null;
  /** Billing and rate-limit usage. Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems. Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response. For example, `output_tokens` will be non-zero, even for an empty string response from Claude. Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`. */
  usage: BetaUsage;
  /** Changes the API made to the request's input before showing it to the model, and blocks that failed a binding check but were left unchanged: one entry per block, in request order. Two entry types today. `thinking_dropped` — a `thinking`, `redacted_thinking` or `connector_text` block from the request's `messages` that was removed from the prompt instead of being shown to the model because it failed a binding check. `thinking_mismatch_allowed` — a `thinking` or `redacted_thinking` block that failed the conversation check (the conversation before it differs from the one it was created in, or it carries no record of one on a model that requires it) and was shown to the model all the same, because that check is not enforced for this request. More entry types may be added over time; ignore types you do not recognize. Requires `anthropic-beta: thinking-binding-controls-2026-08-01`. Present on every such response from a model that supports extended thinking, as `[]` when there is no entry to report; without the beta, blocks are removed or left in place all the same but nothing is reported. Removed blocks contribute nothing to `usage.input_tokens`; blocks left in place count as sent. When streaming, the array is final in `message_start`; the final `message_delta` event carries it only when a server-side model fallback happened mid-stream, in which case it holds the serving model's entries and replaces the one in `message_start`. */
  input_transformations?: Array<BetaInputTransformation> | null; // beta header: thinking-binding-controls-2026-08-01
}

type BetaRawMessageStreamEvent = BetaRawMessageStartEvent | BetaRawMessageDeltaEvent | BetaRawMessageStopEvent | BetaRawContentBlockStartEvent | BetaRawContentBlockDeltaEvent | BetaRawContentBlockStopEvent;
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
type BetaMessageParam = BetaUserMessageParam | BetaAssistantMessageParam | BetaSystemMessageParam;

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

interface BetaCacheControlEphemeral {
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

/** Compact the whole conversation and return a signed `compaction` block, alone, that a later request sends back first in `messages`, in place of the messages it summarizes. There is no trigger and no pause flag: sending the parameter compacts, and nothing is sampled after the block. The summarization prompt is the server's own unless `instructions` are given, which then replace it for this request; a value that is empty or only whitespace counts as absent. */
interface BetaCompactionConfig {
  type: "summarize";
  /** Replaces the server's default summarization prompt for this request. An empty or whitespace-only value counts as absent. */
  instructions?: string | null; // maxLength: 16384
}

/** Container parameters with skills to be loaded. */
interface BetaContainerParams {
  /** Container id */
  id?: string | null;
  /** List of skills to load in the container */
  skills?: Array<BetaSkillParams> | null; // maxItems: 20
}

interface BetaContextManagementConfig {
  /**
   * List of context management edits to apply
   * - `BetaClearThinking20251015Edit`: beta header: context-management-2025-06-27
   * - `BetaCompact20260112Edit`: beta header: compact-2026-01-12
   */
  edits?: Array<BetaClearToolUses20250919Edit | BetaClearThinking20251015Edit | BetaCompact20260112Edit>;
}

/** Request-level diagnostics. Currently carries the previous response id for prompt-cache divergence reporting. */
interface BetaDiagnosticsParam {
  /** The `id` (`msg_...`) from this client's previous /v1/messages response. The server compares that request's prompt fingerprint against this one and returns `diagnostics.cache_miss_reason` when the prompt-cache prefix could not be reused. Pass `null` on the first turn to opt in without a prior message to compare. */
  previous_message_id?: string | null; // maxLength: 256
}

/** Object form of `fallback_credit_token`: the token plus a redemption mode. Requires `anthropic-beta: fallback-credit-2026-07-01`; without that header the field accepts the bare string only. The bare string and the mode-less object are equivalent (both select `strict`), so wrapping an existing token changes nothing by itself. */
interface BetaFallbackCreditTokenParam {
  /** The opaque `fallback_credit_token` from a prior refusal's `stop_details` — the same string the bare-string form carries. */
  token: string; // minLength: 1, maxLength: 2048
  /** How a failing token affects the retry. `strict` (the default, and the bare-string behavior): a failing redemption is a 400 and the retry is not served. `best_effort`: the retry is served either way — a token-layer failure no longer rejects the request; the retry proceeds at normal price and the outcome is reported on the response's `usage.fallback_credit`. Two failures stay hard in both modes: a malformed token, and combining `fallback_credit_token` with `fallbacks`. */
  mode?: "strict" | "best_effort";
}

/** Opt-in server-side retry on one or more substitute models when the requested model declines for policy reasons. Tried in order: if the first entry also declines, the second is tried, and so on. Some models don't support fallbacks; on those models, a list of fallback models returns a 400 error. See [Server-side fallback](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback?sdk_languages=typescript#server-side-fallback). The string "default" requests the requested model's server-defined default fallback configuration. On a model that doesn't support fallbacks, the request runs on the requested model alone, so a declined request stays declined. */
type BetaFallbacksParam = Array<BetaFallbackParam> | "default" | null;

interface BetaRequestMCPServerURLDefinition {
  type: "url";
  name: string;
  url: string;
  authorization_token?: string | null;
  tool_configuration?: BetaRequestMCPServerToolConfiguration | null;
}

interface BetaMetadata {
  /** An external identifier for the user who is associated with the request. This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number. */
  user_id?: string | null; // maxLength: 512
}

interface BetaOutputConfig {
  /** How much effort the model should put into its response. Higher effort levels may result in more thorough analysis but take longer. Valid values are `low`, `medium`, `high`, `xhigh`, or `max`. */
  effort?: "low" | "medium" | "high" | "xhigh" | "max" | null;
  /** A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs?sdk_languages=typescript) */
  format?: BetaJSONOutputFormat | null;
  /** Configuration for token budget tracking across contexts. */
  task_budget?: BetaTokenTaskBudget | null; // beta header: task-budgets-2026-03-13
}

interface BetaTextBlockParam {
  type: "text";
  text: string; // minLength: 1
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
  citations?: Array<BetaTextCitationParam> | null;
}

/** Configuration for Claude's thinking. With `{"type": "adaptive"}`, Claude decides when and how much to think. With `{"type": "enabled"}` (manual extended thinking), you set a `budget_tokens` of at least 1,024. Thinking tokens count toward your `max_tokens` limit. Which `type` values are accepted, and what happens when you omit `thinking`, depend on the model. See [thinking](https://platform.claude.com/docs/en/build-with-claude/thinking?sdk_languages=typescript#configuring-thinking) for each model's behavior. */
type BetaThinkingConfigParam = BetaThinkingConfigEnabled | BetaThinkingConfigDisabled | BetaThinkingConfigBetweenTools | BetaThinkingConfigAdaptive;

/** Server-held conversation state (a Thread). `{"type": "create"}` asks the server to hold this conversation's state under the response's `id`; `{"type": "continue", "previous_message_id": ...}` resumes from a previous response so only the new turn's messages are sent. The response shape is unchanged. */
type BetaMessageThreadParam = BetaThreadCreateParams | BetaThreadContinueParams | null;

/** How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all. */
type BetaToolChoice = BetaToolChoiceAuto | BetaToolChoiceAny | BetaToolChoiceTool | BetaToolChoiceNone;

type BetaToolUnion =
  | BetaTool
  | BetaToolBash20241022 // beta header: computer-use-2024-10-22
  | BetaToolBash20250124
  | BetaCodeExecutionTool20250522
  | BetaCodeExecutionTool20250825
  | BetaCodeExecutionTool20260120
  | BetaCodeExecutionTool20260521
  | BetaBrowserToolset20260801
  | BetaToolComputerUse20241022 // beta header: computer-use-2024-10-22
  | BetaMemoryTool20250818
  | BetaToolComputerUse20250124 // beta header: computer-use-2025-01-24
  | BetaToolTextEditor20241022 // beta header: computer-use-2024-10-22
  | BetaToolComputerUse20251124 // beta header: computer-use-2025-11-24
  | BetaComputerToolset20260801
  | BetaToolTextEditor20250124
  | BetaToolTextEditor20250429
  | BetaToolTextEditor20250728
  | BetaWebSearchTool20250305
  | BetaWebFetchTool20250910
  | BetaWebSearchTool20260209
  | BetaWebFetchTool20260209
  | BetaWebFetchTool20260309
  | BetaWebSearchTool20260318
  | BetaWebFetchTool20260318
  | BetaAdvisorTool20260301 // beta header: advisor-tool-2026-03-01
  | BetaToolSearchToolBm25_20251119
  | BetaToolSearchToolRegex20251119
  | BetaMCPToolset; // beta header: mcp-client-2025-11-20 or mcp-client-2026-09-15

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

interface BetaJSONOutputFormat {
  type: "json_schema";
  /** The JSON schema of the format */
  schema: Record<string, unknown>;
}

/** Information about the container used in the request (for the code execution tool) */
interface BetaContainer {
  /** Identifier for the container used in this request */
  id: string;
  /** The time at which the container will expire. */
  expires_at: string; // format: date-time
  /** Skills loaded in the container */
  skills: Array<BetaContainerSkill> | null;
}

type BetaContentBlock =
  | BetaTextBlock
  | BetaThinkingBlock
  | BetaRedactedThinkingBlock
  | BetaToolUseBlock
  | BetaServerToolUseBlock
  | BetaWebSearchToolResultBlock
  | BetaWebFetchToolResultBlock
  | BetaAdvisorToolResultBlock // beta header: advisor-tool-2026-03-01
  | BetaCodeExecutionToolResultBlock
  | BetaBashCodeExecutionToolResultBlock
  | BetaTextEditorCodeExecutionToolResultBlock
  | BetaToolSearchToolResultBlock
  | BetaMCPToolUseBlock // beta header: mcp-client-2025-04-04 or mcp-client-2025-11-20 or mcp-client-2026-09-15
  | BetaMCPToolResultBlock // beta header: mcp-client-2025-04-04 or mcp-client-2025-11-20 or mcp-client-2026-09-15
  | BetaContainerUploadBlock
  | BetaCompactionBlock // beta header: compact-2026-01-12 or compact-2026-09-04
  | BetaFallbackBlock // beta header: server-side-fallback-2026-06-01 or server-side-fallback-2026-07-01
  | BetaMCPToolListingBlock; // beta header: mcp-client-2026-09-15

interface BetaContextManagementResponse {
  /**
   * List of context management edits that were applied.
   * - `BetaClearThinking20251015EditResponse`: beta header: context-management-2025-06-27
   */
  applied_edits: Array<BetaClearToolUses20250919EditResponse | BetaClearThinking20251015EditResponse>;
}

/** Request-level diagnostics: why the prompt cache could not fully reuse the prefix of the request named by `diagnostics.previous_message_id`. */
interface BetaDiagnostics {
  /** Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed. */
  cache_miss_reason: BetaCacheMissReason | null;
}

/** Structured information about a refusal. */
interface BetaRefusalStopDetails {
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
  /** Opaque code that refunds the cache-miss cost when retrying this refused request on the fallback model. Pass it as `fallback_credit_token` on the retry request. Expires 5 minutes after the refusal. The retry is sent either with the same request body (`system`, `messages`, `tools`, and other render-shaping fields), or with the same body plus one appended `assistant` message whose content is the partial text (with any trailing whitespace stripped from the final text block) and paired server-tool blocks from this refusal — which also authorizes that appended turn as an assistant-prefill continuation on models that otherwise disallow prefill. A token minted mid-server-tool-loop whose partial content was continuable may only be redeemed the second way — if a same-body retry is rejected with a 400 saying the token must be redeemed by continuing the partial response, retry the second way instead. Either way: same workspace, same platform; a mismatch is a 400. Resending a token for an already-warm prefix is permitted but yields no additional credit. `null` when the refused model isn't eligible for a fallback credit. */
  fallback_credit_token: string | null; // beta header: fallback-credit-2026-06-01 or fallback-credit-2026-07-01 or server-side-fallback-2026-06-01 or server-side-fallback-2026-07-01
  /** Whether the accompanying `fallback_credit_token` may be redeemed with the appended-assistant retry form. Only set when `fallback_credit_token` is present. `true`: retry by resending the same request body plus one appended `assistant` message whose content is this response's `content` with any trailing whitespace stripped from the final text block and unpaired `tool_use` blocks omitted (the same appended-turn shape described on `fallback_credit_token`), with the token attached. `false`: retry by resending the original request body unchanged, with the token attached — the appended-assistant form is not available for this refusal (no continuable partial content, or the request uses `output_format` or a `tool_choice` that forces tool use). One exception: when the request used `output_format` or a forced `tool_choice` and the refusal arrived after server tools (including MCP connector tools) had already executed, the token may not be redeemable by either retry form; if the exact-body retry is then rejected with a 400 saying the token must be redeemed by continuing the partial response, discard the token and retry without it. Advisory: if an appended-assistant retry is rejected with a 400 despite `true`, fall back to resending the original request body with the token. */
  fallback_has_prefill_claim: boolean | null; // beta header: fallback-credit-2026-06-01 or fallback-credit-2026-07-01 or server-side-fallback-2026-06-01 or server-side-fallback-2026-07-01
  /** The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise. */
  recommended_model: string | null; // beta header: server-side-fallback-2026-06-01 or server-side-fallback-2026-07-01
}

type BetaStopReason = "end_turn" | "max_tokens" | "stop_sequence" | "tool_use" | "pause_turn" | "compaction" | "refusal" | "model_context_window_exceeded";

interface BetaUsage {
  /** Breakdown of cached tokens by TTL */
  cache_creation: BetaCacheCreation | null;
  /** The number of input tokens used to create the cache entry. */
  cache_creation_input_tokens: number | null; // minimum: 0
  /** The number of input tokens read from the cache. */
  cache_read_input_tokens: number | null; // minimum: 0
  /** Outcome of the `fallback_credit_token` presented on this request. Present on every response to a non-batch request that carried a `fallback_credit_token`, in either redemption mode; absent otherwise (batch items accept and ignore the token and carry no outcome object). */
  fallback_credit: BetaFallbackCreditUsage | null; // beta header: fallback-credit-2026-07-01
  /** The geographic region where inference was performed for this request. */
  inference_geo: string | null;
  /** The number of input tokens which were used. */
  input_tokens: number; // minimum: 0
  /**
   * Per-iteration token usage breakdown.
   *
   * Each entry represents one sampling iteration, with its own input/output token counts and cache statistics, discriminated by `type`. For `message` entries (model sampling iterations, such as the turns of a server-side tool use loop), this allows you to:
   *
   * - Calculate the context window size from the last `message` entry
   * - Understand token accumulation across server-side tool use loops
   *
   * A `compaction` entry reports the token usage of the compaction operation itself — the server-side request that summarizes the context being closed — NOT the size of the context that was compacted away, and its token counts can be much smaller than that closed context (for example, a compaction that closes a ~200k-token context can report only a few thousand tokens). Do not derive the context window size from a `compaction` entry, even when it is the last entry. A `compaction` entry's tokens are not included in the top-level `usage` fields. When an input-token trigger is in effect (the default — 150,000 tokens unless configured otherwise), each `compaction` entry closes a context that had reached at least that threshold, though the context can exceed it by the final iteration's output and tool results.
   */
  iterations: BetaIterationsUsage | null; // beta header: compact-2026-01-12 or compact-2026-09-04 or advisor-tool-2026-03-01 or task-budgets-2026-03-13 or server-side-fallback-2026-06-01 or server-side-fallback-2026-07-01
  /** The number of output tokens which were used. */
  output_tokens: number; // minimum: 0
  /** Breakdown of output tokens by category. `output_tokens` remains the inclusive, authoritative total used for billing. This object provides a read-only decomposition for observability — for example, how many of the billed output tokens were spent on internal reasoning that may have been summarized before being returned to you. */
  output_tokens_details: BetaOutputTokensDetails | null;
  /** The number of server tool requests. */
  server_tool_use: BetaServerToolUsage | null;
  /** If the request used the priority, standard, or batch tier. */
  service_tier: "standard" | "priority" | "batch" | null;
  /** The inference speed mode used for this request. */
  speed: "standard" | "fast" | null;
}

/** One entry of `input_transformations`: either a change the API made to the request's input before showing it to the model, or a block that failed a binding check and was still shown to the model unchanged. The `type` field says which. */
type BetaInputTransformation = BetaThinkingDroppedInputTransformation | BetaThinkingMismatchAllowedInputTransformation;

interface BetaRawMessageStartEvent {
  type: "message_start";
  message: BetaMessage;
}

interface BetaRawMessageDeltaEvent {
  type: "message_delta";
  /** Information about context management strategies applied during the request */
  context_management: BetaContextManagementResponse | null; // beta header: context-management-2025-06-27 or compact-2026-01-12
  delta: Delta;
  /** Billing and rate-limit usage. Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems. Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response. For example, `output_tokens` will be non-zero, even for an empty string response from Claude. Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`. */
  usage: BetaMessageDeltaUsage;
  /** Changes the API made to the request's input before showing it to the model, and blocks that failed a binding check but were left unchanged: one entry per block, in request order. Two entry types today. `thinking_dropped` — a `thinking`, `redacted_thinking` or `connector_text` block from the request's `messages` that was removed from the prompt instead of being shown to the model because it failed a binding check. `thinking_mismatch_allowed` — a `thinking` or `redacted_thinking` block that failed the conversation check (the conversation before it differs from the one it was created in, or it carries no record of one on a model that requires it) and was shown to the model all the same, because that check is not enforced for this request. More entry types may be added over time; ignore types you do not recognize. Requires `anthropic-beta: thinking-binding-controls-2026-08-01`. Present on every such response from a model that supports extended thinking, as `[]` when there is no entry to report; without the beta, blocks are removed or left in place all the same but nothing is reported. Removed blocks contribute nothing to `usage.input_tokens`; blocks left in place count as sent. When streaming, the array is final in `message_start`; the final `message_delta` event carries it only when a server-side model fallback happened mid-stream, in which case it holds the serving model's entries and replaces the one in `message_start`. */
  input_transformations?: Array<BetaInputTransformation> | null; // beta header: thinking-binding-controls-2026-08-01
}

interface BetaRawMessageStopEvent {
  type: "message_stop";
}

interface BetaRawContentBlockStartEvent {
  type: "content_block_start";
  /**
   * - `BetaAdvisorToolResultBlock`: beta header: advisor-tool-2026-03-01
   * - `BetaMCPToolUseBlock`: beta header: mcp-client-2025-04-04 or mcp-client-2025-11-20 or mcp-client-2026-09-15
   * - `BetaMCPToolResultBlock`: beta header: mcp-client-2025-04-04 or mcp-client-2025-11-20 or mcp-client-2026-09-15
   * - `BetaCompactionBlock`: beta header: compact-2026-01-12 or compact-2026-09-04
   * - `BetaFallbackBlock`: beta header: server-side-fallback-2026-06-01 or server-side-fallback-2026-07-01
   * - `BetaMCPToolListingBlock`: beta header: mcp-client-2026-09-15
   */
  content_block: BetaTextBlock | BetaThinkingBlock | BetaRedactedThinkingBlock | BetaToolUseBlock | BetaServerToolUseBlock | BetaWebSearchToolResultBlock | BetaWebFetchToolResultBlock | BetaAdvisorToolResultBlock | BetaCodeExecutionToolResultBlock | BetaBashCodeExecutionToolResultBlock | BetaTextEditorCodeExecutionToolResultBlock | BetaToolSearchToolResultBlock | BetaMCPToolUseBlock | BetaMCPToolResultBlock | BetaContainerUploadBlock | BetaCompactionBlock | BetaFallbackBlock | BetaMCPToolListingBlock;
  index: number;
}

interface BetaRawContentBlockDeltaEvent {
  type: "content_block_delta";
  delta: BetaRawContentBlockDelta;
  index: number;
}

interface BetaRawContentBlockStopEvent {
  type: "content_block_stop";
  index: number;
}

interface BetaUserMessageParam {
  content: BetaMessageContentParam;
  role: "user";
}

interface BetaAssistantMessageParam {
  content: BetaMessageContentParam;
  role: "assistant";
}

interface BetaSystemMessageParam {
  role: "system";
  /** How long this system message's text stays in front of the model. `"never"` (the default) renders it on every request that includes it. `"next_user_message"` renders it only for the user turn it follows: once a later `role: "user"` message exists in `messages` the message stays in the array (send it unchanged) but is no longer shown to the model. Only permitted on `role: "system"` messages. */
  clear_at?: "next_user_message" | "never" | null; // beta header: mid-conversation-system-clear-at-2026-08-21
  /**
   * - `BetaRequestToolAdditionBlock`: beta header: mid-conversation-tool-changes-2026-07-01 or inline-tools-2026-09-15
   * - `BetaRequestToolRemovalBlock`: beta header: mid-conversation-tool-changes-2026-07-01 or inline-tools-2026-09-15
   */
  content?: string | Array<BetaTextBlockParam | BetaRequestToolAdditionBlock | BetaRequestToolRemovalBlock>;
  /** Per-message output configuration on a role:"system" input message. Fields here apply per-turn; `format` remains top-level only. An empty `{}` is accepted on a message that carries content; a message with neither content nor output_config fields is rejected. */
  output_config?: BetaSystemMessageOutputConfig | null; // beta header: mid-conversation-output-config-2026-07-01
}

/** Per-message output configuration on a role:"system" input message. Fields here apply per-turn; `format` remains top-level only. An empty `{}` is accepted on a message that carries content; a message with neither content nor output_config fields is rejected. */
interface BetaSystemMessageOutputConfig {
  /** How much effort the model should put into its response. Higher effort levels may result in more thorough analysis but take longer. Valid values are `low`, `medium`, `high`, `xhigh`, or `max`. */
  effort?: "low" | "medium" | "high" | "xhigh" | "max" | null;
}

type BetaMessageContentParam = string | Array<BetaContentBlockParam>;

type BetaContentBlockParam =
  | BetaTextBlockParam
  | BetaImageBlockParam
  | BetaRequestDocumentBlock
  | BetaSearchResultBlockParam
  | BetaThinkingBlockParam
  | BetaRedactedThinkingBlockParam
  | BetaToolUseBlockParam
  | BetaToolResultBlockParam
  | BetaServerToolUseBlockParam
  | BetaWebSearchToolResultBlockParam
  | BetaWebFetchToolResultBlockParam
  | BetaAdvisorToolResultBlockParam // beta header: advisor-tool-2026-03-01
  | BetaCodeExecutionToolResultBlockParam
  | BetaBashCodeExecutionToolResultBlockParam
  | BetaTextEditorCodeExecutionToolResultBlockParam
  | BetaToolSearchToolResultBlockParam
  | BetaMCPToolUseBlockParam // beta header: mcp-client-2025-04-04 or mcp-client-2025-11-20 or mcp-client-2026-09-15
  | BetaRequestMCPToolResultBlockParam // beta header: mcp-client-2025-04-04 or mcp-client-2025-11-20 or mcp-client-2026-09-15
  | BetaContainerUploadBlockParam
  | BetaCompactionBlockParam // beta header: compact-2026-01-12 or compact-2026-09-04
  | BetaRequestToolAdditionBlock // beta header: mid-conversation-tool-changes-2026-07-01 or inline-tools-2026-09-15
  | BetaRequestToolRemovalBlock // beta header: mid-conversation-tool-changes-2026-07-01 or inline-tools-2026-09-15
  | BetaMCPToolListingBlockParam // beta header: mcp-client-2026-09-15
  | BetaFallbackBlockParam; // beta header: server-side-fallback-2026-06-01 or server-side-fallback-2026-07-01

interface BetaImageBlockParam {
  type: "image";
  source: BetaBase64ImageSource | BetaURLImageSource | BetaFileImageSource;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
  /** Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field. */
  transformations?: BetaImageTransformationsParam | null;
}

interface BetaRequestDocumentBlock {
  type: "document";
  source: BetaBase64PDFSource | BetaPlainTextSource | BetaContentBlockSource | BetaURLPDFSource | BetaFileDocumentSource;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
  citations?: BetaCitationsConfigParam | null;
  context?: string | null; // minLength: 1
  title?: string | null; // minLength: 1, maxLength: 500
}

interface BetaSearchResultBlockParam {
  type: "search_result";
  content: Array<BetaTextBlockParam>;
  source: string;
  title: string;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
  citations?: BetaCitationsConfigParam;
}

interface BetaThinkingBlockParam {
  type: "thinking";
  /** The `signature` value of this thinking block, exactly as returned by the API in a previous response. Used to verify that the block was generated by Claude. Thinking blocks must be passed back unmodified and in their original order; a modified block results in a 400 `invalid_request_error`. */
  signature: string;
  /** The `thinking` text of this block as returned by the API. */
  thinking: string;
}

interface BetaRedactedThinkingBlockParam {
  type: "redacted_thinking";
  /** The `data` value of this redacted thinking block, exactly as returned by the API in a previous response. Opaque and encrypted; pass it back unchanged. */
  data: string;
}

interface BetaToolUseBlockParam {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  input: Record<string, unknown>;
  name: string; // minLength: 1, maxLength: 200
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
  caller?: BetaDirectCaller | BetaServerToolCaller | BetaServerToolCaller20260120;
  /** For a toolset member tool_use, the toolset family this member belongs to. */
  toolset_name?: string | null; // minLength: 1, maxLength: 64, pattern: ^[a-zA-Z0-9_-]+$
}

interface BetaToolResultBlockParam {
  type: "tool_result";
  tool_use_id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
  content?: string | Array<BetaTextBlockParam | BetaImageBlockParam | BetaSearchResultBlockParam | BetaRequestDocumentBlock | BetaToolReferenceBlockParam | BetaBrowserStateBlockParam>;
  is_error?: boolean;
  /** For a toolset member tool_result, the toolset family of the paired tool_use. */
  toolset_name?: string | null; // minLength: 1, maxLength: 64, pattern: ^[a-zA-Z0-9_-]+$
}

interface BetaServerToolUseBlockParam {
  type: "server_tool_use";
  id: string; // pattern: ^srvtoolu_[a-zA-Z0-9_]+$
  input: Record<string, unknown>;
  /** - `"advisor"`: beta header: advisor-tool-2026-03-01 */
  name: "advisor" | "web_search" | "web_fetch" | "code_execution" | "bash_code_execution" | "text_editor_code_execution" | "tool_search_tool_regex" | "tool_search_tool_bm25";
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
  caller?: BetaDirectCaller | BetaServerToolCaller | BetaServerToolCaller20260120;
}

interface BetaWebSearchToolResultBlockParam {
  type: "web_search_tool_result";
  content: BetaWebSearchToolResultBlockParamContent;
  tool_use_id: string; // pattern: ^srvtoolu_[a-zA-Z0-9_]+$
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
  caller?: BetaDirectCaller | BetaServerToolCaller | BetaServerToolCaller20260120;
}

interface BetaWebFetchToolResultBlockParam {
  type: "web_fetch_tool_result";
  content: BetaWebFetchToolResultErrorBlockParam | BetaWebFetchBlockParam;
  tool_use_id: string; // pattern: ^srvtoolu_[a-zA-Z0-9_]+$
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
  caller?: BetaDirectCaller | BetaServerToolCaller | BetaServerToolCaller20260120;
}

interface BetaAdvisorToolResultBlockParam {
  type: "advisor_tool_result";
  content: BetaAdvisorToolResultErrorParam | BetaAdvisorResultBlockParam | BetaAdvisorRedactedResultBlockParam;
  tool_use_id: string; // pattern: ^srvtoolu_[a-zA-Z0-9_]+$
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
}

interface BetaCodeExecutionToolResultBlockParam {
  type: "code_execution_tool_result";
  content: BetaCodeExecutionToolResultBlockParamContent;
  tool_use_id: string; // pattern: ^srvtoolu_[a-zA-Z0-9_]+$
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
}

interface BetaBashCodeExecutionToolResultBlockParam {
  type: "bash_code_execution_tool_result";
  content: BetaBashCodeExecutionToolResultErrorParam | BetaBashCodeExecutionResultBlockParam;
  tool_use_id: string; // pattern: ^srvtoolu_[a-zA-Z0-9_]+$
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
}

interface BetaTextEditorCodeExecutionToolResultBlockParam {
  type: "text_editor_code_execution_tool_result";
  content: BetaTextEditorCodeExecutionToolResultErrorParam | BetaTextEditorCodeExecutionViewResultBlockParam | BetaTextEditorCodeExecutionCreateResultBlockParam | BetaTextEditorCodeExecutionStrReplaceResultBlockParam;
  tool_use_id: string; // pattern: ^srvtoolu_[a-zA-Z0-9_]+$
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
}

interface BetaToolSearchToolResultBlockParam {
  type: "tool_search_tool_result";
  content: BetaToolSearchToolResultErrorParam | BetaToolSearchToolSearchResultBlockParam;
  tool_use_id: string; // pattern: ^srvtoolu_[a-zA-Z0-9_]+$
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
}

interface BetaMCPToolUseBlockParam {
  type: "mcp_tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  input: Record<string, unknown>;
  name: string;
  /** The name of the MCP server */
  server_name: string;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
}

interface BetaRequestMCPToolResultBlockParam {
  type: "mcp_tool_result";
  tool_use_id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
  content?: string | Array<BetaTextBlockParam>;
  is_error?: boolean;
}

/** A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory. */
interface BetaContainerUploadBlockParam {
  type: "container_upload";
  file_id: string;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
}

/** A compaction block containing summary of previous context. Users should round-trip these blocks from responses to subsequent requests to maintain context across compaction boundaries. When content is None, the block represents a failed compaction. The server treats these as no-ops. Empty string content is not allowed. */
interface BetaCompactionBlockParam {
  type: "compaction";
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
  /** Summary of previously compacted content, or null if compaction failed */
  content?: string | null;
  /** Opaque metadata from prior compaction, to be round-tripped verbatim */
  encrypted_content?: string | null; // beta header: task-budgets-2026-03-13
  /** The block's signature as returned, to be sent back verbatim */
  signature?: string | null; // beta header: compact-2026-09-04
  /** The tool changes of the compacted range, as the server returned them on this block: the `tool_addition` and `tool_removal` entries that take the request's `tools` to the tool set in effect at the end of the range. Send them back unchanged with the block. */
  tool_changes?: Array<BetaRequestToolAdditionBlock | BetaRequestToolRemovalBlock> | null; // beta header: inline-tools-2026-09-15
}

/** Mid-conversation directive to make a tool available. `tool` is a reference to a tool (or MCP toolset) declared in the request's `tools`. Under the `inline-tools-2026-09-15` beta it may instead be a reference to a tool defined earlier in `messages`, or a `tool_definition` object that carries an inline tool definition in `definition` (the same object a `tools` entry holds). An `mcp_toolset` definition also requires the `mcp-client-2026-09-15` beta. The tool is offered to the model from this point in the conversation onward. */
interface BetaRequestToolAdditionBlock {
  type: "tool_addition";
  /**
   * - `BetaToolChangeMCPToolReference`: beta header: mcp-client-2025-04-04 or mcp-client-2025-11-20 or mcp-client-2026-09-15
   * - `BetaToolChangeMCPToolsetReference`: beta header: mcp-client-2025-04-04 or mcp-client-2025-11-20 or mcp-client-2026-09-15
   * - `BetaToolChangeToolDefinitionParam`: beta header: inline-tools-2026-09-15
   */
  tool: BetaToolChangeToolReference | BetaToolChangeMCPToolReference | BetaToolChangeMCPToolsetReference | BetaToolChangeToolDefinitionParam;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
}

/** Mid-conversation directive to withdraw a tool. `tool` references a tool (or MCP toolset) by name: one declared in the request's `tools` or defined earlier in `messages`. It is no longer offered to the model from this point in the conversation onward. */
interface BetaRequestToolRemovalBlock {
  type: "tool_removal";
  /**
   * - `BetaToolChangeMCPToolReference`: beta header: mcp-client-2025-04-04 or mcp-client-2025-11-20 or mcp-client-2026-09-15
   * - `BetaToolChangeMCPToolsetReference`: beta header: mcp-client-2025-04-04 or mcp-client-2025-11-20 or mcp-client-2026-09-15
   */
  tool: BetaToolChangeToolReference | BetaToolChangeMCPToolReference | BetaToolChangeMCPToolsetReference;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
}

/** The tool listing an MCP server returned while an earlier response was produced, as that response carried it. Send the assistant message back unchanged, this block included, and the server uses this listing for the matching `mcp_toolset` instead of asking the MCP server again. */
interface BetaMCPToolListingBlockParam {
  type: "mcp_tool_listing";
  /** The name of the MCP server this listing came from, as `mcp_servers` declares it. */
  mcp_server_name: string; // minLength: 1, maxLength: 255
  /** The server's tools, exactly as the response listed them. */
  tools: Array<BetaMCPToolParam>;
}

/** A `fallback` block echoed back from a prior response. Accepted in `messages[].content` and not rendered into the prompt; not validated against the request's `fallbacks` chain or top-level `model`. When you send the assistant turn back, keep this block in its original position. The block marks the boundary between content produced before and after a fallback hop, and the server relies on that boundary to validate the turn: when thinking runs flank the boundary, omitting the block merges them into one span the server cannot validate (the request is rejected), and moving it into the middle of a single run is likewise rejected; between non-thinking blocks the block's placement has no effect on thinking validation. Some blocks from before the turn's final `fallback` block must be left out when you send the turn back, and no `tool_result` is sent for a `tool_use` block you left out. See the [refusals and fallback guide](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback?sdk_languages=typescript#continuing-the-conversation) to learn which blocks to keep. */
interface BetaFallbackBlockParam {
  type: "fallback";
  /** Identifies one hop of a fallback transition. */
  from: BetaFallbackInfoParam;
  /** Identifies one hop of a fallback transition. */
  to: BetaFallbackInfoParam;
  /** The response block's `trigger`, echoed verbatim. Accepted and ignored by the server; any object or `null` is allowed. */
  trigger?: unknown;
}

interface BetaBase64ImageSource {
  type: "base64";
  data: string; // format: byte
  media_type: "image/jpeg" | "image/png" | "image/gif" | "image/webp";
}

interface BetaURLImageSource {
  type: "url";
  url: string;
}

interface BetaFileImageSource {
  type: "file";
  file_id: string;
}

/** Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field. */
interface BetaImageTransformationsParam {
  /** What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down. */
  oversized_image?: "downsize" | "error";
}

interface BetaBase64PDFSource {
  type: "base64";
  data: string; // format: byte
  media_type: "application/pdf";
}

interface BetaPlainTextSource {
  type: "text";
  data: string;
  media_type: "text/plain";
}

interface BetaContentBlockSource {
  type: "content";
  content: string | Array<BetaContentBlockSourceContent>;
}

interface BetaURLPDFSource {
  type: "url";
  url: string;
}

interface BetaFileDocumentSource {
  type: "file";
  file_id: string;
}

interface BetaCitationsConfigParam {
  enabled?: boolean;
}

type BetaContentBlockSourceContent = BetaTextBlockParam | BetaImageBlockParam;

/** Tool invocation directly from the model. */
interface BetaDirectCaller {
  type: "direct";
}

/** Tool invocation generated by a server-side tool. */
interface BetaServerToolCaller {
  type: "code_execution_20250825";
  tool_id: string; // pattern: ^srvtoolu_[a-zA-Z0-9_]+$
}

interface BetaServerToolCaller20260120 {
  type: "code_execution_20260120";
  tool_id: string; // pattern: ^srvtoolu_[a-zA-Z0-9_]+$
}

type BetaWebSearchToolResultBlockParamContent = Array<BetaWebSearchResultBlockParam> | BetaWebSearchToolRequestError;

interface BetaWebSearchResultBlockParam {
  type: "web_search_result";
  encrypted_content: string;
  title: string;
  url: string;
  page_age?: string | null;
}

interface BetaWebSearchToolRequestError {
  type: "web_search_tool_result_error";
  error_code: BetaWebSearchToolResultErrorCode;
}

type BetaWebSearchToolResultErrorCode = "invalid_tool_input" | "unavailable" | "max_uses_exceeded" | "too_many_requests" | "query_too_long" | "request_too_large";

interface BetaWebFetchToolResultErrorBlockParam {
  type: "web_fetch_tool_result_error";
  error_code: BetaWebFetchToolResultErrorCode;
}

interface BetaWebFetchBlockParam {
  type: "web_fetch_result";
  content: BetaRequestDocumentBlock;
  /** Fetched content URL */
  url: string;
  /** ISO 8601 timestamp when the content was retrieved */
  retrieved_at?: string | null;
}

type BetaWebFetchToolResultErrorCode = "invalid_tool_input" | "url_too_long" | "url_not_allowed" | "url_not_in_prior_context" | "url_not_accessible" | "unsupported_content_type" | "too_many_requests" | "max_uses_exceeded" | "unavailable" | "content_too_large";

interface BetaAdvisorToolResultErrorParam {
  type: "advisor_tool_result_error";
  error_code: "max_uses_exceeded" | "prompt_too_long" | "too_many_requests" | "overloaded" | "unavailable" | "execution_time_exceeded" | "model_not_found";
}

interface BetaAdvisorResultBlockParam {
  type: "advisor_result";
  text: string;
  stop_reason?: string | null;
}

interface BetaAdvisorRedactedResultBlockParam {
  type: "advisor_redacted_result";
  /** Opaque blob produced by a prior response; must be round-tripped verbatim. */
  encrypted_content: string;
  stop_reason?: string | null;
}

type BetaCodeExecutionToolResultBlockParamContent = BetaCodeExecutionToolResultErrorParam | BetaCodeExecutionResultBlockParam | BetaEncryptedCodeExecutionResultBlockParam;

interface BetaCodeExecutionToolResultErrorParam {
  type: "code_execution_tool_result_error";
  error_code: BetaCodeExecutionToolResultErrorCode;
}

interface BetaCodeExecutionResultBlockParam {
  type: "code_execution_result";
  content: Array<BetaCodeExecutionOutputBlockParam>;
  return_code: number;
  stderr: string;
  stdout: string;
}

/** The output and exit code of Python code that Claude ran with the code execution tool, with standard output in encrypted form, sent back in a later request. */
interface BetaEncryptedCodeExecutionResultBlockParam {
  type: "encrypted_code_execution_result";
  content: Array<BetaCodeExecutionOutputBlockParam>;
  encrypted_stdout: string;
  return_code: number;
  stderr: string;
}

type BetaCodeExecutionToolResultErrorCode = "invalid_tool_input" | "unavailable" | "too_many_requests" | "execution_time_exceeded";

interface BetaCodeExecutionOutputBlockParam {
  type: "code_execution_output";
  file_id: string;
}

interface BetaBashCodeExecutionToolResultErrorParam {
  type: "bash_code_execution_tool_result_error";
  error_code: "invalid_tool_input" | "unavailable" | "too_many_requests" | "execution_time_exceeded" | "output_file_too_large";
}

interface BetaBashCodeExecutionResultBlockParam {
  type: "bash_code_execution_result";
  content: Array<BetaBashCodeExecutionOutputBlockParam>;
  return_code: number;
  stderr: string;
  stdout: string;
}

interface BetaBashCodeExecutionOutputBlockParam {
  type: "bash_code_execution_output";
  file_id: string;
}

interface BetaTextEditorCodeExecutionToolResultErrorParam {
  type: "text_editor_code_execution_tool_result_error";
  error_code: "invalid_tool_input" | "unavailable" | "too_many_requests" | "execution_time_exceeded" | "file_not_found";
  error_message?: string | null;
}

interface BetaTextEditorCodeExecutionViewResultBlockParam {
  type: "text_editor_code_execution_view_result";
  content: string;
  file_type: "text" | "image" | "pdf";
  num_lines?: number | null;
  start_line?: number | null;
  total_lines?: number | null;
}

interface BetaTextEditorCodeExecutionCreateResultBlockParam {
  type: "text_editor_code_execution_create_result";
  is_file_update: boolean;
}

interface BetaTextEditorCodeExecutionStrReplaceResultBlockParam {
  type: "text_editor_code_execution_str_replace_result";
  lines?: Array<string> | null;
  new_lines?: number | null;
  new_start?: number | null;
  old_lines?: number | null;
  old_start?: number | null;
}

interface BetaToolSearchToolResultErrorParam {
  type: "tool_search_tool_result_error";
  error_code: "invalid_tool_input" | "unavailable" | "too_many_requests" | "execution_time_exceeded";
  error_message?: string | null;
}

interface BetaToolSearchToolSearchResultBlockParam {
  type: "tool_search_tool_search_result";
  tool_references: Array<BetaToolReferenceBlockParam>;
}

/** Reference to a single tool, by the name the model uses to call it: a tool declared in `tools` or defined by an earlier `tool_addition` block. Does not accept the composed `{server}_{name}` form the server assigns to MCP-resolved tools; use `mcp_tool_reference` or `mcp_toolset_reference` for those. */
interface BetaToolChangeToolReference {
  type: "tool_reference";
  name: string; // pattern: ^[a-zA-Z0-9_-]{1,128}$
}

/** Reference to a single MCP tool by its server and remote name; the same `server_name`/`name` pair `mcp_tool_use` carries. */
interface BetaToolChangeMCPToolReference {
  type: "mcp_tool_reference";
  name: string;
  server_name: string;
}

/** Reference to every tool in the named MCP server's toolset. */
interface BetaToolChangeMCPToolsetReference {
  type: "mcp_toolset_reference";
  server_name: string;
}

/** A tool defined by value: `definition` is a `tools` entry (any kind `tools` accepts, an MCP toolset included). An `mcp_toolset` given here also requires the `mcp-client-2026-09-15` beta. */
interface BetaToolChangeToolDefinitionParam {
  type: "tool_definition";
  definition: BetaToolUnion;
}

/** A tool as an MCP server lists it: its name on that server, its description, and its input schema. */
interface BetaMCPToolParam {
  /** The tool's input schema as the MCP server lists it, verbatim. */
  input_schema: Record<string, unknown>;
  /** The tool's name as the MCP server lists it (not prefixed with the server name). */
  name: string; // minLength: 1
  /** The tool's description as the MCP server lists it. */
  description?: string | null;
}

/** Identifies one hop of a fallback transition. */
interface BetaFallbackInfoParam {
  /** The model that will complete your prompt. See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options. */
  model: Model;
}

/** Tool reference block that can be included in tool_result content. */
interface BetaToolReferenceBlockParam {
  type: "tool_reference";
  tool_name: string; // minLength: 1, maxLength: 256, pattern: ^[a-zA-Z0-9_-]{1,256}$
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
}

/** The caller's browser state after a browser toolset member call — the full inventory of open tabs, which tab is active, and any side effects (tabs opened, download state changes) the call produced. At most one per `tool_result`, only on a non-error result answering a browser toolset member `tool_use`. The server renders the model-visible text from it; the model never sees the raw fields. */
interface BetaBrowserStateBlockParam {
  type: "browser_state";
  /** All tabs open in the browser after this call — the full inventory, not a delta. May be empty. Whenever non-empty, exactly one entry carries `active: true`. */
  tabs: Array<BetaBrowserStateTabEntry>; // maxItems: 100
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
  /** Tabs opened and download state changes during this call. "Nothing to report" is expressed by omitting the field, never by an empty list. */
  state_changes?: Array<BetaBrowserStateChange> | null; // minItems: 1, maxItems: 200
}

/** One open browser tab reported in a `browser_state` block's `tabs` inventory. `tab_id` is the caller-assigned identifier for the tab; `title` and `url` describe the page the tab is currently showing and may be empty strings (a blank tab legitimately has both empty). `active` marks the tab that is active after this call; whenever `tabs` is non-empty, exactly one entry is marked. */
interface BetaBrowserStateTabEntry {
  /** The caller-assigned identifier for this tab, unique within the inventory. */
  tab_id: string; // minLength: 1, maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$
  /** The title of the page the tab is showing. May be empty. */
  title: string; // maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$
  /** The URL of the page the tab is showing. May be empty. */
  url: string; // maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$
  /** Whether this tab is the active tab after this call. Whenever `tabs` is non-empty, exactly one entry is marked `active: true`. */
  active?: boolean;
}

type BetaBrowserStateChange = BetaBrowserStateChangeTabOpened | BetaBrowserStateChangeDownloadStarted | BetaBrowserStateChangeDownloadCompleted | BetaBrowserStateChangeDownloadFailed;

/** A tab this call's execution opened that remains open at its end — the creation delta of the `tabs` inventory, not an event log. Carries only the `tab_id`; the tab's `title` and `url` live on its `tabs` entry, which must include the same `tab_id`. A tab opened during a failed call gets no deferred `tab_opened`; it simply appears in the next result's `tabs` inventory. */
interface BetaBrowserStateChangeTabOpened {
  type: "tab_opened";
  /** The `tab_id` of the opened tab, present in `tabs`. */
  tab_id: string; // minLength: 1, maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$
}

/** A file download that started during this call. */
interface BetaBrowserStateChangeDownloadStarted {
  type: "download_started";
  /** The caller-assigned identifier for this download, stable across the state changes reporting it. */
  download_id: string; // minLength: 1, maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$
  /** The final post-redirect URL the download was served from. */
  url: string; // maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$
}

/** A file download that finished during this call, reported with the same `download_id` as its `download_started` — or without a prior `download_started`, when the download finished during the call that started it (at most one state change per `download_id` per result). */
interface BetaBrowserStateChangeDownloadCompleted {
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
interface BetaBrowserStateChangeDownloadFailed {
  type: "download_failed";
  /** The caller-assigned identifier for this download, stable across the state changes reporting it. */
  download_id: string; // minLength: 1, maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$
  /** The final post-redirect URL the download was served from. */
  url: string; // maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$
  /** The failure or cancellation detail, when known. */
  error?: string | null; // maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$
}

/** Specification for a skill to be loaded in a container. */
interface BetaSkillParams {
  /** Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined) */
  type: "anthropic" | "custom";
  /** Skill ID */
  skill_id: string; // minLength: 1, maxLength: 64
  /** Skill version or 'latest' for most recent version */
  version?: string; // minLength: 1, maxLength: 64
}

interface BetaClearToolUses20250919Edit {
  type: "clear_tool_uses_20250919";
  /** Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed. */
  clear_at_least?: BetaInputTokensClearAtLeast | null;
  /** Whether to clear all tool inputs (bool) or specific tool inputs to clear (list) */
  clear_tool_inputs?: boolean | Array<string> | null;
  /** Tool names whose uses are preserved from clearing */
  exclude_tools?: Array<string> | null;
  /** Number of tool uses to retain in the conversation */
  keep?: BetaToolUsesKeep;
  /** Condition that triggers the context management strategy */
  trigger?: BetaInputTokensTrigger | BetaToolUsesTrigger;
}

interface BetaClearThinking20251015Edit {
  type: "clear_thinking_20251015";
  /** Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed. */
  keep?: BetaThinkingTurns | BetaAllThinkingTurns | "all";
}

/** Automatically compact older context when reaching the configured trigger threshold. */
interface BetaCompact20260112Edit {
  type: "compact_20260112";
  /** Additional instructions for summarization. */
  instructions?: string | null;
  /** Whether to pause after compaction and return the compaction block to the user. */
  pause_after_compaction?: boolean;
  /** When to trigger compaction. Defaults to 150000 input tokens. */
  trigger?: BetaInputTokensTrigger | null;
}

interface BetaThinkingTurns {
  type: "thinking_turns";
  value: number; // minimum: 1
}

interface BetaAllThinkingTurns {
  type: "all";
}

interface BetaInputTokensClearAtLeast {
  type: "input_tokens";
  value: number; // minimum: 0
}

interface BetaToolUsesKeep {
  type: "tool_uses";
  value: number; // minimum: 0
}

interface BetaInputTokensTrigger {
  type: "input_tokens";
  value: number; // minimum: 1
}

interface BetaToolUsesTrigger {
  type: "tool_uses";
  value: number; // minimum: 1
}

/** One entry in the `fallbacks` chain on a `/v1/messages` request. `model` is required. The override fields (`max_tokens`, `thinking`, `output_config`, and `speed`) set the corresponding parameter for this attempt only and are validated as if the request were made to `model`. Any other key is rejected at parse time. */
interface BetaFallbackParam {
  /** The model that will complete your prompt. See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options. */
  model: Model;
  /** The `max_tokens` for the fallback attempt that uses this `fallbacks` entry's `model`, in place of the request's `max_tokens`. If you leave it out or set it to `null`, the attempt uses the request's `max_tokens`. See the [refusals and fallback guide](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback?sdk_languages=typescript#naming-your-own-fallback-models) to learn more about fallback entries. */
  max_tokens?: number | null;
  /**
   * Output parameters for the fallback attempt that uses this `fallbacks` entry's `model`, combined with the request's `output_config` one field at a time.
   *
   * - `format`: If you leave it out, the attempt uses the request's `format`. If you set it to `null`, the attempt runs without a format.
   * - `effort`: If you leave it out, the attempt uses the request's `effort` when `model` supports that level with the attempt's `thinking`. If the request doesn't set `effort`, if `model` doesn't support the level, or if you set `effort` to `null`, the attempt runs at the default effort of `model`.
   * - `task_budget`: If you leave it out, the attempt uses the request's `task_budget` when `model` accepts a task budget of that size. If the request doesn't set `task_budget`, if `model` doesn't accept it, or if you set `task_budget` to `null`, the attempt runs without a task budget.
   *
   * Set `output_config` to `null` to run the attempt without a format or a task budget, at the default effort of `model`.
   *
   * These rules apply with the `server-side-fallback-2026-07-01` beta header.
   */
  output_config?: BetaOutputConfig | null;
  /** The inference speed mode for the fallback attempt that uses this `fallbacks` entry's `model`. If you leave it out, the attempt runs at `fast` speed only when the request sets `speed` to `fast` and your organization can use fast mode on `model`. Otherwise, or when you set this field to `null`, the attempt runs at `standard` speed. These rules apply with the `server-side-fallback-2026-07-01` beta header. */
  speed?: "standard" | "fast" | null;
  /** The thinking configuration for the fallback attempt that uses this `fallbacks` entry's `model`. If you leave it out, the attempt uses the request's `thinking` when `model` supports that thinking `type`. If you leave it out and the request's thinking `type` is `between_tools` but `model` doesn't support `between_tools`, the attempt uses `disabled` if `model` supports it. Otherwise, if `model` doesn't support the request's thinking `type`, if the request doesn't set `thinking`, or if you set this field to `null`, the attempt uses the thinking `type` that `model` uses when a request leaves out `thinking`. The request's `thinking.display` still applies where `model` allows it. These rules apply with the `server-side-fallback-2026-07-01` beta header. */
  thinking?: BetaThinkingConfigEnabled | BetaThinkingConfigDisabled | BetaThinkingConfigBetweenTools | BetaThinkingConfigAdaptive | null;
}

interface BetaThinkingConfigEnabled {
  type: "enabled";
  /** Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality. Must be ≥1024 and less than `max_tokens`. See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking?sdk_languages=typescript) for details. */
  budget_tokens: number; // minimum: 1024
  /** Controls for block binding: what happens when a thinking block this request sends back fails the conversation check. `null`, absent or an empty object means every default. */
  block_binding?: BetaThinkingBlockBinding | null; // beta header: thinking-binding-controls-2026-08-01
  /**
   * Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. The default depends on the model; see [Controlling thinking display](https://platform.claude.com/docs/en/build-with-claude/thinking?sdk_languages=typescript#controlling-thinking-display).
   * - `"updates"`: beta header: thinking-display-updates-2026-08-18
   */
  display?: "summarized" | "omitted" | "updates" | null;
}

interface BetaThinkingConfigDisabled {
  type: "disabled";
}

interface BetaThinkingConfigBetweenTools {
  type: "between_tools";
}

interface BetaThinkingConfigAdaptive {
  type: "adaptive";
  /** Controls for block binding: what happens when a thinking block this request sends back fails the conversation check. `null`, absent or an empty object means every default. */
  block_binding?: BetaThinkingBlockBinding | null; // beta header: thinking-binding-controls-2026-08-01
  /**
   * Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. The default depends on the model; see [Controlling thinking display](https://platform.claude.com/docs/en/build-with-claude/thinking?sdk_languages=typescript#controlling-thinking-display).
   * - `"updates"`: beta header: thinking-display-updates-2026-08-18
   */
  display?: "summarized" | "omitted" | "updates" | null;
}

/** Controls for block binding: what happens when a thinking block this request sends back fails the conversation check. Every field is optional; an empty object means every default. */
interface BetaThinkingBlockBinding {
  /** "error" (default) | "drop_block". What happens when a thinking block in `messages` fails the conversation check (it was created in a different conversation, or the messages before it have changed since). "error" fails the request with a 400 error. "drop_block" removes the failing blocks and the request proceeds; each removal is reported in `input_transformations`. */
  prefix_mismatch_behavior?: BetaThinkingPrefixMismatchBehavior | null;
}

/** What happens when a thinking block in `messages` fails the conversation check: it was created in a different conversation, or the messages before it have changed since. `"error"` (the default) fails the request with a 400 error. `"drop_block"` removes the failing blocks and the request proceeds; the model no longer sees the dropped reasoning. */
type BetaThinkingPrefixMismatchBehavior = "error" | "drop_block";

interface BetaRequestMCPServerToolConfiguration {
  allowed_tools?: Array<string> | null;
  enabled?: boolean | null;
}

/** User-configurable total token budget across contexts. */
interface BetaTokenTaskBudget {
  /** The budget type. Currently only 'tokens' is supported. */
  type: "tokens";
  /** Total token budget across all contexts in the session. */
  total: number; // minimum: 1024
  /** Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided. */
  remaining?: number | null; // minimum: 0
}

type BetaTextCitationParam = BetaCitationCharLocationParam | BetaCitationPageLocationParam | BetaCitationContentBlockLocationParam | BetaCitationWebSearchResultLocationParam | BetaCitationSearchResultLocationParam;

interface BetaCitationCharLocationParam {
  type: "char_location";
  cited_text: string;
  document_index: number; // minimum: 0
  document_title: string | null; // minLength: 1, maxLength: 500
  end_char_index: number;
  start_char_index: number; // minimum: 0
}

interface BetaCitationPageLocationParam {
  type: "page_location";
  cited_text: string;
  document_index: number; // minimum: 0
  document_title: string | null; // minLength: 1, maxLength: 500
  end_page_number: number;
  start_page_number: number; // minimum: 1
}

interface BetaCitationContentBlockLocationParam {
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

interface BetaCitationWebSearchResultLocationParam {
  type: "web_search_result_location";
  cited_text: string;
  encrypted_index: string;
  title: string | null; // minLength: 1, maxLength: 512
  url: string; // minLength: 1
}

interface BetaCitationSearchResultLocationParam {
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

/** Start holding conversation state under this response's `id`. */
interface BetaThreadCreateParams {
  type: "create";
}

/** Resume from the response named by `previous_message_id`. */
interface BetaThreadContinueParams {
  type: "continue";
  /** The `id` of the previous response in this Thread. */
  previous_message_id: string;
}

/** The model will automatically decide whether to use tools. */
interface BetaToolChoiceAuto {
  type: "auto";
  /** Whether to disable parallel tool use. Defaults to `false`. If set to `true`, the model will output at most one tool use. */
  disable_parallel_tool_use?: boolean;
}

/** The model will use any available tools. */
interface BetaToolChoiceAny {
  type: "any";
  /** Whether to disable parallel tool use. Defaults to `false`. If set to `true`, the model will output exactly one tool use. */
  disable_parallel_tool_use?: boolean;
}

/** The model will use the specified tool with `tool_choice.name`. */
interface BetaToolChoiceTool {
  type: "tool";
  /** The name of the tool to use. */
  name: string;
  /** Whether to disable parallel tool use. Defaults to `false`. If set to `true`, the model will output exactly one tool use. */
  disable_parallel_tool_use?: boolean;
}

/** The model will not be allowed to use tools. */
interface BetaToolChoiceNone {
  type: "none";
}

/** A skill that was loaded in a container (response model). */
interface BetaContainerSkill {
  /** Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined) */
  type: "anthropic" | "custom";
  /** Skill ID */
  skill_id: string; // minLength: 1, maxLength: 64
  /** The resolved version: a skill version ID for custom skills. */
  version: string; // minLength: 1, maxLength: 64
}

interface BetaTextBlock {
  type: "text";
  /** Citations supporting the text block. The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`. */
  citations: Array<BetaTextCitation> | null;
  text: string;
}

interface BetaThinkingBlock {
  type: "thinking";
  /** A value used to verify that this thinking block was generated by Claude when it is passed back to the API. This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact. See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking?sdk_languages=typescript) for details. */
  signature: string;
  /** The text of Claude's thinking process for this block. */
  thinking: string;
}

interface BetaRedactedThinkingBlock {
  type: "redacted_thinking";
  /** The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content. Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation. See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking?sdk_languages=typescript#redacted-thinking-blocks) for details. */
  data: string;
}

interface BetaToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  input: Record<string, unknown>;
  name: string; // minLength: 1
  caller?: BetaDirectCaller | BetaServerToolCaller | BetaServerToolCaller20260120;
  /** For a toolset member tool_use, the toolset family. */
  toolset_name?: string | null; // minLength: 1, maxLength: 64, pattern: ^[a-zA-Z0-9_-]+$
}

interface BetaServerToolUseBlock {
  type: "server_tool_use";
  id: string; // pattern: ^srvtoolu_[a-zA-Z0-9_]+$
  input: Record<string, unknown>;
  /** - `"advisor"`: beta header: advisor-tool-2026-03-01 */
  name: "advisor" | "web_search" | "web_fetch" | "code_execution" | "bash_code_execution" | "text_editor_code_execution" | "tool_search_tool_regex" | "tool_search_tool_bm25";
  caller?: BetaDirectCaller | BetaServerToolCaller | BetaServerToolCaller20260120;
}

interface BetaWebSearchToolResultBlock {
  type: "web_search_tool_result";
  content: BetaWebSearchToolResultBlockContent;
  tool_use_id: string; // pattern: ^srvtoolu_[a-zA-Z0-9_]+$
  caller?: BetaDirectCaller | BetaServerToolCaller | BetaServerToolCaller20260120;
}

interface BetaWebFetchToolResultBlock {
  type: "web_fetch_tool_result";
  content: BetaWebFetchToolResultErrorBlock | BetaWebFetchBlock;
  tool_use_id: string; // pattern: ^srvtoolu_[a-zA-Z0-9_]+$
  caller?: BetaDirectCaller | BetaServerToolCaller | BetaServerToolCaller20260120;
}

interface BetaAdvisorToolResultBlock {
  type: "advisor_tool_result";
  content: BetaAdvisorToolResultError | BetaAdvisorResultBlock | BetaAdvisorRedactedResultBlock;
  tool_use_id: string; // pattern: ^srvtoolu_[a-zA-Z0-9_]+$
}

interface BetaCodeExecutionToolResultBlock {
  type: "code_execution_tool_result";
  content: BetaCodeExecutionToolResultBlockContent;
  tool_use_id: string; // pattern: ^srvtoolu_[a-zA-Z0-9_]+$
}

interface BetaBashCodeExecutionToolResultBlock {
  type: "bash_code_execution_tool_result";
  content: BetaBashCodeExecutionToolResultError | BetaBashCodeExecutionResultBlock;
  tool_use_id: string; // pattern: ^srvtoolu_[a-zA-Z0-9_]+$
}

interface BetaTextEditorCodeExecutionToolResultBlock {
  type: "text_editor_code_execution_tool_result";
  content: BetaTextEditorCodeExecutionToolResultError | BetaTextEditorCodeExecutionViewResultBlock | BetaTextEditorCodeExecutionCreateResultBlock | BetaTextEditorCodeExecutionStrReplaceResultBlock;
  tool_use_id: string; // pattern: ^srvtoolu_[a-zA-Z0-9_]+$
}

interface BetaToolSearchToolResultBlock {
  type: "tool_search_tool_result";
  content: BetaToolSearchToolResultError | BetaToolSearchToolSearchResultBlock;
  tool_use_id: string; // pattern: ^srvtoolu_[a-zA-Z0-9_]+$
}

interface BetaMCPToolUseBlock {
  type: "mcp_tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  input: Record<string, unknown>;
  /** The name of the MCP tool */
  name: string;
  /** The name of the MCP server */
  server_name: string;
}

interface BetaMCPToolResultBlock {
  type: "mcp_tool_result";
  content: string | Array<BetaTextBlock>;
  is_error: boolean; // default: false
  tool_use_id: string; // pattern: ^[a-zA-Z0-9_-]+$
}

/** Response model for a file uploaded to the container. */
interface BetaContainerUploadBlock {
  type: "container_upload";
  file_id: string;
}

/** A compaction block returned when autocompact is triggered. When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops. */
interface BetaCompactionBlock {
  type: "compaction";
  /** Summary of compacted content, or null if compaction failed */
  content: string | null;
  /** Opaque metadata from prior compaction, to be round-tripped verbatim */
  encrypted_content: string | null; // beta header: task-budgets-2026-03-13
  /** Signature over the summary, to be sent back with the block verbatim */
  signature?: string | null; // beta header: compact-2026-09-04
  /** The tool changes of the compacted range: the `tool_addition` and `tool_removal` blocks that take the request's `tools` to the tool set in effect at the end of the range, or `[]` when the range changed no tool. Absent when the server did not compute them. Send the block back unchanged. */
  tool_changes?: Array<BetaResponseToolAdditionBlock | BetaResponseToolRemovalBlock> | null; // beta header: inline-tools-2026-09-15
}

/** Marks the point in `content` where one model's output gives way to the next. One block appears per hop where a preceding model actually ran this turn and declined. A turn where no preceding model ran and declined has no such boundary and carries no block — the signal for whether a fallback model served the response is the presence of a `fallback_message` entry in `usage.iterations`, not this block. The block is treated like a server-tool content block for streaming: it arrives via the standard `content_block_start` / `content_block_stop` pair and carries no deltas. */
interface BetaFallbackBlock {
  type: "fallback";
  /** The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id. */
  from: BetaFallbackInfo;
  /** The fallback model producing the content that follows this block. Its `model` is always the canonical id. */
  to: BetaFallbackInfo;
  /** What caused the `from` model to hand over at this hop. */
  trigger: BetaFallbackRefusalTrigger;
}

/** The tool listing the server fetched from an MCP server while producing this response. Send the assistant message back unchanged, this block included, so later requests use this listing instead of asking the MCP server again. */
interface BetaMCPToolListingBlock {
  type: "mcp_tool_listing";
  mcp_server_name: string;
  tools: Array<BetaMCPTool>;
}

type BetaWebSearchToolResultBlockContent = BetaWebSearchToolResultError | Array<BetaWebSearchResultBlock>;

interface BetaWebSearchToolResultError {
  type: "web_search_tool_result_error";
  error_code: BetaWebSearchToolResultErrorCode;
}

interface BetaWebSearchResultBlock {
  type: "web_search_result";
  encrypted_content: string;
  page_age: string | null;
  title: string;
  url: string;
}

interface BetaWebFetchToolResultErrorBlock {
  type: "web_fetch_tool_result_error";
  error_code: BetaWebFetchToolResultErrorCode;
}

interface BetaWebFetchBlock {
  type: "web_fetch_result";
  content: BetaDocumentBlock;
  /** ISO 8601 timestamp when the content was retrieved */
  retrieved_at: string | null;
  /** Fetched content URL */
  url: string;
}

interface BetaDocumentBlock {
  type: "document";
  /** Citation configuration for the document */
  citations: BetaCitationConfig | null;
  source: BetaBase64PDFSource | BetaPlainTextSource;
  /** The title of the document */
  title: string | null;
}

interface BetaCitationConfig {
  enabled: boolean; // default: false
}

interface BetaAdvisorToolResultError {
  type: "advisor_tool_result_error";
  error_code: "max_uses_exceeded" | "prompt_too_long" | "too_many_requests" | "overloaded" | "unavailable" | "execution_time_exceeded" | "model_not_found";
}

interface BetaAdvisorResultBlock {
  type: "advisor_result";
  /** The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap. */
  stop_reason: string | null;
  text: string;
}

interface BetaAdvisorRedactedResultBlock {
  type: "advisor_redacted_result";
  /** Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify. */
  encrypted_content: string;
  /** The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). */
  stop_reason: string | null;
}

type BetaCodeExecutionToolResultBlockContent = BetaCodeExecutionToolResultError | BetaCodeExecutionResultBlock | BetaEncryptedCodeExecutionResultBlock;

interface BetaCodeExecutionToolResultError {
  type: "code_execution_tool_result_error";
  error_code: BetaCodeExecutionToolResultErrorCode;
}

interface BetaCodeExecutionResultBlock {
  type: "code_execution_result";
  content: Array<BetaCodeExecutionOutputBlock>;
  return_code: number;
  stderr: string;
  stdout: string;
}

/** The output and exit code of Python code that Claude ran with the code execution tool, with standard output in encrypted form. The API returns this block in place of `code_execution_result` when the code called the web search tool. See the [programmatic tool calling guide](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling?sdk_languages=typescript) to learn more about programmatic tool calling. */
interface BetaEncryptedCodeExecutionResultBlock {
  type: "encrypted_code_execution_result";
  content: Array<BetaCodeExecutionOutputBlock>;
  encrypted_stdout: string;
  return_code: number;
  stderr: string;
}

interface BetaCodeExecutionOutputBlock {
  type: "code_execution_output";
  file_id: string;
}

interface BetaBashCodeExecutionToolResultError {
  type: "bash_code_execution_tool_result_error";
  error_code: "invalid_tool_input" | "unavailable" | "too_many_requests" | "execution_time_exceeded" | "output_file_too_large";
}

interface BetaBashCodeExecutionResultBlock {
  type: "bash_code_execution_result";
  content: Array<BetaBashCodeExecutionOutputBlock>;
  return_code: number;
  stderr: string;
  stdout: string;
}

interface BetaBashCodeExecutionOutputBlock {
  type: "bash_code_execution_output";
  file_id: string;
}

interface BetaTextEditorCodeExecutionToolResultError {
  type: "text_editor_code_execution_tool_result_error";
  error_code: "invalid_tool_input" | "unavailable" | "too_many_requests" | "execution_time_exceeded" | "file_not_found";
  error_message: string | null;
}

interface BetaTextEditorCodeExecutionViewResultBlock {
  type: "text_editor_code_execution_view_result";
  content: string;
  file_type: "text" | "image" | "pdf";
  num_lines: number | null;
  start_line: number | null;
  total_lines: number | null;
}

interface BetaTextEditorCodeExecutionCreateResultBlock {
  type: "text_editor_code_execution_create_result";
  is_file_update: boolean;
}

interface BetaTextEditorCodeExecutionStrReplaceResultBlock {
  type: "text_editor_code_execution_str_replace_result";
  lines: Array<string> | null;
  new_lines: number | null;
  new_start: number | null;
  old_lines: number | null;
  old_start: number | null;
}

interface BetaToolSearchToolResultError {
  type: "tool_search_tool_result_error";
  error_code: "invalid_tool_input" | "unavailable" | "too_many_requests" | "execution_time_exceeded";
  error_message: string | null;
}

interface BetaToolSearchToolSearchResultBlock {
  type: "tool_search_tool_search_result";
  tool_references: Array<BetaToolReferenceBlock>;
}

interface BetaToolReferenceBlock {
  type: "tool_reference";
  tool_name: string; // minLength: 1, maxLength: 256, pattern: ^[a-zA-Z0-9_-]{1,256}$
}

/** An entry of a `compaction` block's `tool_changes`: a tool the compacted range made available, as a reference to a `tools` entry or MCP toolset, or as the tool definition in effect at the end of the range, by value. Send it back unchanged. */
interface BetaResponseToolAdditionBlock {
  type: "tool_addition";
  /** The tool made available: a reference to a `tools` entry or MCP toolset, or a `tool_definition` carrying the definition by value. */
  tool: BetaResponseToolChangeToolReference | BetaResponseToolChangeMCPToolReference | BetaResponseToolChangeMCPToolsetReference | BetaToolChangeToolDefinition;
}

/** An entry of a `compaction` block's `tool_changes`: a tool of the request's `tools` (or an MCP tool or toolset) that the compacted range withdrew. Send it back unchanged. */
interface BetaResponseToolRemovalBlock {
  type: "tool_removal";
  /** A reference to the withdrawn `tools` entry, MCP tool or MCP toolset. */
  tool: BetaResponseToolChangeToolReference | BetaResponseToolChangeMCPToolReference | BetaResponseToolChangeMCPToolsetReference;
}

/** Reference to a single tool, by the name the model uses to call it, as a `compaction` block's `tool_changes` entry reports it: a tool declared in `tools` or defined by an earlier `tool_addition` block. Send it back unchanged with the block. */
interface BetaResponseToolChangeToolReference {
  type: "tool_reference";
  name: string;
}

/** Reference to a single MCP tool, by its server and its name on that server, as a `compaction` block's `tool_changes` entry reports it. Send it back unchanged with the block. */
interface BetaResponseToolChangeMCPToolReference {
  type: "mcp_tool_reference";
  name: string;
  server_name: string;
}

/** Reference to every tool in the named MCP server's toolset, as a `compaction` block's `tool_changes` entry reports it. Send it back unchanged with the block. */
interface BetaResponseToolChangeMCPToolsetReference {
  type: "mcp_toolset_reference";
  server_name: string;
}

/** A tool defined by value, as a `compaction` block's `tool_changes` entry reports it: `definition` is the tool's definition as it was sent, in the form of a `tools` entry, without `cache_control`. Send it back unchanged with the block. */
interface BetaToolChangeToolDefinition {
  type: "tool_definition";
  definition: BetaResponseToolUnion;
}

type BetaResponseToolUnion =
  | BetaResponseTool
  | BetaToolBash20241022 // beta header: computer-use-2024-10-22
  | BetaToolBash20250124
  | BetaCodeExecutionTool20250522
  | BetaCodeExecutionTool20250825
  | BetaCodeExecutionTool20260120
  | BetaCodeExecutionTool20260521
  | BetaBrowserToolset20260801
  | BetaToolComputerUse20241022 // beta header: computer-use-2024-10-22
  | BetaMemoryTool20250818
  | BetaToolComputerUse20250124 // beta header: computer-use-2025-01-24
  | BetaToolTextEditor20241022 // beta header: computer-use-2024-10-22
  | BetaToolComputerUse20251124 // beta header: computer-use-2025-11-24
  | BetaComputerToolset20260801
  | BetaToolTextEditor20250124
  | BetaToolTextEditor20250429
  | BetaToolTextEditor20250728
  | BetaWebSearchTool20250305
  | BetaWebFetchTool20250910
  | BetaWebSearchTool20260209
  | BetaWebFetchTool20260209
  | BetaWebFetchTool20260309
  | BetaWebSearchTool20260318
  | BetaWebFetchTool20260318
  | BetaAdvisorTool20260301 // beta header: advisor-tool-2026-03-01
  | BetaToolSearchToolBm25_20251119
  | BetaToolSearchToolRegex20251119
  | BetaMCPToolset; // beta header: mcp-client-2025-11-20 or mcp-client-2026-09-15

/** A custom tool definition, as sent. */
interface BetaResponseTool {
  type?: "custom" | null;
  /** [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input. This defines the shape of the `input` that your tool accepts and that the model will produce. */
  input_schema: BetaResponseToolInputSchema;
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: string; // minLength: 1, maxLength: 128, pattern: ^[a-zA-Z0-9_-]{1,128}$
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
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

/** [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input. This defines the shape of the `input` that your tool accepts and that the model will produce. */
interface BetaResponseToolInputSchema {
  type: "object";
  properties?: Record<string, unknown> | null;
  required?: Array<string> | null;
}

/** Identifies one hop of a fallback transition. */
interface BetaFallbackInfo {
  /** The model that will complete your prompt. See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options. */
  model: Model;
}

/** The `from` model declined for policy reasons. */
interface BetaFallbackRefusalTrigger {
  type: "refusal";
  /**
   * The policy category that triggered the `from` model's refusal at this hop. `null` when the refusal doesn't map to a named category. Same vocabulary as `stop_details.category`.
   * - `"cyber"`: The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.
   * - `"bio"`: The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.
   * - `"frontier_llm"`: The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.
   * - `"reasoning_extraction"`: The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking?sdk_languages=typescript).
   * - `"general_harms"`: The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.
   */
  category: "cyber" | "bio" | "frontier_llm" | "reasoning_extraction" | "general_harms" | null;
}

/** A tool as an MCP server lists it: its name on that server, its description, and its input schema. */
interface BetaMCPTool {
  input_schema: Record<string, unknown>;
  name: string;
  description?: string;
}

type BetaTextCitation = BetaCitationCharLocation | BetaCitationPageLocation | BetaCitationContentBlockLocation | BetaCitationsWebSearchResultLocation | BetaCitationSearchResultLocation;

interface BetaCitationCharLocation {
  type: "char_location";
  cited_text: string;
  document_index: number; // minimum: 0
  document_title: string | null;
  end_char_index: number;
  file_id: string | null;
  start_char_index: number; // minimum: 0
}

interface BetaCitationPageLocation {
  type: "page_location";
  cited_text: string;
  document_index: number; // minimum: 0
  document_title: string | null;
  end_page_number: number;
  file_id: string | null;
  start_page_number: number; // minimum: 1
}

interface BetaCitationContentBlockLocation {
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

interface BetaCitationsWebSearchResultLocation {
  type: "web_search_result_location";
  cited_text: string;
  encrypted_index: string;
  title: string | null; // maxLength: 512
  url: string;
}

interface BetaCitationSearchResultLocation {
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

interface BetaClearToolUses20250919EditResponse {
  /** The type of context management edit applied. */
  type: "clear_tool_uses_20250919";
  /** Number of input tokens cleared by this edit. */
  cleared_input_tokens: number; // minimum: 0
  /** Number of tool uses that were cleared. */
  cleared_tool_uses: number; // minimum: 0
}

interface BetaClearThinking20251015EditResponse {
  /** The type of context management edit applied. */
  type: "clear_thinking_20251015";
  /** Number of input tokens cleared by this edit. */
  cleared_input_tokens: number; // minimum: 0
  /** Number of thinking turns that were cleared. */
  cleared_thinking_turns: number; // minimum: 0
}

type BetaCacheMissReason = BetaCacheMissModelChanged | BetaCacheMissSystemChanged | BetaCacheMissToolsChanged | BetaCacheMissMessagesChanged | BetaCacheMissPreviousMessageNotFound | BetaCacheMissUnavailable;

/** A `cache_miss_reason` for a request whose `model` or `speed` differs from the previous request's. See the [cache diagnostics guide](https://platform.claude.com/docs/en/build-with-claude/cache-diagnostics?sdk_languages=typescript#cache-miss-reason-types) to learn what to change for each reason. */
interface BetaCacheMissModelChanged {
  type: "model_changed";
  /** Approximate number of input tokens that would have been read from cache had the prefix matched the previous request. */
  cache_missed_input_tokens: number;
}

/** A `cache_miss_reason` for a request whose `system` differs from the previous request's. See the [cache diagnostics guide](https://platform.claude.com/docs/en/build-with-claude/cache-diagnostics?sdk_languages=typescript#cache-miss-reason-types) to learn what to change for each reason. */
interface BetaCacheMissSystemChanged {
  type: "system_changed";
  /** Approximate number of input tokens that would have been read from cache had the prefix matched the previous request. */
  cache_missed_input_tokens: number;
}

/** A `cache_miss_reason` for a request whose `tools` differ from the previous request's, for example because tools were added, removed, or reordered. See the [cache diagnostics guide](https://platform.claude.com/docs/en/build-with-claude/cache-diagnostics?sdk_languages=typescript#cache-miss-reason-types) to learn what to change for each reason. */
interface BetaCacheMissToolsChanged {
  type: "tools_changed";
  /** Approximate number of input tokens that would have been read from cache had the prefix matched the previous request. */
  cache_missed_input_tokens: number;
}

/** A `cache_miss_reason` for a request whose `messages` differ from the previous request's in an earlier entry, instead of only having entries appended. The `model`, `system`, and `tools` match. See the [cache diagnostics guide](https://platform.claude.com/docs/en/build-with-claude/cache-diagnostics?sdk_languages=typescript#cache-miss-reason-types) to learn what to change for each reason. */
interface BetaCacheMissMessagesChanged {
  type: "messages_changed";
  /** Approximate number of input tokens that would have been read from cache had the prefix matched the previous request. */
  cache_missed_input_tokens: number;
}

/** A `cache_miss_reason` for when the API doesn't have a stored record of the request that `diagnostics.previous_message_id` references. This doesn't mean that this request changed. See the [cache diagnostics guide](https://platform.claude.com/docs/en/build-with-claude/cache-diagnostics?sdk_languages=typescript#cache-miss-reason-types) to learn what to change for each reason. */
interface BetaCacheMissPreviousMessageNotFound {
  type: "previous_message_not_found";
}

/** A `cache_miss_reason` for when the API can't give a diagnosis. The request itself was processed normally. This includes a request whose `model`, `system`, and `tools` match the previous request's but whose other prompt-affecting parameters, such as `thinking` or `tool_choice`, differ. See the [cache diagnostics guide](https://platform.claude.com/docs/en/build-with-claude/cache-diagnostics?sdk_languages=typescript#cache-miss-reason-types) to learn what to change for each reason. */
interface BetaCacheMissUnavailable {
  type: "unavailable";
}

interface BetaCacheCreation {
  /** The number of input tokens used to create the 1 hour cache entry. */
  ephemeral_1h_input_tokens: number; // default: 0, minimum: 0
  /** The number of input tokens used to create the 5 minute cache entry. */
  ephemeral_5m_input_tokens: number; // default: 0, minimum: 0
}

/** Outcome of the `fallback_credit_token` presented on this request. */
interface BetaFallbackCreditUsage {
  /** Whether the fallback-credit reprice was applied to this response's billing. A union discriminated on `type`. `redeemed`: the retry is billed as if the conversation had been on the retry model all along — including when the resulting shift is zero because there was nothing to move. `not_applied`: no reprice was applied; the arm's `reason` says why. */
  status: BetaFallbackCreditRedeemed | BetaFallbackCreditNotApplied;
}

/**
 * Per-iteration token usage breakdown.
 *
 * Each entry represents one sampling iteration, with its own input/output token counts and cache statistics, discriminated by `type`. For `message` entries (model sampling iterations, such as the turns of a server-side tool use loop), this allows you to:
 *
 * - Calculate the context window size from the last `message` entry
 * - Understand token accumulation across server-side tool use loops
 *
 * A `compaction` entry reports the token usage of the compaction operation itself — the server-side request that summarizes the context being closed — NOT the size of the context that was compacted away, and its token counts can be much smaller than that closed context (for example, a compaction that closes a ~200k-token context can report only a few thousand tokens). Do not derive the context window size from a `compaction` entry, even when it is the last entry. A `compaction` entry's tokens are not included in the top-level `usage` fields. When an input-token trigger is in effect (the default — 150,000 tokens unless configured otherwise), each `compaction` entry closes a context that had reached at least that threshold, though the context can exceed it by the final iteration's output and tool results.
 * - `BetaAdvisorMessageIterationUsage`: beta header: advisor-tool-2026-03-01
 * - `BetaFallbackMessageIterationUsage`: beta header: server-side-fallback-2026-06-01 or server-side-fallback-2026-07-01
 */
type BetaIterationsUsage = Array<BetaMessageIterationUsage | BetaCompactionIterationUsage | BetaAdvisorMessageIterationUsage | BetaFallbackMessageIterationUsage> | null;

interface BetaOutputTokensDetails {
  /** Number of output tokens the model generated as internal reasoning, including the thinking-block delimiter tokens. Reflects the raw reasoning the model produced, not the (possibly shorter) summarized thinking text returned in the response body. It may differ from the model's exact generation count by a small number of tokens. Always ≤ `output_tokens`; `output_tokens - thinking_tokens` approximates the non-reasoning output. */
  thinking_tokens: number; // default: 0, minimum: 0
}

interface BetaServerToolUsage {
  /** The number of web fetch tool requests. */
  web_fetch_requests: number; // default: 0, minimum: 0
  /** The number of web search tool requests. */
  web_search_requests: number; // default: 0, minimum: 0
}

/** The reprice was applied: the retry is billed as if the conversation had been on the retry model all along. */
interface BetaFallbackCreditRedeemed {
  type: "redeemed";
}

/** No reprice was applied; `reason` says why. */
interface BetaFallbackCreditNotApplied {
  type: "not_applied";
  /** Why the reprice was not applied. A closed enum; additions to the redemption-check vocabulary arrive as deliberate schema updates. */
  reason: "body_mismatch" | "continuation_excluded" | "continuation_only" | "expired" | "invalid_target_model" | "not_enabled" | "reprice_unavailable" | "temporarily_unavailable" | "variant_fields_present" | "wrong_organization" | "wrong_platform" | "wrong_workspace";
  /** Request fields to remove before retrying, so the retry can redeem this token. Present exactly when `reason` is `variant_fields_present` — never null, never an empty array; absent otherwise. Fields are named only from your own request, and only after the sealed variant hash matched. A served best-effort retry has already been billed at normal price; nothing redeems retroactively, but a corrected re-send inside the token's five-minute window can still redeem. */
  remove_to_redeem?: Array<string> | null;
}

/** Token usage for a sampling iteration. */
interface BetaMessageIterationUsage {
  /** Usage for a sampling iteration */
  type: "message";
  /** Breakdown of cached tokens by TTL */
  cache_creation: BetaCacheCreation | null;
  /** The number of input tokens used to create the cache entry. */
  cache_creation_input_tokens: number; // default: 0, minimum: 0
  /** The number of input tokens read from the cache. */
  cache_read_input_tokens: number; // default: 0, minimum: 0
  /** The number of input tokens which were used. */
  input_tokens: number; // minimum: 0
  /** The model that will complete your prompt. See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options. */
  model: Model | null; // beta header: server-side-fallback-2026-06-01 or server-side-fallback-2026-07-01
  /** The number of output tokens which were used. */
  output_tokens: number; // minimum: 0
}

/** Token usage for a compaction iteration. */
interface BetaCompactionIterationUsage {
  /** Usage for a compaction iteration */
  type: "compaction";
  /** Breakdown of cached tokens by TTL */
  cache_creation: BetaCacheCreation | null;
  /** The number of input tokens used to create the cache entry. */
  cache_creation_input_tokens: number; // default: 0, minimum: 0
  /** The number of input tokens read from the cache. */
  cache_read_input_tokens: number; // default: 0, minimum: 0
  /** The number of input tokens which were used. */
  input_tokens: number; // minimum: 0
  /** The number of output tokens which were used. */
  output_tokens: number; // minimum: 0
}

/** Token usage for an advisor sub-inference iteration. */
interface BetaAdvisorMessageIterationUsage {
  /** Usage for an advisor sub-inference iteration */
  type: "advisor_message";
  /** Breakdown of cached tokens by TTL */
  cache_creation: BetaCacheCreation | null;
  /** The number of input tokens used to create the cache entry. */
  cache_creation_input_tokens: number; // default: 0, minimum: 0
  /** The number of input tokens read from the cache. */
  cache_read_input_tokens: number; // default: 0, minimum: 0
  /** The number of input tokens which were used. */
  input_tokens: number; // minimum: 0
  /** The model that will complete your prompt. See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options. */
  model: Model;
  /** The number of output tokens which were used. */
  output_tokens: number; // minimum: 0
}

/** Token usage for the fallback-model attempt of a server-side fallback request. The terminal entry of a fallback-served turn: when a fallback hop's output is the returned message, the entry for the iteration that completed it carries this type in place of `message`. A declined hop and the serving hop's earlier tool-loop iterations produce `message` entries. Whether a fallback model served the response is signalled by the presence of this entry in `usage.iterations`. */
interface BetaFallbackMessageIterationUsage {
  /** Usage for the fallback-model attempt that served the response */
  type: "fallback_message";
  /** Breakdown of cached tokens by TTL */
  cache_creation: BetaCacheCreation | null;
  /** The number of input tokens used to create the cache entry. */
  cache_creation_input_tokens: number; // default: 0, minimum: 0
  /** The number of input tokens read from the cache. */
  cache_read_input_tokens: number; // default: 0, minimum: 0
  /** The number of input tokens which were used. */
  input_tokens: number; // minimum: 0
  /** The model that will complete your prompt. See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options. */
  model: Model;
  /** The number of output tokens which were used. */
  output_tokens: number; // minimum: 0
}

interface BetaThinkingDroppedInputTransformation {
  /** Always `thinking_dropped` for this entry type. */
  type: "thinking_dropped";
  /** Where the removed block was in your request, as `messages.{i}.content.{j}`: `i` indexes the `messages` array you sent and `j` that message's `content` array — the same form error messages use. */
  path: string;
  /** Which binding check removed the block: `model_binding_mismatch` — it was created by a model whose reasoning the requested model may not read; `prefix_binding_mismatch` — the conversation before it differs from the conversation it was created in (the rest of that turn's consecutive thinking blocks are removed with it, each with this reason); `organization_binding_mismatch` — it was created under a different organization (an Anthropic organization, AWS account or Google Cloud project) and this organization is not one of its additional organizations; `end_user_binding_mismatch` — it was created for a different end user, or was removed by the consumer-organization binding. A block that would fail several checks reports one reason, in this order of precedence: `organization_binding_mismatch`, `end_user_binding_mismatch`, `model_binding_mismatch`, `prefix_binding_mismatch`. */
  reason: "model_binding_mismatch" | "prefix_binding_mismatch" | "organization_binding_mismatch" | "end_user_binding_mismatch";
}

interface BetaThinkingMismatchAllowedInputTransformation {
  /** Always `thinking_mismatch_allowed` for this entry type. */
  type: "thinking_mismatch_allowed";
  /** Where the block is in your request, as `messages.{i}.content.{j}`: `i` indexes the `messages` array you sent and `j` that message's `content` array — the same form error messages use. */
  path: string;
  /** Which binding check the block failed; the block was shown to the model all the same. Always `prefix_binding_mismatch` today — the conversation before the block differs from the conversation it was created in, or the block carries no record of one on a model that requires it. Were the check enforced for this request, the block would have been removed or the request rejected (`thinking.block_binding.prefix_mismatch_behavior`). A removal also takes the rest of that turn's consecutive thinking blocks, whereas here each block is checked on its own, so `thinking_mismatch_allowed` entries are a lower bound on what enforcement would remove. */
  reason: "model_binding_mismatch" | "prefix_binding_mismatch" | "organization_binding_mismatch" | "end_user_binding_mismatch";
}

interface Delta {
  /** Information about the container used in this request. This will be non-null if a container tool (e.g. code execution) was used. */
  container: BetaContainer | null;
  /** Structured information about why model output stopped. This is `null` when the `stop_reason` has no additional detail to report. */
  stop_details: BetaRefusalStopDetails | null;
  stop_reason: BetaStopReason | null;
  stop_sequence: string | null;
}

interface BetaMessageDeltaUsage {
  /** The cumulative number of input tokens used to create the cache entry. */
  cache_creation_input_tokens: number | null; // minimum: 0
  /** The cumulative number of input tokens read from the cache. */
  cache_read_input_tokens: number | null; // minimum: 0
  /** Outcome of the `fallback_credit_token` presented on this request. Present on every response to a non-batch request that carried a `fallback_credit_token`, in either redemption mode; absent otherwise (batch items accept and ignore the token and carry no outcome object). */
  fallback_credit: BetaFallbackCreditUsage | null; // beta header: fallback-credit-2026-07-01
  /** The cumulative number of input tokens which were used. */
  input_tokens: number | null; // minimum: 0
  /**
   * Per-iteration token usage breakdown.
   *
   * Each entry represents one sampling iteration, with its own input/output token counts and cache statistics, discriminated by `type`. For `message` entries (model sampling iterations, such as the turns of a server-side tool use loop), this allows you to:
   *
   * - Calculate the context window size from the last `message` entry
   * - Understand token accumulation across server-side tool use loops
   *
   * A `compaction` entry reports the token usage of the compaction operation itself — the server-side request that summarizes the context being closed — NOT the size of the context that was compacted away, and its token counts can be much smaller than that closed context (for example, a compaction that closes a ~200k-token context can report only a few thousand tokens). Do not derive the context window size from a `compaction` entry, even when it is the last entry. A `compaction` entry's tokens are not included in the top-level `usage` fields. When an input-token trigger is in effect (the default — 150,000 tokens unless configured otherwise), each `compaction` entry closes a context that had reached at least that threshold, though the context can exceed it by the final iteration's output and tool results.
   */
  iterations: BetaIterationsUsage | null; // beta header: compact-2026-01-12 or compact-2026-09-04 or advisor-tool-2026-03-01 or task-budgets-2026-03-13 or server-side-fallback-2026-06-01 or server-side-fallback-2026-07-01
  /** The cumulative number of output tokens which were used. */
  output_tokens: number;
  /** Breakdown of output tokens by category. `output_tokens` remains the inclusive, authoritative total used for billing. This object provides a read-only decomposition for observability — for example, how many of the billed output tokens were spent on internal reasoning that may have been summarized before being returned to you. */
  output_tokens_details: BetaOutputTokensDetails | null;
  /** The number of server tool requests. */
  server_tool_use: BetaServerToolUsage | null;
}

type BetaRawContentBlockDelta =
  | BetaTextDelta
  | BetaInputJSONDelta
  | BetaCitationsDelta
  | BetaThinkingDelta
  | BetaSignatureDelta
  | BetaCompactionContentBlockDelta; // beta header: compact-2026-01-12

interface BetaTextDelta {
  type: "text_delta";
  text: string;
}

interface BetaInputJSONDelta {
  type: "input_json_delta";
  partial_json: string;
}

interface BetaCitationsDelta {
  type: "citations_delta";
  citation: BetaCitationCharLocation | BetaCitationPageLocation | BetaCitationContentBlockLocation | BetaCitationsWebSearchResultLocation | BetaCitationSearchResultLocation;
}

interface BetaThinkingDelta {
  type: "thinking_delta";
  /** Per-frame increment of a coarse, running estimate of the tokens this thinking block has produced so far. Present whenever the `thinking-token-count-2026-05-13` beta is set; `null` unless `thinking.display` resolves to `"omitted"` and a count is due this frame. Sum the increments across `thinking_delta` frames on this block for a progress indicator. Each increment is a non-negative multiple of a fixed quantum and the cadence is rate-limited, so this is a deliberately lossy display hint, not a billable count; `usage.output_tokens` remains authoritative. */
  estimated_tokens: number | null; // beta header: thinking-token-count-2026-05-13
  /** The incremental `thinking` text for this content block. Concatenate the `thinking` values of successive `thinking_delta` events to assemble the block's full `thinking` value. */
  thinking: string;
}

interface BetaSignatureDelta {
  type: "signature_delta";
  /** The `signature` for this thinking block: an opaque value used to verify that the block was generated by Claude when it is passed back to the API. Delivered in a `signature_delta` event just before the block's `content_block_stop` event. */
  signature: string;
}

interface BetaCompactionContentBlockDelta {
  type: "compaction_delta";
  content: string | null;
  /** Opaque metadata from prior compaction, to be round-tripped verbatim */
  encrypted_content: string | null; // beta header: task-budgets-2026-03-13
}

interface BetaTool {
  type?: "custom" | null;
  /** [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input. This defines the shape of the `input` that your tool accepts and that the model will produce. */
  input_schema: InputSchema;
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: string; // minLength: 1, maxLength: 128, pattern: ^[a-zA-Z0-9_-]{1,128}$
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
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

interface BetaToolBash20241022 {
  type: "bash_20241022";
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "bash";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  input_examples?: Array<Record<string, unknown>>;
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
}

interface BetaToolBash20250124 {
  type: "bash_20250124";
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "bash";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  input_examples?: Array<Record<string, unknown>>;
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
}

interface BetaCodeExecutionTool20250522 {
  type: "code_execution_20250522";
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "code_execution";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
}

interface BetaCodeExecutionTool20250825 {
  type: "code_execution_20250825";
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "code_execution";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
}

/** A `tools` entry for the code execution tool, version `code_execution_20260120`. It adds REPL state persistence to version `code_execution_20250825`. REPL state persistence applies with programmatic tool calling. With it, the Python interpreter state, such as variable bindings, persists across requests that reuse the container. See the [code execution tool guide](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool?sdk_languages=typescript#tool-versions) to learn what each tool version adds. */
interface BetaCodeExecutionTool20260120 {
  type: "code_execution_20260120";
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "code_execution";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
}

/** Code execution tool with REPL state persistence. */
interface BetaCodeExecutionTool20260521 {
  type: "code_execution_20260521";
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "code_execution";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
}

/** The browser toolset: a single `tools[]` entry (carrying no `name`) that declares the browser tool family. The model is served the family's tool with any members disabled via `configs` removed from its schema. */
interface BetaBrowserToolset20260801 {
  type: "browser_toolset_20260801";
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
  /** Sparse per-member overrides, keyed by member name. Absent, null, and {} are equivalent; a member's defaults apply wherever its key is absent. */
  configs?: BetaBrowserToolsetConfigs | null;
}

interface BetaToolComputerUse20241022 {
  type: "computer_20241022";
  /** The height of the display in pixels. */
  display_height_px: number; // minimum: 1
  /** The width of the display in pixels. */
  display_width_px: number; // minimum: 1
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "computer";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  /** The X11 display number (e.g. 0, 1) for the display. */
  display_number?: number | null; // minimum: 0
  input_examples?: Array<Record<string, unknown>>;
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
}

interface BetaMemoryTool20250818 {
  type: "memory_20250818";
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "memory";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  input_examples?: Array<Record<string, unknown>>;
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
}

interface BetaToolComputerUse20250124 {
  type: "computer_20250124";
  /** The height of the display in pixels. */
  display_height_px: number; // minimum: 1
  /** The width of the display in pixels. */
  display_width_px: number; // minimum: 1
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "computer";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  /** The X11 display number (e.g. 0, 1) for the display. */
  display_number?: number | null; // minimum: 0
  input_examples?: Array<Record<string, unknown>>;
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
}

interface BetaToolTextEditor20241022 {
  type: "text_editor_20241022";
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "str_replace_editor";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  input_examples?: Array<Record<string, unknown>>;
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
}

interface BetaToolComputerUse20251124 {
  type: "computer_20251124";
  /** The height of the display in pixels. */
  display_height_px: number; // minimum: 1
  /** The width of the display in pixels. */
  display_width_px: number; // minimum: 1
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "computer";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  /** The X11 display number (e.g. 0, 1) for the display. */
  display_number?: number | null; // minimum: 0
  /** Whether to enable an action to take a zoomed-in screenshot of the screen. */
  enable_zoom?: boolean;
  input_examples?: Array<Record<string, unknown>>;
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
}

/** The computer toolset: a single `tools[]` entry (carrying no `name`) that declares the computer tool family. The model is served the family's tool with any members disabled via `configs` removed from its schema. Every member is enabled by default, zoom included. The single-tool options `display_number` and `enable_zoom` are not fields of a toolset entry — it carries only `type`, `configs`, and `cache_control`; zoom is controlled via `configs.zoom.enabled`. */
interface BetaComputerToolset20260801 {
  type: "computer_toolset_20260801";
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
  /** Sparse per-member overrides, keyed by member name. Absent, null, and {} are equivalent; a member's defaults apply wherever its key is absent. */
  configs?: BetaComputerToolsetConfigs | null;
}

interface BetaToolTextEditor20250124 {
  type: "text_editor_20250124";
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "str_replace_editor";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  input_examples?: Array<Record<string, unknown>>;
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
}

interface BetaToolTextEditor20250429 {
  type: "text_editor_20250429";
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "str_replace_based_edit_tool";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  input_examples?: Array<Record<string, unknown>>;
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
}

interface BetaToolTextEditor20250728 {
  type: "text_editor_20250728";
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "str_replace_based_edit_tool";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  input_examples?: Array<Record<string, unknown>>;
  /** Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file. */
  max_characters?: number | null; // minimum: 1
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
}

interface BetaWebSearchTool20250305 {
  type: "web_search_20250305";
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "web_search";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`. */
  allowed_domains?: Array<string> | null;
  /** If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`. */
  blocked_domains?: Array<string> | null;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  /** Maximum number of times the tool can be used in the API request. */
  max_uses?: number | null; // minimum: 1
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
  /** Parameters for the user's location. Used to provide more relevant search results. */
  user_location?: BetaUserLocation | null;
}

interface BetaWebFetchTool20250910 {
  type: "web_fetch_20250910";
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "web_fetch";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** List of domains to allow fetching from */
  allowed_domains?: Array<string> | null;
  /** List of domains to block fetching from */
  blocked_domains?: Array<string> | null;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
  /** Citations configuration for fetched documents. Citations are disabled by default. */
  citations?: BetaCitationsConfigParam | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  /** Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs. */
  max_content_tokens?: number | null; // minimum: 1
  /** Maximum number of times the tool can be used in the API request. */
  max_uses?: number | null; // minimum: 1
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
  /** Which sources contribute to the set of URLs the tool may fetch. Omitted means every source. */
  url_sources?: BetaWebFetchURLSources | null;
}

interface BetaWebSearchTool20260209 {
  type: "web_search_20260209";
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "web_search";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`. */
  allowed_domains?: Array<string> | null;
  /** If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`. */
  blocked_domains?: Array<string> | null;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  /** Maximum number of times the tool can be used in the API request. */
  max_uses?: number | null; // minimum: 1
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
  /** Parameters for the user's location. Used to provide more relevant search results. */
  user_location?: BetaUserLocation | null;
}

interface BetaWebFetchTool20260209 {
  type: "web_fetch_20260209";
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "web_fetch";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** List of domains to allow fetching from */
  allowed_domains?: Array<string> | null;
  /** List of domains to block fetching from */
  blocked_domains?: Array<string> | null;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
  /** Citations configuration for fetched documents. Citations are disabled by default. */
  citations?: BetaCitationsConfigParam | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  /** Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs. */
  max_content_tokens?: number | null; // minimum: 1
  /** Maximum number of times the tool can be used in the API request. */
  max_uses?: number | null; // minimum: 1
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
  /** Which sources contribute to the set of URLs the tool may fetch. Omitted means every source. */
  url_sources?: BetaWebFetchURLSources | null;
}

/** Web fetch tool with use_cache parameter for bypassing cached content. */
interface BetaWebFetchTool20260309 {
  type: "web_fetch_20260309";
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "web_fetch";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** List of domains to allow fetching from */
  allowed_domains?: Array<string> | null;
  /** List of domains to block fetching from */
  blocked_domains?: Array<string> | null;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
  /** Citations configuration for fetched documents. Citations are disabled by default. */
  citations?: BetaCitationsConfigParam | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  /** Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs. */
  max_content_tokens?: number | null; // minimum: 1
  /** Maximum number of times the tool can be used in the API request. */
  max_uses?: number | null; // minimum: 1
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
  /** Which sources contribute to the set of URLs the tool may fetch. Omitted means every source. */
  url_sources?: BetaWebFetchURLSources | null;
  /** Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources. */
  use_cache?: boolean;
}

interface BetaWebSearchTool20260318 {
  type: "web_search_20260318";
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "web_search";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`. */
  allowed_domains?: Array<string> | null;
  /** If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`. */
  blocked_domains?: Array<string> | null;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  /** Maximum number of times the tool can be used in the API request. */
  max_uses?: number | null; // minimum: 1
  /** How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn. */
  response_inclusion?: "full" | "excluded";
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
  /** Parameters for the user's location. Used to provide more relevant search results. */
  user_location?: BetaUserLocation | null;
}

interface BetaWebFetchTool20260318 {
  type: "web_fetch_20260318";
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "web_fetch";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** List of domains to allow fetching from */
  allowed_domains?: Array<string> | null;
  /** List of domains to block fetching from */
  blocked_domains?: Array<string> | null;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
  /** Citations configuration for fetched documents. Citations are disabled by default. */
  citations?: BetaCitationsConfigParam | null;
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
  url_sources?: BetaWebFetchURLSources | null;
  /** Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources. */
  use_cache?: boolean;
}

interface BetaAdvisorTool20260301 {
  type: "advisor_20260301";
  /** The model that will complete your prompt. See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options. */
  model: Model;
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "advisor";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
  /** Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached. */
  caching?: BetaCacheControlEphemeral | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  /** Bounds the advisor's total output (thinking + text) per call. When the advisor hits this cap, the returned advisor_result or advisor_redacted_result block carries stop_reason='max_tokens', and a truncation note is appended to the advice text the worker model sees (inside the encrypted blob in redacted mode). When set, the API also passes the advisor its remaining-token budget, so the advisor shapes its output toward the cap. When omitted, the advisor model's default output cap applies and the API doesn't pass a budget. */
  max_tokens?: number | null; // minimum: 1024
  /** Maximum number of times the tool can be used in the API request. */
  max_uses?: number | null; // minimum: 1
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
}

interface BetaToolSearchToolBm25_20251119 {
  type: "tool_search_tool_bm25_20251119" | "tool_search_tool_bm25";
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "tool_search_tool_bm25";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
}

interface BetaToolSearchToolRegex20251119 {
  type: "tool_search_tool_regex_20251119" | "tool_search_tool_regex";
  /** Name of the tool. This is how the tool will be called by the model and in `tool_use` blocks. */
  name: "tool_search_tool_regex";
  allowed_callers?: Array<"direct" | "code_execution_20250825" | "code_execution_20260120" | "code_execution_20260521">;
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
  /** If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search. */
  defer_loading?: boolean;
  /** When true, guarantees schema validation on tool names and inputs */
  strict?: boolean;
}

/** Configuration for a group of tools from an MCP server. Allows configuring enabled status and defer_loading for all tools from an MCP server, with optional per-tool overrides. */
interface BetaMCPToolset {
  type: "mcp_toolset";
  /** Name of the MCP server to configure tools for */
  mcp_server_name: string; // minLength: 1, maxLength: 255
  /** Create a cache control breakpoint at this content block. */
  cache_control?: BetaCacheControlEphemeral | null;
  /** Configuration overrides for specific tools, keyed by tool name */
  configs?: Record<string, BetaMCPToolConfig> | null;
  /** Default configuration applied to all tools from this server */
  default_config?: BetaMCPToolDefaultConfig;
  /** The server's tool listing, pinned: when present, the server is not asked for its tools before sampling and exactly these entries, with `default_config` and `configs` applied, are the toolset's tools. Copy it from the `mcp_tool_listing` block of an earlier response. */
  tools?: Array<BetaMCPToolParam> | null; // beta header: mcp-client-2026-09-15
}

interface InputSchema {
  type: "object";
  properties?: Record<string, unknown> | null;
  required?: Array<string> | null;
}

/** Per-member configuration for `computer_toolset_20260801`: one optional field per member tool, keyed by the member name — the same name the member's `tool_use` blocks carry. Every member is an accepted key, and a member's defaults apply wherever its key is absent. Unknown keys are rejected: the field set is this toolset version's complete member set. */
interface BetaComputerToolsetConfigs {
  /** `type`'s config overrides. */
  type?: BetaComputerTypeConfig | null;
  /** `cursor_position`'s config overrides. */
  cursor_position?: BetaComputerCursorPositionConfig | null;
  /** `double_click`'s config overrides. */
  double_click?: BetaComputerDoubleClickConfig | null;
  /** `hold_key`'s config overrides. */
  hold_key?: BetaComputerHoldKeyConfig | null;
  /** `key`'s config overrides. */
  key?: BetaComputerKeyConfig | null;
  /** `left_click`'s config overrides. */
  left_click?: BetaComputerLeftClickConfig | null;
  /** `left_click_drag`'s config overrides. */
  left_click_drag?: BetaComputerLeftClickDragConfig | null;
  /** `left_mouse_down`'s config overrides. */
  left_mouse_down?: BetaComputerLeftMouseDownConfig | null;
  /** `left_mouse_up`'s config overrides. */
  left_mouse_up?: BetaComputerLeftMouseUpConfig | null;
  /** `middle_click`'s config overrides. */
  middle_click?: BetaComputerMiddleClickConfig | null;
  /** `mouse_move`'s config overrides. */
  mouse_move?: BetaComputerMouseMoveConfig | null;
  /** `right_click`'s config overrides. */
  right_click?: BetaComputerRightClickConfig | null;
  /** `screenshot`'s config overrides. */
  screenshot?: BetaComputerScreenshotConfig | null;
  /** `scroll`'s config overrides. */
  scroll?: BetaComputerScrollConfig | null;
  /** `triple_click`'s config overrides. */
  triple_click?: BetaComputerTripleClickConfig | null;
  /** `wait`'s config overrides. */
  wait?: BetaComputerWaitConfig | null;
  /** `zoom`'s config overrides. */
  zoom?: BetaComputerZoomConfig | null;
}

/** `type`'s config overrides. */
interface BetaComputerTypeConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `cursor_position`'s config overrides. */
interface BetaComputerCursorPositionConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `double_click`'s config overrides. */
interface BetaComputerDoubleClickConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `hold_key`'s config overrides. */
interface BetaComputerHoldKeyConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `key`'s config overrides. */
interface BetaComputerKeyConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `left_click`'s config overrides. */
interface BetaComputerLeftClickConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `left_click_drag`'s config overrides. */
interface BetaComputerLeftClickDragConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `left_mouse_down`'s config overrides. */
interface BetaComputerLeftMouseDownConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `left_mouse_up`'s config overrides. */
interface BetaComputerLeftMouseUpConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `middle_click`'s config overrides. */
interface BetaComputerMiddleClickConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `mouse_move`'s config overrides. */
interface BetaComputerMouseMoveConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `right_click`'s config overrides. */
interface BetaComputerRightClickConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `screenshot`'s config overrides. */
interface BetaComputerScreenshotConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `scroll`'s config overrides. */
interface BetaComputerScrollConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `triple_click`'s config overrides. */
interface BetaComputerTripleClickConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `wait`'s config overrides. */
interface BetaComputerWaitConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `zoom`'s config overrides. */
interface BetaComputerZoomConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

interface BetaUserLocation {
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
interface BetaWebFetchURLSources {
  /** Which client tools' results contribute fetchable URLs: "all", "none", or an only or except list of client tool names from tools[]. */
  client_tool_results?: BetaWebFetchURLSourceAll | BetaWebFetchURLSourceNone | BetaWebFetchURLSourceOnly | BetaWebFetchURLSourceExcept;
  /** Which server tools' results contribute fetchable URLs: "all", "none", or an only or except list of server tool names from tools[]; only web_search and web_fetch results ever contribute. */
  server_tool_results?: BetaWebFetchURLSourceAll | BetaWebFetchURLSourceNone | BetaWebFetchURLSourceOnly | BetaWebFetchURLSourceExcept;
  /** Whether URLs in user messages are fetchable: "all" or "none". */
  user_input?: BetaWebFetchURLSourceAll | BetaWebFetchURLSourceNone;
}

/** The `url_sources` variant under which a source contributes in full: every result of the tool filter's source, or all user input. */
interface BetaWebFetchURLSourceAll {
  type: "all";
}

/** The `url_sources` variant under which a source contributes nothing: no result of the tool filter's source, or no user input. */
interface BetaWebFetchURLSourceNone {
  type: "none";
}

/** The tool filter variant under which only the named tools' results contribute. */
interface BetaWebFetchURLSourceOnly {
  type: "only";
  tools: Array<BetaWebFetchURLSourceToolReference>;
}

/** The tool filter variant under which every result but the named tools' contributes. */
interface BetaWebFetchURLSourceExcept {
  type: "except";
  tools: Array<BetaWebFetchURLSourceToolReference>;
}

/** One entry of a tool filter's `tools`: it must name a tool declared in this request's `tools[]`. */
interface BetaWebFetchURLSourceToolReference {
  type: "tool_reference";
  name: string;
}

/** Configuration for a specific tool in an MCP toolset. */
interface BetaMCPToolConfig {
  defer_loading?: boolean;
  enabled?: boolean;
}

/** Default configuration for tools in an MCP toolset. */
interface BetaMCPToolDefaultConfig {
  defer_loading?: boolean;
  enabled?: boolean;
}

/** Per-member configuration for `browser_toolset_20260801`: one optional field per member tool, keyed by the member name — the same name the member's `tool_use` blocks carry. Every member is an accepted key, and a member's defaults apply wherever its key is absent. Unknown keys are rejected: the field set is this toolset version's complete member set. */
interface BetaBrowserToolsetConfigs {
  /** `type`'s config overrides. */
  type?: BetaBrowserTypeConfig | null;
  /** `close_tab`'s config overrides. */
  close_tab?: BetaBrowserCloseTabConfig | null;
  /** `double_click`'s config overrides. */
  double_click?: BetaBrowserDoubleClickConfig | null;
  /** `file_upload`'s config overrides. */
  file_upload?: BetaBrowserFileUploadConfig | null;
  /** `find`'s config overrides. */
  find?: BetaBrowserFindConfig | null;
  /** `form_input`'s config overrides. */
  form_input?: BetaBrowserFormInputConfig | null;
  /** `get_page_text`'s config overrides. */
  get_page_text?: BetaBrowserGetPageTextConfig | null;
  /** `hold_key`'s config overrides. */
  hold_key?: BetaBrowserHoldKeyConfig | null;
  /** `hover`'s config overrides. */
  hover?: BetaBrowserHoverConfig | null;
  /** `javascript_exec`'s config overrides. */
  javascript_exec?: BetaBrowserJavascriptExecConfig | null;
  /** `key`'s config overrides. */
  key?: BetaBrowserKeyConfig | null;
  /** `left_click`'s config overrides. */
  left_click?: BetaBrowserLeftClickConfig | null;
  /** `left_click_drag`'s config overrides. */
  left_click_drag?: BetaBrowserLeftClickDragConfig | null;
  /** `left_mouse_down`'s config overrides. */
  left_mouse_down?: BetaBrowserLeftMouseDownConfig | null;
  /** `left_mouse_up`'s config overrides. */
  left_mouse_up?: BetaBrowserLeftMouseUpConfig | null;
  /** `list_tabs`'s config overrides. */
  list_tabs?: BetaBrowserListTabsConfig | null;
  /** `middle_click`'s config overrides. */
  middle_click?: BetaBrowserMiddleClickConfig | null;
  /** `mouse_move`'s config overrides. */
  mouse_move?: BetaBrowserMouseMoveConfig | null;
  /** `navigate`'s config overrides. */
  navigate?: BetaBrowserNavigateConfig | null;
  /** `new_tab`'s config overrides. */
  new_tab?: BetaBrowserNewTabConfig | null;
  /** `read_console`'s config overrides. */
  read_console?: BetaBrowserReadConsoleConfig | null;
  /** `read_network`'s config overrides. */
  read_network?: BetaBrowserReadNetworkConfig | null;
  /** `read_page`'s config overrides. */
  read_page?: BetaBrowserReadPageConfig | null;
  /** `right_click`'s config overrides. */
  right_click?: BetaBrowserRightClickConfig | null;
  /** `screenshot`'s config overrides. */
  screenshot?: BetaBrowserScreenshotConfig | null;
  /** `scroll`'s config overrides. */
  scroll?: BetaBrowserScrollConfig | null;
  /** `scroll_to`'s config overrides. */
  scroll_to?: BetaBrowserScrollToConfig | null;
  /** `switch_tab`'s config overrides. */
  switch_tab?: BetaBrowserSwitchTabConfig | null;
  /** `triple_click`'s config overrides. */
  triple_click?: BetaBrowserTripleClickConfig | null;
  /** `wait`'s config overrides. */
  wait?: BetaBrowserWaitConfig | null;
  /** `zoom`'s config overrides. */
  zoom?: BetaBrowserZoomConfig | null;
}

/** `type`'s config overrides. */
interface BetaBrowserTypeConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `close_tab`'s config overrides. */
interface BetaBrowserCloseTabConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `double_click`'s config overrides. */
interface BetaBrowserDoubleClickConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `file_upload`'s config overrides. */
interface BetaBrowserFileUploadConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `find`'s config overrides. */
interface BetaBrowserFindConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `form_input`'s config overrides. */
interface BetaBrowserFormInputConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `get_page_text`'s config overrides. */
interface BetaBrowserGetPageTextConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `hold_key`'s config overrides. */
interface BetaBrowserHoldKeyConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `hover`'s config overrides. */
interface BetaBrowserHoverConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `javascript_exec`'s config overrides. */
interface BetaBrowserJavascriptExecConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `key`'s config overrides. */
interface BetaBrowserKeyConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `left_click`'s config overrides. */
interface BetaBrowserLeftClickConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `left_click_drag`'s config overrides. */
interface BetaBrowserLeftClickDragConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `left_mouse_down`'s config overrides. */
interface BetaBrowserLeftMouseDownConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `left_mouse_up`'s config overrides. */
interface BetaBrowserLeftMouseUpConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `list_tabs`'s config overrides. */
interface BetaBrowserListTabsConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `middle_click`'s config overrides. */
interface BetaBrowserMiddleClickConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `mouse_move`'s config overrides. */
interface BetaBrowserMouseMoveConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `navigate`'s config overrides. */
interface BetaBrowserNavigateConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `new_tab`'s config overrides. */
interface BetaBrowserNewTabConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `read_console`'s config overrides. */
interface BetaBrowserReadConsoleConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `read_network`'s config overrides. */
interface BetaBrowserReadNetworkConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `read_page`'s config overrides. */
interface BetaBrowserReadPageConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `right_click`'s config overrides. */
interface BetaBrowserRightClickConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `screenshot`'s config overrides. */
interface BetaBrowserScreenshotConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `scroll`'s config overrides. */
interface BetaBrowserScrollConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `scroll_to`'s config overrides. */
interface BetaBrowserScrollToConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `switch_tab`'s config overrides. */
interface BetaBrowserSwitchTabConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `triple_click`'s config overrides. */
interface BetaBrowserTripleClickConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `wait`'s config overrides. */
interface BetaBrowserWaitConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}

/** `zoom`'s config overrides. */
interface BetaBrowserZoomConfig {
  /** Defer loading for this member. Must resolve to the same value on every enabled member of the toolset. */
  defer_loading?: boolean | null;
  /** Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema. */
  enabled?: boolean | null;
}
```

## Count tokens in a Message

- Signature: `client.beta.messages.countTokens(params: MessageCountTokensParams, options?: RequestOptions): BetaMessageTokensCount`
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

const betaMessageTokensCount = await client.beta.messages.countTokens({
  messages: [{ content: "Hello, world", role: "user" }],
  model: "claude-opus-5-5"
});

console.log(betaMessageTokensCount.context_management);
```

### Example response (200)

```json
{
  "context_management": {
    "original_input_tokens": 0
  },
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
  messages: Array<BetaMessageParam>;
  /** The model that will complete your prompt. See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options. */
  model: Model;
  /** Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request. */
  cache_control?: BetaCacheControlEphemeral | null;
  /** Compaction configuration. When set on `POST /v1/messages`, the request is a compaction request: the conversation in `messages` is summarized and the response holds only the resulting `compaction` block (`stop_reason` `"compaction"`), which later requests send first in `messages` in place of the messages it summarizes. `POST /v1/messages/count_tokens` accepts this parameter and ignores it: the count it returns is for the conversation in `messages` as sent. Cannot be combined with `context_management`. */
  compaction?: BetaCompactionConfig | null; // beta header: compact-2026-09-04
  /** Context management configuration. This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not. */
  context_management?: BetaContextManagementConfig | null; // beta header: context-management-2025-06-27 or compact-2026-01-12
  /** MCP servers to be utilized in this request */
  mcp_servers?: Array<BetaRequestMCPServerURLDefinition>; // maxItems: 20, beta header: mcp-client-2025-04-04 or mcp-client-2025-11-20 or mcp-client-2026-09-15
  /** Configuration options for the model's output, such as the output format. */
  output_config?: BetaOutputConfig;
  /** The inference speed mode for this request. `"fast"` enables high output-tokens-per-second inference. Some models require the `fast-mode-2026-02-01` beta header for any `speed` value. See [fast mode](https://platform.claude.com/docs/en/build-with-claude/fast-mode?sdk_languages=typescript) for which models. */
  speed?: "standard" | "fast" | null;
  /** System prompt. A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices?sdk_languages=typescript#give-claude-a-role). */
  system?: string | Array<BetaTextBlockParam>;
  /** Configuration for Claude's thinking. With `{"type": "adaptive"}`, Claude decides when and how much to think. With `{"type": "enabled"}` (manual extended thinking), you set a `budget_tokens` of at least 1,024. Thinking tokens count toward your `max_tokens` limit. Which `type` values are accepted, and what happens when you omit `thinking`, depend on the model. See [thinking](https://platform.claude.com/docs/en/build-with-claude/thinking?sdk_languages=typescript#configuring-thinking) for each model's behavior. */
  thinking?: BetaThinkingConfigParam;
  /** How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all. */
  tool_choice?: BetaToolChoice;
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
   * - `BetaToolBash20241022`: beta header: computer-use-2024-10-22
   * - `BetaToolComputerUse20241022`: beta header: computer-use-2024-10-22
   * - `BetaToolComputerUse20250124`: beta header: computer-use-2025-01-24
   * - `BetaToolTextEditor20241022`: beta header: computer-use-2024-10-22
   * - `BetaToolComputerUse20251124`: beta header: computer-use-2025-11-24
   * - `BetaAdvisorTool20260301`: beta header: advisor-tool-2026-03-01
   * - `BetaMCPToolset`: beta header: mcp-client-2025-11-20 or mcp-client-2026-09-15
   */
  tools?: Array<BetaTool | BetaToolBash20241022 | BetaToolBash20250124 | BetaCodeExecutionTool20250522 | BetaCodeExecutionTool20250825 | BetaCodeExecutionTool20260120 | BetaCodeExecutionTool20260521 | BetaBrowserToolset20260801 | BetaToolComputerUse20241022 | BetaMemoryTool20250818 | BetaToolComputerUse20250124 | BetaToolTextEditor20241022 | BetaToolComputerUse20251124 | BetaComputerToolset20260801 | BetaToolTextEditor20250124 | BetaToolTextEditor20250429 | BetaToolTextEditor20250728 | BetaWebSearchTool20250305 | BetaWebFetchTool20250910 | BetaWebSearchTool20260209 | BetaWebFetchTool20260209 | BetaWebFetchTool20260309 | BetaWebSearchTool20260318 | BetaWebFetchTool20260318 | BetaAdvisorTool20260301 | BetaToolSearchToolBm25_20251119 | BetaToolSearchToolRegex20251119 | BetaMCPToolset>;
  /** Optional header to specify the beta version(s) you want to use. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** The user profile ID to attribute this request to. Use when acting on behalf of a party other than your organization. */
  user_profile_id?: string; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
  /**
   * Deprecated: Use `output_config.format` instead. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs?sdk_languages=typescript)
   *
   * A schema to specify Claude's output format in responses. This parameter will be removed in a future release.
   * @deprecated
   */
  output_format?: BetaJSONOutputFormat | null; // beta header: structured-outputs-2025-11-13
}
````

### Returns

```ts
interface BetaMessageTokensCount {
  /** Information about context management applied to the message. */
  context_management: BetaCountTokensContextManagementResponse | null; // beta header: context-management-2025-06-27 or compact-2026-01-12 or compact-2026-09-04
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
interface BetaCountTokensContextManagementResponse {
  /** The original token count before context management was applied */
  original_input_tokens: number;
}
```

## Messages › Batches

### Create a Message Batch

- Signature: `client.beta.messages.batches.create(params: BatchCreateParams, options?: RequestOptions): BetaMessageBatch`
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

const betaMessageBatch = await client.beta.messages.batches.create({
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

console.log(betaMessageBatch.id);
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
  /** Optional header to specify the beta version(s) you want to use. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** The user profile ID to attribute the requests in this batch to. Use when acting on behalf of a party other than your organization. Applies to every request in the batch; an individual request whose `user_profile_id` body field conflicts with this header is errored. */
  user_profile_id?: string; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

#### Returns

```ts
interface BetaMessageBatch {
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
  request_counts: BetaMessageBatchRequestCounts;
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

interface BetaMessageBatchRequestCounts {
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
  messages: Array<BetaMessageParam>;
  /** The model that will complete your prompt. See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options. */
  model: Model;
  /** Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request. */
  cache_control?: BetaCacheControlEphemeral | null;
  /** Compaction configuration. When set on `POST /v1/messages`, the request is a compaction request: the conversation in `messages` is summarized and the response holds only the resulting `compaction` block (`stop_reason` `"compaction"`), which later requests send first in `messages` in place of the messages it summarizes. `POST /v1/messages/count_tokens` accepts this parameter and ignores it: the count it returns is for the conversation in `messages` as sent. Cannot be combined with `context_management`. */
  compaction?: BetaCompactionConfig | null; // beta header: compact-2026-09-04
  /** Container identifier for reuse across requests. */
  container?: BetaContainerParams | string | null;
  /** Context management configuration. This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not. */
  context_management?: BetaContextManagementConfig | null; // beta header: context-management-2025-06-27 or compact-2026-01-12
  /** Request-level diagnostics. Supply `previous_message_id` to have the response include `diagnostics.cache_miss_reason` explaining any prompt-cache divergence from that prior request. */
  diagnostics?: BetaDiagnosticsParam | null;
  /** The `fallback_credit_token` from a prior refusal's `stop_details`. When a preceding request was refused and returned a `fallback_credit_token`, pass that code here on the retry to have the retry's cache-creation tokens for the prefix that was warm on the refused model billed at the cache-read rate. Must be redeemed by the same organization and workspace, with the same request body (optionally extended by one appended `assistant` message whose content is the partial text — with any trailing whitespace stripped from the final text block — and paired server-tool blocks streamed before the refusal; the appended-assistant form is not available for requests with `output_format` set or forced `tool_choice`), on an eligible fallback model, on the same platform, and within 5 minutes of the refusal; a mismatch is a 400. A token minted mid-server-tool-loop whose partial content was continuable may only be redeemed with the appended-assistant form — if an exact-body retry is rejected with a 400 saying the token must be redeemed by continuing the partial response, retry with the appended-assistant form instead. When the appended-assistant form is used on a model that otherwise disallows assistant-turn prefill, this token also authorizes that one prefill. */
  fallback_credit_token?: string | BetaFallbackCreditTokenParam | null; // beta header: fallback-credit-2026-06-01 or fallback-credit-2026-07-01 or server-side-fallback-2026-06-01 or server-side-fallback-2026-07-01
  /** Opt-in server-side retry on one or more substitute models when the requested model declines for policy reasons. Tried in order: if the first entry also declines, the second is tried, and so on. Some models don't support fallbacks; on those models, a list of fallback models returns a 400 error. See [Server-side fallback](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback?sdk_languages=typescript#server-side-fallback). The string "default" requests the requested model's server-defined default fallback configuration. On a model that doesn't support fallbacks, the request runs on the requested model alone, so a declined request stays declined. */
  fallbacks?: BetaFallbacksParam | null; // beta header: server-side-fallback-2026-06-01 or server-side-fallback-2026-07-01
  /** Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used. */
  inference_geo?: string | null;
  /** MCP servers to be utilized in this request */
  mcp_servers?: Array<BetaRequestMCPServerURLDefinition>; // maxItems: 20, beta header: mcp-client-2025-04-04 or mcp-client-2025-11-20 or mcp-client-2026-09-15
  /** An object describing metadata about the request. */
  metadata?: BetaMetadata;
  /** Configuration options for the model's output, such as the output format. */
  output_config?: BetaOutputConfig;
  /** Determines whether to use priority capacity (if available) or standard capacity for this request. Anthropic offers different levels of service for your API requests. See [service-tiers](https://platform.claude.com/docs/en/api/service-tiers?sdk_languages=typescript) for details. */
  service_tier?: "auto" | "standard_only";
  /** The inference speed mode for this request. `"fast"` enables high output-tokens-per-second inference. Some models require the `fast-mode-2026-02-01` beta header for any `speed` value. See [fast mode](https://platform.claude.com/docs/en/build-with-claude/fast-mode?sdk_languages=typescript) for which models. */
  speed?: "standard" | "fast" | null;
  /** Custom text sequences that will cause the model to stop generating. Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`. If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence. */
  stop_sequences?: Array<string>;
  /** Whether to incrementally stream the response using server-sent events. When `true`, SDKs return a raw event stream. In the TypeScript, Python and Ruby SDKs, the recommended way to stream is `messages.stream()`. It sets `stream` for you and accumulates the events into the final message. See [Streaming with SDKs](https://platform.claude.com/docs/en/build-with-claude/streaming?sdk_languages=typescript#streaming-with-sdks) for an example in each language. */
  stream?: boolean;
  /** System prompt. A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices?sdk_languages=typescript#give-claude-a-role). */
  system?: string | Array<BetaTextBlockParam>;
  /** Configuration for Claude's thinking. With `{"type": "adaptive"}`, Claude decides when and how much to think. With `{"type": "enabled"}` (manual extended thinking), you set a `budget_tokens` of at least 1,024. Thinking tokens count toward your `max_tokens` limit. Which `type` values are accepted, and what happens when you omit `thinking`, depend on the model. See [thinking](https://platform.claude.com/docs/en/build-with-claude/thinking?sdk_languages=typescript#configuring-thinking) for each model's behavior. */
  thinking?: BetaThinkingConfigParam;
  /** Server-held conversation state (a Thread). `{"type": "create"}` asks the server to hold this conversation's state under the response's `id`; `{"type": "continue", "previous_message_id": ...}` resumes from a previous response so only the new turn's messages are sent. The response shape is unchanged. */
  thread?: BetaMessageThreadParam | null; // beta header: message-threads-2026-08-12
  /** How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all. */
  tool_choice?: BetaToolChoice;
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
  tools?: Array<BetaToolUnion>;
  /**
   * Deprecated: Use `output_config.format` instead. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs?sdk_languages=typescript)
   *
   * A schema to specify Claude's output format in responses. This parameter will be removed in a future release.
   * @deprecated
   */
  output_format?: BetaJSONOutputFormat | null; // beta header: structured-outputs-2025-11-13
}
````

### Retrieve a Message Batch

- Signature: `client.beta.messages.batches.retrieve(messageBatchID: string, params?: BatchRetrieveParams, options?: RequestOptions): BetaMessageBatch`
- Endpoint: `GET /v1/messages/batches/{message_batch_id}`

This endpoint is idempotent and can be used to poll for Message Batch completion. To access the results of a Message Batch, make a request to the `results_url` field in the response.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing?sdk_languages=typescript)

#### Example request

```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaMessageBatch = await client.beta.messages.batches.retrieve("message_batch_id");

console.log(betaMessageBatch.id);
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
  /** Optional header to specify the beta version(s) you want to use. */
  betas?: Array<AnthropicBeta>; // header parameter
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

- Signature: `client.beta.messages.batches.list(params?: BatchListParams, options?: RequestOptions): Page<BetaMessageBatch>`
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
for await (const betaMessageBatch of client.beta.messages.batches.list()) {
  console.log(betaMessageBatch.id);
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
  /** Optional header to specify the beta version(s) you want to use. */
  betas?: Array<AnthropicBeta>; // header parameter
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

- Signature: `client.beta.messages.batches.cancel(messageBatchID: string, params?: BatchCancelParams, options?: RequestOptions): BetaMessageBatch`
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

const betaMessageBatch = await client.beta.messages.batches.cancel("message_batch_id");

console.log(betaMessageBatch.id);
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
  /** Optional header to specify the beta version(s) you want to use. */
  betas?: Array<AnthropicBeta>; // header parameter
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

- Signature: `client.beta.messages.batches.delete(messageBatchID: string, params?: BatchDeleteParams, options?: RequestOptions): BetaDeletedMessageBatch`
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

const betaDeletedMessageBatch = await client.beta.messages.batches.delete("message_batch_id");

console.log(betaDeletedMessageBatch.id);
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
  /** Optional header to specify the beta version(s) you want to use. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

#### Returns

```ts
interface BetaDeletedMessageBatch {
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

- Signature: `client.beta.messages.batches.results(messageBatchID: string, params?: BatchResultsParams, options?: RequestOptions): JSONLDecoder<BetaMessageBatchIndividualResponse>`
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

const stream = await client.beta.messages.batches.results("message_batch_id");
for await (const betaMessageBatchIndividualResponse of stream) {
  console.log(betaMessageBatchIndividualResponse.custom_id);
}
```

#### Parameters

```ts
/** ID of the Message Batch. */
messageBatchID: string; // path parameter

interface BatchResultsParams {
  /** Optional header to specify the beta version(s) you want to use. */
  betas?: Array<AnthropicBeta>; // header parameter
  /** Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`). Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace. */
  workspace_id?: string; // header parameter
}
```

#### Returns

```ts
/** This is a single line in the response `.jsonl` file and does not represent the response as a whole. */
interface BetaMessageBatchIndividualResponse {
  /** Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order. Must be unique for each request within the Message Batch. */
  custom_id: string;
  /** Processing result for this request. Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration. */
  result: BetaMessageBatchResult;
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
type BetaMessageBatchResult = BetaMessageBatchSucceededResult | BetaMessageBatchErroredResult | BetaMessageBatchCanceledResult | BetaMessageBatchExpiredResult;

interface BetaMessageBatchSucceededResult {
  type: "succeeded";
  message: BetaMessage;
}

interface BetaMessageBatchErroredResult {
  type: "errored";
  error: BetaErrorResponse;
}

interface BetaMessageBatchCanceledResult {
  type: "canceled";
}

interface BetaMessageBatchExpiredResult {
  type: "expired";
}

interface BetaErrorResponse {
  type: "error";
  error: BetaError;
  request_id: string | null;
}

type BetaError = BetaInvalidRequestError | BetaAuthenticationError | BetaBillingError | BetaPermissionError | BetaNotFoundError | BetaRateLimitError | BetaGatewayTimeoutError | BetaAPIError | BetaOverloadedError;

interface BetaInvalidRequestError {
  /** The broad category of the error. */
  type: "invalid_request_error";
  /** A human-readable explanation of the error. Its wording can change, so don't match on it. */
  message: string; // default: Invalid request
}

interface BetaAuthenticationError {
  /** The broad category of the error. */
  type: "authentication_error";
  /** A human-readable explanation of the error. Its wording can change, so don't match on it. */
  message: string; // default: Authentication error
}

interface BetaBillingError {
  /** The broad category of the error. */
  type: "billing_error";
  /** A human-readable explanation of the error. Its wording can change, so don't match on it. */
  message: string; // default: Billing error
}

interface BetaPermissionError {
  /** The broad category of the error. */
  type: "permission_error";
  /** A human-readable explanation of the error. Its wording can change, so don't match on it. */
  message: string; // default: Permission denied
}

interface BetaNotFoundError {
  /** The broad category of the error. */
  type: "not_found_error";
  /** A human-readable explanation of the error. Its wording can change, so don't match on it. */
  message: string; // default: Not found
}

interface BetaRateLimitError {
  /** The broad category of the error. */
  type: "rate_limit_error";
  /** A human-readable explanation of the error. Its wording can change, so don't match on it. */
  message: string; // default: Rate limited
}

interface BetaGatewayTimeoutError {
  /** The broad category of the error. */
  type: "timeout_error";
  /** A human-readable explanation of the error. Its wording can change, so don't match on it. */
  message: string; // default: Request timeout
}

interface BetaAPIError {
  /** The broad category of the error. */
  type: "api_error";
  /** A human-readable explanation of the error. Its wording can change, so don't match on it. */
  message: string; // default: Internal server error
}

interface BetaOverloadedError {
  /** The broad category of the error. */
  type: "overloaded_error";
  /** A human-readable explanation of the error. Its wording can change, so don't match on it. */
  message: string; // default: Overloaded
}
```

## Types

```ts
/** Where to act: either a viewport coordinate or an element reference. */
type BetaBrowserClickTarget = BetaBrowserCoordinateTarget | BetaBrowserRefTarget;

/** Close the tab with the given tab_id. */
interface BetaBrowserCloseTabInput {
  /** The tab to close. */
  tab_id: string;
}

interface BetaBrowserCloseTabToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Close the tab with the given tab_id. */
  input: BetaBrowserCloseTabInput;
  name: "close_tab";
  toolset_name: "browser";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

/** A point in the browser viewport, in viewport pixels (the same frame as a full-viewport screenshot). */
interface BetaBrowserCoordinateTarget {
  type: "coordinate";
  /** Pixels from the left edge of the viewport. */
  x: number; // minimum: 0
  /** Pixels from the top edge of the viewport. */
  y: number; // minimum: 0
}

/** Double left-click at a viewport coordinate or on an element by reference. */
interface BetaBrowserDoubleClickInput {
  /** Where to act: either a viewport coordinate or an element reference. */
  target: BetaBrowserClickTarget;
  /** Optional modifier key chord to hold for the duration of this action (e.g. "shift", "ctrl+shift", "cmd+alt"). */
  modifiers?: string | null;
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BetaBrowserDoubleClickToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Double left-click at a viewport coordinate or on an element by reference. */
  input: BetaBrowserDoubleClickInput;
  name: "double_click";
  toolset_name: "browser";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

/** Set the value of a file-input element to one or more files. The target must be an element reference; at least one of paths or document_ids is required. */
interface BetaBrowserFileUploadInput {
  /** An element on the page, identified by a reference from a prior `read_page` or `find` result. References are scoped to the tab that produced them and become stale after navigation or a major re-render. */
  target: BetaBrowserRefTarget;
  /** References to files the harness has staged, for deployments where the browser executor cannot read the caller's filesystem. */
  document_ids?: Array<string> | null; // minItems: 1
  /** File paths on the browser executor's filesystem. */
  paths?: Array<string> | null; // minItems: 1
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BetaBrowserFileUploadToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Set the value of a file-input element to one or more files. The target must be an element reference; at least one of paths or document_ids is required. */
  input: BetaBrowserFileUploadInput;
  name: "file_upload";
  toolset_name: "browser";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

/** Find elements matching a natural-language description (e.g. "search bar", "add to cart button") and return up to 20 matches with element references. */
interface BetaBrowserFindInput {
  /** Natural-language description of the element(s) to find. */
  query: string;
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BetaBrowserFindToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Find elements matching a natural-language description (e.g. "search bar", "add to cart button") and return up to 20 matches with element references. */
  input: BetaBrowserFindInput;
  name: "find";
  toolset_name: "browser";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

/** Set the value of a form element (input, textarea, select, checkbox). Use a boolean for checkboxes, an option value or text for selects. */
interface BetaBrowserFormInputInput {
  /** An element on the page, identified by a reference from a prior `read_page` or `find` result. References are scoped to the tab that produced them and become stale after navigation or a major re-render. */
  target: BetaBrowserRefTarget;
  /** The value to set. */
  value: BetaBrowserFormInputValue;
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BetaBrowserFormInputToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Set the value of a form element (input, textarea, select, checkbox). Use a boolean for checkboxes, an option value or text for selects. */
  input: BetaBrowserFormInputInput;
  name: "form_input";
  toolset_name: "browser";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

type BetaBrowserFormInputValue = string | number | boolean;

/** Return the page's visible text content as plain text, prioritizing article content. Suited to articles, documentation, and other text-heavy pages. */
interface BetaBrowserGetPageTextInput {
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BetaBrowserGetPageTextToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Return the page's visible text content as plain text, prioritizing article content. Suited to articles, documentation, and other text-heavy pages. */
  input: BetaBrowserGetPageTextInput;
  name: "get_page_text";
  toolset_name: "browser";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

/** Hold a key or key chord down for a duration, then release it. Uses the same key names and "+" chord syntax as the key action. */
interface BetaBrowserHoldKeyInput {
  /** Seconds to hold the key down (maximum 30). */
  duration: number; // minimum: 0, maximum: 30
  /** The key or chord to hold. */
  text: string;
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BetaBrowserHoldKeyToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Hold a key or key chord down for a duration, then release it. Uses the same key names and "+" chord syntax as the key action. */
  input: BetaBrowserHoldKeyInput;
  name: "hold_key";
  toolset_name: "browser";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

/** Move the cursor to a coordinate or element without clicking. */
interface BetaBrowserHoverInput {
  /** Where to act: either a viewport coordinate or an element reference. */
  target: BetaBrowserClickTarget;
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BetaBrowserHoverToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Move the cursor to a coordinate or element without clicking. */
  input: BetaBrowserHoverInput;
  name: "hover";
  toolset_name: "browser";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

/** Execute JavaScript in the page context and return the value of the last expression. The code runs with access to the DOM, `window`, and page variables. Write the expression you want evaluated — do NOT use `return`. */
interface BetaBrowserJavascriptExecInput {
  /** JavaScript to execute in the page context. */
  text: string;
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BetaBrowserJavascriptExecToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Execute JavaScript in the page context and return the value of the last expression. The code runs with access to the DOM, `window`, and page variables. Write the expression you want evaluated — do NOT use `return`. */
  input: BetaBrowserJavascriptExecInput;
  name: "javascript_exec";
  toolset_name: "browser";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

/** Press a key or key chord. Use "+" to combine modifiers with a key (e.g. "ctrl+a", "cmd+shift+p") and space to sequence presses (e.g. "Backspace Backspace Delete"). Common names like "Return", "Tab", "Escape", "BackSpace" are supported. */
interface BetaBrowserKeyInput {
  /** The key, chord, or space-separated sequence to press. */
  text: string;
  /** Number of times to repeat. Default 1. */
  repeat?: number | null; // minimum: 1, maximum: 100
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BetaBrowserKeyToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Press a key or key chord. Use "+" to combine modifiers with a key (e.g. "ctrl+a", "cmd+shift+p") and space to sequence presses (e.g. "Backspace Backspace Delete"). Common names like "Return", "Tab", "Escape", "BackSpace" are supported. */
  input: BetaBrowserKeyInput;
  name: "key";
  toolset_name: "browser";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

/** Press at `from`, drag to `target`, release. Both must be coordinate targets. */
interface BetaBrowserLeftClickDragInput {
  /** A point in the browser viewport, in viewport pixels (the same frame as a full-viewport screenshot). */
  from: BetaBrowserCoordinateTarget;
  /** A point in the browser viewport, in viewport pixels (the same frame as a full-viewport screenshot). */
  target: BetaBrowserCoordinateTarget;
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BetaBrowserLeftClickDragToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Press at `from`, drag to `target`, release. Both must be coordinate targets. */
  input: BetaBrowserLeftClickDragInput;
  name: "left_click_drag";
  toolset_name: "browser";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

/** Left-click at a viewport coordinate or on an element by reference. */
interface BetaBrowserLeftClickInput {
  /** Where to act: either a viewport coordinate or an element reference. */
  target: BetaBrowserClickTarget;
  /** Optional modifier key chord to hold for the duration of this action (e.g. "shift", "ctrl+shift", "cmd+alt"). */
  modifiers?: string | null;
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BetaBrowserLeftClickToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Left-click at a viewport coordinate or on an element by reference. */
  input: BetaBrowserLeftClickInput;
  name: "left_click";
  toolset_name: "browser";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

/** Press and hold the left mouse button at a viewport coordinate. Pair with left_mouse_up to perform a custom drag. */
interface BetaBrowserLeftMouseDownInput {
  /** A point in the browser viewport, in viewport pixels (the same frame as a full-viewport screenshot). */
  target: BetaBrowserCoordinateTarget;
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BetaBrowserLeftMouseDownToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Press and hold the left mouse button at a viewport coordinate. Pair with left_mouse_up to perform a custom drag. */
  input: BetaBrowserLeftMouseDownInput;
  name: "left_mouse_down";
  toolset_name: "browser";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

/** Release the left mouse button at a viewport coordinate. */
interface BetaBrowserLeftMouseUpInput {
  /** A point in the browser viewport, in viewport pixels (the same frame as a full-viewport screenshot). */
  target: BetaBrowserCoordinateTarget;
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BetaBrowserLeftMouseUpToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Release the left mouse button at a viewport coordinate. */
  input: BetaBrowserLeftMouseUpInput;
  name: "left_mouse_up";
  toolset_name: "browser";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

/** List all open tabs with each tab's tab_id, title, and URL. */
interface BetaBrowserListTabsInput {}

interface BetaBrowserListTabsToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** List all open tabs with each tab's tab_id, title, and URL. */
  input: BetaBrowserListTabsInput;
  name: "list_tabs";
  toolset_name: "browser";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

/** Middle-click at a viewport coordinate or on an element by reference. */
interface BetaBrowserMiddleClickInput {
  /** Where to act: either a viewport coordinate or an element reference. */
  target: BetaBrowserClickTarget;
  /** Optional modifier key chord to hold for the duration of this action (e.g. "shift", "ctrl+shift", "cmd+alt"). */
  modifiers?: string | null;
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BetaBrowserMiddleClickToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Middle-click at a viewport coordinate or on an element by reference. */
  input: BetaBrowserMiddleClickInput;
  name: "middle_click";
  toolset_name: "browser";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

/** Move the pointer to a viewport coordinate without clicking. */
interface BetaBrowserMouseMoveInput {
  /** A point in the browser viewport, in viewport pixels (the same frame as a full-viewport screenshot). */
  target: BetaBrowserCoordinateTarget;
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BetaBrowserMouseMoveToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Move the pointer to a viewport coordinate without clicking. */
  input: BetaBrowserMouseMoveInput;
  name: "mouse_move";
  toolset_name: "browser";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

/** Navigate to a URL, or go back/forward/reload in history. The protocol may be omitted (defaults to https://). */
interface BetaBrowserNavigateInput {
  /** The URL to navigate to, or "back" / "forward" / "reload" for history navigation. */
  url: string;
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BetaBrowserNavigateToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Navigate to a URL, or go back/forward/reload in history. The protocol may be omitted (defaults to https://). */
  input: BetaBrowserNavigateInput;
  name: "navigate";
  toolset_name: "browser";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

/** Open a new empty tab and return its tab_id. */
interface BetaBrowserNewTabInput {}

interface BetaBrowserNewTabToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Open a new empty tab and return its tab_id. */
  input: BetaBrowserNewTabInput;
  name: "new_tab";
  toolset_name: "browser";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

/** Return console output (log entries, errors, warnings) accumulated since the driver attached to the tab and since the last read, one line per entry. An empty result does not mean no traffic for a tab that predates attach. */
interface BetaBrowserReadConsoleInput {
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BetaBrowserReadConsoleToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Return console output (log entries, errors, warnings) accumulated since the driver attached to the tab and since the last read, one line per entry. An empty result does not mean no traffic for a tab that predates attach. */
  input: BetaBrowserReadConsoleInput;
  name: "read_console";
  toolset_name: "browser";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

/** Return the network requests (method, URL, status, MIME type, timing) recorded since the driver attached to the tab and since the last read, one line per entry. An empty result does not mean no traffic for a tab that predates attach. */
interface BetaBrowserReadNetworkInput {
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BetaBrowserReadNetworkToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Return the network requests (method, URL, status, MIME type, timing) recorded since the driver attached to the tab and since the last read, one line per entry. An empty result does not mean no traffic for a tab that predates attach. */
  input: BetaBrowserReadNetworkInput;
  name: "read_network";
  toolset_name: "browser";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

type BetaBrowserReadPageFilter = "all" | "interactive";

/** Return a structured accessibility tree of the page (or the subtree rooted at `ref`), with element references like [ref_7] that can be used as targets on later actions. Output is capped at 50,000 characters — narrow with `ref` or a smaller `depth` when exceeded. */
interface BetaBrowserReadPageInput {
  /** Maximum tree depth. Default 15. */
  depth?: number | null; // minimum: 1
  /** Which elements to include. Omitted: every visible element. "interactive": interactive elements only. "all": additionally includes off-viewport elements. */
  filter?: BetaBrowserReadPageFilter | null;
  /** Element reference to read a subtree from. Omit to read from the page root. */
  ref?: string | null;
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BetaBrowserReadPageToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Return a structured accessibility tree of the page (or the subtree rooted at `ref`), with element references like [ref_7] that can be used as targets on later actions. Output is capped at 50,000 characters — narrow with `ref` or a smaller `depth` when exceeded. */
  input: BetaBrowserReadPageInput;
  name: "read_page";
  toolset_name: "browser";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

/** An element on the page, identified by a reference from a prior `read_page` or `find` result. References are scoped to the tab that produced them and become stale after navigation or a major re-render. */
interface BetaBrowserRefTarget {
  type: "ref";
  /** An element reference (e.g. "ref_7") returned by a prior `read_page` or `find` result. */
  ref: string;
}

/** Right-click at a viewport coordinate or on an element by reference. */
interface BetaBrowserRightClickInput {
  /** Where to act: either a viewport coordinate or an element reference. */
  target: BetaBrowserClickTarget;
  /** Optional modifier key chord to hold for the duration of this action (e.g. "shift", "ctrl+shift", "cmd+alt"). */
  modifiers?: string | null;
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BetaBrowserRightClickToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Right-click at a viewport coordinate or on an element by reference. */
  input: BetaBrowserRightClickInput;
  name: "right_click";
  toolset_name: "browser";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

/** Capture the current browser viewport. */
interface BetaBrowserScreenshotInput {
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BetaBrowserScreenshotToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Capture the current browser viewport. */
  input: BetaBrowserScreenshotInput;
  name: "screenshot";
  toolset_name: "browser";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

type BetaBrowserScrollDirection = "up" | "down" | "left" | "right";

/** Scroll at a viewport position. `target` must be a coordinate target. */
interface BetaBrowserScrollInput {
  scroll_direction: BetaBrowserScrollDirection;
  /** A point in the browser viewport, in viewport pixels (the same frame as a full-viewport screenshot). */
  target: BetaBrowserCoordinateTarget;
  /** Scroll-wheel notches (1–10). Default 3. */
  scroll_amount?: number | null; // minimum: 1, maximum: 10
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

/** Scroll an element into view. */
interface BetaBrowserScrollToInput {
  /** An element on the page, identified by a reference from a prior `read_page` or `find` result. References are scoped to the tab that produced them and become stale after navigation or a major re-render. */
  target: BetaBrowserRefTarget;
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BetaBrowserScrollToToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Scroll an element into view. */
  input: BetaBrowserScrollToInput;
  name: "scroll_to";
  toolset_name: "browser";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

interface BetaBrowserScrollToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Scroll at a viewport position. `target` must be a coordinate target. */
  input: BetaBrowserScrollInput;
  name: "scroll";
  toolset_name: "browser";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

/** Make the tab with the given tab_id the active tab — the tab that actions without a tab_id apply to. */
interface BetaBrowserSwitchTabInput {
  /** The tab to switch to. */
  tab_id: string;
}

interface BetaBrowserSwitchTabToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Make the tab with the given tab_id the active tab — the tab that actions without a tab_id apply to. */
  input: BetaBrowserSwitchTabInput;
  name: "switch_tab";
  toolset_name: "browser";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

type BetaBrowserToolUseBlock = BetaBrowserNavigateToolUseBlock | BetaBrowserListTabsToolUseBlock | BetaBrowserNewTabToolUseBlock | BetaBrowserSwitchTabToolUseBlock | BetaBrowserCloseTabToolUseBlock | BetaBrowserReadPageToolUseBlock | BetaBrowserGetPageTextToolUseBlock | BetaBrowserReadConsoleToolUseBlock | BetaBrowserReadNetworkToolUseBlock | BetaBrowserFindToolUseBlock | BetaBrowserFormInputToolUseBlock | BetaBrowserFileUploadToolUseBlock | BetaBrowserScrollToToolUseBlock | BetaBrowserScreenshotToolUseBlock | BetaBrowserZoomToolUseBlock | BetaBrowserLeftClickToolUseBlock | BetaBrowserRightClickToolUseBlock | BetaBrowserMiddleClickToolUseBlock | BetaBrowserDoubleClickToolUseBlock | BetaBrowserTripleClickToolUseBlock | BetaBrowserHoverToolUseBlock | BetaBrowserLeftClickDragToolUseBlock | BetaBrowserLeftMouseDownToolUseBlock | BetaBrowserLeftMouseUpToolUseBlock | BetaBrowserMouseMoveToolUseBlock | BetaBrowserScrollToolUseBlock | BetaBrowserTypeToolUseBlock | BetaBrowserKeyToolUseBlock | BetaBrowserHoldKeyToolUseBlock | BetaBrowserWaitToolUseBlock | BetaBrowserJavascriptExecToolUseBlock;

/** Triple left-click at a viewport coordinate or on an element by reference (typically selects a line or paragraph). */
interface BetaBrowserTripleClickInput {
  /** Where to act: either a viewport coordinate or an element reference. */
  target: BetaBrowserClickTarget;
  /** Optional modifier key chord to hold for the duration of this action (e.g. "shift", "ctrl+shift", "cmd+alt"). */
  modifiers?: string | null;
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BetaBrowserTripleClickToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Triple left-click at a viewport coordinate or on an element by reference (typically selects a line or paragraph). */
  input: BetaBrowserTripleClickInput;
  name: "triple_click";
  toolset_name: "browser";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

/** Type a literal string at the current focus. */
interface BetaBrowserTypeInput {
  /** The text to type. */
  text: string;
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BetaBrowserTypeToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Type a literal string at the current focus. */
  input: BetaBrowserTypeInput;
  name: "type";
  toolset_name: "browser";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

/** Pause for the given duration. */
interface BetaBrowserWaitInput {
  /** Seconds to wait (maximum 30). */
  duration: number; // minimum: 0, maximum: 30
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BetaBrowserWaitToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Pause for the given duration. */
  input: BetaBrowserWaitInput;
  name: "wait";
  toolset_name: "browser";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

/** Return a cropped screenshot of the given viewport region, scaled up for closer inspection — useful for small icons, buttons, or text. Coordinates are in the same viewport-pixel space as a full screenshot. */
interface BetaBrowserZoomInput {
  /** [x0, y0, x1, y1] in viewport pixels. */
  region: Array<number>; // minItems: 4, maxItems: 4
  /** Tab to act on. Defaults to the active tab when omitted. */
  tab_id?: string | null;
}

interface BetaBrowserZoomToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Return a cropped screenshot of the given viewport region, scaled up for closer inspection — useful for small icons, buttons, or text. Coordinates are in the same viewport-pixel space as a full screenshot. */
  input: BetaBrowserZoomInput;
  name: "zoom";
  toolset_name: "browser";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

/** Get the current (x, y) pixel coordinate of the cursor. */
interface BetaComputerCursorPositionInput {}

interface BetaComputerCursorPositionToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Get the current (x, y) pixel coordinate of the cursor. */
  input: BetaComputerCursorPositionInput;
  name: "cursor_position";
  toolset_name: "computer";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

/** Double-click the left mouse button at the specified (x, y) pixel coordinate, or the current cursor position if `coordinate` is omitted. */
interface BetaComputerDoubleClickInput {
  /** (x, y): x pixels from the left edge, y pixels from the top edge. */
  coordinate?: Array<number> | null; // minItems: 2, maxItems: 2
  /** Optional key combination to hold down during this action (e.g. "ctrl", "shift", "ctrl+shift"). */
  text?: string | null;
}

interface BetaComputerDoubleClickToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Double-click the left mouse button at the specified (x, y) pixel coordinate, or the current cursor position if `coordinate` is omitted. */
  input: BetaComputerDoubleClickInput;
  name: "double_click";
  toolset_name: "computer";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

/** Hold down a key or key-combination for a specified duration. Uses the same key syntax as `key`. */
interface BetaComputerHoldKeyInput {
  /** Duration to hold the key, in seconds. */
  duration: number; // maximum: 300
  /** The key or key-combination to hold. */
  text: string;
}

interface BetaComputerHoldKeyToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Hold down a key or key-combination for a specified duration. Uses the same key syntax as `key`. */
  input: BetaComputerHoldKeyInput;
  name: "hold_key";
  toolset_name: "computer";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

/** Press a key or key-combination on the keyboard. Use "+" to combine modifiers with a key (e.g. "ctrl+s", "alt+Tab", "ctrl+shift+Escape"). Key names are case-insensitive; common names like "Return", "Tab", "Escape", "Up", "Down", "Left", "Right", "Home", "End", "Page_Up", "Page_Down", "Delete", "BackSpace" are supported. */
interface BetaComputerKeyInput {
  /** The key or key-combination to press. */
  text: string;
  /** Number of times to repeat the key press. Default is 1. */
  repeat?: number | null; // minimum: 1, maximum: 100
}

interface BetaComputerKeyToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Press a key or key-combination on the keyboard. Use "+" to combine modifiers with a key (e.g. "ctrl+s", "alt+Tab", "ctrl+shift+Escape"). Key names are case-insensitive; common names like "Return", "Tab", "Escape", "Up", "Down", "Left", "Right", "Home", "End", "Page_Up", "Page_Down", "Delete", "BackSpace" are supported. */
  input: BetaComputerKeyInput;
  name: "key";
  toolset_name: "computer";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

/** Click and drag the cursor from `start_coordinate` to `coordinate`. */
interface BetaComputerLeftClickDragInput {
  /** (x, y): x pixels from the left edge, y pixels from the top edge. */
  coordinate: Array<number>; // minItems: 2, maxItems: 2
  /** (x, y): x pixels from the left edge, y pixels from the top edge. */
  start_coordinate: Array<number>; // minItems: 2, maxItems: 2
  /** Optional key combination to hold down during this action (e.g. "ctrl", "shift", "ctrl+shift"). */
  text?: string | null;
}

interface BetaComputerLeftClickDragToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Click and drag the cursor from `start_coordinate` to `coordinate`. */
  input: BetaComputerLeftClickDragInput;
  name: "left_click_drag";
  toolset_name: "computer";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

/** Click the left mouse button at the specified (x, y) pixel coordinate, or the current cursor position if `coordinate` is omitted. */
interface BetaComputerLeftClickInput {
  /** (x, y): x pixels from the left edge, y pixels from the top edge. */
  coordinate?: Array<number> | null; // minItems: 2, maxItems: 2
  /** Optional key combination to hold down during this action (e.g. "ctrl", "shift", "ctrl+shift"). */
  text?: string | null;
}

interface BetaComputerLeftClickToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Click the left mouse button at the specified (x, y) pixel coordinate, or the current cursor position if `coordinate` is omitted. */
  input: BetaComputerLeftClickInput;
  name: "left_click";
  toolset_name: "computer";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

/** Press and hold the left mouse button at the current cursor position. */
interface BetaComputerLeftMouseDownInput {}

interface BetaComputerLeftMouseDownToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Press and hold the left mouse button at the current cursor position. */
  input: BetaComputerLeftMouseDownInput;
  name: "left_mouse_down";
  toolset_name: "computer";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

/** Release the left mouse button. */
interface BetaComputerLeftMouseUpInput {}

interface BetaComputerLeftMouseUpToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Release the left mouse button. */
  input: BetaComputerLeftMouseUpInput;
  name: "left_mouse_up";
  toolset_name: "computer";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

/** Click the middle mouse button at the specified (x, y) pixel coordinate, or the current cursor position if `coordinate` is omitted. */
interface BetaComputerMiddleClickInput {
  /** (x, y): x pixels from the left edge, y pixels from the top edge. */
  coordinate?: Array<number> | null; // minItems: 2, maxItems: 2
  /** Optional key combination to hold down during this action (e.g. "ctrl", "shift", "ctrl+shift"). */
  text?: string | null;
}

interface BetaComputerMiddleClickToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Click the middle mouse button at the specified (x, y) pixel coordinate, or the current cursor position if `coordinate` is omitted. */
  input: BetaComputerMiddleClickInput;
  name: "middle_click";
  toolset_name: "computer";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

/** Move the cursor to a specified (x, y) pixel coordinate. Use this ONLY to hover without clicking; otherwise use a click action directly. */
interface BetaComputerMouseMoveInput {
  /** (x, y): x pixels from the left edge, y pixels from the top edge. */
  coordinate: Array<number>; // minItems: 2, maxItems: 2
}

interface BetaComputerMouseMoveToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Move the cursor to a specified (x, y) pixel coordinate. Use this ONLY to hover without clicking; otherwise use a click action directly. */
  input: BetaComputerMouseMoveInput;
  name: "mouse_move";
  toolset_name: "computer";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

/** Click the right mouse button at the specified (x, y) pixel coordinate, or the current cursor position if `coordinate` is omitted. */
interface BetaComputerRightClickInput {
  /** (x, y): x pixels from the left edge, y pixels from the top edge. */
  coordinate?: Array<number> | null; // minItems: 2, maxItems: 2
  /** Optional key combination to hold down during this action (e.g. "ctrl", "shift", "ctrl+shift"). */
  text?: string | null;
}

interface BetaComputerRightClickToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Click the right mouse button at the specified (x, y) pixel coordinate, or the current cursor position if `coordinate` is omitted. */
  input: BetaComputerRightClickInput;
  name: "right_click";
  toolset_name: "computer";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

/** Take a screenshot of the screen. */
interface BetaComputerScreenshotInput {}

interface BetaComputerScreenshotToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Take a screenshot of the screen. */
  input: BetaComputerScreenshotInput;
  name: "screenshot";
  toolset_name: "computer";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

type BetaComputerScrollDirection = "up" | "down" | "left" | "right";

/** Scroll the screen at the specified (x, y) pixel coordinate, or the current cursor position if `coordinate` is omitted. Do NOT use PageUp/PageDown to scroll. */
interface BetaComputerScrollInput {
  /** Number of 'clicks' of the scroll wheel. */
  scroll_amount: number;
  scroll_direction: BetaComputerScrollDirection;
  /** (x, y): x pixels from the left edge, y pixels from the top edge. */
  coordinate?: Array<number> | null; // minItems: 2, maxItems: 2
  /** Optional key combination to hold down during this action (e.g. "ctrl", "shift", "ctrl+shift"). */
  text?: string | null;
}

interface BetaComputerScrollToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Scroll the screen at the specified (x, y) pixel coordinate, or the current cursor position if `coordinate` is omitted. Do NOT use PageUp/PageDown to scroll. */
  input: BetaComputerScrollInput;
  name: "scroll";
  toolset_name: "computer";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

type BetaComputerToolUseBlock = BetaComputerKeyToolUseBlock | BetaComputerHoldKeyToolUseBlock | BetaComputerTypeToolUseBlock | BetaComputerCursorPositionToolUseBlock | BetaComputerMouseMoveToolUseBlock | BetaComputerLeftMouseDownToolUseBlock | BetaComputerLeftMouseUpToolUseBlock | BetaComputerLeftClickToolUseBlock | BetaComputerLeftClickDragToolUseBlock | BetaComputerRightClickToolUseBlock | BetaComputerMiddleClickToolUseBlock | BetaComputerDoubleClickToolUseBlock | BetaComputerTripleClickToolUseBlock | BetaComputerScrollToolUseBlock | BetaComputerWaitToolUseBlock | BetaComputerScreenshotToolUseBlock | BetaComputerZoomToolUseBlock;

/** Triple-click the left mouse button at the specified (x, y) pixel coordinate, or the current cursor position if `coordinate` is omitted. */
interface BetaComputerTripleClickInput {
  /** (x, y): x pixels from the left edge, y pixels from the top edge. */
  coordinate?: Array<number> | null; // minItems: 2, maxItems: 2
  /** Optional key combination to hold down during this action (e.g. "ctrl", "shift", "ctrl+shift"). */
  text?: string | null;
}

interface BetaComputerTripleClickToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Triple-click the left mouse button at the specified (x, y) pixel coordinate, or the current cursor position if `coordinate` is omitted. */
  input: BetaComputerTripleClickInput;
  name: "triple_click";
  toolset_name: "computer";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

/** Type a string of text on the keyboard. */
interface BetaComputerTypeInput {
  /** The text to type. */
  text: string;
}

interface BetaComputerTypeToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Type a string of text on the keyboard. */
  input: BetaComputerTypeInput;
  name: "type";
  toolset_name: "computer";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

/** Wait for a specified duration. */
interface BetaComputerWaitInput {
  /** Duration to wait, in seconds. */
  duration: number; // maximum: 300
}

interface BetaComputerWaitToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Wait for a specified duration. */
  input: BetaComputerWaitInput;
  name: "wait";
  toolset_name: "computer";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

/** Take a screenshot of a rectangular region. Region coordinates are in the full-screenshot space (not physical display pixels). The crop is scaled up to fill the image budget so fine details become legible. */
interface BetaComputerZoomInput {
  /** (x0, y0, x1, y1): The region to capture. */
  region: Array<number>; // minItems: 4, maxItems: 4
}

interface BetaComputerZoomToolUseBlock {
  type: "tool_use";
  id: string; // pattern: ^[a-zA-Z0-9_-]+$
  /** Take a screenshot of a rectangular region. Region coordinates are in the full-screenshot space (not physical display pixels). The crop is scaled up to fill the image budget so fine details become legible. */
  input: BetaComputerZoomInput;
  name: "zoom";
  toolset_name: "computer";
  /** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
  caller?: BetaToolUseCaller;
}

type BetaMemoryTool20250818Command = BetaMemoryTool20250818ViewCommand | BetaMemoryTool20250818CreateCommand | BetaMemoryTool20250818StrReplaceCommand | BetaMemoryTool20250818InsertCommand | BetaMemoryTool20250818DeleteCommand | BetaMemoryTool20250818RenameCommand;

interface BetaMemoryTool20250818CreateCommand {
  /** Command type identifier */
  command: "create";
  /** Content to write to the file */
  file_text: string;
  /** Path where the file should be created */
  path: string;
}

interface BetaMemoryTool20250818DeleteCommand {
  /** Command type identifier */
  command: "delete";
  /** Path to the file or directory to delete */
  path: string;
}

interface BetaMemoryTool20250818InsertCommand {
  /** Command type identifier */
  command: "insert";
  /** Line number where text should be inserted */
  insert_line: number; // minimum: 1
  /** Text to insert at the specified line */
  insert_text: string;
  /** Path to the file where text should be inserted */
  path: string;
}

interface BetaMemoryTool20250818RenameCommand {
  /** Command type identifier */
  command: "rename";
  /** New path for the file or directory */
  new_path: string;
  /** Current path of the file or directory */
  old_path: string;
}

interface BetaMemoryTool20250818StrReplaceCommand {
  /** Command type identifier */
  command: "str_replace";
  /** Text to replace with */
  new_str: string;
  /** Text to search for and replace */
  old_str: string;
  /** Path to the file where text should be replaced */
  path: string;
}

interface BetaMemoryTool20250818ViewCommand {
  /** Command type identifier */
  command: "view";
  /** Path to directory or file to view */
  path: string;
  /** Optional line range for viewing specific lines */
  view_range?: Array<number>; // minItems: 2, maxItems: 2
}

/** Compact the whole conversation and return a signed `compaction` block, alone, that a later request sends back first in `messages`, in place of the messages it summarizes. There is no trigger and no pause flag: sending the parameter compacts, and nothing is sampled after the block. The summarization prompt is the server's own unless `instructions` are given, which then replace it for this request; a value that is empty or only whitespace counts as absent. */
interface BetaSummarizeCompaction {
  type: "summarize";
  /** Replaces the server's default summarization prompt for this request. An empty or whitespace-only value counts as absent. */
  instructions?: string | null; // maxLength: 16384
}

/** Which party invoked the tool call: the model directly, or a server tool on its behalf. */
type BetaToolUseCaller = BetaDirectCaller | BetaServerToolCaller | BetaServerToolCaller20260120;

type BetaToolsetToolUseBlock = BetaBrowserToolUseBlock | BetaComputerToolUseBlock | BetaToolUseBlock;
```
