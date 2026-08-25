# Tunnel Certificates

## Create Tunnel Certificate

**POST** `/v1/organizations/tunnels/{tunnel_id}/certificates`

**Deprecated**

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](/docs/en/api/beta/tunnels) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

Register a public CA certificate for the tunnel.

Anthropic verifies the gateway's server certificate against this CA
when it terminates the inner TLS session. The PEM body must contain
exactly one X.509 certificate and no private-key material. A tunnel
holds at most two non-archived certificates.

### Path parameters

- `tunnel_id: string`

  ID of the Tunnel.

### Headers

- `"anthropic-beta": array of "mcp-tunnels-2026-05-19"`

  Required for all Tunnel endpoints.

### Body parameters

- `ca_certificate_pem: string`

  PEM-encoded X.509 CA certificate. Must contain exactly one certificate and
  no private-key material.

  maxLength: 8192

### Returns

- `id: string`

  ID of the Tunnel Certificate.

- `archived_at: string or null`

  RFC 3339 datetime string indicating when the certificate was archived, or
  `null` if it is not archived.

  format: date-time

- `created_at: string`

  RFC 3339 datetime string indicating when the certificate was registered.

  format: date-time

- `expires_at: string or null`

  RFC 3339 datetime string indicating when the certificate expires, or
  `null` if it does not expire.

  format: date-time

- `fingerprint: string`

  The certificate's SHA-256 fingerprint, as a lowercase hex string.

- `tunnel_id: string`

  ID of the Tunnel this certificate is registered against.

- `type: "tunnel_certificate"`

  Object type. Always `tunnel_certificate` for Tunnel Certificates.

  default: tunnel_certificate

### Example

```bash
curl https://api.anthropic.com/v1/organizations/tunnels/$TUNNEL_ID/certificates \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{
          "ca_certificate_pem": "-----BEGIN CERTIFICATE-----\nMIIBexampleEXAMPLEexampleEXAMPLEexampleEXAMPLEexampleEXAMPLEexa\n...illustrative placeholder, not a real certificate...\n-----END CERTIFICATE-----\n"
        }'
```

#### Response (200)

```json
{
  "id": "tcrt_01JmWq4ZxnBvR7tKpY2sLdH9",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "expires_at": "2024-10-30T23:58:27.427722Z",
  "fingerprint": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
  "tunnel_id": "tnl_01Hx9Kp2RtQvMn3sWbYdLcF8",
  "type": "tunnel_certificate"
}
```

## Get Tunnel Certificate

**GET** `/v1/organizations/tunnels/{tunnel_id}/certificates/{certificate_id}`

**Deprecated**

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](/docs/en/api/beta/tunnels) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

Retrieve a single certificate registered on a tunnel by ID.

### Path parameters

- `tunnel_id: string`

  ID of the Tunnel.

- `certificate_id: string`

  ID of the Tunnel Certificate.

### Headers

- `"anthropic-beta": array of "mcp-tunnels-2026-05-19"`

  Required for all Tunnel endpoints.

### Returns

- `id: string`

  ID of the Tunnel Certificate.

- `archived_at: string or null`

  RFC 3339 datetime string indicating when the certificate was archived, or
  `null` if it is not archived.

  format: date-time

- `created_at: string`

  RFC 3339 datetime string indicating when the certificate was registered.

  format: date-time

- `expires_at: string or null`

  RFC 3339 datetime string indicating when the certificate expires, or
  `null` if it does not expire.

  format: date-time

- `fingerprint: string`

  The certificate's SHA-256 fingerprint, as a lowercase hex string.

- `tunnel_id: string`

  ID of the Tunnel this certificate is registered against.

- `type: "tunnel_certificate"`

  Object type. Always `tunnel_certificate` for Tunnel Certificates.

  default: tunnel_certificate

### Example

