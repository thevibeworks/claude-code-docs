---
title: Unwrap
url: https://platform.claude.com/docs/en/api/go/beta/webhooks/unwrap
---

# Unwrap

`client.Beta.Webhooks.Unwrap(payload, headers) (*UnwrapWebhookEvent, error)`

Verifies the webhook signature from the `webhook-id`, `webhook-timestamp` and `webhook-signature`
headers using your webhook signing key, then parses the payload into an event. Fails if the
signature is missing or invalid.

## Parameters

- `payload []byte`

  The body of the incoming webhook request, exactly as received: the signature is computed over these bytes.

- `headers http.Header`

  The HTTP headers of the incoming webhook request. Verification reads `webhook-id`, `webhook-timestamp` and `webhook-signature`.

## Returns

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

    - `type BetaWebhookUserProfileEnforcementActionOpenedEventData`

      - `Type UserProfileEnforcementActionOpened`

      - `ID string`

        ID of the user profile the enforcement action is on.

      - `EnforcementActionID string`

        ID (`enac_...`) of the enforcement action that was opened or resolved.

      - `OrganizationID string`

    - `type BetaWebhookUserProfileEnforcementActionResolvedEventData`

      - `Type UserProfileEnforcementActionResolved`

      - `ID string`

        ID of the user profile the enforcement action is on.

      - `EnforcementActionID string`

        ID (`enac_...`) of the enforcement action that was opened or resolved.

      - `OrganizationID string`

## Example

```go
package main

import (
	"fmt"

	"github.com/anthropics/anthropic-sdk-go/v2"
	"github.com/anthropics/anthropic-sdk-go/v2/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	// payload is the raw body of the incoming webhook request and headers are its HTTP headers (an http.Header).
	event, err := client.Beta.Webhooks.Unwrap(payload, headers)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", event)
}
```
