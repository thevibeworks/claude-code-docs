---
title: Create Session
url: https://platform.claude.com/docs/en/api/beta/sessions/create
---

# Create Session

**POST** `/v1/sessions`

Create Session

## Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 42 more`

    - `"message-batches-2024-09-24"`

    - `"prompt-caching-2024-07-31"`

    - `"computer-use-2024-10-22"`

    - `"computer-use-2025-01-24"`

    - `"pdfs-2024-09-25"`

    - `"token-counting-2024-11-01"`

    - `"token-efficient-tools-2025-02-19"`

    - `"output-128k-2025-02-19"`

    - `"files-api-2025-04-14"`

    - `"mcp-client-2025-04-04"`

    - `"mcp-client-2025-11-20"`

    - `"dev-full-thinking-2025-05-14"`

    - `"interleaved-thinking-2025-05-14"`

    - `"code-execution-2025-05-22"`

    - `"extended-cache-ttl-2025-04-11"`

    - `"context-1m-2025-08-07"`

    - `"context-management-2025-06-27"`

    - `"model-context-window-exceeded-2025-08-26"`

    - `"skills-2025-10-02"`

    - `"fast-mode-2026-02-01"`

    - `"output-300k-2026-03-24"`

    - `"user-profiles-2026-03-24"`

    - `"user-profiles-2026-08-18"`

    - `"user-profiles-2026-09-04"`

    - `"advisor-tool-2026-03-01"`

    - `"managed-agents-2026-04-01"`

    - `"cache-diagnosis-2026-04-07"`

    - `"dreaming-2026-04-21"`

    - `"thinking-token-count-2026-05-13"`

    - `"server-side-fallback-2026-06-01"`

    - `"server-side-fallback-2026-07-01"`

    - `"fallback-credit-2026-06-01"`

    - `"fallback-credit-2026-07-01"`

    - `"agent-memory-2026-07-22"`

    - `"mid-conversation-tool-changes-2026-07-01"`

    - `"compact-2026-01-12"`

    - `"computer-use-2025-11-24"`

    - `"mcp-tunnels-2026-06-22"`

    - `"structured-outputs-2025-11-13"`

    - `"task-budgets-2026-03-13"`

    - `"thinking-display-updates-2026-08-18"`

    - `"ce-user-management-2026-07-13"`

    - `"mid-conversation-output-config-2026-07-01"`

    - `"thinking-binding-controls-2026-08-01"`

    - `"mid-conversation-system-clear-at-2026-08-21"`

- `"anthropic-workspace-id": optional string`

## Body parameters

