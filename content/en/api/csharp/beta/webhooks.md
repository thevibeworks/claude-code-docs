---
title: Webhooks
url: https://platform.claude.com/docs/en/api/csharp/beta/webhooks
---

# Webhooks

## Domain types

### Beta Webhook Agent Archived Event Data

- `class BetaWebhookAgentArchivedEventData:`

  - `JsonElement Type = "agent.archived"`

  - `required string ID`

    ID of the agent that triggered the event.

  - `required string OrganizationID`

  - `required string WorkspaceID`

### Beta Webhook Agent Created Event Data

- `class BetaWebhookAgentCreatedEventData:`

  - `JsonElement Type = "agent.created"`

  - `required string ID`

    ID of the agent that triggered the event.

  - `required string OrganizationID`

  - `required string WorkspaceID`

### Beta Webhook Agent Deleted Event Data

- `class BetaWebhookAgentDeletedEventData:`

  - `JsonElement Type = "agent.deleted"`

  - `required string ID`

    ID of the agent that triggered the event.

  - `required string OrganizationID`

  - `required string WorkspaceID`

### Beta Webhook Agent Updated Event Data

- `class BetaWebhookAgentUpdatedEventData:`

  - `JsonElement Type = "agent.updated"`

  - `required string ID`

    ID of the agent that triggered the event.

  - `required string OrganizationID`

  - `required string WorkspaceID`

### Beta Webhook Deployment Archived Event Data

- `class BetaWebhookDeploymentArchivedEventData:`

  - `JsonElement Type = "deployment.archived"`

  - `required string ID`

    ID of the deployment that triggered the event.

  - `required string OrganizationID`

  - `required string WorkspaceID`

### Beta Webhook Deployment Created Event Data

- `class BetaWebhookDeploymentCreatedEventData:`

  - `JsonElement Type = "deployment.created"`

  - `required string ID`

    ID of the deployment that triggered the event.

  - `required string OrganizationID`

  - `required string WorkspaceID`

### Beta Webhook Deployment Deleted Event Data

- `class BetaWebhookDeploymentDeletedEventData:`

  - `JsonElement Type = "deployment.deleted"`

  - `required string ID`

    ID of the deployment that triggered the event.

  - `required string OrganizationID`

  - `required string WorkspaceID`

### Beta Webhook Deployment Paused Event Data

- `class BetaWebhookDeploymentPausedEventData:`

  - `JsonElement Type = "deployment.paused"`

  - `required string ID`

    ID of the deployment that triggered the event.

  - `required string OrganizationID`

  - `required string WorkspaceID`

### Beta Webhook Deployment Run Failed Event Data

- `class BetaWebhookDeploymentRunFailedEventData:`

  - `JsonElement Type = "deployment_run.failed"`

  - `required string ID`

    ID of the deployment run that triggered the event.

  - `required string OrganizationID`

  - `required string WorkspaceID`

### Beta Webhook Deployment Run Started Event Data

- `class BetaWebhookDeploymentRunStartedEventData:`

  - `JsonElement Type = "deployment_run.started"`

  - `required string ID`

    ID of the deployment run that triggered the event.

  - `required string OrganizationID`

  - `required string WorkspaceID`

### Beta Webhook Deployment Run Succeeded Event Data

- `class BetaWebhookDeploymentRunSucceededEventData:`

  - `JsonElement Type = "deployment_run.succeeded"`

  - `required string ID`

    ID of the deployment run that triggered the event.

  - `required string OrganizationID`

  - `required string WorkspaceID`

### Beta Webhook Deployment Unpaused Event Data

- `class BetaWebhookDeploymentUnpausedEventData:`

  - `JsonElement Type = "deployment.unpaused"`

  - `required string ID`

    ID of the deployment that triggered the event.

  - `required string OrganizationID`

  - `required string WorkspaceID`

### Beta Webhook Deployment Updated Event Data

- `class BetaWebhookDeploymentUpdatedEventData:`

  - `JsonElement Type = "deployment.updated"`

  - `required string ID`

    ID of the deployment that triggered the event.

  - `required string OrganizationID`

  - `required string WorkspaceID`

### Beta Webhook Environment Archived Event Data

- `class BetaWebhookEnvironmentArchivedEventData:`

  - `JsonElement Type = "environment.archived"`

  - `required string ID`

    ID of the environment that triggered the event.

  - `required string OrganizationID`

  - `required string WorkspaceID`

