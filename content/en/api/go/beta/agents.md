---
title: Agents
url: https://platform.claude.com/docs/en/api/go/beta/agents
---

# Agents

## Create Agent

`client.Beta.Agents.New(ctx, params) (*BetaManagedAgentsAgent, error)`

**post** `/v1/agents`

Create Agent

### Parameters

- `params BetaAgentNewParams`

  - `Model param.Field[BetaManagedAgentsModelConfigParamsResp]`

    Body param: Model identifier. Accepts the [model string](https://platform.claude.com/docs/en/about-claude/models/overview#latest-models-comparison), e.g. `claude-opus-5`, or a `model_config` object for additional configuration control

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

      - `Effort BetaManagedAgentsModelConfigParamsEffortUnionResp`

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

            - `const BetaManagedAgentsEffortLowTypeLow BetaManagedAgentsEffortLowType = "low"`

        - `type BetaManagedAgentsEffortMedium struct{…}`

          Medium effort. Balances latency and reasoning depth.

          - `Type BetaManagedAgentsEffortMediumType`

            - `const BetaManagedAgentsEffortMediumTypeMedium BetaManagedAgentsEffortMediumType = "medium"`

        - `type BetaManagedAgentsEffortHigh struct{…}`

          High effort. Favors reasoning depth.

          - `Type BetaManagedAgentsEffortHighType`

            - `const BetaManagedAgentsEffortHighTypeHigh BetaManagedAgentsEffortHighType = "high"`

        - `type BetaManagedAgentsEffortXhigh struct{…}`

          Extra-high effort. Not all models accept this level.

          - `Type BetaManagedAgentsEffortXhighType`

            - `const BetaManagedAgentsEffortXhighTypeXhigh BetaManagedAgentsEffortXhighType = "xhigh"`

        - `type BetaManagedAgentsEffortMax struct{…}`

          Maximum effort. Favors reasoning depth over latency.

          - `Type BetaManagedAgentsEffortMaxType`

            - `const BetaManagedAgentsEffortMaxTypeMax BetaManagedAgentsEffortMaxType = "max"`

      - `InferenceGeo string`

        Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo. On update, `model` is whole-object replacement — omitting inference_geo clears it.

      - `Speed BetaManagedAgentsModelConfigParamsSpeed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `const BetaManagedAgentsModelConfigParamsSpeedStandard BetaManagedAgentsModelConfigParamsSpeed = "standard"`

        - `const BetaManagedAgentsModelConfigParamsSpeedFast BetaManagedAgentsModelConfigParamsSpeed = "fast"`

  - `Name param.Field[string]`

    Body param: Human-readable name for the agent.

  - `Description param.Field[string]`

    Body param: Description of what the agent does.

  - `MCPServers param.Field[[]BetaManagedAgentsURLMCPServerParamsResp]`

    Body param: MCP servers this agent connects to. Maximum 20. Names must be unique within the array. Every server must be referenced by an `mcp_toolset` in `tools`; unreferenced servers are rejected. See the [MCP connector guide](https://platform.claude.com/docs/en/managed-agents/mcp-connector).

    - `Name string`

      Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

    - `Type BetaManagedAgentsURLMCPServerParamsType`

      - `const BetaManagedAgentsURLMCPServerParamsTypeURL BetaManagedAgentsURLMCPServerParamsType = "url"`

    - `URL string`

      Endpoint URL for the MCP server.

  - `Metadata param.Field[map[string, string]]`

    Body param: Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `Multiagent param.Field[BetaManagedAgentsMultiagentParamsResp]`

    Body param: A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.

  - `Skills param.Field[[]BetaManagedAgentsSkillParamsUnionResp]`

    Body param: Skills available to the agent.

    - `type BetaManagedAgentsAnthropicSkillParamsResp struct{…}`

      An Anthropic-managed skill.

      - `SkillID string`

        Identifier of the Anthropic skill (e.g., "xlsx").

      - `Type BetaManagedAgentsAnthropicSkillParamsType`

        - `const BetaManagedAgentsAnthropicSkillParamsTypeAnthropic BetaManagedAgentsAnthropicSkillParamsType = "anthropic"`

      - `Version string`

        Version to pin. Defaults to latest if omitted.

    - `type BetaManagedAgentsCustomSkillParamsResp struct{…}`

      A user-created custom skill.

      - `SkillID string`

        Tagged ID of the custom skill (e.g., "skill_01XJ5...").

      - `Type BetaManagedAgentsCustomSkillParamsType`

        - `const BetaManagedAgentsCustomSkillParamsTypeCustom BetaManagedAgentsCustomSkillParamsType = "custom"`

      - `Version string`

        Version to pin. Defaults to latest if omitted.

  - `System param.Field[string]`

    Body param: System prompt for the agent.

  - `Tools param.Field[[]BetaAgentNewParamsToolUnion]`

    Body param: Tool configurations available to the agent. Maximum of 128 tools across all toolsets allowed.

    - `type BetaManagedAgentsAgentToolset20260401ParamsResp struct{…}`

      Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

      - `Type BetaManagedAgentsAgentToolset20260401ParamsType`

        - `const BetaManagedAgentsAgentToolset20260401ParamsTypeAgentToolset20260401 BetaManagedAgentsAgentToolset20260401ParamsType = "agent_toolset_20260401"`

      - `Configs []BetaManagedAgentsAgentToolConfigParamsUnionResp`

        Per-tool configuration overrides.

        - `type BetaManagedAgentsBashToolConfigParamsResp struct{…}`

          Configuration override for the bash tool.

          - `Name Bash`

            Must be "bash".

            - `const BashBash Bash = "bash"`

          - `Enabled bool`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy BetaManagedAgentsBashToolConfigParamsPermissionPolicyUnionResp`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

              - `Type BetaManagedAgentsAlwaysAllowPolicyType`

                - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

              - `Type BetaManagedAgentsAlwaysAskPolicyType`

                - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

          - `Type BetaManagedAgentsBashToolConfigParamsType`

            - `const BetaManagedAgentsBashToolConfigParamsTypeBash BetaManagedAgentsBashToolConfigParamsType = "bash"`

        - `type BetaManagedAgentsEditToolConfigParamsResp struct{…}`

          Configuration override for the edit tool.

          - `Name Edit`

            Must be "edit".

            - `const EditEdit Edit = "edit"`

          - `Enabled bool`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy BetaManagedAgentsEditToolConfigParamsPermissionPolicyUnionResp`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type BetaManagedAgentsEditToolConfigParamsType`

            - `const BetaManagedAgentsEditToolConfigParamsTypeEdit BetaManagedAgentsEditToolConfigParamsType = "edit"`

        - `type BetaManagedAgentsReadToolConfigParamsResp struct{…}`

          Configuration override for the read tool.

          - `Name Read`

            Must be "read".

            - `const ReadRead Read = "read"`

          - `Enabled bool`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy BetaManagedAgentsReadToolConfigParamsPermissionPolicyUnionResp`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type BetaManagedAgentsReadToolConfigParamsType`

            - `const BetaManagedAgentsReadToolConfigParamsTypeRead BetaManagedAgentsReadToolConfigParamsType = "read"`

        - `type BetaManagedAgentsWriteToolConfigParamsResp struct{…}`

          Configuration override for the write tool.

          - `Name Write`

            Must be "write".

            - `const WriteWrite Write = "write"`

          - `Enabled bool`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy BetaManagedAgentsWriteToolConfigParamsPermissionPolicyUnionResp`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type BetaManagedAgentsWriteToolConfigParamsType`

            - `const BetaManagedAgentsWriteToolConfigParamsTypeWrite BetaManagedAgentsWriteToolConfigParamsType = "write"`

        - `type BetaManagedAgentsGlobToolConfigParamsResp struct{…}`

          Configuration override for the glob tool.

          - `Name Glob`

            Must be "glob".

            - `const GlobGlob Glob = "glob"`

          - `Enabled bool`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy BetaManagedAgentsGlobToolConfigParamsPermissionPolicyUnionResp`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type BetaManagedAgentsGlobToolConfigParamsType`

            - `const BetaManagedAgentsGlobToolConfigParamsTypeGlob BetaManagedAgentsGlobToolConfigParamsType = "glob"`

        - `type BetaManagedAgentsGrepToolConfigParamsResp struct{…}`

          Configuration override for the grep tool.

          - `Name Grep`

            Must be "grep".

            - `const GrepGrep Grep = "grep"`

          - `Enabled bool`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy BetaManagedAgentsGrepToolConfigParamsPermissionPolicyUnionResp`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type BetaManagedAgentsGrepToolConfigParamsType`

            - `const BetaManagedAgentsGrepToolConfigParamsTypeGrep BetaManagedAgentsGrepToolConfigParamsType = "grep"`

        - `type BetaManagedAgentsWebFetchToolConfigParamsResp struct{…}`

          Configuration override for the web_fetch tool.

          - `Name WebFetch`

            Must be "web_fetch".

            - `const WebFetchWebFetch WebFetch = "web_fetch"`

          - `AllowedDomains []string`

            Only fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

          - `BlockedDomains []string`

            Never fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

          - `Enabled bool`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `MaxContentTokens int64`

            Maximum number of tokens of fetched text content to include in context per call. Does not apply to binary content such as PDFs.

          - `PermissionPolicy BetaManagedAgentsWebFetchToolConfigParamsPermissionPolicyUnionResp`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type BetaManagedAgentsWebFetchToolConfigParamsType`

            - `const BetaManagedAgentsWebFetchToolConfigParamsTypeWebFetch BetaManagedAgentsWebFetchToolConfigParamsType = "web_fetch"`

        - `type BetaManagedAgentsWebSearchToolConfigParamsResp struct{…}`

          Configuration override for the web_search tool.

          - `Name WebSearch`

            Must be "web_search".

            - `const WebSearchWebSearch WebSearch = "web_search"`

          - `AllowedDomains []string`

            Only return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

          - `BlockedDomains []string`

            Never return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

          - `Enabled bool`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy BetaManagedAgentsWebSearchToolConfigParamsPermissionPolicyUnionResp`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type BetaManagedAgentsWebSearchToolConfigParamsType`

            - `const BetaManagedAgentsWebSearchToolConfigParamsTypeWebSearch BetaManagedAgentsWebSearchToolConfigParamsType = "web_search"`

          - `UserLocation BetaManagedAgentsUserLocation`

            Approximate user location for search result localization.

            - `Type Approximate`

              Location precision. Only "approximate" is supported.

              - `const ApproximateApproximate Approximate = "approximate"`

            - `City string`

              City name.

            - `Country string`

              Two-letter ISO 3166-1 country code, uppercase.

            - `Region string`

              Region or state name.

            - `Timezone string`

              IANA timezone identifier, e.g. "America/Los_Angeles".

      - `DefaultConfig BetaManagedAgentsAgentToolsetDefaultConfigParamsResp`

        Default configuration for all tools in a toolset.

        - `Enabled bool`

          Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

        - `PermissionPolicy BetaManagedAgentsAgentToolsetDefaultConfigParamsPermissionPolicyUnionResp`

          Permission policy for tool execution.

          - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

            Tool calls are automatically approved without user confirmation.

          - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

            Tool calls require user confirmation before execution.

    - `type BetaManagedAgentsMCPToolsetParamsResp struct{…}`

      Configuration for tools from an MCP server defined in `mcp_servers`.

      - `MCPServerName string`

        Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

      - `Type BetaManagedAgentsMCPToolsetParamsType`

        - `const BetaManagedAgentsMCPToolsetParamsTypeMCPToolset BetaManagedAgentsMCPToolsetParamsType = "mcp_toolset"`

      - `Configs []BetaManagedAgentsMCPToolConfigParamsResp`

        Per-tool configuration overrides.

        - `Name string`

          Name of the MCP tool to configure. 1-128 characters.

        - `Enabled bool`

          Whether this tool is enabled. Overrides the `default_config` setting.

        - `PermissionPolicy BetaManagedAgentsMCPToolConfigParamsPermissionPolicyUnionResp`

          Permission policy for tool execution.

          - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

            Tool calls are automatically approved without user confirmation.

          - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

            Tool calls require user confirmation before execution.

      - `DefaultConfig BetaManagedAgentsMCPToolsetDefaultConfigParamsResp`

        Default configuration for all tools from an MCP server.

        - `Enabled bool`

          Whether tools are enabled by default. Defaults to true if not specified.

        - `PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigParamsPermissionPolicyUnionResp`

          Permission policy for tool execution.

          - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

            Tool calls are automatically approved without user confirmation.

          - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

            Tool calls require user confirmation before execution.

    - `type BetaManagedAgentsCustomToolParamsResp struct{…}`

      A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

      - `Description string`

        Description of what the tool does, shown to the agent to help it decide when to use the tool.

      - `InputSchema BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `Type Object`

          - `const ObjectObject Object = "object"`

        - `Properties map[string, any]`

        - `Required []string`

      - `Name string`

        Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

      - `Type BetaManagedAgentsCustomToolParamsType`

        - `const BetaManagedAgentsCustomToolParamsTypeCustom BetaManagedAgentsCustomToolParamsType = "custom"`

  - `Betas param.Field[[]AnthropicBeta]`

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

### Returns

- `type BetaManagedAgentsAgent struct{…}`

  A Managed Agents `agent`.

  - `ID string`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Description string`

  - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

    - `Name string`

    - `Type BetaManagedAgentsMCPServerURLDefinitionType`

      - `const BetaManagedAgentsMCPServerURLDefinitionTypeURL BetaManagedAgentsMCPServerURLDefinitionType = "url"`

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

    - `Effort BetaManagedAgentsModelConfigEffortUnion`

      How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

      - `type BetaManagedAgentsEffortLow struct{…}`

        Low effort. Favors latency over reasoning depth.

        - `Type BetaManagedAgentsEffortLowType`

          - `const BetaManagedAgentsEffortLowTypeLow BetaManagedAgentsEffortLowType = "low"`

      - `type BetaManagedAgentsEffortMedium struct{…}`

        Medium effort. Balances latency and reasoning depth.

        - `Type BetaManagedAgentsEffortMediumType`

          - `const BetaManagedAgentsEffortMediumTypeMedium BetaManagedAgentsEffortMediumType = "medium"`

      - `type BetaManagedAgentsEffortHigh struct{…}`

        High effort. Favors reasoning depth.

        - `Type BetaManagedAgentsEffortHighType`

          - `const BetaManagedAgentsEffortHighTypeHigh BetaManagedAgentsEffortHighType = "high"`

      - `type BetaManagedAgentsEffortXhigh struct{…}`

        Extra-high effort. Not all models accept this level.

        - `Type BetaManagedAgentsEffortXhighType`

          - `const BetaManagedAgentsEffortXhighTypeXhigh BetaManagedAgentsEffortXhighType = "xhigh"`

      - `type BetaManagedAgentsEffortMax struct{…}`

        Maximum effort. Favors reasoning depth over latency.

        - `Type BetaManagedAgentsEffortMaxType`

          - `const BetaManagedAgentsEffortMaxTypeMax BetaManagedAgentsEffortMaxType = "max"`

    - `InferenceGeo string`

      Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

    - `Speed BetaManagedAgentsModelConfigSpeed`

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

          - `const BetaManagedAgentsAgentReferenceTypeAgent BetaManagedAgentsAgentReferenceType = "agent"`

        - `Version int64`

      - `type BetaManagedAgentsAdvisor struct{…}`

        Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

        - `Model string`

          The advisor model id.

        - `Type BetaManagedAgentsAdvisorType`

          - `const BetaManagedAgentsAdvisorTypeAdvisor BetaManagedAgentsAdvisorType = "advisor"`

    - `Type BetaManagedAgentsMultiagentType`

      - `const BetaManagedAgentsMultiagentTypeCoordinator BetaManagedAgentsMultiagentType = "coordinator"`

  - `Name string`

  - `Skills []BetaManagedAgentsAgentSkillUnion`

    - `type BetaManagedAgentsAnthropicSkill struct{…}`

      A resolved Anthropic-managed skill.

      - `SkillID string`

      - `Type BetaManagedAgentsAnthropicSkillType`

        - `const BetaManagedAgentsAnthropicSkillTypeAnthropic BetaManagedAgentsAnthropicSkillType = "anthropic"`

      - `Version string`

    - `type BetaManagedAgentsCustomSkill struct{…}`

      A resolved user-created custom skill.

      - `SkillID string`

      - `Type BetaManagedAgentsCustomSkillType`

        - `const BetaManagedAgentsCustomSkillTypeCustom BetaManagedAgentsCustomSkillType = "custom"`

      - `Version string`

  - `System string`

  - `Tools []BetaManagedAgentsAgentToolUnion`

    - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

      - `Configs []BetaManagedAgentsAgentToolConfigUnion`

        - `type BetaManagedAgentsBashToolConfig struct{…}`

          Configuration for the bash tool.

          - `Enabled bool`

          - `Name Bash`

            - `const BashBash Bash = "bash"`

          - `PermissionPolicy BetaManagedAgentsBashToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

              - `Type BetaManagedAgentsAlwaysAllowPolicyType`

                - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

              - `Type BetaManagedAgentsAlwaysAskPolicyType`

                - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

          - `Type Bash`

            - `const BashBash Bash = "bash"`

        - `type BetaManagedAgentsEditToolConfig struct{…}`

          Configuration for the edit tool.

          - `Enabled bool`

          - `Name Edit`

            - `const EditEdit Edit = "edit"`

          - `PermissionPolicy BetaManagedAgentsEditToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Edit`

            - `const EditEdit Edit = "edit"`

        - `type BetaManagedAgentsReadToolConfig struct{…}`

          Configuration for the read tool.

          - `Enabled bool`

          - `Name Read`

            - `const ReadRead Read = "read"`

          - `PermissionPolicy BetaManagedAgentsReadToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Read`

            - `const ReadRead Read = "read"`

        - `type BetaManagedAgentsWriteToolConfig struct{…}`

          Configuration for the write tool.

          - `Enabled bool`

          - `Name Write`

            - `const WriteWrite Write = "write"`

          - `PermissionPolicy BetaManagedAgentsWriteToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Write`

            - `const WriteWrite Write = "write"`

        - `type BetaManagedAgentsGlobToolConfig struct{…}`

          Configuration for the glob tool.

          - `Enabled bool`

          - `Name Glob`

            - `const GlobGlob Glob = "glob"`

          - `PermissionPolicy BetaManagedAgentsGlobToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Glob`

            - `const GlobGlob Glob = "glob"`

        - `type BetaManagedAgentsGrepToolConfig struct{…}`

          Configuration for the grep tool.

          - `Enabled bool`

          - `Name Grep`

            - `const GrepGrep Grep = "grep"`

          - `PermissionPolicy BetaManagedAgentsGrepToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Grep`

            - `const GrepGrep Grep = "grep"`

        - `type BetaManagedAgentsWebFetchToolConfig struct{…}`

          Configuration for the web_fetch tool.

          - `Enabled bool`

          - `Name WebFetch`

            - `const WebFetchWebFetch WebFetch = "web_fetch"`

          - `PermissionPolicy BetaManagedAgentsWebFetchToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type WebFetch`

            - `const WebFetchWebFetch WebFetch = "web_fetch"`

          - `AllowedDomains []string`

          - `BlockedDomains []string`

          - `MaxContentTokens int64`

        - `type BetaManagedAgentsWebSearchToolConfig struct{…}`

          Configuration for the web_search tool.

          - `Enabled bool`

          - `Name WebSearch`

            - `const WebSearchWebSearch WebSearch = "web_search"`

          - `PermissionPolicy BetaManagedAgentsWebSearchToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type WebSearch`

            - `const WebSearchWebSearch WebSearch = "web_search"`

          - `AllowedDomains []string`

          - `BlockedDomains []string`

          - `UserLocation BetaManagedAgentsUserLocation`

            Approximate user location for search result localization.

            - `Type Approximate`

              Location precision. Only "approximate" is supported.

              - `const ApproximateApproximate Approximate = "approximate"`

            - `City string`

              City name.

            - `Country string`

              Two-letter ISO 3166-1 country code, uppercase.

            - `Region string`

              Region or state name.

            - `Timezone string`

              IANA timezone identifier, e.g. "America/Los_Angeles".

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

        - `const BetaManagedAgentsAgentToolset20260401TypeAgentToolset20260401 BetaManagedAgentsAgentToolset20260401Type = "agent_toolset_20260401"`

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

        - `const BetaManagedAgentsMCPToolsetTypeMCPToolset BetaManagedAgentsMCPToolsetType = "mcp_toolset"`

    - `type BetaManagedAgentsCustomTool struct{…}`

      A custom tool as returned in API responses.

      - `Description string`

      - `InputSchema BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `Type Object`

          - `const ObjectObject Object = "object"`

        - `Properties map[string, any]`

        - `Required []string`

      - `Name string`

      - `Type BetaManagedAgentsCustomToolType`

        - `const BetaManagedAgentsCustomToolTypeCustom BetaManagedAgentsCustomToolType = "custom"`

  - `Type BetaManagedAgentsAgentType`

    - `const BetaManagedAgentsAgentTypeAgent BetaManagedAgentsAgentType = "agent"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `Version int64`

    The agent's current version. Starts at 1 and increments when the agent is modified.

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
	betaManagedAgentsAgent, err := client.Beta.Agents.New(context.TODO(), anthropic.BetaAgentNewParams{
		Model: anthropic.BetaManagedAgentsModelConfigParams{
			ID: anthropic.BetaManagedAgentsModelClaudeOpus5,
		},
		Name: "My First Agent",
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaManagedAgentsAgent.ID)
}
```

#### Response

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

## List Agents

`client.Beta.Agents.List(ctx, params) (*PageCursor[BetaManagedAgentsAgent], error)`

**get** `/v1/agents`

List Agents

### Parameters

- `params BetaAgentListParams`

  - `CreatedAtGte param.Field[Time]`

    Query param: Return agents created at or after this time (inclusive).

  - `CreatedAtLte param.Field[Time]`

    Query param: Return agents created at or before this time (inclusive).

  - `IncludeArchived param.Field[bool]`

    Query param: Include archived agents in results. Defaults to false.

  - `Limit param.Field[int64]`

    Query param: Maximum results per page. Default 20, maximum 100.

  - `Page param.Field[string]`

    Query param: Opaque pagination cursor from a previous response.

  - `Betas param.Field[[]AnthropicBeta]`

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

### Returns

- `type BetaManagedAgentsAgent struct{…}`

  A Managed Agents `agent`.

  - `ID string`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Description string`

  - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

    - `Name string`

    - `Type BetaManagedAgentsMCPServerURLDefinitionType`

      - `const BetaManagedAgentsMCPServerURLDefinitionTypeURL BetaManagedAgentsMCPServerURLDefinitionType = "url"`

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

    - `Effort BetaManagedAgentsModelConfigEffortUnion`

      How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

      - `type BetaManagedAgentsEffortLow struct{…}`

        Low effort. Favors latency over reasoning depth.

        - `Type BetaManagedAgentsEffortLowType`

          - `const BetaManagedAgentsEffortLowTypeLow BetaManagedAgentsEffortLowType = "low"`

      - `type BetaManagedAgentsEffortMedium struct{…}`

        Medium effort. Balances latency and reasoning depth.

        - `Type BetaManagedAgentsEffortMediumType`

          - `const BetaManagedAgentsEffortMediumTypeMedium BetaManagedAgentsEffortMediumType = "medium"`

      - `type BetaManagedAgentsEffortHigh struct{…}`

        High effort. Favors reasoning depth.

        - `Type BetaManagedAgentsEffortHighType`

          - `const BetaManagedAgentsEffortHighTypeHigh BetaManagedAgentsEffortHighType = "high"`

      - `type BetaManagedAgentsEffortXhigh struct{…}`

        Extra-high effort. Not all models accept this level.

        - `Type BetaManagedAgentsEffortXhighType`

          - `const BetaManagedAgentsEffortXhighTypeXhigh BetaManagedAgentsEffortXhighType = "xhigh"`

      - `type BetaManagedAgentsEffortMax struct{…}`

        Maximum effort. Favors reasoning depth over latency.

        - `Type BetaManagedAgentsEffortMaxType`

          - `const BetaManagedAgentsEffortMaxTypeMax BetaManagedAgentsEffortMaxType = "max"`

    - `InferenceGeo string`

      Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

    - `Speed BetaManagedAgentsModelConfigSpeed`

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

          - `const BetaManagedAgentsAgentReferenceTypeAgent BetaManagedAgentsAgentReferenceType = "agent"`

        - `Version int64`

      - `type BetaManagedAgentsAdvisor struct{…}`

        Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

        - `Model string`

          The advisor model id.

        - `Type BetaManagedAgentsAdvisorType`

          - `const BetaManagedAgentsAdvisorTypeAdvisor BetaManagedAgentsAdvisorType = "advisor"`

    - `Type BetaManagedAgentsMultiagentType`

      - `const BetaManagedAgentsMultiagentTypeCoordinator BetaManagedAgentsMultiagentType = "coordinator"`

  - `Name string`

  - `Skills []BetaManagedAgentsAgentSkillUnion`

    - `type BetaManagedAgentsAnthropicSkill struct{…}`

      A resolved Anthropic-managed skill.

      - `SkillID string`

      - `Type BetaManagedAgentsAnthropicSkillType`

        - `const BetaManagedAgentsAnthropicSkillTypeAnthropic BetaManagedAgentsAnthropicSkillType = "anthropic"`

      - `Version string`

    - `type BetaManagedAgentsCustomSkill struct{…}`

      A resolved user-created custom skill.

      - `SkillID string`

      - `Type BetaManagedAgentsCustomSkillType`

        - `const BetaManagedAgentsCustomSkillTypeCustom BetaManagedAgentsCustomSkillType = "custom"`

      - `Version string`

  - `System string`

  - `Tools []BetaManagedAgentsAgentToolUnion`

    - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

      - `Configs []BetaManagedAgentsAgentToolConfigUnion`

        - `type BetaManagedAgentsBashToolConfig struct{…}`

          Configuration for the bash tool.

          - `Enabled bool`

          - `Name Bash`

            - `const BashBash Bash = "bash"`

          - `PermissionPolicy BetaManagedAgentsBashToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

              - `Type BetaManagedAgentsAlwaysAllowPolicyType`

                - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

              - `Type BetaManagedAgentsAlwaysAskPolicyType`

                - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

          - `Type Bash`

            - `const BashBash Bash = "bash"`

        - `type BetaManagedAgentsEditToolConfig struct{…}`

          Configuration for the edit tool.

          - `Enabled bool`

          - `Name Edit`

            - `const EditEdit Edit = "edit"`

          - `PermissionPolicy BetaManagedAgentsEditToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Edit`

            - `const EditEdit Edit = "edit"`

        - `type BetaManagedAgentsReadToolConfig struct{…}`

          Configuration for the read tool.

          - `Enabled bool`

          - `Name Read`

            - `const ReadRead Read = "read"`

          - `PermissionPolicy BetaManagedAgentsReadToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Read`

            - `const ReadRead Read = "read"`

        - `type BetaManagedAgentsWriteToolConfig struct{…}`

          Configuration for the write tool.

          - `Enabled bool`

          - `Name Write`

            - `const WriteWrite Write = "write"`

          - `PermissionPolicy BetaManagedAgentsWriteToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Write`

            - `const WriteWrite Write = "write"`

        - `type BetaManagedAgentsGlobToolConfig struct{…}`

          Configuration for the glob tool.

          - `Enabled bool`

          - `Name Glob`

            - `const GlobGlob Glob = "glob"`

          - `PermissionPolicy BetaManagedAgentsGlobToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Glob`

            - `const GlobGlob Glob = "glob"`

        - `type BetaManagedAgentsGrepToolConfig struct{…}`

          Configuration for the grep tool.

          - `Enabled bool`

          - `Name Grep`

            - `const GrepGrep Grep = "grep"`

          - `PermissionPolicy BetaManagedAgentsGrepToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Grep`

            - `const GrepGrep Grep = "grep"`

        - `type BetaManagedAgentsWebFetchToolConfig struct{…}`

          Configuration for the web_fetch tool.

          - `Enabled bool`

          - `Name WebFetch`

            - `const WebFetchWebFetch WebFetch = "web_fetch"`

          - `PermissionPolicy BetaManagedAgentsWebFetchToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type WebFetch`

            - `const WebFetchWebFetch WebFetch = "web_fetch"`

          - `AllowedDomains []string`

          - `BlockedDomains []string`

          - `MaxContentTokens int64`

        - `type BetaManagedAgentsWebSearchToolConfig struct{…}`

          Configuration for the web_search tool.

          - `Enabled bool`

          - `Name WebSearch`

            - `const WebSearchWebSearch WebSearch = "web_search"`

          - `PermissionPolicy BetaManagedAgentsWebSearchToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type WebSearch`

            - `const WebSearchWebSearch WebSearch = "web_search"`

          - `AllowedDomains []string`

          - `BlockedDomains []string`

          - `UserLocation BetaManagedAgentsUserLocation`

            Approximate user location for search result localization.

            - `Type Approximate`

              Location precision. Only "approximate" is supported.

              - `const ApproximateApproximate Approximate = "approximate"`

            - `City string`

              City name.

            - `Country string`

              Two-letter ISO 3166-1 country code, uppercase.

            - `Region string`

              Region or state name.

            - `Timezone string`

              IANA timezone identifier, e.g. "America/Los_Angeles".

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

        - `const BetaManagedAgentsAgentToolset20260401TypeAgentToolset20260401 BetaManagedAgentsAgentToolset20260401Type = "agent_toolset_20260401"`

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

        - `const BetaManagedAgentsMCPToolsetTypeMCPToolset BetaManagedAgentsMCPToolsetType = "mcp_toolset"`

    - `type BetaManagedAgentsCustomTool struct{…}`

      A custom tool as returned in API responses.

      - `Description string`

      - `InputSchema BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `Type Object`

          - `const ObjectObject Object = "object"`

        - `Properties map[string, any]`

        - `Required []string`

      - `Name string`

      - `Type BetaManagedAgentsCustomToolType`

        - `const BetaManagedAgentsCustomToolTypeCustom BetaManagedAgentsCustomToolType = "custom"`

  - `Type BetaManagedAgentsAgentType`

    - `const BetaManagedAgentsAgentTypeAgent BetaManagedAgentsAgentType = "agent"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `Version int64`

    The agent's current version. Starts at 1 and increments when the agent is modified.

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
	page, err := client.Beta.Agents.List(context.TODO(), anthropic.BetaAgentListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
}
```

#### Response

```json
{
  "data": [
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
  ],
  "next_page": "next_page"
}
```

## Get Agent

`client.Beta.Agents.Get(ctx, agentID, params) (*BetaManagedAgentsAgent, error)`

**get** `/v1/agents/{agent_id}`

Get Agent

### Parameters

- `agentID string`

- `params BetaAgentGetParams`

  - `Version param.Field[int64]`

    Query param: Agent version. Omit for the most recent version. Must be at least 1 if specified.

  - `Betas param.Field[[]AnthropicBeta]`

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

### Returns

- `type BetaManagedAgentsAgent struct{…}`

  A Managed Agents `agent`.

  - `ID string`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Description string`

  - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

    - `Name string`

    - `Type BetaManagedAgentsMCPServerURLDefinitionType`

      - `const BetaManagedAgentsMCPServerURLDefinitionTypeURL BetaManagedAgentsMCPServerURLDefinitionType = "url"`

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

    - `Effort BetaManagedAgentsModelConfigEffortUnion`

      How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

      - `type BetaManagedAgentsEffortLow struct{…}`

        Low effort. Favors latency over reasoning depth.

        - `Type BetaManagedAgentsEffortLowType`

          - `const BetaManagedAgentsEffortLowTypeLow BetaManagedAgentsEffortLowType = "low"`

      - `type BetaManagedAgentsEffortMedium struct{…}`

        Medium effort. Balances latency and reasoning depth.

        - `Type BetaManagedAgentsEffortMediumType`

          - `const BetaManagedAgentsEffortMediumTypeMedium BetaManagedAgentsEffortMediumType = "medium"`

      - `type BetaManagedAgentsEffortHigh struct{…}`

        High effort. Favors reasoning depth.

        - `Type BetaManagedAgentsEffortHighType`

          - `const BetaManagedAgentsEffortHighTypeHigh BetaManagedAgentsEffortHighType = "high"`

      - `type BetaManagedAgentsEffortXhigh struct{…}`

        Extra-high effort. Not all models accept this level.

        - `Type BetaManagedAgentsEffortXhighType`

          - `const BetaManagedAgentsEffortXhighTypeXhigh BetaManagedAgentsEffortXhighType = "xhigh"`

      - `type BetaManagedAgentsEffortMax struct{…}`

        Maximum effort. Favors reasoning depth over latency.

        - `Type BetaManagedAgentsEffortMaxType`

          - `const BetaManagedAgentsEffortMaxTypeMax BetaManagedAgentsEffortMaxType = "max"`

    - `InferenceGeo string`

      Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

    - `Speed BetaManagedAgentsModelConfigSpeed`

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

          - `const BetaManagedAgentsAgentReferenceTypeAgent BetaManagedAgentsAgentReferenceType = "agent"`

        - `Version int64`

      - `type BetaManagedAgentsAdvisor struct{…}`

        Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

        - `Model string`

          The advisor model id.

        - `Type BetaManagedAgentsAdvisorType`

          - `const BetaManagedAgentsAdvisorTypeAdvisor BetaManagedAgentsAdvisorType = "advisor"`

    - `Type BetaManagedAgentsMultiagentType`

      - `const BetaManagedAgentsMultiagentTypeCoordinator BetaManagedAgentsMultiagentType = "coordinator"`

  - `Name string`

  - `Skills []BetaManagedAgentsAgentSkillUnion`

    - `type BetaManagedAgentsAnthropicSkill struct{…}`

      A resolved Anthropic-managed skill.

      - `SkillID string`

      - `Type BetaManagedAgentsAnthropicSkillType`

        - `const BetaManagedAgentsAnthropicSkillTypeAnthropic BetaManagedAgentsAnthropicSkillType = "anthropic"`

      - `Version string`

    - `type BetaManagedAgentsCustomSkill struct{…}`

      A resolved user-created custom skill.

      - `SkillID string`

      - `Type BetaManagedAgentsCustomSkillType`

        - `const BetaManagedAgentsCustomSkillTypeCustom BetaManagedAgentsCustomSkillType = "custom"`

      - `Version string`

  - `System string`

  - `Tools []BetaManagedAgentsAgentToolUnion`

    - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

      - `Configs []BetaManagedAgentsAgentToolConfigUnion`

        - `type BetaManagedAgentsBashToolConfig struct{…}`

          Configuration for the bash tool.

          - `Enabled bool`

          - `Name Bash`

            - `const BashBash Bash = "bash"`

          - `PermissionPolicy BetaManagedAgentsBashToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

              - `Type BetaManagedAgentsAlwaysAllowPolicyType`

                - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

              - `Type BetaManagedAgentsAlwaysAskPolicyType`

                - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

          - `Type Bash`

            - `const BashBash Bash = "bash"`

        - `type BetaManagedAgentsEditToolConfig struct{…}`

          Configuration for the edit tool.

          - `Enabled bool`

          - `Name Edit`

            - `const EditEdit Edit = "edit"`

          - `PermissionPolicy BetaManagedAgentsEditToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Edit`

            - `const EditEdit Edit = "edit"`

        - `type BetaManagedAgentsReadToolConfig struct{…}`

          Configuration for the read tool.

          - `Enabled bool`

          - `Name Read`

            - `const ReadRead Read = "read"`

          - `PermissionPolicy BetaManagedAgentsReadToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Read`

            - `const ReadRead Read = "read"`

        - `type BetaManagedAgentsWriteToolConfig struct{…}`

          Configuration for the write tool.

          - `Enabled bool`

          - `Name Write`

            - `const WriteWrite Write = "write"`

          - `PermissionPolicy BetaManagedAgentsWriteToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Write`

            - `const WriteWrite Write = "write"`

        - `type BetaManagedAgentsGlobToolConfig struct{…}`

          Configuration for the glob tool.

          - `Enabled bool`

          - `Name Glob`

            - `const GlobGlob Glob = "glob"`

          - `PermissionPolicy BetaManagedAgentsGlobToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Glob`

            - `const GlobGlob Glob = "glob"`

        - `type BetaManagedAgentsGrepToolConfig struct{…}`

          Configuration for the grep tool.

          - `Enabled bool`

          - `Name Grep`

            - `const GrepGrep Grep = "grep"`

          - `PermissionPolicy BetaManagedAgentsGrepToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Grep`

            - `const GrepGrep Grep = "grep"`

        - `type BetaManagedAgentsWebFetchToolConfig struct{…}`

          Configuration for the web_fetch tool.

          - `Enabled bool`

          - `Name WebFetch`

            - `const WebFetchWebFetch WebFetch = "web_fetch"`

          - `PermissionPolicy BetaManagedAgentsWebFetchToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type WebFetch`

            - `const WebFetchWebFetch WebFetch = "web_fetch"`

          - `AllowedDomains []string`

          - `BlockedDomains []string`

          - `MaxContentTokens int64`

        - `type BetaManagedAgentsWebSearchToolConfig struct{…}`

          Configuration for the web_search tool.

          - `Enabled bool`

          - `Name WebSearch`

            - `const WebSearchWebSearch WebSearch = "web_search"`

          - `PermissionPolicy BetaManagedAgentsWebSearchToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type WebSearch`

            - `const WebSearchWebSearch WebSearch = "web_search"`

          - `AllowedDomains []string`

          - `BlockedDomains []string`

          - `UserLocation BetaManagedAgentsUserLocation`

            Approximate user location for search result localization.

            - `Type Approximate`

              Location precision. Only "approximate" is supported.

              - `const ApproximateApproximate Approximate = "approximate"`

            - `City string`

              City name.

            - `Country string`

              Two-letter ISO 3166-1 country code, uppercase.

            - `Region string`

              Region or state name.

            - `Timezone string`

              IANA timezone identifier, e.g. "America/Los_Angeles".

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

        - `const BetaManagedAgentsAgentToolset20260401TypeAgentToolset20260401 BetaManagedAgentsAgentToolset20260401Type = "agent_toolset_20260401"`

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

        - `const BetaManagedAgentsMCPToolsetTypeMCPToolset BetaManagedAgentsMCPToolsetType = "mcp_toolset"`

    - `type BetaManagedAgentsCustomTool struct{…}`

      A custom tool as returned in API responses.

      - `Description string`

      - `InputSchema BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `Type Object`

          - `const ObjectObject Object = "object"`

        - `Properties map[string, any]`

        - `Required []string`

      - `Name string`

      - `Type BetaManagedAgentsCustomToolType`

        - `const BetaManagedAgentsCustomToolTypeCustom BetaManagedAgentsCustomToolType = "custom"`

  - `Type BetaManagedAgentsAgentType`

    - `const BetaManagedAgentsAgentTypeAgent BetaManagedAgentsAgentType = "agent"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `Version int64`

    The agent's current version. Starts at 1 and increments when the agent is modified.

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
	betaManagedAgentsAgent, err := client.Beta.Agents.Get(
		context.TODO(),
		"agent_011CZkYpogX7uDKUyvBTophP",
		anthropic.BetaAgentGetParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaManagedAgentsAgent.ID)
}
```

#### Response

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

## Update Agent

`client.Beta.Agents.Update(ctx, agentID, params) (*BetaManagedAgentsAgent, error)`

**post** `/v1/agents/{agent_id}`

Update Agent

### Parameters

- `agentID string`

- `params BetaAgentUpdateParams`

  - `Description param.Field[string]`

    Body param: Description. Omit to preserve; send empty string or null to clear.

  - `MCPServers param.Field[[]BetaManagedAgentsURLMCPServerParamsResp]`

    Body param: MCP servers. Full replacement. Omit to preserve; send empty array or `null` to clear. Names must be unique. Maximum 20. Every server must be referenced by an `mcp_toolset` in the agent's resulting `tools`; unreferenced servers are rejected. See the [MCP connector guide](https://platform.claude.com/docs/en/managed-agents/mcp-connector).

    - `Name string`

      Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

    - `Type BetaManagedAgentsURLMCPServerParamsType`

      - `const BetaManagedAgentsURLMCPServerParamsTypeURL BetaManagedAgentsURLMCPServerParamsType = "url"`

    - `URL string`

      Endpoint URL for the MCP server.

  - `Metadata param.Field[map[string, string]]`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

  - `Model param.Field[BetaManagedAgentsModelConfigParamsResp]`

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

      - `Effort BetaManagedAgentsModelConfigParamsEffortUnionResp`

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

            - `const BetaManagedAgentsEffortLowTypeLow BetaManagedAgentsEffortLowType = "low"`

        - `type BetaManagedAgentsEffortMedium struct{…}`

          Medium effort. Balances latency and reasoning depth.

          - `Type BetaManagedAgentsEffortMediumType`

            - `const BetaManagedAgentsEffortMediumTypeMedium BetaManagedAgentsEffortMediumType = "medium"`

        - `type BetaManagedAgentsEffortHigh struct{…}`

          High effort. Favors reasoning depth.

          - `Type BetaManagedAgentsEffortHighType`

            - `const BetaManagedAgentsEffortHighTypeHigh BetaManagedAgentsEffortHighType = "high"`

        - `type BetaManagedAgentsEffortXhigh struct{…}`

          Extra-high effort. Not all models accept this level.

          - `Type BetaManagedAgentsEffortXhighType`

            - `const BetaManagedAgentsEffortXhighTypeXhigh BetaManagedAgentsEffortXhighType = "xhigh"`

        - `type BetaManagedAgentsEffortMax struct{…}`

          Maximum effort. Favors reasoning depth over latency.

          - `Type BetaManagedAgentsEffortMaxType`

            - `const BetaManagedAgentsEffortMaxTypeMax BetaManagedAgentsEffortMaxType = "max"`

      - `InferenceGeo string`

        Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo. On update, `model` is whole-object replacement — omitting inference_geo clears it.

      - `Speed BetaManagedAgentsModelConfigParamsSpeed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `const BetaManagedAgentsModelConfigParamsSpeedStandard BetaManagedAgentsModelConfigParamsSpeed = "standard"`

        - `const BetaManagedAgentsModelConfigParamsSpeedFast BetaManagedAgentsModelConfigParamsSpeed = "fast"`

  - `Multiagent param.Field[BetaManagedAgentsMultiagentParamsResp]`

    Body param: A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.

  - `Name param.Field[string]`

    Body param: Human-readable name. Must be non-empty. Omit to preserve. Cannot be cleared.

  - `Skills param.Field[[]BetaManagedAgentsSkillParamsUnionResp]`

    Body param: Skills. Full replacement. Omit to preserve; send empty array or null to clear.

    - `type BetaManagedAgentsAnthropicSkillParamsResp struct{…}`

      An Anthropic-managed skill.

      - `SkillID string`

        Identifier of the Anthropic skill (e.g., "xlsx").

      - `Type BetaManagedAgentsAnthropicSkillParamsType`

        - `const BetaManagedAgentsAnthropicSkillParamsTypeAnthropic BetaManagedAgentsAnthropicSkillParamsType = "anthropic"`

      - `Version string`

        Version to pin. Defaults to latest if omitted.

    - `type BetaManagedAgentsCustomSkillParamsResp struct{…}`

      A user-created custom skill.

      - `SkillID string`

        Tagged ID of the custom skill (e.g., "skill_01XJ5...").

      - `Type BetaManagedAgentsCustomSkillParamsType`

        - `const BetaManagedAgentsCustomSkillParamsTypeCustom BetaManagedAgentsCustomSkillParamsType = "custom"`

      - `Version string`

        Version to pin. Defaults to latest if omitted.

  - `System param.Field[string]`

    Body param: System prompt. Omit to preserve; send empty string or null to clear.

  - `Tools param.Field[[]BetaAgentUpdateParamsToolUnion]`

    Body param: Tool configurations available to the agent. Full replacement. Omit to preserve; send empty array or null to clear. Maximum of 128 tools across all toolsets allowed.

    - `type BetaManagedAgentsAgentToolset20260401ParamsResp struct{…}`

      Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

      - `Type BetaManagedAgentsAgentToolset20260401ParamsType`

        - `const BetaManagedAgentsAgentToolset20260401ParamsTypeAgentToolset20260401 BetaManagedAgentsAgentToolset20260401ParamsType = "agent_toolset_20260401"`

      - `Configs []BetaManagedAgentsAgentToolConfigParamsUnionResp`

        Per-tool configuration overrides.

        - `type BetaManagedAgentsBashToolConfigParamsResp struct{…}`

          Configuration override for the bash tool.

          - `Name Bash`

            Must be "bash".

            - `const BashBash Bash = "bash"`

          - `Enabled bool`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy BetaManagedAgentsBashToolConfigParamsPermissionPolicyUnionResp`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

              - `Type BetaManagedAgentsAlwaysAllowPolicyType`

                - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

              - `Type BetaManagedAgentsAlwaysAskPolicyType`

                - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

          - `Type BetaManagedAgentsBashToolConfigParamsType`

            - `const BetaManagedAgentsBashToolConfigParamsTypeBash BetaManagedAgentsBashToolConfigParamsType = "bash"`

        - `type BetaManagedAgentsEditToolConfigParamsResp struct{…}`

          Configuration override for the edit tool.

          - `Name Edit`

            Must be "edit".

            - `const EditEdit Edit = "edit"`

          - `Enabled bool`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy BetaManagedAgentsEditToolConfigParamsPermissionPolicyUnionResp`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type BetaManagedAgentsEditToolConfigParamsType`

            - `const BetaManagedAgentsEditToolConfigParamsTypeEdit BetaManagedAgentsEditToolConfigParamsType = "edit"`

        - `type BetaManagedAgentsReadToolConfigParamsResp struct{…}`

          Configuration override for the read tool.

          - `Name Read`

            Must be "read".

            - `const ReadRead Read = "read"`

          - `Enabled bool`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy BetaManagedAgentsReadToolConfigParamsPermissionPolicyUnionResp`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type BetaManagedAgentsReadToolConfigParamsType`

            - `const BetaManagedAgentsReadToolConfigParamsTypeRead BetaManagedAgentsReadToolConfigParamsType = "read"`

        - `type BetaManagedAgentsWriteToolConfigParamsResp struct{…}`

          Configuration override for the write tool.

          - `Name Write`

            Must be "write".

            - `const WriteWrite Write = "write"`

          - `Enabled bool`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy BetaManagedAgentsWriteToolConfigParamsPermissionPolicyUnionResp`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type BetaManagedAgentsWriteToolConfigParamsType`

            - `const BetaManagedAgentsWriteToolConfigParamsTypeWrite BetaManagedAgentsWriteToolConfigParamsType = "write"`

        - `type BetaManagedAgentsGlobToolConfigParamsResp struct{…}`

          Configuration override for the glob tool.

          - `Name Glob`

            Must be "glob".

            - `const GlobGlob Glob = "glob"`

          - `Enabled bool`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy BetaManagedAgentsGlobToolConfigParamsPermissionPolicyUnionResp`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type BetaManagedAgentsGlobToolConfigParamsType`

            - `const BetaManagedAgentsGlobToolConfigParamsTypeGlob BetaManagedAgentsGlobToolConfigParamsType = "glob"`

        - `type BetaManagedAgentsGrepToolConfigParamsResp struct{…}`

          Configuration override for the grep tool.

          - `Name Grep`

            Must be "grep".

            - `const GrepGrep Grep = "grep"`

          - `Enabled bool`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy BetaManagedAgentsGrepToolConfigParamsPermissionPolicyUnionResp`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type BetaManagedAgentsGrepToolConfigParamsType`

            - `const BetaManagedAgentsGrepToolConfigParamsTypeGrep BetaManagedAgentsGrepToolConfigParamsType = "grep"`

        - `type BetaManagedAgentsWebFetchToolConfigParamsResp struct{…}`

          Configuration override for the web_fetch tool.

          - `Name WebFetch`

            Must be "web_fetch".

            - `const WebFetchWebFetch WebFetch = "web_fetch"`

          - `AllowedDomains []string`

            Only fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

          - `BlockedDomains []string`

            Never fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

          - `Enabled bool`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `MaxContentTokens int64`

            Maximum number of tokens of fetched text content to include in context per call. Does not apply to binary content such as PDFs.

          - `PermissionPolicy BetaManagedAgentsWebFetchToolConfigParamsPermissionPolicyUnionResp`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type BetaManagedAgentsWebFetchToolConfigParamsType`

            - `const BetaManagedAgentsWebFetchToolConfigParamsTypeWebFetch BetaManagedAgentsWebFetchToolConfigParamsType = "web_fetch"`

        - `type BetaManagedAgentsWebSearchToolConfigParamsResp struct{…}`

          Configuration override for the web_search tool.

          - `Name WebSearch`

            Must be "web_search".

            - `const WebSearchWebSearch WebSearch = "web_search"`

          - `AllowedDomains []string`

            Only return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

          - `BlockedDomains []string`

            Never return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

          - `Enabled bool`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy BetaManagedAgentsWebSearchToolConfigParamsPermissionPolicyUnionResp`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type BetaManagedAgentsWebSearchToolConfigParamsType`

            - `const BetaManagedAgentsWebSearchToolConfigParamsTypeWebSearch BetaManagedAgentsWebSearchToolConfigParamsType = "web_search"`

          - `UserLocation BetaManagedAgentsUserLocation`

            Approximate user location for search result localization.

            - `Type Approximate`

              Location precision. Only "approximate" is supported.

              - `const ApproximateApproximate Approximate = "approximate"`

            - `City string`

              City name.

            - `Country string`

              Two-letter ISO 3166-1 country code, uppercase.

            - `Region string`

              Region or state name.

            - `Timezone string`

              IANA timezone identifier, e.g. "America/Los_Angeles".

      - `DefaultConfig BetaManagedAgentsAgentToolsetDefaultConfigParamsResp`

        Default configuration for all tools in a toolset.

        - `Enabled bool`

          Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

        - `PermissionPolicy BetaManagedAgentsAgentToolsetDefaultConfigParamsPermissionPolicyUnionResp`

          Permission policy for tool execution.

          - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

            Tool calls are automatically approved without user confirmation.

          - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

            Tool calls require user confirmation before execution.

    - `type BetaManagedAgentsMCPToolsetParamsResp struct{…}`

      Configuration for tools from an MCP server defined in `mcp_servers`.

      - `MCPServerName string`

        Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

      - `Type BetaManagedAgentsMCPToolsetParamsType`

        - `const BetaManagedAgentsMCPToolsetParamsTypeMCPToolset BetaManagedAgentsMCPToolsetParamsType = "mcp_toolset"`

      - `Configs []BetaManagedAgentsMCPToolConfigParamsResp`

        Per-tool configuration overrides.

        - `Name string`

          Name of the MCP tool to configure. 1-128 characters.

        - `Enabled bool`

          Whether this tool is enabled. Overrides the `default_config` setting.

        - `PermissionPolicy BetaManagedAgentsMCPToolConfigParamsPermissionPolicyUnionResp`

          Permission policy for tool execution.

          - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

            Tool calls are automatically approved without user confirmation.

          - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

            Tool calls require user confirmation before execution.

      - `DefaultConfig BetaManagedAgentsMCPToolsetDefaultConfigParamsResp`

        Default configuration for all tools from an MCP server.

        - `Enabled bool`

          Whether tools are enabled by default. Defaults to true if not specified.

        - `PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigParamsPermissionPolicyUnionResp`

          Permission policy for tool execution.

          - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

            Tool calls are automatically approved without user confirmation.

          - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

            Tool calls require user confirmation before execution.

    - `type BetaManagedAgentsCustomToolParamsResp struct{…}`

      A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

      - `Description string`

        Description of what the tool does, shown to the agent to help it decide when to use the tool.

      - `InputSchema BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `Type Object`

          - `const ObjectObject Object = "object"`

        - `Properties map[string, any]`

        - `Required []string`

      - `Name string`

        Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

      - `Type BetaManagedAgentsCustomToolParamsType`

        - `const BetaManagedAgentsCustomToolParamsTypeCustom BetaManagedAgentsCustomToolParamsType = "custom"`

  - `Version param.Field[int64]`

    Body param: The agent's current version, used to prevent concurrent overwrites. Obtain this value from a create or retrieve response. Must be at least 1 if specified. When supplied, the request fails if it does not match the server's current version; omit to apply the update unconditionally.

  - `Betas param.Field[[]AnthropicBeta]`

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

### Returns

- `type BetaManagedAgentsAgent struct{…}`

  A Managed Agents `agent`.

  - `ID string`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Description string`

  - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

    - `Name string`

    - `Type BetaManagedAgentsMCPServerURLDefinitionType`

      - `const BetaManagedAgentsMCPServerURLDefinitionTypeURL BetaManagedAgentsMCPServerURLDefinitionType = "url"`

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

    - `Effort BetaManagedAgentsModelConfigEffortUnion`

      How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

      - `type BetaManagedAgentsEffortLow struct{…}`

        Low effort. Favors latency over reasoning depth.

        - `Type BetaManagedAgentsEffortLowType`

          - `const BetaManagedAgentsEffortLowTypeLow BetaManagedAgentsEffortLowType = "low"`

      - `type BetaManagedAgentsEffortMedium struct{…}`

        Medium effort. Balances latency and reasoning depth.

        - `Type BetaManagedAgentsEffortMediumType`

          - `const BetaManagedAgentsEffortMediumTypeMedium BetaManagedAgentsEffortMediumType = "medium"`

      - `type BetaManagedAgentsEffortHigh struct{…}`

        High effort. Favors reasoning depth.

        - `Type BetaManagedAgentsEffortHighType`

          - `const BetaManagedAgentsEffortHighTypeHigh BetaManagedAgentsEffortHighType = "high"`

      - `type BetaManagedAgentsEffortXhigh struct{…}`

        Extra-high effort. Not all models accept this level.

        - `Type BetaManagedAgentsEffortXhighType`

          - `const BetaManagedAgentsEffortXhighTypeXhigh BetaManagedAgentsEffortXhighType = "xhigh"`

      - `type BetaManagedAgentsEffortMax struct{…}`

        Maximum effort. Favors reasoning depth over latency.

        - `Type BetaManagedAgentsEffortMaxType`

          - `const BetaManagedAgentsEffortMaxTypeMax BetaManagedAgentsEffortMaxType = "max"`

    - `InferenceGeo string`

      Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

    - `Speed BetaManagedAgentsModelConfigSpeed`

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

          - `const BetaManagedAgentsAgentReferenceTypeAgent BetaManagedAgentsAgentReferenceType = "agent"`

        - `Version int64`

      - `type BetaManagedAgentsAdvisor struct{…}`

        Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

        - `Model string`

          The advisor model id.

        - `Type BetaManagedAgentsAdvisorType`

          - `const BetaManagedAgentsAdvisorTypeAdvisor BetaManagedAgentsAdvisorType = "advisor"`

    - `Type BetaManagedAgentsMultiagentType`

      - `const BetaManagedAgentsMultiagentTypeCoordinator BetaManagedAgentsMultiagentType = "coordinator"`

  - `Name string`

  - `Skills []BetaManagedAgentsAgentSkillUnion`

    - `type BetaManagedAgentsAnthropicSkill struct{…}`

      A resolved Anthropic-managed skill.

      - `SkillID string`

      - `Type BetaManagedAgentsAnthropicSkillType`

        - `const BetaManagedAgentsAnthropicSkillTypeAnthropic BetaManagedAgentsAnthropicSkillType = "anthropic"`

      - `Version string`

    - `type BetaManagedAgentsCustomSkill struct{…}`

      A resolved user-created custom skill.

      - `SkillID string`

      - `Type BetaManagedAgentsCustomSkillType`

        - `const BetaManagedAgentsCustomSkillTypeCustom BetaManagedAgentsCustomSkillType = "custom"`

      - `Version string`

  - `System string`

  - `Tools []BetaManagedAgentsAgentToolUnion`

    - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

      - `Configs []BetaManagedAgentsAgentToolConfigUnion`

        - `type BetaManagedAgentsBashToolConfig struct{…}`

          Configuration for the bash tool.

          - `Enabled bool`

          - `Name Bash`

            - `const BashBash Bash = "bash"`

          - `PermissionPolicy BetaManagedAgentsBashToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

              - `Type BetaManagedAgentsAlwaysAllowPolicyType`

                - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

              - `Type BetaManagedAgentsAlwaysAskPolicyType`

                - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

          - `Type Bash`

            - `const BashBash Bash = "bash"`

        - `type BetaManagedAgentsEditToolConfig struct{…}`

          Configuration for the edit tool.

          - `Enabled bool`

          - `Name Edit`

            - `const EditEdit Edit = "edit"`

          - `PermissionPolicy BetaManagedAgentsEditToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Edit`

            - `const EditEdit Edit = "edit"`

        - `type BetaManagedAgentsReadToolConfig struct{…}`

          Configuration for the read tool.

          - `Enabled bool`

          - `Name Read`

            - `const ReadRead Read = "read"`

          - `PermissionPolicy BetaManagedAgentsReadToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Read`

            - `const ReadRead Read = "read"`

        - `type BetaManagedAgentsWriteToolConfig struct{…}`

          Configuration for the write tool.

          - `Enabled bool`

          - `Name Write`

            - `const WriteWrite Write = "write"`

          - `PermissionPolicy BetaManagedAgentsWriteToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Write`

            - `const WriteWrite Write = "write"`

        - `type BetaManagedAgentsGlobToolConfig struct{…}`

          Configuration for the glob tool.

          - `Enabled bool`

          - `Name Glob`

            - `const GlobGlob Glob = "glob"`

          - `PermissionPolicy BetaManagedAgentsGlobToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Glob`

            - `const GlobGlob Glob = "glob"`

        - `type BetaManagedAgentsGrepToolConfig struct{…}`

          Configuration for the grep tool.

          - `Enabled bool`

          - `Name Grep`

            - `const GrepGrep Grep = "grep"`

          - `PermissionPolicy BetaManagedAgentsGrepToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Grep`

            - `const GrepGrep Grep = "grep"`

        - `type BetaManagedAgentsWebFetchToolConfig struct{…}`

          Configuration for the web_fetch tool.

          - `Enabled bool`

          - `Name WebFetch`

            - `const WebFetchWebFetch WebFetch = "web_fetch"`

          - `PermissionPolicy BetaManagedAgentsWebFetchToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type WebFetch`

            - `const WebFetchWebFetch WebFetch = "web_fetch"`

          - `AllowedDomains []string`

          - `BlockedDomains []string`

          - `MaxContentTokens int64`

        - `type BetaManagedAgentsWebSearchToolConfig struct{…}`

          Configuration for the web_search tool.

          - `Enabled bool`

          - `Name WebSearch`

            - `const WebSearchWebSearch WebSearch = "web_search"`

          - `PermissionPolicy BetaManagedAgentsWebSearchToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type WebSearch`

            - `const WebSearchWebSearch WebSearch = "web_search"`

          - `AllowedDomains []string`

          - `BlockedDomains []string`

          - `UserLocation BetaManagedAgentsUserLocation`

            Approximate user location for search result localization.

            - `Type Approximate`

              Location precision. Only "approximate" is supported.

              - `const ApproximateApproximate Approximate = "approximate"`

            - `City string`

              City name.

            - `Country string`

              Two-letter ISO 3166-1 country code, uppercase.

            - `Region string`

              Region or state name.

            - `Timezone string`

              IANA timezone identifier, e.g. "America/Los_Angeles".

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

        - `const BetaManagedAgentsAgentToolset20260401TypeAgentToolset20260401 BetaManagedAgentsAgentToolset20260401Type = "agent_toolset_20260401"`

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

        - `const BetaManagedAgentsMCPToolsetTypeMCPToolset BetaManagedAgentsMCPToolsetType = "mcp_toolset"`

    - `type BetaManagedAgentsCustomTool struct{…}`

      A custom tool as returned in API responses.

      - `Description string`

      - `InputSchema BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `Type Object`

          - `const ObjectObject Object = "object"`

        - `Properties map[string, any]`

        - `Required []string`

      - `Name string`

      - `Type BetaManagedAgentsCustomToolType`

        - `const BetaManagedAgentsCustomToolTypeCustom BetaManagedAgentsCustomToolType = "custom"`

  - `Type BetaManagedAgentsAgentType`

    - `const BetaManagedAgentsAgentTypeAgent BetaManagedAgentsAgentType = "agent"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `Version int64`

    The agent's current version. Starts at 1 and increments when the agent is modified.

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

#### Response

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

## Archive Agent

`client.Beta.Agents.Archive(ctx, agentID, body) (*BetaManagedAgentsAgent, error)`

**post** `/v1/agents/{agent_id}/archive`

Archive Agent

### Parameters

- `agentID string`

- `body BetaAgentArchiveParams`

  - `Betas param.Field[[]AnthropicBeta]`

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

### Returns

- `type BetaManagedAgentsAgent struct{…}`

  A Managed Agents `agent`.

  - `ID string`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Description string`

  - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

    - `Name string`

    - `Type BetaManagedAgentsMCPServerURLDefinitionType`

      - `const BetaManagedAgentsMCPServerURLDefinitionTypeURL BetaManagedAgentsMCPServerURLDefinitionType = "url"`

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

    - `Effort BetaManagedAgentsModelConfigEffortUnion`

      How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

      - `type BetaManagedAgentsEffortLow struct{…}`

        Low effort. Favors latency over reasoning depth.

        - `Type BetaManagedAgentsEffortLowType`

          - `const BetaManagedAgentsEffortLowTypeLow BetaManagedAgentsEffortLowType = "low"`

      - `type BetaManagedAgentsEffortMedium struct{…}`

        Medium effort. Balances latency and reasoning depth.

        - `Type BetaManagedAgentsEffortMediumType`

          - `const BetaManagedAgentsEffortMediumTypeMedium BetaManagedAgentsEffortMediumType = "medium"`

      - `type BetaManagedAgentsEffortHigh struct{…}`

        High effort. Favors reasoning depth.

        - `Type BetaManagedAgentsEffortHighType`

          - `const BetaManagedAgentsEffortHighTypeHigh BetaManagedAgentsEffortHighType = "high"`

      - `type BetaManagedAgentsEffortXhigh struct{…}`

        Extra-high effort. Not all models accept this level.

        - `Type BetaManagedAgentsEffortXhighType`

          - `const BetaManagedAgentsEffortXhighTypeXhigh BetaManagedAgentsEffortXhighType = "xhigh"`

      - `type BetaManagedAgentsEffortMax struct{…}`

        Maximum effort. Favors reasoning depth over latency.

        - `Type BetaManagedAgentsEffortMaxType`

          - `const BetaManagedAgentsEffortMaxTypeMax BetaManagedAgentsEffortMaxType = "max"`

    - `InferenceGeo string`

      Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

    - `Speed BetaManagedAgentsModelConfigSpeed`

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

          - `const BetaManagedAgentsAgentReferenceTypeAgent BetaManagedAgentsAgentReferenceType = "agent"`

        - `Version int64`

      - `type BetaManagedAgentsAdvisor struct{…}`

        Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

        - `Model string`

          The advisor model id.

        - `Type BetaManagedAgentsAdvisorType`

          - `const BetaManagedAgentsAdvisorTypeAdvisor BetaManagedAgentsAdvisorType = "advisor"`

    - `Type BetaManagedAgentsMultiagentType`

      - `const BetaManagedAgentsMultiagentTypeCoordinator BetaManagedAgentsMultiagentType = "coordinator"`

  - `Name string`

  - `Skills []BetaManagedAgentsAgentSkillUnion`

    - `type BetaManagedAgentsAnthropicSkill struct{…}`

      A resolved Anthropic-managed skill.

      - `SkillID string`

      - `Type BetaManagedAgentsAnthropicSkillType`

        - `const BetaManagedAgentsAnthropicSkillTypeAnthropic BetaManagedAgentsAnthropicSkillType = "anthropic"`

      - `Version string`

    - `type BetaManagedAgentsCustomSkill struct{…}`

      A resolved user-created custom skill.

      - `SkillID string`

      - `Type BetaManagedAgentsCustomSkillType`

        - `const BetaManagedAgentsCustomSkillTypeCustom BetaManagedAgentsCustomSkillType = "custom"`

      - `Version string`

  - `System string`

  - `Tools []BetaManagedAgentsAgentToolUnion`

    - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

      - `Configs []BetaManagedAgentsAgentToolConfigUnion`

        - `type BetaManagedAgentsBashToolConfig struct{…}`

          Configuration for the bash tool.

          - `Enabled bool`

          - `Name Bash`

            - `const BashBash Bash = "bash"`

          - `PermissionPolicy BetaManagedAgentsBashToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

              - `Type BetaManagedAgentsAlwaysAllowPolicyType`

                - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

              - `Type BetaManagedAgentsAlwaysAskPolicyType`

                - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

          - `Type Bash`

            - `const BashBash Bash = "bash"`

        - `type BetaManagedAgentsEditToolConfig struct{…}`

          Configuration for the edit tool.

          - `Enabled bool`

          - `Name Edit`

            - `const EditEdit Edit = "edit"`

          - `PermissionPolicy BetaManagedAgentsEditToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Edit`

            - `const EditEdit Edit = "edit"`

        - `type BetaManagedAgentsReadToolConfig struct{…}`

          Configuration for the read tool.

          - `Enabled bool`

          - `Name Read`

            - `const ReadRead Read = "read"`

          - `PermissionPolicy BetaManagedAgentsReadToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Read`

            - `const ReadRead Read = "read"`

        - `type BetaManagedAgentsWriteToolConfig struct{…}`

          Configuration for the write tool.

          - `Enabled bool`

          - `Name Write`

            - `const WriteWrite Write = "write"`

          - `PermissionPolicy BetaManagedAgentsWriteToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Write`

            - `const WriteWrite Write = "write"`

        - `type BetaManagedAgentsGlobToolConfig struct{…}`

          Configuration for the glob tool.

          - `Enabled bool`

          - `Name Glob`

            - `const GlobGlob Glob = "glob"`

          - `PermissionPolicy BetaManagedAgentsGlobToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Glob`

            - `const GlobGlob Glob = "glob"`

        - `type BetaManagedAgentsGrepToolConfig struct{…}`

          Configuration for the grep tool.

          - `Enabled bool`

          - `Name Grep`

            - `const GrepGrep Grep = "grep"`

          - `PermissionPolicy BetaManagedAgentsGrepToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Grep`

            - `const GrepGrep Grep = "grep"`

        - `type BetaManagedAgentsWebFetchToolConfig struct{…}`

          Configuration for the web_fetch tool.

          - `Enabled bool`

          - `Name WebFetch`

            - `const WebFetchWebFetch WebFetch = "web_fetch"`

          - `PermissionPolicy BetaManagedAgentsWebFetchToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type WebFetch`

            - `const WebFetchWebFetch WebFetch = "web_fetch"`

          - `AllowedDomains []string`

          - `BlockedDomains []string`

          - `MaxContentTokens int64`

        - `type BetaManagedAgentsWebSearchToolConfig struct{…}`

          Configuration for the web_search tool.

          - `Enabled bool`

          - `Name WebSearch`

            - `const WebSearchWebSearch WebSearch = "web_search"`

          - `PermissionPolicy BetaManagedAgentsWebSearchToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type WebSearch`

            - `const WebSearchWebSearch WebSearch = "web_search"`

          - `AllowedDomains []string`

          - `BlockedDomains []string`

          - `UserLocation BetaManagedAgentsUserLocation`

            Approximate user location for search result localization.

            - `Type Approximate`

              Location precision. Only "approximate" is supported.

              - `const ApproximateApproximate Approximate = "approximate"`

            - `City string`

              City name.

            - `Country string`

              Two-letter ISO 3166-1 country code, uppercase.

            - `Region string`

              Region or state name.

            - `Timezone string`

              IANA timezone identifier, e.g. "America/Los_Angeles".

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

        - `const BetaManagedAgentsAgentToolset20260401TypeAgentToolset20260401 BetaManagedAgentsAgentToolset20260401Type = "agent_toolset_20260401"`

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

        - `const BetaManagedAgentsMCPToolsetTypeMCPToolset BetaManagedAgentsMCPToolsetType = "mcp_toolset"`

    - `type BetaManagedAgentsCustomTool struct{…}`

      A custom tool as returned in API responses.

      - `Description string`

      - `InputSchema BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `Type Object`

          - `const ObjectObject Object = "object"`

        - `Properties map[string, any]`

        - `Required []string`

      - `Name string`

      - `Type BetaManagedAgentsCustomToolType`

        - `const BetaManagedAgentsCustomToolTypeCustom BetaManagedAgentsCustomToolType = "custom"`

  - `Type BetaManagedAgentsAgentType`

    - `const BetaManagedAgentsAgentTypeAgent BetaManagedAgentsAgentType = "agent"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `Version int64`

    The agent's current version. Starts at 1 and increments when the agent is modified.

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
	betaManagedAgentsAgent, err := client.Beta.Agents.Archive(
		context.TODO(),
		"agent_011CZkYpogX7uDKUyvBTophP",
		anthropic.BetaAgentArchiveParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaManagedAgentsAgent.ID)
}
```

