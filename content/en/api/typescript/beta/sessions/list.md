---
title: List Sessions
url: https://platform.claude.com/docs/en/api/typescript/beta/sessions/list
---

## List Sessions

`client.beta.sessions.list(SessionListParamsparams?, RequestOptionsoptions?): BidirectionalPageCursor<BetaManagedAgentsSession>`

**get** `/v1/sessions`

List Sessions

### Parameters

- `params: SessionListParams`

  - `agent_id?: string`

    Query param: Filter sessions created with this agent ID.

  - `agent_version?: number`

    Query param: Filter by agent version. Only applies when agent_id is also set.

  - `"created_at[gt]"?: string`

    Query param: Return sessions created after this time (exclusive).

  - `"created_at[gte]"?: string`

    Query param: Return sessions created at or after this time (inclusive).

  - `"created_at[lt]"?: string`

    Query param: Return sessions created before this time (exclusive).

  - `"created_at[lte]"?: string`

    Query param: Return sessions created at or before this time (inclusive).

  - `deployment_id?: string`

    Query param: Filter sessions created by this deployment ID.

  - `include_archived?: boolean`

    Query param: When true, includes archived sessions. Default: false (exclude archived).

  - `limit?: number`

    Query param: Maximum number of results to return.

  - `memory_store_id?: string`

    Query param: Filter sessions whose resources contain a memory_store with this memory store ID.

  - `order?: "asc" | "desc"`

    Query param: Sort direction for results, ordered by created_at. Defaults to desc (newest first).

    - `"asc"`

    - `"desc"`

  - `page?: string`

    Query param: Opaque pagination cursor from a previous response.

  - `statuses?: Array<"rescheduling" | "running" | "idle" | "terminated">`

    Query param: Filter by session status. Repeat the parameter to match any of multiple statuses.

    - `"rescheduling"`

    - `"running"`

    - `"idle"`

    - `"terminated"`

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 31 more`

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

### Returns

- `BetaManagedAgentsSession`

  A Managed Agents `session`.

  - `id: string`

  - `agent: BetaManagedAgentsSessionAgent`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `id: string`

    - `description: string | null`

    - `mcp_servers: Array<BetaManagedAgentsMCPServerURLDefinition>`

      - `name: string`

      - `type: "url"`

        - `"url"`

      - `url: string`

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

            - `"low"`

        - `BetaManagedAgentsEffortMedium`

          Medium effort. Balances latency and reasoning depth.

          - `type: "medium"`

            - `"medium"`

        - `BetaManagedAgentsEffortHigh`

          High effort. Favors reasoning depth.

          - `type: "high"`

            - `"high"`

        - `BetaManagedAgentsEffortXhigh`

          Extra-high effort. Not all models accept this level.

          - `type: "xhigh"`

            - `"xhigh"`

        - `BetaManagedAgentsEffortMax`

          Maximum effort. Favors reasoning depth over latency.

          - `type: "max"`

            - `"max"`

      - `inference_geo?: string`

        Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

      - `speed?: "standard" | "fast"`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `multiagent: BetaManagedAgentsSessionMultiagentCoordinator | null`

      Resolved coordinator topology with full agent definitions for each roster member.

      - `agents: Array<BetaManagedAgentsSessionThreadAgent | BetaManagedAgentsAdvisor>`

        Full `agent` definitions the coordinator may spawn as session threads.

        - `BetaManagedAgentsSessionThreadAgent`

          Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

          - `id: string`

          - `description: string | null`

          - `mcp_servers: Array<BetaManagedAgentsMCPServerURLDefinition>`

            - `name: string`

            - `type: "url"`

            - `url: string`

          - `model: BetaManagedAgentsModelConfig`

            Model identifier and configuration.

          - `name: string`

          - `skills: Array<BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill>`

            - `BetaManagedAgentsAnthropicSkill`

              A resolved Anthropic-managed skill.

              - `skill_id: string`

              - `type: "anthropic"`

                - `"anthropic"`

              - `version: string`

            - `BetaManagedAgentsCustomSkill`

              A resolved user-created custom skill.

              - `skill_id: string`

              - `type: "custom"`

                - `"custom"`

              - `version: string`

          - `system: string | null`

          - `tools: Array<BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool>`

            - `BetaManagedAgentsAgentToolset20260401`

              - `configs: Array<BetaManagedAgentsAgentToolConfig>`

                - `BetaManagedAgentsBashToolConfig`

                  Configuration for the bash tool.

                  - `enabled: boolean`

                  - `name: "bash"`

                    - `"bash"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                      - `type: "always_allow"`

                        - `"always_allow"`

                    - `BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                      - `type: "always_ask"`

                        - `"always_ask"`

                  - `type: "bash"`

                    - `"bash"`

                - `BetaManagedAgentsEditToolConfig`

                  Configuration for the edit tool.

                  - `enabled: boolean`

                  - `name: "edit"`

                    - `"edit"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                  - `type: "edit"`

                    - `"edit"`

                - `BetaManagedAgentsReadToolConfig`

                  Configuration for the read tool.

                  - `enabled: boolean`

                  - `name: "read"`

                    - `"read"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                  - `type: "read"`

                    - `"read"`

                - `BetaManagedAgentsWriteToolConfig`

                  Configuration for the write tool.

                  - `enabled: boolean`

                  - `name: "write"`

                    - `"write"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                  - `type: "write"`

                    - `"write"`

                - `BetaManagedAgentsGlobToolConfig`

                  Configuration for the glob tool.

                  - `enabled: boolean`

                  - `name: "glob"`

                    - `"glob"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                  - `type: "glob"`

                    - `"glob"`

                - `BetaManagedAgentsGrepToolConfig`

                  Configuration for the grep tool.

                  - `enabled: boolean`

                  - `name: "grep"`

                    - `"grep"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                  - `type: "grep"`

                    - `"grep"`

                - `BetaManagedAgentsWebFetchToolConfig`

                  Configuration for the web_fetch tool.

                  - `enabled: boolean`

                  - `name: "web_fetch"`

                    - `"web_fetch"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                  - `type: "web_fetch"`

                    - `"web_fetch"`

                  - `allowed_domains?: Array<string>`

                  - `blocked_domains?: Array<string>`

                  - `max_content_tokens?: number | null`

                - `BetaManagedAgentsWebSearchToolConfig`

                  Configuration for the web_search tool.

                  - `enabled: boolean`

                  - `name: "web_search"`

                    - `"web_search"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy | BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `BetaManagedAgentsAlwaysAllowPolicy`

                      Tool calls are automatically approved without user confirmation.

                    - `BetaManagedAgentsAlwaysAskPolicy`

                      Tool calls require user confirmation before execution.

                  - `type: "web_search"`

                    - `"web_search"`

                  - `allowed_domains?: Array<string>`

                  - `blocked_domains?: Array<string>`

                  - `user_location?: BetaManagedAgentsUserLocation | null`

                    Approximate user location for search result localization.

                    - `type: "approximate"`

                      Location precision. Only "approximate" is supported.

                      - `"approximate"`

                    - `city?: string | null`

                      City name.

                    - `country?: string | null`

                      Two-letter ISO 3166-1 country code, uppercase.

                    - `region?: string | null`

                      Region or state name.

                    - `timezone?: string | null`

                      IANA timezone identifier, e.g. "America/Los_Angeles".

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

                - `"agent_toolset_20260401"`

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

                - `"mcp_toolset"`

            - `BetaManagedAgentsCustomTool`

              A custom tool as returned in API responses.

              - `description: string`

              - `input_schema: BetaManagedAgentsCustomToolInputSchema`

                JSON Schema for custom tool input parameters.

                - `type: "object"`

                  - `"object"`

                - `properties?: Record<string, unknown> | null`

                - `required?: Array<string> | null`

              - `name: string`

              - `type: "custom"`

                - `"custom"`

          - `type: "agent"`

            - `"agent"`

          - `version: number`

        - `BetaManagedAgentsAdvisor`

          Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

          - `model: string`

            The advisor model id.

          - `type: "advisor"`

            - `"advisor"`

      - `type: "coordinator"`

        - `"coordinator"`

    - `name: string`

    - `skills: Array<BetaManagedAgentsAnthropicSkill | BetaManagedAgentsCustomSkill>`

      - `BetaManagedAgentsAnthropicSkill`

        A resolved Anthropic-managed skill.

      - `BetaManagedAgentsCustomSkill`

        A resolved user-created custom skill.

    - `system: string | null`

    - `tools: Array<BetaManagedAgentsAgentToolset20260401 | BetaManagedAgentsMCPToolset | BetaManagedAgentsCustomTool>`

      - `BetaManagedAgentsAgentToolset20260401`

      - `BetaManagedAgentsMCPToolset`

      - `BetaManagedAgentsCustomTool`

        A custom tool as returned in API responses.

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `archived_at: string | null`

    A timestamp in RFC 3339 format

  - `budget: BetaManagedAgentsBudgetLimit | null`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `max_list_cost: BetaMonetaryAmount`

      A monetary amount in a specific currency.

      - `amount: string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: BetaCurrency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

        - `"USD"`

    - `type: "limit"`

      - `"limit"`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `environment_id: string`

  - `metadata: Record<string, string>`

  - `outcome_evaluations: Array<BetaManagedAgentsOutcomeEvaluationResource>`

    Per-outcome evaluation state. One entry per define_outcome event sent to the session.

    - `completed_at: string | null`

      A timestamp in RFC 3339 format

    - `description: string`

      What the agent should produce.

    - `explanation: string | null`

      Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs_revision (intermediate), what's missing; for failed, why unrecoverable.

    - `iteration: number`

      0-indexed revision cycle the outcome is currently on.

    - `outcome_id: string`

      Server-generated outc_ ID for this outcome.

    - `result: string`

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

    - `type: "outcome_evaluation"`

      - `"outcome_evaluation"`

  - `resources: Array<BetaManagedAgentsSessionResource>`

    - `BetaManagedAgentsGitHubRepositoryResource`

      - `id: string`

      - `created_at: string`

        A timestamp in RFC 3339 format

      - `mount_path: string`

      - `type: "github_repository"`

        - `"github_repository"`

      - `updated_at: string`

        A timestamp in RFC 3339 format

      - `url: string`

      - `checkout?: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout | null`

        - `BetaManagedAgentsBranchCheckout`

          - `name: string`

            Branch name to check out.

          - `type: "branch"`

            - `"branch"`

        - `BetaManagedAgentsCommitCheckout`

          - `sha: string`

            Full commit SHA to check out.

          - `type: "commit"`

            - `"commit"`

    - `BetaManagedAgentsFileResource`

      - `id: string`

      - `created_at: string`

        A timestamp in RFC 3339 format

      - `file_id: string`

      - `mount_path: string`

      - `type: "file"`

        - `"file"`

      - `updated_at: string`

        A timestamp in RFC 3339 format

    - `BetaManagedAgentsMemoryStoreResource`

      A memory store attached to an agent session.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

        - `"memory_store"`

      - `access?: "read_write" | "read_only" | null`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `description?: string`

        Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

      - `instructions?: string | null`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      - `mount_path?: string | null`

        Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

      - `name?: string | null`

        Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

  - `stats: BetaManagedAgentsSessionStats`

    Timing statistics for a session.

    - `active_seconds?: number`

      Cumulative time in seconds the session spent in running status. Excludes idle time.

    - `duration_seconds?: number`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

  - `status: "rescheduling" | "running" | "idle" | "terminated"`

    SessionStatus enum

    - `"rescheduling"`

    - `"running"`

    - `"idle"`

    - `"terminated"`

  - `title: string | null`

  - `type: "session"`

    - `"session"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `usage: BetaManagedAgentsSessionUsage`

    Cumulative token usage for a session across all turns.

    - `active_seconds?: number`

      Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once, unlike `stats.active_seconds`, which sums each thread's own active time. This is the duration the session's runtime cost is priced on.

    - `cache_creation?: BetaManagedAgentsCacheCreationUsage`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens?: number`

        Tokens used to create 1-hour ephemeral cache entries.

      - `ephemeral_5m_input_tokens?: number`

        Tokens used to create 5-minute ephemeral cache entries.

    - `cache_read_input_tokens?: number`

      Total tokens read from prompt cache.

    - `input_tokens?: number`

      Total input tokens consumed across all turns.

    - `list_cost?: BetaMonetaryAmount | null`

      A monetary amount in a specific currency.

    - `output_tokens?: number`

      Total output tokens generated across all turns.

    - `server_tool_use?: BetaManagedAgentsServerToolUsage | null`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `web_fetch_requests?: number`

        Number of server-executed web fetch requests.

      - `web_search_requests?: number`

        Number of server-executed web search requests.

  - `vault_ids: Array<string>`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `deployment_id?: string | null`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaManagedAgentsSession of client.beta.sessions.list()) {
  console.log(betaManagedAgentsSession.id);
}
```

#### Response

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
