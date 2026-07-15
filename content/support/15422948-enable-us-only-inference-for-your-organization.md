# Enable US-only inference for your organization

This article explains what the **US-only inference** setting does, how to turn it on, and how it affects billing for your Enterprise organization.

US-only inference is available on usage-based Enterprise plans. Primary Owners, Owners, and custom roles with the Privacy permission set to "Can manage" can manage this setting.

## What is US-only inference?

US-only inference keeps your organization's inference, the model processing that happens when Claude generates a response, within the United States.

When the setting is on, all inference for your organization runs on servers located in the United States. This applies to usage across all the Claude apps, including Claude Code, Claude Desktop, etc., and includes background processing like conversation titles and memory. Using US-only inference comes with an increased cost. See **[How billing works](#h_8f4f5c2b9d)** below.

When the setting is off, inference may be routed to servers in other regions for speed and availability.

## Enable US-only inference

1. Navigate to **[Organization settings > Data and privacy](https://claude.ai/admin-settings/data-privacy-controls)**.

2. Find **US-only inference**.

3. Turn on the toggle.

The setting applies to your entire organization. Changes should take effect instantly, but may have some delay based on which of the Claude apps you’re using.

**Note:** If your organization previously opted out of global routing or has US-only inference requirements in its contract, the setting is already on and can't be changed. Your existing pricing terms continue to apply. Contact your account team with questions.

## How billing works

When US-only inference is on, your organization's usage is billed at 1.1x standard API rates for Claude Opus 4.6, Claude Sonnet 4.6, and later models. Your seat fees don't change and the 1.1x rate applies only to usage. Requests on Claude Opus 4.5, Claude Sonnet 4.5, Claude Haiku 4.5, or earlier models are billed at the standard rate.

Learn more about **[how you're billed for your Enterprise plan](https://support.claude.com/en/articles/11526368-how-am-i-billed-for-my-enterprise-plan)**.

## What US-only inference doesn't cover

US-only inference applies to inference only, where Claude's models process your requests.

It doesn't control:

- **Connectors and third-party services.** When Claude works with a connected service like Slack or Google Drive, that service processes data on its own infrastructure, which may be located outside the US. The US-only inference setting doesn't change where third-party services operate.

- **Data storage.** Where your organization's data is stored is separate from where inference runs.

## Frequently asked questions

### Who can see and change this setting?

Primary Owners, Owners, and members with a custom role that has the Privacy permission set to "Can manage" can change the setting. Members with Privacy set to "Can view" can see it but can't change it.

### Does this setting apply to the Claude API?

This setting applies to your Claude Enterprise organization. For inference location options on the Claude API, see the **[data residency documentation on Claude API Docs](https://platform.claude.com/docs/en/manage-claude/data-residency)**.

### Why don't I see this setting?

US-only inference is only available on usage-based Enterprise plans. If your organization is on a Team plan or a legacy seat-based Enterprise plan, the setting won't appear.