### Beta Webhook Environment Created Event Data

- `class BetaWebhookEnvironmentCreatedEventData:`

  - `JsonElement Type = "environment.created"`

  - `required string ID`

    ID of the environment that triggered the event.

  - `required string OrganizationID`

  - `required string WorkspaceID`

### Beta Webhook Environment Deleted Event Data

- `class BetaWebhookEnvironmentDeletedEventData:`

  - `JsonElement Type = "environment.deleted"`

  - `required string ID`

    ID of the environment that triggered the event.

  - `required string OrganizationID`

  - `required string WorkspaceID`

### Beta Webhook Environment Updated Event Data

- `class BetaWebhookEnvironmentUpdatedEventData:`

  - `JsonElement Type = "environment.updated"`

  - `required string ID`

    ID of the environment that triggered the event.

  - `required string OrganizationID`

  - `required string WorkspaceID`

### Beta Webhook Event

- `class UnwrapWebhookEvent:`

  - `JsonElement Type = "event"`

    Object type. Always `event` for webhook payloads.

  - `required string ID`

    Unique event identifier for idempotency.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 timestamp when the event occurred.

    format: date-time

  - `required BetaWebhookEventData Data`

    - `class BetaWebhookSessionCreatedEventData:`

      - `JsonElement Type = "session.created"`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionPendingEventData:`

      - `JsonElement Type = "session.pending"`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionRunningEventData:`

      - `JsonElement Type = "session.running"`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionIdledEventData:`

      - `JsonElement Type = "session.idled"`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionRequiresActionEventData:`

      - `JsonElement Type = "session.requires_action"`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionArchivedEventData:`

      - `JsonElement Type = "session.archived"`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionDeletedEventData:`

      - `JsonElement Type = "session.deleted"`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionStatusRescheduledEventData:`

      - `JsonElement Type = "session.status_rescheduled"`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionStatusRunStartedEventData:`

      - `JsonElement Type = "session.status_run_started"`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionStatusIdledEventData:`

      - `JsonElement Type = "session.status_idled"`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionStatusTerminatedEventData:`

      - `JsonElement Type = "session.status_terminated"`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionThreadCreatedEventData:`

      - `JsonElement Type = "session.thread_created"`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `required string SessionThreadID`

        ID of the session thread this event refers to.

      - `required string WorkspaceID`

    - `class BetaWebhookSessionThreadIdledEventData:`

      - `JsonElement Type = "session.thread_idled"`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `required string SessionThreadID`

        ID of the session thread this event refers to.

      - `required string WorkspaceID`

    - `class BetaWebhookSessionThreadTerminatedEventData:`

      - `JsonElement Type = "session.thread_terminated"`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `required string SessionThreadID`

        ID of the session thread this event refers to.

      - `required string WorkspaceID`

    - `class BetaWebhookSessionOutcomeEvaluationEndedEventData:`

      - `JsonElement Type = "session.outcome_evaluation_ended"`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `required string WorkspaceID`

    - `class BetaWebhookVaultCreatedEventData:`

      - `JsonElement Type = "vault.created"`

      - `required string ID`

        ID of the vault that triggered the event.

      - `required string OrganizationID`

      - `required string WorkspaceID`

    - `class BetaWebhookVaultArchivedEventData:`

      - `JsonElement Type = "vault.archived"`

      - `required string ID`

        ID of the vault that triggered the event.

      - `required string OrganizationID`

      - `required string WorkspaceID`

    - `class BetaWebhookVaultDeletedEventData:`

      - `JsonElement Type = "vault.deleted"`

      - `required string ID`

        ID of the vault that triggered the event.

      - `required string OrganizationID`

      - `required string WorkspaceID`

    - `class BetaWebhookVaultCredentialCreatedEventData:`

      - `JsonElement Type = "vault_credential.created"`

      - `required string ID`

        ID of the vault credential that triggered the event.

      - `required string OrganizationID`

      - `required string VaultID`

        ID of the vault that owns this credential.

      - `required string WorkspaceID`

    - `class BetaWebhookVaultCredentialArchivedEventData:`

      - `JsonElement Type = "vault_credential.archived"`

      - `required string ID`

        ID of the vault credential that triggered the event.

      - `required string OrganizationID`

      - `required string VaultID`

        ID of the vault that owns this credential.

      - `required string WorkspaceID`

    - `class BetaWebhookVaultCredentialDeletedEventData:`

      - `JsonElement Type = "vault_credential.deleted"`

      - `required string ID`

        ID of the vault credential that triggered the event.

      - `required string OrganizationID`

      - `required string VaultID`

        ID of the vault that owns this credential.

      - `required string WorkspaceID`

    - `class BetaWebhookVaultCredentialRefreshFailedEventData:`

      - `JsonElement Type = "vault_credential.refresh_failed"`

      - `required string ID`

        ID of the vault credential that triggered the event.

      - `required string OrganizationID`

      - `required string VaultID`

        ID of the vault that owns this credential.

      - `required string WorkspaceID`

    - `class BetaWebhookSessionUpdatedEventData:`

      - `JsonElement Type = "session.updated"`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `required string WorkspaceID`

    - `class BetaWebhookAgentCreatedEventData:`

      - `JsonElement Type = "agent.created"`

      - `required string ID`

        ID of the agent that triggered the event.

      - `required string OrganizationID`

      - `required string WorkspaceID`

    - `class BetaWebhookAgentArchivedEventData:`

      - `JsonElement Type = "agent.archived"`

      - `required string ID`

        ID of the agent that triggered the event.

      - `required string OrganizationID`

      - `required string WorkspaceID`

    - `class BetaWebhookAgentDeletedEventData:`

      - `JsonElement Type = "agent.deleted"`

      - `required string ID`

        ID of the agent that triggered the event.

      - `required string OrganizationID`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentPausedEventData:`

      - `JsonElement Type = "deployment.paused"`

      - `required string ID`

        ID of the deployment that triggered the event.

      - `required string OrganizationID`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentRunFailedEventData:`

      - `JsonElement Type = "deployment_run.failed"`

      - `required string ID`

        ID of the deployment run that triggered the event.

      - `required string OrganizationID`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentCreatedEventData:`

      - `JsonElement Type = "deployment.created"`

      - `required string ID`

        ID of the deployment that triggered the event.

      - `required string OrganizationID`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentUpdatedEventData:`

      - `JsonElement Type = "deployment.updated"`

      - `required string ID`

        ID of the deployment that triggered the event.

      - `required string OrganizationID`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentUnpausedEventData:`

      - `JsonElement Type = "deployment.unpaused"`

      - `required string ID`

        ID of the deployment that triggered the event.

      - `required string OrganizationID`

      - `required string WorkspaceID`

    - `class BetaWebhookAgentUpdatedEventData:`

      - `JsonElement Type = "agent.updated"`

      - `required string ID`

        ID of the agent that triggered the event.

      - `required string OrganizationID`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentArchivedEventData:`

      - `JsonElement Type = "deployment.archived"`

      - `required string ID`

        ID of the deployment that triggered the event.

      - `required string OrganizationID`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentRunStartedEventData:`

      - `JsonElement Type = "deployment_run.started"`

      - `required string ID`

        ID of the deployment run that triggered the event.

      - `required string OrganizationID`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentDeletedEventData:`

      - `JsonElement Type = "deployment.deleted"`

      - `required string ID`

        ID of the deployment that triggered the event.

      - `required string OrganizationID`

      - `required string WorkspaceID`

    - `class BetaWebhookDeploymentRunSucceededEventData:`

      - `JsonElement Type = "deployment_run.succeeded"`

      - `required string ID`

        ID of the deployment run that triggered the event.

      - `required string OrganizationID`

      - `required string WorkspaceID`

    - `class BetaWebhookEnvironmentCreatedEventData:`

      - `JsonElement Type = "environment.created"`

      - `required string ID`

        ID of the environment that triggered the event.

      - `required string OrganizationID`

      - `required string WorkspaceID`

    - `class BetaWebhookEnvironmentUpdatedEventData:`

      - `JsonElement Type = "environment.updated"`

      - `required string ID`

        ID of the environment that triggered the event.

      - `required string OrganizationID`

      - `required string WorkspaceID`

    - `class BetaWebhookEnvironmentArchivedEventData:`

      - `JsonElement Type = "environment.archived"`

      - `required string ID`

        ID of the environment that triggered the event.

      - `required string OrganizationID`

      - `required string WorkspaceID`

    - `class BetaWebhookEnvironmentDeletedEventData:`

      - `JsonElement Type = "environment.deleted"`

      - `required string ID`

        ID of the environment that triggered the event.

      - `required string OrganizationID`

      - `required string WorkspaceID`

    - `class BetaWebhookMemoryStoreCreatedEventData:`

      - `JsonElement Type = "memory_store.created"`

      - `required string ID`

        ID of the memory store that triggered the event.

      - `required string OrganizationID`

      - `required string WorkspaceID`

    - `class BetaWebhookMemoryStoreArchivedEventData:`

      - `JsonElement Type = "memory_store.archived"`

      - `required string ID`

        ID of the memory store that triggered the event.

      - `required string OrganizationID`

      - `required string WorkspaceID`

    - `class BetaWebhookMemoryStoreDeletedEventData:`

      - `JsonElement Type = "memory_store.deleted"`

      - `required string ID`

        ID of the memory store that triggered the event.

      - `required string OrganizationID`

      - `required string WorkspaceID`

    - `class BetaWebhookSessionBudgetReachedEventData:`

      - `JsonElement Type = "session.budget_reached"`

      - `required string ID`

        ID of the session that triggered the event.

      - `required string OrganizationID`

      - `required string WorkspaceID`

### Beta Webhook Event Data

- `class BetaWebhookEventData: union`

  - `class BetaWebhookSessionCreatedEventData:`

    - `JsonElement Type = "session.created"`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionPendingEventData:`

    - `JsonElement Type = "session.pending"`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionRunningEventData:`

    - `JsonElement Type = "session.running"`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionIdledEventData:`

    - `JsonElement Type = "session.idled"`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionRequiresActionEventData:`

    - `JsonElement Type = "session.requires_action"`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionArchivedEventData:`

    - `JsonElement Type = "session.archived"`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionDeletedEventData:`

    - `JsonElement Type = "session.deleted"`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionStatusRescheduledEventData:`

    - `JsonElement Type = "session.status_rescheduled"`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionStatusRunStartedEventData:`

    - `JsonElement Type = "session.status_run_started"`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionStatusIdledEventData:`

    - `JsonElement Type = "session.status_idled"`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionStatusTerminatedEventData:`

    - `JsonElement Type = "session.status_terminated"`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionThreadCreatedEventData:`

    - `JsonElement Type = "session.thread_created"`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `required string SessionThreadID`

      ID of the session thread this event refers to.

    - `required string WorkspaceID`

  - `class BetaWebhookSessionThreadIdledEventData:`

    - `JsonElement Type = "session.thread_idled"`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `required string SessionThreadID`

      ID of the session thread this event refers to.

    - `required string WorkspaceID`

  - `class BetaWebhookSessionThreadTerminatedEventData:`

    - `JsonElement Type = "session.thread_terminated"`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `required string SessionThreadID`

      ID of the session thread this event refers to.

    - `required string WorkspaceID`

  - `class BetaWebhookSessionOutcomeEvaluationEndedEventData:`

    - `JsonElement Type = "session.outcome_evaluation_ended"`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `required string WorkspaceID`

  - `class BetaWebhookVaultCreatedEventData:`

    - `JsonElement Type = "vault.created"`

    - `required string ID`

      ID of the vault that triggered the event.

    - `required string OrganizationID`

    - `required string WorkspaceID`

  - `class BetaWebhookVaultArchivedEventData:`

    - `JsonElement Type = "vault.archived"`

    - `required string ID`

      ID of the vault that triggered the event.

    - `required string OrganizationID`

    - `required string WorkspaceID`

  - `class BetaWebhookVaultDeletedEventData:`

    - `JsonElement Type = "vault.deleted"`

    - `required string ID`

      ID of the vault that triggered the event.

    - `required string OrganizationID`

    - `required string WorkspaceID`

  - `class BetaWebhookVaultCredentialCreatedEventData:`

    - `JsonElement Type = "vault_credential.created"`

    - `required string ID`

      ID of the vault credential that triggered the event.

    - `required string OrganizationID`

    - `required string VaultID`

      ID of the vault that owns this credential.

    - `required string WorkspaceID`

  - `class BetaWebhookVaultCredentialArchivedEventData:`

    - `JsonElement Type = "vault_credential.archived"`

    - `required string ID`

      ID of the vault credential that triggered the event.

    - `required string OrganizationID`

    - `required string VaultID`

      ID of the vault that owns this credential.

    - `required string WorkspaceID`

  - `class BetaWebhookVaultCredentialDeletedEventData:`

    - `JsonElement Type = "vault_credential.deleted"`

    - `required string ID`

      ID of the vault credential that triggered the event.

    - `required string OrganizationID`

    - `required string VaultID`

      ID of the vault that owns this credential.

    - `required string WorkspaceID`

  - `class BetaWebhookVaultCredentialRefreshFailedEventData:`

    - `JsonElement Type = "vault_credential.refresh_failed"`

    - `required string ID`

      ID of the vault credential that triggered the event.

    - `required string OrganizationID`

    - `required string VaultID`

      ID of the vault that owns this credential.

    - `required string WorkspaceID`

  - `class BetaWebhookSessionUpdatedEventData:`

    - `JsonElement Type = "session.updated"`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `required string WorkspaceID`

  - `class BetaWebhookAgentCreatedEventData:`

    - `JsonElement Type = "agent.created"`

    - `required string ID`

      ID of the agent that triggered the event.

    - `required string OrganizationID`

    - `required string WorkspaceID`

  - `class BetaWebhookAgentArchivedEventData:`

    - `JsonElement Type = "agent.archived"`

    - `required string ID`

      ID of the agent that triggered the event.

    - `required string OrganizationID`

    - `required string WorkspaceID`

  - `class BetaWebhookAgentDeletedEventData:`

    - `JsonElement Type = "agent.deleted"`

    - `required string ID`

      ID of the agent that triggered the event.

    - `required string OrganizationID`

    - `required string WorkspaceID`

  - `class BetaWebhookDeploymentPausedEventData:`

    - `JsonElement Type = "deployment.paused"`

    - `required string ID`

      ID of the deployment that triggered the event.

    - `required string OrganizationID`

    - `required string WorkspaceID`

  - `class BetaWebhookDeploymentRunFailedEventData:`

    - `JsonElement Type = "deployment_run.failed"`

    - `required string ID`

      ID of the deployment run that triggered the event.

    - `required string OrganizationID`

    - `required string WorkspaceID`

  - `class BetaWebhookDeploymentCreatedEventData:`

    - `JsonElement Type = "deployment.created"`

    - `required string ID`

      ID of the deployment that triggered the event.

    - `required string OrganizationID`

    - `required string WorkspaceID`

  - `class BetaWebhookDeploymentUpdatedEventData:`

    - `JsonElement Type = "deployment.updated"`

    - `required string ID`

      ID of the deployment that triggered the event.

    - `required string OrganizationID`

    - `required string WorkspaceID`

  - `class BetaWebhookDeploymentUnpausedEventData:`

    - `JsonElement Type = "deployment.unpaused"`

    - `required string ID`

      ID of the deployment that triggered the event.

    - `required string OrganizationID`

    - `required string WorkspaceID`

  - `class BetaWebhookAgentUpdatedEventData:`

    - `JsonElement Type = "agent.updated"`

    - `required string ID`

      ID of the agent that triggered the event.

    - `required string OrganizationID`

    - `required string WorkspaceID`

  - `class BetaWebhookDeploymentArchivedEventData:`

    - `JsonElement Type = "deployment.archived"`

    - `required string ID`

      ID of the deployment that triggered the event.

    - `required string OrganizationID`

    - `required string WorkspaceID`

  - `class BetaWebhookDeploymentRunStartedEventData:`

    - `JsonElement Type = "deployment_run.started"`

    - `required string ID`

      ID of the deployment run that triggered the event.

    - `required string OrganizationID`

    - `required string WorkspaceID`

  - `class BetaWebhookDeploymentDeletedEventData:`

    - `JsonElement Type = "deployment.deleted"`

    - `required string ID`

      ID of the deployment that triggered the event.

    - `required string OrganizationID`

    - `required string WorkspaceID`

  - `class BetaWebhookDeploymentRunSucceededEventData:`

    - `JsonElement Type = "deployment_run.succeeded"`

    - `required string ID`

      ID of the deployment run that triggered the event.

    - `required string OrganizationID`

    - `required string WorkspaceID`

  - `class BetaWebhookEnvironmentCreatedEventData:`

    - `JsonElement Type = "environment.created"`

    - `required string ID`

      ID of the environment that triggered the event.

    - `required string OrganizationID`

    - `required string WorkspaceID`

  - `class BetaWebhookEnvironmentUpdatedEventData:`

    - `JsonElement Type = "environment.updated"`

    - `required string ID`

      ID of the environment that triggered the event.

    - `required string OrganizationID`

    - `required string WorkspaceID`

  - `class BetaWebhookEnvironmentArchivedEventData:`

    - `JsonElement Type = "environment.archived"`

    - `required string ID`

      ID of the environment that triggered the event.

    - `required string OrganizationID`

    - `required string WorkspaceID`

  - `class BetaWebhookEnvironmentDeletedEventData:`

    - `JsonElement Type = "environment.deleted"`

    - `required string ID`

      ID of the environment that triggered the event.

    - `required string OrganizationID`

    - `required string WorkspaceID`

  - `class BetaWebhookMemoryStoreCreatedEventData:`

    - `JsonElement Type = "memory_store.created"`

    - `required string ID`

      ID of the memory store that triggered the event.

    - `required string OrganizationID`

    - `required string WorkspaceID`

  - `class BetaWebhookMemoryStoreArchivedEventData:`

    - `JsonElement Type = "memory_store.archived"`

    - `required string ID`

      ID of the memory store that triggered the event.

    - `required string OrganizationID`

    - `required string WorkspaceID`

  - `class BetaWebhookMemoryStoreDeletedEventData:`

    - `JsonElement Type = "memory_store.deleted"`

    - `required string ID`

      ID of the memory store that triggered the event.

    - `required string OrganizationID`

    - `required string WorkspaceID`

  - `class BetaWebhookSessionBudgetReachedEventData:`

    - `JsonElement Type = "session.budget_reached"`

    - `required string ID`

      ID of the session that triggered the event.

    - `required string OrganizationID`

    - `required string WorkspaceID`

