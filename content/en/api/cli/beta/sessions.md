# Sessions

## Create Session

`$ ant beta:sessions create`

**POST** `/v1/sessions`

Create Session

### Parameters

- `--agent: string or BetaManagedAgentsAgentParams or BetaManagedAgentsAgentWithOverridesParams`

  Body param: Agent identifier. Accepts the `agent` ID string, which pins the latest version for the session, or an `agent` object with both id and version specified.

- `--environment-id: string`

  Body param: ID of the `environment` defining the container configuration for this session.

  minLength: 1, maxLength: 128

- `--budget: optional object`

  Body param: A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

- `--initial-event: optional array of BetaManagedAgentsUserMessageEventParams or BetaManagedAgentsUserDefineOutcomeEventParams`

  Body param: Initial events to send to the `session` at creation, processed in order. Supports `user.message` and `user.define_outcome` events. Maximum 50 events.

- `--metadata: optional map[string]`

  Body param: Arbitrary key-value metadata attached to the session. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `--resource: optional array of BetaManagedAgentsGitHubRepositoryResourceParams or BetaManagedAgentsFileResourceParams or BetaManagedAgentsMemoryStoreResourceParam`

  Body param: Resources (e.g. repositories, files) to mount into the session's container.

- `--title: optional string`

  Body param: Human-readable session title.

  maxLength: 500

- `--vault-id: optional array of string`

  Body param: Vault IDs for stored credentials the agent can use during the session.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_session: object`

  A Managed Agents `session`.

  - `id: string`

  - `agent: object`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `id: string`

    - `description: string`

    - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

      - `name: string`

      - `type: "url"`

      - `url: string`

    - `model: object`

      Model identifier and configuration.

      - `id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

      - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

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

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `multiagent: object`

      Resolved coordinator topology with full agent definitions for each roster member.

      - `agents: array of BetaManagedAgentsSessionThreadAgent or BetaManagedAgentsAdvisor`

        Full `agent` definitions the coordinator may spawn as session threads.

        - `beta_managed_agents_session_thread_agent: object`

          Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

          - `id: string`

          - `description: string`

          - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

            - `name: string`

            - `type: "url"`

            - `url: string`

          - `model: object`

            Model identifier and configuration.

            - `id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string`

              The model that will power your agent.

              See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

              How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

            - `inference_geo: optional string`

              Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

            - `speed: optional "standard" or "fast"`

              Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `name: string`

          - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

            - `beta_managed_agents_anthropic_skill: object`

              A resolved Anthropic-managed skill.

              - `skill_id: string`

              - `type: "anthropic"`

              - `version: string`

            - `beta_managed_agents_custom_skill: object`

              A resolved user-created custom skill.

              - `skill_id: string`

              - `type: "custom"`

              - `version: string`

          - `system: string`

          - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

            - `beta_managed_agents_agent_toolset20260401: object`

              - `configs: array of BetaManagedAgentsAgentToolConfig`

                - `beta_managed_agents_bash_tool_config: object`

                  Configuration for the bash tool.

                  - `enabled: boolean`

                  - `name: "bash"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                      - `type: "always_allow"`

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                      - `type: "always_ask"`

                  - `type: "bash"`

                - `beta_managed_agents_edit_tool_config: object`

                  Configuration for the edit tool.

                  - `enabled: boolean`

                  - `name: "edit"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "edit"`

                - `beta_managed_agents_read_tool_config: object`

                  Configuration for the read tool.

                  - `enabled: boolean`

                  - `name: "read"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "read"`

                - `beta_managed_agents_write_tool_config: object`

                  Configuration for the write tool.

                  - `enabled: boolean`

                  - `name: "write"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "write"`

                - `beta_managed_agents_glob_tool_config: object`

                  Configuration for the glob tool.

                  - `enabled: boolean`

                  - `name: "glob"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "glob"`

                - `beta_managed_agents_grep_tool_config: object`

                  Configuration for the grep tool.

                  - `enabled: boolean`

                  - `name: "grep"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "grep"`

                - `beta_managed_agents_web_fetch_tool_config: object`

                  Configuration for the web_fetch tool.

                  - `enabled: boolean`

                  - `name: "web_fetch"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "web_fetch"`

                  - `allowed_domains: optional array of string`

                  - `blocked_domains: optional array of string`

                  - `max_content_tokens: optional number`

                    format: int32

                - `beta_managed_agents_web_search_tool_config: object`

                  Configuration for the web_search tool.

                  - `enabled: boolean`

                  - `name: "web_search"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "web_search"`

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

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

              - `type: "agent_toolset_20260401"`

            - `beta_managed_agents_mcp_toolset: object`

              - `configs: array of BetaManagedAgentsMCPToolConfig`

                - `enabled: boolean`

                - `name: string`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

              - `default_config: object`

                Resolved default configuration for all tools from an MCP server.

                - `enabled: boolean`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

              - `mcp_server_name: string`

              - `type: "mcp_toolset"`

            - `beta_managed_agents_custom_tool: object`

              A custom tool as returned in API responses.

              - `description: string`

              - `input_schema: object`

                JSON Schema for custom tool input parameters.

                - `type: "object"`

                - `properties: optional map[unknown]`

                - `required: optional array of string`

              - `name: string`

              - `type: "custom"`

          - `type: "agent"`

          - `version: number`

            format: int32

        - `beta_managed_agents_advisor: object`

          Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

          - `model: string`

            The advisor model id.

          - `type: "advisor"`

      - `type: "coordinator"`

    - `name: string`

    - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

      - `beta_managed_agents_anthropic_skill: object`

        A resolved Anthropic-managed skill.

      - `beta_managed_agents_custom_skill: object`

        A resolved user-created custom skill.

    - `system: string`

    - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

      - `beta_managed_agents_agent_toolset20260401: object`

      - `beta_managed_agents_mcp_toolset: object`

      - `beta_managed_agents_custom_tool: object`

        A custom tool as returned in API responses.

    - `type: "agent"`

    - `version: number`

      format: int32

  - `archived_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `budget: object`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `max_list_cost: object`

      A monetary amount in a specific currency.

      - `amount: string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: "USD"`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `type: "limit"`

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `environment_id: string`

  - `metadata: map[string]`

  - `outcome_evaluations: array of BetaManagedAgentsOutcomeEvaluationResource`

    Per-outcome evaluation state. One entry per define_outcome event sent to the session.

    - `completed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `description: string`

      What the agent should produce.

    - `explanation: string`

      Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs_revision (intermediate), what's missing; for failed, why unrecoverable.

    - `iteration: number`

      0-indexed revision cycle the outcome is currently on.

      format: int32

    - `outcome_id: string`

      Server-generated outc_ ID for this outcome.

    - `result: string`

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

    - `type: "outcome_evaluation"`

  - `resources: array of BetaManagedAgentsSessionResource`

    - `beta_managed_agents_github_repository_resource: object`

      - `id: string`

      - `created_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `mount_path: string`

      - `type: "github_repository"`

      - `updated_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `url: string`

      - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

        - `beta_managed_agents_branch_checkout: object`

          - `name: string`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `type: "branch"`

        - `beta_managed_agents_commit_checkout: object`

          - `sha: string`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `type: "commit"`

    - `beta_managed_agents_file_resource: object`

      - `id: string`

      - `created_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `file_id: string`

      - `mount_path: string`

      - `type: "file"`

      - `updated_at: string`

        A timestamp in RFC 3339 format

        format: date-time

    - `beta_managed_agents_memory_store_resource: object`

      A memory store attached to an agent session.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

      - `access: optional "read_write" or "read_only"`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `description: optional string`

        Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

      - `instructions: optional string`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

        maxLength: 4096

      - `mount_path: optional string`

        Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

      - `name: optional string`

        Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

  - `stats: object`

    Timing statistics for a session.

    - `active_seconds: optional number`

      Cumulative time in seconds the session spent in running status. Excludes idle time.

      format: double

    - `duration_seconds: optional number`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

      format: double

  - `status: "rescheduling" or "running" or "idle" or "terminated"`

    SessionStatus enum

    - `"rescheduling"`

    - `"running"`

    - `"idle"`

    - `"terminated"`

  - `title: string`

  - `type: "session"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `usage: object`

    Cumulative token usage for a session across all turns.

    - `active_seconds: optional number`

      Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once, unlike `stats.active_seconds`, which sums each thread's own active time. This is the duration the session's runtime cost is priced on.

      format: double

    - `cache_creation: optional object`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: optional number`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `ephemeral_5m_input_tokens: optional number`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `cache_read_input_tokens: optional number`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens: optional number`

      Total input tokens consumed across all turns.

      format: int32

    - `list_cost: optional object`

      A monetary amount in a specific currency.

      - `amount: string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: "USD"`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `output_tokens: optional number`

      Total output tokens generated across all turns.

      format: int32

    - `server_tool_use: optional object`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `web_fetch_requests: optional number`

        Number of server-executed web fetch requests.

        format: int32

      - `web_search_requests: optional number`

        Number of server-executed web search requests.

        format: int32

  - `vault_ids: array of string`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `deployment_id: optional string`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Example

```bash
ant beta:sessions create \
  --api-key my-anthropic-api-key \
  --agent agent_011CZkYpogX7uDKUyvBTophP \
  --environment-id env_011CZkZ9X2dpNyB7HsEFoRfW
```

#### Response (200)

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

## List Sessions

`$ ant beta:sessions list`

**GET** `/v1/sessions`

List Sessions

### Parameters

- `--agent-id: optional string`

  Query param: Filter sessions created with this agent ID.

- `--agent-version: optional number`

  Query param: Filter by agent version. Only applies when agent_id is also set.

  format: int32

- `--created-at-gt: optional string`

  Query param: Return sessions created after this time (exclusive).

  format: date-time

- `--created-at-gte: optional string`

  Query param: Return sessions created at or after this time (inclusive).

  format: date-time

- `--created-at-lt: optional string`

  Query param: Return sessions created before this time (exclusive).

  format: date-time

- `--created-at-lte: optional string`

  Query param: Return sessions created at or before this time (inclusive).

  format: date-time

- `--deployment-id: optional string`

  Query param: Filter sessions created by this deployment ID.

- `--include-archived: optional boolean`

  Query param: When true, includes archived sessions. Default: false (exclude archived).

- `--limit: optional number`

  Query param: Maximum number of results to return.

  format: int32

- `--memory-store-id: optional string`

  Query param: Filter sessions whose resources contain a memory_store with this memory store ID.

- `--order: optional "asc" or "desc"`

  Query param: Sort direction for results, ordered by created_at. Defaults to desc (newest first).

- `--page: optional string`

  Query param: Opaque pagination cursor from a previous response.

- `--status: optional array of "rescheduling" or "running" or "idle" or "terminated"`

  Query param: Filter by session status. Repeat the parameter to match any of multiple statuses.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsListSessions: object`

  Paginated list of sessions.

  - `data: optional array of BetaManagedAgentsSession`

    List of sessions.

    - `id: string`

    - `agent: object`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `id: string`

      - `description: string`

      - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

        - `name: string`

        - `type: "url"`

        - `url: string`

      - `model: object`

        Model identifier and configuration.

        - `id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

        - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

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

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

      - `multiagent: object`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `agents: array of BetaManagedAgentsSessionThreadAgent or BetaManagedAgentsAdvisor`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `beta_managed_agents_session_thread_agent: object`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `id: string`

            - `description: string`

            - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

              - `name: string`

              - `type: "url"`

              - `url: string`

            - `model: object`

              Model identifier and configuration.

              - `id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string`

                The model that will power your agent.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

              - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

                How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

              - `inference_geo: optional string`

                Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

              - `speed: optional "standard" or "fast"`

                Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

            - `name: string`

            - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

              - `beta_managed_agents_anthropic_skill: object`

                A resolved Anthropic-managed skill.

                - `skill_id: string`

                - `type: "anthropic"`

                - `version: string`

              - `beta_managed_agents_custom_skill: object`

                A resolved user-created custom skill.

                - `skill_id: string`

                - `type: "custom"`

                - `version: string`

            - `system: string`

            - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

              - `beta_managed_agents_agent_toolset20260401: object`

                - `configs: array of BetaManagedAgentsAgentToolConfig`

                  - `beta_managed_agents_bash_tool_config: object`

                    Configuration for the bash tool.

                    - `enabled: boolean`

                    - `name: "bash"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                        - `type: "always_allow"`

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                        - `type: "always_ask"`

                    - `type: "bash"`

                  - `beta_managed_agents_edit_tool_config: object`

                    Configuration for the edit tool.

                    - `enabled: boolean`

                    - `name: "edit"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                    - `type: "edit"`

                  - `beta_managed_agents_read_tool_config: object`

                    Configuration for the read tool.

                    - `enabled: boolean`

                    - `name: "read"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                    - `type: "read"`

                  - `beta_managed_agents_write_tool_config: object`

                    Configuration for the write tool.

                    - `enabled: boolean`

                    - `name: "write"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                    - `type: "write"`

                  - `beta_managed_agents_glob_tool_config: object`

                    Configuration for the glob tool.

                    - `enabled: boolean`

                    - `name: "glob"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                    - `type: "glob"`

                  - `beta_managed_agents_grep_tool_config: object`

                    Configuration for the grep tool.

                    - `enabled: boolean`

                    - `name: "grep"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                    - `type: "grep"`

                  - `beta_managed_agents_web_fetch_tool_config: object`

                    Configuration for the web_fetch tool.

                    - `enabled: boolean`

                    - `name: "web_fetch"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                    - `type: "web_fetch"`

                    - `allowed_domains: optional array of string`

                    - `blocked_domains: optional array of string`

                    - `max_content_tokens: optional number`

                      format: int32

                  - `beta_managed_agents_web_search_tool_config: object`

                    Configuration for the web_search tool.

                    - `enabled: boolean`

                    - `name: "web_search"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                    - `type: "web_search"`

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

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                - `type: "agent_toolset_20260401"`

              - `beta_managed_agents_mcp_toolset: object`

                - `configs: array of BetaManagedAgentsMCPToolConfig`

                  - `enabled: boolean`

                  - `name: string`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                - `default_config: object`

                  Resolved default configuration for all tools from an MCP server.

                  - `enabled: boolean`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                - `mcp_server_name: string`

                - `type: "mcp_toolset"`

              - `beta_managed_agents_custom_tool: object`

                A custom tool as returned in API responses.

                - `description: string`

                - `input_schema: object`

                  JSON Schema for custom tool input parameters.

                  - `type: "object"`

                  - `properties: optional map[unknown]`

                  - `required: optional array of string`

                - `name: string`

                - `type: "custom"`

            - `type: "agent"`

            - `version: number`

              format: int32

          - `beta_managed_agents_advisor: object`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `model: string`

              The advisor model id.

            - `type: "advisor"`

        - `type: "coordinator"`

      - `name: string`

      - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

        - `beta_managed_agents_anthropic_skill: object`

          A resolved Anthropic-managed skill.

        - `beta_managed_agents_custom_skill: object`

          A resolved user-created custom skill.

      - `system: string`

      - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

        - `beta_managed_agents_agent_toolset20260401: object`

        - `beta_managed_agents_mcp_toolset: object`

        - `beta_managed_agents_custom_tool: object`

          A custom tool as returned in API responses.

      - `type: "agent"`

      - `version: number`

        format: int32

    - `archived_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `budget: object`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `max_list_cost: object`

        A monetary amount in a specific currency.

        - `amount: string`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `currency: "USD"`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `type: "limit"`

    - `created_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `environment_id: string`

    - `metadata: map[string]`

    - `outcome_evaluations: array of BetaManagedAgentsOutcomeEvaluationResource`

      Per-outcome evaluation state. One entry per define_outcome event sent to the session.

      - `completed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `description: string`

        What the agent should produce.

      - `explanation: string`

        Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs_revision (intermediate), what's missing; for failed, why unrecoverable.

      - `iteration: number`

        0-indexed revision cycle the outcome is currently on.

        format: int32

      - `outcome_id: string`

        Server-generated outc_ ID for this outcome.

      - `result: string`

        Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

      - `type: "outcome_evaluation"`

    - `resources: array of BetaManagedAgentsSessionResource`

      - `beta_managed_agents_github_repository_resource: object`

        - `id: string`

        - `created_at: string`

          A timestamp in RFC 3339 format

          format: date-time

        - `mount_path: string`

        - `type: "github_repository"`

        - `updated_at: string`

          A timestamp in RFC 3339 format

          format: date-time

        - `url: string`

        - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

          - `beta_managed_agents_branch_checkout: object`

            - `name: string`

              Branch name to check out.

              minLength: 1, maxLength: 255

            - `type: "branch"`

          - `beta_managed_agents_commit_checkout: object`

            - `sha: string`

              Full commit SHA to check out.

              minLength: 7, maxLength: 64

            - `type: "commit"`

      - `beta_managed_agents_file_resource: object`

        - `id: string`

        - `created_at: string`

          A timestamp in RFC 3339 format

          format: date-time

        - `file_id: string`

        - `mount_path: string`

        - `type: "file"`

        - `updated_at: string`

          A timestamp in RFC 3339 format

          format: date-time

      - `beta_managed_agents_memory_store_resource: object`

        A memory store attached to an agent session.

        - `memory_store_id: string`

          The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

        - `type: "memory_store"`

        - `access: optional "read_write" or "read_only"`

          Access mode for an attached memory store.

          - `"read_write"`

          - `"read_only"`

        - `description: optional string`

          Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

        - `instructions: optional string`

          Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

          maxLength: 4096

        - `mount_path: optional string`

          Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

        - `name: optional string`

          Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

    - `stats: object`

      Timing statistics for a session.

      - `active_seconds: optional number`

        Cumulative time in seconds the session spent in running status. Excludes idle time.

        format: double

      - `duration_seconds: optional number`

        Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

        format: double

    - `status: "rescheduling" or "running" or "idle" or "terminated"`

      SessionStatus enum

      - `"rescheduling"`

      - `"running"`

      - `"idle"`

      - `"terminated"`

    - `title: string`

    - `type: "session"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `usage: object`

      Cumulative token usage for a session across all turns.

      - `active_seconds: optional number`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once, unlike `stats.active_seconds`, which sums each thread's own active time. This is the duration the session's runtime cost is priced on.

        format: double

      - `cache_creation: optional object`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `ephemeral_1h_input_tokens: optional number`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `ephemeral_5m_input_tokens: optional number`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `cache_read_input_tokens: optional number`

        Total tokens read from prompt cache.

        format: int32

      - `input_tokens: optional number`

        Total input tokens consumed across all turns.

        format: int32

      - `list_cost: optional object`

        A monetary amount in a specific currency.

        - `amount: string`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `currency: "USD"`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `output_tokens: optional number`

        Total output tokens generated across all turns.

        format: int32

      - `server_tool_use: optional object`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `web_fetch_requests: optional number`

          Number of server-executed web fetch requests.

          format: int32

        - `web_search_requests: optional number`

          Number of server-executed web search requests.

          format: int32

    - `vault_ids: array of string`

      Vault IDs attached to the session at creation. Empty when no vaults were supplied.

    - `deployment_id: optional string`

      Deployment ID when the session was created from a deployment reference. Null otherwise.

  - `next_page: optional string`

    Opaque cursor for the next page. Null when no more results.

  - `prev_page: optional string`

    Opaque cursor for the previous page. Null when on the first page. Pass as the `page` parameter to navigate backward.

### Example

```bash
ant beta:sessions list \
  --api-key my-anthropic-api-key
```

#### Response (200)

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

## Get Session

`$ ant beta:sessions retrieve`

**GET** `/v1/sessions/{session_id}`

Get Session

### Parameters

- `--session-id: string`

  Path parameter session_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_session: object`

  A Managed Agents `session`.

  - `id: string`

  - `agent: object`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `id: string`

    - `description: string`

    - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

      - `name: string`

      - `type: "url"`

      - `url: string`

    - `model: object`

      Model identifier and configuration.

      - `id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

      - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

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

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `multiagent: object`

      Resolved coordinator topology with full agent definitions for each roster member.

      - `agents: array of BetaManagedAgentsSessionThreadAgent or BetaManagedAgentsAdvisor`

        Full `agent` definitions the coordinator may spawn as session threads.

        - `beta_managed_agents_session_thread_agent: object`

          Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

          - `id: string`

          - `description: string`

          - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

            - `name: string`

            - `type: "url"`

            - `url: string`

          - `model: object`

            Model identifier and configuration.

            - `id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string`

              The model that will power your agent.

              See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

              How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

            - `inference_geo: optional string`

              Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

            - `speed: optional "standard" or "fast"`

              Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `name: string`

          - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

            - `beta_managed_agents_anthropic_skill: object`

              A resolved Anthropic-managed skill.

              - `skill_id: string`

              - `type: "anthropic"`

              - `version: string`

            - `beta_managed_agents_custom_skill: object`

              A resolved user-created custom skill.

              - `skill_id: string`

              - `type: "custom"`

              - `version: string`

          - `system: string`

          - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

            - `beta_managed_agents_agent_toolset20260401: object`

              - `configs: array of BetaManagedAgentsAgentToolConfig`

                - `beta_managed_agents_bash_tool_config: object`

                  Configuration for the bash tool.

                  - `enabled: boolean`

                  - `name: "bash"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                      - `type: "always_allow"`

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                      - `type: "always_ask"`

                  - `type: "bash"`

                - `beta_managed_agents_edit_tool_config: object`

                  Configuration for the edit tool.

                  - `enabled: boolean`

                  - `name: "edit"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "edit"`

                - `beta_managed_agents_read_tool_config: object`

                  Configuration for the read tool.

                  - `enabled: boolean`

                  - `name: "read"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "read"`

                - `beta_managed_agents_write_tool_config: object`

                  Configuration for the write tool.

                  - `enabled: boolean`

                  - `name: "write"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "write"`

                - `beta_managed_agents_glob_tool_config: object`

                  Configuration for the glob tool.

                  - `enabled: boolean`

                  - `name: "glob"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "glob"`

                - `beta_managed_agents_grep_tool_config: object`

                  Configuration for the grep tool.

                  - `enabled: boolean`

                  - `name: "grep"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "grep"`

                - `beta_managed_agents_web_fetch_tool_config: object`

                  Configuration for the web_fetch tool.

                  - `enabled: boolean`

                  - `name: "web_fetch"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "web_fetch"`

                  - `allowed_domains: optional array of string`

                  - `blocked_domains: optional array of string`

                  - `max_content_tokens: optional number`

                    format: int32

                - `beta_managed_agents_web_search_tool_config: object`

                  Configuration for the web_search tool.

                  - `enabled: boolean`

                  - `name: "web_search"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "web_search"`

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

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

              - `type: "agent_toolset_20260401"`

            - `beta_managed_agents_mcp_toolset: object`

              - `configs: array of BetaManagedAgentsMCPToolConfig`

                - `enabled: boolean`

                - `name: string`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

              - `default_config: object`

                Resolved default configuration for all tools from an MCP server.

                - `enabled: boolean`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

              - `mcp_server_name: string`

              - `type: "mcp_toolset"`

            - `beta_managed_agents_custom_tool: object`

              A custom tool as returned in API responses.

              - `description: string`

              - `input_schema: object`

                JSON Schema for custom tool input parameters.

                - `type: "object"`

                - `properties: optional map[unknown]`

                - `required: optional array of string`

              - `name: string`

              - `type: "custom"`

          - `type: "agent"`

          - `version: number`

            format: int32

        - `beta_managed_agents_advisor: object`

          Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

          - `model: string`

            The advisor model id.

          - `type: "advisor"`

      - `type: "coordinator"`

    - `name: string`

    - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

      - `beta_managed_agents_anthropic_skill: object`

        A resolved Anthropic-managed skill.

      - `beta_managed_agents_custom_skill: object`

        A resolved user-created custom skill.

    - `system: string`

    - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

      - `beta_managed_agents_agent_toolset20260401: object`

      - `beta_managed_agents_mcp_toolset: object`

      - `beta_managed_agents_custom_tool: object`

        A custom tool as returned in API responses.

    - `type: "agent"`

    - `version: number`

      format: int32

  - `archived_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `budget: object`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `max_list_cost: object`

      A monetary amount in a specific currency.

      - `amount: string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: "USD"`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `type: "limit"`

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `environment_id: string`

  - `metadata: map[string]`

  - `outcome_evaluations: array of BetaManagedAgentsOutcomeEvaluationResource`

    Per-outcome evaluation state. One entry per define_outcome event sent to the session.

    - `completed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `description: string`

      What the agent should produce.

    - `explanation: string`

      Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs_revision (intermediate), what's missing; for failed, why unrecoverable.

    - `iteration: number`

      0-indexed revision cycle the outcome is currently on.

      format: int32

    - `outcome_id: string`

      Server-generated outc_ ID for this outcome.

    - `result: string`

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

    - `type: "outcome_evaluation"`

  - `resources: array of BetaManagedAgentsSessionResource`

    - `beta_managed_agents_github_repository_resource: object`

      - `id: string`

      - `created_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `mount_path: string`

      - `type: "github_repository"`

      - `updated_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `url: string`

      - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

        - `beta_managed_agents_branch_checkout: object`

          - `name: string`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `type: "branch"`

        - `beta_managed_agents_commit_checkout: object`

          - `sha: string`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `type: "commit"`

    - `beta_managed_agents_file_resource: object`

      - `id: string`

      - `created_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `file_id: string`

      - `mount_path: string`

      - `type: "file"`

      - `updated_at: string`

        A timestamp in RFC 3339 format

        format: date-time

    - `beta_managed_agents_memory_store_resource: object`

      A memory store attached to an agent session.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

      - `access: optional "read_write" or "read_only"`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `description: optional string`

        Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

      - `instructions: optional string`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

        maxLength: 4096

      - `mount_path: optional string`

        Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

      - `name: optional string`

        Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

  - `stats: object`

    Timing statistics for a session.

    - `active_seconds: optional number`

      Cumulative time in seconds the session spent in running status. Excludes idle time.

      format: double

    - `duration_seconds: optional number`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

      format: double

  - `status: "rescheduling" or "running" or "idle" or "terminated"`

    SessionStatus enum

    - `"rescheduling"`

    - `"running"`

    - `"idle"`

    - `"terminated"`

  - `title: string`

  - `type: "session"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `usage: object`

    Cumulative token usage for a session across all turns.

    - `active_seconds: optional number`

      Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once, unlike `stats.active_seconds`, which sums each thread's own active time. This is the duration the session's runtime cost is priced on.

      format: double

    - `cache_creation: optional object`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: optional number`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `ephemeral_5m_input_tokens: optional number`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `cache_read_input_tokens: optional number`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens: optional number`

      Total input tokens consumed across all turns.

      format: int32

    - `list_cost: optional object`

      A monetary amount in a specific currency.

      - `amount: string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: "USD"`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `output_tokens: optional number`

      Total output tokens generated across all turns.

      format: int32

    - `server_tool_use: optional object`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `web_fetch_requests: optional number`

        Number of server-executed web fetch requests.

        format: int32

      - `web_search_requests: optional number`

        Number of server-executed web search requests.

        format: int32

  - `vault_ids: array of string`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `deployment_id: optional string`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Example

```bash
ant beta:sessions retrieve \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7
```

#### Response (200)

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

## Update Session

`$ ant beta:sessions update`

**POST** `/v1/sessions/{session_id}`

Update Session

### Parameters

- `--session-id: string`

  Path param: Path parameter session_id

- `--agent: optional object`

  Body param: Mid-session agent configuration update. Only `tools` and `mcp_servers` are updatable. Full replacement: the provided array becomes the new value. To preserve existing entries, GET the session, modify the array, and POST it back.

- `--budget: optional object`

  Body param: A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

- `--metadata: optional map[string]`

  Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve.

- `--title: optional string`

  Body param: Human-readable session title.

  minLength: 1, maxLength: 500

