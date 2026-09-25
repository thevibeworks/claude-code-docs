---
title: Messages
url: https://platform.claude.com/docs/en/api/php/beta/messages
---

# Messages

## Create a Message

`$client->beta->messages->create(int maxTokens, list<BetaMessageParam> messages, Model model, ?BetaCacheControlEphemeral cacheControl, ?BetaCompactionConfig compaction, ?Container container, ?BetaContextManagementConfig contextManagement, ?BetaDiagnosticsParam diagnostics, ?FallbackCreditToken fallbackCreditToken, ?BetaFallbacksParam fallbacks, ?string inferenceGeo, ?list<BetaRequestMCPServerURLDefinition> mcpServers, ?BetaMetadata metadata, ?BetaOutputConfig outputConfig, ?BetaJSONOutputFormat outputFormat, ?ServiceTier serviceTier, ?Speed speed, ?list<string> stopSequences, ?System system, ?float temperature, ?BetaThinkingConfigParam thinking, ?BetaToolChoice toolChoice, ?list<BetaToolUnion> tools, ?int topK, ?float topP, ?list<AnthropicBeta> betas, ?string userProfileID, ?string workspaceID): BetaMessage`

**POST** `/v1/messages`

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

The Messages API can be used for either single queries or stateless multi-turn conversations.

