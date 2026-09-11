---
title: Webhooks
url: https://platform.claude.com/docs/en/api/beta/webhooks
---

# Webhooks

## Domain types

### Beta Webhook Agent Archived Event Data

- `BetaWebhookAgentArchivedEventData object`

  - `type: "agent.archived"`

  - `id: string`

    ID of the agent that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Agent Created Event Data

- `BetaWebhookAgentCreatedEventData object`

  - `type: "agent.created"`

  - `id: string`

    ID of the agent that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Agent Deleted Event Data

- `BetaWebhookAgentDeletedEventData object`

  - `type: "agent.deleted"`

  - `id: string`

    ID of the agent that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Agent Updated Event Data

- `BetaWebhookAgentUpdatedEventData object`

  - `type: "agent.updated"`

  - `id: string`

    ID of the agent that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Deployment Archived Event Data

- `BetaWebhookDeploymentArchivedEventData object`

  - `type: "deployment.archived"`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Deployment Created Event Data

- `BetaWebhookDeploymentCreatedEventData object`

  - `type: "deployment.created"`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Deployment Deleted Event Data

- `BetaWebhookDeploymentDeletedEventData object`

  - `type: "deployment.deleted"`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Deployment Paused Event Data

- `BetaWebhookDeploymentPausedEventData object`

  - `type: "deployment.paused"`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Deployment Run Failed Event Data

- `BetaWebhookDeploymentRunFailedEventData object`

  - `type: "deployment_run.failed"`

  - `id: string`

    ID of the deployment run that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Deployment Run Started Event Data

- `BetaWebhookDeploymentRunStartedEventData object`

  - `type: "deployment_run.started"`

  - `id: string`

    ID of the deployment run that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Deployment Run Succeeded Event Data

- `BetaWebhookDeploymentRunSucceededEventData object`

  - `type: "deployment_run.succeeded"`

  - `id: string`

    ID of the deployment run that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Deployment Unpaused Event Data

- `BetaWebhookDeploymentUnpausedEventData object`

  - `type: "deployment.unpaused"`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Deployment Updated Event Data

- `BetaWebhookDeploymentUpdatedEventData object`

  - `type: "deployment.updated"`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Environment Archived Event Data

- `BetaWebhookEnvironmentArchivedEventData object`

  - `type: "environment.archived"`

  - `id: string`

    ID of the environment that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Environment Created Event Data

- `BetaWebhookEnvironmentCreatedEventData object`

  - `type: "environment.created"`

  - `id: string`

    ID of the environment that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Environment Deleted Event Data

- `BetaWebhookEnvironmentDeletedEventData object`

  - `type: "environment.deleted"`

  - `id: string`

    ID of the environment that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Environment Updated Event Data

- `BetaWebhookEnvironmentUpdatedEventData object`

  - `type: "environment.updated"`

  - `id: string`

    ID of the environment that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Event

