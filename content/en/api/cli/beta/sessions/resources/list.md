# List Session Resources

`$ ant beta:sessions:resources list`

**GET** `/v1/sessions/{session_id}/resources`

List Session Resources

## Parameters

- `--session-id: string`

  Path param: Path parameter session_id

- `--limit: optional number`

  Query param: Maximum number of resources to return per page (max 1000). If omitted, returns all resources.

  format: int32

- `--page: optional string`

  Query param: Opaque cursor from a previous response's `next_page` field.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

## Returns

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

## Example

```bash
ant beta:sessions:resources list \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7
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