- `--vault-id: optional array of string`

  Body param: Vault IDs (`vlt_*`) to attach to the session. Not yet supported; requests setting this field are rejected. Reserved for future use.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_session: object`

  A Managed Agents `session`.

  - `id: string`

  - `agent: object`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `id: string`

    - `description: string`

    - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

      - `name: string`

      - `type: "url"`

      - `url: string`

    - `model: object`

      Model identifier and configuration.

      - `id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

      - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

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

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `multiagent: object`

      Resolved coordinator topology with full agent definitions for each roster member.

      - `agents: array of BetaManagedAgentsSessionThreadAgent or BetaManagedAgentsAdvisor`

        Full `agent` definitions the coordinator may spawn as session threads.

        - `beta_managed_agents_session_thread_agent: object`

          Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

          - `id: string`

          - `description: string`

          - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

            - `name: string`

            - `type: "url"`

            - `url: string`

          - `model: object`

            Model identifier and configuration.

            - `id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string`

              The model that will power your agent.

              See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

              How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

            - `inference_geo: optional string`

              Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

            - `speed: optional "standard" or "fast"`

              Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `name: string`

          - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

            - `beta_managed_agents_anthropic_skill: object`

              A resolved Anthropic-managed skill.

              - `skill_id: string`

              - `type: "anthropic"`

              - `version: string`

            - `beta_managed_agents_custom_skill: object`

              A resolved user-created custom skill.

              - `skill_id: string`

              - `type: "custom"`

              - `version: string`

          - `system: string`

          - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

            - `beta_managed_agents_agent_toolset20260401: object`

              - `configs: array of BetaManagedAgentsAgentToolConfig`

                - `beta_managed_agents_bash_tool_config: object`

                  Configuration for the bash tool.

                  - `enabled: boolean`

                  - `name: "bash"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                      - `type: "always_allow"`

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                      - `type: "always_ask"`

                  - `type: "bash"`

                - `beta_managed_agents_edit_tool_config: object`

                  Configuration for the edit tool.

                  - `enabled: boolean`

                  - `name: "edit"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "edit"`

                - `beta_managed_agents_read_tool_config: object`

                  Configuration for the read tool.

                  - `enabled: boolean`

                  - `name: "read"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "read"`

                - `beta_managed_agents_write_tool_config: object`

                  Configuration for the write tool.

                  - `enabled: boolean`

                  - `name: "write"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "write"`

                - `beta_managed_agents_glob_tool_config: object`

                  Configuration for the glob tool.

                  - `enabled: boolean`

                  - `name: "glob"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "glob"`

                - `beta_managed_agents_grep_tool_config: object`

                  Configuration for the grep tool.

                  - `enabled: boolean`

                  - `name: "grep"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "grep"`

                - `beta_managed_agents_web_fetch_tool_config: object`

                  Configuration for the web_fetch tool.

                  - `enabled: boolean`

                  - `name: "web_fetch"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "web_fetch"`

                  - `allowed_domains: optional array of string`

                  - `blocked_domains: optional array of string`

                  - `max_content_tokens: optional number`

                    format: int32

                - `beta_managed_agents_web_search_tool_config: object`

                  Configuration for the web_search tool.

                  - `enabled: boolean`

                  - `name: "web_search"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "web_search"`

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

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

              - `type: "agent_toolset_20260401"`

            - `beta_managed_agents_mcp_toolset: object`

              - `configs: array of BetaManagedAgentsMCPToolConfig`

                - `enabled: boolean`

                - `name: string`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

              - `default_config: object`

                Resolved default configuration for all tools from an MCP server.

                - `enabled: boolean`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

              - `mcp_server_name: string`

              - `type: "mcp_toolset"`

            - `beta_managed_agents_custom_tool: object`

              A custom tool as returned in API responses.

              - `description: string`

              - `input_schema: object`

                JSON Schema for custom tool input parameters.

                - `type: "object"`

                - `properties: optional map[unknown]`

                - `required: optional array of string`

              - `name: string`

              - `type: "custom"`

          - `type: "agent"`

          - `version: number`

            format: int32

        - `beta_managed_agents_advisor: object`

          Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

          - `model: string`

            The advisor model id.

          - `type: "advisor"`

      - `type: "coordinator"`

    - `name: string`

    - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

      - `beta_managed_agents_anthropic_skill: object`

        A resolved Anthropic-managed skill.

      - `beta_managed_agents_custom_skill: object`

        A resolved user-created custom skill.

    - `system: string`

    - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

      - `beta_managed_agents_agent_toolset20260401: object`

      - `beta_managed_agents_mcp_toolset: object`

      - `beta_managed_agents_custom_tool: object`

        A custom tool as returned in API responses.

    - `type: "agent"`

    - `version: number`

      format: int32

  - `archived_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `budget: object`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `max_list_cost: object`

      A monetary amount in a specific currency.

      - `amount: string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: "USD"`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `type: "limit"`

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `environment_id: string`

  - `metadata: map[string]`

  - `outcome_evaluations: array of BetaManagedAgentsOutcomeEvaluationResource`

    Per-outcome evaluation state. One entry per define_outcome event sent to the session.

    - `completed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `description: string`

      What the agent should produce.

    - `explanation: string`

      Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs_revision (intermediate), what's missing; for failed, why unrecoverable.

    - `iteration: number`

      0-indexed revision cycle the outcome is currently on.

      format: int32

    - `outcome_id: string`

      Server-generated outc_ ID for this outcome.

    - `result: string`

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

    - `type: "outcome_evaluation"`

  - `resources: array of BetaManagedAgentsSessionResource`

    - `beta_managed_agents_github_repository_resource: object`

      - `id: string`

      - `created_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `mount_path: string`

      - `type: "github_repository"`

      - `updated_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `url: string`

      - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

        - `beta_managed_agents_branch_checkout: object`

          - `name: string`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `type: "branch"`

        - `beta_managed_agents_commit_checkout: object`

          - `sha: string`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `type: "commit"`

    - `beta_managed_agents_file_resource: object`

      - `id: string`

      - `created_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `file_id: string`

      - `mount_path: string`

      - `type: "file"`

      - `updated_at: string`

        A timestamp in RFC 3339 format

        format: date-time

    - `beta_managed_agents_memory_store_resource: object`

      A memory store attached to an agent session.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

      - `access: optional "read_write" or "read_only"`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `description: optional string`

        Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

      - `instructions: optional string`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

        maxLength: 4096

      - `mount_path: optional string`

        Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

      - `name: optional string`

        Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

  - `stats: object`

    Timing statistics for a session.

    - `active_seconds: optional number`

      Cumulative time in seconds the session spent in running status. Excludes idle time.

      format: double

    - `duration_seconds: optional number`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

      format: double

  - `status: "rescheduling" or "running" or "idle" or "terminated"`

    SessionStatus enum

    - `"rescheduling"`

    - `"running"`

    - `"idle"`

    - `"terminated"`

  - `title: string`

  - `type: "session"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `usage: object`

    Cumulative token usage for a session across all turns.

    - `active_seconds: optional number`

      Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once, unlike `stats.active_seconds`, which sums each thread's own active time. This is the duration the session's runtime cost is priced on.

      format: double

    - `cache_creation: optional object`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: optional number`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `ephemeral_5m_input_tokens: optional number`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `cache_read_input_tokens: optional number`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens: optional number`

      Total input tokens consumed across all turns.

      format: int32

    - `list_cost: optional object`

      A monetary amount in a specific currency.

      - `amount: string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: "USD"`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `output_tokens: optional number`

      Total output tokens generated across all turns.

      format: int32

    - `server_tool_use: optional object`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `web_fetch_requests: optional number`

        Number of server-executed web fetch requests.

        format: int32

      - `web_search_requests: optional number`

        Number of server-executed web search requests.

        format: int32

  - `vault_ids: array of string`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `deployment_id: optional string`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Example

```bash
ant beta:sessions update \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7
```

#### Response (200)

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

## Delete Session

`$ ant beta:sessions delete`

**DELETE** `/v1/sessions/{session_id}`

Delete Session

### Parameters

- `--session-id: string`

  Path parameter session_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_deleted_session: object`

  Confirmation that a `session` has been permanently deleted.

  - `id: string`

  - `type: "session_deleted"`

### Example

```bash
ant beta:sessions delete \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7
```

#### Response (200)

```json
{
  "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "type": "session_deleted"
}
```

## Archive Session

`$ ant beta:sessions archive`

**POST** `/v1/sessions/{session_id}/archive`

Archive Session

### Parameters

- `--session-id: string`

  Path parameter session_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_session: object`

  A Managed Agents `session`.

  - `id: string`

  - `agent: object`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `id: string`

    - `description: string`

    - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

      - `name: string`

      - `type: "url"`

      - `url: string`

    - `model: object`

      Model identifier and configuration.

      - `id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

      - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

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

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `multiagent: object`

      Resolved coordinator topology with full agent definitions for each roster member.

      - `agents: array of BetaManagedAgentsSessionThreadAgent or BetaManagedAgentsAdvisor`

        Full `agent` definitions the coordinator may spawn as session threads.

        - `beta_managed_agents_session_thread_agent: object`

          Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

          - `id: string`

          - `description: string`

          - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

            - `name: string`

            - `type: "url"`

            - `url: string`

          - `model: object`

            Model identifier and configuration.

            - `id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string`

              The model that will power your agent.

              See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

              How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

            - `inference_geo: optional string`

              Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

            - `speed: optional "standard" or "fast"`

              Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `name: string`

          - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

            - `beta_managed_agents_anthropic_skill: object`

              A resolved Anthropic-managed skill.

              - `skill_id: string`

              - `type: "anthropic"`

              - `version: string`

            - `beta_managed_agents_custom_skill: object`

              A resolved user-created custom skill.

              - `skill_id: string`

              - `type: "custom"`

              - `version: string`

          - `system: string`

          - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

            - `beta_managed_agents_agent_toolset20260401: object`

              - `configs: array of BetaManagedAgentsAgentToolConfig`

                - `beta_managed_agents_bash_tool_config: object`

                  Configuration for the bash tool.

                  - `enabled: boolean`

                  - `name: "bash"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                      - `type: "always_allow"`

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                      - `type: "always_ask"`

                  - `type: "bash"`

                - `beta_managed_agents_edit_tool_config: object`

                  Configuration for the edit tool.

                  - `enabled: boolean`

                  - `name: "edit"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "edit"`

                - `beta_managed_agents_read_tool_config: object`

                  Configuration for the read tool.

                  - `enabled: boolean`

                  - `name: "read"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "read"`

                - `beta_managed_agents_write_tool_config: object`

                  Configuration for the write tool.

                  - `enabled: boolean`

                  - `name: "write"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "write"`

                - `beta_managed_agents_glob_tool_config: object`

                  Configuration for the glob tool.

                  - `enabled: boolean`

                  - `name: "glob"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "glob"`

                - `beta_managed_agents_grep_tool_config: object`

                  Configuration for the grep tool.

                  - `enabled: boolean`

                  - `name: "grep"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "grep"`

                - `beta_managed_agents_web_fetch_tool_config: object`

                  Configuration for the web_fetch tool.

                  - `enabled: boolean`

                  - `name: "web_fetch"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "web_fetch"`

                  - `allowed_domains: optional array of string`

                  - `blocked_domains: optional array of string`

                  - `max_content_tokens: optional number`

                    format: int32

                - `beta_managed_agents_web_search_tool_config: object`

                  Configuration for the web_search tool.

                  - `enabled: boolean`

                  - `name: "web_search"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "web_search"`

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

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

              - `type: "agent_toolset_20260401"`

            - `beta_managed_agents_mcp_toolset: object`

              - `configs: array of BetaManagedAgentsMCPToolConfig`

                - `enabled: boolean`

                - `name: string`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

              - `default_config: object`

                Resolved default configuration for all tools from an MCP server.

                - `enabled: boolean`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

              - `mcp_server_name: string`

              - `type: "mcp_toolset"`

            - `beta_managed_agents_custom_tool: object`

              A custom tool as returned in API responses.

              - `description: string`

              - `input_schema: object`

                JSON Schema for custom tool input parameters.

                - `type: "object"`

                - `properties: optional map[unknown]`

                - `required: optional array of string`

              - `name: string`

              - `type: "custom"`

          - `type: "agent"`

          - `version: number`

            format: int32

        - `beta_managed_agents_advisor: object`

          Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

          - `model: string`

            The advisor model id.

          - `type: "advisor"`

      - `type: "coordinator"`

    - `name: string`

    - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

      - `beta_managed_agents_anthropic_skill: object`

        A resolved Anthropic-managed skill.

      - `beta_managed_agents_custom_skill: object`

        A resolved user-created custom skill.

    - `system: string`

    - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

      - `beta_managed_agents_agent_toolset20260401: object`

      - `beta_managed_agents_mcp_toolset: object`

      - `beta_managed_agents_custom_tool: object`

        A custom tool as returned in API responses.

    - `type: "agent"`

    - `version: number`

      format: int32

  - `archived_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `budget: object`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `max_list_cost: object`

      A monetary amount in a specific currency.

      - `amount: string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: "USD"`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `type: "limit"`

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `environment_id: string`

  - `metadata: map[string]`

  - `outcome_evaluations: array of BetaManagedAgentsOutcomeEvaluationResource`

    Per-outcome evaluation state. One entry per define_outcome event sent to the session.

    - `completed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `description: string`

      What the agent should produce.

    - `explanation: string`

      Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs_revision (intermediate), what's missing; for failed, why unrecoverable.

    - `iteration: number`

      0-indexed revision cycle the outcome is currently on.

      format: int32

    - `outcome_id: string`

      Server-generated outc_ ID for this outcome.

    - `result: string`

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

    - `type: "outcome_evaluation"`

  - `resources: array of BetaManagedAgentsSessionResource`

    - `beta_managed_agents_github_repository_resource: object`

      - `id: string`

      - `created_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `mount_path: string`

      - `type: "github_repository"`

      - `updated_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `url: string`

      - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

        - `beta_managed_agents_branch_checkout: object`

          - `name: string`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `type: "branch"`

        - `beta_managed_agents_commit_checkout: object`

          - `sha: string`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `type: "commit"`

    - `beta_managed_agents_file_resource: object`

      - `id: string`

      - `created_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `file_id: string`

      - `mount_path: string`

      - `type: "file"`

      - `updated_at: string`

        A timestamp in RFC 3339 format

        format: date-time

    - `beta_managed_agents_memory_store_resource: object`

      A memory store attached to an agent session.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

      - `access: optional "read_write" or "read_only"`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `description: optional string`

        Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

      - `instructions: optional string`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

        maxLength: 4096

      - `mount_path: optional string`

        Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

      - `name: optional string`

        Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

  - `stats: object`

    Timing statistics for a session.

    - `active_seconds: optional number`

      Cumulative time in seconds the session spent in running status. Excludes idle time.

      format: double

    - `duration_seconds: optional number`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

      format: double

  - `status: "rescheduling" or "running" or "idle" or "terminated"`

    SessionStatus enum

    - `"rescheduling"`

    - `"running"`

    - `"idle"`

    - `"terminated"`

  - `title: string`

  - `type: "session"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `usage: object`

    Cumulative token usage for a session across all turns.

    - `active_seconds: optional number`

      Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once, unlike `stats.active_seconds`, which sums each thread's own active time. This is the duration the session's runtime cost is priced on.

      format: double

    - `cache_creation: optional object`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: optional number`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `ephemeral_5m_input_tokens: optional number`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `cache_read_input_tokens: optional number`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens: optional number`

      Total input tokens consumed across all turns.

      format: int32

    - `list_cost: optional object`

      A monetary amount in a specific currency.

      - `amount: string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: "USD"`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `output_tokens: optional number`

      Total output tokens generated across all turns.

      format: int32

    - `server_tool_use: optional object`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `web_fetch_requests: optional number`

        Number of server-executed web fetch requests.

        format: int32

      - `web_search_requests: optional number`

        Number of server-executed web search requests.

        format: int32

  - `vault_ids: array of string`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `deployment_id: optional string`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Example

```bash
ant beta:sessions archive \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7
```

#### Response (200)

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

## Domain types

### Beta Managed Agents Advisor Params

- `beta_managed_agents_advisor_params: object`

  Platform advisor roster entry: a model the session's primary thread may consult mid-turn. At most one per roster; the entry occupies the roster name `anthropic.advisor`.

  - `model: string`

    A Claude model id. The model must be permitted as an advisor for this agent's model — see the sessions/threads/advisor spec.

    minLength: 1, maxLength: 256

  - `type: "advisor"`

### Beta Managed Agents Agent Message Preview

- `beta_managed_agents_agent_message_preview: object`

  - `id: string`

    The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

  - `type: "agent.message"`

### Beta Managed Agents Agent Params

- `beta_managed_agents_agent_params: object`

  Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

  - `id: string`

    The `agent` ID.

    minLength: 1, maxLength: 128

  - `type: "agent"`

  - `version: optional number`

    The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

    format: int32

### Beta Managed Agents Agent Thinking Preview

- `beta_managed_agents_agent_thinking_preview: object`

  - `id: string`

    The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

  - `type: "agent.thinking"`

### Beta Managed Agents Agent With Overrides Params

- `beta_managed_agents_agent_with_overrides_params: object`

  Reference to an `agent` plus optional configuration overrides. Each provided field replaces the agent's value for the caller's use; the agent resource is unchanged.

  - `id: string`

    The `agent` ID.

    minLength: 1, maxLength: 128

  - `type: "agent_with_overrides"`

  - `mcp_servers: optional array of BetaManagedAgentsURLMCPServerParams`

    Replacement MCP server list. Full replacement: the provided array becomes the MCP servers. Send an empty array to clear; omit to preserve the agent's servers.

    - `name: string`

      Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

      minLength: 1, maxLength: 255

    - `type: "url"`

    - `url: string`

      Endpoint URL for the MCP server.

      maxLength: 2048

  - `model: optional BetaManagedAgentsModelConfigParams`

    Replacement model. Accepts the model string, e.g. `claude-opus-5`, or a `model_config` object. Omit to use the agent's model.

    - `id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

    - `effort: optional "low" or "medium" or "high" or 2 more or BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or 3 more`

      How hard Claude works on each inference call. Accepts a bare level string (`"high"`) or `{"type": "high"}`. On create, omitting it resolves the per-model default; on update, omitting it leaves the stored value unchanged.

      - `BetaManagedAgentsEffortLevel: "low" or "medium" or "high" or 2 more`

        How hard Claude works on each turn. Higher levels favor reasoning depth over latency. Not all models accept every level; invalid combinations are rejected at create time.

        - `"low"`

        - `"medium"`

        - `"high"`

        - `"xhigh"`

        - `"max"`

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

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `skills: optional array of BetaManagedAgentsSkillParams`

    Replacement skill list. Full replacement: the provided array becomes the skills. Send an empty array to clear; omit to preserve the agent's skills.

    - `beta_managed_agents_anthropic_skill_params: object`

      An Anthropic-managed skill.

      - `skill_id: string`

        Identifier of the Anthropic skill (e.g., "xlsx").

        minLength: 1, maxLength: 64

      - `type: "anthropic"`

      - `version: optional string`

        Version to pin. Defaults to latest if omitted.

        minLength: 1, maxLength: 64

    - `beta_managed_agents_custom_skill_params: object`

      A user-created custom skill.

      - `skill_id: string`

        Tagged ID of the custom skill (e.g., "skill_01XJ5...").

        minLength: 1, maxLength: 64

      - `type: "custom"`

      - `version: optional string`

        Version to pin. Defaults to latest if omitted.

        minLength: 1, maxLength: 64

  - `system: optional string`

    Replacement system prompt. Up to 100,000 characters. Set to null to clear the agent's system prompt; omit to preserve it.

    maxLength: 100000

  - `tools: optional array of BetaManagedAgentsAgentToolset20260401Params or BetaManagedAgentsMCPToolsetParams or BetaManagedAgentsCustomToolParams`

    Replacement tool list. Full replacement: the provided array becomes the tool configuration. Send an empty array to clear; omit to preserve the agent's tools.

    - `beta_managed_agents_agent_toolset20260401_params: object`

      Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

      - `type: "agent_toolset_20260401"`

      - `configs: optional array of BetaManagedAgentsAgentToolConfigParams`

        Per-tool configuration overrides.

        - `beta_managed_agents_bash_tool_config_params: object`

          Configuration override for the bash tool.

          - `name: "bash"`

            Must be "bash".

          - `enabled: optional boolean`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

            - `beta_managed_agents_always_ask_policy: object`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

          - `type: optional "bash"`

        - `beta_managed_agents_edit_tool_config_params: object`

          Configuration override for the edit tool.

          - `name: "edit"`

            Must be "edit".

          - `enabled: optional boolean`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object`

              Tool calls require user confirmation before execution.

          - `type: optional "edit"`

        - `beta_managed_agents_read_tool_config_params: object`

          Configuration override for the read tool.

          - `name: "read"`

            Must be "read".

          - `enabled: optional boolean`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object`

              Tool calls require user confirmation before execution.

          - `type: optional "read"`

        - `beta_managed_agents_write_tool_config_params: object`

          Configuration override for the write tool.

          - `name: "write"`

            Must be "write".

          - `enabled: optional boolean`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object`

              Tool calls require user confirmation before execution.

          - `type: optional "write"`

        - `beta_managed_agents_glob_tool_config_params: object`

          Configuration override for the glob tool.

          - `name: "glob"`

            Must be "glob".

          - `enabled: optional boolean`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object`

              Tool calls require user confirmation before execution.

          - `type: optional "glob"`

        - `beta_managed_agents_grep_tool_config_params: object`

          Configuration override for the grep tool.

          - `name: "grep"`

            Must be "grep".

          - `enabled: optional boolean`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object`

              Tool calls require user confirmation before execution.

          - `type: optional "grep"`

        - `beta_managed_agents_web_fetch_tool_config_params: object`

          Configuration override for the web_fetch tool.

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

          - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object`

              Tool calls require user confirmation before execution.

          - `type: optional "web_fetch"`

        - `beta_managed_agents_web_search_tool_config_params: object`

          Configuration override for the web_search tool.

          - `name: "web_search"`

            Must be "web_search".

          - `allowed_domains: optional array of string`

            Only return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

          - `blocked_domains: optional array of string`

            Never return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

          - `enabled: optional boolean`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object`

              Tool calls require user confirmation before execution.

          - `type: optional "web_search"`

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

      - `default_config: optional object`

        Default configuration for all tools in a toolset.

        - `enabled: optional boolean`

          Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

        - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object`

            Tool calls are automatically approved without user confirmation.

          - `beta_managed_agents_always_ask_policy: object`

            Tool calls require user confirmation before execution.

    - `beta_managed_agents_mcp_toolset_params: object`

      Configuration for tools from an MCP server defined in `mcp_servers`.

      - `mcp_server_name: string`

        Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

        minLength: 1, maxLength: 255

      - `type: "mcp_toolset"`

      - `configs: optional array of BetaManagedAgentsMCPToolConfigParams`

        Per-tool configuration overrides.

        - `name: string`

          Name of the MCP tool to configure. 1-128 characters.

          minLength: 1, maxLength: 128

        - `enabled: optional boolean`

          Whether this tool is enabled. Overrides the `default_config` setting.

        - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object`

            Tool calls are automatically approved without user confirmation.

          - `beta_managed_agents_always_ask_policy: object`

            Tool calls require user confirmation before execution.

      - `default_config: optional object`

        Default configuration for all tools from an MCP server.

        - `enabled: optional boolean`

          Whether tools are enabled by default. Defaults to true if not specified.

        - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object`

            Tool calls are automatically approved without user confirmation.

          - `beta_managed_agents_always_ask_policy: object`

            Tool calls require user confirmation before execution.

    - `beta_managed_agents_custom_tool_params: object`

      A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

      - `description: string`

        Description of what the tool does, shown to the agent to help it decide when to use the tool.

        minLength: 1

      - `input_schema: object`

        JSON Schema for custom tool input parameters.

        - `type: "object"`

        - `properties: optional map[unknown]`

        - `required: optional array of string`

      - `name: string`

        Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

        minLength: 1, maxLength: 128

      - `type: "custom"`

  - `version: optional number`

    The specific `agent` version to use. Omit to use the latest version.

    format: int32

### Beta Managed Agents Branch Checkout

- `beta_managed_agents_branch_checkout: object`

  - `name: string`

    Branch name to check out.

    minLength: 1, maxLength: 255

  - `type: "branch"`

### Beta Managed Agents Budget Limit

- `beta_managed_agents_budget_limit: object`

  A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

  - `max_list_cost: object`

    A monetary amount in a specific currency.

    - `amount: string`

      Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

    - `currency: "USD"`

      Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

  - `type: "limit"`

### Beta Managed Agents Cache Creation Usage

- `beta_managed_agents_cache_creation_usage: object`

  Prompt-cache creation token usage broken down by cache lifetime.

  - `ephemeral_1h_input_tokens: optional number`

    Tokens used to create 1-hour ephemeral cache entries.

    format: int32

  - `ephemeral_5m_input_tokens: optional number`

    Tokens used to create 5-minute ephemeral cache entries.

    format: int32

### Beta Managed Agents Commit Checkout

- `beta_managed_agents_commit_checkout: object`

  - `sha: string`

    Full commit SHA to check out.

    minLength: 7, maxLength: 64

  - `type: "commit"`

### Beta Managed Agents Deleted Session

- `beta_managed_agents_deleted_session: object`

  Confirmation that a `session` has been permanently deleted.

  - `id: string`

  - `type: "session_deleted"`

### Beta Managed Agents Delta Content

- `beta_managed_agents_delta_content: object`

  - `content: object`

    Regular text content.

    - `text: string`

      The text content.

      minLength: 1

    - `type: "text"`

  - `type: "content_delta"`

  - `index: optional number`

    Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

    format: uint32

### Beta Managed Agents Delta Event

- `beta_managed_agents_delta_event: object`

  An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

  - `delta: object`

    One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

    - `content: object`

      Regular text content.

      - `text: string`

        The text content.

        minLength: 1

      - `type: "text"`

    - `type: "content_delta"`

    - `index: optional number`

      Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

      format: uint32

  - `event_id: string`

    The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

  - `type: "event_delta"`

### Beta Managed Agents Delta Type

- `beta_managed_agents_delta_type: "agent.message" or "agent.thinking"`

  EventDeltaType enum

  - `"agent.message"`

  - `"agent.thinking"`

### Beta Managed Agents File Resource Params

- `beta_managed_agents_file_resource_params: object`

  Mount a file uploaded via the Files API into the session.

  - `file_id: string`

    ID of a previously uploaded file.

    minLength: 1, maxLength: 128

  - `type: "file"`

  - `mount_path: optional string`

    Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    minLength: 1, maxLength: 4096

### Beta Managed Agents GitHub Repository Resource Params

- `beta_managed_agents_github_repository_resource_params: object`

  Mount a GitHub repository into the session's container.

  - `authorization_token: string`

    GitHub authorization token used to clone the repository.

    minLength: 1, maxLength: 4096

  - `type: "github_repository"`

  - `url: string`

    Github URL of the repository

    minLength: 1, maxLength: 2048

  - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

    Branch or commit to check out. Defaults to the repository's default branch.

    - `beta_managed_agents_branch_checkout: object`

      - `name: string`

        Branch name to check out.

        minLength: 1, maxLength: 255

      - `type: "branch"`

    - `beta_managed_agents_commit_checkout: object`

      - `sha: string`

        Full commit SHA to check out.

        minLength: 7, maxLength: 64

      - `type: "commit"`

  - `mount_path: optional string`

    Mount path in the container. Defaults to `/workspace/<repo-name>`.

    minLength: 1, maxLength: 4096

### Beta Managed Agents Memory Store Resource Param

- `beta_managed_agents_memory_store_resource_param: object`

  Parameters for attaching a memory store to an agent session.

  - `memory_store_id: string`

    The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

  - `type: "memory_store"`

  - `access: optional "read_write" or "read_only"`

    Access mode for an attached memory store.

    - `"read_write"`

    - `"read_only"`

  - `instructions: optional string`

    Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

    maxLength: 4096

### Beta Managed Agents Multiagent

- `beta_managed_agents_multiagent: object`

  Resolved coordinator topology with a concrete agent roster.

  - `agents: array of BetaManagedAgentsAgentReference or BetaManagedAgentsAdvisor`

    Agents the coordinator may spawn as session threads, each resolved to a specific version.

    - `beta_managed_agents_agent_reference: object`

      A resolved agent reference with a concrete version.

      - `id: string`

      - `type: "agent"`

      - `version: number`

        format: int32

    - `beta_managed_agents_advisor: object`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `model: string`

        The advisor model id.

      - `type: "advisor"`

  - `type: "coordinator"`

### Beta Managed Agents Multiagent Params

- `beta_managed_agents_multiagent_params: object`

  A coordinator topology: the session's primary thread orchestrates work by spawning session threads, each running an agent drawn from the `agents` roster.

  - `agents: array of BetaManagedAgentsMultiagentRosterEntryParams`

    Agents the coordinator may spawn as session threads. 1–20 entries. Each entry is an agent ID string, a versioned `{"type":"agent","id","version"}` reference, or `{"type":"self"}` to allow recursive self-invocation. Entries must reference distinct agents (after resolving `self` and string forms); at most one `self`. Referenced agents must exist, must not be archived, and must not themselves have `multiagent` set (depth limit 1).

    - `union_member_0: string`

    - `beta_managed_agents_agent_params: object`

      Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

      - `id: string`

        The `agent` ID.

        minLength: 1, maxLength: 128

      - `type: "agent"`

      - `version: optional number`

        The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

        format: int32

    - `beta_managed_agents_multiagent_self_params: object`

      Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

      - `type: "self"`

    - `beta_managed_agents_advisor_params: object`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn. At most one per roster; the entry occupies the roster name `anthropic.advisor`.

      - `model: string`

        A Claude model id. The model must be permitted as an advisor for this agent's model — see the sessions/threads/advisor spec.

        minLength: 1, maxLength: 256

      - `type: "advisor"`

  - `type: "coordinator"`

### Beta Managed Agents Multiagent Roster Entry Params

- `beta_managed_agents_multiagent_roster_entry_params: string or BetaManagedAgentsAgentParams or BetaManagedAgentsMultiagentSelfParams or BetaManagedAgentsAdvisorParams`

  An entry in a multiagent roster: an agent ID string, a versioned agent reference, or `self`.

  - `union_member_0: string`

  - `beta_managed_agents_agent_params: object`

    Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

    - `id: string`

      The `agent` ID.

      minLength: 1, maxLength: 128

    - `type: "agent"`

    - `version: optional number`

      The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

      format: int32

  - `beta_managed_agents_multiagent_self_params: object`

    Sentinel roster entry meaning "the agent that owns this configuration". Resolved server-side to a concrete agent reference.

    - `type: "self"`

  - `beta_managed_agents_advisor_params: object`

    Platform advisor roster entry: a model the session's primary thread may consult mid-turn. At most one per roster; the entry occupies the roster name `anthropic.advisor`.

    - `model: string`

      A Claude model id. The model must be permitted as an advisor for this agent's model — see the sessions/threads/advisor spec.

      minLength: 1, maxLength: 256

    - `type: "advisor"`

### Beta Managed Agents Outcome Evaluation Resource

