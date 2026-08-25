# Credentials

## Create Credential

`$ ant beta:vaults:credentials create`

**POST** `/v1/vaults/{vault_id}/credentials`

Create Credential

### Parameters

- `--vault-id: string`

  Path param: Path parameter vault_id

- `--auth: BetaManagedAgentsMCPOAuthCreateParams or BetaManagedAgentsStaticBearerCreateParams or BetaManagedAgentsEnvironmentVariableCreateParams`

  Body param: Authentication details for creating a credential.

- `--display-name: optional string`

  Body param: Human-readable name for the credential. Up to 255 characters.

  maxLength: 255

- `--metadata: optional map[string]`

  Body param: Arbitrary key-value metadata to attach to the credential. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_credential: object`

  A credential stored in a vault. Sensitive fields are never returned in responses.

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

### Example

```bash
ant beta:vaults:credentials create \
  --api-key my-anthropic-api-key \
  --vault-id vlt_011CZkZDLs7fYzm1hXNPeRjv \
  --auth '{token: bearer_exampletoken, mcp_server_url: https://example-server.modelcontextprotocol.io/sse, type: static_bearer}'
```

#### Response (200)

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

## List Credentials

`$ ant beta:vaults:credentials list`

**GET** `/v1/vaults/{vault_id}/credentials`

List Credentials

### Parameters

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

### Returns

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

### Example

```bash
ant beta:vaults:credentials list \
  --api-key my-anthropic-api-key \
  --vault-id vlt_011CZkZDLs7fYzm1hXNPeRjv
```

#### Response (200)

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

## Get Credential

`$ ant beta:vaults:credentials retrieve`

**GET** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Get Credential

### Parameters

- `--vault-id: string`

  Path param: Path parameter vault_id

- `--credential-id: string`

  Path param: Path parameter credential_id

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_credential: object`

  A credential stored in a vault. Sensitive fields are never returned in responses.

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

### Example

```bash
ant beta:vaults:credentials retrieve \
  --api-key my-anthropic-api-key \
  --vault-id vlt_011CZkZDLs7fYzm1hXNPeRjv \
  --credential-id vcrd_011CZkZEMt8gZan2iYOQfSkw
```

#### Response (200)

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

## Update Credential

`$ ant beta:vaults:credentials update`

**POST** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Update Credential

### Parameters

- `--vault-id: string`

  Path param: Path parameter vault_id

- `--credential-id: string`

  Path param: Path parameter credential_id

- `--auth: optional BetaManagedAgentsMCPOAuthUpdateParams or BetaManagedAgentsStaticBearerUpdateParams or BetaManagedAgentsEnvironmentVariableUpdateParams`

  Body param: Updated authentication details for a credential.

- `--display-name: optional string`

  Body param: Updated human-readable name for the credential. 1-255 characters.

  minLength: 1, maxLength: 255

- `--metadata: optional map[string]`

  Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_credential: object`

  A credential stored in a vault. Sensitive fields are never returned in responses.

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

### Example

```bash
ant beta:vaults:credentials update \
  --api-key my-anthropic-api-key \
  --vault-id vlt_011CZkZDLs7fYzm1hXNPeRjv \
  --credential-id vcrd_011CZkZEMt8gZan2iYOQfSkw
```

#### Response (200)

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

## Delete Credential

`$ ant beta:vaults:credentials delete`

**DELETE** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Delete Credential

### Parameters

- `--vault-id: string`

  Path param: Path parameter vault_id

- `--credential-id: string`

  Path param: Path parameter credential_id

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_deleted_credential: object`

  Confirmation of a deleted credential.

  - `id: string`

    Unique identifier of the deleted credential.

  - `type: "vault_credential_deleted"`

### Example

```bash
ant beta:vaults:credentials delete \
  --api-key my-anthropic-api-key \
  --vault-id vlt_011CZkZDLs7fYzm1hXNPeRjv \
  --credential-id vcrd_011CZkZEMt8gZan2iYOQfSkw
```

