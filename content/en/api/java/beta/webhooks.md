---
title: Webhooks
url: https://platform.claude.com/docs/en/api/java/beta/webhooks
---

# Webhooks

## Domain types

### Beta Webhook Agent Archived Event Data

- `class BetaWebhookAgentArchivedEventData:`

  - `JsonValue type = "agent.archived"`

  - `String id`

    ID of the agent that triggered the event.

  - `String organizationId`

  - `String workspaceId`

### Beta Webhook Agent Created Event Data

- `class BetaWebhookAgentCreatedEventData:`

  - `JsonValue type = "agent.created"`

  - `String id`

    ID of the agent that triggered the event.

  - `String organizationId`

  - `String workspaceId`

### Beta Webhook Agent Deleted Event Data

- `class BetaWebhookAgentDeletedEventData:`

  - `JsonValue type = "agent.deleted"`

  - `String id`

    ID of the agent that triggered the event.

  - `String organizationId`

  - `String workspaceId`

### Beta Webhook Agent Updated Event Data

- `class BetaWebhookAgentUpdatedEventData:`

  - `JsonValue type = "agent.updated"`

  - `String id`

    ID of the agent that triggered the event.

  - `String organizationId`

  - `String workspaceId`

### Beta Webhook Deployment Archived Event Data

- `class BetaWebhookDeploymentArchivedEventData:`

  - `JsonValue type = "deployment.archived"`

  - `String id`

    ID of the deployment that triggered the event.

  - `String organizationId`

  - `String workspaceId`

### Beta Webhook Deployment Created Event Data

- `class BetaWebhookDeploymentCreatedEventData:`

  - `JsonValue type = "deployment.created"`

  - `String id`

    ID of the deployment that triggered the event.

  - `String organizationId`

  - `String workspaceId`

### Beta Webhook Deployment Deleted Event Data

- `class BetaWebhookDeploymentDeletedEventData:`

  - `JsonValue type = "deployment.deleted"`

  - `String id`

    ID of the deployment that triggered the event.

  - `String organizationId`

  - `String workspaceId`

### Beta Webhook Deployment Paused Event Data

- `class BetaWebhookDeploymentPausedEventData:`

  - `JsonValue type = "deployment.paused"`

  - `String id`

    ID of the deployment that triggered the event.

  - `String organizationId`

  - `String workspaceId`

### Beta Webhook Deployment Run Failed Event Data

- `class BetaWebhookDeploymentRunFailedEventData:`

  - `JsonValue type = "deployment_run.failed"`

  - `String id`

    ID of the deployment run that triggered the event.

  - `String organizationId`

  - `String workspaceId`

### Beta Webhook Deployment Run Started Event Data

- `class BetaWebhookDeploymentRunStartedEventData:`

  - `JsonValue type = "deployment_run.started"`

  - `String id`

    ID of the deployment run that triggered the event.

  - `String organizationId`

  - `String workspaceId`

### Beta Webhook Deployment Run Succeeded Event Data

- `class BetaWebhookDeploymentRunSucceededEventData:`

  - `JsonValue type = "deployment_run.succeeded"`

  - `String id`

    ID of the deployment run that triggered the event.

  - `String organizationId`

  - `String workspaceId`

### Beta Webhook Deployment Unpaused Event Data

- `class BetaWebhookDeploymentUnpausedEventData:`

  - `JsonValue type = "deployment.unpaused"`

  - `String id`

    ID of the deployment that triggered the event.

  - `String organizationId`

  - `String workspaceId`

### Beta Webhook Deployment Updated Event Data

- `class BetaWebhookDeploymentUpdatedEventData:`

  - `JsonValue type = "deployment.updated"`

  - `String id`

    ID of the deployment that triggered the event.

  - `String organizationId`

  - `String workspaceId`

### Beta Webhook Environment Archived Event Data

- `class BetaWebhookEnvironmentArchivedEventData:`

  - `JsonValue type = "environment.archived"`

  - `String id`

    ID of the environment that triggered the event.

  - `String organizationId`

  - `String workspaceId`

### Beta Webhook Environment Created Event Data

- `class BetaWebhookEnvironmentCreatedEventData:`

  - `JsonValue type = "environment.created"`

  - `String id`

    ID of the environment that triggered the event.

  - `String organizationId`

  - `String workspaceId`

### Beta Webhook Environment Deleted Event Data

- `class BetaWebhookEnvironmentDeletedEventData:`

  - `JsonValue type = "environment.deleted"`

  - `String id`

    ID of the environment that triggered the event.

  - `String organizationId`

  - `String workspaceId`

