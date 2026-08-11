# Retrieve and delete chats, files, and projects

Access chat content, file attachments, and projects for claude.ai organizations through the Compliance API.

---

<Note>
  The endpoints on this page are available only to Claude Enterprise organizations. They retrieve claude.ai chats, files, projects, and Cowork and Claude Code session transcripts; they delete chats, files, and projects. See [Set up the Compliance API](/docs/en/manage-claude/compliance-api-access).
</Note>

<Check>
  **Required scope:** `read:compliance_user_data` on the Compliance Access Key. The delete endpoints also require `delete:compliance_user_data`.

  **Prerequisite:** None for listing chats or sessions organization-wide. To filter the chat or remote session lists to specific users, you need user IDs from [List organization users](/docs/en/manage-claude/compliance-org-data#list-organization-users); the local session list has no user filter. The other endpoints on this page take resource IDs directly.
</Check>

The endpoints on this page expose Claude Enterprise chat content, file uploads, projects, project attachments, and session transcripts to compliance reviewers. They support eDiscovery (electronic discovery) exports, data loss prevention (DLP) enforcement, and account-deletion responses. Chat, file, and project content is retained for as long as your organization's retention policy allows; remote session transcripts are retained for 6 years, and local session transcripts (Cowork and Claude Code sessions on your users' machines) for 6 years by default (or your organization's custom conversation retention period, when a finite one is set). Chats that a user has soft-deleted in claude.ai remain visible through the Compliance API with `deleted_at` populated; chats that have been hard-deleted (through the Compliance API itself, or after the organization's retention window expires) are not retrievable.

