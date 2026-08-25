# Tunnels

## Create Tunnel

`$client->beta->tunnels->create(?string displayName, ?list<AnthropicBeta> betas): BetaTunnel`

**POST** `/v1/tunnels`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Creates a tunnel. Creation allocates a fresh hostname and provisions the tunnel; it is not idempotent. The new tunnel rejects MCP traffic until at least one CA certificate is added.

### Parameters

- `displayName?:optional string`

  Optional human-readable name for the tunnel (1-255 characters).

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaTunnel`

  - `string id`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `?string displayName`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `string domain`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `"tunnel" type`

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaTunnel = $client->beta->tunnels->create(
  displayName: 'x', betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24]
);

var_dump($betaTunnel);
```

#### Response (200)

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "display_name": "display_name",
  "domain": "domain",
  "type": "tunnel"
}
```

## Get Tunnel

`$client->beta->tunnels->retrieve(string tunnelID, ?list<AnthropicBeta> betas): BetaTunnel`

**GET** `/v1/tunnels/{tunnel_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel by ID.

### Parameters

- `tunnelID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaTunnel`

  - `string id`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `?string displayName`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `string domain`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `"tunnel" type`

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaTunnel = $client->beta->tunnels->retrieve(
  'tunnel_id', betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24]
);

var_dump($betaTunnel);
```

#### Response (200)

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "display_name": "display_name",
  "domain": "domain",
  "type": "tunnel"
}
```

## List Tunnels

`$client->beta->tunnels->list(?bool includeArchived, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<BetaTunnel>`

**GET** `/v1/tunnels`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists tunnels. Results are ordered by creation time, newest first; archived tunnels are excluded unless include_archived is set.

### Parameters

- `includeArchived?:optional bool`

  Whether to include archived tunnels in the results. Defaults to false.

- `limit?:optional int`

  Maximum number of tunnels to return per page. Defaults to 20, maximum 1000.

- `page?:optional string`

  Opaque pagination cursor from a previous `list_tunnels` response.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaTunnel`

  - `string id`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `?string displayName`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `string domain`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `"tunnel" type`

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->tunnels->list(
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
      "id": "id",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "created_at": "2019-12-27T18:11:19.117Z",
      "display_name": "display_name",
      "domain": "domain",
      "type": "tunnel"
    }
  ],
  "next_page": "next_page"
}
```

## Archive Tunnel

`$client->beta->tunnels->archive(string tunnelID, ?list<AnthropicBeta> betas): BetaTunnel`

**POST** `/v1/tunnels/{tunnel_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel. Archival is irreversible: every non-archived certificate on the tunnel is archived in the same operation, the hostname is retired and never re-allocated, and the tunnel token is invalidated. Retrying against an already-archived tunnel returns the existing record unchanged.

### Parameters

- `tunnelID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaTunnel`

  - `string id`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `?string displayName`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `string domain`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `"tunnel" type`

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaTunnel = $client->beta->tunnels->archive(
  'tunnel_id', betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24]
);

var_dump($betaTunnel);
```

#### Response (200)

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "display_name": "display_name",
  "domain": "domain",
  "type": "tunnel"
}
```

## Reveal Tunnel Token

`$client->beta->tunnels->revealToken(string tunnelID, ?list<AnthropicBeta> betas): BetaTunnelToken`

**POST** `/v1/tunnels/{tunnel_id}/reveal_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Reveals a tunnel's connector token. The value is fetched live on each call; Anthropic does not store it. Repeated calls return the same value until the token is rotated. Exposed as POST so the token does not appear in intermediary access logs.

### Parameters

- `tunnelID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaTunnelToken`

  - `string id`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `string tunnelToken`

    The connector token used to run the tunnel. Treat as a credential.

  - `"tunnel_token" type`

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaTunnelToken = $client->beta->tunnels->revealToken(
  'tunnel_id', betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24]
);

var_dump($betaTunnelToken);
```

#### Response (200)

```json
{
  "id": "id",
  "tunnel_token": "tunnel_token",
  "type": "tunnel_token"
}
```

## Rotate Tunnel Token

`$client->beta->tunnels->rotateToken(string tunnelID, ?string reason, ?list<AnthropicBeta> betas): BetaTunnelToken`

**POST** `/v1/tunnels/{tunnel_id}/rotate_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Rotates a tunnel's connector token. Rotation invalidates the current token for new connections and returns a fresh value; established connections are not severed. A connector restarted after rotation must use the new value.

### Parameters

- `tunnelID: string`

- `reason?:optional string`

  Optional free-text reason for the rotation, recorded for audit.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaTunnelToken`

  - `string id`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `string tunnelToken`

    The connector token used to run the tunnel. Treat as a credential.

  - `"tunnel_token" type`

### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaTunnelToken = $client->beta->tunnels->rotateToken(
  'tunnel_id',
  reason: 'reason',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
);

var_dump($betaTunnelToken);
```

#### Response (200)

```json
{
  "id": "id",
  "tunnel_token": "tunnel_token",
  "type": "tunnel_token"
}
```

## Domain types

### Beta Tunnel

- `BetaTunnel`

  - `string id`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `?string displayName`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `string domain`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `"tunnel" type`

### Beta Tunnel Token

