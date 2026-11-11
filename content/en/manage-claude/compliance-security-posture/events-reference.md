---
title: Security posture events reference
url: https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/events-reference
description: "Look up the Activity Feed activities that record changes on the Security posture page: their fields and values, an example of each, and what the feed does not record."
---

<Note>
  To enable the Compliance API, see [Set up the Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api-access).
</Note>

The [Activity Feed](https://platform.claude.com/docs/en/manage-claude/compliance-activity-feed) records changes to attestations on the [Security posture](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/overview) page as the activities that this page describes. To ingest them into a security information and event management (SIEM) system, start at [Send Security posture events to your SIEM](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/send-events). Pass through any value of `control`, `action`, or another field that this page does not list, ignore unexpected fields, and treat a missing key and a `null` value alike. [Understand the Activity object](https://platform.claude.com/docs/en/manage-claude/compliance-activity-feed#understand-the-activity-object) covers the standard fields and unknown types.

You need a Compliance Access Key that covers the organization, with the `read:compliance_activities` or `read:org_audit` scope.

## Attestation activity

An `org_security_control_attestation_updated` activity records that someone recorded, changed, saved again, or cleared the organization’s attestation for a security control, or that the attestation ended automatically. Its `created_at` is the time of a person’s change or, for an automatic one, the time at which the change was recorded, which can be later than the change. Its `actor` is a `user_actor` for a person’s change and a `system_actor` for an automatic one, such as `lapsed`.

### Fields

This type adds the following fields, where `status` is the attestation’s value and `review_date` is its end date.

| Field             | Type   | Description                                                                                                                                                           |
| ----------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `control`         | string | The identifier of the security control that the attestation applies to, for example, `oauth_conditional_access`; treat it as an opaque string.                        |
| `action`          | string | What changed, as one of the [`action` values](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/events-reference#action-values).          |
| `status`          | string | The attestation’s value: Completed (`completed`), Accepted risk (`accepted_risk`), or attested as Failed (`control_failed`); absent when the attestation was cleared. |
| `previous_status` | string | The attestation’s value before this change, one of the same three; absent when `action` is `attested`.                                                                |
| `review_date`     | string | The UTC day (ISO 8601 date) on which the attestation is due to end; absent if it was saved with no end date or cleared.                                               |

On an information-only control, the value Reviewed is recorded as `completed`.

### `action` values

| `action`   | Meaning                                                                                                                                |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `attested` | An attestation was recorded for a control that had none.                                                                               |
| `changed`  | An attestation was saved again with another value or, where `status` equals `previous_status`, with the same value, as with `renewed`. |
| `renewed`  | An attestation was saved again with the same value.                                                                                    |
| `cleared`  | A person cleared an attestation.                                                                                                       |
| `lapsed`   | An attestation ended automatically, not by a person.                                                                                   |

On `renewed` and `lapsed` activities, `status` equals `previous_status`. A save with the same value after a `lapsed` activity is recorded as `renewed`, not `attested`.

### What a `lapsed` activity means

A `lapsed` activity means that the check result or the control’s current value differs from the one the attestation was saved against; the current value can change with no setting changed, for example when Anthropic rewords it. `status` is the value that ended: any of the three. An attestation of a manual control never gets a `lapsed` activity. The activity can come later than the change that caused it.

### Example

```json
{
  "id": "activity_01Hq7ZtYc4Vb2NmKx8RsPd3W",
  "type": "org_security_control_attestation_updated",
  "created_at": "2026-10-20T15:04:00.220114Z",
  "organization_id": "org_01JuY4bkwkH1x4PodBJaWmh2",
  "organization_uuid": "91012d09-e48b-438e-a489-1bebfd8fa6f9",
  "actor": {
    "type": "user_actor",
    "email_address": "jane.doe@example.com",
    "user_id": "user_01WxYzAbCdEfGhJkMnPqRsTu",
    "ip_address": "192.0.2.34",
    "user_agent": "Mozilla/5.0..."
  },
  "control": "directory_sync_enabled",
  "action": "attested",
  "status": "accepted_risk"
}
```

## What the feed does not record

Do not read the absence of an activity as a sign that nothing changed. For current results, see [Security posture results reference](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/results-reference); its endpoint can omit a control that an activity names.

* Changes from before the [Activity Feed](https://platform.claude.com/docs/en/manage-claude/compliance-activity-feed) began recording these activities for the organization, or while the Compliance API was off, never added later.
* Rarely, a change of any kind.
* Every end date that arrives: not all get an activity, so do not wait for one.
* Each time the Security posture page is turned off or on: do not rely on a [detection rule](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/detect-changes) to detect it.
* Comments saved with an attestation, or any mark that one exists. Changing a comment takes a new save, which the feed records like any other save with the same value (see [`action` values](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/events-reference#action-values)).
* Which kind of control an attestation is for: automatic, manual, or information-only.
* Every change that could end an attestation: not all get a `lapsed` activity.
