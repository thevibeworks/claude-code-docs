# Claim and migrate accounts on your domain

Domain claiming lets Enterprise admins discover, claim, and migrate existing personal Claude accounts (Free, Pro, and Max) on a verified company domain into their Enterprise workspace. This gives your organization a clean path to consolidate accounts on day one of an Enterprise deployment, and allows people using Claude on personal accounts to keep their work. Domain claiming is available for Enterprise plans, whether purchased directly through Anthropic or through the AWS Marketplace, and works the same in both cases.

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

After verifying your domain, you can view all existing personal accounts (Free, Pro, and Max) on that domain that aren’t already in your organization. For each account, you’ll see the email address, plan type, account creation date, and last active date. You can also export this list as a CSV.

Use this view to understand the scope of migration before initiating a claim. Check which accounts are in your identity provider (IdP) and which aren’t—people not in the IdP won’t be able to sign in after migration unless you add them.

### Enable domain capture

Navigate to **[Organization settings > Organization and access](http://claude.ai/admin-settings/organization)**, scroll down to **Security** and toggle **Migrate accounts using your domain** on to enable domain capture. This is an organization-level setting that enforces a policy: no non-Enterprise accounts can exist on your verified domain.

**Warning:** Domain capture is a one-way door. Once enabled, it can’t be reversed. The admin UI will display a prominent confirmation before you proceed. Make sure your prerequisites are fully in place and you’ve reviewed the affected accounts before enabling.

### Initiate the claim

When you enable domain capture, you’ll walk through a flow that shows you the migration impact:

- A preview of all accounts that will be affected (with CSV export)

- Which accounts are in your IdP and which aren’t

- Warnings about any potential issues

Once confirmed, all affected accounts receive notification immediately—both by email and through an in-product banner. The migration window is 30 days from the date you initiate the claim.

### The 30-day migration window

The migration deadline is a single org-wide date, not a rolling per-user timer. All affected accounts share the same deadline.

During this window, each person on the domain can sign in and choose how to migrate:

- **Merge and join:** Bring existing chats, projects, files, and memory into a new account within your Enterprise workspace. See the full list: **[What moves when you migrate](https://support.claude.com/en/articles/9267400-move-your-personal-claude-account-to-a-team-or-enterprise-organization#h_4e63ef6e87)**.

- **Join fresh:** Start with a clean Enterprise account.

### What happens at the deadline

- Any remaining personal accounts that haven’t been migrated are deactivated.

- Paid subscriptions (Pro and Max) are automatically canceled with a prorated refund. Any usage credits remaining on the account will also be refunded.

- Once all accounts are migrated or deactivated, no personal accounts exist on your domain.

- People who don’t choose before the deadline are given a fresh Enterprise account by default and their data will be emailed to them, but their personal account will not be accessible.

New accounts created on the domain after domain capture is enabled go directly through SSO and your Enterprise workspace—no personal account is created.

## What’s not supported

- Claiming Team plan accounts. Only individual accounts (Free, Pro, Max) can be claimed.

- Setting a custom migration deadline. The window is always 30 days.

- Canceling App Store subscriptions. People who purchased Pro or Max through the Apple App Store need to cancel their subscription themselves through their Apple ID settings. For details, see **[Respond to an Enterprise domain claim on your Claude account](https://support.claude.com/en/articles/14625626)**.

## SSO and provisioning sequencing

Domain claiming integrates with your existing SSO and provisioning setup:

- **If SSO is already enforced:** After an organization admin enables a claim for all personal Claude accounts using their verified domain, users will see a banner upon logging into their personal accounts and receive an email telling them to migrate. If a user is not added to your organization’s IdP, they will be locked out, so admins should ensure any users who need access are added before enabling a claim.

- **SCIM and JIT:** If SCIM is enabled, provisioned accounts are linked to migrated accounts by email match. Don’t enable SCIM and JIT provisioning simultaneously—SCIM takes precedence if both are active.

**Important:** To prevent lockouts, make sure all affected users are in your IdP before the migration deadline. Anyone not in the IdP won’t be able to sign in to the Enterprise workspace, and their personal account will be deactivated at the 30-day deadline. Your IT team will need to add them to the IdP.

---

## Frequently asked questions

### What happens if my organization doesn’t have enough seats available for migrated users?

If you purchased your Enterprise plan directly through Anthropic, you'll see an error message in organization settings prompting you to **[buy more seats](https://support.claude.com/en/articles/13393991-purchase-and-manage-seats-on-enterprise-plans)**.

If you purchased your Enterprise plan through the AWS Marketplace, migrated users will see a message asking them to contact their admin when they try to log in after the migration.