---
title: Webhooks
url: https://platform.claude.com/docs/en/api/php/beta/webhooks
---

# Webhooks

## Domain types

### Beta Webhook Agent Archived Event Data

- `class BetaWebhookAgentArchivedEventData`

  - `"agent.archived" type`

  - `string id`

    ID of the agent that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Agent Created Event Data

- `class BetaWebhookAgentCreatedEventData`

  - `"agent.created" type`

  - `string id`

    ID of the agent that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Agent Deleted Event Data

- `class BetaWebhookAgentDeletedEventData`

  - `"agent.deleted" type`

  - `string id`

    ID of the agent that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Agent Updated Event Data

- `class BetaWebhookAgentUpdatedEventData`

  - `"agent.updated" type`

  - `string id`

    ID of the agent that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Deployment Archived Event Data

- `class BetaWebhookDeploymentArchivedEventData`

  - `"deployment.archived" type`

  - `string id`

    ID of the deployment that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Deployment Created Event Data

- `class BetaWebhookDeploymentCreatedEventData`

  - `"deployment.created" type`

  - `string id`

    ID of the deployment that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Deployment Deleted Event Data

- `class BetaWebhookDeploymentDeletedEventData`

  - `"deployment.deleted" type`

  - `string id`

    ID of the deployment that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Deployment Paused Event Data

- `class BetaWebhookDeploymentPausedEventData`

  - `"deployment.paused" type`

  - `string id`

    ID of the deployment that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Deployment Run Failed Event Data

- `class BetaWebhookDeploymentRunFailedEventData`

  - `"deployment_run.failed" type`

  - `string id`

    ID of the deployment run that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Deployment Run Started Event Data

- `class BetaWebhookDeploymentRunStartedEventData`

  - `"deployment_run.started" type`

  - `string id`

    ID of the deployment run that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Deployment Run Succeeded Event Data

- `class BetaWebhookDeploymentRunSucceededEventData`

  - `"deployment_run.succeeded" type`

  - `string id`

    ID of the deployment run that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Deployment Unpaused Event Data

- `class BetaWebhookDeploymentUnpausedEventData`

  - `"deployment.unpaused" type`

  - `string id`

    ID of the deployment that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Deployment Updated Event Data

- `class BetaWebhookDeploymentUpdatedEventData`

  - `"deployment.updated" type`

  - `string id`

    ID of the deployment that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Environment Archived Event Data

- `class BetaWebhookEnvironmentArchivedEventData`

  - `"environment.archived" type`

  - `string id`

    ID of the environment that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Environment Created Event Data

- `class BetaWebhookEnvironmentCreatedEventData`

  - `"environment.created" type`

  - `string id`

    ID of the environment that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Environment Deleted Event Data

- `class BetaWebhookEnvironmentDeletedEventData`

  - `"environment.deleted" type`

  - `string id`

    ID of the environment that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Environment Updated Event Data

- `class BetaWebhookEnvironmentUpdatedEventData`

  - `"environment.updated" type`

  - `string id`

    ID of the environment that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Event

- `class BetaWebhookEvent`

  - `"event" type`

    Object type. Always `event` for webhook payloads.

  - `string id`

    Unique event identifier for idempotency.

  - `\Datetime createdAt`

    RFC 3339 timestamp when the event occurred.

  - `BetaWebhookEventData data`

### Beta Webhook Event Data

