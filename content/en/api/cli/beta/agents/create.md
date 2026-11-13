---
title: Create Agent
url: https://platform.claude.com/docs/en/api/cli/beta/agents/create
---

# Create Agent

`$ ant beta:agents create`

**POST** `/v1/agents`

Create Agent

## Parameters

- `--model: BetaManagedAgentsModel or BetaManagedAgentsModelConfigParams`

  Model identifier. Accepts the [model string](https://platform.claude.com/docs/en/about-claude/models/overview?sdk_languages=cli#latest-models-comparison), e.g. `claude-opus-5-5`, or a `model_config` object for additional configuration control

  - `union_member_0: "claude-fable-5-2" or "claude-haiku-5-5" or "claude-sonnet-5-5" or 15 more`

    The model that will power your agent.

    See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

    - `"claude-fable-5-2"`

      Built for the most ambitious work in coding, enterprise workflows, and the sciences

    - `"claude-haiku-5-5"`

      Fastest model for high-volume, real-time tasks

    - `"claude-sonnet-5-5"`

      Efficient model for coding and agents

    - `"claude-opus-5-5"`

      Powerful intelligence for coding, knowledge work, and long-running agents

    - `"claude-fable-5-1"`

      Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

    - `"claude-sonnet-5"`

      Efficient model for coding and agents

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

    - `"claude-haiku-4-5-20251001"`

    - `"claude-opus-4-5"`

      Powerful intelligence for long-running agents and coding

    - `"claude-opus-4-5-20251101"`

      Powerful intelligence for long-running agents and coding

    - `"claude-sonnet-4-5"`

      **Deprecated**: Will reach end-of-life on November 30, 2026. Please migrate to claude-sonnet-5-5. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.

      High-performance model for agents and coding

    - `"claude-sonnet-4-5-20250929"`

      **Deprecated**: Will reach end-of-life on November 30, 2026. Please migrate to claude-sonnet-5-5. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.

      High-performance model for agents and coding

  - `beta_managed_agents_model_config_params: object`

    An object that defines additional configuration control over model use

    - `id: "claude-fable-5-2" or "claude-haiku-5-5" or "claude-sonnet-5-5" or 15 more or string`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `"claude-fable-5-2"`

        Built for the most ambitious work in coding, enterprise workflows, and the sciences

      - `"claude-haiku-5-5"`

        Fastest model for high-volume, real-time tasks

      - `"claude-sonnet-5-5"`

        Efficient model for coding and agents

      - `"claude-opus-5-5"`

        Powerful intelligence for coding, knowledge work, and long-running agents

      - `"claude-fable-5-1"`

        Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

      - `"claude-sonnet-5"`

        Efficient model for coding and agents

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

      - `"claude-haiku-4-5-20251001"`

      - `"claude-opus-4-5"`

        Powerful intelligence for long-running agents and coding

      - `"claude-opus-4-5-20251101"`

        Powerful intelligence for long-running agents and coding

      - `"claude-sonnet-4-5"`

        **Deprecated**: Will reach end-of-life on November 30, 2026. Please migrate to claude-sonnet-5-5. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.

        High-performance model for agents and coding

      - `"claude-sonnet-4-5-20250929"`

        **Deprecated**: Will reach end-of-life on November 30, 2026. Please migrate to claude-sonnet-5-5. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.

        High-performance model for agents and coding

    - `effort: optional "low" or "medium" or "high" or 2 more or BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or 3 more`

      How hard Claude works on each inference call. Accepts a bare level string (`"high"`) or `{"type": "high"}`. On create, omitting it resolves the per-model default; on update, omitting it leaves the stored value unchanged.

      - `BetaManagedAgentsEffortLevel: "low" or "medium" or "high" or 2 more`

        How hard Claude works on each turn. Higher levels favor reasoning depth over latency. Not all models accept every level; invalid combinations are rejected at create time.

        - `"low"`

          Low effort. Favors latency over reasoning depth.

        - `"medium"`

          Medium effort. Balances latency and reasoning depth.

        - `"high"`

          High effort. Favors reasoning depth.

        - `"xhigh"`

          Extra-high effort. Not all models accept this level.

        - `"max"`

          Maximum effort. Favors reasoning depth over latency.

      - `beta_managed_agents_effort_low: object`

        Low effort. Favors latency over reasoning depth.

        - `type: "low"`

      - `beta_managed_agents_effort_medium: object`

        Medium effort. Balances latency and reasoning depth.

        - `type: "medium"`

      - `beta_managed_agents_effort_high: object`

        High effort. Favors reasoning depth.

        - `type: "high"`

      - `beta_managed_agents_effort_xhigh: object`

        Extra-high effort. Not all models accept this level.

        - `type: "xhigh"`

      - `beta_managed_agents_effort_max: object`

        Maximum effort. Favors reasoning depth over latency.

        - `type: "max"`

    - `inference_geo: optional string`

      Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo. On update, `model` is whole-object replacement — omitting inference_geo clears it.

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Defaults to `standard`. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

- `--name: string`

  Human-readable name for the agent.

  minLength: 1, maxLength: 256

- `--description: optional string`

  Description of what the agent does.

  maxLength: 2048

- `--execution-identity: optional BetaManagedAgentsExecutionIdentityParams`

  Execution principal for runs of this agent. Omitting it, sending null, or sending `{"type": "service_account"}` stores the default.

  - `beta_managed_agents_aws_role_execution_identity_params: object`

    An AWS IAM role principal.

    - `type: "aws_role"`

    - `role_arn: string`

      The IAM role's ARN, e.g. "arn:aws:iam::123456789012:role/my-agent-runner". Maximum 2048 characters.

      maxLength: 2048, pattern: ^arn:aws(-[a-z]+)*:iam::[0-9]{12}:role/[\w+=,.@/-]+$

  - `beta_managed_agents_service_account_execution_identity_params: object`

    The Anthropic-managed service account — the default execution principal. Carries no identifier.

    - `type: "service_account"`

- `--mcp-server: optional array of BetaManagedAgentsURLMCPServerParams`

  MCP servers this agent connects to. Maximum 20. Names must be unique within the array. Every server must be referenced by an `mcp_toolset` in `tools`; unreferenced servers are rejected. See the [MCP connector guide](https://platform.claude.com/docs/en/managed-agents/mcp-connector?sdk_languages=cli).

  - `type: "url"`

  - `name: string`

    Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

    minLength: 1, maxLength: 255

  - `url: string`

    Endpoint URL for the MCP server.

    maxLength: 2048

- `--metadata: optional map[string]`

  Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `--multiagent: optional BetaManagedAgentsMultiagentParams`

  Multiagent orchestration configuration.

  - `beta_managed_agents_multiagent_coordinator_params: object`

    A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.

    - `type: "coordinator"`

    - `agents: array of BetaManagedAgentsMultiagentRosterEntryParams`

      Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).

      - `union_member_0: string`

      - `beta_managed_agents_agent_params: object`

        Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

        - `type: "agent"`

        - `id: string`

          The `agent` ID.

          minLength: 1, maxLength: 128

        - `version: optional number`

          The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

          format: int32

      - `beta_managed_agents_multiagent_self_params: object`

        Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

        - `type: "self"`

      - `beta_managed_agents_advisor_params: object`

        Platform advisor roster entry: a model the session's primary thread may consult mid-turn. At most one per roster; the entry occupies the roster name `anthropic.advisor`.

        - `type: "advisor"`

        - `model: string`

          A Claude model id. The model must be permitted as an advisor for this agent's model.

          minLength: 1, maxLength: 256

  - `beta_managed_agents_multiagent20261001_params: object`

    Multiagent configuration with three members, each enabled or disabled on its own. On an update, if the agent's stored `multiagent` also has type `multiagent_20261001`, this configuration is merged into the stored one, level by level, instead of replacing it. A key that the update omits keeps its stored value. A key sent as null takes its default, on create as well, so `"workflows": null` enables workflows. An object sent with a `type` other than the stored one replaces the stored object, and the keys that it omits take their defaults. A `predefined_agents` list that is sent replaces the stored list. Every object that is sent needs its `type`, and an enabled `advisor` needs its `model`. Other validation applies to the merged result.

    - `type: "multiagent_20261001"`

    - `advisor: optional BetaManagedAgentsMultiagentAdvisorEnabledParams or BetaManagedAgentsMultiagentAdvisorDisabledParams`

      Whether the session's primary thread can consult an advisor model. Defaults to disabled.

      - `beta_managed_agents_multiagent_advisor_enabled_params: object`

        The session's primary thread can consult `model` mid-turn.

        - `type: "enabled"`

        - `model: string`

          A Claude model id. The model must be permitted as an advisor for this agent's model.

          minLength: 1, maxLength: 256

      - `beta_managed_agents_multiagent_advisor_disabled_params: object`

        The agent has no advisor.

        - `type: "disabled"`

    - `subagents: optional BetaManagedAgentsMultiagentSubagentsEnabledParams or BetaManagedAgentsMultiagentSubagentsDisabledParams`

      Whether the agent can spawn session threads. Defaults to enabled.

      - `beta_managed_agents_multiagent_subagents_enabled_params: object`

        The agent can spawn session threads. Each thread runs a predefined agent, which is a saved agent in `predefined_agents`, or an inline agent, which the agent defines when it spawns the thread and which is not saved. If `inline_agents` is disabled, `predefined_agents` must name at least one agent.

        - `type: "enabled"`

        - `inline_agents: optional BetaManagedAgentsMultiagentInlineAgentsEnabledParams or BetaManagedAgentsMultiagentInlineAgentsDisabledParams`

          Whether the agent can define inline agents when it spawns session threads. Defaults to enabled.

          - `beta_managed_agents_multiagent_inline_agents_enabled_params: object`

            The agent can define inline agents.

            - `type: "enabled"`

          - `beta_managed_agents_multiagent_inline_agents_disabled_params: object`

            The agent cannot define inline agents.

            - `type: "disabled"`

        - `predefined_agents: optional array of BetaManagedAgentsMultiagentPredefinedAgentParams`

          Predefined agents that this agent can spawn as session threads. At most 20. Defaults to null. Null and an empty list both mean no predefined agents. This list is separate from `workflows.predefined_agents`, and an agent in one list is not added to the other.

          - `union_member_0: string`

          - `beta_managed_agents_agent_params: object`

            Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

          - `beta_managed_agents_multiagent_self_params: object`

            Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

      - `beta_managed_agents_multiagent_subagents_disabled_params: object`

        The agent cannot spawn session threads.

        - `type: "disabled"`

    - `workflows: optional BetaManagedAgentsMultiagentWorkflowsEnabledParams or BetaManagedAgentsMultiagentWorkflowsDisabledParams`

      Whether the agent can start workflow runs. Defaults to enabled.

      - `beta_managed_agents_multiagent_workflows_enabled_params: object`

        The agent can start workflow runs. Each run follows a plan, a program that the agent writes. A plan can use predefined agents, which are the saved agents in `predefined_agents`, and inline agents, which it defines itself and which are not saved. If `inline_agents` is disabled, `predefined_agents` must name at least one agent.

        - `type: "enabled"`

        - `inline_agents: optional BetaManagedAgentsMultiagentInlineAgentsEnabledParams or BetaManagedAgentsMultiagentInlineAgentsDisabledParams`

          Whether a run's plan can define inline agents. Defaults to enabled.

        - `predefined_agents: optional array of BetaManagedAgentsMultiagentPredefinedAgentParams`

          Predefined agents that a run's plan can use. At most 20. Defaults to null. Null and an empty list both mean no predefined agents. This list is separate from `subagents.predefined_agents`, and an agent in one list is not added to the other.

          - `union_member_0: string`

          - `beta_managed_agents_agent_params: object`

            Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

          - `beta_managed_agents_multiagent_self_params: object`

            Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

      - `beta_managed_agents_multiagent_workflows_disabled_params: object`

        The agent cannot start workflow runs.

        - `type: "disabled"`

- `--skill: optional array of BetaManagedAgentsSkillParams`

  Skills available to the agent.

  - `beta_managed_agents_anthropic_skill_params: object`

    An Anthropic-managed skill.

    - `type: "anthropic"`

    - `skill_id: string`

      Identifier of the Anthropic skill (e.g., "xlsx").

      minLength: 1, maxLength: 64

    - `version: optional string`

      Version to pin. Defaults to latest if omitted.

      minLength: 1, maxLength: 64

  - `beta_managed_agents_custom_skill_params: object`

    A user-created custom skill.

    - `type: "custom"`

    - `skill_id: string`

      Tagged ID of the custom skill (e.g., "skill_01XJ5...").

      minLength: 1, maxLength: 64

    - `version: optional string`

      Version to pin. Defaults to latest if omitted.

      minLength: 1, maxLength: 64

- `--system: optional string`

  System prompt for the agent.

  maxLength: 100000

- `--tool: optional array of BetaManagedAgentsAgentToolset20260401Params or BetaManagedAgentsMCPToolsetParams or BetaManagedAgentsCustomToolParams`

  Tool configurations available to the agent. Maximum of 256 tools across all toolsets allowed.

  - `beta_managed_agents_agent_toolset20260401_params: object`

    Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

    - `type: "agent_toolset_20260401"`

    - `configs: optional array of BetaManagedAgentsAgentToolConfigParams`

      Per-tool configuration overrides.

      - `beta_managed_agents_bash_tool_config_params: object`

        Configuration override for the bash tool.

        - `type: optional "bash"`

        - `name: "bash"`

          Must be "bash".

        - `enabled: optional boolean`

          Whether this tool is enabled and available to Claude. Overrides the default_config setting.

        - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

          Permission policy for this tool. Controls whether tool calls are auto-approved or require confirmation.

          - `beta_managed_agents_always_allow_policy: object`

            Tool calls are automatically approved without user confirmation.

            - `type: "always_allow"`

          - `beta_managed_agents_always_ask_policy: object`

            Tool calls require user confirmation before execution.

            - `type: "always_ask"`

          - `beta_managed_agents_auto_policy: object`

            The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

            - `type: "auto"`

      - `beta_managed_agents_edit_tool_config_params: object`

        Configuration override for the edit tool.

        - `type: optional "edit"`

        - `name: "edit"`

          Must be "edit".

        - `enabled: optional boolean`

          Whether this tool is enabled and available to Claude. Overrides the default_config setting.

        - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

          Permission policy for this tool. Controls whether tool calls are auto-approved or require confirmation.

          - `beta_managed_agents_always_allow_policy: object`

            Tool calls are automatically approved without user confirmation.

          - `beta_managed_agents_always_ask_policy: object`

            Tool calls require user confirmation before execution.

          - `beta_managed_agents_auto_policy: object`

            The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

      - `beta_managed_agents_read_tool_config_params: object`

        Configuration override for the read tool.

        - `type: optional "read"`

        - `name: "read"`

          Must be "read".

        - `enabled: optional boolean`

          Whether this tool is enabled and available to Claude. Overrides the default_config setting.

        - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

          Permission policy for this tool. Controls whether tool calls are auto-approved or require confirmation.

          - `beta_managed_agents_always_allow_policy: object`

            Tool calls are automatically approved without user confirmation.

          - `beta_managed_agents_always_ask_policy: object`

            Tool calls require user confirmation before execution.

          - `beta_managed_agents_auto_policy: object`

            The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

      - `beta_managed_agents_write_tool_config_params: object`

        Configuration override for the write tool.

        - `type: optional "write"`

        - `name: "write"`

          Must be "write".

        - `enabled: optional boolean`

          Whether this tool is enabled and available to Claude. Overrides the default_config setting.

        - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

          Permission policy for this tool. Controls whether tool calls are auto-approved or require confirmation.

          - `beta_managed_agents_always_allow_policy: object`

            Tool calls are automatically approved without user confirmation.

          - `beta_managed_agents_always_ask_policy: object`

            Tool calls require user confirmation before execution.

          - `beta_managed_agents_auto_policy: object`

            The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

      - `beta_managed_agents_glob_tool_config_params: object`

        Configuration override for the glob tool.

        - `type: optional "glob"`

        - `name: "glob"`

          Must be "glob".

        - `enabled: optional boolean`

          Whether this tool is enabled and available to Claude. Overrides the default_config setting.

        - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

          Permission policy for this tool. Controls whether tool calls are auto-approved or require confirmation.

          - `beta_managed_agents_always_allow_policy: object`

            Tool calls are automatically approved without user confirmation.

          - `beta_managed_agents_always_ask_policy: object`

            Tool calls require user confirmation before execution.

          - `beta_managed_agents_auto_policy: object`

            The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

      - `beta_managed_agents_grep_tool_config_params: object`

        Configuration override for the grep tool.

        - `type: optional "grep"`

        - `name: "grep"`

          Must be "grep".

        - `enabled: optional boolean`

          Whether this tool is enabled and available to Claude. Overrides the default_config setting.

        - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

          Permission policy for this tool. Controls whether tool calls are auto-approved or require confirmation.

          - `beta_managed_agents_always_allow_policy: object`

            Tool calls are automatically approved without user confirmation.

          - `beta_managed_agents_always_ask_policy: object`

            Tool calls require user confirmation before execution.

          - `beta_managed_agents_auto_policy: object`

            The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

      - `beta_managed_agents_web_fetch_tool_config_params: object`

        Configuration override for the web_fetch tool.

        - `type: optional "web_fetch"`

        - `name: "web_fetch"`

          Must be "web_fetch".

        - `allowed_domains: optional array of string`

          Only fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

        - `blocked_domains: optional array of string`

          Never fetch URLs whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme, port, or path). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

        - `enabled: optional boolean`

          Whether this tool is enabled and available to Claude. Overrides the default_config setting.

        - `max_content_tokens: optional number`

          Maximum number of tokens of fetched text content to include in context per call. Does not apply to binary content such as PDFs.

          format: int32

        - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

          Permission policy for this tool. Controls whether tool calls are auto-approved or require confirmation.

          - `beta_managed_agents_always_allow_policy: object`

            Tool calls are automatically approved without user confirmation.

          - `beta_managed_agents_always_ask_policy: object`

            Tool calls require user confirmation before execution.

          - `beta_managed_agents_auto_policy: object`

            The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

        - `url_sources: optional object`

          Which sources contribute URLs the tool may fetch. Omit to allow every source.

          - `client_tool_results: optional BetaManagedAgentsWebFetchURLSourceShorthand or BetaManagedAgentsWebFetchURLSourceToolFilter`

            Which custom tools' results contribute URLs that may be fetched: "all" (the default), "none", or an only or except list. Each name in a list must be a custom tool in the same tools array.

            - `beta_managed_agents_web_fetch_url_source_shorthand: "all" or "none"`

              String form of a url_sources value that has no field other than its type: "all" means {"type": "all"} and "none" means {"type": "none"}.

              - `"all"`

              - `"none"`

            - `beta_managed_agents_web_fetch_url_source_tool_filter: BetaManagedAgentsWebFetchURLSourceAll or BetaManagedAgentsWebFetchURLSourceNone or BetaManagedAgentsWebFetchURLSourceOnly or BetaManagedAgentsWebFetchURLSourceExcept`

              Which tools' results contribute URLs that may be fetched.

              - `beta_managed_agents_web_fetch_url_source_all: object`

                Every URL from this source may be fetched. This is the default.

                - `type: "all"`

              - `beta_managed_agents_web_fetch_url_source_none: object`

                This source contributes no URLs that may be fetched.

                - `type: "none"`

              - `beta_managed_agents_web_fetch_url_source_only: object`

                Only the named tools' results contribute URLs that may be fetched.

                - `type: "only"`

                - `tools: array of BetaManagedAgentsWebFetchURLSourceToolReference`

                  The tools whose results contribute. Between 1 and 128 entries, each with a different name. An empty list is rejected; use "none" to allow no tool's results.

                  - `type: "tool_reference"`

                    Must be "tool_reference".

                  - `name: string`

                    Name of the tool. Compared exactly, so upper and lower case letters are different.

                    minLength: 1, maxLength: 128

              - `beta_managed_agents_web_fetch_url_source_except: object`

                Every tool's results contribute URLs that may be fetched, except the named tools' results.

                - `type: "except"`

                - `tools: array of BetaManagedAgentsWebFetchURLSourceToolReference`

                  The tools whose results do not contribute. Between 1 and 128 entries, each with a different name. An empty list is rejected; use "all" to leave out no tool's results.

                  - `type: "tool_reference"`

                    Must be "tool_reference".

                  - `name: string`

                    Name of the tool. Compared exactly, so upper and lower case letters are different.

                    minLength: 1, maxLength: 128

          - `server_tool_results: optional BetaManagedAgentsWebFetchURLSourceShorthand or BetaManagedAgentsWebFetchURLSourceToolFilter`

            Which of the web_search and web_fetch tools' results contribute URLs that may be fetched: "all" (the default), "none", or an only or except list. Each name in a list must be "web_search" or "web_fetch".

          - `user_input: optional BetaManagedAgentsWebFetchURLSourceShorthand or BetaManagedAgentsWebFetchURLSourceUserInput`

            Whether URLs in the text of user messages may be fetched: "all" (the default) or "none".

            - `beta_managed_agents_web_fetch_url_source_shorthand: "all" or "none"`

              String form of a url_sources value that has no field other than its type: "all" means {"type": "all"} and "none" means {"type": "none"}.

            - `beta_managed_agents_web_fetch_url_source_user_input: BetaManagedAgentsWebFetchURLSourceAll or BetaManagedAgentsWebFetchURLSourceNone`

              Whether URLs in the text of user messages may be fetched.

              - `beta_managed_agents_web_fetch_url_source_all: object`

                Every URL from this source may be fetched. This is the default.

              - `beta_managed_agents_web_fetch_url_source_none: object`

                This source contributes no URLs that may be fetched.

      - `beta_managed_agents_web_search_tool_config_params: object`

        Configuration override for the web_search tool.

        - `type: optional "web_search"`

        - `name: "web_search"`

          Must be "web_search".

        - `allowed_domains: optional array of string`

          Only return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

        - `blocked_domains: optional array of string`

          Never return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

        - `enabled: optional boolean`

          Whether this tool is enabled and available to Claude. Overrides the default_config setting.

        - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

          Permission policy for this tool. Controls whether tool calls are auto-approved or require confirmation.

          - `beta_managed_agents_always_allow_policy: object`

            Tool calls are automatically approved without user confirmation.

          - `beta_managed_agents_always_ask_policy: object`

            Tool calls require user confirmation before execution.

          - `beta_managed_agents_auto_policy: object`

            The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

        - `user_location: optional object`

          Approximate user location for search result localization.

          - `type: "approximate"`

            Location precision. Only "approximate" is supported.

          - `city: optional string`

            City name.

            minLength: 1, maxLength: 255

          - `country: optional string`

            Two-letter ISO 3166-1 country code, uppercase.

            pattern: ^[A-Z]{2}$

          - `region: optional string`

            Region or state name.

            minLength: 1, maxLength: 255

          - `timezone: optional string`

            IANA timezone identifier, e.g. "America/Los_Angeles".

            minLength: 1, maxLength: 255

    - `default_config: optional object`

      Default configuration applied to all tools in this set.

      - `enabled: optional boolean`

        Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

      - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

        Default permission policy for tools. Controls whether tool calls are auto-approved or require confirmation.

        - `beta_managed_agents_always_allow_policy: object`

          Tool calls are automatically approved without user confirmation.

        - `beta_managed_agents_always_ask_policy: object`

          Tool calls require user confirmation before execution.

        - `beta_managed_agents_auto_policy: object`

          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

  - `beta_managed_agents_mcp_toolset_params: object`

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

      - `enabled: optional boolean`

        Whether this tool is enabled. Overrides the `default_config` setting.

      - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

        Permission policy for this tool. Overrides the `default_config` setting.

        - `beta_managed_agents_always_allow_policy: object`

          Tool calls are automatically approved without user confirmation.

        - `beta_managed_agents_always_ask_policy: object`

          Tool calls require user confirmation before execution.

        - `beta_managed_agents_auto_policy: object`

          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

    - `default_config: optional object`

      Default configuration for all tools from this server.

      - `enabled: optional boolean`

        Whether tools are enabled by default. Defaults to true if not specified.

      - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

        Default permission policy for tools from this server.

        - `beta_managed_agents_always_allow_policy: object`

          Tool calls are automatically approved without user confirmation.

        - `beta_managed_agents_always_ask_policy: object`

          Tool calls require user confirmation before execution.

        - `beta_managed_agents_auto_policy: object`

          The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

  - `beta_managed_agents_custom_tool_params: object`

    A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

    - `type: "custom"`

    - `description: string`

      Description of what the tool does, shown to the agent to help it decide when to use the tool.

      minLength: 1

    - `input_schema: object`

      JSON Schema defining the expected input parameters for the tool.

      - `type: "object"`

      - `properties: optional map[unknown]`

      - `required: optional array of string`

    - `name: string`

      Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

      minLength: 1, maxLength: 128, pattern: ^[a-zA-Z0-9_-]{1,128}$

