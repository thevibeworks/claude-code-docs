---
title: Webhooks
url: https://platform.claude.com/docs/en/api/typescript/beta/webhooks
---

# Webhooks

## Domain types

### Beta Webhook Agent Archived Event Data

- `interface BetaWebhookAgentArchivedEventData`

  - `type: "agent.archived"`

  - `id: string`

    ID of the agent that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Agent Created Event Data

- `interface BetaWebhookAgentCreatedEventData`

  - `type: "agent.created"`

  - `id: string`

    ID of the agent that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Agent Deleted Event Data

- `interface BetaWebhookAgentDeletedEventData`

  - `type: "agent.deleted"`

  - `id: string`

    ID of the agent that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Agent Updated Event Data

- `interface BetaWebhookAgentUpdatedEventData`

  - `type: "agent.updated"`

  - `id: string`

    ID of the agent that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Deployment Archived Event Data

- `interface BetaWebhookDeploymentArchivedEventData`

  - `type: "deployment.archived"`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Deployment Created Event Data

- `interface BetaWebhookDeploymentCreatedEventData`

  - `type: "deployment.created"`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Deployment Deleted Event Data

- `interface BetaWebhookDeploymentDeletedEventData`

  - `type: "deployment.deleted"`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Deployment Paused Event Data

- `interface BetaWebhookDeploymentPausedEventData`

  - `type: "deployment.paused"`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Deployment Run Failed Event Data

- `interface BetaWebhookDeploymentRunFailedEventData`

  - `type: "deployment_run.failed"`

  - `id: string`

    ID of the deployment run that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Deployment Run Started Event Data

- `interface BetaWebhookDeploymentRunStartedEventData`

  - `type: "deployment_run.started"`

  - `id: string`

    ID of the deployment run that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Deployment Run Succeeded Event Data

- `interface BetaWebhookDeploymentRunSucceededEventData`

  - `type: "deployment_run.succeeded"`

  - `id: string`

    ID of the deployment run that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Deployment Unpaused Event Data

- `interface BetaWebhookDeploymentUnpausedEventData`

  - `type: "deployment.unpaused"`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Deployment Updated Event Data

- `interface BetaWebhookDeploymentUpdatedEventData`

  - `type: "deployment.updated"`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Environment Archived Event Data

- `interface BetaWebhookEnvironmentArchivedEventData`

  - `type: "environment.archived"`

  - `id: string`

    ID of the environment that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Environment Created Event Data

- `interface BetaWebhookEnvironmentCreatedEventData`

  - `type: "environment.created"`

  - `id: string`

    ID of the environment that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Environment Deleted Event Data

- `interface BetaWebhookEnvironmentDeletedEventData`

  - `type: "environment.deleted"`

  - `id: string`

    ID of the environment that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Environment Updated Event Data

- `interface BetaWebhookEnvironmentUpdatedEventData`

  - `type: "environment.updated"`

  - `id: string`

    ID of the environment that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Event

