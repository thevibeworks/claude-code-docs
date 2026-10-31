---
title: Vaults
url: https://platform.claude.com/docs/en/api/ruby/beta/vaults
---

# Vaults

## Create a Vault

`beta.vaults.create(**kwargs) -> BetaManagedAgentsVault`

**POST** `/v1/vaults`

Create a Vault

### Parameters

- `display_name: String`

  Human-readable name for the vault. 1-255 characters.

  minLength: 1, maxLength: 255

- `metadata: Hash[Symbol, String]`

  Arbitrary key-value metadata to attach to the vault. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `betas: Array[AnthropicBeta]` (header parameter)

  This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

  - `String = String`

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

  - `:"user-profiles-2026-09-04"`

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

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

  - `:"telemetry-destinations-2026-08-11"`

  - `:"webhooks-2026-10-07"`

  - `:"message-threads-2026-08-12"`

  - `:"analytics-usage-cost-2026-08-24"`

  - `:"experimental-claude-tag-2026-10-21"`

- `workspace_id: String` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsVault`

  A vault that stores credentials for use by agents during sessions.

  - `type: :vault`

  - `id: String`

    The unique ID of the vault (`vlt_...`).

  - `archived_at: Time`

    When the vault was archived. Null if not archived.

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `display_name: String`

    Human-readable name for the vault.

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata attached to the vault.

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_vault = anthropic.beta.vaults.create(display_name: "Example vault")

puts(beta_managed_agents_vault)
```

#### Response (200)

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "display_name": "Example vault",
  "metadata": {
    "environment": "production"
  },
  "type": "vault",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

## List Vaults

`beta.vaults.list(**kwargs) -> PageCursor<BetaManagedAgentsVault>`

**GET** `/v1/vaults`

List Vaults

### Parameters

- `include_archived: bool` (query parameter)

  Whether to include archived vaults in the results. Defaults to `false`.

- `limit: Integer` (query parameter)

  Maximum number of vaults to return per page. Defaults to 20, maximum 100.

  format: int32