- `--beta: optional array of AnthropicBeta` (header parameter)

  This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

  - `"computer-use-2024-10-22"`

  - `"computer-use-2025-01-24"`

  - `"output-128k-2025-02-19"`

  - `"mcp-client-2025-04-04"`

  - `"mcp-client-2025-11-20"`

  - `"dev-full-thinking-2025-05-14"`

  - `"interleaved-thinking-2025-05-14"`

  - `"code-execution-2025-05-22"`

  - `"context-1m-2025-08-07"`

  - `"context-management-2025-06-27"`

  - `"model-context-window-exceeded-2025-08-26"`

  - `"fast-mode-2026-02-01"`

  - `"output-300k-2026-03-24"`

  - `"user-profiles-2026-03-24"`

  - `"user-profiles-2026-08-18"`

  - `"user-profiles-2026-09-04"`

  - `"advisor-tool-2026-03-01"`

  - `"managed-agents-2026-04-01"`

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

  - `"mid-conversation-output-config-2026-07-01"`

  - `"thinking-binding-controls-2026-08-01"`

  - `"mid-conversation-system-clear-at-2026-08-21"`

  - `"compact-2026-09-04"`

  - `"inline-tools-2026-09-15"`

  - `"mcp-client-2026-09-15"`

  - `"ce-plugins-2026-09-01"`

  - `"spend-limit-reads-2026-09-26"`

  - `"telemetry-destinations-2026-08-11"`

  - `"webhooks-2026-10-07"`

  - `"admin-user-sign-out-2026-10-08"`

  - `"message-threads-2026-08-12"`

  - `"analytics-usage-cost-2026-08-24"`

  - `"experimental-claude-tag-2026-10-21"`

  - `"message-batches-2024-09-24"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `"prompt-caching-2024-07-31"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `"pdfs-2024-09-25"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `"token-counting-2024-11-01"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `"token-efficient-tools-2025-02-19"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `"files-api-2025-04-14"`

    **Deprecated**: Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/files#migrate-from-files-api-2025-04-14

  - `"extended-cache-ttl-2025-04-11"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `"skills-2025-10-02"`

    **Deprecated**: Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/skills-guide#migrate-from-skills-2025-10-02

  - `"cache-diagnosis-2026-04-07"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `"ce-user-management-2026-07-13"`

    **Deprecated**: This value is no longer needed. Remove it from your requests.

- `--workspace-id: optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `beta_managed_agents_agent: object`

  A Managed Agents `agent`.

  - `type: "agent"`

  - `id: string`

  - `archived_at: string`

    When the agent was archived. Null if not archived.

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `description: string`

  - `execution_identity: BetaManagedAgentsAWSRoleExecutionIdentity or BetaManagedAgentsServiceAccountExecutionIdentity`

    Execution principal for runs of this agent. Always present; `{"type": "service_account"}` when runs carry no customer-named principal.

    - `beta_managed_agents_aws_role_execution_identity: object`

      An AWS IAM role principal as returned in API responses.

      - `type: "aws_role"`

      - `role_arn: string`

        The IAM role's ARN.

    - `beta_managed_agents_service_account_execution_identity: object`

      The Anthropic-managed service account as returned in API responses.

      - `type: "service_account"`

  - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

    - `type: "url"`

    - `name: string`

    - `url: string`

  - `metadata: map[string]`

  - `model: object`

    Model identifier and configuration.

    - `id: "claude-fable-5-2" or "claude-haiku-5-5" or "claude-sonnet-5-5" or 15 more or string`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `"claude-fable-5-2"`

        Built for the most ambitious work in coding, enterprise workflows, and the sciences

      - `"claude-haiku-5-5"`

        Fastest model for high-volume, real-time tasks

      - `"claude-sonnet-5-5"`

        Efficient model for coding and agents

      - `"claude-opus-5-5"`

        Powerful intelligence for coding, knowledge work, and long-running agents

      - `"claude-fable-5-1"`

        Frontier intelligence for ambitious tasks across coding, scientific discovery, and enterprise workflows

      - `"claude-sonnet-5"`

        Efficient model for coding and agents

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

      - `"claude-haiku-4-5-20251001"`

      - `"claude-opus-4-5"`

        Powerful intelligence for long-running agents and coding

      - `"claude-opus-4-5-20251101"`

        Powerful intelligence for long-running agents and coding

      - `"claude-sonnet-4-5"`

        **Deprecated**: Will reach end-of-life on November 30, 2026. Please migrate to claude-sonnet-5-5. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.

        High-performance model for agents and coding

      - `"claude-sonnet-4-5-20250929"`

        **Deprecated**: Will reach end-of-life on November 30, 2026. Please migrate to claude-sonnet-5-5. Visit https://docs.anthropic.com/en/docs/resources/model-deprecations for more information.

        High-performance model for agents and coding

    - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

      How hard Claude works on each inference call. One of `low`, `medium`, `high`, `xhigh`, `max`. Always present; resolved to the per-model default at save time when not supplied.

      - `beta_managed_agents_effort_low: object`

        Low effort. Favors latency over reasoning depth.

        - `type: "low"`

      - `beta_managed_agents_effort_medium: object`

        Medium effort. Balances latency and reasoning depth.

        - `type: "medium"`

      - `beta_managed_agents_effort_high: object`

        High effort. Favors reasoning depth.

        - `type: "high"`

      - `beta_managed_agents_effort_xhigh: object`

        Extra-high effort. Not all models accept this level.

        - `type: "xhigh"`

      - `beta_managed_agents_effort_max: object`

        Maximum effort. Favors reasoning depth over latency.

        - `type: "max"`

    - `inference_geo: optional string`

      Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Defaults to `standard`. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `multiagent: BetaManagedAgentsMultiagentCoordinator or BetaManagedAgentsMultiagent20261001`

    Multiagent orchestration configuration. Null when the agent is single-threaded.

    - `beta_managed_agents_multiagent_coordinator: object`

      Resolved coordinator topology with a concrete agent roster.

      - `type: "coordinator"`

      - `agents: array of BetaManagedAgentsAgentReference or BetaManagedAgentsAdvisor`

        Agents the coordinator may spawn as session threads, each resolved to a specific version.

        - `beta_managed_agents_agent_reference: object`

          A resolved agent reference with a concrete version.

          - `type: "agent"`

          - `id: string`

          - `version: number`

            format: int32

        - `beta_managed_agents_advisor: object`

          Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

          - `type: "advisor"`

          - `model: string`

            The advisor model id.

    - `beta_managed_agents_multiagent20261001: object`

      Resolved multiagent configuration with three members, each enabled or disabled on its own.

      - `type: "multiagent_20261001"`

      - `advisor: BetaManagedAgentsMultiagentAdvisorEnabled or BetaManagedAgentsMultiagentAdvisorDisabled`

        Whether the session's primary thread can consult an advisor model.

        - `beta_managed_agents_multiagent_advisor_enabled: object`

          The session's primary thread can consult `model` mid-turn.

          - `type: "enabled"`

          - `model: string`

            The advisor model id.

        - `beta_managed_agents_multiagent_advisor_disabled: object`

          The agent has no advisor.

          - `type: "disabled"`

      - `subagents: BetaManagedAgentsMultiagentSubagentsEnabled or BetaManagedAgentsMultiagentSubagentsDisabled`

        Whether the agent can spawn session threads.

        - `beta_managed_agents_multiagent_subagents_enabled: object`

          The agent can spawn session threads.

          - `type: "enabled"`

          - `inline_agents: BetaManagedAgentsMultiagentInlineAgentsEnabled or BetaManagedAgentsMultiagentInlineAgentsDisabled`

            Whether the agent can define inline agents, which are not saved, when it spawns session threads.

            - `beta_managed_agents_multiagent_inline_agents_enabled: object`

              The agent can define inline agents.

              - `type: "enabled"`

            - `beta_managed_agents_multiagent_inline_agents_disabled: object`

              The agent cannot define inline agents.

              - `type: "disabled"`

          - `predefined_agents: array of BetaManagedAgentsAgentReference`

            Predefined agents, which are saved agents that this agent can spawn as session threads, each resolved to a specific version.

            - `type: "agent"`

            - `id: string`

            - `version: number`

              format: int32

        - `beta_managed_agents_multiagent_subagents_disabled: object`

          The agent cannot spawn session threads.

          - `type: "disabled"`

      - `workflows: BetaManagedAgentsMultiagentWorkflowsEnabled or BetaManagedAgentsMultiagentWorkflowsDisabled`

        Whether the agent can start workflow runs.

        - `beta_managed_agents_multiagent_workflows_enabled: object`

          The agent can start workflow runs.

          - `type: "enabled"`

          - `inline_agents: BetaManagedAgentsMultiagentInlineAgentsEnabled or BetaManagedAgentsMultiagentInlineAgentsDisabled`

            Whether a run's plan can define inline agents, which are not saved.

          - `predefined_agents: array of BetaManagedAgentsAgentReference`

            Predefined agents, which are saved agents that a run's plan can use, each resolved to a specific version.

            - `type: "agent"`

            - `id: string`

            - `version: number`

              format: int32

        - `beta_managed_agents_multiagent_workflows_disabled: object`

          The agent cannot start workflow runs.

          - `type: "disabled"`

  - `name: string`

  - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

    - `beta_managed_agents_anthropic_skill: object`

      A resolved Anthropic-managed skill.

      - `type: "anthropic"`

      - `skill_id: string`

      - `version: string`

    - `beta_managed_agents_custom_skill: object`

      A resolved user-created custom skill.

      - `type: "custom"`

      - `skill_id: string`

      - `version: string`

  - `system: string`

  - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

    - `beta_managed_agents_agent_toolset20260401: object`

      - `type: "agent_toolset_20260401"`

      - `configs: array of BetaManagedAgentsAgentToolConfig`

        - `beta_managed_agents_bash_tool_config: object`

          Configuration for the bash tool.

          - `type: "bash"`

          - `enabled: boolean`

          - `name: "bash"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

            - `beta_managed_agents_always_ask_policy: object`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

            - `beta_managed_agents_auto_policy: object`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

              - `type: "auto"`

        - `beta_managed_agents_edit_tool_config: object`

          Configuration for the edit tool.

          - `type: "edit"`

          - `enabled: boolean`

          - `name: "edit"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object`

              Tool calls require user confirmation before execution.

            - `beta_managed_agents_auto_policy: object`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

        - `beta_managed_agents_read_tool_config: object`

          Configuration for the read tool.

          - `type: "read"`

          - `enabled: boolean`

          - `name: "read"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object`

              Tool calls require user confirmation before execution.

            - `beta_managed_agents_auto_policy: object`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

        - `beta_managed_agents_write_tool_config: object`

          Configuration for the write tool.

          - `type: "write"`

          - `enabled: boolean`

          - `name: "write"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object`

              Tool calls require user confirmation before execution.

            - `beta_managed_agents_auto_policy: object`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

        - `beta_managed_agents_glob_tool_config: object`

          Configuration for the glob tool.

          - `type: "glob"`

          - `enabled: boolean`

          - `name: "glob"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object`

              Tool calls require user confirmation before execution.

            - `beta_managed_agents_auto_policy: object`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

        - `beta_managed_agents_grep_tool_config: object`

          Configuration for the grep tool.

          - `type: "grep"`

          - `enabled: boolean`

          - `name: "grep"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object`

              Tool calls require user confirmation before execution.

            - `beta_managed_agents_auto_policy: object`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

        - `beta_managed_agents_web_fetch_tool_config: object`

          Configuration for the web_fetch tool.

          - `type: "web_fetch"`

          - `enabled: boolean`

          - `name: "web_fetch"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object`

              Tool calls require user confirmation before execution.

            - `beta_managed_agents_auto_policy: object`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

          - `url_sources: object`

            Which sources contribute URLs the tool may fetch, always in the object form. Null when not set, which allows every source.

            - `client_tool_results: BetaManagedAgentsWebFetchURLSourceAll or BetaManagedAgentsWebFetchURLSourceNone or BetaManagedAgentsWebFetchURLSourceOnly or BetaManagedAgentsWebFetchURLSourceExcept`

              Which custom tools' results contribute URLs that may be fetched. Null when not set, which allows every custom tool's results.

              - `beta_managed_agents_web_fetch_url_source_all: object`

                Every URL from this source may be fetched. This is the default.

                - `type: "all"`

              - `beta_managed_agents_web_fetch_url_source_none: object`

                This source contributes no URLs that may be fetched.

                - `type: "none"`

              - `beta_managed_agents_web_fetch_url_source_only: object`

                Only the named tools' results contribute URLs that may be fetched.

                - `type: "only"`

                - `tools: array of BetaManagedAgentsWebFetchURLSourceToolReference`

                  The tools whose results contribute. Between 1 and 128 entries, each with a different name. An empty list is rejected; use "none" to allow no tool's results.

                  - `type: "tool_reference"`

                    Must be "tool_reference".

                  - `name: string`

                    Name of the tool. Compared exactly, so upper and lower case letters are different.

                    minLength: 1, maxLength: 128

              - `beta_managed_agents_web_fetch_url_source_except: object`

                Every tool's results contribute URLs that may be fetched, except the named tools' results.

                - `type: "except"`

                - `tools: array of BetaManagedAgentsWebFetchURLSourceToolReference`

                  The tools whose results do not contribute. Between 1 and 128 entries, each with a different name. An empty list is rejected; use "all" to leave out no tool's results.

                  - `type: "tool_reference"`

                    Must be "tool_reference".

                  - `name: string`

                    Name of the tool. Compared exactly, so upper and lower case letters are different.

                    minLength: 1, maxLength: 128

            - `server_tool_results: BetaManagedAgentsWebFetchURLSourceAll or BetaManagedAgentsWebFetchURLSourceNone or BetaManagedAgentsWebFetchURLSourceOnly or BetaManagedAgentsWebFetchURLSourceExcept`

              Which of the web_search and web_fetch tools' results contribute URLs that may be fetched. Null when not set, which allows both.

            - `user_input: BetaManagedAgentsWebFetchURLSourceAll or BetaManagedAgentsWebFetchURLSourceNone`

              Whether URLs in the text of user messages may be fetched. Null when not set, which allows them.

              - `beta_managed_agents_web_fetch_url_source_all: object`

                Every URL from this source may be fetched. This is the default.

              - `beta_managed_agents_web_fetch_url_source_none: object`

                This source contributes no URLs that may be fetched.

          - `allowed_domains: optional array of string`

          - `blocked_domains: optional array of string`

          - `max_content_tokens: optional number`

            format: int32

        - `beta_managed_agents_web_search_tool_config: object`

          Configuration for the web_search tool.

          - `type: "web_search"`

          - `enabled: boolean`

          - `name: "web_search"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object`

              Tool calls require user confirmation before execution.

            - `beta_managed_agents_auto_policy: object`

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

          - `allowed_domains: optional array of string`

          - `blocked_domains: optional array of string`

          - `user_location: optional object`

            Approximate user location for search result localization.

            - `type: "approximate"`

              Location precision. Only "approximate" is supported.

            - `city: optional string`

              City name.

              minLength: 1, maxLength: 255

            - `country: optional string`

              Two-letter ISO 3166-1 country code, uppercase.

              pattern: ^[A-Z]{2}$

            - `region: optional string`

              Region or state name.

              minLength: 1, maxLength: 255

            - `timezone: optional string`

              IANA timezone identifier, e.g. "America/Los_Angeles".

              minLength: 1, maxLength: 255

      - `default_config: object`

        Resolved default configuration for agent tools.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object`

            Tool calls are automatically approved without user confirmation.

          - `beta_managed_agents_always_ask_policy: object`

            Tool calls require user confirmation before execution.

          - `beta_managed_agents_auto_policy: object`

            The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

    - `beta_managed_agents_mcp_toolset: object`

      - `type: "mcp_toolset"`

      - `configs: array of BetaManagedAgentsMCPToolConfig`

        - `enabled: boolean`

        - `name: string`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object`

            Tool calls are automatically approved without user confirmation.

          - `beta_managed_agents_always_ask_policy: object`

            Tool calls require user confirmation before execution.

          - `beta_managed_agents_auto_policy: object`

            The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

      - `default_config: object`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy or BetaManagedAgentsAutoPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object`

            Tool calls are automatically approved without user confirmation.

          - `beta_managed_agents_always_ask_policy: object`

            Tool calls require user confirmation before execution.

          - `beta_managed_agents_auto_policy: object`

            The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask, or for some causes to deny, for example when the organization is out of credits or has reached a spend limit.

      - `mcp_server_name: string`

    - `beta_managed_agents_custom_tool: object`

      A custom tool as returned in API responses.

      - `type: "custom"`

      - `description: string`

      - `input_schema: object`

        JSON Schema for custom tool input parameters.

        - `type: "object"`

        - `properties: optional map[unknown]`

        - `required: optional array of string`

      - `name: string`

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `version: number`

    The agent's current version. Starts at 1 and increments when the agent is modified.

    format: int32

## Example

```bash
ant beta:agents create \
  --model claude-opus-5-5 \
  --name 'My First Agent'
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
