# Webhooks

## Unwrap

`client.Beta.Webhooks.Unwrap(ctx) error`

Verifies the webhook signature from the `webhook-id`, `webhook-timestamp` and `webhook-signature`
headers using your webhook signing key, then parses the payload into an event. Fails if the
signature is missing or invalid.

### Example

```go
package main

import (
	"context"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	err := client.Beta.Webhooks.Unwrap(context.TODO())
	if err != nil {
		panic(err.Error())
	}
}
```

## Parse Unverified

`client.Beta.Webhooks.ParseUnverified(ctx) error`

Parses a webhook payload into an event without verifying its signature. Prefer `unwrap()` unless
you have already verified the signature yourself.

### Example

```go
package main

import (
	"context"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	err := client.Beta.Webhooks.ParseUnverified(context.TODO())
	if err != nil {
		panic(err.Error())
	}
}
```

## Domain types

### Beta Webhook Agent Archived Event Data

- `type BetaWebhookAgentArchivedEventData struct{…}`

  - `ID string`

    ID of the agent that triggered the event.

  - `OrganizationID string`

  - `Type AgentArchived`

  - `WorkspaceID string`

### Beta Webhook Agent Created Event Data

- `type BetaWebhookAgentCreatedEventData struct{…}`

  - `ID string`

    ID of the agent that triggered the event.

  - `OrganizationID string`

  - `Type AgentCreated`

  - `WorkspaceID string`

### Beta Webhook Agent Deleted Event Data

- `type BetaWebhookAgentDeletedEventData struct{…}`

  - `ID string`

    ID of the agent that triggered the event.

  - `OrganizationID string`

  - `Type AgentDeleted`

  - `WorkspaceID string`

### Beta Webhook Agent Updated Event Data

- `type BetaWebhookAgentUpdatedEventData struct{…}`

  - `ID string`

    ID of the agent that triggered the event.

  - `OrganizationID string`

  - `Type AgentUpdated`

  - `WorkspaceID string`

### Beta Webhook Deployment Archived Event Data

- `type BetaWebhookDeploymentArchivedEventData struct{…}`

  - `ID string`

    ID of the deployment that triggered the event.

  - `OrganizationID string`

  - `Type DeploymentArchived`

  - `WorkspaceID string`

### Beta Webhook Deployment Created Event Data

- `type BetaWebhookDeploymentCreatedEventData struct{…}`

  - `ID string`

    ID of the deployment that triggered the event.

  - `OrganizationID string`

  - `Type DeploymentCreated`

  - `WorkspaceID string`

### Beta Webhook Deployment Deleted Event Data

- `type BetaWebhookDeploymentDeletedEventData struct{…}`

  - `ID string`

    ID of the deployment that triggered the event.

  - `OrganizationID string`

  - `Type DeploymentDeleted`

  - `WorkspaceID string`

### Beta Webhook Deployment Paused Event Data

- `type BetaWebhookDeploymentPausedEventData struct{…}`

  - `ID string`

    ID of the deployment that triggered the event.

  - `OrganizationID string`

  - `Type DeploymentPaused`

  - `WorkspaceID string`

### Beta Webhook Deployment Run Failed Event Data

- `type BetaWebhookDeploymentRunFailedEventData struct{…}`

  - `ID string`

    ID of the deployment run that triggered the event.

  - `OrganizationID string`

  - `Type DeploymentRunFailed`

  - `WorkspaceID string`

### Beta Webhook Deployment Run Started Event Data

- `type BetaWebhookDeploymentRunStartedEventData struct{…}`

  - `ID string`

    ID of the deployment run that triggered the event.

  - `OrganizationID string`

  - `Type DeploymentRunStarted`

  - `WorkspaceID string`

### Beta Webhook Deployment Run Succeeded Event Data

- `type BetaWebhookDeploymentRunSucceededEventData struct{…}`

  - `ID string`

    ID of the deployment run that triggered the event.

  - `OrganizationID string`

  - `Type DeploymentRunSucceeded`

  - `WorkspaceID string`

### Beta Webhook Deployment Unpaused Event Data

- `type BetaWebhookDeploymentUnpausedEventData struct{…}`

  - `ID string`

    ID of the deployment that triggered the event.

  - `OrganizationID string`

  - `Type DeploymentUnpaused`

  - `WorkspaceID string`

### Beta Webhook Deployment Updated Event Data

