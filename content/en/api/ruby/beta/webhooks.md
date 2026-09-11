---
title: Webhooks
url: https://platform.claude.com/docs/en/api/ruby/beta/webhooks
---

# Webhooks

## Domain types

### Beta Webhook Agent Archived Event Data

- `class BetaWebhookAgentArchivedEventData`

  - `type: :"agent.archived"`

  - `id: String`

    ID of the agent that triggered the event.

  - `organization_id: String`

  - `workspace_id: String`

### Beta Webhook Agent Created Event Data

- `class BetaWebhookAgentCreatedEventData`

  - `type: :"agent.created"`

  - `id: String`

    ID of the agent that triggered the event.

  - `organization_id: String`

  - `workspace_id: String`

### Beta Webhook Agent Deleted Event Data

- `class BetaWebhookAgentDeletedEventData`

  - `type: :"agent.deleted"`

  - `id: String`

    ID of the agent that triggered the event.

  - `organization_id: String`

  - `workspace_id: String`

### Beta Webhook Agent Updated Event Data

- `class BetaWebhookAgentUpdatedEventData`

  - `type: :"agent.updated"`

  - `id: String`

    ID of the agent that triggered the event.

  - `organization_id: String`

  - `workspace_id: String`

### Beta Webhook Deployment Archived Event Data

- `class BetaWebhookDeploymentArchivedEventData`

  - `type: :"deployment.archived"`

  - `id: String`

    ID of the deployment that triggered the event.

  - `organization_id: String`

  - `workspace_id: String`

### Beta Webhook Deployment Created Event Data

- `class BetaWebhookDeploymentCreatedEventData`

  - `type: :"deployment.created"`

  - `id: String`

    ID of the deployment that triggered the event.

  - `organization_id: String`

  - `workspace_id: String`

### Beta Webhook Deployment Deleted Event Data

- `class BetaWebhookDeploymentDeletedEventData`

  - `type: :"deployment.deleted"`

  - `id: String`

    ID of the deployment that triggered the event.

  - `organization_id: String`

  - `workspace_id: String`

### Beta Webhook Deployment Paused Event Data

- `class BetaWebhookDeploymentPausedEventData`

  - `type: :"deployment.paused"`

  - `id: String`

    ID of the deployment that triggered the event.

  - `organization_id: String`

  - `workspace_id: String`

### Beta Webhook Deployment Run Failed Event Data

- `class BetaWebhookDeploymentRunFailedEventData`

  - `type: :"deployment_run.failed"`

  - `id: String`

    ID of the deployment run that triggered the event.

  - `organization_id: String`

  - `workspace_id: String`

### Beta Webhook Deployment Run Started Event Data

- `class BetaWebhookDeploymentRunStartedEventData`

  - `type: :"deployment_run.started"`

  - `id: String`

    ID of the deployment run that triggered the event.

  - `organization_id: String`

  - `workspace_id: String`

### Beta Webhook Deployment Run Succeeded Event Data

- `class BetaWebhookDeploymentRunSucceededEventData`

  - `type: :"deployment_run.succeeded"`

  - `id: String`

    ID of the deployment run that triggered the event.

  - `organization_id: String`

  - `workspace_id: String`

### Beta Webhook Deployment Unpaused Event Data

- `class BetaWebhookDeploymentUnpausedEventData`

  - `type: :"deployment.unpaused"`

  - `id: String`

    ID of the deployment that triggered the event.

  - `organization_id: String`

  - `workspace_id: String`

### Beta Webhook Deployment Updated Event Data

- `class BetaWebhookDeploymentUpdatedEventData`

  - `type: :"deployment.updated"`

  - `id: String`

    ID of the deployment that triggered the event.

  - `organization_id: String`

  - `workspace_id: String`

### Beta Webhook Environment Archived Event Data

- `class BetaWebhookEnvironmentArchivedEventData`

  - `type: :"environment.archived"`

  - `id: String`

    ID of the environment that triggered the event.

  - `organization_id: String`

  - `workspace_id: String`

### Beta Webhook Environment Created Event Data

- `class BetaWebhookEnvironmentCreatedEventData`

  - `type: :"environment.created"`

  - `id: String`

    ID of the environment that triggered the event.

  - `organization_id: String`

  - `workspace_id: String`

### Beta Webhook Environment Deleted Event Data

