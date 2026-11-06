> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Identity and access

> Verify domains, connect single sign-on and SCIM, write the routing rules that place people in organizations, and look up what a sign-in error page means.

> **Who this is for:** Tenant administrators who connect the deployment to their agency's identity provider and control which organization each person belongs to.

Identity and access are configured once here and shared by every organization in your tenant.

> [!NOTE]
>
> These cases are covered on other pages:
>
> * **Setting up a new tenant**: see [Tenant setup wizard](https://claude.com/docs/government/tenant-admin/setup-wizard.md)
> * **Mapping directory groups to seat tiers and roles**: see [Group mappings](https://claude.com/docs/government/org-admin/provisioning.md)

## Domains

Claude for Government routes users to your tenant by the domain of their email address, so at least one domain must be verified before members can sign in. While Anthropic is finishing initial setup of your tenant, or if Anthropic has deactivated it, sign-in is disabled for everyone, and only Anthropic can change that. Once a tenant administrator can sign in, that setup is finished.

Your tenant can have more than one domain, and a verified domain can belong to only one tenant. However many domains are verified here, your tenant has one set of [admin portals](https://claude.com/docs/government/tenant-admin/overview.md#tenants-and-organizations), and the [routing rules](#routing-rules) decide which organization each person joins.

Domains that Anthropic registered on your behalf during onboarding are already verified. To add one yourself, enter the domain in the **Claim a domain** field and click **Claim**. You will be shown a DNS TXT record to publish on that domain; once the record is live, click **Verify now** and the domain becomes active.

> [!WARNING]
>
> Verify the domain of your own email address first, if your agency owns it. Once your tenant has a verified domain, you can't start sign-in or get the [emailed sign-in link](#emailed-sign-in-link) by entering an address on an unverified domain.

* **Verification delay.** DNS changes take time to propagate, so try again shortly if verification does not succeed on the first attempt.
* **After verification.** Keep the DNS TXT record in place while you are using Claude for Government.
* **Subdomains.** A subdomain is a separate domain, so verifying `example.gov` doesn't cover email addresses at `sub.example.gov`.
* **Removal.** To withdraw an unverified claim, click **Withdraw** next to it. To remove a verified domain, contact Anthropic.

## Single sign-on

Members sign in through your agency's identity provider (for example, Microsoft Entra, Okta, or ADFS), which needs to support SAML 2.0 or OpenID Connect (OIDC). You need at least one [verified domain](#domains) before you can connect single sign-on.

You register Claude for Government as an application in your identity provider, then enter your provider's connection details here. Once connected, sign-ins are redirected to your provider. A second sign-in from the same browser within a few minutes, such as connecting Claude Desktop right after signing in on the web, may not be redirected again.

Only one protocol is active at a time. Use the **OIDC** and **SAML** tabs to switch between the two forms; saving one replaces the other.

> [!WARNING]
>
> Saving a new single sign-on configuration takes effect immediately and applies to everyone, including you. After saving, select **Test sign-in** to check the connection with your own account while you stay signed in. If single sign-on fails, Primary Owners and tenant administrators can use the [emailed sign-in link](#emailed-sign-in-link).

### Register in your identity provider

Copy the following values from the card into your identity provider when you create the application there:

* **Redirect URI / ACS URL** is where your identity provider sends the user back after authentication. The same value is used whether you choose OIDC (where it's called the Redirect URI) or SAML (where it's called the Assertion Consumer Service URL).
* **SP Entity ID / Audience** is the unique identifier your identity provider uses to recognize this application. Providers label this field differently; it may appear as Identifier, Entity ID, or Audience URI.

For SAML, **More values your IdP may ask for** lists the remaining details some providers request. After you save a SAML connection, an **SP metadata URL** appears alongside these values.

### Connect with OIDC

If your identity provider supports OpenID Connect, fill in the OIDC section:

* **Client ID** is the application ID your identity provider assigned when you registered the app.
* **Client secret** is the secret your identity provider generated for that application. It is stored securely and never shown again after you save.
* **Authorization URL**, **Token URL**, **Issuer**, and **JWKS URL** are your identity provider's OIDC endpoints. Copy them exactly from your provider's OpenID Connect discovery document, whose address ends in `/.well-known/openid-configuration`. For Microsoft Entra, the Issuer ends in `/v2.0`.

### Connect with SAML

If your identity provider uses SAML, fill in the SAML section instead. Your provider must sign the SAML assertion, not only the response.

* **IdP metadata XML** is the federation metadata document for your identity provider. Download the XML file from your provider and paste the full document into the field. The metadata is read from what you paste; it is never fetched from a URL. When your identity provider rotates its signing certificate, download the new metadata XML, paste it into the **IdP metadata XML** field, and click the **Update** button.

Once SAML is active, the card shows the Entity ID and SSO URL extracted from your metadata so you can confirm the connection is pointing where you expect.

### Attribute mapping (advanced)

Open the **Attribute mapping** panel in the OIDC or SAML section if the email, first-name, or last-name fields arrive under different names than the defaults. For OIDC the defaults are the standard `email`, `given_name`, and `family_name` claims; for SAML the email default covers the common attribute names, and the name defaults are `firstName` and `lastName`.

Claude for Government identifies a person at single sign-on from what your identity provider returns, not from the email address they type, so typing an alias doesn't create a second account. A separate identity in your identity provider that has its own email address gets its own account when your [routing rules](#routing-rules) place it.

### Where sign-in starts

People start sign-in from a Claude app, such as Claude Desktop (**Sign in with your organization**), or from the web portal in a browser, and Claude for Government then sends them to your identity provider. Starting from the application's tile in your provider's app portal (such as Microsoft My Apps), or from a sign-in test in your provider's admin console, is not supported.

### Emailed sign-in link

There is no local break-glass account or stored password. Primary Owners and [tenant administrators](https://claude.com/docs/government/tenant-admin/admins.md) can sign in to the web portal without single sign-on, whether or not it is connected: they request a single-use link with **Email me a sign-in link** on the web portal's sign-in page.

Until your tenant has a verified domain, only tenant administrators can get a link. Once it has one, a link is sent only to an active Primary Owner or tenant administrator whose address is exactly on one of your tenant's [verified domains](#domains). One person can get at most five links an hour. The page that follows reads the same whether or not a link is sent.

## SCIM provisioning

<video controls preload="metadata" playsInline src="https://mintcdn.com/claude-ai/gGFKuNSbKYs4JMmK/images/government/videos/admin-04-directory-sync-scim-and-group-mappings.mp4?fit=max&auto=format&n=gGFKuNSbKYs4JMmK&q=85&s=e254e02786c5f309b5c5c240c7752c4e" aria-label="Video walkthrough: Directory sync (SCIM) and group mappings" />

Video: Directory sync (SCIM) and group mappings (2 min 3 s). Narrated with an AI-generated voice, with on-screen captions.

[Transcript](https://claude.com/docs/government/video-walkthroughs.md#directory-sync-scim-and-group-mappings)

SCIM is the standard protocol identity providers use to push users and groups to a connected service automatically, so that accounts are created, updated, and deactivated in step with your agency's directory. Connecting SCIM is optional; without it, users are created the first time they sign in. With SCIM connected, a person your directory has never sent still gets an account the first time they sign in, if a [sign-in rule](#sign-in-rules) covers them. People join your tenant by signing in or through your directory.

[Provisioning rules](#provisioning-rules-scim), [group mappings](https://claude.com/docs/government/org-admin/provisioning.md), and [group-specific settings](https://claude.com/docs/government/config/overview.md#group-specific-settings) need SCIM, because they act on the [directory groups](#directory-groups) your identity provider pushes. Model access and usage limits come from each person's [seat tier](https://claude.com/docs/government/org-admin/seat-tiers.md), which an organization owner can assign on the [Users](https://claude.com/docs/government/org-admin/users.md) page without SCIM.

### Connect your directory

SCIM provisioning is configured entirely from this page, with no action needed from Anthropic. You need at least one [verified domain](#domains) before you can generate a SCIM token.

* **SCIM base URL** is the address your identity provider pushes user and group updates to. You'll paste this value into your identity provider's provisioning settings, where Microsoft Entra calls it the *Tenant URL* and Okta calls it the *SCIM connector base URL*.
* **SCIM secret token.** Your identity provider authenticates to the SCIM address with a bearer token that you generate here. Click **Generate token** to create one, then paste the value into your identity provider's *Secret Token* (or equivalent) field.

> [!WARNING]
>
> The full token value is shown **only once**, immediately after you create it. Copy it into your identity provider before clicking Done. If you lose the value, generate a new token and revoke the old one.

Afterward the token table shows only a short hint (the last few characters) of each token. You can keep more than one token active at a time, which lets you rotate without an outage: generate a new token, update your identity provider to use it, confirm a sync succeeds, and then revoke the old one. Revoking a token takes effect immediately.

### Existing accounts when you connect SCIM

Connecting SCIM keeps existing accounts. A directory entry links to the account with the same email address when a [provisioning rule](#provisioning-rules-scim) names that person's organization, or at the latest at their next sign-in once they are in an organization. There is no need to delete an account first. A deactivation in your directory reaches the account once it is linked. Until then, your directory's request to deactivate, delete, or change the email address of that user is refused with a 409 error. Have your directory resend it once the account is linked.

Have your identity provider send, as the primary SCIM email, the address each person signs in with. A new entry with a different address creates a second account once a provisioning rule places it, and a deactivation in your directory doesn't reach the account they use. For users managed by your directory, the email address shown in Claude for Government is kept in step with your directory, and the sign-in token's email is ignored.

### Directory groups

Once your identity provider has pushed groups over SCIM, they appear here with their member counts. The order you set here is the priority used for group-level configuration on the [Config](https://claude.com/docs/government/config/overview.md#group-specific-settings) page and for [seat-tier mappings](https://claude.com/docs/government/org-admin/provisioning.md#how-mappings-are-applied). Reordering groups can change the seat tier of members who belong to more than one group mapped to a seat tier in their organization, without waiting for the next directory sync.

## Routing rules

<video controls preload="metadata" playsInline src="https://mintcdn.com/claude-ai/gGFKuNSbKYs4JMmK/images/government/videos/admin-03-organizations-seats-and-routing-rules.mp4?fit=max&auto=format&n=gGFKuNSbKYs4JMmK&q=85&s=3b4fdf17a38f17ace0a31daff24dd678" aria-label="Video walkthrough: Organizations, seats, and routing rules" />

Video: Organizations, seats, and routing rules (2 min 14 s). Narrated with an AI-generated voice, with on-screen captions.

[Transcript](https://claude.com/docs/government/video-walkthroughs.md#organizations-seats-and-routing-rules)

A **routing rule** is an instruction of the form "if a person matches this condition, place them in this organization." A new person whom no routing rule matches is refused: there is no default organization and no fallback. To send people to an organization by group, use a [provisioning rule](#provisioning-rules-scim) rather than the identity provider group rule shown in the video. Before you remove or reorder a sign-in rule, read [When rules move people](#when-rules-move-people).

Before any rule runs, the sign-in flow first checks that the person's email domain is one of your tenant's [**verified domains**](#domains). An address outside your verified domains never reaches your tenant at all, regardless of what rules you've written.

A person can arrive by signing in or through your directory, and each way has its own rule list:

* **Sign-in rules** run each time a person signs in.
* **Provisioning rules** run when your directory creates or updates someone through SCIM. They match on synced directory groups, and a change takes effect after you save it, without waiting for the next directory sync.

Until at least one rule is added, no new person can sign in, and a banner on the page says that no routing rules are configured.

### Sign-in rules

An **email domain** rule matches the domain of the user's email address exactly. You choose from your tenant's verified domains; you cannot type an arbitrary domain.

To place people by **group**, use a [provisioning rule](#provisioning-rules-scim).

Rules are evaluated from top to bottom, and the first match wins. Only one rule can exist for any given condition. Each rule shows a status line with diagnostics:

* **Last matched** (or **Never matched**) tells you when the rule most recently matched someone.
* A **target deactivated** badge means the rule points at an organization that has been deactivated. The rule is skipped during evaluation.
* A **stale value** badge means the condition refers to something that no longer exists, such as a domain removed from your verified list. The rule is skipped during evaluation.

### Provisioning rules (SCIM)

The console shows this section once SCIM is connected. Provisioning rules match on **directory groups** that your identity provider has synced, and decide which organization a user is placed in when your directory provisions or updates them. You choose groups from the synced list; a group that hasn't synced yet won't appear in the picker.

Provisioning rules work the same way as sign-in rules: they're an ordered list, the first match wins, and only one rule can exist per group. Adding, reordering, or removing provisioning rules can move already-placed users.

A provisioning rule doesn't place an account that is in no organization. Your tenant's first administrator starts that way, able to use the admin portal but not Claude. A [sign-in rule](#sign-in-rules) for their email domain does place them, but it applies to everyone on that domain who signs in while it exists. A person with no account gets one in the rule's organization. A member of another organization whom your directory doesn't manage [moves to it](#when-rules-move-people). Removing the rule undoes neither. So add the rule, have the administrator sign out and back in, then remove it. Or contact Anthropic to place them.

### Add and remove rules

To add a rule, choose the match type (for sign-in rules), pick the value, choose the target organization, and click **Add rule**. New rules are added at the bottom of the list; reorder after adding if you need a different priority. To remove a rule, click **Remove** next to it and confirm.

### When rules move people

A move ends the person's active sessions. It does not revoke a [Compliance API key](https://claude.com/docs/government/org-admin/compliance-api.md) they created. They lose their seat and role in the organization they leave, join the new one as a User or in the role its group mappings give them, and are reseated according to its available seats. Their account itself is kept. Because the Claude desktop app stores conversations on each person's own device, a move does not affect desktop chat history. See [Data storage and retention](https://claude.com/docs/government/security/security-and-data-handling.md#data-storage-and-retention).

Because sign-in rules run every time, a rule change has these effects on people who already exist:

* If a person now matches a rule that points to a different organization, they are moved on their next sign-in, unless another case in this list applies.
* If a person is a [Primary Owner](https://claude.com/docs/government/org-admin/users.md#understanding-roles) of their organization, they are moved only when they are also a [tenant administrator](https://claude.com/docs/government/tenant-admin/admins.md) and that organization has another active Primary Owner.
* Removing an identity provider group rule (listed as **Anyone with IdP group**), or moving it lower, can move people already in its organization at their next sign-in.
* If a person no longer matches any rule (for example, you removed the only rule that covered them), they keep their current organization and can still sign in. The no-match refusal applies only to people who have no account yet.
* If a person's account is managed by your directory (that is, it was created or linked through SCIM), sign-in rules do **not** move them. Directory-managed accounts are moved only by provisioning rules.

## When someone cannot sign in

### Preview routing

Enter an email address to see how that person would be routed, without changing anything. For a person who already has an account, the preview shows which rule matches them, not [whether they are moved or refused](#when-rules-move-people).

The result lists the rules in order with the outcome for each, for sign-in and, when SCIM is connected, for directory provisioning.

### Unplaced users

* **Rejected sign-ins** lists people who tried to sign in and were turned away, for example because no rule matched them. Each entry shows who tried and when. These records are kept so you can see who's trying and failing to get in. Click **Test in preview** to load that person's email into the preview. Click **Clear** to delete the record, or **Clear all** to remove every entry. Clearing does not block the person; a fresh entry appears if they are refused again.
* **Synced, not routed**, in the **Provisioning rules (SCIM)** section, lists directory entries not yet linked to an account. A new person here can sign in once a sign-in rule covers them or a provisioning rule places them. Someone who already has an account keeps signing in. To place the people in a group, add a provisioning rule that covers it. If someone in the group already has an account in another organization, the rule can [move them](#when-rules-move-people), unless they are a Primary Owner. The rule doesn't place an [account in no organization](#accounts-in-no-organization). People on a domain you haven't verified aren't placed, and people whose mapped tier has no free seats wait for one, as described under [How mappings are applied](https://claude.com/docs/government/org-admin/provisioning.md#how-mappings-are-applied).

Once a person is placed, their entries in these lists are cleaned up automatically.

### Sign-in error pages

The table shows what a person may see when sign-in fails, and what to do about it.

| What the person sees | What it means | What to do |
| - | - | - |
| "We couldn't find an organization for that email." | The address's domain is not a verified domain of any active tenant. Until Anthropic finishes setting up your tenant, everyone sees this | Verify the domain under [Domains](#domains). If no administrator can sign in, contact your Anthropic representative |
| "Single sign-on isn't configured for your organization yet." | The domain is verified, but no identity provider is connected | Connect [single sign-on](#single-sign-on). Primary Owners and tenant administrators can use the [emailed link](#emailed-sign-in-link) |
| **Almost there** | Your identity provider signed them in, but no routing rule matched, or the rule's organization is deactivated | Find them under **Rejected sign-ins** and add a [rule](#routing-rules) that covers them |
| **Signed in with a different account** | Your identity provider returned another address than the one they typed | They can continue as the returned address. If sign-in then finds no organization, verify that address's domain, or correct the address your provider sends |
| **Email address missing** | Your identity provider didn't send an email address | Add an email attribute or claim in your identity provider, or name it under [Attribute mapping](#attribute-mapping-advanced) |
| **Account deactivated** | Their account or directory entry is deactivated | Reactivate them in your directory: see [Deactivated users](https://claude.com/docs/government/org-admin/users.md#deactivated-users). If your directory doesn't manage them, contact your Anthropic representative |
| "Invalid signature in response from identity provider" | Your provider doesn't sign the assertion (required once you save the SAML section), or its signing certificate expired or isn't the one in your saved metadata | For an unsigned assertion, set your provider to sign it; no change is needed in Claude for Government. Otherwise renew the certificate if it expired, then paste the new metadata under [Connect with SAML](#connect-with-saml) |
| "Login timeout. Please sign in again." | A SAML response that arrives outside its validity period, or names the wrong audience, can produce this page right after the person signs in at your provider | Check the clock on each identity provider server you run, and set the audience in your provider to your [**SP Entity ID / Audience**](#register-in-your-identity-provider) |
| **Sign-in not completed** | The sign-in was canceled, or the exchange with your identity provider failed | Run **Test sign-in**, which names the likely cause |
