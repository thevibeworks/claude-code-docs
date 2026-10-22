---
title: Credentials
url: https://platform.claude.com/docs/en/api/php/beta/vaults/credentials
---

# Credentials

## Create a Credential

`$client->beta->vaults->credentials->create(string vaultID, Auth auth, ?string displayName, ?array<string,string> metadata, ?list<AnthropicBeta> betas, ?string workspaceID): ManagedAgentsCredential`

**POST** `/v1/vaults/{vault_id}/credentials`

Create a Credential

### Parameters

- `vaultID: string` (path parameter)

  Identifier of the vault to create the credential in.

- `auth: Auth`

  Authentication configuration for the credential.

- `displayName?:optional string`

  Human-readable name for the credential. Up to 255 characters.

- `metadata?:optional array<string,string>`

  Arbitrary key-value metadata to attach to the credential. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `betas?:optional list<AnthropicBeta>` (header parameter)

  This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

- `workspaceID?:optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class ManagedAgentsCredential`

  - `"vault_credential" type`

  - `string id`

    The unique ID of the credential (`vcrd_...`).

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

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

use Anthropic\Client;
use Anthropic\Beta\AnthropicBeta;

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
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsCredential);
```

#### Response (200)

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

## List Credentials

`$client->beta->vaults->credentials->list(string vaultID, ?bool includeArchived, ?int limit, ?string page, ?list<AnthropicBeta> betas, ?string workspaceID): PageCursor<ManagedAgentsCredential>`

**GET** `/v1/vaults/{vault_id}/credentials`

List Credentials

### Parameters

- `vaultID: string` (path parameter)

  Identifier of the vault to list credentials for.

- `includeArchived?:optional bool` (query parameter)

  Whether to include archived credentials in the results. Defaults to `false`.

- `limit?:optional int` (query parameter)

  Maximum number of credentials to return per page. Defaults to 20, maximum 100.

- `page?:optional string` (query parameter)

  The `next_page` value from a previous [List Credentials](https://platform.claude.com/docs/en/api/beta/vaults/credentials/list?sdk_languages=php) response, to get the next page. Leave it out to get the first page.

- `betas?:optional list<AnthropicBeta>` (header parameter)

  This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

- `workspaceID?:optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class ManagedAgentsCredential`

  - `"vault_credential" type`

  - `string id`

    The unique ID of the credential (`vcrd_...`).

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

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

use Anthropic\Client;
use Anthropic\Beta\AnthropicBeta;

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

#### Response (200)

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

## Retrieve a Credential

`$client->beta->vaults->credentials->retrieve(string credentialID, string vaultID, ?list<AnthropicBeta> betas, ?string workspaceID): ManagedAgentsCredential`

**GET** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Retrieve a Credential

### Parameters

- `vaultID: string` (path parameter)

  Identifier of the vault containing the credential.

- `credentialID: string` (path parameter)

  Unique identifier of the credential to retrieve.

- `betas?:optional list<AnthropicBeta>` (header parameter)

  This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

- `workspaceID?:optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class ManagedAgentsCredential`

  - `"vault_credential" type`

  - `string id`

    The unique ID of the credential (`vcrd_...`).

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

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

use Anthropic\Client;
use Anthropic\Beta\AnthropicBeta;

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsCredential = $client->beta->vaults->credentials->retrieve(
  'vcrd_011CZkZEMt8gZan2iYPQfSkw',
  vaultID: 'vlt_011CZkZDLs7fYzm1hXNPeRjv',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsCredential);
```

#### Response (200)

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

## Update a Credential

`$client->beta->vaults->credentials->update(string credentialID, string vaultID, ?Auth auth, ?string displayName, ?array<string,string> metadata, ?list<AnthropicBeta> betas, ?string workspaceID): ManagedAgentsCredential`

**POST** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Update a Credential

### Parameters

- `vaultID: string` (path parameter)

  Identifier of the vault containing the credential.

- `credentialID: string` (path parameter)

  Unique identifier of the credential to update.

- `auth?:optional Auth`

  New authentication settings for the credential. The `type` must match the credential's current type, which can't be changed.

- `displayName?:optional string`

  Updated human-readable name for the credential. 1-255 characters.

