# Get Deployment Run

`BetaManagedAgentsDeploymentRun Beta.DeploymentRuns.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/deployment_runs/{deployment_run_id}`

Get Deployment Run

## Parameters

- `DeploymentRunRetrieveParams parameters`

  - `required string deploymentRunID`

    Path parameter deployment_run_id

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

- `class BetaManagedAgentsDeploymentRun:`

  A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

  - `required string ID`

    Unique identifier for this run (`drun_...`).

  - `required BetaManagedAgentsAgentReference Agent`

    A resolved agent reference with a concrete version.

    - `required string ID`

    - `required Type Type`

    - `required int Version`

      format: int32

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string DeploymentID`

    ID of the deployment that produced this run.

  - `required Error? Error`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

    - `class BetaManagedAgentsEnvironmentArchivedRunError:`

      The deployment's environment was archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsAgentArchivedRunError:`

      The deployment's agent was archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsEnvironmentNotFoundRunError:`

      The deployment's environment no longer exists.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsVaultNotFoundRunError:`

      A vault referenced by the deployment no longer exists.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsVaultArchivedRunError:`

      A vault referenced by the deployment is archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsFileNotFoundRunError:`

      A file resource referenced by the deployment no longer exists.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsMemoryStoreArchivedRunError:`

      A memory store referenced by the deployment is archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsSkillNotFoundRunError:`

      A skill referenced by the deployment's agent no longer exists.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsSessionResourceNotFoundRunError:`

      A referenced resource no longer exists and its kind was not reported.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsWorkspaceArchivedRunError:`

      The deployment's workspace was archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsOrganizationDisabledRunError:`

      The deployment's organization is disabled.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsSessionRateLimitedRunError:`

      Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsSessionCreationRejectedRunError:`

      The session create request was rejected with a non-retryable validation error.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsUnknownRunError:`

      An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsSelfHostedResourcesUnsupportedRunError:`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsMcpEgressBlockedRunError:`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

  - `required string? SessionID`

    Populated on success. Null on creation failure. Exactly one of `session_id` or `error` is non-null.

  - `required BetaManagedAgentsTriggerContext TriggerContext`

    Describes what triggered a deployment run, with trigger-specific metadata.

    - `class BetaManagedAgentsScheduleTriggerContext:`

      The run was fired by the deployment's cron schedule.

      - `required DateTimeOffset ScheduledAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required Type Type`

    - `class BetaManagedAgentsManualTriggerContext:`

      The run was started manually by creating a session directly against the deployment.

      - `required Type Type`

  - `required Type Type`

## Example

```csharp
DeploymentRunRetrieveParams parameters = new()
{
    DeploymentRunID = "deployment_run_id"
};

var betaManagedAgentsDeploymentRun = await client.Beta.DeploymentRuns.Retrieve(parameters);

Console.WriteLine(betaManagedAgentsDeploymentRun);
```

### Response (200)

```json
{
  "id": "id",
  "agent": {
    "id": "agent_011CZkYqphY8vELVzwCUpqiQ",
    "type": "agent",
    "version": 1
  },
  "created_at": "2019-12-27T18:11:19.117Z",
  "deployment_id": "deployment_id",
  "error": {
    "message": "message",
    "type": "environment_archived_error"
  },
  "session_id": "session_id",
  "trigger_context": {
    "scheduled_at": "2019-12-27T18:11:19.117Z",
    "type": "schedule"
  },
  "type": "deployment_run"
}
```