#### Response

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

## Domain Types

### Beta Managed Agents Advisor

- `type BetaManagedAgentsAdvisor struct{…}`

  Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

  - `Model string`

    The advisor model id.

  - `Type BetaManagedAgentsAdvisorType`

    - `const BetaManagedAgentsAdvisorTypeAdvisor BetaManagedAgentsAdvisorType = "advisor"`

### Beta Managed Agents Agent

- `type BetaManagedAgentsAgent struct{…}`

  A Managed Agents `agent`.

  - `ID string`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Description string`

  - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

    - `Name string`

    - `Type BetaManagedAgentsMCPServerURLDefinitionType`

      - `const BetaManagedAgentsMCPServerURLDefinitionTypeURL BetaManagedAgentsMCPServerURLDefinitionType = "url"`

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

    - `Effort BetaManagedAgentsModelConfigEffortUnion`

      How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

      - `type BetaManagedAgentsEffortLow struct{…}`

        Low effort. Favors latency over reasoning depth.

        - `Type BetaManagedAgentsEffortLowType`

          - `const BetaManagedAgentsEffortLowTypeLow BetaManagedAgentsEffortLowType = "low"`

      - `type BetaManagedAgentsEffortMedium struct{…}`

        Medium effort. Balances latency and reasoning depth.

        - `Type BetaManagedAgentsEffortMediumType`

          - `const BetaManagedAgentsEffortMediumTypeMedium BetaManagedAgentsEffortMediumType = "medium"`

      - `type BetaManagedAgentsEffortHigh struct{…}`

        High effort. Favors reasoning depth.

        - `Type BetaManagedAgentsEffortHighType`

          - `const BetaManagedAgentsEffortHighTypeHigh BetaManagedAgentsEffortHighType = "high"`

      - `type BetaManagedAgentsEffortXhigh struct{…}`

        Extra-high effort. Not all models accept this level.

        - `Type BetaManagedAgentsEffortXhighType`

          - `const BetaManagedAgentsEffortXhighTypeXhigh BetaManagedAgentsEffortXhighType = "xhigh"`

      - `type BetaManagedAgentsEffortMax struct{…}`

        Maximum effort. Favors reasoning depth over latency.

        - `Type BetaManagedAgentsEffortMaxType`

          - `const BetaManagedAgentsEffortMaxTypeMax BetaManagedAgentsEffortMaxType = "max"`

    - `InferenceGeo string`

      Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

    - `Speed BetaManagedAgentsModelConfigSpeed`

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

          - `const BetaManagedAgentsAgentReferenceTypeAgent BetaManagedAgentsAgentReferenceType = "agent"`

        - `Version int64`

      - `type BetaManagedAgentsAdvisor struct{…}`

        Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

        - `Model string`

          The advisor model id.

        - `Type BetaManagedAgentsAdvisorType`

          - `const BetaManagedAgentsAdvisorTypeAdvisor BetaManagedAgentsAdvisorType = "advisor"`

    - `Type BetaManagedAgentsMultiagentType`

      - `const BetaManagedAgentsMultiagentTypeCoordinator BetaManagedAgentsMultiagentType = "coordinator"`

  - `Name string`

  - `Skills []BetaManagedAgentsAgentSkillUnion`

    - `type BetaManagedAgentsAnthropicSkill struct{…}`

      A resolved Anthropic-managed skill.

      - `SkillID string`

      - `Type BetaManagedAgentsAnthropicSkillType`

        - `const BetaManagedAgentsAnthropicSkillTypeAnthropic BetaManagedAgentsAnthropicSkillType = "anthropic"`

      - `Version string`

    - `type BetaManagedAgentsCustomSkill struct{…}`

      A resolved user-created custom skill.

      - `SkillID string`

      - `Type BetaManagedAgentsCustomSkillType`

        - `const BetaManagedAgentsCustomSkillTypeCustom BetaManagedAgentsCustomSkillType = "custom"`

      - `Version string`

  - `System string`

  - `Tools []BetaManagedAgentsAgentToolUnion`

    - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

      - `Configs []BetaManagedAgentsAgentToolConfigUnion`

        - `type BetaManagedAgentsBashToolConfig struct{…}`

          Configuration for the bash tool.

          - `Enabled bool`

          - `Name Bash`

            - `const BashBash Bash = "bash"`

          - `PermissionPolicy BetaManagedAgentsBashToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

              - `Type BetaManagedAgentsAlwaysAllowPolicyType`

                - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

              - `Type BetaManagedAgentsAlwaysAskPolicyType`

                - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

          - `Type Bash`

            - `const BashBash Bash = "bash"`

        - `type BetaManagedAgentsEditToolConfig struct{…}`

          Configuration for the edit tool.

          - `Enabled bool`

          - `Name Edit`

            - `const EditEdit Edit = "edit"`

          - `PermissionPolicy BetaManagedAgentsEditToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Edit`

            - `const EditEdit Edit = "edit"`

        - `type BetaManagedAgentsReadToolConfig struct{…}`

          Configuration for the read tool.

          - `Enabled bool`

          - `Name Read`

            - `const ReadRead Read = "read"`

          - `PermissionPolicy BetaManagedAgentsReadToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Read`

            - `const ReadRead Read = "read"`

        - `type BetaManagedAgentsWriteToolConfig struct{…}`

          Configuration for the write tool.

          - `Enabled bool`

          - `Name Write`

            - `const WriteWrite Write = "write"`

          - `PermissionPolicy BetaManagedAgentsWriteToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Write`

            - `const WriteWrite Write = "write"`

        - `type BetaManagedAgentsGlobToolConfig struct{…}`

          Configuration for the glob tool.

          - `Enabled bool`

          - `Name Glob`

            - `const GlobGlob Glob = "glob"`

          - `PermissionPolicy BetaManagedAgentsGlobToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Glob`

            - `const GlobGlob Glob = "glob"`

        - `type BetaManagedAgentsGrepToolConfig struct{…}`

          Configuration for the grep tool.

          - `Enabled bool`

          - `Name Grep`

            - `const GrepGrep Grep = "grep"`

          - `PermissionPolicy BetaManagedAgentsGrepToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Grep`

            - `const GrepGrep Grep = "grep"`

        - `type BetaManagedAgentsWebFetchToolConfig struct{…}`

          Configuration for the web_fetch tool.

          - `Enabled bool`

          - `Name WebFetch`

            - `const WebFetchWebFetch WebFetch = "web_fetch"`

          - `PermissionPolicy BetaManagedAgentsWebFetchToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type WebFetch`

            - `const WebFetchWebFetch WebFetch = "web_fetch"`

          - `AllowedDomains []string`

          - `BlockedDomains []string`

          - `MaxContentTokens int64`

        - `type BetaManagedAgentsWebSearchToolConfig struct{…}`

          Configuration for the web_search tool.

          - `Enabled bool`

          - `Name WebSearch`

            - `const WebSearchWebSearch WebSearch = "web_search"`

          - `PermissionPolicy BetaManagedAgentsWebSearchToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type WebSearch`

            - `const WebSearchWebSearch WebSearch = "web_search"`

          - `AllowedDomains []string`

          - `BlockedDomains []string`

          - `UserLocation BetaManagedAgentsUserLocation`

            Approximate user location for search result localization.

            - `Type Approximate`

              Location precision. Only "approximate" is supported.

              - `const ApproximateApproximate Approximate = "approximate"`

            - `City string`

              City name.

            - `Country string`

              Two-letter ISO 3166-1 country code, uppercase.

            - `Region string`

              Region or state name.

            - `Timezone string`

              IANA timezone identifier, e.g. "America/Los_Angeles".

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

        - `const BetaManagedAgentsAgentToolset20260401TypeAgentToolset20260401 BetaManagedAgentsAgentToolset20260401Type = "agent_toolset_20260401"`

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

        - `const BetaManagedAgentsMCPToolsetTypeMCPToolset BetaManagedAgentsMCPToolsetType = "mcp_toolset"`

    - `type BetaManagedAgentsCustomTool struct{…}`

      A custom tool as returned in API responses.

      - `Description string`

      - `InputSchema BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `Type Object`

          - `const ObjectObject Object = "object"`

        - `Properties map[string, any]`

        - `Required []string`

      - `Name string`

      - `Type BetaManagedAgentsCustomToolType`

        - `const BetaManagedAgentsCustomToolTypeCustom BetaManagedAgentsCustomToolType = "custom"`

  - `Type BetaManagedAgentsAgentType`

    - `const BetaManagedAgentsAgentTypeAgent BetaManagedAgentsAgentType = "agent"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `Version int64`

    The agent's current version. Starts at 1 and increments when the agent is modified.

