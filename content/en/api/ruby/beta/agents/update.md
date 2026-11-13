---
title: Update Agent
url: https://platform.claude.com/docs/en/api/ruby/beta/agents/update
---

# Update Agent

`beta.agents.update(agent_id, **kwargs) -> BetaManagedAgentsAgent`

**POST** `/v1/agents/{agent_id}`

Update Agent

## Parameters

- `agent_id: String` (path parameter)

  Unique identifier of the agent to update.

- `description: optional String | nil`

  Description. Omit to preserve; send empty string or null to clear.

  maxLength: 2048

- `execution_identity: optional BetaManagedAgentsExecutionIdentityParams | nil`

  Execution principal for runs of this agent. Full replacement. Omit to preserve; send null or `{"type": "service_account"}` to restore the default.

  - `class BetaManagedAgentsAWSRoleExecutionIdentityParams`

    An AWS IAM role principal.

    - `type: :aws_role`

    - `role_arn: String`

      The IAM role's ARN, e.g. "arn:aws:iam::123456789012:role/my-agent-runner". Maximum 2048 characters.

      maxLength: 2048, pattern: ^arn:aws(-[a-z]+)*:iam::[0-9]{12}:role/[\w+=,.@/-]+$

  - `class BetaManagedAgentsServiceAccountExecutionIdentityParams`

    The Anthropic-managed service account — the default execution principal. Carries no identifier.

    - `type: :service_account`

- `mcp_servers: optional Array[BetaManagedAgentsURLMCPServerParams] | nil`

  MCP servers. Full replacement. Omit to preserve; send empty array or `null` to clear. Names must be unique. Maximum 20. Every server must be referenced by an `mcp_toolset` in the agent's resulting `tools`; unreferenced servers are rejected. See the [MCP connector guide](https://platform.claude.com/docs/en/managed-agents/mcp-connector?sdk_languages=ruby).

  - `type: :url`

  - `name: String`

    Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

    minLength: 1, maxLength: 255

  - `url: String`

    Endpoint URL for the MCP server.

    maxLength: 2048

- `metadata: optional Hash[Symbol, String | nil] | nil`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

