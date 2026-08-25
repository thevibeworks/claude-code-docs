---
title: Create Session
url: https://platform.claude.com/docs/en/api/ruby/beta/sessions/create
---

## Create Session

`beta.sessions.create(**kwargs) -> BetaManagedAgentsSession`

**post** `/v1/sessions`

Create Session

### Parameters

- `agent: String | BetaManagedAgentsAgentParams | BetaManagedAgentsAgentWithOverridesParams`

  Agent identifier. Accepts the `agent` ID string, which pins the latest version for the session, or an `agent` object with both id and version specified.

  - `String = String`

  - `class BetaManagedAgentsAgentParams`

    Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

    - `id: String`

      The `agent` ID.

    - `type: :agent`

      - `:agent`

    - `version: Integer`

      The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

  - `class BetaManagedAgentsAgentWithOverridesParams`

    Reference to an `agent` plus optional configuration overrides. Each provided field replaces the agent's value for the caller's use; the agent resource is unchanged.

    - `id: String`

      The `agent` ID.

    - `type: :agent_with_overrides`

      - `:agent_with_overrides`

    - `mcp_servers: Array[BetaManagedAgentsURLMCPServerParams]`

      Replacement MCP server list. Full replacement: the provided array becomes the MCP servers. Send an empty array to clear; omit to preserve the agent's servers.

      - `name: String`

        Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

      - `type: :url`

        - `:url`

      - `url: String`

        Endpoint URL for the MCP server.

    - `model: BetaManagedAgentsModel | BetaManagedAgentsModelConfigParams`

      Replacement model. Accepts the model string, e.g. `claude-opus-5`, or a `model_config` object. Omit to use the agent's model.

      - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-5" | 10 more | String`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-5" | 10 more`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `:"claude-sonnet-5"`

            High-performance model for coding and agents

          - `:"claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `:"claude-opus-5"`

            Powerful intelligence for long-running agents and coding

          - `:"claude-opus-4-8"`

            Powerful intelligence for long-running agents and coding

          - `:"claude-opus-4-7"`

            Powerful intelligence for long-running agents and coding

          - `:"claude-opus-4-6"`

            Powerful intelligence for long-running agents and coding

          - `:"claude-sonnet-4-6"`

            Best combination of speed and intelligence

          - `:"claude-haiku-4-5"`

            Fastest model with near-frontier intelligence

          - `:"claude-haiku-4-5-20251001"`

            Fastest model with near-frontier intelligence

          - `:"claude-opus-4-5"`

            Powerful intelligence for long-running agents and coding

          - `:"claude-opus-4-5-20251101"`

            Powerful intelligence for long-running agents and coding

          - `:"claude-sonnet-4-5"`

            High-performance model for agents and coding

          - `:"claude-sonnet-4-5-20250929"`

            High-performance model for agents and coding

        - `String = String`

      - `class BetaManagedAgentsModelConfigParams`

        An object that defines additional configuration control over model use

        - `id: BetaManagedAgentsModel`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `effort: :low | :medium | :high | 2 more | BetaManagedAgentsEffortLow | BetaManagedAgentsEffortMedium | 3 more`

          How hard Claude works on each inference call. Accepts a bare level string (`"high"`) or `{"type": "high"}`. On create, omitting it resolves the per-model default; on update, omitting it leaves the stored value unchanged.

          - `BetaManagedAgentsEffortLevel = :low | :medium | :high | 2 more`

            How hard Claude works on each turn. Higher levels favor reasoning depth over latency. Not all models accept every level; invalid combinations are rejected at create time.

            - `:low`

            - `:medium`

            - `:high`

            - `:xhigh`

            - `:max`

          - `class BetaManagedAgentsEffortLow`

            Low effort. Favors latency over reasoning depth.

            - `type: :low`

              - `:low`

          - `class BetaManagedAgentsEffortMedium`

            Medium effort. Balances latency and reasoning depth.

            - `type: :medium`

              - `:medium`

          - `class BetaManagedAgentsEffortHigh`

            High effort. Favors reasoning depth.

            - `type: :high`

              - `:high`

          - `class BetaManagedAgentsEffortXhigh`

            Extra-high effort. Not all models accept this level.

            - `type: :xhigh`

              - `:xhigh`

          - `class BetaManagedAgentsEffortMax`

            Maximum effort. Favors reasoning depth over latency.

            - `type: :max`

              - `:max`

        - `inference_geo: String`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo. On update, `model` is whole-object replacement — omitting inference_geo clears it.

        - `speed: :standard | :fast`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `:standard`

          - `:fast`

    - `skills: Array[BetaManagedAgentsSkillParams]`

      Replacement skill list. Full replacement: the provided array becomes the skills. Send an empty array to clear; omit to preserve the agent's skills.

      - `class BetaManagedAgentsAnthropicSkillParams`

        An Anthropic-managed skill.

        - `skill_id: String`

          Identifier of the Anthropic skill (e.g., "xlsx").

        - `type: :anthropic`

          - `:anthropic`

        - `version: String`

          Version to pin. Defaults to latest if omitted.

      - `class BetaManagedAgentsCustomSkillParams`

        A user-created custom skill.

        - `skill_id: String`

          Tagged ID of the custom skill (e.g., "skill_01XJ5...").

        - `type: :custom`

          - `:custom`

        - `version: String`

          Version to pin. Defaults to latest if omitted.

    - `system_: String`

      Replacement system prompt. Up to 100,000 characters. Set to null to clear the agent's system prompt; omit to preserve it.

    - `tools: Array[BetaManagedAgentsAgentToolset20260401Params | BetaManagedAgentsMCPToolsetParams | BetaManagedAgentsCustomToolParams]`

      Replacement tool list. Full replacement: the provided array becomes the tool configuration. Send an empty array to clear; omit to preserve the agent's tools.

      - `class BetaManagedAgentsAgentToolset20260401Params`

        Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

        - `type: :agent_toolset_20260401`

          - `:agent_toolset_20260401`

        - `configs: Array[BetaManagedAgentsAgentToolConfigParams]`

          Per-tool configuration overrides.

          - `class BetaManagedAgentsBashToolConfigParams`

            Configuration override for the bash tool.

            - `name: :bash`

              Must be "bash".

              - `:bash`

            - `enabled: bool`

              Whether this tool is enabled and available to Claude. Overrides the default_config setting.

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy`

                Tool calls are automatically approved without user confirmation.

                - `type: :always_allow`

                  - `:always_allow`

              - `class BetaManagedAgentsAlwaysAskPolicy`

                Tool calls require user confirmation before execution.

                - `type: :always_ask`

                  - `:always_ask`

            - `type: :bash`

              - `:bash`

          - `class BetaManagedAgentsEditToolConfigParams`

            Configuration override for the edit tool.

            - `name: :edit`

              Must be "edit".

              - `:edit`

            - `enabled: bool`

              Whether this tool is enabled and available to Claude. Overrides the default_config setting.

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy`

                Tool calls require user confirmation before execution.

            - `type: :edit`

              - `:edit`

          - `class BetaManagedAgentsReadToolConfigParams`

            Configuration override for the read tool.

            - `name: :read`

              Must be "read".

              - `:read`

            - `enabled: bool`

              Whether this tool is enabled and available to Claude. Overrides the default_config setting.

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy`

                Tool calls require user confirmation before execution.

            - `type: :read`

              - `:read`

          - `class BetaManagedAgentsWriteToolConfigParams`

            Configuration override for the write tool.

            - `name: :write`

              Must be "write".

              - `:write`

            - `enabled: bool`

              Whether this tool is enabled and available to Claude. Overrides the default_config setting.

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy`

                Tool calls require user confirmation before execution.

            - `type: :write`

              - `:write`

          - `class BetaManagedAgentsGlobToolConfigParams`

            Configuration override for the glob tool.

            - `name: :glob`

              Must be "glob".

              - `:glob`

            - `enabled: bool`

              Whether this tool is enabled and available to Claude. Overrides the default_config setting.

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy`

                Tool calls require user confirmation before execution.

            - `type: :glob`

              - `:glob`

          - `class BetaManagedAgentsGrepToolConfigParams`

            Configuration override for the grep tool.

            - `name: :grep`

              Must be "grep".

              - `:grep`

            - `enabled: bool`

              Whether this tool is enabled and available to Claude. Overrides the default_config setting.

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy`

                Tool calls require user confirmation before execution.

            - `type: :grep`

              - `:grep`

          - `class BetaManagedAgentsWebFetchToolConfigParams`

            Configuration override for the web_fetch tool.

            - `name: :web_fetch`

              Must be "web_fetch".

              - `:web_fetch`

            - `allowed_domains: Array[String]`

              Only fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

            - `blocked_domains: Array[String]`

              Never fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

            - `enabled: bool`

              Whether this tool is enabled and available to Claude. Overrides the default_config setting.

            - `max_content_tokens: Integer`

              Maximum number of tokens of fetched text content to include in context per call. Does not apply to binary content such as PDFs.

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy`

                Tool calls require user confirmation before execution.

            - `type: :web_fetch`

              - `:web_fetch`

          - `class BetaManagedAgentsWebSearchToolConfigParams`

            Configuration override for the web_search tool.

            - `name: :web_search`

              Must be "web_search".

              - `:web_search`

            - `allowed_domains: Array[String]`

              Only return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

            - `blocked_domains: Array[String]`

              Never return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

            - `enabled: bool`

              Whether this tool is enabled and available to Claude. Overrides the default_config setting.

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy`

                Tool calls require user confirmation before execution.

            - `type: :web_search`

              - `:web_search`

            - `user_location: BetaManagedAgentsUserLocation`

              Approximate user location for search result localization.

              - `type: :approximate`

                Location precision. Only "approximate" is supported.

                - `:approximate`

              - `city: String`

                City name.

              - `country: String`

                Two-letter ISO 3166-1 country code, uppercase.

              - `region: String`

                Region or state name.

              - `timezone: String`

                IANA timezone identifier, e.g. "America/Los_Angeles".

        - `default_config: BetaManagedAgentsAgentToolsetDefaultConfigParams`

          Default configuration for all tools in a toolset.

          - `enabled: bool`

            Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

      - `class BetaManagedAgentsMCPToolsetParams`

        Configuration for tools from an MCP server defined in `mcp_servers`.

        - `mcp_server_name: String`

          Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

        - `type: :mcp_toolset`

          - `:mcp_toolset`

        - `configs: Array[BetaManagedAgentsMCPToolConfigParams]`

          Per-tool configuration overrides.

          - `name: String`

            Name of the MCP tool to configure. 1-128 characters.

          - `enabled: bool`

            Whether this tool is enabled. Overrides the `default_config` setting.

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

        - `default_config: BetaManagedAgentsMCPToolsetDefaultConfigParams`

          Default configuration for all tools from an MCP server.

          - `enabled: bool`

            Whether tools are enabled by default. Defaults to true if not specified.

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

      - `class BetaManagedAgentsCustomToolParams`

        A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

        - `description: String`

          Description of what the tool does, shown to the agent to help it decide when to use the tool.

        - `input_schema: BetaManagedAgentsCustomToolInputSchema`

          JSON Schema for custom tool input parameters.

          - `type: :object`

            - `:object`

          - `properties: Hash[Symbol, untyped]`

          - `required: Array[String]`

        - `name: String`

          Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

        - `type: :custom`

          - `:custom`

    - `version: Integer`

      The specific `agent` version to use. Omit to use the latest version.

