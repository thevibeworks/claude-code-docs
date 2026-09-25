> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Gmail

> Connect the Gmail connector so Claude can search your email and answer questions from your messages, with citations back to each one.

The Gmail connector lets Claude search your email and answer questions from what it finds, with citations that link back to the messages it used. It's available on Pro, Max, Team, and Enterprise plans. On Team and Enterprise plans, an Owner or Primary Owner enables it for the organization before members can connect.

By the end of this page you have connected your Google account and asked Claude a first question about your email. Claude reads and searches email only; it can't create, send, or modify messages.

<Note>
  If your organization uses Outlook, see [Microsoft 365](/docs/connectors/microsoft/365) instead.
</Note>

## Connect Gmail

You connect Gmail once from your connector settings, and Claude can then search your email in any conversation where you turn the connector on.

<Steps>
  <Step title="Open your connectors">
    Go to [**Customize > Connectors**](https://claude.ai/customize/connectors) in claude.ai. **Customize** is the page that holds your connectors, skills, and plugins.
  </Step>

  <Step title="Connect Gmail">
    Find **Gmail** in the list and select **Connect**.
  </Step>

  <Step title="Sign in to Google">
    Sign in to your Google account and grant the requested permissions.
  </Step>
</Steps>

When the connection succeeds, the **Connect** button on the Gmail connector changes to **Disconnect**.

On Team and Enterprise plans, Gmail doesn't appear in your connector list until an Owner or Primary Owner enables it for your organization. For the full walkthrough, including troubleshooting, see [Get started with connectors](/docs/connectors/getting-started).

## Try the connector

In a conversation, select **+** at the lower left of the message box, select **Connectors**, and turn on **Gmail**. Then ask a question that needs your email. Claude detects when email data is needed and searches Gmail to answer. For example, ask Claude:

* What did Sarah say about the project deadline?
* Find emails about the Q4 budget review
* Summarize my conversation with the sales team last week

Claude's answer includes citations that show which emails it used, with links to the original messages where applicable, so you can open a message to verify the answer or read more context. You can follow up in the same conversation to ask for more detail, find related threads, or summarize a longer exchange.

## Privacy and data handling

You authenticate directly with your Google account, and Claude's access follows these rules:

* Claude accesses only data from the Google account you connected
* Claude searches your email only when your request calls for it
* Claude retrieves the minimum information needed to answer your question
* Your existing Gmail permissions apply, so Claude can search only the email you can access

## Limitations

The connector is read-only, and some email content isn't visible to Claude:

* Claude can't create, send, or modify emails
* Claude can't see images embedded in emails
* Claude can search only the emails you have access to

## Next steps

* [Google Calendar](/docs/connectors/google/calendar): access your calendar information
* [Google Drive](/docs/connectors/google/drive): search and read your Drive files
* [Connectors directory](/docs/connectors/directory): browse verified and community integrations
