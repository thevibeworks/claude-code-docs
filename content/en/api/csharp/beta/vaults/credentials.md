---
title: Credentials
url: https://platform.claude.com/docs/en/api/csharp/beta/vaults/credentials
---

# Credentials

## Create a Credential

`BetaManagedAgentsCredential Beta.Vaults.Credentials.Create(parameters, cancellationToken = default)`

**POST** `/v1/vaults/{vault_id}/credentials`

Create a Credential

### Parameters

- `CredentialCreateParams parameters`

  - `required string vaultID` (path parameter)

    Identifier of the vault to create the credential in.

  - `required Auth auth`

    Authentication configuration for the credential.

    - `class BetaManagedAgentsMcpOAuthCreateParams`

      Parameters for creating an MCP OAuth credential.

      - `JsonElement Type = "mcp_oauth"`

      - `required string AccessToken`

        The OAuth access token to send to the MCP server.

        minLength: 1, maxLength: 8192

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

        minLength: 1, maxLength: 2047

      - `DateTimeOffset? ExpiresAt`

        When `access_token` expires, in RFC 3339.

        Must be in the future.

        format: date-time

      - `BetaManagedAgentsMcpOAuthRefreshParams? Refresh`

        Refresh token configuration, if the credential supports token refresh.

        - `required string ClientID`

          The OAuth client ID to use when refreshing the access token. It can't be changed after the credential is created.

          minLength: 1, maxLength: 1024

        - `required string RefreshToken`

          The OAuth refresh token that the API uses to get a new access token when the current one expires.

          minLength: 1, maxLength: 8192

        - `required string TokenEndpoint`

          Token endpoint URL used to refresh the access token.

          minLength: 1, maxLength: 2047

        - `required TokenEndpointAuth TokenEndpointAuth`

          - `class BetaManagedAgentsTokenEndpointAuthNoneParam`

            Token endpoint requires no client authentication.

            - `JsonElement Type = "none"`

          - `class BetaManagedAgentsTokenEndpointAuthBasicParam`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `JsonElement Type = "client_secret_basic"`

            - `required string ClientSecret`

              The OAuth client secret, sent to `token_endpoint` with HTTP Basic authentication.

              minLength: 1, maxLength: 512

          - `class BetaManagedAgentsTokenEndpointAuthPostParam`

            Token endpoint uses POST body authentication with client credentials.

            - `JsonElement Type = "client_secret_post"`

            - `required string ClientSecret`

              The OAuth client secret, sent to `token_endpoint` in the POST body.

              minLength: 1, maxLength: 512

        - `string? Resource`

          OAuth resource indicator.

          minLength: 1, maxLength: 2047

        - `string? Scope`

          OAuth scope for the refresh request.

          minLength: 1, maxLength: 8192

    - `class BetaManagedAgentsStaticBearerCreateParams`

      Parameters for creating a static bearer token credential.

      - `JsonElement Type = "static_bearer"`

      - `required string Token`

        The static bearer token to send to the MCP server, such as an API key or personal access token.

        minLength: 1, maxLength: 8192

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

        minLength: 1, maxLength: 2047

    - `class BetaManagedAgentsEnvironmentVariableCreateParams`

      Parameters for creating an environment variable credential.

      - `JsonElement Type = "environment_variable"`

      - `required BetaManagedAgentsCredentialNetworkingParams Networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingParams`

          Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

          - `JsonElement Type = "unrestricted"`

        - `class BetaManagedAgentsLimitedCredentialNetworkingParams`

          Substitute the secret only on requests to the listed hosts.

          - `JsonElement Type = "limited"`

          - `required IReadOnlyList<string> AllowedHosts`

            The destination hosts of the outbound requests that the credential's secret is substituted into.

            Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.` wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses aren't accepted. The list can have up to 16 entries.

      - `required string SecretName`

        Name of the environment variable. Immutable after create.

        minLength: 1, maxLength: 255

      - `required string SecretValue`

        The secret to substitute into the agent's outbound requests. It's write-only and never returned in responses.

        minLength: 1, maxLength: 4096

      - `BetaManagedAgentsInjectionLocationParams InjectionLocation`

        Where in the outbound request the secret value may be substituted.

        - `bool Body`

          Substitute when the placeholder appears in the request body.

        - `bool Header`

          Substitute when the placeholder appears in a request header value.

  - `string? displayName`

    Human-readable name for the credential. Up to 255 characters.

    maxLength: 255

  - `IReadOnlyDictionary<string, string> metadata`

    Arbitrary key-value metadata to attach to the credential. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `IReadOnlyList<AnthropicBeta> betas` (header parameter)

    This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

    - `Compact2026_09_04("compact-2026-09-04")`

    - `InlineTools2026_09_15("inline-tools-2026-09-15")`

    - `McpClient2026_09_15("mcp-client-2026-09-15")`

    - `CEPlugins2026_09_01("ce-plugins-2026-09-01")`

    - `SpendLimitReads2026_09_26("spend-limit-reads-2026-09-26")`

    - `TelemetryDestinations2026_08_11("telemetry-destinations-2026-08-11")`

    - `Webhooks2026_10_07("webhooks-2026-10-07")`

  - `string workspaceID` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsCredential`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `JsonElement Type = "vault_credential"`

  - `required string ID`

    The unique ID of the credential (`vcrd_...`).

  - `required DateTimeOffset? ArchivedAt`

    When the credential was archived. Null if not archived.

    format: date-time

  - `required Auth Auth`

    Authentication configuration for this credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse`

      OAuth credential details for an MCP server.

      - `JsonElement Type = "mcp_oauth"`

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `DateTimeOffset? ExpiresAt`

        When the credential's access token expires, in RFC 3339. Absent if the expiry isn't known.

        format: date-time

      - `BetaManagedAgentsMcpOAuthRefreshResponse? Refresh`

        Refresh token configuration, if the credential supports token refresh.

        - `required string ClientID`

          The OAuth client ID used when refreshing the access token.

        - `required string TokenEndpoint`

          Token endpoint URL used to refresh the access token.

        - `required TokenEndpointAuth TokenEndpointAuth`

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse`

            Token endpoint requires no client authentication.

            - `JsonElement Type = "none"`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `JsonElement Type = "client_secret_basic"`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse`

            Token endpoint uses POST body authentication with client credentials.

            - `JsonElement Type = "client_secret_post"`

        - `string? Resource`

          OAuth resource indicator.

        - `string? Scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse`

      Static bearer token credential details for an MCP server.

      - `JsonElement Type = "static_bearer"`

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse`

      Environment variable credential details. The secret value is never returned.

      - `JsonElement Type = "environment_variable"`

      - `required BetaManagedAgentsInjectionLocationResponse InjectionLocation`

        Where in the outbound request the secret value is substituted.

        - `required bool Body`

          Whether the placeholder is substituted in the request body.

        - `required bool Header`

          Whether the placeholder is substituted in request header values.

      - `required Networking Networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `JsonElement Type = "unrestricted"`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse`

          The secret is substituted only on requests to the listed hosts.

          - `JsonElement Type = "limited"`

          - `required IReadOnlyList<string> AllowedHosts`

            The destination hosts of the outbound requests that the credential's secret is substituted into.

            An entry matches the request host exactly. An entry such as `*.example.com` matches any subdomain of `example.com` but not `example.com` itself.

      - `required string SecretName`

        Name of the environment variable.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata attached to the credential.

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string VaultID`

    Identifier of the vault this credential belongs to.

  - `string? DisplayName`

    Human-readable name for the credential.

### Example

```csharp
using System;
using Anthropic.Models.Beta.Vaults.Credentials;

CredentialCreateParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    Auth = new BetaManagedAgentsStaticBearerCreateParams()
    {
        Token = "bearer_exampletoken",
        McpServerUrl = "https://example-server.modelcontextprotocol.io/sse",
    },
};

var betaManagedAgentsCredential = await client.Beta.Vaults.Credentials.Create(parameters);

Console.WriteLine(betaManagedAgentsCredential);
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

`CredentialListPage Beta.Vaults.Credentials.List(parameters, cancellationToken = default)`

**GET** `/v1/vaults/{vault_id}/credentials`

List Credentials

### Parameters

- `CredentialListParams parameters`

  - `required string vaultID` (path parameter)

    Identifier of the vault to list credentials for.

  - `bool includeArchived` (query parameter)

    Whether to include archived credentials in the results. Defaults to `false`.

  - `int limit` (query parameter)

    Maximum number of credentials to return per page. Defaults to 20, maximum 100.

    format: int32

  - `string page` (query parameter)

    The `next_page` value from a previous [List Credentials](https://platform.claude.com/docs/en/api/beta/vaults/credentials/list?sdk_languages=csharp) response, to get the next page. Leave it out to get the first page.

  - `IReadOnlyList<AnthropicBeta> betas` (header parameter)

    This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

    - `Compact2026_09_04("compact-2026-09-04")`

    - `InlineTools2026_09_15("inline-tools-2026-09-15")`

    - `McpClient2026_09_15("mcp-client-2026-09-15")`

    - `CEPlugins2026_09_01("ce-plugins-2026-09-01")`

    - `SpendLimitReads2026_09_26("spend-limit-reads-2026-09-26")`

    - `TelemetryDestinations2026_08_11("telemetry-destinations-2026-08-11")`

    - `Webhooks2026_10_07("webhooks-2026-10-07")`

  - `string workspaceID` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsCredential`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `JsonElement Type = "vault_credential"`

  - `required string ID`

    The unique ID of the credential (`vcrd_...`).

  - `required DateTimeOffset? ArchivedAt`

    When the credential was archived. Null if not archived.

    format: date-time

  - `required Auth Auth`

    Authentication configuration for this credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse`

      OAuth credential details for an MCP server.

      - `JsonElement Type = "mcp_oauth"`

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `DateTimeOffset? ExpiresAt`

        When the credential's access token expires, in RFC 3339. Absent if the expiry isn't known.

        format: date-time

      - `BetaManagedAgentsMcpOAuthRefreshResponse? Refresh`

        Refresh token configuration, if the credential supports token refresh.

        - `required string ClientID`

          The OAuth client ID used when refreshing the access token.

        - `required string TokenEndpoint`

          Token endpoint URL used to refresh the access token.

        - `required TokenEndpointAuth TokenEndpointAuth`

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse`

            Token endpoint requires no client authentication.

            - `JsonElement Type = "none"`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `JsonElement Type = "client_secret_basic"`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse`

            Token endpoint uses POST body authentication with client credentials.

            - `JsonElement Type = "client_secret_post"`

        - `string? Resource`

          OAuth resource indicator.

        - `string? Scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse`

      Static bearer token credential details for an MCP server.

      - `JsonElement Type = "static_bearer"`

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse`

      Environment variable credential details. The secret value is never returned.

      - `JsonElement Type = "environment_variable"`

      - `required BetaManagedAgentsInjectionLocationResponse InjectionLocation`

        Where in the outbound request the secret value is substituted.

        - `required bool Body`

          Whether the placeholder is substituted in the request body.

        - `required bool Header`

          Whether the placeholder is substituted in request header values.

      - `required Networking Networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `JsonElement Type = "unrestricted"`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse`

          The secret is substituted only on requests to the listed hosts.

          - `JsonElement Type = "limited"`

          - `required IReadOnlyList<string> AllowedHosts`

            The destination hosts of the outbound requests that the credential's secret is substituted into.

            An entry matches the request host exactly. An entry such as `*.example.com` matches any subdomain of `example.com` but not `example.com` itself.

      - `required string SecretName`

        Name of the environment variable.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata attached to the credential.

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string VaultID`

    Identifier of the vault this credential belongs to.

  - `string? DisplayName`

    Human-readable name for the credential.

### Example

```csharp
using System;
using Anthropic.Models.Beta.Vaults.Credentials;

CredentialListParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv"
};

var page = await client.Beta.Vaults.Credentials.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
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

`BetaManagedAgentsCredential Beta.Vaults.Credentials.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Retrieve a Credential

### Parameters

- `CredentialRetrieveParams parameters`

  - `required string vaultID` (path parameter)

    Identifier of the vault containing the credential.

  - `required string credentialID` (path parameter)

    Unique identifier of the credential to retrieve.

  - `IReadOnlyList<AnthropicBeta> betas` (header parameter)

    This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

    - `Compact2026_09_04("compact-2026-09-04")`

    - `InlineTools2026_09_15("inline-tools-2026-09-15")`

    - `McpClient2026_09_15("mcp-client-2026-09-15")`

    - `CEPlugins2026_09_01("ce-plugins-2026-09-01")`

    - `SpendLimitReads2026_09_26("spend-limit-reads-2026-09-26")`

    - `TelemetryDestinations2026_08_11("telemetry-destinations-2026-08-11")`

    - `Webhooks2026_10_07("webhooks-2026-10-07")`

  - `string workspaceID` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsCredential`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `JsonElement Type = "vault_credential"`

  - `required string ID`

    The unique ID of the credential (`vcrd_...`).

  - `required DateTimeOffset? ArchivedAt`

    When the credential was archived. Null if not archived.

    format: date-time

  - `required Auth Auth`

    Authentication configuration for this credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse`

      OAuth credential details for an MCP server.

      - `JsonElement Type = "mcp_oauth"`

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `DateTimeOffset? ExpiresAt`

        When the credential's access token expires, in RFC 3339. Absent if the expiry isn't known.

        format: date-time

      - `BetaManagedAgentsMcpOAuthRefreshResponse? Refresh`

        Refresh token configuration, if the credential supports token refresh.

        - `required string ClientID`

          The OAuth client ID used when refreshing the access token.

        - `required string TokenEndpoint`

          Token endpoint URL used to refresh the access token.

        - `required TokenEndpointAuth TokenEndpointAuth`

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse`

            Token endpoint requires no client authentication.

            - `JsonElement Type = "none"`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `JsonElement Type = "client_secret_basic"`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse`

            Token endpoint uses POST body authentication with client credentials.

            - `JsonElement Type = "client_secret_post"`

        - `string? Resource`

          OAuth resource indicator.

        - `string? Scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse`

      Static bearer token credential details for an MCP server.

      - `JsonElement Type = "static_bearer"`

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse`

      Environment variable credential details. The secret value is never returned.

      - `JsonElement Type = "environment_variable"`

      - `required BetaManagedAgentsInjectionLocationResponse InjectionLocation`

        Where in the outbound request the secret value is substituted.

        - `required bool Body`

          Whether the placeholder is substituted in the request body.

        - `required bool Header`

          Whether the placeholder is substituted in request header values.

      - `required Networking Networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `JsonElement Type = "unrestricted"`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse`

          The secret is substituted only on requests to the listed hosts.

          - `JsonElement Type = "limited"`

          - `required IReadOnlyList<string> AllowedHosts`

            The destination hosts of the outbound requests that the credential's secret is substituted into.

            An entry matches the request host exactly. An entry such as `*.example.com` matches any subdomain of `example.com` but not `example.com` itself.

      - `required string SecretName`

        Name of the environment variable.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata attached to the credential.

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string VaultID`

    Identifier of the vault this credential belongs to.

  - `string? DisplayName`

    Human-readable name for the credential.

### Example

```csharp
using System;
using Anthropic.Models.Beta.Vaults.Credentials;

CredentialRetrieveParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    CredentialID = "vcrd_011CZkZEMt8gZan2iYPQfSkw",
};

var betaManagedAgentsCredential = await client.Beta.Vaults.Credentials.Retrieve(parameters);

Console.WriteLine(betaManagedAgentsCredential);
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

`BetaManagedAgentsCredential Beta.Vaults.Credentials.Update(parameters, cancellationToken = default)`

**POST** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Update a Credential

### Parameters

- `CredentialUpdateParams parameters`

  - `required string vaultID` (path parameter)

    Identifier of the vault containing the credential.

  - `required string credentialID` (path parameter)

    Unique identifier of the credential to update.

  - `Auth auth`

    New authentication settings for the credential. The `type` must match the credential's current type, which can't be changed.

    - `class BetaManagedAgentsMcpOAuthUpdateParams`

      Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

      - `JsonElement Type = "mcp_oauth"`

      - `string? AccessToken`

        The new OAuth access token to replace the stored one.

        minLength: 1, maxLength: 8192

      - `DateTimeOffset? ExpiresAt`

        When the credential's access token expires, in RFC 3339. Leave it out to keep the stored expiry.

        If you send a new `access_token`, send its `expires_at` too, or the new token keeps the old expiry.

        Must be in the future.

        format: date-time

      - `BetaManagedAgentsMcpOAuthRefreshUpdateParams? Refresh`

        Updated refresh token configuration.

        - `string? RefreshToken`

          The new OAuth refresh token to replace the stored one.

          minLength: 1, maxLength: 8192

        - `string? Scope`

          The new OAuth scope for refresh requests. Send an empty string to clear the stored scope.

          maxLength: 8192

        - `TokenEndpointAuth TokenEndpointAuth`

          - `class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam`

            Updated HTTP Basic authentication parameters for the token endpoint.

            - `JsonElement Type = "client_secret_basic"`

            - `string? ClientSecret`

              A new OAuth client secret to replace the stored one.

              The credential must already use `client_secret_basic` or `client_secret_post`. It keeps its current `token_endpoint_auth` type, even if the `type` sent with this secret is the other one.

              minLength: 1, maxLength: 512

          - `class BetaManagedAgentsTokenEndpointAuthPostUpdateParam`

            Updated POST body authentication parameters for the token endpoint.

            - `JsonElement Type = "client_secret_post"`

            - `string? ClientSecret`

              A new OAuth client secret to replace the stored one.

              The credential must already use `client_secret_basic` or `client_secret_post`. It keeps its current `token_endpoint_auth` type, even if the `type` sent with this secret is the other one.

              minLength: 1, maxLength: 512

    - `class BetaManagedAgentsStaticBearerUpdateParams`

      Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

      - `JsonElement Type = "static_bearer"`

      - `string? Token`

        The new static bearer token to replace the stored one.

        minLength: 1, maxLength: 8192

    - `class BetaManagedAgentsEnvironmentVariableUpdateParams`

      Parameters for updating an environment variable credential. `secret_name` is immutable.

      - `JsonElement Type = "environment_variable"`

      - `BetaManagedAgentsInjectionLocationUpdateParams InjectionLocation`

        Updated injection location.

        - `bool Body`

          Substitute when the placeholder appears in the request body.

        - `bool Header`

          Substitute when the placeholder appears in a request header value.

      - `BetaManagedAgentsCredentialNetworkingParams? Networking`

        The new networking scope, which replaces the stored one as a whole.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingParams`

          Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

          - `JsonElement Type = "unrestricted"`

        - `class BetaManagedAgentsLimitedCredentialNetworkingParams`

          Substitute the secret only on requests to the listed hosts.

          - `JsonElement Type = "limited"`

          - `required IReadOnlyList<string> AllowedHosts`

            The destination hosts of the outbound requests that the credential's secret is substituted into.

            Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.` wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses aren't accepted. The list can have up to 16 entries.

      - `string? SecretValue`

        The new secret value to replace the stored one.

        minLength: 1, maxLength: 4096

  - `string? displayName`

    Updated human-readable name for the credential. 1-255 characters.

    minLength: 1, maxLength: 255

  - `IReadOnlyDictionary<string, string>? metadata`

    Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

  - `IReadOnlyList<AnthropicBeta> betas` (header parameter)

    This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

    - `Compact2026_09_04("compact-2026-09-04")`

    - `InlineTools2026_09_15("inline-tools-2026-09-15")`

    - `McpClient2026_09_15("mcp-client-2026-09-15")`

    - `CEPlugins2026_09_01("ce-plugins-2026-09-01")`

    - `SpendLimitReads2026_09_26("spend-limit-reads-2026-09-26")`

    - `TelemetryDestinations2026_08_11("telemetry-destinations-2026-08-11")`

    - `Webhooks2026_10_07("webhooks-2026-10-07")`

  - `string workspaceID` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsCredential`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `JsonElement Type = "vault_credential"`

  - `required string ID`

    The unique ID of the credential (`vcrd_...`).

  - `required DateTimeOffset? ArchivedAt`

    When the credential was archived. Null if not archived.

    format: date-time

  - `required Auth Auth`

    Authentication configuration for this credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse`

      OAuth credential details for an MCP server.

      - `JsonElement Type = "mcp_oauth"`

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `DateTimeOffset? ExpiresAt`

        When the credential's access token expires, in RFC 3339. Absent if the expiry isn't known.

        format: date-time

      - `BetaManagedAgentsMcpOAuthRefreshResponse? Refresh`

        Refresh token configuration, if the credential supports token refresh.

        - `required string ClientID`

          The OAuth client ID used when refreshing the access token.

        - `required string TokenEndpoint`

          Token endpoint URL used to refresh the access token.

        - `required TokenEndpointAuth TokenEndpointAuth`

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse`

            Token endpoint requires no client authentication.

            - `JsonElement Type = "none"`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `JsonElement Type = "client_secret_basic"`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse`

            Token endpoint uses POST body authentication with client credentials.

            - `JsonElement Type = "client_secret_post"`

        - `string? Resource`

          OAuth resource indicator.

        - `string? Scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse`

      Static bearer token credential details for an MCP server.

      - `JsonElement Type = "static_bearer"`

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse`

      Environment variable credential details. The secret value is never returned.

      - `JsonElement Type = "environment_variable"`

      - `required BetaManagedAgentsInjectionLocationResponse InjectionLocation`

        Where in the outbound request the secret value is substituted.

        - `required bool Body`

          Whether the placeholder is substituted in the request body.

        - `required bool Header`

          Whether the placeholder is substituted in request header values.

      - `required Networking Networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `JsonElement Type = "unrestricted"`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse`

          The secret is substituted only on requests to the listed hosts.

          - `JsonElement Type = "limited"`

          - `required IReadOnlyList<string> AllowedHosts`

            The destination hosts of the outbound requests that the credential's secret is substituted into.

            An entry matches the request host exactly. An entry such as `*.example.com` matches any subdomain of `example.com` but not `example.com` itself.

      - `required string SecretName`

        Name of the environment variable.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata attached to the credential.

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string VaultID`

    Identifier of the vault this credential belongs to.

  - `string? DisplayName`

    Human-readable name for the credential.

### Example

```csharp
using System;
using Anthropic.Models.Beta.Vaults.Credentials;

CredentialUpdateParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    CredentialID = "vcrd_011CZkZEMt8gZan2iYPQfSkw",
};

