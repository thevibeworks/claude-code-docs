# List Credentials

`$ ant beta:vaults:credentials list`

**GET** `/v1/vaults/{vault_id}/credentials`

List Credentials

## Parameters

- `--vault-id: string`

  Path param: Path parameter vault_id

- `--include-archived: optional boolean`

  Query param: Whether to include archived credentials in the results.

- `--limit: optional number`

  Query param: Maximum number of credentials to return per page. Defaults to 20, maximum 100.

  format: int32

- `--page: optional string`

  Query param: Opaque pagination token from a previous `list_credentials` response.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

## Returns

- `BetaManagedAgentsListCredentialsResponse: object`

  Response containing a paginated list of credentials.

  - `data: optional array of BetaManagedAgentsCredential`

    List of credentials.

    - `id: string`

      Unique identifier for the credential.

    - `archived_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `auth: BetaManagedAgentsMCPOAuthAuthResponse or BetaManagedAgentsStaticBearerAuthResponse or BetaManagedAgentsEnvironmentVariableAuthResponse`

      Authentication details for a credential.

      - `beta_managed_agents_mcp_oauth_auth_response: object`

        OAuth credential details for an MCP server.

        - `mcp_server_url: string`

          URL of the MCP server this credential authenticates against.

        - `type: "mcp_oauth"`

        - `expires_at: optional string`

          A timestamp in RFC 3339 format

          format: date-time

        - `refresh: optional object`

          OAuth refresh token configuration returned in credential responses.

          - `client_id: string`

            OAuth client ID.

          - `token_endpoint: string`

            Token endpoint URL used to refresh the access token.

          - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse or BetaManagedAgentsTokenEndpointAuthBasicResponse or BetaManagedAgentsTokenEndpointAuthPostResponse`

            Token endpoint requires no client authentication.

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

        - `mcp_server_url: string`

          URL of the MCP server this credential authenticates against.

        - `type: "static_bearer"`

      - `beta_managed_agents_environment_variable_auth_response: object`

        Environment variable credential details. The secret value is never returned.

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

            - `allowed_hosts: array of string`

              Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

            - `type: "limited"`

        - `secret_name: string`

          Name of the environment variable.

        - `type: "environment_variable"`

    - `created_at: string`

      A timestamp in RFC 3339 format

      format: date-time

    - `metadata: map[string]`

      Arbitrary key-value metadata attached to the credential.

    - `type: "vault_credential"`

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
  --api-key my-anthropic-api-key \
  --vault-id vlt_011CZkZDLs7fYzm1hXNPeRjv
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