- `metadata?:optional array<string,string>`

  Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

- `betas?:optional list<AnthropicBeta>` (header parameter)

  This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

- `workspaceID?:optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class ManagedAgentsCredential`

  - `"vault_credential" type`

  - `string id`

    The unique ID of the credential (`vcrd_...`).

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

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

use Anthropic\Client;
use Anthropic\Beta\AnthropicBeta;

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsCredential = $client->beta->vaults->credentials->update(
  'vcrd_011CZkZEMt8gZan2iYPQfSkw',
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
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsCredential);
```

#### Response (200)

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

## Delete a Credential

`$client->beta->vaults->credentials->delete(string credentialID, string vaultID, ?list<AnthropicBeta> betas, ?string workspaceID): ManagedAgentsDeletedCredential`

**DELETE** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Delete a Credential

### Parameters

- `vaultID: string` (path parameter)

  Identifier of the vault containing the credential.

- `credentialID: string` (path parameter)

  Unique identifier of the credential to delete.

- `betas?:optional list<AnthropicBeta>` (header parameter)

  This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

- `workspaceID?:optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class ManagedAgentsDeletedCredential`

  - `"vault_credential_deleted" type`

  - `string id`

    The unique ID of the deleted credential (`vcrd_...`).

### Example

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

#### Response (200)

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYPQfSkw",
  "type": "vault_credential_deleted"
}
```

## Archive a Credential

`$client->beta->vaults->credentials->archive(string credentialID, string vaultID, ?list<AnthropicBeta> betas, ?string workspaceID): ManagedAgentsCredential`

**POST** `/v1/vaults/{vault_id}/credentials/{credential_id}/archive`

Archive a Credential

### Parameters

- `vaultID: string` (path parameter)

  Identifier of the vault containing the credential.

- `credentialID: string` (path parameter)

  Unique identifier of the credential to archive.

- `betas?:optional list<AnthropicBeta>` (header parameter)

  This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

- `workspaceID?:optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class ManagedAgentsCredential`

  - `"vault_credential" type`

  - `string id`

    The unique ID of the credential (`vcrd_...`).

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

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

use Anthropic\Client;
use Anthropic\Beta\AnthropicBeta;

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsCredential = $client->beta->vaults->credentials->archive(
  'vcrd_011CZkZEMt8gZan2iYPQfSkw',
  vaultID: 'vlt_011CZkZDLs7fYzm1hXNPeRjv',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsCredential);
```

#### Response (200)

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

## Validate an MCP OAuth Credential

`$client->beta->vaults->credentials->mcpOAuthValidate(string credentialID, string vaultID, ?list<AnthropicBeta> betas, ?string workspaceID): ManagedAgentsCredentialValidation`

**POST** `/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate`

Validate an MCP OAuth Credential

### Parameters

- `vaultID: string` (path parameter)

  Identifier of the vault containing the credential.

- `credentialID: string` (path parameter)

  Unique identifier of the credential to validate.

- `betas?:optional list<AnthropicBeta>` (header parameter)

  This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

- `workspaceID?:optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class ManagedAgentsCredentialValidation`

  - `"vault_credential_validation" type`

  - `string credentialID`

    Unique identifier of the credential that was validated.

  - `bool hasRefreshToken`

    Whether the credential has a refresh token configured.

  - `?ManagedAgentsMCPProbe mcpProbe`

    Details of the MCP probe step that failed, or `null` if the probe succeeded or there was no access token to test.

  - `?ManagedAgentsRefreshObject refresh`

    Details of the refresh-token exchange attempted on a 401. Null when no refresh was attempted.

  - `ManagedAgentsCredentialValidationStatus status`

    Overall verdict of the validation probe.

  - `\Datetime validatedAt`

    When the validation probe was performed.

  - `string vaultID`

    Identifier of the vault containing the credential.

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

use Anthropic\Client;
use Anthropic\Beta\AnthropicBeta;

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaManagedAgentsCredentialValidation = $client
  ->beta
  ->vaults
  ->credentials
  ->mcpOAuthValidate(
  'vcrd_011CZkZEMt8gZan2iYPQfSkw',
  vaultID: 'vlt_011CZkZDLs7fYzm1hXNPeRjv',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
  workspaceID: 'wrkspc_011CZkZaBF1tNoB5wlCeusgy',
);

var_dump($betaManagedAgentsCredentialValidation);
```

