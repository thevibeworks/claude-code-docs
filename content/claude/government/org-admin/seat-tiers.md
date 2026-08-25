> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Seat tiers

> Use this page to see the models and spend limits attached to each tier and, when permitted, to create and edit self-managed tiers.

> **Who this is for:** Organization owners who need to review the seat tiers available to their organization or define their own.

Use this page to see the models and spend limits attached to each tier and, when permitted, to create and edit self-managed tiers.

A **seat tier** bundles together which Claude models a user may access and how much they may spend in a given period. Every user sits on exactly one tier (or is unassigned), and the tier they hold controls their day-to-day limits. The **Tiers** page lists every tier available to your organization.

## The tier list

Tiers are listed with Anthropic-managed tiers first, followed by your organization's self-managed tiers. Each entry shows the tier's name, how many users are currently on it, and the seat limit if one applies. Clicking any tier opens its detail page.

## Anthropic-managed versus self-managed tiers

**Anthropic-managed tiers** are defined by Anthropic and allocated to you through your tenant's billing account. On the detail page you can see which models the tier allows, but the spend limits are not shown and you cannot change the tier's settings or delete it. These tiers are paid for as seats rather than through credit drawdown, so their per-user spend limits are an internal detail that Anthropic manages on your behalf.

**Self-managed tiers** are created by your organization. They draw from the billing account your organization spends from instead of a fixed seat count, and you have full control over their name, spend limits, and allowed models. A self-managed tier may or may not have a seat limit, depending on how it was allocated; when it has no limit, you can place as many users on it as you wish and the account's balance and any spend cap set on your organization are the effective constraint.

## Creating a self-managed tier

Click **New seat tier** and fill in the form.

* **Name** sets what the tier is called, for example *Analyst* or *Reviewer*. Names must be unique within your organization, and cannot duplicate the name of any Anthropic-managed tier.
* **Five-hour spend limit** sets the most each user on this tier can spend in any rolling 5-hour window, expressed in dollars. When a user reaches this amount, further requests are refused until the window rolls forward. Set it to zero to allow no usage at all.
* **Seven-day spend limit** does the same for a rolling 7-day window. Both limits apply at the same time, so whichever is reached first stops the user.
* **Allowed models** controls which Claude models users on this tier may use. If you leave it empty, users on the tier have no model access regardless of their spend limits.
* **Sort order** is a number that controls the order in which a seat is automatically chosen for a newly provisioned user (lowest number is tried first). If two tiers share the same sort order they are ordered consistently, but it is clearer to give each tier a distinct value.

An organization may create up to 50 self-managed tiers.

<Warning>
  The **New seat tier** button only appears if your tenant has allowed organizations to manage their own seat tiers. This permission is controlled by the **Let organizations manage their own seat tiers** setting on the tenant's Config page. If you don't see the button, ask a tenant administrator.
</Warning>

## Viewing and editing a tier

A tier's detail page shows its current values along with an **Allowed models** section that groups the permitted models by family.

<Note>
  The **Edit** form and **Delete** button only appear on self-managed tiers. For an Anthropic-managed tier the page is read-only.
</Note>

For a self-managed tier the **Edit** form lets you update any of the fields above. Changes take effect immediately for every user on the tier: if you lower the spend limit, a user who is already over the new limit will be blocked on their next request until their window rolls forward, and if you remove a model from the allowlist it becomes unavailable to every user on the tier straight away.

## Deleting a tier

The **Delete** button removes a self-managed tier entirely. Deletion is permanent and cannot be undone from this portal.

You can only delete a tier that nothing references. If any users are still assigned to it, any API keys are bound to it, or any group mapping on the [Group mappings](/docs/government/org-admin/provisioning) page points at it, the delete is refused with a message telling you so. Reassign or remove those references first, then delete the tier.

## Things to know

* Changing a tier's **Sort order** affects where newly provisioned users land, but it does not move anyone who already has a seat.
* The spend limits are per user, not per tier. Ten users on a tier with a \$20 seven-day limit can together spend up to \$200 from the billing account over seven days.
* Moving a user between tiers does not reset their usage counters. A user who has spent \$15 in the current 5-hour window carries that spend with them, and it is measured against the new tier's limit on their next request.
* Users choose among a tier's allowed models in the Claude Desktop model picker, described in [Models in Claude Desktop](/docs/government/desktop/models). For some models the picker also offers a **1M context window** entry, which Anthropic sets per model and which is not part of the tier.
