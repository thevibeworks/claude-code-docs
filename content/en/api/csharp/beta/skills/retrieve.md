# Get Skill

`SkillRetrieveResponse Beta.Skills.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/skills/{skill_id}`

Get Skill

## Parameters

- `SkillRetrieveParams parameters`

  - `required string skillID`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

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

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

## Returns

- `class SkillRetrieveResponse:`

  - `required string ID`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `required string CreatedAt`

    ISO 8601 timestamp of when the skill was created.

  - `required string? DisplayTitle`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `required string? LatestVersion`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `required string Source`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `required string Type`

    Object type.

    For Skills, this is always `"skill"`.

  - `required string UpdatedAt`

    ISO 8601 timestamp of when the skill was last updated.

## Example

```csharp
SkillRetrieveParams parameters = new() { SkillID = "skill_id" };

var skill = await client.Beta.Skills.Retrieve(parameters);

Console.WriteLine(skill);
```

### Response (200)

```json
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_title": "My Custom Skill",
  "latest_version": "1759178010641129",
  "source": "custom",
  "type": "type",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```
