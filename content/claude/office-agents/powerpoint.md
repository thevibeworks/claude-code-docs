> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Use Claude for PowerPoint

> A PowerPoint add-in that integrates Claude into your presentation workflow, for Pro, Max, Team, and Enterprise plans.

Claude for PowerPoint is an add-in that brings Claude into PowerPoint.
Build decks from scratch, edit specific slides without regenerating
everything, convert bullets into diagrams and native charts, and iterate
on feedback while preserving template compliance.

<Note>
  Claude for PowerPoint is generally available to Pro, Max,
  Team, and Enterprise plans.
</Note>

## What you can do

With Claude for PowerPoint, you can:

* Build new slides using your existing client or corporate templates.
* Make pinpoint edits to specific slides without regenerating entire
  decks.
* Generate full deck structures from natural language descriptions.
* Convert bullets into diagrams and native PowerPoint charts.
* Pull external context through connectors.
* Iterate on feedback while preserving formatting and template
  compliance.

## Get started with Claude for PowerPoint

### Supported versions

Claude for PowerPoint runs on the following PowerPoint builds.

* PowerPoint on the web
* PowerPoint on Windows with a Microsoft 365 subscription, build 16.0.13127.20296 or later
* PowerPoint on Mac, version 16.46 or later

### Install for yourself

