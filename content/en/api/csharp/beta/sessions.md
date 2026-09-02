# Sessions

## Create Session

`BetaManagedAgentsSession Beta.Sessions.Create(parameters, cancellationToken = default)`

**POST** `/v1/sessions`

Create Session

### Parameters

- `SessionCreateParams parameters`

  - `required Agent agent`

    Body param: Agent identifier. Accepts the `agent` ID string, which pins the latest version for the session, or an `agent` object with both id and version specified.

    - `string`

    - `class BetaManagedAgentsAgentParams:`

      Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

      - `required string ID`

        The `agent` ID.

        minLength: 1, maxLength: 128

      - `required Type Type`

      - `int Version`

        The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

        format: int32

    - `class BetaManagedAgentsAgentWithOverridesParams:`

      Reference to an `agent` plus optional configuration overrides. Each provided field replaces the agent's value for the caller's use; the agent resource is unchanged.

      - `required string ID`

        The `agent` ID.

        minLength: 1, maxLength: 128

      - `required Type Type`

      - `IReadOnlyList<BetaManagedAgentsUrlMcpServerParams> McpServers`

        Replacement MCP server list. Full replacement: the provided array becomes the MCP servers. Send an empty array to clear; omit to preserve the agent's servers.

        - `required string Name`

          Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

          minLength: 1, maxLength: 255

        - `required Type Type`

        - `required string Url`

          Endpoint URL for the MCP server.

          maxLength: 2048

      - `Model Model`

        Replacement model. Accepts the model string, e.g. `claude-opus-5`, or a `model_config` object. Omit to use the agent's model.

        - `enum BetaManagedAgentsModel:`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `ClaudeFable5_1`

            Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

          - `ClaudeSonnet5`

            High-performance model for coding and agents

          - `ClaudeFable5`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `ClaudeOpus5`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_8`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_7`

            Powerful intelligence for long-running agents and coding

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

        - `class BetaManagedAgentsModelConfigParams:`

          An object that defines additional configuration control over model use

          - `required BetaManagedAgentsModel ID`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `ClaudeFable5_1`

              Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

            - `ClaudeSonnet5`

              High-performance model for coding and agents

            - `ClaudeFable5`

              Next generation of intelligence for the hardest knowledge work and coding problems

            - `ClaudeOpus5`

              Powerful intelligence for long-running agents and coding

            - `ClaudeOpus4_8`

              Powerful intelligence for long-running agents and coding

            - `ClaudeOpus4_7`

              Powerful intelligence for long-running agents and coding

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

          - `Effort? Effort`

            How hard Claude works on each inference call. Accepts a bare level string (`"high"`) or `{"type": "high"}`. On create, omitting it resolves the per-model default; on update, omitting it leaves the stored value unchanged.

            - `enum BetaManagedAgentsEffortLevel:`

              How hard Claude works on each turn. Higher levels favor reasoning depth over latency. Not all models accept every level; invalid combinations are rejected at create time.

              - `Low`

              - `Medium`

              - `High`

              - `Xhigh`

              - `Max`

            - `class BetaManagedAgentsEffortLow:`

              Low effort. Favors latency over reasoning depth.

              - `required Type Type`

            - `class BetaManagedAgentsEffortMedium:`

              Medium effort. Balances latency and reasoning depth.

              - `required Type Type`

            - `class BetaManagedAgentsEffortHigh:`

              High effort. Favors reasoning depth.

              - `required Type Type`

            - `class BetaManagedAgentsEffortXhigh:`

              Extra-high effort. Not all models accept this level.

              - `required Type Type`

            - `class BetaManagedAgentsEffortMax:`

              Maximum effort. Favors reasoning depth over latency.

              - `required Type Type`

          - `string? InferenceGeo`

            Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo. On update, `model` is whole-object replacement — omitting inference_geo clears it.

          - `Speed? Speed`

            Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

            - `Standard`

            - `Fast`

      - `IReadOnlyList<BetaManagedAgentsSkillParams> Skills`

        Replacement skill list. Full replacement: the provided array becomes the skills. Send an empty array to clear; omit to preserve the agent's skills.

        - `class BetaManagedAgentsAnthropicSkillParams:`

          An Anthropic-managed skill.

          - `required string SkillID`

            Identifier of the Anthropic skill (e.g., "xlsx").

            minLength: 1, maxLength: 64

          - `required Type Type`

          - `string? Version`

            Version to pin. Defaults to latest if omitted.

            minLength: 1, maxLength: 64

        - `class BetaManagedAgentsCustomSkillParams:`

          A user-created custom skill.

          - `required string SkillID`

            Tagged ID of the custom skill (e.g., "skill_01XJ5...").

            minLength: 1, maxLength: 64

          - `required Type Type`

          - `string? Version`

            Version to pin. Defaults to latest if omitted.

            minLength: 1, maxLength: 64

      - `string? System`

        Replacement system prompt. Up to 100,000 characters. Set to null to clear the agent's system prompt; omit to preserve it.

        maxLength: 100000

      - `IReadOnlyList<Tool> Tools`

        Replacement tool list. Full replacement: the provided array becomes the tool configuration. Send an empty array to clear; omit to preserve the agent's tools.

        - `class BetaManagedAgentsAgentToolset20260401Params:`

          Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

          - `required Type Type`

          - `IReadOnlyList<BetaManagedAgentsAgentToolConfigParams> Configs`

            Per-tool configuration overrides.

            - `class BetaManagedAgentsBashToolConfigParams:`

              Configuration override for the bash tool.

              - `JsonElement Name constant`

                Must be "bash".

              - `bool? Enabled`

                Whether this tool is enabled and available to Claude. Overrides the default_config setting.

              - `PermissionPolicy? PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                  - `required Type Type`

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

                  - `required Type Type`

              - `Type Type`

            - `class BetaManagedAgentsEditToolConfigParams:`

              Configuration override for the edit tool.

              - `JsonElement Name constant`

                Must be "edit".

              - `bool? Enabled`

                Whether this tool is enabled and available to Claude. Overrides the default_config setting.

              - `PermissionPolicy? PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `Type Type`

            - `class BetaManagedAgentsReadToolConfigParams:`

              Configuration override for the read tool.

              - `JsonElement Name constant`

                Must be "read".

              - `bool? Enabled`

                Whether this tool is enabled and available to Claude. Overrides the default_config setting.

              - `PermissionPolicy? PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `Type Type`

            - `class BetaManagedAgentsWriteToolConfigParams:`

              Configuration override for the write tool.

              - `JsonElement Name constant`

                Must be "write".

              - `bool? Enabled`

                Whether this tool is enabled and available to Claude. Overrides the default_config setting.

              - `PermissionPolicy? PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `Type Type`

            - `class BetaManagedAgentsGlobToolConfigParams:`

              Configuration override for the glob tool.

              - `JsonElement Name constant`

                Must be "glob".

              - `bool? Enabled`

                Whether this tool is enabled and available to Claude. Overrides the default_config setting.

              - `PermissionPolicy? PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `Type Type`

            - `class BetaManagedAgentsGrepToolConfigParams:`

              Configuration override for the grep tool.

              - `JsonElement Name constant`

                Must be "grep".

              - `bool? Enabled`

                Whether this tool is enabled and available to Claude. Overrides the default_config setting.

              - `PermissionPolicy? PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `Type Type`

            - `class BetaManagedAgentsWebFetchToolConfigParams:`

              Configuration override for the web_fetch tool.

              - `JsonElement Name constant`

                Must be "web_fetch".

              - `IReadOnlyList<string> AllowedDomains`

                Only fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

              - `IReadOnlyList<string> BlockedDomains`

                Never fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

              - `bool? Enabled`

                Whether this tool is enabled and available to Claude. Overrides the default_config setting.

              - `int? MaxContentTokens`

                Maximum number of tokens of fetched text content to include in context per call. Does not apply to binary content such as PDFs.

                format: int32

              - `PermissionPolicy? PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `Type Type`

            - `class BetaManagedAgentsWebSearchToolConfigParams:`

              Configuration override for the web_search tool.

              - `JsonElement Name constant`

                Must be "web_search".

              - `IReadOnlyList<string> AllowedDomains`

                Only return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

              - `IReadOnlyList<string> BlockedDomains`

                Never return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

              - `bool? Enabled`

                Whether this tool is enabled and available to Claude. Overrides the default_config setting.

              - `PermissionPolicy? PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `Type Type`

              - `BetaManagedAgentsUserLocation? UserLocation`

                Approximate user location for search result localization.

                - `JsonElement Type constant`

                  Location precision. Only "approximate" is supported.

                - `string? City`

                  City name.

                  minLength: 1, maxLength: 255

                - `string? Country`

                  Two-letter ISO 3166-1 country code, uppercase.

                - `string? Region`

                  Region or state name.

                  minLength: 1, maxLength: 255

                - `string? Timezone`

                  IANA timezone identifier, e.g. "America/Los_Angeles".

                  minLength: 1, maxLength: 255

          - `BetaManagedAgentsAgentToolsetDefaultConfigParams? DefaultConfig`

            Default configuration for all tools in a toolset.

            - `bool? Enabled`

              Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

            - `PermissionPolicy? PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

        - `class BetaManagedAgentsMcpToolsetParams:`

          Configuration for tools from an MCP server defined in `mcp_servers`.

          - `required string McpServerName`

            Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

            minLength: 1, maxLength: 255

          - `required Type Type`

          - `IReadOnlyList<BetaManagedAgentsMcpToolConfigParams> Configs`

            Per-tool configuration overrides.

            - `required string Name`

              Name of the MCP tool to configure. 1-128 characters.

              minLength: 1, maxLength: 128

            - `bool? Enabled`

              Whether this tool is enabled. Overrides the `default_config` setting.

            - `PermissionPolicy? PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `BetaManagedAgentsMcpToolsetDefaultConfigParams? DefaultConfig`

            Default configuration for all tools from an MCP server.

            - `bool? Enabled`

              Whether tools are enabled by default. Defaults to true if not specified.

            - `PermissionPolicy? PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

        - `class BetaManagedAgentsCustomToolParams:`

          A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

          - `required string Description`

            Description of what the tool does, shown to the agent to help it decide when to use the tool.

            minLength: 1

          - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

            JSON Schema for custom tool input parameters.

            - `JsonElement Type constant`

            - `IReadOnlyDictionary<string, JsonElement>? Properties`

            - `IReadOnlyList<string>? Required`

          - `required string Name`

            Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

            minLength: 1, maxLength: 128

          - `required Type Type`

      - `int Version`

        The specific `agent` version to use. Omit to use the latest version.

        format: int32

  - `required string environmentID`

    Body param: ID of the `environment` defining the container configuration for this session.

    minLength: 1, maxLength: 128

  - `BetaManagedAgentsBudgetLimit budget`

    Body param: A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

  - `IReadOnlyList<InitialEvent> initialEvents`

    Body param: Initial events to send to the `session` at creation, processed in order. Supports `user.message` and `user.define_outcome` events. Maximum 50 events.

    - `class BetaManagedAgentsUserMessageEventParams:`

      Parameters for sending a user message to the session.

      - `required IReadOnlyList<Content> Content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `required string Text`

            The text content.

            minLength: 1

          - `required Type Type`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

                minLength: 1

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `required Type Type`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

              - `required string Url`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

                minLength: 1

              - `required Type Type`

          - `required Type Type`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

                minLength: 1

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `required Type Type`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

                minLength: 1

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

              - `required Type Type`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

              - `required string Url`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

                minLength: 1

              - `required Type Type`

          - `required Type Type`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

          - `required Type Type`

      - `required Type Type`

    - `class BetaManagedAgentsUserDefineOutcomeEventParams:`

      Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

      - `required string Description`

        What the agent should produce. This is the task specification.

      - `required Rubric Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubricParams:`

          Rubric referenced by a file uploaded via the Files API.

          - `required string FileID`

            ID of the rubric file.

          - `required Type Type`

        - `class BetaManagedAgentsTextRubricParams:`

          Rubric content provided inline as text.

          - `required string Content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

            maxLength: 262144

          - `required Type Type`

      - `required Type Type`

      - `int? MaxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

  - `IReadOnlyDictionary<string, string> metadata`

    Body param: Arbitrary key-value metadata attached to the session. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `IReadOnlyList<Resource> resources`

    Body param: Resources (e.g. repositories, files) to mount into the session's container.

    - `class BetaManagedAgentsGitHubRepositoryResourceParams:`

      Mount a GitHub repository into the session's container.

      - `required string AuthorizationToken`

        GitHub authorization token used to clone the repository.

        minLength: 1, maxLength: 4096

      - `required Type Type`

      - `required string Url`

        Github URL of the repository

        minLength: 1, maxLength: 2048

      - `Checkout? Checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `required string Name`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `required Type Type`

        - `class BetaManagedAgentsCommitCheckout:`

          - `required string Sha`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `required Type Type`

      - `string? MountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

        minLength: 1, maxLength: 4096

    - `class BetaManagedAgentsFileResourceParams:`

      Mount a file uploaded via the Files API into the session.

      - `required string FileID`

        ID of a previously uploaded file.

        minLength: 1, maxLength: 128

      - `required Type Type`

      - `string? MountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

        minLength: 1, maxLength: 4096

    - `class BetaManagedAgentsMemoryStoreResourceParam:`

      Parameters for attaching a memory store to an agent session.

      - `required string MemoryStoreID`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `required Type Type`

      - `Access? Access`

        Access mode for an attached memory store.

        - `ReadWrite`

        - `ReadOnly`

      - `string? Instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

        maxLength: 4096

  - `string? title`

    Body param: Human-readable session title.

    maxLength: 500

  - `IReadOnlyList<string> vaultIds`

    Body param: Vault IDs for stored credentials the agent can use during the session.

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

### Returns

- `class BetaManagedAgentsSession:`

  A Managed Agents `session`.

  - `required string ID`

  - `required BetaManagedAgentsSessionAgent Agent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `required string ID`

    - `required string? Description`

    - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

      - `required string Name`

      - `required Type Type`

      - `required string Url`

    - `required BetaManagedAgentsModelConfig Model`

      Model identifier and configuration.

      - `required BetaManagedAgentsModel ID`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `ClaudeFable5_1`

          Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

        - `ClaudeSonnet5`

          High-performance model for coding and agents

        - `ClaudeFable5`

          Next generation of intelligence for the hardest knowledge work and coding problems

        - `ClaudeOpus5`

          Powerful intelligence for long-running agents and coding

        - `ClaudeOpus4_8`

          Powerful intelligence for long-running agents and coding

        - `ClaudeOpus4_7`

          Powerful intelligence for long-running agents and coding

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

      - `Effort Effort`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

        - `class BetaManagedAgentsEffortLow:`

          Low effort. Favors latency over reasoning depth.

          - `required Type Type`

        - `class BetaManagedAgentsEffortMedium:`

          Medium effort. Balances latency and reasoning depth.

          - `required Type Type`

        - `class BetaManagedAgentsEffortHigh:`

          High effort. Favors reasoning depth.

          - `required Type Type`

        - `class BetaManagedAgentsEffortXhigh:`

          Extra-high effort. Not all models accept this level.

          - `required Type Type`

        - `class BetaManagedAgentsEffortMax:`

          Maximum effort. Favors reasoning depth over latency.

          - `required Type Type`

      - `string InferenceGeo`

        Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

      - `Speed Speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `Standard`

        - `Fast`

    - `required BetaManagedAgentsSessionMultiagentCoordinator? Multiagent`

      Resolved coordinator topology with full agent definitions for each roster member.

      - `required IReadOnlyList<Agent> Agents`

        Full `agent` definitions the coordinator may spawn as session threads.

        - `class BetaManagedAgentsSessionThreadAgent:`

          Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

          - `required string ID`

          - `required string? Description`

          - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

            - `required string Name`

            - `required Type Type`

            - `required string Url`

          - `required BetaManagedAgentsModelConfig Model`

            Model identifier and configuration.

          - `required string Name`

          - `required IReadOnlyList<Skill> Skills`

            - `class BetaManagedAgentsAnthropicSkill:`

              A resolved Anthropic-managed skill.

              - `required string SkillID`

              - `required Type Type`

              - `required string Version`

            - `class BetaManagedAgentsCustomSkill:`

              A resolved user-created custom skill.

              - `required string SkillID`

              - `required Type Type`

              - `required string Version`

          - `required string? System`

          - `required IReadOnlyList<Tool> Tools`

            - `class BetaManagedAgentsAgentToolset20260401:`

              - `required IReadOnlyList<BetaManagedAgentsAgentToolConfig> Configs`

                - `class BetaManagedAgentsBashToolConfig:`

                  Configuration for the bash tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                      - `required Type Type`

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                      - `required Type Type`

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsEditToolConfig:`

                  Configuration for the edit tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsReadToolConfig:`

                  Configuration for the read tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsWriteToolConfig:`

                  Configuration for the write tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsGlobToolConfig:`

                  Configuration for the glob tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsGrepToolConfig:`

                  Configuration for the grep tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsWebFetchToolConfig:`

                  Configuration for the web_fetch tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                  - `IReadOnlyList<string> AllowedDomains`

                  - `IReadOnlyList<string> BlockedDomains`

                  - `int? MaxContentTokens`

                    format: int32

                - `class BetaManagedAgentsWebSearchToolConfig:`

                  Configuration for the web_search tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                  - `IReadOnlyList<string> AllowedDomains`

                  - `IReadOnlyList<string> BlockedDomains`

                  - `BetaManagedAgentsUserLocation? UserLocation`

                    Approximate user location for search result localization.

                    - `JsonElement Type constant`

                      Location precision. Only "approximate" is supported.

                    - `string? City`

                      City name.

                      minLength: 1, maxLength: 255

                    - `string? Country`

                      Two-letter ISO 3166-1 country code, uppercase.

                    - `string? Region`

                      Region or state name.

                      minLength: 1, maxLength: 255

                    - `string? Timezone`

                      IANA timezone identifier, e.g. "America/Los_Angeles".

                      minLength: 1, maxLength: 255

              - `required BetaManagedAgentsAgentToolsetDefaultConfig DefaultConfig`

                Resolved default configuration for agent tools.

                - `required bool Enabled`

                - `required PermissionPolicy PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy:`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy:`

                    Tool calls require user confirmation before execution.

              - `required Type Type`

            - `class BetaManagedAgentsMcpToolset:`

              - `required IReadOnlyList<BetaManagedAgentsMcpToolConfig> Configs`

                - `required bool Enabled`

                - `required string Name`

                - `required PermissionPolicy PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy:`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy:`

                    Tool calls require user confirmation before execution.

              - `required BetaManagedAgentsMcpToolsetDefaultConfig DefaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `required bool Enabled`

                - `required PermissionPolicy PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy:`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy:`

                    Tool calls require user confirmation before execution.

              - `required string McpServerName`

              - `required Type Type`

            - `class BetaManagedAgentsCustomTool:`

              A custom tool as returned in API responses.

              - `required string Description`

              - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

                JSON Schema for custom tool input parameters.

                - `JsonElement Type constant`

                - `IReadOnlyDictionary<string, JsonElement>? Properties`

                - `IReadOnlyList<string>? Required`

              - `required string Name`

              - `required Type Type`

          - `required Type Type`

          - `required int Version`

            format: int32

        - `class BetaManagedAgentsAdvisor:`

          Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

          - `required string Model`

            The advisor model id.

          - `required Type Type`

      - `required Type Type`

    - `required string Name`

    - `required IReadOnlyList<Skill> Skills`

      - `class BetaManagedAgentsAnthropicSkill:`

        A resolved Anthropic-managed skill.

      - `class BetaManagedAgentsCustomSkill:`

        A resolved user-created custom skill.

    - `required string? System`

    - `required IReadOnlyList<Tool> Tools`

      - `class BetaManagedAgentsAgentToolset20260401:`

      - `class BetaManagedAgentsMcpToolset:`

      - `class BetaManagedAgentsCustomTool:`

        A custom tool as returned in API responses.

    - `required Type Type`

    - `required int Version`

      format: int32

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required BetaManagedAgentsBudgetLimit? Budget`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `required BetaMonetaryAmount MaxListCost`

      A monetary amount in a specific currency.

      - `required string Amount`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `required BetaCurrency Currency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `required Type Type`

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string EnvironmentID`

  - `required IReadOnlyDictionary<string, string> Metadata`

  - `required IReadOnlyList<BetaManagedAgentsOutcomeEvaluationResource> OutcomeEvaluations`

    Per-outcome evaluation state. One entry per `define_outcome` event sent to the session.

    - `required DateTimeOffset? CompletedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string Description`

      What the agent should produce.

    - `required string? Explanation`

      Grader's verdict text from the most recent evaluation. For `satisfied`, explains why criteria are met; for `needs_revision` (intermediate), what's missing; for `failed`, why unrecoverable.

    - `required int Iteration`

      0-indexed revision cycle the outcome is currently on.

      format: int32

    - `required string OutcomeID`

      Server-generated outc_ ID for this outcome.

    - `required string Result`

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

    - `required Type Type`

  - `required IReadOnlyList<BetaManagedAgentsSessionResource> Resources`

    - `class BetaManagedAgentsGitHubRepositoryResource:`

      - `required string ID`

      - `required DateTimeOffset CreatedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required string MountPath`

      - `required Type Type`

      - `required DateTimeOffset UpdatedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required string Url`

      - `Checkout? Checkout`

        - `class BetaManagedAgentsBranchCheckout:`

          - `required string Name`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `required Type Type`

        - `class BetaManagedAgentsCommitCheckout:`

          - `required string Sha`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `required Type Type`

    - `class BetaManagedAgentsFileResource:`

      - `required string ID`

      - `required DateTimeOffset CreatedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required string FileID`

      - `required string MountPath`

      - `required Type Type`

      - `required DateTimeOffset UpdatedAt`

        A timestamp in RFC 3339 format

        format: date-time

    - `class BetaManagedAgentsMemoryStoreResource:`

      A memory store attached to an agent session.

      - `required string MemoryStoreID`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `required Type Type`

      - `Access? Access`

        Access mode for an attached memory store.

        - `ReadWrite`

        - `ReadOnly`

      - `string Description`

        Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

      - `string? Instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

        maxLength: 4096

      - `string? MountPath`

        Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

      - `string? Name`

        Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

  - `required BetaManagedAgentsSessionStats Stats`

    Timing statistics for a session.

    - `double ActiveSeconds`

      Cumulative time in seconds the session spent in `running` status. Excludes idle time.

      format: double

    - `double DurationSeconds`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

      format: double

  - `required Status Status`

    SessionStatus enum

    - `Rescheduling`

    - `Running`

    - `Idle`

    - `Terminated`

  - `required string? Title`

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required BetaManagedAgentsSessionUsage Usage`

    Cumulative token usage for a session across all turns.

    - `double ActiveSeconds`

      Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once, unlike `stats.active_seconds`, which sums each thread's own active time. This is the duration the session's runtime cost is priced on.

      format: double

    - `BetaManagedAgentsCacheCreationUsage CacheCreation`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `int Ephemeral1hInputTokens`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `int Ephemeral5mInputTokens`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `int CacheReadInputTokens`

      Total tokens read from prompt cache.

      format: int32

    - `int InputTokens`

      Total input tokens consumed across all turns.

      format: int32

    - `BetaMonetaryAmount? ListCost`

      A monetary amount in a specific currency.

    - `int OutputTokens`

      Total output tokens generated across all turns.

      format: int32

    - `BetaManagedAgentsServerToolUsage? ServerToolUse`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `int WebFetchRequests`

        Number of server-executed web fetch requests.

        format: int32

      - `int WebSearchRequests`

        Number of server-executed web search requests.

        format: int32

  - `required IReadOnlyList<string> VaultIds`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `string? DeploymentID`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Example

```csharp
SessionCreateParams parameters = new()
{
    Agent = "agent_011CZkYpogX7uDKUyvBTophP",
    EnvironmentID = "env_011CZkZ9X2dpNyB7HsEFoRfW",
};

var betaManagedAgentsSession = await client.Beta.Sessions.Create(parameters);

Console.WriteLine(betaManagedAgentsSession);
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

`SessionListPage Beta.Sessions.List(parameters, cancellationToken = default)`

**GET** `/v1/sessions`

List Sessions

### Parameters

- `SessionListParams parameters`

  - `string agentID`

    Query param: Filter sessions created with this agent ID.

  - `int agentVersion`

    Query param: Filter by agent version. Only applies when `agent_id` is also set.

    format: int32

  - `DateTimeOffset createdAtGt`

    Query param: Return sessions created after this time (exclusive).

    format: date-time

  - `DateTimeOffset createdAtGte`

    Query param: Return sessions created at or after this time (inclusive).

    format: date-time

  - `DateTimeOffset createdAtLt`

    Query param: Return sessions created before this time (exclusive).

    format: date-time

  - `DateTimeOffset createdAtLte`

    Query param: Return sessions created at or before this time (inclusive).

    format: date-time

  - `string deploymentID`

    Query param: Filter sessions created by this deployment ID.

  - `bool includeArchived`

    Query param: When true, includes archived sessions. Default: false (exclude archived).

  - `int limit`

    Query param: Maximum number of results to return.

    format: int32

  - `string memoryStoreID`

    Query param: Filter sessions whose resources contain a `memory_store` with this memory store ID.

  - `Order order`

    Query param: Sort direction for results, ordered by `created_at`. Defaults to `desc` (newest first).

    - `Asc`

    - `Desc`

  - `string page`

    Query param: Opaque pagination cursor from a previous response.

  - `IReadOnlyList<Status> statuses`

    Query param: Filter by session status. Repeat the parameter to match any of multiple statuses.

    - `Rescheduling`

    - `Running`

    - `Idle`

    - `Terminated`

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

### Returns