#### Response (200)

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "type": "vault_credential_deleted"
}
```

## Archive Credential

`$ ant beta:vaults:credentials archive`

**POST** `/v1/vaults/{vault_id}/credentials/{credential_id}/archive`

Archive Credential

### Parameters

- `--vault-id: string`

  Path param: Path parameter vault_id

- `--credential-id: string`

  Path param: Path parameter credential_id

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_credential: object`

  A credential stored in a vault. Sensitive fields are never returned in responses.

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

### Example

```bash
ant beta:vaults:credentials archive \
  --api-key my-anthropic-api-key \
  --vault-id vlt_011CZkZDLs7fYzm1hXNPeRjv \
  --credential-id vcrd_011CZkZEMt8gZan2iYOQfSkw
```

#### Response (200)

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

## Validate Credential

`$ ant beta:vaults:credentials mcp-oauth-validate`

**POST** `/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate`

Validate Credential

### Parameters

- `--vault-id: string`

  Path param: Path parameter vault_id

- `--credential-id: string`

  Path param: Path parameter credential_id

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_credential_validation: object`

  Result of live-probing a credential against its configured MCP server.

  - `credential_id: string`

    Unique identifier of the credential that was validated.

  - `has_refresh_token: boolean`

    Whether the credential has a refresh token configured.

  - `mcp_probe: object`

    The failing step of an MCP validation probe.

    - `http_response: object`

      An HTTP response captured during a credential validation probe.

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

    Outcome of a refresh-token exchange attempted during credential validation.

    - `http_response: object`

      An HTTP response captured during a credential validation probe.

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

      Outcome of a refresh-token exchange attempted during credential validation.

      - `"succeeded"`

      - `"failed"`

      - `"connect_error"`

      - `"no_refresh_token"`

  - `status: "valid" or "invalid" or "unknown"`

    Overall verdict of a credential validation probe.

    - `"valid"`

    - `"invalid"`

    - `"unknown"`

  - `type: "vault_credential_validation"`

  - `validated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `vault_id: string`

    Identifier of the vault containing the credential.

### Example

```bash
ant beta:vaults:credentials mcp-oauth-validate \
  --api-key my-anthropic-api-key \
  --vault-id vlt_011CZkZDLs7fYzm1hXNPeRjv \
  --credential-id vcrd_011CZkZEMt8gZan2iYOQfSkw
```

#### Response (200)

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

## Domain types

### Beta Managed Agents Credential

- `beta_managed_agents_credential: object`

  A credential stored in a vault. Sensitive fields are never returned in responses.

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

### Beta Managed Agents Credential Networking Params

- `beta_managed_agents_credential_networking_params: BetaManagedAgentsUnrestrictedCredentialNetworkingParams or BetaManagedAgentsLimitedCredentialNetworkingParams`

  Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

  - `beta_managed_agents_unrestricted_credential_networking_params: object`

    Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

    - `type: "unrestricted"`

  - `beta_managed_agents_limited_credential_networking_params: object`

    Substitute the secret only on requests to the listed hosts.

    - `allowed_hosts: array of string`

      Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

    - `type: "limited"`

### Beta Managed Agents Credential Validation

- `beta_managed_agents_credential_validation: object`

  Result of live-probing a credential against its configured MCP server.

  - `credential_id: string`

    Unique identifier of the credential that was validated.

  - `has_refresh_token: boolean`

    Whether the credential has a refresh token configured.

  - `mcp_probe: object`

    The failing step of an MCP validation probe.

    - `http_response: object`

      An HTTP response captured during a credential validation probe.

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

    Outcome of a refresh-token exchange attempted during credential validation.

    - `http_response: object`

      An HTTP response captured during a credential validation probe.

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

      Outcome of a refresh-token exchange attempted during credential validation.

      - `"succeeded"`

      - `"failed"`

      - `"connect_error"`

      - `"no_refresh_token"`

  - `status: "valid" or "invalid" or "unknown"`

    Overall verdict of a credential validation probe.

    - `"valid"`

    - `"invalid"`

    - `"unknown"`

  - `type: "vault_credential_validation"`

  - `validated_at: string`

    A timestamp in RFC 3339 format

    format: date-time

  - `vault_id: string`

    Identifier of the vault containing the credential.

