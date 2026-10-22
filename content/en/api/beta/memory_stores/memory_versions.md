---
title: Memory Versions
url: https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions
---

# Memory Versions

## List Memory Versions

**GET** `/v1/memory_stores/{memory_store_id}/memory_versions`

List Memory Versions

### Path parameters

- `memory_store_id: string`

  The ID of the memory store whose version history to list (`memstore_...`).

### Query parameters

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

### Example

```bash
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memory_versions \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: agent-memory-2026-07-22' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

#### Response (200)

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

## Retrieve a Memory Version

**GET** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}`

Retrieve a Memory Version

### Path parameters

- `memory_store_id: string`

  The ID of the memory store that holds the version (`memstore_...`).

- `memory_version_id: string`

  The ID of the memory version to retrieve (`memver_...`).

### Query parameters

- `view: optional BetaManagedAgentsMemoryView`

  Whether a `memory` or `memory_version` in the response includes its `content`. Defaults to `full` on retrieve operations and to `basic` on list, create, and update operations.

  With `full`, list operations return at most 20 items per page.

  - `"basic"`

    Return the object with `content` set to `null`. The `content_size_bytes` and `content_sha256` fields remain populated, so sync clients can diff without fetching content.

  - `"full"`

    Return the object with `content` populated. On list endpoints, `view=full` caps `limit` at 20.

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

### Example

```bash
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memory_versions/$MEMORY_VERSION_ID \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: agent-memory-2026-07-22' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

#### Response (200)

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

## Redact a Memory Version

**POST** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact`

Redact a Memory Version

### Path parameters

- `memory_store_id: string`

  The ID of the memory store that holds the version (`memstore_...`).

- `memory_version_id: string`

  The ID of the memory version to redact (`memver_...`).

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

### Example

```bash
curl https://api.anthropic.com/v1/memory_stores/$MEMORY_STORE_ID/memory_versions/$MEMORY_VERSION_ID/redact \
    -X POST \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: agent-memory-2026-07-22' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

#### Response (200)

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

## Domain types

### Beta Managed Agents Actor

- `BetaManagedAgentsActor = BetaManagedAgentsSessionActor or BetaManagedAgentsAPIActor or BetaManagedAgentsUserActor or BetaManagedAgentsServiceAccountActor`

  Identifies who performed an operation. Recorded when the operation happens and not updated afterwards, so the ID may refer to a user, service account, API key, or session that has since been deleted.

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

### Beta Managed Agents API Actor

- `BetaManagedAgentsAPIActor object`

  A direct caller of the public API, identified by the API key that authenticated the request.

  - `type: "api_actor"`

  - `api_key_id: string`

    ID of the API key (an `apikey_...` value). This identifies the key, not the secret.

    minLength: 1

### Beta Managed Agents Memory Version

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

### Beta Managed Agents Memory Version Operation

- `BetaManagedAgentsMemoryVersionOperation = "created" or "modified" or "deleted"`

  The kind of change that a memory version records.

  Every change to a memory adds one version. If you update a memory and nothing changes, the memory doesn't get a new version.

  - `"created"`

    The memory was created. The first version in any memory's lineage.

  - `"modified"`

    The memory's `content`, `path`, or both were changed via update. Writes the agent makes through the filesystem mount also appear as `modified`.

  - `"deleted"`

    The memory was deleted. The `content`, `content_size_bytes`, and `content_sha256` fields are `null` on this version. The preceding version, while it is retained, records the deleted content's size and hash.

### Beta Managed Agents Service Account Actor

- `BetaManagedAgentsServiceAccountActor object`

  A workload authenticated as a service account, for example via Workload Identity Federation.

  - `type: "service_account_actor"`

  - `service_account_id: string`

    ID of the service account (a `svac_...` value).

    minLength: 1

### Beta Managed Agents Session Actor

- `BetaManagedAgentsSessionActor object`

  An agent acting during a session, for example through the session's mounted filesystem. It names the session itself, not the user or API key that started the session.

  - `type: "session_actor"`

  - `session_id: string`

    ID of the session (a `sesn_...` value). Look up the session via [Retrieve a session](https://platform.claude.com/docs/en/api/beta/sessions/retrieve?sdk_languages=http) for further provenance.

    minLength: 1

### Beta Managed Agents User Actor

- `BetaManagedAgentsUserActor object`

  A human user, for example acting through the Anthropic Console.

  - `type: "user_actor"`

  - `user_id: string`

    ID of the user (a `user_...` value).

    minLength: 1
