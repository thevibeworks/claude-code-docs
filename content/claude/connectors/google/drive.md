> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Google Drive integration

> Connect Google Docs directly to Claude

The Google Drive integration lets you connect Google Docs directly to Claude on paid Claude.ai plans. You can add documents by pasting URLs or selecting recent files to provide context for your conversations.

<Note>
  Available on Pro, Max, Team, and Enterprise plans.
</Note>

## How to add Google Docs

### In chats

1. Click the plus sign (+) in the chat interface
2. Select "Add from Google Drive"
3. Authenticate with Google on first use
4. Search recent documents or paste a document URL
5. Claude accesses and processes the document when you send your message

### In projects

The integration works only in private projects:

1. Click "Add Content" in project knowledge
2. Select "Google Drive"
3. Authenticate on first use
4. Search or paste a document URL
5. The document becomes available to Claude within that project

## Supported file types

| Type                 | Supported | Notes                            |
| -------------------- | --------- | -------------------------------- |
| Google Docs          | ✅         | Up to 10MB, text extraction only |
| Google Sheets        | ❌         | Not currently supported          |
| Google Slides        | ❌         | Not currently supported          |
| Images in docs       | ❌         | Not extracted                    |
| Comments/Suggestions | ❌         | Not extracted                    |

<Tip>
  Convert .docx files by opening in Google Docs, clicking "File," then "Save as Google Docs."
</Tip>

## Key features

* **Live sync**: Documents continue syncing with the latest Google Drive version
* **Multiple documents**: Add multiple docs if they fit the context window
* **Permission-based**: You can only sync documents you have permission to view

## Frequently asked questions

<AccordionGroup>
  <Accordion title="Do documents update after I add them?">
    Yes, documents continue syncing with the latest Google Drive version.
  </Accordion>

  <Accordion title="Can I add multiple documents?">
    Yes, you can add multiple docs as long as they fit within the context window.
  </Accordion>

  <Accordion title="What happens if I lose access to a document?">
    You'll lose document preview access but your conversation history remains.
  </Accordion>
</AccordionGroup>

## Troubleshooting

For reconnection errors:

1. Navigate to **Customize > Connectors**
2. Find Google Drive
3. Click the menu button (...)
4. Select "Disconnect"
5. Authenticate again when prompted

For persistent issues, disconnect from Google account connections at [myaccount.google.com](https://myaccount.google.com), search "Claude for Google Drive," and delete all connections.

## Related topics

<Columns cols={2}>
  <Card title="Gmail" icon="envelope" href="/docs/connectors/google/gmail">
    Search and analyze your emails.
  </Card>

  <Card title="Google Calendar" icon="calendar" href="/docs/connectors/google/calendar">
    Access your calendar information.
  </Card>
</Columns>
