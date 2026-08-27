# Create a Message

`client.Beta.Messages.New(ctx, params) (*BetaMessage, error)`

**POST** `/v1/messages`

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

The Messages API can be used for either single queries or stateless multi-turn conversations.

Learn more about the Messages API in our [user guide](https://platform.claude.com/docs/en/get-started)

## Parameters

- `params BetaMessageNewParams`

  - `MaxTokens param.Field[int64]`

    Body param: The maximum number of tokens to generate before stopping.

    Note that our models may stop _before_ reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

    Set to `0` to populate the [prompt cache](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#pre-warming-the-cache) without generating a response.

    Different models have different maximum values for this parameter.  See [models](https://platform.claude.com/docs/en/about-claude/models/overview) for details.

    minimum: 0

  - `Messages param.Field[[]BetaMessageParamResp]`

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

    - `Content []BetaContentBlockParamUnionResp`

      - `[]BetaContentBlockParamUnionResp`

        - `type BetaTextBlockParamResp struct{…}`

          - `Text string`

            minLength: 1

          - `Type Text`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

            - `Type Ephemeral`

            - `TTL BetaCacheControlEphemeralTTL Optional`

              The time-to-live for the cache control breakpoint.

              This may be one the following values:

              - `5m`: 5 minutes
              - `1h`: 1 hour

              Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

              - `const BetaCacheControlEphemeralTTLTTL5m BetaCacheControlEphemeralTTL = "5m"`

              - `const BetaCacheControlEphemeralTTLTTL1h BetaCacheControlEphemeralTTL = "1h"`

          - `Citations []BetaTextCitationParamUnionResp Optional`

            - `type BetaCitationCharLocationParamResp struct{…}`

              - `CitedText string`

              - `DocumentIndex int64`

                minimum: 0

              - `DocumentTitle string`

                maxLength: 500, minLength: 1

              - `EndCharIndex int64`

              - `StartCharIndex int64`

                minimum: 0

              - `Type CharLocation`

            - `type BetaCitationPageLocationParamResp struct{…}`

              - `CitedText string`

              - `DocumentIndex int64`

                minimum: 0

              - `DocumentTitle string`

                maxLength: 500, minLength: 1

              - `EndPageNumber int64`

              - `StartPageNumber int64`

                minimum: 1

              - `Type PageLocation`

            - `type BetaCitationContentBlockLocationParamResp struct{…}`

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

            - `type BetaCitationWebSearchResultLocationParamResp struct{…}`

              - `CitedText string`

              - `EncryptedIndex string`

              - `Title string`

                maxLength: 512, minLength: 1

              - `Type WebSearchResultLocation`

              - `URL string`

                minLength: 1

            - `type BetaCitationSearchResultLocationParamResp struct{…}`

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

        - `type BetaImageBlockParamResp struct{…}`

          - `Source BetaImageBlockParamSourceUnionResp`

            - `type BetaBase64ImageSource struct{…}`

              - `Data string`

                format: byte

              - `MediaType BetaBase64ImageSourceMediaType`

                - `const BetaBase64ImageSourceMediaTypeImageJPEG BetaBase64ImageSourceMediaType = "image/jpeg"`

                - `const BetaBase64ImageSourceMediaTypeImagePNG BetaBase64ImageSourceMediaType = "image/png"`

                - `const BetaBase64ImageSourceMediaTypeImageGIF BetaBase64ImageSourceMediaType = "image/gif"`

                - `const BetaBase64ImageSourceMediaTypeImageWebP BetaBase64ImageSourceMediaType = "image/webp"`

              - `Type Base64`

            - `type BetaURLImageSource struct{…}`

              - `Type URL`

              - `URL string`

            - `type BetaFileImageSource struct{…}`

              - `FileID string`

              - `Type File`

          - `Type Image`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `Transformations BetaImageTransformationsParamResp Optional`

            Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.

            - `OversizedImage BetaImageTransformationsParamOversizedImage Optional`

              What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

              - `const BetaImageTransformationsParamOversizedImageDownsize BetaImageTransformationsParamOversizedImage = "downsize"`

              - `const BetaImageTransformationsParamOversizedImageError BetaImageTransformationsParamOversizedImage = "error"`

        - `type BetaRequestDocumentBlock struct{…}`

          - `Source BetaRequestDocumentBlockSourceUnion`

            - `type BetaBase64PDFSource struct{…}`

              - `Data string`

                format: byte

              - `MediaType ApplicationPDF`

              - `Type Base64`

            - `type BetaPlainTextSource struct{…}`

              - `Data string`

              - `MediaType TextPlain`

              - `Type Text`

            - `type BetaContentBlockSource struct{…}`

              - `Content BetaContentBlockSourceContentUnion`

                - `string`

                - `[]BetaContentBlockSourceContentUnion`

                  - `type BetaTextBlockParamResp struct{…}`

                  - `type BetaImageBlockParamResp struct{…}`

              - `Type Content`

            - `type BetaURLPDFSource struct{…}`

              - `Type URL`

              - `URL string`

            - `type BetaFileDocumentSource struct{…}`

              - `FileID string`

              - `Type File`

          - `Type Document`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `Citations BetaCitationsConfigParamResp Optional`

            - `Enabled bool Optional`

          - `Context string Optional`

            minLength: 1

          - `Title string Optional`

            maxLength: 500, minLength: 1

        - `type BetaSearchResultBlockParamResp struct{…}`

          - `Content []BetaTextBlockParamResp`

            - `Text string`

              minLength: 1

            - `Type Text`

            - `CacheControl BetaCacheControlEphemeral Optional`

              Create a cache control breakpoint at this content block.

            - `Citations []BetaTextCitationParamUnionResp Optional`

          - `Source string`

          - `Title string`

          - `Type SearchResult`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `Citations BetaCitationsConfigParamResp Optional`

        - `type BetaThinkingBlockParamResp struct{…}`

          - `Signature string`

            The `signature` value of this thinking block, exactly as returned by the API in a previous response. Used to verify that the block was generated by Claude.

            Thinking blocks must be passed back unmodified and in their original order; a modified block results in a 400 `invalid_request_error`.

          - `Thinking string`

            The `thinking` text of this block as returned by the API.

          - `Type Thinking`

        - `type BetaRedactedThinkingBlockParamResp struct{…}`

          - `Data string`

            The `data` value of this redacted thinking block, exactly as returned by the API in a previous response. Opaque and encrypted; pass it back unchanged.

          - `Type RedactedThinking`

        - `type BetaToolUseBlockParamResp struct{…}`

          - `ID string`

            pattern: ^[a-zA-Z0-9_-]+$

          - `Input map[string, any]`

          - `Name string`

            maxLength: 200, minLength: 1

          - `Type ToolUse`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `Caller BetaToolUseBlockParamCallerUnionResp Optional`

            Tool invocation directly from the model.

            - `type BetaDirectCaller struct{…}`

              Tool invocation directly from the model.

              - `Type Direct`

            - `type BetaServerToolCaller struct{…}`

              Tool invocation generated by a server-side tool.

              - `ToolID string`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `Type CodeExecution20250825`

            - `type BetaServerToolCaller20260120 struct{…}`

              - `ToolID string`

                pattern: ^srvtoolu_[a-zA-Z0-9_]+$

              - `Type CodeExecution20260120`

          - `ToolsetName string Optional`

            For a toolset member tool_use, the toolset family this member belongs to.

            maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

        - `type BetaToolResultBlockParamResp struct{…}`

          - `ToolUseID string`

            pattern: ^[a-zA-Z0-9_-]+$

          - `Type ToolResult`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `Content []BetaToolResultBlockParamContentUnionResp Optional`

            - `[]BetaToolResultBlockParamContentUnionResp`

              - `type BetaTextBlockParamResp struct{…}`

              - `type BetaImageBlockParamResp struct{…}`

              - `type BetaSearchResultBlockParamResp struct{…}`

              - `type BetaRequestDocumentBlock struct{…}`

              - `type BetaToolReferenceBlockParamResp struct{…}`

                Tool reference block that can be included in tool_result content.

                - `ToolName string`

                  maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

                - `Type ToolReference`

                - `CacheControl BetaCacheControlEphemeral Optional`

                  Create a cache control breakpoint at this content block.

              - `type BetaBrowserStateBlockParamResp struct{…}`

                The caller's browser state after a browser toolset member call —
                the full inventory of open tabs, which tab is active, and any side
                effects (tabs opened, download state changes) the call produced.

                At most one per `tool_result`, only on a non-error result answering a
                browser toolset member `tool_use`. The server renders the
                model-visible text from it; the model never sees the raw fields.

                - `Tabs []BetaBrowserStateTabEntry`

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

                - `CacheControl BetaCacheControlEphemeral Optional`

                  Create a cache control breakpoint at this content block.

                - `StateChanges []BetaBrowserStateChangeUnion Optional`

                  Tabs opened and download state changes during this call. "Nothing to report" is expressed by omitting the field, never by an empty list.

                  maxItems: 200, minItems: 1

                  - `type BetaBrowserStateChangeTabOpened struct{…}`

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

                  - `type BetaBrowserStateChangeDownloadStarted struct{…}`

                    A file download that started during this call.

                    - `DownloadID string`

                      The caller-assigned identifier for this download, stable across the state changes reporting it.

                      maxLength: 4096, minLength: 1, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                    - `Type DownloadStarted`

                    - `URL string`

                      The final post-redirect URL the download was served from.

                      maxLength: 4096, pattern: ^[^\x00-\x1f\x7f-\x9f\u2028\u2029]*$

                  - `type BetaBrowserStateChangeDownloadCompleted struct{…}`

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

                  - `type BetaBrowserStateChangeDownloadFailed struct{…}`

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

        - `type BetaServerToolUseBlockParamResp struct{…}`

          - `ID string`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `Input map[string, any]`

          - `Name BetaServerToolUseBlockParamName`

            - `const BetaServerToolUseBlockParamNameAdvisor BetaServerToolUseBlockParamName = "advisor"`

            - `const BetaServerToolUseBlockParamNameWebSearch BetaServerToolUseBlockParamName = "web_search"`

            - `const BetaServerToolUseBlockParamNameWebFetch BetaServerToolUseBlockParamName = "web_fetch"`

            - `const BetaServerToolUseBlockParamNameCodeExecution BetaServerToolUseBlockParamName = "code_execution"`

            - `const BetaServerToolUseBlockParamNameBashCodeExecution BetaServerToolUseBlockParamName = "bash_code_execution"`

            - `const BetaServerToolUseBlockParamNameTextEditorCodeExecution BetaServerToolUseBlockParamName = "text_editor_code_execution"`

            - `const BetaServerToolUseBlockParamNameToolSearchToolRegex BetaServerToolUseBlockParamName = "tool_search_tool_regex"`

            - `const BetaServerToolUseBlockParamNameToolSearchToolBm25 BetaServerToolUseBlockParamName = "tool_search_tool_bm25"`

          - `Type ServerToolUse`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `Caller BetaServerToolUseBlockParamCallerUnionResp Optional`

            Tool invocation directly from the model.

            - `type BetaDirectCaller struct{…}`

              Tool invocation directly from the model.

            - `type BetaServerToolCaller struct{…}`

              Tool invocation generated by a server-side tool.

            - `type BetaServerToolCaller20260120 struct{…}`

        - `type BetaWebSearchToolResultBlockParamResp struct{…}`

          - `Content BetaWebSearchToolResultBlockParamContentUnionResp`

            - `[]BetaWebSearchResultBlockParamResp`

              - `EncryptedContent string`

              - `Title string`

              - `Type WebSearchResult`

              - `URL string`

              - `PageAge string Optional`

            - `type BetaWebSearchToolRequestError struct{…}`

              - `ErrorCode BetaWebSearchToolResultErrorCode`

                - `const BetaWebSearchToolResultErrorCodeInvalidToolInput BetaWebSearchToolResultErrorCode = "invalid_tool_input"`

                - `const BetaWebSearchToolResultErrorCodeUnavailable BetaWebSearchToolResultErrorCode = "unavailable"`

                - `const BetaWebSearchToolResultErrorCodeMaxUsesExceeded BetaWebSearchToolResultErrorCode = "max_uses_exceeded"`

                - `const BetaWebSearchToolResultErrorCodeTooManyRequests BetaWebSearchToolResultErrorCode = "too_many_requests"`

                - `const BetaWebSearchToolResultErrorCodeQueryTooLong BetaWebSearchToolResultErrorCode = "query_too_long"`

                - `const BetaWebSearchToolResultErrorCodeRequestTooLarge BetaWebSearchToolResultErrorCode = "request_too_large"`

              - `Type WebSearchToolResultError`

          - `ToolUseID string`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `Type WebSearchToolResult`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `Caller BetaWebSearchToolResultBlockParamCallerUnionResp Optional`

            Tool invocation directly from the model.

            - `type BetaDirectCaller struct{…}`

              Tool invocation directly from the model.

            - `type BetaServerToolCaller struct{…}`

              Tool invocation generated by a server-side tool.

            - `type BetaServerToolCaller20260120 struct{…}`

        - `type BetaWebFetchToolResultBlockParamResp struct{…}`

          - `Content BetaWebFetchToolResultBlockParamContentUnionResp`

            - `type BetaWebFetchToolResultErrorBlockParamResp struct{…}`

              - `ErrorCode BetaWebFetchToolResultErrorCode`

                - `const BetaWebFetchToolResultErrorCodeInvalidToolInput BetaWebFetchToolResultErrorCode = "invalid_tool_input"`

                - `const BetaWebFetchToolResultErrorCodeURLTooLong BetaWebFetchToolResultErrorCode = "url_too_long"`

                - `const BetaWebFetchToolResultErrorCodeURLNotAllowed BetaWebFetchToolResultErrorCode = "url_not_allowed"`

                - `const BetaWebFetchToolResultErrorCodeURLNotInPriorContext BetaWebFetchToolResultErrorCode = "url_not_in_prior_context"`

                - `const BetaWebFetchToolResultErrorCodeURLNotAccessible BetaWebFetchToolResultErrorCode = "url_not_accessible"`

                - `const BetaWebFetchToolResultErrorCodeUnsupportedContentType BetaWebFetchToolResultErrorCode = "unsupported_content_type"`

                - `const BetaWebFetchToolResultErrorCodeTooManyRequests BetaWebFetchToolResultErrorCode = "too_many_requests"`

                - `const BetaWebFetchToolResultErrorCodeMaxUsesExceeded BetaWebFetchToolResultErrorCode = "max_uses_exceeded"`

                - `const BetaWebFetchToolResultErrorCodeUnavailable BetaWebFetchToolResultErrorCode = "unavailable"`

              - `Type WebFetchToolResultError`

            - `type BetaWebFetchBlockParamResp struct{…}`

              - `Content BetaRequestDocumentBlock`

              - `Type WebFetchResult`

              - `URL string`

                Fetched content URL

              - `RetrievedAt string Optional`

                ISO 8601 timestamp when the content was retrieved

          - `ToolUseID string`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `Type WebFetchToolResult`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `Caller BetaWebFetchToolResultBlockParamCallerUnionResp Optional`

            Tool invocation directly from the model.

            - `type BetaDirectCaller struct{…}`

              Tool invocation directly from the model.

            - `type BetaServerToolCaller struct{…}`

              Tool invocation generated by a server-side tool.

            - `type BetaServerToolCaller20260120 struct{…}`

        - `type BetaAdvisorToolResultBlockParamResp struct{…}`

          - `Content BetaAdvisorToolResultBlockParamContentUnionResp`

            - `type BetaAdvisorToolResultErrorParamResp struct{…}`

              - `ErrorCode BetaAdvisorToolResultErrorParamErrorCode`

                - `const BetaAdvisorToolResultErrorParamErrorCodeMaxUsesExceeded BetaAdvisorToolResultErrorParamErrorCode = "max_uses_exceeded"`

                - `const BetaAdvisorToolResultErrorParamErrorCodePromptTooLong BetaAdvisorToolResultErrorParamErrorCode = "prompt_too_long"`

                - `const BetaAdvisorToolResultErrorParamErrorCodeTooManyRequests BetaAdvisorToolResultErrorParamErrorCode = "too_many_requests"`

                - `const BetaAdvisorToolResultErrorParamErrorCodeOverloaded BetaAdvisorToolResultErrorParamErrorCode = "overloaded"`

                - `const BetaAdvisorToolResultErrorParamErrorCodeUnavailable BetaAdvisorToolResultErrorParamErrorCode = "unavailable"`

                - `const BetaAdvisorToolResultErrorParamErrorCodeExecutionTimeExceeded BetaAdvisorToolResultErrorParamErrorCode = "execution_time_exceeded"`

                - `const BetaAdvisorToolResultErrorParamErrorCodeModelNotFound BetaAdvisorToolResultErrorParamErrorCode = "model_not_found"`

              - `Type AdvisorToolResultError`

            - `type BetaAdvisorResultBlockParamResp struct{…}`

              - `Text string`

              - `Type AdvisorResult`

              - `StopReason string Optional`

            - `type BetaAdvisorRedactedResultBlockParamResp struct{…}`

              - `EncryptedContent string`

                Opaque blob produced by a prior response; must be round-tripped verbatim.

              - `Type AdvisorRedactedResult`

              - `StopReason string Optional`

          - `ToolUseID string`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `Type AdvisorToolResult`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

        - `type BetaCodeExecutionToolResultBlockParamResp struct{…}`

          - `Content BetaCodeExecutionToolResultBlockParamContentUnionResp`

            Code execution result with encrypted stdout for PFC + web_search results.

            - `type BetaCodeExecutionToolResultErrorParamResp struct{…}`

              - `ErrorCode BetaCodeExecutionToolResultErrorCode`

                - `const BetaCodeExecutionToolResultErrorCodeInvalidToolInput BetaCodeExecutionToolResultErrorCode = "invalid_tool_input"`

                - `const BetaCodeExecutionToolResultErrorCodeUnavailable BetaCodeExecutionToolResultErrorCode = "unavailable"`

                - `const BetaCodeExecutionToolResultErrorCodeTooManyRequests BetaCodeExecutionToolResultErrorCode = "too_many_requests"`

                - `const BetaCodeExecutionToolResultErrorCodeExecutionTimeExceeded BetaCodeExecutionToolResultErrorCode = "execution_time_exceeded"`

              - `Type CodeExecutionToolResultError`

            - `type BetaCodeExecutionResultBlockParamResp struct{…}`

              - `Content []BetaCodeExecutionOutputBlockParamResp`

                - `FileID string`

                - `Type CodeExecutionOutput`

              - `ReturnCode int64`

              - `Stderr string`

              - `Stdout string`

              - `Type CodeExecutionResult`

            - `type BetaEncryptedCodeExecutionResultBlockParamResp struct{…}`

              Code execution result with encrypted stdout for PFC + web_search results.

              - `Content []BetaCodeExecutionOutputBlockParamResp`

                - `FileID string`

                - `Type CodeExecutionOutput`

              - `EncryptedStdout string`

              - `ReturnCode int64`

              - `Stderr string`

              - `Type EncryptedCodeExecutionResult`

          - `ToolUseID string`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `Type CodeExecutionToolResult`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

        - `type BetaBashCodeExecutionToolResultBlockParamResp struct{…}`

          - `Content BetaBashCodeExecutionToolResultBlockParamContentUnionResp`

            - `type BetaBashCodeExecutionToolResultErrorParamResp struct{…}`

              - `ErrorCode BetaBashCodeExecutionToolResultErrorParamErrorCode`

                - `const BetaBashCodeExecutionToolResultErrorParamErrorCodeInvalidToolInput BetaBashCodeExecutionToolResultErrorParamErrorCode = "invalid_tool_input"`

                - `const BetaBashCodeExecutionToolResultErrorParamErrorCodeUnavailable BetaBashCodeExecutionToolResultErrorParamErrorCode = "unavailable"`

                - `const BetaBashCodeExecutionToolResultErrorParamErrorCodeTooManyRequests BetaBashCodeExecutionToolResultErrorParamErrorCode = "too_many_requests"`

                - `const BetaBashCodeExecutionToolResultErrorParamErrorCodeExecutionTimeExceeded BetaBashCodeExecutionToolResultErrorParamErrorCode = "execution_time_exceeded"`

                - `const BetaBashCodeExecutionToolResultErrorParamErrorCodeOutputFileTooLarge BetaBashCodeExecutionToolResultErrorParamErrorCode = "output_file_too_large"`

              - `Type BashCodeExecutionToolResultError`

            - `type BetaBashCodeExecutionResultBlockParamResp struct{…}`

              - `Content []BetaBashCodeExecutionOutputBlockParamResp`

                - `FileID string`

                - `Type BashCodeExecutionOutput`

              - `ReturnCode int64`

              - `Stderr string`

              - `Stdout string`

              - `Type BashCodeExecutionResult`

          - `ToolUseID string`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `Type BashCodeExecutionToolResult`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

        - `type BetaTextEditorCodeExecutionToolResultBlockParamResp struct{…}`

          - `Content BetaTextEditorCodeExecutionToolResultBlockParamContentUnionResp`

            - `type BetaTextEditorCodeExecutionToolResultErrorParamResp struct{…}`

              - `ErrorCode BetaTextEditorCodeExecutionToolResultErrorParamErrorCode`

                - `const BetaTextEditorCodeExecutionToolResultErrorParamErrorCodeInvalidToolInput BetaTextEditorCodeExecutionToolResultErrorParamErrorCode = "invalid_tool_input"`

                - `const BetaTextEditorCodeExecutionToolResultErrorParamErrorCodeUnavailable BetaTextEditorCodeExecutionToolResultErrorParamErrorCode = "unavailable"`

                - `const BetaTextEditorCodeExecutionToolResultErrorParamErrorCodeTooManyRequests BetaTextEditorCodeExecutionToolResultErrorParamErrorCode = "too_many_requests"`

                - `const BetaTextEditorCodeExecutionToolResultErrorParamErrorCodeExecutionTimeExceeded BetaTextEditorCodeExecutionToolResultErrorParamErrorCode = "execution_time_exceeded"`

                - `const BetaTextEditorCodeExecutionToolResultErrorParamErrorCodeFileNotFound BetaTextEditorCodeExecutionToolResultErrorParamErrorCode = "file_not_found"`

              - `Type TextEditorCodeExecutionToolResultError`

              - `ErrorMessage string Optional`

            - `type BetaTextEditorCodeExecutionViewResultBlockParamResp struct{…}`

              - `Content string`

              - `FileType BetaTextEditorCodeExecutionViewResultBlockParamFileType`

                - `const BetaTextEditorCodeExecutionViewResultBlockParamFileTypeText BetaTextEditorCodeExecutionViewResultBlockParamFileType = "text"`

                - `const BetaTextEditorCodeExecutionViewResultBlockParamFileTypeImage BetaTextEditorCodeExecutionViewResultBlockParamFileType = "image"`

                - `const BetaTextEditorCodeExecutionViewResultBlockParamFileTypePDF BetaTextEditorCodeExecutionViewResultBlockParamFileType = "pdf"`

              - `Type TextEditorCodeExecutionViewResult`

              - `NumLines int64 Optional`

              - `StartLine int64 Optional`

              - `TotalLines int64 Optional`

            - `type BetaTextEditorCodeExecutionCreateResultBlockParamResp struct{…}`

              - `IsFileUpdate bool`

              - `Type TextEditorCodeExecutionCreateResult`

            - `type BetaTextEditorCodeExecutionStrReplaceResultBlockParamResp struct{…}`

              - `Type TextEditorCodeExecutionStrReplaceResult`

              - `Lines []string Optional`

              - `NewLines int64 Optional`

              - `NewStart int64 Optional`

              - `OldLines int64 Optional`

              - `OldStart int64 Optional`

          - `ToolUseID string`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `Type TextEditorCodeExecutionToolResult`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

        - `type BetaToolSearchToolResultBlockParamResp struct{…}`

          - `Content BetaToolSearchToolResultBlockParamContentUnionResp`

            - `type BetaToolSearchToolResultErrorParamResp struct{…}`

              - `ErrorCode BetaToolSearchToolResultErrorParamErrorCode`

                - `const BetaToolSearchToolResultErrorParamErrorCodeInvalidToolInput BetaToolSearchToolResultErrorParamErrorCode = "invalid_tool_input"`

                - `const BetaToolSearchToolResultErrorParamErrorCodeUnavailable BetaToolSearchToolResultErrorParamErrorCode = "unavailable"`

                - `const BetaToolSearchToolResultErrorParamErrorCodeTooManyRequests BetaToolSearchToolResultErrorParamErrorCode = "too_many_requests"`

                - `const BetaToolSearchToolResultErrorParamErrorCodeExecutionTimeExceeded BetaToolSearchToolResultErrorParamErrorCode = "execution_time_exceeded"`

              - `Type ToolSearchToolResultError`

              - `ErrorMessage string Optional`

            - `type BetaToolSearchToolSearchResultBlockParamResp struct{…}`

              - `ToolReferences []BetaToolReferenceBlockParamResp`

                - `ToolName string`

                  maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

                - `Type ToolReference`

                - `CacheControl BetaCacheControlEphemeral Optional`

                  Create a cache control breakpoint at this content block.

              - `Type ToolSearchToolSearchResult`

          - `ToolUseID string`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `Type ToolSearchToolResult`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

        - `type BetaMCPToolUseBlockParamResp struct{…}`

          - `ID string`

            pattern: ^[a-zA-Z0-9_-]+$

          - `Input map[string, any]`

          - `Name string`

          - `ServerName string`

            The name of the MCP server

          - `Type MCPToolUse`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

        - `type BetaRequestMCPToolResultBlockParamResp struct{…}`

          - `ToolUseID string`

            pattern: ^[a-zA-Z0-9_-]+$

          - `Type MCPToolResult`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `Content BetaRequestMCPToolResultBlockParamContentUnionResp Optional`

            - `string`

            - `[]BetaTextBlockParamResp`

              - `Text string`

                minLength: 1

              - `Type Text`

              - `CacheControl BetaCacheControlEphemeral Optional`

                Create a cache control breakpoint at this content block.

              - `Citations []BetaTextCitationParamUnionResp Optional`

          - `IsError bool Optional`

        - `type BetaContainerUploadBlockParamResp struct{…}`

          A content block that represents a file to be uploaded to the container
          Files uploaded via this block will be available in the container's input directory.

          - `FileID string`

          - `Type ContainerUpload`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

        - `type BetaCompactionBlockParamResp struct{…}`

          A compaction block containing summary of previous context.

          Users should round-trip these blocks from responses to subsequent requests
          to maintain context across compaction boundaries.

          When content is None, the block represents a failed compaction. The server
          treats these as no-ops. Empty string content is not allowed.

          - `Type Compaction`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

          - `Content string Optional`

            Summary of previously compacted content, or null if compaction failed

          - `EncryptedContent string Optional`

            Opaque metadata from prior compaction, to be round-tripped verbatim

        - `type BetaRequestToolAdditionBlock struct{…}`

          Mid-conversation directive to surface a declared tool.

          `tool` references a tool (or MCP toolset) by name from the request's
          `tools`; it is offered to the model from this point in the
          conversation onward.

          - `Tool BetaRequestToolAdditionBlockToolUnion`

            Reference to a single tool the caller declared directly in
            `tools[]`. Does not accept the composed `{server}_{name}` form the
            server assigns to MCP-resolved tools — use `mcp_tool_reference` or
            `mcp_toolset_reference` for those.

            - `type BetaToolChangeToolReference struct{…}`

              Reference to a single tool the caller declared directly in
              `tools[]`. Does not accept the composed `{server}_{name}` form the
              server assigns to MCP-resolved tools — use `mcp_tool_reference` or
              `mcp_toolset_reference` for those.

              - `Name string`

                pattern: ^[a-zA-Z0-9_-]{1,128}$

              - `Type ToolReference`

            - `type BetaToolChangeMCPToolReference struct{…}`

              Reference to a single MCP tool by its server and remote name — the
              same `server_name`/`name` pair `mcp_tool_use` carries.

              - `Name string`

              - `ServerName string`

              - `Type MCPToolReference`

            - `type BetaToolChangeMCPToolsetReference struct{…}`

              Reference to every tool in the named MCP server's toolset.

              - `ServerName string`

              - `Type MCPToolsetReference`

          - `Type ToolAddition`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

        - `type BetaRequestToolRemovalBlock struct{…}`

          Mid-conversation directive to withdraw a tool.

          `tool` references a tool (or MCP toolset) by name from the request's
          `tools`; it is no longer offered to the model from this point in the
          conversation onward.

          - `Tool BetaRequestToolRemovalBlockToolUnion`

            Reference to a single tool the caller declared directly in
            `tools[]`. Does not accept the composed `{server}_{name}` form the
            server assigns to MCP-resolved tools — use `mcp_tool_reference` or
            `mcp_toolset_reference` for those.

            - `type BetaToolChangeToolReference struct{…}`

              Reference to a single tool the caller declared directly in
              `tools[]`. Does not accept the composed `{server}_{name}` form the
              server assigns to MCP-resolved tools — use `mcp_tool_reference` or
              `mcp_toolset_reference` for those.

            - `type BetaToolChangeMCPToolReference struct{…}`

              Reference to a single MCP tool by its server and remote name — the
              same `server_name`/`name` pair `mcp_tool_use` carries.

            - `type BetaToolChangeMCPToolsetReference struct{…}`

              Reference to every tool in the named MCP server's toolset.

          - `Type ToolRemoval`

          - `CacheControl BetaCacheControlEphemeral Optional`

            Create a cache control breakpoint at this content block.

        - `type BetaFallbackBlockParamResp struct{…}`

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

          - `From BetaFallbackInfoParamResp`

            Identifies one hop of a fallback transition.

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

          - `To BetaFallbackInfoParamResp`

            Identifies one hop of a fallback transition.

          - `Type Fallback`

          - `Trigger any Optional`

            The response block's `trigger`, echoed verbatim. Accepted and ignored by the server; any object or `null` is allowed.

    - `Role BetaMessageParamRole`

      - `const BetaMessageParamRoleUser BetaMessageParamRole = "user"`

      - `const BetaMessageParamRoleAssistant BetaMessageParamRole = "assistant"`

      - `const BetaMessageParamRoleSystem BetaMessageParamRole = "system"`

  - `Model param.Field[Model]`

    Body param: The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `CacheControl param.Field[BetaCacheControlEphemeral] Optional`

    Body param: Top-level cache control automatically applies a cache_control marker to the last cacheable block in the request.

  - `Container param.Field[BetaMessageNewParamsContainerUnion] Optional`

    Body param: Container identifier for reuse across requests.

    - `type BetaContainerParamsResp struct{…}`

      Container parameters with skills to be loaded.

      - `ID string Optional`

        Container id

      - `Skills []BetaSkillParamsResp Optional`

        List of skills to load in the container

        maxItems: 20

        - `SkillID string`

          Skill ID

          maxLength: 64, minLength: 1

        - `Type BetaSkillParamsType`

          Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

          - `const BetaSkillParamsTypeAnthropic BetaSkillParamsType = "anthropic"`

          - `const BetaSkillParamsTypeCustom BetaSkillParamsType = "custom"`

        - `Version string Optional`

          Skill version or 'latest' for most recent version

          maxLength: 64, minLength: 1

    - `string`

  - `ContextManagement param.Field[BetaContextManagementConfig] Optional`

    Body param: Context management configuration.

    This allows you to control how Claude manages context across multiple requests, such as whether to clear function results or not.

  - `Diagnostics param.Field[BetaDiagnosticsParamResp] Optional`

    Body param: Request-level diagnostics. Currently carries the previous response
    id for prompt-cache divergence reporting.

  - `FallbackCreditToken param.Field[BetaMessageNewParamsFallbackCreditTokenUnion] Optional`

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

    - `type BetaFallbackCreditTokenParamResp struct{…}`

      Object form of `fallback_credit_token`: the token plus a redemption
      mode.

      Requires `anthropic-beta: fallback-credit-2026-07-01`; without that
      header the field accepts the bare string only. The bare string and the
      mode-less object are equivalent (both select `strict`), so wrapping
      an existing token changes nothing by itself.

      - `Token string`

        The opaque `fallback_credit_token` from a prior refusal's `stop_details` — the same string the bare-string form carries.

        maxLength: 2048, minLength: 1

      - `Mode BetaFallbackCreditTokenParamMode Optional`

        How a failing token affects the retry. `strict` (the default, and the bare-string behavior): a failing redemption is a 400 and the retry is not served. `best_effort`: the retry is served either way — a token-layer failure no longer rejects the request; the retry proceeds at normal price and the outcome is reported on the response's `usage.fallback_credit`. Two failures stay hard in both modes: a malformed token, and combining `fallback_credit_token` with `fallbacks`.

        - `const BetaFallbackCreditTokenParamModeStrict BetaFallbackCreditTokenParamMode = "strict"`

        - `const BetaFallbackCreditTokenParamModeBestEffort BetaFallbackCreditTokenParamMode = "best_effort"`

  - `Fallbacks param.Field[BetaFallbacksParamUnionResp] Optional`

    Body param: Opt-in server-side retry on one or more substitute models when the requested model declines for policy reasons. Tried in order: if the first entry also declines, the second is tried, and so on. The string "default" requests the requested model's server-defined default fallback configuration.

  - `InferenceGeo param.Field[string] Optional`

    Body param: Specifies the geographic region for inference processing. If not specified, the workspace's `default_inference_geo` is used.

  - `MCPServers param.Field[[]BetaRequestMCPServerURLDefinition] Optional`

    Body param: MCP servers to be utilized in this request

    maxItems: 20

    - `Name string`

    - `Type URL`

    - `URL string`

    - `AuthorizationToken string Optional`

    - `ToolConfiguration BetaRequestMCPServerToolConfiguration Optional`

      - `AllowedTools []string Optional`

      - `Enabled bool Optional`

  - `Metadata param.Field[BetaMetadata] Optional`

    Body param: An object describing metadata about the request.

  - `OutputConfig param.Field[BetaOutputConfig] Optional`

    Body param: Configuration options for the model's output, such as the output format.

  - `ServiceTier param.Field[BetaMessageNewParamsServiceTier] Optional`

    Body param: Determines whether to use priority capacity (if available) or standard capacity for this request.

    Anthropic offers different levels of service for your API requests. See [service-tiers](https://platform.claude.com/docs/en/api/service-tiers) for details.

    - `const BetaMessageNewParamsServiceTierAuto BetaMessageNewParamsServiceTier = "auto"`

    - `const BetaMessageNewParamsServiceTierStandardOnly BetaMessageNewParamsServiceTier = "standard_only"`

  - `Speed param.Field[BetaMessageNewParamsSpeed] Optional`

    Body param: Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `const BetaMessageNewParamsSpeedStandard BetaMessageNewParamsSpeed = "standard"`

    - `const BetaMessageNewParamsSpeedFast BetaMessageNewParamsSpeed = "fast"`

  - `StopSequences param.Field[[]string] Optional`

    Body param: Custom text sequences that will cause the model to stop generating.

    Our models will normally stop when they have naturally completed their turn, which will result in a response `stop_reason` of `"end_turn"`.

    If you want the model to stop generating when it encounters custom strings of text, you can use the `stop_sequences` parameter. If the model encounters one of the custom sequences, the response `stop_reason` value will be `"stop_sequence"` and the response `stop_sequence` value will contain the matched stop sequence.

  - `System param.Field[[]BetaTextBlockParamResp] Optional`

    Body param: System prompt.

    A system prompt is a way of providing context and instructions to Claude, such as specifying a particular goal or role. See our [guide to system prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#give-claude-a-role).

    - `[]BetaTextBlockParam`

      - `Text string`

        minLength: 1

      - `Type Text`

      - `CacheControl BetaCacheControlEphemeral Optional`

        Create a cache control breakpoint at this content block.

      - `Citations []BetaTextCitationParamUnionResp Optional`

  - `Thinking param.Field[BetaThinkingConfigParamUnionResp] Optional`

    Body param: Configuration for enabling Claude's extended thinking.

    When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

    See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

  - `ToolChoice param.Field[BetaToolChoiceUnion] Optional`

    Body param: How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

  - `Tools param.Field[[]BetaToolUnion] Optional`

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

    - `type BetaTool struct{…}`

      - `InputSchema BetaToolInputSchema`

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

        - `const BetaToolAllowedCallerDirect BetaToolAllowedCaller = "direct"`

        - `const BetaToolAllowedCallerCodeExecution20250825 BetaToolAllowedCaller = "code_execution_20250825"`

        - `const BetaToolAllowedCallerCodeExecution20260120 BetaToolAllowedCaller = "code_execution_20260120"`

        - `const BetaToolAllowedCallerCodeExecution20260521 BetaToolAllowedCaller = "code_execution_20260521"`

      - `CacheControl BetaCacheControlEphemeral Optional`

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

      - `Type BetaToolType Optional`

    - `type BetaToolBash20241022 struct{…}`

      - `Name Bash`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `Type Bash20241022`

      - `AllowedCallers []string Optional`

        - `const BetaToolBash20241022AllowedCallerDirect BetaToolBash20241022AllowedCaller = "direct"`

        - `const BetaToolBash20241022AllowedCallerCodeExecution20250825 BetaToolBash20241022AllowedCaller = "code_execution_20250825"`

        - `const BetaToolBash20241022AllowedCallerCodeExecution20260120 BetaToolBash20241022AllowedCaller = "code_execution_20260120"`

        - `const BetaToolBash20241022AllowedCallerCodeExecution20260521 BetaToolBash20241022AllowedCaller = "code_execution_20260521"`

      - `CacheControl BetaCacheControlEphemeral Optional`

        Create a cache control breakpoint at this content block.

      - `DeferLoading bool Optional`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `InputExamples []map[string, any] Optional`

      - `Strict bool Optional`

        When true, guarantees schema validation on tool names and inputs

    - `type BetaToolBash20250124 struct{…}`

      - `Name Bash`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `Type Bash20250124`

      - `AllowedCallers []string Optional`

        - `const BetaToolBash20250124AllowedCallerDirect BetaToolBash20250124AllowedCaller = "direct"`

        - `const BetaToolBash20250124AllowedCallerCodeExecution20250825 BetaToolBash20250124AllowedCaller = "code_execution_20250825"`

        - `const BetaToolBash20250124AllowedCallerCodeExecution20260120 BetaToolBash20250124AllowedCaller = "code_execution_20260120"`

        - `const BetaToolBash20250124AllowedCallerCodeExecution20260521 BetaToolBash20250124AllowedCaller = "code_execution_20260521"`

      - `CacheControl BetaCacheControlEphemeral Optional`

        Create a cache control breakpoint at this content block.

      - `DeferLoading bool Optional`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `InputExamples []map[string, any] Optional`

      - `Strict bool Optional`

        When true, guarantees schema validation on tool names and inputs

    - `type BetaCodeExecutionTool20250522 struct{…}`

      - `Name CodeExecution`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `Type CodeExecution20250522`

      - `AllowedCallers []string Optional`

        - `const BetaCodeExecutionTool20250522AllowedCallerDirect BetaCodeExecutionTool20250522AllowedCaller = "direct"`

        - `const BetaCodeExecutionTool20250522AllowedCallerCodeExecution20250825 BetaCodeExecutionTool20250522AllowedCaller = "code_execution_20250825"`

        - `const BetaCodeExecutionTool20250522AllowedCallerCodeExecution20260120 BetaCodeExecutionTool20250522AllowedCaller = "code_execution_20260120"`

        - `const BetaCodeExecutionTool20250522AllowedCallerCodeExecution20260521 BetaCodeExecutionTool20250522AllowedCaller = "code_execution_20260521"`

      - `CacheControl BetaCacheControlEphemeral Optional`

        Create a cache control breakpoint at this content block.

      - `DeferLoading bool Optional`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Strict bool Optional`

        When true, guarantees schema validation on tool names and inputs

    - `type BetaCodeExecutionTool20250825 struct{…}`

      - `Name CodeExecution`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `Type CodeExecution20250825`

      - `AllowedCallers []string Optional`

        - `const BetaCodeExecutionTool20250825AllowedCallerDirect BetaCodeExecutionTool20250825AllowedCaller = "direct"`

        - `const BetaCodeExecutionTool20250825AllowedCallerCodeExecution20250825 BetaCodeExecutionTool20250825AllowedCaller = "code_execution_20250825"`

        - `const BetaCodeExecutionTool20250825AllowedCallerCodeExecution20260120 BetaCodeExecutionTool20250825AllowedCaller = "code_execution_20260120"`

        - `const BetaCodeExecutionTool20250825AllowedCallerCodeExecution20260521 BetaCodeExecutionTool20250825AllowedCaller = "code_execution_20260521"`

      - `CacheControl BetaCacheControlEphemeral Optional`

        Create a cache control breakpoint at this content block.

      - `DeferLoading bool Optional`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Strict bool Optional`

        When true, guarantees schema validation on tool names and inputs

    - `type BetaCodeExecutionTool20260120 struct{…}`

      Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

      - `Name CodeExecution`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `Type CodeExecution20260120`

      - `AllowedCallers []string Optional`

        - `const BetaCodeExecutionTool20260120AllowedCallerDirect BetaCodeExecutionTool20260120AllowedCaller = "direct"`

        - `const BetaCodeExecutionTool20260120AllowedCallerCodeExecution20250825 BetaCodeExecutionTool20260120AllowedCaller = "code_execution_20250825"`

        - `const BetaCodeExecutionTool20260120AllowedCallerCodeExecution20260120 BetaCodeExecutionTool20260120AllowedCaller = "code_execution_20260120"`

        - `const BetaCodeExecutionTool20260120AllowedCallerCodeExecution20260521 BetaCodeExecutionTool20260120AllowedCaller = "code_execution_20260521"`

      - `CacheControl BetaCacheControlEphemeral Optional`

        Create a cache control breakpoint at this content block.

      - `DeferLoading bool Optional`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Strict bool Optional`

        When true, guarantees schema validation on tool names and inputs

    - `type BetaCodeExecutionTool20260521 struct{…}`

      Code execution tool with REPL state persistence.

      - `Name CodeExecution`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `Type CodeExecution20260521`

      - `AllowedCallers []string Optional`

        - `const BetaCodeExecutionTool20260521AllowedCallerDirect BetaCodeExecutionTool20260521AllowedCaller = "direct"`

        - `const BetaCodeExecutionTool20260521AllowedCallerCodeExecution20250825 BetaCodeExecutionTool20260521AllowedCaller = "code_execution_20250825"`

        - `const BetaCodeExecutionTool20260521AllowedCallerCodeExecution20260120 BetaCodeExecutionTool20260521AllowedCaller = "code_execution_20260120"`

        - `const BetaCodeExecutionTool20260521AllowedCallerCodeExecution20260521 BetaCodeExecutionTool20260521AllowedCaller = "code_execution_20260521"`

      - `CacheControl BetaCacheControlEphemeral Optional`

        Create a cache control breakpoint at this content block.

      - `DeferLoading bool Optional`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Strict bool Optional`

        When true, guarantees schema validation on tool names and inputs

    - `type BetaBrowserToolset20260801 struct{…}`

      The browser toolset: a single `tools[]` entry (carrying no
      `name`) that declares the browser tool family. The model is served
      the family's tool with any members disabled via `configs` removed
      from its schema.

      - `Type BrowserToolset20260801`

      - `AllowedCallers []string Optional`

        - `const BetaBrowserToolset20260801AllowedCallerDirect BetaBrowserToolset20260801AllowedCaller = "direct"`

        - `const BetaBrowserToolset20260801AllowedCallerCodeExecution20250825 BetaBrowserToolset20260801AllowedCaller = "code_execution_20250825"`

        - `const BetaBrowserToolset20260801AllowedCallerCodeExecution20260120 BetaBrowserToolset20260801AllowedCaller = "code_execution_20260120"`

        - `const BetaBrowserToolset20260801AllowedCallerCodeExecution20260521 BetaBrowserToolset20260801AllowedCaller = "code_execution_20260521"`

      - `CacheControl BetaCacheControlEphemeral Optional`

        Create a cache control breakpoint at this content block.

      - `Configs BetaBrowserToolsetConfigs Optional`

        Per-member configuration for `browser_toolset_20260801`: one
        optional field per member tool, keyed by the member name — the same
        name the member's `tool_use` blocks carry. Every member is an
        accepted key, and a member's defaults apply wherever its key is
        absent. Unknown keys are rejected: the field set is this toolset
        version's complete member set.

        - `CloseTab BetaBrowserCloseTabConfig Optional`

          `close_tab`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `DoubleClick BetaBrowserDoubleClickConfig Optional`

          `double_click`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `FileUpload BetaBrowserFileUploadConfig Optional`

          `file_upload`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Find BetaBrowserFindConfig Optional`

          `find`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `FormInput BetaBrowserFormInputConfig Optional`

          `form_input`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `GetPageText BetaBrowserGetPageTextConfig Optional`

          `get_page_text`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `HoldKey BetaBrowserHoldKeyConfig Optional`

          `hold_key`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Hover BetaBrowserHoverConfig Optional`

          `hover`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `JavascriptExec BetaBrowserJavascriptExecConfig Optional`

          `javascript_exec`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Key BetaBrowserKeyConfig Optional`

          `key`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `LeftClick BetaBrowserLeftClickConfig Optional`

          `left_click`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `LeftClickDrag BetaBrowserLeftClickDragConfig Optional`

          `left_click_drag`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `LeftMouseDown BetaBrowserLeftMouseDownConfig Optional`

          `left_mouse_down`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `LeftMouseUp BetaBrowserLeftMouseUpConfig Optional`

          `left_mouse_up`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `ListTabs BetaBrowserListTabsConfig Optional`

          `list_tabs`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `MiddleClick BetaBrowserMiddleClickConfig Optional`

          `middle_click`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `MouseMove BetaBrowserMouseMoveConfig Optional`

          `mouse_move`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Navigate BetaBrowserNavigateConfig Optional`

          `navigate`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `NewTab BetaBrowserNewTabConfig Optional`

          `new_tab`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `ReadConsole BetaBrowserReadConsoleConfig Optional`

          `read_console`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `ReadNetwork BetaBrowserReadNetworkConfig Optional`

          `read_network`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `ReadPage BetaBrowserReadPageConfig Optional`

          `read_page`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `RightClick BetaBrowserRightClickConfig Optional`

          `right_click`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Screenshot BetaBrowserScreenshotConfig Optional`

          `screenshot`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Scroll BetaBrowserScrollConfig Optional`

          `scroll`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `ScrollTo BetaBrowserScrollToConfig Optional`

          `scroll_to`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `SwitchTab BetaBrowserSwitchTabConfig Optional`

          `switch_tab`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `TripleClick BetaBrowserTripleClickConfig Optional`

          `triple_click`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Type BetaBrowserTypeConfig Optional`

          `type`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Wait BetaBrowserWaitConfig Optional`

          `wait`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Zoom BetaBrowserZoomConfig Optional`

          `zoom`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `type BetaToolComputerUse20241022 struct{…}`

      - `DisplayHeightPx int64`

        The height of the display in pixels.

        minimum: 1

      - `DisplayWidthPx int64`

        The width of the display in pixels.

        minimum: 1

      - `Name Computer`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `Type Computer20241022`

      - `AllowedCallers []string Optional`

        - `const BetaToolComputerUse20241022AllowedCallerDirect BetaToolComputerUse20241022AllowedCaller = "direct"`

        - `const BetaToolComputerUse20241022AllowedCallerCodeExecution20250825 BetaToolComputerUse20241022AllowedCaller = "code_execution_20250825"`

        - `const BetaToolComputerUse20241022AllowedCallerCodeExecution20260120 BetaToolComputerUse20241022AllowedCaller = "code_execution_20260120"`

        - `const BetaToolComputerUse20241022AllowedCallerCodeExecution20260521 BetaToolComputerUse20241022AllowedCaller = "code_execution_20260521"`

      - `CacheControl BetaCacheControlEphemeral Optional`

        Create a cache control breakpoint at this content block.

      - `DeferLoading bool Optional`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `DisplayNumber int64 Optional`

        The X11 display number (e.g. 0, 1) for the display.

        minimum: 0

      - `InputExamples []map[string, any] Optional`

      - `Strict bool Optional`

        When true, guarantees schema validation on tool names and inputs

    - `type BetaMemoryTool20250818 struct{…}`

      - `Name Memory`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `Type Memory20250818`

      - `AllowedCallers []string Optional`

        - `const BetaMemoryTool20250818AllowedCallerDirect BetaMemoryTool20250818AllowedCaller = "direct"`

        - `const BetaMemoryTool20250818AllowedCallerCodeExecution20250825 BetaMemoryTool20250818AllowedCaller = "code_execution_20250825"`

        - `const BetaMemoryTool20250818AllowedCallerCodeExecution20260120 BetaMemoryTool20250818AllowedCaller = "code_execution_20260120"`

        - `const BetaMemoryTool20250818AllowedCallerCodeExecution20260521 BetaMemoryTool20250818AllowedCaller = "code_execution_20260521"`

      - `CacheControl BetaCacheControlEphemeral Optional`

        Create a cache control breakpoint at this content block.

      - `DeferLoading bool Optional`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `InputExamples []map[string, any] Optional`

      - `Strict bool Optional`

        When true, guarantees schema validation on tool names and inputs

    - `type BetaToolComputerUse20250124 struct{…}`

      - `DisplayHeightPx int64`

        The height of the display in pixels.

        minimum: 1

      - `DisplayWidthPx int64`

        The width of the display in pixels.

        minimum: 1

      - `Name Computer`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `Type Computer20250124`

      - `AllowedCallers []string Optional`

        - `const BetaToolComputerUse20250124AllowedCallerDirect BetaToolComputerUse20250124AllowedCaller = "direct"`

        - `const BetaToolComputerUse20250124AllowedCallerCodeExecution20250825 BetaToolComputerUse20250124AllowedCaller = "code_execution_20250825"`

        - `const BetaToolComputerUse20250124AllowedCallerCodeExecution20260120 BetaToolComputerUse20250124AllowedCaller = "code_execution_20260120"`

        - `const BetaToolComputerUse20250124AllowedCallerCodeExecution20260521 BetaToolComputerUse20250124AllowedCaller = "code_execution_20260521"`

      - `CacheControl BetaCacheControlEphemeral Optional`

        Create a cache control breakpoint at this content block.

      - `DeferLoading bool Optional`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `DisplayNumber int64 Optional`

        The X11 display number (e.g. 0, 1) for the display.

        minimum: 0

      - `InputExamples []map[string, any] Optional`

      - `Strict bool Optional`

        When true, guarantees schema validation on tool names and inputs

    - `type BetaToolTextEditor20241022 struct{…}`

      - `Name StrReplaceEditor`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `Type TextEditor20241022`

      - `AllowedCallers []string Optional`

        - `const BetaToolTextEditor20241022AllowedCallerDirect BetaToolTextEditor20241022AllowedCaller = "direct"`

        - `const BetaToolTextEditor20241022AllowedCallerCodeExecution20250825 BetaToolTextEditor20241022AllowedCaller = "code_execution_20250825"`

        - `const BetaToolTextEditor20241022AllowedCallerCodeExecution20260120 BetaToolTextEditor20241022AllowedCaller = "code_execution_20260120"`

        - `const BetaToolTextEditor20241022AllowedCallerCodeExecution20260521 BetaToolTextEditor20241022AllowedCaller = "code_execution_20260521"`

      - `CacheControl BetaCacheControlEphemeral Optional`

        Create a cache control breakpoint at this content block.

      - `DeferLoading bool Optional`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `InputExamples []map[string, any] Optional`

      - `Strict bool Optional`

        When true, guarantees schema validation on tool names and inputs

    - `type BetaToolComputerUse20251124 struct{…}`

      - `DisplayHeightPx int64`

        The height of the display in pixels.

        minimum: 1

      - `DisplayWidthPx int64`

        The width of the display in pixels.

        minimum: 1

      - `Name Computer`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `Type Computer20251124`

      - `AllowedCallers []string Optional`

        - `const BetaToolComputerUse20251124AllowedCallerDirect BetaToolComputerUse20251124AllowedCaller = "direct"`

        - `const BetaToolComputerUse20251124AllowedCallerCodeExecution20250825 BetaToolComputerUse20251124AllowedCaller = "code_execution_20250825"`

        - `const BetaToolComputerUse20251124AllowedCallerCodeExecution20260120 BetaToolComputerUse20251124AllowedCaller = "code_execution_20260120"`

        - `const BetaToolComputerUse20251124AllowedCallerCodeExecution20260521 BetaToolComputerUse20251124AllowedCaller = "code_execution_20260521"`

      - `CacheControl BetaCacheControlEphemeral Optional`

        Create a cache control breakpoint at this content block.

      - `DeferLoading bool Optional`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `DisplayNumber int64 Optional`

        The X11 display number (e.g. 0, 1) for the display.

        minimum: 0

      - `EnableZoom bool Optional`

        Whether to enable an action to take a zoomed-in screenshot of the screen.

      - `InputExamples []map[string, any] Optional`

      - `Strict bool Optional`

        When true, guarantees schema validation on tool names and inputs

    - `type BetaComputerToolset20260801 struct{…}`

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

        - `const BetaComputerToolset20260801AllowedCallerDirect BetaComputerToolset20260801AllowedCaller = "direct"`

        - `const BetaComputerToolset20260801AllowedCallerCodeExecution20250825 BetaComputerToolset20260801AllowedCaller = "code_execution_20250825"`

        - `const BetaComputerToolset20260801AllowedCallerCodeExecution20260120 BetaComputerToolset20260801AllowedCaller = "code_execution_20260120"`

        - `const BetaComputerToolset20260801AllowedCallerCodeExecution20260521 BetaComputerToolset20260801AllowedCaller = "code_execution_20260521"`

      - `CacheControl BetaCacheControlEphemeral Optional`

        Create a cache control breakpoint at this content block.

      - `Configs BetaComputerToolsetConfigs Optional`

        Per-member configuration for `computer_toolset_20260801`: one
        optional field per member tool, keyed by the member name — the same
        name the member's `tool_use` blocks carry. Every member is an
        accepted key, and a member's defaults apply wherever its key is
        absent. Unknown keys are rejected: the field set is this toolset
        version's complete member set.

        - `CursorPosition BetaComputerCursorPositionConfig Optional`

          `cursor_position`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `DoubleClick BetaComputerDoubleClickConfig Optional`

          `double_click`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `HoldKey BetaComputerHoldKeyConfig Optional`

          `hold_key`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Key BetaComputerKeyConfig Optional`

          `key`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `LeftClick BetaComputerLeftClickConfig Optional`

          `left_click`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `LeftClickDrag BetaComputerLeftClickDragConfig Optional`

          `left_click_drag`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `LeftMouseDown BetaComputerLeftMouseDownConfig Optional`

          `left_mouse_down`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `LeftMouseUp BetaComputerLeftMouseUpConfig Optional`

          `left_mouse_up`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `MiddleClick BetaComputerMiddleClickConfig Optional`

          `middle_click`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `MouseMove BetaComputerMouseMoveConfig Optional`

          `mouse_move`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `RightClick BetaComputerRightClickConfig Optional`

          `right_click`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Screenshot BetaComputerScreenshotConfig Optional`

          `screenshot`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Scroll BetaComputerScrollConfig Optional`

          `scroll`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `TripleClick BetaComputerTripleClickConfig Optional`

          `triple_click`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Type BetaComputerTypeConfig Optional`

          `type`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Wait BetaComputerWaitConfig Optional`

          `wait`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

        - `Zoom BetaComputerZoomConfig Optional`

          `zoom`'s config overrides.

          - `DeferLoading bool Optional`

            Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

          - `Enabled bool Optional`

            Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.

    - `type BetaToolTextEditor20250124 struct{…}`

      - `Name StrReplaceEditor`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `Type TextEditor20250124`

      - `AllowedCallers []string Optional`

        - `const BetaToolTextEditor20250124AllowedCallerDirect BetaToolTextEditor20250124AllowedCaller = "direct"`

        - `const BetaToolTextEditor20250124AllowedCallerCodeExecution20250825 BetaToolTextEditor20250124AllowedCaller = "code_execution_20250825"`

        - `const BetaToolTextEditor20250124AllowedCallerCodeExecution20260120 BetaToolTextEditor20250124AllowedCaller = "code_execution_20260120"`

        - `const BetaToolTextEditor20250124AllowedCallerCodeExecution20260521 BetaToolTextEditor20250124AllowedCaller = "code_execution_20260521"`

      - `CacheControl BetaCacheControlEphemeral Optional`

        Create a cache control breakpoint at this content block.

      - `DeferLoading bool Optional`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `InputExamples []map[string, any] Optional`

      - `Strict bool Optional`

        When true, guarantees schema validation on tool names and inputs

    - `type BetaToolTextEditor20250429 struct{…}`

      - `Name StrReplaceBasedEditTool`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `Type TextEditor20250429`

      - `AllowedCallers []string Optional`

        - `const BetaToolTextEditor20250429AllowedCallerDirect BetaToolTextEditor20250429AllowedCaller = "direct"`

        - `const BetaToolTextEditor20250429AllowedCallerCodeExecution20250825 BetaToolTextEditor20250429AllowedCaller = "code_execution_20250825"`

        - `const BetaToolTextEditor20250429AllowedCallerCodeExecution20260120 BetaToolTextEditor20250429AllowedCaller = "code_execution_20260120"`

        - `const BetaToolTextEditor20250429AllowedCallerCodeExecution20260521 BetaToolTextEditor20250429AllowedCaller = "code_execution_20260521"`

      - `CacheControl BetaCacheControlEphemeral Optional`

        Create a cache control breakpoint at this content block.

      - `DeferLoading bool Optional`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `InputExamples []map[string, any] Optional`

      - `Strict bool Optional`

        When true, guarantees schema validation on tool names and inputs

    - `type BetaToolTextEditor20250728 struct{…}`

      - `Name StrReplaceBasedEditTool`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `Type TextEditor20250728`

      - `AllowedCallers []string Optional`

        - `const BetaToolTextEditor20250728AllowedCallerDirect BetaToolTextEditor20250728AllowedCaller = "direct"`

        - `const BetaToolTextEditor20250728AllowedCallerCodeExecution20250825 BetaToolTextEditor20250728AllowedCaller = "code_execution_20250825"`

        - `const BetaToolTextEditor20250728AllowedCallerCodeExecution20260120 BetaToolTextEditor20250728AllowedCaller = "code_execution_20260120"`

        - `const BetaToolTextEditor20250728AllowedCallerCodeExecution20260521 BetaToolTextEditor20250728AllowedCaller = "code_execution_20260521"`

      - `CacheControl BetaCacheControlEphemeral Optional`

        Create a cache control breakpoint at this content block.

      - `DeferLoading bool Optional`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `InputExamples []map[string, any] Optional`

      - `MaxCharacters int64 Optional`

        Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

        minimum: 1

      - `Strict bool Optional`

        When true, guarantees schema validation on tool names and inputs

    - `type BetaWebSearchTool20250305 struct{…}`

      - `Name WebSearch`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `Type WebSearch20250305`

      - `AllowedCallers []string Optional`

        - `const BetaWebSearchTool20250305AllowedCallerDirect BetaWebSearchTool20250305AllowedCaller = "direct"`

        - `const BetaWebSearchTool20250305AllowedCallerCodeExecution20250825 BetaWebSearchTool20250305AllowedCaller = "code_execution_20250825"`

        - `const BetaWebSearchTool20250305AllowedCallerCodeExecution20260120 BetaWebSearchTool20250305AllowedCaller = "code_execution_20260120"`

        - `const BetaWebSearchTool20250305AllowedCallerCodeExecution20260521 BetaWebSearchTool20250305AllowedCaller = "code_execution_20260521"`

      - `AllowedDomains []string Optional`

        If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

      - `BlockedDomains []string Optional`

        If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

      - `CacheControl BetaCacheControlEphemeral Optional`

        Create a cache control breakpoint at this content block.

      - `DeferLoading bool Optional`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `MaxUses int64 Optional`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `Strict bool Optional`

        When true, guarantees schema validation on tool names and inputs

      - `UserLocation BetaUserLocation Optional`

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

    - `type BetaWebFetchTool20250910 struct{…}`

      - `Name WebFetch`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `Type WebFetch20250910`

      - `AllowedCallers []string Optional`

        - `const BetaWebFetchTool20250910AllowedCallerDirect BetaWebFetchTool20250910AllowedCaller = "direct"`

        - `const BetaWebFetchTool20250910AllowedCallerCodeExecution20250825 BetaWebFetchTool20250910AllowedCaller = "code_execution_20250825"`

        - `const BetaWebFetchTool20250910AllowedCallerCodeExecution20260120 BetaWebFetchTool20250910AllowedCaller = "code_execution_20260120"`

        - `const BetaWebFetchTool20250910AllowedCallerCodeExecution20260521 BetaWebFetchTool20250910AllowedCaller = "code_execution_20260521"`

      - `AllowedDomains []string Optional`

        List of domains to allow fetching from

      - `BlockedDomains []string Optional`

        List of domains to block fetching from

      - `CacheControl BetaCacheControlEphemeral Optional`

        Create a cache control breakpoint at this content block.

      - `Citations BetaCitationsConfigParamResp Optional`

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

    - `type BetaWebSearchTool20260209 struct{…}`

      - `Name WebSearch`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `Type WebSearch20260209`

      - `AllowedCallers []string Optional`

        - `const BetaWebSearchTool20260209AllowedCallerDirect BetaWebSearchTool20260209AllowedCaller = "direct"`

        - `const BetaWebSearchTool20260209AllowedCallerCodeExecution20250825 BetaWebSearchTool20260209AllowedCaller = "code_execution_20250825"`

        - `const BetaWebSearchTool20260209AllowedCallerCodeExecution20260120 BetaWebSearchTool20260209AllowedCaller = "code_execution_20260120"`

        - `const BetaWebSearchTool20260209AllowedCallerCodeExecution20260521 BetaWebSearchTool20260209AllowedCaller = "code_execution_20260521"`

      - `AllowedDomains []string Optional`

        If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

      - `BlockedDomains []string Optional`

        If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

      - `CacheControl BetaCacheControlEphemeral Optional`

        Create a cache control breakpoint at this content block.

      - `DeferLoading bool Optional`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `MaxUses int64 Optional`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `Strict bool Optional`

        When true, guarantees schema validation on tool names and inputs

      - `UserLocation BetaUserLocation Optional`

        Parameters for the user's location. Used to provide more relevant search results.

    - `type BetaWebFetchTool20260209 struct{…}`

      - `Name WebFetch`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `Type WebFetch20260209`

      - `AllowedCallers []string Optional`

        - `const BetaWebFetchTool20260209AllowedCallerDirect BetaWebFetchTool20260209AllowedCaller = "direct"`

        - `const BetaWebFetchTool20260209AllowedCallerCodeExecution20250825 BetaWebFetchTool20260209AllowedCaller = "code_execution_20250825"`

        - `const BetaWebFetchTool20260209AllowedCallerCodeExecution20260120 BetaWebFetchTool20260209AllowedCaller = "code_execution_20260120"`

        - `const BetaWebFetchTool20260209AllowedCallerCodeExecution20260521 BetaWebFetchTool20260209AllowedCaller = "code_execution_20260521"`

      - `AllowedDomains []string Optional`

        List of domains to allow fetching from

      - `BlockedDomains []string Optional`

        List of domains to block fetching from

      - `CacheControl BetaCacheControlEphemeral Optional`

        Create a cache control breakpoint at this content block.

      - `Citations BetaCitationsConfigParamResp Optional`

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

    - `type BetaWebFetchTool20260309 struct{…}`

      Web fetch tool with use_cache parameter for bypassing cached content.

      - `Name WebFetch`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `Type WebFetch20260309`

      - `AllowedCallers []string Optional`

        - `const BetaWebFetchTool20260309AllowedCallerDirect BetaWebFetchTool20260309AllowedCaller = "direct"`

        - `const BetaWebFetchTool20260309AllowedCallerCodeExecution20250825 BetaWebFetchTool20260309AllowedCaller = "code_execution_20250825"`

        - `const BetaWebFetchTool20260309AllowedCallerCodeExecution20260120 BetaWebFetchTool20260309AllowedCaller = "code_execution_20260120"`

        - `const BetaWebFetchTool20260309AllowedCallerCodeExecution20260521 BetaWebFetchTool20260309AllowedCaller = "code_execution_20260521"`

      - `AllowedDomains []string Optional`

        List of domains to allow fetching from

      - `BlockedDomains []string Optional`

        List of domains to block fetching from

      - `CacheControl BetaCacheControlEphemeral Optional`

        Create a cache control breakpoint at this content block.

      - `Citations BetaCitationsConfigParamResp Optional`

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

    - `type BetaWebSearchTool20260318 struct{…}`

      - `Name WebSearch`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `Type WebSearch20260318`

      - `AllowedCallers []string Optional`

        - `const BetaWebSearchTool20260318AllowedCallerDirect BetaWebSearchTool20260318AllowedCaller = "direct"`

        - `const BetaWebSearchTool20260318AllowedCallerCodeExecution20250825 BetaWebSearchTool20260318AllowedCaller = "code_execution_20250825"`

        - `const BetaWebSearchTool20260318AllowedCallerCodeExecution20260120 BetaWebSearchTool20260318AllowedCaller = "code_execution_20260120"`

        - `const BetaWebSearchTool20260318AllowedCallerCodeExecution20260521 BetaWebSearchTool20260318AllowedCaller = "code_execution_20260521"`

      - `AllowedDomains []string Optional`

        If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

      - `BlockedDomains []string Optional`

        If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

      - `CacheControl BetaCacheControlEphemeral Optional`

        Create a cache control breakpoint at this content block.

      - `DeferLoading bool Optional`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `MaxUses int64 Optional`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `ResponseInclusion BetaWebSearchTool20260318ResponseInclusion Optional`

        How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

        - `const BetaWebSearchTool20260318ResponseInclusionFull BetaWebSearchTool20260318ResponseInclusion = "full"`

        - `const BetaWebSearchTool20260318ResponseInclusionExcluded BetaWebSearchTool20260318ResponseInclusion = "excluded"`

      - `Strict bool Optional`

        When true, guarantees schema validation on tool names and inputs

      - `UserLocation BetaUserLocation Optional`

        Parameters for the user's location. Used to provide more relevant search results.

    - `type BetaWebFetchTool20260318 struct{…}`

      - `Name WebFetch`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `Type WebFetch20260318`

      - `AllowedCallers []string Optional`

        - `const BetaWebFetchTool20260318AllowedCallerDirect BetaWebFetchTool20260318AllowedCaller = "direct"`

        - `const BetaWebFetchTool20260318AllowedCallerCodeExecution20250825 BetaWebFetchTool20260318AllowedCaller = "code_execution_20250825"`

        - `const BetaWebFetchTool20260318AllowedCallerCodeExecution20260120 BetaWebFetchTool20260318AllowedCaller = "code_execution_20260120"`

        - `const BetaWebFetchTool20260318AllowedCallerCodeExecution20260521 BetaWebFetchTool20260318AllowedCaller = "code_execution_20260521"`

      - `AllowedDomains []string Optional`

        List of domains to allow fetching from

      - `BlockedDomains []string Optional`

        List of domains to block fetching from

      - `CacheControl BetaCacheControlEphemeral Optional`

        Create a cache control breakpoint at this content block.

      - `Citations BetaCitationsConfigParamResp Optional`

        Citations configuration for fetched documents. Citations are disabled by default.

      - `DeferLoading bool Optional`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `MaxContentTokens int64 Optional`

        Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

        exclusiveMinimum: 0

      - `MaxUses int64 Optional`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `ResponseInclusion BetaWebFetchTool20260318ResponseInclusion Optional`

        How this tool's result blocks appear in the API response when the result was consumed by a completed code_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server_tool_use and result block pair entirely. Results from direct calls, or from code_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

        - `const BetaWebFetchTool20260318ResponseInclusionFull BetaWebFetchTool20260318ResponseInclusion = "full"`

        - `const BetaWebFetchTool20260318ResponseInclusionExcluded BetaWebFetchTool20260318ResponseInclusion = "excluded"`

      - `Strict bool Optional`

        When true, guarantees schema validation on tool names and inputs

      - `UseCache bool Optional`

        Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

    - `type BetaAdvisorTool20260301 struct{…}`

      - `Model Model`

        The model that will complete your prompt.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `Name Advisor`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `Type Advisor20260301`

      - `AllowedCallers []string Optional`

        - `const BetaAdvisorTool20260301AllowedCallerDirect BetaAdvisorTool20260301AllowedCaller = "direct"`

        - `const BetaAdvisorTool20260301AllowedCallerCodeExecution20250825 BetaAdvisorTool20260301AllowedCaller = "code_execution_20250825"`

        - `const BetaAdvisorTool20260301AllowedCallerCodeExecution20260120 BetaAdvisorTool20260301AllowedCaller = "code_execution_20260120"`

        - `const BetaAdvisorTool20260301AllowedCallerCodeExecution20260521 BetaAdvisorTool20260301AllowedCaller = "code_execution_20260521"`

      - `CacheControl BetaCacheControlEphemeral Optional`

        Create a cache control breakpoint at this content block.

      - `Caching BetaCacheControlEphemeral Optional`

        Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

      - `DeferLoading bool Optional`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `MaxTokens int64 Optional`

        Bounds the advisor's total output (thinking + text) per call. When the advisor hits this cap, the returned advisor_result or advisor_redacted_result block carries stop_reason='max_tokens', and a truncation note is appended to the advice text the worker model sees (inside the encrypted blob in redacted mode). When set, the server also emits a remaining-tokens budget block in the advisor's prompt so the advisor self-shapes toward the cap. When omitted, the advisor model's default output cap applies and no budget block is emitted.

        minimum: 1024

      - `MaxUses int64 Optional`

        Maximum number of times the tool can be used in the API request.

        exclusiveMinimum: 0

      - `Strict bool Optional`

        When true, guarantees schema validation on tool names and inputs

    - `type BetaToolSearchToolBm25_20251119 struct{…}`

      - `Name ToolSearchToolBm25`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `Type BetaToolSearchToolBm25_20251119Type`

        - `const BetaToolSearchToolBm25_20251119TypeToolSearchToolBm25_20251119 BetaToolSearchToolBm25_20251119Type = "tool_search_tool_bm25_20251119"`

        - `const BetaToolSearchToolBm25_20251119TypeToolSearchToolBm25 BetaToolSearchToolBm25_20251119Type = "tool_search_tool_bm25"`

      - `AllowedCallers []string Optional`

        - `const BetaToolSearchToolBm25_20251119AllowedCallerDirect BetaToolSearchToolBm25_20251119AllowedCaller = "direct"`

        - `const BetaToolSearchToolBm25_20251119AllowedCallerCodeExecution20250825 BetaToolSearchToolBm25_20251119AllowedCaller = "code_execution_20250825"`

        - `const BetaToolSearchToolBm25_20251119AllowedCallerCodeExecution20260120 BetaToolSearchToolBm25_20251119AllowedCaller = "code_execution_20260120"`

        - `const BetaToolSearchToolBm25_20251119AllowedCallerCodeExecution20260521 BetaToolSearchToolBm25_20251119AllowedCaller = "code_execution_20260521"`

      - `CacheControl BetaCacheControlEphemeral Optional`

        Create a cache control breakpoint at this content block.

      - `DeferLoading bool Optional`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Strict bool Optional`

        When true, guarantees schema validation on tool names and inputs

    - `type BetaToolSearchToolRegex20251119 struct{…}`

      - `Name ToolSearchToolRegex`

        Name of the tool.

        This is how the tool will be called by the model and in `tool_use` blocks.

      - `Type BetaToolSearchToolRegex20251119Type`

        - `const BetaToolSearchToolRegex20251119TypeToolSearchToolRegex20251119 BetaToolSearchToolRegex20251119Type = "tool_search_tool_regex_20251119"`

        - `const BetaToolSearchToolRegex20251119TypeToolSearchToolRegex BetaToolSearchToolRegex20251119Type = "tool_search_tool_regex"`

      - `AllowedCallers []string Optional`

        - `const BetaToolSearchToolRegex20251119AllowedCallerDirect BetaToolSearchToolRegex20251119AllowedCaller = "direct"`

        - `const BetaToolSearchToolRegex20251119AllowedCallerCodeExecution20250825 BetaToolSearchToolRegex20251119AllowedCaller = "code_execution_20250825"`

        - `const BetaToolSearchToolRegex20251119AllowedCallerCodeExecution20260120 BetaToolSearchToolRegex20251119AllowedCaller = "code_execution_20260120"`

        - `const BetaToolSearchToolRegex20251119AllowedCallerCodeExecution20260521 BetaToolSearchToolRegex20251119AllowedCaller = "code_execution_20260521"`

      - `CacheControl BetaCacheControlEphemeral Optional`

        Create a cache control breakpoint at this content block.

      - `DeferLoading bool Optional`

        If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

      - `Strict bool Optional`

        When true, guarantees schema validation on tool names and inputs

    - `type BetaMCPToolset struct{…}`

      Configuration for a group of tools from an MCP server.

      Allows configuring enabled status and defer_loading for all tools
      from an MCP server, with optional per-tool overrides.

      - `MCPServerName string`

        Name of the MCP server to configure tools for

        maxLength: 255, minLength: 1

      - `Type MCPToolset`

      - `CacheControl BetaCacheControlEphemeral Optional`

        Create a cache control breakpoint at this content block.

      - `Configs map[string, BetaMCPToolConfig] Optional`

        Configuration overrides for specific tools, keyed by tool name

        - `DeferLoading bool Optional`

        - `Enabled bool Optional`

      - `DefaultConfig BetaMCPToolDefaultConfig Optional`

        Default configuration applied to all tools from this server

        - `DeferLoading bool Optional`

        - `Enabled bool Optional`

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

      - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

      - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

      - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

      - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

      - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

      - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

      - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

      - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

  - `UserProfileID param.Field[string] Optional`

    Header param: The user profile ID to attribute this request to. Use when acting on behalf of a party other than your organization. Requires the `user-profiles` beta header.

  - `OutputFormat param.Field[BetaJSONOutputFormat] Optional`

    **Deprecated**

    Body param: Deprecated: Use `output_config.format` instead. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

    A schema to specify Claude's output format in responses. This parameter will be removed in a future release.

  - `Temperature param.Field[float64] Optional`

    **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not support setting temperature. A value of 1.0 of will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

    Body param: Amount of randomness injected into the response.

    Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

    Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

    maximum: 1, minimum: 0

  - `TopK param.Field[int64] Optional`

    **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not accept top_k; any value will be rejected with a 400 error.

    Body param: Only sample from the top K options for each subsequent token.

    Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

    Recommended for advanced use cases only.

    minimum: 0

  - `TopP param.Field[float64] Optional`

    **Deprecated**: Deprecated. Models released after Claude Opus 4.6 do not support setting top_p. A value >= 0.99 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

    Body param: Use nucleus sampling.

    In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.

    Recommended for advanced use cases only.

    maximum: 1, minimum: 0

## Returns

- `type BetaMessage struct{…}`

  - `ID string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `Container BetaContainer`

    Information about the container used in the request (for the code execution tool)

    - `ID string`

      Identifier for the container used in this request

    - `ExpiresAt Time`

      The time at which the container will expire.

      format: date-time

    - `Skills []BetaSkill`

      Skills loaded in the container

      - `SkillID string`

        Skill ID

        maxLength: 64, minLength: 1

      - `Type BetaSkillType`

        Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

        - `const BetaSkillTypeAnthropic BetaSkillType = "anthropic"`

        - `const BetaSkillTypeCustom BetaSkillType = "custom"`

      - `Version string`

        The resolved version: a skill version ID for custom skills.

        maxLength: 64, minLength: 1

  - `Content []BetaContentBlockUnion`

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

    - `type BetaTextBlock struct{…}`

      - `Citations []BetaTextCitationUnion`

        Citations supporting the text block.

        The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

        - `type BetaCitationCharLocation struct{…}`

          - `CitedText string`

          - `DocumentIndex int64`

            minimum: 0

          - `DocumentTitle string`

          - `EndCharIndex int64`

          - `FileID string`

          - `StartCharIndex int64`

            minimum: 0

          - `Type CharLocation`

            default: char_location

        - `type BetaCitationPageLocation struct{…}`

          - `CitedText string`

          - `DocumentIndex int64`

            minimum: 0

          - `DocumentTitle string`

          - `EndPageNumber int64`

          - `FileID string`

          - `StartPageNumber int64`

            minimum: 1

          - `Type PageLocation`

            default: page_location

        - `type BetaCitationContentBlockLocation struct{…}`

          - `CitedText string`

            The full text of the cited block range, concatenated.

            Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

          - `DocumentIndex int64`

            minimum: 0

          - `DocumentTitle string`

          - `EndBlockIndex int64`

            Exclusive 0-based end index of the cited block range in the source's `content` array.

            Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

          - `FileID string`

          - `StartBlockIndex int64`

            0-based index of the first cited block in the source's `content` array.

            minimum: 0

          - `Type ContentBlockLocation`

            default: content_block_location

        - `type BetaCitationsWebSearchResultLocation struct{…}`

          - `CitedText string`

          - `EncryptedIndex string`

          - `Title string`

            maxLength: 512

          - `Type WebSearchResultLocation`

            default: web_search_result_location

          - `URL string`

        - `type BetaCitationSearchResultLocation struct{…}`

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

            default: search_result_location

      - `Text string`

        maxLength: 5000000, minLength: 0

      - `Type Text`

        default: text

    - `type BetaThinkingBlock struct{…}`

      - `Signature string`

        A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

        This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

        See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

      - `Thinking string`

        The text of Claude's thinking process for this block.

      - `Type Thinking`

        default: thinking

    - `type BetaRedactedThinkingBlock struct{…}`

      - `Data string`

        The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

        Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

        See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.

      - `Type RedactedThinking`

        default: redacted_thinking

    - `type BetaToolUseBlock struct{…}`

      - `ID string`

        pattern: ^[a-zA-Z0-9_-]+$

      - `Input map[string, any]`

      - `Name string`

        minLength: 1

      - `Type ToolUse`

        default: tool_use

      - `Caller BetaToolUseBlockCallerUnion Optional`

        Tool invocation directly from the model.

        - `type BetaDirectCaller struct{…}`

          Tool invocation directly from the model.

          - `Type Direct`

        - `type BetaServerToolCaller struct{…}`

          Tool invocation generated by a server-side tool.

          - `ToolID string`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `Type CodeExecution20250825`

        - `type BetaServerToolCaller20260120 struct{…}`

          - `ToolID string`

            pattern: ^srvtoolu_[a-zA-Z0-9_]+$

          - `Type CodeExecution20260120`

      - `ToolsetName string Optional`

        For a toolset member tool_use, the toolset family.

        maxLength: 64, minLength: 1, pattern: ^[a-zA-Z0-9_-]+$

    - `type BetaServerToolUseBlock struct{…}`

      - `ID string`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `Input map[string, any]`

      - `Name BetaServerToolUseBlockName`

        - `const BetaServerToolUseBlockNameAdvisor BetaServerToolUseBlockName = "advisor"`

        - `const BetaServerToolUseBlockNameWebSearch BetaServerToolUseBlockName = "web_search"`

        - `const BetaServerToolUseBlockNameWebFetch BetaServerToolUseBlockName = "web_fetch"`

        - `const BetaServerToolUseBlockNameCodeExecution BetaServerToolUseBlockName = "code_execution"`

        - `const BetaServerToolUseBlockNameBashCodeExecution BetaServerToolUseBlockName = "bash_code_execution"`

        - `const BetaServerToolUseBlockNameTextEditorCodeExecution BetaServerToolUseBlockName = "text_editor_code_execution"`

        - `const BetaServerToolUseBlockNameToolSearchToolRegex BetaServerToolUseBlockName = "tool_search_tool_regex"`

        - `const BetaServerToolUseBlockNameToolSearchToolBm25 BetaServerToolUseBlockName = "tool_search_tool_bm25"`

      - `Type ServerToolUse`

        default: server_tool_use

      - `Caller BetaServerToolUseBlockCallerUnion Optional`

        Tool invocation directly from the model.

        - `type BetaDirectCaller struct{…}`

          Tool invocation directly from the model.

        - `type BetaServerToolCaller struct{…}`

          Tool invocation generated by a server-side tool.

        - `type BetaServerToolCaller20260120 struct{…}`

    - `type BetaWebSearchToolResultBlock struct{…}`

      - `Content BetaWebSearchToolResultBlockContentUnion`

        - `type BetaWebSearchToolResultError struct{…}`

          - `ErrorCode BetaWebSearchToolResultErrorCode`

            - `const BetaWebSearchToolResultErrorCodeInvalidToolInput BetaWebSearchToolResultErrorCode = "invalid_tool_input"`

            - `const BetaWebSearchToolResultErrorCodeUnavailable BetaWebSearchToolResultErrorCode = "unavailable"`

            - `const BetaWebSearchToolResultErrorCodeMaxUsesExceeded BetaWebSearchToolResultErrorCode = "max_uses_exceeded"`

            - `const BetaWebSearchToolResultErrorCodeTooManyRequests BetaWebSearchToolResultErrorCode = "too_many_requests"`

            - `const BetaWebSearchToolResultErrorCodeQueryTooLong BetaWebSearchToolResultErrorCode = "query_too_long"`

            - `const BetaWebSearchToolResultErrorCodeRequestTooLarge BetaWebSearchToolResultErrorCode = "request_too_large"`

          - `Type WebSearchToolResultError`

            default: web_search_tool_result_error

        - `type BetaWebSearchToolResultBlockContentArray []BetaWebSearchResultBlock`

          - `EncryptedContent string`

          - `PageAge string`

          - `Title string`

          - `Type WebSearchResult`

            default: web_search_result

          - `URL string`

      - `ToolUseID string`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `Type WebSearchToolResult`

        default: web_search_tool_result

      - `Caller BetaWebSearchToolResultBlockCallerUnion Optional`

        Tool invocation directly from the model.

        - `type BetaDirectCaller struct{…}`

          Tool invocation directly from the model.

        - `type BetaServerToolCaller struct{…}`

          Tool invocation generated by a server-side tool.

        - `type BetaServerToolCaller20260120 struct{…}`

    - `type BetaWebFetchToolResultBlock struct{…}`

      - `Content BetaWebFetchToolResultBlockContentUnion`

        - `type BetaWebFetchToolResultErrorBlock struct{…}`

          - `ErrorCode BetaWebFetchToolResultErrorCode`

            - `const BetaWebFetchToolResultErrorCodeInvalidToolInput BetaWebFetchToolResultErrorCode = "invalid_tool_input"`

            - `const BetaWebFetchToolResultErrorCodeURLTooLong BetaWebFetchToolResultErrorCode = "url_too_long"`

            - `const BetaWebFetchToolResultErrorCodeURLNotAllowed BetaWebFetchToolResultErrorCode = "url_not_allowed"`

            - `const BetaWebFetchToolResultErrorCodeURLNotInPriorContext BetaWebFetchToolResultErrorCode = "url_not_in_prior_context"`

            - `const BetaWebFetchToolResultErrorCodeURLNotAccessible BetaWebFetchToolResultErrorCode = "url_not_accessible"`

            - `const BetaWebFetchToolResultErrorCodeUnsupportedContentType BetaWebFetchToolResultErrorCode = "unsupported_content_type"`

            - `const BetaWebFetchToolResultErrorCodeTooManyRequests BetaWebFetchToolResultErrorCode = "too_many_requests"`

            - `const BetaWebFetchToolResultErrorCodeMaxUsesExceeded BetaWebFetchToolResultErrorCode = "max_uses_exceeded"`

            - `const BetaWebFetchToolResultErrorCodeUnavailable BetaWebFetchToolResultErrorCode = "unavailable"`

          - `Type WebFetchToolResultError`

            default: web_fetch_tool_result_error

        - `type BetaWebFetchBlock struct{…}`

          - `Content BetaDocumentBlock`

            - `Citations BetaCitationConfig`

              Citation configuration for the document

              - `Enabled bool`

                default: false

            - `Source BetaDocumentBlockSourceUnion`

              - `type BetaBase64PDFSource struct{…}`

                - `Data string`

                  format: byte

                - `MediaType ApplicationPDF`

                - `Type Base64`

              - `type BetaPlainTextSource struct{…}`

                - `Data string`

                - `MediaType TextPlain`

                - `Type Text`

            - `Title string`

              The title of the document

            - `Type Document`

              default: document

          - `RetrievedAt string`

            ISO 8601 timestamp when the content was retrieved

          - `Type WebFetchResult`

            default: web_fetch_result

          - `URL string`

            Fetched content URL

      - `ToolUseID string`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `Type WebFetchToolResult`

        default: web_fetch_tool_result

      - `Caller BetaWebFetchToolResultBlockCallerUnion Optional`

        Tool invocation directly from the model.

        - `type BetaDirectCaller struct{…}`

          Tool invocation directly from the model.

        - `type BetaServerToolCaller struct{…}`

          Tool invocation generated by a server-side tool.

        - `type BetaServerToolCaller20260120 struct{…}`

    - `type BetaAdvisorToolResultBlock struct{…}`

      - `Content BetaAdvisorToolResultBlockContentUnion`

        - `type BetaAdvisorToolResultError struct{…}`

          - `ErrorCode BetaAdvisorToolResultErrorErrorCode`

            - `const BetaAdvisorToolResultErrorErrorCodeMaxUsesExceeded BetaAdvisorToolResultErrorErrorCode = "max_uses_exceeded"`

            - `const BetaAdvisorToolResultErrorErrorCodePromptTooLong BetaAdvisorToolResultErrorErrorCode = "prompt_too_long"`

            - `const BetaAdvisorToolResultErrorErrorCodeTooManyRequests BetaAdvisorToolResultErrorErrorCode = "too_many_requests"`

            - `const BetaAdvisorToolResultErrorErrorCodeOverloaded BetaAdvisorToolResultErrorErrorCode = "overloaded"`

            - `const BetaAdvisorToolResultErrorErrorCodeUnavailable BetaAdvisorToolResultErrorErrorCode = "unavailable"`

            - `const BetaAdvisorToolResultErrorErrorCodeExecutionTimeExceeded BetaAdvisorToolResultErrorErrorCode = "execution_time_exceeded"`

            - `const BetaAdvisorToolResultErrorErrorCodeModelNotFound BetaAdvisorToolResultErrorErrorCode = "model_not_found"`

          - `Type AdvisorToolResultError`

            default: advisor_tool_result_error

        - `type BetaAdvisorResultBlock struct{…}`

          - `StopReason string`

            The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

          - `Text string`

          - `Type AdvisorResult`

            default: advisor_result

        - `type BetaAdvisorRedactedResultBlock struct{…}`

          - `EncryptedContent string`

            Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

          - `StopReason string`

            The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

          - `Type AdvisorRedactedResult`

            default: advisor_redacted_result

      - `ToolUseID string`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `Type AdvisorToolResult`

        default: advisor_tool_result

    - `type BetaCodeExecutionToolResultBlock struct{…}`

      - `Content BetaCodeExecutionToolResultBlockContentUnion`

        Code execution result with encrypted stdout for PFC + web_search results.

        - `type BetaCodeExecutionToolResultError struct{…}`

          - `ErrorCode BetaCodeExecutionToolResultErrorCode`

            - `const BetaCodeExecutionToolResultErrorCodeInvalidToolInput BetaCodeExecutionToolResultErrorCode = "invalid_tool_input"`

            - `const BetaCodeExecutionToolResultErrorCodeUnavailable BetaCodeExecutionToolResultErrorCode = "unavailable"`

            - `const BetaCodeExecutionToolResultErrorCodeTooManyRequests BetaCodeExecutionToolResultErrorCode = "too_many_requests"`

            - `const BetaCodeExecutionToolResultErrorCodeExecutionTimeExceeded BetaCodeExecutionToolResultErrorCode = "execution_time_exceeded"`

          - `Type CodeExecutionToolResultError`

            default: code_execution_tool_result_error

        - `type BetaCodeExecutionResultBlock struct{…}`

          - `Content []BetaCodeExecutionOutputBlock`

            - `FileID string`

            - `Type CodeExecutionOutput`

              default: code_execution_output

          - `ReturnCode int64`

          - `Stderr string`

          - `Stdout string`

          - `Type CodeExecutionResult`

            default: code_execution_result

        - `type BetaEncryptedCodeExecutionResultBlock struct{…}`

          Code execution result with encrypted stdout for PFC + web_search results.

          - `Content []BetaCodeExecutionOutputBlock`

            - `FileID string`

            - `Type CodeExecutionOutput`

              default: code_execution_output

          - `EncryptedStdout string`

          - `ReturnCode int64`

          - `Stderr string`

          - `Type EncryptedCodeExecutionResult`

            default: encrypted_code_execution_result

      - `ToolUseID string`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `Type CodeExecutionToolResult`

        default: code_execution_tool_result

    - `type BetaBashCodeExecutionToolResultBlock struct{…}`

      - `Content BetaBashCodeExecutionToolResultBlockContentUnion`

        - `type BetaBashCodeExecutionToolResultError struct{…}`

          - `ErrorCode BetaBashCodeExecutionToolResultErrorErrorCode`

            - `const BetaBashCodeExecutionToolResultErrorErrorCodeInvalidToolInput BetaBashCodeExecutionToolResultErrorErrorCode = "invalid_tool_input"`

            - `const BetaBashCodeExecutionToolResultErrorErrorCodeUnavailable BetaBashCodeExecutionToolResultErrorErrorCode = "unavailable"`

            - `const BetaBashCodeExecutionToolResultErrorErrorCodeTooManyRequests BetaBashCodeExecutionToolResultErrorErrorCode = "too_many_requests"`

            - `const BetaBashCodeExecutionToolResultErrorErrorCodeExecutionTimeExceeded BetaBashCodeExecutionToolResultErrorErrorCode = "execution_time_exceeded"`

            - `const BetaBashCodeExecutionToolResultErrorErrorCodeOutputFileTooLarge BetaBashCodeExecutionToolResultErrorErrorCode = "output_file_too_large"`

          - `Type BashCodeExecutionToolResultError`

            default: bash_code_execution_tool_result_error

        - `type BetaBashCodeExecutionResultBlock struct{…}`

          - `Content []BetaBashCodeExecutionOutputBlock`

            - `FileID string`

            - `Type BashCodeExecutionOutput`

              default: bash_code_execution_output

          - `ReturnCode int64`

          - `Stderr string`

          - `Stdout string`

          - `Type BashCodeExecutionResult`

            default: bash_code_execution_result

      - `ToolUseID string`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `Type BashCodeExecutionToolResult`

        default: bash_code_execution_tool_result

    - `type BetaTextEditorCodeExecutionToolResultBlock struct{…}`

      - `Content BetaTextEditorCodeExecutionToolResultBlockContentUnion`

        - `type BetaTextEditorCodeExecutionToolResultError struct{…}`

          - `ErrorCode BetaTextEditorCodeExecutionToolResultErrorErrorCode`

            - `const BetaTextEditorCodeExecutionToolResultErrorErrorCodeInvalidToolInput BetaTextEditorCodeExecutionToolResultErrorErrorCode = "invalid_tool_input"`

            - `const BetaTextEditorCodeExecutionToolResultErrorErrorCodeUnavailable BetaTextEditorCodeExecutionToolResultErrorErrorCode = "unavailable"`

            - `const BetaTextEditorCodeExecutionToolResultErrorErrorCodeTooManyRequests BetaTextEditorCodeExecutionToolResultErrorErrorCode = "too_many_requests"`

            - `const BetaTextEditorCodeExecutionToolResultErrorErrorCodeExecutionTimeExceeded BetaTextEditorCodeExecutionToolResultErrorErrorCode = "execution_time_exceeded"`

            - `const BetaTextEditorCodeExecutionToolResultErrorErrorCodeFileNotFound BetaTextEditorCodeExecutionToolResultErrorErrorCode = "file_not_found"`

          - `ErrorMessage string`

          - `Type TextEditorCodeExecutionToolResultError`

            default: text_editor_code_execution_tool_result_error

        - `type BetaTextEditorCodeExecutionViewResultBlock struct{…}`

          - `Content string`

          - `FileType BetaTextEditorCodeExecutionViewResultBlockFileType`

            - `const BetaTextEditorCodeExecutionViewResultBlockFileTypeText BetaTextEditorCodeExecutionViewResultBlockFileType = "text"`

            - `const BetaTextEditorCodeExecutionViewResultBlockFileTypeImage BetaTextEditorCodeExecutionViewResultBlockFileType = "image"`

            - `const BetaTextEditorCodeExecutionViewResultBlockFileTypePDF BetaTextEditorCodeExecutionViewResultBlockFileType = "pdf"`

          - `NumLines int64`

          - `StartLine int64`

          - `TotalLines int64`

          - `Type TextEditorCodeExecutionViewResult`

            default: text_editor_code_execution_view_result

        - `type BetaTextEditorCodeExecutionCreateResultBlock struct{…}`

          - `IsFileUpdate bool`

          - `Type TextEditorCodeExecutionCreateResult`

            default: text_editor_code_execution_create_result

        - `type BetaTextEditorCodeExecutionStrReplaceResultBlock struct{…}`

          - `Lines []string`

          - `NewLines int64`

          - `NewStart int64`

          - `OldLines int64`

          - `OldStart int64`

          - `Type TextEditorCodeExecutionStrReplaceResult`

            default: text_editor_code_execution_str_replace_result

      - `ToolUseID string`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `Type TextEditorCodeExecutionToolResult`

        default: text_editor_code_execution_tool_result

    - `type BetaToolSearchToolResultBlock struct{…}`

      - `Content BetaToolSearchToolResultBlockContentUnion`

        - `type BetaToolSearchToolResultError struct{…}`

          - `ErrorCode BetaToolSearchToolResultErrorErrorCode`

            - `const BetaToolSearchToolResultErrorErrorCodeInvalidToolInput BetaToolSearchToolResultErrorErrorCode = "invalid_tool_input"`

            - `const BetaToolSearchToolResultErrorErrorCodeUnavailable BetaToolSearchToolResultErrorErrorCode = "unavailable"`

            - `const BetaToolSearchToolResultErrorErrorCodeTooManyRequests BetaToolSearchToolResultErrorErrorCode = "too_many_requests"`

            - `const BetaToolSearchToolResultErrorErrorCodeExecutionTimeExceeded BetaToolSearchToolResultErrorErrorCode = "execution_time_exceeded"`

          - `ErrorMessage string`

          - `Type ToolSearchToolResultError`

            default: tool_search_tool_result_error

        - `type BetaToolSearchToolSearchResultBlock struct{…}`

          - `ToolReferences []BetaToolReferenceBlock`

            - `ToolName string`

              maxLength: 256, minLength: 1, pattern: ^[a-zA-Z0-9_-]{1,256}$

            - `Type ToolReference`

              default: tool_reference

          - `Type ToolSearchToolSearchResult`

            default: tool_search_tool_search_result

      - `ToolUseID string`

        pattern: ^srvtoolu_[a-zA-Z0-9_]+$

      - `Type ToolSearchToolResult`

        default: tool_search_tool_result

    - `type BetaMCPToolUseBlock struct{…}`

      - `ID string`

        pattern: ^[a-zA-Z0-9_-]+$

      - `Input map[string, any]`

      - `Name string`

        The name of the MCP tool

      - `ServerName string`

        The name of the MCP server

      - `Type MCPToolUse`

        default: mcp_tool_use

    - `type BetaMCPToolResultBlock struct{…}`

      - `Content BetaMCPToolResultBlockContentUnion`

        - `string`

        - `type BetaMCPToolResultBlockContentBetaMCPToolResultBlockContent []BetaTextBlock`

          - `Citations []BetaTextCitationUnion`

            Citations supporting the text block.

            The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

          - `Text string`

            maxLength: 5000000, minLength: 0

          - `Type Text`

            default: text

      - `IsError bool`

        default: false

      - `ToolUseID string`

        pattern: ^[a-zA-Z0-9_-]+$

      - `Type MCPToolResult`

        default: mcp_tool_result

    - `type BetaContainerUploadBlock struct{…}`

      Response model for a file uploaded to the container.

      - `FileID string`

      - `Type ContainerUpload`

        default: container_upload

    - `type BetaCompactionBlock struct{…}`

      A compaction block returned when autocompact is triggered.

      When content is None, it indicates the compaction failed to produce a valid
      summary (e.g., malformed output from the model). Clients may round-trip
      compaction blocks with null content; the server treats them as no-ops.

      - `Content string`

        Summary of compacted content, or null if compaction failed

      - `EncryptedContent string`

        Opaque metadata from prior compaction, to be round-tripped verbatim

      - `Type Compaction`

        default: compaction

    - `type BetaFallbackBlock struct{…}`

      Marks the point in `content` where one model's output gives way to the next.

      One block appears per hop where a preceding model actually ran this turn and
      declined. A turn where no preceding model ran and declined has no such
      boundary and carries no block — the signal for whether a fallback model
      served the response is the presence of a `fallback_message` entry in
      `usage.iterations`, not this block.

      The block is treated like a server-tool content block for streaming: it
      arrives via the standard `content_block_start` / `content_block_stop`
      pair and carries no deltas.

      - `From BetaFallbackInfo`

        The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.

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

      - `To BetaFallbackInfo`

        The fallback model producing the content that follows this block. Its `model` is always the canonical id.

      - `Trigger BetaFallbackRefusalTrigger`

        What caused the `from` model to hand over at this hop.

        - `Category BetaFallbackRefusalTriggerCategory`

          The policy category that triggered a refusal.

          - `const BetaFallbackRefusalTriggerCategoryCyber BetaFallbackRefusalTriggerCategory = "cyber"`

            The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.

          - `const BetaFallbackRefusalTriggerCategoryBio BetaFallbackRefusalTriggerCategory = "bio"`

            The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.

          - `const BetaFallbackRefusalTriggerCategoryFrontierLLM BetaFallbackRefusalTriggerCategory = "frontier_llm"`

            The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.

          - `const BetaFallbackRefusalTriggerCategoryReasoningExtraction BetaFallbackRefusalTriggerCategory = "reasoning_extraction"`

            The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).

          - `const BetaFallbackRefusalTriggerCategoryGeneralHarms BetaFallbackRefusalTriggerCategory = "general_harms"`

            The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.

        - `Type Refusal`

          default: refusal

      - `Type Fallback`

        default: fallback

  - `ContextManagement BetaContextManagementResponse`

    Context management response.

    Information about context management strategies applied during the request.

    - `AppliedEdits []BetaContextManagementResponseAppliedEditUnion`

      List of context management edits that were applied.

      - `type BetaClearToolUses20250919EditResponse struct{…}`

        - `ClearedInputTokens int64`

          Number of input tokens cleared by this edit.

          minimum: 0

        - `ClearedToolUses int64`

          Number of tool uses that were cleared.

          minimum: 0

        - `Type ClearToolUses20250919`

          The type of context management edit applied.

          default: clear_tool_uses_20250919

      - `type BetaClearThinking20251015EditResponse struct{…}`

        - `ClearedInputTokens int64`

          Number of input tokens cleared by this edit.

          minimum: 0

        - `ClearedThinkingTurns int64`

          Number of thinking turns that were cleared.

          minimum: 0

        - `Type ClearThinking20251015`

          The type of context management edit applied.

          default: clear_thinking_20251015

  - `Diagnostics BetaDiagnostics`

    Response envelope for request-level diagnostics. Present (possibly
    null) whenever the caller supplied `diagnostics` on the request.

    - `CacheMissReason BetaDiagnosticsCacheMissReasonUnion`

      Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

      - `type BetaCacheMissModelChanged struct{…}`

        - `CacheMissedInputTokens int64`

          Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

        - `Type ModelChanged`

          default: model_changed

      - `type BetaCacheMissSystemChanged struct{…}`

        - `CacheMissedInputTokens int64`

          Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

        - `Type SystemChanged`

          default: system_changed

      - `type BetaCacheMissToolsChanged struct{…}`

        - `CacheMissedInputTokens int64`

          Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

        - `Type ToolsChanged`

          default: tools_changed

      - `type BetaCacheMissMessagesChanged struct{…}`

        - `CacheMissedInputTokens int64`

          Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

        - `Type MessagesChanged`

          default: messages_changed

      - `type BetaCacheMissPreviousMessageNotFound struct{…}`

        - `Type PreviousMessageNotFound`

          default: previous_message_not_found

      - `type BetaCacheMissUnavailable struct{…}`

        - `Type Unavailable`

          default: unavailable

  - `Model Model`

    The model that will complete your prompt.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

  - `Role Assistant`

    Conversational role of the generated message.

    This will always be `"assistant"`.

    default: assistant

  - `StopDetails BetaRefusalStopDetails`

    Structured information about a refusal.

    - `Category BetaRefusalStopDetailsCategory`

      The policy category that triggered a refusal.

      - `const BetaRefusalStopDetailsCategoryCyber BetaRefusalStopDetailsCategory = "cyber"`

        The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.

      - `const BetaRefusalStopDetailsCategoryBio BetaRefusalStopDetailsCategory = "bio"`

        The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.

      - `const BetaRefusalStopDetailsCategoryFrontierLLM BetaRefusalStopDetailsCategory = "frontier_llm"`

        The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.

      - `const BetaRefusalStopDetailsCategoryReasoningExtraction BetaRefusalStopDetailsCategory = "reasoning_extraction"`

        The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).

      - `const BetaRefusalStopDetailsCategoryGeneralHarms BetaRefusalStopDetailsCategory = "general_harms"`

        The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.

    - `Explanation string`

      Human-readable explanation of the refusal.

      This text is not guaranteed to be stable. `null` when no explanation is available for the category.

    - `FallbackCreditToken string`

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

    - `FallbackHasPrefillClaim bool`

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

    - `RecommendedModel string`

      The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

    - `Type Refusal`

      default: refusal

  - `StopReason BetaStopReason`

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

    - `const BetaStopReasonEndTurn BetaStopReason = "end_turn"`

    - `const BetaStopReasonMaxTokens BetaStopReason = "max_tokens"`

    - `const BetaStopReasonStopSequence BetaStopReason = "stop_sequence"`

    - `const BetaStopReasonToolUse BetaStopReason = "tool_use"`

    - `const BetaStopReasonPauseTurn BetaStopReason = "pause_turn"`

    - `const BetaStopReasonCompaction BetaStopReason = "compaction"`

    - `const BetaStopReasonRefusal BetaStopReason = "refusal"`

    - `const BetaStopReasonModelContextWindowExceeded BetaStopReason = "model_context_window_exceeded"`

  - `StopSequence string`

    Which custom stop sequence was generated, if any.

    This value will be a non-null string if one of your custom stop sequences was generated.

  - `Type Message`

    Object type.

    For Messages, this is always `"message"`.

    default: message

  - `Usage BetaUsage`

    Billing and rate-limit usage.

    Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

    Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

    For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

    Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

    - `CacheCreation BetaCacheCreation`

      Breakdown of cached tokens by TTL

      - `Ephemeral1hInputTokens int64`

        The number of input tokens used to create the 1 hour cache entry.

        default: 0, minimum: 0

      - `Ephemeral5mInputTokens int64`

        The number of input tokens used to create the 5 minute cache entry.

        default: 0, minimum: 0

    - `CacheCreationInputTokens int64`

      The number of input tokens used to create the cache entry.

      minimum: 0

    - `CacheReadInputTokens int64`

      The number of input tokens read from the cache.

      minimum: 0

    - `FallbackCredit BetaFallbackCreditUsage`

      Outcome of the `fallback_credit_token` presented on this request.

      - `Status BetaFallbackCreditUsageStatusUnion`

        Whether the fallback-credit reprice was applied to this response's billing.

        A union discriminated on `type`. `redeemed`: the retry is billed as if
        the conversation had been on the retry model all along — including when the
        resulting shift is zero because there was nothing to move. `not_applied`:
        no reprice was applied; the arm's `reason` says why.

        - `type BetaFallbackCreditRedeemed struct{…}`

          The reprice was applied: the retry is billed as if the conversation
          had been on the retry model all along.

          - `Type Redeemed`

            default: redeemed

        - `type BetaFallbackCreditNotApplied struct{…}`

          No reprice was applied; `reason` says why.

          - `Reason BetaFallbackCreditNotAppliedReason`

            Why the reprice was not applied.

            A closed enum; additions to the redemption-check vocabulary arrive as
            deliberate schema updates.

            - `const BetaFallbackCreditNotAppliedReasonBodyMismatch BetaFallbackCreditNotAppliedReason = "body_mismatch"`

            - `const BetaFallbackCreditNotAppliedReasonContinuationExcluded BetaFallbackCreditNotAppliedReason = "continuation_excluded"`

            - `const BetaFallbackCreditNotAppliedReasonContinuationOnly BetaFallbackCreditNotAppliedReason = "continuation_only"`

            - `const BetaFallbackCreditNotAppliedReasonExpired BetaFallbackCreditNotAppliedReason = "expired"`

            - `const BetaFallbackCreditNotAppliedReasonInvalidTargetModel BetaFallbackCreditNotAppliedReason = "invalid_target_model"`

            - `const BetaFallbackCreditNotAppliedReasonNotEnabled BetaFallbackCreditNotAppliedReason = "not_enabled"`

            - `const BetaFallbackCreditNotAppliedReasonRepriceUnavailable BetaFallbackCreditNotAppliedReason = "reprice_unavailable"`

            - `const BetaFallbackCreditNotAppliedReasonTemporarilyUnavailable BetaFallbackCreditNotAppliedReason = "temporarily_unavailable"`

            - `const BetaFallbackCreditNotAppliedReasonVariantFieldsPresent BetaFallbackCreditNotAppliedReason = "variant_fields_present"`

            - `const BetaFallbackCreditNotAppliedReasonWrongOrganization BetaFallbackCreditNotAppliedReason = "wrong_organization"`

            - `const BetaFallbackCreditNotAppliedReasonWrongPlatform BetaFallbackCreditNotAppliedReason = "wrong_platform"`

            - `const BetaFallbackCreditNotAppliedReasonWrongWorkspace BetaFallbackCreditNotAppliedReason = "wrong_workspace"`

          - `Type NotApplied`

            default: not_applied

          - `RemoveToRedeem []string Optional`

            Request fields to remove before retrying, so the retry can redeem this
            token.

            Present exactly when `reason` is `variant_fields_present` — never null,
            never an empty array; absent otherwise. Fields are named only from your own request, and only after
            the sealed variant hash matched. A served best-effort retry has already
            been billed at normal price; nothing redeems retroactively, but a corrected
            re-send inside the token's five-minute window can still redeem.

    - `InferenceGeo string`

      The geographic region where inference was performed for this request.

    - `InputTokens int64`

      The number of input tokens which were used.

      minimum: 0

    - `Iterations BetaIterationsUsage`

      Per-iteration token usage breakdown.

      Each entry represents one sampling iteration, with its own input/output token counts and cache statistics, discriminated by `type`. For `message` entries (model sampling iterations, such as the turns of a server-side tool use loop), this allows you to:

      - Determine which iterations exceeded long context thresholds (>=200k tokens)
      - Calculate the context window size from the last `message` entry
      - Understand token accumulation across server-side tool use loops

      A `compaction` entry reports the token usage of the compaction operation itself — the server-side request that summarizes the context being closed — NOT the size of the context that was compacted away, and its token counts can be much smaller than that closed context (for example, a compaction that closes a ~200k-token context can report only a few thousand tokens). Do not derive the context window size from a `compaction` entry, even when it is the last entry. A `compaction` entry's tokens are not included in the top-level `usage` fields. When an input-token trigger is in effect (the default — 150,000 tokens unless configured otherwise), each `compaction` entry closes a context that had reached at least that threshold, though the context can exceed it by the final iteration's output and tool results.

      - `type BetaMessageIterationUsage struct{…}`

        Token usage for a sampling iteration.

        - `CacheCreation BetaCacheCreation`

          Breakdown of cached tokens by TTL

        - `CacheCreationInputTokens int64`

          The number of input tokens used to create the cache entry.

          default: 0, minimum: 0

        - `CacheReadInputTokens int64`

          The number of input tokens read from the cache.

          default: 0, minimum: 0

        - `InputTokens int64`

          The number of input tokens which were used.

          minimum: 0

        - `Model Model`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `OutputTokens int64`

          The number of output tokens which were used.

          minimum: 0

        - `Type Message`

          Usage for a sampling iteration

          default: message

      - `type BetaCompactionIterationUsage struct{…}`

        Token usage for a compaction iteration.

        - `CacheCreation BetaCacheCreation`

          Breakdown of cached tokens by TTL

        - `CacheCreationInputTokens int64`

          The number of input tokens used to create the cache entry.

          default: 0, minimum: 0

        - `CacheReadInputTokens int64`

          The number of input tokens read from the cache.

          default: 0, minimum: 0

        - `InputTokens int64`

          The number of input tokens which were used.

          minimum: 0

        - `OutputTokens int64`

          The number of output tokens which were used.

          minimum: 0

        - `Type Compaction`

          Usage for a compaction iteration

          default: compaction

      - `type BetaAdvisorMessageIterationUsage struct{…}`

        Token usage for an advisor sub-inference iteration.

        - `CacheCreation BetaCacheCreation`

          Breakdown of cached tokens by TTL

        - `CacheCreationInputTokens int64`

          The number of input tokens used to create the cache entry.

          default: 0, minimum: 0

        - `CacheReadInputTokens int64`

          The number of input tokens read from the cache.

          default: 0, minimum: 0

        - `InputTokens int64`

          The number of input tokens which were used.

          minimum: 0

        - `Model Model`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `OutputTokens int64`

          The number of output tokens which were used.

          minimum: 0

        - `Type AdvisorMessage`

          Usage for an advisor sub-inference iteration

          default: advisor_message

      - `type BetaFallbackMessageIterationUsage struct{…}`

        Token usage for the fallback-model attempt of a server-side fallback request.

        Produced in place of a `message` entry for whichever hop served the
        response. A declined hop produces the existing `message` entry. Whether
        a fallback model served the response is signalled by the presence of this
        entry in `usage.iterations`.

        - `CacheCreation BetaCacheCreation`

          Breakdown of cached tokens by TTL

        - `CacheCreationInputTokens int64`

          The number of input tokens used to create the cache entry.

          default: 0, minimum: 0

        - `CacheReadInputTokens int64`

          The number of input tokens read from the cache.

          default: 0, minimum: 0

        - `InputTokens int64`

          The number of input tokens which were used.

          minimum: 0

        - `Model Model`

          The model that will complete your prompt.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `OutputTokens int64`

          The number of output tokens which were used.

          minimum: 0

        - `Type FallbackMessage`

          Usage for the fallback-model attempt that served the response

          default: fallback_message

    - `OutputTokens int64`

      The number of output tokens which were used.

      minimum: 0

    - `OutputTokensDetails BetaOutputTokensDetails`

      Breakdown of output tokens by category.

      `output_tokens` remains the inclusive, authoritative total used for billing.
      This object provides a read-only decomposition for observability — for example,
      how many of the billed output tokens were spent on internal reasoning that may
      have been summarized before being returned to you.

      - `ThinkingTokens int64`

        Number of output tokens the model generated as internal reasoning, including
        the thinking-block delimiter tokens.

        Reflects the raw reasoning the model produced, not the (possibly shorter)
        summarized thinking text returned in the response body. Computed by
        re-tokenizing the raw reasoning text, so it may differ from the model's exact
        generation count by a small number of tokens. Always ≤ `output_tokens`;
        `output_tokens - thinking_tokens` approximates the non-reasoning output.

        default: 0, minimum: 0

    - `ServerToolUse BetaServerToolUsage`

      The number of server tool requests.

      - `WebFetchRequests int64`

        The number of web fetch tool requests.

        default: 0, minimum: 0

      - `WebSearchRequests int64`

        The number of web search tool requests.

        default: 0, minimum: 0

    - `ServiceTier BetaUsageServiceTier`

      If the request used the priority, standard, or batch tier.

      - `const BetaUsageServiceTierStandard BetaUsageServiceTier = "standard"`

      - `const BetaUsageServiceTierPriority BetaUsageServiceTier = "priority"`

      - `const BetaUsageServiceTierBatch BetaUsageServiceTier = "batch"`

    - `Speed BetaUsageSpeed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `const BetaUsageSpeedStandard BetaUsageSpeed = "standard"`

      - `const BetaUsageSpeedFast BetaUsageSpeed = "fast"`

- `type BetaRawMessageStreamEventUnion interface{…}`

  - `type BetaRawMessageStartEvent struct{…}`

    - `Message BetaMessage`

    - `Type MessageStart`

      default: message_start

  - `type BetaRawMessageDeltaEvent struct{…}`

    - `ContextManagement BetaContextManagementResponse`

      Information about context management strategies applied during the request

    - `Delta BetaRawMessageDeltaEventDelta`

      - `Container BetaContainer`

        Information about the container used in the request (for the code execution tool)

      - `StopDetails BetaRefusalStopDetails`

        Structured information about a refusal.

      - `StopReason BetaStopReason`

      - `StopSequence string`

    - `Type MessageDelta`

      default: message_delta

    - `Usage BetaMessageDeltaUsage`

      Billing and rate-limit usage.

      Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

      Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

      For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

      Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

      - `CacheCreationInputTokens int64`

        The cumulative number of input tokens used to create the cache entry.

        minimum: 0

      - `CacheReadInputTokens int64`

        The cumulative number of input tokens read from the cache.

        minimum: 0

      - `FallbackCredit BetaFallbackCreditUsage`

        Outcome of the `fallback_credit_token` presented on this request.

      - `InputTokens int64`

        The cumulative number of input tokens which were used.

        minimum: 0

      - `Iterations BetaIterationsUsage`

        Per-iteration token usage breakdown.

        Each entry represents one sampling iteration, with its own input/output token counts and cache statistics, discriminated by `type`. For `message` entries (model sampling iterations, such as the turns of a server-side tool use loop), this allows you to:

        - Determine which iterations exceeded long context thresholds (>=200k tokens)
        - Calculate the context window size from the last `message` entry
        - Understand token accumulation across server-side tool use loops

        A `compaction` entry reports the token usage of the compaction operation itself — the server-side request that summarizes the context being closed — NOT the size of the context that was compacted away, and its token counts can be much smaller than that closed context (for example, a compaction that closes a ~200k-token context can report only a few thousand tokens). Do not derive the context window size from a `compaction` entry, even when it is the last entry. A `compaction` entry's tokens are not included in the top-level `usage` fields. When an input-token trigger is in effect (the default — 150,000 tokens unless configured otherwise), each `compaction` entry closes a context that had reached at least that threshold, though the context can exceed it by the final iteration's output and tool results.

      - `OutputTokens int64`

        The cumulative number of output tokens which were used.

      - `OutputTokensDetails BetaOutputTokensDetails`

        Breakdown of output tokens by category.

        `output_tokens` remains the inclusive, authoritative total used for billing.
        This object provides a read-only decomposition for observability — for example,
        how many of the billed output tokens were spent on internal reasoning that may
        have been summarized before being returned to you.

      - `ServerToolUse BetaServerToolUsage`

        The number of server tool requests.

  - `type BetaRawMessageStopEvent struct{…}`

    - `Type MessageStop`

      default: message_stop

  - `type BetaRawContentBlockStartEvent struct{…}`

    - `ContentBlock BetaRawContentBlockStartEventContentBlockUnion`

      Response model for a file uploaded to the container.

      - `type BetaTextBlock struct{…}`

      - `type BetaThinkingBlock struct{…}`

      - `type BetaRedactedThinkingBlock struct{…}`

      - `type BetaToolUseBlock struct{…}`

      - `type BetaServerToolUseBlock struct{…}`

      - `type BetaWebSearchToolResultBlock struct{…}`

      - `type BetaWebFetchToolResultBlock struct{…}`

      - `type BetaAdvisorToolResultBlock struct{…}`

      - `type BetaCodeExecutionToolResultBlock struct{…}`

      - `type BetaBashCodeExecutionToolResultBlock struct{…}`

      - `type BetaTextEditorCodeExecutionToolResultBlock struct{…}`

      - `type BetaToolSearchToolResultBlock struct{…}`

      - `type BetaMCPToolUseBlock struct{…}`

      - `type BetaMCPToolResultBlock struct{…}`

      - `type BetaContainerUploadBlock struct{…}`

        Response model for a file uploaded to the container.

      - `type BetaCompactionBlock struct{…}`

        A compaction block returned when autocompact is triggered.

        When content is None, it indicates the compaction failed to produce a valid
        summary (e.g., malformed output from the model). Clients may round-trip
        compaction blocks with null content; the server treats them as no-ops.

      - `type BetaFallbackBlock struct{…}`

        Marks the point in `content` where one model's output gives way to the next.

        One block appears per hop where a preceding model actually ran this turn and
        declined. A turn where no preceding model ran and declined has no such
        boundary and carries no block — the signal for whether a fallback model
        served the response is the presence of a `fallback_message` entry in
        `usage.iterations`, not this block.

        The block is treated like a server-tool content block for streaming: it
        arrives via the standard `content_block_start` / `content_block_stop`
        pair and carries no deltas.

    - `Index int64`

    - `Type ContentBlockStart`

      default: content_block_start

  - `type BetaRawContentBlockDeltaEvent struct{…}`

    - `Delta BetaRawContentBlockDeltaUnion`

      - `type BetaTextDelta struct{…}`

        - `Text string`

        - `Type TextDelta`

          default: text_delta

      - `type BetaInputJSONDelta struct{…}`

        - `PartialJSON string`

        - `Type InputJSONDelta`

          default: input_json_delta

      - `type BetaCitationsDelta struct{…}`

        - `Citation BetaCitationsDeltaCitationUnion`

          - `type BetaCitationCharLocation struct{…}`

          - `type BetaCitationPageLocation struct{…}`

          - `type BetaCitationContentBlockLocation struct{…}`

          - `type BetaCitationsWebSearchResultLocation struct{…}`

          - `type BetaCitationSearchResultLocation struct{…}`

        - `Type CitationsDelta`

          default: citations_delta

      - `type BetaThinkingDelta struct{…}`

        - `EstimatedTokens int64`

          Per-frame increment of a coarse, running estimate of the tokens this thinking block has produced so far. Present whenever the `thinking-token-count-2026-05-13` beta is set; `null` unless `thinking.display` resolves to `"omitted"` and a count is due this frame. Sum the increments across `thinking_delta` frames on this block for a progress indicator. Each increment is a non-negative multiple of a fixed quantum and the cadence is rate-limited, so this is a deliberately lossy display hint, not a billable count; `usage.output_tokens` remains authoritative.

        - `Thinking string`

          The incremental `thinking` text for this content block. Concatenate the `thinking` values of successive `thinking_delta` events to assemble the block's full `thinking` value.

        - `Type ThinkingDelta`

          default: thinking_delta

      - `type BetaSignatureDelta struct{…}`

        - `Signature string`

          The `signature` for this thinking block: an opaque value used to verify that the block was generated by Claude when it is passed back to the API. Delivered in a `signature_delta` event just before the block's `content_block_stop` event.

        - `Type SignatureDelta`

          default: signature_delta

      - `type BetaCompactionContentBlockDelta struct{…}`

        - `Content string`

        - `EncryptedContent string`

          Opaque metadata from prior compaction, to be round-tripped verbatim

        - `Type CompactionDelta`

          default: compaction_delta

    - `Index int64`

    - `Type ContentBlockDelta`

      default: content_block_delta

  - `type BetaRawContentBlockStopEvent struct{…}`

    - `Index int64`

    - `Type ContentBlockStop`

      default: content_block_stop

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
	betaMessage, err := client.Beta.Messages.New(context.TODO(), anthropic.BetaMessageNewParams{
		MaxTokens: 1024,
		Messages: []anthropic.BetaMessageParam{anthropic.BetaMessageParam{
			Content: []anthropic.BetaContentBlockParamUnion{anthropic.BetaContentBlockParamUnion{
				OfText: &anthropic.BetaTextBlockParam{
					Text: "x",
				},
			}},
			Role: anthropic.BetaMessageParamRoleUser,
		}},
		Model: anthropic.ModelClaudeOpus5,
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaMessage.ID)
}
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
        "model": "claude-sonnet-5",
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
  }
}
```
