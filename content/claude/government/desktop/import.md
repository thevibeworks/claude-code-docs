> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Import your data from Claude for Government Web

> Copy your conversations, projects, and files from Claude for Government Web into Claude Desktop, or move your Claude Desktop data to another computer.

> **Who this is for:** Anyone who used Claude for Government Web (the web app) and now uses Claude Desktop connected to Claude for Government, and anyone [moving Claude Desktop to another computer](#move-your-data-to-another-computer).

The import copies your conversations, their attached files, and the projects you created, with their instructions and the files you added to them.

## Before you begin

<video controls preload="metadata" playsInline src="https://mintcdn.com/claude-ai/nMLu5fzo3pFRNLuz/images/government/videos/user-01-signing-in-for-the-first-time-v3.mp4?fit=max&auto=format&n=nMLu5fzo3pFRNLuz&q=85&s=53f074a171b87f7c5f0f8ef71a6e7daa" aria-label="Video walkthrough: Signing in for the first time" />

Video: Signing in for the first time (1 min 26 s). Narrated with an AI-generated voice, with on-screen captions.

> [accordion] Transcript
>
> Claude Desktop is installed and connected for you by your agency. You sign in with your work account. No separate Claude account is needed.
>
> Open Claude. The sign-in screen says the app runs through your organization. Choose Sign in with your organization.
>
> Claude shows a pairing code, and opens your browser. The code works for a few minutes. If it expires, just start again.
>
> In the browser, enter your work email and select Continue. Then sign in the way you always do at your agency.
>
> Next comes the system use notification. Read it, and acknowledge it.
>
> Compare the code with the one in Claude, then select Approve. The page confirms you're signed in. Go back to Claude.
>
> You arrive on the home screen. Projects and your recent conversations are in the sidebar.
>
> You type your message in the message box. The model picker is at the bottom right. Your seat decides which models it lists, so a colleague may see others.
>
> Code is for software work, in a folder you choose on your computer.
>
> If you can sign in but the model picker is empty, ask your organization's owner to check your seat tier and its models.

* **Claude Desktop is up to date.** Update Claude Desktop to 4.29.0 or later and restart it, or ask your IT administrator to update it.
* **You had an account on the web app.** Its work email address must match the one on your account in Claude Desktop.

> **For administrators:** Anthropic enables the import for each organization. If a member's **Import & export** page says import is not enabled and their app is up to date, contact your Anthropic representative. The import needs Claude Desktop to download a component, so on a network that blocks `downloads.claude.ai`, deploy the offline installer described under [Installer and packaging](https://claude.com/docs/government/deploy-desktop/windows-checklist.md#installer-and-packaging) in the Windows fleet checklist.

## Run the import

<video controls preload="metadata" playsInline src="https://mintcdn.com/claude-ai/G8LW177rlshvdwBY/images/government/videos/user-02-bringing-your-chats-and-projects-over-v4.mp4?fit=max&auto=format&n=G8LW177rlshvdwBY&q=85&s=6e910cb7502932bbc23e9a0e43a5ae91" aria-label="Video walkthrough: Bringing your chats and projects over from Claude for Government Web" />

Video: Bringing your chats and projects over from Claude for Government Web (2 min 9 s). Narrated with an AI-generated voice, with on-screen captions.

> [accordion] Transcript
>
> If you used Claude for Government Web, you can copy your chats and projects into Claude Desktop. First, make sure Claude Desktop is up to date. You need an account on the web app, and it must use the same work email as your account in Claude Desktop.
>
> In Claude Desktop, open Settings from the account menu at the bottom of the sidebar, then Import and export, and select Import. Run it when you are ready.
>
> Select Sign in to Claude for Government Web, then Sign in. Claude shows a one-time code and opens a tab in your browser.
>
> In that tab, enter the code from Claude and approve the request. If you are asked to sign in, use your work account. Then go back to Claude.
>
> Check that the email shown is yours, then select Fetch export, and wait while Claude downloads your chats and projects.
>
> Select Continue, review what will be added, then select Import. When it finishes, the dialog reports what came over. Select Done.
>
> Your conversations appear in the sidebar, and your projects under Projects. Projects other people shared with you do not come over.
>
> Imported chats open in Chat. The first time you continue one, Claude asks whether to resume the imported session. Select Trust and resume to continue the conversation.
>
> A project that had instructions shows a notice. Claude won't follow imported instructions until you accept them: select Review instructions, check them, and save, or choose Use as is.
>
> The import only copies. You can run it again, and chats already imported are skipped. If the Import and export page says import isn't enabled, update Claude Desktop. If it still says so, ask your administrator.

You start the import yourself from **Settings**, whenever you are ready. If Claude Desktop's home screen shows a **Pick up where you left off in Claude for Government Web** banner, its **Start import** button takes you to the **Import & export** page in **Settings**. If you click **Skip for now** or close the banner, it can come back a few days later, until you run the import or have skipped it a few times. Claude Desktop versions earlier than 2.16120.0 hide the banner permanently after one skip.

**1. Open the import dialog**

In Claude Desktop, open **Settings**, then the **Import & export** page, and click **Import…**.

In organizations that also allow [export and import between computers](#move-your-data-to-another-computer), Claude Desktop 6.6395.0 or later opens the dialog on **Choose where to import from**. The web app import is the **From the web** row. The **From another computer** row is for a [zip file](#export-and-import-the-zip-file).

![Claude Desktop settings with Import and export selected and the Import from Claude dialog open on its Source step, headed Choose where to import from. A From the web row has a Sign in to Claude for Government Web button, and a From another computer row has a Choose file button.](https://mintcdn.com/claude-ai/ArGP1lHk5ekvCwKg/images/government/import/import-choose-source.png?fit=max\&auto=format\&n=ArGP1lHk5ekvCwKg\&q=85\&s=3f94c4a6321bf01c895cd27d0d8c32d9)

The first step of the import dialog, in an organization that has both the web app import and the zip file import.

**2. Sign in and enter the code**

Click **Sign in to Claude for Government Web…**, and in the dialog that opens, click **Sign in**. Claude Desktop shows a one-time code, which expires after a few minutes, and opens a tab in your default browser. In that tab, enter the code and approve the request. If you are asked to sign in, use your work account. Then return to Claude Desktop.

**3. Fetch your export**

Check that the email address shown is your work address, then click **Fetch export** and wait for the download to finish.

**4. Start the import**

Click **Continue**, review what will be added, then click **Import**. The import can take a few minutes.

**5. Check the results**

When the dialog reports what it brought over, click **Done**. Imported conversations appear in the sidebar, and imported projects appear under **Projects**.

## Continue an imported conversation

The first time you send a message in an imported conversation, Claude Desktop shows a **Resume imported session?** prompt. Click **Trust and resume** to continue.

## Review imported project instructions

If a project had instructions, open it after the import. Its page shows a notice that the instructions came from an import, and Claude doesn't follow them until you accept them. Click **Review instructions** to edit and save them, or **Use as is** to accept them unchanged. They then appear under **Instructions** on the project's page. Claude Desktop versions earlier than 1.25927.0 follow imported instructions straight away.

## Remove an import

To remove an import, open **Settings**, then the **Import & export** page. Under **Import history**, click **Remove** next to the import, or **Remove all** to remove every import listed. Before you confirm, the dialog shows how many conversations and projects it will delete. The files of imported projects stay on your computer, by default in `Claude/Projects` in your home folder, until you delete them yourself.

Removing a [zip file import](#move-your-data-to-another-computer) leaves its other data on your computer, such as memory and skills.

If you ran both the web app import and a zip file import, a conversation that's in both is deleted when you remove the older of the two imports, the lower one under **Import history**. To get it back, run the other import again. If the other import is the web app import, your web app projects then appear twice.

> [!WARNING]
>
> Removing an import also deletes any imported conversation you have continued since, including the new messages, and you cannot undo it.

## Move your data to another computer

You can export your Claude Desktop data to a zip file and import the file on another computer. Check these requirements first:

* **Your organization allows the move.** In Claude Desktop, **Settings > Import & export** shows an **Export…** button.
* **Both computers run Claude Desktop 6.6395.0 or later**, on the same operating system (macOS, Windows, or Linux).
* **You're signed in to the same tenant on both computers.** A [tenant](https://claude.com/docs/government/overview.md#tenant) is your agency's Claude for Government deployment.

If your organization doesn't allow the move, ask your IT administrator to [copy your data](https://claude.com/docs/third-party/claude-desktop/data-storage.md#copy-the-data-to-the-new-device) before you use Claude on the new computer, because the copy replaces any Claude Desktop data already there.

> **For administrators:** A tenant administrator or organization owner goes to **Settings > Config > Product availability** in the admin portal and turns on the [**Export and import between computers**](https://claude.com/docs/government/config/settings.md#export-and-import-between-computers) switch. Use it in place of the [`claudeAiImport` keys](https://claude.com/docs/third-party/claude-desktop/data-storage#turn-on-export-and-import) that other deployments set. Skills, scheduled tasks, plugins, and local MCP servers each need their own switch on as well: [**Let members create skills**](https://claude.com/docs/government/config/settings.md#let-members-create-skills), [**Scheduled tasks**](https://claude.com/docs/government/config/settings.md#scheduled-tasks), [**Let members add their own plugins**](https://claude.com/docs/government/config/settings.md#let-members-add-their-own-plugins), and [**Let members add their own connectors**](https://claude.com/docs/government/config/settings.md#let-members-add-their-own-connectors).

### Whose data the zip file holds

The zip file holds the Claude Desktop data of the Windows, macOS, or Linux account you're logged in to, and only what's stored on the computer you export from.

* **Shared computer accounts**: people who log in to a computer with the same account [share one history](https://claude.com/docs/government/security/security-and-data-handling.md#is-local-history-kept-separate-for-each-organization), so the zip file holds their data too
* **Your tenant**: the zip file carries your tenant's ID as a label, and the import checks that it matches the tenant you're signed in to

### What the zip file includes

> [!WARNING]
>
> The zip file isn't encrypted. Anyone who has it can read it, including any passwords or keys written in your data, such as in a chat, a file, or a local MCP server's arguments.

| Data | What goes in the zip file | Your step on the new computer |
| - | - | - |
| Chats and Cowork tasks | The ones in the date range you select, archived tasks included, with their attached files, output files, and what Claude read from files and connectors | [Trust each one](#continue-an-imported-conversation) the first time you continue it |
| Code sessions | The history of the ones in the date range, archived ones included, without their folders | [Copy and trust each folder](https://claude.com/docs/third-party/claude-desktop/import.md#import-your-data-on-the-new-device) before you import |
| Projects | Your projects, their instructions, and the files in each project's own folder, by default under `Claude/Projects` in your home folder | [Accept the instructions](#review-imported-project-instructions). To use the files in Chat, [add the folder again and start a new chat](https://claude.com/docs/third-party/claude-desktop/import.md#make-an-imported-project-folder-readable-in-chat). |
| Memory and preferences | Your memory and some app preferences | None |
| Skills, plugins, and scheduled tasks | Skills you saved, plugins you uploaded, and your scheduled tasks | [Turn on the ones you want](https://claude.com/docs/third-party/claude-desktop/import.md#turn-on-imported-plugins-skills-and-scheduled-tasks). Each kind imports only if your organization allows it. |
| Local MCP servers | The commands and arguments of servers you added under **Settings > Developer**, if your organization allows them | Click **Add** only if you recognize every command, because the servers start right away. Then [enter their environment variable values again](https://claude.com/docs/third-party/claude-desktop/import.md#set-up-imported-local-mcp-servers). |

### What the zip file leaves out

The zip file leaves out data such as:

* **Access**: sign-ins and their tokens, connectors, and tool permissions such as **Always allow**
* **Project details**: a project's description, links, and hidden files such as `.env`
* **Other folders**: folders you added to a project or task, apart from their paths
* **Artifacts**: the artifacts that Claude made, apart from the output files that Claude built them from ([export a design or deck](https://claude.com/docs/government/desktop/design-and-slides.md#export-a-design-or-deck) first to keep it)

For size limits and more detail, see [What a Claude Desktop export moves](https://claude.com/docs/third-party/claude-desktop/import.md#what-a-claude-desktop-export-moves).

### Export and import the zip file

The import adds to the data on the new computer and replaces nothing. A skill, plugin, local MCP server, or memory note that already has the same name there stays as it is.

1. On the old computer, follow [Export your data from the old device](https://claude.com/docs/third-party/claude-desktop/import.md#export-your-data-from-the-old-device).
2. On the new computer, follow [Import your data on the new device](https://claude.com/docs/third-party/claude-desktop/import.md#import-your-data-on-the-new-device). In organizations that also have the [web app import](#run-the-import), the import dialog opens on [**Choose where to import from**](#choose-where-to-import-from). Click **Choose file…** in the **From another computer** row.
3. When Claude Desktop asks whether the file is your own export, click **Import as my own**. **Import sessions only** is for a file that someone else made. Come back to this page if a dialog asks about projects.
4. If the [web app import](#run-the-import) already brought some of the zip file's projects to this computer, another dialog lists them after you click **Import as my own**. Click **Merge into existing** to have each project once. Your answer covers every project listed. Where a file or the instructions differ, the zip file's version goes in a `From the imported file` folder inside the project's folder.
5. If a project that you created yourself on this computer has the same name as one in the zip file, the [**Duplicates** step](https://claude.com/docs/third-party/claude-desktop/import.md#if-a-project-already-exists) lists it after the import finishes. Click **Keep separate** to keep the imported project whole. In this step, **Merge into existing** moves the imported project's chats and memory into yours. It leaves the files in a folder outside your project, and drops the instructions if your project has its own.

You can run the web app import on the new computer as well. If you clicked **Import as my own**, a conversation that's in both imports appears once. If you continued it on the old computer, it can appear twice: once as it was in the web app, and once with your later messages.

## Troubleshooting

| What you see | Likely cause | What to do |
| - | - | - |
| Your export exceeds the import size limit | You have more data than the import can bring over | Update Claude Desktop to 4.29.0 or later, then run the import again. If you still see this message, contact your administrator, who can ask Anthropic for help |
| The account does not match your organization | You signed in with a different account or organization | Click **Sign in** in the dialog again and use your work account in the browser tab |
| **Settings** has no **Import & export** page, or the page says import isn't enabled for this deployment | Your app is out of date, or Anthropic has not yet enabled the import for your organization | Update Claude Desktop to the latest version. If the page still says import isn't enabled, contact your administrator, who can ask Anthropic to enable it |
| The import dialog has no **Sign in to Claude for Government Web…** button | Anthropic hasn't enabled the web app import for your organization | Contact your administrator, who can ask Anthropic to enable it |
| The **Import & export** page has no **Export…** button | Your app is out of date, or your organization hasn't turned on export and import | Update Claude Desktop to the latest version. If the button is still missing, ask your administrator to turn on **Export and import between computers** |
| That export was made in another organization | The zip file wasn't exported in the tenant you're signed in to | Choose a zip file that was exported in your tenant |
| Not allowed by your organization | Your organization doesn't allow that kind of data | If you need that data, ask your administrator to allow it. Then restart Claude Desktop, import the same zip file again, and click **Import as my own** |
| Your local MCP servers are missing, and the import's last screen doesn't mention them | Your organization didn't allow them when you exported | After your administrator allows them, restart Claude Desktop on both computers, export again, and import the new zip file |
| Cowork tasks from the zip file are missing from the sidebar | You archived them on the old computer, so they arrive archived | Where your Cowork tasks are listed, hover over **Recents** in the sidebar and click the filter icon, **Filter and group recents**. Then select **Status > Archived** |
| Code sessions from the zip file are missing from the sidebar | You archived them on the old computer, so they arrive archived | In the **Code** tab, hover over the heading above the session list and click the **Group and sort** icon. Then click **View all**, then **Archived** |
| An artifact in a chat or task from the zip file opens an empty side panel | The zip file [leaves artifacts out](#what-the-zip-file-leaves-out) | In that chat or task, ask Claude to make the artifact again |
| Your sessions arrived from the zip file, but other data such as memory, skills, and project files didn't | You chose **Import sessions only** when Claude Desktop asked whether the file is your own export | If you still have the zip file, [remove the import](#remove-an-import) named **Claude Desktop export**, which also deletes anything that you added to the imported sessions since. Then [import the same zip file again](#export-and-import-the-zip-file) and click **Import as my own**. If you don't remove the import first, the other data still arrives, but conversations or projects from the web app import can appear twice |

For other problems with a zip file, see [Problems when you move to another device](https://claude.com/docs/third-party/claude-desktop/import.md#problems-when-you-move-to-another-device). For anything else, try the import again. If it keeps failing, contact your administrator.

## Things to know

* **You can run the web app import again, on this computer or another.** Conversations already there are skipped. For conversations that came in a zip file, see [Export and import the zip file](#export-and-import-the-zip-file). The import brings only what was in the web app, not your work since then in Claude Desktop.
* **Conversations can arrive as Cowork tasks.** If your organization's [settings](https://claude.com/docs/government/config/settings.md#product-availability) don't give you Chat when you run the import, your conversations are imported as Cowork tasks instead. If Cowork is also off, they don't appear in the sidebar, so ask your administrator for [Cowork](https://claude.com/docs/government/config/settings.md#cowork-in-claude-desktop). Claude Desktop versions earlier than 1.28929.0 always import them as Cowork tasks.
* **You can't import projects other people shared with you.** You also can't import anything from claude.ai or other AI assistants.
* **In Chat, Claude can't read a folder that the import put on a project until you add the folder to the project again.** For the steps, see [Make an imported project folder readable in Chat](https://claude.com/docs/third-party/claude-desktop/import.md#make-an-imported-project-folder-readable-in-chat).