- `model: optional BetaManagedAgentsModel | BetaManagedAgentsModelConfigParams`

  Model identifier. Accepts the [model string](https://platform.claude.com/docs/en/about-claude/models/overview?sdk_languages=ruby#latest-models-comparison), e.g. `claude-opus-5-5`, or a `model_config` object for additional configuration control. Omit to preserve. Cannot be cleared.

  - `type BetaManagedAgentsModel = :"claude-fable-5-2" | :"claude-haiku-5-5" | :"claude-sonnet-5-5" | 15 more | String`

    The model that will power your agent.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `:"claude-fable-5-2"`

      Built for the most ambitious work in coding, enterprise workflows, and the sciences

    - `:"claude-haiku-5-5"`

      Fastest model for high-volume, real-time tasks

    - `:"claude-sonnet-5-5"`

      Efficient model for coding and agents

    - `:"claude-opus-5-5"`

      Powerful intelligence for coding, knowledge work, and long-running agents

    - `:"claude-fable-5-1"`

      Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

    - `:"claude-sonnet-5"`

      Efficient model for coding and agents

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

    - `:"claude-haiku-4-5-20251001"`

    - `:"claude-opus-4-5"`

      Powerful intelligence for long-running agents and coding

    - `:"claude-opus-4-5-20251101"`

      Powerful intelligence for long-running agents and coding

    - `:"claude-sonnet-4-5"`

      **Deprecated**: Will reach end-of-life on November 30, 2026. Please migrate to claude-sonnet-5-5. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.

      High-performance model for agents and coding

    - `:"claude-sonnet-4-5-20250929"`

      **Deprecated**: Will reach end-of-life on November 30, 2026. Please migrate to claude-sonnet-5-5. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.

      High-performance model for agents and coding

    - `String = String`

  - `class BetaManagedAgentsModelConfigParams`

    An object that defines additional configuration control over model use

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `effort: optional :low | :medium | :high | 2 more | BetaManagedAgentsEffortLow | BetaManagedAgentsEffortMedium | 3 more | nil`

      How hard Claude works on each inference call. Accepts a bare level string (`"high"`) or `{"type": "high"}`. On create, omitting it resolves the per-model default; on update, omitting it leaves the stored value unchanged.

      - `BetaManagedAgentsEffortLevel = :low | :medium | :high | 2 more`

        How hard Claude works on each turn. Higher levels favor reasoning depth over latency. Not all models accept every level; invalid combinations are rejected at create time.

        - `:low`

          Low effort. Favors latency over reasoning depth.

        - `:medium`

          Medium effort. Balances latency and reasoning depth.

        - `:high`

          High effort. Favors reasoning depth.

        - `:xhigh`

          Extra-high effort. Not all models accept this level.

        - `:max`

          Maximum effort. Favors reasoning depth over latency.

      - `class BetaManagedAgentsEffortLow`

        Low effort. Favors latency over reasoning depth.

        - `type: :low`

      - `class BetaManagedAgentsEffortMedium`

        Medium effort. Balances latency and reasoning depth.

        - `type: :medium`

      - `class BetaManagedAgentsEffortHigh`

        High effort. Favors reasoning depth.

        - `type: :high`

      - `class BetaManagedAgentsEffortXhigh`

        Extra-high effort. Not all models accept this level.

        - `type: :xhigh`

      - `class BetaManagedAgentsEffortMax`

        Maximum effort. Favors reasoning depth over latency.

        - `type: :max`

    - `inference_geo: optional String | nil`

      Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo. On update, `model` is whole-object replacement — omitting inference_geo clears it.

    - `speed: optional :standard | :fast | nil`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Defaults to `standard`. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

- `multiagent: optional BetaManagedAgentsMultiagentParams | nil`

  Multiagent orchestration configuration. Full replacement. Omit to preserve; send null to clear.

  - `class BetaManagedAgentsMultiagentCoordinatorParams`

    A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.

    - `type: :coordinator`

    - `agents: Array[BetaManagedAgentsMultiagentRosterEntryParams]`

      Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).

      - `String = String`

      - `class BetaManagedAgentsAgentParams`

        Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

        - `type: :agent`

        - `id: String`

          The `agent` ID.

          minLength: 1, maxLength: 128

        - `version: optional Integer`

          The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

          format: int32

      - `class BetaManagedAgentsMultiagentSelfParams`

        Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

        - `type: :self`

      - `class BetaManagedAgentsAdvisorParams`

        Platform advisor roster entry: a model the session's primary thread may consult mid-turn. At most one per roster; the entry occupies the roster name `anthropic.advisor`.

        - `type: :advisor`

        - `model: String`

          A Claude model id. The model must be permitted as an advisor for this agent's model.

          minLength: 1, maxLength: 256

  - `class BetaManagedAgentsMultiagent20261001Params`

    Multiagent configuration with three members, each enabled or disabled on its own. On an update, if the agent's stored `multiagent` also has type `multiagent_20261001`, this configuration is merged into the stored one, level by level, instead of replacing it. A key that the update omits keeps its stored value. A key sent as null takes its default, on create as well, so `"workflows": null` enables workflows. An object sent with a `type` other than the stored one replaces the stored object, and the keys that it omits take their defaults. A `predefined_agents` list that is sent replaces the stored list. Every object that is sent needs its `type`, and an enabled `advisor` needs its `model`. Other validation applies to the merged result.

    - `type: :multiagent_20261001`

    - `advisor: optional BetaManagedAgentsMultiagentAdvisorParams | nil`

      Whether the session's primary thread can consult an advisor model. Defaults to disabled.

      - `class BetaManagedAgentsMultiagentAdvisorEnabledParams`

        The session's primary thread can consult `model` mid-turn.

        - `type: :enabled`

        - `model: String`

          A Claude model id. The model must be permitted as an advisor for this agent's model.

          minLength: 1, maxLength: 256

      - `class BetaManagedAgentsMultiagentAdvisorDisabledParams`

        The agent has no advisor.

        - `type: :disabled`

    - `subagents: optional BetaManagedAgentsMultiagentSubagentsParams | nil`

      Whether the agent can spawn session threads. Defaults to enabled.

      - `class BetaManagedAgentsMultiagentSubagentsEnabledParams`

        The agent can spawn session threads. Each thread runs a predefined agent, which is a saved agent in `predefined_agents`, or an inline agent, which the agent defines when it spawns the thread and which is not saved. If `inline_agents` is disabled, `predefined_agents` must name at least one agent.

        - `type: :enabled`

        - `inline_agents: optional BetaManagedAgentsMultiagentInlineAgentsParams | nil`

          Whether the agent can define inline agents when it spawns session threads. Defaults to enabled.

          - `class BetaManagedAgentsMultiagentInlineAgentsEnabledParams`

            The agent can define inline agents.

            - `type: :enabled`

          - `class BetaManagedAgentsMultiagentInlineAgentsDisabledParams`

            The agent cannot define inline agents.

            - `type: :disabled`

        - `predefined_agents: optional Array[BetaManagedAgentsMultiagentPredefinedAgentParams] | nil`

          Predefined agents that this agent can spawn as session threads. At most 20. Defaults to null. Null and an empty list both mean no predefined agents. This list is separate from `workflows.predefined_agents`, and an agent in one list is not added to the other.

          - `String = String`

          - `class BetaManagedAgentsAgentParams`

            Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

          - `class BetaManagedAgentsMultiagentSelfParams`

            Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

      - `class BetaManagedAgentsMultiagentSubagentsDisabledParams`

        The agent cannot spawn session threads.

        - `type: :disabled`

    - `workflows: optional BetaManagedAgentsMultiagentWorkflowsParams | nil`

      Whether the agent can start workflow runs. Defaults to enabled.

      - `class BetaManagedAgentsMultiagentWorkflowsEnabledParams`

        The agent can start workflow runs. Each run follows a plan, a program that the agent writes. A plan can use predefined agents, which are the saved agents in `predefined_agents`, and inline agents, which it defines itself and which are not saved. If `inline_agents` is disabled, `predefined_agents` must name at least one agent.

        - `type: :enabled`

        - `inline_agents: optional BetaManagedAgentsMultiagentInlineAgentsParams | nil`

          Whether a run's plan can define inline agents. Defaults to enabled.

        - `predefined_agents: optional Array[BetaManagedAgentsMultiagentPredefinedAgentParams] | nil`

          Predefined agents that a run's plan can use. At most 20. Defaults to null. Null and an empty list both mean no predefined agents. This list is separate from `subagents.predefined_agents`, and an agent in one list is not added to the other.

          - `String = String`

          - `class BetaManagedAgentsAgentParams`

            Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

          - `class BetaManagedAgentsMultiagentSelfParams`

            Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

      - `class BetaManagedAgentsMultiagentWorkflowsDisabledParams`

        The agent cannot start workflow runs.

        - `type: :disabled`

