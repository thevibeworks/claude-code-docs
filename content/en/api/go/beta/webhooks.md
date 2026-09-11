---
title: Webhooks
url: https://platform.claude.com/docs/en/api/go/beta/webhooks
---

# Webhooks

## Domain types

### Beta Webhook Agent Archived Event Data

- `type BetaWebhookAgentArchivedEventData struct{…}`

  - `Type AgentArchived`

  - `ID string`

    ID of the agent that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Agent Created Event Data

- `type BetaWebhookAgentCreatedEventData struct{…}`

  - `Type AgentCreated`

  - `ID string`

    ID of the agent that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Agent Deleted Event Data

- `type BetaWebhookAgentDeletedEventData struct{…}`

  - `Type AgentDeleted`

  - `ID string`

    ID of the agent that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Agent Updated Event Data

- `type BetaWebhookAgentUpdatedEventData struct{…}`

  - `Type AgentUpdated`

  - `ID string`

    ID of the agent that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Deployment Archived Event Data

- `type BetaWebhookDeploymentArchivedEventData struct{…}`

  - `Type DeploymentArchived`

  - `ID string`

    ID of the deployment that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Deployment Created Event Data

- `type BetaWebhookDeploymentCreatedEventData struct{…}`

  - `Type DeploymentCreated`

  - `ID string`

    ID of the deployment that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Deployment Deleted Event Data

- `type BetaWebhookDeploymentDeletedEventData struct{…}`

  - `Type DeploymentDeleted`

  - `ID string`

    ID of the deployment that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Deployment Paused Event Data

- `type BetaWebhookDeploymentPausedEventData struct{…}`

  - `Type DeploymentPaused`

  - `ID string`

    ID of the deployment that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Deployment Run Failed Event Data

- `type BetaWebhookDeploymentRunFailedEventData struct{…}`

  - `Type DeploymentRunFailed`

  - `ID string`

    ID of the deployment run that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Deployment Run Started Event Data

- `type BetaWebhookDeploymentRunStartedEventData struct{…}`

  - `Type DeploymentRunStarted`

  - `ID string`

    ID of the deployment run that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Deployment Run Succeeded Event Data

- `type BetaWebhookDeploymentRunSucceededEventData struct{…}`

  - `Type DeploymentRunSucceeded`

  - `ID string`

    ID of the deployment run that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Deployment Unpaused Event Data

- `type BetaWebhookDeploymentUnpausedEventData struct{…}`

  - `Type DeploymentUnpaused`

  - `ID string`

    ID of the deployment that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Deployment Updated Event Data

- `type BetaWebhookDeploymentUpdatedEventData struct{…}`

  - `Type DeploymentUpdated`

  - `ID string`

    ID of the deployment that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Environment Archived Event Data

- `type BetaWebhookEnvironmentArchivedEventData struct{…}`

  - `Type EnvironmentArchived`

  - `ID string`

    ID of the environment that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Environment Created Event Data

- `type BetaWebhookEnvironmentCreatedEventData struct{…}`

  - `Type EnvironmentCreated`

  - `ID string`

    ID of the environment that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Environment Deleted Event Data

- `type BetaWebhookEnvironmentDeletedEventData struct{…}`

  - `Type EnvironmentDeleted`

  - `ID string`

    ID of the environment that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Environment Updated Event Data

- `type BetaWebhookEnvironmentUpdatedEventData struct{…}`

  - `Type EnvironmentUpdated`

  - `ID string`

    ID of the environment that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Event

