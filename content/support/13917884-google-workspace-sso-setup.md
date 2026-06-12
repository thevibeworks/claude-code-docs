Title: Google Workspace SSO setup

URL Source: https://support.claude.com/en/articles/13917884-google-workspace-sso-setup

Markdown Content:
This guide helps you configure Claude to use Google Workspace as your identity provider for SSO and automated user provisioning. It applies to Team plans, Enterprise plans, and Console organizations.

## Prerequisites

## Where to find your configuration values

The ACS URL, Entity ID, and SCIM credentials referenced below are provided in the WorkOS setup flow within your Identity and access settings — not by contacting Support.

Start the SSO setup flow there and keep it open alongside the Google Admin console as you work through the steps below.

## Step 1 — Add a custom SAML app in Google Admin

## Step 2 — Enter service provider details

## Step 3 — Configure attribute mapping

## Step 4 — Enable auto-provisioning (SCIM)

**Critical:** Both SAML and SCIM must use primaryEmail. If someone has aliases, ensure their primary Google email matches what SCIM sends. For troubleshooting, see **[Google Workspace SSO/SCIM email mismatch](https://support.claude.com/en/articles/13917817)**.

## Step 5 — Assign the app to people or OUs

## Step 6 — Verify

## Need help?

See **[Set up single sign-on](https://support.claude.com/en/articles/13132885)** for the full end-to-end flow including domain verification and choosing a provisioning approach. If you run into issues, contact **[our Support team](https://support.claude.com/en/articles/9015913)** with your organization's domain and a screenshot of your SAML configuration.

* * *

Related Articles

[Google Workspace SSO/SCIM email mismatch](https://support.claude.com/en/articles/13917817-google-workspace-sso-scim-email-mismatch)[Microsoft Entra ID SSO setup](https://support.claude.com/en/articles/13917889-microsoft-entra-id-sso-setup)[Okta SSO setup](https://support.claude.com/en/articles/13917894-okta-sso-setup)[OneLogin SSO setup](https://support.claude.com/en/articles/13917899-onelogin-sso-setup)[Ping Identity SSO setup](https://support.claude.com/en/articles/13917902-ping-identity-sso-setup)
