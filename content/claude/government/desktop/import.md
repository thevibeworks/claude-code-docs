> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Import your data from Claude for Government Web

> Copy your conversations, projects, and files from Claude for Government Web into Claude Desktop.

> **Who this is for:** Anyone who used Claude for Government Web (the web app) and now uses Claude Desktop connected to Claude for Government.

The import copies your conversations, their attached files, and the projects you created, including each project's files and instructions. It does not copy projects that other people shared with you.

## Before you begin

<Frame caption="Video: Signing in for the first time (1 min 32 s). Narrated with an AI-generated voice, with on-screen captions.">
  <video controls preload="metadata" playsInline className="w-full aspect-video" src="https://mintcdn.com/claude-ai/gGFKuNSbKYs4JMmK/images/government/videos/user-01-signing-in-for-the-first-time.mp4?fit=max&auto=format&n=gGFKuNSbKYs4JMmK&q=85&s=fcfdbcaa5f3ee9e9496e6014ed516b65" aria-label="Video walkthrough: Signing in for the first time" data-path="images/government/videos/user-01-signing-in-for-the-first-time.mp4" />
</Frame>

<Accordion title="Transcript">
  Claude Desktop is installed and connected for you by your agency. You sign in with your work account. No separate Claude account is needed.

  Open Claude. The sign-in screen says the app runs through your organization. Choose Sign in with your organization.

  Claude shows a pairing code, and opens your browser. The code works for a few minutes. If it expires, just start again.

  In the browser, enter your work email and select Continue. Then sign in the way you always do at your agency.

  Next comes the system use notification. Read it, and acknowledge it.

  Compare the code with the one in Claude, then select Approve. The page confirms you're signed in. Go back to Claude.

  You arrive on Home. Home and Code sit at the top of the sidebar, above your projects and recent chats.

  If your organization offers both Chat and Cowork, you pick one in the message box. The model picker is at the bottom right. Your seat decides which models it lists, so a colleague may see others.

  Code is for software work, in a folder you choose on your computer.

  If you can sign in but the model picker is empty, you have no seat yet. Ask your organization's owner to assign you one.
</Accordion>

* **You have an account on the web app.** It must use the same work email address as your account in Claude Desktop.
* **You are signed in to the web app in your default browser.** The import opens a browser tab there and asks for a one-time code, which expires after a few minutes.

> **For administrators:** Anthropic enables the import for each organization. If a member's **Import & export** page says import is not enabled and their app is up to date, contact your Anthropic representative. The import needs Claude Desktop to download a component, so on a network that blocks `downloads.claude.ai`, deploy the offline installer described under [Installer and packaging](/docs/government/deploy-desktop/windows-checklist#installer-and-packaging) in the Windows fleet checklist. To remind members to run the import, turn on the [**Show the Claude for Government Web import banner**](/docs/government/config/settings#show-the-claude-for-government-web-import-banner) switch on the **Config** page.

## Run the import

<Frame caption="Video: Bringing your chats and projects over from Claude for Government Web (2 min 10 s). Narrated with an AI-generated voice, with on-screen captions.">
  <video controls preload="metadata" playsInline className="w-full aspect-video" src="https://mintcdn.com/claude-ai/gGFKuNSbKYs4JMmK/images/government/videos/user-02-bringing-your-chats-and-projects-over.mp4?fit=max&auto=format&n=gGFKuNSbKYs4JMmK&q=85&s=b7860d7dd7807b95aecc486b1aaf26f7" aria-label="Video walkthrough: Bringing your chats and projects over from Claude for Government Web" data-path="images/government/videos/user-02-bringing-your-chats-and-projects-over.mp4" />
</Frame>

<Accordion title="Transcript">
  If you used Claude for Government - Web, you can copy your chats and projects into Claude Desktop. First, sign in to the web app in your browser with the same work email you use in Claude Desktop.

  In Claude Desktop, open Settings from the account menu at the bottom of the sidebar, then Import and export, and select Import. The app does not prompt you to do this. Run it when you are ready.

  Select Sign in to Claude for Government Web, then Sign in. Claude shows a one-time code and opens the web app in your browser.

  In the browser tab that opens, sign in if you are asked, enter the code from Claude, and approve the connection. Then go back to Claude.

  Check that the email shown is yours, then select Fetch export. The web app gathers your chats and projects, and Claude downloads them.

  Select Continue, review what will be added, then select Import. When it finishes, the dialog reports what came over. Select Done.

  Your conversations appear in the sidebar with their files, and your projects under Projects with their files and instructions. Projects other people shared with you do not come over.

  Imported chats open in Chat. The first time you continue one, Claude asks whether to resume the imported session. Select Trust and resume to continue the conversation.

  A project that had instructions shows a notice. Claude won't follow imported instructions until you accept them: select Review instructions, check them, and save, or choose Use as is.

  The import only copies. Your chats and projects stay in the web app too. You can run it again, and chats already imported are skipped. If the Import page says import isn't enabled, ask your administrator.
</Accordion>

You start the import yourself from **Settings**, whenever you are ready. If Claude Desktop's home screen shows a **Pick up where you left off in Claude for Government Web** banner, its **Start import** button takes you to the **Import & export** page in **Settings**. If you click **Skip for now** or close the banner, it can come back a few days later, until you run the import or have skipped it a few times. Claude Desktop versions earlier than 2.16120.0 hide the banner permanently after one skip.

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

| What you see | Likely cause | What to do |
| - | - | - |
| Your export exceeds the import size limit | You have more data than the import can bring over | Remove conversations or files you no longer need in the web app, in line with your organization's records policy, then run the import again |
| The account does not match your organization | You signed in to the web app with a different account or organization | In the browser, sign in to the web app with your work account, then click **Sign in** in the dialog again |
| The **Import & export** page says import isn't enabled for this deployment | Your app is out of date, or Anthropic has not yet enabled the import for your organization | Update Claude Desktop to the latest version. If the page still says import isn't enabled, contact your administrator, who can ask Anthropic to enable it |

For anything else, try the import again; if it keeps failing, contact your administrator.

## Things to know

* **You can run the import again.** Conversations you already imported are skipped.
* **Conversations can arrive as Cowork tasks.** If **Chat in Claude Desktop** is turned off for your organization under [Product availability](/docs/government/config/settings#product-availability) when you run the import, your conversations are imported as Cowork tasks instead and open only on computers where Cowork is available.
* **Projects other people shared with you are not imported.** Only the projects you created come over, with their files and instructions.