- `type UnwrapWebhookEvent struct{…}`

  - `Type Event`

    Object type. Always `event` for webhook payloads.

  - `ID string`

    Unique event identifier for idempotency.

  - `CreatedAt Time`

    RFC 3339 timestamp when the event occurred.

    format: date-time

  - `Data BetaWebhookEventDataUnion`

    - `type BetaWebhookSessionCreatedEventData struct{…}`

      - `Type SessionCreated`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookSessionPendingEventData struct{…}`

      - `Type SessionPending`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookSessionRunningEventData struct{…}`

      - `Type SessionRunning`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookSessionIdledEventData struct{…}`

      - `Type SessionIdled`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookSessionRequiresActionEventData struct{…}`

      - `Type SessionRequiresAction`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookSessionArchivedEventData struct{…}`

      - `Type SessionArchived`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookSessionDeletedEventData struct{…}`

      - `Type SessionDeleted`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusRescheduledEventData struct{…}`

      - `Type SessionStatusRescheduled`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusRunStartedEventData struct{…}`

      - `Type SessionStatusRunStarted`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusIdledEventData struct{…}`

      - `Type SessionStatusIdled`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusTerminatedEventData struct{…}`

      - `Type SessionStatusTerminated`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookSessionThreadCreatedEventData struct{…}`

      - `Type SessionThreadCreated`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `SessionThreadID string`

        ID of the session thread this event refers to.

      - `WorkspaceID string`

    - `type BetaWebhookSessionThreadIdledEventData struct{…}`

      - `Type SessionThreadIdled`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `SessionThreadID string`

        ID of the session thread this event refers to.

      - `WorkspaceID string`

    - `type BetaWebhookSessionThreadTerminatedEventData struct{…}`

      - `Type SessionThreadTerminated`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `SessionThreadID string`

        ID of the session thread this event refers to.

      - `WorkspaceID string`

    - `type BetaWebhookSessionOutcomeEvaluationEndedEventData struct{…}`

      - `Type SessionOutcomeEvaluationEnded`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookVaultCreatedEventData struct{…}`

      - `Type VaultCreated`

      - `ID string`

        ID of the vault that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookVaultArchivedEventData struct{…}`

      - `Type VaultArchived`

      - `ID string`

        ID of the vault that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookVaultDeletedEventData struct{…}`

      - `Type VaultDeleted`

      - `ID string`

        ID of the vault that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialCreatedEventData struct{…}`

      - `Type VaultCredentialCreated`

      - `ID string`

        ID of the vault credential that triggered the event.

      - `OrganizationID string`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialArchivedEventData struct{…}`

      - `Type VaultCredentialArchived`

      - `ID string`

        ID of the vault credential that triggered the event.

      - `OrganizationID string`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialDeletedEventData struct{…}`

      - `Type VaultCredentialDeleted`

      - `ID string`

        ID of the vault credential that triggered the event.

      - `OrganizationID string`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialRefreshFailedEventData struct{…}`

      - `Type VaultCredentialRefreshFailed`

      - `ID string`

        ID of the vault credential that triggered the event.

      - `OrganizationID string`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookSessionUpdatedEventData struct{…}`

      - `Type SessionUpdated`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookAgentCreatedEventData struct{…}`

      - `Type AgentCreated`

      - `ID string`

        ID of the agent that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookAgentArchivedEventData struct{…}`

      - `Type AgentArchived`

      - `ID string`

        ID of the agent that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookAgentDeletedEventData struct{…}`

      - `Type AgentDeleted`

      - `ID string`

        ID of the agent that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentPausedEventData struct{…}`

      - `Type DeploymentPaused`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentRunFailedEventData struct{…}`

      - `Type DeploymentRunFailed`

      - `ID string`

        ID of the deployment run that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentCreatedEventData struct{…}`

      - `Type DeploymentCreated`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentUpdatedEventData struct{…}`

      - `Type DeploymentUpdated`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentUnpausedEventData struct{…}`

      - `Type DeploymentUnpaused`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookAgentUpdatedEventData struct{…}`

      - `Type AgentUpdated`

      - `ID string`

        ID of the agent that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentArchivedEventData struct{…}`

      - `Type DeploymentArchived`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentRunStartedEventData struct{…}`

      - `Type DeploymentRunStarted`

      - `ID string`

        ID of the deployment run that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentDeletedEventData struct{…}`

      - `Type DeploymentDeleted`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentRunSucceededEventData struct{…}`

      - `Type DeploymentRunSucceeded`

      - `ID string`

        ID of the deployment run that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookEnvironmentCreatedEventData struct{…}`

      - `Type EnvironmentCreated`

      - `ID string`

        ID of the environment that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookEnvironmentUpdatedEventData struct{…}`

      - `Type EnvironmentUpdated`

      - `ID string`

        ID of the environment that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookEnvironmentArchivedEventData struct{…}`

      - `Type EnvironmentArchived`

      - `ID string`

        ID of the environment that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookEnvironmentDeletedEventData struct{…}`

      - `Type EnvironmentDeleted`

      - `ID string`

        ID of the environment that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookMemoryStoreCreatedEventData struct{…}`

      - `Type MemoryStoreCreated`

      - `ID string`

        ID of the memory store that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookMemoryStoreArchivedEventData struct{…}`

      - `Type MemoryStoreArchived`

      - `ID string`

        ID of the memory store that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookMemoryStoreDeletedEventData struct{…}`

      - `Type MemoryStoreDeleted`

      - `ID string`

        ID of the memory store that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

    - `type BetaWebhookSessionBudgetReachedEventData struct{…}`

      - `Type SessionBudgetReached`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `WorkspaceID string`

### Beta Webhook Event Data

- `type BetaWebhookEventDataUnion interface{…}`

  - `type BetaWebhookSessionCreatedEventData struct{…}`

    - `Type SessionCreated`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookSessionPendingEventData struct{…}`

    - `Type SessionPending`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookSessionRunningEventData struct{…}`

    - `Type SessionRunning`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookSessionIdledEventData struct{…}`

    - `Type SessionIdled`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookSessionRequiresActionEventData struct{…}`

    - `Type SessionRequiresAction`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookSessionArchivedEventData struct{…}`

    - `Type SessionArchived`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookSessionDeletedEventData struct{…}`

    - `Type SessionDeleted`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookSessionStatusRescheduledEventData struct{…}`

    - `Type SessionStatusRescheduled`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookSessionStatusRunStartedEventData struct{…}`

    - `Type SessionStatusRunStarted`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookSessionStatusIdledEventData struct{…}`

    - `Type SessionStatusIdled`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookSessionStatusTerminatedEventData struct{…}`

    - `Type SessionStatusTerminated`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookSessionThreadCreatedEventData struct{…}`

    - `Type SessionThreadCreated`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `SessionThreadID string`

      ID of the session thread this event refers to.

    - `WorkspaceID string`

  - `type BetaWebhookSessionThreadIdledEventData struct{…}`

    - `Type SessionThreadIdled`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `SessionThreadID string`

      ID of the session thread this event refers to.

    - `WorkspaceID string`

  - `type BetaWebhookSessionThreadTerminatedEventData struct{…}`

    - `Type SessionThreadTerminated`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `SessionThreadID string`

      ID of the session thread this event refers to.

    - `WorkspaceID string`

  - `type BetaWebhookSessionOutcomeEvaluationEndedEventData struct{…}`

    - `Type SessionOutcomeEvaluationEnded`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookVaultCreatedEventData struct{…}`

    - `Type VaultCreated`

    - `ID string`

      ID of the vault that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookVaultArchivedEventData struct{…}`

    - `Type VaultArchived`

    - `ID string`

      ID of the vault that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookVaultDeletedEventData struct{…}`

    - `Type VaultDeleted`

    - `ID string`

      ID of the vault that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookVaultCredentialCreatedEventData struct{…}`

    - `Type VaultCredentialCreated`

    - `ID string`

      ID of the vault credential that triggered the event.

    - `OrganizationID string`

    - `VaultID string`

      ID of the vault that owns this credential.

    - `WorkspaceID string`

  - `type BetaWebhookVaultCredentialArchivedEventData struct{…}`

    - `Type VaultCredentialArchived`

    - `ID string`

      ID of the vault credential that triggered the event.

    - `OrganizationID string`

    - `VaultID string`

      ID of the vault that owns this credential.

    - `WorkspaceID string`

  - `type BetaWebhookVaultCredentialDeletedEventData struct{…}`

    - `Type VaultCredentialDeleted`

    - `ID string`

      ID of the vault credential that triggered the event.

    - `OrganizationID string`

    - `VaultID string`

      ID of the vault that owns this credential.

    - `WorkspaceID string`

  - `type BetaWebhookVaultCredentialRefreshFailedEventData struct{…}`

    - `Type VaultCredentialRefreshFailed`

    - `ID string`

      ID of the vault credential that triggered the event.

    - `OrganizationID string`

    - `VaultID string`

      ID of the vault that owns this credential.

    - `WorkspaceID string`

  - `type BetaWebhookSessionUpdatedEventData struct{…}`

    - `Type SessionUpdated`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookAgentCreatedEventData struct{…}`

    - `Type AgentCreated`

    - `ID string`

      ID of the agent that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookAgentArchivedEventData struct{…}`

    - `Type AgentArchived`

    - `ID string`

      ID of the agent that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookAgentDeletedEventData struct{…}`

    - `Type AgentDeleted`

    - `ID string`

      ID of the agent that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentPausedEventData struct{…}`

    - `Type DeploymentPaused`

    - `ID string`

      ID of the deployment that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentRunFailedEventData struct{…}`

    - `Type DeploymentRunFailed`

    - `ID string`

      ID of the deployment run that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentCreatedEventData struct{…}`

    - `Type DeploymentCreated`

    - `ID string`

      ID of the deployment that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentUpdatedEventData struct{…}`

    - `Type DeploymentUpdated`

    - `ID string`

      ID of the deployment that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentUnpausedEventData struct{…}`

    - `Type DeploymentUnpaused`

    - `ID string`

      ID of the deployment that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookAgentUpdatedEventData struct{…}`

    - `Type AgentUpdated`

    - `ID string`

      ID of the agent that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentArchivedEventData struct{…}`

    - `Type DeploymentArchived`

    - `ID string`

      ID of the deployment that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentRunStartedEventData struct{…}`

    - `Type DeploymentRunStarted`

    - `ID string`

      ID of the deployment run that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentDeletedEventData struct{…}`

    - `Type DeploymentDeleted`

    - `ID string`

      ID of the deployment that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentRunSucceededEventData struct{…}`

    - `Type DeploymentRunSucceeded`

    - `ID string`

      ID of the deployment run that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookEnvironmentCreatedEventData struct{…}`

    - `Type EnvironmentCreated`

    - `ID string`

      ID of the environment that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookEnvironmentUpdatedEventData struct{…}`

    - `Type EnvironmentUpdated`

    - `ID string`

      ID of the environment that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookEnvironmentArchivedEventData struct{…}`

    - `Type EnvironmentArchived`

    - `ID string`

      ID of the environment that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookEnvironmentDeletedEventData struct{…}`

    - `Type EnvironmentDeleted`

    - `ID string`

      ID of the environment that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookMemoryStoreCreatedEventData struct{…}`

    - `Type MemoryStoreCreated`

    - `ID string`

      ID of the memory store that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookMemoryStoreArchivedEventData struct{…}`

    - `Type MemoryStoreArchived`

    - `ID string`

      ID of the memory store that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookMemoryStoreDeletedEventData struct{…}`

    - `Type MemoryStoreDeleted`

    - `ID string`

      ID of the memory store that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

  - `type BetaWebhookSessionBudgetReachedEventData struct{…}`

    - `Type SessionBudgetReached`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `WorkspaceID string`

