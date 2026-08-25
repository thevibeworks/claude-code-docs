# List Skill Versions

`VersionListPageResponse Beta.Skills.Versions.List(parameters, cancellationToken = default)`

**GET** `/v1/skills/{skill_id}/versions`

List Skill Versions

## Parameters

- `VersionListParams parameters`

  - `required string skillID`

    Path param: Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `long? limit`

    Query param: Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

  - `string? page`

    Query param: Optionally set to the `next_page` token from the previous response.

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

- `class VersionListPageResponse:`

  - `required IReadOnlyList<VersionListResponse> Data`

    List of skill versions.

    - `required string ID`

      Unique identifier for the skill version.

      The format and length of IDs may change over time.

    - `required string CreatedAt`

      ISO 8601 timestamp of when the skill version was created.

    - `required string Description`

      Description of the skill version.

      This is extracted from the SKILL.md file in the skill upload.

    - `required string Directory`

      Directory name of the skill version.

      This is the top-level directory name that was extracted from the uploaded files.

    - `required string Name`

      Human-readable name of the skill version.

      This is extracted from the SKILL.md file in the skill upload.

    - `required string SkillID`

      Identifier for the skill that this version belongs to.

    - `required string Type`

      Object type.

      For Skill Versions, this is always `"skill_version"`.

    - `required string Version`

      Version identifier for the skill.

      Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

  - `required bool HasMore`

    Indicates if there are more results in the requested page direction.

  - `required string? NextPage`

    Token to provide in as `page` in the subsequent request to retrieve the next page of data.

## Example

```csharp
VersionListParams parameters = new() { SkillID = "skill_id" };

var page = await client.Beta.Skills.Versions.List(parameters);
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
      "id": "skillver_01JAbcdefghijklmnopqrstuvw",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "description": "A custom skill for doing something useful",
      "directory": "my-skill",
      "name": "my-skill",
      "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
      "type": "type",
      "version": "1759178010641129"
    }
  ],
  "has_more": true,
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```
