# Webhooks

## Domain types

### Beta Webhook Agent Archived Event Data

- `class BetaWebhookAgentArchivedEventData:`

  - `String id`

    ID of the agent that triggered the event.

  - `String organizationId`

  - `JsonValue type = "agent.archived"`

  - `String workspaceId`

### Beta Webhook Agent Created Event Data

- `class BetaWebhookAgentCreatedEventData:`

  - `String id`

    ID of the agent that triggered the event.

  - `String organizationId`

  - `JsonValue type = "agent.created"`

  - `String workspaceId`

### Beta Webhook Agent Deleted Event Data

- `class BetaWebhookAgentDeletedEventData:`

  - `String id`

    ID of the agent that triggered the event.

  - `String organizationId`

  - `JsonValue type = "agent.deleted"`

  - `String workspaceId`

### Beta Webhook Agent Updated Event Data

- `class BetaWebhookAgentUpdatedEventData:`

  - `String id`

    ID of the agent that triggered the event.

  - `String organizationId`

  - `JsonValue type = "agent.updated"`

  - `String workspaceId`

### Beta Webhook Deployment Archived Event Data

- `class BetaWebhookDeploymentArchivedEventData:`

  - `String id`

    ID of the deployment that triggered the event.

  - `String organizationId`

  - `JsonValue type = "deployment.archived"`

  - `String workspaceId`

### Beta Webhook Deployment Created Event Data

- `class BetaWebhookDeploymentCreatedEventData:`

  - `String id`

    ID of the deployment that triggered the event.

  - `String organizationId`

  - `JsonValue type = "deployment.created"`

  - `String workspaceId`

### Beta Webhook Deployment Deleted Event Data

- `class BetaWebhookDeploymentDeletedEventData:`

  - `String id`

    ID of the deployment that triggered the event.

  - `String organizationId`

  - `JsonValue type = "deployment.deleted"`

  - `String workspaceId`

### Beta Webhook Deployment Paused Event Data

- `class BetaWebhookDeploymentPausedEventData:`

  - `String id`

    ID of the deployment that triggered the event.

  - `String organizationId`

  - `JsonValue type = "deployment.paused"`

  - `String workspaceId`

### Beta Webhook Deployment Run Failed Event Data

- `class BetaWebhookDeploymentRunFailedEventData:`

  - `String id`

    ID of the deployment run that triggered the event.

  - `String organizationId`

  - `JsonValue type = "deployment_run.failed"`

  - `String workspaceId`

### Beta Webhook Deployment Run Started Event Data

- `class BetaWebhookDeploymentRunStartedEventData:`

  - `String id`

    ID of the deployment run that triggered the event.

  - `String organizationId`

  - `JsonValue type = "deployment_run.started"`

  - `String workspaceId`

### Beta Webhook Deployment Run Succeeded Event Data

- `class BetaWebhookDeploymentRunSucceededEventData:`

  - `String id`

    ID of the deployment run that triggered the event.

  - `String organizationId`

  - `JsonValue type = "deployment_run.succeeded"`

  - `String workspaceId`

### Beta Webhook Deployment Unpaused Event Data

- `class BetaWebhookDeploymentUnpausedEventData:`

  - `String id`

    ID of the deployment that triggered the event.

  - `String organizationId`

  - `JsonValue type = "deployment.unpaused"`

  - `String workspaceId`

### Beta Webhook Deployment Updated Event Data

- `class BetaWebhookDeploymentUpdatedEventData:`

  - `String id`

    ID of the deployment that triggered the event.

  - `String organizationId`

  - `JsonValue type = "deployment.updated"`

  - `String workspaceId`

### Beta Webhook Environment Archived Event Data

- `class BetaWebhookEnvironmentArchivedEventData:`

  - `String id`

    ID of the environment that triggered the event.

  - `String organizationId`

  - `JsonValue type = "environment.archived"`

  - `String workspaceId`

### Beta Webhook Environment Created Event Data

