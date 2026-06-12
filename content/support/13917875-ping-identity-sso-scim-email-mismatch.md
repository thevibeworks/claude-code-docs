Title: Ping Identity SSO/SCIM email mismatch

URL Source: https://support.claude.com/en/articles/13917875-ping-identity-sso-scim-email-mismatch

Markdown Content:
1.   [All Collections](https://support.claude.com/en/)
2.   [Identity management (SSO, JIT, SCIM)](https://support.claude.com/en/collections/17270717-identity-management-sso-jit-scim)
3.   [Troubleshooting by identity provider](https://support.claude.com/en/collections/19039143-troubleshooting-by-identity-provider)
4.   Ping Identity SSO/SCIM email mismatch

March 24, 2026

Claude uses email as the primary identifier to match SSO logins to provisioned seats. Ping Identity products (PingOne and PingFederate) have flexible, layered attribute configuration. When SCIM provisioning and SAML/OIDC SSO pull from different user attributes, a mismatch blocks access.

## Symptoms

People may experience one or more of the following when attempting to access your organization via SSO:

## How this happens

Ping Identity products allow granular attribute mapping at multiple levels (directory, IdP adapter, SP connector, application). SCIM and SSO can each traverse different paths through these layers, resulting in different email values reaching Claude:

**Ping attribute****Typical value****Commonly used by**
`email` (PingOne)`test.user.one@example.com`Recommended for both SCIM and SAML/OIDC
`username` (PingOne)`testuser1` or `testuser1@example.com`Default login identifier; may differ from email
IdP adapter attribute (PingFederate)Varies by adapter type (LDAP, HTML Form, etc.)PingFederate identity sources
LDAP `mail` attribute`test.user.one@example.com`Directory-sourced email in PingFederate
LDAP `sAMAccountName` or uid May be employee ID or short username Sometimes mapped to email by mistake
Custom population attributes Custom fields defined per environment Advanced PingOne configurations

Claude requires an exact string match between the SCIM-provisioned email and the SSO-asserted email.

**PingFederate note:** PingFederate's attribute contract system is especially complex—email can pass through multiple layers (LDAP → IdP adapter → adapter contract → SP connector → assertion). A mismatch at any layer will cause the wrong value to reach Claude. Trace the value end-to-end.

## Diagnostic steps

### Step 1 — Confirm the mismatch (PingOne)

### Step 1 (alternate) — Confirm the mismatch (PingFederate)

### Step 2 — Identify the scope of the problem

### Step 3 — Check attribute values for a specific person

## Resolution

### PingOne — Align both mappings to the email attribute

### PingFederate — Align attribute contract across all layers

### Trigger a full re-sync

**Critical — Full sync required:** An incremental sync will not update existing records after you change an attribute mapping. You must trigger a **full restart** of the provisioning cycle.

## Post-fix cleanup

After correcting the attribute mapping and completing the full sync:

## Verification

## Common issues

**Issue****Solution**
PingOne `username` field used instead of `email`Switch the SCIM mapping to PingOne's **Email Address** attribute.
PingFederate attribute mismatch across contract layers Trace the email attribute end-to-end: LDAP source → IdP adapter → adapter contract → SP connector → assertion.
LDAP `sAMAccountName` or `uid` mapped as email source Use the LDAP `mail` attribute instead.
Incremental provisioning sync doesn't update existing records A full re-sync is required after changing attribute mappings.
Attribute contract updated in PingFederate but SCIM connector not updated Both SP connection and outbound SCIM provisioning channel must be updated independently.
Emails updated in SCIM but person still can't log in Check for rogue free orgs or ghost accounts. Clear browser cookies and retry.

## **When to contact Support**

Contact **[our Support team](https://support.claude.com/en/articles/9015913-how-to-get-support)** with your organization's domain, the affected person's email, and screenshots of your attribute mappings when:

* * *

Related Articles

[Google Workspace SSO/SCIM email mismatch](https://support.claude.com/en/articles/13917817-google-workspace-sso-scim-email-mismatch)[Microsoft Entra ID SSO/SCIM email mismatch](https://support.claude.com/en/articles/13917829-microsoft-entra-id-sso-scim-email-mismatch)[Okta SSO/SCIM email mismatch](https://support.claude.com/en/articles/13917840-okta-sso-scim-email-mismatch)[OneLogin SSO/SCIM email mismatch](https://support.claude.com/en/articles/13917861-onelogin-sso-scim-email-mismatch)[Ping Identity SSO setup](https://support.claude.com/en/articles/13917902-ping-identity-sso-setup)
