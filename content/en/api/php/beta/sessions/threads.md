---
title: Threads
url: https://platform.claude.com/docs/en/api/php/beta/sessions/threads
---

# Threads

## List Session Threads

`$client->beta->sessions->threads->list(string sessionID, ?int limit, ?string page, ?list<AnthropicBeta> betas, ?string workspaceID): PageCursor<ManagedAgentsSessionThread>`

**GET** `/v1/sessions/{session_id}/threads`

List Session Threads

### Parameters

- `sessionID: string`

- `limit?:optional int`

  Maximum results per page. Defaults to 1000.

- `page?:optional string`

  Opaque pagination cursor from a previous response's `next_page`. Forward-only.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class ManagedAgentsSessionThread`

  - `Type type`

  - `string id`

    Unique identifier for this thread.

  - `Agent agent`

    Resolved agent definition for this thread. Snapshot of the agent at thread creation time.

  - `?\Datetime archivedAt`

    When the thread was archived. Null if not archived.

  - `\Datetime createdAt`

    When the thread was created.

  - `?string parentThreadID`

    Parent thread that spawned this thread. Null for the primary thread.

  - `string sessionID`

    The session this thread belongs to.

  - `?ManagedAgentsSessionThreadStats stats`

    Timing statistics for this thread. Null until the thread's first status transition.

  - `ManagedAgentsSessionThreadStatus status`

    Current execution status of the thread.

  - `\Datetime updatedAt`

    When the thread was last updated.

  - `?ManagedAgentsSessionThreadUsage usage`

    Cumulative token usage for this thread. Null until the thread's first idle transition.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->sessions->threads->list(
  'sesn_011CZkZAtmR3yMPDzynEDxu7',
  limit: 0,
  page: 'page',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($page);
```

#### Response (200)

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

## Get Session Thread

`$client->beta->sessions->threads->retrieve(string threadID, string sessionID, ?list<AnthropicBeta> betas, ?string workspaceID): ManagedAgentsSessionThread`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}`

Get Session Thread

### Parameters

- `sessionID: string`

- `threadID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class ManagedAgentsSessionThread`

  - `Type type`

  - `string id`

    Unique identifier for this thread.

  - `Agent agent`

    Resolved agent definition for this thread. Snapshot of the agent at thread creation time.

  - `?\Datetime archivedAt`

    When the thread was archived. Null if not archived.

  - `\Datetime createdAt`

    When the thread was created.

  - `?string parentThreadID`

    Parent thread that spawned this thread. Null for the primary thread.

  - `string sessionID`

    The session this thread belongs to.

  - `?ManagedAgentsSessionThreadStats stats`

    Timing statistics for this thread. Null until the thread's first status transition.

  - `ManagedAgentsSessionThreadStatus status`

    Current execution status of the thread.

  - `\Datetime updatedAt`

    When the thread was last updated.

  - `?ManagedAgentsSessionThreadUsage usage`

    Cumulative token usage for this thread. Null until the thread's first idle transition.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsSessionThread = $client->beta->sessions->threads->retrieve(
  'sthr_011CZkZVWa6oIjw0rgXZpnBt',
  sessionID: 'sesn_011CZkZAtmR3yMPDzynEDxu7',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsSessionThread);
```

#### Response (200)

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

## Archive Session Thread

`$client->beta->sessions->threads->archive(string threadID, string sessionID, ?list<AnthropicBeta> betas, ?string workspaceID): ManagedAgentsSessionThread`

**POST** `/v1/sessions/{session_id}/threads/{thread_id}/archive`

Archive Session Thread

### Parameters

- `sessionID: string`

- `threadID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class ManagedAgentsSessionThread`

  - `Type type`

  - `string id`

    Unique identifier for this thread.

  - `Agent agent`

    Resolved agent definition for this thread. Snapshot of the agent at thread creation time.

  - `?\Datetime archivedAt`

    When the thread was archived. Null if not archived.

  - `\Datetime createdAt`

    When the thread was created.

  - `?string parentThreadID`

    Parent thread that spawned this thread. Null for the primary thread.

  - `string sessionID`

    The session this thread belongs to.

  - `?ManagedAgentsSessionThreadStats stats`

    Timing statistics for this thread. Null until the thread's first status transition.

  - `ManagedAgentsSessionThreadStatus status`

    Current execution status of the thread.

  - `\Datetime updatedAt`

    When the thread was last updated.

  - `?ManagedAgentsSessionThreadUsage usage`

    Cumulative token usage for this thread. Null until the thread's first idle transition.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsSessionThread = $client->beta->sessions->threads->archive(
  'sthr_011CZkZVWa6oIjw0rgXZpnBt',
  sessionID: 'sesn_011CZkZAtmR3yMPDzynEDxu7',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsSessionThread);
```