#### Response (200)

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

## Domain types

### Beta Managed Agents Credential

- `class ManagedAgentsCredential`

  - `"vault_credential" type`

  - `string id`

    The unique ID of the credential (`vcrd_...`).

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

### Beta Managed Agents Credential Networking Params

- `class ManagedAgentsCredentialNetworkingParams`

  - `class ManagedAgentsUnrestrictedCredentialNetworkingParams`

    - `"unrestricted" type`

  - `class ManagedAgentsLimitedCredentialNetworkingParams`

    - `"limited" type`

    - `list<string> allowedHosts`

      The destination hosts of the outbound requests that the credential's secret is substituted into.

      Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.` wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses aren't accepted. The list can have up to 16 entries.

### Beta Managed Agents Credential Validation

- `class ManagedAgentsCredentialValidation`

  - `"vault_credential_validation" type`

  - `string credentialID`

    Unique identifier of the credential that was validated.

  - `bool hasRefreshToken`

    Whether the credential has a refresh token configured.

  - `?ManagedAgentsMCPProbe mcpProbe`

    Details of the MCP probe step that failed, or `null` if the probe succeeded or there was no access token to test.

  - `?ManagedAgentsRefreshObject refresh`

    Details of the refresh-token exchange attempted on a 401. Null when no refresh was attempted.

  - `ManagedAgentsCredentialValidationStatus status`

    Overall verdict of the validation probe.

  - `\Datetime validatedAt`

    When the validation probe was performed.

  - `string vaultID`

    Identifier of the vault containing the credential.

### Beta Managed Agents Credential Validation Status

- `enum ManagedAgentsCredentialValidationStatus`

  - `"valid"`

    The credential successfully authenticated against its MCP server.

  - `"invalid"`

    The probe reached the MCP server and the server rejected the credential, or no access token is stored. A refresh, if one was tried, didn't recover it. Usually the end user needs to authorize again.

  - `"unknown"`

    The probe couldn't tell whether the credential works, for example because of a network error or because a refresh succeeded but the new access token wasn't tested. Validate the credential again to find out.

### Beta Managed Agents Deleted Credential

- `class ManagedAgentsDeletedCredential`

  - `"vault_credential_deleted" type`

  - `string id`

    The unique ID of the deleted credential (`vcrd_...`).

### Beta Managed Agents Environment Variable Auth Response

- `class ManagedAgentsEnvironmentVariableAuthResponse`

  - `"environment_variable" type`

  - `ManagedAgentsInjectionLocationResponse injectionLocation`

    Where in the outbound request the secret value is substituted.

  - `Networking networking`

    Outbound hosts the secret value is substituted on.

  - `string secretName`

    Name of the environment variable.

### Beta Managed Agents Environment Variable Create Params

- `class ManagedAgentsEnvironmentVariableCreateParams`

  - `"environment_variable" type`

  - `ManagedAgentsCredentialNetworkingParams networking`

    Outbound hosts the secret value is substituted on.

  - `string secretName`

    Name of the environment variable. Immutable after create.

  - `string secretValue`

    The secret to substitute into the agent's outbound requests. It's write-only and never returned in responses.

  - `?ManagedAgentsInjectionLocationParams injectionLocation`

    Where in the outbound request the secret value may be substituted.

### Beta Managed Agents Environment Variable Update Params

- `class ManagedAgentsEnvironmentVariableUpdateParams`

  - `"environment_variable" type`

  - `?ManagedAgentsInjectionLocationUpdateParams injectionLocation`

    Updated injection location.

  - `?ManagedAgentsCredentialNetworkingParams networking`

    The new networking scope, which replaces the stored one as a whole.

  - `?string secretValue`

    The new secret value to replace the stored one.

### Beta Managed Agents Injection Location Params

- `class ManagedAgentsInjectionLocationParams`

  - `?bool body`

    Substitute when the placeholder appears in the request body.

  - `?bool header`

    Substitute when the placeholder appears in a request header value.

### Beta Managed Agents Injection Location Response

- `class ManagedAgentsInjectionLocationResponse`

  - `bool body`

    Whether the placeholder is substituted in the request body.

  - `bool header`

    Whether the placeholder is substituted in request header values.

### Beta Managed Agents Injection Location Update Params

- `class ManagedAgentsInjectionLocationUpdateParams`

  - `?bool body`

    Substitute when the placeholder appears in the request body.

  - `?bool header`

    Substitute when the placeholder appears in a request header value.

### Beta Managed Agents Limited Credential Networking Params

- `class ManagedAgentsLimitedCredentialNetworkingParams`

  - `"limited" type`

  - `list<string> allowedHosts`

    The destination hosts of the outbound requests that the credential's secret is substituted into.

    Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.` wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses aren't accepted. The list can have up to 16 entries.