- `class BetaManagedAgentsSession:`

  A Managed Agents `session`.

  - `required string ID`

  - `required BetaManagedAgentsSessionAgent Agent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `required string ID`

    - `required string? Description`

    - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

      - `required string Name`

      - `required Type Type`

      - `required string Url`

    - `required BetaManagedAgentsModelConfig Model`

      Model identifier and configuration.

      - `required BetaManagedAgentsModel ID`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `ClaudeFable5_1`

          Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

        - `ClaudeSonnet5`

          High-performance model for coding and agents

        - `ClaudeFable5`

          Next generation of intelligence for the hardest knowledge work and coding problems

        - `ClaudeOpus5`

          Powerful intelligence for long-running agents and coding

        - `ClaudeOpus4_8`

          Powerful intelligence for long-running agents and coding

        - `ClaudeOpus4_7`

          Powerful intelligence for long-running agents and coding

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

      - `Effort Effort`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

        - `class BetaManagedAgentsEffortLow:`

          Low effort. Favors latency over reasoning depth.

          - `required Type Type`

        - `class BetaManagedAgentsEffortMedium:`

          Medium effort. Balances latency and reasoning depth.

          - `required Type Type`

        - `class BetaManagedAgentsEffortHigh:`

          High effort. Favors reasoning depth.

          - `required Type Type`

        - `class BetaManagedAgentsEffortXhigh:`

          Extra-high effort. Not all models accept this level.

          - `required Type Type`

        - `class BetaManagedAgentsEffortMax:`

          Maximum effort. Favors reasoning depth over latency.

          - `required Type Type`

      - `string InferenceGeo`

        Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

      - `Speed Speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `Standard`

        - `Fast`

    - `required BetaManagedAgentsSessionMultiagentCoordinator? Multiagent`

      Resolved coordinator topology with full agent definitions for each roster member.

      - `required IReadOnlyList<Agent> Agents`

        Full `agent` definitions the coordinator may spawn as session threads.

        - `class BetaManagedAgentsSessionThreadAgent:`

          Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

          - `required string ID`

          - `required string? Description`

          - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

            - `required string Name`

            - `required Type Type`

            - `required string Url`

          - `required BetaManagedAgentsModelConfig Model`

            Model identifier and configuration.

          - `required string Name`

          - `required IReadOnlyList<Skill> Skills`

            - `class BetaManagedAgentsAnthropicSkill:`

              A resolved Anthropic-managed skill.

              - `required string SkillID`

              - `required Type Type`

              - `required string Version`

            - `class BetaManagedAgentsCustomSkill:`

              A resolved user-created custom skill.

              - `required string SkillID`

              - `required Type Type`

              - `required string Version`

          - `required string? System`

          - `required IReadOnlyList<Tool> Tools`

            - `class BetaManagedAgentsAgentToolset20260401:`

              - `required IReadOnlyList<BetaManagedAgentsAgentToolConfig> Configs`

                - `class BetaManagedAgentsBashToolConfig:`

                  Configuration for the bash tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                      - `required Type Type`

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                      - `required Type Type`

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsEditToolConfig:`

                  Configuration for the edit tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsReadToolConfig:`

                  Configuration for the read tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsWriteToolConfig:`

                  Configuration for the write tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsGlobToolConfig:`

                  Configuration for the glob tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsGrepToolConfig:`

                  Configuration for the grep tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsWebFetchToolConfig:`

                  Configuration for the web_fetch tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                  - `IReadOnlyList<string> AllowedDomains`

                  - `IReadOnlyList<string> BlockedDomains`

                  - `int? MaxContentTokens`

                    format: int32

                - `class BetaManagedAgentsWebSearchToolConfig:`

                  Configuration for the web_search tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                  - `IReadOnlyList<string> AllowedDomains`

                  - `IReadOnlyList<string> BlockedDomains`

                  - `BetaManagedAgentsUserLocation? UserLocation`

                    Approximate user location for search result localization.

                    - `JsonElement Type constant`

                      Location precision. Only "approximate" is supported.

                    - `string? City`

                      City name.

                      minLength: 1, maxLength: 255

                    - `string? Country`

                      Two-letter ISO 3166-1 country code, uppercase.

                    - `string? Region`

                      Region or state name.

                      minLength: 1, maxLength: 255

                    - `string? Timezone`

                      IANA timezone identifier, e.g. "America/Los_Angeles".

                      minLength: 1, maxLength: 255

              - `required BetaManagedAgentsAgentToolsetDefaultConfig DefaultConfig`

                Resolved default configuration for agent tools.

                - `required bool Enabled`

                - `required PermissionPolicy PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy:`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy:`

                    Tool calls require user confirmation before execution.

              - `required Type Type`

            - `class BetaManagedAgentsMcpToolset:`

              - `required IReadOnlyList<BetaManagedAgentsMcpToolConfig> Configs`

                - `required bool Enabled`

                - `required string Name`

                - `required PermissionPolicy PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy:`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy:`

                    Tool calls require user confirmation before execution.

              - `required BetaManagedAgentsMcpToolsetDefaultConfig DefaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `required bool Enabled`

                - `required PermissionPolicy PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy:`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy:`

                    Tool calls require user confirmation before execution.

              - `required string McpServerName`

              - `required Type Type`

            - `class BetaManagedAgentsCustomTool:`

              A custom tool as returned in API responses.

              - `required string Description`

              - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

                JSON Schema for custom tool input parameters.

                - `JsonElement Type constant`

                - `IReadOnlyDictionary<string, JsonElement>? Properties`

                - `IReadOnlyList<string>? Required`

              - `required string Name`

              - `required Type Type`

          - `required Type Type`

          - `required int Version`

            format: int32

        - `class BetaManagedAgentsAdvisor:`

          Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

          - `required string Model`

            The advisor model id.

          - `required Type Type`

      - `required Type Type`

    - `required string Name`

    - `required IReadOnlyList<Skill> Skills`

      - `class BetaManagedAgentsAnthropicSkill:`

        A resolved Anthropic-managed skill.

      - `class BetaManagedAgentsCustomSkill:`

        A resolved user-created custom skill.

    - `required string? System`

    - `required IReadOnlyList<Tool> Tools`

      - `class BetaManagedAgentsAgentToolset20260401:`

      - `class BetaManagedAgentsMcpToolset:`

      - `class BetaManagedAgentsCustomTool:`

        A custom tool as returned in API responses.

    - `required Type Type`

    - `required int Version`

      format: int32

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required BetaManagedAgentsBudgetLimit? Budget`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `required BetaMonetaryAmount MaxListCost`

      A monetary amount in a specific currency.

      - `required string Amount`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `required BetaCurrency Currency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `required Type Type`

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string EnvironmentID`

  - `required IReadOnlyDictionary<string, string> Metadata`

  - `required IReadOnlyList<BetaManagedAgentsOutcomeEvaluationResource> OutcomeEvaluations`

    Per-outcome evaluation state. One entry per `define_outcome` event sent to the session.

    - `required DateTimeOffset? CompletedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string Description`

      What the agent should produce.

    - `required string? Explanation`

      Grader's verdict text from the most recent evaluation. For `satisfied`, explains why criteria are met; for `needs_revision` (intermediate), what's missing; for `failed`, why unrecoverable.

    - `required int Iteration`

      0-indexed revision cycle the outcome is currently on.

      format: int32

    - `required string OutcomeID`

      Server-generated outc_ ID for this outcome.

    - `required string Result`

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

    - `required Type Type`

  - `required IReadOnlyList<BetaManagedAgentsSessionResource> Resources`

    - `class BetaManagedAgentsGitHubRepositoryResource:`

      - `required string ID`

      - `required DateTimeOffset CreatedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required string MountPath`

      - `required Type Type`

      - `required DateTimeOffset UpdatedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required string Url`

      - `Checkout? Checkout`

        - `class BetaManagedAgentsBranchCheckout:`

          - `required string Name`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `required Type Type`

        - `class BetaManagedAgentsCommitCheckout:`

          - `required string Sha`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `required Type Type`

    - `class BetaManagedAgentsFileResource:`

      - `required string ID`

      - `required DateTimeOffset CreatedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required string FileID`

      - `required string MountPath`

      - `required Type Type`

      - `required DateTimeOffset UpdatedAt`

        A timestamp in RFC 3339 format

        format: date-time

    - `class BetaManagedAgentsMemoryStoreResource:`

      A memory store attached to an agent session.

      - `required string MemoryStoreID`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `required Type Type`

      - `Access? Access`

        Access mode for an attached memory store.

        - `ReadWrite`

        - `ReadOnly`

      - `string Description`

        Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

      - `string? Instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

        maxLength: 4096

      - `string? MountPath`

        Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

      - `string? Name`

        Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

  - `required BetaManagedAgentsSessionStats Stats`

    Timing statistics for a session.

    - `double ActiveSeconds`

      Cumulative time in seconds the session spent in `running` status. Excludes idle time.

      format: double

    - `double DurationSeconds`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

      format: double

  - `required Status Status`

    SessionStatus enum

    - `Rescheduling`

    - `Running`

    - `Idle`

    - `Terminated`

  - `required string? Title`

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required BetaManagedAgentsSessionUsage Usage`

    Cumulative token usage for a session across all turns.

    - `double ActiveSeconds`

      Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once, unlike `stats.active_seconds`, which sums each thread's own active time. This is the duration the session's runtime cost is priced on.

      format: double

    - `BetaManagedAgentsCacheCreationUsage CacheCreation`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `int Ephemeral1hInputTokens`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `int Ephemeral5mInputTokens`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `int CacheReadInputTokens`

      Total tokens read from prompt cache.

      format: int32

    - `int InputTokens`

      Total input tokens consumed across all turns.

      format: int32

    - `BetaMonetaryAmount? ListCost`

      A monetary amount in a specific currency.

    - `int OutputTokens`

      Total output tokens generated across all turns.

      format: int32

    - `BetaManagedAgentsServerToolUsage? ServerToolUse`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `int WebFetchRequests`

        Number of server-executed web fetch requests.

        format: int32

      - `int WebSearchRequests`

        Number of server-executed web search requests.

        format: int32

  - `required IReadOnlyList<string> VaultIds`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `string? DeploymentID`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Example

```csharp
SessionListParams parameters = new();

var page = await client.Beta.Sessions.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
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

`BetaManagedAgentsSession Beta.Sessions.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/sessions/{session_id}`

Get Session

### Parameters

- `SessionRetrieveParams parameters`

  - `required string sessionID`

    Path parameter session_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

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

### Returns

- `class BetaManagedAgentsSession:`

  A Managed Agents `session`.

  - `required string ID`

  - `required BetaManagedAgentsSessionAgent Agent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `required string ID`

    - `required string? Description`

    - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

      - `required string Name`

      - `required Type Type`

      - `required string Url`

    - `required BetaManagedAgentsModelConfig Model`

      Model identifier and configuration.

      - `required BetaManagedAgentsModel ID`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `ClaudeFable5_1`

          Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

        - `ClaudeSonnet5`

          High-performance model for coding and agents

        - `ClaudeFable5`

          Next generation of intelligence for the hardest knowledge work and coding problems

        - `ClaudeOpus5`

          Powerful intelligence for long-running agents and coding

        - `ClaudeOpus4_8`

          Powerful intelligence for long-running agents and coding

        - `ClaudeOpus4_7`

          Powerful intelligence for long-running agents and coding

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

      - `Effort Effort`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

        - `class BetaManagedAgentsEffortLow:`

          Low effort. Favors latency over reasoning depth.

          - `required Type Type`

        - `class BetaManagedAgentsEffortMedium:`

          Medium effort. Balances latency and reasoning depth.

          - `required Type Type`

        - `class BetaManagedAgentsEffortHigh:`

          High effort. Favors reasoning depth.

          - `required Type Type`

        - `class BetaManagedAgentsEffortXhigh:`

          Extra-high effort. Not all models accept this level.

          - `required Type Type`

        - `class BetaManagedAgentsEffortMax:`

          Maximum effort. Favors reasoning depth over latency.

          - `required Type Type`

      - `string InferenceGeo`

        Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

      - `Speed Speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `Standard`

        - `Fast`

    - `required BetaManagedAgentsSessionMultiagentCoordinator? Multiagent`

      Resolved coordinator topology with full agent definitions for each roster member.

      - `required IReadOnlyList<Agent> Agents`

        Full `agent` definitions the coordinator may spawn as session threads.

        - `class BetaManagedAgentsSessionThreadAgent:`

          Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

          - `required string ID`

          - `required string? Description`

          - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

            - `required string Name`

            - `required Type Type`

            - `required string Url`

          - `required BetaManagedAgentsModelConfig Model`

            Model identifier and configuration.

          - `required string Name`

          - `required IReadOnlyList<Skill> Skills`

            - `class BetaManagedAgentsAnthropicSkill:`

              A resolved Anthropic-managed skill.

              - `required string SkillID`

              - `required Type Type`

              - `required string Version`

            - `class BetaManagedAgentsCustomSkill:`

              A resolved user-created custom skill.

              - `required string SkillID`

              - `required Type Type`

              - `required string Version`

          - `required string? System`

          - `required IReadOnlyList<Tool> Tools`

            - `class BetaManagedAgentsAgentToolset20260401:`

              - `required IReadOnlyList<BetaManagedAgentsAgentToolConfig> Configs`

                - `class BetaManagedAgentsBashToolConfig:`

                  Configuration for the bash tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                      - `required Type Type`

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                      - `required Type Type`

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsEditToolConfig:`

                  Configuration for the edit tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsReadToolConfig:`

                  Configuration for the read tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsWriteToolConfig:`

                  Configuration for the write tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsGlobToolConfig:`

                  Configuration for the glob tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsGrepToolConfig:`

                  Configuration for the grep tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsWebFetchToolConfig:`

                  Configuration for the web_fetch tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                  - `IReadOnlyList<string> AllowedDomains`

                  - `IReadOnlyList<string> BlockedDomains`

                  - `int? MaxContentTokens`

                    format: int32

                - `class BetaManagedAgentsWebSearchToolConfig:`

                  Configuration for the web_search tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                  - `IReadOnlyList<string> AllowedDomains`

                  - `IReadOnlyList<string> BlockedDomains`

                  - `BetaManagedAgentsUserLocation? UserLocation`

                    Approximate user location for search result localization.

                    - `JsonElement Type constant`

                      Location precision. Only "approximate" is supported.

                    - `string? City`

                      City name.

                      minLength: 1, maxLength: 255

                    - `string? Country`

                      Two-letter ISO 3166-1 country code, uppercase.

                    - `string? Region`

                      Region or state name.

                      minLength: 1, maxLength: 255

                    - `string? Timezone`

                      IANA timezone identifier, e.g. "America/Los_Angeles".

                      minLength: 1, maxLength: 255

              - `required BetaManagedAgentsAgentToolsetDefaultConfig DefaultConfig`

                Resolved default configuration for agent tools.

                - `required bool Enabled`

                - `required PermissionPolicy PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy:`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy:`

                    Tool calls require user confirmation before execution.

              - `required Type Type`

            - `class BetaManagedAgentsMcpToolset:`

              - `required IReadOnlyList<BetaManagedAgentsMcpToolConfig> Configs`

                - `required bool Enabled`

                - `required string Name`

                - `required PermissionPolicy PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy:`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy:`

                    Tool calls require user confirmation before execution.

              - `required BetaManagedAgentsMcpToolsetDefaultConfig DefaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `required bool Enabled`

                - `required PermissionPolicy PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy:`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy:`

                    Tool calls require user confirmation before execution.

              - `required string McpServerName`

              - `required Type Type`

            - `class BetaManagedAgentsCustomTool:`

              A custom tool as returned in API responses.

              - `required string Description`

              - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

                JSON Schema for custom tool input parameters.

                - `JsonElement Type constant`

                - `IReadOnlyDictionary<string, JsonElement>? Properties`

                - `IReadOnlyList<string>? Required`

              - `required string Name`

              - `required Type Type`

          - `required Type Type`

          - `required int Version`

            format: int32

        - `class BetaManagedAgentsAdvisor:`

          Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

          - `required string Model`

            The advisor model id.

          - `required Type Type`

      - `required Type Type`

    - `required string Name`

    - `required IReadOnlyList<Skill> Skills`

      - `class BetaManagedAgentsAnthropicSkill:`

        A resolved Anthropic-managed skill.

      - `class BetaManagedAgentsCustomSkill:`

        A resolved user-created custom skill.

    - `required string? System`

    - `required IReadOnlyList<Tool> Tools`

      - `class BetaManagedAgentsAgentToolset20260401:`

      - `class BetaManagedAgentsMcpToolset:`

      - `class BetaManagedAgentsCustomTool:`

        A custom tool as returned in API responses.

    - `required Type Type`

    - `required int Version`

      format: int32

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required BetaManagedAgentsBudgetLimit? Budget`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `required BetaMonetaryAmount MaxListCost`

      A monetary amount in a specific currency.

      - `required string Amount`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `required BetaCurrency Currency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `required Type Type`

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string EnvironmentID`

  - `required IReadOnlyDictionary<string, string> Metadata`

  - `required IReadOnlyList<BetaManagedAgentsOutcomeEvaluationResource> OutcomeEvaluations`

    Per-outcome evaluation state. One entry per `define_outcome` event sent to the session.

    - `required DateTimeOffset? CompletedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string Description`

      What the agent should produce.

    - `required string? Explanation`

      Grader's verdict text from the most recent evaluation. For `satisfied`, explains why criteria are met; for `needs_revision` (intermediate), what's missing; for `failed`, why unrecoverable.

    - `required int Iteration`

      0-indexed revision cycle the outcome is currently on.

      format: int32

    - `required string OutcomeID`

      Server-generated outc_ ID for this outcome.

    - `required string Result`

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

    - `required Type Type`

  - `required IReadOnlyList<BetaManagedAgentsSessionResource> Resources`

    - `class BetaManagedAgentsGitHubRepositoryResource:`

      - `required string ID`

      - `required DateTimeOffset CreatedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required string MountPath`

      - `required Type Type`

      - `required DateTimeOffset UpdatedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required string Url`

      - `Checkout? Checkout`

        - `class BetaManagedAgentsBranchCheckout:`

          - `required string Name`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `required Type Type`

        - `class BetaManagedAgentsCommitCheckout:`

          - `required string Sha`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `required Type Type`

    - `class BetaManagedAgentsFileResource:`

      - `required string ID`

      - `required DateTimeOffset CreatedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required string FileID`

      - `required string MountPath`

      - `required Type Type`

      - `required DateTimeOffset UpdatedAt`

        A timestamp in RFC 3339 format

        format: date-time

    - `class BetaManagedAgentsMemoryStoreResource:`

      A memory store attached to an agent session.

      - `required string MemoryStoreID`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `required Type Type`

      - `Access? Access`

        Access mode for an attached memory store.

        - `ReadWrite`

        - `ReadOnly`

      - `string Description`

        Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

      - `string? Instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

        maxLength: 4096

      - `string? MountPath`

        Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

      - `string? Name`

        Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

  - `required BetaManagedAgentsSessionStats Stats`

    Timing statistics for a session.

    - `double ActiveSeconds`

      Cumulative time in seconds the session spent in `running` status. Excludes idle time.

      format: double

    - `double DurationSeconds`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

      format: double

  - `required Status Status`

    SessionStatus enum

    - `Rescheduling`

    - `Running`

    - `Idle`

    - `Terminated`

  - `required string? Title`

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required BetaManagedAgentsSessionUsage Usage`

    Cumulative token usage for a session across all turns.

    - `double ActiveSeconds`

      Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once, unlike `stats.active_seconds`, which sums each thread's own active time. This is the duration the session's runtime cost is priced on.

      format: double

    - `BetaManagedAgentsCacheCreationUsage CacheCreation`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `int Ephemeral1hInputTokens`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `int Ephemeral5mInputTokens`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `int CacheReadInputTokens`

      Total tokens read from prompt cache.

      format: int32

    - `int InputTokens`

      Total input tokens consumed across all turns.

      format: int32

    - `BetaMonetaryAmount? ListCost`

      A monetary amount in a specific currency.

    - `int OutputTokens`

      Total output tokens generated across all turns.

      format: int32

    - `BetaManagedAgentsServerToolUsage? ServerToolUse`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `int WebFetchRequests`

        Number of server-executed web fetch requests.

        format: int32

      - `int WebSearchRequests`

        Number of server-executed web search requests.

        format: int32

  - `required IReadOnlyList<string> VaultIds`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `string? DeploymentID`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Example

```csharp
SessionRetrieveParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7"
};

var betaManagedAgentsSession = await client.Beta.Sessions.Retrieve(parameters);

Console.WriteLine(betaManagedAgentsSession);
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

`BetaManagedAgentsSession Beta.Sessions.Update(parameters, cancellationToken = default)`

**POST** `/v1/sessions/{session_id}`

Update Session

### Parameters

- `SessionUpdateParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `BetaManagedAgentsSessionAgentUpdate agent`

    Body param: Mid-session agent configuration update. Only `tools` and `mcp_servers` are updatable. Full replacement: the provided array becomes the new value. To preserve existing entries, GET the session, modify the array, and POST it back.

  - `BetaManagedAgentsBudgetLimit? budget`

    Body param: A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

  - `IReadOnlyDictionary<string, string>? metadata`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve.

  - `string? title`

    Body param: Human-readable session title.

    minLength: 1, maxLength: 500

  - `IReadOnlyList<string> vaultIds`

    Body param: Vault IDs (`vlt_*`) to attach to the session. Not yet supported; requests setting this field are rejected. Reserved for future use.

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

### Returns

- `class BetaManagedAgentsSession:`

  A Managed Agents `session`.

  - `required string ID`

  - `required BetaManagedAgentsSessionAgent Agent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `required string ID`

    - `required string? Description`

    - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

      - `required string Name`

      - `required Type Type`

      - `required string Url`

    - `required BetaManagedAgentsModelConfig Model`

      Model identifier and configuration.

      - `required BetaManagedAgentsModel ID`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `ClaudeFable5_1`

          Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

        - `ClaudeSonnet5`

          High-performance model for coding and agents

        - `ClaudeFable5`

          Next generation of intelligence for the hardest knowledge work and coding problems

        - `ClaudeOpus5`

          Powerful intelligence for long-running agents and coding

        - `ClaudeOpus4_8`

          Powerful intelligence for long-running agents and coding

        - `ClaudeOpus4_7`

          Powerful intelligence for long-running agents and coding

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

      - `Effort Effort`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

        - `class BetaManagedAgentsEffortLow:`

          Low effort. Favors latency over reasoning depth.

          - `required Type Type`

        - `class BetaManagedAgentsEffortMedium:`

          Medium effort. Balances latency and reasoning depth.

          - `required Type Type`

        - `class BetaManagedAgentsEffortHigh:`

          High effort. Favors reasoning depth.

          - `required Type Type`

        - `class BetaManagedAgentsEffortXhigh:`

          Extra-high effort. Not all models accept this level.

          - `required Type Type`

        - `class BetaManagedAgentsEffortMax:`

          Maximum effort. Favors reasoning depth over latency.

          - `required Type Type`

      - `string InferenceGeo`

        Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

      - `Speed Speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `Standard`

        - `Fast`

    - `required BetaManagedAgentsSessionMultiagentCoordinator? Multiagent`

      Resolved coordinator topology with full agent definitions for each roster member.

      - `required IReadOnlyList<Agent> Agents`

        Full `agent` definitions the coordinator may spawn as session threads.

        - `class BetaManagedAgentsSessionThreadAgent:`

          Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

          - `required string ID`

          - `required string? Description`

          - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

            - `required string Name`

            - `required Type Type`

            - `required string Url`

          - `required BetaManagedAgentsModelConfig Model`

            Model identifier and configuration.

          - `required string Name`

          - `required IReadOnlyList<Skill> Skills`

            - `class BetaManagedAgentsAnthropicSkill:`

              A resolved Anthropic-managed skill.

              - `required string SkillID`

              - `required Type Type`

              - `required string Version`

            - `class BetaManagedAgentsCustomSkill:`

              A resolved user-created custom skill.

              - `required string SkillID`

              - `required Type Type`

              - `required string Version`

          - `required string? System`

          - `required IReadOnlyList<Tool> Tools`

            - `class BetaManagedAgentsAgentToolset20260401:`

              - `required IReadOnlyList<BetaManagedAgentsAgentToolConfig> Configs`

                - `class BetaManagedAgentsBashToolConfig:`

                  Configuration for the bash tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                      - `required Type Type`

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                      - `required Type Type`

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsEditToolConfig:`

                  Configuration for the edit tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsReadToolConfig:`

                  Configuration for the read tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsWriteToolConfig:`

                  Configuration for the write tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsGlobToolConfig:`

                  Configuration for the glob tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsGrepToolConfig:`

                  Configuration for the grep tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsWebFetchToolConfig:`

                  Configuration for the web_fetch tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                  - `IReadOnlyList<string> AllowedDomains`

                  - `IReadOnlyList<string> BlockedDomains`

                  - `int? MaxContentTokens`

                    format: int32

                - `class BetaManagedAgentsWebSearchToolConfig:`

                  Configuration for the web_search tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                  - `IReadOnlyList<string> AllowedDomains`

                  - `IReadOnlyList<string> BlockedDomains`

                  - `BetaManagedAgentsUserLocation? UserLocation`

                    Approximate user location for search result localization.

                    - `JsonElement Type constant`

                      Location precision. Only "approximate" is supported.

                    - `string? City`

                      City name.

                      minLength: 1, maxLength: 255

                    - `string? Country`

                      Two-letter ISO 3166-1 country code, uppercase.

                    - `string? Region`

                      Region or state name.

                      minLength: 1, maxLength: 255

                    - `string? Timezone`

                      IANA timezone identifier, e.g. "America/Los_Angeles".

                      minLength: 1, maxLength: 255

              - `required BetaManagedAgentsAgentToolsetDefaultConfig DefaultConfig`

                Resolved default configuration for agent tools.

                - `required bool Enabled`

                - `required PermissionPolicy PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy:`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy:`

                    Tool calls require user confirmation before execution.

              - `required Type Type`

            - `class BetaManagedAgentsMcpToolset:`

              - `required IReadOnlyList<BetaManagedAgentsMcpToolConfig> Configs`

                - `required bool Enabled`

                - `required string Name`

                - `required PermissionPolicy PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy:`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy:`

                    Tool calls require user confirmation before execution.

              - `required BetaManagedAgentsMcpToolsetDefaultConfig DefaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `required bool Enabled`

                - `required PermissionPolicy PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy:`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy:`

                    Tool calls require user confirmation before execution.

              - `required string McpServerName`

              - `required Type Type`

            - `class BetaManagedAgentsCustomTool:`

              A custom tool as returned in API responses.

              - `required string Description`

              - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

                JSON Schema for custom tool input parameters.

                - `JsonElement Type constant`

                - `IReadOnlyDictionary<string, JsonElement>? Properties`

                - `IReadOnlyList<string>? Required`

              - `required string Name`

              - `required Type Type`

          - `required Type Type`

          - `required int Version`

            format: int32

        - `class BetaManagedAgentsAdvisor:`

          Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

          - `required string Model`

            The advisor model id.

          - `required Type Type`

      - `required Type Type`

    - `required string Name`

    - `required IReadOnlyList<Skill> Skills`

      - `class BetaManagedAgentsAnthropicSkill:`

        A resolved Anthropic-managed skill.

      - `class BetaManagedAgentsCustomSkill:`

        A resolved user-created custom skill.

    - `required string? System`

    - `required IReadOnlyList<Tool> Tools`

      - `class BetaManagedAgentsAgentToolset20260401:`

      - `class BetaManagedAgentsMcpToolset:`

      - `class BetaManagedAgentsCustomTool:`

        A custom tool as returned in API responses.

    - `required Type Type`

    - `required int Version`

      format: int32

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required BetaManagedAgentsBudgetLimit? Budget`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `required BetaMonetaryAmount MaxListCost`

      A monetary amount in a specific currency.

      - `required string Amount`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `required BetaCurrency Currency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `required Type Type`

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string EnvironmentID`

  - `required IReadOnlyDictionary<string, string> Metadata`

  - `required IReadOnlyList<BetaManagedAgentsOutcomeEvaluationResource> OutcomeEvaluations`

    Per-outcome evaluation state. One entry per `define_outcome` event sent to the session.

    - `required DateTimeOffset? CompletedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string Description`

      What the agent should produce.

    - `required string? Explanation`

      Grader's verdict text from the most recent evaluation. For `satisfied`, explains why criteria are met; for `needs_revision` (intermediate), what's missing; for `failed`, why unrecoverable.

    - `required int Iteration`

      0-indexed revision cycle the outcome is currently on.

      format: int32

    - `required string OutcomeID`

      Server-generated outc_ ID for this outcome.

    - `required string Result`

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

    - `required Type Type`

  - `required IReadOnlyList<BetaManagedAgentsSessionResource> Resources`

    - `class BetaManagedAgentsGitHubRepositoryResource:`

      - `required string ID`

      - `required DateTimeOffset CreatedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required string MountPath`

      - `required Type Type`

      - `required DateTimeOffset UpdatedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required string Url`

      - `Checkout? Checkout`

        - `class BetaManagedAgentsBranchCheckout:`

          - `required string Name`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `required Type Type`

        - `class BetaManagedAgentsCommitCheckout:`

          - `required string Sha`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `required Type Type`

    - `class BetaManagedAgentsFileResource:`

      - `required string ID`

      - `required DateTimeOffset CreatedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required string FileID`

      - `required string MountPath`

      - `required Type Type`

      - `required DateTimeOffset UpdatedAt`

        A timestamp in RFC 3339 format

        format: date-time

    - `class BetaManagedAgentsMemoryStoreResource:`

      A memory store attached to an agent session.

      - `required string MemoryStoreID`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `required Type Type`

      - `Access? Access`

        Access mode for an attached memory store.

        - `ReadWrite`

        - `ReadOnly`

      - `string Description`

        Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

      - `string? Instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

        maxLength: 4096

      - `string? MountPath`

        Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

      - `string? Name`

        Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

  - `required BetaManagedAgentsSessionStats Stats`

    Timing statistics for a session.

    - `double ActiveSeconds`

      Cumulative time in seconds the session spent in `running` status. Excludes idle time.

      format: double

    - `double DurationSeconds`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

      format: double

  - `required Status Status`

    SessionStatus enum

    - `Rescheduling`

    - `Running`

    - `Idle`

    - `Terminated`

  - `required string? Title`

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required BetaManagedAgentsSessionUsage Usage`

    Cumulative token usage for a session across all turns.

    - `double ActiveSeconds`

      Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once, unlike `stats.active_seconds`, which sums each thread's own active time. This is the duration the session's runtime cost is priced on.

      format: double

    - `BetaManagedAgentsCacheCreationUsage CacheCreation`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `int Ephemeral1hInputTokens`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `int Ephemeral5mInputTokens`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `int CacheReadInputTokens`

      Total tokens read from prompt cache.

      format: int32

    - `int InputTokens`

      Total input tokens consumed across all turns.

      format: int32

    - `BetaMonetaryAmount? ListCost`

      A monetary amount in a specific currency.

    - `int OutputTokens`

      Total output tokens generated across all turns.

      format: int32

    - `BetaManagedAgentsServerToolUsage? ServerToolUse`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `int WebFetchRequests`

        Number of server-executed web fetch requests.

        format: int32

      - `int WebSearchRequests`

        Number of server-executed web search requests.

        format: int32

  - `required IReadOnlyList<string> VaultIds`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `string? DeploymentID`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Example

```csharp
SessionUpdateParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7"
};

var betaManagedAgentsSession = await client.Beta.Sessions.Update(parameters);

Console.WriteLine(betaManagedAgentsSession);
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

`BetaManagedAgentsDeletedSession Beta.Sessions.Delete(parameters, cancellationToken = default)`

**DELETE** `/v1/sessions/{session_id}`

Delete Session

### Parameters

- `SessionDeleteParams parameters`

  - `required string sessionID`

    Path parameter session_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

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

### Returns

- `class BetaManagedAgentsDeletedSession:`

  Confirmation that a `session` has been permanently deleted.

  - `required string ID`

  - `required Type Type`

### Example

```csharp
SessionDeleteParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7"
};

var betaManagedAgentsDeletedSession = await client.Beta.Sessions.Delete(parameters);

