# List Agent Versions

`client.beta.agents.versions.list(agentID, params?, options?): PageCursor<BetaManagedAgentsAgent>`

**GET** `/v1/agents/{agent_id}/versions`

List Agent Versions

## Parameters

- `agentID: string`

- `params: VersionListParams`

  - `limit?: number`

    Query param: Maximum results per page. Default 20, maximum 100.

    format: int32

  - `page?: string`

    Query param: Opaque pagination cursor.

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 38 more`

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

## Returns

- `BetaManagedAgentsAgent`

  A Managed Agents `agent`.

  - `id: string`

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `description: string | null`

  - `mcp_servers: Array<BetaManagedAgentsMCPServerURLDefinition>`

    - `name: string`

    - `type: "url"`

    - `url: string`

  - `metadata: Record<string, string>`

  - `model: BetaManagedAgentsModelConfig`

    Model identifier and configuration.

    - `id: BetaManagedAgentsModel`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

      - `"claude-sonnet-5" | "claude-fable-5" | "claude-opus-5" | 10 more`

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

      - `(string & {})`

    - `effort?: BetaManagedAgentsEffortLow | BetaManagedAgentsEffortMedium | BetaManagedAgentsEffortHigh | 2 more`

      How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

      - `BetaManagedAgentsEffortLow`

        Low effort. Favors latency over reasoning depth.

        - `type: "low"`

      - `BetaManagedAgentsEffortMedium`

        Medium effort. Balances latency and reasoning depth.

        - `type: "medium"`

      - `BetaManagedAgentsEffortHigh`

        High effort. Favors reasoning depth.

        - `type: "high"`

      - `BetaManagedAgentsEffortXhigh`

        Extra-high effort. Not all models accept this level.

        - `type: "xhigh"`

      - `BetaManagedAgentsEffortMax`

        Maximum effort. Favors reasoning depth over latency.

        - `type: "max"`

    - `inference_geo?: string`

      Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

    - `speed?: "standard" | "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `multiagent: BetaManagedAgentsMultiagent | null`

    Resolved coordinator topology with a concrete agent roster.

    - `agents: Array<BetaManagedAgentsAgentReference | BetaManagedAgentsAdvisor>`

      Agents the coordinator may spawn as session threads, each resolved to a specific version.

      - `BetaManagedAgentsAgentReference`

        A resolved agent reference with a concrete version.

        - `id: string`

        - `type: "agent"`

        - `version: number`

          format: int32

      - `BetaManagedAgentsAdvisor`

        Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

        - `model: string`

          The advisor model id.

        - `type: "advisor"`

    - `type: "coordinator"`

  - `name: string`

  - `skills: Array<BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill>`

    - `BetaManagedAgentsAnthropicSkill`

      A resolved Anthropic-managed skill.

      - `skill_id: string`

      - `type: "anthropic"`

      - `version: string`

    - `BetaManagedAgentsCustomSkill`

      A resolved user-created custom skill.

      - `skill_id: string`

      - `type: "custom"`

      - `version: string`

  - `system: string | null`

  - `tools: Array<BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool>`

    - `BetaManagedAgentsAgentToolset20260401`

      - `configs: Array<BetaManagedAgentsAgentToolConfig>`

        - `BetaManagedAgentsBashToolConfig`

          Configuration for the bash tool.

          - `enabled: boolean`

          - `name: "bash"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

            - `BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

          - `type: "bash"`

        - `BetaManagedAgentsEditToolConfig`

          Configuration for the edit tool.

          - `enabled: boolean`

          - `name: "edit"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: "edit"`

        - `BetaManagedAgentsReadToolConfig`

          Configuration for the read tool.

          - `enabled: boolean`

          - `name: "read"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: "read"`

        - `BetaManagedAgentsWriteToolConfig`

          Configuration for the write tool.

          - `enabled: boolean`

          - `name: "write"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: "write"`

        - `BetaManagedAgentsGlobToolConfig`

          Configuration for the glob tool.

          - `enabled: boolean`

          - `name: "glob"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: "glob"`

        - `BetaManagedAgentsGrepToolConfig`

          Configuration for the grep tool.

          - `enabled: boolean`

          - `name: "grep"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: "grep"`

        - `BetaManagedAgentsWebFetchToolConfig`

          Configuration for the web_fetch tool.

          - `enabled: boolean`

          - `name: "web_fetch"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: "web_fetch"`

          - `allowed_domains?: Array<string>`

          - `blocked_domains?: Array<string>`

          - `max_content_tokens?: number | null`

            format: int32

        - `BetaManagedAgentsWebSearchToolConfig`

          Configuration for the web_search tool.

          - `enabled: boolean`

          - `name: "web_search"`

          - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `BetaManagedAgentsAlwaysAllowPolicy`

              Tool calls are automatically approved without user confirmation.

            - `BetaManagedAgentsAlwaysAskPolicy`

              Tool calls require user confirmation before execution.

          - `type: "web_search"`

          - `allowed_domains?: Array<string>`

          - `blocked_domains?: Array<string>`

          - `user_location?: BetaManagedAgentsUserLocation | null`

            Approximate user location for search result localization.

            - `type: "approximate"`

              Location precision. Only "approximate" is supported.

            - `city?: string | null`

              City name.

              minLength: 1, maxLength: 255

            - `country?: string | null`

              Two-letter ISO 3166-1 country code, uppercase.

            - `region?: string | null`

              Region or state name.

              minLength: 1, maxLength: 255

            - `timezone?: string | null`

              IANA timezone identifier, e.g. "America/Los_Angeles".

              minLength: 1, maxLength: 255

      - `default_config: BetaManagedAgentsAgentToolsetDefaultConfig`

        Resolved default configuration for agent tools.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `type: "agent_toolset_20260401"`

    - `BetaManagedAgentsMCPToolset`

      - `configs: Array<BetaManagedAgentsMCPToolConfig>`

        - `enabled: boolean`

        - `name: string`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `default_config: BetaManagedAgentsMCPToolsetDefaultConfig`

        Resolved default configuration for all tools from an MCP server.

        - `enabled: boolean`

        - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `BetaManagedAgentsAlwaysAllowPolicy`

            Tool calls are automatically approved without user confirmation.

          - `BetaManagedAgentsAlwaysAskPolicy`

            Tool calls require user confirmation before execution.

      - `mcp_server_name: string`

      - `type: "mcp_toolset"`

    - `BetaManagedAgentsCustomTool`

      A custom tool as returned in API responses.

      - `description: string`

      - `input_schema: BetaManagedAgentsCustomToolInputSchema`

        JSON Schema for custom tool input parameters.

        - `type: "object"`

        - `properties?: Record<string, unknown> | null`

        - `required?: Array<string> | null`

      - `name: string`

      - `type: "custom"`

  - `type: "agent"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `version: number`

    The agent's current version. Starts at 1 and increments when the agent is modified.

    format: int32

## Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaManagedAgentsAgent of client.beta.agents.versions.list(
  "agent_011CZkYpogX7uDKUyvBTophP"
)) {
  console.log(betaManagedAgentsAgent.id);
}
```

### Response (200)

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
