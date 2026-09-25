---
title: List Credentials
url: https://platform.claude.com/docs/en/api/php/beta/vaults/credentials/list
---

# List Credentials

`$client->beta->vaults->credentials->list(string vaultID, ?bool includeArchived, ?int limit, ?string page, ?list<AnthropicBeta> betas, ?string workspaceID): PageCursor<ManagedAgentsCredential>`

**GET** `/v1/vaults/{vault_id}/credentials`

List Credentials

## Parameters

- `vaultID: string`

  Identifier of the vault to list credentials for.

- `includeArchived?:optional bool`

  Whether to include archived credentials in the results.

- `limit?:optional int`

  Maximum number of credentials to return per page. Defaults to 20, maximum 100.

- `page?:optional string`

  Opaque pagination token from a previous `list_credentials` response.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

- `workspaceID?:optional string`

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `class ManagedAgentsCredential`

  - `Type type`

  - `string id`

    Unique identifier for the credential.

  - `?\Datetime archivedAt`

    When the credential was archived. Null if not archived.

  - `Auth auth`

    Authentication configuration for this credential.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `array<string,string> metadata`

    Arbitrary key-value metadata attached to the credential.

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `string vaultID`

    Identifier of the vault this credential belongs to.

  - `?string displayName`

    Human-readable name for the credential.

## Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->vaults->credentials->list(
  'vlt_011CZkZDLs7fYzm1hXNPeRjv',
  includeArchived: true,
  limit: 0,
  page: 'page',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($page);
```

### Response (200)

```json
{
  "data": [
    {
      "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
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
