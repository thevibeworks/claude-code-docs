---
title: Webhooks
url: https://platform.claude.com/docs/en/api/python/beta/webhooks
---

# Webhooks

## Domain types

### Beta Webhook Agent Archived Event Data

- `class BetaWebhookAgentArchivedEventData: …`

  - `type: Literal["agent.archived"]`

  - `id: str`

    ID of the agent that triggered the event.

  - `organization_id: str`

  - `workspace_id: str`

### Beta Webhook Agent Created Event Data

- `class BetaWebhookAgentCreatedEventData: …`

  - `type: Literal["agent.created"]`

  - `id: str`

    ID of the agent that triggered the event.

  - `organization_id: str`

  - `workspace_id: str`

### Beta Webhook Agent Deleted Event Data

- `class BetaWebhookAgentDeletedEventData: …`

  - `type: Literal["agent.deleted"]`

  - `id: str`

    ID of the agent that triggered the event.

  - `organization_id: str`

  - `workspace_id: str`

### Beta Webhook Agent Updated Event Data

- `class BetaWebhookAgentUpdatedEventData: …`

  - `type: Literal["agent.updated"]`

  - `id: str`

    ID of the agent that triggered the event.

  - `organization_id: str`

  - `workspace_id: str`

### Beta Webhook Deployment Archived Event Data

- `class BetaWebhookDeploymentArchivedEventData: …`

  - `type: Literal["deployment.archived"]`

  - `id: str`

    ID of the deployment that triggered the event.

  - `organization_id: str`

  - `workspace_id: str`

### Beta Webhook Deployment Created Event Data

- `class BetaWebhookDeploymentCreatedEventData: …`

  - `type: Literal["deployment.created"]`

  - `id: str`

    ID of the deployment that triggered the event.

  - `organization_id: str`

  - `workspace_id: str`

### Beta Webhook Deployment Deleted Event Data

- `class BetaWebhookDeploymentDeletedEventData: …`

  - `type: Literal["deployment.deleted"]`

  - `id: str`

    ID of the deployment that triggered the event.

  - `organization_id: str`

  - `workspace_id: str`

### Beta Webhook Deployment Paused Event Data

- `class BetaWebhookDeploymentPausedEventData: …`

  - `type: Literal["deployment.paused"]`

  - `id: str`

    ID of the deployment that triggered the event.

  - `organization_id: str`

  - `workspace_id: str`

### Beta Webhook Deployment Run Failed Event Data

- `class BetaWebhookDeploymentRunFailedEventData: …`

  - `type: Literal["deployment_run.failed"]`

  - `id: str`

    ID of the deployment run that triggered the event.

  - `organization_id: str`

  - `workspace_id: str`

### Beta Webhook Deployment Run Started Event Data

- `class BetaWebhookDeploymentRunStartedEventData: …`

  - `type: Literal["deployment_run.started"]`

  - `id: str`

    ID of the deployment run that triggered the event.

  - `organization_id: str`

  - `workspace_id: str`

### Beta Webhook Deployment Run Succeeded Event Data

- `class BetaWebhookDeploymentRunSucceededEventData: …`

  - `type: Literal["deployment_run.succeeded"]`

  - `id: str`

    ID of the deployment run that triggered the event.

  - `organization_id: str`

  - `workspace_id: str`

### Beta Webhook Deployment Unpaused Event Data

- `class BetaWebhookDeploymentUnpausedEventData: …`

  - `type: Literal["deployment.unpaused"]`

  - `id: str`

    ID of the deployment that triggered the event.

  - `organization_id: str`

  - `workspace_id: str`

### Beta Webhook Deployment Updated Event Data

- `class BetaWebhookDeploymentUpdatedEventData: …`

  - `type: Literal["deployment.updated"]`

  - `id: str`

    ID of the deployment that triggered the event.

  - `organization_id: str`

  - `workspace_id: str`

### Beta Webhook Environment Archived Event Data