- `page: String` (query parameter)

  The `next_page` value from a previous [List Vaults](https://platform.claude.com/docs/en/api/beta/vaults/list?sdk_languages=ruby) response, to get the next page. Leave it out to get the first page.

- `betas: Array[AnthropicBeta]` (header parameter)

  This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

  - `String = String`

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

  - `:"user-profiles-2026-09-04"`

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

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

  - `:"telemetry-destinations-2026-08-11"`

  - `:"webhooks-2026-10-07"`

  - `:"message-threads-2026-08-12"`

  - `:"analytics-usage-cost-2026-08-24"`

  - `:"experimental-claude-tag-2026-10-21"`

- `workspace_id: String` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsVault`

  A vault that stores credentials for use by agents during sessions.

  - `type: :vault`

  - `id: String`

    The unique ID of the vault (`vlt_...`).

  - `archived_at: Time`

    When the vault was archived. Null if not archived.

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `display_name: String`

    Human-readable name for the vault.

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata attached to the vault.

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.vaults.list

puts(page)
```

#### Response (200)

```json
{
  "data": [
    {
      "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "display_name": "Example vault",
      "metadata": {
        "environment": "production"
      },
      "type": "vault",
      "updated_at": "2026-03-15T10:00:00Z"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Retrieve a Vault

`beta.vaults.retrieve(vault_id, **kwargs) -> BetaManagedAgentsVault`

**GET** `/v1/vaults/{vault_id}`

Retrieve a Vault

### Parameters

- `vault_id: String` (path parameter)

  Unique identifier of the vault to retrieve.

- `betas: Array[AnthropicBeta]` (header parameter)

  This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

  - `String = String`

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

  - `:"user-profiles-2026-09-04"`

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

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

  - `:"telemetry-destinations-2026-08-11"`

  - `:"webhooks-2026-10-07"`

  - `:"message-threads-2026-08-12"`

  - `:"analytics-usage-cost-2026-08-24"`

  - `:"experimental-claude-tag-2026-10-21"`

- `workspace_id: String` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsVault`

  A vault that stores credentials for use by agents during sessions.

  - `type: :vault`

  - `id: String`

    The unique ID of the vault (`vlt_...`).

  - `archived_at: Time`

    When the vault was archived. Null if not archived.

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `display_name: String`

    Human-readable name for the vault.

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata attached to the vault.

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_vault = anthropic.beta.vaults.retrieve("vlt_011CZkZDLs7fYzm1hXNPeRjv")

puts(beta_managed_agents_vault)
```

#### Response (200)

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "display_name": "Example vault",
  "metadata": {
    "environment": "production"
  },
  "type": "vault",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

## Update a Vault

`beta.vaults.update(vault_id, **kwargs) -> BetaManagedAgentsVault`

**POST** `/v1/vaults/{vault_id}`

Update a Vault

### Parameters

- `vault_id: String` (path parameter)

  Unique identifier of the vault to update.

- `display_name: String`

  Updated human-readable name for the vault. 1-255 characters.

  minLength: 1, maxLength: 255

- `metadata: Hash[Symbol, String]`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

- `betas: Array[AnthropicBeta]` (header parameter)

  This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

  - `String = String`

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

  - `:"user-profiles-2026-09-04"`

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

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

  - `:"telemetry-destinations-2026-08-11"`

  - `:"webhooks-2026-10-07"`

  - `:"message-threads-2026-08-12"`

  - `:"analytics-usage-cost-2026-08-24"`

  - `:"experimental-claude-tag-2026-10-21"`

- `workspace_id: String` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsVault`

  A vault that stores credentials for use by agents during sessions.

  - `type: :vault`

  - `id: String`

    The unique ID of the vault (`vlt_...`).

  - `archived_at: Time`

    When the vault was archived. Null if not archived.

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `display_name: String`

    Human-readable name for the vault.

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata attached to the vault.

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_vault = anthropic.beta.vaults.update("vlt_011CZkZDLs7fYzm1hXNPeRjv")

puts(beta_managed_agents_vault)
```

#### Response (200)

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "display_name": "Example vault",
  "metadata": {
    "environment": "production"
  },
  "type": "vault",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

## Delete a Vault

`beta.vaults.delete(vault_id, **kwargs) -> BetaManagedAgentsDeletedVault`

**DELETE** `/v1/vaults/{vault_id}`

Delete a Vault

### Parameters

- `vault_id: String` (path parameter)

  Unique identifier of the vault to delete.

- `betas: Array[AnthropicBeta]` (header parameter)

  This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

  - `String = String`

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

  - `:"user-profiles-2026-09-04"`

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

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

  - `:"telemetry-destinations-2026-08-11"`

  - `:"webhooks-2026-10-07"`

  - `:"message-threads-2026-08-12"`

  - `:"analytics-usage-cost-2026-08-24"`

  - `:"experimental-claude-tag-2026-10-21"`

- `workspace_id: String` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsDeletedVault`

  Confirmation of a deleted vault.

  - `type: :vault_deleted`

  - `id: String`

    The unique ID of the deleted vault (`vlt_...`).

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_deleted_vault = anthropic.beta.vaults.delete("vlt_011CZkZDLs7fYzm1hXNPeRjv")

puts(beta_managed_agents_deleted_vault)
```

#### Response (200)

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "type": "vault_deleted"
}
```

## Archive a Vault

`beta.vaults.archive(vault_id, **kwargs) -> BetaManagedAgentsVault`

**POST** `/v1/vaults/{vault_id}/archive`

Archive a Vault

### Parameters

- `vault_id: String` (path parameter)

  Unique identifier of the vault to archive.

- `betas: Array[AnthropicBeta]` (header parameter)

  This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

  - `String = String`

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

  - `:"user-profiles-2026-09-04"`

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

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

  - `:"telemetry-destinations-2026-08-11"`

  - `:"webhooks-2026-10-07"`

  - `:"message-threads-2026-08-12"`

  - `:"analytics-usage-cost-2026-08-24"`

  - `:"experimental-claude-tag-2026-10-21"`

- `workspace_id: String` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsVault`

  A vault that stores credentials for use by agents during sessions.

  - `type: :vault`

  - `id: String`

    The unique ID of the vault (`vlt_...`).

  - `archived_at: Time`

    When the vault was archived. Null if not archived.

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `display_name: String`

    Human-readable name for the vault.

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata attached to the vault.

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_vault = anthropic.beta.vaults.archive("vlt_011CZkZDLs7fYzm1hXNPeRjv")

puts(beta_managed_agents_vault)
```

#### Response (200)

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "display_name": "Example vault",
  "metadata": {
    "environment": "production"
  },
  "type": "vault",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

## Domain types

### Beta Managed Agents Deleted Vault

- `class BetaManagedAgentsDeletedVault`

  Confirmation of a deleted vault.

  - `type: :vault_deleted`

  - `id: String`

    The unique ID of the deleted vault (`vlt_...`).

### Beta Managed Agents Vault

- `class BetaManagedAgentsVault`

  A vault that stores credentials for use by agents during sessions.

  - `type: :vault`

  - `id: String`

    The unique ID of the vault (`vlt_...`).

  - `archived_at: Time`

    When the vault was archived. Null if not archived.

    format: date-time

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `display_name: String`

    Human-readable name for the vault.

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata attached to the vault.

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

## Vaults › Credentials

### Create a Credential

`beta.vaults.credentials.create(vault_id, **kwargs) -> BetaManagedAgentsCredential`

**POST** `/v1/vaults/{vault_id}/credentials`

Create a Credential

#### Parameters

- `vault_id: String` (path parameter)

  Identifier of the vault to create the credential in.

- `auth: BetaManagedAgentsMCPOAuthCreateParams | BetaManagedAgentsStaticBearerCreateParams | BetaManagedAgentsEnvironmentVariableCreateParams`

  Authentication configuration for the credential.

  - `class BetaManagedAgentsMCPOAuthCreateParams`

    Parameters for creating an MCP OAuth credential.

    - `type: :mcp_oauth`

    - `access_token: String`

      The OAuth access token to send to the MCP server.

      minLength: 1, maxLength: 8192

    - `mcp_server_url: String`

      URL of the MCP server this credential authenticates against.

      minLength: 1, maxLength: 2047

    - `expires_at: Time`

      When `access_token` expires, in RFC 3339.

      Must be in the future.

      format: date-time

    - `refresh: BetaManagedAgentsMCPOAuthRefreshParams`

      Refresh token configuration, if the credential supports token refresh.

      - `client_id: String`

        The OAuth client ID to use when refreshing the access token. It can't be changed after the credential is created.

        minLength: 1, maxLength: 1024

      - `refresh_token: String`

        The OAuth refresh token that the API uses to get a new access token when the current one expires.

        minLength: 1, maxLength: 8192

      - `token_endpoint: String`

        Token endpoint URL used to refresh the access token.

        minLength: 1, maxLength: 2047

      - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneParam | BetaManagedAgentsTokenEndpointAuthBasicParam | BetaManagedAgentsTokenEndpointAuthPostParam`

        - `class BetaManagedAgentsTokenEndpointAuthNoneParam`

          Token endpoint requires no client authentication.

          - `type: :none`

        - `class BetaManagedAgentsTokenEndpointAuthBasicParam`

          Token endpoint uses HTTP Basic authentication with client credentials.

          - `type: :client_secret_basic`

          - `client_secret: String`

            The OAuth client secret, sent to `token_endpoint` with HTTP Basic authentication.

            minLength: 1, maxLength: 512

        - `class BetaManagedAgentsTokenEndpointAuthPostParam`

          Token endpoint uses POST body authentication with client credentials.

          - `type: :client_secret_post`

          - `client_secret: String`

            The OAuth client secret, sent to `token_endpoint` in the POST body.

            minLength: 1, maxLength: 512

      - `resource: String`

        OAuth resource indicator.

        minLength: 1, maxLength: 2047

      - `scope: String`

        OAuth scope for the refresh request.

        minLength: 1, maxLength: 8192

  - `class BetaManagedAgentsStaticBearerCreateParams`

    Parameters for creating a static bearer token credential.

    - `type: :static_bearer`

    - `token: String`

      The static bearer token to send to the MCP server, such as an API key or personal access token.

      minLength: 1, maxLength: 8192

    - `mcp_server_url: String`

      URL of the MCP server this credential authenticates against.

      minLength: 1, maxLength: 2047

  - `class BetaManagedAgentsEnvironmentVariableCreateParams`

    Parameters for creating an environment variable credential.

    - `type: :environment_variable`

    - `networking: BetaManagedAgentsCredentialNetworkingParams`

      Outbound hosts the secret value is substituted on.

      - `class BetaManagedAgentsUnrestrictedCredentialNetworkingParams`

        Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

        - `type: :unrestricted`

      - `class BetaManagedAgentsLimitedCredentialNetworkingParams`

        Substitute the secret only on requests to the listed hosts.

        - `type: :limited`

        - `allowed_hosts: Array[String]`

          The destination hosts of the outbound requests that the credential's secret is substituted into.

          Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.` wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses aren't accepted. The list can have up to 16 entries.

    - `secret_name: String`

      Name of the environment variable. Immutable after create.

      minLength: 1, maxLength: 255

    - `secret_value: String`

      The secret to substitute into the agent's outbound requests. It's write-only and never returned in responses.

      minLength: 1, maxLength: 4096

    - `injection_location: BetaManagedAgentsInjectionLocationParams`

      Where in the outbound request the secret value may be substituted.

      - `body: bool`

        Substitute when the placeholder appears in the request body.

      - `header: bool`

        Substitute when the placeholder appears in a request header value.

- `display_name: String`

  Human-readable name for the credential. Up to 255 characters.

  maxLength: 255

- `metadata: Hash[Symbol, String]`

  Arbitrary key-value metadata to attach to the credential. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `betas: Array[AnthropicBeta]` (header parameter)

  This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

  - `String = String`

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

  - `:"user-profiles-2026-09-04"`

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

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

  - `:"telemetry-destinations-2026-08-11"`

  - `:"webhooks-2026-10-07"`

  - `:"message-threads-2026-08-12"`

  - `:"analytics-usage-cost-2026-08-24"`

  - `:"experimental-claude-tag-2026-10-21"`

- `workspace_id: String` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaManagedAgentsCredential`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `type: :vault_credential`

  - `id: String`

    The unique ID of the credential (`vcrd_...`).

  - `archived_at: Time`

    When the credential was archived. Null if not archived.

    format: date-time

  - `auth: BetaManagedAgentsMCPOAuthAuthResponse | BetaManagedAgentsStaticBearerAuthResponse | BetaManagedAgentsEnvironmentVariableAuthResponse`

    Authentication configuration for this credential.

    - `class BetaManagedAgentsMCPOAuthAuthResponse`

      OAuth credential details for an MCP server.

      - `type: :mcp_oauth`

      - `mcp_server_url: String`

        URL of the MCP server this credential authenticates against.

      - `expires_at: Time`

        When the credential's access token expires, in RFC 3339. Absent if the expiry isn't known.

        format: date-time

      - `refresh: BetaManagedAgentsMCPOAuthRefreshResponse`

        Refresh token configuration, if the credential supports token refresh.

        - `client_id: String`

          The OAuth client ID used when refreshing the access token.

        - `token_endpoint: String`

          Token endpoint URL used to refresh the access token.

        - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse | BetaManagedAgentsTokenEndpointAuthBasicResponse | BetaManagedAgentsTokenEndpointAuthPostResponse`

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse`

            Token endpoint requires no client authentication.

            - `type: :none`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: :client_secret_basic`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse`

            Token endpoint uses POST body authentication with client credentials.

            - `type: :client_secret_post`

        - `resource: String`

          OAuth resource indicator.

        - `scope: String`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse`

      Static bearer token credential details for an MCP server.

      - `type: :static_bearer`

      - `mcp_server_url: String`

        URL of the MCP server this credential authenticates against.

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse`

      Environment variable credential details. The secret value is never returned.

      - `type: :environment_variable`

      - `injection_location: BetaManagedAgentsInjectionLocationResponse`

        Where in the outbound request the secret value is substituted.

        - `body: bool`

          Whether the placeholder is substituted in the request body.

        - `header: bool`

          Whether the placeholder is substituted in request header values.

      - `networking: BetaManagedAgentsUnrestrictedCredentialNetworkingResponse | BetaManagedAgentsLimitedCredentialNetworkingResponse`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `type: :unrestricted`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse`

          The secret is substituted only on requests to the listed hosts.

          - `type: :limited`

          - `allowed_hosts: Array[String]`

            The destination hosts of the outbound requests that the credential's secret is substituted into.

            An entry matches the request host exactly. An entry such as `*.example.com` matches any subdomain of `example.com` but not `example.com` itself.

      - `secret_name: String`

        Name of the environment variable.

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata attached to the credential.

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `vault_id: String`

    Identifier of the vault this credential belongs to.

  - `display_name: String`

    Human-readable name for the credential.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_credential = anthropic.beta.vaults.credentials.create(
  "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  auth: {
    token: "bearer_exampletoken",
    mcp_server_url: "https://example-server.modelcontextprotocol.io/sse",
    type: :static_bearer
  }
)