<Steps>
  <Step title="Open the marketplace listing">
    Go to the [Claude for Microsoft 365 listing on Microsoft AppSource](https://marketplace.microsoft.com/en-us/product/office/WA200010725?tab=Overview).
  </Step>

  <Step title="Install the add-in">
    Select "Get it now" to install.
  </Step>

  <Step title="Sign in">
    Open PowerPoint, activate the add-in, and sign in with your Claude
    account.
  </Step>
</Steps>

### Deploy to your organization

Organization admins can deploy Claude for PowerPoint through the
Microsoft 365 Admin Center.

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

<Warning>
  Organizations that have disabled "Let users access the Office Store" may
  find that admin-deployed add-ins don't appear for users. To work around
  this, deploy using the manifest XML file described below.
</Warning>

### Deploy with a custom manifest

For IT administrators deploying to multiple users when the Office Store
is disabled:

<Steps>
  <Step title="Download the manifest">
    Download the [custom manifest XML file](https://pivot.claude.ai/manifest-powerpoint.xml)
    and save it to a secure location.
  </Step>

  <Step title="Open the Admin Center">
    Go to [https://admin.microsoft.com](https://admin.microsoft.com),
    sign in, and open Settings, Integrated apps.
  </Step>

  <Step title="Upload the custom add-in">
    Select "Upload custom apps", choose "Office Add-in", then
    "I have a manifest file on this device". Upload the manifest.
  </Step>

  <Step title="Assign users">
    Choose entire organization, specific users, specific groups, or just
    yourself for admin testing.
  </Step>

  <Step title="Deploy">
    Review settings and select "Deploy". The add-in is available within
    minutes. Full organization rollout can take up to 24 hours.
  </Step>
</Steps>

After deployment, users see Claude in PowerPoint's Home ribbon and sign
in with their Claude credentials on first use.

### Connect through a third-party platform

If your organization routes AI traffic through Amazon Bedrock, Google Cloud
Vertex AI, Azure AI Foundry, or an LLM gateway, your admin can deploy
the add-in without individual Claude accounts. See
[Use Claude for M365 with third-party platforms](/docs/office-agents/third-party-platforms).

## Key features

### Build from templates

Start with a client or corporate template already loaded. Describe what
you need, and Claude generates slides using the correct layouts, fonts,
and colors from the slide master. Claude reads your deck's template and
respects its formatting rules.

Example prompts:

* "Create a market sizing section, 3 slides covering TAM, SAM, SOM with
  supporting visuals."
* "Add an executive summary slide using the one-column content layout."

### Edit existing slides

Select a slide and tell Claude what to change. Claude makes edits while
preserving formatting and surrounding context.

Example prompts:

* "Simplify the text on this slide."
* "Add a chart showing the quarterly trend."
* "Restructure the storyline across slides 4 to 7."

### Generate full decks

Open a blank deck and describe your goal. Claude builds a draft with
logical structure and professional defaults, which you can refine.

Example prompts:

* "Create a 10-slide deck walking through our market entry hypotheses."
* "Build an internal project update presentation with timeline and next
  steps."

### Create native charts and diagrams

Convert bullet points into professional visuals such as diagrams, process
flows, or editable native PowerPoint charts. Claude produces visuals you
can edit directly, not static images.

Example prompts:

* "Turn these bullets into a process flow diagram."
* "Create a bar chart comparing Q1 to Q4 performance."

### Template awareness

Claude reads the slide master, layouts, fonts, and color scheme in your
deck and uses them when generating or editing slides. It aims to
maintain template compliance without introducing off-brand elements.

## Connectors and Skills

Claude for PowerPoint supports connectors for pulling external context
into your deck, and Skills for applying reusable task recipes. See
[Connectors and Skills](/docs/office-agents/connectors-and-skills) for
details.

## Set persistent instructions

Open Settings in the add-in sidebar and use the Instructions field to
set preferences that
apply to every conversation in PowerPoint. Instructions are useful for
brand guidelines such as "always use one-line bullets" or "use the blue
accent color for highlights", preferred slide structure, or recurring
context about your workflow.

Instructions you set in PowerPoint only apply to PowerPoint. They are
separate from Instructions you set in Excel or Word.

## Work across M365 apps

Claude for PowerPoint shares context with Claude for Excel, Word, and
Outlook, so a single conversation can span your open deck, workbook,
document, and inbox. See
[Work across M365 apps](/docs/office-agents/work-across-apps).

## Context and session management

The add-in handles long sessions for you so a single conversation can
span an entire workflow.

* **Auto-compaction**: longer conversations are automatically compacted
  into new conversations to avoid running out of context. See
  [Understanding usage and length limits](https://support.claude.com/en/articles/11647753-understanding-usage-and-length-limits).

Your use of Claude for PowerPoint is associated with your existing
Claude account and is subject to the same usage limits.

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
context in recently closed presentations.

Chat history is stored locally in your browser using IndexedDB.
Conversations are not stored on Anthropic's servers, are not synced
across devices, and can be cleared from Settings at any time.
Reinstalling the add-in or switching between Claude add-ins does not
remove it. See [Data storage and retention](/docs/office-agents/data-storage)
for where it sits on disk and how long it is kept.

Claude for PowerPoint does not inherit custom data retention settings
your organization might have set. Activity is not included in Enterprise
audit logs or the Compliance API.

## Current limitations

Claude for PowerPoint is not recommended for:

* Final client deliverables without human review.
* Presentations containing highly sensitive or regulated data without
  proper controls.
* Replacing your judgment on design and narrative flow.

### Unsupported versions

The add-in does not run on these PowerPoint versions.

* PowerPoint 2016 and 2019 perpetual or volume license.
* PowerPoint on iPad.
* PowerPoint on Android.
* Older builds of Microsoft 365 PowerPoint below the SharedRuntime
  threshold.

## Prompt injection risk

<Warning>
  Only use Claude for PowerPoint with trusted files. Files from external
  sources can contain hidden instructions that manipulate the add-in into
  extracting data, modifying records, or performing destructive actions.
</Warning>

External files such as downloaded templates, vendor files,
collaborative documents, and data imports can contain prompt injections that try to trick
Claude into taking unintended actions. Testing has identified scenarios
where Claude for PowerPoint can be manipulated to extract sensitive
information, modify critical data, or perform destructive actions if
allowed to act without verification.

When Claude proposes a risky operation, you are asked to confirm before
it runs. Review confirmations carefully, especially for files from
external sources.

## Best practices

Follow these guidelines to use Claude for PowerPoint safely and
effectively.

* Always review changes before finalizing your work.
* Start with your template already applied before asking Claude to
  generate content.
* Be specific about what you want changed. Claude can target individual
  slides or elements.
* Verify that outputs match your organization's brand guidelines.

## Example use cases

### Consulting deliverables

Prompts that produce client-ready sections and summaries.

* "Build a market sizing section with TAM, SAM, SOM slides."
* "Create a competitive landscape slide comparing 4 players."
* "Summarize these survey results."

### Iterative refinement

Prompts that tighten or restructure an existing deck.

* "Simplify the text on slide 3, it's too dense."
* "Combine slides 5 and 6 into a single summary."
* "Make the recommendations section more visual."

### Data visualization

Prompts that turn raw data into native charts and diagrams.

* "Convert these bullet points into a process flow."
* "Create a bar chart from this data table."
* "Add a pie chart showing market share breakdown."

### Deck restructuring

Prompts that reorder or re-sequence slides.

* "Reorder slides to lead with recommendations first."
* "Add transition slides between each major section."
* "Create an agenda slide that reflects the current structure."
