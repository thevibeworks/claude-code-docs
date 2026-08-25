# List Vaults

`VaultListPageResponse Beta.Vaults.List(parameters, cancellationToken = default)`

**GET** `/v1/vaults`

List Vaults

## Parameters

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

## Returns

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

## Example

```csharp
VaultListParams parameters = new();

var page = await client.Beta.Vaults.List(parameters);
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