### Beta Webhook Memory Store Archived Event Data

- `class BetaWebhookMemoryStoreArchivedEventData:`

  - `JsonElement Type = "memory_store.archived"`

  - `required string ID`

    ID of the memory store that triggered the event.

  - `required string OrganizationID`

  - `required string WorkspaceID`

### Beta Webhook Memory Store Created Event Data

- `class BetaWebhookMemoryStoreCreatedEventData:`

  - `JsonElement Type = "memory_store.created"`

  - `required string ID`

    ID of the memory store that triggered the event.

  - `required string OrganizationID`

  - `required string WorkspaceID`

### Beta Webhook Memory Store Deleted Event Data

- `class BetaWebhookMemoryStoreDeletedEventData:`

  - `JsonElement Type = "memory_store.deleted"`

  - `required string ID`

    ID of the memory store that triggered the event.

  - `required string OrganizationID`

  - `required string WorkspaceID`

### Beta Webhook Session Archived Event Data

- `class BetaWebhookSessionArchivedEventData:`

  - `JsonElement Type = "session.archived"`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `required string WorkspaceID`

### Beta Webhook Session Budget Reached Event Data

- `class BetaWebhookSessionBudgetReachedEventData:`

  - `JsonElement Type = "session.budget_reached"`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `required string WorkspaceID`

