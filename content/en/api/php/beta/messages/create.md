---
title: Create a Message
url: https://platform.claude.com/docs/en/api/php/beta/messages/create
---

# Create a Message

`$client->beta->messages->create(int maxTokens, list<BetaMessageParam> messages, Model model, ?BetaCacheControlEphemeral cacheControl, ?BetaCompactionConfig compaction, ?Container container, ?BetaContextManagementConfig contextManagement, ?BetaDiagnosticsParam diagnostics, ?FallbackCreditToken fallbackCreditToken, ?BetaFallbacksParam fallbacks, ?string inferenceGeo, ?list<BetaRequestMCPServerURLDefinition> mcpServers, ?BetaMetadata metadata, ?BetaOutputConfig outputConfig, ?BetaJSONOutputFormat outputFormat, ?ServiceTier serviceTier, ?Speed speed, ?list<string> stopSequences, ?System system, ?BetaThinkingConfigParam thinking, ?BetaMessageThreadParam thread, ?BetaToolChoice toolChoice, ?list<BetaToolUnion> tools, ?list<AnthropicBeta> betas, ?string userProfileID, ?string workspaceID): BetaMessage`

**POST** `/v1/messages`

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

The Messages API can be used for either single queries or stateless multi-turn conversations.

Learn more about the Messages API in our [user guide](https://platform.claude.com/docs/en/get-started?sdk_languages=php)

## Parameters

- `maxTokens: int`

  The maximum number of tokens to generate before stopping.

  Note that our models may stop _before_ reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

  Set to `0` to populate the [prompt cache](https://platform.claude.com/docs/en/build-with-claude/prompt-caching?sdk_languages=php#pre-warming-the-cache) without generating a response.

  Different models have different maximum values for this parameter.  See [models](https://platform.claude.com/docs/en/about-claude/models/overview?sdk_languages=php) for details.

- `messages: list<BetaMessageParam>`

  Input messages.

  Our models are trained to operate on alternating `user` and `assistant` conversational turns. When creating a new `Message`, you specify the prior conversational turns with the `messages` parameter, and the model then generates the next `Message` in the conversation. Consecutive `user` or `assistant` turns in your request will be combined into a single turn.

  Each input message must be an object with a `role` and `content`. You can specify a single `user`-role message, or you can include multiple `user` and `assistant` messages.

  If the final message uses the `assistant` role, the response content will continue immediately from the content in that message. This can be used to constrain part of the model's response. This is called prefill. On models that don't support prefill, creating a message that ends with a partial `assistant` response returns a 400 error. See [Prefill not supported](https://platform.claude.com/docs/en/api/errors?sdk_languages=php#prefill-not-supported).

  Example with a single `user` message:

  ```json
  [{"role": "user", "content": "Hello, Claude"}]
  ```

  Example with multiple conversational turns:

  ```json
  [
    {"role": "user", "content": "Hello there."},
    {"role": "assistant", "content": "Hi, I'm Claude. How can I help you?"},
    {"role": "user", "content": "Can you explain LLMs in plain English?"},
  ]
  ```

  Example with a partially-filled response from Claude, for models that support prefill:

  ```json
  [
    {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
    {"role": "assistant", "content": "The best answer is ("},
  ]
  ```

  Each input message `content` may be either a single `string` or an array of content blocks, where each block has a specific `type`. Using a `string` for `content` is shorthand for an array of one content block of type `"text"`. The following input messages are equivalent:

  ```json
  {"role": "user", "content": "Hello, Claude"}
  ```

  ```json
  {"role": "user", "content": [{"type": "text", "text": "Hello, Claude"}]}
  ```

  See [input examples](https://platform.claude.com/docs/en/build-with-claude/working-with-messages?sdk_languages=php).

  Note that if you want to include a [system prompt](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices?sdk_languages=php#give-claude-a-role), you can use the top-level `system` parameter.

  There is a limit of 100,000 messages in a single request.

- `model: Model`

  The model that will complete your prompt.

  See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `cacheControl?: optional BetaCacheControlEphemeral`

  Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

- `compaction?: optional BetaCompactionConfig`

  Compaction configuration.

  When set on `POST /v1/messages`, the request is a compaction request: the conversation in `messages` is summarized and the response holds only the resulting `compaction` block (`stop_reason` `"compaction"`), which later requests send first in `messages` in place of the messages it summarizes. `POST /v1/messages/count_tokens` accepts this parameter and ignores it: the count it returns is for the conversation in `messages` as sent. Cannot be combined with `context_management`.

- `container?: optional Container`

  Container identifier for reuse across requests.

- `contextManagement?: optional BetaContextManagementConfig`

  Context management configuration.

  This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.

- `diagnostics?: optional BetaDiagnosticsParam`

  Request-level diagnostics. Supply `previous_message_id` to have the response include `diagnostics.cache_miss_reason` explaining any prompt-cache divergence from that prior request.

- `fallbackCreditToken?: optional FallbackCreditToken`

  The `fallback_credit_token` from a prior refusal's `stop_details`.

  When a preceding request was refused and returned a `fallback_credit_token`,
  pass that code here on the retry to have the retry's cache-creation tokens
  for the prefix that was warm on the refused model billed at the cache-read
  rate. Must be redeemed by the same organization and workspace, with the same
  request body (optionally extended by one appended `assistant` message whose
  content is the partial text — with any trailing whitespace stripped from
  the final text block — and paired server-tool blocks streamed before the
  refusal; the appended-assistant form is not available for requests with
  `output_format` set or forced `tool_choice`), on an eligible fallback
  model, on the same platform,
  and within 5 minutes of the refusal; a mismatch is a 400. A token minted
  mid-server-tool-loop whose partial content was continuable may only be
  redeemed with the appended-assistant form — if an exact-body retry is
  rejected with a 400 saying the token must be redeemed by continuing the
  partial response, retry with the appended-assistant form instead.

  When the appended-assistant form is used on a model that otherwise disallows
  assistant-turn prefill, this token also authorizes that one prefill.

- `fallbacks?: optional BetaFallbacksParam`

  Opt-in server-side retry on one or more substitute models when the requested model declines for policy reasons. Tried in order: if the first entry also declines, the second is tried, and so on. Some models don't support fallbacks; on those models, a list of fallback models returns a 400 error. See [Server-side fallback](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback?sdk_languages=php#server-side-fallback). The string "default" requests the requested model's server-defined default fallback configuration. On a model that doesn't support fallbacks, the request runs on the requested model alone, so a declined request stays declined.

- `inferenceGeo?: optional string`

  Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

- `mcpServers?: optional list<BetaRequestMCPServerURLDefinition>`

  MCP servers to be utilized in this request

- `metadata?: optional BetaMetadata`

  An object describing metadata about the request.

- `outputConfig?: optional BetaOutputConfig`

  Configuration options for the model's output, such as the output format.

- `serviceTier?: optional ServiceTier`

  Determines whether to use priority capacity (if available) or standard capacity for this request.

  Anthropic offers different levels of service for your API requests. See [service-tiers](https://platform.claude.com/docs/en/api/service-tiers?sdk_languages=php) for details.

- `speed?: optional Speed`

  The inference speed mode for this request. `"fast"` enables high output-tokens-per-second inference.

  Some models require the `fast-mode-2026-02-01` beta header for any `speed` value. See [fast mode](https://platform.claude.com/docs/en/build-with-claude/fast-mode?sdk_languages=php) for which models.

- `stopSequences?: optional list<string>`

  Custom text sequences that will cause the model to stop generating.

  Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

  If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

- `system?: optional System`

  System prompt.

  A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices?sdk_languages=php#give-claude-a-role).

- `thinking?: optional BetaThinkingConfigParam`

  Configuration for Claude's thinking.

  With `{"type": "adaptive"}`, Claude decides when and how much to think. With `{"type": "enabled"}` (manual extended thinking), you set a `budget_tokens` of at least 1,024. Thinking tokens count toward your `max_tokens` limit.

  Which `type` values are accepted, and what happens when you omit `thinking`, depend on the model. See [thinking](https://platform.claude.com/docs/en/build-with-claude/thinking?sdk_languages=php#configuring-thinking) for each model's behavior.

- `thread?: optional BetaMessageThreadParam`

  Server-held conversation state (a Thread). `{"type": "create"}` asks the server to hold this conversation's state under the response's `id`; `{"type": "continue", "previous_message_id": ...}` resumes from a previous response so only the new turn's messages are sent. The response shape is unchanged.

- `toolChoice?: optional BetaToolChoice`

  How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

- `tools?: optional list<BetaToolUnion>`

  Definitions of tools that the model may use.

  If you include `tools` in your API request, the model may return `tool_use` content blocks that represent the model's use of those tools. You can then run those tools using the tool input generated by the model and then optionally return results back to the model using `tool_result` content blocks.

  There are two types of tools: **client tools** and **server tools**. The behavior described below applies to client tools. For [server tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools?sdk_languages=php), see their individual documentation as each has its own behavior (e.g., the [web search tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool?sdk_languages=php)).

  Each tool definition includes:

  * `name`: Name of the tool.
  * `description`: Optional, but strongly-recommended description of the tool.
  * `input_schema`: [JSON schema](https://json-schema.org/draft/2020-12) for the tool `input` shape that the model will produce in `tool_use` output content blocks.

  For example, if you defined `tools` as:

  ```json
  [
    {
      "name": "get_stock_price",
      "description": "Get the current stock price for a given ticker symbol.",
      "input_schema": {
        "type": "object",
        "properties": {
          "ticker": {
            "type": "string",
            "description": "The stock ticker symbol, e.g. AAPL for Apple Inc."
          }
        },
        "required": ["ticker"]
      }
    }
  ]
  ```

  And then asked the model "What's the S&P 500 at today?", the model might produce `tool_use` content blocks in the response like this:

  ```json
  [
    {
      "type": "tool_use",
      "id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
      "name": "get_stock_price",
      "input": { "ticker": "^GSPC" }
    }
  ]
  ```

  You might then run your `get_stock_price` tool with `{"ticker": "^GSPC"}` as an input, and return the following back to the model in a subsequent `user` message:

  ```json
  [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
      "content": "259.75 USD"
    }
  ]
  ```

  Tools can be used for workflows that include running client-side tools and functions, or more generally whenever you want the model to produce a particular JSON structure of output.

  See our [guide](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview?sdk_languages=php) for more details.

- `betas?: optional list<AnthropicBeta>` (header parameter)

  Optional header to specify the beta version(s) you want to use.

- `userProfileID?: optional string` (header parameter)

  The user profile ID to attribute this request to. Use when acting on behalf of a party other than your organization.

- `workspaceID?: optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

- `outputFormat?: optional BetaJSONOutputFormat`

  **Deprecated**

  Deprecated: Use `output_config.format` instead. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs?sdk_languages=php)

  A schema to specify Claude's output format in responses. This parameter will be removed in a future release.

## Returns

- `class BetaMessage`

  - `"message" type`

    Object type.

    For Messages, this is always `"message"`.

  - `string id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `?BetaContainer container`

    Information about the container used in this request.

    This will be non-null if a container tool (e.g. code execution) was used.

  - `list<BetaContentBlock> content`

    Content generated by the model.

    This is an array of content blocks, each of which has a `type` that determines its shape.

    Example:

    ```json
    [{"type": "text", "text": "Hi, I'm Claude."}]
    ```

    If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

    For example, if the input `messages` were:

    ```json
    [
      {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
      {"role": "assistant", "content": "The best answer is ("}
    ]
    ```

    Then the response `content` might be:

    ```json
    [{"type": "text", "text": "B)"}]
    ```

  - `?BetaContextManagementResponse contextManagement`

    Context management response.

    Information about context management strategies applied during the request.

  - `?BetaDiagnostics diagnostics`

    Request-level diagnostics. `null` when the request did not supply `diagnostics`, or when it did and no prompt-cache divergence was detected.

  - `Model model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `"assistant" role`

    Conversational role of the generated message.

    This will always be `"assistant"`.

  - `?BetaRefusalStopDetails stopDetails`

    Structured information about why model output stopped.

    This is `null` when the `stop_reason` has no additional detail to report.

  - `?BetaStopReason stopReason`

    The reason that we stopped.

    This may be one the following values:

    * `"end_turn"`: the model reached a natural stopping point
    * `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
    * `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
    * `"tool_use"`: the model invoked one or more tools
    * `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
    * `"refusal"`: when streaming classifiers intervene to handle potential policy violations
    * `"model_context_window_exceeded"`: we exceeded the model's context window

    In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

  - `?string stopSequence`

    Which custom stop sequence was generated, if any.

    This value will be a non-null string if one of your custom stop sequences was generated.

  - `BetaUsage usage`

    Billing and rate-limit usage.

    Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

    Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

    For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

    Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

  - `?list<BetaInputTransformation> inputTransformations`

    Changes the API made to the request's input before showing it to the model,
    and blocks that failed a binding check but were left unchanged: one entry per
    block, in request order. Two entry types today. `thinking_dropped` — a
    `thinking`, `redacted_thinking` or `connector_text` block from the request's
    `messages` that was removed from the prompt instead of being shown to the
    model because it failed a binding check. `thinking_mismatch_allowed` — a
    `thinking` or `redacted_thinking` block that failed the conversation check
    (the conversation before it differs from the one it was created in, or it
    carries no record of one on a model that requires it) and was shown to the
    model all the same, because that check is not enforced for this request.
    More entry types may be added over time; ignore types you do not recognize.

    Requires `anthropic-beta: thinking-binding-controls-2026-08-01`. Present on
    every such response from a model that supports extended thinking, as `[]`
    when there is no entry to report; without the beta, blocks are removed or
    left in place all the same but nothing is reported. Removed blocks contribute
    nothing to `usage.input_tokens`; blocks left in place count as sent. When
    streaming, the array is final in `message_start`; the final `message_delta`
    event carries it only when a server-side model fallback happened mid-stream,
    in which case it holds the serving model's entries and replaces the one in
    `message_start`.

- `class BetaRawMessageStreamEvent`

  - `class BetaRawMessageStartEvent`

    - `"message_start" type`

    - `BetaMessage message`

  - `class BetaRawMessageDeltaEvent`

    - `"message_delta" type`

    - `?BetaContextManagementResponse contextManagement`

      Information about context management strategies applied during the request

    - `Delta delta`

    - `BetaMessageDeltaUsage usage`

      Billing and rate-limit usage.

      Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

      Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

      For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

      Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

    - `?list<BetaInputTransformation> inputTransformations`

      Changes the API made to the request's input before showing it to the model,
      and blocks that failed a binding check but were left unchanged: one entry per
      block, in request order. Two entry types today. `thinking_dropped` — a
      `thinking`, `redacted_thinking` or `connector_text` block from the request's
      `messages` that was removed from the prompt instead of being shown to the
      model because it failed a binding check. `thinking_mismatch_allowed` — a
      `thinking` or `redacted_thinking` block that failed the conversation check
      (the conversation before it differs from the one it was created in, or it
      carries no record of one on a model that requires it) and was shown to the
      model all the same, because that check is not enforced for this request.
      More entry types may be added over time; ignore types you do not recognize.

      Requires `anthropic-beta: thinking-binding-controls-2026-08-01`. Present on
      every such response from a model that supports extended thinking, as `[]`
      when there is no entry to report; without the beta, blocks are removed or
      left in place all the same but nothing is reported. Removed blocks contribute
      nothing to `usage.input_tokens`; blocks left in place count as sent. When
      streaming, the array is final in `message_start`; the final `message_delta`
      event carries it only when a server-side model fallback happened mid-stream,
      in which case it holds the serving model's entries and replaces the one in
      `message_start`.

  - `class BetaRawMessageStopEvent`

    - `"message_stop" type`

  - `class BetaRawContentBlockStartEvent`

    - `"content_block_start" type`

    - `ContentBlock contentBlock`

    - `int index`

  - `class BetaRawContentBlockDeltaEvent`

    - `"content_block_delta" type`

    - `BetaRawContentBlockDelta delta`

    - `int index`

  - `class BetaRawContentBlockStopEvent`

    - `"content_block_stop" type`

    - `int index`

## Errors

Any method can also return the general [HTTP errors](https://platform.claude.com/docs/en/api/errors?sdk_languages=php).

On a streaming call, the errors listed below apply when the API rejects the request before the stream starts. An error partway through the stream can arrive as a more general error type. To identify it, use its error code, if it has one, not its type.

- `AvailableToolsLimitExceededException` (HTTP status 400, error code `available_tools_limit_exceeded`)

  The tools available after a message exceed a limit on their number or their size.

- `ClaudeCodeKeyCreatorNotMemberException` (HTTP status 400, error code `claude_code_key_creator_not_member`)

  The API key belongs to the Claude Code workspace, and the user who created it is no longer a member of the organization or of that workspace.

- `ClaudeCodeVersionTooOldException` (HTTP status 400, error code `claude_code_version_too_old`)

  The request comes from a Claude Code version older than the minimum that the requested model or the organization requires. Update Claude Code, then retry.

- `CMEKKeyDisabledException` (HTTP status 400, error code `cmek_key_disabled`)

  The workspace's customer-managed encryption key is disabled or revoked. Re-enable the key, then retry.

- `CMEKKeyNetworkBlockedException` (HTTP status 400, error code `cmek_key_network_blocked`)

  The key management service's network access controls blocked the request to the workspace's customer-managed encryption key. The key itself may be healthy.

- `CompactionBlockAmbiguousException` (HTTP status 400, error code `compaction_block_ambiguous`)

  `messages` holds more than one `compaction` block with content. Send only the block the conversation returned last.

- `CompactionBlockMisplacedException` (HTTP status 400, error code `compaction_block_misplaced`)

  The `compaction` block is not the first block of the conversation, or is in a `system` message.

- `CompactionContentMismatchException` (HTTP status 400, error code `compaction_content_mismatch`)

  The `compaction` block's `content` differs from the text its `signature` recorded.

- `CompactionIncompleteTurnException` (HTTP status 400, error code `compaction_incomplete_turn`)

  The compaction request ends on an `assistant` turn that is not finished.

- `CompactionNothingToSummarizeException` (HTTP status 400, error code `compaction_nothing_to_summarize`)

  `messages` holds no `user` or `assistant` content to summarize or adopt.

- `CompactionSignatureInvalidException` (HTTP status 400, error code `compaction_signature_invalid`)

  The `compaction` block's `signature` does not verify.

- `CompactionTooManyToolReferencesException` (HTTP status 400, error code `compaction_too_many_tool_references`)

  The conversation references more distinct tools than a `compaction` block can record.

- `CompactionToolChangesMismatchException` (HTTP status 400, error code `compaction_tool_changes_mismatch`)

  The `compaction` block's `tool_changes` differs from what was returned with the block.

- `OrganizationOnHoldException` (HTTP status 400, error code `organization_on_hold`)

  Anthropic has disabled the organization for trust and safety reasons. An organization disabled for any other reason, such as billing, does not get this code. `appeal_url`, when present, is where the organization can appeal.

- `RequestBodyEncodingInvalidException` (HTTP status 400, error code `request_body_encoding_invalid`)

  The request body is not valid for its `Content-Encoding`.

- `RequestBodyEncodingUnsupportedException` (HTTP status 400, error code `request_body_encoding_unsupported`)

  The request's `Content-Encoding` is not supported.

- `ThreadAlreadyContinuedException` (HTTP status 400, error code `thread_already_continued`)

  The response that `previous_message_id` names has already been continued, and each response can be continued only once. Continue from the Thread's most recent response `id`.

- `ThreadContinueInFlightException` (HTTP status 400, error code `thread_continue_in_flight`)

  Another request is still continuing from the same `previous_message_id`. Wait for it to complete and continue from its response `id`, or replay the full conversation with `thread: {"type": "create"}`.

- `ThreadFingerprintMismatchException` (HTTP status 400, error code `thread_fingerprint_mismatch`)

  A field that must stay the same across a Thread's turns differs from the value stored with the Thread; the message names each such field. Send the stored values, or replay the full conversation with `thread: {"type": "create"}` to change them.

- `ThreadUnsupportedRequestException` (HTTP status 400, error code `thread_unsupported_request`)

  The request combines `thread` with a request field or an organization setting that Threads do not support; `unsupported`, when present, names it. Send the full conversation without `thread`, or change that field.

- `ToolNameConflictException` (HTTP status 400, error code `tool_name_conflict`)

  A tool made available in `messages` takes a name that an available tool of another kind, or of another MCP server, already holds.

- `ToolReferenceUnresolvedException` (HTTP status 400, error code `tool_reference_unresolved`)

  A tool change or MCP tool listing references a tool or MCP server that is not defined at that position in the conversation.

- `ThreadNotFoundException` (HTTP status 404, error code `thread_not_found`)

  No usable Thread state was found for `previous_message_id`. Replay the full conversation with `thread: {"type": "create"}` to start a new Thread.

- `SkillReadBlockedUndecryptableException` (HTTP status 409, error code `skill_read_blocked_undecryptable`)

  A custom skill the request names is stored under an encryption key state the workspace cannot currently decrypt.

- `RequestBodyTooLargeAfterDecodingException` (HTTP status 413, error code `request_body_too_large_after_decoding`)

  The compressed request body exceeds the request size limit once decoded.

- `EnforcedSpendLimitReachedException` (HTTP status 429, error code `enforced_spend_limit_reached`)

  The organization has crossed the monthly API usage threshold of its API tier.

- `RampLimitExceededException` (HTTP status 429, error code `ramp_limit_exceeded`)

  The request would exceed a ramp limit, which caps how fast usage can grow. Retry after the time in the `retry-after` header.

- `CMEKKeyUnreachableException` (HTTP status 503, error code `cmek_key_unreachable`)

  The workspace's customer-managed encryption key could not be reached. Retry the request; if this continues, check that the key is available in your key management service, or contact Anthropic support.

- `CompactionUnavailableException` (HTTP status 529, error code `compaction_unavailable`)

  The compaction could not be completed for a transient server reason. Retry the request.

## Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

use Anthropic\Client;
use Anthropic\Beta\AnthropicBeta;
use Anthropic\Beta\Messages\BetaThinkingPrefixMismatchBehavior;
use Anthropic\Messages\Model;

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaMessage = $client->beta->messages->create(
  maxTokens: 1024,
  messages: [['content' => 'Hello, world', 'role' => 'user']],
  model: Model::CLAUDE_OPUS_5_5,
  cacheControl: ['type' => 'ephemeral', 'ttl' => '5m'],
  compaction: ['type' => 'summarize', 'instructions' => 'instructions'],
  container: [
    'id' => 'id',
    'skills' => [
      ['skillID' => 'pdf', 'type' => 'anthropic', 'version' => 'latest']
    ],
  ],
  contextManagement: [
    'edits' => [
      [
        'type' => 'clear_tool_uses_20250919',
        'clearAtLeast' => ['type' => 'input_tokens', 'value' => 0],
        'clearToolInputs' => true,
        'excludeTools' => ['string'],
        'keep' => ['type' => 'tool_uses', 'value' => 0],
        'trigger' => ['type' => 'input_tokens', 'value' => 1],
      ],
    ],
  ],
  diagnostics: ['previousMessageID' => 'previous_message_id'],
  fallbackCreditToken: 'x',
  fallbacks: 'default',
  inferenceGeo: 'inference_geo',
  mcpServers: [
    [
      'name' => 'name',
      'type' => 'url',
      'url' => 'url',
      'authorizationToken' => 'authorization_token',
      'toolConfiguration' => ['allowedTools' => ['string'], 'enabled' => true],
    ],
  ],
  metadata: ['userID' => '13803d75-b4b5-4c3e-b2a2-6f21399b021b'],
  outputConfig: [
    'effort' => 'low',
    'format' => ['schema' => ['foo' => 'bar'], 'type' => 'json_schema'],
    'taskBudget' => ['total' => 1024, 'type' => 'tokens', 'remaining' => 0],
  ],
  outputFormat: ['schema' => ['foo' => 'bar'], 'type' => 'json_schema'],
  serviceTier: 'auto',
  speed: 'standard',
  stopSequences: ['string'],
  system: [
    [
      'text' => 'Today\'s date is 2024-06-01.',
      'type' => 'text',
      'cacheControl' => ['type' => 'ephemeral', 'ttl' => '5m'],
      'citations' => [
        [
          'citedText' => 'The grass is green. The sky is blue.',
          'documentIndex' => 0,
          'documentTitle' => 'x',
          'endCharIndex' => 0,
          'startCharIndex' => 0,
          'type' => 'char_location',
        ],
      ],
    ],
  ],
  thinking: [
    'type' => 'adaptive',
    'blockBinding' => [
      'prefixMismatchBehavior' => BetaThinkingPrefixMismatchBehavior::ERROR
    ],
    'display' => 'summarized',
  ],
  thread: ['type' => 'create'],
  toolChoice: ['type' => 'auto', 'disableParallelToolUse' => true],
  tools: [
    [
      'inputSchema' => [
        'type' => 'object',
        'properties' => ['location' => 'bar', 'unit' => 'bar'],
        'required' => ['location'],
      ],
      'name' => 'name',
      'allowedCallers' => ['direct'],
      'cacheControl' => ['type' => 'ephemeral', 'ttl' => '5m'],
      'deferLoading' => true,
      'description' => 'Get the current weather in a given location',
      'eagerInputStreaming' => true,
      'inputExamples' => [['foo' => 'bar']],
      'strict' => true,
      'type' => 'custom',
    ],
  ],
  betas: [AnthropicBeta::COMPUTER_USE_2024_10_22],
  userProfileID: 'anthropic-user-profile-id',
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaMessage);
```

### Response (200)

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