### Beta Webhook Memory Store Archived Event Data

- `type BetaWebhookMemoryStoreArchivedEventData struct{…}`

  - `Type MemoryStoreArchived`

  - `ID string`

    ID of the memory store that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Memory Store Created Event Data

- `type BetaWebhookMemoryStoreCreatedEventData struct{…}`

  - `Type MemoryStoreCreated`

  - `ID string`

    ID of the memory store that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Memory Store Deleted Event Data

- `type BetaWebhookMemoryStoreDeletedEventData struct{…}`

  - `Type MemoryStoreDeleted`

  - `ID string`

    ID of the memory store that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Session Archived Event Data

- `type BetaWebhookSessionArchivedEventData struct{…}`

  - `Type SessionArchived`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Session Budget Reached Event Data

- `type BetaWebhookSessionBudgetReachedEventData struct{…}`

  - `Type SessionBudgetReached`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Session Created Event Data

- `type BetaWebhookSessionCreatedEventData struct{…}`

  - `Type SessionCreated`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Session Deleted Event Data

- `type BetaWebhookSessionDeletedEventData struct{…}`

  - `Type SessionDeleted`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Session Idled Event Data

- `type BetaWebhookSessionIdledEventData struct{…}`

  - `Type SessionIdled`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `type BetaWebhookSessionOutcomeEvaluationEndedEventData struct{…}`

  - `Type SessionOutcomeEvaluationEnded`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Session Pending Event Data