- `beta_managed_agents_outcome_evaluation_resource: object`

  Evaluation state for a single outcome defined via a define_outcome event.

  - `completed_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `description: string`

    What the agent should produce.

  - `explanation: string`

    Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs_revision (intermediate), what's missing; for failed, why unrecoverable.

  - `iteration: number`

    0-indexed revision cycle the outcome is currently on.

    format: int32

  - `outcome_id: string`

    Server-generated outc_ ID for this outcome.

  - `result: string`

    Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

  - `type: "outcome_evaluation"`

### Beta Managed Agents Server Tool Usage

- `beta_managed_agents_server_tool_usage: object`

  Cumulative count of server-executed tool invocations, broken down by tool.

  - `web_fetch_requests: optional number`

    Number of server-executed web fetch requests.

    format: int32

  - `web_search_requests: optional number`

    Number of server-executed web search requests.

    format: int32

### Beta Managed Agents Session

- `beta_managed_agents_session: object`

  A Managed Agents `session`.

  - `id: string`

  - `agent: object`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `id: string`

    - `description: string`

    - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

      - `name: string`

      - `type: "url"`

      - `url: string`

    - `model: object`

      Model identifier and configuration.

      - `id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

      - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

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

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `multiagent: object`

      Resolved coordinator topology with full agent definitions for each roster member.

      - `agents: array of BetaManagedAgentsSessionThreadAgent or BetaManagedAgentsAdvisor`

        Full `agent` definitions the coordinator may spawn as session threads.

        - `beta_managed_agents_session_thread_agent: object`

          Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

          - `id: string`

          - `description: string`

          - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

            - `name: string`

            - `type: "url"`

            - `url: string`

          - `model: object`

            Model identifier and configuration.

            - `id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string`

              The model that will power your agent.

              See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

              How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

            - `inference_geo: optional string`

              Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

            - `speed: optional "standard" or "fast"`

              Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `name: string`

          - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

            - `beta_managed_agents_anthropic_skill: object`

              A resolved Anthropic-managed skill.

              - `skill_id: string`

              - `type: "anthropic"`

              - `version: string`

            - `beta_managed_agents_custom_skill: object`

              A resolved user-created custom skill.

              - `skill_id: string`

              - `type: "custom"`

              - `version: string`

          - `system: string`

          - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

            - `beta_managed_agents_agent_toolset20260401: object`

              - `configs: array of BetaManagedAgentsAgentToolConfig`

                - `beta_managed_agents_bash_tool_config: object`

                  Configuration for the bash tool.

                  - `enabled: boolean`

                  - `name: "bash"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                      - `type: "always_allow"`

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                      - `type: "always_ask"`

                  - `type: "bash"`

                - `beta_managed_agents_edit_tool_config: object`

                  Configuration for the edit tool.

                  - `enabled: boolean`

                  - `name: "edit"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "edit"`

                - `beta_managed_agents_read_tool_config: object`

                  Configuration for the read tool.

                  - `enabled: boolean`

                  - `name: "read"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "read"`

                - `beta_managed_agents_write_tool_config: object`

                  Configuration for the write tool.

                  - `enabled: boolean`

                  - `name: "write"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "write"`

                - `beta_managed_agents_glob_tool_config: object`

                  Configuration for the glob tool.

                  - `enabled: boolean`

                  - `name: "glob"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "glob"`

                - `beta_managed_agents_grep_tool_config: object`

                  Configuration for the grep tool.

                  - `enabled: boolean`

                  - `name: "grep"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "grep"`

                - `beta_managed_agents_web_fetch_tool_config: object`

                  Configuration for the web_fetch tool.

                  - `enabled: boolean`

                  - `name: "web_fetch"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "web_fetch"`

                  - `allowed_domains: optional array of string`

                  - `blocked_domains: optional array of string`

                  - `max_content_tokens: optional number`

                    format: int32

                - `beta_managed_agents_web_search_tool_config: object`

                  Configuration for the web_search tool.

                  - `enabled: boolean`

                  - `name: "web_search"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "web_search"`

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

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

              - `type: "agent_toolset_20260401"`

            - `beta_managed_agents_mcp_toolset: object`

              - `configs: array of BetaManagedAgentsMCPToolConfig`

                - `enabled: boolean`

                - `name: string`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

              - `default_config: object`

                Resolved default configuration for all tools from an MCP server.

                - `enabled: boolean`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

              - `mcp_server_name: string`

              - `type: "mcp_toolset"`

            - `beta_managed_agents_custom_tool: object`

              A custom tool as returned in API responses.

              - `description: string`

              - `input_schema: object`

                JSON Schema for custom tool input parameters.

                - `type: "object"`

                - `properties: optional map[unknown]`

                - `required: optional array of string`

              - `name: string`

              - `type: "custom"`

          - `type: "agent"`

          - `version: number`

            format: int32

        - `beta_managed_agents_advisor: object`

          Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

          - `model: string`

            The advisor model id.

          - `type: "advisor"`

      - `type: "coordinator"`

    - `name: string`

    - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

      - `beta_managed_agents_anthropic_skill: object`

        A resolved Anthropic-managed skill.

      - `beta_managed_agents_custom_skill: object`

        A resolved user-created custom skill.

    - `system: string`

    - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

      - `beta_managed_agents_agent_toolset20260401: object`

      - `beta_managed_agents_mcp_toolset: object`

      - `beta_managed_agents_custom_tool: object`

        A custom tool as returned in API responses.

    - `type: "agent"`

    - `version: number`

      format: int32

  - `archived_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `budget: object`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `max_list_cost: object`

      A monetary amount in a specific currency.

      - `amount: string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: "USD"`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `type: "limit"`

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `environment_id: string`

  - `metadata: map[string]`

  - `outcome_evaluations: array of BetaManagedAgentsOutcomeEvaluationResource`

    Per-outcome evaluation state. One entry per define_outcome event sent to the session.

    - `completed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `description: string`

      What the agent should produce.

    - `explanation: string`

      Grader's verdict text from the most recent evaluation. For satisfied, explains why criteria are met; for needs_revision (intermediate), what's missing; for failed, why unrecoverable.

    - `iteration: number`

      0-indexed revision cycle the outcome is currently on.

      format: int32

    - `outcome_id: string`

      Server-generated outc_ ID for this outcome.

    - `result: string`

      Current evaluation state. `pending` before the agent begins work; `running` while producing or revising; `evaluating` while the grader scores; `satisfied`/`max_iterations_reached`/`failed`/`interrupted` are terminal.

    - `type: "outcome_evaluation"`

  - `resources: array of BetaManagedAgentsSessionResource`

    - `beta_managed_agents_github_repository_resource: object`

      - `id: string`

      - `created_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `mount_path: string`

      - `type: "github_repository"`

      - `updated_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `url: string`

      - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

        - `beta_managed_agents_branch_checkout: object`

          - `name: string`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `type: "branch"`

        - `beta_managed_agents_commit_checkout: object`

          - `sha: string`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `type: "commit"`

    - `beta_managed_agents_file_resource: object`

      - `id: string`

      - `created_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `file_id: string`

      - `mount_path: string`

      - `type: "file"`

      - `updated_at: string`

        A timestamp in RFC 3339 format

        format: date-time

    - `beta_managed_agents_memory_store_resource: object`

      A memory store attached to an agent session.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

      - `access: optional "read_write" or "read_only"`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `description: optional string`

        Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

      - `instructions: optional string`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

        maxLength: 4096

      - `mount_path: optional string`

        Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

      - `name: optional string`

        Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

  - `stats: object`

    Timing statistics for a session.

    - `active_seconds: optional number`

      Cumulative time in seconds the session spent in running status. Excludes idle time.

      format: double

    - `duration_seconds: optional number`

      Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

      format: double

  - `status: "rescheduling" or "running" or "idle" or "terminated"`

    SessionStatus enum

    - `"rescheduling"`

    - `"running"`

    - `"idle"`

    - `"terminated"`

  - `title: string`

  - `type: "session"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `usage: object`

    Cumulative token usage for a session across all turns.

    - `active_seconds: optional number`

      Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once, unlike `stats.active_seconds`, which sums each thread's own active time. This is the duration the session's runtime cost is priced on.

      format: double

    - `cache_creation: optional object`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: optional number`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `ephemeral_5m_input_tokens: optional number`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `cache_read_input_tokens: optional number`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens: optional number`

      Total input tokens consumed across all turns.

      format: int32

    - `list_cost: optional object`

      A monetary amount in a specific currency.

      - `amount: string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: "USD"`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `output_tokens: optional number`

      Total output tokens generated across all turns.

      format: int32

    - `server_tool_use: optional object`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `web_fetch_requests: optional number`

        Number of server-executed web fetch requests.

        format: int32

      - `web_search_requests: optional number`

        Number of server-executed web search requests.

        format: int32

  - `vault_ids: array of string`

    Vault IDs attached to the session at creation. Empty when no vaults were supplied.

  - `deployment_id: optional string`

    Deployment ID when the session was created from a deployment reference. Null otherwise.

### Beta Managed Agents Session Agent

- `beta_managed_agents_session_agent: object`

  Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

  - `id: string`

  - `description: string`

  - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

    - `name: string`

    - `type: "url"`

    - `url: string`

  - `model: object`

    Model identifier and configuration.

    - `id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string`

      The model that will power your agent.

      See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

    - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

      How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

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

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `multiagent: object`

    Resolved coordinator topology with full agent definitions for each roster member.

    - `agents: array of BetaManagedAgentsSessionThreadAgent or BetaManagedAgentsAdvisor`

      Full `agent` definitions the coordinator may spawn as session threads.

      - `beta_managed_agents_session_thread_agent: object`

        Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

        - `id: string`

        - `description: string`

        - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

          - `name: string`

          - `type: "url"`

          - `url: string`

        - `model: object`

          Model identifier and configuration.

          - `id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

            How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `inference_geo: optional string`

            Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

          - `speed: optional "standard" or "fast"`

            Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `name: string`

        - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

          - `beta_managed_agents_anthropic_skill: object`

            A resolved Anthropic-managed skill.

            - `skill_id: string`

            - `type: "anthropic"`

            - `version: string`

          - `beta_managed_agents_custom_skill: object`

            A resolved user-created custom skill.

            - `skill_id: string`

            - `type: "custom"`

            - `version: string`

        - `system: string`

        - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

          - `beta_managed_agents_agent_toolset20260401: object`

            - `configs: array of BetaManagedAgentsAgentToolConfig`

              - `beta_managed_agents_bash_tool_config: object`

                Configuration for the bash tool.

                - `enabled: boolean`

                - `name: "bash"`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                    - `type: "always_allow"`

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

                    - `type: "always_ask"`

                - `type: "bash"`

              - `beta_managed_agents_edit_tool_config: object`

                Configuration for the edit tool.

                - `enabled: boolean`

                - `name: "edit"`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

                - `type: "edit"`

              - `beta_managed_agents_read_tool_config: object`

                Configuration for the read tool.

                - `enabled: boolean`

                - `name: "read"`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

                - `type: "read"`

              - `beta_managed_agents_write_tool_config: object`

                Configuration for the write tool.

                - `enabled: boolean`

                - `name: "write"`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

                - `type: "write"`

              - `beta_managed_agents_glob_tool_config: object`

                Configuration for the glob tool.

                - `enabled: boolean`

                - `name: "glob"`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

                - `type: "glob"`

              - `beta_managed_agents_grep_tool_config: object`

                Configuration for the grep tool.

                - `enabled: boolean`

                - `name: "grep"`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

                - `type: "grep"`

              - `beta_managed_agents_web_fetch_tool_config: object`

                Configuration for the web_fetch tool.

                - `enabled: boolean`

                - `name: "web_fetch"`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

                - `type: "web_fetch"`

                - `allowed_domains: optional array of string`

                - `blocked_domains: optional array of string`

                - `max_content_tokens: optional number`

                  format: int32

              - `beta_managed_agents_web_search_tool_config: object`

                Configuration for the web_search tool.

                - `enabled: boolean`

                - `name: "web_search"`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

                - `type: "web_search"`

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

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

            - `type: "agent_toolset_20260401"`

          - `beta_managed_agents_mcp_toolset: object`

            - `configs: array of BetaManagedAgentsMCPToolConfig`

              - `enabled: boolean`

              - `name: string`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

            - `default_config: object`

              Resolved default configuration for all tools from an MCP server.

              - `enabled: boolean`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

            - `mcp_server_name: string`

            - `type: "mcp_toolset"`

          - `beta_managed_agents_custom_tool: object`

            A custom tool as returned in API responses.

            - `description: string`

            - `input_schema: object`

              JSON Schema for custom tool input parameters.

              - `type: "object"`

              - `properties: optional map[unknown]`

              - `required: optional array of string`

            - `name: string`

            - `type: "custom"`

        - `type: "agent"`

        - `version: number`

          format: int32

      - `beta_managed_agents_advisor: object`

        Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

        - `model: string`

          The advisor model id.

        - `type: "advisor"`

    - `type: "coordinator"`

  - `name: string`

  - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

    - `beta_managed_agents_anthropic_skill: object`

      A resolved Anthropic-managed skill.

    - `beta_managed_agents_custom_skill: object`

      A resolved user-created custom skill.

  - `system: string`

  - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

    - `beta_managed_agents_agent_toolset20260401: object`

    - `beta_managed_agents_mcp_toolset: object`

    - `beta_managed_agents_custom_tool: object`

      A custom tool as returned in API responses.

  - `type: "agent"`

  - `version: number`

    format: int32

### Beta Managed Agents Session Agent Update

- `beta_managed_agents_session_agent_update: object`

  Mid-session agent configuration update. Only `tools` and `mcp_servers` are updatable. Full replacement: the provided array becomes the new value. To preserve existing entries, GET the session, modify the array, and POST it back.

  - `mcp_servers: optional array of BetaManagedAgentsURLMCPServerParams`

    Replacement MCP server list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.

    - `name: string`

      Unique name for this server, referenced by mcp_toolset configurations. 1-255 characters.

      minLength: 1, maxLength: 255

    - `type: "url"`

    - `url: string`

      Endpoint URL for the MCP server.

      maxLength: 2048

  - `tools: optional array of BetaManagedAgentsAgentToolset20260401Params or BetaManagedAgentsMCPToolsetParams or BetaManagedAgentsCustomToolParams`

    Replacement tool list. Full replacement: the provided array becomes the new value. Send an empty array to clear; omit to preserve.

    - `beta_managed_agents_agent_toolset20260401_params: object`

      Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

      - `type: "agent_toolset_20260401"`

      - `configs: optional array of BetaManagedAgentsAgentToolConfigParams`

        Per-tool configuration overrides.

        - `beta_managed_agents_bash_tool_config_params: object`

          Configuration override for the bash tool.

          - `name: "bash"`

            Must be "bash".

          - `enabled: optional boolean`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object`

              Tool calls are automatically approved without user confirmation.

              - `type: "always_allow"`

            - `beta_managed_agents_always_ask_policy: object`

              Tool calls require user confirmation before execution.

              - `type: "always_ask"`

          - `type: optional "bash"`

        - `beta_managed_agents_edit_tool_config_params: object`

          Configuration override for the edit tool.

          - `name: "edit"`

            Must be "edit".

          - `enabled: optional boolean`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object`

              Tool calls require user confirmation before execution.

          - `type: optional "edit"`

        - `beta_managed_agents_read_tool_config_params: object`

          Configuration override for the read tool.

          - `name: "read"`

            Must be "read".

          - `enabled: optional boolean`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object`

              Tool calls require user confirmation before execution.

          - `type: optional "read"`

        - `beta_managed_agents_write_tool_config_params: object`

          Configuration override for the write tool.

          - `name: "write"`

            Must be "write".

          - `enabled: optional boolean`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object`

              Tool calls require user confirmation before execution.

          - `type: optional "write"`

        - `beta_managed_agents_glob_tool_config_params: object`

          Configuration override for the glob tool.

          - `name: "glob"`

            Must be "glob".

          - `enabled: optional boolean`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object`

              Tool calls require user confirmation before execution.

          - `type: optional "glob"`

        - `beta_managed_agents_grep_tool_config_params: object`

          Configuration override for the grep tool.

          - `name: "grep"`

            Must be "grep".

          - `enabled: optional boolean`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object`

              Tool calls require user confirmation before execution.

          - `type: optional "grep"`

        - `beta_managed_agents_web_fetch_tool_config_params: object`

          Configuration override for the web_fetch tool.

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

          - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object`

              Tool calls require user confirmation before execution.

          - `type: optional "web_fetch"`

        - `beta_managed_agents_web_search_tool_config_params: object`

          Configuration override for the web_search tool.

          - `name: "web_search"`

            Must be "web_search".

          - `allowed_domains: optional array of string`

            Only return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "docs.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with blocked_domains.

          - `blocked_domains: optional array of string`

            Never return search results whose host is one of these domains or a subdomain of one. Each entry is a plain hostname like "ads.example.com" (no scheme or port; an optional path suffix is accepted). At most 64 entries; an empty list is rejected (omit the field instead). Cannot be combined with allowed_domains.

          - `enabled: optional boolean`

            Whether this tool is enabled and available to Claude. Overrides the default_config setting.

          - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

            Permission policy for tool execution.

            - `beta_managed_agents_always_allow_policy: object`

              Tool calls are automatically approved without user confirmation.

            - `beta_managed_agents_always_ask_policy: object`

              Tool calls require user confirmation before execution.

          - `type: optional "web_search"`

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

      - `default_config: optional object`

        Default configuration for all tools in a toolset.

        - `enabled: optional boolean`

          Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

        - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object`

            Tool calls are automatically approved without user confirmation.

          - `beta_managed_agents_always_ask_policy: object`

            Tool calls require user confirmation before execution.

    - `beta_managed_agents_mcp_toolset_params: object`

      Configuration for tools from an MCP server defined in `mcp_servers`.

      - `mcp_server_name: string`

        Name of the MCP server. Must match a server name from the mcp_servers array. 1-255 characters.

        minLength: 1, maxLength: 255

      - `type: "mcp_toolset"`

      - `configs: optional array of BetaManagedAgentsMCPToolConfigParams`

        Per-tool configuration overrides.

        - `name: string`

          Name of the MCP tool to configure. 1-128 characters.

          minLength: 1, maxLength: 128

        - `enabled: optional boolean`

          Whether this tool is enabled. Overrides the `default_config` setting.

        - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object`

            Tool calls are automatically approved without user confirmation.

          - `beta_managed_agents_always_ask_policy: object`

            Tool calls require user confirmation before execution.

      - `default_config: optional object`

        Default configuration for all tools from an MCP server.

        - `enabled: optional boolean`

          Whether tools are enabled by default. Defaults to true if not specified.

        - `permission_policy: optional BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

          Permission policy for tool execution.

          - `beta_managed_agents_always_allow_policy: object`

            Tool calls are automatically approved without user confirmation.

          - `beta_managed_agents_always_ask_policy: object`

            Tool calls require user confirmation before execution.

    - `beta_managed_agents_custom_tool_params: object`

      A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

      - `description: string`

        Description of what the tool does, shown to the agent to help it decide when to use the tool.

        minLength: 1

      - `input_schema: object`

        JSON Schema for custom tool input parameters.

        - `type: "object"`

        - `properties: optional map[unknown]`

        - `required: optional array of string`

      - `name: string`

        Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

        minLength: 1, maxLength: 128

      - `type: "custom"`

### Beta Managed Agents Session Multiagent Coordinator

- `beta_managed_agents_session_multiagent_coordinator: object`

  Resolved coordinator topology with full agent definitions for each roster member.

  - `agents: array of BetaManagedAgentsSessionThreadAgent or BetaManagedAgentsAdvisor`

    Full `agent` definitions the coordinator may spawn as session threads.

    - `beta_managed_agents_session_thread_agent: object`

      Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

      - `id: string`

      - `description: string`

      - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

        - `name: string`

        - `type: "url"`

        - `url: string`

      - `model: object`

        Model identifier and configuration.

        - `id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

        - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

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

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

      - `name: string`

      - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

        - `beta_managed_agents_anthropic_skill: object`

          A resolved Anthropic-managed skill.

          - `skill_id: string`

          - `type: "anthropic"`

          - `version: string`

        - `beta_managed_agents_custom_skill: object`

          A resolved user-created custom skill.

          - `skill_id: string`

          - `type: "custom"`

          - `version: string`

      - `system: string`

      - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

        - `beta_managed_agents_agent_toolset20260401: object`

          - `configs: array of BetaManagedAgentsAgentToolConfig`

            - `beta_managed_agents_bash_tool_config: object`

              Configuration for the bash tool.

              - `enabled: boolean`

              - `name: "bash"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                  - `type: "always_allow"`

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

                  - `type: "always_ask"`

              - `type: "bash"`

            - `beta_managed_agents_edit_tool_config: object`

              Configuration for the edit tool.

              - `enabled: boolean`

              - `name: "edit"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

              - `type: "edit"`

            - `beta_managed_agents_read_tool_config: object`

              Configuration for the read tool.

              - `enabled: boolean`

              - `name: "read"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

              - `type: "read"`

            - `beta_managed_agents_write_tool_config: object`

              Configuration for the write tool.

              - `enabled: boolean`

              - `name: "write"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

              - `type: "write"`

            - `beta_managed_agents_glob_tool_config: object`

              Configuration for the glob tool.

              - `enabled: boolean`

              - `name: "glob"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

              - `type: "glob"`

            - `beta_managed_agents_grep_tool_config: object`

              Configuration for the grep tool.

              - `enabled: boolean`

              - `name: "grep"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

              - `type: "grep"`

            - `beta_managed_agents_web_fetch_tool_config: object`

              Configuration for the web_fetch tool.

              - `enabled: boolean`

              - `name: "web_fetch"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

              - `type: "web_fetch"`

              - `allowed_domains: optional array of string`

              - `blocked_domains: optional array of string`

              - `max_content_tokens: optional number`

                format: int32

            - `beta_managed_agents_web_search_tool_config: object`

              Configuration for the web_search tool.

              - `enabled: boolean`

              - `name: "web_search"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

              - `type: "web_search"`

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

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object`

                Tool calls are automatically approved without user confirmation.

              - `beta_managed_agents_always_ask_policy: object`

                Tool calls require user confirmation before execution.

          - `type: "agent_toolset_20260401"`

        - `beta_managed_agents_mcp_toolset: object`

          - `configs: array of BetaManagedAgentsMCPToolConfig`

            - `enabled: boolean`

            - `name: string`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object`

                Tool calls are automatically approved without user confirmation.

              - `beta_managed_agents_always_ask_policy: object`

                Tool calls require user confirmation before execution.

          - `default_config: object`

            Resolved default configuration for all tools from an MCP server.

            - `enabled: boolean`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object`

                Tool calls are automatically approved without user confirmation.

              - `beta_managed_agents_always_ask_policy: object`

                Tool calls require user confirmation before execution.

          - `mcp_server_name: string`

          - `type: "mcp_toolset"`

        - `beta_managed_agents_custom_tool: object`

          A custom tool as returned in API responses.

          - `description: string`

          - `input_schema: object`

            JSON Schema for custom tool input parameters.

            - `type: "object"`

            - `properties: optional map[unknown]`

            - `required: optional array of string`

          - `name: string`

          - `type: "custom"`

      - `type: "agent"`

      - `version: number`

        format: int32

    - `beta_managed_agents_advisor: object`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `model: string`

        The advisor model id.

      - `type: "advisor"`

  - `type: "coordinator"`

### Beta Managed Agents Session Stats

- `beta_managed_agents_session_stats: object`

  Timing statistics for a session.

  - `active_seconds: optional number`

    Cumulative time in seconds the session spent in running status. Excludes idle time.

    format: double

  - `duration_seconds: optional number`

    Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

    format: double

### Beta Managed Agents Session Updated Event

- `beta_managed_agents_session_updated_event: object`

  Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `type: "session.updated"`

  - `agent: optional object`

    Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

    - `id: string`

    - `description: string`

    - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

      - `name: string`

      - `type: "url"`

      - `url: string`

    - `model: object`

      Model identifier and configuration.

      - `id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string`

        The model that will power your agent.

        See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

      - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

        How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

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

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `multiagent: object`

      Resolved coordinator topology with full agent definitions for each roster member.

      - `agents: array of BetaManagedAgentsSessionThreadAgent or BetaManagedAgentsAdvisor`

        Full `agent` definitions the coordinator may spawn as session threads.

        - `beta_managed_agents_session_thread_agent: object`

          Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

          - `id: string`

          - `description: string`

          - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

            - `name: string`

            - `type: "url"`

            - `url: string`

          - `model: object`

            Model identifier and configuration.

            - `id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string`

              The model that will power your agent.

              See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

            - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

              How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

            - `inference_geo: optional string`

              Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

            - `speed: optional "standard" or "fast"`

              Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `name: string`

          - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

            - `beta_managed_agents_anthropic_skill: object`

              A resolved Anthropic-managed skill.

              - `skill_id: string`

              - `type: "anthropic"`

              - `version: string`

            - `beta_managed_agents_custom_skill: object`

              A resolved user-created custom skill.

              - `skill_id: string`

              - `type: "custom"`

              - `version: string`

          - `system: string`

          - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

            - `beta_managed_agents_agent_toolset20260401: object`

              - `configs: array of BetaManagedAgentsAgentToolConfig`

                - `beta_managed_agents_bash_tool_config: object`

                  Configuration for the bash tool.

                  - `enabled: boolean`

                  - `name: "bash"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                      - `type: "always_allow"`

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                      - `type: "always_ask"`

                  - `type: "bash"`

                - `beta_managed_agents_edit_tool_config: object`

                  Configuration for the edit tool.

                  - `enabled: boolean`

                  - `name: "edit"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "edit"`

                - `beta_managed_agents_read_tool_config: object`

                  Configuration for the read tool.

                  - `enabled: boolean`

                  - `name: "read"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "read"`

                - `beta_managed_agents_write_tool_config: object`

                  Configuration for the write tool.

                  - `enabled: boolean`

                  - `name: "write"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "write"`

                - `beta_managed_agents_glob_tool_config: object`

                  Configuration for the glob tool.

                  - `enabled: boolean`

                  - `name: "glob"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "glob"`

                - `beta_managed_agents_grep_tool_config: object`

                  Configuration for the grep tool.

                  - `enabled: boolean`

                  - `name: "grep"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "grep"`

                - `beta_managed_agents_web_fetch_tool_config: object`

                  Configuration for the web_fetch tool.

                  - `enabled: boolean`

                  - `name: "web_fetch"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "web_fetch"`

                  - `allowed_domains: optional array of string`

                  - `blocked_domains: optional array of string`

                  - `max_content_tokens: optional number`

                    format: int32

                - `beta_managed_agents_web_search_tool_config: object`

                  Configuration for the web_search tool.

                  - `enabled: boolean`

                  - `name: "web_search"`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                  - `type: "web_search"`

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

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

              - `type: "agent_toolset_20260401"`

            - `beta_managed_agents_mcp_toolset: object`

              - `configs: array of BetaManagedAgentsMCPToolConfig`

                - `enabled: boolean`

                - `name: string`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

              - `default_config: object`

                Resolved default configuration for all tools from an MCP server.

                - `enabled: boolean`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

              - `mcp_server_name: string`

              - `type: "mcp_toolset"`

            - `beta_managed_agents_custom_tool: object`

              A custom tool as returned in API responses.

              - `description: string`

              - `input_schema: object`

                JSON Schema for custom tool input parameters.

                - `type: "object"`

                - `properties: optional map[unknown]`

                - `required: optional array of string`

              - `name: string`

              - `type: "custom"`

          - `type: "agent"`

          - `version: number`

            format: int32

        - `beta_managed_agents_advisor: object`

          Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

          - `model: string`

            The advisor model id.

          - `type: "advisor"`

      - `type: "coordinator"`

    - `name: string`

    - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

      - `beta_managed_agents_anthropic_skill: object`

        A resolved Anthropic-managed skill.

      - `beta_managed_agents_custom_skill: object`

        A resolved user-created custom skill.

    - `system: string`

    - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

      - `beta_managed_agents_agent_toolset20260401: object`

      - `beta_managed_agents_mcp_toolset: object`

      - `beta_managed_agents_custom_tool: object`

        A custom tool as returned in API responses.

    - `type: "agent"`

    - `version: number`

      format: int32

  - `budget: optional object`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `max_list_cost: object`

      A monetary amount in a specific currency.

      - `amount: string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: "USD"`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `type: "limit"`

  - `metadata: optional map[string]`

    The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

  - `title: optional string`

    The session's new title. Present only when the update changed it.

### Beta Managed Agents Session Usage

- `beta_managed_agents_session_usage: object`

  Cumulative token usage for a session across all turns.

  - `active_seconds: optional number`

    Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once, unlike `stats.active_seconds`, which sums each thread's own active time. This is the duration the session's runtime cost is priced on.

    format: double

  - `cache_creation: optional object`

    Prompt-cache creation token usage broken down by cache lifetime.

    - `ephemeral_1h_input_tokens: optional number`

      Tokens used to create 1-hour ephemeral cache entries.

      format: int32

    - `ephemeral_5m_input_tokens: optional number`

      Tokens used to create 5-minute ephemeral cache entries.

      format: int32

  - `cache_read_input_tokens: optional number`

    Total tokens read from prompt cache.

    format: int32

  - `input_tokens: optional number`

    Total input tokens consumed across all turns.

    format: int32

  - `list_cost: optional object`

    A monetary amount in a specific currency.

    - `amount: string`

      Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

    - `currency: "USD"`

      Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

  - `output_tokens: optional number`

    Total output tokens generated across all turns.

    format: int32

  - `server_tool_use: optional object`

    Cumulative count of server-executed tool invocations, broken down by tool.

    - `web_fetch_requests: optional number`

      Number of server-executed web fetch requests.

      format: int32

    - `web_search_requests: optional number`

      Number of server-executed web search requests.

      format: int32

### Beta Managed Agents Session Usage Event

- `beta_managed_agents_session_usage_event: object`

  Periodic snapshot of the session's cumulative usage and tracked list cost.

  - `id: string`

    Unique identifier for this event.

  - `processed_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `type: "session.usage"`

  - `usage: object`

    Point-in-time snapshot of a session's cumulative usage.

    - `active_seconds: optional number`

      Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

      format: double

    - `cache_creation: optional object`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: optional number`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `ephemeral_5m_input_tokens: optional number`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `cache_read_input_tokens: optional number`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens: optional number`

      Total input tokens consumed across all turns.

      format: int32

    - `list_cost: optional object`

      A monetary amount in a specific currency.

      - `amount: string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: "USD"`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `output_tokens: optional number`

      Total output tokens generated across all turns.

      format: int32

    - `server_tool_use: optional object`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `web_fetch_requests: optional number`

        Number of server-executed web fetch requests.

        format: int32

      - `web_search_requests: optional number`

        Number of server-executed web search requests.

        format: int32

  - `budget: optional object`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `max_list_cost: object`

      A monetary amount in a specific currency.

      - `amount: string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: "USD"`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `type: "limit"`

