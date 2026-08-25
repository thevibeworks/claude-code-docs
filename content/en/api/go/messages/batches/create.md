# Create a Message Batch

`client.Messages.Batches.New(ctx, params) (*MessageBatch, error)`

**POST** `/v1/messages/batches`

Send a batch of Message creation requests.

The Message Batches API can be used to process multiple Messages API requests at once. Once a Message Batch is created, it begins processing immediately. Batches can take up to 24 hours to complete.

Learn more about the Message Batches API in our [user guide](https://platform.claude.com/docs/en/build-with-claude/batch-processing)

## Parameters

- `params MessageBatchNewParams`

  - `Requests param.Field[[]MessageBatchNewParamsRequest]`

    Body param: List of requests for prompt completion. Each is an individual request to create a Message.

    maxItems: 100000, minItems: 1

    - `CustomID string`

      Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

      Must be unique for each request within the Message Batch.

      maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,64}$

    - `Params MessageBatchNewParamsRequestParams`

      Messages API creation parameters for the individual request.

      See the [Messages API reference](https://platform.claude.com/docs/en/api/messages) for full documentation on available parameters.

      - `MaxTokens int64`

        The maximum number of tokens to generate before stopping.

        Note that our models may stop _before_ reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

        Set to `0` to populate the [prompt cache](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#pre-warming-the-cache) without generating a response.

        Different models have different maximum values for this parameter.  See [models](https://platform.claude.com/docs/en/about-claude/models/overview) for details.

        minimum: 0

      - `Messages []MessageParamResp`

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

        - `Content []ContentBlockParamUnionResp`

          - `[]ContentBlockParamUnionResp`

            - `type TextBlockParamResp struct{…}`

              - `Text string`

                minLength: 1

              - `Type Text`

              - `CacheControl CacheControlEphemeral Optional`

                Create a cache control breakpoint at this content block.

                - `Type Ephemeral`

                - `TTL CacheControlEphemeralTTL Optional`

                  The time-to-live for the cache control breakpoint.

                  This may be one the following values:

                  - `5m`: 5 minutes
                  - `1h`: 1 hour

                  Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

                  - `const CacheControlEphemeralTTLTTL5m CacheControlEphemeralTTL = "5m"`

                  - `const CacheControlEphemeralTTLTTL1h CacheControlEphemeralTTL = "1h"`

              - `Citations []TextCitationParamUnionResp Optional`

                - `type CitationCharLocationParamResp struct{…}`

                  - `CitedText string`

                  - `DocumentIndex int64`

                    minimum: 0

                  - `DocumentTitle string`

                    maxLength: 500, minLength: 1

                  - `EndCharIndex int64`

                  - `StartCharIndex int64`

                    minimum: 0

                  - `Type CharLocation`

                - `type CitationPageLocationParamResp struct{…}`

                  - `CitedText string`

                  - `DocumentIndex int64`

                    minimum: 0

                  - `DocumentTitle string`

                    maxLength: 500, minLength: 1

                  - `EndPageNumber int64`

                  - `StartPageNumber int64`

                    minimum: 1

                  - `Type PageLocation`

                - `type CitationContentBlockLocationParamResp struct{…}`

                  - `CitedText string`

                    The full text of the cited block range, concatenated.

                    Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

                  - `DocumentIndex int64`

                    minimum: 0

                  - `DocumentTitle string`

                    maxLength: 500, minLength: 1

                  - `EndBlockIndex int64`

                    Exclusive 0-based end index of the cited block range in the source's `content` array.

                    Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

                  - `StartBlockIndex int64`

                    0-based index of the first cited block in the source's `content` array.

                    minimum: 0

                  - `Type ContentBlockLocation`

                - `type CitationWebSearchResultLocationParamResp struct{…}`

                  - `CitedText string`

                  - `EncryptedIndex string`

                  - `Title string`

                    maxLength: 512, minLength: 1

                  - `Type WebSearchResultLocation`

                  - `URL string`

                    minLength: 1

                - `type CitationSearchResultLocationParamResp struct{…}`

                  - `CitedText string`

                    The full text of the cited block range, concatenated.

                    Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

                  - `EndBlockIndex int64`

                    Exclusive 0-based end index of the cited block range in the source's `content` array.

                    Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

                  - `SearchResultIndex int64`

                    0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

                    Counted separately from `document_index`; server-side web search results are not included in this count.

                    minimum: 0

                  - `Source string`

                  - `StartBlockIndex int64`

                    0-based index of the first cited block in the source's `content` array.

                    minimum: 0

                  - `Title string`

                  - `Type SearchResultLocation`

            - `type ImageBlockParamResp struct{…}`

              - `Source ImageBlockParamSourceUnionResp`

                - `type Base64ImageSource struct{…}`

                  - `Data string`

                    format: byte

                  - `MediaType Base64ImageSourceMediaType`

                    - `const Base64ImageSourceMediaTypeImageJPEG Base64ImageSourceMediaType = "image/jpeg"`

                    - `const Base64ImageSourceMediaTypeImagePNG Base64ImageSourceMediaType = "image/png"`

                    - `const Base64ImageSourceMediaTypeImageGIF Base64ImageSourceMediaType = "image/gif"`

                    - `const Base64ImageSourceMediaTypeImageWebP Base64ImageSourceMediaType = "image/webp"`

                  - `Type Base64`

                - `type URLImageSource struct{…}`

                  - `Type URL`

                  - `URL string`

                - `type FileImageSource struct{…}`

                  - `FileID string`

                  - `Type File`

              - `Type Image`

              - `CacheControl CacheControlEphemeral Optional`

                Create a cache control breakpoint at this content block.

              - `Transformations ImageTransformationsParamResp Optional`

                Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

                - `OversizedImage ImageTransformationsParamOversizedImage Optional`

                  What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

                  - `const ImageTransformationsParamOversizedImageDownsize ImageTransformationsParamOversizedImage = "downsize"`

                  - `const ImageTransformationsParamOversizedImageError ImageTransformationsParamOversizedImage = "error"`

            - `type DocumentBlockParamResp struct{…}`

              - `Source DocumentBlockParamSourceUnionResp`

                - `type Base64PDFSource struct{…}`

                  - `Data string`

                    format: byte

                  - `MediaType ApplicationPDF`

                  - `Type Base64`

                - `type PlainTextSource struct{…}`

                  - `Data string`

                  - `MediaType TextPlain`

                  - `Type Text`

                - `type ContentBlockSource struct{…}`

                  - `Content ContentBlockSourceContentUnion`

                    - `string`

                    - `[]ContentBlockSourceContentItemUnion`

                      - `type TextBlockParamResp struct{…}`

                      - `type ImageBlockParamResp struct{…}`

                  - `Type Content`

                - `type URLPDFSource struct{…}`

                  - `Type URL`

                  - `URL string`

                - `type FileDocumentSource struct{…}`

                  - `FileID string`

                  - `Type File`

              - `Type Document`

              - `CacheControl CacheControlEphemeral Optional`

                Create a cache control breakpoint at this content block.

              - `Citations CitationsConfigParamResp Optional`

                - `Enabled bool Optional`

              - `Context string Optional`

                minLength: 1

              - `Title string Optional`

                maxLength: 500, minLength: 1

            - `type SearchResultBlockParamResp struct{…}`

              - `Content []TextBlockParamResp`

                - `Text string`

                  minLength: 1

                - `Type Text`

                - `CacheControl CacheControlEphemeral Optional`

                  Create a cache control breakpoint at this content block.

                - `Citations []TextCitationParamUnionResp Optional`

              - `Source string`

              - `Title string`

              - `Type SearchResult`

              - `CacheControl CacheControlEphemeral Optional`

                Create a cache control breakpoint at this content block.

              - `Citations CitationsConfigParamResp Optional`

            - `type ThinkingBlockParamResp struct{…}`

              - `Signature string`

                The `signature` value of this thinking block, exactly as returned by the API in a previous response. Used to verify that the block was generated by Claude.

                Thinking blocks must be passed back unmodified and in their original order; a modified block results in a 400 `invalid_request_error`.

              - `Thinking string`

                The `thinking` text of this block as returned by the API.

              - `Type Thinking`

            - `type RedactedThinkingBlockParamResp struct{…}`

              - `Data string`

                The `data` value of this redacted thinking block, exactly as returned by the API in a previous response. Opaque and encrypted; pass it back unchanged.

              - `Type RedactedThinking`

            - `type ToolUseBlockParamResp struct{…}`

              - `ID string`

                pattern: ^[a-zA-Z0-9_-]+$

              - `Input map[string, any]`

              - `Name string`

                maxLength: 200, minLength: 1

              - `Type ToolUse`

              - `CacheControl CacheControlEphemeral Optional`

                Create a cache control breakpoint at this content block.

              - `Caller ToolUseBlockParamCallerUnionResp Optional`

                Tool invocation directly from the model.

                - `type DirectCaller struct{…}`

                  Tool invocation directly from the model.

                  - `Type Direct`

                - `type ServerToolCaller struct{…}`

                  Tool invocation generated by a server-side tool.

                  - `ToolID string`

                    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

                  - `Type CodeExecution20250825`

                - `type ServerToolCaller20260120 struct{…}`

                  - `ToolID string`

                    pattern: ^srvtoolu_[a-zA-Z0-9_]+$

                  - `Type CodeExecution20260120`

              - `ToolsetName string Optional`

                For a toolset member tool_use, the toolset family this member belongs to.

                maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

            - `type ToolResultBlockParamResp struct{…}`

              - `ToolUseID string`

                pattern: ^[a-zA-Z0-9_-]+$

              - `Type ToolResult`

              - `CacheControl CacheControlEphemeral Optional`

                Create a cache control breakpoint at this content block.

              - `Content []ToolResultBlockParamContentUnionResp Optional`

                - `[]ToolResultBlockParamContentUnionResp`

                  - `type TextBlockParamResp struct{…}`

                  - `type ImageBlockParamResp struct{…}`

                  - `type SearchResultBlockParamResp struct{…}`

                  - `type DocumentBlockParamResp struct{…}`

                  - `type ToolReferenceBlockParamResp struct{…}`

                    Tool reference block that can be included in tool_result content.

                    - `ToolName string`

                      maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

                    - `Type ToolReference`

                    - `CacheControl CacheControlEphemeral Optional`

                      Create a cache control breakpoint at this content block.

                  - `type BrowserStateBlockParamResp struct{…}`

                    The caller's browser state after a browser toolset member call —
                    the full inventory of open tabs, which tab is active, and any side
                    effects (tabs opened, download state changes) the call produced.

                    At most one per `tool_result`, only on a non-error result answering a
                    browser toolset member `tool_use`. The server renders the
                    model-visible text from it; the model never sees the raw fields.

                    - `Tabs []BrowserStateTabEntry`

                      All tabs open in the browser after this call — the full inventory, not a delta. May be empty. Whenever non-empty, exactly one entry carries `active: true`.

                      maxItems: 100

                      - `TabID string`

                        The caller-assigned identifier for this tab, unique within the inventory.

                        maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                      - `Title string`

                        The title of the page the tab is showing. May be empty.

                        maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                      - `URL string`

                        The URL of the page the tab is showing. May be empty.

                        maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                      - `Active bool Optional`

                        Whether this tab is the active tab after this call. Whenever `tabs` is non-empty, exactly one entry is marked `active: true`.

                    - `Type BrowserState`

                    - `CacheControl CacheControlEphemeral Optional`

                      Create a cache control breakpoint at this content block.

                    - `StateChanges []BrowserStateChangeUnion Optional`

                      Tabs opened and download state changes during this call. "Nothing to report" is expressed by omitting the field, never by an empty list.

                      maxItems: 200, minItems: 1

                      - `type BrowserStateChangeTabOpened struct{…}`

                        A tab this call's execution opened that remains open at its end —
                        the creation delta of the `tabs` inventory, not an event log.

                        Carries only the `tab_id`; the tab's `title` and `url` live on its
                        `tabs` entry, which must include the same `tab_id`. A tab opened
                        during a failed call gets no deferred `tab_opened`; it simply appears
                        in the next result's `tabs` inventory.

                        - `TabID string`

                          The `tab_id` of the opened tab, present in `tabs`.

                          maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                        - `Type TabOpened`

                      - `type BrowserStateChangeDownloadStarted struct{…}`

                        A file download that started during this call.

                        - `DownloadID string`

                          The caller-assigned identifier for this download, stable across the state changes reporting it.

                          maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                        - `Type DownloadStarted`

                        - `URL string`

                          The final post-redirect URL the download was served from.

                          maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                      - `type BrowserStateChangeDownloadCompleted struct{…}`

                        A file download that finished during this call, reported with the
                        same `download_id` as its `download_started` — or without a prior
                        `download_started`, when the download finished during the call that
                        started it (at most one state change per `download_id` per result).

                        - `DownloadID string`

                          The caller-assigned identifier for this download, stable across the state changes reporting it.

                          maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                        - `Type DownloadCompleted`

                        - `URL string`

                          The final post-redirect URL the download was served from.

                          maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                        - `Path string Optional`

                          Where the executor saved the file, on the executor's filesystem. Only included when another tool in the same environment can read the file at that path.

                          pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

                        - `SizeBytes int64 Optional`

                          The completed download's size.

                          minimum: 0

                      - `type BrowserStateChangeDownloadFailed struct{…}`

                        A file download that failed — or was cancelled — during this call.

                        - `DownloadID string`

                          The caller-assigned identifier for this download, stable across the state changes reporting it.

                          maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                        - `Type DownloadFailed`

                        - `URL string`

                          The final post-redirect URL the download was served from.

                          maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                        - `Error string Optional`

                          The failure or cancellation detail, when known.

                          pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$, maxLength: 4096

              - `IsError bool Optional`

              - `ToolsetName string Optional`

                For a toolset member tool_result, the toolset family of the paired tool_use.

                maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

            - `type ServerToolUseBlockParamResp struct{…}`

              - `ID string`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `Input map[string, any]`

              - `Name ServerToolUseBlockParamName`

                - `const ServerToolUseBlockParamNameWebSearch ServerToolUseBlockParamName = "web_search"`

                - `const ServerToolUseBlockParamNameWebFetch ServerToolUseBlockParamName = "web_fetch"`

                - `const ServerToolUseBlockParamNameCodeExecution ServerToolUseBlockParamName = "code_execution"`

                - `const ServerToolUseBlockParamNameBashCodeExecution ServerToolUseBlockParamName = "bash_code_execution"`

                - `const ServerToolUseBlockParamNameTextEditorCodeExecution ServerToolUseBlockParamName = "text_editor_code_execution"`

                - `const ServerToolUseBlockParamNameToolSearchToolRegex ServerToolUseBlockParamName = "tool_search_tool_regex"`

                - `const ServerToolUseBlockParamNameToolSearchToolBm25 ServerToolUseBlockParamName = "tool_search_tool_bm25"`

              - `Type ServerToolUse`

              - `CacheControl CacheControlEphemeral Optional`

                Create a cache control breakpoint at this content block.

              - `Caller ServerToolUseBlockParamCallerUnionResp Optional`

                Tool invocation directly from the model.

                - `type DirectCaller struct{…}`

                  Tool invocation directly from the model.

                - `type ServerToolCaller struct{…}`

                  Tool invocation generated by a server-side tool.

                - `type ServerToolCaller20260120 struct{…}`

            - `type WebSearchToolResultBlockParamResp struct{…}`

              - `Content WebSearchToolResultBlockParamContentUnionResp`

                - `[]WebSearchResultBlockParamResp`

                  - `EncryptedContent string`

                  - `Title string`

                  - `Type WebSearchResult`

                  - `URL string`

                  - `PageAge string Optional`

                - `type WebSearchToolRequestError struct{…}`

                  - `ErrorCode WebSearchToolResultErrorCode`

                    - `const WebSearchToolResultErrorCodeInvalidToolInput WebSearchToolResultErrorCode = "invalid_tool_input"`

                    - `const WebSearchToolResultErrorCodeUnavailable WebSearchToolResultErrorCode = "unavailable"`

                    - `const WebSearchToolResultErrorCodeMaxUsesExceeded WebSearchToolResultErrorCode = "max_uses_exceeded"`

                    - `const WebSearchToolResultErrorCodeTooManyRequests WebSearchToolResultErrorCode = "too_many_requests"`

                    - `const WebSearchToolResultErrorCodeQueryTooLong WebSearchToolResultErrorCode = "query_too_long"`

                    - `const WebSearchToolResultErrorCodeRequestTooLarge WebSearchToolResultErrorCode = "request_too_large"`

                  - `Type WebSearchToolResultError`

              - `ToolUseID string`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `Type WebSearchToolResult`

              - `CacheControl CacheControlEphemeral Optional`

                Create a cache control breakpoint at this content block.

              - `Caller WebSearchToolResultBlockParamCallerUnionResp Optional`

                Tool invocation directly from the model.

                - `type DirectCaller struct{…}`

                  Tool invocation directly from the model.

                - `type ServerToolCaller struct{…}`

                  Tool invocation generated by a server-side tool.

                - `type ServerToolCaller20260120 struct{…}`

            - `type WebFetchToolResultBlockParamResp struct{…}`

              - `Content WebFetchToolResultBlockParamContentUnionResp`

                - `type WebFetchToolResultErrorBlockParamResp struct{…}`

                  - `ErrorCode WebFetchToolResultErrorCode`

                    - `const WebFetchToolResultErrorCodeInvalidToolInput WebFetchToolResultErrorCode = "invalid_tool_input"`

                    - `const WebFetchToolResultErrorCodeURLTooLong WebFetchToolResultErrorCode = "url_too_long"`

                    - `const WebFetchToolResultErrorCodeURLNotAllowed WebFetchToolResultErrorCode = "url_not_allowed"`

                    - `const WebFetchToolResultErrorCodeURLNotInPriorContext WebFetchToolResultErrorCode = "url_not_in_prior_context"`

                    - `const WebFetchToolResultErrorCodeURLNotAccessible WebFetchToolResultErrorCode = "url_not_accessible"`

                    - `const WebFetchToolResultErrorCodeUnsupportedContentType WebFetchToolResultErrorCode = "unsupported_content_type"`

                    - `const WebFetchToolResultErrorCodeTooManyRequests WebFetchToolResultErrorCode = "too_many_requests"`

                    - `const WebFetchToolResultErrorCodeMaxUsesExceeded WebFetchToolResultErrorCode = "max_uses_exceeded"`

                    - `const WebFetchToolResultErrorCodeUnavailable WebFetchToolResultErrorCode = "unavailable"`

                  - `Type WebFetchToolResultError`

                - `type WebFetchBlockParamResp struct{…}`

                  - `Content DocumentBlockParamResp`

                  - `Type WebFetchResult`

                  - `URL string`

                    Fetched content URL

                  - `RetrievedAt string Optional`

                    ISO 8601 timestamp when the content was retrieved

              - `ToolUseID string`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `Type WebFetchToolResult`

              - `CacheControl CacheControlEphemeral Optional`

                Create a cache control breakpoint at this content block.

              - `Caller WebFetchToolResultBlockParamCallerUnionResp Optional`

                Tool invocation directly from the model.

                - `type DirectCaller struct{…}`

                  Tool invocation directly from the model.

                - `type ServerToolCaller struct{…}`

                  Tool invocation generated by a server-side tool.

                - `type ServerToolCaller20260120 struct{…}`

            - `type CodeExecutionToolResultBlockParamResp struct{…}`

              - `Content CodeExecutionToolResultBlockParamContentUnionResp`

                Code execution result with encrypted stdout for PFC + web_search results.

                - `type CodeExecutionToolResultErrorParamResp struct{…}`

                  - `ErrorCode CodeExecutionToolResultErrorCode`

                    - `const CodeExecutionToolResultErrorCodeInvalidToolInput CodeExecutionToolResultErrorCode = "invalid_tool_input"`

                    - `const CodeExecutionToolResultErrorCodeUnavailable CodeExecutionToolResultErrorCode = "unavailable"`

                    - `const CodeExecutionToolResultErrorCodeTooManyRequests CodeExecutionToolResultErrorCode = "too_many_requests"`

                    - `const CodeExecutionToolResultErrorCodeExecutionTimeExceeded CodeExecutionToolResultErrorCode = "execution_time_exceeded"`

                  - `Type CodeExecutionToolResultError`

                - `type CodeExecutionResultBlockParamResp struct{…}`

                  - `Content []CodeExecutionOutputBlockParamResp`

                    - `FileID string`

                    - `Type CodeExecutionOutput`

                  - `ReturnCode int64`

                  - `Stderr string`

                  - `Stdout string`

                  - `Type CodeExecutionResult`

                - `type EncryptedCodeExecutionResultBlockParamResp struct{…}`

                  Code execution result with encrypted stdout for PFC + web_search results.

                  - `Content []CodeExecutionOutputBlockParamResp`

                    - `FileID string`

                    - `Type CodeExecutionOutput`

                  - `EncryptedStdout string`

                  - `ReturnCode int64`

                  - `Stderr string`

                  - `Type EncryptedCodeExecutionResult`

              - `ToolUseID string`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `Type CodeExecutionToolResult`

              - `CacheControl CacheControlEphemeral Optional`

                Create a cache control breakpoint at this content block.

            - `type BashCodeExecutionToolResultBlockParamResp struct{…}`

              - `Content BashCodeExecutionToolResultBlockParamContentUnionResp`

                - `type BashCodeExecutionToolResultErrorParamResp struct{…}`

                  - `ErrorCode BashCodeExecutionToolResultErrorCode`

                    - `const BashCodeExecutionToolResultErrorCodeInvalidToolInput BashCodeExecutionToolResultErrorCode = "invalid_tool_input"`

                    - `const BashCodeExecutionToolResultErrorCodeUnavailable BashCodeExecutionToolResultErrorCode = "unavailable"`

                    - `const BashCodeExecutionToolResultErrorCodeTooManyRequests BashCodeExecutionToolResultErrorCode = "too_many_requests"`

                    - `const BashCodeExecutionToolResultErrorCodeExecutionTimeExceeded BashCodeExecutionToolResultErrorCode = "execution_time_exceeded"`

                    - `const BashCodeExecutionToolResultErrorCodeOutputFileTooLarge BashCodeExecutionToolResultErrorCode = "output_file_too_large"`

                  - `Type BashCodeExecutionToolResultError`

                - `type BashCodeExecutionResultBlockParamResp struct{…}`

                  - `Content []BashCodeExecutionOutputBlockParamResp`

                    - `FileID string`

                    - `Type BashCodeExecutionOutput`

                  - `ReturnCode int64`

                  - `Stderr string`

                  - `Stdout string`

                  - `Type BashCodeExecutionResult`

              - `ToolUseID string`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `Type BashCodeExecutionToolResult`

              - `CacheControl CacheControlEphemeral Optional`

                Create a cache control breakpoint at this content block.

            - `type TextEditorCodeExecutionToolResultBlockParamResp struct{…}`

              - `Content TextEditorCodeExecutionToolResultBlockParamContentUnionResp`

                - `type TextEditorCodeExecutionToolResultErrorParamResp struct{…}`

                  - `ErrorCode TextEditorCodeExecutionToolResultErrorCode`

                    - `const TextEditorCodeExecutionToolResultErrorCodeInvalidToolInput TextEditorCodeExecutionToolResultErrorCode = "invalid_tool_input"`

                    - `const TextEditorCodeExecutionToolResultErrorCodeUnavailable TextEditorCodeExecutionToolResultErrorCode = "unavailable"`

                    - `const TextEditorCodeExecutionToolResultErrorCodeTooManyRequests TextEditorCodeExecutionToolResultErrorCode = "too_many_requests"`

                    - `const TextEditorCodeExecutionToolResultErrorCodeExecutionTimeExceeded TextEditorCodeExecutionToolResultErrorCode = "execution_time_exceeded"`

                    - `const TextEditorCodeExecutionToolResultErrorCodeFileNotFound TextEditorCodeExecutionToolResultErrorCode = "file_not_found"`

                  - `Type TextEditorCodeExecutionToolResultError`

                  - `ErrorMessage string Optional`

                - `type TextEditorCodeExecutionViewResultBlockParamResp struct{…}`

                  - `Content string`

                  - `FileType TextEditorCodeExecutionViewResultBlockParamFileType`

                    - `const TextEditorCodeExecutionViewResultBlockParamFileTypeText TextEditorCodeExecutionViewResultBlockParamFileType = "text"`

                    - `const TextEditorCodeExecutionViewResultBlockParamFileTypeImage TextEditorCodeExecutionViewResultBlockParamFileType = "image"`

                    - `const TextEditorCodeExecutionViewResultBlockParamFileTypePDF TextEditorCodeExecutionViewResultBlockParamFileType = "pdf"`

                  - `Type TextEditorCodeExecutionViewResult`

                  - `NumLines int64 Optional`

                  - `StartLine int64 Optional`

                  - `TotalLines int64 Optional`

                - `type TextEditorCodeExecutionCreateResultBlockParamResp struct{…}`

                  - `IsFileUpdate bool`

                  - `Type TextEditorCodeExecutionCreateResult`

                - `type TextEditorCodeExecutionStrReplaceResultBlockParamResp struct{…}`

                  - `Type TextEditorCodeExecutionStrReplaceResult`

                  - `Lines []string Optional`

                  - `NewLines int64 Optional`

                  - `NewStart int64 Optional`

                  - `OldLines int64 Optional`

                  - `OldStart int64 Optional`

              - `ToolUseID string`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `Type TextEditorCodeExecutionToolResult`

              - `CacheControl CacheControlEphemeral Optional`

                Create a cache control breakpoint at this content block.

            - `type ToolSearchToolResultBlockParamResp struct{…}`

              - `Content ToolSearchToolResultBlockParamContentUnionResp`

                - `type ToolSearchToolResultErrorParamResp struct{…}`

                  - `ErrorCode ToolSearchToolResultErrorCode`

                    - `const ToolSearchToolResultErrorCodeInvalidToolInput ToolSearchToolResultErrorCode = "invalid_tool_input"`

                    - `const ToolSearchToolResultErrorCodeUnavailable ToolSearchToolResultErrorCode = "unavailable"`

                    - `const ToolSearchToolResultErrorCodeTooManyRequests ToolSearchToolResultErrorCode = "too_many_requests"`

                    - `const ToolSearchToolResultErrorCodeExecutionTimeExceeded ToolSearchToolResultErrorCode = "execution_time_exceeded"`

                  - `Type ToolSearchToolResultError`

                  - `ErrorMessage string Optional`

                - `type ToolSearchToolSearchResultBlockParamResp struct{…}`

                  - `ToolReferences []ToolReferenceBlockParamResp`

                    - `ToolName string`

                      maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

                    - `Type ToolReference`

                    - `CacheControl CacheControlEphemeral Optional`

                      Create a cache control breakpoint at this content block.

                  - `Type ToolSearchToolSearchResult`

              - `ToolUseID string`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `Type ToolSearchToolResult`

              - `CacheControl CacheControlEphemeral Optional`

                Create a cache control breakpoint at this content block.

            - `type ContainerUploadBlockParamResp struct{…}`

              A content block that represents a file to be uploaded to the container
              Files uploaded via this block will be available in the container's input directory.

              - `FileID string`

              - `Type ContainerUpload`

              - `CacheControl CacheControlEphemeral Optional`

                Create a cache control breakpoint at this content block.

        - `Role MessageParamRole`

          - `const MessageParamRoleUser MessageParamRole = "user"`

          - `const MessageParamRoleAssistant MessageParamRole = "assistant"`

          - `const MessageParamRoleSystem MessageParamRole = "system"`

      - `Model Model`

        The model that will complete your prompt.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `type Model string`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `const ModelClaudeSonnet5 Model = "claude-sonnet-5"`

            High-performance model for coding and agents

          - `const ModelClaudeFable5 Model = "claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `const ModelClaudeMythos5 Model = "claude-mythos-5"`

            Most capable model for cybersecurity and biology research

          - `const ModelClaudeOpus5 Model = "claude-opus-5"`

            Powerful intelligence for long-running agents and coding

          - `const ModelClaudeOpus4_8 Model = "claude-opus-4-8"`

            Powerful intelligence for long-running agents and coding

          - `const ModelClaudeOpus4_7 Model = "claude-opus-4-7"`

            Powerful intelligence for long-running agents and coding

          - `const ModelClaudeMythosPreview Model = "claude-mythos-preview"`

            New class of intelligence, strongest in coding and cybersecurity

          - `const ModelClaudeOpus4_6 Model = "claude-opus-4-6"`

            Powerful intelligence for long-running agents and coding

          - `const ModelClaudeSonnet4_6 Model = "claude-sonnet-4-6"`

            Best combination of speed and intelligence

          - `const ModelClaudeHaiku4_5 Model = "claude-haiku-4-5"`

            Fastest model with near-frontier intelligence

          - `const ModelClaudeHaiku4_5_20251001 Model = "claude-haiku-4-5-20251001"`

            Fastest model with near-frontier intelligence

          - `const ModelClaudeOpus4_5 Model = "claude-opus-4-5"`

            Powerful intelligence for long-running agents and coding

          - `const ModelClaudeOpus4_5_20251101 Model = "claude-opus-4-5-20251101"`

            Powerful intelligence for long-running agents and coding

          - `const ModelClaudeSonnet4_5 Model = "claude-sonnet-4-5"`

            High-performance model for agents and coding

          - `const ModelClaudeSonnet4_5_20250929 Model = "claude-sonnet-4-5-20250929"`

            High-performance model for agents and coding

        - `string`

      - `CacheControl CacheControlEphemeral Optional`

        Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

      - `Container MessageCreateParamsContainerUnionResp Optional`

        Container identifier for reuse across requests.

        - `type ContainerParamsResp struct{…}`

          Container parameters with skills to be loaded.

          - `ID string Optional`

            Container id

          - `Skills []SkillParamsResp Optional`

            List of skills to load in the container

            maxItems: 20

            - `SkillID string`

              Skill ID

              maxLength: 64, minLength: 1

            - `Type SkillParamsType`

              Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

              - `const SkillParamsTypeAnthropic SkillParamsType = "anthropic"`

              - `const SkillParamsTypeCustom SkillParamsType = "custom"`

            - `Version string Optional`

              Skill version or 'latest' for most recent version

              maxLength: 64, minLength: 1

        - `string`

      - `InferenceGeo string Optional`

        Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

      - `Metadata Metadata Optional`

        An object describing metadata about the request.

        - `UserID string Optional`

          An external identifier for the user who is associated with the request.

          This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

          maxLength: 512

      - `OutputConfig OutputConfig Optional`

        Configuration options for the model's output, such as the output format.

        - `Effort OutputConfigEffort Optional`

          All possible effort levels.

          - `const OutputConfigEffortLow OutputConfigEffort = "low"`

          - `const OutputConfigEffortMedium OutputConfigEffort = "medium"`

          - `const OutputConfigEffortHigh OutputConfigEffort = "high"`

          - `const OutputConfigEffortXhigh OutputConfigEffort = "xhigh"`

          - `const OutputConfigEffortMax OutputConfigEffort = "max"`

        - `Format JSONOutputFormat Optional`

          A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

          - `Schema map[string, any]`

            The JSON schema of the format

          - `Type JSONSchema`

      - `ServiceTier string Optional`

        Determines whether to use priority capacity (if available) or standard capacity for this request.

        Anthropic offers different levels of service for your API requests. See [service-tiers](https://platform.claude.com/docs/en/api/service-tiers) for details.

        - `const MessageBatchNewParamsRequestParamsServiceTierAuto MessageBatchNewParamsRequestParamsServiceTier = "auto"`

        - `const MessageBatchNewParamsRequestParamsServiceTierStandardOnly MessageBatchNewParamsRequestParamsServiceTier = "standard_only"`

      - `StopSequences []string Optional`

        Custom text sequences that will cause the model to stop generating.

        Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

        If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

      - `Stream bool Optional`

        Whether to incrementally stream the response using server-sent events.

        See [streaming](https://platform.claude.com/docs/en/build-with-claude/streaming) for details.

      - `System []TextBlockParamResp Optional`

        System prompt.

        A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role).

        - `[]TextBlockParam`

          - `Text string`

            minLength: 1

          - `Type Text`

          - `CacheControl CacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `Citations []TextCitationParamUnionResp Optional`

      - `Thinking ThinkingConfigParamUnionResp Optional`

        Configuration for enabling Claude's extended thinking.

        When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

        See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

        - `type ThinkingConfigEnabled struct{…}`

          - `BudgetTokens int64`

            Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

            Must be ≥1024 and less than `max_tokens`.

            See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

            minimum: 1024

          - `Type Enabled`

          - `Display ThinkingConfigEnabledDisplay Optional`

            Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

            - `const ThinkingConfigEnabledDisplaySummarized ThinkingConfigEnabledDisplay = "summarized"`

            - `const ThinkingConfigEnabledDisplayOmitted ThinkingConfigEnabledDisplay = "omitted"`

        - `type ThinkingConfigDisabled struct{…}`

          - `Type Disabled`

        - `type ThinkingConfigAdaptive struct{…}`

          - `Type Adaptive`

          - `Display ThinkingConfigAdaptiveDisplay Optional`

            Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

            - `const ThinkingConfigAdaptiveDisplaySummarized ThinkingConfigAdaptiveDisplay = "summarized"`

            - `const ThinkingConfigAdaptiveDisplayOmitted ThinkingConfigAdaptiveDisplay = "omitted"`

      - `ToolChoice ToolChoiceUnion Optional`

        How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

        - `type ToolChoiceAuto struct{…}`

          The model will automatically decide whether to use tools.

          - `Type Auto`

          - `DisableParallelToolUse bool Optional`

            Whether to disable parallel tool use.

            Defaults to `false`. If set to `true`, the model will output at most one tool use.

        - `type ToolChoiceAny struct{…}`

          The model will use any available tools.

          - `Type Any`

          - `DisableParallelToolUse bool Optional`

            Whether to disable parallel tool use.

            Defaults to `false`. If set to `true`, the model will output exactly one tool use.

        - `type ToolChoiceTool struct{…}`

          The model will use the specified tool with `tool_choice.name`.

          - `Name string`

            The name of the tool to use.

          - `Type Tool`

          - `DisableParallelToolUse bool Optional`

            Whether to disable parallel tool use.

            Defaults to `false`. If set to `true`, the model will output exactly one tool use.

        - `type ToolChoiceNone struct{…}`

          The model will not be allowed to use tools.

          - `Type None`

      - `Tools []ToolUnion Optional`

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

        - `type Tool struct{…}`

          - `InputSchema ToolInputSchema`

            [JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

            This defines the shape of the `input` that your tool accepts and that the model will produce.

            - `Type Object`

            - `Properties map[string, any] Optional`

            - `Required []string Optional`

          - `Name string`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

            maxLength: 128, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,128}$

          - `AllowedCallers []string Optional`

            - `const ToolAllowedCallerDirect ToolAllowedCaller = "direct"`

            - `const ToolAllowedCallerCodeExecution20250825 ToolAllowedCaller = "code_execution_20250825"`

            - `const ToolAllowedCallerCodeExecution20260120 ToolAllowedCaller = "code_execution_20260120"`

            - `const ToolAllowedCallerCodeExecution20260521 ToolAllowedCaller = "code_execution_20260521"`

          - `CacheControl CacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Description string Optional`

            Description of what this tool does.

            Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

          - `EagerInputStreaming bool Optional`

            Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

          - `InputExamples []map[string, any] Optional`

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

          - `Type ToolType Optional`

        - `type ToolBash20250124 struct{…}`

          - `Name Bash`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type Bash20250124`

          - `AllowedCallers []string Optional`

            - `const ToolBash20250124AllowedCallerDirect ToolBash20250124AllowedCaller = "direct"`

            - `const ToolBash20250124AllowedCallerCodeExecution20250825 ToolBash20250124AllowedCaller = "code_execution_20250825"`

            - `const ToolBash20250124AllowedCallerCodeExecution20260120 ToolBash20250124AllowedCaller = "code_execution_20260120"`

            - `const ToolBash20250124AllowedCallerCodeExecution20260521 ToolBash20250124AllowedCaller = "code_execution_20260521"`

          - `CacheControl CacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `InputExamples []map[string, any] Optional`

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

        - `type CodeExecutionTool20250522 struct{…}`

          - `Name CodeExecution`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type CodeExecution20250522`

          - `AllowedCallers []string Optional`

            - `const CodeExecutionTool20250522AllowedCallerDirect CodeExecutionTool20250522AllowedCaller = "direct"`

            - `const CodeExecutionTool20250522AllowedCallerCodeExecution20250825 CodeExecutionTool20250522AllowedCaller = "code_execution_20250825"`

            - `const CodeExecutionTool20250522AllowedCallerCodeExecution20260120 CodeExecutionTool20250522AllowedCaller = "code_execution_20260120"`

            - `const CodeExecutionTool20250522AllowedCallerCodeExecution20260521 CodeExecutionTool20250522AllowedCaller = "code_execution_20260521"`

          - `CacheControl CacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

        - `type CodeExecutionTool20250825 struct{…}`

          - `Name CodeExecution`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type CodeExecution20250825`

          - `AllowedCallers []string Optional`

            - `const CodeExecutionTool20250825AllowedCallerDirect CodeExecutionTool20250825AllowedCaller = "direct"`

            - `const CodeExecutionTool20250825AllowedCallerCodeExecution20250825 CodeExecutionTool20250825AllowedCaller = "code_execution_20250825"`

            - `const CodeExecutionTool20250825AllowedCallerCodeExecution20260120 CodeExecutionTool20250825AllowedCaller = "code_execution_20260120"`

            - `const CodeExecutionTool20250825AllowedCallerCodeExecution20260521 CodeExecutionTool20250825AllowedCaller = "code_execution_20260521"`

          - `CacheControl CacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

        - `type CodeExecutionTool20260120 struct{…}`

          Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

          - `Name CodeExecution`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type CodeExecution20260120`

          - `AllowedCallers []string Optional`

            - `const CodeExecutionTool20260120AllowedCallerDirect CodeExecutionTool20260120AllowedCaller = "direct"`

            - `const CodeExecutionTool20260120AllowedCallerCodeExecution20250825 CodeExecutionTool20260120AllowedCaller = "code_execution_20250825"`

            - `const CodeExecutionTool20260120AllowedCallerCodeExecution20260120 CodeExecutionTool20260120AllowedCaller = "code_execution_20260120"`

            - `const CodeExecutionTool20260120AllowedCallerCodeExecution20260521 CodeExecutionTool20260120AllowedCaller = "code_execution_20260521"`

          - `CacheControl CacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

        - `type CodeExecutionTool20260521 struct{…}`

          Code execution tool with REPL state persistence.

          - `Name CodeExecution`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type CodeExecution20260521`

          - `AllowedCallers []string Optional`

            - `const CodeExecutionTool20260521AllowedCallerDirect CodeExecutionTool20260521AllowedCaller = "direct"`

            - `const CodeExecutionTool20260521AllowedCallerCodeExecution20250825 CodeExecutionTool20260521AllowedCaller = "code_execution_20250825"`

            - `const CodeExecutionTool20260521AllowedCallerCodeExecution20260120 CodeExecutionTool20260521AllowedCaller = "code_execution_20260120"`

            - `const CodeExecutionTool20260521AllowedCallerCodeExecution20260521 CodeExecutionTool20260521AllowedCaller = "code_execution_20260521"`

          - `CacheControl CacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

        - `type BrowserToolset20260801 struct{…}`

          The browser toolset: a single `tools[]` entry (carrying no
          `name`) that declares the browser tool family. The model is served
          the family's tool with any members disabled via `configs` removed
          from its schema.

          - `Type BrowserToolset20260801`

          - `AllowedCallers []string Optional`

            - `const BrowserToolset20260801AllowedCallerDirect BrowserToolset20260801AllowedCaller = "direct"`

            - `const BrowserToolset20260801AllowedCallerCodeExecution20250825 BrowserToolset20260801AllowedCaller = "code_execution_20250825"`

            - `const BrowserToolset20260801AllowedCallerCodeExecution20260120 BrowserToolset20260801AllowedCaller = "code_execution_20260120"`

            - `const BrowserToolset20260801AllowedCallerCodeExecution20260521 BrowserToolset20260801AllowedCaller = "code_execution_20260521"`

          - `CacheControl CacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `Configs BrowserToolsetConfigs Optional`

            Per-member configuration for `browser_toolset_20260801`: one
            optional field per member tool, keyed by the member name — the same
            name the member's `tool_use` blocks carry. Every member is an
            accepted key, and a member's defaults apply wherever its key is
            absent. Unknown keys are rejected: the field set is this toolset
            version's complete member set.

            - `CloseTab BrowserCloseTabConfig Optional`

              `close_tab`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `DoubleClick BrowserDoubleClickConfig Optional`

              `double_click`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `FileUpload BrowserFileUploadConfig Optional`

              `file_upload`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Find BrowserFindConfig Optional`

              `find`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `FormInput BrowserFormInputConfig Optional`

              `form_input`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `GetPageText BrowserGetPageTextConfig Optional`

              `get_page_text`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `HoldKey BrowserHoldKeyConfig Optional`

              `hold_key`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Hover BrowserHoverConfig Optional`

              `hover`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `JavascriptExec BrowserJavascriptExecConfig Optional`

              `javascript_exec`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Key BrowserKeyConfig Optional`

              `key`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `LeftClick BrowserLeftClickConfig Optional`

              `left_click`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `LeftClickDrag BrowserLeftClickDragConfig Optional`

              `left_click_drag`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `LeftMouseDown BrowserLeftMouseDownConfig Optional`

              `left_mouse_down`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `LeftMouseUp BrowserLeftMouseUpConfig Optional`

              `left_mouse_up`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `ListTabs BrowserListTabsConfig Optional`

              `list_tabs`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `MiddleClick BrowserMiddleClickConfig Optional`

              `middle_click`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `MouseMove BrowserMouseMoveConfig Optional`

              `mouse_move`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Navigate BrowserNavigateConfig Optional`

              `navigate`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `NewTab BrowserNewTabConfig Optional`

              `new_tab`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `ReadConsole BrowserReadConsoleConfig Optional`

              `read_console`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `ReadNetwork BrowserReadNetworkConfig Optional`

              `read_network`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `ReadPage BrowserReadPageConfig Optional`

              `read_page`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `RightClick BrowserRightClickConfig Optional`

              `right_click`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Screenshot BrowserScreenshotConfig Optional`

              `screenshot`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Scroll BrowserScrollConfig Optional`

              `scroll`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `ScrollTo BrowserScrollToConfig Optional`

              `scroll_to`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `SwitchTab BrowserSwitchTabConfig Optional`

              `switch_tab`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `TripleClick BrowserTripleClickConfig Optional`

              `triple_click`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Type BrowserTypeConfig Optional`

              `type`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Wait BrowserWaitConfig Optional`

              `wait`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Zoom BrowserZoomConfig Optional`

              `zoom`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `type MemoryTool20250818 struct{…}`

          - `Name Memory`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type Memory20250818`

          - `AllowedCallers []string Optional`

            - `const MemoryTool20250818AllowedCallerDirect MemoryTool20250818AllowedCaller = "direct"`

            - `const MemoryTool20250818AllowedCallerCodeExecution20250825 MemoryTool20250818AllowedCaller = "code_execution_20250825"`

            - `const MemoryTool20250818AllowedCallerCodeExecution20260120 MemoryTool20250818AllowedCaller = "code_execution_20260120"`

            - `const MemoryTool20250818AllowedCallerCodeExecution20260521 MemoryTool20250818AllowedCaller = "code_execution_20260521"`

          - `CacheControl CacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `InputExamples []map[string, any] Optional`

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

        - `type ComputerToolset20260801 struct{…}`

          The computer toolset: a single `tools[]` entry (carrying no
          `name`) that declares the computer tool family. The model is
          served the family's tool with any members disabled via `configs`
          removed from its schema. Every member is enabled by default, zoom
          included. The single-tool options `display_number` and
          `enable_zoom` are not fields of a toolset entry — it carries only
          `type`, `configs`, and `cache_control`; zoom is controlled
          via `configs.zoom.enabled`.

          - `Type ComputerToolset20260801`

          - `AllowedCallers []string Optional`

            - `const ComputerToolset20260801AllowedCallerDirect ComputerToolset20260801AllowedCaller = "direct"`

            - `const ComputerToolset20260801AllowedCallerCodeExecution20250825 ComputerToolset20260801AllowedCaller = "code_execution_20250825"`

            - `const ComputerToolset20260801AllowedCallerCodeExecution20260120 ComputerToolset20260801AllowedCaller = "code_execution_20260120"`

            - `const ComputerToolset20260801AllowedCallerCodeExecution20260521 ComputerToolset20260801AllowedCaller = "code_execution_20260521"`

          - `CacheControl CacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `Configs ComputerToolsetConfigs Optional`

            Per-member configuration for `computer_toolset_20260801`: one
            optional field per member tool, keyed by the member name — the same
            name the member's `tool_use` blocks carry. Every member is an
            accepted key, and a member's defaults apply wherever its key is
            absent. Unknown keys are rejected: the field set is this toolset
            version's complete member set.

            - `CursorPosition ComputerCursorPositionConfig Optional`

              `cursor_position`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `DoubleClick ComputerDoubleClickConfig Optional`

              `double_click`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `HoldKey ComputerHoldKeyConfig Optional`

              `hold_key`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Key ComputerKeyConfig Optional`

              `key`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `LeftClick ComputerLeftClickConfig Optional`

              `left_click`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `LeftClickDrag ComputerLeftClickDragConfig Optional`

              `left_click_drag`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `LeftMouseDown ComputerLeftMouseDownConfig Optional`

              `left_mouse_down`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `LeftMouseUp ComputerLeftMouseUpConfig Optional`

              `left_mouse_up`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `MiddleClick ComputerMiddleClickConfig Optional`

              `middle_click`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `MouseMove ComputerMouseMoveConfig Optional`

              `mouse_move`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `RightClick ComputerRightClickConfig Optional`

              `right_click`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Screenshot ComputerScreenshotConfig Optional`

              `screenshot`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Scroll ComputerScrollConfig Optional`

              `scroll`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `TripleClick ComputerTripleClickConfig Optional`

              `triple_click`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Type ComputerTypeConfig Optional`

              `type`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Wait ComputerWaitConfig Optional`

              `wait`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

            - `Zoom ComputerZoomConfig Optional`

              `zoom`'s config overrides.

              - `DeferLoading bool Optional`

                Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

              - `Enabled bool Optional`

                Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `type ToolTextEditor20250124 struct{…}`

          - `Name StrReplaceEditor`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type TextEditor20250124`

          - `AllowedCallers []string Optional`

            - `const ToolTextEditor20250124AllowedCallerDirect ToolTextEditor20250124AllowedCaller = "direct"`

            - `const ToolTextEditor20250124AllowedCallerCodeExecution20250825 ToolTextEditor20250124AllowedCaller = "code_execution_20250825"`

            - `const ToolTextEditor20250124AllowedCallerCodeExecution20260120 ToolTextEditor20250124AllowedCaller = "code_execution_20260120"`

            - `const ToolTextEditor20250124AllowedCallerCodeExecution20260521 ToolTextEditor20250124AllowedCaller = "code_execution_20260521"`

          - `CacheControl CacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `InputExamples []map[string, any] Optional`

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

        - `type ToolTextEditor20250429 struct{…}`

          - `Name StrReplaceBasedEditTool`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type TextEditor20250429`

          - `AllowedCallers []string Optional`

            - `const ToolTextEditor20250429AllowedCallerDirect ToolTextEditor20250429AllowedCaller = "direct"`

            - `const ToolTextEditor20250429AllowedCallerCodeExecution20250825 ToolTextEditor20250429AllowedCaller = "code_execution_20250825"`

            - `const ToolTextEditor20250429AllowedCallerCodeExecution20260120 ToolTextEditor20250429AllowedCaller = "code_execution_20260120"`

            - `const ToolTextEditor20250429AllowedCallerCodeExecution20260521 ToolTextEditor20250429AllowedCaller = "code_execution_20260521"`

          - `CacheControl CacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `InputExamples []map[string, any] Optional`

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

        - `type ToolTextEditor20250728 struct{…}`

          - `Name StrReplaceBasedEditTool`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type TextEditor20250728`

          - `AllowedCallers []string Optional`

            - `const ToolTextEditor20250728AllowedCallerDirect ToolTextEditor20250728AllowedCaller = "direct"`

            - `const ToolTextEditor20250728AllowedCallerCodeExecution20250825 ToolTextEditor20250728AllowedCaller = "code_execution_20250825"`

            - `const ToolTextEditor20250728AllowedCallerCodeExecution20260120 ToolTextEditor20250728AllowedCaller = "code_execution_20260120"`

            - `const ToolTextEditor20250728AllowedCallerCodeExecution20260521 ToolTextEditor20250728AllowedCaller = "code_execution_20260521"`

          - `CacheControl CacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `InputExamples []map[string, any] Optional`

          - `MaxCharacters int64 Optional`

            Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

            minimum: 1

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

        - `type WebSearchTool20250305 struct{…}`

          - `Name WebSearch`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type WebSearch20250305`

          - `AllowedCallers []string Optional`

            - `const WebSearchTool20250305AllowedCallerDirect WebSearchTool20250305AllowedCaller = "direct"`

            - `const WebSearchTool20250305AllowedCallerCodeExecution20250825 WebSearchTool20250305AllowedCaller = "code_execution_20250825"`

            - `const WebSearchTool20250305AllowedCallerCodeExecution20260120 WebSearchTool20250305AllowedCaller = "code_execution_20260120"`

            - `const WebSearchTool20250305AllowedCallerCodeExecution20260521 WebSearchTool20250305AllowedCaller = "code_execution_20260521"`

          - `AllowedDomains []string Optional`

            If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

          - `BlockedDomains []string Optional`

            If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

          - `CacheControl CacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `MaxUses int64 Optional`

            Maximum number of times the tool can be used in the API request.

            exclusiveMinimum: 0

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

          - `UserLocation UserLocation Optional`

            Parameters for the user's location. Used to provide more relevant search results.

            - `Type Approximate`

            - `City string Optional`

              The city of the user.

              maxLength: 255, minLength: 1

            - `Country string Optional`

              The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

              maxLength: 2, minLength: 2

            - `Region string Optional`

              The region of the user.

              maxLength: 255, minLength: 1

            - `Timezone string Optional`

              The [IANA timezone](https://nodatime.org/TimeZones) of the user.

              maxLength: 255, minLength: 1

        - `type WebFetchTool20250910 struct{…}`

          - `Name WebFetch`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type WebFetch20250910`

          - `AllowedCallers []string Optional`

            - `const WebFetchTool20250910AllowedCallerDirect WebFetchTool20250910AllowedCaller = "direct"`

            - `const WebFetchTool20250910AllowedCallerCodeExecution20250825 WebFetchTool20250910AllowedCaller = "code_execution_20250825"`

            - `const WebFetchTool20250910AllowedCallerCodeExecution20260120 WebFetchTool20250910AllowedCaller = "code_execution_20260120"`

            - `const WebFetchTool20250910AllowedCallerCodeExecution20260521 WebFetchTool20250910AllowedCaller = "code_execution_20260521"`

          - `AllowedDomains []string Optional`

            List of domains to allow fetching from

          - `BlockedDomains []string Optional`

            List of domains to block fetching from

          - `CacheControl CacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `Citations CitationsConfigParamResp Optional`

            Citations configuration for fetched documents. Citations are disabled by default.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `MaxContentTokens int64 Optional`

            Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

            exclusiveMinimum: 0

          - `MaxUses int64 Optional`

            Maximum number of times the tool can be used in the API request.

            exclusiveMinimum: 0

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

        - `type WebSearchTool20260209 struct{…}`

          - `Name WebSearch`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type WebSearch20260209`

          - `AllowedCallers []string Optional`

            - `const WebSearchTool20260209AllowedCallerDirect WebSearchTool20260209AllowedCaller = "direct"`

            - `const WebSearchTool20260209AllowedCallerCodeExecution20250825 WebSearchTool20260209AllowedCaller = "code_execution_20250825"`

            - `const WebSearchTool20260209AllowedCallerCodeExecution20260120 WebSearchTool20260209AllowedCaller = "code_execution_20260120"`

            - `const WebSearchTool20260209AllowedCallerCodeExecution20260521 WebSearchTool20260209AllowedCaller = "code_execution_20260521"`

          - `AllowedDomains []string Optional`

            If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

          - `BlockedDomains []string Optional`

            If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

          - `CacheControl CacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `MaxUses int64 Optional`

            Maximum number of times the tool can be used in the API request.

            exclusiveMinimum: 0

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

          - `UserLocation UserLocation Optional`

            Parameters for the user's location. Used to provide more relevant search results.

        - `type WebFetchTool20260209 struct{…}`

          - `Name WebFetch`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type WebFetch20260209`

          - `AllowedCallers []string Optional`

            - `const WebFetchTool20260209AllowedCallerDirect WebFetchTool20260209AllowedCaller = "direct"`

            - `const WebFetchTool20260209AllowedCallerCodeExecution20250825 WebFetchTool20260209AllowedCaller = "code_execution_20250825"`

            - `const WebFetchTool20260209AllowedCallerCodeExecution20260120 WebFetchTool20260209AllowedCaller = "code_execution_20260120"`

            - `const WebFetchTool20260209AllowedCallerCodeExecution20260521 WebFetchTool20260209AllowedCaller = "code_execution_20260521"`

          - `AllowedDomains []string Optional`

            List of domains to allow fetching from

          - `BlockedDomains []string Optional`

            List of domains to block fetching from

          - `CacheControl CacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `Citations CitationsConfigParamResp Optional`

            Citations configuration for fetched documents. Citations are disabled by default.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `MaxContentTokens int64 Optional`

            Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

            exclusiveMinimum: 0

          - `MaxUses int64 Optional`

            Maximum number of times the tool can be used in the API request.

            exclusiveMinimum: 0

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

        - `type WebFetchTool20260309 struct{…}`

          Web fetch tool with use_cache parameter for bypassing cached content.

          - `Name WebFetch`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type WebFetch20260309`

          - `AllowedCallers []string Optional`

            - `const WebFetchTool20260309AllowedCallerDirect WebFetchTool20260309AllowedCaller = "direct"`

            - `const WebFetchTool20260309AllowedCallerCodeExecution20250825 WebFetchTool20260309AllowedCaller = "code_execution_20250825"`

            - `const WebFetchTool20260309AllowedCallerCodeExecution20260120 WebFetchTool20260309AllowedCaller = "code_execution_20260120"`

            - `const WebFetchTool20260309AllowedCallerCodeExecution20260521 WebFetchTool20260309AllowedCaller = "code_execution_20260521"`

          - `AllowedDomains []string Optional`

            List of domains to allow fetching from

          - `BlockedDomains []string Optional`

            List of domains to block fetching from

          - `CacheControl CacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `Citations CitationsConfigParamResp Optional`

            Citations configuration for fetched documents. Citations are disabled by default.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `MaxContentTokens int64 Optional`

            Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

            exclusiveMinimum: 0

          - `MaxUses int64 Optional`

            Maximum number of times the tool can be used in the API request.

            exclusiveMinimum: 0

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

          - `UseCache bool Optional`

            Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

        - `type WebSearchTool20260318 struct{…}`

          - `Name WebSearch`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type WebSearch20260318`

          - `AllowedCallers []string Optional`

            - `const WebSearchTool20260318AllowedCallerDirect WebSearchTool20260318AllowedCaller = "direct"`

            - `const WebSearchTool20260318AllowedCallerCodeExecution20250825 WebSearchTool20260318AllowedCaller = "code_execution_20250825"`

            - `const WebSearchTool20260318AllowedCallerCodeExecution20260120 WebSearchTool20260318AllowedCaller = "code_execution_20260120"`

            - `const WebSearchTool20260318AllowedCallerCodeExecution20260521 WebSearchTool20260318AllowedCaller = "code_execution_20260521"`

          - `AllowedDomains []string Optional`

            If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

          - `BlockedDomains []string Optional`

            If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

          - `CacheControl CacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `MaxUses int64 Optional`

            Maximum number of times the tool can be used in the API request.

            exclusiveMinimum: 0

          - `ResponseInclusion WebSearchTool20260318ResponseInclusion Optional`

            How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

            - `const WebSearchTool20260318ResponseInclusionFull WebSearchTool20260318ResponseInclusion = "full"`

            - `const WebSearchTool20260318ResponseInclusionExcluded WebSearchTool20260318ResponseInclusion = "excluded"`

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

          - `UserLocation UserLocation Optional`

            Parameters for the user's location. Used to provide more relevant search results.

        - `type WebFetchTool20260318 struct{…}`

          - `Name WebFetch`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type WebFetch20260318`

          - `AllowedCallers []string Optional`

            - `const WebFetchTool20260318AllowedCallerDirect WebFetchTool20260318AllowedCaller = "direct"`

            - `const WebFetchTool20260318AllowedCallerCodeExecution20250825 WebFetchTool20260318AllowedCaller = "code_execution_20250825"`

            - `const WebFetchTool20260318AllowedCallerCodeExecution20260120 WebFetchTool20260318AllowedCaller = "code_execution_20260120"`

            - `const WebFetchTool20260318AllowedCallerCodeExecution20260521 WebFetchTool20260318AllowedCaller = "code_execution_20260521"`

          - `AllowedDomains []string Optional`

            List of domains to allow fetching from

          - `BlockedDomains []string Optional`

            List of domains to block fetching from

          - `CacheControl CacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `Citations CitationsConfigParamResp Optional`

            Citations configuration for fetched documents. Citations are disabled by default.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `MaxContentTokens int64 Optional`

            Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

            exclusiveMinimum: 0

          - `MaxUses int64 Optional`

            Maximum number of times the tool can be used in the API request.

            exclusiveMinimum: 0

          - `ResponseInclusion WebFetchTool20260318ResponseInclusion Optional`

            How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

            - `const WebFetchTool20260318ResponseInclusionFull WebFetchTool20260318ResponseInclusion = "full"`

            - `const WebFetchTool20260318ResponseInclusionExcluded WebFetchTool20260318ResponseInclusion = "excluded"`

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

          - `UseCache bool Optional`

            Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

        - `type ToolSearchToolBm25_20251119 struct{…}`

          - `Name ToolSearchToolBm25`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type ToolSearchToolBm25_20251119Type`

            - `const ToolSearchToolBm25_20251119TypeToolSearchToolBm25_20251119 ToolSearchToolBm25_20251119Type = "tool_search_tool_bm25_20251119"`

            - `const ToolSearchToolBm25_20251119TypeToolSearchToolBm25 ToolSearchToolBm25_20251119Type = "tool_search_tool_bm25"`

          - `AllowedCallers []string Optional`

            - `const ToolSearchToolBm25_20251119AllowedCallerDirect ToolSearchToolBm25_20251119AllowedCaller = "direct"`

            - `const ToolSearchToolBm25_20251119AllowedCallerCodeExecution20250825 ToolSearchToolBm25_20251119AllowedCaller = "code_execution_20250825"`

            - `const ToolSearchToolBm25_20251119AllowedCallerCodeExecution20260120 ToolSearchToolBm25_20251119AllowedCaller = "code_execution_20260120"`

            - `const ToolSearchToolBm25_20251119AllowedCallerCodeExecution20260521 ToolSearchToolBm25_20251119AllowedCaller = "code_execution_20260521"`

          - `CacheControl CacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

        - `type ToolSearchToolRegex20251119 struct{…}`

          - `Name ToolSearchToolRegex`

            Name of the tool.

            This is how the tool will be called by the model and in `tool_use` blocks.

          - `Type ToolSearchToolRegex20251119Type`

            - `const ToolSearchToolRegex20251119TypeToolSearchToolRegex20251119 ToolSearchToolRegex20251119Type = "tool_search_tool_regex_20251119"`

            - `const ToolSearchToolRegex20251119TypeToolSearchToolRegex ToolSearchToolRegex20251119Type = "tool_search_tool_regex"`

          - `AllowedCallers []string Optional`

            - `const ToolSearchToolRegex20251119AllowedCallerDirect ToolSearchToolRegex20251119AllowedCaller = "direct"`

            - `const ToolSearchToolRegex20251119AllowedCallerCodeExecution20250825 ToolSearchToolRegex20251119AllowedCaller = "code_execution_20250825"`

            - `const ToolSearchToolRegex20251119AllowedCallerCodeExecution20260120 ToolSearchToolRegex20251119AllowedCaller = "code_execution_20260120"`

            - `const ToolSearchToolRegex20251119AllowedCallerCodeExecution20260521 ToolSearchToolRegex20251119AllowedCaller = "code_execution_20260521"`

          - `CacheControl CacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `DeferLoading bool Optional`

            If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

          - `Strict bool Optional`

            When true, guarantees schema validation on tool names and inputs

      - `Temperature float64 Optional`

        **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not support setting temperature. A value of 1.0 of will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

        Amount of randomness injected into the response.

        Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

        Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

        maximum: 1, minimum: 0

      - `TopK int64 Optional`

        **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not accept top_k; any value will be rejected with a 400 error.

        Only sample from the top K options for each subsequent token.

        Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

        Recommended for advanced use cases only.

        minimum: 0

      - `TopP float64 Optional`

        **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not support setting top_p. A value >= 0.99 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

        Use nucleus sampling.

        In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.

        Recommended for advanced use cases only.

        maximum: 1, minimum: 0

  - `UserProfileID param.Field[string] Optional`

    Header param: The user profile ID to attribute the requests in this batch to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header. Applies to every request in the batch; an individual request whose `user_profile_id` body field conflicts with this header is errored.

## Returns

- `type MessageBatch struct{…}`

  - `ID string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `ArchivedAt Time`

    RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

    format: date-time

  - `CancelInitiatedAt Time`

    RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

    format: date-time

  - `CreatedAt Time`

    RFC 3339 datetime string representing the time at which the Message Batch was created.

    format: date-time

  - `EndedAt Time`

    RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

    Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

    format: date-time

  - `ExpiresAt Time`

    RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

    format: date-time

  - `ProcessingStatus MessageBatchProcessingStatus`

    Processing status of the Message Batch.

    - `const MessageBatchProcessingStatusInProgress MessageBatchProcessingStatus = "in_progress"`

    - `const MessageBatchProcessingStatusCanceling MessageBatchProcessingStatus = "canceling"`

    - `const MessageBatchProcessingStatusEnded MessageBatchProcessingStatus = "ended"`

  - `RequestCounts MessageBatchRequestCounts`

    Tallies requests within the Message Batch, categorized by their status.

    Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

    - `Canceled int64`

      Number of requests in the Message Batch that have been canceled.

      This is zero until processing of the entire Message Batch has ended.

      default: 0

    - `Errored int64`

      Number of requests in the Message Batch that encountered an error.

      This is zero until processing of the entire Message Batch has ended.

      default: 0

    - `Expired int64`

      Number of requests in the Message Batch that have expired.

      This is zero until processing of the entire Message Batch has ended.

      default: 0

    - `Processing int64`

      Number of requests in the Message Batch that are processing.

      default: 0

    - `Succeeded int64`

      Number of requests in the Message Batch that have completed successfully.

      This is zero until processing of the entire Message Batch has ended.

      default: 0

  - `ResultsURL string`

    URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

    Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

  - `Type MessageBatch`

    Object type.

    For Message Batches, this is always `"message_batch"`.

    default: message_batch

## Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	messageBatch, err := client.Messages.Batches.New(context.TODO(), anthropic.MessageBatchNewParams{
		Requests: []anthropic.MessageBatchNewParamsRequest{anthropic.MessageBatchNewParamsRequest{
			CustomID: "my-custom-id-1",
			Params: anthropic.MessageBatchNewParamsRequestParams{
				MaxTokens: 1024,
				Messages: []anthropic.MessageParam{anthropic.MessageParam{
					Content: []anthropic.ContentBlockParamUnion{anthropic.ContentBlockParamUnion{
						OfText: &anthropic.TextBlockParam{
							Text: "x",
						},
					}},
					Role: anthropic.MessageParamRoleUser,
				}},
				Model: anthropic.ModelClaudeOpus5,
			},
		}},
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", messageBatch.ID)
}
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
