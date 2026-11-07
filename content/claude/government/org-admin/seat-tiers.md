> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Seat tiers

> Seat tiers set which Claude models a user can access and how much they can spend. Organization owners create and manage their own seat tiers.

> **Who this is for:** Organization owners who need to review the seat tiers available to their organization or define their own.

A **seat tier** bundles together which Claude models a user may access and how much they may spend in a given period. Every user sits on exactly one tier (or is unassigned), and the tier they hold controls their day-to-day limits. The **Tiers** page lists every tier available to your organization. To open it, go to **People > Tiers** in the [organization admin portal](https://claude.com/docs/government/org-admin/overview.md#who-can-access-it). Tenant administrators reach that portal through **Switch to org view** in the tenant view's footer.

> [!NOTE]
>
> These tasks are covered on other pages:
>
> * **Put a user on a tier**: see [Assigning a seat tier](https://claude.com/docs/government/org-admin/users.md#assigning-a-seat-tier)
> * **Turn a Claude product on or off**: see [Product availability](https://claude.com/docs/government/config/settings.md#product-availability)

The tiers your organization creates are **self-managed tiers**. They draw from the credits in the [billing account](https://claude.com/docs/government/org-admin/billing.md) your organization spends from, so requests from people on them are refused while the account has no credits or your organization has reached a spend cap. They have no seat limit unless one is set.

> [!NOTE]
>
> **Anthropic-managed tiers.** If your agency buys seats, Anthropic sets up your tiers, and you don't need to create any. You can't delete an Anthropic-managed tier or change what it allows, and its spend limits aren't shown. To start new members on one, go to **People > Tiers**, open the tier, select [**New members start here**](https://claude.com/docs/government/org-admin/seats.md#how-seats-are-assigned-automatically), and click **Save**. These tiers don't draw from credits, so people on them keep working while the account has none.

## Creating a self-managed tier

You can create, edit, and delete self-managed tiers only if your tenant has [allowed organizations to manage their own seat tiers](https://claude.com/docs/government/config/settings.md#let-organizations-manage-their-own-seat-tiers). Go to **People > Tiers**, click **New seat tier**, and fill in the form. If you don't see the button, a tenant administrator can turn on that setting. If it is already on, contact your Anthropic representative.

> [!WARNING]
>
> Make sure your [billing account](https://claude.com/docs/government/org-admin/billing.md) has credits before anyone is placed on the tier, or their requests are refused.

* **Five-hour spend limit** sets how much each user on this tier can spend in a 5-hour window, expressed in dollars. When a user reaches this amount, further requests are refused until the limit [resets](https://claude.com/docs/government/account/usage.md#reading-the-reset-times).
* **Seven-day spend limit** does the same for a 7-day window. Both limits apply at the same time, so whichever is reached first stops the user.
* **Allowed models** controls which [Claude models](https://claude.com/docs/government/desktop/models.md) users on this tier may use. If you leave it empty, users on the tier have no model access regardless of their spend limits.
* **Default model** sets the model that new chats, tasks, and Code sessions in Claude Desktop start on, chosen from the tier's allowed models. It applies to users who haven't picked a model or effort level in the model picker.
* Select **Always start with the default model** to start every new chat, task, and Code session on the default model. Requires a **Default model** and Claude Desktop 2.110.0 or later.
* **New members start here** makes this the tier that people start on when they join your organization, as described under [How seats are assigned automatically](https://claude.com/docs/government/org-admin/seats.md#how-seats-are-assigned-automatically). Turning it on here turns it off for any other tier. On a tier with a seat limit and a mapped group, turning it off can move provisioned users who are in no mapped group [to another tier](https://claude.com/docs/government/org-admin/provisioning.md#group-to-seat-tier).

## Viewing and editing a tier

Go to **People > Tiers**, open a self-managed tier, and use its **Edit** form.

* Changes to spend limits and allowed models take effect immediately for every user on the tier: if you lower the spend limit, a user who is already over the new limit will be blocked on their next request until the limit resets, and if you remove a model from **Allowed models** it becomes unavailable to every user on the tier straight away.
* Changes to **Default model** and **Always start with the default model** reach users when Claude Desktop next [refreshes its configuration](https://claude.com/docs/government/config/overview.md#when-changes-take-effect), and a new default appears the next time they start Claude Desktop. When you set or change a tier's **Default model**, Claude Desktop prompts users on that tier who have the app open [to restart](https://claude.com/docs/government/config/settings.md#restart-deadline-for-configuration-changes). To avoid the prompt, set a tier's **Default model** before its users first open Claude Desktop.

If a banner that begins **Anthropic has provided default seat tiers** appears in the organization admin portal, Anthropic has set up a self-managed seat tier for your organization to review. Click **Review seat tiers**, then adjust the tier in the **Edit** form and click **Save**, or click **Keep these values**.

## Deleting a tier

Go to **People > Tiers**, open a self-managed tier, and click **Delete** to remove it entirely. Deletion is permanent.

If any users are still assigned to it, or any group mapping on the [Group mappings](https://claude.com/docs/government/org-admin/provisioning.md) page points at it, the delete is refused. Reassign or remove those references first, then delete the tier.