#### Response (200)

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

## Domain types

### Beta Managed Agents Session Thread

- `class ManagedAgentsSessionThread`

  - `Type type`

  - `string id`

    Unique identifier for this thread.

  - `Agent agent`

    Resolved agent definition for this thread. Snapshot of the agent at thread creation time.

  - `?\Datetime archivedAt`

    When the thread was archived. Null if not archived.

  - `\Datetime createdAt`

    When the thread was created.

  - `?string parentThreadID`

    Parent thread that spawned this thread. Null for the primary thread.

  - `string sessionID`

    The session this thread belongs to.

  - `?ManagedAgentsSessionThreadStats stats`

    Timing statistics for this thread. Null until the thread's first status transition.

  - `ManagedAgentsSessionThreadStatus status`

    Current execution status of the thread.

  - `\Datetime updatedAt`

    When the thread was last updated.

  - `?ManagedAgentsSessionThreadUsage usage`

    Cumulative token usage for this thread. Null until the thread's first idle transition.

### Beta Managed Agents Session Thread Stats

- `class ManagedAgentsSessionThreadStats`

  - `?float activeSeconds`

    Cumulative time in seconds the thread spent actively running. Excludes idle time.

  - `?float durationSeconds`

    Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

  - `?float startupSeconds`

    Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

### Beta Managed Agents Session Thread Status

- `enum ManagedAgentsSessionThreadStatus`

  - `"running"`

  - `"idle"`

  - `"rescheduling"`

  - `"terminated"`

### Beta Managed Agents Session Thread Usage

- `class ManagedAgentsSessionThreadUsage`

  - `?float activeSeconds`

    Cumulative time in seconds this thread spent in running status. Equal to `stats.active_seconds`; surfaced here so a thread's usage carries every quantity its cost is priced on.

  - `?BetaManagedAgentsCacheCreationUsage cacheCreation`

    Tokens used to create prompt cache entries, broken down by cache TTL.

  - `?int cacheReadInputTokens`

    Total tokens read from prompt cache.

  - `?int inputTokens`

    Total input tokens consumed across all turns.

  - `?BetaMonetaryAmount listCost`

    Cumulative list cost of this thread across all turns, priced at public list rates. Absent until cost tracking is available for the thread. Each figure is rounded to the nearest cent independently and the session's aggregate `usage.list_cost` additionally includes session runtime, so per-thread costs do not sum exactly to the session figure; the session figure is authoritative and is what a budget is enforced against.

  - `?int outputTokens`

    Total output tokens generated across all turns.

  - `?BetaManagedAgentsServerToolUsage serverToolUse`

    Cumulative server-executed tool usage across all turns of this thread. Absent until server-tool tracking is available for the thread.

### Beta Managed Agents Stream Session Thread Events

