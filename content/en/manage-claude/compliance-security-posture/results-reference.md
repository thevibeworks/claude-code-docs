---
title: Security posture results reference
url: https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/results-reference
description: "Look up the Compliance API endpoint that returns an organization's current Security posture results: the request, the response fields, what each status means, and the errors."
---

<Note>
  To enable the Compliance API, see [Set up the Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api-access).
</Note>

This endpoint returns an entry for most of an organization’s security controls, evaluated at the time of the request, with the [Security posture attestation](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/overview#attestations) that the response shows for each control. You need a Compliance Access Key that covers the organization, with the `read:compliance_org_data` or `read:org_audit` scope; [Security posture availability](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/overview#availability) says which organizations can be read.

## Request

Send a `GET` request to `/v1/compliance/organizations/{organization_id}/security_posture`. Each call reads one organization, and the response is not paginated.

```bash cURL
curl --fail-with-body -sS \
  "https://api.anthropic.com/v1/compliance/organizations/91012d09-e48b-438e-a489-1bebfd8fa6f9/security_posture" \
  -H "x-api-key: $ANTHROPIC_COMPLIANCE_ACCESS_KEY" \
  -H "anthropic-version: 2026-10-21"
```

| Item                | Rule                                                                                                                                                                                                                                                                                   |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `organization_id`   | The `uuid` of a [linked organization](https://platform.claude.com/docs/en/manage-claude/compliance-api#how-the-compliance-api-works) from [List organizations](https://platform.claude.com/docs/en/manage-claude/compliance-org-data#list-organizations); any other value returns 404. |
| Key                 | A [key for the parent organization](https://platform.claude.com/docs/en/manage-claude/compliance-api-access#set-up-the-compliance-api) can name any linked organization, and a key for a single organization can name only that organization.                                          |
| `anthropic-version` | Required; a request without it returns 400.                                                                                                                                                                                                                                            |
| Query parameters    | None; a request with any query parameter returns 400.                                                                                                                                                                                                                                  |

## Response

The following abridged example shows four of the controls that a response can contain. It is the response to a key that holds `read:compliance_org_data` and `read:compliance_user_data`.

```json Response
{
  "type": "security_posture",
  "organization_id": "91012d09-e48b-438e-a489-1bebfd8fa6f9",
  "evaluated_at": "2027-02-09T09:00:02.417305Z",
  "comments_status": "not_enabled",
  "controls": [
    {
      "id": "sso_enabled",
      "display_name": "Single sign-on (SSO)",
      "section": "identity_access",
      "setting_name": "sso_enabled",
      "status": "passed",
      "rating": "passed",
      "current_value": "On",
      "desired_state": "On",
      "attestation": null
    },
    {
      "id": "directory_sync_enabled",
      "display_name": "Directory sync (SCIM)",
      "section": "identity_access",
      "setting_name": "directory_sync_enabled",
      "status": "failed_check_accepted_risk",
      "rating": "passed",
      "current_value": "Off",
      "desired_state": "On",
      "attestation": {
        "state": "in_force",
        "attested_at": "2026-10-20T15:04:00.220114Z",
        "comment": null,
        "attested_by": {
          "type": "user_actor",
          "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu"
        }
      }
    },
    {
      "id": "allowed_invite_domains",
      "display_name": "Allowed email domains",
      "section": "identity_access",
      "setting_name": "allowed_invite_domains",
      "status": "descriptive",
      "rating": "descriptive",
      "current_value": "example.com",
      "desired_state": null,
      "attestation": null
    },
    {
      "id": "oauth_conditional_access",
      "display_name": "OAuth conditional access on connected SaaS",
      "section": "connectors_integrations",
      "setting_name": null,
      "status": "not_attested",
      "rating": "not_attested",
      "current_value": null,
      "desired_state": "Completed",
      "attestation": {
        "state": "review_due",
        "attested_at": "2026-11-02T09:30:00.008771Z",
        "comment": null,
        "attested_by": {
          "type": "user_actor",
          "user_id": "user_01AbCdEfGhJkLmNpQrStUvWx"
        }
      }
    }
  ]
}
```

Every field is always present, and a field with no value is `null`, never left out. A time has either no fractional digits or six, so compare times as times, not as strings.

### Top-level fields

| Field             | Type                   | Description                                                                                                                                                                                          |
| ----------------- | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`            | string                 | Always `security_posture`.                                                                                                                                                                           |
| `organization_id` | string                 | The organization’s UUID.                                                                                                                                                                             |
| `evaluated_at`    | string (RFC 3339, UTC) | The time at which every control was evaluated.                                                                                                                                                       |
| `comments_status` | string                 | Whether attestation comments were read; see [Who attested, and comments](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/results-reference#who-attested-and-comments). |
| `controls`        | array of objects       | The organization’s controls, never empty.                                                                                                                                                            |

### `controls[]` fields

| Field           | Type           | Description                                                                                                                                                                                                                                                                                                            |
| --------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`            | string         | The control’s identifier, which is the same for every organization and never changes.                                                                                                                                                                                                                                  |
| `display_name`  | string         | The control’s display name, as English display text whose wording can change.                                                                                                                                                                                                                                          |
| `section`       | string         | The section that the control belongs to, one of the ten listed after this table; more values can be added, so treat an unknown one as a section of its own.                                                                                                                                                            |
| `setting_name`  | string or null | The `name` of the entry in the organization’s effective settings that this control reads; `null` when it reads no such entry.                                                                                                                                                                                          |
| `status`        | string         | The reason for the control’s result; see [Status values](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/results-reference#status-values).                                                                                                                                               |
| `rating`        | string         | The control’s result, which follows from `status`; see [Status values](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/results-reference#status-values).                                                                                                                                 |
| `current_value` | string or null | The current value, as English display text whose wording can change; `null` on a manual control or when no value was read.                                                                                                                                                                                             |
| `desired_state` | string or null | The recommended value, as English display text whose wording can change; `null` when there is none for this organization.                                                                                                                                                                                              |
| `attestation`   | object or null | The attestation that the response shows, also while it is not in effect; `null` while `status` is `descriptive`, `not_applicable`, or `not_evaluated`, and in [these cases](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/results-reference#how-an-attestation-shows-in-the-response). |

`section` is one of `identity_access`, `data_privacy`, `capabilities`, `connectors_integrations`, `chats_desktop_mdm`, `cowork_admin_console`, `cowork_desktop_mdm`, `claude_code_admin_console`, `claude_code_managed_settings`, and `healthy_adoption`.

To compare values in code, look up `setting_name` in the [effective settings](https://platform.claude.com/docs/en/manage-claude/compliance-org-data#get-effective-organization-settings) of the same organization. The lookup can find nothing, and two controls can share one `setting_name`.

### `attestation` fields

| Field         | Type                   | Description                                                                                                                                                                                                                                           |
| ------------- | ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `state`       | string                 | Whether the attestation is in effect; see [Attestation states](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/results-reference#attestation-states).                                                                   |
| `attested_at` | string (RFC 3339, UTC) | When the attestation was made.                                                                                                                                                                                                                        |
| `comment`     | string or null         | The comment saved with the attestation, of at most 2,000 characters; `null` if there is none or if `comments_status` is not `available`.                                                                                                              |
| `attested_by` | object or null         | The person who attested; `null` when the key holds neither `read:compliance_user_data` nor `read:org_audit`, when that person’s account has been deleted or is being deleted, or when the endpoint does not return who attested for the organization. |

### `attested_by` fields

| Field     | Type   | Description                               |
| --------- | ------ | ----------------------------------------- |
| `type`    | string | Always `user_actor`.                      |
| `user_id` | string | The user’s ID, which starts with `user_`. |

## Status values

`status` gives the reason for a control’s result, and each status has one `rating`.

| `status`                     | Kind of control     | Meaning                                                                                                                  | `rating`       | On the page                                              |
| ---------------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------ | -------------- | -------------------------------------------------------- |
| `passed`                     | automatic           | The current value meets the recommended value.                                                                           | `passed`       | Passed                                                   |
| `matches_profile`            | automatic           | The current value equals the recommended value.                                                                          | `passed`       | Passed                                                   |
| `exceeds_baseline`           | automatic           | The current value is stricter than the recommended value.                                                                | `passed`       | Passed                                                   |
| `failed_check_accepted_risk` | automatic           | The automatic check fails, and an accepted risk is in effect.                                                            | `passed`       | Passed                                                   |
| `failed`                     | automatic or manual | The current value does not meet the recommended value, or an attestation that the response leaves out gives this result. | `failed`       | Failed, or Passed with a Completed attestation in effect |
| `review`                     | automatic           | The current value is looser than the recommended value.                                                                  | `failed`       | Failed                                                   |
| `attested_completed`         | manual              | An attestation with the value Completed (`completed`) is in effect.                                                      | `passed`       | Passed                                                   |
| `attested_accepted_risk`     | manual              | An attestation with the value Accepted risk (`accepted_risk`) is in effect.                                              | `passed`       | Passed                                                   |
| `not_attested`               | manual              | No attestation is in effect.                                                                                             | `not_attested` | Not attested                                             |
| `attestation_not_enabled`    | manual              | Nobody can attest to the control.                                                                                        | `not_attested` | Descriptive                                              |
| `descriptive`                | information-only    | The control is reported, not rated.                                                                                      | `descriptive`  | Descriptive                                              |
| `not_applicable`             | any                 | The control does not apply to the organization.                                                                          | `descriptive`  | Descriptive                                              |
| `not_evaluated`              | any                 | The setting, or another setting that decides whether the control applies, could not be read.                             | `descriptive`  | Descriptive                                              |

No field names the kind of control; for `failed`, a `null` `current_value` marks a manual control. More values can be added, so count a control with an unknown `status` by its `rating` and read an unknown `rating` as not Passed. The status `review` and the attestation state `review_due` are not related.

## Attestation states

`state` says whether the attestation that the response shows is in effect.

| `state`           | Meaning                                                                                                                    |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `in_force`        | The attestation is in effect.                                                                                              |
| `review_due`      | The end date has come.                                                                                                     |
| `setting_changed` | The check fails on a value other than the one whose risk was accepted, or the accepted risk was already recorded as ended. |
| `check_passing`   | The check passes, so there is no risk to accept.                                                                           |

When more than one reason applies, the response gives the first of `check_passing`, `setting_changed`, and `review_due`. From 00:00 UTC on its end date, an attestation is not in effect. The response has no end date, so `state` decides; an end date that was saved is the attestation activity’s [`review_date`](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/events-reference#attestation-activity). Read an unknown `state` as not in effect.

## How an attestation shows in the response

The response shows some attestations and leaves others out, so a `null` `attestation` does not prove that nobody attested.

| Kind of control                             | Attested as                            | `status`                                                             | `rating`               | `attestation`                                       |
| ------------------------------------------- | -------------------------------------- | -------------------------------------------------------------------- | ---------------------- | --------------------------------------------------- |
| Manual                                      | No attestation                         | `not_attested`, or `attestation_not_enabled` where nobody can attest | `not_attested`         | `null`                                              |
| Manual                                      | Completed                              | `attested_completed`                                                 | `passed`               | Shown                                               |
| Manual                                      | Accepted risk                          | `attested_accepted_risk`                                             | `passed`               | Shown                                               |
| Manual                                      | Failed (`control_failed`)              | `failed`                                                             | `failed`               | `null`: never shown                                 |
| Automatic, check failed                     | No attestation                         | `failed` or `review`                                                 | `failed`               | `null`                                              |
| Automatic, check failed                     | Accepted risk                          | `failed_check_accepted_risk`                                         | `passed`               | Shown                                               |
| Automatic, check failed                     | Completed                              | `failed`, even where the automatic check gives `review`              | `failed`               | `null`: never shown                                 |
| Automatic, check failed                     | Failed                                 | The `status` the automatic check gives                               | `failed`               | `null`: never shown                                 |
| Automatic, check passed                     | No attestation                         | `passed`, `matches_profile`, or `exceeds_baseline`                   | `passed`               | `null`                                              |
| Automatic, check passed                     | Completed                              | The `status` the automatic check gives                               | `passed`               | `null`: never shown                                 |
| Automatic, check passed                     | Accepted risk                          | The `status` the automatic check gives                               | `passed`               | `null` while the check passes on the accepted value |
| Automatic, check passed                     | Failed                                 | `failed`                                                             | `failed`               | `null`: never shown                                 |
| Information-only                            | Any value                              | `descriptive`                                                        | `descriptive`          | `null`: never shown                                 |
| Any, while the attestation is not in effect | A value that an earlier row shows      | As with no attestation                                               | As with no attestation | Shown, with a `state` other than `in_force`         |
| Any, while the attestation is not in effect | A value that an earlier row leaves out | As with no attestation                                               | As with no attestation | `null`                                              |

Each row but the last two holds while the attestation is in effect. On an automatic control, an attestation is not in effect while the value that the check reads differs from the one that it was saved on. Every attestation that the response shows on an automatic control is an accepted risk. The [Activity Feed](https://platform.claude.com/docs/en/manage-claude/compliance-activity-feed) also records attestations of the kinds that the response leaves out.

## Count results

Check four things when you count controls by `rating`.

| If you count                | Also check                                                                                                                                                                         |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Passed (`passed`)           | It includes every control with an accepted risk in effect, so look for `failed_check_accepted_risk` and `attested_accepted_risk`.                                                  |
| Failed (`failed`)           | It includes a control attested as Failed (`control_failed`) and a failing automatic check with a Completed attestation in effect, which the Security posture page shows as Passed. |
| Descriptive (`descriptive`) | It can hide a control that could not be read, so look for `not_evaluated`.                                                                                                         |
| Every control               | A control missing from the response is not Passed and is not named, so compare `id` values with those that you have seen for the organization.                                     |

## Who attested, and comments

`attested_by` is filled only for a key that holds `read:compliance_user_data` together with `read:compliance_org_data` or that holds `read:org_audit`. A key with only `read:compliance_user_data` gets a 403. The `user_id` in `attested_by` is the same as the `actor`’s `user_id` on the attestation activity. `attested_by` holds only the user ID: [List organization users](https://platform.claude.com/docs/en/manage-claude/compliance-org-data#list-organization-users) gives the name and email address of each current member. Before you add these scopes, see [Who can see who attested](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/overview#who-can-see-who-attested).

The endpoint returns no comments, even when the Security posture page shows one: every `comment` is `null`, and `comments_status` is `not_enabled` or `not_permitted`. So `not_enabled` and a `null` comment do not mean the attestation has no comment. `comments_status` says how to read a `null` comment, and the schema defines these values.

| `comments_status`           | Meaning                                                                                                                                           |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `not_permitted`             | The API key holds neither `read:compliance_user_data` nor `read:org_audit`, so every `comment` and every `attested_by` is `null`.                 |
| `requires_organization_key` | The API key was not created in the organization, as with a key for the parent organization, so every `comment` is `null`. Retrying does not help. |
| `available`                 | Comments were read, so a `null` comment means that there is none or that it was saved moments ago.                                                |
| `not_enabled`               | This endpoint does not return comments for the organization, so every `comment` is `null`.                                                        |
| `unavailable`               | Comments could not be read for this response; a later request might succeed, but some causes last until the customer acts.                        |

More values can be added; read an unknown one as `unavailable`.

## Errors

Errors use the same body as the rest of the [Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-errors); this table lists the ones that this endpoint returns in its own way.

| Status and `error.type`                                                                | When                                                                                                                                     | What to do                                                                                                                                      |
| -------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| 400 `invalid_request_error`                                                            | `anthropic-version` is missing or invalid, the Compliance API is not enabled for the parent organization, or there is a query parameter. | Fix what `error.message` names.                                                                                                                 |
| 401 `authentication_error`                                                             | The key is missing, not recognized, or not a Compliance Access Key or Admin API key.                                                     | Send a valid Compliance Access Key in `x-api-key`.                                                                                              |
| 403 `permission_error`                                                                 | The key may not call this endpoint, usually because it lacks both `read:compliance_org_data` and `read:org_audit`.                       | Use a key with either scope.                                                                                                                    |
| 404 `not_found_error`                                                                  | See the causes listed after this table.                                                                                                  | Do not retry at once and never read it as no failed controls.                                                                                   |
| 429 `rate_limit_error`                                                                 | The shared Compliance API rate limit, or this endpoint’s lower limit, is used up; `error.message` says which.                            | Wait for `retry-after`; see [429 Too Many Requests](https://platform.claude.com/docs/en/manage-claude/compliance-errors#429-too-many-requests). |
| 503 `overloaded_error`, with `error.details.error_code` of `posture_evaluation_failed` | The result could not be produced.                                                                                                        | Wait for `retry-after`, then retry; if it recurs for one organization on later runs, contact Anthropic support once.                            |
| 503 with no `error_code`, or 504 `timeout_error`                                       | A temporary failure.                                                                                                                     | Retry with exponential backoff.                                                                                                                 |

Causes of a 404:

* `organization_id` is not a UUID, names no organization, or names a deleted one.
* `organization_id` names the parent organization, an organization under another parent, or one that a single-organization key does not cover.
* The organization is not on Claude Enterprise, or Security posture is not available to it, as with a Claude Console organization.
* The Security posture page has been turned off for the organization (see [Security posture availability](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/overview#availability)).
* Security posture is available to the organization, but the endpoint does not serve it.
* Availability could not be checked; a later request can succeed.

Every 404 has the same body, as does a path that does not exist.

## Freshness and side effects

The endpoint evaluates every control when you call it, and `evaluated_at` is that time.

* A change from the last few minutes might not show.
* A result can change with no setting changed, for example when an end date comes or Anthropic changes a recommended value.
* If Anthropic rewords a current value, an accepted risk on it is not in effect.
* A call stores no result and ends no attestation.
* Each request that passes the key, scope, and version checks without a query parameter records one `compliance_api_accessed` activity, whether it succeeds or fails; its `url` names the organization read, and `organization_uuid` is `null` for a key for the parent organization.