puts(beta_managed_agents_credential)
```

##### Response (200)

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYPQfSkw",
  "archived_at": null,
  "auth": {
    "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
    "type": "static_bearer"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {
    "environment": "production"
  },
  "type": "vault_credential",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "display_name": "Example credential"
}
```

### List Credentials

`beta.vaults.credentials.list(vault_id, **kwargs) -> PageCursor<BetaManagedAgentsCredential>`

**GET** `/v1/vaults/{vault_id}/credentials`

List Credentials

#### Parameters

- `vault_id: String` (path parameter)

  Identifier of the vault to list credentials for.

- `include_archived: bool` (query parameter)

  Whether to include archived credentials in the results. Defaults to `false`.

- `limit: Integer` (query parameter)

  Maximum number of credentials to return per page. Defaults to 20, maximum 100.

  format: int32

- `page: String` (query parameter)

  The `next_page` value from a previous [List Credentials](https://platform.claude.com/docs/en/api/beta/vaults/credentials/list?sdk_languages=ruby) response, to get the next page. Leave it out to get the first page.

- `betas: Array[AnthropicBeta]` (header parameter)

  This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

  - `String = String`

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

  - `:"user-profiles-2026-09-04"`

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

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

  - `:"telemetry-destinations-2026-08-11"`

  - `:"webhooks-2026-10-07"`

  - `:"message-threads-2026-08-12"`

  - `:"analytics-usage-cost-2026-08-24"`

  - `:"experimental-claude-tag-2026-10-21"`

- `workspace_id: String` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaManagedAgentsCredential`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `type: :vault_credential`

  - `id: String`

    The unique ID of the credential (`vcrd_...`).

  - `archived_at: Time`

    When the credential was archived. Null if not archived.

    format: date-time

  - `auth: BetaManagedAgentsMCPOAuthAuthResponse | BetaManagedAgentsStaticBearerAuthResponse | BetaManagedAgentsEnvironmentVariableAuthResponse`

    Authentication configuration for this credential.

    - `class BetaManagedAgentsMCPOAuthAuthResponse`

      OAuth credential details for an MCP server.

      - `type: :mcp_oauth`

      - `mcp_server_url: String`

        URL of the MCP server this credential authenticates against.

      - `expires_at: Time`

        When the credential's access token expires, in RFC 3339. Absent if the expiry isn't known.

        format: date-time

      - `refresh: BetaManagedAgentsMCPOAuthRefreshResponse`

        Refresh token configuration, if the credential supports token refresh.

        - `client_id: String`

          The OAuth client ID used when refreshing the access token.

        - `token_endpoint: String`

          Token endpoint URL used to refresh the access token.

        - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse | BetaManagedAgentsTokenEndpointAuthBasicResponse | BetaManagedAgentsTokenEndpointAuthPostResponse`

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse`

            Token endpoint requires no client authentication.

            - `type: :none`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: :client_secret_basic`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse`

            Token endpoint uses POST body authentication with client credentials.

            - `type: :client_secret_post`

        - `resource: String`

          OAuth resource indicator.

        - `scope: String`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse`

      Static bearer token credential details for an MCP server.

      - `type: :static_bearer`

      - `mcp_server_url: String`

        URL of the MCP server this credential authenticates against.

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse`

      Environment variable credential details. The secret value is never returned.

      - `type: :environment_variable`

      - `injection_location: BetaManagedAgentsInjectionLocationResponse`

        Where in the outbound request the secret value is substituted.

        - `body: bool`

          Whether the placeholder is substituted in the request body.

        - `header: bool`

          Whether the placeholder is substituted in request header values.

      - `networking: BetaManagedAgentsUnrestrictedCredentialNetworkingResponse | BetaManagedAgentsLimitedCredentialNetworkingResponse`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `type: :unrestricted`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse`

          The secret is substituted only on requests to the listed hosts.

          - `type: :limited`

          - `allowed_hosts: Array[String]`

            The destination hosts of the outbound requests that the credential's secret is substituted into.

            An entry matches the request host exactly. An entry such as `*.example.com` matches any subdomain of `example.com` but not `example.com` itself.

      - `secret_name: String`

        Name of the environment variable.

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata attached to the credential.

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `vault_id: String`

    Identifier of the vault this credential belongs to.

  - `display_name: String`

    Human-readable name for the credential.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.vaults.credentials.list("vlt_011CZkZDLs7fYzm1hXNPeRjv")

puts(page)
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "vcrd_011CZkZEMt8gZan2iYPQfSkw",
      "archived_at": null,
      "auth": {
        "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
        "type": "static_bearer"
      },
      "created_at": "2026-03-15T10:00:00Z",
      "metadata": {
        "environment": "production"
      },
      "type": "vault_credential",
      "updated_at": "2026-03-15T10:00:00Z",
      "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
      "display_name": "Example credential"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

### Retrieve a Credential

`beta.vaults.credentials.retrieve(credential_id, **kwargs) -> BetaManagedAgentsCredential`

**GET** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Retrieve a Credential

#### Parameters

- `vault_id: String` (path parameter)

  Identifier of the vault containing the credential.

- `credential_id: String` (path parameter)

  Unique identifier of the credential to retrieve.

- `betas: Array[AnthropicBeta]` (header parameter)

  This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

  - `String = String`

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

  - `:"user-profiles-2026-09-04"`

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

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

  - `:"telemetry-destinations-2026-08-11"`

  - `:"webhooks-2026-10-07"`

  - `:"message-threads-2026-08-12"`

  - `:"analytics-usage-cost-2026-08-24"`

  - `:"experimental-claude-tag-2026-10-21"`

- `workspace_id: String` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaManagedAgentsCredential`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `type: :vault_credential`

  - `id: String`

    The unique ID of the credential (`vcrd_...`).

  - `archived_at: Time`

    When the credential was archived. Null if not archived.

    format: date-time

  - `auth: BetaManagedAgentsMCPOAuthAuthResponse | BetaManagedAgentsStaticBearerAuthResponse | BetaManagedAgentsEnvironmentVariableAuthResponse`

    Authentication configuration for this credential.

    - `class BetaManagedAgentsMCPOAuthAuthResponse`

      OAuth credential details for an MCP server.

      - `type: :mcp_oauth`

      - `mcp_server_url: String`

        URL of the MCP server this credential authenticates against.

      - `expires_at: Time`

        When the credential's access token expires, in RFC 3339. Absent if the expiry isn't known.

        format: date-time

      - `refresh: BetaManagedAgentsMCPOAuthRefreshResponse`

        Refresh token configuration, if the credential supports token refresh.

        - `client_id: String`

          The OAuth client ID used when refreshing the access token.

        - `token_endpoint: String`

          Token endpoint URL used to refresh the access token.

        - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse | BetaManagedAgentsTokenEndpointAuthBasicResponse | BetaManagedAgentsTokenEndpointAuthPostResponse`

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse`

            Token endpoint requires no client authentication.

            - `type: :none`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: :client_secret_basic`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse`

            Token endpoint uses POST body authentication with client credentials.

            - `type: :client_secret_post`

        - `resource: String`

          OAuth resource indicator.

        - `scope: String`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse`

      Static bearer token credential details for an MCP server.

      - `type: :static_bearer`

      - `mcp_server_url: String`

        URL of the MCP server this credential authenticates against.

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse`

      Environment variable credential details. The secret value is never returned.

      - `type: :environment_variable`

      - `injection_location: BetaManagedAgentsInjectionLocationResponse`

        Where in the outbound request the secret value is substituted.

        - `body: bool`

          Whether the placeholder is substituted in the request body.

        - `header: bool`

          Whether the placeholder is substituted in request header values.

      - `networking: BetaManagedAgentsUnrestrictedCredentialNetworkingResponse | BetaManagedAgentsLimitedCredentialNetworkingResponse`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `type: :unrestricted`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse`

          The secret is substituted only on requests to the listed hosts.

          - `type: :limited`

          - `allowed_hosts: Array[String]`

            The destination hosts of the outbound requests that the credential's secret is substituted into.

            An entry matches the request host exactly. An entry such as `*.example.com` matches any subdomain of `example.com` but not `example.com` itself.

      - `secret_name: String`

        Name of the environment variable.

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata attached to the credential.

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `vault_id: String`

    Identifier of the vault this credential belongs to.

  - `display_name: String`

    Human-readable name for the credential.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_credential = anthropic.beta.vaults.credentials.retrieve(
  "vcrd_011CZkZEMt8gZan2iYPQfSkw",
  vault_id: "vlt_011CZkZDLs7fYzm1hXNPeRjv"
)

puts(beta_managed_agents_credential)
```

##### Response (200)

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYPQfSkw",
  "archived_at": null,
  "auth": {
    "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
    "type": "static_bearer"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {
    "environment": "production"
  },
  "type": "vault_credential",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "display_name": "Example credential"
}
```

### Update a Credential

`beta.vaults.credentials.update(credential_id, **kwargs) -> BetaManagedAgentsCredential`

**POST** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Update a Credential

#### Parameters

- `vault_id: String` (path parameter)

  Identifier of the vault containing the credential.

- `credential_id: String` (path parameter)

  Unique identifier of the credential to update.

- `auth: BetaManagedAgentsMCPOAuthUpdateParams | BetaManagedAgentsStaticBearerUpdateParams | BetaManagedAgentsEnvironmentVariableUpdateParams`

  New authentication settings for the credential. The `type` must match the credential's current type, which can't be changed.

  - `class BetaManagedAgentsMCPOAuthUpdateParams`

    Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

    - `type: :mcp_oauth`

    - `access_token: String`

      The new OAuth access token to replace the stored one.

      minLength: 1, maxLength: 8192

    - `expires_at: Time`

      When the credential's access token expires, in RFC 3339. Leave it out to keep the stored expiry.

      If you send a new `access_token`, send its `expires_at` too, or the new token keeps the old expiry.

      Must be in the future.

      format: date-time

    - `refresh: BetaManagedAgentsMCPOAuthRefreshUpdateParams`

      Updated refresh token configuration.

      - `refresh_token: String`

        The new OAuth refresh token to replace the stored one.

        minLength: 1, maxLength: 8192

      - `scope: String`

        The new OAuth scope for refresh requests. Send an empty string to clear the stored scope.

        maxLength: 8192

      - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthBasicUpdateParam | BetaManagedAgentsTokenEndpointAuthPostUpdateParam`

        - `class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam`

          Updated HTTP Basic authentication parameters for the token endpoint.

          - `type: :client_secret_basic`

          - `client_secret: String`

            A new OAuth client secret to replace the stored one.

            The credential must already use `client_secret_basic` or `client_secret_post`. It keeps its current `token_endpoint_auth` type, even if the `type` sent with this secret is the other one.

            minLength: 1, maxLength: 512

        - `class BetaManagedAgentsTokenEndpointAuthPostUpdateParam`

          Updated POST body authentication parameters for the token endpoint.

          - `type: :client_secret_post`

          - `client_secret: String`

            A new OAuth client secret to replace the stored one.

            The credential must already use `client_secret_basic` or `client_secret_post`. It keeps its current `token_endpoint_auth` type, even if the `type` sent with this secret is the other one.

            minLength: 1, maxLength: 512

  - `class BetaManagedAgentsStaticBearerUpdateParams`

    Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

    - `type: :static_bearer`

    - `token: String`

      The new static bearer token to replace the stored one.

      minLength: 1, maxLength: 8192

  - `class BetaManagedAgentsEnvironmentVariableUpdateParams`

    Parameters for updating an environment variable credential. `secret_name` is immutable.

    - `type: :environment_variable`

    - `injection_location: BetaManagedAgentsInjectionLocationUpdateParams`

      Updated injection location.

      - `body: bool`

        Substitute when the placeholder appears in the request body.

      - `header: bool`

        Substitute when the placeholder appears in a request header value.

    - `networking: BetaManagedAgentsCredentialNetworkingParams`

      The new networking scope, which replaces the stored one as a whole.

      - `class BetaManagedAgentsUnrestrictedCredentialNetworkingParams`

        Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

        - `type: :unrestricted`

      - `class BetaManagedAgentsLimitedCredentialNetworkingParams`

        Substitute the secret only on requests to the listed hosts.

        - `type: :limited`

        - `allowed_hosts: Array[String]`

          The destination hosts of the outbound requests that the credential's secret is substituted into.

          Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.` wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses aren't accepted. The list can have up to 16 entries.

    - `secret_value: String`

      The new secret value to replace the stored one.

      minLength: 1, maxLength: 4096

- `display_name: String`

  Updated human-readable name for the credential. 1-255 characters.

  minLength: 1, maxLength: 255

- `metadata: Hash[Symbol, String]`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

- `betas: Array[AnthropicBeta]` (header parameter)

  This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

  - `String = String`

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

  - `:"user-profiles-2026-09-04"`

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

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

  - `:"telemetry-destinations-2026-08-11"`

  - `:"webhooks-2026-10-07"`

  - `:"message-threads-2026-08-12"`

  - `:"analytics-usage-cost-2026-08-24"`

  - `:"experimental-claude-tag-2026-10-21"`

- `workspace_id: String` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaManagedAgentsCredential`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `type: :vault_credential`

  - `id: String`

    The unique ID of the credential (`vcrd_...`).

  - `archived_at: Time`

    When the credential was archived. Null if not archived.

    format: date-time

  - `auth: BetaManagedAgentsMCPOAuthAuthResponse | BetaManagedAgentsStaticBearerAuthResponse | BetaManagedAgentsEnvironmentVariableAuthResponse`

    Authentication configuration for this credential.

    - `class BetaManagedAgentsMCPOAuthAuthResponse`

      OAuth credential details for an MCP server.

      - `type: :mcp_oauth`

      - `mcp_server_url: String`

        URL of the MCP server this credential authenticates against.

      - `expires_at: Time`

        When the credential's access token expires, in RFC 3339. Absent if the expiry isn't known.

        format: date-time

      - `refresh: BetaManagedAgentsMCPOAuthRefreshResponse`

        Refresh token configuration, if the credential supports token refresh.

        - `client_id: String`

          The OAuth client ID used when refreshing the access token.

        - `token_endpoint: String`

          Token endpoint URL used to refresh the access token.

        - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse | BetaManagedAgentsTokenEndpointAuthBasicResponse | BetaManagedAgentsTokenEndpointAuthPostResponse`

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse`

            Token endpoint requires no client authentication.

            - `type: :none`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: :client_secret_basic`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse`

            Token endpoint uses POST body authentication with client credentials.

            - `type: :client_secret_post`

        - `resource: String`

          OAuth resource indicator.

        - `scope: String`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse`

      Static bearer token credential details for an MCP server.

      - `type: :static_bearer`

      - `mcp_server_url: String`

        URL of the MCP server this credential authenticates against.

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse`

      Environment variable credential details. The secret value is never returned.

      - `type: :environment_variable`

      - `injection_location: BetaManagedAgentsInjectionLocationResponse`

        Where in the outbound request the secret value is substituted.

        - `body: bool`

          Whether the placeholder is substituted in the request body.

        - `header: bool`

          Whether the placeholder is substituted in request header values.

      - `networking: BetaManagedAgentsUnrestrictedCredentialNetworkingResponse | BetaManagedAgentsLimitedCredentialNetworkingResponse`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `type: :unrestricted`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse`

          The secret is substituted only on requests to the listed hosts.

          - `type: :limited`

          - `allowed_hosts: Array[String]`

            The destination hosts of the outbound requests that the credential's secret is substituted into.

            An entry matches the request host exactly. An entry such as `*.example.com` matches any subdomain of `example.com` but not `example.com` itself.

      - `secret_name: String`

        Name of the environment variable.

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata attached to the credential.

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `vault_id: String`

    Identifier of the vault this credential belongs to.

  - `display_name: String`

    Human-readable name for the credential.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_credential = anthropic.beta.vaults.credentials.update(
  "vcrd_011CZkZEMt8gZan2iYPQfSkw",
  vault_id: "vlt_011CZkZDLs7fYzm1hXNPeRjv"
)

puts(beta_managed_agents_credential)
```

##### Response (200)

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYPQfSkw",
  "archived_at": null,
  "auth": {
    "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
    "type": "static_bearer"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {
    "environment": "production"
  },
  "type": "vault_credential",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "display_name": "Example credential"
}
```

### Delete a Credential

`beta.vaults.credentials.delete(credential_id, **kwargs) -> BetaManagedAgentsDeletedCredential`

**DELETE** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Delete a Credential

#### Parameters

- `vault_id: String` (path parameter)

  Identifier of the vault containing the credential.

- `credential_id: String` (path parameter)

  Unique identifier of the credential to delete.

- `betas: Array[AnthropicBeta]` (header parameter)

  This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

  - `String = String`

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

  - `:"user-profiles-2026-09-04"`

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

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

  - `:"telemetry-destinations-2026-08-11"`

  - `:"webhooks-2026-10-07"`

  - `:"message-threads-2026-08-12"`

  - `:"analytics-usage-cost-2026-08-24"`

  - `:"experimental-claude-tag-2026-10-21"`

- `workspace_id: String` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaManagedAgentsDeletedCredential`

  Confirmation of a deleted credential.

  - `type: :vault_credential_deleted`

  - `id: String`

    The unique ID of the deleted credential (`vcrd_...`).

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_deleted_credential = anthropic.beta.vaults.credentials.delete(
  "vcrd_011CZkZEMt8gZan2iYPQfSkw",
  vault_id: "vlt_011CZkZDLs7fYzm1hXNPeRjv"
)

puts(beta_managed_agents_deleted_credential)
```

##### Response (200)

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYPQfSkw",
  "type": "vault_credential_deleted"
}
```

### Archive a Credential

`beta.vaults.credentials.archive(credential_id, **kwargs) -> BetaManagedAgentsCredential`

**POST** `/v1/vaults/{vault_id}/credentials/{credential_id}/archive`

Archive a Credential

#### Parameters

- `vault_id: String` (path parameter)

  Identifier of the vault containing the credential.

- `credential_id: String` (path parameter)

  Unique identifier of the credential to archive.

- `betas: Array[AnthropicBeta]` (header parameter)

  This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

  - `String = String`

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

  - `:"user-profiles-2026-09-04"`

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

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

  - `:"telemetry-destinations-2026-08-11"`

  - `:"webhooks-2026-10-07"`

  - `:"message-threads-2026-08-12"`

  - `:"analytics-usage-cost-2026-08-24"`

  - `:"experimental-claude-tag-2026-10-21"`

- `workspace_id: String` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaManagedAgentsCredential`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `type: :vault_credential`

  - `id: String`

    The unique ID of the credential (`vcrd_...`).

  - `archived_at: Time`

    When the credential was archived. Null if not archived.

    format: date-time

  - `auth: BetaManagedAgentsMCPOAuthAuthResponse | BetaManagedAgentsStaticBearerAuthResponse | BetaManagedAgentsEnvironmentVariableAuthResponse`

    Authentication configuration for this credential.

    - `class BetaManagedAgentsMCPOAuthAuthResponse`

      OAuth credential details for an MCP server.

      - `type: :mcp_oauth`

      - `mcp_server_url: String`

        URL of the MCP server this credential authenticates against.

      - `expires_at: Time`

        When the credential's access token expires, in RFC 3339. Absent if the expiry isn't known.

        format: date-time

      - `refresh: BetaManagedAgentsMCPOAuthRefreshResponse`

        Refresh token configuration, if the credential supports token refresh.

        - `client_id: String`

          The OAuth client ID used when refreshing the access token.

        - `token_endpoint: String`

          Token endpoint URL used to refresh the access token.

        - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse | BetaManagedAgentsTokenEndpointAuthBasicResponse | BetaManagedAgentsTokenEndpointAuthPostResponse`

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse`

            Token endpoint requires no client authentication.

            - `type: :none`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: :client_secret_basic`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse`

            Token endpoint uses POST body authentication with client credentials.

            - `type: :client_secret_post`

        - `resource: String`

          OAuth resource indicator.

        - `scope: String`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse`

      Static bearer token credential details for an MCP server.

      - `type: :static_bearer`

      - `mcp_server_url: String`

        URL of the MCP server this credential authenticates against.

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse`

      Environment variable credential details. The secret value is never returned.

      - `type: :environment_variable`

      - `injection_location: BetaManagedAgentsInjectionLocationResponse`

        Where in the outbound request the secret value is substituted.

        - `body: bool`

          Whether the placeholder is substituted in the request body.

        - `header: bool`

          Whether the placeholder is substituted in request header values.

      - `networking: BetaManagedAgentsUnrestrictedCredentialNetworkingResponse | BetaManagedAgentsLimitedCredentialNetworkingResponse`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `type: :unrestricted`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse`

          The secret is substituted only on requests to the listed hosts.

          - `type: :limited`

          - `allowed_hosts: Array[String]`

            The destination hosts of the outbound requests that the credential's secret is substituted into.

            An entry matches the request host exactly. An entry such as `*.example.com` matches any subdomain of `example.com` but not `example.com` itself.

      - `secret_name: String`

        Name of the environment variable.

  - `created_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `metadata: Hash[Symbol, String]`

    Arbitrary key-value metadata attached to the credential.

  - `updated_at: Time`

    A timestamp in RFC 3339 format

    format: date-time

  - `vault_id: String`

    Identifier of the vault this credential belongs to.

  - `display_name: String`

    Human-readable name for the credential.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_credential = anthropic.beta.vaults.credentials.archive(
  "vcrd_011CZkZEMt8gZan2iYPQfSkw",
  vault_id: "vlt_011CZkZDLs7fYzm1hXNPeRjv"
)