- `type BetaWebhookDeploymentUpdatedEventData struct{…}`

  - `ID string`

    ID of the deployment that triggered the event.

  - `OrganizationID string`

  - `Type DeploymentUpdated`

  - `WorkspaceID string`

### Beta Webhook Environment Archived Event Data

- `type BetaWebhookEnvironmentArchivedEventData struct{…}`

  - `ID string`

    ID of the environment that triggered the event.

  - `OrganizationID string`

  - `Type EnvironmentArchived`

  - `WorkspaceID string`

### Beta Webhook Environment Created Event Data

- `type BetaWebhookEnvironmentCreatedEventData struct{…}`

  - `ID string`

    ID of the environment that triggered the event.

  - `OrganizationID string`

  - `Type EnvironmentCreated`

  - `WorkspaceID string`

### Beta Webhook Environment Deleted Event Data

- `type BetaWebhookEnvironmentDeletedEventData struct{…}`

  - `ID string`

    ID of the environment that triggered the event.

  - `OrganizationID string`

  - `Type EnvironmentDeleted`

  - `WorkspaceID string`

### Beta Webhook Environment Updated Event Data

- `type BetaWebhookEnvironmentUpdatedEventData struct{…}`

  - `ID string`

    ID of the environment that triggered the event.

  - `OrganizationID string`

  - `Type EnvironmentUpdated`

  - `WorkspaceID string`

### Beta Webhook Event