### Beta Managed Agents Agent Reference

- `type BetaManagedAgentsAgentReference struct{…}`

  A resolved agent reference with a concrete version.

  - `ID string`

  - `Type BetaManagedAgentsAgentReferenceType`

    - `const BetaManagedAgentsAgentReferenceTypeAgent BetaManagedAgentsAgentReferenceType = "agent"`

  - `Version int64`

### Beta Managed Agents Agent Tool Config

- `type BetaManagedAgentsAgentToolConfigUnion interface{…}`

  Configuration for a specific agent tool.

  - `type BetaManagedAgentsBashToolConfig struct{…}`

    Configuration for the bash tool.

    - `Enabled bool`

    - `Name Bash`

      - `const BashBash Bash = "bash"`

    - `PermissionPolicy BetaManagedAgentsBashToolConfigPermissionPolicyUnion`

      Permission policy for tool execution.

      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

        Tool calls are automatically approved without user confirmation.

        - `Type BetaManagedAgentsAlwaysAllowPolicyType`

          - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

        Tool calls require user confirmation before execution.

        - `Type BetaManagedAgentsAlwaysAskPolicyType`

          - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

    - `Type Bash`

      - `const BashBash Bash = "bash"`

  - `type BetaManagedAgentsEditToolConfig struct{…}`

    Configuration for the edit tool.

    - `Enabled bool`

    - `Name Edit`

      - `const EditEdit Edit = "edit"`

    - `PermissionPolicy BetaManagedAgentsEditToolConfigPermissionPolicyUnion`

      Permission policy for tool execution.

      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

        Tool calls are automatically approved without user confirmation.

      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

        Tool calls require user confirmation before execution.

    - `Type Edit`

      - `const EditEdit Edit = "edit"`

  - `type BetaManagedAgentsReadToolConfig struct{…}`

    Configuration for the read tool.

    - `Enabled bool`

    - `Name Read`

      - `const ReadRead Read = "read"`

    - `PermissionPolicy BetaManagedAgentsReadToolConfigPermissionPolicyUnion`

      Permission policy for tool execution.

      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

        Tool calls are automatically approved without user confirmation.

      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

        Tool calls require user confirmation before execution.

    - `Type Read`

      - `const ReadRead Read = "read"`

  - `type BetaManagedAgentsWriteToolConfig struct{…}`

    Configuration for the write tool.

    - `Enabled bool`

    - `Name Write`

      - `const WriteWrite Write = "write"`

    - `PermissionPolicy BetaManagedAgentsWriteToolConfigPermissionPolicyUnion`

      Permission policy for tool execution.

      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

        Tool calls are automatically approved without user confirmation.

      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

        Tool calls require user confirmation before execution.

    - `Type Write`

      - `const WriteWrite Write = "write"`

  - `type BetaManagedAgentsGlobToolConfig struct{…}`

    Configuration for the glob tool.

    - `Enabled bool`

    - `Name Glob`

      - `const GlobGlob Glob = "glob"`

    - `PermissionPolicy BetaManagedAgentsGlobToolConfigPermissionPolicyUnion`

      Permission policy for tool execution.

      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

        Tool calls are automatically approved without user confirmation.

      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

        Tool calls require user confirmation before execution.

    - `Type Glob`

      - `const GlobGlob Glob = "glob"`

  - `type BetaManagedAgentsGrepToolConfig struct{…}`

    Configuration for the grep tool.

    - `Enabled bool`

    - `Name Grep`

      - `const GrepGrep Grep = "grep"`

    - `PermissionPolicy BetaManagedAgentsGrepToolConfigPermissionPolicyUnion`

      Permission policy for tool execution.

      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

        Tool calls are automatically approved without user confirmation.

      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

        Tool calls require user confirmation before execution.

    - `Type Grep`

      - `const GrepGrep Grep = "grep"`

  - `type BetaManagedAgentsWebFetchToolConfig struct{…}`

    Configuration for the web_fetch tool.

    - `Enabled bool`

    - `Name WebFetch`

      - `const WebFetchWebFetch WebFetch = "web_fetch"`

    - `PermissionPolicy BetaManagedAgentsWebFetchToolConfigPermissionPolicyUnion`

      Permission policy for tool execution.

      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

        Tool calls are automatically approved without user confirmation.

      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

        Tool calls require user confirmation before execution.

    - `Type WebFetch`

      - `const WebFetchWebFetch WebFetch = "web_fetch"`

    - `AllowedDomains []string`

    - `BlockedDomains []string`

    - `MaxContentTokens int64`

  - `type BetaManagedAgentsWebSearchToolConfig struct{…}`

    Configuration for the web_search tool.

    - `Enabled bool`

    - `Name WebSearch`

      - `const WebSearchWebSearch WebSearch = "web_search"`

    - `PermissionPolicy BetaManagedAgentsWebSearchToolConfigPermissionPolicyUnion`

      Permission policy for tool execution.

      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

        Tool calls are automatically approved without user confirmation.

      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

        Tool calls require user confirmation before execution.

    - `Type WebSearch`

      - `const WebSearchWebSearch WebSearch = "web_search"`

    - `AllowedDomains []string`

    - `BlockedDomains []string`

    - `UserLocation BetaManagedAgentsUserLocation`

      Approximate user location for search result localization.

      - `Type Approximate`

        Location precision. Only "approximate" is supported.

        - `const ApproximateApproximate Approximate = "approximate"`

      - `City string`

        City name.

      - `Country string`

        Two-letter ISO 3166-1 country code, uppercase.

      - `Region string`

        Region or state name.

      - `Timezone string`

        IANA timezone identifier, e.g. "America/Los_Angeles".

