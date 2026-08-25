> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Seats

> Use this page to check your organization's seat counts at a glance before assigning or reclaiming seats on the Users page.

> **Who this is for:** Organization owners who need to see how many seats of each tier are available and how many are in use.

Use this page to check your organization's seat counts at a glance before assigning or reclaiming seats on the Users page.

The **Seats** page shows how many seats your organization has for each seat tier and how many of them are currently assigned to users. It is the default landing page when you open the organization admin portal.

A **seat tier** is a named level of access that defines which Claude models a person can use and how much they can use them over a rolling time window. Every user in your organization occupies exactly one seat, and that seat belongs to a tier (or the user is **Unassigned**, in which case they have no model access at all).

## What you see

Seats are grouped into two sections based on who controls the tier.

<Note>
  Each section below only appears when your organization has at least one tier of that kind. If you have neither, the page shows a message explaining that seats are distributed by your tenant administrators.
</Note>

**Anthropic-managed tiers** are defined by Anthropic and allocated to your organization from your tenant's seat pool. For each one the table shows the **Assigned** count, which is how many of your users are on that tier, alongside the **Limit**, which is the number of seats your organization has been allocated. You cannot assign more users to a tier than its limit allows.

**Self-managed tiers** are tiers that your organization created itself on the [Tiers](/docs/government/org-admin/seat-tiers) page. For each one the table shows the **Assigned** count and, if a seat limit has been allocated for that tier, the **Limit**. These tiers draw from the billing account your organization spends from, so the effective constraint is usually the account's balance and any spend cap set on your organization rather than a seat count.

## How seats are assigned automatically

When a new user is created in your organization, whether they arrive through single sign-on or through directory provisioning, Claude for Government tries to place them on a seat tier automatically so they can start working right away.

If the user arrives through directory provisioning and belongs to a group you have mapped to a specific tier on the [Group mappings](/docs/government/org-admin/provisioning) page, that mapping takes precedence and the user is placed on the mapped tier if a seat is available.

Otherwise the system walks through all of your tiers, both Anthropic-managed and self-managed, in sort order (lowest first) and places the user on the first tier that has a free seat. Self-managed tiers may or may not have a seat limit, depending on how they were allocated. A user is left **Unassigned** when every tier that has a seat allocation is full, or when your organization has not been allocated any seats yet. An unassigned user has no model access.

Automatic placement happens when a user first arrives. A user who is already **Unassigned** gets a seat tier in one of these ways:

* An owner chooses one for them on the [Users](/docs/government/org-admin/users) page. A tenant administrator can do the same from your organization's admin view.
* Your organization receives its first seat allocation. Members without a seat tier are seated automatically from the new seats at that moment, Primary Owners first and in the same tier order as above, provided nobody in the organization already holds a seat. Anyone still without a seat tier afterwards, for example because there were more members than seats, needs an owner to choose one for them on the Users page. Later allocation changes do not repeat this, so a user you deliberately leave unassigned stays that way.
* The user arrived through directory provisioning and belongs to a group that is mapped to a tier. The next sync seats them once the mapped tier has a free seat, as described on the [Group mappings](/docs/government/org-admin/provisioning) page.

<Tip>
  If you see an Anthropic-managed tier whose **Assigned** count equals its **Limit**, new users cannot land on it automatically. Either increase the allocation on the [Billing](/docs/government/org-admin/billing) page, move existing users to a different tier to free seats, or ask a tenant administrator to add seats.
</Tip>

## What you can do here

This page is read-only. To move a user onto a different tier, use the [Users](/docs/government/org-admin/users) page. To create or edit self-managed tiers, use the [Tiers](/docs/government/org-admin/seat-tiers) page.

<Tip>
  To change how many seats of an Anthropic-managed tier your organization holds, go to the [Billing](/docs/government/org-admin/billing) page if it is available to you, or ask a tenant administrator.
</Tip>

## Things to know

* The **Assigned** count includes only active users. When a user is deactivated, their seat is released immediately and becomes available for someone else.
* Changing a tier's limit on the Billing page does not move anyone who already holds a seat. If you lower a limit, you must first move enough users off the tier so the assigned count fits within the new limit, because the system will not let you reduce an allocation below the number of people currently seated on it.
* The sort order that controls automatic assignment is managed on the [Tiers](/docs/government/org-admin/seat-tiers) page. Anthropic-managed tiers have a fixed order set by Anthropic, and self-managed tiers sort wherever their sort order number places them relative to the managed ones.