### Beta Webhook Session Created Event Data

- `class BetaWebhookSessionCreatedEventData:`

  - `JsonElement Type = "session.created"`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `required string WorkspaceID`

### Beta Webhook Session Deleted Event Data

- `class BetaWebhookSessionDeletedEventData:`

  - `JsonElement Type = "session.deleted"`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `required string WorkspaceID`

### Beta Webhook Session Idled Event Data

- `class BetaWebhookSessionIdledEventData:`

  - `JsonElement Type = "session.idled"`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `required string WorkspaceID`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `class BetaWebhookSessionOutcomeEvaluationEndedEventData:`

  - `JsonElement Type = "session.outcome_evaluation_ended"`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `required string WorkspaceID`

### Beta Webhook Session Pending Event Data

- `class BetaWebhookSessionPendingEventData:`

  - `JsonElement Type = "session.pending"`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `required string WorkspaceID`

### Beta Webhook Session Requires Action Event Data

- `class BetaWebhookSessionRequiresActionEventData:`

  - `JsonElement Type = "session.requires_action"`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `required string WorkspaceID`

### Beta Webhook Session Running Event Data

- `class BetaWebhookSessionRunningEventData:`

  - `JsonElement Type = "session.running"`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `required string WorkspaceID`

### Beta Webhook Session Status Idled Event Data

