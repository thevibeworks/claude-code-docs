Title: Google Workspace SSO setup

URL Source: https://support.claude.com/en/articles/13917884-google-workspace-sso-setup

Markdown Content:
# Google Workspace SSO setup | Claude Help Center

[Skip to main content](https://support.claude.com/en/articles/13917884-google-workspace-sso-setup#main-content)

[![Image 1: Claude Help Center](https://downloads.intercomcdn.com/i/o/lupk8zyo/787776/ade321b9d8ff06050cb06ac0049d/d7ef4b66df4ff3851b5de741185c97ab.png)](https://support.claude.com/en/)

[API Docs](https://docs.claude.com/en/docs/intro)[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)[How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support)

English

[API Docs](https://docs.claude.com/en/docs/intro)[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)[How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support)

English

Search for articles... 

1.   [All Collections](https://support.claude.com/en/) 
2.   [Identity management (SSO, JIT, SCIM)](https://support.claude.com/en/collections/17270717-identity-management-sso-jit-scim) 
3.   [Setup by identity provider](https://support.claude.com/en/collections/19039081-setup-by-identity-provider) 
4.   Google Workspace SSO setup

# Google Workspace SSO setup

March 24, 2026

Table of contents

[Prerequisites](https://support.claude.com/en/articles/13917884-google-workspace-sso-setup#h_1c27513fbf)[Where to find your configuration values](https://support.claude.com/en/articles/13917884-google-workspace-sso-setup#h_709059d047)[Step 1 — Add a custom SAML app in Google Admin](https://support.claude.com/en/articles/13917884-google-workspace-sso-setup#h_b2c87c90da)[Step 2 — Enter service provider details](https://support.claude.com/en/articles/13917884-google-workspace-sso-setup#h_3cc8a8607b)[Step 3 — Configure attribute mapping](https://support.claude.com/en/articles/13917884-google-workspace-sso-setup#h_fed62737e3)[Step 4 — Enable auto-provisioning (SCIM)](https://support.claude.com/en/articles/13917884-google-workspace-sso-setup#h_4b0e3621be)[Step 5 — Assign the app to people or OUs](https://support.claude.com/en/articles/13917884-google-workspace-sso-setup#h_649bb5a947)[Step 6 — Verify](https://support.claude.com/en/articles/13917884-google-workspace-sso-setup#h_bc48acfe94)[Need help?](https://support.claude.com/en/articles/13917884-google-workspace-sso-setup#h_3c49d6fe08)

This guide helps you configure Claude to use Google Workspace as your identity provider for SSO and automated user provisioning. It applies to Team plans, Enterprise plans, and Console organizations.

## Prerequisites

*   A Claude Team plan, Enterprise plan, or Console organization with a parent organization (see **[Important considerations before enabling SSO](https://support.claude.com/en/articles/10276682)** for Console parent org requirements) 
*   Owner or Primary Owner role (Team and Enterprise) or Admin role (Console) 
*   Google Workspace Super Admin access 
*   Your domain verified in Claude's Identity and access settings — see **[Set up single sign-on](https://support.claude.com/en/articles/13132885)** for the full setup path including domain verification  

## Where to find your configuration values

The ACS URL, Entity ID, and SCIM credentials referenced below are provided in the WorkOS setup flow within your Identity and access settings — not by contacting Support.

*   **Team and Enterprise plans:** go to **[claude.ai/admin-settings/identity](https://claude.ai/admin-settings/identity)** 
*   **Console organizations:** go to **[platform.claude.com/settings/identity](https://platform.claude.com/settings/identity)** 

Start the SSO setup flow there and keep it open alongside the Google Admin console as you work through the steps below.

* * *

## Step 1 — Add a custom SAML app in Google Admin

1.   In the **Google Admin console**, go to **Apps → Web and mobile apps → Add app → Add custom SAML app**. 
2.   Name it "Claude" and click "Next." 
3.   Download the **IdP metadata** XML. You'll upload this in the WorkOS setup flow when prompted. 
4.   Click "Next."  

## Step 2 — Enter service provider details

1.   Enter the values from the WorkOS setup flow: **ACS URL** and **Entity ID**. 
2.   Set **Name ID format** to **EMAIL** and **Name ID** to **Basic Information > Primary email**. 
3.   Click "Next."  

## Step 3 — Configure attribute mapping

1.   In the **Attribute mapping** step, add: Google Directory attribute: **Primary email** → App attribute: email. 
2.   Click "Finish."  

## Step 4 — Enable auto-provisioning (SCIM)

**Note:** SCIM provisioning is available on Enterprise plans and eligible Console organizations only. If you're on a Team plan, skip this step — you can use JIT provisioning instead. See **[Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195)**.

1.   In the app's settings, go to the **Autoprovisioning** section and click "Configure autoprovisioning" (may require enabling in Google Workspace admin settings). 
2.   Enter the **Endpoint URL** and **Access token** from the WorkOS setup flow. 
3.   Map the primaryEmail attribute to the Claude email field. 
4.   Enable provisioning and save. 

**Critical:** Both SAML and SCIM must use primaryEmail. If someone has aliases, ensure their primary Google email matches what SCIM sends. For troubleshooting, see **[Google Workspace SSO/SCIM email mismatch](https://support.claude.com/en/articles/13917817)**.

## Step 5 — Assign the app to people or OUs

1.   In the app settings, click "User access." 
2.   Enable the app for the relevant Organizational Units or groups. 
3.   Click "Save."  

## Step 6 — Verify

1.   If you enabled SCIM, check that provisioned people appear in your organization's member list. 
2.   Have a test user log in via SSO and confirm they land in your organization's workspace. 

* * *

## Need help?

See **[Set up single sign-on](https://support.claude.com/en/articles/13132885)** for the full end-to-end flow including domain verification and choosing a provisioning approach. If you run into issues, contact **[our Support team](https://support.claude.com/en/articles/9015913)** with your organization's domain and a screenshot of your SAML configuration.

* * *

Related Articles

[Google Workspace SSO/SCIM email mismatch](https://support.claude.com/en/articles/13917817-google-workspace-sso-scim-email-mismatch)[Microsoft Entra ID SSO setup](https://support.claude.com/en/articles/13917889-microsoft-entra-id-sso-setup)[Okta SSO setup](https://support.claude.com/en/articles/13917894-okta-sso-setup)[OneLogin SSO setup](https://support.claude.com/en/articles/13917899-onelogin-sso-setup)[Ping Identity SSO setup](https://support.claude.com/en/articles/13917902-ping-identity-sso-setup)

Did this answer your question?

😞😐😃

Table of contents

[Prerequisites](https://support.claude.com/en/articles/13917884-google-workspace-sso-setup#h_1c27513fbf)[Where to find your configuration values](https://support.claude.com/en/articles/13917884-google-workspace-sso-setup#h_709059d047)[Step 1 — Add a custom SAML app in Google Admin](https://support.claude.com/en/articles/13917884-google-workspace-sso-setup#h_b2c87c90da)[Step 2 — Enter service provider details](https://support.claude.com/en/articles/13917884-google-workspace-sso-setup#h_3cc8a8607b)[Step 3 — Configure attribute mapping](https://support.claude.com/en/articles/13917884-google-workspace-sso-setup#h_fed62737e3)[Step 4 — Enable auto-provisioning (SCIM)](https://support.claude.com/en/articles/13917884-google-workspace-sso-setup#h_4b0e3621be)[Step 5 — Assign the app to people or OUs](https://support.claude.com/en/articles/13917884-google-workspace-sso-setup#h_649bb5a947)[Step 6 — Verify](https://support.claude.com/en/articles/13917884-google-workspace-sso-setup#h_bc48acfe94)[Need help?](https://support.claude.com/en/articles/13917884-google-workspace-sso-setup#h_3c49d6fe08)

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
