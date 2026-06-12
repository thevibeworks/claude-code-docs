Title: Google Workspace SSO/SCIM email mismatch

URL Source: https://support.claude.com/en/articles/13917817-google-workspace-sso-scim-email-mismatch

Markdown Content:
1.   [All Collections](https://support.claude.com/en/)
2.   [Identity management (SSO, JIT, SCIM)](https://support.claude.com/en/collections/17270717-identity-management-sso-jit-scim)
3.   [Troubleshooting by identity provider](https://support.claude.com/en/collections/19039143-troubleshooting-by-identity-provider)
4.   Google Workspace SSO/SCIM email mismatch

March 24, 2026

Table of contents

Claude uses email as the primary identifier to match SSO logins to provisioned seats. In Google Workspace, SCIM auto-provisioning and SAML SSO can send different email values—especially when people have email aliases—causing a mismatch that blocks access.

## Symptoms

People may experience one or more of the following when attempting to access your organization via SSO:

## How this happens

Google Workspace accounts have a primary email and may have multiple aliases. SCIM provisioning and SAML SSO are configured separately in the Google Admin console and can pull from different address fields:

**Google attribute****Typical value****Commonly used by**
`primaryEmail``[email protected]`Recommended for both SCIM and SAML
Email aliases`[email protected]`, `[email protected]`Sometimes mapped by mistake in SCIM
Custom schema fields Custom attributes defined per org Advanced attribute mappings
Organization unit email OU-derived address variants Rarely, in complex org structures

The most common mismatch: SCIM is configured to send an alias address while SAML sends the primary email (or vice versa). Since aliases and primary emails are different strings, Claude cannot match them. Claude requires an **exact string match**.

**Common confusion:** In Google Admin, SCIM auto-provisioning settings and SAML attribute mapping are on separate tabs within the same app. Admins sometimes update one and miss the other. Verify both locations.

## Diagnostic steps

### Step 1 — Confirm the mismatch

### Step 2 — Identify the scope of the problem

### Step 3 — Check Name ID in SAML configuration

## Resolution

### Align both mappings to primaryEmail

Google Workspace's primaryEmail is the most reliable source for both SCIM and SAML.

### Trigger a full re-sync

**Critical — Full sync required:** An incremental sync will _not_ update existing records after you change an attribute mapping. You must trigger a **full restart** of the provisioning cycle.

## Post-fix cleanup

After correcting the attribute mapping and completing the full sync:

## Verification

## Common issues

**Issue****Solution**
SCIM sends an alias while SAML sends the primary email Always use `primaryEmail` for both.
Name ID in SAML settings was not checked The Name ID field determines the email sent at login. This is separate from the attribute mapping section. Check both.
Custom schema field is blank for some people Stick to standard Google attributes like `primaryEmail`.
Reprovisioning doesn't trigger automatically after mapping change You may need to manually suspend and re-enable provisioning to force a full sync.
Someone's primary email changed but the old email still appears in Claude A full re-sync is needed after primary email changes.
Emails updated in SCIM but person still can't log in Check for rogue free orgs or ghost accounts. Clear browser cookies and retry.

## When to contact Support

Contact **[our Support team](https://support.claude.com/en/articles/9015913)** with your organization's domain, the affected person's email, and screenshots of your attribute mappings when:

* * *

Related Articles

[Microsoft Entra ID SSO/SCIM email mismatch](https://support.claude.com/en/articles/13917829-microsoft-entra-id-sso-scim-email-mismatch)[Okta SSO/SCIM email mismatch](https://support.claude.com/en/articles/13917840-okta-sso-scim-email-mismatch)[OneLogin SSO/SCIM email mismatch](https://support.claude.com/en/articles/13917861-onelogin-sso-scim-email-mismatch)[Ping Identity SSO/SCIM email mismatch](https://support.claude.com/en/articles/13917875-ping-identity-sso-scim-email-mismatch)[Google Workspace SSO setup](https://support.claude.com/en/articles/13917884-google-workspace-sso-setup)
