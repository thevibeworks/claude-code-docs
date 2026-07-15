# Okta SSO setup

This guide covers configuring SSO and SCIM provisioning for Claude with Okta as your identity provider. It applies to Team plans, Enterprise plans, and Console organizations.

## Prerequisites

- A Claude Team plan, Enterprise plan, or Console organization with a parent organization (see **[Important considerations before enabling SSO](https://support.claude.com/en/articles/10276682)** for Console parent org requirements)

- Owner or Primary Owner role (Team and Enterprise) or Admin role (Console)

- Okta administrator access

- Your domain verified in Claude's Identity and access settings — see **[Set up single sign-on](https://support.claude.com/en/articles/13132885)** for the full setup path including domain verification

## Where to find your configuration values

The ACS URL, Entity ID, and SCIM credentials referenced below are provided in the WorkOS setup flow within your Identity and access settings.

- **Team and Enterprise plans:** go to **[claude.ai/admin-settings/identity](https://claude.ai/admin-settings/identity)**

- **Console organizations:** go to **[platform.claude.com/settings/identity](https://platform.claude.com/settings/identity)**

Start the SSO setup flow there and keep it open alongside the Okta Admin console as you work through the steps below.

---

## Step 1 — Create the Okta application

1. In the Okta Admin console, go to **Applications → Applications → Create App Integration**.

2. For the SSO method, choose "SAML 2.0" (recommended) or "OIDC."

3. Name the app "Claude" and click "Next."

## Step 2 — Configure SAML

1. In the **Configure SAML** tab, enter: **Single sign-on URL (ACS URL)** from the WorkOS setup flow, **Audience URI (Entity ID)** from the WorkOS setup flow, **Name ID format:** EmailAddress, and **Application username:** Email.

2. Under **Attribute Statements**, add an attribute named email with value user.email.

3. Download the **Identity Provider metadata** XML and upload it in the WorkOS setup flow when prompted.

## Step 3 — Enable SCIM provisioning

**Note:** SCIM provisioning is available on Enterprise plans and eligible Console organizations only. If you're on a Team plan, skip this step—you can use JIT provisioning instead. See **[Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195)**.

1. In the app, go to the **Provisioning** tab and click “Configure API Integration.”

2. Check **Enable API integration** and enter the SCIM Base URL and API Token from the WorkOS setup flow.

3. Click “Test API credentials” to verify, then save.

4. Under **To App**, enable **Create Users**, **Update User Attributes**, and **Deactivate Users**.

5. In **Attribute Mappings → To App**, confirm the email attribute maps to user.email — the same field as your SAML assertion.

**Important:** SCIM and SAML must use the same Okta field for email. A common issue is SCIM using user.login while SAML uses user.email. See **[Okta SSO/SCIM email mismatch](https://support.claude.com/en/articles/13917840)** if people can't log in after provisioning.

## Step 4 — Assign people or groups

1. In the **Assignments** tab, assign the people or Okta groups that should access Claude.

2. If you enable SCIM, Okta will automatically provision assigned people. If you're using JIT, people will be provisioned on their first SSO login.

## Step 5 — Verify

1. If you enabled SCIM, check provisioning logs to confirm people were successfully created in Claude.

2. Have a test user complete SSO and verify they land in your organization's workspace.

---

## Need help?

For the full end-to-end flow including domain verification and choosing a provisioning approach, see **[Set up single sign-on](https://support.claude.com/en/articles/13132885)**. If you run into issues, contact **[our Support team](https://support.claude.com/en/articles/9015913-how-to-get-support)** with your organization's domain and a screenshot of your Okta SAML configuration.