- `class BetaWebhookEnvironmentArchivedEventData: …`

  - `type: Literal["environment.archived"]`

  - `id: str`

    ID of the environment that triggered the event.

  - `organization_id: str`

  - `workspace_id: str`

### Beta Webhook Environment Created Event Data

- `class BetaWebhookEnvironmentCreatedEventData: …`

  - `type: Literal["environment.created"]`

  - `id: str`

    ID of the environment that triggered the event.

  - `organization_id: str`

  - `workspace_id: str`

### Beta Webhook Environment Deleted Event Data

- `class BetaWebhookEnvironmentDeletedEventData: …`

  - `type: Literal["environment.deleted"]`

  - `id: str`

    ID of the environment that triggered the event.

  - `organization_id: str`

  - `workspace_id: str`

### Beta Webhook Environment Updated Event Data

- `class BetaWebhookEnvironmentUpdatedEventData: …`

  - `type: Literal["environment.updated"]`

  - `id: str`

    ID of the environment that triggered the event.

  - `organization_id: str`

  - `workspace_id: str`

### Beta Webhook Event

- `class BetaWebhookEvent: …`

  - `type: Literal["event"]`

    Object type. Always `event` for webhook payloads.

  - `id: str`

    Unique event identifier for idempotency.

  - `created_at: datetime`

    RFC 3339 timestamp when the event occurred.

    format: date-time

  - `data: BetaWebhookEventData`

    - `class BetaWebhookSessionCreatedEventData: …`

      - `type: Literal["session.created"]`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookSessionPendingEventData: …`

      - `type: Literal["session.pending"]`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookSessionRunningEventData: …`

      - `type: Literal["session.running"]`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookSessionIdledEventData: …`

      - `type: Literal["session.idled"]`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookSessionRequiresActionEventData: …`

      - `type: Literal["session.requires_action"]`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookSessionArchivedEventData: …`

      - `type: Literal["session.archived"]`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookSessionDeletedEventData: …`

      - `type: Literal["session.deleted"]`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookSessionStatusRescheduledEventData: …`

      - `type: Literal["session.status_rescheduled"]`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookSessionStatusRunStartedEventData: …`

      - `type: Literal["session.status_run_started"]`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookSessionStatusIdledEventData: …`

      - `type: Literal["session.status_idled"]`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookSessionStatusTerminatedEventData: …`

      - `type: Literal["session.status_terminated"]`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookSessionThreadCreatedEventData: …`

      - `type: Literal["session.thread_created"]`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `session_thread_id: str`

        ID of the session thread this event refers to.

      - `workspace_id: str`

    - `class BetaWebhookSessionThreadIdledEventData: …`

      - `type: Literal["session.thread_idled"]`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `session_thread_id: str`

        ID of the session thread this event refers to.

      - `workspace_id: str`

    - `class BetaWebhookSessionThreadTerminatedEventData: …`

      - `type: Literal["session.thread_terminated"]`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `session_thread_id: str`

        ID of the session thread this event refers to.

      - `workspace_id: str`

    - `class BetaWebhookSessionOutcomeEvaluationEndedEventData: …`

      - `type: Literal["session.outcome_evaluation_ended"]`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookVaultCreatedEventData: …`

      - `type: Literal["vault.created"]`

      - `id: str`

        ID of the vault that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookVaultArchivedEventData: …`

      - `type: Literal["vault.archived"]`

      - `id: str`

        ID of the vault that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookVaultDeletedEventData: …`

      - `type: Literal["vault.deleted"]`

      - `id: str`

        ID of the vault that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookVaultCredentialCreatedEventData: …`

      - `type: Literal["vault_credential.created"]`

      - `id: str`

        ID of the vault credential that triggered the event.

      - `organization_id: str`

      - `vault_id: str`

        ID of the vault that owns this credential.

      - `workspace_id: str`

    - `class BetaWebhookVaultCredentialArchivedEventData: …`

      - `type: Literal["vault_credential.archived"]`

      - `id: str`

        ID of the vault credential that triggered the event.

      - `organization_id: str`

      - `vault_id: str`

        ID of the vault that owns this credential.

      - `workspace_id: str`

    - `class BetaWebhookVaultCredentialDeletedEventData: …`

      - `type: Literal["vault_credential.deleted"]`

      - `id: str`

        ID of the vault credential that triggered the event.

      - `organization_id: str`

      - `vault_id: str`

        ID of the vault that owns this credential.

      - `workspace_id: str`

    - `class BetaWebhookVaultCredentialRefreshFailedEventData: …`

      - `type: Literal["vault_credential.refresh_failed"]`

      - `id: str`

        ID of the vault credential that triggered the event.

      - `organization_id: str`

      - `vault_id: str`

        ID of the vault that owns this credential.

      - `workspace_id: str`

    - `class BetaWebhookSessionUpdatedEventData: …`

      - `type: Literal["session.updated"]`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookAgentCreatedEventData: …`

      - `type: Literal["agent.created"]`

      - `id: str`

        ID of the agent that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookAgentArchivedEventData: …`

      - `type: Literal["agent.archived"]`

      - `id: str`

        ID of the agent that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookAgentDeletedEventData: …`

      - `type: Literal["agent.deleted"]`

      - `id: str`

        ID of the agent that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentPausedEventData: …`

      - `type: Literal["deployment.paused"]`

      - `id: str`

        ID of the deployment that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentRunFailedEventData: …`

      - `type: Literal["deployment_run.failed"]`

      - `id: str`

        ID of the deployment run that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentCreatedEventData: …`

      - `type: Literal["deployment.created"]`

      - `id: str`

        ID of the deployment that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentUpdatedEventData: …`

      - `type: Literal["deployment.updated"]`

      - `id: str`

        ID of the deployment that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentUnpausedEventData: …`

      - `type: Literal["deployment.unpaused"]`

      - `id: str`

        ID of the deployment that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookAgentUpdatedEventData: …`

      - `type: Literal["agent.updated"]`

      - `id: str`

        ID of the agent that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentArchivedEventData: …`

      - `type: Literal["deployment.archived"]`

      - `id: str`

        ID of the deployment that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentRunStartedEventData: …`

      - `type: Literal["deployment_run.started"]`

      - `id: str`

        ID of the deployment run that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentDeletedEventData: …`

      - `type: Literal["deployment.deleted"]`

      - `id: str`

        ID of the deployment that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookDeploymentRunSucceededEventData: …`

      - `type: Literal["deployment_run.succeeded"]`

      - `id: str`

        ID of the deployment run that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookEnvironmentCreatedEventData: …`

      - `type: Literal["environment.created"]`

      - `id: str`

        ID of the environment that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookEnvironmentUpdatedEventData: …`

      - `type: Literal["environment.updated"]`

      - `id: str`

        ID of the environment that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookEnvironmentArchivedEventData: …`

      - `type: Literal["environment.archived"]`

      - `id: str`

        ID of the environment that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookEnvironmentDeletedEventData: …`

      - `type: Literal["environment.deleted"]`

      - `id: str`

        ID of the environment that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookMemoryStoreCreatedEventData: …`

      - `type: Literal["memory_store.created"]`

      - `id: str`

        ID of the memory store that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookMemoryStoreArchivedEventData: …`

      - `type: Literal["memory_store.archived"]`

      - `id: str`

        ID of the memory store that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookMemoryStoreDeletedEventData: …`

      - `type: Literal["memory_store.deleted"]`

      - `id: str`

        ID of the memory store that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

    - `class BetaWebhookSessionBudgetReachedEventData: …`

      - `type: Literal["session.budget_reached"]`

      - `id: str`

        ID of the session that triggered the event.

      - `organization_id: str`

      - `workspace_id: str`

### Beta Webhook Event Data

- `BetaWebhookEventData`

  - `class BetaWebhookSessionCreatedEventData: …`

    - `type: Literal["session.created"]`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `workspace_id: str`

  - `class BetaWebhookSessionPendingEventData: …`

    - `type: Literal["session.pending"]`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `workspace_id: str`

  - `class BetaWebhookSessionRunningEventData: …`

    - `type: Literal["session.running"]`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `workspace_id: str`

  - `class BetaWebhookSessionIdledEventData: …`

    - `type: Literal["session.idled"]`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `workspace_id: str`

  - `class BetaWebhookSessionRequiresActionEventData: …`

    - `type: Literal["session.requires_action"]`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `workspace_id: str`

  - `class BetaWebhookSessionArchivedEventData: …`

    - `type: Literal["session.archived"]`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `workspace_id: str`

  - `class BetaWebhookSessionDeletedEventData: …`

    - `type: Literal["session.deleted"]`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `workspace_id: str`

  - `class BetaWebhookSessionStatusRescheduledEventData: …`

    - `type: Literal["session.status_rescheduled"]`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `workspace_id: str`

  - `class BetaWebhookSessionStatusRunStartedEventData: …`

    - `type: Literal["session.status_run_started"]`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `workspace_id: str`

  - `class BetaWebhookSessionStatusIdledEventData: …`

    - `type: Literal["session.status_idled"]`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `workspace_id: str`

  - `class BetaWebhookSessionStatusTerminatedEventData: …`

    - `type: Literal["session.status_terminated"]`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `workspace_id: str`

  - `class BetaWebhookSessionThreadCreatedEventData: …`

    - `type: Literal["session.thread_created"]`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `session_thread_id: str`

      ID of the session thread this event refers to.

    - `workspace_id: str`

  - `class BetaWebhookSessionThreadIdledEventData: …`

    - `type: Literal["session.thread_idled"]`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `session_thread_id: str`

      ID of the session thread this event refers to.

    - `workspace_id: str`

  - `class BetaWebhookSessionThreadTerminatedEventData: …`

    - `type: Literal["session.thread_terminated"]`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `session_thread_id: str`

      ID of the session thread this event refers to.

    - `workspace_id: str`

  - `class BetaWebhookSessionOutcomeEvaluationEndedEventData: …`

    - `type: Literal["session.outcome_evaluation_ended"]`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `workspace_id: str`

  - `class BetaWebhookVaultCreatedEventData: …`

    - `type: Literal["vault.created"]`

    - `id: str`

      ID of the vault that triggered the event.

    - `organization_id: str`

    - `workspace_id: str`

  - `class BetaWebhookVaultArchivedEventData: …`

    - `type: Literal["vault.archived"]`

    - `id: str`

      ID of the vault that triggered the event.

    - `organization_id: str`

    - `workspace_id: str`

  - `class BetaWebhookVaultDeletedEventData: …`

    - `type: Literal["vault.deleted"]`

    - `id: str`

      ID of the vault that triggered the event.

    - `organization_id: str`

    - `workspace_id: str`

  - `class BetaWebhookVaultCredentialCreatedEventData: …`

    - `type: Literal["vault_credential.created"]`

    - `id: str`

      ID of the vault credential that triggered the event.

    - `organization_id: str`

    - `vault_id: str`

      ID of the vault that owns this credential.

    - `workspace_id: str`

  - `class BetaWebhookVaultCredentialArchivedEventData: …`

    - `type: Literal["vault_credential.archived"]`

    - `id: str`

      ID of the vault credential that triggered the event.

    - `organization_id: str`

    - `vault_id: str`

      ID of the vault that owns this credential.

    - `workspace_id: str`

  - `class BetaWebhookVaultCredentialDeletedEventData: …`

    - `type: Literal["vault_credential.deleted"]`

    - `id: str`

      ID of the vault credential that triggered the event.

    - `organization_id: str`

    - `vault_id: str`

      ID of the vault that owns this credential.

    - `workspace_id: str`

  - `class BetaWebhookVaultCredentialRefreshFailedEventData: …`

    - `type: Literal["vault_credential.refresh_failed"]`

    - `id: str`

      ID of the vault credential that triggered the event.

    - `organization_id: str`

    - `vault_id: str`

      ID of the vault that owns this credential.

    - `workspace_id: str`

  - `class BetaWebhookSessionUpdatedEventData: …`

    - `type: Literal["session.updated"]`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `workspace_id: str`

  - `class BetaWebhookAgentCreatedEventData: …`

    - `type: Literal["agent.created"]`

    - `id: str`

      ID of the agent that triggered the event.

    - `organization_id: str`

    - `workspace_id: str`

  - `class BetaWebhookAgentArchivedEventData: …`

    - `type: Literal["agent.archived"]`

    - `id: str`

      ID of the agent that triggered the event.

    - `organization_id: str`

    - `workspace_id: str`

  - `class BetaWebhookAgentDeletedEventData: …`

    - `type: Literal["agent.deleted"]`

    - `id: str`

      ID of the agent that triggered the event.

    - `organization_id: str`

    - `workspace_id: str`

  - `class BetaWebhookDeploymentPausedEventData: …`

    - `type: Literal["deployment.paused"]`

    - `id: str`

      ID of the deployment that triggered the event.

    - `organization_id: str`

    - `workspace_id: str`

  - `class BetaWebhookDeploymentRunFailedEventData: …`

    - `type: Literal["deployment_run.failed"]`

    - `id: str`

      ID of the deployment run that triggered the event.

    - `organization_id: str`

    - `workspace_id: str`

  - `class BetaWebhookDeploymentCreatedEventData: …`

    - `type: Literal["deployment.created"]`

    - `id: str`

      ID of the deployment that triggered the event.

    - `organization_id: str`

    - `workspace_id: str`

  - `class BetaWebhookDeploymentUpdatedEventData: …`

    - `type: Literal["deployment.updated"]`

    - `id: str`

      ID of the deployment that triggered the event.

    - `organization_id: str`

    - `workspace_id: str`

  - `class BetaWebhookDeploymentUnpausedEventData: …`

    - `type: Literal["deployment.unpaused"]`

    - `id: str`

      ID of the deployment that triggered the event.

    - `organization_id: str`

    - `workspace_id: str`

  - `class BetaWebhookAgentUpdatedEventData: …`

    - `type: Literal["agent.updated"]`

    - `id: str`

      ID of the agent that triggered the event.

    - `organization_id: str`

    - `workspace_id: str`

  - `class BetaWebhookDeploymentArchivedEventData: …`

    - `type: Literal["deployment.archived"]`

    - `id: str`

      ID of the deployment that triggered the event.

    - `organization_id: str`

    - `workspace_id: str`

  - `class BetaWebhookDeploymentRunStartedEventData: …`

    - `type: Literal["deployment_run.started"]`

    - `id: str`

      ID of the deployment run that triggered the event.

    - `organization_id: str`

    - `workspace_id: str`

  - `class BetaWebhookDeploymentDeletedEventData: …`

    - `type: Literal["deployment.deleted"]`

    - `id: str`

      ID of the deployment that triggered the event.

    - `organization_id: str`

    - `workspace_id: str`

  - `class BetaWebhookDeploymentRunSucceededEventData: …`

    - `type: Literal["deployment_run.succeeded"]`

    - `id: str`

      ID of the deployment run that triggered the event.

    - `organization_id: str`

    - `workspace_id: str`

  - `class BetaWebhookEnvironmentCreatedEventData: …`

    - `type: Literal["environment.created"]`

    - `id: str`

      ID of the environment that triggered the event.

    - `organization_id: str`

    - `workspace_id: str`

  - `class BetaWebhookEnvironmentUpdatedEventData: …`

    - `type: Literal["environment.updated"]`

    - `id: str`

      ID of the environment that triggered the event.

    - `organization_id: str`

    - `workspace_id: str`

  - `class BetaWebhookEnvironmentArchivedEventData: …`

    - `type: Literal["environment.archived"]`

    - `id: str`

      ID of the environment that triggered the event.

    - `organization_id: str`

    - `workspace_id: str`

  - `class BetaWebhookEnvironmentDeletedEventData: …`

    - `type: Literal["environment.deleted"]`

    - `id: str`

      ID of the environment that triggered the event.

    - `organization_id: str`

    - `workspace_id: str`

  - `class BetaWebhookMemoryStoreCreatedEventData: …`

    - `type: Literal["memory_store.created"]`

    - `id: str`

      ID of the memory store that triggered the event.

    - `organization_id: str`

    - `workspace_id: str`

  - `class BetaWebhookMemoryStoreArchivedEventData: …`

    - `type: Literal["memory_store.archived"]`

    - `id: str`

      ID of the memory store that triggered the event.

    - `organization_id: str`

    - `workspace_id: str`

  - `class BetaWebhookMemoryStoreDeletedEventData: …`

    - `type: Literal["memory_store.deleted"]`

    - `id: str`

      ID of the memory store that triggered the event.

    - `organization_id: str`

    - `workspace_id: str`

  - `class BetaWebhookSessionBudgetReachedEventData: …`

    - `type: Literal["session.budget_reached"]`

    - `id: str`

      ID of the session that triggered the event.

    - `organization_id: str`

    - `workspace_id: str`

### Beta Webhook Memory Store Archived Event Data

- `class BetaWebhookMemoryStoreArchivedEventData: …`

  - `type: Literal["memory_store.archived"]`

  - `id: str`

    ID of the memory store that triggered the event.

  - `organization_id: str`

  - `workspace_id: str`

### Beta Webhook Memory Store Created Event Data

- `class BetaWebhookMemoryStoreCreatedEventData: …`

  - `type: Literal["memory_store.created"]`

  - `id: str`

    ID of the memory store that triggered the event.

  - `organization_id: str`

  - `workspace_id: str`

### Beta Webhook Memory Store Deleted Event Data

- `class BetaWebhookMemoryStoreDeletedEventData: …`

  - `type: Literal["memory_store.deleted"]`

  - `id: str`

    ID of the memory store that triggered the event.

  - `organization_id: str`

  - `workspace_id: str`

### Beta Webhook Session Archived Event Data

- `class BetaWebhookSessionArchivedEventData: …`

  - `type: Literal["session.archived"]`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `workspace_id: str`

### Beta Webhook Session Budget Reached Event Data

- `class BetaWebhookSessionBudgetReachedEventData: …`

  - `type: Literal["session.budget_reached"]`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `workspace_id: str`

### Beta Webhook Session Created Event Data

- `class BetaWebhookSessionCreatedEventData: …`

  - `type: Literal["session.created"]`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `workspace_id: str`

### Beta Webhook Session Deleted Event Data

- `class BetaWebhookSessionDeletedEventData: …`

  - `type: Literal["session.deleted"]`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `workspace_id: str`

### Beta Webhook Session Idled Event Data

- `class BetaWebhookSessionIdledEventData: …`

  - `type: Literal["session.idled"]`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `workspace_id: str`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `class BetaWebhookSessionOutcomeEvaluationEndedEventData: …`

  - `type: Literal["session.outcome_evaluation_ended"]`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `workspace_id: str`

### Beta Webhook Session Pending Event Data

- `class BetaWebhookSessionPendingEventData: …`

  - `type: Literal["session.pending"]`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `workspace_id: str`

### Beta Webhook Session Requires Action Event Data

- `class BetaWebhookSessionRequiresActionEventData: …`

  - `type: Literal["session.requires_action"]`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `workspace_id: str`

### Beta Webhook Session Running Event Data

- `class BetaWebhookSessionRunningEventData: …`

  - `type: Literal["session.running"]`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `workspace_id: str`

### Beta Webhook Session Status Idled Event Data

- `class BetaWebhookSessionStatusIdledEventData: …`

  - `type: Literal["session.status_idled"]`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `workspace_id: str`

### Beta Webhook Session Status Rescheduled Event Data

- `class BetaWebhookSessionStatusRescheduledEventData: …`

  - `type: Literal["session.status_rescheduled"]`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `workspace_id: str`

### Beta Webhook Session Status Run Started Event Data

- `class BetaWebhookSessionStatusRunStartedEventData: …`

  - `type: Literal["session.status_run_started"]`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `workspace_id: str`

### Beta Webhook Session Status Terminated Event Data

- `class BetaWebhookSessionStatusTerminatedEventData: …`

  - `type: Literal["session.status_terminated"]`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `workspace_id: str`

### Beta Webhook Session Thread Created Event Data

- `class BetaWebhookSessionThreadCreatedEventData: …`

  - `type: Literal["session.thread_created"]`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `session_thread_id: str`

    ID of the session thread this event refers to.

  - `workspace_id: str`

### Beta Webhook Session Thread Idled Event Data

- `class BetaWebhookSessionThreadIdledEventData: …`

  - `type: Literal["session.thread_idled"]`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `session_thread_id: str`

    ID of the session thread this event refers to.

  - `workspace_id: str`

### Beta Webhook Session Thread Terminated Event Data

- `class BetaWebhookSessionThreadTerminatedEventData: …`

  - `type: Literal["session.thread_terminated"]`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `session_thread_id: str`

    ID of the session thread this event refers to.

  - `workspace_id: str`

### Beta Webhook Session Updated Event Data

- `class BetaWebhookSessionUpdatedEventData: …`

  - `type: Literal["session.updated"]`

  - `id: str`

    ID of the session that triggered the event.

  - `organization_id: str`

  - `workspace_id: str`

### Beta Webhook Vault Archived Event Data

- `class BetaWebhookVaultArchivedEventData: …`

  - `type: Literal["vault.archived"]`

  - `id: str`

    ID of the vault that triggered the event.

  - `organization_id: str`

  - `workspace_id: str`

### Beta Webhook Vault Created Event Data

- `class BetaWebhookVaultCreatedEventData: …`

  - `type: Literal["vault.created"]`

  - `id: str`

    ID of the vault that triggered the event.

  - `organization_id: str`

  - `workspace_id: str`

### Beta Webhook Vault Credential Archived Event Data

- `class BetaWebhookVaultCredentialArchivedEventData: …`

  - `type: Literal["vault_credential.archived"]`

  - `id: str`

    ID of the vault credential that triggered the event.

  - `organization_id: str`

  - `vault_id: str`

    ID of the vault that owns this credential.

  - `workspace_id: str`

### Beta Webhook Vault Credential Created Event Data

- `class BetaWebhookVaultCredentialCreatedEventData: …`

  - `type: Literal["vault_credential.created"]`

  - `id: str`

    ID of the vault credential that triggered the event.

  - `organization_id: str`

  - `vault_id: str`

    ID of the vault that owns this credential.

  - `workspace_id: str`

### Beta Webhook Vault Credential Deleted Event Data

- `class BetaWebhookVaultCredentialDeletedEventData: …`

  - `type: Literal["vault_credential.deleted"]`

  - `id: str`

    ID of the vault credential that triggered the event.

  - `organization_id: str`

  - `vault_id: str`

    ID of the vault that owns this credential.

  - `workspace_id: str`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `class BetaWebhookVaultCredentialRefreshFailedEventData: …`

  - `type: Literal["vault_credential.refresh_failed"]`

  - `id: str`

    ID of the vault credential that triggered the event.

  - `organization_id: str`

  - `vault_id: str`

    ID of the vault that owns this credential.

  - `workspace_id: str`

### Beta Webhook Vault Deleted Event Data

- `class BetaWebhookVaultDeletedEventData: …`

  - `type: Literal["vault.deleted"]`

  - `id: str`

    ID of the vault that triggered the event.

  - `organization_id: str`

  - `workspace_id: str`