- `type UnwrapWebhookEvent struct{…}`

  - `ID string`

    Unique event identifier for idempotency.

  - `CreatedAt Time`

    RFC 3339 timestamp when the event occurred.

    format: date-time

  - `Data BetaWebhookEventDataUnion`

    - `type BetaWebhookSessionCreatedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionCreated`

      - `WorkspaceID string`

    - `type BetaWebhookSessionPendingEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionPending`

      - `WorkspaceID string`

    - `type BetaWebhookSessionRunningEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionRunning`

      - `WorkspaceID string`

    - `type BetaWebhookSessionIdledEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionIdled`

      - `WorkspaceID string`

    - `type BetaWebhookSessionRequiresActionEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionRequiresAction`

      - `WorkspaceID string`

    - `type BetaWebhookSessionArchivedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionArchived`

      - `WorkspaceID string`

    - `type BetaWebhookSessionDeletedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionDeleted`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusRescheduledEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionStatusRescheduled`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusRunStartedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionStatusRunStarted`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusIdledEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionStatusIdled`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusTerminatedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionStatusTerminated`

      - `WorkspaceID string`

    - `type BetaWebhookSessionThreadCreatedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `SessionThreadID string`

        ID of the session thread this event refers to.

      - `Type SessionThreadCreated`

      - `WorkspaceID string`

    - `type BetaWebhookSessionThreadIdledEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `SessionThreadID string`

        ID of the session thread this event refers to.

      - `Type SessionThreadIdled`

      - `WorkspaceID string`

    - `type BetaWebhookSessionThreadTerminatedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `SessionThreadID string`

        ID of the session thread this event refers to.

      - `Type SessionThreadTerminated`

      - `WorkspaceID string`

    - `type BetaWebhookSessionOutcomeEvaluationEndedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionOutcomeEvaluationEnded`

      - `WorkspaceID string`

    - `type BetaWebhookVaultCreatedEventData struct{…}`

      - `ID string`

        ID of the vault that triggered the event.

      - `OrganizationID string`

      - `Type VaultCreated`

      - `WorkspaceID string`

    - `type BetaWebhookVaultArchivedEventData struct{…}`

      - `ID string`

        ID of the vault that triggered the event.

      - `OrganizationID string`

      - `Type VaultArchived`

      - `WorkspaceID string`

    - `type BetaWebhookVaultDeletedEventData struct{…}`

      - `ID string`

        ID of the vault that triggered the event.

      - `OrganizationID string`

      - `Type VaultDeleted`

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialCreatedEventData struct{…}`

      - `ID string`

        ID of the vault credential that triggered the event.

      - `OrganizationID string`

      - `Type VaultCredentialCreated`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialArchivedEventData struct{…}`

      - `ID string`

        ID of the vault credential that triggered the event.

      - `OrganizationID string`

      - `Type VaultCredentialArchived`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialDeletedEventData struct{…}`

      - `ID string`

        ID of the vault credential that triggered the event.

      - `OrganizationID string`

      - `Type VaultCredentialDeleted`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialRefreshFailedEventData struct{…}`

      - `ID string`

        ID of the vault credential that triggered the event.

      - `OrganizationID string`

      - `Type VaultCredentialRefreshFailed`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookSessionUpdatedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionUpdated`

      - `WorkspaceID string`

    - `type BetaWebhookAgentCreatedEventData struct{…}`

      - `ID string`

        ID of the agent that triggered the event.

      - `OrganizationID string`

      - `Type AgentCreated`

      - `WorkspaceID string`

    - `type BetaWebhookAgentArchivedEventData struct{…}`

      - `ID string`

        ID of the agent that triggered the event.

      - `OrganizationID string`

      - `Type AgentArchived`

      - `WorkspaceID string`

    - `type BetaWebhookAgentDeletedEventData struct{…}`

      - `ID string`

        ID of the agent that triggered the event.

      - `OrganizationID string`

      - `Type AgentDeleted`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentPausedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentPaused`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentRunFailedEventData struct{…}`

      - `ID string`

        ID of the deployment run that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentRunFailed`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentCreatedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentCreated`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentUpdatedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentUpdated`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentUnpausedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentUnpaused`

      - `WorkspaceID string`

    - `type BetaWebhookAgentUpdatedEventData struct{…}`

      - `ID string`

        ID of the agent that triggered the event.

      - `OrganizationID string`

      - `Type AgentUpdated`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentArchivedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentArchived`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentRunStartedEventData struct{…}`

      - `ID string`

        ID of the deployment run that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentRunStarted`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentDeletedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentDeleted`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentRunSucceededEventData struct{…}`

      - `ID string`

        ID of the deployment run that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentRunSucceeded`

      - `WorkspaceID string`

    - `type BetaWebhookEnvironmentCreatedEventData struct{…}`

      - `ID string`

        ID of the environment that triggered the event.

      - `OrganizationID string`

      - `Type EnvironmentCreated`

      - `WorkspaceID string`

    - `type BetaWebhookEnvironmentUpdatedEventData struct{…}`

      - `ID string`

        ID of the environment that triggered the event.

      - `OrganizationID string`

      - `Type EnvironmentUpdated`

      - `WorkspaceID string`

    - `type BetaWebhookEnvironmentArchivedEventData struct{…}`

      - `ID string`

        ID of the environment that triggered the event.

      - `OrganizationID string`

      - `Type EnvironmentArchived`

      - `WorkspaceID string`

    - `type BetaWebhookEnvironmentDeletedEventData struct{…}`

      - `ID string`

        ID of the environment that triggered the event.

      - `OrganizationID string`

      - `Type EnvironmentDeleted`

      - `WorkspaceID string`

    - `type BetaWebhookMemoryStoreCreatedEventData struct{…}`

      - `ID string`

        ID of the memory store that triggered the event.

      - `OrganizationID string`

      - `Type MemoryStoreCreated`

      - `WorkspaceID string`

    - `type BetaWebhookMemoryStoreArchivedEventData struct{…}`

      - `ID string`

        ID of the memory store that triggered the event.

      - `OrganizationID string`

      - `Type MemoryStoreArchived`

      - `WorkspaceID string`

    - `type BetaWebhookMemoryStoreDeletedEventData struct{…}`

      - `ID string`

        ID of the memory store that triggered the event.

      - `OrganizationID string`

      - `Type MemoryStoreDeleted`

      - `WorkspaceID string`

    - `type BetaWebhookSessionBudgetReachedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionBudgetReached`

      - `WorkspaceID string`

  - `Type Event`

    Object type. Always `event` for webhook payloads.

### Beta Webhook Event Data

