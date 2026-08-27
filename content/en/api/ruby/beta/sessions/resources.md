# Resources

## Add Session Resource

`beta.sessions.resources.add(session_id, **kwargs) -> BetaManagedAgentsFileResource`

**POST** `/v1/sessions/{session_id}/resources`

Add Session Resource

### Parameters

- `session_id: String`

- `file_id: String`

  ID of a previously uploaded file.

  minLength: 1, maxLength: 128

- `type: :file`

- `mount_path: String`

  Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

  minLength: 1, maxLength: 4096

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 38 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

    - `:"compact-2026-01-12"`

    - `:"computer-use-2025-11-24"`

    - `:"mcp-tunnels-2026-06-22"`

    - `:"structured-outputs-2025-11-13"`

    - `:"task-budgets-2026-03-13"`

    - `:"thinking-display-updates-2026-08-18"`

    - `:"ce-user-management-2026-07-13"`

### Returns

- `class BetaManagedAgentsFileResource`

  - `id: String`

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `file_id: String`

  - `mount_path: String`

  - `type: :file`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_file_resource = anthropic.beta.sessions.resources.add(
  "sesn_011CZkZAtmR3yMPDzynEDxu7",
  file_id: "file_011CNha8iCJcU1wXNR6q4V8w",
  type: :file
)

puts(beta_managed_agents_file_resource)
```

#### Response (200)

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

## List Session Resources

`beta.sessions.resources.list(session_id, **kwargs) -> PageCursor<BetaManagedAgentsSessionResource>`

**GET** `/v1/sessions/{session_id}/resources`

List Session Resources

### Parameters

- `session_id: String`

- `limit: Integer`

  Maximum number of resources to return per page (max 1000). If omitted, returns all resources.

  format: int32

- `page: String`

  Opaque cursor from a previous response's next_page field.

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 38 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

    - `:"compact-2026-01-12"`

    - `:"computer-use-2025-11-24"`

    - `:"mcp-tunnels-2026-06-22"`

    - `:"structured-outputs-2025-11-13"`

    - `:"task-budgets-2026-03-13"`

    - `:"thinking-display-updates-2026-08-18"`

    - `:"ce-user-management-2026-07-13"`

### Returns

- `BetaManagedAgentsSessionResource = BetaManagedAgentsGitHubRepositoryResource | BetaManagedAgentsFileResource | BetaManagedAgentsMemoryStoreResource`

  A memory store attached to an agent session.

  - `class BetaManagedAgentsGitHubRepositoryResource`

    - `id: String`

    - `created_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `mount_path: String`

    - `type: :github_repository`

    - `updated_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `url: String`

    - `checkout: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout`

      - `class BetaManagedAgentsBranchCheckout`

        - `name: String`

          Branch name to check out.

          minLength: 1, maxLength: 255

        - `type: :branch`

      - `class BetaManagedAgentsCommitCheckout`

        - `sha: String`

          Full commit SHA to check out.

          minLength: 7, maxLength: 64

        - `type: :commit`

  - `class BetaManagedAgentsFileResource`

    - `id: String`

    - `created_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `file_id: String`

    - `mount_path: String`

    - `type: :file`

    - `updated_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsMemoryStoreResource`

    A memory store attached to an agent session.

    - `memory_store_id: String`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: :memory_store`

    - `access: :read_write | :read_only`

      Access mode for an attached memory store.

      - `:read_write`

      - `:read_only`

    - `description: String`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `instructions: String`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      maxLength: 4096

    - `mount_path: String`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `name: String`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.sessions.resources.list("sesn_011CZkZAtmR3yMPDzynEDxu7")

puts(page)
```

#### Response (200)

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

## Get Session Resource

`beta.sessions.resources.retrieve(resource_id, **kwargs) -> ResourceRetrieveResponse`

**GET** `/v1/sessions/{session_id}/resources/{resource_id}`

Get Session Resource

### Parameters

- `session_id: String`