- `interface BetaWebhookEvent`

  - `type: "event"`

    Object type. Always `event` for webhook payloads.

  - `id: string`

    Unique event identifier for idempotency.

  - `created_at: string`

    RFC 3339 timestamp when the event occurred.

    format: date-time

  - `data: BetaWebhookEventData`

    - `interface BetaWebhookSessionCreatedEventData`

      - `type: "session.created"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookSessionPendingEventData`

      - `type: "session.pending"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookSessionRunningEventData`

      - `type: "session.running"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookSessionIdledEventData`

      - `type: "session.idled"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookSessionRequiresActionEventData`

      - `type: "session.requires_action"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookSessionArchivedEventData`

      - `type: "session.archived"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookSessionDeletedEventData`

      - `type: "session.deleted"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookSessionStatusRescheduledEventData`

      - `type: "session.status_rescheduled"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookSessionStatusRunStartedEventData`

      - `type: "session.status_run_started"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookSessionStatusIdledEventData`

      - `type: "session.status_idled"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookSessionStatusTerminatedEventData`

      - `type: "session.status_terminated"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookSessionThreadCreatedEventData`

      - `type: "session.thread_created"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `workspace_id: string`

    - `interface BetaWebhookSessionThreadIdledEventData`

      - `type: "session.thread_idled"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `workspace_id: string`

    - `interface BetaWebhookSessionThreadTerminatedEventData`

      - `type: "session.thread_terminated"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `workspace_id: string`

    - `interface BetaWebhookSessionOutcomeEvaluationEndedEventData`

      - `type: "session.outcome_evaluation_ended"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookVaultCreatedEventData`

      - `type: "vault.created"`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookVaultArchivedEventData`

      - `type: "vault.archived"`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookVaultDeletedEventData`

      - `type: "vault.deleted"`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookVaultCredentialCreatedEventData`

      - `type: "vault_credential.created"`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `interface BetaWebhookVaultCredentialArchivedEventData`

      - `type: "vault_credential.archived"`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `interface BetaWebhookVaultCredentialDeletedEventData`

      - `type: "vault_credential.deleted"`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `interface BetaWebhookVaultCredentialRefreshFailedEventData`

      - `type: "vault_credential.refresh_failed"`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `interface BetaWebhookSessionUpdatedEventData`

      - `type: "session.updated"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookAgentCreatedEventData`

      - `type: "agent.created"`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookAgentArchivedEventData`

      - `type: "agent.archived"`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookAgentDeletedEventData`

      - `type: "agent.deleted"`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookDeploymentPausedEventData`

      - `type: "deployment.paused"`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookDeploymentRunFailedEventData`

      - `type: "deployment_run.failed"`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookDeploymentCreatedEventData`

      - `type: "deployment.created"`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookDeploymentUpdatedEventData`

      - `type: "deployment.updated"`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookDeploymentUnpausedEventData`

      - `type: "deployment.unpaused"`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookAgentUpdatedEventData`

      - `type: "agent.updated"`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookDeploymentArchivedEventData`

      - `type: "deployment.archived"`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookDeploymentRunStartedEventData`

      - `type: "deployment_run.started"`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookDeploymentDeletedEventData`

      - `type: "deployment.deleted"`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookDeploymentRunSucceededEventData`

      - `type: "deployment_run.succeeded"`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookEnvironmentCreatedEventData`

      - `type: "environment.created"`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookEnvironmentUpdatedEventData`

      - `type: "environment.updated"`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookEnvironmentArchivedEventData`

      - `type: "environment.archived"`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookEnvironmentDeletedEventData`

      - `type: "environment.deleted"`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookMemoryStoreCreatedEventData`

      - `type: "memory_store.created"`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookMemoryStoreArchivedEventData`

      - `type: "memory_store.archived"`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookMemoryStoreDeletedEventData`

      - `type: "memory_store.deleted"`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

    - `interface BetaWebhookSessionBudgetReachedEventData`

      - `type: "session.budget_reached"`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `workspace_id: string`

### Beta Webhook Event Data

- `type BetaWebhookEventData = BetaWebhookSessionCreatedEventData | BetaWebhookSessionPendingEventData | BetaWebhookSessionRunningEventData | 41 more`

  - `interface BetaWebhookSessionCreatedEventData`

    - `type: "session.created"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `interface BetaWebhookSessionPendingEventData`

    - `type: "session.pending"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `interface BetaWebhookSessionRunningEventData`

    - `type: "session.running"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `interface BetaWebhookSessionIdledEventData`

    - `type: "session.idled"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `interface BetaWebhookSessionRequiresActionEventData`

    - `type: "session.requires_action"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `interface BetaWebhookSessionArchivedEventData`

    - `type: "session.archived"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `interface BetaWebhookSessionDeletedEventData`

    - `type: "session.deleted"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `interface BetaWebhookSessionStatusRescheduledEventData`

    - `type: "session.status_rescheduled"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `interface BetaWebhookSessionStatusRunStartedEventData`

    - `type: "session.status_run_started"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `interface BetaWebhookSessionStatusIdledEventData`

    - `type: "session.status_idled"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `interface BetaWebhookSessionStatusTerminatedEventData`

    - `type: "session.status_terminated"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `interface BetaWebhookSessionThreadCreatedEventData`

    - `type: "session.thread_created"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `session_thread_id: string`

      ID of the session thread this event refers to.

    - `workspace_id: string`

  - `interface BetaWebhookSessionThreadIdledEventData`

    - `type: "session.thread_idled"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `session_thread_id: string`

      ID of the session thread this event refers to.

    - `workspace_id: string`

  - `interface BetaWebhookSessionThreadTerminatedEventData`

    - `type: "session.thread_terminated"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `session_thread_id: string`

      ID of the session thread this event refers to.

    - `workspace_id: string`

  - `interface BetaWebhookSessionOutcomeEvaluationEndedEventData`

    - `type: "session.outcome_evaluation_ended"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `interface BetaWebhookVaultCreatedEventData`

    - `type: "vault.created"`

    - `id: string`

      ID of the vault that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `interface BetaWebhookVaultArchivedEventData`

    - `type: "vault.archived"`

    - `id: string`

      ID of the vault that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `interface BetaWebhookVaultDeletedEventData`

    - `type: "vault.deleted"`

    - `id: string`

      ID of the vault that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `interface BetaWebhookVaultCredentialCreatedEventData`

    - `type: "vault_credential.created"`

    - `id: string`

      ID of the vault credential that triggered the event.

    - `organization_id: string`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `interface BetaWebhookVaultCredentialArchivedEventData`

    - `type: "vault_credential.archived"`

    - `id: string`

      ID of the vault credential that triggered the event.

    - `organization_id: string`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `interface BetaWebhookVaultCredentialDeletedEventData`

    - `type: "vault_credential.deleted"`

    - `id: string`

      ID of the vault credential that triggered the event.

    - `organization_id: string`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `interface BetaWebhookVaultCredentialRefreshFailedEventData`

    - `type: "vault_credential.refresh_failed"`

    - `id: string`

      ID of the vault credential that triggered the event.

    - `organization_id: string`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `interface BetaWebhookSessionUpdatedEventData`

    - `type: "session.updated"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `interface BetaWebhookAgentCreatedEventData`

    - `type: "agent.created"`

    - `id: string`

      ID of the agent that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `interface BetaWebhookAgentArchivedEventData`

    - `type: "agent.archived"`

    - `id: string`

      ID of the agent that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `interface BetaWebhookAgentDeletedEventData`

    - `type: "agent.deleted"`

    - `id: string`

      ID of the agent that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `interface BetaWebhookDeploymentPausedEventData`

    - `type: "deployment.paused"`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `interface BetaWebhookDeploymentRunFailedEventData`

    - `type: "deployment_run.failed"`

    - `id: string`

      ID of the deployment run that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `interface BetaWebhookDeploymentCreatedEventData`

    - `type: "deployment.created"`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `interface BetaWebhookDeploymentUpdatedEventData`

    - `type: "deployment.updated"`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `interface BetaWebhookDeploymentUnpausedEventData`

    - `type: "deployment.unpaused"`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `interface BetaWebhookAgentUpdatedEventData`

    - `type: "agent.updated"`

    - `id: string`

      ID of the agent that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `interface BetaWebhookDeploymentArchivedEventData`

    - `type: "deployment.archived"`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `interface BetaWebhookDeploymentRunStartedEventData`

    - `type: "deployment_run.started"`

    - `id: string`

      ID of the deployment run that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `interface BetaWebhookDeploymentDeletedEventData`

    - `type: "deployment.deleted"`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `interface BetaWebhookDeploymentRunSucceededEventData`

    - `type: "deployment_run.succeeded"`

    - `id: string`

      ID of the deployment run that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `interface BetaWebhookEnvironmentCreatedEventData`

    - `type: "environment.created"`

    - `id: string`

      ID of the environment that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `interface BetaWebhookEnvironmentUpdatedEventData`

    - `type: "environment.updated"`

    - `id: string`

      ID of the environment that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `interface BetaWebhookEnvironmentArchivedEventData`

    - `type: "environment.archived"`

    - `id: string`

      ID of the environment that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `interface BetaWebhookEnvironmentDeletedEventData`

    - `type: "environment.deleted"`

    - `id: string`

      ID of the environment that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `interface BetaWebhookMemoryStoreCreatedEventData`

    - `type: "memory_store.created"`

    - `id: string`

      ID of the memory store that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `interface BetaWebhookMemoryStoreArchivedEventData`

    - `type: "memory_store.archived"`

    - `id: string`

      ID of the memory store that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `interface BetaWebhookMemoryStoreDeletedEventData`

    - `type: "memory_store.deleted"`

    - `id: string`

      ID of the memory store that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

  - `interface BetaWebhookSessionBudgetReachedEventData`

    - `type: "session.budget_reached"`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `workspace_id: string`

### Beta Webhook Memory Store Archived Event Data

- `interface BetaWebhookMemoryStoreArchivedEventData`

  - `type: "memory_store.archived"`

  - `id: string`

    ID of the memory store that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Memory Store Created Event Data

- `interface BetaWebhookMemoryStoreCreatedEventData`

  - `type: "memory_store.created"`

  - `id: string`

    ID of the memory store that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Memory Store Deleted Event Data

- `interface BetaWebhookMemoryStoreDeletedEventData`

  - `type: "memory_store.deleted"`

  - `id: string`

    ID of the memory store that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Archived Event Data

- `interface BetaWebhookSessionArchivedEventData`

  - `type: "session.archived"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Budget Reached Event Data