puts(beta_managed_agents_credential)
```

##### Response (200)

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYPQfSkw",
  "archived_at": null,
  "auth": {
    "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
    "type": "static_bearer"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {
    "environment": "production"
  },
  "type": "vault_credential",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "display_name": "Example credential"
}
```

### Validate an MCP OAuth Credential

`beta.vaults.credentials.mcp_oauth_validate(credential_id, **kwargs) -> BetaManagedAgentsCredentialValidation`

**POST** `/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate`

Validate an MCP OAuth Credential

#### Parameters

- `vault_id: String` (path parameter)

  Identifier of the vault containing the credential.

- `credential_id: String` (path parameter)

  Unique identifier of the credential to validate.

- `betas: Array[AnthropicBeta]` (header parameter)

  This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

  - `String = String`

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

  - `:"user-profiles-2026-09-04"`

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

  - `:"mid-conversation-output-config-2026-07-01"`

  - `:"thinking-binding-controls-2026-08-01"`

  - `:"mid-conversation-system-clear-at-2026-08-21"`

  - `:"compact-2026-09-04"`

  - `:"inline-tools-2026-09-15"`

  - `:"mcp-client-2026-09-15"`

  - `:"ce-plugins-2026-09-01"`

  - `:"spend-limit-reads-2026-09-26"`

  - `:"telemetry-destinations-2026-08-11"`

  - `:"webhooks-2026-10-07"`

  - `:"message-threads-2026-08-12"`

  - `:"analytics-usage-cost-2026-08-24"`

  - `:"experimental-claude-tag-2026-10-21"`