### Beta Managed Agents Limited Credential Networking Response

- `class ManagedAgentsLimitedCredentialNetworkingResponse`

  - `"limited" type`

  - `list<string> allowedHosts`

    The destination hosts of the outbound requests that the credential's secret is substituted into.

    An entry matches the request host exactly. An entry such as `*.example.com` matches any subdomain of `example.com` but not `example.com` itself.

### Beta Managed Agents MCP OAuth Auth Response

- `class ManagedAgentsMCPOAuthAuthResponse`

  - `"mcp_oauth" type`

  - `string mcpServerURL`

    URL of the MCP server this credential authenticates against.

  - `?\Datetime expiresAt`

    When the credential's access token expires, in RFC 3339. Absent if the expiry isn't known.

  - `?ManagedAgentsMCPOAuthRefreshResponse refresh`

    Refresh token configuration, if the credential supports token refresh.

### Beta Managed Agents MCP OAuth Create Params

- `class ManagedAgentsMCPOAuthCreateParams`

  - `"mcp_oauth" type`

  - `string accessToken`

    The OAuth access token to send to the MCP server.

  - `string mcpServerURL`

    URL of the MCP server this credential authenticates against.

  - `?\Datetime expiresAt`

    When `access_token` expires, in RFC 3339.

    Must be in the future.

  - `?ManagedAgentsMCPOAuthRefreshParams refresh`

    Refresh token configuration, if the credential supports token refresh.

### Beta Managed Agents MCP OAuth Refresh Params

- `class ManagedAgentsMCPOAuthRefreshParams`

  - `string clientID`

    The OAuth client ID to use when refreshing the access token. It can't be changed after the credential is created.

  - `string refreshToken`

    The OAuth refresh token that the API uses to get a new access token when the current one expires.

  - `string tokenEndpoint`

    Token endpoint URL used to refresh the access token.

  - `TokenEndpointAuth tokenEndpointAuth`

  - `?string resource`

    OAuth resource indicator.

  - `?string scope`

    OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Response

- `class ManagedAgentsMCPOAuthRefreshResponse`

  - `string clientID`

    The OAuth client ID used when refreshing the access token.

  - `string tokenEndpoint`

    Token endpoint URL used to refresh the access token.

  - `TokenEndpointAuth tokenEndpointAuth`

  - `?string resource`

    OAuth resource indicator.

  - `?string scope`

    OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Update Params

- `class ManagedAgentsMCPOAuthRefreshUpdateParams`

  - `?string refreshToken`

    The new OAuth refresh token to replace the stored one.

  - `?string scope`

    The new OAuth scope for refresh requests. Send an empty string to clear the stored scope.

  - `?TokenEndpointAuth tokenEndpointAuth`

### Beta Managed Agents MCP OAuth Update Params

- `class ManagedAgentsMCPOAuthUpdateParams`

  - `"mcp_oauth" type`

  - `?string accessToken`

    The new OAuth access token to replace the stored one.

  - `?\Datetime expiresAt`

    When the credential's access token expires, in RFC 3339. Leave it out to keep the stored expiry.

    If you send a new `access_token`, send its `expires_at` too, or the new token keeps the old expiry.

    Must be in the future.

  - `?ManagedAgentsMCPOAuthRefreshUpdateParams refresh`

    Updated refresh token configuration.

### Beta Managed Agents MCP Probe

