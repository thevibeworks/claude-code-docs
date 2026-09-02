# Update Vault

`BetaManagedAgentsVault Beta.Vaults.Update(parameters, cancellationToken = default)`

**POST** `/v1/vaults/{vault_id}`

Update Vault

## Parameters

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

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

    - `MidConversationOutputConfig2026_07_01`

    - `ThinkingBindingControls2026_08_01`

    - `MidConversationSystemClearAt2026_08_21`

## Returns

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

## Example

```csharp
VaultUpdateParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv"
};

var betaManagedAgentsVault = await client.Beta.Vaults.Update(parameters);

Console.WriteLine(betaManagedAgentsVault);
```

### Response (200)

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