### Beta Managed Agents Credential Validation Status

- `beta_managed_agents_credential_validation_status: "valid" or "invalid" or "unknown"`

  Overall verdict of a credential validation probe.

  - `"valid"`

  - `"invalid"`

  - `"unknown"`

### Beta Managed Agents Deleted Credential

- `beta_managed_agents_deleted_credential: object`

  Confirmation of a deleted credential.

  - `id: string`

    Unique identifier of the deleted credential.

  - `type: "vault_credential_deleted"`

### Beta Managed Agents Environment Variable Auth Response

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

### Beta Managed Agents Environment Variable Create Params

- `beta_managed_agents_environment_variable_create_params: object`

  Parameters for creating an environment variable credential.

  - `networking: BetaManagedAgentsUnrestrictedCredentialNetworkingParams or BetaManagedAgentsLimitedCredentialNetworkingParams`

    Outbound hosts the secret value is substituted on.

    - `beta_managed_agents_unrestricted_credential_networking_params: object`

      Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

      - `type: "unrestricted"`

    - `beta_managed_agents_limited_credential_networking_params: object`

      Substitute the secret only on requests to the listed hosts.

      - `allowed_hosts: array of string`

        Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

      - `type: "limited"`

  - `secret_name: string`

    Name of the environment variable. Immutable after create.

    minLength: 1, maxLength: 255

  - `secret_value: string`

    Secret value. Write-only; never returned in responses.

    minLength: 1, maxLength: 4096

  - `type: "environment_variable"`

  - `injection_location: optional object`

    Where in the outbound request the secret value may be substituted.

    - `body: optional boolean`

      Substitute when the placeholder appears in the request body.

    - `header: optional boolean`

      Substitute when the placeholder appears in a request header value.

### Beta Managed Agents Environment Variable Update Params

- `beta_managed_agents_environment_variable_update_params: object`

  Parameters for updating an environment variable credential. `secret_name` is immutable.

  - `type: "environment_variable"`

  - `injection_location: optional object`

    Updated injection location.

    - `body: optional boolean`

      Substitute when the placeholder appears in the request body.

    - `header: optional boolean`

      Substitute when the placeholder appears in a request header value.

  - `networking: optional BetaManagedAgentsUnrestrictedCredentialNetworkingParams or BetaManagedAgentsLimitedCredentialNetworkingParams`

    Updated networking scope. Full replacement.

    - `beta_managed_agents_unrestricted_credential_networking_params: object`

      Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

      - `type: "unrestricted"`

    - `beta_managed_agents_limited_credential_networking_params: object`

      Substitute the secret only on requests to the listed hosts.

      - `allowed_hosts: array of string`

        Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

      - `type: "limited"`

  - `secret_value: optional string`

    Updated secret value.

    minLength: 1, maxLength: 4096

### Beta Managed Agents Injection Location Params

- `beta_managed_agents_injection_location_params: object`

  Where in the outbound request the secret value may be substituted.

  - `body: optional boolean`

    Substitute when the placeholder appears in the request body.

  - `header: optional boolean`

    Substitute when the placeholder appears in a request header value.

### Beta Managed Agents Injection Location Response

- `beta_managed_agents_injection_location_response: object`

  Where in the outbound request the secret value is substituted.

  - `body: boolean`

    Whether the placeholder is substituted in the request body.

  - `header: boolean`

    Whether the placeholder is substituted in request header values.

### Beta Managed Agents Injection Location Update Params