- `BetaWebhookEvent object`

  - `type: "event"`

    Object type. Always `event` for webhook payloads.

  - `id: string`

    Unique event identifier for idempotency.

  - `created_at: string`

    RFC 3339 timestamp when the event occurred.

    format: date-time

  - `data: BetaWebhookEventData`

    - `BetaWebhookSessionCreatedEventData object`

      - `type: "session.created"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookSessionPendingEventData object`

      - `type: "session.pending"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookSessionRunningEventData object`

      - `type: "session.running"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookSessionIdledEventData object`

      - `type: "session.idled"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookSessionRequiresActionEventData object`

      - `type: "session.requires_action"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookSessionArchivedEventData object`

      - `type: "session.archived"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookSessionDeletedEventData object`

      - `type: "session.deleted"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusRescheduledEventData object`

      - `type: "session.status_rescheduled"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusRunStartedEventData object`

      - `type: "session.status_run_started"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusIdledEventData object`

      - `type: "session.status_idled"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookSessionStatusTerminatedEventData object`

      - `type: "session.status_terminated"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookSessionThreadCreatedEventData object`

      - `type: "session.thread_created"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `workspace_id: string`

    - `BetaWebhookSessionThreadIdledEventData object`

      - `type: "session.thread_idled"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `workspace_id: string`

    - `BetaWebhookSessionThreadTerminatedEventData object`

      - `type: "session.thread_terminated"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `workspace_id: string`

    - `BetaWebhookSessionOutcomeEvaluationEndedEventData object`

      - `type: "session.outcome_evaluation_ended"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookVaultCreatedEventData object`

      - `type: "vault.created"`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookVaultArchivedEventData object`

      - `type: "vault.archived"`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookVaultDeletedEventData object`

      - `type: "vault.deleted"`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialCreatedEventData object`

      - `type: "vault_credential.created"`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialArchivedEventData object`

      - `type: "vault_credential.archived"`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialDeletedEventData object`

      - `type: "vault_credential.deleted"`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookVaultCredentialRefreshFailedEventData object`

      - `type: "vault_credential.refresh_failed"`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `BetaWebhookSessionUpdatedEventData object`

      - `type: "session.updated"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookAgentCreatedEventData object`

      - `type: "agent.created"`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookAgentArchivedEventData object`

      - `type: "agent.archived"`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookAgentDeletedEventData object`

      - `type: "agent.deleted"`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookDeploymentPausedEventData object`

      - `type: "deployment.paused"`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookDeploymentRunFailedEventData object`

      - `type: "deployment_run.failed"`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookDeploymentCreatedEventData object`

      - `type: "deployment.created"`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookDeploymentUpdatedEventData object`

      - `type: "deployment.updated"`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookDeploymentUnpausedEventData object`

      - `type: "deployment.unpaused"`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookAgentUpdatedEventData object`

      - `type: "agent.updated"`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookDeploymentArchivedEventData object`

      - `type: "deployment.archived"`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookDeploymentRunStartedEventData object`

      - `type: "deployment_run.started"`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookDeploymentDeletedEventData object`

      - `type: "deployment.deleted"`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookDeploymentRunSucceededEventData object`

      - `type: "deployment_run.succeeded"`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookEnvironmentCreatedEventData object`

      - `type: "environment.created"`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookEnvironmentUpdatedEventData object`

      - `type: "environment.updated"`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookEnvironmentArchivedEventData object`

      - `type: "environment.archived"`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookEnvironmentDeletedEventData object`

      - `type: "environment.deleted"`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookMemoryStoreCreatedEventData object`

      - `type: "memory_store.created"`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookMemoryStoreArchivedEventData object`

      - `type: "memory_store.archived"`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookMemoryStoreDeletedEventData object`

      - `type: "memory_store.deleted"`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `BetaWebhookSessionBudgetReachedEventData object`

      - `type: "session.budget_reached"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

### Beta Webhook Event Data

- `BetaWebhookEventData = BetaWebhookSessionCreatedEventData or BetaWebhookSessionPendingEventData or BetaWebhookSessionRunningEventData or 41 more`

  - `BetaWebhookSessionCreatedEventData object`

    - `type: "session.created"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookSessionPendingEventData object`

    - `type: "session.pending"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookSessionRunningEventData object`

    - `type: "session.running"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookSessionIdledEventData object`

    - `type: "session.idled"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookSessionRequiresActionEventData object`

    - `type: "session.requires_action"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookSessionArchivedEventData object`

    - `type: "session.archived"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookSessionDeletedEventData object`

    - `type: "session.deleted"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookSessionStatusRescheduledEventData object`

    - `type: "session.status_rescheduled"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookSessionStatusRunStartedEventData object`

    - `type: "session.status_run_started"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookSessionStatusIdledEventData object`

    - `type: "session.status_idled"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookSessionStatusTerminatedEventData object`

    - `type: "session.status_terminated"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookSessionThreadCreatedEventData object`

    - `type: "session.thread_created"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `session_thread_id: string`

      ID of the session thread this event refers to.

    - `workspace_id: string`

  - `BetaWebhookSessionThreadIdledEventData object`

    - `type: "session.thread_idled"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `session_thread_id: string`

      ID of the session thread this event refers to.

    - `workspace_id: string`

  - `BetaWebhookSessionThreadTerminatedEventData object`

    - `type: "session.thread_terminated"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `session_thread_id: string`

      ID of the session thread this event refers to.

    - `workspace_id: string`

  - `BetaWebhookSessionOutcomeEvaluationEndedEventData object`

    - `type: "session.outcome_evaluation_ended"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookVaultCreatedEventData object`

    - `type: "vault.created"`

    - `id: string`

      ID of the vault that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookVaultArchivedEventData object`

    - `type: "vault.archived"`

    - `id: string`

      ID of the vault that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookVaultDeletedEventData object`

    - `type: "vault.deleted"`

    - `id: string`

      ID of the vault that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookVaultCredentialCreatedEventData object`

    - `type: "vault_credential.created"`

    - `id: string`

      ID of the vault credential that triggered the event.

    - `organization_id: string`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `BetaWebhookVaultCredentialArchivedEventData object`

    - `type: "vault_credential.archived"`

    - `id: string`

      ID of the vault credential that triggered the event.

    - `organization_id: string`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `BetaWebhookVaultCredentialDeletedEventData object`

    - `type: "vault_credential.deleted"`

    - `id: string`

      ID of the vault credential that triggered the event.

    - `organization_id: string`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `BetaWebhookVaultCredentialRefreshFailedEventData object`

    - `type: "vault_credential.refresh_failed"`

    - `id: string`

      ID of the vault credential that triggered the event.

    - `organization_id: string`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `BetaWebhookSessionUpdatedEventData object`

    - `type: "session.updated"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookAgentCreatedEventData object`

    - `type: "agent.created"`

    - `id: string`

      ID of the agent that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookAgentArchivedEventData object`

    - `type: "agent.archived"`

    - `id: string`

      ID of the agent that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookAgentDeletedEventData object`

    - `type: "agent.deleted"`

    - `id: string`

      ID of the agent that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookDeploymentPausedEventData object`

    - `type: "deployment.paused"`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookDeploymentRunFailedEventData object`

    - `type: "deployment_run.failed"`

    - `id: string`

      ID of the deployment run that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookDeploymentCreatedEventData object`

    - `type: "deployment.created"`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookDeploymentUpdatedEventData object`

    - `type: "deployment.updated"`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookDeploymentUnpausedEventData object`

    - `type: "deployment.unpaused"`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookAgentUpdatedEventData object`

    - `type: "agent.updated"`

    - `id: string`

      ID of the agent that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookDeploymentArchivedEventData object`

    - `type: "deployment.archived"`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookDeploymentRunStartedEventData object`

    - `type: "deployment_run.started"`

    - `id: string`

      ID of the deployment run that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookDeploymentDeletedEventData object`

    - `type: "deployment.deleted"`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookDeploymentRunSucceededEventData object`

    - `type: "deployment_run.succeeded"`

    - `id: string`

      ID of the deployment run that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookEnvironmentCreatedEventData object`

    - `type: "environment.created"`

    - `id: string`

      ID of the environment that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookEnvironmentUpdatedEventData object`

    - `type: "environment.updated"`

    - `id: string`

      ID of the environment that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookEnvironmentArchivedEventData object`

    - `type: "environment.archived"`

    - `id: string`

      ID of the environment that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookEnvironmentDeletedEventData object`

    - `type: "environment.deleted"`

    - `id: string`

      ID of the environment that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookMemoryStoreCreatedEventData object`

    - `type: "memory_store.created"`

    - `id: string`

      ID of the memory store that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookMemoryStoreArchivedEventData object`

    - `type: "memory_store.archived"`

    - `id: string`

      ID of the memory store that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookMemoryStoreDeletedEventData object`

    - `type: "memory_store.deleted"`

    - `id: string`

      ID of the memory store that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `BetaWebhookSessionBudgetReachedEventData object`

    - `type: "session.budget_reached"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

### Beta Webhook Memory Store Archived Event Data

- `BetaWebhookMemoryStoreArchivedEventData object`

  - `type: "memory_store.archived"`

  - `id: string`

    ID of the memory store that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Memory Store Created Event Data

- `BetaWebhookMemoryStoreCreatedEventData object`

  - `type: "memory_store.created"`

  - `id: string`

    ID of the memory store that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Memory Store Deleted Event Data

- `BetaWebhookMemoryStoreDeletedEventData object`

  - `type: "memory_store.deleted"`

  - `id: string`

    ID of the memory store that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Archived Event Data

- `BetaWebhookSessionArchivedEventData object`

  - `type: "session.archived"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Budget Reached Event Data