- `class ManagedAgentsMCPProbe`

  - `?ManagedAgentsRefreshHTTPResponse httpResponse`

    The HTTP error response from the MCP server, or `null` if the MCP server didn't return one for the failing step, for example after a timeout or a DNS or TLS failure.

  - `string method`

    The MCP method that failed (for example `initialize` or `tools/list`).

### Beta Managed Agents Refresh HTTP Response

- `class ManagedAgentsRefreshHTTPResponse`

  - `string body`

    Response body. May be truncated and has sensitive values scrubbed.

  - `bool bodyTruncated`

    Whether `body` was truncated.

  - `string contentType`

    Value of the `Content-Type` response header.

  - `int statusCode`

    HTTP status code.

### Beta Managed Agents Refresh Object

- `class ManagedAgentsRefreshObject`

  - `?ManagedAgentsRefreshHTTPResponse httpResponse`

    The captured HTTP error response from the token endpoint. Populated only when `status` is `failed`.

  - `Status status`

    Outcome of the refresh attempt.

### Beta Managed Agents Static Bearer Auth Response

- `class ManagedAgentsStaticBearerAuthResponse`

  - `"static_bearer" type`

  - `string mcpServerURL`

    URL of the MCP server this credential authenticates against.

### Beta Managed Agents Static Bearer Create Params

- `class ManagedAgentsStaticBearerCreateParams`

  - `"static_bearer" type`

  - `string token`

    The static bearer token to send to the MCP server, such as an API key or personal access token.

  - `string mcpServerURL`

    URL of the MCP server this credential authenticates against.

### Beta Managed Agents Static Bearer Update Params

- `class ManagedAgentsStaticBearerUpdateParams`

  - `"static_bearer" type`

  - `?string token`

    The new static bearer token to replace the stored one.

### Beta Managed Agents Token Endpoint Auth Basic Param

- `class ManagedAgentsTokenEndpointAuthBasicParam`

  - `"client_secret_basic" type`

  - `string clientSecret`

    The OAuth client secret, sent to `token_endpoint` with HTTP Basic authentication.

### Beta Managed Agents Token Endpoint Auth Basic Response

- `class ManagedAgentsTokenEndpointAuthBasicResponse`

  - `"client_secret_basic" type`

### Beta Managed Agents Token Endpoint Auth Basic Update Param

- `class ManagedAgentsTokenEndpointAuthBasicUpdateParam`

  - `"client_secret_basic" type`

  - `?string clientSecret`

    A new OAuth client secret to replace the stored one.

    The credential must already use `client_secret_basic` or `client_secret_post`. It keeps its current `token_endpoint_auth` type, even if the `type` sent with this secret is the other one.

### Beta Managed Agents Token Endpoint Auth None Param

- `class ManagedAgentsTokenEndpointAuthNoneParam`

  - `"none" type`

### Beta Managed Agents Token Endpoint Auth None Response

- `class ManagedAgentsTokenEndpointAuthNoneResponse`

  - `"none" type`

### Beta Managed Agents Token Endpoint Auth Post Param

- `class ManagedAgentsTokenEndpointAuthPostParam`

  - `"client_secret_post" type`

  - `string clientSecret`

    The OAuth client secret, sent to `token_endpoint` in the POST body.

### Beta Managed Agents Token Endpoint Auth Post Response

- `class ManagedAgentsTokenEndpointAuthPostResponse`

  - `"client_secret_post" type`

### Beta Managed Agents Token Endpoint Auth Post Update Param

- `class ManagedAgentsTokenEndpointAuthPostUpdateParam`

  - `"client_secret_post" type`

  - `?string clientSecret`

    A new OAuth client secret to replace the stored one.

    The credential must already use `client_secret_basic` or `client_secret_post`. It keeps its current `token_endpoint_auth` type, even if the `type` sent with this secret is the other one.

### Beta Managed Agents Unrestricted Credential Networking Params

- `class ManagedAgentsUnrestrictedCredentialNetworkingParams`

  - `"unrestricted" type`

### Beta Managed Agents Unrestricted Credential Networking Response

- `class ManagedAgentsUnrestrictedCredentialNetworkingResponse`

  - `"unrestricted" type`
