# List Credentials

`CredentialListPageResponse Beta.Vaults.Credentials.List(parameters, cancellationToken = default)`

**GET** `/v1/vaults/{vault_id}/credentials`

List Credentials

## Parameters

- `CredentialListParams parameters`

  - `required string vaultID`

    Path param: Path parameter vault_id

  - `bool includeArchived`

    Query param: Whether to include archived credentials in the results.

  - `int limit`

    Query param: Maximum number of credentials to return per page. Defaults to 20, maximum 100.

    format: int32

  - `string page`

    Query param: Opaque pagination token from a previous `list_credentials` response.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

## Returns

- `class CredentialListPageResponse:`

  Response containing a paginated list of credentials.

  - `IReadOnlyList<BetaManagedAgentsCredential> Data`

    List of credentials.

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

  - `string? NextPage`

    Pagination token for the next page, or null if no more results.

## Example

```csharp
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