- `resource_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 38 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

    - `:"compact-2026-01-12"`

    - `:"computer-use-2025-11-24"`

    - `:"mcp-tunnels-2026-06-22"`

    - `:"structured-outputs-2025-11-13"`

    - `:"task-budgets-2026-03-13"`

    - `:"thinking-display-updates-2026-08-18"`

    - `:"ce-user-management-2026-07-13"`

### Returns

- `ResourceRetrieveResponse = BetaManagedAgentsGitHubRepositoryResource | BetaManagedAgentsFileResource | BetaManagedAgentsMemoryStoreResource`

  The requested session resource.

  - `class BetaManagedAgentsGitHubRepositoryResource`

    - `id: String`

    - `created_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `mount_path: String`

    - `type: :github_repository`

    - `updated_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `url: String`

    - `checkout: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout`

      - `class BetaManagedAgentsBranchCheckout`

        - `name: String`

          Branch name to check out.

          minLength: 1, maxLength: 255

        - `type: :branch`

      - `class BetaManagedAgentsCommitCheckout`

        - `sha: String`

          Full commit SHA to check out.

          minLength: 7, maxLength: 64

        - `type: :commit`

  - `class BetaManagedAgentsFileResource`

    - `id: String`

    - `created_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `file_id: String`

    - `mount_path: String`

    - `type: :file`

    - `updated_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsMemoryStoreResource`

    A memory store attached to an agent session.

    - `memory_store_id: String`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: :memory_store`

    - `access: :read_write | :read_only`

      Access mode for an attached memory store.

      - `:read_write`

      - `:read_only`

    - `description: String`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `instructions: String`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      maxLength: 4096

    - `mount_path: String`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `name: String`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

resource = anthropic.beta.sessions.resources.retrieve(
  "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  session_id: "sesn_011CZkZAtmR3yMPDzynEDxu7"
)

puts(resource)
```

#### Response (200)

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

## Update Session Resource

`beta.sessions.resources.update(resource_id, **kwargs) -> ResourceUpdateResponse`

**POST** `/v1/sessions/{session_id}/resources/{resource_id}`

Update Session Resource

### Parameters

- `session_id: String`

- `resource_id: String`

- `authorization_token: String`

  New authorization token for the resource. Currently only `github_repository` resources support token rotation.

  minLength: 1, maxLength: 4096

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 38 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

    - `:"compact-2026-01-12"`

    - `:"computer-use-2025-11-24"`

    - `:"mcp-tunnels-2026-06-22"`

    - `:"structured-outputs-2025-11-13"`

    - `:"task-budgets-2026-03-13"`

    - `:"thinking-display-updates-2026-08-18"`

    - `:"ce-user-management-2026-07-13"`

### Returns

- `ResourceUpdateResponse = BetaManagedAgentsGitHubRepositoryResource | BetaManagedAgentsFileResource | BetaManagedAgentsMemoryStoreResource`

  The updated session resource.

  - `class BetaManagedAgentsGitHubRepositoryResource`

    - `id: String`

    - `created_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `mount_path: String`

    - `type: :github_repository`

    - `updated_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `url: String`

    - `checkout: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout`

      - `class BetaManagedAgentsBranchCheckout`

        - `name: String`

          Branch name to check out.

          minLength: 1, maxLength: 255

        - `type: :branch`

      - `class BetaManagedAgentsCommitCheckout`

        - `sha: String`

          Full commit SHA to check out.

          minLength: 7, maxLength: 64

        - `type: :commit`

  - `class BetaManagedAgentsFileResource`

    - `id: String`

    - `created_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `file_id: String`

    - `mount_path: String`

    - `type: :file`

    - `updated_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsMemoryStoreResource`

    A memory store attached to an agent session.

    - `memory_store_id: String`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: :memory_store`

    - `access: :read_write | :read_only`

      Access mode for an attached memory store.

      - `:read_write`

      - `:read_only`

    - `description: String`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `instructions: String`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      maxLength: 4096

    - `mount_path: String`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `name: String`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

resource = anthropic.beta.sessions.resources.update(
  "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  session_id: "sesn_011CZkZAtmR3yMPDzynEDxu7",
  authorization_token: "ghp_exampletoken"
)

