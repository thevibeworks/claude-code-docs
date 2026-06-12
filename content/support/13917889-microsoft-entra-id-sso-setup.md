Title: Microsoft Entra ID SSO setup

URL Source: https://support.claude.com/en/articles/13917889-microsoft-entra-id-sso-setup

Markdown Content:
1.   [All Collections](https://support.claude.com/en/)
2.   [Identity management (SSO, JIT, SCIM)](https://support.claude.com/en/collections/17270717-identity-management-sso-jit-scim)
3.   [Setup by identity provider](https://support.claude.com/en/collections/19039081-setup-by-identity-provider)
4.   Microsoft Entra ID SSO setup

March 24, 2026

Table of contents

This guide walks you through configuring single sign-on (SSO) for Claude using Microsoft Entra ID (formerly Azure Active Directory) as your identity provider. It applies to Team plans, Enterprise plans, and Console organizations.

## Prerequisites

## Where to find your configuration values

The Entity ID, Reply URL (ACS URL), and SCIM credentials referenced below are provided in the WorkOS setup flow within your Identity and access settings — not by contacting Support.

Start the SSO setup flow there and keep it open alongside the Entra Admin Center as you work through the steps below.

## Step 1 — Add Claude as an enterprise application in Entra

## Step 2 — Configure SAML SSO

## Step 3 — Configure SCIM provisioning

**Critical:** The attribute used for SCIM email and SSO email must be identical. Mismatches are the most common cause of login failures. For troubleshooting, see **[Microsoft Entra ID SSO/SCIM email mismatch](https://support.claude.com/en/articles/13917829)**.

## Step 4 — Assign people and groups

## Step 5 — Verify

## Need help?

See **[Set up single sign-on](https://support.claude.com/en/articles/13132885)** for the full end-to-end flow including domain verification and choosing a provisioning approach. If you run into issues, contact **[our Support team](https://support.claude.com/en/articles/9015913)** with your Entra tenant ID and a screenshot of your SAML configuration.

* * *

Related Articles

[Microsoft Entra ID SSO/SCIM email mismatch](https://support.claude.com/en/articles/13917829-microsoft-entra-id-sso-scim-email-mismatch)[Google Workspace SSO setup](https://support.claude.com/en/articles/13917884-google-workspace-sso-setup)[Okta SSO setup](https://support.claude.com/en/articles/13917894-okta-sso-setup)[OneLogin SSO setup](https://support.claude.com/en/articles/13917899-onelogin-sso-setup)[Ping Identity SSO setup](https://support.claude.com/en/articles/13917902-ping-identity-sso-setup)
