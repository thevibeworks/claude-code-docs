> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Import your data from Claude for Government Web

> Copy your conversations, projects, and files from Claude for Government Web into Claude Desktop.

> **Who this is for:** Anyone who used Claude for Government Web (the web app) and now uses Claude Desktop connected to Claude for Government.

The import copies your conversations, their attached files, and the projects you created, including each project's files and instructions. It does not copy projects that other people shared with you.

## Before you begin

* **You have an account on the web app.** It must use the same work email address as your account in Claude Desktop.
* **You are signed in to the web app in your default browser.** The import opens a browser tab there and asks for a one-time code, which expires after a few minutes.

> **For administrators:** Anthropic enables the import for each organization, so there is no [product setting](/docs/government/config/settings) for it. If a member's **Import & export** page says import is not enabled and their app is up to date, contact your Anthropic representative. The import needs Claude Desktop to download a component, so on a network that blocks `downloads.claude.ai`, deploy the offline installer described under [Installer and packaging](/docs/government/deploy-desktop/windows-checklist#installer-and-packaging) in the Windows fleet checklist.

## Run the import

<Steps>
  <Step title="Open the import dialog">
    In Claude Desktop, open **Settings**, then the **Import & export** page, and click **Import…**.
  </Step>

  <Step title="Sign in and enter the code">
    Click **Sign in to Claude for Government Web…**, and in the dialog that opens, click **Sign in**. Claude Desktop shows a one-time code and opens the web app in your default browser. Sign in there with your work account if you are asked to, enter the code, and approve the request. Then return to Claude Desktop.
  </Step>

  <Step title="Fetch your export">
    Check that the email address shown is your work address, then click **Fetch export** and wait for the download to finish.
  </Step>

  <Step title="Start the import">
    Click **Continue**, review what will be added, then click **Import**. The import can take a few minutes.
  </Step>

  <Step title="Check the results">
    When the dialog reports what it brought over, click **Done**. Imported conversations appear in the sidebar, and imported projects appear under **Projects** with their files.
  </Step>
</Steps>

## Continue an imported conversation

Imported conversations open in Chat. The first time you send a message in one, Claude Desktop shows a **Resume imported session?** prompt. Click **Trust and resume** to continue.

## Review imported project instructions

If a project had instructions in the web app, open it after the import. Its page shows a notice that the instructions came from an import, and Claude does not follow them until you accept them. Click **Review instructions** to edit and save them, or **Use as is** to accept them unchanged. They then appear under **Instructions** on the project's page.

## Remove an import

To delete what an import added, open **Settings**, then the **Import & export** page. Under **Import history**, click **Remove** next to the import, or **Remove all** to remove every import listed. Before you confirm, the dialog shows how many conversations and projects it will delete.

<Warning>
  Removing an import also deletes any imported conversation you have continued since, including the new messages, and you cannot undo it.
</Warning>

## Troubleshooting

| What you see                                 | Likely cause                                                          | What to do                                                                                                                                  |
| -------------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Your export exceeds the import size limit    | You have more data than the import can bring over                     | Remove conversations or files you no longer need in the web app, in line with your organization's records policy, then run the import again |
| The account does not match your organization | You signed in to the web app with a different account or organization | In the browser, sign in to the web app with your work account, then click **Sign in** in the dialog again                                   |

For anything else, try the import again; if it keeps failing, contact your administrator.

## Things to know

* **You can run the import again.** Conversations you already imported are skipped.
* **Conversations can arrive as Cowork tasks.** If **Chat in Claude Desktop** is turned off for your organization under [Product availability](/docs/government/config/settings#product-availability) when you run the import, your conversations are imported as Cowork tasks instead and open only on computers where Cowork is available.
* **Projects other people shared with you are not imported.** Only the projects you created come over, with their files and instructions.
