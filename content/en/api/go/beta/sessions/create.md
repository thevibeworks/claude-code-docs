---
title: Create Session
url: https://platform.claude.com/docs/en/api/go/beta/sessions/create
---

## Create Session

`client.Beta.Sessions.New(ctx, params) (*BetaManagedAgentsSession, error)`

**post** `/v1/sessions`

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

      - `Type BetaManagedAgentsAgentParamsType`

        - `const BetaManagedAgentsAgentParamsTypeAgent BetaManagedAgentsAgentParamsType = "agent"`

      - `Version int64`

        The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

    - `type BetaManagedAgentsAgentWithOverridesParamsResp struct{…}`

      Reference to an `agent` plus optional configuration overrides. Each provided field replaces the agent's value for the caller's use; the agent resource is unchanged.

      - `ID string`

        The `agent` ID.

      - `Type BetaManagedAgentsAgentWithOverridesParamsType`

        - `const BetaManagedAgentsAgentWithOverridesParamsTypeAgentWithOverrides BetaManagedAgentsAgentWithOverridesParamsType = "agent_with_overrides"`

      - `MCPServers []BetaManagedAgentsURLMCPServerParamsResp`

        Replacement MCP server list. Full replacement: the provided array becomes the MCP servers. Send an empty array to clear; omit to preserve the agent's servers.

        - `Name string`

          Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

        - `Type BetaManagedAgentsURLMCPServerParamsType`

          - `const BetaManagedAgentsURLMCPServerParamsTypeURL BetaManagedAgentsURLMCPServerParamsType = "url"`

        - `URL string`

          Endpoint URL for the MCP server.

      - `Model BetaManagedAgentsModelConfigParamsResp`

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

      - `Skills []BetaManagedAgentsSkillParamsUnionResp`

        Replacement skill list. Full replacement: the provided array becomes the skills. Send an empty array to clear; omit to preserve the agent's skills.

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

      - `System string`

        Replacement system prompt. Up to 100,000 characters. Set to null to clear the agent's system prompt; omit to preserve it.

      - `Tools []BetaManagedAgentsAgentWithOverridesParamsToolUnionResp`

        Replacement tool list. Full replacement: the provided array becomes the tool configuration. Send an empty array to clear; omit to preserve the agent's tools.

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

      - `Version int64`

        The specific `agent` version to use. Omit to use the latest version.

  - `EnvironmentID param.Field[string]`

    Body param: ID of the `environment` defining the container configuration for this session.

  - `Budget param.Field[BetaManagedAgentsBudgetLimit]`

    Body param: A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

  - `InitialEvents param.Field[[]BetaSessionNewParamsInitialEventUnion]`

    Body param: Initial events to send to the `session` at creation, processed in order. Supports `user.message` and `user.define_outcome` events. Maximum 50 events.

    - `type BetaManagedAgentsUserMessageEventParams struct{…}`

      Parameters for sending a user message to the session.

      - `Content []BetaManagedAgentsUserMessageEventParamsContentUnionResp`

        Array of content blocks for the user message.

        - `type BetaManagedAgentsTextBlock struct{…}`

          Regular text content.

          - `Text string`

            The text content.

          - `Type BetaManagedAgentsTextBlockType`

            - `const BetaManagedAgentsTextBlockTypeText BetaManagedAgentsTextBlockType = "text"`

        - `type BetaManagedAgentsImageBlock struct{…}`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source BetaManagedAgentsImageBlockSourceUnion`

            Union type for image source variants.

            - `type BetaManagedAgentsBase64ImageSource struct{…}`

              Base64-encoded image data.

              - `Data string`

                Base64-encoded image data.

              - `MediaType string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `Type BetaManagedAgentsBase64ImageSourceType`

                - `const BetaManagedAgentsBase64ImageSourceTypeBase64 BetaManagedAgentsBase64ImageSourceType = "base64"`

            - `type BetaManagedAgentsURLImageSource struct{…}`

              Image referenced by URL.

              - `Type BetaManagedAgentsURLImageSourceType`

                - `const BetaManagedAgentsURLImageSourceTypeURL BetaManagedAgentsURLImageSourceType = "url"`

              - `URL string`

                URL of the image to fetch.

            - `type BetaManagedAgentsFileImageSource struct{…}`

              Image referenced by file ID.

              - `FileID string`

                ID of a previously uploaded file.

              - `Type BetaManagedAgentsFileImageSourceType`

                - `const BetaManagedAgentsFileImageSourceTypeFile BetaManagedAgentsFileImageSourceType = "file"`

          - `Type BetaManagedAgentsImageBlockType`

            - `const BetaManagedAgentsImageBlockTypeImage BetaManagedAgentsImageBlockType = "image"`

        - `type BetaManagedAgentsDocumentBlock struct{…}`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source BetaManagedAgentsDocumentBlockSourceUnion`

            Union type for document source variants.

            - `type BetaManagedAgentsBase64DocumentSource struct{…}`

              Base64-encoded document data.

              - `Data string`

                Base64-encoded document data.

              - `MediaType string`

                MIME type of the document (e.g., "application/pdf").

              - `Type BetaManagedAgentsBase64DocumentSourceType`

                - `const BetaManagedAgentsBase64DocumentSourceTypeBase64 BetaManagedAgentsBase64DocumentSourceType = "base64"`

            - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

              Plain text document content.

              - `Data string`

                The plain text content.

              - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

                MIME type of the text content. Must be "text/plain".

                - `const BetaManagedAgentsPlainTextDocumentSourceMediaTypeTextPlain BetaManagedAgentsPlainTextDocumentSourceMediaType = "text/plain"`

              - `Type BetaManagedAgentsPlainTextDocumentSourceType`

                - `const BetaManagedAgentsPlainTextDocumentSourceTypeText BetaManagedAgentsPlainTextDocumentSourceType = "text"`

            - `type BetaManagedAgentsURLDocumentSource struct{…}`

              Document referenced by URL.

              - `Type BetaManagedAgentsURLDocumentSourceType`

                - `const BetaManagedAgentsURLDocumentSourceTypeURL BetaManagedAgentsURLDocumentSourceType = "url"`

              - `URL string`

                URL of the document to fetch.

            - `type BetaManagedAgentsFileDocumentSource struct{…}`

              Document referenced by file ID.

              - `FileID string`

                ID of a previously uploaded file.

              - `Type BetaManagedAgentsFileDocumentSourceType`

                - `const BetaManagedAgentsFileDocumentSourceTypeFile BetaManagedAgentsFileDocumentSourceType = "file"`

          - `Type BetaManagedAgentsDocumentBlockType`

            - `const BetaManagedAgentsDocumentBlockTypeDocument BetaManagedAgentsDocumentBlockType = "document"`

          - `Context string`

            Additional context about the document for the model.

          - `Title string`

            The title of the document.

        - `type BetaManagedAgentsRedactedBlockParam struct{…}`

          Placeholder for content withheld by Anthropic model policy.

          - `Type BetaManagedAgentsRedactedBlockType`

            - `const BetaManagedAgentsRedactedBlockTypeRedacted BetaManagedAgentsRedactedBlockType = "redacted"`

      - `Type BetaManagedAgentsUserMessageEventParamsType`

        - `const BetaManagedAgentsUserMessageEventParamsTypeUserMessage BetaManagedAgentsUserMessageEventParamsType = "user.message"`

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

            - `const BetaManagedAgentsFileRubricParamsTypeFile BetaManagedAgentsFileRubricParamsType = "file"`

        - `type BetaManagedAgentsTextRubricParams struct{…}`

          Rubric content provided inline as text.

          - `Content string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

          - `Type BetaManagedAgentsTextRubricParamsType`

            - `const BetaManagedAgentsTextRubricParamsTypeText BetaManagedAgentsTextRubricParamsType = "text"`

      - `Type BetaManagedAgentsUserDefineOutcomeEventParamsType`

        - `const BetaManagedAgentsUserDefineOutcomeEventParamsTypeUserDefineOutcome BetaManagedAgentsUserDefineOutcomeEventParamsType = "user.define_outcome"`

      - `MaxIterations int64`

        Eval→revision cycles before giving up. Default 3, max 20.

  - `Metadata param.Field[map[string, string]]`

    Body param: Arbitrary key-value metadata attached to the session. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `Resources param.Field[[]BetaSessionNewParamsResourceUnion]`

    Body param: Resources (e.g. repositories, files) to mount into the session's container.

    - `type BetaManagedAgentsGitHubRepositoryResourceParamsResp struct{…}`

      Mount a GitHub repository into the session's container.

      - `AuthorizationToken string`

        GitHub authorization token used to clone the repository.

      - `Type BetaManagedAgentsGitHubRepositoryResourceParamsType`

        - `const BetaManagedAgentsGitHubRepositoryResourceParamsTypeGitHubRepository BetaManagedAgentsGitHubRepositoryResourceParamsType = "github_repository"`

      - `URL string`

        Github URL of the repository

      - `Checkout BetaManagedAgentsGitHubRepositoryResourceParamsCheckoutUnionResp`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `type BetaManagedAgentsBranchCheckout struct{…}`

          - `Name string`

            Branch name to check out.

          - `Type BetaManagedAgentsBranchCheckoutType`

            - `const BetaManagedAgentsBranchCheckoutTypeBranch BetaManagedAgentsBranchCheckoutType = "branch"`

        - `type BetaManagedAgentsCommitCheckout struct{…}`

          - `Sha string`

            Full commit SHA to check out.

          - `Type BetaManagedAgentsCommitCheckoutType`

            - `const BetaManagedAgentsCommitCheckoutTypeCommit BetaManagedAgentsCommitCheckoutType = "commit"`

      - `MountPath string`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `type BetaManagedAgentsFileResourceParamsResp struct{…}`

      Mount a file uploaded via the Files API into the session.

      - `FileID string`

        ID of a previously uploaded file.

      - `Type BetaManagedAgentsFileResourceParamsType`

        - `const BetaManagedAgentsFileResourceParamsTypeFile BetaManagedAgentsFileResourceParamsType = "file"`

      - `MountPath string`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `type BetaManagedAgentsMemoryStoreResourceParamResp struct{…}`

      Parameters for attaching a memory store to an agent session.

      - `MemoryStoreID string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type BetaManagedAgentsMemoryStoreResourceParamType`

        - `const BetaManagedAgentsMemoryStoreResourceParamTypeMemoryStore BetaManagedAgentsMemoryStoreResourceParamType = "memory_store"`

      - `Access BetaManagedAgentsMemoryStoreResourceParamAccess`

        Access mode for an attached memory store.

        - `const BetaManagedAgentsMemoryStoreResourceParamAccessReadWrite BetaManagedAgentsMemoryStoreResourceParamAccess = "read_write"`

        - `const BetaManagedAgentsMemoryStoreResourceParamAccessReadOnly BetaManagedAgentsMemoryStoreResourceParamAccess = "read_only"`

      - `Instructions string`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `Title param.Field[string]`

    Body param: Human-readable session title.

  - `VaultIDs param.Field[[]string]`

    Body param: Vault IDs for stored credentials the agent can use during the session.

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

        - `type BetaManagedAgentsAdvisor struct{…}`

          Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

          - `Model string`

            The advisor model id.

          - `Type BetaManagedAgentsAdvisorType`

            - `const BetaManagedAgentsAdvisorTypeAdvisor BetaManagedAgentsAdvisorType = "advisor"`

      - `Type BetaManagedAgentsSessionMultiagentCoordinatorType`

        - `const BetaManagedAgentsSessionMultiagentCoordinatorTypeCoordinator BetaManagedAgentsSessionMultiagentCoordinatorType = "coordinator"`

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

      - `const BetaManagedAgentsSessionAgentTypeAgent BetaManagedAgentsSessionAgentType = "agent"`

    - `Version int64`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `Budget BetaManagedAgentsBudgetLimit`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `MaxListCost BetaMonetaryAmount`

      A monetary amount in a specific currency.

      - `Amount string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `Currency BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

        - `const BetaCurrencyUsd BetaCurrency = "USD"`

    - `Type BetaManagedAgentsBudgetLimitType`

      - `const BetaManagedAgentsBudgetLimitTypeLimit BetaManagedAgentsBudgetLimitType = "limit"`

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `EnvironmentID string`

  - `Metadata map[string, string]`

  - `OutcomeEvaluations []BetaManagedAgentsOutcomeEvaluationResource`

    Per-outcome evaluation state. One entry per define_outcome event sent to the session.

    - `CompletedAt Time`

      A timestamp in RFC 3339 format

    - `Description string`

      What the agent should produce.

    - `Explanation string`

      Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs_revision (intermediate), what's missing; for failed, why unrecoverable.

    - `Iteration int64`

      0-indexed revision cycle the outcome is currently on.

    - `OutcomeID string`

      Server-generated outc_ ID for this outcome.

    - `Result string`

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

    - `Type BetaManagedAgentsOutcomeEvaluationResourceType`

      - `const BetaManagedAgentsOutcomeEvaluationResourceTypeOutcomeEvaluation BetaManagedAgentsOutcomeEvaluationResourceType = "outcome_evaluation"`

  - `Resources []BetaManagedAgentsSessionResourceUnion`

    - `type BetaManagedAgentsGitHubRepositoryResource struct{…}`

      - `ID string`

      - `CreatedAt Time`

        A timestamp in RFC 3339 format

      - `MountPath string`

      - `Type BetaManagedAgentsGitHubRepositoryResourceType`

        - `const BetaManagedAgentsGitHubRepositoryResourceTypeGitHubRepository BetaManagedAgentsGitHubRepositoryResourceType = "github_repository"`

      - `UpdatedAt Time`

        A timestamp in RFC 3339 format

      - `URL string`

      - `Checkout BetaManagedAgentsGitHubRepositoryResourceCheckoutUnion`

        - `type BetaManagedAgentsBranchCheckout struct{…}`

          - `Name string`

            Branch name to check out.

          - `Type BetaManagedAgentsBranchCheckoutType`

            - `const BetaManagedAgentsBranchCheckoutTypeBranch BetaManagedAgentsBranchCheckoutType = "branch"`

        - `type BetaManagedAgentsCommitCheckout struct{…}`

          - `Sha string`

            Full commit SHA to check out.

          - `Type BetaManagedAgentsCommitCheckoutType`

            - `const BetaManagedAgentsCommitCheckoutTypeCommit BetaManagedAgentsCommitCheckoutType = "commit"`

    - `type BetaManagedAgentsFileResource struct{…}`

      - `ID string`

      - `CreatedAt Time`

        A timestamp in RFC 3339 format

      - `FileID string`

      - `MountPath string`

      - `Type BetaManagedAgentsFileResourceType`

        - `const BetaManagedAgentsFileResourceTypeFile BetaManagedAgentsFileResourceType = "file"`

      - `UpdatedAt Time`

        A timestamp in RFC 3339 format

    - `type BetaManagedAgentsMemoryStoreResource struct{…}`

      A memory store attached to an agent session.

      - `MemoryStoreID string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type BetaManagedAgentsMemoryStoreResourceType`

        - `const BetaManagedAgentsMemoryStoreResourceTypeMemoryStore BetaManagedAgentsMemoryStoreResourceType = "memory_store"`

      - `Access BetaManagedAgentsMemoryStoreResourceAccess`

        Access mode for an attached memory store.

        - `const BetaManagedAgentsMemoryStoreResourceAccessReadWrite BetaManagedAgentsMemoryStoreResourceAccess = "read_write"`

        - `const BetaManagedAgentsMemoryStoreResourceAccessReadOnly BetaManagedAgentsMemoryStoreResourceAccess = "read_only"`

      - `Description string`

        Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

      - `Instructions string`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      - `MountPath string`

        Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

      - `Name string`

        Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

  - `Stats BetaManagedAgentsSessionStats`

    Timing statistics for a session.

    - `ActiveSeconds float64`

      Cumulative time in seconds the session spent in running status. Excludes idle time.

    - `DurationSeconds float64`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

  - `Status BetaManagedAgentsSessionStatus`

    SessionStatus enum

    - `const BetaManagedAgentsSessionStatusRescheduling BetaManagedAgentsSessionStatus = "rescheduling"`

    - `const BetaManagedAgentsSessionStatusRunning BetaManagedAgentsSessionStatus = "running"`

    - `const BetaManagedAgentsSessionStatusIdle BetaManagedAgentsSessionStatus = "idle"`

    - `const BetaManagedAgentsSessionStatusTerminated BetaManagedAgentsSessionStatus = "terminated"`

  - `Title string`

  - `Type BetaManagedAgentsSessionType`

    - `const BetaManagedAgentsSessionTypeSession BetaManagedAgentsSessionType = "session"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `Usage BetaManagedAgentsSessionUsage`

    Cumulative token usage for a session across all turns.

    - `ActiveSeconds float64`

      Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once, unlike `stats.active_seconds`, which sums each thread's own active time. This is the duration the session's runtime cost is priced on.

    - `CacheCreation BetaManagedAgentsCacheCreationUsage`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `Ephemeral1hInputTokens int64`

        Tokens used to create 1-hour ephemeral cache entries.

      - `Ephemeral5mInputTokens int64`

        Tokens used to create 5-minute ephemeral cache entries.

    - `CacheReadInputTokens int64`

      Total tokens read from prompt cache.

    - `InputTokens int64`

      Total input tokens consumed across all turns.

    - `ListCost BetaMonetaryAmount`

      A monetary amount in a specific currency.

    - `OutputTokens int64`

      Total output tokens generated across all turns.

    - `ServerToolUse BetaManagedAgentsServerToolUsage`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `WebFetchRequests int64`

        Number of server-executed web fetch requests.

      - `WebSearchRequests int64`

        Number of server-executed web search requests.

  - `VaultIDs []string`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `DeploymentID string`

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

#### Response

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
