> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Use Claude for Word

> A Word add-in that integrates Claude into your document workflow, for Pro, Max, Team, and Enterprise plans.

Claude for Word is an add-in that brings Claude into Word. Ask questions
about your document with clickable section citations, edit selected
passages while preserving formatting, review counterparty redlines,
work through comment threads, and fill templates in your document's
styles.

<Note>
  Claude for Word is generally available to Pro, Max, Team,
  and Enterprise plans.
</Note>

## What you can do

With Claude for Word, you can:

* Ask questions about your document and get answers with clickable
  section citations.
* Edit selected text while preserving surrounding styles, numbering,
  and formatting.
* Use tracked changes mode so every edit lands as a revision you can
  accept or reject in Word's native review pane.
* Have Claude work through comment threads, editing the anchored text
  and replying with what it changed.
* Summarize counterparty redlines and flag the revisions worth pushing
  back on.
* Fill templates with drafted content that inherits your document's
  heading and paragraph styles.
* Find every provision touching a theme with semantic navigation, not
  just keyword search.

## Get started with Claude for Word

### Supported versions

Claude for Word runs on the following Word builds.

* Word on the web
* Word on Windows with a Microsoft 365 subscription, Version 2205,
  build 15202.10000 or later
* Word on Mac, version 16.61, build 22040100 or later

### Install for yourself

