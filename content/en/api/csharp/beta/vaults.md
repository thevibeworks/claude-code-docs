# Vaults

## Create Vault

`BetaManagedAgentsVault Beta.Vaults.Create(parameters, cancellationToken = default)`

**POST** `/v1/vaults`

Create Vault

### Parameters

- `VaultCreateParams parameters`

  - `required string displayName`

    Body param: Human-readable name for the vault. 1-255 characters.

    minLength: 1, maxLength: 255

  - `IReadOnlyDictionary<string, string> metadata`

    Body param: Arbitrary key-value metadata to attach to the vault. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

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

### Returns

- `class BetaManagedAgentsVault:`

  A vault that stores credentials for use by agents during sessions.

  - `required string ID`

    Unique identifier for the vault.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string DisplayName`

    Human-readable name for the vault.

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata attached to the vault.

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

### Example

```csharp
VaultCreateParams parameters = new() { DisplayName = "Example vault" };

var betaManagedAgentsVault = await client.Beta.Vaults.Create(parameters);

Console.WriteLine(betaManagedAgentsVault);
```

#### Response (200)

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "display_name": "Example vault",
  "metadata": {
    "environment": "production"
  },
  "type": "vault",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

## List Vaults

`VaultListPageResponse Beta.Vaults.List(parameters, cancellationToken = default)`

**GET** `/v1/vaults`

List Vaults

### Parameters

- `VaultListParams parameters`

  - `bool includeArchived`

    Query param: Whether to include archived vaults in the results.

  - `int limit`

    Query param: Maximum number of vaults to return per page. Defaults to 20, maximum 100.

    format: int32

  - `string page`

    Query param: Opaque pagination token from a previous `list_vaults` response.

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

### Returns

- `class VaultListPageResponse:`

  Response containing a paginated list of vaults.

  - `IReadOnlyList<BetaManagedAgentsVault> Data`

    List of vaults.

    - `required string ID`

      Unique identifier for the vault.

    - `required DateTimeOffset? ArchivedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string DisplayName`

      Human-readable name for the vault.

    - `required IReadOnlyDictionary<string, string> Metadata`

      Arbitrary key-value metadata attached to the vault.

    - `required Type Type`

    - `required DateTimeOffset UpdatedAt`

      A timestamp in RFC 3339 format

      format: date-time

  - `string? NextPage`

    Pagination token for the next page, or null if no more results.

### Example

```csharp
VaultListParams parameters = new();

var page = await client.Beta.Vaults.List(parameters);
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
      "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "display_name": "Example vault",
      "metadata": {
        "environment": "production"
      },
      "type": "vault",
      "updated_at": "2026-03-15T10:00:00Z"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Get Vault

`BetaManagedAgentsVault Beta.Vaults.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/vaults/{vault_id}`

Get Vault

### Parameters

- `VaultRetrieveParams parameters`

  - `required string vaultID`

    Path parameter vault_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

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

### Returns

- `class BetaManagedAgentsVault:`

  A vault that stores credentials for use by agents during sessions.

  - `required string ID`

    Unique identifier for the vault.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string DisplayName`

    Human-readable name for the vault.

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata attached to the vault.

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

### Example

```csharp
VaultRetrieveParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv"
};

var betaManagedAgentsVault = await client.Beta.Vaults.Retrieve(parameters);

Console.WriteLine(betaManagedAgentsVault);
```

#### Response (200)

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "display_name": "Example vault",
  "metadata": {
    "environment": "production"
  },
  "type": "vault",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

## Update Vault

`BetaManagedAgentsVault Beta.Vaults.Update(parameters, cancellationToken = default)`

**POST** `/v1/vaults/{vault_id}`

Update Vault

### Parameters

- `VaultUpdateParams parameters`

  - `required string vaultID`

    Path param: Path parameter vault_id

  - `string? displayName`

    Body param: Updated human-readable name for the vault. 1-255 characters.

    minLength: 1, maxLength: 255

  - `IReadOnlyDictionary<string, string>? metadata`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

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

### Returns

- `class BetaManagedAgentsVault:`

  A vault that stores credentials for use by agents during sessions.

  - `required string ID`

    Unique identifier for the vault.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string DisplayName`

    Human-readable name for the vault.

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata attached to the vault.

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

### Example

```csharp
VaultUpdateParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv"
};

var betaManagedAgentsVault = await client.Beta.Vaults.Update(parameters);

Console.WriteLine(betaManagedAgentsVault);
```

#### Response (200)

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "display_name": "Example vault",
  "metadata": {
    "environment": "production"
  },
  "type": "vault",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

## Delete Vault

`BetaManagedAgentsDeletedVault Beta.Vaults.Delete(parameters, cancellationToken = default)`

**DELETE** `/v1/vaults/{vault_id}`

Delete Vault

### Parameters

- `VaultDeleteParams parameters`

  - `required string vaultID`

    Path parameter vault_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

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

### Returns

- `class BetaManagedAgentsDeletedVault:`

  Confirmation of a deleted vault.

  - `required string ID`

    Unique identifier of the deleted vault.

  - `required Type Type`