### Beta Managed Agents Agent Tool Config Params

- `type BetaManagedAgentsAgentToolConfigParamsUnionResp interface{…}`

  Configuration override for a specific tool within a toolset.

  - `type BetaManagedAgentsBashToolConfigParamsResp struct{…}`

    Configuration override for the bash tool.

    - `Name Bash`

      Must be "bash".

      - `const BashBash Bash = "bash"`

    - `Enabled bool`

      Whether this tool is enabled and available to Claude. Overrides the default_config setting.

    - `PermissionPolicy BetaManagedAgentsBashToolConfigParamsPermissionPolicyUnionResp`

      Permission policy for tool execution.

      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

        Tool calls are automatically approved without user confirmation.

        - `Type BetaManagedAgentsAlwaysAllowPolicyType`

          - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

        Tool calls require user confirmation before execution.

        - `Type BetaManagedAgentsAlwaysAskPolicyType`

          - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

    - `Type BetaManagedAgentsBashToolConfigParamsType`

      - `const BetaManagedAgentsBashToolConfigParamsTypeBash BetaManagedAgentsBashToolConfigParamsType = "bash"`

  - `type BetaManagedAgentsEditToolConfigParamsResp struct{…}`

    Configuration override for the edit tool.

    - `Name Edit`

      Must be "edit".

      - `const EditEdit Edit = "edit"`

    - `Enabled bool`

      Whether this tool is enabled and available to Claude. Overrides the default_config setting.

    - `PermissionPolicy BetaManagedAgentsEditToolConfigParamsPermissionPolicyUnionResp`

      Permission policy for tool execution.

      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

        Tool calls are automatically approved without user confirmation.

      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

        Tool calls require user confirmation before execution.

    - `Type BetaManagedAgentsEditToolConfigParamsType`

      - `const BetaManagedAgentsEditToolConfigParamsTypeEdit BetaManagedAgentsEditToolConfigParamsType = "edit"`

  - `type BetaManagedAgentsReadToolConfigParamsResp struct{…}`

    Configuration override for the read tool.

    - `Name Read`

      Must be "read".

      - `const ReadRead Read = "read"`

    - `Enabled bool`

      Whether this tool is enabled and available to Claude. Overrides the default_config setting.

    - `PermissionPolicy BetaManagedAgentsReadToolConfigParamsPermissionPolicyUnionResp`

      Permission policy for tool execution.

      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

        Tool calls are automatically approved without user confirmation.

      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

        Tool calls require user confirmation before execution.

    - `Type BetaManagedAgentsReadToolConfigParamsType`

      - `const BetaManagedAgentsReadToolConfigParamsTypeRead BetaManagedAgentsReadToolConfigParamsType = "read"`

  - `type BetaManagedAgentsWriteToolConfigParamsResp struct{…}`

    Configuration override for the write tool.

    - `Name Write`

      Must be "write".

      - `const WriteWrite Write = "write"`

    - `Enabled bool`

      Whether this tool is enabled and available to Claude. Overrides the default_config setting.

    - `PermissionPolicy BetaManagedAgentsWriteToolConfigParamsPermissionPolicyUnionResp`

      Permission policy for tool execution.

      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

        Tool calls are automatically approved without user confirmation.

      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

        Tool calls require user confirmation before execution.

    - `Type BetaManagedAgentsWriteToolConfigParamsType`

      - `const BetaManagedAgentsWriteToolConfigParamsTypeWrite BetaManagedAgentsWriteToolConfigParamsType = "write"`

  - `type BetaManagedAgentsGlobToolConfigParamsResp struct{…}`

    Configuration override for the glob tool.

    - `Name Glob`

      Must be "glob".

      - `const GlobGlob Glob = "glob"`

    - `Enabled bool`

      Whether this tool is enabled and available to Claude. Overrides the default_config setting.

    - `PermissionPolicy BetaManagedAgentsGlobToolConfigParamsPermissionPolicyUnionResp`

      Permission policy for tool execution.

      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

        Tool calls are automatically approved without user confirmation.

      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

        Tool calls require user confirmation before execution.

    - `Type BetaManagedAgentsGlobToolConfigParamsType`

      - `const BetaManagedAgentsGlobToolConfigParamsTypeGlob BetaManagedAgentsGlobToolConfigParamsType = "glob"`

  - `type BetaManagedAgentsGrepToolConfigParamsResp struct{…}`

    Configuration override for the grep tool.

    - `Name Grep`

      Must be "grep".

      - `const GrepGrep Grep = "grep"`

    - `Enabled bool`

      Whether this tool is enabled and available to Claude. Overrides the default_config setting.

    - `PermissionPolicy BetaManagedAgentsGrepToolConfigParamsPermissionPolicyUnionResp`

      Permission policy for tool execution.

      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

        Tool calls are automatically approved without user confirmation.

      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

        Tool calls require user confirmation before execution.

    - `Type BetaManagedAgentsGrepToolConfigParamsType`

      - `const BetaManagedAgentsGrepToolConfigParamsTypeGrep BetaManagedAgentsGrepToolConfigParamsType = "grep"`

  - `type BetaManagedAgentsWebFetchToolConfigParamsResp struct{…}`

    Configuration override for the web_fetch tool.

    - `Name WebFetch`

      Must be "web_fetch".

      - `const WebFetchWebFetch WebFetch = "web_fetch"`

    - `AllowedDomains []string`

      Only fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

    - `BlockedDomains []string`

      Never fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

    - `Enabled bool`

      Whether this tool is enabled and available to Claude. Overrides the default_config setting.

    - `MaxContentTokens int64`

      Maximum number of tokens of fetched text content to include in context per call. Does not apply to binary content such as PDFs.

    - `PermissionPolicy BetaManagedAgentsWebFetchToolConfigParamsPermissionPolicyUnionResp`

      Permission policy for tool execution.

      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

        Tool calls are automatically approved without user confirmation.

      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

        Tool calls require user confirmation before execution.

    - `Type BetaManagedAgentsWebFetchToolConfigParamsType`

      - `const BetaManagedAgentsWebFetchToolConfigParamsTypeWebFetch BetaManagedAgentsWebFetchToolConfigParamsType = "web_fetch"`

  - `type BetaManagedAgentsWebSearchToolConfigParamsResp struct{…}`

    Configuration override for the web_search tool.

    - `Name WebSearch`

      Must be "web_search".

      - `const WebSearchWebSearch WebSearch = "web_search"`

    - `AllowedDomains []string`

      Only return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

    - `BlockedDomains []string`

      Never return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

    - `Enabled bool`

      Whether this tool is enabled and available to Claude. Overrides the default_config setting.

    - `PermissionPolicy BetaManagedAgentsWebSearchToolConfigParamsPermissionPolicyUnionResp`

      Permission policy for tool execution.

      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

        Tool calls are automatically approved without user confirmation.

      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

        Tool calls require user confirmation before execution.

    - `Type BetaManagedAgentsWebSearchToolConfigParamsType`

      - `const BetaManagedAgentsWebSearchToolConfigParamsTypeWebSearch BetaManagedAgentsWebSearchToolConfigParamsType = "web_search"`

    - `UserLocation BetaManagedAgentsUserLocation`

      Approximate user location for search result localization.

      - `Type Approximate`

        Location precision. Only "approximate" is supported.

        - `const ApproximateApproximate Approximate = "approximate"`

      - `City string`

        City name.

      - `Country string`

        Two-letter ISO 3166-1 country code, uppercase.

      - `Region string`

        Region or state name.

      - `Timezone string`

        IANA timezone identifier, e.g. "America/Los_Angeles".