- `interface BetaWebhookSessionBudgetReachedEventData`

  - `type: "session.budget_reached"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Created Event Data

- `interface BetaWebhookSessionCreatedEventData`

  - `type: "session.created"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Deleted Event Data

- `interface BetaWebhookSessionDeletedEventData`

  - `type: "session.deleted"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Idled Event Data

- `interface BetaWebhookSessionIdledEventData`

  - `type: "session.idled"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `interface BetaWebhookSessionOutcomeEvaluationEndedEventData`

  - `type: "session.outcome_evaluation_ended"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Pending Event Data

- `interface BetaWebhookSessionPendingEventData`

  - `type: "session.pending"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Requires Action Event Data

- `interface BetaWebhookSessionRequiresActionEventData`

  - `type: "session.requires_action"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Running Event Data

- `interface BetaWebhookSessionRunningEventData`

  - `type: "session.running"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Status Idled Event Data

- `interface BetaWebhookSessionStatusIdledEventData`

  - `type: "session.status_idled"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Status Rescheduled Event Data

- `interface BetaWebhookSessionStatusRescheduledEventData`

  - `type: "session.status_rescheduled"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Status Run Started Event Data

- `interface BetaWebhookSessionStatusRunStartedEventData`

  - `type: "session.status_run_started"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Status Terminated Event Data

- `interface BetaWebhookSessionStatusTerminatedEventData`

  - `type: "session.status_terminated"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Session Thread Created Event Data

