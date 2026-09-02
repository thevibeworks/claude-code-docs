# List Agents

`AgentListPage Beta.Agents.List(parameters, cancellationToken = default)`

**GET** `/v1/agents`

List Agents

## Parameters

- `AgentListParams parameters`

  - `DateTimeOffset createdAtGte`

    Query param: Return agents created at or after this time (inclusive).

    format: date-time

  - `DateTimeOffset createdAtLte`

    Query param: Return agents created at or before this time (inclusive).

    format: date-time

  - `bool includeArchived`

    Query param: Include archived agents in results. Defaults to false.

  - `int limit`

    Query param: Maximum results per page. Default 20, maximum 100.

    format: int32

  - `string page`

    Query param: Opaque pagination cursor from a previous response.

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

## Returns

- `class BetaManagedAgentsAgent:`

  A Managed Agents `agent`.

  - `required string ID`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string? Description`

  - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

    - `required string Name`

    - `required Type Type`

    - `required string Url`

  - `required IReadOnlyDictionary<string, string> Metadata`

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

  - `required BetaManagedAgentsMultiagent? Multiagent`

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

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required int Version`

    The agent's current version. Starts at 1 and increments when the agent is modified.

    format: int32

## Example

```csharp
AgentListParams parameters = new();

var page = await client.Beta.Agents.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
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