### Beta Managed Agents Start Event

- `beta_managed_agents_start_event: object`

  Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

  - `event: BetaManagedAgentsAgentMessagePreview or BetaManagedAgentsAgentThinkingPreview`

    The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

    - `beta_managed_agents_agent_message_preview: object`

      - `id: string`

        The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

      - `type: "agent.message"`

    - `beta_managed_agents_agent_thinking_preview: object`

      - `id: string`

        The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

      - `type: "agent.thinking"`

  - `type: "event_start"`

### Beta Managed Agents Start Event Preview

- `beta_managed_agents_start_event_preview: BetaManagedAgentsAgentMessagePreview or BetaManagedAgentsAgentThinkingPreview`

  - `beta_managed_agents_agent_message_preview: object`

    - `id: string`

      The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

    - `type: "agent.message"`

  - `beta_managed_agents_agent_thinking_preview: object`

    - `id: string`

      The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

    - `type: "agent.thinking"`

### Beta Managed Agents System Content Block

- `beta_managed_agents_system_content_block: object`

  Regular text content.

  - `text: string`

    The text content.

    minLength: 1

  - `type: "text"`

### Beta Managed Agents System Message Event

- `beta_managed_agents_system_message_event: object`

  A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

  - `id: string`

    Unique identifier for this event.

  - `content: array of BetaManagedAgentsSystemContentBlock`

    System content blocks. Text-only.

    - `text: string`

      The text content.

      minLength: 1

    - `type: "text"`

  - `type: "system.message"`

  - `processed_at: optional string`

    A timestamp in RFC 3339 format

    format: date-time

### Beta Managed Agents User Tool Result Event