- `type BetaWebhookEventDataUnion interface{…}`

  - `type BetaWebhookSessionCreatedEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionCreated`

    - `WorkspaceID string`

  - `type BetaWebhookSessionPendingEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionPending`

    - `WorkspaceID string`

  - `type BetaWebhookSessionRunningEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionRunning`

    - `WorkspaceID string`

  - `type BetaWebhookSessionIdledEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionIdled`

    - `WorkspaceID string`

  - `type BetaWebhookSessionRequiresActionEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionRequiresAction`

    - `WorkspaceID string`

  - `type BetaWebhookSessionArchivedEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionArchived`

    - `WorkspaceID string`

  - `type BetaWebhookSessionDeletedEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionDeleted`

    - `WorkspaceID string`

  - `type BetaWebhookSessionStatusRescheduledEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionStatusRescheduled`

    - `WorkspaceID string`

  - `type BetaWebhookSessionStatusRunStartedEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionStatusRunStarted`

    - `WorkspaceID string`

  - `type BetaWebhookSessionStatusIdledEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionStatusIdled`

    - `WorkspaceID string`

  - `type BetaWebhookSessionStatusTerminatedEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionStatusTerminated`

    - `WorkspaceID string`

  - `type BetaWebhookSessionThreadCreatedEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `SessionThreadID string`

      ID of the session thread this event refers to.

    - `Type SessionThreadCreated`

    - `WorkspaceID string`

  - `type BetaWebhookSessionThreadIdledEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `SessionThreadID string`

      ID of the session thread this event refers to.

    - `Type SessionThreadIdled`

    - `WorkspaceID string`

  - `type BetaWebhookSessionThreadTerminatedEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `SessionThreadID string`

      ID of the session thread this event refers to.

    - `Type SessionThreadTerminated`

    - `WorkspaceID string`

  - `type BetaWebhookSessionOutcomeEvaluationEndedEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionOutcomeEvaluationEnded`

    - `WorkspaceID string`

  - `type BetaWebhookVaultCreatedEventData struct{…}`

    - `ID string`

      ID of the vault that triggered the event.

    - `OrganizationID string`

    - `Type VaultCreated`

    - `WorkspaceID string`

  - `type BetaWebhookVaultArchivedEventData struct{…}`

    - `ID string`

      ID of the vault that triggered the event.

    - `OrganizationID string`

    - `Type VaultArchived`

    - `WorkspaceID string`

  - `type BetaWebhookVaultDeletedEventData struct{…}`

    - `ID string`

      ID of the vault that triggered the event.

    - `OrganizationID string`

    - `Type VaultDeleted`

    - `WorkspaceID string`

  - `type BetaWebhookVaultCredentialCreatedEventData struct{…}`

    - `ID string`

      ID of the vault credential that triggered the event.

    - `OrganizationID string`

    - `Type VaultCredentialCreated`

    - `VaultID string`

      ID of the vault that owns this credential.

    - `WorkspaceID string`

  - `type BetaWebhookVaultCredentialArchivedEventData struct{…}`

    - `ID string`

      ID of the vault credential that triggered the event.

    - `OrganizationID string`

    - `Type VaultCredentialArchived`

    - `VaultID string`

      ID of the vault that owns this credential.

    - `WorkspaceID string`

  - `type BetaWebhookVaultCredentialDeletedEventData struct{…}`

    - `ID string`

      ID of the vault credential that triggered the event.

    - `OrganizationID string`

    - `Type VaultCredentialDeleted`

    - `VaultID string`

      ID of the vault that owns this credential.

    - `WorkspaceID string`

  - `type BetaWebhookVaultCredentialRefreshFailedEventData struct{…}`

    - `ID string`

      ID of the vault credential that triggered the event.

    - `OrganizationID string`

    - `Type VaultCredentialRefreshFailed`

    - `VaultID string`

      ID of the vault that owns this credential.

    - `WorkspaceID string`

  - `type BetaWebhookSessionUpdatedEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionUpdated`

    - `WorkspaceID string`

  - `type BetaWebhookAgentCreatedEventData struct{…}`

    - `ID string`

      ID of the agent that triggered the event.

    - `OrganizationID string`

    - `Type AgentCreated`

    - `WorkspaceID string`

  - `type BetaWebhookAgentArchivedEventData struct{…}`

    - `ID string`

      ID of the agent that triggered the event.

    - `OrganizationID string`

    - `Type AgentArchived`

    - `WorkspaceID string`

  - `type BetaWebhookAgentDeletedEventData struct{…}`

    - `ID string`

      ID of the agent that triggered the event.

    - `OrganizationID string`

    - `Type AgentDeleted`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentPausedEventData struct{…}`

    - `ID string`

      ID of the deployment that triggered the event.

    - `OrganizationID string`

    - `Type DeploymentPaused`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentRunFailedEventData struct{…}`

    - `ID string`

      ID of the deployment run that triggered the event.

    - `OrganizationID string`

    - `Type DeploymentRunFailed`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentCreatedEventData struct{…}`

    - `ID string`

      ID of the deployment that triggered the event.

    - `OrganizationID string`

    - `Type DeploymentCreated`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentUpdatedEventData struct{…}`

    - `ID string`

      ID of the deployment that triggered the event.

    - `OrganizationID string`

    - `Type DeploymentUpdated`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentUnpausedEventData struct{…}`

    - `ID string`

      ID of the deployment that triggered the event.

    - `OrganizationID string`

    - `Type DeploymentUnpaused`

    - `WorkspaceID string`

  - `type BetaWebhookAgentUpdatedEventData struct{…}`

    - `ID string`

      ID of the agent that triggered the event.

    - `OrganizationID string`

    - `Type AgentUpdated`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentArchivedEventData struct{…}`

    - `ID string`

      ID of the deployment that triggered the event.

    - `OrganizationID string`

    - `Type DeploymentArchived`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentRunStartedEventData struct{…}`

    - `ID string`

      ID of the deployment run that triggered the event.

    - `OrganizationID string`

    - `Type DeploymentRunStarted`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentDeletedEventData struct{…}`

    - `ID string`

      ID of the deployment that triggered the event.

    - `OrganizationID string`

    - `Type DeploymentDeleted`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentRunSucceededEventData struct{…}`

    - `ID string`

      ID of the deployment run that triggered the event.

    - `OrganizationID string`

    - `Type DeploymentRunSucceeded`

    - `WorkspaceID string`

  - `type BetaWebhookEnvironmentCreatedEventData struct{…}`

    - `ID string`

      ID of the environment that triggered the event.

    - `OrganizationID string`

    - `Type EnvironmentCreated`

    - `WorkspaceID string`

  - `type BetaWebhookEnvironmentUpdatedEventData struct{…}`

    - `ID string`

      ID of the environment that triggered the event.

    - `OrganizationID string`

    - `Type EnvironmentUpdated`

    - `WorkspaceID string`

  - `type BetaWebhookEnvironmentArchivedEventData struct{…}`

    - `ID string`

      ID of the environment that triggered the event.

    - `OrganizationID string`

    - `Type EnvironmentArchived`

    - `WorkspaceID string`

  - `type BetaWebhookEnvironmentDeletedEventData struct{…}`

    - `ID string`

      ID of the environment that triggered the event.

    - `OrganizationID string`

    - `Type EnvironmentDeleted`

    - `WorkspaceID string`

  - `type BetaWebhookMemoryStoreCreatedEventData struct{…}`

    - `ID string`

      ID of the memory store that triggered the event.

    - `OrganizationID string`

    - `Type MemoryStoreCreated`

    - `WorkspaceID string`

  - `type BetaWebhookMemoryStoreArchivedEventData struct{…}`

    - `ID string`

      ID of the memory store that triggered the event.

    - `OrganizationID string`

    - `Type MemoryStoreArchived`

    - `WorkspaceID string`

  - `type BetaWebhookMemoryStoreDeletedEventData struct{…}`

    - `ID string`

      ID of the memory store that triggered the event.

    - `OrganizationID string`

    - `Type MemoryStoreDeleted`

    - `WorkspaceID string`

  - `type BetaWebhookSessionBudgetReachedEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionBudgetReached`

    - `WorkspaceID string`

