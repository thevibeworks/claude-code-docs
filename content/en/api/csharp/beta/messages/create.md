# Create a Message

`BetaMessage Beta.Messages.Create(parameters, cancellationToken = default)`

**POST** `/v1/messages`

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

The Messages API can be used for either single queries or stateless multi-turn conversations.

Learn more about the Messages API in our [user guide](https://platform.claude.com/docs/en/get-started)

## Parameters

- `MessageCreateParams parameters`

  - `required long maxTokens`

    Body param: The maximum number of tokens to generate before stopping.

    Note that our models may stop _before_ reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

    Set to `0` to populate the [prompt cache](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#pre-warming-the-cache) without generating a response.

    Different models have different maximum values for this parameter.  See [models](https://platform.claude.com/docs/en/about-claude/models/overview) for details.

    minimum: 0

  - `required IReadOnlyList<BetaMessageParam> messages`

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

    - `required Content Content`

      - `string`

      - `IReadOnlyList<BetaContentBlockParam>`

        - `class BetaTextBlockParam:`

          - `required string Text`

            minLength: 1

          - `JsonElement Type = "text"`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

            - `JsonElement Type = "ephemeral"`

            - `Ttl Ttl`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

              - `Ttl5m("5m")`

              - `Ttl1h("1h")`

          - `IReadOnlyList<BetaTextCitationParam>? Citations`

            - `class BetaCitationCharLocationParam:`

              - `required string CitedText`

              - `required long DocumentIndex`

                minimum: 0

              - `required string? DocumentTitle`

                maxLength: 500, minLength: 1

              - `required long EndCharIndex`

              - `required long StartCharIndex`

                minimum: 0

              - `JsonElement Type = "char_location"`

            - `class BetaCitationPageLocationParam:`

              - `required string CitedText`

              - `required long DocumentIndex`

                minimum: 0

              - `required string? DocumentTitle`

                maxLength: 500, minLength: 1

              - `required long EndPageNumber`

              - `required long StartPageNumber`

                minimum: 1

              - `JsonElement Type = "page_location"`

            - `class BetaCitationContentBlockLocationParam:`

              - `required string CitedText`

                The full text of the cited block range, concatenated.

                Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

              - `required long DocumentIndex`

                minimum: 0

              - `required string? DocumentTitle`

                maxLength: 500, minLength: 1

              - `required long EndBlockIndex`

                Exclusive 0-based end index of the cited block range in the source's `content` array.

                Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

              - `required long StartBlockIndex`

                0-based index of the first cited block in the source's `content` array.

                minimum: 0

              - `JsonElement Type = "content_block_location"`

            - `class BetaCitationWebSearchResultLocationParam:`

              - `required string CitedText`

              - `required string EncryptedIndex`

              - `required string? Title`

                maxLength: 512, minLength: 1

              - `JsonElement Type = "web_search_result_location"`

              - `required string Url`

                minLength: 1

            - `class BetaCitationSearchResultLocationParam:`

              - `required string CitedText`

                The full text of the cited block range, concatenated.

                Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

              - `required long EndBlockIndex`

                Exclusive 0-based end index of the cited block range in the source's `content` array.

                Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

              - `required long SearchResultIndex`

                0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

                Counted separately from `document_index`; server-side web search results are not included in this count.

                minimum: 0

              - `required string Source`

              - `required long StartBlockIndex`

                0-based index of the first cited block in the source's `content` array.

                minimum: 0

              - `required string? Title`

              - `JsonElement Type = "search_result_location"`

        - `class BetaImageBlockParam:`

          - `required Source Source`

            - `class BetaBase64ImageSource:`

              - `required string Data`

                format: byte

              - `required MediaType MediaType`

                - `ImageJpeg("image/jpeg")`

                - `ImagePng("image/png")`

                - `ImageGif("image/gif")`

                - `ImageWebP("image/webp")`

              - `JsonElement Type = "base64"`

            - `class BetaUrlImageSource:`

              - `JsonElement Type = "url"`

              - `required string Url`

            - `class BetaFileImageSource:`

              - `required string FileID`

              - `JsonElement Type = "file"`

          - `JsonElement Type = "image"`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `BetaImageTransformationsParam? Transformations`

            Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

            - `OversizedImage OversizedImage`

              What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

              - `Downsize("downsize")`

              - `Error("error")`

        - `class BetaRequestDocumentBlock:`

          - `required Source Source`

            - `class BetaBase64PdfSource:`

              - `required string Data`

                format: byte

              - `JsonElement MediaType = "application/pdf"`

              - `JsonElement Type = "base64"`

            - `class BetaPlainTextSource:`

              - `required string Data`

              - `JsonElement MediaType = "text/plain"`

              - `JsonElement Type = "text"`

            - `class BetaContentBlockSource:`

              - `required Content Content`

                - `string`

                - `IReadOnlyList<BetaContentBlockSourceContent>`

                  - `class BetaTextBlockParam:`

                  - `class BetaImageBlockParam:`

              - `JsonElement Type = "content"`

            - `class BetaUrlPdfSource:`

              - `JsonElement Type = "url"`

              - `required string Url`

            - `class BetaFileDocumentSource:`

              - `required string FileID`

              - `JsonElement Type = "file"`

          - `JsonElement Type = "document"`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `BetaCitationsConfigParam? Citations`

            - `bool Enabled`

          - `string? Context`

            minLength: 1

          - `string? Title`

            maxLength: 500, minLength: 1

        - `class BetaSearchResultBlockParam:`

          - `required IReadOnlyList<BetaTextBlockParam> Content`

            - `required string Text`

              minLength: 1

            - `JsonElement Type = "text"`

            - `BetaCacheControlEphemeral? CacheControl`

              Create a cache control breakpoint at this content block.

            - `IReadOnlyList<BetaTextCitationParam>? Citations`

          - `required string Source`

          - `required string Title`

          - `JsonElement Type = "search_result"`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `BetaCitationsConfigParam Citations`

        - `class BetaThinkingBlockParam:`

          - `required string Signature`

            The `signature` value of this thinking block, exactly as returned by the API in a previous response. Used to verify that the block was generated by Claude.

            Thinking blocks must be passed back unmodified and in their original order; a modified block results in a 400 `invalid_request_error`.

          - `required string Thinking`

            The `thinking` text of this block as returned by the API.

          - `JsonElement Type = "thinking"`

        - `class BetaRedactedThinkingBlockParam:`

          - `required string Data`

            The `data` value of this redacted thinking block, exactly as returned by the API in a previous response. Opaque and encrypted; pass it back unchanged.

          - `JsonElement Type = "redacted_thinking"`

        - `class BetaToolUseBlockParam:`

          - `required string ID`

            pattern: ^[a-zA-Z0-9_-]+$

          - `required IReadOnlyDictionary<string, JsonElement> Input`

          - `required string Name`

            maxLength: 200, minLength: 1

          - `JsonElement Type = "tool_use"`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `Caller Caller`

            Tool invocation directly from the model.

            - `class BetaDirectCaller:`

              Tool invocation directly from the model.

              - `JsonElement Type = "direct"`

            - `class BetaServerToolCaller:`

              Tool invocation generated by a server-side tool.

              - `required string ToolID`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `JsonElement Type = "code_execution_20250825"`

            - `class BetaServerToolCaller20260120:`

              - `required string ToolID`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `JsonElement Type = "code_execution_20260120"`

          - `string? ToolsetName`

            For a toolset member tool_use, the toolset family this member belongs to.

            maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

        - `class BetaToolResultBlockParam:`

          - `required string ToolUseID`

            pattern: ^[a-zA-Z0-9_-]+$

          - `JsonElement Type = "tool_result"`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `Content Content`

            - `string`

            - `IReadOnlyList<Block>`

              - `class BetaTextBlockParam:`

              - `class BetaImageBlockParam:`

              - `class BetaSearchResultBlockParam:`

              - `class BetaRequestDocumentBlock:`

              - `class BetaToolReferenceBlockParam:`

                Tool reference block that can be included in tool_result content.

                - `required string ToolName`

                  maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

                - `JsonElement Type = "tool_reference"`

                - `BetaCacheControlEphemeral? CacheControl`

                  Create a cache control breakpoint at this content block.

              - `class BetaBrowserStateBlockParam:`

                The caller's browser state after a browser toolset member call —
                the full inventory of open tabs, which tab is active, and any side
                effects (tabs opened, download state changes) the call produced.

                At most one per `tool_result`, only on a non-error result answering a
                browser toolset member `tool_use`. The server renders the
                model-visible text from it; the model never sees the raw fields.

                - `required IReadOnlyList<BetaBrowserStateTabEntry> Tabs`

                  All tabs open in the browser after this call — the full inventory, not a delta. May be empty. Whenever non-empty, exactly one entry carries `active: true`.

                  maxItems: 100

                  - `required string TabID`

                    The caller-assigned identifier for this tab, unique within the inventory.

                    maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                  - `required string Title`

                    The title of the page the tab is showing. May be empty.

                    maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                  - `required string Url`

                    The URL of the page the tab is showing. May be empty.

                    maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                  - `bool Active`

                    Whether this tab is the active tab after this call. Whenever `tabs` is non-empty, exactly one entry is marked `active: true`.

                - `JsonElement Type = "browser_state"`

                - `BetaCacheControlEphemeral? CacheControl`

                  Create a cache control breakpoint at this content block.

                - `IReadOnlyList<BetaBrowserStateChange>? StateChanges`

                  Tabs opened and download state changes during this call. "Nothing to report" is expressed by omitting the field, never by an empty list.

                  maxItems: 200, minItems: 1

                  - `class BetaBrowserStateChangeTabOpened:`

                    A tab this call's execution opened that remains open at its end —
                    the creation delta of the `tabs` inventory, not an event log.

                    Carries only the `tab_id`; the tab's `title` and `url` live on its
                    `tabs` entry, which must include the same `tab_id`. A tab opened
                    during a failed call gets no deferred `tab_opened`; it simply appears
                    in the next result's `tabs` inventory.

                    - `required string TabID`

                      The `tab_id` of the opened tab, present in `tabs`.

                      maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                    - `JsonElement Type = "tab_opened"`

                  - `class BetaBrowserStateChangeDownloadStarted:`

                    A file download that started during this call.

                    - `required string DownloadID`

                      The caller-assigned identifier for this download, stable across the state changes reporting it.

                      maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                    - `JsonElement Type = "download_started"`

                    - `required string Url`

                      The final post-redirect URL the download was served from.

                      maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                  - `class BetaBrowserStateChangeDownloadCompleted:`

                    A file download that finished during this call, reported with the
                    same `download_id` as its `download_started` — or without a prior
                    `download_started`, when the download finished during the call that
                    started it (at most one state change per `download_id` per result).

                    - `required string DownloadID`

                      The caller-assigned identifier for this download, stable across the state changes reporting it.

                      maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                    - `JsonElement Type = "download_completed"`

                    - `required string Url`

                      The final post-redirect URL the download was served from.

                      maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                    - `string? Path`

                      Where the executor saved the file, on the executor's filesystem. Only included when another tool in the same environment can read the file at that path.

                      pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

                    - `long? SizeBytes`

                      The completed download's size.

                      minimum: 0

                  - `class BetaBrowserStateChangeDownloadFailed:`

                    A file download that failed — or was cancelled — during this call.

                    - `required string DownloadID`

                      The caller-assigned identifier for this download, stable across the state changes reporting it.

                      maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                    - `JsonElement Type = "download_failed"`

                    - `required string Url`

                      The final post-redirect URL the download was served from.

                      maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                    - `string? Error`

                      The failure or cancellation detail, when known.

                      pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

          - `bool IsError`

          - `string? ToolsetName`

            For a toolset member tool_result, the toolset family of the paired tool_use.

            maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

        - `class BetaServerToolUseBlockParam:`

          - `required string ID`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `required IReadOnlyDictionary<string, JsonElement> Input`

          - `required Name Name`

            - `Advisor("advisor")`

            - `WebSearch("web_search")`

            - `WebFetch("web_fetch")`

            - `CodeExecution("code_execution")`

            - `BashCodeExecution("bash_code_execution")`

            - `TextEditorCodeExecution("text_editor_code_execution")`

            - `ToolSearchToolRegex("tool_search_tool_regex")`

            - `ToolSearchToolBm25("tool_search_tool_bm25")`

          - `JsonElement Type = "server_tool_use"`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `Caller Caller`

            Tool invocation directly from the model.

            - `class BetaDirectCaller:`

              Tool invocation directly from the model.

            - `class BetaServerToolCaller:`

              Tool invocation generated by a server-side tool.

            - `class BetaServerToolCaller20260120:`

        - `class BetaWebSearchToolResultBlockParam:`

          - `required BetaWebSearchToolResultBlockParamContent Content`

            - `IReadOnlyList<BetaWebSearchResultBlockParam>`

              - `required string EncryptedContent`

              - `required string Title`

              - `JsonElement Type = "web_search_result"`

              - `required string Url`

              - `string? PageAge`

            - `class BetaWebSearchToolRequestError:`

              - `required BetaWebSearchToolResultErrorCode ErrorCode`

                - `InvalidToolInput("invalid_tool_input")`

                - `Unavailable("unavailable")`

                - `MaxUsesExceeded("max_uses_exceeded")`

                - `TooManyRequests("too_many_requests")`

                - `QueryTooLong("query_too_long")`

                - `RequestTooLarge("request_too_large")`

              - `JsonElement Type = "web_search_tool_result_error"`

          - `required string ToolUseID`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonElement Type = "web_search_tool_result"`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `Caller Caller`

            Tool invocation directly from the model.

            - `class BetaDirectCaller:`

              Tool invocation directly from the model.

            - `class BetaServerToolCaller:`

              Tool invocation generated by a server-side tool.

            - `class BetaServerToolCaller20260120:`

        - `class BetaWebFetchToolResultBlockParam:`

          - `required Content Content`

            - `class BetaWebFetchToolResultErrorBlockParam:`

              - `required BetaWebFetchToolResultErrorCode ErrorCode`

                - `InvalidToolInput("invalid_tool_input")`

                - `UrlTooLong("url_too_long")`

                - `UrlNotAllowed("url_not_allowed")`

                - `UrlNotInPriorContext("url_not_in_prior_context")`

                - `UrlNotAccessible("url_not_accessible")`

                - `UnsupportedContentType("unsupported_content_type")`

                - `TooManyRequests("too_many_requests")`

                - `MaxUsesExceeded("max_uses_exceeded")`

                - `Unavailable("unavailable")`

              - `JsonElement Type = "web_fetch_tool_result_error"`

            - `class BetaWebFetchBlockParam:`

              - `required BetaRequestDocumentBlock Content`

              - `JsonElement Type = "web_fetch_result"`

              - `required string Url`

                Fetched content URL

              - `string? RetrievedAt`

                ISO 8601 timestamp when the content was retrieved

          - `required string ToolUseID`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonElement Type = "web_fetch_tool_result"`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `Caller Caller`

            Tool invocation directly from the model.

            - `class BetaDirectCaller:`

              Tool invocation directly from the model.

            - `class BetaServerToolCaller:`

              Tool invocation generated by a server-side tool.

            - `class BetaServerToolCaller20260120:`

        - `class BetaAdvisorToolResultBlockParam:`

          - `required Content Content`

            - `class BetaAdvisorToolResultErrorParam:`

              - `required ErrorCode ErrorCode`

                - `MaxUsesExceeded("max_uses_exceeded")`

                - `PromptTooLong("prompt_too_long")`

                - `TooManyRequests("too_many_requests")`

                - `Overloaded("overloaded")`

                - `Unavailable("unavailable")`

                - `ExecutionTimeExceeded("execution_time_exceeded")`

                - `ModelNotFound("model_not_found")`

              - `JsonElement Type = "advisor_tool_result_error"`

            - `class BetaAdvisorResultBlockParam:`

              - `required string Text`

              - `JsonElement Type = "advisor_result"`

              - `string? StopReason`

            - `class BetaAdvisorRedactedResultBlockParam:`

              - `required string EncryptedContent`

                Opaque blob produced by a prior response; must be round-tripped verbatim.

              - `JsonElement Type = "advisor_redacted_result"`

              - `string? StopReason`

          - `required string ToolUseID`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonElement Type = "advisor_tool_result"`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

        - `class BetaCodeExecutionToolResultBlockParam:`

          - `required BetaCodeExecutionToolResultBlockParamContent Content`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `class BetaCodeExecutionToolResultErrorParam:`

              - `required BetaCodeExecutionToolResultErrorCode ErrorCode`

                - `InvalidToolInput("invalid_tool_input")`

                - `Unavailable("unavailable")`

                - `TooManyRequests("too_many_requests")`

                - `ExecutionTimeExceeded("execution_time_exceeded")`

              - `JsonElement Type = "code_execution_tool_result_error"`

            - `class BetaCodeExecutionResultBlockParam:`

              - `required IReadOnlyList<BetaCodeExecutionOutputBlockParam> Content`

                - `required string FileID`

                - `JsonElement Type = "code_execution_output"`

              - `required long ReturnCode`

              - `required string Stderr`

              - `required string Stdout`

              - `JsonElement Type = "code_execution_result"`

            - `class BetaEncryptedCodeExecutionResultBlockParam:`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `required IReadOnlyList<BetaCodeExecutionOutputBlockParam> Content`

                - `required string FileID`

                - `JsonElement Type = "code_execution_output"`

              - `required string EncryptedStdout`

              - `required long ReturnCode`

              - `required string Stderr`

              - `JsonElement Type = "encrypted_code_execution_result"`

          - `required string ToolUseID`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonElement Type = "code_execution_tool_result"`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

        - `class BetaBashCodeExecutionToolResultBlockParam:`

          - `required Content Content`

            - `class BetaBashCodeExecutionToolResultErrorParam:`

              - `required ErrorCode ErrorCode`

                - `InvalidToolInput("invalid_tool_input")`

                - `Unavailable("unavailable")`

                - `TooManyRequests("too_many_requests")`

                - `ExecutionTimeExceeded("execution_time_exceeded")`

                - `OutputFileTooLarge("output_file_too_large")`

              - `JsonElement Type = "bash_code_execution_tool_result_error"`

            - `class BetaBashCodeExecutionResultBlockParam:`

              - `required IReadOnlyList<BetaBashCodeExecutionOutputBlockParam> Content`

                - `required string FileID`

                - `JsonElement Type = "bash_code_execution_output"`

              - `required long ReturnCode`

              - `required string Stderr`

              - `required string Stdout`

              - `JsonElement Type = "bash_code_execution_result"`

          - `required string ToolUseID`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonElement Type = "bash_code_execution_tool_result"`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

        - `class BetaTextEditorCodeExecutionToolResultBlockParam:`

          - `required Content Content`

            - `class BetaTextEditorCodeExecutionToolResultErrorParam:`

              - `required ErrorCode ErrorCode`

                - `InvalidToolInput("invalid_tool_input")`

                - `Unavailable("unavailable")`

                - `TooManyRequests("too_many_requests")`

                - `ExecutionTimeExceeded("execution_time_exceeded")`

                - `FileNotFound("file_not_found")`

              - `JsonElement Type = "text_editor_code_execution_tool_result_error"`

              - `string? ErrorMessage`

            - `class BetaTextEditorCodeExecutionViewResultBlockParam:`

              - `required string Content`

              - `required FileType FileType`

                - `Text("text")`

                - `Image("image")`

                - `Pdf("pdf")`

              - `JsonElement Type = "text_editor_code_execution_view_result"`

              - `long? NumLines`

              - `long? StartLine`

              - `long? TotalLines`

            - `class BetaTextEditorCodeExecutionCreateResultBlockParam:`

              - `required bool IsFileUpdate`

              - `JsonElement Type = "text_editor_code_execution_create_result"`

            - `class BetaTextEditorCodeExecutionStrReplaceResultBlockParam:`

              - `JsonElement Type = "text_editor_code_execution_str_replace_result"`

              - `IReadOnlyList<string>? Lines`

              - `long? NewLines`

              - `long? NewStart`

              - `long? OldLines`

              - `long? OldStart`

          - `required string ToolUseID`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonElement Type = "text_editor_code_execution_tool_result"`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

        - `class BetaToolSearchToolResultBlockParam:`

          - `required Content Content`

            - `class BetaToolSearchToolResultErrorParam:`

              - `required ErrorCode ErrorCode`

                - `InvalidToolInput("invalid_tool_input")`

                - `Unavailable("unavailable")`

                - `TooManyRequests("too_many_requests")`

                - `ExecutionTimeExceeded("execution_time_exceeded")`

              - `JsonElement Type = "tool_search_tool_result_error"`

              - `string? ErrorMessage`

            - `class BetaToolSearchToolSearchResultBlockParam:`

              - `required IReadOnlyList<BetaToolReferenceBlockParam> ToolReferences`

                - `required string ToolName`

                  maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

                - `JsonElement Type = "tool_reference"`

                - `BetaCacheControlEphemeral? CacheControl`

                  Create a cache control breakpoint at this content block.

              - `JsonElement Type = "tool_search_tool_search_result"`

          - `required string ToolUseID`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonElement Type = "tool_search_tool_result"`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

        - `class BetaMcpToolUseBlockParam:`

          - `required string ID`

            pattern: ^[a-zA-Z0-9_-]+$

          - `required IReadOnlyDictionary<string, JsonElement> Input`

          - `required string Name`

          - `required string ServerName`

            The name of the MCP server

          - `JsonElement Type = "mcp_tool_use"`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

        - `class BetaRequestMcpToolResultBlockParam:`

          - `required string ToolUseID`

            pattern: ^[a-zA-Z0-9_-]+$

          - `JsonElement Type = "mcp_tool_result"`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `Content Content`

            - `string`

            - `IReadOnlyList<BetaTextBlockParam>`

              - `required string Text`

                minLength: 1

              - `JsonElement Type = "text"`

              - `BetaCacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

              - `IReadOnlyList<BetaTextCitationParam>? Citations`

          - `bool IsError`

        - `class BetaContainerUploadBlockParam:`

          A content block that represents a file to be uploaded to the container
          Files uploaded via this block will be available in the container's input directory.

          - `required string FileID`

          - `JsonElement Type = "container_upload"`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

        - `class BetaCompactionBlockParam:`

          A compaction block containing summary of previous context.

          Users should round-trip these blocks from responses to subsequent requests
          to maintain context across compaction boundaries.

          When content is None, the block represents a failed compaction. The server
          treats these as no-ops. Empty string content is not allowed.

          - `JsonElement Type = "compaction"`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `string? Content`

            Summary of previously compacted content, or null if compaction failed

          - `string? EncryptedContent`

            Opaque metadata from prior compaction, to be round-tripped verbatim

        - `class BetaRequestToolAdditionBlock:`

          Mid-conversation directive to surface a declared tool.

          `tool` references a tool (or MCP toolset) by name from the request's
          `tools`; it is offered to the model from this point in the
          conversation onward.

          - `required Tool Tool`

            Reference to a single tool the caller declared directly in
            `tools[]`. Does not accept the composed `{server}_{name}` form the
            server assigns to MCP-resolved tools — use `mcp_tool_reference` or
            `mcp_toolset_reference` for those.

            - `class BetaToolChangeToolReference:`

              Reference to a single tool the caller declared directly in
              `tools[]`. Does not accept the composed `{server}_{name}` form the
              server assigns to MCP-resolved tools — use `mcp_tool_reference` or
              `mcp_toolset_reference` for those.

              - `required string Name`

                pattern: ^[a-zA-Z0-9_-]{1,128}$

              - `JsonElement Type = "tool_reference"`

            - `class BetaToolChangeMcpToolReference:`

              Reference to a single MCP tool by its server and remote name — the
              same `server_name`/`name` pair `mcp_tool_use` carries.

              - `required string Name`

              - `required string ServerName`

              - `JsonElement Type = "mcp_tool_reference"`

            - `class BetaToolChangeMcpToolsetReference:`

              Reference to every tool in the named MCP server's toolset.

              - `required string ServerName`

              - `JsonElement Type = "mcp_toolset_reference"`

          - `JsonElement Type = "tool_addition"`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

        - `class BetaRequestToolRemovalBlock:`

          Mid-conversation directive to withdraw a tool.

          `tool` references a tool (or MCP toolset) by name from the request's
          `tools`; it is no longer offered to the model from this point in the
          conversation onward.

          - `required Tool Tool`

            Reference to a single tool the caller declared directly in
            `tools[]`. Does not accept the composed `{server}_{name}` form the
            server assigns to MCP-resolved tools — use `mcp_tool_reference` or
            `mcp_toolset_reference` for those.

            - `class BetaToolChangeToolReference:`

              Reference to a single tool the caller declared directly in
              `tools[]`. Does not accept the composed `{server}_{name}` form the
              server assigns to MCP-resolved tools — use `mcp_tool_reference` or
              `mcp_toolset_reference` for those.

            - `class BetaToolChangeMcpToolReference:`

              Reference to a single MCP tool by its server and remote name — the
              same `server_name`/`name` pair `mcp_tool_use` carries.

            - `class BetaToolChangeMcpToolsetReference:`

              Reference to every tool in the named MCP server's toolset.

          - `JsonElement Type = "tool_removal"`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

        - `class BetaFallbackBlockParam:`

          A `fallback` block echoed back from a prior response.

          Accepted in `messages[].content` and not rendered into the prompt; not
          validated against the request's `fallbacks` chain or top-level `model`.

          Echo the assistant turn back verbatim, including this block in its
          original position. The block marks the boundary between content produced
          before and after a fallback hop, and the server relies on that boundary
          to validate the turn: when thinking runs flank the boundary, omitting
          the block merges them into one span the server cannot validate (the
          request is rejected), and moving it into the middle of a single run is
          likewise rejected; between non-thinking blocks the block's placement has
          no validation effect.

          - `required BetaFallbackInfoParam From`

            Identifies one hop of a fallback transition.

            - `required Model Model`

              The model that will complete your prompt.

              See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

              - `ClaudeFable5_1("claude-fable-5-1")`

                Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

              - `ClaudeMythos5_1("claude-mythos-5-1")`

                Our most capable model for cybersecurity and biology research, available through trusted access programs

              - `ClaudeSonnet5("claude-sonnet-5")`

                High-performance model for coding and agents

              - `ClaudeFable5("claude-fable-5")`

                Next generation of intelligence for the hardest knowledge work and coding problems

              - `ClaudeMythos5("claude-mythos-5")`

                Most capable model for cybersecurity and biology research

              - `ClaudeOpus5("claude-opus-5")`

                Powerful intelligence for long-running agents and coding

              - `ClaudeOpus4_8("claude-opus-4-8")`

                Powerful intelligence for long-running agents and coding

              - `ClaudeOpus4_7("claude-opus-4-7")`

                Powerful intelligence for long-running agents and coding

              - `ClaudeMythosPreview("claude-mythos-preview")`

                New class of intelligence, strongest in coding and cybersecurity

              - `ClaudeOpus4_6("claude-opus-4-6")`

                Powerful intelligence for long-running agents and coding

              - `ClaudeSonnet4_6("claude-sonnet-4-6")`

                Best combination of speed and intelligence

              - `ClaudeHaiku4_5("claude-haiku-4-5")`

                Fastest model with near-frontier intelligence

              - `ClaudeHaiku4_5_20251001("claude-haiku-4-5-20251001")`

                Fastest model with near-frontier intelligence

              - `ClaudeOpus4_5("claude-opus-4-5")`

                Powerful intelligence for long-running agents and coding

              - `ClaudeOpus4_5_20251101("claude-opus-4-5-20251101")`

                Powerful intelligence for long-running agents and coding

              - `ClaudeSonnet4_5("claude-sonnet-4-5")`

                High-performance model for agents and coding

              - `ClaudeSonnet4_5_20250929("claude-sonnet-4-5-20250929")`

                High-performance model for agents and coding

          - `required BetaFallbackInfoParam To`

            Identifies one hop of a fallback transition.

          - `JsonElement Type = "fallback"`

          - `JsonElement Trigger`

            The response block's `trigger`, echoed verbatim. Accepted and ignored by the server; any object or `null` is allowed.

    - `required Role Role`

      - `User("user")`

      - `Assistant("assistant")`

      - `System("system")`

    - `ClearAt? ClearAt`

      How long this system message's text stays in front of the model. `"never"` (the default) renders it on every request that includes it. `"next_user_message"` renders it only for the user turn it follows: once a later `role: "user"` message exists in `messages` the message stays in the array (send it unchanged) but is no longer shown to the model. Only permitted on `role: "system"` messages.

      - `NextUserMessage("next_user_message")`

      - `Never("never")`

    - `BetaSystemMessageOutputConfig? OutputConfig`

      Per-message output configuration on a role:"system" input message.

      Fields here apply per-turn; `format` remains top-level only. An
      empty `{}` is accepted on a message that carries content; a message
      with neither content nor output_config fields is rejected.

      - `Effort? Effort`

        All possible effort levels.

        - `Low("low")`

        - `Medium("medium")`

        - `High("high")`

        - `Xhigh("xhigh")`

        - `Max("max")`

  - `required Model model`

    Body param: The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `BetaCacheControlEphemeral? cacheControl`

    Body param: Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

  - `Container? container`

    Body param: Container identifier for reuse across requests.

    - `class BetaContainerParams:`

      Container parameters with skills to be loaded.

      - `string? ID`

        Container id

      - `IReadOnlyList<BetaSkillParams>? Skills`

        List of skills to load in the container

        maxItems: 20

        - `required string SkillID`

          Skill ID

          maxLength: 64, minLength: 1

        - `required Type Type`

          Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

          - `Anthropic("anthropic")`

          - `Custom("custom")`

        - `string Version`

          Skill version or 'latest' for most recent version

          maxLength: 64, minLength: 1

    - `string`

  - `BetaContextManagementConfig? contextManagement`

    Body param: Context management configuration.

    This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.

  - `BetaDiagnosticsParam? diagnostics`

    Body param: Request-level diagnostics. Currently carries the previous response
    id for prompt-cache divergence reporting.

  - `FallbackCreditToken? fallbackCreditToken`

    Body param: The `fallback_credit_token` from a prior refusal's `stop_details`.

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

    - `string`

    - `class BetaFallbackCreditTokenParam:`

      Object form of `fallback_credit_token`: the token plus a redemption
      mode.

      Requires `anthropic-beta: fallback-credit-2026-07-01`; without that
      header the field accepts the bare string only. The bare string and the
      mode-less object are equivalent (both select `strict`), so wrapping
      an existing token changes nothing by itself.

      - `required string Token`

        The opaque `fallback_credit_token` from a prior refusal's `stop_details` — the same string the bare-string form carries.

        maxLength: 2048, minLength: 1

      - `Mode Mode`

        How a failing token affects the retry. `strict` (the default, and the bare-string behavior): a failing redemption is a 400 and the retry is not served. `best_effort`: the retry is served either way — a token-layer failure no longer rejects the request; the retry proceeds at normal price and the outcome is reported on the response's `usage.fallback_credit`. Two failures stay hard in both modes: a malformed token, and combining `fallback_credit_token` with `fallbacks`.

        - `Strict("strict")`

        - `BestEffort("best_effort")`

  - `BetaFallbacksParam? fallbacks`

    Body param: Opt-in server-side retry on one or more substitute models when the requested model declines for policy reasons. Tried in order: if the first entry also declines, the second is tried, and so on. The string "default" requests the requested model's server-defined default fallback configuration.

  - `string? inferenceGeo`

    Body param: Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

  - `IReadOnlyList<BetaRequestMcpServerUrlDefinition> mcpServers`

    Body param: MCP servers to be utilized in this request

    maxItems: 20

    - `required string Name`

    - `JsonElement Type = "url"`

    - `required string Url`

    - `string? AuthorizationToken`

    - `BetaRequestMcpServerToolConfiguration? ToolConfiguration`

      - `IReadOnlyList<string>? AllowedTools`

      - `bool? Enabled`

  - `BetaMetadata metadata`

    Body param: An object describing metadata about the request.

  - `BetaOutputConfig outputConfig`

    Body param: Configuration options for the model's output, such as the output format.

  - `ServiceTier serviceTier`

    Body param: Determines whether to use priority capacity (if available) or standard capacity for this request.

    Anthropic offers different levels of service for your API requests. See [service-tiers](https://platform.claude.com/docs/en/api/service-tiers) for details.

    - `Auto("auto")`

    - `StandardOnly("standard_only")`

  - `Speed? speed`

    Body param: Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `Standard("standard")`

    - `Fast("fast")`

  - `IReadOnlyList<string> stopSequences`

    Body param: Custom text sequences that will cause the model to stop generating.

    Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

    If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

  - `System system`

    Body param: System prompt.

    A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role).

    - `string`

    - `IReadOnlyList<BetaTextBlockParam>`

      - `required string Text`

        minLength: 1

      - `JsonElement Type = "text"`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `IReadOnlyList<BetaTextCitationParam>? Citations`

  - `BetaThinkingConfigParam thinking`

    Body param: Configuration for enabling Claude's extended thinking.

    When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

    See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

  - `BetaToolChoice toolChoice`

    Body param: How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

  - `IReadOnlyList<BetaToolUnion> tools`

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

    - `class BetaTool:`

      - `required InputSchema InputSchema`

        [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

        This defines the shape of the `input` that your tool accepts and that the model will produce.

        - `JsonElement Type = "object"`

        - `IReadOnlyDictionary<string, JsonElement>? Properties`

        - `IReadOnlyList<string>? Required`

      - `required string Name`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

        maxLength: 128, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,128}$

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct("direct")`

        - `CodeExecution20250825("code_execution_20250825")`

        - `CodeExecution20260120("code_execution_20260120")`

        - `CodeExecution20260521("code_execution_20260521")`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `string Description`

        Description of what this tool does.

        Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

      - `bool? EagerInputStreaming`

        Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

      - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

      - `Type? Type`

    - `class BetaToolBash20241022:`

      - `JsonElement Name = "bash"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type = "bash_20241022"`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct("direct")`

        - `CodeExecution20250825("code_execution_20250825")`

        - `CodeExecution20260120("code_execution_20260120")`

        - `CodeExecution20260521("code_execution_20260521")`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaToolBash20250124:`

      - `JsonElement Name = "bash"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type = "bash_20250124"`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct("direct")`

        - `CodeExecution20250825("code_execution_20250825")`

        - `CodeExecution20260120("code_execution_20260120")`

        - `CodeExecution20260521("code_execution_20260521")`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaCodeExecutionTool20250522:`

      - `JsonElement Name = "code_execution"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type = "code_execution_20250522"`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct("direct")`

        - `CodeExecution20250825("code_execution_20250825")`

        - `CodeExecution20260120("code_execution_20260120")`

        - `CodeExecution20260521("code_execution_20260521")`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaCodeExecutionTool20250825:`

      - `JsonElement Name = "code_execution"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type = "code_execution_20250825"`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct("direct")`

        - `CodeExecution20250825("code_execution_20250825")`

        - `CodeExecution20260120("code_execution_20260120")`

        - `CodeExecution20260521("code_execution_20260521")`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaCodeExecutionTool20260120:`

      Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

      - `JsonElement Name = "code_execution"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type = "code_execution_20260120"`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct("direct")`

        - `CodeExecution20250825("code_execution_20250825")`

        - `CodeExecution20260120("code_execution_20260120")`

        - `CodeExecution20260521("code_execution_20260521")`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaCodeExecutionTool20260521:`

      Code execution tool with REPL state persistence.

      - `JsonElement Name = "code_execution"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type = "code_execution_20260521"`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct("direct")`

        - `CodeExecution20250825("code_execution_20250825")`

        - `CodeExecution20260120("code_execution_20260120")`

        - `CodeExecution20260521("code_execution_20260521")`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaBrowserToolset20260801:`

      The browser toolset: a single `tools[]` entry (carrying no
      `name`) that declares the browser tool family. The model is served
      the family's tool with any members disabled via `configs` removed
      from its schema.

      - `JsonElement Type = "browser_toolset_20260801"`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `BetaBrowserToolsetConfigs? Configs`

        Per-member configuration for `browser_toolset_20260801`: one
        optional field per member tool, keyed by the member name — the same
        name the member's `tool_use` blocks carry. Every member is an
        accepted key, and a member's defaults apply wherever its key is
        absent. Unknown keys are rejected: the field set is this toolset
        version's complete member set.

        - `BetaBrowserCloseTabConfig? CloseTab`

          `close_tab`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaBrowserDoubleClickConfig? DoubleClick`

          `double_click`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaBrowserFileUploadConfig? FileUpload`

          `file_upload`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaBrowserFindConfig? Find`

          `find`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaBrowserFormInputConfig? FormInput`

          `form_input`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaBrowserGetPageTextConfig? GetPageText`

          `get_page_text`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaBrowserHoldKeyConfig? HoldKey`

          `hold_key`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaBrowserHoverConfig? Hover`

          `hover`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaBrowserJavascriptExecConfig? JavascriptExec`

          `javascript_exec`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaBrowserKeyConfig? Key`

          `key`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaBrowserLeftClickConfig? LeftClick`

          `left_click`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaBrowserLeftClickDragConfig? LeftClickDrag`

          `left_click_drag`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaBrowserLeftMouseDownConfig? LeftMouseDown`

          `left_mouse_down`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaBrowserLeftMouseUpConfig? LeftMouseUp`

          `left_mouse_up`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaBrowserListTabsConfig? ListTabs`

          `list_tabs`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaBrowserMiddleClickConfig? MiddleClick`

          `middle_click`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaBrowserMouseMoveConfig? MouseMove`

          `mouse_move`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaBrowserNavigateConfig? Navigate`

          `navigate`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaBrowserNewTabConfig? NewTab`

          `new_tab`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaBrowserReadConsoleConfig? ReadConsole`

          `read_console`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaBrowserReadNetworkConfig? ReadNetwork`

          `read_network`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaBrowserReadPageConfig? ReadPage`

          `read_page`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaBrowserRightClickConfig? RightClick`

          `right_click`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaBrowserScreenshotConfig? Screenshot`

          `screenshot`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaBrowserScrollConfig? Scroll`

          `scroll`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaBrowserScrollToConfig? ScrollTo`

          `scroll_to`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaBrowserSwitchTabConfig? SwitchTab`

          `switch_tab`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaBrowserTripleClickConfig? TripleClick`

          `triple_click`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaBrowserTypeConfig? Type`

          `type`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaBrowserWaitConfig? Wait`

          `wait`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaBrowserZoomConfig? Zoom`

          `zoom`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `class BetaToolComputerUse20241022:`

      - `required long DisplayHeightPx`

        The height of the display in pixels.

        minimum: 1

      - `required long DisplayWidthPx`

        The width of the display in pixels.

        minimum: 1

      - `JsonElement Name = "computer"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type = "computer_20241022"`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct("direct")`

        - `CodeExecution20250825("code_execution_20250825")`

        - `CodeExecution20260120("code_execution_20260120")`

        - `CodeExecution20260521("code_execution_20260521")`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `long? DisplayNumber`

        The X11 display number (e.g. 0, 1) for the display.

        minimum: 0

      - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaMemoryTool20250818:`

      - `JsonElement Name = "memory"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type = "memory_20250818"`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct("direct")`

        - `CodeExecution20250825("code_execution_20250825")`

        - `CodeExecution20260120("code_execution_20260120")`

        - `CodeExecution20260521("code_execution_20260521")`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaToolComputerUse20250124:`

      - `required long DisplayHeightPx`

        The height of the display in pixels.

        minimum: 1

      - `required long DisplayWidthPx`

        The width of the display in pixels.

        minimum: 1

      - `JsonElement Name = "computer"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type = "computer_20250124"`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct("direct")`

        - `CodeExecution20250825("code_execution_20250825")`

        - `CodeExecution20260120("code_execution_20260120")`

        - `CodeExecution20260521("code_execution_20260521")`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `long? DisplayNumber`

        The X11 display number (e.g. 0, 1) for the display.

        minimum: 0

      - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaToolTextEditor20241022:`

      - `JsonElement Name = "str_replace_editor"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type = "text_editor_20241022"`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct("direct")`

        - `CodeExecution20250825("code_execution_20250825")`

        - `CodeExecution20260120("code_execution_20260120")`

        - `CodeExecution20260521("code_execution_20260521")`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaToolComputerUse20251124:`

      - `required long DisplayHeightPx`

        The height of the display in pixels.

        minimum: 1

      - `required long DisplayWidthPx`

        The width of the display in pixels.

        minimum: 1

      - `JsonElement Name = "computer"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type = "computer_20251124"`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct("direct")`

        - `CodeExecution20250825("code_execution_20250825")`

        - `CodeExecution20260120("code_execution_20260120")`

        - `CodeExecution20260521("code_execution_20260521")`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `long? DisplayNumber`

        The X11 display number (e.g. 0, 1) for the display.

        minimum: 0

      - `bool EnableZoom`

        Whether to enable an action to take a zoomed-in screenshot of the screen.

      - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaComputerToolset20260801:`

      The computer toolset: a single `tools[]` entry (carrying no
      `name`) that declares the computer tool family. The model is
      served the family's tool with any members disabled via `configs`
      removed from its schema. Every member is enabled by default, zoom
      included. The single-tool options `display_number` and
      `enable_zoom` are not fields of a toolset entry — it carries only
      `type`, `configs`, and `cache_control`; zoom is controlled
      via `configs.zoom.enabled`.

      - `JsonElement Type = "computer_toolset_20260801"`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `BetaComputerToolsetConfigs? Configs`

        Per-member configuration for `computer_toolset_20260801`: one
        optional field per member tool, keyed by the member name — the same
        name the member's `tool_use` blocks carry. Every member is an
        accepted key, and a member's defaults apply wherever its key is
        absent. Unknown keys are rejected: the field set is this toolset
        version's complete member set.

        - `BetaComputerCursorPositionConfig? CursorPosition`

          `cursor_position`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaComputerDoubleClickConfig? DoubleClick`

          `double_click`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaComputerHoldKeyConfig? HoldKey`

          `hold_key`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaComputerKeyConfig? Key`

          `key`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaComputerLeftClickConfig? LeftClick`

          `left_click`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaComputerLeftClickDragConfig? LeftClickDrag`

          `left_click_drag`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaComputerLeftMouseDownConfig? LeftMouseDown`

          `left_mouse_down`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaComputerLeftMouseUpConfig? LeftMouseUp`

          `left_mouse_up`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaComputerMiddleClickConfig? MiddleClick`

          `middle_click`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaComputerMouseMoveConfig? MouseMove`

          `mouse_move`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaComputerRightClickConfig? RightClick`

          `right_click`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaComputerScreenshotConfig? Screenshot`

          `screenshot`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaComputerScrollConfig? Scroll`

          `scroll`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaComputerTripleClickConfig? TripleClick`

          `triple_click`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaComputerTypeConfig? Type`

          `type`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaComputerWaitConfig? Wait`

          `wait`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `BetaComputerZoomConfig? Zoom`

          `zoom`'s config overrides.

          - `bool? DeferLoading`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `bool? Enabled`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `class BetaToolTextEditor20250124:`

      - `JsonElement Name = "str_replace_editor"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type = "text_editor_20250124"`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct("direct")`

        - `CodeExecution20250825("code_execution_20250825")`

        - `CodeExecution20260120("code_execution_20260120")`

        - `CodeExecution20260521("code_execution_20260521")`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaToolTextEditor20250429:`

      - `JsonElement Name = "str_replace_based_edit_tool"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type = "text_editor_20250429"`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct("direct")`

        - `CodeExecution20250825("code_execution_20250825")`

        - `CodeExecution20260120("code_execution_20260120")`

        - `CodeExecution20260521("code_execution_20260521")`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaToolTextEditor20250728:`

      - `JsonElement Name = "str_replace_based_edit_tool"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type = "text_editor_20250728"`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct("direct")`

        - `CodeExecution20250825("code_execution_20250825")`

        - `CodeExecution20260120("code_execution_20260120")`

        - `CodeExecution20260521("code_execution_20260521")`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

      - `long? MaxCharacters`

        Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

        minimum: 1

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaWebSearchTool20250305:`

      - `JsonElement Name = "web_search"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type = "web_search_20250305"`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct("direct")`

        - `CodeExecution20250825("code_execution_20250825")`

        - `CodeExecution20260120("code_execution_20260120")`

        - `CodeExecution20260521("code_execution_20260521")`

      - `IReadOnlyList<string>? AllowedDomains`

        If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

      - `IReadOnlyList<string>? BlockedDomains`

        If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `long? MaxUses`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

      - `BetaUserLocation? UserLocation`

        Parameters for the user's location. Used to provide more relevant search results.

        - `JsonElement Type = "approximate"`

        - `string? City`

          The city of the user.

          maxLength: 255, minLength: 1

        - `string? Country`

          The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

          maxLength: 2, minLength: 2

        - `string? Region`

          The region of the user.

          maxLength: 255, minLength: 1

        - `string? Timezone`

          The [IANA timezone](https://nodatime.org/TimeZones) of the user.

          maxLength: 255, minLength: 1

    - `class BetaWebFetchTool20250910:`

      - `JsonElement Name = "web_fetch"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type = "web_fetch_20250910"`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct("direct")`

        - `CodeExecution20250825("code_execution_20250825")`

        - `CodeExecution20260120("code_execution_20260120")`

        - `CodeExecution20260521("code_execution_20260521")`

      - `IReadOnlyList<string>? AllowedDomains`

        List of domains to allow fetching from

      - `IReadOnlyList<string>? BlockedDomains`

        List of domains to block fetching from

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `BetaCitationsConfigParam? Citations`

        Citations configuration for fetched documents. Citations are disabled by default.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `long? MaxContentTokens`

        Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

        exclusiveMinimum: 0

      - `long? MaxUses`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaWebSearchTool20260209:`

      - `JsonElement Name = "web_search"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type = "web_search_20260209"`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct("direct")`

        - `CodeExecution20250825("code_execution_20250825")`

        - `CodeExecution20260120("code_execution_20260120")`

        - `CodeExecution20260521("code_execution_20260521")`

      - `IReadOnlyList<string>? AllowedDomains`

        If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

      - `IReadOnlyList<string>? BlockedDomains`

        If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `long? MaxUses`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

      - `BetaUserLocation? UserLocation`

        Parameters for the user's location. Used to provide more relevant search results.

    - `class BetaWebFetchTool20260209:`

      - `JsonElement Name = "web_fetch"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type = "web_fetch_20260209"`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct("direct")`

        - `CodeExecution20250825("code_execution_20250825")`

        - `CodeExecution20260120("code_execution_20260120")`

        - `CodeExecution20260521("code_execution_20260521")`

      - `IReadOnlyList<string>? AllowedDomains`

        List of domains to allow fetching from

      - `IReadOnlyList<string>? BlockedDomains`

        List of domains to block fetching from

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `BetaCitationsConfigParam? Citations`

        Citations configuration for fetched documents. Citations are disabled by default.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `long? MaxContentTokens`

        Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

        exclusiveMinimum: 0

      - `long? MaxUses`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaWebFetchTool20260309:`

      Web fetch tool with use_cache parameter for bypassing cached content.

      - `JsonElement Name = "web_fetch"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type = "web_fetch_20260309"`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct("direct")`

        - `CodeExecution20250825("code_execution_20250825")`

        - `CodeExecution20260120("code_execution_20260120")`

        - `CodeExecution20260521("code_execution_20260521")`

      - `IReadOnlyList<string>? AllowedDomains`

        List of domains to allow fetching from

      - `IReadOnlyList<string>? BlockedDomains`

        List of domains to block fetching from

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `BetaCitationsConfigParam? Citations`

        Citations configuration for fetched documents. Citations are disabled by default.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `long? MaxContentTokens`

        Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

        exclusiveMinimum: 0

      - `long? MaxUses`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

      - `bool UseCache`

        Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

    - `class BetaWebSearchTool20260318:`

      - `JsonElement Name = "web_search"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type = "web_search_20260318"`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct("direct")`

        - `CodeExecution20250825("code_execution_20250825")`

        - `CodeExecution20260120("code_execution_20260120")`

        - `CodeExecution20260521("code_execution_20260521")`

      - `IReadOnlyList<string>? AllowedDomains`

        If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

      - `IReadOnlyList<string>? BlockedDomains`

        If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `long? MaxUses`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `ResponseInclusion ResponseInclusion`

        How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

        - `Full("full")`

        - `Excluded("excluded")`

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

      - `BetaUserLocation? UserLocation`

        Parameters for the user's location. Used to provide more relevant search results.

    - `class BetaWebFetchTool20260318:`

      - `JsonElement Name = "web_fetch"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type = "web_fetch_20260318"`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct("direct")`

        - `CodeExecution20250825("code_execution_20250825")`

        - `CodeExecution20260120("code_execution_20260120")`

        - `CodeExecution20260521("code_execution_20260521")`

      - `IReadOnlyList<string>? AllowedDomains`

        List of domains to allow fetching from

      - `IReadOnlyList<string>? BlockedDomains`

        List of domains to block fetching from

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `BetaCitationsConfigParam? Citations`

        Citations configuration for fetched documents. Citations are disabled by default.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `long? MaxContentTokens`

        Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

        exclusiveMinimum: 0

      - `long? MaxUses`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `ResponseInclusion ResponseInclusion`

        How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

        - `Full("full")`

        - `Excluded("excluded")`

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

      - `bool UseCache`

        Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

    - `class BetaAdvisorTool20260301:`

      - `required Model Model`

        The model that will complete your prompt.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `JsonElement Name = "advisor"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `JsonElement Type = "advisor_20260301"`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct("direct")`

        - `CodeExecution20250825("code_execution_20250825")`

        - `CodeExecution20260120("code_execution_20260120")`

        - `CodeExecution20260521("code_execution_20260521")`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `BetaCacheControlEphemeral? Caching`

        Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `long? MaxTokens`

        Bounds the advisor's total output (thinking + text) per call. When the advisor hits this cap, the returned advisor_result or advisor_redacted_result block carries stop_reason='max_tokens', and a truncation note is appended to the advice text the worker model sees (inside the encrypted blob in redacted mode). When set, the server also emits a remaining-tokens budget block in the advisor's prompt so the advisor self-shapes toward the cap. When omitted, the advisor model's default output cap applies and no budget block is emitted.

        minimum: 1024

      - `long? MaxUses`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaToolSearchToolBm25_20251119:`

      - `JsonElement Name = "tool_search_tool_bm25"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `required Type Type`

        - `ToolSearchToolBm25_20251119("tool_search_tool_bm25_20251119")`

        - `ToolSearchToolBm25("tool_search_tool_bm25")`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct("direct")`

        - `CodeExecution20250825("code_execution_20250825")`

        - `CodeExecution20260120("code_execution_20260120")`

        - `CodeExecution20260521("code_execution_20260521")`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaToolSearchToolRegex20251119:`

      - `JsonElement Name = "tool_search_tool_regex"`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `required Type Type`

        - `ToolSearchToolRegex20251119("tool_search_tool_regex_20251119")`

        - `ToolSearchToolRegex("tool_search_tool_regex")`

      - `IReadOnlyList<AllowedCaller> AllowedCallers`

        - `Direct("direct")`

        - `CodeExecution20250825("code_execution_20250825")`

        - `CodeExecution20260120("code_execution_20260120")`

        - `CodeExecution20260521("code_execution_20260521")`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `bool DeferLoading`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `bool Strict`

        When true, guarantees schema validation on tool names and inputs

    - `class BetaMcpToolset:`

      Configuration for a group of tools from an MCP server.

      Allows configuring enabled status and defer_loading for all tools
      from an MCP server, with optional per-tool overrides.

      - `required string McpServerName`

        Name of the MCP server to configure tools for

        maxLength: 255, minLength: 1

      - `JsonElement Type = "mcp_toolset"`

      - `BetaCacheControlEphemeral? CacheControl`

        Create a cache control breakpoint at this content block.

      - `IReadOnlyDictionary<string, BetaMcpToolConfig>? Configs`

        Configuration overrides for specific tools, keyed by tool name

        - `bool DeferLoading`

        - `bool Enabled`

      - `BetaMcpToolDefaultConfig DefaultConfig`

        Default configuration applied to all tools from this server

        - `bool DeferLoading`

        - `bool Enabled`

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

  - `string userProfileID`

    Header param: The user profile ID to attribute this request to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header.

  - `BetaJsonOutputFormat? outputFormat`

    **Deprecated**

    Body param: Deprecated: Use `output_config.format` instead. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

    A schema to specify Claude's output format in responses. This parameter will be removed in a future release.

  - `double temperature`

    **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not support setting temperature. A value of 1.0 of will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

    Body param: Amount of randomness injected into the response.

    Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

    Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

    maximum: 1, minimum: 0

  - `long topK`

    **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not accept top_k; any value will be rejected with a 400 error.

    Body param: Only sample from the top K options for each subsequent token.

    Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

    Recommended for advanced use cases only.

    minimum: 0

  - `double topP`

    **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not support setting top_p. A value >= 0.99 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

    Body param: Use nucleus sampling.

    In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.

    Recommended for advanced use cases only.

    maximum: 1, minimum: 0

## Returns

- `class BetaMessage:`

  - `required string ID`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `required BetaContainer? Container`

    Information about the container used in the request (for the code execution tool)

    - `required string ID`

      Identifier for the container used in this request

    - `required DateTimeOffset ExpiresAt`

      The time at which the container will expire.

      format: date-time

    - `required IReadOnlyList<BetaContainerSkill>? Skills`

      Skills loaded in the container

      - `required string SkillID`

        Skill ID

        maxLength: 64, minLength: 1

      - `required Type Type`

        Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

        - `Anthropic("anthropic")`

        - `Custom("custom")`

      - `required string Version`

        The resolved version: a skill version ID for custom skills.

        maxLength: 64, minLength: 1

  - `required IReadOnlyList<BetaContentBlock> Content`

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

    - `class BetaTextBlock:`

      - `required IReadOnlyList<BetaTextCitation>? Citations`

        Citations supporting the text block.

        The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

        - `class BetaCitationCharLocation:`

          - `required string CitedText`

          - `required long DocumentIndex`

            minimum: 0

          - `required string? DocumentTitle`

          - `required long EndCharIndex`

          - `required string? FileID`

          - `required long StartCharIndex`

            minimum: 0

          - `JsonElement Type = "char_location"`

        - `class BetaCitationPageLocation:`

          - `required string CitedText`

          - `required long DocumentIndex`

            minimum: 0

          - `required string? DocumentTitle`

          - `required long EndPageNumber`

          - `required string? FileID`

          - `required long StartPageNumber`

            minimum: 1

          - `JsonElement Type = "page_location"`

        - `class BetaCitationContentBlockLocation:`

          - `required string CitedText`

            The full text of the cited block range, concatenated.

            Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

          - `required long DocumentIndex`

            minimum: 0

          - `required string? DocumentTitle`

          - `required long EndBlockIndex`

            Exclusive 0-based end index of the cited block range in the source's `content` array.

            Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

          - `required string? FileID`

          - `required long StartBlockIndex`

            0-based index of the first cited block in the source's `content` array.

            minimum: 0

          - `JsonElement Type = "content_block_location"`

        - `class BetaCitationsWebSearchResultLocation:`

          - `required string CitedText`

          - `required string EncryptedIndex`

          - `required string? Title`

            maxLength: 512

          - `JsonElement Type = "web_search_result_location"`

          - `required string Url`

        - `class BetaCitationSearchResultLocation:`

          - `required string CitedText`

            The full text of the cited block range, concatenated.

            Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

          - `required long EndBlockIndex`

            Exclusive 0-based end index of the cited block range in the source's `content` array.

            Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

          - `required long SearchResultIndex`

            0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

            Counted separately from `document_index`; server-side web search results are not included in this count.

            minimum: 0

          - `required string Source`

          - `required long StartBlockIndex`

            0-based index of the first cited block in the source's `content` array.

            minimum: 0

          - `required string? Title`

          - `JsonElement Type = "search_result_location"`

      - `required string Text`

        maxLength: 5000000, minLength: 0

      - `JsonElement Type = "text"`

    - `class BetaThinkingBlock:`

      - `required string Signature`

        A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

        This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

        See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

      - `required string Thinking`

        The text of Claude's thinking process for this block.

      - `JsonElement Type = "thinking"`

    - `class BetaRedactedThinkingBlock:`

      - `required string Data`

        The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

        Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

        See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

      - `JsonElement Type = "redacted_thinking"`

    - `class BetaToolUseBlock:`

      - `required string ID`

        pattern: ^[a-zA-Z0-9_-]+$

      - `required IReadOnlyDictionary<string, JsonElement> Input`

      - `required string Name`

        minLength: 1

      - `JsonElement Type = "tool_use"`

      - `Caller Caller`

        Tool invocation directly from the model.

        - `class BetaDirectCaller:`

          Tool invocation directly from the model.

          - `JsonElement Type = "direct"`

        - `class BetaServerToolCaller:`

          Tool invocation generated by a server-side tool.

          - `required string ToolID`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonElement Type = "code_execution_20250825"`

        - `class BetaServerToolCaller20260120:`

          - `required string ToolID`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `JsonElement Type = "code_execution_20260120"`

      - `string? ToolsetName`

        For a toolset member tool_use, the toolset family.

        maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

    - `class BetaServerToolUseBlock:`

      - `required string ID`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `required IReadOnlyDictionary<string, JsonElement> Input`

      - `required Name Name`

        - `Advisor("advisor")`

        - `WebSearch("web_search")`

        - `WebFetch("web_fetch")`

        - `CodeExecution("code_execution")`

        - `BashCodeExecution("bash_code_execution")`

        - `TextEditorCodeExecution("text_editor_code_execution")`

        - `ToolSearchToolRegex("tool_search_tool_regex")`

        - `ToolSearchToolBm25("tool_search_tool_bm25")`

      - `JsonElement Type = "server_tool_use"`

      - `Caller Caller`

        Tool invocation directly from the model.

        - `class BetaDirectCaller:`

          Tool invocation directly from the model.

        - `class BetaServerToolCaller:`

          Tool invocation generated by a server-side tool.

        - `class BetaServerToolCaller20260120:`

    - `class BetaWebSearchToolResultBlock:`

      - `required BetaWebSearchToolResultBlockContent Content`

        - `class BetaWebSearchToolResultError:`

          - `required BetaWebSearchToolResultErrorCode ErrorCode`

            - `InvalidToolInput("invalid_tool_input")`

            - `Unavailable("unavailable")`

            - `MaxUsesExceeded("max_uses_exceeded")`

            - `TooManyRequests("too_many_requests")`

            - `QueryTooLong("query_too_long")`

            - `RequestTooLarge("request_too_large")`

          - `JsonElement Type = "web_search_tool_result_error"`

        - `IReadOnlyList<BetaWebSearchResultBlock>`

          - `required string EncryptedContent`

          - `required string? PageAge`

          - `required string Title`

          - `JsonElement Type = "web_search_result"`

          - `required string Url`

      - `required string ToolUseID`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonElement Type = "web_search_tool_result"`

      - `Caller Caller`

        Tool invocation directly from the model.

        - `class BetaDirectCaller:`

          Tool invocation directly from the model.

        - `class BetaServerToolCaller:`

          Tool invocation generated by a server-side tool.

        - `class BetaServerToolCaller20260120:`

    - `class BetaWebFetchToolResultBlock:`

      - `required Content Content`

        - `class BetaWebFetchToolResultErrorBlock:`

          - `required BetaWebFetchToolResultErrorCode ErrorCode`

            - `InvalidToolInput("invalid_tool_input")`

            - `UrlTooLong("url_too_long")`

            - `UrlNotAllowed("url_not_allowed")`

            - `UrlNotInPriorContext("url_not_in_prior_context")`

            - `UrlNotAccessible("url_not_accessible")`

            - `UnsupportedContentType("unsupported_content_type")`

            - `TooManyRequests("too_many_requests")`

            - `MaxUsesExceeded("max_uses_exceeded")`

            - `Unavailable("unavailable")`

          - `JsonElement Type = "web_fetch_tool_result_error"`

        - `class BetaWebFetchBlock:`

          - `required BetaDocumentBlock Content`

            - `required BetaCitationConfig? Citations`

              Citation configuration for the document

              - `required bool Enabled`

            - `required Source Source`

              - `class BetaBase64PdfSource:`

                - `required string Data`

                  format: byte

                - `JsonElement MediaType = "application/pdf"`

                - `JsonElement Type = "base64"`

              - `class BetaPlainTextSource:`

                - `required string Data`

                - `JsonElement MediaType = "text/plain"`

                - `JsonElement Type = "text"`

            - `required string? Title`

              The title of the document

            - `JsonElement Type = "document"`

          - `required string? RetrievedAt`

            ISO 8601 timestamp when the content was retrieved

          - `JsonElement Type = "web_fetch_result"`

          - `required string Url`

            Fetched content URL

      - `required string ToolUseID`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonElement Type = "web_fetch_tool_result"`

      - `Caller Caller`

        Tool invocation directly from the model.

        - `class BetaDirectCaller:`

          Tool invocation directly from the model.

        - `class BetaServerToolCaller:`

          Tool invocation generated by a server-side tool.

        - `class BetaServerToolCaller20260120:`

    - `class BetaAdvisorToolResultBlock:`

      - `required Content Content`

        - `class BetaAdvisorToolResultError:`

          - `required ErrorCode ErrorCode`

            - `MaxUsesExceeded("max_uses_exceeded")`

            - `PromptTooLong("prompt_too_long")`

            - `TooManyRequests("too_many_requests")`

            - `Overloaded("overloaded")`

            - `Unavailable("unavailable")`

            - `ExecutionTimeExceeded("execution_time_exceeded")`

            - `ModelNotFound("model_not_found")`

          - `JsonElement Type = "advisor_tool_result_error"`

        - `class BetaAdvisorResultBlock:`

          - `required string? StopReason`

            The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

          - `required string Text`

          - `JsonElement Type = "advisor_result"`

        - `class BetaAdvisorRedactedResultBlock:`

          - `required string EncryptedContent`

            Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

          - `required string? StopReason`

            The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

          - `JsonElement Type = "advisor_redacted_result"`

      - `required string ToolUseID`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonElement Type = "advisor_tool_result"`

    - `class BetaCodeExecutionToolResultBlock:`

      - `required BetaCodeExecutionToolResultBlockContent Content`

        Code execution result with encrypted stdout for PFC + web_search results.

        - `class BetaCodeExecutionToolResultError:`

          - `required BetaCodeExecutionToolResultErrorCode ErrorCode`

            - `InvalidToolInput("invalid_tool_input")`

            - `Unavailable("unavailable")`

            - `TooManyRequests("too_many_requests")`

            - `ExecutionTimeExceeded("execution_time_exceeded")`

          - `JsonElement Type = "code_execution_tool_result_error"`

        - `class BetaCodeExecutionResultBlock:`

          - `required IReadOnlyList<BetaCodeExecutionOutputBlock> Content`

            - `required string FileID`

            - `JsonElement Type = "code_execution_output"`

          - `required long ReturnCode`

          - `required string Stderr`

          - `required string Stdout`

          - `JsonElement Type = "code_execution_result"`

        - `class BetaEncryptedCodeExecutionResultBlock:`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `required IReadOnlyList<BetaCodeExecutionOutputBlock> Content`

            - `required string FileID`

            - `JsonElement Type = "code_execution_output"`

          - `required string EncryptedStdout`

          - `required long ReturnCode`

          - `required string Stderr`

          - `JsonElement Type = "encrypted_code_execution_result"`

      - `required string ToolUseID`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonElement Type = "code_execution_tool_result"`

    - `class BetaBashCodeExecutionToolResultBlock:`

      - `required Content Content`

        - `class BetaBashCodeExecutionToolResultError:`

          - `required ErrorCode ErrorCode`

            - `InvalidToolInput("invalid_tool_input")`

            - `Unavailable("unavailable")`

            - `TooManyRequests("too_many_requests")`

            - `ExecutionTimeExceeded("execution_time_exceeded")`

            - `OutputFileTooLarge("output_file_too_large")`

          - `JsonElement Type = "bash_code_execution_tool_result_error"`

        - `class BetaBashCodeExecutionResultBlock:`

          - `required IReadOnlyList<BetaBashCodeExecutionOutputBlock> Content`

            - `required string FileID`

            - `JsonElement Type = "bash_code_execution_output"`

          - `required long ReturnCode`

          - `required string Stderr`

          - `required string Stdout`

          - `JsonElement Type = "bash_code_execution_result"`

      - `required string ToolUseID`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonElement Type = "bash_code_execution_tool_result"`

    - `class BetaTextEditorCodeExecutionToolResultBlock:`

      - `required Content Content`

        - `class BetaTextEditorCodeExecutionToolResultError:`

          - `required ErrorCode ErrorCode`

            - `InvalidToolInput("invalid_tool_input")`

            - `Unavailable("unavailable")`

            - `TooManyRequests("too_many_requests")`

            - `ExecutionTimeExceeded("execution_time_exceeded")`

            - `FileNotFound("file_not_found")`

          - `required string? ErrorMessage`

          - `JsonElement Type = "text_editor_code_execution_tool_result_error"`

        - `class BetaTextEditorCodeExecutionViewResultBlock:`

          - `required string Content`

          - `required FileType FileType`

            - `Text("text")`

            - `Image("image")`

            - `Pdf("pdf")`

          - `required long? NumLines`

          - `required long? StartLine`

          - `required long? TotalLines`

          - `JsonElement Type = "text_editor_code_execution_view_result"`

        - `class BetaTextEditorCodeExecutionCreateResultBlock:`

          - `required bool IsFileUpdate`

          - `JsonElement Type = "text_editor_code_execution_create_result"`

        - `class BetaTextEditorCodeExecutionStrReplaceResultBlock:`

          - `required IReadOnlyList<string>? Lines`

          - `required long? NewLines`

          - `required long? NewStart`

          - `required long? OldLines`

          - `required long? OldStart`

          - `JsonElement Type = "text_editor_code_execution_str_replace_result"`

      - `required string ToolUseID`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonElement Type = "text_editor_code_execution_tool_result"`

    - `class BetaToolSearchToolResultBlock:`

      - `required Content Content`

        - `class BetaToolSearchToolResultError:`

          - `required ErrorCode ErrorCode`

            - `InvalidToolInput("invalid_tool_input")`

            - `Unavailable("unavailable")`

            - `TooManyRequests("too_many_requests")`

            - `ExecutionTimeExceeded("execution_time_exceeded")`

          - `required string? ErrorMessage`

          - `JsonElement Type = "tool_search_tool_result_error"`

        - `class BetaToolSearchToolSearchResultBlock:`

          - `required IReadOnlyList<BetaToolReferenceBlock> ToolReferences`

            - `required string ToolName`

              maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

            - `JsonElement Type = "tool_reference"`

          - `JsonElement Type = "tool_search_tool_search_result"`

      - `required string ToolUseID`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `JsonElement Type = "tool_search_tool_result"`

    - `class BetaMcpToolUseBlock:`

      - `required string ID`

        pattern: ^[a-zA-Z0-9_-]+$

      - `required IReadOnlyDictionary<string, JsonElement> Input`

      - `required string Name`

        The name of the MCP tool

      - `required string ServerName`

        The name of the MCP server

      - `JsonElement Type = "mcp_tool_use"`

    - `class BetaMcpToolResultBlock:`

      - `required Content Content`

        - `string`

        - `IReadOnlyList<BetaTextBlock>`

          - `required IReadOnlyList<BetaTextCitation>? Citations`

            Citations supporting the text block.

            The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

          - `required string Text`

            maxLength: 5000000, minLength: 0

          - `JsonElement Type = "text"`

      - `required bool IsError`

      - `required string ToolUseID`

        pattern: ^[a-zA-Z0-9_-]+$

      - `JsonElement Type = "mcp_tool_result"`

    - `class BetaContainerUploadBlock:`

      Response model for a file uploaded to the container.

      - `required string FileID`

      - `JsonElement Type = "container_upload"`

    - `class BetaCompactionBlock:`

      A compaction block returned when autocompact is triggered.

      When content is None, it indicates the compaction failed to produce a valid
      summary (e.g., malformed output from the model). Clients may round-trip
      compaction blocks with null content; the server treats them as no-ops.

      - `required string? Content`

        Summary of compacted content, or null if compaction failed

      - `required string? EncryptedContent`

        Opaque metadata from prior compaction, to be round-tripped verbatim

      - `JsonElement Type = "compaction"`

    - `class BetaFallbackBlock:`

      Marks the point in `content` where one model's output gives way to the next.

      One block appears per hop where a preceding model actually ran this turn and
      declined. A turn where no preceding model ran and declined has no such
      boundary and carries no block — the signal for whether a fallback model
      served the response is the presence of a `fallback_message` entry in
      `usage.iterations`, not this block.

      The block is treated like a server-tool content block for streaming: it
      arrives via the standard `content_block_start` / `content_block_stop`
      pair and carries no deltas.

      - `required BetaFallbackInfo From`

        The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.

        - `required Model Model`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `ClaudeFable5_1("claude-fable-5-1")`

            Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

          - `ClaudeMythos5_1("claude-mythos-5-1")`

            Our most capable model for cybersecurity and biology research, available through trusted access programs

          - `ClaudeSonnet5("claude-sonnet-5")`

            High-performance model for coding and agents

          - `ClaudeFable5("claude-fable-5")`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `ClaudeMythos5("claude-mythos-5")`

            Most capable model for cybersecurity and biology research

          - `ClaudeOpus5("claude-opus-5")`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_8("claude-opus-4-8")`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_7("claude-opus-4-7")`

            Powerful intelligence for long-running agents and coding

          - `ClaudeMythosPreview("claude-mythos-preview")`

            New class of intelligence, strongest in coding and cybersecurity

          - `ClaudeOpus4_6("claude-opus-4-6")`

            Powerful intelligence for long-running agents and coding

          - `ClaudeSonnet4_6("claude-sonnet-4-6")`

            Best combination of speed and intelligence

          - `ClaudeHaiku4_5("claude-haiku-4-5")`

            Fastest model with near-frontier intelligence

          - `ClaudeHaiku4_5_20251001("claude-haiku-4-5-20251001")`

            Fastest model with near-frontier intelligence

          - `ClaudeOpus4_5("claude-opus-4-5")`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_5_20251101("claude-opus-4-5-20251101")`

            Powerful intelligence for long-running agents and coding

          - `ClaudeSonnet4_5("claude-sonnet-4-5")`

            High-performance model for agents and coding

          - `ClaudeSonnet4_5_20250929("claude-sonnet-4-5-20250929")`

            High-performance model for agents and coding

      - `required BetaFallbackInfo To`

        The fallback model producing the content that follows this block. Its `model` is always the canonical id.

      - `required BetaFallbackRefusalTrigger Trigger`

        What caused the `from` model to hand over at this hop.

        - `required BetaFallbackRefusalTriggerCategory? Category`

          The policy category that triggered a refusal.

          - `Cyber("cyber")`

            The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.

          - `Bio("bio")`

            The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.

          - `FrontierLlm("frontier_llm")`

            The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.

          - `ReasoningExtraction("reasoning_extraction")`

            The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).

          - `GeneralHarms("general_harms")`

            The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.

        - `JsonElement Type = "refusal"`

      - `JsonElement Type = "fallback"`

  - `required BetaContextManagementResponse? ContextManagement`

    Context management response.

    Information about context management strategies applied during the request.

    - `required IReadOnlyList<AppliedEdit> AppliedEdits`

      List of context management edits that were applied.

      - `class BetaClearToolUses20250919EditResponse:`

        - `required long ClearedInputTokens`

          Number of input tokens cleared by this edit.

          minimum: 0

        - `required long ClearedToolUses`

          Number of tool uses that were cleared.

          minimum: 0

        - `JsonElement Type = "clear_tool_uses_20250919"`

          The type of context management edit applied.

      - `class BetaClearThinking20251015EditResponse:`

        - `required long ClearedInputTokens`

          Number of input tokens cleared by this edit.

          minimum: 0

        - `required long ClearedThinkingTurns`

          Number of thinking turns that were cleared.

          minimum: 0

        - `JsonElement Type = "clear_thinking_20251015"`

          The type of context management edit applied.

  - `required BetaDiagnostics? Diagnostics`

    Response envelope for request-level diagnostics. Present (possibly
    null) whenever the caller supplied `diagnostics` on the request.

    - `required CacheMissReason? CacheMissReason`

      Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

      - `class BetaCacheMissModelChanged:`

        - `required long CacheMissedInputTokens`

          Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

        - `JsonElement Type = "model_changed"`

      - `class BetaCacheMissSystemChanged:`

        - `required long CacheMissedInputTokens`

          Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

        - `JsonElement Type = "system_changed"`

      - `class BetaCacheMissToolsChanged:`

        - `required long CacheMissedInputTokens`

          Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

        - `JsonElement Type = "tools_changed"`

      - `class BetaCacheMissMessagesChanged:`

        - `required long CacheMissedInputTokens`

          Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

        - `JsonElement Type = "messages_changed"`

      - `class BetaCacheMissPreviousMessageNotFound:`

        - `JsonElement Type = "previous_message_not_found"`

      - `class BetaCacheMissUnavailable:`

        - `JsonElement Type = "unavailable"`

  - `required Model Model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `JsonElement Role = "assistant"`

    Conversational role of the generated message.

    This will always be `"assistant"`.

  - `required BetaRefusalStopDetails? StopDetails`

    Structured information about a refusal.

    - `required Category? Category`

      The policy category that triggered a refusal.

      - `Cyber("cyber")`

        The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.

      - `Bio("bio")`

        The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.

      - `FrontierLlm("frontier_llm")`

        The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.

      - `ReasoningExtraction("reasoning_extraction")`

        The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).

      - `GeneralHarms("general_harms")`

        The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.

    - `required string? Explanation`

      Human-readable explanation of the refusal.

      This text is not guaranteed to be stable. `null` when no explanation is available for the category.

    - `required string? FallbackCreditToken`

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

    - `required bool? FallbackHasPrefillClaim`

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

    - `required string? RecommendedModel`

      The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

    - `JsonElement Type = "refusal"`

  - `required BetaStopReason? StopReason`

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

    - `EndTurn("end_turn")`

    - `MaxTokens("max_tokens")`

    - `StopSequence("stop_sequence")`

    - `ToolUse("tool_use")`

    - `PauseTurn("pause_turn")`

    - `Compaction("compaction")`

    - `Refusal("refusal")`

    - `ModelContextWindowExceeded("model_context_window_exceeded")`

  - `required string? StopSequence`

    Which custom stop sequence was generated, if any.

    This value will be a non-null string if one of your custom stop sequences was generated.

  - `JsonElement Type = "message"`

    Object type.

    For Messages, this is always `"message"`.

  - `required BetaUsage Usage`

    Billing and rate-limit usage.

    Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

    Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

    For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

    Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

    - `required BetaCacheCreation? CacheCreation`

      Breakdown of cached tokens by TTL

      - `required long Ephemeral1hInputTokens`

        The number of input tokens used to create the 1 hour cache entry.

        minimum: 0

      - `required long Ephemeral5mInputTokens`

        The number of input tokens used to create the 5 minute cache entry.

        minimum: 0

    - `required long? CacheCreationInputTokens`

      The number of input tokens used to create the cache entry.

      minimum: 0

    - `required long? CacheReadInputTokens`

      The number of input tokens read from the cache.

      minimum: 0

    - `required BetaFallbackCreditUsage? FallbackCredit`

      Outcome of the `fallback_credit_token` presented on this request.

      - `required Status Status`

        Whether the fallback-credit reprice was applied to this response's billing.

        A union discriminated on `type`. `redeemed`: the retry is billed as if
        the conversation had been on the retry model all along — including when the
        resulting shift is zero because there was nothing to move. `not_applied`:
        no reprice was applied; the arm's `reason` says why.

        - `class BetaFallbackCreditRedeemed:`

          The reprice was applied: the retry is billed as if the conversation
          had been on the retry model all along.

          - `JsonElement Type = "redeemed"`

        - `class BetaFallbackCreditNotApplied:`

          No reprice was applied; `reason` says why.

          - `required Reason Reason`

            Why the reprice was not applied.

            A closed enum; additions to the redemption-check vocabulary arrive as
            deliberate schema updates.

            - `BodyMismatch("body_mismatch")`

            - `ContinuationExcluded("continuation_excluded")`

            - `ContinuationOnly("continuation_only")`

            - `Expired("expired")`

            - `InvalidTargetModel("invalid_target_model")`

            - `NotEnabled("not_enabled")`

            - `RepriceUnavailable("reprice_unavailable")`

            - `TemporarilyUnavailable("temporarily_unavailable")`

            - `VariantFieldsPresent("variant_fields_present")`

            - `WrongOrganization("wrong_organization")`

            - `WrongPlatform("wrong_platform")`

            - `WrongWorkspace("wrong_workspace")`

          - `JsonElement Type = "not_applied"`

          - `IReadOnlyList<string>? RemoveToRedeem`

            Request fields to remove before retrying, so the retry can redeem this
            token.

            Present exactly when `reason` is `variant_fields_present` — never null,
            never an empty array; absent otherwise. Fields are named only from your own request, and only after
            the sealed variant hash matched. A served best-effort retry has already
            been billed at normal price; nothing redeems retroactively, but a corrected
            re-send inside the token's five-minute window can still redeem.

    - `required string? InferenceGeo`

      The geographic region where inference was performed for this request.

    - `required long InputTokens`

      The number of input tokens which were used.

      minimum: 0

    - `required IReadOnlyList<Iteration>? Iterations`

      Per-iteration token usage breakdown.

      Each entry represents one sampling iteration, with its own input/output token counts and cache statistics, discriminated by `type`. For `message` entries (model sampling iterations, such as the turns of a server-side tool use loop), this allows you to:

      - Determine which iterations exceeded long context thresholds (>=200k tokens)
      - Calculate the context window size from the last `message` entry
      - Understand token accumulation across server-side tool use loops

      A `compaction` entry reports the token usage of the compaction operation itself — the server-side request that summarizes the context being closed — NOT the size of the context that was compacted away, and its token counts can be much smaller than that closed context (for example, a compaction that closes a ~200k-token context can report only a few thousand tokens). Do not derive the context window size from a `compaction` entry, even when it is the last entry. A `compaction` entry's tokens are not included in the top-level `usage` fields. When an input-token trigger is in effect (the default — 150,000 tokens unless configured otherwise), each `compaction` entry closes a context that had reached at least that threshold, though the context can exceed it by the final iteration's output and tool results.

      - `class BetaMessageIterationUsage:`

        Token usage for a sampling iteration.

        - `required BetaCacheCreation? CacheCreation`

          Breakdown of cached tokens by TTL

        - `required long CacheCreationInputTokens`

          The number of input tokens used to create the cache entry.

          minimum: 0

        - `required long CacheReadInputTokens`

          The number of input tokens read from the cache.

          minimum: 0

        - `required long InputTokens`

          The number of input tokens which were used.

          minimum: 0

        - `required Model Model`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `required long OutputTokens`

          The number of output tokens which were used.

          minimum: 0

        - `JsonElement Type = "message"`

          Usage for a sampling iteration

      - `class BetaCompactionIterationUsage:`

        Token usage for a compaction iteration.

        - `required BetaCacheCreation? CacheCreation`

          Breakdown of cached tokens by TTL

        - `required long CacheCreationInputTokens`

          The number of input tokens used to create the cache entry.

          minimum: 0

        - `required long CacheReadInputTokens`

          The number of input tokens read from the cache.

          minimum: 0

        - `required long InputTokens`

          The number of input tokens which were used.

          minimum: 0

        - `required long OutputTokens`

          The number of output tokens which were used.

          minimum: 0

        - `JsonElement Type = "compaction"`

          Usage for a compaction iteration

      - `class BetaAdvisorMessageIterationUsage:`

        Token usage for an advisor sub-inference iteration.

        - `required BetaCacheCreation? CacheCreation`

          Breakdown of cached tokens by TTL

        - `required long CacheCreationInputTokens`

          The number of input tokens used to create the cache entry.

          minimum: 0

        - `required long CacheReadInputTokens`

          The number of input tokens read from the cache.

          minimum: 0

        - `required long InputTokens`

          The number of input tokens which were used.

          minimum: 0

        - `required Model Model`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `required long OutputTokens`

          The number of output tokens which were used.

          minimum: 0

        - `JsonElement Type = "advisor_message"`

          Usage for an advisor sub-inference iteration

      - `class BetaFallbackMessageIterationUsage:`

        Token usage for the fallback-model attempt of a server-side fallback request.

        Produced in place of a `message` entry for whichever hop served the
        response. A declined hop produces the existing `message` entry. Whether
        a fallback model served the response is signalled by the presence of this
        entry in `usage.iterations`.

        - `required BetaCacheCreation? CacheCreation`

          Breakdown of cached tokens by TTL

        - `required long CacheCreationInputTokens`

          The number of input tokens used to create the cache entry.

          minimum: 0

        - `required long CacheReadInputTokens`

          The number of input tokens read from the cache.

          minimum: 0

        - `required long InputTokens`

          The number of input tokens which were used.

          minimum: 0

        - `required Model Model`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `required long OutputTokens`

          The number of output tokens which were used.

          minimum: 0

        - `JsonElement Type = "fallback_message"`

          Usage for the fallback-model attempt that served the response

    - `required long OutputTokens`

      The number of output tokens which were used.

      minimum: 0

    - `required BetaOutputTokensDetails? OutputTokensDetails`

      Breakdown of output tokens by category.

      `output_tokens` remains the inclusive, authoritative total used for billing.
      This object provides a read-only decomposition for observability — for example,
      how many of the billed output tokens were spent on internal reasoning that may
      have been summarized before being returned to you.

      - `required long ThinkingTokens`

        Number of output tokens the model generated as internal reasoning, including
        the thinking-block delimiter tokens.

        Reflects the raw reasoning the model produced, not the (possibly shorter)
        summarized thinking text returned in the response body. Computed by
        re-tokenizing the raw reasoning text, so it may differ from the model's exact
        generation count by a small number of tokens. Always ≤ `output_tokens`;
        `output_tokens - thinking_tokens` approximates the non-reasoning output.

        minimum: 0

    - `required BetaServerToolUsage? ServerToolUse`

      The number of server tool requests.

      - `required long WebFetchRequests`

        The number of web fetch tool requests.

        minimum: 0

      - `required long WebSearchRequests`

        The number of web search tool requests.

        minimum: 0

    - `required ServiceTier? ServiceTier`

      If the request used the priority, standard, or batch tier.

      - `Standard("standard")`

      - `Priority("priority")`

      - `Batch("batch")`

    - `required Speed? Speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `Standard("standard")`

      - `Fast("fast")`

  - `IReadOnlyList<BetaThinkingDroppedInputTransformation>? InputTransformations`

    Changes the API made to the request's input before showing it to the model:
    one entry per change, in request order. Today the only entry type is
    `thinking_dropped` — a `thinking`, `redacted_thinking` or `connector_text`
    block from the request's `messages` that was removed from the prompt instead
    of being shown to the model because it failed a binding check. More entry
    types may be added over time; ignore types you do not recognize.

    Requires `anthropic-beta: thinking-binding-controls-2026-08-01`. Present on
    every such response from a model that supports extended thinking, as `[]`
    when nothing was changed; without the beta, blocks are removed all the same
    but nothing is reported. Removed blocks contribute nothing to
    `usage.input_tokens`. When streaming, the array is final in `message_start`;
    the final `message_delta` event carries it only when a server-side model
    fallback happened mid-stream, in which case it holds the serving model's
    entries and replaces the one in `message_start`.

    - `required string Path`

      Where the removed block was in your request, as `messages.{i}.content.{j}`:
      `i` indexes the `messages` array you sent and `j` that message's `content`
      array — the same form error messages use.

    - `required Reason Reason`

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

      - `ModelBindingMismatch("model_binding_mismatch")`

      - `PrefixBindingMismatch("prefix_binding_mismatch")`

      - `OrganizationBindingMismatch("organization_binding_mismatch")`

      - `EndUserBindingMismatch("end_user_binding_mismatch")`

    - `JsonElement Type = "thinking_dropped"`

      Always `thinking_dropped` for this entry type.

- `class BetaRawMessageStreamEvent: union`

  - `class BetaRawMessageStartEvent:`

    - `required BetaMessage Message`

    - `JsonElement Type = "message_start"`

  - `class BetaRawMessageDeltaEvent:`

    - `required BetaContextManagementResponse? ContextManagement`

      Information about context management strategies applied during the request

    - `required Delta Delta`

      - `required BetaContainer? Container`

        Information about the container used in the request (for the code execution tool)

      - `required BetaRefusalStopDetails? StopDetails`

        Structured information about a refusal.

      - `required BetaStopReason? StopReason`

      - `required string? StopSequence`

    - `JsonElement Type = "message_delta"`

    - `required BetaMessageDeltaUsage Usage`

      Billing and rate-limit usage.

      Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

      Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

      For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

      Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

      - `required long? CacheCreationInputTokens`

        The cumulative number of input tokens used to create the cache entry.

        minimum: 0

      - `required long? CacheReadInputTokens`

        The cumulative number of input tokens read from the cache.

        minimum: 0

      - `required BetaFallbackCreditUsage? FallbackCredit`

        Outcome of the `fallback_credit_token` presented on this request.

      - `required long? InputTokens`

        The cumulative number of input tokens which were used.

        minimum: 0

      - `required IReadOnlyList<Iteration>? Iterations`

        Per-iteration token usage breakdown.

        Each entry represents one sampling iteration, with its own input/output token counts and cache statistics, discriminated by `type`. For `message` entries (model sampling iterations, such as the turns of a server-side tool use loop), this allows you to:

        - Determine which iterations exceeded long context thresholds (>=200k tokens)
        - Calculate the context window size from the last `message` entry
        - Understand token accumulation across server-side tool use loops

        A `compaction` entry reports the token usage of the compaction operation itself — the server-side request that summarizes the context being closed — NOT the size of the context that was compacted away, and its token counts can be much smaller than that closed context (for example, a compaction that closes a ~200k-token context can report only a few thousand tokens). Do not derive the context window size from a `compaction` entry, even when it is the last entry. A `compaction` entry's tokens are not included in the top-level `usage` fields. When an input-token trigger is in effect (the default — 150,000 tokens unless configured otherwise), each `compaction` entry closes a context that had reached at least that threshold, though the context can exceed it by the final iteration's output and tool results.

        - `class BetaMessageIterationUsage:`

          Token usage for a sampling iteration.

        - `class BetaCompactionIterationUsage:`

          Token usage for a compaction iteration.

        - `class BetaAdvisorMessageIterationUsage:`

          Token usage for an advisor sub-inference iteration.

        - `class BetaFallbackMessageIterationUsage:`

          Token usage for the fallback-model attempt of a server-side fallback request.

          Produced in place of a `message` entry for whichever hop served the
          response. A declined hop produces the existing `message` entry. Whether
          a fallback model served the response is signalled by the presence of this
          entry in `usage.iterations`.

      - `required long OutputTokens`

        The cumulative number of output tokens which were used.

      - `required BetaOutputTokensDetails? OutputTokensDetails`

        Breakdown of output tokens by category.

        `output_tokens` remains the inclusive, authoritative total used for billing.
        This object provides a read-only decomposition for observability — for example,
        how many of the billed output tokens were spent on internal reasoning that may
        have been summarized before being returned to you.

      - `required BetaServerToolUsage? ServerToolUse`

        The number of server tool requests.

    - `IReadOnlyList<BetaThinkingDroppedInputTransformation>? InputTransformations`

      Changes the API made to the request's input before showing it to the model:
      one entry per change, in request order. Today the only entry type is
      `thinking_dropped` — a `thinking`, `redacted_thinking` or `connector_text`
      block from the request's `messages` that was removed from the prompt instead
      of being shown to the model because it failed a binding check. More entry
      types may be added over time; ignore types you do not recognize.

      Requires `anthropic-beta: thinking-binding-controls-2026-08-01`. Present on
      every such response from a model that supports extended thinking, as `[]`
      when nothing was changed; without the beta, blocks are removed all the same
      but nothing is reported. Removed blocks contribute nothing to
      `usage.input_tokens`. When streaming, the array is final in `message_start`;
      the final `message_delta` event carries it only when a server-side model
      fallback happened mid-stream, in which case it holds the serving model's
      entries and replaces the one in `message_start`.

      - `required string Path`

        Where the removed block was in your request, as `messages.{i}.content.{j}`:
        `i` indexes the `messages` array you sent and `j` that message's `content`
        array — the same form error messages use.

      - `required Reason Reason`

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

      - `JsonElement Type = "thinking_dropped"`

        Always `thinking_dropped` for this entry type.

  - `class BetaRawMessageStopEvent:`

    - `JsonElement Type = "message_stop"`

  - `class BetaRawContentBlockStartEvent:`

    - `required ContentBlock ContentBlock`

      Response model for a file uploaded to the container.

      - `class BetaTextBlock:`

      - `class BetaThinkingBlock:`

      - `class BetaRedactedThinkingBlock:`

      - `class BetaToolUseBlock:`

      - `class BetaServerToolUseBlock:`

      - `class BetaWebSearchToolResultBlock:`

      - `class BetaWebFetchToolResultBlock:`

      - `class BetaAdvisorToolResultBlock:`

      - `class BetaCodeExecutionToolResultBlock:`

      - `class BetaBashCodeExecutionToolResultBlock:`

      - `class BetaTextEditorCodeExecutionToolResultBlock:`

      - `class BetaToolSearchToolResultBlock:`

      - `class BetaMcpToolUseBlock:`

      - `class BetaMcpToolResultBlock:`

      - `class BetaContainerUploadBlock:`

        Response model for a file uploaded to the container.

      - `class BetaCompactionBlock:`

        A compaction block returned when autocompact is triggered.

        When content is None, it indicates the compaction failed to produce a valid
        summary (e.g., malformed output from the model). Clients may round-trip
        compaction blocks with null content; the server treats them as no-ops.

      - `class BetaFallbackBlock:`

        Marks the point in `content` where one model's output gives way to the next.

        One block appears per hop where a preceding model actually ran this turn and
        declined. A turn where no preceding model ran and declined has no such
        boundary and carries no block — the signal for whether a fallback model
        served the response is the presence of a `fallback_message` entry in
        `usage.iterations`, not this block.

        The block is treated like a server-tool content block for streaming: it
        arrives via the standard `content_block_start` / `content_block_stop`
        pair and carries no deltas.

    - `required long Index`

    - `JsonElement Type = "content_block_start"`

  - `class BetaRawContentBlockDeltaEvent:`

    - `required BetaRawContentBlockDelta Delta`

      - `class BetaTextDelta:`

        - `required string Text`

        - `JsonElement Type = "text_delta"`

      - `class BetaInputJsonDelta:`

        - `required string PartialJson`

        - `JsonElement Type = "input_json_delta"`

      - `class BetaCitationsDelta:`

        - `required Citation Citation`

          - `class BetaCitationCharLocation:`

          - `class BetaCitationPageLocation:`

          - `class BetaCitationContentBlockLocation:`

          - `class BetaCitationsWebSearchResultLocation:`

          - `class BetaCitationSearchResultLocation:`

        - `JsonElement Type = "citations_delta"`

      - `class BetaThinkingDelta:`

        - `required long? EstimatedTokens`

          Per-frame increment of a coarse, running estimate of the tokens this thinking block has produced so far. Present whenever the `thinking-token-count-2026-05-13` beta is set; `null` unless `thinking.display` resolves to `"omitted"` and a count is due this frame. Sum the increments across `thinking_delta` frames on this block for a progress indicator. Each increment is a non-negative multiple of a fixed quantum and the cadence is rate-limited, so this is a deliberately lossy display hint, not a billable count; `usage.output_tokens` remains authoritative.

        - `required string Thinking`

          The incremental `thinking` text for this content block. Concatenate the `thinking` values of successive `thinking_delta` events to assemble the block's full `thinking` value.

        - `JsonElement Type = "thinking_delta"`

      - `class BetaSignatureDelta:`

        - `required string Signature`

          The `signature` for this thinking block: an opaque value used to verify that the block was generated by Claude when it is passed back to the API. Delivered in a `signature_delta` event just before the block's `content_block_stop` event.

        - `JsonElement Type = "signature_delta"`

      - `class BetaCompactionContentBlockDelta:`

        - `required string? Content`

        - `required string? EncryptedContent`

          Opaque metadata from prior compaction, to be round-tripped verbatim

        - `JsonElement Type = "compaction_delta"`

    - `required long Index`

    - `JsonElement Type = "content_block_delta"`

  - `class BetaRawContentBlockStopEvent:`

    - `required long Index`

    - `JsonElement Type = "content_block_stop"`

## Example

```csharp
MessageCreateParams parameters = new()
{
    MaxTokens = 1024,
    Messages =
    [
        new()
        {
            Content = "Hello, world",
            Role = Role.User,
            ClearAt = ClearAt.NextUserMessage,
            OutputConfig = new() { Effort = Effort.Low },
        },
    ],
    Model = Model.ClaudeOpus5,
};

var betaMessage = await client.Beta.Messages.Create(parameters);

Console.WriteLine(betaMessage);
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