- `environment_id: String`

  ID of the `environment` defining the container configuration for this session.

- `budget: BetaManagedAgentsBudgetLimit`

  A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

  - `max_list_cost: BetaMonetaryAmount`

    A monetary amount in a specific currency.

    - `amount: String`

      Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

    - `currency: BetaCurrency`

      Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `:USD`

  - `type: :limit`

    - `:limit`

- `initial_events: Array[BetaManagedAgentsUserMessageEventParams | BetaManagedAgentsUserDefineOutcomeEventParams]`

  Initial events to send to the `session` at creation, processed in order. Supports `user.message` and `user.define_outcome` events. Maximum 50 events.

  - `class BetaManagedAgentsUserMessageEventParams`

    Parameters for sending a user message to the session.

    - `content: Array[BetaManagedAgentsTextBlock | BetaManagedAgentsImageBlock | BetaManagedAgentsDocumentBlock | BetaManagedAgentsRedactedBlock]`

      Array of content blocks for the user message.

      - `class BetaManagedAgentsTextBlock`

        Regular text content.

        - `text: String`

          The text content.

        - `type: :text`

          - `:text`

      - `class BetaManagedAgentsImageBlock`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource | BetaManagedAgentsURLImageSource | BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource`

            Base64-encoded image data.

            - `data: String`

              Base64-encoded image data.

            - `media_type: String`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsURLImageSource`

            Image referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the image to fetch.

          - `class BetaManagedAgentsFileImageSource`

            Image referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :image`

          - `:image`

      - `class BetaManagedAgentsDocumentBlock`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource | BetaManagedAgentsPlainTextDocumentSource | BetaManagedAgentsURLDocumentSource | BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource`

            Base64-encoded document data.

            - `data: String`

              Base64-encoded document data.

            - `media_type: String`

              MIME type of the document (e.g., "application/pdf").

            - `type: :base64`

              - `:base64`

          - `class BetaManagedAgentsPlainTextDocumentSource`

            Plain text document content.

            - `data: String`

              The plain text content.

            - `media_type: :"text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `:"text/plain"`

            - `type: :text`

              - `:text`

          - `class BetaManagedAgentsURLDocumentSource`

            Document referenced by URL.

            - `type: :url`

              - `:url`

            - `url: String`

              URL of the document to fetch.

          - `class BetaManagedAgentsFileDocumentSource`

            Document referenced by file ID.

            - `file_id: String`

              ID of a previously uploaded file.

            - `type: :file`

              - `:file`

        - `type: :document`

          - `:document`

        - `context: String`

          Additional context about the document for the model.

        - `title: String`

          The title of the document.

      - `class BetaManagedAgentsRedactedBlock`

        Placeholder for content withheld by Anthropic model policy.

        - `type: :redacted`

          - `:redacted`

    - `type: :"user.message"`

      - `:"user.message"`

  - `class BetaManagedAgentsUserDefineOutcomeEventParams`

    Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

    - `description: String`

      What the agent should produce. This is the task specification.

    - `rubric: BetaManagedAgentsFileRubricParams | BetaManagedAgentsTextRubricParams`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubricParams`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: String`

          ID of the rubric file.

        - `type: :file`

          - `:file`

      - `class BetaManagedAgentsTextRubricParams`

        Rubric content provided inline as text.

        - `content: String`

          Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

        - `type: :text`

          - `:text`

    - `type: :"user.define_outcome"`

      - `:"user.define_outcome"`

    - `max_iterations: Integer`

      Eval→revision cycles before giving up. Default 3, max 20.

- `metadata: Hash[Symbol, String]`

  Arbitrary key-value metadata attached to the session. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `resources: Array[BetaManagedAgentsGitHubRepositoryResourceParams | BetaManagedAgentsFileResourceParams | BetaManagedAgentsMemoryStoreResourceParam]`

  Resources (e.g. repositories, files) to mount into the session's container.

  - `class BetaManagedAgentsGitHubRepositoryResourceParams`

    Mount a GitHub repository into the session's container.

    - `authorization_token: String`

      GitHub authorization token used to clone the repository.

    - `type: :github_repository`

      - `:github_repository`

    - `url: String`

      Github URL of the repository

    - `checkout: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout`

      Branch or commit to check out. Defaults to the repository's default branch.

      - `class BetaManagedAgentsBranchCheckout`

        - `name: String`

          Branch name to check out.

        - `type: :branch`

          - `:branch`

      - `class BetaManagedAgentsCommitCheckout`

        - `sha: String`

          Full commit SHA to check out.

        - `type: :commit`

          - `:commit`

    - `mount_path: String`

      Mount path in the container. Defaults to `/workspace/<repo-name>`.

  - `class BetaManagedAgentsFileResourceParams`

    Mount a file uploaded via the Files API into the session.

    - `file_id: String`

      ID of a previously uploaded file.

    - `type: :file`

      - `:file`

    - `mount_path: String`

      Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

  - `class BetaManagedAgentsMemoryStoreResourceParam`

    Parameters for attaching a memory store to an agent session.

    - `memory_store_id: String`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: :memory_store`

      - `:memory_store`

    - `access: :read_write | :read_only`

      Access mode for an attached memory store.

      - `:read_write`

      - `:read_only`

    - `instructions: String`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