- `class BetaWebhookEventData`

  - `class BetaWebhookSessionCreatedEventData`

    - `"session.created" type`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `class BetaWebhookSessionPendingEventData`

    - `"session.pending" type`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `class BetaWebhookSessionRunningEventData`

    - `"session.running" type`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `class BetaWebhookSessionIdledEventData`

    - `"session.idled" type`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `class BetaWebhookSessionRequiresActionEventData`

    - `"session.requires_action" type`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `class BetaWebhookSessionArchivedEventData`

    - `"session.archived" type`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `class BetaWebhookSessionDeletedEventData`

    - `"session.deleted" type`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `class BetaWebhookSessionStatusRescheduledEventData`

    - `"session.status_rescheduled" type`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `class BetaWebhookSessionStatusRunStartedEventData`

    - `"session.status_run_started" type`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `class BetaWebhookSessionStatusIdledEventData`

    - `"session.status_idled" type`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `class BetaWebhookSessionStatusTerminatedEventData`

    - `"session.status_terminated" type`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `class BetaWebhookSessionThreadCreatedEventData`

    - `"session.thread_created" type`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `string sessionThreadID`

      ID of the session thread this event refers to.

    - `string workspaceID`

  - `class BetaWebhookSessionThreadIdledEventData`

    - `"session.thread_idled" type`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `string sessionThreadID`

      ID of the session thread this event refers to.

    - `string workspaceID`

  - `class BetaWebhookSessionThreadTerminatedEventData`

    - `"session.thread_terminated" type`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `string sessionThreadID`

      ID of the session thread this event refers to.

    - `string workspaceID`

  - `class BetaWebhookSessionOutcomeEvaluationEndedEventData`

    - `"session.outcome_evaluation_ended" type`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `class BetaWebhookVaultCreatedEventData`

    - `"vault.created" type`

    - `string id`

      ID of the vault that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `class BetaWebhookVaultArchivedEventData`

    - `"vault.archived" type`

    - `string id`

      ID of the vault that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `class BetaWebhookVaultDeletedEventData`

    - `"vault.deleted" type`

    - `string id`

      ID of the vault that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `class BetaWebhookVaultCredentialCreatedEventData`

    - `"vault_credential.created" type`

    - `string id`

      ID of the vault credential that triggered the event.

    - `string organizationID`

    - `string vaultID`

      ID of the vault that owns this credential.

    - `string workspaceID`

  - `class BetaWebhookVaultCredentialArchivedEventData`

    - `"vault_credential.archived" type`

    - `string id`

      ID of the vault credential that triggered the event.

    - `string organizationID`

    - `string vaultID`

      ID of the vault that owns this credential.

    - `string workspaceID`

  - `class BetaWebhookVaultCredentialDeletedEventData`

    - `"vault_credential.deleted" type`

    - `string id`

      ID of the vault credential that triggered the event.

    - `string organizationID`

    - `string vaultID`

      ID of the vault that owns this credential.

    - `string workspaceID`

  - `class BetaWebhookVaultCredentialRefreshFailedEventData`

    - `"vault_credential.refresh_failed" type`

    - `string id`

      ID of the vault credential that triggered the event.

    - `string organizationID`

    - `string vaultID`

      ID of the vault that owns this credential.

    - `string workspaceID`

  - `class BetaWebhookSessionUpdatedEventData`

    - `"session.updated" type`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `class BetaWebhookAgentCreatedEventData`

    - `"agent.created" type`

    - `string id`

      ID of the agent that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `class BetaWebhookAgentArchivedEventData`

    - `"agent.archived" type`

    - `string id`

      ID of the agent that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `class BetaWebhookAgentDeletedEventData`

    - `"agent.deleted" type`

    - `string id`

      ID of the agent that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `class BetaWebhookDeploymentPausedEventData`

    - `"deployment.paused" type`

    - `string id`

      ID of the deployment that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `class BetaWebhookDeploymentRunFailedEventData`

    - `"deployment_run.failed" type`

    - `string id`

      ID of the deployment run that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `class BetaWebhookDeploymentCreatedEventData`

    - `"deployment.created" type`

    - `string id`

      ID of the deployment that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `class BetaWebhookDeploymentUpdatedEventData`

    - `"deployment.updated" type`

    - `string id`

      ID of the deployment that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `class BetaWebhookDeploymentUnpausedEventData`

    - `"deployment.unpaused" type`

    - `string id`

      ID of the deployment that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `class BetaWebhookAgentUpdatedEventData`

    - `"agent.updated" type`

    - `string id`

      ID of the agent that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `class BetaWebhookDeploymentArchivedEventData`

    - `"deployment.archived" type`

    - `string id`

      ID of the deployment that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `class BetaWebhookDeploymentRunStartedEventData`

    - `"deployment_run.started" type`

    - `string id`

      ID of the deployment run that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `class BetaWebhookDeploymentDeletedEventData`

    - `"deployment.deleted" type`

    - `string id`

      ID of the deployment that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `class BetaWebhookDeploymentRunSucceededEventData`

    - `"deployment_run.succeeded" type`

    - `string id`

      ID of the deployment run that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `class BetaWebhookEnvironmentCreatedEventData`

    - `"environment.created" type`

    - `string id`

      ID of the environment that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `class BetaWebhookEnvironmentUpdatedEventData`

    - `"environment.updated" type`

    - `string id`

      ID of the environment that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `class BetaWebhookEnvironmentArchivedEventData`

    - `"environment.archived" type`

    - `string id`

      ID of the environment that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `class BetaWebhookEnvironmentDeletedEventData`

    - `"environment.deleted" type`

    - `string id`

      ID of the environment that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `class BetaWebhookMemoryStoreCreatedEventData`

    - `"memory_store.created" type`

    - `string id`

      ID of the memory store that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `class BetaWebhookMemoryStoreArchivedEventData`

    - `"memory_store.archived" type`

    - `string id`

      ID of the memory store that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `class BetaWebhookMemoryStoreDeletedEventData`

    - `"memory_store.deleted" type`

    - `string id`

      ID of the memory store that triggered the event.

    - `string organizationID`

    - `string workspaceID`

  - `class BetaWebhookSessionBudgetReachedEventData`

    - `"session.budget_reached" type`

    - `string id`

      ID of the session that triggered the event.

    - `string organizationID`

    - `string workspaceID`

### Beta Webhook Memory Store Archived Event Data