- `class ManagedAgentsStreamSessionThreadEvents`

  - `class ManagedAgentsUserMessageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Array of content blocks comprising the user message.

    - `?\Datetime processedAt`

      Timestamp when the agent finished processing this message.

  - `class ManagedAgentsUserInterruptEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `?\Datetime processedAt`

      Timestamp when the interrupt was processed.

    - `?string sessionThreadID`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class ManagedAgentsUserToolConfirmationEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `Result result`

      The confirmation result: 'allow' or 'deny'.

    - `string toolUseID`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `?string denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `?\Datetime processedAt`

      Timestamp when the confirmation was processed.

    - `?string sessionThreadID`

      Set by the server to the subagent thread this confirmation was routed to. Omitted when it was routed to the primary thread.

  - `class ManagedAgentsUserCustomToolResultEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string customToolUseID`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

    - `?\Datetime processedAt`

      Timestamp when this result was processed.

    - `?string sessionThreadID`

      Set by the server to the subagent thread this result was routed to. Omitted when it was routed to the primary thread.

  - `class ManagedAgentsAgentCustomToolUseEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string name`

      Name of the custom tool being called.

    - `\Datetime processedAt`

      Timestamp when this tool use was processed.

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.custom_tool_result` by `custom_tool_use_id`, so clients do not send it back.

  - `class ManagedAgentsAgentMessageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Array of text blocks comprising the agent response.

    - `\Datetime processedAt`

      Timestamp when this response was generated.

  - `class ManagedAgentsAgentThinkingEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when this thinking was produced.

  - `class ManagedAgentsAgentMCPToolUseEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string mcpServerName`

      Name of the MCP server providing the tool.

    - `string name`

      Name of the MCP tool being used.

    - `\Datetime processedAt`

      Timestamp when this event was processed.

    - `?ManagedAgentsAgentEvaluatedPermission evaluatedPermission`

      The evaluated permission policy for this tool invocation.

    - `?ManagedAgentsAgentToolEvaluation evaluation`

      Which resolved permission_policy produced evaluated_permission: always_allow, always_ask, or auto (with the server's per-invocation judgement). Absent only when the server refused the call before any policy applied (for example, the named tool is not enabled in the session); such a refusal has evaluated_permission deny. An event recorded before this field existed reads as the arm its evaluated_permission implies (always_allow for allow, always_ask for ask).

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.tool_confirmation` by `tool_use_id`, so clients do not send it back.

  - `class ManagedAgentsAgentMCPToolResultEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string mcpToolUseID`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `\Datetime processedAt`

      Timestamp when this event was processed.

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `class ManagedAgentsAgentToolUseEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string name`

      Name of the agent tool being used.

    - `\Datetime processedAt`

      Timestamp when this event was processed.

    - `?ManagedAgentsAgentEvaluatedPermission evaluatedPermission`

      The evaluated permission policy for this tool invocation.

    - `?ManagedAgentsAgentToolEvaluation evaluation`

      Which resolved permission_policy produced evaluated_permission: always_allow, always_ask, or auto (with the server's per-invocation judgement). Absent only when the server refused the call before any policy applied (for example, the named tool is not enabled in the session); such a refusal has evaluated_permission deny. An event recorded before this field existed reads as the arm its evaluated_permission implies (always_allow for allow, always_ask for ask).

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.tool_confirmation` or `user.tool_result` by `tool_use_id`, so clients do not send it back.

  - `class ManagedAgentsAgentToolResultEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when this event was processed.

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to.

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `class ManagedAgentsAgentThreadMessageReceivedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `string fromSessionThreadID`

      Public `sthr_` ID of the thread that sent the message.

    - `\Datetime processedAt`

      Timestamp when the message was received.

    - `?string fromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class ManagedAgentsAgentThreadMessageSentEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `\Datetime processedAt`

      Timestamp when the message was sent.

    - `string toSessionThreadID`

      Public `sthr_` ID of the thread the message was sent to.

    - `?string toAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class ManagedAgentsAgentThreadContextCompactedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when compaction was processed.

  - `class ManagedAgentsSessionErrorEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `Error error`

    - `\Datetime processedAt`

      Timestamp when the error occurred.

  - `class ManagedAgentsSessionStatusRescheduledEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp of status change.

  - `class ManagedAgentsSessionStatusRunningEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp of status change.

  - `class ManagedAgentsSessionStatusIdleEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp of status change.

    - `StopReason stopReason`

  - `class ManagedAgentsSessionStatusTerminatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp of status change.

  - `class ManagedAgentsSessionThreadCreatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the callable agent the thread runs.

    - `\Datetime processedAt`

      Timestamp when the thread was created.

    - `string sessionThreadID`

      Public `sthr_` ID of the newly created thread.

  - `class ManagedAgentsSpanOutcomeEvaluationStartEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      Timestamp when outcome evaluation started.

  - `class ManagedAgentsSpanOutcomeEvaluationEndEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string explanation`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeEvaluationStartID`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      Timestamp when outcome evaluation ended.

    - `string result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `ManagedAgentsSpanModelUsage usage`

      Aggregate token usage for this evaluation cycle. Sums across all grader model requests within the cycle.

  - `class ManagedAgentsSpanModelRequestStartEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when the model request started.

  - `class ManagedAgentsSpanModelRequestEndEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `?bool isError`

      Whether the model request resulted in an error.

    - `string modelRequestStartID`

      The id of the corresponding `span.model_request_start` event.

    - `ManagedAgentsSpanModelUsage modelUsage`

      Token usage for this model request.

    - `\Datetime processedAt`

      Timestamp when the model request completed.

  - `class ManagedAgentsSpanOutcomeEvaluationOngoingEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      Timestamp when this heartbeat was emitted.

  - `class ManagedAgentsUserDefineOutcomeEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string description`

      What the agent should produce. Copied from the input event.

    - `?int maxIterations`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `string outcomeID`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `\Datetime processedAt`

      Timestamp when the outcome was accepted.

    - `Rubric rubric`

      How to grade the outcome. File rubrics are currently resolved to their text content; clients should handle both variants.

  - `class ManagedAgentsSessionDeletedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when the session was deleted.

  - `class ManagedAgentsSessionThreadStatusRunningEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      Timestamp of the status transition.

    - `string sessionThreadID`

      Public sthr_ ID of the thread that started running.

  - `class ManagedAgentsSessionThreadStatusIdleEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      Timestamp of the status transition.

    - `string sessionThreadID`

      Public sthr_ ID of the thread that went idle.

    - `StopReason stopReason`

  - `class ManagedAgentsSessionThreadStatusTerminatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      Timestamp of the status transition.

    - `string sessionThreadID`

      Public sthr_ ID of the thread that terminated.

  - `class BetaManagedAgentsUserToolResultEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

    - `?\Datetime processedAt`

      Timestamp when this result was processed.

    - `?string sessionThreadID`

      Set by the server to the subagent thread this result was routed to. Omitted when it was routed to the primary thread.

  - `class ManagedAgentsSessionThreadStatusRescheduledEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      Timestamp of the status transition.

    - `string sessionThreadID`

      Public sthr_ ID of the thread that is retrying.

  - `class BetaManagedAgentsSessionUpdatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when the update was applied.

    - `?BetaManagedAgentsSessionAgent agent`

      The session's effective agent configuration after the update. Present only when the update changed `agent` (tools or mcp_servers); when present it is the full materialised snapshot, not a diff.

    - `?BetaManagedAgentsBudgetLimit budget`

      The session's budget after the update: the new budget when set or replaced, or null when the update removed it. Present only when the update changed the budget.

    - `?array<string,string> metadata`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `?string title`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsStartEvent`

    - `Type type`

    - `BetaManagedAgentsStartEventPreview event`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

  - `class BetaManagedAgentsDeltaEvent`

    - `Type type`

    - `BetaManagedAgentsDeltaContent delta`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

    - `string eventID`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

  - `class BetaManagedAgentsSystemMessageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<BetaManagedAgentsSystemContentBlock> content`

      System content blocks. Text-only.

    - `?\Datetime processedAt`

      Timestamp when this system message was processed.

  - `class BetaManagedAgentsSessionUsageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when the snapshot was taken.

    - `ManagedAgentsSessionUsageSnapshot usage`

      The session's cumulative usage at the snapshot time.

    - `?BetaManagedAgentsBudgetLimit budget`

      The session's configured budget at the snapshot time, or null when the session has no budget.

## Threads › Events

### List Session Thread Events

`$client->beta->sessions->threads->events->list(string threadID, string sessionID, ?int limit, ?string page, ?list<AnthropicBeta> betas, ?string workspaceID): PageCursor<ManagedAgentsSessionEvent>`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}/events`

List Session Thread Events

#### Parameters

- `sessionID: string`

- `threadID: string`

- `limit?:optional int`

- `page?:optional string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class ManagedAgentsSessionEvent`

  - `class ManagedAgentsUserMessageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Array of content blocks comprising the user message.

    - `?\Datetime processedAt`

      Timestamp when the agent finished processing this message.

  - `class ManagedAgentsUserInterruptEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `?\Datetime processedAt`

      Timestamp when the interrupt was processed.

    - `?string sessionThreadID`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class ManagedAgentsUserToolConfirmationEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `Result result`

      The confirmation result: 'allow' or 'deny'.

    - `string toolUseID`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `?string denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `?\Datetime processedAt`

      Timestamp when the confirmation was processed.

    - `?string sessionThreadID`

      Set by the server to the subagent thread this confirmation was routed to. Omitted when it was routed to the primary thread.

  - `class ManagedAgentsUserCustomToolResultEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string customToolUseID`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

    - `?\Datetime processedAt`

      Timestamp when this result was processed.

    - `?string sessionThreadID`

      Set by the server to the subagent thread this result was routed to. Omitted when it was routed to the primary thread.

  - `class ManagedAgentsAgentCustomToolUseEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string name`

      Name of the custom tool being called.

    - `\Datetime processedAt`

      Timestamp when this tool use was processed.

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.custom_tool_result` by `custom_tool_use_id`, so clients do not send it back.

  - `class ManagedAgentsAgentMessageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Array of text blocks comprising the agent response.

    - `\Datetime processedAt`

      Timestamp when this response was generated.

  - `class ManagedAgentsAgentThinkingEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when this thinking was produced.

  - `class ManagedAgentsAgentMCPToolUseEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string mcpServerName`

      Name of the MCP server providing the tool.

    - `string name`

      Name of the MCP tool being used.

    - `\Datetime processedAt`

      Timestamp when this event was processed.

    - `?ManagedAgentsAgentEvaluatedPermission evaluatedPermission`

      The evaluated permission policy for this tool invocation.

    - `?ManagedAgentsAgentToolEvaluation evaluation`

      Which resolved permission_policy produced evaluated_permission: always_allow, always_ask, or auto (with the server's per-invocation judgement). Absent only when the server refused the call before any policy applied (for example, the named tool is not enabled in the session); such a refusal has evaluated_permission deny. An event recorded before this field existed reads as the arm its evaluated_permission implies (always_allow for allow, always_ask for ask).

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.tool_confirmation` by `tool_use_id`, so clients do not send it back.

  - `class ManagedAgentsAgentMCPToolResultEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string mcpToolUseID`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `\Datetime processedAt`

      Timestamp when this event was processed.

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `class ManagedAgentsAgentToolUseEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string name`

      Name of the agent tool being used.

    - `\Datetime processedAt`

      Timestamp when this event was processed.

    - `?ManagedAgentsAgentEvaluatedPermission evaluatedPermission`

      The evaluated permission policy for this tool invocation.

    - `?ManagedAgentsAgentToolEvaluation evaluation`

      Which resolved permission_policy produced evaluated_permission: always_allow, always_ask, or auto (with the server's per-invocation judgement). Absent only when the server refused the call before any policy applied (for example, the named tool is not enabled in the session); such a refusal has evaluated_permission deny. An event recorded before this field existed reads as the arm its evaluated_permission implies (always_allow for allow, always_ask for ask).

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.tool_confirmation` or `user.tool_result` by `tool_use_id`, so clients do not send it back.

  - `class ManagedAgentsAgentToolResultEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when this event was processed.

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to.

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `class ManagedAgentsAgentThreadMessageReceivedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `string fromSessionThreadID`

      Public `sthr_` ID of the thread that sent the message.

    - `\Datetime processedAt`

      Timestamp when the message was received.

    - `?string fromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class ManagedAgentsAgentThreadMessageSentEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `\Datetime processedAt`

      Timestamp when the message was sent.

    - `string toSessionThreadID`

      Public `sthr_` ID of the thread the message was sent to.

    - `?string toAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class ManagedAgentsAgentThreadContextCompactedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when compaction was processed.

  - `class ManagedAgentsSessionErrorEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `Error error`

    - `\Datetime processedAt`

      Timestamp when the error occurred.

  - `class ManagedAgentsSessionStatusRescheduledEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp of status change.

  - `class ManagedAgentsSessionStatusRunningEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp of status change.

  - `class ManagedAgentsSessionStatusIdleEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp of status change.

    - `StopReason stopReason`

  - `class ManagedAgentsSessionStatusTerminatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp of status change.

  - `class ManagedAgentsSessionThreadCreatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the callable agent the thread runs.

    - `\Datetime processedAt`

      Timestamp when the thread was created.

    - `string sessionThreadID`

      Public `sthr_` ID of the newly created thread.

  - `class ManagedAgentsSpanOutcomeEvaluationStartEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      Timestamp when outcome evaluation started.

  - `class ManagedAgentsSpanOutcomeEvaluationEndEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string explanation`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeEvaluationStartID`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      Timestamp when outcome evaluation ended.

    - `string result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `ManagedAgentsSpanModelUsage usage`

      Aggregate token usage for this evaluation cycle. Sums across all grader model requests within the cycle.

  - `class ManagedAgentsSpanModelRequestStartEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when the model request started.

  - `class ManagedAgentsSpanModelRequestEndEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `?bool isError`

      Whether the model request resulted in an error.

    - `string modelRequestStartID`

      The id of the corresponding `span.model_request_start` event.

    - `ManagedAgentsSpanModelUsage modelUsage`

      Token usage for this model request.

    - `\Datetime processedAt`

      Timestamp when the model request completed.

  - `class ManagedAgentsSpanOutcomeEvaluationOngoingEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      Timestamp when this heartbeat was emitted.

  - `class ManagedAgentsUserDefineOutcomeEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string description`

      What the agent should produce. Copied from the input event.

    - `?int maxIterations`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `string outcomeID`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `\Datetime processedAt`

      Timestamp when the outcome was accepted.

    - `Rubric rubric`

      How to grade the outcome. File rubrics are currently resolved to their text content; clients should handle both variants.

  - `class ManagedAgentsSessionDeletedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when the session was deleted.

  - `class ManagedAgentsSessionThreadStatusRunningEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      Timestamp of the status transition.

    - `string sessionThreadID`

      Public sthr_ ID of the thread that started running.

  - `class ManagedAgentsSessionThreadStatusIdleEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      Timestamp of the status transition.

    - `string sessionThreadID`

      Public sthr_ ID of the thread that went idle.

    - `StopReason stopReason`

  - `class ManagedAgentsSessionThreadStatusTerminatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      Timestamp of the status transition.

    - `string sessionThreadID`

      Public sthr_ ID of the thread that terminated.

  - `class BetaManagedAgentsUserToolResultEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

    - `?\Datetime processedAt`

      Timestamp when this result was processed.

    - `?string sessionThreadID`

      Set by the server to the subagent thread this result was routed to. Omitted when it was routed to the primary thread.

  - `class ManagedAgentsSessionThreadStatusRescheduledEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      Timestamp of the status transition.

    - `string sessionThreadID`

      Public sthr_ ID of the thread that is retrying.

  - `class BetaManagedAgentsSessionUpdatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when the update was applied.

    - `?BetaManagedAgentsSessionAgent agent`

      The session's effective agent configuration after the update. Present only when the update changed `agent` (tools or mcp_servers); when present it is the full materialised snapshot, not a diff.

    - `?BetaManagedAgentsBudgetLimit budget`

      The session's budget after the update: the new budget when set or replaced, or null when the update removed it. Present only when the update changed the budget.

    - `?array<string,string> metadata`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `?string title`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsSystemMessageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<BetaManagedAgentsSystemContentBlock> content`

      System content blocks. Text-only.

    - `?\Datetime processedAt`

      Timestamp when this system message was processed.

  - `class BetaManagedAgentsSessionUsageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when the snapshot was taken.

    - `ManagedAgentsSessionUsageSnapshot usage`

      The session's cumulative usage at the snapshot time.

    - `?BetaManagedAgentsBudgetLimit budget`

      The session's configured budget at the snapshot time, or null when the session has no budget.

#### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->sessions->threads->events->list(
  'sthr_011CZkZVWa6oIjw0rgXZpnBt',
  sessionID: 'sesn_011CZkZAtmR3yMPDzynEDxu7',
  limit: 0,
  page: 'page',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($page);
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

`$client->beta->sessions->threads->events->stream(string threadID, string sessionID, ?list<BetaManagedAgentsDeltaType> eventDeltas, ?list<AnthropicBeta> betas, ?string workspaceID): ManagedAgentsStreamSessionThreadEvents`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}/stream`

Stream Session Thread Events

#### Parameters

- `sessionID: string`

- `threadID: string`

- `eventDeltas?:optional list<BetaManagedAgentsDeltaType>`

  When set, this connection also receives streaming deltas (`event_start`, `event_delta`) while an event is being produced, before the event itself arrives. Deltas are best-effort; when the final event is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no final event — its terminal `span.model_request_end` closes the preview. Accepts one or more event types to preview and may be repeated: `agent.message` streams `content_delta` fragments; `agent.thinking` is start-only — a signal that the agent has begun extended thinking, concluded by the `agent.thinking` event itself. Only previews of the requested event types are sent.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class ManagedAgentsStreamSessionThreadEvents`

  - `class ManagedAgentsUserMessageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Array of content blocks comprising the user message.

    - `?\Datetime processedAt`

      Timestamp when the agent finished processing this message.

  - `class ManagedAgentsUserInterruptEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `?\Datetime processedAt`

      Timestamp when the interrupt was processed.

    - `?string sessionThreadID`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class ManagedAgentsUserToolConfirmationEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `Result result`

      The confirmation result: 'allow' or 'deny'.

    - `string toolUseID`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `?string denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

    - `?\Datetime processedAt`

      Timestamp when the confirmation was processed.

    - `?string sessionThreadID`

      Set by the server to the subagent thread this confirmation was routed to. Omitted when it was routed to the primary thread.

  - `class ManagedAgentsUserCustomToolResultEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string customToolUseID`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

    - `?\Datetime processedAt`

      Timestamp when this result was processed.

    - `?string sessionThreadID`

      Set by the server to the subagent thread this result was routed to. Omitted when it was routed to the primary thread.

  - `class ManagedAgentsAgentCustomToolUseEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string name`

      Name of the custom tool being called.

    - `\Datetime processedAt`

      Timestamp when this tool use was processed.

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.custom_tool_result` by `custom_tool_use_id`, so clients do not send it back.

  - `class ManagedAgentsAgentMessageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Array of text blocks comprising the agent response.

    - `\Datetime processedAt`

      Timestamp when this response was generated.

  - `class ManagedAgentsAgentThinkingEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when this thinking was produced.

  - `class ManagedAgentsAgentMCPToolUseEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string mcpServerName`

      Name of the MCP server providing the tool.

    - `string name`

      Name of the MCP tool being used.

    - `\Datetime processedAt`

      Timestamp when this event was processed.

    - `?ManagedAgentsAgentEvaluatedPermission evaluatedPermission`

      The evaluated permission policy for this tool invocation.

    - `?ManagedAgentsAgentToolEvaluation evaluation`

      Which resolved permission_policy produced evaluated_permission: always_allow, always_ask, or auto (with the server's per-invocation judgement). Absent only when the server refused the call before any policy applied (for example, the named tool is not enabled in the session); such a refusal has evaluated_permission deny. An event recorded before this field existed reads as the arm its evaluated_permission implies (always_allow for allow, always_ask for ask).

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.tool_confirmation` by `tool_use_id`, so clients do not send it back.

  - `class ManagedAgentsAgentMCPToolResultEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string mcpToolUseID`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `\Datetime processedAt`

      Timestamp when this event was processed.

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `class ManagedAgentsAgentToolUseEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `array<string,mixed> input`

      Input parameters for the tool call.

    - `string name`

      Name of the agent tool being used.

    - `\Datetime processedAt`

      Timestamp when this event was processed.

    - `?ManagedAgentsAgentEvaluatedPermission evaluatedPermission`

      The evaluated permission policy for this tool invocation.

    - `?ManagedAgentsAgentToolEvaluation evaluation`

      Which resolved permission_policy produced evaluated_permission: always_allow, always_ask, or auto (with the server's per-invocation judgement). Absent only when the server refused the call before any policy applied (for example, the named tool is not enabled in the session); such a refusal has evaluated_permission deny. An event recorded before this field existed reads as the arm its evaluated_permission implies (always_allow for allow, always_ask for ask).

    - `?string sessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Informational only: the server routes the matching `user.tool_confirmation` or `user.tool_result` by `tool_use_id`, so clients do not send it back.

  - `class ManagedAgentsAgentToolResultEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when this event was processed.

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to.

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

  - `class ManagedAgentsAgentThreadMessageReceivedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `string fromSessionThreadID`

      Public `sthr_` ID of the thread that sent the message.

    - `\Datetime processedAt`

      Timestamp when the message was received.

    - `?string fromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class ManagedAgentsAgentThreadMessageSentEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<Content> content`

      Message content blocks.

    - `\Datetime processedAt`

      Timestamp when the message was sent.

    - `string toSessionThreadID`

      Public `sthr_` ID of the thread the message was sent to.

    - `?string toAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class ManagedAgentsAgentThreadContextCompactedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when compaction was processed.

  - `class ManagedAgentsSessionErrorEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `Error error`

    - `\Datetime processedAt`

      Timestamp when the error occurred.

  - `class ManagedAgentsSessionStatusRescheduledEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp of status change.

  - `class ManagedAgentsSessionStatusRunningEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp of status change.

  - `class ManagedAgentsSessionStatusIdleEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp of status change.

    - `StopReason stopReason`

  - `class ManagedAgentsSessionStatusTerminatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp of status change.

  - `class ManagedAgentsSessionThreadCreatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the callable agent the thread runs.

    - `\Datetime processedAt`

      Timestamp when the thread was created.

    - `string sessionThreadID`

      Public `sthr_` ID of the newly created thread.

  - `class ManagedAgentsSpanOutcomeEvaluationStartEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      Timestamp when outcome evaluation started.

  - `class ManagedAgentsSpanOutcomeEvaluationEndEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string explanation`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeEvaluationStartID`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      Timestamp when outcome evaluation ended.

    - `string result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `ManagedAgentsSpanModelUsage usage`

      Aggregate token usage for this evaluation cycle. Sums across all grader model requests within the cycle.

  - `class ManagedAgentsSpanModelRequestStartEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when the model request started.

  - `class ManagedAgentsSpanModelRequestEndEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `?bool isError`

      Whether the model request resulted in an error.

    - `string modelRequestStartID`

      The id of the corresponding `span.model_request_start` event.

    - `ManagedAgentsSpanModelUsage modelUsage`

      Token usage for this model request.

    - `\Datetime processedAt`

      Timestamp when the model request completed.

  - `class ManagedAgentsSpanOutcomeEvaluationOngoingEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `int iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

    - `string outcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `\Datetime processedAt`

      Timestamp when this heartbeat was emitted.

  - `class ManagedAgentsUserDefineOutcomeEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string description`

      What the agent should produce. Copied from the input event.

    - `?int maxIterations`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

    - `string outcomeID`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `\Datetime processedAt`

      Timestamp when the outcome was accepted.

    - `Rubric rubric`

      How to grade the outcome. File rubrics are currently resolved to their text content; clients should handle both variants.

  - `class ManagedAgentsSessionDeletedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when the session was deleted.

  - `class ManagedAgentsSessionThreadStatusRunningEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      Timestamp of the status transition.

    - `string sessionThreadID`

      Public sthr_ ID of the thread that started running.

  - `class ManagedAgentsSessionThreadStatusIdleEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      Timestamp of the status transition.

    - `string sessionThreadID`

      Public sthr_ ID of the thread that went idle.

    - `StopReason stopReason`

  - `class ManagedAgentsSessionThreadStatusTerminatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      Timestamp of the status transition.

    - `string sessionThreadID`

      Public sthr_ ID of the thread that terminated.

  - `class BetaManagedAgentsUserToolResultEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string toolUseID`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `?list<Content> content`

      The result content returned by the tool.

    - `?bool isError`

      Whether the tool execution resulted in an error.

    - `?\Datetime processedAt`

      Timestamp when this result was processed.

    - `?string sessionThreadID`

      Set by the server to the subagent thread this result was routed to. Omitted when it was routed to the primary thread.

  - `class ManagedAgentsSessionThreadStatusRescheduledEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `string agentName`

      Name of the agent the thread runs.

    - `\Datetime processedAt`

      Timestamp of the status transition.

    - `string sessionThreadID`

      Public sthr_ ID of the thread that is retrying.

  - `class BetaManagedAgentsSessionUpdatedEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when the update was applied.

    - `?BetaManagedAgentsSessionAgent agent`

      The session's effective agent configuration after the update. Present only when the update changed `agent` (tools or mcp_servers); when present it is the full materialised snapshot, not a diff.

    - `?BetaManagedAgentsBudgetLimit budget`

      The session's budget after the update: the new budget when set or replaced, or null when the update removed it. Present only when the update changed the budget.

    - `?array<string,string> metadata`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `?string title`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsStartEvent`

    - `Type type`

    - `BetaManagedAgentsStartEventPreview event`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

  - `class BetaManagedAgentsDeltaEvent`

    - `Type type`

    - `BetaManagedAgentsDeltaContent delta`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

    - `string eventID`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

  - `class BetaManagedAgentsSystemMessageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `list<BetaManagedAgentsSystemContentBlock> content`

      System content blocks. Text-only.

    - `?\Datetime processedAt`

      Timestamp when this system message was processed.

  - `class BetaManagedAgentsSessionUsageEvent`

    - `Type type`

    - `string id`

      Unique identifier for this event.

    - `\Datetime processedAt`

      Timestamp when the snapshot was taken.

    - `ManagedAgentsSessionUsageSnapshot usage`

      The session's cumulative usage at the snapshot time.

    - `?BetaManagedAgentsBudgetLimit budget`

      The session's configured budget at the snapshot time, or null when the session has no budget.

#### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsStreamSessionThreadEvents = $client
  ->beta
  ->sessions
  ->threads
  ->events
  ->streamStream(
  'sthr_011CZkZVWa6oIjw0rgXZpnBt',
  sessionID: 'sesn_011CZkZAtmR3yMPDzynEDxu7',
  eventDeltas: [BetaManagedAgentsDeltaType::AGENT_MESSAGE],
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsStreamSessionThreadEvents);
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
