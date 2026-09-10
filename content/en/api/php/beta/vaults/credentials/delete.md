---
title: Delete Credential
url: https://platform.claude.com/docs/en/api/php/beta/vaults/credentials/delete
---

# Delete Credential

`$client->beta->vaults->credentials->delete(string credentialID, string vaultID, ?list<AnthropicBeta> betas, ?string workspaceID): ManagedAgentsDeletedCredential`

**DELETE** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Delete Credential

## Parameters

- `vaultID: string`

- `credentialID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

## Returns

- `ManagedAgentsDeletedCredential`

  - `Type type`

  - `string id`

    Unique identifier of the deleted credential.

## Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeletedCredential = $client
  ->beta
  ->vaults
  ->credentials
  ->delete(
  'vcrd_011CZkZEMt8gZan2iYOQfSkw',
  vaultID: 'vlt_011CZkZDLs7fYzm1hXNPeRjv',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsDeletedCredential);
```

### Response (200)

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "type": "vault_credential_deleted"
}
```