- `title: String`

  Human-readable session title.

- `vault_ids: Array[String]`

  Vault IDs for stored credentials the agent can use during the session.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 31 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

### Returns

- `class BetaManagedAgentsSession`

  A Managed Agents `session`.

  - `id: String`

  - `agent: BetaManagedAgentsSessionAgent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `id: String`

    - `description: String`

    - `mcp_servers: Array[BetaManagedAgentsMCPServerURLDefinition]`

      - `name: String`

      - `type: :url`

        - `:url`

      - `url: String`

    - `model: BetaManagedAgentsModelConfig`

      Model identifier and configuration.

      - `id: BetaManagedAgentsModel`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `BetaManagedAgentsModel = :"claude-sonnet-5" | :"claude-fable-5" | :"claude-opus-5" | 10 more`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `:"claude-sonnet-5"`

            High-performance model for coding and agents

          - `:"claude-fable-5"`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `:"claude-opus-5"`

            Powerful intelligence for long-running agents and coding

          - `:"claude-opus-4-8"`

            Powerful intelligence for long-running agents and coding

          - `:"claude-opus-4-7"`

            Powerful intelligence for long-running agents and coding

          - `:"claude-opus-4-6"`

            Powerful intelligence for long-running agents and coding

          - `:"claude-sonnet-4-6"`

            Best combination of speed and intelligence

          - `:"claude-haiku-4-5"`

            Fastest model with near-frontier intelligence

          - `:"claude-haiku-4-5-20251001"`

            Fastest model with near-frontier intelligence

          - `:"claude-opus-4-5"`

            Powerful intelligence for long-running agents and coding

          - `:"claude-opus-4-5-20251101"`

            Powerful intelligence for long-running agents and coding

          - `:"claude-sonnet-4-5"`

            High-performance model for agents and coding

          - `:"claude-sonnet-4-5-20250929"`

            High-performance model for agents and coding

        - `String = String`

      - `effort: BetaManagedAgentsEffortLow | BetaManagedAgentsEffortMedium | BetaManagedAgentsEffortHigh | 2 more`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

        - `class BetaManagedAgentsEffortLow`

          Low effort. Favors latency over reasoning depth.

          - `type: :low`

            - `:low`

        - `class BetaManagedAgentsEffortMedium`

          Medium effort. Balances latency and reasoning depth.

          - `type: :medium`

            - `:medium`

        - `class BetaManagedAgentsEffortHigh`

          High effort. Favors reasoning depth.

          - `type: :high`

            - `:high`

        - `class BetaManagedAgentsEffortXhigh`

          Extra-high effort. Not all models accept this level.

          - `type: :xhigh`

            - `:xhigh`

        - `class BetaManagedAgentsEffortMax`

          Maximum effort. Favors reasoning depth over latency.

          - `type: :max`

            - `:max`

      - `inference_geo: String`

        Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

      - `speed: :standard | :fast`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `:standard`

        - `:fast`

    - `multiagent: BetaManagedAgentsSessionMultiagentCoordinator`

      Resolved coordinator topology with full agent definitions for each roster member.

      - `agents: Array[BetaManagedAgentsSessionThreadAgent | BetaManagedAgentsAdvisor]`

        Full `agent` definitions the coordinator may spawn as session threads.

        - `class BetaManagedAgentsSessionThreadAgent`

          Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

          - `id: String`

          - `description: String`

          - `mcp_servers: Array[BetaManagedAgentsMCPServerURLDefinition]`

            - `name: String`

            - `type: :url`

            - `url: String`

          - `model: BetaManagedAgentsModelConfig`

            Model identifier and configuration.

          - `name: String`

          - `skills: Array[BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill]`

            - `class BetaManagedAgentsAnthropicSkill`

              A resolved Anthropic-managed skill.

              - `skill_id: String`

              - `type: :anthropic`

                - `:anthropic`

              - `version: String`

            - `class BetaManagedAgentsCustomSkill`

              A resolved user-created custom skill.

              - `skill_id: String`

              - `type: :custom`

                - `:custom`

              - `version: String`

          - `system_: String`

          - `tools: Array[BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool]`

            - `class BetaManagedAgentsAgentToolset20260401`

              - `configs: Array[BetaManagedAgentsAgentToolConfig]`

                - `class BetaManagedAgentsBashToolConfig`

                  Configuration for the bash tool.

                  - `enabled: bool`

                  - `name: :bash`

                    - `:bash`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                      - `type: :always_allow`

                        - `:always_allow`

                    - `class BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                      - `type: :always_ask`

                        - `:always_ask`

                  - `type: :bash`

                    - `:bash`

                - `class BetaManagedAgentsEditToolConfig`

                  Configuration for the edit tool.

                  - `enabled: bool`

                  - `name: :edit`

                    - `:edit`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                  - `type: :edit`

                    - `:edit`

                - `class BetaManagedAgentsReadToolConfig`

                  Configuration for the read tool.

                  - `enabled: bool`

                  - `name: :read`

                    - `:read`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                  - `type: :read`

                    - `:read`

                - `class BetaManagedAgentsWriteToolConfig`

                  Configuration for the write tool.

                  - `enabled: bool`

                  - `name: :write`

                    - `:write`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                  - `type: :write`

                    - `:write`

                - `class BetaManagedAgentsGlobToolConfig`

                  Configuration for the glob tool.

                  - `enabled: bool`

                  - `name: :glob`

                    - `:glob`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                  - `type: :glob`

                    - `:glob`

                - `class BetaManagedAgentsGrepToolConfig`

                  Configuration for the grep tool.

                  - `enabled: bool`

                  - `name: :grep`

                    - `:grep`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                  - `type: :grep`

                    - `:grep`

                - `class BetaManagedAgentsWebFetchToolConfig`

                  Configuration for the web_fetch tool.

                  - `enabled: bool`

                  - `name: :web_fetch`

                    - `:web_fetch`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                  - `type: :web_fetch`

                    - `:web_fetch`

                  - `allowed_domains: Array[String]`

                  - `blocked_domains: Array[String]`

                  - `max_content_tokens: Integer`

                - `class BetaManagedAgentsWebSearchToolConfig`

                  Configuration for the web_search tool.

                  - `enabled: bool`

                  - `name: :web_search`

                    - `:web_search`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                  - `type: :web_search`

                    - `:web_search`

                  - `allowed_domains: Array[String]`

                  - `blocked_domains: Array[String]`

                  - `user_location: BetaManagedAgentsUserLocation`

                    Approximate user location for search result localization.

                    - `type: :approximate`

                      Location precision. Only "approximate" is supported.

                      - `:approximate`

                    - `city: String`

                      City name.

                    - `country: String`

                      Two-letter ISO 3166-1 country code, uppercase.

                    - `region: String`

                      Region or state name.

                    - `timezone: String`

                      IANA timezone identifier, e.g. "America/Los_Angeles".

              - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

                Resolved default configuration for agent tools.

                - `enabled: bool`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy`

                    Tool calls require user confirmation before execution.

              - `type: :agent_toolset_20260401`

                - `:agent_toolset_20260401`

            - `class BetaManagedAgentsMCPToolset`

              - `configs: Array[BetaManagedAgentsMCPToolConfig]`

                - `enabled: bool`

                - `name: String`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy`

                    Tool calls require user confirmation before execution.

              - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `enabled: bool`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy`

                    Tool calls require user confirmation before execution.

              - `mcp_server_name: String`

              - `type: :mcp_toolset`

                - `:mcp_toolset`

            - `class BetaManagedAgentsCustomTool`

              A custom tool as returned in API responses.

              - `description: String`

              - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                JSON Schema for custom tool input parameters.

                - `type: :object`

                  - `:object`

                - `properties: Hash[Symbol, untyped]`

                - `required: Array[String]`

              - `name: String`

              - `type: :custom`

                - `:custom`

          - `type: :agent`

            - `:agent`

          - `version: Integer`

        - `class BetaManagedAgentsAdvisor`

          Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

          - `model: String`

            The advisor model id.

          - `type: :advisor`

            - `:advisor`

      - `type: :coordinator`

        - `:coordinator`

    - `name: String`

    - `skills: Array[BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill]`

      - `class BetaManagedAgentsAnthropicSkill`

        A resolved Anthropic-managed skill.

      - `class BetaManagedAgentsCustomSkill`

        A resolved user-created custom skill.

    - `system_: String`

    - `tools: Array[BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool]`

      - `class BetaManagedAgentsAgentToolset20260401`

      - `class BetaManagedAgentsMCPToolset`

      - `class BetaManagedAgentsCustomTool`

        A custom tool as returned in API responses.

    - `type: :agent`

      - `:agent`

    - `version: Integer`

  - `archived_at: Time`

    A timestamp in RFC 3339 format

  - `budget: BetaManagedAgentsBudgetLimit`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `max_list_cost: BetaMonetaryAmount`

      A monetary amount in a specific currency.

      - `amount: String`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

        - `:USD`

    - `type: :limit`

      - `:limit`

  - `created_at: Time`

    A timestamp in RFC 3339 format

  - `environment_id: String`

  - `metadata: Hash[Symbol, String]`

  - `outcome_evaluations: Array[BetaManagedAgentsOutcomeEvaluationResource]`

    Per-outcome evaluation state. One entry per define_outcome event sent to the session.

    - `completed_at: Time`

      A timestamp in RFC 3339 format

    - `description: String`

      What the agent should produce.

    - `explanation: String`

      Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs_revision (intermediate), what's missing; for failed, why unrecoverable.

    - `iteration: Integer`

      0-indexed revision cycle the outcome is currently on.

    - `outcome_id: String`

      Server-generated outc_ ID for this outcome.

    - `result: String`

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

    - `type: :outcome_evaluation`

      - `:outcome_evaluation`

  - `resources: Array[BetaManagedAgentsSessionResource]`

    - `class BetaManagedAgentsGitHubRepositoryResource`

      - `id: String`

      - `created_at: Time`

        A timestamp in RFC 3339 format

      - `mount_path: String`

      - `type: :github_repository`

        - `:github_repository`

      - `updated_at: Time`

        A timestamp in RFC 3339 format

      - `url: String`

      - `checkout: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout`

        - `class BetaManagedAgentsBranchCheckout`

          - `name: String`

            Branch name to check out.

          - `type: :branch`

            - `:branch`

        - `class BetaManagedAgentsCommitCheckout`

          - `sha: String`

            Full commit SHA to check out.

          - `type: :commit`

            - `:commit`

    - `class BetaManagedAgentsFileResource`

      - `id: String`

      - `created_at: Time`

        A timestamp in RFC 3339 format

      - `file_id: String`

      - `mount_path: String`

      - `type: :file`

        - `:file`

      - `updated_at: Time`

        A timestamp in RFC 3339 format

    - `class BetaManagedAgentsMemoryStoreResource`

      A memory store attached to an agent session.

      - `memory_store_id: String`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: :memory_store`

        - `:memory_store`

      - `access: :read_write | :read_only`

        Access mode for an attached memory store.

        - `:read_write`

        - `:read_only`

      - `description: String`

        Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

      - `instructions: String`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      - `mount_path: String`

        Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

      - `name: String`

        Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

  - `stats: BetaManagedAgentsSessionStats`

    Timing statistics for a session.

    - `active_seconds: Float`

      Cumulative time in seconds the session spent in running status. Excludes idle time.

    - `duration_seconds: Float`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

  - `status: :rescheduling | :running | :idle | :terminated`

    SessionStatus enum

    - `:rescheduling`

    - `:running`

    - `:idle`

    - `:terminated`

  - `title: String`

  - `type: :session`

    - `:session`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

  - `usage: BetaManagedAgentsSessionUsage`

    Cumulative token usage for a session across all turns.

    - `active_seconds: Float`

      Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once, unlike `stats.active_seconds`, which sums each thread's own active time. This is the duration the session's runtime cost is priced on.

    - `cache_creation: BetaManagedAgentsCacheCreationUsage`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: Integer`

        Tokens used to create 1-hour ephemeral cache entries.

      - `ephemeral_5m_input_tokens: Integer`

        Tokens used to create 5-minute ephemeral cache entries.

    - `cache_read_input_tokens: Integer`

      Total tokens read from prompt cache.

    - `input_tokens: Integer`

      Total input tokens consumed across all turns.

    - `list_cost: BetaMonetaryAmount`

      A monetary amount in a specific currency.

    - `output_tokens: Integer`

      Total output tokens generated across all turns.

    - `server_tool_use: BetaManagedAgentsServerToolUsage`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `web_fetch_requests: Integer`

        Number of server-executed web fetch requests.

      - `web_search_requests: Integer`

        Number of server-executed web search requests.

  - `vault_ids: Array[String]`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `deployment_id: String`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_session = anthropic.beta.sessions.create(
  agent: "agent_011CZkYpogX7uDKUyvBTophP",
  environment_id: "env_011CZkZ9X2dpNyB7HsEFoRfW"
)

puts(beta_managed_agents_session)
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