- `BetaWebhookSessionBudgetReachedEventData object`

  - `type: "session.budget_reached"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Created Event Data

- `BetaWebhookSessionCreatedEventData object`

  - `type: "session.created"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Deleted Event Data

- `BetaWebhookSessionDeletedEventData object`

  - `type: "session.deleted"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Idled Event Data

- `BetaWebhookSessionIdledEventData object`

  - `type: "session.idled"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `BetaWebhookSessionOutcomeEvaluationEndedEventData object`

  - `type: "session.outcome_evaluation_ended"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Pending Event Data

- `BetaWebhookSessionPendingEventData object`

  - `type: "session.pending"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Requires Action Event Data

- `BetaWebhookSessionRequiresActionEventData object`

  - `type: "session.requires_action"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Running Event Data

- `BetaWebhookSessionRunningEventData object`

  - `type: "session.running"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Status Idled Event Data

- `BetaWebhookSessionStatusIdledEventData object`

  - `type: "session.status_idled"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Status Rescheduled Event Data

- `BetaWebhookSessionStatusRescheduledEventData object`

  - `type: "session.status_rescheduled"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Status Run Started Event Data

- `BetaWebhookSessionStatusRunStartedEventData object`

  - `type: "session.status_run_started"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Status Terminated Event Data

- `BetaWebhookSessionStatusTerminatedEventData object`

  - `type: "session.status_terminated"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Thread Created Event Data

