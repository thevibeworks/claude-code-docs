Title: Okta SSO setup

URL Source: https://support.claude.com/en/articles/13917894-okta-sso-setup

Markdown Content:
# Okta SSO setup | Claude Help Center

[Skip to main content](https://support.claude.com/en/articles/13917894-okta-sso-setup#main-content)

[![Image 1: Claude Help Center](https://downloads.intercomcdn.com/i/o/lupk8zyo/787776/ade321b9d8ff06050cb06ac0049d/d7ef4b66df4ff3851b5de741185c97ab.png)](https://support.claude.com/en/)

[API Docs](https://docs.claude.com/en/docs/intro)[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)[How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support)

English

[API Docs](https://docs.claude.com/en/docs/intro)[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)[How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support)

English

Search for articles... 

1.   [All Collections](https://support.claude.com/en/) 
2.   [Identity management (SSO, JIT, SCIM)](https://support.claude.com/en/collections/17270717-identity-management-sso-jit-scim) 
3.   [Setup by identity provider](https://support.claude.com/en/collections/19039081-setup-by-identity-provider) 
4.   Okta SSO setup

# Okta SSO setup

March 24, 2026

Table of contents

[Prerequisites](https://support.claude.com/en/articles/13917894-okta-sso-setup#h_b5803974ac)[Where to find your configuration values](https://support.claude.com/en/articles/13917894-okta-sso-setup#h_6b2eef4ed4)[Step 1 — Create the Okta application](https://support.claude.com/en/articles/13917894-okta-sso-setup#h_c33f81b019)[Step 2 — Configure SAML](https://support.claude.com/en/articles/13917894-okta-sso-setup#h_7bcc0cfce3)[Step 3 — Enable SCIM provisioning](https://support.claude.com/en/articles/13917894-okta-sso-setup#h_562e1f6754)[Step 4 — Assign people or groups](https://support.claude.com/en/articles/13917894-okta-sso-setup#h_4bb3b13a6d)[Step 5 — Verify](https://support.claude.com/en/articles/13917894-okta-sso-setup#h_f20a647925)[Need help?](https://support.claude.com/en/articles/13917894-okta-sso-setup#h_09b58b7a46)

This guide covers configuring SSO and SCIM provisioning for Claude with Okta as your identity provider. It applies to Team plans, Enterprise plans, and Console organizations.

## Prerequisites

*   A Claude Team plan, Enterprise plan, or Console organization with a parent organization (see **[Important considerations before enabling SSO](https://support.claude.com/en/articles/10276682)** for Console parent org requirements) 
*   Owner or Primary Owner role (Team and Enterprise) or Admin role (Console) 
*   Okta administrator access 
*   Your domain verified in Claude's Identity and access settings — see **[Set up single sign-on](https://support.claude.com/en/articles/13132885)** for the full setup path including domain verification  

## Where to find your configuration values

The ACS URL, Entity ID, and SCIM credentials referenced below are provided in the WorkOS setup flow within your Identity and access settings.

*   **Team and Enterprise plans:** go to **[claude.ai/admin-settings/identity](https://claude.ai/admin-settings/identity)** 
*   **Console organizations:** go to **[platform.claude.com/settings/identity](https://platform.claude.com/settings/identity)** 

Start the SSO setup flow there and keep it open alongside the Okta Admin console as you work through the steps below.

* * *

## Step 1 — Create the Okta application

1.   In the Okta Admin console, go to **Applications → Applications → Create App Integration**. 
2.   For the SSO method, choose "SAML 2.0" (recommended) or "OIDC." 
3.   Name the app "Claude" and click "Next." 

## Step 2 — Configure SAML

1.   In the **Configure SAML** tab, enter: **Single sign-on URL (ACS URL)** from the WorkOS setup flow, **Audience URI (Entity ID)** from the WorkOS setup flow, **Name ID format:** EmailAddress, and **Application username:** Email. 
2.   Under **Attribute Statements**, add an attribute named email with value user.email. 
3.   Download the **Identity Provider metadata** XML and upload it in the WorkOS setup flow when prompted. 

## Step 3 — Enable SCIM provisioning

**Note:** SCIM provisioning is available on Enterprise plans and eligible Console organizations only. If you're on a Team plan, skip this step—you can use JIT provisioning instead. See **[Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195)**.

1.   In the app, go to the **Provisioning** tab and click “Configure API Integration.” 
2.   Check **Enable API integration** and enter the SCIM Base URL and API Token from the WorkOS setup flow. 
3.   Click “Test API credentials” to verify, then save. 
4.   Under **To App**, enable **Create Users**, **Update User Attributes**, and **Deactivate Users**. 
5.   In **Attribute Mappings → To App**, confirm the email attribute maps to user.email — the same field as your SAML assertion. 

**Important:** SCIM and SAML must use the same Okta field for email. A common issue is SCIM using user.login while SAML uses user.email. See **[Okta SSO/SCIM email mismatch](https://support.claude.com/en/articles/13917840)** if people can't log in after provisioning.

## Step 4 — Assign people or groups

1.   In the **Assignments** tab, assign the people or Okta groups that should access Claude. 
2.   If you enable SCIM, Okta will automatically provision assigned people. If you're using JIT, people will be provisioned on their first SSO login. 

## Step 5 — Verify

1.   If you enabled SCIM, check provisioning logs to confirm people were successfully created in Claude. 
2.   Have a test user complete SSO and verify they land in your organization's workspace. 

* * *

## Need help?

For the full end-to-end flow including domain verification and choosing a provisioning approach, see **[Set up single sign-on](https://support.claude.com/en/articles/13132885)**. If you run into issues, contact **[our Support team](https://support.claude.com/en/articles/9015913-how-to-get-support)** with your organization's domain and a screenshot of your Okta SAML configuration.

* * *

Related Articles

[Okta SSO/SCIM email mismatch](https://support.claude.com/en/articles/13917840-okta-sso-scim-email-mismatch)[Google Workspace SSO setup](https://support.claude.com/en/articles/13917884-google-workspace-sso-setup)[Microsoft Entra ID SSO setup](https://support.claude.com/en/articles/13917889-microsoft-entra-id-sso-setup)[OneLogin SSO setup](https://support.claude.com/en/articles/13917899-onelogin-sso-setup)[Ping Identity SSO setup](https://support.claude.com/en/articles/13917902-ping-identity-sso-setup)

Did this answer your question?

😞😐😃

Table of contents

[Prerequisites](https://support.claude.com/en/articles/13917894-okta-sso-setup#h_b5803974ac)[Where to find your configuration values](https://support.claude.com/en/articles/13917894-okta-sso-setup#h_6b2eef4ed4)[Step 1 — Create the Okta application](https://support.claude.com/en/articles/13917894-okta-sso-setup#h_c33f81b019)[Step 2 — Configure SAML](https://support.claude.com/en/articles/13917894-okta-sso-setup#h_7bcc0cfce3)[Step 3 — Enable SCIM provisioning](https://support.claude.com/en/articles/13917894-okta-sso-setup#h_562e1f6754)[Step 4 — Assign people or groups](https://support.claude.com/en/articles/13917894-okta-sso-setup#h_4bb3b13a6d)[Step 5 — Verify](https://support.claude.com/en/articles/13917894-okta-sso-setup#h_f20a647925)[Need help?](https://support.claude.com/en/articles/13917894-okta-sso-setup#h_09b58b7a46)

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
