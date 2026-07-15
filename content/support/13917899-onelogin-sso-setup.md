# OneLogin SSO setup

This guide walks through configuring SSO and SCIM for Claude with OneLogin as your identity provider. It applies to Team plans, Enterprise plans, and Console organizations.

## Prerequisites

- A Claude Team plan, Enterprise plan, or Console organization with a parent organization (see **[Important considerations before enabling SSO](https://support.claude.com/en/articles/10276682)** for Console parent org requirements)

- Owner or Primary Owner role (Team and Enterprise) or Admin role (Console)

- OneLogin Super User access

- Your domain verified in Claude's Identity and access settings — see **[Set up single sign-on](https://support.claude.com/en/articles/13132885)** for the full setup path including domain verification

## Where to find your configuration values

The Audience (Entity ID), ACS URL, and SCIM credentials referenced below are provided in the WorkOS setup flow within your Identity and access settings — not by contacting Support.

- **Team and Enterprise plans:** go to **[claude.ai/admin-settings/identity](https://claude.ai/admin-settings/identity)**

- **Console organizations:** go to **[platform.claude.com/settings/identity](https://platform.claude.com/settings/identity)**

Start the SSO setup flow there and keep it open alongside the OneLogin Admin portal as you work through the steps below.

---

## Step 1 — Create a new application in OneLogin

1. In the OneLogin Admin portal, go to **Applications → Applications → Add App**.

2. Search for "SAML Custom Connector" and select "SAML Custom Connector (Advanced)."

3. Name it "Claude" and click "Save."

## Step 2 — Configure SAML settings

1. In the **Configuration** tab, enter the values from the WorkOS setup flow: **Audience (EntityID)**, **ACS (Consumer) URL**, and **ACS URL Validator** (regex or exact match of the ACS URL).

2. Set **SAML initiator** to **Service Provider**.

3. Set **SAML nameID format** to **Email**.

4. In the **SSO** tab, download the **Issuer URL** metadata and upload it in the WorkOS setup flow when prompted.

## Step 3 — Map attributes

1. In the **Parameters** tab, add a field: **Field name:** email, **Value:** Email (OneLogin's Email field for the person).

2. Ensure this same Email field is used for SCIM provisioning in the next step.

## Step 4 — Enable SCIM provisioning

**Note:** SCIM provisioning is available on Enterprise plans and eligible Console organizations only. If you're on a Team plan, skip this step — you can use JIT provisioning instead. See **[Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195)**.

1. In the **Provisioning** tab, enable **Enable provisioning**.

2. Enter the SCIM Base URL and Bearer Token from the WorkOS setup flow.

3. Enable **Create user**, **Delete user**, and **Update user**.

4. In **Entitlements**, map the email attribute to the same OneLogin field as SAML.

5. Click "Save."

**Critical:** SAML and SCIM must send the same email value. If people experience login failures after provisioning, see **[OneLogin SSO/SCIM email mismatch](https://support.claude.com/en/articles/13917861)**.

## Step 5 — Assign people

In the **Users** tab, assign individual people or use **Rules** to automatically assign based on role or group.

## Step 6 — Verify

1. If you enabled SCIM, check the OneLogin provisioning activity log to confirm people were created in Claude.

2. Have a test user complete SSO login and verify they land in your organization's workspace.

---

## Need help?

See **[Set up single sign-on](https://support.claude.com/en/articles/13132885)** for the full end-to-end flow including domain verification and choosing a provisioning approach. If you run into issues, contact **[our Support team](https://support.claude.com/en/articles/9015913)** with your OneLogin domain and a screenshot of your SAML configuration.