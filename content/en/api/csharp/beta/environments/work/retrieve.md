# Get Work Item

`BetaSelfHostedWork Beta.Environments.Work.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/environments/{environment_id}/work/{work_id}`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Retrieve detailed information about a specific work item.

## Parameters

- `WorkRetrieveParams parameters`

  - `required string environmentID`

    Path param

  - `required string workID`

    Path param

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

- `class BetaSelfHostedWork:`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `required string ID`

    Work identifier (e.g., 'work_...')

  - `required string? AcknowledgedAt`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `required string CreatedAt`

    RFC 3339 timestamp when work was created

  - `required BetaSessionWorkData Data`

    The actual work to be performed

    - `required string ID`

      Session identifier (e.g., 'session_...')

    - `JsonElement Type constant`

      Type of work data

  - `required string EnvironmentID`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `required string? LatestHeartbeatAt`

    RFC 3339 timestamp of the most recent heartbeat

  - `required IReadOnlyDictionary<string, string> Metadata`

    User-provided metadata key-value pairs associated with this work item

  - `required string? Secret`

    Credential payload used by the environment worker to execute this work item. May be populated when polling for work; null on all other retrieval paths.

  - `required string? StartedAt`

    RFC 3339 timestamp when work execution started

  - `required State State`

    Current state of the work item

    - `Queued`

    - `Starting`

    - `Active`

    - `Stopping`

    - `Stopped`

  - `required string? StopRequestedAt`

    RFC 3339 timestamp when stop was requested

  - `required string? StoppedAt`

    RFC 3339 timestamp when work execution stopped

  - `JsonElement Type constant`

    The type of object (always 'work')

## Example

```csharp
WorkRetrieveParams parameters = new()
{
    EnvironmentID = "env_011CZkZ9X2dpNyB7HsEFoRfW",
    WorkID = "work_id",
};

var betaSelfHostedWork = await client.Beta.Environments.Work.Retrieve(parameters);

Console.WriteLine(betaSelfHostedWork);
```

### Response (200)

```json
{
  "id": "id",
  "acknowledged_at": "acknowledged_at",
  "created_at": "created_at",
  "data": {
    "id": "id",
    "type": "session"
  },
  "environment_id": "environment_id",
  "latest_heartbeat_at": "latest_heartbeat_at",
  "metadata": {
    "foo": "string"
  },
  "secret": "secret",
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"
}
```
