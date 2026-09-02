# Get Agent

`beta.agents.retrieve(agent_id, **kwargs)  -> BetaManagedAgentsAgent`

**GET** `/v1/agents/{agent_id}`

Get Agent

## Parameters

- `agent_id: str`

- `version: Optional[int]`

  Agent version. Omit for the most recent version. Must be at least 1 if specified.

  format: int32

- `betas: Optional[List[AnthropicBetaParam]]`

  Optional header to specify the beta version(s) you want to use.

  - `str`

  - `Literal["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 41 more]`

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

## Returns

- `class BetaManagedAgentsAgent: …`

  A Managed Agents `agent`.

  - `id: str`

  - `archived_at: Optional[datetime]`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: datetime`

    A timestamp in RFC 3339 format

    format: date-time

  - `description: Optional[str]`

  - `mcp_servers: List[BetaManagedAgentsMCPServerURLDefinition]`

    - `name: str`

    - `type: Literal["url"]`

    - `url: str`

  - `metadata: Dict[str, str]`

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

  - `multiagent: Optional[BetaManagedAgentsMultiagent]`

    Resolved coordinator topology with a concrete agent roster.

    - `agents: List[Agent]`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `class BetaManagedAgentsAgentReference: …`

        A resolved agent reference with a concrete version.

        - `id: str`

        - `type: Literal["agent"]`

        - `version: int`

          format: int32

      - `class BetaManagedAgentsAdvisor: …`

        Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

        - `model: str`

          The advisor model id.

        - `type: Literal["advisor"]`

    - `type: Literal["coordinator"]`

  - `name: str`

  - `skills: List[Skill]`

    - `class BetaManagedAgentsAnthropicSkill: …`

      A resolved Anthropic-managed skill.

      - `skill_id: str`

      - `type: Literal["anthropic"]`

      - `version: str`

    - `class BetaManagedAgentsCustomSkill: …`

      A resolved user-created custom skill.

      - `skill_id: str`

      - `type: Literal["custom"]`

      - `version: str`

  - `system: Optional[str]`

  - `tools: List[Tool]`

    - `class BetaManagedAgentsAgentToolset20260401: …`

      - `configs: List[BetaManagedAgentsAgentToolConfig]`

        - `class BetaManagedAgentsBashToolConfig: …`

          Configuration for the bash tool.

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

          - `type: Literal["bash"]`

        - `class BetaManagedAgentsEditToolConfig: …`

          Configuration for the edit tool.

          - `enabled: bool`

          - `name: Literal["edit"]`

          - `permission_policy: PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

          - `type: Literal["edit"]`

        - `class BetaManagedAgentsReadToolConfig: …`

          Configuration for the read tool.

          - `enabled: bool`

          - `name: Literal["read"]`

          - `permission_policy: PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

          - `type: Literal["read"]`

        - `class BetaManagedAgentsWriteToolConfig: …`

          Configuration for the write tool.

          - `enabled: bool`

          - `name: Literal["write"]`

          - `permission_policy: PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

          - `type: Literal["write"]`

        - `class BetaManagedAgentsGlobToolConfig: …`

          Configuration for the glob tool.

          - `enabled: bool`

          - `name: Literal["glob"]`

          - `permission_policy: PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

          - `type: Literal["glob"]`

        - `class BetaManagedAgentsGrepToolConfig: …`

          Configuration for the grep tool.

          - `enabled: bool`

          - `name: Literal["grep"]`

          - `permission_policy: PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

          - `type: Literal["grep"]`

        - `class BetaManagedAgentsWebFetchToolConfig: …`

          Configuration for the web_fetch tool.

          - `enabled: bool`

          - `name: Literal["web_fetch"]`

          - `permission_policy: PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

          - `type: Literal["web_fetch"]`

          - `allowed_domains: Optional[List[str]]`

          - `blocked_domains: Optional[List[str]]`

          - `max_content_tokens: Optional[int]`

            format: int32

        - `class BetaManagedAgentsWebSearchToolConfig: …`

          Configuration for the web_search tool.

          - `enabled: bool`

          - `name: Literal["web_search"]`

          - `permission_policy: PermissionPolicy`

            Permission policy for tool execution.

            - `class BetaManagedAgentsAlwaysAllowPolicy: …`

              Tool calls are automatically approved without user confirmation.

            - `class BetaManagedAgentsAlwaysAskPolicy: …`

              Tool calls require user confirmation before execution.

          - `type: Literal["web_search"]`

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

      - `type: Literal["agent_toolset_20260401"]`

    - `class BetaManagedAgentsMCPToolset: …`

      - `configs: List[BetaManagedAgentsMCPToolConfig]`

        - `enabled: bool`

        - `name: str`

        - `permission_policy: PermissionPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy: …`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy: …`

            Tool calls require user confirmation before execution.

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: bool`

        - `permission_policy: PermissionPolicy`

          Permission policy for tool execution.

          - `class BetaManagedAgentsAlwaysAllowPolicy: …`

            Tool calls are automatically approved without user confirmation.

          - `class BetaManagedAgentsAlwaysAskPolicy: …`

            Tool calls require user confirmation before execution.

      - `mcp_server_name: str`

      - `type: Literal["mcp_toolset"]`

    - `class BetaManagedAgentsCustomTool: …`

      A custom tool as returned in API responses.

      - `description: str`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `type: Literal["object"]`

        - `properties: Optional[Dict[str, object]]`

        - `required: Optional[List[str]]`

      - `name: str`

      - `type: Literal["custom"]`

  - `type: Literal["agent"]`

  - `updated_at: datetime`

    A timestamp in RFC 3339 format

    format: date-time

  - `version: int`

    The agent's current version. Starts at 1 and increments when the agent is modified.

    format: int32

## Example

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get(
        "ANTHROPIC_API_KEY"
    ),  # This is the default and can be omitted
)
beta_managed_agents_agent = client.beta.agents.retrieve(
    agent_id="agent_011CZkYpogX7uDKUyvBTophP",
)
print(beta_managed_agents_agent.id)
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
