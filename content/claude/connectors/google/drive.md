> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Google Drive

> Connect the Google Drive connector so Claude can search your Drive, read Docs, Sheets, Slides, and PDFs, and use Drive files in chats and projects.

The Google Drive connector lets Claude search your Google Drive, read the files it finds, and create new files there. Google builds and runs the connector, and each person who uses it signs in with their own Google account, so Claude can reach only the files that account can open. Once you connect it, you can turn it on in any Claude conversation and pick Drive files to add to a chat or to a project's knowledge.

To get going, [connect Google Drive](#connect-google-drive) and then [try a first question](#try-the-connector).

<Note>
  If you want Claude to search your email or calendar rather than your files, see [Gmail](/docs/connectors/google/gmail) or [Google Calendar](/docs/connectors/google/calendar).
</Note>

## Connect Google Drive

You connect Google Drive once from your connector settings, and Claude can then use it in any conversation where you turn the connector on.

<Steps>
  <Step title="Open your connectors">
    Go to [**Customize > Connectors**](https://claude.ai/customize/connectors) in claude.ai. **Customize** is the page that holds your connectors, skills, and plugins.
  </Step>

  <Step title="Connect Google Drive">
    Find **Google Drive** in the list and select **Connect**.
  </Step>

  <Step title="Sign in to Google">
    Sign in to your Google account and grant the requested permissions.
  </Step>
</Steps>

When the connection succeeds, the **Connect** button on the Google Drive connector changes to **Disconnect**.

On Team and Enterprise plans, Google Drive doesn't appear in your connector list until an Owner adds it for your organization. Each member then connects their own Google account. For the full walkthrough, including troubleshooting, see [Get started with connectors](/docs/connectors/getting-started).

## What Claude can read from Drive

With the connector turned on in a conversation, Claude can search your Drive, list your recent files, check a file's details and who it's shared with, and read a file's content. The table shows which file types Claude can read this way.

| File type                                              | Claude can read it |
| ------------------------------------------------------ | ------------------ |
| Google Docs                                            | Yes                |
| Google Sheets                                          | Yes                |
| Google Slides                                          | Yes                |
| PDF                                                    | Yes                |
| Word, Excel, and PowerPoint files                      | Yes                |
| OpenDocument text, spreadsheet, and presentation files | Yes                |
| PNG and JPEG images                                    | Yes                |

Two limits apply to every type:

* **Very large files**: the content Claude receives can be incomplete for a very large file
* **Comments and suggestions**: Claude can't read a file's comments or suggested edits, only its content

## Add Drive files to a chat or project

Besides letting Claude search on its own, you can pick specific Drive files yourself. A file you pick is attached to the conversation, or added to a [project](https://support.claude.com/en/articles/9517075-what-are-projects)'s knowledge so every chat in that project can use it. The picker lists your Google Docs, Sheets, and Slides.

<Tabs>
  <Tab title="In a chat">
    <Steps>
      <Step title="Open the add menu">
        In the conversation, select **+** at the lower left of the message box.
      </Step>

      <Step title="Choose Google Drive">
        Select **Add from Google Drive**.
      </Step>

      <Step title="Pick a file">
        Search for the file by name, or select it from the list.
      </Step>

      <Step title="Send your message">
        Write your question and send it. Claude reads the file's current content from Drive each time you send a message, so later edits in Drive reach Claude too.
      </Step>
    </Steps>
  </Tab>

  <Tab title="In a project">
    You can add Drive files only to a private project, one you haven't shared with other people. In a shared project, the **Google Drive** option is dimmed and shows **Only accessible from private projects**. To add a file to a private project's knowledge:

    <Steps>
      <Step title="Open the add menu">
        Open the project and, in its knowledge section, select **Add files**.
      </Step>

      <Step title="Choose Google Drive">
        Select **Google Drive**.
      </Step>

      <Step title="Pick a file">
        Search for the file, paste its Google Drive URL, or select it from the list.
      </Step>
    </Steps>

    The file appears in the project's knowledge and is available to Claude in every chat in that project. Its content refreshes from Drive periodically when you open the project.
  </Tab>
</Tabs>

Claude receives a text version of each file you add this way:

* **Google Docs**: converted to Markdown, without the images in the document
* **Google Sheets**: converted to CSV, with every tab included
* **Google Slides**: converted to plain text

Google caps exports of Docs, Sheets, and Slides at about 10 MB. For a file over that cap, Claude receives the file's name and details but not its content.

## Try the connector

In a conversation, select **+** at the lower left of the message box, select **Connectors**, and turn on **Google Drive**. Then ask a question that needs your files. For example, ask Claude:

* Find the design brief for the onboarding project in my Drive and summarize the open decisions
* Read the Q3 budget spreadsheet and tell me which lines are over plan
* What files have I worked on in the last week?

Claude can ask for your approval before it uses one of the connector's tools. Its answer draws on the files it read, and you can follow up in the same conversation to ask about another file or a detail in the same one.

## Reconnect or remove Google Drive

Everything about the connector after you've added it is on its own page. Go to [**Customize > Connectors**](https://claude.ai/customize/connectors) and select **Google Drive** under **Your connectors**. From that page you can:

* **Reconnect**: if Claude has lost access to your Google account, the connector's row shows **Reconnect**. Select it and sign in again
* **Disconnect**: select **Disconnect** to sign Claude out of Google. The connector stays in your list and shows **Connect**, so you can sign in again later
* **Remove**: open the three-dot menu and select **Remove** to take the connector off your account

If a reconnection error keeps coming back, select **Disconnect**, then **Connect**, and sign in to Google again.

## Next steps

* [Gmail](/docs/connectors/google/gmail): search and analyze your emails
* [Google Calendar](/docs/connectors/google/calendar): access your calendar information
* [Get started with connectors](/docs/connectors/getting-started#manage-or-disconnect-a-connector): set tool permissions and manage any connector
* [Connectors directory](/docs/connectors/directory): browse verified and community integrations
