> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Tenant setup wizard

> Set up a new tenant in order: verify a domain, connect single sign-on, add an organization, give it seats, and add the routing rule that lets people sign in.

> **Who this is for:** Tenant administrators who have just been given access to a new Claude for Government deployment and need to get it ready for the rest of their agency.

The setup wizard walks you through the things that need to be in place before everyone else can use Claude: a verified email domain, a connection to your identity provider, at least one organization, seats for that organization, and a routing rule that places people in it.

Before single sign-on is connected, you sign in with a single-use link that the sign-in page emails to you on request. See [Emailed sign-in link](https://claude.com/docs/government/tenant-admin/identity-and-access.md#emailed-sign-in-link). Until the required steps are complete, a **Resume setup** banner appears at the top of the tenant admin pages, and its button opens the wizard. If you land in another view, use the footer links to reach the tenant view.

Every step in the wizard edits the same settings as the matching page in the full admin portal. You can leave the wizard at any point using **Continue later**.

## Wizard steps

### Welcome step

The first step is a read-only summary of what Anthropic has already set up for you. If a detail looks wrong (for example, the tenant name is misspelled), contact Anthropic before going further, because the tenant name cannot be changed from the portal.

### Domains step

<video controls preload="metadata" playsInline src="https://mintcdn.com/claude-ai/gGFKuNSbKYs4JMmK/images/government/videos/admin-02-verify-your-domain-and-connect-single-sign-on.mp4?fit=max&auto=format&n=gGFKuNSbKYs4JMmK&q=85&s=bf307a4d18d646cbce35d3c269be51b7" aria-label="Video walkthrough: Verify your domain and connect single sign-on" />

Video: Verify your domain and connect single sign-on (2 min 24 s). Narrated with an AI-generated voice, with on-screen captions.

[Transcript](https://claude.com/docs/government/video-walkthroughs.md#verify-your-domain-and-connect-single-sign-on)

The video also covers the Single sign-on step. For later steps, see [Video walkthroughs](https://claude.com/docs/government/video-walkthroughs.md#admin-series).

Claude for Government looks at the domain of a person's email address to decide which tenant they belong to, so at least one verified domain must be registered before anyone else can sign in. If Anthropic already verified the domain you plan to use, you can move straight on to the next step. To add another domain, see [Domains](https://claude.com/docs/government/tenant-admin/identity-and-access.md#domains), and read its warning first, so that you can still sign in.

### Single sign-on step

Until single sign-on is connected, only tenant administrators and Primary Owners can sign in, by [emailed link](https://claude.com/docs/government/tenant-admin/identity-and-access.md#emailed-sign-in-link). The full field reference for both protocols is on the [Identity and access](https://claude.com/docs/government/tenant-admin/identity-and-access.md#single-sign-on) page.

Once single sign-on is connected, people [sign in from a Claude app or the web portal](https://claude.com/docs/government/tenant-admin/identity-and-access.md#where-sign-in-starts), and Claude for Government sends them to your provider from there. After connecting, use **Test sign-in** on this step to check that it works.

### Provisioning step

This step is optional, though highly recommended. If your identity provider supports SCIM, you can connect it here so that accounts are created automatically. To connect it, see [SCIM provisioning](https://claude.com/docs/government/tenant-admin/identity-and-access.md#scim-provisioning). This step labels the SCIM base URL **Tenant URL**.

You do not have to finish the provider-side setup before moving on. Once your provider has pushed at least one group, you can add provisioning rules that place people by group membership on the [Identity and access](https://claude.com/docs/government/tenant-admin/identity-and-access.md#provisioning-rules-scim) page.

### Organizations step

You need at least one organization before you can route anyone anywhere. If Anthropic already created one, this step lists it and you can move on. To add one, fill in the **Add organization** form, described under [Adding an organization](https://claude.com/docs/government/tenant-admin/organizations.md#adding-an-organization). For **Primary Owner email**, choose someone on one of your verified domains who has no active account in your tenant yet. No invitation is sent, so let them know.

### Seats and spend caps step

This step lets you give each organization seats and, optionally, a spend cap. It shows a seat-count field for the first seat tier. For per-tier control, use the full [Seats](https://claude.com/docs/government/tenant-admin/seats.md) page after setup. If the step says there are no seats to distribute, continue. Each organization then needs [a seat tier of its own](#seat-tiers-and-products-steps) before its members can use Claude. You can adjust caps later from the tenant [Billing](https://claude.com/docs/government/tenant-admin/credits.md) page.

### Routing step

Routing rules decide which organization a person lands in when they sign in. A new person who does not match any rule cannot sign in at all, so you need at least one rule that covers your users. A single rule that maps your main email domain to your main organization is enough to get started. To add one, use the form:

* In the **If** field, choose **Anyone with email domain**, and in the second field pick the domain.
* In the **Then place in** field, pick the organization.
* Click **Add rule**.

A domain rule that covers your own address places you in that organization too, as a User, at your next sign-in. You keep tenant administration. If no domain rule covers your address, see [how to join an organization yourself](https://claude.com/docs/government/tenant-admin/identity-and-access.md#accounts-in-no-organization).

Rules that match directory groups pushed over SCIM are managed on the full [Identity and access](https://claude.com/docs/government/tenant-admin/identity-and-access.md#routing-rules) page, which also has a preview tool for testing where a specific email address would land.

### Seat tiers and Products steps

Unless your tenant has more than one organization, the wizard includes the **Seat tiers** and **Products** steps. In a tenant with more than one organization, each organization's owner completes them in their own [organization setup wizard](https://claude.com/docs/government/org-admin/setup-wizard.md), which describes both. The optional **Products** step sets which Claude products your members can sign in to, such as Claude Desktop, Claude Code, and Claude for Microsoft 365.

Seat tiers set each person's spend limits. To [see or change your seat tiers](https://claude.com/docs/government/org-admin/seat-tiers.md) after setup, select **Switch to org view** in the page footer and go to **People > Tiers**.

### Finish step

The last step shows a live readiness checklist. For what the checks mean, see [Readiness](https://claude.com/docs/government/tenant-admin/readiness.md#tenant-level-checks). **Connect single sign-on** isn't a required step, but members can't sign in until you connect it.

The wizard reads the live state of your tenant, so if something changes later (for example, you remove your only routing rule), the **Resume setup** banner reappears on the tenant admin pages until the checklist is satisfied again.
