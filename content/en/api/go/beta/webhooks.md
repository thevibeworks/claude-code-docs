---
title: Webhooks
url: https://platform.claude.com/docs/en/api/go/beta/webhooks
---

# Webhooks

## Domain types

### Beta Webhook Agent Archived Event Data

- `type BetaWebhookAgentArchivedEventData`

  - `Type AgentArchived`

  - `ID string`

    ID of the agent that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Agent Created Event Data

- `type BetaWebhookAgentCreatedEventData`

  - `Type AgentCreated`

  - `ID string`

    ID of the agent that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Agent Deleted Event Data

- `type BetaWebhookAgentDeletedEventData`

  - `Type AgentDeleted`

  - `ID string`

    ID of the agent that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Agent Updated Event Data

- `type BetaWebhookAgentUpdatedEventData`

  - `Type AgentUpdated`

  - `ID string`

    ID of the agent that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Deployment Archived Event Data

- `type BetaWebhookDeploymentArchivedEventData`

  - `Type DeploymentArchived`

  - `ID string`

    ID of the deployment that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Deployment Created Event Data

- `type BetaWebhookDeploymentCreatedEventData`

  - `Type DeploymentCreated`

  - `ID string`

    ID of the deployment that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Deployment Deleted Event Data

- `type BetaWebhookDeploymentDeletedEventData`

  - `Type DeploymentDeleted`

  - `ID string`

    ID of the deployment that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Deployment Paused Event Data

- `type BetaWebhookDeploymentPausedEventData`

  - `Type DeploymentPaused`

  - `ID string`

    ID of the deployment that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Deployment Run Failed Event Data

- `type BetaWebhookDeploymentRunFailedEventData`

  - `Type DeploymentRunFailed`

  - `ID string`

    ID of the deployment run that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Deployment Run Started Event Data

- `type BetaWebhookDeploymentRunStartedEventData`

  - `Type DeploymentRunStarted`

  - `ID string`

    ID of the deployment run that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Deployment Run Succeeded Event Data

- `type BetaWebhookDeploymentRunSucceededEventData`

  - `Type DeploymentRunSucceeded`

  - `ID string`

    ID of the deployment run that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Deployment Unpaused Event Data

- `type BetaWebhookDeploymentUnpausedEventData`

  - `Type DeploymentUnpaused`

  - `ID string`

    ID of the deployment that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Deployment Updated Event Data

- `type BetaWebhookDeploymentUpdatedEventData`

  - `Type DeploymentUpdated`

  - `ID string`

    ID of the deployment that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Environment Archived Event Data

- `type BetaWebhookEnvironmentArchivedEventData`

  - `Type EnvironmentArchived`

  - `ID string`

    ID of the environment that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Environment Created Event Data

- `type BetaWebhookEnvironmentCreatedEventData`

  - `Type EnvironmentCreated`

  - `ID string`

    ID of the environment that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Environment Deleted Event Data

- `type BetaWebhookEnvironmentDeletedEventData`

  - `Type EnvironmentDeleted`

  - `ID string`

    ID of the environment that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Environment Updated Event Data

- `type BetaWebhookEnvironmentUpdatedEventData`

  - `Type EnvironmentUpdated`

  - `ID string`

    ID of the environment that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Event

