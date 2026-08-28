> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Tenant setup wizard

> Walk through the guided setup that takes a brand new tenant from first sign-in to ready for users.

> **Who this is for:** Tenant administrators who have just been given access to a new Claude for Government deployment and need to get it ready for the rest of their agency.

When Anthropic first hands over your tenant, only you and any other administrators invited by email can sign in. The setup wizard walks you through the handful of things that need to be in place before everyone else can use Claude: a verified email domain, a connection to your identity provider, at least one organization, seats for that organization, and a routing rule that places people in it. Until setup is complete, a **Resume setup** banner appears at the top of the tenant and organization admin pages so you can pick up where you left off.

The wizard has a step list on the left and the current step on the right. Completed steps are ticked, and you can click any step in the list to jump to it. Every step has a **Continue later** link at the bottom that takes you back to the tenant admin portal; nothing is lost, and the **Resume setup** banner brings you back when you are ready. Steps marked **Optional** in the list can be skipped without blocking sign-in.

## Step 1: Welcome

The first step is a read-only summary of what Anthropic has already set up for you: your tenant's name, any email domains that Anthropic verified on your behalf during provisioning, and how many organizations already exist. There is nothing to fill in here. It is simply a chance to confirm that the tenant name is what you expect before you continue.

If a detail looks wrong (for example, the tenant name is misspelled), contact Anthropic before going further, because the tenant name cannot be changed from the portal.

## Step 2: Domains

Claude for Government looks at the domain of a person's email address to decide which tenant they belong to, so at least one verified domain must be registered before anyone else can sign in. The table at the top of this step lists the domains already on your tenant, along with whether each one is verified and whether it was added by Anthropic or by you.

If Anthropic already verified the domain you plan to use, you can move straight on to the next step. To add another domain, type it into the **Claim a domain** field and click **Claim**. You will be shown a DNS TXT record to publish on that domain. Once the record is live, click **Verify now** next to the pending claim and the domain becomes active. DNS changes can take anywhere from a few minutes to an hour to propagate, so try again shortly if verification does not succeed on the first attempt.

