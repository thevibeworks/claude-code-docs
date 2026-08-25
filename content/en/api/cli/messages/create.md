# Create a Message

`$ ant messages create`

**POST** `/v1/messages`

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

The Messages API can be used for either single queries or stateless multi-turn conversations.

Learn more about the Messages API in our [user guide](https://platform.claude.com/docs/en/get-started)

## Parameters

- `--max-tokens: number`

  Body param: The maximum number of tokens to generate before stopping.

  Note that our models may stop _before_ reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

  Set to `0` to populate the [prompt cache](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#pre-warming-the-cache) without generating a response.

  Different models have different maximum values for this parameter.  See [models](https://platform.claude.com/docs/en/about-claude/models/overview) for details.

  minimum: 0

- `--message: array of MessageParam`

  Body param: Input messages.

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

- `--model: "claude-sonnet-5" or "claude-fable-5" or "claude-mythos-5" or 12 more or string`

  Body param: The model that will complete your prompt.

  See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `--cache-control: optional object`

  Body param: Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

- `--container: optional ContainerParams or string`

  Body param: Container identifier for reuse across requests.

- `--inference-geo: optional string`

  Body param: Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

- `--metadata: optional object`

  Body param: An object describing metadata about the request.

- `--output-config: optional object`

  Body param: Configuration options for the model's output, such as the output format.

- `--service-tier: optional "auto" or "standard_only"`

  Body param: Determines whether to use priority capacity (if available) or standard capacity for this request.

  Anthropic offers different levels of service for your API requests. See [service-tiers](https://platform.claude.com/docs/en/api/service-tiers) for details.

- `--stop-sequence: optional array of string`

  Body param: Custom text sequences that will cause the model to stop generating.

  Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

  If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

- `--system: optional string or array of TextBlockParam`

  Body param: System prompt.

  A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role).

- `--thinking: optional ThinkingConfigEnabled or ThinkingConfigDisabled or ThinkingConfigAdaptive`

  Body param: Configuration for enabling Claude's extended thinking.

  When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

  See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

- `--tool-choice: optional ToolChoiceAuto or ToolChoiceAny or ToolChoiceTool or ToolChoiceNone`

  Body param: How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

- `--tool: optional array of ToolUnion`

  Body param: Definitions of tools that the model may use.

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

- `--user-profile-id: optional string`

  Header param: The user profile ID to attribute this request to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header.

- `--temperature: optional number`

  **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not support setting temperature. A value of 1.0 of will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

  Body param: Amount of randomness injected into the response.

  Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

  Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

  maximum: 1, minimum: 0

- `--top-k: optional number`

  **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not accept top_k; any value will be rejected with a 400 error.

  Body param: Only sample from the top K options for each subsequent token.

  Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

  Recommended for advanced use cases only.

  minimum: 0

- `--top-p: optional number`

  **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not support setting top_p. A value >= 0.99 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

  Body param: Use nucleus sampling.

  In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.

  Recommended for advanced use cases only.

  maximum: 1, minimum: 0

## Returns

- `message: object`

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `container: object`

    Information about the container used in the request (for the code execution tool)

    - `id: string`

      Identifier for the container used in this request

    - `expires_at: string`

      The time at which the container will expire.

      format: date-time

    - `skills: array of ContainerSkill`

      Skills loaded in the container

      - `skill_id: string`

        Skill ID

        maxLength: 64, minLength: 1

      - `type: "anthropic" or "custom"`

        Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

        - `"anthropic"`

        - `"custom"`

      - `version: string`

        The resolved version: a skill version ID for custom skills.

        maxLength: 64, minLength: 1

  - `content: array of ContentBlock`

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

    - `text_block: object`

      - `citations: array of TextCitation`

        Citations supporting the text block.

        The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

        - `citation_char_location: object`

          - `cited_text: string`

          - `document_index: number`

            minimum: 0

          - `document_title: string`

          - `end_char_index: number`

          - `file_id: string`

          - `start_char_index: number`

            minimum: 0

          - `type: "char_location"`

        - `citation_page_location: object`

          - `cited_text: string`

          - `document_index: number`

            minimum: 0

          - `document_title: string`

          - `end_page_number: number`

          - `file_id: string`

          - `start_page_number: number`

            minimum: 1

          - `type: "page_location"`

        - `citation_content_block_location: object`

          - `cited_text: string`

            The full text of the cited block range, concatenated.

            Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

          - `document_index: number`

            minimum: 0

          - `document_title: string`

          - `end_block_index: number`

            Exclusive 0-based end index of the cited block range in the source's `content` array.

            Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

          - `file_id: string`

          - `start_block_index: number`

            0-based index of the first cited block in the source's `content` array.

            minimum: 0

          - `type: "content_block_location"`

        - `citations_web_search_result_location: object`

          - `cited_text: string`

          - `encrypted_index: string`

          - `title: string`

            maxLength: 512

          - `type: "web_search_result_location"`

          - `url: string`

        - `citations_search_result_location: object`

          - `cited_text: string`

            The full text of the cited block range, concatenated.

            Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

          - `end_block_index: number`

            Exclusive 0-based end index of the cited block range in the source's `content` array.

            Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

          - `search_result_index: number`

            0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

            Counted separately from `document_index`; server-side web search results are not included in this count.

            minimum: 0

          - `source: string`

          - `start_block_index: number`

            0-based index of the first cited block in the source's `content` array.

            minimum: 0

          - `title: string`

          - `type: "search_result_location"`

      - `text: string`

        maxLength: 5000000, minLength: 0

      - `type: "text"`

    - `thinking_block: object`

      - `signature: string`

        A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

        This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

        See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

      - `thinking: string`

        The text of Claude's thinking process for this block.

      - `type: "thinking"`

    - `redacted_thinking_block: object`

      - `data: string`

        The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

        Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

        See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

      - `type: "redacted_thinking"`

    - `tool_use_block: object`

      - `id: string`

        pattern: ^[a-zA-Z0-9_-]+$

      - `caller: DirectCaller or ServerToolCaller or ServerToolCaller20260120`

        Tool invocation directly from the model.

        - `direct_caller: object`

          Tool invocation directly from the model.

          - `type: "direct"`

        - `server_tool_caller: object`

          Tool invocation generated by a server-side tool.

          - `tool_id: string`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `type: "code_execution_20250825"`

        - `server_tool_caller_20260120: object`

          - `tool_id: string`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `type: "code_execution_20260120"`

      - `input: map[unknown]`

      - `name: string`

        minLength: 1

      - `type: "tool_use"`

      - `toolset_name: optional string`

        For a toolset member tool_use, the toolset family.

        maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

    - `server_tool_use_block: object`

      - `id: string`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `caller: DirectCaller or ServerToolCaller or ServerToolCaller20260120`

        Tool invocation directly from the model.

        - `direct_caller: object`

          Tool invocation directly from the model.

        - `server_tool_caller: object`

          Tool invocation generated by a server-side tool.

        - `server_tool_caller_20260120: object`

      - `input: map[unknown]`

      - `name: "web_search" or "web_fetch" or "code_execution" or 4 more`

        - `"web_search"`

        - `"web_fetch"`

        - `"code_execution"`

        - `"bash_code_execution"`

        - `"text_editor_code_execution"`

        - `"tool_search_tool_regex"`

        - `"tool_search_tool_bm25"`

      - `type: "server_tool_use"`

    - `web_search_tool_result_block: object`

      - `caller: DirectCaller or ServerToolCaller or ServerToolCaller20260120`

        Tool invocation directly from the model.

        - `direct_caller: object`

          Tool invocation directly from the model.

        - `server_tool_caller: object`

          Tool invocation generated by a server-side tool.

        - `server_tool_caller_20260120: object`

      - `content: WebSearchToolResultError or array of WebSearchResultBlock`

        - `web_search_tool_result_error: object`

          - `error_code: "invalid_tool_input" or "unavailable" or "max_uses_exceeded" or 3 more`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"max_uses_exceeded"`

            - `"too_many_requests"`

            - `"query_too_long"`

            - `"request_too_large"`

          - `type: "web_search_tool_result_error"`

        - `union_member_1: array of WebSearchResultBlock`

          - `encrypted_content: string`

          - `page_age: string`

          - `title: string`

          - `type: "web_search_result"`

          - `url: string`

      - `tool_use_id: string`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `type: "web_search_tool_result"`

    - `web_fetch_tool_result_block: object`

      - `caller: DirectCaller or ServerToolCaller or ServerToolCaller20260120`

        Tool invocation directly from the model.

        - `direct_caller: object`

          Tool invocation directly from the model.

        - `server_tool_caller: object`

          Tool invocation generated by a server-side tool.

        - `server_tool_caller_20260120: object`

      - `content: WebFetchToolResultErrorBlock or WebFetchBlock`

        - `web_fetch_tool_result_error_block: object`

          - `error_code: "invalid_tool_input" or "url_too_long" or "url_not_allowed" or 6 more`

            - `"invalid_tool_input"`

            - `"url_too_long"`

            - `"url_not_allowed"`

            - `"url_not_in_prior_context"`

            - `"url_not_accessible"`

            - `"unsupported_content_type"`

            - `"too_many_requests"`

            - `"max_uses_exceeded"`

            - `"unavailable"`

          - `type: "web_fetch_tool_result_error"`

        - `web_fetch_block: object`

          - `content: object`

            - `citations: object`

              Citation configuration for the document

              - `enabled: boolean`

            - `source: Base64PDFSource or PlainTextSource`

              - `base64_pdf_source: object`

                - `data: string`

                  format: byte

                - `media_type: "application/pdf"`

                - `type: "base64"`

              - `plain_text_source: object`

                - `data: string`

                - `media_type: "text/plain"`

                - `type: "text"`

            - `title: string`

              The title of the document

            - `type: "document"`

          - `retrieved_at: string`

            ISO 8601 timestamp when the content was retrieved

          - `type: "web_fetch_result"`

          - `url: string`

            Fetched content URL

      - `tool_use_id: string`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `type: "web_fetch_tool_result"`

    - `code_execution_tool_result_block: object`

      - `content: CodeExecutionToolResultError or CodeExecutionResultBlock or EncryptedCodeExecutionResultBlock`

        Code execution result with encrypted stdout for PFC + web_search results.

        - `code_execution_tool_result_error: object`

          - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"too_many_requests"`

            - `"execution_time_exceeded"`

          - `type: "code_execution_tool_result_error"`

        - `code_execution_result_block: object`

          - `content: array of CodeExecutionOutputBlock`

            - `file_id: string`

            - `type: "code_execution_output"`

          - `return_code: number`

          - `stderr: string`

          - `stdout: string`

          - `type: "code_execution_result"`

        - `encrypted_code_execution_result_block: object`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `content: array of CodeExecutionOutputBlock`

            - `file_id: string`

            - `type: "code_execution_output"`

          - `encrypted_stdout: string`

          - `return_code: number`

          - `stderr: string`

          - `type: "encrypted_code_execution_result"`

      - `tool_use_id: string`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `type: "code_execution_tool_result"`

    - `bash_code_execution_tool_result_block: object`

      - `content: BashCodeExecutionToolResultError or BashCodeExecutionResultBlock`

        - `bash_code_execution_tool_result_error: object`

          - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"too_many_requests"`

            - `"execution_time_exceeded"`

            - `"output_file_too_large"`

          - `type: "bash_code_execution_tool_result_error"`

        - `bash_code_execution_result_block: object`

          - `content: array of BashCodeExecutionOutputBlock`

            - `file_id: string`

            - `type: "bash_code_execution_output"`

          - `return_code: number`

          - `stderr: string`

          - `stdout: string`

          - `type: "bash_code_execution_result"`

      - `tool_use_id: string`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `type: "bash_code_execution_tool_result"`

    - `text_editor_code_execution_tool_result_block: object`

      - `content: TextEditorCodeExecutionToolResultError or TextEditorCodeExecutionViewResultBlock or TextEditorCodeExecutionCreateResultBlock or TextEditorCodeExecutionStrReplaceResultBlock`

        - `text_editor_code_execution_tool_result_error: object`

          - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"too_many_requests"`

            - `"execution_time_exceeded"`

            - `"file_not_found"`

          - `error_message: string`

          - `type: "text_editor_code_execution_tool_result_error"`

        - `text_editor_code_execution_view_result_block: object`

          - `content: string`

          - `file_type: "text" or "image" or "pdf"`

            - `"text"`

            - `"image"`

            - `"pdf"`

          - `num_lines: number`

          - `start_line: number`

          - `total_lines: number`

          - `type: "text_editor_code_execution_view_result"`

        - `text_editor_code_execution_create_result_block: object`

          - `is_file_update: boolean`

          - `type: "text_editor_code_execution_create_result"`

        - `text_editor_code_execution_str_replace_result_block: object`

          - `lines: array of string`

          - `new_lines: number`

          - `new_start: number`

          - `old_lines: number`

          - `old_start: number`

          - `type: "text_editor_code_execution_str_replace_result"`

      - `tool_use_id: string`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `type: "text_editor_code_execution_tool_result"`

    - `tool_search_tool_result_block: object`

      - `content: ToolSearchToolResultError or ToolSearchToolSearchResultBlock`

        - `tool_search_tool_result_error: object`

          - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"too_many_requests"`

            - `"execution_time_exceeded"`

          - `error_message: string`

          - `type: "tool_search_tool_result_error"`

        - `tool_search_tool_search_result_block: object`

          - `tool_references: array of ToolReferenceBlock`

            - `tool_name: string`

              maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

            - `type: "tool_reference"`

          - `type: "tool_search_tool_search_result"`

      - `tool_use_id: string`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `type: "tool_search_tool_result"`

    - `container_upload_block: object`

      Response model for a file uploaded to the container.

      - `file_id: string`

      - `type: "container_upload"`

  - `model: "claude-sonnet-5" or "claude-fable-5" or "claude-mythos-5" or 12 more or string`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

  - `role: "assistant"`

    Conversational role of the generated message.

    This will always be `"assistant"`.

  - `stop_details: object`

    Structured information about a refusal.

    - `category: "cyber" or "bio" or "frontier_llm" or 2 more`

      The policy category that triggered a refusal.

      - `"cyber"`

        The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.

      - `"bio"`

        The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.

      - `"frontier_llm"`

        The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.

      - `"reasoning_extraction"`

        The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).

      - `"general_harms"`

        The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.

    - `explanation: string`

      Human-readable explanation of the refusal.

      This text is not guaranteed to be stable. `null` when no explanation is available for the category.

    - `type: "refusal"`

  - `stop_reason: "end_turn" or "max_tokens" or "stop_sequence" or 4 more`

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

    - `"end_turn"`

    - `"max_tokens"`

    - `"stop_sequence"`

    - `"tool_use"`

    - `"pause_turn"`

    - `"refusal"`

    - `"model_context_window_exceeded"`

  - `stop_sequence: string`

    Which custom stop sequence was generated, if any.

    This value will be a non-null string if one of your custom stop sequences was generated.

  - `type: "message"`

    Object type.

    For Messages, this is always `"message"`.

  - `usage: object`

    Billing and rate-limit usage.

    Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

    Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

    For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

    Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

    - `cache_creation: object`

      Breakdown of cached tokens by TTL

      - `ephemeral_1h_input_tokens: number`

        The number of input tokens used to create the 1 hour cache entry.

        minimum: 0

      - `ephemeral_5m_input_tokens: number`

        The number of input tokens used to create the 5 minute cache entry.

        minimum: 0

    - `cache_creation_input_tokens: number`

      The number of input tokens used to create the cache entry.

      minimum: 0

    - `cache_read_input_tokens: number`

      The number of input tokens read from the cache.

      minimum: 0

    - `inference_geo: string`

      The geographic region where inference was performed for this request.

    - `input_tokens: number`

      The number of input tokens which were used.

      minimum: 0

    - `output_tokens: number`

      The number of output tokens which were used.

      minimum: 0

    - `output_tokens_details: object`

      Breakdown of output tokens by category.

      `output_tokens` remains the inclusive, authoritative total used for billing.
      This object provides a read-only decomposition for observability — for example,
      how many of the billed output tokens were spent on internal reasoning that may
      have been summarized before being returned to you.

      - `thinking_tokens: number`

        Number of output tokens the model generated as internal reasoning, including
        the thinking-block delimiter tokens.

        Reflects the raw reasoning the model produced, not the (possibly shorter)
        summarized thinking text returned in the response body. Computed by
        re-tokenizing the raw reasoning text, so it may differ from the model's exact
        generation count by a small number of tokens. Always ≤ `output_tokens`;
        `output_tokens - thinking_tokens` approximates the non-reasoning output.

        minimum: 0

    - `server_tool_use: object`

      The number of server tool requests.

      - `web_fetch_requests: number`

        The number of web fetch tool requests.

        minimum: 0

      - `web_search_requests: number`

        The number of web search tool requests.

        minimum: 0

    - `service_tier: "standard" or "priority" or "batch"`

      If the request used the priority, standard, or batch tier.

      - `"standard"`

      - `"priority"`

      - `"batch"`

- `raw_message_stream_event: RawMessageStartEvent or RawMessageDeltaEvent or RawMessageStopEvent or 3 more`

  - `raw_message_start_event: object`

    - `message: object`

      - `id: string`

        Unique object identifier.

        The format and length of IDs may change over time.

      - `container: object`

        Information about the container used in the request (for the code execution tool)

      - `content: array of ContentBlock`

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

      - `model: "claude-sonnet-5" or "claude-fable-5" or "claude-mythos-5" or 12 more or string`

        The model that will complete your prompt.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `role: "assistant"`

        Conversational role of the generated message.

        This will always be `"assistant"`.

      - `stop_details: object`

        Structured information about a refusal.

      - `stop_reason: "end_turn" or "max_tokens" or "stop_sequence" or 4 more`

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

      - `stop_sequence: string`

        Which custom stop sequence was generated, if any.

        This value will be a non-null string if one of your custom stop sequences was generated.

      - `type: "message"`

        Object type.

        For Messages, this is always `"message"`.

      - `usage: object`

        Billing and rate-limit usage.

        Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

        Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

        For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

        Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

    - `type: "message_start"`

  - `raw_message_delta_event: object`

    - `delta: object`

      - `container: object`

        Information about the container used in the request (for the code execution tool)

        - `id: string`

          Identifier for the container used in this request

        - `expires_at: string`

          The time at which the container will expire.

          format: date-time

        - `skills: array of ContainerSkill`

          Skills loaded in the container

      - `stop_details: object`

        Structured information about a refusal.

        - `category: "cyber" or "bio" or "frontier_llm" or 2 more`

          The policy category that triggered a refusal.

        - `explanation: string`

          Human-readable explanation of the refusal.

          This text is not guaranteed to be stable. `null` when no explanation is available for the category.

        - `type: "refusal"`

      - `stop_reason: "end_turn" or "max_tokens" or "stop_sequence" or 4 more`

        - `"end_turn"`

        - `"max_tokens"`

        - `"stop_sequence"`

        - `"tool_use"`

        - `"pause_turn"`

        - `"refusal"`

        - `"model_context_window_exceeded"`

      - `stop_sequence: string`

    - `type: "message_delta"`

    - `usage: object`

      Billing and rate-limit usage.

      Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

      Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

      For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

      Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

      - `cache_creation_input_tokens: number`

        The cumulative number of input tokens used to create the cache entry.

        minimum: 0

      - `cache_read_input_tokens: number`

        The cumulative number of input tokens read from the cache.

        minimum: 0

      - `input_tokens: number`

        The cumulative number of input tokens which were used.

        minimum: 0

      - `output_tokens: number`

        The cumulative number of output tokens which were used.

      - `output_tokens_details: object`

        Breakdown of output tokens by category.

        `output_tokens` remains the inclusive, authoritative total used for billing.
        This object provides a read-only decomposition for observability — for example,
        how many of the billed output tokens were spent on internal reasoning that may
        have been summarized before being returned to you.

        - `thinking_tokens: number`

          Number of output tokens the model generated as internal reasoning, including
          the thinking-block delimiter tokens.

          Reflects the raw reasoning the model produced, not the (possibly shorter)
          summarized thinking text returned in the response body. Computed by
          re-tokenizing the raw reasoning text, so it may differ from the model's exact
          generation count by a small number of tokens. Always ≤ `output_tokens`;
          `output_tokens - thinking_tokens` approximates the non-reasoning output.

          minimum: 0

      - `server_tool_use: object`

        The number of server tool requests.

        - `web_fetch_requests: number`

          The number of web fetch tool requests.

          minimum: 0

        - `web_search_requests: number`

          The number of web search tool requests.

          minimum: 0

  - `raw_message_stop_event: object`

    - `type: "message_stop"`

  - `raw_content_block_start_event: object`

    - `content_block: TextBlock or ThinkingBlock or RedactedThinkingBlock or 9 more`

      Response model for a file uploaded to the container.

      - `text_block: object`

        - `citations: array of TextCitation`

          Citations supporting the text block.

          The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

        - `text: string`

          maxLength: 5000000, minLength: 0

        - `type: "text"`

      - `thinking_block: object`

        - `signature: string`

          A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

          This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

          See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

        - `thinking: string`

          The text of Claude's thinking process for this block.

        - `type: "thinking"`

      - `redacted_thinking_block: object`

        - `data: string`

          The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

          Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

          See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

        - `type: "redacted_thinking"`

      - `tool_use_block: object`

        - `id: string`

          pattern: ^[a-zA-Z0-9_-]+$

        - `caller: DirectCaller or ServerToolCaller or ServerToolCaller20260120`

          Tool invocation directly from the model.

        - `input: map[unknown]`

        - `name: string`

          minLength: 1

        - `type: "tool_use"`

        - `toolset_name: optional string`

          For a toolset member tool_use, the toolset family.

          maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

      - `server_tool_use_block: object`

        - `id: string`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `caller: DirectCaller or ServerToolCaller or ServerToolCaller20260120`

          Tool invocation directly from the model.

        - `input: map[unknown]`

        - `name: "web_search" or "web_fetch" or "code_execution" or 4 more`

        - `type: "server_tool_use"`

      - `web_search_tool_result_block: object`

        - `caller: DirectCaller or ServerToolCaller or ServerToolCaller20260120`

          Tool invocation directly from the model.

        - `content: WebSearchToolResultError or array of WebSearchResultBlock`

        - `tool_use_id: string`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `type: "web_search_tool_result"`

      - `web_fetch_tool_result_block: object`

        - `caller: DirectCaller or ServerToolCaller or ServerToolCaller20260120`

          Tool invocation directly from the model.

        - `content: WebFetchToolResultErrorBlock or WebFetchBlock`

        - `tool_use_id: string`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `type: "web_fetch_tool_result"`

      - `code_execution_tool_result_block: object`

        - `content: CodeExecutionToolResultError or CodeExecutionResultBlock or EncryptedCodeExecutionResultBlock`

          Code execution result with encrypted stdout for PFC + web_search results.

        - `tool_use_id: string`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `type: "code_execution_tool_result"`

      - `bash_code_execution_tool_result_block: object`

        - `content: BashCodeExecutionToolResultError or BashCodeExecutionResultBlock`

        - `tool_use_id: string`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `type: "bash_code_execution_tool_result"`

      - `text_editor_code_execution_tool_result_block: object`

        - `content: TextEditorCodeExecutionToolResultError or TextEditorCodeExecutionViewResultBlock or TextEditorCodeExecutionCreateResultBlock or TextEditorCodeExecutionStrReplaceResultBlock`

        - `tool_use_id: string`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `type: "text_editor_code_execution_tool_result"`

      - `tool_search_tool_result_block: object`

        - `content: ToolSearchToolResultError or ToolSearchToolSearchResultBlock`

        - `tool_use_id: string`

          pattern: ^srvtoolu_[a-zA-Z0-9_]+$

        - `type: "tool_search_tool_result"`

      - `container_upload_block: object`

        Response model for a file uploaded to the container.

        - `file_id: string`

        - `type: "container_upload"`

    - `index: number`

    - `type: "content_block_start"`

  - `raw_content_block_delta_event: object`

    - `delta: TextDelta or InputJSONDelta or CitationsDelta or 2 more`

      - `text_delta: object`

        - `text: string`

        - `type: "text_delta"`

      - `input_json_delta: object`

        - `partial_json: string`

        - `type: "input_json_delta"`

      - `citations_delta: object`

        - `citation: CitationCharLocation or CitationPageLocation or CitationContentBlockLocation or 2 more`

          - `citation_char_location: object`

            - `cited_text: string`

            - `document_index: number`

              minimum: 0

            - `document_title: string`

            - `end_char_index: number`

            - `file_id: string`

            - `start_char_index: number`

              minimum: 0

            - `type: "char_location"`

          - `citation_page_location: object`

            - `cited_text: string`

            - `document_index: number`

              minimum: 0

            - `document_title: string`

            - `end_page_number: number`

            - `file_id: string`

            - `start_page_number: number`

              minimum: 1

            - `type: "page_location"`

          - `citation_content_block_location: object`

            - `cited_text: string`

              The full text of the cited block range, concatenated.

              Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

            - `document_index: number`

              minimum: 0

            - `document_title: string`

            - `end_block_index: number`

              Exclusive 0-based end index of the cited block range in the source's `content` array.

              Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

            - `file_id: string`

            - `start_block_index: number`

              0-based index of the first cited block in the source's `content` array.

              minimum: 0

            - `type: "content_block_location"`

          - `citations_web_search_result_location: object`

            - `cited_text: string`

            - `encrypted_index: string`

            - `title: string`

              maxLength: 512

            - `type: "web_search_result_location"`

            - `url: string`

          - `citations_search_result_location: object`

            - `cited_text: string`

              The full text of the cited block range, concatenated.

              Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

            - `end_block_index: number`

              Exclusive 0-based end index of the cited block range in the source's `content` array.

              Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

            - `search_result_index: number`

              0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

              Counted separately from `document_index`; server-side web search results are not included in this count.

              minimum: 0

            - `source: string`

            - `start_block_index: number`

              0-based index of the first cited block in the source's `content` array.

              minimum: 0

            - `title: string`

            - `type: "search_result_location"`

        - `type: "citations_delta"`

      - `thinking_delta: object`

        - `thinking: string`

          The incremental `thinking` text for this content block. Concatenate the `thinking` values of successive `thinking_delta` events to assemble the block's full `thinking` value.

        - `type: "thinking_delta"`

      - `signature_delta: object`

        - `signature: string`

          The `signature` for this thinking block: an opaque value used to verify that the block was generated by Claude when it is passed back to the API. Delivered in a `signature_delta` event just before the block's `content_block_stop` event.

        - `type: "signature_delta"`

    - `index: number`

    - `type: "content_block_delta"`

  - `raw_content_block_stop_event: object`

    - `index: number`

    - `type: "content_block_stop"`

## Example

```bash
ant messages create \
  --api-key my-anthropic-api-key \
  --max-tokens 1024 \
  --message '{content: [{text: x, type: text}], role: user}' \
  --model claude-opus-5
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
