---
title: Vaults
url: https://platform.claude.com/docs/en/api/typescript/beta/vaults
---

# Vaults

## Create a Vault

`client.beta.vaults.create(params, options?): BetaManagedAgentsVault`

**POST** `/v1/vaults`

Create a Vault

### Parameters

- `params: VaultCreateParams`

  - `display_name: string`

    Human-readable name for the vault. 1-255 characters.

    minLength: 1, maxLength: 255

  - `metadata?: Record<string, string>`

    Arbitrary key-value metadata to attach to the vault. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `betas?: Array<AnthropicBeta>` (header parameter)

    This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

    - `(string & {})`

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

    - `"message-threads-2026-08-12"`

    - `"analytics-usage-cost-2026-08-24"`

  - `workspace_id?: string` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `interface BetaManagedAgentsVault`

  A vault that stores credentials for use by agents during sessions.

  - `type: "vault"`

  - `id: string`

    The unique ID of the vault (`vlt_...`).

  - `archived_at: string | null`

    When the vault was archived. Null if not archived.

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `display_name: string`

    Human-readable name for the vault.

  - `metadata: Record<string, string>`

    Arbitrary key-value metadata attached to the vault.

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsVault = await client.beta.vaults.create({
  display_name: "Example vault"
});

console.log(betaManagedAgentsVault.id);
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

`client.beta.vaults.list(params?, options?): PageCursor<BetaManagedAgentsVault>`

**GET** `/v1/vaults`

List Vaults

### Parameters

- `params: VaultListParams`

  - `include_archived?: boolean` (query parameter)

    Whether to include archived vaults in the results. Defaults to `false`.

  - `limit?: number` (query parameter)

    Maximum number of vaults to return per page. Defaults to 20, maximum 100.

    format: int32

  - `page?: string` (query parameter)

    The `next_page` value from a previous [List Vaults](https://platform.claude.com/docs/en/api/beta/vaults/list?sdk_languages=typescript) response, to get the next page. Leave it out to get the first page.

  - `betas?: Array<AnthropicBeta>` (header parameter)

    This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

    - `(string & {})`

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

    - `"message-threads-2026-08-12"`

    - `"analytics-usage-cost-2026-08-24"`

  - `workspace_id?: string` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `interface BetaManagedAgentsVault`

  A vault that stores credentials for use by agents during sessions.

  - `type: "vault"`

  - `id: string`

    The unique ID of the vault (`vlt_...`).

  - `archived_at: string | null`

    When the vault was archived. Null if not archived.

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `display_name: string`

    Human-readable name for the vault.

  - `metadata: Record<string, string>`

    Arbitrary key-value metadata attached to the vault.

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaManagedAgentsVault of client.beta.vaults.list()) {
  console.log(betaManagedAgentsVault.id);
}
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

`client.beta.vaults.retrieve(vaultID, params?, options?): BetaManagedAgentsVault`

**GET** `/v1/vaults/{vault_id}`

Retrieve a Vault

### Parameters

- `vaultID: string` (path parameter)

  Unique identifier of the vault to retrieve.

- `params: VaultRetrieveParams`

  - `betas?: Array<AnthropicBeta>` (header parameter)

    This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

    - `(string & {})`

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

    - `"message-threads-2026-08-12"`

    - `"analytics-usage-cost-2026-08-24"`

  - `workspace_id?: string` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `interface BetaManagedAgentsVault`

  A vault that stores credentials for use by agents during sessions.

  - `type: "vault"`

  - `id: string`

    The unique ID of the vault (`vlt_...`).

  - `archived_at: string | null`

    When the vault was archived. Null if not archived.

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `display_name: string`

    Human-readable name for the vault.

  - `metadata: Record<string, string>`

    Arbitrary key-value metadata attached to the vault.

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsVault = await client.beta.vaults.retrieve(
  "vlt_011CZkZDLs7fYzm1hXNPeRjv"
);

console.log(betaManagedAgentsVault.id);
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

`client.beta.vaults.update(vaultID, params, options?): BetaManagedAgentsVault`

**POST** `/v1/vaults/{vault_id}`

Update a Vault

### Parameters

- `vaultID: string` (path parameter)

  Unique identifier of the vault to update.

- `params: VaultUpdateParams`

  - `display_name?: string | null`

    Updated human-readable name for the vault. 1-255 characters.

    minLength: 1, maxLength: 255

  - `metadata?: Record<string, string | null> | null`

    Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

  - `betas?: Array<AnthropicBeta>` (header parameter)

    This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

    - `(string & {})`

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

    - `"message-threads-2026-08-12"`

    - `"analytics-usage-cost-2026-08-24"`

  - `workspace_id?: string` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `interface BetaManagedAgentsVault`

  A vault that stores credentials for use by agents during sessions.

  - `type: "vault"`

  - `id: string`

    The unique ID of the vault (`vlt_...`).

  - `archived_at: string | null`

    When the vault was archived. Null if not archived.

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `display_name: string`

    Human-readable name for the vault.

  - `metadata: Record<string, string>`

    Arbitrary key-value metadata attached to the vault.

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsVault = await client.beta.vaults.update("vlt_011CZkZDLs7fYzm1hXNPeRjv");

console.log(betaManagedAgentsVault.id);
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

`client.beta.vaults.delete(vaultID, params?, options?): BetaManagedAgentsDeletedVault`

**DELETE** `/v1/vaults/{vault_id}`

