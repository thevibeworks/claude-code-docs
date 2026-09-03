# Run Deployment Now

`BetaManagedAgentsDeploymentRun Beta.Deployments.Run(parameters, cancellationToken = default)`

**POST** `/v1/deployments/{deployment_id}/run`

Run Deployment Now

## Parameters

- `DeploymentRunParams parameters`

  - `required string deploymentID`

    Path parameter deployment_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24("message-batches-2024-09-24")`

    - `PromptCaching2024_07_31("prompt-caching-2024-07-31")`

    - `ComputerUse2024_10_22("computer-use-2024-10-22")`

    - `ComputerUse2025_01_24("computer-use-2025-01-24")`

    - `Pdfs2024_09_25("pdfs-2024-09-25")`

    - `TokenCounting2024_11_01("token-counting-2024-11-01")`

    - `TokenEfficientTools2025_02_19("token-efficient-tools-2025-02-19")`

    - `Output128k2025_02_19("output-128k-2025-02-19")`

    - `FilesApi2025_04_14("files-api-2025-04-14")`

    - `McpClient2025_04_04("mcp-client-2025-04-04")`

    - `McpClient2025_11_20("mcp-client-2025-11-20")`

    - `DevFullThinking2025_05_14("dev-full-thinking-2025-05-14")`

    - `InterleavedThinking2025_05_14("interleaved-thinking-2025-05-14")`

    - `CodeExecution2025_05_22("code-execution-2025-05-22")`

    - `ExtendedCacheTtl2025_04_11("extended-cache-ttl-2025-04-11")`

    - `Context1m2025_08_07("context-1m-2025-08-07")`

    - `ContextManagement2025_06_27("context-management-2025-06-27")`

    - `ModelContextWindowExceeded2025_08_26("model-context-window-exceeded-2025-08-26")`

    - `Skills2025_10_02("skills-2025-10-02")`

    - `FastMode2026_02_01("fast-mode-2026-02-01")`

    - `Output300k2026_03_24("output-300k-2026-03-24")`

    - `UserProfiles2026_03_24("user-profiles-2026-03-24")`

    - `UserProfiles2026_08_18("user-profiles-2026-08-18")`

    - `AdvisorTool2026_03_01("advisor-tool-2026-03-01")`

    - `ManagedAgents2026_04_01("managed-agents-2026-04-01")`

    - `CacheDiagnosis2026_04_07("cache-diagnosis-2026-04-07")`

    - `Dreaming2026_04_21("dreaming-2026-04-21")`

    - `ThinkingTokenCount2026_05_13("thinking-token-count-2026-05-13")`

    - `ServerSideFallback2026_06_01("server-side-fallback-2026-06-01")`

    - `ServerSideFallback2026_07_01("server-side-fallback-2026-07-01")`

    - `FallbackCredit2026_06_01("fallback-credit-2026-06-01")`

    - `FallbackCredit2026_07_01("fallback-credit-2026-07-01")`

    - `AgentMemory2026_07_22("agent-memory-2026-07-22")`

    - `MidConversationToolChanges2026_07_01("mid-conversation-tool-changes-2026-07-01")`

    - `Compact2026_01_12("compact-2026-01-12")`

    - `ComputerUse2025_11_24("computer-use-2025-11-24")`

    - `McpTunnels2026_06_22("mcp-tunnels-2026-06-22")`

    - `StructuredOutputs2025_11_13("structured-outputs-2025-11-13")`

    - `TaskBudgets2026_03_13("task-budgets-2026-03-13")`

    - `ThinkingDisplayUpdates2026_08_18("thinking-display-updates-2026-08-18")`

    - `CEUserManagement2026_07_13("ce-user-management-2026-07-13")`

    - `MidConversationOutputConfig2026_07_01("mid-conversation-output-config-2026-07-01")`

    - `ThinkingBindingControls2026_08_01("thinking-binding-controls-2026-08-01")`

    - `MidConversationSystemClearAt2026_08_21("mid-conversation-system-clear-at-2026-08-21")`

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
DeploymentRunParams parameters = new()
{
    DeploymentID = "depl_011CZkZcDH3vPqd7xnEfwTai"
};

var betaManagedAgentsDeploymentRun = await client.Beta.Deployments.Run(parameters);

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