- `class BetaWebhookEnvironmentDeletedEventData`

  - `type: :"environment.deleted"`

  - `id: String`

    ID of the environment that triggered the event.

  - `organization_id: String`

  - `workspace_id: String`

### Beta Webhook Environment Updated Event Data

- `class BetaWebhookEnvironmentUpdatedEventData`

  - `type: :"environment.updated"`

  - `id: String`

    ID of the environment that triggered the event.

  - `organization_id: String`

  - `workspace_id: String`

### Beta Webhook Event

- `class BetaWebhookEvent`

  - `type: :event`

    Object type. Always `event` for webhook payloads.

  - `id: String`

    Unique event identifier for idempotency.

  - `created_at: Time`

    RFC 3339 timestamp when the event occurred.

    format: date-time

  - `data: BetaWebhookEventData`

    - `class BetaWebhookSessionCreatedEventData`

      - `type: :"session.created"`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookSessionPendingEventData`

      - `type: :"session.pending"`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookSessionRunningEventData`

      - `type: :"session.running"`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookSessionIdledEventData`

      - `type: :"session.idled"`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookSessionRequiresActionEventData`

      - `type: :"session.requires_action"`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookSessionArchivedEventData`

      - `type: :"session.archived"`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookSessionDeletedEventData`

      - `type: :"session.deleted"`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookSessionStatusRescheduledEventData`

      - `type: :"session.status_rescheduled"`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookSessionStatusRunStartedEventData`

      - `type: :"session.status_run_started"`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookSessionStatusIdledEventData`

      - `type: :"session.status_idled"`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookSessionStatusTerminatedEventData`

      - `type: :"session.status_terminated"`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookSessionThreadCreatedEventData`

      - `type: :"session.thread_created"`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `session_thread_id: String`

        ID of the session thread this event refers to.

      - `workspace_id: String`

    - `class BetaWebhookSessionThreadIdledEventData`

      - `type: :"session.thread_idled"`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `session_thread_id: String`

        ID of the session thread this event refers to.

      - `workspace_id: String`

    - `class BetaWebhookSessionThreadTerminatedEventData`

      - `type: :"session.thread_terminated"`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `session_thread_id: String`

        ID of the session thread this event refers to.

      - `workspace_id: String`

    - `class BetaWebhookSessionOutcomeEvaluationEndedEventData`

      - `type: :"session.outcome_evaluation_ended"`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookVaultCreatedEventData`

      - `type: :"vault.created"`

      - `id: String`

        ID of the vault that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookVaultArchivedEventData`

      - `type: :"vault.archived"`

      - `id: String`

        ID of the vault that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookVaultDeletedEventData`

      - `type: :"vault.deleted"`

      - `id: String`

        ID of the vault that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookVaultCredentialCreatedEventData`

      - `type: :"vault_credential.created"`

      - `id: String`

        ID of the vault credential that triggered the event.

      - `organization_id: String`

      - `vault_id: String`

        ID of the vault that owns this credential.

      - `workspace_id: String`

    - `class BetaWebhookVaultCredentialArchivedEventData`

      - `type: :"vault_credential.archived"`

      - `id: String`

        ID of the vault credential that triggered the event.

      - `organization_id: String`

      - `vault_id: String`

        ID of the vault that owns this credential.

      - `workspace_id: String`

    - `class BetaWebhookVaultCredentialDeletedEventData`

      - `type: :"vault_credential.deleted"`

      - `id: String`

        ID of the vault credential that triggered the event.

      - `organization_id: String`

      - `vault_id: String`

        ID of the vault that owns this credential.

      - `workspace_id: String`

    - `class BetaWebhookVaultCredentialRefreshFailedEventData`

      - `type: :"vault_credential.refresh_failed"`

      - `id: String`

        ID of the vault credential that triggered the event.

      - `organization_id: String`

      - `vault_id: String`

        ID of the vault that owns this credential.

      - `workspace_id: String`

    - `class BetaWebhookSessionUpdatedEventData`

      - `type: :"session.updated"`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookAgentCreatedEventData`

      - `type: :"agent.created"`

      - `id: String`

        ID of the agent that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookAgentArchivedEventData`

      - `type: :"agent.archived"`

      - `id: String`

        ID of the agent that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookAgentDeletedEventData`

      - `type: :"agent.deleted"`

      - `id: String`

        ID of the agent that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentPausedEventData`

      - `type: :"deployment.paused"`

      - `id: String`

        ID of the deployment that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentRunFailedEventData`

      - `type: :"deployment_run.failed"`

      - `id: String`

        ID of the deployment run that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentCreatedEventData`

      - `type: :"deployment.created"`

      - `id: String`

        ID of the deployment that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentUpdatedEventData`

      - `type: :"deployment.updated"`

      - `id: String`

        ID of the deployment that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentUnpausedEventData`

      - `type: :"deployment.unpaused"`

      - `id: String`

        ID of the deployment that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookAgentUpdatedEventData`

      - `type: :"agent.updated"`

      - `id: String`

        ID of the agent that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentArchivedEventData`

      - `type: :"deployment.archived"`

      - `id: String`

        ID of the deployment that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentRunStartedEventData`

      - `type: :"deployment_run.started"`

      - `id: String`

        ID of the deployment run that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentDeletedEventData`

      - `type: :"deployment.deleted"`

      - `id: String`

        ID of the deployment that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookDeploymentRunSucceededEventData`

      - `type: :"deployment_run.succeeded"`

      - `id: String`

        ID of the deployment run that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookEnvironmentCreatedEventData`

      - `type: :"environment.created"`

      - `id: String`

        ID of the environment that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookEnvironmentUpdatedEventData`

      - `type: :"environment.updated"`

      - `id: String`

        ID of the environment that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookEnvironmentArchivedEventData`

      - `type: :"environment.archived"`

      - `id: String`

        ID of the environment that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookEnvironmentDeletedEventData`

      - `type: :"environment.deleted"`

      - `id: String`

        ID of the environment that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookMemoryStoreCreatedEventData`

      - `type: :"memory_store.created"`

      - `id: String`

        ID of the memory store that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookMemoryStoreArchivedEventData`

      - `type: :"memory_store.archived"`

      - `id: String`

        ID of the memory store that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookMemoryStoreDeletedEventData`

      - `type: :"memory_store.deleted"`

      - `id: String`

        ID of the memory store that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

    - `class BetaWebhookSessionBudgetReachedEventData`

      - `type: :"session.budget_reached"`

      - `id: String`

        ID of the session that triggered the event.

      - `organization_id: String`

      - `workspace_id: String`

### Beta Webhook Event Data

- `BetaWebhookEventData = BetaWebhookSessionCreatedEventData | BetaWebhookSessionPendingEventData | BetaWebhookSessionRunningEventData | 41 more`

  - `class BetaWebhookSessionCreatedEventData`

    - `type: :"session.created"`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `workspace_id: String`

  - `class BetaWebhookSessionPendingEventData`

    - `type: :"session.pending"`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `workspace_id: String`

  - `class BetaWebhookSessionRunningEventData`

    - `type: :"session.running"`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `workspace_id: String`

  - `class BetaWebhookSessionIdledEventData`

    - `type: :"session.idled"`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `workspace_id: String`

  - `class BetaWebhookSessionRequiresActionEventData`

    - `type: :"session.requires_action"`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `workspace_id: String`

  - `class BetaWebhookSessionArchivedEventData`

    - `type: :"session.archived"`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `workspace_id: String`

  - `class BetaWebhookSessionDeletedEventData`

    - `type: :"session.deleted"`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `workspace_id: String`

  - `class BetaWebhookSessionStatusRescheduledEventData`

    - `type: :"session.status_rescheduled"`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `workspace_id: String`

  - `class BetaWebhookSessionStatusRunStartedEventData`

    - `type: :"session.status_run_started"`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `workspace_id: String`

  - `class BetaWebhookSessionStatusIdledEventData`

    - `type: :"session.status_idled"`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `workspace_id: String`

  - `class BetaWebhookSessionStatusTerminatedEventData`

    - `type: :"session.status_terminated"`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `workspace_id: String`

  - `class BetaWebhookSessionThreadCreatedEventData`

    - `type: :"session.thread_created"`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `session_thread_id: String`

      ID of the session thread this event refers to.

    - `workspace_id: String`

  - `class BetaWebhookSessionThreadIdledEventData`

    - `type: :"session.thread_idled"`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `session_thread_id: String`

      ID of the session thread this event refers to.

    - `workspace_id: String`

  - `class BetaWebhookSessionThreadTerminatedEventData`

    - `type: :"session.thread_terminated"`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `session_thread_id: String`

      ID of the session thread this event refers to.

    - `workspace_id: String`

  - `class BetaWebhookSessionOutcomeEvaluationEndedEventData`

    - `type: :"session.outcome_evaluation_ended"`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `workspace_id: String`

  - `class BetaWebhookVaultCreatedEventData`

    - `type: :"vault.created"`

    - `id: String`

      ID of the vault that triggered the event.

    - `organization_id: String`

    - `workspace_id: String`

  - `class BetaWebhookVaultArchivedEventData`

    - `type: :"vault.archived"`

    - `id: String`

      ID of the vault that triggered the event.

    - `organization_id: String`

    - `workspace_id: String`

  - `class BetaWebhookVaultDeletedEventData`

    - `type: :"vault.deleted"`

    - `id: String`

      ID of the vault that triggered the event.

    - `organization_id: String`

    - `workspace_id: String`

  - `class BetaWebhookVaultCredentialCreatedEventData`

    - `type: :"vault_credential.created"`

    - `id: String`

      ID of the vault credential that triggered the event.

    - `organization_id: String`

    - `vault_id: String`

      ID of the vault that owns this credential.

    - `workspace_id: String`

  - `class BetaWebhookVaultCredentialArchivedEventData`

    - `type: :"vault_credential.archived"`

    - `id: String`

      ID of the vault credential that triggered the event.

    - `organization_id: String`

    - `vault_id: String`

      ID of the vault that owns this credential.

    - `workspace_id: String`

  - `class BetaWebhookVaultCredentialDeletedEventData`

    - `type: :"vault_credential.deleted"`

    - `id: String`

      ID of the vault credential that triggered the event.

    - `organization_id: String`

    - `vault_id: String`

      ID of the vault that owns this credential.

    - `workspace_id: String`

  - `class BetaWebhookVaultCredentialRefreshFailedEventData`

    - `type: :"vault_credential.refresh_failed"`

    - `id: String`

      ID of the vault credential that triggered the event.

    - `organization_id: String`

    - `vault_id: String`

      ID of the vault that owns this credential.

    - `workspace_id: String`

  - `class BetaWebhookSessionUpdatedEventData`

    - `type: :"session.updated"`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `workspace_id: String`

  - `class BetaWebhookAgentCreatedEventData`

    - `type: :"agent.created"`

    - `id: String`

      ID of the agent that triggered the event.

    - `organization_id: String`

    - `workspace_id: String`

  - `class BetaWebhookAgentArchivedEventData`

    - `type: :"agent.archived"`

    - `id: String`

      ID of the agent that triggered the event.

    - `organization_id: String`

    - `workspace_id: String`

  - `class BetaWebhookAgentDeletedEventData`

    - `type: :"agent.deleted"`

    - `id: String`

      ID of the agent that triggered the event.

    - `organization_id: String`

    - `workspace_id: String`

  - `class BetaWebhookDeploymentPausedEventData`

    - `type: :"deployment.paused"`

    - `id: String`

      ID of the deployment that triggered the event.

    - `organization_id: String`

    - `workspace_id: String`

  - `class BetaWebhookDeploymentRunFailedEventData`

    - `type: :"deployment_run.failed"`

    - `id: String`

      ID of the deployment run that triggered the event.

    - `organization_id: String`

    - `workspace_id: String`

  - `class BetaWebhookDeploymentCreatedEventData`

    - `type: :"deployment.created"`

    - `id: String`

      ID of the deployment that triggered the event.

    - `organization_id: String`

    - `workspace_id: String`

  - `class BetaWebhookDeploymentUpdatedEventData`

    - `type: :"deployment.updated"`

    - `id: String`

      ID of the deployment that triggered the event.

    - `organization_id: String`

    - `workspace_id: String`

  - `class BetaWebhookDeploymentUnpausedEventData`

    - `type: :"deployment.unpaused"`

    - `id: String`

      ID of the deployment that triggered the event.

    - `organization_id: String`

    - `workspace_id: String`

  - `class BetaWebhookAgentUpdatedEventData`

    - `type: :"agent.updated"`

    - `id: String`

      ID of the agent that triggered the event.

    - `organization_id: String`

    - `workspace_id: String`

  - `class BetaWebhookDeploymentArchivedEventData`

    - `type: :"deployment.archived"`

    - `id: String`

      ID of the deployment that triggered the event.

    - `organization_id: String`

    - `workspace_id: String`

  - `class BetaWebhookDeploymentRunStartedEventData`

    - `type: :"deployment_run.started"`

    - `id: String`

      ID of the deployment run that triggered the event.

    - `organization_id: String`

    - `workspace_id: String`

  - `class BetaWebhookDeploymentDeletedEventData`

    - `type: :"deployment.deleted"`

    - `id: String`

      ID of the deployment that triggered the event.

    - `organization_id: String`

    - `workspace_id: String`

  - `class BetaWebhookDeploymentRunSucceededEventData`

    - `type: :"deployment_run.succeeded"`

    - `id: String`

      ID of the deployment run that triggered the event.

    - `organization_id: String`

    - `workspace_id: String`

  - `class BetaWebhookEnvironmentCreatedEventData`

    - `type: :"environment.created"`

    - `id: String`

      ID of the environment that triggered the event.

    - `organization_id: String`

    - `workspace_id: String`

  - `class BetaWebhookEnvironmentUpdatedEventData`

    - `type: :"environment.updated"`

    - `id: String`

      ID of the environment that triggered the event.

    - `organization_id: String`

    - `workspace_id: String`

  - `class BetaWebhookEnvironmentArchivedEventData`

    - `type: :"environment.archived"`

    - `id: String`

      ID of the environment that triggered the event.

    - `organization_id: String`

    - `workspace_id: String`

  - `class BetaWebhookEnvironmentDeletedEventData`

    - `type: :"environment.deleted"`

    - `id: String`

      ID of the environment that triggered the event.

    - `organization_id: String`

    - `workspace_id: String`

  - `class BetaWebhookMemoryStoreCreatedEventData`

    - `type: :"memory_store.created"`

    - `id: String`

      ID of the memory store that triggered the event.

    - `organization_id: String`

    - `workspace_id: String`

  - `class BetaWebhookMemoryStoreArchivedEventData`

    - `type: :"memory_store.archived"`

    - `id: String`

      ID of the memory store that triggered the event.

    - `organization_id: String`

    - `workspace_id: String`

  - `class BetaWebhookMemoryStoreDeletedEventData`

    - `type: :"memory_store.deleted"`

    - `id: String`

      ID of the memory store that triggered the event.

    - `organization_id: String`

    - `workspace_id: String`

  - `class BetaWebhookSessionBudgetReachedEventData`

    - `type: :"session.budget_reached"`

    - `id: String`

      ID of the session that triggered the event.

    - `organization_id: String`

    - `workspace_id: String`

### Beta Webhook Memory Store Archived Event Data

- `class BetaWebhookMemoryStoreArchivedEventData`

  - `type: :"memory_store.archived"`

  - `id: String`

    ID of the memory store that triggered the event.

  - `organization_id: String`

  - `workspace_id: String`

### Beta Webhook Memory Store Created Event Data

- `class BetaWebhookMemoryStoreCreatedEventData`

  - `type: :"memory_store.created"`

  - `id: String`

    ID of the memory store that triggered the event.

  - `organization_id: String`

  - `workspace_id: String`

### Beta Webhook Memory Store Deleted Event Data

- `class BetaWebhookMemoryStoreDeletedEventData`

  - `type: :"memory_store.deleted"`

  - `id: String`

    ID of the memory store that triggered the event.

  - `organization_id: String`

  - `workspace_id: String`

### Beta Webhook Session Archived Event Data

- `class BetaWebhookSessionArchivedEventData`

  - `type: :"session.archived"`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `workspace_id: String`

### Beta Webhook Session Budget Reached Event Data

- `class BetaWebhookSessionBudgetReachedEventData`

  - `type: :"session.budget_reached"`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `workspace_id: String`

### Beta Webhook Session Created Event Data

- `class BetaWebhookSessionCreatedEventData`

  - `type: :"session.created"`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `workspace_id: String`

### Beta Webhook Session Deleted Event Data

- `class BetaWebhookSessionDeletedEventData`

  - `type: :"session.deleted"`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `workspace_id: String`

### Beta Webhook Session Idled Event Data

- `class BetaWebhookSessionIdledEventData`

  - `type: :"session.idled"`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `workspace_id: String`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `class BetaWebhookSessionOutcomeEvaluationEndedEventData`

  - `type: :"session.outcome_evaluation_ended"`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `workspace_id: String`

### Beta Webhook Session Pending Event Data

- `class BetaWebhookSessionPendingEventData`

  - `type: :"session.pending"`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `workspace_id: String`

### Beta Webhook Session Requires Action Event Data

- `class BetaWebhookSessionRequiresActionEventData`

  - `type: :"session.requires_action"`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `workspace_id: String`

### Beta Webhook Session Running Event Data

- `class BetaWebhookSessionRunningEventData`

  - `type: :"session.running"`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `workspace_id: String`

### Beta Webhook Session Status Idled Event Data

- `class BetaWebhookSessionStatusIdledEventData`

  - `type: :"session.status_idled"`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `workspace_id: String`

### Beta Webhook Session Status Rescheduled Event Data

- `class BetaWebhookSessionStatusRescheduledEventData`

  - `type: :"session.status_rescheduled"`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `workspace_id: String`

### Beta Webhook Session Status Run Started Event Data

- `class BetaWebhookSessionStatusRunStartedEventData`

  - `type: :"session.status_run_started"`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `workspace_id: String`

### Beta Webhook Session Status Terminated Event Data

- `class BetaWebhookSessionStatusTerminatedEventData`

  - `type: :"session.status_terminated"`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `workspace_id: String`

### Beta Webhook Session Thread Created Event Data

- `class BetaWebhookSessionThreadCreatedEventData`

  - `type: :"session.thread_created"`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `session_thread_id: String`

    ID of the session thread this event refers to.

  - `workspace_id: String`

### Beta Webhook Session Thread Idled Event Data

- `class BetaWebhookSessionThreadIdledEventData`

  - `type: :"session.thread_idled"`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `session_thread_id: String`

    ID of the session thread this event refers to.

  - `workspace_id: String`

### Beta Webhook Session Thread Terminated Event Data

- `class BetaWebhookSessionThreadTerminatedEventData`

  - `type: :"session.thread_terminated"`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `session_thread_id: String`

    ID of the session thread this event refers to.

  - `workspace_id: String`

### Beta Webhook Session Updated Event Data

- `class BetaWebhookSessionUpdatedEventData`

  - `type: :"session.updated"`

  - `id: String`

    ID of the session that triggered the event.

  - `organization_id: String`

  - `workspace_id: String`

### Beta Webhook Vault Archived Event Data

- `class BetaWebhookVaultArchivedEventData`

  - `type: :"vault.archived"`

  - `id: String`

    ID of the vault that triggered the event.

  - `organization_id: String`

  - `workspace_id: String`

### Beta Webhook Vault Created Event Data

- `class BetaWebhookVaultCreatedEventData`

  - `type: :"vault.created"`

  - `id: String`

    ID of the vault that triggered the event.

  - `organization_id: String`

  - `workspace_id: String`

### Beta Webhook Vault Credential Archived Event Data

- `class BetaWebhookVaultCredentialArchivedEventData`

  - `type: :"vault_credential.archived"`

  - `id: String`

    ID of the vault credential that triggered the event.

  - `organization_id: String`

  - `vault_id: String`

    ID of the vault that owns this credential.

  - `workspace_id: String`

### Beta Webhook Vault Credential Created Event Data

- `class BetaWebhookVaultCredentialCreatedEventData`

  - `type: :"vault_credential.created"`

  - `id: String`

    ID of the vault credential that triggered the event.

  - `organization_id: String`

  - `vault_id: String`

    ID of the vault that owns this credential.

  - `workspace_id: String`

### Beta Webhook Vault Credential Deleted Event Data

- `class BetaWebhookVaultCredentialDeletedEventData`

  - `type: :"vault_credential.deleted"`

  - `id: String`

    ID of the vault credential that triggered the event.

  - `organization_id: String`

  - `vault_id: String`

    ID of the vault that owns this credential.

  - `workspace_id: String`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `class BetaWebhookVaultCredentialRefreshFailedEventData`

  - `type: :"vault_credential.refresh_failed"`

  - `id: String`

    ID of the vault credential that triggered the event.

  - `organization_id: String`

  - `vault_id: String`

    ID of the vault that owns this credential.

  - `workspace_id: String`

### Beta Webhook Vault Deleted Event Data

- `class BetaWebhookVaultDeletedEventData`

  - `type: :"vault.deleted"`

  - `id: String`

    ID of the vault that triggered the event.

  - `organization_id: String`

  - `workspace_id: String`
