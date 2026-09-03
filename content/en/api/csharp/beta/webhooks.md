# Webhooks

## Domain types

### Beta Webhook Agent Archived Event Data

- `class BetaWebhookAgentArchivedEventData:`

  - `required string ID`

    ID of the agent that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "agent.archived"`

  - `required string WorkspaceID`

### Beta Webhook Agent Created Event Data

- `class BetaWebhookAgentCreatedEventData:`

  - `required string ID`

    ID of the agent that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "agent.created"`

  - `required string WorkspaceID`

### Beta Webhook Agent Deleted Event Data

- `class BetaWebhookAgentDeletedEventData:`

  - `required string ID`

    ID of the agent that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "agent.deleted"`

  - `required string WorkspaceID`

### Beta Webhook Agent Updated Event Data

- `class BetaWebhookAgentUpdatedEventData:`

  - `required string ID`

    ID of the agent that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "agent.updated"`

  - `required string WorkspaceID`

### Beta Webhook Deployment Archived Event Data

- `class BetaWebhookDeploymentArchivedEventData:`

  - `required string ID`

    ID of the deployment that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "deployment.archived"`

  - `required string WorkspaceID`

### Beta Webhook Deployment Created Event Data

- `class BetaWebhookDeploymentCreatedEventData:`

  - `required string ID`

    ID of the deployment that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "deployment.created"`

  - `required string WorkspaceID`

### Beta Webhook Deployment Deleted Event Data

- `class BetaWebhookDeploymentDeletedEventData:`

  - `required string ID`

    ID of the deployment that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "deployment.deleted"`

  - `required string WorkspaceID`

### Beta Webhook Deployment Paused Event Data

- `class BetaWebhookDeploymentPausedEventData:`

  - `required string ID`

    ID of the deployment that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "deployment.paused"`

  - `required string WorkspaceID`

### Beta Webhook Deployment Run Failed Event Data

- `class BetaWebhookDeploymentRunFailedEventData:`

  - `required string ID`

    ID of the deployment run that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "deployment_run.failed"`

  - `required string WorkspaceID`

### Beta Webhook Deployment Run Started Event Data

- `class BetaWebhookDeploymentRunStartedEventData:`

  - `required string ID`

    ID of the deployment run that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "deployment_run.started"`

  - `required string WorkspaceID`

### Beta Webhook Deployment Run Succeeded Event Data

- `class BetaWebhookDeploymentRunSucceededEventData:`

  - `required string ID`

    ID of the deployment run that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "deployment_run.succeeded"`

  - `required string WorkspaceID`

### Beta Webhook Deployment Unpaused Event Data

- `class BetaWebhookDeploymentUnpausedEventData:`

  - `required string ID`

    ID of the deployment that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "deployment.unpaused"`

  - `required string WorkspaceID`

### Beta Webhook Deployment Updated Event Data

- `class BetaWebhookDeploymentUpdatedEventData:`

  - `required string ID`

    ID of the deployment that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "deployment.updated"`

  - `required string WorkspaceID`

### Beta Webhook Environment Archived Event Data

- `class BetaWebhookEnvironmentArchivedEventData:`

  - `required string ID`

    ID of the environment that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "environment.archived"`

  - `required string WorkspaceID`

### Beta Webhook Environment Created Event Data

- `class BetaWebhookEnvironmentCreatedEventData:`

  - `required string ID`

    ID of the environment that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "environment.created"`

  - `required string WorkspaceID`

### Beta Webhook Environment Deleted Event Data

- `class BetaWebhookEnvironmentDeletedEventData:`

  - `required string ID`

    ID of the environment that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "environment.deleted"`

  - `required string WorkspaceID`

### Beta Webhook Environment Updated Event Data