### Example

```csharp
VaultDeleteParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv"
};

var betaManagedAgentsDeletedVault = await client.Beta.Vaults.Delete(parameters);

Console.WriteLine(betaManagedAgentsDeletedVault);
```

#### Response (200)

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "type": "vault_deleted"
}
```

## Archive Vault

`BetaManagedAgentsVault Beta.Vaults.Archive(parameters, cancellationToken = default)`

**POST** `/v1/vaults/{vault_id}/archive`

Archive Vault

### Parameters

- `VaultArchiveParams parameters`

  - `required string vaultID`

    Path parameter vault_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

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

### Returns

- `class BetaManagedAgentsVault:`

  A vault that stores credentials for use by agents during sessions.

  - `required string ID`

    Unique identifier for the vault.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string DisplayName`

    Human-readable name for the vault.

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata attached to the vault.

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

### Example

```csharp
VaultArchiveParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv"
};

var betaManagedAgentsVault = await client.Beta.Vaults.Archive(parameters);

Console.WriteLine(betaManagedAgentsVault);
```

#### Response (200)

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "display_name": "Example vault",
  "metadata": {
    "environment": "production"
  },
  "type": "vault",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

## Domain types

### Beta Managed Agents Deleted Vault

- `class BetaManagedAgentsDeletedVault:`

  Confirmation of a deleted vault.

  - `required string ID`

    Unique identifier of the deleted vault.

  - `required Type Type`

### Beta Managed Agents Vault

- `class BetaManagedAgentsVault:`

  A vault that stores credentials for use by agents during sessions.

  - `required string ID`

    Unique identifier for the vault.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string DisplayName`

    Human-readable name for the vault.

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata attached to the vault.

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

## Vaults › Credentials

### Create Credential

`BetaManagedAgentsCredential Beta.Vaults.Credentials.Create(parameters, cancellationToken = default)`

**POST** `/v1/vaults/{vault_id}/credentials`

Create Credential

#### Parameters

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

#### Returns

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

#### Example

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

##### Response (200)

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

### List Credentials

`CredentialListPageResponse Beta.Vaults.Credentials.List(parameters, cancellationToken = default)`

**GET** `/v1/vaults/{vault_id}/credentials`

List Credentials

#### Parameters

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

#### Returns

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

#### Example

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

##### Response (200)

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

### Get Credential

`BetaManagedAgentsCredential Beta.Vaults.Credentials.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Get Credential

#### Parameters

- `CredentialRetrieveParams parameters`

  - `required string vaultID`

    Path param: Path parameter vault_id

  - `required string credentialID`

    Path param: Path parameter credential_id

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

#### Returns

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

#### Example

```csharp
CredentialRetrieveParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    CredentialID = "vcrd_011CZkZEMt8gZan2iYOQfSkw",
};

var betaManagedAgentsCredential = await client.Beta.Vaults.Credentials.Retrieve(parameters);

Console.WriteLine(betaManagedAgentsCredential);
```

##### Response (200)

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

### Update Credential

`BetaManagedAgentsCredential Beta.Vaults.Credentials.Update(parameters, cancellationToken = default)`

**POST** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Update Credential

#### Parameters

- `CredentialUpdateParams parameters`

  - `required string vaultID`

    Path param: Path parameter vault_id

  - `required string credentialID`

    Path param: Path parameter credential_id

  - `Auth auth`

    Body param: Updated authentication details for a credential.

    - `class BetaManagedAgentsMcpOAuthUpdateParams:`

      Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

      - `required Type Type`

      - `string? AccessToken`

        Updated OAuth access token.

        minLength: 1, maxLength: 8192

      - `DateTimeOffset? ExpiresAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `BetaManagedAgentsMcpOAuthRefreshUpdateParams? Refresh`

        Parameters for updating OAuth refresh token configuration.

        - `string? RefreshToken`

          Updated OAuth refresh token.

          minLength: 1, maxLength: 4096

        - `string? Scope`

          Updated OAuth scope for the refresh request.

          maxLength: 8192

        - `TokenEndpointAuth TokenEndpointAuth`

          Updated HTTP Basic authentication parameters for the token endpoint.

          - `class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam:`

            Updated HTTP Basic authentication parameters for the token endpoint.

            - `required Type Type`

            - `string? ClientSecret`

              Updated OAuth client secret.

              minLength: 1, maxLength: 512

          - `class BetaManagedAgentsTokenEndpointAuthPostUpdateParam:`

            Updated POST body authentication parameters for the token endpoint.

            - `required Type Type`

            - `string? ClientSecret`

              Updated OAuth client secret.

              minLength: 1, maxLength: 512

    - `class BetaManagedAgentsStaticBearerUpdateParams:`

      Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

      - `required Type Type`

      - `string? Token`

        Updated static bearer token value.

        minLength: 1, maxLength: 8192

    - `class BetaManagedAgentsEnvironmentVariableUpdateParams:`

      Parameters for updating an environment variable credential. `secret_name` is immutable.

      - `required Type Type`

      - `BetaManagedAgentsInjectionLocationUpdateParams InjectionLocation`

        Updated injection location.

        - `bool Body`

          Substitute when the placeholder appears in the request body.

        - `bool Header`

          Substitute when the placeholder appears in a request header value.

      - `BetaManagedAgentsCredentialNetworkingParams? Networking`

        Updated networking scope. Full replacement.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingParams:`

          Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

          - `required Type Type`

        - `class BetaManagedAgentsLimitedCredentialNetworkingParams:`

          Substitute the secret only on requests to the listed hosts.

          - `required IReadOnlyList<string> AllowedHosts`

            Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

          - `required Type Type`

      - `string? SecretValue`

        Updated secret value.

        minLength: 1, maxLength: 4096

  - `string? displayName`

    Body param: Updated human-readable name for the credential. 1-255 characters.

    minLength: 1, maxLength: 255

  - `IReadOnlyDictionary<string, string>? metadata`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

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

