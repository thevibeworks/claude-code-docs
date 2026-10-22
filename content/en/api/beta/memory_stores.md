---
title: Memory Stores
url: https://platform.claude.com/docs/en/api/beta/memory_stores
---

# Memory Stores

## Create a Memory Store

**POST** `/v1/memory_stores`

Create a Memory Store

### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"anthropic-beta": optional array of AnthropicBeta`

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

  - `string`

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

  - `"user-profiles-2026-09-04"`

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

  - `"compact-2026-09-04"`

  - `"inline-tools-2026-09-15"`

  - `"mcp-client-2026-09-15"`

  - `"ce-plugins-2026-09-01"`

  - `"spend-limit-reads-2026-09-26"`

  - `"telemetry-destinations-2026-08-11"`

  - `"webhooks-2026-10-07"`

- `"anthropic-workspace-id": optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Body parameters

- `name: string`

  The name of the memory store, 1 to 255 characters long, without control characters. Names don't have to be unique in a workspace.

  In a session, the store's directory under `/mnt/memory/` is based on this name. The name is lowercased and every run of characters other than ASCII letters and digits becomes one hyphen. The session's memory store resource gives the exact path in `mount_path`.

  See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=http#how-the-agent-accesses-memory) to learn more about how agents access memory stores.

  minLength: 1, maxLength: 255

- `description: optional string`

  Free-text description of what the store contains, up to 1,024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent.

  maxLength: 1024

- `metadata: optional map[string]`

  Key-value pairs for your own use, such as the end user that the store belongs to. The agent doesn't see them.

  A store has at most 16 pairs. Keys are 1 to 64 characters long and values at most 512 characters.

### Returns

- `BetaManagedAgentsMemoryStore object`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `type: "memory_store"`

  - `id: string`

    The unique ID of the memory store (`memstore_...`). Use it to attach the store to a session.

  - `archived_at: string or null`

    When the memory store was archived, in RFC 3339, or `null` if it hasn't been.

    Archiving can't be undone. An archived store can't be attached to new sessions. You can't create or update its memories or update the store. You can still read and delete its memories, redact their versions, and delete the store.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=http#archive-a-store) to learn more about archiving.

    format: date-time

  - `created_at: string`

    When the memory store was created, in RFC 3339.

    format: date-time

  - `description: string`

    Free-text description of what the store contains, up to 1,024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata: map[string]`

    Key-value pairs for your own use, such as the end user that the store belongs to.

    A store has at most 16 pairs. Keys are 1 to 64 characters long and values at most 512 characters. You can't filter lists by metadata.

  - `name: string`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `updated_at: string`

    When the memory store was last changed, in RFC 3339.

    Changing its `name`, `description`, or `metadata` updates it. Archiving the store does too. Changes to the store's memories don't.

    format: date-time

### Example

```bash
curl https://api.anthropic.com/v1/memory_stores \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: agent-memory-2026-07-22' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{
          "name": "x"
        }'
```

#### Response (200)

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "metadata": {
    "foo": "string"
  },
  "name": "name",
  "type": "memory_store",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## List Memory Stores

**GET** `/v1/memory_stores`

List Memory Stores

### Query parameters

- `"created_at[gte]": optional string`

  Return only memory stores created at or after this time (inclusive).

  format: date-time

- `"created_at[lte]": optional string`

  Return only memory stores created at or before this time (inclusive).

  format: date-time

- `include_archived: optional boolean`

  When `true`, archived stores are included in the results. Defaults to `false` (archived stores are excluded).

- `limit: optional number`

  Maximum number of stores to return per page. Must be between 1 and 100. Defaults to 20 when omitted.

  format: int32

- `page: optional string`

  The `next_page` value from a previous response, to get the next page. Omit it to get the first page.

### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"anthropic-beta": optional array of AnthropicBeta`

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

  - `string`

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

  - `"user-profiles-2026-09-04"`

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

  - `"compact-2026-09-04"`

  - `"inline-tools-2026-09-15"`

  - `"mcp-client-2026-09-15"`

  - `"ce-plugins-2026-09-01"`

  - `"spend-limit-reads-2026-09-26"`

  - `"telemetry-destinations-2026-08-11"`

  - `"webhooks-2026-10-07"`

- `"anthropic-workspace-id": optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `data: optional array of BetaManagedAgentsMemoryStore`

  Memory stores on this page, newest first. Empty when there are no stores matching the filters.

  - `type: "memory_store"`

  - `id: string`

    The unique ID of the memory store (`memstore_...`). Use it to attach the store to a session.

  - `archived_at: string or null`

    When the memory store was archived, in RFC 3339, or `null` if it hasn't been.

    Archiving can't be undone. An archived store can't be attached to new sessions. You can't create or update its memories or update the store. You can still read and delete its memories, redact their versions, and delete the store.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=http#archive-a-store) to learn more about archiving.

    format: date-time

  - `created_at: string`

    When the memory store was created, in RFC 3339.

    format: date-time

  - `description: string`

    Free-text description of what the store contains, up to 1,024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata: map[string]`

    Key-value pairs for your own use, such as the end user that the store belongs to.

    A store has at most 16 pairs. Keys are 1 to 64 characters long and values at most 512 characters. You can't filter lists by metadata.

  - `name: string`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `updated_at: string`

    When the memory store was last changed, in RFC 3339.

    Changing its `name`, `description`, or `metadata` updates it. Archiving the store does too. Changes to the store's memories don't.

    format: date-time

- `next_page: optional string or null`

  The value to pass as `page` to get the next page, or `null` if there are no more results.

### Example

