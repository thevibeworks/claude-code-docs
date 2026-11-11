# Claim and migrate accounts on your domain

Domain claiming lets Enterprise admins discover and claim existing personal Claude accounts (Free, Pro, Max, and Ultra) on a verified company domain. Each person then chooses whether to bring what they can into your Enterprise workspace.

This gives your organization a clean path to consolidate accounts on day one of an Enterprise deployment, and allows people using Claude on personal accounts to bring much of their work with them. Domain claiming is available for Enterprise plans, whether purchased directly through Anthropic or through the AWS Marketplace, and works the same in both cases.

Domain claiming is supported on Claude Enterprise plans only.

Team plans can verify a domain and block new personal accounts from being created, but admins can't claim or migrate existing accounts. People on a Team plan can still migrate their own personal accounts voluntarily—see **[Move your personal Claude account to a Team or Enterprise organization](https://support.claude.com/en/articles/9267400)**.

---

## Prerequisites

Before you can enable domain claiming, your organization must have all of the following in place:

1. Restrict organization creation on your verified domain.

2. Complete domain verification (DNS).

3. Enforce SSO (not just configured—SSO must be actively enforced). See **[Set up single sign-on (SSO)](https://support.claude.com/en/articles/13132885-set-up-single-sign-on-sso)**.

4. Enable JIT provisioning or SCIM. See **[Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195-set-up-jit-or-scim-provisioning)**.

These prerequisites exist to prevent people from being locked out of Claude during the migration process. If SSO is enforced and provisioning is active, everyone on your domain will have a path to sign in after their accounts are migrated.

---

## How domain claiming works

### Review accounts on your domain

After verifying your domain, you can view all existing personal accounts (Free, Pro, Max, and Ultra) on that domain that aren’t already in your organization. For each account, you’ll see the email address, plan type, account creation date, and last active date. You can also export this list as a CSV.

Use this view to understand the scope of migration before initiating a claim. Check which accounts are in your identity provider (IdP) and which aren’t—people not in the IdP won’t be able to sign in after migration unless you add them.

### Enable domain capture

Navigate to **[Organization settings > Organization and access](https://claude.ai/admin-settings/organization)**, scroll down to **Security** and toggle **Migrate accounts using your domain** on to enable domain capture. This is an organization-level setting that enforces a policy: no non-Enterprise accounts can exist on your verified domain.

**Warning:** Domain capture is a one-way door. Once enabled, it can’t be reversed. The admin UI will display a prominent confirmation before you proceed. Make sure your prerequisites are fully in place and you’ve reviewed the affected accounts before enabling.

### Initiate the claim

When you enable domain capture, you’ll walk through a flow that shows you the migration impact:

- A preview of all accounts that will be affected (with CSV export)

- Which accounts are in your IdP and which aren’t

- Warnings about any potential issues

Once confirmed, all affected accounts receive notification immediately—both by email and through an in-product banner. The migration window is 30 days from the date you initiate the claim. A claim applies to every personal account on all the domains verified when you start it. Claude Console organizations and API access aren’t affected.

### The 30-day migration window

The migration deadline is a single date for the claim, not a rolling per-user timer. Every account covered by the claim shares that deadline. If you claim an additional domain later, that claim gets its own 30-day window (see **[Add a domain after you've started a claim](#h_d7ccebb0ac)** below).

During this window, each person on the domain can sign in and choose how to migrate:

- **Bring what you can:** Bring existing chats, projects, files, and memory into your Enterprise workspace. Not everything can move. See the full list: **[What moves when you migrate](https://support.claude.com/en/articles/9267400-move-your-personal-claude-account-to-a-team-or-enterprise-organization#h_4e63ef6e87)**. Each person needs a seat in your organization to bring their data.

- **Start fresh:** Their existing data won’t move to your Enterprise workspace. Their personal account closes, and its data will be deleted, per our data retention practices. Learn more about **[how long Anthropic stores your data](https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data)**.

### What happens at the deadline

- Any remaining personal accounts that haven’t been migrated are closed and will be deleted, along with their data, per our **[data retention practices](https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data)**.

- Paid subscriptions (Pro, Max, and Ultra) bought directly from us are automatically canceled with a prorated refund. For subscriptions bought through Google Play, we ask Google Play to cancel them and refund the unused time. People should check Google Play, and cancel there if their plan is still active. People who bought through the Apple App Store must cancel their own (see **[What’s not supported](#h_871e6bea9d)**). Any remaining credits people bought directly from us will also be refunded.

- Once all accounts are migrated or closed, no personal accounts exist on your domain. App Store subscribers’ accounts stay open for a few weeks after they move.

- People who don’t choose before the deadline are emailed a link to download their data. The link only opens if they can sign in, so before the deadline, make sure anyone who needs their data is in your IdP and can be added to your organization, with a seat available (see **[SSO and provisioning sequencing](#h_3eceece083)** below). To use Claude in your organization, they'll sign in with single sign-on (SSO). Ask people to export and download their data before the deadline: Claude for Teachers and FERPA-covered accounts don’t get a download link. For Claude for Teachers, they go to **[Organization settings > Data and privacy](https://claude.ai/admin-settings/data-privacy-controls)**. For FERPA-covered accounts, they go to **[Settings > Privacy](https://claude.ai/settings/data-privacy-controls)**. If they can’t export, they should **[contact Support](https://support.claude.com/en/articles/9015913-how-to-get-support#h_d6fc679aa4)** before the deadline.

New accounts created on the domain after domain capture is enabled go directly through SSO and your Enterprise workspace—no personal account is created.

### Add a domain after you've started a claim

Each claim covers the domains that were verified on your organization at the moment you initiated it. A domain you verify after starting a claim won't be added to the claim in progress, and accounts associated with that domain aren't notified or migrated as part of it.

To migrate accounts on a domain you verified later:

1. Wait for the current claim's 30-day window to end. Only one claim can be in progress at a time.

2. Verify the new domain if you haven't already. See **[Set up single sign-on (SSO)](https://support.claude.com/en/articles/13132885-set-up-single-sign-on-sso)**.

3. Review the accounts on the new domain, then initiate a new claim. This claim has its own 30-day window, and the accounts on the new domain receive the same email and in-product notifications.

**Note:** If you're onboarding several domains in phases, verify all of them before you initiate a claim when possible. That way, one claim and one deadline cover every account. Otherwise, each phase needs its own claim, and each claim has to finish its 30-day window before the next one can start.

## What’s not supported

- Migrating data into organizations with HIPAA readiness or customer-managed encryption keys (CMEK) turned on. You can still claim your domain, and people on it are notified as usual, but they can only start fresh. Nothing from their personal accounts moves over. Learn more about **[HIPAA-ready Enterprise plans](https://support.claude.com/en/articles/13296973)** and **[customer-managed encryption keys](https://support.claude.com/en/articles/15505325)**.

- Claiming Team plan accounts. Only individual accounts (Free, Pro, Max, Ultra) and, for schools and districts, individual Claude for Teachers accounts can be claimed.

- Setting a custom migration deadline.

- Canceling App Store subscriptions. People who purchased Pro, Max, or Ultra through the Apple App Store need to cancel their subscription themselves through their Apple ID settings. For details, see **[Respond to an Enterprise domain claim on your Claude account](https://support.claude.com/en/articles/14625626)**.

## SSO and provisioning sequencing

Domain claiming integrates with your existing SSO and provisioning setup:

- **If SSO is already enforced:** After an organization admin enables a claim for all personal Claude accounts using their verified domain, users will see a banner upon logging into their personal accounts and receive an email telling them to choose before the deadline. If a user is not added to your organization’s IdP, they will be locked out, so admins should ensure any users who need access are added before enabling a claim.

- **SCIM and JIT:** If SCIM is enabled, provisioned accounts are linked to migrated accounts by email match. Don’t enable SCIM and JIT provisioning simultaneously—SCIM takes precedence if both are active.

**Important:** To prevent lockouts, make sure all affected users are in your IdP before the migration deadline. Anyone not in the IdP won’t be able to sign in to the Enterprise workspace. Their personal account will still close at the 30-day deadline and will be deleted, along with its data, per our **[data retention practices](https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data)**. Your IT team will need to add them to the IdP.

---

## Frequently asked questions

### What happens if my organization doesn’t have enough seats available for migrated users?

If you purchased your Enterprise plan directly through Anthropic, you'll see an error message in organization settings prompting you to **[buy more seats](https://support.claude.com/en/articles/13393991-purchase-and-manage-seats-on-enterprise-plans)**.

If you purchased your Enterprise plan through the AWS Marketplace, migrated users will see a message asking them to contact their admin when they try to log in after the migration.