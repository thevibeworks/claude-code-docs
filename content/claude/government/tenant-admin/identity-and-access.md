> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Identity and access

> Connect single sign-on, manage SCIM provisioning, and write the routing rules that place users into organizations.

> **Who this is for:** Tenant administrators who connect the deployment to their agency's identity provider and control which organization each person belongs to.

Use this page to connect single sign-on, manage the SCIM provisioning token, write the routing rules that place users into organizations, preview how a specific person would be routed, and review people who haven't been placed yet.

Identity and access are configured once here and shared by every organization in your tenant. The page is laid out top to bottom in the order you'll usually work through it: connect single sign-on, optionally connect directory provisioning, then write routing rules, then use the preview and the waiting lists to confirm everyone is being placed where you expect.

## Status banners

Three banners can appear at the top of the page:

* **Still being provisioned** appears while Anthropic is finishing initial setup of your tenant. Sign-in is disabled for everyone until provisioning completes, but you can configure everything on this page in the meantime so that it takes effect as soon as the tenant goes live.
* **No routing rules configured** appears when no routing rules exist. Until at least one rule is added, no new person can sign in.
* **Last SCIM push** shows when your directory most recently pushed an update. It appears only after your directory has completed at least one sync.

## Domains

Claude for Government routes users to your tenant by the domain of their email address, so at least one domain must be registered before anyone can sign in. The **Domains** section lists every domain registered to your tenant, along with whether it is verified and whether it was registered by Anthropic or by you.

Domains that Anthropic registered on your behalf during onboarding are already verified. To add one yourself, enter the domain in the **Claim a domain** field and click **Claim**. You will be shown a DNS TXT record to publish on that domain; once the record is live, click **Verify now** and the domain becomes active.

Until at least one domain is verified, the Single sign-on section's Connect button and the SCIM provisioning section's **Generate token** button are both unavailable, and each section shows a banner explaining why. Existing tenant administrators can still sign in by email link during this time.

## Single sign-on

Every user signs in through your agency's identity provider (for example, Microsoft Entra, Okta, or ADFS). You register Claude for Government as an application in your identity provider, then enter your provider's connection details here. Once connected, sign-ins are redirected to your provider. A second sign-in from the same browser within a few minutes, such as connecting Claude Desktop right after signing in on the web, may not be redirected again.

<Note>
  You need at least one verified domain before you can connect single sign-on. Until then, the Connect button is unavailable and a banner prompts you to verify a domain first. If single sign-on was already connected before your last domain was removed, the existing connection stays editable.
</Note>

The card header shows a **Connected (OIDC)**, **Connected (SAML)**, or **Not configured** badge so you can see the current state at a glance. Only one protocol is active at a time. Use the **OIDC** and **SAML** tabs to switch between the two forms; saving one replaces the other.

### Registering in your identity provider

Copy the following values from the card into your identity provider when you create the application there:

* **Redirect URI / ACS URL** is where your identity provider sends the user back after authentication. The same value is used whether you choose OIDC (where it's called the Redirect URI) or SAML (where it's called the Assertion Consumer Service URL).
* **SP Entity ID / Audience** is the unique identifier your identity provider uses to recognize this application. Providers label this field differently; it may appear as Identifier, Entity ID, or Audience URI.

For SAML, a **More values your IdP may ask for** expander below these fields lists the remaining details some providers request: the Name ID format, whether assertions and requests are signed, and the default RelayState.

After you save a SAML connection, an **SP metadata URL** appears alongside these values. Most identity providers can import this address to fill in the other values automatically if you need to reconfigure.

People start sign-in from Claude Desktop (**Sign in with your organization**) or from the web portal in a browser, and Claude for Government then sends them to your identity provider. Starting from the application's tile in your provider's app portal (such as Microsoft My Apps), or from a sign-in test in your provider's admin console, is not supported.

### Connecting with OIDC

If your identity provider supports OpenID Connect, fill in the OIDC section:

* **Client ID** is the application ID your identity provider assigned when you registered the app.
* **Client secret** is the secret your identity provider generated for that application. It is stored securely and never shown again after you save.
* **Authorization URL**, **Token URL**, **Issuer**, and **JWKS URL** are your identity provider's OIDC endpoints. Most providers show these on the application's overview or endpoints page, and some providers publish all four together on an OpenID Connect discovery document.

### Connecting with SAML

If your identity provider uses SAML, fill in the SAML section instead:

* **IdP metadata XML** is the federation metadata document for your identity provider. Download the XML file from your provider (in Microsoft Entra it's under Single sign-on → SAML → Federation Metadata XML; in ADFS it's under Endpoints) and paste the full document into the field. The metadata is read from what you paste; it is never fetched from a URL.

Once SAML is active, the card shows the Entity ID and SSO URL extracted from your metadata so you can confirm the connection is pointing where you expect.