### Beta Webhook Environment Updated Event Data

- `class BetaWebhookEnvironmentUpdatedEventData:`

  - `JsonValue type = "environment.updated"`

  - `String id`

    ID of the environment that triggered the event.

  - `String organizationId`

  - `String workspaceId`

### Beta Webhook Event

- `class UnwrapWebhookEvent:`

  - `JsonValue type = "event"`

    Object type. Always `event` for webhook payloads.

  - `String id`

    Unique event identifier for idempotency.

  - `LocalDateTime createdAt`

    RFC 3339 timestamp when the event occurred.

    format: date-time

  - `BetaWebhookEventData data`

    - `class BetaWebhookSessionCreatedEventData:`

      - `JsonValue type = "session.created"`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookSessionPendingEventData:`

      - `JsonValue type = "session.pending"`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookSessionRunningEventData:`

      - `JsonValue type = "session.running"`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookSessionIdledEventData:`

      - `JsonValue type = "session.idled"`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookSessionRequiresActionEventData:`

      - `JsonValue type = "session.requires_action"`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookSessionArchivedEventData:`

      - `JsonValue type = "session.archived"`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookSessionDeletedEventData:`

      - `JsonValue type = "session.deleted"`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookSessionStatusRescheduledEventData:`

      - `JsonValue type = "session.status_rescheduled"`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookSessionStatusRunStartedEventData:`

      - `JsonValue type = "session.status_run_started"`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookSessionStatusIdledEventData:`

      - `JsonValue type = "session.status_idled"`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookSessionStatusTerminatedEventData:`

      - `JsonValue type = "session.status_terminated"`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookSessionThreadCreatedEventData:`

      - `JsonValue type = "session.thread_created"`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String sessionThreadId`

        ID of the session thread this event refers to.

      - `String workspaceId`

    - `class BetaWebhookSessionThreadIdledEventData:`

      - `JsonValue type = "session.thread_idled"`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String sessionThreadId`

        ID of the session thread this event refers to.

      - `String workspaceId`

    - `class BetaWebhookSessionThreadTerminatedEventData:`

      - `JsonValue type = "session.thread_terminated"`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String sessionThreadId`

        ID of the session thread this event refers to.

      - `String workspaceId`

    - `class BetaWebhookSessionOutcomeEvaluationEndedEventData:`

      - `JsonValue type = "session.outcome_evaluation_ended"`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookVaultCreatedEventData:`

      - `JsonValue type = "vault.created"`

      - `String id`

        ID of the vault that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookVaultArchivedEventData:`

      - `JsonValue type = "vault.archived"`

      - `String id`

        ID of the vault that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookVaultDeletedEventData:`

      - `JsonValue type = "vault.deleted"`

      - `String id`

        ID of the vault that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookVaultCredentialCreatedEventData:`

      - `JsonValue type = "vault_credential.created"`

      - `String id`

        ID of the vault credential that triggered the event.

      - `String organizationId`

      - `String vaultId`

        ID of the vault that owns this credential.

      - `String workspaceId`

    - `class BetaWebhookVaultCredentialArchivedEventData:`

      - `JsonValue type = "vault_credential.archived"`

      - `String id`

        ID of the vault credential that triggered the event.

      - `String organizationId`

      - `String vaultId`

        ID of the vault that owns this credential.

      - `String workspaceId`

    - `class BetaWebhookVaultCredentialDeletedEventData:`

      - `JsonValue type = "vault_credential.deleted"`

      - `String id`

        ID of the vault credential that triggered the event.

      - `String organizationId`

      - `String vaultId`

        ID of the vault that owns this credential.

      - `String workspaceId`

    - `class BetaWebhookVaultCredentialRefreshFailedEventData:`

      - `JsonValue type = "vault_credential.refresh_failed"`

      - `String id`

        ID of the vault credential that triggered the event.

      - `String organizationId`

      - `String vaultId`

        ID of the vault that owns this credential.

      - `String workspaceId`

    - `class BetaWebhookSessionUpdatedEventData:`

      - `JsonValue type = "session.updated"`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookAgentCreatedEventData:`

      - `JsonValue type = "agent.created"`

      - `String id`

        ID of the agent that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookAgentArchivedEventData:`

      - `JsonValue type = "agent.archived"`

      - `String id`

        ID of the agent that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookAgentDeletedEventData:`

      - `JsonValue type = "agent.deleted"`

      - `String id`

        ID of the agent that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookDeploymentPausedEventData:`

      - `JsonValue type = "deployment.paused"`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookDeploymentRunFailedEventData:`

      - `JsonValue type = "deployment_run.failed"`

      - `String id`

        ID of the deployment run that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookDeploymentCreatedEventData:`

      - `JsonValue type = "deployment.created"`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookDeploymentUpdatedEventData:`

      - `JsonValue type = "deployment.updated"`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookDeploymentUnpausedEventData:`

      - `JsonValue type = "deployment.unpaused"`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookAgentUpdatedEventData:`

      - `JsonValue type = "agent.updated"`

      - `String id`

        ID of the agent that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookDeploymentArchivedEventData:`

      - `JsonValue type = "deployment.archived"`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookDeploymentRunStartedEventData:`

      - `JsonValue type = "deployment_run.started"`

      - `String id`

        ID of the deployment run that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookDeploymentDeletedEventData:`

      - `JsonValue type = "deployment.deleted"`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookDeploymentRunSucceededEventData:`

      - `JsonValue type = "deployment_run.succeeded"`

      - `String id`

        ID of the deployment run that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookEnvironmentCreatedEventData:`

      - `JsonValue type = "environment.created"`

      - `String id`

        ID of the environment that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookEnvironmentUpdatedEventData:`

      - `JsonValue type = "environment.updated"`

      - `String id`

        ID of the environment that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookEnvironmentArchivedEventData:`

      - `JsonValue type = "environment.archived"`

      - `String id`

        ID of the environment that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookEnvironmentDeletedEventData:`

      - `JsonValue type = "environment.deleted"`

      - `String id`

        ID of the environment that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookMemoryStoreCreatedEventData:`

      - `JsonValue type = "memory_store.created"`

      - `String id`

        ID of the memory store that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookMemoryStoreArchivedEventData:`

      - `JsonValue type = "memory_store.archived"`

      - `String id`

        ID of the memory store that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookMemoryStoreDeletedEventData:`

      - `JsonValue type = "memory_store.deleted"`

      - `String id`

        ID of the memory store that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookSessionBudgetReachedEventData:`

      - `JsonValue type = "session.budget_reached"`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String workspaceId`