Console.WriteLine(betaManagedAgentsDeletedSession);
```

#### Response (200)

```json
{
  "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "type": "session_deleted"
}
```

## Archive Session

`BetaManagedAgentsSession Beta.Sessions.Archive(parameters, cancellationToken = default)`

**POST** `/v1/sessions/{session_id}/archive`

Archive Session

### Parameters

- `SessionArchiveParams parameters`

  - `required string sessionID`

    Path parameter session_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

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

### Returns

- `class BetaManagedAgentsSession:`

  A Managed Agents `session`.

  - `required string ID`

  - `required BetaManagedAgentsSessionAgent Agent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `required string ID`

    - `required string? Description`

    - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

      - `required string Name`

      - `required Type Type`

      - `required string Url`

    - `required BetaManagedAgentsModelConfig Model`

      Model identifier and configuration.

      - `required BetaManagedAgentsModel ID`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `ClaudeFable5_1`

          Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

        - `ClaudeSonnet5`

          High-performance model for coding and agents

        - `ClaudeFable5`

          Next generation of intelligence for the hardest knowledge work and coding problems

        - `ClaudeOpus5`

          Powerful intelligence for long-running agents and coding

        - `ClaudeOpus4_8`

          Powerful intelligence for long-running agents and coding

        - `ClaudeOpus4_7`

          Powerful intelligence for long-running agents and coding

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

      - `Effort Effort`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

        - `class BetaManagedAgentsEffortLow:`

          Low effort. Favors latency over reasoning depth.

          - `required Type Type`

        - `class BetaManagedAgentsEffortMedium:`

          Medium effort. Balances latency and reasoning depth.

          - `required Type Type`

        - `class BetaManagedAgentsEffortHigh:`

          High effort. Favors reasoning depth.

          - `required Type Type`

        - `class BetaManagedAgentsEffortXhigh:`

          Extra-high effort. Not all models accept this level.

          - `required Type Type`

        - `class BetaManagedAgentsEffortMax:`

          Maximum effort. Favors reasoning depth over latency.

          - `required Type Type`

      - `string InferenceGeo`

        Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

      - `Speed Speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `Standard`

        - `Fast`

    - `required BetaManagedAgentsSessionMultiagentCoordinator? Multiagent`

      Resolved coordinator topology with full agent definitions for each roster member.

      - `required IReadOnlyList<Agent> Agents`

        Full `agent` definitions the coordinator may spawn as session threads.

        - `class BetaManagedAgentsSessionThreadAgent:`

          Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

          - `required string ID`

          - `required string? Description`

          - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

            - `required string Name`

            - `required Type Type`

            - `required string Url`

          - `required BetaManagedAgentsModelConfig Model`

            Model identifier and configuration.

          - `required string Name`

          - `required IReadOnlyList<Skill> Skills`

            - `class BetaManagedAgentsAnthropicSkill:`

              A resolved Anthropic-managed skill.

              - `required string SkillID`

              - `required Type Type`

              - `required string Version`

            - `class BetaManagedAgentsCustomSkill:`

              A resolved user-created custom skill.

              - `required string SkillID`

              - `required Type Type`

              - `required string Version`

          - `required string? System`

          - `required IReadOnlyList<Tool> Tools`

            - `class BetaManagedAgentsAgentToolset20260401:`

              - `required IReadOnlyList<BetaManagedAgentsAgentToolConfig> Configs`

                - `class BetaManagedAgentsBashToolConfig:`

                  Configuration for the bash tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                      - `required Type Type`

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                      - `required Type Type`

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsEditToolConfig:`

                  Configuration for the edit tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsReadToolConfig:`

                  Configuration for the read tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsWriteToolConfig:`

                  Configuration for the write tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsGlobToolConfig:`

                  Configuration for the glob tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsGrepToolConfig:`

                  Configuration for the grep tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsWebFetchToolConfig:`

                  Configuration for the web_fetch tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                  - `IReadOnlyList<string> AllowedDomains`

                  - `IReadOnlyList<string> BlockedDomains`

                  - `int? MaxContentTokens`

                    format: int32

                - `class BetaManagedAgentsWebSearchToolConfig:`

                  Configuration for the web_search tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                  - `IReadOnlyList<string> AllowedDomains`

                  - `IReadOnlyList<string> BlockedDomains`

                  - `BetaManagedAgentsUserLocation? UserLocation`

                    Approximate user location for search result localization.

                    - `JsonElement Type constant`

                      Location precision. Only "approximate" is supported.

                    - `string? City`

                      City name.

                      minLength: 1, maxLength: 255

                    - `string? Country`

                      Two-letter ISO 3166-1 country code, uppercase.

                    - `string? Region`

                      Region or state name.

                      minLength: 1, maxLength: 255

                    - `string? Timezone`

                      IANA timezone identifier, e.g. "America/Los_Angeles".

                      minLength: 1, maxLength: 255

              - `required BetaManagedAgentsAgentToolsetDefaultConfig DefaultConfig`

                Resolved default configuration for agent tools.

                - `required bool Enabled`

                - `required PermissionPolicy PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy:`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy:`

                    Tool calls require user confirmation before execution.

              - `required Type Type`

            - `class BetaManagedAgentsMcpToolset:`

              - `required IReadOnlyList<BetaManagedAgentsMcpToolConfig> Configs`

                - `required bool Enabled`

                - `required string Name`

                - `required PermissionPolicy PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy:`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy:`

                    Tool calls require user confirmation before execution.

              - `required BetaManagedAgentsMcpToolsetDefaultConfig DefaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `required bool Enabled`

                - `required PermissionPolicy PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy:`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy:`

                    Tool calls require user confirmation before execution.

              - `required string McpServerName`

              - `required Type Type`

            - `class BetaManagedAgentsCustomTool:`

              A custom tool as returned in API responses.

              - `required string Description`

              - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

                JSON Schema for custom tool input parameters.

                - `JsonElement Type constant`

                - `IReadOnlyDictionary<string, JsonElement>? Properties`

                - `IReadOnlyList<string>? Required`

              - `required string Name`

              - `required Type Type`

          - `required Type Type`

          - `required int Version`

            format: int32

        - `class BetaManagedAgentsAdvisor:`

          Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

          - `required string Model`

            The advisor model id.

          - `required Type Type`

      - `required Type Type`

    - `required string Name`

    - `required IReadOnlyList<Skill> Skills`

      - `class BetaManagedAgentsAnthropicSkill:`

        A resolved Anthropic-managed skill.

      - `class BetaManagedAgentsCustomSkill:`

        A resolved user-created custom skill.

    - `required string? System`

    - `required IReadOnlyList<Tool> Tools`

      - `class BetaManagedAgentsAgentToolset20260401:`

      - `class BetaManagedAgentsMcpToolset:`

      - `class BetaManagedAgentsCustomTool:`

        A custom tool as returned in API responses.

    - `required Type Type`

    - `required int Version`

      format: int32

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required BetaManagedAgentsBudgetLimit? Budget`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `required BetaMonetaryAmount MaxListCost`

      A monetary amount in a specific currency.

      - `required string Amount`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `required BetaCurrency Currency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `required Type Type`

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string EnvironmentID`

  - `required IReadOnlyDictionary<string, string> Metadata`

  - `required IReadOnlyList<BetaManagedAgentsOutcomeEvaluationResource> OutcomeEvaluations`

    Per-outcome evaluation state. One entry per `define_outcome` event sent to the session.

    - `required DateTimeOffset? CompletedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string Description`

      What the agent should produce.

    - `required string? Explanation`

      Grader's verdict text from the most recent evaluation. For `satisfied`, explains why criteria are met; for `needs_revision` (intermediate), what's missing; for `failed`, why unrecoverable.

    - `required int Iteration`

      0-indexed revision cycle the outcome is currently on.

      format: int32

    - `required string OutcomeID`

      Server-generated outc_ ID for this outcome.

    - `required string Result`

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

    - `required Type Type`

  - `required IReadOnlyList<BetaManagedAgentsSessionResource> Resources`

    - `class BetaManagedAgentsGitHubRepositoryResource:`

      - `required string ID`

      - `required DateTimeOffset CreatedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required string MountPath`

      - `required Type Type`

      - `required DateTimeOffset UpdatedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required string Url`

      - `Checkout? Checkout`

        - `class BetaManagedAgentsBranchCheckout:`

          - `required string Name`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `required Type Type`

        - `class BetaManagedAgentsCommitCheckout:`

          - `required string Sha`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `required Type Type`

    - `class BetaManagedAgentsFileResource:`

      - `required string ID`

      - `required DateTimeOffset CreatedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required string FileID`

      - `required string MountPath`

      - `required Type Type`

      - `required DateTimeOffset UpdatedAt`

        A timestamp in RFC 3339 format

        format: date-time

    - `class BetaManagedAgentsMemoryStoreResource:`

      A memory store attached to an agent session.

      - `required string MemoryStoreID`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `required Type Type`

      - `Access? Access`

        Access mode for an attached memory store.

        - `ReadWrite`

        - `ReadOnly`

      - `string Description`

        Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

      - `string? Instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

        maxLength: 4096

      - `string? MountPath`

        Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

      - `string? Name`

        Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

  - `required BetaManagedAgentsSessionStats Stats`

    Timing statistics for a session.

    - `double ActiveSeconds`

      Cumulative time in seconds the session spent in `running` status. Excludes idle time.

      format: double

    - `double DurationSeconds`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

      format: double

  - `required Status Status`

    SessionStatus enum

    - `Rescheduling`

    - `Running`

    - `Idle`

    - `Terminated`

  - `required string? Title`

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required BetaManagedAgentsSessionUsage Usage`

    Cumulative token usage for a session across all turns.

    - `double ActiveSeconds`

      Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once, unlike `stats.active_seconds`, which sums each thread's own active time. This is the duration the session's runtime cost is priced on.

      format: double

    - `BetaManagedAgentsCacheCreationUsage CacheCreation`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `int Ephemeral1hInputTokens`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `int Ephemeral5mInputTokens`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `int CacheReadInputTokens`

      Total tokens read from prompt cache.

      format: int32

    - `int InputTokens`

      Total input tokens consumed across all turns.

      format: int32

    - `BetaMonetaryAmount? ListCost`

      A monetary amount in a specific currency.

    - `int OutputTokens`

      Total output tokens generated across all turns.

      format: int32

    - `BetaManagedAgentsServerToolUsage? ServerToolUse`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `int WebFetchRequests`

        Number of server-executed web fetch requests.

        format: int32

      - `int WebSearchRequests`

        Number of server-executed web search requests.

        format: int32

  - `required IReadOnlyList<string> VaultIds`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `string? DeploymentID`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Example

```csharp
SessionArchiveParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7"
};

var betaManagedAgentsSession = await client.Beta.Sessions.Archive(parameters);

Console.WriteLine(betaManagedAgentsSession);
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

- `class BetaManagedAgentsAdvisorParams:`

  Platform advisor roster entry: a model the session's primary thread may consult mid-turn. At most one per roster; the entry occupies the roster name `anthropic.advisor`.

  - `required string Model`

    A Claude model id. The model must be permitted as an advisor for this agent's model — see the sessions/threads/advisor spec.

    minLength: 1, maxLength: 256

  - `required Type Type`

### Beta Managed Agents Agent Message Preview

- `class BetaManagedAgentsAgentMessagePreview:`

  - `required string ID`

    The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

  - `required Type Type`

### Beta Managed Agents Agent Params

- `class BetaManagedAgentsAgentParams:`

  Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

  - `required string ID`

    The `agent` ID.

    minLength: 1, maxLength: 128

  - `required Type Type`

  - `int Version`

    The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

    format: int32

### Beta Managed Agents Agent Thinking Preview

- `class BetaManagedAgentsAgentThinkingPreview:`

  - `required string ID`

    The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

  - `required Type Type`

### Beta Managed Agents Agent With Overrides Params

- `class BetaManagedAgentsAgentWithOverridesParams:`

  Reference to an `agent` plus optional configuration overrides. Each provided field replaces the agent's value for the caller's use; the agent resource is unchanged.

  - `required string ID`

    The `agent` ID.

    minLength: 1, maxLength: 128

  - `required Type Type`

  - `IReadOnlyList<BetaManagedAgentsUrlMcpServerParams> McpServers`

    Replacement MCP server list. Full replacement: the provided array becomes the MCP servers. Send an empty array to clear; omit to preserve the agent's servers.

    - `required string Name`

      Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

      minLength: 1, maxLength: 255

    - `required Type Type`

    - `required string Url`

      Endpoint URL for the MCP server.

      maxLength: 2048

  - `Model Model`

    Replacement model. Accepts the model string, e.g. `claude-opus-5`, or a `model_config` object. Omit to use the agent's model.

    - `enum BetaManagedAgentsModel:`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `ClaudeFable5_1`

        Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

      - `ClaudeSonnet5`

        High-performance model for coding and agents

      - `ClaudeFable5`

        Next generation of intelligence for the hardest knowledge work and coding problems

      - `ClaudeOpus5`

        Powerful intelligence for long-running agents and coding

      - `ClaudeOpus4_8`

        Powerful intelligence for long-running agents and coding

      - `ClaudeOpus4_7`

        Powerful intelligence for long-running agents and coding

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

    - `class BetaManagedAgentsModelConfigParams:`

      An object that defines additional configuration control over model use

      - `required BetaManagedAgentsModel ID`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `ClaudeFable5_1`

          Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

        - `ClaudeSonnet5`

          High-performance model for coding and agents

        - `ClaudeFable5`

          Next generation of intelligence for the hardest knowledge work and coding problems

        - `ClaudeOpus5`

          Powerful intelligence for long-running agents and coding

        - `ClaudeOpus4_8`

          Powerful intelligence for long-running agents and coding

        - `ClaudeOpus4_7`

          Powerful intelligence for long-running agents and coding

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

      - `Effort? Effort`

        How hard Claude works on each inference call. Accepts a bare level string (`"high"`) or `{"type": "high"}`. On create, omitting it resolves the per-model default; on update, omitting it leaves the stored value unchanged.

        - `enum BetaManagedAgentsEffortLevel:`

          How hard Claude works on each turn. Higher levels favor reasoning depth over latency. Not all models accept every level; invalid combinations are rejected at create time.

          - `Low`

          - `Medium`

          - `High`

          - `Xhigh`

          - `Max`

        - `class BetaManagedAgentsEffortLow:`

          Low effort. Favors latency over reasoning depth.

          - `required Type Type`

        - `class BetaManagedAgentsEffortMedium:`

          Medium effort. Balances latency and reasoning depth.

          - `required Type Type`

        - `class BetaManagedAgentsEffortHigh:`

          High effort. Favors reasoning depth.

          - `required Type Type`

        - `class BetaManagedAgentsEffortXhigh:`

          Extra-high effort. Not all models accept this level.

          - `required Type Type`

        - `class BetaManagedAgentsEffortMax:`

          Maximum effort. Favors reasoning depth over latency.

          - `required Type Type`

      - `string? InferenceGeo`

        Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo. On update, `model` is whole-object replacement — omitting inference_geo clears it.

      - `Speed? Speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `Standard`

        - `Fast`

  - `IReadOnlyList<BetaManagedAgentsSkillParams> Skills`

    Replacement skill list. Full replacement: the provided array becomes the skills. Send an empty array to clear; omit to preserve the agent's skills.

    - `class BetaManagedAgentsAnthropicSkillParams:`

      An Anthropic-managed skill.

      - `required string SkillID`

        Identifier of the Anthropic skill (e.g., "xlsx").

        minLength: 1, maxLength: 64

      - `required Type Type`

      - `string? Version`

        Version to pin. Defaults to latest if omitted.

        minLength: 1, maxLength: 64

    - `class BetaManagedAgentsCustomSkillParams:`

      A user-created custom skill.

      - `required string SkillID`

        Tagged ID of the custom skill (e.g., "skill_01XJ5...").

        minLength: 1, maxLength: 64

      - `required Type Type`

      - `string? Version`

        Version to pin. Defaults to latest if omitted.

        minLength: 1, maxLength: 64

  - `string? System`

    Replacement system prompt. Up to 100,000 characters. Set to null to clear the agent's system prompt; omit to preserve it.

    maxLength: 100000

  - `IReadOnlyList<Tool> Tools`

    Replacement tool list. Full replacement: the provided array becomes the tool configuration. Send an empty array to clear; omit to preserve the agent's tools.

    - `class BetaManagedAgentsAgentToolset20260401Params:`

      Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

      - `required Type Type`

      - `IReadOnlyList<BetaManagedAgentsAgentToolConfigParams> Configs`

        Per-tool configuration overrides.

        - `class BetaManagedAgentsBashToolConfigParams:`

          Configuration override for the bash tool.

          - `JsonElement Name constant`

            Must be "bash".

          - `bool? Enabled`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy? PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

              - `required Type Type`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `required Type Type`

          - `Type Type`

        - `class BetaManagedAgentsEditToolConfigParams:`

          Configuration override for the edit tool.

          - `JsonElement Name constant`

            Must be "edit".

          - `bool? Enabled`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy? PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `Type Type`

        - `class BetaManagedAgentsReadToolConfigParams:`

          Configuration override for the read tool.

          - `JsonElement Name constant`

            Must be "read".

          - `bool? Enabled`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy? PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `Type Type`

        - `class BetaManagedAgentsWriteToolConfigParams:`

          Configuration override for the write tool.

          - `JsonElement Name constant`

            Must be "write".

          - `bool? Enabled`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy? PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `Type Type`

        - `class BetaManagedAgentsGlobToolConfigParams:`

          Configuration override for the glob tool.

          - `JsonElement Name constant`

            Must be "glob".

          - `bool? Enabled`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy? PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `Type Type`

        - `class BetaManagedAgentsGrepToolConfigParams:`

          Configuration override for the grep tool.

          - `JsonElement Name constant`

            Must be "grep".

          - `bool? Enabled`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy? PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `Type Type`

        - `class BetaManagedAgentsWebFetchToolConfigParams:`

          Configuration override for the web_fetch tool.

          - `JsonElement Name constant`

            Must be "web_fetch".

          - `IReadOnlyList<string> AllowedDomains`

            Only fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

          - `IReadOnlyList<string> BlockedDomains`

            Never fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

          - `bool? Enabled`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `int? MaxContentTokens`

            Maximum number of tokens of fetched text content to include in context per call. Does not apply to binary content such as PDFs.

            format: int32

          - `PermissionPolicy? PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `Type Type`

        - `class BetaManagedAgentsWebSearchToolConfigParams:`

          Configuration override for the web_search tool.

          - `JsonElement Name constant`

            Must be "web_search".

          - `IReadOnlyList<string> AllowedDomains`

            Only return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

          - `IReadOnlyList<string> BlockedDomains`

            Never return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

          - `bool? Enabled`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy? PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `Type Type`

          - `BetaManagedAgentsUserLocation? UserLocation`

            Approximate user location for search result localization.

            - `JsonElement Type constant`

              Location precision. Only "approximate" is supported.

            - `string? City`

              City name.

              minLength: 1, maxLength: 255

            - `string? Country`

              Two-letter ISO 3166-1 country code, uppercase.

            - `string? Region`

              Region or state name.

              minLength: 1, maxLength: 255

            - `string? Timezone`

              IANA timezone identifier, e.g. "America/Los_Angeles".

              minLength: 1, maxLength: 255

      - `BetaManagedAgentsAgentToolsetDefaultConfigParams? DefaultConfig`

        Default configuration for all tools in a toolset.

        - `bool? Enabled`

          Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

        - `PermissionPolicy? PermissionPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy:`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy:`

            Tool calls require user confirmation before execution.

    - `class BetaManagedAgentsMcpToolsetParams:`

      Configuration for tools from an MCP server defined in `mcp_servers`.

      - `required string McpServerName`

        Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

        minLength: 1, maxLength: 255

      - `required Type Type`

      - `IReadOnlyList<BetaManagedAgentsMcpToolConfigParams> Configs`

        Per-tool configuration overrides.

        - `required string Name`

          Name of the MCP tool to configure. 1-128 characters.

          minLength: 1, maxLength: 128

        - `bool? Enabled`

          Whether this tool is enabled. Overrides the `default_config` setting.

        - `PermissionPolicy? PermissionPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy:`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy:`

            Tool calls require user confirmation before execution.

      - `BetaManagedAgentsMcpToolsetDefaultConfigParams? DefaultConfig`

        Default configuration for all tools from an MCP server.

        - `bool? Enabled`

          Whether tools are enabled by default. Defaults to true if not specified.

        - `PermissionPolicy? PermissionPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy:`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy:`

            Tool calls require user confirmation before execution.

    - `class BetaManagedAgentsCustomToolParams:`

      A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

      - `required string Description`

        Description of what the tool does, shown to the agent to help it decide when to use the tool.

        minLength: 1

      - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

        JSON Schema for custom tool input parameters.

        - `JsonElement Type constant`

        - `IReadOnlyDictionary<string, JsonElement>? Properties`

        - `IReadOnlyList<string>? Required`

      - `required string Name`

        Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

        minLength: 1, maxLength: 128

      - `required Type Type`

  - `int Version`

    The specific `agent` version to use. Omit to use the latest version.

    format: int32

### Beta Managed Agents Branch Checkout

- `class BetaManagedAgentsBranchCheckout:`

  - `required string Name`

    Branch name to check out.

    minLength: 1, maxLength: 255

  - `required Type Type`

### Beta Managed Agents Budget Limit

- `class BetaManagedAgentsBudgetLimit:`

  A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

  - `required BetaMonetaryAmount MaxListCost`

    A monetary amount in a specific currency.

    - `required string Amount`

      Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

    - `required BetaCurrency Currency`

      Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

  - `required Type Type`

### Beta Managed Agents Cache Creation Usage

- `class BetaManagedAgentsCacheCreationUsage:`

  Prompt-cache creation token usage broken down by cache lifetime.

  - `int Ephemeral1hInputTokens`

    Tokens used to create 1-hour ephemeral cache entries.

    format: int32

  - `int Ephemeral5mInputTokens`

    Tokens used to create 5-minute ephemeral cache entries.

    format: int32

### Beta Managed Agents Commit Checkout

- `class BetaManagedAgentsCommitCheckout:`

  - `required string Sha`

    Full commit SHA to check out.

    minLength: 7, maxLength: 64

  - `required Type Type`

### Beta Managed Agents Deleted Session

- `class BetaManagedAgentsDeletedSession:`

  Confirmation that a `session` has been permanently deleted.

  - `required string ID`

  - `required Type Type`

### Beta Managed Agents Delta Content

- `class BetaManagedAgentsDeltaContent:`

  - `required BetaManagedAgentsTextBlock Content`

    Regular text content.

    - `required string Text`

      The text content.

      minLength: 1

    - `required Type Type`

  - `required Type Type`

  - `long Index`

    Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

    format: uint32

### Beta Managed Agents Delta Event

- `class BetaManagedAgentsDeltaEvent:`

  An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

  - `required BetaManagedAgentsDeltaContent Delta`

    One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

    - `required BetaManagedAgentsTextBlock Content`

      Regular text content.

      - `required string Text`

        The text content.

        minLength: 1

      - `required Type Type`

    - `required Type Type`

    - `long Index`

      Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

      format: uint32

  - `required string EventID`

    The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

  - `required Type Type`

### Beta Managed Agents Delta Type

- `enum BetaManagedAgentsDeltaType:`

  EventDeltaType enum

  - `AgentMessage`

  - `AgentThinking`

### Beta Managed Agents File Resource Params

- `class BetaManagedAgentsFileResourceParams:`

  Mount a file uploaded via the Files API into the session.

  - `required string FileID`

    ID of a previously uploaded file.

    minLength: 1, maxLength: 128

  - `required Type Type`

  - `string? MountPath`

    Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    minLength: 1, maxLength: 4096

### Beta Managed Agents GitHub Repository Resource Params

- `class BetaManagedAgentsGitHubRepositoryResourceParams:`

  Mount a GitHub repository into the session's container.

  - `required string AuthorizationToken`

    GitHub authorization token used to clone the repository.

    minLength: 1, maxLength: 4096

  - `required Type Type`

  - `required string Url`

    Github URL of the repository

    minLength: 1, maxLength: 2048

  - `Checkout? Checkout`

    Branch or commit to check out. Defaults to the repository's default branch.

    - `class BetaManagedAgentsBranchCheckout:`

      - `required string Name`

        Branch name to check out.

        minLength: 1, maxLength: 255

      - `required Type Type`

    - `class BetaManagedAgentsCommitCheckout:`

      - `required string Sha`

        Full commit SHA to check out.

        minLength: 7, maxLength: 64

      - `required Type Type`

  - `string? MountPath`

    Mount path in the container. Defaults to `/workspace/<repo-name>`.

    minLength: 1, maxLength: 4096

### Beta Managed Agents Memory Store Resource Param

- `class BetaManagedAgentsMemoryStoreResourceParam:`

  Parameters for attaching a memory store to an agent session.

  - `required string MemoryStoreID`

    The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

  - `required Type Type`

  - `Access? Access`

    Access mode for an attached memory store.

    - `ReadWrite`

    - `ReadOnly`

  - `string? Instructions`

    Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

    maxLength: 4096

### Beta Managed Agents Multiagent

- `class BetaManagedAgentsMultiagent:`

  Resolved coordinator topology with a concrete agent roster.

  - `required IReadOnlyList<Agent> Agents`

    Agents the coordinator may spawn as session threads, each resolved to a specific version.

    - `class BetaManagedAgentsAgentReference:`

      A resolved agent reference with a concrete version.

      - `required string ID`

      - `required Type Type`

      - `required int Version`

        format: int32

    - `class BetaManagedAgentsAdvisor:`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `required string Model`

        The advisor model id.

      - `required Type Type`

  - `required Type Type`

### Beta Managed Agents Multiagent Params

- `class BetaManagedAgentsMultiagentParams:`

  A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.

  - `required IReadOnlyList<BetaManagedAgentsMultiagentRosterEntryParams> Agents`

    Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).

    - `string`

    - `class BetaManagedAgentsAgentParams:`

      Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

      - `required string ID`

        The `agent` ID.

        minLength: 1, maxLength: 128

      - `required Type Type`

      - `int Version`

        The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

        format: int32

    - `class BetaManagedAgentsMultiagentSelfParams:`

      Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

      - `required Type Type`

    - `class BetaManagedAgentsAdvisorParams:`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn. At most one per roster; the entry occupies the roster name `anthropic.advisor`.

      - `required string Model`

        A Claude model id. The model must be permitted as an advisor for this agent's model — see the sessions/threads/advisor spec.

        minLength: 1, maxLength: 256

      - `required Type Type`

  - `required Type Type`

### Beta Managed Agents Multiagent Roster Entry Params

- `class BetaManagedAgentsMultiagentRosterEntryParams: union`

  An entry in a multiagent roster: an agent ID string, a versioned agent reference, or `self`.

  - `string`

  - `class BetaManagedAgentsAgentParams:`

    Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

    - `required string ID`

      The `agent` ID.

      minLength: 1, maxLength: 128

    - `required Type Type`

    - `int Version`

      The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

      format: int32

  - `class BetaManagedAgentsMultiagentSelfParams:`

    Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

    - `required Type Type`

  - `class BetaManagedAgentsAdvisorParams:`

    Platform advisor roster entry: a model the session's primary thread may consult mid-turn. At most one per roster; the entry occupies the roster name `anthropic.advisor`.

    - `required string Model`

      A Claude model id. The model must be permitted as an advisor for this agent's model — see the sessions/threads/advisor spec.

      minLength: 1, maxLength: 256

    - `required Type Type`

### Beta Managed Agents Outcome Evaluation Resource

- `class BetaManagedAgentsOutcomeEvaluationResource:`

  Evaluation state for a single outcome defined via a `define_outcome` event.

  - `required DateTimeOffset? CompletedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string Description`

    What the agent should produce.

  - `required string? Explanation`

    Grader's verdict text from the most recent evaluation. For `satisfied`, explains why criteria are met; for `needs_revision` (intermediate), what's missing; for `failed`, why unrecoverable.

  - `required int Iteration`

    0-indexed revision cycle the outcome is currently on.

    format: int32

  - `required string OutcomeID`

    Server-generated outc_ ID for this outcome.

  - `required string Result`

    Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

  - `required Type Type`

### Beta Managed Agents Server Tool Usage

- `class BetaManagedAgentsServerToolUsage:`

  Cumulative count of server-executed tool invocations, broken down by tool.

  - `int WebFetchRequests`

    Number of server-executed web fetch requests.

    format: int32

  - `int WebSearchRequests`

    Number of server-executed web search requests.

    format: int32

### Beta Managed Agents Session