- `class BetaWebhookSessionStatusIdledEventData:`

  - `JsonElement Type = "session.status_idled"`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `required string WorkspaceID`

### Beta Webhook Session Status Rescheduled Event Data

- `class BetaWebhookSessionStatusRescheduledEventData:`

  - `JsonElement Type = "session.status_rescheduled"`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `required string WorkspaceID`

### Beta Webhook Session Status Run Started Event Data

- `class BetaWebhookSessionStatusRunStartedEventData:`

  - `JsonElement Type = "session.status_run_started"`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `required string WorkspaceID`

### Beta Webhook Session Status Terminated Event Data

- `class BetaWebhookSessionStatusTerminatedEventData:`

  - `JsonElement Type = "session.status_terminated"`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `required string WorkspaceID`

### Beta Webhook Session Thread Created Event Data

- `class BetaWebhookSessionThreadCreatedEventData:`

  - `JsonElement Type = "session.thread_created"`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `required string SessionThreadID`

    ID of the session thread this event refers to.

  - `required string WorkspaceID`

### Beta Webhook Session Thread Idled Event Data

- `class BetaWebhookSessionThreadIdledEventData:`

  - `JsonElement Type = "session.thread_idled"`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `required string SessionThreadID`

    ID of the session thread this event refers to.

  - `required string WorkspaceID`

