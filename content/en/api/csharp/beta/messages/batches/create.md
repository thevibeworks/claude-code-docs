# Create a Message Batch

`BetaMessageBatch Beta.Messages.Batches.Create(parameters, cancellationToken = default)`

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

      - `required IReadOnlyList<BetaMessageParam> Messages`

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

          - `IReadOnlyList<BetaContentBlockParam>`

            - `class BetaTextBlockParam:`

              - `required string Text`

                minLength: 1

              - `JsonElement Type constant`

              - `BetaCacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

                - `JsonElement Type constant`

                - `Ttl Ttl`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

                  - `Ttl5m`

                  - `Ttl1h`

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

                  - `JsonElement Type constant`

                - `class BetaCitationPageLocationParam:`

                  - `required string CitedText`

                  - `required long DocumentIndex`

                    minimum: 0

                  - `required string? DocumentTitle`

                    maxLength: 500, minLength: 1

                  - `required long EndPageNumber`

                  - `required long StartPageNumber`

                    minimum: 1

                  - `JsonElement Type constant`

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

                  - `JsonElement Type constant`

                - `class BetaCitationWebSearchResultLocationParam:`

                  - `required string CitedText`

                  - `required string EncryptedIndex`

                  - `required string? Title`

                    maxLength: 512, minLength: 1

                  - `JsonElement Type constant`

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

                  - `JsonElement Type constant`

            - `class BetaImageBlockParam:`

              - `required Source Source`

                - `class BetaBase64ImageSource:`

                  - `required string Data`

                    format: byte

                  - `required MediaType MediaType`

                    - `ImageJpeg`

                    - `ImagePng`

                    - `ImageGif`

                    - `ImageWebP`

                  - `JsonElement Type constant`

                - `class BetaUrlImageSource:`

                  - `JsonElement Type constant`

                  - `required string Url`

                - `class BetaFileImageSource:`

                  - `required string FileID`

                  - `JsonElement Type constant`

              - `JsonElement Type constant`

              - `BetaCacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

              - `BetaImageTransformationsParam? Transformations`

                Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

                - `OversizedImage OversizedImage`

                  What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

                  - `Downsize`

                  - `Error`

            - `class BetaRequestDocumentBlock:`

              - `required Source Source`

                - `class BetaBase64PdfSource:`

                  - `required string Data`

                    format: byte

                  - `JsonElement MediaType constant`

                  - `JsonElement Type constant`

                - `class BetaPlainTextSource:`

                  - `required string Data`

                  - `JsonElement MediaType constant`

                  - `JsonElement Type constant`

                - `class BetaContentBlockSource:`

                  - `required Content Content`

                    - `string`

                    - `IReadOnlyList<BetaContentBlockSourceContent>`

                      - `class BetaTextBlockParam:`

                      - `class BetaImageBlockParam:`

                  - `JsonElement Type constant`

                - `class BetaUrlPdfSource:`

                  - `JsonElement Type constant`

                  - `required string Url`

                - `class BetaFileDocumentSource:`

                  - `required string FileID`

                  - `JsonElement Type constant`

              - `JsonElement Type constant`

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

                - `JsonElement Type constant`

                - `BetaCacheControlEphemeral? CacheControl`

                  Create a cache control breakpoint at this content block.

                - `IReadOnlyList<BetaTextCitationParam>? Citations`

              - `required string Source`

              - `required string Title`

              - `JsonElement Type constant`

              - `BetaCacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

              - `BetaCitationsConfigParam Citations`

            - `class BetaThinkingBlockParam:`

              - `required string Signature`

                The `signature` value of this thinking block, exactly as returned by the API in a previous response. Used to verify that the block was generated by Claude.

                Thinking blocks must be passed back unmodified and in their original order; a modified block results in a 400 `invalid_request_error`.

              - `required string Thinking`

                The `thinking` text of this block as returned by the API.

              - `JsonElement Type constant`

            - `class BetaRedactedThinkingBlockParam:`

              - `required string Data`

                The `data` value of this redacted thinking block, exactly as returned by the API in a previous response. Opaque and encrypted; pass it back unchanged.

              - `JsonElement Type constant`

            - `class BetaToolUseBlockParam:`

              - `required string ID`

                pattern: ^[a-zA-Z0-9_-]+$

              - `required IReadOnlyDictionary<string, JsonElement> Input`

              - `required string Name`

                maxLength: 200, minLength: 1

              - `JsonElement Type constant`

              - `BetaCacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

              - `Caller Caller`

                Tool invocation directly from the model.

                - `class BetaDirectCaller:`

                  Tool invocation directly from the model.

                  - `JsonElement Type constant`

                - `class BetaServerToolCaller:`

                  Tool invocation generated by a server-side tool.

                  - `required string ToolID`

                    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

                  - `JsonElement Type constant`

                - `class BetaServerToolCaller20260120:`

                  - `required string ToolID`

                    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

                  - `JsonElement Type constant`

              - `string? ToolsetName`

                For a toolset member tool_use, the toolset family this member belongs to.

                maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

            - `class BetaToolResultBlockParam:`

              - `required string ToolUseID`

                pattern: ^[a-zA-Z0-9_-]+$

              - `JsonElement Type constant`

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

                    - `JsonElement Type constant`

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

                    - `JsonElement Type constant`

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

                        - `JsonElement Type constant`

                      - `class BetaBrowserStateChangeDownloadStarted:`

                        A file download that started during this call.

                        - `required string DownloadID`

                          The caller-assigned identifier for this download, stable across the state changes reporting it.

                          maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                        - `JsonElement Type constant`

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

                        - `JsonElement Type constant`

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

                        - `JsonElement Type constant`

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

                - `Advisor`

                - `WebSearch`

                - `WebFetch`

                - `CodeExecution`

                - `BashCodeExecution`

                - `TextEditorCodeExecution`

                - `ToolSearchToolRegex`

                - `ToolSearchToolBm25`

              - `JsonElement Type constant`

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

                  - `JsonElement Type constant`

                  - `required string Url`

                  - `string? PageAge`

                - `class BetaWebSearchToolRequestError:`

                  - `required BetaWebSearchToolResultErrorCode ErrorCode`

                    - `InvalidToolInput`

                    - `Unavailable`

                    - `MaxUsesExceeded`

                    - `TooManyRequests`

                    - `QueryTooLong`

                    - `RequestTooLarge`

                  - `JsonElement Type constant`

              - `required string ToolUseID`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `JsonElement Type constant`

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

                    - `InvalidToolInput`

                    - `UrlTooLong`

                    - `UrlNotAllowed`

                    - `UrlNotInPriorContext`

                    - `UrlNotAccessible`

                    - `UnsupportedContentType`

                    - `TooManyRequests`

                    - `MaxUsesExceeded`

                    - `Unavailable`

                  - `JsonElement Type constant`

                - `class BetaWebFetchBlockParam:`

                  - `required BetaRequestDocumentBlock Content`

                  - `JsonElement Type constant`

                  - `required string Url`

                    Fetched content URL

                  - `string? RetrievedAt`

                    ISO 8601 timestamp when the content was retrieved

              - `required string ToolUseID`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `JsonElement Type constant`

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

                    - `MaxUsesExceeded`

                    - `PromptTooLong`

                    - `TooManyRequests`

                    - `Overloaded`

                    - `Unavailable`

                    - `ExecutionTimeExceeded`

                    - `ModelNotFound`

                  - `JsonElement Type constant`

                - `class BetaAdvisorResultBlockParam:`

                  - `required string Text`

                  - `JsonElement Type constant`

                  - `string? StopReason`

                - `class BetaAdvisorRedactedResultBlockParam:`

                  - `required string EncryptedContent`

                    Opaque blob produced by a prior response; must be round-tripped verbatim.

                  - `JsonElement Type constant`

                  - `string? StopReason`

              - `required string ToolUseID`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `JsonElement Type constant`

              - `BetaCacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

            - `class BetaCodeExecutionToolResultBlockParam:`

              - `required BetaCodeExecutionToolResultBlockParamContent Content`

                Code execution result with encrypted stdout for PFC + web_search results.

                - `class BetaCodeExecutionToolResultErrorParam:`

                  - `required BetaCodeExecutionToolResultErrorCode ErrorCode`

                    - `InvalidToolInput`

                    - `Unavailable`

                    - `TooManyRequests`

                    - `ExecutionTimeExceeded`

                  - `JsonElement Type constant`

                - `class BetaCodeExecutionResultBlockParam:`

                  - `required IReadOnlyList<BetaCodeExecutionOutputBlockParam> Content`

                    - `required string FileID`

                    - `JsonElement Type constant`

                  - `required long ReturnCode`

                  - `required string Stderr`

                  - `required string Stdout`

                  - `JsonElement Type constant`

                - `class BetaEncryptedCodeExecutionResultBlockParam:`

                  Code execution result with encrypted stdout for PFC + web_search results.

                  - `required IReadOnlyList<BetaCodeExecutionOutputBlockParam> Content`

                    - `required string FileID`

                    - `JsonElement Type constant`

                  - `required string EncryptedStdout`

                  - `required long ReturnCode`

                  - `required string Stderr`

                  - `JsonElement Type constant`

              - `required string ToolUseID`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `JsonElement Type constant`

              - `BetaCacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

            - `class BetaBashCodeExecutionToolResultBlockParam:`

              - `required Content Content`

                - `class BetaBashCodeExecutionToolResultErrorParam:`

                  - `required ErrorCode ErrorCode`

                    - `InvalidToolInput`

                    - `Unavailable`

                    - `TooManyRequests`

                    - `ExecutionTimeExceeded`

                    - `OutputFileTooLarge`

                  - `JsonElement Type constant`

                - `class BetaBashCodeExecutionResultBlockParam:`

                  - `required IReadOnlyList<BetaBashCodeExecutionOutputBlockParam> Content`

                    - `required string FileID`

                    - `JsonElement Type constant`

                  - `required long ReturnCode`

                  - `required string Stderr`

                  - `required string Stdout`

                  - `JsonElement Type constant`

              - `required string ToolUseID`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `JsonElement Type constant`

              - `BetaCacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

            - `class BetaTextEditorCodeExecutionToolResultBlockParam:`

              - `required Content Content`

                - `class BetaTextEditorCodeExecutionToolResultErrorParam:`

                  - `required ErrorCode ErrorCode`

                    - `InvalidToolInput`

                    - `Unavailable`

                    - `TooManyRequests`

                    - `ExecutionTimeExceeded`

                    - `FileNotFound`

                  - `JsonElement Type constant`

                  - `string? ErrorMessage`

                - `class BetaTextEditorCodeExecutionViewResultBlockParam:`

                  - `required string Content`

                  - `required FileType FileType`

                    - `Text`

                    - `Image`

                    - `Pdf`

                  - `JsonElement Type constant`

                  - `long? NumLines`

                  - `long? StartLine`

                  - `long? TotalLines`

                - `class BetaTextEditorCodeExecutionCreateResultBlockParam:`

                  - `required bool IsFileUpdate`

                  - `JsonElement Type constant`

                - `class BetaTextEditorCodeExecutionStrReplaceResultBlockParam:`

                  - `JsonElement Type constant`

                  - `IReadOnlyList<string>? Lines`

                  - `long? NewLines`

                  - `long? NewStart`

                  - `long? OldLines`

                  - `long? OldStart`

              - `required string ToolUseID`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `JsonElement Type constant`

              - `BetaCacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

            - `class BetaToolSearchToolResultBlockParam:`

              - `required Content Content`

                - `class BetaToolSearchToolResultErrorParam:`

                  - `required ErrorCode ErrorCode`

                    - `InvalidToolInput`

                    - `Unavailable`

                    - `TooManyRequests`

                    - `ExecutionTimeExceeded`

                  - `JsonElement Type constant`

                  - `string? ErrorMessage`

                - `class BetaToolSearchToolSearchResultBlockParam:`

                  - `required IReadOnlyList<BetaToolReferenceBlockParam> ToolReferences`

                    - `required string ToolName`

                      maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

                    - `JsonElement Type constant`

                    - `BetaCacheControlEphemeral? CacheControl`

                      Create a cache control breakpoint at this content block.

                  - `JsonElement Type constant`

              - `required string ToolUseID`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `JsonElement Type constant`

              - `BetaCacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

            - `class BetaMcpToolUseBlockParam:`

              - `required string ID`

                pattern: ^[a-zA-Z0-9_-]+$

              - `required IReadOnlyDictionary<string, JsonElement> Input`

              - `required string Name`

              - `required string ServerName`

                The name of the MCP server

              - `JsonElement Type constant`

              - `BetaCacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

            - `class BetaRequestMcpToolResultBlockParam:`

              - `required string ToolUseID`

                pattern: ^[a-zA-Z0-9_-]+$

              - `JsonElement Type constant`

              - `BetaCacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

              - `Content Content`

                - `string`

                - `IReadOnlyList<BetaTextBlockParam>`

                  - `required string Text`

                    minLength: 1

                  - `JsonElement Type constant`

                  - `BetaCacheControlEphemeral? CacheControl`

                    Create a cache control breakpoint at this content block.

                  - `IReadOnlyList<BetaTextCitationParam>? Citations`

              - `bool IsError`

            - `class BetaContainerUploadBlockParam:`

              A content block that represents a file to be uploaded to the container
              Files uploaded via this block will be available in the container's input directory.

              - `required string FileID`

              - `JsonElement Type constant`

              - `BetaCacheControlEphemeral? CacheControl`

                Create a cache control breakpoint at this content block.

            - `class BetaCompactionBlockParam:`

              A compaction block containing summary of previous context.

              Users should round-trip these blocks from responses to subsequent requests
              to maintain context across compaction boundaries.

              When content is None, the block represents a failed compaction. The server
              treats these as no-ops. Empty string content is not allowed.

              - `JsonElement Type constant`

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

                  - `JsonElement Type constant`

                - `class BetaToolChangeMcpToolReference:`

                  Reference to a single MCP tool by its server and remote name — the
                  same `server_name`/`name` pair `mcp_tool_use` carries.

                  - `required string Name`

                  - `required string ServerName`

                  - `JsonElement Type constant`

                - `class BetaToolChangeMcpToolsetReference:`

                  Reference to every tool in the named MCP server's toolset.

                  - `required string ServerName`

                  - `JsonElement Type constant`

              - `JsonElement Type constant`

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

              - `JsonElement Type constant`

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

                  - `ClaudeFable5_1`

                    Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

                  - `ClaudeMythos5_1`

                    Our most capable model for cybersecurity and biology research, available through trusted access programs

                  - `ClaudeSonnet5`

                    High-performance model for coding and agents

                  - `ClaudeFable5`

                    Next generation of intelligence for the hardest knowledge work and coding problems

                  - `ClaudeMythos5`

                    Most capable model for cybersecurity and biology research

                  - `ClaudeOpus5`

                    Powerful intelligence for long-running agents and coding

                  - `ClaudeOpus4_8`

                    Powerful intelligence for long-running agents and coding

                  - `ClaudeOpus4_7`

                    Powerful intelligence for long-running agents and coding

                  - `ClaudeMythosPreview`

                    New class of intelligence, strongest in coding and cybersecurity

                  - `ClaudeOpus4_6`

                    Powerful intelligence for long-running agents and coding

                  - `ClaudeSonnet4_6`

                    Best combination of speed and intelligence

                  - `ClaudeHaiku4_5`

                    Fastest model with near-frontier intelligence

                  - `ClaudeHaiku4_5_20251001`

                    Fastest model with near-frontier intelligence

                  - `ClaudeOpus4_5`

                    Powerful intelligence for long-running agents and coding

                  - `ClaudeOpus4_5_20251101`

                    Powerful intelligence for long-running agents and coding

                  - `ClaudeSonnet4_5`

                    High-performance model for agents and coding

                  - `ClaudeSonnet4_5_20250929`

                    High-performance model for agents and coding

              - `required BetaFallbackInfoParam To`

                Identifies one hop of a fallback transition.

              - `JsonElement Type constant`

              - `JsonElement Trigger`

                The response block's `trigger`, echoed verbatim. Accepted and ignored by the server; any object or `null` is allowed.

        - `required Role Role`

          - `User`

          - `Assistant`

          - `System`

        - `ClearAt? ClearAt`

          How long this system message's text stays in front of the model. `"never"` (the default) renders it on every request that includes it. `"next_user_message"` renders it only for the user turn it follows: once a later `role: "user"` message exists in `messages` the message stays in the array (send it unchanged) but is no longer shown to the model. Only permitted on `role: "system"` messages.

          - `NextUserMessage`

          - `Never`

        - `BetaSystemMessageOutputConfig? OutputConfig`

          Per-message output configuration on a role:"system" input message.

          Fields here apply per-turn; `format` remains top-level only. An
          empty `{}` is accepted on a message that carries content; a message
          with neither content nor output_config fields is rejected.

          - `Effort? Effort`

            All possible effort levels.

            - `Low`

            - `Medium`

            - `High`

            - `Xhigh`

            - `Max`

      - `required Model Model`

        The model that will complete your prompt.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `BetaCacheControlEphemeral? CacheControl`

        Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

      - `Container? Container`

        Container identifier for reuse across requests.

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

              - `Anthropic`

              - `Custom`

            - `string Version`

              Skill version or 'latest' for most recent version

              maxLength: 64, minLength: 1

        - `string`

      - `BetaContextManagementConfig? ContextManagement`

        Context management configuration.

        This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.

        - `IReadOnlyList<Edit> Edits`

          List of context management edits to apply

          minItems: 0

          - `class BetaClearToolUses20250919Edit:`

            - `JsonElement Type constant`

            - `BetaInputTokensClearAtLeast? ClearAtLeast`

              Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

              - `JsonElement Type constant`

              - `required long Value`

                minimum: 0

            - `ClearToolInputs? ClearToolInputs`

              Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

              - `bool`

              - `IReadOnlyList<string>`

            - `IReadOnlyList<string>? ExcludeTools`

              Tool names whose uses are preserved from clearing

            - `BetaToolUsesKeep Keep`

              Number of tool uses to retain in the conversation

              - `JsonElement Type constant`

              - `required long Value`

                minimum: 0

            - `Trigger Trigger`

              Condition that triggers the context management strategy

              - `class BetaInputTokensTrigger:`

                - `JsonElement Type constant`

                - `required long Value`

                  minimum: 1

              - `class BetaToolUsesTrigger:`

                - `JsonElement Type constant`

                - `required long Value`

                  minimum: 1

          - `class BetaClearThinking20251015Edit:`

            - `JsonElement Type constant`

            - `Keep Keep`

              Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

              - `class BetaThinkingTurns:`

                - `JsonElement Type constant`

                - `required long Value`

                  minimum: 1

              - `class BetaAllThinkingTurns:`

                - `JsonElement Type constant`

              - `class All:`

          - `class BetaCompact20260112Edit:`

            Automatically compact older context when reaching the configured trigger threshold.

            - `JsonElement Type constant`

            - `string? Instructions`

              Additional instructions for summarization.

            - `bool PauseAfterCompaction`

              Whether to pause after compaction and return the compaction block to the user.

            - `BetaInputTokensTrigger? Trigger`

              When to trigger compaction. Defaults to 150000 input tokens.

      - `BetaDiagnosticsParam? Diagnostics`

        Request-level diagnostics. Currently carries the previous response
        id for prompt-cache divergence reporting.

        - `string? PreviousMessageID`

          The `id` (`msg_...`) from this client's previous /v1/messages response. The server compares that request's prompt fingerprint against this one and returns `diagnostics.cache_miss_reason` when the prompt-cache prefix could not be reused. Pass `null` on the first turn to opt in without a prior message to compare.

          maxLength: 256

      - `FallbackCreditToken? FallbackCreditToken`

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

            - `Strict`

            - `BestEffort`

      - `BetaFallbacksParam? Fallbacks`

        Opt-in server-side retry on one or more substitute models when the requested model declines for policy reasons. Tried in order: if the first entry also declines, the second is tried, and so on. The string "default" requests the requested model's server-defined default fallback configuration.

        - `IReadOnlyList<BetaFallbackParam>`

          - `required Model Model`

            The model that will complete your prompt.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `long? MaxTokens`

          - `BetaOutputConfig? OutputConfig`

            - `Effort? Effort`

              All possible effort levels.

              - `Low`

              - `Medium`

              - `High`

              - `Xhigh`

              - `Max`

            - `BetaJsonOutputFormat? Format`

              A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

              - `required IReadOnlyDictionary<string, JsonElement> Schema`

                The JSON schema of the format

              - `JsonElement Type constant`

            - `BetaTokenTaskBudget? TaskBudget`

              User-configurable total token budget across contexts.

              - `required long Total`

                Total token budget across all contexts in the session.

                minimum: 1024

              - `JsonElement Type constant`

                The budget type. Currently only 'tokens' is supported.

              - `long? Remaining`

                Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.

                minimum: 0

          - `Speed? Speed`

            Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

            - `Standard`

            - `Fast`

          - `Thinking? Thinking`

            - `class BetaThinkingConfigEnabled:`

              - `required long BudgetTokens`

                Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

                Must be ≥1024 and less than `max_tokens`.

                See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

                minimum: 1024

              - `JsonElement Type constant`

              - `BetaThinkingBlockBinding? BlockBinding`

                Controls for block binding: what happens when a thinking block this
                request sends back fails the conversation check. Every field is optional;
                an empty object means every default.

                - `BetaThinkingPrefixMismatchBehavior? PrefixMismatchBehavior`

                  What happens when a thinking block in `messages` fails the conversation
                  check: it was created in a different conversation, or the messages before
                  it have changed since. `"error"` (the default) fails the request with a
                  400 error. `"drop_block"` removes the failing blocks and the request
                  proceeds; the model no longer sees the dropped reasoning.

                  - `Error`

                  - `DropBlock`

              - `Display? Display`

                Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

                - `Summarized`

                - `Omitted`

                - `Updates`

            - `class BetaThinkingConfigDisabled:`

              - `JsonElement Type constant`

            - `class BetaThinkingConfigAdaptive:`

              - `JsonElement Type constant`

              - `BetaThinkingBlockBinding? BlockBinding`

                Controls for block binding: what happens when a thinking block this
                request sends back fails the conversation check. Every field is optional;
                an empty object means every default.

              - `Display? Display`

                Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

                - `Summarized`

                - `Omitted`

                - `Updates`

        - `JsonElement`

      - `string? InferenceGeo`

        Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

      - `IReadOnlyList<BetaRequestMcpServerUrlDefinition> McpServers`

        MCP servers to be utilized in this request

        maxItems: 20

        - `required string Name`

        - `JsonElement Type constant`

        - `required string Url`

        - `string? AuthorizationToken`

        - `BetaRequestMcpServerToolConfiguration? ToolConfiguration`

          - `IReadOnlyList<string>? AllowedTools`

          - `bool? Enabled`

      - `BetaMetadata Metadata`

        An object describing metadata about the request.

        - `string? UserID`

          An external identifier for the user who is associated with the request.

          This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

          maxLength: 512

      - `BetaOutputConfig OutputConfig`

        Configuration options for the model's output, such as the output format.

      - `ServiceTier ServiceTier`

        Determines whether to use priority capacity (if available) or standard capacity for this request.

        Anthropic offers different levels of service for your API requests. See [service-tiers](https://platform.claude.com/docs/en/api/service-tiers) for details.

        - `Auto`

        - `StandardOnly`

      - `Speed? Speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `Standard`

        - `Fast`

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

        - `IReadOnlyList<BetaTextBlockParam>`

          - `required string Text`

            minLength: 1

          - `JsonElement Type constant`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `IReadOnlyList<BetaTextCitationParam>? Citations`

      - `BetaThinkingConfigParam Thinking`

        Configuration for enabling Claude's extended thinking.

        When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

        See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

        - `class BetaThinkingConfigEnabled:`

        - `class BetaThinkingConfigDisabled:`

        - `class BetaThinkingConfigAdaptive:`

      - `BetaToolChoice ToolChoice`

        How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

        - `class BetaToolChoiceAuto:`

          The model will automatically decide whether to use tools.

          - `JsonElement Type constant`

          - `bool DisableParallelToolUse`

            Whether to disable parallel tool use.

            Defaults to `false`. If set to `true`, the model will output at most one tool use.

        - `class BetaToolChoiceAny:`

          The model will use any available tools.

          - `JsonElement Type constant`

          - `bool DisableParallelToolUse`

            Whether to disable parallel tool use.

            Defaults to `false`. If set to `true`, the model will output exactly one tool use.

        - `class BetaToolChoiceTool:`

          The model will use the specified tool with `tool_choice.name`.

          - `required string Name`

            The name of the tool to use.

          - `JsonElement Type constant`

          - `bool DisableParallelToolUse`

            Whether to disable parallel tool use.

            Defaults to `false`. If set to `true`, the model will output exactly one tool use.

        - `class BetaToolChoiceNone:`

          The model will not be allowed to use tools.

          - `JsonElement Type constant`

      - `IReadOnlyList<BetaToolUnion> Tools`

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

        - `class BetaTool:`

          - `required InputSchema InputSchema`

            [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

            This defines the shape of the `input` that your tool accepts and that the model will produce.

            - `JsonElement Type constant`

            - `IReadOnlyDictionary<string, JsonElement>? Properties`

            - `IReadOnlyList<string>? Required`

          - `required string Name`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            maxLength: 128, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,128}$

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

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

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaToolBash20250124:`

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaCodeExecutionTool20250522:`

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaCodeExecutionTool20250825:`

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaCodeExecutionTool20260120:`

          Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaCodeExecutionTool20260521:`

          Code execution tool with REPL state persistence.

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

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

          - `JsonElement Type constant`

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

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

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

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

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

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

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

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

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

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

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

          - `JsonElement Type constant`

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

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaToolTextEditor20250429:`

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> InputExamples`

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaToolTextEditor20250728:`

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

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

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

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

            - `JsonElement Type constant`

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

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

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

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

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

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

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

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

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

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

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

            - `Full`

            - `Excluded`

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

          - `BetaUserLocation? UserLocation`

            Parameters for the user's location. Used to provide more relevant search results.

        - `class BetaWebFetchTool20260318:`

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

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

            - `Full`

            - `Excluded`

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

          - `bool UseCache`

            Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

        - `class BetaAdvisorTool20260301:`

          - `required Model Model`

            The model that will complete your prompt.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `JsonElement Type constant`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

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

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `required Type Type`

            - `ToolSearchToolBm25_20251119`

            - `ToolSearchToolBm25`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

          - `BetaCacheControlEphemeral? CacheControl`

            Create a cache control breakpoint at this content block.

          - `bool DeferLoading`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `bool Strict`

            When true, guarantees schema validation on tool names and inputs

        - `class BetaToolSearchToolRegex20251119:`

          - `JsonElement Name constant`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `required Type Type`

            - `ToolSearchToolRegex20251119`

            - `ToolSearchToolRegex`

          - `IReadOnlyList<AllowedCaller> AllowedCallers`

            - `Direct`

            - `CodeExecution20250825`

            - `CodeExecution20260120`

            - `CodeExecution20260521`

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

          - `JsonElement Type constant`

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

      - `BetaJsonOutputFormat? OutputFormat`

        **Deprecated**

        Deprecated: Use `output_config.format` instead. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

        A schema to specify Claude's output format in responses. This parameter will be removed in a future release.

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

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

    - `MidConversationOutputConfig2026_07_01`

    - `ThinkingBindingControls2026_08_01`

    - `MidConversationSystemClearAt2026_08_21`

  - `string userProfileID`

    Header param: The user profile ID to attribute the requests in this batch to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header. Applies to every request in the batch; an individual request whose `user_profile_id` body field conflicts with this header is errored.