- `class BetaWebhookMemoryStoreArchivedEventData`

  - `"memory_store.archived" type`

  - `string id`

    ID of the memory store that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Memory Store Created Event Data

- `class BetaWebhookMemoryStoreCreatedEventData`

  - `"memory_store.created" type`

  - `string id`

    ID of the memory store that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Memory Store Deleted Event Data

- `class BetaWebhookMemoryStoreDeletedEventData`

  - `"memory_store.deleted" type`

  - `string id`

    ID of the memory store that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Session Archived Event Data

- `class BetaWebhookSessionArchivedEventData`

  - `"session.archived" type`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Session Budget Reached Event Data

- `class BetaWebhookSessionBudgetReachedEventData`

  - `"session.budget_reached" type`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Session Created Event Data

- `class BetaWebhookSessionCreatedEventData`

  - `"session.created" type`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Session Deleted Event Data

- `class BetaWebhookSessionDeletedEventData`

  - `"session.deleted" type`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Session Idled Event Data

- `class BetaWebhookSessionIdledEventData`

  - `"session.idled" type`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `class BetaWebhookSessionOutcomeEvaluationEndedEventData`

  - `"session.outcome_evaluation_ended" type`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Session Pending Event Data

- `class BetaWebhookSessionPendingEventData`

  - `"session.pending" type`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Session Requires Action Event Data

- `class BetaWebhookSessionRequiresActionEventData`

  - `"session.requires_action" type`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Session Running Event Data

- `class BetaWebhookSessionRunningEventData`

  - `"session.running" type`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Session Status Idled Event Data

- `class BetaWebhookSessionStatusIdledEventData`

  - `"session.status_idled" type`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Session Status Rescheduled Event Data

- `class BetaWebhookSessionStatusRescheduledEventData`

  - `"session.status_rescheduled" type`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Session Status Run Started Event Data

- `class BetaWebhookSessionStatusRunStartedEventData`

  - `"session.status_run_started" type`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Session Status Terminated Event Data

- `class BetaWebhookSessionStatusTerminatedEventData`

  - `"session.status_terminated" type`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Session Thread Created Event Data

- `class BetaWebhookSessionThreadCreatedEventData`

  - `"session.thread_created" type`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `string sessionThreadID`

    ID of the session thread this event refers to.

  - `string workspaceID`

### Beta Webhook Session Thread Idled Event Data

- `class BetaWebhookSessionThreadIdledEventData`

  - `"session.thread_idled" type`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `string sessionThreadID`

    ID of the session thread this event refers to.

  - `string workspaceID`

### Beta Webhook Session Thread Terminated Event Data

- `class BetaWebhookSessionThreadTerminatedEventData`

  - `"session.thread_terminated" type`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `string sessionThreadID`

    ID of the session thread this event refers to.

  - `string workspaceID`

### Beta Webhook Session Updated Event Data

- `class BetaWebhookSessionUpdatedEventData`

  - `"session.updated" type`

  - `string id`

    ID of the session that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Vault Archived Event Data

- `class BetaWebhookVaultArchivedEventData`

  - `"vault.archived" type`

  - `string id`

    ID of the vault that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Vault Created Event Data

- `class BetaWebhookVaultCreatedEventData`

  - `"vault.created" type`

  - `string id`

    ID of the vault that triggered the event.

  - `string organizationID`

  - `string workspaceID`

### Beta Webhook Vault Credential Archived Event Data

- `class BetaWebhookVaultCredentialArchivedEventData`

  - `"vault_credential.archived" type`

  - `string id`

    ID of the vault credential that triggered the event.

  - `string organizationID`

  - `string vaultID`

    ID of the vault that owns this credential.

  - `string workspaceID`

### Beta Webhook Vault Credential Created Event Data

- `class BetaWebhookVaultCredentialCreatedEventData`

  - `"vault_credential.created" type`

  - `string id`

    ID of the vault credential that triggered the event.

  - `string organizationID`

  - `string vaultID`

    ID of the vault that owns this credential.

  - `string workspaceID`

### Beta Webhook Vault Credential Deleted Event Data

- `class BetaWebhookVaultCredentialDeletedEventData`

  - `"vault_credential.deleted" type`

  - `string id`

    ID of the vault credential that triggered the event.

  - `string organizationID`

  - `string vaultID`

    ID of the vault that owns this credential.

  - `string workspaceID`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `class BetaWebhookVaultCredentialRefreshFailedEventData`

  - `"vault_credential.refresh_failed" type`

  - `string id`

    ID of the vault credential that triggered the event.

  - `string organizationID`

  - `string vaultID`

    ID of the vault that owns this credential.

  - `string workspaceID`

### Beta Webhook Vault Deleted Event Data

- `class BetaWebhookVaultDeletedEventData`

  - `"vault.deleted" type`

  - `string id`

    ID of the vault that triggered the event.

  - `string organizationID`

  - `string workspaceID`