```bash
curl https://api.anthropic.com/v1/organizations/tunnels/$TUNNEL_ID/certificates/$CERTIFICATE_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response (200)

```json
{
  "id": "tcrt_01JmWq4ZxnBvR7tKpY2sLdH9",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "expires_at": "2024-10-30T23:58:27.427722Z",
  "fingerprint": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
  "tunnel_id": "tnl_01Hx9Kp2RtQvMn3sWbYdLcF8",
  "type": "tunnel_certificate"
}
```

## List Tunnel Certificates

**GET** `/v1/organizations/tunnels/{tunnel_id}/certificates`

**Deprecated**

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](/docs/en/api/beta/tunnels) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

List the certificates registered on a tunnel.

Archived certificates are excluded unless `include_archived` is set.

### Path parameters

- `tunnel_id: string`

  ID of the Tunnel.

### Query parameters

- `include_archived: optional boolean`

  Include archived certificates in the results. Archived certificates are
  excluded by default.

  default: false

- `limit: optional number`

  Maximum number of certificates to return.

  default: 20, maximum: 1000, minimum: 1

- `page: optional string`

  A tunnel has at most two active certificates, so this list is not
  paginated.

### Headers

- `"anthropic-beta": array of "mcp-tunnels-2026-05-19"`

  Required for all Tunnel endpoints.

### Returns

- `data: array of object`

  - `id: string`

    ID of the Tunnel Certificate.

  - `archived_at: string or null`

    RFC 3339 datetime string indicating when the certificate was archived, or
    `null` if it is not archived.

    format: date-time

  - `created_at: string`

    RFC 3339 datetime string indicating when the certificate was registered.

    format: date-time

  - `expires_at: string or null`

    RFC 3339 datetime string indicating when the certificate expires, or
    `null` if it does not expire.

    format: date-time

  - `fingerprint: string`

    The certificate's SHA-256 fingerprint, as a lowercase hex string.

  - `tunnel_id: string`

    ID of the Tunnel this certificate is registered against.

  - `type: "tunnel_certificate"`

    Object type. Always `tunnel_certificate` for Tunnel Certificates.

    default: tunnel_certificate

- `next_page: string or null`

  Opaque cursor for the next page, or `null` if there are no more results.

### Example

```bash
curl https://api.anthropic.com/v1/organizations/tunnels/$TUNNEL_ID/certificates \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response (200)

```json
{
  "data": [
    {
      "id": "tcrt_01JmWq4ZxnBvR7tKpY2sLdH9",
      "archived_at": "2024-11-01T23:59:27.427722Z",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "expires_at": "2024-10-30T23:58:27.427722Z",
      "fingerprint": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
      "tunnel_id": "tnl_01Hx9Kp2RtQvMn3sWbYdLcF8",
      "type": "tunnel_certificate"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Archive Tunnel Certificate

**POST** `/v1/organizations/tunnels/{tunnel_id}/certificates/{certificate_id}/archive`

**Deprecated**

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](/docs/en/api/beta/tunnels) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

Archive a certificate, removing it from the set Anthropic trusts for this tunnel.

The certificate record is retained. Archiving the last non-archived
certificate is permitted; the tunnel rejects MCP traffic until a new
certificate is added.

### Path parameters

- `tunnel_id: string`

  ID of the Tunnel.

- `certificate_id: string`

  ID of the Tunnel Certificate.

### Headers

- `"anthropic-beta": array of "mcp-tunnels-2026-05-19"`

  Required for all Tunnel endpoints.

### Returns

- `id: string`

  ID of the Tunnel Certificate.

- `archived_at: string or null`

  RFC 3339 datetime string indicating when the certificate was archived, or
  `null` if it is not archived.

  format: date-time

- `created_at: string`

  RFC 3339 datetime string indicating when the certificate was registered.

  format: date-time

- `expires_at: string or null`

  RFC 3339 datetime string indicating when the certificate expires, or
  `null` if it does not expire.

  format: date-time

- `fingerprint: string`

  The certificate's SHA-256 fingerprint, as a lowercase hex string.

- `tunnel_id: string`

  ID of the Tunnel this certificate is registered against.

- `type: "tunnel_certificate"`

  Object type. Always `tunnel_certificate` for Tunnel Certificates.

  default: tunnel_certificate

### Example

```bash
curl https://api.anthropic.com/v1/organizations/tunnels/$TUNNEL_ID/certificates/$CERTIFICATE_ID/archive \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

