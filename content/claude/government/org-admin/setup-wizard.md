> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Setup wizard

> Walk through the steps that get your organization ready for users after a tenant administrator creates it.

> **Who this is for:** Organization owners setting up a newly created organization, or returning to finish setup later.

When a tenant administrator creates your organization and names you as its primary owner, a few things still need to be in place before your team can use Claude. The setup wizard walks you through those items in order, shows you which ones are already done, and tells you when something is waiting on someone else.

Until setup is complete, a banner reading **A few steps remain before your team can use Claude** appears at the top of every page in the organization admin portal. Click **Resume setup** in that banner to open the wizard. The banner goes away once everything is ready, and it reappears on its own if a required item later becomes incomplete, for example if the billing account's balance runs out or a spend cap is set too low.

You don't need to finish the wizard in one sitting. Use **Continue later** on any step to return to the admin portal, and come back through the banner whenever you are ready.

## How the wizard is laid out

The wizard is titled **Set up your organization** and lists five steps down the left side. Each step shows a green check once its requirement is met, and you can click any step to jump straight to it. The checks reflect the live state of your organization rather than whether you have visited the step, so a step can already be checked when you arrive and can lose its check if something changes later.

At the bottom of every step, **Continue later** exits to the admin portal and **Next** moves to the following step.

## Step 1: Welcome

The first step confirms which organization and tenant you are setting up and what your role is. It also explains the division of responsibility: single sign-on and provisioning are configured by your tenant administrator rather than here, so your members will appear in this organization automatically once they sign in through the tenant's identity provider. There is nothing to fill in on this step.

## Step 2: Seat tiers

A seat tier sets which Claude models a group of users can access and how much they can spend in a given period. This step lists every tier available to your organization. Anthropic-managed tiers are shown first and are labeled **Managed by Anthropic**, followed by any self-managed tiers your organization has defined. Each row shows the tier name and the number of allowed models, and self-managed tiers also show their five-hour and seven-day spend limits.

Click any tier to open it. An Anthropic-managed tier opens as a read-only summary, because its limits are set by Anthropic. A self-managed tier opens as an editable form where you can change the name, spend limits, and allowed models without leaving the wizard.

If your tenant lets organizations manage their own tiers, an **Add seat tier** button appears below the list so you can create one here. If that button is missing, your tenant has not turned on **Let organizations manage their own seat tiers**, and only Anthropic can create or change tiers for your organization.

The step is checked once at least one of your tiers has at least one model allowed. See [Seat tiers](/docs/government/org-admin/seat-tiers) for more on creating and editing tiers.

## Step 3: Seats and credits

This step shows whether your organization has the seats and credits it needs. Seats are allocated by your tenant administrator, and Anthropic adds credits to the billing account your organization draws from, so this step is a status display rather than a form. It is here so you can see at a glance whether you are still waiting on someone.

Two status lines are shown:

* **Add credits** is complete once the billing account your organization draws from has enough balance to serve at least one request. This is funded by Anthropic through your tenant administrator, so when it is incomplete the line shows **Waiting on your tenant admin**. Use **View billing** to open the [Billing](/docs/government/org-admin/billing) page and see the current balance and any spend caps set on your organization.
* **Allocate seats** is complete once your organization has been allocated at least one seat. Use **View seats** to open the [Seats](/docs/government/org-admin/seats) page and see the counts.

The step is checked only when both lines are complete. If either one is still waiting, contact a tenant administrator.

## Step 4: Products

These are the Claude products your members sign in to, such as Claude Desktop, Claude Code, and Claude for Microsoft 365. This step shows an on/off switch for each one. Turning a product on allows your members to sign in to that application.

This step is marked **Optional** in the step list, and you can leave every product off and still complete setup. A product that is not available appears with its switch disabled and a note to contact Anthropic if you would like it enabled.

You can change these switches later from the [Config](/docs/government/org-admin/configuration) page.

## Step 5: Finish

The final step shows the full readiness checklist for your organization so you can confirm everything is in place. Completed items are crossed out, and any item that is still outstanding shows the reason and who it is waiting on.

If anything required is still incomplete, a warning banner appears at the top of this step and the primary button reads **Continue later**. Back in the admin portal the **Resume setup** banner will stay in place until the outstanding items are resolved.

Once every required item is complete, the warning goes away, the primary button changes to **Go to the Admin Console**, and your users can sign in and start using Claude.

## Things to know

* The wizard makes the same changes as the matching pages in the admin portal. Creating a seat tier here is exactly the same as creating one on the Tiers page.
* Checks in the step list are derived from your organization's current state, so they update whenever that state changes, even outside the wizard.
* Once setup is complete the subtitle changes to **Setup complete. Revisit any step to make changes**, and you can return at any time to review or adjust what you set.
