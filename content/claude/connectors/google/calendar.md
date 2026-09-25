> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Google Calendar

> Connect the Google Calendar connector so Claude can answer questions about your meetings, attendees, and availability.

The Google Calendar connector lets Claude read your calendar so it can answer questions about your meetings, attendees, and availability. It's available on Pro, Max, Team, and Enterprise plans. On Team and Enterprise plans, an Owner or Primary Owner enables it for the organization before members can connect.

By the end of this page you have connected your Google account and asked Claude a first question about your schedule. Claude reads your calendar only; it can't create or change events or send invitations.

<Note>
  If your organization uses Outlook or Teams calendars, see [Microsoft 365](/docs/connectors/microsoft/365) instead.
</Note>

## Connect Google Calendar

You connect Google Calendar once from your connector settings, and Claude can then read your calendar in any conversation where you turn the connector on.

<Steps>
  <Step title="Open your connectors">
    Go to [**Customize > Connectors**](https://claude.ai/customize/connectors) in claude.ai. **Customize** is the page that holds your connectors, skills, and plugins.
  </Step>

  <Step title="Connect Google Calendar">
    Find **Google Calendar** in the list and select **Connect**.
  </Step>

  <Step title="Sign in to Google">
    Sign in to your Google account and grant the requested permissions.
  </Step>
</Steps>

When the connection succeeds, the **Connect** button on the Google Calendar connector changes to **Disconnect**.

On Team and Enterprise plans, Google Calendar doesn't appear in your connector list until an Owner or Primary Owner enables it for your organization. For the full walkthrough, including troubleshooting, see [Get started with connectors](/docs/connectors/getting-started).

## Try the connector

In a conversation, select **+** at the lower left of the message box, select **Connectors**, and turn on **Google Calendar**. Then ask a question about your schedule. Claude detects when calendar data is needed and reads your calendar to answer. For example, ask Claude:

* What meetings do I have tomorrow?
* When is my next meeting with the product team?
* Do I have any conflicts next week?
* Who's attending the budget review meeting?

Claude's answer includes citations that show which calendar events it used, with links to the original events where applicable. You can follow up in the same conversation to ask about attendees, event timing and duration, or related meetings and patterns.

## Privacy and data handling

You authenticate directly with your Google account, and Claude's access follows these rules:

* Claude accesses only data from the Google account you connected
* Claude reads your calendar only when your request calls for it
* Claude retrieves the minimum information needed to answer your question
* Your existing calendar permissions apply, so Claude can search only the calendars you can access

## Limitations

The connector is read-only:

* Claude can't create, modify, or delete calendar events
* Claude can't send calendar invitations
* Claude can search only the calendars you have access to

## Next steps

* [Gmail](/docs/connectors/google/gmail): search and analyze your emails
* [Google Drive](/docs/connectors/google/drive): search and read your Drive files
* [Connectors directory](/docs/connectors/directory): browse verified and community integrations
