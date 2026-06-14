Title: Microsoft Entra ID SSO setup

URL Source: https://support.claude.com/en/articles/13917889-microsoft-entra-id-sso-setup

Markdown Content:
# Microsoft Entra ID SSO setup | Claude Help Center

[Skip to main content](https://support.claude.com/en/articles/13917889-microsoft-entra-id-sso-setup#main-content)

[![Image 1: Claude Help Center](https://downloads.intercomcdn.com/i/o/lupk8zyo/787776/ade321b9d8ff06050cb06ac0049d/d7ef4b66df4ff3851b5de741185c97ab.png)](https://support.claude.com/en/)

[API Docs](https://docs.claude.com/en/docs/intro)[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)[How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support)

English

[API Docs](https://docs.claude.com/en/docs/intro)[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)[How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support)

English

Search for articles... 

1.   [All Collections](https://support.claude.com/en/) 
2.   [Identity management (SSO, JIT, SCIM)](https://support.claude.com/en/collections/17270717-identity-management-sso-jit-scim) 
3.   [Setup by identity provider](https://support.claude.com/en/collections/19039081-setup-by-identity-provider) 
4.   Microsoft Entra ID SSO setup

# Microsoft Entra ID SSO setup

March 24, 2026

Table of contents

[Prerequisites](https://support.claude.com/en/articles/13917889-microsoft-entra-id-sso-setup#h_7171c31c6c)[Where to find your configuration values](https://support.claude.com/en/articles/13917889-microsoft-entra-id-sso-setup#h_a67dfce492)[Step 1 — Add Claude as an enterprise application in Entra](https://support.claude.com/en/articles/13917889-microsoft-entra-id-sso-setup#h_c71310e15f)[Step 2 — Configure SAML SSO](https://support.claude.com/en/articles/13917889-microsoft-entra-id-sso-setup#h_9305eb125e)[Step 3 — Configure SCIM provisioning](https://support.claude.com/en/articles/13917889-microsoft-entra-id-sso-setup#h_be13165d06)[Step 4 — Assign people and groups](https://support.claude.com/en/articles/13917889-microsoft-entra-id-sso-setup#h_1799d50770)[Step 5 — Verify](https://support.claude.com/en/articles/13917889-microsoft-entra-id-sso-setup#h_6e49d5b3a7)[Need help?](https://support.claude.com/en/articles/13917889-microsoft-entra-id-sso-setup#h_88279a4170)

This guide walks you through configuring single sign-on (SSO) for Claude using Microsoft Entra ID (formerly Azure Active Directory) as your identity provider. It applies to Team plans, Enterprise plans, and Console organizations.

## Prerequisites

*   A Claude Team plan, Enterprise plan, or Console organization with a parent organization (see **[Important considerations before enabling SSO](https://support.claude.com/en/articles/10276682)** for Console parent org requirements) 
*   Owner or Primary Owner role (Team and Enterprise) or Admin role (Console) 
*   Microsoft Entra ID P1 or P2 license (required for SCIM provisioning) 
*   Global Administrator or Application Administrator role in Entra 
*   Your domain verified in Claude's Identity and access settings — see **[Set up single sign-on](https://support.claude.com/en/articles/13132885)** for the full setup path including domain verification  

## Where to find your configuration values

The Entity ID, Reply URL (ACS URL), and SCIM credentials referenced below are provided in the WorkOS setup flow within your Identity and access settings — not by contacting Support.

*   **Team and Enterprise plans:** go to **[claude.ai/admin-settings/identity](https://claude.ai/admin-settings/identity)** 
*   **Console organizations:** go to **[platform.claude.com/settings/identity](https://platform.claude.com/settings/identity)** 

Start the SSO setup flow there and keep it open alongside the Entra Admin Center as you work through the steps below.

* * *

## Step 1 — Add Claude as an enterprise application in Entra

**Note:** "Enterprise applications" below refers to the section in Microsoft Entra's admin center—it's Microsoft's term for any app you integrate, and is unrelated to your Claude plan type.

1.   In the **Entra Admin Center**, go to **Enterprise applications → New application**. 
2.   Search for "Claude" in the gallery. If available, select it; otherwise choose **Create your own application** and name it "Claude". 
3.   Select **Integrate any other application you don't find in the gallery** and click "Create."  

## Step 2 — Configure SAML SSO

1.   In your new application, click **Single sign-on → SAML**. 
2.   In **Basic SAML Configuration**, enter: **Identifier (Entity ID)** from the WorkOS setup flow, **Reply URL (ACS URL)** from the WorkOS setup flow, and **Sign-on URL:****[https://claude.ai/login](https://claude.ai/login)**. 
3.   In **Attributes & Claims**, ensure the email claim is set to send user.mail (or the same attribute you'll use for SCIM). 
4.   Download the **Federation Metadata XML** and upload it in the WorkOS setup flow when prompted.  

## Step 3 — Configure SCIM provisioning

**Note:** SCIM provisioning is available on Enterprise plans and eligible Console organizations only. If you're on a Team plan, skip this step — you can use JIT provisioning instead. See **[Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195)**.

1.   In the application, go to **Provisioning → Get Started**. 
2.   Set **Provisioning Mode** to **Automatic**. 
3.   Enter the **Tenant URL** and **Secret Token** from the WorkOS setup flow. 
4.   Click **Test Connection** to verify. 
5.   Under **Mappings**, ensure the email attribute mapping points to the same field as your SSO email claim (typically user.mail). 
6.   Set **Provisioning Status** to **On** and save. 

**Critical:** The attribute used for SCIM email and SSO email must be identical. Mismatches are the most common cause of login failures. For troubleshooting, see **[Microsoft Entra ID SSO/SCIM email mismatch](https://support.claude.com/en/articles/13917829)**.

## Step 4 — Assign people and groups

1.   In **Users and groups**, assign the people or groups who should have access to Claude. 
2.   Only assigned people and groups will be provisioned and allowed to SSO.  

## Step 5 — Verify

1.   If you enabled SCIM, trigger a provisioning cycle and confirm people appear in Claude's admin settings. 
2.   Have a test user complete SSO login and verify they land in your organization's workspace.  

* * *

## Need help?

See **[Set up single sign-on](https://support.claude.com/en/articles/13132885)** for the full end-to-end flow including domain verification and choosing a provisioning approach. If you run into issues, contact **[our Support team](https://support.claude.com/en/articles/9015913)** with your Entra tenant ID and a screenshot of your SAML configuration.

* * *

Related Articles

[Microsoft Entra ID SSO/SCIM email mismatch](https://support.claude.com/en/articles/13917829-microsoft-entra-id-sso-scim-email-mismatch)[Google Workspace SSO setup](https://support.claude.com/en/articles/13917884-google-workspace-sso-setup)[Okta SSO setup](https://support.claude.com/en/articles/13917894-okta-sso-setup)[OneLogin SSO setup](https://support.claude.com/en/articles/13917899-onelogin-sso-setup)[Ping Identity SSO setup](https://support.claude.com/en/articles/13917902-ping-identity-sso-setup)

Did this answer your question?

😞😐😃

Table of contents

[Prerequisites](https://support.claude.com/en/articles/13917889-microsoft-entra-id-sso-setup#h_7171c31c6c)[Where to find your configuration values](https://support.claude.com/en/articles/13917889-microsoft-entra-id-sso-setup#h_a67dfce492)[Step 1 — Add Claude as an enterprise application in Entra](https://support.claude.com/en/articles/13917889-microsoft-entra-id-sso-setup#h_c71310e15f)[Step 2 — Configure SAML SSO](https://support.claude.com/en/articles/13917889-microsoft-entra-id-sso-setup#h_9305eb125e)[Step 3 — Configure SCIM provisioning](https://support.claude.com/en/articles/13917889-microsoft-entra-id-sso-setup#h_be13165d06)[Step 4 — Assign people and groups](https://support.claude.com/en/articles/13917889-microsoft-entra-id-sso-setup#h_1799d50770)[Step 5 — Verify](https://support.claude.com/en/articles/13917889-microsoft-entra-id-sso-setup#h_6e49d5b3a7)[Need help?](https://support.claude.com/en/articles/13917889-microsoft-entra-id-sso-setup#h_88279a4170)

[![Image 2: Claude Help Center](https://downloads.intercomcdn.com/i/o/487548/17213f6a445c8e6e874b1f4b/fad85208982e639d11b9108df895a293.png)](https://support.claude.com/en/)

*   [Product](https://www.anthropic.com/product)
*   [Research](https://www.anthropic.com/research)
*   [Company](https://www.anthropic.com/company)
*   [News](https://www.anthropic.com/news)
*   [Careers](https://www.anthropic.com/careers)

*   [Terms of Service - Consumer](https://www.anthropic.com/terms)
*   [Terms of Service - Commercial](https://www.anthropic.com/legal/commercial-terms)
*   [Privacy Policy](https://www.anthropic.com/privacy)
*   [Usage Policy](https://www.anthropic.com/aup)
*   [Responsible Disclosure Policy](https://www.anthropic.com/responsible-disclosure-policy)
*   [Compliance](https://trust.anthropic.com/)