- `class BetaWebhookEnvironmentUpdatedEventData:`

  - `required string ID`

    ID of the environment that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "environment.updated"`

  - `required string WorkspaceID`

### Beta Webhook Event

- `class UnwrapWebhookEvent:`

  - `required string ID`

    Unique event identifier for idempotency.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 timestamp when the event occurred.

    format: date-time

  - `required BetaWebhookEventData Data`

    - `class BetaWebhookSessionCreatedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "session.created"`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionPendingEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "session.pending"`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionRunningEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "session.running"`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionIdledEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "session.idled"`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionRequiresActionEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "session.requires_action"`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionArchivedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "session.archived"`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionDeletedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "session.deleted"`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionStatusRescheduledEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "session.status_rescheduled"`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionStatusRunStartedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "session.status_run_started"`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionStatusIdledEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "session.status_idled"`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionStatusTerminatedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "session.status_terminated"`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionThreadCreatedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `required string SessionThreadID`

        ID of the session thread this event refers to.

      - `JsonElement Type = "session.thread_created"`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionThreadIdledEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `required string SessionThreadID`

        ID of the session thread this event refers to.

      - `JsonElement Type = "session.thread_idled"`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionThreadTerminatedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `required string SessionThreadID`

        ID of the session thread this event refers to.

      - `JsonElement Type = "session.thread_terminated"`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionOutcomeEvaluationEndedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "session.outcome_evaluation_ended"`

      - `required string WorkspaceID`

    - `class BetaWebhookVaultCreatedEventData:`

      - `required string ID`

        ID of the vault that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "vault.created"`

      - `required string WorkspaceID`

    - `class BetaWebhookVaultArchivedEventData:`

      - `required string ID`

        ID of the vault that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "vault.archived"`

      - `required string WorkspaceID`

    - `class BetaWebhookVaultDeletedEventData:`

      - `required string ID`

        ID of the vault that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "vault.deleted"`

      - `required string WorkspaceID`

    - `class BetaWebhookVaultCredentialCreatedEventData:`

      - `required string ID`

        ID of the vault credential that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "vault_credential.created"`

      - `required string VaultID`

        ID of the vault that owns this credential.

      - `required string WorkspaceID`

    - `class BetaWebhookVaultCredentialArchivedEventData:`

      - `required string ID`

        ID of the vault credential that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "vault_credential.archived"`

      - `required string VaultID`

        ID of the vault that owns this credential.

      - `required string WorkspaceID`

    - `class BetaWebhookVaultCredentialDeletedEventData:`

      - `required string ID`

        ID of the vault credential that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "vault_credential.deleted"`

      - `required string VaultID`

        ID of the vault that owns this credential.

      - `required string WorkspaceID`

    - `class BetaWebhookVaultCredentialRefreshFailedEventData:`

      - `required string ID`

        ID of the vault credential that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "vault_credential.refresh_failed"`

      - `required string VaultID`

        ID of the vault that owns this credential.

      - `required string WorkspaceID`

    - `class BetaWebhookSessionUpdatedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "session.updated"`

      - `required string WorkspaceID`

    - `class BetaWebhookAgentCreatedEventData:`

      - `required string ID`

        ID of the agent that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "agent.created"`

      - `required string WorkspaceID`

    - `class BetaWebhookAgentArchivedEventData:`

      - `required string ID`

        ID of the agent that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "agent.archived"`

      - `required string WorkspaceID`

    - `class BetaWebhookAgentDeletedEventData:`

      - `required string ID`

        ID of the agent that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "agent.deleted"`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentPausedEventData:`

      - `required string ID`

        ID of the deployment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "deployment.paused"`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentRunFailedEventData:`

      - `required string ID`

        ID of the deployment run that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "deployment_run.failed"`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentCreatedEventData:`

      - `required string ID`

        ID of the deployment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "deployment.created"`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentUpdatedEventData:`

      - `required string ID`

        ID of the deployment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "deployment.updated"`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentUnpausedEventData:`

      - `required string ID`

        ID of the deployment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "deployment.unpaused"`

      - `required string WorkspaceID`

    - `class BetaWebhookAgentUpdatedEventData:`

      - `required string ID`

        ID of the agent that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "agent.updated"`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentArchivedEventData:`

      - `required string ID`

        ID of the deployment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "deployment.archived"`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentRunStartedEventData:`

      - `required string ID`

        ID of the deployment run that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "deployment_run.started"`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentDeletedEventData:`

      - `required string ID`

        ID of the deployment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "deployment.deleted"`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentRunSucceededEventData:`

      - `required string ID`

        ID of the deployment run that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "deployment_run.succeeded"`

      - `required string WorkspaceID`

    - `class BetaWebhookEnvironmentCreatedEventData:`

      - `required string ID`

        ID of the environment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "environment.created"`

      - `required string WorkspaceID`

    - `class BetaWebhookEnvironmentUpdatedEventData:`

      - `required string ID`

        ID of the environment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "environment.updated"`

      - `required string WorkspaceID`

    - `class BetaWebhookEnvironmentArchivedEventData:`

      - `required string ID`

        ID of the environment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "environment.archived"`

      - `required string WorkspaceID`

    - `class BetaWebhookEnvironmentDeletedEventData:`

      - `required string ID`

        ID of the environment that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "environment.deleted"`

      - `required string WorkspaceID`

    - `class BetaWebhookMemoryStoreCreatedEventData:`

      - `required string ID`

        ID of the memory store that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "memory_store.created"`

      - `required string WorkspaceID`

    - `class BetaWebhookMemoryStoreArchivedEventData:`

      - `required string ID`

        ID of the memory store that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "memory_store.archived"`

      - `required string WorkspaceID`

    - `class BetaWebhookMemoryStoreDeletedEventData:`

      - `required string ID`

        ID of the memory store that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "memory_store.deleted"`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionBudgetReachedEventData:`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `JsonElement Type = "session.budget_reached"`

      - `required string WorkspaceID`

  - `JsonElement Type = "event"`

    Object type. Always `event` for webhook payloads.

### Beta Webhook Event Data

- `class BetaWebhookEventData: union`

  - `class BetaWebhookSessionCreatedEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "session.created"`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionPendingEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "session.pending"`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionRunningEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "session.running"`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionIdledEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "session.idled"`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionRequiresActionEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "session.requires_action"`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionArchivedEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "session.archived"`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionDeletedEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "session.deleted"`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionStatusRescheduledEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "session.status_rescheduled"`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionStatusRunStartedEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "session.status_run_started"`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionStatusIdledEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "session.status_idled"`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionStatusTerminatedEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "session.status_terminated"`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionThreadCreatedEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `required string SessionThreadID`

      ID of the session thread this event refers to.

    - `JsonElement Type = "session.thread_created"`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionThreadIdledEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `required string SessionThreadID`

      ID of the session thread this event refers to.

    - `JsonElement Type = "session.thread_idled"`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionThreadTerminatedEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `required string SessionThreadID`

      ID of the session thread this event refers to.

    - `JsonElement Type = "session.thread_terminated"`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionOutcomeEvaluationEndedEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "session.outcome_evaluation_ended"`

    - `required string WorkspaceID`

  - `class BetaWebhookVaultCreatedEventData:`

    - `required string ID`

      ID of the vault that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "vault.created"`

    - `required string WorkspaceID`

  - `class BetaWebhookVaultArchivedEventData:`

    - `required string ID`

      ID of the vault that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "vault.archived"`

    - `required string WorkspaceID`

  - `class BetaWebhookVaultDeletedEventData:`

    - `required string ID`

      ID of the vault that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "vault.deleted"`

    - `required string WorkspaceID`

  - `class BetaWebhookVaultCredentialCreatedEventData:`

    - `required string ID`

      ID of the vault credential that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "vault_credential.created"`

    - `required string VaultID`

      ID of the vault that owns this credential.

    - `required string WorkspaceID`

  - `class BetaWebhookVaultCredentialArchivedEventData:`

    - `required string ID`

      ID of the vault credential that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "vault_credential.archived"`

    - `required string VaultID`

      ID of the vault that owns this credential.

    - `required string WorkspaceID`

  - `class BetaWebhookVaultCredentialDeletedEventData:`

    - `required string ID`

      ID of the vault credential that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "vault_credential.deleted"`

    - `required string VaultID`

      ID of the vault that owns this credential.

    - `required string WorkspaceID`

  - `class BetaWebhookVaultCredentialRefreshFailedEventData:`

    - `required string ID`

      ID of the vault credential that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "vault_credential.refresh_failed"`

    - `required string VaultID`

      ID of the vault that owns this credential.

    - `required string WorkspaceID`

  - `class BetaWebhookSessionUpdatedEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "session.updated"`

    - `required string WorkspaceID`

  - `class BetaWebhookAgentCreatedEventData:`

    - `required string ID`

      ID of the agent that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "agent.created"`

    - `required string WorkspaceID`

  - `class BetaWebhookAgentArchivedEventData:`

    - `required string ID`

      ID of the agent that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "agent.archived"`

    - `required string WorkspaceID`

  - `class BetaWebhookAgentDeletedEventData:`

    - `required string ID`

      ID of the agent that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "agent.deleted"`

    - `required string WorkspaceID`

  - `class BetaWebhookDeploymentPausedEventData:`

    - `required string ID`

      ID of the deployment that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "deployment.paused"`

    - `required string WorkspaceID`

  - `class BetaWebhookDeploymentRunFailedEventData:`

    - `required string ID`

      ID of the deployment run that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "deployment_run.failed"`

    - `required string WorkspaceID`

  - `class BetaWebhookDeploymentCreatedEventData:`

    - `required string ID`

      ID of the deployment that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "deployment.created"`

    - `required string WorkspaceID`

  - `class BetaWebhookDeploymentUpdatedEventData:`

    - `required string ID`

      ID of the deployment that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "deployment.updated"`

    - `required string WorkspaceID`

  - `class BetaWebhookDeploymentUnpausedEventData:`

    - `required string ID`

      ID of the deployment that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "deployment.unpaused"`

    - `required string WorkspaceID`

  - `class BetaWebhookAgentUpdatedEventData:`

    - `required string ID`

      ID of the agent that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "agent.updated"`

    - `required string WorkspaceID`

  - `class BetaWebhookDeploymentArchivedEventData:`

    - `required string ID`

      ID of the deployment that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "deployment.archived"`

    - `required string WorkspaceID`

  - `class BetaWebhookDeploymentRunStartedEventData:`

    - `required string ID`

      ID of the deployment run that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "deployment_run.started"`

    - `required string WorkspaceID`

  - `class BetaWebhookDeploymentDeletedEventData:`

    - `required string ID`

      ID of the deployment that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "deployment.deleted"`

    - `required string WorkspaceID`

  - `class BetaWebhookDeploymentRunSucceededEventData:`

    - `required string ID`

      ID of the deployment run that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "deployment_run.succeeded"`

    - `required string WorkspaceID`

  - `class BetaWebhookEnvironmentCreatedEventData:`

    - `required string ID`

      ID of the environment that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "environment.created"`

    - `required string WorkspaceID`

  - `class BetaWebhookEnvironmentUpdatedEventData:`

    - `required string ID`

      ID of the environment that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "environment.updated"`

    - `required string WorkspaceID`

  - `class BetaWebhookEnvironmentArchivedEventData:`

    - `required string ID`

      ID of the environment that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "environment.archived"`

    - `required string WorkspaceID`

  - `class BetaWebhookEnvironmentDeletedEventData:`

    - `required string ID`

      ID of the environment that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "environment.deleted"`

    - `required string WorkspaceID`

  - `class BetaWebhookMemoryStoreCreatedEventData:`

    - `required string ID`

      ID of the memory store that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "memory_store.created"`

    - `required string WorkspaceID`

  - `class BetaWebhookMemoryStoreArchivedEventData:`

    - `required string ID`

      ID of the memory store that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "memory_store.archived"`

    - `required string WorkspaceID`

  - `class BetaWebhookMemoryStoreDeletedEventData:`

    - `required string ID`

      ID of the memory store that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "memory_store.deleted"`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionBudgetReachedEventData:`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `JsonElement Type = "session.budget_reached"`

    - `required string WorkspaceID`