- `class BetaWebhookEnvironmentCreatedEventData:`

  - `String id`

    ID of the environment that triggered the event.

  - `String organizationId`

  - `JsonValue type = "environment.created"`

  - `String workspaceId`

### Beta Webhook Environment Deleted Event Data

- `class BetaWebhookEnvironmentDeletedEventData:`

  - `String id`

    ID of the environment that triggered the event.

  - `String organizationId`

  - `JsonValue type = "environment.deleted"`

  - `String workspaceId`

### Beta Webhook Environment Updated Event Data

- `class BetaWebhookEnvironmentUpdatedEventData:`

  - `String id`

    ID of the environment that triggered the event.

  - `String organizationId`

  - `JsonValue type = "environment.updated"`

  - `String workspaceId`

### Beta Webhook Event

- `class UnwrapWebhookEvent:`

  - `String id`

    Unique event identifier for idempotency.

  - `LocalDateTime createdAt`

    RFC 3339 timestamp when the event occurred.

    format: date-time

  - `BetaWebhookEventData data`

    - `class BetaWebhookSessionCreatedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue type = "session.created"`

      - `String workspaceId`

    - `class BetaWebhookSessionPendingEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue type = "session.pending"`

      - `String workspaceId`

    - `class BetaWebhookSessionRunningEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue type = "session.running"`

      - `String workspaceId`

    - `class BetaWebhookSessionIdledEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue type = "session.idled"`

      - `String workspaceId`

    - `class BetaWebhookSessionRequiresActionEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue type = "session.requires_action"`

      - `String workspaceId`

    - `class BetaWebhookSessionArchivedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue type = "session.archived"`

      - `String workspaceId`

    - `class BetaWebhookSessionDeletedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue type = "session.deleted"`

      - `String workspaceId`

    - `class BetaWebhookSessionStatusRescheduledEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue type = "session.status_rescheduled"`

      - `String workspaceId`

    - `class BetaWebhookSessionStatusRunStartedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue type = "session.status_run_started"`

      - `String workspaceId`

    - `class BetaWebhookSessionStatusIdledEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue type = "session.status_idled"`

      - `String workspaceId`

    - `class BetaWebhookSessionStatusTerminatedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue type = "session.status_terminated"`

      - `String workspaceId`

    - `class BetaWebhookSessionThreadCreatedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String sessionThreadId`

        ID of the session thread this event refers to.

      - `JsonValue type = "session.thread_created"`

      - `String workspaceId`

    - `class BetaWebhookSessionThreadIdledEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String sessionThreadId`

        ID of the session thread this event refers to.

      - `JsonValue type = "session.thread_idled"`

      - `String workspaceId`

    - `class BetaWebhookSessionThreadTerminatedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String sessionThreadId`

        ID of the session thread this event refers to.

      - `JsonValue type = "session.thread_terminated"`

      - `String workspaceId`

    - `class BetaWebhookSessionOutcomeEvaluationEndedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue type = "session.outcome_evaluation_ended"`

      - `String workspaceId`

    - `class BetaWebhookVaultCreatedEventData:`

      - `String id`

        ID of the vault that triggered the event.

      - `String organizationId`

      - `JsonValue type = "vault.created"`

      - `String workspaceId`

    - `class BetaWebhookVaultArchivedEventData:`

      - `String id`

        ID of the vault that triggered the event.

      - `String organizationId`

      - `JsonValue type = "vault.archived"`

      - `String workspaceId`

    - `class BetaWebhookVaultDeletedEventData:`

      - `String id`

        ID of the vault that triggered the event.

      - `String organizationId`

      - `JsonValue type = "vault.deleted"`

      - `String workspaceId`

    - `class BetaWebhookVaultCredentialCreatedEventData:`

      - `String id`

        ID of the vault credential that triggered the event.

      - `String organizationId`

      - `JsonValue type = "vault_credential.created"`

      - `String vaultId`

        ID of the vault that owns this credential.

      - `String workspaceId`

    - `class BetaWebhookVaultCredentialArchivedEventData:`

      - `String id`

        ID of the vault credential that triggered the event.

      - `String organizationId`

      - `JsonValue type = "vault_credential.archived"`

      - `String vaultId`

        ID of the vault that owns this credential.

      - `String workspaceId`

    - `class BetaWebhookVaultCredentialDeletedEventData:`

      - `String id`

        ID of the vault credential that triggered the event.

      - `String organizationId`

      - `JsonValue type = "vault_credential.deleted"`

      - `String vaultId`

        ID of the vault that owns this credential.

      - `String workspaceId`

    - `class BetaWebhookVaultCredentialRefreshFailedEventData:`

      - `String id`

        ID of the vault credential that triggered the event.

      - `String organizationId`

      - `JsonValue type = "vault_credential.refresh_failed"`

      - `String vaultId`

        ID of the vault that owns this credential.

      - `String workspaceId`

    - `class BetaWebhookSessionUpdatedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue type = "session.updated"`

      - `String workspaceId`

    - `class BetaWebhookAgentCreatedEventData:`

      - `String id`

        ID of the agent that triggered the event.

      - `String organizationId`

      - `JsonValue type = "agent.created"`

      - `String workspaceId`

    - `class BetaWebhookAgentArchivedEventData:`

      - `String id`

        ID of the agent that triggered the event.

      - `String organizationId`

      - `JsonValue type = "agent.archived"`

      - `String workspaceId`

    - `class BetaWebhookAgentDeletedEventData:`

      - `String id`

        ID of the agent that triggered the event.

      - `String organizationId`

      - `JsonValue type = "agent.deleted"`

      - `String workspaceId`

    - `class BetaWebhookDeploymentPausedEventData:`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `JsonValue type = "deployment.paused"`

      - `String workspaceId`

    - `class BetaWebhookDeploymentRunFailedEventData:`

      - `String id`

        ID of the deployment run that triggered the event.

      - `String organizationId`

      - `JsonValue type = "deployment_run.failed"`

      - `String workspaceId`

    - `class BetaWebhookDeploymentCreatedEventData:`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `JsonValue type = "deployment.created"`

      - `String workspaceId`

    - `class BetaWebhookDeploymentUpdatedEventData:`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `JsonValue type = "deployment.updated"`

      - `String workspaceId`

    - `class BetaWebhookDeploymentUnpausedEventData:`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `JsonValue type = "deployment.unpaused"`

      - `String workspaceId`

    - `class BetaWebhookAgentUpdatedEventData:`

      - `String id`

        ID of the agent that triggered the event.

      - `String organizationId`

      - `JsonValue type = "agent.updated"`

      - `String workspaceId`

    - `class BetaWebhookDeploymentArchivedEventData:`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `JsonValue type = "deployment.archived"`

      - `String workspaceId`

    - `class BetaWebhookDeploymentRunStartedEventData:`

      - `String id`

        ID of the deployment run that triggered the event.

      - `String organizationId`

      - `JsonValue type = "deployment_run.started"`

      - `String workspaceId`

    - `class BetaWebhookDeploymentDeletedEventData:`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `JsonValue type = "deployment.deleted"`

      - `String workspaceId`

    - `class BetaWebhookDeploymentRunSucceededEventData:`

      - `String id`

        ID of the deployment run that triggered the event.

      - `String organizationId`

      - `JsonValue type = "deployment_run.succeeded"`

      - `String workspaceId`

    - `class BetaWebhookEnvironmentCreatedEventData:`

      - `String id`

        ID of the environment that triggered the event.

      - `String organizationId`

      - `JsonValue type = "environment.created"`

      - `String workspaceId`

    - `class BetaWebhookEnvironmentUpdatedEventData:`

      - `String id`

        ID of the environment that triggered the event.

      - `String organizationId`

      - `JsonValue type = "environment.updated"`

      - `String workspaceId`

    - `class BetaWebhookEnvironmentArchivedEventData:`

      - `String id`

        ID of the environment that triggered the event.

      - `String organizationId`

      - `JsonValue type = "environment.archived"`

      - `String workspaceId`

    - `class BetaWebhookEnvironmentDeletedEventData:`

      - `String id`

        ID of the environment that triggered the event.

      - `String organizationId`

      - `JsonValue type = "environment.deleted"`

      - `String workspaceId`

    - `class BetaWebhookMemoryStoreCreatedEventData:`

      - `String id`

        ID of the memory store that triggered the event.

      - `String organizationId`

      - `JsonValue type = "memory_store.created"`

      - `String workspaceId`

    - `class BetaWebhookMemoryStoreArchivedEventData:`

      - `String id`

        ID of the memory store that triggered the event.

      - `String organizationId`

      - `JsonValue type = "memory_store.archived"`

      - `String workspaceId`

    - `class BetaWebhookMemoryStoreDeletedEventData:`

      - `String id`

        ID of the memory store that triggered the event.

      - `String organizationId`

      - `JsonValue type = "memory_store.deleted"`

      - `String workspaceId`

    - `class BetaWebhookSessionBudgetReachedEventData:`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `JsonValue type = "session.budget_reached"`

      - `String workspaceId`

  - `JsonValue type = "event"`

    Object type. Always `event` for webhook payloads.

