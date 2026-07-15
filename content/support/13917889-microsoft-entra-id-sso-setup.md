# Microsoft Entra ID SSO setup

This guide walks you through configuring single sign-on (SSO) for Claude using Microsoft Entra ID (formerly Azure Active Directory) as your identity provider. It applies to Team plans, Enterprise plans, and Console organizations.

## Prerequisites

- A Claude Team plan, Enterprise plan, or Console organization with a parent organization (see **[Important considerations before enabling SSO](https://support.claude.com/en/articles/10276682)** for Console parent org requirements)

- Owner or Primary Owner role (Team and Enterprise) or Admin role (Console)

- Microsoft Entra ID P1 or P2 license (required for SCIM provisioning)

- Global Administrator or Application Administrator role in Entra

- Your domain verified in Claude's Identity and access settings — see **[Set up single sign-on](https://support.claude.com/en/articles/13132885)** for the full setup path including domain verification

## Where to find your configuration values

The Entity ID, Reply URL (ACS URL), and SCIM credentials referenced below are provided in the WorkOS setup flow within your Identity and access settings — not by contacting Support.

- **Team and Enterprise plans:** go to **[claude.ai/admin-settings/identity](https://claude.ai/admin-settings/identity)**

- **Console organizations:** go to **[platform.claude.com/settings/identity](https://platform.claude.com/settings/identity)**

Start the SSO setup flow there and keep it open alongside the Entra Admin Center as you work through the steps below.

---

## Step 1 — Add Claude as an enterprise application in Entra

**Note:** "Enterprise applications" below refers to the section in Microsoft Entra's admin center—it's Microsoft's term for any app you integrate, and is unrelated to your Claude plan type.

1. In the **Entra Admin Center**, go to **Enterprise applications → New application**.

2. Search for "Claude" in the gallery. If available, select it; otherwise choose **Create your own application** and name it "Claude".

3. Select **Integrate any other application you don't find in the gallery** and click "Create."

## Step 2 — Configure SAML SSO

1. In your new application, click **Single sign-on → SAML**.

2. In **Basic SAML Configuration**, enter: **Identifier (Entity ID)** from the WorkOS setup flow, **Reply URL (ACS URL)** from the WorkOS setup flow, and **Sign-on URL:** **<https://claude.ai/login>**.

3. In **Attributes & Claims**, ensure the email claim is set to send user.mail (or the same attribute you'll use for SCIM).

4. Download the **Federation Metadata XML** and upload it in the WorkOS setup flow when prompted.

## Step 3 — Configure SCIM provisioning

**Note:** SCIM provisioning is available on Enterprise plans and eligible Console organizations only. If you're on a Team plan, skip this step — you can use JIT provisioning instead. See **[Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195)**.

1. In the application, go to **Provisioning → Get Started**.

2. Set **Provisioning Mode** to **Automatic**.

3. Enter the **Tenant URL** and **Secret Token** from the WorkOS setup flow.

4. Click **Test Connection** to verify.

5. Under **Mappings**, ensure the email attribute mapping points to the same field as your SSO email claim (typically user.mail).

6. Set **Provisioning Status** to **On** and save.

**Critical:** The attribute used for SCIM email and SSO email must be identical. Mismatches are the most common cause of login failures. For troubleshooting, see **[Microsoft Entra ID SSO/SCIM email mismatch](https://support.claude.com/en/articles/13917829)**.

## Step 4 — Assign people and groups

1. In **Users and groups**, assign the people or groups who should have access to Claude.

2. Only assigned people and groups will be provisioned and allowed to SSO.

## Step 5 — Verify

1. If you enabled SCIM, trigger a provisioning cycle and confirm people appear in Claude's admin settings.

2. Have a test user complete SSO login and verify they land in your organization's workspace.

---

## Need help?

See **[Set up single sign-on](https://support.claude.com/en/articles/13132885)** for the full end-to-end flow including domain verification and choosing a provisioning approach. If you run into issues, contact **[our Support team](https://support.claude.com/en/articles/9015913)** with your Entra tenant ID and a screenshot of your SAML configuration.