Delete a Vault

### Parameters

- `vaultID: string` (path parameter)

  Unique identifier of the vault to delete.

- `params: VaultDeleteParams`

  - `betas?: Array<AnthropicBeta>` (header parameter)

    This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

    - `(string & {})`

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

    - `"message-threads-2026-08-12"`

    - `"analytics-usage-cost-2026-08-24"`

  - `workspace_id?: string` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `interface BetaManagedAgentsDeletedVault`

  Confirmation of a deleted vault.

  - `type: "vault_deleted"`

  - `id: string`

    The unique ID of the deleted vault (`vlt_...`).

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsDeletedVault = await client.beta.vaults.delete(
  "vlt_011CZkZDLs7fYzm1hXNPeRjv"
);

console.log(betaManagedAgentsDeletedVault.id);
```

#### Response (200)

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "type": "vault_deleted"
}
```

## Archive a Vault

`client.beta.vaults.archive(vaultID, params?, options?): BetaManagedAgentsVault`

**POST** `/v1/vaults/{vault_id}/archive`

Archive a Vault

### Parameters

- `vaultID: string` (path parameter)

  Unique identifier of the vault to archive.

- `params: VaultArchiveParams`

  - `betas?: Array<AnthropicBeta>` (header parameter)

    This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

    - `(string & {})`

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

    - `"message-threads-2026-08-12"`

    - `"analytics-usage-cost-2026-08-24"`

  - `workspace_id?: string` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `interface BetaManagedAgentsVault`

  A vault that stores credentials for use by agents during sessions.

  - `type: "vault"`

  - `id: string`

    The unique ID of the vault (`vlt_...`).

  - `archived_at: string | null`

    When the vault was archived. Null if not archived.

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `display_name: string`

    Human-readable name for the vault.

  - `metadata: Record<string, string>`

    Arbitrary key-value metadata attached to the vault.

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsVault = await client.beta.vaults.archive(
  "vlt_011CZkZDLs7fYzm1hXNPeRjv"
);

console.log(betaManagedAgentsVault.id);
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

- `interface BetaManagedAgentsDeletedVault`

  Confirmation of a deleted vault.

  - `type: "vault_deleted"`

  - `id: string`

    The unique ID of the deleted vault (`vlt_...`).

### Beta Managed Agents Vault

- `interface BetaManagedAgentsVault`

  A vault that stores credentials for use by agents during sessions.

  - `type: "vault"`

  - `id: string`

    The unique ID of the vault (`vlt_...`).

  - `archived_at: string | null`

    When the vault was archived. Null if not archived.

    format: date-time

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `display_name: string`

    Human-readable name for the vault.

  - `metadata: Record<string, string>`

    Arbitrary key-value metadata attached to the vault.

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

## Vaults › Credentials

### Create a Credential

`client.beta.vaults.credentials.create(vaultID, params, options?): BetaManagedAgentsCredential`

**POST** `/v1/vaults/{vault_id}/credentials`

Create a Credential

#### Parameters

- `vaultID: string` (path parameter)

  Identifier of the vault to create the credential in.

