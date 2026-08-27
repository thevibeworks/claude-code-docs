# Sessions

## Create Session

`client.Beta.Sessions.New(ctx, params) (*BetaManagedAgentsSession, error)`

**POST** `/v1/sessions`

Create Session

### Parameters

- `params BetaSessionNewParams`

  - `Agent param.Field[BetaSessionNewParamsAgentUnion]`

    Body param: Agent identifier. Accepts the `agent` ID string, which pins the latest version for the session, or an `agent` object with both id and version specified.

    - `string`

    - `type BetaManagedAgentsAgentParamsResp struct{…}`

      Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

      - `ID string`

        The `agent` ID.

        minLength: 1, maxLength: 128

      - `Type BetaManagedAgentsAgentParamsType`

      - `Version int64 Optional`

        The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

        format: int32

    - `type BetaManagedAgentsAgentWithOverridesParamsResp struct{…}`

      Reference to an `agent` plus optional configuration overrides. Each provided field replaces the agent's value for the caller's use; the agent resource is unchanged.

      - `ID string`

        The `agent` ID.

        minLength: 1, maxLength: 128

      - `Type BetaManagedAgentsAgentWithOverridesParamsType`

      - `MCPServers []BetaManagedAgentsURLMCPServerParamsResp Optional`

        Replacement MCP server list. Full replacement: the provided array becomes the MCP servers. Send an empty array to clear; omit to preserve the agent's servers.

        - `Name string`

          Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

          minLength: 1, maxLength: 255

        - `Type BetaManagedAgentsURLMCPServerParamsType`

        - `URL string`

          Endpoint URL for the MCP server.

          maxLength: 2048

      - `Model BetaManagedAgentsModelConfigParamsResp Optional`

        Replacement model. Accepts the model string, e.g. `claude-opus-5`, or a `model_config` object. Omit to use the agent's model.

        - `type BetaManagedAgentsModelConfigParamsResp struct{…}`

          An object that defines additional configuration control over model use

          - `ID BetaManagedAgentsModel`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `type BetaManagedAgentsModel string`

              The model that will power your agent.

              See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

              - `const BetaManagedAgentsModelClaudeSonnet5 BetaManagedAgentsModel = "claude-sonnet-5"`

                High-performance model for coding and agents

              - `const BetaManagedAgentsModelClaudeFable5 BetaManagedAgentsModel = "claude-fable-5"`

                Next generation of intelligence for the hardest knowledge work and coding problems

              - `const BetaManagedAgentsModelClaudeOpus5 BetaManagedAgentsModel = "claude-opus-5"`

                Powerful intelligence for long-running agents and coding

              - `const BetaManagedAgentsModelClaudeOpus4_8 BetaManagedAgentsModel = "claude-opus-4-8"`

                Powerful intelligence for long-running agents and coding

              - `const BetaManagedAgentsModelClaudeOpus4_7 BetaManagedAgentsModel = "claude-opus-4-7"`

                Powerful intelligence for long-running agents and coding

              - `const BetaManagedAgentsModelClaudeOpus4_6 BetaManagedAgentsModel = "claude-opus-4-6"`

                Powerful intelligence for long-running agents and coding

              - `const BetaManagedAgentsModelClaudeSonnet4_6 BetaManagedAgentsModel = "claude-sonnet-4-6"`

                Best combination of speed and intelligence

              - `const BetaManagedAgentsModelClaudeHaiku4_5 BetaManagedAgentsModel = "claude-haiku-4-5"`

                Fastest model with near-frontier intelligence

              - `const BetaManagedAgentsModelClaudeHaiku4_5_20251001 BetaManagedAgentsModel = "claude-haiku-4-5-20251001"`

                Fastest model with near-frontier intelligence

              - `const BetaManagedAgentsModelClaudeOpus4_5 BetaManagedAgentsModel = "claude-opus-4-5"`

                Powerful intelligence for long-running agents and coding

              - `const BetaManagedAgentsModelClaudeOpus4_5_20251101 BetaManagedAgentsModel = "claude-opus-4-5-20251101"`

                Powerful intelligence for long-running agents and coding

              - `const BetaManagedAgentsModelClaudeSonnet4_5 BetaManagedAgentsModel = "claude-sonnet-4-5"`

                High-performance model for agents and coding

              - `const BetaManagedAgentsModelClaudeSonnet4_5_20250929 BetaManagedAgentsModel = "claude-sonnet-4-5-20250929"`

                High-performance model for agents and coding

            - `string`

          - `Effort BetaManagedAgentsModelConfigParamsEffortUnionResp Optional`

            How hard Claude works on each inference call. Accepts a bare level string (`"high"`) or `{"type": "high"}`. On create, omitting it resolves the per-model default; on update, omitting it leaves the stored value unchanged.

            - `string`

              - `const BetaManagedAgentsModelConfigParamsEffortBetaManagedAgentsEffortLevelLow BetaManagedAgentsModelConfigParamsEffortBetaManagedAgentsEffortLevel = "low"`

              - `const BetaManagedAgentsModelConfigParamsEffortBetaManagedAgentsEffortLevelMedium BetaManagedAgentsModelConfigParamsEffortBetaManagedAgentsEffortLevel = "medium"`

              - `const BetaManagedAgentsModelConfigParamsEffortBetaManagedAgentsEffortLevelHigh BetaManagedAgentsModelConfigParamsEffortBetaManagedAgentsEffortLevel = "high"`

              - `const BetaManagedAgentsModelConfigParamsEffortBetaManagedAgentsEffortLevelXhigh BetaManagedAgentsModelConfigParamsEffortBetaManagedAgentsEffortLevel = "xhigh"`

              - `const BetaManagedAgentsModelConfigParamsEffortBetaManagedAgentsEffortLevelMax BetaManagedAgentsModelConfigParamsEffortBetaManagedAgentsEffortLevel = "max"`

            - `type BetaManagedAgentsEffortLow struct{…}`

              Low effort. Favors latency over reasoning depth.

              - `Type BetaManagedAgentsEffortLowType`

            - `type BetaManagedAgentsEffortMedium struct{…}`

              Medium effort. Balances latency and reasoning depth.

              - `Type BetaManagedAgentsEffortMediumType`

            - `type BetaManagedAgentsEffortHigh struct{…}`

              High effort. Favors reasoning depth.

              - `Type BetaManagedAgentsEffortHighType`

            - `type BetaManagedAgentsEffortXhigh struct{…}`

              Extra-high effort. Not all models accept this level.

              - `Type BetaManagedAgentsEffortXhighType`

            - `type BetaManagedAgentsEffortMax struct{…}`

              Maximum effort. Favors reasoning depth over latency.

              - `Type BetaManagedAgentsEffortMaxType`

          - `InferenceGeo string Optional`

            Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo. On update, `model` is whole-object replacement — omitting inference_geo clears it.

          - `Speed BetaManagedAgentsModelConfigParamsSpeed Optional`

            Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

            - `const BetaManagedAgentsModelConfigParamsSpeedStandard BetaManagedAgentsModelConfigParamsSpeed = "standard"`

            - `const BetaManagedAgentsModelConfigParamsSpeedFast BetaManagedAgentsModelConfigParamsSpeed = "fast"`

      - `Skills []BetaManagedAgentsSkillParamsUnionResp Optional`

        Replacement skill list. Full replacement: the provided array becomes the skills. Send an empty array to clear; omit to preserve the agent's skills.

        - `type BetaManagedAgentsAnthropicSkillParamsResp struct{…}`

          An Anthropic-managed skill.

          - `SkillID string`

            Identifier of the Anthropic skill (e.g., "xlsx").

            minLength: 1, maxLength: 64

          - `Type BetaManagedAgentsAnthropicSkillParamsType`

          - `Version string Optional`

            Version to pin. Defaults to latest if omitted.

            minLength: 1, maxLength: 64

        - `type BetaManagedAgentsCustomSkillParamsResp struct{…}`

          A user-created custom skill.

          - `SkillID string`

            Tagged ID of the custom skill (e.g., "skill_01XJ5...").

            minLength: 1, maxLength: 64

          - `Type BetaManagedAgentsCustomSkillParamsType`

          - `Version string Optional`

            Version to pin. Defaults to latest if omitted.

            minLength: 1, maxLength: 64

      - `System string Optional`

        Replacement system prompt. Up to 100,000 characters. Set to null to clear the agent's system prompt; omit to preserve it.

        maxLength: 100000

      - `Tools []BetaManagedAgentsAgentWithOverridesParamsToolUnionResp Optional`

        Replacement tool list. Full replacement: the provided array becomes the tool configuration. Send an empty array to clear; omit to preserve the agent's tools.

        - `type BetaManagedAgentsAgentToolset20260401ParamsResp struct{…}`

          Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

          - `Type BetaManagedAgentsAgentToolset20260401ParamsType`

          - `Configs []BetaManagedAgentsAgentToolConfigParamsUnionResp Optional`

            Per-tool configuration overrides.

            - `type BetaManagedAgentsBashToolConfigParamsResp struct{…}`

              Configuration override for the bash tool.

              - `Name Bash`

                Must be "bash".

              - `Enabled bool Optional`

                Whether this tool is enabled and available to Claude. Overrides the default_config setting.

              - `PermissionPolicy BetaManagedAgentsBashToolConfigParamsPermissionPolicyUnionResp Optional`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                  - `Type BetaManagedAgentsAlwaysAllowPolicyType`

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

                  - `Type BetaManagedAgentsAlwaysAskPolicyType`

              - `Type BetaManagedAgentsBashToolConfigParamsType Optional`

            - `type BetaManagedAgentsEditToolConfigParamsResp struct{…}`

              Configuration override for the edit tool.

              - `Name Edit`

                Must be "edit".

              - `Enabled bool Optional`

                Whether this tool is enabled and available to Claude. Overrides the default_config setting.

              - `PermissionPolicy BetaManagedAgentsEditToolConfigParamsPermissionPolicyUnionResp Optional`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

              - `Type BetaManagedAgentsEditToolConfigParamsType Optional`

            - `type BetaManagedAgentsReadToolConfigParamsResp struct{…}`

              Configuration override for the read tool.

              - `Name Read`

                Must be "read".

              - `Enabled bool Optional`

                Whether this tool is enabled and available to Claude. Overrides the default_config setting.

              - `PermissionPolicy BetaManagedAgentsReadToolConfigParamsPermissionPolicyUnionResp Optional`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

              - `Type BetaManagedAgentsReadToolConfigParamsType Optional`

            - `type BetaManagedAgentsWriteToolConfigParamsResp struct{…}`

              Configuration override for the write tool.

              - `Name Write`

                Must be "write".

              - `Enabled bool Optional`

                Whether this tool is enabled and available to Claude. Overrides the default_config setting.

              - `PermissionPolicy BetaManagedAgentsWriteToolConfigParamsPermissionPolicyUnionResp Optional`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

              - `Type BetaManagedAgentsWriteToolConfigParamsType Optional`

            - `type BetaManagedAgentsGlobToolConfigParamsResp struct{…}`

              Configuration override for the glob tool.

              - `Name Glob`

                Must be "glob".

              - `Enabled bool Optional`

                Whether this tool is enabled and available to Claude. Overrides the default_config setting.

              - `PermissionPolicy BetaManagedAgentsGlobToolConfigParamsPermissionPolicyUnionResp Optional`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

              - `Type BetaManagedAgentsGlobToolConfigParamsType Optional`

            - `type BetaManagedAgentsGrepToolConfigParamsResp struct{…}`

              Configuration override for the grep tool.

              - `Name Grep`

                Must be "grep".

              - `Enabled bool Optional`

                Whether this tool is enabled and available to Claude. Overrides the default_config setting.

              - `PermissionPolicy BetaManagedAgentsGrepToolConfigParamsPermissionPolicyUnionResp Optional`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

              - `Type BetaManagedAgentsGrepToolConfigParamsType Optional`

            - `type BetaManagedAgentsWebFetchToolConfigParamsResp struct{…}`

              Configuration override for the web_fetch tool.

              - `Name WebFetch`

                Must be "web_fetch".

              - `AllowedDomains []string Optional`

                Only fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

              - `BlockedDomains []string Optional`

                Never fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

              - `Enabled bool Optional`

                Whether this tool is enabled and available to Claude. Overrides the default_config setting.

              - `MaxContentTokens int64 Optional`

                Maximum number of tokens of fetched text content to include in context per call. Does not apply to binary content such as PDFs.

                format: int32

              - `PermissionPolicy BetaManagedAgentsWebFetchToolConfigParamsPermissionPolicyUnionResp Optional`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

              - `Type BetaManagedAgentsWebFetchToolConfigParamsType Optional`

            - `type BetaManagedAgentsWebSearchToolConfigParamsResp struct{…}`

              Configuration override for the web_search tool.

              - `Name WebSearch`

                Must be "web_search".

              - `AllowedDomains []string Optional`

                Only return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

              - `BlockedDomains []string Optional`

                Never return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

              - `Enabled bool Optional`

                Whether this tool is enabled and available to Claude. Overrides the default_config setting.

              - `PermissionPolicy BetaManagedAgentsWebSearchToolConfigParamsPermissionPolicyUnionResp Optional`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

              - `Type BetaManagedAgentsWebSearchToolConfigParamsType Optional`

              - `UserLocation BetaManagedAgentsUserLocation Optional`

                Approximate user location for search result localization.

                - `Type Approximate`

                  Location precision. Only "approximate" is supported.

                - `City string Optional`

                  City name.

                  minLength: 1, maxLength: 255

                - `Country string Optional`

                  Two-letter ISO 3166-1 country code, uppercase.

                - `Region string Optional`

                  Region or state name.

                  minLength: 1, maxLength: 255

                - `Timezone string Optional`

                  IANA timezone identifier, e.g. "America/Los_Angeles".

                  minLength: 1, maxLength: 255

          - `DefaultConfig BetaManagedAgentsAgentToolsetDefaultConfigParamsResp Optional`

            Default configuration for all tools in a toolset.

            - `Enabled bool Optional`

              Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

            - `PermissionPolicy BetaManagedAgentsAgentToolsetDefaultConfigParamsPermissionPolicyUnionResp Optional`

              Permission policy for tool execution.

              - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                Tool calls are automatically approved without user confirmation.

              - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                Tool calls require user confirmation before execution.

        - `type BetaManagedAgentsMCPToolsetParamsResp struct{…}`

          Configuration for tools from an MCP server defined in `mcp_servers`.

          - `MCPServerName string`

            Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

            minLength: 1, maxLength: 255

          - `Type BetaManagedAgentsMCPToolsetParamsType`

          - `Configs []BetaManagedAgentsMCPToolConfigParamsResp Optional`

            Per-tool configuration overrides.

            - `Name string`

              Name of the MCP tool to configure. 1-128 characters.

              minLength: 1, maxLength: 128

            - `Enabled bool Optional`

              Whether this tool is enabled. Overrides the `default_config` setting.

            - `PermissionPolicy BetaManagedAgentsMCPToolConfigParamsPermissionPolicyUnionResp Optional`

              Permission policy for tool execution.

              - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                Tool calls are automatically approved without user confirmation.

              - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                Tool calls require user confirmation before execution.

          - `DefaultConfig BetaManagedAgentsMCPToolsetDefaultConfigParamsResp Optional`

            Default configuration for all tools from an MCP server.

            - `Enabled bool Optional`

              Whether tools are enabled by default. Defaults to true if not specified.

            - `PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigParamsPermissionPolicyUnionResp Optional`

              Permission policy for tool execution.

              - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                Tool calls are automatically approved without user confirmation.

              - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                Tool calls require user confirmation before execution.

        - `type BetaManagedAgentsCustomToolParamsResp struct{…}`

          A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

          - `Description string`

            Description of what the tool does, shown to the agent to help it decide when to use the tool.

            minLength: 1

          - `InputSchema BetaManagedAgentsCustomToolInputSchema`

            JSON Schema for custom tool input parameters.

            - `Type Object`

            - `Properties map[string, any] Optional`

            - `Required []string Optional`

          - `Name string`

            Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

            minLength: 1, maxLength: 128

          - `Type BetaManagedAgentsCustomToolParamsType`

      - `Version int64 Optional`

        The specific `agent` version to use. Omit to use the latest version.

        format: int32

  - `EnvironmentID param.Field[string]`

    Body param: ID of the `environment` defining the container configuration for this session.

    minLength: 1, maxLength: 128

  - `Budget param.Field[BetaManagedAgentsBudgetLimit] Optional`

    Body param: A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

  - `InitialEvents param.Field[[]BetaSessionNewParamsInitialEventUnion] Optional`

    Body param: Initial events to send to the `session` at creation, processed in order. Supports `user.message` and `user.define_outcome` events. Maximum 50 events.

    - `type BetaManagedAgentsUserMessageEventParams struct{…}`

      Parameters for sending a user message to the session.

      - `Content []BetaManagedAgentsUserMessageEventParamsContentUnionResp`

        Array of content blocks for the user message.

        - `type BetaManagedAgentsTextBlock struct{…}`

          Regular text content.

          - `Text string`

            The text content.

            minLength: 1

          - `Type BetaManagedAgentsTextBlockType`

        - `type BetaManagedAgentsImageBlock struct{…}`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source BetaManagedAgentsImageBlockSourceUnion`

            Union type for image source variants.

            - `type BetaManagedAgentsBase64ImageSource struct{…}`

              Base64-encoded image data.

              - `Data string`

                Base64-encoded image data.

                minLength: 1

              - `MediaType string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `Type BetaManagedAgentsBase64ImageSourceType`

            - `type BetaManagedAgentsURLImageSource struct{…}`

              Image referenced by URL.

              - `Type BetaManagedAgentsURLImageSourceType`

              - `URL string`

                URL of the image to fetch.

                minLength: 1

            - `type BetaManagedAgentsFileImageSource struct{…}`

              Image referenced by file ID.

              - `FileID string`

                ID of a previously uploaded file.

                minLength: 1

              - `Type BetaManagedAgentsFileImageSourceType`

          - `Type BetaManagedAgentsImageBlockType`

        - `type BetaManagedAgentsDocumentBlock struct{…}`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source BetaManagedAgentsDocumentBlockSourceUnion`

            Union type for document source variants.

            - `type BetaManagedAgentsBase64DocumentSource struct{…}`

              Base64-encoded document data.

              - `Data string`

                Base64-encoded document data.

                minLength: 1

              - `MediaType string`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `Type BetaManagedAgentsBase64DocumentSourceType`

            - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

              Plain text document content.

              - `Data string`

                The plain text content.

                minLength: 1

              - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

                MIME type of the text content. Must be "text/plain".

              - `Type BetaManagedAgentsPlainTextDocumentSourceType`

            - `type BetaManagedAgentsURLDocumentSource struct{…}`

              Document referenced by URL.

              - `Type BetaManagedAgentsURLDocumentSourceType`

              - `URL string`

                URL of the document to fetch.

                minLength: 1

            - `type BetaManagedAgentsFileDocumentSource struct{…}`

              Document referenced by file ID.

              - `FileID string`

                ID of a previously uploaded file.

                minLength: 1

              - `Type BetaManagedAgentsFileDocumentSourceType`

          - `Type BetaManagedAgentsDocumentBlockType`

          - `Context string Optional`

            Additional context about the document for the model.

          - `Title string Optional`

            The title of the document.

        - `type BetaManagedAgentsRedactedBlockParam struct{…}`

          Placeholder for content withheld by Anthropic model policy.

          - `Type BetaManagedAgentsRedactedBlockType`

      - `Type BetaManagedAgentsUserMessageEventParamsType`

    - `type BetaManagedAgentsUserDefineOutcomeEventParams struct{…}`

      Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

      - `Description string`

        What the agent should produce. This is the task specification.

      - `Rubric BetaManagedAgentsUserDefineOutcomeEventParamsRubricUnionResp`

        Rubric for grading the quality of an outcome.

        - `type BetaManagedAgentsFileRubricParams struct{…}`

          Rubric referenced by a file uploaded via the Files API.

          - `FileID string`

            ID of the rubric file.

          - `Type BetaManagedAgentsFileRubricParamsType`

        - `type BetaManagedAgentsTextRubricParams struct{…}`

          Rubric content provided inline as text.

          - `Content string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

            maxLength: 262144

          - `Type BetaManagedAgentsTextRubricParamsType`

      - `Type BetaManagedAgentsUserDefineOutcomeEventParamsType`

      - `MaxIterations int64 Optional`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

  - `Metadata param.Field[map[string, string]] Optional`

    Body param: Arbitrary key-value metadata attached to the session. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `Resources param.Field[[]BetaSessionNewParamsResourceUnion] Optional`

    Body param: Resources (e.g. repositories, files) to mount into the session's container.

    - `type BetaManagedAgentsGitHubRepositoryResourceParamsResp struct{…}`

      Mount a GitHub repository into the session's container.

      - `AuthorizationToken string`

        GitHub authorization token used to clone the repository.

        minLength: 1, maxLength: 4096

      - `Type BetaManagedAgentsGitHubRepositoryResourceParamsType`

      - `URL string`

        Github URL of the repository

        minLength: 1, maxLength: 2048

      - `Checkout BetaManagedAgentsGitHubRepositoryResourceParamsCheckoutUnionResp Optional`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `type BetaManagedAgentsBranchCheckout struct{…}`

          - `Name string`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `Type BetaManagedAgentsBranchCheckoutType`

        - `type BetaManagedAgentsCommitCheckout struct{…}`

          - `Sha string`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `Type BetaManagedAgentsCommitCheckoutType`

      - `MountPath string Optional`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

        minLength: 1, maxLength: 4096

    - `type BetaManagedAgentsFileResourceParamsResp struct{…}`

      Mount a file uploaded via the Files API into the session.

      - `FileID string`

        ID of a previously uploaded file.

        minLength: 1, maxLength: 128

      - `Type BetaManagedAgentsFileResourceParamsType`

      - `MountPath string Optional`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

        minLength: 1, maxLength: 4096

    - `type BetaManagedAgentsMemoryStoreResourceParamResp struct{…}`

      Parameters for attaching a memory store to an agent session.

      - `MemoryStoreID string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type BetaManagedAgentsMemoryStoreResourceParamType`

      - `Access BetaManagedAgentsMemoryStoreResourceParamAccess Optional`

        Access mode for an attached memory store.

        - `const BetaManagedAgentsMemoryStoreResourceParamAccessReadWrite BetaManagedAgentsMemoryStoreResourceParamAccess = "read_write"`

        - `const BetaManagedAgentsMemoryStoreResourceParamAccessReadOnly BetaManagedAgentsMemoryStoreResourceParamAccess = "read_only"`

      - `Instructions string Optional`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

        maxLength: 4096

  - `Title param.Field[string] Optional`

    Body param: Human-readable session title.

    maxLength: 500

  - `VaultIDs param.Field[[]string] Optional`

    Body param: Vault IDs for stored credentials the agent can use during the session.

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

### Returns

- `type BetaManagedAgentsSession struct{…}`

  A Managed Agents `session`.

  - `ID string`

  - `Agent BetaManagedAgentsSessionAgent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `ID string`

    - `Description string`

    - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

      - `Name string`

      - `Type BetaManagedAgentsMCPServerURLDefinitionType`

      - `URL string`

    - `Model BetaManagedAgentsModelConfig`

      Model identifier and configuration.

      - `ID BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `type BetaManagedAgentsModel string`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `const BetaManagedAgentsModelClaudeSonnet5 BetaManagedAgentsModel = "claude-sonnet-5"`

            High-performance model for coding and agents

          - `const BetaManagedAgentsModelClaudeFable5 BetaManagedAgentsModel = "claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `const BetaManagedAgentsModelClaudeOpus5 BetaManagedAgentsModel = "claude-opus-5"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeOpus4_8 BetaManagedAgentsModel = "claude-opus-4-8"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeOpus4_7 BetaManagedAgentsModel = "claude-opus-4-7"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeOpus4_6 BetaManagedAgentsModel = "claude-opus-4-6"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeSonnet4_6 BetaManagedAgentsModel = "claude-sonnet-4-6"`

            Best combination of speed and intelligence

          - `const BetaManagedAgentsModelClaudeHaiku4_5 BetaManagedAgentsModel = "claude-haiku-4-5"`

            Fastest model with near-frontier intelligence

          - `const BetaManagedAgentsModelClaudeHaiku4_5_20251001 BetaManagedAgentsModel = "claude-haiku-4-5-20251001"`

            Fastest model with near-frontier intelligence

          - `const BetaManagedAgentsModelClaudeOpus4_5 BetaManagedAgentsModel = "claude-opus-4-5"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeOpus4_5_20251101 BetaManagedAgentsModel = "claude-opus-4-5-20251101"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeSonnet4_5 BetaManagedAgentsModel = "claude-sonnet-4-5"`

            High-performance model for agents and coding

          - `const BetaManagedAgentsModelClaudeSonnet4_5_20250929 BetaManagedAgentsModel = "claude-sonnet-4-5-20250929"`

            High-performance model for agents and coding

        - `string`

      - `Effort BetaManagedAgentsModelConfigEffortUnion Optional`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

        - `type BetaManagedAgentsEffortLow struct{…}`

          Low effort. Favors latency over reasoning depth.

          - `Type BetaManagedAgentsEffortLowType`

        - `type BetaManagedAgentsEffortMedium struct{…}`

          Medium effort. Balances latency and reasoning depth.

          - `Type BetaManagedAgentsEffortMediumType`

        - `type BetaManagedAgentsEffortHigh struct{…}`

          High effort. Favors reasoning depth.

          - `Type BetaManagedAgentsEffortHighType`

        - `type BetaManagedAgentsEffortXhigh struct{…}`

          Extra-high effort. Not all models accept this level.

          - `Type BetaManagedAgentsEffortXhighType`

        - `type BetaManagedAgentsEffortMax struct{…}`

          Maximum effort. Favors reasoning depth over latency.

          - `Type BetaManagedAgentsEffortMaxType`

      - `InferenceGeo string Optional`

        Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

      - `Speed BetaManagedAgentsModelConfigSpeed Optional`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `const BetaManagedAgentsModelConfigSpeedStandard BetaManagedAgentsModelConfigSpeed = "standard"`

        - `const BetaManagedAgentsModelConfigSpeedFast BetaManagedAgentsModelConfigSpeed = "fast"`

    - `Multiagent BetaManagedAgentsSessionMultiagentCoordinator`

      Resolved coordinator topology with full agent definitions for each roster member.

      - `Agents []BetaManagedAgentsSessionMultiagentCoordinatorAgentUnion`

        Full `agent` definitions the coordinator may spawn as session threads.

        - `type BetaManagedAgentsSessionThreadAgent struct{…}`

          Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

          - `ID string`

          - `Description string`

          - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

            - `Name string`

            - `Type BetaManagedAgentsMCPServerURLDefinitionType`

            - `URL string`

          - `Model BetaManagedAgentsModelConfig`

            Model identifier and configuration.

          - `Name string`

          - `Skills []BetaManagedAgentsSessionThreadAgentSkillUnion`

            - `type BetaManagedAgentsAnthropicSkill struct{…}`

              A resolved Anthropic-managed skill.

              - `SkillID string`

              - `Type BetaManagedAgentsAnthropicSkillType`

              - `Version string`

            - `type BetaManagedAgentsCustomSkill struct{…}`

              A resolved user-created custom skill.

              - `SkillID string`

              - `Type BetaManagedAgentsCustomSkillType`

              - `Version string`

          - `System string`

          - `Tools []BetaManagedAgentsSessionThreadAgentToolUnion`

            - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

              - `Configs []BetaManagedAgentsAgentToolConfigUnion`

                - `type BetaManagedAgentsBashToolConfig struct{…}`

                  Configuration for the bash tool.

                  - `Enabled bool`

                  - `Name Bash`

                  - `PermissionPolicy BetaManagedAgentsBashToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                      - `Type BetaManagedAgentsAlwaysAllowPolicyType`

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                      - `Type BetaManagedAgentsAlwaysAskPolicyType`

                  - `Type Bash`

                - `type BetaManagedAgentsEditToolConfig struct{…}`

                  Configuration for the edit tool.

                  - `Enabled bool`

                  - `Name Edit`

                  - `PermissionPolicy BetaManagedAgentsEditToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type Edit`

                - `type BetaManagedAgentsReadToolConfig struct{…}`

                  Configuration for the read tool.

                  - `Enabled bool`

                  - `Name Read`

                  - `PermissionPolicy BetaManagedAgentsReadToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type Read`

                - `type BetaManagedAgentsWriteToolConfig struct{…}`

                  Configuration for the write tool.

                  - `Enabled bool`

                  - `Name Write`

                  - `PermissionPolicy BetaManagedAgentsWriteToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type Write`

                - `type BetaManagedAgentsGlobToolConfig struct{…}`

                  Configuration for the glob tool.

                  - `Enabled bool`

                  - `Name Glob`

                  - `PermissionPolicy BetaManagedAgentsGlobToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type Glob`

                - `type BetaManagedAgentsGrepToolConfig struct{…}`

                  Configuration for the grep tool.

                  - `Enabled bool`

                  - `Name Grep`

                  - `PermissionPolicy BetaManagedAgentsGrepToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type Grep`

                - `type BetaManagedAgentsWebFetchToolConfig struct{…}`

                  Configuration for the web_fetch tool.

                  - `Enabled bool`

                  - `Name WebFetch`

                  - `PermissionPolicy BetaManagedAgentsWebFetchToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type WebFetch`

                  - `AllowedDomains []string Optional`

                  - `BlockedDomains []string Optional`

                  - `MaxContentTokens int64 Optional`

                    format: int32

                - `type BetaManagedAgentsWebSearchToolConfig struct{…}`

                  Configuration for the web_search tool.

                  - `Enabled bool`

                  - `Name WebSearch`

                  - `PermissionPolicy BetaManagedAgentsWebSearchToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type WebSearch`

                  - `AllowedDomains []string Optional`

                  - `BlockedDomains []string Optional`

                  - `UserLocation BetaManagedAgentsUserLocation Optional`

                    Approximate user location for search result localization.

                    - `Type Approximate`

                      Location precision. Only "approximate" is supported.

                    - `City string Optional`

                      City name.

                      minLength: 1, maxLength: 255

                    - `Country string Optional`

                      Two-letter ISO 3166-1 country code, uppercase.

                    - `Region string Optional`

                      Region or state name.

                      minLength: 1, maxLength: 255

                    - `Timezone string Optional`

                      IANA timezone identifier, e.g. "America/Los_Angeles".

                      minLength: 1, maxLength: 255

              - `DefaultConfig BetaManagedAgentsAgentToolsetDefaultConfig`

                Resolved default configuration for agent tools.

                - `Enabled bool`

                - `PermissionPolicy BetaManagedAgentsAgentToolsetDefaultConfigPermissionPolicyUnion`

                  Permission policy for tool execution.

                  - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                    Tool calls are automatically approved without user confirmation.

                  - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                    Tool calls require user confirmation before execution.

              - `Type BetaManagedAgentsAgentToolset20260401Type`

            - `type BetaManagedAgentsMCPToolset struct{…}`

              - `Configs []BetaManagedAgentsMCPToolConfig`

                - `Enabled bool`

                - `Name string`

                - `PermissionPolicy BetaManagedAgentsMCPToolConfigPermissionPolicyUnion`

                  Permission policy for tool execution.

                  - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                    Tool calls are automatically approved without user confirmation.

                  - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                    Tool calls require user confirmation before execution.

              - `DefaultConfig BetaManagedAgentsMCPToolsetDefaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `Enabled bool`

                - `PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigPermissionPolicyUnion`

                  Permission policy for tool execution.

                  - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                    Tool calls are automatically approved without user confirmation.

                  - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                    Tool calls require user confirmation before execution.

              - `MCPServerName string`

              - `Type BetaManagedAgentsMCPToolsetType`

            - `type BetaManagedAgentsCustomTool struct{…}`

              A custom tool as returned in API responses.

              - `Description string`

              - `InputSchema BetaManagedAgentsCustomToolInputSchema`

                JSON Schema for custom tool input parameters.

                - `Type Object`

                - `Properties map[string, any] Optional`

                - `Required []string Optional`

              - `Name string`

              - `Type BetaManagedAgentsCustomToolType`

          - `Type BetaManagedAgentsSessionThreadAgentType`

          - `Version int64`

            format: int32

        - `type BetaManagedAgentsAdvisor struct{…}`

          Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

          - `Model string`

            The advisor model id.

          - `Type BetaManagedAgentsAdvisorType`

      - `Type BetaManagedAgentsSessionMultiagentCoordinatorType`

    - `Name string`

    - `Skills []BetaManagedAgentsSessionAgentSkillUnion`

      - `type BetaManagedAgentsAnthropicSkill struct{…}`

        A resolved Anthropic-managed skill.

      - `type BetaManagedAgentsCustomSkill struct{…}`

        A resolved user-created custom skill.

    - `System string`

    - `Tools []BetaManagedAgentsSessionAgentToolUnion`

      - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

      - `type BetaManagedAgentsMCPToolset struct{…}`

      - `type BetaManagedAgentsCustomTool struct{…}`

        A custom tool as returned in API responses.

    - `Type BetaManagedAgentsSessionAgentType`

    - `Version int64`

      format: int32

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `Budget BetaManagedAgentsBudgetLimit`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `MaxListCost BetaMonetaryAmount`

      A monetary amount in a specific currency.

      - `Amount string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `Currency BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `Type BetaManagedAgentsBudgetLimitType`

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `EnvironmentID string`

  - `Metadata map[string, string]`

  - `OutcomeEvaluations []BetaManagedAgentsOutcomeEvaluationResource`

    Per-outcome evaluation state. One entry per define_outcome event sent to the session.

    - `CompletedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Description string`

      What the agent should produce.

    - `Explanation string`

      Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs_revision (intermediate), what's missing; for failed, why unrecoverable.

    - `Iteration int64`

      0-indexed revision cycle the outcome is currently on.

      format: int32

    - `OutcomeID string`

      Server-generated outc_ ID for this outcome.

    - `Result string`

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

    - `Type BetaManagedAgentsOutcomeEvaluationResourceType`

  - `Resources []BetaManagedAgentsSessionResourceUnion`

    - `type BetaManagedAgentsGitHubRepositoryResource struct{…}`

      - `ID string`

      - `CreatedAt Time`

        A timestamp in RFC 3339 format

        format: date-time

      - `MountPath string`

      - `Type BetaManagedAgentsGitHubRepositoryResourceType`

      - `UpdatedAt Time`

        A timestamp in RFC 3339 format

        format: date-time

      - `URL string`

      - `Checkout BetaManagedAgentsGitHubRepositoryResourceCheckoutUnion Optional`

        - `type BetaManagedAgentsBranchCheckout struct{…}`

          - `Name string`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `Type BetaManagedAgentsBranchCheckoutType`

        - `type BetaManagedAgentsCommitCheckout struct{…}`

          - `Sha string`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `Type BetaManagedAgentsCommitCheckoutType`

    - `type BetaManagedAgentsFileResource struct{…}`

      - `ID string`

      - `CreatedAt Time`

        A timestamp in RFC 3339 format

        format: date-time

      - `FileID string`

      - `MountPath string`

      - `Type BetaManagedAgentsFileResourceType`

      - `UpdatedAt Time`

        A timestamp in RFC 3339 format

        format: date-time

    - `type BetaManagedAgentsMemoryStoreResource struct{…}`

      A memory store attached to an agent session.

      - `MemoryStoreID string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type BetaManagedAgentsMemoryStoreResourceType`

      - `Access BetaManagedAgentsMemoryStoreResourceAccess Optional`

        Access mode for an attached memory store.

        - `const BetaManagedAgentsMemoryStoreResourceAccessReadWrite BetaManagedAgentsMemoryStoreResourceAccess = "read_write"`

        - `const BetaManagedAgentsMemoryStoreResourceAccessReadOnly BetaManagedAgentsMemoryStoreResourceAccess = "read_only"`

      - `Description string Optional`

        Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

      - `Instructions string Optional`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

        maxLength: 4096

      - `MountPath string Optional`

        Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

      - `Name string Optional`

        Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

  - `Stats BetaManagedAgentsSessionStats`

    Timing statistics for a session.

    - `ActiveSeconds float64 Optional`

      Cumulative time in seconds the session spent in running status. Excludes idle time.

      format: double

    - `DurationSeconds float64 Optional`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

      format: double

  - `Status BetaManagedAgentsSessionStatus`

    SessionStatus enum

    - `const BetaManagedAgentsSessionStatusRescheduling BetaManagedAgentsSessionStatus = "rescheduling"`

    - `const BetaManagedAgentsSessionStatusRunning BetaManagedAgentsSessionStatus = "running"`

    - `const BetaManagedAgentsSessionStatusIdle BetaManagedAgentsSessionStatus = "idle"`

    - `const BetaManagedAgentsSessionStatusTerminated BetaManagedAgentsSessionStatus = "terminated"`

  - `Title string`

  - `Type BetaManagedAgentsSessionType`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `Usage BetaManagedAgentsSessionUsage`

    Cumulative token usage for a session across all turns.

    - `ActiveSeconds float64 Optional`

      Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once, unlike `stats.active_seconds`, which sums each thread's own active time. This is the duration the session's runtime cost is priced on.

      format: double

    - `CacheCreation BetaManagedAgentsCacheCreationUsage Optional`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `Ephemeral1hInputTokens int64 Optional`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `Ephemeral5mInputTokens int64 Optional`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `CacheReadInputTokens int64 Optional`

      Total tokens read from prompt cache.

      format: int32

    - `InputTokens int64 Optional`

      Total input tokens consumed across all turns.

      format: int32

    - `ListCost BetaMonetaryAmount Optional`

      A monetary amount in a specific currency.

    - `OutputTokens int64 Optional`

      Total output tokens generated across all turns.

      format: int32

    - `ServerToolUse BetaManagedAgentsServerToolUsage Optional`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `WebFetchRequests int64 Optional`

        Number of server-executed web fetch requests.

        format: int32

      - `WebSearchRequests int64 Optional`

        Number of server-executed web search requests.

        format: int32

  - `VaultIDs []string`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `DeploymentID string Optional`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Example

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
	betaManagedAgentsSession, err := client.Beta.Sessions.New(context.TODO(), anthropic.BetaSessionNewParams{
		Agent: anthropic.BetaSessionNewParamsAgentUnion{
			OfString: anthropic.String("agent_011CZkYpogX7uDKUyvBTophP"),
		},
		EnvironmentID: "env_011CZkZ9X2dpNyB7HsEFoRfW",
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaManagedAgentsSession.ID)
}
```

#### Response (200)

```json
{
  "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "description": "A general-purpose starter agent.",
    "mcp_servers": [
      {
        "name": "example-mcp",
        "type": "url",
        "url": "https://example-server.modelcontextprotocol.io/sse"
      }
    ],
    "model": {
      "id": "claude-opus-5",
      "effort": {
        "type": "low"
      },
      "inference_geo": "inference_geo",
      "speed": "standard"
    },
    "multiagent": {
      "agents": [
        {
          "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
          "description": "A focused research subagent.",
          "mcp_servers": [
            {
              "name": "example-mcp",
              "type": "url",
              "url": "https://example-server.modelcontextprotocol.io/sse"
            }
          ],
          "model": {
            "id": "claude-opus-5",
            "effort": {
              "type": "low"
            },
            "inference_geo": "inference_geo",
            "speed": "standard"
          },
          "name": "Researcher",
          "skills": [
            {
              "skill_id": "xlsx",
              "type": "anthropic",
              "version": "1"
            }
          ],
          "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
          "tools": [
            {
              "configs": [
                {
                  "enabled": true,
                  "name": "bash",
                  "permission_policy": {
                    "type": "always_allow"
                  },
                  "type": "bash"
                }
              ],
              "default_config": {
                "enabled": true,
                "permission_policy": {
                  "type": "always_ask"
                }
              },
              "type": "agent_toolset_20260401"
            }
          ],
          "type": "agent",
          "version": 1
        }
      ],
      "type": "coordinator"
    },
    "name": "My First Agent",
    "skills": [
      {
        "skill_id": "xlsx",
        "type": "anthropic",
        "version": "1"
      },
      {
        "skill_id": "skill_011CZkZFNu9hAbo3jZPRgTlx",
        "type": "custom",
        "version": "2"
      }
    ],
    "system": "You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.",
    "tools": [
      {
        "configs": [
          {
            "enabled": true,
            "name": "bash",
            "permission_policy": {
              "type": "always_allow"
            },
            "type": "bash"
          }
        ],
        "default_config": {
          "enabled": true,
          "permission_policy": {
            "type": "always_ask"
          }
        },
        "type": "agent_toolset_20260401"
      }
    ],
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "budget": {
    "max_list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "type": "limit"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "metadata": {},
  "outcome_evaluations": [
    {
      "completed_at": "2026-03-15T10:02:31Z",
      "description": "Produce a 2-page summary as summary.md",
      "explanation": "All five sections present with inline citations.",
      "iteration": 0,
      "outcome_id": "outc_011CZkZRSw2kEfs6ncTVljxP",
      "result": "satisfied",
      "type": "outcome_evaluation"
    }
  ],
  "resources": [
    {
      "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
      "created_at": "2026-03-15T10:00:00Z",
      "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
      "mount_path": "/uploads/receipt.pdf",
      "type": "file",
      "updated_at": "2026-03-15T10:00:00Z"
    },
    {
      "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
      "created_at": "2026-03-15T10:00:00Z",
      "mount_path": "/workspace/example-repo",
      "type": "github_repository",
      "updated_at": "2026-03-15T10:00:00Z",
      "url": "https://github.com/example-org/example-repo",
      "checkout": {
        "name": "main",
        "type": "branch"
      }
    }
  ],
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0
  },
  "status": "idle",
  "title": "Order #1234 inquiry",
  "type": "session",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "active_seconds": 0,
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "output_tokens": 0,
    "server_tool_use": {
      "web_fetch_requests": 0,
      "web_search_requests": 3
    }
  },
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "deployment_id": "deployment_id"
}
```

## List Sessions

`client.Beta.Sessions.List(ctx, params) (*BidirectionalPageCursor[BetaManagedAgentsSession], error)`

**GET** `/v1/sessions`

List Sessions

### Parameters

- `params BetaSessionListParams`

  - `AgentID param.Field[string] Optional`

    Query param: Filter sessions created with this agent ID.

  - `AgentVersion param.Field[int64] Optional`

    Query param: Filter by agent version. Only applies when agent_id is also set.

    format: int32

  - `CreatedAtGt param.Field[Time] Optional`

    Query param: Return sessions created after this time (exclusive).

    format: date-time

  - `CreatedAtGte param.Field[Time] Optional`

    Query param: Return sessions created at or after this time (inclusive).

    format: date-time

  - `CreatedAtLt param.Field[Time] Optional`

    Query param: Return sessions created before this time (exclusive).

    format: date-time

  - `CreatedAtLte param.Field[Time] Optional`

    Query param: Return sessions created at or before this time (inclusive).

    format: date-time

  - `DeploymentID param.Field[string] Optional`

    Query param: Filter sessions created by this deployment ID.

  - `IncludeArchived param.Field[bool] Optional`

    Query param: When true, includes archived sessions. Default: false (exclude archived).

  - `Limit param.Field[int64] Optional`

    Query param: Maximum number of results to return.

    format: int32

  - `MemoryStoreID param.Field[string] Optional`

    Query param: Filter sessions whose resources contain a memory_store with this memory store ID.

  - `Order param.Field[BetaSessionListParamsOrder] Optional`

    Query param: Sort direction for results, ordered by created_at. Defaults to desc (newest first).

    - `const BetaSessionListParamsOrderAsc BetaSessionListParamsOrder = "asc"`

    - `const BetaSessionListParamsOrderDesc BetaSessionListParamsOrder = "desc"`

  - `Page param.Field[string] Optional`

    Query param: Opaque pagination cursor from a previous response.

  - `Statuses param.Field[[]string] Optional`

    Query param: Filter by session status. Repeat the parameter to match any of multiple statuses.

    - `const BetaSessionListParamsStatusRescheduling BetaSessionListParamsStatus = "rescheduling"`

    - `const BetaSessionListParamsStatusRunning BetaSessionListParamsStatus = "running"`

    - `const BetaSessionListParamsStatusIdle BetaSessionListParamsStatus = "idle"`

    - `const BetaSessionListParamsStatusTerminated BetaSessionListParamsStatus = "terminated"`

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

### Returns

- `type BetaManagedAgentsSession struct{…}`

  A Managed Agents `session`.

  - `ID string`

  - `Agent BetaManagedAgentsSessionAgent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `ID string`

    - `Description string`

    - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

      - `Name string`

      - `Type BetaManagedAgentsMCPServerURLDefinitionType`

      - `URL string`

    - `Model BetaManagedAgentsModelConfig`

      Model identifier and configuration.

      - `ID BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `type BetaManagedAgentsModel string`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `const BetaManagedAgentsModelClaudeSonnet5 BetaManagedAgentsModel = "claude-sonnet-5"`

            High-performance model for coding and agents

          - `const BetaManagedAgentsModelClaudeFable5 BetaManagedAgentsModel = "claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `const BetaManagedAgentsModelClaudeOpus5 BetaManagedAgentsModel = "claude-opus-5"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeOpus4_8 BetaManagedAgentsModel = "claude-opus-4-8"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeOpus4_7 BetaManagedAgentsModel = "claude-opus-4-7"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeOpus4_6 BetaManagedAgentsModel = "claude-opus-4-6"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeSonnet4_6 BetaManagedAgentsModel = "claude-sonnet-4-6"`

            Best combination of speed and intelligence

          - `const BetaManagedAgentsModelClaudeHaiku4_5 BetaManagedAgentsModel = "claude-haiku-4-5"`

            Fastest model with near-frontier intelligence

          - `const BetaManagedAgentsModelClaudeHaiku4_5_20251001 BetaManagedAgentsModel = "claude-haiku-4-5-20251001"`

            Fastest model with near-frontier intelligence

          - `const BetaManagedAgentsModelClaudeOpus4_5 BetaManagedAgentsModel = "claude-opus-4-5"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeOpus4_5_20251101 BetaManagedAgentsModel = "claude-opus-4-5-20251101"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeSonnet4_5 BetaManagedAgentsModel = "claude-sonnet-4-5"`

            High-performance model for agents and coding

          - `const BetaManagedAgentsModelClaudeSonnet4_5_20250929 BetaManagedAgentsModel = "claude-sonnet-4-5-20250929"`

            High-performance model for agents and coding

        - `string`

      - `Effort BetaManagedAgentsModelConfigEffortUnion Optional`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

        - `type BetaManagedAgentsEffortLow struct{…}`

          Low effort. Favors latency over reasoning depth.

          - `Type BetaManagedAgentsEffortLowType`

        - `type BetaManagedAgentsEffortMedium struct{…}`

          Medium effort. Balances latency and reasoning depth.

          - `Type BetaManagedAgentsEffortMediumType`

        - `type BetaManagedAgentsEffortHigh struct{…}`

          High effort. Favors reasoning depth.

          - `Type BetaManagedAgentsEffortHighType`

        - `type BetaManagedAgentsEffortXhigh struct{…}`

          Extra-high effort. Not all models accept this level.

          - `Type BetaManagedAgentsEffortXhighType`

        - `type BetaManagedAgentsEffortMax struct{…}`

          Maximum effort. Favors reasoning depth over latency.

          - `Type BetaManagedAgentsEffortMaxType`

      - `InferenceGeo string Optional`

        Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

      - `Speed BetaManagedAgentsModelConfigSpeed Optional`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `const BetaManagedAgentsModelConfigSpeedStandard BetaManagedAgentsModelConfigSpeed = "standard"`

        - `const BetaManagedAgentsModelConfigSpeedFast BetaManagedAgentsModelConfigSpeed = "fast"`

    - `Multiagent BetaManagedAgentsSessionMultiagentCoordinator`

      Resolved coordinator topology with full agent definitions for each roster member.

      - `Agents []BetaManagedAgentsSessionMultiagentCoordinatorAgentUnion`

        Full `agent` definitions the coordinator may spawn as session threads.

        - `type BetaManagedAgentsSessionThreadAgent struct{…}`

          Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

          - `ID string`

          - `Description string`

          - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

            - `Name string`

            - `Type BetaManagedAgentsMCPServerURLDefinitionType`

            - `URL string`

          - `Model BetaManagedAgentsModelConfig`

            Model identifier and configuration.

          - `Name string`

          - `Skills []BetaManagedAgentsSessionThreadAgentSkillUnion`

            - `type BetaManagedAgentsAnthropicSkill struct{…}`

              A resolved Anthropic-managed skill.

              - `SkillID string`

              - `Type BetaManagedAgentsAnthropicSkillType`

              - `Version string`

            - `type BetaManagedAgentsCustomSkill struct{…}`

              A resolved user-created custom skill.

              - `SkillID string`

              - `Type BetaManagedAgentsCustomSkillType`

              - `Version string`

          - `System string`

          - `Tools []BetaManagedAgentsSessionThreadAgentToolUnion`

            - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

              - `Configs []BetaManagedAgentsAgentToolConfigUnion`

                - `type BetaManagedAgentsBashToolConfig struct{…}`

                  Configuration for the bash tool.

                  - `Enabled bool`

                  - `Name Bash`

                  - `PermissionPolicy BetaManagedAgentsBashToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                      - `Type BetaManagedAgentsAlwaysAllowPolicyType`

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                      - `Type BetaManagedAgentsAlwaysAskPolicyType`

                  - `Type Bash`

                - `type BetaManagedAgentsEditToolConfig struct{…}`

                  Configuration for the edit tool.

                  - `Enabled bool`

                  - `Name Edit`

                  - `PermissionPolicy BetaManagedAgentsEditToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type Edit`

                - `type BetaManagedAgentsReadToolConfig struct{…}`

                  Configuration for the read tool.

                  - `Enabled bool`

                  - `Name Read`

                  - `PermissionPolicy BetaManagedAgentsReadToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type Read`

                - `type BetaManagedAgentsWriteToolConfig struct{…}`

                  Configuration for the write tool.

                  - `Enabled bool`

                  - `Name Write`

                  - `PermissionPolicy BetaManagedAgentsWriteToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type Write`

                - `type BetaManagedAgentsGlobToolConfig struct{…}`

                  Configuration for the glob tool.

                  - `Enabled bool`

                  - `Name Glob`

                  - `PermissionPolicy BetaManagedAgentsGlobToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type Glob`

                - `type BetaManagedAgentsGrepToolConfig struct{…}`

                  Configuration for the grep tool.

                  - `Enabled bool`

                  - `Name Grep`

                  - `PermissionPolicy BetaManagedAgentsGrepToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type Grep`

                - `type BetaManagedAgentsWebFetchToolConfig struct{…}`

                  Configuration for the web_fetch tool.

                  - `Enabled bool`

                  - `Name WebFetch`

                  - `PermissionPolicy BetaManagedAgentsWebFetchToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type WebFetch`

                  - `AllowedDomains []string Optional`

                  - `BlockedDomains []string Optional`

                  - `MaxContentTokens int64 Optional`

                    format: int32

                - `type BetaManagedAgentsWebSearchToolConfig struct{…}`

                  Configuration for the web_search tool.

                  - `Enabled bool`

                  - `Name WebSearch`

                  - `PermissionPolicy BetaManagedAgentsWebSearchToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type WebSearch`

                  - `AllowedDomains []string Optional`

                  - `BlockedDomains []string Optional`

                  - `UserLocation BetaManagedAgentsUserLocation Optional`

                    Approximate user location for search result localization.

                    - `Type Approximate`

                      Location precision. Only "approximate" is supported.

                    - `City string Optional`

                      City name.

                      minLength: 1, maxLength: 255

                    - `Country string Optional`

                      Two-letter ISO 3166-1 country code, uppercase.

                    - `Region string Optional`

                      Region or state name.

                      minLength: 1, maxLength: 255

                    - `Timezone string Optional`

                      IANA timezone identifier, e.g. "America/Los_Angeles".

                      minLength: 1, maxLength: 255

              - `DefaultConfig BetaManagedAgentsAgentToolsetDefaultConfig`

                Resolved default configuration for agent tools.

                - `Enabled bool`

                - `PermissionPolicy BetaManagedAgentsAgentToolsetDefaultConfigPermissionPolicyUnion`

                  Permission policy for tool execution.

                  - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                    Tool calls are automatically approved without user confirmation.

                  - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                    Tool calls require user confirmation before execution.

              - `Type BetaManagedAgentsAgentToolset20260401Type`

            - `type BetaManagedAgentsMCPToolset struct{…}`

              - `Configs []BetaManagedAgentsMCPToolConfig`

                - `Enabled bool`

                - `Name string`

                - `PermissionPolicy BetaManagedAgentsMCPToolConfigPermissionPolicyUnion`

                  Permission policy for tool execution.

                  - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                    Tool calls are automatically approved without user confirmation.

                  - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                    Tool calls require user confirmation before execution.

              - `DefaultConfig BetaManagedAgentsMCPToolsetDefaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `Enabled bool`

                - `PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigPermissionPolicyUnion`

                  Permission policy for tool execution.

                  - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                    Tool calls are automatically approved without user confirmation.

                  - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                    Tool calls require user confirmation before execution.

              - `MCPServerName string`

              - `Type BetaManagedAgentsMCPToolsetType`

            - `type BetaManagedAgentsCustomTool struct{…}`

              A custom tool as returned in API responses.

              - `Description string`

              - `InputSchema BetaManagedAgentsCustomToolInputSchema`

                JSON Schema for custom tool input parameters.

                - `Type Object`

                - `Properties map[string, any] Optional`

                - `Required []string Optional`

              - `Name string`

              - `Type BetaManagedAgentsCustomToolType`

          - `Type BetaManagedAgentsSessionThreadAgentType`

          - `Version int64`

            format: int32

        - `type BetaManagedAgentsAdvisor struct{…}`

          Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

          - `Model string`

            The advisor model id.

          - `Type BetaManagedAgentsAdvisorType`

      - `Type BetaManagedAgentsSessionMultiagentCoordinatorType`

    - `Name string`

    - `Skills []BetaManagedAgentsSessionAgentSkillUnion`

      - `type BetaManagedAgentsAnthropicSkill struct{…}`

        A resolved Anthropic-managed skill.

      - `type BetaManagedAgentsCustomSkill struct{…}`

        A resolved user-created custom skill.

    - `System string`

    - `Tools []BetaManagedAgentsSessionAgentToolUnion`

      - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

      - `type BetaManagedAgentsMCPToolset struct{…}`

      - `type BetaManagedAgentsCustomTool struct{…}`

        A custom tool as returned in API responses.

    - `Type BetaManagedAgentsSessionAgentType`

    - `Version int64`

      format: int32

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `Budget BetaManagedAgentsBudgetLimit`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `MaxListCost BetaMonetaryAmount`

      A monetary amount in a specific currency.

      - `Amount string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `Currency BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `Type BetaManagedAgentsBudgetLimitType`

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `EnvironmentID string`

  - `Metadata map[string, string]`

  - `OutcomeEvaluations []BetaManagedAgentsOutcomeEvaluationResource`

    Per-outcome evaluation state. One entry per define_outcome event sent to the session.

    - `CompletedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Description string`

      What the agent should produce.

    - `Explanation string`

      Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs_revision (intermediate), what's missing; for failed, why unrecoverable.

    - `Iteration int64`

      0-indexed revision cycle the outcome is currently on.

      format: int32

    - `OutcomeID string`

      Server-generated outc_ ID for this outcome.

    - `Result string`

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

    - `Type BetaManagedAgentsOutcomeEvaluationResourceType`

  - `Resources []BetaManagedAgentsSessionResourceUnion`

    - `type BetaManagedAgentsGitHubRepositoryResource struct{…}`

      - `ID string`

      - `CreatedAt Time`

        A timestamp in RFC 3339 format

        format: date-time

      - `MountPath string`

      - `Type BetaManagedAgentsGitHubRepositoryResourceType`

      - `UpdatedAt Time`

        A timestamp in RFC 3339 format

        format: date-time

      - `URL string`

      - `Checkout BetaManagedAgentsGitHubRepositoryResourceCheckoutUnion Optional`

        - `type BetaManagedAgentsBranchCheckout struct{…}`

          - `Name string`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `Type BetaManagedAgentsBranchCheckoutType`

        - `type BetaManagedAgentsCommitCheckout struct{…}`

          - `Sha string`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `Type BetaManagedAgentsCommitCheckoutType`

    - `type BetaManagedAgentsFileResource struct{…}`

      - `ID string`

      - `CreatedAt Time`

        A timestamp in RFC 3339 format

        format: date-time

      - `FileID string`

      - `MountPath string`

      - `Type BetaManagedAgentsFileResourceType`

      - `UpdatedAt Time`

        A timestamp in RFC 3339 format

        format: date-time

    - `type BetaManagedAgentsMemoryStoreResource struct{…}`

      A memory store attached to an agent session.

      - `MemoryStoreID string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type BetaManagedAgentsMemoryStoreResourceType`

      - `Access BetaManagedAgentsMemoryStoreResourceAccess Optional`

        Access mode for an attached memory store.

        - `const BetaManagedAgentsMemoryStoreResourceAccessReadWrite BetaManagedAgentsMemoryStoreResourceAccess = "read_write"`

        - `const BetaManagedAgentsMemoryStoreResourceAccessReadOnly BetaManagedAgentsMemoryStoreResourceAccess = "read_only"`

      - `Description string Optional`

        Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

      - `Instructions string Optional`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

        maxLength: 4096

      - `MountPath string Optional`

        Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

      - `Name string Optional`

        Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

  - `Stats BetaManagedAgentsSessionStats`

    Timing statistics for a session.

    - `ActiveSeconds float64 Optional`

      Cumulative time in seconds the session spent in running status. Excludes idle time.

      format: double

    - `DurationSeconds float64 Optional`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

      format: double

  - `Status BetaManagedAgentsSessionStatus`

    SessionStatus enum

    - `const BetaManagedAgentsSessionStatusRescheduling BetaManagedAgentsSessionStatus = "rescheduling"`

    - `const BetaManagedAgentsSessionStatusRunning BetaManagedAgentsSessionStatus = "running"`

    - `const BetaManagedAgentsSessionStatusIdle BetaManagedAgentsSessionStatus = "idle"`

    - `const BetaManagedAgentsSessionStatusTerminated BetaManagedAgentsSessionStatus = "terminated"`

  - `Title string`

  - `Type BetaManagedAgentsSessionType`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `Usage BetaManagedAgentsSessionUsage`

    Cumulative token usage for a session across all turns.

    - `ActiveSeconds float64 Optional`

      Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once, unlike `stats.active_seconds`, which sums each thread's own active time. This is the duration the session's runtime cost is priced on.

      format: double

    - `CacheCreation BetaManagedAgentsCacheCreationUsage Optional`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `Ephemeral1hInputTokens int64 Optional`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `Ephemeral5mInputTokens int64 Optional`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `CacheReadInputTokens int64 Optional`

      Total tokens read from prompt cache.

      format: int32

    - `InputTokens int64 Optional`

      Total input tokens consumed across all turns.

      format: int32

    - `ListCost BetaMonetaryAmount Optional`

      A monetary amount in a specific currency.

    - `OutputTokens int64 Optional`

      Total output tokens generated across all turns.

      format: int32

    - `ServerToolUse BetaManagedAgentsServerToolUsage Optional`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `WebFetchRequests int64 Optional`

        Number of server-executed web fetch requests.

        format: int32

      - `WebSearchRequests int64 Optional`

        Number of server-executed web search requests.

        format: int32

  - `VaultIDs []string`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `DeploymentID string Optional`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Example

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
	page, err := client.Beta.Sessions.List(context.TODO(), anthropic.BetaSessionListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
}
```

#### Response (200)

```json
{
  "data": [
    {
      "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
      "agent": {
        "id": "agent_011CZkYpogX7uDKUyvBTophP",
        "description": "A general-purpose starter agent.",
        "mcp_servers": [
          {
            "name": "example-mcp",
            "type": "url",
            "url": "https://example-server.modelcontextprotocol.io/sse"
          }
        ],
        "model": {
          "id": "claude-opus-5",
          "effort": {
            "type": "low"
          },
          "inference_geo": "inference_geo",
          "speed": "standard"
        },
        "multiagent": {
          "agents": [
            {
              "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
              "description": "A focused research subagent.",
              "mcp_servers": [
                {
                  "name": "example-mcp",
                  "type": "url",
                  "url": "https://example-server.modelcontextprotocol.io/sse"
                }
              ],
              "model": {
                "id": "claude-opus-5",
                "effort": {
                  "type": "low"
                },
                "inference_geo": "inference_geo",
                "speed": "standard"
              },
              "name": "Researcher",
              "skills": [
                {
                  "skill_id": "xlsx",
                  "type": "anthropic",
                  "version": "1"
                }
              ],
              "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
              "tools": [
                {
                  "configs": [
                    {
                      "enabled": true,
                      "name": "bash",
                      "permission_policy": {
                        "type": "always_allow"
                      },
                      "type": "bash"
                    }
                  ],
                  "default_config": {
                    "enabled": true,
                    "permission_policy": {
                      "type": "always_ask"
                    }
                  },
                  "type": "agent_toolset_20260401"
                }
              ],
              "type": "agent",
              "version": 1
            }
          ],
          "type": "coordinator"
        },
        "name": "My First Agent",
        "skills": [
          {
            "skill_id": "xlsx",
            "type": "anthropic",
            "version": "1"
          },
          {
            "skill_id": "skill_011CZkZFNu9hAbo3jZPRgTlx",
            "type": "custom",
            "version": "2"
          }
        ],
        "system": "You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.",
        "tools": [
          {
            "configs": [
              {
                "enabled": true,
                "name": "bash",
                "permission_policy": {
                  "type": "always_allow"
                },
                "type": "bash"
              }
            ],
            "default_config": {
              "enabled": true,
              "permission_policy": {
                "type": "always_ask"
              }
            },
            "type": "agent_toolset_20260401"
          }
        ],
        "type": "agent",
        "version": 1
      },
      "archived_at": null,
      "budget": {
        "max_list_cost": {
          "amount": "2500",
          "currency": "USD"
        },
        "type": "limit"
      },
      "created_at": "2026-03-15T10:00:00Z",
      "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
      "metadata": {},
      "outcome_evaluations": [
        {
          "completed_at": "2026-03-15T10:02:31Z",
          "description": "Produce a 2-page summary as summary.md",
          "explanation": "All five sections present with inline citations.",
          "iteration": 0,
          "outcome_id": "outc_011CZkZRSw2kEfs6ncTVljxP",
          "result": "satisfied",
          "type": "outcome_evaluation"
        }
      ],
      "resources": [
        {
          "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
          "created_at": "2026-03-15T10:00:00Z",
          "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
          "mount_path": "/uploads/receipt.pdf",
          "type": "file",
          "updated_at": "2026-03-15T10:00:00Z"
        },
        {
          "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
          "created_at": "2026-03-15T10:00:00Z",
          "mount_path": "/workspace/example-repo",
          "type": "github_repository",
          "updated_at": "2026-03-15T10:00:00Z",
          "url": "https://github.com/example-org/example-repo",
          "checkout": {
            "name": "main",
            "type": "branch"
          }
        }
      ],
      "stats": {
        "active_seconds": 0,
        "duration_seconds": 0
      },
      "status": "idle",
      "title": "Order #1234 inquiry",
      "type": "session",
      "updated_at": "2026-03-15T10:00:00Z",
      "usage": {
        "active_seconds": 0,
        "cache_creation": {
          "ephemeral_1h_input_tokens": 0,
          "ephemeral_5m_input_tokens": 0
        },
        "cache_read_input_tokens": 0,
        "input_tokens": 0,
        "list_cost": {
          "amount": "2500",
          "currency": "USD"
        },
        "output_tokens": 0,
        "server_tool_use": {
          "web_fetch_requests": 0,
          "web_search_requests": 3
        }
      },
      "vault_ids": [
        "vlt_011CZkZDLs7fYzm1hXNPeRjv"
      ],
      "deployment_id": "deployment_id"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo=",
  "prev_page": "page_MjAyNS0wNS0xM1QwMDowMDowMFo="
}
```

## Get Session

`client.Beta.Sessions.Get(ctx, sessionID, query) (*BetaManagedAgentsSession, error)`

**GET** `/v1/sessions/{session_id}`

Get Session

### Parameters

- `sessionID string`

- `query BetaSessionGetParams`

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Optional header to specify the beta version(s) you want to use.

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

### Returns

- `type BetaManagedAgentsSession struct{…}`

  A Managed Agents `session`.

  - `ID string`

  - `Agent BetaManagedAgentsSessionAgent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `ID string`

    - `Description string`

    - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

      - `Name string`

      - `Type BetaManagedAgentsMCPServerURLDefinitionType`

      - `URL string`

    - `Model BetaManagedAgentsModelConfig`

      Model identifier and configuration.

      - `ID BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `type BetaManagedAgentsModel string`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `const BetaManagedAgentsModelClaudeSonnet5 BetaManagedAgentsModel = "claude-sonnet-5"`

            High-performance model for coding and agents

          - `const BetaManagedAgentsModelClaudeFable5 BetaManagedAgentsModel = "claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `const BetaManagedAgentsModelClaudeOpus5 BetaManagedAgentsModel = "claude-opus-5"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeOpus4_8 BetaManagedAgentsModel = "claude-opus-4-8"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeOpus4_7 BetaManagedAgentsModel = "claude-opus-4-7"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeOpus4_6 BetaManagedAgentsModel = "claude-opus-4-6"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeSonnet4_6 BetaManagedAgentsModel = "claude-sonnet-4-6"`

            Best combination of speed and intelligence

          - `const BetaManagedAgentsModelClaudeHaiku4_5 BetaManagedAgentsModel = "claude-haiku-4-5"`

            Fastest model with near-frontier intelligence

          - `const BetaManagedAgentsModelClaudeHaiku4_5_20251001 BetaManagedAgentsModel = "claude-haiku-4-5-20251001"`

            Fastest model with near-frontier intelligence

          - `const BetaManagedAgentsModelClaudeOpus4_5 BetaManagedAgentsModel = "claude-opus-4-5"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeOpus4_5_20251101 BetaManagedAgentsModel = "claude-opus-4-5-20251101"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeSonnet4_5 BetaManagedAgentsModel = "claude-sonnet-4-5"`

            High-performance model for agents and coding

          - `const BetaManagedAgentsModelClaudeSonnet4_5_20250929 BetaManagedAgentsModel = "claude-sonnet-4-5-20250929"`

            High-performance model for agents and coding

        - `string`

      - `Effort BetaManagedAgentsModelConfigEffortUnion Optional`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

        - `type BetaManagedAgentsEffortLow struct{…}`

          Low effort. Favors latency over reasoning depth.

          - `Type BetaManagedAgentsEffortLowType`

        - `type BetaManagedAgentsEffortMedium struct{…}`

          Medium effort. Balances latency and reasoning depth.

          - `Type BetaManagedAgentsEffortMediumType`

        - `type BetaManagedAgentsEffortHigh struct{…}`

          High effort. Favors reasoning depth.

          - `Type BetaManagedAgentsEffortHighType`

        - `type BetaManagedAgentsEffortXhigh struct{…}`

          Extra-high effort. Not all models accept this level.

          - `Type BetaManagedAgentsEffortXhighType`

        - `type BetaManagedAgentsEffortMax struct{…}`

          Maximum effort. Favors reasoning depth over latency.

          - `Type BetaManagedAgentsEffortMaxType`

      - `InferenceGeo string Optional`

        Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

      - `Speed BetaManagedAgentsModelConfigSpeed Optional`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `const BetaManagedAgentsModelConfigSpeedStandard BetaManagedAgentsModelConfigSpeed = "standard"`

        - `const BetaManagedAgentsModelConfigSpeedFast BetaManagedAgentsModelConfigSpeed = "fast"`

    - `Multiagent BetaManagedAgentsSessionMultiagentCoordinator`

      Resolved coordinator topology with full agent definitions for each roster member.

      - `Agents []BetaManagedAgentsSessionMultiagentCoordinatorAgentUnion`

        Full `agent` definitions the coordinator may spawn as session threads.

        - `type BetaManagedAgentsSessionThreadAgent struct{…}`

          Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

          - `ID string`

          - `Description string`

          - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

            - `Name string`

            - `Type BetaManagedAgentsMCPServerURLDefinitionType`

            - `URL string`

          - `Model BetaManagedAgentsModelConfig`

            Model identifier and configuration.

          - `Name string`

          - `Skills []BetaManagedAgentsSessionThreadAgentSkillUnion`

            - `type BetaManagedAgentsAnthropicSkill struct{…}`

              A resolved Anthropic-managed skill.

              - `SkillID string`

              - `Type BetaManagedAgentsAnthropicSkillType`

              - `Version string`

            - `type BetaManagedAgentsCustomSkill struct{…}`

              A resolved user-created custom skill.

              - `SkillID string`

              - `Type BetaManagedAgentsCustomSkillType`

              - `Version string`

          - `System string`

          - `Tools []BetaManagedAgentsSessionThreadAgentToolUnion`

            - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

              - `Configs []BetaManagedAgentsAgentToolConfigUnion`

                - `type BetaManagedAgentsBashToolConfig struct{…}`

                  Configuration for the bash tool.

                  - `Enabled bool`

                  - `Name Bash`

                  - `PermissionPolicy BetaManagedAgentsBashToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                      - `Type BetaManagedAgentsAlwaysAllowPolicyType`

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                      - `Type BetaManagedAgentsAlwaysAskPolicyType`

                  - `Type Bash`

                - `type BetaManagedAgentsEditToolConfig struct{…}`

                  Configuration for the edit tool.

                  - `Enabled bool`

                  - `Name Edit`

                  - `PermissionPolicy BetaManagedAgentsEditToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type Edit`

                - `type BetaManagedAgentsReadToolConfig struct{…}`

                  Configuration for the read tool.

                  - `Enabled bool`

                  - `Name Read`

                  - `PermissionPolicy BetaManagedAgentsReadToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type Read`

                - `type BetaManagedAgentsWriteToolConfig struct{…}`

                  Configuration for the write tool.

                  - `Enabled bool`

                  - `Name Write`

                  - `PermissionPolicy BetaManagedAgentsWriteToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type Write`

                - `type BetaManagedAgentsGlobToolConfig struct{…}`

                  Configuration for the glob tool.

                  - `Enabled bool`

                  - `Name Glob`

                  - `PermissionPolicy BetaManagedAgentsGlobToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type Glob`

                - `type BetaManagedAgentsGrepToolConfig struct{…}`

                  Configuration for the grep tool.

                  - `Enabled bool`

                  - `Name Grep`

                  - `PermissionPolicy BetaManagedAgentsGrepToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type Grep`

                - `type BetaManagedAgentsWebFetchToolConfig struct{…}`

                  Configuration for the web_fetch tool.

                  - `Enabled bool`

                  - `Name WebFetch`

                  - `PermissionPolicy BetaManagedAgentsWebFetchToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type WebFetch`

                  - `AllowedDomains []string Optional`

                  - `BlockedDomains []string Optional`

                  - `MaxContentTokens int64 Optional`

                    format: int32

                - `type BetaManagedAgentsWebSearchToolConfig struct{…}`

                  Configuration for the web_search tool.

                  - `Enabled bool`

                  - `Name WebSearch`

                  - `PermissionPolicy BetaManagedAgentsWebSearchToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type WebSearch`

                  - `AllowedDomains []string Optional`

                  - `BlockedDomains []string Optional`

                  - `UserLocation BetaManagedAgentsUserLocation Optional`

                    Approximate user location for search result localization.

                    - `Type Approximate`

                      Location precision. Only "approximate" is supported.

                    - `City string Optional`

                      City name.

                      minLength: 1, maxLength: 255

                    - `Country string Optional`

                      Two-letter ISO 3166-1 country code, uppercase.

                    - `Region string Optional`

                      Region or state name.

                      minLength: 1, maxLength: 255

                    - `Timezone string Optional`

                      IANA timezone identifier, e.g. "America/Los_Angeles".

                      minLength: 1, maxLength: 255

              - `DefaultConfig BetaManagedAgentsAgentToolsetDefaultConfig`

                Resolved default configuration for agent tools.

                - `Enabled bool`

                - `PermissionPolicy BetaManagedAgentsAgentToolsetDefaultConfigPermissionPolicyUnion`

                  Permission policy for tool execution.

                  - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                    Tool calls are automatically approved without user confirmation.

                  - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                    Tool calls require user confirmation before execution.

              - `Type BetaManagedAgentsAgentToolset20260401Type`

            - `type BetaManagedAgentsMCPToolset struct{…}`

              - `Configs []BetaManagedAgentsMCPToolConfig`

                - `Enabled bool`

                - `Name string`

                - `PermissionPolicy BetaManagedAgentsMCPToolConfigPermissionPolicyUnion`

                  Permission policy for tool execution.

                  - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                    Tool calls are automatically approved without user confirmation.

                  - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                    Tool calls require user confirmation before execution.

              - `DefaultConfig BetaManagedAgentsMCPToolsetDefaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `Enabled bool`

                - `PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigPermissionPolicyUnion`

                  Permission policy for tool execution.

                  - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                    Tool calls are automatically approved without user confirmation.

                  - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                    Tool calls require user confirmation before execution.

              - `MCPServerName string`

              - `Type BetaManagedAgentsMCPToolsetType`

            - `type BetaManagedAgentsCustomTool struct{…}`

              A custom tool as returned in API responses.

              - `Description string`

              - `InputSchema BetaManagedAgentsCustomToolInputSchema`

                JSON Schema for custom tool input parameters.

                - `Type Object`

                - `Properties map[string, any] Optional`

                - `Required []string Optional`

              - `Name string`

              - `Type BetaManagedAgentsCustomToolType`

          - `Type BetaManagedAgentsSessionThreadAgentType`

          - `Version int64`

            format: int32

        - `type BetaManagedAgentsAdvisor struct{…}`

          Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

          - `Model string`

            The advisor model id.

          - `Type BetaManagedAgentsAdvisorType`

      - `Type BetaManagedAgentsSessionMultiagentCoordinatorType`

    - `Name string`

    - `Skills []BetaManagedAgentsSessionAgentSkillUnion`

      - `type BetaManagedAgentsAnthropicSkill struct{…}`

        A resolved Anthropic-managed skill.

      - `type BetaManagedAgentsCustomSkill struct{…}`

        A resolved user-created custom skill.

    - `System string`

    - `Tools []BetaManagedAgentsSessionAgentToolUnion`

      - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

      - `type BetaManagedAgentsMCPToolset struct{…}`

      - `type BetaManagedAgentsCustomTool struct{…}`

        A custom tool as returned in API responses.

    - `Type BetaManagedAgentsSessionAgentType`

    - `Version int64`

      format: int32

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `Budget BetaManagedAgentsBudgetLimit`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `MaxListCost BetaMonetaryAmount`

      A monetary amount in a specific currency.

      - `Amount string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `Currency BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `Type BetaManagedAgentsBudgetLimitType`

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `EnvironmentID string`

  - `Metadata map[string, string]`

  - `OutcomeEvaluations []BetaManagedAgentsOutcomeEvaluationResource`

    Per-outcome evaluation state. One entry per define_outcome event sent to the session.

    - `CompletedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Description string`

      What the agent should produce.

    - `Explanation string`

      Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs_revision (intermediate), what's missing; for failed, why unrecoverable.

    - `Iteration int64`

      0-indexed revision cycle the outcome is currently on.

      format: int32

    - `OutcomeID string`

      Server-generated outc_ ID for this outcome.

    - `Result string`

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

    - `Type BetaManagedAgentsOutcomeEvaluationResourceType`

  - `Resources []BetaManagedAgentsSessionResourceUnion`

    - `type BetaManagedAgentsGitHubRepositoryResource struct{…}`

      - `ID string`

      - `CreatedAt Time`

        A timestamp in RFC 3339 format

        format: date-time

      - `MountPath string`

      - `Type BetaManagedAgentsGitHubRepositoryResourceType`

      - `UpdatedAt Time`

        A timestamp in RFC 3339 format

        format: date-time

      - `URL string`

      - `Checkout BetaManagedAgentsGitHubRepositoryResourceCheckoutUnion Optional`

        - `type BetaManagedAgentsBranchCheckout struct{…}`

          - `Name string`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `Type BetaManagedAgentsBranchCheckoutType`

        - `type BetaManagedAgentsCommitCheckout struct{…}`

          - `Sha string`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `Type BetaManagedAgentsCommitCheckoutType`

    - `type BetaManagedAgentsFileResource struct{…}`

      - `ID string`

      - `CreatedAt Time`

        A timestamp in RFC 3339 format

        format: date-time

      - `FileID string`

      - `MountPath string`

      - `Type BetaManagedAgentsFileResourceType`

      - `UpdatedAt Time`

        A timestamp in RFC 3339 format

        format: date-time

    - `type BetaManagedAgentsMemoryStoreResource struct{…}`

      A memory store attached to an agent session.

      - `MemoryStoreID string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type BetaManagedAgentsMemoryStoreResourceType`

      - `Access BetaManagedAgentsMemoryStoreResourceAccess Optional`

        Access mode for an attached memory store.

        - `const BetaManagedAgentsMemoryStoreResourceAccessReadWrite BetaManagedAgentsMemoryStoreResourceAccess = "read_write"`

        - `const BetaManagedAgentsMemoryStoreResourceAccessReadOnly BetaManagedAgentsMemoryStoreResourceAccess = "read_only"`

      - `Description string Optional`

        Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

      - `Instructions string Optional`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

        maxLength: 4096

      - `MountPath string Optional`

        Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

      - `Name string Optional`

        Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

  - `Stats BetaManagedAgentsSessionStats`

    Timing statistics for a session.

    - `ActiveSeconds float64 Optional`

      Cumulative time in seconds the session spent in running status. Excludes idle time.

      format: double

    - `DurationSeconds float64 Optional`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

      format: double

  - `Status BetaManagedAgentsSessionStatus`

    SessionStatus enum

    - `const BetaManagedAgentsSessionStatusRescheduling BetaManagedAgentsSessionStatus = "rescheduling"`

    - `const BetaManagedAgentsSessionStatusRunning BetaManagedAgentsSessionStatus = "running"`

    - `const BetaManagedAgentsSessionStatusIdle BetaManagedAgentsSessionStatus = "idle"`

    - `const BetaManagedAgentsSessionStatusTerminated BetaManagedAgentsSessionStatus = "terminated"`

  - `Title string`

  - `Type BetaManagedAgentsSessionType`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `Usage BetaManagedAgentsSessionUsage`

    Cumulative token usage for a session across all turns.

    - `ActiveSeconds float64 Optional`

      Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once, unlike `stats.active_seconds`, which sums each thread's own active time. This is the duration the session's runtime cost is priced on.

      format: double

    - `CacheCreation BetaManagedAgentsCacheCreationUsage Optional`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `Ephemeral1hInputTokens int64 Optional`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `Ephemeral5mInputTokens int64 Optional`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `CacheReadInputTokens int64 Optional`

      Total tokens read from prompt cache.

      format: int32

    - `InputTokens int64 Optional`

      Total input tokens consumed across all turns.

      format: int32

    - `ListCost BetaMonetaryAmount Optional`

      A monetary amount in a specific currency.

    - `OutputTokens int64 Optional`

      Total output tokens generated across all turns.

      format: int32

    - `ServerToolUse BetaManagedAgentsServerToolUsage Optional`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `WebFetchRequests int64 Optional`

        Number of server-executed web fetch requests.

        format: int32

      - `WebSearchRequests int64 Optional`

        Number of server-executed web search requests.

        format: int32

  - `VaultIDs []string`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `DeploymentID string Optional`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Example

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
	betaManagedAgentsSession, err := client.Beta.Sessions.Get(
		context.TODO(),
		"sesn_011CZkZAtmR3yMPDzynEDxu7",
		anthropic.BetaSessionGetParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaManagedAgentsSession.ID)
}
```

#### Response (200)

```json
{
  "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "description": "A general-purpose starter agent.",
    "mcp_servers": [
      {
        "name": "example-mcp",
        "type": "url",
        "url": "https://example-server.modelcontextprotocol.io/sse"
      }
    ],
    "model": {
      "id": "claude-opus-5",
      "effort": {
        "type": "low"
      },
      "inference_geo": "inference_geo",
      "speed": "standard"
    },
    "multiagent": {
      "agents": [
        {
          "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
          "description": "A focused research subagent.",
          "mcp_servers": [
            {
              "name": "example-mcp",
              "type": "url",
              "url": "https://example-server.modelcontextprotocol.io/sse"
            }
          ],
          "model": {
            "id": "claude-opus-5",
            "effort": {
              "type": "low"
            },
            "inference_geo": "inference_geo",
            "speed": "standard"
          },
          "name": "Researcher",
          "skills": [
            {
              "skill_id": "xlsx",
              "type": "anthropic",
              "version": "1"
            }
          ],
          "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
          "tools": [
            {
              "configs": [
                {
                  "enabled": true,
                  "name": "bash",
                  "permission_policy": {
                    "type": "always_allow"
                  },
                  "type": "bash"
                }
              ],
              "default_config": {
                "enabled": true,
                "permission_policy": {
                  "type": "always_ask"
                }
              },
              "type": "agent_toolset_20260401"
            }
          ],
          "type": "agent",
          "version": 1
        }
      ],
      "type": "coordinator"
    },
    "name": "My First Agent",
    "skills": [
      {
        "skill_id": "xlsx",
        "type": "anthropic",
        "version": "1"
      },
      {
        "skill_id": "skill_011CZkZFNu9hAbo3jZPRgTlx",
        "type": "custom",
        "version": "2"
      }
    ],
    "system": "You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.",
    "tools": [
      {
        "configs": [
          {
            "enabled": true,
            "name": "bash",
            "permission_policy": {
              "type": "always_allow"
            },
            "type": "bash"
          }
        ],
        "default_config": {
          "enabled": true,
          "permission_policy": {
            "type": "always_ask"
          }
        },
        "type": "agent_toolset_20260401"
      }
    ],
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "budget": {
    "max_list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "type": "limit"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "metadata": {},
  "outcome_evaluations": [
    {
      "completed_at": "2026-03-15T10:02:31Z",
      "description": "Produce a 2-page summary as summary.md",
      "explanation": "All five sections present with inline citations.",
      "iteration": 0,
      "outcome_id": "outc_011CZkZRSw2kEfs6ncTVljxP",
      "result": "satisfied",
      "type": "outcome_evaluation"
    }
  ],
  "resources": [
    {
      "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
      "created_at": "2026-03-15T10:00:00Z",
      "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
      "mount_path": "/uploads/receipt.pdf",
      "type": "file",
      "updated_at": "2026-03-15T10:00:00Z"
    },
    {
      "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
      "created_at": "2026-03-15T10:00:00Z",
      "mount_path": "/workspace/example-repo",
      "type": "github_repository",
      "updated_at": "2026-03-15T10:00:00Z",
      "url": "https://github.com/example-org/example-repo",
      "checkout": {
        "name": "main",
        "type": "branch"
      }
    }
  ],
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0
  },
  "status": "idle",
  "title": "Order #1234 inquiry",
  "type": "session",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "active_seconds": 0,
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "output_tokens": 0,
    "server_tool_use": {
      "web_fetch_requests": 0,
      "web_search_requests": 3
    }
  },
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "deployment_id": "deployment_id"
}
```

## Update Session

`client.Beta.Sessions.Update(ctx, sessionID, params) (*BetaManagedAgentsSession, error)`

**POST** `/v1/sessions/{session_id}`

Update Session

### Parameters

- `sessionID string`

- `params BetaSessionUpdateParams`

  - `Agent param.Field[BetaManagedAgentsSessionAgentUpdate] Optional`

    Body param: Mid-session agent configuration update. Only `tools` and `mcp_servers` are updatable. Full replacement: the provided array becomes the new value. To preserve existing entries, GET the session, modify the array, and POST it back.

  - `Budget param.Field[BetaManagedAgentsBudgetLimit] Optional`

    Body param: A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

  - `Metadata param.Field[map[string, string]] Optional`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve.

  - `Title param.Field[string] Optional`

    Body param: Human-readable session title.

    minLength: 1, maxLength: 500

  - `VaultIDs param.Field[[]string] Optional`

    Body param: Vault IDs (`vlt_*`) to attach to the session. Not yet supported; requests setting this field are rejected. Reserved for future use.

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

### Returns

- `type BetaManagedAgentsSession struct{…}`

  A Managed Agents `session`.

  - `ID string`

  - `Agent BetaManagedAgentsSessionAgent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `ID string`

    - `Description string`

    - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

      - `Name string`

      - `Type BetaManagedAgentsMCPServerURLDefinitionType`

      - `URL string`

    - `Model BetaManagedAgentsModelConfig`

      Model identifier and configuration.

      - `ID BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `type BetaManagedAgentsModel string`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `const BetaManagedAgentsModelClaudeSonnet5 BetaManagedAgentsModel = "claude-sonnet-5"`

            High-performance model for coding and agents

          - `const BetaManagedAgentsModelClaudeFable5 BetaManagedAgentsModel = "claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `const BetaManagedAgentsModelClaudeOpus5 BetaManagedAgentsModel = "claude-opus-5"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeOpus4_8 BetaManagedAgentsModel = "claude-opus-4-8"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeOpus4_7 BetaManagedAgentsModel = "claude-opus-4-7"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeOpus4_6 BetaManagedAgentsModel = "claude-opus-4-6"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeSonnet4_6 BetaManagedAgentsModel = "claude-sonnet-4-6"`

            Best combination of speed and intelligence

          - `const BetaManagedAgentsModelClaudeHaiku4_5 BetaManagedAgentsModel = "claude-haiku-4-5"`

            Fastest model with near-frontier intelligence

          - `const BetaManagedAgentsModelClaudeHaiku4_5_20251001 BetaManagedAgentsModel = "claude-haiku-4-5-20251001"`

            Fastest model with near-frontier intelligence

          - `const BetaManagedAgentsModelClaudeOpus4_5 BetaManagedAgentsModel = "claude-opus-4-5"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeOpus4_5_20251101 BetaManagedAgentsModel = "claude-opus-4-5-20251101"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeSonnet4_5 BetaManagedAgentsModel = "claude-sonnet-4-5"`

            High-performance model for agents and coding

          - `const BetaManagedAgentsModelClaudeSonnet4_5_20250929 BetaManagedAgentsModel = "claude-sonnet-4-5-20250929"`

            High-performance model for agents and coding

        - `string`

      - `Effort BetaManagedAgentsModelConfigEffortUnion Optional`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

        - `type BetaManagedAgentsEffortLow struct{…}`

          Low effort. Favors latency over reasoning depth.

          - `Type BetaManagedAgentsEffortLowType`

        - `type BetaManagedAgentsEffortMedium struct{…}`

          Medium effort. Balances latency and reasoning depth.

          - `Type BetaManagedAgentsEffortMediumType`

        - `type BetaManagedAgentsEffortHigh struct{…}`

          High effort. Favors reasoning depth.

          - `Type BetaManagedAgentsEffortHighType`

        - `type BetaManagedAgentsEffortXhigh struct{…}`

          Extra-high effort. Not all models accept this level.

          - `Type BetaManagedAgentsEffortXhighType`

        - `type BetaManagedAgentsEffortMax struct{…}`

          Maximum effort. Favors reasoning depth over latency.

          - `Type BetaManagedAgentsEffortMaxType`

      - `InferenceGeo string Optional`

        Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

      - `Speed BetaManagedAgentsModelConfigSpeed Optional`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `const BetaManagedAgentsModelConfigSpeedStandard BetaManagedAgentsModelConfigSpeed = "standard"`

        - `const BetaManagedAgentsModelConfigSpeedFast BetaManagedAgentsModelConfigSpeed = "fast"`

    - `Multiagent BetaManagedAgentsSessionMultiagentCoordinator`

      Resolved coordinator topology with full agent definitions for each roster member.

      - `Agents []BetaManagedAgentsSessionMultiagentCoordinatorAgentUnion`

        Full `agent` definitions the coordinator may spawn as session threads.

        - `type BetaManagedAgentsSessionThreadAgent struct{…}`

          Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

          - `ID string`

          - `Description string`

          - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

            - `Name string`

            - `Type BetaManagedAgentsMCPServerURLDefinitionType`

            - `URL string`

          - `Model BetaManagedAgentsModelConfig`

            Model identifier and configuration.

          - `Name string`

          - `Skills []BetaManagedAgentsSessionThreadAgentSkillUnion`

            - `type BetaManagedAgentsAnthropicSkill struct{…}`

              A resolved Anthropic-managed skill.

              - `SkillID string`

              - `Type BetaManagedAgentsAnthropicSkillType`

              - `Version string`

            - `type BetaManagedAgentsCustomSkill struct{…}`

              A resolved user-created custom skill.

              - `SkillID string`

              - `Type BetaManagedAgentsCustomSkillType`

              - `Version string`

          - `System string`

          - `Tools []BetaManagedAgentsSessionThreadAgentToolUnion`

            - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

              - `Configs []BetaManagedAgentsAgentToolConfigUnion`

                - `type BetaManagedAgentsBashToolConfig struct{…}`

                  Configuration for the bash tool.

                  - `Enabled bool`

                  - `Name Bash`

                  - `PermissionPolicy BetaManagedAgentsBashToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                      - `Type BetaManagedAgentsAlwaysAllowPolicyType`

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                      - `Type BetaManagedAgentsAlwaysAskPolicyType`

                  - `Type Bash`

                - `type BetaManagedAgentsEditToolConfig struct{…}`

                  Configuration for the edit tool.

                  - `Enabled bool`

                  - `Name Edit`

                  - `PermissionPolicy BetaManagedAgentsEditToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type Edit`

                - `type BetaManagedAgentsReadToolConfig struct{…}`

                  Configuration for the read tool.

                  - `Enabled bool`

                  - `Name Read`

                  - `PermissionPolicy BetaManagedAgentsReadToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type Read`

                - `type BetaManagedAgentsWriteToolConfig struct{…}`

                  Configuration for the write tool.

                  - `Enabled bool`

                  - `Name Write`

                  - `PermissionPolicy BetaManagedAgentsWriteToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type Write`

                - `type BetaManagedAgentsGlobToolConfig struct{…}`

                  Configuration for the glob tool.

                  - `Enabled bool`

                  - `Name Glob`

                  - `PermissionPolicy BetaManagedAgentsGlobToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type Glob`

                - `type BetaManagedAgentsGrepToolConfig struct{…}`

                  Configuration for the grep tool.

                  - `Enabled bool`

                  - `Name Grep`

                  - `PermissionPolicy BetaManagedAgentsGrepToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type Grep`

                - `type BetaManagedAgentsWebFetchToolConfig struct{…}`

                  Configuration for the web_fetch tool.

                  - `Enabled bool`

                  - `Name WebFetch`

                  - `PermissionPolicy BetaManagedAgentsWebFetchToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type WebFetch`

                  - `AllowedDomains []string Optional`

                  - `BlockedDomains []string Optional`

                  - `MaxContentTokens int64 Optional`

                    format: int32

                - `type BetaManagedAgentsWebSearchToolConfig struct{…}`

                  Configuration for the web_search tool.

                  - `Enabled bool`

                  - `Name WebSearch`

                  - `PermissionPolicy BetaManagedAgentsWebSearchToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type WebSearch`

                  - `AllowedDomains []string Optional`

                  - `BlockedDomains []string Optional`

                  - `UserLocation BetaManagedAgentsUserLocation Optional`

                    Approximate user location for search result localization.

                    - `Type Approximate`

                      Location precision. Only "approximate" is supported.

                    - `City string Optional`

                      City name.

                      minLength: 1, maxLength: 255

                    - `Country string Optional`

                      Two-letter ISO 3166-1 country code, uppercase.

                    - `Region string Optional`

                      Region or state name.

                      minLength: 1, maxLength: 255

                    - `Timezone string Optional`

                      IANA timezone identifier, e.g. "America/Los_Angeles".

                      minLength: 1, maxLength: 255

              - `DefaultConfig BetaManagedAgentsAgentToolsetDefaultConfig`

                Resolved default configuration for agent tools.

                - `Enabled bool`

                - `PermissionPolicy BetaManagedAgentsAgentToolsetDefaultConfigPermissionPolicyUnion`

                  Permission policy for tool execution.

                  - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                    Tool calls are automatically approved without user confirmation.

                  - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                    Tool calls require user confirmation before execution.

              - `Type BetaManagedAgentsAgentToolset20260401Type`

            - `type BetaManagedAgentsMCPToolset struct{…}`

              - `Configs []BetaManagedAgentsMCPToolConfig`

                - `Enabled bool`

                - `Name string`

                - `PermissionPolicy BetaManagedAgentsMCPToolConfigPermissionPolicyUnion`

                  Permission policy for tool execution.

                  - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                    Tool calls are automatically approved without user confirmation.

                  - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                    Tool calls require user confirmation before execution.

              - `DefaultConfig BetaManagedAgentsMCPToolsetDefaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `Enabled bool`

                - `PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigPermissionPolicyUnion`

                  Permission policy for tool execution.

                  - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                    Tool calls are automatically approved without user confirmation.

                  - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                    Tool calls require user confirmation before execution.

              - `MCPServerName string`

              - `Type BetaManagedAgentsMCPToolsetType`

            - `type BetaManagedAgentsCustomTool struct{…}`

              A custom tool as returned in API responses.

              - `Description string`

              - `InputSchema BetaManagedAgentsCustomToolInputSchema`

                JSON Schema for custom tool input parameters.

                - `Type Object`

                - `Properties map[string, any] Optional`

                - `Required []string Optional`

              - `Name string`

              - `Type BetaManagedAgentsCustomToolType`

          - `Type BetaManagedAgentsSessionThreadAgentType`

          - `Version int64`

            format: int32

        - `type BetaManagedAgentsAdvisor struct{…}`

          Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

          - `Model string`

            The advisor model id.

          - `Type BetaManagedAgentsAdvisorType`

      - `Type BetaManagedAgentsSessionMultiagentCoordinatorType`

    - `Name string`

    - `Skills []BetaManagedAgentsSessionAgentSkillUnion`

      - `type BetaManagedAgentsAnthropicSkill struct{…}`

        A resolved Anthropic-managed skill.

      - `type BetaManagedAgentsCustomSkill struct{…}`

        A resolved user-created custom skill.

    - `System string`

    - `Tools []BetaManagedAgentsSessionAgentToolUnion`

      - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

      - `type BetaManagedAgentsMCPToolset struct{…}`

      - `type BetaManagedAgentsCustomTool struct{…}`

        A custom tool as returned in API responses.

    - `Type BetaManagedAgentsSessionAgentType`

    - `Version int64`

      format: int32

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `Budget BetaManagedAgentsBudgetLimit`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `MaxListCost BetaMonetaryAmount`

      A monetary amount in a specific currency.

      - `Amount string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `Currency BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `Type BetaManagedAgentsBudgetLimitType`

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `EnvironmentID string`

  - `Metadata map[string, string]`

  - `OutcomeEvaluations []BetaManagedAgentsOutcomeEvaluationResource`

    Per-outcome evaluation state. One entry per define_outcome event sent to the session.

    - `CompletedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Description string`

      What the agent should produce.

    - `Explanation string`

      Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs_revision (intermediate), what's missing; for failed, why unrecoverable.

    - `Iteration int64`

      0-indexed revision cycle the outcome is currently on.

      format: int32

    - `OutcomeID string`

      Server-generated outc_ ID for this outcome.

    - `Result string`

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

    - `Type BetaManagedAgentsOutcomeEvaluationResourceType`

  - `Resources []BetaManagedAgentsSessionResourceUnion`

    - `type BetaManagedAgentsGitHubRepositoryResource struct{…}`

      - `ID string`

      - `CreatedAt Time`

        A timestamp in RFC 3339 format

        format: date-time

      - `MountPath string`

      - `Type BetaManagedAgentsGitHubRepositoryResourceType`

      - `UpdatedAt Time`

        A timestamp in RFC 3339 format

        format: date-time

      - `URL string`

      - `Checkout BetaManagedAgentsGitHubRepositoryResourceCheckoutUnion Optional`

        - `type BetaManagedAgentsBranchCheckout struct{…}`

          - `Name string`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `Type BetaManagedAgentsBranchCheckoutType`

        - `type BetaManagedAgentsCommitCheckout struct{…}`

          - `Sha string`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `Type BetaManagedAgentsCommitCheckoutType`

    - `type BetaManagedAgentsFileResource struct{…}`

      - `ID string`

      - `CreatedAt Time`

        A timestamp in RFC 3339 format

        format: date-time

      - `FileID string`

      - `MountPath string`

      - `Type BetaManagedAgentsFileResourceType`

      - `UpdatedAt Time`

        A timestamp in RFC 3339 format

        format: date-time

    - `type BetaManagedAgentsMemoryStoreResource struct{…}`

      A memory store attached to an agent session.

      - `MemoryStoreID string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type BetaManagedAgentsMemoryStoreResourceType`

      - `Access BetaManagedAgentsMemoryStoreResourceAccess Optional`

        Access mode for an attached memory store.

        - `const BetaManagedAgentsMemoryStoreResourceAccessReadWrite BetaManagedAgentsMemoryStoreResourceAccess = "read_write"`

        - `const BetaManagedAgentsMemoryStoreResourceAccessReadOnly BetaManagedAgentsMemoryStoreResourceAccess = "read_only"`

      - `Description string Optional`

        Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

      - `Instructions string Optional`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

        maxLength: 4096

      - `MountPath string Optional`

        Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

      - `Name string Optional`

        Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

  - `Stats BetaManagedAgentsSessionStats`

    Timing statistics for a session.

    - `ActiveSeconds float64 Optional`

      Cumulative time in seconds the session spent in running status. Excludes idle time.

      format: double

    - `DurationSeconds float64 Optional`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

      format: double

  - `Status BetaManagedAgentsSessionStatus`

    SessionStatus enum

    - `const BetaManagedAgentsSessionStatusRescheduling BetaManagedAgentsSessionStatus = "rescheduling"`

    - `const BetaManagedAgentsSessionStatusRunning BetaManagedAgentsSessionStatus = "running"`

    - `const BetaManagedAgentsSessionStatusIdle BetaManagedAgentsSessionStatus = "idle"`

    - `const BetaManagedAgentsSessionStatusTerminated BetaManagedAgentsSessionStatus = "terminated"`

  - `Title string`

  - `Type BetaManagedAgentsSessionType`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `Usage BetaManagedAgentsSessionUsage`

    Cumulative token usage for a session across all turns.

    - `ActiveSeconds float64 Optional`

      Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once, unlike `stats.active_seconds`, which sums each thread's own active time. This is the duration the session's runtime cost is priced on.

      format: double

    - `CacheCreation BetaManagedAgentsCacheCreationUsage Optional`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `Ephemeral1hInputTokens int64 Optional`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `Ephemeral5mInputTokens int64 Optional`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `CacheReadInputTokens int64 Optional`

      Total tokens read from prompt cache.

      format: int32

    - `InputTokens int64 Optional`

      Total input tokens consumed across all turns.

      format: int32

    - `ListCost BetaMonetaryAmount Optional`

      A monetary amount in a specific currency.

    - `OutputTokens int64 Optional`

      Total output tokens generated across all turns.

      format: int32

    - `ServerToolUse BetaManagedAgentsServerToolUsage Optional`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `WebFetchRequests int64 Optional`

        Number of server-executed web fetch requests.

        format: int32

      - `WebSearchRequests int64 Optional`

        Number of server-executed web search requests.

        format: int32

  - `VaultIDs []string`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `DeploymentID string Optional`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Example

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
	betaManagedAgentsSession, err := client.Beta.Sessions.Update(
		context.TODO(),
		"sesn_011CZkZAtmR3yMPDzynEDxu7",
		anthropic.BetaSessionUpdateParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaManagedAgentsSession.ID)
}
```

#### Response (200)

```json
{
  "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "description": "A general-purpose starter agent.",
    "mcp_servers": [
      {
        "name": "example-mcp",
        "type": "url",
        "url": "https://example-server.modelcontextprotocol.io/sse"
      }
    ],
    "model": {
      "id": "claude-opus-5",
      "effort": {
        "type": "low"
      },
      "inference_geo": "inference_geo",
      "speed": "standard"
    },
    "multiagent": {
      "agents": [
        {
          "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
          "description": "A focused research subagent.",
          "mcp_servers": [
            {
              "name": "example-mcp",
              "type": "url",
              "url": "https://example-server.modelcontextprotocol.io/sse"
            }
          ],
          "model": {
            "id": "claude-opus-5",
            "effort": {
              "type": "low"
            },
            "inference_geo": "inference_geo",
            "speed": "standard"
          },
          "name": "Researcher",
          "skills": [
            {
              "skill_id": "xlsx",
              "type": "anthropic",
              "version": "1"
            }
          ],
          "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
          "tools": [
            {
              "configs": [
                {
                  "enabled": true,
                  "name": "bash",
                  "permission_policy": {
                    "type": "always_allow"
                  },
                  "type": "bash"
                }
              ],
              "default_config": {
                "enabled": true,
                "permission_policy": {
                  "type": "always_ask"
                }
              },
              "type": "agent_toolset_20260401"
            }
          ],
          "type": "agent",
          "version": 1
        }
      ],
      "type": "coordinator"
    },
    "name": "My First Agent",
    "skills": [
      {
        "skill_id": "xlsx",
        "type": "anthropic",
        "version": "1"
      },
      {
        "skill_id": "skill_011CZkZFNu9hAbo3jZPRgTlx",
        "type": "custom",
        "version": "2"
      }
    ],
    "system": "You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.",
    "tools": [
      {
        "configs": [
          {
            "enabled": true,
            "name": "bash",
            "permission_policy": {
              "type": "always_allow"
            },
            "type": "bash"
          }
        ],
        "default_config": {
          "enabled": true,
          "permission_policy": {
            "type": "always_ask"
          }
        },
        "type": "agent_toolset_20260401"
      }
    ],
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "budget": {
    "max_list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "type": "limit"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "metadata": {},
  "outcome_evaluations": [
    {
      "completed_at": "2026-03-15T10:02:31Z",
      "description": "Produce a 2-page summary as summary.md",
      "explanation": "All five sections present with inline citations.",
      "iteration": 0,
      "outcome_id": "outc_011CZkZRSw2kEfs6ncTVljxP",
      "result": "satisfied",
      "type": "outcome_evaluation"
    }
  ],
  "resources": [
    {
      "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
      "created_at": "2026-03-15T10:00:00Z",
      "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
      "mount_path": "/uploads/receipt.pdf",
      "type": "file",
      "updated_at": "2026-03-15T10:00:00Z"
    },
    {
      "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
      "created_at": "2026-03-15T10:00:00Z",
      "mount_path": "/workspace/example-repo",
      "type": "github_repository",
      "updated_at": "2026-03-15T10:00:00Z",
      "url": "https://github.com/example-org/example-repo",
      "checkout": {
        "name": "main",
        "type": "branch"
      }
    }
  ],
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0
  },
  "status": "idle",
  "title": "Order #1234 inquiry",
  "type": "session",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "active_seconds": 0,
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "output_tokens": 0,
    "server_tool_use": {
      "web_fetch_requests": 0,
      "web_search_requests": 3
    }
  },
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "deployment_id": "deployment_id"
}
```

## Delete Session

`client.Beta.Sessions.Delete(ctx, sessionID, body) (*BetaManagedAgentsDeletedSession, error)`

**DELETE** `/v1/sessions/{session_id}`

Delete Session

### Parameters

- `sessionID string`

- `body BetaSessionDeleteParams`

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Optional header to specify the beta version(s) you want to use.

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

### Returns

- `type BetaManagedAgentsDeletedSession struct{…}`

  Confirmation that a `session` has been permanently deleted.

  - `ID string`

  - `Type BetaManagedAgentsDeletedSessionType`

### Example

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
	betaManagedAgentsDeletedSession, err := client.Beta.Sessions.Delete(
		context.TODO(),
		"sesn_011CZkZAtmR3yMPDzynEDxu7",
		anthropic.BetaSessionDeleteParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaManagedAgentsDeletedSession.ID)
}
```

#### Response (200)

```json
{
  "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "type": "session_deleted"
}
```

## Archive Session

`client.Beta.Sessions.Archive(ctx, sessionID, body) (*BetaManagedAgentsSession, error)`

**POST** `/v1/sessions/{session_id}/archive`

Archive Session

### Parameters

- `sessionID string`

- `body BetaSessionArchiveParams`

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Optional header to specify the beta version(s) you want to use.

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

### Returns

- `type BetaManagedAgentsSession struct{…}`

  A Managed Agents `session`.

  - `ID string`

  - `Agent BetaManagedAgentsSessionAgent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `ID string`

    - `Description string`

    - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

      - `Name string`

      - `Type BetaManagedAgentsMCPServerURLDefinitionType`

      - `URL string`

    - `Model BetaManagedAgentsModelConfig`

      Model identifier and configuration.

      - `ID BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `type BetaManagedAgentsModel string`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `const BetaManagedAgentsModelClaudeSonnet5 BetaManagedAgentsModel = "claude-sonnet-5"`

            High-performance model for coding and agents

          - `const BetaManagedAgentsModelClaudeFable5 BetaManagedAgentsModel = "claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `const BetaManagedAgentsModelClaudeOpus5 BetaManagedAgentsModel = "claude-opus-5"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeOpus4_8 BetaManagedAgentsModel = "claude-opus-4-8"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeOpus4_7 BetaManagedAgentsModel = "claude-opus-4-7"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeOpus4_6 BetaManagedAgentsModel = "claude-opus-4-6"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeSonnet4_6 BetaManagedAgentsModel = "claude-sonnet-4-6"`

            Best combination of speed and intelligence

          - `const BetaManagedAgentsModelClaudeHaiku4_5 BetaManagedAgentsModel = "claude-haiku-4-5"`

            Fastest model with near-frontier intelligence

          - `const BetaManagedAgentsModelClaudeHaiku4_5_20251001 BetaManagedAgentsModel = "claude-haiku-4-5-20251001"`

            Fastest model with near-frontier intelligence

          - `const BetaManagedAgentsModelClaudeOpus4_5 BetaManagedAgentsModel = "claude-opus-4-5"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeOpus4_5_20251101 BetaManagedAgentsModel = "claude-opus-4-5-20251101"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeSonnet4_5 BetaManagedAgentsModel = "claude-sonnet-4-5"`

            High-performance model for agents and coding

          - `const BetaManagedAgentsModelClaudeSonnet4_5_20250929 BetaManagedAgentsModel = "claude-sonnet-4-5-20250929"`

            High-performance model for agents and coding

        - `string`

      - `Effort BetaManagedAgentsModelConfigEffortUnion Optional`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

        - `type BetaManagedAgentsEffortLow struct{…}`

          Low effort. Favors latency over reasoning depth.

          - `Type BetaManagedAgentsEffortLowType`

        - `type BetaManagedAgentsEffortMedium struct{…}`

          Medium effort. Balances latency and reasoning depth.

          - `Type BetaManagedAgentsEffortMediumType`

        - `type BetaManagedAgentsEffortHigh struct{…}`

          High effort. Favors reasoning depth.

          - `Type BetaManagedAgentsEffortHighType`

        - `type BetaManagedAgentsEffortXhigh struct{…}`

          Extra-high effort. Not all models accept this level.

          - `Type BetaManagedAgentsEffortXhighType`

        - `type BetaManagedAgentsEffortMax struct{…}`

          Maximum effort. Favors reasoning depth over latency.

          - `Type BetaManagedAgentsEffortMaxType`

      - `InferenceGeo string Optional`

        Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

      - `Speed BetaManagedAgentsModelConfigSpeed Optional`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `const BetaManagedAgentsModelConfigSpeedStandard BetaManagedAgentsModelConfigSpeed = "standard"`

        - `const BetaManagedAgentsModelConfigSpeedFast BetaManagedAgentsModelConfigSpeed = "fast"`

    - `Multiagent BetaManagedAgentsSessionMultiagentCoordinator`

      Resolved coordinator topology with full agent definitions for each roster member.

      - `Agents []BetaManagedAgentsSessionMultiagentCoordinatorAgentUnion`

        Full `agent` definitions the coordinator may spawn as session threads.

        - `type BetaManagedAgentsSessionThreadAgent struct{…}`

          Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

          - `ID string`

          - `Description string`

          - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

            - `Name string`

            - `Type BetaManagedAgentsMCPServerURLDefinitionType`

            - `URL string`

          - `Model BetaManagedAgentsModelConfig`

            Model identifier and configuration.

          - `Name string`

          - `Skills []BetaManagedAgentsSessionThreadAgentSkillUnion`

            - `type BetaManagedAgentsAnthropicSkill struct{…}`

              A resolved Anthropic-managed skill.

              - `SkillID string`

              - `Type BetaManagedAgentsAnthropicSkillType`

              - `Version string`

            - `type BetaManagedAgentsCustomSkill struct{…}`

              A resolved user-created custom skill.

              - `SkillID string`

              - `Type BetaManagedAgentsCustomSkillType`

              - `Version string`

          - `System string`

          - `Tools []BetaManagedAgentsSessionThreadAgentToolUnion`

            - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

              - `Configs []BetaManagedAgentsAgentToolConfigUnion`

                - `type BetaManagedAgentsBashToolConfig struct{…}`

                  Configuration for the bash tool.

                  - `Enabled bool`

                  - `Name Bash`

                  - `PermissionPolicy BetaManagedAgentsBashToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                      - `Type BetaManagedAgentsAlwaysAllowPolicyType`

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                      - `Type BetaManagedAgentsAlwaysAskPolicyType`

                  - `Type Bash`

                - `type BetaManagedAgentsEditToolConfig struct{…}`

                  Configuration for the edit tool.

                  - `Enabled bool`

                  - `Name Edit`

                  - `PermissionPolicy BetaManagedAgentsEditToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type Edit`

                - `type BetaManagedAgentsReadToolConfig struct{…}`

                  Configuration for the read tool.

                  - `Enabled bool`

                  - `Name Read`

                  - `PermissionPolicy BetaManagedAgentsReadToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type Read`

                - `type BetaManagedAgentsWriteToolConfig struct{…}`

                  Configuration for the write tool.

                  - `Enabled bool`

                  - `Name Write`

                  - `PermissionPolicy BetaManagedAgentsWriteToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type Write`

                - `type BetaManagedAgentsGlobToolConfig struct{…}`

                  Configuration for the glob tool.

                  - `Enabled bool`

                  - `Name Glob`

                  - `PermissionPolicy BetaManagedAgentsGlobToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type Glob`

                - `type BetaManagedAgentsGrepToolConfig struct{…}`

                  Configuration for the grep tool.

                  - `Enabled bool`

                  - `Name Grep`

                  - `PermissionPolicy BetaManagedAgentsGrepToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type Grep`

                - `type BetaManagedAgentsWebFetchToolConfig struct{…}`

                  Configuration for the web_fetch tool.

                  - `Enabled bool`

                  - `Name WebFetch`

                  - `PermissionPolicy BetaManagedAgentsWebFetchToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type WebFetch`

                  - `AllowedDomains []string Optional`

                  - `BlockedDomains []string Optional`

                  - `MaxContentTokens int64 Optional`

                    format: int32

                - `type BetaManagedAgentsWebSearchToolConfig struct{…}`

                  Configuration for the web_search tool.

                  - `Enabled bool`

                  - `Name WebSearch`

                  - `PermissionPolicy BetaManagedAgentsWebSearchToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type WebSearch`

                  - `AllowedDomains []string Optional`

                  - `BlockedDomains []string Optional`

                  - `UserLocation BetaManagedAgentsUserLocation Optional`

                    Approximate user location for search result localization.

                    - `Type Approximate`

                      Location precision. Only "approximate" is supported.

                    - `City string Optional`

                      City name.

                      minLength: 1, maxLength: 255

                    - `Country string Optional`

                      Two-letter ISO 3166-1 country code, uppercase.

                    - `Region string Optional`

                      Region or state name.

                      minLength: 1, maxLength: 255

                    - `Timezone string Optional`

                      IANA timezone identifier, e.g. "America/Los_Angeles".

                      minLength: 1, maxLength: 255

              - `DefaultConfig BetaManagedAgentsAgentToolsetDefaultConfig`

                Resolved default configuration for agent tools.

                - `Enabled bool`

                - `PermissionPolicy BetaManagedAgentsAgentToolsetDefaultConfigPermissionPolicyUnion`

                  Permission policy for tool execution.

                  - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                    Tool calls are automatically approved without user confirmation.

                  - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                    Tool calls require user confirmation before execution.

              - `Type BetaManagedAgentsAgentToolset20260401Type`

            - `type BetaManagedAgentsMCPToolset struct{…}`

              - `Configs []BetaManagedAgentsMCPToolConfig`

                - `Enabled bool`

                - `Name string`

                - `PermissionPolicy BetaManagedAgentsMCPToolConfigPermissionPolicyUnion`

                  Permission policy for tool execution.

                  - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                    Tool calls are automatically approved without user confirmation.

                  - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                    Tool calls require user confirmation before execution.

              - `DefaultConfig BetaManagedAgentsMCPToolsetDefaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `Enabled bool`

                - `PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigPermissionPolicyUnion`

                  Permission policy for tool execution.

                  - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                    Tool calls are automatically approved without user confirmation.

                  - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                    Tool calls require user confirmation before execution.

              - `MCPServerName string`

              - `Type BetaManagedAgentsMCPToolsetType`

            - `type BetaManagedAgentsCustomTool struct{…}`

              A custom tool as returned in API responses.

              - `Description string`

              - `InputSchema BetaManagedAgentsCustomToolInputSchema`

                JSON Schema for custom tool input parameters.

                - `Type Object`

                - `Properties map[string, any] Optional`

                - `Required []string Optional`

              - `Name string`

              - `Type BetaManagedAgentsCustomToolType`

          - `Type BetaManagedAgentsSessionThreadAgentType`

          - `Version int64`

            format: int32

        - `type BetaManagedAgentsAdvisor struct{…}`

          Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

          - `Model string`

            The advisor model id.

          - `Type BetaManagedAgentsAdvisorType`

      - `Type BetaManagedAgentsSessionMultiagentCoordinatorType`

    - `Name string`

    - `Skills []BetaManagedAgentsSessionAgentSkillUnion`

      - `type BetaManagedAgentsAnthropicSkill struct{…}`

        A resolved Anthropic-managed skill.

      - `type BetaManagedAgentsCustomSkill struct{…}`

        A resolved user-created custom skill.

    - `System string`

    - `Tools []BetaManagedAgentsSessionAgentToolUnion`

      - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

      - `type BetaManagedAgentsMCPToolset struct{…}`

      - `type BetaManagedAgentsCustomTool struct{…}`

        A custom tool as returned in API responses.

    - `Type BetaManagedAgentsSessionAgentType`

    - `Version int64`

      format: int32

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `Budget BetaManagedAgentsBudgetLimit`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `MaxListCost BetaMonetaryAmount`

      A monetary amount in a specific currency.

      - `Amount string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `Currency BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `Type BetaManagedAgentsBudgetLimitType`

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `EnvironmentID string`

  - `Metadata map[string, string]`

  - `OutcomeEvaluations []BetaManagedAgentsOutcomeEvaluationResource`

    Per-outcome evaluation state. One entry per define_outcome event sent to the session.

    - `CompletedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Description string`

      What the agent should produce.

    - `Explanation string`

      Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs_revision (intermediate), what's missing; for failed, why unrecoverable.

    - `Iteration int64`

      0-indexed revision cycle the outcome is currently on.

      format: int32

    - `OutcomeID string`

      Server-generated outc_ ID for this outcome.

    - `Result string`

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

    - `Type BetaManagedAgentsOutcomeEvaluationResourceType`

  - `Resources []BetaManagedAgentsSessionResourceUnion`

    - `type BetaManagedAgentsGitHubRepositoryResource struct{…}`

      - `ID string`

      - `CreatedAt Time`

        A timestamp in RFC 3339 format

        format: date-time

      - `MountPath string`

      - `Type BetaManagedAgentsGitHubRepositoryResourceType`

      - `UpdatedAt Time`

        A timestamp in RFC 3339 format

        format: date-time

      - `URL string`

      - `Checkout BetaManagedAgentsGitHubRepositoryResourceCheckoutUnion Optional`

        - `type BetaManagedAgentsBranchCheckout struct{…}`

          - `Name string`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `Type BetaManagedAgentsBranchCheckoutType`

        - `type BetaManagedAgentsCommitCheckout struct{…}`

          - `Sha string`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `Type BetaManagedAgentsCommitCheckoutType`

    - `type BetaManagedAgentsFileResource struct{…}`

      - `ID string`

      - `CreatedAt Time`

        A timestamp in RFC 3339 format

        format: date-time

      - `FileID string`

      - `MountPath string`

      - `Type BetaManagedAgentsFileResourceType`

      - `UpdatedAt Time`

        A timestamp in RFC 3339 format

        format: date-time

    - `type BetaManagedAgentsMemoryStoreResource struct{…}`

      A memory store attached to an agent session.

      - `MemoryStoreID string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type BetaManagedAgentsMemoryStoreResourceType`

      - `Access BetaManagedAgentsMemoryStoreResourceAccess Optional`

        Access mode for an attached memory store.

        - `const BetaManagedAgentsMemoryStoreResourceAccessReadWrite BetaManagedAgentsMemoryStoreResourceAccess = "read_write"`

        - `const BetaManagedAgentsMemoryStoreResourceAccessReadOnly BetaManagedAgentsMemoryStoreResourceAccess = "read_only"`

      - `Description string Optional`

        Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

      - `Instructions string Optional`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

        maxLength: 4096

      - `MountPath string Optional`

        Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

      - `Name string Optional`

        Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

  - `Stats BetaManagedAgentsSessionStats`

    Timing statistics for a session.

    - `ActiveSeconds float64 Optional`

      Cumulative time in seconds the session spent in running status. Excludes idle time.

      format: double

    - `DurationSeconds float64 Optional`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

      format: double

  - `Status BetaManagedAgentsSessionStatus`

    SessionStatus enum

    - `const BetaManagedAgentsSessionStatusRescheduling BetaManagedAgentsSessionStatus = "rescheduling"`

    - `const BetaManagedAgentsSessionStatusRunning BetaManagedAgentsSessionStatus = "running"`

    - `const BetaManagedAgentsSessionStatusIdle BetaManagedAgentsSessionStatus = "idle"`

    - `const BetaManagedAgentsSessionStatusTerminated BetaManagedAgentsSessionStatus = "terminated"`

  - `Title string`

  - `Type BetaManagedAgentsSessionType`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `Usage BetaManagedAgentsSessionUsage`

    Cumulative token usage for a session across all turns.

    - `ActiveSeconds float64 Optional`

      Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once, unlike `stats.active_seconds`, which sums each thread's own active time. This is the duration the session's runtime cost is priced on.

      format: double

    - `CacheCreation BetaManagedAgentsCacheCreationUsage Optional`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `Ephemeral1hInputTokens int64 Optional`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `Ephemeral5mInputTokens int64 Optional`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `CacheReadInputTokens int64 Optional`

      Total tokens read from prompt cache.

      format: int32

    - `InputTokens int64 Optional`

      Total input tokens consumed across all turns.

      format: int32

    - `ListCost BetaMonetaryAmount Optional`

      A monetary amount in a specific currency.

    - `OutputTokens int64 Optional`

      Total output tokens generated across all turns.

      format: int32

    - `ServerToolUse BetaManagedAgentsServerToolUsage Optional`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `WebFetchRequests int64 Optional`

        Number of server-executed web fetch requests.

        format: int32

      - `WebSearchRequests int64 Optional`

        Number of server-executed web search requests.

        format: int32

  - `VaultIDs []string`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `DeploymentID string Optional`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Example

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
	betaManagedAgentsSession, err := client.Beta.Sessions.Archive(
		context.TODO(),
		"sesn_011CZkZAtmR3yMPDzynEDxu7",
		anthropic.BetaSessionArchiveParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaManagedAgentsSession.ID)
}
```

#### Response (200)

```json
{
  "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "agent": {
    "id": "agent_011CZkYpogX7uDKUyvBTophP",
    "description": "A general-purpose starter agent.",
    "mcp_servers": [
      {
        "name": "example-mcp",
        "type": "url",
        "url": "https://example-server.modelcontextprotocol.io/sse"
      }
    ],
    "model": {
      "id": "claude-opus-5",
      "effort": {
        "type": "low"
      },
      "inference_geo": "inference_geo",
      "speed": "standard"
    },
    "multiagent": {
      "agents": [
        {
          "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
          "description": "A focused research subagent.",
          "mcp_servers": [
            {
              "name": "example-mcp",
              "type": "url",
              "url": "https://example-server.modelcontextprotocol.io/sse"
            }
          ],
          "model": {
            "id": "claude-opus-5",
            "effort": {
              "type": "low"
            },
            "inference_geo": "inference_geo",
            "speed": "standard"
          },
          "name": "Researcher",
          "skills": [
            {
              "skill_id": "xlsx",
              "type": "anthropic",
              "version": "1"
            }
          ],
          "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
          "tools": [
            {
              "configs": [
                {
                  "enabled": true,
                  "name": "bash",
                  "permission_policy": {
                    "type": "always_allow"
                  },
                  "type": "bash"
                }
              ],
              "default_config": {
                "enabled": true,
                "permission_policy": {
                  "type": "always_ask"
                }
              },
              "type": "agent_toolset_20260401"
            }
          ],
          "type": "agent",
          "version": 1
        }
      ],
      "type": "coordinator"
    },
    "name": "My First Agent",
    "skills": [
      {
        "skill_id": "xlsx",
        "type": "anthropic",
        "version": "1"
      },
      {
        "skill_id": "skill_011CZkZFNu9hAbo3jZPRgTlx",
        "type": "custom",
        "version": "2"
      }
    ],
    "system": "You are a general-purpose agent that can research, write code, run commands, and use connected tools to complete the user's task end to end.",
    "tools": [
      {
        "configs": [
          {
            "enabled": true,
            "name": "bash",
            "permission_policy": {
              "type": "always_allow"
            },
            "type": "bash"
          }
        ],
        "default_config": {
          "enabled": true,
          "permission_policy": {
            "type": "always_ask"
          }
        },
        "type": "agent_toolset_20260401"
      }
    ],
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "budget": {
    "max_list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "type": "limit"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "metadata": {},
  "outcome_evaluations": [
    {
      "completed_at": "2026-03-15T10:02:31Z",
      "description": "Produce a 2-page summary as summary.md",
      "explanation": "All five sections present with inline citations.",
      "iteration": 0,
      "outcome_id": "outc_011CZkZRSw2kEfs6ncTVljxP",
      "result": "satisfied",
      "type": "outcome_evaluation"
    }
  ],
  "resources": [
    {
      "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
      "created_at": "2026-03-15T10:00:00Z",
      "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
      "mount_path": "/uploads/receipt.pdf",
      "type": "file",
      "updated_at": "2026-03-15T10:00:00Z"
    },
    {
      "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
      "created_at": "2026-03-15T10:00:00Z",
      "mount_path": "/workspace/example-repo",
      "type": "github_repository",
      "updated_at": "2026-03-15T10:00:00Z",
      "url": "https://github.com/example-org/example-repo",
      "checkout": {
        "name": "main",
        "type": "branch"
      }
    }
  ],
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0
  },
  "status": "idle",
  "title": "Order #1234 inquiry",
  "type": "session",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "active_seconds": 0,
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "output_tokens": 0,
    "server_tool_use": {
      "web_fetch_requests": 0,
      "web_search_requests": 3
    }
  },
  "vault_ids": [
    "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  ],
  "deployment_id": "deployment_id"
}
```

## Domain types

### Beta Managed Agents Advisor Params

- `type BetaManagedAgentsAdvisorParamsResp struct{…}`

  Platform advisor roster entry: a model the session's primary thread may consult mid-turn. At most one per roster; the entry occupies the roster name `anthropic.advisor`.

  - `Model string`

    A Claude model id. The model must be permitted as an advisor for this agent's model — see the sessions/threads/advisor spec.

    minLength: 1, maxLength: 256

  - `Type BetaManagedAgentsAdvisorParamsType`

### Beta Managed Agents Agent Message Preview

- `type BetaManagedAgentsAgentMessagePreview struct{…}`

  - `ID string`

    The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

  - `Type BetaManagedAgentsAgentMessagePreviewType`

### Beta Managed Agents Agent Params

- `type BetaManagedAgentsAgentParamsResp struct{…}`

  Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

  - `ID string`

    The `agent` ID.

    minLength: 1, maxLength: 128

  - `Type BetaManagedAgentsAgentParamsType`

  - `Version int64 Optional`

    The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

    format: int32

### Beta Managed Agents Agent Thinking Preview

- `type BetaManagedAgentsAgentThinkingPreview struct{…}`

  - `ID string`

    The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

  - `Type BetaManagedAgentsAgentThinkingPreviewType`

### Beta Managed Agents Agent With Overrides Params

- `type BetaManagedAgentsAgentWithOverridesParamsResp struct{…}`

  Reference to an `agent` plus optional configuration overrides. Each provided field replaces the agent's value for the caller's use; the agent resource is unchanged.

  - `ID string`

    The `agent` ID.

    minLength: 1, maxLength: 128

  - `Type BetaManagedAgentsAgentWithOverridesParamsType`

  - `MCPServers []BetaManagedAgentsURLMCPServerParamsResp Optional`

    Replacement MCP server list. Full replacement: the provided array becomes the MCP servers. Send an empty array to clear; omit to preserve the agent's servers.

    - `Name string`

      Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

      minLength: 1, maxLength: 255

    - `Type BetaManagedAgentsURLMCPServerParamsType`

    - `URL string`

      Endpoint URL for the MCP server.

      maxLength: 2048

  - `Model BetaManagedAgentsModelConfigParamsResp Optional`

    Replacement model. Accepts the model string, e.g. `claude-opus-5`, or a `model_config` object. Omit to use the agent's model.

    - `type BetaManagedAgentsModelConfigParamsResp struct{…}`

      An object that defines additional configuration control over model use

      - `ID BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `type BetaManagedAgentsModel string`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `const BetaManagedAgentsModelClaudeSonnet5 BetaManagedAgentsModel = "claude-sonnet-5"`

            High-performance model for coding and agents

          - `const BetaManagedAgentsModelClaudeFable5 BetaManagedAgentsModel = "claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `const BetaManagedAgentsModelClaudeOpus5 BetaManagedAgentsModel = "claude-opus-5"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeOpus4_8 BetaManagedAgentsModel = "claude-opus-4-8"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeOpus4_7 BetaManagedAgentsModel = "claude-opus-4-7"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeOpus4_6 BetaManagedAgentsModel = "claude-opus-4-6"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeSonnet4_6 BetaManagedAgentsModel = "claude-sonnet-4-6"`

            Best combination of speed and intelligence

          - `const BetaManagedAgentsModelClaudeHaiku4_5 BetaManagedAgentsModel = "claude-haiku-4-5"`

            Fastest model with near-frontier intelligence

          - `const BetaManagedAgentsModelClaudeHaiku4_5_20251001 BetaManagedAgentsModel = "claude-haiku-4-5-20251001"`

            Fastest model with near-frontier intelligence

          - `const BetaManagedAgentsModelClaudeOpus4_5 BetaManagedAgentsModel = "claude-opus-4-5"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeOpus4_5_20251101 BetaManagedAgentsModel = "claude-opus-4-5-20251101"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeSonnet4_5 BetaManagedAgentsModel = "claude-sonnet-4-5"`

            High-performance model for agents and coding

          - `const BetaManagedAgentsModelClaudeSonnet4_5_20250929 BetaManagedAgentsModel = "claude-sonnet-4-5-20250929"`

            High-performance model for agents and coding

        - `string`

      - `Effort BetaManagedAgentsModelConfigParamsEffortUnionResp Optional`

        How hard Claude works on each inference call. Accepts a bare level string (`"high"`) or `{"type": "high"}`. On create, omitting it resolves the per-model default; on update, omitting it leaves the stored value unchanged.

        - `string`

          - `const BetaManagedAgentsModelConfigParamsEffortBetaManagedAgentsEffortLevelLow BetaManagedAgentsModelConfigParamsEffortBetaManagedAgentsEffortLevel = "low"`

          - `const BetaManagedAgentsModelConfigParamsEffortBetaManagedAgentsEffortLevelMedium BetaManagedAgentsModelConfigParamsEffortBetaManagedAgentsEffortLevel = "medium"`

          - `const BetaManagedAgentsModelConfigParamsEffortBetaManagedAgentsEffortLevelHigh BetaManagedAgentsModelConfigParamsEffortBetaManagedAgentsEffortLevel = "high"`

          - `const BetaManagedAgentsModelConfigParamsEffortBetaManagedAgentsEffortLevelXhigh BetaManagedAgentsModelConfigParamsEffortBetaManagedAgentsEffortLevel = "xhigh"`

          - `const BetaManagedAgentsModelConfigParamsEffortBetaManagedAgentsEffortLevelMax BetaManagedAgentsModelConfigParamsEffortBetaManagedAgentsEffortLevel = "max"`

        - `type BetaManagedAgentsEffortLow struct{…}`

          Low effort. Favors latency over reasoning depth.

          - `Type BetaManagedAgentsEffortLowType`

        - `type BetaManagedAgentsEffortMedium struct{…}`

          Medium effort. Balances latency and reasoning depth.

          - `Type BetaManagedAgentsEffortMediumType`

        - `type BetaManagedAgentsEffortHigh struct{…}`

          High effort. Favors reasoning depth.

          - `Type BetaManagedAgentsEffortHighType`

        - `type BetaManagedAgentsEffortXhigh struct{…}`

          Extra-high effort. Not all models accept this level.

          - `Type BetaManagedAgentsEffortXhighType`

        - `type BetaManagedAgentsEffortMax struct{…}`

          Maximum effort. Favors reasoning depth over latency.

          - `Type BetaManagedAgentsEffortMaxType`

      - `InferenceGeo string Optional`

        Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo. On update, `model` is whole-object replacement — omitting inference_geo clears it.

      - `Speed BetaManagedAgentsModelConfigParamsSpeed Optional`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `const BetaManagedAgentsModelConfigParamsSpeedStandard BetaManagedAgentsModelConfigParamsSpeed = "standard"`

        - `const BetaManagedAgentsModelConfigParamsSpeedFast BetaManagedAgentsModelConfigParamsSpeed = "fast"`

  - `Skills []BetaManagedAgentsSkillParamsUnionResp Optional`

    Replacement skill list. Full replacement: the provided array becomes the skills. Send an empty array to clear; omit to preserve the agent's skills.

    - `type BetaManagedAgentsAnthropicSkillParamsResp struct{…}`

      An Anthropic-managed skill.

      - `SkillID string`

        Identifier of the Anthropic skill (e.g., "xlsx").

        minLength: 1, maxLength: 64

      - `Type BetaManagedAgentsAnthropicSkillParamsType`

      - `Version string Optional`

        Version to pin. Defaults to latest if omitted.

        minLength: 1, maxLength: 64

    - `type BetaManagedAgentsCustomSkillParamsResp struct{…}`

      A user-created custom skill.

      - `SkillID string`

        Tagged ID of the custom skill (e.g., "skill_01XJ5...").

        minLength: 1, maxLength: 64

      - `Type BetaManagedAgentsCustomSkillParamsType`

      - `Version string Optional`

        Version to pin. Defaults to latest if omitted.

        minLength: 1, maxLength: 64

  - `System string Optional`

    Replacement system prompt. Up to 100,000 characters. Set to null to clear the agent's system prompt; omit to preserve it.

    maxLength: 100000

  - `Tools []BetaManagedAgentsAgentWithOverridesParamsToolUnionResp Optional`

    Replacement tool list. Full replacement: the provided array becomes the tool configuration. Send an empty array to clear; omit to preserve the agent's tools.

    - `type BetaManagedAgentsAgentToolset20260401ParamsResp struct{…}`

      Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

      - `Type BetaManagedAgentsAgentToolset20260401ParamsType`

      - `Configs []BetaManagedAgentsAgentToolConfigParamsUnionResp Optional`

        Per-tool configuration overrides.

        - `type BetaManagedAgentsBashToolConfigParamsResp struct{…}`

          Configuration override for the bash tool.

          - `Name Bash`

            Must be "bash".

          - `Enabled bool Optional`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy BetaManagedAgentsBashToolConfigParamsPermissionPolicyUnionResp Optional`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

              - `Type BetaManagedAgentsAlwaysAllowPolicyType`

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

              - `Type BetaManagedAgentsAlwaysAskPolicyType`

          - `Type BetaManagedAgentsBashToolConfigParamsType Optional`

        - `type BetaManagedAgentsEditToolConfigParamsResp struct{…}`

          Configuration override for the edit tool.

          - `Name Edit`

            Must be "edit".

          - `Enabled bool Optional`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy BetaManagedAgentsEditToolConfigParamsPermissionPolicyUnionResp Optional`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type BetaManagedAgentsEditToolConfigParamsType Optional`

        - `type BetaManagedAgentsReadToolConfigParamsResp struct{…}`

          Configuration override for the read tool.

          - `Name Read`

            Must be "read".

          - `Enabled bool Optional`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy BetaManagedAgentsReadToolConfigParamsPermissionPolicyUnionResp Optional`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type BetaManagedAgentsReadToolConfigParamsType Optional`

        - `type BetaManagedAgentsWriteToolConfigParamsResp struct{…}`

          Configuration override for the write tool.

          - `Name Write`

            Must be "write".

          - `Enabled bool Optional`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy BetaManagedAgentsWriteToolConfigParamsPermissionPolicyUnionResp Optional`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type BetaManagedAgentsWriteToolConfigParamsType Optional`

        - `type BetaManagedAgentsGlobToolConfigParamsResp struct{…}`

          Configuration override for the glob tool.

          - `Name Glob`

            Must be "glob".

          - `Enabled bool Optional`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy BetaManagedAgentsGlobToolConfigParamsPermissionPolicyUnionResp Optional`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type BetaManagedAgentsGlobToolConfigParamsType Optional`

        - `type BetaManagedAgentsGrepToolConfigParamsResp struct{…}`

          Configuration override for the grep tool.

          - `Name Grep`

            Must be "grep".

          - `Enabled bool Optional`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy BetaManagedAgentsGrepToolConfigParamsPermissionPolicyUnionResp Optional`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type BetaManagedAgentsGrepToolConfigParamsType Optional`

        - `type BetaManagedAgentsWebFetchToolConfigParamsResp struct{…}`

          Configuration override for the web_fetch tool.

          - `Name WebFetch`

            Must be "web_fetch".

          - `AllowedDomains []string Optional`

            Only fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

          - `BlockedDomains []string Optional`

            Never fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

          - `Enabled bool Optional`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `MaxContentTokens int64 Optional`

            Maximum number of tokens of fetched text content to include in context per call. Does not apply to binary content such as PDFs.

            format: int32

          - `PermissionPolicy BetaManagedAgentsWebFetchToolConfigParamsPermissionPolicyUnionResp Optional`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type BetaManagedAgentsWebFetchToolConfigParamsType Optional`

        - `type BetaManagedAgentsWebSearchToolConfigParamsResp struct{…}`

          Configuration override for the web_search tool.

          - `Name WebSearch`

            Must be "web_search".

          - `AllowedDomains []string Optional`

            Only return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

          - `BlockedDomains []string Optional`

            Never return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

          - `Enabled bool Optional`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy BetaManagedAgentsWebSearchToolConfigParamsPermissionPolicyUnionResp Optional`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type BetaManagedAgentsWebSearchToolConfigParamsType Optional`

          - `UserLocation BetaManagedAgentsUserLocation Optional`

            Approximate user location for search result localization.

            - `Type Approximate`

              Location precision. Only "approximate" is supported.

            - `City string Optional`

              City name.

              minLength: 1, maxLength: 255

            - `Country string Optional`

              Two-letter ISO 3166-1 country code, uppercase.

            - `Region string Optional`

              Region or state name.

              minLength: 1, maxLength: 255

            - `Timezone string Optional`

              IANA timezone identifier, e.g. "America/Los_Angeles".

              minLength: 1, maxLength: 255

      - `DefaultConfig BetaManagedAgentsAgentToolsetDefaultConfigParamsResp Optional`

        Default configuration for all tools in a toolset.

        - `Enabled bool Optional`

          Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

        - `PermissionPolicy BetaManagedAgentsAgentToolsetDefaultConfigParamsPermissionPolicyUnionResp Optional`

          Permission policy for tool execution.

          - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

            Tool calls are automatically approved without user confirmation.

          - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

            Tool calls require user confirmation before execution.

    - `type BetaManagedAgentsMCPToolsetParamsResp struct{…}`

      Configuration for tools from an MCP server defined in `mcp_servers`.

      - `MCPServerName string`

        Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

        minLength: 1, maxLength: 255

      - `Type BetaManagedAgentsMCPToolsetParamsType`

      - `Configs []BetaManagedAgentsMCPToolConfigParamsResp Optional`

        Per-tool configuration overrides.

        - `Name string`

          Name of the MCP tool to configure. 1-128 characters.

          minLength: 1, maxLength: 128

        - `Enabled bool Optional`

          Whether this tool is enabled. Overrides the `default_config` setting.

        - `PermissionPolicy BetaManagedAgentsMCPToolConfigParamsPermissionPolicyUnionResp Optional`

          Permission policy for tool execution.

          - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

            Tool calls are automatically approved without user confirmation.

          - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

            Tool calls require user confirmation before execution.

      - `DefaultConfig BetaManagedAgentsMCPToolsetDefaultConfigParamsResp Optional`

        Default configuration for all tools from an MCP server.

        - `Enabled bool Optional`

          Whether tools are enabled by default. Defaults to true if not specified.

        - `PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigParamsPermissionPolicyUnionResp Optional`

          Permission policy for tool execution.

          - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

            Tool calls are automatically approved without user confirmation.

          - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

            Tool calls require user confirmation before execution.

    - `type BetaManagedAgentsCustomToolParamsResp struct{…}`

      A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

      - `Description string`

        Description of what the tool does, shown to the agent to help it decide when to use the tool.

        minLength: 1

      - `InputSchema BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `Type Object`

        - `Properties map[string, any] Optional`

        - `Required []string Optional`

      - `Name string`

        Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

        minLength: 1, maxLength: 128

      - `Type BetaManagedAgentsCustomToolParamsType`

  - `Version int64 Optional`

    The specific `agent` version to use. Omit to use the latest version.

    format: int32

### Beta Managed Agents Branch Checkout

- `type BetaManagedAgentsBranchCheckout struct{…}`

  - `Name string`

    Branch name to check out.

    minLength: 1, maxLength: 255

  - `Type BetaManagedAgentsBranchCheckoutType`

### Beta Managed Agents Budget Limit

- `type BetaManagedAgentsBudgetLimit struct{…}`

  A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

  - `MaxListCost BetaMonetaryAmount`

    A monetary amount in a specific currency.

    - `Amount string`

      Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

    - `Currency BetaCurrency`

      Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

  - `Type BetaManagedAgentsBudgetLimitType`

### Beta Managed Agents Cache Creation Usage

- `type BetaManagedAgentsCacheCreationUsage struct{…}`

  Prompt-cache creation token usage broken down by cache lifetime.

  - `Ephemeral1hInputTokens int64 Optional`

    Tokens used to create 1-hour ephemeral cache entries.

    format: int32

  - `Ephemeral5mInputTokens int64 Optional`

    Tokens used to create 5-minute ephemeral cache entries.

    format: int32

### Beta Managed Agents Commit Checkout

- `type BetaManagedAgentsCommitCheckout struct{…}`

  - `Sha string`

    Full commit SHA to check out.

    minLength: 7, maxLength: 64

  - `Type BetaManagedAgentsCommitCheckoutType`

### Beta Managed Agents Deleted Session

- `type BetaManagedAgentsDeletedSession struct{…}`

  Confirmation that a `session` has been permanently deleted.

  - `ID string`

  - `Type BetaManagedAgentsDeletedSessionType`

### Beta Managed Agents Delta Content

- `type BetaManagedAgentsDeltaContent struct{…}`

  - `Content BetaManagedAgentsTextBlock`

    Regular text content.

    - `Text string`

      The text content.

      minLength: 1

    - `Type BetaManagedAgentsTextBlockType`

  - `Type BetaManagedAgentsDeltaContentType`

  - `Index int64 Optional`

    Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

    format: uint32

### Beta Managed Agents Delta Event

- `type BetaManagedAgentsDeltaEvent struct{…}`

  An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

  - `Delta BetaManagedAgentsDeltaContent`

    One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

    - `Content BetaManagedAgentsTextBlock`

      Regular text content.

      - `Text string`

        The text content.

        minLength: 1

      - `Type BetaManagedAgentsTextBlockType`

    - `Type BetaManagedAgentsDeltaContentType`

    - `Index int64 Optional`

      Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

      format: uint32

  - `EventID string`

    The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

  - `Type BetaManagedAgentsDeltaEventType`

### Beta Managed Agents Delta Type

- `type BetaManagedAgentsDeltaType string`

  EventDeltaType enum

  - `const BetaManagedAgentsDeltaTypeAgentMessage BetaManagedAgentsDeltaType = "agent.message"`

  - `const BetaManagedAgentsDeltaTypeAgentThinking BetaManagedAgentsDeltaType = "agent.thinking"`

### Beta Managed Agents File Resource Params

- `type BetaManagedAgentsFileResourceParamsResp struct{…}`

  Mount a file uploaded via the Files API into the session.

  - `FileID string`

    ID of a previously uploaded file.

    minLength: 1, maxLength: 128

  - `Type BetaManagedAgentsFileResourceParamsType`

  - `MountPath string Optional`

    Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    minLength: 1, maxLength: 4096

### Beta Managed Agents GitHub Repository Resource Params

- `type BetaManagedAgentsGitHubRepositoryResourceParamsResp struct{…}`

  Mount a GitHub repository into the session's container.

  - `AuthorizationToken string`

    GitHub authorization token used to clone the repository.

    minLength: 1, maxLength: 4096

  - `Type BetaManagedAgentsGitHubRepositoryResourceParamsType`

  - `URL string`

    Github URL of the repository

    minLength: 1, maxLength: 2048

  - `Checkout BetaManagedAgentsGitHubRepositoryResourceParamsCheckoutUnionResp Optional`

    Branch or commit to check out. Defaults to the repository's default branch.

    - `type BetaManagedAgentsBranchCheckout struct{…}`

      - `Name string`

        Branch name to check out.

        minLength: 1, maxLength: 255

      - `Type BetaManagedAgentsBranchCheckoutType`

    - `type BetaManagedAgentsCommitCheckout struct{…}`

      - `Sha string`

        Full commit SHA to check out.

        minLength: 7, maxLength: 64

      - `Type BetaManagedAgentsCommitCheckoutType`

  - `MountPath string Optional`

    Mount path in the container. Defaults to `/workspace/<repo-name>`.

    minLength: 1, maxLength: 4096

### Beta Managed Agents Memory Store Resource Param

- `type BetaManagedAgentsMemoryStoreResourceParamResp struct{…}`

  Parameters for attaching a memory store to an agent session.

  - `MemoryStoreID string`

    The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

  - `Type BetaManagedAgentsMemoryStoreResourceParamType`

  - `Access BetaManagedAgentsMemoryStoreResourceParamAccess Optional`

    Access mode for an attached memory store.

    - `const BetaManagedAgentsMemoryStoreResourceParamAccessReadWrite BetaManagedAgentsMemoryStoreResourceParamAccess = "read_write"`

    - `const BetaManagedAgentsMemoryStoreResourceParamAccessReadOnly BetaManagedAgentsMemoryStoreResourceParamAccess = "read_only"`

  - `Instructions string Optional`

    Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

    maxLength: 4096

### Beta Managed Agents Multiagent

- `type BetaManagedAgentsMultiagent struct{…}`

  Resolved coordinator topology with a concrete agent roster.

  - `Agents []BetaManagedAgentsMultiagentAgentUnion`

    Agents the coordinator may spawn as session threads, each resolved to a specific version.

    - `type BetaManagedAgentsAgentReference struct{…}`

      A resolved agent reference with a concrete version.

      - `ID string`

      - `Type BetaManagedAgentsAgentReferenceType`

      - `Version int64`

        format: int32

    - `type BetaManagedAgentsAdvisor struct{…}`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `Model string`

        The advisor model id.

      - `Type BetaManagedAgentsAdvisorType`

  - `Type BetaManagedAgentsMultiagentType`

### Beta Managed Agents Multiagent Params

- `type BetaManagedAgentsMultiagentParamsResp struct{…}`

  A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.

  - `Agents []BetaManagedAgentsMultiagentRosterEntryParamsUnionResp`

    Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).

    - `string`

    - `type BetaManagedAgentsAgentParamsResp struct{…}`

      Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

      - `ID string`

        The `agent` ID.

        minLength: 1, maxLength: 128

      - `Type BetaManagedAgentsAgentParamsType`

      - `Version int64 Optional`

        The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

        format: int32

    - `type BetaManagedAgentsMultiagentSelfParamsResp struct{…}`

      Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

      - `Type BetaManagedAgentsMultiagentSelfParamsType`

    - `type BetaManagedAgentsAdvisorParamsResp struct{…}`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn. At most one per roster; the entry occupies the roster name `anthropic.advisor`.

      - `Model string`

        A Claude model id. The model must be permitted as an advisor for this agent's model — see the sessions/threads/advisor spec.

        minLength: 1, maxLength: 256

      - `Type BetaManagedAgentsAdvisorParamsType`

  - `Type BetaManagedAgentsMultiagentParamsType`

### Beta Managed Agents Multiagent Roster Entry Params

- `type BetaManagedAgentsMultiagentRosterEntryParamsUnionResp interface{…}`

  An entry in a multiagent roster: an agent ID string, a versioned agent reference, or `self`.

  - `string`

  - `type BetaManagedAgentsAgentParamsResp struct{…}`

    Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

    - `ID string`

      The `agent` ID.

      minLength: 1, maxLength: 128

    - `Type BetaManagedAgentsAgentParamsType`

    - `Version int64 Optional`

      The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

      format: int32

  - `type BetaManagedAgentsMultiagentSelfParamsResp struct{…}`

    Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

    - `Type BetaManagedAgentsMultiagentSelfParamsType`

  - `type BetaManagedAgentsAdvisorParamsResp struct{…}`

    Platform advisor roster entry: a model the session's primary thread may consult mid-turn. At most one per roster; the entry occupies the roster name `anthropic.advisor`.

    - `Model string`

      A Claude model id. The model must be permitted as an advisor for this agent's model — see the sessions/threads/advisor spec.

      minLength: 1, maxLength: 256

    - `Type BetaManagedAgentsAdvisorParamsType`

### Beta Managed Agents Outcome Evaluation Resource

- `type BetaManagedAgentsOutcomeEvaluationResource struct{…}`

  Evaluation state for a single outcome defined via a define_outcome event.

  - `CompletedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `Description string`

    What the agent should produce.

  - `Explanation string`

    Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs_revision (intermediate), what's missing; for failed, why unrecoverable.

  - `Iteration int64`

    0-indexed revision cycle the outcome is currently on.

    format: int32

  - `OutcomeID string`

    Server-generated outc_ ID for this outcome.

  - `Result string`

    Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

  - `Type BetaManagedAgentsOutcomeEvaluationResourceType`

### Beta Managed Agents Server Tool Usage

- `type BetaManagedAgentsServerToolUsage struct{…}`

  Cumulative count of server-executed tool invocations, broken down by tool.

  - `WebFetchRequests int64 Optional`

    Number of server-executed web fetch requests.

    format: int32

  - `WebSearchRequests int64 Optional`

    Number of server-executed web search requests.

    format: int32

### Beta Managed Agents Session

- `type BetaManagedAgentsSession struct{…}`

  A Managed Agents `session`.

  - `ID string`

  - `Agent BetaManagedAgentsSessionAgent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `ID string`

    - `Description string`

    - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

      - `Name string`

      - `Type BetaManagedAgentsMCPServerURLDefinitionType`

      - `URL string`

    - `Model BetaManagedAgentsModelConfig`

      Model identifier and configuration.

      - `ID BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `type BetaManagedAgentsModel string`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `const BetaManagedAgentsModelClaudeSonnet5 BetaManagedAgentsModel = "claude-sonnet-5"`

            High-performance model for coding and agents

          - `const BetaManagedAgentsModelClaudeFable5 BetaManagedAgentsModel = "claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `const BetaManagedAgentsModelClaudeOpus5 BetaManagedAgentsModel = "claude-opus-5"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeOpus4_8 BetaManagedAgentsModel = "claude-opus-4-8"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeOpus4_7 BetaManagedAgentsModel = "claude-opus-4-7"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeOpus4_6 BetaManagedAgentsModel = "claude-opus-4-6"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeSonnet4_6 BetaManagedAgentsModel = "claude-sonnet-4-6"`

            Best combination of speed and intelligence

          - `const BetaManagedAgentsModelClaudeHaiku4_5 BetaManagedAgentsModel = "claude-haiku-4-5"`

            Fastest model with near-frontier intelligence

          - `const BetaManagedAgentsModelClaudeHaiku4_5_20251001 BetaManagedAgentsModel = "claude-haiku-4-5-20251001"`

            Fastest model with near-frontier intelligence

          - `const BetaManagedAgentsModelClaudeOpus4_5 BetaManagedAgentsModel = "claude-opus-4-5"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeOpus4_5_20251101 BetaManagedAgentsModel = "claude-opus-4-5-20251101"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeSonnet4_5 BetaManagedAgentsModel = "claude-sonnet-4-5"`

            High-performance model for agents and coding

          - `const BetaManagedAgentsModelClaudeSonnet4_5_20250929 BetaManagedAgentsModel = "claude-sonnet-4-5-20250929"`

            High-performance model for agents and coding

        - `string`

      - `Effort BetaManagedAgentsModelConfigEffortUnion Optional`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

        - `type BetaManagedAgentsEffortLow struct{…}`

          Low effort. Favors latency over reasoning depth.

          - `Type BetaManagedAgentsEffortLowType`

        - `type BetaManagedAgentsEffortMedium struct{…}`

          Medium effort. Balances latency and reasoning depth.

          - `Type BetaManagedAgentsEffortMediumType`

        - `type BetaManagedAgentsEffortHigh struct{…}`

          High effort. Favors reasoning depth.

          - `Type BetaManagedAgentsEffortHighType`

        - `type BetaManagedAgentsEffortXhigh struct{…}`

          Extra-high effort. Not all models accept this level.

          - `Type BetaManagedAgentsEffortXhighType`

        - `type BetaManagedAgentsEffortMax struct{…}`

          Maximum effort. Favors reasoning depth over latency.

          - `Type BetaManagedAgentsEffortMaxType`

      - `InferenceGeo string Optional`

        Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

      - `Speed BetaManagedAgentsModelConfigSpeed Optional`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `const BetaManagedAgentsModelConfigSpeedStandard BetaManagedAgentsModelConfigSpeed = "standard"`

        - `const BetaManagedAgentsModelConfigSpeedFast BetaManagedAgentsModelConfigSpeed = "fast"`

    - `Multiagent BetaManagedAgentsSessionMultiagentCoordinator`

      Resolved coordinator topology with full agent definitions for each roster member.

      - `Agents []BetaManagedAgentsSessionMultiagentCoordinatorAgentUnion`

        Full `agent` definitions the coordinator may spawn as session threads.

        - `type BetaManagedAgentsSessionThreadAgent struct{…}`

          Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

          - `ID string`

          - `Description string`

          - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

            - `Name string`

            - `Type BetaManagedAgentsMCPServerURLDefinitionType`

            - `URL string`

          - `Model BetaManagedAgentsModelConfig`

            Model identifier and configuration.

          - `Name string`

          - `Skills []BetaManagedAgentsSessionThreadAgentSkillUnion`

            - `type BetaManagedAgentsAnthropicSkill struct{…}`

              A resolved Anthropic-managed skill.

              - `SkillID string`

              - `Type BetaManagedAgentsAnthropicSkillType`

              - `Version string`

            - `type BetaManagedAgentsCustomSkill struct{…}`

              A resolved user-created custom skill.

              - `SkillID string`

              - `Type BetaManagedAgentsCustomSkillType`

              - `Version string`

          - `System string`

          - `Tools []BetaManagedAgentsSessionThreadAgentToolUnion`

            - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

              - `Configs []BetaManagedAgentsAgentToolConfigUnion`

                - `type BetaManagedAgentsBashToolConfig struct{…}`

                  Configuration for the bash tool.

                  - `Enabled bool`

                  - `Name Bash`

                  - `PermissionPolicy BetaManagedAgentsBashToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                      - `Type BetaManagedAgentsAlwaysAllowPolicyType`

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                      - `Type BetaManagedAgentsAlwaysAskPolicyType`

                  - `Type Bash`

                - `type BetaManagedAgentsEditToolConfig struct{…}`

                  Configuration for the edit tool.

                  - `Enabled bool`

                  - `Name Edit`

                  - `PermissionPolicy BetaManagedAgentsEditToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type Edit`

                - `type BetaManagedAgentsReadToolConfig struct{…}`

                  Configuration for the read tool.

                  - `Enabled bool`

                  - `Name Read`

                  - `PermissionPolicy BetaManagedAgentsReadToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type Read`

                - `type BetaManagedAgentsWriteToolConfig struct{…}`

                  Configuration for the write tool.

                  - `Enabled bool`

                  - `Name Write`

                  - `PermissionPolicy BetaManagedAgentsWriteToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type Write`

                - `type BetaManagedAgentsGlobToolConfig struct{…}`

                  Configuration for the glob tool.

                  - `Enabled bool`

                  - `Name Glob`

                  - `PermissionPolicy BetaManagedAgentsGlobToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type Glob`

                - `type BetaManagedAgentsGrepToolConfig struct{…}`

                  Configuration for the grep tool.

                  - `Enabled bool`

                  - `Name Grep`

                  - `PermissionPolicy BetaManagedAgentsGrepToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type Grep`

                - `type BetaManagedAgentsWebFetchToolConfig struct{…}`

                  Configuration for the web_fetch tool.

                  - `Enabled bool`

                  - `Name WebFetch`

                  - `PermissionPolicy BetaManagedAgentsWebFetchToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type WebFetch`

                  - `AllowedDomains []string Optional`

                  - `BlockedDomains []string Optional`

                  - `MaxContentTokens int64 Optional`

                    format: int32

                - `type BetaManagedAgentsWebSearchToolConfig struct{…}`

                  Configuration for the web_search tool.

                  - `Enabled bool`

                  - `Name WebSearch`

                  - `PermissionPolicy BetaManagedAgentsWebSearchToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type WebSearch`

                  - `AllowedDomains []string Optional`

                  - `BlockedDomains []string Optional`

                  - `UserLocation BetaManagedAgentsUserLocation Optional`

                    Approximate user location for search result localization.

                    - `Type Approximate`

                      Location precision. Only "approximate" is supported.

                    - `City string Optional`

                      City name.

                      minLength: 1, maxLength: 255

                    - `Country string Optional`

                      Two-letter ISO 3166-1 country code, uppercase.

                    - `Region string Optional`

                      Region or state name.

                      minLength: 1, maxLength: 255

                    - `Timezone string Optional`

                      IANA timezone identifier, e.g. "America/Los_Angeles".

                      minLength: 1, maxLength: 255

              - `DefaultConfig BetaManagedAgentsAgentToolsetDefaultConfig`

                Resolved default configuration for agent tools.

                - `Enabled bool`

                - `PermissionPolicy BetaManagedAgentsAgentToolsetDefaultConfigPermissionPolicyUnion`

                  Permission policy for tool execution.

                  - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                    Tool calls are automatically approved without user confirmation.

                  - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                    Tool calls require user confirmation before execution.

              - `Type BetaManagedAgentsAgentToolset20260401Type`

            - `type BetaManagedAgentsMCPToolset struct{…}`

              - `Configs []BetaManagedAgentsMCPToolConfig`

                - `Enabled bool`

                - `Name string`

                - `PermissionPolicy BetaManagedAgentsMCPToolConfigPermissionPolicyUnion`

                  Permission policy for tool execution.

                  - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                    Tool calls are automatically approved without user confirmation.

                  - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                    Tool calls require user confirmation before execution.

              - `DefaultConfig BetaManagedAgentsMCPToolsetDefaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `Enabled bool`

                - `PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigPermissionPolicyUnion`

                  Permission policy for tool execution.

                  - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                    Tool calls are automatically approved without user confirmation.

                  - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                    Tool calls require user confirmation before execution.

              - `MCPServerName string`

              - `Type BetaManagedAgentsMCPToolsetType`

            - `type BetaManagedAgentsCustomTool struct{…}`

              A custom tool as returned in API responses.

              - `Description string`

              - `InputSchema BetaManagedAgentsCustomToolInputSchema`

                JSON Schema for custom tool input parameters.

                - `Type Object`

                - `Properties map[string, any] Optional`

                - `Required []string Optional`

              - `Name string`

              - `Type BetaManagedAgentsCustomToolType`

          - `Type BetaManagedAgentsSessionThreadAgentType`

          - `Version int64`

            format: int32

        - `type BetaManagedAgentsAdvisor struct{…}`

          Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

          - `Model string`

            The advisor model id.

          - `Type BetaManagedAgentsAdvisorType`

      - `Type BetaManagedAgentsSessionMultiagentCoordinatorType`

    - `Name string`

    - `Skills []BetaManagedAgentsSessionAgentSkillUnion`

      - `type BetaManagedAgentsAnthropicSkill struct{…}`

        A resolved Anthropic-managed skill.

      - `type BetaManagedAgentsCustomSkill struct{…}`

        A resolved user-created custom skill.

    - `System string`

    - `Tools []BetaManagedAgentsSessionAgentToolUnion`

      - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

      - `type BetaManagedAgentsMCPToolset struct{…}`

      - `type BetaManagedAgentsCustomTool struct{…}`

        A custom tool as returned in API responses.

    - `Type BetaManagedAgentsSessionAgentType`

    - `Version int64`

      format: int32

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `Budget BetaManagedAgentsBudgetLimit`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `MaxListCost BetaMonetaryAmount`

      A monetary amount in a specific currency.

      - `Amount string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `Currency BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `Type BetaManagedAgentsBudgetLimitType`

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `EnvironmentID string`

  - `Metadata map[string, string]`

  - `OutcomeEvaluations []BetaManagedAgentsOutcomeEvaluationResource`

    Per-outcome evaluation state. One entry per define_outcome event sent to the session.

    - `CompletedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Description string`

      What the agent should produce.

    - `Explanation string`

      Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs_revision (intermediate), what's missing; for failed, why unrecoverable.

    - `Iteration int64`

      0-indexed revision cycle the outcome is currently on.

      format: int32

    - `OutcomeID string`

      Server-generated outc_ ID for this outcome.

    - `Result string`

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

    - `Type BetaManagedAgentsOutcomeEvaluationResourceType`

  - `Resources []BetaManagedAgentsSessionResourceUnion`

    - `type BetaManagedAgentsGitHubRepositoryResource struct{…}`

      - `ID string`

      - `CreatedAt Time`

        A timestamp in RFC 3339 format

        format: date-time

      - `MountPath string`

      - `Type BetaManagedAgentsGitHubRepositoryResourceType`

      - `UpdatedAt Time`

        A timestamp in RFC 3339 format

        format: date-time

      - `URL string`

      - `Checkout BetaManagedAgentsGitHubRepositoryResourceCheckoutUnion Optional`

        - `type BetaManagedAgentsBranchCheckout struct{…}`

          - `Name string`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `Type BetaManagedAgentsBranchCheckoutType`

        - `type BetaManagedAgentsCommitCheckout struct{…}`

          - `Sha string`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `Type BetaManagedAgentsCommitCheckoutType`

    - `type BetaManagedAgentsFileResource struct{…}`

      - `ID string`

      - `CreatedAt Time`

        A timestamp in RFC 3339 format

        format: date-time

      - `FileID string`

      - `MountPath string`

      - `Type BetaManagedAgentsFileResourceType`

      - `UpdatedAt Time`

        A timestamp in RFC 3339 format

        format: date-time

    - `type BetaManagedAgentsMemoryStoreResource struct{…}`

      A memory store attached to an agent session.

      - `MemoryStoreID string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type BetaManagedAgentsMemoryStoreResourceType`

      - `Access BetaManagedAgentsMemoryStoreResourceAccess Optional`

        Access mode for an attached memory store.

        - `const BetaManagedAgentsMemoryStoreResourceAccessReadWrite BetaManagedAgentsMemoryStoreResourceAccess = "read_write"`

        - `const BetaManagedAgentsMemoryStoreResourceAccessReadOnly BetaManagedAgentsMemoryStoreResourceAccess = "read_only"`

      - `Description string Optional`

        Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

      - `Instructions string Optional`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

        maxLength: 4096

      - `MountPath string Optional`

        Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

      - `Name string Optional`

        Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

  - `Stats BetaManagedAgentsSessionStats`

    Timing statistics for a session.

    - `ActiveSeconds float64 Optional`

      Cumulative time in seconds the session spent in running status. Excludes idle time.

      format: double

    - `DurationSeconds float64 Optional`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

      format: double

  - `Status BetaManagedAgentsSessionStatus`

    SessionStatus enum

    - `const BetaManagedAgentsSessionStatusRescheduling BetaManagedAgentsSessionStatus = "rescheduling"`

    - `const BetaManagedAgentsSessionStatusRunning BetaManagedAgentsSessionStatus = "running"`

    - `const BetaManagedAgentsSessionStatusIdle BetaManagedAgentsSessionStatus = "idle"`

    - `const BetaManagedAgentsSessionStatusTerminated BetaManagedAgentsSessionStatus = "terminated"`

  - `Title string`

  - `Type BetaManagedAgentsSessionType`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `Usage BetaManagedAgentsSessionUsage`

    Cumulative token usage for a session across all turns.

    - `ActiveSeconds float64 Optional`

      Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once, unlike `stats.active_seconds`, which sums each thread's own active time. This is the duration the session's runtime cost is priced on.

      format: double

    - `CacheCreation BetaManagedAgentsCacheCreationUsage Optional`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `Ephemeral1hInputTokens int64 Optional`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `Ephemeral5mInputTokens int64 Optional`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `CacheReadInputTokens int64 Optional`

      Total tokens read from prompt cache.

      format: int32

    - `InputTokens int64 Optional`

      Total input tokens consumed across all turns.

      format: int32

    - `ListCost BetaMonetaryAmount Optional`

      A monetary amount in a specific currency.

    - `OutputTokens int64 Optional`

      Total output tokens generated across all turns.

      format: int32

    - `ServerToolUse BetaManagedAgentsServerToolUsage Optional`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `WebFetchRequests int64 Optional`

        Number of server-executed web fetch requests.

        format: int32

      - `WebSearchRequests int64 Optional`

        Number of server-executed web search requests.

        format: int32

  - `VaultIDs []string`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `DeploymentID string Optional`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Beta Managed Agents Session Agent

- `type BetaManagedAgentsSessionAgent struct{…}`

  Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

  - `ID string`

  - `Description string`

  - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

    - `Name string`

    - `Type BetaManagedAgentsMCPServerURLDefinitionType`

    - `URL string`

  - `Model BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `ID BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `type BetaManagedAgentsModel string`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `const BetaManagedAgentsModelClaudeSonnet5 BetaManagedAgentsModel = "claude-sonnet-5"`

          High-performance model for coding and agents

        - `const BetaManagedAgentsModelClaudeFable5 BetaManagedAgentsModel = "claude-fable-5"`

          Next generation of intelligence for the hardest knowledge work and coding problems

        - `const BetaManagedAgentsModelClaudeOpus5 BetaManagedAgentsModel = "claude-opus-5"`

          Powerful intelligence for long-running agents and coding

        - `const BetaManagedAgentsModelClaudeOpus4_8 BetaManagedAgentsModel = "claude-opus-4-8"`

          Powerful intelligence for long-running agents and coding

        - `const BetaManagedAgentsModelClaudeOpus4_7 BetaManagedAgentsModel = "claude-opus-4-7"`

          Powerful intelligence for long-running agents and coding

        - `const BetaManagedAgentsModelClaudeOpus4_6 BetaManagedAgentsModel = "claude-opus-4-6"`

          Powerful intelligence for long-running agents and coding

        - `const BetaManagedAgentsModelClaudeSonnet4_6 BetaManagedAgentsModel = "claude-sonnet-4-6"`

          Best combination of speed and intelligence

        - `const BetaManagedAgentsModelClaudeHaiku4_5 BetaManagedAgentsModel = "claude-haiku-4-5"`

          Fastest model with near-frontier intelligence

        - `const BetaManagedAgentsModelClaudeHaiku4_5_20251001 BetaManagedAgentsModel = "claude-haiku-4-5-20251001"`

          Fastest model with near-frontier intelligence

        - `const BetaManagedAgentsModelClaudeOpus4_5 BetaManagedAgentsModel = "claude-opus-4-5"`

          Powerful intelligence for long-running agents and coding

        - `const BetaManagedAgentsModelClaudeOpus4_5_20251101 BetaManagedAgentsModel = "claude-opus-4-5-20251101"`

          Powerful intelligence for long-running agents and coding

        - `const BetaManagedAgentsModelClaudeSonnet4_5 BetaManagedAgentsModel = "claude-sonnet-4-5"`

          High-performance model for agents and coding

        - `const BetaManagedAgentsModelClaudeSonnet4_5_20250929 BetaManagedAgentsModel = "claude-sonnet-4-5-20250929"`

          High-performance model for agents and coding

      - `string`

    - `Effort BetaManagedAgentsModelConfigEffortUnion Optional`

      How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

      - `type BetaManagedAgentsEffortLow struct{…}`

        Low effort. Favors latency over reasoning depth.

        - `Type BetaManagedAgentsEffortLowType`

      - `type BetaManagedAgentsEffortMedium struct{…}`

        Medium effort. Balances latency and reasoning depth.

        - `Type BetaManagedAgentsEffortMediumType`

      - `type BetaManagedAgentsEffortHigh struct{…}`

        High effort. Favors reasoning depth.

        - `Type BetaManagedAgentsEffortHighType`

      - `type BetaManagedAgentsEffortXhigh struct{…}`

        Extra-high effort. Not all models accept this level.

        - `Type BetaManagedAgentsEffortXhighType`

      - `type BetaManagedAgentsEffortMax struct{…}`

        Maximum effort. Favors reasoning depth over latency.

        - `Type BetaManagedAgentsEffortMaxType`

    - `InferenceGeo string Optional`

      Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

    - `Speed BetaManagedAgentsModelConfigSpeed Optional`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `const BetaManagedAgentsModelConfigSpeedStandard BetaManagedAgentsModelConfigSpeed = "standard"`

      - `const BetaManagedAgentsModelConfigSpeedFast BetaManagedAgentsModelConfigSpeed = "fast"`

  - `Multiagent BetaManagedAgentsSessionMultiagentCoordinator`

    Resolved coordinator topology with full agent definitions for each roster member.

    - `Agents []BetaManagedAgentsSessionMultiagentCoordinatorAgentUnion`

      Full `agent` definitions the coordinator may spawn as session threads.

      - `type BetaManagedAgentsSessionThreadAgent struct{…}`

        Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

        - `ID string`

        - `Description string`

        - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

          - `Name string`

          - `Type BetaManagedAgentsMCPServerURLDefinitionType`

          - `URL string`

        - `Model BetaManagedAgentsModelConfig`

          Model identifier and configuration.

        - `Name string`

        - `Skills []BetaManagedAgentsSessionThreadAgentSkillUnion`

          - `type BetaManagedAgentsAnthropicSkill struct{…}`

            A resolved Anthropic-managed skill.

            - `SkillID string`

            - `Type BetaManagedAgentsAnthropicSkillType`

            - `Version string`

          - `type BetaManagedAgentsCustomSkill struct{…}`

            A resolved user-created custom skill.

            - `SkillID string`

            - `Type BetaManagedAgentsCustomSkillType`

            - `Version string`

        - `System string`

        - `Tools []BetaManagedAgentsSessionThreadAgentToolUnion`

          - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

            - `Configs []BetaManagedAgentsAgentToolConfigUnion`

              - `type BetaManagedAgentsBashToolConfig struct{…}`

                Configuration for the bash tool.

                - `Enabled bool`

                - `Name Bash`

                - `PermissionPolicy BetaManagedAgentsBashToolConfigPermissionPolicyUnion`

                  Permission policy for tool execution.

                  - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                    Tool calls are automatically approved without user confirmation.

                    - `Type BetaManagedAgentsAlwaysAllowPolicyType`

                  - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                    Tool calls require user confirmation before execution.

                    - `Type BetaManagedAgentsAlwaysAskPolicyType`

                - `Type Bash`

              - `type BetaManagedAgentsEditToolConfig struct{…}`

                Configuration for the edit tool.

                - `Enabled bool`

                - `Name Edit`

                - `PermissionPolicy BetaManagedAgentsEditToolConfigPermissionPolicyUnion`

                  Permission policy for tool execution.

                  - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                    Tool calls are automatically approved without user confirmation.

                  - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                    Tool calls require user confirmation before execution.

                - `Type Edit`

              - `type BetaManagedAgentsReadToolConfig struct{…}`

                Configuration for the read tool.

                - `Enabled bool`

                - `Name Read`

                - `PermissionPolicy BetaManagedAgentsReadToolConfigPermissionPolicyUnion`

                  Permission policy for tool execution.

                  - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                    Tool calls are automatically approved without user confirmation.

                  - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                    Tool calls require user confirmation before execution.

                - `Type Read`

              - `type BetaManagedAgentsWriteToolConfig struct{…}`

                Configuration for the write tool.

                - `Enabled bool`

                - `Name Write`

                - `PermissionPolicy BetaManagedAgentsWriteToolConfigPermissionPolicyUnion`

                  Permission policy for tool execution.

                  - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                    Tool calls are automatically approved without user confirmation.

                  - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                    Tool calls require user confirmation before execution.

                - `Type Write`

              - `type BetaManagedAgentsGlobToolConfig struct{…}`

                Configuration for the glob tool.

                - `Enabled bool`

                - `Name Glob`

                - `PermissionPolicy BetaManagedAgentsGlobToolConfigPermissionPolicyUnion`

                  Permission policy for tool execution.

                  - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                    Tool calls are automatically approved without user confirmation.

                  - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                    Tool calls require user confirmation before execution.

                - `Type Glob`

              - `type BetaManagedAgentsGrepToolConfig struct{…}`

                Configuration for the grep tool.

                - `Enabled bool`

                - `Name Grep`

                - `PermissionPolicy BetaManagedAgentsGrepToolConfigPermissionPolicyUnion`

                  Permission policy for tool execution.

                  - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                    Tool calls are automatically approved without user confirmation.

                  - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                    Tool calls require user confirmation before execution.

                - `Type Grep`

              - `type BetaManagedAgentsWebFetchToolConfig struct{…}`

                Configuration for the web_fetch tool.

                - `Enabled bool`

                - `Name WebFetch`

                - `PermissionPolicy BetaManagedAgentsWebFetchToolConfigPermissionPolicyUnion`

                  Permission policy for tool execution.

                  - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                    Tool calls are automatically approved without user confirmation.

                  - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                    Tool calls require user confirmation before execution.

                - `Type WebFetch`

                - `AllowedDomains []string Optional`

                - `BlockedDomains []string Optional`

                - `MaxContentTokens int64 Optional`

                  format: int32

              - `type BetaManagedAgentsWebSearchToolConfig struct{…}`

                Configuration for the web_search tool.

                - `Enabled bool`

                - `Name WebSearch`

                - `PermissionPolicy BetaManagedAgentsWebSearchToolConfigPermissionPolicyUnion`

                  Permission policy for tool execution.

                  - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                    Tool calls are automatically approved without user confirmation.

                  - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                    Tool calls require user confirmation before execution.

                - `Type WebSearch`

                - `AllowedDomains []string Optional`

                - `BlockedDomains []string Optional`

                - `UserLocation BetaManagedAgentsUserLocation Optional`

                  Approximate user location for search result localization.

                  - `Type Approximate`

                    Location precision. Only "approximate" is supported.

                  - `City string Optional`

                    City name.

                    minLength: 1, maxLength: 255

                  - `Country string Optional`

                    Two-letter ISO 3166-1 country code, uppercase.

                  - `Region string Optional`

                    Region or state name.

                    minLength: 1, maxLength: 255

                  - `Timezone string Optional`

                    IANA timezone identifier, e.g. "America/Los_Angeles".

                    minLength: 1, maxLength: 255

            - `DefaultConfig BetaManagedAgentsAgentToolsetDefaultConfig`

              Resolved default configuration for agent tools.

              - `Enabled bool`

              - `PermissionPolicy BetaManagedAgentsAgentToolsetDefaultConfigPermissionPolicyUnion`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

            - `Type BetaManagedAgentsAgentToolset20260401Type`

          - `type BetaManagedAgentsMCPToolset struct{…}`

            - `Configs []BetaManagedAgentsMCPToolConfig`

              - `Enabled bool`

              - `Name string`

              - `PermissionPolicy BetaManagedAgentsMCPToolConfigPermissionPolicyUnion`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

            - `DefaultConfig BetaManagedAgentsMCPToolsetDefaultConfig`

              Resolved default configuration for all tools from an MCP server.

              - `Enabled bool`

              - `PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigPermissionPolicyUnion`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

            - `MCPServerName string`

            - `Type BetaManagedAgentsMCPToolsetType`

          - `type BetaManagedAgentsCustomTool struct{…}`

            A custom tool as returned in API responses.

            - `Description string`

            - `InputSchema BetaManagedAgentsCustomToolInputSchema`

              JSON Schema for custom tool input parameters.

              - `Type Object`

              - `Properties map[string, any] Optional`

              - `Required []string Optional`

            - `Name string`

            - `Type BetaManagedAgentsCustomToolType`

        - `Type BetaManagedAgentsSessionThreadAgentType`

        - `Version int64`

          format: int32

      - `type BetaManagedAgentsAdvisor struct{…}`

        Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

        - `Model string`

          The advisor model id.

        - `Type BetaManagedAgentsAdvisorType`

    - `Type BetaManagedAgentsSessionMultiagentCoordinatorType`

  - `Name string`

  - `Skills []BetaManagedAgentsSessionAgentSkillUnion`

    - `type BetaManagedAgentsAnthropicSkill struct{…}`

      A resolved Anthropic-managed skill.

    - `type BetaManagedAgentsCustomSkill struct{…}`

      A resolved user-created custom skill.

  - `System string`

  - `Tools []BetaManagedAgentsSessionAgentToolUnion`

    - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

    - `type BetaManagedAgentsMCPToolset struct{…}`

    - `type BetaManagedAgentsCustomTool struct{…}`

      A custom tool as returned in API responses.

  - `Type BetaManagedAgentsSessionAgentType`

  - `Version int64`

    format: int32

### Beta Managed Agents Session Agent Update

- `type BetaManagedAgentsSessionAgentUpdate struct{…}`

  Mid-session agent configuration update. Only `tools` and `mcp_servers` are updatable. Full replacement: the provided array becomes the new value. To preserve existing entries, GET the session, modify the array, and POST it back.

  - `MCPServers []BetaManagedAgentsURLMCPServerParamsResp Optional`

    Replacement MCP server list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.

    - `Name string`

      Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

      minLength: 1, maxLength: 255

    - `Type BetaManagedAgentsURLMCPServerParamsType`

    - `URL string`

      Endpoint URL for the MCP server.

      maxLength: 2048

  - `Tools []BetaManagedAgentsSessionAgentUpdateToolUnion Optional`

    Replacement tool list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.

    - `type BetaManagedAgentsAgentToolset20260401ParamsResp struct{…}`

      Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

      - `Type BetaManagedAgentsAgentToolset20260401ParamsType`

      - `Configs []BetaManagedAgentsAgentToolConfigParamsUnionResp Optional`

        Per-tool configuration overrides.

        - `type BetaManagedAgentsBashToolConfigParamsResp struct{…}`

          Configuration override for the bash tool.

          - `Name Bash`

            Must be "bash".

          - `Enabled bool Optional`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy BetaManagedAgentsBashToolConfigParamsPermissionPolicyUnionResp Optional`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

              - `Type BetaManagedAgentsAlwaysAllowPolicyType`

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

              - `Type BetaManagedAgentsAlwaysAskPolicyType`

          - `Type BetaManagedAgentsBashToolConfigParamsType Optional`

        - `type BetaManagedAgentsEditToolConfigParamsResp struct{…}`

          Configuration override for the edit tool.

          - `Name Edit`

            Must be "edit".

          - `Enabled bool Optional`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy BetaManagedAgentsEditToolConfigParamsPermissionPolicyUnionResp Optional`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type BetaManagedAgentsEditToolConfigParamsType Optional`

        - `type BetaManagedAgentsReadToolConfigParamsResp struct{…}`

          Configuration override for the read tool.

          - `Name Read`

            Must be "read".

          - `Enabled bool Optional`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy BetaManagedAgentsReadToolConfigParamsPermissionPolicyUnionResp Optional`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type BetaManagedAgentsReadToolConfigParamsType Optional`

        - `type BetaManagedAgentsWriteToolConfigParamsResp struct{…}`

          Configuration override for the write tool.

          - `Name Write`

            Must be "write".

          - `Enabled bool Optional`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy BetaManagedAgentsWriteToolConfigParamsPermissionPolicyUnionResp Optional`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type BetaManagedAgentsWriteToolConfigParamsType Optional`

        - `type BetaManagedAgentsGlobToolConfigParamsResp struct{…}`

          Configuration override for the glob tool.

          - `Name Glob`

            Must be "glob".

          - `Enabled bool Optional`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy BetaManagedAgentsGlobToolConfigParamsPermissionPolicyUnionResp Optional`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type BetaManagedAgentsGlobToolConfigParamsType Optional`

        - `type BetaManagedAgentsGrepToolConfigParamsResp struct{…}`

          Configuration override for the grep tool.

          - `Name Grep`

            Must be "grep".

          - `Enabled bool Optional`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy BetaManagedAgentsGrepToolConfigParamsPermissionPolicyUnionResp Optional`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type BetaManagedAgentsGrepToolConfigParamsType Optional`

        - `type BetaManagedAgentsWebFetchToolConfigParamsResp struct{…}`

          Configuration override for the web_fetch tool.

          - `Name WebFetch`

            Must be "web_fetch".

          - `AllowedDomains []string Optional`

            Only fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

          - `BlockedDomains []string Optional`

            Never fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

          - `Enabled bool Optional`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `MaxContentTokens int64 Optional`

            Maximum number of tokens of fetched text content to include in context per call. Does not apply to binary content such as PDFs.

            format: int32

          - `PermissionPolicy BetaManagedAgentsWebFetchToolConfigParamsPermissionPolicyUnionResp Optional`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type BetaManagedAgentsWebFetchToolConfigParamsType Optional`

        - `type BetaManagedAgentsWebSearchToolConfigParamsResp struct{…}`

          Configuration override for the web_search tool.

          - `Name WebSearch`

            Must be "web_search".

          - `AllowedDomains []string Optional`

            Only return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

          - `BlockedDomains []string Optional`

            Never return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

          - `Enabled bool Optional`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy BetaManagedAgentsWebSearchToolConfigParamsPermissionPolicyUnionResp Optional`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type BetaManagedAgentsWebSearchToolConfigParamsType Optional`

          - `UserLocation BetaManagedAgentsUserLocation Optional`

            Approximate user location for search result localization.

            - `Type Approximate`

              Location precision. Only "approximate" is supported.

            - `City string Optional`

              City name.

              minLength: 1, maxLength: 255

            - `Country string Optional`

              Two-letter ISO 3166-1 country code, uppercase.

            - `Region string Optional`

              Region or state name.

              minLength: 1, maxLength: 255

            - `Timezone string Optional`

              IANA timezone identifier, e.g. "America/Los_Angeles".

              minLength: 1, maxLength: 255

      - `DefaultConfig BetaManagedAgentsAgentToolsetDefaultConfigParamsResp Optional`

        Default configuration for all tools in a toolset.

        - `Enabled bool Optional`

          Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

        - `PermissionPolicy BetaManagedAgentsAgentToolsetDefaultConfigParamsPermissionPolicyUnionResp Optional`

          Permission policy for tool execution.

          - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

            Tool calls are automatically approved without user confirmation.

          - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

            Tool calls require user confirmation before execution.

    - `type BetaManagedAgentsMCPToolsetParamsResp struct{…}`

      Configuration for tools from an MCP server defined in `mcp_servers`.

      - `MCPServerName string`

        Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

        minLength: 1, maxLength: 255

      - `Type BetaManagedAgentsMCPToolsetParamsType`

      - `Configs []BetaManagedAgentsMCPToolConfigParamsResp Optional`

        Per-tool configuration overrides.

        - `Name string`

          Name of the MCP tool to configure. 1-128 characters.

          minLength: 1, maxLength: 128

        - `Enabled bool Optional`

          Whether this tool is enabled. Overrides the `default_config` setting.

        - `PermissionPolicy BetaManagedAgentsMCPToolConfigParamsPermissionPolicyUnionResp Optional`

          Permission policy for tool execution.

          - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

            Tool calls are automatically approved without user confirmation.

          - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

            Tool calls require user confirmation before execution.

      - `DefaultConfig BetaManagedAgentsMCPToolsetDefaultConfigParamsResp Optional`

        Default configuration for all tools from an MCP server.

        - `Enabled bool Optional`

          Whether tools are enabled by default. Defaults to true if not specified.

        - `PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigParamsPermissionPolicyUnionResp Optional`

          Permission policy for tool execution.

          - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

            Tool calls are automatically approved without user confirmation.

          - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

            Tool calls require user confirmation before execution.

    - `type BetaManagedAgentsCustomToolParamsResp struct{…}`

      A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

      - `Description string`

        Description of what the tool does, shown to the agent to help it decide when to use the tool.

        minLength: 1

      - `InputSchema BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `Type Object`

        - `Properties map[string, any] Optional`

        - `Required []string Optional`

      - `Name string`

        Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

        minLength: 1, maxLength: 128

      - `Type BetaManagedAgentsCustomToolParamsType`

### Beta Managed Agents Session Multiagent Coordinator

- `type BetaManagedAgentsSessionMultiagentCoordinator struct{…}`

  Resolved coordinator topology with full agent definitions for each roster member.

  - `Agents []BetaManagedAgentsSessionMultiagentCoordinatorAgentUnion`

    Full `agent` definitions the coordinator may spawn as session threads.

    - `type BetaManagedAgentsSessionThreadAgent struct{…}`

      Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

      - `ID string`

      - `Description string`

      - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

        - `Name string`

        - `Type BetaManagedAgentsMCPServerURLDefinitionType`

        - `URL string`

      - `Model BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `ID BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `type BetaManagedAgentsModel string`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `const BetaManagedAgentsModelClaudeSonnet5 BetaManagedAgentsModel = "claude-sonnet-5"`

              High-performance model for coding and agents

            - `const BetaManagedAgentsModelClaudeFable5 BetaManagedAgentsModel = "claude-fable-5"`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `const BetaManagedAgentsModelClaudeOpus5 BetaManagedAgentsModel = "claude-opus-5"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeOpus4_8 BetaManagedAgentsModel = "claude-opus-4-8"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeOpus4_7 BetaManagedAgentsModel = "claude-opus-4-7"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeOpus4_6 BetaManagedAgentsModel = "claude-opus-4-6"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeSonnet4_6 BetaManagedAgentsModel = "claude-sonnet-4-6"`

              Best combination of speed and intelligence

            - `const BetaManagedAgentsModelClaudeHaiku4_5 BetaManagedAgentsModel = "claude-haiku-4-5"`

              Fastest model with near-frontier intelligence

            - `const BetaManagedAgentsModelClaudeHaiku4_5_20251001 BetaManagedAgentsModel = "claude-haiku-4-5-20251001"`

              Fastest model with near-frontier intelligence

            - `const BetaManagedAgentsModelClaudeOpus4_5 BetaManagedAgentsModel = "claude-opus-4-5"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeOpus4_5_20251101 BetaManagedAgentsModel = "claude-opus-4-5-20251101"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeSonnet4_5 BetaManagedAgentsModel = "claude-sonnet-4-5"`

              High-performance model for agents and coding

            - `const BetaManagedAgentsModelClaudeSonnet4_5_20250929 BetaManagedAgentsModel = "claude-sonnet-4-5-20250929"`

              High-performance model for agents and coding

          - `string`

        - `Effort BetaManagedAgentsModelConfigEffortUnion Optional`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `type BetaManagedAgentsEffortLow struct{…}`

            Low effort. Favors latency over reasoning depth.

            - `Type BetaManagedAgentsEffortLowType`

          - `type BetaManagedAgentsEffortMedium struct{…}`

            Medium effort. Balances latency and reasoning depth.

            - `Type BetaManagedAgentsEffortMediumType`

          - `type BetaManagedAgentsEffortHigh struct{…}`

            High effort. Favors reasoning depth.

            - `Type BetaManagedAgentsEffortHighType`

          - `type BetaManagedAgentsEffortXhigh struct{…}`

            Extra-high effort. Not all models accept this level.

            - `Type BetaManagedAgentsEffortXhighType`

          - `type BetaManagedAgentsEffortMax struct{…}`

            Maximum effort. Favors reasoning depth over latency.

            - `Type BetaManagedAgentsEffortMaxType`

        - `InferenceGeo string Optional`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `Speed BetaManagedAgentsModelConfigSpeed Optional`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `const BetaManagedAgentsModelConfigSpeedStandard BetaManagedAgentsModelConfigSpeed = "standard"`

          - `const BetaManagedAgentsModelConfigSpeedFast BetaManagedAgentsModelConfigSpeed = "fast"`

      - `Name string`

      - `Skills []BetaManagedAgentsSessionThreadAgentSkillUnion`

        - `type BetaManagedAgentsAnthropicSkill struct{…}`

          A resolved Anthropic-managed skill.

          - `SkillID string`

          - `Type BetaManagedAgentsAnthropicSkillType`

          - `Version string`

        - `type BetaManagedAgentsCustomSkill struct{…}`

          A resolved user-created custom skill.

          - `SkillID string`

          - `Type BetaManagedAgentsCustomSkillType`

          - `Version string`

      - `System string`

      - `Tools []BetaManagedAgentsSessionThreadAgentToolUnion`

        - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

          - `Configs []BetaManagedAgentsAgentToolConfigUnion`

            - `type BetaManagedAgentsBashToolConfig struct{…}`

              Configuration for the bash tool.

              - `Enabled bool`

              - `Name Bash`

              - `PermissionPolicy BetaManagedAgentsBashToolConfigPermissionPolicyUnion`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                  - `Type BetaManagedAgentsAlwaysAllowPolicyType`

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

                  - `Type BetaManagedAgentsAlwaysAskPolicyType`

              - `Type Bash`

            - `type BetaManagedAgentsEditToolConfig struct{…}`

              Configuration for the edit tool.

              - `Enabled bool`

              - `Name Edit`

              - `PermissionPolicy BetaManagedAgentsEditToolConfigPermissionPolicyUnion`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

              - `Type Edit`

            - `type BetaManagedAgentsReadToolConfig struct{…}`

              Configuration for the read tool.

              - `Enabled bool`

              - `Name Read`

              - `PermissionPolicy BetaManagedAgentsReadToolConfigPermissionPolicyUnion`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

              - `Type Read`

            - `type BetaManagedAgentsWriteToolConfig struct{…}`

              Configuration for the write tool.

              - `Enabled bool`

              - `Name Write`

              - `PermissionPolicy BetaManagedAgentsWriteToolConfigPermissionPolicyUnion`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

              - `Type Write`

            - `type BetaManagedAgentsGlobToolConfig struct{…}`

              Configuration for the glob tool.

              - `Enabled bool`

              - `Name Glob`

              - `PermissionPolicy BetaManagedAgentsGlobToolConfigPermissionPolicyUnion`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

              - `Type Glob`

            - `type BetaManagedAgentsGrepToolConfig struct{…}`

              Configuration for the grep tool.

              - `Enabled bool`

              - `Name Grep`

              - `PermissionPolicy BetaManagedAgentsGrepToolConfigPermissionPolicyUnion`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

              - `Type Grep`

            - `type BetaManagedAgentsWebFetchToolConfig struct{…}`

              Configuration for the web_fetch tool.

              - `Enabled bool`

              - `Name WebFetch`

              - `PermissionPolicy BetaManagedAgentsWebFetchToolConfigPermissionPolicyUnion`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

              - `Type WebFetch`

              - `AllowedDomains []string Optional`

              - `BlockedDomains []string Optional`

              - `MaxContentTokens int64 Optional`

                format: int32

            - `type BetaManagedAgentsWebSearchToolConfig struct{…}`

              Configuration for the web_search tool.

              - `Enabled bool`

              - `Name WebSearch`

              - `PermissionPolicy BetaManagedAgentsWebSearchToolConfigPermissionPolicyUnion`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

              - `Type WebSearch`

              - `AllowedDomains []string Optional`

              - `BlockedDomains []string Optional`

              - `UserLocation BetaManagedAgentsUserLocation Optional`

                Approximate user location for search result localization.

                - `Type Approximate`

                  Location precision. Only "approximate" is supported.

                - `City string Optional`

                  City name.

                  minLength: 1, maxLength: 255

                - `Country string Optional`

                  Two-letter ISO 3166-1 country code, uppercase.

                - `Region string Optional`

                  Region or state name.

                  minLength: 1, maxLength: 255

                - `Timezone string Optional`

                  IANA timezone identifier, e.g. "America/Los_Angeles".

                  minLength: 1, maxLength: 255

          - `DefaultConfig BetaManagedAgentsAgentToolsetDefaultConfig`

            Resolved default configuration for agent tools.

            - `Enabled bool`

            - `PermissionPolicy BetaManagedAgentsAgentToolsetDefaultConfigPermissionPolicyUnion`

              Permission policy for tool execution.

              - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                Tool calls are automatically approved without user confirmation.

              - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                Tool calls require user confirmation before execution.

          - `Type BetaManagedAgentsAgentToolset20260401Type`

        - `type BetaManagedAgentsMCPToolset struct{…}`

          - `Configs []BetaManagedAgentsMCPToolConfig`

            - `Enabled bool`

            - `Name string`

            - `PermissionPolicy BetaManagedAgentsMCPToolConfigPermissionPolicyUnion`

              Permission policy for tool execution.

              - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                Tool calls are automatically approved without user confirmation.

              - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                Tool calls require user confirmation before execution.

          - `DefaultConfig BetaManagedAgentsMCPToolsetDefaultConfig`

            Resolved default configuration for all tools from an MCP server.

            - `Enabled bool`

            - `PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigPermissionPolicyUnion`

              Permission policy for tool execution.

              - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                Tool calls are automatically approved without user confirmation.

              - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                Tool calls require user confirmation before execution.

          - `MCPServerName string`

          - `Type BetaManagedAgentsMCPToolsetType`

        - `type BetaManagedAgentsCustomTool struct{…}`

          A custom tool as returned in API responses.

          - `Description string`

          - `InputSchema BetaManagedAgentsCustomToolInputSchema`

            JSON Schema for custom tool input parameters.

            - `Type Object`

            - `Properties map[string, any] Optional`

            - `Required []string Optional`

          - `Name string`

          - `Type BetaManagedAgentsCustomToolType`

      - `Type BetaManagedAgentsSessionThreadAgentType`

      - `Version int64`

        format: int32

    - `type BetaManagedAgentsAdvisor struct{…}`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `Model string`

        The advisor model id.

      - `Type BetaManagedAgentsAdvisorType`

  - `Type BetaManagedAgentsSessionMultiagentCoordinatorType`

### Beta Managed Agents Session Stats

- `type BetaManagedAgentsSessionStats struct{…}`

  Timing statistics for a session.

  - `ActiveSeconds float64 Optional`

    Cumulative time in seconds the session spent in running status. Excludes idle time.

    format: double

  - `DurationSeconds float64 Optional`

    Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

    format: double

### Beta Managed Agents Session Updated Event

- `type BetaManagedAgentsSessionUpdatedEvent struct{…}`

  Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

  - `ID string`

    Unique identifier for this event.

  - `ProcessedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `Type BetaManagedAgentsSessionUpdatedEventType`

  - `Agent BetaManagedAgentsSessionAgent Optional`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `ID string`

    - `Description string`

    - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

      - `Name string`

      - `Type BetaManagedAgentsMCPServerURLDefinitionType`

      - `URL string`

    - `Model BetaManagedAgentsModelConfig`

      Model identifier and configuration.

      - `ID BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `type BetaManagedAgentsModel string`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `const BetaManagedAgentsModelClaudeSonnet5 BetaManagedAgentsModel = "claude-sonnet-5"`

            High-performance model for coding and agents

          - `const BetaManagedAgentsModelClaudeFable5 BetaManagedAgentsModel = "claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `const BetaManagedAgentsModelClaudeOpus5 BetaManagedAgentsModel = "claude-opus-5"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeOpus4_8 BetaManagedAgentsModel = "claude-opus-4-8"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeOpus4_7 BetaManagedAgentsModel = "claude-opus-4-7"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeOpus4_6 BetaManagedAgentsModel = "claude-opus-4-6"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeSonnet4_6 BetaManagedAgentsModel = "claude-sonnet-4-6"`

            Best combination of speed and intelligence

          - `const BetaManagedAgentsModelClaudeHaiku4_5 BetaManagedAgentsModel = "claude-haiku-4-5"`

            Fastest model with near-frontier intelligence

          - `const BetaManagedAgentsModelClaudeHaiku4_5_20251001 BetaManagedAgentsModel = "claude-haiku-4-5-20251001"`

            Fastest model with near-frontier intelligence

          - `const BetaManagedAgentsModelClaudeOpus4_5 BetaManagedAgentsModel = "claude-opus-4-5"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeOpus4_5_20251101 BetaManagedAgentsModel = "claude-opus-4-5-20251101"`

            Powerful intelligence for long-running agents and coding

          - `const BetaManagedAgentsModelClaudeSonnet4_5 BetaManagedAgentsModel = "claude-sonnet-4-5"`

            High-performance model for agents and coding

          - `const BetaManagedAgentsModelClaudeSonnet4_5_20250929 BetaManagedAgentsModel = "claude-sonnet-4-5-20250929"`

            High-performance model for agents and coding

        - `string`

      - `Effort BetaManagedAgentsModelConfigEffortUnion Optional`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

        - `type BetaManagedAgentsEffortLow struct{…}`

          Low effort. Favors latency over reasoning depth.

          - `Type BetaManagedAgentsEffortLowType`

        - `type BetaManagedAgentsEffortMedium struct{…}`

          Medium effort. Balances latency and reasoning depth.

          - `Type BetaManagedAgentsEffortMediumType`

        - `type BetaManagedAgentsEffortHigh struct{…}`

          High effort. Favors reasoning depth.

          - `Type BetaManagedAgentsEffortHighType`

        - `type BetaManagedAgentsEffortXhigh struct{…}`

          Extra-high effort. Not all models accept this level.

          - `Type BetaManagedAgentsEffortXhighType`

        - `type BetaManagedAgentsEffortMax struct{…}`

          Maximum effort. Favors reasoning depth over latency.

          - `Type BetaManagedAgentsEffortMaxType`

      - `InferenceGeo string Optional`

        Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

      - `Speed BetaManagedAgentsModelConfigSpeed Optional`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `const BetaManagedAgentsModelConfigSpeedStandard BetaManagedAgentsModelConfigSpeed = "standard"`

        - `const BetaManagedAgentsModelConfigSpeedFast BetaManagedAgentsModelConfigSpeed = "fast"`

    - `Multiagent BetaManagedAgentsSessionMultiagentCoordinator`

      Resolved coordinator topology with full agent definitions for each roster member.

      - `Agents []BetaManagedAgentsSessionMultiagentCoordinatorAgentUnion`

        Full `agent` definitions the coordinator may spawn as session threads.

        - `type BetaManagedAgentsSessionThreadAgent struct{…}`

          Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

          - `ID string`

          - `Description string`

          - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

            - `Name string`

            - `Type BetaManagedAgentsMCPServerURLDefinitionType`

            - `URL string`

          - `Model BetaManagedAgentsModelConfig`

            Model identifier and configuration.

          - `Name string`

          - `Skills []BetaManagedAgentsSessionThreadAgentSkillUnion`

            - `type BetaManagedAgentsAnthropicSkill struct{…}`

              A resolved Anthropic-managed skill.

              - `SkillID string`

              - `Type BetaManagedAgentsAnthropicSkillType`

              - `Version string`

            - `type BetaManagedAgentsCustomSkill struct{…}`

              A resolved user-created custom skill.

              - `SkillID string`

              - `Type BetaManagedAgentsCustomSkillType`

              - `Version string`

          - `System string`

          - `Tools []BetaManagedAgentsSessionThreadAgentToolUnion`

            - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

              - `Configs []BetaManagedAgentsAgentToolConfigUnion`

                - `type BetaManagedAgentsBashToolConfig struct{…}`

                  Configuration for the bash tool.

                  - `Enabled bool`

                  - `Name Bash`

                  - `PermissionPolicy BetaManagedAgentsBashToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                      - `Type BetaManagedAgentsAlwaysAllowPolicyType`

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                      - `Type BetaManagedAgentsAlwaysAskPolicyType`

                  - `Type Bash`

                - `type BetaManagedAgentsEditToolConfig struct{…}`

                  Configuration for the edit tool.

                  - `Enabled bool`

                  - `Name Edit`

                  - `PermissionPolicy BetaManagedAgentsEditToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type Edit`

                - `type BetaManagedAgentsReadToolConfig struct{…}`

                  Configuration for the read tool.

                  - `Enabled bool`

                  - `Name Read`

                  - `PermissionPolicy BetaManagedAgentsReadToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type Read`

                - `type BetaManagedAgentsWriteToolConfig struct{…}`

                  Configuration for the write tool.

                  - `Enabled bool`

                  - `Name Write`

                  - `PermissionPolicy BetaManagedAgentsWriteToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type Write`

                - `type BetaManagedAgentsGlobToolConfig struct{…}`

                  Configuration for the glob tool.

                  - `Enabled bool`

                  - `Name Glob`

                  - `PermissionPolicy BetaManagedAgentsGlobToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type Glob`

                - `type BetaManagedAgentsGrepToolConfig struct{…}`

                  Configuration for the grep tool.

                  - `Enabled bool`

                  - `Name Grep`

                  - `PermissionPolicy BetaManagedAgentsGrepToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type Grep`

                - `type BetaManagedAgentsWebFetchToolConfig struct{…}`

                  Configuration for the web_fetch tool.

                  - `Enabled bool`

                  - `Name WebFetch`

                  - `PermissionPolicy BetaManagedAgentsWebFetchToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type WebFetch`

                  - `AllowedDomains []string Optional`

                  - `BlockedDomains []string Optional`

                  - `MaxContentTokens int64 Optional`

                    format: int32

                - `type BetaManagedAgentsWebSearchToolConfig struct{…}`

                  Configuration for the web_search tool.

                  - `Enabled bool`

                  - `Name WebSearch`

                  - `PermissionPolicy BetaManagedAgentsWebSearchToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                  - `Type WebSearch`

                  - `AllowedDomains []string Optional`

                  - `BlockedDomains []string Optional`

                  - `UserLocation BetaManagedAgentsUserLocation Optional`

                    Approximate user location for search result localization.

                    - `Type Approximate`

                      Location precision. Only "approximate" is supported.

                    - `City string Optional`

                      City name.

                      minLength: 1, maxLength: 255

                    - `Country string Optional`

                      Two-letter ISO 3166-1 country code, uppercase.

                    - `Region string Optional`

                      Region or state name.

                      minLength: 1, maxLength: 255

                    - `Timezone string Optional`

                      IANA timezone identifier, e.g. "America/Los_Angeles".

                      minLength: 1, maxLength: 255

              - `DefaultConfig BetaManagedAgentsAgentToolsetDefaultConfig`

                Resolved default configuration for agent tools.

                - `Enabled bool`

                - `PermissionPolicy BetaManagedAgentsAgentToolsetDefaultConfigPermissionPolicyUnion`

                  Permission policy for tool execution.

                  - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                    Tool calls are automatically approved without user confirmation.

                  - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                    Tool calls require user confirmation before execution.

              - `Type BetaManagedAgentsAgentToolset20260401Type`

            - `type BetaManagedAgentsMCPToolset struct{…}`

              - `Configs []BetaManagedAgentsMCPToolConfig`

                - `Enabled bool`

                - `Name string`

                - `PermissionPolicy BetaManagedAgentsMCPToolConfigPermissionPolicyUnion`

                  Permission policy for tool execution.

                  - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                    Tool calls are automatically approved without user confirmation.

                  - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                    Tool calls require user confirmation before execution.

              - `DefaultConfig BetaManagedAgentsMCPToolsetDefaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `Enabled bool`

                - `PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigPermissionPolicyUnion`

                  Permission policy for tool execution.

                  - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                    Tool calls are automatically approved without user confirmation.

                  - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                    Tool calls require user confirmation before execution.

              - `MCPServerName string`

              - `Type BetaManagedAgentsMCPToolsetType`

            - `type BetaManagedAgentsCustomTool struct{…}`

              A custom tool as returned in API responses.

              - `Description string`

              - `InputSchema BetaManagedAgentsCustomToolInputSchema`

                JSON Schema for custom tool input parameters.

                - `Type Object`

                - `Properties map[string, any] Optional`

                - `Required []string Optional`

              - `Name string`

              - `Type BetaManagedAgentsCustomToolType`

          - `Type BetaManagedAgentsSessionThreadAgentType`

          - `Version int64`

            format: int32

        - `type BetaManagedAgentsAdvisor struct{…}`

          Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

          - `Model string`

            The advisor model id.

          - `Type BetaManagedAgentsAdvisorType`

      - `Type BetaManagedAgentsSessionMultiagentCoordinatorType`

    - `Name string`

    - `Skills []BetaManagedAgentsSessionAgentSkillUnion`

      - `type BetaManagedAgentsAnthropicSkill struct{…}`

        A resolved Anthropic-managed skill.

      - `type BetaManagedAgentsCustomSkill struct{…}`

        A resolved user-created custom skill.

    - `System string`

    - `Tools []BetaManagedAgentsSessionAgentToolUnion`

      - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

      - `type BetaManagedAgentsMCPToolset struct{…}`

      - `type BetaManagedAgentsCustomTool struct{…}`

        A custom tool as returned in API responses.

    - `Type BetaManagedAgentsSessionAgentType`

    - `Version int64`

      format: int32

  - `Budget BetaManagedAgentsBudgetLimit Optional`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `MaxListCost BetaMonetaryAmount`

      A monetary amount in a specific currency.

      - `Amount string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `Currency BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `Type BetaManagedAgentsBudgetLimitType`

  - `Metadata map[string, string] Optional`

    The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

  - `Title string Optional`

    The session's new title. Present only when the update changed it.

### Beta Managed Agents Session Usage

- `type BetaManagedAgentsSessionUsage struct{…}`

  Cumulative token usage for a session across all turns.

  - `ActiveSeconds float64 Optional`

    Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once, unlike `stats.active_seconds`, which sums each thread's own active time. This is the duration the session's runtime cost is priced on.

    format: double

  - `CacheCreation BetaManagedAgentsCacheCreationUsage Optional`

    Prompt-cache creation token usage broken down by cache lifetime.

    - `Ephemeral1hInputTokens int64 Optional`

      Tokens used to create 1-hour ephemeral cache entries.

      format: int32

    - `Ephemeral5mInputTokens int64 Optional`

      Tokens used to create 5-minute ephemeral cache entries.

      format: int32

  - `CacheReadInputTokens int64 Optional`

    Total tokens read from prompt cache.

    format: int32

  - `InputTokens int64 Optional`

    Total input tokens consumed across all turns.

    format: int32

  - `ListCost BetaMonetaryAmount Optional`

    A monetary amount in a specific currency.

    - `Amount string`

      Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

    - `Currency BetaCurrency`

      Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

  - `OutputTokens int64 Optional`

    Total output tokens generated across all turns.

    format: int32

  - `ServerToolUse BetaManagedAgentsServerToolUsage Optional`

    Cumulative count of server-executed tool invocations, broken down by tool.

    - `WebFetchRequests int64 Optional`

      Number of server-executed web fetch requests.

      format: int32

    - `WebSearchRequests int64 Optional`

      Number of server-executed web search requests.

      format: int32

### Beta Managed Agents Session Usage Event

- `type BetaManagedAgentsSessionUsageEvent struct{…}`

  Periodic snapshot of the session's cumulative usage and tracked list cost.

  - `ID string`

    Unique identifier for this event.

  - `ProcessedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `Type BetaManagedAgentsSessionUsageEventType`

  - `Usage BetaManagedAgentsSessionUsageSnapshot`

    Point-in-time snapshot of a session's cumulative usage.

    - `ActiveSeconds float64 Optional`

      Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

      format: double

    - `CacheCreation BetaManagedAgentsCacheCreationUsage Optional`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `Ephemeral1hInputTokens int64 Optional`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `Ephemeral5mInputTokens int64 Optional`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `CacheReadInputTokens int64 Optional`

      Total tokens read from prompt cache.

      format: int32

    - `InputTokens int64 Optional`

      Total input tokens consumed across all turns.

      format: int32

    - `ListCost BetaMonetaryAmount Optional`

      A monetary amount in a specific currency.

      - `Amount string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `Currency BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `OutputTokens int64 Optional`

      Total output tokens generated across all turns.

      format: int32

    - `ServerToolUse BetaManagedAgentsServerToolUsage Optional`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `WebFetchRequests int64 Optional`

        Number of server-executed web fetch requests.

        format: int32

      - `WebSearchRequests int64 Optional`

        Number of server-executed web search requests.

        format: int32

  - `Budget BetaManagedAgentsBudgetLimit Optional`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `MaxListCost BetaMonetaryAmount`

      A monetary amount in a specific currency.

    - `Type BetaManagedAgentsBudgetLimitType`

### Beta Managed Agents Start Event

- `type BetaManagedAgentsStartEvent struct{…}`

  Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

  - `Event BetaManagedAgentsStartEventPreviewUnion`

    The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

    - `type BetaManagedAgentsAgentMessagePreview struct{…}`

      - `ID string`

        The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

      - `Type BetaManagedAgentsAgentMessagePreviewType`

    - `type BetaManagedAgentsAgentThinkingPreview struct{…}`

      - `ID string`

        The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

      - `Type BetaManagedAgentsAgentThinkingPreviewType`

  - `Type BetaManagedAgentsStartEventType`

### Beta Managed Agents Start Event Preview

- `type BetaManagedAgentsStartEventPreviewUnion interface{…}`

  - `type BetaManagedAgentsAgentMessagePreview struct{…}`

    - `ID string`

      The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

    - `Type BetaManagedAgentsAgentMessagePreviewType`

  - `type BetaManagedAgentsAgentThinkingPreview struct{…}`

    - `ID string`

      The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

    - `Type BetaManagedAgentsAgentThinkingPreviewType`

### Beta Managed Agents System Content Block

- `type BetaManagedAgentsSystemContentBlock struct{…}`

  Regular text content.

  - `Text string`

    The text content.

    minLength: 1

  - `Type BetaManagedAgentsSystemContentBlockType`

### Beta Managed Agents System Message Event

- `type BetaManagedAgentsSystemMessageEvent struct{…}`

  A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

  - `ID string`

    Unique identifier for this event.

  - `Content []BetaManagedAgentsSystemContentBlock`

    System content blocks. Text-only.

    - `Text string`

      The text content.

      minLength: 1

    - `Type BetaManagedAgentsSystemContentBlockType`

  - `Type BetaManagedAgentsSystemMessageEventType`

  - `ProcessedAt Time Optional`

    A timestamp in RFC 3339 format

    format: date-time

### Beta Managed Agents User Tool Result Event

- `type BetaManagedAgentsUserToolResultEvent struct{…}`

  Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

  - `ID string`

    Unique identifier for this event.

  - `ToolUseID string`

    The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `Type BetaManagedAgentsUserToolResultEventType`

  - `Content []BetaManagedAgentsUserToolResultEventContentUnion Optional`

    The result content returned by the tool.

    - `type BetaManagedAgentsTextBlock struct{…}`

      Regular text content.

      - `Text string`

        The text content.

        minLength: 1

      - `Type BetaManagedAgentsTextBlockType`

    - `type BetaManagedAgentsImageBlock struct{…}`

      Image content specified directly as base64 data or as a reference via a URL.

      - `Source BetaManagedAgentsImageBlockSourceUnion`

        Union type for image source variants.

        - `type BetaManagedAgentsBase64ImageSource struct{…}`

          Base64-encoded image data.

          - `Data string`

            Base64-encoded image data.

            minLength: 1

          - `MediaType string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            minLength: 1

          - `Type BetaManagedAgentsBase64ImageSourceType`

        - `type BetaManagedAgentsURLImageSource struct{…}`

          Image referenced by URL.

          - `Type BetaManagedAgentsURLImageSourceType`

          - `URL string`

            URL of the image to fetch.

            minLength: 1

        - `type BetaManagedAgentsFileImageSource struct{…}`

          Image referenced by file ID.

          - `FileID string`

            ID of a previously uploaded file.

            minLength: 1

          - `Type BetaManagedAgentsFileImageSourceType`

      - `Type BetaManagedAgentsImageBlockType`

    - `type BetaManagedAgentsDocumentBlock struct{…}`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `Source BetaManagedAgentsDocumentBlockSourceUnion`

        Union type for document source variants.

        - `type BetaManagedAgentsBase64DocumentSource struct{…}`

          Base64-encoded document data.

          - `Data string`

            Base64-encoded document data.

            minLength: 1

          - `MediaType string`

            MIME type of the document (e.g., "application/pdf").

            minLength: 1

          - `Type BetaManagedAgentsBase64DocumentSourceType`

        - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

          Plain text document content.

          - `Data string`

            The plain text content.

            minLength: 1

          - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

            MIME type of the text content. Must be "text/plain".

          - `Type BetaManagedAgentsPlainTextDocumentSourceType`

        - `type BetaManagedAgentsURLDocumentSource struct{…}`

          Document referenced by URL.

          - `Type BetaManagedAgentsURLDocumentSourceType`

          - `URL string`

            URL of the document to fetch.

            minLength: 1

        - `type BetaManagedAgentsFileDocumentSource struct{…}`

          Document referenced by file ID.

          - `FileID string`

            ID of a previously uploaded file.

            minLength: 1

          - `Type BetaManagedAgentsFileDocumentSourceType`

      - `Type BetaManagedAgentsDocumentBlockType`

      - `Context string Optional`

        Additional context about the document for the model.

      - `Title string Optional`

        The title of the document.

    - `type BetaManagedAgentsSearchResultBlock struct{…}`

      A block containing a web search result.

      - `Citations BetaManagedAgentsSearchResultCitations`

        Citation settings for a search result.

        - `Enabled bool`

          Whether citations are enabled for this search result.

      - `Content []BetaManagedAgentsSearchResultContent`

        Array of text content blocks from the search result.

        - `Text string`

          The text content.

          minLength: 1

        - `Type BetaManagedAgentsSearchResultContentType`

      - `Source string`

        The URL source of the search result.

        minLength: 1

      - `Title string`

        The title of the search result.

        minLength: 1

      - `Type BetaManagedAgentsSearchResultBlockType`

  - `IsError bool Optional`

    Whether the tool execution resulted in an error.

  - `ProcessedAt Time Optional`

    A timestamp in RFC 3339 format

    format: date-time

  - `SessionThreadID string Optional`

    Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

## Sessions › Events

### List Events

`client.Beta.Sessions.Events.List(ctx, sessionID, params) (*PageCursor[BetaManagedAgentsSessionEventUnion], error)`

**GET** `/v1/sessions/{session_id}/events`

List Events

#### Parameters

- `sessionID string`

- `params BetaSessionEventListParams`

  - `CreatedAtGt param.Field[Time] Optional`

    Query param: Return events created after this time (exclusive). Compared against the event's `processed_at` value.

    format: date-time

  - `CreatedAtGte param.Field[Time] Optional`

    Query param: Return events created at or after this time (inclusive). Compared against the event's `processed_at` value.

    format: date-time

  - `CreatedAtLt param.Field[Time] Optional`

    Query param: Return events created before this time (exclusive). Compared against the event's `processed_at` value.

    format: date-time

  - `CreatedAtLte param.Field[Time] Optional`

    Query param: Return events created at or before this time (inclusive). Compared against the event's `processed_at` value.

    format: date-time

  - `Limit param.Field[int64] Optional`

    Query param: Query parameter for limit

    format: int32

  - `Order param.Field[BetaSessionEventListParamsOrder] Optional`

    Query param: Sort direction for results, ordered by the event's `processed_at`. Defaults to asc (chronological).

    - `const BetaSessionEventListParamsOrderAsc BetaSessionEventListParamsOrder = "asc"`

    - `const BetaSessionEventListParamsOrderDesc BetaSessionEventListParamsOrder = "desc"`

  - `Page param.Field[string] Optional`

    Query param: Opaque pagination cursor from a previous response's next_page.

  - `Types param.Field[[]string] Optional`

    Query param: Filter by event type. Values match the `type` field on returned events (for example, `user.message` or `agent.tool_use`). Omit to return all event types.

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

#### Returns

- `type BetaManagedAgentsSessionEventUnion interface{…}`

  Union type for all event types in a session.

  - `type BetaManagedAgentsUserMessageEvent struct{…}`

    A user message event in the session conversation.

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsUserMessageEventContentUnion`

      Array of content blocks comprising the user message.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

        - `Text string`

          The text content.

          minLength: 1

        - `Type BetaManagedAgentsTextBlockType`

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source BetaManagedAgentsImageBlockSourceUnion`

          Union type for image source variants.

          - `type BetaManagedAgentsBase64ImageSource struct{…}`

            Base64-encoded image data.

            - `Data string`

              Base64-encoded image data.

              minLength: 1

            - `MediaType string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

            - `Type BetaManagedAgentsBase64ImageSourceType`

          - `type BetaManagedAgentsURLImageSource struct{…}`

            Image referenced by URL.

            - `Type BetaManagedAgentsURLImageSourceType`

            - `URL string`

              URL of the image to fetch.

              minLength: 1

          - `type BetaManagedAgentsFileImageSource struct{…}`

            Image referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

              minLength: 1

            - `Type BetaManagedAgentsFileImageSourceType`

        - `Type BetaManagedAgentsImageBlockType`

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source BetaManagedAgentsDocumentBlockSourceUnion`

          Union type for document source variants.

          - `type BetaManagedAgentsBase64DocumentSource struct{…}`

            Base64-encoded document data.

            - `Data string`

              Base64-encoded document data.

              minLength: 1

            - `MediaType string`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

            - `Type BetaManagedAgentsBase64DocumentSourceType`

          - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

            Plain text document content.

            - `Data string`

              The plain text content.

              minLength: 1

            - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

              MIME type of the text content. Must be "text/plain".

            - `Type BetaManagedAgentsPlainTextDocumentSourceType`

          - `type BetaManagedAgentsURLDocumentSource struct{…}`

            Document referenced by URL.

            - `Type BetaManagedAgentsURLDocumentSourceType`

            - `URL string`

              URL of the document to fetch.

              minLength: 1

          - `type BetaManagedAgentsFileDocumentSource struct{…}`

            Document referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

              minLength: 1

            - `Type BetaManagedAgentsFileDocumentSourceType`

        - `Type BetaManagedAgentsDocumentBlockType`

        - `Context string Optional`

          Additional context about the document for the model.

        - `Title string Optional`

          The title of the document.

      - `type BetaManagedAgentsRedactedBlockParam struct{…}`

        Placeholder for content withheld by Anthropic model policy.

        - `Type BetaManagedAgentsRedactedBlockType`

    - `Type BetaManagedAgentsUserMessageEventType`

    - `ProcessedAt Time Optional`

      A timestamp in RFC 3339 format

      format: date-time

  - `type BetaManagedAgentsUserInterruptEvent struct{…}`

    An interrupt event that pauses agent execution and returns control to the user.

    - `ID string`

      Unique identifier for this event.

    - `Type BetaManagedAgentsUserInterruptEventType`

    - `ProcessedAt Time Optional`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string Optional`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `type BetaManagedAgentsUserToolConfirmationEvent struct{…}`

    A tool confirmation event that approves or denies a pending tool execution.

    - `ID string`

      Unique identifier for this event.

    - `Result BetaManagedAgentsUserToolConfirmationEventResult`

      UserToolConfirmationResult enum

      - `const BetaManagedAgentsUserToolConfirmationEventResultAllow BetaManagedAgentsUserToolConfirmationEventResult = "allow"`

      - `const BetaManagedAgentsUserToolConfirmationEventResultDeny BetaManagedAgentsUserToolConfirmationEventResult = "deny"`

    - `ToolUseID string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type BetaManagedAgentsUserToolConfirmationEventType`

    - `DenyMessage string Optional`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `ProcessedAt Time Optional`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string Optional`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `type BetaManagedAgentsUserCustomToolResultEvent struct{…}`

    Event sent by the client providing the result of a custom tool execution.

    - `ID string`

      Unique identifier for this event.

    - `CustomToolUseID string`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type BetaManagedAgentsUserCustomToolResultEventType`

    - `Content []BetaManagedAgentsUserCustomToolResultEventContentUnion Optional`

      The result content returned by the tool.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `type BetaManagedAgentsSearchResultBlock struct{…}`

        A block containing a web search result.

        - `Citations BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `Enabled bool`

            Whether citations are enabled for this search result.

        - `Content []BetaManagedAgentsSearchResultContent`

          Array of text content blocks from the search result.

          - `Text string`

            The text content.

            minLength: 1

          - `Type BetaManagedAgentsSearchResultContentType`

        - `Source string`

          The URL source of the search result.

          minLength: 1

        - `Title string`

          The title of the search result.

          minLength: 1

        - `Type BetaManagedAgentsSearchResultBlockType`

    - `IsError bool Optional`

      Whether the tool execution resulted in an error.

    - `ProcessedAt Time Optional`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string Optional`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `type BetaManagedAgentsAgentCustomToolUseEvent struct{…}`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `ID string`

      Unique identifier for this event.

    - `Input map[string, any]`

      Input parameters for the tool call.

    - `Name string`

      Name of the custom tool being called.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsAgentCustomToolUseEventType`

    - `SessionThreadID string Optional`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `type BetaManagedAgentsAgentMessageEvent struct{…}`

    An agent response event in the session conversation.

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsAgentMessageEventContentUnion`

      Array of text blocks comprising the agent response.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

      - `type BetaManagedAgentsRedactedBlockParam struct{…}`

        Placeholder for content withheld by Anthropic model policy.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsAgentMessageEventType`

  - `type BetaManagedAgentsAgentThinkingEvent struct{…}`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsAgentThinkingEventType`

  - `type BetaManagedAgentsAgentMCPToolUseEvent struct{…}`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `ID string`

      Unique identifier for this event.

    - `Input map[string, any]`

      Input parameters for the tool call.

    - `MCPServerName string`

      Name of the MCP server providing the tool.

    - `Name string`

      Name of the MCP tool being used.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsAgentMCPToolUseEventType`

    - `EvaluatedPermission BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission Optional`

      AgentEvaluatedPermission enum

      - `const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionAllow BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "allow"`

      - `const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionAsk BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "ask"`

      - `const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionDeny BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "deny"`

    - `SessionThreadID string Optional`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `type BetaManagedAgentsAgentMCPToolResultEvent struct{…}`

    Event representing the result of an MCP tool execution.

    - `ID string`

      Unique identifier for this event.

    - `MCPToolUseID string`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsAgentMCPToolResultEventType`

    - `Content []BetaManagedAgentsAgentMCPToolResultEventContentUnion Optional`

      The result content returned by the tool.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `type BetaManagedAgentsSearchResultBlock struct{…}`

        A block containing a web search result.

    - `IsError bool Optional`

      Whether the tool execution resulted in an error.

  - `type BetaManagedAgentsAgentToolUseEvent struct{…}`

    Event emitted when the agent invokes a built-in agent tool.

    - `ID string`

      Unique identifier for this event.

    - `Input map[string, any]`

      Input parameters for the tool call.

    - `Name string`

      Name of the agent tool being used.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsAgentToolUseEventType`

    - `EvaluatedPermission BetaManagedAgentsAgentToolUseEventEvaluatedPermission Optional`

      AgentEvaluatedPermission enum

      - `const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionAllow BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "allow"`

      - `const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionAsk BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "ask"`

      - `const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionDeny BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "deny"`

    - `SessionThreadID string Optional`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `type BetaManagedAgentsAgentToolResultEvent struct{…}`

    Event representing the result of an agent tool execution.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `ToolUseID string`

      The id of the `agent.tool_use` event this result corresponds to.

    - `Type BetaManagedAgentsAgentToolResultEventType`

    - `Content []BetaManagedAgentsAgentToolResultEventContentUnion Optional`

      The result content returned by the tool.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `type BetaManagedAgentsSearchResultBlock struct{…}`

        A block containing a web search result.

    - `IsError bool Optional`

      Whether the tool execution resulted in an error.

  - `type BetaManagedAgentsAgentThreadMessageReceivedEvent struct{…}`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsAgentThreadMessageReceivedEventContentUnion`

      Message content blocks.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `type BetaManagedAgentsRedactedBlockParam struct{…}`

        Placeholder for content withheld by Anthropic model policy.

    - `FromSessionThreadID string`

      Public `sthr_` ID of the thread that sent the message.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsAgentThreadMessageReceivedEventType`

    - `FromAgentName string Optional`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `type BetaManagedAgentsAgentThreadMessageSentEvent struct{…}`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsAgentThreadMessageSentEventContentUnion`

      Message content blocks.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `type BetaManagedAgentsRedactedBlockParam struct{…}`

        Placeholder for content withheld by Anthropic model policy.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `ToSessionThreadID string`

      Public `sthr_` ID of the thread the message was sent to.

    - `Type BetaManagedAgentsAgentThreadMessageSentEventType`

    - `ToAgentName string Optional`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `type BetaManagedAgentsAgentThreadContextCompactedEvent struct{…}`

    Indicates that context compaction (summarization) occurred during the session.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsAgentThreadContextCompactedEventType`

  - `type BetaManagedAgentsSessionErrorEvent struct{…}`

    An error event indicating a problem occurred during session execution.

    - `ID string`

      Unique identifier for this event.

    - `Error BetaManagedAgentsSessionErrorEventErrorUnion`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `type BetaManagedAgentsUnknownError struct{…}`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsUnknownErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type BetaManagedAgentsRetryStatusRetryingType`

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type BetaManagedAgentsRetryStatusExhaustedType`

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type BetaManagedAgentsRetryStatusTerminalType`

        - `Type BetaManagedAgentsUnknownErrorType`

      - `type BetaManagedAgentsModelOverloadedError struct{…}`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsModelOverloadedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type BetaManagedAgentsModelOverloadedErrorType`

      - `type BetaManagedAgentsModelRateLimitedError struct{…}`

        The model request was rate-limited.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsModelRateLimitedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type BetaManagedAgentsModelRateLimitedErrorType`

      - `type BetaManagedAgentsModelRequestFailedError struct{…}`

        A model request failed for a reason other than overload or rate-limiting.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsModelRequestFailedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type BetaManagedAgentsModelRequestFailedErrorType`

      - `type BetaManagedAgentsMCPConnectionFailedError struct{…}`

        Failed to connect to an MCP server.

        - `MCPServerName string`

          Name of the MCP server that failed to connect.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsMCPConnectionFailedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type BetaManagedAgentsMCPConnectionFailedErrorType`

      - `type BetaManagedAgentsMCPAuthenticationFailedError struct{…}`

        Authentication to an MCP server failed.

        - `MCPServerName string`

          Name of the MCP server that failed authentication.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsMCPAuthenticationFailedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type BetaManagedAgentsMCPAuthenticationFailedErrorType`

      - `type BetaManagedAgentsBillingError struct{…}`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsBillingErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type BetaManagedAgentsBillingErrorType`

      - `type BetaManagedAgentsCredentialHostUnreachableError struct{…}`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `CredentialID string`

          ID of the affected credential.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsCredentialHostUnreachableErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type BetaManagedAgentsCredentialHostUnreachableErrorType`

        - `VaultID string`

          ID of the vault containing the affected credential.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSessionErrorEventType`

  - `type BetaManagedAgentsSessionStatusRescheduledEvent struct{…}`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSessionStatusRescheduledEventType`

  - `type BetaManagedAgentsSessionStatusRunningEvent struct{…}`

    Indicates the session is actively running and the agent is working.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSessionStatusRunningEventType`

  - `type BetaManagedAgentsSessionStatusIdleEvent struct{…}`

    Indicates the agent has paused and is awaiting user input.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `StopReason BetaManagedAgentsSessionStatusIdleEventStopReasonUnion`

      The agent completed its turn naturally and is ready for the next user message.

      - `type BetaManagedAgentsSessionEndTurn struct{…}`

        The agent completed its turn naturally and is ready for the next user message.

        - `Type BetaManagedAgentsSessionEndTurnType`

      - `type BetaManagedAgentsSessionRequiresAction struct{…}`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `EventIDs []string`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `Type BetaManagedAgentsSessionRequiresActionType`

      - `type BetaManagedAgentsSessionRetriesExhausted struct{…}`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `Type BetaManagedAgentsSessionRetriesExhaustedType`

      - `type BetaManagedAgentsSessionBudgetReached struct{…}`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `Type BetaManagedAgentsSessionBudgetReachedType`

    - `Type BetaManagedAgentsSessionStatusIdleEventType`

  - `type BetaManagedAgentsSessionStatusTerminatedEvent struct{…}`

    Indicates the session has terminated, either due to an error or completion.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSessionStatusTerminatedEventType`

  - `type BetaManagedAgentsSessionThreadCreatedEvent struct{…}`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the callable agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string`

      Public `sthr_` ID of the newly created thread.

    - `Type BetaManagedAgentsSessionThreadCreatedEventType`

  - `type BetaManagedAgentsSpanOutcomeEvaluationStartEvent struct{…}`

    Emitted when an outcome evaluation cycle begins.

    - `ID string`

      Unique identifier for this event.

    - `Iteration int64`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

      format: int32

    - `OutcomeID string`

      The `outc_` ID of the outcome being evaluated.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSpanOutcomeEvaluationStartEventType`

  - `type BetaManagedAgentsSpanOutcomeEvaluationEndEvent struct{…}`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `ID string`

      Unique identifier for this event.

    - `Explanation string`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `Iteration int64`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `OutcomeEvaluationStartID string`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `OutcomeID string`

      The `outc_` ID of the outcome being evaluated.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Result string`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `Type BetaManagedAgentsSpanOutcomeEvaluationEndEventType`

    - `Usage BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `CacheCreationInputTokens int64`

        Tokens used to create prompt cache in this request.

        format: int32

      - `CacheReadInputTokens int64`

        Tokens read from prompt cache in this request.

        format: int32

      - `InputTokens int64`

        Input tokens consumed by this request.

        format: int32

      - `OutputTokens int64`

        Output tokens generated by this request.

        format: int32

      - `Speed BetaManagedAgentsSpanModelUsageSpeed Optional`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `const BetaManagedAgentsSpanModelUsageSpeedStandard BetaManagedAgentsSpanModelUsageSpeed = "standard"`

        - `const BetaManagedAgentsSpanModelUsageSpeedFast BetaManagedAgentsSpanModelUsageSpeed = "fast"`

  - `type BetaManagedAgentsSpanModelRequestStartEvent struct{…}`

    Emitted when a model request is initiated by the agent.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSpanModelRequestStartEventType`

  - `type BetaManagedAgentsSpanModelRequestEndEvent struct{…}`

    Emitted when a model request completes.

    - `ID string`

      Unique identifier for this event.

    - `IsError bool`

      Whether the model request resulted in an error.

    - `ModelRequestStartID string`

      The id of the corresponding `span.model_request_start` event.

    - `ModelUsage BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSpanModelRequestEndEventType`

  - `type BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent struct{…}`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `ID string`

      Unique identifier for this event.

    - `Iteration int64`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `OutcomeID string`

      The `outc_` ID of the outcome being evaluated.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSpanOutcomeEvaluationOngoingEventType`

  - `type BetaManagedAgentsUserDefineOutcomeEvent struct{…}`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `ID string`

      Unique identifier for this event.

    - `Description string`

      What the agent should produce. Copied from the input event.

    - `MaxIterations int64`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

      format: int32

    - `OutcomeID string`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Rubric BetaManagedAgentsUserDefineOutcomeEventRubricUnion`

      Rubric for grading the quality of an outcome.

      - `type BetaManagedAgentsFileRubric struct{…}`

        Rubric referenced by a file uploaded via the Files API.

        - `FileID string`

          ID of the rubric file.

        - `Type BetaManagedAgentsFileRubricType`

      - `type BetaManagedAgentsTextRubric struct{…}`

        Rubric content provided inline as text.

        - `Content string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `Type BetaManagedAgentsTextRubricType`

    - `Type BetaManagedAgentsUserDefineOutcomeEventType`

  - `type BetaManagedAgentsSessionDeletedEvent struct{…}`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSessionDeletedEventType`

  - `type BetaManagedAgentsSessionThreadStatusRunningEvent struct{…}`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string`

      Public sthr_ ID of the thread that started running.

    - `Type BetaManagedAgentsSessionThreadStatusRunningEventType`

  - `type BetaManagedAgentsSessionThreadStatusIdleEvent struct{…}`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string`

      Public sthr_ ID of the thread that went idle.

    - `StopReason BetaManagedAgentsSessionThreadStatusIdleEventStopReasonUnion`

      The agent completed its turn naturally and is ready for the next user message.

      - `type BetaManagedAgentsSessionEndTurn struct{…}`

        The agent completed its turn naturally and is ready for the next user message.

      - `type BetaManagedAgentsSessionRequiresAction struct{…}`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `type BetaManagedAgentsSessionRetriesExhausted struct{…}`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `type BetaManagedAgentsSessionBudgetReached struct{…}`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

    - `Type BetaManagedAgentsSessionThreadStatusIdleEventType`

  - `type BetaManagedAgentsSessionThreadStatusTerminatedEvent struct{…}`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string`

      Public sthr_ ID of the thread that terminated.

    - `Type BetaManagedAgentsSessionThreadStatusTerminatedEventType`

  - `type BetaManagedAgentsUserToolResultEvent struct{…}`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `ID string`

      Unique identifier for this event.

    - `ToolUseID string`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type BetaManagedAgentsUserToolResultEventType`

    - `Content []BetaManagedAgentsUserToolResultEventContentUnion Optional`

      The result content returned by the tool.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `type BetaManagedAgentsSearchResultBlock struct{…}`

        A block containing a web search result.

    - `IsError bool Optional`

      Whether the tool execution resulted in an error.

    - `ProcessedAt Time Optional`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string Optional`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `type BetaManagedAgentsSessionThreadStatusRescheduledEvent struct{…}`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string`

      Public sthr_ ID of the thread that is retrying.

    - `Type BetaManagedAgentsSessionThreadStatusRescheduledEventType`

  - `type BetaManagedAgentsSessionUpdatedEvent struct{…}`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSessionUpdatedEventType`

    - `Agent BetaManagedAgentsSessionAgent Optional`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `ID string`

      - `Description string`

      - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

        - `Name string`

        - `Type BetaManagedAgentsMCPServerURLDefinitionType`

        - `URL string`

      - `Model BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `ID BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `type BetaManagedAgentsModel string`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `const BetaManagedAgentsModelClaudeSonnet5 BetaManagedAgentsModel = "claude-sonnet-5"`

              High-performance model for coding and agents

            - `const BetaManagedAgentsModelClaudeFable5 BetaManagedAgentsModel = "claude-fable-5"`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `const BetaManagedAgentsModelClaudeOpus5 BetaManagedAgentsModel = "claude-opus-5"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeOpus4_8 BetaManagedAgentsModel = "claude-opus-4-8"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeOpus4_7 BetaManagedAgentsModel = "claude-opus-4-7"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeOpus4_6 BetaManagedAgentsModel = "claude-opus-4-6"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeSonnet4_6 BetaManagedAgentsModel = "claude-sonnet-4-6"`

              Best combination of speed and intelligence

            - `const BetaManagedAgentsModelClaudeHaiku4_5 BetaManagedAgentsModel = "claude-haiku-4-5"`

              Fastest model with near-frontier intelligence

            - `const BetaManagedAgentsModelClaudeHaiku4_5_20251001 BetaManagedAgentsModel = "claude-haiku-4-5-20251001"`

              Fastest model with near-frontier intelligence

            - `const BetaManagedAgentsModelClaudeOpus4_5 BetaManagedAgentsModel = "claude-opus-4-5"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeOpus4_5_20251101 BetaManagedAgentsModel = "claude-opus-4-5-20251101"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeSonnet4_5 BetaManagedAgentsModel = "claude-sonnet-4-5"`

              High-performance model for agents and coding

            - `const BetaManagedAgentsModelClaudeSonnet4_5_20250929 BetaManagedAgentsModel = "claude-sonnet-4-5-20250929"`

              High-performance model for agents and coding

          - `string`

        - `Effort BetaManagedAgentsModelConfigEffortUnion Optional`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `type BetaManagedAgentsEffortLow struct{…}`

            Low effort. Favors latency over reasoning depth.

            - `Type BetaManagedAgentsEffortLowType`

          - `type BetaManagedAgentsEffortMedium struct{…}`

            Medium effort. Balances latency and reasoning depth.

            - `Type BetaManagedAgentsEffortMediumType`

          - `type BetaManagedAgentsEffortHigh struct{…}`

            High effort. Favors reasoning depth.

            - `Type BetaManagedAgentsEffortHighType`

          - `type BetaManagedAgentsEffortXhigh struct{…}`

            Extra-high effort. Not all models accept this level.

            - `Type BetaManagedAgentsEffortXhighType`

          - `type BetaManagedAgentsEffortMax struct{…}`

            Maximum effort. Favors reasoning depth over latency.

            - `Type BetaManagedAgentsEffortMaxType`

        - `InferenceGeo string Optional`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `Speed BetaManagedAgentsModelConfigSpeed Optional`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `const BetaManagedAgentsModelConfigSpeedStandard BetaManagedAgentsModelConfigSpeed = "standard"`

          - `const BetaManagedAgentsModelConfigSpeedFast BetaManagedAgentsModelConfigSpeed = "fast"`

      - `Multiagent BetaManagedAgentsSessionMultiagentCoordinator`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `Agents []BetaManagedAgentsSessionMultiagentCoordinatorAgentUnion`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `type BetaManagedAgentsSessionThreadAgent struct{…}`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `ID string`

            - `Description string`

            - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

              - `Name string`

              - `Type BetaManagedAgentsMCPServerURLDefinitionType`

              - `URL string`

            - `Model BetaManagedAgentsModelConfig`

              Model identifier and configuration.

            - `Name string`

            - `Skills []BetaManagedAgentsSessionThreadAgentSkillUnion`

              - `type BetaManagedAgentsAnthropicSkill struct{…}`

                A resolved Anthropic-managed skill.

                - `SkillID string`

                - `Type BetaManagedAgentsAnthropicSkillType`

                - `Version string`

              - `type BetaManagedAgentsCustomSkill struct{…}`

                A resolved user-created custom skill.

                - `SkillID string`

                - `Type BetaManagedAgentsCustomSkillType`

                - `Version string`

            - `System string`

            - `Tools []BetaManagedAgentsSessionThreadAgentToolUnion`

              - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

                - `Configs []BetaManagedAgentsAgentToolConfigUnion`

                  - `type BetaManagedAgentsBashToolConfig struct{…}`

                    Configuration for the bash tool.

                    - `Enabled bool`

                    - `Name Bash`

                    - `PermissionPolicy BetaManagedAgentsBashToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                        - `Type BetaManagedAgentsAlwaysAllowPolicyType`

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                        - `Type BetaManagedAgentsAlwaysAskPolicyType`

                    - `Type Bash`

                  - `type BetaManagedAgentsEditToolConfig struct{…}`

                    Configuration for the edit tool.

                    - `Enabled bool`

                    - `Name Edit`

                    - `PermissionPolicy BetaManagedAgentsEditToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                    - `Type Edit`

                  - `type BetaManagedAgentsReadToolConfig struct{…}`

                    Configuration for the read tool.

                    - `Enabled bool`

                    - `Name Read`

                    - `PermissionPolicy BetaManagedAgentsReadToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                    - `Type Read`

                  - `type BetaManagedAgentsWriteToolConfig struct{…}`

                    Configuration for the write tool.

                    - `Enabled bool`

                    - `Name Write`

                    - `PermissionPolicy BetaManagedAgentsWriteToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                    - `Type Write`

                  - `type BetaManagedAgentsGlobToolConfig struct{…}`

                    Configuration for the glob tool.

                    - `Enabled bool`

                    - `Name Glob`

                    - `PermissionPolicy BetaManagedAgentsGlobToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                    - `Type Glob`

                  - `type BetaManagedAgentsGrepToolConfig struct{…}`

                    Configuration for the grep tool.

                    - `Enabled bool`

                    - `Name Grep`

                    - `PermissionPolicy BetaManagedAgentsGrepToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                    - `Type Grep`

                  - `type BetaManagedAgentsWebFetchToolConfig struct{…}`

                    Configuration for the web_fetch tool.

                    - `Enabled bool`

                    - `Name WebFetch`

                    - `PermissionPolicy BetaManagedAgentsWebFetchToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                    - `Type WebFetch`

                    - `AllowedDomains []string Optional`

                    - `BlockedDomains []string Optional`

                    - `MaxContentTokens int64 Optional`

                      format: int32

                  - `type BetaManagedAgentsWebSearchToolConfig struct{…}`

                    Configuration for the web_search tool.

                    - `Enabled bool`

                    - `Name WebSearch`

                    - `PermissionPolicy BetaManagedAgentsWebSearchToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                    - `Type WebSearch`

                    - `AllowedDomains []string Optional`

                    - `BlockedDomains []string Optional`

                    - `UserLocation BetaManagedAgentsUserLocation Optional`

                      Approximate user location for search result localization.

                      - `Type Approximate`

                        Location precision. Only "approximate" is supported.

                      - `City string Optional`

                        City name.

                        minLength: 1, maxLength: 255

                      - `Country string Optional`

                        Two-letter ISO 3166-1 country code, uppercase.

                      - `Region string Optional`

                        Region or state name.

                        minLength: 1, maxLength: 255

                      - `Timezone string Optional`

                        IANA timezone identifier, e.g. "America/Los_Angeles".

                        minLength: 1, maxLength: 255

                - `DefaultConfig BetaManagedAgentsAgentToolsetDefaultConfig`

                  Resolved default configuration for agent tools.

                  - `Enabled bool`

                  - `PermissionPolicy BetaManagedAgentsAgentToolsetDefaultConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                - `Type BetaManagedAgentsAgentToolset20260401Type`

              - `type BetaManagedAgentsMCPToolset struct{…}`

                - `Configs []BetaManagedAgentsMCPToolConfig`

                  - `Enabled bool`

                  - `Name string`

                  - `PermissionPolicy BetaManagedAgentsMCPToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                - `DefaultConfig BetaManagedAgentsMCPToolsetDefaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `Enabled bool`

                  - `PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                - `MCPServerName string`

                - `Type BetaManagedAgentsMCPToolsetType`

              - `type BetaManagedAgentsCustomTool struct{…}`

                A custom tool as returned in API responses.

                - `Description string`

                - `InputSchema BetaManagedAgentsCustomToolInputSchema`

                  JSON Schema for custom tool input parameters.

                  - `Type Object`

                  - `Properties map[string, any] Optional`

                  - `Required []string Optional`

                - `Name string`

                - `Type BetaManagedAgentsCustomToolType`

            - `Type BetaManagedAgentsSessionThreadAgentType`

            - `Version int64`

              format: int32

          - `type BetaManagedAgentsAdvisor struct{…}`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `Model string`

              The advisor model id.

            - `Type BetaManagedAgentsAdvisorType`

        - `Type BetaManagedAgentsSessionMultiagentCoordinatorType`

      - `Name string`

      - `Skills []BetaManagedAgentsSessionAgentSkillUnion`

        - `type BetaManagedAgentsAnthropicSkill struct{…}`

          A resolved Anthropic-managed skill.

        - `type BetaManagedAgentsCustomSkill struct{…}`

          A resolved user-created custom skill.

      - `System string`

      - `Tools []BetaManagedAgentsSessionAgentToolUnion`

        - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

        - `type BetaManagedAgentsMCPToolset struct{…}`

        - `type BetaManagedAgentsCustomTool struct{…}`

          A custom tool as returned in API responses.

      - `Type BetaManagedAgentsSessionAgentType`

      - `Version int64`

        format: int32

    - `Budget BetaManagedAgentsBudgetLimit Optional`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `MaxListCost BetaMonetaryAmount`

        A monetary amount in a specific currency.

        - `Amount string`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `Currency BetaCurrency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `Type BetaManagedAgentsBudgetLimitType`

    - `Metadata map[string, string] Optional`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `Title string Optional`

      The session's new title. Present only when the update changed it.

  - `type BetaManagedAgentsSystemMessageEvent struct{…}`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsSystemContentBlock`

      System content blocks. Text-only.

      - `Text string`

        The text content.

        minLength: 1

      - `Type BetaManagedAgentsSystemContentBlockType`

    - `Type BetaManagedAgentsSystemMessageEventType`

    - `ProcessedAt Time Optional`

      A timestamp in RFC 3339 format

      format: date-time

  - `type BetaManagedAgentsSessionUsageEvent struct{…}`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSessionUsageEventType`

    - `Usage BetaManagedAgentsSessionUsageSnapshot`

      Point-in-time snapshot of a session's cumulative usage.

      - `ActiveSeconds float64 Optional`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `CacheCreation BetaManagedAgentsCacheCreationUsage Optional`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `Ephemeral1hInputTokens int64 Optional`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `Ephemeral5mInputTokens int64 Optional`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `CacheReadInputTokens int64 Optional`

        Total tokens read from prompt cache.

        format: int32

      - `InputTokens int64 Optional`

        Total input tokens consumed across all turns.

        format: int32

      - `ListCost BetaMonetaryAmount Optional`

        A monetary amount in a specific currency.

      - `OutputTokens int64 Optional`

        Total output tokens generated across all turns.

        format: int32

      - `ServerToolUse BetaManagedAgentsServerToolUsage Optional`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `WebFetchRequests int64 Optional`

          Number of server-executed web fetch requests.

          format: int32

        - `WebSearchRequests int64 Optional`

          Number of server-executed web search requests.

          format: int32

    - `Budget BetaManagedAgentsBudgetLimit Optional`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

#### Example

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
	page, err := client.Beta.Sessions.Events.List(
		context.TODO(),
		"sesn_011CZkZAtmR3yMPDzynEDxu7",
		anthropic.BetaSessionEventListParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
}
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message",
      "processed_at": "2026-03-15T10:00:00Z"
    },
    {
      "id": "sevt_011CZkZHPq1jCdq5lbRTjiVnz",
      "content": [
        {
          "text": "Let me look up order #1234 for you.",
          "type": "text"
        }
      ],
      "processed_at": "2026-03-15T10:00:00Z",
      "type": "agent.message"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

### Send Events

`client.Beta.Sessions.Events.Send(ctx, sessionID, params) (*BetaManagedAgentsSendSessionEvents, error)`

**POST** `/v1/sessions/{session_id}/events`

Send Events

#### Parameters

- `sessionID string`

- `params BetaSessionEventSendParams`

  - `Events param.Field[[]BetaManagedAgentsEventParamsUnionResp]`

    Body param: Events to send to the `session`.

    - `type BetaManagedAgentsUserMessageEventParams struct{…}`

      Parameters for sending a user message to the session.

      - `Content []BetaManagedAgentsUserMessageEventParamsContentUnionResp`

        Array of content blocks for the user message.

        - `type BetaManagedAgentsTextBlock struct{…}`

          Regular text content.

          - `Text string`

            The text content.

            minLength: 1

          - `Type BetaManagedAgentsTextBlockType`

        - `type BetaManagedAgentsImageBlock struct{…}`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source BetaManagedAgentsImageBlockSourceUnion`

            Union type for image source variants.

            - `type BetaManagedAgentsBase64ImageSource struct{…}`

              Base64-encoded image data.

              - `Data string`

                Base64-encoded image data.

                minLength: 1

              - `MediaType string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `Type BetaManagedAgentsBase64ImageSourceType`

            - `type BetaManagedAgentsURLImageSource struct{…}`

              Image referenced by URL.

              - `Type BetaManagedAgentsURLImageSourceType`

              - `URL string`

                URL of the image to fetch.

                minLength: 1

            - `type BetaManagedAgentsFileImageSource struct{…}`

              Image referenced by file ID.

              - `FileID string`

                ID of a previously uploaded file.

                minLength: 1

              - `Type BetaManagedAgentsFileImageSourceType`

          - `Type BetaManagedAgentsImageBlockType`

        - `type BetaManagedAgentsDocumentBlock struct{…}`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source BetaManagedAgentsDocumentBlockSourceUnion`

            Union type for document source variants.

            - `type BetaManagedAgentsBase64DocumentSource struct{…}`

              Base64-encoded document data.

              - `Data string`

                Base64-encoded document data.

                minLength: 1

              - `MediaType string`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `Type BetaManagedAgentsBase64DocumentSourceType`

            - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

              Plain text document content.

              - `Data string`

                The plain text content.

                minLength: 1

              - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

                MIME type of the text content. Must be "text/plain".

              - `Type BetaManagedAgentsPlainTextDocumentSourceType`

            - `type BetaManagedAgentsURLDocumentSource struct{…}`

              Document referenced by URL.

              - `Type BetaManagedAgentsURLDocumentSourceType`

              - `URL string`

                URL of the document to fetch.

                minLength: 1

            - `type BetaManagedAgentsFileDocumentSource struct{…}`

              Document referenced by file ID.

              - `FileID string`

                ID of a previously uploaded file.

                minLength: 1

              - `Type BetaManagedAgentsFileDocumentSourceType`

          - `Type BetaManagedAgentsDocumentBlockType`

          - `Context string Optional`

            Additional context about the document for the model.

          - `Title string Optional`

            The title of the document.

        - `type BetaManagedAgentsRedactedBlockParam struct{…}`

          Placeholder for content withheld by Anthropic model policy.

          - `Type BetaManagedAgentsRedactedBlockType`

      - `Type BetaManagedAgentsUserMessageEventParamsType`

    - `type BetaManagedAgentsUserInterruptEventParamsResp struct{…}`

      Parameters for sending an interrupt to pause the agent.

      - `Type BetaManagedAgentsUserInterruptEventParamsType`

      - `SessionThreadID string Optional`

        If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

    - `type BetaManagedAgentsUserToolConfirmationEventParamsResp struct{…}`

      Parameters for confirming or denying a tool execution request.

      - `Result BetaManagedAgentsUserToolConfirmationEventParamsResult`

        UserToolConfirmationResult enum

        - `const BetaManagedAgentsUserToolConfirmationEventParamsResultAllow BetaManagedAgentsUserToolConfirmationEventParamsResult = "allow"`

        - `const BetaManagedAgentsUserToolConfirmationEventParamsResultDeny BetaManagedAgentsUserToolConfirmationEventParamsResult = "deny"`

      - `ToolUseID string`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

        minLength: 1, maxLength: 128

      - `Type BetaManagedAgentsUserToolConfirmationEventParamsType`

      - `DenyMessage string Optional`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

        maxLength: 10000

    - `type BetaManagedAgentsUserCustomToolResultEventParamsResp struct{…}`

      Parameters for providing the result of a custom tool execution.

      - `CustomToolUseID string`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

        minLength: 1, maxLength: 128

      - `Type BetaManagedAgentsUserCustomToolResultEventParamsType`

      - `Content []BetaManagedAgentsUserCustomToolResultEventParamsContentUnionResp Optional`

        The result content returned by the tool.

        - `type BetaManagedAgentsTextBlock struct{…}`

          Regular text content.

        - `type BetaManagedAgentsImageBlock struct{…}`

          Image content specified directly as base64 data or as a reference via a URL.

        - `type BetaManagedAgentsDocumentBlock struct{…}`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `type BetaManagedAgentsSearchResultBlock struct{…}`

          A block containing a web search result.

          - `Citations BetaManagedAgentsSearchResultCitations`

            Citation settings for a search result.

            - `Enabled bool`

              Whether citations are enabled for this search result.

          - `Content []BetaManagedAgentsSearchResultContent`

            Array of text content blocks from the search result.

            - `Text string`

              The text content.

              minLength: 1

            - `Type BetaManagedAgentsSearchResultContentType`

          - `Source string`

            The URL source of the search result.

            minLength: 1

          - `Title string`

            The title of the search result.

            minLength: 1

          - `Type BetaManagedAgentsSearchResultBlockType`

      - `IsError bool Optional`

        Whether the tool execution resulted in an error.

    - `type BetaManagedAgentsUserDefineOutcomeEventParams struct{…}`

      Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

      - `Description string`

        What the agent should produce. This is the task specification.

      - `Rubric BetaManagedAgentsUserDefineOutcomeEventParamsRubricUnionResp`

        Rubric for grading the quality of an outcome.

        - `type BetaManagedAgentsFileRubricParams struct{…}`

          Rubric referenced by a file uploaded via the Files API.

          - `FileID string`

            ID of the rubric file.

          - `Type BetaManagedAgentsFileRubricParamsType`

        - `type BetaManagedAgentsTextRubricParams struct{…}`

          Rubric content provided inline as text.

          - `Content string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

            maxLength: 262144

          - `Type BetaManagedAgentsTextRubricParamsType`

      - `Type BetaManagedAgentsUserDefineOutcomeEventParamsType`

      - `MaxIterations int64 Optional`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `type BetaManagedAgentsUserToolResultEventParamsResp struct{…}`

      Parameters for providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

      - `ToolUseID string`

        The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

        minLength: 1, maxLength: 128

      - `Type BetaManagedAgentsUserToolResultEventParamsType`

      - `Content []BetaManagedAgentsUserToolResultEventParamsContentUnionResp Optional`

        The result content returned by the tool.

        - `type BetaManagedAgentsTextBlock struct{…}`

          Regular text content.

        - `type BetaManagedAgentsImageBlock struct{…}`

          Image content specified directly as base64 data or as a reference via a URL.

        - `type BetaManagedAgentsDocumentBlock struct{…}`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `type BetaManagedAgentsSearchResultBlock struct{…}`

          A block containing a web search result.

      - `IsError bool Optional`

        Whether the tool execution resulted in an error.

    - `type BetaManagedAgentsSystemMessageEventParamsResp struct{…}`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

      - `Content []BetaManagedAgentsSystemContentBlock`

        System content blocks to append. Text-only.

        - `Text string`

          The text content.

          minLength: 1

        - `Type BetaManagedAgentsSystemContentBlockType`

      - `Type BetaManagedAgentsSystemMessageEventParamsType`

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

#### Returns

- `type BetaManagedAgentsSendSessionEvents struct{…}`

  Events that were successfully sent to the session.

  - `Data []BetaManagedAgentsSendSessionEventsDataUnion Optional`

    Sent events

    - `type BetaManagedAgentsUserMessageEvent struct{…}`

      A user message event in the session conversation.

      - `ID string`

        Unique identifier for this event.

      - `Content []BetaManagedAgentsUserMessageEventContentUnion`

        Array of content blocks comprising the user message.

        - `type BetaManagedAgentsTextBlock struct{…}`

          Regular text content.

          - `Text string`

            The text content.

            minLength: 1

          - `Type BetaManagedAgentsTextBlockType`

        - `type BetaManagedAgentsImageBlock struct{…}`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source BetaManagedAgentsImageBlockSourceUnion`

            Union type for image source variants.

            - `type BetaManagedAgentsBase64ImageSource struct{…}`

              Base64-encoded image data.

              - `Data string`

                Base64-encoded image data.

                minLength: 1

              - `MediaType string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `Type BetaManagedAgentsBase64ImageSourceType`

            - `type BetaManagedAgentsURLImageSource struct{…}`

              Image referenced by URL.

              - `Type BetaManagedAgentsURLImageSourceType`

              - `URL string`

                URL of the image to fetch.

                minLength: 1

            - `type BetaManagedAgentsFileImageSource struct{…}`

              Image referenced by file ID.

              - `FileID string`

                ID of a previously uploaded file.

                minLength: 1

              - `Type BetaManagedAgentsFileImageSourceType`

          - `Type BetaManagedAgentsImageBlockType`

        - `type BetaManagedAgentsDocumentBlock struct{…}`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source BetaManagedAgentsDocumentBlockSourceUnion`

            Union type for document source variants.

            - `type BetaManagedAgentsBase64DocumentSource struct{…}`

              Base64-encoded document data.

              - `Data string`

                Base64-encoded document data.

                minLength: 1

              - `MediaType string`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `Type BetaManagedAgentsBase64DocumentSourceType`

            - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

              Plain text document content.

              - `Data string`

                The plain text content.

                minLength: 1

              - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

                MIME type of the text content. Must be "text/plain".

              - `Type BetaManagedAgentsPlainTextDocumentSourceType`

            - `type BetaManagedAgentsURLDocumentSource struct{…}`

              Document referenced by URL.

              - `Type BetaManagedAgentsURLDocumentSourceType`

              - `URL string`

                URL of the document to fetch.

                minLength: 1

            - `type BetaManagedAgentsFileDocumentSource struct{…}`

              Document referenced by file ID.

              - `FileID string`

                ID of a previously uploaded file.

                minLength: 1

              - `Type BetaManagedAgentsFileDocumentSourceType`

          - `Type BetaManagedAgentsDocumentBlockType`

          - `Context string Optional`

            Additional context about the document for the model.

          - `Title string Optional`

            The title of the document.

        - `type BetaManagedAgentsRedactedBlockParam struct{…}`

          Placeholder for content withheld by Anthropic model policy.

          - `Type BetaManagedAgentsRedactedBlockType`

      - `Type BetaManagedAgentsUserMessageEventType`

      - `ProcessedAt Time Optional`

        A timestamp in RFC 3339 format

        format: date-time

    - `type BetaManagedAgentsUserInterruptEvent struct{…}`

      An interrupt event that pauses agent execution and returns control to the user.

      - `ID string`

        Unique identifier for this event.

      - `Type BetaManagedAgentsUserInterruptEventType`

      - `ProcessedAt Time Optional`

        A timestamp in RFC 3339 format

        format: date-time

      - `SessionThreadID string Optional`

        If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

    - `type BetaManagedAgentsUserToolConfirmationEvent struct{…}`

      A tool confirmation event that approves or denies a pending tool execution.

      - `ID string`

        Unique identifier for this event.

      - `Result BetaManagedAgentsUserToolConfirmationEventResult`

        UserToolConfirmationResult enum

        - `const BetaManagedAgentsUserToolConfirmationEventResultAllow BetaManagedAgentsUserToolConfirmationEventResult = "allow"`

        - `const BetaManagedAgentsUserToolConfirmationEventResultDeny BetaManagedAgentsUserToolConfirmationEventResult = "deny"`

      - `ToolUseID string`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `Type BetaManagedAgentsUserToolConfirmationEventType`

      - `DenyMessage string Optional`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

        maxLength: 10000

      - `ProcessedAt Time Optional`

        A timestamp in RFC 3339 format

        format: date-time

      - `SessionThreadID string Optional`

        When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

    - `type BetaManagedAgentsUserCustomToolResultEvent struct{…}`

      Event sent by the client providing the result of a custom tool execution.

      - `ID string`

        Unique identifier for this event.

      - `CustomToolUseID string`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `Type BetaManagedAgentsUserCustomToolResultEventType`

      - `Content []BetaManagedAgentsUserCustomToolResultEventContentUnion Optional`

        The result content returned by the tool.

        - `type BetaManagedAgentsTextBlock struct{…}`

          Regular text content.

        - `type BetaManagedAgentsImageBlock struct{…}`

          Image content specified directly as base64 data or as a reference via a URL.

        - `type BetaManagedAgentsDocumentBlock struct{…}`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `type BetaManagedAgentsSearchResultBlock struct{…}`

          A block containing a web search result.

          - `Citations BetaManagedAgentsSearchResultCitations`

            Citation settings for a search result.

            - `Enabled bool`

              Whether citations are enabled for this search result.

          - `Content []BetaManagedAgentsSearchResultContent`

            Array of text content blocks from the search result.

            - `Text string`

              The text content.

              minLength: 1

            - `Type BetaManagedAgentsSearchResultContentType`

          - `Source string`

            The URL source of the search result.

            minLength: 1

          - `Title string`

            The title of the search result.

            minLength: 1

          - `Type BetaManagedAgentsSearchResultBlockType`

      - `IsError bool Optional`

        Whether the tool execution resulted in an error.

      - `ProcessedAt Time Optional`

        A timestamp in RFC 3339 format

        format: date-time

      - `SessionThreadID string Optional`

        Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

    - `type BetaManagedAgentsUserDefineOutcomeEvent struct{…}`

      Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

      - `ID string`

        Unique identifier for this event.

      - `Description string`

        What the agent should produce. Copied from the input event.

      - `MaxIterations int64`

        Evaluate-then-revise cycles before giving up. Default 3, max 20.

        format: int32

      - `OutcomeID string`

        Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

      - `ProcessedAt Time`

        A timestamp in RFC 3339 format

        format: date-time

      - `Rubric BetaManagedAgentsUserDefineOutcomeEventRubricUnion`

        Rubric for grading the quality of an outcome.

        - `type BetaManagedAgentsFileRubric struct{…}`

          Rubric referenced by a file uploaded via the Files API.

          - `FileID string`

            ID of the rubric file.

          - `Type BetaManagedAgentsFileRubricType`

        - `type BetaManagedAgentsTextRubric struct{…}`

          Rubric content provided inline as text.

          - `Content string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `Type BetaManagedAgentsTextRubricType`

      - `Type BetaManagedAgentsUserDefineOutcomeEventType`

    - `type BetaManagedAgentsUserToolResultEvent struct{…}`

      Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

      - `ID string`

        Unique identifier for this event.

      - `ToolUseID string`

        The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `Type BetaManagedAgentsUserToolResultEventType`

      - `Content []BetaManagedAgentsUserToolResultEventContentUnion Optional`

        The result content returned by the tool.

        - `type BetaManagedAgentsTextBlock struct{…}`

          Regular text content.

        - `type BetaManagedAgentsImageBlock struct{…}`

          Image content specified directly as base64 data or as a reference via a URL.

        - `type BetaManagedAgentsDocumentBlock struct{…}`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `type BetaManagedAgentsSearchResultBlock struct{…}`

          A block containing a web search result.

      - `IsError bool Optional`

        Whether the tool execution resulted in an error.

      - `ProcessedAt Time Optional`

        A timestamp in RFC 3339 format

        format: date-time

      - `SessionThreadID string Optional`

        Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

    - `type BetaManagedAgentsSystemMessageEvent struct{…}`

      A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

      - `ID string`

        Unique identifier for this event.

      - `Content []BetaManagedAgentsSystemContentBlock`

        System content blocks. Text-only.

        - `Text string`

          The text content.

          minLength: 1

        - `Type BetaManagedAgentsSystemContentBlockType`

      - `Type BetaManagedAgentsSystemMessageEventType`

      - `ProcessedAt Time Optional`

        A timestamp in RFC 3339 format

        format: date-time

#### Example

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
	betaManagedAgentsSendSessionEvents, err := client.Beta.Sessions.Events.Send(
		context.TODO(),
		"sesn_011CZkZAtmR3yMPDzynEDxu7",
		anthropic.BetaSessionEventSendParams{
			Events: []anthropic.BetaManagedAgentsEventParamsUnion{anthropic.BetaManagedAgentsEventParamsUnion{
				OfUserMessage: &anthropic.BetaManagedAgentsUserMessageEventParams{
					Content: []anthropic.BetaManagedAgentsUserMessageEventParamsContentUnion{anthropic.BetaManagedAgentsUserMessageEventParamsContentUnion{
						OfText: &anthropic.BetaManagedAgentsTextBlockParam{
							Text: "Where is my order #1234?",
							Type: anthropic.BetaManagedAgentsTextBlockTypeText,
						},
					}},
					Type: anthropic.BetaManagedAgentsUserMessageEventParamsTypeUserMessage,
				},
			}},
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaManagedAgentsSendSessionEvents.Data)
}
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message",
      "processed_at": "2026-03-15T10:00:00Z"
    }
  ]
}
```

### Stream Events

`client.Beta.Sessions.Events.Stream(ctx, sessionID, params) (*BetaManagedAgentsStreamSessionEventsUnion, error)`

**GET** `/v1/sessions/{session_id}/events/stream`

Stream Events

#### Parameters

- `sessionID string`

- `params BetaSessionEventStreamParams`

  - `EventDeltas param.Field[[]BetaManagedAgentsDeltaType] Optional`

    Query param: When set, this connection also receives streaming deltas (`event_start`, `event_delta`) while an event is being produced, before the event itself arrives. Deltas are best-effort; when the final event is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no final event — its terminal `span.model_request_end` closes the preview. Accepts one or more event types to preview and may be repeated: `agent.message` streams `content_delta` fragments; `agent.thinking` is start-only — a signal that the agent has begun extended thinking, concluded by the `agent.thinking` event itself. Only previews of the requested event types are sent.

    - `const BetaManagedAgentsDeltaTypeAgentMessage BetaManagedAgentsDeltaType = "agent.message"`

    - `const BetaManagedAgentsDeltaTypeAgentThinking BetaManagedAgentsDeltaType = "agent.thinking"`

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

#### Returns

- `type BetaManagedAgentsStreamSessionEventsUnion interface{…}`

  Server-sent event in the session stream.

  - `type BetaManagedAgentsUserMessageEvent struct{…}`

    A user message event in the session conversation.

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsUserMessageEventContentUnion`

      Array of content blocks comprising the user message.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

        - `Text string`

          The text content.

          minLength: 1

        - `Type BetaManagedAgentsTextBlockType`

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source BetaManagedAgentsImageBlockSourceUnion`

          Union type for image source variants.

          - `type BetaManagedAgentsBase64ImageSource struct{…}`

            Base64-encoded image data.

            - `Data string`

              Base64-encoded image data.

              minLength: 1

            - `MediaType string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

            - `Type BetaManagedAgentsBase64ImageSourceType`

          - `type BetaManagedAgentsURLImageSource struct{…}`

            Image referenced by URL.

            - `Type BetaManagedAgentsURLImageSourceType`

            - `URL string`

              URL of the image to fetch.

              minLength: 1

          - `type BetaManagedAgentsFileImageSource struct{…}`

            Image referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

              minLength: 1

            - `Type BetaManagedAgentsFileImageSourceType`

        - `Type BetaManagedAgentsImageBlockType`

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source BetaManagedAgentsDocumentBlockSourceUnion`

          Union type for document source variants.

          - `type BetaManagedAgentsBase64DocumentSource struct{…}`

            Base64-encoded document data.

            - `Data string`

              Base64-encoded document data.

              minLength: 1

            - `MediaType string`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

            - `Type BetaManagedAgentsBase64DocumentSourceType`

          - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

            Plain text document content.

            - `Data string`

              The plain text content.

              minLength: 1

            - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

              MIME type of the text content. Must be "text/plain".

            - `Type BetaManagedAgentsPlainTextDocumentSourceType`

          - `type BetaManagedAgentsURLDocumentSource struct{…}`

            Document referenced by URL.

            - `Type BetaManagedAgentsURLDocumentSourceType`

            - `URL string`

              URL of the document to fetch.

              minLength: 1

          - `type BetaManagedAgentsFileDocumentSource struct{…}`

            Document referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

              minLength: 1

            - `Type BetaManagedAgentsFileDocumentSourceType`

        - `Type BetaManagedAgentsDocumentBlockType`

        - `Context string Optional`

          Additional context about the document for the model.

        - `Title string Optional`

          The title of the document.

      - `type BetaManagedAgentsRedactedBlockParam struct{…}`

        Placeholder for content withheld by Anthropic model policy.

        - `Type BetaManagedAgentsRedactedBlockType`

    - `Type BetaManagedAgentsUserMessageEventType`

    - `ProcessedAt Time Optional`

      A timestamp in RFC 3339 format

      format: date-time

  - `type BetaManagedAgentsUserInterruptEvent struct{…}`

    An interrupt event that pauses agent execution and returns control to the user.

    - `ID string`

      Unique identifier for this event.

    - `Type BetaManagedAgentsUserInterruptEventType`

    - `ProcessedAt Time Optional`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string Optional`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `type BetaManagedAgentsUserToolConfirmationEvent struct{…}`

    A tool confirmation event that approves or denies a pending tool execution.

    - `ID string`

      Unique identifier for this event.

    - `Result BetaManagedAgentsUserToolConfirmationEventResult`

      UserToolConfirmationResult enum

      - `const BetaManagedAgentsUserToolConfirmationEventResultAllow BetaManagedAgentsUserToolConfirmationEventResult = "allow"`

      - `const BetaManagedAgentsUserToolConfirmationEventResultDeny BetaManagedAgentsUserToolConfirmationEventResult = "deny"`

    - `ToolUseID string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type BetaManagedAgentsUserToolConfirmationEventType`

    - `DenyMessage string Optional`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `ProcessedAt Time Optional`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string Optional`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `type BetaManagedAgentsUserCustomToolResultEvent struct{…}`

    Event sent by the client providing the result of a custom tool execution.

    - `ID string`

      Unique identifier for this event.

    - `CustomToolUseID string`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type BetaManagedAgentsUserCustomToolResultEventType`

    - `Content []BetaManagedAgentsUserCustomToolResultEventContentUnion Optional`

      The result content returned by the tool.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `type BetaManagedAgentsSearchResultBlock struct{…}`

        A block containing a web search result.

        - `Citations BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `Enabled bool`

            Whether citations are enabled for this search result.

        - `Content []BetaManagedAgentsSearchResultContent`

          Array of text content blocks from the search result.

          - `Text string`

            The text content.

            minLength: 1

          - `Type BetaManagedAgentsSearchResultContentType`

        - `Source string`

          The URL source of the search result.

          minLength: 1

        - `Title string`

          The title of the search result.

          minLength: 1

        - `Type BetaManagedAgentsSearchResultBlockType`

    - `IsError bool Optional`

      Whether the tool execution resulted in an error.

    - `ProcessedAt Time Optional`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string Optional`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `type BetaManagedAgentsAgentCustomToolUseEvent struct{…}`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `ID string`

      Unique identifier for this event.

    - `Input map[string, any]`

      Input parameters for the tool call.

    - `Name string`

      Name of the custom tool being called.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsAgentCustomToolUseEventType`

    - `SessionThreadID string Optional`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `type BetaManagedAgentsAgentMessageEvent struct{…}`

    An agent response event in the session conversation.

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsAgentMessageEventContentUnion`

      Array of text blocks comprising the agent response.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

      - `type BetaManagedAgentsRedactedBlockParam struct{…}`

        Placeholder for content withheld by Anthropic model policy.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsAgentMessageEventType`

  - `type BetaManagedAgentsAgentThinkingEvent struct{…}`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsAgentThinkingEventType`

  - `type BetaManagedAgentsAgentMCPToolUseEvent struct{…}`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `ID string`

      Unique identifier for this event.

    - `Input map[string, any]`

      Input parameters for the tool call.

    - `MCPServerName string`

      Name of the MCP server providing the tool.

    - `Name string`

      Name of the MCP tool being used.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsAgentMCPToolUseEventType`

    - `EvaluatedPermission BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission Optional`

      AgentEvaluatedPermission enum

      - `const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionAllow BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "allow"`

      - `const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionAsk BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "ask"`

      - `const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionDeny BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "deny"`

    - `SessionThreadID string Optional`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `type BetaManagedAgentsAgentMCPToolResultEvent struct{…}`

    Event representing the result of an MCP tool execution.

    - `ID string`

      Unique identifier for this event.

    - `MCPToolUseID string`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsAgentMCPToolResultEventType`

    - `Content []BetaManagedAgentsAgentMCPToolResultEventContentUnion Optional`

      The result content returned by the tool.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `type BetaManagedAgentsSearchResultBlock struct{…}`

        A block containing a web search result.

    - `IsError bool Optional`

      Whether the tool execution resulted in an error.

  - `type BetaManagedAgentsAgentToolUseEvent struct{…}`

    Event emitted when the agent invokes a built-in agent tool.

    - `ID string`

      Unique identifier for this event.

    - `Input map[string, any]`

      Input parameters for the tool call.

    - `Name string`

      Name of the agent tool being used.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsAgentToolUseEventType`

    - `EvaluatedPermission BetaManagedAgentsAgentToolUseEventEvaluatedPermission Optional`

      AgentEvaluatedPermission enum

      - `const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionAllow BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "allow"`

      - `const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionAsk BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "ask"`

      - `const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionDeny BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "deny"`

    - `SessionThreadID string Optional`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `type BetaManagedAgentsAgentToolResultEvent struct{…}`

    Event representing the result of an agent tool execution.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `ToolUseID string`

      The id of the `agent.tool_use` event this result corresponds to.

    - `Type BetaManagedAgentsAgentToolResultEventType`

    - `Content []BetaManagedAgentsAgentToolResultEventContentUnion Optional`

      The result content returned by the tool.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `type BetaManagedAgentsSearchResultBlock struct{…}`

        A block containing a web search result.

    - `IsError bool Optional`

      Whether the tool execution resulted in an error.

  - `type BetaManagedAgentsAgentThreadMessageReceivedEvent struct{…}`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsAgentThreadMessageReceivedEventContentUnion`

      Message content blocks.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `type BetaManagedAgentsRedactedBlockParam struct{…}`

        Placeholder for content withheld by Anthropic model policy.

    - `FromSessionThreadID string`

      Public `sthr_` ID of the thread that sent the message.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsAgentThreadMessageReceivedEventType`

    - `FromAgentName string Optional`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `type BetaManagedAgentsAgentThreadMessageSentEvent struct{…}`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsAgentThreadMessageSentEventContentUnion`

      Message content blocks.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `type BetaManagedAgentsRedactedBlockParam struct{…}`

        Placeholder for content withheld by Anthropic model policy.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `ToSessionThreadID string`

      Public `sthr_` ID of the thread the message was sent to.

    - `Type BetaManagedAgentsAgentThreadMessageSentEventType`

    - `ToAgentName string Optional`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `type BetaManagedAgentsAgentThreadContextCompactedEvent struct{…}`

    Indicates that context compaction (summarization) occurred during the session.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsAgentThreadContextCompactedEventType`

  - `type BetaManagedAgentsSessionErrorEvent struct{…}`

    An error event indicating a problem occurred during session execution.

    - `ID string`

      Unique identifier for this event.

    - `Error BetaManagedAgentsSessionErrorEventErrorUnion`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `type BetaManagedAgentsUnknownError struct{…}`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsUnknownErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type BetaManagedAgentsRetryStatusRetryingType`

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type BetaManagedAgentsRetryStatusExhaustedType`

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type BetaManagedAgentsRetryStatusTerminalType`

        - `Type BetaManagedAgentsUnknownErrorType`

      - `type BetaManagedAgentsModelOverloadedError struct{…}`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsModelOverloadedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type BetaManagedAgentsModelOverloadedErrorType`

      - `type BetaManagedAgentsModelRateLimitedError struct{…}`

        The model request was rate-limited.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsModelRateLimitedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type BetaManagedAgentsModelRateLimitedErrorType`

      - `type BetaManagedAgentsModelRequestFailedError struct{…}`

        A model request failed for a reason other than overload or rate-limiting.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsModelRequestFailedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type BetaManagedAgentsModelRequestFailedErrorType`

      - `type BetaManagedAgentsMCPConnectionFailedError struct{…}`

        Failed to connect to an MCP server.

        - `MCPServerName string`

          Name of the MCP server that failed to connect.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsMCPConnectionFailedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type BetaManagedAgentsMCPConnectionFailedErrorType`

      - `type BetaManagedAgentsMCPAuthenticationFailedError struct{…}`

        Authentication to an MCP server failed.

        - `MCPServerName string`

          Name of the MCP server that failed authentication.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsMCPAuthenticationFailedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type BetaManagedAgentsMCPAuthenticationFailedErrorType`

      - `type BetaManagedAgentsBillingError struct{…}`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsBillingErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type BetaManagedAgentsBillingErrorType`

      - `type BetaManagedAgentsCredentialHostUnreachableError struct{…}`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `CredentialID string`

          ID of the affected credential.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsCredentialHostUnreachableErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type BetaManagedAgentsCredentialHostUnreachableErrorType`

        - `VaultID string`

          ID of the vault containing the affected credential.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSessionErrorEventType`

  - `type BetaManagedAgentsSessionStatusRescheduledEvent struct{…}`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSessionStatusRescheduledEventType`

  - `type BetaManagedAgentsSessionStatusRunningEvent struct{…}`

    Indicates the session is actively running and the agent is working.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSessionStatusRunningEventType`

  - `type BetaManagedAgentsSessionStatusIdleEvent struct{…}`

    Indicates the agent has paused and is awaiting user input.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `StopReason BetaManagedAgentsSessionStatusIdleEventStopReasonUnion`

      The agent completed its turn naturally and is ready for the next user message.

      - `type BetaManagedAgentsSessionEndTurn struct{…}`

        The agent completed its turn naturally and is ready for the next user message.

        - `Type BetaManagedAgentsSessionEndTurnType`

      - `type BetaManagedAgentsSessionRequiresAction struct{…}`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `EventIDs []string`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `Type BetaManagedAgentsSessionRequiresActionType`

      - `type BetaManagedAgentsSessionRetriesExhausted struct{…}`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `Type BetaManagedAgentsSessionRetriesExhaustedType`

      - `type BetaManagedAgentsSessionBudgetReached struct{…}`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `Type BetaManagedAgentsSessionBudgetReachedType`

    - `Type BetaManagedAgentsSessionStatusIdleEventType`

  - `type BetaManagedAgentsSessionStatusTerminatedEvent struct{…}`

    Indicates the session has terminated, either due to an error or completion.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSessionStatusTerminatedEventType`

  - `type BetaManagedAgentsSessionThreadCreatedEvent struct{…}`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the callable agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string`

      Public `sthr_` ID of the newly created thread.

    - `Type BetaManagedAgentsSessionThreadCreatedEventType`

  - `type BetaManagedAgentsSpanOutcomeEvaluationStartEvent struct{…}`

    Emitted when an outcome evaluation cycle begins.

    - `ID string`

      Unique identifier for this event.

    - `Iteration int64`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

      format: int32

    - `OutcomeID string`

      The `outc_` ID of the outcome being evaluated.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSpanOutcomeEvaluationStartEventType`

  - `type BetaManagedAgentsSpanOutcomeEvaluationEndEvent struct{…}`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `ID string`

      Unique identifier for this event.

    - `Explanation string`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `Iteration int64`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `OutcomeEvaluationStartID string`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `OutcomeID string`

      The `outc_` ID of the outcome being evaluated.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Result string`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `Type BetaManagedAgentsSpanOutcomeEvaluationEndEventType`

    - `Usage BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `CacheCreationInputTokens int64`

        Tokens used to create prompt cache in this request.

        format: int32

      - `CacheReadInputTokens int64`

        Tokens read from prompt cache in this request.

        format: int32

      - `InputTokens int64`

        Input tokens consumed by this request.

        format: int32

      - `OutputTokens int64`

        Output tokens generated by this request.

        format: int32

      - `Speed BetaManagedAgentsSpanModelUsageSpeed Optional`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `const BetaManagedAgentsSpanModelUsageSpeedStandard BetaManagedAgentsSpanModelUsageSpeed = "standard"`

        - `const BetaManagedAgentsSpanModelUsageSpeedFast BetaManagedAgentsSpanModelUsageSpeed = "fast"`

  - `type BetaManagedAgentsSpanModelRequestStartEvent struct{…}`

    Emitted when a model request is initiated by the agent.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSpanModelRequestStartEventType`

  - `type BetaManagedAgentsSpanModelRequestEndEvent struct{…}`

    Emitted when a model request completes.

    - `ID string`

      Unique identifier for this event.

    - `IsError bool`

      Whether the model request resulted in an error.

    - `ModelRequestStartID string`

      The id of the corresponding `span.model_request_start` event.

    - `ModelUsage BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSpanModelRequestEndEventType`

  - `type BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent struct{…}`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `ID string`

      Unique identifier for this event.

    - `Iteration int64`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `OutcomeID string`

      The `outc_` ID of the outcome being evaluated.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSpanOutcomeEvaluationOngoingEventType`

  - `type BetaManagedAgentsUserDefineOutcomeEvent struct{…}`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `ID string`

      Unique identifier for this event.

    - `Description string`

      What the agent should produce. Copied from the input event.

    - `MaxIterations int64`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

      format: int32

    - `OutcomeID string`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Rubric BetaManagedAgentsUserDefineOutcomeEventRubricUnion`

      Rubric for grading the quality of an outcome.

      - `type BetaManagedAgentsFileRubric struct{…}`

        Rubric referenced by a file uploaded via the Files API.

        - `FileID string`

          ID of the rubric file.

        - `Type BetaManagedAgentsFileRubricType`

      - `type BetaManagedAgentsTextRubric struct{…}`

        Rubric content provided inline as text.

        - `Content string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `Type BetaManagedAgentsTextRubricType`

    - `Type BetaManagedAgentsUserDefineOutcomeEventType`

  - `type BetaManagedAgentsSessionDeletedEvent struct{…}`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSessionDeletedEventType`

  - `type BetaManagedAgentsSessionThreadStatusRunningEvent struct{…}`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string`

      Public sthr_ ID of the thread that started running.

    - `Type BetaManagedAgentsSessionThreadStatusRunningEventType`

  - `type BetaManagedAgentsSessionThreadStatusIdleEvent struct{…}`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string`

      Public sthr_ ID of the thread that went idle.

    - `StopReason BetaManagedAgentsSessionThreadStatusIdleEventStopReasonUnion`

      The agent completed its turn naturally and is ready for the next user message.

      - `type BetaManagedAgentsSessionEndTurn struct{…}`

        The agent completed its turn naturally and is ready for the next user message.

      - `type BetaManagedAgentsSessionRequiresAction struct{…}`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `type BetaManagedAgentsSessionRetriesExhausted struct{…}`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `type BetaManagedAgentsSessionBudgetReached struct{…}`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

    - `Type BetaManagedAgentsSessionThreadStatusIdleEventType`

  - `type BetaManagedAgentsSessionThreadStatusTerminatedEvent struct{…}`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string`

      Public sthr_ ID of the thread that terminated.

    - `Type BetaManagedAgentsSessionThreadStatusTerminatedEventType`

  - `type BetaManagedAgentsUserToolResultEvent struct{…}`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `ID string`

      Unique identifier for this event.

    - `ToolUseID string`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type BetaManagedAgentsUserToolResultEventType`

    - `Content []BetaManagedAgentsUserToolResultEventContentUnion Optional`

      The result content returned by the tool.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `type BetaManagedAgentsSearchResultBlock struct{…}`

        A block containing a web search result.

    - `IsError bool Optional`

      Whether the tool execution resulted in an error.

    - `ProcessedAt Time Optional`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string Optional`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `type BetaManagedAgentsSessionThreadStatusRescheduledEvent struct{…}`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string`

      Public sthr_ ID of the thread that is retrying.

    - `Type BetaManagedAgentsSessionThreadStatusRescheduledEventType`

  - `type BetaManagedAgentsSessionUpdatedEvent struct{…}`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSessionUpdatedEventType`

    - `Agent BetaManagedAgentsSessionAgent Optional`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `ID string`

      - `Description string`

      - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

        - `Name string`

        - `Type BetaManagedAgentsMCPServerURLDefinitionType`

        - `URL string`

      - `Model BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `ID BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `type BetaManagedAgentsModel string`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `const BetaManagedAgentsModelClaudeSonnet5 BetaManagedAgentsModel = "claude-sonnet-5"`

              High-performance model for coding and agents

            - `const BetaManagedAgentsModelClaudeFable5 BetaManagedAgentsModel = "claude-fable-5"`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `const BetaManagedAgentsModelClaudeOpus5 BetaManagedAgentsModel = "claude-opus-5"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeOpus4_8 BetaManagedAgentsModel = "claude-opus-4-8"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeOpus4_7 BetaManagedAgentsModel = "claude-opus-4-7"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeOpus4_6 BetaManagedAgentsModel = "claude-opus-4-6"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeSonnet4_6 BetaManagedAgentsModel = "claude-sonnet-4-6"`

              Best combination of speed and intelligence

            - `const BetaManagedAgentsModelClaudeHaiku4_5 BetaManagedAgentsModel = "claude-haiku-4-5"`

              Fastest model with near-frontier intelligence

            - `const BetaManagedAgentsModelClaudeHaiku4_5_20251001 BetaManagedAgentsModel = "claude-haiku-4-5-20251001"`

              Fastest model with near-frontier intelligence

            - `const BetaManagedAgentsModelClaudeOpus4_5 BetaManagedAgentsModel = "claude-opus-4-5"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeOpus4_5_20251101 BetaManagedAgentsModel = "claude-opus-4-5-20251101"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeSonnet4_5 BetaManagedAgentsModel = "claude-sonnet-4-5"`

              High-performance model for agents and coding

            - `const BetaManagedAgentsModelClaudeSonnet4_5_20250929 BetaManagedAgentsModel = "claude-sonnet-4-5-20250929"`

              High-performance model for agents and coding

          - `string`

        - `Effort BetaManagedAgentsModelConfigEffortUnion Optional`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `type BetaManagedAgentsEffortLow struct{…}`

            Low effort. Favors latency over reasoning depth.

            - `Type BetaManagedAgentsEffortLowType`

          - `type BetaManagedAgentsEffortMedium struct{…}`

            Medium effort. Balances latency and reasoning depth.

            - `Type BetaManagedAgentsEffortMediumType`

          - `type BetaManagedAgentsEffortHigh struct{…}`

            High effort. Favors reasoning depth.

            - `Type BetaManagedAgentsEffortHighType`

          - `type BetaManagedAgentsEffortXhigh struct{…}`

            Extra-high effort. Not all models accept this level.

            - `Type BetaManagedAgentsEffortXhighType`

          - `type BetaManagedAgentsEffortMax struct{…}`

            Maximum effort. Favors reasoning depth over latency.

            - `Type BetaManagedAgentsEffortMaxType`

        - `InferenceGeo string Optional`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `Speed BetaManagedAgentsModelConfigSpeed Optional`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `const BetaManagedAgentsModelConfigSpeedStandard BetaManagedAgentsModelConfigSpeed = "standard"`

          - `const BetaManagedAgentsModelConfigSpeedFast BetaManagedAgentsModelConfigSpeed = "fast"`

      - `Multiagent BetaManagedAgentsSessionMultiagentCoordinator`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `Agents []BetaManagedAgentsSessionMultiagentCoordinatorAgentUnion`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `type BetaManagedAgentsSessionThreadAgent struct{…}`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `ID string`

            - `Description string`

            - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

              - `Name string`

              - `Type BetaManagedAgentsMCPServerURLDefinitionType`

              - `URL string`

            - `Model BetaManagedAgentsModelConfig`

              Model identifier and configuration.

            - `Name string`

            - `Skills []BetaManagedAgentsSessionThreadAgentSkillUnion`

              - `type BetaManagedAgentsAnthropicSkill struct{…}`

                A resolved Anthropic-managed skill.

                - `SkillID string`

                - `Type BetaManagedAgentsAnthropicSkillType`

                - `Version string`

              - `type BetaManagedAgentsCustomSkill struct{…}`

                A resolved user-created custom skill.

                - `SkillID string`

                - `Type BetaManagedAgentsCustomSkillType`

                - `Version string`

            - `System string`

            - `Tools []BetaManagedAgentsSessionThreadAgentToolUnion`

              - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

                - `Configs []BetaManagedAgentsAgentToolConfigUnion`

                  - `type BetaManagedAgentsBashToolConfig struct{…}`

                    Configuration for the bash tool.

                    - `Enabled bool`

                    - `Name Bash`

                    - `PermissionPolicy BetaManagedAgentsBashToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                        - `Type BetaManagedAgentsAlwaysAllowPolicyType`

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                        - `Type BetaManagedAgentsAlwaysAskPolicyType`

                    - `Type Bash`

                  - `type BetaManagedAgentsEditToolConfig struct{…}`

                    Configuration for the edit tool.

                    - `Enabled bool`

                    - `Name Edit`

                    - `PermissionPolicy BetaManagedAgentsEditToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                    - `Type Edit`

                  - `type BetaManagedAgentsReadToolConfig struct{…}`

                    Configuration for the read tool.

                    - `Enabled bool`

                    - `Name Read`

                    - `PermissionPolicy BetaManagedAgentsReadToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                    - `Type Read`

                  - `type BetaManagedAgentsWriteToolConfig struct{…}`

                    Configuration for the write tool.

                    - `Enabled bool`

                    - `Name Write`

                    - `PermissionPolicy BetaManagedAgentsWriteToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                    - `Type Write`

                  - `type BetaManagedAgentsGlobToolConfig struct{…}`

                    Configuration for the glob tool.

                    - `Enabled bool`

                    - `Name Glob`

                    - `PermissionPolicy BetaManagedAgentsGlobToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                    - `Type Glob`

                  - `type BetaManagedAgentsGrepToolConfig struct{…}`

                    Configuration for the grep tool.

                    - `Enabled bool`

                    - `Name Grep`

                    - `PermissionPolicy BetaManagedAgentsGrepToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                    - `Type Grep`

                  - `type BetaManagedAgentsWebFetchToolConfig struct{…}`

                    Configuration for the web_fetch tool.

                    - `Enabled bool`

                    - `Name WebFetch`

                    - `PermissionPolicy BetaManagedAgentsWebFetchToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                    - `Type WebFetch`

                    - `AllowedDomains []string Optional`

                    - `BlockedDomains []string Optional`

                    - `MaxContentTokens int64 Optional`

                      format: int32

                  - `type BetaManagedAgentsWebSearchToolConfig struct{…}`

                    Configuration for the web_search tool.

                    - `Enabled bool`

                    - `Name WebSearch`

                    - `PermissionPolicy BetaManagedAgentsWebSearchToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                    - `Type WebSearch`

                    - `AllowedDomains []string Optional`

                    - `BlockedDomains []string Optional`

                    - `UserLocation BetaManagedAgentsUserLocation Optional`

                      Approximate user location for search result localization.

                      - `Type Approximate`

                        Location precision. Only "approximate" is supported.

                      - `City string Optional`

                        City name.

                        minLength: 1, maxLength: 255

                      - `Country string Optional`

                        Two-letter ISO 3166-1 country code, uppercase.

                      - `Region string Optional`

                        Region or state name.

                        minLength: 1, maxLength: 255

                      - `Timezone string Optional`

                        IANA timezone identifier, e.g. "America/Los_Angeles".

                        minLength: 1, maxLength: 255

                - `DefaultConfig BetaManagedAgentsAgentToolsetDefaultConfig`

                  Resolved default configuration for agent tools.

                  - `Enabled bool`

                  - `PermissionPolicy BetaManagedAgentsAgentToolsetDefaultConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                - `Type BetaManagedAgentsAgentToolset20260401Type`

              - `type BetaManagedAgentsMCPToolset struct{…}`

                - `Configs []BetaManagedAgentsMCPToolConfig`

                  - `Enabled bool`

                  - `Name string`

                  - `PermissionPolicy BetaManagedAgentsMCPToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                - `DefaultConfig BetaManagedAgentsMCPToolsetDefaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `Enabled bool`

                  - `PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                - `MCPServerName string`

                - `Type BetaManagedAgentsMCPToolsetType`

              - `type BetaManagedAgentsCustomTool struct{…}`

                A custom tool as returned in API responses.

                - `Description string`

                - `InputSchema BetaManagedAgentsCustomToolInputSchema`

                  JSON Schema for custom tool input parameters.

                  - `Type Object`

                  - `Properties map[string, any] Optional`

                  - `Required []string Optional`

                - `Name string`

                - `Type BetaManagedAgentsCustomToolType`

            - `Type BetaManagedAgentsSessionThreadAgentType`

            - `Version int64`

              format: int32

          - `type BetaManagedAgentsAdvisor struct{…}`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `Model string`

              The advisor model id.

            - `Type BetaManagedAgentsAdvisorType`

        - `Type BetaManagedAgentsSessionMultiagentCoordinatorType`

      - `Name string`

      - `Skills []BetaManagedAgentsSessionAgentSkillUnion`

        - `type BetaManagedAgentsAnthropicSkill struct{…}`

          A resolved Anthropic-managed skill.

        - `type BetaManagedAgentsCustomSkill struct{…}`

          A resolved user-created custom skill.

      - `System string`

      - `Tools []BetaManagedAgentsSessionAgentToolUnion`

        - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

        - `type BetaManagedAgentsMCPToolset struct{…}`

        - `type BetaManagedAgentsCustomTool struct{…}`

          A custom tool as returned in API responses.

      - `Type BetaManagedAgentsSessionAgentType`

      - `Version int64`

        format: int32

    - `Budget BetaManagedAgentsBudgetLimit Optional`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `MaxListCost BetaMonetaryAmount`

        A monetary amount in a specific currency.

        - `Amount string`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `Currency BetaCurrency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `Type BetaManagedAgentsBudgetLimitType`

    - `Metadata map[string, string] Optional`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `Title string Optional`

      The session's new title. Present only when the update changed it.

  - `type BetaManagedAgentsStartEvent struct{…}`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `Event BetaManagedAgentsStartEventPreviewUnion`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

      - `type BetaManagedAgentsAgentMessagePreview struct{…}`

        - `ID string`

          The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

        - `Type BetaManagedAgentsAgentMessagePreviewType`

      - `type BetaManagedAgentsAgentThinkingPreview struct{…}`

        - `ID string`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

        - `Type BetaManagedAgentsAgentThinkingPreviewType`

    - `Type BetaManagedAgentsStartEventType`

  - `type BetaManagedAgentsDeltaEvent struct{…}`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `Delta BetaManagedAgentsDeltaContent`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `Content BetaManagedAgentsTextBlock`

        Regular text content.

      - `Type BetaManagedAgentsDeltaContentType`

      - `Index int64 Optional`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

        format: uint32

    - `EventID string`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

    - `Type BetaManagedAgentsDeltaEventType`

  - `type BetaManagedAgentsSystemMessageEvent struct{…}`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsSystemContentBlock`

      System content blocks. Text-only.

      - `Text string`

        The text content.

        minLength: 1

      - `Type BetaManagedAgentsSystemContentBlockType`

    - `Type BetaManagedAgentsSystemMessageEventType`

    - `ProcessedAt Time Optional`

      A timestamp in RFC 3339 format

      format: date-time

  - `type BetaManagedAgentsSessionUsageEvent struct{…}`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSessionUsageEventType`

    - `Usage BetaManagedAgentsSessionUsageSnapshot`

      Point-in-time snapshot of a session's cumulative usage.

      - `ActiveSeconds float64 Optional`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `CacheCreation BetaManagedAgentsCacheCreationUsage Optional`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `Ephemeral1hInputTokens int64 Optional`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `Ephemeral5mInputTokens int64 Optional`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `CacheReadInputTokens int64 Optional`

        Total tokens read from prompt cache.

        format: int32

      - `InputTokens int64 Optional`

        Total input tokens consumed across all turns.

        format: int32

      - `ListCost BetaMonetaryAmount Optional`

        A monetary amount in a specific currency.

      - `OutputTokens int64 Optional`

        Total output tokens generated across all turns.

        format: int32

      - `ServerToolUse BetaManagedAgentsServerToolUsage Optional`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `WebFetchRequests int64 Optional`

          Number of server-executed web fetch requests.

          format: int32

        - `WebSearchRequests int64 Optional`

          Number of server-executed web search requests.

          format: int32

    - `Budget BetaManagedAgentsBudgetLimit Optional`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

- `type BetaManagedAgentsStreamSessionEventsUnion interface{…}`

  Server-sent event in the session stream.

#### Example

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
	stream := client.Beta.Sessions.Events.StreamEvents(
		context.TODO(),
		"sesn_011CZkZAtmR3yMPDzynEDxu7",
		anthropic.BetaSessionEventStreamParams{},
	)
	for stream.Next() {
		fmt.Printf("%+v\n", stream.Current())
	}
	err := stream.Err()
	if err != nil {
		panic(err.Error())
	}
}
```

##### Response (200)

```json
{
  "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
  "content": [
    {
      "text": "Where is my order #1234?",
      "type": "text"
    }
  ],
  "type": "user.message",
  "processed_at": "2026-03-15T10:00:00Z"
}
```

## Sessions › Resources

### Add Session Resource

`client.Beta.Sessions.Resources.Add(ctx, sessionID, params) (*BetaManagedAgentsFileResource, error)`

**POST** `/v1/sessions/{session_id}/resources`

Add Session Resource

#### Parameters

- `sessionID string`

- `params BetaSessionResourceAddParams`

  - `BetaManagedAgentsFileResourceParams param.Field[BetaManagedAgentsFileResourceParamsResp]`

    Body param: Mount a file uploaded via the Files API into the session.

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

#### Returns

- `type BetaManagedAgentsFileResource struct{…}`

  - `ID string`

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `FileID string`

  - `MountPath string`

  - `Type BetaManagedAgentsFileResourceType`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

#### Example

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
	betaManagedAgentsFileResource, err := client.Beta.Sessions.Resources.Add(
		context.TODO(),
		"sesn_011CZkZAtmR3yMPDzynEDxu7",
		anthropic.BetaSessionResourceAddParams{
			BetaManagedAgentsFileResourceParams: anthropic.BetaManagedAgentsFileResourceParams{
				FileID: "file_011CNha8iCJcU1wXNR6q4V8w",
				Type:   anthropic.BetaManagedAgentsFileResourceParamsTypeFile,
			},
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaManagedAgentsFileResource.ID)
}
```

##### Response (200)

```json
{
  "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  "created_at": "2026-03-15T10:00:00Z",
  "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "mount_path": "/uploads/receipt.pdf",
  "type": "file",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

### List Session Resources

`client.Beta.Sessions.Resources.List(ctx, sessionID, params) (*PageCursor[BetaManagedAgentsSessionResourceUnion], error)`

**GET** `/v1/sessions/{session_id}/resources`

List Session Resources

#### Parameters

- `sessionID string`

- `params BetaSessionResourceListParams`

  - `Limit param.Field[int64] Optional`

    Query param: Maximum number of resources to return per page (max 1000). If omitted, returns all resources.

    format: int32

  - `Page param.Field[string] Optional`

    Query param: Opaque cursor from a previous response's next_page field.

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

#### Returns

- `type BetaManagedAgentsSessionResourceUnion interface{…}`

  A memory store attached to an agent session.

  - `type BetaManagedAgentsGitHubRepositoryResource struct{…}`

    - `ID string`

    - `CreatedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `MountPath string`

    - `Type BetaManagedAgentsGitHubRepositoryResourceType`

    - `UpdatedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `URL string`

    - `Checkout BetaManagedAgentsGitHubRepositoryResourceCheckoutUnion Optional`

      - `type BetaManagedAgentsBranchCheckout struct{…}`

        - `Name string`

          Branch name to check out.

          minLength: 1, maxLength: 255

        - `Type BetaManagedAgentsBranchCheckoutType`

      - `type BetaManagedAgentsCommitCheckout struct{…}`

        - `Sha string`

          Full commit SHA to check out.

          minLength: 7, maxLength: 64

        - `Type BetaManagedAgentsCommitCheckoutType`

  - `type BetaManagedAgentsFileResource struct{…}`

    - `ID string`

    - `CreatedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `FileID string`

    - `MountPath string`

    - `Type BetaManagedAgentsFileResourceType`

    - `UpdatedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

  - `type BetaManagedAgentsMemoryStoreResource struct{…}`

    A memory store attached to an agent session.

    - `MemoryStoreID string`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `Type BetaManagedAgentsMemoryStoreResourceType`

    - `Access BetaManagedAgentsMemoryStoreResourceAccess Optional`

      Access mode for an attached memory store.

      - `const BetaManagedAgentsMemoryStoreResourceAccessReadWrite BetaManagedAgentsMemoryStoreResourceAccess = "read_write"`

      - `const BetaManagedAgentsMemoryStoreResourceAccessReadOnly BetaManagedAgentsMemoryStoreResourceAccess = "read_only"`

    - `Description string Optional`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `Instructions string Optional`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      maxLength: 4096

    - `MountPath string Optional`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `Name string Optional`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

#### Example

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
	page, err := client.Beta.Sessions.Resources.List(
		context.TODO(),
		"sesn_011CZkZAtmR3yMPDzynEDxu7",
		anthropic.BetaSessionResourceListParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
}
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
      "created_at": "2026-03-15T10:00:00Z",
      "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
      "mount_path": "/uploads/receipt.pdf",
      "type": "file",
      "updated_at": "2026-03-15T10:00:00Z"
    },
    {
      "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
      "created_at": "2026-03-15T10:00:00Z",
      "mount_path": "/workspace/example-repo",
      "type": "github_repository",
      "updated_at": "2026-03-15T10:00:00Z",
      "url": "https://github.com/example-org/example-repo",
      "checkout": {
        "name": "main",
        "type": "branch"
      }
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

### Get Session Resource

`client.Beta.Sessions.Resources.Get(ctx, resourceID, params) (*BetaSessionResourceGetResponseUnion, error)`

**GET** `/v1/sessions/{session_id}/resources/{resource_id}`

Get Session Resource

#### Parameters

- `resourceID string`

- `params BetaSessionResourceGetParams`

  - `SessionID param.Field[string]`

    Path param: Path parameter session_id

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

#### Returns

- `type BetaSessionResourceGetResponseUnion interface{…}`

  The requested session resource.

  - `type BetaManagedAgentsGitHubRepositoryResource struct{…}`

    - `ID string`

    - `CreatedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `MountPath string`

    - `Type BetaManagedAgentsGitHubRepositoryResourceType`

    - `UpdatedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `URL string`

    - `Checkout BetaManagedAgentsGitHubRepositoryResourceCheckoutUnion Optional`

      - `type BetaManagedAgentsBranchCheckout struct{…}`

        - `Name string`

          Branch name to check out.

          minLength: 1, maxLength: 255

        - `Type BetaManagedAgentsBranchCheckoutType`

      - `type BetaManagedAgentsCommitCheckout struct{…}`

        - `Sha string`

          Full commit SHA to check out.

          minLength: 7, maxLength: 64

        - `Type BetaManagedAgentsCommitCheckoutType`

  - `type BetaManagedAgentsFileResource struct{…}`

    - `ID string`

    - `CreatedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `FileID string`

    - `MountPath string`

    - `Type BetaManagedAgentsFileResourceType`

    - `UpdatedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

  - `type BetaManagedAgentsMemoryStoreResource struct{…}`

    A memory store attached to an agent session.

    - `MemoryStoreID string`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `Type BetaManagedAgentsMemoryStoreResourceType`

    - `Access BetaManagedAgentsMemoryStoreResourceAccess Optional`

      Access mode for an attached memory store.

      - `const BetaManagedAgentsMemoryStoreResourceAccessReadWrite BetaManagedAgentsMemoryStoreResourceAccess = "read_write"`

      - `const BetaManagedAgentsMemoryStoreResourceAccessReadOnly BetaManagedAgentsMemoryStoreResourceAccess = "read_only"`

    - `Description string Optional`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `Instructions string Optional`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      maxLength: 4096

    - `MountPath string Optional`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `Name string Optional`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

#### Example

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
	resource, err := client.Beta.Sessions.Resources.Get(
		context.TODO(),
		"sesrsc_011CZkZBJq5dWxk9fVLNcPht",
		anthropic.BetaSessionResourceGetParams{
			SessionID: "sesn_011CZkZAtmR3yMPDzynEDxu7",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", resource)
}
```

##### Response (200)

```json
{
  "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
  "created_at": "2026-03-15T10:00:00Z",
  "mount_path": "/workspace/example-repo",
  "type": "github_repository",
  "updated_at": "2026-03-15T10:00:00Z",
  "url": "https://github.com/example-org/example-repo",
  "checkout": {
    "name": "main",
    "type": "branch"
  }
}
```

### Update Session Resource

`client.Beta.Sessions.Resources.Update(ctx, resourceID, params) (*BetaSessionResourceUpdateResponseUnion, error)`

**POST** `/v1/sessions/{session_id}/resources/{resource_id}`

Update Session Resource

#### Parameters

- `resourceID string`

- `params BetaSessionResourceUpdateParams`

  - `SessionID param.Field[string]`

    Path param: Path parameter session_id

  - `AuthorizationToken param.Field[string]`

    Body param: New authorization token for the resource. Currently only `github_repository` resources support token rotation.

    minLength: 1, maxLength: 4096

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

#### Returns

- `type BetaSessionResourceUpdateResponseUnion interface{…}`

  The updated session resource.

  - `type BetaManagedAgentsGitHubRepositoryResource struct{…}`

    - `ID string`

    - `CreatedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `MountPath string`

    - `Type BetaManagedAgentsGitHubRepositoryResourceType`

    - `UpdatedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `URL string`

    - `Checkout BetaManagedAgentsGitHubRepositoryResourceCheckoutUnion Optional`

      - `type BetaManagedAgentsBranchCheckout struct{…}`

        - `Name string`

          Branch name to check out.

          minLength: 1, maxLength: 255

        - `Type BetaManagedAgentsBranchCheckoutType`

      - `type BetaManagedAgentsCommitCheckout struct{…}`

        - `Sha string`

          Full commit SHA to check out.

          minLength: 7, maxLength: 64

        - `Type BetaManagedAgentsCommitCheckoutType`

  - `type BetaManagedAgentsFileResource struct{…}`

    - `ID string`

    - `CreatedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `FileID string`

    - `MountPath string`

    - `Type BetaManagedAgentsFileResourceType`

    - `UpdatedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

  - `type BetaManagedAgentsMemoryStoreResource struct{…}`

    A memory store attached to an agent session.

    - `MemoryStoreID string`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `Type BetaManagedAgentsMemoryStoreResourceType`

    - `Access BetaManagedAgentsMemoryStoreResourceAccess Optional`

      Access mode for an attached memory store.

      - `const BetaManagedAgentsMemoryStoreResourceAccessReadWrite BetaManagedAgentsMemoryStoreResourceAccess = "read_write"`

      - `const BetaManagedAgentsMemoryStoreResourceAccessReadOnly BetaManagedAgentsMemoryStoreResourceAccess = "read_only"`

    - `Description string Optional`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `Instructions string Optional`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      maxLength: 4096

    - `MountPath string Optional`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `Name string Optional`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

#### Example

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
	resource, err := client.Beta.Sessions.Resources.Update(
		context.TODO(),
		"sesrsc_011CZkZBJq5dWxk9fVLNcPht",
		anthropic.BetaSessionResourceUpdateParams{
			SessionID:          "sesn_011CZkZAtmR3yMPDzynEDxu7",
			AuthorizationToken: "ghp_exampletoken",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", resource)
}
```

##### Response (200)

```json
{
  "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
  "created_at": "2026-03-15T10:00:00Z",
  "mount_path": "/workspace/example-repo",
  "type": "github_repository",
  "updated_at": "2026-03-15T10:00:00Z",
  "url": "https://github.com/example-org/example-repo",
  "checkout": {
    "name": "main",
    "type": "branch"
  }
}
```

### Delete Session Resource

`client.Beta.Sessions.Resources.Delete(ctx, resourceID, params) (*BetaManagedAgentsDeleteSessionResource, error)`

**DELETE** `/v1/sessions/{session_id}/resources/{resource_id}`

Delete Session Resource

#### Parameters

- `resourceID string`

- `params BetaSessionResourceDeleteParams`

  - `SessionID param.Field[string]`

    Path param: Path parameter session_id

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

#### Returns

- `type BetaManagedAgentsDeleteSessionResource struct{…}`

  Confirmation of resource deletion.

  - `ID string`

  - `Type BetaManagedAgentsDeleteSessionResourceType`

#### Example

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
	betaManagedAgentsDeleteSessionResource, err := client.Beta.Sessions.Resources.Delete(
		context.TODO(),
		"sesrsc_011CZkZBJq5dWxk9fVLNcPht",
		anthropic.BetaSessionResourceDeleteParams{
			SessionID: "sesn_011CZkZAtmR3yMPDzynEDxu7",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaManagedAgentsDeleteSessionResource.ID)
}
```

##### Response (200)

```json
{
  "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  "type": "session_resource_deleted"
}
```

## Sessions › Threads

### List Session Threads

`client.Beta.Sessions.Threads.List(ctx, sessionID, params) (*PageCursor[BetaManagedAgentsSessionThread], error)`

**GET** `/v1/sessions/{session_id}/threads`

List Session Threads

#### Parameters

- `sessionID string`

- `params BetaSessionThreadListParams`

  - `Limit param.Field[int64] Optional`

    Query param: Maximum results per page. Defaults to 1000.

    format: int32

  - `Page param.Field[string] Optional`

    Query param: Opaque pagination cursor from a previous response's next_page. Forward-only.

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

#### Returns

- `type BetaManagedAgentsSessionThread struct{…}`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `ID string`

    Unique identifier for this thread.

  - `Agent BetaManagedAgentsSessionThreadAgentUnion`

    The resolved agent a session thread runs: a saved-agent snapshot, the platform advisor entry, or an inline-defined (ephemeral) agent snapshot.

    - `type BetaManagedAgentsSessionThreadAgent struct{…}`

      Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

      - `ID string`

      - `Description string`

      - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

        - `Name string`

        - `Type BetaManagedAgentsMCPServerURLDefinitionType`

        - `URL string`

      - `Model BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `ID BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `type BetaManagedAgentsModel string`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `const BetaManagedAgentsModelClaudeSonnet5 BetaManagedAgentsModel = "claude-sonnet-5"`

              High-performance model for coding and agents

            - `const BetaManagedAgentsModelClaudeFable5 BetaManagedAgentsModel = "claude-fable-5"`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `const BetaManagedAgentsModelClaudeOpus5 BetaManagedAgentsModel = "claude-opus-5"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeOpus4_8 BetaManagedAgentsModel = "claude-opus-4-8"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeOpus4_7 BetaManagedAgentsModel = "claude-opus-4-7"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeOpus4_6 BetaManagedAgentsModel = "claude-opus-4-6"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeSonnet4_6 BetaManagedAgentsModel = "claude-sonnet-4-6"`

              Best combination of speed and intelligence

            - `const BetaManagedAgentsModelClaudeHaiku4_5 BetaManagedAgentsModel = "claude-haiku-4-5"`

              Fastest model with near-frontier intelligence

            - `const BetaManagedAgentsModelClaudeHaiku4_5_20251001 BetaManagedAgentsModel = "claude-haiku-4-5-20251001"`

              Fastest model with near-frontier intelligence

            - `const BetaManagedAgentsModelClaudeOpus4_5 BetaManagedAgentsModel = "claude-opus-4-5"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeOpus4_5_20251101 BetaManagedAgentsModel = "claude-opus-4-5-20251101"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeSonnet4_5 BetaManagedAgentsModel = "claude-sonnet-4-5"`

              High-performance model for agents and coding

            - `const BetaManagedAgentsModelClaudeSonnet4_5_20250929 BetaManagedAgentsModel = "claude-sonnet-4-5-20250929"`

              High-performance model for agents and coding

          - `string`

        - `Effort BetaManagedAgentsModelConfigEffortUnion Optional`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `type BetaManagedAgentsEffortLow struct{…}`

            Low effort. Favors latency over reasoning depth.

            - `Type BetaManagedAgentsEffortLowType`

          - `type BetaManagedAgentsEffortMedium struct{…}`

            Medium effort. Balances latency and reasoning depth.

            - `Type BetaManagedAgentsEffortMediumType`

          - `type BetaManagedAgentsEffortHigh struct{…}`

            High effort. Favors reasoning depth.

            - `Type BetaManagedAgentsEffortHighType`

          - `type BetaManagedAgentsEffortXhigh struct{…}`

            Extra-high effort. Not all models accept this level.

            - `Type BetaManagedAgentsEffortXhighType`

          - `type BetaManagedAgentsEffortMax struct{…}`

            Maximum effort. Favors reasoning depth over latency.

            - `Type BetaManagedAgentsEffortMaxType`

        - `InferenceGeo string Optional`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `Speed BetaManagedAgentsModelConfigSpeed Optional`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `const BetaManagedAgentsModelConfigSpeedStandard BetaManagedAgentsModelConfigSpeed = "standard"`

          - `const BetaManagedAgentsModelConfigSpeedFast BetaManagedAgentsModelConfigSpeed = "fast"`

      - `Name string`

      - `Skills []BetaManagedAgentsSessionThreadAgentSkillUnion`

        - `type BetaManagedAgentsAnthropicSkill struct{…}`

          A resolved Anthropic-managed skill.

          - `SkillID string`

          - `Type BetaManagedAgentsAnthropicSkillType`

          - `Version string`

        - `type BetaManagedAgentsCustomSkill struct{…}`

          A resolved user-created custom skill.

          - `SkillID string`

          - `Type BetaManagedAgentsCustomSkillType`

          - `Version string`

      - `System string`

      - `Tools []BetaManagedAgentsSessionThreadAgentToolUnion`

        - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

          - `Configs []BetaManagedAgentsAgentToolConfigUnion`

            - `type BetaManagedAgentsBashToolConfig struct{…}`

              Configuration for the bash tool.

              - `Enabled bool`

              - `Name Bash`

              - `PermissionPolicy BetaManagedAgentsBashToolConfigPermissionPolicyUnion`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                  - `Type BetaManagedAgentsAlwaysAllowPolicyType`

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

                  - `Type BetaManagedAgentsAlwaysAskPolicyType`

              - `Type Bash`

            - `type BetaManagedAgentsEditToolConfig struct{…}`

              Configuration for the edit tool.

              - `Enabled bool`

              - `Name Edit`

              - `PermissionPolicy BetaManagedAgentsEditToolConfigPermissionPolicyUnion`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

              - `Type Edit`

            - `type BetaManagedAgentsReadToolConfig struct{…}`

              Configuration for the read tool.

              - `Enabled bool`

              - `Name Read`

              - `PermissionPolicy BetaManagedAgentsReadToolConfigPermissionPolicyUnion`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

              - `Type Read`

            - `type BetaManagedAgentsWriteToolConfig struct{…}`

              Configuration for the write tool.

              - `Enabled bool`

              - `Name Write`

              - `PermissionPolicy BetaManagedAgentsWriteToolConfigPermissionPolicyUnion`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

              - `Type Write`

            - `type BetaManagedAgentsGlobToolConfig struct{…}`

              Configuration for the glob tool.

              - `Enabled bool`

              - `Name Glob`

              - `PermissionPolicy BetaManagedAgentsGlobToolConfigPermissionPolicyUnion`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

              - `Type Glob`

            - `type BetaManagedAgentsGrepToolConfig struct{…}`

              Configuration for the grep tool.

              - `Enabled bool`

              - `Name Grep`

              - `PermissionPolicy BetaManagedAgentsGrepToolConfigPermissionPolicyUnion`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

              - `Type Grep`

            - `type BetaManagedAgentsWebFetchToolConfig struct{…}`

              Configuration for the web_fetch tool.

              - `Enabled bool`

              - `Name WebFetch`

              - `PermissionPolicy BetaManagedAgentsWebFetchToolConfigPermissionPolicyUnion`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

              - `Type WebFetch`

              - `AllowedDomains []string Optional`

              - `BlockedDomains []string Optional`

              - `MaxContentTokens int64 Optional`

                format: int32

            - `type BetaManagedAgentsWebSearchToolConfig struct{…}`

              Configuration for the web_search tool.

              - `Enabled bool`

              - `Name WebSearch`

              - `PermissionPolicy BetaManagedAgentsWebSearchToolConfigPermissionPolicyUnion`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

              - `Type WebSearch`

              - `AllowedDomains []string Optional`

              - `BlockedDomains []string Optional`

              - `UserLocation BetaManagedAgentsUserLocation Optional`

                Approximate user location for search result localization.

                - `Type Approximate`

                  Location precision. Only "approximate" is supported.

                - `City string Optional`

                  City name.

                  minLength: 1, maxLength: 255

                - `Country string Optional`

                  Two-letter ISO 3166-1 country code, uppercase.

                - `Region string Optional`

                  Region or state name.

                  minLength: 1, maxLength: 255

                - `Timezone string Optional`

                  IANA timezone identifier, e.g. "America/Los_Angeles".

                  minLength: 1, maxLength: 255

          - `DefaultConfig BetaManagedAgentsAgentToolsetDefaultConfig`

            Resolved default configuration for agent tools.

            - `Enabled bool`

            - `PermissionPolicy BetaManagedAgentsAgentToolsetDefaultConfigPermissionPolicyUnion`

              Permission policy for tool execution.

              - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                Tool calls are automatically approved without user confirmation.

              - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                Tool calls require user confirmation before execution.

          - `Type BetaManagedAgentsAgentToolset20260401Type`

        - `type BetaManagedAgentsMCPToolset struct{…}`

          - `Configs []BetaManagedAgentsMCPToolConfig`

            - `Enabled bool`

            - `Name string`

            - `PermissionPolicy BetaManagedAgentsMCPToolConfigPermissionPolicyUnion`

              Permission policy for tool execution.

              - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                Tool calls are automatically approved without user confirmation.

              - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                Tool calls require user confirmation before execution.

          - `DefaultConfig BetaManagedAgentsMCPToolsetDefaultConfig`

            Resolved default configuration for all tools from an MCP server.

            - `Enabled bool`

            - `PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigPermissionPolicyUnion`

              Permission policy for tool execution.

              - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                Tool calls are automatically approved without user confirmation.

              - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                Tool calls require user confirmation before execution.

          - `MCPServerName string`

          - `Type BetaManagedAgentsMCPToolsetType`

        - `type BetaManagedAgentsCustomTool struct{…}`

          A custom tool as returned in API responses.

          - `Description string`

          - `InputSchema BetaManagedAgentsCustomToolInputSchema`

            JSON Schema for custom tool input parameters.

            - `Type Object`

            - `Properties map[string, any] Optional`

            - `Required []string Optional`

          - `Name string`

          - `Type BetaManagedAgentsCustomToolType`

      - `Type BetaManagedAgentsSessionThreadAgentType`

      - `Version int64`

        format: int32

    - `type BetaManagedAgentsAdvisor struct{…}`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `Model string`

        The advisor model id.

      - `Type BetaManagedAgentsAdvisorType`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `ParentThreadID string`

    Parent thread that spawned this thread. Null for the primary thread.

  - `SessionID string`

    The session this thread belongs to.

  - `Stats BetaManagedAgentsSessionThreadStats`

    Timing statistics for a session thread.

    - `ActiveSeconds float64 Optional`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

      format: double

    - `DurationSeconds float64 Optional`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

      format: double

    - `StartupSeconds float64 Optional`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

      format: double

  - `Status BetaManagedAgentsSessionThreadStatus`

    SessionThreadStatus enum

    - `const BetaManagedAgentsSessionThreadStatusRunning BetaManagedAgentsSessionThreadStatus = "running"`

    - `const BetaManagedAgentsSessionThreadStatusIdle BetaManagedAgentsSessionThreadStatus = "idle"`

    - `const BetaManagedAgentsSessionThreadStatusRescheduling BetaManagedAgentsSessionThreadStatus = "rescheduling"`

    - `const BetaManagedAgentsSessionThreadStatusTerminated BetaManagedAgentsSessionThreadStatus = "terminated"`

  - `Type BetaManagedAgentsSessionThreadType`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `Usage BetaManagedAgentsSessionThreadUsage`

    Cumulative token usage for a session thread across all turns.

    - `ActiveSeconds float64 Optional`

      Cumulative time in seconds this thread spent in running status. Equal to `stats.active_seconds`; surfaced here so a thread's usage carries every quantity its cost is priced on.

      format: double

    - `CacheCreation BetaManagedAgentsCacheCreationUsage Optional`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `Ephemeral1hInputTokens int64 Optional`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `Ephemeral5mInputTokens int64 Optional`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `CacheReadInputTokens int64 Optional`

      Total tokens read from prompt cache.

      format: int32

    - `InputTokens int64 Optional`

      Total input tokens consumed across all turns.

      format: int32

    - `ListCost BetaMonetaryAmount Optional`

      A monetary amount in a specific currency.

      - `Amount string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `Currency BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `OutputTokens int64 Optional`

      Total output tokens generated across all turns.

      format: int32

    - `ServerToolUse BetaManagedAgentsServerToolUsage Optional`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `WebFetchRequests int64 Optional`

        Number of server-executed web fetch requests.

        format: int32

      - `WebSearchRequests int64 Optional`

        Number of server-executed web search requests.

        format: int32

#### Example

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
	page, err := client.Beta.Sessions.Threads.List(
		context.TODO(),
		"sesn_011CZkZAtmR3yMPDzynEDxu7",
		anthropic.BetaSessionThreadListParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
}
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "sthr_011CZkZVWa6oIjw0rgXZpnBt",
      "agent": {
        "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
        "description": "A focused research subagent.",
        "mcp_servers": [
          {
            "name": "example-mcp",
            "type": "url",
            "url": "https://example-server.modelcontextprotocol.io/sse"
          }
        ],
        "model": {
          "id": "claude-opus-5",
          "effort": {
            "type": "low"
          },
          "inference_geo": "inference_geo",
          "speed": "standard"
        },
        "name": "Researcher",
        "skills": [
          {
            "skill_id": "xlsx",
            "type": "anthropic",
            "version": "1"
          }
        ],
        "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
        "tools": [
          {
            "configs": [
              {
                "enabled": true,
                "name": "bash",
                "permission_policy": {
                  "type": "always_allow"
                },
                "type": "bash"
              }
            ],
            "default_config": {
              "enabled": true,
              "permission_policy": {
                "type": "always_ask"
              }
            },
            "type": "agent_toolset_20260401"
          }
        ],
        "type": "agent",
        "version": 1
      },
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "parent_thread_id": null,
      "session_id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
      "stats": {
        "active_seconds": 0,
        "duration_seconds": 0,
        "startup_seconds": 0
      },
      "status": "idle",
      "type": "session_thread",
      "updated_at": "2026-03-15T10:00:00Z",
      "usage": {
        "active_seconds": 0,
        "cache_creation": {
          "ephemeral_1h_input_tokens": 0,
          "ephemeral_5m_input_tokens": 0
        },
        "cache_read_input_tokens": 0,
        "input_tokens": 0,
        "list_cost": {
          "amount": "2500",
          "currency": "USD"
        },
        "output_tokens": 0,
        "server_tool_use": {
          "web_fetch_requests": 0,
          "web_search_requests": 3
        }
      }
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

### Get Session Thread

`client.Beta.Sessions.Threads.Get(ctx, threadID, params) (*BetaManagedAgentsSessionThread, error)`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}`

Get Session Thread

#### Parameters

- `threadID string`

- `params BetaSessionThreadGetParams`

  - `SessionID param.Field[string]`

    Path param: Path parameter session_id

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

#### Returns

- `type BetaManagedAgentsSessionThread struct{…}`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `ID string`

    Unique identifier for this thread.

  - `Agent BetaManagedAgentsSessionThreadAgentUnion`

    The resolved agent a session thread runs: a saved-agent snapshot, the platform advisor entry, or an inline-defined (ephemeral) agent snapshot.

    - `type BetaManagedAgentsSessionThreadAgent struct{…}`

      Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

      - `ID string`

      - `Description string`

      - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

        - `Name string`

        - `Type BetaManagedAgentsMCPServerURLDefinitionType`

        - `URL string`

      - `Model BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `ID BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `type BetaManagedAgentsModel string`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `const BetaManagedAgentsModelClaudeSonnet5 BetaManagedAgentsModel = "claude-sonnet-5"`

              High-performance model for coding and agents

            - `const BetaManagedAgentsModelClaudeFable5 BetaManagedAgentsModel = "claude-fable-5"`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `const BetaManagedAgentsModelClaudeOpus5 BetaManagedAgentsModel = "claude-opus-5"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeOpus4_8 BetaManagedAgentsModel = "claude-opus-4-8"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeOpus4_7 BetaManagedAgentsModel = "claude-opus-4-7"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeOpus4_6 BetaManagedAgentsModel = "claude-opus-4-6"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeSonnet4_6 BetaManagedAgentsModel = "claude-sonnet-4-6"`

              Best combination of speed and intelligence

            - `const BetaManagedAgentsModelClaudeHaiku4_5 BetaManagedAgentsModel = "claude-haiku-4-5"`

              Fastest model with near-frontier intelligence

            - `const BetaManagedAgentsModelClaudeHaiku4_5_20251001 BetaManagedAgentsModel = "claude-haiku-4-5-20251001"`

              Fastest model with near-frontier intelligence

            - `const BetaManagedAgentsModelClaudeOpus4_5 BetaManagedAgentsModel = "claude-opus-4-5"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeOpus4_5_20251101 BetaManagedAgentsModel = "claude-opus-4-5-20251101"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeSonnet4_5 BetaManagedAgentsModel = "claude-sonnet-4-5"`

              High-performance model for agents and coding

            - `const BetaManagedAgentsModelClaudeSonnet4_5_20250929 BetaManagedAgentsModel = "claude-sonnet-4-5-20250929"`

              High-performance model for agents and coding

          - `string`

        - `Effort BetaManagedAgentsModelConfigEffortUnion Optional`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `type BetaManagedAgentsEffortLow struct{…}`

            Low effort. Favors latency over reasoning depth.

            - `Type BetaManagedAgentsEffortLowType`

          - `type BetaManagedAgentsEffortMedium struct{…}`

            Medium effort. Balances latency and reasoning depth.

            - `Type BetaManagedAgentsEffortMediumType`

          - `type BetaManagedAgentsEffortHigh struct{…}`

            High effort. Favors reasoning depth.

            - `Type BetaManagedAgentsEffortHighType`

          - `type BetaManagedAgentsEffortXhigh struct{…}`

            Extra-high effort. Not all models accept this level.

            - `Type BetaManagedAgentsEffortXhighType`

          - `type BetaManagedAgentsEffortMax struct{…}`

            Maximum effort. Favors reasoning depth over latency.

            - `Type BetaManagedAgentsEffortMaxType`

        - `InferenceGeo string Optional`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `Speed BetaManagedAgentsModelConfigSpeed Optional`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `const BetaManagedAgentsModelConfigSpeedStandard BetaManagedAgentsModelConfigSpeed = "standard"`

          - `const BetaManagedAgentsModelConfigSpeedFast BetaManagedAgentsModelConfigSpeed = "fast"`

      - `Name string`

      - `Skills []BetaManagedAgentsSessionThreadAgentSkillUnion`

        - `type BetaManagedAgentsAnthropicSkill struct{…}`

          A resolved Anthropic-managed skill.

          - `SkillID string`

          - `Type BetaManagedAgentsAnthropicSkillType`

          - `Version string`

        - `type BetaManagedAgentsCustomSkill struct{…}`

          A resolved user-created custom skill.

          - `SkillID string`

          - `Type BetaManagedAgentsCustomSkillType`

          - `Version string`

      - `System string`

      - `Tools []BetaManagedAgentsSessionThreadAgentToolUnion`

        - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

          - `Configs []BetaManagedAgentsAgentToolConfigUnion`

            - `type BetaManagedAgentsBashToolConfig struct{…}`

              Configuration for the bash tool.

              - `Enabled bool`

              - `Name Bash`

              - `PermissionPolicy BetaManagedAgentsBashToolConfigPermissionPolicyUnion`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                  - `Type BetaManagedAgentsAlwaysAllowPolicyType`

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

                  - `Type BetaManagedAgentsAlwaysAskPolicyType`

              - `Type Bash`

            - `type BetaManagedAgentsEditToolConfig struct{…}`

              Configuration for the edit tool.

              - `Enabled bool`

              - `Name Edit`

              - `PermissionPolicy BetaManagedAgentsEditToolConfigPermissionPolicyUnion`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

              - `Type Edit`

            - `type BetaManagedAgentsReadToolConfig struct{…}`

              Configuration for the read tool.

              - `Enabled bool`

              - `Name Read`

              - `PermissionPolicy BetaManagedAgentsReadToolConfigPermissionPolicyUnion`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

              - `Type Read`

            - `type BetaManagedAgentsWriteToolConfig struct{…}`

              Configuration for the write tool.

              - `Enabled bool`

              - `Name Write`

              - `PermissionPolicy BetaManagedAgentsWriteToolConfigPermissionPolicyUnion`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

              - `Type Write`

            - `type BetaManagedAgentsGlobToolConfig struct{…}`

              Configuration for the glob tool.

              - `Enabled bool`

              - `Name Glob`

              - `PermissionPolicy BetaManagedAgentsGlobToolConfigPermissionPolicyUnion`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

              - `Type Glob`

            - `type BetaManagedAgentsGrepToolConfig struct{…}`

              Configuration for the grep tool.

              - `Enabled bool`

              - `Name Grep`

              - `PermissionPolicy BetaManagedAgentsGrepToolConfigPermissionPolicyUnion`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

              - `Type Grep`

            - `type BetaManagedAgentsWebFetchToolConfig struct{…}`

              Configuration for the web_fetch tool.

              - `Enabled bool`

              - `Name WebFetch`

              - `PermissionPolicy BetaManagedAgentsWebFetchToolConfigPermissionPolicyUnion`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

              - `Type WebFetch`

              - `AllowedDomains []string Optional`

              - `BlockedDomains []string Optional`

              - `MaxContentTokens int64 Optional`

                format: int32

            - `type BetaManagedAgentsWebSearchToolConfig struct{…}`

              Configuration for the web_search tool.

              - `Enabled bool`

              - `Name WebSearch`

              - `PermissionPolicy BetaManagedAgentsWebSearchToolConfigPermissionPolicyUnion`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

              - `Type WebSearch`

              - `AllowedDomains []string Optional`

              - `BlockedDomains []string Optional`

              - `UserLocation BetaManagedAgentsUserLocation Optional`

                Approximate user location for search result localization.

                - `Type Approximate`

                  Location precision. Only "approximate" is supported.

                - `City string Optional`

                  City name.

                  minLength: 1, maxLength: 255

                - `Country string Optional`

                  Two-letter ISO 3166-1 country code, uppercase.

                - `Region string Optional`

                  Region or state name.

                  minLength: 1, maxLength: 255

                - `Timezone string Optional`

                  IANA timezone identifier, e.g. "America/Los_Angeles".

                  minLength: 1, maxLength: 255

          - `DefaultConfig BetaManagedAgentsAgentToolsetDefaultConfig`

            Resolved default configuration for agent tools.

            - `Enabled bool`

            - `PermissionPolicy BetaManagedAgentsAgentToolsetDefaultConfigPermissionPolicyUnion`

              Permission policy for tool execution.

              - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                Tool calls are automatically approved without user confirmation.

              - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                Tool calls require user confirmation before execution.

          - `Type BetaManagedAgentsAgentToolset20260401Type`

        - `type BetaManagedAgentsMCPToolset struct{…}`

          - `Configs []BetaManagedAgentsMCPToolConfig`

            - `Enabled bool`

            - `Name string`

            - `PermissionPolicy BetaManagedAgentsMCPToolConfigPermissionPolicyUnion`

              Permission policy for tool execution.

              - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                Tool calls are automatically approved without user confirmation.

              - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                Tool calls require user confirmation before execution.

          - `DefaultConfig BetaManagedAgentsMCPToolsetDefaultConfig`

            Resolved default configuration for all tools from an MCP server.

            - `Enabled bool`

            - `PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigPermissionPolicyUnion`

              Permission policy for tool execution.

              - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                Tool calls are automatically approved without user confirmation.

              - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                Tool calls require user confirmation before execution.

          - `MCPServerName string`

          - `Type BetaManagedAgentsMCPToolsetType`

        - `type BetaManagedAgentsCustomTool struct{…}`

          A custom tool as returned in API responses.

          - `Description string`

          - `InputSchema BetaManagedAgentsCustomToolInputSchema`

            JSON Schema for custom tool input parameters.

            - `Type Object`

            - `Properties map[string, any] Optional`

            - `Required []string Optional`

          - `Name string`

          - `Type BetaManagedAgentsCustomToolType`

      - `Type BetaManagedAgentsSessionThreadAgentType`

      - `Version int64`

        format: int32

    - `type BetaManagedAgentsAdvisor struct{…}`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `Model string`

        The advisor model id.

      - `Type BetaManagedAgentsAdvisorType`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `ParentThreadID string`

    Parent thread that spawned this thread. Null for the primary thread.

  - `SessionID string`

    The session this thread belongs to.

  - `Stats BetaManagedAgentsSessionThreadStats`

    Timing statistics for a session thread.

    - `ActiveSeconds float64 Optional`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

      format: double

    - `DurationSeconds float64 Optional`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

      format: double

    - `StartupSeconds float64 Optional`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

      format: double

  - `Status BetaManagedAgentsSessionThreadStatus`

    SessionThreadStatus enum

    - `const BetaManagedAgentsSessionThreadStatusRunning BetaManagedAgentsSessionThreadStatus = "running"`

    - `const BetaManagedAgentsSessionThreadStatusIdle BetaManagedAgentsSessionThreadStatus = "idle"`

    - `const BetaManagedAgentsSessionThreadStatusRescheduling BetaManagedAgentsSessionThreadStatus = "rescheduling"`

    - `const BetaManagedAgentsSessionThreadStatusTerminated BetaManagedAgentsSessionThreadStatus = "terminated"`

  - `Type BetaManagedAgentsSessionThreadType`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `Usage BetaManagedAgentsSessionThreadUsage`

    Cumulative token usage for a session thread across all turns.

    - `ActiveSeconds float64 Optional`

      Cumulative time in seconds this thread spent in running status. Equal to `stats.active_seconds`; surfaced here so a thread's usage carries every quantity its cost is priced on.

      format: double

    - `CacheCreation BetaManagedAgentsCacheCreationUsage Optional`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `Ephemeral1hInputTokens int64 Optional`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `Ephemeral5mInputTokens int64 Optional`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `CacheReadInputTokens int64 Optional`

      Total tokens read from prompt cache.

      format: int32

    - `InputTokens int64 Optional`

      Total input tokens consumed across all turns.

      format: int32

    - `ListCost BetaMonetaryAmount Optional`

      A monetary amount in a specific currency.

      - `Amount string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `Currency BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `OutputTokens int64 Optional`

      Total output tokens generated across all turns.

      format: int32

    - `ServerToolUse BetaManagedAgentsServerToolUsage Optional`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `WebFetchRequests int64 Optional`

        Number of server-executed web fetch requests.

        format: int32

      - `WebSearchRequests int64 Optional`

        Number of server-executed web search requests.

        format: int32

#### Example

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
	betaManagedAgentsSessionThread, err := client.Beta.Sessions.Threads.Get(
		context.TODO(),
		"sthr_011CZkZVWa6oIjw0rgXZpnBt",
		anthropic.BetaSessionThreadGetParams{
			SessionID: "sesn_011CZkZAtmR3yMPDzynEDxu7",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaManagedAgentsSessionThread.ID)
}
```

##### Response (200)

```json
{
  "id": "sthr_011CZkZVWa6oIjw0rgXZpnBt",
  "agent": {
    "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
    "description": "A focused research subagent.",
    "mcp_servers": [
      {
        "name": "example-mcp",
        "type": "url",
        "url": "https://example-server.modelcontextprotocol.io/sse"
      }
    ],
    "model": {
      "id": "claude-opus-5",
      "effort": {
        "type": "low"
      },
      "inference_geo": "inference_geo",
      "speed": "standard"
    },
    "name": "Researcher",
    "skills": [
      {
        "skill_id": "xlsx",
        "type": "anthropic",
        "version": "1"
      }
    ],
    "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
    "tools": [
      {
        "configs": [
          {
            "enabled": true,
            "name": "bash",
            "permission_policy": {
              "type": "always_allow"
            },
            "type": "bash"
          }
        ],
        "default_config": {
          "enabled": true,
          "permission_policy": {
            "type": "always_ask"
          }
        },
        "type": "agent_toolset_20260401"
      }
    ],
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "parent_thread_id": null,
  "session_id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0,
    "startup_seconds": 0
  },
  "status": "idle",
  "type": "session_thread",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "active_seconds": 0,
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "output_tokens": 0,
    "server_tool_use": {
      "web_fetch_requests": 0,
      "web_search_requests": 3
    }
  }
}
```

### Archive Session Thread

`client.Beta.Sessions.Threads.Archive(ctx, threadID, params) (*BetaManagedAgentsSessionThread, error)`

**POST** `/v1/sessions/{session_id}/threads/{thread_id}/archive`

Archive Session Thread

#### Parameters

- `threadID string`

- `params BetaSessionThreadArchiveParams`

  - `SessionID param.Field[string]`

    Path param: Path parameter session_id

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

#### Returns

- `type BetaManagedAgentsSessionThread struct{…}`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `ID string`

    Unique identifier for this thread.

  - `Agent BetaManagedAgentsSessionThreadAgentUnion`

    The resolved agent a session thread runs: a saved-agent snapshot, the platform advisor entry, or an inline-defined (ephemeral) agent snapshot.

    - `type BetaManagedAgentsSessionThreadAgent struct{…}`

      Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

      - `ID string`

      - `Description string`

      - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

        - `Name string`

        - `Type BetaManagedAgentsMCPServerURLDefinitionType`

        - `URL string`

      - `Model BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `ID BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `type BetaManagedAgentsModel string`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `const BetaManagedAgentsModelClaudeSonnet5 BetaManagedAgentsModel = "claude-sonnet-5"`

              High-performance model for coding and agents

            - `const BetaManagedAgentsModelClaudeFable5 BetaManagedAgentsModel = "claude-fable-5"`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `const BetaManagedAgentsModelClaudeOpus5 BetaManagedAgentsModel = "claude-opus-5"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeOpus4_8 BetaManagedAgentsModel = "claude-opus-4-8"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeOpus4_7 BetaManagedAgentsModel = "claude-opus-4-7"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeOpus4_6 BetaManagedAgentsModel = "claude-opus-4-6"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeSonnet4_6 BetaManagedAgentsModel = "claude-sonnet-4-6"`

              Best combination of speed and intelligence

            - `const BetaManagedAgentsModelClaudeHaiku4_5 BetaManagedAgentsModel = "claude-haiku-4-5"`

              Fastest model with near-frontier intelligence

            - `const BetaManagedAgentsModelClaudeHaiku4_5_20251001 BetaManagedAgentsModel = "claude-haiku-4-5-20251001"`

              Fastest model with near-frontier intelligence

            - `const BetaManagedAgentsModelClaudeOpus4_5 BetaManagedAgentsModel = "claude-opus-4-5"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeOpus4_5_20251101 BetaManagedAgentsModel = "claude-opus-4-5-20251101"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeSonnet4_5 BetaManagedAgentsModel = "claude-sonnet-4-5"`

              High-performance model for agents and coding

            - `const BetaManagedAgentsModelClaudeSonnet4_5_20250929 BetaManagedAgentsModel = "claude-sonnet-4-5-20250929"`

              High-performance model for agents and coding

          - `string`

        - `Effort BetaManagedAgentsModelConfigEffortUnion Optional`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `type BetaManagedAgentsEffortLow struct{…}`

            Low effort. Favors latency over reasoning depth.

            - `Type BetaManagedAgentsEffortLowType`

          - `type BetaManagedAgentsEffortMedium struct{…}`

            Medium effort. Balances latency and reasoning depth.

            - `Type BetaManagedAgentsEffortMediumType`

          - `type BetaManagedAgentsEffortHigh struct{…}`

            High effort. Favors reasoning depth.

            - `Type BetaManagedAgentsEffortHighType`

          - `type BetaManagedAgentsEffortXhigh struct{…}`

            Extra-high effort. Not all models accept this level.

            - `Type BetaManagedAgentsEffortXhighType`

          - `type BetaManagedAgentsEffortMax struct{…}`

            Maximum effort. Favors reasoning depth over latency.

            - `Type BetaManagedAgentsEffortMaxType`

        - `InferenceGeo string Optional`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `Speed BetaManagedAgentsModelConfigSpeed Optional`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `const BetaManagedAgentsModelConfigSpeedStandard BetaManagedAgentsModelConfigSpeed = "standard"`

          - `const BetaManagedAgentsModelConfigSpeedFast BetaManagedAgentsModelConfigSpeed = "fast"`

      - `Name string`

      - `Skills []BetaManagedAgentsSessionThreadAgentSkillUnion`

        - `type BetaManagedAgentsAnthropicSkill struct{…}`

          A resolved Anthropic-managed skill.

          - `SkillID string`

          - `Type BetaManagedAgentsAnthropicSkillType`

          - `Version string`

        - `type BetaManagedAgentsCustomSkill struct{…}`

          A resolved user-created custom skill.

          - `SkillID string`

          - `Type BetaManagedAgentsCustomSkillType`

          - `Version string`

      - `System string`

      - `Tools []BetaManagedAgentsSessionThreadAgentToolUnion`

        - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

          - `Configs []BetaManagedAgentsAgentToolConfigUnion`

            - `type BetaManagedAgentsBashToolConfig struct{…}`

              Configuration for the bash tool.

              - `Enabled bool`

              - `Name Bash`

              - `PermissionPolicy BetaManagedAgentsBashToolConfigPermissionPolicyUnion`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                  - `Type BetaManagedAgentsAlwaysAllowPolicyType`

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

                  - `Type BetaManagedAgentsAlwaysAskPolicyType`

              - `Type Bash`

            - `type BetaManagedAgentsEditToolConfig struct{…}`

              Configuration for the edit tool.

              - `Enabled bool`

              - `Name Edit`

              - `PermissionPolicy BetaManagedAgentsEditToolConfigPermissionPolicyUnion`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

              - `Type Edit`

            - `type BetaManagedAgentsReadToolConfig struct{…}`

              Configuration for the read tool.

              - `Enabled bool`

              - `Name Read`

              - `PermissionPolicy BetaManagedAgentsReadToolConfigPermissionPolicyUnion`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

              - `Type Read`

            - `type BetaManagedAgentsWriteToolConfig struct{…}`

              Configuration for the write tool.

              - `Enabled bool`

              - `Name Write`

              - `PermissionPolicy BetaManagedAgentsWriteToolConfigPermissionPolicyUnion`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

              - `Type Write`

            - `type BetaManagedAgentsGlobToolConfig struct{…}`

              Configuration for the glob tool.

              - `Enabled bool`

              - `Name Glob`

              - `PermissionPolicy BetaManagedAgentsGlobToolConfigPermissionPolicyUnion`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

              - `Type Glob`

            - `type BetaManagedAgentsGrepToolConfig struct{…}`

              Configuration for the grep tool.

              - `Enabled bool`

              - `Name Grep`

              - `PermissionPolicy BetaManagedAgentsGrepToolConfigPermissionPolicyUnion`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

              - `Type Grep`

            - `type BetaManagedAgentsWebFetchToolConfig struct{…}`

              Configuration for the web_fetch tool.

              - `Enabled bool`

              - `Name WebFetch`

              - `PermissionPolicy BetaManagedAgentsWebFetchToolConfigPermissionPolicyUnion`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

              - `Type WebFetch`

              - `AllowedDomains []string Optional`

              - `BlockedDomains []string Optional`

              - `MaxContentTokens int64 Optional`

                format: int32

            - `type BetaManagedAgentsWebSearchToolConfig struct{…}`

              Configuration for the web_search tool.

              - `Enabled bool`

              - `Name WebSearch`

              - `PermissionPolicy BetaManagedAgentsWebSearchToolConfigPermissionPolicyUnion`

                Permission policy for tool execution.

                - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                  Tool calls are automatically approved without user confirmation.

                - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                  Tool calls require user confirmation before execution.

              - `Type WebSearch`

              - `AllowedDomains []string Optional`

              - `BlockedDomains []string Optional`

              - `UserLocation BetaManagedAgentsUserLocation Optional`

                Approximate user location for search result localization.

                - `Type Approximate`

                  Location precision. Only "approximate" is supported.

                - `City string Optional`

                  City name.

                  minLength: 1, maxLength: 255

                - `Country string Optional`

                  Two-letter ISO 3166-1 country code, uppercase.

                - `Region string Optional`

                  Region or state name.

                  minLength: 1, maxLength: 255

                - `Timezone string Optional`

                  IANA timezone identifier, e.g. "America/Los_Angeles".

                  minLength: 1, maxLength: 255

          - `DefaultConfig BetaManagedAgentsAgentToolsetDefaultConfig`

            Resolved default configuration for agent tools.

            - `Enabled bool`

            - `PermissionPolicy BetaManagedAgentsAgentToolsetDefaultConfigPermissionPolicyUnion`

              Permission policy for tool execution.

              - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                Tool calls are automatically approved without user confirmation.

              - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                Tool calls require user confirmation before execution.

          - `Type BetaManagedAgentsAgentToolset20260401Type`

        - `type BetaManagedAgentsMCPToolset struct{…}`

          - `Configs []BetaManagedAgentsMCPToolConfig`

            - `Enabled bool`

            - `Name string`

            - `PermissionPolicy BetaManagedAgentsMCPToolConfigPermissionPolicyUnion`

              Permission policy for tool execution.

              - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                Tool calls are automatically approved without user confirmation.

              - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                Tool calls require user confirmation before execution.

          - `DefaultConfig BetaManagedAgentsMCPToolsetDefaultConfig`

            Resolved default configuration for all tools from an MCP server.

            - `Enabled bool`

            - `PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigPermissionPolicyUnion`

              Permission policy for tool execution.

              - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                Tool calls are automatically approved without user confirmation.

              - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                Tool calls require user confirmation before execution.

          - `MCPServerName string`

          - `Type BetaManagedAgentsMCPToolsetType`

        - `type BetaManagedAgentsCustomTool struct{…}`

          A custom tool as returned in API responses.

          - `Description string`

          - `InputSchema BetaManagedAgentsCustomToolInputSchema`

            JSON Schema for custom tool input parameters.

            - `Type Object`

            - `Properties map[string, any] Optional`

            - `Required []string Optional`

          - `Name string`

          - `Type BetaManagedAgentsCustomToolType`

      - `Type BetaManagedAgentsSessionThreadAgentType`

      - `Version int64`

        format: int32

    - `type BetaManagedAgentsAdvisor struct{…}`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `Model string`

        The advisor model id.

      - `Type BetaManagedAgentsAdvisorType`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `ParentThreadID string`

    Parent thread that spawned this thread. Null for the primary thread.

  - `SessionID string`

    The session this thread belongs to.

  - `Stats BetaManagedAgentsSessionThreadStats`

    Timing statistics for a session thread.

    - `ActiveSeconds float64 Optional`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

      format: double

    - `DurationSeconds float64 Optional`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

      format: double

    - `StartupSeconds float64 Optional`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

      format: double

  - `Status BetaManagedAgentsSessionThreadStatus`

    SessionThreadStatus enum

    - `const BetaManagedAgentsSessionThreadStatusRunning BetaManagedAgentsSessionThreadStatus = "running"`

    - `const BetaManagedAgentsSessionThreadStatusIdle BetaManagedAgentsSessionThreadStatus = "idle"`

    - `const BetaManagedAgentsSessionThreadStatusRescheduling BetaManagedAgentsSessionThreadStatus = "rescheduling"`

    - `const BetaManagedAgentsSessionThreadStatusTerminated BetaManagedAgentsSessionThreadStatus = "terminated"`

  - `Type BetaManagedAgentsSessionThreadType`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `Usage BetaManagedAgentsSessionThreadUsage`

    Cumulative token usage for a session thread across all turns.

    - `ActiveSeconds float64 Optional`

      Cumulative time in seconds this thread spent in running status. Equal to `stats.active_seconds`; surfaced here so a thread's usage carries every quantity its cost is priced on.

      format: double

    - `CacheCreation BetaManagedAgentsCacheCreationUsage Optional`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `Ephemeral1hInputTokens int64 Optional`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `Ephemeral5mInputTokens int64 Optional`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `CacheReadInputTokens int64 Optional`

      Total tokens read from prompt cache.

      format: int32

    - `InputTokens int64 Optional`

      Total input tokens consumed across all turns.

      format: int32

    - `ListCost BetaMonetaryAmount Optional`

      A monetary amount in a specific currency.

      - `Amount string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `Currency BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `OutputTokens int64 Optional`

      Total output tokens generated across all turns.

      format: int32

    - `ServerToolUse BetaManagedAgentsServerToolUsage Optional`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `WebFetchRequests int64 Optional`

        Number of server-executed web fetch requests.

        format: int32

      - `WebSearchRequests int64 Optional`

        Number of server-executed web search requests.

        format: int32

#### Example

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
	betaManagedAgentsSessionThread, err := client.Beta.Sessions.Threads.Archive(
		context.TODO(),
		"sthr_011CZkZVWa6oIjw0rgXZpnBt",
		anthropic.BetaSessionThreadArchiveParams{
			SessionID: "sesn_011CZkZAtmR3yMPDzynEDxu7",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaManagedAgentsSessionThread.ID)
}
```

##### Response (200)

```json
{
  "id": "sthr_011CZkZVWa6oIjw0rgXZpnBt",
  "agent": {
    "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
    "description": "A focused research subagent.",
    "mcp_servers": [
      {
        "name": "example-mcp",
        "type": "url",
        "url": "https://example-server.modelcontextprotocol.io/sse"
      }
    ],
    "model": {
      "id": "claude-opus-5",
      "effort": {
        "type": "low"
      },
      "inference_geo": "inference_geo",
      "speed": "standard"
    },
    "name": "Researcher",
    "skills": [
      {
        "skill_id": "xlsx",
        "type": "anthropic",
        "version": "1"
      }
    ],
    "system": "You are a research subagent that gathers and summarises sources for the coordinating agent.",
    "tools": [
      {
        "configs": [
          {
            "enabled": true,
            "name": "bash",
            "permission_policy": {
              "type": "always_allow"
            },
            "type": "bash"
          }
        ],
        "default_config": {
          "enabled": true,
          "permission_policy": {
            "type": "always_ask"
          }
        },
        "type": "agent_toolset_20260401"
      }
    ],
    "type": "agent",
    "version": 1
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "parent_thread_id": null,
  "session_id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0,
    "startup_seconds": 0
  },
  "status": "idle",
  "type": "session_thread",
  "updated_at": "2026-03-15T10:00:00Z",
  "usage": {
    "active_seconds": 0,
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_read_input_tokens": 0,
    "input_tokens": 0,
    "list_cost": {
      "amount": "2500",
      "currency": "USD"
    },
    "output_tokens": 0,
    "server_tool_use": {
      "web_fetch_requests": 0,
      "web_search_requests": 3
    }
  }
}
```

## Sessions › Threads › Events

### List Session Thread Events

`client.Beta.Sessions.Threads.Events.List(ctx, threadID, params) (*PageCursor[BetaManagedAgentsSessionEventUnion], error)`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}/events`

List Session Thread Events

#### Parameters

- `threadID string`

- `params BetaSessionThreadEventListParams`

  - `SessionID param.Field[string]`

    Path param: Path parameter session_id

  - `Limit param.Field[int64] Optional`

    Query param: Query parameter for limit

    format: int32

  - `Page param.Field[string] Optional`

    Query param: Query parameter for page

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

#### Returns

- `type BetaManagedAgentsSessionEventUnion interface{…}`

  Union type for all event types in a session.

  - `type BetaManagedAgentsUserMessageEvent struct{…}`

    A user message event in the session conversation.

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsUserMessageEventContentUnion`

      Array of content blocks comprising the user message.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

        - `Text string`

          The text content.

          minLength: 1

        - `Type BetaManagedAgentsTextBlockType`

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source BetaManagedAgentsImageBlockSourceUnion`

          Union type for image source variants.

          - `type BetaManagedAgentsBase64ImageSource struct{…}`

            Base64-encoded image data.

            - `Data string`

              Base64-encoded image data.

              minLength: 1

            - `MediaType string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

            - `Type BetaManagedAgentsBase64ImageSourceType`

          - `type BetaManagedAgentsURLImageSource struct{…}`

            Image referenced by URL.

            - `Type BetaManagedAgentsURLImageSourceType`

            - `URL string`

              URL of the image to fetch.

              minLength: 1

          - `type BetaManagedAgentsFileImageSource struct{…}`

            Image referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

              minLength: 1

            - `Type BetaManagedAgentsFileImageSourceType`

        - `Type BetaManagedAgentsImageBlockType`

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source BetaManagedAgentsDocumentBlockSourceUnion`

          Union type for document source variants.

          - `type BetaManagedAgentsBase64DocumentSource struct{…}`

            Base64-encoded document data.

            - `Data string`

              Base64-encoded document data.

              minLength: 1

            - `MediaType string`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

            - `Type BetaManagedAgentsBase64DocumentSourceType`

          - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

            Plain text document content.

            - `Data string`

              The plain text content.

              minLength: 1

            - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

              MIME type of the text content. Must be "text/plain".

            - `Type BetaManagedAgentsPlainTextDocumentSourceType`

          - `type BetaManagedAgentsURLDocumentSource struct{…}`

            Document referenced by URL.

            - `Type BetaManagedAgentsURLDocumentSourceType`

            - `URL string`

              URL of the document to fetch.

              minLength: 1

          - `type BetaManagedAgentsFileDocumentSource struct{…}`

            Document referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

              minLength: 1

            - `Type BetaManagedAgentsFileDocumentSourceType`

        - `Type BetaManagedAgentsDocumentBlockType`

        - `Context string Optional`

          Additional context about the document for the model.

        - `Title string Optional`

          The title of the document.

      - `type BetaManagedAgentsRedactedBlockParam struct{…}`

        Placeholder for content withheld by Anthropic model policy.

        - `Type BetaManagedAgentsRedactedBlockType`

    - `Type BetaManagedAgentsUserMessageEventType`

    - `ProcessedAt Time Optional`

      A timestamp in RFC 3339 format

      format: date-time

  - `type BetaManagedAgentsUserInterruptEvent struct{…}`

    An interrupt event that pauses agent execution and returns control to the user.

    - `ID string`

      Unique identifier for this event.

    - `Type BetaManagedAgentsUserInterruptEventType`

    - `ProcessedAt Time Optional`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string Optional`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `type BetaManagedAgentsUserToolConfirmationEvent struct{…}`

    A tool confirmation event that approves or denies a pending tool execution.

    - `ID string`

      Unique identifier for this event.

    - `Result BetaManagedAgentsUserToolConfirmationEventResult`

      UserToolConfirmationResult enum

      - `const BetaManagedAgentsUserToolConfirmationEventResultAllow BetaManagedAgentsUserToolConfirmationEventResult = "allow"`

      - `const BetaManagedAgentsUserToolConfirmationEventResultDeny BetaManagedAgentsUserToolConfirmationEventResult = "deny"`

    - `ToolUseID string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type BetaManagedAgentsUserToolConfirmationEventType`

    - `DenyMessage string Optional`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `ProcessedAt Time Optional`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string Optional`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `type BetaManagedAgentsUserCustomToolResultEvent struct{…}`

    Event sent by the client providing the result of a custom tool execution.

    - `ID string`

      Unique identifier for this event.

    - `CustomToolUseID string`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type BetaManagedAgentsUserCustomToolResultEventType`

    - `Content []BetaManagedAgentsUserCustomToolResultEventContentUnion Optional`

      The result content returned by the tool.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `type BetaManagedAgentsSearchResultBlock struct{…}`

        A block containing a web search result.

        - `Citations BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `Enabled bool`

            Whether citations are enabled for this search result.

        - `Content []BetaManagedAgentsSearchResultContent`

          Array of text content blocks from the search result.

          - `Text string`

            The text content.

            minLength: 1

          - `Type BetaManagedAgentsSearchResultContentType`

        - `Source string`

          The URL source of the search result.

          minLength: 1

        - `Title string`

          The title of the search result.

          minLength: 1

        - `Type BetaManagedAgentsSearchResultBlockType`

    - `IsError bool Optional`

      Whether the tool execution resulted in an error.

    - `ProcessedAt Time Optional`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string Optional`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `type BetaManagedAgentsAgentCustomToolUseEvent struct{…}`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `ID string`

      Unique identifier for this event.

    - `Input map[string, any]`

      Input parameters for the tool call.

    - `Name string`

      Name of the custom tool being called.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsAgentCustomToolUseEventType`

    - `SessionThreadID string Optional`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `type BetaManagedAgentsAgentMessageEvent struct{…}`

    An agent response event in the session conversation.

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsAgentMessageEventContentUnion`

      Array of text blocks comprising the agent response.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

      - `type BetaManagedAgentsRedactedBlockParam struct{…}`

        Placeholder for content withheld by Anthropic model policy.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsAgentMessageEventType`

  - `type BetaManagedAgentsAgentThinkingEvent struct{…}`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsAgentThinkingEventType`

  - `type BetaManagedAgentsAgentMCPToolUseEvent struct{…}`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `ID string`

      Unique identifier for this event.

    - `Input map[string, any]`

      Input parameters for the tool call.

    - `MCPServerName string`

      Name of the MCP server providing the tool.

    - `Name string`

      Name of the MCP tool being used.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsAgentMCPToolUseEventType`

    - `EvaluatedPermission BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission Optional`

      AgentEvaluatedPermission enum

      - `const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionAllow BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "allow"`

      - `const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionAsk BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "ask"`

      - `const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionDeny BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "deny"`

    - `SessionThreadID string Optional`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `type BetaManagedAgentsAgentMCPToolResultEvent struct{…}`

    Event representing the result of an MCP tool execution.

    - `ID string`

      Unique identifier for this event.

    - `MCPToolUseID string`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsAgentMCPToolResultEventType`

    - `Content []BetaManagedAgentsAgentMCPToolResultEventContentUnion Optional`

      The result content returned by the tool.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `type BetaManagedAgentsSearchResultBlock struct{…}`

        A block containing a web search result.

    - `IsError bool Optional`

      Whether the tool execution resulted in an error.

  - `type BetaManagedAgentsAgentToolUseEvent struct{…}`

    Event emitted when the agent invokes a built-in agent tool.

    - `ID string`

      Unique identifier for this event.

    - `Input map[string, any]`

      Input parameters for the tool call.

    - `Name string`

      Name of the agent tool being used.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsAgentToolUseEventType`

    - `EvaluatedPermission BetaManagedAgentsAgentToolUseEventEvaluatedPermission Optional`

      AgentEvaluatedPermission enum

      - `const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionAllow BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "allow"`

      - `const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionAsk BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "ask"`

      - `const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionDeny BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "deny"`

    - `SessionThreadID string Optional`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `type BetaManagedAgentsAgentToolResultEvent struct{…}`

    Event representing the result of an agent tool execution.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `ToolUseID string`

      The id of the `agent.tool_use` event this result corresponds to.

    - `Type BetaManagedAgentsAgentToolResultEventType`

    - `Content []BetaManagedAgentsAgentToolResultEventContentUnion Optional`

      The result content returned by the tool.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `type BetaManagedAgentsSearchResultBlock struct{…}`

        A block containing a web search result.

    - `IsError bool Optional`

      Whether the tool execution resulted in an error.

  - `type BetaManagedAgentsAgentThreadMessageReceivedEvent struct{…}`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsAgentThreadMessageReceivedEventContentUnion`

      Message content blocks.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `type BetaManagedAgentsRedactedBlockParam struct{…}`

        Placeholder for content withheld by Anthropic model policy.

    - `FromSessionThreadID string`

      Public `sthr_` ID of the thread that sent the message.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsAgentThreadMessageReceivedEventType`

    - `FromAgentName string Optional`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `type BetaManagedAgentsAgentThreadMessageSentEvent struct{…}`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsAgentThreadMessageSentEventContentUnion`

      Message content blocks.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `type BetaManagedAgentsRedactedBlockParam struct{…}`

        Placeholder for content withheld by Anthropic model policy.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `ToSessionThreadID string`

      Public `sthr_` ID of the thread the message was sent to.

    - `Type BetaManagedAgentsAgentThreadMessageSentEventType`

    - `ToAgentName string Optional`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `type BetaManagedAgentsAgentThreadContextCompactedEvent struct{…}`

    Indicates that context compaction (summarization) occurred during the session.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsAgentThreadContextCompactedEventType`

  - `type BetaManagedAgentsSessionErrorEvent struct{…}`

    An error event indicating a problem occurred during session execution.

    - `ID string`

      Unique identifier for this event.

    - `Error BetaManagedAgentsSessionErrorEventErrorUnion`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `type BetaManagedAgentsUnknownError struct{…}`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsUnknownErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type BetaManagedAgentsRetryStatusRetryingType`

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type BetaManagedAgentsRetryStatusExhaustedType`

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type BetaManagedAgentsRetryStatusTerminalType`

        - `Type BetaManagedAgentsUnknownErrorType`

      - `type BetaManagedAgentsModelOverloadedError struct{…}`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsModelOverloadedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type BetaManagedAgentsModelOverloadedErrorType`

      - `type BetaManagedAgentsModelRateLimitedError struct{…}`

        The model request was rate-limited.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsModelRateLimitedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type BetaManagedAgentsModelRateLimitedErrorType`

      - `type BetaManagedAgentsModelRequestFailedError struct{…}`

        A model request failed for a reason other than overload or rate-limiting.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsModelRequestFailedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type BetaManagedAgentsModelRequestFailedErrorType`

      - `type BetaManagedAgentsMCPConnectionFailedError struct{…}`

        Failed to connect to an MCP server.

        - `MCPServerName string`

          Name of the MCP server that failed to connect.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsMCPConnectionFailedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type BetaManagedAgentsMCPConnectionFailedErrorType`

      - `type BetaManagedAgentsMCPAuthenticationFailedError struct{…}`

        Authentication to an MCP server failed.

        - `MCPServerName string`

          Name of the MCP server that failed authentication.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsMCPAuthenticationFailedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type BetaManagedAgentsMCPAuthenticationFailedErrorType`

      - `type BetaManagedAgentsBillingError struct{…}`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsBillingErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type BetaManagedAgentsBillingErrorType`

      - `type BetaManagedAgentsCredentialHostUnreachableError struct{…}`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `CredentialID string`

          ID of the affected credential.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsCredentialHostUnreachableErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type BetaManagedAgentsCredentialHostUnreachableErrorType`

        - `VaultID string`

          ID of the vault containing the affected credential.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSessionErrorEventType`

  - `type BetaManagedAgentsSessionStatusRescheduledEvent struct{…}`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSessionStatusRescheduledEventType`

  - `type BetaManagedAgentsSessionStatusRunningEvent struct{…}`

    Indicates the session is actively running and the agent is working.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSessionStatusRunningEventType`

  - `type BetaManagedAgentsSessionStatusIdleEvent struct{…}`

    Indicates the agent has paused and is awaiting user input.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `StopReason BetaManagedAgentsSessionStatusIdleEventStopReasonUnion`

      The agent completed its turn naturally and is ready for the next user message.

      - `type BetaManagedAgentsSessionEndTurn struct{…}`

        The agent completed its turn naturally and is ready for the next user message.

        - `Type BetaManagedAgentsSessionEndTurnType`

      - `type BetaManagedAgentsSessionRequiresAction struct{…}`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `EventIDs []string`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `Type BetaManagedAgentsSessionRequiresActionType`

      - `type BetaManagedAgentsSessionRetriesExhausted struct{…}`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `Type BetaManagedAgentsSessionRetriesExhaustedType`

      - `type BetaManagedAgentsSessionBudgetReached struct{…}`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `Type BetaManagedAgentsSessionBudgetReachedType`

    - `Type BetaManagedAgentsSessionStatusIdleEventType`

  - `type BetaManagedAgentsSessionStatusTerminatedEvent struct{…}`

    Indicates the session has terminated, either due to an error or completion.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSessionStatusTerminatedEventType`

  - `type BetaManagedAgentsSessionThreadCreatedEvent struct{…}`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the callable agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string`

      Public `sthr_` ID of the newly created thread.

    - `Type BetaManagedAgentsSessionThreadCreatedEventType`

  - `type BetaManagedAgentsSpanOutcomeEvaluationStartEvent struct{…}`

    Emitted when an outcome evaluation cycle begins.

    - `ID string`

      Unique identifier for this event.

    - `Iteration int64`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

      format: int32

    - `OutcomeID string`

      The `outc_` ID of the outcome being evaluated.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSpanOutcomeEvaluationStartEventType`

  - `type BetaManagedAgentsSpanOutcomeEvaluationEndEvent struct{…}`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `ID string`

      Unique identifier for this event.

    - `Explanation string`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `Iteration int64`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `OutcomeEvaluationStartID string`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `OutcomeID string`

      The `outc_` ID of the outcome being evaluated.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Result string`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `Type BetaManagedAgentsSpanOutcomeEvaluationEndEventType`

    - `Usage BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `CacheCreationInputTokens int64`

        Tokens used to create prompt cache in this request.

        format: int32

      - `CacheReadInputTokens int64`

        Tokens read from prompt cache in this request.

        format: int32

      - `InputTokens int64`

        Input tokens consumed by this request.

        format: int32

      - `OutputTokens int64`

        Output tokens generated by this request.

        format: int32

      - `Speed BetaManagedAgentsSpanModelUsageSpeed Optional`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `const BetaManagedAgentsSpanModelUsageSpeedStandard BetaManagedAgentsSpanModelUsageSpeed = "standard"`

        - `const BetaManagedAgentsSpanModelUsageSpeedFast BetaManagedAgentsSpanModelUsageSpeed = "fast"`

  - `type BetaManagedAgentsSpanModelRequestStartEvent struct{…}`

    Emitted when a model request is initiated by the agent.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSpanModelRequestStartEventType`

  - `type BetaManagedAgentsSpanModelRequestEndEvent struct{…}`

    Emitted when a model request completes.

    - `ID string`

      Unique identifier for this event.

    - `IsError bool`

      Whether the model request resulted in an error.

    - `ModelRequestStartID string`

      The id of the corresponding `span.model_request_start` event.

    - `ModelUsage BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSpanModelRequestEndEventType`

  - `type BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent struct{…}`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `ID string`

      Unique identifier for this event.

    - `Iteration int64`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `OutcomeID string`

      The `outc_` ID of the outcome being evaluated.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSpanOutcomeEvaluationOngoingEventType`

  - `type BetaManagedAgentsUserDefineOutcomeEvent struct{…}`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `ID string`

      Unique identifier for this event.

    - `Description string`

      What the agent should produce. Copied from the input event.

    - `MaxIterations int64`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

      format: int32

    - `OutcomeID string`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Rubric BetaManagedAgentsUserDefineOutcomeEventRubricUnion`

      Rubric for grading the quality of an outcome.

      - `type BetaManagedAgentsFileRubric struct{…}`

        Rubric referenced by a file uploaded via the Files API.

        - `FileID string`

          ID of the rubric file.

        - `Type BetaManagedAgentsFileRubricType`

      - `type BetaManagedAgentsTextRubric struct{…}`

        Rubric content provided inline as text.

        - `Content string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `Type BetaManagedAgentsTextRubricType`

    - `Type BetaManagedAgentsUserDefineOutcomeEventType`

  - `type BetaManagedAgentsSessionDeletedEvent struct{…}`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSessionDeletedEventType`

  - `type BetaManagedAgentsSessionThreadStatusRunningEvent struct{…}`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string`

      Public sthr_ ID of the thread that started running.

    - `Type BetaManagedAgentsSessionThreadStatusRunningEventType`

  - `type BetaManagedAgentsSessionThreadStatusIdleEvent struct{…}`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string`

      Public sthr_ ID of the thread that went idle.

    - `StopReason BetaManagedAgentsSessionThreadStatusIdleEventStopReasonUnion`

      The agent completed its turn naturally and is ready for the next user message.

      - `type BetaManagedAgentsSessionEndTurn struct{…}`

        The agent completed its turn naturally and is ready for the next user message.

      - `type BetaManagedAgentsSessionRequiresAction struct{…}`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `type BetaManagedAgentsSessionRetriesExhausted struct{…}`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `type BetaManagedAgentsSessionBudgetReached struct{…}`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

    - `Type BetaManagedAgentsSessionThreadStatusIdleEventType`

  - `type BetaManagedAgentsSessionThreadStatusTerminatedEvent struct{…}`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string`

      Public sthr_ ID of the thread that terminated.

    - `Type BetaManagedAgentsSessionThreadStatusTerminatedEventType`

  - `type BetaManagedAgentsUserToolResultEvent struct{…}`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `ID string`

      Unique identifier for this event.

    - `ToolUseID string`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type BetaManagedAgentsUserToolResultEventType`

    - `Content []BetaManagedAgentsUserToolResultEventContentUnion Optional`

      The result content returned by the tool.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `type BetaManagedAgentsSearchResultBlock struct{…}`

        A block containing a web search result.

    - `IsError bool Optional`

      Whether the tool execution resulted in an error.

    - `ProcessedAt Time Optional`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string Optional`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `type BetaManagedAgentsSessionThreadStatusRescheduledEvent struct{…}`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string`

      Public sthr_ ID of the thread that is retrying.

    - `Type BetaManagedAgentsSessionThreadStatusRescheduledEventType`

  - `type BetaManagedAgentsSessionUpdatedEvent struct{…}`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSessionUpdatedEventType`

    - `Agent BetaManagedAgentsSessionAgent Optional`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `ID string`

      - `Description string`

      - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

        - `Name string`

        - `Type BetaManagedAgentsMCPServerURLDefinitionType`

        - `URL string`

      - `Model BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `ID BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `type BetaManagedAgentsModel string`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `const BetaManagedAgentsModelClaudeSonnet5 BetaManagedAgentsModel = "claude-sonnet-5"`

              High-performance model for coding and agents

            - `const BetaManagedAgentsModelClaudeFable5 BetaManagedAgentsModel = "claude-fable-5"`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `const BetaManagedAgentsModelClaudeOpus5 BetaManagedAgentsModel = "claude-opus-5"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeOpus4_8 BetaManagedAgentsModel = "claude-opus-4-8"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeOpus4_7 BetaManagedAgentsModel = "claude-opus-4-7"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeOpus4_6 BetaManagedAgentsModel = "claude-opus-4-6"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeSonnet4_6 BetaManagedAgentsModel = "claude-sonnet-4-6"`

              Best combination of speed and intelligence

            - `const BetaManagedAgentsModelClaudeHaiku4_5 BetaManagedAgentsModel = "claude-haiku-4-5"`

              Fastest model with near-frontier intelligence

            - `const BetaManagedAgentsModelClaudeHaiku4_5_20251001 BetaManagedAgentsModel = "claude-haiku-4-5-20251001"`

              Fastest model with near-frontier intelligence

            - `const BetaManagedAgentsModelClaudeOpus4_5 BetaManagedAgentsModel = "claude-opus-4-5"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeOpus4_5_20251101 BetaManagedAgentsModel = "claude-opus-4-5-20251101"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeSonnet4_5 BetaManagedAgentsModel = "claude-sonnet-4-5"`

              High-performance model for agents and coding

            - `const BetaManagedAgentsModelClaudeSonnet4_5_20250929 BetaManagedAgentsModel = "claude-sonnet-4-5-20250929"`

              High-performance model for agents and coding

          - `string`

        - `Effort BetaManagedAgentsModelConfigEffortUnion Optional`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `type BetaManagedAgentsEffortLow struct{…}`

            Low effort. Favors latency over reasoning depth.

            - `Type BetaManagedAgentsEffortLowType`

          - `type BetaManagedAgentsEffortMedium struct{…}`

            Medium effort. Balances latency and reasoning depth.

            - `Type BetaManagedAgentsEffortMediumType`

          - `type BetaManagedAgentsEffortHigh struct{…}`

            High effort. Favors reasoning depth.

            - `Type BetaManagedAgentsEffortHighType`

          - `type BetaManagedAgentsEffortXhigh struct{…}`

            Extra-high effort. Not all models accept this level.

            - `Type BetaManagedAgentsEffortXhighType`

          - `type BetaManagedAgentsEffortMax struct{…}`

            Maximum effort. Favors reasoning depth over latency.

            - `Type BetaManagedAgentsEffortMaxType`

        - `InferenceGeo string Optional`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `Speed BetaManagedAgentsModelConfigSpeed Optional`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `const BetaManagedAgentsModelConfigSpeedStandard BetaManagedAgentsModelConfigSpeed = "standard"`

          - `const BetaManagedAgentsModelConfigSpeedFast BetaManagedAgentsModelConfigSpeed = "fast"`

      - `Multiagent BetaManagedAgentsSessionMultiagentCoordinator`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `Agents []BetaManagedAgentsSessionMultiagentCoordinatorAgentUnion`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `type BetaManagedAgentsSessionThreadAgent struct{…}`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `ID string`

            - `Description string`

            - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

              - `Name string`

              - `Type BetaManagedAgentsMCPServerURLDefinitionType`

              - `URL string`

            - `Model BetaManagedAgentsModelConfig`

              Model identifier and configuration.

            - `Name string`

            - `Skills []BetaManagedAgentsSessionThreadAgentSkillUnion`

              - `type BetaManagedAgentsAnthropicSkill struct{…}`

                A resolved Anthropic-managed skill.

                - `SkillID string`

                - `Type BetaManagedAgentsAnthropicSkillType`

                - `Version string`

              - `type BetaManagedAgentsCustomSkill struct{…}`

                A resolved user-created custom skill.

                - `SkillID string`

                - `Type BetaManagedAgentsCustomSkillType`

                - `Version string`

            - `System string`

            - `Tools []BetaManagedAgentsSessionThreadAgentToolUnion`

              - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

                - `Configs []BetaManagedAgentsAgentToolConfigUnion`

                  - `type BetaManagedAgentsBashToolConfig struct{…}`

                    Configuration for the bash tool.

                    - `Enabled bool`

                    - `Name Bash`

                    - `PermissionPolicy BetaManagedAgentsBashToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                        - `Type BetaManagedAgentsAlwaysAllowPolicyType`

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                        - `Type BetaManagedAgentsAlwaysAskPolicyType`

                    - `Type Bash`

                  - `type BetaManagedAgentsEditToolConfig struct{…}`

                    Configuration for the edit tool.

                    - `Enabled bool`

                    - `Name Edit`

                    - `PermissionPolicy BetaManagedAgentsEditToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                    - `Type Edit`

                  - `type BetaManagedAgentsReadToolConfig struct{…}`

                    Configuration for the read tool.

                    - `Enabled bool`

                    - `Name Read`

                    - `PermissionPolicy BetaManagedAgentsReadToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                    - `Type Read`

                  - `type BetaManagedAgentsWriteToolConfig struct{…}`

                    Configuration for the write tool.

                    - `Enabled bool`

                    - `Name Write`

                    - `PermissionPolicy BetaManagedAgentsWriteToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                    - `Type Write`

                  - `type BetaManagedAgentsGlobToolConfig struct{…}`

                    Configuration for the glob tool.

                    - `Enabled bool`

                    - `Name Glob`

                    - `PermissionPolicy BetaManagedAgentsGlobToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                    - `Type Glob`

                  - `type BetaManagedAgentsGrepToolConfig struct{…}`

                    Configuration for the grep tool.

                    - `Enabled bool`

                    - `Name Grep`

                    - `PermissionPolicy BetaManagedAgentsGrepToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                    - `Type Grep`

                  - `type BetaManagedAgentsWebFetchToolConfig struct{…}`

                    Configuration for the web_fetch tool.

                    - `Enabled bool`

                    - `Name WebFetch`

                    - `PermissionPolicy BetaManagedAgentsWebFetchToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                    - `Type WebFetch`

                    - `AllowedDomains []string Optional`

                    - `BlockedDomains []string Optional`

                    - `MaxContentTokens int64 Optional`

                      format: int32

                  - `type BetaManagedAgentsWebSearchToolConfig struct{…}`

                    Configuration for the web_search tool.

                    - `Enabled bool`

                    - `Name WebSearch`

                    - `PermissionPolicy BetaManagedAgentsWebSearchToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                    - `Type WebSearch`

                    - `AllowedDomains []string Optional`

                    - `BlockedDomains []string Optional`

                    - `UserLocation BetaManagedAgentsUserLocation Optional`

                      Approximate user location for search result localization.

                      - `Type Approximate`

                        Location precision. Only "approximate" is supported.

                      - `City string Optional`

                        City name.

                        minLength: 1, maxLength: 255

                      - `Country string Optional`

                        Two-letter ISO 3166-1 country code, uppercase.

                      - `Region string Optional`

                        Region or state name.

                        minLength: 1, maxLength: 255

                      - `Timezone string Optional`

                        IANA timezone identifier, e.g. "America/Los_Angeles".

                        minLength: 1, maxLength: 255

                - `DefaultConfig BetaManagedAgentsAgentToolsetDefaultConfig`

                  Resolved default configuration for agent tools.

                  - `Enabled bool`

                  - `PermissionPolicy BetaManagedAgentsAgentToolsetDefaultConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                - `Type BetaManagedAgentsAgentToolset20260401Type`

              - `type BetaManagedAgentsMCPToolset struct{…}`

                - `Configs []BetaManagedAgentsMCPToolConfig`

                  - `Enabled bool`

                  - `Name string`

                  - `PermissionPolicy BetaManagedAgentsMCPToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                - `DefaultConfig BetaManagedAgentsMCPToolsetDefaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `Enabled bool`

                  - `PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                - `MCPServerName string`

                - `Type BetaManagedAgentsMCPToolsetType`

              - `type BetaManagedAgentsCustomTool struct{…}`

                A custom tool as returned in API responses.

                - `Description string`

                - `InputSchema BetaManagedAgentsCustomToolInputSchema`

                  JSON Schema for custom tool input parameters.

                  - `Type Object`

                  - `Properties map[string, any] Optional`

                  - `Required []string Optional`

                - `Name string`

                - `Type BetaManagedAgentsCustomToolType`

            - `Type BetaManagedAgentsSessionThreadAgentType`

            - `Version int64`

              format: int32

          - `type BetaManagedAgentsAdvisor struct{…}`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `Model string`

              The advisor model id.

            - `Type BetaManagedAgentsAdvisorType`

        - `Type BetaManagedAgentsSessionMultiagentCoordinatorType`

      - `Name string`

      - `Skills []BetaManagedAgentsSessionAgentSkillUnion`

        - `type BetaManagedAgentsAnthropicSkill struct{…}`

          A resolved Anthropic-managed skill.

        - `type BetaManagedAgentsCustomSkill struct{…}`

          A resolved user-created custom skill.

      - `System string`

      - `Tools []BetaManagedAgentsSessionAgentToolUnion`

        - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

        - `type BetaManagedAgentsMCPToolset struct{…}`

        - `type BetaManagedAgentsCustomTool struct{…}`

          A custom tool as returned in API responses.

      - `Type BetaManagedAgentsSessionAgentType`

      - `Version int64`

        format: int32

    - `Budget BetaManagedAgentsBudgetLimit Optional`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `MaxListCost BetaMonetaryAmount`

        A monetary amount in a specific currency.

        - `Amount string`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `Currency BetaCurrency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `Type BetaManagedAgentsBudgetLimitType`

    - `Metadata map[string, string] Optional`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `Title string Optional`

      The session's new title. Present only when the update changed it.

  - `type BetaManagedAgentsSystemMessageEvent struct{…}`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsSystemContentBlock`

      System content blocks. Text-only.

      - `Text string`

        The text content.

        minLength: 1

      - `Type BetaManagedAgentsSystemContentBlockType`

    - `Type BetaManagedAgentsSystemMessageEventType`

    - `ProcessedAt Time Optional`

      A timestamp in RFC 3339 format

      format: date-time

  - `type BetaManagedAgentsSessionUsageEvent struct{…}`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSessionUsageEventType`

    - `Usage BetaManagedAgentsSessionUsageSnapshot`

      Point-in-time snapshot of a session's cumulative usage.

      - `ActiveSeconds float64 Optional`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `CacheCreation BetaManagedAgentsCacheCreationUsage Optional`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `Ephemeral1hInputTokens int64 Optional`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `Ephemeral5mInputTokens int64 Optional`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `CacheReadInputTokens int64 Optional`

        Total tokens read from prompt cache.

        format: int32

      - `InputTokens int64 Optional`

        Total input tokens consumed across all turns.

        format: int32

      - `ListCost BetaMonetaryAmount Optional`

        A monetary amount in a specific currency.

      - `OutputTokens int64 Optional`

        Total output tokens generated across all turns.

        format: int32

      - `ServerToolUse BetaManagedAgentsServerToolUsage Optional`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `WebFetchRequests int64 Optional`

          Number of server-executed web fetch requests.

          format: int32

        - `WebSearchRequests int64 Optional`

          Number of server-executed web search requests.

          format: int32

    - `Budget BetaManagedAgentsBudgetLimit Optional`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

#### Example

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
	page, err := client.Beta.Sessions.Threads.Events.List(
		context.TODO(),
		"sthr_011CZkZVWa6oIjw0rgXZpnBt",
		anthropic.BetaSessionThreadEventListParams{
			SessionID: "sesn_011CZkZAtmR3yMPDzynEDxu7",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
}
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message",
      "processed_at": "2026-03-15T10:00:00Z"
    }
  ],
  "next_page": "next_page"
}
```

### Stream Session Thread Events

`client.Beta.Sessions.Threads.Events.Stream(ctx, threadID, params) (*BetaManagedAgentsStreamSessionThreadEventsUnion, error)`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}/stream`

Stream Session Thread Events

#### Parameters

- `threadID string`

- `params BetaSessionThreadEventStreamParams`

  - `SessionID param.Field[string]`

    Path param: Path parameter session_id

  - `EventDeltas param.Field[[]BetaManagedAgentsDeltaType] Optional`

    Query param: When set, this connection also receives streaming deltas (`event_start`, `event_delta`) while an event is being produced, before the event itself arrives. Deltas are best-effort; when the final event is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no final event — its terminal `span.model_request_end` closes the preview. Accepts one or more event types to preview and may be repeated: `agent.message` streams `content_delta` fragments; `agent.thinking` is start-only — a signal that the agent has begun extended thinking, concluded by the `agent.thinking` event itself. Only previews of the requested event types are sent.

    - `const BetaManagedAgentsDeltaTypeAgentMessage BetaManagedAgentsDeltaType = "agent.message"`

    - `const BetaManagedAgentsDeltaTypeAgentThinking BetaManagedAgentsDeltaType = "agent.thinking"`

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

#### Returns

- `type BetaManagedAgentsStreamSessionThreadEventsUnion interface{…}`

  Server-sent event in a single thread's stream.

  - `type BetaManagedAgentsUserMessageEvent struct{…}`

    A user message event in the session conversation.

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsUserMessageEventContentUnion`

      Array of content blocks comprising the user message.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

        - `Text string`

          The text content.

          minLength: 1

        - `Type BetaManagedAgentsTextBlockType`

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source BetaManagedAgentsImageBlockSourceUnion`

          Union type for image source variants.

          - `type BetaManagedAgentsBase64ImageSource struct{…}`

            Base64-encoded image data.

            - `Data string`

              Base64-encoded image data.

              minLength: 1

            - `MediaType string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

            - `Type BetaManagedAgentsBase64ImageSourceType`

          - `type BetaManagedAgentsURLImageSource struct{…}`

            Image referenced by URL.

            - `Type BetaManagedAgentsURLImageSourceType`

            - `URL string`

              URL of the image to fetch.

              minLength: 1

          - `type BetaManagedAgentsFileImageSource struct{…}`

            Image referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

              minLength: 1

            - `Type BetaManagedAgentsFileImageSourceType`

        - `Type BetaManagedAgentsImageBlockType`

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source BetaManagedAgentsDocumentBlockSourceUnion`

          Union type for document source variants.

          - `type BetaManagedAgentsBase64DocumentSource struct{…}`

            Base64-encoded document data.

            - `Data string`

              Base64-encoded document data.

              minLength: 1

            - `MediaType string`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

            - `Type BetaManagedAgentsBase64DocumentSourceType`

          - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

            Plain text document content.

            - `Data string`

              The plain text content.

              minLength: 1

            - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

              MIME type of the text content. Must be "text/plain".

            - `Type BetaManagedAgentsPlainTextDocumentSourceType`

          - `type BetaManagedAgentsURLDocumentSource struct{…}`

            Document referenced by URL.

            - `Type BetaManagedAgentsURLDocumentSourceType`

            - `URL string`

              URL of the document to fetch.

              minLength: 1

          - `type BetaManagedAgentsFileDocumentSource struct{…}`

            Document referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

              minLength: 1

            - `Type BetaManagedAgentsFileDocumentSourceType`

        - `Type BetaManagedAgentsDocumentBlockType`

        - `Context string Optional`

          Additional context about the document for the model.

        - `Title string Optional`

          The title of the document.

      - `type BetaManagedAgentsRedactedBlockParam struct{…}`

        Placeholder for content withheld by Anthropic model policy.

        - `Type BetaManagedAgentsRedactedBlockType`

    - `Type BetaManagedAgentsUserMessageEventType`

    - `ProcessedAt Time Optional`

      A timestamp in RFC 3339 format

      format: date-time

  - `type BetaManagedAgentsUserInterruptEvent struct{…}`

    An interrupt event that pauses agent execution and returns control to the user.

    - `ID string`

      Unique identifier for this event.

    - `Type BetaManagedAgentsUserInterruptEventType`

    - `ProcessedAt Time Optional`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string Optional`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `type BetaManagedAgentsUserToolConfirmationEvent struct{…}`

    A tool confirmation event that approves or denies a pending tool execution.

    - `ID string`

      Unique identifier for this event.

    - `Result BetaManagedAgentsUserToolConfirmationEventResult`

      UserToolConfirmationResult enum

      - `const BetaManagedAgentsUserToolConfirmationEventResultAllow BetaManagedAgentsUserToolConfirmationEventResult = "allow"`

      - `const BetaManagedAgentsUserToolConfirmationEventResultDeny BetaManagedAgentsUserToolConfirmationEventResult = "deny"`

    - `ToolUseID string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type BetaManagedAgentsUserToolConfirmationEventType`

    - `DenyMessage string Optional`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `ProcessedAt Time Optional`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string Optional`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `type BetaManagedAgentsUserCustomToolResultEvent struct{…}`

    Event sent by the client providing the result of a custom tool execution.

    - `ID string`

      Unique identifier for this event.

    - `CustomToolUseID string`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type BetaManagedAgentsUserCustomToolResultEventType`

    - `Content []BetaManagedAgentsUserCustomToolResultEventContentUnion Optional`

      The result content returned by the tool.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `type BetaManagedAgentsSearchResultBlock struct{…}`

        A block containing a web search result.

        - `Citations BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `Enabled bool`

            Whether citations are enabled for this search result.

        - `Content []BetaManagedAgentsSearchResultContent`

          Array of text content blocks from the search result.

          - `Text string`

            The text content.

            minLength: 1

          - `Type BetaManagedAgentsSearchResultContentType`

        - `Source string`

          The URL source of the search result.

          minLength: 1

        - `Title string`

          The title of the search result.

          minLength: 1

        - `Type BetaManagedAgentsSearchResultBlockType`

    - `IsError bool Optional`

      Whether the tool execution resulted in an error.

    - `ProcessedAt Time Optional`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string Optional`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `type BetaManagedAgentsAgentCustomToolUseEvent struct{…}`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `ID string`

      Unique identifier for this event.

    - `Input map[string, any]`

      Input parameters for the tool call.

    - `Name string`

      Name of the custom tool being called.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsAgentCustomToolUseEventType`

    - `SessionThreadID string Optional`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `type BetaManagedAgentsAgentMessageEvent struct{…}`

    An agent response event in the session conversation.

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsAgentMessageEventContentUnion`

      Array of text blocks comprising the agent response.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

      - `type BetaManagedAgentsRedactedBlockParam struct{…}`

        Placeholder for content withheld by Anthropic model policy.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsAgentMessageEventType`

  - `type BetaManagedAgentsAgentThinkingEvent struct{…}`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsAgentThinkingEventType`

  - `type BetaManagedAgentsAgentMCPToolUseEvent struct{…}`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `ID string`

      Unique identifier for this event.

    - `Input map[string, any]`

      Input parameters for the tool call.

    - `MCPServerName string`

      Name of the MCP server providing the tool.

    - `Name string`

      Name of the MCP tool being used.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsAgentMCPToolUseEventType`

    - `EvaluatedPermission BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission Optional`

      AgentEvaluatedPermission enum

      - `const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionAllow BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "allow"`

      - `const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionAsk BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "ask"`

      - `const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionDeny BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "deny"`

    - `SessionThreadID string Optional`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `type BetaManagedAgentsAgentMCPToolResultEvent struct{…}`

    Event representing the result of an MCP tool execution.

    - `ID string`

      Unique identifier for this event.

    - `MCPToolUseID string`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsAgentMCPToolResultEventType`

    - `Content []BetaManagedAgentsAgentMCPToolResultEventContentUnion Optional`

      The result content returned by the tool.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `type BetaManagedAgentsSearchResultBlock struct{…}`

        A block containing a web search result.

    - `IsError bool Optional`

      Whether the tool execution resulted in an error.

  - `type BetaManagedAgentsAgentToolUseEvent struct{…}`

    Event emitted when the agent invokes a built-in agent tool.

    - `ID string`

      Unique identifier for this event.

    - `Input map[string, any]`

      Input parameters for the tool call.

    - `Name string`

      Name of the agent tool being used.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsAgentToolUseEventType`

    - `EvaluatedPermission BetaManagedAgentsAgentToolUseEventEvaluatedPermission Optional`

      AgentEvaluatedPermission enum

      - `const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionAllow BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "allow"`

      - `const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionAsk BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "ask"`

      - `const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionDeny BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "deny"`

    - `SessionThreadID string Optional`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `type BetaManagedAgentsAgentToolResultEvent struct{…}`

    Event representing the result of an agent tool execution.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `ToolUseID string`

      The id of the `agent.tool_use` event this result corresponds to.

    - `Type BetaManagedAgentsAgentToolResultEventType`

    - `Content []BetaManagedAgentsAgentToolResultEventContentUnion Optional`

      The result content returned by the tool.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `type BetaManagedAgentsSearchResultBlock struct{…}`

        A block containing a web search result.

    - `IsError bool Optional`

      Whether the tool execution resulted in an error.

  - `type BetaManagedAgentsAgentThreadMessageReceivedEvent struct{…}`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsAgentThreadMessageReceivedEventContentUnion`

      Message content blocks.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `type BetaManagedAgentsRedactedBlockParam struct{…}`

        Placeholder for content withheld by Anthropic model policy.

    - `FromSessionThreadID string`

      Public `sthr_` ID of the thread that sent the message.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsAgentThreadMessageReceivedEventType`

    - `FromAgentName string Optional`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `type BetaManagedAgentsAgentThreadMessageSentEvent struct{…}`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsAgentThreadMessageSentEventContentUnion`

      Message content blocks.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `type BetaManagedAgentsRedactedBlockParam struct{…}`

        Placeholder for content withheld by Anthropic model policy.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `ToSessionThreadID string`

      Public `sthr_` ID of the thread the message was sent to.

    - `Type BetaManagedAgentsAgentThreadMessageSentEventType`

    - `ToAgentName string Optional`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `type BetaManagedAgentsAgentThreadContextCompactedEvent struct{…}`

    Indicates that context compaction (summarization) occurred during the session.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsAgentThreadContextCompactedEventType`

  - `type BetaManagedAgentsSessionErrorEvent struct{…}`

    An error event indicating a problem occurred during session execution.

    - `ID string`

      Unique identifier for this event.

    - `Error BetaManagedAgentsSessionErrorEventErrorUnion`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `type BetaManagedAgentsUnknownError struct{…}`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsUnknownErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type BetaManagedAgentsRetryStatusRetryingType`

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type BetaManagedAgentsRetryStatusExhaustedType`

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type BetaManagedAgentsRetryStatusTerminalType`

        - `Type BetaManagedAgentsUnknownErrorType`

      - `type BetaManagedAgentsModelOverloadedError struct{…}`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsModelOverloadedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type BetaManagedAgentsModelOverloadedErrorType`

      - `type BetaManagedAgentsModelRateLimitedError struct{…}`

        The model request was rate-limited.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsModelRateLimitedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type BetaManagedAgentsModelRateLimitedErrorType`

      - `type BetaManagedAgentsModelRequestFailedError struct{…}`

        A model request failed for a reason other than overload or rate-limiting.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsModelRequestFailedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type BetaManagedAgentsModelRequestFailedErrorType`

      - `type BetaManagedAgentsMCPConnectionFailedError struct{…}`

        Failed to connect to an MCP server.

        - `MCPServerName string`

          Name of the MCP server that failed to connect.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsMCPConnectionFailedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type BetaManagedAgentsMCPConnectionFailedErrorType`

      - `type BetaManagedAgentsMCPAuthenticationFailedError struct{…}`

        Authentication to an MCP server failed.

        - `MCPServerName string`

          Name of the MCP server that failed authentication.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsMCPAuthenticationFailedErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type BetaManagedAgentsMCPAuthenticationFailedErrorType`

      - `type BetaManagedAgentsBillingError struct{…}`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsBillingErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type BetaManagedAgentsBillingErrorType`

      - `type BetaManagedAgentsCredentialHostUnreachableError struct{…}`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `CredentialID string`

          ID of the affected credential.

        - `Message string`

          Human-readable error description.

        - `RetryStatus BetaManagedAgentsCredentialHostUnreachableErrorRetryStatusUnion`

          What the client should do next in response to this error.

          - `type BetaManagedAgentsRetryStatusRetrying struct{…}`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `type BetaManagedAgentsRetryStatusExhausted struct{…}`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `type BetaManagedAgentsRetryStatusTerminal struct{…}`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type BetaManagedAgentsCredentialHostUnreachableErrorType`

        - `VaultID string`

          ID of the vault containing the affected credential.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSessionErrorEventType`

  - `type BetaManagedAgentsSessionStatusRescheduledEvent struct{…}`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSessionStatusRescheduledEventType`

  - `type BetaManagedAgentsSessionStatusRunningEvent struct{…}`

    Indicates the session is actively running and the agent is working.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSessionStatusRunningEventType`

  - `type BetaManagedAgentsSessionStatusIdleEvent struct{…}`

    Indicates the agent has paused and is awaiting user input.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `StopReason BetaManagedAgentsSessionStatusIdleEventStopReasonUnion`

      The agent completed its turn naturally and is ready for the next user message.

      - `type BetaManagedAgentsSessionEndTurn struct{…}`

        The agent completed its turn naturally and is ready for the next user message.

        - `Type BetaManagedAgentsSessionEndTurnType`

      - `type BetaManagedAgentsSessionRequiresAction struct{…}`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `EventIDs []string`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `Type BetaManagedAgentsSessionRequiresActionType`

      - `type BetaManagedAgentsSessionRetriesExhausted struct{…}`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `Type BetaManagedAgentsSessionRetriesExhaustedType`

      - `type BetaManagedAgentsSessionBudgetReached struct{…}`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `Type BetaManagedAgentsSessionBudgetReachedType`

    - `Type BetaManagedAgentsSessionStatusIdleEventType`

  - `type BetaManagedAgentsSessionStatusTerminatedEvent struct{…}`

    Indicates the session has terminated, either due to an error or completion.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSessionStatusTerminatedEventType`

  - `type BetaManagedAgentsSessionThreadCreatedEvent struct{…}`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the callable agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string`

      Public `sthr_` ID of the newly created thread.

    - `Type BetaManagedAgentsSessionThreadCreatedEventType`

  - `type BetaManagedAgentsSpanOutcomeEvaluationStartEvent struct{…}`

    Emitted when an outcome evaluation cycle begins.

    - `ID string`

      Unique identifier for this event.

    - `Iteration int64`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

      format: int32

    - `OutcomeID string`

      The `outc_` ID of the outcome being evaluated.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSpanOutcomeEvaluationStartEventType`

  - `type BetaManagedAgentsSpanOutcomeEvaluationEndEvent struct{…}`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `ID string`

      Unique identifier for this event.

    - `Explanation string`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `Iteration int64`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `OutcomeEvaluationStartID string`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `OutcomeID string`

      The `outc_` ID of the outcome being evaluated.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Result string`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `Type BetaManagedAgentsSpanOutcomeEvaluationEndEventType`

    - `Usage BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `CacheCreationInputTokens int64`

        Tokens used to create prompt cache in this request.

        format: int32

      - `CacheReadInputTokens int64`

        Tokens read from prompt cache in this request.

        format: int32

      - `InputTokens int64`

        Input tokens consumed by this request.

        format: int32

      - `OutputTokens int64`

        Output tokens generated by this request.

        format: int32

      - `Speed BetaManagedAgentsSpanModelUsageSpeed Optional`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `const BetaManagedAgentsSpanModelUsageSpeedStandard BetaManagedAgentsSpanModelUsageSpeed = "standard"`

        - `const BetaManagedAgentsSpanModelUsageSpeedFast BetaManagedAgentsSpanModelUsageSpeed = "fast"`

  - `type BetaManagedAgentsSpanModelRequestStartEvent struct{…}`

    Emitted when a model request is initiated by the agent.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSpanModelRequestStartEventType`

  - `type BetaManagedAgentsSpanModelRequestEndEvent struct{…}`

    Emitted when a model request completes.

    - `ID string`

      Unique identifier for this event.

    - `IsError bool`

      Whether the model request resulted in an error.

    - `ModelRequestStartID string`

      The id of the corresponding `span.model_request_start` event.

    - `ModelUsage BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSpanModelRequestEndEventType`

  - `type BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent struct{…}`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `ID string`

      Unique identifier for this event.

    - `Iteration int64`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `OutcomeID string`

      The `outc_` ID of the outcome being evaluated.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSpanOutcomeEvaluationOngoingEventType`

  - `type BetaManagedAgentsUserDefineOutcomeEvent struct{…}`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `ID string`

      Unique identifier for this event.

    - `Description string`

      What the agent should produce. Copied from the input event.

    - `MaxIterations int64`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

      format: int32

    - `OutcomeID string`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Rubric BetaManagedAgentsUserDefineOutcomeEventRubricUnion`

      Rubric for grading the quality of an outcome.

      - `type BetaManagedAgentsFileRubric struct{…}`

        Rubric referenced by a file uploaded via the Files API.

        - `FileID string`

          ID of the rubric file.

        - `Type BetaManagedAgentsFileRubricType`

      - `type BetaManagedAgentsTextRubric struct{…}`

        Rubric content provided inline as text.

        - `Content string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `Type BetaManagedAgentsTextRubricType`

    - `Type BetaManagedAgentsUserDefineOutcomeEventType`

  - `type BetaManagedAgentsSessionDeletedEvent struct{…}`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSessionDeletedEventType`

  - `type BetaManagedAgentsSessionThreadStatusRunningEvent struct{…}`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string`

      Public sthr_ ID of the thread that started running.

    - `Type BetaManagedAgentsSessionThreadStatusRunningEventType`

  - `type BetaManagedAgentsSessionThreadStatusIdleEvent struct{…}`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string`

      Public sthr_ ID of the thread that went idle.

    - `StopReason BetaManagedAgentsSessionThreadStatusIdleEventStopReasonUnion`

      The agent completed its turn naturally and is ready for the next user message.

      - `type BetaManagedAgentsSessionEndTurn struct{…}`

        The agent completed its turn naturally and is ready for the next user message.

      - `type BetaManagedAgentsSessionRequiresAction struct{…}`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `type BetaManagedAgentsSessionRetriesExhausted struct{…}`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `type BetaManagedAgentsSessionBudgetReached struct{…}`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

    - `Type BetaManagedAgentsSessionThreadStatusIdleEventType`

  - `type BetaManagedAgentsSessionThreadStatusTerminatedEvent struct{…}`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string`

      Public sthr_ ID of the thread that terminated.

    - `Type BetaManagedAgentsSessionThreadStatusTerminatedEventType`

  - `type BetaManagedAgentsUserToolResultEvent struct{…}`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `ID string`

      Unique identifier for this event.

    - `ToolUseID string`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type BetaManagedAgentsUserToolResultEventType`

    - `Content []BetaManagedAgentsUserToolResultEventContentUnion Optional`

      The result content returned by the tool.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `type BetaManagedAgentsSearchResultBlock struct{…}`

        A block containing a web search result.

    - `IsError bool Optional`

      Whether the tool execution resulted in an error.

    - `ProcessedAt Time Optional`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string Optional`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `type BetaManagedAgentsSessionThreadStatusRescheduledEvent struct{…}`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `ID string`

      Unique identifier for this event.

    - `AgentName string`

      Name of the agent the thread runs.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `SessionThreadID string`

      Public sthr_ ID of the thread that is retrying.

    - `Type BetaManagedAgentsSessionThreadStatusRescheduledEventType`

  - `type BetaManagedAgentsSessionUpdatedEvent struct{…}`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSessionUpdatedEventType`

    - `Agent BetaManagedAgentsSessionAgent Optional`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `ID string`

      - `Description string`

      - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

        - `Name string`

        - `Type BetaManagedAgentsMCPServerURLDefinitionType`

        - `URL string`

      - `Model BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `ID BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `type BetaManagedAgentsModel string`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `const BetaManagedAgentsModelClaudeSonnet5 BetaManagedAgentsModel = "claude-sonnet-5"`

              High-performance model for coding and agents

            - `const BetaManagedAgentsModelClaudeFable5 BetaManagedAgentsModel = "claude-fable-5"`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `const BetaManagedAgentsModelClaudeOpus5 BetaManagedAgentsModel = "claude-opus-5"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeOpus4_8 BetaManagedAgentsModel = "claude-opus-4-8"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeOpus4_7 BetaManagedAgentsModel = "claude-opus-4-7"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeOpus4_6 BetaManagedAgentsModel = "claude-opus-4-6"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeSonnet4_6 BetaManagedAgentsModel = "claude-sonnet-4-6"`

              Best combination of speed and intelligence

            - `const BetaManagedAgentsModelClaudeHaiku4_5 BetaManagedAgentsModel = "claude-haiku-4-5"`

              Fastest model with near-frontier intelligence

            - `const BetaManagedAgentsModelClaudeHaiku4_5_20251001 BetaManagedAgentsModel = "claude-haiku-4-5-20251001"`

              Fastest model with near-frontier intelligence

            - `const BetaManagedAgentsModelClaudeOpus4_5 BetaManagedAgentsModel = "claude-opus-4-5"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeOpus4_5_20251101 BetaManagedAgentsModel = "claude-opus-4-5-20251101"`

              Powerful intelligence for long-running agents and coding

            - `const BetaManagedAgentsModelClaudeSonnet4_5 BetaManagedAgentsModel = "claude-sonnet-4-5"`

              High-performance model for agents and coding

            - `const BetaManagedAgentsModelClaudeSonnet4_5_20250929 BetaManagedAgentsModel = "claude-sonnet-4-5-20250929"`

              High-performance model for agents and coding

          - `string`

        - `Effort BetaManagedAgentsModelConfigEffortUnion Optional`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `type BetaManagedAgentsEffortLow struct{…}`

            Low effort. Favors latency over reasoning depth.

            - `Type BetaManagedAgentsEffortLowType`

          - `type BetaManagedAgentsEffortMedium struct{…}`

            Medium effort. Balances latency and reasoning depth.

            - `Type BetaManagedAgentsEffortMediumType`

          - `type BetaManagedAgentsEffortHigh struct{…}`

            High effort. Favors reasoning depth.

            - `Type BetaManagedAgentsEffortHighType`

          - `type BetaManagedAgentsEffortXhigh struct{…}`

            Extra-high effort. Not all models accept this level.

            - `Type BetaManagedAgentsEffortXhighType`

          - `type BetaManagedAgentsEffortMax struct{…}`

            Maximum effort. Favors reasoning depth over latency.

            - `Type BetaManagedAgentsEffortMaxType`

        - `InferenceGeo string Optional`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `Speed BetaManagedAgentsModelConfigSpeed Optional`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `const BetaManagedAgentsModelConfigSpeedStandard BetaManagedAgentsModelConfigSpeed = "standard"`

          - `const BetaManagedAgentsModelConfigSpeedFast BetaManagedAgentsModelConfigSpeed = "fast"`

      - `Multiagent BetaManagedAgentsSessionMultiagentCoordinator`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `Agents []BetaManagedAgentsSessionMultiagentCoordinatorAgentUnion`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `type BetaManagedAgentsSessionThreadAgent struct{…}`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `ID string`

            - `Description string`

            - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

              - `Name string`

              - `Type BetaManagedAgentsMCPServerURLDefinitionType`

              - `URL string`

            - `Model BetaManagedAgentsModelConfig`

              Model identifier and configuration.

            - `Name string`

            - `Skills []BetaManagedAgentsSessionThreadAgentSkillUnion`

              - `type BetaManagedAgentsAnthropicSkill struct{…}`

                A resolved Anthropic-managed skill.

                - `SkillID string`

                - `Type BetaManagedAgentsAnthropicSkillType`

                - `Version string`

              - `type BetaManagedAgentsCustomSkill struct{…}`

                A resolved user-created custom skill.

                - `SkillID string`

                - `Type BetaManagedAgentsCustomSkillType`

                - `Version string`

            - `System string`

            - `Tools []BetaManagedAgentsSessionThreadAgentToolUnion`

              - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

                - `Configs []BetaManagedAgentsAgentToolConfigUnion`

                  - `type BetaManagedAgentsBashToolConfig struct{…}`

                    Configuration for the bash tool.

                    - `Enabled bool`

                    - `Name Bash`

                    - `PermissionPolicy BetaManagedAgentsBashToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                        - `Type BetaManagedAgentsAlwaysAllowPolicyType`

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                        - `Type BetaManagedAgentsAlwaysAskPolicyType`

                    - `Type Bash`

                  - `type BetaManagedAgentsEditToolConfig struct{…}`

                    Configuration for the edit tool.

                    - `Enabled bool`

                    - `Name Edit`

                    - `PermissionPolicy BetaManagedAgentsEditToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                    - `Type Edit`

                  - `type BetaManagedAgentsReadToolConfig struct{…}`

                    Configuration for the read tool.

                    - `Enabled bool`

                    - `Name Read`

                    - `PermissionPolicy BetaManagedAgentsReadToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                    - `Type Read`

                  - `type BetaManagedAgentsWriteToolConfig struct{…}`

                    Configuration for the write tool.

                    - `Enabled bool`

                    - `Name Write`

                    - `PermissionPolicy BetaManagedAgentsWriteToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                    - `Type Write`

                  - `type BetaManagedAgentsGlobToolConfig struct{…}`

                    Configuration for the glob tool.

                    - `Enabled bool`

                    - `Name Glob`

                    - `PermissionPolicy BetaManagedAgentsGlobToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                    - `Type Glob`

                  - `type BetaManagedAgentsGrepToolConfig struct{…}`

                    Configuration for the grep tool.

                    - `Enabled bool`

                    - `Name Grep`

                    - `PermissionPolicy BetaManagedAgentsGrepToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                    - `Type Grep`

                  - `type BetaManagedAgentsWebFetchToolConfig struct{…}`

                    Configuration for the web_fetch tool.

                    - `Enabled bool`

                    - `Name WebFetch`

                    - `PermissionPolicy BetaManagedAgentsWebFetchToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                    - `Type WebFetch`

                    - `AllowedDomains []string Optional`

                    - `BlockedDomains []string Optional`

                    - `MaxContentTokens int64 Optional`

                      format: int32

                  - `type BetaManagedAgentsWebSearchToolConfig struct{…}`

                    Configuration for the web_search tool.

                    - `Enabled bool`

                    - `Name WebSearch`

                    - `PermissionPolicy BetaManagedAgentsWebSearchToolConfigPermissionPolicyUnion`

                      Permission policy for tool execution.

                      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                        Tool calls are automatically approved without user confirmation.

                      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                        Tool calls require user confirmation before execution.

                    - `Type WebSearch`

                    - `AllowedDomains []string Optional`

                    - `BlockedDomains []string Optional`

                    - `UserLocation BetaManagedAgentsUserLocation Optional`

                      Approximate user location for search result localization.

                      - `Type Approximate`

                        Location precision. Only "approximate" is supported.

                      - `City string Optional`

                        City name.

                        minLength: 1, maxLength: 255

                      - `Country string Optional`

                        Two-letter ISO 3166-1 country code, uppercase.

                      - `Region string Optional`

                        Region or state name.

                        minLength: 1, maxLength: 255

                      - `Timezone string Optional`

                        IANA timezone identifier, e.g. "America/Los_Angeles".

                        minLength: 1, maxLength: 255

                - `DefaultConfig BetaManagedAgentsAgentToolsetDefaultConfig`

                  Resolved default configuration for agent tools.

                  - `Enabled bool`

                  - `PermissionPolicy BetaManagedAgentsAgentToolsetDefaultConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                - `Type BetaManagedAgentsAgentToolset20260401Type`

              - `type BetaManagedAgentsMCPToolset struct{…}`

                - `Configs []BetaManagedAgentsMCPToolConfig`

                  - `Enabled bool`

                  - `Name string`

                  - `PermissionPolicy BetaManagedAgentsMCPToolConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                - `DefaultConfig BetaManagedAgentsMCPToolsetDefaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `Enabled bool`

                  - `PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigPermissionPolicyUnion`

                    Permission policy for tool execution.

                    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

                      Tool calls are automatically approved without user confirmation.

                    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

                      Tool calls require user confirmation before execution.

                - `MCPServerName string`

                - `Type BetaManagedAgentsMCPToolsetType`

              - `type BetaManagedAgentsCustomTool struct{…}`

                A custom tool as returned in API responses.

                - `Description string`

                - `InputSchema BetaManagedAgentsCustomToolInputSchema`

                  JSON Schema for custom tool input parameters.

                  - `Type Object`

                  - `Properties map[string, any] Optional`

                  - `Required []string Optional`

                - `Name string`

                - `Type BetaManagedAgentsCustomToolType`

            - `Type BetaManagedAgentsSessionThreadAgentType`

            - `Version int64`

              format: int32

          - `type BetaManagedAgentsAdvisor struct{…}`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `Model string`

              The advisor model id.

            - `Type BetaManagedAgentsAdvisorType`

        - `Type BetaManagedAgentsSessionMultiagentCoordinatorType`

      - `Name string`

      - `Skills []BetaManagedAgentsSessionAgentSkillUnion`

        - `type BetaManagedAgentsAnthropicSkill struct{…}`

          A resolved Anthropic-managed skill.

        - `type BetaManagedAgentsCustomSkill struct{…}`

          A resolved user-created custom skill.

      - `System string`

      - `Tools []BetaManagedAgentsSessionAgentToolUnion`

        - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

        - `type BetaManagedAgentsMCPToolset struct{…}`

        - `type BetaManagedAgentsCustomTool struct{…}`

          A custom tool as returned in API responses.

      - `Type BetaManagedAgentsSessionAgentType`

      - `Version int64`

        format: int32

    - `Budget BetaManagedAgentsBudgetLimit Optional`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `MaxListCost BetaMonetaryAmount`

        A monetary amount in a specific currency.

        - `Amount string`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `Currency BetaCurrency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `Type BetaManagedAgentsBudgetLimitType`

    - `Metadata map[string, string] Optional`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `Title string Optional`

      The session's new title. Present only when the update changed it.

  - `type BetaManagedAgentsStartEvent struct{…}`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `Event BetaManagedAgentsStartEventPreviewUnion`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

      - `type BetaManagedAgentsAgentMessagePreview struct{…}`

        - `ID string`

          The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

        - `Type BetaManagedAgentsAgentMessagePreviewType`

      - `type BetaManagedAgentsAgentThinkingPreview struct{…}`

        - `ID string`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

        - `Type BetaManagedAgentsAgentThinkingPreviewType`

    - `Type BetaManagedAgentsStartEventType`

  - `type BetaManagedAgentsDeltaEvent struct{…}`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `Delta BetaManagedAgentsDeltaContent`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `Content BetaManagedAgentsTextBlock`

        Regular text content.

      - `Type BetaManagedAgentsDeltaContentType`

      - `Index int64 Optional`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

        format: uint32

    - `EventID string`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

    - `Type BetaManagedAgentsDeltaEventType`

  - `type BetaManagedAgentsSystemMessageEvent struct{…}`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `ID string`

      Unique identifier for this event.

    - `Content []BetaManagedAgentsSystemContentBlock`

      System content blocks. Text-only.

      - `Text string`

        The text content.

        minLength: 1

      - `Type BetaManagedAgentsSystemContentBlockType`

    - `Type BetaManagedAgentsSystemMessageEventType`

    - `ProcessedAt Time Optional`

      A timestamp in RFC 3339 format

      format: date-time

  - `type BetaManagedAgentsSessionUsageEvent struct{…}`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `ID string`

      Unique identifier for this event.

    - `ProcessedAt Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type BetaManagedAgentsSessionUsageEventType`

    - `Usage BetaManagedAgentsSessionUsageSnapshot`

      Point-in-time snapshot of a session's cumulative usage.

      - `ActiveSeconds float64 Optional`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `CacheCreation BetaManagedAgentsCacheCreationUsage Optional`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `Ephemeral1hInputTokens int64 Optional`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `Ephemeral5mInputTokens int64 Optional`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `CacheReadInputTokens int64 Optional`

        Total tokens read from prompt cache.

        format: int32

      - `InputTokens int64 Optional`

        Total input tokens consumed across all turns.

        format: int32

      - `ListCost BetaMonetaryAmount Optional`

        A monetary amount in a specific currency.

      - `OutputTokens int64 Optional`

        Total output tokens generated across all turns.

        format: int32

      - `ServerToolUse BetaManagedAgentsServerToolUsage Optional`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `WebFetchRequests int64 Optional`

          Number of server-executed web fetch requests.

          format: int32

        - `WebSearchRequests int64 Optional`

          Number of server-executed web search requests.

          format: int32

    - `Budget BetaManagedAgentsBudgetLimit Optional`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

- `type BetaManagedAgentsStreamSessionThreadEventsUnion interface{…}`

  Server-sent event in a single thread's stream.

#### Example

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
	stream := client.Beta.Sessions.Threads.Events.StreamEvents(
		context.TODO(),
		"sthr_011CZkZVWa6oIjw0rgXZpnBt",
		anthropic.BetaSessionThreadEventStreamParams{
			SessionID: "sesn_011CZkZAtmR3yMPDzynEDxu7",
		},
	)
	for stream.Next() {
		fmt.Printf("%+v\n", stream.Current())
	}
	err := stream.Err()
	if err != nil {
		panic(err.Error())
	}
}
```

##### Response (200)

```json
{
  "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
  "content": [
    {
      "text": "Where is my order #1234?",
      "type": "text"
    }
  ],
  "type": "user.message",
  "processed_at": "2026-03-15T10:00:00Z"
}
```