- `agent: string or BetaManagedAgentsAgentParams or BetaManagedAgentsAgentWithOverridesParams`

  Agent identifier. Accepts the `agent` ID string, which pins the latest version for the session, or an `agent` object with both id and version specified.

  - `string`

  - `BetaManagedAgentsAgentParams object`

    Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

    - `type: "agent"`

    - `id: string`

      The `agent` ID.

      minLength: 1, maxLength: 128

    - `version: optional number`

      The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

      format: int32

  - `BetaManagedAgentsAgentWithOverridesParams object`

    Reference to an `agent` plus optional configuration overrides. Each provided field replaces the agent's value for the caller's use; the agent resource is unchanged.

    - `type: "agent_with_overrides"`

    - `id: string`

      The `agent` ID.

      minLength: 1, maxLength: 128

    - `mcp_servers: optional array of BetaManagedAgentsURLMCPServerParams`

      Replacement MCP server list. Full replacement: the provided array becomes the MCP servers. Send an empty array to clear; omit to preserve the agent's servers.

      - `type: "url"`

      - `name: string`

        Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

        minLength: 1, maxLength: 255

      - `url: string`

        Endpoint URL for the MCP server.

        maxLength: 2048

    - `model: optional BetaManagedAgentsModel or BetaManagedAgentsModelConfigParams`

      Replacement model. Accepts the model string, e.g. `claude-opus-5`, or a `model_config` object. Omit to use the agent's model.

      - `BetaManagedAgentsModel = "claude-fable-5-1" or "claude-sonnet-5" or "claude-fable-5" or 11 more or string`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `"claude-fable-5-1" or "claude-sonnet-5" or "claude-fable-5" or 11 more`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `"claude-fable-5-1"`

            Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

          - `"claude-sonnet-5"`

            High-performance model for coding and agents

          - `"claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `"claude-opus-5"`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-8"`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-7"`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-6"`

            Powerful intelligence for long-running agents and coding

          - `"claude-sonnet-4-6"`

            Best combination of speed and intelligence

          - `"claude-haiku-4-5"`

            Fastest model with near-frontier intelligence

          - `"claude-haiku-4-5-20251001"`

            Fastest model with near-frontier intelligence

          - `"claude-opus-4-5"`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-5-20251101"`

            Powerful intelligence for long-running agents and coding

          - `"claude-sonnet-4-5"`

            High-performance model for agents and coding

          - `"claude-sonnet-4-5-20250929"`

            High-performance model for agents and coding

        - `string`

      - `BetaManagedAgentsModelConfigParams object`

        An object that defines additional configuration control over model use

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `effort: optional "low" or "medium" or "high" or 2 more or BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or 3 more or null`

          How hard Claude works on each inference call. Accepts a bare level string (`"high"`) or `{"type": "high"}`. On create, omitting it resolves the per-model default; on update, omitting it leaves the stored value unchanged.

          - `BetaManagedAgentsEffortLevel = "low" or "medium" or "high" or 2 more`

            How hard Claude works on each turn. Higher levels favor reasoning depth over latency. Not all models accept every level; invalid combinations are rejected at create time.

            - `"low"`

            - `"medium"`

            - `"high"`

            - `"xhigh"`

            - `"max"`

          - `BetaManagedAgentsEffortLow object`

            Low effort. Favors latency over reasoning depth.

            - `type: "low"`

          - `BetaManagedAgentsEffortMedium object`

            Medium effort. Balances latency and reasoning depth.

            - `type: "medium"`

          - `BetaManagedAgentsEffortHigh object`

            High effort. Favors reasoning depth.

            - `type: "high"`

          - `BetaManagedAgentsEffortXhigh object`

            Extra-high effort. Not all models accept this level.

            - `type: "xhigh"`

          - `BetaManagedAgentsEffortMax object`

            Maximum effort. Favors reasoning depth over latency.

            - `type: "max"`

        - `inference_geo: optional string or null`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo. On update, `model` is whole-object replacement — omitting inference_geo clears it.

        - `speed: optional "standard" or "fast" or null`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

    - `skills: optional array of BetaManagedAgentsSkillParams`

      Replacement skill list. Full replacement: the provided array becomes the skills. Send an empty array to clear; omit to preserve the agent's skills.

      - `BetaManagedAgentsAnthropicSkillParams object`

        An Anthropic-managed skill.

        - `type: "anthropic"`

        - `skill_id: string`

          Identifier of the Anthropic skill (e.g., "xlsx").

          minLength: 1, maxLength: 64

        - `version: optional string or null`

          Version to pin. Defaults to latest if omitted.

          minLength: 1, maxLength: 64

      - `BetaManagedAgentsCustomSkillParams object`

        A user-created custom skill.

        - `type: "custom"`

        - `skill_id: string`

          Tagged ID of the custom skill (e.g., "skill_01XJ5...").

          minLength: 1, maxLength: 64

        - `version: optional string or null`

          Version to pin. Defaults to latest if omitted.

          minLength: 1, maxLength: 64

    - `system: optional string or null`

      Replacement system prompt. Up to 100,000 characters. Set to null to clear the agent's system prompt; omit to preserve it.

      maxLength: 100000

    - `tools: optional array of BetaManagedAgentsAgentToolset20260401Params or BetaManagedAgentsMCPToolsetParams or BetaManagedAgentsCustomToolParams`

      Replacement tool list. Full replacement: the provided array becomes the tool configuration. Send an empty array to clear; omit to preserve the agent's tools.

      - `BetaManagedAgentsAgentToolset20260401Params object`

        Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

        - `type: "agent_toolset_20260401"`

        - `configs: optional array of BetaManagedAgentsAgentToolConfigParams`

          Per-tool configuration overrides.

          - `BetaManagedAgentsBashToolConfigParams object`

            Configuration override for the bash tool.

            - `type: optional "bash"`

            - `name: "bash"`

              Must be "bash".

            - `enabled: optional boolean or null`

              Whether this tool is enabled and available to Claude. Overrides the default_config setting.

            - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy or null`

              Permission policy for tool execution.

              - `BetaManagedAgentsAlwaysAllowPolicy object`

                Tool calls are automatically approved without user confirmation.

                - `type: "always_allow"`

              - `BetaManagedAgentsAlwaysAskPolicy object`

                Tool calls require user confirmation before execution.

                - `type: "always_ask"`

              - `BetaManagedAgentsAutoPolicy object`

                The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `type: "auto"`

          - `BetaManagedAgentsEditToolConfigParams object`

            Configuration override for the edit tool.

            - `type: optional "edit"`

            - `name: "edit"`

              Must be "edit".

            - `enabled: optional boolean or null`

              Whether this tool is enabled and available to Claude. Overrides the default_config setting.

            - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy or null`

              Permission policy for tool execution.

              - `BetaManagedAgentsAlwaysAllowPolicy object`

                Tool calls are automatically approved without user confirmation.

              - `BetaManagedAgentsAlwaysAskPolicy object`

                Tool calls require user confirmation before execution.

              - `BetaManagedAgentsAutoPolicy object`

                The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

          - `BetaManagedAgentsReadToolConfigParams object`

            Configuration override for the read tool.

            - `type: optional "read"`

            - `name: "read"`

              Must be "read".

            - `enabled: optional boolean or null`

              Whether this tool is enabled and available to Claude. Overrides the default_config setting.

            - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy or null`

              Permission policy for tool execution.

              - `BetaManagedAgentsAlwaysAllowPolicy object`

                Tool calls are automatically approved without user confirmation.

              - `BetaManagedAgentsAlwaysAskPolicy object`

                Tool calls require user confirmation before execution.

              - `BetaManagedAgentsAutoPolicy object`

                The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

          - `BetaManagedAgentsWriteToolConfigParams object`

            Configuration override for the write tool.

            - `type: optional "write"`

            - `name: "write"`

              Must be "write".

            - `enabled: optional boolean or null`

              Whether this tool is enabled and available to Claude. Overrides the default_config setting.

            - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy or null`

              Permission policy for tool execution.

              - `BetaManagedAgentsAlwaysAllowPolicy object`

                Tool calls are automatically approved without user confirmation.

              - `BetaManagedAgentsAlwaysAskPolicy object`

                Tool calls require user confirmation before execution.

              - `BetaManagedAgentsAutoPolicy object`

                The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

          - `BetaManagedAgentsGlobToolConfigParams object`

            Configuration override for the glob tool.

            - `type: optional "glob"`

            - `name: "glob"`

              Must be "glob".

            - `enabled: optional boolean or null`

              Whether this tool is enabled and available to Claude. Overrides the default_config setting.

            - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy or null`

              Permission policy for tool execution.

              - `BetaManagedAgentsAlwaysAllowPolicy object`

                Tool calls are automatically approved without user confirmation.

              - `BetaManagedAgentsAlwaysAskPolicy object`

                Tool calls require user confirmation before execution.

              - `BetaManagedAgentsAutoPolicy object`

                The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

          - `BetaManagedAgentsGrepToolConfigParams object`

            Configuration override for the grep tool.

            - `type: optional "grep"`

            - `name: "grep"`

              Must be "grep".

            - `enabled: optional boolean or null`

              Whether this tool is enabled and available to Claude. Overrides the default_config setting.

            - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy or null`

              Permission policy for tool execution.

              - `BetaManagedAgentsAlwaysAllowPolicy object`

                Tool calls are automatically approved without user confirmation.

              - `BetaManagedAgentsAlwaysAskPolicy object`

                Tool calls require user confirmation before execution.

              - `BetaManagedAgentsAutoPolicy object`

                The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

          - `BetaManagedAgentsWebFetchToolConfigParams object`

            Configuration override for the web_fetch tool.

            - `type: optional "web_fetch"`

            - `name: "web_fetch"`

              Must be "web_fetch".

            - `allowed_domains: optional array of string`

              Only fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

            - `blocked_domains: optional array of string`

              Never fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

            - `enabled: optional boolean or null`

              Whether this tool is enabled and available to Claude. Overrides the default_config setting.

            - `max_content_tokens: optional number or null`

              Maximum number of tokens of fetched text content to include in context per call. Does not apply to binary content such as PDFs.

              format: int32

            - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy or null`

              Permission policy for tool execution.

              - `BetaManagedAgentsAlwaysAllowPolicy object`

                Tool calls are automatically approved without user confirmation.

              - `BetaManagedAgentsAlwaysAskPolicy object`

                Tool calls require user confirmation before execution.

              - `BetaManagedAgentsAutoPolicy object`

                The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

          - `BetaManagedAgentsWebSearchToolConfigParams object`

            Configuration override for the web_search tool.

            - `type: optional "web_search"`

            - `name: "web_search"`

              Must be "web_search".

            - `allowed_domains: optional array of string`

              Only return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

            - `blocked_domains: optional array of string`

              Never return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

            - `enabled: optional boolean or null`

              Whether this tool is enabled and available to Claude. Overrides the default_config setting.

            - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy or null`

              Permission policy for tool execution.

              - `BetaManagedAgentsAlwaysAllowPolicy object`

                Tool calls are automatically approved without user confirmation.

              - `BetaManagedAgentsAlwaysAskPolicy object`

                Tool calls require user confirmation before execution.

              - `BetaManagedAgentsAutoPolicy object`

                The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `user_location: optional BetaManagedAgentsUserLocation or null`

              Approximate user location for search result localization.

              - `type: "approximate"`

                Location precision. Only "approximate" is supported.

              - `city: optional string or null`

                City name.

                minLength: 1, maxLength: 255

              - `country: optional string or null`

                Two-letter ISO 3166-1 country code, uppercase.

              - `region: optional string or null`

                Region or state name.

                minLength: 1, maxLength: 255

              - `timezone: optional string or null`

                IANA timezone identifier, e.g. "America/Los_Angeles".

                minLength: 1, maxLength: 255

        - `default_config: optional BetaManagedAgentsAgentToolsetDefaultConfigParams or null`

          Default configuration for all tools in a toolset.

          - `enabled: optional boolean or null`

            Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

          - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy or null`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy object`

              Tool calls are automatically approved without user confirmation.

            - `BetaManagedAgentsAlwaysAskPolicy object`

              Tool calls require user confirmation before execution.

            - `BetaManagedAgentsAutoPolicy object`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

      - `BetaManagedAgentsMCPToolsetParams object`

        Configuration for tools from an MCP server defined in `mcp_servers`.

        - `type: "mcp_toolset"`

        - `mcp_server_name: string`

          Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

          minLength: 1, maxLength: 255

        - `configs: optional array of BetaManagedAgentsMCPToolConfigParams`

          Per-tool configuration overrides.

          - `name: string`

            Name of the MCP tool to configure. 1-128 characters.

            minLength: 1, maxLength: 128

          - `enabled: optional boolean or null`

            Whether this tool is enabled. Overrides the `default_config` setting.

          - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy or null`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy object`

              Tool calls are automatically approved without user confirmation.

            - `BetaManagedAgentsAlwaysAskPolicy object`

              Tool calls require user confirmation before execution.

            - `BetaManagedAgentsAutoPolicy object`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

        - `default_config: optional BetaManagedAgentsMCPToolsetDefaultConfigParams or null`

          Default configuration for all tools from an MCP server.

          - `enabled: optional boolean or null`

            Whether tools are enabled by default. Defaults to true if not specified.

          - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy or null`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy object`

              Tool calls are automatically approved without user confirmation.

            - `BetaManagedAgentsAlwaysAskPolicy object`

              Tool calls require user confirmation before execution.

            - `BetaManagedAgentsAutoPolicy object`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

      - `BetaManagedAgentsCustomToolParams object`

        A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

        - `type: "custom"`

        - `description: string`

          Description of what the tool does, shown to the agent to help it decide when to use the tool.

          minLength: 1

        - `input_schema: BetaManagedAgentsCustomToolInputSchema`

          JSON Schema for custom tool input parameters.

          - `type: "object"`

          - `properties: optional map[unknown] or null`

          - `required: optional array of string or null`

        - `name: string`

          Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

          minLength: 1, maxLength: 128

    - `version: optional number`

      The specific `agent` version to use. Omit to use the latest version.

      format: int32

