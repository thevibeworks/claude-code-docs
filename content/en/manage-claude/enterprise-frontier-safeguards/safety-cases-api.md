---
title: Safety Cases API
url: https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/safety-cases-api
description: List, read, and respond to Safety Cases over HTTP with the Compliance API.
---

The Safety Cases API serves Safety Cases over HTTP. It is in beta. You can select a [Case bucket](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/faq#glossary) for each workspace under **Safety Case and Transcript storage**. Without one, you get no Safety Cases for messages with a user profile. The API is part of the [Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api), and it’s available only on Claude Platform. To learn how your team reviews and responds to a Safety Case, see [Review Safety Cases](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases).

<Warning>
  Enterprise Frontier Safeguards is in beta. It’s available under your agreement with Anthropic, such as the Internal use only terms, [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms) and the [Service Specific Terms](https://www.anthropic.com/legal/service-specific-terms). Settings and behavior can change during the beta.
</Warning>

## Get access

To get access to the Safety Cases API:

1. **Turn on the Compliance API.** You must have it on for your organization. If it’s off, see [Set up the Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api-access#set-up-the-compliance-api) to turn it on.
2. **Create an Admin API key.** As an organization admin, create an [Admin API key](https://platform.claude.com/docs/en/manage-claude/admin-api-keys#create-a-key-for-a-claude-console-organization) in the Claude Console. There are no scopes to select. An Admin API key gets access to the Safety Cases API only if you create it while the API is available to your organization. An Admin API key that you created earlier never gains this access. If you turn the Compliance API off, the Safety Cases API refuses your key’s requests with a 400 error.

To test the key, [list your Safety Cases](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/safety-cases-api#poll) with it:

| Response | What it means and what to do |
| ----- | ----- |
| 200, even with an empty list | Your key can list Safety Cases. You get Safety Cases only for workspaces without Anthropic Human Review. |
| 401, 403, or 404 | Your key can’t list Safety Cases. Check that you sent the whole key, then create another Admin API key and try again. |
| 403 or 404 with the new key | The API isn’t available to your organization. |

Delete any Admin API keys that you don’t need.

The key reaches only its own organization’s Safety Cases and messages, even under a parent organization. It’s a full Admin API key. While the API is available to your organization, every Admin API key that you create gets this access. For that reason, limit who can create and hold these keys. A test organization’s keys don’t get this access.

The key gets all three of the following scopes:

| Scope | What it allows |
| ----- | ----- |
| `read:compliance_review_cases` | List and read Safety Cases and Safety Notices, which never hold a message’s prompt or response. |
| `read:compliance_review_items` | Read the prompt, response, and sender of a flagged message. |
| `write:compliance_review_cases` | Respond to a Safety Case. |

Other keys can also read this data:

* **Safety Cases and Safety Notices:** Where the API is available, keys with [`read:org_audit`](https://platform.claude.com/docs/en/manage-claude/admin-api-keys#choose-scopes-for-a-claude-enterprise-key) can read only their own organization’s Safety Cases and Safety Notices. They can do this only if that organization has a parent organization.
* **Flagged messages:** In some organizations, keys with `read:org_audit` can also read the flagged messages, and so can keys with `read:compliance_user_data`. Some of these keys reach the flagged messages of every organization under their parent organization.

Send the [`anthropic-version`](https://platform.claude.com/docs/en/api/versioning) header on every request. A request without it can return a 400 error. After a 429 or 503 error, retry the request later.

## Poll for Safety Cases

Check the Safety Cases API regularly for new Safety Cases, so that you can respond promptly.

On your first run, leave `updated_at[gte]` out. Then, store the largest `updated_at` you have read, and send it as `updated_at[gte]` on the next run:

```bash cURL
curl --fail-with-body -sS -G \
  "https://api.anthropic.com/v1/compliance/review/cases" \
  --data-urlencode "updated_at[gte]=2026-11-23T18:15:34Z" \
  -d "order_by=updated_at" \
  -d "order=asc" \
  -d "limit=100" \
  -H "x-api-key: $ANTHROPIC_ADMIN_KEY" \
  -H "anthropic-version: 2026-10-21"
```

```json Response
{
  "data": [
    {
      "type": "compliance_review_case",
      "id": "rvc_01Hq3Zt8KpWv5NcR2yLbXs7D",
      "organization_id": "abcdef01-2345-6789-abcd-ef0123456789",
      "status": { "type": "open" },
      "created_at": "2026-11-23T18:42:07.106255Z",
      "updated_at": "2026-11-23T18:42:07.106255Z",
      "workspace_id": "wrkspc_01AbCdEfGhJkLmNpQrStUvWx",
      "policy_categories": ["cyber"],
      "enforcement_action": null,
      "transcripts": [
        {
          "item_id": "msg_01XFDUDYJgAACzvnptvVoYEL",
          "user_profile_id": null
        }
      ]
    }
  ],
  "next_page": null
}
```

This request returns Safety Cases that opened, closed, or got a Safety Notice since that time. To read one Safety Case, send `GET /v1/compliance/review/cases/{case_id}`.

Follow these recommendations when you build a polling job:

* **Read every page.** To read the next page, send `next_page` as `page` until the request returns `next_page` as `null`. A page can be short or empty while `next_page` is set.
* **Don’t keep `next_page` between runs.** It works only within one list result, and the API refuses it with a 400 error if the filters or the order differ.
* **Update your copy of each Safety Case by `id`.** The API also returns Safety Cases slightly older than the time you send, and returns one again when it closes or gets a Safety Notice.
* **Filter on `updated_at`, not `created_at`.** A filter on `created_at` misses a Safety Case that closes or gets a Safety Notice after you first read it, and it can miss a new one.

A closed Safety Case has `status.type` set to `closed`, and `status.reason.type` says why:

| `status.reason.type` | What it means |
| ----- | ----- |
| `responded` | Anthropic has your response. |
| `window_ended` | Anthropic got no valid response within 7 calendar days of `created_at`. |
| `ended_by_anthropic` | Anthropic ended the Safety Case before that. |

Anthropic can add fields, `policy_categories` values, `enforcement_action` types, and close reasons, so accept the ones you don’t know.

### Poll for Safety Notices

A Safety Notice is a message from Anthropic about one or more of your Safety Cases or about your organization as a whole. It can ask for an answer by a set time. Its `kind.type` says what kind it is:

| `kind.type` | What it is |
| ----- | ----- |
| `response_requested` | A request to respond. To answer, [respond to the Safety Case](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/safety-cases-api#respond). |
| `warning` | A warning. |
| `question` | A question. To answer, contact your Anthropic account team. |

Anthropic can add other kinds, so accept the ones you don’t know. Don’t rely on a Safety Notice to remind you of an open Safety Case: one with no file in your Case bucket gets no automatic reminder.

To read Safety Notices, poll `GET /v1/compliance/review/notices`:

* **Send `created_at[gte]` and `order=asc`,** and store the largest `created_at` you have read. Safety Notices have no `updated_at` or `order_by`, and they never change.
* **Read every page,** as you do for Safety Cases.
* **Match Safety Notices by `id`,** because results can repeat.

A list of Safety Notices looks like this:

```json Response
{
  "data": [
    {
      "type": "compliance_review_notice",
      "id": "rvn_01Jt5Yw2MnQx8VbK4zRcHd6F",
      "organization_id": "abcdef01-2345-6789-abcd-ef0123456789",
      "case_ids": ["rvc_01Hq3Zt8KpWv5NcR2yLbXs7D"],
      "kind": { "type": "response_requested" },
      "created_at": "2026-11-27T18:00:00Z",
      "message": "Anthropic has found no valid response to the Case in case_ids. Review the Case and write your response file before the time in respond_by. If you wrote a valid response file in the last hour, ignore this notice.",
      "respond_by": "2026-11-30T18:42:07Z"
    }
  ],
  "next_page": null
}
```

`respond_by` is `null` if the Safety Notice has no deadline. A [Safety Notice file](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/safety-case-files#notice) has the same fields, without `type` and `organization_id`, and with `schema_version`.

### How the fields differ from the file

Anthropic can also write Safety Cases to a bucket in your own cloud account, as [Safety Case files](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/safety-case-files). The files are another way to read and respond to Safety Cases. The files use the API’s field names, with these differences:

| In the API | In the [Safety Case file](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/safety-case-files#safety-case-file) |
| ----- | ----- |
| `type`, `organization_id` | Not in the file |
| `transcripts[].user_profile_id` is `null` if there’s none or if the message is more than 28 days old | The key is left out if there’s none |
| Not in the API | `schema_version`, `transcripts[].object_key`, `derived_data_object_keys` |
| A closed Safety Case always has a `status.reason` | `status.reason` can be `null` |
| `updated_at` also changes when a Safety Notice names the Safety Case | `updated_at` changes only when Anthropic writes the file |
| Times with fractions of a second | Times in whole seconds. `created_at` can be slightly earlier. |

## Read a message

Fetch each `item_id` in `transcripts`. Whether you can read a message that you sent with a user profile depends on the key:

* **An Admin API key from the Claude Console** can’t read such a message. That request returns a 404 error. Anthropic writes the message’s [Transcript](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/safety-case-files#transcript) to the workspace’s Case bucket, if it has one.
* **Other keys** can read such a message in some organizations (see [Get access](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/safety-cases-api#get-access)). With such a key, send the user profile’s ID in the `anthropic-user-profile-id` header. For any other message, leave the header out. A wrong or missing ID returns a 404 error, and so does an ID on a message that you sent with no user profile.

```bash cURL
curl --fail-with-body -sS \
  "https://api.anthropic.com/v1/compliance/safeguards/items/msg_01XFDUDYJgAACzvnptvVoYEL" \
  -H "x-api-key: $ANTHROPIC_ADMIN_KEY" \
  -H "anthropic-version: 2026-10-21"
```

The response holds the message and the sender that Anthropic recorded:

```json Response
{
  "type": "compliance_safeguards_review_item",
  "id": "msg_01XFDUDYJgAACzvnptvVoYEL",
  "organization_uuid": "abcdef01-2345-6789-abcd-ef0123456789",
  "sampled_at": "2026-11-23T17:58:12.482913Z",
  "content_expires_at": "2026-12-21T17:58:12.482913Z",
  "product_surface": "api",
  "model": "claude-opus-5-5",
  "workspace_id": "wrkspc_01AbCdEfGhJkLmNpQrStUvWx",
  "api_key_id": null,
  "user": { "id": "user_01JkWm4Rt7YpXc2NvBq9sZdH", "email_address": "user@example.com" },
  "user_profile_id": null,
  "refs": {
    "batch_id": null,
    "local_session_id": null,
    "claude_chat_id": null,
    "claude_chat_message_id": null,
    "remote_session_id": null,
    "remote_session_event_id": null,
    "agent_session_id": null
  },
  "content": {
    "request": {
      "model": "claude-opus-5-5",
      "max_tokens": 1024,
      "messages": [{ "role": "user", "content": "Hello, Claude" }]
    },
    "response": {
      "id": "msg_01XFDUDYJgAACzvnptvVoYEL",
      "type": "message",
      "role": "assistant",
      "content": [{ "type": "text", "text": "Hello! How can I help you today?" }]
    }
  },
  "content_unavailable_reason": null
}
```

`content` holds the stored request and response. It’s not an exact copy: Anthropic cuts some URLs to their host, redacts MCP server tokens, removes thinking blocks, and can replace an image or a document with resized images or a placeholder.

Anthropic records one sender for each message:

| Sender | `user` | `api_key_id` |
| ----- | ----- | ----- |
| A [personal key](https://platform.claude.com/docs/en/manage-claude/authentication#key-types) or a user’s sign-in | The account’s ID and email address | `null` |
| A workspace key | `null` | The key’s ID |
| A service account, or no sender recorded | `null` | `null` |

`user` identifies the account, not the person who wrote the prompt. To find that person, use your own logs (see [Log message IDs](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases#log-message-ids)). `email_address` is always `null` in an organization with no parent organization, and it can be `null` in others.

A Safety Case can list a message that you can’t read. This table shows what the request can return:

| Result | What it means | What to do |
| ----- | ----- | ----- |
| A 404 error | For example, the message has expired or is no longer flagged. | A 404 error can be temporary, so try again later before you treat a message as unreadable. |
| A 404 error for every message | This happens if Anthropic hasn’t turned on message reads for your organization, or if your organization no longer has Anthropic’s approval to turn off Anthropic Human Review. | See [Reach out for help](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases#get-help). A 404 error can be temporary, so try again later before you treat a message as unreadable. |
| A 503 error | The error can be temporary. | Try again later before you treat a message as unreadable. |
| The message, with `content` set to `null` | Anthropic has no copy of the text. `content_unavailable_reason` is `not_captured` or `use_ref`, and Anthropic can add values. | With `use_ref`, `refs` can hold an ID that names the conversation. Read the conversation through the Compliance API endpoint for that ID, with a key that has access to it. |

Read and save each message as soon as the Safety Case arrives, and no later than `content_expires_at`. That time is at most 28 days after `sampled_at`, and an open Safety Case doesn’t extend it. A message can stop being readable before that time.

## Respond to a Safety Case

After you investigate a Safety Case, respond to tell Anthropic what you found. [Respond to a Safety Case](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases#respond-to-a-case) says what a response confirms, and [If you don’t respond](https://platform.claude.com/docs/en/manage-claude/enterprise-frontier-safeguards/flagged-cases#if-you-dont-respond) says what happens without one.

<Warning>
  A response closes the Safety Case, so you can’t change your response later.
</Warning>

Send one request within 7 calendar days of the Safety Case’s `created_at`:

```bash cURL
curl --fail-with-body -sS \
  "https://api.anthropic.com/v1/compliance/review/cases/rvc_01Hq3Zt8KpWv5NcR2yLbXs7D/respond" \
  -H "x-api-key: $ANTHROPIC_ADMIN_KEY" \
  -H "anthropic-version: 2026-10-21" \
  -H "content-type: application/json" \
  -d '{
    "determination": "violation",
    "policy_categories": ["cyber"]
  }'
```

`determination` is required, `policy_categories` is required with `violation`, and `verdicts` is optional:

| Field | What to send |
| ----- | ----- |
| `determination` | `violation` or `no_violation`, for the Safety Case as a whole |
| `policy_categories` | With `violation`, one to four categories that you confirmed, such as `cyber`, or `other` if none fits. `benign` and `undetermined` return a 400 error. With `no_violation`, leave it out or send an empty list. |
| `verdicts` | To judge messages separately, a list with an `item_id`, a `determination`, and a `policy_category` (a category or `null`, and always `null` with `no_violation`) for each. |

A 200 response returns the closed Safety Case, with `status.reason.type` set to `responded`. That confirms that Anthropic has received your response.

Anthropic counts the first response, whether it arrives through the API or as a file:

| What you send next | What the API returns |
| ----- | ----- |
| The same response again | A 200 response. Nothing changes, so it’s safe to retry. |
| Any other valid response to a closed Safety Case | A 400 error with `error.details.error_code` set to `case_closed`. |
