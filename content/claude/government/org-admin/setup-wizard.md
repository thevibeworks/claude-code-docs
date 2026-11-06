> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Setup wizard

> Setup wizard for a new organization: how to open it, and what the seat tiers, seats and credits, products, and finish steps cover.

> **Who this is for:** Organization owners setting up a newly created organization, or returning to finish setup later.

When a tenant administrator creates your organization and names you as its primary owner, a few things still need to be in place before your team can use Claude. The setup wizard walks you through those items in order, shows you which ones are already done, and tells you when something is waiting on someone else.

Until setup is complete, a banner reading **A few steps remain before your team can use Claude** appears in the organization admin portal. Click **Resume setup** in that banner to open the wizard. The banner goes away once every required item is complete, and it reappears on its own if a required item later becomes incomplete, for example if a spend cap is set too low.

Use **Continue later** on any step to leave the wizard, and come back through the banner whenever you are ready. The wizard makes the same changes as the matching pages in the admin portal.

## Wizard steps

* **Welcome.** Single sign-on and provisioning are configured by your tenant administrator rather than here, so your members will appear in this organization once they sign in through the tenant's identity provider, if your tenant administrator's routing rules send them here.
* **Seat tiers.** This step lists every tier available to your organization. See [Seat tiers](https://claude.com/docs/government/org-admin/seat-tiers.md#creating-a-self-managed-tier) for more on creating and editing tiers.
* **Seats & credits.** [Seats](https://claude.com/docs/government/org-admin/seats.md) are allocated outside the wizard, and Anthropic adds credits to the [billing account](https://claude.com/docs/government/org-admin/billing.md) your organization draws from, so this step is a status display rather than a form. Each line is a check from the [Readiness](https://claude.com/docs/government/org-admin/readiness.md#what-the-checks-mean) page and names who it is waiting on.
* **Products.** These are the Claude products your members sign in to, such as Claude Desktop, Claude Code, and Claude for Microsoft 365. Turning a product on allows your members to sign in to that application, unless your tenant administrator has turned it off for the whole tenant. This step is marked **Optional** in the step list. A product that is not available appears with its switch disabled and a note to contact Anthropic. You can change these switches later from the [Config](https://claude.com/docs/government/org-admin/configuration.md) page.
* **Finish.** The final step shows the full readiness checklist for your organization. For what the checks mean, see [Readiness](https://claude.com/docs/government/org-admin/readiness.md#what-the-checks-mean).
