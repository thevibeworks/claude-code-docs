---
title: Messages
url: https://platform.claude.com/docs/en/api/php/messages
---

# Messages

## Create a Message

`$client->messages->create(int maxTokens, list<MessageParam> messages, Model model, ?CacheControlEphemeral cacheControl, ?MessageCreateParamsContainer container, ?string inferenceGeo, ?Metadata metadata, ?OutputConfig outputConfig, ?ServiceTier serviceTier, ?list<string> stopSequences, ?System system, ?float temperature, ?ThinkingConfigParam thinking, ?ToolChoice toolChoice, ?list<ToolUnion> tools, ?int topK, ?float topP, ?string userProfileID, ?string workspaceID): Message`

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

- `messages: list<MessageParam>`

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

- `cacheControl?:optional CacheControlEphemeral`

  Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

- `container?:optional MessageCreateParamsContainer`

  Container identifier for reuse across requests.

- `inferenceGeo?:optional string`

  Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

- `metadata?:optional Metadata`

  An object describing metadata about the request.

- `outputConfig?:optional OutputConfig`

  Configuration options for the model's output, such as the output format.

- `serviceTier?:optional ServiceTier`

  Determines whether to use priority capacity (if available) or standard capacity for this request.

  Anthropic offers different levels of service for your API requests. See [service-tiers](https://platform.claude.com/docs/en/api/service-tiers) for details.

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

- `thinking?:optional ThinkingConfigParam`

  Configuration for enabling Claude's extended thinking.

  When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

  See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

- `toolChoice?:optional ToolChoice`

  How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

- `tools?:optional list<ToolUnion>`

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

- `userProfileID?:optional string`

  The user profile ID to attribute this request to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header.

- `workspaceID?:optional string`

- `temperature?:optional float`

  **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not support setting temperature. A value of 1.0 of will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

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

- `Message`

  - `"message" type`

    Object type.

    For Messages, this is always `"message"`.

  - `string id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `?Container container`

    Information about the container used in the request (for the code execution tool)

  - `list<ContentBlock> content`

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

  - `Model model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `"assistant" role`

    Conversational role of the generated message.

    This will always be `"assistant"`.

  - `?RefusalStopDetails stopDetails`

    Structured information about a refusal.

  - `?StopReason stopReason`

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

  - `Usage usage`

    Billing and rate-limit usage.

    Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

    Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

    For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

    Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

- `RawMessageStreamEvent`

  - `RawMessageStartEvent`

    - `"message_start" type`

    - `Message message`

  - `RawMessageDeltaEvent`

    - `"message_delta" type`

    - `Delta delta`

    - `MessageDeltaUsage usage`

      Billing and rate-limit usage.

      Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

      Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

      For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

      Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

  - `RawMessageStopEvent`

    - `"message_stop" type`

  - `RawContentBlockStartEvent`

    - `"content_block_start" type`

    - `ContentBlock contentBlock`

    - `int index`

  - `RawContentBlockDeltaEvent`

    - `"content_block_delta" type`

    - `RawContentBlockDelta delta`

    - `int index`

  - `RawContentBlockStopEvent`

    - `"content_block_stop" type`

    - `int index`

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$message = $client->messages->create(
  maxTokens: 1024,
  messages: [['content' => 'Hello, world', 'role' => 'user']],
  model: Model::CLAUDE_OPUS_5,
  cacheControl: ['type' => 'ephemeral', 'ttl' => '5m'],
  container: [
    'id' => 'id',
    'skills' => [
      ['skillID' => 'pdf', 'type' => 'anthropic', 'version' => 'latest']
    ],
  ],
  inferenceGeo: 'inference_geo',
  metadata: ['userID' => '13803d75-b4b5-4c3e-b2a2-6f21399b021b'],
  outputConfig: [
    'effort' => 'low',
    'format' => ['schema' => ['foo' => 'bar'], 'type' => 'json_schema'],
  ],
  serviceTier: 'auto',
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
  thinking: ['type' => 'adaptive', 'display' => 'summarized'],
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
  userProfileID: 'anthropic-user-profile-id',
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($message);
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
  "model": "claude-opus-5",
  "role": "assistant",
  "stop_details": {
    "category": "cyber",
    "explanation": "This request was declined because it conflicts with Anthropic's Usage Policy.",
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
    "service_tier": "standard"
  }
}
```

## Count tokens in a Message

`$client->messages->countTokens(list<MessageParam> messages, Model model, ?CacheControlEphemeral cacheControl, ?OutputConfig outputConfig, ?System system, ?ThinkingConfigParam thinking, ?ToolChoice toolChoice, ?list<MessageCountTokensTool> tools, ?string userProfileID, ?string workspaceID): MessageTokensCount`

**POST** `/v1/messages/count_tokens`

Count the number of tokens in a Message.

The Token Count API can be used to count the number of tokens in a Message, including tools, images, and documents, without creating it.

Learn more about token counting in our [user guide](https://platform.claude.com/docs/en/build-with-claude/token-counting)

### Parameters

- `messages: list<MessageParam>`

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

- `cacheControl?:optional CacheControlEphemeral`

  Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

- `outputConfig?:optional OutputConfig`

  Configuration options for the model's output, such as the output format.

- `system?:optional System`

  System prompt.

  A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role).

- `thinking?:optional ThinkingConfigParam`

  Configuration for enabling Claude's extended thinking.

  When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

  See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

- `toolChoice?:optional ToolChoice`

  How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

- `tools?:optional list<MessageCountTokensTool>`

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

- `userProfileID?:optional string`

  The user profile ID to attribute this request to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header.

- `workspaceID?:optional string`

### Returns

- `MessageTokensCount`

  - `int inputTokens`

    The total number of tokens across the provided list of messages, system prompt, and tools.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$messageTokensCount = $client->messages->countTokens(
  messages: [['content' => 'Hello, world', 'role' => 'user']],
  model: Model::CLAUDE_OPUS_5,
  cacheControl: ['type' => 'ephemeral', 'ttl' => '5m'],
  outputConfig: [
    'effort' => 'low',
    'format' => ['schema' => ['foo' => 'bar'], 'type' => 'json_schema'],
  ],
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
  thinking: ['type' => 'adaptive', 'display' => 'summarized'],
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
  userProfileID: 'anthropic-user-profile-id',
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($messageTokensCount);
```

#### Response (200)

```json
{
  "input_tokens": 2095
}
```

## Domain types

### Base64 Image Source

- `Base64ImageSource`

  - `"base64" type`

  - `string data`

  - `MediaType mediaType`

### Base64 PDF Source

- `Base64PDFSource`

  - `"base64" type`

  - `string data`

  - `"application/pdf" mediaType`

### Bash Code Execution Output Block

- `BashCodeExecutionOutputBlock`

  - `"bash_code_execution_output" type`

  - `string fileID`

### Bash Code Execution Output Block Param

- `BashCodeExecutionOutputBlockParam`

  - `"bash_code_execution_output" type`

  - `string fileID`

### Bash Code Execution Result Block

- `BashCodeExecutionResultBlock`

  - `"bash_code_execution_result" type`

  - `list<BashCodeExecutionOutputBlock> content`

  - `int returnCode`

  - `string stderr`

  - `string stdout`

### Bash Code Execution Result Block Param

- `BashCodeExecutionResultBlockParam`

  - `"bash_code_execution_result" type`

  - `list<BashCodeExecutionOutputBlockParam> content`

  - `int returnCode`

  - `string stderr`

  - `string stdout`

### Bash Code Execution Tool Result Block

- `BashCodeExecutionToolResultBlock`

  - `"bash_code_execution_tool_result" type`

  - `Content content`

  - `string toolUseID`

### Bash Code Execution Tool Result Block Param

- `BashCodeExecutionToolResultBlockParam`

  - `"bash_code_execution_tool_result" type`

  - `Content content`

  - `string toolUseID`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

### Bash Code Execution Tool Result Error

- `BashCodeExecutionToolResultError`

  - `"bash_code_execution_tool_result_error" type`

  - `BashCodeExecutionToolResultErrorCode errorCode`

### Bash Code Execution Tool Result Error Code

- `BashCodeExecutionToolResultErrorCode`

  - `"invalid_tool_input"`

  - `"unavailable"`

  - `"too_many_requests"`

  - `"execution_time_exceeded"`

  - `"output_file_too_large"`

### Bash Code Execution Tool Result Error Param

- `BashCodeExecutionToolResultErrorParam`

  - `"bash_code_execution_tool_result_error" type`

  - `BashCodeExecutionToolResultErrorCode errorCode`

### Browser Close Tab Config

- `BrowserCloseTabConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Double Click Config

- `BrowserDoubleClickConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser File Upload Config

- `BrowserFileUploadConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Find Config

- `BrowserFindConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Form Input Config

- `BrowserFormInputConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Get Page Text Config

- `BrowserGetPageTextConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Hold Key Config

- `BrowserHoldKeyConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Hover Config

- `BrowserHoverConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Javascript Exec Config

- `BrowserJavascriptExecConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Key Config

- `BrowserKeyConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Left Click Config

- `BrowserLeftClickConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Left Click Drag Config

- `BrowserLeftClickDragConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Left Mouse Down Config

- `BrowserLeftMouseDownConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Left Mouse Up Config

- `BrowserLeftMouseUpConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser List Tabs Config

- `BrowserListTabsConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Middle Click Config

- `BrowserMiddleClickConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Mouse Move Config

- `BrowserMouseMoveConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Navigate Config

- `BrowserNavigateConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser New Tab Config

- `BrowserNewTabConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Read Console Config

- `BrowserReadConsoleConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Read Network Config

- `BrowserReadNetworkConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Read Page Config

- `BrowserReadPageConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Right Click Config

- `BrowserRightClickConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Screenshot Config

- `BrowserScreenshotConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Scroll Config

- `BrowserScrollConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Scroll To Config

- `BrowserScrollToConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser State Block Param

- `BrowserStateBlockParam`

  - `"browser_state" type`

  - `list<BrowserStateTabEntry> tabs`

    All tabs open in the browser after this call — the full inventory, not a delta. May be empty. Whenever non-empty, exactly one entry carries `active: true`.

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?list<BrowserStateChange> stateChanges`

    Tabs opened and download state changes during this call. "Nothing to report" is expressed by omitting the field, never by an empty list.

### Browser State Change

- `BrowserStateChange`

  - `BrowserStateChangeTabOpened`

    - `"tab_opened" type`

    - `string tabID`

      The `tab_id` of the opened tab, present in `tabs`.

  - `BrowserStateChangeDownloadStarted`

    - `"download_started" type`

    - `string downloadID`

      The caller-assigned identifier for this download, stable across the state changes reporting it.

    - `string url`

      The final post-redirect URL the download was served from.

  - `BrowserStateChangeDownloadCompleted`

    - `"download_completed" type`

    - `string downloadID`

      The caller-assigned identifier for this download, stable across the state changes reporting it.

    - `string url`

      The final post-redirect URL the download was served from.

    - `?string path`

      Where the executor saved the file, on the executor's filesystem. Only included when another tool in the same environment can read the file at that path.

    - `?int sizeBytes`

      The completed download's size.

  - `BrowserStateChangeDownloadFailed`

    - `"download_failed" type`

    - `string downloadID`

      The caller-assigned identifier for this download, stable across the state changes reporting it.

    - `string url`

      The final post-redirect URL the download was served from.

    - `?string error`

      The failure or cancellation detail, when known.

### Browser State Change Download Completed

- `BrowserStateChangeDownloadCompleted`

  - `"download_completed" type`

  - `string downloadID`

    The caller-assigned identifier for this download, stable across the state changes reporting it.

  - `string url`

    The final post-redirect URL the download was served from.

  - `?string path`

    Where the executor saved the file, on the executor's filesystem. Only included when another tool in the same environment can read the file at that path.

  - `?int sizeBytes`

    The completed download's size.

### Browser State Change Download Failed

- `BrowserStateChangeDownloadFailed`

  - `"download_failed" type`

  - `string downloadID`

    The caller-assigned identifier for this download, stable across the state changes reporting it.

  - `string url`

    The final post-redirect URL the download was served from.

  - `?string error`

    The failure or cancellation detail, when known.

### Browser State Change Download Started

- `BrowserStateChangeDownloadStarted`

  - `"download_started" type`

  - `string downloadID`

    The caller-assigned identifier for this download, stable across the state changes reporting it.

  - `string url`

    The final post-redirect URL the download was served from.

### Browser State Change Tab Opened

- `BrowserStateChangeTabOpened`

  - `"tab_opened" type`

  - `string tabID`

    The `tab_id` of the opened tab, present in `tabs`.

### Browser State Tab Entry

- `BrowserStateTabEntry`

  - `string tabID`

    The caller-assigned identifier for this tab, unique within the inventory.

  - `string title`

    The title of the page the tab is showing. May be empty.

  - `string url`

    The URL of the page the tab is showing. May be empty.

  - `?bool active`

    Whether this tab is the active tab after this call. Whenever `tabs` is non-empty, exactly one entry is marked `active: true`.

### Browser Switch Tab Config

- `BrowserSwitchTabConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Toolset 20260801

- `BrowserToolset20260801`

  - `"browser_toolset_20260801" type`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?BrowserToolsetConfigs configs`

    Per-member configuration for `browser_toolset_20260801`: one
    optional field per member tool, keyed by the member name — the same
    name the member's `tool_use` blocks carry. Every member is an
    accepted key, and a member's defaults apply wherever its key is
    absent. Unknown keys are rejected: the field set is this toolset
    version's complete member set.

### Browser Toolset Configs

- `BrowserToolsetConfigs`

  - `?BrowserTypeConfig type`

    `type`'s config overrides.

  - `?BrowserCloseTabConfig closeTab`

    `close_tab`'s config overrides.

  - `?BrowserDoubleClickConfig doubleClick`

    `double_click`'s config overrides.

  - `?BrowserFileUploadConfig fileUpload`

    `file_upload`'s config overrides.

  - `?BrowserFindConfig find`

    `find`'s config overrides.

  - `?BrowserFormInputConfig formInput`

    `form_input`'s config overrides.

  - `?BrowserGetPageTextConfig getPageText`

    `get_page_text`'s config overrides.

  - `?BrowserHoldKeyConfig holdKey`

    `hold_key`'s config overrides.

  - `?BrowserHoverConfig hover`

    `hover`'s config overrides.

  - `?BrowserJavascriptExecConfig javascriptExec`

    `javascript_exec`'s config overrides.

  - `?BrowserKeyConfig key`

    `key`'s config overrides.

  - `?BrowserLeftClickConfig leftClick`

    `left_click`'s config overrides.

  - `?BrowserLeftClickDragConfig leftClickDrag`

    `left_click_drag`'s config overrides.

  - `?BrowserLeftMouseDownConfig leftMouseDown`

    `left_mouse_down`'s config overrides.

  - `?BrowserLeftMouseUpConfig leftMouseUp`

    `left_mouse_up`'s config overrides.

  - `?BrowserListTabsConfig listTabs`

    `list_tabs`'s config overrides.

  - `?BrowserMiddleClickConfig middleClick`

    `middle_click`'s config overrides.

  - `?BrowserMouseMoveConfig mouseMove`

    `mouse_move`'s config overrides.

  - `?BrowserNavigateConfig navigate`

    `navigate`'s config overrides.

  - `?BrowserNewTabConfig newTab`

    `new_tab`'s config overrides.

  - `?BrowserReadConsoleConfig readConsole`

    `read_console`'s config overrides.

  - `?BrowserReadNetworkConfig readNetwork`

    `read_network`'s config overrides.

  - `?BrowserReadPageConfig readPage`

    `read_page`'s config overrides.

  - `?BrowserRightClickConfig rightClick`

    `right_click`'s config overrides.

  - `?BrowserScreenshotConfig screenshot`

    `screenshot`'s config overrides.

  - `?BrowserScrollConfig scroll`

    `scroll`'s config overrides.

  - `?BrowserScrollToConfig scrollTo`

    `scroll_to`'s config overrides.

  - `?BrowserSwitchTabConfig switchTab`

    `switch_tab`'s config overrides.

  - `?BrowserTripleClickConfig tripleClick`

    `triple_click`'s config overrides.

  - `?BrowserWaitConfig wait`

    `wait`'s config overrides.

  - `?BrowserZoomConfig zoom`

    `zoom`'s config overrides.

### Browser Triple Click Config

- `BrowserTripleClickConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Type Config

- `BrowserTypeConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Wait Config

- `BrowserWaitConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Zoom Config

- `BrowserZoomConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Cache Control Ephemeral

- `CacheControlEphemeral`

  - `"ephemeral" type`

  - `?TTL ttl`

    The time-to-live for the cache control breakpoint.

    This may be one the following values:

    - `5m`: 5 minutes
    - `1h`: 1 hour

    Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

### Cache Creation

- `CacheCreation`

  - `int ephemeral1hInputTokens`

    The number of input tokens used to create the 1 hour cache entry.

  - `int ephemeral5mInputTokens`

    The number of input tokens used to create the 5 minute cache entry.

### Citation Char Location

- `CitationCharLocation`

  - `"char_location" type`

  - `string citedText`

  - `int documentIndex`

  - `?string documentTitle`

  - `int endCharIndex`

  - `?string fileID`

  - `int startCharIndex`

### Citation Char Location Param

- `CitationCharLocationParam`

  - `"char_location" type`

  - `string citedText`

  - `int documentIndex`

  - `?string documentTitle`

  - `int endCharIndex`

  - `int startCharIndex`

### Citation Content Block Location

- `CitationContentBlockLocation`

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

### Citation Content Block Location Param

- `CitationContentBlockLocationParam`

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

### Citation Page Location

- `CitationPageLocation`

  - `"page_location" type`

  - `string citedText`

  - `int documentIndex`

  - `?string documentTitle`

  - `int endPageNumber`

  - `?string fileID`

  - `int startPageNumber`

### Citation Page Location Param

- `CitationPageLocationParam`

  - `"page_location" type`

  - `string citedText`

  - `int documentIndex`

  - `?string documentTitle`

  - `int endPageNumber`

  - `int startPageNumber`

### Citation Search Result Location Param

- `CitationSearchResultLocationParam`

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

### Citation Web Search Result Location Param

- `CitationWebSearchResultLocationParam`

  - `"web_search_result_location" type`

  - `string citedText`

  - `string encryptedIndex`

  - `?string title`

  - `string url`

### Citations Config

- `CitationsConfig`

  - `bool enabled`

### Citations Config Param

- `CitationsConfigParam`

  - `?bool enabled`

### Citations Delta

- `CitationsDelta`

  - `"citations_delta" type`

  - `Citation citation`

### Citations Search Result Location

- `CitationsSearchResultLocation`

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

### Citations Web Search Result Location

- `CitationsWebSearchResultLocation`

  - `"web_search_result_location" type`

  - `string citedText`

  - `string encryptedIndex`

  - `?string title`

  - `string url`

### Code Execution Output Block

- `CodeExecutionOutputBlock`

  - `"code_execution_output" type`

  - `string fileID`

### Code Execution Output Block Param

- `CodeExecutionOutputBlockParam`

  - `"code_execution_output" type`

  - `string fileID`

### Code Execution Result Block

- `CodeExecutionResultBlock`

  - `"code_execution_result" type`

  - `list<CodeExecutionOutputBlock> content`

  - `int returnCode`

  - `string stderr`

  - `string stdout`

### Code Execution Result Block Param

- `CodeExecutionResultBlockParam`

  - `"code_execution_result" type`

  - `list<CodeExecutionOutputBlockParam> content`

  - `int returnCode`

  - `string stderr`

  - `string stdout`

### Code Execution Tool 20250522

- `CodeExecutionTool20250522`

  - `"code_execution_20250522" type`

  - `"code_execution" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Code Execution Tool 20250825

- `CodeExecutionTool20250825`

  - `"code_execution_20250825" type`

  - `"code_execution" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Code Execution Tool 20260120

- `CodeExecutionTool20260120`

  - `"code_execution_20260120" type`

  - `"code_execution" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Code Execution Tool 20260521

- `CodeExecutionTool20260521`

  - `"code_execution_20260521" type`

  - `"code_execution" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Code Execution Tool Result Block

- `CodeExecutionToolResultBlock`

  - `"code_execution_tool_result" type`

  - `CodeExecutionToolResultBlockContent content`

  - `string toolUseID`

### Code Execution Tool Result Block Content

- `CodeExecutionToolResultBlockContent`

  - `CodeExecutionToolResultError`

    - `"code_execution_tool_result_error" type`

    - `CodeExecutionToolResultErrorCode errorCode`

  - `CodeExecutionResultBlock`

    - `"code_execution_result" type`

    - `list<CodeExecutionOutputBlock> content`

    - `int returnCode`

    - `string stderr`

    - `string stdout`

  - `EncryptedCodeExecutionResultBlock`

    - `"encrypted_code_execution_result" type`

    - `list<CodeExecutionOutputBlock> content`

    - `string encryptedStdout`

    - `int returnCode`

    - `string stderr`

### Code Execution Tool Result Block Param

- `CodeExecutionToolResultBlockParam`

  - `"code_execution_tool_result" type`

  - `CodeExecutionToolResultBlockParamContent content`

  - `string toolUseID`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

### Code Execution Tool Result Block Param Content

- `CodeExecutionToolResultBlockParamContent`

  - `CodeExecutionToolResultErrorParam`

    - `"code_execution_tool_result_error" type`

    - `CodeExecutionToolResultErrorCode errorCode`

  - `CodeExecutionResultBlockParam`

    - `"code_execution_result" type`

    - `list<CodeExecutionOutputBlockParam> content`

    - `int returnCode`

    - `string stderr`

    - `string stdout`

  - `EncryptedCodeExecutionResultBlockParam`

    - `"encrypted_code_execution_result" type`

    - `list<CodeExecutionOutputBlockParam> content`

    - `string encryptedStdout`

    - `int returnCode`

    - `string stderr`

### Code Execution Tool Result Error

- `CodeExecutionToolResultError`

  - `"code_execution_tool_result_error" type`

  - `CodeExecutionToolResultErrorCode errorCode`

### Code Execution Tool Result Error Code

- `CodeExecutionToolResultErrorCode`

  - `"invalid_tool_input"`

  - `"unavailable"`

  - `"too_many_requests"`

  - `"execution_time_exceeded"`

### Code Execution Tool Result Error Param

- `CodeExecutionToolResultErrorParam`

  - `"code_execution_tool_result_error" type`

  - `CodeExecutionToolResultErrorCode errorCode`

### Computer Cursor Position Config

- `ComputerCursorPositionConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Double Click Config

- `ComputerDoubleClickConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Hold Key Config

- `ComputerHoldKeyConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Key Config

- `ComputerKeyConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Left Click Config

- `ComputerLeftClickConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Left Click Drag Config

- `ComputerLeftClickDragConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Left Mouse Down Config

- `ComputerLeftMouseDownConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Left Mouse Up Config

- `ComputerLeftMouseUpConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Middle Click Config

- `ComputerMiddleClickConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Mouse Move Config

- `ComputerMouseMoveConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Right Click Config

- `ComputerRightClickConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Screenshot Config

- `ComputerScreenshotConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Scroll Config

- `ComputerScrollConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Toolset 20260801

- `ComputerToolset20260801`

  - `"computer_toolset_20260801" type`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?ComputerToolsetConfigs configs`

    Per-member configuration for `computer_toolset_20260801`: one
    optional field per member tool, keyed by the member name — the same
    name the member's `tool_use` blocks carry. Every member is an
    accepted key, and a member's defaults apply wherever its key is
    absent. Unknown keys are rejected: the field set is this toolset
    version's complete member set.

### Computer Toolset Configs

- `ComputerToolsetConfigs`

  - `?ComputerTypeConfig type`

    `type`'s config overrides.

  - `?ComputerCursorPositionConfig cursorPosition`

    `cursor_position`'s config overrides.

  - `?ComputerDoubleClickConfig doubleClick`

    `double_click`'s config overrides.

  - `?ComputerHoldKeyConfig holdKey`

    `hold_key`'s config overrides.

  - `?ComputerKeyConfig key`

    `key`'s config overrides.

  - `?ComputerLeftClickConfig leftClick`

    `left_click`'s config overrides.

  - `?ComputerLeftClickDragConfig leftClickDrag`

    `left_click_drag`'s config overrides.

  - `?ComputerLeftMouseDownConfig leftMouseDown`

    `left_mouse_down`'s config overrides.

  - `?ComputerLeftMouseUpConfig leftMouseUp`

    `left_mouse_up`'s config overrides.

  - `?ComputerMiddleClickConfig middleClick`

    `middle_click`'s config overrides.

  - `?ComputerMouseMoveConfig mouseMove`

    `mouse_move`'s config overrides.

  - `?ComputerRightClickConfig rightClick`

    `right_click`'s config overrides.

  - `?ComputerScreenshotConfig screenshot`

    `screenshot`'s config overrides.

  - `?ComputerScrollConfig scroll`

    `scroll`'s config overrides.

  - `?ComputerTripleClickConfig tripleClick`

    `triple_click`'s config overrides.

  - `?ComputerWaitConfig wait`

    `wait`'s config overrides.

  - `?ComputerZoomConfig zoom`

    `zoom`'s config overrides.

### Computer Triple Click Config

- `ComputerTripleClickConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Type Config

- `ComputerTypeConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Wait Config

- `ComputerWaitConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Zoom Config

- `ComputerZoomConfig`

  - `?bool deferLoading`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `?bool enabled`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Container

- `Container`

  - `string id`

    Identifier for the container used in this request

  - `\Datetime expiresAt`

    The time at which the container will expire.

  - `?list<ContainerSkill> skills`

    Skills loaded in the container

### Container Params

- `ContainerParams`

  - `?string id`

    Container id

  - `?list<SkillParams> skills`

    List of skills to load in the container

### Container Skill

- `ContainerSkill`

  - `Type type`

    Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

  - `string skillID`

    Skill ID

  - `string version`

    The resolved version: a skill version ID for custom skills.

### Container Upload Block

- `ContainerUploadBlock`

  - `"container_upload" type`

  - `string fileID`

### Container Upload Block Param

- `ContainerUploadBlockParam`

  - `"container_upload" type`

  - `string fileID`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

### Content Block

- `ContentBlock`

  - `TextBlock`

    - `"text" type`

    - `?list<TextCitation> citations`

      Citations supporting the text block.

      The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

    - `string text`

  - `ThinkingBlock`

    - `"thinking" type`

    - `string signature`

      A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

      This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

      See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

    - `string thinking`

      The text of Claude's thinking process for this block.

  - `RedactedThinkingBlock`

    - `"redacted_thinking" type`

    - `string data`

      The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

      Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

      See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

  - `ToolUseBlock`

    - `"tool_use" type`

    - `string id`

    - `Caller caller`

    - `array<string,mixed> input`

    - `string name`

    - `?string toolsetName`

      For a toolset member tool_use, the toolset family.

  - `ServerToolUseBlock`

    - `"server_tool_use" type`

    - `string id`

    - `Caller caller`

    - `array<string,mixed> input`

    - `Name name`

  - `WebSearchToolResultBlock`

    - `"web_search_tool_result" type`

    - `Caller caller`

    - `WebSearchToolResultBlockContent content`

    - `string toolUseID`

  - `WebFetchToolResultBlock`

    - `"web_fetch_tool_result" type`

    - `Caller caller`

    - `Content content`

    - `string toolUseID`

  - `CodeExecutionToolResultBlock`

    - `"code_execution_tool_result" type`

    - `CodeExecutionToolResultBlockContent content`

    - `string toolUseID`

  - `BashCodeExecutionToolResultBlock`

    - `"bash_code_execution_tool_result" type`

    - `Content content`

    - `string toolUseID`

  - `TextEditorCodeExecutionToolResultBlock`

    - `"text_editor_code_execution_tool_result" type`

    - `Content content`

    - `string toolUseID`

  - `ToolSearchToolResultBlock`

    - `"tool_search_tool_result" type`

    - `Content content`

    - `string toolUseID`

  - `ContainerUploadBlock`

    - `"container_upload" type`

    - `string fileID`

### Content Block Param

- `ContentBlockParam`

  - `TextBlockParam`

    - `"text" type`

    - `string text`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?list<TextCitationParam> citations`

  - `ImageBlockParam`

    - `"image" type`

    - `Source source`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?ImageTransformationsParam transformations`

      Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

  - `DocumentBlockParam`

    - `"document" type`

    - `Source source`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?CitationsConfigParam citations`

    - `?string context`

    - `?string title`

  - `SearchResultBlockParam`

    - `"search_result" type`

    - `list<TextBlockParam> content`

    - `string source`

    - `string title`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?CitationsConfigParam citations`

  - `ThinkingBlockParam`

    - `"thinking" type`

    - `string signature`

      The `signature` value of this thinking block, exactly as returned by the API in a previous response. Used to verify that the block was generated by Claude.

      Thinking blocks must be passed back unmodified and in their original order; a modified block results in a 400 `invalid_request_error`.

    - `string thinking`

      The `thinking` text of this block as returned by the API.

  - `RedactedThinkingBlockParam`

    - `"redacted_thinking" type`

    - `string data`

      The `data` value of this redacted thinking block, exactly as returned by the API in a previous response. Opaque and encrypted; pass it back unchanged.

  - `ToolUseBlockParam`

    - `"tool_use" type`

    - `string id`

    - `array<string,mixed> input`

    - `string name`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?Caller caller`

    - `?string toolsetName`

      For a toolset member tool_use, the toolset family this member belongs to.

  - `ToolResultBlockParam`

    - `"tool_result" type`

    - `string toolUseID`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?Content content`

    - `?bool isError`

    - `?string toolsetName`

      For a toolset member tool_result, the toolset family of the paired tool_use.

  - `ServerToolUseBlockParam`

    - `"server_tool_use" type`

    - `string id`

    - `array<string,mixed> input`

    - `Name name`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?Caller caller`

  - `WebSearchToolResultBlockParam`

    - `"web_search_tool_result" type`

    - `WebSearchToolResultBlockParamContent content`

    - `string toolUseID`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?Caller caller`

  - `WebFetchToolResultBlockParam`

    - `"web_fetch_tool_result" type`

    - `Content content`

    - `string toolUseID`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?Caller caller`

  - `CodeExecutionToolResultBlockParam`

    - `"code_execution_tool_result" type`

    - `CodeExecutionToolResultBlockParamContent content`

    - `string toolUseID`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

  - `BashCodeExecutionToolResultBlockParam`

    - `"bash_code_execution_tool_result" type`

    - `Content content`

    - `string toolUseID`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

  - `TextEditorCodeExecutionToolResultBlockParam`

    - `"text_editor_code_execution_tool_result" type`

    - `Content content`

    - `string toolUseID`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

  - `ToolSearchToolResultBlockParam`

    - `"tool_search_tool_result" type`

    - `Content content`

    - `string toolUseID`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

  - `ContainerUploadBlockParam`

    - `"container_upload" type`

    - `string fileID`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

### Content Block Source

- `ContentBlockSource`

  - `"content" type`

  - `Content content`

### Content Block Source Content

- `ContentBlockSourceContent`

  - `TextBlockParam`

    - `"text" type`

    - `string text`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?list<TextCitationParam> citations`

  - `ImageBlockParam`

    - `"image" type`

    - `Source source`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?ImageTransformationsParam transformations`

      Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

### Direct Caller

- `DirectCaller`

  - `"direct" type`

### Document Block

- `DocumentBlock`

  - `"document" type`

  - `?CitationsConfig citations`

    Citation configuration for the document

  - `Source source`

  - `?string title`

    The title of the document

### Document Block Param

- `DocumentBlockParam`

  - `"document" type`

  - `Source source`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?CitationsConfigParam citations`

  - `?string context`

  - `?string title`

### Encrypted Code Execution Result Block

- `EncryptedCodeExecutionResultBlock`

  - `"encrypted_code_execution_result" type`

  - `list<CodeExecutionOutputBlock> content`

  - `string encryptedStdout`

  - `int returnCode`

  - `string stderr`

### Encrypted Code Execution Result Block Param

- `EncryptedCodeExecutionResultBlockParam`

  - `"encrypted_code_execution_result" type`

  - `list<CodeExecutionOutputBlockParam> content`

  - `string encryptedStdout`

  - `int returnCode`

  - `string stderr`

### File Document Source

- `FileDocumentSource`

  - `"file" type`

  - `string fileID`

### File Image Source

- `FileImageSource`

  - `"file" type`

  - `string fileID`

### Image Block Param

- `ImageBlockParam`

  - `"image" type`

  - `Source source`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?ImageTransformationsParam transformations`

    Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

### Image Transformations Param

- `ImageTransformationsParam`

  - `?OversizedImage oversizedImage`

    What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

### Input JSON Delta

- `InputJSONDelta`

  - `"input_json_delta" type`

  - `string partialJSON`

### JSON Output Format

- `JSONOutputFormat`

  - `"json_schema" type`

  - `array<string,mixed> schema`

    The JSON schema of the format

### Memory Tool 20250818

- `MemoryTool20250818`

  - `"memory_20250818" type`

  - `"memory" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?list<array<string,mixed>> inputExamples`

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Message

- `Message`

  - `"message" type`

    Object type.

    For Messages, this is always `"message"`.

  - `string id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `?Container container`

    Information about the container used in the request (for the code execution tool)

  - `list<ContentBlock> content`

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

  - `Model model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `"assistant" role`

    Conversational role of the generated message.

    This will always be `"assistant"`.

  - `?RefusalStopDetails stopDetails`

    Structured information about a refusal.

  - `?StopReason stopReason`

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

  - `Usage usage`

    Billing and rate-limit usage.

    Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

    Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

    For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

    Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

### Message Count Tokens Tool

- `MessageCountTokensTool`

  - `Tool`

    - `?Type type`

    - `InputSchema inputSchema`

      [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

      This defines the shape of the `input` that your tool accepts and that the model will produce.

    - `string name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

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

  - `ToolBash20250124`

    - `"bash_20250124" type`

    - `"bash" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `CodeExecutionTool20250522`

    - `"code_execution_20250522" type`

    - `"code_execution" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `CodeExecutionTool20250825`

    - `"code_execution_20250825" type`

    - `"code_execution" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `CodeExecutionTool20260120`

    - `"code_execution_20260120" type`

    - `"code_execution" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `CodeExecutionTool20260521`

    - `"code_execution_20260521" type`

    - `"code_execution" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `BrowserToolset20260801`

    - `"browser_toolset_20260801" type`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?BrowserToolsetConfigs configs`

      Per-member configuration for `browser_toolset_20260801`: one
      optional field per member tool, keyed by the member name — the same
      name the member's `tool_use` blocks carry. Every member is an
      accepted key, and a member's defaults apply wherever its key is
      absent. Unknown keys are rejected: the field set is this toolset
      version's complete member set.

  - `MemoryTool20250818`

    - `"memory_20250818" type`

    - `"memory" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `ComputerToolset20260801`

    - `"computer_toolset_20260801" type`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?ComputerToolsetConfigs configs`

      Per-member configuration for `computer_toolset_20260801`: one
      optional field per member tool, keyed by the member name — the same
      name the member's `tool_use` blocks carry. Every member is an
      accepted key, and a member's defaults apply wherever its key is
      absent. Unknown keys are rejected: the field set is this toolset
      version's complete member set.

  - `ToolTextEditor20250124`

    - `"text_editor_20250124" type`

    - `"str_replace_editor" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `ToolTextEditor20250429`

    - `"text_editor_20250429" type`

    - `"str_replace_based_edit_tool" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `ToolTextEditor20250728`

    - `"text_editor_20250728" type`

    - `"str_replace_based_edit_tool" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?int maxCharacters`

      Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `WebSearchTool20250305`

    - `"web_search_20250305" type`

    - `"web_search" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `?list<string> blockedDomains`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

    - `?UserLocation userLocation`

      Parameters for the user's location. Used to provide more relevant search results.

  - `WebFetchTool20250910`

    - `"web_fetch_20250910" type`

    - `"web_fetch" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      List of domains to allow fetching from

    - `?list<string> blockedDomains`

      List of domains to block fetching from

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?CitationsConfigParam citations`

      Citations configuration for fetched documents. Citations are disabled by default.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxContentTokens`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `WebSearchTool20260209`

    - `"web_search_20260209" type`

    - `"web_search" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `?list<string> blockedDomains`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

    - `?UserLocation userLocation`

      Parameters for the user's location. Used to provide more relevant search results.

  - `WebFetchTool20260209`

    - `"web_fetch_20260209" type`

    - `"web_fetch" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      List of domains to allow fetching from

    - `?list<string> blockedDomains`

      List of domains to block fetching from

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?CitationsConfigParam citations`

      Citations configuration for fetched documents. Citations are disabled by default.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxContentTokens`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `WebFetchTool20260309`

    - `"web_fetch_20260309" type`

    - `"web_fetch" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      List of domains to allow fetching from

    - `?list<string> blockedDomains`

      List of domains to block fetching from

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?CitationsConfigParam citations`

      Citations configuration for fetched documents. Citations are disabled by default.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxContentTokens`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

    - `?bool useCache`

      Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

  - `WebSearchTool20260318`

    - `"web_search_20260318" type`

    - `"web_search" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `?list<string> blockedDomains`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?ResponseInclusion responseInclusion`

      How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

    - `?UserLocation userLocation`

      Parameters for the user's location. Used to provide more relevant search results.

  - `WebFetchTool20260318`

    - `"web_fetch_20260318" type`

    - `"web_fetch" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      List of domains to allow fetching from

    - `?list<string> blockedDomains`

      List of domains to block fetching from

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?CitationsConfigParam citations`

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

    - `?bool useCache`

      Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

  - `ToolSearchToolBm25_20251119`

    - `Type type`

    - `"tool_search_tool_bm25" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `ToolSearchToolRegex20251119`

    - `Type type`

    - `"tool_search_tool_regex" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

### Message Create Params Container

- `MessageCreateParamsContainer`

  - `ContainerParams`

    - `?string id`

      Container id

    - `?list<SkillParams> skills`

      List of skills to load in the container

  - `string`

### Message Delta Usage

- `MessageDeltaUsage`

  - `?int cacheCreationInputTokens`

    The cumulative number of input tokens used to create the cache entry.

  - `?int cacheReadInputTokens`

    The cumulative number of input tokens read from the cache.

  - `?int inputTokens`

    The cumulative number of input tokens which were used.

  - `int outputTokens`

    The cumulative number of output tokens which were used.

  - `?OutputTokensDetails outputTokensDetails`

    Breakdown of output tokens by category.

    `output_tokens` remains the inclusive, authoritative total used for billing.
    This object provides a read-only decomposition for observability — for example,
    how many of the billed output tokens were spent on internal reasoning that may
    have been summarized before being returned to you.

  - `?ServerToolUsage serverToolUse`

    The number of server tool requests.

### Message Param

- `MessageParam`

  - `Content content`

  - `Role role`

### Message Tokens Count

- `MessageTokensCount`

  - `int inputTokens`

    The total number of tokens across the provided list of messages, system prompt, and tools.

### Metadata

- `Metadata`

  - `?string userID`

    An external identifier for the user who is associated with the request.

    This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

### Model

- `Model`

  - `"claude-fable-5-1"`

    Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

  - `"claude-mythos-5-1"`

    Our most capable model for cybersecurity and biology research, available through trusted access programs

  - `"claude-sonnet-5"`

    High-performance model for coding and agents

  - `"claude-fable-5"`

    Next generation of intelligence for the hardest knowledge work and coding problems

  - `"claude-mythos-5"`

    Most capable model for cybersecurity and biology research

  - `"claude-opus-5"`

    Powerful intelligence for long-running agents and coding

  - `"claude-opus-4-8"`

    Powerful intelligence for long-running agents and coding

  - `"claude-opus-4-7"`

    Powerful intelligence for long-running agents and coding

  - `"claude-mythos-preview"`

    New class of intelligence, strongest in coding and cybersecurity

  - `"claude-opus-4-6"`

    Powerful intelligence for long-running agents and coding

  - `"claude-sonnet-4-6"`

    Best combination of speed and intelligence

  - `"claude-haiku-4-5"`

    Fastest model with near-frontier intelligence

  - `"claude-haiku-4-5-20251001"`

    Fastest model with near-frontier intelligence

  - `"claude-opus-4-5"`

    Powerful intelligence for long-running agents and coding

  - `"claude-opus-4-5-20251101"`

    Powerful intelligence for long-running agents and coding

  - `"claude-sonnet-4-5"`

    High-performance model for agents and coding

  - `"claude-sonnet-4-5-20250929"`

    High-performance model for agents and coding

### Output Config

- `OutputConfig`

  - `?Effort effort`

    All possible effort levels.

  - `?JSONOutputFormat format`

    A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

### Output Tokens Details

- `OutputTokensDetails`

  - `int thinkingTokens`

    Number of output tokens the model generated as internal reasoning, including
    the thinking-block delimiter tokens.

    Reflects the raw reasoning the model produced, not the (possibly shorter)
    summarized thinking text returned in the response body. Computed by
    re-tokenizing the raw reasoning text, so it may differ from the model's exact
    generation count by a small number of tokens. Always ≤ `output_tokens`;
    `output_tokens - thinking_tokens` approximates the non-reasoning output.

### Plain Text Source

- `PlainTextSource`

  - `"text" type`

  - `string data`

  - `"text/plain" mediaType`

### Raw Content Block Delta

- `RawContentBlockDelta`

  - `TextDelta`

    - `"text_delta" type`

    - `string text`

  - `InputJSONDelta`

    - `"input_json_delta" type`

    - `string partialJSON`

  - `CitationsDelta`

    - `"citations_delta" type`

    - `Citation citation`

  - `ThinkingDelta`

    - `"thinking_delta" type`

    - `string thinking`

      The incremental `thinking` text for this content block. Concatenate the `thinking` values of successive `thinking_delta` events to assemble the block's full `thinking` value.

  - `SignatureDelta`

    - `"signature_delta" type`

    - `string signature`

      The `signature` for this thinking block: an opaque value used to verify that the block was generated by Claude when it is passed back to the API. Delivered in a `signature_delta` event just before the block's `content_block_stop` event.

### Raw Content Block Delta Event

- `RawContentBlockDeltaEvent`

  - `"content_block_delta" type`

  - `RawContentBlockDelta delta`

  - `int index`

### Raw Content Block Start Event

- `RawContentBlockStartEvent`

  - `"content_block_start" type`

  - `ContentBlock contentBlock`

  - `int index`

### Raw Content Block Stop Event

- `RawContentBlockStopEvent`

  - `"content_block_stop" type`

  - `int index`

### Raw Message Delta Event

- `RawMessageDeltaEvent`

  - `"message_delta" type`

  - `Delta delta`

  - `MessageDeltaUsage usage`

    Billing and rate-limit usage.

    Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

    Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

    For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

    Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

### Raw Message Start Event

- `RawMessageStartEvent`

  - `"message_start" type`

  - `Message message`

### Raw Message Stop Event

- `RawMessageStopEvent`

  - `"message_stop" type`

### Raw Message Stream Event

- `RawMessageStreamEvent`

  - `RawMessageStartEvent`

    - `"message_start" type`

    - `Message message`

  - `RawMessageDeltaEvent`

    - `"message_delta" type`

    - `Delta delta`

    - `MessageDeltaUsage usage`

      Billing and rate-limit usage.

      Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

      Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

      For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

      Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

  - `RawMessageStopEvent`

    - `"message_stop" type`

  - `RawContentBlockStartEvent`

    - `"content_block_start" type`

    - `ContentBlock contentBlock`

    - `int index`

  - `RawContentBlockDeltaEvent`

    - `"content_block_delta" type`

    - `RawContentBlockDelta delta`

    - `int index`

  - `RawContentBlockStopEvent`

    - `"content_block_stop" type`

    - `int index`

### Redacted Thinking Block

- `RedactedThinkingBlock`

  - `"redacted_thinking" type`

  - `string data`

    The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

    Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

    See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

### Redacted Thinking Block Param

- `RedactedThinkingBlockParam`

  - `"redacted_thinking" type`

  - `string data`

    The `data` value of this redacted thinking block, exactly as returned by the API in a previous response. Opaque and encrypted; pass it back unchanged.

### Refusal Stop Details

- `RefusalStopDetails`

  - `"refusal" type`

  - `?Category category`

    The policy category that triggered a refusal.

  - `?string explanation`

    Human-readable explanation of the refusal.

    This text is not guaranteed to be stable. `null` when no explanation is available for the category.

### Search Result Block Param

- `SearchResultBlockParam`

  - `"search_result" type`

  - `list<TextBlockParam> content`

  - `string source`

  - `string title`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?CitationsConfigParam citations`

### Server Tool Caller

- `ServerToolCaller`

  - `"code_execution_20250825" type`

  - `string toolID`

### Server Tool Caller 20260120

- `ServerToolCaller20260120`

  - `"code_execution_20260120" type`

  - `string toolID`

### Server Tool Usage

- `ServerToolUsage`

  - `int webFetchRequests`

    The number of web fetch tool requests.

  - `int webSearchRequests`

    The number of web search tool requests.

### Server Tool Use Block

- `ServerToolUseBlock`

  - `"server_tool_use" type`

  - `string id`

  - `Caller caller`

  - `array<string,mixed> input`

  - `Name name`

### Server Tool Use Block Param

- `ServerToolUseBlockParam`

  - `"server_tool_use" type`

  - `string id`

  - `array<string,mixed> input`

  - `Name name`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?Caller caller`

### Signature Delta

- `SignatureDelta`

  - `"signature_delta" type`

  - `string signature`

    The `signature` for this thinking block: an opaque value used to verify that the block was generated by Claude when it is passed back to the API. Delivered in a `signature_delta` event just before the block's `content_block_stop` event.

### Skill Params

- `SkillParams`

  - `Type type`

    Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

  - `string skillID`

    Skill ID

  - `?string version`

    Skill version or 'latest' for most recent version

### Stop Reason

- `StopReason`

  - `"end_turn"`

  - `"max_tokens"`

  - `"stop_sequence"`

  - `"tool_use"`

  - `"pause_turn"`

  - `"refusal"`

  - `"model_context_window_exceeded"`

### Text Block

- `TextBlock`

  - `"text" type`

  - `?list<TextCitation> citations`

    Citations supporting the text block.

    The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

  - `string text`

### Text Block Param

- `TextBlockParam`

  - `"text" type`

  - `string text`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?list<TextCitationParam> citations`

### Text Citation

- `TextCitation`

  - `CitationCharLocation`

    - `"char_location" type`

    - `string citedText`

    - `int documentIndex`

    - `?string documentTitle`

    - `int endCharIndex`

    - `?string fileID`

    - `int startCharIndex`

  - `CitationPageLocation`

    - `"page_location" type`

    - `string citedText`

    - `int documentIndex`

    - `?string documentTitle`

    - `int endPageNumber`

    - `?string fileID`

    - `int startPageNumber`

  - `CitationContentBlockLocation`

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

  - `CitationsWebSearchResultLocation`

    - `"web_search_result_location" type`

    - `string citedText`

    - `string encryptedIndex`

    - `?string title`

    - `string url`

  - `CitationsSearchResultLocation`

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

### Text Citation Param

- `TextCitationParam`

  - `CitationCharLocationParam`

    - `"char_location" type`

    - `string citedText`

    - `int documentIndex`

    - `?string documentTitle`

    - `int endCharIndex`

    - `int startCharIndex`

  - `CitationPageLocationParam`

    - `"page_location" type`

    - `string citedText`

    - `int documentIndex`

    - `?string documentTitle`

    - `int endPageNumber`

    - `int startPageNumber`

  - `CitationContentBlockLocationParam`

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

  - `CitationWebSearchResultLocationParam`

    - `"web_search_result_location" type`

    - `string citedText`

    - `string encryptedIndex`

    - `?string title`

    - `string url`

  - `CitationSearchResultLocationParam`

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

### Text Delta

- `TextDelta`

  - `"text_delta" type`

  - `string text`

### Text Editor Code Execution Create Result Block

- `TextEditorCodeExecutionCreateResultBlock`

  - `"text_editor_code_execution_create_result" type`

  - `bool isFileUpdate`

### Text Editor Code Execution Create Result Block Param

- `TextEditorCodeExecutionCreateResultBlockParam`

  - `"text_editor_code_execution_create_result" type`

  - `bool isFileUpdate`

### Text Editor Code Execution Str Replace Result Block

- `TextEditorCodeExecutionStrReplaceResultBlock`

  - `"text_editor_code_execution_str_replace_result" type`

  - `?list<string> lines`

  - `?int newLines`

  - `?int newStart`

  - `?int oldLines`

  - `?int oldStart`

### Text Editor Code Execution Str Replace Result Block Param

- `TextEditorCodeExecutionStrReplaceResultBlockParam`

  - `"text_editor_code_execution_str_replace_result" type`

  - `?list<string> lines`

  - `?int newLines`

  - `?int newStart`

  - `?int oldLines`

  - `?int oldStart`

### Text Editor Code Execution Tool Result Block

- `TextEditorCodeExecutionToolResultBlock`

  - `"text_editor_code_execution_tool_result" type`

  - `Content content`

  - `string toolUseID`

### Text Editor Code Execution Tool Result Block Param

- `TextEditorCodeExecutionToolResultBlockParam`

  - `"text_editor_code_execution_tool_result" type`

  - `Content content`

  - `string toolUseID`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

### Text Editor Code Execution Tool Result Error

- `TextEditorCodeExecutionToolResultError`

  - `"text_editor_code_execution_tool_result_error" type`

  - `TextEditorCodeExecutionToolResultErrorCode errorCode`

  - `?string errorMessage`

### Text Editor Code Execution Tool Result Error Code

- `TextEditorCodeExecutionToolResultErrorCode`

  - `"invalid_tool_input"`

  - `"unavailable"`

  - `"too_many_requests"`

  - `"execution_time_exceeded"`

  - `"file_not_found"`

### Text Editor Code Execution Tool Result Error Param

- `TextEditorCodeExecutionToolResultErrorParam`

  - `"text_editor_code_execution_tool_result_error" type`

  - `TextEditorCodeExecutionToolResultErrorCode errorCode`

  - `?string errorMessage`

### Text Editor Code Execution View Result Block

- `TextEditorCodeExecutionViewResultBlock`

  - `"text_editor_code_execution_view_result" type`

  - `string content`

  - `FileType fileType`

  - `?int numLines`

  - `?int startLine`

  - `?int totalLines`

### Text Editor Code Execution View Result Block Param

- `TextEditorCodeExecutionViewResultBlockParam`

  - `"text_editor_code_execution_view_result" type`

  - `string content`

  - `FileType fileType`

  - `?int numLines`

  - `?int startLine`

  - `?int totalLines`

### Thinking Block

- `ThinkingBlock`

  - `"thinking" type`

  - `string signature`

    A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

    This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

    See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

  - `string thinking`

    The text of Claude's thinking process for this block.

### Thinking Block Param

- `ThinkingBlockParam`

  - `"thinking" type`

  - `string signature`

    The `signature` value of this thinking block, exactly as returned by the API in a previous response. Used to verify that the block was generated by Claude.

    Thinking blocks must be passed back unmodified and in their original order; a modified block results in a 400 `invalid_request_error`.

  - `string thinking`

    The `thinking` text of this block as returned by the API.

### Thinking Config Adaptive

- `ThinkingConfigAdaptive`

  - `"adaptive" type`

  - `?Display display`

    Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

### Thinking Config Disabled

- `ThinkingConfigDisabled`

  - `"disabled" type`

### Thinking Config Enabled

- `ThinkingConfigEnabled`

  - `"enabled" type`

  - `int budgetTokens`

    Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

    Must be ≥1024 and less than `max_tokens`.

    See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

  - `?Display display`

    Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

### Thinking Config Param

- `ThinkingConfigParam`

  - `ThinkingConfigEnabled`

    - `"enabled" type`

    - `int budgetTokens`

      Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

      Must be ≥1024 and less than `max_tokens`.

      See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

    - `?Display display`

      Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

  - `ThinkingConfigDisabled`

    - `"disabled" type`

  - `ThinkingConfigAdaptive`

    - `"adaptive" type`

    - `?Display display`

      Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

### Thinking Delta

- `ThinkingDelta`

  - `"thinking_delta" type`

  - `string thinking`

    The incremental `thinking` text for this content block. Concatenate the `thinking` values of successive `thinking_delta` events to assemble the block's full `thinking` value.

### Tool

- `Tool`

  - `?Type type`

  - `InputSchema inputSchema`

    [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

    This defines the shape of the `input` that your tool accepts and that the model will produce.

  - `string name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?CacheControlEphemeral cacheControl`

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

### Tool Bash 20250124

- `ToolBash20250124`

  - `"bash_20250124" type`

  - `"bash" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?list<array<string,mixed>> inputExamples`

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Tool Choice

- `ToolChoice`

  - `ToolChoiceAuto`

    - `"auto" type`

    - `?bool disableParallelToolUse`

      Whether to disable parallel tool use.

      Defaults to `false`. If set to `true`, the model will output at most one tool use.

  - `ToolChoiceAny`

    - `"any" type`

    - `?bool disableParallelToolUse`

      Whether to disable parallel tool use.

      Defaults to `false`. If set to `true`, the model will output exactly one tool use.

  - `ToolChoiceTool`

    - `"tool" type`

    - `string name`

      The name of the tool to use.

    - `?bool disableParallelToolUse`

      Whether to disable parallel tool use.

      Defaults to `false`. If set to `true`, the model will output exactly one tool use.

  - `ToolChoiceNone`

    - `"none" type`

### Tool Choice Any

- `ToolChoiceAny`

  - `"any" type`

  - `?bool disableParallelToolUse`

    Whether to disable parallel tool use.

    Defaults to `false`. If set to `true`, the model will output exactly one tool use.

### Tool Choice Auto

- `ToolChoiceAuto`

  - `"auto" type`

  - `?bool disableParallelToolUse`

    Whether to disable parallel tool use.

    Defaults to `false`. If set to `true`, the model will output at most one tool use.

### Tool Choice None

- `ToolChoiceNone`

  - `"none" type`

### Tool Choice Tool

- `ToolChoiceTool`

  - `"tool" type`

  - `string name`

    The name of the tool to use.

  - `?bool disableParallelToolUse`

    Whether to disable parallel tool use.

    Defaults to `false`. If set to `true`, the model will output exactly one tool use.

### Tool Reference Block

- `ToolReferenceBlock`

  - `"tool_reference" type`

  - `string toolName`

### Tool Reference Block Param

- `ToolReferenceBlockParam`

  - `"tool_reference" type`

  - `string toolName`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

### Tool Result Block Param

- `ToolResultBlockParam`

  - `"tool_result" type`

  - `string toolUseID`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?Content content`

  - `?bool isError`

  - `?string toolsetName`

    For a toolset member tool_result, the toolset family of the paired tool_use.

### Tool Search Tool Bm25 20251119

- `ToolSearchToolBm25_20251119`

  - `Type type`

  - `"tool_search_tool_bm25" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Tool Search Tool Regex 20251119

- `ToolSearchToolRegex20251119`

  - `Type type`

  - `"tool_search_tool_regex" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Tool Search Tool Result Block

- `ToolSearchToolResultBlock`

  - `"tool_search_tool_result" type`

  - `Content content`

  - `string toolUseID`

### Tool Search Tool Result Block Param

- `ToolSearchToolResultBlockParam`

  - `"tool_search_tool_result" type`

  - `Content content`

  - `string toolUseID`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

### Tool Search Tool Result Error

- `ToolSearchToolResultError`

  - `"tool_search_tool_result_error" type`

  - `ToolSearchToolResultErrorCode errorCode`

  - `?string errorMessage`

### Tool Search Tool Result Error Code

- `ToolSearchToolResultErrorCode`

  - `"invalid_tool_input"`

  - `"unavailable"`

  - `"too_many_requests"`

  - `"execution_time_exceeded"`

### Tool Search Tool Result Error Param

- `ToolSearchToolResultErrorParam`

  - `"tool_search_tool_result_error" type`

  - `ToolSearchToolResultErrorCode errorCode`

  - `?string errorMessage`

### Tool Search Tool Search Result Block

- `ToolSearchToolSearchResultBlock`

  - `"tool_search_tool_search_result" type`

  - `list<ToolReferenceBlock> toolReferences`

### Tool Search Tool Search Result Block Param

- `ToolSearchToolSearchResultBlockParam`

  - `"tool_search_tool_search_result" type`

  - `list<ToolReferenceBlockParam> toolReferences`

### Tool Text Editor 20250124

- `ToolTextEditor20250124`

  - `"text_editor_20250124" type`

  - `"str_replace_editor" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?list<array<string,mixed>> inputExamples`

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Tool Text Editor 20250429

- `ToolTextEditor20250429`

  - `"text_editor_20250429" type`

  - `"str_replace_based_edit_tool" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?list<array<string,mixed>> inputExamples`

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Tool Text Editor 20250728

- `ToolTextEditor20250728`

  - `"text_editor_20250728" type`

  - `"str_replace_based_edit_tool" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?list<array<string,mixed>> inputExamples`

  - `?int maxCharacters`

    Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Tool Union

- `ToolUnion`

  - `Tool`

    - `?Type type`

    - `InputSchema inputSchema`

      [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

      This defines the shape of the `input` that your tool accepts and that the model will produce.

    - `string name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

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

  - `ToolBash20250124`

    - `"bash_20250124" type`

    - `"bash" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `CodeExecutionTool20250522`

    - `"code_execution_20250522" type`

    - `"code_execution" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `CodeExecutionTool20250825`

    - `"code_execution_20250825" type`

    - `"code_execution" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `CodeExecutionTool20260120`

    - `"code_execution_20260120" type`

    - `"code_execution" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `CodeExecutionTool20260521`

    - `"code_execution_20260521" type`

    - `"code_execution" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `BrowserToolset20260801`

    - `"browser_toolset_20260801" type`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?BrowserToolsetConfigs configs`

      Per-member configuration for `browser_toolset_20260801`: one
      optional field per member tool, keyed by the member name — the same
      name the member's `tool_use` blocks carry. Every member is an
      accepted key, and a member's defaults apply wherever its key is
      absent. Unknown keys are rejected: the field set is this toolset
      version's complete member set.

  - `MemoryTool20250818`

    - `"memory_20250818" type`

    - `"memory" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `ComputerToolset20260801`

    - `"computer_toolset_20260801" type`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?ComputerToolsetConfigs configs`

      Per-member configuration for `computer_toolset_20260801`: one
      optional field per member tool, keyed by the member name — the same
      name the member's `tool_use` blocks carry. Every member is an
      accepted key, and a member's defaults apply wherever its key is
      absent. Unknown keys are rejected: the field set is this toolset
      version's complete member set.

  - `ToolTextEditor20250124`

    - `"text_editor_20250124" type`

    - `"str_replace_editor" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `ToolTextEditor20250429`

    - `"text_editor_20250429" type`

    - `"str_replace_based_edit_tool" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `ToolTextEditor20250728`

    - `"text_editor_20250728" type`

    - `"str_replace_based_edit_tool" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?list<array<string,mixed>> inputExamples`

    - `?int maxCharacters`

      Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `WebSearchTool20250305`

    - `"web_search_20250305" type`

    - `"web_search" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `?list<string> blockedDomains`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

    - `?UserLocation userLocation`

      Parameters for the user's location. Used to provide more relevant search results.

  - `WebFetchTool20250910`

    - `"web_fetch_20250910" type`

    - `"web_fetch" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      List of domains to allow fetching from

    - `?list<string> blockedDomains`

      List of domains to block fetching from

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?CitationsConfigParam citations`

      Citations configuration for fetched documents. Citations are disabled by default.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxContentTokens`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `WebSearchTool20260209`

    - `"web_search_20260209" type`

    - `"web_search" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `?list<string> blockedDomains`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

    - `?UserLocation userLocation`

      Parameters for the user's location. Used to provide more relevant search results.

  - `WebFetchTool20260209`

    - `"web_fetch_20260209" type`

    - `"web_fetch" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      List of domains to allow fetching from

    - `?list<string> blockedDomains`

      List of domains to block fetching from

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?CitationsConfigParam citations`

      Citations configuration for fetched documents. Citations are disabled by default.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxContentTokens`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `WebFetchTool20260309`

    - `"web_fetch_20260309" type`

    - `"web_fetch" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      List of domains to allow fetching from

    - `?list<string> blockedDomains`

      List of domains to block fetching from

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?CitationsConfigParam citations`

      Citations configuration for fetched documents. Citations are disabled by default.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxContentTokens`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

    - `?bool useCache`

      Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

  - `WebSearchTool20260318`

    - `"web_search_20260318" type`

    - `"web_search" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `?list<string> blockedDomains`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?int maxUses`

      Maximum number of times the tool can be used in the API request.

    - `?ResponseInclusion responseInclusion`

      How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

    - `?UserLocation userLocation`

      Parameters for the user's location. Used to provide more relevant search results.

  - `WebFetchTool20260318`

    - `"web_fetch_20260318" type`

    - `"web_fetch" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?list<string> allowedDomains`

      List of domains to allow fetching from

    - `?list<string> blockedDomains`

      List of domains to block fetching from

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?CitationsConfigParam citations`

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

    - `?bool useCache`

      Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

  - `ToolSearchToolBm25_20251119`

    - `Type type`

    - `"tool_search_tool_bm25" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

  - `ToolSearchToolRegex20251119`

    - `Type type`

    - `"tool_search_tool_regex" name`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `?list<AllowedCaller> allowedCallers`

    - `?CacheControlEphemeral cacheControl`

      Create a cache control breakpoint at this content block.

    - `?bool deferLoading`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `?bool strict`

      When true, guarantees schema validation on tool names and inputs

### Tool Use Block

- `ToolUseBlock`

  - `"tool_use" type`

  - `string id`

  - `Caller caller`

  - `array<string,mixed> input`

  - `string name`

  - `?string toolsetName`

    For a toolset member tool_use, the toolset family.

### Tool Use Block Param

- `ToolUseBlockParam`

  - `"tool_use" type`

  - `string id`

  - `array<string,mixed> input`

  - `string name`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?Caller caller`

  - `?string toolsetName`

    For a toolset member tool_use, the toolset family this member belongs to.

### URL Image Source

- `URLImageSource`

  - `"url" type`

  - `string url`

### URL PDF Source

- `URLPDFSource`

  - `"url" type`

  - `string url`

### Usage

- `Usage`

  - `?CacheCreation cacheCreation`

    Breakdown of cached tokens by TTL

  - `?int cacheCreationInputTokens`

    The number of input tokens used to create the cache entry.

  - `?int cacheReadInputTokens`

    The number of input tokens read from the cache.

  - `?string inferenceGeo`

    The geographic region where inference was performed for this request.

  - `int inputTokens`

    The number of input tokens which were used.

  - `int outputTokens`

    The number of output tokens which were used.

  - `?OutputTokensDetails outputTokensDetails`

    Breakdown of output tokens by category.

    `output_tokens` remains the inclusive, authoritative total used for billing.
    This object provides a read-only decomposition for observability — for example,
    how many of the billed output tokens were spent on internal reasoning that may
    have been summarized before being returned to you.

  - `?ServerToolUsage serverToolUse`

    The number of server tool requests.

  - `?ServiceTier serviceTier`

    If the request used the priority, standard, or batch tier.

### User Location

- `UserLocation`

  - `"approximate" type`

  - `?string city`

    The city of the user.

  - `?string country`

    The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

  - `?string region`

    The region of the user.

  - `?string timezone`

    The [IANA timezone](https://nodatime.org/TimeZones) of the user.

### Web Fetch Block

- `WebFetchBlock`

  - `"web_fetch_result" type`

  - `DocumentBlock content`

  - `?string retrievedAt`

    ISO 8601 timestamp when the content was retrieved

  - `string url`

    Fetched content URL

### Web Fetch Block Param

- `WebFetchBlockParam`

  - `"web_fetch_result" type`

  - `DocumentBlockParam content`

  - `string url`

    Fetched content URL

  - `?string retrievedAt`

    ISO 8601 timestamp when the content was retrieved

### Web Fetch Tool 20250910

- `WebFetchTool20250910`

  - `"web_fetch_20250910" type`

  - `"web_fetch" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?list<string> allowedDomains`

    List of domains to allow fetching from

  - `?list<string> blockedDomains`

    List of domains to block fetching from

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?CitationsConfigParam citations`

    Citations configuration for fetched documents. Citations are disabled by default.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?int maxContentTokens`

    Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

  - `?int maxUses`

    Maximum number of times the tool can be used in the API request.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Web Fetch Tool 20260209

- `WebFetchTool20260209`

  - `"web_fetch_20260209" type`

  - `"web_fetch" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?list<string> allowedDomains`

    List of domains to allow fetching from

  - `?list<string> blockedDomains`

    List of domains to block fetching from

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?CitationsConfigParam citations`

    Citations configuration for fetched documents. Citations are disabled by default.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?int maxContentTokens`

    Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

  - `?int maxUses`

    Maximum number of times the tool can be used in the API request.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

### Web Fetch Tool 20260309

- `WebFetchTool20260309`

  - `"web_fetch_20260309" type`

  - `"web_fetch" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?list<string> allowedDomains`

    List of domains to allow fetching from

  - `?list<string> blockedDomains`

    List of domains to block fetching from

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?CitationsConfigParam citations`

    Citations configuration for fetched documents. Citations are disabled by default.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?int maxContentTokens`

    Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

  - `?int maxUses`

    Maximum number of times the tool can be used in the API request.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

  - `?bool useCache`

    Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

### Web Fetch Tool 20260318

- `WebFetchTool20260318`

  - `"web_fetch_20260318" type`

  - `"web_fetch" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?list<string> allowedDomains`

    List of domains to allow fetching from

  - `?list<string> blockedDomains`

    List of domains to block fetching from

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?CitationsConfigParam citations`

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

  - `?bool useCache`

    Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

### Web Fetch Tool Result Block

- `WebFetchToolResultBlock`

  - `"web_fetch_tool_result" type`

  - `Caller caller`

  - `Content content`

  - `string toolUseID`

### Web Fetch Tool Result Block Param

- `WebFetchToolResultBlockParam`

  - `"web_fetch_tool_result" type`

  - `Content content`

  - `string toolUseID`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?Caller caller`

### Web Fetch Tool Result Error Block

- `WebFetchToolResultErrorBlock`

  - `"web_fetch_tool_result_error" type`

  - `WebFetchToolResultErrorCode errorCode`

### Web Fetch Tool Result Error Block Param

- `WebFetchToolResultErrorBlockParam`

  - `"web_fetch_tool_result_error" type`

  - `WebFetchToolResultErrorCode errorCode`

### Web Fetch Tool Result Error Code

- `WebFetchToolResultErrorCode`

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

### Web Search Result Block

- `WebSearchResultBlock`

  - `"web_search_result" type`

  - `string encryptedContent`

  - `?string pageAge`

  - `string title`

  - `string url`

### Web Search Result Block Param

- `WebSearchResultBlockParam`

  - `"web_search_result" type`

  - `string encryptedContent`

  - `string title`

  - `string url`

  - `?string pageAge`

### Web Search Tool 20250305

- `WebSearchTool20250305`

  - `"web_search_20250305" type`

  - `"web_search" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?list<string> allowedDomains`

    If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

  - `?list<string> blockedDomains`

    If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?int maxUses`

    Maximum number of times the tool can be used in the API request.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

  - `?UserLocation userLocation`

    Parameters for the user's location. Used to provide more relevant search results.

### Web Search Tool 20260209

- `WebSearchTool20260209`

  - `"web_search_20260209" type`

  - `"web_search" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?list<string> allowedDomains`

    If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

  - `?list<string> blockedDomains`

    If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?int maxUses`

    Maximum number of times the tool can be used in the API request.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

  - `?UserLocation userLocation`

    Parameters for the user's location. Used to provide more relevant search results.

### Web Search Tool 20260318

- `WebSearchTool20260318`

  - `"web_search_20260318" type`

  - `"web_search" name`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `?list<AllowedCaller> allowedCallers`

  - `?list<string> allowedDomains`

    If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

  - `?list<string> blockedDomains`

    If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?bool deferLoading`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `?int maxUses`

    Maximum number of times the tool can be used in the API request.

  - `?ResponseInclusion responseInclusion`

    How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

  - `?bool strict`

    When true, guarantees schema validation on tool names and inputs

  - `?UserLocation userLocation`

    Parameters for the user's location. Used to provide more relevant search results.

### Web Search Tool Request Error

- `WebSearchToolRequestError`

  - `"web_search_tool_result_error" type`

  - `WebSearchToolResultErrorCode errorCode`

### Web Search Tool Result Block

- `WebSearchToolResultBlock`

  - `"web_search_tool_result" type`

  - `Caller caller`

  - `WebSearchToolResultBlockContent content`

  - `string toolUseID`

### Web Search Tool Result Block Content

- `WebSearchToolResultBlockContent`

  - `WebSearchToolResultError`

    - `"web_search_tool_result_error" type`

    - `WebSearchToolResultErrorCode errorCode`

  - `list<WebSearchResultBlock>`

    - `"web_search_result" type`

    - `string encryptedContent`

    - `?string pageAge`

    - `string title`

    - `string url`

### Web Search Tool Result Block Param

- `WebSearchToolResultBlockParam`

  - `"web_search_tool_result" type`

  - `WebSearchToolResultBlockParamContent content`

  - `string toolUseID`

  - `?CacheControlEphemeral cacheControl`

    Create a cache control breakpoint at this content block.

  - `?Caller caller`

### Web Search Tool Result Block Param Content

- `WebSearchToolResultBlockParamContent`

  - `list<WebSearchResultBlockParam>`

    - `"web_search_result" type`

    - `string encryptedContent`

    - `string title`

    - `string url`

    - `?string pageAge`

  - `WebSearchToolRequestError`

    - `"web_search_tool_result_error" type`

    - `WebSearchToolResultErrorCode errorCode`

### Web Search Tool Result Error

- `WebSearchToolResultError`

  - `"web_search_tool_result_error" type`

  - `WebSearchToolResultErrorCode errorCode`

### Web Search Tool Result Error Code

- `WebSearchToolResultErrorCode`

  - `"invalid_tool_input"`

  - `"unavailable"`

  - `"max_uses_exceeded"`

  - `"too_many_requests"`

  - `"query_too_long"`

  - `"request_too_large"`

## Messages › Batches

### Create a Message Batch

`$client->messages->batches->create(list<Request> requests, ?string userProfileID, ?string workspaceID): MessageBatch`

**POST** `/v1/messages/batches`

Send a batch of Message creation requests.

The Message Batches API can be used to process multiple Messages API requests at once. Once a Message Batch is created, it begins processing immediately. Batches can take up to 24 hours to complete.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

#### Parameters

- `requests: list<Request>`

  List of requests for prompt completion. Each is an individual request to create a Message.

- `userProfileID?:optional string`

  The user profile ID to attribute the requests in this batch to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header. Applies to every request in the batch; an individual request whose `user_profile_id` body field conflicts with this header is errored.

- `workspaceID?:optional string`

#### Returns

- `MessageBatch`

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

$messageBatch = $client->messages->batches->create(
  requests: [
    [
      'customID' => 'my-custom-id-1',
      'params' => [
        'maxTokens' => 1024,
        'messages' => [['content' => 'Hello, world', 'role' => 'user']],
        'model' => Model::CLAUDE_OPUS_5,
        'cacheControl' => ['type' => 'ephemeral', 'ttl' => '5m'],
        'container' => [
          'id' => 'id',
          'skills' => [
            ['skillID' => 'pdf', 'type' => 'anthropic', 'version' => 'latest']
          ],
        ],
        'inferenceGeo' => 'inference_geo',
        'metadata' => ['userID' => '13803d75-b4b5-4c3e-b2a2-6f21399b021b'],
        'outputConfig' => [
          'effort' => 'low',
          'format' => ['schema' => ['foo' => 'bar'], 'type' => 'json_schema'],
        ],
        'serviceTier' => 'auto',
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
        'thinking' => ['type' => 'adaptive', 'display' => 'summarized'],
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
  userProfileID: 'anthropic-user-profile-id',
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($messageBatch);
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

`$client->messages->batches->retrieve(string messageBatchID, ?string workspaceID): MessageBatch`

**GET** `/v1/messages/batches/{message_batch_id}`

This endpoint is idempotent and can be used to poll for Message Batch completion. To access the results of a Message Batch, make a request to the `results_url` field in the response.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

#### Parameters

- `messageBatchID: string`

  ID of the Message Batch.

- `workspaceID?:optional string`

#### Returns

- `MessageBatch`

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

$messageBatch = $client->messages->batches->retrieve(
  'message_batch_id', workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy'
);

var_dump($messageBatch);
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

`$client->messages->batches->list(?string afterID, ?string beforeID, ?int limit, ?string workspaceID): Page<MessageBatch>`

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

- `workspaceID?:optional string`

#### Returns

- `MessageBatch`

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

$page = $client->messages->batches->list(
  afterID: 'after_id',
  beforeID: 'before_id',
  limit: 1,
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

`$client->messages->batches->cancel(string messageBatchID, ?string workspaceID): MessageBatch`

**POST** `/v1/messages/batches/{message_batch_id}/cancel`

Batches may be canceled any time before processing ends. Once cancellation is initiated, the batch enters a `canceling` state, at which time the system may complete any in-progress, non-interruptible requests before finalizing cancellation.

The number of canceled requests is specified in `request_counts`. To determine which requests were canceled, check the individual results within the batch. Note that cancellation may not result in any canceled requests if they were non-interruptible.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

#### Parameters

- `messageBatchID: string`

  ID of the Message Batch.

- `workspaceID?:optional string`

#### Returns

- `MessageBatch`

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

$messageBatch = $client->messages->batches->cancel(
  'message_batch_id', workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy'
);

var_dump($messageBatch);
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

`$client->messages->batches->delete(string messageBatchID, ?string workspaceID): DeletedMessageBatch`

**DELETE** `/v1/messages/batches/{message_batch_id}`

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

#### Parameters

- `messageBatchID: string`

  ID of the Message Batch.

- `workspaceID?:optional string`

#### Returns

- `DeletedMessageBatch`

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

$deletedMessageBatch = $client->messages->batches->delete(
  'message_batch_id', workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy'
);

var_dump($deletedMessageBatch);
```

##### Response (200)

```json
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "type": "message_batch_deleted"
}
```

### Retrieve Message Batch results

`$client->messages->batches->results(string messageBatchID, ?string workspaceID): MessageBatchIndividualResponse`

**GET** `/v1/messages/batches/{message_batch_id}/results`

Streams the results of a Message Batch as a `.jsonl` file.

Each line in the file is a JSON object containing the result of a single request in the Message Batch. Results are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

#### Parameters

- `messageBatchID: string`

  ID of the Message Batch.

- `workspaceID?:optional string`

#### Returns

- `MessageBatchIndividualResponse`

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

$messageBatchIndividualResponse = $client->messages->batches->resultsStream(
  'message_batch_id', workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy'
);

var_dump($messageBatchIndividualResponse);
```
