Title: OneLogin SSO setup

URL Source: https://support.claude.com/en/articles/13917899-onelogin-sso-setup

Markdown Content:
1.   [All Collections](https://support.claude.com/en/)
2.   [Identity management (SSO, JIT, SCIM)](https://support.claude.com/en/collections/17270717-identity-management-sso-jit-scim)
3.   [Setup by identity provider](https://support.claude.com/en/collections/19039081-setup-by-identity-provider)
4.   OneLogin SSO setup

March 24, 2026

Table of contents

This guide walks through configuring SSO and SCIM for Claude with OneLogin as your identity provider. It applies to Team plans, Enterprise plans, and Console organizations.

## Prerequisites

## Where to find your configuration values

The Audience (Entity ID), ACS URL, and SCIM credentials referenced below are provided in the WorkOS setup flow within your Identity and access settings — not by contacting Support.

Start the SSO setup flow there and keep it open alongside the OneLogin Admin portal as you work through the steps below.

## Step 1 — Create a new application in OneLogin

## Step 2 — Configure SAML settings

## Step 3 — Map attributes

## Step 4 — Enable SCIM provisioning

**Critical:** SAML and SCIM must send the same email value. If people experience login failures after provisioning, see **[OneLogin SSO/SCIM email mismatch](https://support.claude.com/en/articles/13917861)**.

## Step 5 — Assign people

In the **Users** tab, assign individual people or use **Rules** to automatically assign based on role or group.

## Step 6 — Verify

## Need help?

See **[Set up single sign-on](https://support.claude.com/en/articles/13132885)** for the full end-to-end flow including domain verification and choosing a provisioning approach. If you run into issues, contact **[our Support team](https://support.claude.com/en/articles/9015913)** with your OneLogin domain and a screenshot of your SAML configuration.

* * *

Related Articles

[OneLogin SSO/SCIM email mismatch](https://support.claude.com/en/articles/13917861-onelogin-sso-scim-email-mismatch)[Google Workspace SSO setup](https://support.claude.com/en/articles/13917884-google-workspace-sso-setup)[Microsoft Entra ID SSO setup](https://support.claude.com/en/articles/13917889-microsoft-entra-id-sso-setup)[Okta SSO setup](https://support.claude.com/en/articles/13917894-okta-sso-setup)[Ping Identity SSO setup](https://support.claude.com/en/articles/13917902-ping-identity-sso-setup)