Learn more about the Messages API in our [user guide](https://platform.claude.com/docs/en/get-started)

### Parameters

- `maxTokens: int`

  The maximum number of tokens to generate before stopping.

  Note that our models may stop _before_ reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

  Set to `0` to populate the [prompt cache](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#pre-warming-the-cache) without generating a response.

  Different models have different maximum values for this parameter.  See [models](https://platform.claude.com/docs/en/about-claude/models/overview) for details.

- `messages: list<BetaMessageParam>`

  Input messages.

  Our models are trained to operate on alternating `user` and `assistant` conversational turns. When creating a new `Message`, you specify the prior conversational turns with the `messages` parameter, and the model then generates the next `Message` in the conversation. Consecutive `user` or `assistant` turns in your request will be combined into a single turn.

  Each input message must be an object with a `role` and `content`. You can specify a single `user`-role message, or you can include multiple `user` and `assistant` messages.

  If the final message uses the `assistant` role, the response content will continue immediately from the content in that message. This can be used to constrain part of the model's response.

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

  Example with a partially-filled response from Claude:

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

  See [input examples](https://platform.claude.com/docs/en/build-with-claude/working-with-messages).

  Note that if you want to include a [system prompt](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role), you can use the top-level `system` parameter — there is no `"system"` role for input messages in the Messages API.

  There is a limit of 100,000 messages in a single request.

- `model: Model`

  The model that will complete your prompt.

  See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `cacheControl?:optional BetaCacheControlEphemeral`

  Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

- `compaction?:optional BetaCompactionConfig`

  Compaction configuration.

  When set on `POST /v1/messages`, the request is a compaction request: the conversation in `messages` is summarized and the response holds only the resulting `compaction` block (`stop_reason` `"compaction"`), which later requests send first in `messages` in place of the messages it summarizes. `POST /v1/messages/count_tokens` accepts this parameter and ignores it: the count it returns is for the conversation in `messages` as sent. Cannot be combined with `context_management`.

- `container?:optional Container`

  Container identifier for reuse across requests.

- `contextManagement?:optional BetaContextManagementConfig`

  Context management configuration.

  This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.

- `diagnostics?:optional BetaDiagnosticsParam`

  Request-level diagnostics. Supply `previous_message_id` to have the response include `diagnostics.cache_miss_reason` explaining any prompt-cache divergence from that prior request.

- `fallbackCreditToken?:optional FallbackCreditToken`

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

- `fallbacks?:optional BetaFallbacksParam`

  Opt-in server-side retry on one or more substitute models when the requested model declines for policy reasons. Tried in order: if the first entry also declines, the second is tried, and so on. The string "default" requests the requested model's server-defined default fallback configuration.

- `inferenceGeo?:optional string`

  Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

- `mcpServers?:optional list<BetaRequestMCPServerURLDefinition>`

  MCP servers to be utilized in this request

- `metadata?:optional BetaMetadata`

  An object describing metadata about the request.

- `outputConfig?:optional BetaOutputConfig`

  Configuration options for the model's output, such as the output format.

- `serviceTier?:optional ServiceTier`

  Determines whether to use priority capacity (if available) or standard capacity for this request.

  Anthropic offers different levels of service for your API requests. See [service-tiers](https://platform.claude.com/docs/en/api/service-tiers) for details.

- `speed?:optional Speed`

  The inference speed mode for this request. `"fast"` enables high output-tokens-per-second inference.

- `stopSequences?:optional list<string>`

  Custom text sequences that will cause the model to stop generating.

  Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

  If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

- `stream?:optional bool`

  Whether to incrementally stream the response using server-sent events.

  See [streaming](https://platform.claude.com/docs/en/build-with-claude/streaming) for details.

- `system?:optional System`

  System prompt.

  A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role).

- `thinking?:optional BetaThinkingConfigParam`

  Configuration for enabling Claude's extended thinking.

  When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

  See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

- `toolChoice?:optional BetaToolChoice`

  How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

- `tools?:optional list<BetaToolUnion>`

  Definitions of tools that the model may use.

  If you include `tools` in your API request, the model may return `tool_use` content blocks that represent the model's use of those tools. You can then run those tools using the tool input generated by the model and then optionally return results back to the model using `tool_result` content blocks.

  There are two types of tools: **client tools** and **server tools**. The behavior described below applies to client tools. For [server tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools), see their individual documentation as each has its own behavior (e.g., the [web search tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)).

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

  See our [guide](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview) for more details.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `userProfileID?:optional string`

  The user profile ID to attribute this request to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

- `outputFormat?:optional BetaJSONOutputFormat`

  **Deprecated**

  Deprecated: Use `output_config.format` instead. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

  A schema to specify Claude's output format in responses. This parameter will be removed in a future release.

- `temperature?:optional float`

  **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not support setting temperature. A value of 1.0 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

  Amount of randomness injected into the response.

  Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

  Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

- `topK?:optional int`

  **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not accept top_k; any value will be rejected with a 400 error.

  Only sample from the top K options for each subsequent token.

  Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

  Recommended for advanced use cases only.

- `topP?:optional float`

  **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not support setting top_p. A value >= 0.99 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

  Use nucleus sampling.

  In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.

  Recommended for advanced use cases only.

### Returns

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

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaMessage = $client->beta->messages->create(
  maxTokens: 1024,
  messages: [
    [
      'content' => 'Hello, world',
      'role' => 'user',
      'clearAt' => 'next_user_message',
      'outputConfig' => ['effort' => 'low'],
    ],
  ],
  model: Model::CLAUDE_OPUS_5,
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
  temperature: 1,
  thinking: [
    'type' => 'adaptive',
    'blockBinding' => [
      'prefixMismatchBehavior' => BetaThinkingPrefixMismatchBehavior::ERROR
    ],
    'display' => 'summarized',
  ],
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
  topK: 5,
  topP: 0.7,
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  userProfileID: 'anthropic-user-profile-id',
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaMessage);
```

#### Response (200)

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
      "citations": [
        {
          "cited_text": "The grass is green. The sky is blue.",
          "document_index": 0,
          "document_title": "My Document",
          "end_char_index": 0,
          "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
          "start_char_index": 0,
          "type": "char_location"
        }
      ],
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
  "diagnostics": {
    "cache_miss_reason": {
      "cache_missed_input_tokens": 0,
      "type": "model_changed"
    }
  },
  "model": "claude-opus-5",
  "role": "assistant",
  "stop_details": {
    "category": "cyber",
    "explanation": "This request was declined because it conflicts with Anthropic's Usage Policy.",
    "fallback_credit_token": "QW50aHJvcGljL0NsYXVkZQ==",
    "fallback_has_prefill_claim": true,
    "recommended_model": "claude-opus-4-8",
    "type": "refusal"
  },
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
        "model": "claude-fable-5-1",
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

## Count tokens in a Message

`$client->beta->messages->countTokens(list<BetaMessageParam> messages, Model model, ?BetaCacheControlEphemeral cacheControl, ?BetaCompactionConfig compaction, ?BetaContextManagementConfig contextManagement, ?list<BetaRequestMCPServerURLDefinition> mcpServers, ?BetaOutputConfig outputConfig, ?BetaJSONOutputFormat outputFormat, ?Speed speed, ?System system, ?BetaThinkingConfigParam thinking, ?BetaToolChoice toolChoice, ?list<Tool> tools, ?list<AnthropicBeta> betas, ?string userProfileID, ?string workspaceID): BetaMessageTokensCount`

**POST** `/v1/messages/count_tokens`

Count the number of tokens in a Message.

The Token Count API can be used to count the number of tokens in a Message, including tools, images, and documents, without creating it.

Learn more about token counting in our [user guide](https://platform.claude.com/docs/en/build-with-claude/token-counting)

### Parameters

- `messages: list<BetaMessageParam>`

  Input messages.

  Our models are trained to operate on alternating `user` and `assistant` conversational turns. When creating a new `Message`, you specify the prior conversational turns with the `messages` parameter, and the model then generates the next `Message` in the conversation. Consecutive `user` or `assistant` turns in your request will be combined into a single turn.

  Each input message must be an object with a `role` and `content`. You can specify a single `user`-role message, or you can include multiple `user` and `assistant` messages.

  If the final message uses the `assistant` role, the response content will continue immediately from the content in that message. This can be used to constrain part of the model's response.

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

  Example with a partially-filled response from Claude:

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

  See [input examples](https://platform.claude.com/docs/en/build-with-claude/working-with-messages).

  Note that if you want to include a [system prompt](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role), you can use the top-level `system` parameter — there is no `"system"` role for input messages in the Messages API.

  There is a limit of 100,000 messages in a single request.

- `model: Model`

  The model that will complete your prompt.

  See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `cacheControl?:optional BetaCacheControlEphemeral`

  Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

- `compaction?:optional BetaCompactionConfig`

  Compaction configuration.

  When set on `POST /v1/messages`, the request is a compaction request: the conversation in `messages` is summarized and the response holds only the resulting `compaction` block (`stop_reason` `"compaction"`), which later requests send first in `messages` in place of the messages it summarizes. `POST /v1/messages/count_tokens` accepts this parameter and ignores it: the count it returns is for the conversation in `messages` as sent. Cannot be combined with `context_management`.

- `contextManagement?:optional BetaContextManagementConfig`

  Context management configuration.

  This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.

- `mcpServers?:optional list<BetaRequestMCPServerURLDefinition>`

  MCP servers to be utilized in this request

- `outputConfig?:optional BetaOutputConfig`

  Configuration options for the model's output, such as the output format.

- `speed?:optional Speed`

  The inference speed mode for this request. `"fast"` enables high output-tokens-per-second inference.

- `system?:optional System`

  System prompt.

  A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role).

- `thinking?:optional BetaThinkingConfigParam`

  Configuration for enabling Claude's extended thinking.

  When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

  See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

- `toolChoice?:optional BetaToolChoice`

  How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

- `tools?:optional list<Tool>`

  Definitions of tools that the model may use.

  If you include `tools` in your API request, the model may return `tool_use` content blocks that represent the model's use of those tools. You can then run those tools using the tool input generated by the model and then optionally return results back to the model using `tool_result` content blocks.

  There are two types of tools: **client tools** and **server tools**. The behavior described below applies to client tools. For [server tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools), see their individual documentation as each has its own behavior (e.g., the [web search tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)).

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

  See our [guide](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview) for more details.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `userProfileID?:optional string`

  The user profile ID to attribute this request to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

- `outputFormat?:optional BetaJSONOutputFormat`

  **Deprecated**

  Deprecated: Use `output_config.format` instead. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

  A schema to specify Claude's output format in responses. This parameter will be removed in a future release.

### Returns

- `class BetaMessageTokensCount`

  - `?BetaCountTokensContextManagementResponse contextManagement`

    Information about context management applied to the message.

  - `int inputTokens`

    The total number of tokens across the provided list of messages, system prompt, and tools.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaMessageTokensCount = $client->beta->messages->countTokens(
  messages: [
    [
      'content' => 'Hello, world',
      'role' => 'user',
      'clearAt' => 'next_user_message',
      'outputConfig' => ['effort' => 'low'],
    ],
  ],
  model: Model::CLAUDE_OPUS_5,
  cacheControl: ['type' => 'ephemeral', 'ttl' => '5m'],
  compaction: ['type' => 'summarize', 'instructions' => 'instructions'],
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
  mcpServers: [
    [
      'name' => 'name',
      'type' => 'url',
      'url' => 'url',
      'authorizationToken' => 'authorization_token',
      'toolConfiguration' => ['allowedTools' => ['string'], 'enabled' => true],
    ],
  ],
  outputConfig: [
    'effort' => 'low',
    'format' => ['schema' => ['foo' => 'bar'], 'type' => 'json_schema'],
    'taskBudget' => ['total' => 1024, 'type' => 'tokens', 'remaining' => 0],
  ],
  outputFormat: ['schema' => ['foo' => 'bar'], 'type' => 'json_schema'],
  speed: 'standard',
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
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  userProfileID: 'anthropic-user-profile-id',
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaMessageTokensCount);
```

#### Response (200)

```json
{
  "context_management": {
    "original_input_tokens": 0
  },
  "input_tokens": 2095
}
```

## Domain types

### Beta Advisor Message Iteration Usage

- `class BetaAdvisorMessageIterationUsage`

  - `"advisor_message" type`

    Usage for an advisor sub-inference iteration

  - `?BetaCacheCreation cacheCreation`

    Breakdown of cached tokens by TTL

  - `int cacheCreationInputTokens`

    The number of input tokens used to create the cache entry.

  - `int cacheReadInputTokens`

    The number of input tokens read from the cache.

  - `int inputTokens`

    The number of input tokens which were used.

  - `Model model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `int outputTokens`

    The number of output tokens which were used.

### Beta Advisor Redacted Result Block

- `class BetaAdvisorRedactedResultBlock`

  - `"advisor_redacted_result" type`

  - `string encryptedContent`

    Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

  - `?string stopReason`

    The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

### Beta Advisor Redacted Result Block Param

- `class BetaAdvisorRedactedResultBlockParam`

  - `"advisor_redacted_result" type`

  - `string encryptedContent`

    Opaque blob produced by a prior response; must be round-tripped verbatim.

  - `?string stopReason`

### Beta Advisor Result Block

- `class BetaAdvisorResultBlock`

  - `"advisor_result" type`

  - `?string stopReason`

    The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

  - `string text`

### Beta Advisor Result Block Param

- `class BetaAdvisorResultBlockParam`

  - `"advisor_result" type`

  - `string text`

  - `?string stopReason`

### Beta Advisor Tool 20260301

- `class BetaAdvisorTool20260301`

  - `"advisor_20260301" type`

  - `Model model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `"advisor" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?BetaCacheControlEphemeral caching`

    Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?int maxTokens`

    Bounds the advisor's total output (thinking + text) per call. When the advisor hits this cap, the returned advisor_result or advisor_redacted_result block carries stop_reason='max_tokens', and a truncation note is appended to the advice text the worker model sees (inside the encrypted blob in redacted mode). When set, the server also emits a remaining-tokens budget block in the advisor's prompt so the advisor self-shapes toward the cap. When omitted, the advisor model's default output cap applies and no budget block is emitted.

  - `?int maxUses`

    Maximum number of times the tool can be used in the API request.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Beta Advisor Tool Result Block

- `class BetaAdvisorToolResultBlock`

  - `"advisor_tool_result" type`

  - `Content content`

  - `string toolUseID`

### Beta Advisor Tool Result Block Param

- `class BetaAdvisorToolResultBlockParam`

  - `"advisor_tool_result" type`

  - `Content content`

  - `string toolUseID`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

### Beta Advisor Tool Result Error

- `class BetaAdvisorToolResultError`

  - `"advisor_tool_result_error" type`

  - `ErrorCode errorCode`

### Beta Advisor Tool Result Error Param

- `class BetaAdvisorToolResultErrorParam`

  - `"advisor_tool_result_error" type`

  - `ErrorCode errorCode`

### Beta All Thinking Turns

- `class BetaAllThinkingTurns`

  - `"all" type`

### Beta Base64 Image Source

- `class BetaBase64ImageSource`

  - `"base64" type`

  - `string data`

  - `MediaType mediaType`

### Beta Base64 PDF Source

- `class BetaBase64PDFSource`

  - `"base64" type`

  - `string data`

  - `"application/pdf" mediaType`

### Beta Bash Code Execution Output Block

- `class BetaBashCodeExecutionOutputBlock`

  - `"bash_code_execution_output" type`

  - `string fileID`

### Beta Bash Code Execution Output Block Param

- `class BetaBashCodeExecutionOutputBlockParam`

  - `"bash_code_execution_output" type`

  - `string fileID`

### Beta Bash Code Execution Result Block

- `class BetaBashCodeExecutionResultBlock`

  - `"bash_code_execution_result" type`

  - `list<BetaBashCodeExecutionOutputBlock> content`

  - `int returnCode`

  - `string stderr`

  - `string stdout`

### Beta Bash Code Execution Result Block Param

- `class BetaBashCodeExecutionResultBlockParam`

  - `"bash_code_execution_result" type`

  - `list<BetaBashCodeExecutionOutputBlockParam> content`

  - `int returnCode`

  - `string stderr`

  - `string stdout`

### Beta Bash Code Execution Tool Result Block

- `class BetaBashCodeExecutionToolResultBlock`

  - `"bash_code_execution_tool_result" type`

  - `Content content`

  - `string toolUseID`

### Beta Bash Code Execution Tool Result Block Param

- `class BetaBashCodeExecutionToolResultBlockParam`

  - `"bash_code_execution_tool_result" type`

  - `Content content`

  - `string toolUseID`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

### Beta Bash Code Execution Tool Result Error

- `class BetaBashCodeExecutionToolResultError`

  - `"bash_code_execution_tool_result_error" type`

  - `ErrorCode errorCode`

### Beta Bash Code Execution Tool Result Error Param

- `class BetaBashCodeExecutionToolResultErrorParam`

  - `"bash_code_execution_tool_result_error" type`

  - `ErrorCode errorCode`

### Beta Browser Close Tab Config

- `class BetaBrowserCloseTabConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Browser Double Click Config

- `class BetaBrowserDoubleClickConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Browser File Upload Config

- `class BetaBrowserFileUploadConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Browser Find Config

- `class BetaBrowserFindConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Browser Form Input Config

- `class BetaBrowserFormInputConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Browser Get Page Text Config

- `class BetaBrowserGetPageTextConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Browser Hold Key Config

- `class BetaBrowserHoldKeyConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Browser Hover Config

- `class BetaBrowserHoverConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Browser Javascript Exec Config

- `class BetaBrowserJavascriptExecConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Browser Key Config

- `class BetaBrowserKeyConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Browser Left Click Config

- `class BetaBrowserLeftClickConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Browser Left Click Drag Config

- `class BetaBrowserLeftClickDragConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Browser Left Mouse Down Config

- `class BetaBrowserLeftMouseDownConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Browser Left Mouse Up Config

- `class BetaBrowserLeftMouseUpConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Browser List Tabs Config

- `class BetaBrowserListTabsConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Browser Middle Click Config

- `class BetaBrowserMiddleClickConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Browser Mouse Move Config

- `class BetaBrowserMouseMoveConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Browser Navigate Config

- `class BetaBrowserNavigateConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Browser New Tab Config

- `class BetaBrowserNewTabConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Browser Read Console Config

- `class BetaBrowserReadConsoleConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Browser Read Network Config

- `class BetaBrowserReadNetworkConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Browser Read Page Config

- `class BetaBrowserReadPageConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Browser Right Click Config

- `class BetaBrowserRightClickConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Browser Screenshot Config

- `class BetaBrowserScreenshotConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Browser Scroll Config

- `class BetaBrowserScrollConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Browser Scroll To Config

- `class BetaBrowserScrollToConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Browser State Block Param

- `class BetaBrowserStateBlockParam`

  - `"browser_state" type`

  - `list<BetaBrowserStateTabEntry> tabs`

    All tabs open in the browser after this call — the full inventory, not a delta. May be empty. Whenever non-empty, exactly one entry carries `active: true`.

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?list<BetaBrowserStateChange> stateChanges`

    Tabs opened and download state changes during this call. "Nothing to report" is expressed by omitting the field, never by an empty list.

### Beta Browser State Change

- `class BetaBrowserStateChange`

  - `class BetaBrowserStateChangeTabOpened`

    - `"tab_opened" type`

    - `string tabID`

      The `tab_id` of the opened tab, present in `tabs`.

  - `class BetaBrowserStateChangeDownloadStarted`

    - `"download_started" type`

    - `string downloadID`

      The caller-assigned identifier for this download, stable across the state changes reporting it.

    - `string url`

      The final post-redirect URL the download was served from.

  - `class BetaBrowserStateChangeDownloadCompleted`

    - `"download_completed" type`

    - `string downloadID`

      The caller-assigned identifier for this download, stable across the state changes reporting it.

    - `string url`

      The final post-redirect URL the download was served from.

    - `?string path`

      Where the executor saved the file, on the executor's filesystem. Only included when another tool in the same environment can read the file at that path.

    - `?int sizeBytes`

      The completed download's size.

  - `class BetaBrowserStateChangeDownloadFailed`

    - `"download_failed" type`

    - `string downloadID`

      The caller-assigned identifier for this download, stable across the state changes reporting it.

    - `string url`

      The final post-redirect URL the download was served from.

    - `?string error`

      The failure or cancellation detail, when known.

### Beta Browser State Change Download Completed

- `class BetaBrowserStateChangeDownloadCompleted`

  - `"download_completed" type`

  - `string downloadID`

    The caller-assigned identifier for this download, stable across the state changes reporting it.

  - `string url`

    The final post-redirect URL the download was served from.

  - `?string path`

    Where the executor saved the file, on the executor's filesystem. Only included when another tool in the same environment can read the file at that path.

  - `?int sizeBytes`

    The completed download's size.

### Beta Browser State Change Download Failed

- `class BetaBrowserStateChangeDownloadFailed`

  - `"download_failed" type`

  - `string downloadID`

    The caller-assigned identifier for this download, stable across the state changes reporting it.

  - `string url`

    The final post-redirect URL the download was served from.

  - `?string error`

    The failure or cancellation detail, when known.

### Beta Browser State Change Download Started

- `class BetaBrowserStateChangeDownloadStarted`

  - `"download_started" type`

  - `string downloadID`

    The caller-assigned identifier for this download, stable across the state changes reporting it.

  - `string url`

    The final post-redirect URL the download was served from.

### Beta Browser State Change Tab Opened

- `class BetaBrowserStateChangeTabOpened`

  - `"tab_opened" type`

  - `string tabID`

    The `tab_id` of the opened tab, present in `tabs`.

### Beta Browser State Tab Entry

- `class BetaBrowserStateTabEntry`

  - `string tabID`

    The caller-assigned identifier for this tab, unique within the inventory.

  - `string title`

    The title of the page the tab is showing. May be empty.

  - `string url`

    The URL of the page the tab is showing. May be empty.

  - `?bool active`

    Whether this tab is the active tab after this call. Whenever `tabs` is non-empty, exactly one entry is marked `active: true`.

### Beta Browser Switch Tab Config

- `class BetaBrowserSwitchTabConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Browser Toolset 20260801

- `class BetaBrowserToolset20260801`

  - `"browser_toolset_20260801" type`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?BetaBrowserToolsetConfigs configs`

    Sparse per-member overrides, keyed by member name. Absent, null, and {} are equivalent; a member's defaults apply wherever its key is absent.

### Beta Browser Toolset Configs

- `class BetaBrowserToolsetConfigs`

  - `?BetaBrowserTypeConfig type`

    `type`'s config overrides.

  - `?BetaBrowserCloseTabConfig closeTab`

    `close_tab`'s config overrides.

  - `?BetaBrowserDoubleClickConfig doubleClick`

    `double_click`'s config overrides.

  - `?BetaBrowserFileUploadConfig fileUpload`

    `file_upload`'s config overrides.

  - `?BetaBrowserFindConfig find`

    `find`'s config overrides.

  - `?BetaBrowserFormInputConfig formInput`

    `form_input`'s config overrides.

  - `?BetaBrowserGetPageTextConfig getPageText`

    `get_page_text`'s config overrides.

  - `?BetaBrowserHoldKeyConfig holdKey`

    `hold_key`'s config overrides.

  - `?BetaBrowserHoverConfig hover`

    `hover`'s config overrides.

  - `?BetaBrowserJavascriptExecConfig javascriptExec`

    `javascript_exec`'s config overrides.

  - `?BetaBrowserKeyConfig key`

    `key`'s config overrides.

  - `?BetaBrowserLeftClickConfig leftClick`

    `left_click`'s config overrides.

  - `?BetaBrowserLeftClickDragConfig leftClickDrag`

    `left_click_drag`'s config overrides.

  - `?BetaBrowserLeftMouseDownConfig leftMouseDown`

    `left_mouse_down`'s config overrides.

  - `?BetaBrowserLeftMouseUpConfig leftMouseUp`

    `left_mouse_up`'s config overrides.

  - `?BetaBrowserListTabsConfig listTabs`

    `list_tabs`'s config overrides.

  - `?BetaBrowserMiddleClickConfig middleClick`

    `middle_click`'s config overrides.

  - `?BetaBrowserMouseMoveConfig mouseMove`

    `mouse_move`'s config overrides.

  - `?BetaBrowserNavigateConfig navigate`

    `navigate`'s config overrides.

  - `?BetaBrowserNewTabConfig newTab`

    `new_tab`'s config overrides.

  - `?BetaBrowserReadConsoleConfig readConsole`

    `read_console`'s config overrides.

  - `?BetaBrowserReadNetworkConfig readNetwork`

    `read_network`'s config overrides.

  - `?BetaBrowserReadPageConfig readPage`

    `read_page`'s config overrides.

  - `?BetaBrowserRightClickConfig rightClick`

    `right_click`'s config overrides.

  - `?BetaBrowserScreenshotConfig screenshot`

    `screenshot`'s config overrides.

  - `?BetaBrowserScrollConfig scroll`

    `scroll`'s config overrides.

  - `?BetaBrowserScrollToConfig scrollTo`

    `scroll_to`'s config overrides.

  - `?BetaBrowserSwitchTabConfig switchTab`

    `switch_tab`'s config overrides.

  - `?BetaBrowserTripleClickConfig tripleClick`

    `triple_click`'s config overrides.

  - `?BetaBrowserWaitConfig wait`

    `wait`'s config overrides.

  - `?BetaBrowserZoomConfig zoom`

    `zoom`'s config overrides.

### Beta Browser Triple Click Config

- `class BetaBrowserTripleClickConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Browser Type Config

- `class BetaBrowserTypeConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Browser Wait Config

- `class BetaBrowserWaitConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Browser Zoom Config

- `class BetaBrowserZoomConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Cache Control Ephemeral

- `class BetaCacheControlEphemeral`

  - `"ephemeral" type`

  - `?TTL ttl`

    The time-to-live for the cache control breakpoint.

    This may be one the following values:

    - `5m`: 5 minutes
    - `1h`: 1 hour

    Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

### Beta Cache Creation

- `class BetaCacheCreation`

  - `int ephemeral1hInputTokens`

    The number of input tokens used to create the 1 hour cache entry.

  - `int ephemeral5mInputTokens`

    The number of input tokens used to create the 5 minute cache entry.

### Beta Cache Miss Messages Changed

- `class BetaCacheMissMessagesChanged`

  - `"messages_changed" type`

  - `int cacheMissedInputTokens`

    Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

### Beta Cache Miss Model Changed

- `class BetaCacheMissModelChanged`

  - `"model_changed" type`

  - `int cacheMissedInputTokens`

    Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

### Beta Cache Miss Previous Message Not Found

- `class BetaCacheMissPreviousMessageNotFound`

  - `"previous_message_not_found" type`

### Beta Cache Miss Reason

- `class BetaCacheMissReason`

  - `class BetaCacheMissModelChanged`

    - `"model_changed" type`

    - `int cacheMissedInputTokens`

      Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

  - `class BetaCacheMissSystemChanged`

    - `"system_changed" type`

    - `int cacheMissedInputTokens`

      Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

  - `class BetaCacheMissToolsChanged`

    - `"tools_changed" type`

    - `int cacheMissedInputTokens`

      Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

  - `class BetaCacheMissMessagesChanged`

    - `"messages_changed" type`

    - `int cacheMissedInputTokens`

      Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

  - `class BetaCacheMissPreviousMessageNotFound`

    - `"previous_message_not_found" type`

  - `class BetaCacheMissUnavailable`

    - `"unavailable" type`

### Beta Cache Miss System Changed

- `class BetaCacheMissSystemChanged`

  - `"system_changed" type`

  - `int cacheMissedInputTokens`

    Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

### Beta Cache Miss Tools Changed

- `class BetaCacheMissToolsChanged`

  - `"tools_changed" type`

  - `int cacheMissedInputTokens`

    Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

### Beta Cache Miss Unavailable

- `class BetaCacheMissUnavailable`

  - `"unavailable" type`

### Beta Citation Char Location

- `class BetaCitationCharLocation`

  - `"char_location" type`

  - `string citedText`

  - `int documentIndex`

  - `?string documentTitle`

  - `int endCharIndex`

  - `?string fileID`

  - `int startCharIndex`

### Beta Citation Char Location Param

- `class BetaCitationCharLocationParam`

  - `"char_location" type`

  - `string citedText`

  - `int documentIndex`

  - `?string documentTitle`

  - `int endCharIndex`

  - `int startCharIndex`

### Beta Citation Config

- `class BetaCitationConfig`

  - `bool enabled`

### Beta Citation Content Block Location

- `class BetaCitationContentBlockLocation`

  - `"content_block_location" type`

  - `string citedText`

    The full text of the cited block range, concatenated.

    Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

  - `int documentIndex`

  - `?string documentTitle`

  - `int endBlockIndex`

    Exclusive 0-based end index of the cited block range in the source's `content` array.

    Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

  - `?string fileID`

  - `int startBlockIndex`

    0-based index of the first cited block in the source's `content` array.

### Beta Citation Content Block Location Param

- `class BetaCitationContentBlockLocationParam`

  - `"content_block_location" type`

  - `string citedText`

    The full text of the cited block range, concatenated.

    Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

  - `int documentIndex`

  - `?string documentTitle`

  - `int endBlockIndex`

    Exclusive 0-based end index of the cited block range in the source's `content` array.

    Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

  - `int startBlockIndex`

    0-based index of the first cited block in the source's `content` array.

### Beta Citation Page Location

- `class BetaCitationPageLocation`

  - `"page_location" type`

  - `string citedText`

  - `int documentIndex`

  - `?string documentTitle`

  - `int endPageNumber`

  - `?string fileID`

  - `int startPageNumber`

### Beta Citation Page Location Param

- `class BetaCitationPageLocationParam`

  - `"page_location" type`

  - `string citedText`

  - `int documentIndex`

  - `?string documentTitle`

  - `int endPageNumber`

  - `int startPageNumber`

### Beta Citation Search Result Location

- `class BetaCitationSearchResultLocation`

  - `"search_result_location" type`

  - `string citedText`

    The full text of the cited block range, concatenated.

    Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

  - `int endBlockIndex`

    Exclusive 0-based end index of the cited block range in the source's `content` array.

    Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

  - `int searchResultIndex`

    0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

    Counted separately from `document_index`; server-side web search results are not included in this count.

  - `string source`

  - `int startBlockIndex`

    0-based index of the first cited block in the source's `content` array.

  - `?string title`

### Beta Citation Search Result Location Param

- `class BetaCitationSearchResultLocationParam`

  - `"search_result_location" type`

  - `string citedText`

    The full text of the cited block range, concatenated.

    Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

  - `int endBlockIndex`

    Exclusive 0-based end index of the cited block range in the source's `content` array.

    Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

  - `int searchResultIndex`

    0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

    Counted separately from `document_index`; server-side web search results are not included in this count.

  - `string source`

  - `int startBlockIndex`

    0-based index of the first cited block in the source's `content` array.

  - `?string title`

### Beta Citation Web Search Result Location Param

- `class BetaCitationWebSearchResultLocationParam`

  - `"web_search_result_location" type`

  - `string citedText`

  - `string encryptedIndex`

  - `?string title`

  - `string url`

### Beta Citations Config Param

- `class BetaCitationsConfigParam`

  - `?bool enabled`

### Beta Citations Delta

- `class BetaCitationsDelta`

  - `"citations_delta" type`

  - `Citation citation`

### Beta Citations Web Search Result Location

- `class BetaCitationsWebSearchResultLocation`

  - `"web_search_result_location" type`

  - `string citedText`

  - `string encryptedIndex`

  - `?string title`

  - `string url`

### Beta Clear Thinking 20251015 Edit

- `class BetaClearThinking20251015Edit`

  - `"clear_thinking_20251015" type`

  - `?Keep keep`

    Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

### Beta Clear Thinking 20251015 Edit Response

- `class BetaClearThinking20251015EditResponse`

  - `"clear_thinking_20251015" type`

    The type of context management edit applied.

  - `int clearedInputTokens`

    Number of input tokens cleared by this edit.

  - `int clearedThinkingTurns`

    Number of thinking turns that were cleared.

### Beta Clear Tool Uses 20250919 Edit

- `class BetaClearToolUses20250919Edit`

  - `"clear_tool_uses_20250919" type`

  - `?BetaInputTokensClearAtLeast clearAtLeast`

    Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

  - `?ClearToolInputs clearToolInputs`

    Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

  - `?list<string> excludeTools`

    Tool names whose uses are preserved from clearing

  - `?BetaToolUsesKeep keep`

    Number of tool uses to retain in the conversation

  - `?Trigger trigger`

    Condition that triggers the context management strategy

### Beta Clear Tool Uses 20250919 Edit Response

- `class BetaClearToolUses20250919EditResponse`

  - `"clear_tool_uses_20250919" type`

    The type of context management edit applied.

  - `int clearedInputTokens`

    Number of input tokens cleared by this edit.

  - `int clearedToolUses`

    Number of tool uses that were cleared.

### Beta Code Execution Output Block

- `class BetaCodeExecutionOutputBlock`

  - `"code_execution_output" type`

  - `string fileID`

### Beta Code Execution Output Block Param

- `class BetaCodeExecutionOutputBlockParam`

  - `"code_execution_output" type`

  - `string fileID`

### Beta Code Execution Result Block

- `class BetaCodeExecutionResultBlock`

  - `"code_execution_result" type`

  - `list<BetaCodeExecutionOutputBlock> content`

  - `int returnCode`

  - `string stderr`

  - `string stdout`

### Beta Code Execution Result Block Param

- `class BetaCodeExecutionResultBlockParam`

  - `"code_execution_result" type`

  - `list<BetaCodeExecutionOutputBlockParam> content`

  - `int returnCode`

  - `string stderr`

  - `string stdout`

### Beta Code Execution Tool 20250522

- `class BetaCodeExecutionTool20250522`

  - `"code_execution_20250522" type`

  - `"code_execution" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Beta Code Execution Tool 20250825

- `class BetaCodeExecutionTool20250825`

  - `"code_execution_20250825" type`

  - `"code_execution" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Beta Code Execution Tool 20260120

- `class BetaCodeExecutionTool20260120`

  - `"code_execution_20260120" type`

  - `"code_execution" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Beta Code Execution Tool 20260521

- `class BetaCodeExecutionTool20260521`

  - `"code_execution_20260521" type`

  - `"code_execution" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Beta Code Execution Tool Result Block

- `class BetaCodeExecutionToolResultBlock`

  - `"code_execution_tool_result" type`

  - `BetaCodeExecutionToolResultBlockContent content`

  - `string toolUseID`

### Beta Code Execution Tool Result Block Content

- `class BetaCodeExecutionToolResultBlockContent`

  - `class BetaCodeExecutionToolResultError`

    - `"code_execution_tool_result_error" type`

    - `BetaCodeExecutionToolResultErrorCode errorCode`

  - `class BetaCodeExecutionResultBlock`

    - `"code_execution_result" type`

    - `list<BetaCodeExecutionOutputBlock> content`

    - `int returnCode`

    - `string stderr`

    - `string stdout`

  - `class BetaEncryptedCodeExecutionResultBlock`

    - `"encrypted_code_execution_result" type`

    - `list<BetaCodeExecutionOutputBlock> content`

    - `string encryptedStdout`

    - `int returnCode`

    - `string stderr`

### Beta Code Execution Tool Result Block Param

- `class BetaCodeExecutionToolResultBlockParam`

  - `"code_execution_tool_result" type`

  - `BetaCodeExecutionToolResultBlockParamContent content`

  - `string toolUseID`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

### Beta Code Execution Tool Result Block Param Content

- `class BetaCodeExecutionToolResultBlockParamContent`

  - `class BetaCodeExecutionToolResultErrorParam`

    - `"code_execution_tool_result_error" type`

    - `BetaCodeExecutionToolResultErrorCode errorCode`

  - `class BetaCodeExecutionResultBlockParam`

    - `"code_execution_result" type`

    - `list<BetaCodeExecutionOutputBlockParam> content`

    - `int returnCode`

    - `string stderr`

    - `string stdout`

  - `class BetaEncryptedCodeExecutionResultBlockParam`

    - `"encrypted_code_execution_result" type`

    - `list<BetaCodeExecutionOutputBlockParam> content`

    - `string encryptedStdout`

    - `int returnCode`

    - `string stderr`

### Beta Code Execution Tool Result Error

- `class BetaCodeExecutionToolResultError`

  - `"code_execution_tool_result_error" type`

  - `BetaCodeExecutionToolResultErrorCode errorCode`

### Beta Code Execution Tool Result Error Code

- `enum BetaCodeExecutionToolResultErrorCode`

  - `"invalid_tool_input"`

  - `"unavailable"`

  - `"too_many_requests"`

  - `"execution_time_exceeded"`

### Beta Code Execution Tool Result Error Param

- `class BetaCodeExecutionToolResultErrorParam`

  - `"code_execution_tool_result_error" type`

  - `BetaCodeExecutionToolResultErrorCode errorCode`

### Beta Compact 20260112 Edit

- `class BetaCompact20260112Edit`

  - `"compact_20260112" type`

  - `?string instructions`

    Additional instructions for summarization.

  - `?bool pauseAfterCompaction`

    Whether to pause after compaction and return the compaction block to the user.

  - `?BetaInputTokensTrigger trigger`

    When to trigger compaction. Defaults to 150000 input tokens.

### Beta Compaction Block

- `class BetaCompactionBlock`

  - `"compaction" type`

  - `?string content`

    Summary of compacted content, or null if compaction failed

  - `?string encryptedContent`

    Opaque metadata from prior compaction, to be round-tripped verbatim

  - `?string signature`

    Signature over the summary, to be sent back with the block verbatim

  - `?list<ToolChange> toolChanges`

    The tool changes of the compacted range: the `tool_addition` and `tool_removal` blocks that take the request's `tools` to the tool set in effect at the end of the range, or `[]` when the range changed no tool. Absent when the server did not compute them. Send the block back unchanged.

### Beta Compaction Block Param

- `class BetaCompactionBlockParam`

  - `"compaction" type`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?string content`

    Summary of previously compacted content, or null if compaction failed

  - `?string encryptedContent`

    Opaque metadata from prior compaction, to be round-tripped verbatim

  - `?string signature`

    The block's signature as returned, to be sent back verbatim

  - `?list<ToolChange> toolChanges`

    The tool changes of the compacted range, as the server returned them on this block: the `tool_addition` and `tool_removal` entries that take the request's `tools` to the tool set in effect at the end of the range. Send them back unchanged with the block.

### Beta Compaction Config

- `class BetaCompactionConfig`

  - `"summarize" type`

  - `?string instructions`

    Replaces the server's default summarization prompt for this request. An empty or whitespace-only value counts as absent.

### Beta Compaction Content Block Delta

- `class BetaCompactionContentBlockDelta`

  - `"compaction_delta" type`

  - `?string content`

  - `?string encryptedContent`

    Opaque metadata from prior compaction, to be round-tripped verbatim

### Beta Compaction Iteration Usage

- `class BetaCompactionIterationUsage`

  - `"compaction" type`

    Usage for a compaction iteration

  - `?BetaCacheCreation cacheCreation`

    Breakdown of cached tokens by TTL

  - `int cacheCreationInputTokens`

    The number of input tokens used to create the cache entry.

  - `int cacheReadInputTokens`

    The number of input tokens read from the cache.

  - `int inputTokens`

    The number of input tokens which were used.

  - `int outputTokens`

    The number of output tokens which were used.

### Beta Computer Cursor Position Config

- `class BetaComputerCursorPositionConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Computer Double Click Config

- `class BetaComputerDoubleClickConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Computer Hold Key Config

- `class BetaComputerHoldKeyConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Computer Key Config

- `class BetaComputerKeyConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Computer Left Click Config

- `class BetaComputerLeftClickConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Computer Left Click Drag Config

- `class BetaComputerLeftClickDragConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Computer Left Mouse Down Config

- `class BetaComputerLeftMouseDownConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Computer Left Mouse Up Config

- `class BetaComputerLeftMouseUpConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Computer Middle Click Config

- `class BetaComputerMiddleClickConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Computer Mouse Move Config

- `class BetaComputerMouseMoveConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Computer Right Click Config

- `class BetaComputerRightClickConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Computer Screenshot Config

- `class BetaComputerScreenshotConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Computer Scroll Config

- `class BetaComputerScrollConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Computer Toolset 20260801

- `class BetaComputerToolset20260801`

  - `"computer_toolset_20260801" type`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?BetaComputerToolsetConfigs configs`

    Sparse per-member overrides, keyed by member name. Absent, null, and {} are equivalent; a member's defaults apply wherever its key is absent.

### Beta Computer Toolset Configs

- `class BetaComputerToolsetConfigs`

  - `?BetaComputerTypeConfig type`

    `type`'s config overrides.

  - `?BetaComputerCursorPositionConfig cursorPosition`

    `cursor_position`'s config overrides.

  - `?BetaComputerDoubleClickConfig doubleClick`

    `double_click`'s config overrides.

  - `?BetaComputerHoldKeyConfig holdKey`

    `hold_key`'s config overrides.

  - `?BetaComputerKeyConfig key`

    `key`'s config overrides.

  - `?BetaComputerLeftClickConfig leftClick`

    `left_click`'s config overrides.

  - `?BetaComputerLeftClickDragConfig leftClickDrag`

    `left_click_drag`'s config overrides.

  - `?BetaComputerLeftMouseDownConfig leftMouseDown`

    `left_mouse_down`'s config overrides.

  - `?BetaComputerLeftMouseUpConfig leftMouseUp`

    `left_mouse_up`'s config overrides.

  - `?BetaComputerMiddleClickConfig middleClick`

    `middle_click`'s config overrides.

  - `?BetaComputerMouseMoveConfig mouseMove`

    `mouse_move`'s config overrides.

  - `?BetaComputerRightClickConfig rightClick`

    `right_click`'s config overrides.

  - `?BetaComputerScreenshotConfig screenshot`

    `screenshot`'s config overrides.

  - `?BetaComputerScrollConfig scroll`

    `scroll`'s config overrides.

  - `?BetaComputerTripleClickConfig tripleClick`

    `triple_click`'s config overrides.

  - `?BetaComputerWaitConfig wait`

    `wait`'s config overrides.

  - `?BetaComputerZoomConfig zoom`

    `zoom`'s config overrides.

### Beta Computer Triple Click Config

- `class BetaComputerTripleClickConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Computer Type Config

- `class BetaComputerTypeConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Computer Wait Config

- `class BetaComputerWaitConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Computer Zoom Config

- `class BetaComputerZoomConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Beta Container

- `class BetaContainer`

  - `string id`

    Identifier for the container used in this request

  - `\Datetime expiresAt`

    The time at which the container will expire.

  - `?list<BetaContainerSkill> skills`

    Skills loaded in the container

### Beta Container Params

- `class BetaContainerParams`

  - `?string id`

    Container id

  - `?list<BetaSkillParams> skills`

    List of skills to load in the container

### Beta Container Skill

- `class BetaContainerSkill`

  - `Type type`

    Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

  - `string skillID`

    Skill ID

  - `string version`

    The resolved version: a skill version ID for custom skills.

### Beta Container Upload Block

- `class BetaContainerUploadBlock`

  - `"container_upload" type`

  - `string fileID`

### Beta Container Upload Block Param

- `class BetaContainerUploadBlockParam`

  - `"container_upload" type`

  - `string fileID`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

### Beta Content Block

- `class BetaContentBlock`

  - `class BetaTextBlock`

    - `"text" type`

    - `?list<BetaTextCitation> citations`

      Citations supporting the text block.

      The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

    - `string text`

  - `class BetaThinkingBlock`

    - `"thinking" type`

    - `string signature`

      A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

      This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

      See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

    - `string thinking`

      The text of Claude's thinking process for this block.

  - `class BetaRedactedThinkingBlock`

    - `"redacted_thinking" type`

    - `string data`

      The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

      Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

      See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

  - `class BetaToolUseBlock`

    - `"tool_use" type`

    - `string id`

    - `array<string,mixed> input`

    - `string name`

    - `?Caller caller`

    - `?string toolsetName`

      For a toolset member tool_use, the toolset family.

  - `class BetaServerToolUseBlock`

    - `"server_tool_use" type`

    - `string id`

    - `array<string,mixed> input`

    - `Name name`

    - `?Caller caller`

  - `class BetaWebSearchToolResultBlock`

    - `"web_search_tool_result" type`

    - `BetaWebSearchToolResultBlockContent content`

    - `string toolUseID`

    - `?Caller caller`

  - `class BetaWebFetchToolResultBlock`

    - `"web_fetch_tool_result" type`

    - `Content content`

    - `string toolUseID`

    - `?Caller caller`

  - `class BetaAdvisorToolResultBlock`

    - `"advisor_tool_result" type`

    - `Content content`

    - `string toolUseID`

  - `class BetaCodeExecutionToolResultBlock`

    - `"code_execution_tool_result" type`

    - `BetaCodeExecutionToolResultBlockContent content`

    - `string toolUseID`

  - `class BetaBashCodeExecutionToolResultBlock`

    - `"bash_code_execution_tool_result" type`

    - `Content content`

    - `string toolUseID`

  - `class BetaTextEditorCodeExecutionToolResultBlock`

    - `"text_editor_code_execution_tool_result" type`

    - `Content content`

    - `string toolUseID`

  - `class BetaToolSearchToolResultBlock`

    - `"tool_search_tool_result" type`

    - `Content content`

    - `string toolUseID`

  - `class BetaMCPToolUseBlock`

    - `"mcp_tool_use" type`

    - `string id`

    - `array<string,mixed> input`

    - `string name`

      The name of the MCP tool

    - `string serverName`

      The name of the MCP server

  - `class BetaMCPToolResultBlock`

    - `"mcp_tool_result" type`

    - `Content content`

    - `bool isError`

    - `string toolUseID`

  - `class BetaContainerUploadBlock`

    - `"container_upload" type`

    - `string fileID`

  - `class BetaCompactionBlock`

    - `"compaction" type`

    - `?string content`

      Summary of compacted content, or null if compaction failed

    - `?string encryptedContent`

      Opaque metadata from prior compaction, to be round-tripped verbatim

    - `?string signature`

      Signature over the summary, to be sent back with the block verbatim

    - `?list<ToolChange> toolChanges`

      The tool changes of the compacted range: the `tool_addition` and `tool_removal` blocks that take the request's `tools` to the tool set in effect at the end of the range, or `[]` when the range changed no tool. Absent when the server did not compute them. Send the block back unchanged.

  - `class BetaFallbackBlock`

    - `"fallback" type`

    - `BetaFallbackInfo from`

      The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.

    - `BetaFallbackInfo to`

      The fallback model producing the content that follows this block. Its `model` is always the canonical id.

    - `BetaFallbackRefusalTrigger trigger`

      What caused the `from` model to hand over at this hop.

  - `class BetaMCPToolListingBlock`

    - `"mcp_tool_listing" type`

    - `string mcpServerName`

    - `list<BetaMCPTool> tools`

### Beta Content Block Param

- `class BetaContentBlockParam`

  - `class BetaTextBlockParam`

    - `"text" type`

    - `string text`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?list<BetaTextCitationParam> citations`

  - `class BetaImageBlockParam`

    - `"image" type`

    - `Source source`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?BetaImageTransformationsParam transformations`

      Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

  - `class BetaRequestDocumentBlock`

    - `"document" type`

    - `Source source`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?BetaCitationsConfigParam citations`

    - `?string context`

    - `?string title`

  - `class BetaSearchResultBlockParam`

    - `"search_result" type`

    - `list<BetaTextBlockParam> content`

    - `string source`

    - `string title`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?BetaCitationsConfigParam citations`

  - `class BetaThinkingBlockParam`

    - `"thinking" type`

    - `string signature`

      The `signature` value of this thinking block, exactly as returned by the API in a previous response. Used to verify that the block was generated by Claude.

      Thinking blocks must be passed back unmodified and in their original order; a modified block results in a 400 `invalid_request_error`.

    - `string thinking`

      The `thinking` text of this block as returned by the API.

  - `class BetaRedactedThinkingBlockParam`

    - `"redacted_thinking" type`

    - `string data`

      The `data` value of this redacted thinking block, exactly as returned by the API in a previous response. Opaque and encrypted; pass it back unchanged.

  - `class BetaToolUseBlockParam`

    - `"tool_use" type`

    - `string id`

    - `array<string,mixed> input`

    - `string name`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?Caller caller`

    - `?string toolsetName`

      For a toolset member tool_use, the toolset family this member belongs to.

  - `class BetaToolResultBlockParam`

    - `"tool_result" type`

    - `string toolUseID`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?Content content`

    - `?bool isError`

    - `?string toolsetName`

      For a toolset member tool_result, the toolset family of the paired tool_use.

  - `class BetaServerToolUseBlockParam`

    - `"server_tool_use" type`

    - `string id`

    - `array<string,mixed> input`

    - `Name name`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?Caller caller`

  - `class BetaWebSearchToolResultBlockParam`

    - `"web_search_tool_result" type`

    - `BetaWebSearchToolResultBlockParamContent content`

    - `string toolUseID`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?Caller caller`

  - `class BetaWebFetchToolResultBlockParam`

    - `"web_fetch_tool_result" type`

    - `Content content`

    - `string toolUseID`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?Caller caller`

  - `class BetaAdvisorToolResultBlockParam`

    - `"advisor_tool_result" type`

    - `Content content`

    - `string toolUseID`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

  - `class BetaCodeExecutionToolResultBlockParam`

    - `"code_execution_tool_result" type`

    - `BetaCodeExecutionToolResultBlockParamContent content`

    - `string toolUseID`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

  - `class BetaBashCodeExecutionToolResultBlockParam`

    - `"bash_code_execution_tool_result" type`

    - `Content content`

    - `string toolUseID`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

  - `class BetaTextEditorCodeExecutionToolResultBlockParam`

    - `"text_editor_code_execution_tool_result" type`

    - `Content content`

    - `string toolUseID`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

  - `class BetaToolSearchToolResultBlockParam`

    - `"tool_search_tool_result" type`

    - `Content content`

    - `string toolUseID`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

  - `class BetaMCPToolUseBlockParam`

    - `"mcp_tool_use" type`

    - `string id`

    - `array<string,mixed> input`

    - `string name`

    - `string serverName`

      The name of the MCP server

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

  - `class BetaRequestMCPToolResultBlockParam`

    - `"mcp_tool_result" type`

    - `string toolUseID`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?Content content`

    - `?bool isError`

  - `class BetaContainerUploadBlockParam`

    - `"container_upload" type`

    - `string fileID`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

  - `class BetaCompactionBlockParam`

    - `"compaction" type`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?string content`

      Summary of previously compacted content, or null if compaction failed

    - `?string encryptedContent`

      Opaque metadata from prior compaction, to be round-tripped verbatim

    - `?string signature`

      The block's signature as returned, to be sent back verbatim

    - `?list<ToolChange> toolChanges`

      The tool changes of the compacted range, as the server returned them on this block: the `tool_addition` and `tool_removal` entries that take the request's `tools` to the tool set in effect at the end of the range. Send them back unchanged with the block.

  - `class BetaRequestToolAdditionBlock`

    - `"tool_addition" type`

    - `Tool tool`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

  - `class BetaRequestToolRemovalBlock`

    - `"tool_removal" type`

    - `Tool tool`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

  - `class BetaMCPToolListingBlockParam`

    - `"mcp_tool_listing" type`

    - `string mcpServerName`

      The name of the MCP server this listing came from, as `mcp_servers` declares it.

    - `list<BetaMCPToolParam> tools`

      The server's tools, exactly as the response listed them.

  - `class BetaFallbackBlockParam`

    - `"fallback" type`

    - `BetaFallbackInfoParam from`

      Identifies one hop of a fallback transition.

    - `BetaFallbackInfoParam to`

      Identifies one hop of a fallback transition.

    - `?mixed trigger`

      The response block's `trigger`, echoed verbatim. Accepted and ignored by the server; any object or `null` is allowed.

### Beta Content Block Source

- `class BetaContentBlockSource`

  - `"content" type`

  - `Content content`

### Beta Content Block Source Content

- `class BetaContentBlockSourceContent`

  - `class BetaTextBlockParam`

    - `"text" type`

    - `string text`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?list<BetaTextCitationParam> citations`

  - `class BetaImageBlockParam`

    - `"image" type`

    - `Source source`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?BetaImageTransformationsParam transformations`

      Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

### Beta Context Management Config

- `class BetaContextManagementConfig`

  - `?list<Edit> edits`

    List of context management edits to apply

### Beta Context Management Response

- `class BetaContextManagementResponse`

  - `list<AppliedEdit> appliedEdits`

    List of context management edits that were applied.

### Beta Count Tokens Context Management Response

- `class BetaCountTokensContextManagementResponse`

  - `int originalInputTokens`

    The original token count before context management was applied

### Beta Diagnostics

- `class BetaDiagnostics`

  - `?BetaCacheMissReason cacheMissReason`

    Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

### Beta Diagnostics Param

- `class BetaDiagnosticsParam`

  - `?string previousMessageID`

    The `id` (`msg_...`) from this client's previous /v1/messages response. The server compares that request's prompt fingerprint against this one and returns `diagnostics.cache_miss_reason` when the prompt-cache prefix could not be reused. Pass `null` on the first turn to opt in without a prior message to compare.

### Beta Direct Caller

- `class BetaDirectCaller`

  - `"direct" type`

### Beta Document Block

- `class BetaDocumentBlock`

  - `"document" type`

  - `?BetaCitationConfig citations`

    Citation configuration for the document

  - `Source source`

  - `?string title`

    The title of the document

### Beta Encrypted Code Execution Result Block

- `class BetaEncryptedCodeExecutionResultBlock`

  - `"encrypted_code_execution_result" type`

  - `list<BetaCodeExecutionOutputBlock> content`

  - `string encryptedStdout`

  - `int returnCode`

  - `string stderr`

### Beta Encrypted Code Execution Result Block Param

- `class BetaEncryptedCodeExecutionResultBlockParam`

  - `"encrypted_code_execution_result" type`

  - `list<BetaCodeExecutionOutputBlockParam> content`

  - `string encryptedStdout`

  - `int returnCode`

  - `string stderr`

### Beta Fallback Block

- `class BetaFallbackBlock`

  - `"fallback" type`

  - `BetaFallbackInfo from`

    The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.

  - `BetaFallbackInfo to`

    The fallback model producing the content that follows this block. Its `model` is always the canonical id.

  - `BetaFallbackRefusalTrigger trigger`

    What caused the `from` model to hand over at this hop.

### Beta Fallback Block Param

- `class BetaFallbackBlockParam`

  - `"fallback" type`

  - `BetaFallbackInfoParam from`

    Identifies one hop of a fallback transition.

  - `BetaFallbackInfoParam to`

    Identifies one hop of a fallback transition.

  - `?mixed trigger`

    The response block's `trigger`, echoed verbatim. Accepted and ignored by the server; any object or `null` is allowed.

### Beta Fallback Credit Not Applied

- `class BetaFallbackCreditNotApplied`

  - `"not_applied" type`

  - `Reason reason`

    Why the reprice was not applied.

    A closed enum; additions to the redemption-check vocabulary arrive as
    deliberate schema updates.

  - `?list<string> removeToRedeem`

    Request fields to remove before retrying, so the retry can redeem this
    token.

    Present exactly when `reason` is `variant_fields_present` — never null,
    never an empty array; absent otherwise. Fields are named only from your own request, and only after
    the sealed variant hash matched. A served best-effort retry has already
    been billed at normal price; nothing redeems retroactively, but a corrected
    re-send inside the token's five-minute window can still redeem.

### Beta Fallback Credit Redeemed

- `class BetaFallbackCreditRedeemed`

  - `"redeemed" type`

### Beta Fallback Credit Token Param

- `class BetaFallbackCreditTokenParam`

  - `string token`

    The opaque `fallback_credit_token` from a prior refusal's `stop_details` — the same string the bare-string form carries.

  - `?Mode mode`

    How a failing token affects the retry. `strict` (the default, and the bare-string behavior): a failing redemption is a 400 and the retry is not served. `best_effort`: the retry is served either way — a token-layer failure no longer rejects the request; the retry proceeds at normal price and the outcome is reported on the response's `usage.fallback_credit`. Two failures stay hard in both modes: a malformed token, and combining `fallback_credit_token` with `fallbacks`.

### Beta Fallback Credit Usage

- `class BetaFallbackCreditUsage`

  - `Status status`

    Whether the fallback-credit reprice was applied to this response's billing.

    A union discriminated on `type`. `redeemed`: the retry is billed as if
    the conversation had been on the retry model all along — including when the
    resulting shift is zero because there was nothing to move. `not_applied`:
    no reprice was applied; the arm's `reason` says why.

### Beta Fallback Info

- `class BetaFallbackInfo`

  - `Model model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

### Beta Fallback Info Param

- `class BetaFallbackInfoParam`

  - `Model model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

### Beta Fallback Message Iteration Usage

- `class BetaFallbackMessageIterationUsage`

  - `"fallback_message" type`

    Usage for the fallback-model attempt that served the response

  - `?BetaCacheCreation cacheCreation`

    Breakdown of cached tokens by TTL

  - `int cacheCreationInputTokens`

    The number of input tokens used to create the cache entry.

  - `int cacheReadInputTokens`

    The number of input tokens read from the cache.

  - `int inputTokens`

    The number of input tokens which were used.

  - `Model model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `int outputTokens`

    The number of output tokens which were used.

### Beta Fallback Param

- `class BetaFallbackParam`

  - `Model model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `?int maxTokens`

  - `?BetaOutputConfig outputConfig`

  - `?Speed speed`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

  - `?Thinking thinking`

### Beta Fallback Refusal Trigger

- `class BetaFallbackRefusalTrigger`

  - `"refusal" type`

  - `?Category category`

    The policy category that triggered the `from` model's refusal at this hop. `null` when the refusal doesn't map to a named category. Same vocabulary as `stop_details.category`.

### Beta Fallbacks Param

- `class BetaFallbacksParam`

  - `class list<BetaFallbackParam>`

    - `Model model`

      The model that will complete your prompt.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `?int maxTokens`

    - `?BetaOutputConfig outputConfig`

    - `?Speed speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `?Thinking thinking`

  - `"default"`

### Beta File Document Source

- `class BetaFileDocumentSource`

  - `"file" type`

  - `string fileID`

### Beta File Image Source

- `class BetaFileImageSource`

  - `"file" type`

  - `string fileID`

### Beta Image Block Param

- `class BetaImageBlockParam`

  - `"image" type`

  - `Source source`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?BetaImageTransformationsParam transformations`

    Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

### Beta Image Transformations Param

- `class BetaImageTransformationsParam`

  - `?OversizedImage oversizedImage`

    What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

### Beta Input JSON Delta

- `class BetaInputJSONDelta`

  - `"input_json_delta" type`

  - `string partialJSON`

### Beta Input Tokens Clear At Least

- `class BetaInputTokensClearAtLeast`

  - `"input_tokens" type`

  - `int value`

### Beta Input Tokens Trigger

- `class BetaInputTokensTrigger`

  - `"input_tokens" type`

  - `int value`

### Beta Input Transformation

- `class BetaInputTransformation`

  - `class BetaThinkingDroppedInputTransformation`

    - `"thinking_dropped" type`

      Always `thinking_dropped` for this entry type.

    - `string path`

      Where the removed block was in your request, as `messages.{i}.content.{j}`:
      `i` indexes the `messages` array you sent and `j` that message's `content`
      array — the same form error messages use.

    - `Reason reason`

      Which binding check removed the block: `model_binding_mismatch` — it was
      created by a model whose reasoning the requested model may not read;
      `prefix_binding_mismatch` — the conversation before it differs from the
      conversation it was created in (the rest of that turn's consecutive thinking
      blocks are removed with it, each with this reason);
      `organization_binding_mismatch` — it was created under a different
      organization (an Anthropic organization, AWS account or Google Cloud project)
      and this organization is not one of its additional organizations;
      `end_user_binding_mismatch` — it was created for a different end user, or
      was removed by the consumer-organization binding. A block that would fail
      several checks reports one reason, in this order of precedence:
      `organization_binding_mismatch`, `end_user_binding_mismatch`,
      `model_binding_mismatch`, `prefix_binding_mismatch`.

  - `class BetaThinkingMismatchAllowedInputTransformation`

    - `"thinking_mismatch_allowed" type`

      Always `thinking_mismatch_allowed` for this entry type.

    - `string path`

      Where the block is in your request, as `messages.{i}.content.{j}`:
      `i` indexes the `messages` array you sent and `j` that message's `content`
      array — the same form error messages use.

    - `Reason reason`

      Which binding check the block failed; the block was shown to the model all
      the same. Always `prefix_binding_mismatch` today — the conversation before
      the block differs from the conversation it was created in, or the block
      carries no record of one on a model that requires it. Were the check
      enforced for this request, the block would have been removed or the request
      rejected (`thinking.block_binding.prefix_mismatch_behavior`). A removal also
      takes the rest of that turn's consecutive thinking blocks, whereas here each
      block is checked on its own, so `thinking_mismatch_allowed` entries are a
      lower bound on what enforcement would remove.

### Beta Iterations Usage

- `list<BetaIterationsUsageItem>`

  - `class BetaMessageIterationUsage`

    - `"message" type`

      Usage for a sampling iteration

    - `?BetaCacheCreation cacheCreation`

      Breakdown of cached tokens by TTL

    - `int cacheCreationInputTokens`

      The number of input tokens used to create the cache entry.

    - `int cacheReadInputTokens`

      The number of input tokens read from the cache.

    - `int inputTokens`

      The number of input tokens which were used.

    - `?Model model`

      The model that will complete your prompt.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `int outputTokens`

      The number of output tokens which were used.

  - `class BetaCompactionIterationUsage`

    - `"compaction" type`

      Usage for a compaction iteration

    - `?BetaCacheCreation cacheCreation`

      Breakdown of cached tokens by TTL

    - `int cacheCreationInputTokens`

      The number of input tokens used to create the cache entry.

    - `int cacheReadInputTokens`

      The number of input tokens read from the cache.

    - `int inputTokens`

      The number of input tokens which were used.

    - `int outputTokens`

      The number of output tokens which were used.

  - `class BetaAdvisorMessageIterationUsage`

    - `"advisor_message" type`

      Usage for an advisor sub-inference iteration

    - `?BetaCacheCreation cacheCreation`

      Breakdown of cached tokens by TTL

    - `int cacheCreationInputTokens`

      The number of input tokens used to create the cache entry.

    - `int cacheReadInputTokens`

      The number of input tokens read from the cache.

    - `int inputTokens`

      The number of input tokens which were used.

    - `Model model`

      The model that will complete your prompt.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `int outputTokens`

      The number of output tokens which were used.

  - `class BetaFallbackMessageIterationUsage`

    - `"fallback_message" type`

      Usage for the fallback-model attempt that served the response

    - `?BetaCacheCreation cacheCreation`

      Breakdown of cached tokens by TTL

    - `int cacheCreationInputTokens`

      The number of input tokens used to create the cache entry.

    - `int cacheReadInputTokens`

      The number of input tokens read from the cache.

    - `int inputTokens`

      The number of input tokens which were used.

    - `Model model`

      The model that will complete your prompt.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `int outputTokens`

      The number of output tokens which were used.

### Beta JSON Output Format

- `class BetaJSONOutputFormat`

  - `"json_schema" type`

  - `array<string,mixed> schema`

    The JSON schema of the format

### Beta MCP Tool

- `class BetaMCPTool`

  - `array<string,mixed> inputSchema`

  - `string name`

  - `?string description`

### Beta MCP Tool Config

- `class BetaMCPToolConfig`

  - `?bool deferLoading`

  - `?bool enabled`

### Beta MCP Tool Default Config

- `class BetaMCPToolDefaultConfig`

  - `?bool deferLoading`

  - `?bool enabled`

### Beta MCP Tool Listing Block

- `class BetaMCPToolListingBlock`

  - `"mcp_tool_listing" type`

  - `string mcpServerName`

  - `list<BetaMCPTool> tools`

### Beta MCP Tool Listing Block Param

- `class BetaMCPToolListingBlockParam`

  - `"mcp_tool_listing" type`

  - `string mcpServerName`

    The name of the MCP server this listing came from, as `mcp_servers` declares it.

  - `list<BetaMCPToolParam> tools`

    The server's tools, exactly as the response listed them.

### Beta MCP Tool Param

- `class BetaMCPToolParam`

  - `array<string,mixed> inputSchema`

    The tool's input schema as the MCP server lists it, verbatim.

  - `string name`

    The tool's name as the MCP server lists it (not prefixed with the server name).

  - `?string description`

    The tool's description as the MCP server lists it.

### Beta MCP Tool Result Block

- `class BetaMCPToolResultBlock`

  - `"mcp_tool_result" type`

  - `Content content`

  - `bool isError`

  - `string toolUseID`

### Beta MCP Tool Use Block

- `class BetaMCPToolUseBlock`

  - `"mcp_tool_use" type`

  - `string id`

  - `array<string,mixed> input`

  - `string name`

    The name of the MCP tool

  - `string serverName`

    The name of the MCP server

### Beta MCP Tool Use Block Param

- `class BetaMCPToolUseBlockParam`

  - `"mcp_tool_use" type`

  - `string id`

  - `array<string,mixed> input`

  - `string name`

  - `string serverName`

    The name of the MCP server

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

### Beta MCP Toolset

- `class BetaMCPToolset`

  - `"mcp_toolset" type`

  - `string mcpServerName`

    Name of the MCP server to configure tools for

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?array<string,BetaMCPToolConfig> configs`

    Configuration overrides for specific tools, keyed by tool name

  - `?BetaMCPToolDefaultConfig defaultConfig`

    Default configuration applied to all tools from this server

  - `?list<BetaMCPToolParam> tools`

    The server's tool listing, pinned: when present, the server is not asked for its tools before sampling and exactly these entries, with `default_config` and `configs` applied, are the toolset's tools. Copy it from the `mcp_tool_listing` block of an earlier response.

### Beta Memory Tool 20250818

- `class BetaMemoryTool20250818`

  - `"memory_20250818" type`

  - `"memory" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?list<array<string,mixed>> inputExamples`

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Beta Memory Tool 20250818 Command

- `class BetaMemoryTool20250818Command`

  - `class BetaMemoryTool20250818ViewCommand`

    - `"view" command`

      Command type identifier

    - `string path`

      Path to directory or file to view

    - `?list<int> viewRange`

      Optional line range for viewing specific lines

  - `class BetaMemoryTool20250818CreateCommand`

    - `"create" command`

      Command type identifier

    - `string fileText`

      Content to write to the file

    - `string path`

      Path where the file should be created

  - `class BetaMemoryTool20250818StrReplaceCommand`

    - `"str_replace" command`

      Command type identifier

    - `string newStr`

      Text to replace with

    - `string oldStr`

      Text to search for and replace

    - `string path`

      Path to the file where text should be replaced

  - `class BetaMemoryTool20250818InsertCommand`

    - `"insert" command`

      Command type identifier

    - `int insertLine`

      Line number where text should be inserted

    - `string insertText`

      Text to insert at the specified line

    - `string path`

      Path to the file where text should be inserted

  - `class BetaMemoryTool20250818DeleteCommand`

    - `"delete" command`

      Command type identifier

    - `string path`

      Path to the file or directory to delete

  - `class BetaMemoryTool20250818RenameCommand`

    - `"rename" command`

      Command type identifier

    - `string newPath`

      New path for the file or directory

    - `string oldPath`

      Current path of the file or directory

### Beta Memory Tool 20250818 Create Command

- `class BetaMemoryTool20250818CreateCommand`

  - `"create" command`

    Command type identifier

  - `string fileText`

    Content to write to the file

  - `string path`

    Path where the file should be created

### Beta Memory Tool 20250818 Delete Command

- `class BetaMemoryTool20250818DeleteCommand`

  - `"delete" command`

    Command type identifier

  - `string path`

    Path to the file or directory to delete

### Beta Memory Tool 20250818 Insert Command

- `class BetaMemoryTool20250818InsertCommand`

  - `"insert" command`

    Command type identifier

  - `int insertLine`

    Line number where text should be inserted

  - `string insertText`

    Text to insert at the specified line

  - `string path`

    Path to the file where text should be inserted

### Beta Memory Tool 20250818 Rename Command

- `class BetaMemoryTool20250818RenameCommand`

  - `"rename" command`

    Command type identifier

  - `string newPath`

    New path for the file or directory

  - `string oldPath`

    Current path of the file or directory

### Beta Memory Tool 20250818 Str Replace Command

- `class BetaMemoryTool20250818StrReplaceCommand`

  - `"str_replace" command`

    Command type identifier

  - `string newStr`

    Text to replace with

  - `string oldStr`

    Text to search for and replace

  - `string path`

    Path to the file where text should be replaced

### Beta Memory Tool 20250818 View Command

- `class BetaMemoryTool20250818ViewCommand`

  - `"view" command`

    Command type identifier

  - `string path`

    Path to directory or file to view

  - `?list<int> viewRange`

    Optional line range for viewing specific lines

### Beta Message

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

### Beta Message Delta Usage

- `class BetaMessageDeltaUsage`

  - `?int cacheCreationInputTokens`

    The cumulative number of input tokens used to create the cache entry.

  - `?int cacheReadInputTokens`

    The cumulative number of input tokens read from the cache.

  - `?BetaFallbackCreditUsage fallbackCredit`

    Outcome of the `fallback_credit_token` presented on this request.

    Present on every response to a non-batch request that carried a
    `fallback_credit_token`, in either redemption mode; absent otherwise (batch
    items accept and ignore the token and carry no outcome object).

  - `?int inputTokens`

    The cumulative number of input tokens which were used.

  - `?list<BetaIterationsUsageItem> iterations`

    Per-iteration token usage breakdown.

    Each entry represents one sampling iteration, with its own input/output token counts and cache statistics, discriminated by `type`. For `message` entries (model sampling iterations, such as the turns of a server-side tool use loop), this allows you to:

    - Determine which iterations exceeded long context thresholds (>=200k tokens)
    - Calculate the context window size from the last `message` entry
    - Understand token accumulation across server-side tool use loops

    A `compaction` entry reports the token usage of the compaction operation itself — the server-side request that summarizes the context being closed — NOT the size of the context that was compacted away, and its token counts can be much smaller than that closed context (for example, a compaction that closes a ~200k-token context can report only a few thousand tokens). Do not derive the context window size from a `compaction` entry, even when it is the last entry. A `compaction` entry's tokens are not included in the top-level `usage` fields. When an input-token trigger is in effect (the default — 150,000 tokens unless configured otherwise), each `compaction` entry closes a context that had reached at least that threshold, though the context can exceed it by the final iteration's output and tool results.

  - `int outputTokens`

    The cumulative number of output tokens which were used.

  - `?BetaOutputTokensDetails outputTokensDetails`

    Breakdown of output tokens by category.

    `output_tokens` remains the inclusive, authoritative total used for billing.
    This object provides a read-only decomposition for observability — for example,
    how many of the billed output tokens were spent on internal reasoning that may
    have been summarized before being returned to you.

  - `?BetaServerToolUsage serverToolUse`

    The number of server tool requests.

### Beta Message Iteration Usage

- `class BetaMessageIterationUsage`

  - `"message" type`

    Usage for a sampling iteration

  - `?BetaCacheCreation cacheCreation`

    Breakdown of cached tokens by TTL

  - `int cacheCreationInputTokens`

    The number of input tokens used to create the cache entry.

  - `int cacheReadInputTokens`

    The number of input tokens read from the cache.

  - `int inputTokens`

    The number of input tokens which were used.

  - `?Model model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `int outputTokens`

    The number of output tokens which were used.

### Beta Message Param

- `class BetaMessageParam`

  - `Content content`

  - `Role role`

  - `?ClearAt clearAt`

    How long this system message's text stays in front of the model. `"never"` (the default) renders it on every request that includes it. `"next_user_message"` renders it only for the user turn it follows: once a later `role: "user"` message exists in `messages` the message stays in the array (send it unchanged) but is no longer shown to the model. Only permitted on `role: "system"` messages.

  - `?BetaSystemMessageOutputConfig outputConfig`

    Per-message output configuration on a role:"system" input message.

    Fields here apply per-turn; `format` remains top-level only. An
    empty `{}` is accepted on a message that carries content; a message
    with neither content nor output_config fields is rejected.

### Beta Message Tokens Count

- `class BetaMessageTokensCount`

  - `?BetaCountTokensContextManagementResponse contextManagement`

    Information about context management applied to the message.

  - `int inputTokens`

    The total number of tokens across the provided list of messages, system prompt, and tools.

### Beta Metadata

- `class BetaMetadata`

  - `?string userID`

    An external identifier for the user who is associated with the request.

    This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

### Beta Output Config

- `class BetaOutputConfig`

  - `?Effort effort`

    How much effort the model should put into its response. Higher effort levels may result in more thorough analysis but take longer.

    Valid values are `low`, `medium`, `high`, `xhigh`, or `max`.

  - `?BetaJSONOutputFormat format`

    A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

  - `?BetaTokenTaskBudget taskBudget`

    Configuration for token budget tracking across contexts.

### Beta Output Tokens Details

- `class BetaOutputTokensDetails`

  - `int thinkingTokens`

    Number of output tokens the model generated as internal reasoning, including
    the thinking-block delimiter tokens.

    Reflects the raw reasoning the model produced, not the (possibly shorter)
    summarized thinking text returned in the response body. Computed by
    re-tokenizing the raw reasoning text, so it may differ from the model's exact
    generation count by a small number of tokens. Always ≤ `output_tokens`;
    `output_tokens - thinking_tokens` approximates the non-reasoning output.

### Beta Plain Text Source

- `class BetaPlainTextSource`

  - `"text" type`

  - `string data`

  - `"text/plain" mediaType`

### Beta Raw Content Block Delta

- `class BetaRawContentBlockDelta`

  - `class BetaTextDelta`

    - `"text_delta" type`

    - `string text`

  - `class BetaInputJSONDelta`

    - `"input_json_delta" type`

    - `string partialJSON`

  - `class BetaCitationsDelta`

    - `"citations_delta" type`

    - `Citation citation`

  - `class BetaThinkingDelta`

    - `"thinking_delta" type`

    - `?int estimatedTokens`

      Per-frame increment of a coarse, running estimate of the tokens this thinking block has produced so far. Present whenever the `thinking-token-count-2026-05-13` beta is set; `null` unless `thinking.display` resolves to `"omitted"` and a count is due this frame. Sum the increments across `thinking_delta` frames on this block for a progress indicator. Each increment is a non-negative multiple of a fixed quantum and the cadence is rate-limited, so this is a deliberately lossy display hint, not a billable count; `usage.output_tokens` remains authoritative.

    - `string thinking`

      The incremental `thinking` text for this content block. Concatenate the `thinking` values of successive `thinking_delta` events to assemble the block's full `thinking` value.

  - `class BetaSignatureDelta`

    - `"signature_delta" type`

    - `string signature`

      The `signature` for this thinking block: an opaque value used to verify that the block was generated by Claude when it is passed back to the API. Delivered in a `signature_delta` event just before the block's `content_block_stop` event.

  - `class BetaCompactionContentBlockDelta`

    - `"compaction_delta" type`

    - `?string content`

    - `?string encryptedContent`

      Opaque metadata from prior compaction, to be round-tripped verbatim

### Beta Raw Content Block Delta Event

- `class BetaRawContentBlockDeltaEvent`

  - `"content_block_delta" type`

  - `BetaRawContentBlockDelta delta`

  - `int index`

### Beta Raw Content Block Start Event

- `class BetaRawContentBlockStartEvent`

  - `"content_block_start" type`

  - `ContentBlock contentBlock`

  - `int index`

### Beta Raw Content Block Stop Event

- `class BetaRawContentBlockStopEvent`

  - `"content_block_stop" type`

  - `int index`

### Beta Raw Message Delta Event

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

### Beta Raw Message Start Event

- `class BetaRawMessageStartEvent`

  - `"message_start" type`

  - `BetaMessage message`

### Beta Raw Message Stop Event

- `class BetaRawMessageStopEvent`

  - `"message_stop" type`

### Beta Raw Message Stream Event

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

### Beta Redacted Thinking Block

- `class BetaRedactedThinkingBlock`

  - `"redacted_thinking" type`

  - `string data`

    The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

    Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

    See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

### Beta Redacted Thinking Block Param

- `class BetaRedactedThinkingBlockParam`

  - `"redacted_thinking" type`

  - `string data`

    The `data` value of this redacted thinking block, exactly as returned by the API in a previous response. Opaque and encrypted; pass it back unchanged.

### Beta Refusal Stop Details

- `class BetaRefusalStopDetails`

  - `"refusal" type`

  - `?Category category`

    The policy category that triggered the refusal.

    `null` when the refusal doesn't map to a named category.

  - `?string explanation`

    Human-readable explanation of the refusal.

    This text is not guaranteed to be stable. `null` when no explanation is available for the category.

  - `?string fallbackCreditToken`

    Opaque code that refunds the cache-miss cost when retrying this refused
    request on the fallback model. Pass it as `fallback_credit_token` on the
    retry request. Expires 5 minutes after the refusal.

    The retry is sent either with the same request body (`system`, `messages`,
    `tools`, and other render-shaping fields), or with the same body plus one
    appended `assistant` message whose content is the partial text (with any
    trailing whitespace stripped from the final text block) and paired
    server-tool blocks from this refusal — which also authorizes that
    appended turn as an assistant-prefill continuation on models that otherwise
    disallow prefill. A token minted mid-server-tool-loop whose partial content
    was continuable may only be redeemed the second way — if a same-body retry
    is rejected with a 400 saying the token must be redeemed by continuing the
    partial response, retry the second way instead. Either way: same workspace,
    same platform; a mismatch is a 400. Resending a token for an already-warm
    prefix is permitted but yields no additional credit.

    `null` when the refused model isn't eligible for a fallback credit.

  - `?bool fallbackHasPrefillClaim`

    Whether the accompanying `fallback_credit_token` may be redeemed with the
    appended-assistant retry form. Only set when `fallback_credit_token` is
    present.

    `true`: retry by resending the same request body plus one appended
    `assistant` message whose content is this response's `content` with any
    trailing whitespace stripped from the final text block and unpaired
    `tool_use` blocks omitted (the same appended-turn shape described on
    `fallback_credit_token`), with the token attached. `false`: retry by
    resending the original request body unchanged, with the token attached —
    the appended-assistant form is not available for this refusal (no
    continuable partial content, or the request uses `output_format` or a
    `tool_choice` that forces tool use). One exception: when the request used
    `output_format` or a forced `tool_choice` and the refusal arrived after
    server tools (including MCP connector tools) had already executed, the
    token may not be redeemable by either retry form; if the exact-body retry
    is then rejected with a 400 saying the token must be redeemed by
    continuing the partial response, discard the token and retry without it.

    Advisory: if an appended-assistant retry is rejected with a 400 despite
    `true`, fall back to resending the original request body with the token.

  - `?string recommendedModel`

    The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

### Beta Request Document Block

- `class BetaRequestDocumentBlock`

  - `"document" type`

  - `Source source`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?BetaCitationsConfigParam citations`

  - `?string context`

  - `?string title`

### Beta Request MCP Server Tool Configuration

- `class BetaRequestMCPServerToolConfiguration`

  - `?list<string> allowedTools`

  - `?bool enabled`

### Beta Request MCP Server URL Definition

- `class BetaRequestMCPServerURLDefinition`

  - `"url" type`

  - `string name`

  - `string url`

  - `?string authorizationToken`

  - `?BetaRequestMCPServerToolConfiguration toolConfiguration`

### Beta Request MCP Tool Result Block Param

- `class BetaRequestMCPToolResultBlockParam`

  - `"mcp_tool_result" type`

  - `string toolUseID`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?Content content`

  - `?bool isError`

### Beta Request Tool Addition Block

- `class BetaRequestToolAdditionBlock`

  - `"tool_addition" type`

  - `Tool tool`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

### Beta Request Tool Removal Block

- `class BetaRequestToolRemovalBlock`

  - `"tool_removal" type`

  - `Tool tool`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

### Beta Response Tool

- `class BetaResponseTool`

  - `?Type type`

  - `BetaResponseToolInputSchema inputSchema`

    [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

    This defines the shape of the `input` that your tool accepts and that the model will produce.

  - `string name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?string description`

    Description of what this tool does.

    Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

  - `?bool eagerInputStreaming`

    Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

  - `?list<array<string,mixed>> inputExamples`

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Beta Response Tool Addition Block

- `class BetaResponseToolAdditionBlock`

  - `"tool_addition" type`

  - `Tool tool`

    The tool made available: a reference to a `tools` entry or MCP toolset, or a `tool_definition` carrying the definition by value.

### Beta Response Tool Change MCP Tool Reference

- `class BetaResponseToolChangeMCPToolReference`

  - `"mcp_tool_reference" type`

  - `string name`

  - `string serverName`

### Beta Response Tool Change MCP Toolset Reference

- `class BetaResponseToolChangeMCPToolsetReference`

  - `"mcp_toolset_reference" type`

  - `string serverName`

### Beta Response Tool Change Tool Reference

- `class BetaResponseToolChangeToolReference`

  - `"tool_reference" type`

  - `string name`

### Beta Response Tool Input Schema

- `class BetaResponseToolInputSchema`

  - `"object" type`

  - `?array<string,mixed> properties`

  - `?list<string> required`

### Beta Response Tool Removal Block

- `class BetaResponseToolRemovalBlock`

  - `"tool_removal" type`

  - `Tool tool`

    A reference to the withdrawn `tools` entry, MCP tool or MCP toolset.

### Beta Response Tool Union

- `class BetaResponseToolUnion`

  - `class BetaResponseTool`

    - `?Type type`

    - `BetaResponseToolInputSchema inputSchema`

      [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

      This defines the shape of the `input` that your tool accepts and that the model will produce.

    - `string name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?string description`

      Description of what this tool does.

      Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

    - `?bool eagerInputStreaming`

      Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaToolBash20241022`

    - `"bash_20241022" type`

    - `"bash" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaToolBash20250124`

    - `"bash_20250124" type`

    - `"bash" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaCodeExecutionTool20250522`

    - `"code_execution_20250522" type`

    - `"code_execution" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaCodeExecutionTool20250825`

    - `"code_execution_20250825" type`

    - `"code_execution" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaCodeExecutionTool20260120`

    - `"code_execution_20260120" type`

    - `"code_execution" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaCodeExecutionTool20260521`

    - `"code_execution_20260521" type`

    - `"code_execution" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaBrowserToolset20260801`

    - `"browser_toolset_20260801" type`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?BetaBrowserToolsetConfigs configs`

      Sparse per-member overrides, keyed by member name. Absent, null, and {} are equivalent; a member's defaults apply wherever its key is absent.

  - `class BetaToolComputerUse20241022`

    - `"computer_20241022" type`

    - `int displayHeightPx`

      The height of the display in pixels.

    - `int displayWidthPx`

      The width of the display in pixels.

    - `"computer" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int displayNumber`

      The X11 display number (e.g. 0, 1) for the display.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaMemoryTool20250818`

    - `"memory_20250818" type`

    - `"memory" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaToolComputerUse20250124`

    - `"computer_20250124" type`

    - `int displayHeightPx`

      The height of the display in pixels.

    - `int displayWidthPx`

      The width of the display in pixels.

    - `"computer" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int displayNumber`

      The X11 display number (e.g. 0, 1) for the display.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaToolTextEditor20241022`

    - `"text_editor_20241022" type`

    - `"str_replace_editor" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaToolComputerUse20251124`

    - `"computer_20251124" type`

    - `int displayHeightPx`

      The height of the display in pixels.

    - `int displayWidthPx`

      The width of the display in pixels.

    - `"computer" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int displayNumber`

      The X11 display number (e.g. 0, 1) for the display.

    - `?bool enableZoom`

      Whether to enable an action to take a zoomed-in screenshot of the screen.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaComputerToolset20260801`

    - `"computer_toolset_20260801" type`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?BetaComputerToolsetConfigs configs`

      Sparse per-member overrides, keyed by member name. Absent, null, and {} are equivalent; a member's defaults apply wherever its key is absent.

  - `class BetaToolTextEditor20250124`

    - `"text_editor_20250124" type`

    - `"str_replace_editor" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaToolTextEditor20250429`

    - `"text_editor_20250429" type`

    - `"str_replace_based_edit_tool" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaToolTextEditor20250728`

    - `"text_editor_20250728" type`

    - `"str_replace_based_edit_tool" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?int maxCharacters`

      Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaWebSearchTool20250305`

    - `"web_search_20250305" type`

    - `"web_search" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `?list<string> blockedDomains`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

    - `?BetaUserLocation userLocation`

      Parameters for the user's location. Used to provide more relevant search results.

  - `class BetaWebFetchTool20250910`

    - `"web_fetch_20250910" type`

    - `"web_fetch" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      List of domains to allow fetching from

    - `?list<string> blockedDomains`

      List of domains to block fetching from

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?BetaCitationsConfigParam citations`

      Citations configuration for fetched documents. Citations are disabled by default.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxContentTokens`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

    - `?BetaWebFetchURLSources urlSources`

      Which sources contribute to the set of URLs the tool may fetch. Omitted means every source.

  - `class BetaWebSearchTool20260209`

    - `"web_search_20260209" type`

    - `"web_search" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `?list<string> blockedDomains`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

    - `?BetaUserLocation userLocation`

      Parameters for the user's location. Used to provide more relevant search results.

  - `class BetaWebFetchTool20260209`

    - `"web_fetch_20260209" type`

    - `"web_fetch" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      List of domains to allow fetching from

    - `?list<string> blockedDomains`

      List of domains to block fetching from

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?BetaCitationsConfigParam citations`

      Citations configuration for fetched documents. Citations are disabled by default.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxContentTokens`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

    - `?BetaWebFetchURLSources urlSources`

      Which sources contribute to the set of URLs the tool may fetch. Omitted means every source.

  - `class BetaWebFetchTool20260309`

    - `"web_fetch_20260309" type`

    - `"web_fetch" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      List of domains to allow fetching from

    - `?list<string> blockedDomains`

      List of domains to block fetching from

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?BetaCitationsConfigParam citations`

      Citations configuration for fetched documents. Citations are disabled by default.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxContentTokens`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

    - `?BetaWebFetchURLSources urlSources`

      Which sources contribute to the set of URLs the tool may fetch. Omitted means every source.

    - `?bool useCache`

      Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

  - `class BetaWebSearchTool20260318`

    - `"web_search_20260318" type`

    - `"web_search" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `?list<string> blockedDomains`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?ResponseInclusion responseInclusion`

      How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

    - `?BetaUserLocation userLocation`

      Parameters for the user's location. Used to provide more relevant search results.

  - `class BetaWebFetchTool20260318`

    - `"web_fetch_20260318" type`

    - `"web_fetch" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      List of domains to allow fetching from

    - `?list<string> blockedDomains`

      List of domains to block fetching from

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?BetaCitationsConfigParam citations`

      Citations configuration for fetched documents. Citations are disabled by default.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxContentTokens`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?ResponseInclusion responseInclusion`

      How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

    - `?BetaWebFetchURLSources urlSources`

      Which sources contribute to the set of URLs the tool may fetch. Omitted means every source.

    - `?bool useCache`

      Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

  - `class BetaAdvisorTool20260301`

    - `"advisor_20260301" type`

    - `Model model`

      The model that will complete your prompt.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `"advisor" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?BetaCacheControlEphemeral caching`

      Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxTokens`

      Bounds the advisor's total output (thinking + text) per call. When the advisor hits this cap, the returned advisor_result or advisor_redacted_result block carries stop_reason='max_tokens', and a truncation note is appended to the advice text the worker model sees (inside the encrypted blob in redacted mode). When set, the server also emits a remaining-tokens budget block in the advisor's prompt so the advisor self-shapes toward the cap. When omitted, the advisor model's default output cap applies and no budget block is emitted.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaToolSearchToolBm25_20251119`

    - `Type type`

    - `"tool_search_tool_bm25" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaToolSearchToolRegex20251119`

    - `Type type`

    - `"tool_search_tool_regex" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaMCPToolset`

    - `"mcp_toolset" type`

    - `string mcpServerName`

      Name of the MCP server to configure tools for

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?array<string,BetaMCPToolConfig> configs`

      Configuration overrides for specific tools, keyed by tool name

    - `?BetaMCPToolDefaultConfig defaultConfig`

      Default configuration applied to all tools from this server

    - `?list<BetaMCPToolParam> tools`

      The server's tool listing, pinned: when present, the server is not asked for its tools before sampling and exactly these entries, with `default_config` and `configs` applied, are the toolset's tools. Copy it from the `mcp_tool_listing` block of an earlier response.

### Beta Search Result Block Param

- `class BetaSearchResultBlockParam`

  - `"search_result" type`

  - `list<BetaTextBlockParam> content`

  - `string source`

  - `string title`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?BetaCitationsConfigParam citations`

### Beta Server Tool Caller

- `class BetaServerToolCaller`

  - `"code_execution_20250825" type`

  - `string toolID`

### Beta Server Tool Caller 20260120

- `class BetaServerToolCaller20260120`

  - `"code_execution_20260120" type`

  - `string toolID`

### Beta Server Tool Usage

- `class BetaServerToolUsage`

  - `int webFetchRequests`

    The number of web fetch tool requests.

  - `int webSearchRequests`

    The number of web search tool requests.

### Beta Server Tool Use Block

- `class BetaServerToolUseBlock`

  - `"server_tool_use" type`

  - `string id`

  - `array<string,mixed> input`

  - `Name name`

  - `?Caller caller`

### Beta Server Tool Use Block Param

- `class BetaServerToolUseBlockParam`

  - `"server_tool_use" type`

  - `string id`

  - `array<string,mixed> input`

  - `Name name`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?Caller caller`

### Beta Signature Delta

- `class BetaSignatureDelta`

  - `"signature_delta" type`

  - `string signature`

    The `signature` for this thinking block: an opaque value used to verify that the block was generated by Claude when it is passed back to the API. Delivered in a `signature_delta` event just before the block's `content_block_stop` event.

### Beta Skill Params

- `class BetaSkillParams`

  - `Type type`

    Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

  - `string skillID`

    Skill ID

  - `?string version`

    Skill version or 'latest' for most recent version

### Beta Stop Reason

- `enum BetaStopReason`

  - `"end_turn"`

  - `"max_tokens"`

  - `"stop_sequence"`

  - `"tool_use"`

  - `"pause_turn"`

  - `"compaction"`

  - `"refusal"`

  - `"model_context_window_exceeded"`

### Beta Summarize Compaction

- `class BetaSummarizeCompaction`

  - `"summarize" type`

  - `?string instructions`

    Replaces the server's default summarization prompt for this request. An empty or whitespace-only value counts as absent.

### Beta System Message Output Config

- `class BetaSystemMessageOutputConfig`

  - `?Effort effort`

    How much effort the model should put into its response. Higher effort levels may result in more thorough analysis but take longer.

    Valid values are `low`, `medium`, `high`, `xhigh`, or `max`.

### Beta Text Block

- `class BetaTextBlock`

  - `"text" type`

  - `?list<BetaTextCitation> citations`

    Citations supporting the text block.

    The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

  - `string text`

### Beta Text Block Param

- `class BetaTextBlockParam`

  - `"text" type`

  - `string text`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?list<BetaTextCitationParam> citations`

### Beta Text Citation

- `class BetaTextCitation`

  - `class BetaCitationCharLocation`

    - `"char_location" type`

    - `string citedText`

    - `int documentIndex`

    - `?string documentTitle`

    - `int endCharIndex`

    - `?string fileID`

    - `int startCharIndex`

  - `class BetaCitationPageLocation`

    - `"page_location" type`

    - `string citedText`

    - `int documentIndex`

    - `?string documentTitle`

    - `int endPageNumber`

    - `?string fileID`

    - `int startPageNumber`

  - `class BetaCitationContentBlockLocation`

    - `"content_block_location" type`

    - `string citedText`

      The full text of the cited block range, concatenated.

      Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

    - `int documentIndex`

    - `?string documentTitle`

    - `int endBlockIndex`

      Exclusive 0-based end index of the cited block range in the source's `content` array.

      Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

    - `?string fileID`

    - `int startBlockIndex`

      0-based index of the first cited block in the source's `content` array.

  - `class BetaCitationsWebSearchResultLocation`

    - `"web_search_result_location" type`

    - `string citedText`

    - `string encryptedIndex`

    - `?string title`

    - `string url`

  - `class BetaCitationSearchResultLocation`

    - `"search_result_location" type`

    - `string citedText`

      The full text of the cited block range, concatenated.

      Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

    - `int endBlockIndex`

      Exclusive 0-based end index of the cited block range in the source's `content` array.

      Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

    - `int searchResultIndex`

      0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

      Counted separately from `document_index`; server-side web search results are not included in this count.

    - `string source`

    - `int startBlockIndex`

      0-based index of the first cited block in the source's `content` array.

    - `?string title`

### Beta Text Citation Param

- `class BetaTextCitationParam`

  - `class BetaCitationCharLocationParam`

    - `"char_location" type`

    - `string citedText`

    - `int documentIndex`

    - `?string documentTitle`

    - `int endCharIndex`

    - `int startCharIndex`

  - `class BetaCitationPageLocationParam`

    - `"page_location" type`

    - `string citedText`

    - `int documentIndex`

    - `?string documentTitle`

    - `int endPageNumber`

    - `int startPageNumber`

  - `class BetaCitationContentBlockLocationParam`

    - `"content_block_location" type`

    - `string citedText`

      The full text of the cited block range, concatenated.

      Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

    - `int documentIndex`

    - `?string documentTitle`

    - `int endBlockIndex`

      Exclusive 0-based end index of the cited block range in the source's `content` array.

      Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

    - `int startBlockIndex`

      0-based index of the first cited block in the source's `content` array.

  - `class BetaCitationWebSearchResultLocationParam`

    - `"web_search_result_location" type`

    - `string citedText`

    - `string encryptedIndex`

    - `?string title`

    - `string url`

  - `class BetaCitationSearchResultLocationParam`

    - `"search_result_location" type`

    - `string citedText`

      The full text of the cited block range, concatenated.

      Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

    - `int endBlockIndex`

      Exclusive 0-based end index of the cited block range in the source's `content` array.

      Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

    - `int searchResultIndex`

      0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

      Counted separately from `document_index`; server-side web search results are not included in this count.

    - `string source`

    - `int startBlockIndex`

      0-based index of the first cited block in the source's `content` array.

    - `?string title`

### Beta Text Delta

- `class BetaTextDelta`

  - `"text_delta" type`

  - `string text`

### Beta Text Editor Code Execution Create Result Block

- `class BetaTextEditorCodeExecutionCreateResultBlock`

  - `"text_editor_code_execution_create_result" type`

  - `bool isFileUpdate`

### Beta Text Editor Code Execution Create Result Block Param

- `class BetaTextEditorCodeExecutionCreateResultBlockParam`

  - `"text_editor_code_execution_create_result" type`

  - `bool isFileUpdate`

### Beta Text Editor Code Execution Str Replace Result Block

- `class BetaTextEditorCodeExecutionStrReplaceResultBlock`

  - `"text_editor_code_execution_str_replace_result" type`

  - `?list<string> lines`

  - `?int newLines`

  - `?int newStart`

  - `?int oldLines`

  - `?int oldStart`

### Beta Text Editor Code Execution Str Replace Result Block Param

- `class BetaTextEditorCodeExecutionStrReplaceResultBlockParam`

  - `"text_editor_code_execution_str_replace_result" type`

  - `?list<string> lines`

  - `?int newLines`

  - `?int newStart`

  - `?int oldLines`

  - `?int oldStart`

### Beta Text Editor Code Execution Tool Result Block

- `class BetaTextEditorCodeExecutionToolResultBlock`

  - `"text_editor_code_execution_tool_result" type`

  - `Content content`

  - `string toolUseID`

### Beta Text Editor Code Execution Tool Result Block Param

- `class BetaTextEditorCodeExecutionToolResultBlockParam`

  - `"text_editor_code_execution_tool_result" type`

  - `Content content`

  - `string toolUseID`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

### Beta Text Editor Code Execution Tool Result Error

- `class BetaTextEditorCodeExecutionToolResultError`

  - `"text_editor_code_execution_tool_result_error" type`

  - `ErrorCode errorCode`

  - `?string errorMessage`

### Beta Text Editor Code Execution Tool Result Error Param

- `class BetaTextEditorCodeExecutionToolResultErrorParam`

  - `"text_editor_code_execution_tool_result_error" type`

  - `ErrorCode errorCode`

  - `?string errorMessage`

### Beta Text Editor Code Execution View Result Block

- `class BetaTextEditorCodeExecutionViewResultBlock`

  - `"text_editor_code_execution_view_result" type`

  - `string content`

  - `FileType fileType`

  - `?int numLines`

  - `?int startLine`

  - `?int totalLines`

### Beta Text Editor Code Execution View Result Block Param

- `class BetaTextEditorCodeExecutionViewResultBlockParam`

  - `"text_editor_code_execution_view_result" type`

  - `string content`

  - `FileType fileType`

  - `?int numLines`

  - `?int startLine`

  - `?int totalLines`

### Beta Thinking Block

- `class BetaThinkingBlock`

  - `"thinking" type`

  - `string signature`

    A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

    This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

    See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

  - `string thinking`

    The text of Claude's thinking process for this block.

### Beta Thinking Block Binding

- `class BetaThinkingBlockBinding`

  - `?BetaThinkingPrefixMismatchBehavior prefixMismatchBehavior`

    "error" (default) | "drop_block". What happens when a thinking block in `messages` fails the conversation check (it was created in a different conversation, or the messages before it have changed since). "error" fails the request with a 400 error. "drop_block" removes the failing blocks and the request proceeds; each removal is reported in `input_transformations`.

### Beta Thinking Block Param

- `class BetaThinkingBlockParam`

  - `"thinking" type`

  - `string signature`

    The `signature` value of this thinking block, exactly as returned by the API in a previous response. Used to verify that the block was generated by Claude.

    Thinking blocks must be passed back unmodified and in their original order; a modified block results in a 400 `invalid_request_error`.

  - `string thinking`

    The `thinking` text of this block as returned by the API.

### Beta Thinking Config Adaptive

- `class BetaThinkingConfigAdaptive`

  - `"adaptive" type`

  - `?BetaThinkingBlockBinding blockBinding`

    Controls for block binding: what happens when a thinking block this request sends back fails the conversation check. `null`, absent or an empty object means every default.

  - `?Display display`

    Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

### Beta Thinking Config Disabled

- `class BetaThinkingConfigDisabled`

  - `"disabled" type`

### Beta Thinking Config Enabled

- `class BetaThinkingConfigEnabled`

  - `"enabled" type`

  - `int budgetTokens`

    Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

    Must be ≥1024 and less than `max_tokens`.

    See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

  - `?BetaThinkingBlockBinding blockBinding`

    Controls for block binding: what happens when a thinking block this request sends back fails the conversation check. `null`, absent or an empty object means every default.

  - `?Display display`

    Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

### Beta Thinking Config Param

- `class BetaThinkingConfigParam`

  - `class BetaThinkingConfigEnabled`

    - `"enabled" type`

    - `int budgetTokens`

      Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

      Must be ≥1024 and less than `max_tokens`.

      See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

    - `?BetaThinkingBlockBinding blockBinding`

      Controls for block binding: what happens when a thinking block this request sends back fails the conversation check. `null`, absent or an empty object means every default.

    - `?Display display`

      Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

  - `class BetaThinkingConfigDisabled`

    - `"disabled" type`

  - `class BetaThinkingConfigAdaptive`

    - `"adaptive" type`

    - `?BetaThinkingBlockBinding blockBinding`

      Controls for block binding: what happens when a thinking block this request sends back fails the conversation check. `null`, absent or an empty object means every default.

    - `?Display display`

      Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

### Beta Thinking Delta

- `class BetaThinkingDelta`

  - `"thinking_delta" type`

  - `?int estimatedTokens`

    Per-frame increment of a coarse, running estimate of the tokens this thinking block has produced so far. Present whenever the `thinking-token-count-2026-05-13` beta is set; `null` unless `thinking.display` resolves to `"omitted"` and a count is due this frame. Sum the increments across `thinking_delta` frames on this block for a progress indicator. Each increment is a non-negative multiple of a fixed quantum and the cadence is rate-limited, so this is a deliberately lossy display hint, not a billable count; `usage.output_tokens` remains authoritative.

  - `string thinking`

    The incremental `thinking` text for this content block. Concatenate the `thinking` values of successive `thinking_delta` events to assemble the block's full `thinking` value.

### Beta Thinking Dropped Input Transformation

- `class BetaThinkingDroppedInputTransformation`

  - `"thinking_dropped" type`

    Always `thinking_dropped` for this entry type.

  - `string path`

    Where the removed block was in your request, as `messages.{i}.content.{j}`:
    `i` indexes the `messages` array you sent and `j` that message's `content`
    array — the same form error messages use.

  - `Reason reason`

    Which binding check removed the block: `model_binding_mismatch` — it was
    created by a model whose reasoning the requested model may not read;
    `prefix_binding_mismatch` — the conversation before it differs from the
    conversation it was created in (the rest of that turn's consecutive thinking
    blocks are removed with it, each with this reason);
    `organization_binding_mismatch` — it was created under a different
    organization (an Anthropic organization, AWS account or Google Cloud project)
    and this organization is not one of its additional organizations;
    `end_user_binding_mismatch` — it was created for a different end user, or
    was removed by the consumer-organization binding. A block that would fail
    several checks reports one reason, in this order of precedence:
    `organization_binding_mismatch`, `end_user_binding_mismatch`,
    `model_binding_mismatch`, `prefix_binding_mismatch`.

### Beta Thinking Mismatch Allowed Input Transformation

- `class BetaThinkingMismatchAllowedInputTransformation`

  - `"thinking_mismatch_allowed" type`

    Always `thinking_mismatch_allowed` for this entry type.

  - `string path`

    Where the block is in your request, as `messages.{i}.content.{j}`:
    `i` indexes the `messages` array you sent and `j` that message's `content`
    array — the same form error messages use.

  - `Reason reason`

    Which binding check the block failed; the block was shown to the model all
    the same. Always `prefix_binding_mismatch` today — the conversation before
    the block differs from the conversation it was created in, or the block
    carries no record of one on a model that requires it. Were the check
    enforced for this request, the block would have been removed or the request
    rejected (`thinking.block_binding.prefix_mismatch_behavior`). A removal also
    takes the rest of that turn's consecutive thinking blocks, whereas here each
    block is checked on its own, so `thinking_mismatch_allowed` entries are a
    lower bound on what enforcement would remove.

### Beta Thinking Prefix Mismatch Behavior

- `enum BetaThinkingPrefixMismatchBehavior`

  - `"error"`

  - `"drop_block"`

### Beta Thinking Turns

- `class BetaThinkingTurns`

  - `"thinking_turns" type`

  - `int value`

### Beta Token Task Budget

- `class BetaTokenTaskBudget`

  - `"tokens" type`

    The budget type. Currently only 'tokens' is supported.

  - `int total`

    Total token budget across all contexts in the session.

  - `?int remaining`

    Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.

### Beta Tool

- `class BetaTool`

  - `?Type type`

  - `InputSchema inputSchema`

    [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

    This defines the shape of the `input` that your tool accepts and that the model will produce.

  - `string name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?string description`

    Description of what this tool does.

    Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

  - `?bool eagerInputStreaming`

    Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

  - `?list<array<string,mixed>> inputExamples`

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Beta Tool Bash 20241022

- `class BetaToolBash20241022`

  - `"bash_20241022" type`

  - `"bash" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?list<array<string,mixed>> inputExamples`

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Beta Tool Bash 20250124

- `class BetaToolBash20250124`

  - `"bash_20250124" type`

  - `"bash" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?list<array<string,mixed>> inputExamples`

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Beta Tool Change MCP Tool Reference

- `class BetaToolChangeMCPToolReference`

  - `"mcp_tool_reference" type`

  - `string name`

  - `string serverName`

### Beta Tool Change MCP Toolset Reference

- `class BetaToolChangeMCPToolsetReference`

  - `"mcp_toolset_reference" type`

  - `string serverName`

### Beta Tool Change Tool Definition

- `class BetaToolChangeToolDefinition`

  - `"tool_definition" type`

  - `BetaResponseToolUnion definition`

### Beta Tool Change Tool Definition Param

- `class BetaToolChangeToolDefinitionParam`

  - `"tool_definition" type`

  - `BetaToolUnion definition`

### Beta Tool Change Tool Reference

- `class BetaToolChangeToolReference`

  - `"tool_reference" type`

  - `string name`

### Beta Tool Choice

- `class BetaToolChoice`

  - `class BetaToolChoiceAuto`

    - `"auto" type`

    - `?bool disableParallelToolUse`

      Whether to disable parallel tool use.

      Defaults to `false`. If set to `true`, the model will output at most one tool use.

  - `class BetaToolChoiceAny`

    - `"any" type`

    - `?bool disableParallelToolUse`

      Whether to disable parallel tool use.

      Defaults to `false`. If set to `true`, the model will output exactly one tool use.

  - `class BetaToolChoiceTool`

    - `"tool" type`

    - `string name`

      The name of the tool to use.

    - `?bool disableParallelToolUse`

      Whether to disable parallel tool use.

      Defaults to `false`. If set to `true`, the model will output exactly one tool use.

  - `class BetaToolChoiceNone`

    - `"none" type`

### Beta Tool Choice Any

- `class BetaToolChoiceAny`

  - `"any" type`

  - `?bool disableParallelToolUse`

    Whether to disable parallel tool use.

    Defaults to `false`. If set to `true`, the model will output exactly one tool use.

### Beta Tool Choice Auto

- `class BetaToolChoiceAuto`

  - `"auto" type`

  - `?bool disableParallelToolUse`

    Whether to disable parallel tool use.

    Defaults to `false`. If set to `true`, the model will output at most one tool use.

### Beta Tool Choice None

- `class BetaToolChoiceNone`

  - `"none" type`

### Beta Tool Choice Tool

- `class BetaToolChoiceTool`

  - `"tool" type`

  - `string name`

    The name of the tool to use.

  - `?bool disableParallelToolUse`

    Whether to disable parallel tool use.

    Defaults to `false`. If set to `true`, the model will output exactly one tool use.

### Beta Tool Computer Use 20241022

- `class BetaToolComputerUse20241022`

  - `"computer_20241022" type`

  - `int displayHeightPx`

    The height of the display in pixels.

  - `int displayWidthPx`

    The width of the display in pixels.

  - `"computer" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?int displayNumber`

    The X11 display number (e.g. 0, 1) for the display.

  - `?list<array<string,mixed>> inputExamples`

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Beta Tool Computer Use 20250124

- `class BetaToolComputerUse20250124`

  - `"computer_20250124" type`

  - `int displayHeightPx`

    The height of the display in pixels.

  - `int displayWidthPx`

    The width of the display in pixels.

  - `"computer" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?int displayNumber`

    The X11 display number (e.g. 0, 1) for the display.

  - `?list<array<string,mixed>> inputExamples`

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Beta Tool Computer Use 20251124

- `class BetaToolComputerUse20251124`

  - `"computer_20251124" type`

  - `int displayHeightPx`

    The height of the display in pixels.

  - `int displayWidthPx`

    The width of the display in pixels.

  - `"computer" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?int displayNumber`

    The X11 display number (e.g. 0, 1) for the display.

  - `?bool enableZoom`

    Whether to enable an action to take a zoomed-in screenshot of the screen.

  - `?list<array<string,mixed>> inputExamples`

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Beta Tool Reference Block

- `class BetaToolReferenceBlock`

  - `"tool_reference" type`

  - `string toolName`

### Beta Tool Reference Block Param

- `class BetaToolReferenceBlockParam`

  - `"tool_reference" type`

  - `string toolName`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

### Beta Tool Result Block Param

- `class BetaToolResultBlockParam`

  - `"tool_result" type`

  - `string toolUseID`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?Content content`

  - `?bool isError`

  - `?string toolsetName`

    For a toolset member tool_result, the toolset family of the paired tool_use.

### Beta Tool Search Tool Bm25 20251119

- `class BetaToolSearchToolBm25_20251119`

  - `Type type`

  - `"tool_search_tool_bm25" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Beta Tool Search Tool Regex 20251119

- `class BetaToolSearchToolRegex20251119`

  - `Type type`

  - `"tool_search_tool_regex" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Beta Tool Search Tool Result Block

- `class BetaToolSearchToolResultBlock`

  - `"tool_search_tool_result" type`

  - `Content content`

  - `string toolUseID`

### Beta Tool Search Tool Result Block Param

- `class BetaToolSearchToolResultBlockParam`

  - `"tool_search_tool_result" type`

  - `Content content`

  - `string toolUseID`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

### Beta Tool Search Tool Result Error

- `class BetaToolSearchToolResultError`

  - `"tool_search_tool_result_error" type`

  - `ErrorCode errorCode`

  - `?string errorMessage`

### Beta Tool Search Tool Result Error Param

- `class BetaToolSearchToolResultErrorParam`

  - `"tool_search_tool_result_error" type`

  - `ErrorCode errorCode`

  - `?string errorMessage`

### Beta Tool Search Tool Search Result Block

- `class BetaToolSearchToolSearchResultBlock`

  - `"tool_search_tool_search_result" type`

  - `list<BetaToolReferenceBlock> toolReferences`

### Beta Tool Search Tool Search Result Block Param

- `class BetaToolSearchToolSearchResultBlockParam`

  - `"tool_search_tool_search_result" type`

  - `list<BetaToolReferenceBlockParam> toolReferences`

### Beta Tool Text Editor 20241022

- `class BetaToolTextEditor20241022`

  - `"text_editor_20241022" type`

  - `"str_replace_editor" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?list<array<string,mixed>> inputExamples`

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Beta Tool Text Editor 20250124

- `class BetaToolTextEditor20250124`

  - `"text_editor_20250124" type`

  - `"str_replace_editor" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?list<array<string,mixed>> inputExamples`

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Beta Tool Text Editor 20250429

- `class BetaToolTextEditor20250429`

  - `"text_editor_20250429" type`

  - `"str_replace_based_edit_tool" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?list<array<string,mixed>> inputExamples`

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Beta Tool Text Editor 20250728

- `class BetaToolTextEditor20250728`

  - `"text_editor_20250728" type`

  - `"str_replace_based_edit_tool" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?list<array<string,mixed>> inputExamples`

  - `?int maxCharacters`

    Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Beta Tool Union

- `class BetaToolUnion`

  - `class BetaTool`

    - `?Type type`

    - `InputSchema inputSchema`

      [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

      This defines the shape of the `input` that your tool accepts and that the model will produce.

    - `string name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?string description`

      Description of what this tool does.

      Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

    - `?bool eagerInputStreaming`

      Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaToolBash20241022`

    - `"bash_20241022" type`

    - `"bash" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaToolBash20250124`

    - `"bash_20250124" type`

    - `"bash" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaCodeExecutionTool20250522`

    - `"code_execution_20250522" type`

    - `"code_execution" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaCodeExecutionTool20250825`

    - `"code_execution_20250825" type`

    - `"code_execution" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaCodeExecutionTool20260120`

    - `"code_execution_20260120" type`

    - `"code_execution" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaCodeExecutionTool20260521`

    - `"code_execution_20260521" type`

    - `"code_execution" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaBrowserToolset20260801`

    - `"browser_toolset_20260801" type`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?BetaBrowserToolsetConfigs configs`

      Sparse per-member overrides, keyed by member name. Absent, null, and {} are equivalent; a member's defaults apply wherever its key is absent.

  - `class BetaToolComputerUse20241022`

    - `"computer_20241022" type`

    - `int displayHeightPx`

      The height of the display in pixels.

    - `int displayWidthPx`

      The width of the display in pixels.

    - `"computer" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int displayNumber`

      The X11 display number (e.g. 0, 1) for the display.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaMemoryTool20250818`

    - `"memory_20250818" type`

    - `"memory" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaToolComputerUse20250124`

    - `"computer_20250124" type`

    - `int displayHeightPx`

      The height of the display in pixels.

    - `int displayWidthPx`

      The width of the display in pixels.

    - `"computer" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int displayNumber`

      The X11 display number (e.g. 0, 1) for the display.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaToolTextEditor20241022`

    - `"text_editor_20241022" type`

    - `"str_replace_editor" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaToolComputerUse20251124`

    - `"computer_20251124" type`

    - `int displayHeightPx`

      The height of the display in pixels.

    - `int displayWidthPx`

      The width of the display in pixels.

    - `"computer" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int displayNumber`

      The X11 display number (e.g. 0, 1) for the display.

    - `?bool enableZoom`

      Whether to enable an action to take a zoomed-in screenshot of the screen.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaComputerToolset20260801`

    - `"computer_toolset_20260801" type`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?BetaComputerToolsetConfigs configs`

      Sparse per-member overrides, keyed by member name. Absent, null, and {} are equivalent; a member's defaults apply wherever its key is absent.

  - `class BetaToolTextEditor20250124`

    - `"text_editor_20250124" type`

    - `"str_replace_editor" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaToolTextEditor20250429`

    - `"text_editor_20250429" type`

    - `"str_replace_based_edit_tool" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaToolTextEditor20250728`

    - `"text_editor_20250728" type`

    - `"str_replace_based_edit_tool" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?int maxCharacters`

      Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaWebSearchTool20250305`

    - `"web_search_20250305" type`

    - `"web_search" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `?list<string> blockedDomains`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

    - `?BetaUserLocation userLocation`

      Parameters for the user's location. Used to provide more relevant search results.

  - `class BetaWebFetchTool20250910`

    - `"web_fetch_20250910" type`

    - `"web_fetch" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      List of domains to allow fetching from

    - `?list<string> blockedDomains`

      List of domains to block fetching from

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?BetaCitationsConfigParam citations`

      Citations configuration for fetched documents. Citations are disabled by default.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxContentTokens`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

    - `?BetaWebFetchURLSources urlSources`

      Which sources contribute to the set of URLs the tool may fetch. Omitted means every source.

  - `class BetaWebSearchTool20260209`

    - `"web_search_20260209" type`

    - `"web_search" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `?list<string> blockedDomains`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

    - `?BetaUserLocation userLocation`

      Parameters for the user's location. Used to provide more relevant search results.

  - `class BetaWebFetchTool20260209`

    - `"web_fetch_20260209" type`

    - `"web_fetch" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      List of domains to allow fetching from

    - `?list<string> blockedDomains`

      List of domains to block fetching from

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?BetaCitationsConfigParam citations`

      Citations configuration for fetched documents. Citations are disabled by default.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxContentTokens`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

    - `?BetaWebFetchURLSources urlSources`

      Which sources contribute to the set of URLs the tool may fetch. Omitted means every source.

  - `class BetaWebFetchTool20260309`

    - `"web_fetch_20260309" type`

    - `"web_fetch" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      List of domains to allow fetching from

    - `?list<string> blockedDomains`

      List of domains to block fetching from

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?BetaCitationsConfigParam citations`

      Citations configuration for fetched documents. Citations are disabled by default.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxContentTokens`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

    - `?BetaWebFetchURLSources urlSources`

      Which sources contribute to the set of URLs the tool may fetch. Omitted means every source.

    - `?bool useCache`

      Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

  - `class BetaWebSearchTool20260318`

    - `"web_search_20260318" type`

    - `"web_search" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `?list<string> blockedDomains`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?ResponseInclusion responseInclusion`

      How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

    - `?BetaUserLocation userLocation`

      Parameters for the user's location. Used to provide more relevant search results.

  - `class BetaWebFetchTool20260318`

    - `"web_fetch_20260318" type`

    - `"web_fetch" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      List of domains to allow fetching from

    - `?list<string> blockedDomains`

      List of domains to block fetching from

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?BetaCitationsConfigParam citations`

      Citations configuration for fetched documents. Citations are disabled by default.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxContentTokens`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?ResponseInclusion responseInclusion`

      How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

    - `?BetaWebFetchURLSources urlSources`

      Which sources contribute to the set of URLs the tool may fetch. Omitted means every source.

    - `?bool useCache`

      Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

  - `class BetaAdvisorTool20260301`

    - `"advisor_20260301" type`

    - `Model model`

      The model that will complete your prompt.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `"advisor" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?BetaCacheControlEphemeral caching`

      Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxTokens`

      Bounds the advisor's total output (thinking + text) per call. When the advisor hits this cap, the returned advisor_result or advisor_redacted_result block carries stop_reason='max_tokens', and a truncation note is appended to the advice text the worker model sees (inside the encrypted blob in redacted mode). When set, the server also emits a remaining-tokens budget block in the advisor's prompt so the advisor self-shapes toward the cap. When omitted, the advisor model's default output cap applies and no budget block is emitted.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaToolSearchToolBm25_20251119`

    - `Type type`

    - `"tool_search_tool_bm25" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaToolSearchToolRegex20251119`

    - `Type type`

    - `"tool_search_tool_regex" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `class BetaMCPToolset`

    - `"mcp_toolset" type`

    - `string mcpServerName`

      Name of the MCP server to configure tools for

    - `?BetaCacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?array<string,BetaMCPToolConfig> configs`

      Configuration overrides for specific tools, keyed by tool name

    - `?BetaMCPToolDefaultConfig defaultConfig`

      Default configuration applied to all tools from this server

    - `?list<BetaMCPToolParam> tools`

      The server's tool listing, pinned: when present, the server is not asked for its tools before sampling and exactly these entries, with `default_config` and `configs` applied, are the toolset's tools. Copy it from the `mcp_tool_listing` block of an earlier response.

### Beta Tool Use Block

- `class BetaToolUseBlock`

  - `"tool_use" type`

  - `string id`

  - `array<string,mixed> input`

  - `string name`

  - `?Caller caller`

  - `?string toolsetName`

    For a toolset member tool_use, the toolset family.

### Beta Tool Use Block Param

- `class BetaToolUseBlockParam`

  - `"tool_use" type`

  - `string id`

  - `array<string,mixed> input`

  - `string name`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?Caller caller`

  - `?string toolsetName`

    For a toolset member tool_use, the toolset family this member belongs to.

### Beta Tool Uses Keep

- `class BetaToolUsesKeep`

  - `"tool_uses" type`

  - `int value`

### Beta Tool Uses Trigger

- `class BetaToolUsesTrigger`

  - `"tool_uses" type`

  - `int value`

### Beta URL Image Source

- `class BetaURLImageSource`

  - `"url" type`

  - `string url`

### Beta URL PDF Source

- `class BetaURLPDFSource`

  - `"url" type`

  - `string url`

### Beta Usage

- `class BetaUsage`

  - `?BetaCacheCreation cacheCreation`

    Breakdown of cached tokens by TTL

  - `?int cacheCreationInputTokens`

    The number of input tokens used to create the cache entry.

  - `?int cacheReadInputTokens`

    The number of input tokens read from the cache.

  - `?BetaFallbackCreditUsage fallbackCredit`

    Outcome of the `fallback_credit_token` presented on this request.

    Present on every response to a non-batch request that carried a
    `fallback_credit_token`, in either redemption mode; absent otherwise (batch
    items accept and ignore the token and carry no outcome object).

  - `?string inferenceGeo`

    The geographic region where inference was performed for this request.

  - `int inputTokens`

    The number of input tokens which were used.

  - `?list<BetaIterationsUsageItem> iterations`

    Per-iteration token usage breakdown.

    Each entry represents one sampling iteration, with its own input/output token counts and cache statistics, discriminated by `type`. For `message` entries (model sampling iterations, such as the turns of a server-side tool use loop), this allows you to:

    - Determine which iterations exceeded long context thresholds (>=200k tokens)
    - Calculate the context window size from the last `message` entry
    - Understand token accumulation across server-side tool use loops

    A `compaction` entry reports the token usage of the compaction operation itself — the server-side request that summarizes the context being closed — NOT the size of the context that was compacted away, and its token counts can be much smaller than that closed context (for example, a compaction that closes a ~200k-token context can report only a few thousand tokens). Do not derive the context window size from a `compaction` entry, even when it is the last entry. A `compaction` entry's tokens are not included in the top-level `usage` fields. When an input-token trigger is in effect (the default — 150,000 tokens unless configured otherwise), each `compaction` entry closes a context that had reached at least that threshold, though the context can exceed it by the final iteration's output and tool results.

  - `int outputTokens`

    The number of output tokens which were used.

  - `?BetaOutputTokensDetails outputTokensDetails`

    Breakdown of output tokens by category.

    `output_tokens` remains the inclusive, authoritative total used for billing.
    This object provides a read-only decomposition for observability — for example,
    how many of the billed output tokens were spent on internal reasoning that may
    have been summarized before being returned to you.

  - `?BetaServerToolUsage serverToolUse`

    The number of server tool requests.

  - `?ServiceTier serviceTier`

    If the request used the priority, standard, or batch tier.

  - `?Speed speed`

    The inference speed mode used for this request.

### Beta User Location

- `class BetaUserLocation`

  - `"approximate" type`

  - `?string city`

    The city of the user.

  - `?string country`

    The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

  - `?string region`

    The region of the user.

  - `?string timezone`

    The [IANA timezone](https://nodatime.org/TimeZones) of the user.

### Beta Web Fetch Block

- `class BetaWebFetchBlock`

  - `"web_fetch_result" type`

  - `BetaDocumentBlock content`

  - `?string retrievedAt`

    ISO 8601 timestamp when the content was retrieved

  - `string url`

    Fetched content URL

### Beta Web Fetch Block Param

- `class BetaWebFetchBlockParam`

  - `"web_fetch_result" type`

  - `BetaRequestDocumentBlock content`

  - `string url`

    Fetched content URL

  - `?string retrievedAt`

    ISO 8601 timestamp when the content was retrieved

### Beta Web Fetch Tool 20250910

- `class BetaWebFetchTool20250910`

  - `"web_fetch_20250910" type`

  - `"web_fetch" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?list<string> allowedDomains`

    List of domains to allow fetching from

  - `?list<string> blockedDomains`

    List of domains to block fetching from

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?BetaCitationsConfigParam citations`

    Citations configuration for fetched documents. Citations are disabled by default.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?int maxContentTokens`

    Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

  - `?int maxUses`

    Maximum number of times the tool can be used in the API request.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

  - `?BetaWebFetchURLSources urlSources`

    Which sources contribute to the set of URLs the tool may fetch. Omitted means every source.

### Beta Web Fetch Tool 20260209

- `class BetaWebFetchTool20260209`

  - `"web_fetch_20260209" type`

  - `"web_fetch" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?list<string> allowedDomains`

    List of domains to allow fetching from

  - `?list<string> blockedDomains`

    List of domains to block fetching from

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?BetaCitationsConfigParam citations`

    Citations configuration for fetched documents. Citations are disabled by default.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?int maxContentTokens`

    Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

  - `?int maxUses`

    Maximum number of times the tool can be used in the API request.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

  - `?BetaWebFetchURLSources urlSources`

    Which sources contribute to the set of URLs the tool may fetch. Omitted means every source.

### Beta Web Fetch Tool 20260309

- `class BetaWebFetchTool20260309`

  - `"web_fetch_20260309" type`

  - `"web_fetch" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?list<string> allowedDomains`

    List of domains to allow fetching from

  - `?list<string> blockedDomains`

    List of domains to block fetching from

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?BetaCitationsConfigParam citations`

    Citations configuration for fetched documents. Citations are disabled by default.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?int maxContentTokens`

    Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

  - `?int maxUses`

    Maximum number of times the tool can be used in the API request.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

  - `?BetaWebFetchURLSources urlSources`

    Which sources contribute to the set of URLs the tool may fetch. Omitted means every source.

  - `?bool useCache`

    Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

### Beta Web Fetch Tool 20260318

- `class BetaWebFetchTool20260318`

  - `"web_fetch_20260318" type`

  - `"web_fetch" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?list<string> allowedDomains`

    List of domains to allow fetching from

  - `?list<string> blockedDomains`

    List of domains to block fetching from

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?BetaCitationsConfigParam citations`

    Citations configuration for fetched documents. Citations are disabled by default.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?int maxContentTokens`

    Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

  - `?int maxUses`

    Maximum number of times the tool can be used in the API request.

  - `?ResponseInclusion responseInclusion`

    How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

  - `?BetaWebFetchURLSources urlSources`

    Which sources contribute to the set of URLs the tool may fetch. Omitted means every source.

  - `?bool useCache`

    Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

### Beta Web Fetch Tool Result Block

- `class BetaWebFetchToolResultBlock`

  - `"web_fetch_tool_result" type`

  - `Content content`

  - `string toolUseID`

  - `?Caller caller`

### Beta Web Fetch Tool Result Block Param

- `class BetaWebFetchToolResultBlockParam`

  - `"web_fetch_tool_result" type`

  - `Content content`

  - `string toolUseID`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?Caller caller`

### Beta Web Fetch Tool Result Error Block

- `class BetaWebFetchToolResultErrorBlock`

  - `"web_fetch_tool_result_error" type`

  - `BetaWebFetchToolResultErrorCode errorCode`

### Beta Web Fetch Tool Result Error Block Param

- `class BetaWebFetchToolResultErrorBlockParam`

  - `"web_fetch_tool_result_error" type`

  - `BetaWebFetchToolResultErrorCode errorCode`

### Beta Web Fetch Tool Result Error Code

- `enum BetaWebFetchToolResultErrorCode`

  - `"invalid_tool_input"`

  - `"url_too_long"`

  - `"url_not_allowed"`

  - `"url_not_in_prior_context"`

  - `"url_not_accessible"`

  - `"unsupported_content_type"`

  - `"too_many_requests"`

  - `"max_uses_exceeded"`

  - `"unavailable"`

  - `"content_too_large"`

### Beta Web Fetch URL Source All

- `class BetaWebFetchURLSourceAll`

  - `"all" type`

### Beta Web Fetch URL Source Except

- `class BetaWebFetchURLSourceExcept`

  - `"except" type`

  - `list<BetaWebFetchURLSourceToolReference> tools`

### Beta Web Fetch URL Source None

- `class BetaWebFetchURLSourceNone`

  - `"none" type`

### Beta Web Fetch URL Source Only

- `class BetaWebFetchURLSourceOnly`

  - `"only" type`

  - `list<BetaWebFetchURLSourceToolReference> tools`

### Beta Web Fetch URL Source Tool Reference

- `class BetaWebFetchURLSourceToolReference`

  - `"tool_reference" type`

  - `string name`

### Beta Web Fetch URL Sources

- `class BetaWebFetchURLSources`

  - `?ClientToolResults clientToolResults`

    Which client tools' results contribute fetchable URLs: "all", "none", or an only or except list of client tool names from tools[].

  - `?ServerToolResults serverToolResults`

    Which server tools' results contribute fetchable URLs: "all", "none", or an only or except list of server tool names from tools[]; only web_search and web_fetch results ever contribute.

  - `?UserInput userInput`

    Whether URLs in user messages are fetchable: "all" or "none".

### Beta Web Search Result Block

- `class BetaWebSearchResultBlock`

  - `"web_search_result" type`

  - `string encryptedContent`

  - `?string pageAge`

  - `string title`

  - `string url`

### Beta Web Search Result Block Param

- `class BetaWebSearchResultBlockParam`

  - `"web_search_result" type`

  - `string encryptedContent`

  - `string title`

  - `string url`

  - `?string pageAge`

### Beta Web Search Tool 20250305

- `class BetaWebSearchTool20250305`

  - `"web_search_20250305" type`

  - `"web_search" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?list<string> allowedDomains`

    If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

  - `?list<string> blockedDomains`

    If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?int maxUses`

    Maximum number of times the tool can be used in the API request.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

  - `?BetaUserLocation userLocation`

    Parameters for the user's location. Used to provide more relevant search results.

### Beta Web Search Tool 20260209

- `class BetaWebSearchTool20260209`

  - `"web_search_20260209" type`

  - `"web_search" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?list<string> allowedDomains`

    If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

  - `?list<string> blockedDomains`

    If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?int maxUses`

    Maximum number of times the tool can be used in the API request.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

  - `?BetaUserLocation userLocation`

    Parameters for the user's location. Used to provide more relevant search results.

### Beta Web Search Tool 20260318

- `class BetaWebSearchTool20260318`

  - `"web_search_20260318" type`

  - `"web_search" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?list<string> allowedDomains`

    If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

  - `?list<string> blockedDomains`

    If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?int maxUses`

    Maximum number of times the tool can be used in the API request.

  - `?ResponseInclusion responseInclusion`

    How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

  - `?BetaUserLocation userLocation`

    Parameters for the user's location. Used to provide more relevant search results.

### Beta Web Search Tool Request Error

- `class BetaWebSearchToolRequestError`

  - `"web_search_tool_result_error" type`

  - `BetaWebSearchToolResultErrorCode errorCode`

### Beta Web Search Tool Result Block

- `class BetaWebSearchToolResultBlock`

  - `"web_search_tool_result" type`

  - `BetaWebSearchToolResultBlockContent content`

  - `string toolUseID`

  - `?Caller caller`

### Beta Web Search Tool Result Block Content

- `class BetaWebSearchToolResultBlockContent`

  - `class BetaWebSearchToolResultError`

    - `"web_search_tool_result_error" type`

    - `BetaWebSearchToolResultErrorCode errorCode`

  - `class list<BetaWebSearchResultBlock>`

    - `"web_search_result" type`

    - `string encryptedContent`

    - `?string pageAge`

    - `string title`

    - `string url`

### Beta Web Search Tool Result Block Param

- `class BetaWebSearchToolResultBlockParam`

  - `"web_search_tool_result" type`

  - `BetaWebSearchToolResultBlockParamContent content`

  - `string toolUseID`

  - `?BetaCacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?Caller caller`

### Beta Web Search Tool Result Block Param Content

- `class BetaWebSearchToolResultBlockParamContent`

  - `class list<BetaWebSearchResultBlockParam>`

    - `"web_search_result" type`

    - `string encryptedContent`

    - `string title`

    - `string url`

    - `?string pageAge`

  - `class BetaWebSearchToolRequestError`

    - `"web_search_tool_result_error" type`

    - `BetaWebSearchToolResultErrorCode errorCode`

### Beta Web Search Tool Result Error

- `class BetaWebSearchToolResultError`

  - `"web_search_tool_result_error" type`

  - `BetaWebSearchToolResultErrorCode errorCode`

### Beta Web Search Tool Result Error Code

- `enum BetaWebSearchToolResultErrorCode`

  - `"invalid_tool_input"`

  - `"unavailable"`

  - `"max_uses_exceeded"`

  - `"too_many_requests"`

  - `"query_too_long"`

  - `"request_too_large"`

## Messages › Batches

### Create a Message Batch

`$client->beta->messages->batches->create(list<Request> requests, ?list<AnthropicBeta> betas, ?string userProfileID, ?string workspaceID): MessageBatch`

**POST** `/v1/messages/batches`

Send a batch of Message creation requests.

The Message Batches API can be used to process multiple Messages API requests at once. Once a Message Batch is created, it begins processing immediately. Batches can take up to 24 hours to complete.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

#### Parameters

- `requests: list<Request>`

  List of requests for prompt completion. Each is an individual request to create a Message.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `userProfileID?:optional string`

  The user profile ID to attribute the requests in this batch to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header. Applies to every request in the batch; an individual request whose `user_profile_id` body field conflicts with this header is errored.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class MessageBatch`

  - `"message_batch" type`

    Object type.

    For Message Batches, this is always `"message_batch"`.

  - `string id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `?\Datetime archivedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

  - `?\Datetime cancelInitiatedAt`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

  - `\Datetime createdAt`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

  - `?\Datetime endedAt`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

  - `\Datetime expiresAt`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

  - `ProcessingStatus processingStatus`

    Processing status of the Message Batch.

  - `MessageBatchRequestCounts requestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

  - `?string resultsURL`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

#### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaMessageBatch = $client->beta->messages->batches->create(
  requests: [
    [
      'customID' => 'my-custom-id-1',
      'params' => [
        'maxTokens' => 1024,
        'messages' => [
          [
            'content' => 'Hello, world',
            'role' => 'user',
            'clearAt' => 'next_user_message',
            'outputConfig' => ['effort' => 'low'],
          ],
        ],
        'model' => Model::CLAUDE_OPUS_5,
        'cacheControl' => ['type' => 'ephemeral', 'ttl' => '5m'],
        'compaction' => [
          'type' => 'summarize', 'instructions' => 'instructions'
        ],
        'container' => [
          'id' => 'id',
          'skills' => [
            ['skillID' => 'pdf', 'type' => 'anthropic', 'version' => 'latest']
          ],
        ],
        'contextManagement' => [
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
        'diagnostics' => ['previousMessageID' => 'previous_message_id'],
        'fallbackCreditToken' => 'x',
        'fallbacks' => 'default',
        'inferenceGeo' => 'inference_geo',
        'mcpServers' => [
          [
            'name' => 'name',
            'type' => 'url',
            'url' => 'url',
            'authorizationToken' => 'authorization_token',
            'toolConfiguration' => [
              'allowedTools' => ['string'], 'enabled' => true
            ],
          ],
        ],
        'metadata' => ['userID' => '13803d75-b4b5-4c3e-b2a2-6f21399b021b'],
        'outputConfig' => [
          'effort' => 'low',
          'format' => ['schema' => ['foo' => 'bar'], 'type' => 'json_schema'],
          'taskBudget' => [
            'total' => 1024, 'type' => 'tokens', 'remaining' => 0
          ],
        ],
        'outputFormat' => [
          'schema' => ['foo' => 'bar'], 'type' => 'json_schema'
        ],
        'serviceTier' => 'auto',
        'speed' => 'standard',
        'stopSequences' => ['string'],
        'stream' => false,
        'system' => [
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
        'temperature' => 1,
        'thinking' => [
          'type' => 'adaptive',
          'blockBinding' => [
            'prefixMismatchBehavior' => BetaThinkingPrefixMismatchBehavior::ERROR,
          ],
          'display' => 'summarized',
        ],
        'toolChoice' => ['type' => 'auto', 'disableParallelToolUse' => true],
        'tools' => [
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
        'topK' => 5,
        'topP' => 0.7,
      ],
    ],
  ],
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  userProfileID: 'anthropic-user-profile-id',
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaMessageBatch);
```

##### Response (200)

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

### Retrieve a Message Batch

`$client->beta->messages->batches->retrieve(string messageBatchID, ?list<AnthropicBeta> betas, ?string workspaceID): MessageBatch`

**GET** `/v1/messages/batches/{message_batch_id}`

This endpoint is idempotent and can be used to poll for Message Batch completion. To access the results of a Message Batch, make a request to the `results_url` field in the response.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

#### Parameters

- `messageBatchID: string`

  ID of the Message Batch.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class MessageBatch`

  - `"message_batch" type`

    Object type.

    For Message Batches, this is always `"message_batch"`.

  - `string id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `?\Datetime archivedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

  - `?\Datetime cancelInitiatedAt`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

  - `\Datetime createdAt`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

  - `?\Datetime endedAt`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

  - `\Datetime expiresAt`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

  - `ProcessingStatus processingStatus`

    Processing status of the Message Batch.

  - `MessageBatchRequestCounts requestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

  - `?string resultsURL`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

#### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaMessageBatch = $client->beta->messages->batches->retrieve(
  'message_batch_id',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaMessageBatch);
```

##### Response (200)

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

### List Message Batches

`$client->beta->messages->batches->list(?string afterID, ?string beforeID, ?int limit, ?list<AnthropicBeta> betas, ?string workspaceID): Page<MessageBatch>`

**GET** `/v1/messages/batches`

List all Message Batches within a Workspace. Most recently created batches are returned first.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

#### Parameters

- `afterID?:optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `beforeID?:optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `limit?:optional int`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  default: 20

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class MessageBatch`

  - `"message_batch" type`

    Object type.

    For Message Batches, this is always `"message_batch"`.

  - `string id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `?\Datetime archivedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

  - `?\Datetime cancelInitiatedAt`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

  - `\Datetime createdAt`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

  - `?\Datetime endedAt`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

  - `\Datetime expiresAt`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

  - `ProcessingStatus processingStatus`

    Processing status of the Message Batch.

  - `MessageBatchRequestCounts requestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

  - `?string resultsURL`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

#### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->messages->batches->list(
  afterID: 'after_id',
  beforeID: 'before_id',
  limit: 1,
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($page);
```

##### Response (200)

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

### Cancel a Message Batch

`$client->beta->messages->batches->cancel(string messageBatchID, ?list<AnthropicBeta> betas, ?string workspaceID): MessageBatch`

**POST** `/v1/messages/batches/{message_batch_id}/cancel`

Batches may be canceled any time before processing ends. Once cancellation is initiated, the batch enters a `canceling` state, at which time the system may complete any in-progress, non-interruptible requests before finalizing cancellation.

The number of canceled requests is specified in `request_counts`. To determine which requests were canceled, check the individual results within the batch. Note that cancellation may not result in any canceled requests if they were non-interruptible.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

#### Parameters

- `messageBatchID: string`

  ID of the Message Batch.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class MessageBatch`

  - `"message_batch" type`

    Object type.

    For Message Batches, this is always `"message_batch"`.

  - `string id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `?\Datetime archivedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

  - `?\Datetime cancelInitiatedAt`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

  - `\Datetime createdAt`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

  - `?\Datetime endedAt`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

  - `\Datetime expiresAt`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

  - `ProcessingStatus processingStatus`

    Processing status of the Message Batch.

  - `MessageBatchRequestCounts requestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

  - `?string resultsURL`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

#### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaMessageBatch = $client->beta->messages->batches->cancel(
  'message_batch_id',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaMessageBatch);
```

##### Response (200)

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

### Delete a Message Batch

`$client->beta->messages->batches->delete(string messageBatchID, ?list<AnthropicBeta> betas, ?string workspaceID): DeletedMessageBatch`

**DELETE** `/v1/messages/batches/{message_batch_id}`

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

#### Parameters

- `messageBatchID: string`

  ID of the Message Batch.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class DeletedMessageBatch`

  - `"message_batch_deleted" type`

    Deleted object type.

    For Message Batches, this is always `"message_batch_deleted"`.

  - `string id`

    ID of the Message Batch.

#### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaDeletedMessageBatch = $client->beta->messages->batches->delete(
  'message_batch_id',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaDeletedMessageBatch);
```

##### Response (200)

```json
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "type": "message_batch_deleted"
}
```

### Retrieve Message Batch results

`$client->beta->messages->batches->results(string messageBatchID, ?list<AnthropicBeta> betas, ?string workspaceID): MessageBatchIndividualResponse`

**GET** `/v1/messages/batches/{message_batch_id}/results`

Streams the results of a Message Batch as a `.jsonl` file.

Each line in the file is a JSON object containing the result of a single request in the Message Batch. Results are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

#### Parameters

- `messageBatchID: string`

  ID of the Message Batch.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class MessageBatchIndividualResponse`

  - `string customID`

    Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

    Must be unique for each request within the Message Batch.

  - `MessageBatchResult result`

    Processing result for this request.

    Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

#### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaMessageBatchIndividualResponse = $client
  ->beta
  ->messages
  ->batches
  ->resultsStream(
  'message_batch_id',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaMessageBatchIndividualResponse);
```