- `name: optional String`

  Human-readable name. Must be non-empty. Omit to preserve. Cannot be cleared.

  maxLength: 256

- `skills: optional Array[BetaManagedAgentsSkillParams] | nil`

  Skills. Full replacement. Omit to preserve; send empty array or null to clear.

  - `class BetaManagedAgentsAnthropicSkillParams`

    An Anthropic-managed skill.

    - `type: :anthropic`

    - `skill_id: String`

      Identifier of the Anthropic skill (e.g., "xlsx").

      minLength: 1, maxLength: 64

    - `version: optional String | nil`

      Version to pin. Defaults to latest if omitted.

      minLength: 1, maxLength: 64

  - `class BetaManagedAgentsCustomSkillParams`

    A user-created custom skill.

    - `type: :custom`

    - `skill_id: String`

      Tagged ID of the custom skill (e.g., "skill_01XJ5...").

      minLength: 1, maxLength: 64

    - `version: optional String | nil`

      Version to pin. Defaults to latest if omitted.

      minLength: 1, maxLength: 64

- `system_: optional String | nil`

  System prompt. Omit to preserve; send empty string or null to clear.

  maxLength: 100000

- `tools: optional Array[BetaManagedAgentsAgentToolset20260401Params | BetaManagedAgentsMCPToolsetParams | BetaManagedAgentsCustomToolParams] | nil`

  Tool configurations available to the agent. Full replacement. Omit to preserve; send empty array or null to clear. Maximum of 256 tools across all toolsets allowed.

  - `class BetaManagedAgentsAgentToolset20260401Params`

    Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

    - `type: :agent_toolset_20260401`

    - `configs: optional Array[BetaManagedAgentsAgentToolConfigParams]`

      Per-tool configuration overrides.

      - `class BetaManagedAgentsBashToolConfigParams`

        Configuration override for the bash tool.

        - `type: optional :bash`

        - `name: :bash`

          Must be "bash".

        - `enabled: optional bool | nil`

          Whether this tool is enabled and available to Claude. Overrides the default_config setting.

        - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy | nil`

          Permission policy for this tool. Controls whether tool calls are auto-approved or require confirmation.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

            - `type: :always_allow`

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

            - `type: :always_ask`

          - `class BetaManagedAgentsAutoPolicy`

            The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

            - `type: :auto`

      - `class BetaManagedAgentsEditToolConfigParams`

        Configuration override for the edit tool.

        - `type: optional :edit`

        - `name: :edit`

          Must be "edit".

        - `enabled: optional bool | nil`

          Whether this tool is enabled and available to Claude. Overrides the default_config setting.

        - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy | nil`

          Permission policy for this tool. Controls whether tool calls are auto-approved or require confirmation.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

          - `class BetaManagedAgentsAutoPolicy`

            The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

      - `class BetaManagedAgentsReadToolConfigParams`

        Configuration override for the read tool.

        - `type: optional :read`

        - `name: :read`

          Must be "read".

        - `enabled: optional bool | nil`

          Whether this tool is enabled and available to Claude. Overrides the default_config setting.

        - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy | nil`

          Permission policy for this tool. Controls whether tool calls are auto-approved or require confirmation.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

          - `class BetaManagedAgentsAutoPolicy`

            The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

      - `class BetaManagedAgentsWriteToolConfigParams`

        Configuration override for the write tool.

        - `type: optional :write`

        - `name: :write`

          Must be "write".

        - `enabled: optional bool | nil`

          Whether this tool is enabled and available to Claude. Overrides the default_config setting.

        - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy | nil`

          Permission policy for this tool. Controls whether tool calls are auto-approved or require confirmation.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

          - `class BetaManagedAgentsAutoPolicy`

            The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

      - `class BetaManagedAgentsGlobToolConfigParams`

        Configuration override for the glob tool.

        - `type: optional :glob`

        - `name: :glob`

          Must be "glob".

        - `enabled: optional bool | nil`

          Whether this tool is enabled and available to Claude. Overrides the default_config setting.

        - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy | nil`

          Permission policy for this tool. Controls whether tool calls are auto-approved or require confirmation.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

          - `class BetaManagedAgentsAutoPolicy`

            The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

      - `class BetaManagedAgentsGrepToolConfigParams`

        Configuration override for the grep tool.

        - `type: optional :grep`

        - `name: :grep`

          Must be "grep".

        - `enabled: optional bool | nil`

          Whether this tool is enabled and available to Claude. Overrides the default_config setting.

        - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy | nil`

          Permission policy for this tool. Controls whether tool calls are auto-approved or require confirmation.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

          - `class BetaManagedAgentsAutoPolicy`

            The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

      - `class BetaManagedAgentsWebFetchToolConfigParams`

        Configuration override for the web_fetch tool.

        - `type: optional :web_fetch`

        - `name: :web_fetch`

          Must be "web_fetch".

        - `allowed_domains: optional Array[String]`

          Only fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

        - `blocked_domains: optional Array[String]`

          Never fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

        - `enabled: optional bool | nil`

          Whether this tool is enabled and available to Claude. Overrides the default_config setting.

        - `max_content_tokens: optional Integer | nil`

          Maximum number of tokens of fetched text content to include in context per call. Does not apply to binary content such as PDFs.

          format: int32

        - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy | nil`

          Permission policy for this tool. Controls whether tool calls are auto-approved or require confirmation.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

          - `class BetaManagedAgentsAutoPolicy`

            The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

        - `url_sources: optional BetaManagedAgentsWebFetchURLSourcesParams | nil`

          Which sources contribute URLs the tool may fetch. Omit to allow every source.

          - `client_tool_results: optional BetaManagedAgentsWebFetchURLSourceToolFilterParams | nil`

            Which custom tools' results contribute URLs that may be fetched: "all" (the default), "none", or an only or except list. Each name in a list must be a custom tool in the same tools array.

            - `type BetaManagedAgentsWebFetchURLSourceShorthand = :all | :none`

              String form of a url_sources value that has no field other than its type: "all" means {"type": "all"} and "none" means {"type": "none"}.

              - `:all`

              - `:none`

            - `type BetaManagedAgentsWebFetchURLSourceToolFilter = BetaManagedAgentsWebFetchURLSourceAll | BetaManagedAgentsWebFetchURLSourceNone | BetaManagedAgentsWebFetchURLSourceOnly | BetaManagedAgentsWebFetchURLSourceExcept`

              Which tools' results contribute URLs that may be fetched.

              - `class BetaManagedAgentsWebFetchURLSourceAll`

                Every URL from this source may be fetched. This is the default.

                - `type: :all`

              - `class BetaManagedAgentsWebFetchURLSourceNone`

                This source contributes no URLs that may be fetched.

                - `type: :none`

              - `class BetaManagedAgentsWebFetchURLSourceOnly`

                Only the named tools' results contribute URLs that may be fetched.

                - `type: :only`

                - `tools: Array[BetaManagedAgentsWebFetchURLSourceToolReference]`

                  The tools whose results contribute. Between 1 and 128 entries, each with a different name. An empty list is rejected; use "none" to allow no tool's results.

                  - `type: :tool_reference`

                    Must be "tool_reference".

                  - `name: String`

                    Name of the tool. Compared exactly, so upper and lower case letters are different.

                    minLength: 1, maxLength: 128

              - `class BetaManagedAgentsWebFetchURLSourceExcept`

                Every tool's results contribute URLs that may be fetched, except the named tools' results.

                - `type: :except`

                - `tools: Array[BetaManagedAgentsWebFetchURLSourceToolReference]`

                  The tools whose results do not contribute. Between 1 and 128 entries, each with a different name. An empty list is rejected; use "all" to leave out no tool's results.

                  - `type: :tool_reference`

                    Must be "tool_reference".

                  - `name: String`

                    Name of the tool. Compared exactly, so upper and lower case letters are different.

                    minLength: 1, maxLength: 128

          - `server_tool_results: optional BetaManagedAgentsWebFetchURLSourceToolFilterParams | nil`

            Which of the web_search and web_fetch tools' results contribute URLs that may be fetched: "all" (the default), "none", or an only or except list. Each name in a list must be "web_search" or "web_fetch".

          - `user_input: optional BetaManagedAgentsWebFetchURLSourceUserInputParams | nil`

            Whether URLs in the text of user messages may be fetched: "all" (the default) or "none".

            - `type BetaManagedAgentsWebFetchURLSourceShorthand = :all | :none`

              String form of a url_sources value that has no field other than its type: "all" means {"type": "all"} and "none" means {"type": "none"}.

            - `type BetaManagedAgentsWebFetchURLSourceUserInput = BetaManagedAgentsWebFetchURLSourceAll | BetaManagedAgentsWebFetchURLSourceNone`

              Whether URLs in the text of user messages may be fetched.

              - `class BetaManagedAgentsWebFetchURLSourceAll`

                Every URL from this source may be fetched. This is the default.

              - `class BetaManagedAgentsWebFetchURLSourceNone`

                This source contributes no URLs that may be fetched.

      - `class BetaManagedAgentsWebSearchToolConfigParams`

        Configuration override for the web_search tool.

        - `type: optional :web_search`

        - `name: :web_search`

          Must be "web_search".

        - `allowed_domains: optional Array[String]`

          Only return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

        - `blocked_domains: optional Array[String]`

          Never return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

        - `enabled: optional bool | nil`

          Whether this tool is enabled and available to Claude. Overrides the default_config setting.

        - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy | nil`

          Permission policy for this tool. Controls whether tool calls are auto-approved or require confirmation.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

          - `class BetaManagedAgentsAutoPolicy`

            The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

        - `user_location: optional BetaManagedAgentsUserLocation | nil`

          Approximate user location for search result localization.

          - `type: :approximate`

            Location precision. Only "approximate" is supported.

          - `city: optional String | nil`

            City name.

            minLength: 1, maxLength: 255

          - `country: optional String | nil`

            Two-letter ISO 3166-1 country code, uppercase.

            pattern: ^[A-Z]{2}$

          - `region: optional String | nil`

            Region or state name.

            minLength: 1, maxLength: 255

          - `timezone: optional String | nil`

            IANA timezone identifier, e.g. "America/Los_Angeles".

            minLength: 1, maxLength: 255

    - `default_config: optional BetaManagedAgentsAgentToolsetDefaultConfigParams | nil`

      Default configuration applied to all tools in this set.

      - `enabled: optional bool | nil`

        Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

      - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy | nil`

        Default permission policy for tools. Controls whether tool calls are auto-approved or require confirmation.

        - `class BetaManagedAgentsAlwaysAllowPolicy`

          Tool calls are automatically approved without user confirmation.

        - `class BetaManagedAgentsAlwaysAskPolicy`

          Tool calls require user confirmation before execution.

        - `class BetaManagedAgentsAutoPolicy`

          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

  - `class BetaManagedAgentsMCPToolsetParams`

    Configuration for tools from an MCP server defined in `mcp_servers`.

    - `type: :mcp_toolset`

    - `mcp_server_name: String`

      Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

      minLength: 1, maxLength: 255

    - `configs: optional Array[BetaManagedAgentsMCPToolConfigParams]`

      Per-tool configuration overrides.

      - `name: String`

        Name of the MCP tool to configure. 1-128 characters.

        minLength: 1, maxLength: 128

      - `enabled: optional bool | nil`

        Whether this tool is enabled. Overrides the `default_config` setting.

      - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy | nil`

        Permission policy for this tool. Overrides the `default_config` setting.

        - `class BetaManagedAgentsAlwaysAllowPolicy`

          Tool calls are automatically approved without user confirmation.

        - `class BetaManagedAgentsAlwaysAskPolicy`

          Tool calls require user confirmation before execution.

        - `class BetaManagedAgentsAutoPolicy`

          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

    - `default_config: optional BetaManagedAgentsMCPToolsetDefaultConfigParams | nil`

      Default configuration for all tools from this server.

      - `enabled: optional bool | nil`

        Whether tools are enabled by default. Defaults to true if not specified.

      - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy | nil`

        Default permission policy for tools from this server.

        - `class BetaManagedAgentsAlwaysAllowPolicy`

          Tool calls are automatically approved without user confirmation.

        - `class BetaManagedAgentsAlwaysAskPolicy`

          Tool calls require user confirmation before execution.

        - `class BetaManagedAgentsAutoPolicy`

          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

  - `class BetaManagedAgentsCustomToolParams`

    A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

    - `type: :custom`

    - `description: String`

      Description of what the tool does, shown to the agent to help it decide when to use the tool.

      minLength: 1

    - `input_schema: BetaManagedAgentsCustomToolInputSchema`

      JSON Schema defining the expected input parameters for the tool.

      - `type: :object`

      - `properties: optional Hash[Symbol, untyped] | nil`

      - `required: optional Array[String] | nil`

    - `name: String`

      Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

      minLength: 1, maxLength: 128, pattern: ^[a-zA-Z0-9_-]{1,128}$

- `version: optional Integer`

  The agent's current version, used to prevent concurrent overwrites. Obtain this value from a create or retrieve response. Must be at least 1 if specified. When supplied, the request fails if it does not match the server's current version; omit to apply the update unconditionally.

  format: int32

- `betas: optional Array[AnthropicBeta]` (header parameter)

  This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

  - `String = String`

  - `:"computer-use-2024-10-22"`

  - `:"computer-use-2025-01-24"`

  - `:"output-128k-2025-02-19"`

  - `:"mcp-client-2025-04-04"`

  - `:"mcp-client-2025-11-20"`

  - `:"dev-full-thinking-2025-05-14"`

  - `:"interleaved-thinking-2025-05-14"`

  - `:"code-execution-2025-05-22"`

  - `:"context-1m-2025-08-07"`

  - `:"context-management-2025-06-27"`

  - `:"model-context-window-exceeded-2025-08-26"`

  - `:"fast-mode-2026-02-01"`

  - `:"output-300k-2026-03-24"`

  - `:"user-profiles-2026-03-24"`

  - `:"user-profiles-2026-08-18"`

  - `:"user-profiles-2026-09-04"`

  - `:"advisor-tool-2026-03-01"`

  - `:"managed-agents-2026-04-01"`

  - `:"dreaming-2026-04-21"`

  - `:"thinking-token-count-2026-05-13"`

  - `:"server-side-fallback-2026-06-01"`

  - `:"server-side-fallback-2026-07-01"`

  - `:"fallback-credit-2026-06-01"`

  - `:"fallback-credit-2026-07-01"`

  - `:"agent-memory-2026-07-22"`

  - `:"mid-conversation-tool-changes-2026-07-01"`

  - `:"compact-2026-01-12"`

  - `:"computer-use-2025-11-24"`

  - `:"mcp-tunnels-2026-06-22"`

  - `:"structured-outputs-2025-11-13"`

  - `:"task-budgets-2026-03-13"`

  - `:"thinking-display-updates-2026-08-18"`

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

  - `:"telemetry-destinations-2026-08-11"`

  - `:"webhooks-2026-10-07"`

  - `:"admin-user-sign-out-2026-10-08"`

  - `:"message-threads-2026-08-12"`

  - `:"analytics-usage-cost-2026-08-24"`

  - `:"experimental-claude-tag-2026-10-21"`

  - `:"message-batches-2024-09-24"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"prompt-caching-2024-07-31"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"pdfs-2024-09-25"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"token-counting-2024-11-01"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"token-efficient-tools-2025-02-19"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"files-api-2025-04-14"`

    **Deprecated**: Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/files#migrate-from-files-api-2025-04-14

  - `:"extended-cache-ttl-2025-04-11"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"skills-2025-10-02"`

    **Deprecated**: Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/skills-guide#migrate-from-skills-2025-10-02

  - `:"cache-diagnosis-2026-04-07"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `:"ce-user-management-2026-07-13"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

- `workspace_id: optional String` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `class BetaManagedAgentsAgent`

  A Managed Agents `agent`.

  - `type: :agent`

  - `id: String`

  - `archived_at: Time | nil`

    When the agent was archived. Null if not archived.

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `description: String | nil`

  - `execution_identity: BetaManagedAgentsExecutionIdentity`

    Execution principal for runs of this agent. Always present; `{"type": "service_account"}` when runs carry no customer-named principal.

    - `class BetaManagedAgentsAWSRoleExecutionIdentity`

      An AWS IAM role principal as returned in API responses.

      - `type: :aws_role`

      - `role_arn: String`

        The IAM role's ARN.

    - `class BetaManagedAgentsServiceAccountExecutionIdentity`

      The Anthropic-managed service account as returned in API responses.

      - `type: :service_account`

  - `mcp_servers: Array[BetaManagedAgentsMCPServerURLDefinition]`

    - `type: :url`

    - `name: String`

    - `url: String`

  - `metadata: Hash[Symbol, String]`

  - `model: BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `:"claude-fable-5-2"`

        Built for the most ambitious work in coding, enterprise workflows, and the sciences

      - `:"claude-haiku-5-5"`

        Fastest model for high-volume, real-time tasks

      - `:"claude-sonnet-5-5"`

        Efficient model for coding and agents

      - `:"claude-opus-5-5"`

        Powerful intelligence for coding, knowledge work, and long-running agents

      - `:"claude-fable-5-1"`

        Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

      - `:"claude-sonnet-5"`

        Efficient model for coding and agents

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

      - `:"claude-haiku-4-5-20251001"`

      - `:"claude-opus-4-5"`

        Powerful intelligence for long-running agents and coding

      - `:"claude-opus-4-5-20251101"`

        Powerful intelligence for long-running agents and coding

      - `:"claude-sonnet-4-5"`

        **Deprecated**: Will reach end-of-life on November 30, 2026. Please migrate to claude-sonnet-5-5. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.

        High-performance model for agents and coding

      - `:"claude-sonnet-4-5-20250929"`

        **Deprecated**: Will reach end-of-life on November 30, 2026. Please migrate to claude-sonnet-5-5. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.

        High-performance model for agents and coding

      - `String = String`

    - `effort: optional BetaManagedAgentsEffortLow | BetaManagedAgentsEffortMedium | BetaManagedAgentsEffortHigh | 2 more`

      How hard Claude works on each inference call. One of `low`, `medium`, `high`, `xhigh`, `max`. Always present; resolved to the per-model default at save time when not supplied.

      - `class BetaManagedAgentsEffortLow`

        Low effort. Favors latency over reasoning depth.

        - `type: :low`

      - `class BetaManagedAgentsEffortMedium`

        Medium effort. Balances latency and reasoning depth.

        - `type: :medium`

      - `class BetaManagedAgentsEffortHigh`

        High effort. Favors reasoning depth.

        - `type: :high`

      - `class BetaManagedAgentsEffortXhigh`

        Extra-high effort. Not all models accept this level.

        - `type: :xhigh`

      - `class BetaManagedAgentsEffortMax`

        Maximum effort. Favors reasoning depth over latency.

        - `type: :max`

    - `inference_geo: optional String`

      Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

    - `speed: optional :standard | :fast`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Defaults to `standard`. Not all models support `fast`; invalid combinations are rejected at create time.

      - `:standard`

      - `:fast`

  - `multiagent: BetaManagedAgentsMultiagent | nil`

    Multiagent orchestration configuration. Null when the agent is single-threaded.

    - `class BetaManagedAgentsMultiagentCoordinator`

      Resolved coordinator topology with a concrete agent roster.

      - `type: :coordinator`

      - `agents: Array[BetaManagedAgentsAgentReference | BetaManagedAgentsAdvisor]`

        Agents the coordinator may spawn as session threads, each resolved to a specific version.

        - `class BetaManagedAgentsAgentReference`

          A resolved agent reference with a concrete version.

          - `type: :agent`

          - `id: String`

          - `version: Integer`

            format: int32

        - `class BetaManagedAgentsAdvisor`

          Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

          - `type: :advisor`

          - `model: String`

            The advisor model id.

    - `class BetaManagedAgentsMultiagent20261001`

      Resolved multiagent configuration with three members, each enabled or disabled on its own.

      - `type: :multiagent_20261001`

      - `advisor: BetaManagedAgentsMultiagentAdvisor`

        Whether the session's primary thread can consult an advisor model.

        - `class BetaManagedAgentsMultiagentAdvisorEnabled`

          The session's primary thread can consult `model` mid-turn.

          - `type: :enabled`

          - `model: String`

            The advisor model id.

        - `class BetaManagedAgentsMultiagentAdvisorDisabled`

          The agent has no advisor.

          - `type: :disabled`

      - `subagents: BetaManagedAgentsMultiagentSubagents`

        Whether the agent can spawn session threads.

        - `class BetaManagedAgentsMultiagentSubagentsEnabled`

          The agent can spawn session threads.

          - `type: :enabled`

          - `inline_agents: BetaManagedAgentsMultiagentInlineAgents`

            Whether the agent can define inline agents, which are not saved, when it spawns session threads.

            - `class BetaManagedAgentsMultiagentInlineAgentsEnabled`

              The agent can define inline agents.

              - `type: :enabled`

            - `class BetaManagedAgentsMultiagentInlineAgentsDisabled`

              The agent cannot define inline agents.

              - `type: :disabled`

          - `predefined_agents: Array[BetaManagedAgentsAgentReference]`

            Predefined agents, which are saved agents that this agent can spawn as session threads, each resolved to a specific version.

            - `type: :agent`

            - `id: String`

            - `version: Integer`

              format: int32

        - `class BetaManagedAgentsMultiagentSubagentsDisabled`

          The agent cannot spawn session threads.

          - `type: :disabled`

      - `workflows: BetaManagedAgentsMultiagentWorkflows`

        Whether the agent can start workflow runs.

        - `class BetaManagedAgentsMultiagentWorkflowsEnabled`

          The agent can start workflow runs.

          - `type: :enabled`

          - `inline_agents: BetaManagedAgentsMultiagentInlineAgents`

            Whether a run's plan can define inline agents, which are not saved.

          - `predefined_agents: Array[BetaManagedAgentsAgentReference]`

            Predefined agents, which are saved agents that a run's plan can use, each resolved to a specific version.

            - `type: :agent`

            - `id: String`

            - `version: Integer`

              format: int32

        - `class BetaManagedAgentsMultiagentWorkflowsDisabled`

          The agent cannot start workflow runs.

          - `type: :disabled`

  - `name: String`

  - `skills: Array[BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill]`

    - `class BetaManagedAgentsAnthropicSkill`

      A resolved Anthropic-managed skill.

      - `type: :anthropic`

      - `skill_id: String`

      - `version: String`

    - `class BetaManagedAgentsCustomSkill`

      A resolved user-created custom skill.

      - `type: :custom`

      - `skill_id: String`

      - `version: String`

  - `system_: String | nil`

  - `tools: Array[BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool]`

    - `class BetaManagedAgentsAgentToolset20260401`

      - `type: :agent_toolset_20260401`

      - `configs: Array[BetaManagedAgentsAgentToolConfig]`

        - `class BetaManagedAgentsBashToolConfig`

          Configuration for the bash tool.

          - `type: :bash`

          - `enabled: bool`

          - `name: :bash`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: :always_allow`

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: :always_ask`

            - `class BetaManagedAgentsAutoPolicy`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

              - `type: :auto`

        - `class BetaManagedAgentsEditToolConfig`

          Configuration for the edit tool.

          - `type: :edit`

          - `enabled: bool`

          - `name: :edit`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

            - `class BetaManagedAgentsAutoPolicy`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

        - `class BetaManagedAgentsReadToolConfig`

          Configuration for the read tool.

          - `type: :read`

          - `enabled: bool`

          - `name: :read`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

            - `class BetaManagedAgentsAutoPolicy`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

        - `class BetaManagedAgentsWriteToolConfig`

          Configuration for the write tool.

          - `type: :write`

          - `enabled: bool`

          - `name: :write`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

            - `class BetaManagedAgentsAutoPolicy`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

        - `class BetaManagedAgentsGlobToolConfig`

          Configuration for the glob tool.

          - `type: :glob`

          - `enabled: bool`

          - `name: :glob`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

            - `class BetaManagedAgentsAutoPolicy`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

        - `class BetaManagedAgentsGrepToolConfig`

          Configuration for the grep tool.

          - `type: :grep`

          - `enabled: bool`

          - `name: :grep`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

            - `class BetaManagedAgentsAutoPolicy`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

        - `class BetaManagedAgentsWebFetchToolConfig`

          Configuration for the web_fetch tool.

          - `type: :web_fetch`

          - `enabled: bool`

          - `name: :web_fetch`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

            - `class BetaManagedAgentsAutoPolicy`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

          - `url_sources: BetaManagedAgentsWebFetchURLSources | nil`

            Which sources contribute URLs the tool may fetch, always in the object form. Null when not set, which allows every source.

            - `client_tool_results: BetaManagedAgentsWebFetchURLSourceToolFilter | nil`

              Which custom tools' results contribute URLs that may be fetched. Null when not set, which allows every custom tool's results.

              - `class BetaManagedAgentsWebFetchURLSourceAll`

                Every URL from this source may be fetched. This is the default.

                - `type: :all`

              - `class BetaManagedAgentsWebFetchURLSourceNone`

                This source contributes no URLs that may be fetched.

                - `type: :none`

              - `class BetaManagedAgentsWebFetchURLSourceOnly`

                Only the named tools' results contribute URLs that may be fetched.

                - `type: :only`

                - `tools: Array[BetaManagedAgentsWebFetchURLSourceToolReference]`

                  The tools whose results contribute. Between 1 and 128 entries, each with a different name. An empty list is rejected; use "none" to allow no tool's results.

                  - `type: :tool_reference`

                    Must be "tool_reference".

                  - `name: String`

                    Name of the tool. Compared exactly, so upper and lower case letters are different.

                    minLength: 1, maxLength: 128

              - `class BetaManagedAgentsWebFetchURLSourceExcept`

                Every tool's results contribute URLs that may be fetched, except the named tools' results.

                - `type: :except`

                - `tools: Array[BetaManagedAgentsWebFetchURLSourceToolReference]`

                  The tools whose results do not contribute. Between 1 and 128 entries, each with a different name. An empty list is rejected; use "all" to leave out no tool's results.

                  - `type: :tool_reference`

                    Must be "tool_reference".

                  - `name: String`

                    Name of the tool. Compared exactly, so upper and lower case letters are different.

                    minLength: 1, maxLength: 128

            - `server_tool_results: BetaManagedAgentsWebFetchURLSourceToolFilter | nil`

              Which of the web_search and web_fetch tools' results contribute URLs that may be fetched. Null when not set, which allows both.

            - `user_input: BetaManagedAgentsWebFetchURLSourceUserInput | nil`

              Whether URLs in the text of user messages may be fetched. Null when not set, which allows them.

              - `class BetaManagedAgentsWebFetchURLSourceAll`

                Every URL from this source may be fetched. This is the default.

              - `class BetaManagedAgentsWebFetchURLSourceNone`

                This source contributes no URLs that may be fetched.

          - `allowed_domains: optional Array[String]`

          - `blocked_domains: optional Array[String]`

          - `max_content_tokens: optional Integer | nil`

            format: int32

        - `class BetaManagedAgentsWebSearchToolConfig`

          Configuration for the web_search tool.

          - `type: :web_search`

          - `enabled: bool`

          - `name: :web_search`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

            - `class BetaManagedAgentsAutoPolicy`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

          - `allowed_domains: optional Array[String]`

          - `blocked_domains: optional Array[String]`

          - `user_location: optional BetaManagedAgentsUserLocation | nil`

            Approximate user location for search result localization.

            - `type: :approximate`

              Location precision. Only "approximate" is supported.

            - `city: optional String | nil`

              City name.

              minLength: 1, maxLength: 255

            - `country: optional String | nil`

              Two-letter ISO 3166-1 country code, uppercase.

              pattern: ^[A-Z]{2}$

            - `region: optional String | nil`

              Region or state name.

              minLength: 1, maxLength: 255

            - `timezone: optional String | nil`

              IANA timezone identifier, e.g. "America/Los_Angeles".

              minLength: 1, maxLength: 255

      - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

        Resolved default configuration for agent tools.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

          - `class BetaManagedAgentsAutoPolicy`

            The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

    - `class BetaManagedAgentsMCPToolset`

      - `type: :mcp_toolset`

      - `configs: Array[BetaManagedAgentsMCPToolConfig]`

        - `enabled: bool`

        - `name: String`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

          - `class BetaManagedAgentsAutoPolicy`

            The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: bool`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy | BetaManagedAgentsAutoPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

          - `class BetaManagedAgentsAutoPolicy`

            The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

      - `mcp_server_name: String`

    - `class BetaManagedAgentsCustomTool`

      A custom tool as returned in API responses.

      - `type: :custom`

      - `description: String`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `type: :object`

        - `properties: optional Hash[Symbol, untyped] | nil`

        - `required: optional Array[String] | nil`

      - `name: String`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `version: Integer`

    The agent's current version. Starts at 1 and increments when the agent is modified.

    format: int32

## Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_agent = anthropic.beta.agents.update("agent_011CZkYpogX7uDKUyvBTophP")

puts(beta_managed_agents_agent)
```

### Response (200)

```json
{
  "id": "agent_011CZkYpogX7uDKUyvBTophP",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "description": "A general-purpose starter agent.",
  "execution_identity": {
    "type": "service_account"
  },
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
    "id": "claude-opus-5-5",
    "effort": {
      "type": "low"
    },
    "inference_geo": "inference_geo",
    "speed": "standard"
  },
  "multiagent": {
    "advisor": {
      "type": "disabled"
    },
    "subagents": {
      "inline_agents": {
        "type": "enabled"
      },
      "predefined_agents": [
        {
          "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
          "type": "agent",
          "version": 1
        }
      ],
      "type": "enabled"
    },
    "type": "multiagent_20261001",
    "workflows": {
      "inline_agents": {
        "type": "enabled"
      },
      "predefined_agents": [
        {
          "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
          "type": "agent",
          "version": 1
        }
      ],
      "type": "enabled"
    }
  },
  "name": "My First Agent",
  "skills": [
    {
      "skill_id": "xlsx",
      "type": "anthropic",
      "version": "1"
    },
    {
      "skill_id": "skill_011CZkZFNu9hAbo3jZPRgTmx",
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
