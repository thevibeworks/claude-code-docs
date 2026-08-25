# Update Session Resource

`ResourceUpdateResponse Beta.Sessions.Resources.Update(parameters, cancellationToken = default)`

**POST** `/v1/sessions/{session_id}/resources/{resource_id}`

Update Session Resource

## Parameters

- `ResourceUpdateParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `required string resourceID`

    Path param: Path parameter resource_id

  - `required string authorizationToken`

    Body param: New authorization token for the resource. Currently only `github_repository` resources support token rotation.

    minLength: 1, maxLength: 4096

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

- `class ResourceUpdateResponse: union`

  The updated session resource.

  - `class BetaManagedAgentsGitHubRepositoryResource:`

    - `required string ID`

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string MountPath`

    - `required Type Type`

    - `required DateTimeOffset UpdatedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string Url`

    - `Checkout? Checkout`

      - `class BetaManagedAgentsBranchCheckout:`

        - `required string Name`

          Branch name to check out.

          minLength: 1, maxLength: 255

        - `required Type Type`

      - `class BetaManagedAgentsCommitCheckout:`

        - `required string Sha`

          Full commit SHA to check out.

          minLength: 7, maxLength: 64

        - `required Type Type`

  - `class BetaManagedAgentsFileResource:`

    - `required string ID`

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string FileID`

    - `required string MountPath`

    - `required Type Type`

    - `required DateTimeOffset UpdatedAt`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsMemoryStoreResource:`

    A memory store attached to an agent session.

    - `required string MemoryStoreID`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `required Type Type`

    - `Access? Access`

      Access mode for an attached memory store.

      - `ReadWrite`

      - `ReadOnly`

    - `string Description`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `string? Instructions`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      maxLength: 4096

    - `string? MountPath`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `string? Name`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

## Example

```csharp
ResourceUpdateParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7",
    ResourceID = "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
    AuthorizationToken = "ghp_exampletoken",
};

var resource = await client.Beta.Sessions.Resources.Update(parameters);

Console.WriteLine(resource);
```

### Response (200)

```json
{
  "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
  "created_at": "2026-03-15T10:00:00Z",
  "mount_path": "/workspace/example-repo",
  "type": "github_repository",
  "updated_at": "2026-03-15T10:00:00Z",
  "url": "https://github.com/example-org/example-repo",
  "checkout": {
    "name": "main",
    "type": "branch"
  }
}
```