#### Response (200)

```json
{
  "id": "tcrt_01JmWq4ZxnBvR7tKpY2sLdH9",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "expires_at": "2024-10-30T23:58:27.427722Z",
  "fingerprint": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
  "tunnel_id": "tnl_01Hx9Kp2RtQvMn3sWbYdLcF8",
  "type": "tunnel_certificate"
}
```

## Domain types

### Tunnel Certificate Create Response

- `TunnelCertificateCreateResponse object`

  - `id: string`

    ID of the Tunnel Certificate.

  - `archived_at: string or null`

    RFC 3339 datetime string indicating when the certificate was archived, or
    `null` if it is not archived.

    format: date-time

  - `created_at: string`

    RFC 3339 datetime string indicating when the certificate was registered.

    format: date-time

  - `expires_at: string or null`

    RFC 3339 datetime string indicating when the certificate expires, or
    `null` if it does not expire.

    format: date-time

  - `fingerprint: string`

    The certificate's SHA-256 fingerprint, as a lowercase hex string.

  - `tunnel_id: string`

    ID of the Tunnel this certificate is registered against.

  - `type: "tunnel_certificate"`

    Object type. Always `tunnel_certificate` for Tunnel Certificates.

    default: tunnel_certificate

### Tunnel Certificate Retrieve Response

- `TunnelCertificateRetrieveResponse object`

  - `id: string`

    ID of the Tunnel Certificate.

  - `archived_at: string or null`

    RFC 3339 datetime string indicating when the certificate was archived, or
    `null` if it is not archived.

    format: date-time

  - `created_at: string`

    RFC 3339 datetime string indicating when the certificate was registered.

    format: date-time

  - `expires_at: string or null`

    RFC 3339 datetime string indicating when the certificate expires, or
    `null` if it does not expire.

    format: date-time

  - `fingerprint: string`

    The certificate's SHA-256 fingerprint, as a lowercase hex string.

  - `tunnel_id: string`

    ID of the Tunnel this certificate is registered against.

  - `type: "tunnel_certificate"`

    Object type. Always `tunnel_certificate` for Tunnel Certificates.

    default: tunnel_certificate

### Tunnel Certificate List Response

- `TunnelCertificateListResponse object`

  - `id: string`

    ID of the Tunnel Certificate.

  - `archived_at: string or null`

    RFC 3339 datetime string indicating when the certificate was archived, or
    `null` if it is not archived.

    format: date-time

  - `created_at: string`

    RFC 3339 datetime string indicating when the certificate was registered.

    format: date-time

  - `expires_at: string or null`

    RFC 3339 datetime string indicating when the certificate expires, or
    `null` if it does not expire.

    format: date-time

  - `fingerprint: string`

    The certificate's SHA-256 fingerprint, as a lowercase hex string.

  - `tunnel_id: string`

    ID of the Tunnel this certificate is registered against.

  - `type: "tunnel_certificate"`

    Object type. Always `tunnel_certificate` for Tunnel Certificates.

    default: tunnel_certificate

### Tunnel Certificate Archive Response

- `TunnelCertificateArchiveResponse object`

  - `id: string`

    ID of the Tunnel Certificate.

  - `archived_at: string or null`

    RFC 3339 datetime string indicating when the certificate was archived, or
    `null` if it is not archived.

    format: date-time

  - `created_at: string`

    RFC 3339 datetime string indicating when the certificate was registered.

    format: date-time

  - `expires_at: string or null`

    RFC 3339 datetime string indicating when the certificate expires, or
    `null` if it does not expire.

    format: date-time

  - `fingerprint: string`

    The certificate's SHA-256 fingerprint, as a lowercase hex string.

  - `tunnel_id: string`

    ID of the Tunnel this certificate is registered against.

  - `type: "tunnel_certificate"`

    Object type. Always `tunnel_certificate` for Tunnel Certificates.

    default: tunnel_certificate