- `class BetaManagedAgentsSession:`

  A Managed Agents `session`.

  - `required string ID`

  - `required BetaManagedAgentsSessionAgent Agent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `required string ID`

    - `required string? Description`

    - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

      - `required string Name`

      - `required Type Type`

      - `required string Url`

    - `required BetaManagedAgentsModelConfig Model`

      Model identifier and configuration.

      - `required BetaManagedAgentsModel ID`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `ClaudeFable5_1`

          Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

        - `ClaudeSonnet5`

          High-performance model for coding and agents

        - `ClaudeFable5`

          Next generation of intelligence for the hardest knowledge work and coding problems

        - `ClaudeOpus5`

          Powerful intelligence for long-running agents and coding

        - `ClaudeOpus4_8`

          Powerful intelligence for long-running agents and coding

        - `ClaudeOpus4_7`

          Powerful intelligence for long-running agents and coding

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

      - `Effort Effort`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

        - `class BetaManagedAgentsEffortLow:`

          Low effort. Favors latency over reasoning depth.

          - `required Type Type`

        - `class BetaManagedAgentsEffortMedium:`

          Medium effort. Balances latency and reasoning depth.

          - `required Type Type`

        - `class BetaManagedAgentsEffortHigh:`

          High effort. Favors reasoning depth.

          - `required Type Type`

        - `class BetaManagedAgentsEffortXhigh:`

          Extra-high effort. Not all models accept this level.

          - `required Type Type`

        - `class BetaManagedAgentsEffortMax:`

          Maximum effort. Favors reasoning depth over latency.

          - `required Type Type`

      - `string InferenceGeo`

        Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

      - `Speed Speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `Standard`

        - `Fast`

    - `required BetaManagedAgentsSessionMultiagentCoordinator? Multiagent`

      Resolved coordinator topology with full agent definitions for each roster member.

      - `required IReadOnlyList<Agent> Agents`

        Full `agent` definitions the coordinator may spawn as session threads.

        - `class BetaManagedAgentsSessionThreadAgent:`

          Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

          - `required string ID`

          - `required string? Description`

          - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

            - `required string Name`

            - `required Type Type`

            - `required string Url`

          - `required BetaManagedAgentsModelConfig Model`

            Model identifier and configuration.

          - `required string Name`

          - `required IReadOnlyList<Skill> Skills`

            - `class BetaManagedAgentsAnthropicSkill:`

              A resolved Anthropic-managed skill.

              - `required string SkillID`

              - `required Type Type`

              - `required string Version`

            - `class BetaManagedAgentsCustomSkill:`

              A resolved user-created custom skill.

              - `required string SkillID`

              - `required Type Type`

              - `required string Version`

          - `required string? System`

          - `required IReadOnlyList<Tool> Tools`

            - `class BetaManagedAgentsAgentToolset20260401:`

              - `required IReadOnlyList<BetaManagedAgentsAgentToolConfig> Configs`

                - `class BetaManagedAgentsBashToolConfig:`

                  Configuration for the bash tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                      - `required Type Type`

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                      - `required Type Type`

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsEditToolConfig:`

                  Configuration for the edit tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsReadToolConfig:`

                  Configuration for the read tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsWriteToolConfig:`

                  Configuration for the write tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsGlobToolConfig:`

                  Configuration for the glob tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsGrepToolConfig:`

                  Configuration for the grep tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsWebFetchToolConfig:`

                  Configuration for the web_fetch tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                  - `IReadOnlyList<string> AllowedDomains`

                  - `IReadOnlyList<string> BlockedDomains`

                  - `int? MaxContentTokens`

                    format: int32

                - `class BetaManagedAgentsWebSearchToolConfig:`

                  Configuration for the web_search tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                  - `IReadOnlyList<string> AllowedDomains`

                  - `IReadOnlyList<string> BlockedDomains`

                  - `BetaManagedAgentsUserLocation? UserLocation`

                    Approximate user location for search result localization.

                    - `JsonElement Type constant`

                      Location precision. Only "approximate" is supported.

                    - `string? City`

                      City name.

                      minLength: 1, maxLength: 255

                    - `string? Country`

                      Two-letter ISO 3166-1 country code, uppercase.

                    - `string? Region`

                      Region or state name.

                      minLength: 1, maxLength: 255

                    - `string? Timezone`

                      IANA timezone identifier, e.g. "America/Los_Angeles".

                      minLength: 1, maxLength: 255

              - `required BetaManagedAgentsAgentToolsetDefaultConfig DefaultConfig`

                Resolved default configuration for agent tools.

                - `required bool Enabled`

                - `required PermissionPolicy PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy:`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy:`

                    Tool calls require user confirmation before execution.

              - `required Type Type`

            - `class BetaManagedAgentsMcpToolset:`

              - `required IReadOnlyList<BetaManagedAgentsMcpToolConfig> Configs`

                - `required bool Enabled`

                - `required string Name`

                - `required PermissionPolicy PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy:`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy:`

                    Tool calls require user confirmation before execution.

              - `required BetaManagedAgentsMcpToolsetDefaultConfig DefaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `required bool Enabled`

                - `required PermissionPolicy PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy:`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy:`

                    Tool calls require user confirmation before execution.

              - `required string McpServerName`

              - `required Type Type`

            - `class BetaManagedAgentsCustomTool:`

              A custom tool as returned in API responses.

              - `required string Description`

              - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

                JSON Schema for custom tool input parameters.

                - `JsonElement Type constant`

                - `IReadOnlyDictionary<string, JsonElement>? Properties`

                - `IReadOnlyList<string>? Required`

              - `required string Name`

              - `required Type Type`

          - `required Type Type`

          - `required int Version`

            format: int32

        - `class BetaManagedAgentsAdvisor:`

          Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

          - `required string Model`

            The advisor model id.

          - `required Type Type`

      - `required Type Type`

    - `required string Name`

    - `required IReadOnlyList<Skill> Skills`

      - `class BetaManagedAgentsAnthropicSkill:`

        A resolved Anthropic-managed skill.

      - `class BetaManagedAgentsCustomSkill:`

        A resolved user-created custom skill.

    - `required string? System`

    - `required IReadOnlyList<Tool> Tools`

      - `class BetaManagedAgentsAgentToolset20260401:`

      - `class BetaManagedAgentsMcpToolset:`

      - `class BetaManagedAgentsCustomTool:`

        A custom tool as returned in API responses.

    - `required Type Type`

    - `required int Version`

      format: int32

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required BetaManagedAgentsBudgetLimit? Budget`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `required BetaMonetaryAmount MaxListCost`

      A monetary amount in a specific currency.

      - `required string Amount`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `required BetaCurrency Currency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `required Type Type`

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string EnvironmentID`

  - `required IReadOnlyDictionary<string, string> Metadata`

  - `required IReadOnlyList<BetaManagedAgentsOutcomeEvaluationResource> OutcomeEvaluations`

    Per-outcome evaluation state. One entry per `define_outcome` event sent to the session.

    - `required DateTimeOffset? CompletedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string Description`

      What the agent should produce.

    - `required string? Explanation`

      Grader's verdict text from the most recent evaluation. For `satisfied`, explains why criteria are met; for `needs_revision` (intermediate), what's missing; for `failed`, why unrecoverable.

    - `required int Iteration`

      0-indexed revision cycle the outcome is currently on.

      format: int32

    - `required string OutcomeID`

      Server-generated outc_ ID for this outcome.

    - `required string Result`

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

    - `required Type Type`

  - `required IReadOnlyList<BetaManagedAgentsSessionResource> Resources`

    - `class BetaManagedAgentsGitHubRepositoryResource:`

      - `required string ID`

      - `required DateTimeOffset CreatedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required string MountPath`

      - `required Type Type`

      - `required DateTimeOffset UpdatedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required string Url`

      - `Checkout? Checkout`

        - `class BetaManagedAgentsBranchCheckout:`

          - `required string Name`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `required Type Type`

        - `class BetaManagedAgentsCommitCheckout:`

          - `required string Sha`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `required Type Type`

    - `class BetaManagedAgentsFileResource:`

      - `required string ID`

      - `required DateTimeOffset CreatedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required string FileID`

      - `required string MountPath`

      - `required Type Type`

      - `required DateTimeOffset UpdatedAt`

        A timestamp in RFC 3339 format

        format: date-time

    - `class BetaManagedAgentsMemoryStoreResource:`

      A memory store attached to an agent session.

      - `required string MemoryStoreID`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `required Type Type`

      - `Access? Access`

        Access mode for an attached memory store.

        - `ReadWrite`

        - `ReadOnly`

      - `string Description`

        Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

      - `string? Instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

        maxLength: 4096

      - `string? MountPath`

        Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

      - `string? Name`

        Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

  - `required BetaManagedAgentsSessionStats Stats`

    Timing statistics for a session.

    - `double ActiveSeconds`

      Cumulative time in seconds the session spent in `running` status. Excludes idle time.

      format: double

    - `double DurationSeconds`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

      format: double

  - `required Status Status`

    SessionStatus enum

    - `Rescheduling`

    - `Running`

    - `Idle`

    - `Terminated`

  - `required string? Title`

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required BetaManagedAgentsSessionUsage Usage`

    Cumulative token usage for a session across all turns.

    - `double ActiveSeconds`

      Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once, unlike `stats.active_seconds`, which sums each thread's own active time. This is the duration the session's runtime cost is priced on.

      format: double

    - `BetaManagedAgentsCacheCreationUsage CacheCreation`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `int Ephemeral1hInputTokens`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `int Ephemeral5mInputTokens`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `int CacheReadInputTokens`

      Total tokens read from prompt cache.

      format: int32

    - `int InputTokens`

      Total input tokens consumed across all turns.

      format: int32

    - `BetaMonetaryAmount? ListCost`

      A monetary amount in a specific currency.

    - `int OutputTokens`

      Total output tokens generated across all turns.

      format: int32

    - `BetaManagedAgentsServerToolUsage? ServerToolUse`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `int WebFetchRequests`

        Number of server-executed web fetch requests.

        format: int32

      - `int WebSearchRequests`

        Number of server-executed web search requests.

        format: int32

  - `required IReadOnlyList<string> VaultIds`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `string? DeploymentID`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Beta Managed Agents Session Agent

- `class BetaManagedAgentsSessionAgent:`

  Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

  - `required string ID`

  - `required string? Description`

  - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

    - `required string Name`

    - `required Type Type`

    - `required string Url`

  - `required BetaManagedAgentsModelConfig Model`

    Model identifier and configuration.

    - `required BetaManagedAgentsModel ID`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `ClaudeFable5_1`

        Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

      - `ClaudeSonnet5`

        High-performance model for coding and agents

      - `ClaudeFable5`

        Next generation of intelligence for the hardest knowledge work and coding problems

      - `ClaudeOpus5`

        Powerful intelligence for long-running agents and coding

      - `ClaudeOpus4_8`

        Powerful intelligence for long-running agents and coding

      - `ClaudeOpus4_7`

        Powerful intelligence for long-running agents and coding

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

    - `Effort Effort`

      How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

      - `class BetaManagedAgentsEffortLow:`

        Low effort. Favors latency over reasoning depth.

        - `required Type Type`

      - `class BetaManagedAgentsEffortMedium:`

        Medium effort. Balances latency and reasoning depth.

        - `required Type Type`

      - `class BetaManagedAgentsEffortHigh:`

        High effort. Favors reasoning depth.

        - `required Type Type`

      - `class BetaManagedAgentsEffortXhigh:`

        Extra-high effort. Not all models accept this level.

        - `required Type Type`

      - `class BetaManagedAgentsEffortMax:`

        Maximum effort. Favors reasoning depth over latency.

        - `required Type Type`

    - `string InferenceGeo`

      Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

    - `Speed Speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `Standard`

      - `Fast`

  - `required BetaManagedAgentsSessionMultiagentCoordinator? Multiagent`

    Resolved coordinator topology with full agent definitions for each roster member.

    - `required IReadOnlyList<Agent> Agents`

      Full `agent` definitions the coordinator may spawn as session threads.

      - `class BetaManagedAgentsSessionThreadAgent:`

        Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

        - `required string ID`

        - `required string? Description`

        - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

          - `required string Name`

          - `required Type Type`

          - `required string Url`

        - `required BetaManagedAgentsModelConfig Model`

          Model identifier and configuration.

        - `required string Name`

        - `required IReadOnlyList<Skill> Skills`

          - `class BetaManagedAgentsAnthropicSkill:`

            A resolved Anthropic-managed skill.

            - `required string SkillID`

            - `required Type Type`

            - `required string Version`

          - `class BetaManagedAgentsCustomSkill:`

            A resolved user-created custom skill.

            - `required string SkillID`

            - `required Type Type`

            - `required string Version`

        - `required string? System`

        - `required IReadOnlyList<Tool> Tools`

          - `class BetaManagedAgentsAgentToolset20260401:`

            - `required IReadOnlyList<BetaManagedAgentsAgentToolConfig> Configs`

              - `class BetaManagedAgentsBashToolConfig:`

                Configuration for the bash tool.

                - `required bool Enabled`

                - `JsonElement Name constant`

                - `required PermissionPolicy PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy:`

                    Tool calls are automatically approved without user confirmation.

                    - `required Type Type`

                  - `class BetaManagedAgentsAlwaysAskPolicy:`

                    Tool calls require user confirmation before execution.

                    - `required Type Type`

                - `JsonElement Type constant`

              - `class BetaManagedAgentsEditToolConfig:`

                Configuration for the edit tool.

                - `required bool Enabled`

                - `JsonElement Name constant`

                - `required PermissionPolicy PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy:`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy:`

                    Tool calls require user confirmation before execution.

                - `JsonElement Type constant`

              - `class BetaManagedAgentsReadToolConfig:`

                Configuration for the read tool.

                - `required bool Enabled`

                - `JsonElement Name constant`

                - `required PermissionPolicy PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy:`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy:`

                    Tool calls require user confirmation before execution.

                - `JsonElement Type constant`

              - `class BetaManagedAgentsWriteToolConfig:`

                Configuration for the write tool.

                - `required bool Enabled`

                - `JsonElement Name constant`

                - `required PermissionPolicy PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy:`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy:`

                    Tool calls require user confirmation before execution.

                - `JsonElement Type constant`

              - `class BetaManagedAgentsGlobToolConfig:`

                Configuration for the glob tool.

                - `required bool Enabled`

                - `JsonElement Name constant`

                - `required PermissionPolicy PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy:`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy:`

                    Tool calls require user confirmation before execution.

                - `JsonElement Type constant`

              - `class BetaManagedAgentsGrepToolConfig:`

                Configuration for the grep tool.

                - `required bool Enabled`

                - `JsonElement Name constant`

                - `required PermissionPolicy PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy:`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy:`

                    Tool calls require user confirmation before execution.

                - `JsonElement Type constant`

              - `class BetaManagedAgentsWebFetchToolConfig:`

                Configuration for the web_fetch tool.

                - `required bool Enabled`

                - `JsonElement Name constant`

                - `required PermissionPolicy PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy:`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy:`

                    Tool calls require user confirmation before execution.

                - `JsonElement Type constant`

                - `IReadOnlyList<string> AllowedDomains`

                - `IReadOnlyList<string> BlockedDomains`

                - `int? MaxContentTokens`

                  format: int32

              - `class BetaManagedAgentsWebSearchToolConfig:`

                Configuration for the web_search tool.

                - `required bool Enabled`

                - `JsonElement Name constant`

                - `required PermissionPolicy PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy:`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy:`

                    Tool calls require user confirmation before execution.

                - `JsonElement Type constant`

                - `IReadOnlyList<string> AllowedDomains`

                - `IReadOnlyList<string> BlockedDomains`

                - `BetaManagedAgentsUserLocation? UserLocation`

                  Approximate user location for search result localization.

                  - `JsonElement Type constant`

                    Location precision. Only "approximate" is supported.

                  - `string? City`

                    City name.

                    minLength: 1, maxLength: 255

                  - `string? Country`

                    Two-letter ISO 3166-1 country code, uppercase.

                  - `string? Region`

                    Region or state name.

                    minLength: 1, maxLength: 255

                  - `string? Timezone`

                    IANA timezone identifier, e.g. "America/Los_Angeles".

                    minLength: 1, maxLength: 255

            - `required BetaManagedAgentsAgentToolsetDefaultConfig DefaultConfig`

              Resolved default configuration for agent tools.

              - `required bool Enabled`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

            - `required Type Type`

          - `class BetaManagedAgentsMcpToolset:`

            - `required IReadOnlyList<BetaManagedAgentsMcpToolConfig> Configs`

              - `required bool Enabled`

              - `required string Name`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

            - `required BetaManagedAgentsMcpToolsetDefaultConfig DefaultConfig`

              Resolved default configuration for all tools from an MCP server.

              - `required bool Enabled`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

            - `required string McpServerName`

            - `required Type Type`

          - `class BetaManagedAgentsCustomTool:`

            A custom tool as returned in API responses.

            - `required string Description`

            - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

              JSON Schema for custom tool input parameters.

              - `JsonElement Type constant`

              - `IReadOnlyDictionary<string, JsonElement>? Properties`

              - `IReadOnlyList<string>? Required`

            - `required string Name`

            - `required Type Type`

        - `required Type Type`

        - `required int Version`

          format: int32

      - `class BetaManagedAgentsAdvisor:`

        Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

        - `required string Model`

          The advisor model id.

        - `required Type Type`

    - `required Type Type`

  - `required string Name`

  - `required IReadOnlyList<Skill> Skills`

    - `class BetaManagedAgentsAnthropicSkill:`

      A resolved Anthropic-managed skill.

    - `class BetaManagedAgentsCustomSkill:`

      A resolved user-created custom skill.

  - `required string? System`

  - `required IReadOnlyList<Tool> Tools`

    - `class BetaManagedAgentsAgentToolset20260401:`

    - `class BetaManagedAgentsMcpToolset:`

    - `class BetaManagedAgentsCustomTool:`

      A custom tool as returned in API responses.

  - `required Type Type`

  - `required int Version`

    format: int32

### Beta Managed Agents Session Agent Update

- `class BetaManagedAgentsSessionAgentUpdate:`

  Mid-session agent configuration update. Only `tools` and `mcp_servers` are updatable. Full replacement: the provided array becomes the new value. To preserve existing entries, GET the session, modify the array, and POST it back.

  - `IReadOnlyList<BetaManagedAgentsUrlMcpServerParams> McpServers`

    Replacement MCP server list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.

    - `required string Name`

      Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

      minLength: 1, maxLength: 255

    - `required Type Type`

    - `required string Url`

      Endpoint URL for the MCP server.

      maxLength: 2048

  - `IReadOnlyList<Tool> Tools`

    Replacement tool list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.

    - `class BetaManagedAgentsAgentToolset20260401Params:`

      Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

      - `required Type Type`

      - `IReadOnlyList<BetaManagedAgentsAgentToolConfigParams> Configs`

        Per-tool configuration overrides.

        - `class BetaManagedAgentsBashToolConfigParams:`

          Configuration override for the bash tool.

          - `JsonElement Name constant`

            Must be "bash".

          - `bool? Enabled`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy? PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

              - `required Type Type`

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

              - `required Type Type`

          - `Type Type`

        - `class BetaManagedAgentsEditToolConfigParams:`

          Configuration override for the edit tool.

          - `JsonElement Name constant`

            Must be "edit".

          - `bool? Enabled`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy? PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `Type Type`

        - `class BetaManagedAgentsReadToolConfigParams:`

          Configuration override for the read tool.

          - `JsonElement Name constant`

            Must be "read".

          - `bool? Enabled`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy? PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `Type Type`

        - `class BetaManagedAgentsWriteToolConfigParams:`

          Configuration override for the write tool.

          - `JsonElement Name constant`

            Must be "write".

          - `bool? Enabled`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy? PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `Type Type`

        - `class BetaManagedAgentsGlobToolConfigParams:`

          Configuration override for the glob tool.

          - `JsonElement Name constant`

            Must be "glob".

          - `bool? Enabled`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy? PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `Type Type`

        - `class BetaManagedAgentsGrepToolConfigParams:`

          Configuration override for the grep tool.

          - `JsonElement Name constant`

            Must be "grep".

          - `bool? Enabled`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy? PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `Type Type`

        - `class BetaManagedAgentsWebFetchToolConfigParams:`

          Configuration override for the web_fetch tool.

          - `JsonElement Name constant`

            Must be "web_fetch".

          - `IReadOnlyList<string> AllowedDomains`

            Only fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

          - `IReadOnlyList<string> BlockedDomains`

            Never fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

          - `bool? Enabled`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `int? MaxContentTokens`

            Maximum number of tokens of fetched text content to include in context per call. Does not apply to binary content such as PDFs.

            format: int32

          - `PermissionPolicy? PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `Type Type`

        - `class BetaManagedAgentsWebSearchToolConfigParams:`

          Configuration override for the web_search tool.

          - `JsonElement Name constant`

            Must be "web_search".

          - `IReadOnlyList<string> AllowedDomains`

            Only return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

          - `IReadOnlyList<string> BlockedDomains`

            Never return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

          - `bool? Enabled`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `PermissionPolicy? PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy:`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy:`

              Tool calls require user confirmation before execution.

          - `Type Type`

          - `BetaManagedAgentsUserLocation? UserLocation`

            Approximate user location for search result localization.

            - `JsonElement Type constant`

              Location precision. Only "approximate" is supported.

            - `string? City`

              City name.

              minLength: 1, maxLength: 255

            - `string? Country`

              Two-letter ISO 3166-1 country code, uppercase.

            - `string? Region`

              Region or state name.

              minLength: 1, maxLength: 255

            - `string? Timezone`

              IANA timezone identifier, e.g. "America/Los_Angeles".

              minLength: 1, maxLength: 255

      - `BetaManagedAgentsAgentToolsetDefaultConfigParams? DefaultConfig`

        Default configuration for all tools in a toolset.

        - `bool? Enabled`

          Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

        - `PermissionPolicy? PermissionPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy:`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy:`

            Tool calls require user confirmation before execution.

    - `class BetaManagedAgentsMcpToolsetParams:`

      Configuration for tools from an MCP server defined in `mcp_servers`.

      - `required string McpServerName`

        Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

        minLength: 1, maxLength: 255

      - `required Type Type`

      - `IReadOnlyList<BetaManagedAgentsMcpToolConfigParams> Configs`

        Per-tool configuration overrides.

        - `required string Name`

          Name of the MCP tool to configure. 1-128 characters.

          minLength: 1, maxLength: 128

        - `bool? Enabled`

          Whether this tool is enabled. Overrides the `default_config` setting.

        - `PermissionPolicy? PermissionPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy:`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy:`

            Tool calls require user confirmation before execution.

      - `BetaManagedAgentsMcpToolsetDefaultConfigParams? DefaultConfig`

        Default configuration for all tools from an MCP server.

        - `bool? Enabled`

          Whether tools are enabled by default. Defaults to true if not specified.

        - `PermissionPolicy? PermissionPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy:`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy:`

            Tool calls require user confirmation before execution.

    - `class BetaManagedAgentsCustomToolParams:`

      A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

      - `required string Description`

        Description of what the tool does, shown to the agent to help it decide when to use the tool.

        minLength: 1

      - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

        JSON Schema for custom tool input parameters.

        - `JsonElement Type constant`

        - `IReadOnlyDictionary<string, JsonElement>? Properties`

        - `IReadOnlyList<string>? Required`

      - `required string Name`

        Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

        minLength: 1, maxLength: 128

      - `required Type Type`

### Beta Managed Agents Session Multiagent Coordinator

- `class BetaManagedAgentsSessionMultiagentCoordinator:`

  Resolved coordinator topology with full agent definitions for each roster member.

  - `required IReadOnlyList<Agent> Agents`

    Full `agent` definitions the coordinator may spawn as session threads.

    - `class BetaManagedAgentsSessionThreadAgent:`

      Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

      - `required string ID`

      - `required string? Description`

      - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

        - `required string Name`

        - `required Type Type`

        - `required string Url`

      - `required BetaManagedAgentsModelConfig Model`

        Model identifier and configuration.

        - `required BetaManagedAgentsModel ID`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `ClaudeFable5_1`

            Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

          - `ClaudeSonnet5`

            High-performance model for coding and agents

          - `ClaudeFable5`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `ClaudeOpus5`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_8`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_7`

            Powerful intelligence for long-running agents and coding

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

        - `Effort Effort`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow:`

            Low effort. Favors latency over reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortMedium:`

            Medium effort. Balances latency and reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortHigh:`

            High effort. Favors reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortXhigh:`

            Extra-high effort. Not all models accept this level.

            - `required Type Type`

          - `class BetaManagedAgentsEffortMax:`

            Maximum effort. Favors reasoning depth over latency.

            - `required Type Type`

        - `string InferenceGeo`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `Speed Speed`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `Standard`

          - `Fast`

      - `required string Name`

      - `required IReadOnlyList<Skill> Skills`

        - `class BetaManagedAgentsAnthropicSkill:`

          A resolved Anthropic-managed skill.

          - `required string SkillID`

          - `required Type Type`

          - `required string Version`

        - `class BetaManagedAgentsCustomSkill:`

          A resolved user-created custom skill.

          - `required string SkillID`

          - `required Type Type`

          - `required string Version`

      - `required string? System`

      - `required IReadOnlyList<Tool> Tools`

        - `class BetaManagedAgentsAgentToolset20260401:`

          - `required IReadOnlyList<BetaManagedAgentsAgentToolConfig> Configs`

            - `class BetaManagedAgentsBashToolConfig:`

              Configuration for the bash tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                  - `required Type Type`

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

                  - `required Type Type`

              - `JsonElement Type constant`

            - `class BetaManagedAgentsEditToolConfig:`

              Configuration for the edit tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

            - `class BetaManagedAgentsReadToolConfig:`

              Configuration for the read tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

            - `class BetaManagedAgentsWriteToolConfig:`

              Configuration for the write tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

            - `class BetaManagedAgentsGlobToolConfig:`

              Configuration for the glob tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

            - `class BetaManagedAgentsGrepToolConfig:`

              Configuration for the grep tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

            - `class BetaManagedAgentsWebFetchToolConfig:`

              Configuration for the web_fetch tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

              - `IReadOnlyList<string> AllowedDomains`

              - `IReadOnlyList<string> BlockedDomains`

              - `int? MaxContentTokens`

                format: int32

            - `class BetaManagedAgentsWebSearchToolConfig:`

              Configuration for the web_search tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

              - `IReadOnlyList<string> AllowedDomains`

              - `IReadOnlyList<string> BlockedDomains`

              - `BetaManagedAgentsUserLocation? UserLocation`

                Approximate user location for search result localization.

                - `JsonElement Type constant`

                  Location precision. Only "approximate" is supported.

                - `string? City`

                  City name.

                  minLength: 1, maxLength: 255

                - `string? Country`

                  Two-letter ISO 3166-1 country code, uppercase.

                - `string? Region`

                  Region or state name.

                  minLength: 1, maxLength: 255

                - `string? Timezone`

                  IANA timezone identifier, e.g. "America/Los_Angeles".

                  minLength: 1, maxLength: 255

          - `required BetaManagedAgentsAgentToolsetDefaultConfig DefaultConfig`

            Resolved default configuration for agent tools.

            - `required bool Enabled`

            - `required PermissionPolicy PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `required Type Type`

        - `class BetaManagedAgentsMcpToolset:`

          - `required IReadOnlyList<BetaManagedAgentsMcpToolConfig> Configs`

            - `required bool Enabled`

            - `required string Name`

            - `required PermissionPolicy PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `required BetaManagedAgentsMcpToolsetDefaultConfig DefaultConfig`

            Resolved default configuration for all tools from an MCP server.

            - `required bool Enabled`

            - `required PermissionPolicy PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `required string McpServerName`

          - `required Type Type`

        - `class BetaManagedAgentsCustomTool:`

          A custom tool as returned in API responses.

          - `required string Description`

          - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

            JSON Schema for custom tool input parameters.

            - `JsonElement Type constant`

            - `IReadOnlyDictionary<string, JsonElement>? Properties`

            - `IReadOnlyList<string>? Required`

          - `required string Name`

          - `required Type Type`

      - `required Type Type`

      - `required int Version`

        format: int32

    - `class BetaManagedAgentsAdvisor:`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `required string Model`

        The advisor model id.

      - `required Type Type`

  - `required Type Type`

### Beta Managed Agents Session Stats

- `class BetaManagedAgentsSessionStats:`

  Timing statistics for a session.

  - `double ActiveSeconds`

    Cumulative time in seconds the session spent in `running` status. Excludes idle time.

    format: double

  - `double DurationSeconds`

    Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

    format: double

### Beta Managed Agents Session Updated Event

- `class BetaManagedAgentsSessionUpdatedEvent:`

  Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

  - `required string ID`

    Unique identifier for this event.

  - `required DateTimeOffset ProcessedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required Type Type`

  - `BetaManagedAgentsSessionAgent? Agent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `required string ID`

    - `required string? Description`

    - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

      - `required string Name`

      - `required Type Type`

      - `required string Url`

    - `required BetaManagedAgentsModelConfig Model`

      Model identifier and configuration.

      - `required BetaManagedAgentsModel ID`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `ClaudeFable5_1`

          Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

        - `ClaudeSonnet5`

          High-performance model for coding and agents

        - `ClaudeFable5`

          Next generation of intelligence for the hardest knowledge work and coding problems

        - `ClaudeOpus5`

          Powerful intelligence for long-running agents and coding

        - `ClaudeOpus4_8`

          Powerful intelligence for long-running agents and coding

        - `ClaudeOpus4_7`

          Powerful intelligence for long-running agents and coding

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

      - `Effort Effort`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

        - `class BetaManagedAgentsEffortLow:`

          Low effort. Favors latency over reasoning depth.

          - `required Type Type`

        - `class BetaManagedAgentsEffortMedium:`

          Medium effort. Balances latency and reasoning depth.

          - `required Type Type`

        - `class BetaManagedAgentsEffortHigh:`

          High effort. Favors reasoning depth.

          - `required Type Type`

        - `class BetaManagedAgentsEffortXhigh:`

          Extra-high effort. Not all models accept this level.

          - `required Type Type`

        - `class BetaManagedAgentsEffortMax:`

          Maximum effort. Favors reasoning depth over latency.

          - `required Type Type`

      - `string InferenceGeo`

        Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

      - `Speed Speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `Standard`

        - `Fast`

    - `required BetaManagedAgentsSessionMultiagentCoordinator? Multiagent`

      Resolved coordinator topology with full agent definitions for each roster member.

      - `required IReadOnlyList<Agent> Agents`

        Full `agent` definitions the coordinator may spawn as session threads.

        - `class BetaManagedAgentsSessionThreadAgent:`

          Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

          - `required string ID`

          - `required string? Description`

          - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

            - `required string Name`

            - `required Type Type`

            - `required string Url`

          - `required BetaManagedAgentsModelConfig Model`

            Model identifier and configuration.

          - `required string Name`

          - `required IReadOnlyList<Skill> Skills`

            - `class BetaManagedAgentsAnthropicSkill:`

              A resolved Anthropic-managed skill.

              - `required string SkillID`

              - `required Type Type`

              - `required string Version`

            - `class BetaManagedAgentsCustomSkill:`

              A resolved user-created custom skill.

              - `required string SkillID`

              - `required Type Type`

              - `required string Version`

          - `required string? System`

          - `required IReadOnlyList<Tool> Tools`

            - `class BetaManagedAgentsAgentToolset20260401:`

              - `required IReadOnlyList<BetaManagedAgentsAgentToolConfig> Configs`

                - `class BetaManagedAgentsBashToolConfig:`

                  Configuration for the bash tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                      - `required Type Type`

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                      - `required Type Type`

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsEditToolConfig:`

                  Configuration for the edit tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsReadToolConfig:`

                  Configuration for the read tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsWriteToolConfig:`

                  Configuration for the write tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsGlobToolConfig:`

                  Configuration for the glob tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsGrepToolConfig:`

                  Configuration for the grep tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                - `class BetaManagedAgentsWebFetchToolConfig:`

                  Configuration for the web_fetch tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                  - `IReadOnlyList<string> AllowedDomains`

                  - `IReadOnlyList<string> BlockedDomains`

                  - `int? MaxContentTokens`

                    format: int32

                - `class BetaManagedAgentsWebSearchToolConfig:`

                  Configuration for the web_search tool.

                  - `required bool Enabled`

                  - `JsonElement Name constant`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonElement Type constant`

                  - `IReadOnlyList<string> AllowedDomains`

                  - `IReadOnlyList<string> BlockedDomains`

                  - `BetaManagedAgentsUserLocation? UserLocation`

                    Approximate user location for search result localization.

                    - `JsonElement Type constant`

                      Location precision. Only "approximate" is supported.

                    - `string? City`

                      City name.

                      minLength: 1, maxLength: 255

                    - `string? Country`

                      Two-letter ISO 3166-1 country code, uppercase.

                    - `string? Region`

                      Region or state name.

                      minLength: 1, maxLength: 255

                    - `string? Timezone`

                      IANA timezone identifier, e.g. "America/Los_Angeles".

                      minLength: 1, maxLength: 255

              - `required BetaManagedAgentsAgentToolsetDefaultConfig DefaultConfig`

                Resolved default configuration for agent tools.

                - `required bool Enabled`

                - `required PermissionPolicy PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy:`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy:`

                    Tool calls require user confirmation before execution.

              - `required Type Type`

            - `class BetaManagedAgentsMcpToolset:`

              - `required IReadOnlyList<BetaManagedAgentsMcpToolConfig> Configs`

                - `required bool Enabled`

                - `required string Name`

                - `required PermissionPolicy PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy:`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy:`

                    Tool calls require user confirmation before execution.

              - `required BetaManagedAgentsMcpToolsetDefaultConfig DefaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `required bool Enabled`

                - `required PermissionPolicy PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy:`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy:`

                    Tool calls require user confirmation before execution.

              - `required string McpServerName`

              - `required Type Type`

            - `class BetaManagedAgentsCustomTool:`

              A custom tool as returned in API responses.

              - `required string Description`

              - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

                JSON Schema for custom tool input parameters.

                - `JsonElement Type constant`

                - `IReadOnlyDictionary<string, JsonElement>? Properties`

                - `IReadOnlyList<string>? Required`

              - `required string Name`

              - `required Type Type`

          - `required Type Type`

          - `required int Version`

            format: int32

        - `class BetaManagedAgentsAdvisor:`

          Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

          - `required string Model`

            The advisor model id.

          - `required Type Type`

      - `required Type Type`

    - `required string Name`

    - `required IReadOnlyList<Skill> Skills`

      - `class BetaManagedAgentsAnthropicSkill:`

        A resolved Anthropic-managed skill.

      - `class BetaManagedAgentsCustomSkill:`

        A resolved user-created custom skill.

    - `required string? System`

    - `required IReadOnlyList<Tool> Tools`

      - `class BetaManagedAgentsAgentToolset20260401:`

      - `class BetaManagedAgentsMcpToolset:`

      - `class BetaManagedAgentsCustomTool:`

        A custom tool as returned in API responses.

    - `required Type Type`

    - `required int Version`

      format: int32

  - `BetaManagedAgentsBudgetLimit? Budget`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `required BetaMonetaryAmount MaxListCost`

      A monetary amount in a specific currency.

      - `required string Amount`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `required BetaCurrency Currency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `required Type Type`

  - `IReadOnlyDictionary<string, string> Metadata`

    The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

  - `string? Title`

    The session's new title. Present only when the update changed it.