- `interface BetaWebhookSessionThreadCreatedEventData`

  - `type: "session.thread_created"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `session_thread_id: string`

    ID of the session thread this event refers to.

  - `workspace_id: string`

### Beta Webhook Session Thread Idled Event Data

- `interface BetaWebhookSessionThreadIdledEventData`

  - `type: "session.thread_idled"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `session_thread_id: string`

    ID of the session thread this event refers to.

  - `workspace_id: string`

### Beta Webhook Session Thread Terminated Event Data

- `interface BetaWebhookSessionThreadTerminatedEventData`

  - `type: "session.thread_terminated"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `session_thread_id: string`

    ID of the session thread this event refers to.

  - `workspace_id: string`

### Beta Webhook Session Updated Event Data

- `interface BetaWebhookSessionUpdatedEventData`

  - `type: "session.updated"`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Vault Archived Event Data

- `interface BetaWebhookVaultArchivedEventData`

  - `type: "vault.archived"`

  - `id: string`

    ID of the vault that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Vault Created Event Data

- `interface BetaWebhookVaultCreatedEventData`

  - `type: "vault.created"`

  - `id: string`

    ID of the vault that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`

### Beta Webhook Vault Credential Archived Event Data

- `interface BetaWebhookVaultCredentialArchivedEventData`

  - `type: "vault_credential.archived"`

  - `id: string`

    ID of the vault credential that triggered the event.

  - `organization_id: string`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Credential Created Event Data

- `interface BetaWebhookVaultCredentialCreatedEventData`

  - `type: "vault_credential.created"`

  - `id: string`

    ID of the vault credential that triggered the event.

  - `organization_id: string`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Credential Deleted Event Data

- `interface BetaWebhookVaultCredentialDeletedEventData`

  - `type: "vault_credential.deleted"`

  - `id: string`

    ID of the vault credential that triggered the event.

  - `organization_id: string`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `interface BetaWebhookVaultCredentialRefreshFailedEventData`

  - `type: "vault_credential.refresh_failed"`

  - `id: string`

    ID of the vault credential that triggered the event.

  - `organization_id: string`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Deleted Event Data

- `interface BetaWebhookVaultDeletedEventData`

  - `type: "vault.deleted"`

  - `id: string`

    ID of the vault that triggered the event.

  - `organization_id: string`

  - `workspace_id: string`
