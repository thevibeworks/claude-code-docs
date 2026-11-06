---
title: Unwrap
url: https://platform.claude.com/docs/en/api/java/beta/webhooks/unwrap
---

# Unwrap

`UnwrapWebhookEvent beta().webhooks().unwrap(unwrapParams)`

Verifies the webhook signature from the `webhook-id`, `webhook-timestamp` and `webhook-signature`
headers using your webhook signing key, then parses the payload into an event. Fails if the
signature is missing or invalid.

## Parameters

- `UnwrapWebhookParams unwrapParams`

  - `String body`

    The body of the incoming webhook request, exactly as received: the signature is computed over these bytes.

  - `Headers headers`

    The HTTP headers of the incoming webhook request. Verification reads `webhook-id`, `webhook-timestamp` and `webhook-signature`.

  - `Optional<String> secret`

    The webhook signing key. Defaults to the client's `webhookKey` option.

## Returns

- `class UnwrapWebhookEvent`

  - `JsonValue type = "event"`

    Object type. Always `event` for webhook payloads.

  - `String id`

    Unique event identifier for idempotency.

  - `OffsetDateTime createdAt`

    RFC 3339 timestamp when the event occurred.

    format: date-time

  - `BetaWebhookEventData data`

    - `class BetaWebhookSessionCreatedEventData`

      - `JsonValue type = "session.created"`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookSessionPendingEventData`

      - `JsonValue type = "session.pending"`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookSessionRunningEventData`

      - `JsonValue type = "session.running"`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookSessionIdledEventData`

      - `JsonValue type = "session.idled"`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookSessionRequiresActionEventData`

      - `JsonValue type = "session.requires_action"`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookSessionArchivedEventData`

      - `JsonValue type = "session.archived"`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookSessionDeletedEventData`

      - `JsonValue type = "session.deleted"`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookSessionStatusRescheduledEventData`

      - `JsonValue type = "session.status_rescheduled"`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookSessionStatusRunStartedEventData`

      - `JsonValue type = "session.status_run_started"`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookSessionStatusIdledEventData`

      - `JsonValue type = "session.status_idled"`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookSessionStatusTerminatedEventData`

      - `JsonValue type = "session.status_terminated"`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookSessionThreadCreatedEventData`

      - `JsonValue type = "session.thread_created"`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String sessionThreadId`

        ID of the session thread this event refers to.

      - `String workspaceId`

    - `class BetaWebhookSessionThreadIdledEventData`

      - `JsonValue type = "session.thread_idled"`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String sessionThreadId`

        ID of the session thread this event refers to.

      - `String workspaceId`

    - `class BetaWebhookSessionThreadTerminatedEventData`

      - `JsonValue type = "session.thread_terminated"`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String sessionThreadId`

        ID of the session thread this event refers to.

      - `String workspaceId`

    - `class BetaWebhookSessionOutcomeEvaluationEndedEventData`

      - `JsonValue type = "session.outcome_evaluation_ended"`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookVaultCreatedEventData`

      - `JsonValue type = "vault.created"`

      - `String id`

        ID of the vault that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookVaultArchivedEventData`

      - `JsonValue type = "vault.archived"`

      - `String id`

        ID of the vault that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookVaultDeletedEventData`

      - `JsonValue type = "vault.deleted"`

      - `String id`

        ID of the vault that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookVaultCredentialCreatedEventData`

      - `JsonValue type = "vault_credential.created"`

      - `String id`

        ID of the vault credential that triggered the event.

      - `String organizationId`

      - `String vaultId`

        ID of the vault that owns this credential.

      - `String workspaceId`

    - `class BetaWebhookVaultCredentialArchivedEventData`

      - `JsonValue type = "vault_credential.archived"`

      - `String id`

        ID of the vault credential that triggered the event.

      - `String organizationId`

      - `String vaultId`

        ID of the vault that owns this credential.

      - `String workspaceId`

    - `class BetaWebhookVaultCredentialDeletedEventData`

      - `JsonValue type = "vault_credential.deleted"`

      - `String id`

        ID of the vault credential that triggered the event.

      - `String organizationId`

      - `String vaultId`

        ID of the vault that owns this credential.

      - `String workspaceId`

    - `class BetaWebhookVaultCredentialRefreshFailedEventData`

      - `JsonValue type = "vault_credential.refresh_failed"`

      - `String id`

        ID of the vault credential that triggered the event.

      - `String organizationId`

      - `String vaultId`

        ID of the vault that owns this credential.

      - `String workspaceId`

    - `class BetaWebhookSessionUpdatedEventData`

      - `JsonValue type = "session.updated"`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookAgentCreatedEventData`

      - `JsonValue type = "agent.created"`

      - `String id`

        ID of the agent that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookAgentArchivedEventData`

      - `JsonValue type = "agent.archived"`

      - `String id`

        ID of the agent that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookAgentDeletedEventData`

      - `JsonValue type = "agent.deleted"`

      - `String id`

        ID of the agent that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookDeploymentPausedEventData`

      - `JsonValue type = "deployment.paused"`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookDeploymentRunFailedEventData`

      - `JsonValue type = "deployment_run.failed"`

      - `String id`

        ID of the deployment run that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookDeploymentCreatedEventData`

      - `JsonValue type = "deployment.created"`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookDeploymentUpdatedEventData`

      - `JsonValue type = "deployment.updated"`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookDeploymentUnpausedEventData`

      - `JsonValue type = "deployment.unpaused"`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookAgentUpdatedEventData`

      - `JsonValue type = "agent.updated"`

      - `String id`

        ID of the agent that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookDeploymentArchivedEventData`

      - `JsonValue type = "deployment.archived"`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookDeploymentRunStartedEventData`

      - `JsonValue type = "deployment_run.started"`

      - `String id`

        ID of the deployment run that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookDeploymentDeletedEventData`

      - `JsonValue type = "deployment.deleted"`

      - `String id`

        ID of the deployment that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookDeploymentRunSucceededEventData`

      - `JsonValue type = "deployment_run.succeeded"`

      - `String id`

        ID of the deployment run that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookEnvironmentCreatedEventData`

      - `JsonValue type = "environment.created"`

      - `String id`

        ID of the environment that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookEnvironmentUpdatedEventData`

      - `JsonValue type = "environment.updated"`

      - `String id`

        ID of the environment that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookEnvironmentArchivedEventData`

      - `JsonValue type = "environment.archived"`

      - `String id`

        ID of the environment that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookEnvironmentDeletedEventData`

      - `JsonValue type = "environment.deleted"`

      - `String id`

        ID of the environment that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookMemoryStoreCreatedEventData`

      - `JsonValue type = "memory_store.created"`

      - `String id`

        ID of the memory store that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookMemoryStoreArchivedEventData`

      - `JsonValue type = "memory_store.archived"`

      - `String id`

        ID of the memory store that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookMemoryStoreDeletedEventData`

      - `JsonValue type = "memory_store.deleted"`

      - `String id`

        ID of the memory store that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookSessionBudgetReachedEventData`

      - `JsonValue type = "session.budget_reached"`

      - `String id`

        ID of the session that triggered the event.

      - `String organizationId`

      - `String workspaceId`

    - `class BetaWebhookUserProfileEnforcementActionOpenedEventData`

      - `JsonValue type = "user_profile.enforcement_action_opened"`

      - `String id`

        ID of the user profile the enforcement action is on.

      - `String enforcementActionId`

        ID (`enac_...`) of the enforcement action that was opened or resolved.

      - `String organizationId`

    - `class BetaWebhookUserProfileEnforcementActionResolvedEventData`

      - `JsonValue type = "user_profile.enforcement_action_resolved"`

      - `String id`

        ID of the user profile the enforcement action is on.

      - `String enforcementActionId`

        ID (`enac_...`) of the enforcement action that was opened or resolved.

      - `String organizationId`

## Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.core.UnwrapWebhookParams;
import com.anthropic.models.beta.webhooks.UnwrapWebhookEvent;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        // `body` is the raw body of the incoming webhook request and `headers` are its HTTP headers as a `Headers` (`Headers.builder().put(name, value).build()`).
        UnwrapWebhookParams params = UnwrapWebhookParams.builder()
            .body(body)
            .headers(headers)
            .build();
        UnwrapWebhookEvent event = client.beta().webhooks().unwrap(params);
    }
}
```
