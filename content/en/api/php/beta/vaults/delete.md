---
title: Delete Vault
url: https://platform.claude.com/docs/en/api/php/beta/vaults/delete
---

# Delete Vault

`$client->beta->vaults->delete(string vaultID, ?list<AnthropicBeta> betas, ?string workspaceID): BetaManagedAgentsDeletedVault`

**DELETE** `/v1/vaults/{vault_id}`

Delete Vault

## Parameters

- `vaultID: string`

  Unique identifier of the vault to delete.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `class BetaManagedAgentsDeletedVault`

  - `Type type`

  - `string id`

    Unique identifier of the deleted vault.

## Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeletedVault = $client->beta->vaults->delete(
  'vlt_011CZkZDLs7fYzm1hXNPeRjv',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsDeletedVault);
```

### Response (200)

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "type": "vault_deleted"
}
```
