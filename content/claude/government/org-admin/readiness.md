> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Readiness

> Readiness checks for your organization: what the checks on credits, spend caps, seats, seat tiers, models, and products mean, and who can clear each one.

> **Who this is for:** Organization owners who are setting up an organization for the first time, or who need to find out why their users are unable to use Claude.

The **Readiness** page shows what this organization still needs before its members can use Claude, and where each item is resolved. To open it, go to **Settings > Readiness** in the organization admin portal. You would normally work through it once when the organization is first set up and then return whenever the **Settings** menu shows a notification dot. The dot means a required step is unfinished.

An open step explains why it is blocked, and either offers a button that takes you to the page where the fix is made or names who it is waiting on. A step that isn't required doesn't raise the dot, but members can still be stuck until it is done.

Your tenant administrator can clear the steps that wait on them from the [tenant Readiness page](https://claude.com/docs/government/tenant-admin/readiness.md), which shows every organization's checklist in one place.

## What the checks mean

The table shows what a check means when it is unfinished, and who can clear it.

| Check | What it means | Who clears it |
| - | - | - |
| **Activate the organization** | This organization has been deactivated. While it is inactive its members cannot sign in and none of the other checks can be cleared. | Anthropic |
| **Assign a seat tier to the organization** | No seat tier is available to this organization. Until one is, no member can be given a seat. | You, or whoever the step names |
| **Add credits** | The billing account your organization draws from needs credits. Until it has them, every message from a user on a [self-managed tier](https://claude.com/docs/government/org-admin/seat-tiers.md#anthropic-managed-versus-self-managed-tiers) is refused. | Only Anthropic can add credits, so this step shows **Waiting on Anthropic** |
| **Raise the organization's spend cap** | A tenant administrator has set a spend cap on your organization that is too low to cover a request. Every request from a user on a self-managed tier is refused until the cap is raised or cleared. | Only a tenant administrator can change caps, so this step shows **Waiting on your tenant admin** |
| **Assign a model to your seat tier** | No seat tier in this organization both allows a usable model and has usage limits high enough for one request, so nobody can send a message regardless of credits or seats. | You, on the [Seat tiers](https://claude.com/docs/government/org-admin/seat-tiers.md) page, by adding a model or raising the tier's limits. Anthropic, for a tier you can't edit |
| **Allocate seats** | New members arrive without a seat and cannot send messages. | Your tenant administrator, or the organization that manages your billing account: see [Seats](https://claude.com/docs/government/org-admin/seats.md) |
| **Assign seat tiers to members** | An active member has no seat tier, and a member without one cannot use Claude. | You, on the [Users](https://claude.com/docs/government/org-admin/users.md) page, when a seat is free. A member without a seat shows **Unassigned** there. See also [How seats are assigned automatically](https://claude.com/docs/government/org-admin/seats.md#how-seats-are-assigned-automatically) |
| **Enable a product** | No Claude product, such as Claude Desktop, Claude Code, or Claude for Microsoft 365, is enabled for this organization. With nothing enabled, no client application can start. | You or your tenant administrator, on the [Config](https://claude.com/docs/government/org-admin/configuration.md) page |
