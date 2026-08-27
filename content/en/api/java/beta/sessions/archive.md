# Archive Session

`BetaManagedAgentsSession beta().sessions().archive(params = SessionArchiveParams.none(), requestOptions = RequestOptions.none())`

**POST** `/v1/sessions/{session_id}/archive`

Archive Session

## Parameters

- `SessionArchiveParams params`

  - `Optional<String> sessionId`

  - `Optional<List<AnthropicBeta>> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `SKILLS_2025_10_02("skills-2025-10-02")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

    - `DREAMING_2026_04_21("dreaming-2026-04-21")`

    - `THINKING_TOKEN_COUNT_2026_05_13("thinking-token-count-2026-05-13")`

    - `SERVER_SIDE_FALLBACK_2026_06_01("server-side-fallback-2026-06-01")`

    - `SERVER_SIDE_FALLBACK_2026_07_01("server-side-fallback-2026-07-01")`

    - `FALLBACK_CREDIT_2026_06_01("fallback-credit-2026-06-01")`

    - `FALLBACK_CREDIT_2026_07_01("fallback-credit-2026-07-01")`

    - `AGENT_MEMORY_2026_07_22("agent-memory-2026-07-22")`

    - `MID_CONVERSATION_TOOL_CHANGES_2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `COMPACT_2026_01_12("compact-2026-01-12")`

    - `COMPUTER_USE_2025_11_24("computer-use-2025-11-24")`

    - `MCP_TUNNELS_2026_06_22("mcp-tunnels-2026-06-22")`

    - `STRUCTURED_OUTPUTS_2025_11_13("structured-outputs-2025-11-13")`

    - `TASK_BUDGETS_2026_03_13("task-budgets-2026-03-13")`

    - `THINKING_DISPLAY_UPDATES_2026_08_18("thinking-display-updates-2026-08-18")`

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

## Returns

- `class BetaManagedAgentsSession:`

  A Managed Agents `session`.

  - `String id`

  - `BetaManagedAgentsSessionAgent agent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `String id`

    - `Optional<String> description`

    - `List<BetaManagedAgentsMcpServerUrlDefinition> mcpServers`

      - `String name`

      - `Type type`

      - `String url`

    - `BetaManagedAgentsModelConfig model`

      Model identifier and configuration.

      - `BetaManagedAgentsModel id`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

        - `CLAUDE_SONNET_5("claude-sonnet-5")`

          High-performance model for coding and agents

        - `CLAUDE_FABLE_5("claude-fable-5")`

          Next generation of intelligence for the hardest knowledge work and coding problems

        - `CLAUDE_OPUS_5("claude-opus-5")`

          Powerful intelligence for long-running agents and coding

        - `CLAUDE_OPUS_4_8("claude-opus-4-8")`

          Powerful intelligence for long-running agents and coding

        - `CLAUDE_OPUS_4_7("claude-opus-4-7")`

          Powerful intelligence for long-running agents and coding

        - `CLAUDE_OPUS_4_6("claude-opus-4-6")`

          Powerful intelligence for long-running agents and coding

        - `CLAUDE_SONNET_4_6("claude-sonnet-4-6")`

          Best combination of speed and intelligence

        - `CLAUDE_HAIKU_4_5("claude-haiku-4-5")`

          Fastest model with near-frontier intelligence

        - `CLAUDE_HAIKU_4_5_20251001("claude-haiku-4-5-20251001")`

          Fastest model with near-frontier intelligence

        - `CLAUDE_OPUS_4_5("claude-opus-4-5")`

          Powerful intelligence for long-running agents and coding

        - `CLAUDE_OPUS_4_5_20251101("claude-opus-4-5-20251101")`

          Powerful intelligence for long-running agents and coding

        - `CLAUDE_SONNET_4_5("claude-sonnet-4-5")`

          High-performance model for agents and coding

        - `CLAUDE_SONNET_4_5_20250929("claude-sonnet-4-5-20250929")`

          High-performance model for agents and coding

      - `Optional<Effort> effort`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

        - `class BetaManagedAgentsEffortLow:`

          Low effort. Favors latency over reasoning depth.

          - `Type type`

        - `class BetaManagedAgentsEffortMedium:`

          Medium effort. Balances latency and reasoning depth.

          - `Type type`

        - `class BetaManagedAgentsEffortHigh:`

          High effort. Favors reasoning depth.

          - `Type type`

        - `class BetaManagedAgentsEffortXhigh:`

          Extra-high effort. Not all models accept this level.

          - `Type type`

        - `class BetaManagedAgentsEffortMax:`

          Maximum effort. Favors reasoning depth over latency.

          - `Type type`

      - `Optional<String> inferenceGeo`

        Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

      - `Optional<Speed> speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `STANDARD("standard")`

        - `FAST("fast")`

    - `Optional<BetaManagedAgentsSessionMultiagentCoordinator> multiagent`

      Resolved coordinator topology with full agent definitions for each roster member.

      - `List<Agent> agents`

        Full `agent` definitions the coordinator may spawn as session threads.

        - `class BetaManagedAgentsSessionThreadAgent:`

          Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

          - `String id`

          - `Optional<String> description`

          - `List<BetaManagedAgentsMcpServerUrlDefinition> mcpServers`

            - `String name`

            - `Type type`

            - `String url`

          - `BetaManagedAgentsModelConfig model`

            Model identifier and configuration.

          - `String name`

          - `List<Skill> skills`

            - `class BetaManagedAgentsAnthropicSkill:`

              A resolved Anthropic-managed skill.

              - `String skillId`

              - `Type type`

              - `String version`

            - `class BetaManagedAgentsCustomSkill:`

              A resolved user-created custom skill.

              - `String skillId`

              - `Type type`

              - `String version`

          - `Optional<String> system`

          - `List<Tool> tools`

            - `class BetaManagedAgentsAgentToolset20260401:`

              - `List<BetaManagedAgentsAgentToolConfig> configs`

                - `class BetaManagedAgentsBashToolConfig:`

                  Configuration for the bash tool.

                  - `boolean enabled`

                  - `JsonValue name constant`

                  - `PermissionPolicy permissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                      - `Type type`

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                      - `Type type`

                  - `JsonValue type constant`

                - `class BetaManagedAgentsEditToolConfig:`

                  Configuration for the edit tool.

                  - `boolean enabled`

                  - `JsonValue name constant`

                  - `PermissionPolicy permissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonValue type constant`

                - `class BetaManagedAgentsReadToolConfig:`

                  Configuration for the read tool.

                  - `boolean enabled`

                  - `JsonValue name constant`

                  - `PermissionPolicy permissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonValue type constant`

                - `class BetaManagedAgentsWriteToolConfig:`

                  Configuration for the write tool.

                  - `boolean enabled`

                  - `JsonValue name constant`

                  - `PermissionPolicy permissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonValue type constant`

                - `class BetaManagedAgentsGlobToolConfig:`

                  Configuration for the glob tool.

                  - `boolean enabled`

                  - `JsonValue name constant`

                  - `PermissionPolicy permissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonValue type constant`

                - `class BetaManagedAgentsGrepToolConfig:`

                  Configuration for the grep tool.

                  - `boolean enabled`

                  - `JsonValue name constant`

                  - `PermissionPolicy permissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonValue type constant`

                - `class BetaManagedAgentsWebFetchToolConfig:`

                  Configuration for the web_fetch tool.

                  - `boolean enabled`

                  - `JsonValue name constant`

                  - `PermissionPolicy permissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonValue type constant`

                  - `Optional<List<String>> allowedDomains`

                  - `Optional<List<String>> blockedDomains`

                  - `Optional<Long> maxContentTokens`

                    format: int32

                - `class BetaManagedAgentsWebSearchToolConfig:`

                  Configuration for the web_search tool.

                  - `boolean enabled`

                  - `JsonValue name constant`

                  - `PermissionPolicy permissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                  - `JsonValue type constant`

                  - `Optional<List<String>> allowedDomains`

                  - `Optional<List<String>> blockedDomains`

                  - `Optional<BetaManagedAgentsUserLocation> userLocation`

                    Approximate user location for search result localization.

                    - `JsonValue type constant`

                      Location precision. Only "approximate" is supported.

                    - `Optional<String> city`

                      City name.

                      minLength: 1, maxLength: 255

                    - `Optional<String> country`

                      Two-letter ISO 3166-1 country code, uppercase.

                    - `Optional<String> region`

                      Region or state name.

                      minLength: 1, maxLength: 255

                    - `Optional<String> timezone`

                      IANA timezone identifier, e.g. "America/Los_Angeles".

                      minLength: 1, maxLength: 255

              - `BetaManagedAgentsAgentToolsetDefaultConfig defaultConfig`

                Resolved default configuration for agent tools.

                - `boolean enabled`

                - `PermissionPolicy permissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy:`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy:`

                    Tool calls require user confirmation before execution.

              - `Type type`

            - `class BetaManagedAgentsMcpToolset:`

              - `List<BetaManagedAgentsMcpToolConfig> configs`

                - `boolean enabled`

                - `String name`

                - `PermissionPolicy permissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy:`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy:`

                    Tool calls require user confirmation before execution.

              - `BetaManagedAgentsMcpToolsetDefaultConfig defaultConfig`

                Resolved default configuration for all tools from an MCP server.

                - `boolean enabled`

                - `PermissionPolicy permissionPolicy`

                  Permission policy for tool execution.

                  - `class BetaManagedAgentsAlwaysAllowPolicy:`

                    Tool calls are automatically approved without user confirmation.

                  - `class BetaManagedAgentsAlwaysAskPolicy:`

                    Tool calls require user confirmation before execution.

              - `String mcpServerName`

              - `Type type`

            - `class BetaManagedAgentsCustomTool:`

              A custom tool as returned in API responses.

              - `String description`

              - `BetaManagedAgentsCustomToolInputSchema inputSchema`

                JSON Schema for custom tool input parameters.

                - `JsonValue type constant`

                - `Optional<Properties> properties`

                - `Optional<List<String>> required`

              - `String name`

              - `Type type`

          - `Type type`

          - `long version`

            format: int32

        - `class BetaManagedAgentsAdvisor:`

          Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

          - `String model`

            The advisor model id.

          - `Type type`

      - `Type type`

    - `String name`

    - `List<Skill> skills`

      - `class BetaManagedAgentsAnthropicSkill:`

        A resolved Anthropic-managed skill.

      - `class BetaManagedAgentsCustomSkill:`

        A resolved user-created custom skill.

    - `Optional<String> system`

    - `List<Tool> tools`

      - `class BetaManagedAgentsAgentToolset20260401:`

      - `class BetaManagedAgentsMcpToolset:`

      - `class BetaManagedAgentsCustomTool:`

        A custom tool as returned in API responses.

    - `Type type`

    - `long version`

      format: int32

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<BetaManagedAgentsBudgetLimit> budget`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `BetaMonetaryAmount maxListCost`

      A monetary amount in a specific currency.

      - `String amount`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `BetaCurrency currency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `Type type`

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String environmentId`

  - `Metadata metadata`

  - `List<BetaManagedAgentsOutcomeEvaluationResource> outcomeEvaluations`

    Per-outcome evaluation state. One entry per define_outcome event sent to the session.

    - `Optional<LocalDateTime> completedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String description`

      What the agent should produce.

    - `Optional<String> explanation`

      Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs_revision (intermediate), what's missing; for failed, why unrecoverable.

    - `long iteration`

      0-indexed revision cycle the outcome is currently on.

      format: int32

    - `String outcomeId`

      Server-generated outc_ ID for this outcome.

    - `String result`

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

    - `Type type`

  - `List<BetaManagedAgentsSessionResource> resources`

    - `class BetaManagedAgentsGitHubRepositoryResource:`

      - `String id`

      - `LocalDateTime createdAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `String mountPath`

      - `Type type`

      - `LocalDateTime updatedAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `String url`

      - `Optional<Checkout> checkout`

        - `class BetaManagedAgentsBranchCheckout:`

          - `String name`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `Type type`

        - `class BetaManagedAgentsCommitCheckout:`

          - `String sha`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `Type type`

    - `class BetaManagedAgentsFileResource:`

      - `String id`

      - `LocalDateTime createdAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `String fileId`

      - `String mountPath`

      - `Type type`

      - `LocalDateTime updatedAt`

        A timestamp in RFC 3339 format

        format: date-time

    - `class BetaManagedAgentsMemoryStoreResource:`

      A memory store attached to an agent session.

      - `String memoryStoreId`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type type`

      - `Optional<Access> access`

        Access mode for an attached memory store.

        - `READ_WRITE("read_write")`

        - `READ_ONLY("read_only")`

      - `Optional<String> description`

        Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

      - `Optional<String> instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

        maxLength: 4096

      - `Optional<String> mountPath`

        Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

      - `Optional<String> name`

        Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

  - `BetaManagedAgentsSessionStats stats`

    Timing statistics for a session.

    - `Optional<Double> activeSeconds`

      Cumulative time in seconds the session spent in running status. Excludes idle time.

      format: double

    - `Optional<Double> durationSeconds`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

      format: double

  - `Status status`

    SessionStatus enum

    - `RESCHEDULING("rescheduling")`

    - `RUNNING("running")`

    - `IDLE("idle")`

    - `TERMINATED("terminated")`

  - `Optional<String> title`

  - `Type type`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `BetaManagedAgentsSessionUsage usage`

    Cumulative token usage for a session across all turns.

    - `Optional<Double> activeSeconds`

      Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once, unlike `stats.active_seconds`, which sums each thread's own active time. This is the duration the session's runtime cost is priced on.

      format: double

    - `Optional<BetaManagedAgentsCacheCreationUsage> cacheCreation`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `Optional<Long> ephemeral1hInputTokens`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `Optional<Long> ephemeral5mInputTokens`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `Optional<Long> cacheReadInputTokens`

      Total tokens read from prompt cache.

      format: int32

    - `Optional<Long> inputTokens`

      Total input tokens consumed across all turns.

      format: int32

    - `Optional<BetaMonetaryAmount> listCost`

      A monetary amount in a specific currency.

    - `Optional<Long> outputTokens`

      Total output tokens generated across all turns.

      format: int32

    - `Optional<BetaManagedAgentsServerToolUsage> serverToolUse`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `Optional<Long> webFetchRequests`

        Number of server-executed web fetch requests.

        format: int32

      - `Optional<Long> webSearchRequests`

        Number of server-executed web search requests.

        format: int32

  - `List<String> vaultIds`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `Optional<String> deploymentId`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

## Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.sessions.BetaManagedAgentsSession;
import com.anthropic.models.beta.sessions.SessionArchiveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsSession betaManagedAgentsSession = client.beta().sessions().archive("sesn_011CZkZAtmR3yMPDzynEDxu7");
    }
}
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