### Beta Managed Agents Agent Toolset Default Config

- `type BetaManagedAgentsAgentToolsetDefaultConfig struct{…}`

  Resolved default configuration for agent tools.

  - `Enabled bool`

  - `PermissionPolicy BetaManagedAgentsAgentToolsetDefaultConfigPermissionPolicyUnion`

    Permission policy for tool execution.

    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

      Tool calls are automatically approved without user confirmation.

      - `Type BetaManagedAgentsAlwaysAllowPolicyType`

        - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

      Tool calls require user confirmation before execution.

      - `Type BetaManagedAgentsAlwaysAskPolicyType`

        - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

### Beta Managed Agents Agent Toolset Default Config Params

- `type BetaManagedAgentsAgentToolsetDefaultConfigParamsResp struct{…}`

  Default configuration for all tools in a toolset.

  - `Enabled bool`

    Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

  - `PermissionPolicy BetaManagedAgentsAgentToolsetDefaultConfigParamsPermissionPolicyUnionResp`

    Permission policy for tool execution.

    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

      Tool calls are automatically approved without user confirmation.

      - `Type BetaManagedAgentsAlwaysAllowPolicyType`

        - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

      Tool calls require user confirmation before execution.

      - `Type BetaManagedAgentsAlwaysAskPolicyType`

        - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

### Beta Managed Agents Agent Toolset20260401

- `type BetaManagedAgentsAgentToolset20260401 struct{…}`

  - `Configs []BetaManagedAgentsAgentToolConfigUnion`

    - `type BetaManagedAgentsBashToolConfig struct{…}`

      Configuration for the bash tool.

      - `Enabled bool`

      - `Name Bash`

        - `const BashBash Bash = "bash"`

      - `PermissionPolicy BetaManagedAgentsBashToolConfigPermissionPolicyUnion`

        Permission policy for tool execution.

        - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

          Tool calls are automatically approved without user confirmation.

          - `Type BetaManagedAgentsAlwaysAllowPolicyType`

            - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

        - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

          Tool calls require user confirmation before execution.

          - `Type BetaManagedAgentsAlwaysAskPolicyType`

            - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

      - `Type Bash`

        - `const BashBash Bash = "bash"`

    - `type BetaManagedAgentsEditToolConfig struct{…}`

      Configuration for the edit tool.

      - `Enabled bool`

      - `Name Edit`

        - `const EditEdit Edit = "edit"`

      - `PermissionPolicy BetaManagedAgentsEditToolConfigPermissionPolicyUnion`

        Permission policy for tool execution.

        - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

          Tool calls are automatically approved without user confirmation.

        - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

          Tool calls require user confirmation before execution.

      - `Type Edit`

        - `const EditEdit Edit = "edit"`

    - `type BetaManagedAgentsReadToolConfig struct{…}`

      Configuration for the read tool.

      - `Enabled bool`

      - `Name Read`

        - `const ReadRead Read = "read"`

      - `PermissionPolicy BetaManagedAgentsReadToolConfigPermissionPolicyUnion`

        Permission policy for tool execution.

        - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

          Tool calls are automatically approved without user confirmation.

        - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

          Tool calls require user confirmation before execution.

      - `Type Read`

        - `const ReadRead Read = "read"`

    - `type BetaManagedAgentsWriteToolConfig struct{…}`

      Configuration for the write tool.

      - `Enabled bool`

      - `Name Write`

        - `const WriteWrite Write = "write"`

      - `PermissionPolicy BetaManagedAgentsWriteToolConfigPermissionPolicyUnion`

        Permission policy for tool execution.

        - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

          Tool calls are automatically approved without user confirmation.

        - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

          Tool calls require user confirmation before execution.

      - `Type Write`

        - `const WriteWrite Write = "write"`

    - `type BetaManagedAgentsGlobToolConfig struct{…}`

      Configuration for the glob tool.

      - `Enabled bool`

      - `Name Glob`

        - `const GlobGlob Glob = "glob"`

      - `PermissionPolicy BetaManagedAgentsGlobToolConfigPermissionPolicyUnion`

        Permission policy for tool execution.

        - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

          Tool calls are automatically approved without user confirmation.

        - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

          Tool calls require user confirmation before execution.

      - `Type Glob`

        - `const GlobGlob Glob = "glob"`

    - `type BetaManagedAgentsGrepToolConfig struct{…}`

      Configuration for the grep tool.

      - `Enabled bool`

      - `Name Grep`

        - `const GrepGrep Grep = "grep"`

      - `PermissionPolicy BetaManagedAgentsGrepToolConfigPermissionPolicyUnion`

        Permission policy for tool execution.

        - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

          Tool calls are automatically approved without user confirmation.

        - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

          Tool calls require user confirmation before execution.

      - `Type Grep`

        - `const GrepGrep Grep = "grep"`

    - `type BetaManagedAgentsWebFetchToolConfig struct{…}`

      Configuration for the web_fetch tool.

      - `Enabled bool`

      - `Name WebFetch`

        - `const WebFetchWebFetch WebFetch = "web_fetch"`

      - `PermissionPolicy BetaManagedAgentsWebFetchToolConfigPermissionPolicyUnion`

        Permission policy for tool execution.

        - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

          Tool calls are automatically approved without user confirmation.

        - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

          Tool calls require user confirmation before execution.

      - `Type WebFetch`

        - `const WebFetchWebFetch WebFetch = "web_fetch"`

      - `AllowedDomains []string`

      - `BlockedDomains []string`

      - `MaxContentTokens int64`

    - `type BetaManagedAgentsWebSearchToolConfig struct{…}`

      Configuration for the web_search tool.

      - `Enabled bool`

      - `Name WebSearch`

        - `const WebSearchWebSearch WebSearch = "web_search"`

      - `PermissionPolicy BetaManagedAgentsWebSearchToolConfigPermissionPolicyUnion`

        Permission policy for tool execution.

        - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

          Tool calls are automatically approved without user confirmation.

        - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

          Tool calls require user confirmation before execution.

      - `Type WebSearch`

        - `const WebSearchWebSearch WebSearch = "web_search"`

      - `AllowedDomains []string`

      - `BlockedDomains []string`

      - `UserLocation BetaManagedAgentsUserLocation`

        Approximate user location for search result localization.

        - `Type Approximate`

          Location precision. Only "approximate" is supported.

          - `const ApproximateApproximate Approximate = "approximate"`

        - `City string`

          City name.

        - `Country string`

          Two-letter ISO 3166-1 country code, uppercase.

        - `Region string`

          Region or state name.

        - `Timezone string`

          IANA timezone identifier, e.g. "America/Los_Angeles".

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

    - `const BetaManagedAgentsAgentToolset20260401TypeAgentToolset20260401 BetaManagedAgentsAgentToolset20260401Type = "agent_toolset_20260401"`

### Beta Managed Agents Agent Toolset20260401 Bash Input

- `type BetaManagedAgentsAgentToolset20260401BashInput struct{…}`

  Input payload for the `bash` tool of the
  `agent_toolset_20260401` toolset. All fields are optional;
  a normal invocation supplies `command`, while `restart=true`
  (with no `command`) reboots the runner-side bash session.

  - `Command string`

    Shell command to execute. Omit only when `restart` is true.

  - `Restart bool`

    When true, restart the persistent bash session instead of
    running a command. Subsequent calls without `restart` will
    run against the fresh session.

  - `TimeoutMs int64`

    Per-call timeout in milliseconds. Defaults to the
    runner-wide tool timeout when omitted or zero.

### Beta Managed Agents Agent Toolset20260401 Edit Input

- `type BetaManagedAgentsAgentToolset20260401EditInput struct{…}`

  Input payload for the `edit` tool. Performs a string
  replacement in the named file; by default `old_string` must
  occur exactly once.

  - `FilePath string`

    Path of the file to edit.

  - `NewString string`

    Replacement text.

  - `OldString string`

    Substring to find and replace.

  - `ReplaceAll bool`

    When true, replace every occurrence of `old_string`
    instead of requiring a unique match.

### Beta Managed Agents Agent Toolset20260401 Glob Input

- `type BetaManagedAgentsAgentToolset20260401GlobInput struct{…}`

  Input payload for the `glob` tool. Returns paths matching a
  doublestar glob pattern, newest first.

  - `Pattern string`

    Doublestar glob pattern (e.g. `**/*.go`). Absolute patterns
    are only permitted when the runner is configured to allow
    them.

  - `Path string`

    Optional directory root to search under. Defaults to the
    runner's working directory.

### Beta Managed Agents Agent Toolset20260401 Grep Input

- `type BetaManagedAgentsAgentToolset20260401GrepInput struct{…}`

  Input payload for the `grep` tool. Searches file contents for
  a regular expression, returning matching lines.

  - `Pattern string`

    Regular expression to search for.

  - `Path string`

    Optional directory root to search under. Defaults to the
    runner's working directory.

### Beta Managed Agents Agent Toolset20260401 Params