### Beta Webhook Event Data

- `class BetaWebhookEventData: union`

  - `class BetaWebhookSessionCreatedEventData:`

    - `JsonValue type = "session.created"`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `String workspaceId`

  - `class BetaWebhookSessionPendingEventData:`

    - `JsonValue type = "session.pending"`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `String workspaceId`

  - `class BetaWebhookSessionRunningEventData:`

    - `JsonValue type = "session.running"`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `String workspaceId`

  - `class BetaWebhookSessionIdledEventData:`

    - `JsonValue type = "session.idled"`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `String workspaceId`

  - `class BetaWebhookSessionRequiresActionEventData:`

    - `JsonValue type = "session.requires_action"`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `String workspaceId`

  - `class BetaWebhookSessionArchivedEventData:`

    - `JsonValue type = "session.archived"`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `String workspaceId`

  - `class BetaWebhookSessionDeletedEventData:`

    - `JsonValue type = "session.deleted"`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `String workspaceId`

  - `class BetaWebhookSessionStatusRescheduledEventData:`

    - `JsonValue type = "session.status_rescheduled"`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `String workspaceId`

  - `class BetaWebhookSessionStatusRunStartedEventData:`

    - `JsonValue type = "session.status_run_started"`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `String workspaceId`

  - `class BetaWebhookSessionStatusIdledEventData:`

    - `JsonValue type = "session.status_idled"`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `String workspaceId`

  - `class BetaWebhookSessionStatusTerminatedEventData:`

    - `JsonValue type = "session.status_terminated"`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `String workspaceId`

  - `class BetaWebhookSessionThreadCreatedEventData:`

    - `JsonValue type = "session.thread_created"`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `String sessionThreadId`

      ID of the session thread this event refers to.

    - `String workspaceId`

  - `class BetaWebhookSessionThreadIdledEventData:`

    - `JsonValue type = "session.thread_idled"`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `String sessionThreadId`

      ID of the session thread this event refers to.

    - `String workspaceId`

  - `class BetaWebhookSessionThreadTerminatedEventData:`

    - `JsonValue type = "session.thread_terminated"`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `String sessionThreadId`

      ID of the session thread this event refers to.

    - `String workspaceId`

  - `class BetaWebhookSessionOutcomeEvaluationEndedEventData:`

    - `JsonValue type = "session.outcome_evaluation_ended"`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `String workspaceId`

  - `class BetaWebhookVaultCreatedEventData:`

    - `JsonValue type = "vault.created"`

    - `String id`

      ID of the vault that triggered the event.

    - `String organizationId`

    - `String workspaceId`

  - `class BetaWebhookVaultArchivedEventData:`

    - `JsonValue type = "vault.archived"`

    - `String id`

      ID of the vault that triggered the event.

    - `String organizationId`

    - `String workspaceId`

  - `class BetaWebhookVaultDeletedEventData:`

    - `JsonValue type = "vault.deleted"`

    - `String id`

      ID of the vault that triggered the event.

    - `String organizationId`

    - `String workspaceId`

  - `class BetaWebhookVaultCredentialCreatedEventData:`

    - `JsonValue type = "vault_credential.created"`

    - `String id`

      ID of the vault credential that triggered the event.

    - `String organizationId`

    - `String vaultId`

      ID of the vault that owns this credential.

    - `String workspaceId`

  - `class BetaWebhookVaultCredentialArchivedEventData:`

    - `JsonValue type = "vault_credential.archived"`

    - `String id`

      ID of the vault credential that triggered the event.

    - `String organizationId`

    - `String vaultId`

      ID of the vault that owns this credential.

    - `String workspaceId`

  - `class BetaWebhookVaultCredentialDeletedEventData:`

    - `JsonValue type = "vault_credential.deleted"`

    - `String id`

      ID of the vault credential that triggered the event.

    - `String organizationId`

    - `String vaultId`

      ID of the vault that owns this credential.

    - `String workspaceId`

  - `class BetaWebhookVaultCredentialRefreshFailedEventData:`

    - `JsonValue type = "vault_credential.refresh_failed"`

    - `String id`

      ID of the vault credential that triggered the event.

    - `String organizationId`

    - `String vaultId`

      ID of the vault that owns this credential.

    - `String workspaceId`

  - `class BetaWebhookSessionUpdatedEventData:`

    - `JsonValue type = "session.updated"`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `String workspaceId`

  - `class BetaWebhookAgentCreatedEventData:`

    - `JsonValue type = "agent.created"`

    - `String id`

      ID of the agent that triggered the event.

    - `String organizationId`

    - `String workspaceId`

  - `class BetaWebhookAgentArchivedEventData:`

    - `JsonValue type = "agent.archived"`

    - `String id`

      ID of the agent that triggered the event.

    - `String organizationId`

    - `String workspaceId`

  - `class BetaWebhookAgentDeletedEventData:`

    - `JsonValue type = "agent.deleted"`

    - `String id`

      ID of the agent that triggered the event.

    - `String organizationId`

    - `String workspaceId`

  - `class BetaWebhookDeploymentPausedEventData:`

    - `JsonValue type = "deployment.paused"`

    - `String id`

      ID of the deployment that triggered the event.

    - `String organizationId`

    - `String workspaceId`

  - `class BetaWebhookDeploymentRunFailedEventData:`

    - `JsonValue type = "deployment_run.failed"`

    - `String id`

      ID of the deployment run that triggered the event.

    - `String organizationId`

    - `String workspaceId`

  - `class BetaWebhookDeploymentCreatedEventData:`

    - `JsonValue type = "deployment.created"`

    - `String id`

      ID of the deployment that triggered the event.

    - `String organizationId`

    - `String workspaceId`

  - `class BetaWebhookDeploymentUpdatedEventData:`

    - `JsonValue type = "deployment.updated"`

    - `String id`

      ID of the deployment that triggered the event.

    - `String organizationId`

    - `String workspaceId`

  - `class BetaWebhookDeploymentUnpausedEventData:`

    - `JsonValue type = "deployment.unpaused"`

    - `String id`

      ID of the deployment that triggered the event.

    - `String organizationId`

    - `String workspaceId`

  - `class BetaWebhookAgentUpdatedEventData:`

    - `JsonValue type = "agent.updated"`

    - `String id`

      ID of the agent that triggered the event.

    - `String organizationId`

    - `String workspaceId`

  - `class BetaWebhookDeploymentArchivedEventData:`

    - `JsonValue type = "deployment.archived"`

    - `String id`

      ID of the deployment that triggered the event.

    - `String organizationId`

    - `String workspaceId`

  - `class BetaWebhookDeploymentRunStartedEventData:`

    - `JsonValue type = "deployment_run.started"`

    - `String id`

      ID of the deployment run that triggered the event.

    - `String organizationId`

    - `String workspaceId`

  - `class BetaWebhookDeploymentDeletedEventData:`

    - `JsonValue type = "deployment.deleted"`

    - `String id`

      ID of the deployment that triggered the event.

    - `String organizationId`

    - `String workspaceId`

  - `class BetaWebhookDeploymentRunSucceededEventData:`

    - `JsonValue type = "deployment_run.succeeded"`

    - `String id`

      ID of the deployment run that triggered the event.

    - `String organizationId`

    - `String workspaceId`

  - `class BetaWebhookEnvironmentCreatedEventData:`

    - `JsonValue type = "environment.created"`

    - `String id`

      ID of the environment that triggered the event.

    - `String organizationId`

    - `String workspaceId`

  - `class BetaWebhookEnvironmentUpdatedEventData:`

    - `JsonValue type = "environment.updated"`

    - `String id`

      ID of the environment that triggered the event.

    - `String organizationId`

    - `String workspaceId`

  - `class BetaWebhookEnvironmentArchivedEventData:`

    - `JsonValue type = "environment.archived"`

    - `String id`

      ID of the environment that triggered the event.

    - `String organizationId`

    - `String workspaceId`

  - `class BetaWebhookEnvironmentDeletedEventData:`

    - `JsonValue type = "environment.deleted"`

    - `String id`

      ID of the environment that triggered the event.

    - `String organizationId`

    - `String workspaceId`

  - `class BetaWebhookMemoryStoreCreatedEventData:`

    - `JsonValue type = "memory_store.created"`

    - `String id`

      ID of the memory store that triggered the event.

    - `String organizationId`

    - `String workspaceId`

  - `class BetaWebhookMemoryStoreArchivedEventData:`

    - `JsonValue type = "memory_store.archived"`

    - `String id`

      ID of the memory store that triggered the event.

    - `String organizationId`

    - `String workspaceId`

  - `class BetaWebhookMemoryStoreDeletedEventData:`

    - `JsonValue type = "memory_store.deleted"`

    - `String id`

      ID of the memory store that triggered the event.

    - `String organizationId`

    - `String workspaceId`

  - `class BetaWebhookSessionBudgetReachedEventData:`

    - `JsonValue type = "session.budget_reached"`

    - `String id`

      ID of the session that triggered the event.

    - `String organizationId`

    - `String workspaceId`