### Beta Webhook Event Data

- `class BetaWebhookEventData: union`

  - `class BetaWebhookSessionCreatedEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue type = "session.created"`

    - `String workspaceId`

  - `class BetaWebhookSessionPendingEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue type = "session.pending"`

    - `String workspaceId`

  - `class BetaWebhookSessionRunningEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue type = "session.running"`

    - `String workspaceId`

  - `class BetaWebhookSessionIdledEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue type = "session.idled"`

    - `String workspaceId`

  - `class BetaWebhookSessionRequiresActionEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue type = "session.requires_action"`

    - `String workspaceId`

  - `class BetaWebhookSessionArchivedEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue type = "session.archived"`

    - `String workspaceId`

  - `class BetaWebhookSessionDeletedEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue type = "session.deleted"`

    - `String workspaceId`

  - `class BetaWebhookSessionStatusRescheduledEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue type = "session.status_rescheduled"`

    - `String workspaceId`

  - `class BetaWebhookSessionStatusRunStartedEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue type = "session.status_run_started"`

    - `String workspaceId`

  - `class BetaWebhookSessionStatusIdledEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue type = "session.status_idled"`

    - `String workspaceId`

  - `class BetaWebhookSessionStatusTerminatedEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue type = "session.status_terminated"`

    - `String workspaceId`

  - `class BetaWebhookSessionThreadCreatedEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `String sessionThreadId`

      ID of the session thread this event refers to.

    - `JsonValue type = "session.thread_created"`

    - `String workspaceId`

  - `class BetaWebhookSessionThreadIdledEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `String sessionThreadId`

      ID of the session thread this event refers to.

    - `JsonValue type = "session.thread_idled"`

    - `String workspaceId`

  - `class BetaWebhookSessionThreadTerminatedEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `String sessionThreadId`

      ID of the session thread this event refers to.

    - `JsonValue type = "session.thread_terminated"`

    - `String workspaceId`

  - `class BetaWebhookSessionOutcomeEvaluationEndedEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue type = "session.outcome_evaluation_ended"`

    - `String workspaceId`

  - `class BetaWebhookVaultCreatedEventData:`

    - `String id`

      ID of the vault that triggered the event.

    - `String organizationId`

    - `JsonValue type = "vault.created"`

    - `String workspaceId`

  - `class BetaWebhookVaultArchivedEventData:`

    - `String id`

      ID of the vault that triggered the event.

    - `String organizationId`

    - `JsonValue type = "vault.archived"`

    - `String workspaceId`

  - `class BetaWebhookVaultDeletedEventData:`

    - `String id`

      ID of the vault that triggered the event.

    - `String organizationId`

    - `JsonValue type = "vault.deleted"`

    - `String workspaceId`

  - `class BetaWebhookVaultCredentialCreatedEventData:`

    - `String id`

      ID of the vault credential that triggered the event.

    - `String organizationId`

    - `JsonValue type = "vault_credential.created"`

    - `String vaultId`

      ID of the vault that owns this credential.

    - `String workspaceId`

  - `class BetaWebhookVaultCredentialArchivedEventData:`

    - `String id`

      ID of the vault credential that triggered the event.

    - `String organizationId`

    - `JsonValue type = "vault_credential.archived"`

    - `String vaultId`

      ID of the vault that owns this credential.

    - `String workspaceId`

  - `class BetaWebhookVaultCredentialDeletedEventData:`

    - `String id`

      ID of the vault credential that triggered the event.

    - `String organizationId`

    - `JsonValue type = "vault_credential.deleted"`

    - `String vaultId`

      ID of the vault that owns this credential.

    - `String workspaceId`

  - `class BetaWebhookVaultCredentialRefreshFailedEventData:`

    - `String id`

      ID of the vault credential that triggered the event.

    - `String organizationId`

    - `JsonValue type = "vault_credential.refresh_failed"`

    - `String vaultId`

      ID of the vault that owns this credential.

    - `String workspaceId`

  - `class BetaWebhookSessionUpdatedEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue type = "session.updated"`

    - `String workspaceId`

  - `class BetaWebhookAgentCreatedEventData:`

    - `String id`

      ID of the agent that triggered the event.

    - `String organizationId`

    - `JsonValue type = "agent.created"`

    - `String workspaceId`

  - `class BetaWebhookAgentArchivedEventData:`

    - `String id`

      ID of the agent that triggered the event.

    - `String organizationId`

    - `JsonValue type = "agent.archived"`

    - `String workspaceId`

  - `class BetaWebhookAgentDeletedEventData:`

    - `String id`

      ID of the agent that triggered the event.

    - `String organizationId`

    - `JsonValue type = "agent.deleted"`

    - `String workspaceId`

  - `class BetaWebhookDeploymentPausedEventData:`

    - `String id`

      ID of the deployment that triggered the event.

    - `String organizationId`

    - `JsonValue type = "deployment.paused"`

    - `String workspaceId`

  - `class BetaWebhookDeploymentRunFailedEventData:`

    - `String id`

      ID of the deployment run that triggered the event.

    - `String organizationId`

    - `JsonValue type = "deployment_run.failed"`

    - `String workspaceId`

  - `class BetaWebhookDeploymentCreatedEventData:`

    - `String id`

      ID of the deployment that triggered the event.

    - `String organizationId`

    - `JsonValue type = "deployment.created"`

    - `String workspaceId`

  - `class BetaWebhookDeploymentUpdatedEventData:`

    - `String id`

      ID of the deployment that triggered the event.

    - `String organizationId`

    - `JsonValue type = "deployment.updated"`

    - `String workspaceId`

  - `class BetaWebhookDeploymentUnpausedEventData:`

    - `String id`

      ID of the deployment that triggered the event.

    - `String organizationId`

    - `JsonValue type = "deployment.unpaused"`

    - `String workspaceId`

  - `class BetaWebhookAgentUpdatedEventData:`

    - `String id`

      ID of the agent that triggered the event.

    - `String organizationId`

    - `JsonValue type = "agent.updated"`

    - `String workspaceId`

  - `class BetaWebhookDeploymentArchivedEventData:`

    - `String id`

      ID of the deployment that triggered the event.

    - `String organizationId`

    - `JsonValue type = "deployment.archived"`

    - `String workspaceId`

  - `class BetaWebhookDeploymentRunStartedEventData:`

    - `String id`

      ID of the deployment run that triggered the event.

    - `String organizationId`

    - `JsonValue type = "deployment_run.started"`

    - `String workspaceId`

  - `class BetaWebhookDeploymentDeletedEventData:`

    - `String id`

      ID of the deployment that triggered the event.

    - `String organizationId`

    - `JsonValue type = "deployment.deleted"`

    - `String workspaceId`

  - `class BetaWebhookDeploymentRunSucceededEventData:`

    - `String id`

      ID of the deployment run that triggered the event.

    - `String organizationId`

    - `JsonValue type = "deployment_run.succeeded"`

    - `String workspaceId`

  - `class BetaWebhookEnvironmentCreatedEventData:`

    - `String id`

      ID of the environment that triggered the event.

    - `String organizationId`

    - `JsonValue type = "environment.created"`

    - `String workspaceId`

  - `class BetaWebhookEnvironmentUpdatedEventData:`

    - `String id`

      ID of the environment that triggered the event.

    - `String organizationId`

    - `JsonValue type = "environment.updated"`

    - `String workspaceId`

  - `class BetaWebhookEnvironmentArchivedEventData:`

    - `String id`

      ID of the environment that triggered the event.

    - `String organizationId`

    - `JsonValue type = "environment.archived"`

    - `String workspaceId`

  - `class BetaWebhookEnvironmentDeletedEventData:`

    - `String id`

      ID of the environment that triggered the event.

    - `String organizationId`

    - `JsonValue type = "environment.deleted"`

    - `String workspaceId`

  - `class BetaWebhookMemoryStoreCreatedEventData:`

    - `String id`

      ID of the memory store that triggered the event.

    - `String organizationId`

    - `JsonValue type = "memory_store.created"`

    - `String workspaceId`

  - `class BetaWebhookMemoryStoreArchivedEventData:`

    - `String id`

      ID of the memory store that triggered the event.

    - `String organizationId`

    - `JsonValue type = "memory_store.archived"`

    - `String workspaceId`

  - `class BetaWebhookMemoryStoreDeletedEventData:`

    - `String id`

      ID of the memory store that triggered the event.

    - `String organizationId`

    - `JsonValue type = "memory_store.deleted"`

    - `String workspaceId`

  - `class BetaWebhookSessionBudgetReachedEventData:`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `JsonValue type = "session.budget_reached"`

    - `String workspaceId`

### Beta Webhook Memory Store Archived Event Data

- `class BetaWebhookMemoryStoreArchivedEventData:`

  - `String id`

    ID of the memory store that triggered the event.

  - `String organizationId`

  - `JsonValue type = "memory_store.archived"`

  - `String workspaceId`

### Beta Webhook Memory Store Created Event Data

- `class BetaWebhookMemoryStoreCreatedEventData:`

  - `String id`

    ID of the memory store that triggered the event.

  - `String organizationId`

  - `JsonValue type = "memory_store.created"`

  - `String workspaceId`

### Beta Webhook Memory Store Deleted Event Data

- `class BetaWebhookMemoryStoreDeletedEventData:`

  - `String id`

    ID of the memory store that triggered the event.

  - `String organizationId`

  - `JsonValue type = "memory_store.deleted"`

  - `String workspaceId`

### Beta Webhook Session Archived Event Data

- `class BetaWebhookSessionArchivedEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue type = "session.archived"`

  - `String workspaceId`

### Beta Webhook Session Budget Reached Event Data

- `class BetaWebhookSessionBudgetReachedEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue type = "session.budget_reached"`

  - `String workspaceId`

### Beta Webhook Session Created Event Data

- `class BetaWebhookSessionCreatedEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue type = "session.created"`

  - `String workspaceId`

### Beta Webhook Session Deleted Event Data

- `class BetaWebhookSessionDeletedEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue type = "session.deleted"`

  - `String workspaceId`

### Beta Webhook Session Idled Event Data

- `class BetaWebhookSessionIdledEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue type = "session.idled"`

  - `String workspaceId`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `class BetaWebhookSessionOutcomeEvaluationEndedEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue type = "session.outcome_evaluation_ended"`

  - `String workspaceId`

### Beta Webhook Session Pending Event Data

- `class BetaWebhookSessionPendingEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue type = "session.pending"`

  - `String workspaceId`

### Beta Webhook Session Requires Action Event Data

- `class BetaWebhookSessionRequiresActionEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue type = "session.requires_action"`

  - `String workspaceId`

### Beta Webhook Session Running Event Data

- `class BetaWebhookSessionRunningEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue type = "session.running"`

  - `String workspaceId`

### Beta Webhook Session Status Idled Event Data

- `class BetaWebhookSessionStatusIdledEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue type = "session.status_idled"`

  - `String workspaceId`

### Beta Webhook Session Status Rescheduled Event Data

- `class BetaWebhookSessionStatusRescheduledEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue type = "session.status_rescheduled"`

  - `String workspaceId`

### Beta Webhook Session Status Run Started Event Data

- `class BetaWebhookSessionStatusRunStartedEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue type = "session.status_run_started"`

  - `String workspaceId`

### Beta Webhook Session Status Terminated Event Data

- `class BetaWebhookSessionStatusTerminatedEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue type = "session.status_terminated"`

  - `String workspaceId`

### Beta Webhook Session Thread Created Event Data

- `class BetaWebhookSessionThreadCreatedEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `String sessionThreadId`

    ID of the session thread this event refers to.

  - `JsonValue type = "session.thread_created"`

  - `String workspaceId`