puts(resource)
```

#### Response (200)

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

## Delete Session Resource

`beta.sessions.resources.delete(resource_id, **kwargs) -> BetaManagedAgentsDeleteSessionResource`

**DELETE** `/v1/sessions/{session_id}/resources/{resource_id}`

Delete Session Resource

### Parameters

- `session_id: String`

- `resource_id: String`

- `betas: Array[AnthropicBeta]`

  Optional header to specify the beta version(s) you want to use.

  - `String = String`

  - `AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 38 more`

    - `:"message-batches-2024-09-24"`

    - `:"prompt-caching-2024-07-31"`

    - `:"computer-use-2024-10-22"`

    - `:"computer-use-2025-01-24"`

    - `:"pdfs-2024-09-25"`

    - `:"token-counting-2024-11-01"`

    - `:"token-efficient-tools-2025-02-19"`

    - `:"output-128k-2025-02-19"`

    - `:"files-api-2025-04-14"`

    - `:"mcp-client-2025-04-04"`

    - `:"mcp-client-2025-11-20"`

    - `:"dev-full-thinking-2025-05-14"`

    - `:"interleaved-thinking-2025-05-14"`

    - `:"code-execution-2025-05-22"`

    - `:"extended-cache-ttl-2025-04-11"`

    - `:"context-1m-2025-08-07"`

    - `:"context-management-2025-06-27"`

    - `:"model-context-window-exceeded-2025-08-26"`

    - `:"skills-2025-10-02"`

    - `:"fast-mode-2026-02-01"`

    - `:"output-300k-2026-03-24"`

    - `:"user-profiles-2026-03-24"`

    - `:"user-profiles-2026-08-18"`

    - `:"advisor-tool-2026-03-01"`

    - `:"managed-agents-2026-04-01"`

    - `:"cache-diagnosis-2026-04-07"`

    - `:"dreaming-2026-04-21"`

    - `:"thinking-token-count-2026-05-13"`

    - `:"server-side-fallback-2026-06-01"`

    - `:"server-side-fallback-2026-07-01"`

    - `:"fallback-credit-2026-06-01"`

    - `:"fallback-credit-2026-07-01"`

    - `:"agent-memory-2026-07-22"`

    - `:"mid-conversation-tool-changes-2026-07-01"`

    - `:"compact-2026-01-12"`

    - `:"computer-use-2025-11-24"`

    - `:"mcp-tunnels-2026-06-22"`

    - `:"structured-outputs-2025-11-13"`

    - `:"task-budgets-2026-03-13"`

    - `:"thinking-display-updates-2026-08-18"`

    - `:"ce-user-management-2026-07-13"`

### Returns

- `class BetaManagedAgentsDeleteSessionResource`

  Confirmation of resource deletion.

  - `id: String`

  - `type: :session_resource_deleted`

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_delete_session_resource = anthropic.beta.sessions.resources.delete(
  "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  session_id: "sesn_011CZkZAtmR3yMPDzynEDxu7"
)

puts(beta_managed_agents_delete_session_resource)
```

#### Response (200)

```json
{
  "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  "type": "session_resource_deleted"
}
```

## Domain types

### Beta Managed Agents Delete Session Resource

- `class BetaManagedAgentsDeleteSessionResource`

  Confirmation of resource deletion.

  - `id: String`

  - `type: :session_resource_deleted`

### Beta Managed Agents File Resource

- `class BetaManagedAgentsFileResource`

  - `id: String`

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `file_id: String`

  - `mount_path: String`

  - `type: :file`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

### Beta Managed Agents GitHub Repository Resource

- `class BetaManagedAgentsGitHubRepositoryResource`

  - `id: String`

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `mount_path: String`

  - `type: :github_repository`

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `url: String`

  - `checkout: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout`

    - `class BetaManagedAgentsBranchCheckout`

      - `name: String`

        Branch name to check out.

        minLength: 1, maxLength: 255

      - `type: :branch`

    - `class BetaManagedAgentsCommitCheckout`

      - `sha: String`

        Full commit SHA to check out.

        minLength: 7, maxLength: 64

      - `type: :commit`

### Beta Managed Agents Memory Store Resource

- `class BetaManagedAgentsMemoryStoreResource`

  A memory store attached to an agent session.

  - `memory_store_id: String`

    The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

  - `type: :memory_store`

  - `access: :read_write | :read_only`

    Access mode for an attached memory store.

    - `:read_write`

    - `:read_only`

  - `description: String`

    Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

  - `instructions: String`

    Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

    maxLength: 4096

  - `mount_path: String`

    Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

  - `name: String`

    Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