- `workspace_id: String` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `class BetaManagedAgentsCredentialValidation`

  Result of live-probing a credential against its configured MCP server.

  - `type: :vault_credential_validation`

  - `credential_id: String`

    Unique identifier of the credential that was validated.

  - `has_refresh_token: bool`

    Whether the credential has a refresh token configured.

  - `mcp_probe: BetaManagedAgentsMCPProbe`

    Details of the MCP probe step that failed, or `null` if the probe succeeded or there was no access token to test.

    - `http_response: BetaManagedAgentsRefreshHTTPResponse`

      The HTTP error response from the MCP server, or `null` if the MCP server didn't return one for the failing step, for example after a timeout or a DNS or TLS failure.

      - `body: String`

        Response body. May be truncated and has sensitive values scrubbed.

      - `body_truncated: bool`

        Whether `body` was truncated.

      - `content_type: String`

        Value of the `Content-Type` response header.

      - `status_code: Integer`

        HTTP status code.

        format: int32

    - `method_: String`

      The MCP method that failed (for example `initialize` or `tools/list`).

  - `refresh: BetaManagedAgentsRefreshObject`

    Details of the refresh-token exchange attempted on a 401. Null when no refresh was attempted.

    - `http_response: BetaManagedAgentsRefreshHTTPResponse`

      The captured HTTP error response from the token endpoint. Populated only when `status` is `failed`.

    - `status: :succeeded | :failed | :connect_error | :no_refresh_token`

      Outcome of the refresh attempt.

      - `:succeeded`

        The token endpoint returned a new access token.

      - `:failed`

        The token endpoint returned an error response. See `http_response` for detail.

      - `:connect_error`

        The token endpoint could not be reached (DNS, TLS, or connection error).

      - `:no_refresh_token`

        No refresh token is stored for the credential, so no exchange was attempted.

  - `status: BetaManagedAgentsCredentialValidationStatus`

    Overall verdict of the validation probe.

    - `:valid`

      The credential successfully authenticated against its MCP server.

    - `:invalid`

      The probe reached the MCP server and the server rejected the credential, or no access token is stored. A refresh, if one was tried, didn't recover it. Usually the end user needs to authorize again.

    - `:unknown`

      The probe couldn't tell whether the credential works, for example because of a network error or because a refresh succeeded but the new access token wasn't tested. Validate the credential again to find out.

  - `validated_at: Time`

    When the validation probe was performed.

    format: date-time

  - `vault_id: String`

    Identifier of the vault containing the credential.

#### Example

```ruby
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_credential_validation = anthropic.beta.vaults.credentials.mcp_oauth_validate(
  "vcrd_011CZkZEMt8gZan2iYPQfSkw",
  vault_id: "vlt_011CZkZDLs7fYzm1hXNPeRjv"
)

puts(beta_managed_agents_credential_validation)
```

##### Response (200)

```json
{
  "credential_id": "vcrd_011CZkZEMt8gZan2iYPQfSkw",
  "has_refresh_token": true,
  "mcp_probe": {
    "http_response": {
      "body": "body",
      "body_truncated": true,
      "content_type": "content_type",
      "status_code": 0
    },
    "method": "method"
  },
  "refresh": {
    "http_response": {
      "body": "body",
      "body_truncated": true,
      "content_type": "content_type",
      "status_code": 0
    },
    "status": "succeeded"
  },
  "status": "valid",
  "type": "vault_credential_validation",
  "validated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv"
}
```