- `beta_managed_agents_injection_location_update_params: object`

  Updated injection location.

  - `body: optional boolean`

    Substitute when the placeholder appears in the request body.

  - `header: optional boolean`

    Substitute when the placeholder appears in a request header value.

### Beta Managed Agents Limited Credential Networking Params

- `beta_managed_agents_limited_credential_networking_params: object`

  Substitute the secret only on requests to the listed hosts.

  - `allowed_hosts: array of string`

    Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

  - `type: "limited"`

### Beta Managed Agents Limited Credential Networking Response

- `beta_managed_agents_limited_credential_networking_response: object`

  The secret is substituted only on requests to the listed hosts.

  - `allowed_hosts: array of string`

    Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

  - `type: "limited"`

### Beta Managed Agents MCP OAuth Auth Response

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

### Beta Managed Agents MCP OAuth Create Params

- `beta_managed_agents_mcp_oauth_create_params: object`

  Parameters for creating an MCP OAuth credential.

  - `access_token: string`

    OAuth access token.

    minLength: 1, maxLength: 8192

  - `mcp_server_url: string`

    URL of the MCP server this credential authenticates against.

    minLength: 1, maxLength: 2047

  - `type: "mcp_oauth"`

  - `expires_at: optional string`

    A timestamp in RFC 3339 format

    format: date-time

  - `refresh: optional object`

    OAuth refresh token parameters for creating a credential with refresh support.

    - `client_id: string`

      OAuth client ID.

      minLength: 1, maxLength: 1024

    - `refresh_token: string`

      OAuth refresh token.

      minLength: 1, maxLength: 4096

    - `token_endpoint: string`

      Token endpoint URL used to refresh the access token.

      minLength: 1, maxLength: 2047

    - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneParam or BetaManagedAgentsTokenEndpointAuthBasicParam or BetaManagedAgentsTokenEndpointAuthPostParam`

      Token endpoint requires no client authentication.

      - `beta_managed_agents_token_endpoint_auth_none_param: object`

        Token endpoint requires no client authentication.

        - `type: "none"`

      - `beta_managed_agents_token_endpoint_auth_basic_param: object`

        Token endpoint uses HTTP Basic authentication with client credentials.

        - `client_secret: string`

          OAuth client secret.

          minLength: 1, maxLength: 512

        - `type: "client_secret_basic"`

      - `beta_managed_agents_token_endpoint_auth_post_param: object`

        Token endpoint uses POST body authentication with client credentials.

        - `client_secret: string`

          OAuth client secret.

          minLength: 1, maxLength: 512

        - `type: "client_secret_post"`

    - `resource: optional string`

      OAuth resource indicator.

      minLength: 1, maxLength: 2047

    - `scope: optional string`

      OAuth scope for the refresh request.

      minLength: 1, maxLength: 8192

### Beta Managed Agents MCP OAuth Refresh Params

- `beta_managed_agents_mcp_oauth_refresh_params: object`

  OAuth refresh token parameters for creating a credential with refresh support.

  - `client_id: string`

    OAuth client ID.

    minLength: 1, maxLength: 1024

  - `refresh_token: string`

    OAuth refresh token.

    minLength: 1, maxLength: 4096

  - `token_endpoint: string`

    Token endpoint URL used to refresh the access token.

    minLength: 1, maxLength: 2047

  - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneParam or BetaManagedAgentsTokenEndpointAuthBasicParam or BetaManagedAgentsTokenEndpointAuthPostParam`

    Token endpoint requires no client authentication.

    - `beta_managed_agents_token_endpoint_auth_none_param: object`

      Token endpoint requires no client authentication.

      - `type: "none"`

    - `beta_managed_agents_token_endpoint_auth_basic_param: object`

      Token endpoint uses HTTP Basic authentication with client credentials.

      - `client_secret: string`

        OAuth client secret.

        minLength: 1, maxLength: 512

      - `type: "client_secret_basic"`

    - `beta_managed_agents_token_endpoint_auth_post_param: object`

      Token endpoint uses POST body authentication with client credentials.

      - `client_secret: string`

        OAuth client secret.

        minLength: 1, maxLength: 512

      - `type: "client_secret_post"`

  - `resource: optional string`

    OAuth resource indicator.

    minLength: 1, maxLength: 2047

  - `scope: optional string`

    OAuth scope for the refresh request.

    minLength: 1, maxLength: 8192