- `type UnwrapWebhookEvent`

  - `Type Event`

    Object type. Always `event` for webhook payloads.

  - `ID string`

    Unique event identifier for idempotency.

  - `CreatedAt Time`

    RFC 3339 timestamp when the event occurred.

    format: date-time

  - `Data BetaWebhookEventDataUnion`

    - `type BetaWebhookSessionCreatedEventData`

      - `Type SessionCreated`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookSessionPendingEventData`

      - `Type SessionPending`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookSessionRunningEventData`

      - `Type SessionRunning`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookSessionIdledEventData`

      - `Type SessionIdled`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookSessionRequiresActionEventData`

      - `Type SessionRequiresAction`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookSessionArchivedEventData`

      - `Type SessionArchived`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookSessionDeletedEventData`

      - `Type SessionDeleted`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusRescheduledEventData`

      - `Type SessionStatusRescheduled`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusRunStartedEventData`

      - `Type SessionStatusRunStarted`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusIdledEventData`

      - `Type SessionStatusIdled`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusTerminatedEventData`

      - `Type SessionStatusTerminated`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookSessionThreadCreatedEventData`

      - `Type SessionThreadCreated`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `SessionThreadID string`

        ID of the session thread this event refers to.

      - `WorkspaceID string`

    - `type BetaWebhookSessionThreadIdledEventData`

      - `Type SessionThreadIdled`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `SessionThreadID string`

        ID of the session thread this event refers to.

      - `WorkspaceID string`

    - `type BetaWebhookSessionThreadTerminatedEventData`

      - `Type SessionThreadTerminated`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `SessionThreadID string`

        ID of the session thread this event refers to.

      - `WorkspaceID string`

    - `type BetaWebhookSessionOutcomeEvaluationEndedEventData`

      - `Type SessionOutcomeEvaluationEnded`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookVaultCreatedEventData`

      - `Type VaultCreated`

      - `ID string`

        ID of the vault that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookVaultArchivedEventData`

      - `Type VaultArchived`

      - `ID string`

        ID of the vault that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookVaultDeletedEventData`

      - `Type VaultDeleted`

      - `ID string`

        ID of the vault that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialCreatedEventData`

      - `Type VaultCredentialCreated`

      - `ID string`

        ID of the vault credential that triggered the event.

      - `OrganizationID string`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialArchivedEventData`

      - `Type VaultCredentialArchived`

      - `ID string`

        ID of the vault credential that triggered the event.

      - `OrganizationID string`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialDeletedEventData`

      - `Type VaultCredentialDeleted`

      - `ID string`

        ID of the vault credential that triggered the event.

      - `OrganizationID string`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialRefreshFailedEventData`

      - `Type VaultCredentialRefreshFailed`

      - `ID string`

        ID of the vault credential that triggered the event.

      - `OrganizationID string`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookSessionUpdatedEventData`

      - `Type SessionUpdated`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookAgentCreatedEventData`

      - `Type AgentCreated`

      - `ID string`

        ID of the agent that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookAgentArchivedEventData`

      - `Type AgentArchived`

      - `ID string`

        ID of the agent that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookAgentDeletedEventData`

      - `Type AgentDeleted`

      - `ID string`

        ID of the agent that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentPausedEventData`

      - `Type DeploymentPaused`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentRunFailedEventData`

      - `Type DeploymentRunFailed`

      - `ID string`

        ID of the deployment run that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentCreatedEventData`

      - `Type DeploymentCreated`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentUpdatedEventData`

      - `Type DeploymentUpdated`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentUnpausedEventData`

      - `Type DeploymentUnpaused`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookAgentUpdatedEventData`

      - `Type AgentUpdated`

      - `ID string`

        ID of the agent that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentArchivedEventData`

      - `Type DeploymentArchived`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentRunStartedEventData`

      - `Type DeploymentRunStarted`

      - `ID string`

        ID of the deployment run that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentDeletedEventData`

      - `Type DeploymentDeleted`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentRunSucceededEventData`

      - `Type DeploymentRunSucceeded`

      - `ID string`

        ID of the deployment run that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookEnvironmentCreatedEventData`

      - `Type EnvironmentCreated`

      - `ID string`

        ID of the environment that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookEnvironmentUpdatedEventData`

      - `Type EnvironmentUpdated`

      - `ID string`

        ID of the environment that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookEnvironmentArchivedEventData`

      - `Type EnvironmentArchived`

      - `ID string`

        ID of the environment that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookEnvironmentDeletedEventData`

      - `Type EnvironmentDeleted`

      - `ID string`

        ID of the environment that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookMemoryStoreCreatedEventData`

      - `Type MemoryStoreCreated`

      - `ID string`

        ID of the memory store that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookMemoryStoreArchivedEventData`

      - `Type MemoryStoreArchived`

      - `ID string`

        ID of the memory store that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookMemoryStoreDeletedEventData`

      - `Type MemoryStoreDeleted`

      - `ID string`

        ID of the memory store that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookSessionBudgetReachedEventData`

      - `Type SessionBudgetReached`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

### Beta Webhook Event Data