### Beta Webhook Memory Store Archived Event Data

- `class BetaWebhookMemoryStoreArchivedEventData:`

  - `required string ID`

    ID of the memory store that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "memory_store.archived"`

  - `required string WorkspaceID`

### Beta Webhook Memory Store Created Event Data

- `class BetaWebhookMemoryStoreCreatedEventData:`

  - `required string ID`

    ID of the memory store that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "memory_store.created"`

  - `required string WorkspaceID`

### Beta Webhook Memory Store Deleted Event Data

- `class BetaWebhookMemoryStoreDeletedEventData:`

  - `required string ID`

    ID of the memory store that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "memory_store.deleted"`

  - `required string WorkspaceID`

### Beta Webhook Session Archived Event Data

- `class BetaWebhookSessionArchivedEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "session.archived"`

  - `required string WorkspaceID`

### Beta Webhook Session Budget Reached Event Data

- `class BetaWebhookSessionBudgetReachedEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "session.budget_reached"`

  - `required string WorkspaceID`

### Beta Webhook Session Created Event Data

- `class BetaWebhookSessionCreatedEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "session.created"`

  - `required string WorkspaceID`

### Beta Webhook Session Deleted Event Data

- `class BetaWebhookSessionDeletedEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "session.deleted"`

  - `required string WorkspaceID`

### Beta Webhook Session Idled Event Data

- `class BetaWebhookSessionIdledEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "session.idled"`

  - `required string WorkspaceID`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `class BetaWebhookSessionOutcomeEvaluationEndedEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "session.outcome_evaluation_ended"`

  - `required string WorkspaceID`

### Beta Webhook Session Pending Event Data

- `class BetaWebhookSessionPendingEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "session.pending"`

  - `required string WorkspaceID`

### Beta Webhook Session Requires Action Event Data

- `class BetaWebhookSessionRequiresActionEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "session.requires_action"`

  - `required string WorkspaceID`

### Beta Webhook Session Running Event Data

- `class BetaWebhookSessionRunningEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "session.running"`

  - `required string WorkspaceID`

### Beta Webhook Session Status Idled Event Data

- `class BetaWebhookSessionStatusIdledEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "session.status_idled"`

  - `required string WorkspaceID`

### Beta Webhook Session Status Rescheduled Event Data

- `class BetaWebhookSessionStatusRescheduledEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "session.status_rescheduled"`

  - `required string WorkspaceID`

### Beta Webhook Session Status Run Started Event Data

- `class BetaWebhookSessionStatusRunStartedEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "session.status_run_started"`

  - `required string WorkspaceID`

### Beta Webhook Session Status Terminated Event Data

- `class BetaWebhookSessionStatusTerminatedEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "session.status_terminated"`

  - `required string WorkspaceID`

### Beta Webhook Session Thread Created Event Data

- `class BetaWebhookSessionThreadCreatedEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `required string SessionThreadID`

    ID of the session thread this event refers to.

  - `JsonElement Type = "session.thread_created"`

  - `required string WorkspaceID`

