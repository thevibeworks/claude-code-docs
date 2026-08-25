> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Gmail integration

> Search and analyze emails with Claude

The Gmail integration enables Claude to search your emails and provide answers based on your email content, reducing time spent retrieving information.

<Note>
  Available on Pro, Max, Team, and Enterprise plans.
</Note>

## Connect Gmail

1. In claude.ai, go to **Customize > Connectors**.
2. Find Gmail and click **Connect**.
3. Sign in to your Google account and grant the requested permissions.

On Team and Enterprise plans, an Owner or Primary Owner must enable the integration for your organization before it appears in your connector list. For the full walkthrough, including troubleshooting, see [Get started with connectors](/docs/connectors/getting-started).

## How to use Gmail integration

### 1. Ask a question

Simply ask Claude a question that needs email information. Claude automatically detects when email data is needed.

**Example questions:**

* "What did Sarah say about the project deadline?"
* "Find emails about the Q4 budget review"
* "Summarize my conversation with the sales team last week"

### 2. Review Claude's response

Claude provides answers that include:

* Clear answers to your questions
* Citations indicating which emails were used
* Links to original sources when applicable

### 3. Follow up

You can ask for more details, such as:

* Requesting additional email information
* Finding related threads
* Summarizing longer conversations

## Understanding citations

Citations show which specific emails Claude used to answer your question. You can follow links back to original sources for verification and additional context.

## Privacy and data handling

### Authentication

You must authenticate directly to your Google account. For Claude for Work (Team/Enterprise) plans, an Owner or Primary Owner must enable integrations at the account level.

### Data access

* Claude accesses only data from your connected Google account
* Access occurs only when you explicitly request it
* Minimum information is retrieved to answer your question
* Your existing Gmail permissions are mirrored

## Limitations

<Warning>
  * Claude cannot create, send, or modify emails
  * Embedded images in emails are not visible to Claude
  * Only emails you have access to can be searched
</Warning>

## Related topics

<Columns cols={2}>
  <Card title="Google Calendar" icon="calendar" href="/docs/connectors/google/calendar">
    Access your calendar information.
  </Card>

  <Card title="Google Drive" icon="google-drive" href="/docs/connectors/google/drive">
    Connect your documents.
  </Card>
</Columns>
