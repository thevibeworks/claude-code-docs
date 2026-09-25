---
title: Update Vault
url: https://platform.claude.com/docs/en/api/php/beta/vaults/update
---

# Update Vault

`$client->beta->vaults->update(string vaultID, ?string displayName, ?array<string,string> metadata, ?list<AnthropicBeta> betas, ?string workspaceID): BetaManagedAgentsVault`

**POST** `/v1/vaults/{vault_id}`

Update Vault

## Parameters

- `vaultID: string`

  Unique identifier of the vault to update.

- `displayName?:optional string`

  Updated human-readable name for the vault. 1-255 characters.

- `metadata?:optional array<string,string>`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `class BetaManagedAgentsVault`

  - `Type type`

  - `string id`

    Unique identifier for the vault.

  - `?\Datetime archivedAt`

    When the vault was archived. Null if not archived.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string displayName`

    Human-readable name for the vault.

  - `array<string,string> metadata`

    Arbitrary key-value metadata attached to the vault.

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

## Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsVault = $client->beta->vaults->update(
  'vlt_011CZkZDLs7fYzm1hXNPeRjv',
  displayName: 'Example vault',
  metadata: ['environment' => 'production'],
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsVault);
```

### Response (200)

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