- `BetaTunnelToken`

  - `string id`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `string tunnelToken`

    The connector token used to run the tunnel. Treat as a credential.

  - `"tunnel_token" type`

## Tunnels › Certificates

### Create Tunnel Certificate

`$client->beta->tunnels->certificates->create(string tunnelID, string caCertificatePem, ?list<AnthropicBeta> betas): TunnelCertificate`

**POST** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Registers a public CA certificate on a tunnel. Anthropic verifies the gateway's server certificate against this CA when it terminates the inner TLS session. A tunnel holds at most two non-archived certificates.

#### Parameters

- `tunnelID: string`

- `caCertificatePem: string`

  PEM-encoded X.509 CA certificate. Must contain exactly one certificate and no private-key material. Maximum 8KB.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

#### Returns

- `TunnelCertificate`

  - `string id`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `?\Datetime expiresAt`

    A timestamp in RFC 3339 format

  - `string fingerprint`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `string tunnelID`

    ID of the tunnel the certificate is registered against.

  - `"tunnel_certificate" type`

#### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaTunnelCertificate = $client->beta->tunnels->certificates->create(
  'tunnel_id',
  caCertificatePem: 'ca_certificate_pem',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
);

var_dump($betaTunnelCertificate);
```

##### Response (200)

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "expires_at": "2019-12-27T18:11:19.117Z",
  "fingerprint": "fingerprint",
  "tunnel_id": "tunnel_id",
  "type": "tunnel_certificate"
}
```

### Get Tunnel Certificate

`$client->beta->tunnels->certificates->retrieve(string certificateID, string tunnelID, ?list<AnthropicBeta> betas): TunnelCertificate`

**GET** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel certificate by ID.

#### Parameters

- `tunnelID: string`

- `certificateID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

#### Returns

- `TunnelCertificate`

  - `string id`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `?\Datetime expiresAt`

    A timestamp in RFC 3339 format

  - `string fingerprint`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `string tunnelID`

    ID of the tunnel the certificate is registered against.

  - `"tunnel_certificate" type`

#### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaTunnelCertificate = $client->beta->tunnels->certificates->retrieve(
  'certificate_id',
  tunnelID: 'tunnel_id',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
);

var_dump($betaTunnelCertificate);
```

##### Response (200)

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "expires_at": "2019-12-27T18:11:19.117Z",
  "fingerprint": "fingerprint",
  "tunnel_id": "tunnel_id",
  "type": "tunnel_certificate"
}
```

### List Tunnel Certificates

`$client->beta->tunnels->certificates->list(string tunnelID, ?bool includeArchived, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<TunnelCertificate>`

**GET** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists the certificates registered on a tunnel. Archived certificates are excluded unless include_archived is set.

#### Parameters

- `tunnelID: string`

- `includeArchived?:optional bool`

  Whether to include archived certificates in the results. Defaults to false.

- `limit?:optional int`

  Maximum number of certificates to return per page. Defaults to 20, maximum 1000.

- `page?:optional string`

  Opaque pagination cursor from a previous `list_tunnel_certificates` response.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

#### Returns

- `TunnelCertificate`

  - `string id`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `?\Datetime expiresAt`

    A timestamp in RFC 3339 format

  - `string fingerprint`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `string tunnelID`

    ID of the tunnel the certificate is registered against.

  - `"tunnel_certificate" type`

#### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->tunnels->certificates->list(
  'tunnel_id',
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
      "id": "id",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "created_at": "2019-12-27T18:11:19.117Z",
      "expires_at": "2019-12-27T18:11:19.117Z",
      "fingerprint": "fingerprint",
      "tunnel_id": "tunnel_id",
      "type": "tunnel_certificate"
    }
  ],
  "next_page": "next_page"
}
```

### Archive Tunnel Certificate

`$client->beta->tunnels->certificates->archive(string certificateID, string tunnelID, ?list<AnthropicBeta> betas): TunnelCertificate`

**POST** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel certificate, removing it from the set Anthropic trusts for the tunnel. The certificate record is retained. Archiving the last non-archived certificate is permitted; the tunnel rejects MCP traffic until a new certificate is added.

#### Parameters

- `tunnelID: string`

- `certificateID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

#### Returns

- `TunnelCertificate`

  - `string id`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `?\Datetime archivedAt`

    A timestamp in RFC 3339 format

  - `\Datetime createdAt`

    A timestamp in RFC 3339 format

  - `?\Datetime expiresAt`

    A timestamp in RFC 3339 format

  - `string fingerprint`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `string tunnelID`

    ID of the tunnel the certificate is registered against.

  - `"tunnel_certificate" type`

#### Example

```php
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaTunnelCertificate = $client->beta->tunnels->certificates->archive(
  'certificate_id',
  tunnelID: 'tunnel_id',
  betas: [AnthropicBeta::MESSAGE_BATCHES_2024_09_24],
);

var_dump($betaTunnelCertificate);
```

##### Response (200)

```json
{
  "id": "id",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "created_at": "2019-12-27T18:11:19.117Z",
  "expires_at": "2019-12-27T18:11:19.117Z",
  "fingerprint": "fingerprint",
  "tunnel_id": "tunnel_id",
  "type": "tunnel_certificate"
}
```