- `params: CredentialCreateParams`

  - `auth: BetaManagedAgentsMCPOAuthCreateParams | BetaManagedAgentsStaticBearerCreateParams | BetaManagedAgentsEnvironmentVariableCreateParams`

    Authentication configuration for the credential.

    - `interface BetaManagedAgentsMCPOAuthCreateParams`

      Parameters for creating an MCP OAuth credential.

      - `type: "mcp_oauth"`

      - `access_token: string`

        The OAuth access token to send to the MCP server.

        minLength: 1, maxLength: 8192

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

        minLength: 1, maxLength: 2047

      - `expires_at?: string | null`

        When `access_token` expires, in RFC 3339.

        Must be in the future.

        format: date-time

      - `refresh?: BetaManagedAgentsMCPOAuthRefreshParams | null`

        Refresh token configuration, if the credential supports token refresh.

        - `client_id: string`

          The OAuth client ID to use when refreshing the access token. It can't be changed after the credential is created.

          minLength: 1, maxLength: 1024

        - `refresh_token: string`

          The OAuth refresh token that the API uses to get a new access token when the current one expires.

          minLength: 1, maxLength: 8192

        - `token_endpoint: string`

          Token endpoint URL used to refresh the access token.

          minLength: 1, maxLength: 2047

        - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneParam | BetaManagedAgentsTokenEndpointAuthBasicParam | BetaManagedAgentsTokenEndpointAuthPostParam`

          - `interface BetaManagedAgentsTokenEndpointAuthNoneParam`

            Token endpoint requires no client authentication.

            - `type: "none"`

          - `interface BetaManagedAgentsTokenEndpointAuthBasicParam`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: "client_secret_basic"`

            - `client_secret: string`

              The OAuth client secret, sent to `token_endpoint` with HTTP Basic authentication.

              minLength: 1, maxLength: 512

          - `interface BetaManagedAgentsTokenEndpointAuthPostParam`

            Token endpoint uses POST body authentication with client credentials.

            - `type: "client_secret_post"`

            - `client_secret: string`

              The OAuth client secret, sent to `token_endpoint` in the POST body.

              minLength: 1, maxLength: 512

        - `resource?: string | null`

          OAuth resource indicator.

          minLength: 1, maxLength: 2047

        - `scope?: string | null`

          OAuth scope for the refresh request.

          minLength: 1, maxLength: 8192

    - `interface BetaManagedAgentsStaticBearerCreateParams`

      Parameters for creating a static bearer token credential.

      - `type: "static_bearer"`

      - `token: string`

        The static bearer token to send to the MCP server, such as an API key or personal access token.

        minLength: 1, maxLength: 8192

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

        minLength: 1, maxLength: 2047

    - `interface BetaManagedAgentsEnvironmentVariableCreateParams`

      Parameters for creating an environment variable credential.

      - `type: "environment_variable"`

      - `networking: BetaManagedAgentsCredentialNetworkingParams`

        Outbound hosts the secret value is substituted on.

        - `interface BetaManagedAgentsUnrestrictedCredentialNetworkingParams`

          Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

          - `type: "unrestricted"`

        - `interface BetaManagedAgentsLimitedCredentialNetworkingParams`

          Substitute the secret only on requests to the listed hosts.

          - `type: "limited"`

          - `allowed_hosts: Array<string>`

            The destination hosts of the outbound requests that the credential's secret is substituted into.

            Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.` wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses aren't accepted. The list can have up to 16 entries.

      - `secret_name: string`

        Name of the environment variable. Immutable after create.

        minLength: 1, maxLength: 255

      - `secret_value: string`

        The secret to substitute into the agent's outbound requests. It's write-only and never returned in responses.

        minLength: 1, maxLength: 4096

      - `injection_location?: BetaManagedAgentsInjectionLocationParams`

        Where in the outbound request the secret value may be substituted.

        - `body?: boolean`

          Substitute when the placeholder appears in the request body.

        - `header?: boolean`

          Substitute when the placeholder appears in a request header value.

  - `display_name?: string | null`

    Human-readable name for the credential. Up to 255 characters.

    maxLength: 255

  - `metadata?: Record<string, string>`

    Arbitrary key-value metadata to attach to the credential. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `betas?: Array<AnthropicBeta>` (header parameter)

    This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

    - `(string & {})`

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

    - `"message-threads-2026-08-12"`

    - `"analytics-usage-cost-2026-08-24"`

  - `workspace_id?: string` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `interface BetaManagedAgentsCredential`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `type: "vault_credential"`

  - `id: string`

    The unique ID of the credential (`vcrd_...`).

  - `archived_at: string | null`

    When the credential was archived. Null if not archived.

    format: date-time

  - `auth: BetaManagedAgentsMCPOAuthAuthResponse | BetaManagedAgentsStaticBearerAuthResponse | BetaManagedAgentsEnvironmentVariableAuthResponse`

    Authentication configuration for this credential.

    - `interface BetaManagedAgentsMCPOAuthAuthResponse`

      OAuth credential details for an MCP server.

      - `type: "mcp_oauth"`

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

      - `expires_at?: string | null`

        When the credential's access token expires, in RFC 3339. Absent if the expiry isn't known.

        format: date-time

      - `refresh?: BetaManagedAgentsMCPOAuthRefreshResponse | null`

        Refresh token configuration, if the credential supports token refresh.

        - `client_id: string`

          The OAuth client ID used when refreshing the access token.

        - `token_endpoint: string`

          Token endpoint URL used to refresh the access token.

        - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse | BetaManagedAgentsTokenEndpointAuthBasicResponse | BetaManagedAgentsTokenEndpointAuthPostResponse`

          - `interface BetaManagedAgentsTokenEndpointAuthNoneResponse`

            Token endpoint requires no client authentication.

            - `type: "none"`

          - `interface BetaManagedAgentsTokenEndpointAuthBasicResponse`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: "client_secret_basic"`

          - `interface BetaManagedAgentsTokenEndpointAuthPostResponse`

            Token endpoint uses POST body authentication with client credentials.

            - `type: "client_secret_post"`

        - `resource?: string | null`

          OAuth resource indicator.

        - `scope?: string | null`

          OAuth scope for the refresh request.

    - `interface BetaManagedAgentsStaticBearerAuthResponse`

      Static bearer token credential details for an MCP server.

      - `type: "static_bearer"`

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

    - `interface BetaManagedAgentsEnvironmentVariableAuthResponse`

      Environment variable credential details. The secret value is never returned.

      - `type: "environment_variable"`

      - `injection_location: BetaManagedAgentsInjectionLocationResponse`

        Where in the outbound request the secret value is substituted.

        - `body: boolean`

          Whether the placeholder is substituted in the request body.

        - `header: boolean`

          Whether the placeholder is substituted in request header values.

      - `networking: BetaManagedAgentsUnrestrictedCredentialNetworkingResponse | BetaManagedAgentsLimitedCredentialNetworkingResponse`

        Outbound hosts the secret value is substituted on.

        - `interface BetaManagedAgentsUnrestrictedCredentialNetworkingResponse`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `type: "unrestricted"`

        - `interface BetaManagedAgentsLimitedCredentialNetworkingResponse`

          The secret is substituted only on requests to the listed hosts.

          - `type: "limited"`

          - `allowed_hosts: Array<string>`

            The destination hosts of the outbound requests that the credential's secret is substituted into.

            An entry matches the request host exactly. An entry such as `*.example.com` matches any subdomain of `example.com` but not `example.com` itself.

      - `secret_name: string`

        Name of the environment variable.

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `metadata: Record<string, string>`

    Arbitrary key-value metadata attached to the credential.

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `vault_id: string`

    Identifier of the vault this credential belongs to.

  - `display_name?: string | null`

    Human-readable name for the credential.

#### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsCredential = await client.beta.vaults.credentials.create(
  "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  {
    auth: {
      token: "bearer_exampletoken",
      mcp_server_url: "https://example-server.modelcontextprotocol.io/sse",
      type: "static_bearer"
    }
  }
);

console.log(betaManagedAgentsCredential.id);
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

`client.beta.vaults.credentials.list(vaultID, params?, options?): PageCursor<BetaManagedAgentsCredential>`

**GET** `/v1/vaults/{vault_id}/credentials`

List Credentials

#### Parameters

- `vaultID: string` (path parameter)

  Identifier of the vault to list credentials for.

- `params: CredentialListParams`

  - `include_archived?: boolean` (query parameter)

    Whether to include archived credentials in the results. Defaults to `false`.

  - `limit?: number` (query parameter)

    Maximum number of credentials to return per page. Defaults to 20, maximum 100.

    format: int32

  - `page?: string` (query parameter)

    The `next_page` value from a previous [List Credentials](https://platform.claude.com/docs/en/api/beta/vaults/credentials/list?sdk_languages=typescript) response, to get the next page. Leave it out to get the first page.

  - `betas?: Array<AnthropicBeta>` (header parameter)

    This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

    - `(string & {})`

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

    - `"message-threads-2026-08-12"`

    - `"analytics-usage-cost-2026-08-24"`

  - `workspace_id?: string` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `interface BetaManagedAgentsCredential`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `type: "vault_credential"`

  - `id: string`

    The unique ID of the credential (`vcrd_...`).

  - `archived_at: string | null`

    When the credential was archived. Null if not archived.

    format: date-time

  - `auth: BetaManagedAgentsMCPOAuthAuthResponse | BetaManagedAgentsStaticBearerAuthResponse | BetaManagedAgentsEnvironmentVariableAuthResponse`

    Authentication configuration for this credential.

    - `interface BetaManagedAgentsMCPOAuthAuthResponse`

      OAuth credential details for an MCP server.

      - `type: "mcp_oauth"`

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

      - `expires_at?: string | null`

        When the credential's access token expires, in RFC 3339. Absent if the expiry isn't known.

        format: date-time

      - `refresh?: BetaManagedAgentsMCPOAuthRefreshResponse | null`

        Refresh token configuration, if the credential supports token refresh.

        - `client_id: string`

          The OAuth client ID used when refreshing the access token.

        - `token_endpoint: string`

          Token endpoint URL used to refresh the access token.

        - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse | BetaManagedAgentsTokenEndpointAuthBasicResponse | BetaManagedAgentsTokenEndpointAuthPostResponse`

          - `interface BetaManagedAgentsTokenEndpointAuthNoneResponse`

            Token endpoint requires no client authentication.

            - `type: "none"`

          - `interface BetaManagedAgentsTokenEndpointAuthBasicResponse`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: "client_secret_basic"`

          - `interface BetaManagedAgentsTokenEndpointAuthPostResponse`

            Token endpoint uses POST body authentication with client credentials.

            - `type: "client_secret_post"`

        - `resource?: string | null`

          OAuth resource indicator.

        - `scope?: string | null`

          OAuth scope for the refresh request.

    - `interface BetaManagedAgentsStaticBearerAuthResponse`

      Static bearer token credential details for an MCP server.

      - `type: "static_bearer"`

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

    - `interface BetaManagedAgentsEnvironmentVariableAuthResponse`

      Environment variable credential details. The secret value is never returned.

      - `type: "environment_variable"`

      - `injection_location: BetaManagedAgentsInjectionLocationResponse`

        Where in the outbound request the secret value is substituted.

        - `body: boolean`

          Whether the placeholder is substituted in the request body.

        - `header: boolean`

          Whether the placeholder is substituted in request header values.

      - `networking: BetaManagedAgentsUnrestrictedCredentialNetworkingResponse | BetaManagedAgentsLimitedCredentialNetworkingResponse`

        Outbound hosts the secret value is substituted on.

        - `interface BetaManagedAgentsUnrestrictedCredentialNetworkingResponse`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `type: "unrestricted"`

        - `interface BetaManagedAgentsLimitedCredentialNetworkingResponse`

          The secret is substituted only on requests to the listed hosts.

          - `type: "limited"`

          - `allowed_hosts: Array<string>`

            The destination hosts of the outbound requests that the credential's secret is substituted into.

            An entry matches the request host exactly. An entry such as `*.example.com` matches any subdomain of `example.com` but not `example.com` itself.

      - `secret_name: string`

        Name of the environment variable.

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `metadata: Record<string, string>`

    Arbitrary key-value metadata attached to the credential.

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `vault_id: string`

    Identifier of the vault this credential belongs to.

  - `display_name?: string | null`

    Human-readable name for the credential.

#### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaManagedAgentsCredential of client.beta.vaults.credentials.list(
  "vlt_011CZkZDLs7fYzm1hXNPeRjv"
)) {
  console.log(betaManagedAgentsCredential.id);
}
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

`client.beta.vaults.credentials.retrieve(credentialID, params, options?): BetaManagedAgentsCredential`

**GET** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Retrieve a Credential

#### Parameters

- `credentialID: string` (path parameter)

  Unique identifier of the credential to retrieve.

- `params: CredentialRetrieveParams`

  - `vault_id: string` (path parameter)

    Identifier of the vault containing the credential.

  - `betas?: Array<AnthropicBeta>` (header parameter)

    This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

    - `(string & {})`

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

    - `"message-threads-2026-08-12"`

    - `"analytics-usage-cost-2026-08-24"`

  - `workspace_id?: string` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `interface BetaManagedAgentsCredential`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `type: "vault_credential"`

  - `id: string`

    The unique ID of the credential (`vcrd_...`).

  - `archived_at: string | null`

    When the credential was archived. Null if not archived.

    format: date-time

  - `auth: BetaManagedAgentsMCPOAuthAuthResponse | BetaManagedAgentsStaticBearerAuthResponse | BetaManagedAgentsEnvironmentVariableAuthResponse`

    Authentication configuration for this credential.

    - `interface BetaManagedAgentsMCPOAuthAuthResponse`

      OAuth credential details for an MCP server.

      - `type: "mcp_oauth"`

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

      - `expires_at?: string | null`

        When the credential's access token expires, in RFC 3339. Absent if the expiry isn't known.

        format: date-time

      - `refresh?: BetaManagedAgentsMCPOAuthRefreshResponse | null`

        Refresh token configuration, if the credential supports token refresh.

        - `client_id: string`

          The OAuth client ID used when refreshing the access token.

        - `token_endpoint: string`

          Token endpoint URL used to refresh the access token.

        - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse | BetaManagedAgentsTokenEndpointAuthBasicResponse | BetaManagedAgentsTokenEndpointAuthPostResponse`

          - `interface BetaManagedAgentsTokenEndpointAuthNoneResponse`

            Token endpoint requires no client authentication.

            - `type: "none"`

          - `interface BetaManagedAgentsTokenEndpointAuthBasicResponse`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: "client_secret_basic"`

          - `interface BetaManagedAgentsTokenEndpointAuthPostResponse`

            Token endpoint uses POST body authentication with client credentials.

            - `type: "client_secret_post"`

        - `resource?: string | null`

          OAuth resource indicator.

        - `scope?: string | null`

          OAuth scope for the refresh request.

    - `interface BetaManagedAgentsStaticBearerAuthResponse`

      Static bearer token credential details for an MCP server.

      - `type: "static_bearer"`

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

    - `interface BetaManagedAgentsEnvironmentVariableAuthResponse`

      Environment variable credential details. The secret value is never returned.

      - `type: "environment_variable"`

      - `injection_location: BetaManagedAgentsInjectionLocationResponse`

        Where in the outbound request the secret value is substituted.

        - `body: boolean`

          Whether the placeholder is substituted in the request body.

        - `header: boolean`

          Whether the placeholder is substituted in request header values.

      - `networking: BetaManagedAgentsUnrestrictedCredentialNetworkingResponse | BetaManagedAgentsLimitedCredentialNetworkingResponse`

        Outbound hosts the secret value is substituted on.

        - `interface BetaManagedAgentsUnrestrictedCredentialNetworkingResponse`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `type: "unrestricted"`

        - `interface BetaManagedAgentsLimitedCredentialNetworkingResponse`

          The secret is substituted only on requests to the listed hosts.

          - `type: "limited"`

          - `allowed_hosts: Array<string>`

            The destination hosts of the outbound requests that the credential's secret is substituted into.

            An entry matches the request host exactly. An entry such as `*.example.com` matches any subdomain of `example.com` but not `example.com` itself.

      - `secret_name: string`

        Name of the environment variable.

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `metadata: Record<string, string>`

    Arbitrary key-value metadata attached to the credential.

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `vault_id: string`

    Identifier of the vault this credential belongs to.

  - `display_name?: string | null`

    Human-readable name for the credential.

#### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsCredential = await client.beta.vaults.credentials.retrieve(
  "vcrd_011CZkZEMt8gZan2iYPQfSkw",
  { vault_id: "vlt_011CZkZDLs7fYzm1hXNPeRjv" }
);

console.log(betaManagedAgentsCredential.id);
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

`client.beta.vaults.credentials.update(credentialID, params, options?): BetaManagedAgentsCredential`

**POST** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Update a Credential

#### Parameters

- `credentialID: string` (path parameter)

  Unique identifier of the credential to update.

- `params: CredentialUpdateParams`

  - `vault_id: string` (path parameter)

    Identifier of the vault containing the credential.

  - `auth?: BetaManagedAgentsMCPOAuthUpdateParams | BetaManagedAgentsStaticBearerUpdateParams | BetaManagedAgentsEnvironmentVariableUpdateParams`

    New authentication settings for the credential. The `type` must match the credential's current type, which can't be changed.

    - `interface BetaManagedAgentsMCPOAuthUpdateParams`

      Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

      - `type: "mcp_oauth"`

      - `access_token?: string | null`

        The new OAuth access token to replace the stored one.

        minLength: 1, maxLength: 8192

      - `expires_at?: string | null`

        When the credential's access token expires, in RFC 3339. Leave it out to keep the stored expiry.

        If you send a new `access_token`, send its `expires_at` too, or the new token keeps the old expiry.

        Must be in the future.

        format: date-time

      - `refresh?: BetaManagedAgentsMCPOAuthRefreshUpdateParams | null`

        Updated refresh token configuration.

        - `refresh_token?: string | null`

          The new OAuth refresh token to replace the stored one.

          minLength: 1, maxLength: 8192

        - `scope?: string | null`

          The new OAuth scope for refresh requests. Send an empty string to clear the stored scope.

          maxLength: 8192

        - `token_endpoint_auth?: BetaManagedAgentsTokenEndpointAuthBasicUpdateParam | BetaManagedAgentsTokenEndpointAuthPostUpdateParam`

          - `interface BetaManagedAgentsTokenEndpointAuthBasicUpdateParam`

            Updated HTTP Basic authentication parameters for the token endpoint.

            - `type: "client_secret_basic"`

            - `client_secret?: string | null`

              A new OAuth client secret to replace the stored one.

              The credential must already use `client_secret_basic` or `client_secret_post`. It keeps its current `token_endpoint_auth` type, even if the `type` sent with this secret is the other one.

              minLength: 1, maxLength: 512

          - `interface BetaManagedAgentsTokenEndpointAuthPostUpdateParam`

            Updated POST body authentication parameters for the token endpoint.

            - `type: "client_secret_post"`

            - `client_secret?: string | null`

              A new OAuth client secret to replace the stored one.

              The credential must already use `client_secret_basic` or `client_secret_post`. It keeps its current `token_endpoint_auth` type, even if the `type` sent with this secret is the other one.

              minLength: 1, maxLength: 512

    - `interface BetaManagedAgentsStaticBearerUpdateParams`

      Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

      - `type: "static_bearer"`

      - `token?: string | null`

        The new static bearer token to replace the stored one.

        minLength: 1, maxLength: 8192

    - `interface BetaManagedAgentsEnvironmentVariableUpdateParams`

      Parameters for updating an environment variable credential. `secret_name` is immutable.

      - `type: "environment_variable"`

      - `injection_location?: BetaManagedAgentsInjectionLocationUpdateParams`

        Updated injection location.

        - `body?: boolean`

          Substitute when the placeholder appears in the request body.

        - `header?: boolean`

          Substitute when the placeholder appears in a request header value.

      - `networking?: BetaManagedAgentsCredentialNetworkingParams | null`

        The new networking scope, which replaces the stored one as a whole.

        - `interface BetaManagedAgentsUnrestrictedCredentialNetworkingParams`

          Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

          - `type: "unrestricted"`

        - `interface BetaManagedAgentsLimitedCredentialNetworkingParams`

          Substitute the secret only on requests to the listed hosts.

          - `type: "limited"`

          - `allowed_hosts: Array<string>`

            The destination hosts of the outbound requests that the credential's secret is substituted into.

            Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.` wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses aren't accepted. The list can have up to 16 entries.

      - `secret_value?: string | null`

        The new secret value to replace the stored one.

        minLength: 1, maxLength: 4096

  - `display_name?: string | null`

    Updated human-readable name for the credential. 1-255 characters.

    minLength: 1, maxLength: 255

  - `metadata?: Record<string, string | null> | null`

    Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

  - `betas?: Array<AnthropicBeta>` (header parameter)

    This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

    - `(string & {})`

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

    - `"message-threads-2026-08-12"`

    - `"analytics-usage-cost-2026-08-24"`

  - `workspace_id?: string` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `interface BetaManagedAgentsCredential`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `type: "vault_credential"`

  - `id: string`

    The unique ID of the credential (`vcrd_...`).

  - `archived_at: string | null`

    When the credential was archived. Null if not archived.

    format: date-time

  - `auth: BetaManagedAgentsMCPOAuthAuthResponse | BetaManagedAgentsStaticBearerAuthResponse | BetaManagedAgentsEnvironmentVariableAuthResponse`

    Authentication configuration for this credential.

    - `interface BetaManagedAgentsMCPOAuthAuthResponse`

      OAuth credential details for an MCP server.

      - `type: "mcp_oauth"`

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

      - `expires_at?: string | null`

        When the credential's access token expires, in RFC 3339. Absent if the expiry isn't known.

        format: date-time

      - `refresh?: BetaManagedAgentsMCPOAuthRefreshResponse | null`

        Refresh token configuration, if the credential supports token refresh.

        - `client_id: string`

          The OAuth client ID used when refreshing the access token.

        - `token_endpoint: string`

          Token endpoint URL used to refresh the access token.

        - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse | BetaManagedAgentsTokenEndpointAuthBasicResponse | BetaManagedAgentsTokenEndpointAuthPostResponse`

          - `interface BetaManagedAgentsTokenEndpointAuthNoneResponse`

            Token endpoint requires no client authentication.

            - `type: "none"`

          - `interface BetaManagedAgentsTokenEndpointAuthBasicResponse`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: "client_secret_basic"`

          - `interface BetaManagedAgentsTokenEndpointAuthPostResponse`

            Token endpoint uses POST body authentication with client credentials.

            - `type: "client_secret_post"`

        - `resource?: string | null`

          OAuth resource indicator.

        - `scope?: string | null`

          OAuth scope for the refresh request.

    - `interface BetaManagedAgentsStaticBearerAuthResponse`

      Static bearer token credential details for an MCP server.

      - `type: "static_bearer"`

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

    - `interface BetaManagedAgentsEnvironmentVariableAuthResponse`

      Environment variable credential details. The secret value is never returned.

      - `type: "environment_variable"`

      - `injection_location: BetaManagedAgentsInjectionLocationResponse`

        Where in the outbound request the secret value is substituted.

        - `body: boolean`

          Whether the placeholder is substituted in the request body.

        - `header: boolean`

          Whether the placeholder is substituted in request header values.

      - `networking: BetaManagedAgentsUnrestrictedCredentialNetworkingResponse | BetaManagedAgentsLimitedCredentialNetworkingResponse`

        Outbound hosts the secret value is substituted on.

        - `interface BetaManagedAgentsUnrestrictedCredentialNetworkingResponse`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `type: "unrestricted"`

        - `interface BetaManagedAgentsLimitedCredentialNetworkingResponse`

          The secret is substituted only on requests to the listed hosts.

          - `type: "limited"`

          - `allowed_hosts: Array<string>`

            The destination hosts of the outbound requests that the credential's secret is substituted into.

            An entry matches the request host exactly. An entry such as `*.example.com` matches any subdomain of `example.com` but not `example.com` itself.

      - `secret_name: string`

        Name of the environment variable.

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `metadata: Record<string, string>`

    Arbitrary key-value metadata attached to the credential.

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `vault_id: string`

    Identifier of the vault this credential belongs to.

  - `display_name?: string | null`

    Human-readable name for the credential.

#### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsCredential = await client.beta.vaults.credentials.update(
  "vcrd_011CZkZEMt8gZan2iYPQfSkw",
  { vault_id: "vlt_011CZkZDLs7fYzm1hXNPeRjv" }
);

console.log(betaManagedAgentsCredential.id);
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

`client.beta.vaults.credentials.delete(credentialID, params, options?): BetaManagedAgentsDeletedCredential`

**DELETE** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Delete a Credential

#### Parameters

- `credentialID: string` (path parameter)

  Unique identifier of the credential to delete.

- `params: CredentialDeleteParams`

  - `vault_id: string` (path parameter)

    Identifier of the vault containing the credential.

  - `betas?: Array<AnthropicBeta>` (header parameter)

    This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

    - `(string & {})`

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

    - `"message-threads-2026-08-12"`

    - `"analytics-usage-cost-2026-08-24"`

  - `workspace_id?: string` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `interface BetaManagedAgentsDeletedCredential`

  Confirmation of a deleted credential.

  - `type: "vault_credential_deleted"`

  - `id: string`

    The unique ID of the deleted credential (`vcrd_...`).

#### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsDeletedCredential = await client.beta.vaults.credentials.delete(
  "vcrd_011CZkZEMt8gZan2iYPQfSkw",
  { vault_id: "vlt_011CZkZDLs7fYzm1hXNPeRjv" }
);

