> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Work across M365 apps

> Let Claude read from one Microsoft 365 app and make changes in another in a single conversation.

Claude can coordinate between the Excel, PowerPoint, Word, and Outlook
add-ins in your Microsoft 365 suite. Instead of switching between apps
and re-providing context each time, Claude can read from one app and
make changes in another.

<Note>
  Working across apps is available when you sign in with your Claude
  account directly. It is not supported when connecting through Amazon
  Bedrock, Google Cloud Vertex AI, Azure AI Foundry, or an LLM gateway.
</Note>

## Requirements

Install each Claude for M365 add-in and confirm your plan before turning
on cross-app mode.

* A paid Claude plan: Pro, Max, Team, or Enterprise.
* [Claude for Excel](/docs/office-agents/excel) installed from the
  Microsoft AppSource.
* [Claude for PowerPoint](/docs/office-agents/powerpoint) installed
  from the Microsoft AppSource.
* [Claude for Word](/docs/office-agents/word) installed from the
  Microsoft AppSource.
* [Claude for Outlook](/docs/office-agents/outlook) installed from the
  Microsoft AppSource.

## Enable cross-app mode

<Steps>
  <Step title="Install each add-in">
    Install Claude for Excel, PowerPoint, Word, and Outlook from the
    Microsoft AppSource. Open each app and activate the add-in at
    least once before using cross-app features.
  </Step>

  <Step title="Enable per add-in">
    Open Settings in each add-in and turn on "Let Claude work across
    files". Pro and Max plans have this on by default; Team and
    Enterprise plans default to off. The toggle is per-device, so enable
    it in every host you want to coordinate from.
  </Step>
</Steps>

Once enabled, connected-app indicators appear in the sidebar when other
Excel, PowerPoint, Word, or Outlook sessions are linked.

## How it works

When you describe a task that involves multiple files or apps, Claude
coordinates automatically:

* Claude uses the Excel, PowerPoint, Word, and Outlook add-ins to read
  from and write to open files and email threads.
* Context transfers between apps automatically, so you don't need to
  copy and paste information manually.

You stay in one place while Claude does the switching.

## What you can do

### Read and write across open apps

Claude can read data from an open Excel workbook, PowerPoint
presentation, Word document, or Outlook email thread, and make changes
to them directly. For example:

* Pull numbers from an Excel model into a PowerPoint slide or a Word
  memo.
* Update a chart in PowerPoint with the latest figures from Excel.
* Read content from a presentation and use it to populate a spreadsheet.
* Summarize a Word document into PowerPoint slides.
* Draft a Word memo using data from an Excel workbook.
* Open an attached letter of intent in Word with the Outlook thread
  already loaded as context.
* Pull figures from an email thread into an open Excel model.

### Pass context between apps

Claude carries relevant context forward when working across multiple
files. If you've been building a financial model in Excel and ask Claude
to create a summary deck or draft an investment memo, Claude already
understands the model's structure and key outputs, so you don't need to
re-explain.

## Skills work across apps

Skills you've enabled in your Claude settings apply when Claude is
working in Excel, PowerPoint, Word, or Outlook during a cross-app task. If you
have a Skill that enforces your team's modeling conventions in Excel and
another that matches your slide template in PowerPoint, Claude uses each
one in the right app as it moves through the workflow.

For more on Skills, see
[Use Skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

## Manage access as an admin

Team and Enterprise organization owners can control whether team members
can access this capability.

<Steps>
  <Step title="Open organization settings">
    Go to Organization settings, Office agents.
  </Step>

  <Step title="Toggle the setting">
    Turn "Let Claude work across apps" on or off.
  </Step>
</Steps>

Admins can also manage member access to the Claude for Excel,
PowerPoint, Word, and Outlook add-ins through the Microsoft 365 Admin
Center.

## Data handling

Inputs and outputs are deleted from Anthropic's backend within 30 days
of receipt or generation, except in cases outlined in
[How long do you store my organization's data?](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data).

The Claude for M365 add-ins do not inherit custom data retention
settings your organization may have set, and activity is not included in
Enterprise audit logs, the Compliance API, or data exports. Chat history
is stored locally in your browser, not on Anthropic's servers, and can
be cleared from Settings at any time.

## Current limitations

* Claude can only read from and write to files that are currently open
  in Excel, PowerPoint, or Word, and the email or event currently open
  in Outlook.
* Claude cannot create, open, close, or switch files directly. The files
  and add-ins must be open with the feature turned on.

## Troubleshooting

### Claude doesn't see my open file

Make sure the add-in is activated in the app (Tools, Add-ins on Mac or
Home, Add-ins on Windows) and that working across apps is turned on in
the add-in settings.

### Changes aren't appearing in the other app

Claude works on open files in sequence. Wait for Claude to finish its
current action, then check the target file. You may need to ask Claude
to refresh or re-read the file.