- `beta_managed_agents_user_tool_result_event: object`

  Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

  - `id: string`

    Unique identifier for this event.

  - `tool_use_id: string`

    The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

  - `type: "user.tool_result"`

  - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

    The result content returned by the tool.

    - `beta_managed_agents_text_block: object`

      Regular text content.

      - `text: string`

        The text content.

        minLength: 1

      - `type: "text"`

    - `beta_managed_agents_image_block: object`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

        Union type for image source variants.

        - `beta_managed_agents_base64_image_source: object`

          Base64-encoded image data.

          - `data: string`

            Base64-encoded image data.

            minLength: 1

          - `media_type: string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            minLength: 1

          - `type: "base64"`

        - `beta_managed_agents_url_image_source: object`

          Image referenced by URL.

          - `type: "url"`

          - `url: string`

            URL of the image to fetch.

            minLength: 1

        - `beta_managed_agents_file_image_source: object`

          Image referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

            minLength: 1

          - `type: "file"`

      - `type: "image"`

    - `beta_managed_agents_document_block: object`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `beta_managed_agents_base64_document_source: object`

          Base64-encoded document data.

          - `data: string`

            Base64-encoded document data.

            minLength: 1

          - `media_type: string`

            MIME type of the document (e.g., "application/pdf").

            minLength: 1

          - `type: "base64"`

        - `beta_managed_agents_plain_text_document_source: object`

          Plain text document content.

          - `data: string`

            The plain text content.

            minLength: 1

          - `media_type: "text/plain"`

            MIME type of the text content. Must be "text/plain".

          - `type: "text"`

        - `beta_managed_agents_url_document_source: object`

          Document referenced by URL.

          - `type: "url"`

          - `url: string`

            URL of the document to fetch.

            minLength: 1

        - `beta_managed_agents_file_document_source: object`

          Document referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

            minLength: 1

          - `type: "file"`

      - `type: "document"`

      - `context: optional string`

        Additional context about the document for the model.

      - `title: optional string`

        The title of the document.

    - `beta_managed_agents_search_result_block: object`

      A block containing a web search result.

      - `citations: object`

        Citation settings for a search result.

        - `enabled: boolean`

          Whether citations are enabled for this search result.

      - `content: array of BetaManagedAgentsSearchResultContent`

        Array of text content blocks from the search result.

        - `text: string`

          The text content.

          minLength: 1

        - `type: "text"`

      - `source: string`

        The URL source of the search result.

        minLength: 1

      - `title: string`

        The title of the search result.

        minLength: 1

      - `type: "search_result"`

  - `is_error: optional boolean`

    Whether the tool execution resulted in an error.

  - `processed_at: optional string`

    A timestamp in RFC 3339 format

    format: date-time

  - `session_thread_id: optional string`

    Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

## Sessions › Events

### List Events

`$ ant beta:sessions:events list`

**GET** `/v1/sessions/{session_id}/events`

List Events

#### Parameters

- `--session-id: string`

  Path param: Path parameter session_id

- `--created-at-gt: optional string`

  Query param: Return events created after this time (exclusive). Compared against the event's `processed_at` value.

  format: date-time

- `--created-at-gte: optional string`

  Query param: Return events created at or after this time (inclusive). Compared against the event's `processed_at` value.

  format: date-time

- `--created-at-lt: optional string`

  Query param: Return events created before this time (exclusive). Compared against the event's `processed_at` value.

  format: date-time

- `--created-at-lte: optional string`

  Query param: Return events created at or before this time (inclusive). Compared against the event's `processed_at` value.

  format: date-time

- `--limit: optional number`

  Query param: Query parameter for limit

  format: int32

- `--order: optional "asc" or "desc"`

  Query param: Sort direction for results, ordered by the event's `processed_at`. Defaults to asc (chronological).

- `--page: optional string`

  Query param: Opaque pagination cursor from a previous response's next_page.

- `--type: optional array of string`

  Query param: Filter by event type. Values match the `type` field on returned events (for example, `user.message` or `agent.tool_use`). Omit to return all event types.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `BetaManagedAgentsListSessionEvents: object`

  Paginated list of events for a `session`.

  - `data: optional array of BetaManagedAgentsSessionEvent`

    Events for the session, ordered by `processed_at`.

    - `beta_managed_agents_user_message_event: object`

      A user message event in the session conversation.

      - `id: string`

        Unique identifier for this event.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

        Array of content blocks comprising the user message.

        - `beta_managed_agents_text_block: object`

          Regular text content.

          - `text: string`

            The text content.

            minLength: 1

          - `type: "text"`

        - `beta_managed_agents_image_block: object`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `beta_managed_agents_base64_image_source: object`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

                minLength: 1

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `type: "base64"`

            - `beta_managed_agents_url_image_source: object`

              Image referenced by URL.

              - `type: "url"`

              - `url: string`

                URL of the image to fetch.

                minLength: 1

            - `beta_managed_agents_file_image_source: object`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

                minLength: 1

              - `type: "file"`

          - `type: "image"`

        - `beta_managed_agents_document_block: object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `beta_managed_agents_base64_document_source: object`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

                minLength: 1

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `type: "base64"`

            - `beta_managed_agents_plain_text_document_source: object`

              Plain text document content.

              - `data: string`

                The plain text content.

                minLength: 1

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

              - `type: "text"`

            - `beta_managed_agents_url_document_source: object`

              Document referenced by URL.

              - `type: "url"`

              - `url: string`

                URL of the document to fetch.

                minLength: 1

            - `beta_managed_agents_file_document_source: object`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

                minLength: 1

              - `type: "file"`

          - `type: "document"`

          - `context: optional string`

            Additional context about the document for the model.

          - `title: optional string`

            The title of the document.

        - `beta_managed_agents_redacted_block: object`

          Placeholder for content withheld by Anthropic model policy.

          - `type: "redacted"`

      - `type: "user.message"`

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

        format: date-time

    - `beta_managed_agents_user_interrupt_event: object`

      An interrupt event that pauses agent execution and returns control to the user.

      - `id: string`

        Unique identifier for this event.

      - `type: "user.interrupt"`

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: optional string`

        If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

    - `beta_managed_agents_user_tool_confirmation_event: object`

      A tool confirmation event that approves or denies a pending tool execution.

      - `id: string`

        Unique identifier for this event.

      - `result: "allow" or "deny"`

        UserToolConfirmationResult enum

        - `"allow"`

        - `"deny"`

      - `tool_use_id: string`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: "user.tool_confirmation"`

      - `deny_message: optional string`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

        maxLength: 10000

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: optional string`

        When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

    - `beta_managed_agents_user_custom_tool_result_event: object`

      Event sent by the client providing the result of a custom tool execution.

      - `id: string`

        Unique identifier for this event.

      - `custom_tool_use_id: string`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: "user.custom_tool_result"`

      - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

        The result content returned by the tool.

        - `beta_managed_agents_text_block: object`

          Regular text content.

        - `beta_managed_agents_image_block: object`

          Image content specified directly as base64 data or as a reference via a URL.

        - `beta_managed_agents_document_block: object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `beta_managed_agents_search_result_block: object`

          A block containing a web search result.

          - `citations: object`

            Citation settings for a search result.

            - `enabled: boolean`

              Whether citations are enabled for this search result.

          - `content: array of BetaManagedAgentsSearchResultContent`

            Array of text content blocks from the search result.

            - `text: string`

              The text content.

              minLength: 1

            - `type: "text"`

          - `source: string`

            The URL source of the search result.

            minLength: 1

          - `title: string`

            The title of the search result.

            minLength: 1

          - `type: "search_result"`

      - `is_error: optional boolean`

        Whether the tool execution resulted in an error.

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: optional string`

        Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

    - `beta_managed_agents_agent_custom_tool_use_event: object`

      Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

      - `id: string`

        Unique identifier for this event.

      - `input: map[unknown]`

        Input parameters for the tool call.

      - `name: string`

        Name of the custom tool being called.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: "agent.custom_tool_use"`

      - `session_thread_id: optional string`

        When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

    - `beta_managed_agents_agent_message_event: object`

      An agent response event in the session conversation.

      - `id: string`

        Unique identifier for this event.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsRedactedBlock`

        Array of text blocks comprising the agent response.

        - `beta_managed_agents_text_block: object`

          Regular text content.

        - `beta_managed_agents_redacted_block: object`

          Placeholder for content withheld by Anthropic model policy.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: "agent.message"`

    - `beta_managed_agents_agent_thinking_event: object`

      Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: "agent.thinking"`

    - `beta_managed_agents_agent_mcp_tool_use_event: object`

      Event emitted when the agent invokes a tool provided by an MCP server.

      - `id: string`

        Unique identifier for this event.

      - `input: map[unknown]`

        Input parameters for the tool call.

      - `mcp_server_name: string`

        Name of the MCP server providing the tool.

      - `name: string`

        Name of the MCP tool being used.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: "agent.mcp_tool_use"`

      - `evaluated_permission: optional "allow" or "ask" or "deny"`

        AgentEvaluatedPermission enum

        - `"allow"`

        - `"ask"`

        - `"deny"`

      - `session_thread_id: optional string`

        When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

    - `beta_managed_agents_agent_mcp_tool_result_event: object`

      Event representing the result of an MCP tool execution.

      - `id: string`

        Unique identifier for this event.

      - `mcp_tool_use_id: string`

        The id of the `agent.mcp_tool_use` event this result corresponds to.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: "agent.mcp_tool_result"`

      - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

        The result content returned by the tool.

        - `beta_managed_agents_text_block: object`

          Regular text content.

        - `beta_managed_agents_image_block: object`

          Image content specified directly as base64 data or as a reference via a URL.

        - `beta_managed_agents_document_block: object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `beta_managed_agents_search_result_block: object`

          A block containing a web search result.

      - `is_error: optional boolean`

        Whether the tool execution resulted in an error.

    - `beta_managed_agents_agent_tool_use_event: object`

      Event emitted when the agent invokes a built-in agent tool.

      - `id: string`

        Unique identifier for this event.

      - `input: map[unknown]`

        Input parameters for the tool call.

      - `name: string`

        Name of the agent tool being used.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: "agent.tool_use"`

      - `evaluated_permission: optional "allow" or "ask" or "deny"`

        AgentEvaluatedPermission enum

        - `"allow"`

        - `"ask"`

        - `"deny"`

      - `session_thread_id: optional string`

        When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

    - `beta_managed_agents_agent_tool_result_event: object`

      Event representing the result of an agent tool execution.

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `tool_use_id: string`

        The id of the `agent.tool_use` event this result corresponds to.

      - `type: "agent.tool_result"`

      - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

        The result content returned by the tool.

        - `beta_managed_agents_text_block: object`

          Regular text content.

        - `beta_managed_agents_image_block: object`

          Image content specified directly as base64 data or as a reference via a URL.

        - `beta_managed_agents_document_block: object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `beta_managed_agents_search_result_block: object`

          A block containing a web search result.

      - `is_error: optional boolean`

        Whether the tool execution resulted in an error.

    - `beta_managed_agents_agent_thread_message_received_event: object`

      Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

      - `id: string`

        Unique identifier for this event.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

        Message content blocks.

        - `beta_managed_agents_text_block: object`

          Regular text content.

        - `beta_managed_agents_image_block: object`

          Image content specified directly as base64 data or as a reference via a URL.

        - `beta_managed_agents_document_block: object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `beta_managed_agents_redacted_block: object`

          Placeholder for content withheld by Anthropic model policy.

      - `from_session_thread_id: string`

        Public `sthr_` ID of the thread that sent the message.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: "agent.thread_message_received"`

      - `from_agent_name: optional string`

        Name of the callable agent this message came from. Absent when received from the primary agent.

    - `beta_managed_agents_agent_thread_message_sent_event: object`

      Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

      - `id: string`

        Unique identifier for this event.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

        Message content blocks.

        - `beta_managed_agents_text_block: object`

          Regular text content.

        - `beta_managed_agents_image_block: object`

          Image content specified directly as base64 data or as a reference via a URL.

        - `beta_managed_agents_document_block: object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `beta_managed_agents_redacted_block: object`

          Placeholder for content withheld by Anthropic model policy.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `to_session_thread_id: string`

        Public `sthr_` ID of the thread the message was sent to.

      - `type: "agent.thread_message_sent"`

      - `to_agent_name: optional string`

        Name of the callable agent this message was sent to. Absent when sent to the primary agent.

    - `beta_managed_agents_agent_thread_context_compacted_event: object`

      Indicates that context compaction (summarization) occurred during the session.

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: "agent.thread_context_compacted"`

    - `beta_managed_agents_session_error_event: object`

      An error event indicating a problem occurred during session execution.

      - `id: string`

        Unique identifier for this event.

      - `error: BetaManagedAgentsUnknownError or BetaManagedAgentsModelOverloadedError or BetaManagedAgentsModelRateLimitedError or 5 more`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `beta_managed_agents_unknown_error: object`

          An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

          - `message: string`

            Human-readable error description.

          - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

            What the client should do next in response to this error.

            - `beta_managed_agents_retry_status_retrying: object`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

              - `type: "retrying"`

            - `beta_managed_agents_retry_status_exhausted: object`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

              - `type: "exhausted"`

            - `beta_managed_agents_retry_status_terminal: object`

              The session encountered a terminal error and will transition to `terminated` state.

              - `type: "terminal"`

          - `type: "unknown_error"`

        - `beta_managed_agents_model_overloaded_error: object`

          The model is currently overloaded. Emitted after automatic retries are exhausted.

          - `message: string`

            Human-readable error description.

          - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

            What the client should do next in response to this error.

            - `beta_managed_agents_retry_status_retrying: object`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `beta_managed_agents_retry_status_exhausted: object`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `beta_managed_agents_retry_status_terminal: object`

              The session encountered a terminal error and will transition to `terminated` state.

          - `type: "model_overloaded_error"`

        - `beta_managed_agents_model_rate_limited_error: object`

          The model request was rate-limited.

          - `message: string`

            Human-readable error description.

          - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

            What the client should do next in response to this error.

            - `beta_managed_agents_retry_status_retrying: object`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `beta_managed_agents_retry_status_exhausted: object`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `beta_managed_agents_retry_status_terminal: object`

              The session encountered a terminal error and will transition to `terminated` state.

          - `type: "model_rate_limited_error"`

        - `beta_managed_agents_model_request_failed_error: object`

          A model request failed for a reason other than overload or rate-limiting.

          - `message: string`

            Human-readable error description.

          - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

            What the client should do next in response to this error.

            - `beta_managed_agents_retry_status_retrying: object`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `beta_managed_agents_retry_status_exhausted: object`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `beta_managed_agents_retry_status_terminal: object`

              The session encountered a terminal error and will transition to `terminated` state.

          - `type: "model_request_failed_error"`

        - `beta_managed_agents_mcp_connection_failed_error: object`

          Failed to connect to an MCP server.

          - `mcp_server_name: string`

            Name of the MCP server that failed to connect.

          - `message: string`

            Human-readable error description.

          - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

            What the client should do next in response to this error.

            - `beta_managed_agents_retry_status_retrying: object`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `beta_managed_agents_retry_status_exhausted: object`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `beta_managed_agents_retry_status_terminal: object`

              The session encountered a terminal error and will transition to `terminated` state.

          - `type: "mcp_connection_failed_error"`

        - `beta_managed_agents_mcp_authentication_failed_error: object`

          Authentication to an MCP server failed.

          - `mcp_server_name: string`

            Name of the MCP server that failed authentication.

          - `message: string`

            Human-readable error description.

          - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

            What the client should do next in response to this error.

            - `beta_managed_agents_retry_status_retrying: object`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `beta_managed_agents_retry_status_exhausted: object`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `beta_managed_agents_retry_status_terminal: object`

              The session encountered a terminal error and will transition to `terminated` state.

          - `type: "mcp_authentication_failed_error"`

        - `beta_managed_agents_billing_error: object`

          The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

          - `message: string`

            Human-readable error description.

          - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

            What the client should do next in response to this error.

            - `beta_managed_agents_retry_status_retrying: object`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `beta_managed_agents_retry_status_exhausted: object`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `beta_managed_agents_retry_status_terminal: object`

              The session encountered a terminal error and will transition to `terminated` state.

          - `type: "billing_error"`

        - `beta_managed_agents_credential_host_unreachable_error: object`

          An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

          - `credential_id: string`

            ID of the affected credential.

          - `message: string`

            Human-readable error description.

          - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

            What the client should do next in response to this error.

            - `beta_managed_agents_retry_status_retrying: object`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `beta_managed_agents_retry_status_exhausted: object`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `beta_managed_agents_retry_status_terminal: object`

              The session encountered a terminal error and will transition to `terminated` state.

          - `type: "credential_host_unreachable_error"`

          - `vault_id: string`

            ID of the vault containing the affected credential.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: "session.error"`

    - `beta_managed_agents_session_status_rescheduled_event: object`

      Indicates the session is recovering from an error state and is rescheduled for execution.

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: "session.status_rescheduled"`

    - `beta_managed_agents_session_status_running_event: object`

      Indicates the session is actively running and the agent is working.

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: "session.status_running"`

    - `beta_managed_agents_session_status_idle_event: object`

      Indicates the agent has paused and is awaiting user input.

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted or BetaManagedAgentsSessionBudgetReached`

        The agent completed its turn naturally and is ready for the next user message.

        - `beta_managed_agents_session_end_turn: object`

          The agent completed its turn naturally and is ready for the next user message.

          - `type: "end_turn"`

        - `beta_managed_agents_session_requires_action: object`

          The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

          - `event_ids: array of string`

            The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

          - `type: "requires_action"`

        - `beta_managed_agents_session_retries_exhausted: object`

          The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

          - `type: "retries_exhausted"`

        - `beta_managed_agents_session_budget_reached: object`

          The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

          - `type: "budget_reached"`

      - `type: "session.status_idle"`

    - `beta_managed_agents_session_status_terminated_event: object`

      Indicates the session has terminated, either due to an error or completion.

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: "session.status_terminated"`

    - `beta_managed_agents_session_thread_created_event: object`

      Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

      - `id: string`

        Unique identifier for this event.

      - `agent_name: string`

        Name of the callable agent the thread runs.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: string`

        Public `sthr_` ID of the newly created thread.

      - `type: "session.thread_created"`

    - `beta_managed_agents_span_outcome_evaluation_start_event: object`

      Emitted when an outcome evaluation cycle begins.

      - `id: string`

        Unique identifier for this event.

      - `iteration: number`

        0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

        format: int32

      - `outcome_id: string`

        The `outc_` ID of the outcome being evaluated.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: "span.outcome_evaluation_start"`

    - `beta_managed_agents_span_outcome_evaluation_end_event: object`

      Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

      - `id: string`

        Unique identifier for this event.

      - `explanation: string`

        Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

      - `iteration: number`

        0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

        format: int32

      - `outcome_evaluation_start_id: string`

        The id of the corresponding `span.outcome_evaluation_start` event.

      - `outcome_id: string`

        The `outc_` ID of the outcome being evaluated.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `result: string`

        Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

      - `type: "span.outcome_evaluation_end"`

      - `usage: object`

        Token usage for a single model request.

        - `cache_creation_input_tokens: number`

          Tokens used to create prompt cache in this request.

          format: int32

        - `cache_read_input_tokens: number`

          Tokens read from prompt cache in this request.

          format: int32

        - `input_tokens: number`

          Input tokens consumed by this request.

          format: int32

        - `output_tokens: number`

          Output tokens generated by this request.

          format: int32

        - `speed: optional "standard" or "fast"`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

    - `beta_managed_agents_span_model_request_start_event: object`

      Emitted when a model request is initiated by the agent.

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: "span.model_request_start"`

    - `beta_managed_agents_span_model_request_end_event: object`

      Emitted when a model request completes.

      - `id: string`

        Unique identifier for this event.

      - `is_error: boolean`

        Whether the model request resulted in an error.

      - `model_request_start_id: string`

        The id of the corresponding `span.model_request_start` event.

      - `model_usage: object`

        Token usage for a single model request.

        - `cache_creation_input_tokens: number`

          Tokens used to create prompt cache in this request.

          format: int32

        - `cache_read_input_tokens: number`

          Tokens read from prompt cache in this request.

          format: int32

        - `input_tokens: number`

          Input tokens consumed by this request.

          format: int32

        - `output_tokens: number`

          Output tokens generated by this request.

          format: int32

        - `speed: optional "standard" or "fast"`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: "span.model_request_end"`

    - `beta_managed_agents_span_outcome_evaluation_ongoing_event: object`

      Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

      - `id: string`

        Unique identifier for this event.

      - `iteration: number`

        0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

        format: int32

      - `outcome_id: string`

        The `outc_` ID of the outcome being evaluated.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: "span.outcome_evaluation_ongoing"`

    - `beta_managed_agents_user_define_outcome_event: object`

      Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

      - `id: string`

        Unique identifier for this event.

      - `description: string`

        What the agent should produce. Copied from the input event.

      - `max_iterations: number`

        Evaluate-then-revise cycles before giving up. Default 3, max 20.

        format: int32

      - `outcome_id: string`

        Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `beta_managed_agents_file_rubric: object`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: string`

            ID of the rubric file.

          - `type: "file"`

        - `beta_managed_agents_text_rubric: object`

          Rubric content provided inline as text.

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: "text"`

      - `type: "user.define_outcome"`

    - `beta_managed_agents_session_deleted_event: object`

      Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: "session.deleted"`

    - `beta_managed_agents_session_thread_status_running_event: object`

      A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

      - `id: string`

        Unique identifier for this event.

      - `agent_name: string`

        Name of the agent the thread runs.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: string`

        Public sthr_ ID of the thread that started running.

      - `type: "session.thread_status_running"`

    - `beta_managed_agents_session_thread_status_idle_event: object`

      A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

      - `id: string`

        Unique identifier for this event.

      - `agent_name: string`

        Name of the agent the thread runs.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: string`

        Public sthr_ ID of the thread that went idle.

      - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted or BetaManagedAgentsSessionBudgetReached`

        The agent completed its turn naturally and is ready for the next user message.

        - `beta_managed_agents_session_end_turn: object`

          The agent completed its turn naturally and is ready for the next user message.

        - `beta_managed_agents_session_requires_action: object`

          The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `beta_managed_agents_session_retries_exhausted: object`

          The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `beta_managed_agents_session_budget_reached: object`

          The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

      - `type: "session.thread_status_idle"`

    - `beta_managed_agents_session_thread_status_terminated_event: object`

      A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

      - `id: string`

        Unique identifier for this event.

      - `agent_name: string`

        Name of the agent the thread runs.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: string`

        Public sthr_ ID of the thread that terminated.

      - `type: "session.thread_status_terminated"`

    - `beta_managed_agents_user_tool_result_event: object`

      Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

      - `id: string`

        Unique identifier for this event.

      - `tool_use_id: string`

        The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: "user.tool_result"`

      - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

        The result content returned by the tool.

        - `beta_managed_agents_text_block: object`

          Regular text content.

        - `beta_managed_agents_image_block: object`

          Image content specified directly as base64 data or as a reference via a URL.

        - `beta_managed_agents_document_block: object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `beta_managed_agents_search_result_block: object`

          A block containing a web search result.

      - `is_error: optional boolean`

        Whether the tool execution resulted in an error.

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: optional string`

        Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

    - `beta_managed_agents_session_thread_status_rescheduled_event: object`

      A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

      - `id: string`

        Unique identifier for this event.

      - `agent_name: string`

        Name of the agent the thread runs.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: string`

        Public sthr_ ID of the thread that is retrying.

      - `type: "session.thread_status_rescheduled"`

    - `beta_managed_agents_session_updated_event: object`

      Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: "session.updated"`

      - `agent: optional object`

        Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

        - `id: string`

        - `description: string`

        - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

          - `name: string`

          - `type: "url"`

          - `url: string`

        - `model: object`

          Model identifier and configuration.

          - `id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

          - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

            How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

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

            Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

            - `"standard"`

            - `"fast"`

        - `multiagent: object`

          Resolved coordinator topology with full agent definitions for each roster member.

          - `agents: array of BetaManagedAgentsSessionThreadAgent or BetaManagedAgentsAdvisor`

            Full `agent` definitions the coordinator may spawn as session threads.

            - `beta_managed_agents_session_thread_agent: object`

              Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

              - `id: string`

              - `description: string`

              - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

                - `name: string`

                - `type: "url"`

                - `url: string`

              - `model: object`

                Model identifier and configuration.

                - `id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string`

                  The model that will power your agent.

                  See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

                - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

                  How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

                - `inference_geo: optional string`

                  Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

                - `speed: optional "standard" or "fast"`

                  Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

              - `name: string`

              - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

                - `beta_managed_agents_anthropic_skill: object`

                  A resolved Anthropic-managed skill.

                  - `skill_id: string`

                  - `type: "anthropic"`

                  - `version: string`

                - `beta_managed_agents_custom_skill: object`

                  A resolved user-created custom skill.

                  - `skill_id: string`

                  - `type: "custom"`

                  - `version: string`

              - `system: string`

              - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

                - `beta_managed_agents_agent_toolset20260401: object`

                  - `configs: array of BetaManagedAgentsAgentToolConfig`

                    - `beta_managed_agents_bash_tool_config: object`

                      Configuration for the bash tool.

                      - `enabled: boolean`

                      - `name: "bash"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                        Permission policy for tool execution.

                        - `beta_managed_agents_always_allow_policy: object`

                          Tool calls are automatically approved without user confirmation.

                          - `type: "always_allow"`

                        - `beta_managed_agents_always_ask_policy: object`

                          Tool calls require user confirmation before execution.

                          - `type: "always_ask"`

                      - `type: "bash"`

                    - `beta_managed_agents_edit_tool_config: object`

                      Configuration for the edit tool.

                      - `enabled: boolean`

                      - `name: "edit"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                        Permission policy for tool execution.

                        - `beta_managed_agents_always_allow_policy: object`

                          Tool calls are automatically approved without user confirmation.

                        - `beta_managed_agents_always_ask_policy: object`

                          Tool calls require user confirmation before execution.

                      - `type: "edit"`

                    - `beta_managed_agents_read_tool_config: object`

                      Configuration for the read tool.

                      - `enabled: boolean`

                      - `name: "read"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                        Permission policy for tool execution.

                        - `beta_managed_agents_always_allow_policy: object`

                          Tool calls are automatically approved without user confirmation.

                        - `beta_managed_agents_always_ask_policy: object`

                          Tool calls require user confirmation before execution.

                      - `type: "read"`

                    - `beta_managed_agents_write_tool_config: object`

                      Configuration for the write tool.

                      - `enabled: boolean`

                      - `name: "write"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                        Permission policy for tool execution.

                        - `beta_managed_agents_always_allow_policy: object`

                          Tool calls are automatically approved without user confirmation.

                        - `beta_managed_agents_always_ask_policy: object`

                          Tool calls require user confirmation before execution.

                      - `type: "write"`

                    - `beta_managed_agents_glob_tool_config: object`

                      Configuration for the glob tool.

                      - `enabled: boolean`

                      - `name: "glob"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                        Permission policy for tool execution.

                        - `beta_managed_agents_always_allow_policy: object`

                          Tool calls are automatically approved without user confirmation.

                        - `beta_managed_agents_always_ask_policy: object`

                          Tool calls require user confirmation before execution.

                      - `type: "glob"`

                    - `beta_managed_agents_grep_tool_config: object`

                      Configuration for the grep tool.

                      - `enabled: boolean`

                      - `name: "grep"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                        Permission policy for tool execution.

                        - `beta_managed_agents_always_allow_policy: object`

                          Tool calls are automatically approved without user confirmation.

                        - `beta_managed_agents_always_ask_policy: object`

                          Tool calls require user confirmation before execution.

                      - `type: "grep"`

                    - `beta_managed_agents_web_fetch_tool_config: object`

                      Configuration for the web_fetch tool.

                      - `enabled: boolean`

                      - `name: "web_fetch"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                        Permission policy for tool execution.

                        - `beta_managed_agents_always_allow_policy: object`

                          Tool calls are automatically approved without user confirmation.

                        - `beta_managed_agents_always_ask_policy: object`

                          Tool calls require user confirmation before execution.

                      - `type: "web_fetch"`

                      - `allowed_domains: optional array of string`

                      - `blocked_domains: optional array of string`

                      - `max_content_tokens: optional number`

                        format: int32

                    - `beta_managed_agents_web_search_tool_config: object`

                      Configuration for the web_search tool.

                      - `enabled: boolean`

                      - `name: "web_search"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                        Permission policy for tool execution.

                        - `beta_managed_agents_always_allow_policy: object`

                          Tool calls are automatically approved without user confirmation.

                        - `beta_managed_agents_always_ask_policy: object`

                          Tool calls require user confirmation before execution.

                      - `type: "web_search"`

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

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                  - `type: "agent_toolset_20260401"`

                - `beta_managed_agents_mcp_toolset: object`

                  - `configs: array of BetaManagedAgentsMCPToolConfig`

                    - `enabled: boolean`

                    - `name: string`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                  - `default_config: object`

                    Resolved default configuration for all tools from an MCP server.

                    - `enabled: boolean`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                  - `mcp_server_name: string`

                  - `type: "mcp_toolset"`

                - `beta_managed_agents_custom_tool: object`

                  A custom tool as returned in API responses.

                  - `description: string`

                  - `input_schema: object`

                    JSON Schema for custom tool input parameters.

                    - `type: "object"`

                    - `properties: optional map[unknown]`

                    - `required: optional array of string`

                  - `name: string`

                  - `type: "custom"`

              - `type: "agent"`

              - `version: number`

                format: int32

            - `beta_managed_agents_advisor: object`

              Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

              - `model: string`

                The advisor model id.

              - `type: "advisor"`

          - `type: "coordinator"`

        - `name: string`

        - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

          - `beta_managed_agents_anthropic_skill: object`

            A resolved Anthropic-managed skill.

          - `beta_managed_agents_custom_skill: object`

            A resolved user-created custom skill.

        - `system: string`

        - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

          - `beta_managed_agents_agent_toolset20260401: object`

          - `beta_managed_agents_mcp_toolset: object`

          - `beta_managed_agents_custom_tool: object`

            A custom tool as returned in API responses.

        - `type: "agent"`

        - `version: number`

          format: int32

      - `budget: optional object`

        A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

        - `max_list_cost: object`

          A monetary amount in a specific currency.

          - `amount: string`

            Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

          - `currency: "USD"`

            Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

        - `type: "limit"`

      - `metadata: optional map[string]`

        The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

      - `title: optional string`

        The session's new title. Present only when the update changed it.

    - `beta_managed_agents_system_message_event: object`

      A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

      - `id: string`

        Unique identifier for this event.

      - `content: array of BetaManagedAgentsSystemContentBlock`

        System content blocks. Text-only.

        - `text: string`

          The text content.

          minLength: 1

        - `type: "text"`

      - `type: "system.message"`

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

        format: date-time

    - `beta_managed_agents_session_usage_event: object`

      Periodic snapshot of the session's cumulative usage and tracked list cost.

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: "session.usage"`

      - `usage: object`

        Point-in-time snapshot of a session's cumulative usage.

        - `active_seconds: optional number`

          Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

          format: double

        - `cache_creation: optional object`

          Prompt-cache creation token usage broken down by cache lifetime.

          - `ephemeral_1h_input_tokens: optional number`

            Tokens used to create 1-hour ephemeral cache entries.

            format: int32

          - `ephemeral_5m_input_tokens: optional number`

            Tokens used to create 5-minute ephemeral cache entries.

            format: int32

        - `cache_read_input_tokens: optional number`

          Total tokens read from prompt cache.

          format: int32

        - `input_tokens: optional number`

          Total input tokens consumed across all turns.

          format: int32

        - `list_cost: optional object`

          A monetary amount in a specific currency.

          - `amount: string`

            Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

          - `currency: "USD"`

            Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

        - `output_tokens: optional number`

          Total output tokens generated across all turns.

          format: int32

        - `server_tool_use: optional object`

          Cumulative count of server-executed tool invocations, broken down by tool.

          - `web_fetch_requests: optional number`

            Number of server-executed web fetch requests.

            format: int32

          - `web_search_requests: optional number`

            Number of server-executed web search requests.

            format: int32

      - `budget: optional object`

        A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

        - `max_list_cost: object`

          A monetary amount in a specific currency.

        - `type: "limit"`

  - `next_page: optional string`

    Opaque cursor for the next page. Null when no more results.

#### Example

```bash
ant beta:sessions:events list \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message",
      "processed_at": "2026-03-15T10:00:00Z"
    },
    {
      "id": "sevt_011CZkZHPq1jCdq5lbRTjiVnz",
      "content": [
        {
          "text": "Let me look up order #1234 for you.",
          "type": "text"
        }
      ],
      "processed_at": "2026-03-15T10:00:00Z",
      "type": "agent.message"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

### Send Events

`$ ant beta:sessions:events send`

**POST** `/v1/sessions/{session_id}/events`

Send Events

#### Parameters

- `--session-id: string`

  Path param: Path parameter session_id

- `--event: array of BetaManagedAgentsEventParams`

  Body param: Events to send to the `session`.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_managed_agents_send_session_events: object`

  Events that were successfully sent to the session.

  - `data: optional array of BetaManagedAgentsUserMessageEvent or BetaManagedAgentsUserInterruptEvent or BetaManagedAgentsUserToolConfirmationEvent or 4 more`

    Sent events

    - `beta_managed_agents_user_message_event: object`

      A user message event in the session conversation.

      - `id: string`

        Unique identifier for this event.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

        Array of content blocks comprising the user message.

        - `beta_managed_agents_text_block: object`

          Regular text content.

          - `text: string`

            The text content.

            minLength: 1

          - `type: "text"`

        - `beta_managed_agents_image_block: object`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `beta_managed_agents_base64_image_source: object`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

                minLength: 1

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `type: "base64"`

            - `beta_managed_agents_url_image_source: object`

              Image referenced by URL.

              - `type: "url"`

              - `url: string`

                URL of the image to fetch.

                minLength: 1

            - `beta_managed_agents_file_image_source: object`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

                minLength: 1

              - `type: "file"`

          - `type: "image"`

        - `beta_managed_agents_document_block: object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `beta_managed_agents_base64_document_source: object`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

                minLength: 1

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `type: "base64"`

            - `beta_managed_agents_plain_text_document_source: object`

              Plain text document content.

              - `data: string`

                The plain text content.

                minLength: 1

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

              - `type: "text"`

            - `beta_managed_agents_url_document_source: object`

              Document referenced by URL.

              - `type: "url"`

              - `url: string`

                URL of the document to fetch.

                minLength: 1

            - `beta_managed_agents_file_document_source: object`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

                minLength: 1

              - `type: "file"`

          - `type: "document"`

          - `context: optional string`

            Additional context about the document for the model.

          - `title: optional string`

            The title of the document.

        - `beta_managed_agents_redacted_block: object`

          Placeholder for content withheld by Anthropic model policy.

          - `type: "redacted"`

      - `type: "user.message"`

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

        format: date-time

    - `beta_managed_agents_user_interrupt_event: object`

      An interrupt event that pauses agent execution and returns control to the user.

      - `id: string`

        Unique identifier for this event.

      - `type: "user.interrupt"`

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: optional string`

        If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

    - `beta_managed_agents_user_tool_confirmation_event: object`

      A tool confirmation event that approves or denies a pending tool execution.

      - `id: string`

        Unique identifier for this event.

      - `result: "allow" or "deny"`

        UserToolConfirmationResult enum

        - `"allow"`

        - `"deny"`

      - `tool_use_id: string`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: "user.tool_confirmation"`

      - `deny_message: optional string`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

        maxLength: 10000

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: optional string`

        When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

    - `beta_managed_agents_user_custom_tool_result_event: object`

      Event sent by the client providing the result of a custom tool execution.

      - `id: string`

        Unique identifier for this event.

      - `custom_tool_use_id: string`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: "user.custom_tool_result"`

      - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

        The result content returned by the tool.

        - `beta_managed_agents_text_block: object`

          Regular text content.

        - `beta_managed_agents_image_block: object`

          Image content specified directly as base64 data or as a reference via a URL.

        - `beta_managed_agents_document_block: object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `beta_managed_agents_search_result_block: object`

          A block containing a web search result.

          - `citations: object`

            Citation settings for a search result.

            - `enabled: boolean`

              Whether citations are enabled for this search result.

          - `content: array of BetaManagedAgentsSearchResultContent`

            Array of text content blocks from the search result.

            - `text: string`

              The text content.

              minLength: 1

            - `type: "text"`

          - `source: string`

            The URL source of the search result.

            minLength: 1

          - `title: string`

            The title of the search result.

            minLength: 1

          - `type: "search_result"`

      - `is_error: optional boolean`

        Whether the tool execution resulted in an error.

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: optional string`

        Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

    - `beta_managed_agents_user_define_outcome_event: object`

      Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

      - `id: string`

        Unique identifier for this event.

      - `description: string`

        What the agent should produce. Copied from the input event.

      - `max_iterations: number`

        Evaluate-then-revise cycles before giving up. Default 3, max 20.

        format: int32

      - `outcome_id: string`

        Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `beta_managed_agents_file_rubric: object`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: string`

            ID of the rubric file.

          - `type: "file"`

        - `beta_managed_agents_text_rubric: object`

          Rubric content provided inline as text.

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: "text"`

      - `type: "user.define_outcome"`

    - `beta_managed_agents_user_tool_result_event: object`

      Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

      - `id: string`

        Unique identifier for this event.

      - `tool_use_id: string`

        The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: "user.tool_result"`

      - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

        The result content returned by the tool.

        - `beta_managed_agents_text_block: object`

          Regular text content.

        - `beta_managed_agents_image_block: object`

          Image content specified directly as base64 data or as a reference via a URL.

        - `beta_managed_agents_document_block: object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `beta_managed_agents_search_result_block: object`

          A block containing a web search result.

      - `is_error: optional boolean`

        Whether the tool execution resulted in an error.

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: optional string`

        Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

    - `beta_managed_agents_system_message_event: object`

      A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

      - `id: string`

        Unique identifier for this event.

      - `content: array of BetaManagedAgentsSystemContentBlock`

        System content blocks. Text-only.

        - `text: string`

          The text content.

          minLength: 1

        - `type: "text"`

      - `type: "system.message"`

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

        format: date-time

#### Example

```bash
ant beta:sessions:events send \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7 \
  --event '{content: [{text: '\''Where is my order #1234?'\'', type: text}], type: user.message}'
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message",
      "processed_at": "2026-03-15T10:00:00Z"
    }
  ]
}
```

### Stream Events

`$ ant beta:sessions:events stream`

**GET** `/v1/sessions/{session_id}/events/stream`

Stream Events

#### Parameters

- `--session-id: string`

  Path param: Path parameter session_id

- `--event-delta: optional array of BetaManagedAgentsDeltaType`

  Query param: When set, this connection also receives streaming deltas (`event_start`, `event_delta`) while an event is being produced, before the event itself arrives. Deltas are best-effort; when the final event is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no final event — its terminal `span.model_request_end` closes the preview. Accepts one or more event types to preview and may be repeated: `agent.message` streams `content_delta` fragments; `agent.thinking` is start-only — a signal that the agent has begun extended thinking, concluded by the `agent.thinking` event itself. Only previews of the requested event types are sent.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_managed_agents_stream_session_events: BetaManagedAgentsUserMessageEvent or BetaManagedAgentsUserInterruptEvent or BetaManagedAgentsUserToolConfirmationEvent or 34 more`

  Server-sent event in the session stream.

  - `beta_managed_agents_user_message_event: object`

    A user message event in the session conversation.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

      Array of content blocks comprising the user message.

      - `beta_managed_agents_text_block: object`

        Regular text content.

        - `text: string`

          The text content.

          minLength: 1

        - `type: "text"`

      - `beta_managed_agents_image_block: object`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `beta_managed_agents_base64_image_source: object`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

              minLength: 1

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

            - `type: "base64"`

          - `beta_managed_agents_url_image_source: object`

            Image referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the image to fetch.

              minLength: 1

          - `beta_managed_agents_file_image_source: object`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

            - `type: "file"`

        - `type: "image"`

      - `beta_managed_agents_document_block: object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `beta_managed_agents_base64_document_source: object`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

              minLength: 1

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

            - `type: "base64"`

          - `beta_managed_agents_plain_text_document_source: object`

            Plain text document content.

            - `data: string`

              The plain text content.

              minLength: 1

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

            - `type: "text"`

          - `beta_managed_agents_url_document_source: object`

            Document referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the document to fetch.

              minLength: 1

          - `beta_managed_agents_file_document_source: object`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

            - `type: "file"`

        - `type: "document"`

        - `context: optional string`

          Additional context about the document for the model.

        - `title: optional string`

          The title of the document.

      - `beta_managed_agents_redacted_block: object`

        Placeholder for content withheld by Anthropic model policy.

        - `type: "redacted"`

    - `type: "user.message"`

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

      format: date-time

  - `beta_managed_agents_user_interrupt_event: object`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: string`

      Unique identifier for this event.

    - `type: "user.interrupt"`

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: optional string`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `beta_managed_agents_user_tool_confirmation_event: object`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: string`

      Unique identifier for this event.

    - `result: "allow" or "deny"`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.tool_confirmation"`

    - `deny_message: optional string`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: optional string`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `beta_managed_agents_user_custom_tool_result_event: object`

    Event sent by the client providing the result of a custom tool execution.

    - `id: string`

      Unique identifier for this event.

    - `custom_tool_use_id: string`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.custom_tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `beta_managed_agents_text_block: object`

        Regular text content.

      - `beta_managed_agents_image_block: object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `beta_managed_agents_document_block: object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `beta_managed_agents_search_result_block: object`

        A block containing a web search result.

        - `citations: object`

          Citation settings for a search result.

          - `enabled: boolean`

            Whether citations are enabled for this search result.

        - `content: array of BetaManagedAgentsSearchResultContent`

          Array of text content blocks from the search result.

          - `text: string`

            The text content.

            minLength: 1

          - `type: "text"`

        - `source: string`

          The URL source of the search result.

          minLength: 1

        - `title: string`

          The title of the search result.

          minLength: 1

        - `type: "search_result"`

    - `is_error: optional boolean`

      Whether the tool execution resulted in an error.

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: optional string`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `beta_managed_agents_agent_custom_tool_use_event: object`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `name: string`

      Name of the custom tool being called.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.custom_tool_use"`

    - `session_thread_id: optional string`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `beta_managed_agents_agent_message_event: object`

    An agent response event in the session conversation.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsRedactedBlock`

      Array of text blocks comprising the agent response.

      - `beta_managed_agents_text_block: object`

        Regular text content.

      - `beta_managed_agents_redacted_block: object`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.message"`

  - `beta_managed_agents_agent_thinking_event: object`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.thinking"`

  - `beta_managed_agents_agent_mcp_tool_use_event: object`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `mcp_server_name: string`

      Name of the MCP server providing the tool.

    - `name: string`

      Name of the MCP tool being used.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.mcp_tool_use"`

    - `evaluated_permission: optional "allow" or "ask" or "deny"`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: optional string`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `beta_managed_agents_agent_mcp_tool_result_event: object`

    Event representing the result of an MCP tool execution.

    - `id: string`

      Unique identifier for this event.

    - `mcp_tool_use_id: string`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.mcp_tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `beta_managed_agents_text_block: object`

        Regular text content.

      - `beta_managed_agents_image_block: object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `beta_managed_agents_document_block: object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `beta_managed_agents_search_result_block: object`

        A block containing a web search result.

    - `is_error: optional boolean`

      Whether the tool execution resulted in an error.

  - `beta_managed_agents_agent_tool_use_event: object`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `name: string`

      Name of the agent tool being used.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.tool_use"`

    - `evaluated_permission: optional "allow" or "ask" or "deny"`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: optional string`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `beta_managed_agents_agent_tool_result_event: object`

    Event representing the result of an agent tool execution.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: "agent.tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `beta_managed_agents_text_block: object`

        Regular text content.

      - `beta_managed_agents_image_block: object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `beta_managed_agents_document_block: object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `beta_managed_agents_search_result_block: object`

        A block containing a web search result.

    - `is_error: optional boolean`

      Whether the tool execution resulted in an error.

  - `beta_managed_agents_agent_thread_message_received_event: object`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

      Message content blocks.

      - `beta_managed_agents_text_block: object`

        Regular text content.

      - `beta_managed_agents_image_block: object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `beta_managed_agents_document_block: object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `beta_managed_agents_redacted_block: object`

        Placeholder for content withheld by Anthropic model policy.

    - `from_session_thread_id: string`

      Public `sthr_` ID of the thread that sent the message.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.thread_message_received"`

    - `from_agent_name: optional string`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `beta_managed_agents_agent_thread_message_sent_event: object`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

      Message content blocks.

      - `beta_managed_agents_text_block: object`

        Regular text content.

      - `beta_managed_agents_image_block: object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `beta_managed_agents_document_block: object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `beta_managed_agents_redacted_block: object`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `to_session_thread_id: string`

      Public `sthr_` ID of the thread the message was sent to.

    - `type: "agent.thread_message_sent"`

    - `to_agent_name: optional string`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `beta_managed_agents_agent_thread_context_compacted_event: object`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.thread_context_compacted"`

  - `beta_managed_agents_session_error_event: object`

    An error event indicating a problem occurred during session execution.

    - `id: string`

      Unique identifier for this event.

    - `error: BetaManagedAgentsUnknownError or BetaManagedAgentsModelOverloadedError or BetaManagedAgentsModelRateLimitedError or 5 more`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `beta_managed_agents_unknown_error: object`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

          - `beta_managed_agents_retry_status_exhausted: object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

          - `beta_managed_agents_retry_status_terminal: object`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

        - `type: "unknown_error"`

      - `beta_managed_agents_model_overloaded_error: object`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `beta_managed_agents_retry_status_exhausted: object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `beta_managed_agents_retry_status_terminal: object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "model_overloaded_error"`

      - `beta_managed_agents_model_rate_limited_error: object`

        The model request was rate-limited.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `beta_managed_agents_retry_status_exhausted: object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `beta_managed_agents_retry_status_terminal: object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "model_rate_limited_error"`

      - `beta_managed_agents_model_request_failed_error: object`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `beta_managed_agents_retry_status_exhausted: object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `beta_managed_agents_retry_status_terminal: object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "model_request_failed_error"`

      - `beta_managed_agents_mcp_connection_failed_error: object`

        Failed to connect to an MCP server.

        - `mcp_server_name: string`

          Name of the MCP server that failed to connect.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `beta_managed_agents_retry_status_exhausted: object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `beta_managed_agents_retry_status_terminal: object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "mcp_connection_failed_error"`

      - `beta_managed_agents_mcp_authentication_failed_error: object`

        Authentication to an MCP server failed.

        - `mcp_server_name: string`

          Name of the MCP server that failed authentication.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `beta_managed_agents_retry_status_exhausted: object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `beta_managed_agents_retry_status_terminal: object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "mcp_authentication_failed_error"`

      - `beta_managed_agents_billing_error: object`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `beta_managed_agents_retry_status_exhausted: object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `beta_managed_agents_retry_status_terminal: object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "billing_error"`

      - `beta_managed_agents_credential_host_unreachable_error: object`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `credential_id: string`

          ID of the affected credential.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `beta_managed_agents_retry_status_exhausted: object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `beta_managed_agents_retry_status_terminal: object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "credential_host_unreachable_error"`

        - `vault_id: string`

          ID of the vault containing the affected credential.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.error"`

  - `beta_managed_agents_session_status_rescheduled_event: object`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.status_rescheduled"`

  - `beta_managed_agents_session_status_running_event: object`

    Indicates the session is actively running and the agent is working.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.status_running"`

  - `beta_managed_agents_session_status_idle_event: object`

    Indicates the agent has paused and is awaiting user input.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted or BetaManagedAgentsSessionBudgetReached`

      The agent completed its turn naturally and is ready for the next user message.

      - `beta_managed_agents_session_end_turn: object`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: "end_turn"`

      - `beta_managed_agents_session_requires_action: object`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: array of string`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: "requires_action"`

      - `beta_managed_agents_session_retries_exhausted: object`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `type: "retries_exhausted"`

      - `beta_managed_agents_session_budget_reached: object`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `type: "budget_reached"`

    - `type: "session.status_idle"`

  - `beta_managed_agents_session_status_terminated_event: object`

    Indicates the session has terminated, either due to an error or completion.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.status_terminated"`

  - `beta_managed_agents_session_thread_created_event: object`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the callable agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public `sthr_` ID of the newly created thread.

    - `type: "session.thread_created"`

  - `beta_managed_agents_span_outcome_evaluation_start_event: object`

    Emitted when an outcome evaluation cycle begins.

    - `id: string`

      Unique identifier for this event.

    - `iteration: number`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

      format: int32

    - `outcome_id: string`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "span.outcome_evaluation_start"`

  - `beta_managed_agents_span_outcome_evaluation_end_event: object`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `id: string`

      Unique identifier for this event.

    - `explanation: string`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `iteration: number`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `outcome_evaluation_start_id: string`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `outcome_id: string`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `result: string`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `type: "span.outcome_evaluation_end"`

    - `usage: object`

      Token usage for a single model request.

      - `cache_creation_input_tokens: number`

        Tokens used to create prompt cache in this request.

        format: int32

      - `cache_read_input_tokens: number`

        Tokens read from prompt cache in this request.

        format: int32

      - `input_tokens: number`

        Input tokens consumed by this request.

        format: int32

      - `output_tokens: number`

        Output tokens generated by this request.

        format: int32

      - `speed: optional "standard" or "fast"`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `beta_managed_agents_span_model_request_start_event: object`

    Emitted when a model request is initiated by the agent.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "span.model_request_start"`

  - `beta_managed_agents_span_model_request_end_event: object`

    Emitted when a model request completes.

    - `id: string`

      Unique identifier for this event.

    - `is_error: boolean`

      Whether the model request resulted in an error.

    - `model_request_start_id: string`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: object`

      Token usage for a single model request.

      - `cache_creation_input_tokens: number`

        Tokens used to create prompt cache in this request.

        format: int32

      - `cache_read_input_tokens: number`

        Tokens read from prompt cache in this request.

        format: int32

      - `input_tokens: number`

        Input tokens consumed by this request.

        format: int32

      - `output_tokens: number`

        Output tokens generated by this request.

        format: int32

      - `speed: optional "standard" or "fast"`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "span.model_request_end"`

  - `beta_managed_agents_span_outcome_evaluation_ongoing_event: object`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `id: string`

      Unique identifier for this event.

    - `iteration: number`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `outcome_id: string`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "span.outcome_evaluation_ongoing"`

  - `beta_managed_agents_user_define_outcome_event: object`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `id: string`

      Unique identifier for this event.

    - `description: string`

      What the agent should produce. Copied from the input event.

    - `max_iterations: number`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

      format: int32

    - `outcome_id: string`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

      Rubric for grading the quality of an outcome.

      - `beta_managed_agents_file_rubric: object`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: string`

          ID of the rubric file.

        - `type: "file"`

      - `beta_managed_agents_text_rubric: object`

        Rubric content provided inline as text.

        - `content: string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `type: "text"`

    - `type: "user.define_outcome"`

  - `beta_managed_agents_session_deleted_event: object`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.deleted"`

  - `beta_managed_agents_session_thread_status_running_event: object`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that started running.

    - `type: "session.thread_status_running"`

  - `beta_managed_agents_session_thread_status_idle_event: object`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that went idle.

    - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted or BetaManagedAgentsSessionBudgetReached`

      The agent completed its turn naturally and is ready for the next user message.

      - `beta_managed_agents_session_end_turn: object`

        The agent completed its turn naturally and is ready for the next user message.

      - `beta_managed_agents_session_requires_action: object`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `beta_managed_agents_session_retries_exhausted: object`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `beta_managed_agents_session_budget_reached: object`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

    - `type: "session.thread_status_idle"`

  - `beta_managed_agents_session_thread_status_terminated_event: object`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that terminated.

    - `type: "session.thread_status_terminated"`

  - `beta_managed_agents_user_tool_result_event: object`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `id: string`

      Unique identifier for this event.

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `beta_managed_agents_text_block: object`

        Regular text content.

      - `beta_managed_agents_image_block: object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `beta_managed_agents_document_block: object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `beta_managed_agents_search_result_block: object`

        A block containing a web search result.

    - `is_error: optional boolean`

      Whether the tool execution resulted in an error.

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: optional string`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `beta_managed_agents_session_thread_status_rescheduled_event: object`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that is retrying.

    - `type: "session.thread_status_rescheduled"`

  - `beta_managed_agents_session_updated_event: object`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.updated"`

    - `agent: optional object`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `id: string`

      - `description: string`

      - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

        - `name: string`

        - `type: "url"`

        - `url: string`

      - `model: object`

        Model identifier and configuration.

        - `id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

        - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

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

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

      - `multiagent: object`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `agents: array of BetaManagedAgentsSessionThreadAgent or BetaManagedAgentsAdvisor`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `beta_managed_agents_session_thread_agent: object`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `id: string`

            - `description: string`

            - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

              - `name: string`

              - `type: "url"`

              - `url: string`

            - `model: object`

              Model identifier and configuration.

              - `id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string`

                The model that will power your agent.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

              - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

                How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

              - `inference_geo: optional string`

                Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

              - `speed: optional "standard" or "fast"`

                Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

            - `name: string`

            - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

              - `beta_managed_agents_anthropic_skill: object`

                A resolved Anthropic-managed skill.

                - `skill_id: string`

                - `type: "anthropic"`

                - `version: string`

              - `beta_managed_agents_custom_skill: object`

                A resolved user-created custom skill.

                - `skill_id: string`

                - `type: "custom"`

                - `version: string`

            - `system: string`

            - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

              - `beta_managed_agents_agent_toolset20260401: object`

                - `configs: array of BetaManagedAgentsAgentToolConfig`

                  - `beta_managed_agents_bash_tool_config: object`

                    Configuration for the bash tool.

                    - `enabled: boolean`

                    - `name: "bash"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                        - `type: "always_allow"`

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                        - `type: "always_ask"`

                    - `type: "bash"`

                  - `beta_managed_agents_edit_tool_config: object`

                    Configuration for the edit tool.

                    - `enabled: boolean`

                    - `name: "edit"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                    - `type: "edit"`

                  - `beta_managed_agents_read_tool_config: object`

                    Configuration for the read tool.

                    - `enabled: boolean`

                    - `name: "read"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                    - `type: "read"`

                  - `beta_managed_agents_write_tool_config: object`

                    Configuration for the write tool.

                    - `enabled: boolean`

                    - `name: "write"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                    - `type: "write"`

                  - `beta_managed_agents_glob_tool_config: object`

                    Configuration for the glob tool.

                    - `enabled: boolean`

                    - `name: "glob"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                    - `type: "glob"`

                  - `beta_managed_agents_grep_tool_config: object`

                    Configuration for the grep tool.

                    - `enabled: boolean`

                    - `name: "grep"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                    - `type: "grep"`

                  - `beta_managed_agents_web_fetch_tool_config: object`

                    Configuration for the web_fetch tool.

                    - `enabled: boolean`

                    - `name: "web_fetch"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                    - `type: "web_fetch"`

                    - `allowed_domains: optional array of string`

                    - `blocked_domains: optional array of string`

                    - `max_content_tokens: optional number`

                      format: int32

                  - `beta_managed_agents_web_search_tool_config: object`

                    Configuration for the web_search tool.

                    - `enabled: boolean`

                    - `name: "web_search"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                    - `type: "web_search"`

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

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                - `type: "agent_toolset_20260401"`

              - `beta_managed_agents_mcp_toolset: object`

                - `configs: array of BetaManagedAgentsMCPToolConfig`

                  - `enabled: boolean`

                  - `name: string`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                - `default_config: object`

                  Resolved default configuration for all tools from an MCP server.

                  - `enabled: boolean`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                - `mcp_server_name: string`

                - `type: "mcp_toolset"`

              - `beta_managed_agents_custom_tool: object`

                A custom tool as returned in API responses.

                - `description: string`

                - `input_schema: object`

                  JSON Schema for custom tool input parameters.

                  - `type: "object"`

                  - `properties: optional map[unknown]`

                  - `required: optional array of string`

                - `name: string`

                - `type: "custom"`

            - `type: "agent"`

            - `version: number`

              format: int32

          - `beta_managed_agents_advisor: object`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `model: string`

              The advisor model id.

            - `type: "advisor"`

        - `type: "coordinator"`

      - `name: string`

      - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

        - `beta_managed_agents_anthropic_skill: object`

          A resolved Anthropic-managed skill.

        - `beta_managed_agents_custom_skill: object`

          A resolved user-created custom skill.

      - `system: string`

      - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

        - `beta_managed_agents_agent_toolset20260401: object`

        - `beta_managed_agents_mcp_toolset: object`

        - `beta_managed_agents_custom_tool: object`

          A custom tool as returned in API responses.

      - `type: "agent"`

      - `version: number`

        format: int32

    - `budget: optional object`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `max_list_cost: object`

        A monetary amount in a specific currency.

        - `amount: string`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `currency: "USD"`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `type: "limit"`

    - `metadata: optional map[string]`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title: optional string`

      The session's new title. Present only when the update changed it.

  - `beta_managed_agents_start_event: object`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `event: BetaManagedAgentsAgentMessagePreview or BetaManagedAgentsAgentThinkingPreview`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

      - `beta_managed_agents_agent_message_preview: object`

        - `id: string`

          The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

        - `type: "agent.message"`

      - `beta_managed_agents_agent_thinking_preview: object`

        - `id: string`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

        - `type: "agent.thinking"`

    - `type: "event_start"`

  - `beta_managed_agents_delta_event: object`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `delta: object`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `content: object`

        Regular text content.

        - `text: string`

          The text content.

          minLength: 1

        - `type: "text"`

      - `type: "content_delta"`

      - `index: optional number`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

        format: uint32

    - `event_id: string`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

    - `type: "event_delta"`

  - `beta_managed_agents_system_message_event: object`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsSystemContentBlock`

      System content blocks. Text-only.

      - `text: string`

        The text content.

        minLength: 1

      - `type: "text"`

    - `type: "system.message"`

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

      format: date-time

  - `beta_managed_agents_session_usage_event: object`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.usage"`

    - `usage: object`

      Point-in-time snapshot of a session's cumulative usage.

      - `active_seconds: optional number`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `cache_creation: optional object`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `ephemeral_1h_input_tokens: optional number`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `ephemeral_5m_input_tokens: optional number`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `cache_read_input_tokens: optional number`

        Total tokens read from prompt cache.

        format: int32

      - `input_tokens: optional number`

        Total input tokens consumed across all turns.

        format: int32

      - `list_cost: optional object`

        A monetary amount in a specific currency.

        - `amount: string`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `currency: "USD"`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `output_tokens: optional number`

        Total output tokens generated across all turns.

        format: int32

      - `server_tool_use: optional object`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `web_fetch_requests: optional number`

          Number of server-executed web fetch requests.

          format: int32

        - `web_search_requests: optional number`

          Number of server-executed web search requests.

          format: int32

    - `budget: optional object`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `max_list_cost: object`

        A monetary amount in a specific currency.

      - `type: "limit"`

