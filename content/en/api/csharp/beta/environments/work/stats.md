# Get Queue Statistics

`BetaSelfHostedWorkQueueStats Beta.Environments.Work.Stats(parameters, cancellationToken = default)`

**GET** `/v1/environments/{environment_id}/work/stats`

Get statistics about the work queue for an environment.

## Parameters

- `WorkStatsParams parameters`

  - `required string environmentID`

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

    - `MidConversationOutputConfig2026_07_01`

    - `ThinkingBindingControls2026_08_01`

    - `MidConversationSystemClearAt2026_08_21`

## Returns

- `class BetaSelfHostedWorkQueueStats:`

  Statistics about the work queue for an environment.

  Uses Redis Stream consumer group metrics for O(1) queries.

  - `required long Depth`

    Number of work items waiting to be picked up (lag from consumer group)

  - `required string? OldestQueuedAt`

    RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

  - `required long Pending`

    Number of work items being processed (polled but not acknowledged)

  - `JsonElement Type constant`

    The type of object

  - `required long? WorkersPolling`

    Number of workers that have polled for work in the last 30 seconds. Requires worker_id to be sent with poll requests.

## Example

```csharp
WorkStatsParams parameters = new()
{
    EnvironmentID = "env_011CZkZ9X2dpNyB7HsEFoRfW"
};

var betaSelfHostedWorkQueueStats = await client.Beta.Environments.Work.Stats(parameters);

Console.WriteLine(betaSelfHostedWorkQueueStats);
```

### Response (200)

```json
{
  "depth": 0,
  "oldest_queued_at": "oldest_queued_at",
  "pending": 0,
  "type": "work_queue_stats",
  "workers_polling": 0
}
```