var betaManagedAgentsCredential = await client.Beta.Vaults.Credentials.Update(parameters);

Console.WriteLine(betaManagedAgentsCredential);
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

`BetaManagedAgentsDeletedCredential Beta.Vaults.Credentials.Delete(parameters, cancellationToken = default)`

**DELETE** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Delete a Credential

### Parameters

- `CredentialDeleteParams parameters`

  - `required string vaultID` (path parameter)

    Identifier of the vault containing the credential.

  - `required string credentialID` (path parameter)

    Unique identifier of the credential to delete.

  - `IReadOnlyList<AnthropicBeta> betas` (header parameter)

    This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

    - `Compact2026_09_04("compact-2026-09-04")`

    - `InlineTools2026_09_15("inline-tools-2026-09-15")`

    - `McpClient2026_09_15("mcp-client-2026-09-15")`

    - `CEPlugins2026_09_01("ce-plugins-2026-09-01")`

    - `SpendLimitReads2026_09_26("spend-limit-reads-2026-09-26")`

    - `TelemetryDestinations2026_08_11("telemetry-destinations-2026-08-11")`

    - `Webhooks2026_10_07("webhooks-2026-10-07")`

  - `string workspaceID` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsDeletedCredential`

  Confirmation of a deleted credential.

  - `JsonElement Type = "vault_credential_deleted"`

  - `required string ID`

    The unique ID of the deleted credential (`vcrd_...`).

### Example

```csharp
using System;
using Anthropic.Models.Beta.Vaults.Credentials;

CredentialDeleteParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    CredentialID = "vcrd_011CZkZEMt8gZan2iYPQfSkw",
};

var betaManagedAgentsDeletedCredential = await client.Beta.Vaults.Credentials.Delete(parameters);

Console.WriteLine(betaManagedAgentsDeletedCredential);
```

#### Response (200)

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYPQfSkw",
  "type": "vault_credential_deleted"
}
```

## Archive a Credential

`BetaManagedAgentsCredential Beta.Vaults.Credentials.Archive(parameters, cancellationToken = default)`

**POST** `/v1/vaults/{vault_id}/credentials/{credential_id}/archive`

Archive a Credential

### Parameters

- `CredentialArchiveParams parameters`

  - `required string vaultID` (path parameter)

    Identifier of the vault containing the credential.

  - `required string credentialID` (path parameter)

    Unique identifier of the credential to archive.

  - `IReadOnlyList<AnthropicBeta> betas` (header parameter)

    This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

    - `Compact2026_09_04("compact-2026-09-04")`

    - `InlineTools2026_09_15("inline-tools-2026-09-15")`

    - `McpClient2026_09_15("mcp-client-2026-09-15")`

    - `CEPlugins2026_09_01("ce-plugins-2026-09-01")`

    - `SpendLimitReads2026_09_26("spend-limit-reads-2026-09-26")`

    - `TelemetryDestinations2026_08_11("telemetry-destinations-2026-08-11")`

    - `Webhooks2026_10_07("webhooks-2026-10-07")`

  - `string workspaceID` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsCredential`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `JsonElement Type = "vault_credential"`

  - `required string ID`

    The unique ID of the credential (`vcrd_...`).

  - `required DateTimeOffset? ArchivedAt`

    When the credential was archived. Null if not archived.

    format: date-time

  - `required Auth Auth`

    Authentication configuration for this credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse`

      OAuth credential details for an MCP server.

      - `JsonElement Type = "mcp_oauth"`

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `DateTimeOffset? ExpiresAt`

        When the credential's access token expires, in RFC 3339. Absent if the expiry isn't known.

        format: date-time

      - `BetaManagedAgentsMcpOAuthRefreshResponse? Refresh`

        Refresh token configuration, if the credential supports token refresh.

        - `required string ClientID`

          The OAuth client ID used when refreshing the access token.

        - `required string TokenEndpoint`

          Token endpoint URL used to refresh the access token.

        - `required TokenEndpointAuth TokenEndpointAuth`

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse`

            Token endpoint requires no client authentication.

            - `JsonElement Type = "none"`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `JsonElement Type = "client_secret_basic"`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse`

            Token endpoint uses POST body authentication with client credentials.

            - `JsonElement Type = "client_secret_post"`

        - `string? Resource`

          OAuth resource indicator.

        - `string? Scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse`

      Static bearer token credential details for an MCP server.

      - `JsonElement Type = "static_bearer"`

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse`

      Environment variable credential details. The secret value is never returned.

      - `JsonElement Type = "environment_variable"`

      - `required BetaManagedAgentsInjectionLocationResponse InjectionLocation`

        Where in the outbound request the secret value is substituted.

        - `required bool Body`

          Whether the placeholder is substituted in the request body.

        - `required bool Header`

          Whether the placeholder is substituted in request header values.

      - `required Networking Networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `JsonElement Type = "unrestricted"`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse`

          The secret is substituted only on requests to the listed hosts.

          - `JsonElement Type = "limited"`

          - `required IReadOnlyList<string> AllowedHosts`

            The destination hosts of the outbound requests that the credential's secret is substituted into.

            An entry matches the request host exactly. An entry such as `*.example.com` matches any subdomain of `example.com` but not `example.com` itself.

      - `required string SecretName`

        Name of the environment variable.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata attached to the credential.

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string VaultID`

    Identifier of the vault this credential belongs to.

  - `string? DisplayName`

    Human-readable name for the credential.

### Example

```csharp
using System;
using Anthropic.Models.Beta.Vaults.Credentials;

CredentialArchiveParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    CredentialID = "vcrd_011CZkZEMt8gZan2iYPQfSkw",
};

var betaManagedAgentsCredential = await client.Beta.Vaults.Credentials.Archive(parameters);

Console.WriteLine(betaManagedAgentsCredential);
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

`BetaManagedAgentsCredentialValidation Beta.Vaults.Credentials.McpOAuthValidate(parameters, cancellationToken = default)`

**POST** `/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate`

Validate an MCP OAuth Credential

### Parameters

- `CredentialMcpOAuthValidateParams parameters`

  - `required string vaultID` (path parameter)

    Identifier of the vault containing the credential.

  - `required string credentialID` (path parameter)

    Unique identifier of the credential to validate.

  - `IReadOnlyList<AnthropicBeta> betas` (header parameter)

    This endpoint is in beta: requests must send `managed-agents-2026-04-01` in this header.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `UserProfiles2026_09_04("user-profiles-2026-09-04")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

    - `Compact2026_09_04("compact-2026-09-04")`

    - `InlineTools2026_09_15("inline-tools-2026-09-15")`

    - `McpClient2026_09_15("mcp-client-2026-09-15")`

    - `CEPlugins2026_09_01("ce-plugins-2026-09-01")`

    - `SpendLimitReads2026_09_26("spend-limit-reads-2026-09-26")`

    - `TelemetryDestinations2026_08_11("telemetry-destinations-2026-08-11")`

    - `Webhooks2026_10_07("webhooks-2026-10-07")`

  - `string workspaceID` (header parameter)

    Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

    Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

### Returns

