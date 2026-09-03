# Create a Message Batch

`MessageBatch Messages.Batches.Create(parameters, cancellationToken = default)`

**POST** `/v1/messages/batches`

Send a batch of Message creation requests.

The Message Batches API can be used to process multiple Messages API requests at once. Once a Message Batch is created, it begins processing immediately. Batches can take up to 24 hours to complete.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

## Parameters

- `BatchCreateParams parameters`

  - `required IReadOnlyList<Request> requests`

    Body param: List of requests for prompt completion. Each is an individual request to create a Message.

    maxItems: 100000, minItems: 1

    - `required string CustomID`

      Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

      Must be unique for each request within the Message Batch.

      maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,64}$

    - `required Params Params`

      Messages API creation parameters for the individual request.

      See the [Messages API reference](https://platform.claude.com/docs/en/api/messages) for full documentation on available parameters.

      - `required long MaxTokens`

        The maximum number of tokens to generate before stopping.

        Note that our models may stop _before_ reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

        Set to `0` to populate the [prompt cache](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#pre-warming-the-cache) without generating a response.

        Different models have different maximum values for this parameter.  See [models](https://platform.claude.com/docs/en/about-claude/models/overview) for details.

        minimum: 0

      - `required IReadOnlyList<MessageParam> Messages`

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

        - `required Content Content`

          - `string`

          - `IReadOnlyList<ContentBlockParam>`

            - `class TextBlockParam:`

              - `required string Text`

                minLength: 1

              - `JsonElement Type = "text"`

              - `CacheControlEphemeral? CacheControl`

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

              - `IReadOnlyList<TextCitationParam>? Citations`

                - `class CitationCharLocationParam:`

                  - `required string CitedText`

                  - `required long DocumentIndex`

                    minimum: 0

                  - `required string? DocumentTitle`

                    maxLength: 500, minLength: 1

                  - `required long EndCharIndex`

                  - `required long StartCharIndex`

                    minimum: 0

                  - `JsonElement Type = "char_location"`

                - `class CitationPageLocationParam:`

                  - `required string CitedText`

                  - `required long DocumentIndex`

                    minimum: 0

                  - `required string? DocumentTitle`

                    maxLength: 500, minLength: 1

                  - `required long EndPageNumber`

                  - `required long StartPageNumber`

                    minimum: 1

                  - `JsonElement Type = "page_location"`

                - `class CitationContentBlockLocationParam:`

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

                - `class CitationWebSearchResultLocationParam:`

                  - `required string CitedText`

                  - `required string EncryptedIndex`

                  - `required string? Title`

                    maxLength: 512, minLength: 1

                  - `JsonElement Type = "web_search_result_location"`

                  - `required string Url`

                    minLength: 1

                - `class CitationSearchResultLocationParam:`

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

            - `class ImageBlockParam:`

              - `required Source Source`

                - `class Base64ImageSource:`

                  - `required string Data`

                    format: byte

                  - `required MediaType MediaType`

                    - `ImageJpeg("image/jpeg")`

                    - `ImagePng("image/png")`

                    - `ImageGif("image/gif")`

                    - `ImageWebP("image/webp")`

                  - `JsonElement Type = "base64"`

                - `class UrlImageSource:`

                  - `JsonElement Type = "url"`

                  - `required string Url`

                - `class FileImageSource:`

                  - `required string FileID`

                  - `JsonElement Type = "file"`

              - `JsonElement Type = "image"`

              - `CacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

              - `ImageTransformationsParam? Transformations`

                Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

                - `OversizedImage OversizedImage`

                  What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

                  - `Downsize("downsize")`

                  - `Error("error")`

            - `class DocumentBlockParam:`

              - `required Source Source`

                - `class Base64PdfSource:`

                  - `required string Data`

                    format: byte

                  - `JsonElement MediaType = "application/pdf"`

                  - `JsonElement Type = "base64"`

                - `class PlainTextSource:`

                  - `required string Data`

                  - `JsonElement MediaType = "text/plain"`

                  - `JsonElement Type = "text"`

                - `class ContentBlockSource:`

                  - `required Content Content`

                    - `string`

                    - `IReadOnlyList<ContentBlockSourceContent>`

                      - `class TextBlockParam:`

                      - `class ImageBlockParam:`

                  - `JsonElement Type = "content"`

                - `class UrlPdfSource:`

                  - `JsonElement Type = "url"`

                  - `required string Url`

                - `class FileDocumentSource:`

                  - `required string FileID`

                  - `JsonElement Type = "file"`

              - `JsonElement Type = "document"`

              - `CacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

              - `CitationsConfigParam? Citations`

                - `bool Enabled`

              - `string? Context`

                minLength: 1

              - `string? Title`

                maxLength: 500, minLength: 1

            - `class SearchResultBlockParam:`

              - `required IReadOnlyList<TextBlockParam> Content`

                - `required string Text`

                  minLength: 1

                - `JsonElement Type = "text"`

                - `CacheControlEphemeral? CacheControl`

                  Create a cache control breakpoint at this content block.

                - `IReadOnlyList<TextCitationParam>? Citations`

              - `required string Source`

              - `required string Title`

              - `JsonElement Type = "search_result"`

              - `CacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

              - `CitationsConfigParam Citations`

            - `class ThinkingBlockParam:`

              - `required string Signature`

                The `signature` value of this thinking block, exactly as returned by the API in a previous response. Used to verify that the block was generated by Claude.

                Thinking blocks must be passed back unmodified and in their original order; a modified block results in a 400 `invalid_request_error`.

              - `required string Thinking`

                The `thinking` text of this block as returned by the API.

              - `JsonElement Type = "thinking"`

            - `class RedactedThinkingBlockParam:`

              - `required string Data`

                The `data` value of this redacted thinking block, exactly as returned by the API in a previous response. Opaque and encrypted; pass it back unchanged.

              - `JsonElement Type = "redacted_thinking"`

            - `class ToolUseBlockParam:`

              - `required string ID`

                pattern: ^[a-zA-Z0-9_-]+$

              - `required IReadOnlyDictionary<string, JsonElement> Input`

              - `required string Name`

                maxLength: 200, minLength: 1

              - `JsonElement Type = "tool_use"`

              - `CacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

              - `Caller Caller`

                Tool invocation directly from the model.

                - `class DirectCaller:`

                  Tool invocation directly from the model.

                  - `JsonElement Type = "direct"`

                - `class ServerToolCaller:`

                  Tool invocation generated by a server-side tool.

                  - `required string ToolID`

                    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

                  - `JsonElement Type = "code_execution_20250825"`

                - `class ServerToolCaller20260120:`

                  - `required string ToolID`

                    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

                  - `JsonElement Type = "code_execution_20260120"`

              - `string? ToolsetName`

                For a toolset member tool_use, the toolset family this member belongs to.

                maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

            - `class ToolResultBlockParam:`

              - `required string ToolUseID`

                pattern: ^[a-zA-Z0-9_-]+$

              - `JsonElement Type = "tool_result"`

              - `CacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

              - `Content Content`

                - `string`

                - `IReadOnlyList<Block>`

                  - `class TextBlockParam:`

                  - `class ImageBlockParam:`

                  - `class SearchResultBlockParam:`

                  - `class DocumentBlockParam:`

                  - `class ToolReferenceBlockParam:`

                    Tool reference block that can be included in tool_result content.

                    - `required string ToolName`

                      maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

                    - `JsonElement Type = "tool_reference"`

                    - `CacheControlEphemeral? CacheControl`

                      Create a cache control breakpoint at this content block.

                  - `class BrowserStateBlockParam:`

                    The caller's browser state after a browser toolset member call —
                    the full inventory of open tabs, which tab is active, and any side
                    effects (tabs opened, download state changes) the call produced.

                    At most one per `tool_result`, only on a non-error result answering a
                    browser toolset member `tool_use`. The server renders the
                    model-visible text from it; the model never sees the raw fields.

                    - `required IReadOnlyList<BrowserStateTabEntry> Tabs`

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

                    - `CacheControlEphemeral? CacheControl`

                      Create a cache control breakpoint at this content block.

                    - `IReadOnlyList<BrowserStateChange>? StateChanges`

                      Tabs opened and download state changes during this call. "Nothing to report" is expressed by omitting the field, never by an empty list.

                      maxItems: 200, minItems: 1

                      - `class BrowserStateChangeTabOpened:`

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

                      - `class BrowserStateChangeDownloadStarted:`

                        A file download that started during this call.

                        - `required string DownloadID`

                          The caller-assigned identifier for this download, stable across the state changes reporting it.

                          maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                        - `JsonElement Type = "download_started"`

                        - `required string Url`

                          The final post-redirect URL the download was served from.

                          maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                      - `class BrowserStateChangeDownloadCompleted:`

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

                      - `class BrowserStateChangeDownloadFailed:`

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

            - `class ServerToolUseBlockParam:`

              - `required string ID`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `required IReadOnlyDictionary<string, JsonElement> Input`

              - `required Name Name`

                - `WebSearch("web_search")`

                - `WebFetch("web_fetch")`

                - `CodeExecution("code_execution")`

                - `BashCodeExecution("bash_code_execution")`

                - `TextEditorCodeExecution("text_editor_code_execution")`

                - `ToolSearchToolRegex("tool_search_tool_regex")`

                - `ToolSearchToolBm25("tool_search_tool_bm25")`

              - `JsonElement Type = "server_tool_use"`

              - `CacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

              - `Caller Caller`

                Tool invocation directly from the model.

                - `class DirectCaller:`

                  Tool invocation directly from the model.

                - `class ServerToolCaller:`

                  Tool invocation generated by a server-side tool.

                - `class ServerToolCaller20260120:`

            - `class WebSearchToolResultBlockParam:`

              - `required WebSearchToolResultBlockParamContent Content`

                - `IReadOnlyList<WebSearchResultBlockParam>`

                  - `required string EncryptedContent`

                  - `required string Title`

                  - `JsonElement Type = "web_search_result"`

                  - `required string Url`

                  - `string? PageAge`

                - `class WebSearchToolRequestError:`

                  - `required WebSearchToolResultErrorCode ErrorCode`

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

              - `CacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

              - `Caller Caller`

                Tool invocation directly from the model.

                - `class DirectCaller:`

                  Tool invocation directly from the model.

                - `class ServerToolCaller:`

                  Tool invocation generated by a server-side tool.

                - `class ServerToolCaller20260120:`

            - `class WebFetchToolResultBlockParam:`

              - `required Content Content`

                - `class WebFetchToolResultErrorBlockParam:`

                  - `required WebFetchToolResultErrorCode ErrorCode`

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

                - `class WebFetchBlockParam:`

                  - `required DocumentBlockParam Content`

                  - `JsonElement Type = "web_fetch_result"`

                  - `required string Url`

                    Fetched content URL

                  - `string? RetrievedAt`

                    ISO 8601 timestamp when the content was retrieved

              - `required string ToolUseID`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `JsonElement Type = "web_fetch_tool_result"`

              - `CacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

              - `Caller Caller`

                Tool invocation directly from the model.

                - `class DirectCaller:`

                  Tool invocation directly from the model.

                - `class ServerToolCaller:`

                  Tool invocation generated by a server-side tool.

                - `class ServerToolCaller20260120:`

            - `class CodeExecutionToolResultBlockParam:`

              - `required CodeExecutionToolResultBlockParamContent Content`

                Code execution result with encrypted stdout for PFC + web_search results.

                - `class CodeExecutionToolResultErrorParam:`

                  - `required CodeExecutionToolResultErrorCode ErrorCode`

                    - `InvalidToolInput("invalid_tool_input")`

                    - `Unavailable("unavailable")`

                    - `TooManyRequests("too_many_requests")`

                    - `ExecutionTimeExceeded("execution_time_exceeded")`

                  - `JsonElement Type = "code_execution_tool_result_error"`

                - `class CodeExecutionResultBlockParam:`

                  - `required IReadOnlyList<CodeExecutionOutputBlockParam> Content`

                    - `required string FileID`

                    - `JsonElement Type = "code_execution_output"`

                  - `required long ReturnCode`

                  - `required string Stderr`

                  - `required string Stdout`

                  - `JsonElement Type = "code_execution_result"`

                - `class EncryptedCodeExecutionResultBlockParam:`

                  Code execution result with encrypted stdout for PFC + web_search results.

                  - `required IReadOnlyList<CodeExecutionOutputBlockParam> Content`

                    - `required string FileID`

                    - `JsonElement Type = "code_execution_output"`

                  - `required string EncryptedStdout`

                  - `required long ReturnCode`

                  - `required string Stderr`

                  - `JsonElement Type = "encrypted_code_execution_result"`

              - `required string ToolUseID`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `JsonElement Type = "code_execution_tool_result"`

              - `CacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

            - `class BashCodeExecutionToolResultBlockParam:`

              - `required Content Content`

                - `class BashCodeExecutionToolResultErrorParam:`

                  - `required BashCodeExecutionToolResultErrorCode ErrorCode`

                    - `InvalidToolInput("invalid_tool_input")`

                    - `Unavailable("unavailable")`

                    - `TooManyRequests("too_many_requests")`

                    - `ExecutionTimeExceeded("execution_time_exceeded")`

                    - `OutputFileTooLarge("output_file_too_large")`

                  - `JsonElement Type = "bash_code_execution_tool_result_error"`

                - `class BashCodeExecutionResultBlockParam:`

                  - `required IReadOnlyList<BashCodeExecutionOutputBlockParam> Content`

                    - `required string FileID`

                    - `JsonElement Type = "bash_code_execution_output"`

                  - `required long ReturnCode`

                  - `required string Stderr`

                  - `required string Stdout`

                  - `JsonElement Type = "bash_code_execution_result"`

              - `required string ToolUseID`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `JsonElement Type = "bash_code_execution_tool_result"`

              - `CacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

            - `class TextEditorCodeExecutionToolResultBlockParam:`

              - `required Content Content`

                - `class TextEditorCodeExecutionToolResultErrorParam:`

                  - `required TextEditorCodeExecutionToolResultErrorCode ErrorCode`

                    - `InvalidToolInput("invalid_tool_input")`

                    - `Unavailable("unavailable")`

                    - `TooManyRequests("too_many_requests")`

                    - `ExecutionTimeExceeded("execution_time_exceeded")`

                    - `FileNotFound("file_not_found")`

                  - `JsonElement Type = "text_editor_code_execution_tool_result_error"`

                  - `string? ErrorMessage`

                - `class TextEditorCodeExecutionViewResultBlockParam:`

                  - `required string Content`

                  - `required FileType FileType`

                    - `Text("text")`

                    - `Image("image")`

                    - `Pdf("pdf")`

                  - `JsonElement Type = "text_editor_code_execution_view_result"`

                  - `long? NumLines`

                  - `long? StartLine`

                  - `long? TotalLines`

                - `class TextEditorCodeExecutionCreateResultBlockParam:`

                  - `required bool IsFileUpdate`

                  - `JsonElement Type = "text_editor_code_execution_create_result"`

                - `class TextEditorCodeExecutionStrReplaceResultBlockParam:`

                  - `JsonElement Type = "text_editor_code_execution_str_replace_result"`

                  - `IReadOnlyList<string>? Lines`

                  - `long? NewLines`

                  - `long? NewStart`

                  - `long? OldLines`

                  - `long? OldStart`

              - `required string ToolUseID`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `JsonElement Type = "text_editor_code_execution_tool_result"`

              - `CacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

            - `class ToolSearchToolResultBlockParam:`

              - `required Content Content`

                - `class ToolSearchToolResultErrorParam:`

                  - `required ToolSearchToolResultErrorCode ErrorCode`

                    - `InvalidToolInput("invalid_tool_input")`

                    - `Unavailable("unavailable")`

                    - `TooManyRequests("too_many_requests")`

                    - `ExecutionTimeExceeded("execution_time_exceeded")`

                  - `JsonElement Type = "tool_search_tool_result_error"`

                  - `string? ErrorMessage`

                - `class ToolSearchToolSearchResultBlockParam:`

                  - `required IReadOnlyList<ToolReferenceBlockParam> ToolReferences`

                    - `required string ToolName`

                      maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

                    - `JsonElement Type = "tool_reference"`

                    - `CacheControlEphemeral? CacheControl`

                      Create a cache control breakpoint at this content block.

                  - `JsonElement Type = "tool_search_tool_search_result"`

              - `required string ToolUseID`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `JsonElement Type = "tool_search_tool_result"`

              - `CacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

            - `class ContainerUploadBlockParam:`

              A content block that represents a file to be uploaded to the container
              Files uploaded via this block will be available in the container's input directory.

              - `required string FileID`

              - `JsonElement Type = "container_upload"`

              - `CacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

        - `required Role Role`

          - `User("user")`

          - `Assistant("assistant")`

          - `System("system")`

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

      - `CacheControlEphemeral? CacheControl`

        Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

      - `MessageCreateParamsContainer? Container`

        Container identifier for reuse across requests.

        - `class ContainerParams:`

          Container parameters with skills to be loaded.

          - `string? ID`

            Container id

          - `IReadOnlyList<SkillParams>? Skills`

            List of skills to load in the container

            maxItems: 20

            - `required string SkillID`

              Skill ID

              maxLength: 64, minLength: 1

            - `required SkillParamsType Type`

              Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

              - `Anthropic("anthropic")`

              - `Custom("custom")`

            - `string Version`

              Skill version or 'latest' for most recent version

              maxLength: 64, minLength: 1

        - `string`

      - `string? InferenceGeo`

        Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

      - `Metadata Metadata`

        An object describing metadata about the request.

        - `string? UserID`

          An external identifier for the user who is associated with the request.

          This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

          maxLength: 512

      - `OutputConfig OutputConfig`

        Configuration options for the model's output, such as the output format.

        - `Effort? Effort`

          All possible effort levels.

          - `Low("low")`

          - `Medium("medium")`

          - `High("high")`

          - `Xhigh("xhigh")`

          - `Max("max")`

        - `JsonOutputFormat? Format`

          A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

          - `required IReadOnlyDictionary<string, JsonElement> Schema`

            The JSON schema of the format

          - `JsonElement Type = "json_schema"`

      - `ServiceTier ServiceTier`

        Determines whether to use priority capacity (if available) or standard capacity for this request.

        Anthropic offers different levels of service for your API requests. See [service-tiers](https://platform.claude.com/docs/en/api/service-tiers) for details.

        - `Auto("auto")`

        - `StandardOnly("standard_only")`

      - `IReadOnlyList<string> StopSequences`

        Custom text sequences that will cause the model to stop generating.

        Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

        If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

      - `bool Stream`

        Whether to incrementally stream the response using server-sent events.

        See [streaming](https://platform.claude.com/docs/en/build-with-claude/streaming) for details.

      - `System System`

        System prompt.

        A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role).

        - `string`

        - `IReadOnlyList<TextBlockParam>`

          - `required string Text`

            minLength: 1

          - `JsonElement Type = "text"`

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `IReadOnlyList<TextCitationParam>? Citations`

      - `ThinkingConfigParam Thinking`

        Configuration for enabling Claude's extended thinking.

        When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

        See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

        - `class ThinkingConfigEnabled:`

          - `required long BudgetTokens`

            Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

            Must be ≥1024 and less than `max_tokens`.

            See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

            minimum: 1024

          - `JsonElement Type = "enabled"`

          - `Display? Display`

            Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

            - `Summarized("summarized")`

            - `Omitted("omitted")`

        - `class ThinkingConfigDisabled:`

          - `JsonElement Type = "disabled"`

        - `class ThinkingConfigAdaptive:`

          - `JsonElement Type = "adaptive"`

          - `Display? Display`

            Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

            - `Summarized("summarized")`

            - `Omitted("omitted")`

      - `ToolChoice ToolChoice`

        How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

        - `class ToolChoiceAuto:`

          The model will automatically decide whether to use tools.

          - `JsonElement Type = "auto"`

          - `bool DisableParallelToolUse`

            Whether to disable parallel tool use.

            Defaults to `false`. If set to `true`, the model will output at most one tool use.

        - `class ToolChoiceAny:`

          The model will use any available tools.

          - `JsonElement Type = "any"`

          - `bool DisableParallelToolUse`

            Whether to disable parallel tool use.

            Defaults to `false`. If set to `true`, the model will output exactly one tool use.

        - `class ToolChoiceTool:`

          The model will use the specified tool with `tool_choice.name`.

          - `required string Name`

            The name of the tool to use.

          - `JsonElement Type = "tool"`

          - `bool DisableParallelToolUse`

            Whether to disable parallel tool use.

            Defaults to `false`. If set to `true`, the model will output exactly one tool use.

        - `class ToolChoiceNone:`

          The model will not be allowed to use tools.

          - `JsonElement Type = "none"`

      - `IReadOnlyList<ToolUnion> Tools`

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

        - `class Tool:`

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

          - `CacheControlEphemeral? CacheControl`

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

        - `class ToolBash20250124:`

          - `JsonElement Name = "bash"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type = "bash_20250124"`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct("direct")`

            - `CodeExecution20250825("code_execution_20250825")`

            - `CodeExecution20260120("code_execution_20260120")`

            - `CodeExecution20260521("code_execution_20260521")`

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class CodeExecutionTool20250522:`

          - `JsonElement Name = "code_execution"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type = "code_execution_20250522"`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct("direct")`

            - `CodeExecution20250825("code_execution_20250825")`

            - `CodeExecution20260120("code_execution_20260120")`

            - `CodeExecution20260521("code_execution_20260521")`

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class CodeExecutionTool20250825:`

          - `JsonElement Name = "code_execution"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type = "code_execution_20250825"`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct("direct")`

            - `CodeExecution20250825("code_execution_20250825")`

            - `CodeExecution20260120("code_execution_20260120")`

            - `CodeExecution20260521("code_execution_20260521")`

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class CodeExecutionTool20260120:`

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

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class CodeExecutionTool20260521:`

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

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BrowserToolset20260801:`

          The browser toolset: a single `tools[]` entry (carrying no
          `name`) that declares the browser tool family. The model is served
          the family's tool with any members disabled via `configs` removed
          from its schema.

          - `JsonElement Type = "browser_toolset_20260801"`

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `BrowserToolsetConfigs? Configs`

            Per-member configuration for `browser_toolset_20260801`: one
            optional field per member tool, keyed by the member name — the same
            name the member's `tool_use` blocks carry. Every member is an
            accepted key, and a member's defaults apply wherever its key is
            absent. Unknown keys are rejected: the field set is this toolset
            version's complete member set.

            - `BrowserCloseTabConfig? CloseTab`

              `close_tab`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BrowserDoubleClickConfig? DoubleClick`

              `double_click`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BrowserFileUploadConfig? FileUpload`

              `file_upload`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BrowserFindConfig? Find`

              `find`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BrowserFormInputConfig? FormInput`

              `form_input`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BrowserGetPageTextConfig? GetPageText`

              `get_page_text`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BrowserHoldKeyConfig? HoldKey`

              `hold_key`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BrowserHoverConfig? Hover`

              `hover`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BrowserJavascriptExecConfig? JavascriptExec`

              `javascript_exec`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BrowserKeyConfig? Key`

              `key`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BrowserLeftClickConfig? LeftClick`

              `left_click`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BrowserLeftClickDragConfig? LeftClickDrag`

              `left_click_drag`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BrowserLeftMouseDownConfig? LeftMouseDown`

              `left_mouse_down`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BrowserLeftMouseUpConfig? LeftMouseUp`

              `left_mouse_up`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BrowserListTabsConfig? ListTabs`

              `list_tabs`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BrowserMiddleClickConfig? MiddleClick`

              `middle_click`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BrowserMouseMoveConfig? MouseMove`

              `mouse_move`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BrowserNavigateConfig? Navigate`

              `navigate`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BrowserNewTabConfig? NewTab`

              `new_tab`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BrowserReadConsoleConfig? ReadConsole`

              `read_console`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BrowserReadNetworkConfig? ReadNetwork`

              `read_network`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BrowserReadPageConfig? ReadPage`

              `read_page`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BrowserRightClickConfig? RightClick`

              `right_click`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BrowserScreenshotConfig? Screenshot`

              `screenshot`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BrowserScrollConfig? Scroll`

              `scroll`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BrowserScrollToConfig? ScrollTo`

              `scroll_to`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BrowserSwitchTabConfig? SwitchTab`

              `switch_tab`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BrowserTripleClickConfig? TripleClick`

              `triple_click`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BrowserTypeConfig? Type`

              `type`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BrowserWaitConfig? Wait`

              `wait`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `BrowserZoomConfig? Zoom`

              `zoom`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `class MemoryTool20250818:`

          - `JsonElement Name = "memory"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type = "memory_20250818"`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct("direct")`

            - `CodeExecution20250825("code_execution_20250825")`

            - `CodeExecution20260120("code_execution_20260120")`

            - `CodeExecution20260521("code_execution_20260521")`

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class ComputerToolset20260801:`

          The computer toolset: a single `tools[]` entry (carrying no
          `name`) that declares the computer tool family. The model is
          served the family's tool with any members disabled via `configs`
          removed from its schema. Every member is enabled by default, zoom
          included. The single-tool options `display_number` and
          `enable_zoom` are not fields of a toolset entry — it carries only
          `type`, `configs`, and `cache_control`; zoom is controlled
          via `configs.zoom.enabled`.

          - `JsonElement Type = "computer_toolset_20260801"`

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `ComputerToolsetConfigs? Configs`

            Per-member configuration for `computer_toolset_20260801`: one
            optional field per member tool, keyed by the member name — the same
            name the member's `tool_use` blocks carry. Every member is an
            accepted key, and a member's defaults apply wherever its key is
            absent. Unknown keys are rejected: the field set is this toolset
            version's complete member set.

            - `ComputerCursorPositionConfig? CursorPosition`

              `cursor_position`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `ComputerDoubleClickConfig? DoubleClick`

              `double_click`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `ComputerHoldKeyConfig? HoldKey`

              `hold_key`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `ComputerKeyConfig? Key`

              `key`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `ComputerLeftClickConfig? LeftClick`

              `left_click`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `ComputerLeftClickDragConfig? LeftClickDrag`

              `left_click_drag`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `ComputerLeftMouseDownConfig? LeftMouseDown`

              `left_mouse_down`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `ComputerLeftMouseUpConfig? LeftMouseUp`

              `left_mouse_up`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `ComputerMiddleClickConfig? MiddleClick`

              `middle_click`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `ComputerMouseMoveConfig? MouseMove`

              `mouse_move`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `ComputerRightClickConfig? RightClick`

              `right_click`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `ComputerScreenshotConfig? Screenshot`

              `screenshot`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `ComputerScrollConfig? Scroll`

              `scroll`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `ComputerTripleClickConfig? TripleClick`

              `triple_click`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `ComputerTypeConfig? Type`

              `type`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `ComputerWaitConfig? Wait`

              `wait`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `ComputerZoomConfig? Zoom`

              `zoom`'s config overrides.

              - `bool? DeferLoading`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `bool? Enabled`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `class ToolTextEditor20250124:`

          - `JsonElement Name = "str_replace_editor"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type = "text_editor_20250124"`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct("direct")`

            - `CodeExecution20250825("code_execution_20250825")`

            - `CodeExecution20260120("code_execution_20260120")`

            - `CodeExecution20260521("code_execution_20260521")`

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class ToolTextEditor20250429:`

          - `JsonElement Name = "str_replace_based_edit_tool"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type = "text_editor_20250429"`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct("direct")`

            - `CodeExecution20250825("code_execution_20250825")`

            - `CodeExecution20260120("code_execution_20260120")`

            - `CodeExecution20260521("code_execution_20260521")`

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class ToolTextEditor20250728:`

          - `JsonElement Name = "str_replace_based_edit_tool"`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type = "text_editor_20250728"`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct("direct")`

            - `CodeExecution20250825("code_execution_20250825")`

            - `CodeExecution20260120("code_execution_20260120")`

            - `CodeExecution20260521("code_execution_20260521")`

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

          - `long? MaxCharacters`

            Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

            minimum: 1

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class WebSearchTool20250305:`

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

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `long? MaxUses`

            Maximum number of times the tool can be used in the API request.

            exclusiveMinimum: 0

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

          - `UserLocation? UserLocation`

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

        - `class WebFetchTool20250910:`

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

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `CitationsConfigParam? Citations`

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

        - `class WebSearchTool20260209:`

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

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `long? MaxUses`

            Maximum number of times the tool can be used in the API request.

            exclusiveMinimum: 0

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

          - `UserLocation? UserLocation`

            Parameters for the user's location. Used to provide more relevant search results.

        - `class WebFetchTool20260209:`

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

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `CitationsConfigParam? Citations`

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

        - `class WebFetchTool20260309:`

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

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `CitationsConfigParam? Citations`

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

        - `class WebSearchTool20260318:`

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

          - `CacheControlEphemeral? CacheControl`

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

          - `UserLocation? UserLocation`

            Parameters for the user's location. Used to provide more relevant search results.

        - `class WebFetchTool20260318:`

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

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `CitationsConfigParam? Citations`

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

        - `class ToolSearchToolBm25_20251119:`

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

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class ToolSearchToolRegex20251119:`

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

          - `CacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

      - `double Temperature`

        **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not support setting temperature. A value of 1.0 of will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

        Amount of randomness injected into the response.

        Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

        Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

        maximum: 1, minimum: 0

      - `long TopK`

        **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not accept top_k; any value will be rejected with a 400 error.

        Only sample from the top K options for each subsequent token.

        Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

        Recommended for advanced use cases only.

        minimum: 0

      - `double TopP`

        **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not support setting top_p. A value >= 0.99 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

        Use nucleus sampling.

        In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.

        Recommended for advanced use cases only.

        maximum: 1, minimum: 0

  - `string userProfileID`

    Header param: The user profile ID to attribute the requests in this batch to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header. Applies to every request in the batch; an individual request whose `user_profile_id` body field conflicts with this header is errored.

## Returns

- `class MessageBatch:`

  - `required string ID`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `required DateTimeOffset? ArchivedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

    format: date-time

  - `required DateTimeOffset? CancelInitiatedAt`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

    format: date-time

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

    format: date-time

  - `required DateTimeOffset? EndedAt`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

    format: date-time

  - `required DateTimeOffset ExpiresAt`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

    format: date-time

  - `required ProcessingStatus ProcessingStatus`

    Processing status of the Message Batch.

    - `InProgress("in_progress")`

    - `Canceling("canceling")`

    - `Ended("ended")`

  - `required MessageBatchRequestCounts RequestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `required long Canceled`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

    - `required long Errored`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

    - `required long Expired`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

    - `required long Processing`

      Number of requests in the Message Batch that are processing.

    - `required long Succeeded`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

  - `required string? ResultsUrl`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `JsonElement Type = "message_batch"`

    Object type.

    For Message Batches, this is always `"message_batch"`.

## Example

```csharp
BatchCreateParams parameters = new()
{
    Requests =
    [
        new()
        {
            CustomID = "my-custom-id-1",
            Params = new()
            {
                MaxTokens = 1024,
                Messages =
                [
                    new()
                    {
                        Content = "Hello, world",
                        Role = Role.User,
                    },
                ],
                Model = Model.ClaudeOpus5,
                CacheControl = new() { Ttl = Ttl.Ttl5m },
                Container = new ContainerParams()
                {
                    ID = "id",
                    Skills =
                    [
                        new()
                        {
                            SkillID = "pdf",
                            Type = SkillParamsType.Anthropic,
                            Version = "latest",
                        },
                    ],
                },
                InferenceGeo = "inference_geo",
                Metadata = new()
                {
                    UserID = "13803d75-b4b5-4c3e-b2a2-6f21399b021b"
                },
                OutputConfig = new()
                {
                    Effort = Effort.Low,
                    Format = new()
                    {
                        Schema = new Dictionary<string, JsonElement>()
                        {
                            { "foo", JsonSerializer.SerializeToElement("bar") }
                        },
                    },
                },
                ServiceTier = ServiceTier.Auto,
                StopSequences =
                [
                    "string"
                ],
                Stream = false,
                System = new(

                    [
                        new TextBlockParam()
                        {
                            Text = "Today's date is 2024-06-01.",
                            CacheControl = new() { Ttl = Ttl.Ttl5m },
                            Citations =
                            [
                                new CitationCharLocationParam()
                                {
                                    CitedText = "The grass is green. The sky is blue.",
                                    DocumentIndex = 0,
                                    DocumentTitle = "x",
                                    EndCharIndex = 0,
                                    StartCharIndex = 0,
                                },
                            ],
                        },
                    ]
                ),
                Temperature = 1,
                Thinking = new ThinkingConfigAdaptive()
                {
                    Display = Display.Summarized
                },
                ToolChoice = new ToolChoiceAuto()
                {
                    DisableParallelToolUse = true
                },
                Tools =
                [
                    new Tool()
                    {
                        InputSchema = new()
                        {
                            Properties = new Dictionary<string, JsonElement>()
                            {
                                { "location", JsonSerializer.SerializeToElement("bar") },
                                { "unit", JsonSerializer.SerializeToElement("bar") },
                            },
                            Required =
                            [
                                "location"
                            ],
                        },
                        Name = "name",
                        AllowedCallers =
                        [
                            AllowedCaller.Direct
                        ],
                        CacheControl = new() { Ttl = Ttl.Ttl5m },
                        DeferLoading = true,
                        Description = "Get the current weather in a given location",
                        EagerInputStreaming = true,
                        InputExamples =
                        [
                            new Dictionary<string, JsonElement>()
                            {
                                { "foo", JsonSerializer.SerializeToElement("bar") },
                            },
                        ],
                        Strict = true,
                        Type = Type.Custom,
                    },
                ],
                TopK = 5,
                TopP = 0.7,
            },
        },
    ],
};

var messageBatch = await client.Messages.Batches.Create(parameters);

Console.WriteLine(messageBatch);
```

### Response (200)

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
