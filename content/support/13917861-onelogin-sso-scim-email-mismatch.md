Title: OneLogin SSO/SCIM email mismatch

URL Source: https://support.claude.com/en/articles/13917861-onelogin-sso-scim-email-mismatch

Markdown Content:
1.   [All Collections](https://support.claude.com/en/)
2.   [Identity management (SSO, JIT, SCIM)](https://support.claude.com/en/collections/17270717-identity-management-sso-jit-scim)
3.   [Troubleshooting by identity provider](https://support.claude.com/en/collections/19039143-troubleshooting-by-identity-provider)
4.   OneLogin SSO/SCIM email mismatch

March 24, 2026

Table of contents

Claude uses email as the primary identifier to match SSO logins to provisioned seats. In OneLogin, SCIM provisioning and SAML SSO are configured in separate tabs of the app and can reference different user profile fields, causing a mismatch that blocks access.

## Symptoms

People may experience one or more of the following when attempting to access your organization via SSO:

## How this happens

OneLogin user profiles contain distinct fields for username and email, which may hold different values. SCIM provisioning parameters and SAML attribute statements are configured independently and can each pull from a different field:

**OneLogin field****Typical value****Commonly used by**
`Username``testuser1` or [`[email protected]`](https://support.claude.com/cdn-cgi/l/email-protection#f68293858283859384c7b6938e979b869a93d895999b)Sometimes used in SCIM userName mapping
`Email`[`[email protected]`](https://support.claude.com/cdn-cgi/l/email-protection#01756472752f747264732f6e6f64416479606c716d642f626e6c)Recommended for both SCIM and SAML
`Login Name`May differ from email if SSO is used for non-email logins Legacy or custom configurations
Custom user fields Custom attributes defined per org Advanced attribute mappings

A common mismatch: the SCIM parameters tab maps the email attribute to Username (which may be an employee ID or short name) while the SAML attribute statement sends the Email field. Claude requires an **exact string match**.

**Common confusion:** OneLogin's SCIM parameters and SAML attribute statements are in different tabs of the same app — **Parameters** for SCIM and **SSO** (or **Parameters** with SAML-specific fields) for SSO. Both must be checked and aligned.

## Diagnostic steps

## Step 1 — Confirm the mismatch

## Step 2 — Identify the scope of the problem

## Step 3 — Review user field values

## Resolution

## Align both mappings to the Email field

OneLogin's Email field is the most reliable source for both SCIM and SAML, as it's designed to hold a valid email address.

## Trigger a full re-sync

**Critical — Full sync required:** An incremental sync will _not_ update existing records after you change an attribute mapping. You must trigger a **full restart** of the provisioning cycle.

## Post-fix cleanup

After correcting the attribute mapping and completing the full sync:

## Verification

## Common issues

**Issue****Solution**
Username field holds a short name or employee ID, not an email Switch SCIM to use the **Email** field.
SAML attributes updated but SCIM parameters were not changed Both the Parameters tab (for SCIM) and the SSO/SAML attributes must be updated independently.
Re-sync doesn't appear to trigger Try removing and re-assigning affected people from the app.
Custom user fields are mapped but blank for some people Switch to the standard **Email** field.
Emails updated in SCIM but person still can't log in Check for rogue free orgs or ghost accounts. Clear browser cookies and retry.
"Invite domain not allowed" when trying to re-add people Your organization's domain may not be verified in Claude. Contact Support.

## When to contact Support

Contact **[our Support team](https://support.claude.com/en/articles/9015913)** with your organization's domain, the affected person's email, and screenshots of your attribute mappings when:

* * *

Related Articles

[Google Workspace SSO/SCIM email mismatch](https://support.claude.com/en/articles/13917817-google-workspace-sso-scim-email-mismatch)[Microsoft Entra ID SSO/SCIM email mismatch](https://support.claude.com/en/articles/13917829-microsoft-entra-id-sso-scim-email-mismatch)[Okta SSO/SCIM email mismatch](https://support.claude.com/en/articles/13917840-okta-sso-scim-email-mismatch)[Ping Identity SSO/SCIM email mismatch](https://support.claude.com/en/articles/13917875-ping-identity-sso-scim-email-mismatch)[OneLogin SSO setup](https://support.claude.com/en/articles/13917899-onelogin-sso-setup)
