> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Use Claude for Excel

> An Excel add-in that integrates Claude into your spreadsheet workflow, for Pro, Max, Team, and Enterprise plans.

Claude for Excel is an add-in that brings Claude into Excel. Ask questions
about open workbooks, adjust assumptions while preserving formula
relationships, debug errors, and build or populate models, all without
leaving Excel.

<Note>
  Claude for Excel is generally available to Pro, Max, Team,
  and Enterprise plans.
</Note>

## What you can do

With Claude for Excel, you can:

* Ask questions about your workbook and get answers with cell-level
  citations.
* Adjust assumptions while keeping formula relationships intact.
* Identify and resolve errors and their root causes.
* Generate new spreadsheet models or populate existing templates.
* Work across multi-tab workbooks.
* Pull external context through connectors such as S\&P Global, LSEG,
  and Daloopa.
* Apply enabled Skills automatically while you work.

## Get started with Claude for Excel

### Supported versions

Claude for Excel runs on the following Excel builds.

* Excel on the web
* Excel on Windows with a Microsoft 365 subscription, build 16.0.13127.20296 or later
* Excel on Mac, version 16.46 or later, build 21011600 or later

### Install for yourself

<Steps>
  <Step title="Open the marketplace listing">
    Go to the [Claude for Microsoft 365 listing on Microsoft AppSource](https://marketplace.microsoft.com/en-us/product/office/WA200010725?tab=Overview).
  </Step>

  <Step title="Install the add-in">
    Select "Get it now" to install.
  </Step>

  <Step title="Sign in">
    Open Excel, activate the add-in, and sign in with your Claude account.
  </Step>
</Steps>

### Deploy to your organization

Organization admins can deploy Claude for Excel through the Microsoft 365
Admin Center.

<Steps>
  <Step title="Allow Office Store access">
    In the [Microsoft 365 Admin Center](https://admin.microsoft.com), go
    to Settings, Org Settings, User owned apps and services, and turn on
    ["Let users access the Office Store"](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-addins-in-the-admin-center).
  </Step>

  <Step title="Open Integrated apps">
    Go to Settings, Integrated apps, Add-ins.
  </Step>

  <Step title="Find the add-in">
    Search for "Claude for Microsoft 365" in Microsoft AppSource.
  </Step>

  <Step title="Deploy">
    Assign the add-in to your organization or to specific users or
    groups. Share [Microsoft's deployment guide](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-deployment-of-add-ins)
    with your team for activation steps.
  </Step>
</Steps>

<Note>
  If your organization uses Microsoft Entra Privileged Identity
  Management (PIM) for admin roles, the Integrated apps page does not
  recognize roles activated through PIM, so deployment fails. This is a
  [known Microsoft issue](https://learn.microsoft.com/en-us/office/dev/add-ins/resources/resources-office-add-in-known-issues),
  tracking ID 11126536. To work around it, deploy from an admin account
  with the required role assigned as permanently active rather than
  PIM-eligible. See
  [Microsoft's troubleshooting guidance](https://learn.microsoft.com/en-us/troubleshoot/microsoft-365/admin/miscellaneous/cannot-deploy-add-in-integrated-apps-menu).
  Individual users can still
  [install the add-in themselves](#install-for-yourself).
</Note>

After deployment, users can activate the Claude add-in from Tools,
Add-ins on Mac or Home, Add-ins on Windows, sign in, and start working.

For environments where "Let users access the Office Store" is disabled,
deploy using the custom manifest XML file instead. Download the
[Excel manifest XML file](https://pivot.claude.ai/manifest-excel.xml),
then follow
[Deploy with a custom manifest](/docs/office-agents/word#deploy-with-a-custom-manifest)
for the upload steps. The flow is identical apart from which manifest
file you upload in Step 1.

### Connect through a third-party platform

If your organization routes AI traffic through Amazon Bedrock, Google Cloud
Vertex AI, Azure AI Foundry, or an LLM gateway, your admin can deploy
the add-in without individual Claude accounts. See
[Use Claude for M365 with third-party platforms](/docs/office-agents/third-party-platforms).

## Key features

### Understand complex models

Ask Claude to trace assumptions, explain formulas, or walk through how a
number was derived. Answers include cell-level citations you can click
to navigate to the referenced cell.

Example prompts:

* "Walk me through how the revenue number in cell C42 is calculated."
* "What assumptions drive the gross margin forecast?"

### Update values safely

Claude updates cell values while keeping formula relationships intact,
so downstream cells recompute correctly.

Example prompts:

* "Change the discount rate to 8% and update dependent calculations."
* "Flex the growth rate from 5% to 10% and show me the impact on terminal
  value."

### Build templates and models

Populate an existing template or generate a new model from a natural
language description.

Example prompts:

* "Populate this LBO template with a \$500M purchase price and 6x
  leverage."
* "Build a three-statement model from this trial balance."

### Debug errors

Locate the root cause of calculation errors and suggest fixes.

Example prompts:

* "Find the source of the #REF! error in the summary tab."
* "Trace why cell H15 is returning #DIV/0."

### Native Excel operations

Claude can sort, filter, edit pivot tables, apply conditional
formatting, and create data validation dropdowns. Ask for these
directly.

## Connectors and Skills

Claude for Excel supports connectors for pulling external context into
your workbook, and Skills for applying reusable task recipes. See
[Connectors and Skills](/docs/office-agents/connectors-and-skills) for
details.

## Set persistent instructions

Open Settings in the add-in sidebar and use the Instructions field to
set preferences that
apply to every conversation in Excel. Instructions are useful for
formatting conventions such as "format numbers with thousand separators"
or "always bold column headers", currency or locale preferences, or
recurring context about your workflow.

Instructions you set in Excel only apply to Excel. They are separate
from Instructions you set in PowerPoint or Word.

## Work across M365 apps

Claude for Excel shares context with Claude for PowerPoint, Word, and
Outlook, so a single conversation can span your open workbook,
presentation, document, and inbox. See
[Work across M365 apps](/docs/office-agents/work-across-apps).

## Context and session management

The add-in handles long sessions and protects against accidental
overwrites for you.

* **Auto-compaction**: longer conversations are automatically compacted
  into new conversations to avoid running out of context. See
  [Understanding usage and length limits](https://support.claude.com/en/articles/11647753-understanding-usage-and-length-limits).
* **Overwrite protection**: Claude warns you before overwriting existing
  data to avoid accidental data loss.

Your use of Claude for Excel is associated with your existing Claude
account and is subject to the same usage limits.

## Models available

Claude for M365 offers a curated subset of the Claude models: the ones
that work best for Office tasks, so the list you see in the add-in can
be shorter than what you see in Claude.ai. Your organization's model
access settings also apply, and a model appears here only if your role
permits it. See
[Manage model access for your organization](https://support.claude.com/en/articles/15694740-manage-model-access-for-your-organization)
for how those settings interact with each product. If you connect
through Amazon Bedrock, Google Cloud Vertex AI, Azure AI Foundry, or an
LLM gateway, the available models come from that platform and your
admin's configuration instead of your Claude.ai model access settings.
See [Use Claude for M365 with third-party platforms](/docs/office-agents/third-party-platforms)
for details.

## Data handling

Inputs and outputs are deleted on the backend within 30 days of receipt
or generation, except in cases outlined in
[How long do you store my organization's data?](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data).
Data is cached for a number of hours after deletion so users can access
context in recently closed workbooks.

Chat history is stored locally in your browser using IndexedDB.
Conversations are not stored on Anthropic's servers, are not synced
across devices, and can be cleared from Settings at any time.
Reinstalling the add-in or switching between Claude add-ins does not
remove it. See [Data storage and retention](/docs/office-agents/data-storage)
for where it sits on disk and how long it is kept.

Claude for Excel does not inherit custom data retention settings your
organization might have set. Activity is not included in Enterprise
audit logs or the Compliance API.

## Current limitations

Claude for Excel is not recommended for:

* Final client deliverables without human review.
* Audit-critical calculations without verification.
* Models containing highly sensitive or regulated data without proper
  controls.

Unsupported capabilities:

* Data tables.
* Macros and VBA operations.

### Unsupported versions

The add-in does not run on these Excel versions.

* Excel 2016 and 2019 perpetual or volume license.
* Excel on iPad. The add-in requires SharedRuntime support, which iPad
  does not provide.
* Excel on Android.
* Older builds of Microsoft 365 Excel below the SharedRuntime threshold.

## Prompt injection risk

<Warning>
  Only use Claude for Excel with trusted spreadsheets. Files from external
  sources can contain hidden instructions that manipulate the add-in into
  extracting data, modifying records, or performing destructive actions.
</Warning>

External files such as downloaded templates, vendor files, and data
imports can contain prompt injections that try to trick Claude into
taking unintended actions. Testing has identified scenarios where Claude for
Excel can be manipulated to extract sensitive information, modify
critical data, or perform destructive actions if allowed to act without
verification.

When Claude proposes a risky operation, you are asked to confirm before
it runs. Review confirmations carefully, especially for files from
external sources.

## Best practices

Follow these guidelines to use Claude for Excel safely and effectively.

* Always review changes before finalizing your work.
* Start with a trusted copy of the workbook before asking Claude to edit
  widely.
* Be specific about what you want changed.
* Verify that outputs match your organization's standards and your own
  judgment.