### Beta Webhook Memory Store Archived Event Data

- `class BetaWebhookMemoryStoreArchivedEventData:`

  - `JsonValue type = "memory_store.archived"`

  - `String id`

    ID of the memory store that triggered the event.

  - `String organizationId`

  - `String workspaceId`

### Beta Webhook Memory Store Created Event Data

- `class BetaWebhookMemoryStoreCreatedEventData:`

  - `JsonValue type = "memory_store.created"`

  - `String id`

    ID of the memory store that triggered the event.

  - `String organizationId`

  - `String workspaceId`

### Beta Webhook Memory Store Deleted Event Data

- `class BetaWebhookMemoryStoreDeletedEventData:`

  - `JsonValue type = "memory_store.deleted"`

  - `String id`

    ID of the memory store that triggered the event.

  - `String organizationId`

  - `String workspaceId`

### Beta Webhook Session Archived Event Data

- `class BetaWebhookSessionArchivedEventData:`

  - `JsonValue type = "session.archived"`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `String workspaceId`

### Beta Webhook Session Budget Reached Event Data

- `class BetaWebhookSessionBudgetReachedEventData:`

  - `JsonValue type = "session.budget_reached"`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `String workspaceId`

### Beta Webhook Session Created Event Data

- `class BetaWebhookSessionCreatedEventData:`

  - `JsonValue type = "session.created"`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `String workspaceId`