For more detail on how domains work and how to remove one later, see the [Domains section of the Identity and access page](/docs/government/tenant-admin/identity-and-access#domains).

## Step 3: Single sign-on

This step connects Claude for Government to your agency's identity provider (for example, Microsoft Entra, Okta, or ADFS) so that everyone signs in with their existing agency credentials. A **Connected** or **Not connected** badge next to the heading shows the current state.

This step is unavailable until you have verified at least one domain on the previous step. A banner on this step says so, because sign-in routes people to your tenant by the domain of their email address.

Setting this up is a two-way exchange:

1. Copy the values shown on this step and register a new application in your identity provider using them. **Redirect URI / ACS URL** is where your provider sends the user back after authentication (providers call it the Redirect URI for OIDC, or the Assertion Consumer Service URL for SAML). **SP Entity ID / Audience** is the identifier your provider uses to recognize this application.
2. Choose the **OIDC** or **SAML** tab to match what your provider supports, then fill in the form with the values your provider gives you for the new application. For OIDC these are the Client ID, Client secret, Authorization URL, Token URL, Issuer, and JWKS URL. For SAML this is a single IdP metadata XML document: paste the federation metadata from your provider, and the Entity ID and SSO URL are read from it and shown back to you once connected.
3. Save the form. The badge changes to **Connected** once the connection has been verified.

After you save a SAML connection, an **SP metadata URL** appears with the other values; most providers can import it to fill in the values automatically if you need to reconfigure.

Until single sign-on is connected, only owners who were invited directly by email can sign in. The full field reference for both protocols is on the [Identity and access](/docs/government/tenant-admin/identity-and-access#single-sign-on) page.

Once single sign-on is connected, people sign in from Claude Desktop or the web portal, and Claude for Government sends them to your provider from there. Starting from the application's tile in your provider's app portal, or from a sign-in test in its admin console, is not supported.

## Step 4: Provisioning (optional)

This step is optional. If your identity provider supports SCIM, which is a standard way for directory systems to push users and group memberships into other applications, you can connect it here so that accounts are created automatically rather than at first sign-in.

Like single sign-on, this step is unavailable until you have verified at least one domain on Step 2.

Copy the **Tenant URL** shown on this step into your identity provider's SCIM connector, then click **Generate token** and paste the token into the connector's secret token field. The token is shown only once, so copy it before closing the page. If you need to rotate it later, generate a new one and revoke the old one with the **Revoke** button.

You do not have to finish the provider-side setup before moving on. Once your provider has pushed at least one group, you can come back to the Routing step (or the [Identity and access](/docs/government/tenant-admin/identity-and-access#scim-provisioning) page) and add rules that place people by group membership.

## Step 5: Organizations

An organization is a workspace with its own members, its own seat allocation, its own spend caps, and its own settings. You need at least one before you can route anyone anywhere, and many agencies only ever need one. You would add more if different bureaus or programs need separate usage reporting, separate budgets, or different product settings.

Any organizations that already exist are listed at the top. To create one, fill in the **Add organization** form:

* **Name** is the display name shown throughout the portal.
* **Primary Owner email** is the person who will manage this organization's members and seats. They will be invited by email and land in the organization admin view when they sign in.
* **Billing account** is the account this organization draws from for seats and billed usage. Several organizations can share one account if they should be funded from a single budget.

Click **Add** and the new organization appears in the list. You can create as many as you need now and add more later from the [Organizations](/docs/government/tenant-admin/organizations) page.

## Step 6: Seats and spend caps

This step lets you give each organization seats and, optionally, a spend cap.

Seats control how many people in each organization can use Claude. The table shows each organization with a seat-count field for the first seat tier. Enter the number of seats each organization should have and save. Saving an organization's first seats also seats its Primary Owner, and anyone else already in it who has no seat tier, automatically. For per-tier control, use the full [Seats](/docs/government/tenant-admin/seats) page after setup.

Each organization's usage spends directly from its billing account's balance, and you can add a spend cap to limit how much any one organization can use in a rolling window. Caps are optional. If you leave them blank, the billing account's balance is the only limit. You can adjust both seats and caps later from the tenant [Seats](/docs/government/tenant-admin/seats) and [Billing](/docs/government/tenant-admin/credits) pages.

## Step 7: Routing

Routing rules decide which organization a person lands in when they sign in. A new person who does not match any rule cannot sign in at all, so you need at least one rule that covers your users. A single rule that maps your main email domain to your main organization is enough to get started.

Each rule reads like a sentence: a condition on the left, an arrow, and the target organization on the right. To add one, use the form at the bottom:

* In the **If** field, choose **Anyone with email domain** to match on the domain of the person's email address, or **Anyone with IdP group** to match on a group claim from your identity provider.
* In the second field, pick the domain or type the group name.
* In the **Then place in** field, pick the organization.
* Click **Add rule**.

Rules run from top to bottom and the first match wins, so drag more specific rules above broader ones. Rules that match directory groups pushed over SCIM are managed on the full [Identity and access](/docs/government/tenant-admin/identity-and-access#routing-rules) page, which also has a preview tool for testing where a specific email address would land.

## Steps 8 and 9: Seat tiers and Products (single-organization tenants only)

If your tenant has exactly one organization, the wizard includes two extra steps so that you can finish the organization-level setup without switching portals. You will only see these two steps in the step list if your tenant has a single organization. Tenants with more than one organization skip straight to the Finish step, and each organization's owner completes these two steps in their own [organization setup wizard](/docs/government/org-admin/setup-wizard) instead.

* **Seat tiers** lists the seat tiers available to the organization. A seat tier bundles together which Claude models a user may access and how much they may spend. Anthropic-managed tiers are set up for you during provisioning; if your organization is allowed to create self-managed tiers, you can add one here. See the organization [Seat tiers](/docs/government/org-admin/seat-tiers) page for the full editor.
* **Products** lets you choose which Claude products the organization's members can sign in to, for example Claude Desktop, Claude Code, and Claude for Microsoft 365. This is optional, and a product that is not available on your deployment is shown grayed out with a note to contact Anthropic.

## Final step: Finish

The last step shows a live readiness checklist. Each row is something that has to be in place before people can sign in, and it is ticked or crossed out as soon as you complete it. Items under the **Optional** heading do not block sign-in.

If anything required is still outstanding, a yellow banner tells you so, and the button at the bottom reads **Continue later** so you can come back. Once every required item is ticked, the button changes to **Go to tenant** and your deployment is ready. As colleagues sign in they will start appearing on each organization's Users page.

There is no separate "mark complete" action. The wizard reads the live state of your tenant, so if something changes later (for example, you remove your only routing rule), the **Resume setup** banner reappears on the tenant admin pages until the checklist is satisfied again.

## Things to know

* You can leave the wizard at any point using **Continue later**. Everything you have entered is saved, and the **Resume setup** banner on the tenant and organization admin pages brings you back to where you left off.
* Every step in the wizard edits the same settings as the matching page in the full tenant admin portal. You can use either one, and changes made in one place show up in the other.
* Steps tick automatically when the underlying condition is met. The **Provisioning** and **Products** steps are optional and never block the Finish step.
* Single sign-on and at least one routing rule are the two things that actually gate sign-in for everyone else. If you only have a few minutes, do those two first and come back for the rest.