- `BetaWebhookSessionThreadCreatedEventData object`

  - `type: "session.thread_created"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `session_thread_id: string`

    ID of the session thread this event refers to.

  - `workspace_id: string`

### Beta Webhook Session Thread Idled Event Data

- `BetaWebhookSessionThreadIdledEventData object`

  - `type: "session.thread_idled"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `session_thread_id: string`

    ID of the session thread this event refers to.

  - `workspace_id: string`

### Beta Webhook Session Thread Terminated Event Data

- `BetaWebhookSessionThreadTerminatedEventData object`

  - `type: "session.thread_terminated"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `session_thread_id: string`

    ID of the session thread this event refers to.

  - `workspace_id: string`

### Beta Webhook Session Updated Event Data

- `BetaWebhookSessionUpdatedEventData object`

  - `type: "session.updated"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Vault Archived Event Data

- `BetaWebhookVaultArchivedEventData object`

  - `type: "vault.archived"`

  - `id: string`

    ID of the vault that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Vault Created Event Data

- `BetaWebhookVaultCreatedEventData object`

  - `type: "vault.created"`

  - `id: string`

    ID of the vault that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Vault Credential Archived Event Data

- `BetaWebhookVaultCredentialArchivedEventData object`

  - `type: "vault_credential.archived"`

  - `id: string`

    ID of the vault credential that triggered the event.

  - `organization_id: string`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Credential Created Event Data

- `BetaWebhookVaultCredentialCreatedEventData object`

  - `type: "vault_credential.created"`

  - `id: string`

    ID of the vault credential that triggered the event.

  - `organization_id: string`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Credential Deleted Event Data

- `BetaWebhookVaultCredentialDeletedEventData object`

  - `type: "vault_credential.deleted"`

  - `id: string`

    ID of the vault credential that triggered the event.

  - `organization_id: string`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `BetaWebhookVaultCredentialRefreshFailedEventData object`

  - `type: "vault_credential.refresh_failed"`

  - `id: string`

    ID of the vault credential that triggered the event.

  - `organization_id: string`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Deleted Event Data

- `BetaWebhookVaultDeletedEventData object`

  - `type: "vault.deleted"`

  - `id: string`

    ID of the vault that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`