- `type BetaManagedAgentsAgentToolset20260401ParamsResp struct{…}`

  Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

  - `Type BetaManagedAgentsAgentToolset20260401ParamsType`

    - `const BetaManagedAgentsAgentToolset20260401ParamsTypeAgentToolset20260401 BetaManagedAgentsAgentToolset20260401ParamsType = "agent_toolset_20260401"`

  - `Configs []BetaManagedAgentsAgentToolConfigParamsUnionResp`

    Per-tool configuration overrides.

    - `type BetaManagedAgentsBashToolConfigParamsResp struct{…}`

      Configuration override for the bash tool.

      - `Name Bash`

        Must be "bash".

        - `const BashBash Bash = "bash"`

      - `Enabled bool`

        Whether this tool is enabled and available to Claude. Overrides the default_config setting.

      - `PermissionPolicy BetaManagedAgentsBashToolConfigParamsPermissionPolicyUnionResp`

        Permission policy for tool execution.

        - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

          Tool calls are automatically approved without user confirmation.

          - `Type BetaManagedAgentsAlwaysAllowPolicyType`

            - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

        - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

          Tool calls require user confirmation before execution.

          - `Type BetaManagedAgentsAlwaysAskPolicyType`

            - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

      - `Type BetaManagedAgentsBashToolConfigParamsType`

        - `const BetaManagedAgentsBashToolConfigParamsTypeBash BetaManagedAgentsBashToolConfigParamsType = "bash"`

    - `type BetaManagedAgentsEditToolConfigParamsResp struct{…}`

      Configuration override for the edit tool.

      - `Name Edit`

        Must be "edit".

        - `const EditEdit Edit = "edit"`

      - `Enabled bool`

        Whether this tool is enabled and available to Claude. Overrides the default_config setting.

      - `PermissionPolicy BetaManagedAgentsEditToolConfigParamsPermissionPolicyUnionResp`

        Permission policy for tool execution.

        - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

          Tool calls are automatically approved without user confirmation.

        - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

          Tool calls require user confirmation before execution.

      - `Type BetaManagedAgentsEditToolConfigParamsType`

        - `const BetaManagedAgentsEditToolConfigParamsTypeEdit BetaManagedAgentsEditToolConfigParamsType = "edit"`

    - `type BetaManagedAgentsReadToolConfigParamsResp struct{…}`

      Configuration override for the read tool.

      - `Name Read`

        Must be "read".

        - `const ReadRead Read = "read"`

      - `Enabled bool`

        Whether this tool is enabled and available to Claude. Overrides the default_config setting.

      - `PermissionPolicy BetaManagedAgentsReadToolConfigParamsPermissionPolicyUnionResp`

        Permission policy for tool execution.

        - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

          Tool calls are automatically approved without user confirmation.

        - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

          Tool calls require user confirmation before execution.

      - `Type BetaManagedAgentsReadToolConfigParamsType`

        - `const BetaManagedAgentsReadToolConfigParamsTypeRead BetaManagedAgentsReadToolConfigParamsType = "read"`

    - `type BetaManagedAgentsWriteToolConfigParamsResp struct{…}`

      Configuration override for the write tool.

      - `Name Write`

        Must be "write".

        - `const WriteWrite Write = "write"`

      - `Enabled bool`

        Whether this tool is enabled and available to Claude. Overrides the default_config setting.

      - `PermissionPolicy BetaManagedAgentsWriteToolConfigParamsPermissionPolicyUnionResp`

        Permission policy for tool execution.

        - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

          Tool calls are automatically approved without user confirmation.

        - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

          Tool calls require user confirmation before execution.

      - `Type BetaManagedAgentsWriteToolConfigParamsType`

        - `const BetaManagedAgentsWriteToolConfigParamsTypeWrite BetaManagedAgentsWriteToolConfigParamsType = "write"`

    - `type BetaManagedAgentsGlobToolConfigParamsResp struct{…}`

      Configuration override for the glob tool.

      - `Name Glob`

        Must be "glob".

        - `const GlobGlob Glob = "glob"`

      - `Enabled bool`

        Whether this tool is enabled and available to Claude. Overrides the default_config setting.

      - `PermissionPolicy BetaManagedAgentsGlobToolConfigParamsPermissionPolicyUnionResp`

        Permission policy for tool execution.

        - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

          Tool calls are automatically approved without user confirmation.

        - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

          Tool calls require user confirmation before execution.

      - `Type BetaManagedAgentsGlobToolConfigParamsType`

        - `const BetaManagedAgentsGlobToolConfigParamsTypeGlob BetaManagedAgentsGlobToolConfigParamsType = "glob"`

    - `type BetaManagedAgentsGrepToolConfigParamsResp struct{…}`

      Configuration override for the grep tool.

      - `Name Grep`

        Must be "grep".

        - `const GrepGrep Grep = "grep"`

      - `Enabled bool`

        Whether this tool is enabled and available to Claude. Overrides the default_config setting.

      - `PermissionPolicy BetaManagedAgentsGrepToolConfigParamsPermissionPolicyUnionResp`

        Permission policy for tool execution.

        - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

          Tool calls are automatically approved without user confirmation.

        - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

          Tool calls require user confirmation before execution.

      - `Type BetaManagedAgentsGrepToolConfigParamsType`

        - `const BetaManagedAgentsGrepToolConfigParamsTypeGrep BetaManagedAgentsGrepToolConfigParamsType = "grep"`

    - `type BetaManagedAgentsWebFetchToolConfigParamsResp struct{…}`

      Configuration override for the web_fetch tool.

      - `Name WebFetch`

        Must be "web_fetch".

        - `const WebFetchWebFetch WebFetch = "web_fetch"`

      - `AllowedDomains []string`

        Only fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

      - `BlockedDomains []string`

        Never fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

      - `Enabled bool`

        Whether this tool is enabled and available to Claude. Overrides the default_config setting.

      - `MaxContentTokens int64`

        Maximum number of tokens of fetched text content to include in context per call. Does not apply to binary content such as PDFs.

      - `PermissionPolicy BetaManagedAgentsWebFetchToolConfigParamsPermissionPolicyUnionResp`

        Permission policy for tool execution.

        - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

          Tool calls are automatically approved without user confirmation.

        - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

          Tool calls require user confirmation before execution.

      - `Type BetaManagedAgentsWebFetchToolConfigParamsType`

        - `const BetaManagedAgentsWebFetchToolConfigParamsTypeWebFetch BetaManagedAgentsWebFetchToolConfigParamsType = "web_fetch"`

    - `type BetaManagedAgentsWebSearchToolConfigParamsResp struct{…}`

      Configuration override for the web_search tool.

      - `Name WebSearch`

        Must be "web_search".

        - `const WebSearchWebSearch WebSearch = "web_search"`

      - `AllowedDomains []string`

        Only return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

      - `BlockedDomains []string`

        Never return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

      - `Enabled bool`

        Whether this tool is enabled and available to Claude. Overrides the default_config setting.

      - `PermissionPolicy BetaManagedAgentsWebSearchToolConfigParamsPermissionPolicyUnionResp`

        Permission policy for tool execution.

        - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

          Tool calls are automatically approved without user confirmation.

        - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

          Tool calls require user confirmation before execution.

      - `Type BetaManagedAgentsWebSearchToolConfigParamsType`

        - `const BetaManagedAgentsWebSearchToolConfigParamsTypeWebSearch BetaManagedAgentsWebSearchToolConfigParamsType = "web_search"`

      - `UserLocation BetaManagedAgentsUserLocation`

        Approximate user location for search result localization.

        - `Type Approximate`

          Location precision. Only "approximate" is supported.

          - `const ApproximateApproximate Approximate = "approximate"`

        - `City string`

          City name.

        - `Country string`

          Two-letter ISO 3166-1 country code, uppercase.

        - `Region string`

          Region or state name.

        - `Timezone string`

          IANA timezone identifier, e.g. "America/Los_Angeles".

  - `DefaultConfig BetaManagedAgentsAgentToolsetDefaultConfigParamsResp`

    Default configuration for all tools in a toolset.

    - `Enabled bool`

      Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

    - `PermissionPolicy BetaManagedAgentsAgentToolsetDefaultConfigParamsPermissionPolicyUnionResp`

      Permission policy for tool execution.

      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

        Tool calls are automatically approved without user confirmation.

      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

        Tool calls require user confirmation before execution.

### Beta Managed Agents Agent Toolset20260401 Read Input

- `type BetaManagedAgentsAgentToolset20260401ReadInput struct{…}`

  Input payload for the `read` tool. Reads file contents
  relative to the runner's working directory (or absolute when
  the runner permits).

  - `FilePath string`

    Path of the file to read.

  - `ViewRange []int64`

    Optional `[start_line, end_line]` 1-indexed inclusive
    range. When omitted the entire file is returned.
    `end_line` of 0 or negative means "to end of file".

### Beta Managed Agents Agent Toolset20260401 Write Input

- `type BetaManagedAgentsAgentToolset20260401WriteInput struct{…}`

  Input payload for the `write` tool. Writes (overwriting) the
  entire file contents.

  - `Content string`

    Full file contents to write.

  - `FilePath string`

    Path of the file to write.

### Beta Managed Agents Always Allow Policy

- `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

  Tool calls are automatically approved without user confirmation.

  - `Type BetaManagedAgentsAlwaysAllowPolicyType`

    - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

### Beta Managed Agents Always Ask Policy

- `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

  Tool calls require user confirmation before execution.

  - `Type BetaManagedAgentsAlwaysAskPolicyType`

    - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

### Beta Managed Agents Anthropic Skill

- `type BetaManagedAgentsAnthropicSkill struct{…}`

  A resolved Anthropic-managed skill.

  - `SkillID string`

  - `Type BetaManagedAgentsAnthropicSkillType`

    - `const BetaManagedAgentsAnthropicSkillTypeAnthropic BetaManagedAgentsAnthropicSkillType = "anthropic"`

  - `Version string`

### Beta Managed Agents Anthropic Skill Params

- `type BetaManagedAgentsAnthropicSkillParamsResp struct{…}`

  An Anthropic-managed skill.

  - `SkillID string`

    Identifier of the Anthropic skill (e.g., "xlsx").

  - `Type BetaManagedAgentsAnthropicSkillParamsType`

    - `const BetaManagedAgentsAnthropicSkillParamsTypeAnthropic BetaManagedAgentsAnthropicSkillParamsType = "anthropic"`

  - `Version string`

    Version to pin. Defaults to latest if omitted.

### Beta Managed Agents Bash Tool Config

- `type BetaManagedAgentsBashToolConfig struct{…}`

  Configuration for the bash tool.

  - `Enabled bool`

  - `Name Bash`

    - `const BashBash Bash = "bash"`

  - `PermissionPolicy BetaManagedAgentsBashToolConfigPermissionPolicyUnion`

    Permission policy for tool execution.

    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

      Tool calls are automatically approved without user confirmation.

      - `Type BetaManagedAgentsAlwaysAllowPolicyType`

        - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

      Tool calls require user confirmation before execution.

      - `Type BetaManagedAgentsAlwaysAskPolicyType`

        - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

  - `Type Bash`

    - `const BashBash Bash = "bash"`

### Beta Managed Agents Bash Tool Config Params

- `type BetaManagedAgentsBashToolConfigParamsResp struct{…}`

  Configuration override for the bash tool.

  - `Name Bash`

    Must be "bash".

    - `const BashBash Bash = "bash"`

  - `Enabled bool`

    Whether this tool is enabled and available to Claude. Overrides the default_config setting.

  - `PermissionPolicy BetaManagedAgentsBashToolConfigParamsPermissionPolicyUnionResp`

    Permission policy for tool execution.

    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

      Tool calls are automatically approved without user confirmation.

      - `Type BetaManagedAgentsAlwaysAllowPolicyType`

        - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

      Tool calls require user confirmation before execution.

      - `Type BetaManagedAgentsAlwaysAskPolicyType`

        - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

  - `Type BetaManagedAgentsBashToolConfigParamsType`

    - `const BetaManagedAgentsBashToolConfigParamsTypeBash BetaManagedAgentsBashToolConfigParamsType = "bash"`

### Beta Managed Agents Custom Skill

- `type BetaManagedAgentsCustomSkill struct{…}`

  A resolved user-created custom skill.

  - `SkillID string`

  - `Type BetaManagedAgentsCustomSkillType`

    - `const BetaManagedAgentsCustomSkillTypeCustom BetaManagedAgentsCustomSkillType = "custom"`

  - `Version string`

### Beta Managed Agents Custom Skill Params

- `type BetaManagedAgentsCustomSkillParamsResp struct{…}`

  A user-created custom skill.

  - `SkillID string`

    Tagged ID of the custom skill (e.g., "skill_01XJ5...").

  - `Type BetaManagedAgentsCustomSkillParamsType`

    - `const BetaManagedAgentsCustomSkillParamsTypeCustom BetaManagedAgentsCustomSkillParamsType = "custom"`

  - `Version string`

    Version to pin. Defaults to latest if omitted.

### Beta Managed Agents Custom Tool

- `type BetaManagedAgentsCustomTool struct{…}`

  A custom tool as returned in API responses.

  - `Description string`

  - `InputSchema BetaManagedAgentsCustomToolInputSchema`

    JSON Schema for custom tool input parameters.

    - `Type Object`

      - `const ObjectObject Object = "object"`

    - `Properties map[string, any]`

    - `Required []string`

  - `Name string`

  - `Type BetaManagedAgentsCustomToolType`

    - `const BetaManagedAgentsCustomToolTypeCustom BetaManagedAgentsCustomToolType = "custom"`

### Beta Managed Agents Custom Tool Input Schema

- `type BetaManagedAgentsCustomToolInputSchema struct{…}`

  JSON Schema for custom tool input parameters.

  - `Type Object`

    - `const ObjectObject Object = "object"`

  - `Properties map[string, any]`

  - `Required []string`

### Beta Managed Agents Custom Tool Params

- `type BetaManagedAgentsCustomToolParamsResp struct{…}`

  A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

  - `Description string`

    Description of what the tool does, shown to the agent to help it decide when to use the tool.

  - `InputSchema BetaManagedAgentsCustomToolInputSchema`

    JSON Schema for custom tool input parameters.

    - `Type Object`

      - `const ObjectObject Object = "object"`

    - `Properties map[string, any]`

    - `Required []string`

  - `Name string`

    Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

  - `Type BetaManagedAgentsCustomToolParamsType`

    - `const BetaManagedAgentsCustomToolParamsTypeCustom BetaManagedAgentsCustomToolParamsType = "custom"`

### Beta Managed Agents Edit Tool Config

- `type BetaManagedAgentsEditToolConfig struct{…}`

  Configuration for the edit tool.

  - `Enabled bool`

  - `Name Edit`

    - `const EditEdit Edit = "edit"`

  - `PermissionPolicy BetaManagedAgentsEditToolConfigPermissionPolicyUnion`

    Permission policy for tool execution.

    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

      Tool calls are automatically approved without user confirmation.

      - `Type BetaManagedAgentsAlwaysAllowPolicyType`

        - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

      Tool calls require user confirmation before execution.

      - `Type BetaManagedAgentsAlwaysAskPolicyType`

        - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

  - `Type Edit`

    - `const EditEdit Edit = "edit"`

### Beta Managed Agents Edit Tool Config Params

- `type BetaManagedAgentsEditToolConfigParamsResp struct{…}`

  Configuration override for the edit tool.

  - `Name Edit`

    Must be "edit".

    - `const EditEdit Edit = "edit"`

  - `Enabled bool`

    Whether this tool is enabled and available to Claude. Overrides the default_config setting.

  - `PermissionPolicy BetaManagedAgentsEditToolConfigParamsPermissionPolicyUnionResp`

    Permission policy for tool execution.

    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

      Tool calls are automatically approved without user confirmation.

      - `Type BetaManagedAgentsAlwaysAllowPolicyType`

        - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

      Tool calls require user confirmation before execution.

      - `Type BetaManagedAgentsAlwaysAskPolicyType`

        - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

  - `Type BetaManagedAgentsEditToolConfigParamsType`

    - `const BetaManagedAgentsEditToolConfigParamsTypeEdit BetaManagedAgentsEditToolConfigParamsType = "edit"`

### Beta Managed Agents Effort High

- `type BetaManagedAgentsEffortHigh struct{…}`

  High effort. Favors reasoning depth.

  - `Type BetaManagedAgentsEffortHighType`

    - `const BetaManagedAgentsEffortHighTypeHigh BetaManagedAgentsEffortHighType = "high"`

### Beta Managed Agents Effort Low

- `type BetaManagedAgentsEffortLow struct{…}`

  Low effort. Favors latency over reasoning depth.

  - `Type BetaManagedAgentsEffortLowType`

    - `const BetaManagedAgentsEffortLowTypeLow BetaManagedAgentsEffortLowType = "low"`

### Beta Managed Agents Effort Max

- `type BetaManagedAgentsEffortMax struct{…}`

  Maximum effort. Favors reasoning depth over latency.

  - `Type BetaManagedAgentsEffortMaxType`

    - `const BetaManagedAgentsEffortMaxTypeMax BetaManagedAgentsEffortMaxType = "max"`

### Beta Managed Agents Effort Medium

- `type BetaManagedAgentsEffortMedium struct{…}`

  Medium effort. Balances latency and reasoning depth.

  - `Type BetaManagedAgentsEffortMediumType`

    - `const BetaManagedAgentsEffortMediumTypeMedium BetaManagedAgentsEffortMediumType = "medium"`

### Beta Managed Agents Effort Xhigh

- `type BetaManagedAgentsEffortXhigh struct{…}`

  Extra-high effort. Not all models accept this level.

  - `Type BetaManagedAgentsEffortXhighType`

    - `const BetaManagedAgentsEffortXhighTypeXhigh BetaManagedAgentsEffortXhighType = "xhigh"`

### Beta Managed Agents Glob Tool Config

- `type BetaManagedAgentsGlobToolConfig struct{…}`

  Configuration for the glob tool.

  - `Enabled bool`

  - `Name Glob`

    - `const GlobGlob Glob = "glob"`

  - `PermissionPolicy BetaManagedAgentsGlobToolConfigPermissionPolicyUnion`

    Permission policy for tool execution.

    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

      Tool calls are automatically approved without user confirmation.

      - `Type BetaManagedAgentsAlwaysAllowPolicyType`

        - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

      Tool calls require user confirmation before execution.

      - `Type BetaManagedAgentsAlwaysAskPolicyType`

        - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

  - `Type Glob`

    - `const GlobGlob Glob = "glob"`

### Beta Managed Agents Glob Tool Config Params

- `type BetaManagedAgentsGlobToolConfigParamsResp struct{…}`

  Configuration override for the glob tool.

  - `Name Glob`

    Must be "glob".

    - `const GlobGlob Glob = "glob"`

  - `Enabled bool`

    Whether this tool is enabled and available to Claude. Overrides the default_config setting.

  - `PermissionPolicy BetaManagedAgentsGlobToolConfigParamsPermissionPolicyUnionResp`

    Permission policy for tool execution.

    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

      Tool calls are automatically approved without user confirmation.

      - `Type BetaManagedAgentsAlwaysAllowPolicyType`

        - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

      Tool calls require user confirmation before execution.

      - `Type BetaManagedAgentsAlwaysAskPolicyType`

        - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

  - `Type BetaManagedAgentsGlobToolConfigParamsType`

    - `const BetaManagedAgentsGlobToolConfigParamsTypeGlob BetaManagedAgentsGlobToolConfigParamsType = "glob"`

### Beta Managed Agents Grep Tool Config

- `type BetaManagedAgentsGrepToolConfig struct{…}`

  Configuration for the grep tool.

  - `Enabled bool`

  - `Name Grep`

    - `const GrepGrep Grep = "grep"`

  - `PermissionPolicy BetaManagedAgentsGrepToolConfigPermissionPolicyUnion`

    Permission policy for tool execution.

    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

      Tool calls are automatically approved without user confirmation.

      - `Type BetaManagedAgentsAlwaysAllowPolicyType`

        - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

      Tool calls require user confirmation before execution.

      - `Type BetaManagedAgentsAlwaysAskPolicyType`

        - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

  - `Type Grep`

    - `const GrepGrep Grep = "grep"`

### Beta Managed Agents Grep Tool Config Params

- `type BetaManagedAgentsGrepToolConfigParamsResp struct{…}`

  Configuration override for the grep tool.

  - `Name Grep`

    Must be "grep".

    - `const GrepGrep Grep = "grep"`

  - `Enabled bool`

    Whether this tool is enabled and available to Claude. Overrides the default_config setting.

  - `PermissionPolicy BetaManagedAgentsGrepToolConfigParamsPermissionPolicyUnionResp`

    Permission policy for tool execution.

    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

      Tool calls are automatically approved without user confirmation.

      - `Type BetaManagedAgentsAlwaysAllowPolicyType`

        - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

      Tool calls require user confirmation before execution.

      - `Type BetaManagedAgentsAlwaysAskPolicyType`

        - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

  - `Type BetaManagedAgentsGrepToolConfigParamsType`

    - `const BetaManagedAgentsGrepToolConfigParamsTypeGrep BetaManagedAgentsGrepToolConfigParamsType = "grep"`

### Beta Managed Agents MCP Server URL Definition

