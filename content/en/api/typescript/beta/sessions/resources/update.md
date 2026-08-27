# Update Session Resource

`client.beta.sessions.resources.update(resourceID, params, options?): ResourceUpdateResponse`

**POST** `/v1/sessions/{session_id}/resources/{resource_id}`

Update Session Resource

## Parameters

- `resourceID: string`

- `params: ResourceUpdateParams`

  - `session_id: string`

    Path param: Path parameter session_id

  - `authorization_token: string`

    Body param: New authorization token for the resource. Currently only `github_repository` resources support token rotation.

    minLength: 1, maxLength: 4096

  - `betas?: Array<AnthropicBeta>`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `(string & {})`

    - `"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 38 more`

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

      - `"compact-2026-01-12"`

      - `"computer-use-2025-11-24"`

      - `"mcp-tunnels-2026-06-22"`

      - `"structured-outputs-2025-11-13"`

      - `"task-budgets-2026-03-13"`

      - `"thinking-display-updates-2026-08-18"`

      - `"ce-user-management-2026-07-13"`

## Returns

- `ResourceUpdateResponse = BetaManagedAgentsGitHubRepositoryResource | BetaManagedAgentsFileResource | BetaManagedAgentsMemoryStoreResource`

  The updated session resource.

  - `BetaManagedAgentsGitHubRepositoryResource`

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

    - `checkout?: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout | null`

      - `BetaManagedAgentsBranchCheckout`

        - `name: string`

          Branch name to check out.

          minLength: 1, maxLength: 255

        - `type: "branch"`

      - `BetaManagedAgentsCommitCheckout`

        - `sha: string`

          Full commit SHA to check out.

          minLength: 7, maxLength: 64

        - `type: "commit"`

  - `BetaManagedAgentsFileResource`

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

  - `BetaManagedAgentsMemoryStoreResource`

    A memory store attached to an agent session.

    - `memory_store_id: string`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: "memory_store"`

    - `access?: "read_write" | "read_only" | null`

      Access mode for an attached memory store.

      - `"read_write"`

      - `"read_only"`

    - `description?: string`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `instructions?: string | null`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      maxLength: 4096

    - `mount_path?: string | null`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `name?: string | null`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

## Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const resource = await client.beta.sessions.resources.update(
  "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  { session_id: "sesn_011CZkZAtmR3yMPDzynEDxu7", authorization_token: "ghp_exampletoken" }
);

console.log(resource);
```

### Response (200)

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