- `beta_managed_agents_stream_session_events: BetaManagedAgentsUserMessageEvent or BetaManagedAgentsUserInterruptEvent or BetaManagedAgentsUserToolConfirmationEvent or 34 more`

  Server-sent event in the session stream.

  - `beta_managed_agents_user_message_event: object`

    A user message event in the session conversation.

  - `beta_managed_agents_user_interrupt_event: object`

    An interrupt event that pauses agent execution and returns control to the user.

  - `beta_managed_agents_user_tool_confirmation_event: object`

    A tool confirmation event that approves or denies a pending tool execution.

  - `beta_managed_agents_user_custom_tool_result_event: object`

    Event sent by the client providing the result of a custom tool execution.

  - `beta_managed_agents_agent_custom_tool_use_event: object`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

  - `beta_managed_agents_agent_message_event: object`

    An agent response event in the session conversation.

  - `beta_managed_agents_agent_thinking_event: object`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

  - `beta_managed_agents_agent_mcp_tool_use_event: object`

    Event emitted when the agent invokes a tool provided by an MCP server.

  - `beta_managed_agents_agent_mcp_tool_result_event: object`

    Event representing the result of an MCP tool execution.

  - `beta_managed_agents_agent_tool_use_event: object`

    Event emitted when the agent invokes a built-in agent tool.

  - `beta_managed_agents_agent_tool_result_event: object`

    Event representing the result of an agent tool execution.

  - `beta_managed_agents_agent_thread_message_received_event: object`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

  - `beta_managed_agents_agent_thread_message_sent_event: object`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

  - `beta_managed_agents_agent_thread_context_compacted_event: object`

    Indicates that context compaction (summarization) occurred during the session.

  - `beta_managed_agents_session_error_event: object`

    An error event indicating a problem occurred during session execution.

  - `beta_managed_agents_session_status_rescheduled_event: object`

    Indicates the session is recovering from an error state and is rescheduled for execution.

  - `beta_managed_agents_session_status_running_event: object`

    Indicates the session is actively running and the agent is working.

  - `beta_managed_agents_session_status_idle_event: object`

    Indicates the agent has paused and is awaiting user input.

  - `beta_managed_agents_session_status_terminated_event: object`

    Indicates the session has terminated, either due to an error or completion.

  - `beta_managed_agents_session_thread_created_event: object`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

  - `beta_managed_agents_span_outcome_evaluation_start_event: object`

    Emitted when an outcome evaluation cycle begins.

  - `beta_managed_agents_span_outcome_evaluation_end_event: object`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

  - `beta_managed_agents_span_model_request_start_event: object`

    Emitted when a model request is initiated by the agent.

  - `beta_managed_agents_span_model_request_end_event: object`

    Emitted when a model request completes.

  - `beta_managed_agents_span_outcome_evaluation_ongoing_event: object`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

  - `beta_managed_agents_user_define_outcome_event: object`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

  - `beta_managed_agents_session_deleted_event: object`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

  - `beta_managed_agents_session_thread_status_running_event: object`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

  - `beta_managed_agents_session_thread_status_idle_event: object`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

  - `beta_managed_agents_session_thread_status_terminated_event: object`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

  - `beta_managed_agents_user_tool_result_event: object`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

  - `beta_managed_agents_session_thread_status_rescheduled_event: object`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

  - `beta_managed_agents_session_updated_event: object`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

  - `beta_managed_agents_start_event: object`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

  - `beta_managed_agents_delta_event: object`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

  - `beta_managed_agents_system_message_event: object`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

  - `beta_managed_agents_session_usage_event: object`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

#### Example

```bash
ant beta:sessions:events stream \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7
```

##### Response (200)

```json
{
  "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
  "content": [
    {
      "text": "Where is my order #1234?",
      "type": "text"
    }
  ],
  "type": "user.message",
  "processed_at": "2026-03-15T10:00:00Z"
}
```

## Sessions › Resources

### Add Session Resource

`$ ant beta:sessions:resources add`

**POST** `/v1/sessions/{session_id}/resources`

Add Session Resource

#### Parameters

- `--session-id: string`

  Path param: Path parameter session_id

- `--file-id: string`

  Body param: ID of a previously uploaded file.

  minLength: 1, maxLength: 128

- `--type: "file"`

  Body param

- `--mount-path: optional string`

  Body param: Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

  minLength: 1, maxLength: 4096

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_managed_agents_file_resource: object`

  - `id: string`

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `file_id: string`

  - `mount_path: string`

  - `type: "file"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

#### Example

```bash
ant beta:sessions:resources add \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7 \
  --file-id file_011CNha8iCJcU1wXNR6q4V8w \
  --type file
```

##### Response (200)

```json
{
  "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  "created_at": "2026-03-15T10:00:00Z",
  "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "mount_path": "/uploads/receipt.pdf",
  "type": "file",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

### List Session Resources

`$ ant beta:sessions:resources list`

**GET** `/v1/sessions/{session_id}/resources`

List Session Resources

#### Parameters

- `--session-id: string`

  Path param: Path parameter session_id

- `--limit: optional number`

  Query param: Maximum number of resources to return per page (max 1000). If omitted, returns all resources.

  format: int32

- `--page: optional string`

  Query param: Opaque cursor from a previous response's next_page field.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `BetaManagedAgentsListSessionResources: object`

  Paginated list of resources attached to a session.

  - `data: array of BetaManagedAgentsSessionResource`

    Resources for the session, ordered by `created_at`.

    - `beta_managed_agents_github_repository_resource: object`

      - `id: string`

      - `created_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `mount_path: string`

      - `type: "github_repository"`

      - `updated_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `url: string`

      - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

        - `beta_managed_agents_branch_checkout: object`

          - `name: string`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `type: "branch"`

        - `beta_managed_agents_commit_checkout: object`

          - `sha: string`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `type: "commit"`

    - `beta_managed_agents_file_resource: object`

      - `id: string`

      - `created_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `file_id: string`

      - `mount_path: string`

      - `type: "file"`

      - `updated_at: string`

        A timestamp in RFC 3339 format

        format: date-time

    - `beta_managed_agents_memory_store_resource: object`

      A memory store attached to an agent session.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

      - `access: optional "read_write" or "read_only"`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `description: optional string`

        Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

      - `instructions: optional string`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

        maxLength: 4096

      - `mount_path: optional string`

        Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

      - `name: optional string`

        Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

  - `next_page: optional string`

    Opaque cursor for the next page. Null when no more results.

#### Example

```bash
ant beta:sessions:resources list \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7
```

##### Response (200)

```json
{
  "data": [
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
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

### Get Session Resource

`$ ant beta:sessions:resources retrieve`

**GET** `/v1/sessions/{session_id}/resources/{resource_id}`

Get Session Resource

#### Parameters

- `--session-id: string`

  Path param: Path parameter session_id

- `--resource-id: string`

  Path param: Path parameter resource_id

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `BetaSessionResourceGetResponse: BetaManagedAgentsGitHubRepositoryResource or BetaManagedAgentsFileResource or BetaManagedAgentsMemoryStoreResource`

  The requested session resource.

  - `beta_managed_agents_github_repository_resource: object`

    - `id: string`

    - `created_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `mount_path: string`

    - `type: "github_repository"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `url: string`

    - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

      - `beta_managed_agents_branch_checkout: object`

        - `name: string`

          Branch name to check out.

          minLength: 1, maxLength: 255

        - `type: "branch"`

      - `beta_managed_agents_commit_checkout: object`

        - `sha: string`

          Full commit SHA to check out.

          minLength: 7, maxLength: 64

        - `type: "commit"`

  - `beta_managed_agents_file_resource: object`

    - `id: string`

    - `created_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `file_id: string`

    - `mount_path: string`

    - `type: "file"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `beta_managed_agents_memory_store_resource: object`

    A memory store attached to an agent session.

    - `memory_store_id: string`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: "memory_store"`

    - `access: optional "read_write" or "read_only"`

      Access mode for an attached memory store.

      - `"read_write"`

      - `"read_only"`

    - `description: optional string`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `instructions: optional string`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      maxLength: 4096

    - `mount_path: optional string`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `name: optional string`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

#### Example

```bash
ant beta:sessions:resources retrieve \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7 \
  --resource-id sesrsc_011CZkZBJq5dWxk9fVLNcPht
```

##### Response (200)

```json
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
```

### Update Session Resource

`$ ant beta:sessions:resources update`

**POST** `/v1/sessions/{session_id}/resources/{resource_id}`

Update Session Resource

#### Parameters

- `--session-id: string`

  Path param: Path parameter session_id

- `--resource-id: string`

  Path param: Path parameter resource_id

- `--authorization-token: string`

  Body param: New authorization token for the resource. Currently only `github_repository` resources support token rotation.

  minLength: 1, maxLength: 4096

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `BetaSessionResourceUpdateResponse: BetaManagedAgentsGitHubRepositoryResource or BetaManagedAgentsFileResource or BetaManagedAgentsMemoryStoreResource`

  The updated session resource.

  - `beta_managed_agents_github_repository_resource: object`

    - `id: string`

    - `created_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `mount_path: string`

    - `type: "github_repository"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `url: string`

    - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

      - `beta_managed_agents_branch_checkout: object`

        - `name: string`

          Branch name to check out.

          minLength: 1, maxLength: 255

        - `type: "branch"`

      - `beta_managed_agents_commit_checkout: object`

        - `sha: string`

          Full commit SHA to check out.

          minLength: 7, maxLength: 64

        - `type: "commit"`

  - `beta_managed_agents_file_resource: object`

    - `id: string`

    - `created_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `file_id: string`

    - `mount_path: string`

    - `type: "file"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

      format: date-time

  - `beta_managed_agents_memory_store_resource: object`

    A memory store attached to an agent session.

    - `memory_store_id: string`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: "memory_store"`

    - `access: optional "read_write" or "read_only"`

      Access mode for an attached memory store.

      - `"read_write"`

      - `"read_only"`

    - `description: optional string`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `instructions: optional string`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      maxLength: 4096

    - `mount_path: optional string`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `name: optional string`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

#### Example

```bash
ant beta:sessions:resources update \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7 \
  --resource-id sesrsc_011CZkZBJq5dWxk9fVLNcPht \
  --authorization-token ghp_exampletoken
```

##### Response (200)

```json
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
```

### Delete Session Resource

`$ ant beta:sessions:resources delete`

**DELETE** `/v1/sessions/{session_id}/resources/{resource_id}`

Delete Session Resource

#### Parameters

- `--session-id: string`

  Path param: Path parameter session_id

- `--resource-id: string`

  Path param: Path parameter resource_id

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_managed_agents_delete_session_resource: object`

  Confirmation of resource deletion.

  - `id: string`

  - `type: "session_resource_deleted"`

#### Example

```bash
ant beta:sessions:resources delete \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7 \
  --resource-id sesrsc_011CZkZBJq5dWxk9fVLNcPht
```

##### Response (200)

```json
{
  "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  "type": "session_resource_deleted"
}
```

## Sessions › Threads

### List Session Threads

`$ ant beta:sessions:threads list`

**GET** `/v1/sessions/{session_id}/threads`

List Session Threads

#### Parameters

- `--session-id: string`

  Path param: Path parameter session_id

- `--limit: optional number`

  Query param: Maximum results per page. Defaults to 1000.

  format: int32

- `--page: optional string`

  Query param: Opaque pagination cursor from a previous response's next_page. Forward-only.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `BetaManagedAgentsListSessionThreads: object`

  Paginated list of threads within a `session`.

  - `data: optional array of BetaManagedAgentsSessionThread`

    Threads in the session, primary first then children in spawn order.

    - `id: string`

      Unique identifier for this thread.

    - `agent: BetaManagedAgentsSessionThreadAgent or BetaManagedAgentsAdvisor`

      The resolved agent a session thread runs: a saved-agent snapshot, the platform advisor entry, or an inline-defined (ephemeral) agent snapshot.

      - `beta_managed_agents_session_thread_agent: object`

        Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

        - `id: string`

        - `description: string`

        - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

          - `name: string`

          - `type: "url"`

          - `url: string`

        - `model: object`

          Model identifier and configuration.

          - `id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

          - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

            How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

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

            Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

            - `"standard"`

            - `"fast"`

        - `name: string`

        - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

          - `beta_managed_agents_anthropic_skill: object`

            A resolved Anthropic-managed skill.

            - `skill_id: string`

            - `type: "anthropic"`

            - `version: string`

          - `beta_managed_agents_custom_skill: object`

            A resolved user-created custom skill.

            - `skill_id: string`

            - `type: "custom"`

            - `version: string`

        - `system: string`

        - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

          - `beta_managed_agents_agent_toolset20260401: object`

            - `configs: array of BetaManagedAgentsAgentToolConfig`

              - `beta_managed_agents_bash_tool_config: object`

                Configuration for the bash tool.

                - `enabled: boolean`

                - `name: "bash"`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                    - `type: "always_allow"`

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

                    - `type: "always_ask"`

                - `type: "bash"`

              - `beta_managed_agents_edit_tool_config: object`

                Configuration for the edit tool.

                - `enabled: boolean`

                - `name: "edit"`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

                - `type: "edit"`

              - `beta_managed_agents_read_tool_config: object`

                Configuration for the read tool.

                - `enabled: boolean`

                - `name: "read"`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

                - `type: "read"`

              - `beta_managed_agents_write_tool_config: object`

                Configuration for the write tool.

                - `enabled: boolean`

                - `name: "write"`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

                - `type: "write"`

              - `beta_managed_agents_glob_tool_config: object`

                Configuration for the glob tool.

                - `enabled: boolean`

                - `name: "glob"`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

                - `type: "glob"`

              - `beta_managed_agents_grep_tool_config: object`

                Configuration for the grep tool.

                - `enabled: boolean`

                - `name: "grep"`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

                - `type: "grep"`

              - `beta_managed_agents_web_fetch_tool_config: object`

                Configuration for the web_fetch tool.

                - `enabled: boolean`

                - `name: "web_fetch"`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

                - `type: "web_fetch"`

                - `allowed_domains: optional array of string`

                - `blocked_domains: optional array of string`

                - `max_content_tokens: optional number`

                  format: int32

              - `beta_managed_agents_web_search_tool_config: object`

                Configuration for the web_search tool.

                - `enabled: boolean`

                - `name: "web_search"`

                - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                  Permission policy for tool execution.

                  - `beta_managed_agents_always_allow_policy: object`

                    Tool calls are automatically approved without user confirmation.

                  - `beta_managed_agents_always_ask_policy: object`

                    Tool calls require user confirmation before execution.

                - `type: "web_search"`

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

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

            - `type: "agent_toolset_20260401"`

          - `beta_managed_agents_mcp_toolset: object`

            - `configs: array of BetaManagedAgentsMCPToolConfig`

              - `enabled: boolean`

              - `name: string`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

            - `default_config: object`

              Resolved default configuration for all tools from an MCP server.

              - `enabled: boolean`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

            - `mcp_server_name: string`

            - `type: "mcp_toolset"`

          - `beta_managed_agents_custom_tool: object`

            A custom tool as returned in API responses.

            - `description: string`

            - `input_schema: object`

              JSON Schema for custom tool input parameters.

              - `type: "object"`

              - `properties: optional map[unknown]`

              - `required: optional array of string`

            - `name: string`

            - `type: "custom"`

        - `type: "agent"`

        - `version: number`

          format: int32

      - `beta_managed_agents_advisor: object`

        Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

        - `model: string`

          The advisor model id.

        - `type: "advisor"`

    - `archived_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `created_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `parent_thread_id: string`

      Parent thread that spawned this thread. Null for the primary thread.

    - `session_id: string`

      The session this thread belongs to.

    - `stats: object`

      Timing statistics for a session thread.

      - `active_seconds: optional number`

        Cumulative time in seconds the thread spent actively running. Excludes idle time.

        format: double

      - `duration_seconds: optional number`

        Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

        format: double

      - `startup_seconds: optional number`

        Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

        format: double

    - `status: "running" or "idle" or "rescheduling" or "terminated"`

      SessionThreadStatus enum

      - `"running"`

      - `"idle"`

      - `"rescheduling"`

      - `"terminated"`

    - `type: "session_thread"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `usage: object`

      Cumulative token usage for a session thread across all turns.

      - `active_seconds: optional number`

        Cumulative time in seconds this thread spent in running status. Equal to `stats.active_seconds`; surfaced here so a thread's usage carries every quantity its cost is priced on.

        format: double

      - `cache_creation: optional object`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `ephemeral_1h_input_tokens: optional number`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `ephemeral_5m_input_tokens: optional number`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `cache_read_input_tokens: optional number`

        Total tokens read from prompt cache.

        format: int32

      - `input_tokens: optional number`

        Total input tokens consumed across all turns.

        format: int32

      - `list_cost: optional object`

        A monetary amount in a specific currency.

        - `amount: string`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `currency: "USD"`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `output_tokens: optional number`

        Total output tokens generated across all turns.

        format: int32

      - `server_tool_use: optional object`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `web_fetch_requests: optional number`

          Number of server-executed web fetch requests.

          format: int32

        - `web_search_requests: optional number`

          Number of server-executed web search requests.

          format: int32

  - `next_page: optional string`

    Opaque cursor for the next page. Null when no more results.

#### Example

```bash
ant beta:sessions:threads list \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "sthr_011CZkZVWa6oIjw0rgXZpnBt",
      "agent": {
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
      },
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "parent_thread_id": null,
      "session_id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
      "stats": {
        "active_seconds": 0,
        "duration_seconds": 0,
        "startup_seconds": 0
      },
      "status": "idle",
      "type": "session_thread",
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
      }
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

### Get Session Thread

`$ ant beta:sessions:threads retrieve`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}`

Get Session Thread

#### Parameters

- `--session-id: string`

  Path param: Path parameter session_id

- `--thread-id: string`

  Path param: Path parameter thread_id

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_managed_agents_session_thread: object`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `id: string`

    Unique identifier for this thread.

  - `agent: BetaManagedAgentsSessionThreadAgent or BetaManagedAgentsAdvisor`

    The resolved agent a session thread runs: a saved-agent snapshot, the platform advisor entry, or an inline-defined (ephemeral) agent snapshot.

    - `beta_managed_agents_session_thread_agent: object`

      Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

      - `id: string`

      - `description: string`

      - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

        - `name: string`

        - `type: "url"`

        - `url: string`

      - `model: object`

        Model identifier and configuration.

        - `id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

        - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

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

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

      - `name: string`

      - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

        - `beta_managed_agents_anthropic_skill: object`

          A resolved Anthropic-managed skill.

          - `skill_id: string`

          - `type: "anthropic"`

          - `version: string`

        - `beta_managed_agents_custom_skill: object`

          A resolved user-created custom skill.

          - `skill_id: string`

          - `type: "custom"`

          - `version: string`

      - `system: string`

      - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

        - `beta_managed_agents_agent_toolset20260401: object`

          - `configs: array of BetaManagedAgentsAgentToolConfig`

            - `beta_managed_agents_bash_tool_config: object`

              Configuration for the bash tool.

              - `enabled: boolean`

              - `name: "bash"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                  - `type: "always_allow"`

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

                  - `type: "always_ask"`

              - `type: "bash"`

            - `beta_managed_agents_edit_tool_config: object`

              Configuration for the edit tool.

              - `enabled: boolean`

              - `name: "edit"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

              - `type: "edit"`

            - `beta_managed_agents_read_tool_config: object`

              Configuration for the read tool.

              - `enabled: boolean`

              - `name: "read"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

              - `type: "read"`

            - `beta_managed_agents_write_tool_config: object`

              Configuration for the write tool.

              - `enabled: boolean`

              - `name: "write"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

              - `type: "write"`

            - `beta_managed_agents_glob_tool_config: object`

              Configuration for the glob tool.

              - `enabled: boolean`

              - `name: "glob"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

              - `type: "glob"`

            - `beta_managed_agents_grep_tool_config: object`

              Configuration for the grep tool.

              - `enabled: boolean`

              - `name: "grep"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

              - `type: "grep"`

            - `beta_managed_agents_web_fetch_tool_config: object`

              Configuration for the web_fetch tool.

              - `enabled: boolean`

              - `name: "web_fetch"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

              - `type: "web_fetch"`

              - `allowed_domains: optional array of string`

              - `blocked_domains: optional array of string`

              - `max_content_tokens: optional number`

                format: int32

            - `beta_managed_agents_web_search_tool_config: object`

              Configuration for the web_search tool.

              - `enabled: boolean`

              - `name: "web_search"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

              - `type: "web_search"`

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

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object`

                Tool calls are automatically approved without user confirmation.

              - `beta_managed_agents_always_ask_policy: object`

                Tool calls require user confirmation before execution.

          - `type: "agent_toolset_20260401"`

        - `beta_managed_agents_mcp_toolset: object`

          - `configs: array of BetaManagedAgentsMCPToolConfig`

            - `enabled: boolean`

            - `name: string`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object`

                Tool calls are automatically approved without user confirmation.

              - `beta_managed_agents_always_ask_policy: object`

                Tool calls require user confirmation before execution.

          - `default_config: object`

            Resolved default configuration for all tools from an MCP server.

            - `enabled: boolean`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object`

                Tool calls are automatically approved without user confirmation.

              - `beta_managed_agents_always_ask_policy: object`

                Tool calls require user confirmation before execution.

          - `mcp_server_name: string`

          - `type: "mcp_toolset"`

        - `beta_managed_agents_custom_tool: object`

          A custom tool as returned in API responses.

          - `description: string`

          - `input_schema: object`

            JSON Schema for custom tool input parameters.

            - `type: "object"`

            - `properties: optional map[unknown]`

            - `required: optional array of string`

          - `name: string`

          - `type: "custom"`

      - `type: "agent"`

      - `version: number`

        format: int32

    - `beta_managed_agents_advisor: object`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `model: string`

        The advisor model id.

      - `type: "advisor"`

  - `archived_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `parent_thread_id: string`

    Parent thread that spawned this thread. Null for the primary thread.

  - `session_id: string`

    The session this thread belongs to.

  - `stats: object`

    Timing statistics for a session thread.

    - `active_seconds: optional number`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

      format: double

    - `duration_seconds: optional number`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

      format: double

    - `startup_seconds: optional number`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

      format: double

  - `status: "running" or "idle" or "rescheduling" or "terminated"`

    SessionThreadStatus enum

    - `"running"`

    - `"idle"`

    - `"rescheduling"`

    - `"terminated"`

  - `type: "session_thread"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `usage: object`

    Cumulative token usage for a session thread across all turns.

    - `active_seconds: optional number`

      Cumulative time in seconds this thread spent in running status. Equal to `stats.active_seconds`; surfaced here so a thread's usage carries every quantity its cost is priced on.

      format: double

    - `cache_creation: optional object`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: optional number`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `ephemeral_5m_input_tokens: optional number`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `cache_read_input_tokens: optional number`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens: optional number`

      Total input tokens consumed across all turns.

      format: int32

    - `list_cost: optional object`

      A monetary amount in a specific currency.

      - `amount: string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: "USD"`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `output_tokens: optional number`

      Total output tokens generated across all turns.

      format: int32

    - `server_tool_use: optional object`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `web_fetch_requests: optional number`

        Number of server-executed web fetch requests.

        format: int32

      - `web_search_requests: optional number`

        Number of server-executed web search requests.

        format: int32

#### Example

```bash
ant beta:sessions:threads retrieve \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7 \
  --thread-id sthr_011CZkZVWa6oIjw0rgXZpnBt
```

##### Response (200)

```json
{
  "id": "sthr_011CZkZVWa6oIjw0rgXZpnBt",
  "agent": {
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
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "parent_thread_id": null,
  "session_id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0,
    "startup_seconds": 0
  },
  "status": "idle",
  "type": "session_thread",
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
  }
}
```

### Archive Session Thread

`$ ant beta:sessions:threads archive`

**POST** `/v1/sessions/{session_id}/threads/{thread_id}/archive`

Archive Session Thread

#### Parameters

- `--session-id: string`

  Path param: Path parameter session_id

- `--thread-id: string`

  Path param: Path parameter thread_id

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_managed_agents_session_thread: object`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `id: string`

    Unique identifier for this thread.

  - `agent: BetaManagedAgentsSessionThreadAgent or BetaManagedAgentsAdvisor`

    The resolved agent a session thread runs: a saved-agent snapshot, the platform advisor entry, or an inline-defined (ephemeral) agent snapshot.

    - `beta_managed_agents_session_thread_agent: object`

      Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

      - `id: string`

      - `description: string`

      - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

        - `name: string`

        - `type: "url"`

        - `url: string`

      - `model: object`

        Model identifier and configuration.

        - `id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

        - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

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

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

      - `name: string`

      - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

        - `beta_managed_agents_anthropic_skill: object`

          A resolved Anthropic-managed skill.

          - `skill_id: string`

          - `type: "anthropic"`

          - `version: string`

        - `beta_managed_agents_custom_skill: object`

          A resolved user-created custom skill.

          - `skill_id: string`

          - `type: "custom"`

          - `version: string`

      - `system: string`

      - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

        - `beta_managed_agents_agent_toolset20260401: object`

          - `configs: array of BetaManagedAgentsAgentToolConfig`

            - `beta_managed_agents_bash_tool_config: object`

              Configuration for the bash tool.

              - `enabled: boolean`

              - `name: "bash"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                  - `type: "always_allow"`

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

                  - `type: "always_ask"`

              - `type: "bash"`

            - `beta_managed_agents_edit_tool_config: object`

              Configuration for the edit tool.

              - `enabled: boolean`

              - `name: "edit"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

              - `type: "edit"`

            - `beta_managed_agents_read_tool_config: object`

              Configuration for the read tool.

              - `enabled: boolean`

              - `name: "read"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

              - `type: "read"`

            - `beta_managed_agents_write_tool_config: object`

              Configuration for the write tool.

              - `enabled: boolean`

              - `name: "write"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

              - `type: "write"`

            - `beta_managed_agents_glob_tool_config: object`

              Configuration for the glob tool.

              - `enabled: boolean`

              - `name: "glob"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

              - `type: "glob"`

            - `beta_managed_agents_grep_tool_config: object`

              Configuration for the grep tool.

              - `enabled: boolean`

              - `name: "grep"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

              - `type: "grep"`

            - `beta_managed_agents_web_fetch_tool_config: object`

              Configuration for the web_fetch tool.

              - `enabled: boolean`

              - `name: "web_fetch"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

              - `type: "web_fetch"`

              - `allowed_domains: optional array of string`

              - `blocked_domains: optional array of string`

              - `max_content_tokens: optional number`

                format: int32

            - `beta_managed_agents_web_search_tool_config: object`

              Configuration for the web_search tool.

              - `enabled: boolean`

              - `name: "web_search"`

              - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                Permission policy for tool execution.

                - `beta_managed_agents_always_allow_policy: object`

                  Tool calls are automatically approved without user confirmation.

                - `beta_managed_agents_always_ask_policy: object`

                  Tool calls require user confirmation before execution.

              - `type: "web_search"`

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

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object`

                Tool calls are automatically approved without user confirmation.

              - `beta_managed_agents_always_ask_policy: object`

                Tool calls require user confirmation before execution.

          - `type: "agent_toolset_20260401"`

        - `beta_managed_agents_mcp_toolset: object`

          - `configs: array of BetaManagedAgentsMCPToolConfig`

            - `enabled: boolean`

            - `name: string`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object`

                Tool calls are automatically approved without user confirmation.

              - `beta_managed_agents_always_ask_policy: object`

                Tool calls require user confirmation before execution.

          - `default_config: object`

            Resolved default configuration for all tools from an MCP server.

            - `enabled: boolean`

            - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

              Permission policy for tool execution.

              - `beta_managed_agents_always_allow_policy: object`

                Tool calls are automatically approved without user confirmation.

              - `beta_managed_agents_always_ask_policy: object`

                Tool calls require user confirmation before execution.

          - `mcp_server_name: string`

          - `type: "mcp_toolset"`

        - `beta_managed_agents_custom_tool: object`

          A custom tool as returned in API responses.

          - `description: string`

          - `input_schema: object`

            JSON Schema for custom tool input parameters.

            - `type: "object"`

            - `properties: optional map[unknown]`

            - `required: optional array of string`

          - `name: string`

          - `type: "custom"`

      - `type: "agent"`

      - `version: number`

        format: int32

    - `beta_managed_agents_advisor: object`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `model: string`

        The advisor model id.

      - `type: "advisor"`

  - `archived_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `parent_thread_id: string`

    Parent thread that spawned this thread. Null for the primary thread.

  - `session_id: string`

    The session this thread belongs to.

  - `stats: object`

    Timing statistics for a session thread.

    - `active_seconds: optional number`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

      format: double

    - `duration_seconds: optional number`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

      format: double

    - `startup_seconds: optional number`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

      format: double

  - `status: "running" or "idle" or "rescheduling" or "terminated"`

    SessionThreadStatus enum

    - `"running"`

    - `"idle"`

    - `"rescheduling"`

    - `"terminated"`

  - `type: "session_thread"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `usage: object`

    Cumulative token usage for a session thread across all turns.

    - `active_seconds: optional number`

      Cumulative time in seconds this thread spent in running status. Equal to `stats.active_seconds`; surfaced here so a thread's usage carries every quantity its cost is priced on.

      format: double

    - `cache_creation: optional object`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `ephemeral_1h_input_tokens: optional number`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `ephemeral_5m_input_tokens: optional number`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `cache_read_input_tokens: optional number`

      Total tokens read from prompt cache.

      format: int32

    - `input_tokens: optional number`

      Total input tokens consumed across all turns.

      format: int32

    - `list_cost: optional object`

      A monetary amount in a specific currency.

      - `amount: string`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `currency: "USD"`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `output_tokens: optional number`

      Total output tokens generated across all turns.

      format: int32

    - `server_tool_use: optional object`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `web_fetch_requests: optional number`

        Number of server-executed web fetch requests.

        format: int32

      - `web_search_requests: optional number`

        Number of server-executed web search requests.

        format: int32

