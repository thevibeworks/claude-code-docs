---
title: Handle Compliance API errors
url: https://platform.claude.com/docs/en/manage-claude/compliance-errors
description: Compliance API error responses by HTTP status code, with the cause and fix for each.
---

<Note>
  To enable the Compliance API, see [Set up the Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api-access).
</Note>

This page lists common Compliance API error responses by HTTP status code, with the cause and the fix for each.

The Compliance API returns errors in the standard [Anthropic error format](https://platform.claude.com/docs/en/api/errors): a non-2xx status code, a `request-id` response header, and a JSON body with an `error` object containing `type` and `message`. Include the `request-id` header value when you escalate to support.

```json
{
  "error": {
    "type": "permission_error",
    "message": "Missing required scopes. Got: ['read:compliance_activities'] Needed one of: ['read:compliance_user_data', 'read:org_audit']"
  }
}
```

On this page, local sessions run on users' machines and remote sessions run in the cloud; see [Retrieve session transcripts](https://platform.claude.com/docs/en/manage-claude/compliance-sessions).

Match on the HTTP status code and `error.type`, not on the message string. Messages are stable enough to copy into runbooks but might be reworded over time; the status codes and type values are part of the API contract. A few responses that share a status code and type are told apart by their message; each is called out where it applies.

The following table tells you at a glance whether to retry. Each section that follows shows the verbatim error body and the fix.

| Status                                                                                                                     | Retry?                      | When                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------- | --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [400 Bad Request](https://platform.claude.com/docs/en/manage-claude/compliance-errors#400-bad-request)                     | No                          | Fix the request, or enable the Compliance API if the message says it is not enabled, then resend.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [401 Unauthorized](https://platform.claude.com/docs/en/manage-claude/compliance-errors#401-unauthorized)                   | No                          | The key is not recognized, has been deactivated, or has expired; re-enable or replace it, then resend.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [403 Forbidden](https://platform.claude.com/docs/en/manage-claude/compliance-errors#403-forbidden)                         | No                          | Add the missing scope or use the right key type, then resend.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [404 Not Found](https://platform.claude.com/docs/en/manage-claude/compliance-errors#404-not-found)                         | Usually no                  | A message that names a resource means it was deleted or never existed; remove it from your queue. The bare message `Not found` means the request did not authenticate (or the path does not exist), not that a resource is gone; see [Request not authenticated](https://platform.claude.com/docs/en/manage-claude/compliance-errors#request-not-authenticated). The session endpoints add two more cases: on the local session endpoints, the message `Local sessions are not available.` (returned on every call, including the list) means the endpoints are currently unavailable to your parent organization, not that a session is gone; keep your queued IDs and see [Local session not found](https://platform.claude.com/docs/en/manage-claude/compliance-errors#local-session-not-found). A remote session still in `pending` status 404s on its messages endpoint until it starts; see [Remote session not found](https://platform.claude.com/docs/en/manage-claude/compliance-errors#remote-session-not-found). |
| [409 Conflict](https://platform.claude.com/docs/en/manage-claude/compliance-errors#409-conflict)                           | No                          | The request conflicts with the resource's current state; resolve the conflict (such as detaching child resources), then retry.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [429 Too Many Requests](https://platform.claude.com/docs/en/manage-claude/compliance-errors#429-too-many-requests)         | Yes, after `retry-after`    | Wait the seconds in `retry-after`, then retry; do not advance your cursor.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [500 Internal Server Error](https://platform.claude.com/docs/en/manage-claude/compliance-errors#500-internal-server-error) | Depends on `x-should-retry` | Check the `x-should-retry` response header before retrying.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [502, 503, 504, 529](https://platform.claude.com/docs/en/manage-claude/compliance-errors#500-internal-server-error)        | Yes, with backoff           | Transient; retry with exponential backoff. Exception: some local session 503s are not transient. See [Local sessions temporarily unavailable](https://platform.claude.com/docs/en/manage-claude/compliance-errors#local-sessions-temporarily-unavailable).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

## 400 Bad Request

The request was syntactically valid, but the server rejected a parameter or the Compliance API is not enabled for the organization. Fix the cause named in the message and resend.

### Compliance API not enabled

**Type:** `invalid_request_error`

```text wrap
Compliance API is not enabled for this organization
```

**Cause:** The key is valid, but the Compliance API is not enabled for the organization or parent organization the key belongs to. Every endpoint returns this response until the API is enabled, and again if an administrator turns the API off.

**Fix:** Enable the Compliance API by following [Set up the Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api-access#set-up-the-compliance-api), then resend the request.

### Unknown query parameter

**Type:** `invalid_request_error`

```text wrap
Unknown query parameter: 'created_at[gte]'. Did you mean 'created_at.gte'?
```

**Cause:** The request included a query parameter that the endpoint does not define; the Compliance API rejects unrecognized parameters rather than ignoring them. The message names the parameter and, for near misses such as bracket notation in place of a dot or a missing `[]` suffix, suggests the defined name.

**Fix:** Use the parameter names shown on the endpoint's [Compliance API reference](https://platform.claude.com/docs/en/api/compliance) page. Range filters use dot notation (for example, `created_at.gte`), array filters take a `[]` suffix (for example, `activity_types[]`), and the pagination parameters are `after_id`, `before_id`, or `page`, depending on the endpoint.

### Invalid parameter value

**Type:** `invalid_request_error`

```text wrap
limit: Input should be less than or equal to 1000
```

```text wrap
created_at.gte: Input should be a valid datetime or date, invalid character in year
```

```text wrap
activity_types[].0: Input is not one of the permitted values.
```

**Cause:** A query parameter's value failed validation. The message starts with the parameter name (followed by the element's position for an array parameter), then states the constraint that failed. Three common cases are shown: a `limit` above the endpoint's maximum (the number in the message is that endpoint's maximum), a `created_at.*` or `updated_at.*` value that cannot be parsed as a date or timestamp, and an `activity_types[]` value that is not a supported activity type.

**Fix:** Correct the parameter named in the message. Each list endpoint has its own `limit` range; see the parameter constraints on the corresponding [Compliance API reference](https://platform.claude.com/docs/en/api/compliance) page. Send timestamps in RFC 3339 format with an explicit UTC offset, for example, `2024-03-01T00:00:00Z` or `2024-03-01T00:00:00+00:00`; the local session list rejects a timestamp without an offset (`created_at.gte: Input should have timezone info`). For the supported `activity_types[]` values, see [Query compliance activities](https://platform.claude.com/docs/en/api/compliance/activities/list).

The local session list (`GET /v1/compliance/apps/sessions/local`) also returns a 400 `invalid_request_error` when both time bounds are supplied and `created_at.lt` is not strictly after `created_at.gte`. The body reads:

```text wrap
created_at.lt must be strictly after created_at.gte.
```

Send a `created_at.lt` later than `created_at.gte`, or omit one of the bounds.

The session transcript endpoints (`GET /v1/compliance/apps/sessions/local/{session_id}/messages` and `GET /v1/compliance/apps/sessions/remote/{session_id}/messages`) validate their truncation parameters the same way: `tool_use_input_max_bytes` and `tool_result_max_bytes` each accept a positive byte count or `-1` (the server maximum), so a value such as `0` returns the same 400 `invalid_request_error`.

### Invalid pagination cursor

**Type:** `invalid_request_error`

```text wrap
Invalid activity_id format: 'activity_invalid123'
```

```text wrap
Invalid pagination cursor for 'after_id'
```

**Cause:** A pagination cursor could not be decoded. On the Activity Feed, an `after_id` or `before_id` value that is neither a cursor the API issued nor a well-formed activity ID returns the first body, which echoes the value sent. On the chat and chat message endpoints, an `after_id` or `before_id` value that cannot be decoded returns the second body, which names the parameter.

**Fix:** Treat pagination cursors as opaque strings. Always copy the `first_id` or `last_id` value returned by the previous page; stop when `has_more` is `false`. Do not construct cursors from object IDs.

The directory, project, and session endpoints (organizations, users, roles, role permissions, groups, group members, projects, project attachments, local and remote sessions, and session messages) paginate with an opaque `page` token rather than `after_id` and `before_id`. The same advice applies: pass the `next_page` value from the previous response unchanged, and stop when `has_more` is `false` (or, on the session endpoints, which return no `has_more`, when `next_page` is `null`). A malformed `page` token returns the same 400 `invalid_request_error` as a malformed `after_id` or `before_id`, with a message specific to the endpoint.

The two paginated local session endpoints (the list and the messages endpoint) return the following 400 `invalid_request_error` for any `page` value they cannot decode, for example, a token that was truncated or altered after you stored it, or one issued by a different endpoint or under a different parent organization. On the local session messages endpoint (`GET /v1/compliance/apps/sessions/local/{session_id}/messages`), each `page` cursor is also bound to the session and `order` it was issued for, so a cursor issued for a different session or sort order returns the same body:

```text wrap
The page parameter is not a valid cursor for this request.
```

Cursors on the messages endpoint also expire 24 hours after the walk (one pass through the pages) began. An expired cursor returns:

```text wrap
The page cursor has expired. Restart the walk without a page parameter; results will reflect the current retention boundary.
```

For the first body, resend the unmodified `next_page` value from the previous response to the endpoint and session that issued it. For an expired cursor, restart without a `page` parameter; the new walk reflects the retention boundary in effect when it starts, so messages that aged out of the retention period in the meantime are no longer returned (see [Retrieve a local session transcript](https://platform.claude.com/docs/en/manage-claude/compliance-sessions#retrieve-a-local-session-transcript)).

## 401 Unauthorized

The request carried a Compliance Access Key (`sk-ant-api01-...`) or Admin API key (`sk-ant-admin01-...`) that does not authenticate. A request that carries no key, or a key of another type, returns [404 Not Found](https://platform.claude.com/docs/en/manage-claude/compliance-errors#request-not-authenticated) instead on every endpoint except organization settings, and a valid key with the wrong scopes returns [403 Forbidden](https://platform.claude.com/docs/en/manage-claude/compliance-errors#403-forbidden).

### Invalid, deactivated, or expired API key

**Type:** `authentication_error`

```text wrap
API key is invalid.
```

```text wrap
API key has been deactivated.
```

```text wrap
API key has expired.
```

**Cause:** `API key is invalid.` means the value sent does not match a usable key, for example because it was truncated or altered when it was stored. `API key has been deactivated.` means the key has been disabled or deleted. `API key has expired.` means an Admin API key's expiration date has passed; Compliance Access Keys are not created with one.

**Fix:** For `API key is invalid.`, compare the value your client sends against the secret you stored when the key was created; the full secret is displayed only once, so if your stored copy is wrong, create a new key. For `API key has been deactivated.`, re-enable the key if it was only disabled, in [claude.ai > Organization settings > API](https://claude.ai/admin-settings/api-access) for a Compliance Access Key or [Claude Console > Settings > Admin keys](https://platform.claude.com/settings/admin-keys) for an Admin API key; a deleted key cannot be restored. For a deleted or expired key, create a new key and update your integration to use it, as described in [Manage and rotate keys](https://platform.claude.com/docs/en/manage-claude/compliance-api-access#manage-and-rotate-keys).

## 403 Forbidden

The key in `x-api-key` is valid but does not carry a scope the endpoint accepts. The verbatim message lists the scopes the key carries (`Got:`) and the scopes the endpoint accepts (`Needed one of:` on read endpoints, where any one listed scope is sufficient, or `Needed:` on delete endpoints), so you can confirm what the key carries without rechecking Claude Console or claude.ai. On read endpoints the accepted list also includes `read:org_audit`, a read-only audit scope that covers every Compliance API read endpoint; see [Choose scopes for a Claude Enterprise key](https://platform.claude.com/docs/en/manage-claude/admin-api-keys#choose-scopes-for-a-claude-enterprise-key). Compliance Access Key scopes are immutable after creation, so each insufficient-scope fix directs you to create a new key rather than edit the existing one. A standalone Claude Console organization (one with no parent organization) cannot create a Compliance Access Key, so fixes that require one do not apply to it; it can query the Activity Feed only.

### Insufficient scope: Activity Feed

**Type:** `permission_error`

```text wrap
Missing required scopes. Got: ['read:compliance_user_data'] Needed one of: ['read:compliance_activities', 'read:org_audit']
```

**Cause:** A key without `read:compliance_activities` was used to call `GET /v1/compliance/activities`. There are two common paths to this error:

* A Compliance Access Key (`sk-ant-api01-...`) was created without the `read:compliance_activities` scope.
* A Claude Console Admin API key (`sk-ant-admin01-...`) was created while the Compliance API was not enabled for the organization. Keys created while the Compliance API was not enabled do not carry the scope; see [Set up the Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api-access#set-up-the-compliance-api).

**Fix:** Compliance Access Key scopes are immutable after creation. Create a new key that includes `read:compliance_activities`, or use a Claude Console Admin API key. See [Which key do you need?](https://platform.claude.com/docs/en/manage-claude/compliance-api-access#which-key-do-you-need) for the conditions under which an Admin API key carries this scope.

### Insufficient scope: organization data

**Type:** `permission_error`

```text wrap
Missing required scopes. Got: ['read:compliance_user_data'] Needed one of: ['read:compliance_org_data', 'read:org_audit']
```

**Cause:** A key without `read:compliance_org_data` was used to call an organizations, roles, groups, or effective-settings endpoint. There are two common paths to this error:

* A Compliance Access Key (`sk-ant-api01-...`) was created without the `read:compliance_org_data` scope.
* A Claude Console Admin API key (`sk-ant-admin01-...`) was used. Admin API keys carry only `read:compliance_activities` and cannot read organization metadata.

**Fix:** [Create a new Compliance Access Key](https://platform.claude.com/docs/en/manage-claude/compliance-api-access#set-up-the-compliance-api) with `read:compliance_org_data` selected. Admin API keys cannot read organization metadata; the Compliance Access Key is required.

### Retired scope: organization settings

**Type:** `permission_error`

```text wrap
Missing required scopes. Got: ['read:compliance_org_settings'] Needed one of: ['read:compliance_org_data', 'read:org_audit']
```

**Cause:** The `read:compliance_org_settings` scope was retired on June 30, 2026. `GET /v1/compliance/organizations/{organization_id}/settings` now requires `read:compliance_org_data`, the same scope as the other organization endpoints, and the retired scope no longer authorizes anything. A Compliance Access Key that carries only `read:compliance_org_settings` returns this error on every call to the settings endpoint, even though the key worked before the retirement. The retired scope can no longer be selected or granted when creating a key.

**Fix:** Compliance Access Key scopes are immutable after creation. [Create a new Compliance Access Key](https://platform.claude.com/docs/en/manage-claude/compliance-api-access#set-up-the-compliance-api) with `read:compliance_org_data` selected, update your integration to use it, then delete the old key. A key that already carries `read:compliance_org_data` is unaffected by the retirement.

### Insufficient scope: user data

**Type:** `permission_error`

```text wrap
Missing required scopes. Got: ['read:compliance_activities'] Needed one of: ['read:compliance_user_data', 'read:org_audit']
```

**Cause:** A key without `read:compliance_user_data` was used to call a chats, messages, files, projects, sessions, organization users, or group-members endpoint. There are two common paths to this error:

* A Compliance Access Key (`sk-ant-api01-...`) was created without the `read:compliance_user_data` scope.
* A Claude Console Admin API key (`sk-ant-admin01-...`) was used. Admin API keys carry only `read:compliance_activities` and cannot be granted `read:compliance_user_data`, so they cannot call the chat, file, project, project attachment, session, user, or group-member endpoints.

**Fix:** Use a [Compliance Access Key](https://platform.claude.com/docs/en/manage-claude/compliance-api-access#set-up-the-compliance-api) created in claude.ai with `read:compliance_user_data` selected. If the request really should be Activity Feed only, point the Admin API key at `GET /v1/compliance/activities` instead.

### Insufficient scope: delete

**Type:** `permission_error`

```text wrap
Missing required scopes. Got: ['read:compliance_user_data'] Needed: ['delete:compliance_user_data']
```

**Cause:** A Compliance Access Key without `delete:compliance_user_data` was used to call a `DELETE` endpoint on chats, files, or projects.

**Fix:** [Create a new Compliance Access Key](https://platform.claude.com/docs/en/manage-claude/compliance-api-access#set-up-the-compliance-api) with `delete:compliance_user_data` selected. The delete scope is separate from `read:compliance_user_data` so that read-only audit keys cannot delete content.

## 404 Not Found

A 404 whose message names a resource or a resource type means the ID in the path does not exist or has already been deleted. Compliance API deletes are immediate and permanent, so a 404 on a previously known ID usually means the content is gone: hard-deleted through a Compliance API delete call, removed by a retention policy, or, for files and artifacts, deleted along with their chat by a user in claude.ai. A 404 with the bare message `Not found` is different: the request did not authenticate (or the path does not exist), and any endpoint can return it, list endpoints included; see [Request not authenticated](https://platform.claude.com/docs/en/manage-claude/compliance-errors#request-not-authenticated). The session endpoints add two cases. On the local session endpoints, a separate 404 message, `Local sessions are not available.`, is returned on every call (including the list) while the endpoints are unavailable to your parent organization; it does not depend on the session ID and can be temporary. See [Local session not found](https://platform.claude.com/docs/en/manage-claude/compliance-errors#local-session-not-found). On the remote session endpoints, a session that is still being provisioned (`status` of `pending`) has no transcript yet, so its messages endpoint 404s until the session starts. See [Remote session not found](https://platform.claude.com/docs/en/manage-claude/compliance-errors#remote-session-not-found). The activity-type strings cited in each Fix (for example, `claude_chat_created`) are values you can pass to the Activity Feed `activity_types[]` filter; see [Query compliance activities](https://platform.claude.com/docs/en/api/compliance/activities/list) for every supported value.

### Request not authenticated

**Type:** `not_found_error`

```text wrap
Not found
```

**Cause:** The request did not carry a credential the Compliance API accepts: no API key was sent, or the key is not a Compliance Access Key (`sk-ant-api01-...`) or Admin API key (`sk-ant-admin01-...`), for example, a Claude API key (`sk-ant-api03-...`). The status, type, and message are the same as for a path that does not exist and do not depend on the endpoint or any resource ID, so list endpoints such as `GET /v1/compliance/activities` return this body too. The one exception is `GET /v1/compliance/organizations/{organization_id}/settings`, which answers these requests with 401 `authentication_error`. On every endpoint, a Compliance Access Key or Admin API key that does not authenticate returns [401 Unauthorized](https://platform.claude.com/docs/en/manage-claude/compliance-errors#401-unauthorized) instead.

**Fix:** Send the key in the `x-api-key` header and check its prefix: the Compliance API accepts only `sk-ant-api01-...` and `sk-ant-admin01-...` keys; see [Which key do you need?](https://platform.claude.com/docs/en/manage-claude/compliance-api-access#which-key-do-you-need). If the header and key are right and one path still returns `Not found` while others succeed, check that path against the [Compliance API reference](https://platform.claude.com/docs/en/api/compliance).

### Chat not found

**Type:** `not_found_error`

```text wrap
Chat conversation not found: 'claude_chat_01H5CWunD7RpVJ5bHa8RCkja'
```

**Cause:** The chat ID in the path does not match a chat readable through the Compliance API. The chat might have been hard-deleted through a previous Compliance API call or removed by your organization's retention policy, or it might belong to an organization the calling key cannot read. Chats that a user deleted in claude.ai do not return 404; they remain readable, with `deleted_at` populated, but without their message content.

**Fix:** Confirm the chat ID against a recent `claude_chat_created` or `claude_chat_viewed` activity. If the activity is recent and the read still fails, the chat has been hard-deleted (through this API or by retention-policy expiry) or belongs to an organization outside your key's scope.

### File not found

**Type:** `not_found_error`

```text wrap
File not found: 0d3b8f72-6c1e-4a59-b2de-7f4c9a1e5b60
```

**Cause:** The file ID does not exist in an organization your key can read, or the file has been deleted. Deleting a chat in claude.ai also deletes the files attached to it, although the chat itself remains listed. The message identifies the file by its underlying UUID rather than by the `claude_file_...` ID sent in the request. The metadata, content, and delete endpoints return this body; it applies to both chat-attached files (`claude_file_...`) and project files.

**Fix:** Reconcile against recent `claude_file_uploaded` or `claude_file_deleted` activities. Files deleted along with a chat have no `claude_file_deleted` activity, so check for the chat's `claude_chat_deleted` activity as well. If the file was deleted, the binary is gone; the activity records remain in the feed for the 6-year retention window.

### Generated file or artifact not found

**Type:** `not_found_error`

```text wrap
Generated file not found: 'claude_gen_file_01TbR8wAcCeFhJkLnPqStUvX'
```

```text wrap
Generated file content not found: 'claude_gen_file_01TbR8wAcCeFhJkLnPqStUvX'
```

```text wrap
Artifact version not found: 'claude_artifact_version_01KmNpQrSt3UvWxYz5AbCdEfG'
```

**Cause:** The ID in the path does not match a tool-generated file or artifact version readable through the Compliance API. The generated-file metadata endpoint returns the first body, the content endpoint returns the second, and both artifact endpoints return the third. Generated files and artifacts are deleted with the chat they were created in, including when a user deletes the chat in claude.ai.

**Fix:** Use [Get chat messages](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list) to look up the chat the ID came from. If the chat's `deleted_at` is populated, or a `claude_chat_deleted` activity names the chat, the content is gone; remove the ID from your queue. Otherwise, confirm the ID against the `generated_files` and `artifacts` arrays on the chat's messages.

### Project not found

**Type:** `not_found_error`

```text wrap
No project is found with the provided id.
```

```text wrap
No project found with provided id, or it has already been deleted.
```

**Cause:** The project ID does not exist or has been deleted. The project detail, attachments, and collaborators endpoints return the first body; `DELETE /v1/compliance/apps/projects/{project_id}` returns the second.

**Fix:** Reconcile against recent `claude_project_created` or `claude_project_deleted` activities. The Activity Feed continues to expose the project's lifecycle events even after the project itself is gone.

### Project document not found

**Type:** `not_found_error`

```text wrap
No project document found with the provided id.
```

```text wrap
No project document found with the provided id, or it has already been deleted.
```

**Cause:** The project document ID does not exist or has been deleted. The document content and metadata endpoints return the first body; `DELETE /v1/compliance/apps/projects/documents/{document_id}` returns the second. This error applies to text project documents (`claude_proj_doc_...`), not to project files.

**Fix:** Use `GET /v1/compliance/apps/projects/{project_id}/attachments` to list current attachments. If the document is missing, it was deleted; retrieve it through a `claude_project_document_uploaded` activity record if you only need the metadata. The activity record shows who uploaded the document, when, and to which project, but not its name.

### Local session not found

**Type:** `not_found_error`

```text wrap
Local session not found.
```

**Cause:** The session ID passed to `GET /v1/compliance/apps/sessions/local/{session_id}` or `GET /v1/compliance/apps/sessions/local/{session_id}/messages` does not match a local session readable through the Compliance API. Both endpoints return this one message, without distinguishing the cause, when the ID is not a session in an organization your key can read (including IDs that belong to another parent organization), when the session never existed, when [zero data retention](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#zero-data-retention-zdr-scope) is in effect for the session, or when all of the session's activity has aged past the retention period that applies to the organization that ran it. The `Local session not found.` response has no transient form, because local sessions have no provisioning (`pending`) state; compare [Remote session not found](https://platform.claude.com/docs/en/manage-claude/compliance-errors#remote-session-not-found), where a `pending` session 404s until it starts. A session ID that is not a well-formed `clls_` identifier returns [400 Bad Request](https://platform.claude.com/docs/en/manage-claude/compliance-errors#400-bad-request) instead.

The local session endpoints, including the list endpoint, return a different 404 message, `Local sessions are not available.`, while the endpoints themselves are unavailable to your parent organization. That response does not depend on the session ID; no customer-side key, scope, or setting changes it, and it can be temporary. Both responses carry the `not_found_error` type; the message text is what tells them apart.

**Fix:** Confirm the session ID against `GET /v1/compliance/apps/sessions/local`; see [Sessions on users' machines](https://platform.claude.com/docs/en/manage-claude/compliance-sessions#retrieve-local-sessions). If the session no longer appears in the list, its content has aged past retention (or the session is otherwise no longer in an organization your key can read) and its transcript is not retrievable; remove the ID from your queue. If every call, including the list, returns `Local sessions are not available.`, keep your queued session IDs and retry on your next scheduled run; if the response persists, contact your Anthropic representative and include the `request-id` response header.

### Remote session not found

**Type:** `not_found_error`

```text wrap
Remote session not found.
```

**Cause:** The session ID passed to `GET /v1/compliance/apps/sessions/remote/{session_id}/messages` does not match a session transcript readable through the Compliance API. This occurs when the session ID (`cse_...`) does not exist or the session has been deleted, when the session belongs to an organization your key cannot read, or when the session's `status` is still `pending`: a pending session has no transcript yet, so the messages endpoint returns 404 until the session starts. A session ID that is not a well-formed `cse_` identifier returns [400 Bad Request](https://platform.claude.com/docs/en/manage-claude/compliance-errors#400-bad-request) instead.

**Fix:** Confirm the session ID and its `status` against `GET /v1/compliance/apps/sessions/remote`; see [Sessions in the cloud](https://platform.claude.com/docs/en/manage-claude/compliance-sessions#retrieve-remote-sessions). If the session is `pending`, retry after it leaves that status. If the session no longer appears in the list, it has been deleted and its transcript is not retrievable.

### Organization, role, or group not found

**Type:** `not_found_error`

```text wrap
The "ce86b5f3-7c16-48b3-a9f3-e1d2c4b8a0f1" organization does not exist or the requester is not authorized to access it.
```

The organization, role, and group endpoints return a 404 `not_found_error` in the standard error format. The organization message names the `org_uuid`; the role and group messages are generic (`Role not found.`, `Group not found.`). This occurs when a path ID (`org_uuid`, `role_id`, or `group_id`) does not exist or no longer belongs to a tree the calling key can read.

**Cause:** The ID in the path does not match a record readable through the Compliance API. Roles and groups can be deleted, and organizations can be unlinked from the parent tree.

**Fix:** Verify the ID against the corresponding list endpoint, and reconcile against recent organization, role, or group activities in the [Activity Feed](https://platform.claude.com/docs/en/manage-claude/compliance-activity-feed).

### Organization settings not available

**Type:** `not_found_error`

```text wrap
organization `91012d09-e48b-438e-a489-1bebfd8fa6f9` not found in this organization's hierarchy
```

**Cause:** `GET /v1/compliance/organizations/{organization_id}/settings` returns this 404 in three cases that intentionally share the same body so the response does not reveal whether an organization exists: the `organization_id` is not one of your parent's linked organizations, the value is not a valid UUID, or the settings endpoint is not yet enabled for your parent organization.

**Fix:** Verify the ID against [List organizations](https://platform.claude.com/docs/en/api/compliance/organizations/list). If a known-good organization ID still returns 404, the settings endpoint is not yet enabled for your parent organization; contact your Anthropic representative.

## 409 Conflict

The request is well-formed and authorized but conflicts with the resource's current state. The body carries the `invalid_request_error` type, which 400 responses also use, so distinguish a conflict by the 409 status code rather than by `error.type`.

### Project has attached chats

**Type:** `invalid_request_error`

```text wrap
The "claude_proj_01KGp4eZNug9ri4kE35RSppq" project cannot be deleted as it has chats attached to it. Delete or detach all chats, and try deleting the project again.
```

**Cause:** `DELETE /v1/compliance/apps/projects/{project_id}` was called on a project that still has chats attached.

**Fix:** List the project's chats with `GET /v1/compliance/apps/chats?user_ids[]={user_id}&project_ids[]={project_id}` (the `project_ids[]` filter requires at least one `user_ids[]` value; enumerate IDs through [List organization users](https://platform.claude.com/docs/en/manage-claude/compliance-org-data#list-organization-users)), delete each one with `DELETE /v1/compliance/apps/chats/{claude_chat_id}`, and then retry the project delete.

## 429 Too Many Requests

Requests to the Compliance API are limited to **600 requests per minute per [parent organization](https://platform.claude.com/docs/en/manage-claude/compliance-api#how-the-compliance-api-works)**. The limit is one budget shared across every key under the parent (Compliance Access Keys and the Admin API keys of all linked organizations) and across every `/v1/compliance/*` endpoint; the remote session endpoints carry a second request budget on top. For a standalone Claude Console organization, which has no parent organization, the same budget applies to the organization itself and is shared across its Admin API keys. Contact your Anthropic representative if your integration needs a higher limit.

Once your API key authenticates, Compliance API responses report the shared budget through the standard [rate-limit response headers](https://platform.claude.com/docs/en/api/rate-limits#response-headers) so your client can throttle proactively instead of waiting for a 429:

* `anthropic-ratelimit-requests-limit` is the per-minute request budget.
* `anthropic-ratelimit-requests-remaining` is the budget left in the current window.
* `anthropic-ratelimit-requests-reset` is the RFC 3339 timestamp when the window resets and the full budget is restored.

A 429 response also carries a `retry-after` header with the number of seconds to wait before sending the next request. This value might include a small safety margin beyond `anthropic-ratelimit-requests-reset`; honor `retry-after`.

```http
HTTP/1.1 429 Too Many Requests
date: Tue, 21 Apr 2026 14:38:02 GMT
retry-after: 25
anthropic-ratelimit-requests-limit: 600
anthropic-ratelimit-requests-remaining: 0
anthropic-ratelimit-requests-reset: 2026-04-21T14:38:25Z
```

```json
{
  "error": {
    "type": "rate_limit_error",
    "message": "Compliance API rate limit of 600 requests per minute per parent organization has been exceeded. Retry after the time indicated by the retry-after header. Quote the request-id response header when contacting Anthropic support."
  }
}
```

**Cause:** Your parent organization (or standalone Claude Console organization) sent more than 600 requests to `/v1/compliance/*` in a 1-minute window, across all of the keys that share its budget, or it exhausted the remote session endpoints' second request budget (described later in this section).

**Fix:** Wait the number of seconds in the `retry-after` header, then retry. If the header is absent (for example, stripped by an intermediary), fall back to exponential backoff (start at 1 second, double up to 60 seconds). Do not advance your pagination cursor on a 429: the failed request returned no data, so the cursor from the last successful page is still correct.

Requests that fail authentication (a missing or unrecognized key, or a Claude API key rather than a Compliance Access Key or Admin API key) are rejected before the rate limiter and do not consume quota. A valid key that lacks the endpoint's required scope consumes one quota unit before the 403 is returned.

The [local session endpoints](https://platform.claude.com/docs/en/manage-claude/compliance-sessions#retrieve-local-sessions) count only against the shared limit. The [remote session endpoints](https://platform.claude.com/docs/en/manage-claude/compliance-sessions#retrieve-remote-sessions) also carry a second request budget, keyed to your parent organization like the shared limit, on top of it. A 429 from that budget carries a `retry-after` header that is always `1` (a minimum wait, not the actual reset time); any `anthropic-ratelimit-*` headers on that response describe the shared limit rather than this budget, so back off exponentially if the 429 repeats.

If you poll the [Activity Feed](https://platform.claude.com/docs/en/manage-claude/compliance-activity-feed) on a schedule, budget your aggregate request rate (across all keys, linked organizations, and concurrent workers) below the shared limit. Watch `anthropic-ratelimit-requests-remaining` to slow down before you reach it. See [Design your compliance integration](https://platform.claude.com/docs/en/manage-claude/compliance-integration-patterns#choose-a-feed-consumption-pattern) for choosing between window-polling and cursor-driven ingestion.

## 500 Internal Server Error

A 500 from the Compliance API carries an `x-should-retry: false` response header when the failure is deterministic. Anthropic SDKs honor this header automatically. If you use a generic HTTP retry library that retries on every 5xx, suppress retries when `x-should-retry` is `false`; retrying this error fails identically on every attempt.

A 500 without the `x-should-retry: false` header is transient: retry with exponential backoff (start at 1 second, double up to 60 seconds). The same applies to 502, 503, 504, and 529 responses. The exception is a small set of local session 503s, described next, that depend on an organization's settings or encryption key rather than on load. See [Errors](https://platform.claude.com/docs/en/api/errors) for the platform-wide retry semantics.

### Local sessions temporarily unavailable

**Type:** `overloaded_error`

```text wrap
The local-sessions index is temporarily unavailable. Try again shortly.
```

```text wrap
Captured content is temporarily unavailable. Try again shortly.
```

```text wrap
The local-sessions index cannot currently evaluate retention overrides for this page. Try again later.
```

**Cause:** The [local session endpoints](https://platform.claude.com/docs/en/manage-claude/compliance-sessions#retrieve-local-sessions) return 503 with one of these bodies. All three share the `overloaded_error` type, so this is one of the few errors on this page where you need the message text, not `error.type`, to tell the conditions apart:

* The `index is temporarily unavailable` body means session listings are briefly unavailable because of load or a backend condition. This is transient.
* The `Captured content` body means a session's transcript content cannot be returned right now. This is usually transient too. In organizations that use [customer-managed encryption keys](https://platform.claude.com/docs/en/manage-claude/cmek), the messages endpoint also returns this body for every page that contains content your customer-managed key cannot decrypt, for example because you disabled, revoked, or destroyed the key, or because the key cannot be reached. In that case the error persists for as long as the key cannot be used. The message text is the same either way, so the only signal that the key is the cause is that the error keeps recurring for that organization. An unusable key is never reported as `not_captured`.
* The `retention overrides` body means a retention or data-handling setting that applies to one or more sessions in the requested range could not be evaluated yet. On the retrieve and messages endpoints it reads `for this session` instead of `for this page`. It depends on the data and settings of the organization that ran the session rather than on load, and it can persist for an extended period.

**Fix:** Handle each body as follows:

* For the two `Try again shortly.` bodies, retry with exponential backoff and do not advance your `page` cursor, because the failed request returned no data.
* If the `Captured content` body keeps recurring on the messages endpoint for an organization that uses a customer-managed key, treat it as persistent: stop walking that organization's transcripts and check the key's status in your key management service. Transcripts in other linked organizations, and session metadata everywhere, are unaffected. If you retry on a later run, restart each session's walk without `page`, because messages page cursors expire 24 hours after the walk's first page.
* For the `Try again later.` body, do not hold a walk open waiting for it to clear. On the list endpoint, either retry later by restarting without the `page` parameter (a list page token older than 24 hours is still accepted but is re-evaluated against the current retention boundary, so a parked walk can skip sessions), or narrow the `created_at.gte` and `created_at.lt` window until the request succeeds and export the skipped range separately on a later run. On the retrieve and messages endpoints, skip that session ID, continue with the rest of your export, and retry the session on a later run. Messages page cursors expire 24 hours after the walk's first page, so restart that session's walk without `page` when you return to it.

If any of these conditions recurs across runs, contact your Anthropic representative and include the `request-id` response header. For the customer-managed key case, do this only if the error continues while that key is usable.

For service-wide incidents, check [status.anthropic.com](https://status.anthropic.com).

## Next steps

<CardGroup cols={2}>
  <Card title="Compliance API FAQ" href="https://platform.claude.com/docs/en/manage-claude/compliance-faq">
    Common questions about access, scopes, retention, and integration.
  </Card>

  <Card title="Errors" href="https://platform.claude.com/docs/en/api/errors">
    The platform-wide error catalog and retry semantics.
  </Card>
</CardGroup>