- `environment_id: string`

  ID of the `environment` defining the container configuration for this session.

  minLength: 1, maxLength: 128

- `budget: optional BetaManagedAgentsBudgetLimit`

  A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

  - `type: "limit"`

  - `max_list_cost: BetaMonetaryAmount`

    A monetary amount in a specific currency.

    - `amount: string`

      Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

    - `currency: BetaCurrency`

      Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

- `initial_events: optional array of BetaManagedAgentsUserMessageEventParams or BetaManagedAgentsUserDefineOutcomeEventParams`

  Initial events to send to the `session` at creation, processed in order. Supports `user.message` and `user.define_outcome` events. Maximum 50 events.

  - `BetaManagedAgentsUserMessageEventParams object`

    Parameters for sending a user message to the session.

    - `type: "user.message"`

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

      Array of content blocks for the user message.

      - `BetaManagedAgentsTextBlock object`

        Regular text content.

        - `type: "text"`

        - `text: string`

          The text content.

          minLength: 1

      - `BetaManagedAgentsImageBlock object`

        Image content specified directly as base64 data or as a reference via a URL.

        - `type: "image"`

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `BetaManagedAgentsBase64ImageSource object`

            Base64-encoded image data.

            - `type: "base64"`

            - `data: string`

              Base64-encoded image data.

              minLength: 1

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

          - `BetaManagedAgentsURLImageSource object`

            Image referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the image to fetch.

              minLength: 1

          - `BetaManagedAgentsFileImageSource object`

            Image referenced by file ID.

            - `type: "file"`

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

      - `BetaManagedAgentsDocumentBlock object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `type: "document"`

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `BetaManagedAgentsBase64DocumentSource object`

            Base64-encoded document data.

            - `type: "base64"`

            - `data: string`

              Base64-encoded document data.

              minLength: 1

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

          - `BetaManagedAgentsPlainTextDocumentSource object`

            Plain text document content.

            - `type: "text"`

            - `data: string`

              The plain text content.

              minLength: 1

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

          - `BetaManagedAgentsURLDocumentSource object`

            Document referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the document to fetch.

              minLength: 1

          - `BetaManagedAgentsFileDocumentSource object`

            Document referenced by file ID.

            - `type: "file"`

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

        - `context: optional string or null`

          Additional context about the document for the model.

        - `title: optional string or null`

          The title of the document.

      - `BetaManagedAgentsRedactedBlock object`

        Placeholder for content withheld by Anthropic model policy.

        - `type: "redacted"`

  - `BetaManagedAgentsUserDefineOutcomeEventParams object`

    Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

    - `type: "user.define_outcome"`

    - `description: string`

      What the agent should produce. This is the task specification.

    - `rubric: BetaManagedAgentsFileRubricParams or BetaManagedAgentsTextRubricParams`

      Rubric for grading the quality of an outcome.

      - `BetaManagedAgentsFileRubricParams object`

        Rubric referenced by a file uploaded via the Files API.

        - `type: "file"`

        - `file_id: string`

          ID of the rubric file.

      - `BetaManagedAgentsTextRubricParams object`

        Rubric content provided inline as text.

        - `type: "text"`

        - `content: string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

          maxLength: 262144

    - `max_iterations: optional number or null`

      Eval→revision cycles before giving up. Default 3, max 20.

      format: int32