Both scopes are granted only on Compliance Access Keys (`sk-ant-api01-...`) created in claude.ai; see [Set up the Compliance API](/docs/en/manage-claude/compliance-api-access) to provision one. The `read:compliance_user_data` scope covers retrieval; `delete:compliance_user_data` is required only for the delete endpoints. The chat, file, project, attachment, and session endpoints are not available to Admin API keys (`sk-ant-admin01-...`); calls authenticated with an Admin API key return [403 Forbidden](/docs/en/manage-claude/compliance-errors#403-forbidden).

Endpoints on this page paginate two ways; see [Paginate results](/docs/en/manage-claude/compliance-activity-feed#paginate-results) for the full reference. Each section notes which scheme applies.

## Retrieve chats and messages

Use [List chats](/docs/en/api/compliance/apps/chats/list) to page through chat metadata, then [Get chat messages](/docs/en/api/compliance/apps/chats/messages/list) to fetch the full message content of one chat.

The chat list endpoint defaults to organization-wide scope: leave off `user_ids[]` to include every chat under your parent organization. Add `order_by=updated_at` to sort by last update time. This combination is the recommended way to export chats and keep an export current, because one paginated loop picks up both new and modified chats for every user without enumerating users first. The following request lists chats updated since a given date.

```bash cURL
curl --fail-with-body -sS -G \
  "https://api.anthropic.com/v1/compliance/apps/chats" \
  --header "x-api-key: $ANTHROPIC_COMPLIANCE_ACCESS_KEY" \
  --data-urlencode "order_by=updated_at" \
  --data-urlencode "updated_at.gte=2025-06-01T00:00:00Z" \
  --data-urlencode "limit=100"
```

```json Response
{
  "data": [
    {
      "id": "claude_chat_01H5CWunD7RpVJ5bHa8RCkja",
      "name": "Product Requirements Discussion",
      "created_at": "2026-04-10T08:09:10Z",
      "updated_at": "2026-04-10T09:10:11Z",
      "deleted_at": null,
      "href": "https://claude.ai/chat/abcdef01-2345-6789-abcd-ef0123456789",
      "model": "claude-opus-5",
      "organization_uuid": "91012d09-e48b-438e-a489-1bebfd8fa6f9",
      "project_id": "claude_proj_01KGp4eZNug9ri4kE35RSppq",
      "user": {
        "id": "user_01XyDMpzjS89pFZXqSFUBDr6",
        "email_address": "user@example.com"
      }
    }
  ],
  "has_more": true,
  "first_id": "eyJrIjogInVwZGF0ZWRfYXQiLCAidCI6ICIyMDI2LTA0LTEwVDA5OjEwOjExKzAwOjAwIiwgImlkIjogImFiY2RlZjAxLS4uLiJ9",
  "last_id": "eyJrIjogInVwZGF0ZWRfYXQiLCAidCI6ICIyMDI2LTA0LTEwVDA5OjEwOjExKzAwOjAwIiwgImlkIjogImFiY2RlZjAxLS4uLiJ9"
}
```

Results sort ascending by the `order_by` field, oldest first, with ties broken by `id`. Pagination uses the standard `first_id`/`last_id`/`has_more` cursor fields described in [Paginate results](/docs/en/manage-claude/compliance-activity-feed#paginate-results). To walk forward toward newer chats, pass the response's `last_id` back as `after_id` on the next request.

That forward walk is also how you keep an export current across runs: persist the final page's `last_id` and resume from it as `after_id` on the next run. Because the list is ordered by `updated_at`, a chat that changes after your saved cursor reappears ahead of it, so each incremental run returns both brand-new chats and older chats that have since been modified. Process results idempotently, keyed by chat `id`, to handle those reappearances.

A few constraints apply to these organization-wide queries. Cursors are opaque and bound to the sort key, so an `after_id` issued under one `order_by` value is rejected with a 400 error under the other. Time-filter bounds must match the sort key too: pair `updated_at.*` bounds with `order_by=updated_at`, and `created_at.*` bounds with the default `order_by=created_at`. Backward pagination with `before_id` is not supported, and the `project_ids[]` filter is not available. See [List chats](/docs/en/api/compliance/apps/chats/list) for the full filter reference.

To scope the list to specific users instead (for example, a legal hold on named custodians), pass 1–10 `user_ids[]` values. Obtain the IDs from [List organization users](/docs/en/manage-claude/compliance-org-data#list-organization-users). User-filtered queries always sort by `created_at` (passing `order_by=updated_at` returns a 400 error) and support both `after_id` and `before_id`. Filtering by `project_ids[]` is only available in this user-filtered form.

```bash cURL
curl --fail-with-body -sS -G \
  "https://api.anthropic.com/v1/compliance/apps/chats" \
  --header "x-api-key: $ANTHROPIC_COMPLIANCE_ACCESS_KEY" \
  --data-urlencode "user_ids[]=user_01XyDMpzjS89pFZXqSFUBDr6" \
  --data-urlencode "created_at.gte=2025-06-01T00:00:00Z" \
  --data-urlencode "limit=100"
```

The list response carries chat metadata only. To pull the actual chat content, attached files, and inline artifacts (structured documents Claude generates inside a chat), follow up with the messages endpoint for each chat ID:

```bash cURL
chat_id="claude_chat_01H5CWunD7RpVJ5bHa8RCkja"

curl --fail-with-body -sS \
  "https://api.anthropic.com/v1/compliance/apps/chats/$chat_id/messages" \
  --header "x-api-key: $ANTHROPIC_COMPLIANCE_ACCESS_KEY"
```

The messages endpoint returns the chat's metadata plus a `chat_messages` array sorted by `created_at`. When `limit` is omitted, the full message set is returned in one response; pass `limit`, `after_id`, or `before_id` to page through very long chats. The endpoint also accepts `created_at.*` and `updated_at.*` range bounds (`gt`, `gte`, `lt`, `lte`) and an `order` parameter (`asc` or `desc`). See [Get chat messages](/docs/en/api/compliance/apps/chats/messages/list) for the full parameter list. For user messages, `created_at` is when the message was sent; for assistant messages, it is when Claude finished generating the message. Each message carries its text content and, when present, any uploaded files (typically on user messages), any tool-generated files, and any artifacts the assistant produced or updated (typically on assistant messages):

```json Response
{
  "id": "claude_chat_01H5CWunD7RpVJ5bHa8RCkja",
  "name": "Product Requirements Discussion",
  "created_at": "2026-04-10T08:09:10Z",
  "updated_at": "2026-04-10T09:10:11Z",
  "deleted_at": null,
  "href": "https://claude.ai/chat/abcdef01-2345-6789-abcd-ef0123456789",
  "model": "claude-opus-5",
  "organization_uuid": "91012d09-e48b-438e-a489-1bebfd8fa6f9",
  "project_id": "claude_proj_01KGp4eZNug9ri4kE35RSppq",
  "user": {
    "id": "user_01XyDMpzjS89pFZXqSFUBDr6",
    "email_address": "user@example.com"
  },
  "chat_messages": [
    {
      "id": "claude_chat_msg_01VnBPkLmtj7YdW5QrXKEA8c",
      "role": "user",
      "created_at": "2026-04-10T08:09:10Z",
      "content": [
        {
          "type": "text",
          "text": "Can you help me draft requirements for our new dashboard feature?"
        }
      ],
      "files": [
        {
          "id": "claude_file_01UaT9wBcDfGhJkLmNpQrSv7",
          "filename": "dashboard_mockup_v1.pdf",
          "mime_type": "application/pdf"
        }
      ]
    },
    {
      "id": "claude_chat_msg_01M8tFcHwbQ2kY6NpEjRZv4D",
      "role": "assistant",
      "created_at": "2026-04-10T08:09:11Z",
      "content": [
        {
          "type": "text",
          "text": "I'd be happy to help you draft requirements for your dashboard feature..."
        }
      ],
      "generated_files": [
        {
          "id": "claude_gen_file_01TbR8wAcCeFhJkLnPqStUvX",
          "filename": "requirements_summary.csv",
          "mime_type": "text/csv"
        }
      ],
      "artifacts": [
        {
          "id": "claude_artifact_01HqRsTuVwXyZa2BcDeFgH4J",
          "version_id": "claude_artifact_version_01KmNpQrSt3UvWxYz5AbCdEfG",
          "title": "Dashboard Requirements Draft",
          "artifact_type": "text/markdown"
        }
      ]
    }
  ],
  "has_more": false,
  "first_id": "eyJtc2dfdXVpZCI6ICIwZjcwYjA2Ni0uLi4ifQ==",
  "last_id": "eyJtc2dfdXVpZCI6ICJhNGUwYjE3Mi0uLi4ifQ=="
}
```

`files`, `generated_files`, and `artifacts` can each be `null` on a given message. `files` are binary uploads (PDFs, images, spreadsheets) the user attached to the message. `generated_files` are binary files the assistant created during the conversation through tool use (for example, PDFs, spreadsheets, or slide decks). `artifacts` are versioned documents (for example, code or markdown) the assistant generated or updated in its response; an artifact can be revised across multiple assistant turns in the same chat, and each revision appears as a new `version_id` under the same artifact `id`. Pass each entry's `id` (or `version_id` for artifacts) to the matching content endpoint in [Retrieve files and artifacts](#retrieve-files-and-artifacts) to download it.

## Retrieve files and artifacts

Files and artifacts are downloaded by ID, not listed independently. The IDs come from the chat messages endpoint in [Retrieve chats and messages](#retrieve-chats-and-messages) (the `files`, `generated_files`, and `artifacts` arrays on each message) or, for project-level uploads, from the [project attachments endpoint](#retrieve-projects-and-attachments).

Pick the endpoint that matches your ID type and the data you need. The same file content endpoint serves both chat files and project files.

| You have                       | You want                                | Use this endpoint                                                                               |
| ------------------------------ | --------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `claude_file_*` ID             | The file's binary content               | [Download file content](/docs/en/api/compliance/apps/chats/files/download)                      |
| `claude_file_*` ID             | The file's metadata only                | [Get file metadata](/docs/en/api/compliance/apps/chats/files/retrieve)                          |
| `claude_gen_file_*` ID         | A tool-generated file's binary content  | [Download a Claude-generated file](/docs/en/api/compliance/apps/chats/generated_files/download) |
| `claude_gen_file_*` ID         | A tool-generated file's metadata only   | [Get generated-file metadata](/docs/en/api/compliance/apps/chats/generated_files/retrieve)      |
| `claude_artifact_version_*` ID | One artifact version's text             | [Download artifact content](/docs/en/api/compliance/apps/artifacts/download)                    |
| `claude_artifact_version_*` ID | The artifact version's metadata only    | [Get artifact metadata](/docs/en/api/compliance/apps/artifacts/retrieve)                        |
| `claude_proj_doc_*` ID         | A project document's plain-text content | [Get project document content](/docs/en/api/compliance/apps/projects/documents/retrieve)        |
| `claude_proj_doc_*` ID         | A project document's metadata only      | [Get project document metadata](/docs/en/api/compliance/apps/projects/documents/metadata)       |

The file content endpoint streams the original upload as a chunked binary response with these headers:

* `Content-Disposition: attachment; filename*=utf-8''<percent-encoded filename>` carries the original upload file name in RFC 5987 extended form. The extended form is used for every file name, not only non-ASCII ones.
* `Content-Type` carries the upload's MIME type.
* `Content-MD5` carries the file's MD5 digest, base64-encoded as specified in RFC 1864.
* `Transfer-Encoding: chunked` is always set.

```bash cURL
file_id="claude_file_01UaT9wBcDfGhJkLmNpQrSv7"

curl --fail-with-body -sS -OJ \
  --header "x-api-key: $ANTHROPIC_COMPLIANCE_ACCESS_KEY" \
  "https://api.anthropic.com/v1/compliance/apps/chats/files/$file_id/content"
```

The `-OJ` flags tell curl to save the response under the file name from `Content-Disposition`, which is the original file name the user uploaded.

The artifact content endpoint returns the text body of one artifact version. Pass the `version_id` from one of the entries in an assistant message's `artifacts` array, not the artifact's stable `id`. Each new version of an artifact has its own `version_id`, and the Compliance API serves the exact bytes of that version.

## Retrieve projects and attachments

Projects bundle related chats together with custom instructions, knowledge base content, and attached files or text documents. The Compliance API exposes project metadata, project details, and the list of attachments belonging to a project.

* [List projects](/docs/en/api/compliance/apps/projects/list)
* [Get project details](/docs/en/api/compliance/apps/projects/retrieve)
* [List project attachments](/docs/en/api/compliance/apps/projects/attachments/list)
* [Get project document content](/docs/en/api/compliance/apps/projects/documents/retrieve)

Project results are sorted by creation date ascending. Attachment results are sorted by `created_at` ascending, with ties broken by `id`. Project list and attachment list responses paginate with an opaque `next_page` page token instead of the `first_id`/`last_id` cursors used by chats and the Activity Feed. Pass the token back as the `page` query parameter on the next request.

### Project files versus project documents

A project attachment is one of two distinct shapes, identified by the `type` discriminator on each entry:

Entries with `type` of `project_file` are binary uploads (PDFs, images, spreadsheets) whose IDs start with `claude_file_`; download them with [Download file content](/docs/en/api/compliance/apps/chats/files/download). Entries with `type` of `project_doc` are plain-text documents (always `text/plain`) whose IDs start with `claude_proj_doc_`; fetch them with [Get project document content](/docs/en/api/compliance/apps/projects/documents/retrieve).

A consumer that walks the attachment list must branch on `type` and call the matching content endpoint for each entry. The following request lists one page of attachments; paginate by passing `next_page` back as the `page` parameter until `has_more` is `false`.

```bash cURL
project_id="claude_proj_01KGp4eZNug9ri4kE35RSppq"

curl --fail-with-body -sS -G \
  "https://api.anthropic.com/v1/compliance/apps/projects/$project_id/attachments" \
  --header "x-api-key: $ANTHROPIC_COMPLIANCE_ACCESS_KEY"
```

```json Response
{
  "data": [
    {
      "id": "claude_file_01UaT9wBcDfGhJkLmNpQrSv7",
      "created_at": "2026-04-10T08:09:10Z",
      "filename": "dashboard_mockup_v1.pdf",
      "mime_type": "application/pdf",
      "type": "project_file"
    },
    {
      "id": "claude_proj_doc_01YnT8sBcWvUtXzQpMkRfDgH",
      "created_at": "2026-04-10T08:09:11Z",
      "filename": "requirements.md",
      "mime_type": "text/plain",
      "type": "project_doc"
    }
  ],
  "has_more": false,
  "next_page": null
}
```

## Retrieve local sessions

Local sessions are Cowork and Claude Code sessions that run on a user's own machine while the user is signed in with their Claude Enterprise account: Cowork in Claude Desktop, and Claude Code in the terminal, in Claude Desktop, or in an IDE extension. Anthropic records each conversation server-side as its requests reach the Claude API; nothing is installed on the device, and nothing is collected beyond the requests the client already sends to the Claude API.

The Compliance API exposes local sessions through three endpoints: `GET /v1/compliance/apps/sessions/local` lists session metadata, `GET /v1/compliance/apps/sessions/local/{session_id}` retrieves one session's metadata, and `GET /v1/compliance/apps/sessions/local/{session_id}/messages` returns one session's transcript. All three require the `read:compliance_user_data` scope and count only against the shared Compliance API rate limit; they are not subject to the additional endpoint-specific limit that applies to the remote session endpoints. See [429 Too Many Requests](/docs/en/manage-claude/compliance-errors#429-too-many-requests). If local sessions are not available to your parent organization, all three endpoints return 404 with the message `Local sessions are not available.` (see [Local session not found](/docs/en/manage-claude/compliance-errors#local-session-not-found)); while session listings or captured content are temporarily unavailable, they return 503 (see [Local sessions temporarily unavailable](/docs/en/manage-claude/compliance-errors#local-sessions-temporarily-unavailable)).

<Note>
  The local session endpoints are in beta. They work with the same Compliance Access Key and `read:compliance_user_data` scope as the rest of the content endpoints; no new key, scope, setting, or client update is required.
</Note>

The following table summarizes how local sessions differ from the [remote sessions](#retrieve-remote-sessions) covered later on this page.

|                                         | Local sessions                                                                                            | Remote sessions                                                         |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Endpoints                               | List, retrieve, and messages endpoints under `/v1/compliance/apps/sessions/local`                         | List and messages endpoints under `/v1/compliance/apps/sessions/remote` |
| Where the session runs                  | The user's own machine                                                                                    | An Anthropic-managed cloud environment                                  |
| `product_surface` values                | `cowork`, `claude_code`                                                                                   | `cowork_remote`                                                         |
| ID prefix                               | `clls_`                                                                                                   | `cse_`                                                                  |
| List filters                            | `created_at` range only                                                                                   | Organization, user, and `created_at` range                              |
| Lifecycle fields                        | None: no `status` or `updated_at`                                                                         | `status`, `updated_at`                                                  |
| Retention                               | 6 years by default, or your organization's custom conversation retention period, when a finite one is set | 6 years                                                                 |
| Additional endpoint-specific rate limit | No                                                                                                        | Yes                                                                     |
| Deletion through the API                | No                                                                                                        | No                                                                      |

Local session transcripts show what Claude was asked to do and what it returned, not what happened on the device. File and network activity is visible only through the tool calls and tool results in the transcript, so activity that never reaches the API (for example, local files the session never sent) is not captured.

Capture is tied to the Compliance API being enabled for your organization and applies while the user is signed in with their Claude Enterprise account. Sessions are not captured when Claude Code authenticates with a Claude Console API key or runs through a third-party cloud platform such as Amazon Bedrock, Google Cloud, or Microsoft Foundry, and Claude Code on the web sessions are not captured. Claude Code on the web runs in Anthropic-managed cloud environments but is not a remote session either; the remote session endpoints return Cowork sessions only. For organizations with [HIPAA readiness](/docs/en/manage-claude/api-and-data-retention#hipaa-readiness) enabled, no local session data is captured, so these endpoints return no local sessions for those organizations. For organizations that use [customer-managed encryption keys](/docs/en/manage-claude/cmek), local sessions are listed and retrievable as usual, but transcript content is not currently returned: every message on the messages endpoint carries `provenance.type` of `content_unavailable` with `reason` of `not_captured` and an empty `content` array (see [Retrieve a local session transcript](#retrieve-a-local-session-transcript)).

The list endpoint returns session metadata, with no transcript content, for every linked organization your key can read. Unlike the remote session list, it has no organization or user filters: bound the results in time with the `created_at.gte` and `created_at.lt` parameters. Both take RFC 3339 timestamps with a required UTC offset, and when both are supplied, `created_at.lt` must be strictly after `created_at.gte` or the request returns [400 Bad Request](/docs/en/manage-claude/compliance-errors#400-bad-request). Sessions for which [zero data retention (ZDR)](/docs/en/manage-claude/api-and-data-retention#zero-data-retention-zdr-scope) is in effect are excluded. New sessions and messages appear in results after a short processing delay, typically within minutes; a session that is missing immediately after it starts is not necessarily uncaptured. The following request lists sessions created since a given date.

```bash cURL
curl --fail-with-body -sS -G \
  "https://api.anthropic.com/v1/compliance/apps/sessions/local" \
  --header "x-api-key: $ANTHROPIC_COMPLIANCE_ACCESS_KEY" \
  --data-urlencode "created_at.gte=2026-07-01T00:00:00Z" \
  --data-urlencode "limit=100"
```

```json Response
{
  "data": [
    {
      "type": "compliance_local_session",
      "id": "clls_01HxKpLmNoPqRsTuVwXyZaBc",
      "organization_uuid": "9a1e0000-0000-0000-0000-000000000000",
      "workspace_id": "wrkspc_01SvYKoWVRVHoEbwESNvzYdR",
      "user": {
        "id": "user_01GpKpLmNoPqRsTuVwXyZaBc",
        "email_address": "engineer@example.com"
      },
      "product_surface": "cowork",
      "created_at": "2026-07-09T14:02:11Z"
    },
    {
      "type": "compliance_local_session",
      "id": "clls_01HyLqMnOpQrStUvWxYzAbCd",
      "organization_uuid": "9a1e0000-0000-0000-0000-000000000000",
      "workspace_id": null,
      "user": {
        "id": "user_01HqRsTuVwXyZaBcDeFgHiJk",
        "email_address": null
      },
      "product_surface": "claude_code",
      "created_at": "2026-07-08T09:15:43Z"
    }
  ],
  "next_page": "page_AAEfQx7mPdLkq9Rt2VwHbZk"
}
```

Results are sorted in reverse chronological order (newest first) by `created_at`, with ties broken by `id`, and capped at `limit` results per response (default 100, max 500). The endpoint paginates forward only, with the same page-token scheme as projects and attachments (see [Paginate results](/docs/en/manage-claude/compliance-activity-feed#paginate-results)): pass the response's `next_page` value back as the `page` query parameter on the next request, and stop when `next_page` is `null`. The response has no `has_more` field. Complete a list walk within 24 hours of starting it; an older list cursor is still accepted but is re-evaluated against the current retention boundary, so sessions whose oldest retained activity is about to age out of the retention period can be skipped.

In each session object, `user.id` is always set and survives account deletion; `user.email_address` is `null` when the user's account has been deleted or the user is no longer a member of an organization your key can read. `workspace_id` is `null` when the session was not associated with a workspace. A local session corresponds to one client session ID: starting a new conversation in the client, or clearing its context, begins a new session record. Treat `id` values as opaque strings; the format may change without notice.

Local sessions carry no `status` and no `updated_at`: a local session has no server-side lifecycle, and its visibility is governed by retention instead. A local session is captured as the series of Claude API calls (inference calls) that the client makes during the session, and retention applies to each captured call individually. `created_at` is the timestamp of the session's earliest retained call (UTC). As older calls age past the retention period, `created_at` advances accordingly, and once every call in a session has aged out, the session is no longer returned. Because `created_at` can shift between runs, deduplicate on `id` when you re-walk the list over time. A session's `created_at` does not move later as the session continues, and there is no `updated_at`, so a session that gains messages after you first export it does not reappear in a later `created_at` window. To keep transcripts current, re-list a trailing window at least as long as your longest-running sessions on each run and re-fetch the transcripts of the sessions it returns, deduplicating messages on `id`.

The list is built from session activity metadata, so it can include sessions whose transcript content was not captured, for example sessions that ran before capture began for your organization (as far back as your retention period allows); every message in such a session's transcript carries `provenance.type` of `content_unavailable` with `reason` of `not_captured` (see [Retrieve a local session transcript](#retrieve-a-local-session-transcript)).

Captured local session content is stored for 6 years from capture by default. If the organization that ran the session has set a finite custom conversation retention period in [claude.ai > Organization settings > Data and privacy](https://claude.ai/admin-settings/data-privacy-controls), that period applies instead, whether it is shorter or longer than the default; when the organization has more than one custom retention period configured, the shortest applies. A change to that setting takes effect in two different ways: the endpoints stop returning activity older than the organization's current period as soon as the setting changes, whereas each captured message is stored for the period that was in effect when it was captured, so lengthening the period later does not restore content that has already expired.

To fetch one session's metadata directly, pass its ID to `GET /v1/compliance/apps/sessions/local/{session_id}`. The response is the same session object the list endpoint returns, with no envelope and no transcript content. A malformed session ID returns [400 Bad Request](/docs/en/manage-claude/compliance-errors#400-bad-request). A single [404 Not Found](/docs/en/manage-claude/compliance-errors#404-not-found) covers four cases that the response does not distinguish: the session is not in an organization your key can read (including sessions under another parent organization), it does not exist, zero data retention is in effect for it, or every call in it has aged past retention.

`product_surface` (string or `null`) identifies the product that created the session: `cowork` for Cowork sessions in Claude Desktop, and `claude_code` for Claude Code sessions. New values appear as coverage expands.

<Note>
  **Build forward-compatible handlers.** Pass through unrecognized `product_surface` values, and ignore fields your handler does not expect, so your integration keeps working as new product surfaces ship.
</Note>

### Retrieve a local session transcript

The messages endpoint returns the session's transcript, reconstructed from the captured Claude API calls: user prompts, assistant text, tool calls, and the text portions of tool results, all returned as they were sent apart from size truncation. Nothing masks URLs, credentials, or personal data in that content, so treat transcripts as sensitive. The transcript omits or replaces the following:

* Thinking blocks are never included.
* The request's system prompt is never returned. A marker message reading `[system prompt content not shown]` stands in for it (normally once per session; a session with no captured content carries no marker).
* Tool definitions and MCP server configuration are not part of the transcript.
* Images, PDFs, and other binary or structured blocks are not returned. Each appears as a `text` block reading `[<block type> content not shown]` (for example, `[image content not shown]`) with `truncated` set to `true`. Non-text items inside a tool result are replaced by one `[N non-text item(s) not shown]` entry, and the tool result block's `truncated` is `true`.
* Citation metadata on `text` blocks is omitted, and the affected block carries `truncated` set to `true`.

Project instruction files such as `CLAUDE.md` appear as ordinary user-role content. Skill content appears when the client sends it as message content and is not distinguished from other user text. For a coverage summary and a comparison with OpenTelemetry logging for Cowork and Claude Code, see the [Compliance API FAQ](/docs/en/manage-claude/compliance-faq#data-coverage-and-retention).

```bash cURL
session_id="clls_01HxKpLmNoPqRsTuVwXyZaBc"

curl --fail-with-body -sS \
  "https://api.anthropic.com/v1/compliance/apps/sessions/local/$session_id/messages" \
  --header "x-api-key: $ANTHROPIC_COMPLIANCE_ACCESS_KEY"
```

```json Response
{
  "session": {
    "type": "compliance_local_session",
    "id": "clls_01HxKpLmNoPqRsTuVwXyZaBc",
    "organization_uuid": "9a1e0000-0000-0000-0000-000000000000",
    "workspace_id": "wrkspc_01SvYKoWVRVHoEbwESNvzYdR",
    "user": {
      "id": "user_01GpKpLmNoPqRsTuVwXyZaBc",
      "email_address": null
    },
    "product_surface": "cowork",
    "created_at": "2026-07-09T14:02:11Z"
  },
  "data": [
    {
      "type": "compliance_local_session_message",
      "id": "clsm_01J4KpLmNoPqRsTuVwXyZaBa",
      "role": "user",
      "created_at": "2026-07-09T14:02:11Z",
      "provenance": {
        "type": "synthetic_marker"
      },
      "content": [
        {
          "type": "text",
          "text": "[system prompt content not shown]",
          "truncated": true
        }
      ]
    },
    {
      "type": "compliance_local_session_message",
      "id": "clsm_01J4KpLmNoPqRsTuVwXyZaBc",
      "role": "user",
      "created_at": "2026-07-09T14:02:11Z",
      "provenance": null,
      "content": [
        {
          "type": "text",
          "text": "Fix the failing test in tests/auth_test.py",
          "truncated": false
        }
      ]
    },
    {
      "type": "compliance_local_session_message",
      "id": "clsm_01J4KpLmNoPqRsTuVwXyZaBd",
      "role": "assistant",
      "created_at": "2026-07-09T14:02:11Z",
      "provenance": null,
      "content": [
        {
          "type": "text",
          "text": "I'll read the test file first.",
          "truncated": false
        },
        {
          "type": "tool_use",
          "id": "toolu_01AbCdEfGhIjKlMnOpQrSt",
          "name": "Read",
          "input": "{\"file_path\":\"tests/auth_test.py\"}",
          "truncated": false
        }
      ]
    },
    {
      "type": "compliance_local_session_message",
      "id": "clsm_01J4KpLmNoPqRsTuVwXyZaBe",
      "role": "user",
      "created_at": "2026-07-09T14:02:38Z",
      "provenance": null,
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01AbCdEfGhIjKlMnOpQrSt",
          "name": "Read",
          "is_error": false,
          "content": [
            {
              "type": "text",
              "text": "def test_login_expiry():\n    ..."
            }
          ],
          "truncated": false
        }
      ]
    },
    {
      "type": "compliance_local_session_message",
      "id": "clsm_01J4KpLmNoPqRsTuVwXyZaBf",
      "role": "assistant",
      "created_at": "2026-07-09T14:02:38Z",
      "provenance": null,
      "content": [
        {
          "type": "text",
          "text": "The test was asserting on a stale expiry timestamp. I've updated it.",
          "truncated": false
        }
      ]
    }
  ],
  "next_page": null
}
```

The response embeds a `session` envelope alongside the paginated `data` array. The first record in this example is the marker that stands in for the request's system prompt; its `provenance` is described later in this section. On this endpoint `user.email_address` is always `null`: the messages endpoint does not resolve email addresses, so a `null` here does not mean the user's account was deleted. To attribute a session to an email address, join `user.id` against the [list endpoint](#retrieve-local-sessions) or the retrieve endpoint (`GET /v1/compliance/apps/sessions/local/{session_id}`).

Messages are returned oldest first by default; pass `order=desc` to reverse. Pagination uses the same `page`/`next_page` scheme as the list endpoint, with a `limit` default of 100 and a max of 1,000. A page can end early when the response reaches its size limit, so a page with fewer than `limit` messages does not mean you have reached the end; keep paginating until `next_page` is `null`. Page cursors are bound to the session and sort order they were issued under, and a walk's cursors expire 24 hours after its first page: an expired cursor returns [400 Bad Request](/docs/en/manage-claude/compliance-errors#400-bad-request) telling you to restart without the `page` parameter, and the restarted walk reflects the current retention boundary. A cursor issued for a different session or `order` also returns 400, as an invalid cursor.

Each message carries a `role` (`user` or `assistant`) and a `content` array of `text`, `tool_use`, and `tool_result` blocks. A `text` block carries `text` and `truncated`. A `tool_use` block carries `id`, `name`, `input`, and `truncated`, where `input` is a JSON-encoded string rather than an object. A `tool_result` block carries `tool_use_id`, `name`, `is_error`, a `content` array of `text` entries, and `truncated`. MCP tool calls and results, and most server tool calls and results, are normalized into these same `tool_use` and `tool_result` shapes; any other block type appears as a `[<block type> content not shown]` placeholder. A message `id` is stable while the turn is retained. Every message reconstructed from the same inference call carries that call's timestamp, so consecutive messages often share a `created_at` value; preserve the returned order rather than re-sorting by timestamp.

Each message also carries a `provenance` field describing how its content was captured. `provenance` is `null` for verified content captured by the Claude API, which is the common case. Otherwise it is an object whose `type` marks the exception:

* `content_unavailable` means the content cannot be returned. The `content` array is empty, and `provenance.reason` states why. `not_captured` means no content is available for the turn; it does not prove that no record was stored, because content withheld by a storage-side access policy is reported with the same reason (for example, in organizations that use customer-managed encryption keys, as described in [Retrieve local sessions](#retrieve-local-sessions)), and individual turns within an otherwise captured session can be unavailable for other data-handling reasons and carry the same reason. `cmek_key_revoked` is reserved for content encrypted under your organization's customer-managed key when that key is unavailable (for example, revoked); it is not currently returned, so handle it for forward compatibility. `retention_elapsed` means the content aged past retention. `oversize` means a single message exceeded the per-message size bound; the message is still returned, with an empty `content` array.
* `client_asserted` marks assistant messages that the client supplied as conversation history and that could not be matched to a captured response; their authorship is not verified.
* `synthetic_marker` marks records generated by the endpoint itself, such as the marker that stands in for the system prompt. When the client rewrites or compacts its conversation history mid-session (for example, after context compaction), the transcript inserts a marker message at that point and continues with the new content the client sent; when your organization has a finite retention period, the rewritten history itself is withheld (a second marker notes this) and only the latest user turn and what follows are shown.

Marker and client-asserted messages begin with a bracketed explanatory `text` block flagged `truncated: true`, for example `[system prompt content not shown]`. Treat these records as present but unavailable or unverified rather than missing, and tolerate unrecognized `provenance` types and reasons.

Two parameters cap how many bytes of each tool block are returned: `tool_use_input_max_bytes` and `tool_result_max_bytes`, both defaulting to 10,000 bytes. Pass `-1` for the server maximum (about 1 MiB per string); `0` returns [400 Bad Request](/docs/en/manage-claude/compliance-errors#400-bad-request), and values above the maximum are clamped to it. A string cut off by either cap is cut on a character boundary and has an in-band suffix appended (for example, `…[truncated; pass tool_result_max_bytes=-1 for the server max]`), and its block carries `"truncated": true`. A truncated `tool_use` `input` is therefore no longer valid JSON, so parse tool inputs only from untruncated blocks (or raise the cap and refetch). Blocks of type `text` are always capped at the same server maximum of about 1 MiB; no parameter raises it, and a `text` block at the bound also carries `"truncated": true`.

Transcript content honors the retention period described in [Retrieve local sessions](#retrieve-local-sessions). When the start of a session has aged past it, the transcript begins with a single `content_unavailable` placeholder with `reason` of `retention_elapsed`, and the retained messages follow. When every call in a session has aged out, the messages endpoint returns [404 Not Found](/docs/en/manage-claude/compliance-errors#404-not-found), as it does for sessions in organizations your key cannot read, sessions that do not exist, and sessions for which zero data retention is in effect. A malformed session ID returns [400 Bad Request](/docs/en/manage-claude/compliance-errors#400-bad-request).

## Retrieve remote sessions

Cowork sessions started on claude.ai web or mobile run in Anthropic-managed cloud environments. The Compliance API exposes these remote sessions through two endpoints: `GET /v1/compliance/apps/sessions/remote` lists session metadata, and `GET /v1/compliance/apps/sessions/remote/{session_id}/messages` returns one session's transcript. Both require the `read:compliance_user_data` scope, and both count against the shared Compliance API rate limit plus a second budget specific to these endpoints; see [429 Too Many Requests](/docs/en/manage-claude/compliance-errors#429-too-many-requests).

<Note>
  The remote session endpoints are in beta. No additional setup is required: they work with the same Compliance Access Key and `read:compliance_user_data` scope as the rest of the content endpoints.
</Note>

The list endpoint defaults to organization-wide scope: leave off `organization_ids[]` to include every claude.ai organization your key can read, or pass up to 500 values to narrow the scope. To scope the list to specific users instead, pass 1–10 `user_ids[]` values (obtain the IDs from [List organization users](/docs/en/manage-claude/compliance-org-data#list-organization-users)); the filter matches the session's owning user, so agent-owned sessions are excluded whenever `user_ids[]` is set. Bound the results in time with `created_at` range parameters (`gte`, `gt`, `lt`, `lte`, in RFC 3339 format). There is no `updated_at` filter. The following request lists sessions created since a given date.

```bash cURL
curl --fail-with-body -sS -G \
  "https://api.anthropic.com/v1/compliance/apps/sessions/remote" \
  --header "x-api-key: $ANTHROPIC_COMPLIANCE_ACCESS_KEY" \
  --data-urlencode "created_at.gte=2026-06-01T00:00:00Z" \
  --data-urlencode "limit=100"
```

```json Response
{
  "data": [
    {
      "id": "cse_01WpQrStUvXyZaBcDeFgHjK6",
      "organization_uuid": "91012d09-e48b-438e-a489-1bebfd8fa6f9",
      "user": {
        "id": "user_01XyDMpzjS89pFZXqSFUBDr6",
        "email_address": "user@example.com"
      },
      "agent_id": null,
      "started_by_user": null,
      "status": "active",
      "created_at": "2026-07-01T17:04:05Z",
      "updated_at": "2026-07-01T18:00:41Z",
      "product_surface": "cowork_remote"
    },
    {
      "id": "cse_01TkNpRsUvWxYzAbCdEfGhJ4",
      "organization_uuid": "91012d09-e48b-438e-a489-1bebfd8fa6f9",
      "user": null,
      "agent_id": "cagt_01MnPqRsTuVwXyZaBcDeFgH8",
      "started_by_user": {
        "id": "user_01XyDMpzjS89pFZXqSFUBDr6",
        "email_address": "user@example.com"
      },
      "status": "archived",
      "created_at": "2026-06-28T09:15:22Z",
      "updated_at": "2026-06-28T09:47:10Z",
      "product_surface": "cowork_remote"
    }
  ],
  "next_page": "page_AAEfMk93cXpYdGxrZXk"
}
```

Results are sorted in reverse chronological order (newest first) by `created_at` and capped at `limit` results per response (default 100, max 500). The endpoint paginates with the same page-token scheme as projects and attachments (see [Paginate results](/docs/en/manage-claude/compliance-activity-feed#paginate-results)): pass the response's `next_page` value back as the `page` query parameter on the next request, and stop when `next_page` is `null`.

A session is owned by either a user or an agent, never both. For user-owned sessions, `user` carries the owner's ID and email address (`email_address` is `null` when the user is no longer a member of an organization your key can read) and `agent_id` is `null`. For agent-owned sessions (for example, scheduled tasks), `user` is `null`, `agent_id` carries the agent's ID (prefix `cagt_`), and `started_by_user` identifies the human who initiated the run, for example by starting a scheduled task; on user-owned sessions, `started_by_user` is `null`.

`status` is one of `pending`, `active`, `paused`, `archived`, or `failed`. A session is `pending` while it is being provisioned; a `pending` session has no transcript yet, and the messages endpoint returns 404 for it until provisioning completes. Sessions that have been deleted are never returned.

`product_surface` (string or `null`) identifies the product that created the session. The endpoint currently returns only sessions with `product_surface` of `cowork_remote`: Cowork sessions started on claude.ai web or mobile.

<Note>
  **Build forward-compatible handlers.** Pass through unrecognized `status` and `product_surface` values, and ignore fields your handler does not expect, so your integration keeps working as new statuses and product surfaces ship.
</Note>

### Retrieve a remote session transcript

The messages endpoint returns the session's transcript: user prompts, assistant responses, and tool calls and results. Thinking blocks and images are not included. For a coverage summary and a comparison with Cowork's OpenTelemetry logging, see the [Compliance API FAQ](/docs/en/manage-claude/compliance-faq#data-coverage-and-retention).

```bash cURL
session_id="cse_01WpQrStUvXyZaBcDeFgHjK6"

curl --fail-with-body -sS \
  "https://api.anthropic.com/v1/compliance/apps/sessions/remote/$session_id/messages" \
  --header "x-api-key: $ANTHROPIC_COMPLIANCE_ACCESS_KEY"
```

```json Response
{
  "session": {
    "id": "cse_01WpQrStUvXyZaBcDeFgHjK6",
    "organization_uuid": "91012d09-e48b-438e-a489-1bebfd8fa6f9",
    "user": {
      "id": "user_01XyDMpzjS89pFZXqSFUBDr6",
      "email_address": null
    },
    "agent_id": null,
    "started_by_user": null,
    "status": "active",
    "created_at": "2026-07-01T17:04:05Z",
    "updated_at": "2026-07-01T18:00:41Z",
    "product_surface": "cowork_remote"
  },
  "data": [
    {
      "id": "csev_01HjKmNpQrStUvWxYzAbCdE2",
      "role": "user",
      "created_at": "2026-07-01T17:04:05Z",
      "content": [
        {
          "type": "text",
          "text": "Summarize the customer feedback in the attached spreadsheet."
        }
      ],
      "sent_by_user_id": null,
      "content_unavailable": false
    },
    {
      "id": "csev_01BcDeFgHjKmNpQrStUvWxY4",
      "role": "assistant",
      "created_at": "2026-07-01T17:04:06Z",
      "content": [
        {
          "type": "text",
          "text": "I'll start by reading the spreadsheet..."
        }
      ],
      "sent_by_user_id": null,
      "content_unavailable": false
    }
  ],
  "next_page": null
}
```

The response embeds a `session` envelope alongside the paginated `data` array. On this endpoint the envelope always has `user.email_address` and `started_by_user` set to `null`; get those values from the list endpoint instead.

Messages are returned oldest first by default; pass `order=desc` to reverse. Pagination uses the same `page`/`next_page` scheme as the list endpoint, with a `limit` default of 100 and a max of 1,000. A page can end early when the response reaches its size budget, so a page with fewer than `limit` messages does not mean you have reached the end; keep paginating until `next_page` is `null`.

Each message carries a `role` (`user` or `assistant`) and a `content` array of `text`, `tool_use`, and `tool_result` blocks. Message `created_at` values are commit timestamps: consecutive messages can share a timestamp or slightly invert, so preserve the returned order rather than re-sorting by `created_at`. On agent-owned sessions, `sent_by_user_id` records the user who sent a given user message when one is attributable; it is `null` otherwise, including on all assistant messages. When a message's content cannot be returned at all (for example, it exceeds size bounds), the message carries `content_unavailable` set to `true`.

Two parameters cap how many bytes of each tool block are returned: `tool_use_input_max_bytes` and `tool_result_max_bytes`, both defaulting to 10,000 bytes. Pass `-1` for the server maximum (about 1 MiB); `0` is invalid. A block cut off by either cap carries `"truncated": true`, and a truncated `tool_use` input is no longer valid JSON, so parse tool inputs only from untruncated blocks (or raise the cap and refetch).

The messages endpoint returns [404 Not Found](/docs/en/manage-claude/compliance-errors#404-not-found) for `pending` sessions, deleted sessions, and sessions in organizations your key cannot read.

## Delete content

<Warning>
  Every successful delete is permanent and immediate. There is no recovery window.
</Warning>

The Compliance API exposes hard-delete endpoints for chats, files, project documents, and entire projects. A hard-deleted chat cannot be restored, and it stops appearing in list responses afterward (whereas a chat soft-deleted from claude.ai still appears with `deleted_at` populated).

* [Delete chat](/docs/en/api/compliance/apps/chats/delete): also removes the chat's messages and any files attached to those messages.
* [Delete file](/docs/en/api/compliance/apps/chats/files/delete): handles both chat files and project files.
* [Delete project document](/docs/en/api/compliance/apps/projects/documents/delete): removes a single project document by ID.
* [Delete project](/docs/en/api/compliance/apps/projects/delete): see [Detach chats before deleting a project](#detach-chats-before-deleting-a-project).

All four endpoints require the `delete:compliance_user_data` scope, which is granted separately from the read scope when the Compliance Access Key is created.

The session endpoints are read-only; local and remote sessions cannot be deleted through the Compliance API. Remote session transcripts are retained for 6 years, and local session transcripts for 6 years by default, or your organization's custom conversation retention period, when a finite one is set; see [Retrieve local sessions](#retrieve-local-sessions) and [API and data retention](/docs/en/manage-claude/api-and-data-retention).

The following request deletes one chat. The same pattern applies to the other delete endpoints; only the URL changes.

```bash cURL
# WARNING: This operation PERMANENTLY deletes the chat, all of its messages,
# and any attached files. Deletion is immediate and cannot be undone. It
# requires the `delete:compliance_user_data` scope, which is granted separately
# from `read:compliance_user_data` when the Compliance Access Key is created.
# Ensure you have explicit authorization before running this.

chat_id="claude_chat_01H5CWunD7RpVJ5bHa8RCkja"

curl --fail-with-body -sS -X DELETE \
  "https://api.anthropic.com/v1/compliance/apps/chats/$chat_id" \
  --header "x-api-key: $ANTHROPIC_COMPLIANCE_ACCESS_KEY"
```

```json Response
{
  "id": "claude_chat_01H5CWunD7RpVJ5bHa8RCkja",
  "type": "claude_chat_deleted"
}
```

Each successful delete returns a small confirmation envelope with an `id` and a `type` discriminator. The chat endpoint returns `claude_chat_deleted`; check the `type` field before treating the delete as confirmed. See the response schema on each delete endpoint's [API reference](/docs/en/api/compliance/apps) page for the exact `type` value the other endpoints return.

### Detach chats before deleting a project

A project cannot be deleted while any chats remain attached to it. The API returns 409 with this body:

```json
{
  "error": {
    "type": "conflict_error",
    "message": "The \"claude_proj_01KGp4eZNug9ri4kE35RSppq\" project cannot be deleted as it has chats attached to it. Delete or detach all chats, and try deleting the project again."
  }
}
```

To resolve, list the project's chats with `GET /v1/compliance/apps/chats?user_ids[]={user_id}&project_ids[]={project_id}` (the `project_ids[]` filter requires at least one `user_ids[]` value; enumerate IDs through [List organization users](/docs/en/manage-claude/compliance-org-data#list-organization-users)), delete each one with `DELETE /v1/compliance/apps/chats/{claude_chat_id}` (or move it out of the project from claude.ai), and then retry the project delete.

## Next steps

<CardGroup cols={2}>
  <Card title="API reference" href="/docs/en/api/compliance/apps">
    The full request and response schema for every chat, file, project, and artifact endpoint.
  </Card>

  <Card title="List organizations, users, roles, groups, and settings" href="/docs/en/manage-claude/compliance-org-data">
    Enumerate the people and teams associated with the chats, projects, and sessions on this page.
  </Card>
</CardGroup>
