# Create Credential

`BetaManagedAgentsCredential Beta.Vaults.Credentials.Create(parameters, cancellationToken = default)`

**POST** `/v1/vaults/{vault_id}/credentials`

Create Credential

## Parameters

- `CredentialCreateParams parameters`

  - `required string vaultID`

    Path param: Path parameter vault_id

  - `required Auth auth`

    Body param: Authentication details for creating a credential.

    - `class BetaManagedAgentsMcpOAuthCreateParams:`

      Parameters for creating an MCP OAuth credential.

      - `required string AccessToken`

        OAuth access token.

        minLength: 1, maxLength: 8192

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

        minLength: 1, maxLength: 2047

      - `required Type Type`

      - `DateTimeOffset? ExpiresAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `BetaManagedAgentsMcpOAuthRefreshParams? Refresh`

        OAuth refresh token parameters for creating a credential with refresh support.

        - `required string ClientID`

          OAuth client ID.

          minLength: 1, maxLength: 1024

        - `required string RefreshToken`

          OAuth refresh token.

          minLength: 1, maxLength: 4096

        - `required string TokenEndpoint`

          Token endpoint URL used to refresh the access token.

          minLength: 1, maxLength: 2047

        - `required TokenEndpointAuth TokenEndpointAuth`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneParam:`

            Token endpoint requires no client authentication.

            - `required Type Type`

          - `class BetaManagedAgentsTokenEndpointAuthBasicParam:`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `required string ClientSecret`

              OAuth client secret.

              minLength: 1, maxLength: 512

            - `required Type Type`

          - `class BetaManagedAgentsTokenEndpointAuthPostParam:`

            Token endpoint uses POST body authentication with client credentials.

            - `required string ClientSecret`

              OAuth client secret.

              minLength: 1, maxLength: 512

            - `required Type Type`

        - `string? Resource`

          OAuth resource indicator.

          minLength: 1, maxLength: 2047

        - `string? Scope`

          OAuth scope for the refresh request.

          minLength: 1, maxLength: 8192

    - `class BetaManagedAgentsStaticBearerCreateParams:`

      Parameters for creating a static bearer token credential.

      - `required string Token`

        Static bearer token value.

        minLength: 1, maxLength: 8192

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

        minLength: 1, maxLength: 2047

      - `required Type Type`

    - `class BetaManagedAgentsEnvironmentVariableCreateParams:`

      Parameters for creating an environment variable credential.

      - `required BetaManagedAgentsCredentialNetworkingParams Networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingParams:`

          Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

          - `required Type Type`

        - `class BetaManagedAgentsLimitedCredentialNetworkingParams:`

          Substitute the secret only on requests to the listed hosts.

          - `required IReadOnlyList<string> AllowedHosts`

            Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

          - `required Type Type`

      - `required string SecretName`

        Name of the environment variable. Immutable after create.

        minLength: 1, maxLength: 255

      - `required string SecretValue`

        Secret value. Write-only; never returned in responses.

        minLength: 1, maxLength: 4096

      - `required Type Type`

      - `BetaManagedAgentsInjectionLocationParams InjectionLocation`

        Where in the outbound request the secret value may be substituted.

        - `bool Body`

          Substitute when the placeholder appears in the request body.

        - `bool Header`

          Substitute when the placeholder appears in a request header value.

  - `string? displayName`

    Body param: Human-readable name for the credential. Up to 255 characters.

    maxLength: 255

  - `IReadOnlyDictionary<string, string> metadata`

    Body param: Arbitrary key-value metadata to attach to the credential. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

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

## Returns

- `class BetaManagedAgentsCredential:`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `required string ID`

    Unique identifier for the credential.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required Auth Auth`

    Authentication details for a credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse:`

      OAuth credential details for an MCP server.

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `required Type Type`

      - `DateTimeOffset? ExpiresAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `BetaManagedAgentsMcpOAuthRefreshResponse? Refresh`

        OAuth refresh token configuration returned in credential responses.

        - `required string ClientID`

          OAuth client ID.

        - `required string TokenEndpoint`

          Token endpoint URL used to refresh the access token.

        - `required TokenEndpointAuth TokenEndpointAuth`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse:`

            Token endpoint requires no client authentication.

            - `required Type Type`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `required Type Type`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

            Token endpoint uses POST body authentication with client credentials.

            - `required Type Type`

        - `string? Resource`

          OAuth resource indicator.

        - `string? Scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse:`

      Static bearer token credential details for an MCP server.

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `required Type Type`

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse:`

      Environment variable credential details. The secret value is never returned.

      - `required BetaManagedAgentsInjectionLocationResponse InjectionLocation`

        Where in the outbound request the secret value is substituted.

        - `required bool Body`

          Whether the placeholder is substituted in the request body.

        - `required bool Header`

          Whether the placeholder is substituted in request header values.

      - `required Networking Networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse:`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `required Type Type`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse:`

          The secret is substituted only on requests to the listed hosts.

          - `required IReadOnlyList<string> AllowedHosts`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `required Type Type`

      - `required string SecretName`

        Name of the environment variable.

      - `required Type Type`

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata attached to the credential.

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string VaultID`

    Identifier of the vault this credential belongs to.

  - `string? DisplayName`

    Human-readable name for the credential.

## Example

```csharp
CredentialCreateParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    Auth = new BetaManagedAgentsStaticBearerCreateParams()
    {
        Token = "bearer_exampletoken",
        McpServerUrl = "https://example-server.modelcontextprotocol.io/sse",
        Type = Type.StaticBearer,
    },
};

var betaManagedAgentsCredential = await client.Beta.Vaults.Credentials.Create(parameters);

Console.WriteLine(betaManagedAgentsCredential);
```

### Response (200)

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
