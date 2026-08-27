# Create Session

`client.Beta.Sessions.New(ctx, params) (*BetaManagedAgentsSession, error)`

**POST** `/v1/sessions`

Create Session

## Parameters

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

## Returns

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

### Response (200)

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