### Beta Webhook Session Thread Idled Event Data

- `class BetaWebhookSessionThreadIdledEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `required string SessionThreadID`

    ID of the session thread this event refers to.

  - `JsonElement Type = "session.thread_idled"`

  - `required string WorkspaceID`

### Beta Webhook Session Thread Terminated Event Data

- `class BetaWebhookSessionThreadTerminatedEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `required string SessionThreadID`

    ID of the session thread this event refers to.

  - `JsonElement Type = "session.thread_terminated"`

  - `required string WorkspaceID`

### Beta Webhook Session Updated Event Data

- `class BetaWebhookSessionUpdatedEventData:`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "session.updated"`

  - `required string WorkspaceID`

### Beta Webhook Vault Archived Event Data

- `class BetaWebhookVaultArchivedEventData:`

  - `required string ID`

    ID of the vault that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "vault.archived"`

  - `required string WorkspaceID`

### Beta Webhook Vault Created Event Data

- `class BetaWebhookVaultCreatedEventData:`

  - `required string ID`

    ID of the vault that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "vault.created"`

  - `required string WorkspaceID`

### Beta Webhook Vault Credential Archived Event Data

- `class BetaWebhookVaultCredentialArchivedEventData:`

  - `required string ID`

    ID of the vault credential that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "vault_credential.archived"`

  - `required string VaultID`

    ID of the vault that owns this credential.

  - `required string WorkspaceID`

### Beta Webhook Vault Credential Created Event Data

- `class BetaWebhookVaultCredentialCreatedEventData:`

  - `required string ID`

    ID of the vault credential that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "vault_credential.created"`

  - `required string VaultID`

    ID of the vault that owns this credential.

  - `required string WorkspaceID`

### Beta Webhook Vault Credential Deleted Event Data

- `class BetaWebhookVaultCredentialDeletedEventData:`

  - `required string ID`

    ID of the vault credential that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "vault_credential.deleted"`

  - `required string VaultID`

    ID of the vault that owns this credential.

  - `required string WorkspaceID`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `class BetaWebhookVaultCredentialRefreshFailedEventData:`

  - `required string ID`

    ID of the vault credential that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "vault_credential.refresh_failed"`

  - `required string VaultID`

    ID of the vault that owns this credential.

  - `required string WorkspaceID`

### Beta Webhook Vault Deleted Event Data

- `class BetaWebhookVaultDeletedEventData:`

  - `required string ID`

    ID of the vault that triggered the event.

  - `required string OrganizationID`

  - `JsonElement Type = "vault.deleted"`

  - `required string WorkspaceID`
