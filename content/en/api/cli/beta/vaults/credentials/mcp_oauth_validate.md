---
title: Validate an MCP OAuth Credential
url: https://platform.claude.com/docs/en/api/cli/beta/vaults/credentials/mcp_oauth_validate
---

# Validate an MCP OAuth Credential

`$ ant beta:vaults:credentials mcp-oauth-validate`

**POST** `/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate`

Validate an MCP OAuth Credential

## Parameters

- `--vault-id: string` (path parameter)

  Identifier of the vault containing the credential.

- `--credential-id: string` (path parameter)

  Unique identifier of the credential to validate.

- `--beta: optional array of AnthropicBeta` (header parameter)

  This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

- `--workspace-id: optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `beta_managed_agents_credential_validation: object`

  Result of live-probing a credential against its configured MCP server.

  - `type: "vault_credential_validation"`

  - `credential_id: string`

    Unique identifier of the credential that was validated.

  - `has_refresh_token: boolean`

    Whether the credential has a refresh token configured.

  - `mcp_probe: object`

    Details of the MCP probe step that failed, or `null` if the probe succeeded or there was no access token to test.

    - `http_response: object`

      The HTTP error response from the MCP server, or `null` if the MCP server didn't return one for the failing step, for example after a timeout or a DNS or TLS failure.

      - `body: string`

        Response body. May be truncated and has sensitive values scrubbed.

      - `body_truncated: boolean`

        Whether `body` was truncated.

      - `content_type: string`

        Value of the `Content-Type` response header.

      - `status_code: number`

        HTTP status code.

        format: int32

    - `method: string`

      The MCP method that failed (for example `initialize` or `tools/list`).

  - `refresh: object`

    Details of the refresh-token exchange attempted on a 401. Null when no refresh was attempted.

    - `http_response: object`

      The captured HTTP error response from the token endpoint. Populated only when `status` is `failed`.

      - `body: string`

        Response body. May be truncated and has sensitive values scrubbed.

      - `body_truncated: boolean`

        Whether `body` was truncated.

      - `content_type: string`

        Value of the `Content-Type` response header.

      - `status_code: number`

        HTTP status code.

        format: int32

    - `status: "succeeded" or "failed" or "connect_error" or "no_refresh_token"`

      Outcome of the refresh attempt.

      - `"succeeded"`

        The token endpoint returned a new access token.

      - `"failed"`

        The token endpoint returned an error response. See `http_response` for detail.

      - `"connect_error"`

        The token endpoint could not be reached (DNS, TLS, or connection error).

      - `"no_refresh_token"`

        No refresh token is stored for the credential, so no exchange was attempted.

  - `status: "valid" or "invalid" or "unknown"`

    Overall verdict of the validation probe.

    - `"valid"`

      The credential successfully authenticated against its MCP server.

    - `"invalid"`

      The probe reached the MCP server and the server rejected the credential, or no access token is stored. A refresh, if one was tried, didn't recover it. Usually the end user needs to authorize again.

    - `"unknown"`

      The probe couldn't tell whether the credential works, for example because of a network error or because a refresh succeeded but the new access token wasn't tested. Validate the credential again to find out.

  - `validated_at: string`

    When the validation probe was performed.

    format: date-time

  - `vault_id: string`

    Identifier of the vault containing the credential.

## Example

```bash
ant beta:vaults:credentials mcp-oauth-validate \
  --vault-id vlt_011CZkZDLs7fYzm1hXNPeRjv \
  --credential-id vcrd_011CZkZEMt8gZan2iYPQfSkw
```

### Response (200)

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
