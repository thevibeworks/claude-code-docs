# Covered Models under a Business Associate Agreement \(BAA\)

This article is for organizations that use Anthropic's HIPAA-ready services under a Business Associate Agreement (BAA). It explains which configurations are Eligible Services under the BAA and whether you can access Covered Models. **Your organization is responsible for ensuring its use of these services complies with applicable legal obligations.** Learn about **[Business Associate Agreements (BAA) for Commercial Customers](https://support.claude.com/en/articles/8114513-business-associate-agreements-baa-for-commercial-customers)** and **[Covered Models](https://support.claude.com/en/articles/15425695-covered-models)**.

**Important:** The primary ways to access Covered Models while covered by Anthropic's BAA are through the HIPAA-ready API and Chat on HIPAA-ready Claude Enterprise plans. There's currently no configuration that allows BAA-covered access to Covered Models in Claude Code or Cowork.

## Covered Models and data retention

Covered Models, like Claude Fable 5, require 30-day data retention on every platform where they're offered, as part of our safety work, and they can't be accessed from organizations or workspaces with zero data retention (ZDR) enabled. Learn about **[data retention practices for Mythos-class models](https://support.claude.com/en/articles/15425996-data-retention-practices-for-mythos-class-models)**.

Access to newly released Covered Models rolls out in stages on subscription and seat-based Enterprise plans, so a model may not appear for your organization right away—no configuration change is needed. Some Covered Models are available only to approved partners under limited access programs.

## Coverage at a glance

Each row in the table is a configuration: a product, how you access it, and whether you're using standard retention or zero data retention. The two right-hand columns show whether that configuration is covered under Anthropic's BAA and whether it can access Covered Models.

**Note:** Coverage under Anthropic's BAA always requires (a) signing the BAA, and (b) accessing Anthropic's products via their HIPAA-ready or (in the case of Claude Code) zero data retention configurations. Learn about **[HIPAA-ready API access](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#hipaa-readiness)** and **[HIPAA-ready Enterprise plans](https://support.claude.com/en/articles/13296973-hipaa-ready-enterprise-plans)**.

| **Product**         | **How you access it**         | **Data retention**                                                             | **Eligible Service under Anthropic's BAA?** | **Can you access Covered Models?** |
| ------------------- | ----------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------- | ---------------------------------- |
| Chat                | Claude Enterprise             | Standard retention                                                             | ✅ Yes                                       | ✅ Yes                              |
| Claude Code         | Claude Enterprise             | Zero data retention<br>**Note:** ZDR is available for qualified accounts only. | ✅ Yes<br>                                   | ❌ No                               |
| Claude Code         | Claude Enterprise             | Standard retention                                                             | ❌ No                                        | ✅ Yes                              |
| Claude Code         | 1P API org                    | Zero data retention                                                            | ✅ Yes                                       | ❌ No                               |
| Claude Code         | 1P API org                    | Standard retention                                                             | ❌ No                                        | ✅ Yes                              |
| Claude Code         | 3P API (Google Vertex only)\* | Standard retention                                                             | ❌ No                                        | ✅ Yes                              |
| Cowork              | Claude Enterprise             | Standard retention                                                             | ❌ No                                        | ✅ Yes                              |
| Claude API (1P API) | HIPAA-ready API               | Standard retention                                                             | ✅ Yes                                       | ✅ Yes                              |
| Claude API (1P API) | Regular API                   | Zero data retention                                                            | ✅ Yes                                       | ❌ No                               |
| Claude API (1P API) | Regular API                   | Standard retention                                                             | ❌ No                                        | ✅ Yes                              |

*Anthropic's BAA doesn't apply to services purchased through a third-party cloud provider. For questions about coverage on these platforms, contact your cloud provider and your Anthropic account team.
​

Requests to a Covered Model from a ZDR-enabled organization or workspace return an error.

## How to access Covered Models under the BAA

To access Covered Models in configurations that are covered under the BAA:

- **For API workloads: use a HIPAA-ready API organization.** This configuration operates with standard retention, so your applications can access Covered Models, including Claude Fable 5. If your organization doesn't have a HIPAA-ready API organization yet, contact your Anthropic account team to set one up. Note that Claude Code isn't an Eligible Service on a HIPAA-ready API organization. Learn more **[about HIPAA-ready API access](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#hipaa-readiness)**.

- **For Chat: use a HIPAA-ready Claude Enterprise plan.** Chat operates with standard retention, so it can access Covered Models with no configuration change. If your organization hasn't activated HIPAA readiness on its Enterprise plan, learn how in **[HIPAA-ready Enterprise plans](https://support.claude.com/en/articles/13296973-hipaa-ready-enterprise-plans)**.

**Important:** Claude Code is only covered under the BAA with ZDR enabled, and ZDR blocks Covered Models. Cowork isn't an Eligible Service under the BAA in any configuration. You can use Covered Models in Claude Code or Cowork outside the BAA, but don't submit protected health information (PHI).

## How to access Covered Models outside the BAA

To access Covered Models in configurations that aren't covered under the BAA:

- **On a 1P API organization with zero data retention enabled, you have two options:**

  - Enable standard retention in a dedicated workspace (**Workspace > Manage > Privacy Controls**). Your other workspaces keep ZDR. See **[Data retention practices for Mythos-class models](https://support.claude.com/en/articles/15425996-data-retention-practices-for-mythos-class-models#h_7008995545)** for instructions.

  - Contact your Anthropic account team to remove ZDR from the organization entirely.

- **For Claude Code through Claude Enterprise with zero data retention enabled:** Contact your Anthropic account team to change the retention setting or to set up a separate sandbox organization. You can also access Claude Code through a 1P API organization with standard retention.

**Note:** These configurations are not covered under the BAA. Don't submit protected health information (PHI) through them.

## Before you change your configuration

Some organizations may consider setting up a separate, non-ZDR organization to access Covered Models in Claude Code, Cowork, Chat, or API in production. Before you do, keep in mind:

- **A standard API organization without ZDR or the HIPAA configuration is not an Eligible Service under Anthropic's BAA.** Don't submit protected health information (PHI) through it.

- **HIPAA readiness and ZDR cannot coexist on a single 1P API organization.** If your organization needs both HIPAA-ready production API usage and ZDR for Claude Code, you'll need separate organization IDs.

- **Cowork is not an Eligible Service under Anthropic's BAA in any configuration**, regardless of retention settings or the model in use, and shouldn't be used with PHI.

- **If your teams work across multiple organizations with different coverage, you're responsible for ensuring PHI is only submitted through Eligible Services**, configured according to the **[Implementation Guide for HIPAA Entities](https://trust.anthropic.com/resources?s=rgirr4qe8u7ek8c2igx3&name=claude-for-enterprise-hipaa-ready-offering-implementation-guide)**.