- `type BetaWebhookSessionPendingEventData struct{…}`

  - `Type SessionPending`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Session Requires Action Event Data

- `type BetaWebhookSessionRequiresActionEventData struct{…}`

  - `Type SessionRequiresAction`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Session Running Event Data

- `type BetaWebhookSessionRunningEventData struct{…}`

  - `Type SessionRunning`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Session Status Idled Event Data

- `type BetaWebhookSessionStatusIdledEventData struct{…}`

  - `Type SessionStatusIdled`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Session Status Rescheduled Event Data

- `type BetaWebhookSessionStatusRescheduledEventData struct{…}`

  - `Type SessionStatusRescheduled`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Session Status Run Started Event Data

- `type BetaWebhookSessionStatusRunStartedEventData struct{…}`

  - `Type SessionStatusRunStarted`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Session Status Terminated Event Data

- `type BetaWebhookSessionStatusTerminatedEventData struct{…}`

  - `Type SessionStatusTerminated`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Session Thread Created Event Data

- `type BetaWebhookSessionThreadCreatedEventData struct{…}`

  - `Type SessionThreadCreated`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `SessionThreadID string`

    ID of the session thread this event refers to.

  - `WorkspaceID string`

### Beta Webhook Session Thread Idled Event Data

- `type BetaWebhookSessionThreadIdledEventData struct{…}`

  - `Type SessionThreadIdled`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `SessionThreadID string`

    ID of the session thread this event refers to.

  - `WorkspaceID string`

