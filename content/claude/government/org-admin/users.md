> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Users

> Use this page to find a user, change their role or seat tier, check how close they are to their usage limits, and reset those limits when needed.

> **Who this is for:** Organization owners who need to manage individual users' roles, seat tiers, and usage limits.

Use this page to find a user, change their role or seat tier, check how close they are to their usage limits, and reset those limits when needed.

The **Users** page lists everyone in your organization and lets you manage their access.

## Finding users

Type into the search box to filter the list by name or email address. Use **Filters** to include deactivated accounts.

## What's shown for each user

Each user appears as a card with their name, email address, and the following fields:

| Field          | Description                                                                                                                                                                                                                                         |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Role**       | The user's role in this organization. You can change it directly from the dropdown.                                                                                                                                                                 |
| **Seat tier**  | Which seat tier the user currently occupies. You can change it directly from the dropdown.                                                                                                                                                          |
| **Usage**      | Two bars showing how much of the user's 5-hour and 7-day spend limits are currently used, with the exact percentage alongside each. Hover over the bars to see when each limit resets. Users who have no seat tier show a dash instead of the bars. |
| **Last login** | The date and time the user last signed in.                                                                                                                                                                                                          |

The **…** menu on each card has the **Reset usage limits** action, which clears the user's current rate-limit windows. The menu appears only when your organization has at least one [self-managed seat tier](/docs/government/org-admin/seat-tiers).

## Understanding roles

A **role** controls what a person can do in the admin portal. It has no effect on which Claude models they can use or how much they can use them; those are controlled by the seat tier.

* A **User** can use the Claude products but has no admin access.
* An **Owner** can access this organization admin portal and perform every action described in this guide except for granting or removing the Primary Owner role.
* A **Primary Owner** has the same access as an Owner and is additionally protected so that an organization can never be left without one. Only a Primary Owner can promote another user to Primary Owner or demote an existing one.

An organization must always have at least one active Primary Owner and may have up to three. Keep at least two so that when one leaves your agency or loses account access, a remaining Primary Owner can promote a replacement and demote the person who left.

If your organization no longer has a Primary Owner who can sign in, contact Anthropic to have a new one appointed. A tenant administrator cannot grant the role for you, because opening your organization from the tenant portal gives them Owner access only. Until the new Primary Owner is in place, your Owners and tenant administrators can keep managing users, seats, and settings.

## Changing a user's role

Use the **Role** dropdown on a user's row to move them between User, Owner, and Primary Owner. The change applies immediately, and a user who is promoted to Owner can open the admin portal as soon as they refresh.

The following safeguards apply and the dropdown will refuse the change if any of them would be violated.

* You cannot change your own role. To be promoted or demoted, ask another Owner or Primary Owner to make the change for you.
* Only a Primary Owner can grant or remove the Primary Owner role. An Owner can freely move people between User and Owner, but any change that crosses into or out of Primary Owner must be made by a Primary Owner.
* You cannot demote the organization's only active Primary Owner. Promote a second person to Primary Owner first, then demote the original.
* You cannot promote a deactivated user to Primary Owner. Reactivate them first.
* You cannot add a fourth Primary Owner. Demote one of the existing Primary Owners first if you need to make room.

<Warning>
  If your organization uses directory provisioning with a group-to-role mapping, be aware that the next sync will re-apply the mapped role and may overwrite a manual change you make here. To make a permanent role change for a provisioned user, update their group membership in your identity provider instead.
</Warning>

## Assigning a seat tier

Use the **Seat tier** dropdown to move a user onto a different tier or back to **Unassigned**. An unassigned user has no model access at all, which is the appropriate state for someone who should keep their account but should not consume any Claude usage.

The dropdown lists Anthropic-managed tiers first, each labeled *Managed by Anthropic*, followed by your self-managed tiers with a short summary of their model count and spend caps. If a tier has no seats remaining it appears marked **(at capacity)** and cannot be selected, unless the user is already on it.

Changing a user's tier takes effect on their very next request. If you move someone to a tier with a different set of allowed models, any model that is no longer in their tier's allowlist becomes unavailable to them immediately.

<Warning>
  If your organization uses directory provisioning with a group-to-tier mapping, the next sync will re-apply the mapped tier. For provisioned users, adjust their directory group membership rather than changing the tier here.
</Warning>

## Resetting a user's limits

Every seat tier sets a rolling **5-hour** and **7-day** spend limit for each user. When a user reaches either limit, further requests are refused until the window rolls forward.

If a user on a self-managed tier has hit a limit and you want them to continue working immediately, use **Reset usage limits** in the **…** menu on their card. This clears both of their current windows so their next request is admitted. The reset does not refund or alter any credits that have already been consumed, and it does not change anything shown on the [Analytics](/docs/government/org-admin/analytics) page; it only clears the per-user counter that enforces the limit.

<Warning>
  The reset button is disabled for users on Anthropic-managed tiers because those limits are set by Anthropic and are not yours to waive. Additionally, if a user moved off an Anthropic-managed tier within the last seven days, the reset button is temporarily unavailable for them and the tooltip tells you when it becomes available again.
</Warning>

## Deactivated users

Accounts are deactivated through your directory's SCIM provisioning rather than from this page. A deactivated user cannot sign in and does not occupy a seat. Deactivating a user releases their seat immediately, and reactivating them later will attempt to place them back on a seat using the same automatic assignment logic described on the [Seats](/docs/government/org-admin/seats) page.

Deactivated users keep their role, but a deactivated Primary Owner does not count toward the "at least one" rule or the limit of three. You must always have at least one *active* Primary Owner.

## Things to know

* Claude for Government has exactly three organization roles: **User**, **Owner**, and **Primary Owner**. There are no additional roles such as Billing or Developer. Tenant administrator access is a separate tenant-level membership managed on the [Admins](/docs/government/tenant-admin/admins) page, not an organization role.
