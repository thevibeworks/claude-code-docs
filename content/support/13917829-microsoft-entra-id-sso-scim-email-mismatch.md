Title: Microsoft Entra ID SSO/SCIM email mismatch

URL Source: https://support.claude.com/en/articles/13917829-microsoft-entra-id-sso-scim-email-mismatch

Markdown Content:
Claude uses email as the primary identifier to match SSO logins to provisioned seats. In Microsoft Entra ID, SCIM provisioning and SSO authentication are configured in _separate places_ and can pull email from different user attributes—causing a mismatch that blocks access. This guide walks through how to identify the problem, fix the attribute mapping, and clean up any side effects.

## Symptoms

People may experience one or more of the following when attempting to access your organization via SSO:

## How this happens

Microsoft Entra ID user accounts have multiple email-like attributes that can hold _different values_. SCIM provisioning and SSO authentication are configured in separate admin areas and each can pull from a different attribute:

**Entra attribute****Typical value****Commonly used by**
`userPrincipalName``[email protected]` (may be employee ID format)Default SCIM userName mapping
`mail``[email protected]` (standard email)OIDC / SAML email claim
`proxyAddresses``SMTP:[email protected]`Exchange / M365 primary address
`otherMails`May contain aliases or secondary addresses Alternative contact emails

The mismatch occurs when SCIM pulls email from one attribute while SSO sends the email from another. Even a subtle difference blocks access—Claude requires an **exact string match**.

**Common confusion:** Entra has two separate admin areas. The **SCIM provisioning app** lives under **Enterprise applications** (Microsoft's term for integrated apps—unrelated to your Claude plan). The **SSO/OIDC app** lives under **App registrations**. IT admins frequently navigate to the wrong location.

## Diagnostic steps

### Step 1 — Confirm the mismatch

### Step 2 — Identify the scope

### Step 3 — Check the OIDC token claims (OIDC apps only)

## Resolution

### Fix the SCIM attribute mapping

Navigate to the **SCIM provisioning app** — not the SSO/OIDC app:

### Trigger a full provisioning sync

**Full sync required — incremental won't work.** You must trigger a **full restart** of the provisioning cycle.

## Post-fix cleanup

After correcting the attribute mapping and completing the full sync:

## Verification

## Common issues

**Issue****Solution**
SCIM mapping updated but SSO claim not checked (or vice versa)Both must be updated. SCIM under **Enterprise applications → Provisioning**; SSO claims under **Single sign-on → Attributes & Claims** or **App registrations → Token configuration**.
userPrincipalName is in employee-ID format, not a real email Switch SCIM to use the mail attribute instead.
Incremental sync runs but emails don't update**Restart provisioning** is required after an attribute mapping change.
OIDC app email claim not configured as an optional claim Add email under **App registrations → Token configuration**.
Emails updated but person still can't log in Look for rogue free orgs or ghost accounts. Clear browser cookies and retry.

## When to contact Support

Contact **[our Support team](https://support.claude.com/en/articles/9015913)** with your organization's domain, the affected person's email, and attribute mapping screenshots when:

* * *

Related Articles

[Google Workspace SSO/SCIM email mismatch](https://support.claude.com/en/articles/13917817-google-workspace-sso-scim-email-mismatch)[Okta SSO/SCIM email mismatch](https://support.claude.com/en/articles/13917840-okta-sso-scim-email-mismatch)[OneLogin SSO/SCIM email mismatch](https://support.claude.com/en/articles/13917861-onelogin-sso-scim-email-mismatch)[Ping Identity SSO/SCIM email mismatch](https://support.claude.com/en/articles/13917875-ping-identity-sso-scim-email-mismatch)[Microsoft Entra ID SSO setup](https://support.claude.com/en/articles/13917889-microsoft-entra-id-sso-setup)