#### Example

```bash
ant beta:sessions:threads archive \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7 \
  --thread-id sthr_011CZkZVWa6oIjw0rgXZpnBt
```

##### Response (200)

```json
{
  "id": "sthr_011CZkZVWa6oIjw0rgXZpnBt",
  "agent": {
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
  },
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "parent_thread_id": null,
  "session_id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "stats": {
    "active_seconds": 0,
    "duration_seconds": 0,
    "startup_seconds": 0
  },
  "status": "idle",
  "type": "session_thread",
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
  }
}
```

## Sessions › Threads › Events

### List Session Thread Events

`$ ant beta:sessions:threads:events list`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}/events`

List Session Thread Events

#### Parameters

- `--session-id: string`

  Path param: Path parameter session_id

- `--thread-id: string`

  Path param: Path parameter thread_id

- `--limit: optional number`

  Query param: Query parameter for limit

  format: int32

- `--page: optional string`

  Query param: Query parameter for page

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `BetaManagedAgentsListSessionThreadEvents: object`

  Paginated list of events for a single thread within a `session`.

  - `data: optional array of BetaManagedAgentsSessionEvent`

    Events for the thread, ordered by `processed_at`.

    - `beta_managed_agents_user_message_event: object`

      A user message event in the session conversation.

      - `id: string`

        Unique identifier for this event.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

        Array of content blocks comprising the user message.

        - `beta_managed_agents_text_block: object`

          Regular text content.

          - `text: string`

            The text content.

            minLength: 1

          - `type: "text"`

        - `beta_managed_agents_image_block: object`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `beta_managed_agents_base64_image_source: object`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

                minLength: 1

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `type: "base64"`

            - `beta_managed_agents_url_image_source: object`

              Image referenced by URL.

              - `type: "url"`

              - `url: string`

                URL of the image to fetch.

                minLength: 1

            - `beta_managed_agents_file_image_source: object`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

                minLength: 1

              - `type: "file"`

          - `type: "image"`

        - `beta_managed_agents_document_block: object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `beta_managed_agents_base64_document_source: object`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

                minLength: 1

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `type: "base64"`

            - `beta_managed_agents_plain_text_document_source: object`

              Plain text document content.

              - `data: string`

                The plain text content.

                minLength: 1

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

              - `type: "text"`

            - `beta_managed_agents_url_document_source: object`

              Document referenced by URL.

              - `type: "url"`

              - `url: string`

                URL of the document to fetch.

                minLength: 1

            - `beta_managed_agents_file_document_source: object`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

                minLength: 1

              - `type: "file"`

          - `type: "document"`

          - `context: optional string`

            Additional context about the document for the model.

          - `title: optional string`

            The title of the document.

        - `beta_managed_agents_redacted_block: object`

          Placeholder for content withheld by Anthropic model policy.

          - `type: "redacted"`

      - `type: "user.message"`

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

        format: date-time

    - `beta_managed_agents_user_interrupt_event: object`

      An interrupt event that pauses agent execution and returns control to the user.

      - `id: string`

        Unique identifier for this event.

      - `type: "user.interrupt"`

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: optional string`

        If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

    - `beta_managed_agents_user_tool_confirmation_event: object`

      A tool confirmation event that approves or denies a pending tool execution.

      - `id: string`

        Unique identifier for this event.

      - `result: "allow" or "deny"`

        UserToolConfirmationResult enum

        - `"allow"`

        - `"deny"`

      - `tool_use_id: string`

        The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: "user.tool_confirmation"`

      - `deny_message: optional string`

        Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

        maxLength: 10000

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: optional string`

        When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

    - `beta_managed_agents_user_custom_tool_result_event: object`

      Event sent by the client providing the result of a custom tool execution.

      - `id: string`

        Unique identifier for this event.

      - `custom_tool_use_id: string`

        The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: "user.custom_tool_result"`

      - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

        The result content returned by the tool.

        - `beta_managed_agents_text_block: object`

          Regular text content.

        - `beta_managed_agents_image_block: object`

          Image content specified directly as base64 data or as a reference via a URL.

        - `beta_managed_agents_document_block: object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `beta_managed_agents_search_result_block: object`

          A block containing a web search result.

          - `citations: object`

            Citation settings for a search result.

            - `enabled: boolean`

              Whether citations are enabled for this search result.

          - `content: array of BetaManagedAgentsSearchResultContent`

            Array of text content blocks from the search result.

            - `text: string`

              The text content.

              minLength: 1

            - `type: "text"`

          - `source: string`

            The URL source of the search result.

            minLength: 1

          - `title: string`

            The title of the search result.

            minLength: 1

          - `type: "search_result"`

      - `is_error: optional boolean`

        Whether the tool execution resulted in an error.

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: optional string`

        Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

    - `beta_managed_agents_agent_custom_tool_use_event: object`

      Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

      - `id: string`

        Unique identifier for this event.

      - `input: map[unknown]`

        Input parameters for the tool call.

      - `name: string`

        Name of the custom tool being called.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: "agent.custom_tool_use"`

      - `session_thread_id: optional string`

        When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

    - `beta_managed_agents_agent_message_event: object`

      An agent response event in the session conversation.

      - `id: string`

        Unique identifier for this event.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsRedactedBlock`

        Array of text blocks comprising the agent response.

        - `beta_managed_agents_text_block: object`

          Regular text content.

        - `beta_managed_agents_redacted_block: object`

          Placeholder for content withheld by Anthropic model policy.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: "agent.message"`

    - `beta_managed_agents_agent_thinking_event: object`

      Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: "agent.thinking"`

    - `beta_managed_agents_agent_mcp_tool_use_event: object`

      Event emitted when the agent invokes a tool provided by an MCP server.

      - `id: string`

        Unique identifier for this event.

      - `input: map[unknown]`

        Input parameters for the tool call.

      - `mcp_server_name: string`

        Name of the MCP server providing the tool.

      - `name: string`

        Name of the MCP tool being used.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: "agent.mcp_tool_use"`

      - `evaluated_permission: optional "allow" or "ask" or "deny"`

        AgentEvaluatedPermission enum

        - `"allow"`

        - `"ask"`

        - `"deny"`

      - `session_thread_id: optional string`

        When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

    - `beta_managed_agents_agent_mcp_tool_result_event: object`

      Event representing the result of an MCP tool execution.

      - `id: string`

        Unique identifier for this event.

      - `mcp_tool_use_id: string`

        The id of the `agent.mcp_tool_use` event this result corresponds to.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: "agent.mcp_tool_result"`

      - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

        The result content returned by the tool.

        - `beta_managed_agents_text_block: object`

          Regular text content.

        - `beta_managed_agents_image_block: object`

          Image content specified directly as base64 data or as a reference via a URL.

        - `beta_managed_agents_document_block: object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `beta_managed_agents_search_result_block: object`

          A block containing a web search result.

      - `is_error: optional boolean`

        Whether the tool execution resulted in an error.

    - `beta_managed_agents_agent_tool_use_event: object`

      Event emitted when the agent invokes a built-in agent tool.

      - `id: string`

        Unique identifier for this event.

      - `input: map[unknown]`

        Input parameters for the tool call.

      - `name: string`

        Name of the agent tool being used.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: "agent.tool_use"`

      - `evaluated_permission: optional "allow" or "ask" or "deny"`

        AgentEvaluatedPermission enum

        - `"allow"`

        - `"ask"`

        - `"deny"`

      - `session_thread_id: optional string`

        When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

    - `beta_managed_agents_agent_tool_result_event: object`

      Event representing the result of an agent tool execution.

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `tool_use_id: string`

        The id of the `agent.tool_use` event this result corresponds to.

      - `type: "agent.tool_result"`

      - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

        The result content returned by the tool.

        - `beta_managed_agents_text_block: object`

          Regular text content.

        - `beta_managed_agents_image_block: object`

          Image content specified directly as base64 data or as a reference via a URL.

        - `beta_managed_agents_document_block: object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `beta_managed_agents_search_result_block: object`

          A block containing a web search result.

      - `is_error: optional boolean`

        Whether the tool execution resulted in an error.

    - `beta_managed_agents_agent_thread_message_received_event: object`

      Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

      - `id: string`

        Unique identifier for this event.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

        Message content blocks.

        - `beta_managed_agents_text_block: object`

          Regular text content.

        - `beta_managed_agents_image_block: object`

          Image content specified directly as base64 data or as a reference via a URL.

        - `beta_managed_agents_document_block: object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `beta_managed_agents_redacted_block: object`

          Placeholder for content withheld by Anthropic model policy.

      - `from_session_thread_id: string`

        Public `sthr_` ID of the thread that sent the message.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: "agent.thread_message_received"`

      - `from_agent_name: optional string`

        Name of the callable agent this message came from. Absent when received from the primary agent.

    - `beta_managed_agents_agent_thread_message_sent_event: object`

      Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

      - `id: string`

        Unique identifier for this event.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

        Message content blocks.

        - `beta_managed_agents_text_block: object`

          Regular text content.

        - `beta_managed_agents_image_block: object`

          Image content specified directly as base64 data or as a reference via a URL.

        - `beta_managed_agents_document_block: object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `beta_managed_agents_redacted_block: object`

          Placeholder for content withheld by Anthropic model policy.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `to_session_thread_id: string`

        Public `sthr_` ID of the thread the message was sent to.

      - `type: "agent.thread_message_sent"`

      - `to_agent_name: optional string`

        Name of the callable agent this message was sent to. Absent when sent to the primary agent.

    - `beta_managed_agents_agent_thread_context_compacted_event: object`

      Indicates that context compaction (summarization) occurred during the session.

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: "agent.thread_context_compacted"`

    - `beta_managed_agents_session_error_event: object`

      An error event indicating a problem occurred during session execution.

      - `id: string`

        Unique identifier for this event.

      - `error: BetaManagedAgentsUnknownError or BetaManagedAgentsModelOverloadedError or BetaManagedAgentsModelRateLimitedError or 5 more`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `beta_managed_agents_unknown_error: object`

          An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

          - `message: string`

            Human-readable error description.

          - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

            What the client should do next in response to this error.

            - `beta_managed_agents_retry_status_retrying: object`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

              - `type: "retrying"`

            - `beta_managed_agents_retry_status_exhausted: object`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

              - `type: "exhausted"`

            - `beta_managed_agents_retry_status_terminal: object`

              The session encountered a terminal error and will transition to `terminated` state.

              - `type: "terminal"`

          - `type: "unknown_error"`

        - `beta_managed_agents_model_overloaded_error: object`

          The model is currently overloaded. Emitted after automatic retries are exhausted.

          - `message: string`

            Human-readable error description.

          - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

            What the client should do next in response to this error.

            - `beta_managed_agents_retry_status_retrying: object`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `beta_managed_agents_retry_status_exhausted: object`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `beta_managed_agents_retry_status_terminal: object`

              The session encountered a terminal error and will transition to `terminated` state.

          - `type: "model_overloaded_error"`

        - `beta_managed_agents_model_rate_limited_error: object`

          The model request was rate-limited.

          - `message: string`

            Human-readable error description.

          - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

            What the client should do next in response to this error.

            - `beta_managed_agents_retry_status_retrying: object`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `beta_managed_agents_retry_status_exhausted: object`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `beta_managed_agents_retry_status_terminal: object`

              The session encountered a terminal error and will transition to `terminated` state.

          - `type: "model_rate_limited_error"`

        - `beta_managed_agents_model_request_failed_error: object`

          A model request failed for a reason other than overload or rate-limiting.

          - `message: string`

            Human-readable error description.

          - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

            What the client should do next in response to this error.

            - `beta_managed_agents_retry_status_retrying: object`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `beta_managed_agents_retry_status_exhausted: object`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `beta_managed_agents_retry_status_terminal: object`

              The session encountered a terminal error and will transition to `terminated` state.

          - `type: "model_request_failed_error"`

        - `beta_managed_agents_mcp_connection_failed_error: object`

          Failed to connect to an MCP server.

          - `mcp_server_name: string`

            Name of the MCP server that failed to connect.

          - `message: string`

            Human-readable error description.

          - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

            What the client should do next in response to this error.

            - `beta_managed_agents_retry_status_retrying: object`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `beta_managed_agents_retry_status_exhausted: object`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `beta_managed_agents_retry_status_terminal: object`

              The session encountered a terminal error and will transition to `terminated` state.

          - `type: "mcp_connection_failed_error"`

        - `beta_managed_agents_mcp_authentication_failed_error: object`

          Authentication to an MCP server failed.

          - `mcp_server_name: string`

            Name of the MCP server that failed authentication.

          - `message: string`

            Human-readable error description.

          - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

            What the client should do next in response to this error.

            - `beta_managed_agents_retry_status_retrying: object`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `beta_managed_agents_retry_status_exhausted: object`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `beta_managed_agents_retry_status_terminal: object`

              The session encountered a terminal error and will transition to `terminated` state.

          - `type: "mcp_authentication_failed_error"`

        - `beta_managed_agents_billing_error: object`

          The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

          - `message: string`

            Human-readable error description.

          - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

            What the client should do next in response to this error.

            - `beta_managed_agents_retry_status_retrying: object`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `beta_managed_agents_retry_status_exhausted: object`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `beta_managed_agents_retry_status_terminal: object`

              The session encountered a terminal error and will transition to `terminated` state.

          - `type: "billing_error"`

        - `beta_managed_agents_credential_host_unreachable_error: object`

          An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

          - `credential_id: string`

            ID of the affected credential.

          - `message: string`

            Human-readable error description.

          - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

            What the client should do next in response to this error.

            - `beta_managed_agents_retry_status_retrying: object`

              The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `beta_managed_agents_retry_status_exhausted: object`

              This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `beta_managed_agents_retry_status_terminal: object`

              The session encountered a terminal error and will transition to `terminated` state.

          - `type: "credential_host_unreachable_error"`

          - `vault_id: string`

            ID of the vault containing the affected credential.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: "session.error"`

    - `beta_managed_agents_session_status_rescheduled_event: object`

      Indicates the session is recovering from an error state and is rescheduled for execution.

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: "session.status_rescheduled"`

    - `beta_managed_agents_session_status_running_event: object`

      Indicates the session is actively running and the agent is working.

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: "session.status_running"`

    - `beta_managed_agents_session_status_idle_event: object`

      Indicates the agent has paused and is awaiting user input.

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted or BetaManagedAgentsSessionBudgetReached`

        The agent completed its turn naturally and is ready for the next user message.

        - `beta_managed_agents_session_end_turn: object`

          The agent completed its turn naturally and is ready for the next user message.

          - `type: "end_turn"`

        - `beta_managed_agents_session_requires_action: object`

          The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

          - `event_ids: array of string`

            The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

          - `type: "requires_action"`

        - `beta_managed_agents_session_retries_exhausted: object`

          The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

          - `type: "retries_exhausted"`

        - `beta_managed_agents_session_budget_reached: object`

          The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

          - `type: "budget_reached"`

      - `type: "session.status_idle"`

    - `beta_managed_agents_session_status_terminated_event: object`

      Indicates the session has terminated, either due to an error or completion.

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: "session.status_terminated"`

    - `beta_managed_agents_session_thread_created_event: object`

      Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

      - `id: string`

        Unique identifier for this event.

      - `agent_name: string`

        Name of the callable agent the thread runs.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: string`

        Public `sthr_` ID of the newly created thread.

      - `type: "session.thread_created"`

    - `beta_managed_agents_span_outcome_evaluation_start_event: object`

      Emitted when an outcome evaluation cycle begins.

      - `id: string`

        Unique identifier for this event.

      - `iteration: number`

        0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

        format: int32

      - `outcome_id: string`

        The `outc_` ID of the outcome being evaluated.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: "span.outcome_evaluation_start"`

    - `beta_managed_agents_span_outcome_evaluation_end_event: object`

      Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

      - `id: string`

        Unique identifier for this event.

      - `explanation: string`

        Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

      - `iteration: number`

        0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

        format: int32

      - `outcome_evaluation_start_id: string`

        The id of the corresponding `span.outcome_evaluation_start` event.

      - `outcome_id: string`

        The `outc_` ID of the outcome being evaluated.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `result: string`

        Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

      - `type: "span.outcome_evaluation_end"`

      - `usage: object`

        Token usage for a single model request.

        - `cache_creation_input_tokens: number`

          Tokens used to create prompt cache in this request.

          format: int32

        - `cache_read_input_tokens: number`

          Tokens read from prompt cache in this request.

          format: int32

        - `input_tokens: number`

          Input tokens consumed by this request.

          format: int32

        - `output_tokens: number`

          Output tokens generated by this request.

          format: int32

        - `speed: optional "standard" or "fast"`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

    - `beta_managed_agents_span_model_request_start_event: object`

      Emitted when a model request is initiated by the agent.

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: "span.model_request_start"`

    - `beta_managed_agents_span_model_request_end_event: object`

      Emitted when a model request completes.

      - `id: string`

        Unique identifier for this event.

      - `is_error: boolean`

        Whether the model request resulted in an error.

      - `model_request_start_id: string`

        The id of the corresponding `span.model_request_start` event.

      - `model_usage: object`

        Token usage for a single model request.

        - `cache_creation_input_tokens: number`

          Tokens used to create prompt cache in this request.

          format: int32

        - `cache_read_input_tokens: number`

          Tokens read from prompt cache in this request.

          format: int32

        - `input_tokens: number`

          Input tokens consumed by this request.

          format: int32

        - `output_tokens: number`

          Output tokens generated by this request.

          format: int32

        - `speed: optional "standard" or "fast"`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: "span.model_request_end"`

    - `beta_managed_agents_span_outcome_evaluation_ongoing_event: object`

      Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

      - `id: string`

        Unique identifier for this event.

      - `iteration: number`

        0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

        format: int32

      - `outcome_id: string`

        The `outc_` ID of the outcome being evaluated.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: "span.outcome_evaluation_ongoing"`

    - `beta_managed_agents_user_define_outcome_event: object`

      Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

      - `id: string`

        Unique identifier for this event.

      - `description: string`

        What the agent should produce. Copied from the input event.

      - `max_iterations: number`

        Evaluate-then-revise cycles before giving up. Default 3, max 20.

        format: int32

      - `outcome_id: string`

        Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `beta_managed_agents_file_rubric: object`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: string`

            ID of the rubric file.

          - `type: "file"`

        - `beta_managed_agents_text_rubric: object`

          Rubric content provided inline as text.

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: "text"`

      - `type: "user.define_outcome"`

    - `beta_managed_agents_session_deleted_event: object`

      Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: "session.deleted"`

    - `beta_managed_agents_session_thread_status_running_event: object`

      A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

      - `id: string`

        Unique identifier for this event.

      - `agent_name: string`

        Name of the agent the thread runs.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: string`

        Public sthr_ ID of the thread that started running.

      - `type: "session.thread_status_running"`

    - `beta_managed_agents_session_thread_status_idle_event: object`

      A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

      - `id: string`

        Unique identifier for this event.

      - `agent_name: string`

        Name of the agent the thread runs.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: string`

        Public sthr_ ID of the thread that went idle.

      - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted or BetaManagedAgentsSessionBudgetReached`

        The agent completed its turn naturally and is ready for the next user message.

        - `beta_managed_agents_session_end_turn: object`

          The agent completed its turn naturally and is ready for the next user message.

        - `beta_managed_agents_session_requires_action: object`

          The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `beta_managed_agents_session_retries_exhausted: object`

          The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `beta_managed_agents_session_budget_reached: object`

          The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

      - `type: "session.thread_status_idle"`

    - `beta_managed_agents_session_thread_status_terminated_event: object`

      A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

      - `id: string`

        Unique identifier for this event.

      - `agent_name: string`

        Name of the agent the thread runs.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: string`

        Public sthr_ ID of the thread that terminated.

      - `type: "session.thread_status_terminated"`

    - `beta_managed_agents_user_tool_result_event: object`

      Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

      - `id: string`

        Unique identifier for this event.

      - `tool_use_id: string`

        The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

      - `type: "user.tool_result"`

      - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

        The result content returned by the tool.

        - `beta_managed_agents_text_block: object`

          Regular text content.

        - `beta_managed_agents_image_block: object`

          Image content specified directly as base64 data or as a reference via a URL.

        - `beta_managed_agents_document_block: object`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `beta_managed_agents_search_result_block: object`

          A block containing a web search result.

      - `is_error: optional boolean`

        Whether the tool execution resulted in an error.

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: optional string`

        Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

    - `beta_managed_agents_session_thread_status_rescheduled_event: object`

      A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

      - `id: string`

        Unique identifier for this event.

      - `agent_name: string`

        Name of the agent the thread runs.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `session_thread_id: string`

        Public sthr_ ID of the thread that is retrying.

      - `type: "session.thread_status_rescheduled"`

    - `beta_managed_agents_session_updated_event: object`

      Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: "session.updated"`

      - `agent: optional object`

        Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

        - `id: string`

        - `description: string`

        - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

          - `name: string`

          - `type: "url"`

          - `url: string`

        - `model: object`

          Model identifier and configuration.

          - `id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string`

            The model that will power your agent.

            See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

          - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

            How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

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

            Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

            - `"standard"`

            - `"fast"`

        - `multiagent: object`

          Resolved coordinator topology with full agent definitions for each roster member.

          - `agents: array of BetaManagedAgentsSessionThreadAgent or BetaManagedAgentsAdvisor`

            Full `agent` definitions the coordinator may spawn as session threads.

            - `beta_managed_agents_session_thread_agent: object`

              Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

              - `id: string`

              - `description: string`

              - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

                - `name: string`

                - `type: "url"`

                - `url: string`

              - `model: object`

                Model identifier and configuration.

                - `id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string`

                  The model that will power your agent.

                  See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

                - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

                  How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

                - `inference_geo: optional string`

                  Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

                - `speed: optional "standard" or "fast"`

                  Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

              - `name: string`

              - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

                - `beta_managed_agents_anthropic_skill: object`

                  A resolved Anthropic-managed skill.

                  - `skill_id: string`

                  - `type: "anthropic"`

                  - `version: string`

                - `beta_managed_agents_custom_skill: object`

                  A resolved user-created custom skill.

                  - `skill_id: string`

                  - `type: "custom"`

                  - `version: string`

              - `system: string`

              - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

                - `beta_managed_agents_agent_toolset20260401: object`

                  - `configs: array of BetaManagedAgentsAgentToolConfig`

                    - `beta_managed_agents_bash_tool_config: object`

                      Configuration for the bash tool.

                      - `enabled: boolean`

                      - `name: "bash"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                        Permission policy for tool execution.

                        - `beta_managed_agents_always_allow_policy: object`

                          Tool calls are automatically approved without user confirmation.

                          - `type: "always_allow"`

                        - `beta_managed_agents_always_ask_policy: object`

                          Tool calls require user confirmation before execution.

                          - `type: "always_ask"`

                      - `type: "bash"`

                    - `beta_managed_agents_edit_tool_config: object`

                      Configuration for the edit tool.

                      - `enabled: boolean`

                      - `name: "edit"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                        Permission policy for tool execution.

                        - `beta_managed_agents_always_allow_policy: object`

                          Tool calls are automatically approved without user confirmation.

                        - `beta_managed_agents_always_ask_policy: object`

                          Tool calls require user confirmation before execution.

                      - `type: "edit"`

                    - `beta_managed_agents_read_tool_config: object`

                      Configuration for the read tool.

                      - `enabled: boolean`

                      - `name: "read"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                        Permission policy for tool execution.

                        - `beta_managed_agents_always_allow_policy: object`

                          Tool calls are automatically approved without user confirmation.

                        - `beta_managed_agents_always_ask_policy: object`

                          Tool calls require user confirmation before execution.

                      - `type: "read"`

                    - `beta_managed_agents_write_tool_config: object`

                      Configuration for the write tool.

                      - `enabled: boolean`

                      - `name: "write"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                        Permission policy for tool execution.

                        - `beta_managed_agents_always_allow_policy: object`

                          Tool calls are automatically approved without user confirmation.

                        - `beta_managed_agents_always_ask_policy: object`

                          Tool calls require user confirmation before execution.

                      - `type: "write"`

                    - `beta_managed_agents_glob_tool_config: object`

                      Configuration for the glob tool.

                      - `enabled: boolean`

                      - `name: "glob"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                        Permission policy for tool execution.

                        - `beta_managed_agents_always_allow_policy: object`

                          Tool calls are automatically approved without user confirmation.

                        - `beta_managed_agents_always_ask_policy: object`

                          Tool calls require user confirmation before execution.

                      - `type: "glob"`

                    - `beta_managed_agents_grep_tool_config: object`

                      Configuration for the grep tool.

                      - `enabled: boolean`

                      - `name: "grep"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                        Permission policy for tool execution.

                        - `beta_managed_agents_always_allow_policy: object`

                          Tool calls are automatically approved without user confirmation.

                        - `beta_managed_agents_always_ask_policy: object`

                          Tool calls require user confirmation before execution.

                      - `type: "grep"`

                    - `beta_managed_agents_web_fetch_tool_config: object`

                      Configuration for the web_fetch tool.

                      - `enabled: boolean`

                      - `name: "web_fetch"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                        Permission policy for tool execution.

                        - `beta_managed_agents_always_allow_policy: object`

                          Tool calls are automatically approved without user confirmation.

                        - `beta_managed_agents_always_ask_policy: object`

                          Tool calls require user confirmation before execution.

                      - `type: "web_fetch"`

                      - `allowed_domains: optional array of string`

                      - `blocked_domains: optional array of string`

                      - `max_content_tokens: optional number`

                        format: int32

                    - `beta_managed_agents_web_search_tool_config: object`

                      Configuration for the web_search tool.

                      - `enabled: boolean`

                      - `name: "web_search"`

                      - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                        Permission policy for tool execution.

                        - `beta_managed_agents_always_allow_policy: object`

                          Tool calls are automatically approved without user confirmation.

                        - `beta_managed_agents_always_ask_policy: object`

                          Tool calls require user confirmation before execution.

                      - `type: "web_search"`

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

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                  - `type: "agent_toolset_20260401"`

                - `beta_managed_agents_mcp_toolset: object`

                  - `configs: array of BetaManagedAgentsMCPToolConfig`

                    - `enabled: boolean`

                    - `name: string`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                  - `default_config: object`

                    Resolved default configuration for all tools from an MCP server.

                    - `enabled: boolean`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                  - `mcp_server_name: string`

                  - `type: "mcp_toolset"`

                - `beta_managed_agents_custom_tool: object`

                  A custom tool as returned in API responses.

                  - `description: string`

                  - `input_schema: object`

                    JSON Schema for custom tool input parameters.

                    - `type: "object"`

                    - `properties: optional map[unknown]`

                    - `required: optional array of string`

                  - `name: string`

                  - `type: "custom"`

              - `type: "agent"`

              - `version: number`

                format: int32

            - `beta_managed_agents_advisor: object`

              Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

              - `model: string`

                The advisor model id.

              - `type: "advisor"`

          - `type: "coordinator"`

        - `name: string`

        - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

          - `beta_managed_agents_anthropic_skill: object`

            A resolved Anthropic-managed skill.

          - `beta_managed_agents_custom_skill: object`

            A resolved user-created custom skill.

        - `system: string`

        - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

          - `beta_managed_agents_agent_toolset20260401: object`

          - `beta_managed_agents_mcp_toolset: object`

          - `beta_managed_agents_custom_tool: object`

            A custom tool as returned in API responses.

        - `type: "agent"`

        - `version: number`

          format: int32

      - `budget: optional object`

        A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

        - `max_list_cost: object`

          A monetary amount in a specific currency.

          - `amount: string`

            Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

          - `currency: "USD"`

            Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

        - `type: "limit"`

      - `metadata: optional map[string]`

        The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

      - `title: optional string`

        The session's new title. Present only when the update changed it.

    - `beta_managed_agents_system_message_event: object`

      A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

      - `id: string`

        Unique identifier for this event.

      - `content: array of BetaManagedAgentsSystemContentBlock`

        System content blocks. Text-only.

        - `text: string`

          The text content.

          minLength: 1

        - `type: "text"`

      - `type: "system.message"`

      - `processed_at: optional string`

        A timestamp in RFC 3339 format

        format: date-time

    - `beta_managed_agents_session_usage_event: object`

      Periodic snapshot of the session's cumulative usage and tracked list cost.

      - `id: string`

        Unique identifier for this event.

      - `processed_at: string`

        A timestamp in RFC 3339 format

        format: date-time

      - `type: "session.usage"`

      - `usage: object`

        Point-in-time snapshot of a session's cumulative usage.

        - `active_seconds: optional number`

          Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

          format: double

        - `cache_creation: optional object`

          Prompt-cache creation token usage broken down by cache lifetime.

          - `ephemeral_1h_input_tokens: optional number`

            Tokens used to create 1-hour ephemeral cache entries.

            format: int32

          - `ephemeral_5m_input_tokens: optional number`

            Tokens used to create 5-minute ephemeral cache entries.

            format: int32

        - `cache_read_input_tokens: optional number`

          Total tokens read from prompt cache.

          format: int32

        - `input_tokens: optional number`

          Total input tokens consumed across all turns.

          format: int32

        - `list_cost: optional object`

          A monetary amount in a specific currency.

          - `amount: string`

            Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

          - `currency: "USD"`

            Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

        - `output_tokens: optional number`

          Total output tokens generated across all turns.

          format: int32

        - `server_tool_use: optional object`

          Cumulative count of server-executed tool invocations, broken down by tool.

          - `web_fetch_requests: optional number`

            Number of server-executed web fetch requests.

            format: int32

          - `web_search_requests: optional number`

            Number of server-executed web search requests.

            format: int32

      - `budget: optional object`

        A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

        - `max_list_cost: object`

          A monetary amount in a specific currency.

        - `type: "limit"`

  - `next_page: optional string`

    Opaque cursor for the next page. Null when no more results.

#### Example

```bash
ant beta:sessions:threads:events list \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7 \
  --thread-id sthr_011CZkZVWa6oIjw0rgXZpnBt
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message",
      "processed_at": "2026-03-15T10:00:00Z"
    }
  ],
  "next_page": "next_page"
}
```

### Stream Session Thread Events

`$ ant beta:sessions:threads:events stream`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}/stream`