- `type BetaManagedAgentsMCPServerURLDefinition struct{…}`

  URL-based MCP server connection as returned in API responses.

  - `Name string`

  - `Type BetaManagedAgentsMCPServerURLDefinitionType`

    - `const BetaManagedAgentsMCPServerURLDefinitionTypeURL BetaManagedAgentsMCPServerURLDefinitionType = "url"`

  - `URL string`

### Beta Managed Agents MCP Tool Config

- `type BetaManagedAgentsMCPToolConfig struct{…}`

  Resolved configuration for a specific MCP tool.

  - `Enabled bool`

  - `Name string`

  - `PermissionPolicy BetaManagedAgentsMCPToolConfigPermissionPolicyUnion`

    Permission policy for tool execution.

    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

      Tool calls are automatically approved without user confirmation.

      - `Type BetaManagedAgentsAlwaysAllowPolicyType`

        - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

      Tool calls require user confirmation before execution.

      - `Type BetaManagedAgentsAlwaysAskPolicyType`

        - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

### Beta Managed Agents MCP Tool Config Params

- `type BetaManagedAgentsMCPToolConfigParamsResp struct{…}`

  Configuration override for a specific MCP tool.

  - `Name string`

    Name of the MCP tool to configure. 1-128 characters.

  - `Enabled bool`

    Whether this tool is enabled. Overrides the `default_config` setting.

  - `PermissionPolicy BetaManagedAgentsMCPToolConfigParamsPermissionPolicyUnionResp`

    Permission policy for tool execution.

    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

      Tool calls are automatically approved without user confirmation.

      - `Type BetaManagedAgentsAlwaysAllowPolicyType`

        - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

      Tool calls require user confirmation before execution.

      - `Type BetaManagedAgentsAlwaysAskPolicyType`

        - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

### Beta Managed Agents MCP Toolset

- `type BetaManagedAgentsMCPToolset struct{…}`

  - `Configs []BetaManagedAgentsMCPToolConfig`

    - `Enabled bool`

    - `Name string`

    - `PermissionPolicy BetaManagedAgentsMCPToolConfigPermissionPolicyUnion`

      Permission policy for tool execution.

      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

        Tool calls are automatically approved without user confirmation.

        - `Type BetaManagedAgentsAlwaysAllowPolicyType`

          - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

        Tool calls require user confirmation before execution.

        - `Type BetaManagedAgentsAlwaysAskPolicyType`

          - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

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

    - `const BetaManagedAgentsMCPToolsetTypeMCPToolset BetaManagedAgentsMCPToolsetType = "mcp_toolset"`

### Beta Managed Agents MCP Toolset Default Config

- `type BetaManagedAgentsMCPToolsetDefaultConfig struct{…}`

  Resolved default configuration for all tools from an MCP server.

  - `Enabled bool`

  - `PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigPermissionPolicyUnion`

    Permission policy for tool execution.

    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

      Tool calls are automatically approved without user confirmation.

      - `Type BetaManagedAgentsAlwaysAllowPolicyType`

        - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

      Tool calls require user confirmation before execution.

      - `Type BetaManagedAgentsAlwaysAskPolicyType`

        - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

### Beta Managed Agents MCP Toolset Default Config Params

- `type BetaManagedAgentsMCPToolsetDefaultConfigParamsResp struct{…}`

  Default configuration for all tools from an MCP server.

  - `Enabled bool`

    Whether tools are enabled by default. Defaults to true if not specified.

  - `PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigParamsPermissionPolicyUnionResp`

    Permission policy for tool execution.

    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

      Tool calls are automatically approved without user confirmation.

      - `Type BetaManagedAgentsAlwaysAllowPolicyType`

        - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

      Tool calls require user confirmation before execution.

      - `Type BetaManagedAgentsAlwaysAskPolicyType`

        - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

### Beta Managed Agents MCP Toolset Params

- `type BetaManagedAgentsMCPToolsetParamsResp struct{…}`

  Configuration for tools from an MCP server defined in `mcp_servers`.

  - `MCPServerName string`

    Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

  - `Type BetaManagedAgentsMCPToolsetParamsType`

    - `const BetaManagedAgentsMCPToolsetParamsTypeMCPToolset BetaManagedAgentsMCPToolsetParamsType = "mcp_toolset"`

  - `Configs []BetaManagedAgentsMCPToolConfigParamsResp`

    Per-tool configuration overrides.

    - `Name string`

      Name of the MCP tool to configure. 1-128 characters.

    - `Enabled bool`

      Whether this tool is enabled. Overrides the `default_config` setting.

    - `PermissionPolicy BetaManagedAgentsMCPToolConfigParamsPermissionPolicyUnionResp`

      Permission policy for tool execution.

      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

        Tool calls are automatically approved without user confirmation.

        - `Type BetaManagedAgentsAlwaysAllowPolicyType`

          - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

        Tool calls require user confirmation before execution.

        - `Type BetaManagedAgentsAlwaysAskPolicyType`

          - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

  - `DefaultConfig BetaManagedAgentsMCPToolsetDefaultConfigParamsResp`

    Default configuration for all tools from an MCP server.

    - `Enabled bool`

      Whether tools are enabled by default. Defaults to true if not specified.

    - `PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigParamsPermissionPolicyUnionResp`

      Permission policy for tool execution.

      - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

        Tool calls are automatically approved without user confirmation.

      - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

        Tool calls require user confirmation before execution.

### Beta Managed Agents Model

- `type BetaManagedAgentsModel interface{…}`

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

### Beta Managed Agents Model Config

- `type BetaManagedAgentsModelConfig struct{…}`

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

  - `Effort BetaManagedAgentsModelConfigEffortUnion`

    How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

    - `type BetaManagedAgentsEffortLow struct{…}`

      Low effort. Favors latency over reasoning depth.

      - `Type BetaManagedAgentsEffortLowType`

        - `const BetaManagedAgentsEffortLowTypeLow BetaManagedAgentsEffortLowType = "low"`

    - `type BetaManagedAgentsEffortMedium struct{…}`

      Medium effort. Balances latency and reasoning depth.

      - `Type BetaManagedAgentsEffortMediumType`

        - `const BetaManagedAgentsEffortMediumTypeMedium BetaManagedAgentsEffortMediumType = "medium"`

    - `type BetaManagedAgentsEffortHigh struct{…}`

      High effort. Favors reasoning depth.

      - `Type BetaManagedAgentsEffortHighType`

        - `const BetaManagedAgentsEffortHighTypeHigh BetaManagedAgentsEffortHighType = "high"`

    - `type BetaManagedAgentsEffortXhigh struct{…}`

      Extra-high effort. Not all models accept this level.

      - `Type BetaManagedAgentsEffortXhighType`

        - `const BetaManagedAgentsEffortXhighTypeXhigh BetaManagedAgentsEffortXhighType = "xhigh"`

    - `type BetaManagedAgentsEffortMax struct{…}`

      Maximum effort. Favors reasoning depth over latency.

      - `Type BetaManagedAgentsEffortMaxType`

        - `const BetaManagedAgentsEffortMaxTypeMax BetaManagedAgentsEffortMaxType = "max"`

  - `InferenceGeo string`

    Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

  - `Speed BetaManagedAgentsModelConfigSpeed`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `const BetaManagedAgentsModelConfigSpeedStandard BetaManagedAgentsModelConfigSpeed = "standard"`

    - `const BetaManagedAgentsModelConfigSpeedFast BetaManagedAgentsModelConfigSpeed = "fast"`

### Beta Managed Agents Model Config Params

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

  - `Effort BetaManagedAgentsModelConfigParamsEffortUnionResp`

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

        - `const BetaManagedAgentsEffortLowTypeLow BetaManagedAgentsEffortLowType = "low"`

    - `type BetaManagedAgentsEffortMedium struct{…}`

      Medium effort. Balances latency and reasoning depth.

      - `Type BetaManagedAgentsEffortMediumType`

        - `const BetaManagedAgentsEffortMediumTypeMedium BetaManagedAgentsEffortMediumType = "medium"`

    - `type BetaManagedAgentsEffortHigh struct{…}`

      High effort. Favors reasoning depth.

      - `Type BetaManagedAgentsEffortHighType`

        - `const BetaManagedAgentsEffortHighTypeHigh BetaManagedAgentsEffortHighType = "high"`

    - `type BetaManagedAgentsEffortXhigh struct{…}`

      Extra-high effort. Not all models accept this level.

      - `Type BetaManagedAgentsEffortXhighType`

        - `const BetaManagedAgentsEffortXhighTypeXhigh BetaManagedAgentsEffortXhighType = "xhigh"`

    - `type BetaManagedAgentsEffortMax struct{…}`

      Maximum effort. Favors reasoning depth over latency.

      - `Type BetaManagedAgentsEffortMaxType`

        - `const BetaManagedAgentsEffortMaxTypeMax BetaManagedAgentsEffortMaxType = "max"`

  - `InferenceGeo string`

    Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo. On update, `model` is whole-object replacement — omitting inference_geo clears it.

  - `Speed BetaManagedAgentsModelConfigParamsSpeed`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `const BetaManagedAgentsModelConfigParamsSpeedStandard BetaManagedAgentsModelConfigParamsSpeed = "standard"`

    - `const BetaManagedAgentsModelConfigParamsSpeedFast BetaManagedAgentsModelConfigParamsSpeed = "fast"`

### Beta Managed Agents Multiagent Coordinator

- `type BetaManagedAgentsMultiagentCoordinator struct{…}`

  Resolved coordinator topology with a concrete agent roster.

  - `Agents []BetaManagedAgentsMultiagentCoordinatorAgentUnion`

    Agents the coordinator may spawn as session threads, each resolved to a specific version.

    - `type BetaManagedAgentsAgentReference struct{…}`

      A resolved agent reference with a concrete version.

      - `ID string`

      - `Type BetaManagedAgentsAgentReferenceType`

        - `const BetaManagedAgentsAgentReferenceTypeAgent BetaManagedAgentsAgentReferenceType = "agent"`

      - `Version int64`

    - `type BetaManagedAgentsAdvisor struct{…}`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `Model string`

        The advisor model id.

      - `Type BetaManagedAgentsAdvisorType`

        - `const BetaManagedAgentsAdvisorTypeAdvisor BetaManagedAgentsAdvisorType = "advisor"`

  - `Type BetaManagedAgentsMultiagentCoordinatorType`

    - `const BetaManagedAgentsMultiagentCoordinatorTypeCoordinator BetaManagedAgentsMultiagentCoordinatorType = "coordinator"`

### Beta Managed Agents Multiagent Coordinator Params

- `type BetaManagedAgentsMultiagentCoordinatorParamsResp struct{…}`

  A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.

  - `Agents []BetaManagedAgentsMultiagentRosterEntryParamsUnionResp`

    Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).

    - `string`

    - `type BetaManagedAgentsAgentParamsResp struct{…}`

      Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

      - `ID string`

        The `agent` ID.

      - `Type BetaManagedAgentsAgentParamsType`

        - `const BetaManagedAgentsAgentParamsTypeAgent BetaManagedAgentsAgentParamsType = "agent"`

      - `Version int64`

        The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

    - `type BetaManagedAgentsMultiagentSelfParamsResp struct{…}`

      Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

      - `Type BetaManagedAgentsMultiagentSelfParamsType`

        - `const BetaManagedAgentsMultiagentSelfParamsTypeSelf BetaManagedAgentsMultiagentSelfParamsType = "self"`

    - `type BetaManagedAgentsAdvisorParamsResp struct{…}`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn. At most one per roster; the entry occupies the roster name `anthropic.advisor`.

      - `Model string`

        A Claude model id. The model must be permitted as an advisor for this agent's model — see the sessions/threads/advisor spec.

      - `Type BetaManagedAgentsAdvisorParamsType`

        - `const BetaManagedAgentsAdvisorParamsTypeAdvisor BetaManagedAgentsAdvisorParamsType = "advisor"`

  - `Type BetaManagedAgentsMultiagentCoordinatorParamsType`

    - `const BetaManagedAgentsMultiagentCoordinatorParamsTypeCoordinator BetaManagedAgentsMultiagentCoordinatorParamsType = "coordinator"`

### Beta Managed Agents Multiagent Self Params

- `type BetaManagedAgentsMultiagentSelfParamsResp struct{…}`

  Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

  - `Type BetaManagedAgentsMultiagentSelfParamsType`

    - `const BetaManagedAgentsMultiagentSelfParamsTypeSelf BetaManagedAgentsMultiagentSelfParamsType = "self"`

### Beta Managed Agents Read Tool Config

- `type BetaManagedAgentsReadToolConfig struct{…}`

  Configuration for the read tool.

  - `Enabled bool`

  - `Name Read`

    - `const ReadRead Read = "read"`

  - `PermissionPolicy BetaManagedAgentsReadToolConfigPermissionPolicyUnion`

    Permission policy for tool execution.

    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

      Tool calls are automatically approved without user confirmation.

      - `Type BetaManagedAgentsAlwaysAllowPolicyType`

        - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

      Tool calls require user confirmation before execution.

      - `Type BetaManagedAgentsAlwaysAskPolicyType`

        - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

  - `Type Read`

    - `const ReadRead Read = "read"`

### Beta Managed Agents Read Tool Config Params

- `type BetaManagedAgentsReadToolConfigParamsResp struct{…}`

  Configuration override for the read tool.

  - `Name Read`

    Must be "read".

    - `const ReadRead Read = "read"`

  - `Enabled bool`

    Whether this tool is enabled and available to Claude. Overrides the default_config setting.

  - `PermissionPolicy BetaManagedAgentsReadToolConfigParamsPermissionPolicyUnionResp`

    Permission policy for tool execution.

    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

      Tool calls are automatically approved without user confirmation.

      - `Type BetaManagedAgentsAlwaysAllowPolicyType`

        - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

      Tool calls require user confirmation before execution.

      - `Type BetaManagedAgentsAlwaysAskPolicyType`

        - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

  - `Type BetaManagedAgentsReadToolConfigParamsType`

    - `const BetaManagedAgentsReadToolConfigParamsTypeRead BetaManagedAgentsReadToolConfigParamsType = "read"`

### Beta Managed Agents Session Thread Agent