### Attribute mapping (advanced)

Both the OIDC and SAML sections include an **Attribute mapping** panel that's collapsed by default. Open it if the email, first-name, or last-name fields arrive under different names than the defaults. Each field offers a short list of common names for your chosen protocol; you can pick one or type your own. For OIDC the defaults are the standard `email`, `given_name`, and `family_name` claims; for SAML the defaults cover the common attribute names most providers use. Leave a field blank to use its default.

<Warning>
  Saving a new single sign-on configuration takes effect immediately and applies to everyone, including you. Before saving, confirm you can authenticate with the new provider in another browser window so that you don't lock yourself out.
</Warning>

## SCIM provisioning

SCIM is the standard protocol identity providers use to push users and groups to a connected service automatically, so that accounts are created, updated, and deactivated in step with your agency's directory. Connecting SCIM is optional; without it, users are created the first time they sign in.

<Note>
  You need at least one verified domain before you can generate a SCIM token. Until then, **Generate token** is unavailable and a banner prompts you to verify a domain first.
</Note>

* **SCIM base URL** is the address your identity provider pushes user and group updates to. A copy button sits next to it. You'll paste this value into your identity provider's provisioning settings (Okta and Microsoft Entra call this the *Tenant URL*).

### SCIM secret token

Your identity provider authenticates to the SCIM address with a bearer token that you generate here. Click **Generate token** to create one, then paste the value into your identity provider's *Secret Token* (or equivalent) field.

<Warning>
  The full token value is shown **only once**, immediately after you create it. Copy it into your identity provider before clicking Done. If you lose the value, generate a new token and revoke the old one.
</Warning>

The token table lists every token with its created date, a short hint (the last few characters) so you can tell them apart, and a status of **Active** or **Revoked**. You can keep more than one token active at a time, which lets you rotate without an outage: generate a new token, update your identity provider to use it, confirm a sync succeeds, and then revoke the old one. Revoking a token takes effect immediately.

Once a token is active and your directory completes its first sync, the provisioning-rule list and the **Synced, not routed** waiting list become available further down the page.

## Directory groups