- `metadata: optional map[string]`

  Arbitrary key-value metadata attached to the session. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `resources: optional array of BetaManagedAgentsGitHubRepositoryResourceParams or BetaManagedAgentsFileResourceParams or BetaManagedAgentsMemoryStoreResourceParam`

  Resources (e.g. repositories, files) to mount into the session's container.

  - `BetaManagedAgentsGitHubRepositoryResourceParams object`

    Mount a GitHub repository into the session's container.

    - `type: "github_repository"`

    - `url: string`

      Github URL of the repository

      minLength: 1, maxLength: 2048

    - `authorization_token: optional string`

      GitHub authorization token used to clone the repository. Required for private repositories; optional for public ones.

      minLength: 1, maxLength: 4096

    - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout or null`

      Branch or commit to check out. Defaults to the repository's default branch.

      - `BetaManagedAgentsBranchCheckout object`

        - `type: "branch"`

        - `name: string`

          Branch name to check out.

          minLength: 1, maxLength: 255

      - `BetaManagedAgentsCommitCheckout object`

        - `type: "commit"`

        - `sha: string`

          Full commit SHA to check out.

          minLength: 7, maxLength: 64

    - `mount_path: optional string or null`

      Mount path in the container. Defaults to `/workspace/<repo-name>`.

      minLength: 1, maxLength: 4096

  - `BetaManagedAgentsFileResourceParams object`

    Mount a file uploaded via the Files API into the session.

    - `type: "file"`

    - `file_id: string`

      ID of a previously uploaded file.

      minLength: 1, maxLength: 128

    - `mount_path: optional string or null`

      Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

      minLength: 1, maxLength: 4096

  - `BetaManagedAgentsMemoryStoreResourceParam object`

    Parameters for attaching a memory store to an agent session.

    - `type: "memory_store"`

    - `memory_store_id: string`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `access: optional "read_write" or "read_only" or null`

      Access mode for an attached memory store.

      - `"read_write"`

      - `"read_only"`

    - `instructions: optional string or null`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      maxLength: 4096

- `title: optional string or null`

  Human-readable session title.

  maxLength: 500

- `vault_ids: optional array of string`

  Vault IDs for stored credentials the agent can use during the session.

## Returns

- `BetaManagedAgentsSession object`

  A Managed Agents `session`.

  - `type: "session"`

  - `id: string`

  - `agent: BetaManagedAgentsSessionAgent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `type: "agent"`

    - `id: string`

    - `description: string or null`

    - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

      - `type: "url"`

      - `name: string`

      - `url: string`

    - `model: BetaManagedAgentsModelConfig`

      Model identifier and configuration.

      - `id: BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `"claude-fable-5-1" or "claude-sonnet-5" or "claude-fable-5" or 11 more`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `"claude-fable-5-1"`

            Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

          - `"claude-sonnet-5"`

            High-performance model for coding and agents

          - `"claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `"claude-opus-5"`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-8"`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-7"`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-6"`

            Powerful intelligence for long-running agents and coding

          - `"claude-sonnet-4-6"`

            Best combination of speed and intelligence

          - `"claude-haiku-4-5"`

            Fastest model with near-frontier intelligence

          - `"claude-haiku-4-5-20251001"`

            Fastest model with near-frontier intelligence

          - `"claude-opus-4-5"`

            Powerful intelligence for long-running agents and coding

          - `"claude-opus-4-5-20251101"`

            Powerful intelligence for long-running agents and coding

          - `"claude-sonnet-4-5"`

            High-performance model for agents and coding

          - `"claude-sonnet-4-5-20250929"`

            High-performance model for agents and coding

        - `string`

      - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

        - `BetaManagedAgentsEffortLow object`

          Low effort. Favors latency over reasoning depth.

          - `type: "low"`

        - `BetaManagedAgentsEffortMedium object`

          Medium effort. Balances latency and reasoning depth.

          - `type: "medium"`

        - `BetaManagedAgentsEffortHigh object`

          High effort. Favors reasoning depth.

          - `type: "high"`

        - `BetaManagedAgentsEffortXhigh object`

          Extra-high effort. Not all models accept this level.

          - `type: "xhigh"`

        - `BetaManagedAgentsEffortMax object`

          Maximum effort. Favors reasoning depth over latency.

          - `type: "max"`

      - `inference_geo: optional string`

        Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

      - `speed: optional "standard" or "fast"`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `multiagent: BetaManagedAgentsSessionMultiagentCoordinator or null`

      Resolved coordinator topology with full agent definitions for each roster member.

      - `type: "coordinator"`

      - `agents: array of BetaManagedAgentsSessionThreadAgent or BetaManagedAgentsAdvisor`

        Full `agent` definitions the coordinator may spawn as session threads.

        - `BetaManagedAgentsSessionThreadAgent object`

          Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

          - `type: "agent"`

          - `id: string`

          - `description: string or null`

          - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

            - `type: "url"`

            - `name: string`

            - `url: string`

          - `model: BetaManagedAgentsModelConfig`

            Model identifier and configuration.

          - `name: string`

          - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

            - `BetaManagedAgentsAnthropicSkill object`

              A resolved Anthropic-managed skill.

              - `type: "anthropic"`

              - `skill_id: string`

              - `version: string`

            - `BetaManagedAgentsCustomSkill object`

              A resolved user-created custom skill.

              - `type: "custom"`

              - `skill_id: string`

              - `version: string`

          - `system: string or null`

          - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

            - `BetaManagedAgentsAgentToolset20260401 object`

              - `type: "agent_toolset_20260401"`

              - `configs: array of BetaManagedAgentsAgentToolConfig`

                - `BetaManagedAgentsBashToolConfig object`

                  Configuration for the bash tool.

                  - `type: "bash"`

                  - `enabled: boolean`

                  - `name: "bash"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy object`

                      Tool calls are automatically approved without user confirmation.

                      - `type: "always_allow"`

                    - `BetaManagedAgentsAlwaysAskPolicy object`

                      Tool calls require user confirmation before execution.

                      - `type: "always_ask"`

                    - `BetaManagedAgentsAutoPolicy object`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                      - `type: "auto"`

                - `BetaManagedAgentsEditToolConfig object`

                  Configuration for the edit tool.

                  - `type: "edit"`

                  - `enabled: boolean`

                  - `name: "edit"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy object`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy object`

                      Tool calls require user confirmation before execution.

                    - `BetaManagedAgentsAutoPolicy object`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `BetaManagedAgentsReadToolConfig object`

                  Configuration for the read tool.

                  - `type: "read"`

                  - `enabled: boolean`

                  - `name: "read"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy object`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy object`

                      Tool calls require user confirmation before execution.

                    - `BetaManagedAgentsAutoPolicy object`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `BetaManagedAgentsWriteToolConfig object`

                  Configuration for the write tool.

                  - `type: "write"`

                  - `enabled: boolean`

                  - `name: "write"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy object`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy object`

                      Tool calls require user confirmation before execution.

                    - `BetaManagedAgentsAutoPolicy object`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `BetaManagedAgentsGlobToolConfig object`

                  Configuration for the glob tool.

                  - `type: "glob"`

                  - `enabled: boolean`

                  - `name: "glob"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy object`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy object`

                      Tool calls require user confirmation before execution.

                    - `BetaManagedAgentsAutoPolicy object`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `BetaManagedAgentsGrepToolConfig object`

                  Configuration for the grep tool.

                  - `type: "grep"`

                  - `enabled: boolean`

                  - `name: "grep"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy object`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy object`

                      Tool calls require user confirmation before execution.

                    - `BetaManagedAgentsAutoPolicy object`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `BetaManagedAgentsWebFetchToolConfig object`

                  Configuration for the web_fetch tool.

                  - `type: "web_fetch"`

                  - `enabled: boolean`

                  - `name: "web_fetch"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy object`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy object`

                      Tool calls require user confirmation before execution.

                    - `BetaManagedAgentsAutoPolicy object`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `allowed_domains: optional array of string`

                  - `blocked_domains: optional array of string`

                  - `max_content_tokens: optional number or null`

                    format: int32

                - `BetaManagedAgentsWebSearchToolConfig object`

                  Configuration for the web_search tool.

                  - `type: "web_search"`

                  - `enabled: boolean`

                  - `name: "web_search"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy object`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy object`

                      Tool calls require user confirmation before execution.

                    - `BetaManagedAgentsAutoPolicy object`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `allowed_domains: optional array of string`

                  - `blocked_domains: optional array of string`

                  - `user_location: optional BetaManagedAgentsUserLocation or null`

                    Approximate user location for search result localization.

                    - `type: "approximate"`

                      Location precision. Only "approximate" is supported.

                    - `city: optional string or null`

                      City name.

                      minLength: 1, maxLength: 255

                    - `country: optional string or null`

                      Two-letter ISO 3166-1 country code, uppercase.

                    - `region: optional string or null`

                      Region or state name.

                      minLength: 1, maxLength: 255

                    - `timezone: optional string or null`

                      IANA timezone identifier, e.g. "America/Los_Angeles".

                      minLength: 1, maxLength: 255

              - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

                Resolved default configuration for agent tools.

                - `enabled: boolean`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                  Permission policy for tool execution.

                  - `BetaManagedAgentsAlwaysAllowPolicy object`

                    Tool calls are automatically approved without user confirmation.

                  - `BetaManagedAgentsAlwaysAskPolicy object`

                    Tool calls require user confirmation before execution.

                  - `BetaManagedAgentsAutoPolicy object`

                    The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `BetaManagedAgentsMCPToolset object`

              - `type: "mcp_toolset"`

              - `configs: array of BetaManagedAgentsMCPToolConfig`

                - `enabled: boolean`

                - `name: string`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                  Permission policy for tool execution.

                  - `BetaManagedAgentsAlwaysAllowPolicy object`

                    Tool calls are automatically approved without user confirmation.

                  - `BetaManagedAgentsAlwaysAskPolicy object`

                    Tool calls require user confirmation before execution.

                  - `BetaManagedAgentsAutoPolicy object`

                    The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `enabled: boolean`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

                  Permission policy for tool execution.

                  - `BetaManagedAgentsAlwaysAllowPolicy object`

                    Tool calls are automatically approved without user confirmation.

                  - `BetaManagedAgentsAlwaysAskPolicy object`

                    Tool calls require user confirmation before execution.

                  - `BetaManagedAgentsAutoPolicy object`

                    The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `mcp_server_name: string`

            - `BetaManagedAgentsCustomTool object`

              A custom tool as returned in API responses.

              - `type: "custom"`

              - `description: string`

              - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                JSON Schema for custom tool input parameters.

                - `type: "object"`

                - `properties: optional map[unknown] or null`

                - `required: optional array of string or null`

              - `name: string`

          - `version: number`

            format: int32

        - `BetaManagedAgentsAdvisor object`

          Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

          - `type: "advisor"`

          - `model: string`

            The advisor model id.

    - `name: string`

    - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

      - `BetaManagedAgentsAnthropicSkill object`

        A resolved Anthropic-managed skill.

      - `BetaManagedAgentsCustomSkill object`

        A resolved user-created custom skill.

    - `system: string or null`

    - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

      - `BetaManagedAgentsAgentToolset20260401 object`

      - `BetaManagedAgentsMCPToolset object`

      - `BetaManagedAgentsCustomTool object`

        A custom tool as returned in API responses.

    - `version: number`

      format: int32

  - `archived_at: string or null`

    A timestamp in RFC 3339 format

    format: date-time

  - `budget: BetaManagedAgentsBudgetLimit or null`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `type: "limit"`

    - `max_list_cost: BetaMonetaryAmount`

      A monetary amount in a specific currency.

      - `amount: string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `environment_id: string`

  - `metadata: map[string]`

  - `outcome_evaluations: array of BetaManagedAgentsOutcomeEvaluationResource`

    Per-outcome evaluation state. One entry per `define_outcome` event sent to the session.

    - `type: "outcome_evaluation"`

    - `completed_at: string or null`

      A timestamp in RFC 3339 format

      format: date-time

    - `description: string`

      What the agent should produce.

    - `explanation: string or null`

      Grader's verdict text from the most recent evaluation. For `satisfied`, explains why criteria are met; for `needs_revision` (intermediate), what's missing; for `failed`, why unrecoverable.

    - `iteration: number`

      0-indexed revision cycle the outcome is currently on.

      format: int32

    - `outcome_id: string`

      Server-generated outc_ ID for this outcome.

    - `result: string`

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

  - `resources: array of BetaManagedAgentsSessionResource`

    - `BetaManagedAgentsGitHubRepositoryResource object`

      - `type: "github_repository"`

      - `id: string`

      - `created_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `mount_path: string`

      - `updated_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `url: string`

      - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout or null`

        - `BetaManagedAgentsBranchCheckout object`

          - `type: "branch"`

          - `name: string`

            Branch name to check out.

            minLength: 1, maxLength: 255

        - `BetaManagedAgentsCommitCheckout object`

          - `type: "commit"`

          - `sha: string`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

    - `BetaManagedAgentsFileResource object`

      - `type: "file"`

      - `id: string`

      - `created_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `file_id: string`

      - `mount_path: string`

      - `updated_at: string`

        A timestamp in RFC 3339 format

        format: date-time

    - `BetaManagedAgentsMemoryStoreResource object`

      A memory store attached to an agent session.

      - `type: "memory_store"`

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `access: optional "read_write" or "read_only" or null`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `description: optional string`

        Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

      - `instructions: optional string or null`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

        maxLength: 4096

      - `mount_path: optional string or null`

        Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

      - `name: optional string or null`

        Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

  - `stats: BetaManagedAgentsSessionStats`

    Timing statistics for a session.

    - `active_seconds: optional number`

      Cumulative time in seconds the session spent in `running` status. Excludes idle time.

      format: double

    - `duration_seconds: optional number`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

      format: double

  - `status: "rescheduling" or "running" or "idle" or "terminated"`

    SessionStatus enum

    - `"rescheduling"`

    - `"running"`

    - `"idle"`

    - `"terminated"`

  - `title: string or null`

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `usage: BetaManagedAgentsSessionUsage`

    Cumulative token usage for a session across all turns.

    - `active_seconds: optional number`

      Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once, unlike `stats.active_seconds`, which sums each thread's own active time. This is the duration the session's runtime cost is priced on.

      format: double

    - `cache_creation: optional BetaManagedAgentsCacheCreationUsage`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: optional number`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `ephemeral_5m_input_tokens: optional number`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `cache_read_input_tokens: optional number`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens: optional number`

      Total input tokens consumed across all turns.

      format: int32

    - `list_cost: optional BetaMonetaryAmount or null`

      A monetary amount in a specific currency.

    - `output_tokens: optional number`

      Total output tokens generated across all turns.

      format: int32

    - `server_tool_use: optional BetaManagedAgentsServerToolUsage or null`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `web_fetch_requests: optional number`

        Number of server-executed web fetch requests.

        format: int32

      - `web_search_requests: optional number`

        Number of server-executed web search requests.

        format: int32

  - `vault_ids: array of string`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `deployment_id: optional string or null`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

## Example

```bash
curl https://api.anthropic.com/v1/sessions \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "agent": "agent_011CZkYpogX7uDKUyvBTophP",
          "environment_id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
          "title": "Order #1234 inquiry"
        }'
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