### Beta Webhook Session Thread Idled Event Data

- `class BetaWebhookSessionThreadIdledEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `String sessionThreadId`

    ID of the session thread this event refers to.

  - `JsonValue type = "session.thread_idled"`

  - `String workspaceId`

### Beta Webhook Session Thread Terminated Event Data

- `class BetaWebhookSessionThreadTerminatedEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `String sessionThreadId`

    ID of the session thread this event refers to.

  - `JsonValue type = "session.thread_terminated"`

  - `String workspaceId`

### Beta Webhook Session Updated Event Data

- `class BetaWebhookSessionUpdatedEventData:`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `JsonValue type = "session.updated"`

  - `String workspaceId`

### Beta Webhook Vault Archived Event Data

- `class BetaWebhookVaultArchivedEventData:`

  - `String id`

    ID of the vault that triggered the event.

  - `String organizationId`

  - `JsonValue type = "vault.archived"`

  - `String workspaceId`

### Beta Webhook Vault Created Event Data

- `class BetaWebhookVaultCreatedEventData:`

  - `String id`

    ID of the vault that triggered the event.

  - `String organizationId`

  - `JsonValue type = "vault.created"`

  - `String workspaceId`

### Beta Webhook Vault Credential Archived Event Data

- `class BetaWebhookVaultCredentialArchivedEventData:`

  - `String id`

    ID of the vault credential that triggered the event.

  - `String organizationId`

  - `JsonValue type = "vault_credential.archived"`

  - `String vaultId`

    ID of the vault that owns this credential.

  - `String workspaceId`