## Returns

- `class BetaMessageBatch:`

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

    - `InProgress`

    - `Canceling`

    - `Ended`

  - `required BetaMessageBatchRequestCounts RequestCounts`

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

  - `JsonElement Type constant`

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
                        ClearAt = ClearAt.NextUserMessage,
                        OutputConfig = new() { Effort = Effort.Low },
                    },
                ],
                Model = Model.ClaudeOpus5,
                CacheControl = new() { Ttl = Ttl.Ttl5m },
                Container = new BetaContainerParams()
                {
                    ID = "id",
                    Skills =
                    [
                        new()
                        {
                            SkillID = "pdf",
                            Type = Type.Anthropic,
                            Version = "latest",
                        },
                    ],
                },
                ContextManagement = new()
                {
                    Edits =
                    [
                        new BetaClearToolUses20250919Edit()
                        {
                            ClearAtLeast = new(0),
                            ClearToolInputs = true,
                            ExcludeTools =
                            [
                                "string"
                            ],
                            Keep = new(0),
                            Trigger = new BetaInputTokensTrigger(1),
                        },
                    ],
                },
                Diagnostics = new()
                {
                    PreviousMessageID = "previous_message_id"
                },
                FallbackCreditToken = "x",
                Fallbacks = new Default(),
                InferenceGeo = "inference_geo",
                McpServers =
                [
                    new()
                    {
                        Name = "name",
                        Url = "url",
                        AuthorizationToken = "authorization_token",
                        ToolConfiguration = new()
                        {
                            AllowedTools =
                            [
                                "string"
                            ],
                            Enabled = true,
                        },
                    },
                ],
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
                    TaskBudget = new()
                    {
                        Total = 1024,
                        Remaining = 0,
                    },
                },
                OutputFormat = new()
                {
                    Schema = new Dictionary<string, JsonElement>()
                    {
                        { "foo", JsonSerializer.SerializeToElement("bar") }
                    },
                },
                ServiceTier = ServiceTier.Auto,
                Speed = Speed.Standard,
                StopSequences =
                [
                    "string"
                ],
                Stream = false,
                System = new(

                    [
                        new BetaTextBlockParam()
                        {
                            Text = "Today's date is 2024-06-01.",
                            CacheControl = new() { Ttl = Ttl.Ttl5m },
                            Citations =
                            [
                                new BetaCitationCharLocationParam()
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
                Thinking = new BetaThinkingConfigAdaptive()
                {
                    BlockBinding = new()
                    {
                        PrefixMismatchBehavior = BetaThinkingPrefixMismatchBehavior.Error,
                    },
                    Display = Display.Summarized,
                },
                ToolChoice = new BetaToolChoiceAuto()
                {
                    DisableParallelToolUse = true
                },
                Tools =
                [
                    new BetaTool()
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

var betaMessageBatch = await client.Beta.Messages.Batches.Create(parameters);

Console.WriteLine(betaMessageBatch);
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