### Beta Webhook Memory Store Archived Event Data

- `type BetaWebhookMemoryStoreArchivedEventData struct{…}`

  - `ID string`

    ID of the memory store that triggered the event.

  - `OrganizationID string`

  - `Type MemoryStoreArchived`

  - `WorkspaceID string`

### Beta Webhook Memory Store Created Event Data

- `type BetaWebhookMemoryStoreCreatedEventData struct{…}`

  - `ID string`

    ID of the memory store that triggered the event.

  - `OrganizationID string`

  - `Type MemoryStoreCreated`

  - `WorkspaceID string`

### Beta Webhook Memory Store Deleted Event Data

- `type BetaWebhookMemoryStoreDeletedEventData struct{…}`

  - `ID string`

    ID of the memory store that triggered the event.

  - `OrganizationID string`

  - `Type MemoryStoreDeleted`

  - `WorkspaceID string`

### Beta Webhook Session Archived Event Data

- `type BetaWebhookSessionArchivedEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionArchived`

  - `WorkspaceID string`

### Beta Webhook Session Budget Reached Event Data

- `type BetaWebhookSessionBudgetReachedEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionBudgetReached`

  - `WorkspaceID string`

### Beta Webhook Session Created Event Data

- `type BetaWebhookSessionCreatedEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionCreated`

  - `WorkspaceID string`

### Beta Webhook Session Deleted Event Data

- `type BetaWebhookSessionDeletedEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionDeleted`

  - `WorkspaceID string`

### Beta Webhook Session Idled Event Data

- `type BetaWebhookSessionIdledEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionIdled`

  - `WorkspaceID string`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `type BetaWebhookSessionOutcomeEvaluationEndedEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionOutcomeEvaluationEnded`

  - `WorkspaceID string`

### Beta Webhook Session Pending Event Data

- `type BetaWebhookSessionPendingEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionPending`

  - `WorkspaceID string`

### Beta Webhook Session Requires Action Event Data

- `type BetaWebhookSessionRequiresActionEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionRequiresAction`

  - `WorkspaceID string`

### Beta Webhook Session Running Event Data

- `type BetaWebhookSessionRunningEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionRunning`

  - `WorkspaceID string`

### Beta Webhook Session Status Idled Event Data

- `type BetaWebhookSessionStatusIdledEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionStatusIdled`

  - `WorkspaceID string`

### Beta Webhook Session Status Rescheduled Event Data

- `type BetaWebhookSessionStatusRescheduledEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionStatusRescheduled`

  - `WorkspaceID string`

### Beta Webhook Session Status Run Started Event Data

- `type BetaWebhookSessionStatusRunStartedEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionStatusRunStarted`

  - `WorkspaceID string`

### Beta Webhook Session Status Terminated Event Data

- `type BetaWebhookSessionStatusTerminatedEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionStatusTerminated`

  - `WorkspaceID string`

### Beta Webhook Session Thread Created Event Data

- `type BetaWebhookSessionThreadCreatedEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `SessionThreadID string`

    ID of the session thread this event refers to.

  - `Type SessionThreadCreated`

  - `WorkspaceID string`

### Beta Webhook Session Thread Idled Event Data

- `type BetaWebhookSessionThreadIdledEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `SessionThreadID string`

    ID of the session thread this event refers to.

  - `Type SessionThreadIdled`

  - `WorkspaceID string`

### Beta Webhook Session Thread Terminated Event Data

- `type BetaWebhookSessionThreadTerminatedEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `SessionThreadID string`

    ID of the session thread this event refers to.

  - `Type SessionThreadTerminated`

  - `WorkspaceID string`

### Beta Webhook Session Updated Event Data

- `type BetaWebhookSessionUpdatedEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionUpdated`

  - `WorkspaceID string`

### Beta Webhook Vault Archived Event Data

- `type BetaWebhookVaultArchivedEventData struct{…}`

  - `ID string`

    ID of the vault that triggered the event.

  - `OrganizationID string`

  - `Type VaultArchived`

  - `WorkspaceID string`

### Beta Webhook Vault Created Event Data

- `type BetaWebhookVaultCreatedEventData struct{…}`

  - `ID string`

    ID of the vault that triggered the event.

  - `OrganizationID string`

  - `Type VaultCreated`

  - `WorkspaceID string`

### Beta Webhook Vault Credential Archived Event Data

- `type BetaWebhookVaultCredentialArchivedEventData struct{…}`

  - `ID string`

    ID of the vault credential that triggered the event.

  - `OrganizationID string`

  - `Type VaultCredentialArchived`

  - `VaultID string`

    ID of the vault that owns this credential.

  - `WorkspaceID string`

### Beta Webhook Vault Credential Created Event Data

- `type BetaWebhookVaultCredentialCreatedEventData struct{…}`

  - `ID string`

    ID of the vault credential that triggered the event.

  - `OrganizationID string`

  - `Type VaultCredentialCreated`

  - `VaultID string`

    ID of the vault that owns this credential.

  - `WorkspaceID string`

### Beta Webhook Vault Credential Deleted Event Data

- `type BetaWebhookVaultCredentialDeletedEventData struct{…}`

  - `ID string`

    ID of the vault credential that triggered the event.

  - `OrganizationID string`

  - `Type VaultCredentialDeleted`

  - `VaultID string`

    ID of the vault that owns this credential.

  - `WorkspaceID string`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `type BetaWebhookVaultCredentialRefreshFailedEventData struct{…}`

  - `ID string`

    ID of the vault credential that triggered the event.

  - `OrganizationID string`

  - `Type VaultCredentialRefreshFailed`

  - `VaultID string`

    ID of the vault that owns this credential.

  - `WorkspaceID string`

### Beta Webhook Vault Deleted Event Data

- `type BetaWebhookVaultDeletedEventData struct{…}`

  - `ID string`

    ID of the vault that triggered the event.

  - `OrganizationID string`

  - `Type VaultDeleted`

  - `WorkspaceID string`