### Beta Webhook Session Deleted Event Data

- `class BetaWebhookSessionDeletedEventData:`

  - `JsonValue type = "session.deleted"`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `String workspaceId`

### Beta Webhook Session Idled Event Data

- `class BetaWebhookSessionIdledEventData:`

  - `JsonValue type = "session.idled"`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `String workspaceId`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `class BetaWebhookSessionOutcomeEvaluationEndedEventData:`

  - `JsonValue type = "session.outcome_evaluation_ended"`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `String workspaceId`

### Beta Webhook Session Pending Event Data

- `class BetaWebhookSessionPendingEventData:`

  - `JsonValue type = "session.pending"`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `String workspaceId`

### Beta Webhook Session Requires Action Event Data

- `class BetaWebhookSessionRequiresActionEventData:`

  - `JsonValue type = "session.requires_action"`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `String workspaceId`

### Beta Webhook Session Running Event Data

- `class BetaWebhookSessionRunningEventData:`

  - `JsonValue type = "session.running"`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `String workspaceId`

### Beta Webhook Session Status Idled Event Data

- `class BetaWebhookSessionStatusIdledEventData:`

  - `JsonValue type = "session.status_idled"`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `String workspaceId`

### Beta Webhook Session Status Rescheduled Event Data

- `class BetaWebhookSessionStatusRescheduledEventData:`

  - `JsonValue type = "session.status_rescheduled"`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `String workspaceId`