- `class BetaManagedAgentsCredentialValidation`

  Result of live-probing a credential against its configured MCP server.

  - `JsonElement Type = "vault_credential_validation"`

  - `required string CredentialID`

    Unique identifier of the credential that was validated.

  - `required bool HasRefreshToken`

    Whether the credential has a refresh token configured.

  - `required BetaManagedAgentsMcpProbe? McpProbe`

    Details of the MCP probe step that failed, or `null` if the probe succeeded or there was no access token to test.

    - `required BetaManagedAgentsRefreshHttpResponse? HttpResponse`

      The HTTP error response from the MCP server, or `null` if the MCP server didn't return one for the failing step, for example after a timeout or a DNS or TLS failure.

      - `required string Body`

        Response body. May be truncated and has sensitive values scrubbed.

      - `required bool BodyTruncated`

        Whether `body` was truncated.

      - `required string ContentType`

        Value of the `Content-Type` response header.

      - `required int StatusCode`

        HTTP status code.

        format: int32

    - `required string Method`

      The MCP method that failed (for example `initialize` or `tools/list`).

  - `required BetaManagedAgentsRefreshObject? Refresh`

    Details of the refresh-token exchange attempted on a 401. Null when no refresh was attempted.

    - `required BetaManagedAgentsRefreshHttpResponse? HttpResponse`

      The captured HTTP error response from the token endpoint. Populated only when `status` is `failed`.

    - `required Status Status`

      Outcome of the refresh attempt.

      - `Succeeded("succeeded")`

        The token endpoint returned a new access token.

      - `Failed("failed")`

        The token endpoint returned an error response. See `http_response` for detail.

      - `ConnectError("connect_error")`

        The token endpoint could not be reached (DNS, TLS, or connection error).

      - `NoRefreshToken("no_refresh_token")`

        No refresh token is stored for the credential, so no exchange was attempted.

  - `required BetaManagedAgentsCredentialValidationStatus Status`

    Overall verdict of the validation probe.

    - `Valid("valid")`

      The credential successfully authenticated against its MCP server.

    - `Invalid("invalid")`

      The probe reached the MCP server and the server rejected the credential, or no access token is stored. A refresh, if one was tried, didn't recover it. Usually the end user needs to authorize again.

    - `Unknown("unknown")`

      The probe couldn't tell whether the credential works, for example because of a network error or because a refresh succeeded but the new access token wasn't tested. Validate the credential again to find out.

  - `required DateTimeOffset ValidatedAt`

    When the validation probe was performed.

    format: date-time

  - `required string VaultID`

    Identifier of the vault containing the credential.

### Example

```csharp
using System;
using Anthropic.Models.Beta.Vaults.Credentials;

CredentialMcpOAuthValidateParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    CredentialID = "vcrd_011CZkZEMt8gZan2iYPQfSkw",
};

var betaManagedAgentsCredentialValidation = await client.Beta.Vaults.Credentials.McpOAuthValidate(parameters);

Console.WriteLine(betaManagedAgentsCredentialValidation);
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

- `class BetaManagedAgentsCredential`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `JsonElement Type = "vault_credential"`

  - `required string ID`

    The unique ID of the credential (`vcrd_...`).

  - `required DateTimeOffset? ArchivedAt`

    When the credential was archived. Null if not archived.

    format: date-time

  - `required Auth Auth`

    Authentication configuration for this credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse`

      OAuth credential details for an MCP server.

      - `JsonElement Type = "mcp_oauth"`

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `DateTimeOffset? ExpiresAt`

        When the credential's access token expires, in RFC 3339. Absent if the expiry isn't known.

        format: date-time

      - `BetaManagedAgentsMcpOAuthRefreshResponse? Refresh`

        Refresh token configuration, if the credential supports token refresh.

        - `required string ClientID`

          The OAuth client ID used when refreshing the access token.

        - `required string TokenEndpoint`

          Token endpoint URL used to refresh the access token.

        - `required TokenEndpointAuth TokenEndpointAuth`

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse`

            Token endpoint requires no client authentication.

            - `JsonElement Type = "none"`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `JsonElement Type = "client_secret_basic"`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse`

            Token endpoint uses POST body authentication with client credentials.

            - `JsonElement Type = "client_secret_post"`

        - `string? Resource`

          OAuth resource indicator.

        - `string? Scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse`

      Static bearer token credential details for an MCP server.

      - `JsonElement Type = "static_bearer"`

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse`

      Environment variable credential details. The secret value is never returned.

      - `JsonElement Type = "environment_variable"`

      - `required BetaManagedAgentsInjectionLocationResponse InjectionLocation`

        Where in the outbound request the secret value is substituted.

        - `required bool Body`

          Whether the placeholder is substituted in the request body.

        - `required bool Header`

          Whether the placeholder is substituted in request header values.

      - `required Networking Networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `JsonElement Type = "unrestricted"`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse`

          The secret is substituted only on requests to the listed hosts.

          - `JsonElement Type = "limited"`

          - `required IReadOnlyList<string> AllowedHosts`

            The destination hosts of the outbound requests that the credential's secret is substituted into.

            An entry matches the request host exactly. An entry such as `*.example.com` matches any subdomain of `example.com` but not `example.com` itself.

      - `required string SecretName`

        Name of the environment variable.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata attached to the credential.

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string VaultID`

    Identifier of the vault this credential belongs to.

  - `string? DisplayName`

    Human-readable name for the credential.

### Beta Managed Agents Credential Networking Params

- `class BetaManagedAgentsCredentialNetworkingParams: union`

  - `class BetaManagedAgentsUnrestrictedCredentialNetworkingParams`

    Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

    - `JsonElement Type = "unrestricted"`

  - `class BetaManagedAgentsLimitedCredentialNetworkingParams`

    Substitute the secret only on requests to the listed hosts.

    - `JsonElement Type = "limited"`

    - `required IReadOnlyList<string> AllowedHosts`

      The destination hosts of the outbound requests that the credential's secret is substituted into.

      Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.` wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses aren't accepted. The list can have up to 16 entries.

### Beta Managed Agents Credential Validation

- `class BetaManagedAgentsCredentialValidation`

  Result of live-probing a credential against its configured MCP server.

  - `JsonElement Type = "vault_credential_validation"`

  - `required string CredentialID`

    Unique identifier of the credential that was validated.

  - `required bool HasRefreshToken`

    Whether the credential has a refresh token configured.

  - `required BetaManagedAgentsMcpProbe? McpProbe`

    Details of the MCP probe step that failed, or `null` if the probe succeeded or there was no access token to test.

    - `required BetaManagedAgentsRefreshHttpResponse? HttpResponse`

      The HTTP error response from the MCP server, or `null` if the MCP server didn't return one for the failing step, for example after a timeout or a DNS or TLS failure.

      - `required string Body`

        Response body. May be truncated and has sensitive values scrubbed.

      - `required bool BodyTruncated`

        Whether `body` was truncated.

      - `required string ContentType`

        Value of the `Content-Type` response header.

      - `required int StatusCode`

        HTTP status code.

        format: int32

    - `required string Method`

      The MCP method that failed (for example `initialize` or `tools/list`).

  - `required BetaManagedAgentsRefreshObject? Refresh`

    Details of the refresh-token exchange attempted on a 401. Null when no refresh was attempted.

    - `required BetaManagedAgentsRefreshHttpResponse? HttpResponse`

      The captured HTTP error response from the token endpoint. Populated only when `status` is `failed`.

    - `required Status Status`

      Outcome of the refresh attempt.

      - `Succeeded("succeeded")`

        The token endpoint returned a new access token.

      - `Failed("failed")`

        The token endpoint returned an error response. See `http_response` for detail.

      - `ConnectError("connect_error")`

        The token endpoint could not be reached (DNS, TLS, or connection error).

      - `NoRefreshToken("no_refresh_token")`

        No refresh token is stored for the credential, so no exchange was attempted.

  - `required BetaManagedAgentsCredentialValidationStatus Status`

    Overall verdict of the validation probe.

    - `Valid("valid")`

      The credential successfully authenticated against its MCP server.

    - `Invalid("invalid")`

      The probe reached the MCP server and the server rejected the credential, or no access token is stored. A refresh, if one was tried, didn't recover it. Usually the end user needs to authorize again.

    - `Unknown("unknown")`

      The probe couldn't tell whether the credential works, for example because of a network error or because a refresh succeeded but the new access token wasn't tested. Validate the credential again to find out.

  - `required DateTimeOffset ValidatedAt`

    When the validation probe was performed.

    format: date-time

  - `required string VaultID`

    Identifier of the vault containing the credential.

### Beta Managed Agents Credential Validation Status

- `enum BetaManagedAgentsCredentialValidationStatus`

  Overall verdict of a credential validation probe.

  - `Valid("valid")`

    The credential successfully authenticated against its MCP server.

  - `Invalid("invalid")`

    The probe reached the MCP server and the server rejected the credential, or no access token is stored. A refresh, if one was tried, didn't recover it. Usually the end user needs to authorize again.

  - `Unknown("unknown")`

    The probe couldn't tell whether the credential works, for example because of a network error or because a refresh succeeded but the new access token wasn't tested. Validate the credential again to find out.

### Beta Managed Agents Deleted Credential

- `class BetaManagedAgentsDeletedCredential`

  Confirmation of a deleted credential.

  - `JsonElement Type = "vault_credential_deleted"`

  - `required string ID`

    The unique ID of the deleted credential (`vcrd_...`).

### Beta Managed Agents Environment Variable Auth Response

- `class BetaManagedAgentsEnvironmentVariableAuthResponse`

  Environment variable credential details. The secret value is never returned.

  - `JsonElement Type = "environment_variable"`

  - `required BetaManagedAgentsInjectionLocationResponse InjectionLocation`

    Where in the outbound request the secret value is substituted.

    - `required bool Body`

      Whether the placeholder is substituted in the request body.

    - `required bool Header`

      Whether the placeholder is substituted in request header values.

  - `required Networking Networking`

    Outbound hosts the secret value is substituted on.

    - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse`

      The secret is substituted on any host the session's Environment network policy permits egress to.

      - `JsonElement Type = "unrestricted"`

    - `class BetaManagedAgentsLimitedCredentialNetworkingResponse`

      The secret is substituted only on requests to the listed hosts.

      - `JsonElement Type = "limited"`

      - `required IReadOnlyList<string> AllowedHosts`

        The destination hosts of the outbound requests that the credential's secret is substituted into.

        An entry matches the request host exactly. An entry such as `*.example.com` matches any subdomain of `example.com` but not `example.com` itself.

  - `required string SecretName`

    Name of the environment variable.

