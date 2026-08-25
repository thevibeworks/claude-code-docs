> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Google Calendar integration

> Access your calendar and meeting information with Claude

The Google Calendar integration enables Claude to understand your calendar commitments, helping you manage your schedule more effectively.

<Note>
  Available on Pro, Max, Team, and Enterprise plans.
</Note>

## Connect Google Calendar

1. In claude.ai, go to **Customize > Connectors**.
2. Find Google Calendar and click **Connect**.
3. Sign in to your Google account and grant the requested permissions.

On Team and Enterprise plans, an Owner or Primary Owner must enable the integration for your organization before it appears in your connector list. For the full walkthrough, including troubleshooting, see [Get started with connectors](/docs/connectors/getting-started).

## How to use Calendar integration

### 1. Ask about your schedule

Simply ask Claude questions about your calendar. Claude automatically detects when calendar data is needed.

**Example questions:**

* "What meetings do I have tomorrow?"
* "When is my next meeting with the product team?"
* "Do I have any conflicts next week?"
* "Who's attending the budget review meeting?"

### 2. Review Claude's response

Claude provides answers that include:

* Clear answers to your questions
* Citations indicating which calendar events were used
* Links to original events when applicable

### 3. Follow up

You can ask for more details about:

* Meeting attendees
* Event timing and duration
* Related meetings and patterns

## Privacy and data handling

### Authentication

You must authenticate directly to your Google account. For Claude for Work (Team/Enterprise) plans, an Owner or Primary Owner must enable integrations at the account level.

### Data access

* Claude accesses only data from your connected Google account
* Access occurs only when you explicitly request it
* Minimum information is retrieved to answer your question
* Your existing calendar permissions are mirrored

## Limitations

<Warning>
  * Claude cannot create, modify, or delete calendar events
  * Claude cannot send calendar invitations
  * Only calendars you have access to can be searched
</Warning>

## Related topics

<Columns cols={2}>
  <Card title="Gmail" icon="envelope" href="/docs/connectors/google/gmail">
    Search and analyze your emails.
  </Card>

  <Card title="Google Drive" icon="google-drive" href="/docs/connectors/google/drive">
    Connect your documents.
  </Card>
</Columns>