### Beta Managed Agents Session Usage

- `class BetaManagedAgentsSessionUsage:`

  Cumulative token usage for a session across all turns.

  - `double ActiveSeconds`

    Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once, unlike `stats.active_seconds`, which sums each thread's own active time. This is the duration the session's runtime cost is priced on.

    format: double

  - `BetaManagedAgentsCacheCreationUsage CacheCreation`

    Prompt-cache creation token usage broken down by cache lifetime.

    - `int Ephemeral1hInputTokens`

      Tokens used to create 1-hour ephemeral cache entries.

      format: int32

    - `int Ephemeral5mInputTokens`

      Tokens used to create 5-minute ephemeral cache entries.

      format: int32

  - `int CacheReadInputTokens`

    Total tokens read from prompt cache.

    format: int32

  - `int InputTokens`

    Total input tokens consumed across all turns.

    format: int32

  - `BetaMonetaryAmount? ListCost`

    A monetary amount in a specific currency.

    - `required string Amount`

      Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

    - `required BetaCurrency Currency`

      Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

  - `int OutputTokens`

    Total output tokens generated across all turns.

    format: int32

  - `BetaManagedAgentsServerToolUsage? ServerToolUse`

    Cumulative count of server-executed tool invocations, broken down by tool.

    - `int WebFetchRequests`

      Number of server-executed web fetch requests.

      format: int32

    - `int WebSearchRequests`

      Number of server-executed web search requests.

      format: int32

### Beta Managed Agents Session Usage Event

- `class BetaManagedAgentsSessionUsageEvent:`

  Periodic snapshot of the session's cumulative usage and tracked list cost.

  - `required string ID`

    Unique identifier for this event.

  - `required DateTimeOffset ProcessedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required Type Type`

  - `required BetaManagedAgentsSessionUsageSnapshot Usage`

    Point-in-time snapshot of a session's cumulative usage.

    - `double ActiveSeconds`

      Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

      format: double

    - `BetaManagedAgentsCacheCreationUsage CacheCreation`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `int Ephemeral1hInputTokens`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `int Ephemeral5mInputTokens`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `int CacheReadInputTokens`

      Total tokens read from prompt cache.

      format: int32

    - `int InputTokens`

      Total input tokens consumed across all turns.

      format: int32

    - `BetaMonetaryAmount ListCost`

      A monetary amount in a specific currency.

      - `required string Amount`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `required BetaCurrency Currency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `int OutputTokens`

      Total output tokens generated across all turns.

      format: int32

    - `BetaManagedAgentsServerToolUsage ServerToolUse`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `int WebFetchRequests`

        Number of server-executed web fetch requests.

        format: int32

      - `int WebSearchRequests`

        Number of server-executed web search requests.

        format: int32

  - `BetaManagedAgentsBudgetLimit? Budget`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `required BetaMonetaryAmount MaxListCost`

      A monetary amount in a specific currency.

    - `required Type Type`

### Beta Managed Agents Start Event

- `class BetaManagedAgentsStartEvent:`

  Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

  - `required BetaManagedAgentsStartEventPreview Event`

    The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

    - `class BetaManagedAgentsAgentMessagePreview:`

      - `required string ID`

        The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

      - `required Type Type`

    - `class BetaManagedAgentsAgentThinkingPreview:`

      - `required string ID`

        The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

      - `required Type Type`

  - `required Type Type`

### Beta Managed Agents Start Event Preview

- `class BetaManagedAgentsStartEventPreview: union`

  - `class BetaManagedAgentsAgentMessagePreview:`

    - `required string ID`

      The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

    - `required Type Type`

  - `class BetaManagedAgentsAgentThinkingPreview:`

    - `required string ID`

      The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

    - `required Type Type`

### Beta Managed Agents System Content Block

- `class BetaManagedAgentsSystemContentBlock:`

  Regular text content.

  - `required string Text`

    The text content.

    minLength: 1

  - `required Type Type`

### Beta Managed Agents System Message Event

- `class BetaManagedAgentsSystemMessageEvent:`

  A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

  - `required string ID`

    Unique identifier for this event.

  - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

    System content blocks. Text-only.

    - `required string Text`

      The text content.

      minLength: 1

    - `required Type Type`

  - `required Type Type`

  - `DateTimeOffset? ProcessedAt`

    A timestamp in RFC 3339 format

    format: date-time

### Beta Managed Agents User Tool Result Event

- `class BetaManagedAgentsUserToolResultEvent:`

  Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

  - `required string ID`

    Unique identifier for this event.

  - `required string ToolUseID`

    The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `required Type Type`

  - `IReadOnlyList<Content> Content`

    The result content returned by the tool.

    - `class BetaManagedAgentsTextBlock:`

      Regular text content.

      - `required string Text`

        The text content.

        minLength: 1

      - `required Type Type`

    - `class BetaManagedAgentsImageBlock:`

      Image content specified directly as base64 data or as a reference via a URL.

      - `required Source Source`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource:`

          Base64-encoded image data.

          - `required string Data`

            Base64-encoded image data.

            minLength: 1

          - `required string MediaType`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            minLength: 1

          - `required Type Type`

        - `class BetaManagedAgentsUrlImageSource:`

          Image referenced by URL.

          - `required Type Type`

          - `required string Url`

            URL of the image to fetch.

            minLength: 1

        - `class BetaManagedAgentsFileImageSource:`

          Image referenced by file ID.

          - `required string FileID`

            ID of a previously uploaded file.

            minLength: 1

          - `required Type Type`

      - `required Type Type`

    - `class BetaManagedAgentsDocumentBlock:`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `required Source Source`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource:`

          Base64-encoded document data.

          - `required string Data`

            Base64-encoded document data.

            minLength: 1

          - `required string MediaType`

            MIME type of the document (e.g., "application/pdf").

            minLength: 1

          - `required Type Type`

        - `class BetaManagedAgentsPlainTextDocumentSource:`

          Plain text document content.

          - `required string Data`

            The plain text content.

            minLength: 1

          - `required MediaType MediaType`

            MIME type of the text content. Must be "text/plain".

          - `required Type Type`

        - `class BetaManagedAgentsUrlDocumentSource:`

          Document referenced by URL.

          - `required Type Type`

          - `required string Url`

            URL of the document to fetch.

            minLength: 1

        - `class BetaManagedAgentsFileDocumentSource:`

          Document referenced by file ID.

          - `required string FileID`

            ID of a previously uploaded file.

            minLength: 1

          - `required Type Type`

      - `required Type Type`

      - `string? Context`

        Additional context about the document for the model.

      - `string? Title`

        The title of the document.

    - `class BetaManagedAgentsSearchResultBlock:`

      A block containing a web search result.

      - `required BetaManagedAgentsSearchResultCitations Citations`

        Citation settings for a search result.

        - `required bool Enabled`

          Whether citations are enabled for this search result.

      - `required IReadOnlyList<BetaManagedAgentsSearchResultContent> Content`

        Array of text content blocks from the search result.

        - `required string Text`

          The text content.

          minLength: 1

        - `required Type Type`

      - `required string Source`

        The URL source of the search result.

        minLength: 1

      - `required string Title`

        The title of the search result.

        minLength: 1

      - `required Type Type`

  - `bool? IsError`

    Whether the tool execution resulted in an error.

  - `DateTimeOffset? ProcessedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `string? SessionThreadID`

    Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

## Sessions › Events

### List Events

`EventListPage Beta.Sessions.Events.List(parameters, cancellationToken = default)`

**GET** `/v1/sessions/{session_id}/events`

List Events

#### Parameters

- `EventListParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `DateTimeOffset createdAtGt`

    Query param: Return events created after this time (exclusive). Compared against the event's `processed_at` value.

    format: date-time

  - `DateTimeOffset createdAtGte`

    Query param: Return events created at or after this time (inclusive). Compared against the event's `processed_at` value.

    format: date-time

  - `DateTimeOffset createdAtLt`

    Query param: Return events created before this time (exclusive). Compared against the event's `processed_at` value.

    format: date-time

  - `DateTimeOffset createdAtLte`

    Query param: Return events created at or before this time (inclusive). Compared against the event's `processed_at` value.

    format: date-time

  - `int limit`

    Query param: Query parameter for limit

    format: int32

  - `Order order`

    Query param: Sort direction for results, ordered by the event's `processed_at`. Defaults to `asc` (chronological).

    - `Asc`

    - `Desc`

  - `string page`

    Query param: Opaque pagination cursor from a previous response's `next_page`.

  - `IReadOnlyList<string> types`

    Query param: Filter by event type. Values match the `type` field on returned events (for example, `user.message` or `agent.tool_use`). Omit to return all event types.

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

#### Returns

- `class BetaManagedAgentsSessionEvent: union`

  Union type for all event types in a session.

  - `class BetaManagedAgentsUserMessageEvent:`

    A user message event in the session conversation.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<Content> Content`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `required string Text`

          The text content.

          minLength: 1

        - `required Type Type`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `required Source Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `required string Data`

              Base64-encoded image data.

              minLength: 1

            - `required string MediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

            - `required Type Type`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `required Type Type`

            - `required string Url`

              URL of the image to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

              minLength: 1

            - `required Type Type`

        - `required Type Type`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `required Source Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `required string Data`

              Base64-encoded document data.

              minLength: 1

            - `required string MediaType`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

            - `required Type Type`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `required string Data`

              The plain text content.

              minLength: 1

            - `required MediaType MediaType`

              MIME type of the text content. Must be "text/plain".

            - `required Type Type`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `required Type Type`

            - `required string Url`

              URL of the document to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

              minLength: 1

            - `required Type Type`

        - `required Type Type`

        - `string? Context`

          Additional context about the document for the model.

        - `string? Title`

          The title of the document.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

        - `required Type Type`

    - `required Type Type`

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsUserInterruptEvent:`

    An interrupt event that pauses agent execution and returns control to the user.

    - `required string ID`

      Unique identifier for this event.

    - `required Type Type`

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `string? SessionThreadID`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEvent:`

    A tool confirmation event that approves or denies a pending tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required Result Result`

      UserToolConfirmationResult enum

      - `Allow`

      - `Deny`

    - `required string ToolUseID`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `required Type Type`

    - `string? DenyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `string? SessionThreadID`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `class BetaManagedAgentsUserCustomToolResultEvent:`

    Event sent by the client providing the result of a custom tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required string CustomToolUseID`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `required Type Type`

    - `IReadOnlyList<Content> Content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

        - `required BetaManagedAgentsSearchResultCitations Citations`

          Citation settings for a search result.

          - `required bool Enabled`

            Whether citations are enabled for this search result.

        - `required IReadOnlyList<BetaManagedAgentsSearchResultContent> Content`

          Array of text content blocks from the search result.

          - `required string Text`

            The text content.

            minLength: 1

          - `required Type Type`

        - `required string Source`

          The URL source of the search result.

          minLength: 1

        - `required string Title`

          The title of the search result.

          minLength: 1

        - `required Type Type`

    - `bool? IsError`

      Whether the tool execution resulted in an error.

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `string? SessionThreadID`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsAgentCustomToolUseEvent:`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyDictionary<string, JsonElement> Input`

      Input parameters for the tool call.

    - `required string Name`

      Name of the custom tool being called.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

    - `string? SessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `class BetaManagedAgentsAgentMessageEvent:`

    An agent response event in the session conversation.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<Content> Content`

      Array of text blocks comprising the agent response.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsAgentThinkingEvent:`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsAgentMcpToolUseEvent:`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyDictionary<string, JsonElement> Input`

      Input parameters for the tool call.

    - `required string McpServerName`

      Name of the MCP server providing the tool.

    - `required string Name`

      Name of the MCP tool being used.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

    - `EvaluatedPermission EvaluatedPermission`

      AgentEvaluatedPermission enum

      - `Allow`

      - `Ask`

      - `Deny`

    - `string? SessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentMcpToolResultEvent:`

    Event representing the result of an MCP tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required string McpToolUseID`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

    - `IReadOnlyList<Content> Content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

    - `bool? IsError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent:`

    Event emitted when the agent invokes a built-in agent tool.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyDictionary<string, JsonElement> Input`

      Input parameters for the tool call.

    - `required string Name`

      Name of the agent tool being used.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

    - `EvaluatedPermission EvaluatedPermission`

      AgentEvaluatedPermission enum

      - `Allow`

      - `Ask`

      - `Deny`

    - `string? SessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentToolResultEvent:`

    Event representing the result of an agent tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string ToolUseID`

      The id of the `agent.tool_use` event this result corresponds to.

    - `required Type Type`

    - `IReadOnlyList<Content> Content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

    - `bool? IsError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadMessageReceivedEvent:`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<Content> Content`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

    - `required string FromSessionThreadID`

      Public `sthr_` ID of the thread that sent the message.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

    - `string? FromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class BetaManagedAgentsAgentThreadMessageSentEvent:`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<Content> Content`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string ToSessionThreadID`

      Public `sthr_` ID of the thread the message was sent to.

    - `required Type Type`

    - `string? ToAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent:`

    Indicates that context compaction (summarization) occurred during the session.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSessionErrorEvent:`

    An error event indicating a problem occurred during session execution.

    - `required string ID`

      Unique identifier for this event.

    - `required Error Error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError:`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `required Type Type`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `required Type Type`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `required Type Type`

        - `required Type Type`

      - `class BetaManagedAgentsModelOverloadedError:`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

      - `class BetaManagedAgentsModelRateLimitedError:`

        The model request was rate-limited.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

      - `class BetaManagedAgentsModelRequestFailedError:`

        A model request failed for a reason other than overload or rate-limiting.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

      - `class BetaManagedAgentsMcpConnectionFailedError:`

        Failed to connect to an MCP server.

        - `required string McpServerName`

          Name of the MCP server that failed to connect.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

      - `class BetaManagedAgentsMcpAuthenticationFailedError:`

        Authentication to an MCP server failed.

        - `required string McpServerName`

          Name of the MCP server that failed authentication.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

      - `class BetaManagedAgentsBillingError:`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

      - `class BetaManagedAgentsCredentialHostUnreachableError:`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `required string CredentialID`

          ID of the affected credential.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

        - `required string VaultID`

          ID of the vault containing the affected credential.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent:`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSessionStatusRunningEvent:`

    Indicates the session is actively running and the agent is working.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSessionStatusIdleEvent:`

    Indicates the agent has paused and is awaiting user input.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required StopReason StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

        - `required Type Type`

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `required IReadOnlyList<string> EventIds`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `required Type Type`

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `required Type Type`

      - `class BetaManagedAgentsSessionBudgetReached:`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `required Type Type`

    - `required Type Type`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent:`

    Indicates the session has terminated, either due to an error or completion.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSessionThreadCreatedEvent:`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the callable agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string SessionThreadID`

      Public `sthr_` ID of the newly created thread.

    - `required Type Type`

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent:`

    Emitted when an outcome evaluation cycle begins.

    - `required string ID`

      Unique identifier for this event.

    - `required int Iteration`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

      format: int32

    - `required string OutcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent:`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `required string ID`

      Unique identifier for this event.

    - `required string Explanation`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `required int Iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `required string OutcomeEvaluationStartID`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `required string OutcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string Result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `required Type Type`

    - `required BetaManagedAgentsSpanModelUsage Usage`

      Token usage for a single model request.

      - `required int CacheCreationInputTokens`

        Tokens used to create prompt cache in this request.

        format: int32

      - `required int CacheReadInputTokens`

        Tokens read from prompt cache in this request.

        format: int32

      - `required int InputTokens`

        Input tokens consumed by this request.

        format: int32

      - `required int OutputTokens`

        Output tokens generated by this request.

        format: int32

      - `Speed? Speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `Standard`

        - `Fast`

  - `class BetaManagedAgentsSpanModelRequestStartEvent:`

    Emitted when a model request is initiated by the agent.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSpanModelRequestEndEvent:`

    Emitted when a model request completes.

    - `required string ID`

      Unique identifier for this event.

    - `required bool? IsError`

      Whether the model request resulted in an error.

    - `required string ModelRequestStartID`

      The id of the corresponding `span.model_request_start` event.

    - `required BetaManagedAgentsSpanModelUsage ModelUsage`

      Token usage for a single model request.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent:`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `required string ID`

      Unique identifier for this event.

    - `required int Iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `required string OutcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsUserDefineOutcomeEvent:`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `required string ID`

      Unique identifier for this event.

    - `required string Description`

      What the agent should produce. Copied from the input event.

    - `required int? MaxIterations`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

      format: int32

    - `required string OutcomeID`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Rubric Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric:`

        Rubric referenced by a file uploaded via the Files API.

        - `required string FileID`

          ID of the rubric file.

        - `required Type Type`

      - `class BetaManagedAgentsTextRubric:`

        Rubric content provided inline as text.

        - `required string Content`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `required Type Type`

    - `required Type Type`

  - `class BetaManagedAgentsSessionDeletedEvent:`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent:`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string SessionThreadID`

      Public sthr_ ID of the thread that started running.

    - `required Type Type`

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent:`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string SessionThreadID`

      Public sthr_ ID of the thread that went idle.

    - `required StopReason StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `class BetaManagedAgentsSessionBudgetReached:`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

    - `required Type Type`

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent:`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string SessionThreadID`

      Public sthr_ ID of the thread that terminated.

    - `required Type Type`

  - `class BetaManagedAgentsUserToolResultEvent:`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `required string ID`

      Unique identifier for this event.

    - `required string ToolUseID`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `required Type Type`

    - `IReadOnlyList<Content> Content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

    - `bool? IsError`

      Whether the tool execution resulted in an error.

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `string? SessionThreadID`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent:`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string SessionThreadID`

      Public sthr_ ID of the thread that is retrying.

    - `required Type Type`

  - `class BetaManagedAgentsSessionUpdatedEvent:`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

    - `BetaManagedAgentsSessionAgent? Agent`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `required string ID`

      - `required string? Description`

      - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

        - `required string Name`

        - `required Type Type`

        - `required string Url`

      - `required BetaManagedAgentsModelConfig Model`

        Model identifier and configuration.

        - `required BetaManagedAgentsModel ID`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `ClaudeFable5_1`

            Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

          - `ClaudeSonnet5`

            High-performance model for coding and agents

          - `ClaudeFable5`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `ClaudeOpus5`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_8`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_7`

            Powerful intelligence for long-running agents and coding

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

        - `Effort Effort`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow:`

            Low effort. Favors latency over reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortMedium:`

            Medium effort. Balances latency and reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortHigh:`

            High effort. Favors reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortXhigh:`

            Extra-high effort. Not all models accept this level.

            - `required Type Type`

          - `class BetaManagedAgentsEffortMax:`

            Maximum effort. Favors reasoning depth over latency.

            - `required Type Type`

        - `string InferenceGeo`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `Speed Speed`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `Standard`

          - `Fast`

      - `required BetaManagedAgentsSessionMultiagentCoordinator? Multiagent`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `required IReadOnlyList<Agent> Agents`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `class BetaManagedAgentsSessionThreadAgent:`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `required string ID`

            - `required string? Description`

            - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

              - `required string Name`

              - `required Type Type`

              - `required string Url`

            - `required BetaManagedAgentsModelConfig Model`

              Model identifier and configuration.

            - `required string Name`

            - `required IReadOnlyList<Skill> Skills`

              - `class BetaManagedAgentsAnthropicSkill:`

                A resolved Anthropic-managed skill.

                - `required string SkillID`

                - `required Type Type`

                - `required string Version`

              - `class BetaManagedAgentsCustomSkill:`

                A resolved user-created custom skill.

                - `required string SkillID`

                - `required Type Type`

                - `required string Version`

            - `required string? System`

            - `required IReadOnlyList<Tool> Tools`

              - `class BetaManagedAgentsAgentToolset20260401:`

                - `required IReadOnlyList<BetaManagedAgentsAgentToolConfig> Configs`

                  - `class BetaManagedAgentsBashToolConfig:`

                    Configuration for the bash tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                        - `required Type Type`

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                        - `required Type Type`

                    - `JsonElement Type constant`

                  - `class BetaManagedAgentsEditToolConfig:`

                    Configuration for the edit tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                  - `class BetaManagedAgentsReadToolConfig:`

                    Configuration for the read tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                  - `class BetaManagedAgentsWriteToolConfig:`

                    Configuration for the write tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                  - `class BetaManagedAgentsGlobToolConfig:`

                    Configuration for the glob tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                  - `class BetaManagedAgentsGrepToolConfig:`

                    Configuration for the grep tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                  - `class BetaManagedAgentsWebFetchToolConfig:`

                    Configuration for the web_fetch tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                    - `IReadOnlyList<string> AllowedDomains`

                    - `IReadOnlyList<string> BlockedDomains`

                    - `int? MaxContentTokens`

                      format: int32

                  - `class BetaManagedAgentsWebSearchToolConfig:`

                    Configuration for the web_search tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                    - `IReadOnlyList<string> AllowedDomains`

                    - `IReadOnlyList<string> BlockedDomains`

                    - `BetaManagedAgentsUserLocation? UserLocation`

                      Approximate user location for search result localization.

                      - `JsonElement Type constant`

                        Location precision. Only "approximate" is supported.

                      - `string? City`

                        City name.

                        minLength: 1, maxLength: 255

                      - `string? Country`

                        Two-letter ISO 3166-1 country code, uppercase.

                      - `string? Region`

                        Region or state name.

                        minLength: 1, maxLength: 255

                      - `string? Timezone`

                        IANA timezone identifier, e.g. "America/Los_Angeles".

                        minLength: 1, maxLength: 255

                - `required BetaManagedAgentsAgentToolsetDefaultConfig DefaultConfig`

                  Resolved default configuration for agent tools.

                  - `required bool Enabled`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `required Type Type`

              - `class BetaManagedAgentsMcpToolset:`

                - `required IReadOnlyList<BetaManagedAgentsMcpToolConfig> Configs`

                  - `required bool Enabled`

                  - `required string Name`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `required BetaManagedAgentsMcpToolsetDefaultConfig DefaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `required bool Enabled`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `required string McpServerName`

                - `required Type Type`

              - `class BetaManagedAgentsCustomTool:`

                A custom tool as returned in API responses.

                - `required string Description`

                - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

                  JSON Schema for custom tool input parameters.

                  - `JsonElement Type constant`

                  - `IReadOnlyDictionary<string, JsonElement>? Properties`

                  - `IReadOnlyList<string>? Required`

                - `required string Name`

                - `required Type Type`

            - `required Type Type`

            - `required int Version`

              format: int32

          - `class BetaManagedAgentsAdvisor:`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `required string Model`

              The advisor model id.

            - `required Type Type`

        - `required Type Type`

      - `required string Name`

      - `required IReadOnlyList<Skill> Skills`

        - `class BetaManagedAgentsAnthropicSkill:`

          A resolved Anthropic-managed skill.

        - `class BetaManagedAgentsCustomSkill:`

          A resolved user-created custom skill.

      - `required string? System`

      - `required IReadOnlyList<Tool> Tools`

        - `class BetaManagedAgentsAgentToolset20260401:`

        - `class BetaManagedAgentsMcpToolset:`

        - `class BetaManagedAgentsCustomTool:`

          A custom tool as returned in API responses.

      - `required Type Type`

      - `required int Version`

        format: int32

    - `BetaManagedAgentsBudgetLimit? Budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `required BetaMonetaryAmount MaxListCost`

        A monetary amount in a specific currency.

        - `required string Amount`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `required BetaCurrency Currency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `required Type Type`

    - `IReadOnlyDictionary<string, string> Metadata`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `string? Title`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsSystemMessageEvent:`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

      System content blocks. Text-only.

      - `required string Text`

        The text content.

        minLength: 1

      - `required Type Type`

    - `required Type Type`

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionUsageEvent:`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

    - `required BetaManagedAgentsSessionUsageSnapshot Usage`

      Point-in-time snapshot of a session's cumulative usage.

      - `double ActiveSeconds`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `BetaManagedAgentsCacheCreationUsage CacheCreation`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `int Ephemeral1hInputTokens`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `int Ephemeral5mInputTokens`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `int CacheReadInputTokens`

        Total tokens read from prompt cache.

        format: int32

      - `int InputTokens`

        Total input tokens consumed across all turns.

        format: int32

      - `BetaMonetaryAmount ListCost`

        A monetary amount in a specific currency.

      - `int OutputTokens`

        Total output tokens generated across all turns.

        format: int32

      - `BetaManagedAgentsServerToolUsage ServerToolUse`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `int WebFetchRequests`

          Number of server-executed web fetch requests.

          format: int32

        - `int WebSearchRequests`

          Number of server-executed web search requests.

          format: int32

    - `BetaManagedAgentsBudgetLimit? Budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

#### Example

```csharp
EventListParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7"
};

var page = await client.Beta.Sessions.Events.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
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

`BetaManagedAgentsSendSessionEvents Beta.Sessions.Events.Send(parameters, cancellationToken = default)`

**POST** `/v1/sessions/{session_id}/events`

Send Events

#### Parameters