### Beta Managed Agents MCP OAuth Refresh Response

- `beta_managed_agents_mcp_oauth_refresh_response: object`

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

### Beta Managed Agents MCP OAuth Refresh Update Params

- `beta_managed_agents_mcp_oauth_refresh_update_params: object`

  Parameters for updating OAuth refresh token configuration.

  - `refresh_token: optional string`

    Updated OAuth refresh token.

    minLength: 1, maxLength: 4096

  - `scope: optional string`

    Updated OAuth scope for the refresh request.

    maxLength: 8192

  - `token_endpoint_auth: optional BetaManagedAgentsTokenEndpointAuthBasicUpdateParam or BetaManagedAgentsTokenEndpointAuthPostUpdateParam`

    Updated HTTP Basic authentication parameters for the token endpoint.

    - `beta_managed_agents_token_endpoint_auth_basic_update_param: object`

      Updated HTTP Basic authentication parameters for the token endpoint.

      - `type: "client_secret_basic"`

      - `client_secret: optional string`

        Updated OAuth client secret.

        minLength: 1, maxLength: 512

    - `beta_managed_agents_token_endpoint_auth_post_update_param: object`

      Updated POST body authentication parameters for the token endpoint.

      - `type: "client_secret_post"`

      - `client_secret: optional string`

        Updated OAuth client secret.

        minLength: 1, maxLength: 512

### Beta Managed Agents MCP OAuth Update Params

- `beta_managed_agents_mcp_oauth_update_params: object`

  Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

  - `type: "mcp_oauth"`

  - `access_token: optional string`

    Updated OAuth access token.

    minLength: 1, maxLength: 8192

  - `expires_at: optional string`

    A timestamp in RFC 3339 format

    format: date-time

  - `refresh: optional object`

    Parameters for updating OAuth refresh token configuration.

    - `refresh_token: optional string`

      Updated OAuth refresh token.

      minLength: 1, maxLength: 4096

    - `scope: optional string`

      Updated OAuth scope for the refresh request.

      maxLength: 8192

    - `token_endpoint_auth: optional BetaManagedAgentsTokenEndpointAuthBasicUpdateParam or BetaManagedAgentsTokenEndpointAuthPostUpdateParam`

      Updated HTTP Basic authentication parameters for the token endpoint.

      - `beta_managed_agents_token_endpoint_auth_basic_update_param: object`

        Updated HTTP Basic authentication parameters for the token endpoint.

        - `type: "client_secret_basic"`

        - `client_secret: optional string`

          Updated OAuth client secret.

          minLength: 1, maxLength: 512

      - `beta_managed_agents_token_endpoint_auth_post_update_param: object`

        Updated POST body authentication parameters for the token endpoint.

        - `type: "client_secret_post"`

        - `client_secret: optional string`

          Updated OAuth client secret.

          minLength: 1, maxLength: 512

### Beta Managed Agents MCP Probe

- `beta_managed_agents_mcp_probe: object`

  The failing step of an MCP validation probe.

  - `http_response: object`

    An HTTP response captured during a credential validation probe.

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

### Beta Managed Agents Refresh HTTP Response

- `beta_managed_agents_refresh_http_response: object`

  An HTTP response captured during a credential validation probe.

  - `body: string`

    Response body. May be truncated and has sensitive values scrubbed.

  - `body_truncated: boolean`

    Whether `body` was truncated.

  - `content_type: string`

    Value of the `Content-Type` response header.

  - `status_code: number`

    HTTP status code.

    format: int32

### Beta Managed Agents Refresh Object

