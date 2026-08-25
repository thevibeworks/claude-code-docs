# Certificates

## Create Tunnel Certificate

`$client->beta->tunnels->certificates->create(string tunnelID, string caCertificatePem, ?list<AnthropicBeta> betas): TunnelCertificate`

**POST** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Registers a public CA certificate on a tunnel. Anthropic verifies the gateway's server certificate against this CA when it terminates the inner TLS session. A tunnel holds at most two non-archived certificates.

### Parameters

- `tunnelID: string`

- `caCertificatePem: string`

  PEM-encoded X.509 CA certificate. Must contain exactly one certificate and no private-key material. Maximum 8KB.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

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

### Example

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

#### Response (200)

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

## Get Tunnel Certificate

`$client->beta->tunnels->certificates->retrieve(string certificateID, string tunnelID, ?list<AnthropicBeta> betas): TunnelCertificate`

**GET** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel certificate by ID.

### Parameters

- `tunnelID: string`

- `certificateID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

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

### Example

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

#### Response (200)

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

## List Tunnel Certificates

`$client->beta->tunnels->certificates->list(string tunnelID, ?bool includeArchived, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<TunnelCertificate>`

**GET** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists the certificates registered on a tunnel. Archived certificates are excluded unless include_archived is set.

### Parameters

- `tunnelID: string`

- `includeArchived?:optional bool`

  Whether to include archived certificates in the results. Defaults to false.

- `limit?:optional int`

  Maximum number of certificates to return per page. Defaults to 20, maximum 1000.

- `page?:optional string`

  Opaque pagination cursor from a previous `list_tunnel_certificates` response.

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

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

### Example

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

#### Response (200)

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

## Archive Tunnel Certificate

`$client->beta->tunnels->certificates->archive(string certificateID, string tunnelID, ?list<AnthropicBeta> betas): TunnelCertificate`

**POST** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel certificate, removing it from the set Anthropic trusts for the tunnel. The certificate record is retained. Archiving the last non-archived certificate is permitted; the tunnel rejects MCP traffic until a new certificate is added.

### Parameters

- `tunnelID: string`

- `certificateID: string`

- `betas?:optional list<AnthropicBeta>`

  Optional header to specify the beta version(s) you want to use.

### Returns

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

### Example

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

#### Response (200)

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

## Domain types

### Beta Tunnel Certificate

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