### Beta Webhook Session Thread Terminated Event Data

- `type BetaWebhookSessionThreadTerminatedEventData struct{…}`

  - `Type SessionThreadTerminated`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `SessionThreadID string`

    ID of the session thread this event refers to.

  - `WorkspaceID string`

### Beta Webhook Session Updated Event Data

- `type BetaWebhookSessionUpdatedEventData struct{…}`

  - `Type SessionUpdated`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Vault Archived Event Data

- `type BetaWebhookVaultArchivedEventData struct{…}`

  - `Type VaultArchived`

  - `ID string`

    ID of the vault that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Vault Created Event Data

- `type BetaWebhookVaultCreatedEventData struct{…}`

  - `Type VaultCreated`

  - `ID string`

    ID of the vault that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`

### Beta Webhook Vault Credential Archived Event Data

- `type BetaWebhookVaultCredentialArchivedEventData struct{…}`

  - `Type VaultCredentialArchived`

  - `ID string`

    ID of the vault credential that triggered the event.

  - `OrganizationID string`

  - `VaultID string`

    ID of the vault that owns this credential.

  - `WorkspaceID string`

### Beta Webhook Vault Credential Created Event Data

- `type BetaWebhookVaultCredentialCreatedEventData struct{…}`

  - `Type VaultCredentialCreated`

  - `ID string`

    ID of the vault credential that triggered the event.

  - `OrganizationID string`

  - `VaultID string`

    ID of the vault that owns this credential.

  - `WorkspaceID string`

### Beta Webhook Vault Credential Deleted Event Data

- `type BetaWebhookVaultCredentialDeletedEventData struct{…}`

  - `Type VaultCredentialDeleted`

  - `ID string`

    ID of the vault credential that triggered the event.

  - `OrganizationID string`

  - `VaultID string`

    ID of the vault that owns this credential.

  - `WorkspaceID string`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `type BetaWebhookVaultCredentialRefreshFailedEventData struct{…}`

  - `Type VaultCredentialRefreshFailed`

  - `ID string`

    ID of the vault credential that triggered the event.

  - `OrganizationID string`

  - `VaultID string`

    ID of the vault that owns this credential.

  - `WorkspaceID string`

### Beta Webhook Vault Deleted Event Data

- `type BetaWebhookVaultDeletedEventData struct{…}`

  - `Type VaultDeleted`

  - `ID string`

    ID of the vault that triggered the event.

  - `OrganizationID string`

  - `WorkspaceID string`
