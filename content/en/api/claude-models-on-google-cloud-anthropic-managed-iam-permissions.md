---
title: IAM permissions for Claude Models on Google Cloud (Anthropic managed)
url: https://platform.claude.com/docs/en/api/claude-models-on-google-cloud-anthropic-managed-iam-permissions
description: Look up Google Cloud IAM permissions, predefined roles, and audit log types for Claude Models on Google Cloud (Anthropic managed).
---

Claude Models on Google Cloud (Anthropic managed) uses Google Cloud IAM for access control. Every API route needs one permission from the `claude.googleapis.com` service. If the caller doesn’t hold that permission, Google Cloud returns an HTTP 403 error. Three predefined roles bundle the permissions. For setup and authentication, see [Claude Models on Google Cloud (Anthropic managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed).

## Service details

The following table describes the Google Cloud service for Claude Models on Google Cloud (Anthropic managed).

| Attribute                         | Value                                                                                                                                                                                                                     |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Service**                       | `claude.googleapis.com`                                                                                                                                                                                                   |
| **Where permissions are checked** | A workspace or the Anthropic organization                                                                                                                                                                                 |
| **Audit log types**               | Data Access, Admin Activity<br />To turn on Data Access logs, see [Monitoring and logging](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed#monitoring-and-logging). |

Grant roles on the Google Cloud project. For how projects, organizations, and workspaces relate, see [Workspaces](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed#workspaces).

Permissions on this page are in the short form `resource.verb`, such as `messages.create`.

## Predefined roles

The following table lists the predefined roles for Claude Models on Google Cloud (Anthropic managed).

| Role                  | Display name  | Permissions                                                                                                                                                                           |
| --------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `roles/claude.viewer` | Claude Viewer | Every `get` and `list` permission on workspace resources.                                                                                                                             |
| `roles/claude.user`   | Claude User   | Everything in `roles/claude.viewer`, plus every other permission on workspace resources.<br />For example, `messages.create`, `messages.countTokens`, and `environments.processWork`. |
| `roles/claude.admin`  | Claude Admin  | Everything in `roles/claude.user`, plus the permissions checked on your Anthropic organization.<br />For example, `externalKeys.*` and `usageAnalytics.list`.                         |

In the following tables, **Admin**, **User**, and **Viewer** stand for these three roles.

## Permissions

The following tables list 69 permissions across 113 routes.

The `get` and `list` permissions are the read-only ones.

Unless a section says otherwise, each route’s audit log type is Data Access.

`roles/claude.viewer` can’t send messages or count tokens. Sending a message needs `messages.create`. Counting tokens needs `messages.countTokens`.

Some routes in the following tables might not be available to your organization. To check which features are available, see [Feature support](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed#feature-support).

### Messages

| Permission             | Roles       | Routes authorized                |
| ---------------------- | ----------- | -------------------------------- |
| `messages.create`      | Admin, User | `POST /v1/messages`              |
| `messages.countTokens` | Admin, User | `POST /v1/messages/count_tokens` |

### Message batches

| Permission              | Roles               | Routes authorized                                                                                        |
| ----------------------- | ------------------- | -------------------------------------------------------------------------------------------------------- |
| `messageBatches.create` | Admin, User         | `POST /v1/messages/batches`                                                                              |
| `messageBatches.get`    | Admin, User, Viewer | `GET /v1/messages/batches/{message_batch_id}`<br />`GET /v1/messages/batches/{message_batch_id}/results` |
| `messageBatches.list`   | Admin, User, Viewer | `GET /v1/messages/batches`                                                                               |
| `messageBatches.delete` | Admin, User         | `DELETE /v1/messages/batches/{message_batch_id}`                                                         |
| `messageBatches.cancel` | Admin, User         | `POST /v1/messages/batches/{message_batch_id}/cancel`                                                    |

`roles/claude.viewer` can read batch results. `messageBatches.get` authorizes both reading a batch’s metadata and downloading its results.

### Models

| Permission    | Roles               | Routes authorized           |
| ------------- | ------------------- | --------------------------- |
| `models.get`  | Admin, User, Viewer | `GET /v1/models/{model_id}` |
| `models.list` | Admin, User, Viewer | `GET /v1/models`            |

### Files

| Permission     | Roles               | Routes authorized                                                |
| -------------- | ------------------- | ---------------------------------------------------------------- |
| `files.create` | Admin, User         | `POST /v1/files`                                                 |
| `files.get`    | Admin, User, Viewer | `GET /v1/files/{file_id}`<br />`GET /v1/files/{file_id}/content` |
| `files.list`   | Admin, User, Viewer | `GET /v1/files`                                                  |
| `files.delete` | Admin, User         | `DELETE /v1/files/{file_id}`                                     |

`roles/claude.viewer` can download files. `files.get` authorizes both reading a file’s metadata and downloading its content.

### Skills

| Permission      | Roles               | Routes authorized                                                                                                                                                                     |
| --------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `skills.create` | Admin, User         | `POST /v1/skills`                                                                                                                                                                     |
| `skills.get`    | Admin, User, Viewer | `GET /v1/skills/{skill_id}`<br />`GET /v1/skills/{skill_id}/versions`<br />`GET /v1/skills/{skill_id}/versions/{version}`<br />`GET /v1/skills/{skill_id}/versions/{version}/content` |
| `skills.list`   | Admin, User, Viewer | `GET /v1/skills`                                                                                                                                                                      |
| `skills.update` | Admin, User         | `POST /v1/skills/{skill_id}/versions`<br />`DELETE /v1/skills/{skill_id}/versions/{version}`                                                                                          |
| `skills.delete` | Admin, User         | `DELETE /v1/skills/{skill_id}`                                                                                                                                                        |

Creating or deleting a skill version needs `skills.update`, not `skills.create` or `skills.delete`.

### Agents

| Permission       | Roles               | Routes authorized                                                     |
| ---------------- | ------------------- | --------------------------------------------------------------------- |
| `agents.create`  | Admin, User         | `POST /v1/agents`                                                     |
| `agents.get`     | Admin, User, Viewer | `GET /v1/agents/{agent_id}`<br />`GET /v1/agents/{agent_id}/versions` |
| `agents.list`    | Admin, User, Viewer | `GET /v1/agents`                                                      |
| `agents.update`  | Admin, User         | `POST /v1/agents/{agent_id}`                                          |
| `agents.archive` | Admin, User         | `POST /v1/agents/{agent_id}/archive`                                  |

You can archive an agent but not delete it.

### Sessions

| Permission         | Roles               | Routes authorized                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------ | ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sessions.create`  | Admin, User         | `POST /v1/sessions`                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `sessions.get`     | Admin, User, Viewer | `GET /v1/sessions/{session_id}`<br />`GET /v1/sessions/{session_id}/events`<br />`GET /v1/sessions/{session_id}/events/stream`<br />`GET /v1/sessions/{session_id}/resources`<br />`GET /v1/sessions/{session_id}/resources/{resource_id}`<br />`GET /v1/sessions/{session_id}/threads`<br />`GET /v1/sessions/{session_id}/threads/{thread_id}`<br />`GET /v1/sessions/{session_id}/threads/{thread_id}/events`<br />`GET /v1/sessions/{session_id}/threads/{thread_id}/stream` |
| `sessions.list`    | Admin, User, Viewer | `GET /v1/sessions`                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `sessions.update`  | Admin, User         | `POST /v1/sessions/{session_id}`<br />`POST /v1/sessions/{session_id}/events`<br />`POST /v1/sessions/{session_id}/resources`<br />`POST /v1/sessions/{session_id}/resources/{resource_id}`<br />`DELETE /v1/sessions/{session_id}/resources/{resource_id}`                                                                                                                                                                                                                      |
| `sessions.archive` | Admin, User         | `POST /v1/sessions/{session_id}/archive`<br />`POST /v1/sessions/{session_id}/threads/{thread_id}/archive`                                                                                                                                                                                                                                                                                                                                                                       |
| `sessions.delete`  | Admin, User         | `DELETE /v1/sessions/{session_id}`                                                                                                                                                                                                                                                                                                                                                                                                                                               |

`sessions.get` authorizes reading the session, its event history and event stream, its resources, and its threads. As a result, `roles/claude.viewer` can read every session’s full event history.

Other session operations need the following permissions:

* Sending events: `sessions.update`
* Adding, changing, or removing session resources: `sessions.update`
* Archiving a thread: `sessions.archive`

### Environments

| Permission                 | Roles               | Routes authorized                                                                                                                                                                                                                                                                                                        |
| -------------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `environments.create`      | Admin, User         | `POST /v1/environments`                                                                                                                                                                                                                                                                                                  |
| `environments.get`         | Admin, User, Viewer | `GET /v1/environments/{environment_id}`<br />`GET /v1/environments/{environment_id}/work`<br />`GET /v1/environments/{environment_id}/work/stats`<br />`GET /v1/environments/{environment_id}/work/{work_id}`                                                                                                            |
| `environments.list`        | Admin, User, Viewer | `GET /v1/environments`                                                                                                                                                                                                                                                                                                   |
| `environments.update`      | Admin, User         | `POST /v1/environments/{environment_id}`                                                                                                                                                                                                                                                                                 |
| `environments.archive`     | Admin, User         | `POST /v1/environments/{environment_id}/archive`                                                                                                                                                                                                                                                                         |
| `environments.delete`      | Admin, User         | `DELETE /v1/environments/{environment_id}`                                                                                                                                                                                                                                                                               |
| `environments.processWork` | Admin, User         | `GET /v1/environments/{environment_id}/work/poll`<br />`POST /v1/environments/{environment_id}/work/{work_id}`<br />`POST /v1/environments/{environment_id}/work/{work_id}/ack`<br />`POST /v1/environments/{environment_id}/work/{work_id}/heartbeat`<br />`POST /v1/environments/{environment_id}/work/{work_id}/stop` |

`roles/claude.user` and `roles/claude.admin` include every permission that a [self-hosted sandbox](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes) worker needs. `environments.processWork` authorizes these worker actions:

* Polling for work
* Acknowledging work items
* Sending heartbeats for work items
* Stopping work items
* Updating work items

This permission is separate from `environments.update`. Reading the work queue and its statistics needs only `environments.get`.

Besides `environments.processWork`, a worker needs other permissions to run a session, such as `sessions.get` to read the session and its events, `sessions.update` to send tool results, and `skills.get` to download the agent’s skills.

### Vaults

Google Cloud records these routes in Admin Activity audit logs, except the route for `vaults.verify`, whose audit log type is Data Access.

| Permission       | Roles               | Routes authorized                                                                                                                                                                                        |
| ---------------- | ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `vaults.create`  | Admin, User         | `POST /v1/vaults`                                                                                                                                                                                        |
| `vaults.get`     | Admin, User, Viewer | `GET /v1/vaults/{vault_id}`<br />`GET /v1/vaults/{vault_id}/credentials`<br />`GET /v1/vaults/{vault_id}/credentials/{credential_id}`                                                                    |
| `vaults.list`    | Admin, User, Viewer | `GET /v1/vaults`                                                                                                                                                                                         |
| `vaults.update`  | Admin, User         | `POST /v1/vaults/{vault_id}`<br />`POST /v1/vaults/{vault_id}/credentials`<br />`POST /v1/vaults/{vault_id}/credentials/{credential_id}`<br />`DELETE /v1/vaults/{vault_id}/credentials/{credential_id}` |
| `vaults.archive` | Admin, User         | `POST /v1/vaults/{vault_id}/archive`<br />`POST /v1/vaults/{vault_id}/credentials/{credential_id}/archive`                                                                                               |
| `vaults.delete`  | Admin, User         | `DELETE /v1/vaults/{vault_id}`                                                                                                                                                                           |
| `vaults.verify`  | Admin, User         | `POST /v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate`                                                                                                                              |

Credential operations need the following permissions:

* Creating, changing, or deleting a credential: `vaults.update`
* Archiving a credential: `vaults.archive`
* Reading a credential: `vaults.get`
* Checking a stored MCP OAuth credential: `vaults.verify`

With `vaults.get`, `roles/claude.viewer` can list a vault’s credentials. Claude Models on Google Cloud (Anthropic managed) never returns a credential’s secret fields. To learn more, see [Authenticate with vaults](https://platform.claude.com/docs/en/managed-agents/vaults).

### Memory stores

| Permission             | Roles               | Routes authorized                                                                                                                                                                                                                                                                                                                          |
| ---------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `memoryStores.create`  | Admin, User         | `POST /v1/memory_stores`                                                                                                                                                                                                                                                                                                                   |
| `memoryStores.get`     | Admin, User, Viewer | `GET /v1/memory_stores/{memory_store_id}`<br />`GET /v1/memory_stores/{memory_store_id}/memories`<br />`GET /v1/memory_stores/{memory_store_id}/memories/{memory_id}`<br />`GET /v1/memory_stores/{memory_store_id}/memory_versions`<br />`GET /v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}`                    |
| `memoryStores.list`    | Admin, User, Viewer | `GET /v1/memory_stores`                                                                                                                                                                                                                                                                                                                    |
| `memoryStores.update`  | Admin, User         | `POST /v1/memory_stores/{memory_store_id}`<br />`POST /v1/memory_stores/{memory_store_id}/memories`<br />`POST /v1/memory_stores/{memory_store_id}/memories/{memory_id}`<br />`DELETE /v1/memory_stores/{memory_store_id}/memories/{memory_id}`<br />`POST /v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact` |
| `memoryStores.archive` | Admin, User         | `POST /v1/memory_stores/{memory_store_id}/archive`                                                                                                                                                                                                                                                                                         |
| `memoryStores.delete`  | Admin, User         | `DELETE /v1/memory_stores/{memory_store_id}`                                                                                                                                                                                                                                                                                               |

Memory store operations need the following permissions:

* Reading the store, its memories, or its version history: `memoryStores.get`
* Creating, changing, or deleting a memory: `memoryStores.update`
* Redacting a memory version: `memoryStores.update`

### Deployments

| Permission            | Roles               | Routes authorized                                                                                                       |
| --------------------- | ------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `deployments.create`  | Admin, User         | `POST /v1/deployments`                                                                                                  |
| `deployments.get`     | Admin, User, Viewer | `GET /v1/deployment_runs`<br />`GET /v1/deployment_runs/{deployment_run_id}`<br />`GET /v1/deployments/{deployment_id}` |
| `deployments.list`    | Admin, User, Viewer | `GET /v1/deployments`                                                                                                   |
| `deployments.update`  | Admin, User         | `POST /v1/deployments/{deployment_id}`                                                                                  |
| `deployments.archive` | Admin, User         | `POST /v1/deployments/{deployment_id}/archive`                                                                          |
| `deployments.run`     | Admin, User         | `POST /v1/deployments/{deployment_id}/run`                                                                              |
| `deployments.pause`   | Admin, User         | `POST /v1/deployments/{deployment_id}/pause`                                                                            |
| `deployments.unpause` | Admin, User         | `POST /v1/deployments/{deployment_id}/unpause`                                                                          |

Reading deployment runs needs `deployments.get`.

### Dreams

| Permission       | Roles               | Routes authorized                    |
| ---------------- | ------------------- | ------------------------------------ |
| `dreams.create`  | Admin, User         | `POST /v1/dreams`                    |
| `dreams.get`     | Admin, User, Viewer | `GET /v1/dreams/{dream_id}`          |
| `dreams.list`    | Admin, User, Viewer | `GET /v1/dreams`                     |
| `dreams.archive` | Admin, User         | `POST /v1/dreams/{dream_id}/archive` |
| `dreams.cancel`  | Admin, User         | `POST /v1/dreams/{dream_id}/cancel`  |

Dreams is a research preview feature. To request access, see [Dreams](https://platform.claude.com/docs/en/managed-agents/dreams).

### Encryption keys

Google Cloud records these routes in Admin Activity audit logs.

| Permission            | Roles | Routes authorized                                          |
| --------------------- | ----- | ---------------------------------------------------------- |
| `externalKeys.create` | Admin | `POST /v1/organizations/external_keys`                     |
| `externalKeys.get`    | Admin | `GET /v1/organizations/external_keys/{external_key_id}`    |
| `externalKeys.list`   | Admin | `GET /v1/organizations/external_keys`                      |
| `externalKeys.update` | Admin | `POST /v1/organizations/external_keys/{external_key_id}`   |
| `externalKeys.delete` | Admin | `DELETE /v1/organizations/external_keys/{external_key_id}` |

These permissions manage your organization’s encryption key registrations. Of the three predefined roles, only `roles/claude.admin` includes them.

### Usage reports

| Permission            | Roles | Routes authorized                                                                          |
| --------------------- | ----- | ------------------------------------------------------------------------------------------ |
| `usageAnalytics.list` | Admin | `GET /v1/organizations/usage_report/messages`<br />`GET /v1/organizations/analytics/usage` |
| `costAnalytics.list`  | Admin | `GET /v1/organizations/analytics/cost`                                                     |

Of the three predefined roles, only `roles/claude.admin` includes `usageAnalytics.list` and `costAnalytics.list`.

## See also

* [Claude Models on Google Cloud (Anthropic managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed)
* [IAM roles](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed#iam-roles)
* [Monitoring and logging](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed#monitoring-and-logging)