### Beta Webhook Vault Credential Created Event Data

- `class BetaWebhookVaultCredentialCreatedEventData:`

  - `String id`

    ID of the vault credential that triggered the event.

  - `String organizationId`

  - `JsonValue type = "vault_credential.created"`

  - `String vaultId`

    ID of the vault that owns this credential.

  - `String workspaceId`

### Beta Webhook Vault Credential Deleted Event Data

- `class BetaWebhookVaultCredentialDeletedEventData:`

  - `String id`

    ID of the vault credential that triggered the event.

  - `String organizationId`

  - `JsonValue type = "vault_credential.deleted"`

  - `String vaultId`

    ID of the vault that owns this credential.

  - `String workspaceId`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `class BetaWebhookVaultCredentialRefreshFailedEventData:`

  - `String id`

    ID of the vault credential that triggered the event.

  - `String organizationId`

  - `JsonValue type = "vault_credential.refresh_failed"`

  - `String vaultId`

    ID of the vault that owns this credential.

  - `String workspaceId`

### Beta Webhook Vault Deleted Event Data

- `class BetaWebhookVaultDeletedEventData:`

  - `String id`

    ID of the vault that triggered the event.

  - `String organizationId`

  - `JsonValue type = "vault.deleted"`

  - `String workspaceId`
