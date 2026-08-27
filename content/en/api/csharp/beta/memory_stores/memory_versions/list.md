# List memory versions

`MemoryVersionListPageResponse Beta.MemoryStores.MemoryVersions.List(parameters, cancellationToken = default)`

**GET** `/v1/memory_stores/{memory_store_id}/memory_versions`

List memory versions

## Parameters

- `MemoryVersionListParams parameters`

  - `required string memoryStoreID`

    Path param: Path parameter memory_store_id

  - `string apiKeyID`

    Query param: Query parameter for api_key_id

  - `DateTimeOffset createdAtGte`

    Query param: Return versions created at or after this time (inclusive).

    format: date-time

  - `DateTimeOffset createdAtLte`

    Query param: Return versions created at or before this time (inclusive).

    format: date-time

  - `int limit`

    Query param: Query parameter for limit

    format: int32

  - `string memoryID`

    Query param: Query parameter for memory_id

  - `BetaManagedAgentsMemoryVersionOperation operation`

    Query param: Query parameter for operation

  - `string page`

    Query param: Query parameter for page

  - `string serviceAccountID`

    Query param: Query parameter for service_account_id

  - `string sessionID`

    Query param: Query parameter for session_id

  - `BetaManagedAgentsMemoryView view`

    Query param: Query parameter for view

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

- `class MemoryVersionListPageResponse:`

  Response payload for [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `IReadOnlyList<BetaManagedAgentsMemoryVersion> Data`

    One page of `memory_version` objects, ordered by `created_at` descending (newest first), with `id` as tiebreak.

    - `required string ID`

      Unique identifier for this version (a `memver_...` value).

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string MemoryID`

      ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the memory's retained versions, including the `deleted` row while the lineage is retained.

    - `required string MemoryStoreID`

      ID of the memory store this version belongs to (a `memstore_...` value).

    - `required BetaManagedAgentsMemoryVersionOperation Operation`

      The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

      - `Created`

      - `Modified`

      - `Deleted`

    - `required Type Type`

    - `string? Content`

      The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

    - `string? ContentSha256`

      Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

    - `int? ContentSizeBytes`

      Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

      format: int32

    - `BetaManagedAgentsActor CreatedBy`

      Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

      - `class BetaManagedAgentsSessionActor:`

        Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

        - `required string SessionID`

          ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

          minLength: 1

        - `required Type Type`

      - `class BetaManagedAgentsApiActor:`

        Attribution for a write made directly via the public API (outside of any session).

        - `required string ApiKeyID`

          ID of the API key that performed the write. This identifies the key, not the secret.

          minLength: 1

        - `required Type Type`

      - `class BetaManagedAgentsUserActor:`

        Attribution for a write made by a human user through the Anthropic Console.

        - `required Type Type`

        - `required string UserID`

          ID of the user who performed the write (a `user_...` value).

          minLength: 1

      - `class BetaManagedAgentsServiceAccountActor:`

        Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

        - `required string ServiceAccountID`

          ID of the service account that performed the write (a `svac_...` value).

          minLength: 1

        - `JsonElement Type constant`

    - `string? Path`

      The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

    - `DateTimeOffset? RedactedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `BetaManagedAgentsActor RedactedBy`

      Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

  - `string? NextPage`

    Opaque cursor for the next page (a `page_...` value), or `null` if there are no more results. Pass as `page` on the next request.

## Example

```csharp
MemoryVersionListParams parameters = new()
{
    MemoryStoreID = "memory_store_id"
};

var page = await client.Beta.MemoryStores.MemoryVersions.List(parameters);
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
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "memory_id": "memory_id",
      "memory_store_id": "memory_store_id",
      "operation": "created",
      "type": "memory_version",
      "content": "content",
      "content_sha256": "content_sha256",
      "content_size_bytes": 0,
      "created_by": {
        "session_id": "x",
        "type": "session_actor"
      },
      "path": "path",
      "redacted_at": "2019-12-27T18:11:19.117Z",
      "redacted_by": {
        "session_id": "x",
        "type": "session_actor"
      }
    }
  ],
  "next_page": "next_page"
}
```
