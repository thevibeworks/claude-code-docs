# Ping Identity SSO setup

This guide covers configuring Claude with PingOne or PingFederate as your identity provider. It applies to Team plans, Enterprise plans, and Console organizations.

## Prerequisites

- A Claude Team plan, Enterprise plan, or Console organization with a parent organization (see **[Important considerations before enabling SSO](https://support.claude.com/en/articles/10276682)** for Console parent org requirements)

- Owner or Primary Owner role (Team and Enterprise) or Admin role (Console)

- PingOne Environment Admin or PingFederate Admin access

- Your domain verified in Claude's Identity and access settings — see **[Set up single sign-on](https://support.claude.com/en/articles/13132885)** for the full setup path including domain verification

## Where to find your configuration values

The ACS URL, Entity ID, and SCIM credentials referenced below are provided in the WorkOS setup flow within your Identity and access settings — not by contacting Support.

- **Team and Enterprise plans:** go to **[claude.ai/admin-settings/identity](https://claude.ai/admin-settings/identity)**

- **Console organizations:** go to **[platform.claude.com/settings/identity](https://platform.claude.com/settings/identity)**

Start the SSO setup flow there and keep it open alongside your Ping admin console as you work through the steps below.

---

## PingOne setup

### Step 1 — Create an application connection

1. In the PingOne admin console, go to **Connections → Applications → + Add Application**.

2. Select "SAML Application."

3. Name it "Claude" and click "Configure."

### Step 2 — Configure SAML

1. Choose "Manually Enter" and provide the SP details from the WorkOS setup flow: **ACS URL** and **Entity ID**.

2. Download the PingOne **IdP metadata** and upload it in the WorkOS setup flow when prompted.

3. In **Attribute Mappings**, map `email` to the PingOne **Email Address** attribute.

### Step 3 — Enable SCIM provisioning

**Note:** SCIM provisioning is available on Enterprise plans and eligible Console organizations only. If you're on a Team plan, skip this step — you can use JIT provisioning instead. See **[Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195)**.

1. In the application settings, go to the **Provisioning** tab.

2. Enable **Outbound Provisioning** and enter the SCIM endpoint URL and access token from the WorkOS setup flow.

3. Map `emails[primary].value` to the PingOne **Email Address** attribute—the same attribute used in SAML.

**Critical:** Ensure SAML and SCIM use identical attribute sources. See **[Ping Identity SSO/SCIM email mismatch](https://support.claude.com/en/articles/13917875)** for troubleshooting.

### Step 4 — Assign population

1. Under **Populations**, assign the user population that should access Claude.

2. Enable the application and click "Save."

---

## PingFederate setup

PingFederate configurations vary significantly by version and deployment. The general approach is:

1. Create a new **SP Connection** using the SP metadata from the WorkOS setup flow.

2. Configure the **Attribute Contract** to include `email`.

3. Map the email attribute in the **Adapter Mapping** to the person's primary email field.

4. For SCIM (Enterprise plans and eligible Console organizations only), configure an outbound provisioning channel targeting the SCIM endpoint from the WorkOS setup flow.

Contact **[our Support team](https://support.claude.com/en/articles/9015913)** for PingFederate-specific guidance.

---

## Need help?

See **[Set up single sign-on](https://support.claude.com/en/articles/13132885)** for the full end-to-end flow including domain verification and choosing a provisioning approach. If you run into issues, contact **[our Support team](https://support.claude.com/en/articles/9015913)** with your Ping environment details.