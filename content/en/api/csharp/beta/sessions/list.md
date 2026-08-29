# List Sessions

`SessionListPage Beta.Sessions.List(parameters, cancellationToken = default)`

**GET** `/v1/sessions`

List Sessions

## Parameters

- `SessionListParams parameters`

  - `string agentID`

    Query param: Filter sessions created with this agent ID.

  - `int agentVersion`

    Query param: Filter by agent version. Only applies when agent_id is also set.

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

    Query param: Filter sessions whose resources contain a memory_store with this memory store ID.

  - `Order order`

    Query param: Sort direction for results, ordered by created_at. Defaults to desc (newest first).

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

## Returns

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

    Per-outcome evaluation state. One entry per define_outcome event sent to the session.

    - `required DateTimeOffset? CompletedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string Description`

      What the agent should produce.

    - `required string? Explanation`

      Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs_revision (intermediate), what's missing; for failed, why unrecoverable.

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

      Cumulative time in seconds the session spent in running status. Excludes idle time.

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

## Example

```csharp
SessionListParams parameters = new();

var page = await client.Beta.Sessions.List(parameters);
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