#### Returns

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

#### Example

```csharp
CredentialUpdateParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    CredentialID = "vcrd_011CZkZEMt8gZan2iYOQfSkw",
};

var betaManagedAgentsCredential = await client.Beta.Vaults.Credentials.Update(parameters);

Console.WriteLine(betaManagedAgentsCredential);
```

##### Response (200)

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

### Delete Credential

`BetaManagedAgentsDeletedCredential Beta.Vaults.Credentials.Delete(parameters, cancellationToken = default)`

**DELETE** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Delete Credential

#### Parameters

- `CredentialDeleteParams parameters`

  - `required string vaultID`

    Path param: Path parameter vault_id

  - `required string credentialID`

    Path param: Path parameter credential_id

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

#### Returns

- `class BetaManagedAgentsDeletedCredential:`

  Confirmation of a deleted credential.

  - `required string ID`

    Unique identifier of the deleted credential.

  - `required Type Type`

#### Example

```csharp
CredentialDeleteParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    CredentialID = "vcrd_011CZkZEMt8gZan2iYOQfSkw",
};

var betaManagedAgentsDeletedCredential = await client.Beta.Vaults.Credentials.Delete(parameters);

Console.WriteLine(betaManagedAgentsDeletedCredential);
```

##### Response (200)

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "type": "vault_credential_deleted"
}
```

### Archive Credential

`BetaManagedAgentsCredential Beta.Vaults.Credentials.Archive(parameters, cancellationToken = default)`

**POST** `/v1/vaults/{vault_id}/credentials/{credential_id}/archive`

Archive Credential

#### Parameters

- `CredentialArchiveParams parameters`

  - `required string vaultID`

    Path param: Path parameter vault_id

  - `required string credentialID`

    Path param: Path parameter credential_id

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

#### Returns

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

#### Example

```csharp
CredentialArchiveParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    CredentialID = "vcrd_011CZkZEMt8gZan2iYOQfSkw",
};

var betaManagedAgentsCredential = await client.Beta.Vaults.Credentials.Archive(parameters);

Console.WriteLine(betaManagedAgentsCredential);
```

##### Response (200)

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

### Validate Credential

`BetaManagedAgentsCredentialValidation Beta.Vaults.Credentials.McpOAuthValidate(parameters, cancellationToken = default)`

**POST** `/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate`

Validate Credential

#### Parameters

- `CredentialMcpOAuthValidateParams parameters`

  - `required string vaultID`

    Path param: Path parameter vault_id

  - `required string credentialID`

    Path param: Path parameter credential_id

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

#### Returns

- `class BetaManagedAgentsCredentialValidation:`

  Result of live-probing a credential against its configured MCP server.

  - `required string CredentialID`

    Unique identifier of the credential that was validated.

  - `required bool HasRefreshToken`

    Whether the credential has a refresh token configured.

  - `required BetaManagedAgentsMcpProbe? McpProbe`

    The failing step of an MCP validation probe.

    - `required BetaManagedAgentsRefreshHttpResponse? HttpResponse`

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

    - `required string Method`

      The MCP method that failed (for example `initialize` or `tools/list`).

  - `required BetaManagedAgentsRefreshObject? Refresh`

    Outcome of a refresh-token exchange attempted during credential validation.

    - `required BetaManagedAgentsRefreshHttpResponse? HttpResponse`

      An HTTP response captured during a credential validation probe.

    - `required Status Status`

      Outcome of a refresh-token exchange attempted during credential validation.

      - `Succeeded`

      - `Failed`

      - `ConnectError`

      - `NoRefreshToken`

  - `required BetaManagedAgentsCredentialValidationStatus Status`

    Overall verdict of a credential validation probe.

    - `Valid`

    - `Invalid`

    - `Unknown`

  - `required Type Type`

  - `required DateTimeOffset ValidatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string VaultID`

    Identifier of the vault containing the credential.

#### Example

```csharp
CredentialMcpOAuthValidateParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    CredentialID = "vcrd_011CZkZEMt8gZan2iYOQfSkw",
};

var betaManagedAgentsCredentialValidation = await client.Beta.Vaults.Credentials.McpOAuthValidate(parameters);

Console.WriteLine(betaManagedAgentsCredentialValidation);
```

##### Response (200)

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