### Beta Webhook Session Status Run Started Event Data

- `class BetaWebhookSessionStatusRunStartedEventData:`

  - `JsonValue type = "session.status_run_started"`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `String workspaceId`

### Beta Webhook Session Status Terminated Event Data

- `class BetaWebhookSessionStatusTerminatedEventData:`

  - `JsonValue type = "session.status_terminated"`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `String workspaceId`

### Beta Webhook Session Thread Created Event Data

- `class BetaWebhookSessionThreadCreatedEventData:`

  - `JsonValue type = "session.thread_created"`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `String sessionThreadId`

    ID of the session thread this event refers to.

  - `String workspaceId`

### Beta Webhook Session Thread Idled Event Data

- `class BetaWebhookSessionThreadIdledEventData:`

  - `JsonValue type = "session.thread_idled"`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `String sessionThreadId`

    ID of the session thread this event refers to.

  - `String workspaceId`

### Beta Webhook Session Thread Terminated Event Data

- `class BetaWebhookSessionThreadTerminatedEventData:`

  - `JsonValue type = "session.thread_terminated"`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `String sessionThreadId`

    ID of the session thread this event refers to.

  - `String workspaceId`

### Beta Webhook Session Updated Event Data

- `class BetaWebhookSessionUpdatedEventData:`

  - `JsonValue type = "session.updated"`

  - `String id`

    ID of the session that triggered the event.

  - `String organizationId`

  - `String workspaceId`

### Beta Webhook Vault Archived Event Data

- `class BetaWebhookVaultArchivedEventData:`

  - `JsonValue type = "vault.archived"`

  - `String id`

    ID of the vault that triggered the event.

  - `String organizationId`

  - `String workspaceId`

### Beta Webhook Vault Created Event Data

- `class BetaWebhookVaultCreatedEventData:`

  - `JsonValue type = "vault.created"`

  - `String id`

    ID of the vault that triggered the event.

  - `String organizationId`

  - `String workspaceId`

### Beta Webhook Vault Credential Archived Event Data

- `class BetaWebhookVaultCredentialArchivedEventData:`

  - `JsonValue type = "vault_credential.archived"`

  - `String id`

    ID of the vault credential that triggered the event.

  - `String organizationId`

  - `String vaultId`

    ID of the vault that owns this credential.

  - `String workspaceId`

### Beta Webhook Vault Credential Created Event Data

- `class BetaWebhookVaultCredentialCreatedEventData:`

  - `JsonValue type = "vault_credential.created"`

  - `String id`

    ID of the vault credential that triggered the event.

  - `String organizationId`

  - `String vaultId`

    ID of the vault that owns this credential.

  - `String workspaceId`

### Beta Webhook Vault Credential Deleted Event Data

- `class BetaWebhookVaultCredentialDeletedEventData:`

  - `JsonValue type = "vault_credential.deleted"`

  - `String id`

    ID of the vault credential that triggered the event.

  - `String organizationId`

  - `String vaultId`

    ID of the vault that owns this credential.

  - `String workspaceId`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `class BetaWebhookVaultCredentialRefreshFailedEventData:`

  - `JsonValue type = "vault_credential.refresh_failed"`

  - `String id`

    ID of the vault credential that triggered the event.

  - `String organizationId`

  - `String vaultId`

    ID of the vault that owns this credential.

  - `String workspaceId`

### Beta Webhook Vault Deleted Event Data

- `class BetaWebhookVaultDeletedEventData:`

  - `JsonValue type = "vault.deleted"`

  - `String id`

    ID of the vault that triggered the event.

  - `String organizationId`

  - `String workspaceId`
