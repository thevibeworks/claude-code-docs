# Vaults

## Create Vault

`$client->beta->vaults->create(string displayName, ?array<string,string> metadata, ?list<AnthropicBeta> betas): BetaManagedAgentsVault`

**POST** `/v1/vaults`

Create Vault

### Parameters

- `displayName: string`

  Human-readable name for the vault. 1-255 characters.

- `metadata?:optional array<string,string>`

  Arbitrary key-value metadata to attach to the vault. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsVault`

  - `string id`

    Unique identifier for the vault.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string displayName`

    Human-readable name for the vault.

  - `array<string,string> metadata`

    Arbitrary key-value metadata attached to the vault.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsVault = $client->beta->vaults->create(
  displayName: 'Example vault',
  metadata: ['environment' => 'production'],
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
);

var_dump($betaManagedAgentsVault);
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

`$client->beta->vaults->list(?bool includeArchived, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<BetaManagedAgentsVault>`

**GET** `/v1/vaults`

List Vaults

### Parameters

- `includeArchived?:optional bool`

  Whether to include archived vaults in the results.

- `limit?:optional int`

  Maximum number of vaults to return per page. Defaults to 20, maximum 100.

- `page?:optional string`

  Opaque pagination token from a previous `list_vaults` response.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsVault`

  - `string id`

    Unique identifier for the vault.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string displayName`

    Human-readable name for the vault.

  - `array<string,string> metadata`

    Arbitrary key-value metadata attached to the vault.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->vaults->list(
  includeArchived: true,
  limit: 0,
  page: 'page',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
);

var_dump($page);
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

## Get Vault

`$client->beta->vaults->retrieve(string vaultID, ?list<AnthropicBeta> betas): BetaManagedAgentsVault`

**GET** `/v1/vaults/{vault_id}`

Get Vault

### Parameters

- `vaultID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsVault`

  - `string id`

    Unique identifier for the vault.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string displayName`

    Human-readable name for the vault.

  - `array<string,string> metadata`

    Arbitrary key-value metadata attached to the vault.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsVault = $client->beta->vaults->retrieve(
  'vlt_011CZkZDLs7fYzm1hXNPeRjv',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
);

var_dump($betaManagedAgentsVault);
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

## Update Vault

`$client->beta->vaults->update(string vaultID, ?string displayName, ?array<string,string> metadata, ?list<AnthropicBeta> betas): BetaManagedAgentsVault`

**POST** `/v1/vaults/{vault_id}`

Update Vault

### Parameters

- `vaultID: string`

- `displayName?:optional string`

  Updated human-readable name for the vault. 1-255 characters.

- `metadata?:optional array<string,string>`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsVault`

  - `string id`

    Unique identifier for the vault.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string displayName`

    Human-readable name for the vault.

  - `array<string,string> metadata`

    Arbitrary key-value metadata attached to the vault.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsVault = $client->beta->vaults->update(
  'vlt_011CZkZDLs7fYzm1hXNPeRjv',
  displayName: 'Example vault',
  metadata: ['environment' => 'production'],
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
);

var_dump($betaManagedAgentsVault);
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

## Delete Vault

`$client->beta->vaults->delete(string vaultID, ?list<AnthropicBeta> betas): BetaManagedAgentsDeletedVault`

**DELETE** `/v1/vaults/{vault_id}`

Delete Vault

### Parameters

- `vaultID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsDeletedVault`

  - `string id`

    Unique identifier of the deleted vault.

  - `Type type`

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsDeletedVault = $client->beta->vaults->delete(
  'vlt_011CZkZDLs7fYzm1hXNPeRjv',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
);

var_dump($betaManagedAgentsDeletedVault);
```

#### Response (200)

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "type": "vault_deleted"
}
```

## Archive Vault

`$client->beta->vaults->archive(string vaultID, ?list<AnthropicBeta> betas): BetaManagedAgentsVault`

**POST** `/v1/vaults/{vault_id}/archive`

Archive Vault

### Parameters

- `vaultID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsVault`

  - `string id`

    Unique identifier for the vault.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string displayName`

    Human-readable name for the vault.

  - `array<string,string> metadata`

    Arbitrary key-value metadata attached to the vault.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsVault = $client->beta->vaults->archive(
  'vlt_011CZkZDLs7fYzm1hXNPeRjv',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
);