- `EventSendParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `required IReadOnlyList<BetaManagedAgentsEventParams> events`

    Body param: Events to send to the `session`.

    - `class BetaManagedAgentsUserMessageEventParams:`

      Parameters for sending a user message to the session.

      - `required IReadOnlyList<Content> Content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `required string Text`

            The text content.

            minLength: 1

          - `required Type Type`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

                minLength: 1

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `required Type Type`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

              - `required string Url`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

                minLength: 1

              - `required Type Type`

          - `required Type Type`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

                minLength: 1

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `required Type Type`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

                minLength: 1

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

              - `required Type Type`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

              - `required string Url`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

                minLength: 1

              - `required Type Type`

          - `required Type Type`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

          - `required Type Type`

      - `required Type Type`

    - `class BetaManagedAgentsUserInterruptEventParams:`

      Parameters for sending an interrupt to pause the agent.

      - `required Type Type`

      - `string? SessionThreadID`

        If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

    - `class BetaManagedAgentsUserToolConfirmationEventParams:`

      Parameters for confirming or denying a tool execution request.

      - `required Result Result`

        UserToolConfirmationResult enum

        - `Allow`

        - `Deny`

      - `required string ToolUseID`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

        minLength: 1, maxLength: 128

      - `required Type Type`

      - `string? DenyMessage`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

        maxLength: 10000

    - `class BetaManagedAgentsUserCustomToolResultEventParams:`

      Parameters for providing the result of a custom tool execution.

      - `required string CustomToolUseID`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

        minLength: 1, maxLength: 128

      - `required Type Type`

      - `IReadOnlyList<Content> Content`

        The result content returned by the tool.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `class BetaManagedAgentsSearchResultBlock:`

          A block containing a web search result.

          - `required BetaManagedAgentsSearchResultCitations Citations`

            Citation settings for a search result.

            - `required bool Enabled`

              Whether citations are enabled for this search result.

          - `required IReadOnlyList<BetaManagedAgentsSearchResultContent> Content`

            Array of text content blocks from the search result.

            - `required string Text`

              The text content.

              minLength: 1

            - `required Type Type`

          - `required string Source`

            The URL source of the search result.

            minLength: 1

          - `required string Title`

            The title of the search result.

            minLength: 1

          - `required Type Type`

      - `bool? IsError`

        Whether the tool execution resulted in an error.

    - `class BetaManagedAgentsUserDefineOutcomeEventParams:`

      Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

      - `required string Description`

        What the agent should produce. This is the task specification.

      - `required Rubric Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubricParams:`

          Rubric referenced by a file uploaded via the Files API.

          - `required string FileID`

            ID of the rubric file.

          - `required Type Type`

        - `class BetaManagedAgentsTextRubricParams:`

          Rubric content provided inline as text.

          - `required string Content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

            maxLength: 262144

          - `required Type Type`

      - `required Type Type`

      - `int? MaxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `class BetaManagedAgentsUserToolResultEventParams:`

      Parameters for providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

      - `required string ToolUseID`

        The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

        minLength: 1, maxLength: 128

      - `required Type Type`

      - `IReadOnlyList<Content> Content`

        The result content returned by the tool.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `class BetaManagedAgentsSearchResultBlock:`

          A block containing a web search result.

      - `bool? IsError`

        Whether the tool execution resulted in an error.

    - `class BetaManagedAgentsSystemMessageEventParams:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

      - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

        System content blocks to append. Text-only.

        - `required string Text`

          The text content.

          minLength: 1

        - `required Type Type`

      - `required Type Type`

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

#### Returns

- `class BetaManagedAgentsSendSessionEvents:`

  Events that were successfully sent to the session.

  - `IReadOnlyList<Data> Data`

    Sent events

    - `class BetaManagedAgentsUserMessageEvent:`

      A user message event in the session conversation.

      - `required string ID`

        Unique identifier for this event.

      - `required IReadOnlyList<Content> Content`

        Array of content blocks comprising the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `required string Text`

            The text content.

            minLength: 1

          - `required Type Type`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

                minLength: 1

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `required Type Type`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

              - `required string Url`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

                minLength: 1

              - `required Type Type`

          - `required Type Type`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

                minLength: 1

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `required Type Type`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

                minLength: 1

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

              - `required Type Type`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

              - `required string Url`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

                minLength: 1

              - `required Type Type`

          - `required Type Type`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

          - `required Type Type`

      - `required Type Type`

      - `DateTimeOffset? ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

    - `class BetaManagedAgentsUserInterruptEvent:`

      An interrupt event that pauses agent execution and returns control to the user.

      - `required string ID`

        Unique identifier for this event.

      - `required Type Type`

      - `DateTimeOffset? ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `string? SessionThreadID`

        If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

    - `class BetaManagedAgentsUserToolConfirmationEvent:`

      A tool confirmation event that approves or denies a pending tool execution.

      - `required string ID`

        Unique identifier for this event.

      - `required Result Result`

        UserToolConfirmationResult enum

        - `Allow`

        - `Deny`

      - `required string ToolUseID`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `required Type Type`

      - `string? DenyMessage`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

        maxLength: 10000

      - `DateTimeOffset? ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `string? SessionThreadID`

        When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

    - `class BetaManagedAgentsUserCustomToolResultEvent:`

      Event sent by the client providing the result of a custom tool execution.

      - `required string ID`

        Unique identifier for this event.

      - `required string CustomToolUseID`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `required Type Type`

      - `IReadOnlyList<Content> Content`

        The result content returned by the tool.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `class BetaManagedAgentsSearchResultBlock:`

          A block containing a web search result.

          - `required BetaManagedAgentsSearchResultCitations Citations`

            Citation settings for a search result.

            - `required bool Enabled`

              Whether citations are enabled for this search result.

          - `required IReadOnlyList<BetaManagedAgentsSearchResultContent> Content`

            Array of text content blocks from the search result.

            - `required string Text`

              The text content.

              minLength: 1

            - `required Type Type`

          - `required string Source`

            The URL source of the search result.

            minLength: 1

          - `required string Title`

            The title of the search result.

            minLength: 1

          - `required Type Type`

      - `bool? IsError`

        Whether the tool execution resulted in an error.

      - `DateTimeOffset? ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `string? SessionThreadID`

        Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

    - `class BetaManagedAgentsUserDefineOutcomeEvent:`

      Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

      - `required string ID`

        Unique identifier for this event.

      - `required string Description`

        What the agent should produce. Copied from the input event.

      - `required int? MaxIterations`

        Evaluate-then-revise cycles before giving up. Default 3, max 20.

        format: int32

      - `required string OutcomeID`

        Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

      - `required DateTimeOffset ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required Rubric Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric:`

          Rubric referenced by a file uploaded via the Files API.

          - `required string FileID`

            ID of the rubric file.

          - `required Type Type`

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `required string Content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `required Type Type`

      - `required Type Type`

    - `class BetaManagedAgentsUserToolResultEvent:`

      Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

      - `required string ID`

        Unique identifier for this event.

      - `required string ToolUseID`

        The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `required Type Type`

      - `IReadOnlyList<Content> Content`

        The result content returned by the tool.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `class BetaManagedAgentsSearchResultBlock:`

          A block containing a web search result.

      - `bool? IsError`

        Whether the tool execution resulted in an error.

      - `DateTimeOffset? ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `string? SessionThreadID`

        Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

    - `class BetaManagedAgentsSystemMessageEvent:`

      A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

      - `required string ID`

        Unique identifier for this event.

      - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

        System content blocks. Text-only.

        - `required string Text`

          The text content.

          minLength: 1

        - `required Type Type`

      - `required Type Type`

      - `DateTimeOffset? ProcessedAt`

        A timestamp in RFC 3339 format

        format: date-time

#### Example

```csharp
EventSendParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7",
    Events =
    [
        new BetaManagedAgentsUserMessageEventParams()
        {
            Content =
            [
                new BetaManagedAgentsTextBlock()
                {
                    Text = "Where is my order #1234?",
                    Type = Type.Text,
                },
            ],
            Type = Type.UserMessage,
        },
    ],
};

var betaManagedAgentsSendSessionEvents = await client.Beta.Sessions.Events.Send(parameters);

Console.WriteLine(betaManagedAgentsSendSessionEvents);
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

`BetaManagedAgentsStreamSessionEvents Beta.Sessions.Events.StreamStreaming(parameters, cancellationToken = default)`

**GET** `/v1/sessions/{session_id}/events/stream`

Stream Events

#### Parameters

- `EventStreamParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `IReadOnlyList<BetaManagedAgentsDeltaType> eventDeltas`

    Query param: When set, this connection also receives streaming deltas (`event_start`, `event_delta`) while an event is being produced, before the event itself arrives. Deltas are best-effort; when the final event is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no final event — its terminal `span.model_request_end` closes the preview. Accepts one or more event types to preview and may be repeated: `agent.message` streams `content_delta` fragments; `agent.thinking` is start-only — a signal that the agent has begun extended thinking, concluded by the `agent.thinking` event itself. Only previews of the requested event types are sent.

    - `AgentMessage`

    - `AgentThinking`

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

#### Returns

- `class BetaManagedAgentsStreamSessionEvents: union`

  Server-sent event in the session stream.

  - `class BetaManagedAgentsUserMessageEvent:`

    A user message event in the session conversation.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<Content> Content`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `required string Text`

          The text content.

          minLength: 1

        - `required Type Type`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `required Source Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `required string Data`

              Base64-encoded image data.

              minLength: 1

            - `required string MediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

            - `required Type Type`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `required Type Type`

            - `required string Url`

              URL of the image to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

              minLength: 1

            - `required Type Type`

        - `required Type Type`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `required Source Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `required string Data`

              Base64-encoded document data.

              minLength: 1

            - `required string MediaType`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

            - `required Type Type`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `required string Data`

              The plain text content.

              minLength: 1

            - `required MediaType MediaType`

              MIME type of the text content. Must be "text/plain".

            - `required Type Type`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `required Type Type`

            - `required string Url`

              URL of the document to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

              minLength: 1

            - `required Type Type`

        - `required Type Type`

        - `string? Context`

          Additional context about the document for the model.

        - `string? Title`

          The title of the document.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

        - `required Type Type`

    - `required Type Type`

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsUserInterruptEvent:`

    An interrupt event that pauses agent execution and returns control to the user.

    - `required string ID`

      Unique identifier for this event.

    - `required Type Type`

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `string? SessionThreadID`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEvent:`

    A tool confirmation event that approves or denies a pending tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required Result Result`

      UserToolConfirmationResult enum

      - `Allow`

      - `Deny`

    - `required string ToolUseID`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `required Type Type`

    - `string? DenyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `string? SessionThreadID`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `class BetaManagedAgentsUserCustomToolResultEvent:`

    Event sent by the client providing the result of a custom tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required string CustomToolUseID`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `required Type Type`

    - `IReadOnlyList<Content> Content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

        - `required BetaManagedAgentsSearchResultCitations Citations`

          Citation settings for a search result.

          - `required bool Enabled`

            Whether citations are enabled for this search result.

        - `required IReadOnlyList<BetaManagedAgentsSearchResultContent> Content`

          Array of text content blocks from the search result.

          - `required string Text`

            The text content.

            minLength: 1

          - `required Type Type`

        - `required string Source`

          The URL source of the search result.

          minLength: 1

        - `required string Title`

          The title of the search result.

          minLength: 1

        - `required Type Type`

    - `bool? IsError`

      Whether the tool execution resulted in an error.

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `string? SessionThreadID`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsAgentCustomToolUseEvent:`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyDictionary<string, JsonElement> Input`

      Input parameters for the tool call.

    - `required string Name`

      Name of the custom tool being called.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

    - `string? SessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `class BetaManagedAgentsAgentMessageEvent:`

    An agent response event in the session conversation.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<Content> Content`

      Array of text blocks comprising the agent response.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsAgentThinkingEvent:`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsAgentMcpToolUseEvent:`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyDictionary<string, JsonElement> Input`

      Input parameters for the tool call.

    - `required string McpServerName`

      Name of the MCP server providing the tool.

    - `required string Name`

      Name of the MCP tool being used.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

    - `EvaluatedPermission EvaluatedPermission`

      AgentEvaluatedPermission enum

      - `Allow`

      - `Ask`

      - `Deny`

    - `string? SessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentMcpToolResultEvent:`

    Event representing the result of an MCP tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required string McpToolUseID`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

    - `IReadOnlyList<Content> Content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

    - `bool? IsError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent:`

    Event emitted when the agent invokes a built-in agent tool.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyDictionary<string, JsonElement> Input`

      Input parameters for the tool call.

    - `required string Name`

      Name of the agent tool being used.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

    - `EvaluatedPermission EvaluatedPermission`

      AgentEvaluatedPermission enum

      - `Allow`

      - `Ask`

      - `Deny`

    - `string? SessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentToolResultEvent:`

    Event representing the result of an agent tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string ToolUseID`

      The id of the `agent.tool_use` event this result corresponds to.

    - `required Type Type`

    - `IReadOnlyList<Content> Content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

    - `bool? IsError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadMessageReceivedEvent:`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<Content> Content`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

    - `required string FromSessionThreadID`

      Public `sthr_` ID of the thread that sent the message.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

    - `string? FromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class BetaManagedAgentsAgentThreadMessageSentEvent:`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<Content> Content`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string ToSessionThreadID`

      Public `sthr_` ID of the thread the message was sent to.

    - `required Type Type`

    - `string? ToAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent:`

    Indicates that context compaction (summarization) occurred during the session.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSessionErrorEvent:`

    An error event indicating a problem occurred during session execution.

    - `required string ID`

      Unique identifier for this event.

    - `required Error Error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError:`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `required Type Type`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `required Type Type`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `required Type Type`

        - `required Type Type`

      - `class BetaManagedAgentsModelOverloadedError:`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

      - `class BetaManagedAgentsModelRateLimitedError:`

        The model request was rate-limited.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

      - `class BetaManagedAgentsModelRequestFailedError:`

        A model request failed for a reason other than overload or rate-limiting.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

      - `class BetaManagedAgentsMcpConnectionFailedError:`

        Failed to connect to an MCP server.

        - `required string McpServerName`

          Name of the MCP server that failed to connect.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

      - `class BetaManagedAgentsMcpAuthenticationFailedError:`

        Authentication to an MCP server failed.

        - `required string McpServerName`

          Name of the MCP server that failed authentication.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

      - `class BetaManagedAgentsBillingError:`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

      - `class BetaManagedAgentsCredentialHostUnreachableError:`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `required string CredentialID`

          ID of the affected credential.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

        - `required string VaultID`

          ID of the vault containing the affected credential.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent:`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSessionStatusRunningEvent:`

    Indicates the session is actively running and the agent is working.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSessionStatusIdleEvent:`

    Indicates the agent has paused and is awaiting user input.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required StopReason StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

        - `required Type Type`

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `required IReadOnlyList<string> EventIds`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `required Type Type`

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `required Type Type`

      - `class BetaManagedAgentsSessionBudgetReached:`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `required Type Type`

    - `required Type Type`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent:`

    Indicates the session has terminated, either due to an error or completion.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSessionThreadCreatedEvent:`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the callable agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string SessionThreadID`

      Public `sthr_` ID of the newly created thread.

    - `required Type Type`

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent:`

    Emitted when an outcome evaluation cycle begins.

    - `required string ID`

      Unique identifier for this event.

    - `required int Iteration`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

      format: int32

    - `required string OutcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent:`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `required string ID`

      Unique identifier for this event.

    - `required string Explanation`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `required int Iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `required string OutcomeEvaluationStartID`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `required string OutcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string Result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `required Type Type`

    - `required BetaManagedAgentsSpanModelUsage Usage`

      Token usage for a single model request.

      - `required int CacheCreationInputTokens`

        Tokens used to create prompt cache in this request.

        format: int32

      - `required int CacheReadInputTokens`

        Tokens read from prompt cache in this request.

        format: int32

      - `required int InputTokens`

        Input tokens consumed by this request.

        format: int32

      - `required int OutputTokens`

        Output tokens generated by this request.

        format: int32

      - `Speed? Speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `Standard`

        - `Fast`

  - `class BetaManagedAgentsSpanModelRequestStartEvent:`

    Emitted when a model request is initiated by the agent.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSpanModelRequestEndEvent:`

    Emitted when a model request completes.

    - `required string ID`

      Unique identifier for this event.

    - `required bool? IsError`

      Whether the model request resulted in an error.

    - `required string ModelRequestStartID`

      The id of the corresponding `span.model_request_start` event.

    - `required BetaManagedAgentsSpanModelUsage ModelUsage`

      Token usage for a single model request.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent:`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `required string ID`

      Unique identifier for this event.

    - `required int Iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `required string OutcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsUserDefineOutcomeEvent:`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `required string ID`

      Unique identifier for this event.

    - `required string Description`

      What the agent should produce. Copied from the input event.

    - `required int? MaxIterations`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

      format: int32

    - `required string OutcomeID`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Rubric Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric:`

        Rubric referenced by a file uploaded via the Files API.

        - `required string FileID`

          ID of the rubric file.

        - `required Type Type`

      - `class BetaManagedAgentsTextRubric:`

        Rubric content provided inline as text.

        - `required string Content`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `required Type Type`

    - `required Type Type`

  - `class BetaManagedAgentsSessionDeletedEvent:`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent:`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string SessionThreadID`

      Public sthr_ ID of the thread that started running.

    - `required Type Type`

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent:`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string SessionThreadID`

      Public sthr_ ID of the thread that went idle.

    - `required StopReason StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `class BetaManagedAgentsSessionBudgetReached:`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

    - `required Type Type`

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent:`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string SessionThreadID`

      Public sthr_ ID of the thread that terminated.

    - `required Type Type`

  - `class BetaManagedAgentsUserToolResultEvent:`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `required string ID`

      Unique identifier for this event.

    - `required string ToolUseID`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `required Type Type`

    - `IReadOnlyList<Content> Content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

    - `bool? IsError`

      Whether the tool execution resulted in an error.

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `string? SessionThreadID`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent:`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string SessionThreadID`

      Public sthr_ ID of the thread that is retrying.

    - `required Type Type`

  - `class BetaManagedAgentsSessionUpdatedEvent:`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

    - `BetaManagedAgentsSessionAgent? Agent`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `required string ID`

      - `required string? Description`

      - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

        - `required string Name`

        - `required Type Type`

        - `required string Url`

      - `required BetaManagedAgentsModelConfig Model`

        Model identifier and configuration.

        - `required BetaManagedAgentsModel ID`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `ClaudeFable5_1`

            Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

          - `ClaudeSonnet5`

            High-performance model for coding and agents

          - `ClaudeFable5`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `ClaudeOpus5`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_8`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_7`

            Powerful intelligence for long-running agents and coding

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

        - `Effort Effort`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow:`

            Low effort. Favors latency over reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortMedium:`

            Medium effort. Balances latency and reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortHigh:`

            High effort. Favors reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortXhigh:`

            Extra-high effort. Not all models accept this level.

            - `required Type Type`

          - `class BetaManagedAgentsEffortMax:`

            Maximum effort. Favors reasoning depth over latency.

            - `required Type Type`

        - `string InferenceGeo`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `Speed Speed`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `Standard`

          - `Fast`

      - `required BetaManagedAgentsSessionMultiagentCoordinator? Multiagent`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `required IReadOnlyList<Agent> Agents`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `class BetaManagedAgentsSessionThreadAgent:`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `required string ID`

            - `required string? Description`

            - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

              - `required string Name`

              - `required Type Type`

              - `required string Url`

            - `required BetaManagedAgentsModelConfig Model`

              Model identifier and configuration.

            - `required string Name`

            - `required IReadOnlyList<Skill> Skills`

              - `class BetaManagedAgentsAnthropicSkill:`

                A resolved Anthropic-managed skill.

                - `required string SkillID`

                - `required Type Type`

                - `required string Version`

              - `class BetaManagedAgentsCustomSkill:`

                A resolved user-created custom skill.

                - `required string SkillID`

                - `required Type Type`

                - `required string Version`

            - `required string? System`

            - `required IReadOnlyList<Tool> Tools`

              - `class BetaManagedAgentsAgentToolset20260401:`

                - `required IReadOnlyList<BetaManagedAgentsAgentToolConfig> Configs`

                  - `class BetaManagedAgentsBashToolConfig:`

                    Configuration for the bash tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                        - `required Type Type`

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                        - `required Type Type`

                    - `JsonElement Type constant`

                  - `class BetaManagedAgentsEditToolConfig:`

                    Configuration for the edit tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                  - `class BetaManagedAgentsReadToolConfig:`

                    Configuration for the read tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                  - `class BetaManagedAgentsWriteToolConfig:`

                    Configuration for the write tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                  - `class BetaManagedAgentsGlobToolConfig:`

                    Configuration for the glob tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                  - `class BetaManagedAgentsGrepToolConfig:`

                    Configuration for the grep tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                  - `class BetaManagedAgentsWebFetchToolConfig:`

                    Configuration for the web_fetch tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                    - `IReadOnlyList<string> AllowedDomains`

                    - `IReadOnlyList<string> BlockedDomains`

                    - `int? MaxContentTokens`

                      format: int32

                  - `class BetaManagedAgentsWebSearchToolConfig:`

                    Configuration for the web_search tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                    - `IReadOnlyList<string> AllowedDomains`

                    - `IReadOnlyList<string> BlockedDomains`

                    - `BetaManagedAgentsUserLocation? UserLocation`

                      Approximate user location for search result localization.

                      - `JsonElement Type constant`

                        Location precision. Only "approximate" is supported.

                      - `string? City`

                        City name.

                        minLength: 1, maxLength: 255

                      - `string? Country`

                        Two-letter ISO 3166-1 country code, uppercase.

                      - `string? Region`

                        Region or state name.

                        minLength: 1, maxLength: 255

                      - `string? Timezone`

                        IANA timezone identifier, e.g. "America/Los_Angeles".

                        minLength: 1, maxLength: 255

                - `required BetaManagedAgentsAgentToolsetDefaultConfig DefaultConfig`

                  Resolved default configuration for agent tools.

                  - `required bool Enabled`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `required Type Type`

              - `class BetaManagedAgentsMcpToolset:`

                - `required IReadOnlyList<BetaManagedAgentsMcpToolConfig> Configs`

                  - `required bool Enabled`

                  - `required string Name`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `required BetaManagedAgentsMcpToolsetDefaultConfig DefaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `required bool Enabled`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `required string McpServerName`

                - `required Type Type`

              - `class BetaManagedAgentsCustomTool:`

                A custom tool as returned in API responses.

                - `required string Description`

                - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

                  JSON Schema for custom tool input parameters.

                  - `JsonElement Type constant`

                  - `IReadOnlyDictionary<string, JsonElement>? Properties`

                  - `IReadOnlyList<string>? Required`

                - `required string Name`

                - `required Type Type`

            - `required Type Type`

            - `required int Version`

              format: int32

          - `class BetaManagedAgentsAdvisor:`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `required string Model`

              The advisor model id.

            - `required Type Type`

        - `required Type Type`

      - `required string Name`

      - `required IReadOnlyList<Skill> Skills`

        - `class BetaManagedAgentsAnthropicSkill:`

          A resolved Anthropic-managed skill.

        - `class BetaManagedAgentsCustomSkill:`

          A resolved user-created custom skill.

      - `required string? System`

      - `required IReadOnlyList<Tool> Tools`

        - `class BetaManagedAgentsAgentToolset20260401:`

        - `class BetaManagedAgentsMcpToolset:`

        - `class BetaManagedAgentsCustomTool:`

          A custom tool as returned in API responses.

      - `required Type Type`

      - `required int Version`

        format: int32

    - `BetaManagedAgentsBudgetLimit? Budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `required BetaMonetaryAmount MaxListCost`

        A monetary amount in a specific currency.

        - `required string Amount`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `required BetaCurrency Currency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `required Type Type`

    - `IReadOnlyDictionary<string, string> Metadata`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `string? Title`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsStartEvent:`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `required BetaManagedAgentsStartEventPreview Event`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

      - `class BetaManagedAgentsAgentMessagePreview:`

        - `required string ID`

          The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

        - `required Type Type`

      - `class BetaManagedAgentsAgentThinkingPreview:`

        - `required string ID`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

        - `required Type Type`

    - `required Type Type`

  - `class BetaManagedAgentsDeltaEvent:`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `required BetaManagedAgentsDeltaContent Delta`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `required BetaManagedAgentsTextBlock Content`

        Regular text content.

      - `required Type Type`

      - `long Index`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

        format: uint32

    - `required string EventID`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

    - `required Type Type`

  - `class BetaManagedAgentsSystemMessageEvent:`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

      System content blocks. Text-only.

      - `required string Text`

        The text content.

        minLength: 1

      - `required Type Type`

    - `required Type Type`

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionUsageEvent:`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

    - `required BetaManagedAgentsSessionUsageSnapshot Usage`

      Point-in-time snapshot of a session's cumulative usage.

      - `double ActiveSeconds`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `BetaManagedAgentsCacheCreationUsage CacheCreation`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `int Ephemeral1hInputTokens`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `int Ephemeral5mInputTokens`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `int CacheReadInputTokens`

        Total tokens read from prompt cache.

        format: int32

      - `int InputTokens`

        Total input tokens consumed across all turns.

        format: int32

      - `BetaMonetaryAmount ListCost`

        A monetary amount in a specific currency.

      - `int OutputTokens`

        Total output tokens generated across all turns.

        format: int32

      - `BetaManagedAgentsServerToolUsage ServerToolUse`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `int WebFetchRequests`

          Number of server-executed web fetch requests.

          format: int32

        - `int WebSearchRequests`

          Number of server-executed web search requests.

          format: int32

    - `BetaManagedAgentsBudgetLimit? Budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

- `class BetaManagedAgentsStreamSessionEvents: union`

  Server-sent event in the session stream.

#### Example

```csharp
EventStreamParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7"
};

await foreach (var betaManagedAgentsStreamSessionEvents in client.Beta.Sessions.Events.StreamStreaming(parameters))
{
    Console.WriteLine(betaManagedAgentsStreamSessionEvents);
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

`BetaManagedAgentsFileResource Beta.Sessions.Resources.Add(parameters, cancellationToken = default)`

**POST** `/v1/sessions/{session_id}/resources`

Add Session Resource

#### Parameters

- `ResourceAddParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `required string fileID`

    Body param: ID of a previously uploaded file.

    minLength: 1, maxLength: 128

  - `required Type type`

    Body param

    - `File`

  - `string? mountPath`

    Body param: Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    minLength: 1, maxLength: 4096

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

#### Returns

- `class BetaManagedAgentsFileResource:`

  - `required string ID`

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string FileID`

  - `required string MountPath`

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

#### Example

```csharp
ResourceAddParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7",
    FileID = "file_011CNha8iCJcU1wXNR6q4V8w",
    Type = Type.File,
};

var betaManagedAgentsFileResource = await client.Beta.Sessions.Resources.Add(parameters);

Console.WriteLine(betaManagedAgentsFileResource);
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

`ResourceListPage Beta.Sessions.Resources.List(parameters, cancellationToken = default)`

**GET** `/v1/sessions/{session_id}/resources`

List Session Resources

#### Parameters

- `ResourceListParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `int limit`

    Query param: Maximum number of resources to return per page (max 1000). If omitted, returns all resources.

    format: int32

  - `string page`

    Query param: Opaque cursor from a previous response's `next_page` field.

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

#### Returns

- `class BetaManagedAgentsSessionResource: union`

  A memory store attached to an agent session.

  - `class BetaManagedAgentsGitHubRepositoryResource:`

    - `required string ID`

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string MountPath`

    - `required Type Type`

    - `required DateTimeOffset UpdatedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string Url`

    - `Checkout? Checkout`

      - `class BetaManagedAgentsBranchCheckout:`

        - `required string Name`

          Branch name to check out.

          minLength: 1, maxLength: 255

        - `required Type Type`

      - `class BetaManagedAgentsCommitCheckout:`

        - `required string Sha`

          Full commit SHA to check out.

          minLength: 7, maxLength: 64

        - `required Type Type`

  - `class BetaManagedAgentsFileResource:`

    - `required string ID`

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string FileID`

    - `required string MountPath`

    - `required Type Type`

    - `required DateTimeOffset UpdatedAt`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsMemoryStoreResource:`

    A memory store attached to an agent session.

    - `required string MemoryStoreID`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `required Type Type`

    - `Access? Access`

      Access mode for an attached memory store.

      - `ReadWrite`

      - `ReadOnly`

    - `string Description`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `string? Instructions`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      maxLength: 4096

    - `string? MountPath`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `string? Name`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

#### Example

```csharp
ResourceListParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7"
};

var page = await client.Beta.Sessions.Resources.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
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

`ResourceRetrieveResponse Beta.Sessions.Resources.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/sessions/{session_id}/resources/{resource_id}`

Get Session Resource

#### Parameters

- `ResourceRetrieveParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `required string resourceID`

    Path param: Path parameter resource_id

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

#### Returns

- `class ResourceRetrieveResponse: union`

  The requested session resource.

  - `class BetaManagedAgentsGitHubRepositoryResource:`

    - `required string ID`

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string MountPath`

    - `required Type Type`

    - `required DateTimeOffset UpdatedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string Url`

    - `Checkout? Checkout`

      - `class BetaManagedAgentsBranchCheckout:`

        - `required string Name`

          Branch name to check out.

          minLength: 1, maxLength: 255

        - `required Type Type`

      - `class BetaManagedAgentsCommitCheckout:`

        - `required string Sha`

          Full commit SHA to check out.

          minLength: 7, maxLength: 64

        - `required Type Type`

  - `class BetaManagedAgentsFileResource:`

    - `required string ID`

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string FileID`

    - `required string MountPath`

    - `required Type Type`

    - `required DateTimeOffset UpdatedAt`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsMemoryStoreResource:`

    A memory store attached to an agent session.

    - `required string MemoryStoreID`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `required Type Type`

    - `Access? Access`

      Access mode for an attached memory store.

      - `ReadWrite`

      - `ReadOnly`

    - `string Description`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `string? Instructions`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      maxLength: 4096

    - `string? MountPath`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `string? Name`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

#### Example