<Steps>
  <Step title="Open the marketplace listing">
    Go to the [Claude for Microsoft 365 listing on Microsoft AppSource](https://marketplace.microsoft.com/en-us/product/office/WA200010725?tab=Overview).
  </Step>

  <Step title="Install the add-in">
    Select "Get it now" to install.
  </Step>

  <Step title="Sign in">
    Open Word, activate the add-in, and sign in with your Claude
    account.
  </Step>
</Steps>

### Deploy to your organization

Organization admins can deploy Claude for Word through the Microsoft
365 Admin Center.

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
    Download the [custom manifest XML file](https://pivot.claude.ai/manifest-word.xml)
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

After deployment, users see Claude in Word's Home ribbon and sign in
with their Claude credentials on first use.

### Connect through a third-party platform

If your organization routes AI traffic through Amazon Bedrock, Google Cloud
Vertex AI, Azure AI Foundry, or an LLM gateway, your admin can deploy
the add-in without individual Claude accounts. See
[Use Claude for M365 with third-party platforms](/docs/office-agents/third-party-platforms).

## Key features

### Read and understand documents

Ask Claude questions about specific sections, clauses, or defined terms
in your document. Claude provides answers with clickable citations that
navigate directly to the referenced section.

<Note>
  Claude recognizes common document patterns including multi-level legal
  numbering, defined terms, cross-references, and standard contract
  structures. Verify that outputs match your specific requirements and
  your firm's standard positions.
</Note>

Example prompts:

* "What's the liability cap and is it mutual?"
* "Summarize the key commercial terms in this agreement."
* "What assumptions drive the revenue forecast in section 3?"

### Edit selected text

Select a passage and tell Claude what to change. Claude edits only the
selection while preserving surrounding styles, numbering, and
formatting. New text inherits the paragraph style, font, and numbering
of the surrounding content.

Example prompts:

* "Tighten this paragraph and drop the passive voice."
* "Rewrite this clause to make the indemnification mutual."
* "Simplify this section for a non-technical audience."

### Tracked changes mode

When you enter tracked changes mode, Claude's edits land as tracked
revisions. The original text is visible as a deletion and the new text
as an insertion, all reviewable in Word's native review pane. Review
every edit before accepting it, and undo with Word's standard Ctrl+Z
on Windows or Cmd+Z on Mac if you want to revert.

Example prompts:

* "Rewrite section 4.2 to cap damages at 12 months of fees, and make it
  mutual."
* "Draft a mutual indemnification clause after section 8."

### Comment-driven editing

Claude reads comment threads in your document, understands what text
each thread is anchored to, and can work through them one by one. For
each comment, Claude edits the anchored passage and replies to the
thread with a note explaining what it did.

Example prompts:

* "Work through my open comments."
* "Address the comment on the liability section."

### Summarize counterparty redlines

When a counterparty returns a document with tracked changes, Claude can
read and summarize what they changed. Ask Claude to group changes by
severity or flag the ones worth pushing back on.

Example prompts:

* "Summarize what the other side changed and flag anything that's worth
  discussing."
* "Which of these redlines are dealbreakers?"

### Fill templates

Draft sections in your document's heading and paragraph styles. Claude
uses your template's formatting when generating content, so new
headings, bullets, and table entries match what's already there. Tables
populate in place without reflowing layout or changing column widths.

Example prompts:

* "Draft the Key Risks section with four risks in the template's style."
* "Populate the summary table with revenue, gross margin, and net
  retention for the last three years."

### Semantic navigation

Find every provision or passage in your document that touches a
specific theme. Claude returns thematic matches, not just keyword hits,
and each result navigates to the relevant location on click.

Example prompts:

* "Find every provision touching data retention."
* "Where does this agreement address termination?"

## Connectors and Skills

Claude for Word supports connectors for pulling external context into
your document, and Skills for applying reusable task recipes. See
[Connectors and Skills](/docs/office-agents/connectors-and-skills) for
details.

## Set persistent instructions

Open Settings in the add-in sidebar and use the Instructions field to
set preferences that
apply to every conversation in Word. Instructions are useful for tone
and style conventions such as "use formal tone" or "follow APA citation
style", document structure preferences, or recurring context about your
workflow.

Instructions you set in Word only apply to Word. They are separate from
Instructions you set in Excel or PowerPoint.

## Work across M365 apps

Claude for Word shares context with Claude for Excel, PowerPoint, and
Outlook, so a single conversation can span your open document,
workbook, deck, and inbox. See
[Work across M365 apps](/docs/office-agents/work-across-apps).

## Context and session management

The add-in handles long sessions for you so a single conversation can
span an entire workflow.

* **Auto-compaction**: longer conversations are automatically compacted
  into new conversations to avoid running out of context. See
  [Understanding usage and length limits](https://support.claude.com/en/articles/11647753-understanding-usage-and-length-limits).

Your use of Claude for Word is associated with your existing Claude
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
context in recently closed documents.

Chat history is stored locally in your browser using IndexedDB.
Conversations are not stored on Anthropic's servers, are not synced
across devices, and can be cleared from Settings at any time.
Reinstalling the add-in or switching between Claude add-ins does not
remove it. See [Data storage and retention](/docs/office-agents/data-storage)
for where it sits on disk and how long it is kept.

Claude for Word does not inherit custom data retention settings your
organization might have set. Activity is not included in Enterprise
audit logs or the Compliance API.

Claude reads the content of your currently open document, including
text, comments, tracked changes, footnotes, tables, and bookmarks. It
only accesses the document you have open in Word. For highly sensitive
or regulated data, follow your organization's data handling policies.

## Current limitations

Claude for Word is not recommended for:

* Final client deliverables or counterparty sends without human review.
* Litigation filings or audit-critical documents without verification.
* Replacing legal or financial judgment.
* Documents containing highly sensitive or privileged data without
  proper controls.

### Unsupported versions

The add-in does not run on these Word versions.

* Word 2016 and 2019 perpetual or volume license.
* Word on iPad.
* Word on Android.
* Microsoft 365 Word builds older than Version 2205 on Windows or
  version 16.61 on Mac.
* Legacy `.doc` files. Save as `.docx` first.

## Prompt injection risk

<Warning>
  Only use Claude for Word with trusted documents. Documents from external
  sources such as downloaded templates, counterparty files, or files
  shared via email can contain hidden instructions that manipulate the
  add-in into extracting data, modifying records, or performing
  destructive actions.
</Warning>

Prompt injection attacks hide malicious instructions in document
content such as text, comments, tracked changes, headers, and footers
to trick Claude into taking unintended actions. Testing has identified
scenarios where Claude for Word can be manipulated to:

* Extract and share sensitive information through web searches
  containing your sensitive data or file system access that exposes
  proprietary information.
* Modify critical content such as contract terms or financial figures.
* Perform destructive actions without verification when allowed to act
  unsupervised.

When Claude proposes a risky operation, you are asked to confirm before
it runs. Review confirmations carefully, especially for content from
external sources.

## Best practices

Follow these guidelines to use Claude for Word safely and effectively.

* Always review tracked changes before accepting them.
* Verify that outputs match your firm's playbook and standard
  positions.
* Use appropriate permissions and access controls.
* Maintain human oversight for client-facing work.

## Example use cases

### Legal contract review

Prompts that review and revise contracts and counterparty redlines.

* "Summarize the key commercial terms: parties, term, governing law,
  and anything off-market."
* "Flag provisions that deviate from standard market position, ranked
  by severity."
* "Make the indemnification mutual and insert our standard fallback
  language."
* "Work through all five reviewer comments as tracked changes."
* "What did the counterparty change, and which revisions are
  dealbreakers?"

### Finance memo drafting

Prompts that build out investment memos and finance writeups.

* "Draft the Investment Thesis section with three points, pulling the
  numbers from the uploaded 10-K."
* "Populate the summary table with revenue, gross margin, and FCF for
  the last three years."
* "Too generic on point two. Use the customer count from the deck."
* "Address the partner's comment on the Risks section."

### Document QA and consistency

Prompts that check a document for internal consistency and quality.

* "Flag inconsistent defined terms and broken cross-references."
* "Check the numbering scheme for gaps."
* "Proofread for spelling, grammar, and punctuation."
* "Is the same party referred to by different names anywhere in this
  document?"

### General document editing

Prompts that tighten or restructure prose.

* "Tighten section 4 and drop the passive voice."
* "Rewrite this for a non-technical audience."
* "Add a fourth risk addressing customer concentration."
* "Define this term and use it consistently throughout."
