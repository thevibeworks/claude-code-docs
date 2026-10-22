---
title: List Credentials
url: https://platform.claude.com/docs/en/api/cli/beta/vaults/credentials/list
---

# List Credentials

`$ ant beta:vaults:credentials list`

**GET** `/v1/vaults/{vault_id}/credentials`

List Credentials

## Parameters

- `--vault-id: string` (path parameter)

  Identifier of the vault to list credentials for.

- `--include-archived: optional boolean` (query parameter)

  Whether to include archived credentials in the results. Defaults to `false`.

- `--limit: optional number` (query parameter)

  Maximum number of credentials to return per page. Defaults to 20, maximum 100.

  format: int32

- `--page: optional string` (query parameter)

  The `next_page` value from a previous [List Credentials](https://platform.claude.com/docs/en/api/beta/vaults/credentials/list?sdk_languages=cli) response, to get the next page. Leave it out to get the first page.

- `--beta: optional array of AnthropicBeta` (header parameter)

  This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

- `--workspace-id: optional string` (header parameter)

  Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

  Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

## Returns

- `BetaManagedAgentsListCredentialsResponse: object`

  Response containing a paginated list of credentials.

  - `data: optional array of BetaManagedAgentsCredential`

    The credentials on this page, newest first.

    - `type: "vault_credential"`

    - `id: string`

      The unique ID of the credential (`vcrd_...`).

    - `archived_at: string`

      When the credential was archived. Null if not archived.

      format: date-time

    - `auth: BetaManagedAgentsMCPOAuthAuthResponse or BetaManagedAgentsStaticBearerAuthResponse or BetaManagedAgentsEnvironmentVariableAuthResponse`

      Authentication configuration for this credential.

      - `beta_managed_agents_mcp_oauth_auth_response: object`

        OAuth credential details for an MCP server.

        - `type: "mcp_oauth"`

        - `mcp_server_url: string`

          URL of the MCP server this credential authenticates against.

        - `expires_at: optional string`

          When the credential's access token expires, in RFC 3339. Absent if the expiry isn't known.

          format: date-time

        - `refresh: optional object`

          Refresh token configuration, if the credential supports token refresh.

          - `client_id: string`

            The OAuth client ID used when refreshing the access token.

          - `token_endpoint: string`

            Token endpoint URL used to refresh the access token.

          - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse or BetaManagedAgentsTokenEndpointAuthBasicResponse or BetaManagedAgentsTokenEndpointAuthPostResponse`

            - `beta_managed_agents_token_endpoint_auth_none_response: object`

              Token endpoint requires no client authentication.

              - `type: "none"`

            - `beta_managed_agents_token_endpoint_auth_basic_response: object`

              Token endpoint uses HTTP Basic authentication with client credentials.

              - `type: "client_secret_basic"`

            - `beta_managed_agents_token_endpoint_auth_post_response: object`

              Token endpoint uses POST body authentication with client credentials.

              - `type: "client_secret_post"`

          - `resource: optional string`

            OAuth resource indicator.

          - `scope: optional string`

            OAuth scope for the refresh request.

      - `beta_managed_agents_static_bearer_auth_response: object`

        Static bearer token credential details for an MCP server.

        - `type: "static_bearer"`

        - `mcp_server_url: string`

          URL of the MCP server this credential authenticates against.

      - `beta_managed_agents_environment_variable_auth_response: object`

        Environment variable credential details. The secret value is never returned.

        - `type: "environment_variable"`

        - `injection_location: object`

          Where in the outbound request the secret value is substituted.

          - `body: boolean`

            Whether the placeholder is substituted in the request body.

          - `header: boolean`

            Whether the placeholder is substituted in request header values.

        - `networking: BetaManagedAgentsUnrestrictedCredentialNetworkingResponse or BetaManagedAgentsLimitedCredentialNetworkingResponse`

          Outbound hosts the secret value is substituted on.

          - `beta_managed_agents_unrestricted_credential_networking_response: object`

            The secret is substituted on any host the session's Environment network policy permits egress to.

            - `type: "unrestricted"`

          - `beta_managed_agents_limited_credential_networking_response: object`

            The secret is substituted only on requests to the listed hosts.

            - `type: "limited"`

            - `allowed_hosts: array of string`

              The destination hosts of the outbound requests that the credential's secret is substituted into.

              An entry matches the request host exactly. An entry such as `*.example.com` matches any subdomain of `example.com` but not `example.com` itself.

        - `secret_name: string`

          Name of the environment variable.

    - `created_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `metadata: map[string]`

      Arbitrary key-value metadata attached to the credential.

    - `updated_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `vault_id: string`

      Identifier of the vault this credential belongs to.

    - `display_name: optional string`

      Human-readable name for the credential.

  - `next_page: optional string`

    Pagination token for the next page, or null if no more results.

## Example

```bash
ant beta:vaults:credentials list \
  --vault-id vlt_011CZkZDLs7fYzm1hXNPeRjv
```

### Response (200)

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