```csharp
ResourceRetrieveParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7",
    ResourceID = "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
};

var resource = await client.Beta.Sessions.Resources.Retrieve(parameters);

Console.WriteLine(resource);
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

`ResourceUpdateResponse Beta.Sessions.Resources.Update(parameters, cancellationToken = default)`

**POST** `/v1/sessions/{session_id}/resources/{resource_id}`

Update Session Resource

#### Parameters

- `ResourceUpdateParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `required string resourceID`

    Path param: Path parameter resource_id

  - `required string authorizationToken`

    Body param: New authorization token for the resource. Currently only `github_repository` resources support token rotation.

    minLength: 1, maxLength: 4096

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

#### Returns

- `class ResourceUpdateResponse: union`

  The updated session resource.

  - `class BetaManagedAgentsGitHubRepositoryResource:`

    - `required string ID`

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string MountPath`

    - `required Type Type`

    - `required DateTimeOffset UpdatedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string Url`

    - `Checkout? Checkout`

      - `class BetaManagedAgentsBranchCheckout:`

        - `required string Name`

          Branch name to check out.

          minLength: 1, maxLength: 255

        - `required Type Type`

      - `class BetaManagedAgentsCommitCheckout:`

        - `required string Sha`

          Full commit SHA to check out.

          minLength: 7, maxLength: 64

        - `required Type Type`

  - `class BetaManagedAgentsFileResource:`

    - `required string ID`

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string FileID`

    - `required string MountPath`

    - `required Type Type`

    - `required DateTimeOffset UpdatedAt`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsMemoryStoreResource:`

    A memory store attached to an agent session.

    - `required string MemoryStoreID`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `required Type Type`

    - `Access? Access`

      Access mode for an attached memory store.

      - `ReadWrite`

      - `ReadOnly`

    - `string Description`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `string? Instructions`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      maxLength: 4096

    - `string? MountPath`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `string? Name`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

#### Example

```csharp
ResourceUpdateParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7",
    ResourceID = "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
    AuthorizationToken = "ghp_exampletoken",
};

var resource = await client.Beta.Sessions.Resources.Update(parameters);

Console.WriteLine(resource);
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

`BetaManagedAgentsDeleteSessionResource Beta.Sessions.Resources.Delete(parameters, cancellationToken = default)`

**DELETE** `/v1/sessions/{session_id}/resources/{resource_id}`

Delete Session Resource

#### Parameters

- `ResourceDeleteParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `required string resourceID`

    Path param: Path parameter resource_id

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

#### Returns

- `class BetaManagedAgentsDeleteSessionResource:`

  Confirmation of resource deletion.

  - `required string ID`

  - `required Type Type`

#### Example

```csharp
ResourceDeleteParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7",
    ResourceID = "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
};

var betaManagedAgentsDeleteSessionResource = await client.Beta.Sessions.Resources.Delete(parameters);

Console.WriteLine(betaManagedAgentsDeleteSessionResource);
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

`ThreadListPage Beta.Sessions.Threads.List(parameters, cancellationToken = default)`

**GET** `/v1/sessions/{session_id}/threads`

List Session Threads

#### Parameters

- `ThreadListParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `int limit`

    Query param: Maximum results per page. Defaults to 1000.

    format: int32

  - `string page`

    Query param: Opaque pagination cursor from a previous response's `next_page`. Forward-only.

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

#### Returns

- `class BetaManagedAgentsSessionThread:`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `required string ID`

    Unique identifier for this thread.

  - `required Agent Agent`

    The resolved agent a session thread runs: a saved-agent snapshot, the platform advisor entry, or an inline-defined (ephemeral) agent snapshot.

    - `class BetaManagedAgentsSessionThreadAgent:`

      Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

      - `required string ID`

      - `required string? Description`

      - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

        - `required string Name`

        - `required Type Type`

        - `required string Url`

      - `required BetaManagedAgentsModelConfig Model`

        Model identifier and configuration.

        - `required BetaManagedAgentsModel ID`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `ClaudeFable5_1`

            Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

          - `ClaudeSonnet5`

            High-performance model for coding and agents

          - `ClaudeFable5`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `ClaudeOpus5`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_8`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_7`

            Powerful intelligence for long-running agents and coding

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

        - `Effort Effort`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow:`

            Low effort. Favors latency over reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortMedium:`

            Medium effort. Balances latency and reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortHigh:`

            High effort. Favors reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortXhigh:`

            Extra-high effort. Not all models accept this level.

            - `required Type Type`

          - `class BetaManagedAgentsEffortMax:`

            Maximum effort. Favors reasoning depth over latency.

            - `required Type Type`

        - `string InferenceGeo`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `Speed Speed`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `Standard`

          - `Fast`

      - `required string Name`

      - `required IReadOnlyList<Skill> Skills`

        - `class BetaManagedAgentsAnthropicSkill:`

          A resolved Anthropic-managed skill.

          - `required string SkillID`

          - `required Type Type`

          - `required string Version`

        - `class BetaManagedAgentsCustomSkill:`

          A resolved user-created custom skill.

          - `required string SkillID`

          - `required Type Type`

          - `required string Version`

      - `required string? System`

      - `required IReadOnlyList<Tool> Tools`

        - `class BetaManagedAgentsAgentToolset20260401:`

          - `required IReadOnlyList<BetaManagedAgentsAgentToolConfig> Configs`

            - `class BetaManagedAgentsBashToolConfig:`

              Configuration for the bash tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                  - `required Type Type`

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

                  - `required Type Type`

              - `JsonElement Type constant`

            - `class BetaManagedAgentsEditToolConfig:`

              Configuration for the edit tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

            - `class BetaManagedAgentsReadToolConfig:`

              Configuration for the read tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

            - `class BetaManagedAgentsWriteToolConfig:`

              Configuration for the write tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

            - `class BetaManagedAgentsGlobToolConfig:`

              Configuration for the glob tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

            - `class BetaManagedAgentsGrepToolConfig:`

              Configuration for the grep tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

            - `class BetaManagedAgentsWebFetchToolConfig:`

              Configuration for the web_fetch tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

              - `IReadOnlyList<string> AllowedDomains`

              - `IReadOnlyList<string> BlockedDomains`

              - `int? MaxContentTokens`

                format: int32

            - `class BetaManagedAgentsWebSearchToolConfig:`

              Configuration for the web_search tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

              - `IReadOnlyList<string> AllowedDomains`

              - `IReadOnlyList<string> BlockedDomains`

              - `BetaManagedAgentsUserLocation? UserLocation`

                Approximate user location for search result localization.

                - `JsonElement Type constant`

                  Location precision. Only "approximate" is supported.

                - `string? City`

                  City name.

                  minLength: 1, maxLength: 255

                - `string? Country`

                  Two-letter ISO 3166-1 country code, uppercase.

                - `string? Region`

                  Region or state name.

                  minLength: 1, maxLength: 255

                - `string? Timezone`

                  IANA timezone identifier, e.g. "America/Los_Angeles".

                  minLength: 1, maxLength: 255

          - `required BetaManagedAgentsAgentToolsetDefaultConfig DefaultConfig`

            Resolved default configuration for agent tools.

            - `required bool Enabled`

            - `required PermissionPolicy PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `required Type Type`

        - `class BetaManagedAgentsMcpToolset:`

          - `required IReadOnlyList<BetaManagedAgentsMcpToolConfig> Configs`

            - `required bool Enabled`

            - `required string Name`

            - `required PermissionPolicy PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `required BetaManagedAgentsMcpToolsetDefaultConfig DefaultConfig`

            Resolved default configuration for all tools from an MCP server.

            - `required bool Enabled`

            - `required PermissionPolicy PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `required string McpServerName`

          - `required Type Type`

        - `class BetaManagedAgentsCustomTool:`

          A custom tool as returned in API responses.

          - `required string Description`

          - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

            JSON Schema for custom tool input parameters.

            - `JsonElement Type constant`

            - `IReadOnlyDictionary<string, JsonElement>? Properties`

            - `IReadOnlyList<string>? Required`

          - `required string Name`

          - `required Type Type`

      - `required Type Type`

      - `required int Version`

        format: int32

    - `class BetaManagedAgentsAdvisor:`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `required string Model`

        The advisor model id.

      - `required Type Type`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string? ParentThreadID`

    Parent thread that spawned this thread. Null for the primary thread.

  - `required string SessionID`

    The session this thread belongs to.

  - `required BetaManagedAgentsSessionThreadStats? Stats`

    Timing statistics for a session thread.

    - `double ActiveSeconds`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

      format: double

    - `double DurationSeconds`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

      format: double

    - `double StartupSeconds`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

      format: double

  - `required BetaManagedAgentsSessionThreadStatus Status`

    SessionThreadStatus enum

    - `Running`

    - `Idle`

    - `Rescheduling`

    - `Terminated`

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required BetaManagedAgentsSessionThreadUsage? Usage`

    Cumulative token usage for a session thread across all turns.

    - `double ActiveSeconds`

      Cumulative time in seconds this thread spent in running status. Equal to `stats.active_seconds`; surfaced here so a thread's usage carries every quantity its cost is priced on.

      format: double

    - `BetaManagedAgentsCacheCreationUsage CacheCreation`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `int Ephemeral1hInputTokens`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `int Ephemeral5mInputTokens`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `int CacheReadInputTokens`

      Total tokens read from prompt cache.

      format: int32

    - `int InputTokens`

      Total input tokens consumed across all turns.

      format: int32

    - `BetaMonetaryAmount? ListCost`

      A monetary amount in a specific currency.

      - `required string Amount`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `required BetaCurrency Currency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `int OutputTokens`

      Total output tokens generated across all turns.

      format: int32

    - `BetaManagedAgentsServerToolUsage? ServerToolUse`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `int WebFetchRequests`

        Number of server-executed web fetch requests.

        format: int32

      - `int WebSearchRequests`

        Number of server-executed web search requests.

        format: int32

#### Example

```csharp
ThreadListParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7"
};

var page = await client.Beta.Sessions.Threads.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
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

`BetaManagedAgentsSessionThread Beta.Sessions.Threads.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}`

Get Session Thread

#### Parameters

- `ThreadRetrieveParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `required string threadID`

    Path param: Path parameter thread_id

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

#### Returns

- `class BetaManagedAgentsSessionThread:`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `required string ID`

    Unique identifier for this thread.

  - `required Agent Agent`

    The resolved agent a session thread runs: a saved-agent snapshot, the platform advisor entry, or an inline-defined (ephemeral) agent snapshot.

    - `class BetaManagedAgentsSessionThreadAgent:`

      Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

      - `required string ID`

      - `required string? Description`

      - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

        - `required string Name`

        - `required Type Type`

        - `required string Url`

      - `required BetaManagedAgentsModelConfig Model`

        Model identifier and configuration.

        - `required BetaManagedAgentsModel ID`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `ClaudeFable5_1`

            Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

          - `ClaudeSonnet5`

            High-performance model for coding and agents

          - `ClaudeFable5`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `ClaudeOpus5`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_8`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_7`

            Powerful intelligence for long-running agents and coding

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

        - `Effort Effort`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow:`

            Low effort. Favors latency over reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortMedium:`

            Medium effort. Balances latency and reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortHigh:`

            High effort. Favors reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortXhigh:`

            Extra-high effort. Not all models accept this level.

            - `required Type Type`

          - `class BetaManagedAgentsEffortMax:`

            Maximum effort. Favors reasoning depth over latency.

            - `required Type Type`

        - `string InferenceGeo`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `Speed Speed`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `Standard`

          - `Fast`

      - `required string Name`

      - `required IReadOnlyList<Skill> Skills`

        - `class BetaManagedAgentsAnthropicSkill:`

          A resolved Anthropic-managed skill.

          - `required string SkillID`

          - `required Type Type`

          - `required string Version`

        - `class BetaManagedAgentsCustomSkill:`

          A resolved user-created custom skill.

          - `required string SkillID`

          - `required Type Type`

          - `required string Version`

      - `required string? System`

      - `required IReadOnlyList<Tool> Tools`

        - `class BetaManagedAgentsAgentToolset20260401:`

          - `required IReadOnlyList<BetaManagedAgentsAgentToolConfig> Configs`

            - `class BetaManagedAgentsBashToolConfig:`

              Configuration for the bash tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                  - `required Type Type`

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

                  - `required Type Type`

              - `JsonElement Type constant`

            - `class BetaManagedAgentsEditToolConfig:`

              Configuration for the edit tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

            - `class BetaManagedAgentsReadToolConfig:`

              Configuration for the read tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

            - `class BetaManagedAgentsWriteToolConfig:`

              Configuration for the write tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

            - `class BetaManagedAgentsGlobToolConfig:`

              Configuration for the glob tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

            - `class BetaManagedAgentsGrepToolConfig:`

              Configuration for the grep tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

            - `class BetaManagedAgentsWebFetchToolConfig:`

              Configuration for the web_fetch tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

              - `IReadOnlyList<string> AllowedDomains`

              - `IReadOnlyList<string> BlockedDomains`

              - `int? MaxContentTokens`

                format: int32

            - `class BetaManagedAgentsWebSearchToolConfig:`

              Configuration for the web_search tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

              - `IReadOnlyList<string> AllowedDomains`

              - `IReadOnlyList<string> BlockedDomains`

              - `BetaManagedAgentsUserLocation? UserLocation`

                Approximate user location for search result localization.

                - `JsonElement Type constant`

                  Location precision. Only "approximate" is supported.

                - `string? City`

                  City name.

                  minLength: 1, maxLength: 255

                - `string? Country`

                  Two-letter ISO 3166-1 country code, uppercase.

                - `string? Region`

                  Region or state name.

                  minLength: 1, maxLength: 255

                - `string? Timezone`

                  IANA timezone identifier, e.g. "America/Los_Angeles".

                  minLength: 1, maxLength: 255

          - `required BetaManagedAgentsAgentToolsetDefaultConfig DefaultConfig`

            Resolved default configuration for agent tools.

            - `required bool Enabled`

            - `required PermissionPolicy PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `required Type Type`

        - `class BetaManagedAgentsMcpToolset:`

          - `required IReadOnlyList<BetaManagedAgentsMcpToolConfig> Configs`

            - `required bool Enabled`

            - `required string Name`

            - `required PermissionPolicy PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `required BetaManagedAgentsMcpToolsetDefaultConfig DefaultConfig`

            Resolved default configuration for all tools from an MCP server.

            - `required bool Enabled`

            - `required PermissionPolicy PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `required string McpServerName`

          - `required Type Type`

        - `class BetaManagedAgentsCustomTool:`

          A custom tool as returned in API responses.

          - `required string Description`

          - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

            JSON Schema for custom tool input parameters.

            - `JsonElement Type constant`

            - `IReadOnlyDictionary<string, JsonElement>? Properties`

            - `IReadOnlyList<string>? Required`

          - `required string Name`

          - `required Type Type`

      - `required Type Type`

      - `required int Version`

        format: int32

    - `class BetaManagedAgentsAdvisor:`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `required string Model`

        The advisor model id.

      - `required Type Type`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string? ParentThreadID`

    Parent thread that spawned this thread. Null for the primary thread.

  - `required string SessionID`

    The session this thread belongs to.

  - `required BetaManagedAgentsSessionThreadStats? Stats`

    Timing statistics for a session thread.

    - `double ActiveSeconds`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

      format: double

    - `double DurationSeconds`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

      format: double

    - `double StartupSeconds`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

      format: double

  - `required BetaManagedAgentsSessionThreadStatus Status`

    SessionThreadStatus enum

    - `Running`

    - `Idle`

    - `Rescheduling`

    - `Terminated`

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required BetaManagedAgentsSessionThreadUsage? Usage`

    Cumulative token usage for a session thread across all turns.

    - `double ActiveSeconds`

      Cumulative time in seconds this thread spent in running status. Equal to `stats.active_seconds`; surfaced here so a thread's usage carries every quantity its cost is priced on.

      format: double

    - `BetaManagedAgentsCacheCreationUsage CacheCreation`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `int Ephemeral1hInputTokens`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `int Ephemeral5mInputTokens`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `int CacheReadInputTokens`

      Total tokens read from prompt cache.

      format: int32

    - `int InputTokens`

      Total input tokens consumed across all turns.

      format: int32

    - `BetaMonetaryAmount? ListCost`

      A monetary amount in a specific currency.

      - `required string Amount`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `required BetaCurrency Currency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `int OutputTokens`

      Total output tokens generated across all turns.

      format: int32

    - `BetaManagedAgentsServerToolUsage? ServerToolUse`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `int WebFetchRequests`

        Number of server-executed web fetch requests.

        format: int32

      - `int WebSearchRequests`

        Number of server-executed web search requests.

        format: int32

#### Example

```csharp
ThreadRetrieveParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7",
    ThreadID = "sthr_011CZkZVWa6oIjw0rgXZpnBt",
};

var betaManagedAgentsSessionThread = await client.Beta.Sessions.Threads.Retrieve(parameters);

Console.WriteLine(betaManagedAgentsSessionThread);
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

`BetaManagedAgentsSessionThread Beta.Sessions.Threads.Archive(parameters, cancellationToken = default)`

**POST** `/v1/sessions/{session_id}/threads/{thread_id}/archive`

Archive Session Thread

#### Parameters

- `ThreadArchiveParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `required string threadID`

    Path param: Path parameter thread_id

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

#### Returns

- `class BetaManagedAgentsSessionThread:`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `required string ID`

    Unique identifier for this thread.

  - `required Agent Agent`

    The resolved agent a session thread runs: a saved-agent snapshot, the platform advisor entry, or an inline-defined (ephemeral) agent snapshot.

    - `class BetaManagedAgentsSessionThreadAgent:`

      Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

      - `required string ID`

      - `required string? Description`

      - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

        - `required string Name`

        - `required Type Type`

        - `required string Url`

      - `required BetaManagedAgentsModelConfig Model`

        Model identifier and configuration.

        - `required BetaManagedAgentsModel ID`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `ClaudeFable5_1`

            Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

          - `ClaudeSonnet5`

            High-performance model for coding and agents

          - `ClaudeFable5`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `ClaudeOpus5`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_8`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_7`

            Powerful intelligence for long-running agents and coding

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

        - `Effort Effort`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow:`

            Low effort. Favors latency over reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortMedium:`

            Medium effort. Balances latency and reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortHigh:`

            High effort. Favors reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortXhigh:`

            Extra-high effort. Not all models accept this level.

            - `required Type Type`

          - `class BetaManagedAgentsEffortMax:`

            Maximum effort. Favors reasoning depth over latency.

            - `required Type Type`

        - `string InferenceGeo`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `Speed Speed`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `Standard`

          - `Fast`

      - `required string Name`

      - `required IReadOnlyList<Skill> Skills`

        - `class BetaManagedAgentsAnthropicSkill:`

          A resolved Anthropic-managed skill.

          - `required string SkillID`

          - `required Type Type`

          - `required string Version`

        - `class BetaManagedAgentsCustomSkill:`

          A resolved user-created custom skill.

          - `required string SkillID`

          - `required Type Type`

          - `required string Version`

      - `required string? System`

      - `required IReadOnlyList<Tool> Tools`

        - `class BetaManagedAgentsAgentToolset20260401:`

          - `required IReadOnlyList<BetaManagedAgentsAgentToolConfig> Configs`

            - `class BetaManagedAgentsBashToolConfig:`

              Configuration for the bash tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                  - `required Type Type`

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

                  - `required Type Type`

              - `JsonElement Type constant`

            - `class BetaManagedAgentsEditToolConfig:`

              Configuration for the edit tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

            - `class BetaManagedAgentsReadToolConfig:`

              Configuration for the read tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

            - `class BetaManagedAgentsWriteToolConfig:`

              Configuration for the write tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

            - `class BetaManagedAgentsGlobToolConfig:`

              Configuration for the glob tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

            - `class BetaManagedAgentsGrepToolConfig:`

              Configuration for the grep tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

            - `class BetaManagedAgentsWebFetchToolConfig:`

              Configuration for the web_fetch tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

              - `IReadOnlyList<string> AllowedDomains`

              - `IReadOnlyList<string> BlockedDomains`

              - `int? MaxContentTokens`

                format: int32

            - `class BetaManagedAgentsWebSearchToolConfig:`

              Configuration for the web_search tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

              - `IReadOnlyList<string> AllowedDomains`

              - `IReadOnlyList<string> BlockedDomains`

              - `BetaManagedAgentsUserLocation? UserLocation`

                Approximate user location for search result localization.

                - `JsonElement Type constant`

                  Location precision. Only "approximate" is supported.

                - `string? City`

                  City name.

                  minLength: 1, maxLength: 255

                - `string? Country`

                  Two-letter ISO 3166-1 country code, uppercase.

                - `string? Region`

                  Region or state name.

                  minLength: 1, maxLength: 255

                - `string? Timezone`

                  IANA timezone identifier, e.g. "America/Los_Angeles".

                  minLength: 1, maxLength: 255

          - `required BetaManagedAgentsAgentToolsetDefaultConfig DefaultConfig`

            Resolved default configuration for agent tools.

            - `required bool Enabled`

            - `required PermissionPolicy PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `required Type Type`

        - `class BetaManagedAgentsMcpToolset:`

          - `required IReadOnlyList<BetaManagedAgentsMcpToolConfig> Configs`

            - `required bool Enabled`

            - `required string Name`

            - `required PermissionPolicy PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `required BetaManagedAgentsMcpToolsetDefaultConfig DefaultConfig`

            Resolved default configuration for all tools from an MCP server.

            - `required bool Enabled`

            - `required PermissionPolicy PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `required string McpServerName`

          - `required Type Type`

        - `class BetaManagedAgentsCustomTool:`

          A custom tool as returned in API responses.

          - `required string Description`

          - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

            JSON Schema for custom tool input parameters.

            - `JsonElement Type constant`

            - `IReadOnlyDictionary<string, JsonElement>? Properties`

            - `IReadOnlyList<string>? Required`

          - `required string Name`

          - `required Type Type`

      - `required Type Type`

      - `required int Version`

        format: int32

    - `class BetaManagedAgentsAdvisor:`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `required string Model`

        The advisor model id.

      - `required Type Type`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string? ParentThreadID`

    Parent thread that spawned this thread. Null for the primary thread.

  - `required string SessionID`

    The session this thread belongs to.

  - `required BetaManagedAgentsSessionThreadStats? Stats`

    Timing statistics for a session thread.

    - `double ActiveSeconds`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

      format: double

    - `double DurationSeconds`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

      format: double

    - `double StartupSeconds`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

      format: double

  - `required BetaManagedAgentsSessionThreadStatus Status`

    SessionThreadStatus enum

    - `Running`

    - `Idle`

    - `Rescheduling`

    - `Terminated`

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required BetaManagedAgentsSessionThreadUsage? Usage`

    Cumulative token usage for a session thread across all turns.

    - `double ActiveSeconds`

      Cumulative time in seconds this thread spent in running status. Equal to `stats.active_seconds`; surfaced here so a thread's usage carries every quantity its cost is priced on.

      format: double

    - `BetaManagedAgentsCacheCreationUsage CacheCreation`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `int Ephemeral1hInputTokens`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `int Ephemeral5mInputTokens`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `int CacheReadInputTokens`

      Total tokens read from prompt cache.

      format: int32

    - `int InputTokens`

      Total input tokens consumed across all turns.

      format: int32

    - `BetaMonetaryAmount? ListCost`

      A monetary amount in a specific currency.

      - `required string Amount`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `required BetaCurrency Currency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `int OutputTokens`

      Total output tokens generated across all turns.

      format: int32

    - `BetaManagedAgentsServerToolUsage? ServerToolUse`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `int WebFetchRequests`

        Number of server-executed web fetch requests.

        format: int32

      - `int WebSearchRequests`

        Number of server-executed web search requests.

        format: int32

#### Example

```csharp
ThreadArchiveParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7",
    ThreadID = "sthr_011CZkZVWa6oIjw0rgXZpnBt",
};

var betaManagedAgentsSessionThread = await client.Beta.Sessions.Threads.Archive(parameters);

Console.WriteLine(betaManagedAgentsSessionThread);
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

`EventListPage Beta.Sessions.Threads.Events.List(parameters, cancellationToken = default)`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}/events`

List Session Thread Events

#### Parameters

- `EventListParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `required string threadID`

    Path param: Path parameter thread_id

  - `int limit`

    Query param: Query parameter for limit

    format: int32

  - `string page`

    Query param: Query parameter for page

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

#### Returns