- `beta_managed_agents_refresh_object: object`

  Outcome of a refresh-token exchange attempted during credential validation.

  - `http_response: object`

    An HTTP response captured during a credential validation probe.

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

    Outcome of a refresh-token exchange attempted during credential validation.

    - `"succeeded"`

    - `"failed"`

    - `"connect_error"`

    - `"no_refresh_token"`

### Beta Managed Agents Static Bearer Auth Response

- `beta_managed_agents_static_bearer_auth_response: object`

  Static bearer token credential details for an MCP server.

  - `mcp_server_url: string`

    URL of the MCP server this credential authenticates against.

  - `type: "static_bearer"`

### Beta Managed Agents Static Bearer Create Params

- `beta_managed_agents_static_bearer_create_params: object`

  Parameters for creating a static bearer token credential.

  - `token: string`

    Static bearer token value.

    minLength: 1, maxLength: 8192

  - `mcp_server_url: string`

    URL of the MCP server this credential authenticates against.

    minLength: 1, maxLength: 2047

  - `type: "static_bearer"`

### Beta Managed Agents Static Bearer Update Params

- `beta_managed_agents_static_bearer_update_params: object`

  Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

  - `type: "static_bearer"`

  - `token: optional string`

    Updated static bearer token value.

    minLength: 1, maxLength: 8192

### Beta Managed Agents Token Endpoint Auth Basic Param

- `beta_managed_agents_token_endpoint_auth_basic_param: object`

  Token endpoint uses HTTP Basic authentication with client credentials.

  - `client_secret: string`

    OAuth client secret.

    minLength: 1, maxLength: 512

  - `type: "client_secret_basic"`

### Beta Managed Agents Token Endpoint Auth Basic Response

- `beta_managed_agents_token_endpoint_auth_basic_response: object`

  Token endpoint uses HTTP Basic authentication with client credentials.

  - `type: "client_secret_basic"`

### Beta Managed Agents Token Endpoint Auth Basic Update Param

- `beta_managed_agents_token_endpoint_auth_basic_update_param: object`

  Updated HTTP Basic authentication parameters for the token endpoint.

  - `type: "client_secret_basic"`

  - `client_secret: optional string`

    Updated OAuth client secret.

    minLength: 1, maxLength: 512

### Beta Managed Agents Token Endpoint Auth None Param

- `beta_managed_agents_token_endpoint_auth_none_param: object`

  Token endpoint requires no client authentication.

  - `type: "none"`

### Beta Managed Agents Token Endpoint Auth None Response

- `beta_managed_agents_token_endpoint_auth_none_response: object`

  Token endpoint requires no client authentication.

  - `type: "none"`

### Beta Managed Agents Token Endpoint Auth Post Param

- `beta_managed_agents_token_endpoint_auth_post_param: object`

  Token endpoint uses POST body authentication with client credentials.

  - `client_secret: string`

    OAuth client secret.

    minLength: 1, maxLength: 512

  - `type: "client_secret_post"`

### Beta Managed Agents Token Endpoint Auth Post Response

- `beta_managed_agents_token_endpoint_auth_post_response: object`

  Token endpoint uses POST body authentication with client credentials.

  - `type: "client_secret_post"`

### Beta Managed Agents Token Endpoint Auth Post Update Param

- `beta_managed_agents_token_endpoint_auth_post_update_param: object`

  Updated POST body authentication parameters for the token endpoint.

  - `type: "client_secret_post"`

  - `client_secret: optional string`

    Updated OAuth client secret.

    minLength: 1, maxLength: 512

### Beta Managed Agents Unrestricted Credential Networking Params

- `beta_managed_agents_unrestricted_credential_networking_params: object`

  Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

  - `type: "unrestricted"`

### Beta Managed Agents Unrestricted Credential Networking Response

- `beta_managed_agents_unrestricted_credential_networking_response: object`

  The secret is substituted on any host the session's Environment network policy permits egress to.

  - `type: "unrestricted"`