var_dump($betaManagedAgentsVault);
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

- `BetaManagedAgentsDeletedVault`

  - `string id`

    Unique identifier of the deleted vault.

  - `Type type`

### Beta Managed Agents Vault

- `BetaManagedAgentsVault`

  - `string id`

    Unique identifier for the vault.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `string displayName`

    Human-readable name for the vault.

  - `array<string,string> metadata`

    Arbitrary key-value metadata attached to the vault.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

## Vaults › Credentials

### Create Credential

`$client->beta->vaults->credentials->create(string vaultID, Auth auth, ?string displayName, ?array<string,string> metadata, ?list<AnthropicBeta> betas): ManagedAgentsCredential`

**POST** `/v1/vaults/{vault_id}/credentials`

Create Credential

#### Parameters

- `vaultID: string`

- `auth: Auth`

  Authentication details for creating a credential.

- `displayName?:optional string`

  Human-readable name for the credential. Up to 255 characters.

- `metadata?:optional array<string,string>`

  Arbitrary key-value metadata to attach to the credential. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

#### Returns

- `ManagedAgentsCredential`

  - `string id`

    Unique identifier for the credential.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `Auth auth`

    Authentication details for a credential.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `array<string,string> metadata`

    Arbitrary key-value metadata attached to the credential.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `string vaultID`

    Identifier of the vault this credential belongs to.

  - `?string displayName`

    Human-readable name for the credential.

#### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsCredential = $client->beta->vaults->credentials->create(
  'vlt_011CZkZDLs7fYzm1hXNPeRjv',
  auth: [
    'token' => 'bearer_exampletoken',
    'mcpServerURL' => 'https://example-server.modelcontextprotocol.io/sse',
    'type' => 'static_bearer',
  ],
  displayName: 'Example credential',
  metadata: ['environment' => 'production'],
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
);

var_dump($betaManagedAgentsCredential);
```

##### Response (200)

```json
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
```

### List Credentials

`$client->beta->vaults->credentials->list(string vaultID, ?bool includeArchived, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<ManagedAgentsCredential>`

**GET** `/v1/vaults/{vault_id}/credentials`

List Credentials

#### Parameters

- `vaultID: string`

- `includeArchived?:optional bool`

  Whether to include archived credentials in the results.

- `limit?:optional int`

  Maximum number of credentials to return per page. Defaults to 20, maximum 100.

- `page?:optional string`

  Opaque pagination token from a previous `list_credentials` response.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

#### Returns

- `ManagedAgentsCredential`

  - `string id`

    Unique identifier for the credential.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `Auth auth`

    Authentication details for a credential.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `array<string,string> metadata`

    Arbitrary key-value metadata attached to the credential.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `string vaultID`

    Identifier of the vault this credential belongs to.

  - `?string displayName`

    Human-readable name for the credential.

#### Example

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
);

var_dump($page);
```

##### Response (200)

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

### Get Credential

`$client->beta->vaults->credentials->retrieve(string credentialID, string vaultID, ?list<AnthropicBeta> betas): ManagedAgentsCredential`

**GET** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Get Credential

#### Parameters

- `vaultID: string`

- `credentialID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

#### Returns

- `ManagedAgentsCredential`

  - `string id`

    Unique identifier for the credential.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `Auth auth`

    Authentication details for a credential.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `array<string,string> metadata`

    Arbitrary key-value metadata attached to the credential.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `string vaultID`

    Identifier of the vault this credential belongs to.

  - `?string displayName`

    Human-readable name for the credential.

#### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsCredential = $client->beta->vaults->credentials->retrieve(
  'vcrd_011CZkZEMt8gZan2iYOQfSkw',
  vaultID: 'vlt_011CZkZDLs7fYzm1hXNPeRjv',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
);

var_dump($betaManagedAgentsCredential);
```

##### Response (200)

```json
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
```

### Update Credential

`$client->beta->vaults->credentials->update(string credentialID, string vaultID, ?Auth auth, ?string displayName, ?array<string,string> metadata, ?list<AnthropicBeta> betas): ManagedAgentsCredential`

**POST** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Update Credential

#### Parameters

- `vaultID: string`

- `credentialID: string`

- `auth?:optional Auth`

  Updated authentication details for a credential.

- `displayName?:optional string`

  Updated human-readable name for the credential. 1-255 characters.

- `metadata?:optional array<string,string>`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

#### Returns

- `ManagedAgentsCredential`

  - `string id`

    Unique identifier for the credential.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `Auth auth`

    Authentication details for a credential.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `array<string,string> metadata`

    Arbitrary key-value metadata attached to the credential.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `string vaultID`

    Identifier of the vault this credential belongs to.

  - `?string displayName`

    Human-readable name for the credential.

#### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsCredential = $client->beta->vaults->credentials->update(
  'vcrd_011CZkZEMt8gZan2iYOQfSkw',
  vaultID: 'vlt_011CZkZDLs7fYzm1hXNPeRjv',
  auth: [
    'type' => 'mcp_oauth',
    'accessToken' => 'x',
    'expiresAt' => new \DateTimeImmutable('2019-12-27T18:11:19.117Z'),
    'refresh' => [
      'refreshToken' => 'x',
      'scope' => 'scope',
      'tokenEndpointAuth' => [
        'type' => 'client_secret_basic', 'clientSecret' => 'x'
      ],
    ],
  ],
  displayName: 'Example credential',
  metadata: ['environment' => 'production'],
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
);