- `class BetaManagedAgentsSessionEvent: union`

  Union type for all event types in a session.

  - `class BetaManagedAgentsUserMessageEvent:`

    A user message event in the session conversation.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<Content> Content`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `required string Text`

          The text content.

          minLength: 1

        - `required Type Type`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `required Source Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `required string Data`

              Base64-encoded image data.

              minLength: 1

            - `required string MediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

            - `required Type Type`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `required Type Type`

            - `required string Url`

              URL of the image to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

              minLength: 1

            - `required Type Type`

        - `required Type Type`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `required Source Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `required string Data`

              Base64-encoded document data.

              minLength: 1

            - `required string MediaType`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

            - `required Type Type`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `required string Data`

              The plain text content.

              minLength: 1

            - `required MediaType MediaType`

              MIME type of the text content. Must be "text/plain".

            - `required Type Type`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `required Type Type`

            - `required string Url`

              URL of the document to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

              minLength: 1

            - `required Type Type`

        - `required Type Type`

        - `string? Context`

          Additional context about the document for the model.

        - `string? Title`

          The title of the document.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

        - `required Type Type`

    - `required Type Type`

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsUserInterruptEvent:`

    An interrupt event that pauses agent execution and returns control to the user.

    - `required string ID`

      Unique identifier for this event.

    - `required Type Type`

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `string? SessionThreadID`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEvent:`

    A tool confirmation event that approves or denies a pending tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required Result Result`

      UserToolConfirmationResult enum

      - `Allow`

      - `Deny`

    - `required string ToolUseID`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `required Type Type`

    - `string? DenyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `string? SessionThreadID`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `class BetaManagedAgentsUserCustomToolResultEvent:`

    Event sent by the client providing the result of a custom tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required string CustomToolUseID`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `required Type Type`

    - `IReadOnlyList<Content> Content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

        - `required BetaManagedAgentsSearchResultCitations Citations`

          Citation settings for a search result.

          - `required bool Enabled`

            Whether citations are enabled for this search result.

        - `required IReadOnlyList<BetaManagedAgentsSearchResultContent> Content`

          Array of text content blocks from the search result.

          - `required string Text`

            The text content.

            minLength: 1

          - `required Type Type`

        - `required string Source`

          The URL source of the search result.

          minLength: 1

        - `required string Title`

          The title of the search result.

          minLength: 1

        - `required Type Type`

    - `bool? IsError`

      Whether the tool execution resulted in an error.

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `string? SessionThreadID`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsAgentCustomToolUseEvent:`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyDictionary<string, JsonElement> Input`

      Input parameters for the tool call.

    - `required string Name`

      Name of the custom tool being called.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

    - `string? SessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `class BetaManagedAgentsAgentMessageEvent:`

    An agent response event in the session conversation.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<Content> Content`

      Array of text blocks comprising the agent response.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsAgentThinkingEvent:`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsAgentMcpToolUseEvent:`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyDictionary<string, JsonElement> Input`

      Input parameters for the tool call.

    - `required string McpServerName`

      Name of the MCP server providing the tool.

    - `required string Name`

      Name of the MCP tool being used.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

    - `EvaluatedPermission EvaluatedPermission`

      AgentEvaluatedPermission enum

      - `Allow`

      - `Ask`

      - `Deny`

    - `string? SessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentMcpToolResultEvent:`

    Event representing the result of an MCP tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required string McpToolUseID`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

    - `IReadOnlyList<Content> Content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

    - `bool? IsError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent:`

    Event emitted when the agent invokes a built-in agent tool.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyDictionary<string, JsonElement> Input`

      Input parameters for the tool call.

    - `required string Name`

      Name of the agent tool being used.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

    - `EvaluatedPermission EvaluatedPermission`

      AgentEvaluatedPermission enum

      - `Allow`

      - `Ask`

      - `Deny`

    - `string? SessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentToolResultEvent:`

    Event representing the result of an agent tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string ToolUseID`

      The id of the `agent.tool_use` event this result corresponds to.

    - `required Type Type`

    - `IReadOnlyList<Content> Content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

    - `bool? IsError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadMessageReceivedEvent:`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<Content> Content`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

    - `required string FromSessionThreadID`

      Public `sthr_` ID of the thread that sent the message.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

    - `string? FromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class BetaManagedAgentsAgentThreadMessageSentEvent:`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<Content> Content`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string ToSessionThreadID`

      Public `sthr_` ID of the thread the message was sent to.

    - `required Type Type`

    - `string? ToAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent:`

    Indicates that context compaction (summarization) occurred during the session.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSessionErrorEvent:`

    An error event indicating a problem occurred during session execution.

    - `required string ID`

      Unique identifier for this event.

    - `required Error Error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError:`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `required Type Type`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `required Type Type`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `required Type Type`

        - `required Type Type`

      - `class BetaManagedAgentsModelOverloadedError:`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

      - `class BetaManagedAgentsModelRateLimitedError:`

        The model request was rate-limited.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

      - `class BetaManagedAgentsModelRequestFailedError:`

        A model request failed for a reason other than overload or rate-limiting.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

      - `class BetaManagedAgentsMcpConnectionFailedError:`

        Failed to connect to an MCP server.

        - `required string McpServerName`

          Name of the MCP server that failed to connect.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

      - `class BetaManagedAgentsMcpAuthenticationFailedError:`

        Authentication to an MCP server failed.

        - `required string McpServerName`

          Name of the MCP server that failed authentication.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

      - `class BetaManagedAgentsBillingError:`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

      - `class BetaManagedAgentsCredentialHostUnreachableError:`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `required string CredentialID`

          ID of the affected credential.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

        - `required string VaultID`

          ID of the vault containing the affected credential.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent:`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSessionStatusRunningEvent:`

    Indicates the session is actively running and the agent is working.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSessionStatusIdleEvent:`

    Indicates the agent has paused and is awaiting user input.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required StopReason StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

        - `required Type Type`

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `required IReadOnlyList<string> EventIds`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `required Type Type`

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `required Type Type`

      - `class BetaManagedAgentsSessionBudgetReached:`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `required Type Type`

    - `required Type Type`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent:`

    Indicates the session has terminated, either due to an error or completion.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSessionThreadCreatedEvent:`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the callable agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string SessionThreadID`

      Public `sthr_` ID of the newly created thread.

    - `required Type Type`

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent:`

    Emitted when an outcome evaluation cycle begins.

    - `required string ID`

      Unique identifier for this event.

    - `required int Iteration`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

      format: int32

    - `required string OutcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent:`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `required string ID`

      Unique identifier for this event.

    - `required string Explanation`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `required int Iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `required string OutcomeEvaluationStartID`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `required string OutcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string Result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `required Type Type`

    - `required BetaManagedAgentsSpanModelUsage Usage`

      Token usage for a single model request.

      - `required int CacheCreationInputTokens`

        Tokens used to create prompt cache in this request.

        format: int32

      - `required int CacheReadInputTokens`

        Tokens read from prompt cache in this request.

        format: int32

      - `required int InputTokens`

        Input tokens consumed by this request.

        format: int32

      - `required int OutputTokens`

        Output tokens generated by this request.

        format: int32

      - `Speed? Speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `Standard`

        - `Fast`

  - `class BetaManagedAgentsSpanModelRequestStartEvent:`

    Emitted when a model request is initiated by the agent.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSpanModelRequestEndEvent:`

    Emitted when a model request completes.

    - `required string ID`

      Unique identifier for this event.

    - `required bool? IsError`

      Whether the model request resulted in an error.

    - `required string ModelRequestStartID`

      The id of the corresponding `span.model_request_start` event.

    - `required BetaManagedAgentsSpanModelUsage ModelUsage`

      Token usage for a single model request.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent:`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `required string ID`

      Unique identifier for this event.

    - `required int Iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `required string OutcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsUserDefineOutcomeEvent:`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `required string ID`

      Unique identifier for this event.

    - `required string Description`

      What the agent should produce. Copied from the input event.

    - `required int? MaxIterations`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

      format: int32

    - `required string OutcomeID`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Rubric Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric:`

        Rubric referenced by a file uploaded via the Files API.

        - `required string FileID`

          ID of the rubric file.

        - `required Type Type`

      - `class BetaManagedAgentsTextRubric:`

        Rubric content provided inline as text.

        - `required string Content`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `required Type Type`

    - `required Type Type`

  - `class BetaManagedAgentsSessionDeletedEvent:`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent:`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string SessionThreadID`

      Public sthr_ ID of the thread that started running.

    - `required Type Type`

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent:`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string SessionThreadID`

      Public sthr_ ID of the thread that went idle.

    - `required StopReason StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `class BetaManagedAgentsSessionBudgetReached:`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

    - `required Type Type`

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent:`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string SessionThreadID`

      Public sthr_ ID of the thread that terminated.

    - `required Type Type`

  - `class BetaManagedAgentsUserToolResultEvent:`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `required string ID`

      Unique identifier for this event.

    - `required string ToolUseID`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `required Type Type`

    - `IReadOnlyList<Content> Content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

    - `bool? IsError`

      Whether the tool execution resulted in an error.

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `string? SessionThreadID`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent:`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string SessionThreadID`

      Public sthr_ ID of the thread that is retrying.

    - `required Type Type`

  - `class BetaManagedAgentsSessionUpdatedEvent:`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

    - `BetaManagedAgentsSessionAgent? Agent`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `required string ID`

      - `required string? Description`

      - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

        - `required string Name`

        - `required Type Type`

        - `required string Url`

      - `required BetaManagedAgentsModelConfig Model`

        Model identifier and configuration.

        - `required BetaManagedAgentsModel ID`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `ClaudeFable5_1`

            Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

          - `ClaudeSonnet5`

            High-performance model for coding and agents

          - `ClaudeFable5`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `ClaudeOpus5`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_8`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_7`

            Powerful intelligence for long-running agents and coding

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

        - `Effort Effort`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow:`

            Low effort. Favors latency over reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortMedium:`

            Medium effort. Balances latency and reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortHigh:`

            High effort. Favors reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortXhigh:`

            Extra-high effort. Not all models accept this level.

            - `required Type Type`

          - `class BetaManagedAgentsEffortMax:`

            Maximum effort. Favors reasoning depth over latency.

            - `required Type Type`

        - `string InferenceGeo`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `Speed Speed`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `Standard`

          - `Fast`

      - `required BetaManagedAgentsSessionMultiagentCoordinator? Multiagent`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `required IReadOnlyList<Agent> Agents`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `class BetaManagedAgentsSessionThreadAgent:`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `required string ID`

            - `required string? Description`

            - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

              - `required string Name`

              - `required Type Type`

              - `required string Url`

            - `required BetaManagedAgentsModelConfig Model`

              Model identifier and configuration.

            - `required string Name`

            - `required IReadOnlyList<Skill> Skills`

              - `class BetaManagedAgentsAnthropicSkill:`

                A resolved Anthropic-managed skill.

                - `required string SkillID`

                - `required Type Type`

                - `required string Version`

              - `class BetaManagedAgentsCustomSkill:`

                A resolved user-created custom skill.

                - `required string SkillID`

                - `required Type Type`

                - `required string Version`

            - `required string? System`

            - `required IReadOnlyList<Tool> Tools`

              - `class BetaManagedAgentsAgentToolset20260401:`

                - `required IReadOnlyList<BetaManagedAgentsAgentToolConfig> Configs`

                  - `class BetaManagedAgentsBashToolConfig:`

                    Configuration for the bash tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                        - `required Type Type`

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                        - `required Type Type`

                    - `JsonElement Type constant`

                  - `class BetaManagedAgentsEditToolConfig:`

                    Configuration for the edit tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                  - `class BetaManagedAgentsReadToolConfig:`

                    Configuration for the read tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                  - `class BetaManagedAgentsWriteToolConfig:`

                    Configuration for the write tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                  - `class BetaManagedAgentsGlobToolConfig:`

                    Configuration for the glob tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                  - `class BetaManagedAgentsGrepToolConfig:`

                    Configuration for the grep tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                  - `class BetaManagedAgentsWebFetchToolConfig:`

                    Configuration for the web_fetch tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                    - `IReadOnlyList<string> AllowedDomains`

                    - `IReadOnlyList<string> BlockedDomains`

                    - `int? MaxContentTokens`

                      format: int32

                  - `class BetaManagedAgentsWebSearchToolConfig:`

                    Configuration for the web_search tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                    - `IReadOnlyList<string> AllowedDomains`

                    - `IReadOnlyList<string> BlockedDomains`

                    - `BetaManagedAgentsUserLocation? UserLocation`

                      Approximate user location for search result localization.

                      - `JsonElement Type constant`

                        Location precision. Only "approximate" is supported.

                      - `string? City`

                        City name.

                        minLength: 1, maxLength: 255

                      - `string? Country`

                        Two-letter ISO 3166-1 country code, uppercase.

                      - `string? Region`

                        Region or state name.

                        minLength: 1, maxLength: 255

                      - `string? Timezone`

                        IANA timezone identifier, e.g. "America/Los_Angeles".

                        minLength: 1, maxLength: 255

                - `required BetaManagedAgentsAgentToolsetDefaultConfig DefaultConfig`

                  Resolved default configuration for agent tools.

                  - `required bool Enabled`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `required Type Type`

              - `class BetaManagedAgentsMcpToolset:`

                - `required IReadOnlyList<BetaManagedAgentsMcpToolConfig> Configs`

                  - `required bool Enabled`

                  - `required string Name`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `required BetaManagedAgentsMcpToolsetDefaultConfig DefaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `required bool Enabled`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `required string McpServerName`

                - `required Type Type`

              - `class BetaManagedAgentsCustomTool:`

                A custom tool as returned in API responses.

                - `required string Description`

                - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

                  JSON Schema for custom tool input parameters.

                  - `JsonElement Type constant`

                  - `IReadOnlyDictionary<string, JsonElement>? Properties`

                  - `IReadOnlyList<string>? Required`

                - `required string Name`

                - `required Type Type`

            - `required Type Type`

            - `required int Version`

              format: int32

          - `class BetaManagedAgentsAdvisor:`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `required string Model`

              The advisor model id.

            - `required Type Type`

        - `required Type Type`

      - `required string Name`

      - `required IReadOnlyList<Skill> Skills`

        - `class BetaManagedAgentsAnthropicSkill:`

          A resolved Anthropic-managed skill.

        - `class BetaManagedAgentsCustomSkill:`

          A resolved user-created custom skill.

      - `required string? System`

      - `required IReadOnlyList<Tool> Tools`

        - `class BetaManagedAgentsAgentToolset20260401:`

        - `class BetaManagedAgentsMcpToolset:`

        - `class BetaManagedAgentsCustomTool:`

          A custom tool as returned in API responses.

      - `required Type Type`

      - `required int Version`

        format: int32

    - `BetaManagedAgentsBudgetLimit? Budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `required BetaMonetaryAmount MaxListCost`

        A monetary amount in a specific currency.

        - `required string Amount`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `required BetaCurrency Currency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `required Type Type`

    - `IReadOnlyDictionary<string, string> Metadata`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `string? Title`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsSystemMessageEvent:`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

      System content blocks. Text-only.

      - `required string Text`

        The text content.

        minLength: 1

      - `required Type Type`

    - `required Type Type`

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionUsageEvent:`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

    - `required BetaManagedAgentsSessionUsageSnapshot Usage`

      Point-in-time snapshot of a session's cumulative usage.

      - `double ActiveSeconds`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `BetaManagedAgentsCacheCreationUsage CacheCreation`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `int Ephemeral1hInputTokens`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `int Ephemeral5mInputTokens`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `int CacheReadInputTokens`

        Total tokens read from prompt cache.

        format: int32

      - `int InputTokens`

        Total input tokens consumed across all turns.

        format: int32

      - `BetaMonetaryAmount ListCost`

        A monetary amount in a specific currency.

      - `int OutputTokens`

        Total output tokens generated across all turns.

        format: int32

      - `BetaManagedAgentsServerToolUsage ServerToolUse`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `int WebFetchRequests`

          Number of server-executed web fetch requests.

          format: int32

        - `int WebSearchRequests`

          Number of server-executed web search requests.

          format: int32

    - `BetaManagedAgentsBudgetLimit? Budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

#### Example

```csharp
EventListParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7",
    ThreadID = "sthr_011CZkZVWa6oIjw0rgXZpnBt",
};

var page = await client.Beta.Sessions.Threads.Events.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
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

`BetaManagedAgentsStreamSessionThreadEvents Beta.Sessions.Threads.Events.StreamStreaming(parameters, cancellationToken = default)`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}/stream`

Stream Session Thread Events

#### Parameters

- `EventStreamParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `required string threadID`

    Path param: Path parameter thread_id

  - `IReadOnlyList<BetaManagedAgentsDeltaType> eventDeltas`

    Query param: When set, this connection also receives streaming deltas (`event_start`, `event_delta`) while an event is being produced, before the event itself arrives. Deltas are best-effort; when the final event is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no final event — its terminal `span.model_request_end` closes the preview. Accepts one or more event types to preview and may be repeated: `agent.message` streams `content_delta` fragments; `agent.thinking` is start-only — a signal that the agent has begun extended thinking, concluded by the `agent.thinking` event itself. Only previews of the requested event types are sent.

    - `AgentMessage`

    - `AgentThinking`

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

#### Returns

- `class BetaManagedAgentsStreamSessionThreadEvents: union`

  Server-sent event in a single thread's stream.

  - `class BetaManagedAgentsUserMessageEvent:`

    A user message event in the session conversation.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<Content> Content`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `required string Text`

          The text content.

          minLength: 1

        - `required Type Type`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `required Source Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `required string Data`

              Base64-encoded image data.

              minLength: 1

            - `required string MediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

            - `required Type Type`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `required Type Type`

            - `required string Url`

              URL of the image to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

              minLength: 1

            - `required Type Type`

        - `required Type Type`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `required Source Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `required string Data`

              Base64-encoded document data.

              minLength: 1

            - `required string MediaType`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

            - `required Type Type`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `required string Data`

              The plain text content.

              minLength: 1

            - `required MediaType MediaType`

              MIME type of the text content. Must be "text/plain".

            - `required Type Type`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `required Type Type`

            - `required string Url`

              URL of the document to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

              minLength: 1

            - `required Type Type`

        - `required Type Type`

        - `string? Context`

          Additional context about the document for the model.

        - `string? Title`

          The title of the document.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

        - `required Type Type`

    - `required Type Type`

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsUserInterruptEvent:`

    An interrupt event that pauses agent execution and returns control to the user.

    - `required string ID`

      Unique identifier for this event.

    - `required Type Type`

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `string? SessionThreadID`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEvent:`

    A tool confirmation event that approves or denies a pending tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required Result Result`

      UserToolConfirmationResult enum

      - `Allow`

      - `Deny`

    - `required string ToolUseID`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `required Type Type`

    - `string? DenyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `string? SessionThreadID`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `class BetaManagedAgentsUserCustomToolResultEvent:`

    Event sent by the client providing the result of a custom tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required string CustomToolUseID`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `required Type Type`

    - `IReadOnlyList<Content> Content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

        - `required BetaManagedAgentsSearchResultCitations Citations`

          Citation settings for a search result.

          - `required bool Enabled`

            Whether citations are enabled for this search result.

        - `required IReadOnlyList<BetaManagedAgentsSearchResultContent> Content`

          Array of text content blocks from the search result.

          - `required string Text`

            The text content.

            minLength: 1

          - `required Type Type`

        - `required string Source`

          The URL source of the search result.

          minLength: 1

        - `required string Title`

          The title of the search result.

          minLength: 1

        - `required Type Type`

    - `bool? IsError`

      Whether the tool execution resulted in an error.

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `string? SessionThreadID`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsAgentCustomToolUseEvent:`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyDictionary<string, JsonElement> Input`

      Input parameters for the tool call.

    - `required string Name`

      Name of the custom tool being called.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

    - `string? SessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `class BetaManagedAgentsAgentMessageEvent:`

    An agent response event in the session conversation.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<Content> Content`

      Array of text blocks comprising the agent response.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsAgentThinkingEvent:`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsAgentMcpToolUseEvent:`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyDictionary<string, JsonElement> Input`

      Input parameters for the tool call.

    - `required string McpServerName`

      Name of the MCP server providing the tool.

    - `required string Name`

      Name of the MCP tool being used.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

    - `EvaluatedPermission EvaluatedPermission`

      AgentEvaluatedPermission enum

      - `Allow`

      - `Ask`

      - `Deny`

    - `string? SessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentMcpToolResultEvent:`

    Event representing the result of an MCP tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required string McpToolUseID`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

    - `IReadOnlyList<Content> Content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

    - `bool? IsError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent:`

    Event emitted when the agent invokes a built-in agent tool.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyDictionary<string, JsonElement> Input`

      Input parameters for the tool call.

    - `required string Name`

      Name of the agent tool being used.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

    - `EvaluatedPermission EvaluatedPermission`

      AgentEvaluatedPermission enum

      - `Allow`

      - `Ask`

      - `Deny`

    - `string? SessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentToolResultEvent:`

    Event representing the result of an agent tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string ToolUseID`

      The id of the `agent.tool_use` event this result corresponds to.

    - `required Type Type`

    - `IReadOnlyList<Content> Content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

    - `bool? IsError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadMessageReceivedEvent:`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<Content> Content`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

    - `required string FromSessionThreadID`

      Public `sthr_` ID of the thread that sent the message.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

    - `string? FromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class BetaManagedAgentsAgentThreadMessageSentEvent:`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<Content> Content`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string ToSessionThreadID`

      Public `sthr_` ID of the thread the message was sent to.

    - `required Type Type`

    - `string? ToAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent:`

    Indicates that context compaction (summarization) occurred during the session.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSessionErrorEvent:`

    An error event indicating a problem occurred during session execution.

    - `required string ID`

      Unique identifier for this event.

    - `required Error Error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError:`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `required Type Type`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `required Type Type`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `required Type Type`

        - `required Type Type`

      - `class BetaManagedAgentsModelOverloadedError:`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

      - `class BetaManagedAgentsModelRateLimitedError:`

        The model request was rate-limited.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

      - `class BetaManagedAgentsModelRequestFailedError:`

        A model request failed for a reason other than overload or rate-limiting.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

      - `class BetaManagedAgentsMcpConnectionFailedError:`

        Failed to connect to an MCP server.

        - `required string McpServerName`

          Name of the MCP server that failed to connect.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

      - `class BetaManagedAgentsMcpAuthenticationFailedError:`

        Authentication to an MCP server failed.

        - `required string McpServerName`

          Name of the MCP server that failed authentication.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

      - `class BetaManagedAgentsBillingError:`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

      - `class BetaManagedAgentsCredentialHostUnreachableError:`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `required string CredentialID`

          ID of the affected credential.

        - `required string Message`

          Human-readable error description.

        - `required RetryStatus RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `required Type Type`

        - `required string VaultID`

          ID of the vault containing the affected credential.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent:`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSessionStatusRunningEvent:`

    Indicates the session is actively running and the agent is working.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSessionStatusIdleEvent:`

    Indicates the agent has paused and is awaiting user input.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required StopReason StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

        - `required Type Type`

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `required IReadOnlyList<string> EventIds`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `required Type Type`

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `required Type Type`

      - `class BetaManagedAgentsSessionBudgetReached:`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `required Type Type`

    - `required Type Type`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent:`

    Indicates the session has terminated, either due to an error or completion.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSessionThreadCreatedEvent:`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the callable agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string SessionThreadID`

      Public `sthr_` ID of the newly created thread.

    - `required Type Type`

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent:`

    Emitted when an outcome evaluation cycle begins.

    - `required string ID`

      Unique identifier for this event.

    - `required int Iteration`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

      format: int32

    - `required string OutcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent:`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `required string ID`

      Unique identifier for this event.

    - `required string Explanation`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `required int Iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `required string OutcomeEvaluationStartID`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `required string OutcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string Result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `required Type Type`

    - `required BetaManagedAgentsSpanModelUsage Usage`

      Token usage for a single model request.

      - `required int CacheCreationInputTokens`

        Tokens used to create prompt cache in this request.

        format: int32

      - `required int CacheReadInputTokens`

        Tokens read from prompt cache in this request.

        format: int32

      - `required int InputTokens`

        Input tokens consumed by this request.

        format: int32

      - `required int OutputTokens`

        Output tokens generated by this request.

        format: int32

      - `Speed? Speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `Standard`

        - `Fast`

  - `class BetaManagedAgentsSpanModelRequestStartEvent:`

    Emitted when a model request is initiated by the agent.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSpanModelRequestEndEvent:`

    Emitted when a model request completes.

    - `required string ID`

      Unique identifier for this event.

    - `required bool? IsError`

      Whether the model request resulted in an error.

    - `required string ModelRequestStartID`

      The id of the corresponding `span.model_request_start` event.

    - `required BetaManagedAgentsSpanModelUsage ModelUsage`

      Token usage for a single model request.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent:`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `required string ID`

      Unique identifier for this event.

    - `required int Iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `required string OutcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsUserDefineOutcomeEvent:`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `required string ID`

      Unique identifier for this event.

    - `required string Description`

      What the agent should produce. Copied from the input event.

    - `required int? MaxIterations`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

      format: int32

    - `required string OutcomeID`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Rubric Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric:`

        Rubric referenced by a file uploaded via the Files API.

        - `required string FileID`

          ID of the rubric file.

        - `required Type Type`

      - `class BetaManagedAgentsTextRubric:`

        Rubric content provided inline as text.

        - `required string Content`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `required Type Type`

    - `required Type Type`

  - `class BetaManagedAgentsSessionDeletedEvent:`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent:`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string SessionThreadID`

      Public sthr_ ID of the thread that started running.

    - `required Type Type`

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent:`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string SessionThreadID`

      Public sthr_ ID of the thread that went idle.

    - `required StopReason StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `class BetaManagedAgentsSessionBudgetReached:`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

    - `required Type Type`

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent:`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string SessionThreadID`

      Public sthr_ ID of the thread that terminated.

    - `required Type Type`

  - `class BetaManagedAgentsUserToolResultEvent:`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `required string ID`

      Unique identifier for this event.

    - `required string ToolUseID`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `required Type Type`

    - `IReadOnlyList<Content> Content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

    - `bool? IsError`

      Whether the tool execution resulted in an error.

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `string? SessionThreadID`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent:`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string SessionThreadID`

      Public sthr_ ID of the thread that is retrying.

    - `required Type Type`

  - `class BetaManagedAgentsSessionUpdatedEvent:`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

    - `BetaManagedAgentsSessionAgent? Agent`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `required string ID`

      - `required string? Description`

      - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

        - `required string Name`

        - `required Type Type`

        - `required string Url`

      - `required BetaManagedAgentsModelConfig Model`

        Model identifier and configuration.

        - `required BetaManagedAgentsModel ID`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `ClaudeFable5_1`

            Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

          - `ClaudeSonnet5`

            High-performance model for coding and agents

          - `ClaudeFable5`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `ClaudeOpus5`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_8`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_7`

            Powerful intelligence for long-running agents and coding

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

        - `Effort Effort`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow:`

            Low effort. Favors latency over reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortMedium:`

            Medium effort. Balances latency and reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortHigh:`

            High effort. Favors reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortXhigh:`

            Extra-high effort. Not all models accept this level.

            - `required Type Type`

          - `class BetaManagedAgentsEffortMax:`

            Maximum effort. Favors reasoning depth over latency.

            - `required Type Type`

        - `string InferenceGeo`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `Speed Speed`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `Standard`

          - `Fast`

      - `required BetaManagedAgentsSessionMultiagentCoordinator? Multiagent`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `required IReadOnlyList<Agent> Agents`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `class BetaManagedAgentsSessionThreadAgent:`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `required string ID`

            - `required string? Description`

            - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

              - `required string Name`

              - `required Type Type`

              - `required string Url`

            - `required BetaManagedAgentsModelConfig Model`

              Model identifier and configuration.

            - `required string Name`

            - `required IReadOnlyList<Skill> Skills`

              - `class BetaManagedAgentsAnthropicSkill:`

                A resolved Anthropic-managed skill.

                - `required string SkillID`

                - `required Type Type`

                - `required string Version`

              - `class BetaManagedAgentsCustomSkill:`

                A resolved user-created custom skill.

                - `required string SkillID`

                - `required Type Type`

                - `required string Version`

            - `required string? System`

            - `required IReadOnlyList<Tool> Tools`

              - `class BetaManagedAgentsAgentToolset20260401:`

                - `required IReadOnlyList<BetaManagedAgentsAgentToolConfig> Configs`

                  - `class BetaManagedAgentsBashToolConfig:`

                    Configuration for the bash tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                        - `required Type Type`

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                        - `required Type Type`

                    - `JsonElement Type constant`

                  - `class BetaManagedAgentsEditToolConfig:`

                    Configuration for the edit tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                  - `class BetaManagedAgentsReadToolConfig:`

                    Configuration for the read tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                  - `class BetaManagedAgentsWriteToolConfig:`

                    Configuration for the write tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                  - `class BetaManagedAgentsGlobToolConfig:`

                    Configuration for the glob tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                  - `class BetaManagedAgentsGrepToolConfig:`

                    Configuration for the grep tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                  - `class BetaManagedAgentsWebFetchToolConfig:`

                    Configuration for the web_fetch tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                    - `IReadOnlyList<string> AllowedDomains`

                    - `IReadOnlyList<string> BlockedDomains`

                    - `int? MaxContentTokens`

                      format: int32

                  - `class BetaManagedAgentsWebSearchToolConfig:`

                    Configuration for the web_search tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                    - `IReadOnlyList<string> AllowedDomains`

                    - `IReadOnlyList<string> BlockedDomains`

                    - `BetaManagedAgentsUserLocation? UserLocation`

                      Approximate user location for search result localization.

                      - `JsonElement Type constant`

                        Location precision. Only "approximate" is supported.

                      - `string? City`

                        City name.

                        minLength: 1, maxLength: 255

                      - `string? Country`

                        Two-letter ISO 3166-1 country code, uppercase.

                      - `string? Region`

                        Region or state name.

                        minLength: 1, maxLength: 255

                      - `string? Timezone`

                        IANA timezone identifier, e.g. "America/Los_Angeles".

                        minLength: 1, maxLength: 255

                - `required BetaManagedAgentsAgentToolsetDefaultConfig DefaultConfig`

                  Resolved default configuration for agent tools.

                  - `required bool Enabled`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `required Type Type`

              - `class BetaManagedAgentsMcpToolset:`

                - `required IReadOnlyList<BetaManagedAgentsMcpToolConfig> Configs`

                  - `required bool Enabled`

                  - `required string Name`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `required BetaManagedAgentsMcpToolsetDefaultConfig DefaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `required bool Enabled`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `required string McpServerName`

                - `required Type Type`

              - `class BetaManagedAgentsCustomTool:`

                A custom tool as returned in API responses.

                - `required string Description`

                - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

                  JSON Schema for custom tool input parameters.

                  - `JsonElement Type constant`

                  - `IReadOnlyDictionary<string, JsonElement>? Properties`

                  - `IReadOnlyList<string>? Required`

                - `required string Name`

                - `required Type Type`

            - `required Type Type`

            - `required int Version`

              format: int32

          - `class BetaManagedAgentsAdvisor:`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `required string Model`

              The advisor model id.

            - `required Type Type`

        - `required Type Type`

      - `required string Name`

      - `required IReadOnlyList<Skill> Skills`

        - `class BetaManagedAgentsAnthropicSkill:`

          A resolved Anthropic-managed skill.

        - `class BetaManagedAgentsCustomSkill:`

          A resolved user-created custom skill.

      - `required string? System`

      - `required IReadOnlyList<Tool> Tools`

        - `class BetaManagedAgentsAgentToolset20260401:`

        - `class BetaManagedAgentsMcpToolset:`

        - `class BetaManagedAgentsCustomTool:`

          A custom tool as returned in API responses.

      - `required Type Type`

      - `required int Version`

        format: int32

    - `BetaManagedAgentsBudgetLimit? Budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `required BetaMonetaryAmount MaxListCost`

        A monetary amount in a specific currency.

        - `required string Amount`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `required BetaCurrency Currency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `required Type Type`

    - `IReadOnlyDictionary<string, string> Metadata`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `string? Title`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsStartEvent:`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `required BetaManagedAgentsStartEventPreview Event`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

      - `class BetaManagedAgentsAgentMessagePreview:`

        - `required string ID`

          The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

        - `required Type Type`

      - `class BetaManagedAgentsAgentThinkingPreview:`

        - `required string ID`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

        - `required Type Type`

    - `required Type Type`

  - `class BetaManagedAgentsDeltaEvent:`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `required BetaManagedAgentsDeltaContent Delta`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `required BetaManagedAgentsTextBlock Content`

        Regular text content.

      - `required Type Type`

      - `long Index`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

        format: uint32

    - `required string EventID`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

    - `required Type Type`

  - `class BetaManagedAgentsSystemMessageEvent:`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

      System content blocks. Text-only.

      - `required string Text`

        The text content.

        minLength: 1

      - `required Type Type`

    - `required Type Type`

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionUsageEvent:`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

    - `required BetaManagedAgentsSessionUsageSnapshot Usage`

      Point-in-time snapshot of a session's cumulative usage.

      - `double ActiveSeconds`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `BetaManagedAgentsCacheCreationUsage CacheCreation`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `int Ephemeral1hInputTokens`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `int Ephemeral5mInputTokens`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `int CacheReadInputTokens`

        Total tokens read from prompt cache.

        format: int32

      - `int InputTokens`

        Total input tokens consumed across all turns.

        format: int32

      - `BetaMonetaryAmount ListCost`

        A monetary amount in a specific currency.

      - `int OutputTokens`

        Total output tokens generated across all turns.

        format: int32

      - `BetaManagedAgentsServerToolUsage ServerToolUse`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `int WebFetchRequests`

          Number of server-executed web fetch requests.

          format: int32

        - `int WebSearchRequests`

          Number of server-executed web search requests.

          format: int32

    - `BetaManagedAgentsBudgetLimit? Budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

- `class BetaManagedAgentsStreamSessionThreadEvents: union`

  Server-sent event in a single thread's stream.

#### Example

```csharp
EventStreamParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7",
    ThreadID = "sthr_011CZkZVWa6oIjw0rgXZpnBt",
};

await foreach (var betaManagedAgentsStreamSessionThreadEvents in client.Beta.Sessions.Threads.Events.StreamStreaming(parameters))
{
    Console.WriteLine(betaManagedAgentsStreamSessionThreadEvents);
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
