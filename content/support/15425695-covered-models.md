# Covered Models

Anthropic may designate certain models as “Covered Models” when they cross capability thresholds that warrant additional safeguards or other treatment. This page lists the models currently designated as Covered Models and describes the data handling, privacy, and access policies that apply to them.

**Note:** These policies apply only to the models listed on this page. All other Claude models continue to operate under your existing agreement and configured retention settings.

## What is a Covered Model?

A Covered Model is a Claude model whose capabilities—for example in software engineering, agentic workflows, scientific reasoning, or cybersecurity — represent a substantial step up from prior generations and create elevated risk if misused. Because some forms of misuse only become detectable across many requests, these models require safeguards that operate over a retained window of usage data rather than on a single request at a time.

Anthropic may designate certain models as "Covered Models" when their capabilities warrant additional safeguards or other treatment. When a model is designated as a Covered Model, it will be added to the list below and the policies on this page take effect for that model on every surface where it is offered.

## Current Covered Models

| **Model**         | **Designation date** | **Status**               | **Availability**                                                                                     |
| ----------------- | -------------------- | ------------------------ | ---------------------------------------------------------------------------------------------------- |
| Claude Mythos 5.1 | August 31, 2026      | Limited availability     | Limited access (approved partners)                                                                   |
| Claude Fable 5.1  | August 31, 2026      | Generally available      | Claude applications, Claude Platform, Amazon Bedrock, Google Cloud Agent Platform, Microsoft Foundry |
| Claude Mythos 5   | June 9, 2026         | Limited availability<br> | Limited access (approved partners)                                                                   |
| Claude Fable 5    | June 9, 2026         | Generally available      | Claude applications, Claude Platform, Amazon Bedrock, Google Cloud Agent Platform, Microsoft Foundry |

*We will update this list as new models are designated or as existing designations change.*

## Policies that apply to Covered Models

The following policies apply to every Covered Model listed above, on every platform where it is available (Claude apps, Claude Platform, Amazon Bedrock, Google Cloud Agent Platform, and Microsoft Foundry).

### Data retention

- **30-day minimum retention by default.** Prompts and model completions are retained for at least 30 days and then automatically deleted, unless they are subject to a safety investigation or we are legally required to maintain them. Accordingly, zero data retention is not available in workspaces, Claude Enterprise organizations, or third-party platforms (e.g., Azure Subscriptions) where Covered Models can be accessed. Customers who are eligible for zero data retention can continue to use prior Claude models under their existing settings and agreements. Learn more about data retention practices for Covered Models here: **[Data retention practices for Mythos-class models](https://support.claude.com/en/articles/15425996).**

### Use and review of retained data

- **How retained data is used.** Information about how Anthropic uses inputs, outputs, and other information from commercial and consumer plans can be found in our Privacy Center:

  - **[Commercial Customers](https://privacy.claude.com/en/collections/10663361-commercial-customers)**

  - **[Consumers](https://privacy.claude.com/en/collections/10663362-consumers)**

- **Automated review by default.** Retained data is assessed by automated safety systems designed to flag harmful content.

### Security and privacy controls

- **Information security program.** Retained data is protected by Anthropic’s documented information security program, with breach notification in accordance with organizations’ agreements with Anthropic and our Data Processing Addendum.

### Availability and access

- **All surfaces.** These policies follow the model. They apply wherever Covered Models are offered, including third-party cloud platforms.

- **Eligibility.** Some Covered Models (such as Claude Mythos 5) are available only to approved partners under limited access programs. See the table above for current availability.

- **Enablement.** Contact your Anthropic account team to inquire about limited-availability models or grants or our security and privacy controls.

- **BAA customers.** If your organization uses Anthropic’s HIPAA-ready services under a Business Associate Agreement (BAA), see **[Covered Models under Anthropic’s BAA](https://support.claude.com/en/articles/15455031)** for which configurations can access Covered Models as Eligible Services.

## Zero data retention and Enterprise Frontier Safeguards

All commercial customers can use Claude Fable 5 and Fable 5.1 today under the standard policies described above. For organizations whose privacy or regulatory obligations make Anthropic-held data retention difficult, we are introducing **[Enterprise Frontier Safeguards](https://www.anthropic.com/news/enterprise-frontier-safeguards)** (EFS), which combines automated safety monitoring with the option to keep retained monitoring data in cloud infrastructure the customer controls. EFS will roll out in phases beginning in fall 2026.

To make the transition smooth, eligible customers will receive the option to use ZDR with Fable 5 and Fable 5.1 for their own internal business applications. This arrangement is available for a limited time, and intended to be a transition to EFS. Anthropic or your cloud provider will contact eligible organizations directly; you can also request consideration using **[this form](https://claude.com/form/enterprise-frontier-safeguards)**.

Certain products built on Claude may extend the option to use ZDR with these models to their own eligible business customers under terms agreed with Anthropic, and we are working to broaden product support over time.

This arrangement affects only the retention and review of stored data. The Usage Policy, real-time safety classifiers, and Anthropic's enforcement systems continue to apply to all traffic, and Anthropic may modify or withdraw the arrangement, including in response to misuse.