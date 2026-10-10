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

  Model identifier. Accepts the [model string](https://platform.claude.com/docs/en/about-claude/models/overview#latest-models-comparison), e.g. `claude-opus-5`, or a `model_config` object for additional configuration control

- `--name: string`

  Human-readable name for the agent.

  minLength: 1, maxLength: 256

- `--description: optional string`

  Description of what the agent does.

  maxLength: 2048

- `--mcp-server: optional array of BetaManagedAgentsURLMCPServerParams`

  MCP servers this agent connects to. Maximum 20. Names must be unique within the array. Every server must be referenced by an `mcp_toolset` in `tools`; unreferenced servers are rejected. See the [MCP connector guide](https://platform.claude.com/docs/en/managed-agents/mcp-connector).

- `--metadata: optional map[string]`

  Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `--multiagent: optional BetaManagedAgentsMultiagentCoordinatorParams or BetaManagedAgentsMultiagent20261001Params`

  Multiagent orchestration configuration.

- `--skill: optional array of BetaManagedAgentsSkillParams`

  Skills available to the agent.

- `--system: optional string`

  System prompt for the agent.

  maxLength: 100000

- `--tool: optional array of BetaManagedAgentsAgentToolset20260401Params or BetaManagedAgentsMCPToolsetParams or BetaManagedAgentsCustomToolParams`

  Tool configurations available to the agent. Maximum of 256 tools across all toolsets allowed.

- `--beta: optional array of AnthropicBeta` (header parameter)

  Optional header to specify the beta version(s) you want to use.

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

  - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

    - `type: "url"`

    - `name: string`

    - `url: string`

  - `metadata: map[string]`

  - `model: object`

    Model identifier and configuration.

    - `id: "claude-haiku-5-5" or "claude-sonnet-5-5" or "claude-opus-5-5" or 14 more or string`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

            - `beta_managed_agents_multiagent_inline_agents_enabled: object`

              The agent can define inline agents.

            - `beta_managed_agents_multiagent_inline_agents_disabled: object`

              The agent cannot define inline agents.

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

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

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

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

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

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

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

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

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

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

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

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

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

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

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

              - `beta_managed_agents_web_fetch_url_source_all: object`

                Every URL from this source may be fetched. This is the default.

              - `beta_managed_agents_web_fetch_url_source_none: object`

                This source contributes no URLs that may be fetched.

              - `beta_managed_agents_web_fetch_url_source_only: object`

                Only the named tools' results contribute URLs that may be fetched.

              - `beta_managed_agents_web_fetch_url_source_except: object`

                Every tool's results contribute URLs that may be fetched, except the named tools' results.

            - `user_input: BetaManagedAgentsWebFetchURLSourceAll or BetaManagedAgentsWebFetchURLSourceNone`

              Whether URLs in the text of user messages may be fetched. Null when not set, which allows them.

              - `beta_managed_agents_web_fetch_url_source_all: object`

                Every URL from this source may be fetched. This is the default.

                - `type: "all"`

              - `beta_managed_agents_web_fetch_url_source_none: object`

                This source contributes no URLs that may be fetched.

                - `type: "none"`

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

              The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

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

            The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

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

            The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

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

            The server decides each tool call individually: it judges, from the tool, its input, and the session content so far, whether the call is safe to execute or high-risk, and evaluates it to allow when judged safe and to deny when judged high-risk. A call the server cannot reach a judgement on evaluates to ask.

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
  --api-key my-anthropic-api-key \
  --model claude-opus-5 \
  --name 'My First Agent'
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
