# Messages

## Create a Message

`$ ant messages create`

**POST** `/v1/messages`

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

The Messages API can be used for either single queries or stateless multi-turn conversations.

Learn more about the Messages API in our [user guide](https://platform.claude.com/docs/en/get-started)

### Parameters

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

- `--model: "claude-fable-5-1" or "claude-mythos-5-1" or "claude-sonnet-5" or 14 more or string`

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

### Returns

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

  - `model: "claude-fable-5-1" or "claude-mythos-5-1" or "claude-sonnet-5" or 14 more or string`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

      - `model: "claude-fable-5-1" or "claude-mythos-5-1" or "claude-sonnet-5" or 14 more or string`

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

### Example

```bash
ant messages create \
  --api-key my-anthropic-api-key \
  --max-tokens 1024 \
  --message '{content: [{text: x, type: text}], role: user}' \
  --model claude-opus-5
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

`$ ant messages count-tokens`

**POST** `/v1/messages/count_tokens`

Count the number of tokens in a Message.

The Token Count API can be used to count the number of tokens in a Message, including tools, images, and documents, without creating it.

Learn more about token counting in our [user guide](https://platform.claude.com/docs/en/build-with-claude/token-counting)

### Parameters

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

- `--model: "claude-fable-5-1" or "claude-mythos-5-1" or "claude-sonnet-5" or 14 more or string`

  Body param: The model that will complete your prompt.

  See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `--cache-control: optional object`

  Body param: Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

- `--output-config: optional object`

  Body param: Configuration options for the model's output, such as the output format.

- `--system: optional string or array of TextBlockParam`

  Body param: System prompt.

  A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role).

- `--thinking: optional ThinkingConfigEnabled or ThinkingConfigDisabled or ThinkingConfigAdaptive`

  Body param: Configuration for enabling Claude's extended thinking.

  When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

  See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

- `--tool-choice: optional ToolChoiceAuto or ToolChoiceAny or ToolChoiceTool or ToolChoiceNone`

  Body param: How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

- `--tool: optional array of MessageCountTokensTool`

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

### Returns

- `message_tokens_count: object`

  - `input_tokens: number`

    The total number of tokens across the provided list of messages, system prompt, and tools.

### Example

```bash
ant messages count-tokens \
  --api-key my-anthropic-api-key \
  --message '{content: [{text: x, type: text}], role: user}' \
  --model claude-opus-5
```

#### Response (200)

```json
{
  "input_tokens": 2095
}
```

## Domain types

### Base64 Image Source

- `base64_image_source: object`

  - `data: string`

    format: byte

  - `media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"`

    - `"image/jpeg"`

    - `"image/png"`

    - `"image/gif"`

    - `"image/webp"`

  - `type: "base64"`

### Base64 PDF Source

- `base64_pdf_source: object`

  - `data: string`

    format: byte

  - `media_type: "application/pdf"`

  - `type: "base64"`

### Bash Code Execution Output Block

- `bash_code_execution_output_block: object`

  - `file_id: string`

  - `type: "bash_code_execution_output"`

### Bash Code Execution Output Block Param

- `bash_code_execution_output_block_param: object`

  - `file_id: string`

  - `type: "bash_code_execution_output"`

### Bash Code Execution Result Block

- `bash_code_execution_result_block: object`

  - `content: array of BashCodeExecutionOutputBlock`

    - `file_id: string`

    - `type: "bash_code_execution_output"`

  - `return_code: number`

  - `stderr: string`

  - `stdout: string`

  - `type: "bash_code_execution_result"`

### Bash Code Execution Result Block Param

- `bash_code_execution_result_block_param: object`

  - `content: array of BashCodeExecutionOutputBlockParam`

    - `file_id: string`

    - `type: "bash_code_execution_output"`

  - `return_code: number`

  - `stderr: string`

  - `stdout: string`

  - `type: "bash_code_execution_result"`

### Bash Code Execution Tool Result Block

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

### Bash Code Execution Tool Result Block Param

- `bash_code_execution_tool_result_block_param: object`

  - `content: BashCodeExecutionToolResultErrorParam or BashCodeExecutionResultBlockParam`

    - `bash_code_execution_tool_result_error_param: object`

      - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

        - `"invalid_tool_input"`

        - `"unavailable"`

        - `"too_many_requests"`

        - `"execution_time_exceeded"`

        - `"output_file_too_large"`

      - `type: "bash_code_execution_tool_result_error"`

    - `bash_code_execution_result_block_param: object`

      - `content: array of BashCodeExecutionOutputBlockParam`

        - `file_id: string`

        - `type: "bash_code_execution_output"`

      - `return_code: number`

      - `stderr: string`

      - `stdout: string`

      - `type: "bash_code_execution_result"`

  - `tool_use_id: string`

    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

  - `type: "bash_code_execution_tool_result"`

  - `cache_control: optional object`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `"5m"`

      - `"1h"`

### Bash Code Execution Tool Result Error

- `bash_code_execution_tool_result_error: object`

  - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

    - `"invalid_tool_input"`

    - `"unavailable"`

    - `"too_many_requests"`

    - `"execution_time_exceeded"`

    - `"output_file_too_large"`

  - `type: "bash_code_execution_tool_result_error"`

### Bash Code Execution Tool Result Error Code

- `bash_code_execution_tool_result_error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

  - `"invalid_tool_input"`

  - `"unavailable"`

  - `"too_many_requests"`

  - `"execution_time_exceeded"`

  - `"output_file_too_large"`

### Bash Code Execution Tool Result Error Param

- `bash_code_execution_tool_result_error_param: object`

  - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

    - `"invalid_tool_input"`

    - `"unavailable"`

    - `"too_many_requests"`

    - `"execution_time_exceeded"`

    - `"output_file_too_large"`

  - `type: "bash_code_execution_tool_result_error"`

### Browser Close Tab Config

- `browser_close_tab_config: object`

  `close_tab`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Double Click Config

- `browser_double_click_config: object`

  `double_click`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser File Upload Config

- `browser_file_upload_config: object`

  `file_upload`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Find Config

- `browser_find_config: object`

  `find`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Form Input Config

- `browser_form_input_config: object`

  `form_input`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Get Page Text Config

- `browser_get_page_text_config: object`

  `get_page_text`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Hold Key Config

- `browser_hold_key_config: object`

  `hold_key`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Hover Config

- `browser_hover_config: object`

  `hover`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Javascript Exec Config

- `browser_javascript_exec_config: object`

  `javascript_exec`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Key Config

- `browser_key_config: object`

  `key`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Left Click Config

- `browser_left_click_config: object`

  `left_click`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Left Click Drag Config

- `browser_left_click_drag_config: object`

  `left_click_drag`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Left Mouse Down Config

- `browser_left_mouse_down_config: object`

  `left_mouse_down`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Left Mouse Up Config

- `browser_left_mouse_up_config: object`

  `left_mouse_up`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser List Tabs Config

- `browser_list_tabs_config: object`

  `list_tabs`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Middle Click Config

- `browser_middle_click_config: object`

  `middle_click`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Mouse Move Config

- `browser_mouse_move_config: object`

  `mouse_move`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Navigate Config

- `browser_navigate_config: object`

  `navigate`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser New Tab Config

- `browser_new_tab_config: object`

  `new_tab`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Read Console Config

- `browser_read_console_config: object`

  `read_console`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Read Network Config

- `browser_read_network_config: object`

  `read_network`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Read Page Config

- `browser_read_page_config: object`

  `read_page`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Right Click Config

- `browser_right_click_config: object`

  `right_click`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Screenshot Config

- `browser_screenshot_config: object`

  `screenshot`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Scroll Config

- `browser_scroll_config: object`

  `scroll`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Scroll To Config

- `browser_scroll_to_config: object`

  `scroll_to`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser State Block Param

- `browser_state_block_param: object`

  The caller's browser state after a browser toolset member call —
  the full inventory of open tabs, which tab is active, and any side
  effects (tabs opened, download state changes) the call produced.

  At most one per `tool_result`, only on a non-error result answering a
  browser toolset member `tool_use`. The server renders the
  model-visible text from it; the model never sees the raw fields.

  - `tabs: array of BrowserStateTabEntry`

    All tabs open in the browser after this call — the full inventory, not a delta. May be empty. Whenever non-empty, exactly one entry carries `active: true`.

    maxItems: 100

    - `tab_id: string`

      The caller-assigned identifier for this tab, unique within the inventory.

      maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

    - `title: string`

      The title of the page the tab is showing. May be empty.

      maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

    - `url: string`

      The URL of the page the tab is showing. May be empty.

      maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

    - `active: optional boolean`

      Whether this tab is the active tab after this call. Whenever `tabs` is non-empty, exactly one entry is marked `active: true`.

  - `type: "browser_state"`

  - `cache_control: optional object`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `"5m"`

      - `"1h"`

  - `state_changes: optional array of BrowserStateChange`

    Tabs opened and download state changes during this call. "Nothing to report" is expressed by omitting the field, never by an empty list.

    maxItems: 200, minItems: 1

    - `browser_state_change_tab_opened: object`

      A tab this call's execution opened that remains open at its end —
      the creation delta of the `tabs` inventory, not an event log.

      Carries only the `tab_id`; the tab's `title` and `url` live on its
      `tabs` entry, which must include the same `tab_id`. A tab opened
      during a failed call gets no deferred `tab_opened`; it simply appears
      in the next result's `tabs` inventory.

      - `tab_id: string`

        The `tab_id` of the opened tab, present in `tabs`.

        maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

      - `type: "tab_opened"`

    - `browser_state_change_download_started: object`

      A file download that started during this call.

      - `download_id: string`

        The caller-assigned identifier for this download, stable across the state changes reporting it.

        maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

      - `type: "download_started"`

      - `url: string`

        The final post-redirect URL the download was served from.

        maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

    - `browser_state_change_download_completed: object`

      A file download that finished during this call, reported with the
      same `download_id` as its `download_started` — or without a prior
      `download_started`, when the download finished during the call that
      started it (at most one state change per `download_id` per result).

      - `download_id: string`

        The caller-assigned identifier for this download, stable across the state changes reporting it.

        maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

      - `type: "download_completed"`

      - `url: string`

        The final post-redirect URL the download was served from.

        maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

      - `path: optional string`

        Where the executor saved the file, on the executor's filesystem. Only included when another tool in the same environment can read the file at that path.

        pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

      - `size_bytes: optional number`

        The completed download's size.

        minimum: 0

    - `browser_state_change_download_failed: object`

      A file download that failed — or was cancelled — during this call.

      - `download_id: string`

        The caller-assigned identifier for this download, stable across the state changes reporting it.

        maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

      - `type: "download_failed"`

      - `url: string`

        The final post-redirect URL the download was served from.

        maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

      - `error: optional string`

        The failure or cancellation detail, when known.

        pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

### Browser State Change

- `browser_state_change: BrowserStateChangeTabOpened or BrowserStateChangeDownloadStarted or BrowserStateChangeDownloadCompleted or BrowserStateChangeDownloadFailed`

  A tab this call's execution opened that remains open at its end —
  the creation delta of the `tabs` inventory, not an event log.

  Carries only the `tab_id`; the tab's `title` and `url` live on its
  `tabs` entry, which must include the same `tab_id`. A tab opened
  during a failed call gets no deferred `tab_opened`; it simply appears
  in the next result's `tabs` inventory.

  - `browser_state_change_tab_opened: object`

    A tab this call's execution opened that remains open at its end —
    the creation delta of the `tabs` inventory, not an event log.

    Carries only the `tab_id`; the tab's `title` and `url` live on its
    `tabs` entry, which must include the same `tab_id`. A tab opened
    during a failed call gets no deferred `tab_opened`; it simply appears
    in the next result's `tabs` inventory.

    - `tab_id: string`

      The `tab_id` of the opened tab, present in `tabs`.

      maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

    - `type: "tab_opened"`

  - `browser_state_change_download_started: object`

    A file download that started during this call.

    - `download_id: string`

      The caller-assigned identifier for this download, stable across the state changes reporting it.

      maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

    - `type: "download_started"`

    - `url: string`

      The final post-redirect URL the download was served from.

      maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

  - `browser_state_change_download_completed: object`

    A file download that finished during this call, reported with the
    same `download_id` as its `download_started` — or without a prior
    `download_started`, when the download finished during the call that
    started it (at most one state change per `download_id` per result).

    - `download_id: string`

      The caller-assigned identifier for this download, stable across the state changes reporting it.

      maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

    - `type: "download_completed"`

    - `url: string`

      The final post-redirect URL the download was served from.

      maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

    - `path: optional string`

      Where the executor saved the file, on the executor's filesystem. Only included when another tool in the same environment can read the file at that path.

      pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

    - `size_bytes: optional number`

      The completed download's size.

      minimum: 0

  - `browser_state_change_download_failed: object`

    A file download that failed — or was cancelled — during this call.

    - `download_id: string`

      The caller-assigned identifier for this download, stable across the state changes reporting it.

      maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

    - `type: "download_failed"`

    - `url: string`

      The final post-redirect URL the download was served from.

      maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

    - `error: optional string`

      The failure or cancellation detail, when known.

      pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

### Browser State Change Download Completed

- `browser_state_change_download_completed: object`

  A file download that finished during this call, reported with the
  same `download_id` as its `download_started` — or without a prior
  `download_started`, when the download finished during the call that
  started it (at most one state change per `download_id` per result).

  - `download_id: string`

    The caller-assigned identifier for this download, stable across the state changes reporting it.

    maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

  - `type: "download_completed"`

  - `url: string`

    The final post-redirect URL the download was served from.

    maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

  - `path: optional string`

    Where the executor saved the file, on the executor's filesystem. Only included when another tool in the same environment can read the file at that path.

    pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

  - `size_bytes: optional number`

    The completed download's size.

    minimum: 0

### Browser State Change Download Failed

- `browser_state_change_download_failed: object`

  A file download that failed — or was cancelled — during this call.

  - `download_id: string`

    The caller-assigned identifier for this download, stable across the state changes reporting it.

    maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

  - `type: "download_failed"`

  - `url: string`

    The final post-redirect URL the download was served from.

    maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

  - `error: optional string`

    The failure or cancellation detail, when known.

    pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

### Browser State Change Download Started

- `browser_state_change_download_started: object`

  A file download that started during this call.

  - `download_id: string`

    The caller-assigned identifier for this download, stable across the state changes reporting it.

    maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

  - `type: "download_started"`

  - `url: string`

    The final post-redirect URL the download was served from.

    maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

### Browser State Change Tab Opened

- `browser_state_change_tab_opened: object`

  A tab this call's execution opened that remains open at its end —
  the creation delta of the `tabs` inventory, not an event log.

  Carries only the `tab_id`; the tab's `title` and `url` live on its
  `tabs` entry, which must include the same `tab_id`. A tab opened
  during a failed call gets no deferred `tab_opened`; it simply appears
  in the next result's `tabs` inventory.

  - `tab_id: string`

    The `tab_id` of the opened tab, present in `tabs`.

    maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

  - `type: "tab_opened"`

### Browser State Tab Entry

- `browser_state_tab_entry: object`

  One open browser tab reported in a `browser_state` block's `tabs`
  inventory.

  `tab_id` is the caller-assigned identifier for the tab; `title` and
  `url` describe the page the tab is currently showing and may be empty
  strings (a blank tab legitimately has both empty). `active` marks the
  tab that is active after this call; whenever `tabs` is non-empty,
  exactly one entry is marked.

  - `tab_id: string`

    The caller-assigned identifier for this tab, unique within the inventory.

    maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

  - `title: string`

    The title of the page the tab is showing. May be empty.

    maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

  - `url: string`

    The URL of the page the tab is showing. May be empty.

    maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

  - `active: optional boolean`

    Whether this tab is the active tab after this call. Whenever `tabs` is non-empty, exactly one entry is marked `active: true`.

### Browser Switch Tab Config

- `browser_switch_tab_config: object`

  `switch_tab`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Toolset 20260801

- `browser_toolset_20260801: object`

  The browser toolset: a single `tools[]` entry (carrying no
  `name`) that declares the browser tool family. The model is served
  the family's tool with any members disabled via `configs` removed
  from its schema.

  - `type: "browser_toolset_20260801"`

  - `cache_control: optional object`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `"5m"`

      - `"1h"`

  - `configs: optional object`

    Per-member configuration for `browser_toolset_20260801`: one
    optional field per member tool, keyed by the member name — the same
    name the member's `tool_use` blocks carry. Every member is an
    accepted key, and a member's defaults apply wherever its key is
    absent. Unknown keys are rejected: the field set is this toolset
    version's complete member set.

    - `close_tab: optional object`

      `close_tab`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `double_click: optional object`

      `double_click`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `file_upload: optional object`

      `file_upload`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `find: optional object`

      `find`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `form_input: optional object`

      `form_input`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `get_page_text: optional object`

      `get_page_text`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `hold_key: optional object`

      `hold_key`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `hover: optional object`

      `hover`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `javascript_exec: optional object`

      `javascript_exec`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `key: optional object`

      `key`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `left_click: optional object`

      `left_click`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `left_click_drag: optional object`

      `left_click_drag`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `left_mouse_down: optional object`

      `left_mouse_down`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `left_mouse_up: optional object`

      `left_mouse_up`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `list_tabs: optional object`

      `list_tabs`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `middle_click: optional object`

      `middle_click`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `mouse_move: optional object`

      `mouse_move`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `navigate: optional object`

      `navigate`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `new_tab: optional object`

      `new_tab`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `read_console: optional object`

      `read_console`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `read_network: optional object`

      `read_network`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `read_page: optional object`

      `read_page`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `right_click: optional object`

      `right_click`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `screenshot: optional object`

      `screenshot`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `scroll: optional object`

      `scroll`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `scroll_to: optional object`

      `scroll_to`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `switch_tab: optional object`

      `switch_tab`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `triple_click: optional object`

      `triple_click`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `type: optional object`

      `type`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `wait: optional object`

      `wait`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `zoom: optional object`

      `zoom`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Toolset Configs

- `browser_toolset_configs: object`

  Per-member configuration for `browser_toolset_20260801`: one
  optional field per member tool, keyed by the member name — the same
  name the member's `tool_use` blocks carry. Every member is an
  accepted key, and a member's defaults apply wherever its key is
  absent. Unknown keys are rejected: the field set is this toolset
  version's complete member set.

  - `close_tab: optional object`

    `close_tab`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `double_click: optional object`

    `double_click`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `file_upload: optional object`

    `file_upload`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `find: optional object`

    `find`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `form_input: optional object`

    `form_input`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `get_page_text: optional object`

    `get_page_text`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `hold_key: optional object`

    `hold_key`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `hover: optional object`

    `hover`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `javascript_exec: optional object`

    `javascript_exec`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `key: optional object`

    `key`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `left_click: optional object`

    `left_click`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `left_click_drag: optional object`

    `left_click_drag`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `left_mouse_down: optional object`

    `left_mouse_down`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `left_mouse_up: optional object`

    `left_mouse_up`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `list_tabs: optional object`

    `list_tabs`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `middle_click: optional object`

    `middle_click`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `mouse_move: optional object`

    `mouse_move`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `navigate: optional object`

    `navigate`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `new_tab: optional object`

    `new_tab`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `read_console: optional object`

    `read_console`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `read_network: optional object`

    `read_network`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `read_page: optional object`

    `read_page`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `right_click: optional object`

    `right_click`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `screenshot: optional object`

    `screenshot`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `scroll: optional object`

    `scroll`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `scroll_to: optional object`

    `scroll_to`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `switch_tab: optional object`

    `switch_tab`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `triple_click: optional object`

    `triple_click`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `type: optional object`

    `type`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `wait: optional object`

    `wait`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `zoom: optional object`

    `zoom`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Triple Click Config

- `browser_triple_click_config: object`

  `triple_click`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Type Config

- `browser_type_config: object`

  `type`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Wait Config

- `browser_wait_config: object`

  `wait`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Browser Zoom Config

- `browser_zoom_config: object`

  `zoom`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Cache Control Ephemeral

- `cache_control_ephemeral: object`

  - `type: "ephemeral"`

  - `ttl: optional "5m" or "1h"`

    The time-to-live for the cache control breakpoint.

    This may be one the following values:

    - `5m`: 5 minutes
    - `1h`: 1 hour

    Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `"5m"`

    - `"1h"`

### Cache Creation

- `cache_creation: object`

  - `ephemeral_1h_input_tokens: number`

    The number of input tokens used to create the 1 hour cache entry.

    minimum: 0

  - `ephemeral_5m_input_tokens: number`

    The number of input tokens used to create the 5 minute cache entry.

    minimum: 0

### Citation Char Location

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

### Citation Char Location Param

- `citation_char_location_param: object`

  - `cited_text: string`

  - `document_index: number`

    minimum: 0

  - `document_title: string`

    maxLength: 500, minLength: 1

  - `end_char_index: number`

  - `start_char_index: number`

    minimum: 0

  - `type: "char_location"`

### Citation Content Block Location

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

### Citation Content Block Location Param

- `citation_content_block_location_param: object`

  - `cited_text: string`

    The full text of the cited block range, concatenated.

    Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

  - `document_index: number`

    minimum: 0

  - `document_title: string`

    maxLength: 500, minLength: 1

  - `end_block_index: number`

    Exclusive 0-based end index of the cited block range in the source's `content` array.

    Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

  - `start_block_index: number`

    0-based index of the first cited block in the source's `content` array.

    minimum: 0

  - `type: "content_block_location"`

### Citation Page Location

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

### Citation Page Location Param

- `citation_page_location_param: object`

  - `cited_text: string`

  - `document_index: number`

    minimum: 0

  - `document_title: string`

    maxLength: 500, minLength: 1

  - `end_page_number: number`

  - `start_page_number: number`

    minimum: 1

  - `type: "page_location"`

### Citation Search Result Location Param

- `citation_search_result_location_param: object`

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

### Citation Web Search Result Location Param

- `citation_web_search_result_location_param: object`

  - `cited_text: string`

  - `encrypted_index: string`

  - `title: string`

    maxLength: 512, minLength: 1

  - `type: "web_search_result_location"`

  - `url: string`

    minLength: 1

### Citations Config

- `citations_config: object`

  - `enabled: boolean`

### Citations Config Param

- `citations_config_param: object`

  - `enabled: optional boolean`

### Citations Delta

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

### Citations Search Result Location

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

### Citations Web Search Result Location

- `citations_web_search_result_location: object`

  - `cited_text: string`

  - `encrypted_index: string`

  - `title: string`

    maxLength: 512

  - `type: "web_search_result_location"`

  - `url: string`

### Code Execution Output Block

- `code_execution_output_block: object`

  - `file_id: string`

  - `type: "code_execution_output"`

### Code Execution Output Block Param

- `code_execution_output_block_param: object`

  - `file_id: string`

  - `type: "code_execution_output"`

### Code Execution Result Block

- `code_execution_result_block: object`

  - `content: array of CodeExecutionOutputBlock`

    - `file_id: string`

    - `type: "code_execution_output"`

  - `return_code: number`

  - `stderr: string`

  - `stdout: string`

  - `type: "code_execution_result"`

### Code Execution Result Block Param

- `code_execution_result_block_param: object`

  - `content: array of CodeExecutionOutputBlockParam`

    - `file_id: string`

    - `type: "code_execution_output"`

  - `return_code: number`

  - `stderr: string`

  - `stdout: string`

  - `type: "code_execution_result"`

### Code Execution Tool 20250522

- `code_execution_tool_20250522: object`

  - `name: "code_execution"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `type: "code_execution_20250522"`

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

    - `"code_execution_20260521"`

  - `cache_control: optional object`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `"5m"`

      - `"1h"`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

### Code Execution Tool 20250825

- `code_execution_tool_20250825: object`

  - `name: "code_execution"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `type: "code_execution_20250825"`

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

    - `"code_execution_20260521"`

  - `cache_control: optional object`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `"5m"`

      - `"1h"`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

### Code Execution Tool 20260120

- `code_execution_tool_20260120: object`

  Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

  - `name: "code_execution"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `type: "code_execution_20260120"`

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

    - `"code_execution_20260521"`

  - `cache_control: optional object`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `"5m"`

      - `"1h"`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

### Code Execution Tool 20260521

- `code_execution_tool_20260521: object`

  Code execution tool with REPL state persistence.

  - `name: "code_execution"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `type: "code_execution_20260521"`

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

    - `"code_execution_20260521"`

  - `cache_control: optional object`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `"5m"`

      - `"1h"`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

### Code Execution Tool Result Block

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

### Code Execution Tool Result Block Content

- `code_execution_tool_result_block_content: CodeExecutionToolResultError or CodeExecutionResultBlock or EncryptedCodeExecutionResultBlock`

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

### Code Execution Tool Result Block Param

- `code_execution_tool_result_block_param: object`

  - `content: CodeExecutionToolResultErrorParam or CodeExecutionResultBlockParam or EncryptedCodeExecutionResultBlockParam`

    Code execution result with encrypted stdout for PFC + web_search results.

    - `code_execution_tool_result_error_param: object`

      - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

        - `"invalid_tool_input"`

        - `"unavailable"`

        - `"too_many_requests"`

        - `"execution_time_exceeded"`

      - `type: "code_execution_tool_result_error"`

    - `code_execution_result_block_param: object`

      - `content: array of CodeExecutionOutputBlockParam`

        - `file_id: string`

        - `type: "code_execution_output"`

      - `return_code: number`

      - `stderr: string`

      - `stdout: string`

      - `type: "code_execution_result"`

    - `encrypted_code_execution_result_block_param: object`

      Code execution result with encrypted stdout for PFC + web_search results.

      - `content: array of CodeExecutionOutputBlockParam`

        - `file_id: string`

        - `type: "code_execution_output"`

      - `encrypted_stdout: string`

      - `return_code: number`

      - `stderr: string`

      - `type: "encrypted_code_execution_result"`

  - `tool_use_id: string`

    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

  - `type: "code_execution_tool_result"`

  - `cache_control: optional object`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `"5m"`

      - `"1h"`

### Code Execution Tool Result Block Param Content

- `code_execution_tool_result_block_param_content: CodeExecutionToolResultErrorParam or CodeExecutionResultBlockParam or EncryptedCodeExecutionResultBlockParam`

  Code execution result with encrypted stdout for PFC + web_search results.

  - `code_execution_tool_result_error_param: object`

    - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

      - `"invalid_tool_input"`

      - `"unavailable"`

      - `"too_many_requests"`

      - `"execution_time_exceeded"`

    - `type: "code_execution_tool_result_error"`

  - `code_execution_result_block_param: object`

    - `content: array of CodeExecutionOutputBlockParam`

      - `file_id: string`

      - `type: "code_execution_output"`

    - `return_code: number`

    - `stderr: string`

    - `stdout: string`

    - `type: "code_execution_result"`

  - `encrypted_code_execution_result_block_param: object`

    Code execution result with encrypted stdout for PFC + web_search results.

    - `content: array of CodeExecutionOutputBlockParam`

      - `file_id: string`

      - `type: "code_execution_output"`

    - `encrypted_stdout: string`

    - `return_code: number`

    - `stderr: string`

    - `type: "encrypted_code_execution_result"`

### Code Execution Tool Result Error

- `code_execution_tool_result_error: object`

  - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

    - `"invalid_tool_input"`

    - `"unavailable"`

    - `"too_many_requests"`

    - `"execution_time_exceeded"`

  - `type: "code_execution_tool_result_error"`

### Code Execution Tool Result Error Code

- `code_execution_tool_result_error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

  - `"invalid_tool_input"`

  - `"unavailable"`

  - `"too_many_requests"`

  - `"execution_time_exceeded"`

### Code Execution Tool Result Error Param

- `code_execution_tool_result_error_param: object`

  - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

    - `"invalid_tool_input"`

    - `"unavailable"`

    - `"too_many_requests"`

    - `"execution_time_exceeded"`

  - `type: "code_execution_tool_result_error"`

### Computer Cursor Position Config

- `computer_cursor_position_config: object`

  `cursor_position`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Double Click Config

- `computer_double_click_config: object`

  `double_click`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Hold Key Config

- `computer_hold_key_config: object`

  `hold_key`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Key Config

- `computer_key_config: object`

  `key`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Left Click Config

- `computer_left_click_config: object`

  `left_click`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Left Click Drag Config

- `computer_left_click_drag_config: object`

  `left_click_drag`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Left Mouse Down Config

- `computer_left_mouse_down_config: object`

  `left_mouse_down`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Left Mouse Up Config

- `computer_left_mouse_up_config: object`

  `left_mouse_up`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Middle Click Config

- `computer_middle_click_config: object`

  `middle_click`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Mouse Move Config

- `computer_mouse_move_config: object`

  `mouse_move`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Right Click Config

- `computer_right_click_config: object`

  `right_click`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Screenshot Config

- `computer_screenshot_config: object`

  `screenshot`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Scroll Config

- `computer_scroll_config: object`

  `scroll`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Toolset 20260801

- `computer_toolset_20260801: object`

  The computer toolset: a single `tools[]` entry (carrying no
  `name`) that declares the computer tool family. The model is
  served the family's tool with any members disabled via `configs`
  removed from its schema. Every member is enabled by default, zoom
  included. The single-tool options `display_number` and
  `enable_zoom` are not fields of a toolset entry — it carries only
  `type`, `configs`, and `cache_control`; zoom is controlled
  via `configs.zoom.enabled`.

  - `type: "computer_toolset_20260801"`

  - `cache_control: optional object`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `"5m"`

      - `"1h"`

  - `configs: optional object`

    Per-member configuration for `computer_toolset_20260801`: one
    optional field per member tool, keyed by the member name — the same
    name the member's `tool_use` blocks carry. Every member is an
    accepted key, and a member's defaults apply wherever its key is
    absent. Unknown keys are rejected: the field set is this toolset
    version's complete member set.

    - `cursor_position: optional object`

      `cursor_position`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `double_click: optional object`

      `double_click`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `hold_key: optional object`

      `hold_key`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `key: optional object`

      `key`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `left_click: optional object`

      `left_click`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `left_click_drag: optional object`

      `left_click_drag`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `left_mouse_down: optional object`

      `left_mouse_down`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `left_mouse_up: optional object`

      `left_mouse_up`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `middle_click: optional object`

      `middle_click`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `mouse_move: optional object`

      `mouse_move`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `right_click: optional object`

      `right_click`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `screenshot: optional object`

      `screenshot`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `scroll: optional object`

      `scroll`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `triple_click: optional object`

      `triple_click`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `type: optional object`

      `type`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `wait: optional object`

      `wait`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `zoom: optional object`

      `zoom`'s config overrides.

      - `defer_loading: optional boolean`

        Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

      - `enabled: optional boolean`

        Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Toolset Configs

- `computer_toolset_configs: object`

  Per-member configuration for `computer_toolset_20260801`: one
  optional field per member tool, keyed by the member name — the same
  name the member's `tool_use` blocks carry. Every member is an
  accepted key, and a member's defaults apply wherever its key is
  absent. Unknown keys are rejected: the field set is this toolset
  version's complete member set.

  - `cursor_position: optional object`

    `cursor_position`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `double_click: optional object`

    `double_click`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `hold_key: optional object`

    `hold_key`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `key: optional object`

    `key`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `left_click: optional object`

    `left_click`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `left_click_drag: optional object`

    `left_click_drag`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `left_mouse_down: optional object`

    `left_mouse_down`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `left_mouse_up: optional object`

    `left_mouse_up`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `middle_click: optional object`

    `middle_click`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `mouse_move: optional object`

    `mouse_move`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `right_click: optional object`

    `right_click`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `screenshot: optional object`

    `screenshot`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `scroll: optional object`

    `scroll`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `triple_click: optional object`

    `triple_click`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `type: optional object`

    `type`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `wait: optional object`

    `wait`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `zoom: optional object`

    `zoom`'s config overrides.

    - `defer_loading: optional boolean`

      Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

    - `enabled: optional boolean`

      Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Triple Click Config

- `computer_triple_click_config: object`

  `triple_click`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Type Config

- `computer_type_config: object`

  `type`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Wait Config

- `computer_wait_config: object`

  `wait`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Computer Zoom Config

- `computer_zoom_config: object`

  `zoom`'s config overrides.

  - `defer_loading: optional boolean`

    Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

  - `enabled: optional boolean`

    Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

### Container

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

### Container Params

- `container_params: object`

  Container parameters with skills to be loaded.

  - `id: optional string`

    Container id

  - `skills: optional array of SkillParams`

    List of skills to load in the container

    maxItems: 20

    - `skill_id: string`

      Skill ID

      maxLength: 64, minLength: 1

    - `type: "anthropic" or "custom"`

      Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

      - `"anthropic"`

      - `"custom"`

    - `version: optional string`

      Skill version or 'latest' for most recent version

      maxLength: 64, minLength: 1

### Container Skill

- `container_skill: object`

  A skill that was loaded in a container (response model).

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

### Container Upload Block

- `container_upload_block: object`

  Response model for a file uploaded to the container.

  - `file_id: string`

  - `type: "container_upload"`

### Container Upload Block Param

- `container_upload_block_param: object`

  A content block that represents a file to be uploaded to the container
  Files uploaded via this block will be available in the container's input directory.

  - `file_id: string`

  - `type: "container_upload"`

  - `cache_control: optional object`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `"5m"`

      - `"1h"`

### Content Block

- `content_block: TextBlock or ThinkingBlock or RedactedThinkingBlock or 9 more`

  Response model for a file uploaded to the container.

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

### Content Block Param

- `content_block_param: TextBlockParam or ImageBlockParam or DocumentBlockParam or 13 more`

  Regular text content.

  - `text_block_param: object`

    - `text: string`

      minLength: 1

    - `type: "text"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

        - `"5m"`

        - `"1h"`

    - `citations: optional array of TextCitationParam`

      - `citation_char_location_param: object`

        - `cited_text: string`

        - `document_index: number`

          minimum: 0

        - `document_title: string`

          maxLength: 500, minLength: 1

        - `end_char_index: number`

        - `start_char_index: number`

          minimum: 0

        - `type: "char_location"`

      - `citation_page_location_param: object`

        - `cited_text: string`

        - `document_index: number`

          minimum: 0

        - `document_title: string`

          maxLength: 500, minLength: 1

        - `end_page_number: number`

        - `start_page_number: number`

          minimum: 1

        - `type: "page_location"`

      - `citation_content_block_location_param: object`

        - `cited_text: string`

          The full text of the cited block range, concatenated.

          Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

        - `document_index: number`

          minimum: 0

        - `document_title: string`

          maxLength: 500, minLength: 1

        - `end_block_index: number`

          Exclusive 0-based end index of the cited block range in the source's `content` array.

          Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

        - `start_block_index: number`

          0-based index of the first cited block in the source's `content` array.

          minimum: 0

        - `type: "content_block_location"`

      - `citation_web_search_result_location_param: object`

        - `cited_text: string`

        - `encrypted_index: string`

        - `title: string`

          maxLength: 512, minLength: 1

        - `type: "web_search_result_location"`

        - `url: string`

          minLength: 1

      - `citation_search_result_location_param: object`

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

  - `image_block_param: object`

    - `source: Base64ImageSource or URLImageSource or FileImageSource`

      - `base64_image_source: object`

        - `data: string`

          format: byte

        - `media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"`

          - `"image/jpeg"`

          - `"image/png"`

          - `"image/gif"`

          - `"image/webp"`

        - `type: "base64"`

      - `url_image_source: object`

        - `type: "url"`

        - `url: string`

      - `file_image_source: object`

        - `file_id: string`

        - `type: "file"`

    - `type: "image"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `transformations: optional object`

      Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

      - `oversized_image: optional "downsize" or "error"`

        What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

        - `"downsize"`

        - `"error"`

  - `document_block_param: object`

    - `source: Base64PDFSource or PlainTextSource or ContentBlockSource or 2 more`

      - `base64_pdf_source: object`

        - `data: string`

          format: byte

        - `media_type: "application/pdf"`

        - `type: "base64"`

      - `plain_text_source: object`

        - `data: string`

        - `media_type: "text/plain"`

        - `type: "text"`

      - `content_block_source: object`

        - `content: string or array of ContentBlockSourceContent`

          - `union_member_0: string`

          - `content_block_source_content: array of ContentBlockSourceContent`

            - `text_block_param: object`

              - `text: string`

                minLength: 1

              - `type: "text"`

              - `cache_control: optional object`

                Create a cache control breakpoint at this content block.

              - `citations: optional array of TextCitationParam`

            - `image_block_param: object`

              - `source: Base64ImageSource or URLImageSource or FileImageSource`

              - `type: "image"`

              - `cache_control: optional object`

                Create a cache control breakpoint at this content block.

              - `transformations: optional object`

                Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

        - `type: "content"`

      - `url_pdf_source: object`

        - `type: "url"`

        - `url: string`

      - `file_document_source: object`

        - `file_id: string`

        - `type: "file"`

    - `type: "document"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `citations: optional object`

      - `enabled: optional boolean`

    - `context: optional string`

      minLength: 1

    - `title: optional string`

      maxLength: 500, minLength: 1

  - `search_result_block_param: object`

    - `content: array of TextBlockParam`

      - `text: string`

        minLength: 1

      - `type: "text"`

      - `cache_control: optional object`

        Create a cache control breakpoint at this content block.

      - `citations: optional array of TextCitationParam`

    - `source: string`

    - `title: string`

    - `type: "search_result"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `citations: optional object`

      - `enabled: optional boolean`

  - `thinking_block_param: object`

    - `signature: string`

      The `signature` value of this thinking block, exactly as returned by the API in a previous response. Used to verify that the block was generated by Claude.

      Thinking blocks must be passed back unmodified and in their original order; a modified block results in a 400 `invalid_request_error`.

    - `thinking: string`

      The `thinking` text of this block as returned by the API.

    - `type: "thinking"`

  - `redacted_thinking_block_param: object`

    - `data: string`

      The `data` value of this redacted thinking block, exactly as returned by the API in a previous response. Opaque and encrypted; pass it back unchanged.

    - `type: "redacted_thinking"`

  - `tool_use_block_param: object`

    - `id: string`

      pattern: ^[a-zA-Z0-9_-]+$

    - `input: map[unknown]`

    - `name: string`

      maxLength: 200, minLength: 1

    - `type: "tool_use"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `caller: optional DirectCaller or ServerToolCaller or ServerToolCaller20260120`

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

    - `toolset_name: optional string`

      For a toolset member tool_use, the toolset family this member belongs to.

      maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

  - `tool_result_block_param: object`

    - `tool_use_id: string`

      pattern: ^[a-zA-Z0-9_-]+$

    - `type: "tool_result"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `content: optional array of TextBlockParam or ImageBlockParam or SearchResultBlockParam or 3 more`

      - `text_block_param: object`

        - `text: string`

          minLength: 1

        - `type: "text"`

        - `cache_control: optional object`

          Create a cache control breakpoint at this content block.

        - `citations: optional array of TextCitationParam`

      - `image_block_param: object`

        - `source: Base64ImageSource or URLImageSource or FileImageSource`

        - `type: "image"`

        - `cache_control: optional object`

          Create a cache control breakpoint at this content block.

        - `transformations: optional object`

          Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

      - `search_result_block_param: object`

        - `content: array of TextBlockParam`

        - `source: string`

        - `title: string`

        - `type: "search_result"`

        - `cache_control: optional object`

          Create a cache control breakpoint at this content block.

        - `citations: optional object`

      - `document_block_param: object`

        - `source: Base64PDFSource or PlainTextSource or ContentBlockSource or 2 more`

        - `type: "document"`

        - `cache_control: optional object`

          Create a cache control breakpoint at this content block.

        - `citations: optional object`

        - `context: optional string`

          minLength: 1

        - `title: optional string`

          maxLength: 500, minLength: 1

      - `tool_reference_block_param: object`

        Tool reference block that can be included in tool_result content.

        - `tool_name: string`

          maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

        - `type: "tool_reference"`

        - `cache_control: optional object`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

          - `ttl: optional "5m" or "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `browser_state_block_param: object`

        The caller's browser state after a browser toolset member call —
        the full inventory of open tabs, which tab is active, and any side
        effects (tabs opened, download state changes) the call produced.

        At most one per `tool_result`, only on a non-error result answering a
        browser toolset member `tool_use`. The server renders the
        model-visible text from it; the model never sees the raw fields.

        - `tabs: array of BrowserStateTabEntry`

          All tabs open in the browser after this call — the full inventory, not a delta. May be empty. Whenever non-empty, exactly one entry carries `active: true`.

          maxItems: 100

          - `tab_id: string`

            The caller-assigned identifier for this tab, unique within the inventory.

            maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

          - `title: string`

            The title of the page the tab is showing. May be empty.

            maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

          - `url: string`

            The URL of the page the tab is showing. May be empty.

            maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

          - `active: optional boolean`

            Whether this tab is the active tab after this call. Whenever `tabs` is non-empty, exactly one entry is marked `active: true`.

        - `type: "browser_state"`

        - `cache_control: optional object`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

          - `ttl: optional "5m" or "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

        - `state_changes: optional array of BrowserStateChange`

          Tabs opened and download state changes during this call. "Nothing to report" is expressed by omitting the field, never by an empty list.

          maxItems: 200, minItems: 1

          - `browser_state_change_tab_opened: object`

            A tab this call's execution opened that remains open at its end —
            the creation delta of the `tabs` inventory, not an event log.

            Carries only the `tab_id`; the tab's `title` and `url` live on its
            `tabs` entry, which must include the same `tab_id`. A tab opened
            during a failed call gets no deferred `tab_opened`; it simply appears
            in the next result's `tabs` inventory.

            - `tab_id: string`

              The `tab_id` of the opened tab, present in `tabs`.

              maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

            - `type: "tab_opened"`

          - `browser_state_change_download_started: object`

            A file download that started during this call.

            - `download_id: string`

              The caller-assigned identifier for this download, stable across the state changes reporting it.

              maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

            - `type: "download_started"`

            - `url: string`

              The final post-redirect URL the download was served from.

              maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

          - `browser_state_change_download_completed: object`

            A file download that finished during this call, reported with the
            same `download_id` as its `download_started` — or without a prior
            `download_started`, when the download finished during the call that
            started it (at most one state change per `download_id` per result).

            - `download_id: string`

              The caller-assigned identifier for this download, stable across the state changes reporting it.

              maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

            - `type: "download_completed"`

            - `url: string`

              The final post-redirect URL the download was served from.

              maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

            - `path: optional string`

              Where the executor saved the file, on the executor's filesystem. Only included when another tool in the same environment can read the file at that path.

              pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

            - `size_bytes: optional number`

              The completed download's size.

              minimum: 0

          - `browser_state_change_download_failed: object`

            A file download that failed — or was cancelled — during this call.

            - `download_id: string`

              The caller-assigned identifier for this download, stable across the state changes reporting it.

              maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

            - `type: "download_failed"`

            - `url: string`

              The final post-redirect URL the download was served from.

              maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

            - `error: optional string`

              The failure or cancellation detail, when known.

              pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

    - `is_error: optional boolean`

    - `toolset_name: optional string`

      For a toolset member tool_result, the toolset family of the paired tool_use.

      maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

  - `server_tool_use_block_param: object`

    - `id: string`

      pattern: ^srvtoolu_[a-zA-Z0-9_]+$

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

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `caller: optional DirectCaller or ServerToolCaller or ServerToolCaller20260120`

      Tool invocation directly from the model.

      - `direct_caller: object`

        Tool invocation directly from the model.

      - `server_tool_caller: object`

        Tool invocation generated by a server-side tool.

      - `server_tool_caller_20260120: object`

  - `web_search_tool_result_block_param: object`

    - `content: array of WebSearchResultBlockParam or WebSearchToolRequestError`

      - `web_search_tool_result_block_item: array of WebSearchResultBlockParam`

        - `encrypted_content: string`

        - `title: string`

        - `type: "web_search_result"`

        - `url: string`

        - `page_age: optional string`

      - `web_search_tool_request_error: object`

        - `error_code: "invalid_tool_input" or "unavailable" or "max_uses_exceeded" or 3 more`

          - `"invalid_tool_input"`

          - `"unavailable"`

          - `"max_uses_exceeded"`

          - `"too_many_requests"`

          - `"query_too_long"`

          - `"request_too_large"`

        - `type: "web_search_tool_result_error"`

    - `tool_use_id: string`

      pattern: ^srvtoolu_[a-zA-Z0-9_]+$

    - `type: "web_search_tool_result"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `caller: optional DirectCaller or ServerToolCaller or ServerToolCaller20260120`

      Tool invocation directly from the model.

      - `direct_caller: object`

        Tool invocation directly from the model.

      - `server_tool_caller: object`

        Tool invocation generated by a server-side tool.

      - `server_tool_caller_20260120: object`

  - `web_fetch_tool_result_block_param: object`

    - `content: WebFetchToolResultErrorBlockParam or WebFetchBlockParam`

      - `web_fetch_tool_result_error_block_param: object`

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

      - `web_fetch_block_param: object`

        - `content: object`

          - `source: Base64PDFSource or PlainTextSource or ContentBlockSource or 2 more`

          - `type: "document"`

          - `cache_control: optional object`

            Create a cache control breakpoint at this content block.

          - `citations: optional object`

          - `context: optional string`

            minLength: 1

          - `title: optional string`

            maxLength: 500, minLength: 1

        - `type: "web_fetch_result"`

        - `url: string`

          Fetched content URL

        - `retrieved_at: optional string`

          ISO 8601 timestamp when the content was retrieved

    - `tool_use_id: string`

      pattern: ^srvtoolu_[a-zA-Z0-9_]+$

    - `type: "web_fetch_tool_result"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `caller: optional DirectCaller or ServerToolCaller or ServerToolCaller20260120`

      Tool invocation directly from the model.

      - `direct_caller: object`

        Tool invocation directly from the model.

      - `server_tool_caller: object`

        Tool invocation generated by a server-side tool.

      - `server_tool_caller_20260120: object`

  - `code_execution_tool_result_block_param: object`

    - `content: CodeExecutionToolResultErrorParam or CodeExecutionResultBlockParam or EncryptedCodeExecutionResultBlockParam`

      Code execution result with encrypted stdout for PFC + web_search results.

      - `code_execution_tool_result_error_param: object`

        - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

          - `"invalid_tool_input"`

          - `"unavailable"`

          - `"too_many_requests"`

          - `"execution_time_exceeded"`

        - `type: "code_execution_tool_result_error"`

      - `code_execution_result_block_param: object`

        - `content: array of CodeExecutionOutputBlockParam`

          - `file_id: string`

          - `type: "code_execution_output"`

        - `return_code: number`

        - `stderr: string`

        - `stdout: string`

        - `type: "code_execution_result"`

      - `encrypted_code_execution_result_block_param: object`

        Code execution result with encrypted stdout for PFC + web_search results.

        - `content: array of CodeExecutionOutputBlockParam`

          - `file_id: string`

          - `type: "code_execution_output"`

        - `encrypted_stdout: string`

        - `return_code: number`

        - `stderr: string`

        - `type: "encrypted_code_execution_result"`

    - `tool_use_id: string`

      pattern: ^srvtoolu_[a-zA-Z0-9_]+$

    - `type: "code_execution_tool_result"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

  - `bash_code_execution_tool_result_block_param: object`

    - `content: BashCodeExecutionToolResultErrorParam or BashCodeExecutionResultBlockParam`

      - `bash_code_execution_tool_result_error_param: object`

        - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

          - `"invalid_tool_input"`

          - `"unavailable"`

          - `"too_many_requests"`

          - `"execution_time_exceeded"`

          - `"output_file_too_large"`

        - `type: "bash_code_execution_tool_result_error"`

      - `bash_code_execution_result_block_param: object`

        - `content: array of BashCodeExecutionOutputBlockParam`

          - `file_id: string`

          - `type: "bash_code_execution_output"`

        - `return_code: number`

        - `stderr: string`

        - `stdout: string`

        - `type: "bash_code_execution_result"`

    - `tool_use_id: string`

      pattern: ^srvtoolu_[a-zA-Z0-9_]+$

    - `type: "bash_code_execution_tool_result"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

  - `text_editor_code_execution_tool_result_block_param: object`

    - `content: TextEditorCodeExecutionToolResultErrorParam or TextEditorCodeExecutionViewResultBlockParam or TextEditorCodeExecutionCreateResultBlockParam or TextEditorCodeExecutionStrReplaceResultBlockParam`

      - `text_editor_code_execution_tool_result_error_param: object`

        - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

          - `"invalid_tool_input"`

          - `"unavailable"`

          - `"too_many_requests"`

          - `"execution_time_exceeded"`

          - `"file_not_found"`

        - `type: "text_editor_code_execution_tool_result_error"`

        - `error_message: optional string`

      - `text_editor_code_execution_view_result_block_param: object`

        - `content: string`

        - `file_type: "text" or "image" or "pdf"`

          - `"text"`

          - `"image"`

          - `"pdf"`

        - `type: "text_editor_code_execution_view_result"`

        - `num_lines: optional number`

        - `start_line: optional number`

        - `total_lines: optional number`

      - `text_editor_code_execution_create_result_block_param: object`

        - `is_file_update: boolean`

        - `type: "text_editor_code_execution_create_result"`

      - `text_editor_code_execution_str_replace_result_block_param: object`

        - `type: "text_editor_code_execution_str_replace_result"`

        - `lines: optional array of string`

        - `new_lines: optional number`

        - `new_start: optional number`

        - `old_lines: optional number`

        - `old_start: optional number`

    - `tool_use_id: string`

      pattern: ^srvtoolu_[a-zA-Z0-9_]+$

    - `type: "text_editor_code_execution_tool_result"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

  - `tool_search_tool_result_block_param: object`

    - `content: ToolSearchToolResultErrorParam or ToolSearchToolSearchResultBlockParam`

      - `tool_search_tool_result_error_param: object`

        - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

          - `"invalid_tool_input"`

          - `"unavailable"`

          - `"too_many_requests"`

          - `"execution_time_exceeded"`

        - `type: "tool_search_tool_result_error"`

        - `error_message: optional string`

      - `tool_search_tool_search_result_block_param: object`

        - `tool_references: array of ToolReferenceBlockParam`

          - `tool_name: string`

            maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

          - `type: "tool_reference"`

          - `cache_control: optional object`

            Create a cache control breakpoint at this content block.

        - `type: "tool_search_tool_search_result"`

    - `tool_use_id: string`

      pattern: ^srvtoolu_[a-zA-Z0-9_]+$

    - `type: "tool_search_tool_result"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

  - `container_upload_block_param: object`

    A content block that represents a file to be uploaded to the container
    Files uploaded via this block will be available in the container's input directory.

    - `file_id: string`

    - `type: "container_upload"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

### Content Block Source

- `content_block_source: object`

  - `content: string or array of ContentBlockSourceContent`

    - `union_member_0: string`

    - `content_block_source_content: array of ContentBlockSourceContent`

      - `text_block_param: object`

        - `text: string`

          minLength: 1

        - `type: "text"`

        - `cache_control: optional object`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

          - `ttl: optional "5m" or "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

            - `"5m"`

            - `"1h"`

        - `citations: optional array of TextCitationParam`

          - `citation_char_location_param: object`

            - `cited_text: string`

            - `document_index: number`

              minimum: 0

            - `document_title: string`

              maxLength: 500, minLength: 1

            - `end_char_index: number`

            - `start_char_index: number`

              minimum: 0

            - `type: "char_location"`

          - `citation_page_location_param: object`

            - `cited_text: string`

            - `document_index: number`

              minimum: 0

            - `document_title: string`

              maxLength: 500, minLength: 1

            - `end_page_number: number`

            - `start_page_number: number`

              minimum: 1

            - `type: "page_location"`

          - `citation_content_block_location_param: object`

            - `cited_text: string`

              The full text of the cited block range, concatenated.

              Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

            - `document_index: number`

              minimum: 0

            - `document_title: string`

              maxLength: 500, minLength: 1

            - `end_block_index: number`

              Exclusive 0-based end index of the cited block range in the source's `content` array.

              Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

            - `start_block_index: number`

              0-based index of the first cited block in the source's `content` array.

              minimum: 0

            - `type: "content_block_location"`

          - `citation_web_search_result_location_param: object`

            - `cited_text: string`

            - `encrypted_index: string`

            - `title: string`

              maxLength: 512, minLength: 1

            - `type: "web_search_result_location"`

            - `url: string`

              minLength: 1

          - `citation_search_result_location_param: object`

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

      - `image_block_param: object`

        - `source: Base64ImageSource or URLImageSource or FileImageSource`

          - `base64_image_source: object`

            - `data: string`

              format: byte

            - `media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"`

              - `"image/jpeg"`

              - `"image/png"`

              - `"image/gif"`

              - `"image/webp"`

            - `type: "base64"`

          - `url_image_source: object`

            - `type: "url"`

            - `url: string`

          - `file_image_source: object`

            - `file_id: string`

            - `type: "file"`

        - `type: "image"`

        - `cache_control: optional object`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

          - `ttl: optional "5m" or "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

        - `transformations: optional object`

          Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

          - `oversized_image: optional "downsize" or "error"`

            What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

            - `"downsize"`

            - `"error"`

  - `type: "content"`

### Content Block Source Content

- `content_block_source_content: TextBlockParam or ImageBlockParam`

  - `text_block_param: object`

    - `text: string`

      minLength: 1

    - `type: "text"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

        - `"5m"`

        - `"1h"`

    - `citations: optional array of TextCitationParam`

      - `citation_char_location_param: object`

        - `cited_text: string`

        - `document_index: number`

          minimum: 0

        - `document_title: string`

          maxLength: 500, minLength: 1

        - `end_char_index: number`

        - `start_char_index: number`

          minimum: 0

        - `type: "char_location"`

      - `citation_page_location_param: object`

        - `cited_text: string`

        - `document_index: number`

          minimum: 0

        - `document_title: string`

          maxLength: 500, minLength: 1

        - `end_page_number: number`

        - `start_page_number: number`

          minimum: 1

        - `type: "page_location"`

      - `citation_content_block_location_param: object`

        - `cited_text: string`

          The full text of the cited block range, concatenated.

          Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

        - `document_index: number`

          minimum: 0

        - `document_title: string`

          maxLength: 500, minLength: 1

        - `end_block_index: number`

          Exclusive 0-based end index of the cited block range in the source's `content` array.

          Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

        - `start_block_index: number`

          0-based index of the first cited block in the source's `content` array.

          minimum: 0

        - `type: "content_block_location"`

      - `citation_web_search_result_location_param: object`

        - `cited_text: string`

        - `encrypted_index: string`

        - `title: string`

          maxLength: 512, minLength: 1

        - `type: "web_search_result_location"`

        - `url: string`

          minLength: 1

      - `citation_search_result_location_param: object`

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

  - `image_block_param: object`

    - `source: Base64ImageSource or URLImageSource or FileImageSource`

      - `base64_image_source: object`

        - `data: string`

          format: byte

        - `media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"`

          - `"image/jpeg"`

          - `"image/png"`

          - `"image/gif"`

          - `"image/webp"`

        - `type: "base64"`

      - `url_image_source: object`

        - `type: "url"`

        - `url: string`

      - `file_image_source: object`

        - `file_id: string`

        - `type: "file"`

    - `type: "image"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `transformations: optional object`

      Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

      - `oversized_image: optional "downsize" or "error"`

        What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

        - `"downsize"`

        - `"error"`

### Direct Caller

- `direct_caller: object`

  Tool invocation directly from the model.

  - `type: "direct"`

### Document Block

- `document_block: object`

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

### Document Block Param

- `document_block_param: object`

  - `source: Base64PDFSource or PlainTextSource or ContentBlockSource or 2 more`

    - `base64_pdf_source: object`

      - `data: string`

        format: byte

      - `media_type: "application/pdf"`

      - `type: "base64"`

    - `plain_text_source: object`

      - `data: string`

      - `media_type: "text/plain"`

      - `type: "text"`

    - `content_block_source: object`

      - `content: string or array of ContentBlockSourceContent`

        - `union_member_0: string`

        - `content_block_source_content: array of ContentBlockSourceContent`

          - `text_block_param: object`

            - `text: string`

              minLength: 1

            - `type: "text"`

            - `cache_control: optional object`

              Create a cache control breakpoint at this content block.

              - `type: "ephemeral"`

              - `ttl: optional "5m" or "1h"`

                The time-to-live for the cache control breakpoint.

                This may be one the following values:

                - `5m`: 5 minutes
                - `1h`: 1 hour

                Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

                - `"5m"`

                - `"1h"`

            - `citations: optional array of TextCitationParam`

              - `citation_char_location_param: object`

                - `cited_text: string`

                - `document_index: number`

                  minimum: 0

                - `document_title: string`

                  maxLength: 500, minLength: 1

                - `end_char_index: number`

                - `start_char_index: number`

                  minimum: 0

                - `type: "char_location"`

              - `citation_page_location_param: object`

                - `cited_text: string`

                - `document_index: number`

                  minimum: 0

                - `document_title: string`

                  maxLength: 500, minLength: 1

                - `end_page_number: number`

                - `start_page_number: number`

                  minimum: 1

                - `type: "page_location"`

              - `citation_content_block_location_param: object`

                - `cited_text: string`

                  The full text of the cited block range, concatenated.

                  Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

                - `document_index: number`

                  minimum: 0

                - `document_title: string`

                  maxLength: 500, minLength: 1

                - `end_block_index: number`

                  Exclusive 0-based end index of the cited block range in the source's `content` array.

                  Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

                - `start_block_index: number`

                  0-based index of the first cited block in the source's `content` array.

                  minimum: 0

                - `type: "content_block_location"`

              - `citation_web_search_result_location_param: object`

                - `cited_text: string`

                - `encrypted_index: string`

                - `title: string`

                  maxLength: 512, minLength: 1

                - `type: "web_search_result_location"`

                - `url: string`

                  minLength: 1

              - `citation_search_result_location_param: object`

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

          - `image_block_param: object`

            - `source: Base64ImageSource or URLImageSource or FileImageSource`

              - `base64_image_source: object`

                - `data: string`

                  format: byte

                - `media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"`

                  - `"image/jpeg"`

                  - `"image/png"`

                  - `"image/gif"`

                  - `"image/webp"`

                - `type: "base64"`

              - `url_image_source: object`

                - `type: "url"`

                - `url: string`

              - `file_image_source: object`

                - `file_id: string`

                - `type: "file"`

            - `type: "image"`

            - `cache_control: optional object`

              Create a cache control breakpoint at this content block.

              - `type: "ephemeral"`

              - `ttl: optional "5m" or "1h"`

                The time-to-live for the cache control breakpoint.

                This may be one the following values:

                - `5m`: 5 minutes
                - `1h`: 1 hour

                Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

            - `transformations: optional object`

              Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

              - `oversized_image: optional "downsize" or "error"`

                What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

                - `"downsize"`

                - `"error"`

      - `type: "content"`

    - `url_pdf_source: object`

      - `type: "url"`

      - `url: string`

    - `file_document_source: object`

      - `file_id: string`

      - `type: "file"`

  - `type: "document"`

  - `cache_control: optional object`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

  - `citations: optional object`

    - `enabled: optional boolean`

  - `context: optional string`

    minLength: 1

  - `title: optional string`

    maxLength: 500, minLength: 1

### Encrypted Code Execution Result Block

- `encrypted_code_execution_result_block: object`

  Code execution result with encrypted stdout for PFC + web_search results.

  - `content: array of CodeExecutionOutputBlock`

    - `file_id: string`

    - `type: "code_execution_output"`

  - `encrypted_stdout: string`

  - `return_code: number`

  - `stderr: string`

  - `type: "encrypted_code_execution_result"`

### Encrypted Code Execution Result Block Param

- `encrypted_code_execution_result_block_param: object`

  Code execution result with encrypted stdout for PFC + web_search results.

  - `content: array of CodeExecutionOutputBlockParam`

    - `file_id: string`

    - `type: "code_execution_output"`

  - `encrypted_stdout: string`

  - `return_code: number`

  - `stderr: string`

  - `type: "encrypted_code_execution_result"`

### File Document Source

- `file_document_source: object`

  - `file_id: string`

  - `type: "file"`

### File Image Source

- `file_image_source: object`

  - `file_id: string`

  - `type: "file"`

### Image Block Param

- `image_block_param: object`

  - `source: Base64ImageSource or URLImageSource or FileImageSource`

    - `base64_image_source: object`

      - `data: string`

        format: byte

      - `media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"`

        - `"image/jpeg"`

        - `"image/png"`

        - `"image/gif"`

        - `"image/webp"`

      - `type: "base64"`

    - `url_image_source: object`

      - `type: "url"`

      - `url: string`

    - `file_image_source: object`

      - `file_id: string`

      - `type: "file"`

  - `type: "image"`

  - `cache_control: optional object`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `"5m"`

      - `"1h"`

  - `transformations: optional object`

    Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

    - `oversized_image: optional "downsize" or "error"`

      What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

      - `"downsize"`

      - `"error"`

### Image Transformations Param

- `image_transformations_param: object`

  Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

  - `oversized_image: optional "downsize" or "error"`

    What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

    - `"downsize"`

    - `"error"`

### Input JSON Delta

- `input_json_delta: object`

  - `partial_json: string`

  - `type: "input_json_delta"`

### JSON Output Format

- `json_output_format: object`

  - `schema: map[unknown]`

    The JSON schema of the format

  - `type: "json_schema"`

### Memory Tool 20250818

- `memory_tool_20250818: object`

  - `name: "memory"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `type: "memory_20250818"`

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

    - `"code_execution_20260521"`

  - `cache_control: optional object`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `"5m"`

      - `"1h"`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `input_examples: optional array of map[unknown]`

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

### Message

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

  - `model: "claude-fable-5-1" or "claude-mythos-5-1" or "claude-sonnet-5" or 14 more or string`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

### Message Count Tokens Tool

- `message_count_tokens_tool: Tool or ToolBash20250124 or CodeExecutionTool20250522 or 18 more`

  Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

  - `tool: object`

    - `input_schema: object`

      [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

      This defines the shape of the `input` that your tool accepts and that the model will produce.

      - `type: "object"`

      - `properties: optional map[unknown]`

      - `required: optional array of string`

    - `name: string`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      maxLength: 128, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,128}$

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

        - `"5m"`

        - `"1h"`

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `description: optional string`

      Description of what this tool does.

      Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

    - `eager_input_streaming: optional boolean`

      Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

    - `input_examples: optional array of map[unknown]`

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

    - `type: optional "custom"`

  - `tool_bash_20250124: object`

    - `name: "bash"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "bash_20250124"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples: optional array of map[unknown]`

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `code_execution_tool_20250522: object`

    - `name: "code_execution"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "code_execution_20250522"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `code_execution_tool_20250825: object`

    - `name: "code_execution"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "code_execution_20250825"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `code_execution_tool_20260120: object`

    Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

    - `name: "code_execution"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "code_execution_20260120"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `code_execution_tool_20260521: object`

    Code execution tool with REPL state persistence.

    - `name: "code_execution"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "code_execution_20260521"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `browser_toolset_20260801: object`

    The browser toolset: a single `tools[]` entry (carrying no
    `name`) that declares the browser tool family. The model is served
    the family's tool with any members disabled via `configs` removed
    from its schema.

    - `type: "browser_toolset_20260801"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `configs: optional object`

      Per-member configuration for `browser_toolset_20260801`: one
      optional field per member tool, keyed by the member name — the same
      name the member's `tool_use` blocks carry. Every member is an
      accepted key, and a member's defaults apply wherever its key is
      absent. Unknown keys are rejected: the field set is this toolset
      version's complete member set.

      - `close_tab: optional object`

        `close_tab`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `double_click: optional object`

        `double_click`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `file_upload: optional object`

        `file_upload`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `find: optional object`

        `find`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `form_input: optional object`

        `form_input`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `get_page_text: optional object`

        `get_page_text`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `hold_key: optional object`

        `hold_key`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `hover: optional object`

        `hover`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `javascript_exec: optional object`

        `javascript_exec`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `key: optional object`

        `key`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `left_click: optional object`

        `left_click`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `left_click_drag: optional object`

        `left_click_drag`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `left_mouse_down: optional object`

        `left_mouse_down`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `left_mouse_up: optional object`

        `left_mouse_up`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `list_tabs: optional object`

        `list_tabs`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `middle_click: optional object`

        `middle_click`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `mouse_move: optional object`

        `mouse_move`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `navigate: optional object`

        `navigate`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `new_tab: optional object`

        `new_tab`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `read_console: optional object`

        `read_console`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `read_network: optional object`

        `read_network`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `read_page: optional object`

        `read_page`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `right_click: optional object`

        `right_click`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `screenshot: optional object`

        `screenshot`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `scroll: optional object`

        `scroll`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `scroll_to: optional object`

        `scroll_to`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `switch_tab: optional object`

        `switch_tab`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `triple_click: optional object`

        `triple_click`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `type: optional object`

        `type`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `wait: optional object`

        `wait`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `zoom: optional object`

        `zoom`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `memory_tool_20250818: object`

    - `name: "memory"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "memory_20250818"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples: optional array of map[unknown]`

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `computer_toolset_20260801: object`

    The computer toolset: a single `tools[]` entry (carrying no
    `name`) that declares the computer tool family. The model is
    served the family's tool with any members disabled via `configs`
    removed from its schema. Every member is enabled by default, zoom
    included. The single-tool options `display_number` and
    `enable_zoom` are not fields of a toolset entry — it carries only
    `type`, `configs`, and `cache_control`; zoom is controlled
    via `configs.zoom.enabled`.

    - `type: "computer_toolset_20260801"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `configs: optional object`

      Per-member configuration for `computer_toolset_20260801`: one
      optional field per member tool, keyed by the member name — the same
      name the member's `tool_use` blocks carry. Every member is an
      accepted key, and a member's defaults apply wherever its key is
      absent. Unknown keys are rejected: the field set is this toolset
      version's complete member set.

      - `cursor_position: optional object`

        `cursor_position`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `double_click: optional object`

        `double_click`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `hold_key: optional object`

        `hold_key`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `key: optional object`

        `key`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `left_click: optional object`

        `left_click`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `left_click_drag: optional object`

        `left_click_drag`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `left_mouse_down: optional object`

        `left_mouse_down`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `left_mouse_up: optional object`

        `left_mouse_up`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `middle_click: optional object`

        `middle_click`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `mouse_move: optional object`

        `mouse_move`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `right_click: optional object`

        `right_click`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `screenshot: optional object`

        `screenshot`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `scroll: optional object`

        `scroll`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `triple_click: optional object`

        `triple_click`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `type: optional object`

        `type`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `wait: optional object`

        `wait`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `zoom: optional object`

        `zoom`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `tool_text_editor_20250124: object`

    - `name: "str_replace_editor"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "text_editor_20250124"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples: optional array of map[unknown]`

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `tool_text_editor_20250429: object`

    - `name: "str_replace_based_edit_tool"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "text_editor_20250429"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples: optional array of map[unknown]`

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `tool_text_editor_20250728: object`

    - `name: "str_replace_based_edit_tool"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "text_editor_20250728"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples: optional array of map[unknown]`

    - `max_characters: optional number`

      Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

      minimum: 1

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `web_search_tool_20250305: object`

    - `name: "web_search"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "web_search_20250305"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `allowed_domains: optional array of string`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `blocked_domains: optional array of string`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_uses: optional number`

      Maximum number of times the tool can be used in the API request.

      exclusiveMinimum: 0

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

    - `user_location: optional object`

      Parameters for the user's location. Used to provide more relevant search results.

      - `type: "approximate"`

      - `city: optional string`

        The city of the user.

        maxLength: 255, minLength: 1

      - `country: optional string`

        The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

        maxLength: 2, minLength: 2

      - `region: optional string`

        The region of the user.

        maxLength: 255, minLength: 1

      - `timezone: optional string`

        The [IANA timezone](https://nodatime.org/TimeZones) of the user.

        maxLength: 255, minLength: 1

  - `web_fetch_tool_20250910: object`

    - `name: "web_fetch"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "web_fetch_20250910"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `allowed_domains: optional array of string`

      List of domains to allow fetching from

    - `blocked_domains: optional array of string`

      List of domains to block fetching from

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `citations: optional object`

      Citations configuration for fetched documents. Citations are disabled by default.

      - `enabled: optional boolean`

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_content_tokens: optional number`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

      exclusiveMinimum: 0

    - `max_uses: optional number`

      Maximum number of times the tool can be used in the API request.

      exclusiveMinimum: 0

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `web_search_tool_20260209: object`

    - `name: "web_search"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "web_search_20260209"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `allowed_domains: optional array of string`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `blocked_domains: optional array of string`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_uses: optional number`

      Maximum number of times the tool can be used in the API request.

      exclusiveMinimum: 0

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

    - `user_location: optional object`

      Parameters for the user's location. Used to provide more relevant search results.

      - `type: "approximate"`

      - `city: optional string`

        The city of the user.

        maxLength: 255, minLength: 1

      - `country: optional string`

        The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

        maxLength: 2, minLength: 2

      - `region: optional string`

        The region of the user.

        maxLength: 255, minLength: 1

      - `timezone: optional string`

        The [IANA timezone](https://nodatime.org/TimeZones) of the user.

        maxLength: 255, minLength: 1

  - `web_fetch_tool_20260209: object`

    - `name: "web_fetch"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "web_fetch_20260209"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `allowed_domains: optional array of string`

      List of domains to allow fetching from

    - `blocked_domains: optional array of string`

      List of domains to block fetching from

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `citations: optional object`

      Citations configuration for fetched documents. Citations are disabled by default.

      - `enabled: optional boolean`

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_content_tokens: optional number`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

      exclusiveMinimum: 0

    - `max_uses: optional number`

      Maximum number of times the tool can be used in the API request.

      exclusiveMinimum: 0

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `web_fetch_tool_20260309: object`

    Web fetch tool with use_cache parameter for bypassing cached content.

    - `name: "web_fetch"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "web_fetch_20260309"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `allowed_domains: optional array of string`

      List of domains to allow fetching from

    - `blocked_domains: optional array of string`

      List of domains to block fetching from

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `citations: optional object`

      Citations configuration for fetched documents. Citations are disabled by default.

      - `enabled: optional boolean`

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_content_tokens: optional number`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

      exclusiveMinimum: 0

    - `max_uses: optional number`

      Maximum number of times the tool can be used in the API request.

      exclusiveMinimum: 0

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

    - `use_cache: optional boolean`

      Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

  - `web_search_tool_20260318: object`

    - `name: "web_search"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "web_search_20260318"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `allowed_domains: optional array of string`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `blocked_domains: optional array of string`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_uses: optional number`

      Maximum number of times the tool can be used in the API request.

      exclusiveMinimum: 0

    - `response_inclusion: optional "full" or "excluded"`

      How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

      - `"full"`

      - `"excluded"`

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

    - `user_location: optional object`

      Parameters for the user's location. Used to provide more relevant search results.

      - `type: "approximate"`

      - `city: optional string`

        The city of the user.

        maxLength: 255, minLength: 1

      - `country: optional string`

        The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

        maxLength: 2, minLength: 2

      - `region: optional string`

        The region of the user.

        maxLength: 255, minLength: 1

      - `timezone: optional string`

        The [IANA timezone](https://nodatime.org/TimeZones) of the user.

        maxLength: 255, minLength: 1

  - `web_fetch_tool_20260318: object`

    - `name: "web_fetch"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "web_fetch_20260318"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `allowed_domains: optional array of string`

      List of domains to allow fetching from

    - `blocked_domains: optional array of string`

      List of domains to block fetching from

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `citations: optional object`

      Citations configuration for fetched documents. Citations are disabled by default.

      - `enabled: optional boolean`

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_content_tokens: optional number`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

      exclusiveMinimum: 0

    - `max_uses: optional number`

      Maximum number of times the tool can be used in the API request.

      exclusiveMinimum: 0

    - `response_inclusion: optional "full" or "excluded"`

      How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

      - `"full"`

      - `"excluded"`

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

    - `use_cache: optional boolean`

      Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

  - `tool_search_tool_bm25_20251119: object`

    - `name: "tool_search_tool_bm25"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "tool_search_tool_bm25_20251119" or "tool_search_tool_bm25"`

      - `"tool_search_tool_bm25_20251119"`

      - `"tool_search_tool_bm25"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `tool_search_tool_regex_20251119: object`

    - `name: "tool_search_tool_regex"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "tool_search_tool_regex_20251119" or "tool_search_tool_regex"`

      - `"tool_search_tool_regex_20251119"`

      - `"tool_search_tool_regex"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

### Message Create Params Container

- `message_create_params_container: ContainerParams or string`

  Container identifier for reuse across requests.

  - `container_params: object`

    Container parameters with skills to be loaded.

    - `id: optional string`

      Container id

    - `skills: optional array of SkillParams`

      List of skills to load in the container

      maxItems: 20

      - `skill_id: string`

        Skill ID

        maxLength: 64, minLength: 1

      - `type: "anthropic" or "custom"`

        Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

        - `"anthropic"`

        - `"custom"`

      - `version: optional string`

        Skill version or 'latest' for most recent version

        maxLength: 64, minLength: 1

  - `union_member_1: string`

### Message Delta Usage

- `message_delta_usage: object`

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

### Message Param

- `message_param: object`

  - `content: array of ContentBlockParam`

    - `text_block_param: object`

      - `text: string`

        minLength: 1

      - `type: "text"`

      - `cache_control: optional object`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

          - `"5m"`

          - `"1h"`

      - `citations: optional array of TextCitationParam`

        - `citation_char_location_param: object`

          - `cited_text: string`

          - `document_index: number`

            minimum: 0

          - `document_title: string`

            maxLength: 500, minLength: 1

          - `end_char_index: number`

          - `start_char_index: number`

            minimum: 0

          - `type: "char_location"`

        - `citation_page_location_param: object`

          - `cited_text: string`

          - `document_index: number`

            minimum: 0

          - `document_title: string`

            maxLength: 500, minLength: 1

          - `end_page_number: number`

          - `start_page_number: number`

            minimum: 1

          - `type: "page_location"`

        - `citation_content_block_location_param: object`

          - `cited_text: string`

            The full text of the cited block range, concatenated.

            Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

          - `document_index: number`

            minimum: 0

          - `document_title: string`

            maxLength: 500, minLength: 1

          - `end_block_index: number`

            Exclusive 0-based end index of the cited block range in the source's `content` array.

            Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

          - `start_block_index: number`

            0-based index of the first cited block in the source's `content` array.

            minimum: 0

          - `type: "content_block_location"`

        - `citation_web_search_result_location_param: object`

          - `cited_text: string`

          - `encrypted_index: string`

          - `title: string`

            maxLength: 512, minLength: 1

          - `type: "web_search_result_location"`

          - `url: string`

            minLength: 1

        - `citation_search_result_location_param: object`

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

    - `image_block_param: object`

      - `source: Base64ImageSource or URLImageSource or FileImageSource`

        - `base64_image_source: object`

          - `data: string`

            format: byte

          - `media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"`

            - `"image/jpeg"`

            - `"image/png"`

            - `"image/gif"`

            - `"image/webp"`

          - `type: "base64"`

        - `url_image_source: object`

          - `type: "url"`

          - `url: string`

        - `file_image_source: object`

          - `file_id: string`

          - `type: "file"`

      - `type: "image"`

      - `cache_control: optional object`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `transformations: optional object`

        Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

        - `oversized_image: optional "downsize" or "error"`

          What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

          - `"downsize"`

          - `"error"`

    - `document_block_param: object`

      - `source: Base64PDFSource or PlainTextSource or ContentBlockSource or 2 more`

        - `base64_pdf_source: object`

          - `data: string`

            format: byte

          - `media_type: "application/pdf"`

          - `type: "base64"`

        - `plain_text_source: object`

          - `data: string`

          - `media_type: "text/plain"`

          - `type: "text"`

        - `content_block_source: object`

          - `content: string or array of ContentBlockSourceContent`

            - `union_member_0: string`

            - `content_block_source_content: array of ContentBlockSourceContent`

              - `text_block_param: object`

                - `text: string`

                  minLength: 1

                - `type: "text"`

                - `cache_control: optional object`

                  Create a cache control breakpoint at this content block.

                - `citations: optional array of TextCitationParam`

              - `image_block_param: object`

                - `source: Base64ImageSource or URLImageSource or FileImageSource`

                - `type: "image"`

                - `cache_control: optional object`

                  Create a cache control breakpoint at this content block.

                - `transformations: optional object`

                  Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

          - `type: "content"`

        - `url_pdf_source: object`

          - `type: "url"`

          - `url: string`

        - `file_document_source: object`

          - `file_id: string`

          - `type: "file"`

      - `type: "document"`

      - `cache_control: optional object`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `citations: optional object`

        - `enabled: optional boolean`

      - `context: optional string`

        minLength: 1

      - `title: optional string`

        maxLength: 500, minLength: 1

    - `search_result_block_param: object`

      - `content: array of TextBlockParam`

        - `text: string`

          minLength: 1

        - `type: "text"`

        - `cache_control: optional object`

          Create a cache control breakpoint at this content block.

        - `citations: optional array of TextCitationParam`

      - `source: string`

      - `title: string`

      - `type: "search_result"`

      - `cache_control: optional object`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `citations: optional object`

        - `enabled: optional boolean`

    - `thinking_block_param: object`

      - `signature: string`

        The `signature` value of this thinking block, exactly as returned by the API in a previous response. Used to verify that the block was generated by Claude.

        Thinking blocks must be passed back unmodified and in their original order; a modified block results in a 400 `invalid_request_error`.

      - `thinking: string`

        The `thinking` text of this block as returned by the API.

      - `type: "thinking"`

    - `redacted_thinking_block_param: object`

      - `data: string`

        The `data` value of this redacted thinking block, exactly as returned by the API in a previous response. Opaque and encrypted; pass it back unchanged.

      - `type: "redacted_thinking"`

    - `tool_use_block_param: object`

      - `id: string`

        pattern: ^[a-zA-Z0-9_-]+$

      - `input: map[unknown]`

      - `name: string`

        maxLength: 200, minLength: 1

      - `type: "tool_use"`

      - `cache_control: optional object`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `caller: optional DirectCaller or ServerToolCaller or ServerToolCaller20260120`

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

      - `toolset_name: optional string`

        For a toolset member tool_use, the toolset family this member belongs to.

        maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

    - `tool_result_block_param: object`

      - `tool_use_id: string`

        pattern: ^[a-zA-Z0-9_-]+$

      - `type: "tool_result"`

      - `cache_control: optional object`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `content: optional array of TextBlockParam or ImageBlockParam or SearchResultBlockParam or 3 more`

        - `text_block_param: object`

          - `text: string`

            minLength: 1

          - `type: "text"`

          - `cache_control: optional object`

            Create a cache control breakpoint at this content block.

          - `citations: optional array of TextCitationParam`

        - `image_block_param: object`

          - `source: Base64ImageSource or URLImageSource or FileImageSource`

          - `type: "image"`

          - `cache_control: optional object`

            Create a cache control breakpoint at this content block.

          - `transformations: optional object`

            Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

        - `search_result_block_param: object`

          - `content: array of TextBlockParam`

          - `source: string`

          - `title: string`

          - `type: "search_result"`

          - `cache_control: optional object`

            Create a cache control breakpoint at this content block.

          - `citations: optional object`

        - `document_block_param: object`

          - `source: Base64PDFSource or PlainTextSource or ContentBlockSource or 2 more`

          - `type: "document"`

          - `cache_control: optional object`

            Create a cache control breakpoint at this content block.

          - `citations: optional object`

          - `context: optional string`

            minLength: 1

          - `title: optional string`

            maxLength: 500, minLength: 1

        - `tool_reference_block_param: object`

          Tool reference block that can be included in tool_result content.

          - `tool_name: string`

            maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

          - `type: "tool_reference"`

          - `cache_control: optional object`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

            - `ttl: optional "5m" or "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

        - `browser_state_block_param: object`

          The caller's browser state after a browser toolset member call —
          the full inventory of open tabs, which tab is active, and any side
          effects (tabs opened, download state changes) the call produced.

          At most one per `tool_result`, only on a non-error result answering a
          browser toolset member `tool_use`. The server renders the
          model-visible text from it; the model never sees the raw fields.

          - `tabs: array of BrowserStateTabEntry`

            All tabs open in the browser after this call — the full inventory, not a delta. May be empty. Whenever non-empty, exactly one entry carries `active: true`.

            maxItems: 100

            - `tab_id: string`

              The caller-assigned identifier for this tab, unique within the inventory.

              maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

            - `title: string`

              The title of the page the tab is showing. May be empty.

              maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

            - `url: string`

              The URL of the page the tab is showing. May be empty.

              maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

            - `active: optional boolean`

              Whether this tab is the active tab after this call. Whenever `tabs` is non-empty, exactly one entry is marked `active: true`.

          - `type: "browser_state"`

          - `cache_control: optional object`

            Create a cache control breakpoint at this content block.

            - `type: "ephemeral"`

            - `ttl: optional "5m" or "1h"`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

          - `state_changes: optional array of BrowserStateChange`

            Tabs opened and download state changes during this call. "Nothing to report" is expressed by omitting the field, never by an empty list.

            maxItems: 200, minItems: 1

            - `browser_state_change_tab_opened: object`

              A tab this call's execution opened that remains open at its end —
              the creation delta of the `tabs` inventory, not an event log.

              Carries only the `tab_id`; the tab's `title` and `url` live on its
              `tabs` entry, which must include the same `tab_id`. A tab opened
              during a failed call gets no deferred `tab_opened`; it simply appears
              in the next result's `tabs` inventory.

              - `tab_id: string`

                The `tab_id` of the opened tab, present in `tabs`.

                maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

              - `type: "tab_opened"`

            - `browser_state_change_download_started: object`

              A file download that started during this call.

              - `download_id: string`

                The caller-assigned identifier for this download, stable across the state changes reporting it.

                maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

              - `type: "download_started"`

              - `url: string`

                The final post-redirect URL the download was served from.

                maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

            - `browser_state_change_download_completed: object`

              A file download that finished during this call, reported with the
              same `download_id` as its `download_started` — or without a prior
              `download_started`, when the download finished during the call that
              started it (at most one state change per `download_id` per result).

              - `download_id: string`

                The caller-assigned identifier for this download, stable across the state changes reporting it.

                maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

              - `type: "download_completed"`

              - `url: string`

                The final post-redirect URL the download was served from.

                maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

              - `path: optional string`

                Where the executor saved the file, on the executor's filesystem. Only included when another tool in the same environment can read the file at that path.

                pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

              - `size_bytes: optional number`

                The completed download's size.

                minimum: 0

            - `browser_state_change_download_failed: object`

              A file download that failed — or was cancelled — during this call.

              - `download_id: string`

                The caller-assigned identifier for this download, stable across the state changes reporting it.

                maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

              - `type: "download_failed"`

              - `url: string`

                The final post-redirect URL the download was served from.

                maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

              - `error: optional string`

                The failure or cancellation detail, when known.

                pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

      - `is_error: optional boolean`

      - `toolset_name: optional string`

        For a toolset member tool_result, the toolset family of the paired tool_use.

        maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

    - `server_tool_use_block_param: object`

      - `id: string`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

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

      - `cache_control: optional object`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `caller: optional DirectCaller or ServerToolCaller or ServerToolCaller20260120`

        Tool invocation directly from the model.

        - `direct_caller: object`

          Tool invocation directly from the model.

        - `server_tool_caller: object`

          Tool invocation generated by a server-side tool.

        - `server_tool_caller_20260120: object`

    - `web_search_tool_result_block_param: object`

      - `content: array of WebSearchResultBlockParam or WebSearchToolRequestError`

        - `web_search_tool_result_block_item: array of WebSearchResultBlockParam`

          - `encrypted_content: string`

          - `title: string`

          - `type: "web_search_result"`

          - `url: string`

          - `page_age: optional string`

        - `web_search_tool_request_error: object`

          - `error_code: "invalid_tool_input" or "unavailable" or "max_uses_exceeded" or 3 more`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"max_uses_exceeded"`

            - `"too_many_requests"`

            - `"query_too_long"`

            - `"request_too_large"`

          - `type: "web_search_tool_result_error"`

      - `tool_use_id: string`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `type: "web_search_tool_result"`

      - `cache_control: optional object`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `caller: optional DirectCaller or ServerToolCaller or ServerToolCaller20260120`

        Tool invocation directly from the model.

        - `direct_caller: object`

          Tool invocation directly from the model.

        - `server_tool_caller: object`

          Tool invocation generated by a server-side tool.

        - `server_tool_caller_20260120: object`

    - `web_fetch_tool_result_block_param: object`

      - `content: WebFetchToolResultErrorBlockParam or WebFetchBlockParam`

        - `web_fetch_tool_result_error_block_param: object`

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

        - `web_fetch_block_param: object`

          - `content: object`

            - `source: Base64PDFSource or PlainTextSource or ContentBlockSource or 2 more`

            - `type: "document"`

            - `cache_control: optional object`

              Create a cache control breakpoint at this content block.

            - `citations: optional object`

            - `context: optional string`

              minLength: 1

            - `title: optional string`

              maxLength: 500, minLength: 1

          - `type: "web_fetch_result"`

          - `url: string`

            Fetched content URL

          - `retrieved_at: optional string`

            ISO 8601 timestamp when the content was retrieved

      - `tool_use_id: string`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `type: "web_fetch_tool_result"`

      - `cache_control: optional object`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `caller: optional DirectCaller or ServerToolCaller or ServerToolCaller20260120`

        Tool invocation directly from the model.

        - `direct_caller: object`

          Tool invocation directly from the model.

        - `server_tool_caller: object`

          Tool invocation generated by a server-side tool.

        - `server_tool_caller_20260120: object`

    - `code_execution_tool_result_block_param: object`

      - `content: CodeExecutionToolResultErrorParam or CodeExecutionResultBlockParam or EncryptedCodeExecutionResultBlockParam`

        Code execution result with encrypted stdout for PFC + web_search results.

        - `code_execution_tool_result_error_param: object`

          - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"too_many_requests"`

            - `"execution_time_exceeded"`

          - `type: "code_execution_tool_result_error"`

        - `code_execution_result_block_param: object`

          - `content: array of CodeExecutionOutputBlockParam`

            - `file_id: string`

            - `type: "code_execution_output"`

          - `return_code: number`

          - `stderr: string`

          - `stdout: string`

          - `type: "code_execution_result"`

        - `encrypted_code_execution_result_block_param: object`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `content: array of CodeExecutionOutputBlockParam`

            - `file_id: string`

            - `type: "code_execution_output"`

          - `encrypted_stdout: string`

          - `return_code: number`

          - `stderr: string`

          - `type: "encrypted_code_execution_result"`

      - `tool_use_id: string`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `type: "code_execution_tool_result"`

      - `cache_control: optional object`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `bash_code_execution_tool_result_block_param: object`

      - `content: BashCodeExecutionToolResultErrorParam or BashCodeExecutionResultBlockParam`

        - `bash_code_execution_tool_result_error_param: object`

          - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"too_many_requests"`

            - `"execution_time_exceeded"`

            - `"output_file_too_large"`

          - `type: "bash_code_execution_tool_result_error"`

        - `bash_code_execution_result_block_param: object`

          - `content: array of BashCodeExecutionOutputBlockParam`

            - `file_id: string`

            - `type: "bash_code_execution_output"`

          - `return_code: number`

          - `stderr: string`

          - `stdout: string`

          - `type: "bash_code_execution_result"`

      - `tool_use_id: string`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `type: "bash_code_execution_tool_result"`

      - `cache_control: optional object`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `text_editor_code_execution_tool_result_block_param: object`

      - `content: TextEditorCodeExecutionToolResultErrorParam or TextEditorCodeExecutionViewResultBlockParam or TextEditorCodeExecutionCreateResultBlockParam or TextEditorCodeExecutionStrReplaceResultBlockParam`

        - `text_editor_code_execution_tool_result_error_param: object`

          - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"too_many_requests"`

            - `"execution_time_exceeded"`

            - `"file_not_found"`

          - `type: "text_editor_code_execution_tool_result_error"`

          - `error_message: optional string`

        - `text_editor_code_execution_view_result_block_param: object`

          - `content: string`

          - `file_type: "text" or "image" or "pdf"`

            - `"text"`

            - `"image"`

            - `"pdf"`

          - `type: "text_editor_code_execution_view_result"`

          - `num_lines: optional number`

          - `start_line: optional number`

          - `total_lines: optional number`

        - `text_editor_code_execution_create_result_block_param: object`

          - `is_file_update: boolean`

          - `type: "text_editor_code_execution_create_result"`

        - `text_editor_code_execution_str_replace_result_block_param: object`

          - `type: "text_editor_code_execution_str_replace_result"`

          - `lines: optional array of string`

          - `new_lines: optional number`

          - `new_start: optional number`

          - `old_lines: optional number`

          - `old_start: optional number`

      - `tool_use_id: string`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `type: "text_editor_code_execution_tool_result"`

      - `cache_control: optional object`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `tool_search_tool_result_block_param: object`

      - `content: ToolSearchToolResultErrorParam or ToolSearchToolSearchResultBlockParam`

        - `tool_search_tool_result_error_param: object`

          - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

            - `"invalid_tool_input"`

            - `"unavailable"`

            - `"too_many_requests"`

            - `"execution_time_exceeded"`

          - `type: "tool_search_tool_result_error"`

          - `error_message: optional string`

        - `tool_search_tool_search_result_block_param: object`

          - `tool_references: array of ToolReferenceBlockParam`

            - `tool_name: string`

              maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

            - `type: "tool_reference"`

            - `cache_control: optional object`

              Create a cache control breakpoint at this content block.

          - `type: "tool_search_tool_search_result"`

      - `tool_use_id: string`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `type: "tool_search_tool_result"`

      - `cache_control: optional object`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `container_upload_block_param: object`

      A content block that represents a file to be uploaded to the container
      Files uploaded via this block will be available in the container's input directory.

      - `file_id: string`

      - `type: "container_upload"`

      - `cache_control: optional object`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

  - `role: "user" or "assistant" or "system"`

    - `"user"`

    - `"assistant"`

    - `"system"`

### Message Tokens Count

- `message_tokens_count: object`

  - `input_tokens: number`

    The total number of tokens across the provided list of messages, system prompt, and tools.

### Metadata

- `metadata: object`

  - `user_id: optional string`

    An external identifier for the user who is associated with the request.

    This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

    maxLength: 512

### Output Config

- `output_config: object`

  - `effort: optional "low" or "medium" or "high" or 2 more`

    All possible effort levels.

    - `"low"`

    - `"medium"`

    - `"high"`

    - `"xhigh"`

    - `"max"`

  - `format: optional object`

    A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

    - `schema: map[unknown]`

      The JSON schema of the format

    - `type: "json_schema"`

### Output Tokens Details

- `output_tokens_details: object`

  - `thinking_tokens: number`

    Number of output tokens the model generated as internal reasoning, including
    the thinking-block delimiter tokens.

    Reflects the raw reasoning the model produced, not the (possibly shorter)
    summarized thinking text returned in the response body. Computed by
    re-tokenizing the raw reasoning text, so it may differ from the model's exact
    generation count by a small number of tokens. Always ≤ `output_tokens`;
    `output_tokens - thinking_tokens` approximates the non-reasoning output.

    minimum: 0

### Plain Text Source

- `plain_text_source: object`

  - `data: string`

  - `media_type: "text/plain"`

  - `type: "text"`

### Raw Content Block Delta

- `raw_content_block_delta: TextDelta or InputJSONDelta or CitationsDelta or 2 more`

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

### Raw Content Block Delta Event

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

### Raw Content Block Start Event

- `raw_content_block_start_event: object`

  - `content_block: TextBlock or ThinkingBlock or RedactedThinkingBlock or 9 more`

    Response model for a file uploaded to the container.

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

  - `index: number`

  - `type: "content_block_start"`

### Raw Content Block Stop Event

- `raw_content_block_stop_event: object`

  - `index: number`

  - `type: "content_block_stop"`

### Raw Message Delta Event

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

### Raw Message Start Event

- `raw_message_start_event: object`

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

    - `model: "claude-fable-5-1" or "claude-mythos-5-1" or "claude-sonnet-5" or 14 more or string`

      The model that will complete your prompt.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

  - `type: "message_start"`

### Raw Message Stop Event

- `raw_message_stop_event: object`

  - `type: "message_stop"`

### Raw Message Stream Event

- `raw_message_stream_event: RawMessageStartEvent or RawMessageDeltaEvent or RawMessageStopEvent or 3 more`

  - `raw_message_start_event: object`

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

      - `model: "claude-fable-5-1" or "claude-mythos-5-1" or "claude-sonnet-5" or 14 more or string`

        The model that will complete your prompt.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

### Redacted Thinking Block

- `redacted_thinking_block: object`

  - `data: string`

    The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

    Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

    See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

  - `type: "redacted_thinking"`

### Redacted Thinking Block Param

- `redacted_thinking_block_param: object`

  - `data: string`

    The `data` value of this redacted thinking block, exactly as returned by the API in a previous response. Opaque and encrypted; pass it back unchanged.

  - `type: "redacted_thinking"`

### Refusal Stop Details

- `refusal_stop_details: object`

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

### Search Result Block Param

- `search_result_block_param: object`

  - `content: array of TextBlockParam`

    - `text: string`

      minLength: 1

    - `type: "text"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

        - `"5m"`

        - `"1h"`

    - `citations: optional array of TextCitationParam`

      - `citation_char_location_param: object`

        - `cited_text: string`

        - `document_index: number`

          minimum: 0

        - `document_title: string`

          maxLength: 500, minLength: 1

        - `end_char_index: number`

        - `start_char_index: number`

          minimum: 0

        - `type: "char_location"`

      - `citation_page_location_param: object`

        - `cited_text: string`

        - `document_index: number`

          minimum: 0

        - `document_title: string`

          maxLength: 500, minLength: 1

        - `end_page_number: number`

        - `start_page_number: number`

          minimum: 1

        - `type: "page_location"`

      - `citation_content_block_location_param: object`

        - `cited_text: string`

          The full text of the cited block range, concatenated.

          Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

        - `document_index: number`

          minimum: 0

        - `document_title: string`

          maxLength: 500, minLength: 1

        - `end_block_index: number`

          Exclusive 0-based end index of the cited block range in the source's `content` array.

          Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

        - `start_block_index: number`

          0-based index of the first cited block in the source's `content` array.

          minimum: 0

        - `type: "content_block_location"`

      - `citation_web_search_result_location_param: object`

        - `cited_text: string`

        - `encrypted_index: string`

        - `title: string`

          maxLength: 512, minLength: 1

        - `type: "web_search_result_location"`

        - `url: string`

          minLength: 1

      - `citation_search_result_location_param: object`

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

  - `source: string`

  - `title: string`

  - `type: "search_result"`

  - `cache_control: optional object`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

  - `citations: optional object`

    - `enabled: optional boolean`

### Server Tool Caller

- `server_tool_caller: object`

  Tool invocation generated by a server-side tool.

  - `tool_id: string`

    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

  - `type: "code_execution_20250825"`

### Server Tool Caller 20260120

- `server_tool_caller_20260120: object`

  - `tool_id: string`

    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

  - `type: "code_execution_20260120"`

### Server Tool Usage

- `server_tool_usage: object`

  - `web_fetch_requests: number`

    The number of web fetch tool requests.

    minimum: 0

  - `web_search_requests: number`

    The number of web search tool requests.

    minimum: 0

### Server Tool Use Block

- `server_tool_use_block: object`

  - `id: string`

    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

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

  - `name: "web_search" or "web_fetch" or "code_execution" or 4 more`

    - `"web_search"`

    - `"web_fetch"`

    - `"code_execution"`

    - `"bash_code_execution"`

    - `"text_editor_code_execution"`

    - `"tool_search_tool_regex"`

    - `"tool_search_tool_bm25"`

  - `type: "server_tool_use"`

### Server Tool Use Block Param

- `server_tool_use_block_param: object`

  - `id: string`

    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

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

  - `cache_control: optional object`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `"5m"`

      - `"1h"`

  - `caller: optional DirectCaller or ServerToolCaller or ServerToolCaller20260120`

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

### Signature Delta

- `signature_delta: object`

  - `signature: string`

    The `signature` for this thinking block: an opaque value used to verify that the block was generated by Claude when it is passed back to the API. Delivered in a `signature_delta` event just before the block's `content_block_stop` event.

  - `type: "signature_delta"`

### Skill Params

- `skill_params: object`

  Specification for a skill to be loaded in a container (request model).

  - `skill_id: string`

    Skill ID

    maxLength: 64, minLength: 1

  - `type: "anthropic" or "custom"`

    Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

    - `"anthropic"`

    - `"custom"`

  - `version: optional string`

    Skill version or 'latest' for most recent version

    maxLength: 64, minLength: 1

### Stop Reason

- `stop_reason: "end_turn" or "max_tokens" or "stop_sequence" or 4 more`

  - `"end_turn"`

  - `"max_tokens"`

  - `"stop_sequence"`

  - `"tool_use"`

  - `"pause_turn"`

  - `"refusal"`

  - `"model_context_window_exceeded"`

### Text Block

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

### Text Block Param

- `text_block_param: object`

  - `text: string`

    minLength: 1

  - `type: "text"`

  - `cache_control: optional object`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `"5m"`

      - `"1h"`

  - `citations: optional array of TextCitationParam`

    - `citation_char_location_param: object`

      - `cited_text: string`

      - `document_index: number`

        minimum: 0

      - `document_title: string`

        maxLength: 500, minLength: 1

      - `end_char_index: number`

      - `start_char_index: number`

        minimum: 0

      - `type: "char_location"`

    - `citation_page_location_param: object`

      - `cited_text: string`

      - `document_index: number`

        minimum: 0

      - `document_title: string`

        maxLength: 500, minLength: 1

      - `end_page_number: number`

      - `start_page_number: number`

        minimum: 1

      - `type: "page_location"`

    - `citation_content_block_location_param: object`

      - `cited_text: string`

        The full text of the cited block range, concatenated.

        Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

      - `document_index: number`

        minimum: 0

      - `document_title: string`

        maxLength: 500, minLength: 1

      - `end_block_index: number`

        Exclusive 0-based end index of the cited block range in the source's `content` array.

        Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

      - `start_block_index: number`

        0-based index of the first cited block in the source's `content` array.

        minimum: 0

      - `type: "content_block_location"`

    - `citation_web_search_result_location_param: object`

      - `cited_text: string`

      - `encrypted_index: string`

      - `title: string`

        maxLength: 512, minLength: 1

      - `type: "web_search_result_location"`

      - `url: string`

        minLength: 1

    - `citation_search_result_location_param: object`

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

### Text Citation

- `text_citation: CitationCharLocation or CitationPageLocation or CitationContentBlockLocation or 2 more`

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

### Text Citation Param

- `text_citation_param: CitationCharLocationParam or CitationPageLocationParam or CitationContentBlockLocationParam or 2 more`

  - `citation_char_location_param: object`

    - `cited_text: string`

    - `document_index: number`

      minimum: 0

    - `document_title: string`

      maxLength: 500, minLength: 1

    - `end_char_index: number`

    - `start_char_index: number`

      minimum: 0

    - `type: "char_location"`

  - `citation_page_location_param: object`

    - `cited_text: string`

    - `document_index: number`

      minimum: 0

    - `document_title: string`

      maxLength: 500, minLength: 1

    - `end_page_number: number`

    - `start_page_number: number`

      minimum: 1

    - `type: "page_location"`

  - `citation_content_block_location_param: object`

    - `cited_text: string`

      The full text of the cited block range, concatenated.

      Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

    - `document_index: number`

      minimum: 0

    - `document_title: string`

      maxLength: 500, minLength: 1

    - `end_block_index: number`

      Exclusive 0-based end index of the cited block range in the source's `content` array.

      Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

    - `start_block_index: number`

      0-based index of the first cited block in the source's `content` array.

      minimum: 0

    - `type: "content_block_location"`

  - `citation_web_search_result_location_param: object`

    - `cited_text: string`

    - `encrypted_index: string`

    - `title: string`

      maxLength: 512, minLength: 1

    - `type: "web_search_result_location"`

    - `url: string`

      minLength: 1

  - `citation_search_result_location_param: object`

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

### Text Delta

- `text_delta: object`

  - `text: string`

  - `type: "text_delta"`

### Text Editor Code Execution Create Result Block

- `text_editor_code_execution_create_result_block: object`

  - `is_file_update: boolean`

  - `type: "text_editor_code_execution_create_result"`

### Text Editor Code Execution Create Result Block Param

- `text_editor_code_execution_create_result_block_param: object`

  - `is_file_update: boolean`

  - `type: "text_editor_code_execution_create_result"`

### Text Editor Code Execution Str Replace Result Block

- `text_editor_code_execution_str_replace_result_block: object`

  - `lines: array of string`

  - `new_lines: number`

  - `new_start: number`

  - `old_lines: number`

  - `old_start: number`

  - `type: "text_editor_code_execution_str_replace_result"`

### Text Editor Code Execution Str Replace Result Block Param

- `text_editor_code_execution_str_replace_result_block_param: object`

  - `type: "text_editor_code_execution_str_replace_result"`

  - `lines: optional array of string`

  - `new_lines: optional number`

  - `new_start: optional number`

  - `old_lines: optional number`

  - `old_start: optional number`

### Text Editor Code Execution Tool Result Block

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

### Text Editor Code Execution Tool Result Block Param

- `text_editor_code_execution_tool_result_block_param: object`

  - `content: TextEditorCodeExecutionToolResultErrorParam or TextEditorCodeExecutionViewResultBlockParam or TextEditorCodeExecutionCreateResultBlockParam or TextEditorCodeExecutionStrReplaceResultBlockParam`

    - `text_editor_code_execution_tool_result_error_param: object`

      - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

        - `"invalid_tool_input"`

        - `"unavailable"`

        - `"too_many_requests"`

        - `"execution_time_exceeded"`

        - `"file_not_found"`

      - `type: "text_editor_code_execution_tool_result_error"`

      - `error_message: optional string`

    - `text_editor_code_execution_view_result_block_param: object`

      - `content: string`

      - `file_type: "text" or "image" or "pdf"`

        - `"text"`

        - `"image"`

        - `"pdf"`

      - `type: "text_editor_code_execution_view_result"`

      - `num_lines: optional number`

      - `start_line: optional number`

      - `total_lines: optional number`

    - `text_editor_code_execution_create_result_block_param: object`

      - `is_file_update: boolean`

      - `type: "text_editor_code_execution_create_result"`

    - `text_editor_code_execution_str_replace_result_block_param: object`

      - `type: "text_editor_code_execution_str_replace_result"`

      - `lines: optional array of string`

      - `new_lines: optional number`

      - `new_start: optional number`

      - `old_lines: optional number`

      - `old_start: optional number`

  - `tool_use_id: string`

    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

  - `type: "text_editor_code_execution_tool_result"`

  - `cache_control: optional object`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `"5m"`

      - `"1h"`

### Text Editor Code Execution Tool Result Error

- `text_editor_code_execution_tool_result_error: object`

  - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

    - `"invalid_tool_input"`

    - `"unavailable"`

    - `"too_many_requests"`

    - `"execution_time_exceeded"`

    - `"file_not_found"`

  - `error_message: string`

  - `type: "text_editor_code_execution_tool_result_error"`

### Text Editor Code Execution Tool Result Error Code

- `text_editor_code_execution_tool_result_error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

  - `"invalid_tool_input"`

  - `"unavailable"`

  - `"too_many_requests"`

  - `"execution_time_exceeded"`

  - `"file_not_found"`

### Text Editor Code Execution Tool Result Error Param

- `text_editor_code_execution_tool_result_error_param: object`

  - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more`

    - `"invalid_tool_input"`

    - `"unavailable"`

    - `"too_many_requests"`

    - `"execution_time_exceeded"`

    - `"file_not_found"`

  - `type: "text_editor_code_execution_tool_result_error"`

  - `error_message: optional string`

### Text Editor Code Execution View Result Block

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

### Text Editor Code Execution View Result Block Param

- `text_editor_code_execution_view_result_block_param: object`

  - `content: string`

  - `file_type: "text" or "image" or "pdf"`

    - `"text"`

    - `"image"`

    - `"pdf"`

  - `type: "text_editor_code_execution_view_result"`

  - `num_lines: optional number`

  - `start_line: optional number`

  - `total_lines: optional number`

### Thinking Block

- `thinking_block: object`

  - `signature: string`

    A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

    This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

    See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

  - `thinking: string`

    The text of Claude's thinking process for this block.

  - `type: "thinking"`

### Thinking Block Param

- `thinking_block_param: object`

  - `signature: string`

    The `signature` value of this thinking block, exactly as returned by the API in a previous response. Used to verify that the block was generated by Claude.

    Thinking blocks must be passed back unmodified and in their original order; a modified block results in a 400 `invalid_request_error`.

  - `thinking: string`

    The `thinking` text of this block as returned by the API.

  - `type: "thinking"`

### Thinking Config Adaptive

- `thinking_config_adaptive: object`

  - `type: "adaptive"`

  - `display: optional "summarized" or "omitted"`

    Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

    - `"summarized"`

    - `"omitted"`

### Thinking Config Disabled

- `thinking_config_disabled: object`

  - `type: "disabled"`

### Thinking Config Enabled

- `thinking_config_enabled: object`

  - `budget_tokens: number`

    Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

    Must be ≥1024 and less than `max_tokens`.

    See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

    minimum: 1024

  - `type: "enabled"`

  - `display: optional "summarized" or "omitted"`

    Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

    - `"summarized"`

    - `"omitted"`

### Thinking Config Param

- `thinking_config_param: ThinkingConfigEnabled or ThinkingConfigDisabled or ThinkingConfigAdaptive`

  Configuration for enabling Claude's extended thinking.

  When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

  See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

  - `thinking_config_enabled: object`

    - `budget_tokens: number`

      Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

      Must be ≥1024 and less than `max_tokens`.

      See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

      minimum: 1024

    - `type: "enabled"`

    - `display: optional "summarized" or "omitted"`

      Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

      - `"summarized"`

      - `"omitted"`

  - `thinking_config_disabled: object`

    - `type: "disabled"`

  - `thinking_config_adaptive: object`

    - `type: "adaptive"`

    - `display: optional "summarized" or "omitted"`

      Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

      - `"summarized"`

      - `"omitted"`

### Thinking Delta

- `thinking_delta: object`

  - `thinking: string`

    The incremental `thinking` text for this content block. Concatenate the `thinking` values of successive `thinking_delta` events to assemble the block's full `thinking` value.

  - `type: "thinking_delta"`

### Tool

- `tool: object`

  - `input_schema: object`

    [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

    This defines the shape of the `input` that your tool accepts and that the model will produce.

    - `type: "object"`

    - `properties: optional map[unknown]`

    - `required: optional array of string`

  - `name: string`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

    maxLength: 128, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,128}$

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

    - `"code_execution_20260521"`

  - `cache_control: optional object`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `"5m"`

      - `"1h"`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `description: optional string`

    Description of what this tool does.

    Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

  - `eager_input_streaming: optional boolean`

    Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

  - `input_examples: optional array of map[unknown]`

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

  - `type: optional "custom"`

### Tool Bash 20250124

- `tool_bash_20250124: object`

  - `name: "bash"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `type: "bash_20250124"`

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

    - `"code_execution_20260521"`

  - `cache_control: optional object`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `"5m"`

      - `"1h"`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `input_examples: optional array of map[unknown]`

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

### Tool Choice

- `tool_choice: ToolChoiceAuto or ToolChoiceAny or ToolChoiceTool or ToolChoiceNone`

  How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

  - `tool_choice_auto: object`

    The model will automatically decide whether to use tools.

    - `type: "auto"`

    - `disable_parallel_tool_use: optional boolean`

      Whether to disable parallel tool use.

      Defaults to `false`. If set to `true`, the model will output at most one tool use.

  - `tool_choice_any: object`

    The model will use any available tools.

    - `type: "any"`

    - `disable_parallel_tool_use: optional boolean`

      Whether to disable parallel tool use.

      Defaults to `false`. If set to `true`, the model will output exactly one tool use.

  - `tool_choice_tool: object`

    The model will use the specified tool with `tool_choice.name`.

    - `name: string`

      The name of the tool to use.

    - `type: "tool"`

    - `disable_parallel_tool_use: optional boolean`

      Whether to disable parallel tool use.

      Defaults to `false`. If set to `true`, the model will output exactly one tool use.

  - `tool_choice_none: object`

    The model will not be allowed to use tools.

    - `type: "none"`

### Tool Choice Any

- `tool_choice_any: object`

  The model will use any available tools.

  - `type: "any"`

  - `disable_parallel_tool_use: optional boolean`

    Whether to disable parallel tool use.

    Defaults to `false`. If set to `true`, the model will output exactly one tool use.

### Tool Choice Auto

- `tool_choice_auto: object`

  The model will automatically decide whether to use tools.

  - `type: "auto"`

  - `disable_parallel_tool_use: optional boolean`

    Whether to disable parallel tool use.

    Defaults to `false`. If set to `true`, the model will output at most one tool use.

### Tool Choice None

- `tool_choice_none: object`

  The model will not be allowed to use tools.

  - `type: "none"`

### Tool Choice Tool

- `tool_choice_tool: object`

  The model will use the specified tool with `tool_choice.name`.

  - `name: string`

    The name of the tool to use.

  - `type: "tool"`

  - `disable_parallel_tool_use: optional boolean`

    Whether to disable parallel tool use.

    Defaults to `false`. If set to `true`, the model will output exactly one tool use.

### Tool Reference Block

- `tool_reference_block: object`

  - `tool_name: string`

    maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

  - `type: "tool_reference"`

### Tool Reference Block Param

- `tool_reference_block_param: object`

  Tool reference block that can be included in tool_result content.

  - `tool_name: string`

    maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

  - `type: "tool_reference"`

  - `cache_control: optional object`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `"5m"`

      - `"1h"`

### Tool Result Block Param

- `tool_result_block_param: object`

  - `tool_use_id: string`

    pattern: ^[a-zA-Z0-9_-]+$

  - `type: "tool_result"`

  - `cache_control: optional object`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `"5m"`

      - `"1h"`

  - `content: optional array of TextBlockParam or ImageBlockParam or SearchResultBlockParam or 3 more`

    - `text_block_param: object`

      - `text: string`

        minLength: 1

      - `type: "text"`

      - `cache_control: optional object`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `citations: optional array of TextCitationParam`

        - `citation_char_location_param: object`

          - `cited_text: string`

          - `document_index: number`

            minimum: 0

          - `document_title: string`

            maxLength: 500, minLength: 1

          - `end_char_index: number`

          - `start_char_index: number`

            minimum: 0

          - `type: "char_location"`

        - `citation_page_location_param: object`

          - `cited_text: string`

          - `document_index: number`

            minimum: 0

          - `document_title: string`

            maxLength: 500, minLength: 1

          - `end_page_number: number`

          - `start_page_number: number`

            minimum: 1

          - `type: "page_location"`

        - `citation_content_block_location_param: object`

          - `cited_text: string`

            The full text of the cited block range, concatenated.

            Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

          - `document_index: number`

            minimum: 0

          - `document_title: string`

            maxLength: 500, minLength: 1

          - `end_block_index: number`

            Exclusive 0-based end index of the cited block range in the source's `content` array.

            Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

          - `start_block_index: number`

            0-based index of the first cited block in the source's `content` array.

            minimum: 0

          - `type: "content_block_location"`

        - `citation_web_search_result_location_param: object`

          - `cited_text: string`

          - `encrypted_index: string`

          - `title: string`

            maxLength: 512, minLength: 1

          - `type: "web_search_result_location"`

          - `url: string`

            minLength: 1

        - `citation_search_result_location_param: object`

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

    - `image_block_param: object`

      - `source: Base64ImageSource or URLImageSource or FileImageSource`

        - `base64_image_source: object`

          - `data: string`

            format: byte

          - `media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"`

            - `"image/jpeg"`

            - `"image/png"`

            - `"image/gif"`

            - `"image/webp"`

          - `type: "base64"`

        - `url_image_source: object`

          - `type: "url"`

          - `url: string`

        - `file_image_source: object`

          - `file_id: string`

          - `type: "file"`

      - `type: "image"`

      - `cache_control: optional object`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `transformations: optional object`

        Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

        - `oversized_image: optional "downsize" or "error"`

          What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

          - `"downsize"`

          - `"error"`

    - `search_result_block_param: object`

      - `content: array of TextBlockParam`

        - `text: string`

          minLength: 1

        - `type: "text"`

        - `cache_control: optional object`

          Create a cache control breakpoint at this content block.

        - `citations: optional array of TextCitationParam`

      - `source: string`

      - `title: string`

      - `type: "search_result"`

      - `cache_control: optional object`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `citations: optional object`

        - `enabled: optional boolean`

    - `document_block_param: object`

      - `source: Base64PDFSource or PlainTextSource or ContentBlockSource or 2 more`

        - `base64_pdf_source: object`

          - `data: string`

            format: byte

          - `media_type: "application/pdf"`

          - `type: "base64"`

        - `plain_text_source: object`

          - `data: string`

          - `media_type: "text/plain"`

          - `type: "text"`

        - `content_block_source: object`

          - `content: string or array of ContentBlockSourceContent`

            - `union_member_0: string`

            - `content_block_source_content: array of ContentBlockSourceContent`

              - `text_block_param: object`

                - `text: string`

                  minLength: 1

                - `type: "text"`

                - `cache_control: optional object`

                  Create a cache control breakpoint at this content block.

                - `citations: optional array of TextCitationParam`

              - `image_block_param: object`

                - `source: Base64ImageSource or URLImageSource or FileImageSource`

                - `type: "image"`

                - `cache_control: optional object`

                  Create a cache control breakpoint at this content block.

                - `transformations: optional object`

                  Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

          - `type: "content"`

        - `url_pdf_source: object`

          - `type: "url"`

          - `url: string`

        - `file_document_source: object`

          - `file_id: string`

          - `type: "file"`

      - `type: "document"`

      - `cache_control: optional object`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `citations: optional object`

        - `enabled: optional boolean`

      - `context: optional string`

        minLength: 1

      - `title: optional string`

        maxLength: 500, minLength: 1

    - `tool_reference_block_param: object`

      Tool reference block that can be included in tool_result content.

      - `tool_name: string`

        maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

      - `type: "tool_reference"`

      - `cache_control: optional object`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `browser_state_block_param: object`

      The caller's browser state after a browser toolset member call —
      the full inventory of open tabs, which tab is active, and any side
      effects (tabs opened, download state changes) the call produced.

      At most one per `tool_result`, only on a non-error result answering a
      browser toolset member `tool_use`. The server renders the
      model-visible text from it; the model never sees the raw fields.

      - `tabs: array of BrowserStateTabEntry`

        All tabs open in the browser after this call — the full inventory, not a delta. May be empty. Whenever non-empty, exactly one entry carries `active: true`.

        maxItems: 100

        - `tab_id: string`

          The caller-assigned identifier for this tab, unique within the inventory.

          maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

        - `title: string`

          The title of the page the tab is showing. May be empty.

          maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

        - `url: string`

          The URL of the page the tab is showing. May be empty.

          maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

        - `active: optional boolean`

          Whether this tab is the active tab after this call. Whenever `tabs` is non-empty, exactly one entry is marked `active: true`.

      - `type: "browser_state"`

      - `cache_control: optional object`

        Create a cache control breakpoint at this content block.

        - `type: "ephemeral"`

        - `ttl: optional "5m" or "1h"`

          The time-to-live for the cache control breakpoint.

          This may be one the following values:

          - `5m`: 5 minutes
          - `1h`: 1 hour

          Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `state_changes: optional array of BrowserStateChange`

        Tabs opened and download state changes during this call. "Nothing to report" is expressed by omitting the field, never by an empty list.

        maxItems: 200, minItems: 1

        - `browser_state_change_tab_opened: object`

          A tab this call's execution opened that remains open at its end —
          the creation delta of the `tabs` inventory, not an event log.

          Carries only the `tab_id`; the tab's `title` and `url` live on its
          `tabs` entry, which must include the same `tab_id`. A tab opened
          during a failed call gets no deferred `tab_opened`; it simply appears
          in the next result's `tabs` inventory.

          - `tab_id: string`

            The `tab_id` of the opened tab, present in `tabs`.

            maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

          - `type: "tab_opened"`

        - `browser_state_change_download_started: object`

          A file download that started during this call.

          - `download_id: string`

            The caller-assigned identifier for this download, stable across the state changes reporting it.

            maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

          - `type: "download_started"`

          - `url: string`

            The final post-redirect URL the download was served from.

            maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

        - `browser_state_change_download_completed: object`

          A file download that finished during this call, reported with the
          same `download_id` as its `download_started` — or without a prior
          `download_started`, when the download finished during the call that
          started it (at most one state change per `download_id` per result).

          - `download_id: string`

            The caller-assigned identifier for this download, stable across the state changes reporting it.

            maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

          - `type: "download_completed"`

          - `url: string`

            The final post-redirect URL the download was served from.

            maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

          - `path: optional string`

            Where the executor saved the file, on the executor's filesystem. Only included when another tool in the same environment can read the file at that path.

            pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

          - `size_bytes: optional number`

            The completed download's size.

            minimum: 0

        - `browser_state_change_download_failed: object`

          A file download that failed — or was cancelled — during this call.

          - `download_id: string`

            The caller-assigned identifier for this download, stable across the state changes reporting it.

            maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

          - `type: "download_failed"`

          - `url: string`

            The final post-redirect URL the download was served from.

            maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

          - `error: optional string`

            The failure or cancellation detail, when known.

            pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

  - `is_error: optional boolean`

  - `toolset_name: optional string`

    For a toolset member tool_result, the toolset family of the paired tool_use.

    maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

### Tool Search Tool Bm25 20251119

- `tool_search_tool_bm25_20251119: object`

  - `name: "tool_search_tool_bm25"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `type: "tool_search_tool_bm25_20251119" or "tool_search_tool_bm25"`

    - `"tool_search_tool_bm25_20251119"`

    - `"tool_search_tool_bm25"`

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

    - `"code_execution_20260521"`

  - `cache_control: optional object`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `"5m"`

      - `"1h"`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

### Tool Search Tool Regex 20251119

- `tool_search_tool_regex_20251119: object`

  - `name: "tool_search_tool_regex"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `type: "tool_search_tool_regex_20251119" or "tool_search_tool_regex"`

    - `"tool_search_tool_regex_20251119"`

    - `"tool_search_tool_regex"`

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

    - `"code_execution_20260521"`

  - `cache_control: optional object`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `"5m"`

      - `"1h"`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

### Tool Search Tool Result Block

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

### Tool Search Tool Result Block Param

- `tool_search_tool_result_block_param: object`

  - `content: ToolSearchToolResultErrorParam or ToolSearchToolSearchResultBlockParam`

    - `tool_search_tool_result_error_param: object`

      - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

        - `"invalid_tool_input"`

        - `"unavailable"`

        - `"too_many_requests"`

        - `"execution_time_exceeded"`

      - `type: "tool_search_tool_result_error"`

      - `error_message: optional string`

    - `tool_search_tool_search_result_block_param: object`

      - `tool_references: array of ToolReferenceBlockParam`

        - `tool_name: string`

          maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

        - `type: "tool_reference"`

        - `cache_control: optional object`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

          - `ttl: optional "5m" or "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

            - `"5m"`

            - `"1h"`

      - `type: "tool_search_tool_search_result"`

  - `tool_use_id: string`

    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

  - `type: "tool_search_tool_result"`

  - `cache_control: optional object`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

### Tool Search Tool Result Error

- `tool_search_tool_result_error: object`

  - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

    - `"invalid_tool_input"`

    - `"unavailable"`

    - `"too_many_requests"`

    - `"execution_time_exceeded"`

  - `error_message: string`

  - `type: "tool_search_tool_result_error"`

### Tool Search Tool Result Error Code

- `tool_search_tool_result_error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

  - `"invalid_tool_input"`

  - `"unavailable"`

  - `"too_many_requests"`

  - `"execution_time_exceeded"`

### Tool Search Tool Result Error Param

- `tool_search_tool_result_error_param: object`

  - `error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"`

    - `"invalid_tool_input"`

    - `"unavailable"`

    - `"too_many_requests"`

    - `"execution_time_exceeded"`

  - `type: "tool_search_tool_result_error"`

  - `error_message: optional string`

### Tool Search Tool Search Result Block

- `tool_search_tool_search_result_block: object`

  - `tool_references: array of ToolReferenceBlock`

    - `tool_name: string`

      maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

    - `type: "tool_reference"`

  - `type: "tool_search_tool_search_result"`

### Tool Search Tool Search Result Block Param

- `tool_search_tool_search_result_block_param: object`

  - `tool_references: array of ToolReferenceBlockParam`

    - `tool_name: string`

      maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

    - `type: "tool_reference"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

        - `"5m"`

        - `"1h"`

  - `type: "tool_search_tool_search_result"`

### Tool Text Editor 20250124

- `tool_text_editor_20250124: object`

  - `name: "str_replace_editor"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `type: "text_editor_20250124"`

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

    - `"code_execution_20260521"`

  - `cache_control: optional object`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `"5m"`

      - `"1h"`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `input_examples: optional array of map[unknown]`

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

### Tool Text Editor 20250429

- `tool_text_editor_20250429: object`

  - `name: "str_replace_based_edit_tool"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `type: "text_editor_20250429"`

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

    - `"code_execution_20260521"`

  - `cache_control: optional object`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `"5m"`

      - `"1h"`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `input_examples: optional array of map[unknown]`

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

### Tool Text Editor 20250728

- `tool_text_editor_20250728: object`

  - `name: "str_replace_based_edit_tool"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `type: "text_editor_20250728"`

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

    - `"code_execution_20260521"`

  - `cache_control: optional object`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `"5m"`

      - `"1h"`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `input_examples: optional array of map[unknown]`

  - `max_characters: optional number`

    Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

    minimum: 1

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

### Tool Union

- `tool_union: Tool or ToolBash20250124 or CodeExecutionTool20250522 or 18 more`

  Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

  - `tool: object`

    - `input_schema: object`

      [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

      This defines the shape of the `input` that your tool accepts and that the model will produce.

      - `type: "object"`

      - `properties: optional map[unknown]`

      - `required: optional array of string`

    - `name: string`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

      maxLength: 128, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,128}$

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

        - `"5m"`

        - `"1h"`

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `description: optional string`

      Description of what this tool does.

      Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

    - `eager_input_streaming: optional boolean`

      Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

    - `input_examples: optional array of map[unknown]`

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

    - `type: optional "custom"`

  - `tool_bash_20250124: object`

    - `name: "bash"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "bash_20250124"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples: optional array of map[unknown]`

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `code_execution_tool_20250522: object`

    - `name: "code_execution"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "code_execution_20250522"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `code_execution_tool_20250825: object`

    - `name: "code_execution"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "code_execution_20250825"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `code_execution_tool_20260120: object`

    Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

    - `name: "code_execution"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "code_execution_20260120"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `code_execution_tool_20260521: object`

    Code execution tool with REPL state persistence.

    - `name: "code_execution"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "code_execution_20260521"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `browser_toolset_20260801: object`

    The browser toolset: a single `tools[]` entry (carrying no
    `name`) that declares the browser tool family. The model is served
    the family's tool with any members disabled via `configs` removed
    from its schema.

    - `type: "browser_toolset_20260801"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `configs: optional object`

      Per-member configuration for `browser_toolset_20260801`: one
      optional field per member tool, keyed by the member name — the same
      name the member's `tool_use` blocks carry. Every member is an
      accepted key, and a member's defaults apply wherever its key is
      absent. Unknown keys are rejected: the field set is this toolset
      version's complete member set.

      - `close_tab: optional object`

        `close_tab`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `double_click: optional object`

        `double_click`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `file_upload: optional object`

        `file_upload`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `find: optional object`

        `find`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `form_input: optional object`

        `form_input`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `get_page_text: optional object`

        `get_page_text`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `hold_key: optional object`

        `hold_key`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `hover: optional object`

        `hover`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `javascript_exec: optional object`

        `javascript_exec`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `key: optional object`

        `key`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `left_click: optional object`

        `left_click`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `left_click_drag: optional object`

        `left_click_drag`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `left_mouse_down: optional object`

        `left_mouse_down`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `left_mouse_up: optional object`

        `left_mouse_up`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `list_tabs: optional object`

        `list_tabs`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `middle_click: optional object`

        `middle_click`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `mouse_move: optional object`

        `mouse_move`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `navigate: optional object`

        `navigate`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `new_tab: optional object`

        `new_tab`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `read_console: optional object`

        `read_console`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `read_network: optional object`

        `read_network`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `read_page: optional object`

        `read_page`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `right_click: optional object`

        `right_click`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `screenshot: optional object`

        `screenshot`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `scroll: optional object`

        `scroll`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `scroll_to: optional object`

        `scroll_to`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `switch_tab: optional object`

        `switch_tab`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `triple_click: optional object`

        `triple_click`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `type: optional object`

        `type`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `wait: optional object`

        `wait`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `zoom: optional object`

        `zoom`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `memory_tool_20250818: object`

    - `name: "memory"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "memory_20250818"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples: optional array of map[unknown]`

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `computer_toolset_20260801: object`

    The computer toolset: a single `tools[]` entry (carrying no
    `name`) that declares the computer tool family. The model is
    served the family's tool with any members disabled via `configs`
    removed from its schema. Every member is enabled by default, zoom
    included. The single-tool options `display_number` and
    `enable_zoom` are not fields of a toolset entry — it carries only
    `type`, `configs`, and `cache_control`; zoom is controlled
    via `configs.zoom.enabled`.

    - `type: "computer_toolset_20260801"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `configs: optional object`

      Per-member configuration for `computer_toolset_20260801`: one
      optional field per member tool, keyed by the member name — the same
      name the member's `tool_use` blocks carry. Every member is an
      accepted key, and a member's defaults apply wherever its key is
      absent. Unknown keys are rejected: the field set is this toolset
      version's complete member set.

      - `cursor_position: optional object`

        `cursor_position`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `double_click: optional object`

        `double_click`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `hold_key: optional object`

        `hold_key`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `key: optional object`

        `key`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `left_click: optional object`

        `left_click`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `left_click_drag: optional object`

        `left_click_drag`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `left_mouse_down: optional object`

        `left_mouse_down`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `left_mouse_up: optional object`

        `left_mouse_up`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `middle_click: optional object`

        `middle_click`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `mouse_move: optional object`

        `mouse_move`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `right_click: optional object`

        `right_click`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `screenshot: optional object`

        `screenshot`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `scroll: optional object`

        `scroll`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `triple_click: optional object`

        `triple_click`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `type: optional object`

        `type`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `wait: optional object`

        `wait`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

      - `zoom: optional object`

        `zoom`'s config overrides.

        - `defer_loading: optional boolean`

          Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

        - `enabled: optional boolean`

          Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

  - `tool_text_editor_20250124: object`

    - `name: "str_replace_editor"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "text_editor_20250124"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples: optional array of map[unknown]`

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `tool_text_editor_20250429: object`

    - `name: "str_replace_based_edit_tool"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "text_editor_20250429"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples: optional array of map[unknown]`

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `tool_text_editor_20250728: object`

    - `name: "str_replace_based_edit_tool"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "text_editor_20250728"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `input_examples: optional array of map[unknown]`

    - `max_characters: optional number`

      Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

      minimum: 1

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `web_search_tool_20250305: object`

    - `name: "web_search"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "web_search_20250305"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `allowed_domains: optional array of string`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `blocked_domains: optional array of string`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_uses: optional number`

      Maximum number of times the tool can be used in the API request.

      exclusiveMinimum: 0

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

    - `user_location: optional object`

      Parameters for the user's location. Used to provide more relevant search results.

      - `type: "approximate"`

      - `city: optional string`

        The city of the user.

        maxLength: 255, minLength: 1

      - `country: optional string`

        The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

        maxLength: 2, minLength: 2

      - `region: optional string`

        The region of the user.

        maxLength: 255, minLength: 1

      - `timezone: optional string`

        The [IANA timezone](https://nodatime.org/TimeZones) of the user.

        maxLength: 255, minLength: 1

  - `web_fetch_tool_20250910: object`

    - `name: "web_fetch"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "web_fetch_20250910"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `allowed_domains: optional array of string`

      List of domains to allow fetching from

    - `blocked_domains: optional array of string`

      List of domains to block fetching from

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `citations: optional object`

      Citations configuration for fetched documents. Citations are disabled by default.

      - `enabled: optional boolean`

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_content_tokens: optional number`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

      exclusiveMinimum: 0

    - `max_uses: optional number`

      Maximum number of times the tool can be used in the API request.

      exclusiveMinimum: 0

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `web_search_tool_20260209: object`

    - `name: "web_search"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "web_search_20260209"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `allowed_domains: optional array of string`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `blocked_domains: optional array of string`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_uses: optional number`

      Maximum number of times the tool can be used in the API request.

      exclusiveMinimum: 0

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

    - `user_location: optional object`

      Parameters for the user's location. Used to provide more relevant search results.

      - `type: "approximate"`

      - `city: optional string`

        The city of the user.

        maxLength: 255, minLength: 1

      - `country: optional string`

        The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

        maxLength: 2, minLength: 2

      - `region: optional string`

        The region of the user.

        maxLength: 255, minLength: 1

      - `timezone: optional string`

        The [IANA timezone](https://nodatime.org/TimeZones) of the user.

        maxLength: 255, minLength: 1

  - `web_fetch_tool_20260209: object`

    - `name: "web_fetch"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "web_fetch_20260209"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `allowed_domains: optional array of string`

      List of domains to allow fetching from

    - `blocked_domains: optional array of string`

      List of domains to block fetching from

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `citations: optional object`

      Citations configuration for fetched documents. Citations are disabled by default.

      - `enabled: optional boolean`

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_content_tokens: optional number`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

      exclusiveMinimum: 0

    - `max_uses: optional number`

      Maximum number of times the tool can be used in the API request.

      exclusiveMinimum: 0

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `web_fetch_tool_20260309: object`

    Web fetch tool with use_cache parameter for bypassing cached content.

    - `name: "web_fetch"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "web_fetch_20260309"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `allowed_domains: optional array of string`

      List of domains to allow fetching from

    - `blocked_domains: optional array of string`

      List of domains to block fetching from

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `citations: optional object`

      Citations configuration for fetched documents. Citations are disabled by default.

      - `enabled: optional boolean`

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_content_tokens: optional number`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

      exclusiveMinimum: 0

    - `max_uses: optional number`

      Maximum number of times the tool can be used in the API request.

      exclusiveMinimum: 0

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

    - `use_cache: optional boolean`

      Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

  - `web_search_tool_20260318: object`

    - `name: "web_search"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "web_search_20260318"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `allowed_domains: optional array of string`

      If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

    - `blocked_domains: optional array of string`

      If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_uses: optional number`

      Maximum number of times the tool can be used in the API request.

      exclusiveMinimum: 0

    - `response_inclusion: optional "full" or "excluded"`

      How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

      - `"full"`

      - `"excluded"`

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

    - `user_location: optional object`

      Parameters for the user's location. Used to provide more relevant search results.

      - `type: "approximate"`

      - `city: optional string`

        The city of the user.

        maxLength: 255, minLength: 1

      - `country: optional string`

        The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

        maxLength: 2, minLength: 2

      - `region: optional string`

        The region of the user.

        maxLength: 255, minLength: 1

      - `timezone: optional string`

        The [IANA timezone](https://nodatime.org/TimeZones) of the user.

        maxLength: 255, minLength: 1

  - `web_fetch_tool_20260318: object`

    - `name: "web_fetch"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "web_fetch_20260318"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `allowed_domains: optional array of string`

      List of domains to allow fetching from

    - `blocked_domains: optional array of string`

      List of domains to block fetching from

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `citations: optional object`

      Citations configuration for fetched documents. Citations are disabled by default.

      - `enabled: optional boolean`

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `max_content_tokens: optional number`

      Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

      exclusiveMinimum: 0

    - `max_uses: optional number`

      Maximum number of times the tool can be used in the API request.

      exclusiveMinimum: 0

    - `response_inclusion: optional "full" or "excluded"`

      How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

      - `"full"`

      - `"excluded"`

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

    - `use_cache: optional boolean`

      Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

  - `tool_search_tool_bm25_20251119: object`

    - `name: "tool_search_tool_bm25"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "tool_search_tool_bm25_20251119" or "tool_search_tool_bm25"`

      - `"tool_search_tool_bm25_20251119"`

      - `"tool_search_tool_bm25"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

  - `tool_search_tool_regex_20251119: object`

    - `name: "tool_search_tool_regex"`

      Name of the tool.

      This is how the tool will be called by the model and in `tool_use` blocks.

    - `type: "tool_search_tool_regex_20251119" or "tool_search_tool_regex"`

      - `"tool_search_tool_regex_20251119"`

      - `"tool_search_tool_regex"`

    - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

      - `"direct"`

      - `"code_execution_20250825"`

      - `"code_execution_20260120"`

      - `"code_execution_20260521"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `defer_loading: optional boolean`

      If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

    - `strict: optional boolean`

      When true, guarantees schema validation on tool names and inputs

### Tool Use Block

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

### Tool Use Block Param

- `tool_use_block_param: object`

  - `id: string`

    pattern: ^[a-zA-Z0-9_-]+$

  - `input: map[unknown]`

  - `name: string`

    maxLength: 200, minLength: 1

  - `type: "tool_use"`

  - `cache_control: optional object`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `"5m"`

      - `"1h"`

  - `caller: optional DirectCaller or ServerToolCaller or ServerToolCaller20260120`

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

  - `toolset_name: optional string`

    For a toolset member tool_use, the toolset family this member belongs to.

    maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

### URL Image Source

- `url_image_source: object`

  - `type: "url"`

  - `url: string`

### URL PDF Source

- `url_pdf_source: object`

  - `type: "url"`

  - `url: string`

### Usage

- `usage: object`

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

### User Location

- `user_location: object`

  - `type: "approximate"`

  - `city: optional string`

    The city of the user.

    maxLength: 255, minLength: 1

  - `country: optional string`

    The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

    maxLength: 2, minLength: 2

  - `region: optional string`

    The region of the user.

    maxLength: 255, minLength: 1

  - `timezone: optional string`

    The [IANA timezone](https://nodatime.org/TimeZones) of the user.

    maxLength: 255, minLength: 1

### Web Fetch Block

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

### Web Fetch Block Param

- `web_fetch_block_param: object`

  - `content: object`

    - `source: Base64PDFSource or PlainTextSource or ContentBlockSource or 2 more`

      - `base64_pdf_source: object`

        - `data: string`

          format: byte

        - `media_type: "application/pdf"`

        - `type: "base64"`

      - `plain_text_source: object`

        - `data: string`

        - `media_type: "text/plain"`

        - `type: "text"`

      - `content_block_source: object`

        - `content: string or array of ContentBlockSourceContent`

          - `union_member_0: string`

          - `content_block_source_content: array of ContentBlockSourceContent`

            - `text_block_param: object`

              - `text: string`

                minLength: 1

              - `type: "text"`

              - `cache_control: optional object`

                Create a cache control breakpoint at this content block.

                - `type: "ephemeral"`

                - `ttl: optional "5m" or "1h"`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

                  - `"5m"`

                  - `"1h"`

              - `citations: optional array of TextCitationParam`

                - `citation_char_location_param: object`

                  - `cited_text: string`

                  - `document_index: number`

                    minimum: 0

                  - `document_title: string`

                    maxLength: 500, minLength: 1

                  - `end_char_index: number`

                  - `start_char_index: number`

                    minimum: 0

                  - `type: "char_location"`

                - `citation_page_location_param: object`

                  - `cited_text: string`

                  - `document_index: number`

                    minimum: 0

                  - `document_title: string`

                    maxLength: 500, minLength: 1

                  - `end_page_number: number`

                  - `start_page_number: number`

                    minimum: 1

                  - `type: "page_location"`

                - `citation_content_block_location_param: object`

                  - `cited_text: string`

                    The full text of the cited block range, concatenated.

                    Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

                  - `document_index: number`

                    minimum: 0

                  - `document_title: string`

                    maxLength: 500, minLength: 1

                  - `end_block_index: number`

                    Exclusive 0-based end index of the cited block range in the source's `content` array.

                    Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

                  - `start_block_index: number`

                    0-based index of the first cited block in the source's `content` array.

                    minimum: 0

                  - `type: "content_block_location"`

                - `citation_web_search_result_location_param: object`

                  - `cited_text: string`

                  - `encrypted_index: string`

                  - `title: string`

                    maxLength: 512, minLength: 1

                  - `type: "web_search_result_location"`

                  - `url: string`

                    minLength: 1

                - `citation_search_result_location_param: object`

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

            - `image_block_param: object`

              - `source: Base64ImageSource or URLImageSource or FileImageSource`

                - `base64_image_source: object`

                  - `data: string`

                    format: byte

                  - `media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"`

                    - `"image/jpeg"`

                    - `"image/png"`

                    - `"image/gif"`

                    - `"image/webp"`

                  - `type: "base64"`

                - `url_image_source: object`

                  - `type: "url"`

                  - `url: string`

                - `file_image_source: object`

                  - `file_id: string`

                  - `type: "file"`

              - `type: "image"`

              - `cache_control: optional object`

                Create a cache control breakpoint at this content block.

                - `type: "ephemeral"`

                - `ttl: optional "5m" or "1h"`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

              - `transformations: optional object`

                Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

                - `oversized_image: optional "downsize" or "error"`

                  What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

                  - `"downsize"`

                  - `"error"`

        - `type: "content"`

      - `url_pdf_source: object`

        - `type: "url"`

        - `url: string`

      - `file_document_source: object`

        - `file_id: string`

        - `type: "file"`

    - `type: "document"`

    - `cache_control: optional object`

      Create a cache control breakpoint at this content block.

      - `type: "ephemeral"`

      - `ttl: optional "5m" or "1h"`

        The time-to-live for the cache control breakpoint.

        This may be one the following values:

        - `5m`: 5 minutes
        - `1h`: 1 hour

        Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

    - `citations: optional object`

      - `enabled: optional boolean`

    - `context: optional string`

      minLength: 1

    - `title: optional string`

      maxLength: 500, minLength: 1

  - `type: "web_fetch_result"`

  - `url: string`

    Fetched content URL

  - `retrieved_at: optional string`

    ISO 8601 timestamp when the content was retrieved

### Web Fetch Tool 20250910

- `web_fetch_tool_20250910: object`

  - `name: "web_fetch"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `type: "web_fetch_20250910"`

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

    - `"code_execution_20260521"`

  - `allowed_domains: optional array of string`

    List of domains to allow fetching from

  - `blocked_domains: optional array of string`

    List of domains to block fetching from

  - `cache_control: optional object`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `"5m"`

      - `"1h"`

  - `citations: optional object`

    Citations configuration for fetched documents. Citations are disabled by default.

    - `enabled: optional boolean`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `max_content_tokens: optional number`

    Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    exclusiveMinimum: 0

  - `max_uses: optional number`

    Maximum number of times the tool can be used in the API request.

    exclusiveMinimum: 0

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

### Web Fetch Tool 20260209

- `web_fetch_tool_20260209: object`

  - `name: "web_fetch"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `type: "web_fetch_20260209"`

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

    - `"code_execution_20260521"`

  - `allowed_domains: optional array of string`

    List of domains to allow fetching from

  - `blocked_domains: optional array of string`

    List of domains to block fetching from

  - `cache_control: optional object`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `"5m"`

      - `"1h"`

  - `citations: optional object`

    Citations configuration for fetched documents. Citations are disabled by default.

    - `enabled: optional boolean`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `max_content_tokens: optional number`

    Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    exclusiveMinimum: 0

  - `max_uses: optional number`

    Maximum number of times the tool can be used in the API request.

    exclusiveMinimum: 0

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

### Web Fetch Tool 20260309

- `web_fetch_tool_20260309: object`

  Web fetch tool with use_cache parameter for bypassing cached content.

  - `name: "web_fetch"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `type: "web_fetch_20260309"`

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

    - `"code_execution_20260521"`

  - `allowed_domains: optional array of string`

    List of domains to allow fetching from

  - `blocked_domains: optional array of string`

    List of domains to block fetching from

  - `cache_control: optional object`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `"5m"`

      - `"1h"`

  - `citations: optional object`

    Citations configuration for fetched documents. Citations are disabled by default.

    - `enabled: optional boolean`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `max_content_tokens: optional number`

    Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    exclusiveMinimum: 0

  - `max_uses: optional number`

    Maximum number of times the tool can be used in the API request.

    exclusiveMinimum: 0

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

  - `use_cache: optional boolean`

    Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

### Web Fetch Tool 20260318

- `web_fetch_tool_20260318: object`

  - `name: "web_fetch"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `type: "web_fetch_20260318"`

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

    - `"code_execution_20260521"`

  - `allowed_domains: optional array of string`

    List of domains to allow fetching from

  - `blocked_domains: optional array of string`

    List of domains to block fetching from

  - `cache_control: optional object`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `"5m"`

      - `"1h"`

  - `citations: optional object`

    Citations configuration for fetched documents. Citations are disabled by default.

    - `enabled: optional boolean`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `max_content_tokens: optional number`

    Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

    exclusiveMinimum: 0

  - `max_uses: optional number`

    Maximum number of times the tool can be used in the API request.

    exclusiveMinimum: 0

  - `response_inclusion: optional "full" or "excluded"`

    How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

    - `"full"`

    - `"excluded"`

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

  - `use_cache: optional boolean`

    Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

### Web Fetch Tool Result Block

- `web_fetch_tool_result_block: object`

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

### Web Fetch Tool Result Block Param

- `web_fetch_tool_result_block_param: object`

  - `content: WebFetchToolResultErrorBlockParam or WebFetchBlockParam`

    - `web_fetch_tool_result_error_block_param: object`

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

    - `web_fetch_block_param: object`

      - `content: object`

        - `source: Base64PDFSource or PlainTextSource or ContentBlockSource or 2 more`

          - `base64_pdf_source: object`

            - `data: string`

              format: byte

            - `media_type: "application/pdf"`

            - `type: "base64"`

          - `plain_text_source: object`

            - `data: string`

            - `media_type: "text/plain"`

            - `type: "text"`

          - `content_block_source: object`

            - `content: string or array of ContentBlockSourceContent`

              - `union_member_0: string`

              - `content_block_source_content: array of ContentBlockSourceContent`

                - `text_block_param: object`

                  - `text: string`

                    minLength: 1

                  - `type: "text"`

                  - `cache_control: optional object`

                    Create a cache control breakpoint at this content block.

                    - `type: "ephemeral"`

                    - `ttl: optional "5m" or "1h"`

                      The time-to-live for the cache control breakpoint.

                      This may be one the following values:

                      - `5m`: 5 minutes
                      - `1h`: 1 hour

                      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

                      - `"5m"`

                      - `"1h"`

                  - `citations: optional array of TextCitationParam`

                    - `citation_char_location_param: object`

                      - `cited_text: string`

                      - `document_index: number`

                        minimum: 0

                      - `document_title: string`

                        maxLength: 500, minLength: 1

                      - `end_char_index: number`

                      - `start_char_index: number`

                        minimum: 0

                      - `type: "char_location"`

                    - `citation_page_location_param: object`

                      - `cited_text: string`

                      - `document_index: number`

                        minimum: 0

                      - `document_title: string`

                        maxLength: 500, minLength: 1

                      - `end_page_number: number`

                      - `start_page_number: number`

                        minimum: 1

                      - `type: "page_location"`

                    - `citation_content_block_location_param: object`

                      - `cited_text: string`

                        The full text of the cited block range, concatenated.

                        Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

                      - `document_index: number`

                        minimum: 0

                      - `document_title: string`

                        maxLength: 500, minLength: 1

                      - `end_block_index: number`

                        Exclusive 0-based end index of the cited block range in the source's `content` array.

                        Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

                      - `start_block_index: number`

                        0-based index of the first cited block in the source's `content` array.

                        minimum: 0

                      - `type: "content_block_location"`

                    - `citation_web_search_result_location_param: object`

                      - `cited_text: string`

                      - `encrypted_index: string`

                      - `title: string`

                        maxLength: 512, minLength: 1

                      - `type: "web_search_result_location"`

                      - `url: string`

                        minLength: 1

                    - `citation_search_result_location_param: object`

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

                - `image_block_param: object`

                  - `source: Base64ImageSource or URLImageSource or FileImageSource`

                    - `base64_image_source: object`

                      - `data: string`

                        format: byte

                      - `media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"`

                        - `"image/jpeg"`

                        - `"image/png"`

                        - `"image/gif"`

                        - `"image/webp"`

                      - `type: "base64"`

                    - `url_image_source: object`

                      - `type: "url"`

                      - `url: string`

                    - `file_image_source: object`

                      - `file_id: string`

                      - `type: "file"`

                  - `type: "image"`

                  - `cache_control: optional object`

                    Create a cache control breakpoint at this content block.

                    - `type: "ephemeral"`

                    - `ttl: optional "5m" or "1h"`

                      The time-to-live for the cache control breakpoint.

                      This may be one the following values:

                      - `5m`: 5 minutes
                      - `1h`: 1 hour

                      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

                  - `transformations: optional object`

                    Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

                    - `oversized_image: optional "downsize" or "error"`

                      What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

                      - `"downsize"`

                      - `"error"`

            - `type: "content"`

          - `url_pdf_source: object`

            - `type: "url"`

            - `url: string`

          - `file_document_source: object`

            - `file_id: string`

            - `type: "file"`

        - `type: "document"`

        - `cache_control: optional object`

          Create a cache control breakpoint at this content block.

          - `type: "ephemeral"`

          - `ttl: optional "5m" or "1h"`

            The time-to-live for the cache control breakpoint.

            This may be one the following values:

            - `5m`: 5 minutes
            - `1h`: 1 hour

            Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

        - `citations: optional object`

          - `enabled: optional boolean`

        - `context: optional string`

          minLength: 1

        - `title: optional string`

          maxLength: 500, minLength: 1

      - `type: "web_fetch_result"`

      - `url: string`

        Fetched content URL

      - `retrieved_at: optional string`

        ISO 8601 timestamp when the content was retrieved

  - `tool_use_id: string`

    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

  - `type: "web_fetch_tool_result"`

  - `cache_control: optional object`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

  - `caller: optional DirectCaller or ServerToolCaller or ServerToolCaller20260120`

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

### Web Fetch Tool Result Error Block

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

### Web Fetch Tool Result Error Block Param

- `web_fetch_tool_result_error_block_param: object`

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

### Web Fetch Tool Result Error Code

- `web_fetch_tool_result_error_code: "invalid_tool_input" or "url_too_long" or "url_not_allowed" or 6 more`

  - `"invalid_tool_input"`

  - `"url_too_long"`

  - `"url_not_allowed"`

  - `"url_not_in_prior_context"`

  - `"url_not_accessible"`

  - `"unsupported_content_type"`

  - `"too_many_requests"`

  - `"max_uses_exceeded"`

  - `"unavailable"`

### Web Search Result Block

- `web_search_result_block: object`

  - `encrypted_content: string`

  - `page_age: string`

  - `title: string`

  - `type: "web_search_result"`

  - `url: string`

### Web Search Result Block Param

- `web_search_result_block_param: object`

  - `encrypted_content: string`

  - `title: string`

  - `type: "web_search_result"`

  - `url: string`

  - `page_age: optional string`

### Web Search Tool 20250305

- `web_search_tool_20250305: object`

  - `name: "web_search"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `type: "web_search_20250305"`

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

    - `"code_execution_20260521"`

  - `allowed_domains: optional array of string`

    If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

  - `blocked_domains: optional array of string`

    If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

  - `cache_control: optional object`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `"5m"`

      - `"1h"`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `max_uses: optional number`

    Maximum number of times the tool can be used in the API request.

    exclusiveMinimum: 0

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

  - `user_location: optional object`

    Parameters for the user's location. Used to provide more relevant search results.

    - `type: "approximate"`

    - `city: optional string`

      The city of the user.

      maxLength: 255, minLength: 1

    - `country: optional string`

      The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

      maxLength: 2, minLength: 2

    - `region: optional string`

      The region of the user.

      maxLength: 255, minLength: 1

    - `timezone: optional string`

      The [IANA timezone](https://nodatime.org/TimeZones) of the user.

      maxLength: 255, minLength: 1

### Web Search Tool 20260209

- `web_search_tool_20260209: object`

  - `name: "web_search"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `type: "web_search_20260209"`

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

    - `"code_execution_20260521"`

  - `allowed_domains: optional array of string`

    If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

  - `blocked_domains: optional array of string`

    If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

  - `cache_control: optional object`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `"5m"`

      - `"1h"`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `max_uses: optional number`

    Maximum number of times the tool can be used in the API request.

    exclusiveMinimum: 0

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

  - `user_location: optional object`

    Parameters for the user's location. Used to provide more relevant search results.

    - `type: "approximate"`

    - `city: optional string`

      The city of the user.

      maxLength: 255, minLength: 1

    - `country: optional string`

      The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

      maxLength: 2, minLength: 2

    - `region: optional string`

      The region of the user.

      maxLength: 255, minLength: 1

    - `timezone: optional string`

      The [IANA timezone](https://nodatime.org/TimeZones) of the user.

      maxLength: 255, minLength: 1

### Web Search Tool 20260318

- `web_search_tool_20260318: object`

  - `name: "web_search"`

    Name of the tool.

    This is how the tool will be called by the model and in `tool_use` blocks.

  - `type: "web_search_20260318"`

  - `allowed_callers: optional array of "direct" or "code_execution_20250825" or "code_execution_20260120" or "code_execution_20260521"`

    - `"direct"`

    - `"code_execution_20250825"`

    - `"code_execution_20260120"`

    - `"code_execution_20260521"`

  - `allowed_domains: optional array of string`

    If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

  - `blocked_domains: optional array of string`

    If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

  - `cache_control: optional object`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `"5m"`

      - `"1h"`

  - `defer_loading: optional boolean`

    If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

  - `max_uses: optional number`

    Maximum number of times the tool can be used in the API request.

    exclusiveMinimum: 0

  - `response_inclusion: optional "full" or "excluded"`

    How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

    - `"full"`

    - `"excluded"`

  - `strict: optional boolean`

    When true, guarantees schema validation on tool names and inputs

  - `user_location: optional object`

    Parameters for the user's location. Used to provide more relevant search results.

    - `type: "approximate"`

    - `city: optional string`

      The city of the user.

      maxLength: 255, minLength: 1

    - `country: optional string`

      The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

      maxLength: 2, minLength: 2

    - `region: optional string`

      The region of the user.

      maxLength: 255, minLength: 1

    - `timezone: optional string`

      The [IANA timezone](https://nodatime.org/TimeZones) of the user.

      maxLength: 255, minLength: 1

### Web Search Tool Request Error

- `web_search_tool_request_error: object`

  - `error_code: "invalid_tool_input" or "unavailable" or "max_uses_exceeded" or 3 more`

    - `"invalid_tool_input"`

    - `"unavailable"`

    - `"max_uses_exceeded"`

    - `"too_many_requests"`

    - `"query_too_long"`

    - `"request_too_large"`

  - `type: "web_search_tool_result_error"`

### Web Search Tool Result Block

- `web_search_tool_result_block: object`

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

### Web Search Tool Result Block Content

- `web_search_tool_result_block_content: WebSearchToolResultError or array of WebSearchResultBlock`

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

### Web Search Tool Result Block Param

- `web_search_tool_result_block_param: object`

  - `content: array of WebSearchResultBlockParam or WebSearchToolRequestError`

    - `web_search_tool_result_block_item: array of WebSearchResultBlockParam`

      - `encrypted_content: string`

      - `title: string`

      - `type: "web_search_result"`

      - `url: string`

      - `page_age: optional string`

    - `web_search_tool_request_error: object`

      - `error_code: "invalid_tool_input" or "unavailable" or "max_uses_exceeded" or 3 more`

        - `"invalid_tool_input"`

        - `"unavailable"`

        - `"max_uses_exceeded"`

        - `"too_many_requests"`

        - `"query_too_long"`

        - `"request_too_large"`

      - `type: "web_search_tool_result_error"`

  - `tool_use_id: string`

    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

  - `type: "web_search_tool_result"`

  - `cache_control: optional object`

    Create a cache control breakpoint at this content block.

    - `type: "ephemeral"`

    - `ttl: optional "5m" or "1h"`

      The time-to-live for the cache control breakpoint.

      This may be one the following values:

      - `5m`: 5 minutes
      - `1h`: 1 hour

      Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

      - `"5m"`

      - `"1h"`

  - `caller: optional DirectCaller or ServerToolCaller or ServerToolCaller20260120`

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

### Web Search Tool Result Block Param Content

- `web_search_tool_result_block_param_content: array of WebSearchResultBlockParam or WebSearchToolRequestError`

  - `web_search_tool_result_block_item: array of WebSearchResultBlockParam`

    - `encrypted_content: string`

    - `title: string`

    - `type: "web_search_result"`

    - `url: string`

    - `page_age: optional string`

  - `web_search_tool_request_error: object`

    - `error_code: "invalid_tool_input" or "unavailable" or "max_uses_exceeded" or 3 more`

      - `"invalid_tool_input"`

      - `"unavailable"`

      - `"max_uses_exceeded"`

      - `"too_many_requests"`

      - `"query_too_long"`

      - `"request_too_large"`

    - `type: "web_search_tool_result_error"`

### Web Search Tool Result Error

- `web_search_tool_result_error: object`

  - `error_code: "invalid_tool_input" or "unavailable" or "max_uses_exceeded" or 3 more`

    - `"invalid_tool_input"`

    - `"unavailable"`

    - `"max_uses_exceeded"`

    - `"too_many_requests"`

    - `"query_too_long"`

    - `"request_too_large"`

  - `type: "web_search_tool_result_error"`

### Web Search Tool Result Error Code

- `web_search_tool_result_error_code: "invalid_tool_input" or "unavailable" or "max_uses_exceeded" or 3 more`

  - `"invalid_tool_input"`

  - `"unavailable"`

  - `"max_uses_exceeded"`

  - `"too_many_requests"`

  - `"query_too_long"`

  - `"request_too_large"`

## Messages › Batches

### Create a Message Batch

`$ ant messages:batches create`

**POST** `/v1/messages/batches`

Send a batch of Message creation requests.

The Message Batches API can be used to process multiple Messages API requests at once. Once a Message Batch is created, it begins processing immediately. Batches can take up to 24 hours to complete.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

#### Parameters

- `--request: array of object`

  Body param: List of requests for prompt completion. Each is an individual request to create a Message.

  maxItems: 100000, minItems: 1

- `--user-profile-id: optional string`

  Header param: The user profile ID to attribute the requests in this batch to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header. Applies to every request in the batch; an individual request whose `user_profile_id` body field conflicts with this header is errored.

#### Returns

- `message_batch: object`

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `archived_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

    format: date-time

  - `cancel_initiated_at: string`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

    format: date-time

  - `created_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

    format: date-time

  - `ended_at: string`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

    format: date-time

  - `expires_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

    format: date-time

  - `processing_status: "in_progress" or "canceling" or "ended"`

    Processing status of the Message Batch.

    - `"in_progress"`

    - `"canceling"`

    - `"ended"`

  - `request_counts: object`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `canceled: number`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `errored: number`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `expired: number`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `processing: number`

      Number of requests in the Message Batch that are processing.

    - `succeeded: number`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `results_url: string`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `type: "message_batch"`

    Object type.

    For Message Batches, this is always `"message_batch"`.

#### Example

```bash
ant messages:batches create \
  --api-key my-anthropic-api-key \
  --request '{custom_id: my-custom-id-1, params: {max_tokens: 1024, messages: [{content: [{text: x, type: text}], role: user}], model: claude-opus-5}}'
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

`$ ant messages:batches retrieve`

**GET** `/v1/messages/batches/{message_batch_id}`

This endpoint is idempotent and can be used to poll for Message Batch completion. To access the results of a Message Batch, make a request to the `results_url` field in the response.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

#### Parameters

- `--message-batch-id: string`

  ID of the Message Batch.

#### Returns

- `message_batch: object`

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `archived_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

    format: date-time

  - `cancel_initiated_at: string`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

    format: date-time

  - `created_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

    format: date-time

  - `ended_at: string`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

    format: date-time

  - `expires_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

    format: date-time

  - `processing_status: "in_progress" or "canceling" or "ended"`

    Processing status of the Message Batch.

    - `"in_progress"`

    - `"canceling"`

    - `"ended"`

  - `request_counts: object`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `canceled: number`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `errored: number`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `expired: number`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `processing: number`

      Number of requests in the Message Batch that are processing.

    - `succeeded: number`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `results_url: string`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `type: "message_batch"`

    Object type.

    For Message Batches, this is always `"message_batch"`.

#### Example

```bash
ant messages:batches retrieve \
  --api-key my-anthropic-api-key \
  --message-batch-id message_batch_id
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

`$ ant messages:batches list`

**GET** `/v1/messages/batches`

List all Message Batches within a Workspace. Most recently created batches are returned first.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

#### Parameters

- `--after-id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `--before-id: optional string`

  ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `--limit: optional number`

  Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

  maximum: 1000, minimum: 1

#### Returns

- `ListResponse_MessageBatch_: object`

  - `data: array of MessageBatch`

    - `id: string`

      Unique object identifier.

      The format and length of IDs may change over time.

    - `archived_at: string`

      RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

      format: date-time

    - `cancel_initiated_at: string`

      RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

      format: date-time

    - `created_at: string`

      RFC 3339 datetime string representing the time at which the Message Batch was created.

      format: date-time

    - `ended_at: string`

      RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

      Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

      format: date-time

    - `expires_at: string`

      RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

      format: date-time

    - `processing_status: "in_progress" or "canceling" or "ended"`

      Processing status of the Message Batch.

      - `"in_progress"`

      - `"canceling"`

      - `"ended"`

    - `request_counts: object`

      Tallies requests within the Message Batch, categorized by their status.

      Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

      - `canceled: number`

        Number of requests in the Message Batch that have been canceled.

        This is zero until processing of the entire Message Batch has ended.

      - `errored: number`

        Number of requests in the Message Batch that encountered an error.

        This is zero until processing of the entire Message Batch has ended.

      - `expired: number`

        Number of requests in the Message Batch that have expired.

        This is zero until processing of the entire Message Batch has ended.

      - `processing: number`

        Number of requests in the Message Batch that are processing.

      - `succeeded: number`

        Number of requests in the Message Batch that have completed successfully.

        This is zero until processing of the entire Message Batch has ended.

    - `results_url: string`

      URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

      Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

    - `type: "message_batch"`

      Object type.

      For Message Batches, this is always `"message_batch"`.

  - `first_id: string`

    First ID in the `data` list. Can be used as the `before_id` for the previous page.

  - `has_more: boolean`

    Indicates if there are more results in the requested page direction.

  - `last_id: string`

    Last ID in the `data` list. Can be used as the `after_id` for the next page.

#### Example

```bash
ant messages:batches list \
  --api-key my-anthropic-api-key
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

`$ ant messages:batches cancel`

**POST** `/v1/messages/batches/{message_batch_id}/cancel`

Batches may be canceled any time before processing ends. Once cancellation is initiated, the batch enters a `canceling` state, at which time the system may complete any in-progress, non-interruptible requests before finalizing cancellation.

The number of canceled requests is specified in `request_counts`. To determine which requests were canceled, check the individual results within the batch. Note that cancellation may not result in any canceled requests if they were non-interruptible.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

#### Parameters

- `--message-batch-id: string`

  ID of the Message Batch.

#### Returns

- `message_batch: object`

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `archived_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

    format: date-time

  - `cancel_initiated_at: string`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

    format: date-time

  - `created_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

    format: date-time

  - `ended_at: string`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

    format: date-time

  - `expires_at: string`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

    format: date-time

  - `processing_status: "in_progress" or "canceling" or "ended"`

    Processing status of the Message Batch.

    - `"in_progress"`

    - `"canceling"`

    - `"ended"`

  - `request_counts: object`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `canceled: number`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `errored: number`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `expired: number`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `processing: number`

      Number of requests in the Message Batch that are processing.

    - `succeeded: number`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `results_url: string`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `type: "message_batch"`

    Object type.

    For Message Batches, this is always `"message_batch"`.

#### Example

```bash
ant messages:batches cancel \
  --api-key my-anthropic-api-key \
  --message-batch-id message_batch_id
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

`$ ant messages:batches delete`

**DELETE** `/v1/messages/batches/{message_batch_id}`

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

#### Parameters

- `--message-batch-id: string`

  ID of the Message Batch.

#### Returns

- `deleted_message_batch: object`

  - `id: string`

    ID of the Message Batch.

  - `type: "message_batch_deleted"`

    Deleted object type.

    For Message Batches, this is always `"message_batch_deleted"`.

#### Example

```bash
ant messages:batches delete \
  --api-key my-anthropic-api-key \
  --message-batch-id message_batch_id
```

##### Response (200)

```json
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "type": "message_batch_deleted"
}
```

### Retrieve Message Batch results

`$ ant messages:batches results`

**GET** `/v1/messages/batches/{message_batch_id}/results`

Streams the results of a Message Batch as a `.jsonl` file.

Each line in the file is a JSON object containing the result of a single request in the Message Batch. Results are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

#### Parameters

- `--message-batch-id: string`

  ID of the Message Batch.

#### Returns

- `message_batch_individual_response: object`

  This is a single line in the response `.jsonl` file and does not represent the response as a whole.

  - `custom_id: string`

    Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

    Must be unique for each request within the Message Batch.

  - `result: MessageBatchSucceededResult or MessageBatchErroredResult or MessageBatchCanceledResult or MessageBatchExpiredResult`

    Processing result for this request.

    Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

    - `message_batch_succeeded_result: object`

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

        - `model: "claude-fable-5-1" or "claude-mythos-5-1" or "claude-sonnet-5" or 14 more or string`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

      - `type: "succeeded"`

    - `message_batch_errored_result: object`

      - `error: object`

        - `error: InvalidRequestError or AuthenticationError or BillingError or 6 more`

          - `invalid_request_error: object`

            - `message: string`

            - `type: "invalid_request_error"`

          - `authentication_error: object`

            - `message: string`

            - `type: "authentication_error"`

          - `billing_error: object`

            - `message: string`

            - `type: "billing_error"`

          - `permission_error: object`

            - `message: string`

            - `type: "permission_error"`

          - `not_found_error: object`

            - `message: string`

            - `type: "not_found_error"`

          - `rate_limit_error: object`

            - `message: string`

            - `type: "rate_limit_error"`

          - `gateway_timeout_error: object`

            - `message: string`

            - `type: "timeout_error"`

          - `api_error_object: object`

            - `message: string`

            - `type: "api_error"`

          - `overloaded_error: object`

            - `message: string`

            - `type: "overloaded_error"`

        - `request_id: string`

        - `type: "error"`

      - `type: "errored"`

    - `message_batch_canceled_result: object`

      - `type: "canceled"`

    - `message_batch_expired_result: object`

      - `type: "expired"`

#### Example

```bash
ant messages:batches results \
  --api-key my-anthropic-api-key \
  --message-batch-id message_batch_id
```