Stream Session Thread Events

#### Parameters

- `--session-id: string`

  Path param: Path parameter session_id

- `--thread-id: string`

  Path param: Path parameter thread_id

- `--event-delta: optional array of BetaManagedAgentsDeltaType`

  Query param: When set, this connection also receives streaming deltas (`event_start`, `event_delta`) while an event is being produced, before the event itself arrives. Deltas are best-effort; when the final event is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no final event — its terminal `span.model_request_end` closes the preview. Accepts one or more event types to preview and may be repeated: `agent.message` streams `content_delta` fragments; `agent.thinking` is start-only — a signal that the agent has begun extended thinking, concluded by the `agent.thinking` event itself. Only previews of the requested event types are sent.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

#### Returns

- `beta_managed_agents_stream_session_thread_events: BetaManagedAgentsUserMessageEvent or BetaManagedAgentsUserInterruptEvent or BetaManagedAgentsUserToolConfirmationEvent or 34 more`

  Server-sent event in a single thread's stream.

  - `beta_managed_agents_user_message_event: object`

    A user message event in the session conversation.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

      Array of content blocks comprising the user message.

      - `beta_managed_agents_text_block: object`

        Regular text content.

        - `text: string`

          The text content.

          minLength: 1

        - `type: "text"`

      - `beta_managed_agents_image_block: object`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `beta_managed_agents_base64_image_source: object`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

              minLength: 1

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

            - `type: "base64"`

          - `beta_managed_agents_url_image_source: object`

            Image referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the image to fetch.

              minLength: 1

          - `beta_managed_agents_file_image_source: object`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

            - `type: "file"`

        - `type: "image"`

      - `beta_managed_agents_document_block: object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `beta_managed_agents_base64_document_source: object`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

              minLength: 1

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

            - `type: "base64"`

          - `beta_managed_agents_plain_text_document_source: object`

            Plain text document content.

            - `data: string`

              The plain text content.

              minLength: 1

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

            - `type: "text"`

          - `beta_managed_agents_url_document_source: object`

            Document referenced by URL.

            - `type: "url"`

            - `url: string`

              URL of the document to fetch.

              minLength: 1

          - `beta_managed_agents_file_document_source: object`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

              minLength: 1

            - `type: "file"`

        - `type: "document"`

        - `context: optional string`

          Additional context about the document for the model.

        - `title: optional string`

          The title of the document.

      - `beta_managed_agents_redacted_block: object`

        Placeholder for content withheld by Anthropic model policy.

        - `type: "redacted"`

    - `type: "user.message"`

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

      format: date-time

  - `beta_managed_agents_user_interrupt_event: object`

    An interrupt event that pauses agent execution and returns control to the user.

    - `id: string`

      Unique identifier for this event.

    - `type: "user.interrupt"`

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: optional string`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `beta_managed_agents_user_tool_confirmation_event: object`

    A tool confirmation event that approves or denies a pending tool execution.

    - `id: string`

      Unique identifier for this event.

    - `result: "allow" or "deny"`

      UserToolConfirmationResult enum

      - `"allow"`

      - `"deny"`

    - `tool_use_id: string`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.tool_confirmation"`

    - `deny_message: optional string`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: optional string`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `beta_managed_agents_user_custom_tool_result_event: object`

    Event sent by the client providing the result of a custom tool execution.

    - `id: string`

      Unique identifier for this event.

    - `custom_tool_use_id: string`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.custom_tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `beta_managed_agents_text_block: object`

        Regular text content.

      - `beta_managed_agents_image_block: object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `beta_managed_agents_document_block: object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `beta_managed_agents_search_result_block: object`

        A block containing a web search result.

        - `citations: object`

          Citation settings for a search result.

          - `enabled: boolean`

            Whether citations are enabled for this search result.

        - `content: array of BetaManagedAgentsSearchResultContent`

          Array of text content blocks from the search result.

          - `text: string`

            The text content.

            minLength: 1

          - `type: "text"`

        - `source: string`

          The URL source of the search result.

          minLength: 1

        - `title: string`

          The title of the search result.

          minLength: 1

        - `type: "search_result"`

    - `is_error: optional boolean`

      Whether the tool execution resulted in an error.

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: optional string`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `beta_managed_agents_agent_custom_tool_use_event: object`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `name: string`

      Name of the custom tool being called.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.custom_tool_use"`

    - `session_thread_id: optional string`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `beta_managed_agents_agent_message_event: object`

    An agent response event in the session conversation.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsRedactedBlock`

      Array of text blocks comprising the agent response.

      - `beta_managed_agents_text_block: object`

        Regular text content.

      - `beta_managed_agents_redacted_block: object`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.message"`

  - `beta_managed_agents_agent_thinking_event: object`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.thinking"`

  - `beta_managed_agents_agent_mcp_tool_use_event: object`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `mcp_server_name: string`

      Name of the MCP server providing the tool.

    - `name: string`

      Name of the MCP tool being used.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.mcp_tool_use"`

    - `evaluated_permission: optional "allow" or "ask" or "deny"`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: optional string`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `beta_managed_agents_agent_mcp_tool_result_event: object`

    Event representing the result of an MCP tool execution.

    - `id: string`

      Unique identifier for this event.

    - `mcp_tool_use_id: string`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.mcp_tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `beta_managed_agents_text_block: object`

        Regular text content.

      - `beta_managed_agents_image_block: object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `beta_managed_agents_document_block: object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `beta_managed_agents_search_result_block: object`

        A block containing a web search result.

    - `is_error: optional boolean`

      Whether the tool execution resulted in an error.

  - `beta_managed_agents_agent_tool_use_event: object`

    Event emitted when the agent invokes a built-in agent tool.

    - `id: string`

      Unique identifier for this event.

    - `input: map[unknown]`

      Input parameters for the tool call.

    - `name: string`

      Name of the agent tool being used.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.tool_use"`

    - `evaluated_permission: optional "allow" or "ask" or "deny"`

      AgentEvaluatedPermission enum

      - `"allow"`

      - `"ask"`

      - `"deny"`

    - `session_thread_id: optional string`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `beta_managed_agents_agent_tool_result_event: object`

    Event representing the result of an agent tool execution.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to.

    - `type: "agent.tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `beta_managed_agents_text_block: object`

        Regular text content.

      - `beta_managed_agents_image_block: object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `beta_managed_agents_document_block: object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `beta_managed_agents_search_result_block: object`

        A block containing a web search result.

    - `is_error: optional boolean`

      Whether the tool execution resulted in an error.

  - `beta_managed_agents_agent_thread_message_received_event: object`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

      Message content blocks.

      - `beta_managed_agents_text_block: object`

        Regular text content.

      - `beta_managed_agents_image_block: object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `beta_managed_agents_document_block: object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `beta_managed_agents_redacted_block: object`

        Placeholder for content withheld by Anthropic model policy.

    - `from_session_thread_id: string`

      Public `sthr_` ID of the thread that sent the message.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.thread_message_received"`

    - `from_agent_name: optional string`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `beta_managed_agents_agent_thread_message_sent_event: object`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsRedactedBlock`

      Message content blocks.

      - `beta_managed_agents_text_block: object`

        Regular text content.

      - `beta_managed_agents_image_block: object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `beta_managed_agents_document_block: object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `beta_managed_agents_redacted_block: object`

        Placeholder for content withheld by Anthropic model policy.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `to_session_thread_id: string`

      Public `sthr_` ID of the thread the message was sent to.

    - `type: "agent.thread_message_sent"`

    - `to_agent_name: optional string`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `beta_managed_agents_agent_thread_context_compacted_event: object`

    Indicates that context compaction (summarization) occurred during the session.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "agent.thread_context_compacted"`

  - `beta_managed_agents_session_error_event: object`

    An error event indicating a problem occurred during session execution.

    - `id: string`

      Unique identifier for this event.

    - `error: BetaManagedAgentsUnknownError or BetaManagedAgentsModelOverloadedError or BetaManagedAgentsModelRateLimitedError or 5 more`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `beta_managed_agents_unknown_error: object`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `type: "retrying"`

          - `beta_managed_agents_retry_status_exhausted: object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `type: "exhausted"`

          - `beta_managed_agents_retry_status_terminal: object`

            The session encountered a terminal error and will transition to `terminated` state.

            - `type: "terminal"`

        - `type: "unknown_error"`

      - `beta_managed_agents_model_overloaded_error: object`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `beta_managed_agents_retry_status_exhausted: object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `beta_managed_agents_retry_status_terminal: object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "model_overloaded_error"`

      - `beta_managed_agents_model_rate_limited_error: object`

        The model request was rate-limited.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `beta_managed_agents_retry_status_exhausted: object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `beta_managed_agents_retry_status_terminal: object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "model_rate_limited_error"`

      - `beta_managed_agents_model_request_failed_error: object`

        A model request failed for a reason other than overload or rate-limiting.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `beta_managed_agents_retry_status_exhausted: object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `beta_managed_agents_retry_status_terminal: object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "model_request_failed_error"`

      - `beta_managed_agents_mcp_connection_failed_error: object`

        Failed to connect to an MCP server.

        - `mcp_server_name: string`

          Name of the MCP server that failed to connect.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `beta_managed_agents_retry_status_exhausted: object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `beta_managed_agents_retry_status_terminal: object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "mcp_connection_failed_error"`

      - `beta_managed_agents_mcp_authentication_failed_error: object`

        Authentication to an MCP server failed.

        - `mcp_server_name: string`

          Name of the MCP server that failed authentication.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `beta_managed_agents_retry_status_exhausted: object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `beta_managed_agents_retry_status_terminal: object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "mcp_authentication_failed_error"`

      - `beta_managed_agents_billing_error: object`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `beta_managed_agents_retry_status_exhausted: object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `beta_managed_agents_retry_status_terminal: object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "billing_error"`

      - `beta_managed_agents_credential_host_unreachable_error: object`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `credential_id: string`

          ID of the affected credential.

        - `message: string`

          Human-readable error description.

        - `retry_status: BetaManagedAgentsRetryStatusRetrying or BetaManagedAgentsRetryStatusExhausted or BetaManagedAgentsRetryStatusTerminal`

          What the client should do next in response to this error.

          - `beta_managed_agents_retry_status_retrying: object`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `beta_managed_agents_retry_status_exhausted: object`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `beta_managed_agents_retry_status_terminal: object`

            The session encountered a terminal error and will transition to `terminated` state.

        - `type: "credential_host_unreachable_error"`

        - `vault_id: string`

          ID of the vault containing the affected credential.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.error"`

  - `beta_managed_agents_session_status_rescheduled_event: object`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.status_rescheduled"`

  - `beta_managed_agents_session_status_running_event: object`

    Indicates the session is actively running and the agent is working.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.status_running"`

  - `beta_managed_agents_session_status_idle_event: object`

    Indicates the agent has paused and is awaiting user input.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted or BetaManagedAgentsSessionBudgetReached`

      The agent completed its turn naturally and is ready for the next user message.

      - `beta_managed_agents_session_end_turn: object`

        The agent completed its turn naturally and is ready for the next user message.

        - `type: "end_turn"`

      - `beta_managed_agents_session_requires_action: object`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `event_ids: array of string`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `type: "requires_action"`

      - `beta_managed_agents_session_retries_exhausted: object`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `type: "retries_exhausted"`

      - `beta_managed_agents_session_budget_reached: object`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `type: "budget_reached"`

    - `type: "session.status_idle"`

  - `beta_managed_agents_session_status_terminated_event: object`

    Indicates the session has terminated, either due to an error or completion.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.status_terminated"`

  - `beta_managed_agents_session_thread_created_event: object`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the callable agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public `sthr_` ID of the newly created thread.

    - `type: "session.thread_created"`

  - `beta_managed_agents_span_outcome_evaluation_start_event: object`

    Emitted when an outcome evaluation cycle begins.

    - `id: string`

      Unique identifier for this event.

    - `iteration: number`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

      format: int32

    - `outcome_id: string`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "span.outcome_evaluation_start"`

  - `beta_managed_agents_span_outcome_evaluation_end_event: object`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `id: string`

      Unique identifier for this event.

    - `explanation: string`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `iteration: number`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `outcome_evaluation_start_id: string`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `outcome_id: string`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `result: string`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `type: "span.outcome_evaluation_end"`

    - `usage: object`

      Token usage for a single model request.

      - `cache_creation_input_tokens: number`

        Tokens used to create prompt cache in this request.

        format: int32

      - `cache_read_input_tokens: number`

        Tokens read from prompt cache in this request.

        format: int32

      - `input_tokens: number`

        Input tokens consumed by this request.

        format: int32

      - `output_tokens: number`

        Output tokens generated by this request.

        format: int32

      - `speed: optional "standard" or "fast"`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

  - `beta_managed_agents_span_model_request_start_event: object`

    Emitted when a model request is initiated by the agent.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "span.model_request_start"`

  - `beta_managed_agents_span_model_request_end_event: object`

    Emitted when a model request completes.

    - `id: string`

      Unique identifier for this event.

    - `is_error: boolean`

      Whether the model request resulted in an error.

    - `model_request_start_id: string`

      The id of the corresponding `span.model_request_start` event.

    - `model_usage: object`

      Token usage for a single model request.

      - `cache_creation_input_tokens: number`

        Tokens used to create prompt cache in this request.

        format: int32

      - `cache_read_input_tokens: number`

        Tokens read from prompt cache in this request.

        format: int32

      - `input_tokens: number`

        Input tokens consumed by this request.

        format: int32

      - `output_tokens: number`

        Output tokens generated by this request.

        format: int32

      - `speed: optional "standard" or "fast"`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "span.model_request_end"`

  - `beta_managed_agents_span_outcome_evaluation_ongoing_event: object`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `id: string`

      Unique identifier for this event.

    - `iteration: number`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `outcome_id: string`

      The `outc_` ID of the outcome being evaluated.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "span.outcome_evaluation_ongoing"`

  - `beta_managed_agents_user_define_outcome_event: object`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `id: string`

      Unique identifier for this event.

    - `description: string`

      What the agent should produce. Copied from the input event.

    - `max_iterations: number`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

      format: int32

    - `outcome_id: string`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

      Rubric for grading the quality of an outcome.

      - `beta_managed_agents_file_rubric: object`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: string`

          ID of the rubric file.

        - `type: "file"`

      - `beta_managed_agents_text_rubric: object`

        Rubric content provided inline as text.

        - `content: string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `type: "text"`

    - `type: "user.define_outcome"`

  - `beta_managed_agents_session_deleted_event: object`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.deleted"`

  - `beta_managed_agents_session_thread_status_running_event: object`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that started running.

    - `type: "session.thread_status_running"`

  - `beta_managed_agents_session_thread_status_idle_event: object`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that went idle.

    - `stop_reason: BetaManagedAgentsSessionEndTurn or BetaManagedAgentsSessionRequiresAction or BetaManagedAgentsSessionRetriesExhausted or BetaManagedAgentsSessionBudgetReached`

      The agent completed its turn naturally and is ready for the next user message.

      - `beta_managed_agents_session_end_turn: object`

        The agent completed its turn naturally and is ready for the next user message.

      - `beta_managed_agents_session_requires_action: object`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `beta_managed_agents_session_retries_exhausted: object`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `beta_managed_agents_session_budget_reached: object`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

    - `type: "session.thread_status_idle"`

  - `beta_managed_agents_session_thread_status_terminated_event: object`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that terminated.

    - `type: "session.thread_status_terminated"`

  - `beta_managed_agents_user_tool_result_event: object`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `id: string`

      Unique identifier for this event.

    - `tool_use_id: string`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `type: "user.tool_result"`

    - `content: optional array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock or BetaManagedAgentsSearchResultBlock`

      The result content returned by the tool.

      - `beta_managed_agents_text_block: object`

        Regular text content.

      - `beta_managed_agents_image_block: object`

        Image content specified directly as base64 data or as a reference via a URL.

      - `beta_managed_agents_document_block: object`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `beta_managed_agents_search_result_block: object`

        A block containing a web search result.

    - `is_error: optional boolean`

      Whether the tool execution resulted in an error.

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: optional string`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `beta_managed_agents_session_thread_status_rescheduled_event: object`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `id: string`

      Unique identifier for this event.

    - `agent_name: string`

      Name of the agent the thread runs.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `session_thread_id: string`

      Public sthr_ ID of the thread that is retrying.

    - `type: "session.thread_status_rescheduled"`

  - `beta_managed_agents_session_updated_event: object`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.updated"`

    - `agent: optional object`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `id: string`

      - `description: string`

      - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

        - `name: string`

        - `type: "url"`

        - `url: string`

      - `model: object`

        Model identifier and configuration.

        - `id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

        - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

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

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `"standard"`

          - `"fast"`

      - `multiagent: object`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `agents: array of BetaManagedAgentsSessionThreadAgent or BetaManagedAgentsAdvisor`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `beta_managed_agents_session_thread_agent: object`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `id: string`

            - `description: string`

            - `mcp_servers: array of BetaManagedAgentsMCPServerURLDefinition`

              - `name: string`

              - `type: "url"`

              - `url: string`

            - `model: object`

              Model identifier and configuration.

              - `id: "claude-sonnet-5" or "claude-fable-5" or "claude-opus-5" or 10 more or string`

                The model that will power your agent.

                See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

              - `effort: optional BetaManagedAgentsEffortLow or BetaManagedAgentsEffortMedium or BetaManagedAgentsEffortHigh or 2 more`

                How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

              - `inference_geo: optional string`

                Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

              - `speed: optional "standard" or "fast"`

                Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

            - `name: string`

            - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

              - `beta_managed_agents_anthropic_skill: object`

                A resolved Anthropic-managed skill.

                - `skill_id: string`

                - `type: "anthropic"`

                - `version: string`

              - `beta_managed_agents_custom_skill: object`

                A resolved user-created custom skill.

                - `skill_id: string`

                - `type: "custom"`

                - `version: string`

            - `system: string`

            - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

              - `beta_managed_agents_agent_toolset20260401: object`

                - `configs: array of BetaManagedAgentsAgentToolConfig`

                  - `beta_managed_agents_bash_tool_config: object`

                    Configuration for the bash tool.

                    - `enabled: boolean`

                    - `name: "bash"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                        - `type: "always_allow"`

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                        - `type: "always_ask"`

                    - `type: "bash"`

                  - `beta_managed_agents_edit_tool_config: object`

                    Configuration for the edit tool.

                    - `enabled: boolean`

                    - `name: "edit"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                    - `type: "edit"`

                  - `beta_managed_agents_read_tool_config: object`

                    Configuration for the read tool.

                    - `enabled: boolean`

                    - `name: "read"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                    - `type: "read"`

                  - `beta_managed_agents_write_tool_config: object`

                    Configuration for the write tool.

                    - `enabled: boolean`

                    - `name: "write"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                    - `type: "write"`

                  - `beta_managed_agents_glob_tool_config: object`

                    Configuration for the glob tool.

                    - `enabled: boolean`

                    - `name: "glob"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                    - `type: "glob"`

                  - `beta_managed_agents_grep_tool_config: object`

                    Configuration for the grep tool.

                    - `enabled: boolean`

                    - `name: "grep"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                    - `type: "grep"`

                  - `beta_managed_agents_web_fetch_tool_config: object`

                    Configuration for the web_fetch tool.

                    - `enabled: boolean`

                    - `name: "web_fetch"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                    - `type: "web_fetch"`

                    - `allowed_domains: optional array of string`

                    - `blocked_domains: optional array of string`

                    - `max_content_tokens: optional number`

                      format: int32

                  - `beta_managed_agents_web_search_tool_config: object`

                    Configuration for the web_search tool.

                    - `enabled: boolean`

                    - `name: "web_search"`

                    - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                      Permission policy for tool execution.

                      - `beta_managed_agents_always_allow_policy: object`

                        Tool calls are automatically approved without user confirmation.

                      - `beta_managed_agents_always_ask_policy: object`

                        Tool calls require user confirmation before execution.

                    - `type: "web_search"`

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

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                - `type: "agent_toolset_20260401"`

              - `beta_managed_agents_mcp_toolset: object`

                - `configs: array of BetaManagedAgentsMCPToolConfig`

                  - `enabled: boolean`

                  - `name: string`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                - `default_config: object`

                  Resolved default configuration for all tools from an MCP server.

                  - `enabled: boolean`

                  - `permission_policy: BetaManagedAgentsAlwaysAllowPolicy or BetaManagedAgentsAlwaysAskPolicy`

                    Permission policy for tool execution.

                    - `beta_managed_agents_always_allow_policy: object`

                      Tool calls are automatically approved without user confirmation.

                    - `beta_managed_agents_always_ask_policy: object`

                      Tool calls require user confirmation before execution.

                - `mcp_server_name: string`

                - `type: "mcp_toolset"`

              - `beta_managed_agents_custom_tool: object`

                A custom tool as returned in API responses.

                - `description: string`

                - `input_schema: object`

                  JSON Schema for custom tool input parameters.

                  - `type: "object"`

                  - `properties: optional map[unknown]`

                  - `required: optional array of string`

                - `name: string`

                - `type: "custom"`

            - `type: "agent"`

            - `version: number`

              format: int32

          - `beta_managed_agents_advisor: object`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `model: string`

              The advisor model id.

            - `type: "advisor"`

        - `type: "coordinator"`

      - `name: string`

      - `skills: array of BetaManagedAgentsAnthropicSkill or BetaManagedAgentsCustomSkill`

        - `beta_managed_agents_anthropic_skill: object`

          A resolved Anthropic-managed skill.

        - `beta_managed_agents_custom_skill: object`

          A resolved user-created custom skill.

      - `system: string`

      - `tools: array of BetaManagedAgentsAgentToolset20260401 or BetaManagedAgentsMCPToolset or BetaManagedAgentsCustomTool`

        - `beta_managed_agents_agent_toolset20260401: object`

        - `beta_managed_agents_mcp_toolset: object`

        - `beta_managed_agents_custom_tool: object`

          A custom tool as returned in API responses.

      - `type: "agent"`

      - `version: number`

        format: int32

    - `budget: optional object`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `max_list_cost: object`

        A monetary amount in a specific currency.

        - `amount: string`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `currency: "USD"`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `type: "limit"`

    - `metadata: optional map[string]`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `title: optional string`

      The session's new title. Present only when the update changed it.

  - `beta_managed_agents_start_event: object`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `event: BetaManagedAgentsAgentMessagePreview or BetaManagedAgentsAgentThinkingPreview`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

      - `beta_managed_agents_agent_message_preview: object`

        - `id: string`

          The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

        - `type: "agent.message"`

      - `beta_managed_agents_agent_thinking_preview: object`

        - `id: string`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

        - `type: "agent.thinking"`

    - `type: "event_start"`

  - `beta_managed_agents_delta_event: object`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `delta: object`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `content: object`

        Regular text content.

        - `text: string`

          The text content.

          minLength: 1

        - `type: "text"`

      - `type: "content_delta"`

      - `index: optional number`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

        format: uint32

    - `event_id: string`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

    - `type: "event_delta"`

  - `beta_managed_agents_system_message_event: object`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsSystemContentBlock`

      System content blocks. Text-only.

      - `text: string`

        The text content.

        minLength: 1

      - `type: "text"`

    - `type: "system.message"`

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

      format: date-time

  - `beta_managed_agents_session_usage_event: object`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `id: string`

      Unique identifier for this event.

    - `processed_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `type: "session.usage"`

    - `usage: object`

      Point-in-time snapshot of a session's cumulative usage.

      - `active_seconds: optional number`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `cache_creation: optional object`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `ephemeral_1h_input_tokens: optional number`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `ephemeral_5m_input_tokens: optional number`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `cache_read_input_tokens: optional number`

        Total tokens read from prompt cache.

        format: int32

      - `input_tokens: optional number`

        Total input tokens consumed across all turns.

        format: int32

      - `list_cost: optional object`

        A monetary amount in a specific currency.

        - `amount: string`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `currency: "USD"`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `output_tokens: optional number`

        Total output tokens generated across all turns.

        format: int32

      - `server_tool_use: optional object`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `web_fetch_requests: optional number`

          Number of server-executed web fetch requests.

          format: int32

        - `web_search_requests: optional number`

          Number of server-executed web search requests.

          format: int32

    - `budget: optional object`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `max_list_cost: object`

        A monetary amount in a specific currency.

      - `type: "limit"`

- `beta_managed_agents_stream_session_thread_events: BetaManagedAgentsUserMessageEvent or BetaManagedAgentsUserInterruptEvent or BetaManagedAgentsUserToolConfirmationEvent or 34 more`

  Server-sent event in a single thread's stream.

  - `beta_managed_agents_user_message_event: object`

    A user message event in the session conversation.

  - `beta_managed_agents_user_interrupt_event: object`

    An interrupt event that pauses agent execution and returns control to the user.

  - `beta_managed_agents_user_tool_confirmation_event: object`

    A tool confirmation event that approves or denies a pending tool execution.

  - `beta_managed_agents_user_custom_tool_result_event: object`

    Event sent by the client providing the result of a custom tool execution.

  - `beta_managed_agents_agent_custom_tool_use_event: object`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

  - `beta_managed_agents_agent_message_event: object`

    An agent response event in the session conversation.

  - `beta_managed_agents_agent_thinking_event: object`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

  - `beta_managed_agents_agent_mcp_tool_use_event: object`

    Event emitted when the agent invokes a tool provided by an MCP server.

  - `beta_managed_agents_agent_mcp_tool_result_event: object`

    Event representing the result of an MCP tool execution.

  - `beta_managed_agents_agent_tool_use_event: object`

    Event emitted when the agent invokes a built-in agent tool.

  - `beta_managed_agents_agent_tool_result_event: object`

    Event representing the result of an agent tool execution.

  - `beta_managed_agents_agent_thread_message_received_event: object`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

  - `beta_managed_agents_agent_thread_message_sent_event: object`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

  - `beta_managed_agents_agent_thread_context_compacted_event: object`

    Indicates that context compaction (summarization) occurred during the session.

  - `beta_managed_agents_session_error_event: object`

    An error event indicating a problem occurred during session execution.

  - `beta_managed_agents_session_status_rescheduled_event: object`

    Indicates the session is recovering from an error state and is rescheduled for execution.

  - `beta_managed_agents_session_status_running_event: object`

    Indicates the session is actively running and the agent is working.

  - `beta_managed_agents_session_status_idle_event: object`

    Indicates the agent has paused and is awaiting user input.

  - `beta_managed_agents_session_status_terminated_event: object`

    Indicates the session has terminated, either due to an error or completion.

  - `beta_managed_agents_session_thread_created_event: object`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

  - `beta_managed_agents_span_outcome_evaluation_start_event: object`

    Emitted when an outcome evaluation cycle begins.

  - `beta_managed_agents_span_outcome_evaluation_end_event: object`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

  - `beta_managed_agents_span_model_request_start_event: object`

    Emitted when a model request is initiated by the agent.

  - `beta_managed_agents_span_model_request_end_event: object`

    Emitted when a model request completes.

  - `beta_managed_agents_span_outcome_evaluation_ongoing_event: object`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

  - `beta_managed_agents_user_define_outcome_event: object`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

  - `beta_managed_agents_session_deleted_event: object`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

  - `beta_managed_agents_session_thread_status_running_event: object`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

  - `beta_managed_agents_session_thread_status_idle_event: object`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

  - `beta_managed_agents_session_thread_status_terminated_event: object`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

  - `beta_managed_agents_user_tool_result_event: object`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

  - `beta_managed_agents_session_thread_status_rescheduled_event: object`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

  - `beta_managed_agents_session_updated_event: object`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

  - `beta_managed_agents_start_event: object`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

  - `beta_managed_agents_delta_event: object`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

  - `beta_managed_agents_system_message_event: object`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

  - `beta_managed_agents_session_usage_event: object`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

#### Example

```bash
ant beta:sessions:threads:events stream \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7 \
  --thread-id sthr_011CZkZVWa6oIjw0rgXZpnBt
```

##### Response (200)

```json
{
  "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
  "content": [
    {
      "text": "Where is my order #1234?",
      "type": "text"
    }
  ],
  "type": "user.message",
  "processed_at": "2026-03-15T10:00:00Z"
}
```