console.log(betaManagedAgentsDeletedCredential.id);
```

##### Response (200)

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYPQfSkw",
  "type": "vault_credential_deleted"
}
```

### Archive a Credential

`client.beta.vaults.credentials.archive(credentialID, params, options?): BetaManagedAgentsCredential`

**POST** `/v1/vaults/{vault_id}/credentials/{credential_id}/archive`

Archive a Credential

#### Parameters

- `credentialID: string` (path parameter)

  Unique identifier of the credential to archive.

- `params: CredentialArchiveParams`

  - `vault_id: string` (path parameter)

    Identifier of the vault containing the credential.

  - `betas?: Array<AnthropicBeta>` (header parameter)

    This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

    - `(string & {})`

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

    - `"message-threads-2026-08-12"`

    - `"analytics-usage-cost-2026-08-24"`

  - `workspace_id?: string` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `interface BetaManagedAgentsCredential`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `type: "vault_credential"`

  - `id: string`

    The unique ID of the credential (`vcrd_...`).

  - `archived_at: string | null`

    When the credential was archived. Null if not archived.

    format: date-time

  - `auth: BetaManagedAgentsMCPOAuthAuthResponse | BetaManagedAgentsStaticBearerAuthResponse | BetaManagedAgentsEnvironmentVariableAuthResponse`

    Authentication configuration for this credential.

    - `interface BetaManagedAgentsMCPOAuthAuthResponse`

      OAuth credential details for an MCP server.

      - `type: "mcp_oauth"`

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

      - `expires_at?: string | null`

        When the credential's access token expires, in RFC 3339. Absent if the expiry isn't known.

        format: date-time

      - `refresh?: BetaManagedAgentsMCPOAuthRefreshResponse | null`

        Refresh token configuration, if the credential supports token refresh.

        - `client_id: string`

          The OAuth client ID used when refreshing the access token.

        - `token_endpoint: string`

          Token endpoint URL used to refresh the access token.

        - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse | BetaManagedAgentsTokenEndpointAuthBasicResponse | BetaManagedAgentsTokenEndpointAuthPostResponse`

          - `interface BetaManagedAgentsTokenEndpointAuthNoneResponse`

            Token endpoint requires no client authentication.

            - `type: "none"`

          - `interface BetaManagedAgentsTokenEndpointAuthBasicResponse`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: "client_secret_basic"`

          - `interface BetaManagedAgentsTokenEndpointAuthPostResponse`

            Token endpoint uses POST body authentication with client credentials.

            - `type: "client_secret_post"`

        - `resource?: string | null`

          OAuth resource indicator.

        - `scope?: string | null`

          OAuth scope for the refresh request.

    - `interface BetaManagedAgentsStaticBearerAuthResponse`

      Static bearer token credential details for an MCP server.

      - `type: "static_bearer"`

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

    - `interface BetaManagedAgentsEnvironmentVariableAuthResponse`

      Environment variable credential details. The secret value is never returned.

      - `type: "environment_variable"`

      - `injection_location: BetaManagedAgentsInjectionLocationResponse`

        Where in the outbound request the secret value is substituted.

        - `body: boolean`

          Whether the placeholder is substituted in the request body.

        - `header: boolean`

          Whether the placeholder is substituted in request header values.

      - `networking: BetaManagedAgentsUnrestrictedCredentialNetworkingResponse | BetaManagedAgentsLimitedCredentialNetworkingResponse`

        Outbound hosts the secret value is substituted on.

        - `interface BetaManagedAgentsUnrestrictedCredentialNetworkingResponse`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `type: "unrestricted"`

        - `interface BetaManagedAgentsLimitedCredentialNetworkingResponse`

          The secret is substituted only on requests to the listed hosts.

          - `type: "limited"`

          - `allowed_hosts: Array<string>`

            The destination hosts of the outbound requests that the credential's secret is substituted into.

            An entry matches the request host exactly. An entry such as `*.example.com` matches any subdomain of `example.com` but not `example.com` itself.

      - `secret_name: string`

        Name of the environment variable.

  - `created_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `metadata: Record<string, string>`

    Arbitrary key-value metadata attached to the credential.

  - `updated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `vault_id: string`

    Identifier of the vault this credential belongs to.

  - `display_name?: string | null`

    Human-readable name for the credential.

#### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsCredential = await client.beta.vaults.credentials.archive(
  "vcrd_011CZkZEMt8gZan2iYPQfSkw",
  { vault_id: "vlt_011CZkZDLs7fYzm1hXNPeRjv" }
);

console.log(betaManagedAgentsCredential.id);
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

`client.beta.vaults.credentials.mcpOAuthValidate(credentialID, params, options?): BetaManagedAgentsCredentialValidation`

**POST** `/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate`

Validate an MCP OAuth Credential

#### Parameters

- `credentialID: string` (path parameter)

  Unique identifier of the credential to validate.

- `params: CredentialMCPOAuthValidateParams`

  - `vault_id: string` (path parameter)

    Identifier of the vault containing the credential.

  - `betas?: Array<AnthropicBeta>` (header parameter)

    This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

    - `(string & {})`

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

    - `"message-threads-2026-08-12"`

    - `"analytics-usage-cost-2026-08-24"`

  - `workspace_id?: string` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

#### Returns

- `interface BetaManagedAgentsCredentialValidation`

  Result of live-probing a credential against its configured MCP server.

  - `type: "vault_credential_validation"`

  - `credential_id: string`

    Unique identifier of the credential that was validated.

  - `has_refresh_token: boolean`

    Whether the credential has a refresh token configured.

  - `mcp_probe: BetaManagedAgentsMCPProbe | null`

    Details of the MCP probe step that failed, or `null` if the probe succeeded or there was no access token to test.

    - `http_response: BetaManagedAgentsRefreshHTTPResponse | null`

      The HTTP error response from the MCP server, or `null` if the MCP server didn't return one for the failing step, for example after a timeout or a DNS or TLS failure.

      - `body: string`

        Response body. May be truncated and has sensitive values scrubbed.

      - `body_truncated: boolean`

        Whether `body` was truncated.

      - `content_type: string`

        Value of the `Content-Type` response header.

      - `status_code: number`

        HTTP status code.

        format: int32

    - `method: string`

      The MCP method that failed (for example `initialize` or `tools/list`).

  - `refresh: BetaManagedAgentsRefreshObject | null`

    Details of the refresh-token exchange attempted on a 401. Null when no refresh was attempted.

    - `http_response: BetaManagedAgentsRefreshHTTPResponse | null`

      The captured HTTP error response from the token endpoint. Populated only when `status` is `failed`.

    - `status: "succeeded" | "failed" | "connect_error" | "no_refresh_token"`

      Outcome of the refresh attempt.

      - `"succeeded"`

        The token endpoint returned a new access token.

      - `"failed"`

        The token endpoint returned an error response. See `http_response` for detail.

      - `"connect_error"`

        The token endpoint could not be reached (DNS, TLS, or connection error).

      - `"no_refresh_token"`

        No refresh token is stored for the credential, so no exchange was attempted.

  - `status: BetaManagedAgentsCredentialValidationStatus`

    Overall verdict of the validation probe.

    - `"valid"`

      The credential successfully authenticated against its MCP server.

    - `"invalid"`

      The probe reached the MCP server and the server rejected the credential, or no access token is stored. A refresh, if one was tried, didn't recover it. Usually the end user needs to authorize again.

    - `"unknown"`

      The probe couldn't tell whether the credential works, for example because of a network error or because a refresh succeeded but the new access token wasn't tested. Validate the credential again to find out.

  - `validated_at: string`

    When the validation probe was performed.

    format: date-time

  - `vault_id: string`

    Identifier of the vault containing the credential.

#### Example

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env["ANTHROPIC_API_KEY"] // This is the default and can be omitted
});

const betaManagedAgentsCredentialValidation =
  await client.beta.vaults.credentials.mcpOAuthValidate("vcrd_011CZkZEMt8gZan2iYPQfSkw", {
    vault_id: "vlt_011CZkZDLs7fYzm1hXNPeRjv"
  });

console.log(betaManagedAgentsCredentialValidation.credential_id);
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