### Beta Managed Agents Environment Variable Create Params

- `class BetaManagedAgentsEnvironmentVariableCreateParams`

  Parameters for creating an environment variable credential.

  - `JsonElement Type = "environment_variable"`

  - `required BetaManagedAgentsCredentialNetworkingParams Networking`

    Outbound hosts the secret value is substituted on.

    - `class BetaManagedAgentsUnrestrictedCredentialNetworkingParams`

      Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

      - `JsonElement Type = "unrestricted"`

    - `class BetaManagedAgentsLimitedCredentialNetworkingParams`

      Substitute the secret only on requests to the listed hosts.

      - `JsonElement Type = "limited"`

      - `required IReadOnlyList<string> AllowedHosts`

        The destination hosts of the outbound requests that the credential's secret is substituted into.

        Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.` wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses aren't accepted. The list can have up to 16 entries.

  - `required string SecretName`

    Name of the environment variable. Immutable after create.

    minLength: 1, maxLength: 255

  - `required string SecretValue`

    The secret to substitute into the agent's outbound requests. It's write-only and never returned in responses.

    minLength: 1, maxLength: 4096

  - `BetaManagedAgentsInjectionLocationParams InjectionLocation`

    Where in the outbound request the secret value may be substituted.

    - `bool Body`

      Substitute when the placeholder appears in the request body.

    - `bool Header`

      Substitute when the placeholder appears in a request header value.

### Beta Managed Agents Environment Variable Update Params

- `class BetaManagedAgentsEnvironmentVariableUpdateParams`

  Parameters for updating an environment variable credential. `secret_name` is immutable.

  - `JsonElement Type = "environment_variable"`

  - `BetaManagedAgentsInjectionLocationUpdateParams InjectionLocation`

    Updated injection location.

    - `bool Body`

      Substitute when the placeholder appears in the request body.

    - `bool Header`

      Substitute when the placeholder appears in a request header value.

  - `BetaManagedAgentsCredentialNetworkingParams? Networking`

    The new networking scope, which replaces the stored one as a whole.

    - `class BetaManagedAgentsUnrestrictedCredentialNetworkingParams`

      Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

      - `JsonElement Type = "unrestricted"`

    - `class BetaManagedAgentsLimitedCredentialNetworkingParams`

      Substitute the secret only on requests to the listed hosts.

      - `JsonElement Type = "limited"`

      - `required IReadOnlyList<string> AllowedHosts`

        The destination hosts of the outbound requests that the credential's secret is substituted into.

        Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.` wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses aren't accepted. The list can have up to 16 entries.

  - `string? SecretValue`

    The new secret value to replace the stored one.

    minLength: 1, maxLength: 4096

### Beta Managed Agents Injection Location Params

- `class BetaManagedAgentsInjectionLocationParams`

  Where in the outbound request the secret value may be substituted.

  - `bool Body`

    Substitute when the placeholder appears in the request body.

  - `bool Header`

    Substitute when the placeholder appears in a request header value.

### Beta Managed Agents Injection Location Response

- `class BetaManagedAgentsInjectionLocationResponse`

  Where in the outbound request the secret value is substituted.

  - `required bool Body`

    Whether the placeholder is substituted in the request body.

  - `required bool Header`

    Whether the placeholder is substituted in request header values.

### Beta Managed Agents Injection Location Update Params