- `type BetaWebhookEventDataUnion interface{…}`

  - `type BetaWebhookSessionCreatedEventData`

    - `Type SessionCreated`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookSessionPendingEventData`

    - `Type SessionPending`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookSessionRunningEventData`

    - `Type SessionRunning`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookSessionIdledEventData`

    - `Type SessionIdled`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookSessionRequiresActionEventData`

    - `Type SessionRequiresAction`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookSessionArchivedEventData`

    - `Type SessionArchived`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookSessionDeletedEventData`

    - `Type SessionDeleted`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookSessionStatusRescheduledEventData`

    - `Type SessionStatusRescheduled`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookSessionStatusRunStartedEventData`

    - `Type SessionStatusRunStarted`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookSessionStatusIdledEventData`

    - `Type SessionStatusIdled`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookSessionStatusTerminatedEventData`

    - `Type SessionStatusTerminated`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookSessionThreadCreatedEventData`

    - `Type SessionThreadCreated`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `SessionThreadID string`

      ID of the session thread this event refers to.

    - `WorkspaceID string`

  - `type BetaWebhookSessionThreadIdledEventData`

    - `Type SessionThreadIdled`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `SessionThreadID string`

      ID of the session thread this event refers to.

    - `WorkspaceID string`

  - `type BetaWebhookSessionThreadTerminatedEventData`

    - `Type SessionThreadTerminated`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `SessionThreadID string`

      ID of the session thread this event refers to.

    - `WorkspaceID string`

  - `type BetaWebhookSessionOutcomeEvaluationEndedEventData`

    - `Type SessionOutcomeEvaluationEnded`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookVaultCreatedEventData`

    - `Type VaultCreated`

    - `ID string`

      ID of the vault that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookVaultArchivedEventData`

    - `Type VaultArchived`

    - `ID string`

      ID of the vault that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookVaultDeletedEventData`

    - `Type VaultDeleted`

    - `ID string`

      ID of the vault that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookVaultCredentialCreatedEventData`

    - `Type VaultCredentialCreated`

    - `ID string`

      ID of the vault credential that triggered the event.

    - `OrganizationID string`

    - `VaultID string`

      ID of the vault that owns this credential.

    - `WorkspaceID string`

  - `type BetaWebhookVaultCredentialArchivedEventData`

    - `Type VaultCredentialArchived`

    - `ID string`

      ID of the vault credential that triggered the event.

    - `OrganizationID string`

    - `VaultID string`

      ID of the vault that owns this credential.

    - `WorkspaceID string`

  - `type BetaWebhookVaultCredentialDeletedEventData`

    - `Type VaultCredentialDeleted`

    - `ID string`

      ID of the vault credential that triggered the event.

    - `OrganizationID string`

    - `VaultID string`

      ID of the vault that owns this credential.

    - `WorkspaceID string`

  - `type BetaWebhookVaultCredentialRefreshFailedEventData`

    - `Type VaultCredentialRefreshFailed`

    - `ID string`

      ID of the vault credential that triggered the event.

    - `OrganizationID string`

    - `VaultID string`

      ID of the vault that owns this credential.

    - `WorkspaceID string`

  - `type BetaWebhookSessionUpdatedEventData`

    - `Type SessionUpdated`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookAgentCreatedEventData`

    - `Type AgentCreated`

    - `ID string`

      ID of the agent that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookAgentArchivedEventData`

    - `Type AgentArchived`

    - `ID string`

      ID of the agent that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookAgentDeletedEventData`

    - `Type AgentDeleted`

    - `ID string`

      ID of the agent that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentPausedEventData`

    - `Type DeploymentPaused`

    - `ID string`

      ID of the deployment that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentRunFailedEventData`

    - `Type DeploymentRunFailed`

    - `ID string`

      ID of the deployment run that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentCreatedEventData`

    - `Type DeploymentCreated`

    - `ID string`

      ID of the deployment that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentUpdatedEventData`

    - `Type DeploymentUpdated`

    - `ID string`

      ID of the deployment that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentUnpausedEventData`

    - `Type DeploymentUnpaused`

    - `ID string`

      ID of the deployment that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookAgentUpdatedEventData`

    - `Type AgentUpdated`

    - `ID string`

      ID of the agent that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentArchivedEventData`

    - `Type DeploymentArchived`

    - `ID string`

      ID of the deployment that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentRunStartedEventData`

    - `Type DeploymentRunStarted`

    - `ID string`

      ID of the deployment run that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentDeletedEventData`

    - `Type DeploymentDeleted`

    - `ID string`

      ID of the deployment that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentRunSucceededEventData`

    - `Type DeploymentRunSucceeded`

    - `ID string`

      ID of the deployment run that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookEnvironmentCreatedEventData`

    - `Type EnvironmentCreated`

    - `ID string`

      ID of the environment that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookEnvironmentUpdatedEventData`

    - `Type EnvironmentUpdated`

    - `ID string`

      ID of the environment that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookEnvironmentArchivedEventData`

    - `Type EnvironmentArchived`

    - `ID string`

      ID of the environment that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookEnvironmentDeletedEventData`

    - `Type EnvironmentDeleted`

    - `ID string`

      ID of the environment that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookMemoryStoreCreatedEventData`

    - `Type MemoryStoreCreated`

    - `ID string`

      ID of the memory store that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookMemoryStoreArchivedEventData`

    - `Type MemoryStoreArchived`

    - `ID string`

      ID of the memory store that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookMemoryStoreDeletedEventData`

    - `Type MemoryStoreDeleted`

    - `ID string`

      ID of the memory store that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookSessionBudgetReachedEventData`

    - `Type SessionBudgetReached`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

### Beta Webhook Memory Store Archived Event Data

- `type BetaWebhookMemoryStoreArchivedEventData`

  - `Type MemoryStoreArchived`

  - `ID string`

    ID of the memory store that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Memory Store Created Event Data