### Beta Managed Agents Session Resource

- `BetaManagedAgentsSessionResource = BetaManagedAgentsGitHubRepositoryResource | BetaManagedAgentsFileResource | BetaManagedAgentsMemoryStoreResource`

  A memory store attached to an agent session.

  - `class BetaManagedAgentsGitHubRepositoryResource`

    - `id: String`

    - `created_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `mount_path: String`

    - `type: :github_repository`

    - `updated_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `url: String`

    - `checkout: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout`

      - `class BetaManagedAgentsBranchCheckout`

        - `name: String`

          Branch name to check out.

          minLength: 1, maxLength: 255

        - `type: :branch`

      - `class BetaManagedAgentsCommitCheckout`

        - `sha: String`

          Full commit SHA to check out.

          minLength: 7, maxLength: 64

        - `type: :commit`

  - `class BetaManagedAgentsFileResource`

    - `id: String`

    - `created_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `file_id: String`

    - `mount_path: String`

    - `type: :file`

    - `updated_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsMemoryStoreResource`

    A memory store attached to an agent session.

    - `memory_store_id: String`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: :memory_store`

    - `access: :read_write | :read_only`

      Access mode for an attached memory store.

      - `:read_write`

      - `:read_only`

    - `description: String`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `instructions: String`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      maxLength: 4096

    - `mount_path: String`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `name: String`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

### Resource Retrieve Response

- `ResourceRetrieveResponse = BetaManagedAgentsGitHubRepositoryResource | BetaManagedAgentsFileResource | BetaManagedAgentsMemoryStoreResource`

  The requested session resource.

  - `class BetaManagedAgentsGitHubRepositoryResource`

    - `id: String`

    - `created_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `mount_path: String`

    - `type: :github_repository`

    - `updated_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `url: String`

    - `checkout: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout`

      - `class BetaManagedAgentsBranchCheckout`

        - `name: String`

          Branch name to check out.

          minLength: 1, maxLength: 255

        - `type: :branch`

      - `class BetaManagedAgentsCommitCheckout`

        - `sha: String`

          Full commit SHA to check out.

          minLength: 7, maxLength: 64

        - `type: :commit`

  - `class BetaManagedAgentsFileResource`

    - `id: String`

    - `created_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `file_id: String`

    - `mount_path: String`

    - `type: :file`

    - `updated_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsMemoryStoreResource`

    A memory store attached to an agent session.

    - `memory_store_id: String`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: :memory_store`

    - `access: :read_write | :read_only`

      Access mode for an attached memory store.

      - `:read_write`

      - `:read_only`

    - `description: String`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `instructions: String`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      maxLength: 4096

    - `mount_path: String`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `name: String`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

### Resource Update Response

- `ResourceUpdateResponse = BetaManagedAgentsGitHubRepositoryResource | BetaManagedAgentsFileResource | BetaManagedAgentsMemoryStoreResource`

  The updated session resource.

  - `class BetaManagedAgentsGitHubRepositoryResource`

    - `id: String`

    - `created_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `mount_path: String`

    - `type: :github_repository`

    - `updated_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `url: String`

    - `checkout: BetaManagedAgentsBranchCheckout | BetaManagedAgentsCommitCheckout`

      - `class BetaManagedAgentsBranchCheckout`

        - `name: String`

          Branch name to check out.

          minLength: 1, maxLength: 255

        - `type: :branch`

      - `class BetaManagedAgentsCommitCheckout`

        - `sha: String`

          Full commit SHA to check out.

          minLength: 7, maxLength: 64

        - `type: :commit`

  - `class BetaManagedAgentsFileResource`

    - `id: String`

    - `created_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

    - `file_id: String`

    - `mount_path: String`

    - `type: :file`

    - `updated_at: Time`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsMemoryStoreResource`

    A memory store attached to an agent session.

    - `memory_store_id: String`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: :memory_store`

    - `access: :read_write | :read_only`

      Access mode for an attached memory store.

      - `:read_write`

      - `:read_only`

    - `description: String`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `instructions: String`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      maxLength: 4096

    - `mount_path: String`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `name: String`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.
