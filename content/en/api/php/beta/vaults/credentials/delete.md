---
title: Delete a Credential
url: https://platform.claude.com/docs/en/api/php/beta/vaults/credentials/delete
---

# Delete a Credential

`$client->beta->vaults->credentials->delete(string credentialID, string vaultID, ?list<AnthropicBeta> betas, ?string workspaceID): ManagedAgentsDeletedCredential`

**DELETE** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Delete a Credential

## Parameters

- `vaultID: string` (path parameter)

  Identifier of the vault containing the credential.

- `credentialID: string` (path parameter)

  Unique identifier of the credential to delete.

- `betas?:optional list<AnthropicBeta>` (header parameter)

  This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

- `workspaceID?:optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `class ManagedAgentsDeletedCredential`

  - `"vault_credential_deleted" type`

  - `string id`

    The unique ID of the deleted credential (`vcrd_...`).

## Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

use Anthropic\Client;
use Anthropic\Beta\AnthropicBeta;

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeletedCredential = $client
  ->beta
  ->vaults
  ->credentials
  ->delete(
  'vcrd_011CZkZEMt8gZan2iYPQfSkw',
  vaultID: 'vlt_011CZkZDLs7fYzm1hXNPeRjv',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsDeletedCredential);
```

### Response (200)

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYPQfSkw",
  "type": "vault_credential_deleted"
}
```
