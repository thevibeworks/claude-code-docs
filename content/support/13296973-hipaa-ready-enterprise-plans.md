# HIPAA-ready Enterprise plans

This feature is available for Enterprise plans only (both self-serve and sales-assisted).

We offer a HIPAA-ready version of Claude that is available for organizations on Enterprise plans that choose to process protected health information (PHI) through Claude. This article explains what the offering includes, which features are available, and how to get started.

## Overview

The HIPAA-ready Enterprise offering is designed for healthcare providers, health plans, healthcare data processors, and their business associates who are subject to HIPAA requirements. This offering includes a Business Associate Agreement (BAA), functionality, and safeguards designed to support an organization's HIPAA compliance requirements.

## Who is this for?

This offering is designed for HIPAA-covered entities and their business associates, including:

- Healthcare providers (e.g., hospitals, clinics, physicians)

- Health plans and insurers

- Healthcare data processors

- Business associates that handle PHI on behalf of covered entities

- Other HIPAA regulated entities

If you're unsure whether your organization benefits from a HIPAA-ready product, ask yourself: will you be processing protected health information through Claude? If yes, you need the HIPAA-ready offering with a BAA.

## Feature availability

The HIPAA-ready Enterprise offering includes access to certain features available on **[standard Enterprise plans](https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan)**. For example, users can chat with Claude, create projects and artifacts, and use voice mode. Depending on what functions are enabled by the organization’s plan administrator, users can also leverage connectors, enterprise search, file creation and code execution, web search, research, and skills. More information about the specific features, functionality, and administrator controls are included in the **[Implementation Guide for HIPAA Entities](https://trust.anthropic.com/resources?s=rgirr4qe8u7ek8c2igx3&name=claude-for-enterprise-hipaa-ready-offering-implementation-guide)**.

**Important:** Enabling HIPAA readiness alone doesn't bring Claude Code under your BAA. Claude Code is covered under your BAA only with zero data retention (ZDR) enabled, and only on qualified accounts. Without ZDR, Claude Code remains available to use but isn't covered—including when Claude Code access is bundled into your Enterprise seats. To explore Claude Code coverage, contact your Anthropic account team or our **[Sales team](https://www.anthropic.com/contact-sales)**.

Additionally, Cowork is not yet covered under Anthropic’s BAA.

## Additional resources

For detailed implementation requirements and technical specifications, review the **[Implementation Guide for HIPAA Entities](https://trust.anthropic.com/resources?s=rgirr4qe8u7ek8c2igx3&name=claude-for-enterprise-hipaa-ready-offering-implementation-guide)** on the Anthropic Trust Center. You can download the Implementation Guide directly during the setup flow.

**Note:** You'll need to request access to view the Implementation Guide. Requests from domains matching existing customer accounts are approved automatically.

---

## Get started

Eligible Enterprise organizations can enable HIPAA-ready configuration directly from organization settings—no sales or legal cycle required. The Business Associate Agreement (BAA) is included in the flow as click-to-accept, so there's no separate document to sign and return. Clicking “Accept and Enable HIPAA” constitutes acceptance of the BAA.

### Eligibility

You can enable the HIPAA configuration from organization settings if your organization is on an Enterprise plan. Team plans and individual plans (Free, Pro, and Max) can't enable HIPAA.

Only the **Primary Owner** of the organization can accept the BAA and enable HIPAA. Other Owners or Admins can't complete this flow on the org's behalf. If you're an admin but not the Primary Owner of the Enterprise organization, ask your Primary Owner to sign in and complete enablement.

### Before you begin

Two things to know up front:

- **Enabling HIPAA resets certain settings across your organization.** Some configurations return to defaults as part of the transition to a HIPAA-ready state. The onboarding modal and the Implementation Guide (downloadable during the flow) detail what changes.

- **This is a one-way decision.** Once HIPAA is enabled and the BAA is accepted, the change can't be reversed from organization settings.

You must review the BAA and the Implementation Guide before accepting, as this is an irreversible organization transition.

**Note:** The BAA offered through the self-serve flow is a standard agreement and can't be modified.

### Enable HIPAA

1. Sign in to Claude as the Primary Owner and go to **[Organization settings > Data and privacy](https://claude.ai/admin-settings/data-privacy-controls)**.

2. Go to **HIPAA Compliance.**

3. Click “Enable” to open the consent flow.

4. Download the Business Associate Agreement, review it, then click “Next.”

5. Download the Implementation Guide, review it, then click “Next.”

6. Click “Accept and enable HIPAA.”

### Confirmation

Once enabled, you'll see a checkmark in the **HIPAA Compliance** section of organization settings, confirming your organization has been configured to process PHI through Claude in accordance with HIPAA. If you don't see this checkmark, your organization isn't enabled.

The onboarding modal will guide you through next steps for your team.

For help with the BAA, the Implementation Guide, or post-enablement questions, reach out to your Anthropic account team or **[our support team](https://support.claude.com/en/articles/9015913-how-to-get-support)**.

---

## If you have an existing API BAA

If your organization signed a BAA for Claude API usage before December 2, 2025, that agreement only covers API usage—it does not extend to the HIPAA-ready Enterprise plan. To add this Enterprise plan access, you'll need to sign a new BAA with your account team.

BAAs signed after December 2, 2025 can cover both API usage and the Enterprise plan under a single agreement.

If you use the Claude API, learn more about **[HIPAA-ready Claude API access and how to set it up](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#hipaa-readiness)**.