- `type BetaWebhookMemoryStoreCreatedEventData`

  - `Type MemoryStoreCreated`

  - `ID string`

    ID of the memory store that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Memory Store Deleted Event Data

- `type BetaWebhookMemoryStoreDeletedEventData`

  - `Type MemoryStoreDeleted`

  - `ID string`

    ID of the memory store that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Session Archived Event Data

- `type BetaWebhookSessionArchivedEventData`

  - `Type SessionArchived`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Session Budget Reached Event Data

- `type BetaWebhookSessionBudgetReachedEventData`

  - `Type SessionBudgetReached`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Session Created Event Data

- `type BetaWebhookSessionCreatedEventData`

  - `Type SessionCreated`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Session Deleted Event Data

- `type BetaWebhookSessionDeletedEventData`

  - `Type SessionDeleted`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Session Idled Event Data

- `type BetaWebhookSessionIdledEventData`

  - `Type SessionIdled`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `type BetaWebhookSessionOutcomeEvaluationEndedEventData`

  - `Type SessionOutcomeEvaluationEnded`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Session Pending Event Data

- `type BetaWebhookSessionPendingEventData`

  - `Type SessionPending`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Session Requires Action Event Data

- `type BetaWebhookSessionRequiresActionEventData`

  - `Type SessionRequiresAction`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Session Running Event Data

- `type BetaWebhookSessionRunningEventData`

  - `Type SessionRunning`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Session Status Idled Event Data

- `type BetaWebhookSessionStatusIdledEventData`

  - `Type SessionStatusIdled`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Session Status Rescheduled Event Data

- `type BetaWebhookSessionStatusRescheduledEventData`

  - `Type SessionStatusRescheduled`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Session Status Run Started Event Data

- `type BetaWebhookSessionStatusRunStartedEventData`

  - `Type SessionStatusRunStarted`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Session Status Terminated Event Data

- `type BetaWebhookSessionStatusTerminatedEventData`

  - `Type SessionStatusTerminated`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Session Thread Created Event Data

- `type BetaWebhookSessionThreadCreatedEventData`

  - `Type SessionThreadCreated`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `SessionThreadID string`

    ID of the session thread this event refers to.

  - `WorkspaceID string`

### Beta Webhook Session Thread Idled Event Data

- `type BetaWebhookSessionThreadIdledEventData`

  - `Type SessionThreadIdled`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `SessionThreadID string`

    ID of the session thread this event refers to.

  - `WorkspaceID string`

### Beta Webhook Session Thread Terminated Event Data

- `type BetaWebhookSessionThreadTerminatedEventData`

  - `Type SessionThreadTerminated`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `SessionThreadID string`

    ID of the session thread this event refers to.

  - `WorkspaceID string`

### Beta Webhook Session Updated Event Data

- `type BetaWebhookSessionUpdatedEventData`

  - `Type SessionUpdated`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Vault Archived Event Data

- `type BetaWebhookVaultArchivedEventData`

  - `Type VaultArchived`

  - `ID string`

    ID of the vault that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Vault Created Event Data

- `type BetaWebhookVaultCreatedEventData`

  - `Type VaultCreated`

  - `ID string`

    ID of the vault that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Vault Credential Archived Event Data

- `type BetaWebhookVaultCredentialArchivedEventData`

  - `Type VaultCredentialArchived`

  - `ID string`

    ID of the vault credential that triggered the event.

  - `OrganizationID string`

  - `VaultID string`

    ID of the vault that owns this credential.

  - `WorkspaceID string`

### Beta Webhook Vault Credential Created Event Data

- `type BetaWebhookVaultCredentialCreatedEventData`

  - `Type VaultCredentialCreated`

  - `ID string`

    ID of the vault credential that triggered the event.

  - `OrganizationID string`

  - `VaultID string`

    ID of the vault that owns this credential.

  - `WorkspaceID string`

### Beta Webhook Vault Credential Deleted Event Data

- `type BetaWebhookVaultCredentialDeletedEventData`

  - `Type VaultCredentialDeleted`

  - `ID string`

    ID of the vault credential that triggered the event.

  - `OrganizationID string`

  - `VaultID string`

    ID of the vault that owns this credential.

  - `WorkspaceID string`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `type BetaWebhookVaultCredentialRefreshFailedEventData`

  - `Type VaultCredentialRefreshFailed`

  - `ID string`

    ID of the vault credential that triggered the event.

  - `OrganizationID string`

  - `VaultID string`

    ID of the vault that owns this credential.

  - `WorkspaceID string`

### Beta Webhook Vault Deleted Event Data

- `type BetaWebhookVaultDeletedEventData`

  - `Type VaultDeleted`

  - `ID string`

    ID of the vault that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`