Once your identity provider has pushed groups over SCIM, they appear here with their member counts. Drag the groups into the order you want; this priority is used for group-level configuration on the [Config](/docs/government/config/overview#group-specific-settings) page.

## Routing rules

A **routing rule** is an instruction of the form "if a person matches this condition, place them in this organization." Routing rules are the **only** way a new person gets into your deployment; there is no default organization and no fallback.

Before any rule runs, the sign-in flow first checks that the person's email domain is one of your tenant's **verified domains** (listed in the Domains section above). An address outside your verified domains never reaches your tenant at all, regardless of what rules you've written.

There are two separate rule lists, because there are two ways a person can arrive:

* **Sign-in rules** run each time a person signs in through single sign-on. They apply on every sign-in, not just the first one, so changing a sign-in rule can move an existing member to a different organization the next time that person signs in.
* **Provisioning rules** run when your directory creates or updates someone through SCIM. They match on synced directory groups, and changes take effect at the next directory sync.

### When rules move people

Because sign-in rules run every time, a rule change has these effects on people who already exist:

* If a person now matches a rule that points to a different organization, they are moved on their next sign-in. Their active sessions and API keys are revoked as part of the move, so they land cleanly in the new organization.
* If a person no longer matches any rule (for example, you removed the only rule that covered them), they keep their current organization and can still sign in. The no-match refusal applies only to people who have never been placed.
* If a person's account is managed by your directory (that is, it was created or linked through SCIM), sign-in rules do **not** move them. Directory-managed accounts are moved only by provisioning rules, so that your directory remains the single source of truth for where they belong.

Because the Claude desktop app stores conversations on each person's own device, a move does not affect desktop chat history.

<Tip>
  When you add or edit a rule that would move people, a confirmation dialog shows how many existing members would be affected and a sample of their email addresses. Review that list before confirming.
</Tip>

> **For organization owners:** A member being moved out of your organization by a rule change loses their seat and role in your organization. Their account itself is kept, and they are reseated in the destination organization according to its available seats.

### Sign-in rules

Each sign-in rule reads as a sentence, for example *"Anyone with email domain `example.gov` → place in OEO."* A rule matches on one of the following:

* An **email domain** rule matches the domain of the user's email address exactly. You choose from your tenant's verified domains; you cannot type an arbitrary domain. Subdomains are not matched automatically, so `sub.example.gov` needs its own rule if you want it routed.
* An **identity provider (IdP) group** rule matches a value in the group membership list that your identity provider includes in the sign-in token. You type the exact value your provider sends, and matching is exact and case-sensitive.

Rules are evaluated from top to bottom, and the first match wins. When you have more than one rule, drag the handle next to a rule (or focus the handle and press the up or down arrow key) to reorder the list. Only one rule can exist for any given condition. If you pick a domain or group that already has a rule, a message below the form shows which organization it currently routes to and asks you to remove that rule first.

Each rule shows a status line with diagnostics:

* **Last matched** (or **Never matched**) tells you when the rule most recently placed or moved someone.
* A **matches broadly** badge marks a domain rule that sits above one or more group rules. Because it matches everyone on that domain, group rules below it can never win for those users; move it lower if that's not what you intended.
* A **target deactivated** badge means the rule points at an organization that has been deactivated. The rule is skipped during evaluation.
* A **stale value** badge means the condition refers to something that no longer exists, such as a domain removed from your verified list. The rule is skipped during evaluation.

### Provisioning rules (SCIM)

<Note>
  This section only appears when SCIM is connected (you have an active SCIM token or your directory has synced groups) or when provisioning rules already exist.
</Note>

Provisioning rules match on **directory groups** that your identity provider has synced, and decide which organization a user is placed in when your directory provisions or updates them. You choose groups from the synced list; a group that hasn't synced yet won't appear in the picker.

Provisioning rules work the same way as sign-in rules: they're an ordered list, the first match wins, and only one rule can exist per group. Because your directory re-evaluates placement on each sync, reordering or removing provisioning rules can move already-placed users at the next sync. You'll be asked to confirm before reordering.

### Adding and removing rules

To add a rule, choose the match type (for sign-in rules), pick or type the value, choose the target organization, and click **Add rule**. New rules are added at the bottom of the list; reorder after adding if you need a different priority.

To remove a rule, click **Remove** next to it and confirm. Removing the last sign-in rule is called out specifically: no new person can sign in until another rule is added, and existing members keep their current organization until another rule covers them.

## Preview routing

Enter an email address (and, optionally, a comma-separated list of IdP groups) to see exactly how that person would be routed, without changing anything. The preview runs the same evaluation that real sign-in and provisioning use, so what you see here is what will actually happen.

The result shows one panel for sign-in and a separate panel for directory provisioning.

<Note>
  The directory provisioning panel only appears when SCIM is connected for your tenant.
</Note>

Each panel shows whether the person would be placed (and in which organization) or refused, and it lists every rule in order with the outcome for each: **matched**, **no match**, or **target deactivated**. If the email's domain isn't one of your tenant's verified domains, the preview explains that sign-in would never reach this tenant at all, and no rules are evaluated.

<Tip>
  Editing any rule clears the preview result automatically so you never read a verdict that's out of date. Re-run the preview after making changes.
</Tip>

## Unplaced users

The unplaced-users lists collect people who have arrived but aren't in an organization yet. There are two kinds of entry:

* **Rejected sign-ins** are people from one of your verified domains who tried to sign in but matched no rule and were turned away. Each entry shows who tried, when they last tried, how many times, and which IdP groups their sign-in token carried. These records are kept so you can see who's trying and failing to get in.
* **Synced, not routed** entries are people your directory has provisioned through SCIM who don't yet match any provisioning rule. They exist in the sync but have not been placed in an organization, so they cannot sign in.

<Note>
  The Rejected sign-ins list only appears when at least one sign-in has been turned away. The Synced, not routed list appears inside the provisioning-rules card and only when at least one provisioned user is waiting without a matching rule.
</Note>

For rejected sign-ins you can do the following:

* Click **Test in preview** to load that person's email and recorded groups into the preview, so you can see exactly which rule would cover them before you add one.
* Click **Clear** to delete the record, or **Clear all** to remove every entry. Clearing does not block the person; a fresh entry appears if they try again.

For synced, not routed entries, add a provisioning rule that covers their group. They'll be placed automatically at the next directory sync; there is nothing to clear.

Once a person is successfully placed (by signing in through a matching rule or by the next directory sync), their entries in these lists are cleaned up automatically.

## Things to know

* Keep the DNS TXT record in place while you are using Claude for Government.
* There is no local break-glass account or stored password. When single sign-on is unavailable, Primary Owners and tenant administrators can request an emailed single-use sign-in link from the sign-in page.
* SCIM provisioning is configured entirely from this page, with no action needed from Anthropic. Use **Generate token** under [SCIM provisioning](#scim-provisioning) on this page to create a bearer token, then enter it along with the SCIM base URL shown there into your identity provider's provisioning settings.
* If two administrators reorder the same rule list at the same time, the second save is rejected with a message that the rules changed in another session. The list refreshes so you can review the current order and try again.
* A user who was previously deactivated cannot regain access by matching a rule; they are refused with a deactivated-user reason instead.
* For users managed by your directory, the email address shown in Claude for Government is kept in step with your directory. The sign-in token's email is ignored for those users so that a provider that sends different values in different fields (a common quirk in Microsoft Entra) does not bounce the address back and forth.
