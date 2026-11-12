---
title: Security posture in the Compliance API
url: https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/overview
description: Understand what the Compliance API exposes about the Security posture page (Security Center) in claude.ai and where to start.
---

<Note>
  To enable the Compliance API, see [Set up the Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api-access).
</Note>

The **Security posture** page in claude.ai **Organization settings** compares your organization’s Claude settings with Anthropic’s recommended security controls. Through the Compliance API, your security tools can read the changes that the page records. They can also read current results. Security posture reports on your settings and does not change them. The sidebar item is **Security posture**, and the page it opens is headed **Security Center**.

## Choose your path

To get changes on the page into your security information and event management (SIEM) system, start with [Send Security posture events to your SIEM](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/send-events). If you already ingest the whole Activity Feed, you have them; check two things in the [If you already ingest the full feed](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/send-events#if-you-already-ingest-the-full-feed) section.

* To alert on risky changes, see [Detect changes in Security posture](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/detect-changes).
* To normalize to the Open Cybersecurity Schema Framework (OCSF), see [Map Security posture events to OCSF](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/ocsf-mapping).
* To find who accepted which risk, when, and until when, see [Security posture events reference](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/events-reference); for risks in effect, see [Current results](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/overview#current-results).

To work with current results from the endpoint, use these pages:

* For dashboards, see [Security posture results reference](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/results-reference).
* To verify stored events, see [Check stored Security posture events against current results](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/check-events-against-results).
* If the endpoint and the page disagree, see [How an attestation shows in the response](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/results-reference#how-an-attestation-shows-in-the-response).

To understand the data, read on.

## What Security posture evaluates

Security posture evaluates a list of controls and gives each one a result.

### Controls

A control is one recommended setting or practice, such as single sign-on. Each control has a display name and an identifier. The identifier is the same for every organization. A control can also have a current value (`current_value`) and a recommended value (`desired_state`). Controls come in three kinds:

| Kind                     | What decides its result                                                                                     | Example                    |
| ------------------------ | ----------------------------------------------------------------------------------------------------------- | -------------------------- |
| Automatic control        | An automatic check of the current value against the recommended value, unless an attestation is in effect.  | `sso_enabled`              |
| Manual control           | A person, because Anthropic cannot read the setting, for example when it lives in another vendor’s console. | `oauth_conditional_access` |
| Information-only control | Nothing: there is no recommended value, so the control is reported and not rated.                           | `allowed_invite_domains`   |

### Attestations

An attestation is a person’s recorded statement of how the organization stands on a control; it is not the result of a check. Most controls can carry an attestation, automatic ones included, whatever their check’s result. An attestation has one of three values:

* Completed (`completed`): the control is in place.
* Accepted risk (`accepted_risk`): the control is not in place, and the organization accepts the risk.
* Failed (`control_failed`): the control is not in place.

Someone who can attest does so on the page. The API reads attestations and cannot make them. The page can ask a question when someone attests, sometimes requiring an answer, and stores the answer with the attestation as its [comment](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/overview#what-anthropic-stores-when-someone-attests), up to 2,000 characters. An Activity Feed activity never includes the comment or shows that one exists. The endpoint returns no comments either.

### Results

Each control has one of four results.

| Result                        | Meaning                                                                                                                 |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Passed (`passed`)             | Meets the recommended value, or an attestation of Completed or Accepted risk is in effect.                              |
| Failed (`failed`)             | Does not meet the recommended value or is attested as Failed (`control_failed`).                                        |
| Not attested (`not_attested`) | A manual control with no attestation in effect.                                                                         |
| Descriptive (`descriptive`)   | Not rated, even when attested; it covers information-only controls and controls that do not apply or could not be read. |

An accepted risk in effect counts as Passed on an automatic or manual control, though the control is not in place. In the response, an automatic control [attested as Completed while its check fails](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/results-reference#how-an-attestation-shows-in-the-response) is `failed`.

### What ends an attestation

An attestation stays in effect until one of three things happens:

* Someone clears or changes it.
* Its end date (`review_date`) arrives. The person who attests picks 90 days or none.
* On an automatic or information-only control, the current value changes, or, for an accepted risk on some automatic controls, the check passes.

Without an attestation in effect, an automatic control’s result follows its check, and a manual control is Not attested.

## Changes over time: the Activity Feed

The Activity Feed answers what changed, when, and who changed it. It records an activity when someone attests to a control, changes an attestation, or clears one, and sometimes when one ends automatically.

These pages’ titles call the activities events. Reading them takes the `read:compliance_activities` or `read:org_audit` scope. [Security posture events reference](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/events-reference) lists their fields. To collect them, see [Send Security posture events to your SIEM](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/send-events).

## Current results: the endpoint

The endpoint answers what a control’s result is at the time of the request. Use it to report across the organizations under your [parent organization](https://platform.claude.com/docs/en/manage-claude/compliance-api#how-the-compliance-api-works). Each call reads one organization and returns no history. For each control it lists, the response gives its `id`, `display_name`, and result in `rating`, using the identifiers in the [results table](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/overview#results).

Calling it takes the `read:compliance_org_data` or `read:org_audit` scope.

The page, the endpoint, and the feed do not always show the same thing, because the response leaves out some controls and some attestations. See [How an attestation shows in the response](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/results-reference#how-an-attestation-shows-in-the-response) and [Check stored Security posture events against current results](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/check-events-against-results).

## Availability

Security posture is in beta.

**If your organization is on Claude Enterprise, Security posture is available to it, and its parent organization has the Compliance API enabled,** the Activity Feed records attestation activities for it, and the endpoint returns your organization’s results.

You also need a Compliance Access Key with the matching scope. These pages assume you have read [Set up the Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api-access) and [Query the Activity Feed](https://platform.claude.com/docs/en/manage-claude/compliance-activity-feed).

**If your organization is on another plan or is a Claude Console organization,** the Activity Feed records no Security posture activities for it, and the endpoint returns 404.

**If the Security posture page has been turned off for your organization,** the endpoint returns 404 for your organization until the page is turned on. Even a key for the parent organization gets that 404.

For some organizations, the endpoint returns 404 even when all three conditions hold and the page has not been turned off.

## Who can see who attested

Each attestation activity that a person caused records their user ID, their email address at the time, and the request’s IP address and user agent. Any key that covers the organization and holds `read:compliance_activities` or `read:org_audit` can read them, even after they leave the organization or their account is deleted. Deleting the organization does not remove these activities from the Activity Feed, which retains activities for 6 years. The organization’s own keys stop working when it is deleted.

Any key with both `read:compliance_org_data` and `read:compliance_user_data`, or `read:org_audit`, can read, in the endpoint’s `attested_by`, the user ID of the person who attested, where the endpoint returns it, even for attestations made before you had access.

These values are personal data; your copies outlive the person’s membership. Before you collect this data, tell the people who attest.

## What Anthropic stores when someone attests

Anthropic stores one attestation per control, including the value, when it was made, any end date, and the account of the person who attested. Attesting again replaces it.

Anthropic keeps storing an attestation after its end date arrives or it [ends automatically](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/overview#what-ends-an-attestation), until someone clears it or Anthropic deletes it with the organization. If the account of the person who attested is deleted, Anthropic keeps storing the attestation, which no longer says who attested. Any Activity Feed activities that this person caused still name them. Clearing or replacing the attestation removes nothing from the Activity Feed (see [Who can see who attested](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/overview#who-can-see-who-attested)).

[Customer-managed encryption keys (CMEK)](https://platform.claude.com/docs/en/manage-claude/cmek), [zero data retention (ZDR) for Claude Code](https://code.claude.com/docs/en/zero-data-retention), and a [HIPAA-ready Enterprise plan](https://support.claude.com/en/articles/13296973-hipaa-ready-enterprise-plans) do not change what Anthropic stores of an attestation’s control, value, dates, and account. None of the three shortens how long Anthropic stores them. CMEK does not encrypt these fields.

An attestation’s comment is the answer to the question that the Security posture page can ask when someone attests. Anthropic stores an attestation’s comment until someone clears the attestation or Anthropic deletes the comment with the organization. Attesting again can replace or remove the comment. A custom conversation retention period does not shorten how long Anthropic stores the attestation or the comment. Activity Feed activities never include the comment (see [What the feed does not record](https://platform.claude.com/docs/en/manage-claude/compliance-security-posture/events-reference#what-the-feed-does-not-record)).

Some organizations cannot save a comment with an attestation because of their data-handling settings, such as CMEK or ZDR. For those organizations, the Security posture page shows no comment box and asks for no answer when someone attests. If an organization saved a comment before those settings applied to it, the comment stays stored with its attestation. The Security posture page does not show that comment. Clearing the attestation deletes that comment.

While Security posture is not available to an organization, Anthropic keeps storing its attestations and comments. In that time, nobody can see or clear them on the Security posture page.