- `class BetaManagedAgentsInjectionLocationUpdateParams`

  Changes which parts of an outbound request the secret is substituted into. A location you leave out keeps its current setting.

  After the change, at least one location must be enabled.

  See [Authenticate with vaults](https://platform.claude.com/docs/en/managed-agents/vaults?sdk_languages=csharp#add-a-credential) to learn more about injection locations.

  - `bool Body`

    Substitute when the placeholder appears in the request body.

  - `bool Header`

    Substitute when the placeholder appears in a request header value.

### Beta Managed Agents Limited Credential Networking Params

- `class BetaManagedAgentsLimitedCredentialNetworkingParams`

  Substitute the secret only on requests to the listed hosts.

  - `JsonElement Type = "limited"`

  - `required IReadOnlyList<string> AllowedHosts`

    The destination hosts of the outbound requests that the credential's secret is substituted into.

    Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.` wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses aren't accepted. The list can have up to 16 entries.

### Beta Managed Agents Limited Credential Networking Response

- `class BetaManagedAgentsLimitedCredentialNetworkingResponse`

  The secret is substituted only on requests to the listed hosts.

  - `JsonElement Type = "limited"`

  - `required IReadOnlyList<string> AllowedHosts`

    The destination hosts of the outbound requests that the credential's secret is substituted into.

    An entry matches the request host exactly. An entry such as `*.example.com` matches any subdomain of `example.com` but not `example.com` itself.

### Beta Managed Agents MCP OAuth Auth Response

- `class BetaManagedAgentsMcpOAuthAuthResponse`

  OAuth credential details for an MCP server.

  - `JsonElement Type = "mcp_oauth"`

  - `required string McpServerUrl`

    URL of the MCP server this credential authenticates against.

  - `DateTimeOffset? ExpiresAt`

    When the credential's access token expires, in RFC 3339. Absent if the expiry isn't known.

    format: date-time

  - `BetaManagedAgentsMcpOAuthRefreshResponse? Refresh`

    Refresh token configuration, if the credential supports token refresh.

    - `required string ClientID`

      The OAuth client ID used when refreshing the access token.

    - `required string TokenEndpoint`

      Token endpoint URL used to refresh the access token.

    - `required TokenEndpointAuth TokenEndpointAuth`

      - `class BetaManagedAgentsTokenEndpointAuthNoneResponse`

        Token endpoint requires no client authentication.

        - `JsonElement Type = "none"`

      - `class BetaManagedAgentsTokenEndpointAuthBasicResponse`

        Token endpoint uses HTTP Basic authentication with client credentials.

        - `JsonElement Type = "client_secret_basic"`

      - `class BetaManagedAgentsTokenEndpointAuthPostResponse`

        Token endpoint uses POST body authentication with client credentials.

        - `JsonElement Type = "client_secret_post"`

    - `string? Resource`

      OAuth resource indicator.

    - `string? Scope`

      OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Create Params

- `class BetaManagedAgentsMcpOAuthCreateParams`

  Parameters for creating an MCP OAuth credential.

  - `JsonElement Type = "mcp_oauth"`

  - `required string AccessToken`

    The OAuth access token to send to the MCP server.

    minLength: 1, maxLength: 8192

  - `required string McpServerUrl`

    URL of the MCP server this credential authenticates against.

    minLength: 1, maxLength: 2047

  - `DateTimeOffset? ExpiresAt`

    When `access_token` expires, in RFC 3339.

    Must be in the future.

    format: date-time

  - `BetaManagedAgentsMcpOAuthRefreshParams? Refresh`

    Refresh token configuration, if the credential supports token refresh.

    - `required string ClientID`

      The OAuth client ID to use when refreshing the access token. It can't be changed after the credential is created.

      minLength: 1, maxLength: 1024

    - `required string RefreshToken`

      The OAuth refresh token that the API uses to get a new access token when the current one expires.

      minLength: 1, maxLength: 8192

    - `required string TokenEndpoint`

      Token endpoint URL used to refresh the access token.

      minLength: 1, maxLength: 2047

    - `required TokenEndpointAuth TokenEndpointAuth`

      - `class BetaManagedAgentsTokenEndpointAuthNoneParam`

        Token endpoint requires no client authentication.

        - `JsonElement Type = "none"`

      - `class BetaManagedAgentsTokenEndpointAuthBasicParam`

        Token endpoint uses HTTP Basic authentication with client credentials.

        - `JsonElement Type = "client_secret_basic"`

        - `required string ClientSecret`

          The OAuth client secret, sent to `token_endpoint` with HTTP Basic authentication.

          minLength: 1, maxLength: 512

      - `class BetaManagedAgentsTokenEndpointAuthPostParam`

        Token endpoint uses POST body authentication with client credentials.

        - `JsonElement Type = "client_secret_post"`

        - `required string ClientSecret`

          The OAuth client secret, sent to `token_endpoint` in the POST body.

          minLength: 1, maxLength: 512

    - `string? Resource`

      OAuth resource indicator.

      minLength: 1, maxLength: 2047

    - `string? Scope`

      OAuth scope for the refresh request.

      minLength: 1, maxLength: 8192

### Beta Managed Agents MCP OAuth Refresh Params

- `class BetaManagedAgentsMcpOAuthRefreshParams`

  OAuth refresh token parameters for creating a credential with refresh support.

  - `required string ClientID`

    The OAuth client ID to use when refreshing the access token. It can't be changed after the credential is created.

    minLength: 1, maxLength: 1024

  - `required string RefreshToken`

    The OAuth refresh token that the API uses to get a new access token when the current one expires.

    minLength: 1, maxLength: 8192

  - `required string TokenEndpoint`

    Token endpoint URL used to refresh the access token.

    minLength: 1, maxLength: 2047

  - `required TokenEndpointAuth TokenEndpointAuth`

    - `class BetaManagedAgentsTokenEndpointAuthNoneParam`

      Token endpoint requires no client authentication.

      - `JsonElement Type = "none"`

    - `class BetaManagedAgentsTokenEndpointAuthBasicParam`

      Token endpoint uses HTTP Basic authentication with client credentials.

      - `JsonElement Type = "client_secret_basic"`

      - `required string ClientSecret`

        The OAuth client secret, sent to `token_endpoint` with HTTP Basic authentication.

        minLength: 1, maxLength: 512

    - `class BetaManagedAgentsTokenEndpointAuthPostParam`

      Token endpoint uses POST body authentication with client credentials.

      - `JsonElement Type = "client_secret_post"`

      - `required string ClientSecret`

        The OAuth client secret, sent to `token_endpoint` in the POST body.

        minLength: 1, maxLength: 512

  - `string? Resource`

    OAuth resource indicator.

    minLength: 1, maxLength: 2047

  - `string? Scope`

    OAuth scope for the refresh request.

    minLength: 1, maxLength: 8192

### Beta Managed Agents MCP OAuth Refresh Response

- `class BetaManagedAgentsMcpOAuthRefreshResponse`

  OAuth refresh token configuration returned in credential responses.

  - `required string ClientID`

    The OAuth client ID used when refreshing the access token.

  - `required string TokenEndpoint`

    Token endpoint URL used to refresh the access token.

  - `required TokenEndpointAuth TokenEndpointAuth`

    - `class BetaManagedAgentsTokenEndpointAuthNoneResponse`

      Token endpoint requires no client authentication.

      - `JsonElement Type = "none"`

    - `class BetaManagedAgentsTokenEndpointAuthBasicResponse`

      Token endpoint uses HTTP Basic authentication with client credentials.

      - `JsonElement Type = "client_secret_basic"`

    - `class BetaManagedAgentsTokenEndpointAuthPostResponse`

      Token endpoint uses POST body authentication with client credentials.

      - `JsonElement Type = "client_secret_post"`

  - `string? Resource`

    OAuth resource indicator.

  - `string? Scope`

    OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Update Params

- `class BetaManagedAgentsMcpOAuthRefreshUpdateParams`

  Parameters for updating OAuth refresh token configuration.

  - `string? RefreshToken`

    The new OAuth refresh token to replace the stored one.

    minLength: 1, maxLength: 8192

  - `string? Scope`

    The new OAuth scope for refresh requests. Send an empty string to clear the stored scope.

    maxLength: 8192

  - `TokenEndpointAuth TokenEndpointAuth`

    - `class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam`

      Updated HTTP Basic authentication parameters for the token endpoint.

      - `JsonElement Type = "client_secret_basic"`

      - `string? ClientSecret`

        A new OAuth client secret to replace the stored one.

        The credential must already use `client_secret_basic` or `client_secret_post`. It keeps its current `token_endpoint_auth` type, even if the `type` sent with this secret is the other one.

        minLength: 1, maxLength: 512

    - `class BetaManagedAgentsTokenEndpointAuthPostUpdateParam`

      Updated POST body authentication parameters for the token endpoint.

      - `JsonElement Type = "client_secret_post"`

      - `string? ClientSecret`

        A new OAuth client secret to replace the stored one.

        The credential must already use `client_secret_basic` or `client_secret_post`. It keeps its current `token_endpoint_auth` type, even if the `type` sent with this secret is the other one.

        minLength: 1, maxLength: 512

### Beta Managed Agents MCP OAuth Update Params

- `class BetaManagedAgentsMcpOAuthUpdateParams`

  Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

  - `JsonElement Type = "mcp_oauth"`

  - `string? AccessToken`

    The new OAuth access token to replace the stored one.

    minLength: 1, maxLength: 8192

  - `DateTimeOffset? ExpiresAt`

    When the credential's access token expires, in RFC 3339. Leave it out to keep the stored expiry.

    If you send a new `access_token`, send its `expires_at` too, or the new token keeps the old expiry.

    Must be in the future.

    format: date-time

  - `BetaManagedAgentsMcpOAuthRefreshUpdateParams? Refresh`

    Updated refresh token configuration.

    - `string? RefreshToken`

      The new OAuth refresh token to replace the stored one.

      minLength: 1, maxLength: 8192

    - `string? Scope`

      The new OAuth scope for refresh requests. Send an empty string to clear the stored scope.

      maxLength: 8192

    - `TokenEndpointAuth TokenEndpointAuth`

      - `class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam`

        Updated HTTP Basic authentication parameters for the token endpoint.

        - `JsonElement Type = "client_secret_basic"`

        - `string? ClientSecret`

          A new OAuth client secret to replace the stored one.

          The credential must already use `client_secret_basic` or `client_secret_post`. It keeps its current `token_endpoint_auth` type, even if the `type` sent with this secret is the other one.

          minLength: 1, maxLength: 512

      - `class BetaManagedAgentsTokenEndpointAuthPostUpdateParam`

        Updated POST body authentication parameters for the token endpoint.

        - `JsonElement Type = "client_secret_post"`

        - `string? ClientSecret`

          A new OAuth client secret to replace the stored one.

          The credential must already use `client_secret_basic` or `client_secret_post`. It keeps its current `token_endpoint_auth` type, even if the `type` sent with this secret is the other one.

          minLength: 1, maxLength: 512

### Beta Managed Agents MCP Probe

- `class BetaManagedAgentsMcpProbe`

  The failing step of an MCP validation probe.

  - `required BetaManagedAgentsRefreshHttpResponse? HttpResponse`

    The HTTP error response from the MCP server, or `null` if the MCP server didn't return one for the failing step, for example after a timeout or a DNS or TLS failure.

    - `required string Body`

      Response body. May be truncated and has sensitive values scrubbed.

    - `required bool BodyTruncated`

      Whether `body` was truncated.

    - `required string ContentType`

      Value of the `Content-Type` response header.

    - `required int StatusCode`

      HTTP status code.

      format: int32

  - `required string Method`

    The MCP method that failed (for example `initialize` or `tools/list`).

### Beta Managed Agents Refresh HTTP Response

- `class BetaManagedAgentsRefreshHttpResponse`

  An HTTP response captured during a credential validation probe.

  - `required string Body`

    Response body. May be truncated and has sensitive values scrubbed.

  - `required bool BodyTruncated`

    Whether `body` was truncated.

  - `required string ContentType`

    Value of the `Content-Type` response header.

  - `required int StatusCode`

    HTTP status code.

    format: int32

### Beta Managed Agents Refresh Object

- `class BetaManagedAgentsRefreshObject`

  Outcome of a refresh-token exchange attempted during credential validation.

  - `required BetaManagedAgentsRefreshHttpResponse? HttpResponse`

    The captured HTTP error response from the token endpoint. Populated only when `status` is `failed`.

    - `required string Body`

      Response body. May be truncated and has sensitive values scrubbed.

    - `required bool BodyTruncated`

      Whether `body` was truncated.

    - `required string ContentType`

      Value of the `Content-Type` response header.

    - `required int StatusCode`

      HTTP status code.

      format: int32

  - `required Status Status`

    Outcome of the refresh attempt.

    - `Succeeded("succeeded")`

      The token endpoint returned a new access token.

    - `Failed("failed")`

      The token endpoint returned an error response. See `http_response` for detail.

    - `ConnectError("connect_error")`

      The token endpoint could not be reached (DNS, TLS, or connection error).

    - `NoRefreshToken("no_refresh_token")`

      No refresh token is stored for the credential, so no exchange was attempted.

### Beta Managed Agents Static Bearer Auth Response

- `class BetaManagedAgentsStaticBearerAuthResponse`

  Static bearer token credential details for an MCP server.

  - `JsonElement Type = "static_bearer"`

  - `required string McpServerUrl`

    URL of the MCP server this credential authenticates against.

### Beta Managed Agents Static Bearer Create Params

- `class BetaManagedAgentsStaticBearerCreateParams`

  Parameters for creating a static bearer token credential.

  - `JsonElement Type = "static_bearer"`

  - `required string Token`

    The static bearer token to send to the MCP server, such as an API key or personal access token.

    minLength: 1, maxLength: 8192

  - `required string McpServerUrl`

    URL of the MCP server this credential authenticates against.

    minLength: 1, maxLength: 2047

### Beta Managed Agents Static Bearer Update Params

- `class BetaManagedAgentsStaticBearerUpdateParams`

  Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

  - `JsonElement Type = "static_bearer"`

  - `string? Token`

    The new static bearer token to replace the stored one.

    minLength: 1, maxLength: 8192

### Beta Managed Agents Token Endpoint Auth Basic Param

- `class BetaManagedAgentsTokenEndpointAuthBasicParam`

  Token endpoint uses HTTP Basic authentication with client credentials.

  - `JsonElement Type = "client_secret_basic"`

  - `required string ClientSecret`

    The OAuth client secret, sent to `token_endpoint` with HTTP Basic authentication.

    minLength: 1, maxLength: 512

### Beta Managed Agents Token Endpoint Auth Basic Response

- `class BetaManagedAgentsTokenEndpointAuthBasicResponse`

  Token endpoint uses HTTP Basic authentication with client credentials.

  - `JsonElement Type = "client_secret_basic"`

### Beta Managed Agents Token Endpoint Auth Basic Update Param

- `class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam`

  Updated HTTP Basic authentication parameters for the token endpoint.

  - `JsonElement Type = "client_secret_basic"`

  - `string? ClientSecret`

    A new OAuth client secret to replace the stored one.

    The credential must already use `client_secret_basic` or `client_secret_post`. It keeps its current `token_endpoint_auth` type, even if the `type` sent with this secret is the other one.

    minLength: 1, maxLength: 512

### Beta Managed Agents Token Endpoint Auth None Param

- `class BetaManagedAgentsTokenEndpointAuthNoneParam`

  Token endpoint requires no client authentication.

  - `JsonElement Type = "none"`

### Beta Managed Agents Token Endpoint Auth None Response

- `class BetaManagedAgentsTokenEndpointAuthNoneResponse`

  Token endpoint requires no client authentication.

  - `JsonElement Type = "none"`

### Beta Managed Agents Token Endpoint Auth Post Param

- `class BetaManagedAgentsTokenEndpointAuthPostParam`

  Token endpoint uses POST body authentication with client credentials.

  - `JsonElement Type = "client_secret_post"`

  - `required string ClientSecret`

    The OAuth client secret, sent to `token_endpoint` in the POST body.

    minLength: 1, maxLength: 512

### Beta Managed Agents Token Endpoint Auth Post Response

- `class BetaManagedAgentsTokenEndpointAuthPostResponse`

  Token endpoint uses POST body authentication with client credentials.

  - `JsonElement Type = "client_secret_post"`

### Beta Managed Agents Token Endpoint Auth Post Update Param

- `class BetaManagedAgentsTokenEndpointAuthPostUpdateParam`

  Updated POST body authentication parameters for the token endpoint.

  - `JsonElement Type = "client_secret_post"`

  - `string? ClientSecret`

    A new OAuth client secret to replace the stored one.

    The credential must already use `client_secret_basic` or `client_secret_post`. It keeps its current `token_endpoint_auth` type, even if the `type` sent with this secret is the other one.

    minLength: 1, maxLength: 512

### Beta Managed Agents Unrestricted Credential Networking Params

- `class BetaManagedAgentsUnrestrictedCredentialNetworkingParams`

  Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

  - `JsonElement Type = "unrestricted"`

### Beta Managed Agents Unrestricted Credential Networking Response

- `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse`

  The secret is substituted on any host the session's Environment network policy permits egress to.

  - `JsonElement Type = "unrestricted"`
