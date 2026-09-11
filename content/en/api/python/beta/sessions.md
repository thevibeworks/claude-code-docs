---
title: Sessions
url: https://platform.claude.com/docs/en/api/python/beta/sessions
---

# Sessions

## Create Session

`beta.sessions.create(**kwargs)  -> BetaManagedAgentsSession`

**POST** `/v1/sessions`

Create Session

### Parameters

- `agent: Agent`

  Agent identifier. Accepts the `agent` ID string, which pins the latest version for the session, or an `agent` object with both id and version specified.

  - `str`

  - `class BetaManagedAgentsAgentParams: …`

    Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

    - `type: Literal["agent"]`

    - `id: str`

      The `agent` ID.

      minLength: 1, maxLength: 128

    - `version: Optional[int]`

      The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

      format: int32

  - `class BetaManagedAgentsAgentWithOverridesParams: …`

    Reference to an `agent` plus optional configuration overrides. Each provided field replaces the agent's value for the caller's use; the agent resource is unchanged.

    - `type: Literal["agent_with_overrides"]`

    - `id: str`

      The `agent` ID.

      minLength: 1, maxLength: 128

    - `mcp_servers: Optional[List[BetaManagedAgentsURLMCPServerParams]]`

      Replacement MCP server list. Full replacement: the provided array becomes the MCP servers. Send an empty array to clear; omit to preserve the agent's servers.

      - `type: Literal["url"]`

      - `name: str`

        Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

        minLength: 1, maxLength: 255

      - `url: str`

        Endpoint URL for the MCP server.

        maxLength: 2048

    - `model: Optional[Model]`

      Replacement model. Accepts the model string, e.g. `claude-opus-5`, or a `model_config` object. Omit to use the agent's model.

      - `Union[Literal["claude-fable-5-1", "claude-sonnet-5", "claude-fable-5", 11 more], str]`

        - `Literal["claude-fable-5-1", "claude-sonnet-5", "claude-fable-5", 11 more]`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `claude-fable-5-1` - Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows
          - `claude-sonnet-5` - High-performance model for coding and agents
          - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
          - `claude-opus-5` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-8` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-7` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-6` - Powerful intelligence for long-running agents and coding
          - `claude-sonnet-4-6` - Best combination of speed and intelligence
          - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
          - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
          - `claude-opus-4-5` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-5-20251101` - Powerful intelligence for long-running agents and coding
          - `claude-sonnet-4-5` - High-performance model for agents and coding
          - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

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

        - `str`

      - `class BetaManagedAgentsModelConfigParams: …`

        An object that defines additional configuration control over model use

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `Literal["claude-fable-5-1", "claude-sonnet-5", "claude-fable-5", 11 more]`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `claude-fable-5-1` - Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows
            - `claude-sonnet-5` - High-performance model for coding and agents
            - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
            - `claude-opus-5` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-8` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-7` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-6` - Powerful intelligence for long-running agents and coding
            - `claude-sonnet-4-6` - Best combination of speed and intelligence
            - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
            - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
            - `claude-opus-4-5` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-5-20251101` - Powerful intelligence for long-running agents and coding
            - `claude-sonnet-4-5` - High-performance model for agents and coding
            - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

          - `str`

        - `effort: Optional[Effort]`

          How hard Claude works on each inference call. Accepts a bare level string (`"high"`) or `{"type": "high"}`. On create, omitting it resolves the per-model default; on update, omitting it leaves the stored value unchanged.

          - `Literal["low", "medium", "high", 2 more]`

            How hard Claude works on each turn. Higher levels favor reasoning depth over latency. Not all models accept every level; invalid combinations are rejected at create time.

            - `"low"`

            - `"medium"`

            - `"high"`

            - `"xhigh"`

            - `"max"`

          - `class BetaManagedAgentsEffortLow: …`

            Low effort. Favors latency over reasoning depth.

            - `type: Literal["low"]`

          - `class BetaManagedAgentsEffortMedium: …`

            Medium effort. Balances latency and reasoning depth.

            - `type: Literal["medium"]`

          - `class BetaManagedAgentsEffortHigh: …`

            High effort. Favors reasoning depth.

            - `type: Literal["high"]`

          - `class BetaManagedAgentsEffortXhigh: …`

            Extra-high effort. Not all models accept this level.

            - `type: Literal["xhigh"]`

          - `class BetaManagedAgentsEffortMax: …`

            Maximum effort. Favors reasoning depth over latency.

            - `type: Literal["max"]`

        - `inference_geo: Optional[str]`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo. On update, `model` is whole-object replacement — omitting inference_geo clears it.

        - `speed: Optional[Literal["standard", "fast"]]`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

    - `skills: Optional[List[BetaManagedAgentsSkillParams]]`

      Replacement skill list. Full replacement: the provided array becomes the skills. Send an empty array to clear; omit to preserve the agent's skills.

      - `class BetaManagedAgentsAnthropicSkillParams: …`

        An Anthropic-managed skill.

        - `type: Literal["anthropic"]`

        - `skill_id: str`

          Identifier of the Anthropic skill (e.g., "xlsx").

          minLength: 1, maxLength: 64

        - `version: Optional[str]`

          Version to pin. Defaults to latest if omitted.

          minLength: 1, maxLength: 64

      - `class BetaManagedAgentsCustomSkillParams: …`

        A user-created custom skill.

        - `type: Literal["custom"]`

        - `skill_id: str`

          Tagged ID of the custom skill (e.g., "skill_01XJ5...").

          minLength: 1, maxLength: 64

        - `version: Optional[str]`

          Version to pin. Defaults to latest if omitted.

          minLength: 1, maxLength: 64

    - `system: Optional[str]`

      Replacement system prompt. Up to 100,000 characters. Set to null to clear the agent's system prompt; omit to preserve it.

      maxLength: 100000

    - `tools: Optional[List[Tool]]`

      Replacement tool list. Full replacement: the provided array becomes the tool configuration. Send an empty array to clear; omit to preserve the agent's tools.

      - `class BetaManagedAgentsAgentToolset20260401Params: …`

        Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

        - `type: Literal["agent_toolset_20260401"]`

        - `configs: Optional[List[BetaManagedAgentsAgentToolConfigParams]]`

          Per-tool configuration overrides.

          - `class BetaManagedAgentsBashToolConfigParams: …`

            Configuration override for the bash tool.

            - `type: Optional[Literal["bash"]]`

            - `name: Literal["bash"]`

              Must be "bash".

            - `enabled: Optional[bool]`

              Whether this tool is enabled and available to Claude. Overrides the default_config setting.

            - `permission_policy: Optional[PermissionPolicy]`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                Tool calls are automatically approved without user confirmation.

                - `type: Literal["always_allow"]`

              - `class BetaManagedAgentsAlwaysAskPolicy: …`

                Tool calls require user confirmation before execution.

                - `type: Literal["always_ask"]`

              - `class BetaManagedAgentsAutoPolicy: …`

                The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `type: Literal["auto"]`

          - `class BetaManagedAgentsEditToolConfigParams: …`

            Configuration override for the edit tool.

            - `type: Optional[Literal["edit"]]`

            - `name: Literal["edit"]`

              Must be "edit".

            - `enabled: Optional[bool]`

              Whether this tool is enabled and available to Claude. Overrides the default_config setting.

            - `permission_policy: Optional[PermissionPolicy]`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy: …`

                Tool calls require user confirmation before execution.

              - `class BetaManagedAgentsAutoPolicy: …`

                The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

          - `class BetaManagedAgentsReadToolConfigParams: …`

            Configuration override for the read tool.

            - `type: Optional[Literal["read"]]`

            - `name: Literal["read"]`

              Must be "read".

            - `enabled: Optional[bool]`

              Whether this tool is enabled and available to Claude. Overrides the default_config setting.

            - `permission_policy: Optional[PermissionPolicy]`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy: …`

                Tool calls require user confirmation before execution.

              - `class BetaManagedAgentsAutoPolicy: …`

                The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

          - `class BetaManagedAgentsWriteToolConfigParams: …`

            Configuration override for the write tool.

            - `type: Optional[Literal["write"]]`

            - `name: Literal["write"]`

              Must be "write".

            - `enabled: Optional[bool]`

              Whether this tool is enabled and available to Claude. Overrides the default_config setting.

            - `permission_policy: Optional[PermissionPolicy]`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy: …`

                Tool calls require user confirmation before execution.

              - `class BetaManagedAgentsAutoPolicy: …`

                The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

          - `class BetaManagedAgentsGlobToolConfigParams: …`

            Configuration override for the glob tool.

            - `type: Optional[Literal["glob"]]`

            - `name: Literal["glob"]`

              Must be "glob".

            - `enabled: Optional[bool]`

              Whether this tool is enabled and available to Claude. Overrides the default_config setting.

            - `permission_policy: Optional[PermissionPolicy]`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy: …`

                Tool calls require user confirmation before execution.

              - `class BetaManagedAgentsAutoPolicy: …`

                The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

          - `class BetaManagedAgentsGrepToolConfigParams: …`

            Configuration override for the grep tool.

            - `type: Optional[Literal["grep"]]`

            - `name: Literal["grep"]`

              Must be "grep".

            - `enabled: Optional[bool]`

              Whether this tool is enabled and available to Claude. Overrides the default_config setting.

            - `permission_policy: Optional[PermissionPolicy]`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy: …`

                Tool calls require user confirmation before execution.

              - `class BetaManagedAgentsAutoPolicy: …`

                The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

          - `class BetaManagedAgentsWebFetchToolConfigParams: …`

            Configuration override for the web_fetch tool.

            - `type: Optional[Literal["web_fetch"]]`

            - `name: Literal["web_fetch"]`

              Must be "web_fetch".

            - `allowed_domains: Optional[List[str]]`

              Only fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

            - `blocked_domains: Optional[List[str]]`

              Never fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

            - `enabled: Optional[bool]`

              Whether this tool is enabled and available to Claude. Overrides the default_config setting.

            - `max_content_tokens: Optional[int]`

              Maximum number of tokens of fetched text content to include in context per call. Does not apply to binary content such as PDFs.

              format: int32

            - `permission_policy: Optional[PermissionPolicy]`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy: …`

                Tool calls require user confirmation before execution.

              - `class BetaManagedAgentsAutoPolicy: …`

                The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

          - `class BetaManagedAgentsWebSearchToolConfigParams: …`

            Configuration override for the web_search tool.

            - `type: Optional[Literal["web_search"]]`

            - `name: Literal["web_search"]`

              Must be "web_search".

            - `allowed_domains: Optional[List[str]]`

              Only return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

            - `blocked_domains: Optional[List[str]]`

              Never return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

            - `enabled: Optional[bool]`

              Whether this tool is enabled and available to Claude. Overrides the default_config setting.

            - `permission_policy: Optional[PermissionPolicy]`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy: …`

                Tool calls require user confirmation before execution.

              - `class BetaManagedAgentsAutoPolicy: …`

                The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `user_location: Optional[BetaManagedAgentsUserLocation]`

              Approximate user location for search result localization.

              - `type: Literal["approximate"]`

                Location precision. Only "approximate" is supported.

              - `city: Optional[str]`

                City name.

                minLength: 1, maxLength: 255

              - `country: Optional[str]`

                Two-letter ISO 3166-1 country code, uppercase.

              - `region: Optional[str]`

                Region or state name.

                minLength: 1, maxLength: 255

              - `timezone: Optional[str]`

                IANA timezone identifier, e.g. "America/Los_Angeles".

                minLength: 1, maxLength: 255

        - `default_config: Optional[BetaManagedAgentsAgentToolsetDefaultConfigParams]`

          Default configuration for all tools in a toolset.

          - `enabled: Optional[bool]`

            Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

          - `permission_policy: Optional[PermissionPolicy]`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

            - `class BetaManagedAgentsAutoPolicy: …`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

      - `class BetaManagedAgentsMCPToolsetParams: …`

        Configuration for tools from an MCP server defined in `mcp_servers`.

        - `type: Literal["mcp_toolset"]`

        - `mcp_server_name: str`

          Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

          minLength: 1, maxLength: 255

        - `configs: Optional[List[BetaManagedAgentsMCPToolConfigParams]]`

          Per-tool configuration overrides.

          - `name: str`

            Name of the MCP tool to configure. 1-128 characters.

            minLength: 1, maxLength: 128

          - `enabled: Optional[bool]`

            Whether this tool is enabled. Overrides the `default_config` setting.

          - `permission_policy: Optional[PermissionPolicy]`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

            - `class BetaManagedAgentsAutoPolicy: …`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

        - `default_config: Optional[BetaManagedAgentsMCPToolsetDefaultConfigParams]`

          Default configuration for all tools from an MCP server.

          - `enabled: Optional[bool]`

            Whether tools are enabled by default. Defaults to true if not specified.

          - `permission_policy: Optional[PermissionPolicy]`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

            - `class BetaManagedAgentsAutoPolicy: …`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

      - `class BetaManagedAgentsCustomToolParams: …`

        A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

        - `type: Literal["custom"]`

        - `description: str`

          Description of what the tool does, shown to the agent to help it decide when to use the tool.

          minLength: 1

        - `input_schema: BetaManagedAgentsCustomToolInputSchema`

          JSON Schema for custom tool input parameters.

          - `type: Literal["object"]`

          - `properties: Optional[Dict[str, object]]`

          - `required: Optional[List[str]]`

        - `name: str`

          Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

          minLength: 1, maxLength: 128

    - `version: Optional[int]`

      The specific `agent` version to use. Omit to use the latest version.

      format: int32

- `environment_id: str`

  ID of the `environment` defining the container configuration for this session.

  minLength: 1, maxLength: 128

- `budget: Optional[BetaManagedAgentsBudgetLimitParam]`

  A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

  - `type: Literal["limit"]`

  - `max_list_cost: BetaMonetaryAmount`

    A monetary amount in a specific currency.

    - `amount: str`

      Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

    - `currency: BetaCurrency`

      Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

- `initial_events: Optional[Iterable[InitialEvent]]`

  Initial events to send to the `session` at creation, processed in order. Supports `user.message` and `user.define_outcome` events. Maximum 50 events.

  - `class BetaManagedAgentsUserMessageEventParams: …`

    Parameters for sending a user message to the session.

    - `type: Literal["user.message"]`

    - `content: Iterable[Content]`

      Array of content blocks for the user message.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

        - `type: Literal["text"]`

        - `text: str`

          The text content.

          minLength: 1

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

        - `type: Literal["image"]`

        - `source: Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource: …`

            Base64-encoded image data.

            - `type: Literal["base64"]`

            - `data: str`

              Base64-encoded image data.

              minLength: 1

            - `media_type: str`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

          - `class BetaManagedAgentsURLImageSource: …`

            Image referenced by URL.

            - `type: Literal["url"]`

            - `url: str`

              URL of the image to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileImageSource: …`

            Image referenced by file ID.

            - `type: Literal["file"]`

            - `file_id: str`

              ID of a previously uploaded file.

              minLength: 1

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `type: Literal["document"]`

        - `source: Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource: …`

            Base64-encoded document data.

            - `type: Literal["base64"]`

            - `data: str`

              Base64-encoded document data.

              minLength: 1

            - `media_type: str`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

          - `class BetaManagedAgentsPlainTextDocumentSource: …`

            Plain text document content.

            - `type: Literal["text"]`

            - `data: str`

              The plain text content.

              minLength: 1

            - `media_type: Literal["text/plain"]`

              MIME type of the text content. Must be "text/plain".

          - `class BetaManagedAgentsURLDocumentSource: …`

            Document referenced by URL.

            - `type: Literal["url"]`

            - `url: str`

              URL of the document to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileDocumentSource: …`

            Document referenced by file ID.

            - `type: Literal["file"]`

            - `file_id: str`

              ID of a previously uploaded file.

              minLength: 1

        - `context: Optional[str]`

          Additional context about the document for the model.

        - `title: Optional[str]`

          The title of the document.

      - `class BetaManagedAgentsRedactedBlock: …`

        Placeholder for content withheld by Anthropic model policy.

        - `type: Literal["redacted"]`

  - `class BetaManagedAgentsUserDefineOutcomeEventParams: …`

    Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

    - `type: Literal["user.define_outcome"]`

    - `description: str`

      What the agent should produce. This is the task specification.

    - `rubric: Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubricParams: …`

        Rubric referenced by a file uploaded via the Files API.

        - `type: Literal["file"]`

        - `file_id: str`

          ID of the rubric file.

      - `class BetaManagedAgentsTextRubricParams: …`

        Rubric content provided inline as text.

        - `type: Literal["text"]`

        - `content: str`

          Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

          maxLength: 262144

    - `max_iterations: Optional[int]`

      Eval→revision cycles before giving up. Default 3, max 20.

      format: int32

- `metadata: Optional[Dict[str, str]]`

  Arbitrary key-value metadata attached to the session. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `resources: Optional[Iterable[Resource]]`

  Resources (e.g. repositories, files) to mount into the session's container.

  - `class BetaManagedAgentsGitHubRepositoryResourceParams: …`

    Mount a GitHub repository into the session's container.

    - `type: Literal["github_repository"]`

    - `url: str`

      Github URL of the repository

      minLength: 1, maxLength: 2048

    - `authorization_token: Optional[str]`

      GitHub authorization token used to clone the repository. Required for private repositories; optional for public ones.

      minLength: 1, maxLength: 4096

    - `checkout: Optional[Checkout]`

      Branch or commit to check out. Defaults to the repository's default branch.

      - `class BetaManagedAgentsBranchCheckout: …`

        - `type: Literal["branch"]`

        - `name: str`

          Branch name to check out.

          minLength: 1, maxLength: 255

      - `class BetaManagedAgentsCommitCheckout: …`

        - `type: Literal["commit"]`

        - `sha: str`

          Full commit SHA to check out.

          minLength: 7, maxLength: 64

    - `mount_path: Optional[str]`

      Mount path in the container. Defaults to `/workspace/<repo-name>`.

      minLength: 1, maxLength: 4096

  - `class BetaManagedAgentsFileResourceParams: …`

    Mount a file uploaded via the Files API into the session.

    - `type: Literal["file"]`

    - `file_id: str`

      ID of a previously uploaded file.

      minLength: 1, maxLength: 128

    - `mount_path: Optional[str]`

      Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

      minLength: 1, maxLength: 4096

  - `class BetaManagedAgentsMemoryStoreResourceParam: …`

    Parameters for attaching a memory store to an agent session.

    - `type: Literal["memory_store"]`

    - `memory_store_id: str`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `access: Optional[Literal["read_write", "read_only"]]`

      Access mode for an attached memory store.

      - `"read_write"`

      - `"read_only"`

    - `instructions: Optional[str]`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      maxLength: 4096

- `title: Optional[str]`

  Human-readable session title.

  maxLength: 500

- `vault_ids: Optional[Sequence[str]]`

  Vault IDs for stored credentials the agent can use during the session.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

- `workspace_id: Optional[str]`

### Returns

- `class BetaManagedAgentsSession: …`

  A Managed Agents `session`.

  - `type: Literal["session"]`

  - `id: str`

  - `agent: BetaManagedAgentsSessionAgent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `type: Literal["agent"]`

    - `id: str`

    - `description: Optional[str]`

    - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

      - `type: Literal["url"]`

      - `name: str`

      - `url: str`

    - `model: BetaManagedAgentsModelConfig`

      Model identifier and configuration.

      - `id: BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `Literal["claude-fable-5-1", "claude-sonnet-5", "claude-fable-5", 11 more]`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `claude-fable-5-1` - Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows
          - `claude-sonnet-5` - High-performance model for coding and agents
          - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
          - `claude-opus-5` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-8` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-7` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-6` - Powerful intelligence for long-running agents and coding
          - `claude-sonnet-4-6` - Best combination of speed and intelligence
          - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
          - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
          - `claude-opus-4-5` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-5-20251101` - Powerful intelligence for long-running agents and coding
          - `claude-sonnet-4-5` - High-performance model for agents and coding
          - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

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

        - `str`

      - `effort: Optional[Effort]`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

        - `class BetaManagedAgentsEffortLow: …`

          Low effort. Favors latency over reasoning depth.

          - `type: Literal["low"]`

        - `class BetaManagedAgentsEffortMedium: …`

          Medium effort. Balances latency and reasoning depth.

          - `type: Literal["medium"]`

        - `class BetaManagedAgentsEffortHigh: …`

          High effort. Favors reasoning depth.

          - `type: Literal["high"]`

        - `class BetaManagedAgentsEffortXhigh: …`

          Extra-high effort. Not all models accept this level.

          - `type: Literal["xhigh"]`

        - `class BetaManagedAgentsEffortMax: …`

          Maximum effort. Favors reasoning depth over latency.

          - `type: Literal["max"]`

      - `inference_geo: Optional[str]`

        Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

      - `speed: Optional[Literal["standard", "fast"]]`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `multiagent: Optional[BetaManagedAgentsSessionMultiagentCoordinator]`

      Resolved coordinator topology with full agent definitions for each roster member.

      - `type: Literal["coordinator"]`

      - `agents: List[Agent]`

        Full `agent` definitions the coordinator may spawn as session threads.

        - `class BetaManagedAgentsSessionThreadAgent: …`

          Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

          - `type: Literal["agent"]`

          - `id: str`

          - `description: Optional[str]`

          - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

            - `type: Literal["url"]`

            - `name: str`

            - `url: str`

          - `model: BetaManagedAgentsModelConfig`

            Model identifier and configuration.

          - `name: str`

          - `skills: List[Skill]`

            - `class BetaManagedAgentsAnthropicSkill: …`

              A resolved Anthropic-managed skill.

              - `type: Literal["anthropic"]`

              - `skill_id: str`

              - `version: str`

            - `class BetaManagedAgentsCustomSkill: …`

              A resolved user-created custom skill.

              - `type: Literal["custom"]`

              - `skill_id: str`

              - `version: str`

          - `system: Optional[str]`

          - `tools: List[Tool]`

            - `class BetaManagedAgentsAgentToolset20260401: …`

              - `type: Literal["agent_toolset_20260401"]`

              - `configs: List[BetaManagedAgentsAgentToolConfig]`

                - `class BetaManagedAgentsBashToolConfig: …`

                  Configuration for the bash tool.

                  - `type: Literal["bash"]`

                  - `enabled: bool`

                  - `name: Literal["bash"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                      - `type: Literal["always_allow"]`

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                      - `type: Literal["always_ask"]`

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                      - `type: Literal["auto"]`

                - `class BetaManagedAgentsEditToolConfig: …`

                  Configuration for the edit tool.

                  - `type: Literal["edit"]`

                  - `enabled: bool`

                  - `name: Literal["edit"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `class BetaManagedAgentsReadToolConfig: …`

                  Configuration for the read tool.

                  - `type: Literal["read"]`

                  - `enabled: bool`

                  - `name: Literal["read"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `class BetaManagedAgentsWriteToolConfig: …`

                  Configuration for the write tool.

                  - `type: Literal["write"]`

                  - `enabled: bool`

                  - `name: Literal["write"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `class BetaManagedAgentsGlobToolConfig: …`

                  Configuration for the glob tool.

                  - `type: Literal["glob"]`

                  - `enabled: bool`

                  - `name: Literal["glob"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `class BetaManagedAgentsGrepToolConfig: …`

                  Configuration for the grep tool.

                  - `type: Literal["grep"]`

                  - `enabled: bool`

                  - `name: Literal["grep"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `class BetaManagedAgentsWebFetchToolConfig: …`

                  Configuration for the web_fetch tool.

                  - `type: Literal["web_fetch"]`

                  - `enabled: bool`

                  - `name: Literal["web_fetch"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `allowed_domains: Optional[List[str]]`

                  - `blocked_domains: Optional[List[str]]`

                  - `max_content_tokens: Optional[int]`

                    format: int32

                - `class BetaManagedAgentsWebSearchToolConfig: …`

                  Configuration for the web_search tool.

                  - `type: Literal["web_search"]`

                  - `enabled: bool`

                  - `name: Literal["web_search"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `allowed_domains: Optional[List[str]]`

                  - `blocked_domains: Optional[List[str]]`

                  - `user_location: Optional[BetaManagedAgentsUserLocation]`

                    Approximate user location for search result localization.

                    - `type: Literal["approximate"]`

                      Location precision. Only "approximate" is supported.

                    - `city: Optional[str]`

                      City name.

                      minLength: 1, maxLength: 255

                    - `country: Optional[str]`

                      Two-letter ISO 3166-1 country code, uppercase.

                    - `region: Optional[str]`

                      Region or state name.

                      minLength: 1, maxLength: 255

                    - `timezone: Optional[str]`

                      IANA timezone identifier, e.g. "America/Los_Angeles".

                      minLength: 1, maxLength: 255

              - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

                Resolved default configuration for agent tools.

                - `enabled: bool`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

                  - `class BetaManagedAgentsAutoPolicy: …`

                    The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `class BetaManagedAgentsMCPToolset: …`

              - `type: Literal["mcp_toolset"]`

              - `configs: List[BetaManagedAgentsMCPToolConfig]`

                - `enabled: bool`

                - `name: str`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

                  - `class BetaManagedAgentsAutoPolicy: …`

                    The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `enabled: bool`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

                  - `class BetaManagedAgentsAutoPolicy: …`

                    The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `mcp_server_name: str`

            - `class BetaManagedAgentsCustomTool: …`

              A custom tool as returned in API responses.

              - `type: Literal["custom"]`

              - `description: str`

              - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                JSON Schema for custom tool input parameters.

                - `type: Literal["object"]`

                - `properties: Optional[Dict[str, object]]`

                - `required: Optional[List[str]]`

              - `name: str`

          - `version: int`

            format: int32

        - `class BetaManagedAgentsAdvisor: …`

          Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

          - `type: Literal["advisor"]`

          - `model: str`

            The advisor model id.

    - `name: str`

    - `skills: List[Skill]`

      - `class BetaManagedAgentsAnthropicSkill: …`

        A resolved Anthropic-managed skill.

      - `class BetaManagedAgentsCustomSkill: …`

        A resolved user-created custom skill.

    - `system: Optional[str]`

    - `tools: List[Tool]`

      - `class BetaManagedAgentsAgentToolset20260401: …`

      - `class BetaManagedAgentsMCPToolset: …`

      - `class BetaManagedAgentsCustomTool: …`

        A custom tool as returned in API responses.

    - `version: int`

      format: int32

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

    format: date-time

  - `budget: Optional[BetaManagedAgentsBudgetLimit]`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `type: Literal["limit"]`

    - `max_list_cost: BetaMonetaryAmount`

      A monetary amount in a specific currency.

      - `amount: str`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

  - `created_at: datetime`

    A timestamp in RFC 3339 format

    format: date-time

  - `environment_id: str`

  - `metadata: Dict[str, str]`

  - `outcome_evaluations: List[BetaManagedAgentsOutcomeEvaluationResource]`

    Per-outcome evaluation state. One entry per `define_outcome` event sent to the session.

    - `type: Literal["outcome_evaluation"]`

    - `completed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

      format: date-time

    - `description: str`

      What the agent should produce.

    - `explanation: Optional[str]`

      Grader's verdict text from the most recent evaluation. For `satisfied`, explains why criteria are met; for `needs_revision` (intermediate), what's missing; for `failed`, why unrecoverable.

    - `iteration: int`

      0-indexed revision cycle the outcome is currently on.

      format: int32

    - `outcome_id: str`

      Server-generated outc_ ID for this outcome.

    - `result: str`

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

  - `resources: List[BetaManagedAgentsSessionResource]`

    - `class BetaManagedAgentsGitHubRepositoryResource: …`

      - `type: Literal["github_repository"]`

      - `id: str`

      - `created_at: datetime`

        A timestamp in RFC 3339 format

        format: date-time

      - `mount_path: str`

      - `updated_at: datetime`

        A timestamp in RFC 3339 format

        format: date-time

      - `url: str`

      - `checkout: Optional[Checkout]`

        - `class BetaManagedAgentsBranchCheckout: …`

          - `type: Literal["branch"]`

          - `name: str`

            Branch name to check out.

            minLength: 1, maxLength: 255

        - `class BetaManagedAgentsCommitCheckout: …`

          - `type: Literal["commit"]`

          - `sha: str`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

    - `class BetaManagedAgentsFileResource: …`

      - `type: Literal["file"]`

      - `id: str`

      - `created_at: datetime`

        A timestamp in RFC 3339 format

        format: date-time

      - `file_id: str`

      - `mount_path: str`

      - `updated_at: datetime`

        A timestamp in RFC 3339 format

        format: date-time

    - `class BetaManagedAgentsMemoryStoreResource: …`

      A memory store attached to an agent session.

      - `type: Literal["memory_store"]`

      - `memory_store_id: str`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `access: Optional[Literal["read_write", "read_only"]]`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `description: Optional[str]`

        Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

      - `instructions: Optional[str]`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

        maxLength: 4096

      - `mount_path: Optional[str]`

        Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

      - `name: Optional[str]`

        Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

  - `stats: BetaManagedAgentsSessionStats`

    Timing statistics for a session.

    - `active_seconds: Optional[float]`

      Cumulative time in seconds the session spent in `running` status. Excludes idle time.

      format: double

    - `duration_seconds: Optional[float]`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

      format: double

  - `status: Literal["rescheduling", "running", "idle", "terminated"]`

    SessionStatus enum

    - `"rescheduling"`

    - `"running"`

    - `"idle"`

    - `"terminated"`

  - `title: Optional[str]`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

    format: date-time

  - `usage: BetaManagedAgentsSessionUsage`

    Cumulative token usage for a session across all turns.

    - `active_seconds: Optional[float]`

      Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once, unlike `stats.active_seconds`, which sums each thread's own active time. This is the duration the session's runtime cost is priced on.

      format: double

    - `cache_creation: Optional[BetaManagedAgentsCacheCreationUsage]`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: Optional[int]`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `ephemeral_5m_input_tokens: Optional[int]`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `cache_read_input_tokens: Optional[int]`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens: Optional[int]`

      Total input tokens consumed across all turns.

      format: int32

    - `list_cost: Optional[BetaMonetaryAmount]`

      A monetary amount in a specific currency.

    - `output_tokens: Optional[int]`

      Total output tokens generated across all turns.

      format: int32

    - `server_tool_use: Optional[BetaManagedAgentsServerToolUsage]`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `web_fetch_requests: Optional[int]`

        Number of server-executed web fetch requests.

        format: int32

      - `web_search_requests: Optional[int]`

        Number of server-executed web search requests.

        format: int32

  - `vault_ids: List[str]`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `deployment_id: Optional[str]`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_managed_agents_session = client.beta.sessions.create(
    agent="agent_011CZkYpogX7uDKUyvBTophP",
    environment_id="env_011CZkZ9X2dpNyB7HsEFoRfW",
)
print(beta_managed_agents_session.id)
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

`beta.sessions.list(**kwargs)  -> SyncBidirectionalPageCursor[BetaManagedAgentsSession]`

**GET** `/v1/sessions`

List Sessions

### Parameters

- `agent_id: Optional[str]`

  Filter sessions created with this agent ID.

- `agent_version: Optional[int]`

  Filter by agent version. Only applies when `agent_id` is also set.

  format: int32

- `created_at_gt: Optional[Union[str, datetime]]`

  Return sessions created after this time (exclusive).

  format: date-time

- `created_at_gte: Optional[Union[str, datetime]]`

  Return sessions created at or after this time (inclusive).

  format: date-time

- `created_at_lt: Optional[Union[str, datetime]]`

  Return sessions created before this time (exclusive).

  format: date-time

- `created_at_lte: Optional[Union[str, datetime]]`

  Return sessions created at or before this time (inclusive).

  format: date-time

- `deployment_id: Optional[str]`

  Filter sessions created by this deployment ID.

- `include_archived: Optional[bool]`

  When true, includes archived sessions. Default: false (exclude archived).

- `limit: Optional[int]`

  Maximum number of results to return.

  format: int32

- `memory_store_id: Optional[str]`

  Filter sessions whose resources contain a `memory_store` with this memory store ID.

- `order: Optional[Literal["asc", "desc"]]`

  Sort direction for results, ordered by `created_at`. Defaults to `desc` (newest first).

  - `"asc"`

  - `"desc"`

- `page: Optional[str]`

  Opaque pagination cursor from a previous response.

- `statuses: Optional[List[Literal["rescheduling", "running", "idle", "terminated"]]]`

  Filter by session status. Repeat the parameter to match any of multiple statuses.

  - `"rescheduling"`

  - `"running"`

  - `"idle"`

  - `"terminated"`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

- `workspace_id: Optional[str]`

### Returns

- `class BetaManagedAgentsSession: …`

  A Managed Agents `session`.

  - `type: Literal["session"]`

  - `id: str`

  - `agent: BetaManagedAgentsSessionAgent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `type: Literal["agent"]`

    - `id: str`

    - `description: Optional[str]`

    - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

      - `type: Literal["url"]`

      - `name: str`

      - `url: str`

    - `model: BetaManagedAgentsModelConfig`

      Model identifier and configuration.

      - `id: BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `Literal["claude-fable-5-1", "claude-sonnet-5", "claude-fable-5", 11 more]`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `claude-fable-5-1` - Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows
          - `claude-sonnet-5` - High-performance model for coding and agents
          - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
          - `claude-opus-5` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-8` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-7` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-6` - Powerful intelligence for long-running agents and coding
          - `claude-sonnet-4-6` - Best combination of speed and intelligence
          - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
          - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
          - `claude-opus-4-5` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-5-20251101` - Powerful intelligence for long-running agents and coding
          - `claude-sonnet-4-5` - High-performance model for agents and coding
          - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

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

        - `str`

      - `effort: Optional[Effort]`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

        - `class BetaManagedAgentsEffortLow: …`

          Low effort. Favors latency over reasoning depth.

          - `type: Literal["low"]`

        - `class BetaManagedAgentsEffortMedium: …`

          Medium effort. Balances latency and reasoning depth.

          - `type: Literal["medium"]`

        - `class BetaManagedAgentsEffortHigh: …`

          High effort. Favors reasoning depth.

          - `type: Literal["high"]`

        - `class BetaManagedAgentsEffortXhigh: …`

          Extra-high effort. Not all models accept this level.

          - `type: Literal["xhigh"]`

        - `class BetaManagedAgentsEffortMax: …`

          Maximum effort. Favors reasoning depth over latency.

          - `type: Literal["max"]`

      - `inference_geo: Optional[str]`

        Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

      - `speed: Optional[Literal["standard", "fast"]]`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `multiagent: Optional[BetaManagedAgentsSessionMultiagentCoordinator]`

      Resolved coordinator topology with full agent definitions for each roster member.

      - `type: Literal["coordinator"]`

      - `agents: List[Agent]`

        Full `agent` definitions the coordinator may spawn as session threads.

        - `class BetaManagedAgentsSessionThreadAgent: …`

          Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

          - `type: Literal["agent"]`

          - `id: str`

          - `description: Optional[str]`

          - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

            - `type: Literal["url"]`

            - `name: str`

            - `url: str`

          - `model: BetaManagedAgentsModelConfig`

            Model identifier and configuration.

          - `name: str`

          - `skills: List[Skill]`

            - `class BetaManagedAgentsAnthropicSkill: …`

              A resolved Anthropic-managed skill.

              - `type: Literal["anthropic"]`

              - `skill_id: str`

              - `version: str`

            - `class BetaManagedAgentsCustomSkill: …`

              A resolved user-created custom skill.

              - `type: Literal["custom"]`

              - `skill_id: str`

              - `version: str`

          - `system: Optional[str]`

          - `tools: List[Tool]`

            - `class BetaManagedAgentsAgentToolset20260401: …`

              - `type: Literal["agent_toolset_20260401"]`

              - `configs: List[BetaManagedAgentsAgentToolConfig]`

                - `class BetaManagedAgentsBashToolConfig: …`

                  Configuration for the bash tool.

                  - `type: Literal["bash"]`

                  - `enabled: bool`

                  - `name: Literal["bash"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                      - `type: Literal["always_allow"]`

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                      - `type: Literal["always_ask"]`

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                      - `type: Literal["auto"]`

                - `class BetaManagedAgentsEditToolConfig: …`

                  Configuration for the edit tool.

                  - `type: Literal["edit"]`

                  - `enabled: bool`

                  - `name: Literal["edit"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `class BetaManagedAgentsReadToolConfig: …`

                  Configuration for the read tool.

                  - `type: Literal["read"]`

                  - `enabled: bool`

                  - `name: Literal["read"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `class BetaManagedAgentsWriteToolConfig: …`

                  Configuration for the write tool.

                  - `type: Literal["write"]`

                  - `enabled: bool`

                  - `name: Literal["write"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `class BetaManagedAgentsGlobToolConfig: …`

                  Configuration for the glob tool.

                  - `type: Literal["glob"]`

                  - `enabled: bool`

                  - `name: Literal["glob"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `class BetaManagedAgentsGrepToolConfig: …`

                  Configuration for the grep tool.

                  - `type: Literal["grep"]`

                  - `enabled: bool`

                  - `name: Literal["grep"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `class BetaManagedAgentsWebFetchToolConfig: …`

                  Configuration for the web_fetch tool.

                  - `type: Literal["web_fetch"]`

                  - `enabled: bool`

                  - `name: Literal["web_fetch"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `allowed_domains: Optional[List[str]]`

                  - `blocked_domains: Optional[List[str]]`

                  - `max_content_tokens: Optional[int]`

                    format: int32

                - `class BetaManagedAgentsWebSearchToolConfig: …`

                  Configuration for the web_search tool.

                  - `type: Literal["web_search"]`

                  - `enabled: bool`

                  - `name: Literal["web_search"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `allowed_domains: Optional[List[str]]`

                  - `blocked_domains: Optional[List[str]]`

                  - `user_location: Optional[BetaManagedAgentsUserLocation]`

                    Approximate user location for search result localization.

                    - `type: Literal["approximate"]`

                      Location precision. Only "approximate" is supported.

                    - `city: Optional[str]`

                      City name.

                      minLength: 1, maxLength: 255

                    - `country: Optional[str]`

                      Two-letter ISO 3166-1 country code, uppercase.

                    - `region: Optional[str]`

                      Region or state name.

                      minLength: 1, maxLength: 255

                    - `timezone: Optional[str]`

                      IANA timezone identifier, e.g. "America/Los_Angeles".

                      minLength: 1, maxLength: 255

              - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

                Resolved default configuration for agent tools.

                - `enabled: bool`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

                  - `class BetaManagedAgentsAutoPolicy: …`

                    The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `class BetaManagedAgentsMCPToolset: …`

              - `type: Literal["mcp_toolset"]`

              - `configs: List[BetaManagedAgentsMCPToolConfig]`

                - `enabled: bool`

                - `name: str`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

                  - `class BetaManagedAgentsAutoPolicy: …`

                    The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `enabled: bool`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

                  - `class BetaManagedAgentsAutoPolicy: …`

                    The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `mcp_server_name: str`

            - `class BetaManagedAgentsCustomTool: …`

              A custom tool as returned in API responses.

              - `type: Literal["custom"]`

              - `description: str`

              - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                JSON Schema for custom tool input parameters.

                - `type: Literal["object"]`

                - `properties: Optional[Dict[str, object]]`

                - `required: Optional[List[str]]`

              - `name: str`

          - `version: int`

            format: int32

        - `class BetaManagedAgentsAdvisor: …`

          Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

          - `type: Literal["advisor"]`

          - `model: str`

            The advisor model id.

    - `name: str`

    - `skills: List[Skill]`

      - `class BetaManagedAgentsAnthropicSkill: …`

        A resolved Anthropic-managed skill.

      - `class BetaManagedAgentsCustomSkill: …`

        A resolved user-created custom skill.

    - `system: Optional[str]`

    - `tools: List[Tool]`

      - `class BetaManagedAgentsAgentToolset20260401: …`

      - `class BetaManagedAgentsMCPToolset: …`

      - `class BetaManagedAgentsCustomTool: …`

        A custom tool as returned in API responses.

    - `version: int`

      format: int32

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

    format: date-time

  - `budget: Optional[BetaManagedAgentsBudgetLimit]`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `type: Literal["limit"]`

    - `max_list_cost: BetaMonetaryAmount`

      A monetary amount in a specific currency.

      - `amount: str`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

  - `created_at: datetime`

    A timestamp in RFC 3339 format

    format: date-time

  - `environment_id: str`

  - `metadata: Dict[str, str]`

  - `outcome_evaluations: List[BetaManagedAgentsOutcomeEvaluationResource]`

    Per-outcome evaluation state. One entry per `define_outcome` event sent to the session.

    - `type: Literal["outcome_evaluation"]`

    - `completed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

      format: date-time

    - `description: str`

      What the agent should produce.

    - `explanation: Optional[str]`

      Grader's verdict text from the most recent evaluation. For `satisfied`, explains why criteria are met; for `needs_revision` (intermediate), what's missing; for `failed`, why unrecoverable.

    - `iteration: int`

      0-indexed revision cycle the outcome is currently on.

      format: int32

    - `outcome_id: str`

      Server-generated outc_ ID for this outcome.

    - `result: str`

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

  - `resources: List[BetaManagedAgentsSessionResource]`

    - `class BetaManagedAgentsGitHubRepositoryResource: …`

      - `type: Literal["github_repository"]`

      - `id: str`

      - `created_at: datetime`

        A timestamp in RFC 3339 format

        format: date-time

      - `mount_path: str`

      - `updated_at: datetime`

        A timestamp in RFC 3339 format

        format: date-time

      - `url: str`

      - `checkout: Optional[Checkout]`

        - `class BetaManagedAgentsBranchCheckout: …`

          - `type: Literal["branch"]`

          - `name: str`

            Branch name to check out.

            minLength: 1, maxLength: 255

        - `class BetaManagedAgentsCommitCheckout: …`

          - `type: Literal["commit"]`

          - `sha: str`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

    - `class BetaManagedAgentsFileResource: …`

      - `type: Literal["file"]`

      - `id: str`

      - `created_at: datetime`

        A timestamp in RFC 3339 format

        format: date-time

      - `file_id: str`

      - `mount_path: str`

      - `updated_at: datetime`

        A timestamp in RFC 3339 format

        format: date-time

    - `class BetaManagedAgentsMemoryStoreResource: …`

      A memory store attached to an agent session.

      - `type: Literal["memory_store"]`

      - `memory_store_id: str`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `access: Optional[Literal["read_write", "read_only"]]`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `description: Optional[str]`

        Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

      - `instructions: Optional[str]`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

        maxLength: 4096

      - `mount_path: Optional[str]`

        Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

      - `name: Optional[str]`

        Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

  - `stats: BetaManagedAgentsSessionStats`

    Timing statistics for a session.

    - `active_seconds: Optional[float]`

      Cumulative time in seconds the session spent in `running` status. Excludes idle time.

      format: double

    - `duration_seconds: Optional[float]`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

      format: double

  - `status: Literal["rescheduling", "running", "idle", "terminated"]`

    SessionStatus enum

    - `"rescheduling"`

    - `"running"`

    - `"idle"`

    - `"terminated"`

  - `title: Optional[str]`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

    format: date-time

  - `usage: BetaManagedAgentsSessionUsage`

    Cumulative token usage for a session across all turns.

    - `active_seconds: Optional[float]`

      Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once, unlike `stats.active_seconds`, which sums each thread's own active time. This is the duration the session's runtime cost is priced on.

      format: double

    - `cache_creation: Optional[BetaManagedAgentsCacheCreationUsage]`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: Optional[int]`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `ephemeral_5m_input_tokens: Optional[int]`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `cache_read_input_tokens: Optional[int]`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens: Optional[int]`

      Total input tokens consumed across all turns.

      format: int32

    - `list_cost: Optional[BetaMonetaryAmount]`

      A monetary amount in a specific currency.

    - `output_tokens: Optional[int]`

      Total output tokens generated across all turns.

      format: int32

    - `server_tool_use: Optional[BetaManagedAgentsServerToolUsage]`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `web_fetch_requests: Optional[int]`

        Number of server-executed web fetch requests.

        format: int32

      - `web_search_requests: Optional[int]`

        Number of server-executed web search requests.

        format: int32

  - `vault_ids: List[str]`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `deployment_id: Optional[str]`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
page = client.beta.sessions.list()
page = page.data[0]
print(page.id)
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

`beta.sessions.retrieve(session_id, **kwargs)  -> BetaManagedAgentsSession`

**GET** `/v1/sessions/{session_id}`

Get Session

### Parameters

- `session_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

- `workspace_id: Optional[str]`

### Returns

- `class BetaManagedAgentsSession: …`

  A Managed Agents `session`.

  - `type: Literal["session"]`

  - `id: str`

  - `agent: BetaManagedAgentsSessionAgent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `type: Literal["agent"]`

    - `id: str`

    - `description: Optional[str]`

    - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

      - `type: Literal["url"]`

      - `name: str`

      - `url: str`

    - `model: BetaManagedAgentsModelConfig`

      Model identifier and configuration.

      - `id: BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `Literal["claude-fable-5-1", "claude-sonnet-5", "claude-fable-5", 11 more]`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `claude-fable-5-1` - Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows
          - `claude-sonnet-5` - High-performance model for coding and agents
          - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
          - `claude-opus-5` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-8` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-7` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-6` - Powerful intelligence for long-running agents and coding
          - `claude-sonnet-4-6` - Best combination of speed and intelligence
          - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
          - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
          - `claude-opus-4-5` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-5-20251101` - Powerful intelligence for long-running agents and coding
          - `claude-sonnet-4-5` - High-performance model for agents and coding
          - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

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

        - `str`

      - `effort: Optional[Effort]`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

        - `class BetaManagedAgentsEffortLow: …`

          Low effort. Favors latency over reasoning depth.

          - `type: Literal["low"]`

        - `class BetaManagedAgentsEffortMedium: …`

          Medium effort. Balances latency and reasoning depth.

          - `type: Literal["medium"]`

        - `class BetaManagedAgentsEffortHigh: …`

          High effort. Favors reasoning depth.

          - `type: Literal["high"]`

        - `class BetaManagedAgentsEffortXhigh: …`

          Extra-high effort. Not all models accept this level.

          - `type: Literal["xhigh"]`

        - `class BetaManagedAgentsEffortMax: …`

          Maximum effort. Favors reasoning depth over latency.

          - `type: Literal["max"]`

      - `inference_geo: Optional[str]`

        Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

      - `speed: Optional[Literal["standard", "fast"]]`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `multiagent: Optional[BetaManagedAgentsSessionMultiagentCoordinator]`

      Resolved coordinator topology with full agent definitions for each roster member.

      - `type: Literal["coordinator"]`

      - `agents: List[Agent]`

        Full `agent` definitions the coordinator may spawn as session threads.

        - `class BetaManagedAgentsSessionThreadAgent: …`

          Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

          - `type: Literal["agent"]`

          - `id: str`

          - `description: Optional[str]`

          - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

            - `type: Literal["url"]`

            - `name: str`

            - `url: str`

          - `model: BetaManagedAgentsModelConfig`

            Model identifier and configuration.

          - `name: str`

          - `skills: List[Skill]`

            - `class BetaManagedAgentsAnthropicSkill: …`

              A resolved Anthropic-managed skill.

              - `type: Literal["anthropic"]`

              - `skill_id: str`

              - `version: str`

            - `class BetaManagedAgentsCustomSkill: …`

              A resolved user-created custom skill.

              - `type: Literal["custom"]`

              - `skill_id: str`

              - `version: str`

          - `system: Optional[str]`

          - `tools: List[Tool]`

            - `class BetaManagedAgentsAgentToolset20260401: …`

              - `type: Literal["agent_toolset_20260401"]`

              - `configs: List[BetaManagedAgentsAgentToolConfig]`

                - `class BetaManagedAgentsBashToolConfig: …`

                  Configuration for the bash tool.

                  - `type: Literal["bash"]`

                  - `enabled: bool`

                  - `name: Literal["bash"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                      - `type: Literal["always_allow"]`

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                      - `type: Literal["always_ask"]`

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                      - `type: Literal["auto"]`

                - `class BetaManagedAgentsEditToolConfig: …`

                  Configuration for the edit tool.

                  - `type: Literal["edit"]`

                  - `enabled: bool`

                  - `name: Literal["edit"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `class BetaManagedAgentsReadToolConfig: …`

                  Configuration for the read tool.

                  - `type: Literal["read"]`

                  - `enabled: bool`

                  - `name: Literal["read"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `class BetaManagedAgentsWriteToolConfig: …`

                  Configuration for the write tool.

                  - `type: Literal["write"]`

                  - `enabled: bool`

                  - `name: Literal["write"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `class BetaManagedAgentsGlobToolConfig: …`

                  Configuration for the glob tool.

                  - `type: Literal["glob"]`

                  - `enabled: bool`

                  - `name: Literal["glob"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `class BetaManagedAgentsGrepToolConfig: …`

                  Configuration for the grep tool.

                  - `type: Literal["grep"]`

                  - `enabled: bool`

                  - `name: Literal["grep"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `class BetaManagedAgentsWebFetchToolConfig: …`

                  Configuration for the web_fetch tool.

                  - `type: Literal["web_fetch"]`

                  - `enabled: bool`

                  - `name: Literal["web_fetch"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `allowed_domains: Optional[List[str]]`

                  - `blocked_domains: Optional[List[str]]`

                  - `max_content_tokens: Optional[int]`

                    format: int32

                - `class BetaManagedAgentsWebSearchToolConfig: …`

                  Configuration for the web_search tool.

                  - `type: Literal["web_search"]`

                  - `enabled: bool`

                  - `name: Literal["web_search"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `allowed_domains: Optional[List[str]]`

                  - `blocked_domains: Optional[List[str]]`

                  - `user_location: Optional[BetaManagedAgentsUserLocation]`

                    Approximate user location for search result localization.

                    - `type: Literal["approximate"]`

                      Location precision. Only "approximate" is supported.

                    - `city: Optional[str]`

                      City name.

                      minLength: 1, maxLength: 255

                    - `country: Optional[str]`

                      Two-letter ISO 3166-1 country code, uppercase.

                    - `region: Optional[str]`

                      Region or state name.

                      minLength: 1, maxLength: 255

                    - `timezone: Optional[str]`

                      IANA timezone identifier, e.g. "America/Los_Angeles".

                      minLength: 1, maxLength: 255

              - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

                Resolved default configuration for agent tools.

                - `enabled: bool`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

                  - `class BetaManagedAgentsAutoPolicy: …`

                    The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `class BetaManagedAgentsMCPToolset: …`

              - `type: Literal["mcp_toolset"]`

              - `configs: List[BetaManagedAgentsMCPToolConfig]`

                - `enabled: bool`

                - `name: str`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

                  - `class BetaManagedAgentsAutoPolicy: …`

                    The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `enabled: bool`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

                  - `class BetaManagedAgentsAutoPolicy: …`

                    The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `mcp_server_name: str`

            - `class BetaManagedAgentsCustomTool: …`

              A custom tool as returned in API responses.

              - `type: Literal["custom"]`

              - `description: str`

              - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                JSON Schema for custom tool input parameters.

                - `type: Literal["object"]`

                - `properties: Optional[Dict[str, object]]`

                - `required: Optional[List[str]]`

              - `name: str`

          - `version: int`

            format: int32

        - `class BetaManagedAgentsAdvisor: …`

          Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

          - `type: Literal["advisor"]`

          - `model: str`

            The advisor model id.

    - `name: str`

    - `skills: List[Skill]`

      - `class BetaManagedAgentsAnthropicSkill: …`

        A resolved Anthropic-managed skill.

      - `class BetaManagedAgentsCustomSkill: …`

        A resolved user-created custom skill.

    - `system: Optional[str]`

    - `tools: List[Tool]`

      - `class BetaManagedAgentsAgentToolset20260401: …`

      - `class BetaManagedAgentsMCPToolset: …`

      - `class BetaManagedAgentsCustomTool: …`

        A custom tool as returned in API responses.

    - `version: int`

      format: int32

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

    format: date-time

  - `budget: Optional[BetaManagedAgentsBudgetLimit]`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `type: Literal["limit"]`

    - `max_list_cost: BetaMonetaryAmount`

      A monetary amount in a specific currency.

      - `amount: str`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

  - `created_at: datetime`

    A timestamp in RFC 3339 format

    format: date-time

  - `environment_id: str`

  - `metadata: Dict[str, str]`

  - `outcome_evaluations: List[BetaManagedAgentsOutcomeEvaluationResource]`

    Per-outcome evaluation state. One entry per `define_outcome` event sent to the session.

    - `type: Literal["outcome_evaluation"]`

    - `completed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

      format: date-time

    - `description: str`

      What the agent should produce.

    - `explanation: Optional[str]`

      Grader's verdict text from the most recent evaluation. For `satisfied`, explains why criteria are met; for `needs_revision` (intermediate), what's missing; for `failed`, why unrecoverable.

    - `iteration: int`

      0-indexed revision cycle the outcome is currently on.

      format: int32

    - `outcome_id: str`

      Server-generated outc_ ID for this outcome.

    - `result: str`

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

  - `resources: List[BetaManagedAgentsSessionResource]`

    - `class BetaManagedAgentsGitHubRepositoryResource: …`

      - `type: Literal["github_repository"]`

      - `id: str`

      - `created_at: datetime`

        A timestamp in RFC 3339 format

        format: date-time

      - `mount_path: str`

      - `updated_at: datetime`

        A timestamp in RFC 3339 format

        format: date-time

      - `url: str`

      - `checkout: Optional[Checkout]`

        - `class BetaManagedAgentsBranchCheckout: …`

          - `type: Literal["branch"]`

          - `name: str`

            Branch name to check out.

            minLength: 1, maxLength: 255

        - `class BetaManagedAgentsCommitCheckout: …`

          - `type: Literal["commit"]`

          - `sha: str`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

    - `class BetaManagedAgentsFileResource: …`

      - `type: Literal["file"]`

      - `id: str`

      - `created_at: datetime`

        A timestamp in RFC 3339 format

        format: date-time

      - `file_id: str`

      - `mount_path: str`

      - `updated_at: datetime`

        A timestamp in RFC 3339 format

        format: date-time

    - `class BetaManagedAgentsMemoryStoreResource: …`

      A memory store attached to an agent session.

      - `type: Literal["memory_store"]`

      - `memory_store_id: str`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `access: Optional[Literal["read_write", "read_only"]]`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `description: Optional[str]`

        Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

      - `instructions: Optional[str]`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

        maxLength: 4096

      - `mount_path: Optional[str]`

        Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

      - `name: Optional[str]`

        Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

  - `stats: BetaManagedAgentsSessionStats`

    Timing statistics for a session.

    - `active_seconds: Optional[float]`

      Cumulative time in seconds the session spent in `running` status. Excludes idle time.

      format: double

    - `duration_seconds: Optional[float]`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

      format: double

  - `status: Literal["rescheduling", "running", "idle", "terminated"]`

    SessionStatus enum

    - `"rescheduling"`

    - `"running"`

    - `"idle"`

    - `"terminated"`

  - `title: Optional[str]`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

    format: date-time

  - `usage: BetaManagedAgentsSessionUsage`

    Cumulative token usage for a session across all turns.

    - `active_seconds: Optional[float]`

      Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once, unlike `stats.active_seconds`, which sums each thread's own active time. This is the duration the session's runtime cost is priced on.

      format: double

    - `cache_creation: Optional[BetaManagedAgentsCacheCreationUsage]`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: Optional[int]`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `ephemeral_5m_input_tokens: Optional[int]`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `cache_read_input_tokens: Optional[int]`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens: Optional[int]`

      Total input tokens consumed across all turns.

      format: int32

    - `list_cost: Optional[BetaMonetaryAmount]`

      A monetary amount in a specific currency.

    - `output_tokens: Optional[int]`

      Total output tokens generated across all turns.

      format: int32

    - `server_tool_use: Optional[BetaManagedAgentsServerToolUsage]`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `web_fetch_requests: Optional[int]`

        Number of server-executed web fetch requests.

        format: int32

      - `web_search_requests: Optional[int]`

        Number of server-executed web search requests.

        format: int32

  - `vault_ids: List[str]`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `deployment_id: Optional[str]`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_managed_agents_session = client.beta.sessions.retrieve(
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
)
print(beta_managed_agents_session.id)
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

`beta.sessions.update(session_id, **kwargs)  -> BetaManagedAgentsSession`

**POST** `/v1/sessions/{session_id}`

Update Session

### Parameters

- `session_id: str`

- `agent: Optional[BetaManagedAgentsSessionAgentUpdateParam]`

  Mid-session agent configuration update. Only `tools` and `mcp_servers` are updatable. Full replacement: the provided array becomes the new value. To preserve existing entries, GET the session, modify the array, and POST it back.

  - `mcp_servers: Optional[List[BetaManagedAgentsURLMCPServerParams]]`

    Replacement MCP server list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.

    - `type: Literal["url"]`

    - `name: str`

      Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

      minLength: 1, maxLength: 255

    - `url: str`

      Endpoint URL for the MCP server.

      maxLength: 2048

  - `tools: Optional[List[Tool]]`

    Replacement tool list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.

    - `class BetaManagedAgentsAgentToolset20260401Params: …`

      Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

      - `type: Literal["agent_toolset_20260401"]`

      - `configs: Optional[List[BetaManagedAgentsAgentToolConfigParams]]`

        Per-tool configuration overrides.

        - `class BetaManagedAgentsBashToolConfigParams: …`

          Configuration override for the bash tool.

          - `type: Optional[Literal["bash"]]`

          - `name: Literal["bash"]`

            Must be "bash".

          - `enabled: Optional[bool]`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy: Optional[PermissionPolicy]`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

              - `type: Literal["always_allow"]`

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

              - `type: Literal["always_ask"]`

            - `class BetaManagedAgentsAutoPolicy: …`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `type: Literal["auto"]`

        - `class BetaManagedAgentsEditToolConfigParams: …`

          Configuration override for the edit tool.

          - `type: Optional[Literal["edit"]]`

          - `name: Literal["edit"]`

            Must be "edit".

          - `enabled: Optional[bool]`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy: Optional[PermissionPolicy]`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

            - `class BetaManagedAgentsAutoPolicy: …`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

        - `class BetaManagedAgentsReadToolConfigParams: …`

          Configuration override for the read tool.

          - `type: Optional[Literal["read"]]`

          - `name: Literal["read"]`

            Must be "read".

          - `enabled: Optional[bool]`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy: Optional[PermissionPolicy]`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

            - `class BetaManagedAgentsAutoPolicy: …`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

        - `class BetaManagedAgentsWriteToolConfigParams: …`

          Configuration override for the write tool.

          - `type: Optional[Literal["write"]]`

          - `name: Literal["write"]`

            Must be "write".

          - `enabled: Optional[bool]`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy: Optional[PermissionPolicy]`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

            - `class BetaManagedAgentsAutoPolicy: …`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

        - `class BetaManagedAgentsGlobToolConfigParams: …`

          Configuration override for the glob tool.

          - `type: Optional[Literal["glob"]]`

          - `name: Literal["glob"]`

            Must be "glob".

          - `enabled: Optional[bool]`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy: Optional[PermissionPolicy]`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

            - `class BetaManagedAgentsAutoPolicy: …`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

        - `class BetaManagedAgentsGrepToolConfigParams: …`

          Configuration override for the grep tool.

          - `type: Optional[Literal["grep"]]`

          - `name: Literal["grep"]`

            Must be "grep".

          - `enabled: Optional[bool]`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy: Optional[PermissionPolicy]`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

            - `class BetaManagedAgentsAutoPolicy: …`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

        - `class BetaManagedAgentsWebFetchToolConfigParams: …`

          Configuration override for the web_fetch tool.

          - `type: Optional[Literal["web_fetch"]]`

          - `name: Literal["web_fetch"]`

            Must be "web_fetch".

          - `allowed_domains: Optional[List[str]]`

            Only fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

          - `blocked_domains: Optional[List[str]]`

            Never fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

          - `enabled: Optional[bool]`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `max_content_tokens: Optional[int]`

            Maximum number of tokens of fetched text content to include in context per call. Does not apply to binary content such as PDFs.

            format: int32

          - `permission_policy: Optional[PermissionPolicy]`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

            - `class BetaManagedAgentsAutoPolicy: …`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

        - `class BetaManagedAgentsWebSearchToolConfigParams: …`

          Configuration override for the web_search tool.

          - `type: Optional[Literal["web_search"]]`

          - `name: Literal["web_search"]`

            Must be "web_search".

          - `allowed_domains: Optional[List[str]]`

            Only return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

          - `blocked_domains: Optional[List[str]]`

            Never return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

          - `enabled: Optional[bool]`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy: Optional[PermissionPolicy]`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

            - `class BetaManagedAgentsAutoPolicy: …`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

          - `user_location: Optional[BetaManagedAgentsUserLocation]`

            Approximate user location for search result localization.

            - `type: Literal["approximate"]`

              Location precision. Only "approximate" is supported.

            - `city: Optional[str]`

              City name.

              minLength: 1, maxLength: 255

            - `country: Optional[str]`

              Two-letter ISO 3166-1 country code, uppercase.

            - `region: Optional[str]`

              Region or state name.

              minLength: 1, maxLength: 255

            - `timezone: Optional[str]`

              IANA timezone identifier, e.g. "America/Los_Angeles".

              minLength: 1, maxLength: 255

      - `default_config: Optional[BetaManagedAgentsAgentToolsetDefaultConfigParams]`

        Default configuration for all tools in a toolset.

        - `enabled: Optional[bool]`

          Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

        - `permission_policy: Optional[PermissionPolicy]`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy: …`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy: …`

            Tool calls require user confirmation before execution.

          - `class BetaManagedAgentsAutoPolicy: …`

            The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

    - `class BetaManagedAgentsMCPToolsetParams: …`

      Configuration for tools from an MCP server defined in `mcp_servers`.

      - `type: Literal["mcp_toolset"]`

      - `mcp_server_name: str`

        Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

        minLength: 1, maxLength: 255

      - `configs: Optional[List[BetaManagedAgentsMCPToolConfigParams]]`

        Per-tool configuration overrides.

        - `name: str`

          Name of the MCP tool to configure. 1-128 characters.

          minLength: 1, maxLength: 128

        - `enabled: Optional[bool]`

          Whether this tool is enabled. Overrides the `default_config` setting.

        - `permission_policy: Optional[PermissionPolicy]`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy: …`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy: …`

            Tool calls require user confirmation before execution.

          - `class BetaManagedAgentsAutoPolicy: …`

            The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

      - `default_config: Optional[BetaManagedAgentsMCPToolsetDefaultConfigParams]`

        Default configuration for all tools from an MCP server.

        - `enabled: Optional[bool]`

          Whether tools are enabled by default. Defaults to true if not specified.

        - `permission_policy: Optional[PermissionPolicy]`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy: …`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy: …`

            Tool calls require user confirmation before execution.

          - `class BetaManagedAgentsAutoPolicy: …`

            The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

    - `class BetaManagedAgentsCustomToolParams: …`

      A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

      - `type: Literal["custom"]`

      - `description: str`

        Description of what the tool does, shown to the agent to help it decide when to use the tool.

        minLength: 1

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `type: Literal["object"]`

        - `properties: Optional[Dict[str, object]]`

        - `required: Optional[List[str]]`

      - `name: str`

        Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

        minLength: 1, maxLength: 128

- `budget: Optional[BetaManagedAgentsBudgetLimitParam]`

  A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

  - `type: Literal["limit"]`

  - `max_list_cost: BetaMonetaryAmount`

    A monetary amount in a specific currency.

    - `amount: str`

      Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

    - `currency: BetaCurrency`

      Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

- `metadata: Optional[Dict[str, Optional[str]]]`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve.

- `title: Optional[str]`

  Human-readable session title.

  minLength: 1, maxLength: 500

- `vault_ids: Optional[Sequence[str]]`

  Vault IDs (`vlt_*`) to attach to the session. Not yet supported; requests setting this field are rejected. Reserved for future use.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

- `workspace_id: Optional[str]`

### Returns

- `class BetaManagedAgentsSession: …`

  A Managed Agents `session`.

  - `type: Literal["session"]`

  - `id: str`

  - `agent: BetaManagedAgentsSessionAgent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `type: Literal["agent"]`

    - `id: str`

    - `description: Optional[str]`

    - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

      - `type: Literal["url"]`

      - `name: str`

      - `url: str`

    - `model: BetaManagedAgentsModelConfig`

      Model identifier and configuration.

      - `id: BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `Literal["claude-fable-5-1", "claude-sonnet-5", "claude-fable-5", 11 more]`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `claude-fable-5-1` - Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows
          - `claude-sonnet-5` - High-performance model for coding and agents
          - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
          - `claude-opus-5` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-8` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-7` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-6` - Powerful intelligence for long-running agents and coding
          - `claude-sonnet-4-6` - Best combination of speed and intelligence
          - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
          - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
          - `claude-opus-4-5` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-5-20251101` - Powerful intelligence for long-running agents and coding
          - `claude-sonnet-4-5` - High-performance model for agents and coding
          - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

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

        - `str`

      - `effort: Optional[Effort]`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

        - `class BetaManagedAgentsEffortLow: …`

          Low effort. Favors latency over reasoning depth.

          - `type: Literal["low"]`

        - `class BetaManagedAgentsEffortMedium: …`

          Medium effort. Balances latency and reasoning depth.

          - `type: Literal["medium"]`

        - `class BetaManagedAgentsEffortHigh: …`

          High effort. Favors reasoning depth.

          - `type: Literal["high"]`

        - `class BetaManagedAgentsEffortXhigh: …`

          Extra-high effort. Not all models accept this level.

          - `type: Literal["xhigh"]`

        - `class BetaManagedAgentsEffortMax: …`

          Maximum effort. Favors reasoning depth over latency.

          - `type: Literal["max"]`

      - `inference_geo: Optional[str]`

        Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

      - `speed: Optional[Literal["standard", "fast"]]`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `multiagent: Optional[BetaManagedAgentsSessionMultiagentCoordinator]`

      Resolved coordinator topology with full agent definitions for each roster member.

      - `type: Literal["coordinator"]`

      - `agents: List[Agent]`

        Full `agent` definitions the coordinator may spawn as session threads.

        - `class BetaManagedAgentsSessionThreadAgent: …`

          Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

          - `type: Literal["agent"]`

          - `id: str`

          - `description: Optional[str]`

          - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

            - `type: Literal["url"]`

            - `name: str`

            - `url: str`

          - `model: BetaManagedAgentsModelConfig`

            Model identifier and configuration.

          - `name: str`

          - `skills: List[Skill]`

            - `class BetaManagedAgentsAnthropicSkill: …`

              A resolved Anthropic-managed skill.

              - `type: Literal["anthropic"]`

              - `skill_id: str`

              - `version: str`

            - `class BetaManagedAgentsCustomSkill: …`

              A resolved user-created custom skill.

              - `type: Literal["custom"]`

              - `skill_id: str`

              - `version: str`

          - `system: Optional[str]`

          - `tools: List[Tool]`

            - `class BetaManagedAgentsAgentToolset20260401: …`

              - `type: Literal["agent_toolset_20260401"]`

              - `configs: List[BetaManagedAgentsAgentToolConfig]`

                - `class BetaManagedAgentsBashToolConfig: …`

                  Configuration for the bash tool.

                  - `type: Literal["bash"]`

                  - `enabled: bool`

                  - `name: Literal["bash"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                      - `type: Literal["always_allow"]`

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                      - `type: Literal["always_ask"]`

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                      - `type: Literal["auto"]`

                - `class BetaManagedAgentsEditToolConfig: …`

                  Configuration for the edit tool.

                  - `type: Literal["edit"]`

                  - `enabled: bool`

                  - `name: Literal["edit"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `class BetaManagedAgentsReadToolConfig: …`

                  Configuration for the read tool.

                  - `type: Literal["read"]`

                  - `enabled: bool`

                  - `name: Literal["read"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `class BetaManagedAgentsWriteToolConfig: …`

                  Configuration for the write tool.

                  - `type: Literal["write"]`

                  - `enabled: bool`

                  - `name: Literal["write"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `class BetaManagedAgentsGlobToolConfig: …`

                  Configuration for the glob tool.

                  - `type: Literal["glob"]`

                  - `enabled: bool`

                  - `name: Literal["glob"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `class BetaManagedAgentsGrepToolConfig: …`

                  Configuration for the grep tool.

                  - `type: Literal["grep"]`

                  - `enabled: bool`

                  - `name: Literal["grep"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `class BetaManagedAgentsWebFetchToolConfig: …`

                  Configuration for the web_fetch tool.

                  - `type: Literal["web_fetch"]`

                  - `enabled: bool`

                  - `name: Literal["web_fetch"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `allowed_domains: Optional[List[str]]`

                  - `blocked_domains: Optional[List[str]]`

                  - `max_content_tokens: Optional[int]`

                    format: int32

                - `class BetaManagedAgentsWebSearchToolConfig: …`

                  Configuration for the web_search tool.

                  - `type: Literal["web_search"]`

                  - `enabled: bool`

                  - `name: Literal["web_search"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `allowed_domains: Optional[List[str]]`

                  - `blocked_domains: Optional[List[str]]`

                  - `user_location: Optional[BetaManagedAgentsUserLocation]`

                    Approximate user location for search result localization.

                    - `type: Literal["approximate"]`

                      Location precision. Only "approximate" is supported.

                    - `city: Optional[str]`

                      City name.

                      minLength: 1, maxLength: 255

                    - `country: Optional[str]`

                      Two-letter ISO 3166-1 country code, uppercase.

                    - `region: Optional[str]`

                      Region or state name.

                      minLength: 1, maxLength: 255

                    - `timezone: Optional[str]`

                      IANA timezone identifier, e.g. "America/Los_Angeles".

                      minLength: 1, maxLength: 255

              - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

                Resolved default configuration for agent tools.

                - `enabled: bool`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

                  - `class BetaManagedAgentsAutoPolicy: …`

                    The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `class BetaManagedAgentsMCPToolset: …`

              - `type: Literal["mcp_toolset"]`

              - `configs: List[BetaManagedAgentsMCPToolConfig]`

                - `enabled: bool`

                - `name: str`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

                  - `class BetaManagedAgentsAutoPolicy: …`

                    The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `enabled: bool`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

                  - `class BetaManagedAgentsAutoPolicy: …`

                    The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `mcp_server_name: str`

            - `class BetaManagedAgentsCustomTool: …`

              A custom tool as returned in API responses.

              - `type: Literal["custom"]`

              - `description: str`

              - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                JSON Schema for custom tool input parameters.

                - `type: Literal["object"]`

                - `properties: Optional[Dict[str, object]]`

                - `required: Optional[List[str]]`

              - `name: str`

          - `version: int`

            format: int32

        - `class BetaManagedAgentsAdvisor: …`

          Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

          - `type: Literal["advisor"]`

          - `model: str`

            The advisor model id.

    - `name: str`

    - `skills: List[Skill]`

      - `class BetaManagedAgentsAnthropicSkill: …`

        A resolved Anthropic-managed skill.

      - `class BetaManagedAgentsCustomSkill: …`

        A resolved user-created custom skill.

    - `system: Optional[str]`

    - `tools: List[Tool]`

      - `class BetaManagedAgentsAgentToolset20260401: …`

      - `class BetaManagedAgentsMCPToolset: …`

      - `class BetaManagedAgentsCustomTool: …`

        A custom tool as returned in API responses.

    - `version: int`

      format: int32

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

    format: date-time

  - `budget: Optional[BetaManagedAgentsBudgetLimit]`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `type: Literal["limit"]`

    - `max_list_cost: BetaMonetaryAmount`

      A monetary amount in a specific currency.

      - `amount: str`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

  - `created_at: datetime`

    A timestamp in RFC 3339 format

    format: date-time

  - `environment_id: str`

  - `metadata: Dict[str, str]`

  - `outcome_evaluations: List[BetaManagedAgentsOutcomeEvaluationResource]`

    Per-outcome evaluation state. One entry per `define_outcome` event sent to the session.

    - `type: Literal["outcome_evaluation"]`

    - `completed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

      format: date-time

    - `description: str`

      What the agent should produce.

    - `explanation: Optional[str]`

      Grader's verdict text from the most recent evaluation. For `satisfied`, explains why criteria are met; for `needs_revision` (intermediate), what's missing; for `failed`, why unrecoverable.

    - `iteration: int`

      0-indexed revision cycle the outcome is currently on.

      format: int32

    - `outcome_id: str`

      Server-generated outc_ ID for this outcome.

    - `result: str`

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

  - `resources: List[BetaManagedAgentsSessionResource]`

    - `class BetaManagedAgentsGitHubRepositoryResource: …`

      - `type: Literal["github_repository"]`

      - `id: str`

      - `created_at: datetime`

        A timestamp in RFC 3339 format

        format: date-time

      - `mount_path: str`

      - `updated_at: datetime`

        A timestamp in RFC 3339 format

        format: date-time

      - `url: str`

      - `checkout: Optional[Checkout]`

        - `class BetaManagedAgentsBranchCheckout: …`

          - `type: Literal["branch"]`

          - `name: str`

            Branch name to check out.

            minLength: 1, maxLength: 255

        - `class BetaManagedAgentsCommitCheckout: …`

          - `type: Literal["commit"]`

          - `sha: str`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

    - `class BetaManagedAgentsFileResource: …`

      - `type: Literal["file"]`

      - `id: str`

      - `created_at: datetime`

        A timestamp in RFC 3339 format

        format: date-time

      - `file_id: str`

      - `mount_path: str`

      - `updated_at: datetime`

        A timestamp in RFC 3339 format

        format: date-time

    - `class BetaManagedAgentsMemoryStoreResource: …`

      A memory store attached to an agent session.

      - `type: Literal["memory_store"]`

      - `memory_store_id: str`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `access: Optional[Literal["read_write", "read_only"]]`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `description: Optional[str]`

        Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

      - `instructions: Optional[str]`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

        maxLength: 4096

      - `mount_path: Optional[str]`

        Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

      - `name: Optional[str]`

        Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

  - `stats: BetaManagedAgentsSessionStats`

    Timing statistics for a session.

    - `active_seconds: Optional[float]`

      Cumulative time in seconds the session spent in `running` status. Excludes idle time.

      format: double

    - `duration_seconds: Optional[float]`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

      format: double

  - `status: Literal["rescheduling", "running", "idle", "terminated"]`

    SessionStatus enum

    - `"rescheduling"`

    - `"running"`

    - `"idle"`

    - `"terminated"`

  - `title: Optional[str]`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

    format: date-time

  - `usage: BetaManagedAgentsSessionUsage`

    Cumulative token usage for a session across all turns.

    - `active_seconds: Optional[float]`

      Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once, unlike `stats.active_seconds`, which sums each thread's own active time. This is the duration the session's runtime cost is priced on.

      format: double

    - `cache_creation: Optional[BetaManagedAgentsCacheCreationUsage]`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: Optional[int]`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `ephemeral_5m_input_tokens: Optional[int]`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `cache_read_input_tokens: Optional[int]`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens: Optional[int]`

      Total input tokens consumed across all turns.

      format: int32

    - `list_cost: Optional[BetaMonetaryAmount]`

      A monetary amount in a specific currency.

    - `output_tokens: Optional[int]`

      Total output tokens generated across all turns.

      format: int32

    - `server_tool_use: Optional[BetaManagedAgentsServerToolUsage]`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `web_fetch_requests: Optional[int]`

        Number of server-executed web fetch requests.

        format: int32

      - `web_search_requests: Optional[int]`

        Number of server-executed web search requests.

        format: int32

  - `vault_ids: List[str]`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `deployment_id: Optional[str]`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_managed_agents_session = client.beta.sessions.update(
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
)
print(beta_managed_agents_session.id)
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

`beta.sessions.delete(session_id, **kwargs)  -> BetaManagedAgentsDeletedSession`

**DELETE** `/v1/sessions/{session_id}`

Delete Session

### Parameters

- `session_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

- `workspace_id: Optional[str]`

### Returns

- `class BetaManagedAgentsDeletedSession: …`

  Confirmation that a `session` has been permanently deleted.

  - `type: Literal["session_deleted"]`

  - `id: str`

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_managed_agents_deleted_session = client.beta.sessions.delete(
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
)
print(beta_managed_agents_deleted_session.id)
```

#### Response (200)

```json
{
  "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "type": "session_deleted"
}
```

## Archive Session

`beta.sessions.archive(session_id, **kwargs)  -> BetaManagedAgentsSession`

**POST** `/v1/sessions/{session_id}/archive`

Archive Session

### Parameters

- `session_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

- `workspace_id: Optional[str]`

### Returns

- `class BetaManagedAgentsSession: …`

  A Managed Agents `session`.

  - `type: Literal["session"]`

  - `id: str`

  - `agent: BetaManagedAgentsSessionAgent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `type: Literal["agent"]`

    - `id: str`

    - `description: Optional[str]`

    - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

      - `type: Literal["url"]`

      - `name: str`

      - `url: str`

    - `model: BetaManagedAgentsModelConfig`

      Model identifier and configuration.

      - `id: BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `Literal["claude-fable-5-1", "claude-sonnet-5", "claude-fable-5", 11 more]`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `claude-fable-5-1` - Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows
          - `claude-sonnet-5` - High-performance model for coding and agents
          - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
          - `claude-opus-5` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-8` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-7` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-6` - Powerful intelligence for long-running agents and coding
          - `claude-sonnet-4-6` - Best combination of speed and intelligence
          - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
          - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
          - `claude-opus-4-5` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-5-20251101` - Powerful intelligence for long-running agents and coding
          - `claude-sonnet-4-5` - High-performance model for agents and coding
          - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

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

        - `str`

      - `effort: Optional[Effort]`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

        - `class BetaManagedAgentsEffortLow: …`

          Low effort. Favors latency over reasoning depth.

          - `type: Literal["low"]`

        - `class BetaManagedAgentsEffortMedium: …`

          Medium effort. Balances latency and reasoning depth.

          - `type: Literal["medium"]`

        - `class BetaManagedAgentsEffortHigh: …`

          High effort. Favors reasoning depth.

          - `type: Literal["high"]`

        - `class BetaManagedAgentsEffortXhigh: …`

          Extra-high effort. Not all models accept this level.

          - `type: Literal["xhigh"]`

        - `class BetaManagedAgentsEffortMax: …`

          Maximum effort. Favors reasoning depth over latency.

          - `type: Literal["max"]`

      - `inference_geo: Optional[str]`

        Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

      - `speed: Optional[Literal["standard", "fast"]]`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `multiagent: Optional[BetaManagedAgentsSessionMultiagentCoordinator]`

      Resolved coordinator topology with full agent definitions for each roster member.

      - `type: Literal["coordinator"]`

      - `agents: List[Agent]`

        Full `agent` definitions the coordinator may spawn as session threads.

        - `class BetaManagedAgentsSessionThreadAgent: …`

          Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

          - `type: Literal["agent"]`

          - `id: str`

          - `description: Optional[str]`

          - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

            - `type: Literal["url"]`

            - `name: str`

            - `url: str`

          - `model: BetaManagedAgentsModelConfig`

            Model identifier and configuration.

          - `name: str`

          - `skills: List[Skill]`

            - `class BetaManagedAgentsAnthropicSkill: …`

              A resolved Anthropic-managed skill.

              - `type: Literal["anthropic"]`

              - `skill_id: str`

              - `version: str`

            - `class BetaManagedAgentsCustomSkill: …`

              A resolved user-created custom skill.

              - `type: Literal["custom"]`

              - `skill_id: str`

              - `version: str`

          - `system: Optional[str]`

          - `tools: List[Tool]`

            - `class BetaManagedAgentsAgentToolset20260401: …`

              - `type: Literal["agent_toolset_20260401"]`

              - `configs: List[BetaManagedAgentsAgentToolConfig]`

                - `class BetaManagedAgentsBashToolConfig: …`

                  Configuration for the bash tool.

                  - `type: Literal["bash"]`

                  - `enabled: bool`

                  - `name: Literal["bash"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                      - `type: Literal["always_allow"]`

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                      - `type: Literal["always_ask"]`

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                      - `type: Literal["auto"]`

                - `class BetaManagedAgentsEditToolConfig: …`

                  Configuration for the edit tool.

                  - `type: Literal["edit"]`

                  - `enabled: bool`

                  - `name: Literal["edit"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `class BetaManagedAgentsReadToolConfig: …`

                  Configuration for the read tool.

                  - `type: Literal["read"]`

                  - `enabled: bool`

                  - `name: Literal["read"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `class BetaManagedAgentsWriteToolConfig: …`

                  Configuration for the write tool.

                  - `type: Literal["write"]`

                  - `enabled: bool`

                  - `name: Literal["write"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `class BetaManagedAgentsGlobToolConfig: …`

                  Configuration for the glob tool.

                  - `type: Literal["glob"]`

                  - `enabled: bool`

                  - `name: Literal["glob"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `class BetaManagedAgentsGrepToolConfig: …`

                  Configuration for the grep tool.

                  - `type: Literal["grep"]`

                  - `enabled: bool`

                  - `name: Literal["grep"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `class BetaManagedAgentsWebFetchToolConfig: …`

                  Configuration for the web_fetch tool.

                  - `type: Literal["web_fetch"]`

                  - `enabled: bool`

                  - `name: Literal["web_fetch"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `allowed_domains: Optional[List[str]]`

                  - `blocked_domains: Optional[List[str]]`

                  - `max_content_tokens: Optional[int]`

                    format: int32

                - `class BetaManagedAgentsWebSearchToolConfig: …`

                  Configuration for the web_search tool.

                  - `type: Literal["web_search"]`

                  - `enabled: bool`

                  - `name: Literal["web_search"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `allowed_domains: Optional[List[str]]`

                  - `blocked_domains: Optional[List[str]]`

                  - `user_location: Optional[BetaManagedAgentsUserLocation]`

                    Approximate user location for search result localization.

                    - `type: Literal["approximate"]`

                      Location precision. Only "approximate" is supported.

                    - `city: Optional[str]`

                      City name.

                      minLength: 1, maxLength: 255

                    - `country: Optional[str]`

                      Two-letter ISO 3166-1 country code, uppercase.

                    - `region: Optional[str]`

                      Region or state name.

                      minLength: 1, maxLength: 255

                    - `timezone: Optional[str]`

                      IANA timezone identifier, e.g. "America/Los_Angeles".

                      minLength: 1, maxLength: 255

              - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

                Resolved default configuration for agent tools.

                - `enabled: bool`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

                  - `class BetaManagedAgentsAutoPolicy: …`

                    The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `class BetaManagedAgentsMCPToolset: …`

              - `type: Literal["mcp_toolset"]`

              - `configs: List[BetaManagedAgentsMCPToolConfig]`

                - `enabled: bool`

                - `name: str`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

                  - `class BetaManagedAgentsAutoPolicy: …`

                    The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `enabled: bool`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

                  - `class BetaManagedAgentsAutoPolicy: …`

                    The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `mcp_server_name: str`

            - `class BetaManagedAgentsCustomTool: …`

              A custom tool as returned in API responses.

              - `type: Literal["custom"]`

              - `description: str`

              - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                JSON Schema for custom tool input parameters.

                - `type: Literal["object"]`

                - `properties: Optional[Dict[str, object]]`

                - `required: Optional[List[str]]`

              - `name: str`

          - `version: int`

            format: int32

        - `class BetaManagedAgentsAdvisor: …`

          Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

          - `type: Literal["advisor"]`

          - `model: str`

            The advisor model id.

    - `name: str`

    - `skills: List[Skill]`

      - `class BetaManagedAgentsAnthropicSkill: …`

        A resolved Anthropic-managed skill.

      - `class BetaManagedAgentsCustomSkill: …`

        A resolved user-created custom skill.

    - `system: Optional[str]`

    - `tools: List[Tool]`

      - `class BetaManagedAgentsAgentToolset20260401: …`

      - `class BetaManagedAgentsMCPToolset: …`

      - `class BetaManagedAgentsCustomTool: …`

        A custom tool as returned in API responses.

    - `version: int`

      format: int32

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

    format: date-time

  - `budget: Optional[BetaManagedAgentsBudgetLimit]`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `type: Literal["limit"]`

    - `max_list_cost: BetaMonetaryAmount`

      A monetary amount in a specific currency.

      - `amount: str`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

  - `created_at: datetime`

    A timestamp in RFC 3339 format

    format: date-time

  - `environment_id: str`

  - `metadata: Dict[str, str]`

  - `outcome_evaluations: List[BetaManagedAgentsOutcomeEvaluationResource]`

    Per-outcome evaluation state. One entry per `define_outcome` event sent to the session.

    - `type: Literal["outcome_evaluation"]`

    - `completed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

      format: date-time

    - `description: str`

      What the agent should produce.

    - `explanation: Optional[str]`

      Grader's verdict text from the most recent evaluation. For `satisfied`, explains why criteria are met; for `needs_revision` (intermediate), what's missing; for `failed`, why unrecoverable.

    - `iteration: int`

      0-indexed revision cycle the outcome is currently on.

      format: int32

    - `outcome_id: str`

      Server-generated outc_ ID for this outcome.

    - `result: str`

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

  - `resources: List[BetaManagedAgentsSessionResource]`

    - `class BetaManagedAgentsGitHubRepositoryResource: …`

      - `type: Literal["github_repository"]`

      - `id: str`

      - `created_at: datetime`

        A timestamp in RFC 3339 format

        format: date-time

      - `mount_path: str`

      - `updated_at: datetime`

        A timestamp in RFC 3339 format

        format: date-time

      - `url: str`

      - `checkout: Optional[Checkout]`

        - `class BetaManagedAgentsBranchCheckout: …`

          - `type: Literal["branch"]`

          - `name: str`

            Branch name to check out.

            minLength: 1, maxLength: 255

        - `class BetaManagedAgentsCommitCheckout: …`

          - `type: Literal["commit"]`

          - `sha: str`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

    - `class BetaManagedAgentsFileResource: …`

      - `type: Literal["file"]`

      - `id: str`

      - `created_at: datetime`

        A timestamp in RFC 3339 format

        format: date-time

      - `file_id: str`

      - `mount_path: str`

      - `updated_at: datetime`

        A timestamp in RFC 3339 format

        format: date-time

    - `class BetaManagedAgentsMemoryStoreResource: …`

      A memory store attached to an agent session.

      - `type: Literal["memory_store"]`

      - `memory_store_id: str`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `access: Optional[Literal["read_write", "read_only"]]`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `description: Optional[str]`

        Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

      - `instructions: Optional[str]`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

        maxLength: 4096

      - `mount_path: Optional[str]`

        Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

      - `name: Optional[str]`

        Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

  - `stats: BetaManagedAgentsSessionStats`

    Timing statistics for a session.

    - `active_seconds: Optional[float]`

      Cumulative time in seconds the session spent in `running` status. Excludes idle time.

      format: double

    - `duration_seconds: Optional[float]`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

      format: double

  - `status: Literal["rescheduling", "running", "idle", "terminated"]`

    SessionStatus enum

    - `"rescheduling"`

    - `"running"`

    - `"idle"`

    - `"terminated"`

  - `title: Optional[str]`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

    format: date-time

  - `usage: BetaManagedAgentsSessionUsage`

    Cumulative token usage for a session across all turns.

    - `active_seconds: Optional[float]`

      Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once, unlike `stats.active_seconds`, which sums each thread's own active time. This is the duration the session's runtime cost is priced on.

      format: double

    - `cache_creation: Optional[BetaManagedAgentsCacheCreationUsage]`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: Optional[int]`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `ephemeral_5m_input_tokens: Optional[int]`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `cache_read_input_tokens: Optional[int]`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens: Optional[int]`

      Total input tokens consumed across all turns.

      format: int32

    - `list_cost: Optional[BetaMonetaryAmount]`

      A monetary amount in a specific currency.

    - `output_tokens: Optional[int]`

      Total output tokens generated across all turns.

      format: int32

    - `server_tool_use: Optional[BetaManagedAgentsServerToolUsage]`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `web_fetch_requests: Optional[int]`

        Number of server-executed web fetch requests.

        format: int32

      - `web_search_requests: Optional[int]`

        Number of server-executed web search requests.

        format: int32

  - `vault_ids: List[str]`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `deployment_id: Optional[str]`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_managed_agents_session = client.beta.sessions.archive(
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
)
print(beta_managed_agents_session.id)
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

- `class BetaManagedAgentsAdvisorParams: …`

  Platform advisor roster entry: a model the session's primary thread may consult mid-turn. At most one per roster; the entry occupies the roster name `anthropic.advisor`.

  - `type: Literal["advisor"]`

  - `model: str`

    A Claude model id. The model must be permitted as an advisor for this agent's model — see the sessions/threads/advisor spec.

    minLength: 1, maxLength: 256

### Beta Managed Agents Agent Message Preview

- `class BetaManagedAgentsAgentMessagePreview: …`

  - `type: Literal["agent.message"]`

  - `id: str`

    The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

### Beta Managed Agents Agent Params

- `class BetaManagedAgentsAgentParams: …`

  Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

  - `type: Literal["agent"]`

  - `id: str`

    The `agent` ID.

    minLength: 1, maxLength: 128

  - `version: Optional[int]`

    The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

    format: int32

### Beta Managed Agents Agent Thinking Preview

- `class BetaManagedAgentsAgentThinkingPreview: …`

  - `type: Literal["agent.thinking"]`

  - `id: str`

    The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

### Beta Managed Agents Agent With Overrides Params

- `class BetaManagedAgentsAgentWithOverridesParams: …`

  Reference to an `agent` plus optional configuration overrides. Each provided field replaces the agent's value for the caller's use; the agent resource is unchanged.

  - `type: Literal["agent_with_overrides"]`

  - `id: str`

    The `agent` ID.

    minLength: 1, maxLength: 128

  - `mcp_servers: Optional[List[BetaManagedAgentsURLMCPServerParams]]`

    Replacement MCP server list. Full replacement: the provided array becomes the MCP servers. Send an empty array to clear; omit to preserve the agent's servers.

    - `type: Literal["url"]`

    - `name: str`

      Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

      minLength: 1, maxLength: 255

    - `url: str`

      Endpoint URL for the MCP server.

      maxLength: 2048

  - `model: Optional[Model]`

    Replacement model. Accepts the model string, e.g. `claude-opus-5`, or a `model_config` object. Omit to use the agent's model.

    - `Union[Literal["claude-fable-5-1", "claude-sonnet-5", "claude-fable-5", 11 more], str]`

      - `Literal["claude-fable-5-1", "claude-sonnet-5", "claude-fable-5", 11 more]`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `claude-fable-5-1` - Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows
        - `claude-sonnet-5` - High-performance model for coding and agents
        - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
        - `claude-opus-5` - Powerful intelligence for long-running agents and coding
        - `claude-opus-4-8` - Powerful intelligence for long-running agents and coding
        - `claude-opus-4-7` - Powerful intelligence for long-running agents and coding
        - `claude-opus-4-6` - Powerful intelligence for long-running agents and coding
        - `claude-sonnet-4-6` - Best combination of speed and intelligence
        - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
        - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
        - `claude-opus-4-5` - Powerful intelligence for long-running agents and coding
        - `claude-opus-4-5-20251101` - Powerful intelligence for long-running agents and coding
        - `claude-sonnet-4-5` - High-performance model for agents and coding
        - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

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

      - `str`

    - `class BetaManagedAgentsModelConfigParams: …`

      An object that defines additional configuration control over model use

      - `id: BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `Literal["claude-fable-5-1", "claude-sonnet-5", "claude-fable-5", 11 more]`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `claude-fable-5-1` - Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows
          - `claude-sonnet-5` - High-performance model for coding and agents
          - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
          - `claude-opus-5` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-8` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-7` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-6` - Powerful intelligence for long-running agents and coding
          - `claude-sonnet-4-6` - Best combination of speed and intelligence
          - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
          - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
          - `claude-opus-4-5` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-5-20251101` - Powerful intelligence for long-running agents and coding
          - `claude-sonnet-4-5` - High-performance model for agents and coding
          - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

        - `str`

      - `effort: Optional[Effort]`

        How hard Claude works on each inference call. Accepts a bare level string (`"high"`) or `{"type": "high"}`. On create, omitting it resolves the per-model default; on update, omitting it leaves the stored value unchanged.

        - `Literal["low", "medium", "high", 2 more]`

          How hard Claude works on each turn. Higher levels favor reasoning depth over latency. Not all models accept every level; invalid combinations are rejected at create time.

          - `"low"`

          - `"medium"`

          - `"high"`

          - `"xhigh"`

          - `"max"`

        - `class BetaManagedAgentsEffortLow: …`

          Low effort. Favors latency over reasoning depth.

          - `type: Literal["low"]`

        - `class BetaManagedAgentsEffortMedium: …`

          Medium effort. Balances latency and reasoning depth.

          - `type: Literal["medium"]`

        - `class BetaManagedAgentsEffortHigh: …`

          High effort. Favors reasoning depth.

          - `type: Literal["high"]`

        - `class BetaManagedAgentsEffortXhigh: …`

          Extra-high effort. Not all models accept this level.

          - `type: Literal["xhigh"]`

        - `class BetaManagedAgentsEffortMax: …`

          Maximum effort. Favors reasoning depth over latency.

          - `type: Literal["max"]`

      - `inference_geo: Optional[str]`

        Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo. On update, `model` is whole-object replacement — omitting inference_geo clears it.

      - `speed: Optional[Literal["standard", "fast"]]`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `skills: Optional[List[BetaManagedAgentsSkillParams]]`

    Replacement skill list. Full replacement: the provided array becomes the skills. Send an empty array to clear; omit to preserve the agent's skills.

    - `class BetaManagedAgentsAnthropicSkillParams: …`

      An Anthropic-managed skill.

      - `type: Literal["anthropic"]`

      - `skill_id: str`

        Identifier of the Anthropic skill (e.g., "xlsx").

        minLength: 1, maxLength: 64

      - `version: Optional[str]`

        Version to pin. Defaults to latest if omitted.

        minLength: 1, maxLength: 64

    - `class BetaManagedAgentsCustomSkillParams: …`

      A user-created custom skill.

      - `type: Literal["custom"]`

      - `skill_id: str`

        Tagged ID of the custom skill (e.g., "skill_01XJ5...").

        minLength: 1, maxLength: 64

      - `version: Optional[str]`

        Version to pin. Defaults to latest if omitted.

        minLength: 1, maxLength: 64

  - `system: Optional[str]`

    Replacement system prompt. Up to 100,000 characters. Set to null to clear the agent's system prompt; omit to preserve it.

    maxLength: 100000

  - `tools: Optional[List[Tool]]`

    Replacement tool list. Full replacement: the provided array becomes the tool configuration. Send an empty array to clear; omit to preserve the agent's tools.

    - `class BetaManagedAgentsAgentToolset20260401Params: …`

      Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

      - `type: Literal["agent_toolset_20260401"]`

      - `configs: Optional[List[BetaManagedAgentsAgentToolConfigParams]]`

        Per-tool configuration overrides.

        - `class BetaManagedAgentsBashToolConfigParams: …`

          Configuration override for the bash tool.

          - `type: Optional[Literal["bash"]]`

          - `name: Literal["bash"]`

            Must be "bash".

          - `enabled: Optional[bool]`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy: Optional[PermissionPolicy]`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

              - `type: Literal["always_allow"]`

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

              - `type: Literal["always_ask"]`

            - `class BetaManagedAgentsAutoPolicy: …`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `type: Literal["auto"]`

        - `class BetaManagedAgentsEditToolConfigParams: …`

          Configuration override for the edit tool.

          - `type: Optional[Literal["edit"]]`

          - `name: Literal["edit"]`

            Must be "edit".

          - `enabled: Optional[bool]`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy: Optional[PermissionPolicy]`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

            - `class BetaManagedAgentsAutoPolicy: …`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

        - `class BetaManagedAgentsReadToolConfigParams: …`

          Configuration override for the read tool.

          - `type: Optional[Literal["read"]]`

          - `name: Literal["read"]`

            Must be "read".

          - `enabled: Optional[bool]`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy: Optional[PermissionPolicy]`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

            - `class BetaManagedAgentsAutoPolicy: …`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

        - `class BetaManagedAgentsWriteToolConfigParams: …`

          Configuration override for the write tool.

          - `type: Optional[Literal["write"]]`

          - `name: Literal["write"]`

            Must be "write".

          - `enabled: Optional[bool]`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy: Optional[PermissionPolicy]`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

            - `class BetaManagedAgentsAutoPolicy: …`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

        - `class BetaManagedAgentsGlobToolConfigParams: …`

          Configuration override for the glob tool.

          - `type: Optional[Literal["glob"]]`

          - `name: Literal["glob"]`

            Must be "glob".

          - `enabled: Optional[bool]`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy: Optional[PermissionPolicy]`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

            - `class BetaManagedAgentsAutoPolicy: …`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

        - `class BetaManagedAgentsGrepToolConfigParams: …`

          Configuration override for the grep tool.

          - `type: Optional[Literal["grep"]]`

          - `name: Literal["grep"]`

            Must be "grep".

          - `enabled: Optional[bool]`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy: Optional[PermissionPolicy]`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

            - `class BetaManagedAgentsAutoPolicy: …`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

        - `class BetaManagedAgentsWebFetchToolConfigParams: …`

          Configuration override for the web_fetch tool.

          - `type: Optional[Literal["web_fetch"]]`

          - `name: Literal["web_fetch"]`

            Must be "web_fetch".

          - `allowed_domains: Optional[List[str]]`

            Only fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

          - `blocked_domains: Optional[List[str]]`

            Never fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

          - `enabled: Optional[bool]`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `max_content_tokens: Optional[int]`

            Maximum number of tokens of fetched text content to include in context per call. Does not apply to binary content such as PDFs.

            format: int32

          - `permission_policy: Optional[PermissionPolicy]`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

            - `class BetaManagedAgentsAutoPolicy: …`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

        - `class BetaManagedAgentsWebSearchToolConfigParams: …`

          Configuration override for the web_search tool.

          - `type: Optional[Literal["web_search"]]`

          - `name: Literal["web_search"]`

            Must be "web_search".

          - `allowed_domains: Optional[List[str]]`

            Only return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

          - `blocked_domains: Optional[List[str]]`

            Never return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

          - `enabled: Optional[bool]`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy: Optional[PermissionPolicy]`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

            - `class BetaManagedAgentsAutoPolicy: …`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

          - `user_location: Optional[BetaManagedAgentsUserLocation]`

            Approximate user location for search result localization.

            - `type: Literal["approximate"]`

              Location precision. Only "approximate" is supported.

            - `city: Optional[str]`

              City name.

              minLength: 1, maxLength: 255

            - `country: Optional[str]`

              Two-letter ISO 3166-1 country code, uppercase.

            - `region: Optional[str]`

              Region or state name.

              minLength: 1, maxLength: 255

            - `timezone: Optional[str]`

              IANA timezone identifier, e.g. "America/Los_Angeles".

              minLength: 1, maxLength: 255

      - `default_config: Optional[BetaManagedAgentsAgentToolsetDefaultConfigParams]`

        Default configuration for all tools in a toolset.

        - `enabled: Optional[bool]`

          Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

        - `permission_policy: Optional[PermissionPolicy]`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy: …`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy: …`

            Tool calls require user confirmation before execution.

          - `class BetaManagedAgentsAutoPolicy: …`

            The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

    - `class BetaManagedAgentsMCPToolsetParams: …`

      Configuration for tools from an MCP server defined in `mcp_servers`.

      - `type: Literal["mcp_toolset"]`

      - `mcp_server_name: str`

        Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

        minLength: 1, maxLength: 255

      - `configs: Optional[List[BetaManagedAgentsMCPToolConfigParams]]`

        Per-tool configuration overrides.

        - `name: str`

          Name of the MCP tool to configure. 1-128 characters.

          minLength: 1, maxLength: 128

        - `enabled: Optional[bool]`

          Whether this tool is enabled. Overrides the `default_config` setting.

        - `permission_policy: Optional[PermissionPolicy]`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy: …`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy: …`

            Tool calls require user confirmation before execution.

          - `class BetaManagedAgentsAutoPolicy: …`

            The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

      - `default_config: Optional[BetaManagedAgentsMCPToolsetDefaultConfigParams]`

        Default configuration for all tools from an MCP server.

        - `enabled: Optional[bool]`

          Whether tools are enabled by default. Defaults to true if not specified.

        - `permission_policy: Optional[PermissionPolicy]`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy: …`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy: …`

            Tool calls require user confirmation before execution.

          - `class BetaManagedAgentsAutoPolicy: …`

            The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

    - `class BetaManagedAgentsCustomToolParams: …`

      A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

      - `type: Literal["custom"]`

      - `description: str`

        Description of what the tool does, shown to the agent to help it decide when to use the tool.

        minLength: 1

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `type: Literal["object"]`

        - `properties: Optional[Dict[str, object]]`

        - `required: Optional[List[str]]`

      - `name: str`

        Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

        minLength: 1, maxLength: 128

  - `version: Optional[int]`

    The specific `agent` version to use. Omit to use the latest version.

    format: int32

### Beta Managed Agents Branch Checkout

- `class BetaManagedAgentsBranchCheckout: …`

  - `type: Literal["branch"]`

  - `name: str`

    Branch name to check out.

    minLength: 1, maxLength: 255

### Beta Managed Agents Budget Limit

- `class BetaManagedAgentsBudgetLimit: …`

  A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

  - `type: Literal["limit"]`

  - `max_list_cost: BetaMonetaryAmount`

    A monetary amount in a specific currency.

    - `amount: str`

      Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

    - `currency: BetaCurrency`

      Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

### Beta Managed Agents Cache Creation Usage

- `class BetaManagedAgentsCacheCreationUsage: …`

  Prompt-cache creation token usage broken down by cache lifetime.

  - `ephemeral_1h_input_tokens: Optional[int]`

    Tokens used to create 1-hour ephemeral cache entries.

    format: int32

  - `ephemeral_5m_input_tokens: Optional[int]`

    Tokens used to create 5-minute ephemeral cache entries.

    format: int32

### Beta Managed Agents Commit Checkout

- `class BetaManagedAgentsCommitCheckout: …`

  - `type: Literal["commit"]`

  - `sha: str`

    Full commit SHA to check out.

    minLength: 7, maxLength: 64

### Beta Managed Agents Deleted Session

- `class BetaManagedAgentsDeletedSession: …`

  Confirmation that a `session` has been permanently deleted.

  - `type: Literal["session_deleted"]`

  - `id: str`

### Beta Managed Agents Delta Content

- `class BetaManagedAgentsDeltaContent: …`

  - `type: Literal["content_delta"]`

  - `content: BetaManagedAgentsTextBlock`

    Regular text content.

    - `type: Literal["text"]`

    - `text: str`

      The text content.

      minLength: 1

  - `index: Optional[int]`

    Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

    format: uint32

### Beta Managed Agents Delta Event

- `class BetaManagedAgentsDeltaEvent: …`

  An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

  - `type: Literal["event_delta"]`

  - `delta: BetaManagedAgentsDeltaContent`

    One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

    - `type: Literal["content_delta"]`

    - `content: BetaManagedAgentsTextBlock`

      Regular text content.

      - `type: Literal["text"]`

      - `text: str`

        The text content.

        minLength: 1

    - `index: Optional[int]`

      Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

      format: uint32

  - `event_id: str`

    The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

### Beta Managed Agents Delta Type

- `Literal["agent.message", "agent.thinking"]`

  EventDeltaType enum

  - `"agent.message"`

  - `"agent.thinking"`

### Beta Managed Agents File Resource Params

- `class BetaManagedAgentsFileResourceParams: …`

  Mount a file uploaded via the Files API into the session.

  - `type: Literal["file"]`

  - `file_id: str`

    ID of a previously uploaded file.

    minLength: 1, maxLength: 128

  - `mount_path: Optional[str]`

    Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    minLength: 1, maxLength: 4096

### Beta Managed Agents GitHub Repository Resource Params

- `class BetaManagedAgentsGitHubRepositoryResourceParams: …`

  Mount a GitHub repository into the session's container.

  - `type: Literal["github_repository"]`

  - `url: str`

    Github URL of the repository

    minLength: 1, maxLength: 2048

  - `authorization_token: Optional[str]`

    GitHub authorization token used to clone the repository. Required for private repositories; optional for public ones.

    minLength: 1, maxLength: 4096

  - `checkout: Optional[Checkout]`

    Branch or commit to check out. Defaults to the repository's default branch.

    - `class BetaManagedAgentsBranchCheckout: …`

      - `type: Literal["branch"]`

      - `name: str`

        Branch name to check out.

        minLength: 1, maxLength: 255

    - `class BetaManagedAgentsCommitCheckout: …`

      - `type: Literal["commit"]`

      - `sha: str`

        Full commit SHA to check out.

        minLength: 7, maxLength: 64

  - `mount_path: Optional[str]`

    Mount path in the container. Defaults to `/workspace/<repo-name>`.

    minLength: 1, maxLength: 4096

### Beta Managed Agents Memory Store Resource Param

- `class BetaManagedAgentsMemoryStoreResourceParam: …`

  Parameters for attaching a memory store to an agent session.

  - `type: Literal["memory_store"]`

  - `memory_store_id: str`

    The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

  - `access: Optional[Literal["read_write", "read_only"]]`

    Access mode for an attached memory store.

    - `"read_write"`

    - `"read_only"`

  - `instructions: Optional[str]`

    Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

    maxLength: 4096

### Beta Managed Agents Multiagent

- `class BetaManagedAgentsMultiagent: …`

  Resolved coordinator topology with a concrete agent roster.

  - `type: Literal["coordinator"]`

  - `agents: List[Agent]`

    Agents the coordinator may spawn as session threads, each resolved to a specific version.

    - `class BetaManagedAgentsAgentReference: …`

      A resolved agent reference with a concrete version.

      - `type: Literal["agent"]`

      - `id: str`

      - `version: int`

        format: int32

    - `class BetaManagedAgentsAdvisor: …`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `type: Literal["advisor"]`

      - `model: str`

        The advisor model id.

### Beta Managed Agents Multiagent Params

- `class BetaManagedAgentsMultiagentParams: …`

  A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.

  - `type: Literal["coordinator"]`

  - `agents: Sequence[BetaManagedAgentsMultiagentRosterEntryParams]`

    Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).

    - `str`

    - `class BetaManagedAgentsAgentParams: …`

      Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

      - `type: Literal["agent"]`

      - `id: str`

        The `agent` ID.

        minLength: 1, maxLength: 128

      - `version: Optional[int]`

        The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

        format: int32

    - `class BetaManagedAgentsMultiagentSelfParams: …`

      Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

      - `type: Literal["self"]`

    - `class BetaManagedAgentsAdvisorParams: …`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn. At most one per roster; the entry occupies the roster name `anthropic.advisor`.

      - `type: Literal["advisor"]`

      - `model: str`

        A Claude model id. The model must be permitted as an advisor for this agent's model — see the sessions/threads/advisor spec.

        minLength: 1, maxLength: 256

### Beta Managed Agents Multiagent Roster Entry Params

- `BetaManagedAgentsMultiagentRosterEntryParams`

  An entry in a multiagent roster: an agent ID string, a versioned agent reference, or `self`.

  - `str`

  - `class BetaManagedAgentsAgentParams: …`

    Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

    - `type: Literal["agent"]`

    - `id: str`

      The `agent` ID.

      minLength: 1, maxLength: 128

    - `version: Optional[int]`

      The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

      format: int32

  - `class BetaManagedAgentsMultiagentSelfParams: …`

    Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

    - `type: Literal["self"]`

  - `class BetaManagedAgentsAdvisorParams: …`

    Platform advisor roster entry: a model the session's primary thread may consult mid-turn. At most one per roster; the entry occupies the roster name `anthropic.advisor`.

    - `type: Literal["advisor"]`

    - `model: str`

      A Claude model id. The model must be permitted as an advisor for this agent's model — see the sessions/threads/advisor spec.

      minLength: 1, maxLength: 256

### Beta Managed Agents Outcome Evaluation Resource

- `class BetaManagedAgentsOutcomeEvaluationResource: …`

  Evaluation state for a single outcome defined via a `define_outcome` event.

  - `type: Literal["outcome_evaluation"]`

  - `completed_at: Optional[datetime]`

    A timestamp in RFC 3339 format

    format: date-time

  - `description: str`

    What the agent should produce.

  - `explanation: Optional[str]`

    Grader's verdict text from the most recent evaluation. For `satisfied`, explains why criteria are met; for `needs_revision` (intermediate), what's missing; for `failed`, why unrecoverable.

  - `iteration: int`

    0-indexed revision cycle the outcome is currently on.

    format: int32

  - `outcome_id: str`

    Server-generated outc_ ID for this outcome.

  - `result: str`

    Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

### Beta Managed Agents Server Tool Usage

- `class BetaManagedAgentsServerToolUsage: …`

  Cumulative count of server-executed tool invocations, broken down by tool.

  - `web_fetch_requests: Optional[int]`

    Number of server-executed web fetch requests.

    format: int32

  - `web_search_requests: Optional[int]`

    Number of server-executed web search requests.

    format: int32

### Beta Managed Agents Session

- `class BetaManagedAgentsSession: …`

  A Managed Agents `session`.

  - `type: Literal["session"]`

  - `id: str`

  - `agent: BetaManagedAgentsSessionAgent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `type: Literal["agent"]`

    - `id: str`

    - `description: Optional[str]`

    - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

      - `type: Literal["url"]`

      - `name: str`

      - `url: str`

    - `model: BetaManagedAgentsModelConfig`

      Model identifier and configuration.

      - `id: BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `Literal["claude-fable-5-1", "claude-sonnet-5", "claude-fable-5", 11 more]`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `claude-fable-5-1` - Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows
          - `claude-sonnet-5` - High-performance model for coding and agents
          - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
          - `claude-opus-5` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-8` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-7` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-6` - Powerful intelligence for long-running agents and coding
          - `claude-sonnet-4-6` - Best combination of speed and intelligence
          - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
          - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
          - `claude-opus-4-5` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-5-20251101` - Powerful intelligence for long-running agents and coding
          - `claude-sonnet-4-5` - High-performance model for agents and coding
          - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

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

        - `str`

      - `effort: Optional[Effort]`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

        - `class BetaManagedAgentsEffortLow: …`

          Low effort. Favors latency over reasoning depth.

          - `type: Literal["low"]`

        - `class BetaManagedAgentsEffortMedium: …`

          Medium effort. Balances latency and reasoning depth.

          - `type: Literal["medium"]`

        - `class BetaManagedAgentsEffortHigh: …`

          High effort. Favors reasoning depth.

          - `type: Literal["high"]`

        - `class BetaManagedAgentsEffortXhigh: …`

          Extra-high effort. Not all models accept this level.

          - `type: Literal["xhigh"]`

        - `class BetaManagedAgentsEffortMax: …`

          Maximum effort. Favors reasoning depth over latency.

          - `type: Literal["max"]`

      - `inference_geo: Optional[str]`

        Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

      - `speed: Optional[Literal["standard", "fast"]]`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `multiagent: Optional[BetaManagedAgentsSessionMultiagentCoordinator]`

      Resolved coordinator topology with full agent definitions for each roster member.

      - `type: Literal["coordinator"]`

      - `agents: List[Agent]`

        Full `agent` definitions the coordinator may spawn as session threads.

        - `class BetaManagedAgentsSessionThreadAgent: …`

          Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

          - `type: Literal["agent"]`

          - `id: str`

          - `description: Optional[str]`

          - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

            - `type: Literal["url"]`

            - `name: str`

            - `url: str`

          - `model: BetaManagedAgentsModelConfig`

            Model identifier and configuration.

          - `name: str`

          - `skills: List[Skill]`

            - `class BetaManagedAgentsAnthropicSkill: …`

              A resolved Anthropic-managed skill.

              - `type: Literal["anthropic"]`

              - `skill_id: str`

              - `version: str`

            - `class BetaManagedAgentsCustomSkill: …`

              A resolved user-created custom skill.

              - `type: Literal["custom"]`

              - `skill_id: str`

              - `version: str`

          - `system: Optional[str]`

          - `tools: List[Tool]`

            - `class BetaManagedAgentsAgentToolset20260401: …`

              - `type: Literal["agent_toolset_20260401"]`

              - `configs: List[BetaManagedAgentsAgentToolConfig]`

                - `class BetaManagedAgentsBashToolConfig: …`

                  Configuration for the bash tool.

                  - `type: Literal["bash"]`

                  - `enabled: bool`

                  - `name: Literal["bash"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                      - `type: Literal["always_allow"]`

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                      - `type: Literal["always_ask"]`

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                      - `type: Literal["auto"]`

                - `class BetaManagedAgentsEditToolConfig: …`

                  Configuration for the edit tool.

                  - `type: Literal["edit"]`

                  - `enabled: bool`

                  - `name: Literal["edit"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `class BetaManagedAgentsReadToolConfig: …`

                  Configuration for the read tool.

                  - `type: Literal["read"]`

                  - `enabled: bool`

                  - `name: Literal["read"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `class BetaManagedAgentsWriteToolConfig: …`

                  Configuration for the write tool.

                  - `type: Literal["write"]`

                  - `enabled: bool`

                  - `name: Literal["write"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `class BetaManagedAgentsGlobToolConfig: …`

                  Configuration for the glob tool.

                  - `type: Literal["glob"]`

                  - `enabled: bool`

                  - `name: Literal["glob"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `class BetaManagedAgentsGrepToolConfig: …`

                  Configuration for the grep tool.

                  - `type: Literal["grep"]`

                  - `enabled: bool`

                  - `name: Literal["grep"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `class BetaManagedAgentsWebFetchToolConfig: …`

                  Configuration for the web_fetch tool.

                  - `type: Literal["web_fetch"]`

                  - `enabled: bool`

                  - `name: Literal["web_fetch"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `allowed_domains: Optional[List[str]]`

                  - `blocked_domains: Optional[List[str]]`

                  - `max_content_tokens: Optional[int]`

                    format: int32

                - `class BetaManagedAgentsWebSearchToolConfig: …`

                  Configuration for the web_search tool.

                  - `type: Literal["web_search"]`

                  - `enabled: bool`

                  - `name: Literal["web_search"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `allowed_domains: Optional[List[str]]`

                  - `blocked_domains: Optional[List[str]]`

                  - `user_location: Optional[BetaManagedAgentsUserLocation]`

                    Approximate user location for search result localization.

                    - `type: Literal["approximate"]`

                      Location precision. Only "approximate" is supported.

                    - `city: Optional[str]`

                      City name.

                      minLength: 1, maxLength: 255

                    - `country: Optional[str]`

                      Two-letter ISO 3166-1 country code, uppercase.

                    - `region: Optional[str]`

                      Region or state name.

                      minLength: 1, maxLength: 255

                    - `timezone: Optional[str]`

                      IANA timezone identifier, e.g. "America/Los_Angeles".

                      minLength: 1, maxLength: 255

              - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

                Resolved default configuration for agent tools.

                - `enabled: bool`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

                  - `class BetaManagedAgentsAutoPolicy: …`

                    The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `class BetaManagedAgentsMCPToolset: …`

              - `type: Literal["mcp_toolset"]`

              - `configs: List[BetaManagedAgentsMCPToolConfig]`

                - `enabled: bool`

                - `name: str`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

                  - `class BetaManagedAgentsAutoPolicy: …`

                    The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `enabled: bool`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

                  - `class BetaManagedAgentsAutoPolicy: …`

                    The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `mcp_server_name: str`

            - `class BetaManagedAgentsCustomTool: …`

              A custom tool as returned in API responses.

              - `type: Literal["custom"]`

              - `description: str`

              - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                JSON Schema for custom tool input parameters.

                - `type: Literal["object"]`

                - `properties: Optional[Dict[str, object]]`

                - `required: Optional[List[str]]`

              - `name: str`

          - `version: int`

            format: int32

        - `class BetaManagedAgentsAdvisor: …`

          Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

          - `type: Literal["advisor"]`

          - `model: str`

            The advisor model id.

    - `name: str`

    - `skills: List[Skill]`

      - `class BetaManagedAgentsAnthropicSkill: …`

        A resolved Anthropic-managed skill.

      - `class BetaManagedAgentsCustomSkill: …`

        A resolved user-created custom skill.

    - `system: Optional[str]`

    - `tools: List[Tool]`

      - `class BetaManagedAgentsAgentToolset20260401: …`

      - `class BetaManagedAgentsMCPToolset: …`

      - `class BetaManagedAgentsCustomTool: …`

        A custom tool as returned in API responses.

    - `version: int`

      format: int32

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

    format: date-time

  - `budget: Optional[BetaManagedAgentsBudgetLimit]`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `type: Literal["limit"]`

    - `max_list_cost: BetaMonetaryAmount`

      A monetary amount in a specific currency.

      - `amount: str`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

  - `created_at: datetime`

    A timestamp in RFC 3339 format

    format: date-time

  - `environment_id: str`

  - `metadata: Dict[str, str]`

  - `outcome_evaluations: List[BetaManagedAgentsOutcomeEvaluationResource]`

    Per-outcome evaluation state. One entry per `define_outcome` event sent to the session.

    - `type: Literal["outcome_evaluation"]`

    - `completed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

      format: date-time

    - `description: str`

      What the agent should produce.

    - `explanation: Optional[str]`

      Grader's verdict text from the most recent evaluation. For `satisfied`, explains why criteria are met; for `needs_revision` (intermediate), what's missing; for `failed`, why unrecoverable.

    - `iteration: int`

      0-indexed revision cycle the outcome is currently on.

      format: int32

    - `outcome_id: str`

      Server-generated outc_ ID for this outcome.

    - `result: str`

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

  - `resources: List[BetaManagedAgentsSessionResource]`

    - `class BetaManagedAgentsGitHubRepositoryResource: …`

      - `type: Literal["github_repository"]`

      - `id: str`

      - `created_at: datetime`

        A timestamp in RFC 3339 format

        format: date-time

      - `mount_path: str`

      - `updated_at: datetime`

        A timestamp in RFC 3339 format

        format: date-time

      - `url: str`

      - `checkout: Optional[Checkout]`

        - `class BetaManagedAgentsBranchCheckout: …`

          - `type: Literal["branch"]`

          - `name: str`

            Branch name to check out.

            minLength: 1, maxLength: 255

        - `class BetaManagedAgentsCommitCheckout: …`

          - `type: Literal["commit"]`

          - `sha: str`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

    - `class BetaManagedAgentsFileResource: …`

      - `type: Literal["file"]`

      - `id: str`

      - `created_at: datetime`

        A timestamp in RFC 3339 format

        format: date-time

      - `file_id: str`

      - `mount_path: str`

      - `updated_at: datetime`

        A timestamp in RFC 3339 format

        format: date-time

    - `class BetaManagedAgentsMemoryStoreResource: …`

      A memory store attached to an agent session.

      - `type: Literal["memory_store"]`

      - `memory_store_id: str`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `access: Optional[Literal["read_write", "read_only"]]`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `description: Optional[str]`

        Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

      - `instructions: Optional[str]`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

        maxLength: 4096

      - `mount_path: Optional[str]`

        Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

      - `name: Optional[str]`

        Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

  - `stats: BetaManagedAgentsSessionStats`

    Timing statistics for a session.

    - `active_seconds: Optional[float]`

      Cumulative time in seconds the session spent in `running` status. Excludes idle time.

      format: double

    - `duration_seconds: Optional[float]`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

      format: double

  - `status: Literal["rescheduling", "running", "idle", "terminated"]`

    SessionStatus enum

    - `"rescheduling"`

    - `"running"`

    - `"idle"`

    - `"terminated"`

  - `title: Optional[str]`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

    format: date-time

  - `usage: BetaManagedAgentsSessionUsage`

    Cumulative token usage for a session across all turns.

    - `active_seconds: Optional[float]`

      Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once, unlike `stats.active_seconds`, which sums each thread's own active time. This is the duration the session's runtime cost is priced on.

      format: double

    - `cache_creation: Optional[BetaManagedAgentsCacheCreationUsage]`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: Optional[int]`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `ephemeral_5m_input_tokens: Optional[int]`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `cache_read_input_tokens: Optional[int]`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens: Optional[int]`

      Total input tokens consumed across all turns.

      format: int32

    - `list_cost: Optional[BetaMonetaryAmount]`

      A monetary amount in a specific currency.

    - `output_tokens: Optional[int]`

      Total output tokens generated across all turns.

      format: int32

    - `server_tool_use: Optional[BetaManagedAgentsServerToolUsage]`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `web_fetch_requests: Optional[int]`

        Number of server-executed web fetch requests.

        format: int32

      - `web_search_requests: Optional[int]`

        Number of server-executed web search requests.

        format: int32

  - `vault_ids: List[str]`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `deployment_id: Optional[str]`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Beta Managed Agents Session Agent

- `class BetaManagedAgentsSessionAgent: …`

  Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

  - `type: Literal["agent"]`

  - `id: str`

  - `description: Optional[str]`

  - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

    - `type: Literal["url"]`

    - `name: str`

    - `url: str`

  - `model: BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `Literal["claude-fable-5-1", "claude-sonnet-5", "claude-fable-5", 11 more]`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `claude-fable-5-1` - Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows
        - `claude-sonnet-5` - High-performance model for coding and agents
        - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
        - `claude-opus-5` - Powerful intelligence for long-running agents and coding
        - `claude-opus-4-8` - Powerful intelligence for long-running agents and coding
        - `claude-opus-4-7` - Powerful intelligence for long-running agents and coding
        - `claude-opus-4-6` - Powerful intelligence for long-running agents and coding
        - `claude-sonnet-4-6` - Best combination of speed and intelligence
        - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
        - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
        - `claude-opus-4-5` - Powerful intelligence for long-running agents and coding
        - `claude-opus-4-5-20251101` - Powerful intelligence for long-running agents and coding
        - `claude-sonnet-4-5` - High-performance model for agents and coding
        - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

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

      - `str`

    - `effort: Optional[Effort]`

      How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

      - `class BetaManagedAgentsEffortLow: …`

        Low effort. Favors latency over reasoning depth.

        - `type: Literal["low"]`

      - `class BetaManagedAgentsEffortMedium: …`

        Medium effort. Balances latency and reasoning depth.

        - `type: Literal["medium"]`

      - `class BetaManagedAgentsEffortHigh: …`

        High effort. Favors reasoning depth.

        - `type: Literal["high"]`

      - `class BetaManagedAgentsEffortXhigh: …`

        Extra-high effort. Not all models accept this level.

        - `type: Literal["xhigh"]`

      - `class BetaManagedAgentsEffortMax: …`

        Maximum effort. Favors reasoning depth over latency.

        - `type: Literal["max"]`

    - `inference_geo: Optional[str]`

      Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

    - `speed: Optional[Literal["standard", "fast"]]`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `multiagent: Optional[BetaManagedAgentsSessionMultiagentCoordinator]`

    Resolved coordinator topology with full agent definitions for each roster member.

    - `type: Literal["coordinator"]`

    - `agents: List[Agent]`

      Full `agent` definitions the coordinator may spawn as session threads.

      - `class BetaManagedAgentsSessionThreadAgent: …`

        Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

        - `type: Literal["agent"]`

        - `id: str`

        - `description: Optional[str]`

        - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

          - `type: Literal["url"]`

          - `name: str`

          - `url: str`

        - `model: BetaManagedAgentsModelConfig`

          Model identifier and configuration.

        - `name: str`

        - `skills: List[Skill]`

          - `class BetaManagedAgentsAnthropicSkill: …`

            A resolved Anthropic-managed skill.

            - `type: Literal["anthropic"]`

            - `skill_id: str`

            - `version: str`

          - `class BetaManagedAgentsCustomSkill: …`

            A resolved user-created custom skill.

            - `type: Literal["custom"]`

            - `skill_id: str`

            - `version: str`

        - `system: Optional[str]`

        - `tools: List[Tool]`

          - `class BetaManagedAgentsAgentToolset20260401: …`

            - `type: Literal["agent_toolset_20260401"]`

            - `configs: List[BetaManagedAgentsAgentToolConfig]`

              - `class BetaManagedAgentsBashToolConfig: …`

                Configuration for the bash tool.

                - `type: Literal["bash"]`

                - `enabled: bool`

                - `name: Literal["bash"]`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                    - `type: Literal["always_allow"]`

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

                    - `type: Literal["always_ask"]`

                  - `class BetaManagedAgentsAutoPolicy: …`

                    The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `type: Literal["auto"]`

              - `class BetaManagedAgentsEditToolConfig: …`

                Configuration for the edit tool.

                - `type: Literal["edit"]`

                - `enabled: bool`

                - `name: Literal["edit"]`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

                  - `class BetaManagedAgentsAutoPolicy: …`

                    The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `class BetaManagedAgentsReadToolConfig: …`

                Configuration for the read tool.

                - `type: Literal["read"]`

                - `enabled: bool`

                - `name: Literal["read"]`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

                  - `class BetaManagedAgentsAutoPolicy: …`

                    The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `class BetaManagedAgentsWriteToolConfig: …`

                Configuration for the write tool.

                - `type: Literal["write"]`

                - `enabled: bool`

                - `name: Literal["write"]`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

                  - `class BetaManagedAgentsAutoPolicy: …`

                    The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `class BetaManagedAgentsGlobToolConfig: …`

                Configuration for the glob tool.

                - `type: Literal["glob"]`

                - `enabled: bool`

                - `name: Literal["glob"]`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

                  - `class BetaManagedAgentsAutoPolicy: …`

                    The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `class BetaManagedAgentsGrepToolConfig: …`

                Configuration for the grep tool.

                - `type: Literal["grep"]`

                - `enabled: bool`

                - `name: Literal["grep"]`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

                  - `class BetaManagedAgentsAutoPolicy: …`

                    The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `class BetaManagedAgentsWebFetchToolConfig: …`

                Configuration for the web_fetch tool.

                - `type: Literal["web_fetch"]`

                - `enabled: bool`

                - `name: Literal["web_fetch"]`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

                  - `class BetaManagedAgentsAutoPolicy: …`

                    The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `allowed_domains: Optional[List[str]]`

                - `blocked_domains: Optional[List[str]]`

                - `max_content_tokens: Optional[int]`

                  format: int32

              - `class BetaManagedAgentsWebSearchToolConfig: …`

                Configuration for the web_search tool.

                - `type: Literal["web_search"]`

                - `enabled: bool`

                - `name: Literal["web_search"]`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

                  - `class BetaManagedAgentsAutoPolicy: …`

                    The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `allowed_domains: Optional[List[str]]`

                - `blocked_domains: Optional[List[str]]`

                - `user_location: Optional[BetaManagedAgentsUserLocation]`

                  Approximate user location for search result localization.

                  - `type: Literal["approximate"]`

                    Location precision. Only "approximate" is supported.

                  - `city: Optional[str]`

                    City name.

                    minLength: 1, maxLength: 255

                  - `country: Optional[str]`

                    Two-letter ISO 3166-1 country code, uppercase.

                  - `region: Optional[str]`

                    Region or state name.

                    minLength: 1, maxLength: 255

                  - `timezone: Optional[str]`

                    IANA timezone identifier, e.g. "America/Los_Angeles".

                    minLength: 1, maxLength: 255

            - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

              Resolved default configuration for agent tools.

              - `enabled: bool`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

                - `class BetaManagedAgentsAutoPolicy: …`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

          - `class BetaManagedAgentsMCPToolset: …`

            - `type: Literal["mcp_toolset"]`

            - `configs: List[BetaManagedAgentsMCPToolConfig]`

              - `enabled: bool`

              - `name: str`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

                - `class BetaManagedAgentsAutoPolicy: …`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

              Resolved default configuration for all tools from an MCP server.

              - `enabled: bool`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

                - `class BetaManagedAgentsAutoPolicy: …`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `mcp_server_name: str`

          - `class BetaManagedAgentsCustomTool: …`

            A custom tool as returned in API responses.

            - `type: Literal["custom"]`

            - `description: str`

            - `input_schema: BetaManagedAgentsCustomToolInputSchema`

              JSON Schema for custom tool input parameters.

              - `type: Literal["object"]`

              - `properties: Optional[Dict[str, object]]`

              - `required: Optional[List[str]]`

            - `name: str`

        - `version: int`

          format: int32

      - `class BetaManagedAgentsAdvisor: …`

        Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

        - `type: Literal["advisor"]`

        - `model: str`

          The advisor model id.

  - `name: str`

  - `skills: List[Skill]`

    - `class BetaManagedAgentsAnthropicSkill: …`

      A resolved Anthropic-managed skill.

    - `class BetaManagedAgentsCustomSkill: …`

      A resolved user-created custom skill.

  - `system: Optional[str]`

  - `tools: List[Tool]`

    - `class BetaManagedAgentsAgentToolset20260401: …`

    - `class BetaManagedAgentsMCPToolset: …`

    - `class BetaManagedAgentsCustomTool: …`

      A custom tool as returned in API responses.

  - `version: int`

    format: int32

### Beta Managed Agents Session Agent Update

- `class BetaManagedAgentsSessionAgentUpdate: …`

  Mid-session agent configuration update. Only `tools` and `mcp_servers` are updatable. Full replacement: the provided array becomes the new value. To preserve existing entries, GET the session, modify the array, and POST it back.

  - `mcp_servers: Optional[List[BetaManagedAgentsURLMCPServerParams]]`

    Replacement MCP server list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.

    - `type: Literal["url"]`

    - `name: str`

      Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

      minLength: 1, maxLength: 255

    - `url: str`

      Endpoint URL for the MCP server.

      maxLength: 2048

  - `tools: Optional[List[Tool]]`

    Replacement tool list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.

    - `class BetaManagedAgentsAgentToolset20260401Params: …`

      Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

      - `type: Literal["agent_toolset_20260401"]`

      - `configs: Optional[List[BetaManagedAgentsAgentToolConfigParams]]`

        Per-tool configuration overrides.

        - `class BetaManagedAgentsBashToolConfigParams: …`

          Configuration override for the bash tool.

          - `type: Optional[Literal["bash"]]`

          - `name: Literal["bash"]`

            Must be "bash".

          - `enabled: Optional[bool]`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy: Optional[PermissionPolicy]`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

              - `type: Literal["always_allow"]`

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

              - `type: Literal["always_ask"]`

            - `class BetaManagedAgentsAutoPolicy: …`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `type: Literal["auto"]`

        - `class BetaManagedAgentsEditToolConfigParams: …`

          Configuration override for the edit tool.

          - `type: Optional[Literal["edit"]]`

          - `name: Literal["edit"]`

            Must be "edit".

          - `enabled: Optional[bool]`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy: Optional[PermissionPolicy]`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

            - `class BetaManagedAgentsAutoPolicy: …`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

        - `class BetaManagedAgentsReadToolConfigParams: …`

          Configuration override for the read tool.

          - `type: Optional[Literal["read"]]`

          - `name: Literal["read"]`

            Must be "read".

          - `enabled: Optional[bool]`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy: Optional[PermissionPolicy]`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

            - `class BetaManagedAgentsAutoPolicy: …`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

        - `class BetaManagedAgentsWriteToolConfigParams: …`

          Configuration override for the write tool.

          - `type: Optional[Literal["write"]]`

          - `name: Literal["write"]`

            Must be "write".

          - `enabled: Optional[bool]`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy: Optional[PermissionPolicy]`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

            - `class BetaManagedAgentsAutoPolicy: …`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

        - `class BetaManagedAgentsGlobToolConfigParams: …`

          Configuration override for the glob tool.

          - `type: Optional[Literal["glob"]]`

          - `name: Literal["glob"]`

            Must be "glob".

          - `enabled: Optional[bool]`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy: Optional[PermissionPolicy]`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

            - `class BetaManagedAgentsAutoPolicy: …`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

        - `class BetaManagedAgentsGrepToolConfigParams: …`

          Configuration override for the grep tool.

          - `type: Optional[Literal["grep"]]`

          - `name: Literal["grep"]`

            Must be "grep".

          - `enabled: Optional[bool]`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy: Optional[PermissionPolicy]`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

            - `class BetaManagedAgentsAutoPolicy: …`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

        - `class BetaManagedAgentsWebFetchToolConfigParams: …`

          Configuration override for the web_fetch tool.

          - `type: Optional[Literal["web_fetch"]]`

          - `name: Literal["web_fetch"]`

            Must be "web_fetch".

          - `allowed_domains: Optional[List[str]]`

            Only fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

          - `blocked_domains: Optional[List[str]]`

            Never fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

          - `enabled: Optional[bool]`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `max_content_tokens: Optional[int]`

            Maximum number of tokens of fetched text content to include in context per call. Does not apply to binary content such as PDFs.

            format: int32

          - `permission_policy: Optional[PermissionPolicy]`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

            - `class BetaManagedAgentsAutoPolicy: …`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

        - `class BetaManagedAgentsWebSearchToolConfigParams: …`

          Configuration override for the web_search tool.

          - `type: Optional[Literal["web_search"]]`

          - `name: Literal["web_search"]`

            Must be "web_search".

          - `allowed_domains: Optional[List[str]]`

            Only return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

          - `blocked_domains: Optional[List[str]]`

            Never return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

          - `enabled: Optional[bool]`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy: Optional[PermissionPolicy]`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

            - `class BetaManagedAgentsAutoPolicy: …`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

          - `user_location: Optional[BetaManagedAgentsUserLocation]`

            Approximate user location for search result localization.

            - `type: Literal["approximate"]`

              Location precision. Only "approximate" is supported.

            - `city: Optional[str]`

              City name.

              minLength: 1, maxLength: 255

            - `country: Optional[str]`

              Two-letter ISO 3166-1 country code, uppercase.

            - `region: Optional[str]`

              Region or state name.

              minLength: 1, maxLength: 255

            - `timezone: Optional[str]`

              IANA timezone identifier, e.g. "America/Los_Angeles".

              minLength: 1, maxLength: 255

      - `default_config: Optional[BetaManagedAgentsAgentToolsetDefaultConfigParams]`

        Default configuration for all tools in a toolset.

        - `enabled: Optional[bool]`

          Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

        - `permission_policy: Optional[PermissionPolicy]`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy: …`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy: …`

            Tool calls require user confirmation before execution.

          - `class BetaManagedAgentsAutoPolicy: …`

            The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

    - `class BetaManagedAgentsMCPToolsetParams: …`

      Configuration for tools from an MCP server defined in `mcp_servers`.

      - `type: Literal["mcp_toolset"]`

      - `mcp_server_name: str`

        Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

        minLength: 1, maxLength: 255

      - `configs: Optional[List[BetaManagedAgentsMCPToolConfigParams]]`

        Per-tool configuration overrides.

        - `name: str`

          Name of the MCP tool to configure. 1-128 characters.

          minLength: 1, maxLength: 128

        - `enabled: Optional[bool]`

          Whether this tool is enabled. Overrides the `default_config` setting.

        - `permission_policy: Optional[PermissionPolicy]`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy: …`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy: …`

            Tool calls require user confirmation before execution.

          - `class BetaManagedAgentsAutoPolicy: …`

            The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

      - `default_config: Optional[BetaManagedAgentsMCPToolsetDefaultConfigParams]`

        Default configuration for all tools from an MCP server.

        - `enabled: Optional[bool]`

          Whether tools are enabled by default. Defaults to true if not specified.

        - `permission_policy: Optional[PermissionPolicy]`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy: …`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy: …`

            Tool calls require user confirmation before execution.

          - `class BetaManagedAgentsAutoPolicy: …`

            The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

    - `class BetaManagedAgentsCustomToolParams: …`

      A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

      - `type: Literal["custom"]`

      - `description: str`

        Description of what the tool does, shown to the agent to help it decide when to use the tool.

        minLength: 1

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `type: Literal["object"]`

        - `properties: Optional[Dict[str, object]]`

        - `required: Optional[List[str]]`

      - `name: str`

        Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

        minLength: 1, maxLength: 128

### Beta Managed Agents Session Multiagent Coordinator

- `class BetaManagedAgentsSessionMultiagentCoordinator: …`

  Resolved coordinator topology with full agent definitions for each roster member.

  - `type: Literal["coordinator"]`

  - `agents: List[Agent]`

    Full `agent` definitions the coordinator may spawn as session threads.

    - `class BetaManagedAgentsSessionThreadAgent: …`

      Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

      - `type: Literal["agent"]`

      - `id: str`

      - `description: Optional[str]`

      - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

        - `type: Literal["url"]`

        - `name: str`

        - `url: str`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `Literal["claude-fable-5-1", "claude-sonnet-5", "claude-fable-5", 11 more]`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `claude-fable-5-1` - Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows
            - `claude-sonnet-5` - High-performance model for coding and agents
            - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
            - `claude-opus-5` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-8` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-7` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-6` - Powerful intelligence for long-running agents and coding
            - `claude-sonnet-4-6` - Best combination of speed and intelligence
            - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
            - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
            - `claude-opus-4-5` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-5-20251101` - Powerful intelligence for long-running agents and coding
            - `claude-sonnet-4-5` - High-performance model for agents and coding
            - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

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

          - `str`

        - `effort: Optional[Effort]`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow: …`

            Low effort. Favors latency over reasoning depth.

            - `type: Literal["low"]`

          - `class BetaManagedAgentsEffortMedium: …`

            Medium effort. Balances latency and reasoning depth.

            - `type: Literal["medium"]`

          - `class BetaManagedAgentsEffortHigh: …`

            High effort. Favors reasoning depth.

            - `type: Literal["high"]`

          - `class BetaManagedAgentsEffortXhigh: …`

            Extra-high effort. Not all models accept this level.

            - `type: Literal["xhigh"]`

          - `class BetaManagedAgentsEffortMax: …`

            Maximum effort. Favors reasoning depth over latency.

            - `type: Literal["max"]`

        - `inference_geo: Optional[str]`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `speed: Optional[Literal["standard", "fast"]]`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

      - `name: str`

      - `skills: List[Skill]`

        - `class BetaManagedAgentsAnthropicSkill: …`

          A resolved Anthropic-managed skill.

          - `type: Literal["anthropic"]`

          - `skill_id: str`

          - `version: str`

        - `class BetaManagedAgentsCustomSkill: …`

          A resolved user-created custom skill.

          - `type: Literal["custom"]`

          - `skill_id: str`

          - `version: str`

      - `system: Optional[str]`

      - `tools: List[Tool]`

        - `class BetaManagedAgentsAgentToolset20260401: …`

          - `type: Literal["agent_toolset_20260401"]`

          - `configs: List[BetaManagedAgentsAgentToolConfig]`

            - `class BetaManagedAgentsBashToolConfig: …`

              Configuration for the bash tool.

              - `type: Literal["bash"]`

              - `enabled: bool`

              - `name: Literal["bash"]`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                  - `type: Literal["always_allow"]`

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

                  - `type: Literal["always_ask"]`

                - `class BetaManagedAgentsAutoPolicy: …`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `type: Literal["auto"]`

            - `class BetaManagedAgentsEditToolConfig: …`

              Configuration for the edit tool.

              - `type: Literal["edit"]`

              - `enabled: bool`

              - `name: Literal["edit"]`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

                - `class BetaManagedAgentsAutoPolicy: …`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `class BetaManagedAgentsReadToolConfig: …`

              Configuration for the read tool.

              - `type: Literal["read"]`

              - `enabled: bool`

              - `name: Literal["read"]`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

                - `class BetaManagedAgentsAutoPolicy: …`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `class BetaManagedAgentsWriteToolConfig: …`

              Configuration for the write tool.

              - `type: Literal["write"]`

              - `enabled: bool`

              - `name: Literal["write"]`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

                - `class BetaManagedAgentsAutoPolicy: …`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `class BetaManagedAgentsGlobToolConfig: …`

              Configuration for the glob tool.

              - `type: Literal["glob"]`

              - `enabled: bool`

              - `name: Literal["glob"]`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

                - `class BetaManagedAgentsAutoPolicy: …`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `class BetaManagedAgentsGrepToolConfig: …`

              Configuration for the grep tool.

              - `type: Literal["grep"]`

              - `enabled: bool`

              - `name: Literal["grep"]`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

                - `class BetaManagedAgentsAutoPolicy: …`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `class BetaManagedAgentsWebFetchToolConfig: …`

              Configuration for the web_fetch tool.

              - `type: Literal["web_fetch"]`

              - `enabled: bool`

              - `name: Literal["web_fetch"]`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

                - `class BetaManagedAgentsAutoPolicy: …`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `allowed_domains: Optional[List[str]]`

              - `blocked_domains: Optional[List[str]]`

              - `max_content_tokens: Optional[int]`

                format: int32

            - `class BetaManagedAgentsWebSearchToolConfig: …`

              Configuration for the web_search tool.

              - `type: Literal["web_search"]`

              - `enabled: bool`

              - `name: Literal["web_search"]`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

                - `class BetaManagedAgentsAutoPolicy: …`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `allowed_domains: Optional[List[str]]`

              - `blocked_domains: Optional[List[str]]`

              - `user_location: Optional[BetaManagedAgentsUserLocation]`

                Approximate user location for search result localization.

                - `type: Literal["approximate"]`

                  Location precision. Only "approximate" is supported.

                - `city: Optional[str]`

                  City name.

                  minLength: 1, maxLength: 255

                - `country: Optional[str]`

                  Two-letter ISO 3166-1 country code, uppercase.

                - `region: Optional[str]`

                  Region or state name.

                  minLength: 1, maxLength: 255

                - `timezone: Optional[str]`

                  IANA timezone identifier, e.g. "America/Los_Angeles".

                  minLength: 1, maxLength: 255

          - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

            Resolved default configuration for agent tools.

            - `enabled: bool`

            - `permission_policy: PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy: …`

                Tool calls require user confirmation before execution.

              - `class BetaManagedAgentsAutoPolicy: …`

                The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

        - `class BetaManagedAgentsMCPToolset: …`

          - `type: Literal["mcp_toolset"]`

          - `configs: List[BetaManagedAgentsMCPToolConfig]`

            - `enabled: bool`

            - `name: str`

            - `permission_policy: PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy: …`

                Tool calls require user confirmation before execution.

              - `class BetaManagedAgentsAutoPolicy: …`

                The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

          - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

            Resolved default configuration for all tools from an MCP server.

            - `enabled: bool`

            - `permission_policy: PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy: …`

                Tool calls require user confirmation before execution.

              - `class BetaManagedAgentsAutoPolicy: …`

                The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

          - `mcp_server_name: str`

        - `class BetaManagedAgentsCustomTool: …`

          A custom tool as returned in API responses.

          - `type: Literal["custom"]`

          - `description: str`

          - `input_schema: BetaManagedAgentsCustomToolInputSchema`

            JSON Schema for custom tool input parameters.

            - `type: Literal["object"]`

            - `properties: Optional[Dict[str, object]]`

            - `required: Optional[List[str]]`

          - `name: str`

      - `version: int`

        format: int32

    - `class BetaManagedAgentsAdvisor: …`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `type: Literal["advisor"]`

      - `model: str`

        The advisor model id.

### Beta Managed Agents Session Stats

- `class BetaManagedAgentsSessionStats: …`

  Timing statistics for a session.

  - `active_seconds: Optional[float]`

    Cumulative time in seconds the session spent in `running` status. Excludes idle time.

    format: double

  - `duration_seconds: Optional[float]`

    Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

    format: double

### Beta Managed Agents Session Updated Event

- `class BetaManagedAgentsSessionUpdatedEvent: …`

  Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

  - `type: Literal["session.updated"]`

  - `id: str`

    Unique identifier for this event.

  - `processed_at: datetime`

    A timestamp in RFC 3339 format

    format: date-time

  - `agent: Optional[BetaManagedAgentsSessionAgent]`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `type: Literal["agent"]`

    - `id: str`

    - `description: Optional[str]`

    - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

      - `type: Literal["url"]`

      - `name: str`

      - `url: str`

    - `model: BetaManagedAgentsModelConfig`

      Model identifier and configuration.

      - `id: BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `Literal["claude-fable-5-1", "claude-sonnet-5", "claude-fable-5", 11 more]`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `claude-fable-5-1` - Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows
          - `claude-sonnet-5` - High-performance model for coding and agents
          - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
          - `claude-opus-5` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-8` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-7` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-6` - Powerful intelligence for long-running agents and coding
          - `claude-sonnet-4-6` - Best combination of speed and intelligence
          - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
          - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
          - `claude-opus-4-5` - Powerful intelligence for long-running agents and coding
          - `claude-opus-4-5-20251101` - Powerful intelligence for long-running agents and coding
          - `claude-sonnet-4-5` - High-performance model for agents and coding
          - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

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

        - `str`

      - `effort: Optional[Effort]`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

        - `class BetaManagedAgentsEffortLow: …`

          Low effort. Favors latency over reasoning depth.

          - `type: Literal["low"]`

        - `class BetaManagedAgentsEffortMedium: …`

          Medium effort. Balances latency and reasoning depth.

          - `type: Literal["medium"]`

        - `class BetaManagedAgentsEffortHigh: …`

          High effort. Favors reasoning depth.

          - `type: Literal["high"]`

        - `class BetaManagedAgentsEffortXhigh: …`

          Extra-high effort. Not all models accept this level.

          - `type: Literal["xhigh"]`

        - `class BetaManagedAgentsEffortMax: …`

          Maximum effort. Favors reasoning depth over latency.

          - `type: Literal["max"]`

      - `inference_geo: Optional[str]`

        Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

      - `speed: Optional[Literal["standard", "fast"]]`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `multiagent: Optional[BetaManagedAgentsSessionMultiagentCoordinator]`

      Resolved coordinator topology with full agent definitions for each roster member.

      - `type: Literal["coordinator"]`

      - `agents: List[Agent]`

        Full `agent` definitions the coordinator may spawn as session threads.

        - `class BetaManagedAgentsSessionThreadAgent: …`

          Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

          - `type: Literal["agent"]`

          - `id: str`

          - `description: Optional[str]`

          - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

            - `type: Literal["url"]`

            - `name: str`

            - `url: str`

          - `model: BetaManagedAgentsModelConfig`

            Model identifier and configuration.

          - `name: str`

          - `skills: List[Skill]`

            - `class BetaManagedAgentsAnthropicSkill: …`

              A resolved Anthropic-managed skill.

              - `type: Literal["anthropic"]`

              - `skill_id: str`

              - `version: str`

            - `class BetaManagedAgentsCustomSkill: …`

              A resolved user-created custom skill.

              - `type: Literal["custom"]`

              - `skill_id: str`

              - `version: str`

          - `system: Optional[str]`

          - `tools: List[Tool]`

            - `class BetaManagedAgentsAgentToolset20260401: …`

              - `type: Literal["agent_toolset_20260401"]`

              - `configs: List[BetaManagedAgentsAgentToolConfig]`

                - `class BetaManagedAgentsBashToolConfig: …`

                  Configuration for the bash tool.

                  - `type: Literal["bash"]`

                  - `enabled: bool`

                  - `name: Literal["bash"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                      - `type: Literal["always_allow"]`

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                      - `type: Literal["always_ask"]`

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                      - `type: Literal["auto"]`

                - `class BetaManagedAgentsEditToolConfig: …`

                  Configuration for the edit tool.

                  - `type: Literal["edit"]`

                  - `enabled: bool`

                  - `name: Literal["edit"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `class BetaManagedAgentsReadToolConfig: …`

                  Configuration for the read tool.

                  - `type: Literal["read"]`

                  - `enabled: bool`

                  - `name: Literal["read"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `class BetaManagedAgentsWriteToolConfig: …`

                  Configuration for the write tool.

                  - `type: Literal["write"]`

                  - `enabled: bool`

                  - `name: Literal["write"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `class BetaManagedAgentsGlobToolConfig: …`

                  Configuration for the glob tool.

                  - `type: Literal["glob"]`

                  - `enabled: bool`

                  - `name: Literal["glob"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `class BetaManagedAgentsGrepToolConfig: …`

                  Configuration for the grep tool.

                  - `type: Literal["grep"]`

                  - `enabled: bool`

                  - `name: Literal["grep"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `class BetaManagedAgentsWebFetchToolConfig: …`

                  Configuration for the web_fetch tool.

                  - `type: Literal["web_fetch"]`

                  - `enabled: bool`

                  - `name: Literal["web_fetch"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `allowed_domains: Optional[List[str]]`

                  - `blocked_domains: Optional[List[str]]`

                  - `max_content_tokens: Optional[int]`

                    format: int32

                - `class BetaManagedAgentsWebSearchToolConfig: …`

                  Configuration for the web_search tool.

                  - `type: Literal["web_search"]`

                  - `enabled: bool`

                  - `name: Literal["web_search"]`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `allowed_domains: Optional[List[str]]`

                  - `blocked_domains: Optional[List[str]]`

                  - `user_location: Optional[BetaManagedAgentsUserLocation]`

                    Approximate user location for search result localization.

                    - `type: Literal["approximate"]`

                      Location precision. Only "approximate" is supported.

                    - `city: Optional[str]`

                      City name.

                      minLength: 1, maxLength: 255

                    - `country: Optional[str]`

                      Two-letter ISO 3166-1 country code, uppercase.

                    - `region: Optional[str]`

                      Region or state name.

                      minLength: 1, maxLength: 255

                    - `timezone: Optional[str]`

                      IANA timezone identifier, e.g. "America/Los_Angeles".

                      minLength: 1, maxLength: 255

              - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

                Resolved default configuration for agent tools.

                - `enabled: bool`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

                  - `class BetaManagedAgentsAutoPolicy: …`

                    The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `class BetaManagedAgentsMCPToolset: …`

              - `type: Literal["mcp_toolset"]`

              - `configs: List[BetaManagedAgentsMCPToolConfig]`

                - `enabled: bool`

                - `name: str`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

                  - `class BetaManagedAgentsAutoPolicy: …`

                    The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `enabled: bool`

                - `permission_policy: PermissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy: …`

                    Tool calls require user confirmation before execution.

                  - `class BetaManagedAgentsAutoPolicy: …`

                    The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `mcp_server_name: str`

            - `class BetaManagedAgentsCustomTool: …`

              A custom tool as returned in API responses.

              - `type: Literal["custom"]`

              - `description: str`

              - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                JSON Schema for custom tool input parameters.

                - `type: Literal["object"]`

                - `properties: Optional[Dict[str, object]]`

                - `required: Optional[List[str]]`

              - `name: str`

          - `version: int`

            format: int32

        - `class BetaManagedAgentsAdvisor: …`

          Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

          - `type: Literal["advisor"]`

          - `model: str`

            The advisor model id.

    - `name: str`

    - `skills: List[Skill]`

      - `class BetaManagedAgentsAnthropicSkill: …`

        A resolved Anthropic-managed skill.

      - `class BetaManagedAgentsCustomSkill: …`

        A resolved user-created custom skill.

    - `system: Optional[str]`

    - `tools: List[Tool]`

      - `class BetaManagedAgentsAgentToolset20260401: …`

      - `class BetaManagedAgentsMCPToolset: …`

      - `class BetaManagedAgentsCustomTool: …`

        A custom tool as returned in API responses.

    - `version: int`

      format: int32

  - `budget: Optional[BetaManagedAgentsBudgetLimit]`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `type: Literal["limit"]`

    - `max_list_cost: BetaMonetaryAmount`

      A monetary amount in a specific currency.

      - `amount: str`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

  - `metadata: Optional[Dict[str, str]]`

    The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

  - `title: Optional[str]`

    The session's new title. Present only when the update changed it.

### Beta Managed Agents Session Usage

- `class BetaManagedAgentsSessionUsage: …`

  Cumulative token usage for a session across all turns.

  - `active_seconds: Optional[float]`

    Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once, unlike `stats.active_seconds`, which sums each thread's own active time. This is the duration the session's runtime cost is priced on.

    format: double

  - `cache_creation: Optional[BetaManagedAgentsCacheCreationUsage]`

    Prompt-cache creation token usage broken down by cache lifetime.

    - `ephemeral_1h_input_tokens: Optional[int]`

      Tokens used to create 1-hour ephemeral cache entries.

      format: int32

    - `ephemeral_5m_input_tokens: Optional[int]`

      Tokens used to create 5-minute ephemeral cache entries.

      format: int32

  - `cache_read_input_tokens: Optional[int]`

    Total tokens read from prompt cache.

    format: int32

  - `input_tokens: Optional[int]`

    Total input tokens consumed across all turns.

    format: int32

  - `list_cost: Optional[BetaMonetaryAmount]`

    A monetary amount in a specific currency.

    - `amount: str`

      Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

    - `currency: BetaCurrency`

      Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

  - `output_tokens: Optional[int]`

    Total output tokens generated across all turns.

    format: int32

  - `server_tool_use: Optional[BetaManagedAgentsServerToolUsage]`

    Cumulative count of server-executed tool invocations, broken down by tool.

    - `web_fetch_requests: Optional[int]`

      Number of server-executed web fetch requests.

      format: int32

    - `web_search_requests: Optional[int]`

      Number of server-executed web search requests.

      format: int32

### Beta Managed Agents Session Usage Event

- `class BetaManagedAgentsSessionUsageEvent: …`

  Periodic snapshot of the session's cumulative usage and tracked list cost.

  - `type: Literal["session.usage"]`

  - `id: str`

    Unique identifier for this event.

  - `processed_at: datetime`

    A timestamp in RFC 3339 format

    format: date-time

  - `usage: BetaManagedAgentsSessionUsageSnapshot`

    Point-in-time snapshot of a session's cumulative usage.

    - `active_seconds: Optional[float]`

      Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

      format: double

    - `cache_creation: Optional[BetaManagedAgentsCacheCreationUsage]`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: Optional[int]`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `ephemeral_5m_input_tokens: Optional[int]`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `cache_read_input_tokens: Optional[int]`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens: Optional[int]`

      Total input tokens consumed across all turns.

      format: int32

    - `list_cost: Optional[BetaMonetaryAmount]`

      A monetary amount in a specific currency.

      - `amount: str`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `output_tokens: Optional[int]`

      Total output tokens generated across all turns.

      format: int32

    - `server_tool_use: Optional[BetaManagedAgentsServerToolUsage]`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `web_fetch_requests: Optional[int]`

        Number of server-executed web fetch requests.

        format: int32

      - `web_search_requests: Optional[int]`

        Number of server-executed web search requests.

        format: int32

  - `budget: Optional[BetaManagedAgentsBudgetLimit]`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `type: Literal["limit"]`

    - `max_list_cost: BetaMonetaryAmount`

      A monetary amount in a specific currency.

### Beta Managed Agents Start Event

- `class BetaManagedAgentsStartEvent: …`

  Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

  - `type: Literal["event_start"]`

  - `event: BetaManagedAgentsStartEventPreview`

    The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

    - `class BetaManagedAgentsAgentMessagePreview: …`

      - `type: Literal["agent.message"]`

      - `id: str`

        The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

    - `class BetaManagedAgentsAgentThinkingPreview: …`

      - `type: Literal["agent.thinking"]`

      - `id: str`

        The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

### Beta Managed Agents Start Event Preview

- `BetaManagedAgentsStartEventPreview`

  - `class BetaManagedAgentsAgentMessagePreview: …`

    - `type: Literal["agent.message"]`

    - `id: str`

      The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

  - `class BetaManagedAgentsAgentThinkingPreview: …`

    - `type: Literal["agent.thinking"]`

    - `id: str`

      The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

### Beta Managed Agents System Content Block

- `class BetaManagedAgentsSystemContentBlock: …`

  Regular text content.

  - `type: Literal["text"]`

  - `text: str`

    The text content.

    minLength: 1

### Beta Managed Agents System Message Event

- `class BetaManagedAgentsSystemMessageEvent: …`

  A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

  - `type: Literal["system.message"]`

  - `id: str`

    Unique identifier for this event.

  - `content: List[BetaManagedAgentsSystemContentBlock]`

    System content blocks. Text-only.

    - `type: Literal["text"]`

    - `text: str`

      The text content.

      minLength: 1

  - `processed_at: Optional[datetime]`

    A timestamp in RFC 3339 format

    format: date-time

### Beta Managed Agents User Tool Result Event

- `class BetaManagedAgentsUserToolResultEvent: …`

  Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

  - `type: Literal["user.tool_result"]`

  - `id: str`

    Unique identifier for this event.

  - `tool_use_id: str`

    The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `content: Optional[List[Content]]`

    The result content returned by the tool.

    - `class BetaManagedAgentsTextBlock: …`

      Regular text content.

      - `type: Literal["text"]`

      - `text: str`

        The text content.

        minLength: 1

    - `class BetaManagedAgentsImageBlock: …`

      Image content specified directly as base64 data or as a reference via a URL.

      - `type: Literal["image"]`

      - `source: Source`

        Union type for image source variants.

        - `class BetaManagedAgentsBase64ImageSource: …`

          Base64-encoded image data.

          - `type: Literal["base64"]`

          - `data: str`

            Base64-encoded image data.

            minLength: 1

          - `media_type: str`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            minLength: 1

        - `class BetaManagedAgentsURLImageSource: …`

          Image referenced by URL.

          - `type: Literal["url"]`

          - `url: str`

            URL of the image to fetch.

            minLength: 1

        - `class BetaManagedAgentsFileImageSource: …`

          Image referenced by file ID.

          - `type: Literal["file"]`

          - `file_id: str`

            ID of a previously uploaded file.

            minLength: 1

    - `class BetaManagedAgentsDocumentBlock: …`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `type: Literal["document"]`

      - `source: Source`

        Union type for document source variants.

        - `class BetaManagedAgentsBase64DocumentSource: …`

          Base64-encoded document data.

          - `type: Literal["base64"]`

          - `data: str`

            Base64-encoded document data.

            minLength: 1

          - `media_type: str`

            MIME type of the document (e.g., "application/pdf").

            minLength: 1

        - `class BetaManagedAgentsPlainTextDocumentSource: …`

          Plain text document content.

          - `type: Literal["text"]`

          - `data: str`

            The plain text content.

            minLength: 1

          - `media_type: Literal["text/plain"]`

            MIME type of the text content. Must be "text/plain".

        - `class BetaManagedAgentsURLDocumentSource: …`

          Document referenced by URL.

          - `type: Literal["url"]`

          - `url: str`

            URL of the document to fetch.

            minLength: 1

        - `class BetaManagedAgentsFileDocumentSource: …`

          Document referenced by file ID.

          - `type: Literal["file"]`

          - `file_id: str`

            ID of a previously uploaded file.

            minLength: 1

      - `context: Optional[str]`

        Additional context about the document for the model.

      - `title: Optional[str]`

        The title of the document.

    - `class BetaManagedAgentsSearchResultBlock: …`

      A block containing a web search result.

      - `type: Literal["search_result"]`

      - `citations: BetaManagedAgentsSearchResultCitations`

        Citation settings for a search result.

        - `enabled: bool`

          Whether citations are enabled for this search result.

      - `content: List[BetaManagedAgentsSearchResultContent]`

        Array of text content blocks from the search result.

        - `type: Literal["text"]`

        - `text: str`

          The text content.

          minLength: 1

      - `source: str`

        The URL source of the search result.

        minLength: 1

      - `title: str`

        The title of the search result.

        minLength: 1

  - `is_error: Optional[bool]`

    Whether the tool execution resulted in an error.

  - `processed_at: Optional[datetime]`

    A timestamp in RFC 3339 format

    format: date-time

  - `session_thread_id: Optional[str]`

    Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

## Sessions › Events

### List Events

`beta.sessions.events.list(session_id, **kwargs)  -> SyncPageCursor[BetaManagedAgentsSessionEvent]`

**GET** `/v1/sessions/{session_id}/events`

List Events

#### Parameters

- `session_id: str`

- `created_at_gt: Optional[Union[str, datetime]]`

  Return events created after this time (exclusive). Compared against the event's `processed_at` value.

  format: date-time

- `created_at_gte: Optional[Union[str, datetime]]`

  Return events created at or after this time (inclusive). Compared against the event's `processed_at` value.

  format: date-time

- `created_at_lt: Optional[Union[str, datetime]]`

  Return events created before this time (exclusive). Compared against the event's `processed_at` value.

  format: date-time

- `created_at_lte: Optional[Union[str, datetime]]`

  Return events created at or before this time (inclusive). Compared against the event's `processed_at` value.

  format: date-time

- `limit: Optional[int]`

  Query parameter for limit

  format: int32

- `order: Optional[Literal["asc", "desc"]]`

  Sort direction for results, ordered by the event's `processed_at`. Defaults to `asc` (chronological).

  - `"asc"`

  - `"desc"`

- `page: Optional[str]`

  Opaque pagination cursor from a previous response's `next_page`.

- `types: Optional[Sequence[str]]`

  Filter by event type. Values match the `type` field on returned events (for example, `user.message` or `agent.tool_use`). Omit to return all event types.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

- `workspace_id: Optional[str]`

#### Returns

- `BetaManagedAgentsSessionEvent`

  Union type for all event types in a session.

  - `class BetaManagedAgentsUserMessageEvent: …`

    A user message event in the session conversation.

    - `type: Literal["user.message"]`

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

        - `type: Literal["text"]`

        - `text: str`

          The text content.

          minLength: 1

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

        - `type: Literal["image"]`

        - `source: Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource: …`

            Base64-encoded image data.

            - `type: Literal["base64"]`

            - `data: str`

              Base64-encoded image data.

              minLength: 1

            - `media_type: str`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

          - `class BetaManagedAgentsURLImageSource: …`

            Image referenced by URL.

            - `type: Literal["url"]`

            - `url: str`

              URL of the image to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileImageSource: …`

            Image referenced by file ID.

            - `type: Literal["file"]`

            - `file_id: str`

              ID of a previously uploaded file.

              minLength: 1

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `type: Literal["document"]`

        - `source: Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource: …`

            Base64-encoded document data.

            - `type: Literal["base64"]`

            - `data: str`

              Base64-encoded document data.

              minLength: 1

            - `media_type: str`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

          - `class BetaManagedAgentsPlainTextDocumentSource: …`

            Plain text document content.

            - `type: Literal["text"]`

            - `data: str`

              The plain text content.

              minLength: 1

            - `media_type: Literal["text/plain"]`

              MIME type of the text content. Must be "text/plain".

          - `class BetaManagedAgentsURLDocumentSource: …`

            Document referenced by URL.

            - `type: Literal["url"]`

            - `url: str`

              URL of the document to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileDocumentSource: …`

            Document referenced by file ID.

            - `type: Literal["file"]`

            - `file_id: str`

              ID of a previously uploaded file.

              minLength: 1

        - `context: Optional[str]`

          Additional context about the document for the model.

        - `title: Optional[str]`

          The title of the document.

      - `class BetaManagedAgentsRedactedBlock: …`

        Placeholder for content withheld by Anthropic model policy.

        - `type: Literal["redacted"]`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsUserInterruptEvent: …`

    An interrupt event that pauses agent execution and returns control to the user.

    - `type: Literal["user.interrupt"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: Optional[str]`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEvent: …`

    A tool confirmation event that approves or denies a pending tool execution.

    - `type: Literal["user.tool_confirmation"]`

    - `id: str`

      Unique identifier for this event.

    - `result: Literal["allow", "deny"]`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: str`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `deny_message: Optional[str]`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: Optional[str]`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `class BetaManagedAgentsUserCustomToolResultEvent: …`

    Event sent by the client providing the result of a custom tool execution.

    - `type: Literal["user.custom_tool_result"]`

    - `id: str`

      Unique identifier for this event.

    - `custom_tool_use_id: str`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

        - `type: Literal["search_result"]`

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `enabled: bool`

            Whether citations are enabled for this search result.

        - `content: List[BetaManagedAgentsSearchResultContent]`

          Array of text content blocks from the search result.

          - `type: Literal["text"]`

          - `text: str`

            The text content.

            minLength: 1

        - `source: str`

          The URL source of the search result.

          minLength: 1

        - `title: str`

          The title of the search result.

          minLength: 1

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: Optional[str]`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsAgentCustomToolUseEvent: …`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `type: Literal["agent.custom_tool_use"]`

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `name: str`

      Name of the custom tool being called.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `class BetaManagedAgentsAgentMessageEvent: …`

    An agent response event in the session conversation.

    - `type: Literal["agent.message"]`

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Array of text blocks comprising the agent response.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsRedactedBlock: …`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsAgentThinkingEvent: …`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `type: Literal["agent.thinking"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsAgentMCPToolUseEvent: …`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `type: Literal["agent.mcp_tool_use"]`

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `mcp_server_name: str`

      Name of the MCP server providing the tool.

    - `name: str`

      Name of the MCP tool being used.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `evaluated_permission: Optional[Literal["allow", "ask", "deny"]]`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `evaluation: Optional[BetaManagedAgentsAgentToolEvaluation]`

      Names the resolved permission_policy that produced evaluated_permission, and under auto carries the judgement. Open union: clients must tolerate unknown variants.

      - `class BetaManagedAgentsAgentToolEvaluationAlwaysAllow: …`

        The resolved permission_policy was always_allow; accompanies evaluated_permission "allow".

        - `type: Literal["always_allow"]`

      - `class BetaManagedAgentsAgentToolEvaluationAlwaysAsk: …`

        The resolved permission_policy was always_ask; accompanies evaluated_permission "ask".

        - `type: Literal["always_ask"]`

      - `class BetaManagedAgentsAgentToolEvaluationAuto: …`

        The resolved permission_policy was auto: the server judged this invocation individually.

        - `type: Literal["auto"]`

        - `evaluated_permission: BetaManagedAgentsAgentAutoEvaluatedPermission`

          The server's per-invocation judgement under the auto permission policy. Its type always equals the event's top-level evaluated_permission. Open union: clients must tolerate unknown variants.

          - `class BetaManagedAgentsAgentAutoEvaluatedPermissionAllow: …`

            The server judged the invocation safe to execute without client approval.

            - `type: Literal["allow"]`

          - `class BetaManagedAgentsAgentAutoEvaluatedPermissionAsk: …`

            The server reached no judgement; the invocation is held for client approval.

            - `type: Literal["ask"]`

            - `reason_code: str`

              The judgement's grounds in registry-bound terms, for client branching and audit rather than end-user display. Open registry; currently "indeterminate" (no judgement was reached). Clients must tolerate values outside this set.

              maxLength: 64

          - `class BetaManagedAgentsAgentAutoEvaluatedPermissionDeny: …`

            The server judged the invocation high-risk; it does not execute and a synthetic error tool result is appended.

            - `type: Literal["deny"]`

            - `reason_code: str`

              The judgement's grounds in registry-bound terms. Open registry; currently "high_risk" (judged high-risk; the call does not run). Clients must tolerate values outside this set.

              maxLength: 64

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentMCPToolResultEvent: …`

    Event representing the result of an MCP tool execution.

    - `type: Literal["agent.mcp_tool_result"]`

    - `id: str`

      Unique identifier for this event.

    - `mcp_tool_use_id: str`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent: …`

    Event emitted when the agent invokes a built-in agent tool.

    - `type: Literal["agent.tool_use"]`

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `name: str`

      Name of the agent tool being used.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `evaluated_permission: Optional[Literal["allow", "ask", "deny"]]`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `evaluation: Optional[BetaManagedAgentsAgentToolEvaluation]`

      Names the resolved permission_policy that produced evaluated_permission, and under auto carries the judgement. Open union: clients must tolerate unknown variants.

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentToolResultEvent: …`

    Event representing the result of an agent tool execution.

    - `type: Literal["agent.tool_result"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `tool_use_id: str`

      The id of the `agent.tool_use` event this result corresponds to.

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadMessageReceivedEvent: …`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `type: Literal["agent.thread_message_received"]`

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock: …`

        Placeholder for content withheld by Anthropic model policy.

    - `from_session_thread_id: str`

      Public `sthr_` ID of the thread that sent the message.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `from_agent_name: Optional[str]`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class BetaManagedAgentsAgentThreadMessageSentEvent: …`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `type: Literal["agent.thread_message_sent"]`

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock: …`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `to_session_thread_id: str`

      Public `sthr_` ID of the thread the message was sent to.

    - `to_agent_name: Optional[str]`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent: …`

    Indicates that context compaction (summarization) occurred during the session.

    - `type: Literal["agent.thread_context_compacted"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionErrorEvent: …`

    An error event indicating a problem occurred during session execution.

    - `type: Literal["session.error"]`

    - `id: str`

      Unique identifier for this event.

    - `error: Error`

      - `class BetaManagedAgentsUnknownError: …`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `type: Literal["unknown_error"]`

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: Literal["retrying"]`

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: Literal["exhausted"]`

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: Literal["terminal"]`

      - `class BetaManagedAgentsModelOverloadedError: …`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `type: Literal["model_overloaded_error"]`

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

      - `class BetaManagedAgentsModelRateLimitedError: …`

        The model request was rate-limited.

        - `type: Literal["model_rate_limited_error"]`

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

      - `class BetaManagedAgentsModelRequestFailedError: …`

        A model request failed for a reason other than overload or rate-limiting.

        - `type: Literal["model_request_failed_error"]`

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

      - `class BetaManagedAgentsMCPConnectionFailedError: …`

        Failed to connect to an MCP server.

        - `type: Literal["mcp_connection_failed_error"]`

        - `mcp_server_name: str`

          Name of the MCP server that failed to connect.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

      - `class BetaManagedAgentsMCPAuthenticationFailedError: …`

        Authentication to an MCP server failed.

        - `type: Literal["mcp_authentication_failed_error"]`

        - `mcp_server_name: str`

          Name of the MCP server that failed authentication.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

      - `class BetaManagedAgentsBillingError: …`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `type: Literal["billing_error"]`

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

      - `class BetaManagedAgentsCredentialHostUnreachableError: …`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `type: Literal["credential_host_unreachable_error"]`

        - `credential_id: str`

          ID of the affected credential.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `vault_id: str`

          ID of the vault containing the affected credential.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionStatusRescheduledEvent: …`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `type: Literal["session.status_rescheduled"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionStatusRunningEvent: …`

    Indicates the session is actively running and the agent is working.

    - `type: Literal["session.status_running"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionStatusIdleEvent: …`

    Indicates the agent has paused and is awaiting user input.

    - `type: Literal["session.status_idle"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `stop_reason: StopReason`

      - `class BetaManagedAgentsSessionEndTurn: …`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: Literal["end_turn"]`

      - `class BetaManagedAgentsSessionRequiresAction: …`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `type: Literal["requires_action"]`

        - `event_ids: List[str]`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

      - `class BetaManagedAgentsSessionRetriesExhausted: …`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `type: Literal["retries_exhausted"]`

      - `class BetaManagedAgentsSessionBudgetReached: …`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `type: Literal["budget_reached"]`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent: …`

    Indicates the session has terminated, either due to an error or completion.

    - `type: Literal["session.status_terminated"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionThreadCreatedEvent: …`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `type: Literal["session.thread_created"]`

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the callable agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: str`

      Public `sthr_` ID of the newly created thread.

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent: …`

    Emitted when an outcome evaluation cycle begins.

    - `type: Literal["span.outcome_evaluation_start"]`

    - `id: str`

      Unique identifier for this event.

    - `iteration: int`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

      format: int32

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent: …`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `type: Literal["span.outcome_evaluation_end"]`

    - `id: str`

      Unique identifier for this event.

    - `explanation: str`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `iteration: int`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `outcome_evaluation_start_id: str`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `result: str`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `cache_creation_input_tokens: int`

        Tokens used to create prompt cache in this request.

        format: int32

      - `cache_read_input_tokens: int`

        Tokens read from prompt cache in this request.

        format: int32

      - `input_tokens: int`

        Input tokens consumed by this request.

        format: int32

      - `output_tokens: int`

        Output tokens generated by this request.

        format: int32

      - `speed: Optional[Literal["standard", "fast"]]`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `class BetaManagedAgentsSpanModelRequestStartEvent: …`

    Emitted when a model request is initiated by the agent.

    - `type: Literal["span.model_request_start"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSpanModelRequestEndEvent: …`

    Emitted when a model request completes.

    - `type: Literal["span.model_request_end"]`

    - `id: str`

      Unique identifier for this event.

    - `is_error: Optional[bool]`

      Whether the model request resulted in an error.

    - `model_request_start_id: str`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent: …`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `type: Literal["span.outcome_evaluation_ongoing"]`

    - `id: str`

      Unique identifier for this event.

    - `iteration: int`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsUserDefineOutcomeEvent: …`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `type: Literal["user.define_outcome"]`

    - `id: str`

      Unique identifier for this event.

    - `description: str`

      What the agent should produce. Copied from the input event.

    - `max_iterations: Optional[int]`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

      format: int32

    - `outcome_id: str`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `rubric: Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric: …`

        Rubric referenced by a file uploaded via the Files API.

        - `type: Literal["file"]`

        - `file_id: str`

          ID of the rubric file.

      - `class BetaManagedAgentsTextRubric: …`

        Rubric content provided inline as text.

        - `type: Literal["text"]`

        - `content: str`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

  - `class BetaManagedAgentsSessionDeletedEvent: …`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `type: Literal["session.deleted"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent: …`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: Literal["session.thread_status_running"]`

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: str`

      Public sthr_ ID of the thread that started running.

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent: …`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: Literal["session.thread_status_idle"]`

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: str`

      Public sthr_ ID of the thread that went idle.

    - `stop_reason: StopReason`

      - `class BetaManagedAgentsSessionEndTurn: …`

        The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionRequiresAction: …`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `class BetaManagedAgentsSessionRetriesExhausted: …`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `class BetaManagedAgentsSessionBudgetReached: …`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent: …`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: Literal["session.thread_status_terminated"]`

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: str`

      Public sthr_ ID of the thread that terminated.

  - `class BetaManagedAgentsUserToolResultEvent: …`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `type: Literal["user.tool_result"]`

    - `id: str`

      Unique identifier for this event.

    - `tool_use_id: str`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: Optional[str]`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent: …`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: Literal["session.thread_status_rescheduled"]`

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: str`

      Public sthr_ ID of the thread that is retrying.

  - `class BetaManagedAgentsSessionUpdatedEvent: …`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `type: Literal["session.updated"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `agent: Optional[BetaManagedAgentsSessionAgent]`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `type: Literal["agent"]`

      - `id: str`

      - `description: Optional[str]`

      - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

        - `type: Literal["url"]`

        - `name: str`

        - `url: str`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `Literal["claude-fable-5-1", "claude-sonnet-5", "claude-fable-5", 11 more]`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `claude-fable-5-1` - Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows
            - `claude-sonnet-5` - High-performance model for coding and agents
            - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
            - `claude-opus-5` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-8` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-7` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-6` - Powerful intelligence for long-running agents and coding
            - `claude-sonnet-4-6` - Best combination of speed and intelligence
            - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
            - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
            - `claude-opus-4-5` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-5-20251101` - Powerful intelligence for long-running agents and coding
            - `claude-sonnet-4-5` - High-performance model for agents and coding
            - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

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

          - `str`

        - `effort: Optional[Effort]`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow: …`

            Low effort. Favors latency over reasoning depth.

            - `type: Literal["low"]`

          - `class BetaManagedAgentsEffortMedium: …`

            Medium effort. Balances latency and reasoning depth.

            - `type: Literal["medium"]`

          - `class BetaManagedAgentsEffortHigh: …`

            High effort. Favors reasoning depth.

            - `type: Literal["high"]`

          - `class BetaManagedAgentsEffortXhigh: …`

            Extra-high effort. Not all models accept this level.

            - `type: Literal["xhigh"]`

          - `class BetaManagedAgentsEffortMax: …`

            Maximum effort. Favors reasoning depth over latency.

            - `type: Literal["max"]`

        - `inference_geo: Optional[str]`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `speed: Optional[Literal["standard", "fast"]]`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

      - `multiagent: Optional[BetaManagedAgentsSessionMultiagentCoordinator]`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `type: Literal["coordinator"]`

        - `agents: List[Agent]`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `class BetaManagedAgentsSessionThreadAgent: …`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `type: Literal["agent"]`

            - `id: str`

            - `description: Optional[str]`

            - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

              - `type: Literal["url"]`

              - `name: str`

              - `url: str`

            - `model: BetaManagedAgentsModelConfig`

              Model identifier and configuration.

            - `name: str`

            - `skills: List[Skill]`

              - `class BetaManagedAgentsAnthropicSkill: …`

                A resolved Anthropic-managed skill.

                - `type: Literal["anthropic"]`

                - `skill_id: str`

                - `version: str`

              - `class BetaManagedAgentsCustomSkill: …`

                A resolved user-created custom skill.

                - `type: Literal["custom"]`

                - `skill_id: str`

                - `version: str`

            - `system: Optional[str]`

            - `tools: List[Tool]`

              - `class BetaManagedAgentsAgentToolset20260401: …`

                - `type: Literal["agent_toolset_20260401"]`

                - `configs: List[BetaManagedAgentsAgentToolConfig]`

                  - `class BetaManagedAgentsBashToolConfig: …`

                    Configuration for the bash tool.

                    - `type: Literal["bash"]`

                    - `enabled: bool`

                    - `name: Literal["bash"]`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                        - `type: Literal["always_allow"]`

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                        - `type: Literal["always_ask"]`

                      - `class BetaManagedAgentsAutoPolicy: …`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                        - `type: Literal["auto"]`

                  - `class BetaManagedAgentsEditToolConfig: …`

                    Configuration for the edit tool.

                    - `type: Literal["edit"]`

                    - `enabled: bool`

                    - `name: Literal["edit"]`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                      - `class BetaManagedAgentsAutoPolicy: …`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `class BetaManagedAgentsReadToolConfig: …`

                    Configuration for the read tool.

                    - `type: Literal["read"]`

                    - `enabled: bool`

                    - `name: Literal["read"]`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                      - `class BetaManagedAgentsAutoPolicy: …`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `class BetaManagedAgentsWriteToolConfig: …`

                    Configuration for the write tool.

                    - `type: Literal["write"]`

                    - `enabled: bool`

                    - `name: Literal["write"]`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                      - `class BetaManagedAgentsAutoPolicy: …`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `class BetaManagedAgentsGlobToolConfig: …`

                    Configuration for the glob tool.

                    - `type: Literal["glob"]`

                    - `enabled: bool`

                    - `name: Literal["glob"]`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                      - `class BetaManagedAgentsAutoPolicy: …`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `class BetaManagedAgentsGrepToolConfig: …`

                    Configuration for the grep tool.

                    - `type: Literal["grep"]`

                    - `enabled: bool`

                    - `name: Literal["grep"]`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                      - `class BetaManagedAgentsAutoPolicy: …`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `class BetaManagedAgentsWebFetchToolConfig: …`

                    Configuration for the web_fetch tool.

                    - `type: Literal["web_fetch"]`

                    - `enabled: bool`

                    - `name: Literal["web_fetch"]`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                      - `class BetaManagedAgentsAutoPolicy: …`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `allowed_domains: Optional[List[str]]`

                    - `blocked_domains: Optional[List[str]]`

                    - `max_content_tokens: Optional[int]`

                      format: int32

                  - `class BetaManagedAgentsWebSearchToolConfig: …`

                    Configuration for the web_search tool.

                    - `type: Literal["web_search"]`

                    - `enabled: bool`

                    - `name: Literal["web_search"]`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                      - `class BetaManagedAgentsAutoPolicy: …`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `allowed_domains: Optional[List[str]]`

                    - `blocked_domains: Optional[List[str]]`

                    - `user_location: Optional[BetaManagedAgentsUserLocation]`

                      Approximate user location for search result localization.

                      - `type: Literal["approximate"]`

                        Location precision. Only "approximate" is supported.

                      - `city: Optional[str]`

                        City name.

                        minLength: 1, maxLength: 255

                      - `country: Optional[str]`

                        Two-letter ISO 3166-1 country code, uppercase.

                      - `region: Optional[str]`

                        Region or state name.

                        minLength: 1, maxLength: 255

                      - `timezone: Optional[str]`

                        IANA timezone identifier, e.g. "America/Los_Angeles".

                        minLength: 1, maxLength: 255

                - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

                  Resolved default configuration for agent tools.

                  - `enabled: bool`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `class BetaManagedAgentsMCPToolset: …`

                - `type: Literal["mcp_toolset"]`

                - `configs: List[BetaManagedAgentsMCPToolConfig]`

                  - `enabled: bool`

                  - `name: str`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `enabled: bool`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `mcp_server_name: str`

              - `class BetaManagedAgentsCustomTool: …`

                A custom tool as returned in API responses.

                - `type: Literal["custom"]`

                - `description: str`

                - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                  JSON Schema for custom tool input parameters.

                  - `type: Literal["object"]`

                  - `properties: Optional[Dict[str, object]]`

                  - `required: Optional[List[str]]`

                - `name: str`

            - `version: int`

              format: int32

          - `class BetaManagedAgentsAdvisor: …`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `type: Literal["advisor"]`

            - `model: str`

              The advisor model id.

      - `name: str`

      - `skills: List[Skill]`

        - `class BetaManagedAgentsAnthropicSkill: …`

          A resolved Anthropic-managed skill.

        - `class BetaManagedAgentsCustomSkill: …`

          A resolved user-created custom skill.

      - `system: Optional[str]`

      - `tools: List[Tool]`

        - `class BetaManagedAgentsAgentToolset20260401: …`

        - `class BetaManagedAgentsMCPToolset: …`

        - `class BetaManagedAgentsCustomTool: …`

          A custom tool as returned in API responses.

      - `version: int`

        format: int32

    - `budget: Optional[BetaManagedAgentsBudgetLimit]`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `type: Literal["limit"]`

      - `max_list_cost: BetaMonetaryAmount`

        A monetary amount in a specific currency.

        - `amount: str`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `currency: BetaCurrency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `metadata: Optional[Dict[str, str]]`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title: Optional[str]`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsSystemMessageEvent: …`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `type: Literal["system.message"]`

    - `id: str`

      Unique identifier for this event.

    - `content: List[BetaManagedAgentsSystemContentBlock]`

      System content blocks. Text-only.

      - `type: Literal["text"]`

      - `text: str`

        The text content.

        minLength: 1

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionUsageEvent: …`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `type: Literal["session.usage"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `usage: BetaManagedAgentsSessionUsageSnapshot`

      Point-in-time snapshot of a session's cumulative usage.

      - `active_seconds: Optional[float]`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `cache_creation: Optional[BetaManagedAgentsCacheCreationUsage]`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `ephemeral_1h_input_tokens: Optional[int]`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `ephemeral_5m_input_tokens: Optional[int]`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `cache_read_input_tokens: Optional[int]`

        Total tokens read from prompt cache.

        format: int32

      - `input_tokens: Optional[int]`

        Total input tokens consumed across all turns.

        format: int32

      - `list_cost: Optional[BetaMonetaryAmount]`

        A monetary amount in a specific currency.

      - `output_tokens: Optional[int]`

        Total output tokens generated across all turns.

        format: int32

      - `server_tool_use: Optional[BetaManagedAgentsServerToolUsage]`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `web_fetch_requests: Optional[int]`

          Number of server-executed web fetch requests.

          format: int32

        - `web_search_requests: Optional[int]`

          Number of server-executed web search requests.

          format: int32

    - `budget: Optional[BetaManagedAgentsBudgetLimit]`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
page = client.beta.sessions.events.list(
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
)
page = page.data[0]
print(page)
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

`beta.sessions.events.send(session_id, **kwargs)  -> BetaManagedAgentsSendSessionEvents`

**POST** `/v1/sessions/{session_id}/events`

Send Events

#### Parameters

- `session_id: str`

- `events: Iterable[BetaManagedAgentsEventParams]`

  Events to send to the `session`.

  - `class BetaManagedAgentsUserMessageEventParams: …`

    Parameters for sending a user message to the session.

    - `type: Literal["user.message"]`

    - `content: Iterable[Content]`

      Array of content blocks for the user message.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

        - `type: Literal["text"]`

        - `text: str`

          The text content.

          minLength: 1

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

        - `type: Literal["image"]`

        - `source: Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource: …`

            Base64-encoded image data.

            - `type: Literal["base64"]`

            - `data: str`

              Base64-encoded image data.

              minLength: 1

            - `media_type: str`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

          - `class BetaManagedAgentsURLImageSource: …`

            Image referenced by URL.

            - `type: Literal["url"]`

            - `url: str`

              URL of the image to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileImageSource: …`

            Image referenced by file ID.

            - `type: Literal["file"]`

            - `file_id: str`

              ID of a previously uploaded file.

              minLength: 1

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `type: Literal["document"]`

        - `source: Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource: …`

            Base64-encoded document data.

            - `type: Literal["base64"]`

            - `data: str`

              Base64-encoded document data.

              minLength: 1

            - `media_type: str`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

          - `class BetaManagedAgentsPlainTextDocumentSource: …`

            Plain text document content.

            - `type: Literal["text"]`

            - `data: str`

              The plain text content.

              minLength: 1

            - `media_type: Literal["text/plain"]`

              MIME type of the text content. Must be "text/plain".

          - `class BetaManagedAgentsURLDocumentSource: …`

            Document referenced by URL.

            - `type: Literal["url"]`

            - `url: str`

              URL of the document to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileDocumentSource: …`

            Document referenced by file ID.

            - `type: Literal["file"]`

            - `file_id: str`

              ID of a previously uploaded file.

              minLength: 1

        - `context: Optional[str]`

          Additional context about the document for the model.

        - `title: Optional[str]`

          The title of the document.

      - `class BetaManagedAgentsRedactedBlock: …`

        Placeholder for content withheld by Anthropic model policy.

        - `type: Literal["redacted"]`

  - `class BetaManagedAgentsUserInterruptEventParams: …`

    Parameters for sending an interrupt to pause the agent.

    - `type: Literal["user.interrupt"]`

    - `session_thread_id: Optional[str]`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEventParams: …`

    Parameters for confirming or denying a tool execution request.

    - `type: Literal["user.tool_confirmation"]`

    - `result: Literal["allow", "deny"]`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: str`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      minLength: 1, maxLength: 128

    - `deny_message: Optional[str]`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

  - `class BetaManagedAgentsUserCustomToolResultEventParams: …`

    Parameters for providing the result of a custom tool execution.

    - `type: Literal["user.custom_tool_result"]`

    - `custom_tool_use_id: str`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      minLength: 1, maxLength: 128

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

        - `type: Literal["search_result"]`

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `enabled: bool`

            Whether citations are enabled for this search result.

        - `content: List[BetaManagedAgentsSearchResultContent]`

          Array of text content blocks from the search result.

          - `type: Literal["text"]`

          - `text: str`

            The text content.

            minLength: 1

        - `source: str`

          The URL source of the search result.

          minLength: 1

        - `title: str`

          The title of the search result.

          minLength: 1

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsUserDefineOutcomeEventParams: …`

    Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

    - `type: Literal["user.define_outcome"]`

    - `description: str`

      What the agent should produce. This is the task specification.

    - `rubric: Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubricParams: …`

        Rubric referenced by a file uploaded via the Files API.

        - `type: Literal["file"]`

        - `file_id: str`

          ID of the rubric file.

      - `class BetaManagedAgentsTextRubricParams: …`

        Rubric content provided inline as text.

        - `type: Literal["text"]`

        - `content: str`

          Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

          maxLength: 262144

    - `max_iterations: Optional[int]`

      Eval→revision cycles before giving up. Default 3, max 20.

      format: int32

  - `class BetaManagedAgentsUserToolResultEventParams: …`

    Parameters for providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `type: Literal["user.tool_result"]`

    - `tool_use_id: str`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      minLength: 1, maxLength: 128

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsSystemMessageEventParams: …`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

    - `type: Literal["system.message"]`

    - `content: List[BetaManagedAgentsSystemContentBlock]`

      System content blocks to append. Text-only.

      - `type: Literal["text"]`

      - `text: str`

        The text content.

        minLength: 1

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

- `workspace_id: Optional[str]`

#### Returns

- `class BetaManagedAgentsSendSessionEvents: …`

  Events that were successfully sent to the session.

  - `data: Optional[List[Data]]`

    Sent events

    - `class BetaManagedAgentsUserMessageEvent: …`

      A user message event in the session conversation.

      - `type: Literal["user.message"]`

      - `id: str`

        Unique identifier for this event.

      - `content: List[Content]`

        Array of content blocks comprising the user message.

        - `class BetaManagedAgentsTextBlock: …`

          Regular text content.

          - `type: Literal["text"]`

          - `text: str`

            The text content.

            minLength: 1

        - `class BetaManagedAgentsImageBlock: …`

          Image content specified directly as base64 data or as a reference via a URL.

          - `type: Literal["image"]`

          - `source: Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource: …`

              Base64-encoded image data.

              - `type: Literal["base64"]`

              - `data: str`

                Base64-encoded image data.

                minLength: 1

              - `media_type: str`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

            - `class BetaManagedAgentsURLImageSource: …`

              Image referenced by URL.

              - `type: Literal["url"]`

              - `url: str`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource: …`

              Image referenced by file ID.

              - `type: Literal["file"]`

              - `file_id: str`

                ID of a previously uploaded file.

                minLength: 1

        - `class BetaManagedAgentsDocumentBlock: …`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `type: Literal["document"]`

          - `source: Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource: …`

              Base64-encoded document data.

              - `type: Literal["base64"]`

              - `data: str`

                Base64-encoded document data.

                minLength: 1

              - `media_type: str`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

            - `class BetaManagedAgentsPlainTextDocumentSource: …`

              Plain text document content.

              - `type: Literal["text"]`

              - `data: str`

                The plain text content.

                minLength: 1

              - `media_type: Literal["text/plain"]`

                MIME type of the text content. Must be "text/plain".

            - `class BetaManagedAgentsURLDocumentSource: …`

              Document referenced by URL.

              - `type: Literal["url"]`

              - `url: str`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource: …`

              Document referenced by file ID.

              - `type: Literal["file"]`

              - `file_id: str`

                ID of a previously uploaded file.

                minLength: 1

          - `context: Optional[str]`

            Additional context about the document for the model.

          - `title: Optional[str]`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock: …`

          Placeholder for content withheld by Anthropic model policy.

          - `type: Literal["redacted"]`

      - `processed_at: Optional[datetime]`

        A timestamp in RFC 3339 format

        format: date-time

    - `class BetaManagedAgentsUserInterruptEvent: …`

      An interrupt event that pauses agent execution and returns control to the user.

      - `type: Literal["user.interrupt"]`

      - `id: str`

        Unique identifier for this event.

      - `processed_at: Optional[datetime]`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: Optional[str]`

        If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

    - `class BetaManagedAgentsUserToolConfirmationEvent: …`

      A tool confirmation event that approves or denies a pending tool execution.

      - `type: Literal["user.tool_confirmation"]`

      - `id: str`

        Unique identifier for this event.

      - `result: Literal["allow", "deny"]`

        UserToolConfirmationResult enum

        - `"allow"`

        - `"deny"`

      - `tool_use_id: str`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `deny_message: Optional[str]`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

        maxLength: 10000

      - `processed_at: Optional[datetime]`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: Optional[str]`

        When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

    - `class BetaManagedAgentsUserCustomToolResultEvent: …`

      Event sent by the client providing the result of a custom tool execution.

      - `type: Literal["user.custom_tool_result"]`

      - `id: str`

        Unique identifier for this event.

      - `custom_tool_use_id: str`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `content: Optional[List[Content]]`

        The result content returned by the tool.

        - `class BetaManagedAgentsTextBlock: …`

          Regular text content.

        - `class BetaManagedAgentsImageBlock: …`

          Image content specified directly as base64 data or as a reference via a URL.

        - `class BetaManagedAgentsDocumentBlock: …`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `class BetaManagedAgentsSearchResultBlock: …`

          A block containing a web search result.

          - `type: Literal["search_result"]`

          - `citations: BetaManagedAgentsSearchResultCitations`

            Citation settings for a search result.

            - `enabled: bool`

              Whether citations are enabled for this search result.

          - `content: List[BetaManagedAgentsSearchResultContent]`

            Array of text content blocks from the search result.

            - `type: Literal["text"]`

            - `text: str`

              The text content.

              minLength: 1

          - `source: str`

            The URL source of the search result.

            minLength: 1

          - `title: str`

            The title of the search result.

            minLength: 1

      - `is_error: Optional[bool]`

        Whether the tool execution resulted in an error.

      - `processed_at: Optional[datetime]`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: Optional[str]`

        Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

    - `class BetaManagedAgentsUserDefineOutcomeEvent: …`

      Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

      - `type: Literal["user.define_outcome"]`

      - `id: str`

        Unique identifier for this event.

      - `description: str`

        What the agent should produce. Copied from the input event.

      - `max_iterations: Optional[int]`

        Evaluate-then-revise cycles before giving up. Default 3, max 20.

        format: int32

      - `outcome_id: str`

        Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

      - `processed_at: datetime`

        A timestamp in RFC 3339 format

        format: date-time

      - `rubric: Rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric: …`

          Rubric referenced by a file uploaded via the Files API.

          - `type: Literal["file"]`

          - `file_id: str`

            ID of the rubric file.

        - `class BetaManagedAgentsTextRubric: …`

          Rubric content provided inline as text.

          - `type: Literal["text"]`

          - `content: str`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

    - `class BetaManagedAgentsUserToolResultEvent: …`

      Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

      - `type: Literal["user.tool_result"]`

      - `id: str`

        Unique identifier for this event.

      - `tool_use_id: str`

        The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `content: Optional[List[Content]]`

        The result content returned by the tool.

        - `class BetaManagedAgentsTextBlock: …`

          Regular text content.

        - `class BetaManagedAgentsImageBlock: …`

          Image content specified directly as base64 data or as a reference via a URL.

        - `class BetaManagedAgentsDocumentBlock: …`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `class BetaManagedAgentsSearchResultBlock: …`

          A block containing a web search result.

      - `is_error: Optional[bool]`

        Whether the tool execution resulted in an error.

      - `processed_at: Optional[datetime]`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: Optional[str]`

        Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

    - `class BetaManagedAgentsSystemMessageEvent: …`

      A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

      - `type: Literal["system.message"]`

      - `id: str`

        Unique identifier for this event.

      - `content: List[BetaManagedAgentsSystemContentBlock]`

        System content blocks. Text-only.

        - `type: Literal["text"]`

        - `text: str`

          The text content.

          minLength: 1

      - `processed_at: Optional[datetime]`

        A timestamp in RFC 3339 format

        format: date-time

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_managed_agents_send_session_events = client.beta.sessions.events.send(
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
    events=[
        {
            "content": [
                {
                    "text": "Where is my order #1234?",
                    "type": "text",
                }
            ],
            "type": "user.message",
        }
    ],
)
print(beta_managed_agents_send_session_events.data)
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

`beta.sessions.events.stream(session_id, **kwargs)  -> BetaManagedAgentsStreamSessionEvents`

**GET** `/v1/sessions/{session_id}/events/stream`

Stream Events

#### Parameters

- `session_id: str`

- `event_deltas: Optional[List[BetaManagedAgentsDeltaType]]`

  When set, this connection also receives streaming deltas (`event_start`, `event_delta`) while an event is being produced, before the event itself arrives. Deltas are best-effort; when the final event is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no final event — its terminal `span.model_request_end` closes the preview. Accepts one or more event types to preview and may be repeated: `agent.message` streams `content_delta` fragments; `agent.thinking` is start-only — a signal that the agent has begun extended thinking, concluded by the `agent.thinking` event itself. Only previews of the requested event types are sent.

  - `"agent.message"`

  - `"agent.thinking"`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

- `workspace_id: Optional[str]`

#### Returns

- `BetaManagedAgentsStreamSessionEvents`

  Server-sent event in the session stream.

  - `class BetaManagedAgentsUserMessageEvent: …`

    A user message event in the session conversation.

    - `type: Literal["user.message"]`

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

        - `type: Literal["text"]`

        - `text: str`

          The text content.

          minLength: 1

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

        - `type: Literal["image"]`

        - `source: Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource: …`

            Base64-encoded image data.

            - `type: Literal["base64"]`

            - `data: str`

              Base64-encoded image data.

              minLength: 1

            - `media_type: str`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

          - `class BetaManagedAgentsURLImageSource: …`

            Image referenced by URL.

            - `type: Literal["url"]`

            - `url: str`

              URL of the image to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileImageSource: …`

            Image referenced by file ID.

            - `type: Literal["file"]`

            - `file_id: str`

              ID of a previously uploaded file.

              minLength: 1

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `type: Literal["document"]`

        - `source: Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource: …`

            Base64-encoded document data.

            - `type: Literal["base64"]`

            - `data: str`

              Base64-encoded document data.

              minLength: 1

            - `media_type: str`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

          - `class BetaManagedAgentsPlainTextDocumentSource: …`

            Plain text document content.

            - `type: Literal["text"]`

            - `data: str`

              The plain text content.

              minLength: 1

            - `media_type: Literal["text/plain"]`

              MIME type of the text content. Must be "text/plain".

          - `class BetaManagedAgentsURLDocumentSource: …`

            Document referenced by URL.

            - `type: Literal["url"]`

            - `url: str`

              URL of the document to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileDocumentSource: …`

            Document referenced by file ID.

            - `type: Literal["file"]`

            - `file_id: str`

              ID of a previously uploaded file.

              minLength: 1

        - `context: Optional[str]`

          Additional context about the document for the model.

        - `title: Optional[str]`

          The title of the document.

      - `class BetaManagedAgentsRedactedBlock: …`

        Placeholder for content withheld by Anthropic model policy.

        - `type: Literal["redacted"]`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsUserInterruptEvent: …`

    An interrupt event that pauses agent execution and returns control to the user.

    - `type: Literal["user.interrupt"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: Optional[str]`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEvent: …`

    A tool confirmation event that approves or denies a pending tool execution.

    - `type: Literal["user.tool_confirmation"]`

    - `id: str`

      Unique identifier for this event.

    - `result: Literal["allow", "deny"]`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: str`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `deny_message: Optional[str]`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: Optional[str]`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `class BetaManagedAgentsUserCustomToolResultEvent: …`

    Event sent by the client providing the result of a custom tool execution.

    - `type: Literal["user.custom_tool_result"]`

    - `id: str`

      Unique identifier for this event.

    - `custom_tool_use_id: str`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

        - `type: Literal["search_result"]`

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `enabled: bool`

            Whether citations are enabled for this search result.

        - `content: List[BetaManagedAgentsSearchResultContent]`

          Array of text content blocks from the search result.

          - `type: Literal["text"]`

          - `text: str`

            The text content.

            minLength: 1

        - `source: str`

          The URL source of the search result.

          minLength: 1

        - `title: str`

          The title of the search result.

          minLength: 1

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: Optional[str]`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsAgentCustomToolUseEvent: …`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `type: Literal["agent.custom_tool_use"]`

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `name: str`

      Name of the custom tool being called.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `class BetaManagedAgentsAgentMessageEvent: …`

    An agent response event in the session conversation.

    - `type: Literal["agent.message"]`

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Array of text blocks comprising the agent response.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsRedactedBlock: …`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsAgentThinkingEvent: …`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `type: Literal["agent.thinking"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsAgentMCPToolUseEvent: …`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `type: Literal["agent.mcp_tool_use"]`

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `mcp_server_name: str`

      Name of the MCP server providing the tool.

    - `name: str`

      Name of the MCP tool being used.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `evaluated_permission: Optional[Literal["allow", "ask", "deny"]]`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `evaluation: Optional[BetaManagedAgentsAgentToolEvaluation]`

      Names the resolved permission_policy that produced evaluated_permission, and under auto carries the judgement. Open union: clients must tolerate unknown variants.

      - `class BetaManagedAgentsAgentToolEvaluationAlwaysAllow: …`

        The resolved permission_policy was always_allow; accompanies evaluated_permission "allow".

        - `type: Literal["always_allow"]`

      - `class BetaManagedAgentsAgentToolEvaluationAlwaysAsk: …`

        The resolved permission_policy was always_ask; accompanies evaluated_permission "ask".

        - `type: Literal["always_ask"]`

      - `class BetaManagedAgentsAgentToolEvaluationAuto: …`

        The resolved permission_policy was auto: the server judged this invocation individually.

        - `type: Literal["auto"]`

        - `evaluated_permission: BetaManagedAgentsAgentAutoEvaluatedPermission`

          The server's per-invocation judgement under the auto permission policy. Its type always equals the event's top-level evaluated_permission. Open union: clients must tolerate unknown variants.

          - `class BetaManagedAgentsAgentAutoEvaluatedPermissionAllow: …`

            The server judged the invocation safe to execute without client approval.

            - `type: Literal["allow"]`

          - `class BetaManagedAgentsAgentAutoEvaluatedPermissionAsk: …`

            The server reached no judgement; the invocation is held for client approval.

            - `type: Literal["ask"]`

            - `reason_code: str`

              The judgement's grounds in registry-bound terms, for client branching and audit rather than end-user display. Open registry; currently "indeterminate" (no judgement was reached). Clients must tolerate values outside this set.

              maxLength: 64

          - `class BetaManagedAgentsAgentAutoEvaluatedPermissionDeny: …`

            The server judged the invocation high-risk; it does not execute and a synthetic error tool result is appended.

            - `type: Literal["deny"]`

            - `reason_code: str`

              The judgement's grounds in registry-bound terms. Open registry; currently "high_risk" (judged high-risk; the call does not run). Clients must tolerate values outside this set.

              maxLength: 64

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentMCPToolResultEvent: …`

    Event representing the result of an MCP tool execution.

    - `type: Literal["agent.mcp_tool_result"]`

    - `id: str`

      Unique identifier for this event.

    - `mcp_tool_use_id: str`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent: …`

    Event emitted when the agent invokes a built-in agent tool.

    - `type: Literal["agent.tool_use"]`

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `name: str`

      Name of the agent tool being used.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `evaluated_permission: Optional[Literal["allow", "ask", "deny"]]`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `evaluation: Optional[BetaManagedAgentsAgentToolEvaluation]`

      Names the resolved permission_policy that produced evaluated_permission, and under auto carries the judgement. Open union: clients must tolerate unknown variants.

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentToolResultEvent: …`

    Event representing the result of an agent tool execution.

    - `type: Literal["agent.tool_result"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `tool_use_id: str`

      The id of the `agent.tool_use` event this result corresponds to.

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadMessageReceivedEvent: …`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `type: Literal["agent.thread_message_received"]`

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock: …`

        Placeholder for content withheld by Anthropic model policy.

    - `from_session_thread_id: str`

      Public `sthr_` ID of the thread that sent the message.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `from_agent_name: Optional[str]`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class BetaManagedAgentsAgentThreadMessageSentEvent: …`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `type: Literal["agent.thread_message_sent"]`

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock: …`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `to_session_thread_id: str`

      Public `sthr_` ID of the thread the message was sent to.

    - `to_agent_name: Optional[str]`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent: …`

    Indicates that context compaction (summarization) occurred during the session.

    - `type: Literal["agent.thread_context_compacted"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionErrorEvent: …`

    An error event indicating a problem occurred during session execution.

    - `type: Literal["session.error"]`

    - `id: str`

      Unique identifier for this event.

    - `error: Error`

      - `class BetaManagedAgentsUnknownError: …`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `type: Literal["unknown_error"]`

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: Literal["retrying"]`

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: Literal["exhausted"]`

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: Literal["terminal"]`

      - `class BetaManagedAgentsModelOverloadedError: …`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `type: Literal["model_overloaded_error"]`

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

      - `class BetaManagedAgentsModelRateLimitedError: …`

        The model request was rate-limited.

        - `type: Literal["model_rate_limited_error"]`

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

      - `class BetaManagedAgentsModelRequestFailedError: …`

        A model request failed for a reason other than overload or rate-limiting.

        - `type: Literal["model_request_failed_error"]`

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

      - `class BetaManagedAgentsMCPConnectionFailedError: …`

        Failed to connect to an MCP server.

        - `type: Literal["mcp_connection_failed_error"]`

        - `mcp_server_name: str`

          Name of the MCP server that failed to connect.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

      - `class BetaManagedAgentsMCPAuthenticationFailedError: …`

        Authentication to an MCP server failed.

        - `type: Literal["mcp_authentication_failed_error"]`

        - `mcp_server_name: str`

          Name of the MCP server that failed authentication.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

      - `class BetaManagedAgentsBillingError: …`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `type: Literal["billing_error"]`

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

      - `class BetaManagedAgentsCredentialHostUnreachableError: …`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `type: Literal["credential_host_unreachable_error"]`

        - `credential_id: str`

          ID of the affected credential.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `vault_id: str`

          ID of the vault containing the affected credential.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionStatusRescheduledEvent: …`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `type: Literal["session.status_rescheduled"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionStatusRunningEvent: …`

    Indicates the session is actively running and the agent is working.

    - `type: Literal["session.status_running"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionStatusIdleEvent: …`

    Indicates the agent has paused and is awaiting user input.

    - `type: Literal["session.status_idle"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `stop_reason: StopReason`

      - `class BetaManagedAgentsSessionEndTurn: …`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: Literal["end_turn"]`

      - `class BetaManagedAgentsSessionRequiresAction: …`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `type: Literal["requires_action"]`

        - `event_ids: List[str]`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

      - `class BetaManagedAgentsSessionRetriesExhausted: …`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `type: Literal["retries_exhausted"]`

      - `class BetaManagedAgentsSessionBudgetReached: …`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `type: Literal["budget_reached"]`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent: …`

    Indicates the session has terminated, either due to an error or completion.

    - `type: Literal["session.status_terminated"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionThreadCreatedEvent: …`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `type: Literal["session.thread_created"]`

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the callable agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: str`

      Public `sthr_` ID of the newly created thread.

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent: …`

    Emitted when an outcome evaluation cycle begins.

    - `type: Literal["span.outcome_evaluation_start"]`

    - `id: str`

      Unique identifier for this event.

    - `iteration: int`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

      format: int32

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent: …`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `type: Literal["span.outcome_evaluation_end"]`

    - `id: str`

      Unique identifier for this event.

    - `explanation: str`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `iteration: int`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `outcome_evaluation_start_id: str`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `result: str`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `cache_creation_input_tokens: int`

        Tokens used to create prompt cache in this request.

        format: int32

      - `cache_read_input_tokens: int`

        Tokens read from prompt cache in this request.

        format: int32

      - `input_tokens: int`

        Input tokens consumed by this request.

        format: int32

      - `output_tokens: int`

        Output tokens generated by this request.

        format: int32

      - `speed: Optional[Literal["standard", "fast"]]`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `class BetaManagedAgentsSpanModelRequestStartEvent: …`

    Emitted when a model request is initiated by the agent.

    - `type: Literal["span.model_request_start"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSpanModelRequestEndEvent: …`

    Emitted when a model request completes.

    - `type: Literal["span.model_request_end"]`

    - `id: str`

      Unique identifier for this event.

    - `is_error: Optional[bool]`

      Whether the model request resulted in an error.

    - `model_request_start_id: str`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent: …`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `type: Literal["span.outcome_evaluation_ongoing"]`

    - `id: str`

      Unique identifier for this event.

    - `iteration: int`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsUserDefineOutcomeEvent: …`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `type: Literal["user.define_outcome"]`

    - `id: str`

      Unique identifier for this event.

    - `description: str`

      What the agent should produce. Copied from the input event.

    - `max_iterations: Optional[int]`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

      format: int32

    - `outcome_id: str`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `rubric: Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric: …`

        Rubric referenced by a file uploaded via the Files API.

        - `type: Literal["file"]`

        - `file_id: str`

          ID of the rubric file.

      - `class BetaManagedAgentsTextRubric: …`

        Rubric content provided inline as text.

        - `type: Literal["text"]`

        - `content: str`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

  - `class BetaManagedAgentsSessionDeletedEvent: …`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `type: Literal["session.deleted"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent: …`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: Literal["session.thread_status_running"]`

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: str`

      Public sthr_ ID of the thread that started running.

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent: …`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: Literal["session.thread_status_idle"]`

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: str`

      Public sthr_ ID of the thread that went idle.

    - `stop_reason: StopReason`

      - `class BetaManagedAgentsSessionEndTurn: …`

        The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionRequiresAction: …`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `class BetaManagedAgentsSessionRetriesExhausted: …`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `class BetaManagedAgentsSessionBudgetReached: …`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent: …`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: Literal["session.thread_status_terminated"]`

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: str`

      Public sthr_ ID of the thread that terminated.

  - `class BetaManagedAgentsUserToolResultEvent: …`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `type: Literal["user.tool_result"]`

    - `id: str`

      Unique identifier for this event.

    - `tool_use_id: str`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: Optional[str]`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent: …`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: Literal["session.thread_status_rescheduled"]`

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: str`

      Public sthr_ ID of the thread that is retrying.

  - `class BetaManagedAgentsSessionUpdatedEvent: …`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `type: Literal["session.updated"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `agent: Optional[BetaManagedAgentsSessionAgent]`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `type: Literal["agent"]`

      - `id: str`

      - `description: Optional[str]`

      - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

        - `type: Literal["url"]`

        - `name: str`

        - `url: str`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `Literal["claude-fable-5-1", "claude-sonnet-5", "claude-fable-5", 11 more]`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `claude-fable-5-1` - Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows
            - `claude-sonnet-5` - High-performance model for coding and agents
            - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
            - `claude-opus-5` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-8` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-7` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-6` - Powerful intelligence for long-running agents and coding
            - `claude-sonnet-4-6` - Best combination of speed and intelligence
            - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
            - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
            - `claude-opus-4-5` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-5-20251101` - Powerful intelligence for long-running agents and coding
            - `claude-sonnet-4-5` - High-performance model for agents and coding
            - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

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

          - `str`

        - `effort: Optional[Effort]`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow: …`

            Low effort. Favors latency over reasoning depth.

            - `type: Literal["low"]`

          - `class BetaManagedAgentsEffortMedium: …`

            Medium effort. Balances latency and reasoning depth.

            - `type: Literal["medium"]`

          - `class BetaManagedAgentsEffortHigh: …`

            High effort. Favors reasoning depth.

            - `type: Literal["high"]`

          - `class BetaManagedAgentsEffortXhigh: …`

            Extra-high effort. Not all models accept this level.

            - `type: Literal["xhigh"]`

          - `class BetaManagedAgentsEffortMax: …`

            Maximum effort. Favors reasoning depth over latency.

            - `type: Literal["max"]`

        - `inference_geo: Optional[str]`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `speed: Optional[Literal["standard", "fast"]]`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

      - `multiagent: Optional[BetaManagedAgentsSessionMultiagentCoordinator]`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `type: Literal["coordinator"]`

        - `agents: List[Agent]`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `class BetaManagedAgentsSessionThreadAgent: …`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `type: Literal["agent"]`

            - `id: str`

            - `description: Optional[str]`

            - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

              - `type: Literal["url"]`

              - `name: str`

              - `url: str`

            - `model: BetaManagedAgentsModelConfig`

              Model identifier and configuration.

            - `name: str`

            - `skills: List[Skill]`

              - `class BetaManagedAgentsAnthropicSkill: …`

                A resolved Anthropic-managed skill.

                - `type: Literal["anthropic"]`

                - `skill_id: str`

                - `version: str`

              - `class BetaManagedAgentsCustomSkill: …`

                A resolved user-created custom skill.

                - `type: Literal["custom"]`

                - `skill_id: str`

                - `version: str`

            - `system: Optional[str]`

            - `tools: List[Tool]`

              - `class BetaManagedAgentsAgentToolset20260401: …`

                - `type: Literal["agent_toolset_20260401"]`

                - `configs: List[BetaManagedAgentsAgentToolConfig]`

                  - `class BetaManagedAgentsBashToolConfig: …`

                    Configuration for the bash tool.

                    - `type: Literal["bash"]`

                    - `enabled: bool`

                    - `name: Literal["bash"]`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                        - `type: Literal["always_allow"]`

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                        - `type: Literal["always_ask"]`

                      - `class BetaManagedAgentsAutoPolicy: …`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                        - `type: Literal["auto"]`

                  - `class BetaManagedAgentsEditToolConfig: …`

                    Configuration for the edit tool.

                    - `type: Literal["edit"]`

                    - `enabled: bool`

                    - `name: Literal["edit"]`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                      - `class BetaManagedAgentsAutoPolicy: …`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `class BetaManagedAgentsReadToolConfig: …`

                    Configuration for the read tool.

                    - `type: Literal["read"]`

                    - `enabled: bool`

                    - `name: Literal["read"]`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                      - `class BetaManagedAgentsAutoPolicy: …`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `class BetaManagedAgentsWriteToolConfig: …`

                    Configuration for the write tool.

                    - `type: Literal["write"]`

                    - `enabled: bool`

                    - `name: Literal["write"]`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                      - `class BetaManagedAgentsAutoPolicy: …`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `class BetaManagedAgentsGlobToolConfig: …`

                    Configuration for the glob tool.

                    - `type: Literal["glob"]`

                    - `enabled: bool`

                    - `name: Literal["glob"]`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                      - `class BetaManagedAgentsAutoPolicy: …`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `class BetaManagedAgentsGrepToolConfig: …`

                    Configuration for the grep tool.

                    - `type: Literal["grep"]`

                    - `enabled: bool`

                    - `name: Literal["grep"]`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                      - `class BetaManagedAgentsAutoPolicy: …`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `class BetaManagedAgentsWebFetchToolConfig: …`

                    Configuration for the web_fetch tool.

                    - `type: Literal["web_fetch"]`

                    - `enabled: bool`

                    - `name: Literal["web_fetch"]`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                      - `class BetaManagedAgentsAutoPolicy: …`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `allowed_domains: Optional[List[str]]`

                    - `blocked_domains: Optional[List[str]]`

                    - `max_content_tokens: Optional[int]`

                      format: int32

                  - `class BetaManagedAgentsWebSearchToolConfig: …`

                    Configuration for the web_search tool.

                    - `type: Literal["web_search"]`

                    - `enabled: bool`

                    - `name: Literal["web_search"]`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                      - `class BetaManagedAgentsAutoPolicy: …`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `allowed_domains: Optional[List[str]]`

                    - `blocked_domains: Optional[List[str]]`

                    - `user_location: Optional[BetaManagedAgentsUserLocation]`

                      Approximate user location for search result localization.

                      - `type: Literal["approximate"]`

                        Location precision. Only "approximate" is supported.

                      - `city: Optional[str]`

                        City name.

                        minLength: 1, maxLength: 255

                      - `country: Optional[str]`

                        Two-letter ISO 3166-1 country code, uppercase.

                      - `region: Optional[str]`

                        Region or state name.

                        minLength: 1, maxLength: 255

                      - `timezone: Optional[str]`

                        IANA timezone identifier, e.g. "America/Los_Angeles".

                        minLength: 1, maxLength: 255

                - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

                  Resolved default configuration for agent tools.

                  - `enabled: bool`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `class BetaManagedAgentsMCPToolset: …`

                - `type: Literal["mcp_toolset"]`

                - `configs: List[BetaManagedAgentsMCPToolConfig]`

                  - `enabled: bool`

                  - `name: str`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `enabled: bool`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `mcp_server_name: str`

              - `class BetaManagedAgentsCustomTool: …`

                A custom tool as returned in API responses.

                - `type: Literal["custom"]`

                - `description: str`

                - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                  JSON Schema for custom tool input parameters.

                  - `type: Literal["object"]`

                  - `properties: Optional[Dict[str, object]]`

                  - `required: Optional[List[str]]`

                - `name: str`

            - `version: int`

              format: int32

          - `class BetaManagedAgentsAdvisor: …`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `type: Literal["advisor"]`

            - `model: str`

              The advisor model id.

      - `name: str`

      - `skills: List[Skill]`

        - `class BetaManagedAgentsAnthropicSkill: …`

          A resolved Anthropic-managed skill.

        - `class BetaManagedAgentsCustomSkill: …`

          A resolved user-created custom skill.

      - `system: Optional[str]`

      - `tools: List[Tool]`

        - `class BetaManagedAgentsAgentToolset20260401: …`

        - `class BetaManagedAgentsMCPToolset: …`

        - `class BetaManagedAgentsCustomTool: …`

          A custom tool as returned in API responses.

      - `version: int`

        format: int32

    - `budget: Optional[BetaManagedAgentsBudgetLimit]`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `type: Literal["limit"]`

      - `max_list_cost: BetaMonetaryAmount`

        A monetary amount in a specific currency.

        - `amount: str`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `currency: BetaCurrency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `metadata: Optional[Dict[str, str]]`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title: Optional[str]`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsStartEvent: …`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `type: Literal["event_start"]`

    - `event: BetaManagedAgentsStartEventPreview`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

      - `class BetaManagedAgentsAgentMessagePreview: …`

        - `type: Literal["agent.message"]`

        - `id: str`

          The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

      - `class BetaManagedAgentsAgentThinkingPreview: …`

        - `type: Literal["agent.thinking"]`

        - `id: str`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

  - `class BetaManagedAgentsDeltaEvent: …`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `type: Literal["event_delta"]`

    - `delta: BetaManagedAgentsDeltaContent`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `type: Literal["content_delta"]`

      - `content: BetaManagedAgentsTextBlock`

        Regular text content.

      - `index: Optional[int]`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

        format: uint32

    - `event_id: str`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

  - `class BetaManagedAgentsSystemMessageEvent: …`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `type: Literal["system.message"]`

    - `id: str`

      Unique identifier for this event.

    - `content: List[BetaManagedAgentsSystemContentBlock]`

      System content blocks. Text-only.

      - `type: Literal["text"]`

      - `text: str`

        The text content.

        minLength: 1

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionUsageEvent: …`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `type: Literal["session.usage"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `usage: BetaManagedAgentsSessionUsageSnapshot`

      Point-in-time snapshot of a session's cumulative usage.

      - `active_seconds: Optional[float]`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `cache_creation: Optional[BetaManagedAgentsCacheCreationUsage]`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `ephemeral_1h_input_tokens: Optional[int]`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `ephemeral_5m_input_tokens: Optional[int]`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `cache_read_input_tokens: Optional[int]`

        Total tokens read from prompt cache.

        format: int32

      - `input_tokens: Optional[int]`

        Total input tokens consumed across all turns.

        format: int32

      - `list_cost: Optional[BetaMonetaryAmount]`

        A monetary amount in a specific currency.

      - `output_tokens: Optional[int]`

        Total output tokens generated across all turns.

        format: int32

      - `server_tool_use: Optional[BetaManagedAgentsServerToolUsage]`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `web_fetch_requests: Optional[int]`

          Number of server-executed web fetch requests.

          format: int32

        - `web_search_requests: Optional[int]`

          Number of server-executed web search requests.

          format: int32

    - `budget: Optional[BetaManagedAgentsBudgetLimit]`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
for event in client.beta.sessions.events.stream(
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
):
    print(event)
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

`beta.sessions.resources.add(session_id, **kwargs)  -> BetaManagedAgentsFileResource`

**POST** `/v1/sessions/{session_id}/resources`

Add Session Resource

#### Parameters

- `session_id: str`

- `file_id: str`

  ID of a previously uploaded file.

  minLength: 1, maxLength: 128

- `type: Literal["file"]`

- `mount_path: Optional[str]`

  Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

  minLength: 1, maxLength: 4096

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

- `workspace_id: Optional[str]`

#### Returns

- `class BetaManagedAgentsFileResource: …`

  - `type: Literal["file"]`

  - `id: str`

  - `created_at: datetime`

    A timestamp in RFC 3339 format

    format: date-time

  - `file_id: str`

  - `mount_path: str`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

    format: date-time

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_managed_agents_file_resource = client.beta.sessions.resources.add(
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
    file_id="file_011CNha8iCJcU1wXNR6q4V8w",
    type="file",
)
print(beta_managed_agents_file_resource.id)
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

`beta.sessions.resources.list(session_id, **kwargs)  -> SyncPageCursor[BetaManagedAgentsSessionResource]`

**GET** `/v1/sessions/{session_id}/resources`

List Session Resources

#### Parameters

- `session_id: str`

- `limit: Optional[int]`

  Maximum number of resources to return per page (max 1000). If omitted, returns all resources.

  format: int32

- `page: Optional[str]`

  Opaque cursor from a previous response's `next_page` field.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

- `workspace_id: Optional[str]`

#### Returns

- `BetaManagedAgentsSessionResource`

  - `class BetaManagedAgentsGitHubRepositoryResource: …`

    - `type: Literal["github_repository"]`

    - `id: str`

    - `created_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `mount_path: str`

    - `updated_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `url: str`

    - `checkout: Optional[Checkout]`

      - `class BetaManagedAgentsBranchCheckout: …`

        - `type: Literal["branch"]`

        - `name: str`

          Branch name to check out.

          minLength: 1, maxLength: 255

      - `class BetaManagedAgentsCommitCheckout: …`

        - `type: Literal["commit"]`

        - `sha: str`

          Full commit SHA to check out.

          minLength: 7, maxLength: 64

  - `class BetaManagedAgentsFileResource: …`

    - `type: Literal["file"]`

    - `id: str`

    - `created_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `file_id: str`

    - `mount_path: str`

    - `updated_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsMemoryStoreResource: …`

    A memory store attached to an agent session.

    - `type: Literal["memory_store"]`

    - `memory_store_id: str`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `access: Optional[Literal["read_write", "read_only"]]`

      Access mode for an attached memory store.

      - `"read_write"`

      - `"read_only"`

    - `description: Optional[str]`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `instructions: Optional[str]`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      maxLength: 4096

    - `mount_path: Optional[str]`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `name: Optional[str]`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
page = client.beta.sessions.resources.list(
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
)
page = page.data[0]
print(page)
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

`beta.sessions.resources.retrieve(resource_id, **kwargs)  -> ResourceRetrieveResponse`

**GET** `/v1/sessions/{session_id}/resources/{resource_id}`

Get Session Resource

#### Parameters

- `session_id: str`

- `resource_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

- `workspace_id: Optional[str]`

#### Returns

- `ResourceRetrieveResponse`

  The requested session resource.

  - `class BetaManagedAgentsGitHubRepositoryResource: …`

    - `type: Literal["github_repository"]`

    - `id: str`

    - `created_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `mount_path: str`

    - `updated_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `url: str`

    - `checkout: Optional[Checkout]`

      - `class BetaManagedAgentsBranchCheckout: …`

        - `type: Literal["branch"]`

        - `name: str`

          Branch name to check out.

          minLength: 1, maxLength: 255

      - `class BetaManagedAgentsCommitCheckout: …`

        - `type: Literal["commit"]`

        - `sha: str`

          Full commit SHA to check out.

          minLength: 7, maxLength: 64

  - `class BetaManagedAgentsFileResource: …`

    - `type: Literal["file"]`

    - `id: str`

    - `created_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `file_id: str`

    - `mount_path: str`

    - `updated_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsMemoryStoreResource: …`

    A memory store attached to an agent session.

    - `type: Literal["memory_store"]`

    - `memory_store_id: str`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `access: Optional[Literal["read_write", "read_only"]]`

      Access mode for an attached memory store.

      - `"read_write"`

      - `"read_only"`

    - `description: Optional[str]`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `instructions: Optional[str]`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      maxLength: 4096

    - `mount_path: Optional[str]`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `name: Optional[str]`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
resource = client.beta.sessions.resources.retrieve(
    resource_id="sesrsc_011CZkZBJq5dWxk9fVLNcPht",
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
)
print(resource)
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

`beta.sessions.resources.update(resource_id, **kwargs)  -> ResourceUpdateResponse`

**POST** `/v1/sessions/{session_id}/resources/{resource_id}`

Update Session Resource

#### Parameters

- `session_id: str`

- `resource_id: str`

- `authorization_token: str`

  New authorization token for the resource. Currently only `github_repository` resources support token rotation.

  minLength: 1, maxLength: 4096

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

- `workspace_id: Optional[str]`

#### Returns

- `ResourceUpdateResponse`

  The updated session resource.

  - `class BetaManagedAgentsGitHubRepositoryResource: …`

    - `type: Literal["github_repository"]`

    - `id: str`

    - `created_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `mount_path: str`

    - `updated_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `url: str`

    - `checkout: Optional[Checkout]`

      - `class BetaManagedAgentsBranchCheckout: …`

        - `type: Literal["branch"]`

        - `name: str`

          Branch name to check out.

          minLength: 1, maxLength: 255

      - `class BetaManagedAgentsCommitCheckout: …`

        - `type: Literal["commit"]`

        - `sha: str`

          Full commit SHA to check out.

          minLength: 7, maxLength: 64

  - `class BetaManagedAgentsFileResource: …`

    - `type: Literal["file"]`

    - `id: str`

    - `created_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `file_id: str`

    - `mount_path: str`

    - `updated_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsMemoryStoreResource: …`

    A memory store attached to an agent session.

    - `type: Literal["memory_store"]`

    - `memory_store_id: str`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `access: Optional[Literal["read_write", "read_only"]]`

      Access mode for an attached memory store.

      - `"read_write"`

      - `"read_only"`

    - `description: Optional[str]`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `instructions: Optional[str]`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      maxLength: 4096

    - `mount_path: Optional[str]`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `name: Optional[str]`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
resource = client.beta.sessions.resources.update(
    resource_id="sesrsc_011CZkZBJq5dWxk9fVLNcPht",
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
    authorization_token="ghp_exampletoken",
)
print(resource)
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

`beta.sessions.resources.delete(resource_id, **kwargs)  -> BetaManagedAgentsDeleteSessionResource`

**DELETE** `/v1/sessions/{session_id}/resources/{resource_id}`

Delete Session Resource

#### Parameters

- `session_id: str`

- `resource_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

- `workspace_id: Optional[str]`

#### Returns

- `class BetaManagedAgentsDeleteSessionResource: …`

  Confirmation of resource deletion.

  - `type: Literal["session_resource_deleted"]`

  - `id: str`

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_managed_agents_delete_session_resource = client.beta.sessions.resources.delete(
    resource_id="sesrsc_011CZkZBJq5dWxk9fVLNcPht",
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
)
print(beta_managed_agents_delete_session_resource.id)
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

`beta.sessions.threads.list(session_id, **kwargs)  -> SyncPageCursor[BetaManagedAgentsSessionThread]`

**GET** `/v1/sessions/{session_id}/threads`

List Session Threads

#### Parameters

- `session_id: str`

- `limit: Optional[int]`

  Maximum results per page. Defaults to 1000.

  format: int32

- `page: Optional[str]`

  Opaque pagination cursor from a previous response's `next_page`. Forward-only.

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

- `workspace_id: Optional[str]`

#### Returns

- `class BetaManagedAgentsSessionThread: …`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `type: Literal["session_thread"]`

  - `id: str`

    Unique identifier for this thread.

  - `agent: Agent`

    The resolved agent a session thread runs: a saved-agent snapshot, the platform advisor entry, or an inline-defined (ephemeral) agent snapshot.

    - `class BetaManagedAgentsSessionThreadAgent: …`

      Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

      - `type: Literal["agent"]`

      - `id: str`

      - `description: Optional[str]`

      - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

        - `type: Literal["url"]`

        - `name: str`

        - `url: str`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `Literal["claude-fable-5-1", "claude-sonnet-5", "claude-fable-5", 11 more]`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `claude-fable-5-1` - Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows
            - `claude-sonnet-5` - High-performance model for coding and agents
            - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
            - `claude-opus-5` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-8` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-7` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-6` - Powerful intelligence for long-running agents and coding
            - `claude-sonnet-4-6` - Best combination of speed and intelligence
            - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
            - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
            - `claude-opus-4-5` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-5-20251101` - Powerful intelligence for long-running agents and coding
            - `claude-sonnet-4-5` - High-performance model for agents and coding
            - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

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

          - `str`

        - `effort: Optional[Effort]`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow: …`

            Low effort. Favors latency over reasoning depth.

            - `type: Literal["low"]`

          - `class BetaManagedAgentsEffortMedium: …`

            Medium effort. Balances latency and reasoning depth.

            - `type: Literal["medium"]`

          - `class BetaManagedAgentsEffortHigh: …`

            High effort. Favors reasoning depth.

            - `type: Literal["high"]`

          - `class BetaManagedAgentsEffortXhigh: …`

            Extra-high effort. Not all models accept this level.

            - `type: Literal["xhigh"]`

          - `class BetaManagedAgentsEffortMax: …`

            Maximum effort. Favors reasoning depth over latency.

            - `type: Literal["max"]`

        - `inference_geo: Optional[str]`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `speed: Optional[Literal["standard", "fast"]]`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

      - `name: str`

      - `skills: List[Skill]`

        - `class BetaManagedAgentsAnthropicSkill: …`

          A resolved Anthropic-managed skill.

          - `type: Literal["anthropic"]`

          - `skill_id: str`

          - `version: str`

        - `class BetaManagedAgentsCustomSkill: …`

          A resolved user-created custom skill.

          - `type: Literal["custom"]`

          - `skill_id: str`

          - `version: str`

      - `system: Optional[str]`

      - `tools: List[Tool]`

        - `class BetaManagedAgentsAgentToolset20260401: …`

          - `type: Literal["agent_toolset_20260401"]`

          - `configs: List[BetaManagedAgentsAgentToolConfig]`

            - `class BetaManagedAgentsBashToolConfig: …`

              Configuration for the bash tool.

              - `type: Literal["bash"]`

              - `enabled: bool`

              - `name: Literal["bash"]`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                  - `type: Literal["always_allow"]`

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

                  - `type: Literal["always_ask"]`

                - `class BetaManagedAgentsAutoPolicy: …`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `type: Literal["auto"]`

            - `class BetaManagedAgentsEditToolConfig: …`

              Configuration for the edit tool.

              - `type: Literal["edit"]`

              - `enabled: bool`

              - `name: Literal["edit"]`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

                - `class BetaManagedAgentsAutoPolicy: …`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `class BetaManagedAgentsReadToolConfig: …`

              Configuration for the read tool.

              - `type: Literal["read"]`

              - `enabled: bool`

              - `name: Literal["read"]`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

                - `class BetaManagedAgentsAutoPolicy: …`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `class BetaManagedAgentsWriteToolConfig: …`

              Configuration for the write tool.

              - `type: Literal["write"]`

              - `enabled: bool`

              - `name: Literal["write"]`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

                - `class BetaManagedAgentsAutoPolicy: …`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `class BetaManagedAgentsGlobToolConfig: …`

              Configuration for the glob tool.

              - `type: Literal["glob"]`

              - `enabled: bool`

              - `name: Literal["glob"]`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

                - `class BetaManagedAgentsAutoPolicy: …`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `class BetaManagedAgentsGrepToolConfig: …`

              Configuration for the grep tool.

              - `type: Literal["grep"]`

              - `enabled: bool`

              - `name: Literal["grep"]`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

                - `class BetaManagedAgentsAutoPolicy: …`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `class BetaManagedAgentsWebFetchToolConfig: …`

              Configuration for the web_fetch tool.

              - `type: Literal["web_fetch"]`

              - `enabled: bool`

              - `name: Literal["web_fetch"]`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

                - `class BetaManagedAgentsAutoPolicy: …`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `allowed_domains: Optional[List[str]]`

              - `blocked_domains: Optional[List[str]]`

              - `max_content_tokens: Optional[int]`

                format: int32

            - `class BetaManagedAgentsWebSearchToolConfig: …`

              Configuration for the web_search tool.

              - `type: Literal["web_search"]`

              - `enabled: bool`

              - `name: Literal["web_search"]`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

                - `class BetaManagedAgentsAutoPolicy: …`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `allowed_domains: Optional[List[str]]`

              - `blocked_domains: Optional[List[str]]`

              - `user_location: Optional[BetaManagedAgentsUserLocation]`

                Approximate user location for search result localization.

                - `type: Literal["approximate"]`

                  Location precision. Only "approximate" is supported.

                - `city: Optional[str]`

                  City name.

                  minLength: 1, maxLength: 255

                - `country: Optional[str]`

                  Two-letter ISO 3166-1 country code, uppercase.

                - `region: Optional[str]`

                  Region or state name.

                  minLength: 1, maxLength: 255

                - `timezone: Optional[str]`

                  IANA timezone identifier, e.g. "America/Los_Angeles".

                  minLength: 1, maxLength: 255

          - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

            Resolved default configuration for agent tools.

            - `enabled: bool`

            - `permission_policy: PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy: …`

                Tool calls require user confirmation before execution.

              - `class BetaManagedAgentsAutoPolicy: …`

                The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

        - `class BetaManagedAgentsMCPToolset: …`

          - `type: Literal["mcp_toolset"]`

          - `configs: List[BetaManagedAgentsMCPToolConfig]`

            - `enabled: bool`

            - `name: str`

            - `permission_policy: PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy: …`

                Tool calls require user confirmation before execution.

              - `class BetaManagedAgentsAutoPolicy: …`

                The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

          - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

            Resolved default configuration for all tools from an MCP server.

            - `enabled: bool`

            - `permission_policy: PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy: …`

                Tool calls require user confirmation before execution.

              - `class BetaManagedAgentsAutoPolicy: …`

                The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

          - `mcp_server_name: str`

        - `class BetaManagedAgentsCustomTool: …`

          A custom tool as returned in API responses.

          - `type: Literal["custom"]`

          - `description: str`

          - `input_schema: BetaManagedAgentsCustomToolInputSchema`

            JSON Schema for custom tool input parameters.

            - `type: Literal["object"]`

            - `properties: Optional[Dict[str, object]]`

            - `required: Optional[List[str]]`

          - `name: str`

      - `version: int`

        format: int32

    - `class BetaManagedAgentsAdvisor: …`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `type: Literal["advisor"]`

      - `model: str`

        The advisor model id.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: datetime`

    A timestamp in RFC 3339 format

    format: date-time

  - `parent_thread_id: Optional[str]`

    Parent thread that spawned this thread. Null for the primary thread.

  - `session_id: str`

    The session this thread belongs to.

  - `stats: Optional[BetaManagedAgentsSessionThreadStats]`

    Timing statistics for a session thread.

    - `active_seconds: Optional[float]`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

      format: double

    - `duration_seconds: Optional[float]`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

      format: double

    - `startup_seconds: Optional[float]`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

      format: double

  - `status: BetaManagedAgentsSessionThreadStatus`

    SessionThreadStatus enum

    - `"running"`

    - `"idle"`

    - `"rescheduling"`

    - `"terminated"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

    format: date-time

  - `usage: Optional[BetaManagedAgentsSessionThreadUsage]`

    Cumulative token usage for a session thread across all turns.

    - `active_seconds: Optional[float]`

      Cumulative time in seconds this thread spent in running status. Equal to `stats.active_seconds`; surfaced here so a thread's usage carries every quantity its cost is priced on.

      format: double

    - `cache_creation: Optional[BetaManagedAgentsCacheCreationUsage]`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: Optional[int]`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `ephemeral_5m_input_tokens: Optional[int]`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `cache_read_input_tokens: Optional[int]`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens: Optional[int]`

      Total input tokens consumed across all turns.

      format: int32

    - `list_cost: Optional[BetaMonetaryAmount]`

      A monetary amount in a specific currency.

      - `amount: str`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `output_tokens: Optional[int]`

      Total output tokens generated across all turns.

      format: int32

    - `server_tool_use: Optional[BetaManagedAgentsServerToolUsage]`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `web_fetch_requests: Optional[int]`

        Number of server-executed web fetch requests.

        format: int32

      - `web_search_requests: Optional[int]`

        Number of server-executed web search requests.

        format: int32

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
page = client.beta.sessions.threads.list(
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
)
page = page.data[0]
print(page.id)
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

`beta.sessions.threads.retrieve(thread_id, **kwargs)  -> BetaManagedAgentsSessionThread`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}`

Get Session Thread

#### Parameters

- `session_id: str`

- `thread_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

- `workspace_id: Optional[str]`

#### Returns

- `class BetaManagedAgentsSessionThread: …`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `type: Literal["session_thread"]`

  - `id: str`

    Unique identifier for this thread.

  - `agent: Agent`

    The resolved agent a session thread runs: a saved-agent snapshot, the platform advisor entry, or an inline-defined (ephemeral) agent snapshot.

    - `class BetaManagedAgentsSessionThreadAgent: …`

      Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

      - `type: Literal["agent"]`

      - `id: str`

      - `description: Optional[str]`

      - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

        - `type: Literal["url"]`

        - `name: str`

        - `url: str`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `Literal["claude-fable-5-1", "claude-sonnet-5", "claude-fable-5", 11 more]`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `claude-fable-5-1` - Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows
            - `claude-sonnet-5` - High-performance model for coding and agents
            - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
            - `claude-opus-5` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-8` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-7` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-6` - Powerful intelligence for long-running agents and coding
            - `claude-sonnet-4-6` - Best combination of speed and intelligence
            - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
            - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
            - `claude-opus-4-5` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-5-20251101` - Powerful intelligence for long-running agents and coding
            - `claude-sonnet-4-5` - High-performance model for agents and coding
            - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

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

          - `str`

        - `effort: Optional[Effort]`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow: …`

            Low effort. Favors latency over reasoning depth.

            - `type: Literal["low"]`

          - `class BetaManagedAgentsEffortMedium: …`

            Medium effort. Balances latency and reasoning depth.

            - `type: Literal["medium"]`

          - `class BetaManagedAgentsEffortHigh: …`

            High effort. Favors reasoning depth.

            - `type: Literal["high"]`

          - `class BetaManagedAgentsEffortXhigh: …`

            Extra-high effort. Not all models accept this level.

            - `type: Literal["xhigh"]`

          - `class BetaManagedAgentsEffortMax: …`

            Maximum effort. Favors reasoning depth over latency.

            - `type: Literal["max"]`

        - `inference_geo: Optional[str]`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `speed: Optional[Literal["standard", "fast"]]`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

      - `name: str`

      - `skills: List[Skill]`

        - `class BetaManagedAgentsAnthropicSkill: …`

          A resolved Anthropic-managed skill.

          - `type: Literal["anthropic"]`

          - `skill_id: str`

          - `version: str`

        - `class BetaManagedAgentsCustomSkill: …`

          A resolved user-created custom skill.

          - `type: Literal["custom"]`

          - `skill_id: str`

          - `version: str`

      - `system: Optional[str]`

      - `tools: List[Tool]`

        - `class BetaManagedAgentsAgentToolset20260401: …`

          - `type: Literal["agent_toolset_20260401"]`

          - `configs: List[BetaManagedAgentsAgentToolConfig]`

            - `class BetaManagedAgentsBashToolConfig: …`

              Configuration for the bash tool.

              - `type: Literal["bash"]`

              - `enabled: bool`

              - `name: Literal["bash"]`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                  - `type: Literal["always_allow"]`

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

                  - `type: Literal["always_ask"]`

                - `class BetaManagedAgentsAutoPolicy: …`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `type: Literal["auto"]`

            - `class BetaManagedAgentsEditToolConfig: …`

              Configuration for the edit tool.

              - `type: Literal["edit"]`

              - `enabled: bool`

              - `name: Literal["edit"]`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

                - `class BetaManagedAgentsAutoPolicy: …`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `class BetaManagedAgentsReadToolConfig: …`

              Configuration for the read tool.

              - `type: Literal["read"]`

              - `enabled: bool`

              - `name: Literal["read"]`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

                - `class BetaManagedAgentsAutoPolicy: …`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `class BetaManagedAgentsWriteToolConfig: …`

              Configuration for the write tool.

              - `type: Literal["write"]`

              - `enabled: bool`

              - `name: Literal["write"]`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

                - `class BetaManagedAgentsAutoPolicy: …`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `class BetaManagedAgentsGlobToolConfig: …`

              Configuration for the glob tool.

              - `type: Literal["glob"]`

              - `enabled: bool`

              - `name: Literal["glob"]`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

                - `class BetaManagedAgentsAutoPolicy: …`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `class BetaManagedAgentsGrepToolConfig: …`

              Configuration for the grep tool.

              - `type: Literal["grep"]`

              - `enabled: bool`

              - `name: Literal["grep"]`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

                - `class BetaManagedAgentsAutoPolicy: …`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `class BetaManagedAgentsWebFetchToolConfig: …`

              Configuration for the web_fetch tool.

              - `type: Literal["web_fetch"]`

              - `enabled: bool`

              - `name: Literal["web_fetch"]`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

                - `class BetaManagedAgentsAutoPolicy: …`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `allowed_domains: Optional[List[str]]`

              - `blocked_domains: Optional[List[str]]`

              - `max_content_tokens: Optional[int]`

                format: int32

            - `class BetaManagedAgentsWebSearchToolConfig: …`

              Configuration for the web_search tool.

              - `type: Literal["web_search"]`

              - `enabled: bool`

              - `name: Literal["web_search"]`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

                - `class BetaManagedAgentsAutoPolicy: …`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `allowed_domains: Optional[List[str]]`

              - `blocked_domains: Optional[List[str]]`

              - `user_location: Optional[BetaManagedAgentsUserLocation]`

                Approximate user location for search result localization.

                - `type: Literal["approximate"]`

                  Location precision. Only "approximate" is supported.

                - `city: Optional[str]`

                  City name.

                  minLength: 1, maxLength: 255

                - `country: Optional[str]`

                  Two-letter ISO 3166-1 country code, uppercase.

                - `region: Optional[str]`

                  Region or state name.

                  minLength: 1, maxLength: 255

                - `timezone: Optional[str]`

                  IANA timezone identifier, e.g. "America/Los_Angeles".

                  minLength: 1, maxLength: 255

          - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

            Resolved default configuration for agent tools.

            - `enabled: bool`

            - `permission_policy: PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy: …`

                Tool calls require user confirmation before execution.

              - `class BetaManagedAgentsAutoPolicy: …`

                The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

        - `class BetaManagedAgentsMCPToolset: …`

          - `type: Literal["mcp_toolset"]`

          - `configs: List[BetaManagedAgentsMCPToolConfig]`

            - `enabled: bool`

            - `name: str`

            - `permission_policy: PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy: …`

                Tool calls require user confirmation before execution.

              - `class BetaManagedAgentsAutoPolicy: …`

                The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

          - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

            Resolved default configuration for all tools from an MCP server.

            - `enabled: bool`

            - `permission_policy: PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy: …`

                Tool calls require user confirmation before execution.

              - `class BetaManagedAgentsAutoPolicy: …`

                The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

          - `mcp_server_name: str`

        - `class BetaManagedAgentsCustomTool: …`

          A custom tool as returned in API responses.

          - `type: Literal["custom"]`

          - `description: str`

          - `input_schema: BetaManagedAgentsCustomToolInputSchema`

            JSON Schema for custom tool input parameters.

            - `type: Literal["object"]`

            - `properties: Optional[Dict[str, object]]`

            - `required: Optional[List[str]]`

          - `name: str`

      - `version: int`

        format: int32

    - `class BetaManagedAgentsAdvisor: …`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `type: Literal["advisor"]`

      - `model: str`

        The advisor model id.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: datetime`

    A timestamp in RFC 3339 format

    format: date-time

  - `parent_thread_id: Optional[str]`

    Parent thread that spawned this thread. Null for the primary thread.

  - `session_id: str`

    The session this thread belongs to.

  - `stats: Optional[BetaManagedAgentsSessionThreadStats]`

    Timing statistics for a session thread.

    - `active_seconds: Optional[float]`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

      format: double

    - `duration_seconds: Optional[float]`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

      format: double

    - `startup_seconds: Optional[float]`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

      format: double

  - `status: BetaManagedAgentsSessionThreadStatus`

    SessionThreadStatus enum

    - `"running"`

    - `"idle"`

    - `"rescheduling"`

    - `"terminated"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

    format: date-time

  - `usage: Optional[BetaManagedAgentsSessionThreadUsage]`

    Cumulative token usage for a session thread across all turns.

    - `active_seconds: Optional[float]`

      Cumulative time in seconds this thread spent in running status. Equal to `stats.active_seconds`; surfaced here so a thread's usage carries every quantity its cost is priced on.

      format: double

    - `cache_creation: Optional[BetaManagedAgentsCacheCreationUsage]`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: Optional[int]`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `ephemeral_5m_input_tokens: Optional[int]`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `cache_read_input_tokens: Optional[int]`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens: Optional[int]`

      Total input tokens consumed across all turns.

      format: int32

    - `list_cost: Optional[BetaMonetaryAmount]`

      A monetary amount in a specific currency.

      - `amount: str`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `output_tokens: Optional[int]`

      Total output tokens generated across all turns.

      format: int32

    - `server_tool_use: Optional[BetaManagedAgentsServerToolUsage]`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `web_fetch_requests: Optional[int]`

        Number of server-executed web fetch requests.

        format: int32

      - `web_search_requests: Optional[int]`

        Number of server-executed web search requests.

        format: int32

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_managed_agents_session_thread = client.beta.sessions.threads.retrieve(
    thread_id="sthr_011CZkZVWa6oIjw0rgXZpnBt",
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
)
print(beta_managed_agents_session_thread.id)
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

`beta.sessions.threads.archive(thread_id, **kwargs)  -> BetaManagedAgentsSessionThread`

**POST** `/v1/sessions/{session_id}/threads/{thread_id}/archive`

Archive Session Thread

#### Parameters

- `session_id: str`

- `thread_id: str`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

- `workspace_id: Optional[str]`

#### Returns

- `class BetaManagedAgentsSessionThread: …`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `type: Literal["session_thread"]`

  - `id: str`

    Unique identifier for this thread.

  - `agent: Agent`

    The resolved agent a session thread runs: a saved-agent snapshot, the platform advisor entry, or an inline-defined (ephemeral) agent snapshot.

    - `class BetaManagedAgentsSessionThreadAgent: …`

      Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

      - `type: Literal["agent"]`

      - `id: str`

      - `description: Optional[str]`

      - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

        - `type: Literal["url"]`

        - `name: str`

        - `url: str`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `Literal["claude-fable-5-1", "claude-sonnet-5", "claude-fable-5", 11 more]`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `claude-fable-5-1` - Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows
            - `claude-sonnet-5` - High-performance model for coding and agents
            - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
            - `claude-opus-5` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-8` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-7` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-6` - Powerful intelligence for long-running agents and coding
            - `claude-sonnet-4-6` - Best combination of speed and intelligence
            - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
            - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
            - `claude-opus-4-5` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-5-20251101` - Powerful intelligence for long-running agents and coding
            - `claude-sonnet-4-5` - High-performance model for agents and coding
            - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

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

          - `str`

        - `effort: Optional[Effort]`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow: …`

            Low effort. Favors latency over reasoning depth.

            - `type: Literal["low"]`

          - `class BetaManagedAgentsEffortMedium: …`

            Medium effort. Balances latency and reasoning depth.

            - `type: Literal["medium"]`

          - `class BetaManagedAgentsEffortHigh: …`

            High effort. Favors reasoning depth.

            - `type: Literal["high"]`

          - `class BetaManagedAgentsEffortXhigh: …`

            Extra-high effort. Not all models accept this level.

            - `type: Literal["xhigh"]`

          - `class BetaManagedAgentsEffortMax: …`

            Maximum effort. Favors reasoning depth over latency.

            - `type: Literal["max"]`

        - `inference_geo: Optional[str]`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `speed: Optional[Literal["standard", "fast"]]`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

      - `name: str`

      - `skills: List[Skill]`

        - `class BetaManagedAgentsAnthropicSkill: …`

          A resolved Anthropic-managed skill.

          - `type: Literal["anthropic"]`

          - `skill_id: str`

          - `version: str`

        - `class BetaManagedAgentsCustomSkill: …`

          A resolved user-created custom skill.

          - `type: Literal["custom"]`

          - `skill_id: str`

          - `version: str`

      - `system: Optional[str]`

      - `tools: List[Tool]`

        - `class BetaManagedAgentsAgentToolset20260401: …`

          - `type: Literal["agent_toolset_20260401"]`

          - `configs: List[BetaManagedAgentsAgentToolConfig]`

            - `class BetaManagedAgentsBashToolConfig: …`

              Configuration for the bash tool.

              - `type: Literal["bash"]`

              - `enabled: bool`

              - `name: Literal["bash"]`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                  - `type: Literal["always_allow"]`

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

                  - `type: Literal["always_ask"]`

                - `class BetaManagedAgentsAutoPolicy: …`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `type: Literal["auto"]`

            - `class BetaManagedAgentsEditToolConfig: …`

              Configuration for the edit tool.

              - `type: Literal["edit"]`

              - `enabled: bool`

              - `name: Literal["edit"]`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

                - `class BetaManagedAgentsAutoPolicy: …`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `class BetaManagedAgentsReadToolConfig: …`

              Configuration for the read tool.

              - `type: Literal["read"]`

              - `enabled: bool`

              - `name: Literal["read"]`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

                - `class BetaManagedAgentsAutoPolicy: …`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `class BetaManagedAgentsWriteToolConfig: …`

              Configuration for the write tool.

              - `type: Literal["write"]`

              - `enabled: bool`

              - `name: Literal["write"]`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

                - `class BetaManagedAgentsAutoPolicy: …`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `class BetaManagedAgentsGlobToolConfig: …`

              Configuration for the glob tool.

              - `type: Literal["glob"]`

              - `enabled: bool`

              - `name: Literal["glob"]`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

                - `class BetaManagedAgentsAutoPolicy: …`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `class BetaManagedAgentsGrepToolConfig: …`

              Configuration for the grep tool.

              - `type: Literal["grep"]`

              - `enabled: bool`

              - `name: Literal["grep"]`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

                - `class BetaManagedAgentsAutoPolicy: …`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

            - `class BetaManagedAgentsWebFetchToolConfig: …`

              Configuration for the web_fetch tool.

              - `type: Literal["web_fetch"]`

              - `enabled: bool`

              - `name: Literal["web_fetch"]`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

                - `class BetaManagedAgentsAutoPolicy: …`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `allowed_domains: Optional[List[str]]`

              - `blocked_domains: Optional[List[str]]`

              - `max_content_tokens: Optional[int]`

                format: int32

            - `class BetaManagedAgentsWebSearchToolConfig: …`

              Configuration for the web_search tool.

              - `type: Literal["web_search"]`

              - `enabled: bool`

              - `name: Literal["web_search"]`

              - `permission_policy: PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy: …`

                  Tool calls require user confirmation before execution.

                - `class BetaManagedAgentsAutoPolicy: …`

                  The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `allowed_domains: Optional[List[str]]`

              - `blocked_domains: Optional[List[str]]`

              - `user_location: Optional[BetaManagedAgentsUserLocation]`

                Approximate user location for search result localization.

                - `type: Literal["approximate"]`

                  Location precision. Only "approximate" is supported.

                - `city: Optional[str]`

                  City name.

                  minLength: 1, maxLength: 255

                - `country: Optional[str]`

                  Two-letter ISO 3166-1 country code, uppercase.

                - `region: Optional[str]`

                  Region or state name.

                  minLength: 1, maxLength: 255

                - `timezone: Optional[str]`

                  IANA timezone identifier, e.g. "America/Los_Angeles".

                  minLength: 1, maxLength: 255

          - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

            Resolved default configuration for agent tools.

            - `enabled: bool`

            - `permission_policy: PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy: …`

                Tool calls require user confirmation before execution.

              - `class BetaManagedAgentsAutoPolicy: …`

                The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

        - `class BetaManagedAgentsMCPToolset: …`

          - `type: Literal["mcp_toolset"]`

          - `configs: List[BetaManagedAgentsMCPToolConfig]`

            - `enabled: bool`

            - `name: str`

            - `permission_policy: PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy: …`

                Tool calls require user confirmation before execution.

              - `class BetaManagedAgentsAutoPolicy: …`

                The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

          - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

            Resolved default configuration for all tools from an MCP server.

            - `enabled: bool`

            - `permission_policy: PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy: …`

                Tool calls require user confirmation before execution.

              - `class BetaManagedAgentsAutoPolicy: …`

                The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

          - `mcp_server_name: str`

        - `class BetaManagedAgentsCustomTool: …`

          A custom tool as returned in API responses.

          - `type: Literal["custom"]`

          - `description: str`

          - `input_schema: BetaManagedAgentsCustomToolInputSchema`

            JSON Schema for custom tool input parameters.

            - `type: Literal["object"]`

            - `properties: Optional[Dict[str, object]]`

            - `required: Optional[List[str]]`

          - `name: str`

      - `version: int`

        format: int32

    - `class BetaManagedAgentsAdvisor: …`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `type: Literal["advisor"]`

      - `model: str`

        The advisor model id.

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: datetime`

    A timestamp in RFC 3339 format

    format: date-time

  - `parent_thread_id: Optional[str]`

    Parent thread that spawned this thread. Null for the primary thread.

  - `session_id: str`

    The session this thread belongs to.

  - `stats: Optional[BetaManagedAgentsSessionThreadStats]`

    Timing statistics for a session thread.

    - `active_seconds: Optional[float]`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

      format: double

    - `duration_seconds: Optional[float]`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

      format: double

    - `startup_seconds: Optional[float]`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

      format: double

  - `status: BetaManagedAgentsSessionThreadStatus`

    SessionThreadStatus enum

    - `"running"`

    - `"idle"`

    - `"rescheduling"`

    - `"terminated"`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

    format: date-time

  - `usage: Optional[BetaManagedAgentsSessionThreadUsage]`

    Cumulative token usage for a session thread across all turns.

    - `active_seconds: Optional[float]`

      Cumulative time in seconds this thread spent in running status. Equal to `stats.active_seconds`; surfaced here so a thread's usage carries every quantity its cost is priced on.

      format: double

    - `cache_creation: Optional[BetaManagedAgentsCacheCreationUsage]`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: Optional[int]`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `ephemeral_5m_input_tokens: Optional[int]`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `cache_read_input_tokens: Optional[int]`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens: Optional[int]`

      Total input tokens consumed across all turns.

      format: int32

    - `list_cost: Optional[BetaMonetaryAmount]`

      A monetary amount in a specific currency.

      - `amount: str`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `output_tokens: Optional[int]`

      Total output tokens generated across all turns.

      format: int32

    - `server_tool_use: Optional[BetaManagedAgentsServerToolUsage]`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `web_fetch_requests: Optional[int]`

        Number of server-executed web fetch requests.

        format: int32

      - `web_search_requests: Optional[int]`

        Number of server-executed web search requests.

        format: int32

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_managed_agents_session_thread = client.beta.sessions.threads.archive(
    thread_id="sthr_011CZkZVWa6oIjw0rgXZpnBt",
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
)
print(beta_managed_agents_session_thread.id)
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

`beta.sessions.threads.events.list(thread_id, **kwargs)  -> SyncPageCursor[BetaManagedAgentsSessionEvent]`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}/events`

List Session Thread Events

#### Parameters

- `session_id: str`

- `thread_id: str`

- `limit: Optional[int]`

  Query parameter for limit

  format: int32

- `page: Optional[str]`

  Query parameter for page

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

- `workspace_id: Optional[str]`

#### Returns

- `BetaManagedAgentsSessionEvent`

  Union type for all event types in a session.

  - `class BetaManagedAgentsUserMessageEvent: …`

    A user message event in the session conversation.

    - `type: Literal["user.message"]`

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

        - `type: Literal["text"]`

        - `text: str`

          The text content.

          minLength: 1

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

        - `type: Literal["image"]`

        - `source: Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource: …`

            Base64-encoded image data.

            - `type: Literal["base64"]`

            - `data: str`

              Base64-encoded image data.

              minLength: 1

            - `media_type: str`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

          - `class BetaManagedAgentsURLImageSource: …`

            Image referenced by URL.

            - `type: Literal["url"]`

            - `url: str`

              URL of the image to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileImageSource: …`

            Image referenced by file ID.

            - `type: Literal["file"]`

            - `file_id: str`

              ID of a previously uploaded file.

              minLength: 1

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `type: Literal["document"]`

        - `source: Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource: …`

            Base64-encoded document data.

            - `type: Literal["base64"]`

            - `data: str`

              Base64-encoded document data.

              minLength: 1

            - `media_type: str`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

          - `class BetaManagedAgentsPlainTextDocumentSource: …`

            Plain text document content.

            - `type: Literal["text"]`

            - `data: str`

              The plain text content.

              minLength: 1

            - `media_type: Literal["text/plain"]`

              MIME type of the text content. Must be "text/plain".

          - `class BetaManagedAgentsURLDocumentSource: …`

            Document referenced by URL.

            - `type: Literal["url"]`

            - `url: str`

              URL of the document to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileDocumentSource: …`

            Document referenced by file ID.

            - `type: Literal["file"]`

            - `file_id: str`

              ID of a previously uploaded file.

              minLength: 1

        - `context: Optional[str]`

          Additional context about the document for the model.

        - `title: Optional[str]`

          The title of the document.

      - `class BetaManagedAgentsRedactedBlock: …`

        Placeholder for content withheld by Anthropic model policy.

        - `type: Literal["redacted"]`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsUserInterruptEvent: …`

    An interrupt event that pauses agent execution and returns control to the user.

    - `type: Literal["user.interrupt"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: Optional[str]`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEvent: …`

    A tool confirmation event that approves or denies a pending tool execution.

    - `type: Literal["user.tool_confirmation"]`

    - `id: str`

      Unique identifier for this event.

    - `result: Literal["allow", "deny"]`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: str`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `deny_message: Optional[str]`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: Optional[str]`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `class BetaManagedAgentsUserCustomToolResultEvent: …`

    Event sent by the client providing the result of a custom tool execution.

    - `type: Literal["user.custom_tool_result"]`

    - `id: str`

      Unique identifier for this event.

    - `custom_tool_use_id: str`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

        - `type: Literal["search_result"]`

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `enabled: bool`

            Whether citations are enabled for this search result.

        - `content: List[BetaManagedAgentsSearchResultContent]`

          Array of text content blocks from the search result.

          - `type: Literal["text"]`

          - `text: str`

            The text content.

            minLength: 1

        - `source: str`

          The URL source of the search result.

          minLength: 1

        - `title: str`

          The title of the search result.

          minLength: 1

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: Optional[str]`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsAgentCustomToolUseEvent: …`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `type: Literal["agent.custom_tool_use"]`

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `name: str`

      Name of the custom tool being called.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `class BetaManagedAgentsAgentMessageEvent: …`

    An agent response event in the session conversation.

    - `type: Literal["agent.message"]`

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Array of text blocks comprising the agent response.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsRedactedBlock: …`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsAgentThinkingEvent: …`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `type: Literal["agent.thinking"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsAgentMCPToolUseEvent: …`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `type: Literal["agent.mcp_tool_use"]`

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `mcp_server_name: str`

      Name of the MCP server providing the tool.

    - `name: str`

      Name of the MCP tool being used.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `evaluated_permission: Optional[Literal["allow", "ask", "deny"]]`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `evaluation: Optional[BetaManagedAgentsAgentToolEvaluation]`

      Names the resolved permission_policy that produced evaluated_permission, and under auto carries the judgement. Open union: clients must tolerate unknown variants.

      - `class BetaManagedAgentsAgentToolEvaluationAlwaysAllow: …`

        The resolved permission_policy was always_allow; accompanies evaluated_permission "allow".

        - `type: Literal["always_allow"]`

      - `class BetaManagedAgentsAgentToolEvaluationAlwaysAsk: …`

        The resolved permission_policy was always_ask; accompanies evaluated_permission "ask".

        - `type: Literal["always_ask"]`

      - `class BetaManagedAgentsAgentToolEvaluationAuto: …`

        The resolved permission_policy was auto: the server judged this invocation individually.

        - `type: Literal["auto"]`

        - `evaluated_permission: BetaManagedAgentsAgentAutoEvaluatedPermission`

          The server's per-invocation judgement under the auto permission policy. Its type always equals the event's top-level evaluated_permission. Open union: clients must tolerate unknown variants.

          - `class BetaManagedAgentsAgentAutoEvaluatedPermissionAllow: …`

            The server judged the invocation safe to execute without client approval.

            - `type: Literal["allow"]`

          - `class BetaManagedAgentsAgentAutoEvaluatedPermissionAsk: …`

            The server reached no judgement; the invocation is held for client approval.

            - `type: Literal["ask"]`

            - `reason_code: str`

              The judgement's grounds in registry-bound terms, for client branching and audit rather than end-user display. Open registry; currently "indeterminate" (no judgement was reached). Clients must tolerate values outside this set.

              maxLength: 64

          - `class BetaManagedAgentsAgentAutoEvaluatedPermissionDeny: …`

            The server judged the invocation high-risk; it does not execute and a synthetic error tool result is appended.

            - `type: Literal["deny"]`

            - `reason_code: str`

              The judgement's grounds in registry-bound terms. Open registry; currently "high_risk" (judged high-risk; the call does not run). Clients must tolerate values outside this set.

              maxLength: 64

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentMCPToolResultEvent: …`

    Event representing the result of an MCP tool execution.

    - `type: Literal["agent.mcp_tool_result"]`

    - `id: str`

      Unique identifier for this event.

    - `mcp_tool_use_id: str`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent: …`

    Event emitted when the agent invokes a built-in agent tool.

    - `type: Literal["agent.tool_use"]`

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `name: str`

      Name of the agent tool being used.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `evaluated_permission: Optional[Literal["allow", "ask", "deny"]]`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `evaluation: Optional[BetaManagedAgentsAgentToolEvaluation]`

      Names the resolved permission_policy that produced evaluated_permission, and under auto carries the judgement. Open union: clients must tolerate unknown variants.

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentToolResultEvent: …`

    Event representing the result of an agent tool execution.

    - `type: Literal["agent.tool_result"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `tool_use_id: str`

      The id of the `agent.tool_use` event this result corresponds to.

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadMessageReceivedEvent: …`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `type: Literal["agent.thread_message_received"]`

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock: …`

        Placeholder for content withheld by Anthropic model policy.

    - `from_session_thread_id: str`

      Public `sthr_` ID of the thread that sent the message.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `from_agent_name: Optional[str]`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class BetaManagedAgentsAgentThreadMessageSentEvent: …`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `type: Literal["agent.thread_message_sent"]`

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock: …`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `to_session_thread_id: str`

      Public `sthr_` ID of the thread the message was sent to.

    - `to_agent_name: Optional[str]`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent: …`

    Indicates that context compaction (summarization) occurred during the session.

    - `type: Literal["agent.thread_context_compacted"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionErrorEvent: …`

    An error event indicating a problem occurred during session execution.

    - `type: Literal["session.error"]`

    - `id: str`

      Unique identifier for this event.

    - `error: Error`

      - `class BetaManagedAgentsUnknownError: …`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `type: Literal["unknown_error"]`

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: Literal["retrying"]`

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: Literal["exhausted"]`

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: Literal["terminal"]`

      - `class BetaManagedAgentsModelOverloadedError: …`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `type: Literal["model_overloaded_error"]`

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

      - `class BetaManagedAgentsModelRateLimitedError: …`

        The model request was rate-limited.

        - `type: Literal["model_rate_limited_error"]`

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

      - `class BetaManagedAgentsModelRequestFailedError: …`

        A model request failed for a reason other than overload or rate-limiting.

        - `type: Literal["model_request_failed_error"]`

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

      - `class BetaManagedAgentsMCPConnectionFailedError: …`

        Failed to connect to an MCP server.

        - `type: Literal["mcp_connection_failed_error"]`

        - `mcp_server_name: str`

          Name of the MCP server that failed to connect.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

      - `class BetaManagedAgentsMCPAuthenticationFailedError: …`

        Authentication to an MCP server failed.

        - `type: Literal["mcp_authentication_failed_error"]`

        - `mcp_server_name: str`

          Name of the MCP server that failed authentication.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

      - `class BetaManagedAgentsBillingError: …`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `type: Literal["billing_error"]`

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

      - `class BetaManagedAgentsCredentialHostUnreachableError: …`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `type: Literal["credential_host_unreachable_error"]`

        - `credential_id: str`

          ID of the affected credential.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `vault_id: str`

          ID of the vault containing the affected credential.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionStatusRescheduledEvent: …`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `type: Literal["session.status_rescheduled"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionStatusRunningEvent: …`

    Indicates the session is actively running and the agent is working.

    - `type: Literal["session.status_running"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionStatusIdleEvent: …`

    Indicates the agent has paused and is awaiting user input.

    - `type: Literal["session.status_idle"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `stop_reason: StopReason`

      - `class BetaManagedAgentsSessionEndTurn: …`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: Literal["end_turn"]`

      - `class BetaManagedAgentsSessionRequiresAction: …`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `type: Literal["requires_action"]`

        - `event_ids: List[str]`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

      - `class BetaManagedAgentsSessionRetriesExhausted: …`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `type: Literal["retries_exhausted"]`

      - `class BetaManagedAgentsSessionBudgetReached: …`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `type: Literal["budget_reached"]`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent: …`

    Indicates the session has terminated, either due to an error or completion.

    - `type: Literal["session.status_terminated"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionThreadCreatedEvent: …`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `type: Literal["session.thread_created"]`

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the callable agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: str`

      Public `sthr_` ID of the newly created thread.

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent: …`

    Emitted when an outcome evaluation cycle begins.

    - `type: Literal["span.outcome_evaluation_start"]`

    - `id: str`

      Unique identifier for this event.

    - `iteration: int`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

      format: int32

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent: …`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `type: Literal["span.outcome_evaluation_end"]`

    - `id: str`

      Unique identifier for this event.

    - `explanation: str`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `iteration: int`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `outcome_evaluation_start_id: str`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `result: str`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `cache_creation_input_tokens: int`

        Tokens used to create prompt cache in this request.

        format: int32

      - `cache_read_input_tokens: int`

        Tokens read from prompt cache in this request.

        format: int32

      - `input_tokens: int`

        Input tokens consumed by this request.

        format: int32

      - `output_tokens: int`

        Output tokens generated by this request.

        format: int32

      - `speed: Optional[Literal["standard", "fast"]]`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `class BetaManagedAgentsSpanModelRequestStartEvent: …`

    Emitted when a model request is initiated by the agent.

    - `type: Literal["span.model_request_start"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSpanModelRequestEndEvent: …`

    Emitted when a model request completes.

    - `type: Literal["span.model_request_end"]`

    - `id: str`

      Unique identifier for this event.

    - `is_error: Optional[bool]`

      Whether the model request resulted in an error.

    - `model_request_start_id: str`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent: …`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `type: Literal["span.outcome_evaluation_ongoing"]`

    - `id: str`

      Unique identifier for this event.

    - `iteration: int`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsUserDefineOutcomeEvent: …`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `type: Literal["user.define_outcome"]`

    - `id: str`

      Unique identifier for this event.

    - `description: str`

      What the agent should produce. Copied from the input event.

    - `max_iterations: Optional[int]`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

      format: int32

    - `outcome_id: str`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `rubric: Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric: …`

        Rubric referenced by a file uploaded via the Files API.

        - `type: Literal["file"]`

        - `file_id: str`

          ID of the rubric file.

      - `class BetaManagedAgentsTextRubric: …`

        Rubric content provided inline as text.

        - `type: Literal["text"]`

        - `content: str`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

  - `class BetaManagedAgentsSessionDeletedEvent: …`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `type: Literal["session.deleted"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent: …`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: Literal["session.thread_status_running"]`

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: str`

      Public sthr_ ID of the thread that started running.

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent: …`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: Literal["session.thread_status_idle"]`

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: str`

      Public sthr_ ID of the thread that went idle.

    - `stop_reason: StopReason`

      - `class BetaManagedAgentsSessionEndTurn: …`

        The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionRequiresAction: …`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `class BetaManagedAgentsSessionRetriesExhausted: …`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `class BetaManagedAgentsSessionBudgetReached: …`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent: …`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: Literal["session.thread_status_terminated"]`

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: str`

      Public sthr_ ID of the thread that terminated.

  - `class BetaManagedAgentsUserToolResultEvent: …`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `type: Literal["user.tool_result"]`

    - `id: str`

      Unique identifier for this event.

    - `tool_use_id: str`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: Optional[str]`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent: …`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: Literal["session.thread_status_rescheduled"]`

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: str`

      Public sthr_ ID of the thread that is retrying.

  - `class BetaManagedAgentsSessionUpdatedEvent: …`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `type: Literal["session.updated"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `agent: Optional[BetaManagedAgentsSessionAgent]`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `type: Literal["agent"]`

      - `id: str`

      - `description: Optional[str]`

      - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

        - `type: Literal["url"]`

        - `name: str`

        - `url: str`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `Literal["claude-fable-5-1", "claude-sonnet-5", "claude-fable-5", 11 more]`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `claude-fable-5-1` - Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows
            - `claude-sonnet-5` - High-performance model for coding and agents
            - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
            - `claude-opus-5` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-8` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-7` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-6` - Powerful intelligence for long-running agents and coding
            - `claude-sonnet-4-6` - Best combination of speed and intelligence
            - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
            - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
            - `claude-opus-4-5` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-5-20251101` - Powerful intelligence for long-running agents and coding
            - `claude-sonnet-4-5` - High-performance model for agents and coding
            - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

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

          - `str`

        - `effort: Optional[Effort]`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow: …`

            Low effort. Favors latency over reasoning depth.

            - `type: Literal["low"]`

          - `class BetaManagedAgentsEffortMedium: …`

            Medium effort. Balances latency and reasoning depth.

            - `type: Literal["medium"]`

          - `class BetaManagedAgentsEffortHigh: …`

            High effort. Favors reasoning depth.

            - `type: Literal["high"]`

          - `class BetaManagedAgentsEffortXhigh: …`

            Extra-high effort. Not all models accept this level.

            - `type: Literal["xhigh"]`

          - `class BetaManagedAgentsEffortMax: …`

            Maximum effort. Favors reasoning depth over latency.

            - `type: Literal["max"]`

        - `inference_geo: Optional[str]`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `speed: Optional[Literal["standard", "fast"]]`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

      - `multiagent: Optional[BetaManagedAgentsSessionMultiagentCoordinator]`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `type: Literal["coordinator"]`

        - `agents: List[Agent]`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `class BetaManagedAgentsSessionThreadAgent: …`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `type: Literal["agent"]`

            - `id: str`

            - `description: Optional[str]`

            - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

              - `type: Literal["url"]`

              - `name: str`

              - `url: str`

            - `model: BetaManagedAgentsModelConfig`

              Model identifier and configuration.

            - `name: str`

            - `skills: List[Skill]`

              - `class BetaManagedAgentsAnthropicSkill: …`

                A resolved Anthropic-managed skill.

                - `type: Literal["anthropic"]`

                - `skill_id: str`

                - `version: str`

              - `class BetaManagedAgentsCustomSkill: …`

                A resolved user-created custom skill.

                - `type: Literal["custom"]`

                - `skill_id: str`

                - `version: str`

            - `system: Optional[str]`

            - `tools: List[Tool]`

              - `class BetaManagedAgentsAgentToolset20260401: …`

                - `type: Literal["agent_toolset_20260401"]`

                - `configs: List[BetaManagedAgentsAgentToolConfig]`

                  - `class BetaManagedAgentsBashToolConfig: …`

                    Configuration for the bash tool.

                    - `type: Literal["bash"]`

                    - `enabled: bool`

                    - `name: Literal["bash"]`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                        - `type: Literal["always_allow"]`

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                        - `type: Literal["always_ask"]`

                      - `class BetaManagedAgentsAutoPolicy: …`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                        - `type: Literal["auto"]`

                  - `class BetaManagedAgentsEditToolConfig: …`

                    Configuration for the edit tool.

                    - `type: Literal["edit"]`

                    - `enabled: bool`

                    - `name: Literal["edit"]`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                      - `class BetaManagedAgentsAutoPolicy: …`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `class BetaManagedAgentsReadToolConfig: …`

                    Configuration for the read tool.

                    - `type: Literal["read"]`

                    - `enabled: bool`

                    - `name: Literal["read"]`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                      - `class BetaManagedAgentsAutoPolicy: …`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `class BetaManagedAgentsWriteToolConfig: …`

                    Configuration for the write tool.

                    - `type: Literal["write"]`

                    - `enabled: bool`

                    - `name: Literal["write"]`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                      - `class BetaManagedAgentsAutoPolicy: …`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `class BetaManagedAgentsGlobToolConfig: …`

                    Configuration for the glob tool.

                    - `type: Literal["glob"]`

                    - `enabled: bool`

                    - `name: Literal["glob"]`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                      - `class BetaManagedAgentsAutoPolicy: …`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `class BetaManagedAgentsGrepToolConfig: …`

                    Configuration for the grep tool.

                    - `type: Literal["grep"]`

                    - `enabled: bool`

                    - `name: Literal["grep"]`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                      - `class BetaManagedAgentsAutoPolicy: …`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `class BetaManagedAgentsWebFetchToolConfig: …`

                    Configuration for the web_fetch tool.

                    - `type: Literal["web_fetch"]`

                    - `enabled: bool`

                    - `name: Literal["web_fetch"]`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                      - `class BetaManagedAgentsAutoPolicy: …`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `allowed_domains: Optional[List[str]]`

                    - `blocked_domains: Optional[List[str]]`

                    - `max_content_tokens: Optional[int]`

                      format: int32

                  - `class BetaManagedAgentsWebSearchToolConfig: …`

                    Configuration for the web_search tool.

                    - `type: Literal["web_search"]`

                    - `enabled: bool`

                    - `name: Literal["web_search"]`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                      - `class BetaManagedAgentsAutoPolicy: …`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `allowed_domains: Optional[List[str]]`

                    - `blocked_domains: Optional[List[str]]`

                    - `user_location: Optional[BetaManagedAgentsUserLocation]`

                      Approximate user location for search result localization.

                      - `type: Literal["approximate"]`

                        Location precision. Only "approximate" is supported.

                      - `city: Optional[str]`

                        City name.

                        minLength: 1, maxLength: 255

                      - `country: Optional[str]`

                        Two-letter ISO 3166-1 country code, uppercase.

                      - `region: Optional[str]`

                        Region or state name.

                        minLength: 1, maxLength: 255

                      - `timezone: Optional[str]`

                        IANA timezone identifier, e.g. "America/Los_Angeles".

                        minLength: 1, maxLength: 255

                - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

                  Resolved default configuration for agent tools.

                  - `enabled: bool`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `class BetaManagedAgentsMCPToolset: …`

                - `type: Literal["mcp_toolset"]`

                - `configs: List[BetaManagedAgentsMCPToolConfig]`

                  - `enabled: bool`

                  - `name: str`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `enabled: bool`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `mcp_server_name: str`

              - `class BetaManagedAgentsCustomTool: …`

                A custom tool as returned in API responses.

                - `type: Literal["custom"]`

                - `description: str`

                - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                  JSON Schema for custom tool input parameters.

                  - `type: Literal["object"]`

                  - `properties: Optional[Dict[str, object]]`

                  - `required: Optional[List[str]]`

                - `name: str`

            - `version: int`

              format: int32

          - `class BetaManagedAgentsAdvisor: …`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `type: Literal["advisor"]`

            - `model: str`

              The advisor model id.

      - `name: str`

      - `skills: List[Skill]`

        - `class BetaManagedAgentsAnthropicSkill: …`

          A resolved Anthropic-managed skill.

        - `class BetaManagedAgentsCustomSkill: …`

          A resolved user-created custom skill.

      - `system: Optional[str]`

      - `tools: List[Tool]`

        - `class BetaManagedAgentsAgentToolset20260401: …`

        - `class BetaManagedAgentsMCPToolset: …`

        - `class BetaManagedAgentsCustomTool: …`

          A custom tool as returned in API responses.

      - `version: int`

        format: int32

    - `budget: Optional[BetaManagedAgentsBudgetLimit]`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `type: Literal["limit"]`

      - `max_list_cost: BetaMonetaryAmount`

        A monetary amount in a specific currency.

        - `amount: str`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `currency: BetaCurrency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `metadata: Optional[Dict[str, str]]`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title: Optional[str]`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsSystemMessageEvent: …`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `type: Literal["system.message"]`

    - `id: str`

      Unique identifier for this event.

    - `content: List[BetaManagedAgentsSystemContentBlock]`

      System content blocks. Text-only.

      - `type: Literal["text"]`

      - `text: str`

        The text content.

        minLength: 1

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionUsageEvent: …`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `type: Literal["session.usage"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `usage: BetaManagedAgentsSessionUsageSnapshot`

      Point-in-time snapshot of a session's cumulative usage.

      - `active_seconds: Optional[float]`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `cache_creation: Optional[BetaManagedAgentsCacheCreationUsage]`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `ephemeral_1h_input_tokens: Optional[int]`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `ephemeral_5m_input_tokens: Optional[int]`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `cache_read_input_tokens: Optional[int]`

        Total tokens read from prompt cache.

        format: int32

      - `input_tokens: Optional[int]`

        Total input tokens consumed across all turns.

        format: int32

      - `list_cost: Optional[BetaMonetaryAmount]`

        A monetary amount in a specific currency.

      - `output_tokens: Optional[int]`

        Total output tokens generated across all turns.

        format: int32

      - `server_tool_use: Optional[BetaManagedAgentsServerToolUsage]`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `web_fetch_requests: Optional[int]`

          Number of server-executed web fetch requests.

          format: int32

        - `web_search_requests: Optional[int]`

          Number of server-executed web search requests.

          format: int32

    - `budget: Optional[BetaManagedAgentsBudgetLimit]`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
page = client.beta.sessions.threads.events.list(
    thread_id="sthr_011CZkZVWa6oIjw0rgXZpnBt",
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
)
page = page.data[0]
print(page)
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

`beta.sessions.threads.events.stream(thread_id, **kwargs)  -> BetaManagedAgentsStreamSessionThreadEvents`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}/stream`

Stream Session Thread Events

#### Parameters

- `session_id: str`

- `thread_id: str`

- `event_deltas: Optional[List[BetaManagedAgentsDeltaType]]`

  When set, this connection also receives streaming deltas (`event_start`, `event_delta`) while an event is being produced, before the event itself arrives. Deltas are best-effort; when the final event is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no final event — its terminal `span.model_request_end` closes the preview. Accepts one or more event types to preview and may be repeated: `agent.message` streams `content_delta` fragments; `agent.thinking` is start-only — a signal that the agent has begun extended thinking, concluded by the `agent.thinking` event itself. Only previews of the requested event types are sent.

  - `"agent.message"`

  - `"agent.thinking"`

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 42 more]`

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

- `workspace_id: Optional[str]`

#### Returns

- `BetaManagedAgentsStreamSessionThreadEvents`

  Server-sent event in a single thread's stream.

  - `class BetaManagedAgentsUserMessageEvent: …`

    A user message event in the session conversation.

    - `type: Literal["user.message"]`

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

        - `type: Literal["text"]`

        - `text: str`

          The text content.

          minLength: 1

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

        - `type: Literal["image"]`

        - `source: Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource: …`

            Base64-encoded image data.

            - `type: Literal["base64"]`

            - `data: str`

              Base64-encoded image data.

              minLength: 1

            - `media_type: str`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

          - `class BetaManagedAgentsURLImageSource: …`

            Image referenced by URL.

            - `type: Literal["url"]`

            - `url: str`

              URL of the image to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileImageSource: …`

            Image referenced by file ID.

            - `type: Literal["file"]`

            - `file_id: str`

              ID of a previously uploaded file.

              minLength: 1

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `type: Literal["document"]`

        - `source: Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource: …`

            Base64-encoded document data.

            - `type: Literal["base64"]`

            - `data: str`

              Base64-encoded document data.

              minLength: 1

            - `media_type: str`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

          - `class BetaManagedAgentsPlainTextDocumentSource: …`

            Plain text document content.

            - `type: Literal["text"]`

            - `data: str`

              The plain text content.

              minLength: 1

            - `media_type: Literal["text/plain"]`

              MIME type of the text content. Must be "text/plain".

          - `class BetaManagedAgentsURLDocumentSource: …`

            Document referenced by URL.

            - `type: Literal["url"]`

            - `url: str`

              URL of the document to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileDocumentSource: …`

            Document referenced by file ID.

            - `type: Literal["file"]`

            - `file_id: str`

              ID of a previously uploaded file.

              minLength: 1

        - `context: Optional[str]`

          Additional context about the document for the model.

        - `title: Optional[str]`

          The title of the document.

      - `class BetaManagedAgentsRedactedBlock: …`

        Placeholder for content withheld by Anthropic model policy.

        - `type: Literal["redacted"]`

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsUserInterruptEvent: …`

    An interrupt event that pauses agent execution and returns control to the user.

    - `type: Literal["user.interrupt"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: Optional[str]`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEvent: …`

    A tool confirmation event that approves or denies a pending tool execution.

    - `type: Literal["user.tool_confirmation"]`

    - `id: str`

      Unique identifier for this event.

    - `result: Literal["allow", "deny"]`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: str`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `deny_message: Optional[str]`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: Optional[str]`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `class BetaManagedAgentsUserCustomToolResultEvent: …`

    Event sent by the client providing the result of a custom tool execution.

    - `type: Literal["user.custom_tool_result"]`

    - `id: str`

      Unique identifier for this event.

    - `custom_tool_use_id: str`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

        - `type: Literal["search_result"]`

        - `citations: BetaManagedAgentsSearchResultCitations`

          Citation settings for a search result.

          - `enabled: bool`

            Whether citations are enabled for this search result.

        - `content: List[BetaManagedAgentsSearchResultContent]`

          Array of text content blocks from the search result.

          - `type: Literal["text"]`

          - `text: str`

            The text content.

            minLength: 1

        - `source: str`

          The URL source of the search result.

          minLength: 1

        - `title: str`

          The title of the search result.

          minLength: 1

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: Optional[str]`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsAgentCustomToolUseEvent: …`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `type: Literal["agent.custom_tool_use"]`

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `name: str`

      Name of the custom tool being called.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `class BetaManagedAgentsAgentMessageEvent: …`

    An agent response event in the session conversation.

    - `type: Literal["agent.message"]`

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Array of text blocks comprising the agent response.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsRedactedBlock: …`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsAgentThinkingEvent: …`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `type: Literal["agent.thinking"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsAgentMCPToolUseEvent: …`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `type: Literal["agent.mcp_tool_use"]`

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `mcp_server_name: str`

      Name of the MCP server providing the tool.

    - `name: str`

      Name of the MCP tool being used.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `evaluated_permission: Optional[Literal["allow", "ask", "deny"]]`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `evaluation: Optional[BetaManagedAgentsAgentToolEvaluation]`

      Names the resolved permission_policy that produced evaluated_permission, and under auto carries the judgement. Open union: clients must tolerate unknown variants.

      - `class BetaManagedAgentsAgentToolEvaluationAlwaysAllow: …`

        The resolved permission_policy was always_allow; accompanies evaluated_permission "allow".

        - `type: Literal["always_allow"]`

      - `class BetaManagedAgentsAgentToolEvaluationAlwaysAsk: …`

        The resolved permission_policy was always_ask; accompanies evaluated_permission "ask".

        - `type: Literal["always_ask"]`

      - `class BetaManagedAgentsAgentToolEvaluationAuto: …`

        The resolved permission_policy was auto: the server judged this invocation individually.

        - `type: Literal["auto"]`

        - `evaluated_permission: BetaManagedAgentsAgentAutoEvaluatedPermission`

          The server's per-invocation judgement under the auto permission policy. Its type always equals the event's top-level evaluated_permission. Open union: clients must tolerate unknown variants.

          - `class BetaManagedAgentsAgentAutoEvaluatedPermissionAllow: …`

            The server judged the invocation safe to execute without client approval.

            - `type: Literal["allow"]`

          - `class BetaManagedAgentsAgentAutoEvaluatedPermissionAsk: …`

            The server reached no judgement; the invocation is held for client approval.

            - `type: Literal["ask"]`

            - `reason_code: str`

              The judgement's grounds in registry-bound terms, for client branching and audit rather than end-user display. Open registry; currently "indeterminate" (no judgement was reached). Clients must tolerate values outside this set.

              maxLength: 64

          - `class BetaManagedAgentsAgentAutoEvaluatedPermissionDeny: …`

            The server judged the invocation high-risk; it does not execute and a synthetic error tool result is appended.

            - `type: Literal["deny"]`

            - `reason_code: str`

              The judgement's grounds in registry-bound terms. Open registry; currently "high_risk" (judged high-risk; the call does not run). Clients must tolerate values outside this set.

              maxLength: 64

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentMCPToolResultEvent: …`

    Event representing the result of an MCP tool execution.

    - `type: Literal["agent.mcp_tool_result"]`

    - `id: str`

      Unique identifier for this event.

    - `mcp_tool_use_id: str`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent: …`

    Event emitted when the agent invokes a built-in agent tool.

    - `type: Literal["agent.tool_use"]`

    - `id: str`

      Unique identifier for this event.

    - `input: Dict[str, object]`

      Input parameters for the tool call.

    - `name: str`

      Name of the agent tool being used.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `evaluated_permission: Optional[Literal["allow", "ask", "deny"]]`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `evaluation: Optional[BetaManagedAgentsAgentToolEvaluation]`

      Names the resolved permission_policy that produced evaluated_permission, and under auto carries the judgement. Open union: clients must tolerate unknown variants.

    - `session_thread_id: Optional[str]`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentToolResultEvent: …`

    Event representing the result of an agent tool execution.

    - `type: Literal["agent.tool_result"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `tool_use_id: str`

      The id of the `agent.tool_use` event this result corresponds to.

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadMessageReceivedEvent: …`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `type: Literal["agent.thread_message_received"]`

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock: …`

        Placeholder for content withheld by Anthropic model policy.

    - `from_session_thread_id: str`

      Public `sthr_` ID of the thread that sent the message.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `from_agent_name: Optional[str]`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class BetaManagedAgentsAgentThreadMessageSentEvent: …`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `type: Literal["agent.thread_message_sent"]`

    - `id: str`

      Unique identifier for this event.

    - `content: List[Content]`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock: …`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `to_session_thread_id: str`

      Public `sthr_` ID of the thread the message was sent to.

    - `to_agent_name: Optional[str]`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent: …`

    Indicates that context compaction (summarization) occurred during the session.

    - `type: Literal["agent.thread_context_compacted"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionErrorEvent: …`

    An error event indicating a problem occurred during session execution.

    - `type: Literal["session.error"]`

    - `id: str`

      Unique identifier for this event.

    - `error: Error`

      - `class BetaManagedAgentsUnknownError: …`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `type: Literal["unknown_error"]`

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: Literal["retrying"]`

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: Literal["exhausted"]`

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: Literal["terminal"]`

      - `class BetaManagedAgentsModelOverloadedError: …`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `type: Literal["model_overloaded_error"]`

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

      - `class BetaManagedAgentsModelRateLimitedError: …`

        The model request was rate-limited.

        - `type: Literal["model_rate_limited_error"]`

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

      - `class BetaManagedAgentsModelRequestFailedError: …`

        A model request failed for a reason other than overload or rate-limiting.

        - `type: Literal["model_request_failed_error"]`

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

      - `class BetaManagedAgentsMCPConnectionFailedError: …`

        Failed to connect to an MCP server.

        - `type: Literal["mcp_connection_failed_error"]`

        - `mcp_server_name: str`

          Name of the MCP server that failed to connect.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

      - `class BetaManagedAgentsMCPAuthenticationFailedError: …`

        Authentication to an MCP server failed.

        - `type: Literal["mcp_authentication_failed_error"]`

        - `mcp_server_name: str`

          Name of the MCP server that failed authentication.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

      - `class BetaManagedAgentsBillingError: …`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `type: Literal["billing_error"]`

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

      - `class BetaManagedAgentsCredentialHostUnreachableError: …`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `type: Literal["credential_host_unreachable_error"]`

        - `credential_id: str`

          ID of the affected credential.

        - `message: str`

          Human-readable error description.

        - `retry_status: RetryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying: …`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted: …`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal: …`

            The session encountered a terminal error and will transition to `terminated` state.

        - `vault_id: str`

          ID of the vault containing the affected credential.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionStatusRescheduledEvent: …`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `type: Literal["session.status_rescheduled"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionStatusRunningEvent: …`

    Indicates the session is actively running and the agent is working.

    - `type: Literal["session.status_running"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionStatusIdleEvent: …`

    Indicates the agent has paused and is awaiting user input.

    - `type: Literal["session.status_idle"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `stop_reason: StopReason`

      - `class BetaManagedAgentsSessionEndTurn: …`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: Literal["end_turn"]`

      - `class BetaManagedAgentsSessionRequiresAction: …`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `type: Literal["requires_action"]`

        - `event_ids: List[str]`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

      - `class BetaManagedAgentsSessionRetriesExhausted: …`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `type: Literal["retries_exhausted"]`

      - `class BetaManagedAgentsSessionBudgetReached: …`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `type: Literal["budget_reached"]`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent: …`

    Indicates the session has terminated, either due to an error or completion.

    - `type: Literal["session.status_terminated"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionThreadCreatedEvent: …`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `type: Literal["session.thread_created"]`

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the callable agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: str`

      Public `sthr_` ID of the newly created thread.

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent: …`

    Emitted when an outcome evaluation cycle begins.

    - `type: Literal["span.outcome_evaluation_start"]`

    - `id: str`

      Unique identifier for this event.

    - `iteration: int`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

      format: int32

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent: …`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `type: Literal["span.outcome_evaluation_end"]`

    - `id: str`

      Unique identifier for this event.

    - `explanation: str`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `iteration: int`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `outcome_evaluation_start_id: str`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `result: str`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

      - `cache_creation_input_tokens: int`

        Tokens used to create prompt cache in this request.

        format: int32

      - `cache_read_input_tokens: int`

        Tokens read from prompt cache in this request.

        format: int32

      - `input_tokens: int`

        Input tokens consumed by this request.

        format: int32

      - `output_tokens: int`

        Output tokens generated by this request.

        format: int32

      - `speed: Optional[Literal["standard", "fast"]]`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `class BetaManagedAgentsSpanModelRequestStartEvent: …`

    Emitted when a model request is initiated by the agent.

    - `type: Literal["span.model_request_start"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSpanModelRequestEndEvent: …`

    Emitted when a model request completes.

    - `type: Literal["span.model_request_end"]`

    - `id: str`

      Unique identifier for this event.

    - `is_error: Optional[bool]`

      Whether the model request resulted in an error.

    - `model_request_start_id: str`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: BetaManagedAgentsSpanModelUsage`

      Token usage for a single model request.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent: …`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `type: Literal["span.outcome_evaluation_ongoing"]`

    - `id: str`

      Unique identifier for this event.

    - `iteration: int`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `outcome_id: str`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsUserDefineOutcomeEvent: …`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `type: Literal["user.define_outcome"]`

    - `id: str`

      Unique identifier for this event.

    - `description: str`

      What the agent should produce. Copied from the input event.

    - `max_iterations: Optional[int]`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

      format: int32

    - `outcome_id: str`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `rubric: Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric: …`

        Rubric referenced by a file uploaded via the Files API.

        - `type: Literal["file"]`

        - `file_id: str`

          ID of the rubric file.

      - `class BetaManagedAgentsTextRubric: …`

        Rubric content provided inline as text.

        - `type: Literal["text"]`

        - `content: str`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

  - `class BetaManagedAgentsSessionDeletedEvent: …`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `type: Literal["session.deleted"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent: …`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: Literal["session.thread_status_running"]`

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: str`

      Public sthr_ ID of the thread that started running.

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent: …`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: Literal["session.thread_status_idle"]`

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: str`

      Public sthr_ ID of the thread that went idle.

    - `stop_reason: StopReason`

      - `class BetaManagedAgentsSessionEndTurn: …`

        The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionRequiresAction: …`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `class BetaManagedAgentsSessionRetriesExhausted: …`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `class BetaManagedAgentsSessionBudgetReached: …`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent: …`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: Literal["session.thread_status_terminated"]`

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: str`

      Public sthr_ ID of the thread that terminated.

  - `class BetaManagedAgentsUserToolResultEvent: …`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `type: Literal["user.tool_result"]`

    - `id: str`

      Unique identifier for this event.

    - `tool_use_id: str`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `content: Optional[List[Content]]`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock: …`

        Regular text content.

      - `class BetaManagedAgentsImageBlock: …`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock: …`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock: …`

        A block containing a web search result.

    - `is_error: Optional[bool]`

      Whether the tool execution resulted in an error.

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: Optional[str]`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent: …`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `type: Literal["session.thread_status_rescheduled"]`

    - `id: str`

      Unique identifier for this event.

    - `agent_name: str`

      Name of the agent the thread runs.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: str`

      Public sthr_ ID of the thread that is retrying.

  - `class BetaManagedAgentsSessionUpdatedEvent: …`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `type: Literal["session.updated"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `agent: Optional[BetaManagedAgentsSessionAgent]`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `type: Literal["agent"]`

      - `id: str`

      - `description: Optional[str]`

      - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

        - `type: Literal["url"]`

        - `name: str`

        - `url: str`

      - `model: BetaManagedAgentsModelConfig`

        Model identifier and configuration.

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `Literal["claude-fable-5-1", "claude-sonnet-5", "claude-fable-5", 11 more]`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `claude-fable-5-1` - Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows
            - `claude-sonnet-5` - High-performance model for coding and agents
            - `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
            - `claude-opus-5` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-8` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-7` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-6` - Powerful intelligence for long-running agents and coding
            - `claude-sonnet-4-6` - Best combination of speed and intelligence
            - `claude-haiku-4-5` - Fastest model with near-frontier intelligence
            - `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
            - `claude-opus-4-5` - Powerful intelligence for long-running agents and coding
            - `claude-opus-4-5-20251101` - Powerful intelligence for long-running agents and coding
            - `claude-sonnet-4-5` - High-performance model for agents and coding
            - `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

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

          - `str`

        - `effort: Optional[Effort]`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow: …`

            Low effort. Favors latency over reasoning depth.

            - `type: Literal["low"]`

          - `class BetaManagedAgentsEffortMedium: …`

            Medium effort. Balances latency and reasoning depth.

            - `type: Literal["medium"]`

          - `class BetaManagedAgentsEffortHigh: …`

            High effort. Favors reasoning depth.

            - `type: Literal["high"]`

          - `class BetaManagedAgentsEffortXhigh: …`

            Extra-high effort. Not all models accept this level.

            - `type: Literal["xhigh"]`

          - `class BetaManagedAgentsEffortMax: …`

            Maximum effort. Favors reasoning depth over latency.

            - `type: Literal["max"]`

        - `inference_geo: Optional[str]`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `speed: Optional[Literal["standard", "fast"]]`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

      - `multiagent: Optional[BetaManagedAgentsSessionMultiagentCoordinator]`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `type: Literal["coordinator"]`

        - `agents: List[Agent]`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `class BetaManagedAgentsSessionThreadAgent: …`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `type: Literal["agent"]`

            - `id: str`

            - `description: Optional[str]`

            - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

              - `type: Literal["url"]`

              - `name: str`

              - `url: str`

            - `model: BetaManagedAgentsModelConfig`

              Model identifier and configuration.

            - `name: str`

            - `skills: List[Skill]`

              - `class BetaManagedAgentsAnthropicSkill: …`

                A resolved Anthropic-managed skill.

                - `type: Literal["anthropic"]`

                - `skill_id: str`

                - `version: str`

              - `class BetaManagedAgentsCustomSkill: …`

                A resolved user-created custom skill.

                - `type: Literal["custom"]`

                - `skill_id: str`

                - `version: str`

            - `system: Optional[str]`

            - `tools: List[Tool]`

              - `class BetaManagedAgentsAgentToolset20260401: …`

                - `type: Literal["agent_toolset_20260401"]`

                - `configs: List[BetaManagedAgentsAgentToolConfig]`

                  - `class BetaManagedAgentsBashToolConfig: …`

                    Configuration for the bash tool.

                    - `type: Literal["bash"]`

                    - `enabled: bool`

                    - `name: Literal["bash"]`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                        - `type: Literal["always_allow"]`

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                        - `type: Literal["always_ask"]`

                      - `class BetaManagedAgentsAutoPolicy: …`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                        - `type: Literal["auto"]`

                  - `class BetaManagedAgentsEditToolConfig: …`

                    Configuration for the edit tool.

                    - `type: Literal["edit"]`

                    - `enabled: bool`

                    - `name: Literal["edit"]`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                      - `class BetaManagedAgentsAutoPolicy: …`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `class BetaManagedAgentsReadToolConfig: …`

                    Configuration for the read tool.

                    - `type: Literal["read"]`

                    - `enabled: bool`

                    - `name: Literal["read"]`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                      - `class BetaManagedAgentsAutoPolicy: …`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `class BetaManagedAgentsWriteToolConfig: …`

                    Configuration for the write tool.

                    - `type: Literal["write"]`

                    - `enabled: bool`

                    - `name: Literal["write"]`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                      - `class BetaManagedAgentsAutoPolicy: …`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `class BetaManagedAgentsGlobToolConfig: …`

                    Configuration for the glob tool.

                    - `type: Literal["glob"]`

                    - `enabled: bool`

                    - `name: Literal["glob"]`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                      - `class BetaManagedAgentsAutoPolicy: …`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `class BetaManagedAgentsGrepToolConfig: …`

                    Configuration for the grep tool.

                    - `type: Literal["grep"]`

                    - `enabled: bool`

                    - `name: Literal["grep"]`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                      - `class BetaManagedAgentsAutoPolicy: …`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                  - `class BetaManagedAgentsWebFetchToolConfig: …`

                    Configuration for the web_fetch tool.

                    - `type: Literal["web_fetch"]`

                    - `enabled: bool`

                    - `name: Literal["web_fetch"]`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                      - `class BetaManagedAgentsAutoPolicy: …`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `allowed_domains: Optional[List[str]]`

                    - `blocked_domains: Optional[List[str]]`

                    - `max_content_tokens: Optional[int]`

                      format: int32

                  - `class BetaManagedAgentsWebSearchToolConfig: …`

                    Configuration for the web_search tool.

                    - `type: Literal["web_search"]`

                    - `enabled: bool`

                    - `name: Literal["web_search"]`

                    - `permission_policy: PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy: …`

                        Tool calls require user confirmation before execution.

                      - `class BetaManagedAgentsAutoPolicy: …`

                        The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                    - `allowed_domains: Optional[List[str]]`

                    - `blocked_domains: Optional[List[str]]`

                    - `user_location: Optional[BetaManagedAgentsUserLocation]`

                      Approximate user location for search result localization.

                      - `type: Literal["approximate"]`

                        Location precision. Only "approximate" is supported.

                      - `city: Optional[str]`

                        City name.

                        minLength: 1, maxLength: 255

                      - `country: Optional[str]`

                        Two-letter ISO 3166-1 country code, uppercase.

                      - `region: Optional[str]`

                        Region or state name.

                        minLength: 1, maxLength: 255

                      - `timezone: Optional[str]`

                        IANA timezone identifier, e.g. "America/Los_Angeles".

                        minLength: 1, maxLength: 255

                - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

                  Resolved default configuration for agent tools.

                  - `enabled: bool`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

              - `class BetaManagedAgentsMCPToolset: …`

                - `type: Literal["mcp_toolset"]`

                - `configs: List[BetaManagedAgentsMCPToolConfig]`

                  - `enabled: bool`

                  - `name: str`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `enabled: bool`

                  - `permission_policy: PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy: …`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy: …`

                      Tool calls require user confirmation before execution.

                    - `class BetaManagedAgentsAutoPolicy: …`

                      The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

                - `mcp_server_name: str`

              - `class BetaManagedAgentsCustomTool: …`

                A custom tool as returned in API responses.

                - `type: Literal["custom"]`

                - `description: str`

                - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                  JSON Schema for custom tool input parameters.

                  - `type: Literal["object"]`

                  - `properties: Optional[Dict[str, object]]`

                  - `required: Optional[List[str]]`

                - `name: str`

            - `version: int`

              format: int32

          - `class BetaManagedAgentsAdvisor: …`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `type: Literal["advisor"]`

            - `model: str`

              The advisor model id.

      - `name: str`

      - `skills: List[Skill]`

        - `class BetaManagedAgentsAnthropicSkill: …`

          A resolved Anthropic-managed skill.

        - `class BetaManagedAgentsCustomSkill: …`

          A resolved user-created custom skill.

      - `system: Optional[str]`

      - `tools: List[Tool]`

        - `class BetaManagedAgentsAgentToolset20260401: …`

        - `class BetaManagedAgentsMCPToolset: …`

        - `class BetaManagedAgentsCustomTool: …`

          A custom tool as returned in API responses.

      - `version: int`

        format: int32

    - `budget: Optional[BetaManagedAgentsBudgetLimit]`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `type: Literal["limit"]`

      - `max_list_cost: BetaMonetaryAmount`

        A monetary amount in a specific currency.

        - `amount: str`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `currency: BetaCurrency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `metadata: Optional[Dict[str, str]]`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title: Optional[str]`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsStartEvent: …`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `type: Literal["event_start"]`

    - `event: BetaManagedAgentsStartEventPreview`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

      - `class BetaManagedAgentsAgentMessagePreview: …`

        - `type: Literal["agent.message"]`

        - `id: str`

          The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

      - `class BetaManagedAgentsAgentThinkingPreview: …`

        - `type: Literal["agent.thinking"]`

        - `id: str`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

  - `class BetaManagedAgentsDeltaEvent: …`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `type: Literal["event_delta"]`

    - `delta: BetaManagedAgentsDeltaContent`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `type: Literal["content_delta"]`

      - `content: BetaManagedAgentsTextBlock`

        Regular text content.

      - `index: Optional[int]`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

        format: uint32

    - `event_id: str`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

  - `class BetaManagedAgentsSystemMessageEvent: …`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `type: Literal["system.message"]`

    - `id: str`

      Unique identifier for this event.

    - `content: List[BetaManagedAgentsSystemContentBlock]`

      System content blocks. Text-only.

      - `type: Literal["text"]`

      - `text: str`

        The text content.

        minLength: 1

    - `processed_at: Optional[datetime]`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionUsageEvent: …`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `type: Literal["session.usage"]`

    - `id: str`

      Unique identifier for this event.

    - `processed_at: datetime`

      A timestamp in RFC 3339 format

      format: date-time

    - `usage: BetaManagedAgentsSessionUsageSnapshot`

      Point-in-time snapshot of a session's cumulative usage.

      - `active_seconds: Optional[float]`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `cache_creation: Optional[BetaManagedAgentsCacheCreationUsage]`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `ephemeral_1h_input_tokens: Optional[int]`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `ephemeral_5m_input_tokens: Optional[int]`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `cache_read_input_tokens: Optional[int]`

        Total tokens read from prompt cache.

        format: int32

      - `input_tokens: Optional[int]`

        Total input tokens consumed across all turns.

        format: int32

      - `list_cost: Optional[BetaMonetaryAmount]`

        A monetary amount in a specific currency.

      - `output_tokens: Optional[int]`

        Total output tokens generated across all turns.

        format: int32

      - `server_tool_use: Optional[BetaManagedAgentsServerToolUsage]`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `web_fetch_requests: Optional[int]`

          Number of server-executed web fetch requests.

          format: int32

        - `web_search_requests: Optional[int]`

          Number of server-executed web search requests.

          format: int32

    - `budget: Optional[BetaManagedAgentsBudgetLimit]`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

#### Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
for event in client.beta.sessions.threads.events.stream(
    thread_id="sthr_011CZkZVWa6oIjw0rgXZpnBt",
    session_id="sesn_011CZkZAtmR3yMPDzynEDxu7",
):
    print(event)
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