- `type BetaManagedAgentsSessionThreadAgent struct{…}`

  Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

  - `ID string`

  - `Description string`

  - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

    - `Name string`

    - `Type BetaManagedAgentsMCPServerURLDefinitionType`

      - `const BetaManagedAgentsMCPServerURLDefinitionTypeURL BetaManagedAgentsMCPServerURLDefinitionType = "url"`

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

    - `Effort BetaManagedAgentsModelConfigEffortUnion`

      How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

      - `type BetaManagedAgentsEffortLow struct{…}`

        Low effort. Favors latency over reasoning depth.

        - `Type BetaManagedAgentsEffortLowType`

          - `const BetaManagedAgentsEffortLowTypeLow BetaManagedAgentsEffortLowType = "low"`

      - `type BetaManagedAgentsEffortMedium struct{…}`

        Medium effort. Balances latency and reasoning depth.

        - `Type BetaManagedAgentsEffortMediumType`

          - `const BetaManagedAgentsEffortMediumTypeMedium BetaManagedAgentsEffortMediumType = "medium"`

      - `type BetaManagedAgentsEffortHigh struct{…}`

        High effort. Favors reasoning depth.

        - `Type BetaManagedAgentsEffortHighType`

          - `const BetaManagedAgentsEffortHighTypeHigh BetaManagedAgentsEffortHighType = "high"`

      - `type BetaManagedAgentsEffortXhigh struct{…}`

        Extra-high effort. Not all models accept this level.

        - `Type BetaManagedAgentsEffortXhighType`

          - `const BetaManagedAgentsEffortXhighTypeXhigh BetaManagedAgentsEffortXhighType = "xhigh"`

      - `type BetaManagedAgentsEffortMax struct{…}`

        Maximum effort. Favors reasoning depth over latency.

        - `Type BetaManagedAgentsEffortMaxType`

          - `const BetaManagedAgentsEffortMaxTypeMax BetaManagedAgentsEffortMaxType = "max"`

    - `InferenceGeo string`

      Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

    - `Speed BetaManagedAgentsModelConfigSpeed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `const BetaManagedAgentsModelConfigSpeedStandard BetaManagedAgentsModelConfigSpeed = "standard"`

      - `const BetaManagedAgentsModelConfigSpeedFast BetaManagedAgentsModelConfigSpeed = "fast"`

  - `Name string`

  - `Skills []BetaManagedAgentsSessionThreadAgentSkillUnion`

    - `type BetaManagedAgentsAnthropicSkill struct{…}`

      A resolved Anthropic-managed skill.

      - `SkillID string`

      - `Type BetaManagedAgentsAnthropicSkillType`

        - `const BetaManagedAgentsAnthropicSkillTypeAnthropic BetaManagedAgentsAnthropicSkillType = "anthropic"`

      - `Version string`

    - `type BetaManagedAgentsCustomSkill struct{…}`

      A resolved user-created custom skill.

      - `SkillID string`

      - `Type BetaManagedAgentsCustomSkillType`

        - `const BetaManagedAgentsCustomSkillTypeCustom BetaManagedAgentsCustomSkillType = "custom"`

      - `Version string`

  - `System string`

  - `Tools []BetaManagedAgentsSessionThreadAgentToolUnion`

    - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

      - `Configs []BetaManagedAgentsAgentToolConfigUnion`

        - `type BetaManagedAgentsBashToolConfig struct{…}`

          Configuration for the bash tool.

          - `Enabled bool`

          - `Name Bash`

            - `const BashBash Bash = "bash"`

          - `PermissionPolicy BetaManagedAgentsBashToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

              - `Type BetaManagedAgentsAlwaysAllowPolicyType`

                - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

              - `Type BetaManagedAgentsAlwaysAskPolicyType`

                - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

          - `Type Bash`

            - `const BashBash Bash = "bash"`

        - `type BetaManagedAgentsEditToolConfig struct{…}`

          Configuration for the edit tool.

          - `Enabled bool`

          - `Name Edit`

            - `const EditEdit Edit = "edit"`

          - `PermissionPolicy BetaManagedAgentsEditToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Edit`

            - `const EditEdit Edit = "edit"`

        - `type BetaManagedAgentsReadToolConfig struct{…}`

          Configuration for the read tool.

          - `Enabled bool`

          - `Name Read`

            - `const ReadRead Read = "read"`

          - `PermissionPolicy BetaManagedAgentsReadToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Read`

            - `const ReadRead Read = "read"`

        - `type BetaManagedAgentsWriteToolConfig struct{…}`

          Configuration for the write tool.

          - `Enabled bool`

          - `Name Write`

            - `const WriteWrite Write = "write"`

          - `PermissionPolicy BetaManagedAgentsWriteToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Write`

            - `const WriteWrite Write = "write"`

        - `type BetaManagedAgentsGlobToolConfig struct{…}`

          Configuration for the glob tool.

          - `Enabled bool`

          - `Name Glob`

            - `const GlobGlob Glob = "glob"`

          - `PermissionPolicy BetaManagedAgentsGlobToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Glob`

            - `const GlobGlob Glob = "glob"`

        - `type BetaManagedAgentsGrepToolConfig struct{…}`

          Configuration for the grep tool.

          - `Enabled bool`

          - `Name Grep`

            - `const GrepGrep Grep = "grep"`

          - `PermissionPolicy BetaManagedAgentsGrepToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Grep`

            - `const GrepGrep Grep = "grep"`

        - `type BetaManagedAgentsWebFetchToolConfig struct{…}`

          Configuration for the web_fetch tool.

          - `Enabled bool`

          - `Name WebFetch`

            - `const WebFetchWebFetch WebFetch = "web_fetch"`

          - `PermissionPolicy BetaManagedAgentsWebFetchToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type WebFetch`

            - `const WebFetchWebFetch WebFetch = "web_fetch"`

          - `AllowedDomains []string`

          - `BlockedDomains []string`

          - `MaxContentTokens int64`

        - `type BetaManagedAgentsWebSearchToolConfig struct{…}`

          Configuration for the web_search tool.

          - `Enabled bool`

          - `Name WebSearch`

            - `const WebSearchWebSearch WebSearch = "web_search"`

          - `PermissionPolicy BetaManagedAgentsWebSearchToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type WebSearch`

            - `const WebSearchWebSearch WebSearch = "web_search"`

          - `AllowedDomains []string`

          - `BlockedDomains []string`

          - `UserLocation BetaManagedAgentsUserLocation`

            Approximate user location for search result localization.

            - `Type Approximate`

              Location precision. Only "approximate" is supported.

              - `const ApproximateApproximate Approximate = "approximate"`

            - `City string`

              City name.

            - `Country string`

              Two-letter ISO 3166-1 country code, uppercase.

            - `Region string`

              Region or state name.

            - `Timezone string`

              IANA timezone identifier, e.g. "America/Los_Angeles".

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

        - `const BetaManagedAgentsAgentToolset20260401TypeAgentToolset20260401 BetaManagedAgentsAgentToolset20260401Type = "agent_toolset_20260401"`

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

        - `const BetaManagedAgentsMCPToolsetTypeMCPToolset BetaManagedAgentsMCPToolsetType = "mcp_toolset"`

    - `type BetaManagedAgentsCustomTool struct{…}`

      A custom tool as returned in API responses.

      - `Description string`

      - `InputSchema BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `Type Object`

          - `const ObjectObject Object = "object"`

        - `Properties map[string, any]`

        - `Required []string`

      - `Name string`

      - `Type BetaManagedAgentsCustomToolType`

        - `const BetaManagedAgentsCustomToolTypeCustom BetaManagedAgentsCustomToolType = "custom"`

  - `Type BetaManagedAgentsSessionThreadAgentType`

    - `const BetaManagedAgentsSessionThreadAgentTypeAgent BetaManagedAgentsSessionThreadAgentType = "agent"`

  - `Version int64`

### Beta Managed Agents Skill Params

- `type BetaManagedAgentsSkillParamsUnionResp interface{…}`

  Skill to load in the session container.

  - `type BetaManagedAgentsAnthropicSkillParamsResp struct{…}`

    An Anthropic-managed skill.

    - `SkillID string`

      Identifier of the Anthropic skill (e.g., "xlsx").

    - `Type BetaManagedAgentsAnthropicSkillParamsType`

      - `const BetaManagedAgentsAnthropicSkillParamsTypeAnthropic BetaManagedAgentsAnthropicSkillParamsType = "anthropic"`

    - `Version string`

      Version to pin. Defaults to latest if omitted.

  - `type BetaManagedAgentsCustomSkillParamsResp struct{…}`

    A user-created custom skill.

    - `SkillID string`

      Tagged ID of the custom skill (e.g., "skill_01XJ5...").

    - `Type BetaManagedAgentsCustomSkillParamsType`

      - `const BetaManagedAgentsCustomSkillParamsTypeCustom BetaManagedAgentsCustomSkillParamsType = "custom"`

    - `Version string`

      Version to pin. Defaults to latest if omitted.

### Beta Managed Agents URL MCP Server Params

- `type BetaManagedAgentsURLMCPServerParamsResp struct{…}`

  URL-based MCP server connection.

  - `Name string`

    Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

  - `Type BetaManagedAgentsURLMCPServerParamsType`

    - `const BetaManagedAgentsURLMCPServerParamsTypeURL BetaManagedAgentsURLMCPServerParamsType = "url"`

  - `URL string`

    Endpoint URL for the MCP server.

### Beta Managed Agents User Location

- `type BetaManagedAgentsUserLocation struct{…}`

  Approximate user location for search result localization.

  - `Type Approximate`

    Location precision. Only "approximate" is supported.

    - `const ApproximateApproximate Approximate = "approximate"`

  - `City string`

    City name.

  - `Country string`

    Two-letter ISO 3166-1 country code, uppercase.

  - `Region string`

    Region or state name.

  - `Timezone string`

    IANA timezone identifier, e.g. "America/Los_Angeles".

### Beta Managed Agents Web Fetch Tool Config

- `type BetaManagedAgentsWebFetchToolConfig struct{…}`

  Configuration for the web_fetch tool.

  - `Enabled bool`

  - `Name WebFetch`

    - `const WebFetchWebFetch WebFetch = "web_fetch"`

  - `PermissionPolicy BetaManagedAgentsWebFetchToolConfigPermissionPolicyUnion`

    Permission policy for tool execution.

    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

      Tool calls are automatically approved without user confirmation.

      - `Type BetaManagedAgentsAlwaysAllowPolicyType`

        - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

      Tool calls require user confirmation before execution.

      - `Type BetaManagedAgentsAlwaysAskPolicyType`

        - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

  - `Type WebFetch`

    - `const WebFetchWebFetch WebFetch = "web_fetch"`

  - `AllowedDomains []string`

  - `BlockedDomains []string`

  - `MaxContentTokens int64`

### Beta Managed Agents Web Fetch Tool Config Params

- `type BetaManagedAgentsWebFetchToolConfigParamsResp struct{…}`

  Configuration override for the web_fetch tool.

  - `Name WebFetch`

    Must be "web_fetch".

    - `const WebFetchWebFetch WebFetch = "web_fetch"`

  - `AllowedDomains []string`

    Only fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

  - `BlockedDomains []string`

    Never fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

  - `Enabled bool`

    Whether this tool is enabled and available to Claude. Overrides the default_config setting.

  - `MaxContentTokens int64`

    Maximum number of tokens of fetched text content to include in context per call. Does not apply to binary content such as PDFs.

  - `PermissionPolicy BetaManagedAgentsWebFetchToolConfigParamsPermissionPolicyUnionResp`

    Permission policy for tool execution.

    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

      Tool calls are automatically approved without user confirmation.

      - `Type BetaManagedAgentsAlwaysAllowPolicyType`

        - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

      Tool calls require user confirmation before execution.

      - `Type BetaManagedAgentsAlwaysAskPolicyType`

        - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

  - `Type BetaManagedAgentsWebFetchToolConfigParamsType`

    - `const BetaManagedAgentsWebFetchToolConfigParamsTypeWebFetch BetaManagedAgentsWebFetchToolConfigParamsType = "web_fetch"`

### Beta Managed Agents Web Search Tool Config

- `type BetaManagedAgentsWebSearchToolConfig struct{…}`

  Configuration for the web_search tool.

  - `Enabled bool`

  - `Name WebSearch`

    - `const WebSearchWebSearch WebSearch = "web_search"`

  - `PermissionPolicy BetaManagedAgentsWebSearchToolConfigPermissionPolicyUnion`

    Permission policy for tool execution.

    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

      Tool calls are automatically approved without user confirmation.

      - `Type BetaManagedAgentsAlwaysAllowPolicyType`

        - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

      Tool calls require user confirmation before execution.

      - `Type BetaManagedAgentsAlwaysAskPolicyType`

        - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

  - `Type WebSearch`

    - `const WebSearchWebSearch WebSearch = "web_search"`

  - `AllowedDomains []string`

  - `BlockedDomains []string`

  - `UserLocation BetaManagedAgentsUserLocation`

    Approximate user location for search result localization.

    - `Type Approximate`

      Location precision. Only "approximate" is supported.

      - `const ApproximateApproximate Approximate = "approximate"`

    - `City string`

      City name.

    - `Country string`

      Two-letter ISO 3166-1 country code, uppercase.

    - `Region string`

      Region or state name.

    - `Timezone string`

      IANA timezone identifier, e.g. "America/Los_Angeles".

### Beta Managed Agents Web Search Tool Config Params

- `type BetaManagedAgentsWebSearchToolConfigParamsResp struct{…}`

  Configuration override for the web_search tool.

  - `Name WebSearch`

    Must be "web_search".

    - `const WebSearchWebSearch WebSearch = "web_search"`

  - `AllowedDomains []string`

    Only return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

  - `BlockedDomains []string`

    Never return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

  - `Enabled bool`

    Whether this tool is enabled and available to Claude. Overrides the default_config setting.

  - `PermissionPolicy BetaManagedAgentsWebSearchToolConfigParamsPermissionPolicyUnionResp`

    Permission policy for tool execution.

    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

      Tool calls are automatically approved without user confirmation.

      - `Type BetaManagedAgentsAlwaysAllowPolicyType`

        - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

      Tool calls require user confirmation before execution.

      - `Type BetaManagedAgentsAlwaysAskPolicyType`

        - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

  - `Type BetaManagedAgentsWebSearchToolConfigParamsType`

    - `const BetaManagedAgentsWebSearchToolConfigParamsTypeWebSearch BetaManagedAgentsWebSearchToolConfigParamsType = "web_search"`

  - `UserLocation BetaManagedAgentsUserLocation`

    Approximate user location for search result localization.

    - `Type Approximate`

      Location precision. Only "approximate" is supported.

      - `const ApproximateApproximate Approximate = "approximate"`

    - `City string`

      City name.

    - `Country string`

      Two-letter ISO 3166-1 country code, uppercase.

    - `Region string`

      Region or state name.

    - `Timezone string`

      IANA timezone identifier, e.g. "America/Los_Angeles".

### Beta Managed Agents Write Tool Config

- `type BetaManagedAgentsWriteToolConfig struct{…}`

  Configuration for the write tool.

  - `Enabled bool`

  - `Name Write`

    - `const WriteWrite Write = "write"`

  - `PermissionPolicy BetaManagedAgentsWriteToolConfigPermissionPolicyUnion`

    Permission policy for tool execution.

    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

      Tool calls are automatically approved without user confirmation.

      - `Type BetaManagedAgentsAlwaysAllowPolicyType`

        - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

      Tool calls require user confirmation before execution.

      - `Type BetaManagedAgentsAlwaysAskPolicyType`

        - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

  - `Type Write`

    - `const WriteWrite Write = "write"`

### Beta Managed Agents Write Tool Config Params

- `type BetaManagedAgentsWriteToolConfigParamsResp struct{…}`

  Configuration override for the write tool.

  - `Name Write`

    Must be "write".

    - `const WriteWrite Write = "write"`

  - `Enabled bool`

    Whether this tool is enabled and available to Claude. Overrides the default_config setting.

  - `PermissionPolicy BetaManagedAgentsWriteToolConfigParamsPermissionPolicyUnionResp`

    Permission policy for tool execution.

    - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

      Tool calls are automatically approved without user confirmation.

      - `Type BetaManagedAgentsAlwaysAllowPolicyType`

        - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

    - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

      Tool calls require user confirmation before execution.

      - `Type BetaManagedAgentsAlwaysAskPolicyType`

        - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

  - `Type BetaManagedAgentsWriteToolConfigParamsType`

    - `const BetaManagedAgentsWriteToolConfigParamsTypeWrite BetaManagedAgentsWriteToolConfigParamsType = "write"`

# Versions

## List Agent Versions

`client.Beta.Agents.Versions.List(ctx, agentID, params) (*PageCursor[BetaManagedAgentsAgent], error)`

**get** `/v1/agents/{agent_id}/versions`

List Agent Versions

### Parameters

- `agentID string`

- `params BetaAgentVersionListParams`

  - `Limit param.Field[int64]`

    Query param: Maximum results per page. Default 20, maximum 100.

  - `Page param.Field[string]`

    Query param: Opaque pagination cursor.

  - `Betas param.Field[[]AnthropicBeta]`

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

### Returns

- `type BetaManagedAgentsAgent struct{…}`

  A Managed Agents `agent`.

  - `ID string`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Description string`

  - `MCPServers []BetaManagedAgentsMCPServerURLDefinition`

    - `Name string`

    - `Type BetaManagedAgentsMCPServerURLDefinitionType`

      - `const BetaManagedAgentsMCPServerURLDefinitionTypeURL BetaManagedAgentsMCPServerURLDefinitionType = "url"`

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

    - `Effort BetaManagedAgentsModelConfigEffortUnion`

      How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

      - `type BetaManagedAgentsEffortLow struct{…}`

        Low effort. Favors latency over reasoning depth.

        - `Type BetaManagedAgentsEffortLowType`

          - `const BetaManagedAgentsEffortLowTypeLow BetaManagedAgentsEffortLowType = "low"`

      - `type BetaManagedAgentsEffortMedium struct{…}`

        Medium effort. Balances latency and reasoning depth.

        - `Type BetaManagedAgentsEffortMediumType`

          - `const BetaManagedAgentsEffortMediumTypeMedium BetaManagedAgentsEffortMediumType = "medium"`

      - `type BetaManagedAgentsEffortHigh struct{…}`

        High effort. Favors reasoning depth.

        - `Type BetaManagedAgentsEffortHighType`

          - `const BetaManagedAgentsEffortHighTypeHigh BetaManagedAgentsEffortHighType = "high"`

      - `type BetaManagedAgentsEffortXhigh struct{…}`

        Extra-high effort. Not all models accept this level.

        - `Type BetaManagedAgentsEffortXhighType`

          - `const BetaManagedAgentsEffortXhighTypeXhigh BetaManagedAgentsEffortXhighType = "xhigh"`

      - `type BetaManagedAgentsEffortMax struct{…}`

        Maximum effort. Favors reasoning depth over latency.

        - `Type BetaManagedAgentsEffortMaxType`

          - `const BetaManagedAgentsEffortMaxTypeMax BetaManagedAgentsEffortMaxType = "max"`

    - `InferenceGeo string`

      Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

    - `Speed BetaManagedAgentsModelConfigSpeed`

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

          - `const BetaManagedAgentsAgentReferenceTypeAgent BetaManagedAgentsAgentReferenceType = "agent"`

        - `Version int64`

      - `type BetaManagedAgentsAdvisor struct{…}`

        Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

        - `Model string`

          The advisor model id.

        - `Type BetaManagedAgentsAdvisorType`

          - `const BetaManagedAgentsAdvisorTypeAdvisor BetaManagedAgentsAdvisorType = "advisor"`

    - `Type BetaManagedAgentsMultiagentType`

      - `const BetaManagedAgentsMultiagentTypeCoordinator BetaManagedAgentsMultiagentType = "coordinator"`

  - `Name string`

  - `Skills []BetaManagedAgentsAgentSkillUnion`

    - `type BetaManagedAgentsAnthropicSkill struct{…}`

      A resolved Anthropic-managed skill.

      - `SkillID string`

      - `Type BetaManagedAgentsAnthropicSkillType`

        - `const BetaManagedAgentsAnthropicSkillTypeAnthropic BetaManagedAgentsAnthropicSkillType = "anthropic"`

      - `Version string`

    - `type BetaManagedAgentsCustomSkill struct{…}`

      A resolved user-created custom skill.

      - `SkillID string`

      - `Type BetaManagedAgentsCustomSkillType`

        - `const BetaManagedAgentsCustomSkillTypeCustom BetaManagedAgentsCustomSkillType = "custom"`

      - `Version string`

  - `System string`

  - `Tools []BetaManagedAgentsAgentToolUnion`

    - `type BetaManagedAgentsAgentToolset20260401 struct{…}`

      - `Configs []BetaManagedAgentsAgentToolConfigUnion`

        - `type BetaManagedAgentsBashToolConfig struct{…}`

          Configuration for the bash tool.

          - `Enabled bool`

          - `Name Bash`

            - `const BashBash Bash = "bash"`

          - `PermissionPolicy BetaManagedAgentsBashToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

              - `Type BetaManagedAgentsAlwaysAllowPolicyType`

                - `const BetaManagedAgentsAlwaysAllowPolicyTypeAlwaysAllow BetaManagedAgentsAlwaysAllowPolicyType = "always_allow"`

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

              - `Type BetaManagedAgentsAlwaysAskPolicyType`

                - `const BetaManagedAgentsAlwaysAskPolicyTypeAlwaysAsk BetaManagedAgentsAlwaysAskPolicyType = "always_ask"`

          - `Type Bash`

            - `const BashBash Bash = "bash"`

        - `type BetaManagedAgentsEditToolConfig struct{…}`

          Configuration for the edit tool.

          - `Enabled bool`

          - `Name Edit`

            - `const EditEdit Edit = "edit"`

          - `PermissionPolicy BetaManagedAgentsEditToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Edit`

            - `const EditEdit Edit = "edit"`

        - `type BetaManagedAgentsReadToolConfig struct{…}`

          Configuration for the read tool.

          - `Enabled bool`

          - `Name Read`

            - `const ReadRead Read = "read"`

          - `PermissionPolicy BetaManagedAgentsReadToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Read`

            - `const ReadRead Read = "read"`

        - `type BetaManagedAgentsWriteToolConfig struct{…}`

          Configuration for the write tool.

          - `Enabled bool`

          - `Name Write`

            - `const WriteWrite Write = "write"`

          - `PermissionPolicy BetaManagedAgentsWriteToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Write`

            - `const WriteWrite Write = "write"`

        - `type BetaManagedAgentsGlobToolConfig struct{…}`

          Configuration for the glob tool.

          - `Enabled bool`

          - `Name Glob`

            - `const GlobGlob Glob = "glob"`

          - `PermissionPolicy BetaManagedAgentsGlobToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Glob`

            - `const GlobGlob Glob = "glob"`

        - `type BetaManagedAgentsGrepToolConfig struct{…}`

          Configuration for the grep tool.

          - `Enabled bool`

          - `Name Grep`

            - `const GrepGrep Grep = "grep"`

          - `PermissionPolicy BetaManagedAgentsGrepToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type Grep`

            - `const GrepGrep Grep = "grep"`

        - `type BetaManagedAgentsWebFetchToolConfig struct{…}`

          Configuration for the web_fetch tool.

          - `Enabled bool`

          - `Name WebFetch`

            - `const WebFetchWebFetch WebFetch = "web_fetch"`

          - `PermissionPolicy BetaManagedAgentsWebFetchToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type WebFetch`

            - `const WebFetchWebFetch WebFetch = "web_fetch"`

          - `AllowedDomains []string`

          - `BlockedDomains []string`

          - `MaxContentTokens int64`

        - `type BetaManagedAgentsWebSearchToolConfig struct{…}`

          Configuration for the web_search tool.

          - `Enabled bool`

          - `Name WebSearch`

            - `const WebSearchWebSearch WebSearch = "web_search"`

          - `PermissionPolicy BetaManagedAgentsWebSearchToolConfigPermissionPolicyUnion`

            Permission policy for tool execution.

            - `type BetaManagedAgentsAlwaysAllowPolicy struct{…}`

              Tool calls are automatically approved without user confirmation.

            - `type BetaManagedAgentsAlwaysAskPolicy struct{…}`

              Tool calls require user confirmation before execution.

          - `Type WebSearch`

            - `const WebSearchWebSearch WebSearch = "web_search"`

          - `AllowedDomains []string`

          - `BlockedDomains []string`

          - `UserLocation BetaManagedAgentsUserLocation`

            Approximate user location for search result localization.

            - `Type Approximate`

              Location precision. Only "approximate" is supported.

              - `const ApproximateApproximate Approximate = "approximate"`

            - `City string`

              City name.

            - `Country string`

              Two-letter ISO 3166-1 country code, uppercase.

            - `Region string`

              Region or state name.

            - `Timezone string`

              IANA timezone identifier, e.g. "America/Los_Angeles".

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

        - `const BetaManagedAgentsAgentToolset20260401TypeAgentToolset20260401 BetaManagedAgentsAgentToolset20260401Type = "agent_toolset_20260401"`

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

        - `const BetaManagedAgentsMCPToolsetTypeMCPToolset BetaManagedAgentsMCPToolsetType = "mcp_toolset"`

    - `type BetaManagedAgentsCustomTool struct{…}`

      A custom tool as returned in API responses.

      - `Description string`

      - `InputSchema BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `Type Object`

          - `const ObjectObject Object = "object"`

        - `Properties map[string, any]`

        - `Required []string`

      - `Name string`

      - `Type BetaManagedAgentsCustomToolType`

        - `const BetaManagedAgentsCustomToolTypeCustom BetaManagedAgentsCustomToolType = "custom"`

  - `Type BetaManagedAgentsAgentType`

    - `const BetaManagedAgentsAgentTypeAgent BetaManagedAgentsAgentType = "agent"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `Version int64`

    The agent's current version. Starts at 1 and increments when the agent is modified.

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
	page, err := client.Beta.Agents.Versions.List(
		context.TODO(),
		"agent_011CZkYpogX7uDKUyvBTophP",
		anthropic.BetaAgentVersionListParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
}
```

#### Response

```json
{
  "data": [
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
  ],
  "next_page": "next_page"
}
```