### Beta Webhook Session Thread Terminated Event Data

- `class BetaWebhookSessionThreadTerminatedEventData:`

  - `JsonElement Type = "session.thread_terminated"`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `required string SessionThreadID`

    ID of the session thread this event refers to.

  - `required string WorkspaceID`

### Beta Webhook Session Updated Event Data

- `class BetaWebhookSessionUpdatedEventData:`

  - `JsonElement Type = "session.updated"`

  - `required string ID`

    ID of the session that triggered the event.

  - `required string OrganizationID`

  - `required string WorkspaceID`

### Beta Webhook Vault Archived Event Data

- `class BetaWebhookVaultArchivedEventData:`

  - `JsonElement Type = "vault.archived"`

  - `required string ID`

    ID of the vault that triggered the event.

  - `required string OrganizationID`

  - `required string WorkspaceID`

### Beta Webhook Vault Created Event Data

- `class BetaWebhookVaultCreatedEventData:`

  - `JsonElement Type = "vault.created"`

  - `required string ID`

    ID of the vault that triggered the event.

  - `required string OrganizationID`

  - `required string WorkspaceID`

### Beta Webhook Vault Credential Archived Event Data

- `class BetaWebhookVaultCredentialArchivedEventData:`

  - `JsonElement Type = "vault_credential.archived"`

  - `required string ID`

    ID of the vault credential that triggered the event.

  - `required string OrganizationID`

  - `required string VaultID`

    ID of the vault that owns this credential.

  - `required string WorkspaceID`

