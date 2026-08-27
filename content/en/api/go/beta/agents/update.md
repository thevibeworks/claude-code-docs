# Update Agent

`client.Beta.Agents.Update(ctx, agentID, params) (*BetaManagedAgentsAgent, error)`

**POST** `/v1/agents/{agent_id}`

Update Agent

## Parameters

- `agentID string`

- `params BetaAgentUpdateParams`

  - `Description param.Field[string] Optional`

    Body param: Description. Omit to preserve; send empty string or null to clear.

    maxLength: 2048

  - `MCPServers param.Field[[]BetaManagedAgentsURLMCPServerParamsResp] Optional`

    Body param: MCP servers. Full replacement. Omit to preserve; send empty array or `null` to clear. Names must be unique. Maximum 20. Every server must be referenced by an `mcp_toolset` in the agent's resulting `tools`; unreferenced servers are rejected. See the [MCP connector guide](https://platform.claude.com/docs/en/managed-agents/mcp-connector).

    - `Name string`

      Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

      minLength: 1, maxLength: 255

    - `Type BetaManagedAgentsURLMCPServerParamsType`

    - `URL string`

      Endpoint URL for the MCP server.

      maxLength: 2048

  - `Metadata param.Field[map[string, string]] Optional`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

  - `Model param.Field[BetaManagedAgentsModelConfigParamsResp] Optional`

    Body param: Model identifier. Accepts the [model string](https://platform.claude.com/docs/en/about-claude/models/overview#latest-models-comparison), e.g. `claude-opus-5`, or a `model_config` object for additional configuration control. Omit to preserve. Cannot be cleared.

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

  - `Multiagent param.Field[BetaManagedAgentsMultiagentParamsResp] Optional`

    Body param: A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.

  - `Name param.Field[string] Optional`

    Body param: Human-readable name. Must be non-empty. Omit to preserve. Cannot be cleared.

    maxLength: 256

  - `Skills param.Field[[]BetaManagedAgentsSkillParamsUnionResp] Optional`

    Body param: Skills. Full replacement. Omit to preserve; send empty array or null to clear.

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

  - `System param.Field[string] Optional`

    Body param: System prompt. Omit to preserve; send empty string or null to clear.

    maxLength: 100000

  - `Tools param.Field[[]BetaAgentUpdateParamsToolUnion] Optional`

    Body param: Tool configurations available to the agent. Full replacement. Omit to preserve; send empty array or null to clear. Maximum of 128 tools across all toolsets allowed.

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

  - `Version param.Field[int64] Optional`

    Body param: The agent's current version, used to prevent concurrent overwrites. Obtain this value from a create or retrieve response. Must be at least 1 if specified. When supplied, the request fails if it does not match the server's current version; omit to apply the update unconditionally.

    format: int32

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

- `type BetaManagedAgentsAgent struct{…}`

  A Managed Agents `agent`.

  - `ID string`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `Description string`

  - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

    - `Name string`

    - `Type BetaManagedAgentsMCPServerURLDefinitionType`

    - `URL string`

  - `Metadata map[string, string]`

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

  - `Multiagent BetaManagedAgentsMultiagent`

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

  - `Name string`

  - `Skills []BetaManagedAgentsAgentSkillUnion`

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

  - `Tools []BetaManagedAgentsAgentToolUnion`

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

  - `Type BetaManagedAgentsAgentType`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `Version int64`

    The agent's current version. Starts at 1 and increments when the agent is modified.

    format: int32

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
	betaManagedAgentsAgent, err := client.Beta.Agents.Update(
		context.TODO(),
		"agent_011CZkYpogX7uDKUyvBTophP",
		anthropic.BetaAgentUpdateParams{
			Description: anthropic.String("updated"),
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaManagedAgentsAgent.ID)
}
```

### Response (200)

```json
{
  "id": "agent_011CZkYpogX7uDKUyvBTophP",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "A general-purpose starter agent.",
  "mcp_servers": [
    {
      "name": "example-mcp",
      "type": "url",
      "url": "https://example-server.modelcontextprotocol.io/sse"
    }
  ],
  "metadata": {
    "foo": "bar"
  },
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
  "updated_at": "2026-03-15T10:00:00Z",
  "version": 1
}
```
