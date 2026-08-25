# List Session Resources

**GET** `/v1/sessions/{session_id}/resources`

List Session Resources

## Path parameters

- `session_id: string`

## Query parameters

- `limit: optional number`

  Maximum number of resources to return per page (max 1000). If omitted, returns all resources.

  format: int32

- `page: optional string`

  Opaque cursor from a previous response's next_page field.

## Headers

- `"anthropic-beta": optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

  - `string`

  - `"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 31 more`

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

## Returns

- `data: array of BetaManagedAgentsSessionResource`

  Resources for the session, ordered by `created_at`.

  - `BetaManagedAgentsGitHubRepositoryResource object`

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

    - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout or null`

      - `BetaManagedAgentsBranchCheckout object`

        - `name: string`

          Branch name to check out.

          minLength: 1, maxLength: 255

        - `type: "branch"`

      - `BetaManagedAgentsCommitCheckout object`

        - `sha: string`

          Full commit SHA to check out.

          minLength: 7, maxLength: 64

        - `type: "commit"`

  - `BetaManagedAgentsFileResource object`

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

  - `BetaManagedAgentsMemoryStoreResource object`

    A memory store attached to an agent session.

    - `memory_store_id: string`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: "memory_store"`

    - `access: optional "read_write" or "read_only" or null`

      Access mode for an attached memory store.

      - `"read_write"`

      - `"read_only"`

    - `description: optional string`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `instructions: optional string or null`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      maxLength: 4096

    - `mount_path: optional string or null`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `name: optional string or null`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

- `next_page: optional string or null`

  Opaque cursor for the next page. Null when no more results.

## Example

```bash
curl https://api.anthropic.com/v1/sessions/$SESSION_ID/resources \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

### Response (200)

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