### Beta Webhook Vault Credential Created Event Data

- `class BetaWebhookVaultCredentialCreatedEventData:`

  - `JsonElement Type = "vault_credential.created"`

  - `required string ID`

    ID of the vault credential that triggered the event.

  - `required string OrganizationID`

  - `required string VaultID`

    ID of the vault that owns this credential.

  - `required string WorkspaceID`

### Beta Webhook Vault Credential Deleted Event Data

- `class BetaWebhookVaultCredentialDeletedEventData:`

  - `JsonElement Type = "vault_credential.deleted"`

  - `required string ID`

    ID of the vault credential that triggered the event.

  - `required string OrganizationID`

  - `required string VaultID`

    ID of the vault that owns this credential.

  - `required string WorkspaceID`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `class BetaWebhookVaultCredentialRefreshFailedEventData:`

  - `JsonElement Type = "vault_credential.refresh_failed"`

  - `required string ID`

    ID of the vault credential that triggered the event.

  - `required string OrganizationID`

  - `required string VaultID`

    ID of the vault that owns this credential.

  - `required string WorkspaceID`

### Beta Webhook Vault Deleted Event Data

- `class BetaWebhookVaultDeletedEventData:`

  - `JsonElement Type = "vault.deleted"`

  - `required string ID`

    ID of the vault that triggered the event.

  - `required string OrganizationID`

  - `required string WorkspaceID`