var_dump($betaManagedAgentsCredential);
```

##### Response (200)

```json
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
```

### Delete Credential

`$client->beta->vaults->credentials->delete(string credentialID, string vaultID, ?list<AnthropicBeta> betas): ManagedAgentsDeletedCredential`

**DELETE** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Delete Credential

#### Parameters

- `vaultID: string`

- `credentialID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

#### Returns

- `ManagedAgentsDeletedCredential`

  - `string id`

    Unique identifier of the deleted credential.

  - `Type type`

#### Example

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
);

var_dump($betaManagedAgentsDeletedCredential);
```

##### Response (200)

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "type": "vault_credential_deleted"
}
```

### Archive Credential

`$client->beta->vaults->credentials->archive(string credentialID, string vaultID, ?list<AnthropicBeta> betas): ManagedAgentsCredential`

**POST** `/v1/vaults/{vault_id}/credentials/{credential_id}/archive`

Archive Credential

#### Parameters

- `vaultID: string`

- `credentialID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

#### Returns

- `ManagedAgentsCredential`

  - `string id`

    Unique identifier for the credential.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `Auth auth`

    Authentication details for a credential.

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `array<string,string> metadata`

    Arbitrary key-value metadata attached to the credential.

  - `Type type`

  - `\Datetime updatedAt`

    A timestamp in RFC 3339 format

  - `string vaultID`

    Identifier of the vault this credential belongs to.

  - `?string displayName`

    Human-readable name for the credential.

#### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsCredential = $client->beta->vaults->credentials->archive(
  'vcrd_011CZkZEMt8gZan2iYOQfSkw',
  vaultID: 'vlt_011CZkZDLs7fYzm1hXNPeRjv',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
);

var_dump($betaManagedAgentsCredential);
```

##### Response (200)

```json
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
```

### Validate Credential

`$client->beta->vaults->credentials->mcpOAuthValidate(string credentialID, string vaultID, ?list<AnthropicBeta> betas): ManagedAgentsCredentialValidation`

**POST** `/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate`

Validate Credential

#### Parameters

- `vaultID: string`

- `credentialID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

#### Returns

- `ManagedAgentsCredentialValidation`

  - `string credentialID`

    Unique identifier of the credential that was validated.

  - `bool hasRefreshToken`

    Whether the credential has a refresh token configured.

  - `?ManagedAgentsMCPProbe mcpProbe`

    The failing step of an MCP validation probe.

  - `?ManagedAgentsRefreshObject refresh`

    Outcome of a refresh-token exchange attempted during credential validation.

  - `ManagedAgentsCredentialValidationStatus status`

    Overall verdict of a credential validation probe.

  - `Type type`

  - `\Datetime validatedAt`

    A timestamp in RFC 3339 format

  - `string vaultID`

    Identifier of the vault containing the credential.

#### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsCredentialValidation = $client
  ->beta
  ->vaults
  ->credentials
  ->mcpOAuthValidate(
  'vcrd_011CZkZEMt8gZan2iYOQfSkw',
  vaultID: 'vlt_011CZkZDLs7fYzm1hXNPeRjv',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
);

var_dump($betaManagedAgentsCredentialValidation);
```

##### Response (200)

```json
{
  "credential_id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
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