```bash
curl https://api.anthropic.com/v1/memory_stores \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: agent-memory-2026-07-22' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

#### Response (200)

```json
{
  "data": [
    {
      "id": "memstore_01Wf3kQ8tZxB2mVr7HcJ4aNd",
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "description": "Per-user preferences and project context.",
      "metadata": {},
      "name": "User Preferences",
      "type": "memory_store",
      "updated_at": "2026-03-15T10:00:00Z"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Retrieve a Memory Store

**GET** `/v1/memory_stores/{memory_store_id}`

Retrieve a Memory Store

### Path parameters

- `memory_store_id: string`

  The ID of the memory store to retrieve (`memstore_...`).

### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"anthropic-beta": optional array of AnthropicBeta`

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

  - `string`

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

  - `"user-profiles-2026-09-04"`

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

  - `"compact-2026-09-04"`

  - `"inline-tools-2026-09-15"`

  - `"mcp-client-2026-09-15"`

  - `"ce-plugins-2026-09-01"`

  - `"spend-limit-reads-2026-09-26"`

  - `"telemetry-destinations-2026-08-11"`

  - `"webhooks-2026-10-07"`

- `"anthropic-workspace-id": optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `BetaManagedAgentsMemoryStore object`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `type: "memory_store"`

  - `id: string`

    The unique ID of the memory store (`memstore_...`). Use it to attach the store to a session.

  - `archived_at: string or null`

    When the memory store was archived, in RFC 3339, or `null` if it hasn't been.

    Archiving can't be undone. An archived store can't be attached to new sessions. You can't create or update its memories or update the store. You can still read and delete its memories, redact their versions, and delete the store.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=http#archive-a-store) to learn more about archiving.

    format: date-time

  - `created_at: string`

    When the memory store was created, in RFC 3339.

    format: date-time

  - `description: string`

    Free-text description of what the store contains, up to 1,024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata: map[string]`

    Key-value pairs for your own use, such as the end user that the store belongs to.

    A store has at most 16 pairs. Keys are 1 to 64 characters long and values at most 512 characters. You can't filter lists by metadata.

  - `name: string`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `updated_at: string`

    When the memory store was last changed, in RFC 3339.

    Changing its `name`, `description`, or `metadata` updates it. Archiving the store does too. Changes to the store's memories don't.

    format: date-time

### Example

```bash
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: agent-memory-2026-07-22' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

#### Response (200)

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "metadata": {
    "foo": "string"
  },
  "name": "name",
  "type": "memory_store",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## Update a Memory Store

**POST** `/v1/memory_stores/{memory_store_id}`

Update a Memory Store

### Path parameters

- `memory_store_id: string`

  The ID of the memory store to update (`memstore_...`).

  The request fails with HTTP status 400 if the store is archived.

### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"anthropic-beta": optional array of AnthropicBeta`

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

  - `string`

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

  - `"user-profiles-2026-09-04"`

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

  - `"compact-2026-09-04"`

  - `"inline-tools-2026-09-15"`

  - `"mcp-client-2026-09-15"`

  - `"ce-plugins-2026-09-01"`

  - `"spend-limit-reads-2026-09-26"`

  - `"telemetry-destinations-2026-08-11"`

  - `"webhooks-2026-10-07"`

- `"anthropic-workspace-id": optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Body parameters

- `description: optional string or null`

  New description for the store, up to 1,024 characters. Pass an empty string to clear it.

  maxLength: 1024

- `metadata: optional map[string] or null`

  Changes to apply to the memory store's metadata. Keys you leave out keep their values.

  Set a key to a string to add or replace it, or to `null` to remove it. After the change, the metadata can hold at most 16 key-value pairs. Keys are 1 to 64 characters long and values at most 512 characters.

- `name: optional string or null`

  The new name of the memory store, 1 to 255 characters long, without control characters.

  Sessions created after the change use the new name for the store's directory under `/mnt/memory/`.

  minLength: 1, maxLength: 255

### Returns

- `BetaManagedAgentsMemoryStore object`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `type: "memory_store"`

  - `id: string`

    The unique ID of the memory store (`memstore_...`). Use it to attach the store to a session.

  - `archived_at: string or null`

    When the memory store was archived, in RFC 3339, or `null` if it hasn't been.

    Archiving can't be undone. An archived store can't be attached to new sessions. You can't create or update its memories or update the store. You can still read and delete its memories, redact their versions, and delete the store.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=http#archive-a-store) to learn more about archiving.

    format: date-time

  - `created_at: string`

    When the memory store was created, in RFC 3339.

    format: date-time

  - `description: string`

    Free-text description of what the store contains, up to 1,024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata: map[string]`

    Key-value pairs for your own use, such as the end user that the store belongs to.

    A store has at most 16 pairs. Keys are 1 to 64 characters long and values at most 512 characters. You can't filter lists by metadata.

  - `name: string`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `updated_at: string`

    When the memory store was last changed, in RFC 3339.

    Changing its `name`, `description`, or `metadata` updates it. Archiving the store does too. Changes to the store's memories don't.

    format: date-time

### Example

```bash
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: agent-memory-2026-07-22' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{}'
```

#### Response (200)

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "metadata": {
    "foo": "string"
  },
  "name": "name",
  "type": "memory_store",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## Delete a Memory Store

**DELETE** `/v1/memory_stores/{memory_store_id}`

Delete a Memory Store

### Path parameters

- `memory_store_id: string`

  The ID of the memory store to delete (`memstore_...`).

  Deleting a store also deletes all its memories and memory versions. It can't be undone.

### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"anthropic-beta": optional array of AnthropicBeta`

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

  - `string`

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

  - `"user-profiles-2026-09-04"`

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

  - `"compact-2026-09-04"`

  - `"inline-tools-2026-09-15"`

  - `"mcp-client-2026-09-15"`

  - `"ce-plugins-2026-09-01"`

  - `"spend-limit-reads-2026-09-26"`

  - `"telemetry-destinations-2026-08-11"`

  - `"webhooks-2026-10-07"`

- `"anthropic-workspace-id": optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `BetaManagedAgentsDeletedMemoryStore object`

  Confirmation that a `memory_store` was deleted.

  - `type: "memory_store_deleted"`

  - `id: string`

    ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

### Example

```bash
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID \
    -X DELETE \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: agent-memory-2026-07-22' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

#### Response (200)

```json
{
  "id": "id",
  "type": "memory_store_deleted"
}
```

## Archive a Memory Store

**POST** `/v1/memory_stores/{memory_store_id}/archive`

Archive a Memory Store

### Path parameters

- `memory_store_id: string`

  The ID of the memory store to archive (`memstore_...`).

  Archiving can't be undone. Archiving a store that is already archived returns it unchanged.

### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"anthropic-beta": optional array of AnthropicBeta`

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

  - `string`

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

  - `"user-profiles-2026-09-04"`

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

  - `"compact-2026-09-04"`

  - `"inline-tools-2026-09-15"`

  - `"mcp-client-2026-09-15"`

  - `"ce-plugins-2026-09-01"`

  - `"spend-limit-reads-2026-09-26"`

  - `"telemetry-destinations-2026-08-11"`

  - `"webhooks-2026-10-07"`

- `"anthropic-workspace-id": optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `BetaManagedAgentsMemoryStore object`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `type: "memory_store"`

  - `id: string`

    The unique ID of the memory store (`memstore_...`). Use it to attach the store to a session.

  - `archived_at: string or null`

    When the memory store was archived, in RFC 3339, or `null` if it hasn't been.

    Archiving can't be undone. An archived store can't be attached to new sessions. You can't create or update its memories or update the store. You can still read and delete its memories, redact their versions, and delete the store.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=http#archive-a-store) to learn more about archiving.

    format: date-time

  - `created_at: string`

    When the memory store was created, in RFC 3339.

    format: date-time

  - `description: string`

    Free-text description of what the store contains, up to 1,024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata: map[string]`

    Key-value pairs for your own use, such as the end user that the store belongs to.

    A store has at most 16 pairs. Keys are 1 to 64 characters long and values at most 512 characters. You can't filter lists by metadata.

  - `name: string`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `updated_at: string`

    When the memory store was last changed, in RFC 3339.

    Changing its `name`, `description`, or `metadata` updates it. Archiving the store does too. Changes to the store's memories don't.

    format: date-time

### Example

```bash
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/archive \
    -X POST \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: agent-memory-2026-07-22' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

#### Response (200)

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "description": "description",
  "metadata": {
    "foo": "string"
  },
  "name": "name",
  "type": "memory_store",
  "updated_at": "2019-12-27T18:11:19.117Z"
}
```

## Domain types

### Beta Managed Agents Deleted Memory Store

- `BetaManagedAgentsDeletedMemoryStore object`

  Confirmation that a `memory_store` was deleted.

  - `type: "memory_store_deleted"`

  - `id: string`

    ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

### Beta Managed Agents Memory Store

- `BetaManagedAgentsMemoryStore object`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `type: "memory_store"`

  - `id: string`

    The unique ID of the memory store (`memstore_...`). Use it to attach the store to a session.

  - `archived_at: string or null`

    When the memory store was archived, in RFC 3339, or `null` if it hasn't been.

    Archiving can't be undone. An archived store can't be attached to new sessions. You can't create or update its memories or update the store. You can still read and delete its memories, redact their versions, and delete the store.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=http#archive-a-store) to learn more about archiving.

    format: date-time

  - `created_at: string`

    When the memory store was created, in RFC 3339.

    format: date-time

  - `description: string`

    Free-text description of what the store contains, up to 1,024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata: map[string]`

    Key-value pairs for your own use, such as the end user that the store belongs to.

    A store has at most 16 pairs. Keys are 1 to 64 characters long and values at most 512 characters. You can't filter lists by metadata.

  - `name: string`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `updated_at: string`

    When the memory store was last changed, in RFC 3339.

    Changing its `name`, `description`, or `metadata` updates it. Archiving the store does too. Changes to the store's memories don't.

    format: date-time

## Memory Stores › Memories

### Create a Memory

**POST** `/v1/memory_stores/{memory_store_id}/memories`

Create a Memory

#### Path parameters

- `memory_store_id: string`

  The ID of the memory store to create the memory in (`memstore_...`).

#### Query parameters

- `view: optional BetaManagedAgentsMemoryView`

  Whether a `memory` or `memory_version` in the response includes its `content`. Defaults to `full` on retrieve operations and to `basic` on list, create, and update operations.

  With `full`, list operations return at most 20 items per page.

  - `"basic"`

    Return the object with `content` set to `null`. The `content_size_bytes` and `content_sha256` fields remain populated, so sync clients can diff without fetching content.

  - `"full"`

    Return the object with `content` populated. On list endpoints, `view=full` caps `limit` at 20.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"anthropic-beta": optional array of AnthropicBeta`

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

  - `string`

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

  - `"user-profiles-2026-09-04"`

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

  - `"compact-2026-09-04"`

  - `"inline-tools-2026-09-15"`

  - `"mcp-client-2026-09-15"`

  - `"ce-plugins-2026-09-01"`

  - `"spend-limit-reads-2026-09-26"`

  - `"telemetry-destinations-2026-08-11"`

  - `"webhooks-2026-10-07"`

- `"anthropic-workspace-id": optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Body parameters

- `content: string or null`

  The UTF-8 text content of the new memory. Pass `""` to create an empty memory.

  The maximum size is 100 kB (102,400 bytes).

- `path: string`

  The path of the new memory, such as `/projects/foo/notes.md`. Paths are case-sensitive.

  A path starts with `/` and has 1 to 20 segments. A segment can't be empty and can't be `.` or `..`. A path can't contain control characters, format characters, or the line and paragraph separators U+2028 and U+2029. It must be in Unicode Normalization Form C and at most 1,024 bytes long.

  minLength: 2, maxLength: 1024

#### Returns

- `BetaManagedAgentsMemory object`

  A text document at a path inside a memory store.

  `content` is `null` when the response uses `view=basic`. `content_size_bytes` and `content_sha256` are always set, so you can detect changes without fetching the content. To retrieve, update, or delete a memory, pass its ID, which stays the same when its path changes.

  See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=http#view-and-edit-memories) to learn more about working with memories.

  - `type: "memory"`

  - `id: string`

    The unique ID of the memory (`mem_...`). It stays the same when the memory's path changes.

    To retrieve, update, or delete the memory, pass this ID.

  - `content_sha256: string`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `content_size_bytes: number`

    The size of the memory's `content` in UTF-8 bytes. It is set regardless of `view`.

    format: int32

  - `created_at: string`

    When this memory was created, in RFC 3339 format.

    format: date-time

  - `memory_store_id: string`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `memory_version_id: string`

    The ID of the memory version that holds the memory's current content (`memver_...`).

    Memory versions don't have a flag that marks the latest one. Compare their IDs with this field instead.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=http#audit-memory-changes) to learn more about memory versions.

  - `path: string`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `updated_at: string`

    When the memory was last changed, in RFC 3339.

    To find out who made the change, look at `created_by` on the memory version that `memory_version_id` references.

    format: date-time

  - `content: optional string or null`

    The memory's UTF-8 text content, or `null` when the response uses `view=basic`.

    The maximum size is 100 kB (102,400 bytes).

#### Example

```bash
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memories \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: agent-memory-2026-07-22' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{
          "content": "content",
          "path": "xx"
        }'
```

##### Response (200)

```json
{
  "id": "id",
  "content_sha256": "content_sha256",
  "content_size_bytes": 0,
  "created_at": "2019-12-27T18:11:19.117Z",
  "memory_store_id": "memory_store_id",
  "memory_version_id": "memory_version_id",
  "path": "path",
  "type": "memory",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "content": "content"
}
```

### List Memories

**GET** `/v1/memory_stores/{memory_store_id}/memories`

List Memories

#### Path parameters

- `memory_store_id: string`

  The ID of the memory store to list memories from (`memstore_...`).

#### Query parameters

- `depth: optional number`

  How far below `path_prefix` to list. Defaults to `0`, which lists every memory below the prefix.

  Pass `1` to list only the direct children. Deeper memories are then grouped into `memory_prefix` items.

  format: int32

- `limit: optional number`

  The maximum number of items to return per page, from 1 to 100. Defaults to 20.

  With `view=full`, a page holds at most 20 items. `memory` and `memory_prefix` items both count toward the limit.

  format: int32

- `page: optional string`

  The `next_page` value from a previous response, to get the next page. Omit it to get the first page.

- `path_prefix: optional string`

  Return only memories whose path starts with this prefix, such as `/notes/`. This value appears in request URLs. Do not include secrets or personally identifiable information.

  Omit it to list the whole store. The prefix must end with `/` and matches whole segments, so `/notes/` matches `/notes/todo.md` but not `/notes-archive/todo.md`.

- `view: optional BetaManagedAgentsMemoryView`

  Whether each memory in the response includes `content`. Defaults to `basic`, which sets it to `null`.

  With `full`, a page holds at most 20 items.

  - `"basic"`

    Return the object with `content` set to `null`. The `content_size_bytes` and `content_sha256` fields remain populated, so sync clients can diff without fetching content.

  - `"full"`

    Return the object with `content` populated. On list endpoints, `view=full` caps `limit` at 20.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"anthropic-beta": optional array of AnthropicBeta`

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

  - `string`

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

  - `"user-profiles-2026-09-04"`

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

  - `"compact-2026-09-04"`

  - `"inline-tools-2026-09-15"`

  - `"mcp-client-2026-09-15"`

  - `"ce-plugins-2026-09-01"`

  - `"spend-limit-reads-2026-09-26"`

  - `"telemetry-destinations-2026-08-11"`

  - `"webhooks-2026-10-07"`

- `"anthropic-workspace-id": optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `data: optional array of BetaManagedAgentsMemoryListItem`

  One page of results. Each item is either a `memory` object or, when `depth` was set, a `memory_prefix` rollup marker. Items are returned in a stable, server-defined order.

  - `BetaManagedAgentsMemory object`

    A text document at a path inside a memory store.

    `content` is `null` when the response uses `view=basic`. `content_size_bytes` and `content_sha256` are always set, so you can detect changes without fetching the content. To retrieve, update, or delete a memory, pass its ID, which stays the same when its path changes.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=http#view-and-edit-memories) to learn more about working with memories.

    - `type: "memory"`

    - `id: string`

      The unique ID of the memory (`mem_...`). It stays the same when the memory's path changes.

      To retrieve, update, or delete the memory, pass this ID.

    - `content_sha256: string`

      Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

    - `content_size_bytes: number`

      The size of the memory's `content` in UTF-8 bytes. It is set regardless of `view`.

      format: int32

    - `created_at: string`

      When this memory was created, in RFC 3339 format.

      format: date-time

    - `memory_store_id: string`

      ID of the memory store this memory belongs to (a `memstore_...` value).

    - `memory_version_id: string`

      The ID of the memory version that holds the memory's current content (`memver_...`).

      Memory versions don't have a flag that marks the latest one. Compare their IDs with this field instead.

      See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=http#audit-memory-changes) to learn more about memory versions.

    - `path: string`

      Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

    - `updated_at: string`

      When the memory was last changed, in RFC 3339.

      To find out who made the change, look at `created_by` on the memory version that `memory_version_id` references.

      format: date-time

    - `content: optional string or null`

      The memory's UTF-8 text content, or `null` when the response uses `view=basic`.

      The maximum size is 100 kB (102,400 bytes).

  - `BetaManagedAgentsMemoryPrefix object`

    A directory marker that [List Memories](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/list?sdk_languages=http) returns instead of the memories below the requested `depth`.

    It stands for one or more memories whose paths start with `path`. It isn't a stored object and doesn't have an ID. Each marker counts toward the page `limit`.

    - `type: "memory_prefix"`

    - `path: string`

      The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

- `next_page: optional string or null`

  The value to pass as `page` to get the next page, or `null` if there are no more results.

#### Example

```bash
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memories \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: agent-memory-2026-07-22' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "mem_011CZkZ9X2dpNyB6YbtxvB6e",
      "content_sha256": "ba7936d94c84d948a2232088f78228f175df6a8353b2d5bc9228eee5794a0024",
      "content_size_bytes": 28,
      "created_at": "2026-03-15T10:00:00Z",
      "memory_store_id": "memstore_01Wf3kQ8tZxB2mVr7HcJ4aNd",
      "memory_version_id": "memver_011CZkZBJq5dWxk9fVLNcPht",
      "path": "/preferences/formatting.md",
      "type": "memory",
      "updated_at": "2026-03-15T10:00:00Z",
      "content": null
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

### Retrieve a Memory

**GET** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Retrieve a Memory

#### Path parameters

- `memory_store_id: string`

  The ID of the memory store that holds the memory (`memstore_...`).

- `memory_id: string`

  The ID of the memory to retrieve (`mem_...`).

#### Query parameters

- `view: optional BetaManagedAgentsMemoryView`

  Whether a `memory` or `memory_version` in the response includes its `content`. Defaults to `full` on retrieve operations and to `basic` on list, create, and update operations.

  With `full`, list operations return at most 20 items per page.

  - `"basic"`

    Return the object with `content` set to `null`. The `content_size_bytes` and `content_sha256` fields remain populated, so sync clients can diff without fetching content.

  - `"full"`

    Return the object with `content` populated. On list endpoints, `view=full` caps `limit` at 20.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"anthropic-beta": optional array of AnthropicBeta`

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

  - `string`

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

  - `"user-profiles-2026-09-04"`

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

  - `"compact-2026-09-04"`

  - `"inline-tools-2026-09-15"`

  - `"mcp-client-2026-09-15"`

  - `"ce-plugins-2026-09-01"`

  - `"spend-limit-reads-2026-09-26"`

  - `"telemetry-destinations-2026-08-11"`

  - `"webhooks-2026-10-07"`

- `"anthropic-workspace-id": optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `BetaManagedAgentsMemory object`

  A text document at a path inside a memory store.

  `content` is `null` when the response uses `view=basic`. `content_size_bytes` and `content_sha256` are always set, so you can detect changes without fetching the content. To retrieve, update, or delete a memory, pass its ID, which stays the same when its path changes.

  See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=http#view-and-edit-memories) to learn more about working with memories.

  - `type: "memory"`

  - `id: string`

    The unique ID of the memory (`mem_...`). It stays the same when the memory's path changes.

    To retrieve, update, or delete the memory, pass this ID.

  - `content_sha256: string`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `content_size_bytes: number`

    The size of the memory's `content` in UTF-8 bytes. It is set regardless of `view`.

    format: int32

  - `created_at: string`

    When this memory was created, in RFC 3339 format.

    format: date-time

  - `memory_store_id: string`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `memory_version_id: string`

    The ID of the memory version that holds the memory's current content (`memver_...`).

    Memory versions don't have a flag that marks the latest one. Compare their IDs with this field instead.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=http#audit-memory-changes) to learn more about memory versions.

  - `path: string`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `updated_at: string`

    When the memory was last changed, in RFC 3339.

    To find out who made the change, look at `created_by` on the memory version that `memory_version_id` references.

    format: date-time

  - `content: optional string or null`

    The memory's UTF-8 text content, or `null` when the response uses `view=basic`.

    The maximum size is 100 kB (102,400 bytes).

#### Example

```bash
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memories/$MEMORY_ID \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: agent-memory-2026-07-22' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "id": "id",
  "content_sha256": "content_sha256",
  "content_size_bytes": 0,
  "created_at": "2019-12-27T18:11:19.117Z",
  "memory_store_id": "memory_store_id",
  "memory_version_id": "memory_version_id",
  "path": "path",
  "type": "memory",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "content": "content"
}
```

### Update a Memory

**POST** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Update a Memory

#### Path parameters

- `memory_store_id: string`

  The ID of the memory store that holds the memory (`memstore_...`).

- `memory_id: string`

  The ID of the memory to update (`mem_...`).

#### Query parameters

- `view: optional BetaManagedAgentsMemoryView`

  Whether a `memory` or `memory_version` in the response includes its `content`. Defaults to `full` on retrieve operations and to `basic` on list, create, and update operations.

  With `full`, list operations return at most 20 items per page.

  - `"basic"`

    Return the object with `content` set to `null`. The `content_size_bytes` and `content_sha256` fields remain populated, so sync clients can diff without fetching content.

  - `"full"`

    Return the object with `content` populated. On list endpoints, `view=full` caps `limit` at 20.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"anthropic-beta": optional array of AnthropicBeta`

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

  - `string`

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

  - `"user-profiles-2026-09-04"`

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

  - `"compact-2026-09-04"`

  - `"inline-tools-2026-09-15"`

  - `"mcp-client-2026-09-15"`

  - `"ce-plugins-2026-09-01"`

  - `"spend-limit-reads-2026-09-26"`

  - `"telemetry-destinations-2026-08-11"`

  - `"webhooks-2026-10-07"`

- `"anthropic-workspace-id": optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Body parameters

- `content: optional string or null`

  New UTF-8 text content for the memory. Maximum 100 kB (102,400 bytes). Omit to leave the content unchanged (e.g., for a rename-only update).

- `path: optional string or null`

  The new path of the memory, which renames it. Omit it to keep the current path.

  The memory keeps its `id`. A path starts with `/` and has 1 to 20 segments. A segment can't be empty and can't be `.` or `..`. A path can't contain control characters, format characters, or the line and paragraph separators U+2028 and U+2029. It must be in Unicode Normalization Form C and at most 1,024 bytes long. Paths are case-sensitive.

  minLength: 2, maxLength: 1024

- `precondition: optional BetaManagedAgentsPrecondition`

  The condition that the memory must meet for the update to apply. Omit it to update unconditionally.

  If the condition fails, the request fails with HTTP status 409.

  - `type: "content_sha256"`

  - `content_sha256: optional string`

    Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

#### Returns

- `BetaManagedAgentsMemory object`

  A text document at a path inside a memory store.

  `content` is `null` when the response uses `view=basic`. `content_size_bytes` and `content_sha256` are always set, so you can detect changes without fetching the content. To retrieve, update, or delete a memory, pass its ID, which stays the same when its path changes.

  See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=http#view-and-edit-memories) to learn more about working with memories.

  - `type: "memory"`

  - `id: string`

    The unique ID of the memory (`mem_...`). It stays the same when the memory's path changes.

    To retrieve, update, or delete the memory, pass this ID.

  - `content_sha256: string`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `content_size_bytes: number`

    The size of the memory's `content` in UTF-8 bytes. It is set regardless of `view`.

    format: int32

  - `created_at: string`

    When this memory was created, in RFC 3339 format.

    format: date-time

  - `memory_store_id: string`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `memory_version_id: string`

    The ID of the memory version that holds the memory's current content (`memver_...`).

    Memory versions don't have a flag that marks the latest one. Compare their IDs with this field instead.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=http#audit-memory-changes) to learn more about memory versions.

  - `path: string`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `updated_at: string`

    When the memory was last changed, in RFC 3339.

    To find out who made the change, look at `created_by` on the memory version that `memory_version_id` references.

    format: date-time

  - `content: optional string or null`

    The memory's UTF-8 text content, or `null` when the response uses `view=basic`.

    The maximum size is 100 kB (102,400 bytes).

#### Example

```bash
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memories/$MEMORY_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: agent-memory-2026-07-22' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{}'
```

##### Response (200)

```json
{
  "id": "id",
  "content_sha256": "content_sha256",
  "content_size_bytes": 0,
  "created_at": "2019-12-27T18:11:19.117Z",
  "memory_store_id": "memory_store_id",
  "memory_version_id": "memory_version_id",
  "path": "path",
  "type": "memory",
  "updated_at": "2019-12-27T18:11:19.117Z",
  "content": "content"
}
```

### Delete a Memory

**DELETE** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Delete a Memory

#### Path parameters

- `memory_store_id: string`

  The ID of the memory store that holds the memory (`memstore_...`).

- `memory_id: string`

  The ID of the memory to delete (`mem_...`).

#### Query parameters

- `expected_content_sha256: optional string`

  Delete the memory only if its current `content_sha256` equals this value, given as 64 lowercase hexadecimal characters. Omit it to delete unconditionally.

  If the hashes differ, the request fails with HTTP status 409 and nothing is deleted.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"anthropic-beta": optional array of AnthropicBeta`

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

  - `string`

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

  - `"user-profiles-2026-09-04"`

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

  - `"compact-2026-09-04"`

  - `"inline-tools-2026-09-15"`

  - `"mcp-client-2026-09-15"`

  - `"ce-plugins-2026-09-01"`

  - `"spend-limit-reads-2026-09-26"`

  - `"telemetry-destinations-2026-08-11"`

  - `"webhooks-2026-10-07"`

- `"anthropic-workspace-id": optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `BetaManagedAgentsDeletedMemory object`

  The confirmation that [Delete a Memory](https://platform.claude.com/docs/en/api/beta/memory_stores/memories/delete?sdk_languages=http) returns.

  Deleting a memory doesn't delete its versions. [List Memory Versions](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/list?sdk_languages=http) returns them while they are retained: each version is kept for at least the version retention period after it was written, unless the store itself is deleted.

  See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=http#audit-memory-changes) to learn more about how long versions are kept.

  - `type: "memory_deleted"`

  - `id: string`

    ID of the deleted memory (a `mem_...` value).

#### Example

```bash
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memories/$MEMORY_ID \
    -X DELETE \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: agent-memory-2026-07-22' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "id": "id",
  "type": "memory_deleted"
}
```

## Memory Stores › Memory Versions

### List Memory Versions

**GET** `/v1/memory_stores/{memory_store_id}/memory_versions`

List Memory Versions

#### Path parameters

- `memory_store_id: string`

  The ID of the memory store whose version history to list (`memstore_...`).

#### Query parameters

- `api_key_id: optional string`

  Return only versions written with the API key that has this ID.

- `"created_at[gte]": optional string`

  Return versions created at or after this time (inclusive).

  format: date-time

- `"created_at[lte]": optional string`

  Return versions created at or before this time (inclusive).

  format: date-time

- `limit: optional number`

  The maximum number of versions to return per page, from 1 to 100. Defaults to 20.

  With `view=full`, a page holds at most 20 versions.

  format: int32

- `memory_id: optional string`

  Return only versions of the memory with this ID (`mem_...`).

  The filter still works after the memory is deleted. While that memory's versions are retained, the results include the version whose `operation` is `deleted`.

- `operation: optional BetaManagedAgentsMemoryVersionOperation`

  Return only versions that record this kind of change.

  - `"created"`

    The memory was created. The first version in any memory's lineage.

  - `"modified"`

    The memory's `content`, `path`, or both were changed via update. Writes the agent makes through the filesystem mount also appear as `modified`.

  - `"deleted"`

    The memory was deleted. The `content`, `content_size_bytes`, and `content_sha256` fields are `null` on this version. The preceding version, while it is retained, records the deleted content's size and hash.

- `page: optional string`

  The `next_page` value from a previous response, to get the next page. Omit it to get the first page.

- `service_account_id: optional string`

  Return only versions written by the service account with this ID (`svac_...`).

- `session_id: optional string`

  Return only versions written by the session with this ID.

- `view: optional BetaManagedAgentsMemoryView`

  Whether a `memory` or `memory_version` in the response includes its `content`. Defaults to `full` on retrieve operations and to `basic` on list, create, and update operations.

  With `full`, list operations return at most 20 items per page.

  - `"basic"`

    Return the object with `content` set to `null`. The `content_size_bytes` and `content_sha256` fields remain populated, so sync clients can diff without fetching content.

  - `"full"`

    Return the object with `content` populated. On list endpoints, `view=full` caps `limit` at 20.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"anthropic-beta": optional array of AnthropicBeta`

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

  - `string`

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

  - `"user-profiles-2026-09-04"`

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

  - `"compact-2026-09-04"`

  - `"inline-tools-2026-09-15"`

  - `"mcp-client-2026-09-15"`

  - `"ce-plugins-2026-09-01"`

  - `"spend-limit-reads-2026-09-26"`

  - `"telemetry-destinations-2026-08-11"`

  - `"webhooks-2026-10-07"`

- `"anthropic-workspace-id": optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `data: optional array of BetaManagedAgentsMemoryVersion`

  One page of `memory_version` objects, ordered by `created_at` descending (newest first), with `id` as tiebreak.

  - `type: "memory_version"`

  - `id: string`

    Unique identifier for this version (a `memver_...` value).

  - `created_at: string`

    When this version was written, in RFC 3339 format.

    format: date-time

  - `memory_id: string`

    The ID of the memory that this version belongs to (`mem_...`).

    The ID stays valid after the memory is deleted. Pass it as `memory_id` to [List Memory Versions](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/list?sdk_languages=http) to get the memory's retained versions, including its `deleted` version while the lineage is retained.

  - `memory_store_id: string`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `operation: BetaManagedAgentsMemoryVersionOperation`

    The kind of mutation this version records: `created`, `modified`, or `deleted`.

    - `"created"`

      The memory was created. The first version in any memory's lineage.

    - `"modified"`

      The memory's `content`, `path`, or both were changed via update. Writes the agent makes through the filesystem mount also appear as `modified`.

    - `"deleted"`

      The memory was deleted. The `content`, `content_size_bytes`, and `content_sha256` fields are `null` on this version. The preceding version, while it is retained, records the deleted content's size and hash.

  - `content: optional string or null`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `content_sha256: optional string or null`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `content_size_bytes: optional number or null`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

    format: int32

  - `created_by: optional BetaManagedAgentsActor`

    Who made this change to the memory, or `null` if the author wasn't recorded.

    Redacting the version doesn't change this field. A `session_actor` here is an agent that wrote through the store's mounted filesystem at `/mnt/memory/`. The version doesn't record the API key that created that session. So the author in `created_by` is who made the change, not who is ultimately responsible for it.

    You can [retrieve the session](https://platform.claude.com/docs/en/api/beta/sessions/retrieve?sdk_languages=http) to learn more about where the change came from.

    - `BetaManagedAgentsSessionActor object`

      An agent acting during a session, for example through the session's mounted filesystem. It names the session itself, not the user or API key that started the session.

      - `type: "session_actor"`

      - `session_id: string`

        ID of the session (a `sesn_...` value). Look up the session via [Retrieve a session](https://platform.claude.com/docs/en/api/beta/sessions/retrieve?sdk_languages=http) for further provenance.

        minLength: 1

    - `BetaManagedAgentsAPIActor object`

      A direct caller of the public API, identified by the API key that authenticated the request.

      - `type: "api_actor"`

      - `api_key_id: string`

        ID of the API key (an `apikey_...` value). This identifies the key, not the secret.

        minLength: 1

    - `BetaManagedAgentsUserActor object`

      A human user, for example acting through the Anthropic Console.

      - `type: "user_actor"`

      - `user_id: string`

        ID of the user (a `user_...` value).

        minLength: 1

    - `BetaManagedAgentsServiceAccountActor object`

      A workload authenticated as a service account, for example via Workload Identity Federation.

      - `type: "service_account_actor"`

      - `service_account_id: string`

        ID of the service account (a `svac_...` value).

        minLength: 1

  - `path: optional string or null`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `redacted_at: optional string or null`

    When the version was redacted, in RFC 3339, or `null` if it hasn't been.

    When set, `content`, `path`, `content_size_bytes`, and `content_sha256` are `null`.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=http#redact-a-version) to learn more about redaction.

    format: date-time

  - `redacted_by: optional BetaManagedAgentsActor`

    Who redacted this version, or `null` if it has not been redacted. In practice always an `api_actor`, `user_actor`, or `service_account_actor` (agents do not have a redact capability).

- `next_page: optional string or null`

  The value to pass as `page` to get the next page, or `null` if there are no more results.

#### Example

```bash
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memory_versions \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: agent-memory-2026-07-22' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "memver_011CZkZBJq5dWxk9fVLNcPht",
      "created_at": "2026-03-15T10:00:00Z",
      "memory_id": "mem_011CZkZ9X2dpNyB6YbtxvB6e",
      "memory_store_id": "memstore_01Wf3kQ8tZxB2mVr7HcJ4aNd",
      "operation": "created",
      "type": "memory_version",
      "content": null,
      "content_sha256": "ba7936d94c84d948a2232088f78228f175df6a8353b2d5bc9228eee5794a0024",
      "content_size_bytes": 28,
      "created_by": {
        "session_id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
        "type": "session_actor"
      },
      "path": "/preferences/formatting.md",
      "redacted_at": null,
      "redacted_by": {
        "session_id": "x",
        "type": "session_actor"
      }
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

### Retrieve a Memory Version

**GET** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}`

Retrieve a Memory Version

#### Path parameters

- `memory_store_id: string`

  The ID of the memory store that holds the version (`memstore_...`).

- `memory_version_id: string`

  The ID of the memory version to retrieve (`memver_...`).

#### Query parameters

- `view: optional BetaManagedAgentsMemoryView`

  Whether a `memory` or `memory_version` in the response includes its `content`. Defaults to `full` on retrieve operations and to `basic` on list, create, and update operations.

  With `full`, list operations return at most 20 items per page.

  - `"basic"`

    Return the object with `content` set to `null`. The `content_size_bytes` and `content_sha256` fields remain populated, so sync clients can diff without fetching content.

  - `"full"`

    Return the object with `content` populated. On list endpoints, `view=full` caps `limit` at 20.

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"anthropic-beta": optional array of AnthropicBeta`

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

  - `string`

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

  - `"user-profiles-2026-09-04"`

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

  - `"compact-2026-09-04"`

  - `"inline-tools-2026-09-15"`

  - `"mcp-client-2026-09-15"`

  - `"ce-plugins-2026-09-01"`

  - `"spend-limit-reads-2026-09-26"`

  - `"telemetry-destinations-2026-08-11"`

  - `"webhooks-2026-10-07"`

- `"anthropic-workspace-id": optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `BetaManagedAgentsMemoryVersion object`

  One entry in a memory's history, recording a single change and who made it.

  Every change to a memory adds one version. Only redaction can change a version after that. Versions belong to the memory store and stay after the memory is deleted. Each version is retained for at least the version retention period after it was written, unless the store itself is deleted.

  Retrieving a redacted version succeeds, with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`. Check `redacted_at` to find out whether a version was redacted.

  See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=http#audit-memory-changes) to learn more about memory versions.

  - `type: "memory_version"`

  - `id: string`

    Unique identifier for this version (a `memver_...` value).

  - `created_at: string`

    When this version was written, in RFC 3339 format.

    format: date-time

  - `memory_id: string`

    The ID of the memory that this version belongs to (`mem_...`).

    The ID stays valid after the memory is deleted. Pass it as `memory_id` to [List Memory Versions](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/list?sdk_languages=http) to get the memory's retained versions, including its `deleted` version while the lineage is retained.

  - `memory_store_id: string`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `operation: BetaManagedAgentsMemoryVersionOperation`

    The kind of mutation this version records: `created`, `modified`, or `deleted`.

    - `"created"`

      The memory was created. The first version in any memory's lineage.

    - `"modified"`

      The memory's `content`, `path`, or both were changed via update. Writes the agent makes through the filesystem mount also appear as `modified`.

    - `"deleted"`

      The memory was deleted. The `content`, `content_size_bytes`, and `content_sha256` fields are `null` on this version. The preceding version, while it is retained, records the deleted content's size and hash.

  - `content: optional string or null`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `content_sha256: optional string or null`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `content_size_bytes: optional number or null`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

    format: int32

  - `created_by: optional BetaManagedAgentsActor`

    Who made this change to the memory, or `null` if the author wasn't recorded.

    Redacting the version doesn't change this field. A `session_actor` here is an agent that wrote through the store's mounted filesystem at `/mnt/memory/`. The version doesn't record the API key that created that session. So the author in `created_by` is who made the change, not who is ultimately responsible for it.

    You can [retrieve the session](https://platform.claude.com/docs/en/api/beta/sessions/retrieve?sdk_languages=http) to learn more about where the change came from.

    - `BetaManagedAgentsSessionActor object`

      An agent acting during a session, for example through the session's mounted filesystem. It names the session itself, not the user or API key that started the session.

      - `type: "session_actor"`

      - `session_id: string`

        ID of the session (a `sesn_...` value). Look up the session via [Retrieve a session](https://platform.claude.com/docs/en/api/beta/sessions/retrieve?sdk_languages=http) for further provenance.

        minLength: 1

    - `BetaManagedAgentsAPIActor object`

      A direct caller of the public API, identified by the API key that authenticated the request.

      - `type: "api_actor"`

      - `api_key_id: string`

        ID of the API key (an `apikey_...` value). This identifies the key, not the secret.

        minLength: 1

    - `BetaManagedAgentsUserActor object`

      A human user, for example acting through the Anthropic Console.

      - `type: "user_actor"`

      - `user_id: string`

        ID of the user (a `user_...` value).

        minLength: 1

    - `BetaManagedAgentsServiceAccountActor object`

      A workload authenticated as a service account, for example via Workload Identity Federation.

      - `type: "service_account_actor"`

      - `service_account_id: string`

        ID of the service account (a `svac_...` value).

        minLength: 1

  - `path: optional string or null`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `redacted_at: optional string or null`

    When the version was redacted, in RFC 3339, or `null` if it hasn't been.

    When set, `content`, `path`, `content_size_bytes`, and `content_sha256` are `null`.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=http#redact-a-version) to learn more about redaction.

    format: date-time

  - `redacted_by: optional BetaManagedAgentsActor`

    Who redacted this version, or `null` if it has not been redacted. In practice always an `api_actor`, `user_actor`, or `service_account_actor` (agents do not have a redact capability).

#### Example

```bash
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memory_versions/$MEMORY_VERSION_ID \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: agent-memory-2026-07-22' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "memory_id": "memory_id",
  "memory_store_id": "memory_store_id",
  "operation": "created",
  "type": "memory_version",
  "content": "content",
  "content_sha256": "content_sha256",
  "content_size_bytes": 0,
  "created_by": {
    "session_id": "x",
    "type": "session_actor"
  },
  "path": "path",
  "redacted_at": "2019-12-27T18:11:19.117Z",
  "redacted_by": {
    "session_id": "x",
    "type": "session_actor"
  }
}
```

### Redact a Memory Version

**POST** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact`

Redact a Memory Version

#### Path parameters

- `memory_store_id: string`

  The ID of the memory store that holds the version (`memstore_...`).

- `memory_version_id: string`

  The ID of the memory version to redact (`memver_...`).

#### Headers

- `"anthropic-version": optional string`

  The version of the Claude API you want to use.

  Read more about versioning and our version history [here](https://platform.claude.com/docs/en/api/versioning?sdk_languages=http).

- `"anthropic-beta": optional array of AnthropicBeta`

  This endpoint is in beta: requests must send `agent-memory-2026-07-22` or `managed-agents-2026-04-01` in this header.

  - `string`

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

  - `"user-profiles-2026-09-04"`

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

  - `"compact-2026-09-04"`

  - `"inline-tools-2026-09-15"`

  - `"mcp-client-2026-09-15"`

  - `"ce-plugins-2026-09-01"`

  - `"spend-limit-reads-2026-09-26"`

  - `"telemetry-destinations-2026-08-11"`

  - `"webhooks-2026-10-07"`

- `"anthropic-workspace-id": optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `BetaManagedAgentsMemoryVersion object`

  One entry in a memory's history, recording a single change and who made it.

  Every change to a memory adds one version. Only redaction can change a version after that. Versions belong to the memory store and stay after the memory is deleted. Each version is retained for at least the version retention period after it was written, unless the store itself is deleted.

  Retrieving a redacted version succeeds, with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`. Check `redacted_at` to find out whether a version was redacted.

  See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=http#audit-memory-changes) to learn more about memory versions.

  - `type: "memory_version"`

  - `id: string`

    Unique identifier for this version (a `memver_...` value).

  - `created_at: string`

    When this version was written, in RFC 3339 format.

    format: date-time

  - `memory_id: string`

    The ID of the memory that this version belongs to (`mem_...`).

    The ID stays valid after the memory is deleted. Pass it as `memory_id` to [List Memory Versions](https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions/list?sdk_languages=http) to get the memory's retained versions, including its `deleted` version while the lineage is retained.

  - `memory_store_id: string`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `operation: BetaManagedAgentsMemoryVersionOperation`

    The kind of mutation this version records: `created`, `modified`, or `deleted`.

    - `"created"`

      The memory was created. The first version in any memory's lineage.

    - `"modified"`

      The memory's `content`, `path`, or both were changed via update. Writes the agent makes through the filesystem mount also appear as `modified`.

    - `"deleted"`

      The memory was deleted. The `content`, `content_size_bytes`, and `content_sha256` fields are `null` on this version. The preceding version, while it is retained, records the deleted content's size and hash.

  - `content: optional string or null`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `content_sha256: optional string or null`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `content_size_bytes: optional number or null`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

    format: int32

  - `created_by: optional BetaManagedAgentsActor`

    Who made this change to the memory, or `null` if the author wasn't recorded.

    Redacting the version doesn't change this field. A `session_actor` here is an agent that wrote through the store's mounted filesystem at `/mnt/memory/`. The version doesn't record the API key that created that session. So the author in `created_by` is who made the change, not who is ultimately responsible for it.

    You can [retrieve the session](https://platform.claude.com/docs/en/api/beta/sessions/retrieve?sdk_languages=http) to learn more about where the change came from.

    - `BetaManagedAgentsSessionActor object`

      An agent acting during a session, for example through the session's mounted filesystem. It names the session itself, not the user or API key that started the session.

      - `type: "session_actor"`

      - `session_id: string`

        ID of the session (a `sesn_...` value). Look up the session via [Retrieve a session](https://platform.claude.com/docs/en/api/beta/sessions/retrieve?sdk_languages=http) for further provenance.

        minLength: 1

    - `BetaManagedAgentsAPIActor object`

      A direct caller of the public API, identified by the API key that authenticated the request.

      - `type: "api_actor"`

      - `api_key_id: string`

        ID of the API key (an `apikey_...` value). This identifies the key, not the secret.

        minLength: 1

    - `BetaManagedAgentsUserActor object`

      A human user, for example acting through the Anthropic Console.

      - `type: "user_actor"`

      - `user_id: string`

        ID of the user (a `user_...` value).

        minLength: 1

    - `BetaManagedAgentsServiceAccountActor object`

      A workload authenticated as a service account, for example via Workload Identity Federation.

      - `type: "service_account_actor"`

      - `service_account_id: string`

        ID of the service account (a `svac_...` value).

        minLength: 1

  - `path: optional string or null`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `redacted_at: optional string or null`

    When the version was redacted, in RFC 3339, or `null` if it hasn't been.

    When set, `content`, `path`, `content_size_bytes`, and `content_sha256` are `null`.

    See the [memory guide](https://platform.claude.com/docs/en/managed-agents/memory?sdk_languages=http#redact-a-version) to learn more about redaction.

    format: date-time

  - `redacted_by: optional BetaManagedAgentsActor`

    Who redacted this version, or `null` if it has not been redacted. In practice always an `api_actor`, `user_actor`, or `service_account_actor` (agents do not have a redact capability).

#### Example

```bash
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memory_versions/$MEMORY_VERSION_ID/redact \
    -X POST \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: agent-memory-2026-07-22' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

##### Response (200)

```json
{
  "id": "id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "memory_id": "memory_id",
  "memory_store_id": "memory_store_id",
  "operation": "created",
  "type": "memory_version",
  "content": "content",
  "content_sha256": "content_sha256",
  "content_size_bytes": 0,
  "created_by": {
    "session_id": "x",
    "type": "session_actor"
  },
  "path": "path",
  "redacted_at": "2019-12-27T18:11:19.117Z",
  "redacted_by": {
    "session_id": "x",
    "type": "session_actor"
  }
}
```
