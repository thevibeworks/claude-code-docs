Title: Okta SSO/SCIM email mismatch

URL Source: https://support.claude.com/en/articles/13917840-okta-sso-scim-email-mismatch

Markdown Content:
Claude uses email as the primary identifier to match SSO logins to provisioned seats. In Okta, SCIM provisioning and SSO are configured separately and can pull email from different user profile fields. This guide explains how to identify and resolve the mismatch.

## Symptoms

People may experience one or more of the following when attempting to access your organization via SSO:

## How this happens

Okta user profiles contain multiple fields that represent identity. SCIM provisioning (under **Provisioning → To App**) and SAML/OIDC SSO (under **Sign On**) are configured independently.

**Okta attribute****Typical value****Commonly used by**
`user.login``testuser1` or [`testuser1@example.com`](mailto:testuser1@example.com)Default SCIM userName mapping; sometimes NameID
`user.email`[`test.user.one@example.com`](mailto:test.user.one@example.com)SAML/OIDC email claim (recommended)
`appuser.email`App-level override of user email Custom app-level attribute mapping

A common mismatch: SCIM uses `user.login` while SAML sends `user.email`. Claude requires an exact string match.

**Common confusion:** Okta's SCIM attribute mappings and SAML attribute statements live in two different tabs — **Provisioning → To App** for SCIM, and **Sign On** for SSO.

## Diagnostic steps

### Step 1 — Confirm the mismatch

### Step 2 — Identify the scope of the problem

### Step 3 — Verify Okta user profiles directly

## Resolution

### Align both mappings to the same Okta field

The safest fix is to use `user.email` for both SCIM and SSO, as this field contains the canonical email address in Okta.

### Force a full re-sync

**Critical — Full sync required:** An incremental sync will not update existing records after you change an attribute mapping.

## Post-fix cleanup

After correcting the attribute mapping and completing the full sync:

## Verification

After completing the fix and any cleanup:

## Common issues

**Issue****Solution**
Admin updates SAML claims but forgets SCIM attribute mappings (or vice versa)Both must be updated. SCIM mappings under **Provisioning → To App**; SAML claims under **Sign On → SAML Settings**.
`user.login` contains a username (not email) for some people Switch both to `user.email` and verify email fields are populated for everyone.
Incremental sync runs but emails don't update**Force Sync** or **Push Users** is required after an attribute mapping change.
App-level profile attribute (`appuser.email`) differs from user profile (`user.email`)Check if app-level attribute mappings override user profile values.
Emails updated but person still can't log in Look for rogue free orgs or ghost accounts. Clear browser cookies and retry. Contact Support if it persists.
OIDC and SAML apps are separate Okta apps for Claude Some organizations configure both. Ensure attribute alignment in both apps.

## When to contact Support

Contact **[our Support team](https://support.claude.com/en/articles/9015913)** with your organization's domain, the affected person's email, and attribute mapping screenshots when:

* * *

Related Articles

[Google Workspace SSO/SCIM email mismatch](https://support.claude.com/en/articles/13917817-google-workspace-sso-scim-email-mismatch)[Microsoft Entra ID SSO/SCIM email mismatch](https://support.claude.com/en/articles/13917829-microsoft-entra-id-sso-scim-email-mismatch)[OneLogin SSO/SCIM email mismatch](https://support.claude.com/en/articles/13917861-onelogin-sso-scim-email-mismatch)[Ping Identity SSO/SCIM email mismatch](https://support.claude.com/en/articles/13917875-ping-identity-sso-scim-email-mismatch)[Okta SSO setup](https://support.claude.com/en/articles/13917894-okta-sso-setup)
