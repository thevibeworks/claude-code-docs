---
title: Stop Work
url: https://platform.claude.com/docs/en/api/java/beta/environments/work/stop
---

# Stop Work

`BetaSelfHostedWork beta().environments().work().stop(params, requestOptions = RequestOptions.none())`

**POST** `/v1/environments/{environment_id}/work/{work_id}/stop`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Stop a work item, initiating graceful or forced shutdown.

## Parameters

- `WorkStopParams params`

  - `String environmentId` (path parameter)

  - `Optional<String> workId` (path parameter)

  - `Optional<List<AnthropicBeta>> betas` (header parameter)

    Optional header to specify the beta version(s) you want to use.

    - `COMPUTER_USE_2024_10_22("computer-use-2024-10-22")`

    - `COMPUTER_USE_2025_01_24("computer-use-2025-01-24")`

    - `OUTPUT_128K_2025_02_19("output-128k-2025-02-19")`

    - `MCP_CLIENT_2025_04_04("mcp-client-2025-04-04")`

    - `MCP_CLIENT_2025_11_20("mcp-client-2025-11-20")`

    - `DEV_FULL_THINKING_2025_05_14("dev-full-thinking-2025-05-14")`

    - `INTERLEAVED_THINKING_2025_05_14("interleaved-thinking-2025-05-14")`

    - `CODE_EXECUTION_2025_05_22("code-execution-2025-05-22")`

    - `CONTEXT_1M_2025_08_07("context-1m-2025-08-07")`

    - `CONTEXT_MANAGEMENT_2025_06_27("context-management-2025-06-27")`

    - `MODEL_CONTEXT_WINDOW_EXCEEDED_2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `FAST_MODE_2026_02_01("fast-mode-2026-02-01")`

    - `OUTPUT_300K_2026_03_24("output-300k-2026-03-24")`

    - `USER_PROFILES_2026_03_24("user-profiles-2026-03-24")`

    - `USER_PROFILES_2026_08_18("user-profiles-2026-08-18")`

    - `USER_PROFILES_2026_09_04("user-profiles-2026-09-04")`

    - `ADVISOR_TOOL_2026_03_01("advisor-tool-2026-03-01")`

    - `MANAGED_AGENTS_2026_04_01("managed-agents-2026-04-01")`

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

    - `MID_CONVERSATION_OUTPUT_CONFIG_2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `THINKING_BINDING_CONTROLS_2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MID_CONVERSATION_SYSTEM_CLEAR_AT_2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

    - `COMPACT_2026_09_04("compact-2026-09-04")`

    - `INLINE_TOOLS_2026_09_15("inline-tools-2026-09-15")`

    - `MCP_CLIENT_2026_09_15("mcp-client-2026-09-15")`

    - `CE_PLUGINS_2026_09_01("ce-plugins-2026-09-01")`

    - `SPEND_LIMIT_READS_2026_09_26("spend-limit-reads-2026-09-26")`

    - `TELEMETRY_DESTINATIONS_2026_08_11("telemetry-destinations-2026-08-11")`

    - `WEBHOOKS_2026_10_07("webhooks-2026-10-07")`

    - `ADMIN_USER_SIGN_OUT_2026_10_08("admin-user-sign-out-2026-10-08")`

    - `MESSAGE_THREADS_2026_08_12("message-threads-2026-08-12")`

    - `ANALYTICS_USAGE_COST_2026_08_24("analytics-usage-cost-2026-08-24")`

    - `EXPERIMENTAL_CLAUDE_TAG_2026_10_21("experimental-claude-tag-2026-10-21")`

    - `MESSAGE_BATCHES_2024_09_24("message-batches-2024-09-24")`

      **Deprecated**: This value is no longer needed. Remove it from your requests.

    - `PROMPT_CACHING_2024_07_31("prompt-caching-2024-07-31")`

      **Deprecated**: This value is no longer needed. Remove it from your requests.

    - `PDFS_2024_09_25("pdfs-2024-09-25")`

      **Deprecated**: This value is no longer needed. Remove it from your requests.

    - `TOKEN_COUNTING_2024_11_01("token-counting-2024-11-01")`

      **Deprecated**: This value is no longer needed. Remove it from your requests.

    - `TOKEN_EFFICIENT_TOOLS_2025_02_19("token-efficient-tools-2025-02-19")`

      **Deprecated**: This value is no longer needed. Remove it from your requests.

    - `FILES_API_2025_04_14("files-api-2025-04-14")`

      **Deprecated**: Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/files#migrate-from-files-api-2025-04-14

    - `EXTENDED_CACHE_TTL_2025_04_11("extended-cache-ttl-2025-04-11")`

      **Deprecated**: This value is no longer needed. Remove it from your requests.

    - `SKILLS_2025_10_02("skills-2025-10-02")`

      **Deprecated**: Sending this value selects the beta response shapes. Removing it moves you to the current shapes, so follow the migration steps: https://platform.claude.com/docs/en/build-with-claude/skills-guide#migrate-from-skills-2025-10-02

    - `CACHE_DIAGNOSIS_2026_04_07("cache-diagnosis-2026-04-07")`

      **Deprecated**: This value is no longer needed. Remove it from your requests.

    - `CE_USER_MANAGEMENT_2026_07_13("ce-user-management-2026-07-13")`

      **Deprecated**: This value is no longer needed. Remove it from your requests.

  - `Optional<String> workspaceId` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

  - `BetaSelfHostedWorkStopRequest betaSelfHostedWorkStopRequest`

    Request to stop a work item.

## Returns

- `class BetaSelfHostedWork`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `JsonValue type = "work"`

    The type of object (always 'work')

  - `String id`

    Work identifier (e.g., 'work_...')

  - `Optional<String> acknowledgedAt`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `String createdAt`

    RFC 3339 timestamp when work was created

  - `BetaSessionWorkData data`

    The actual work to be performed

    - `JsonValue type = "session"`

      Type of work data

    - `String id`

      Session identifier (e.g., 'session_...')

  - `String environmentId`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `Optional<String> latestHeartbeatAt`

    RFC 3339 timestamp of the most recent heartbeat

  - `Metadata metadata`

    User-provided metadata key-value pairs associated with this work item

  - `Optional<String> secret`

    Credential payload used by the environment worker to execute this work item. May be populated when polling for work; null on all other retrieval paths.

  - `Optional<String> startedAt`

    RFC 3339 timestamp when work execution started

  - `State state`

    Current state of the work item

    - `QUEUED("queued")`

    - `STARTING("starting")`

    - `ACTIVE("active")`

    - `STOPPING("stopping")`

    - `STOPPED("stopped")`

  - `Optional<String> stopRequestedAt`

    RFC 3339 timestamp when stop was requested

  - `Optional<String> stoppedAt`

    RFC 3339 timestamp when work execution stopped

## Errors

Any method can also return the general [HTTP errors](https://platform.claude.com/docs/en/api/errors?sdk_languages=java).

- `ClaudeCodeKeyCreatorNotMemberException` (HTTP status 400, error code `claude_code_key_creator_not_member`)

  The API key belongs to the Claude Code workspace, and the user who created it is no longer a member of the organization or of that workspace.

- `OrganizationOnHoldException` (HTTP status 400, error code `organization_on_hold`)

  Anthropic has disabled the organization for trust and safety reasons. An organization disabled for any other reason, such as billing, does not get this code. `appeal_url`, when present, is where the organization can appeal.

## Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.environments.work.BetaSelfHostedWork;
import com.anthropic.models.beta.environments.work.BetaSelfHostedWorkStopRequest;
import com.anthropic.models.beta.environments.work.WorkStopParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        WorkStopParams params = WorkStopParams.builder()
            .environmentId("env_011CZkZ9X2dpNyB7HsEFoRfW")
            .workId("work_id")
            .betaSelfHostedWorkStopRequest(BetaSelfHostedWorkStopRequest.builder().build())
            .build();
        BetaSelfHostedWork betaSelfHostedWork = client.beta().environments().work().stop(params);
    }
}
```

### Response (200)

```json
{
  "id": "id",
  "acknowledged_at": "acknowledged_at",
  "created_at": "created_at",
  "data": {
    "id": "id",
    "type": "session"
  },
  "environment_id": "environment_id",
  "latest_heartbeat_at": "latest_heartbeat_at",
  "metadata": {
    "foo": "string"
  },
  "secret": "secret",
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"
}
```
