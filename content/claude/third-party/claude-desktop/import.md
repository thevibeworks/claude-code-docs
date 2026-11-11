> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Import history from claude.ai

> Bring conversations, projects, and local Cowork and Code sessions into Claude Desktop on 3P from a claude.ai workspace, an earlier install, or another device

Import brings a copy of your claude.ai conversations and projects into Claude Desktop on third-party (3P), along with any Cowork and Claude Code sessions already on this machine from an earlier install. Everything lands in the local session store described in [User identity and local data](https://claude.com/docs/third-party/claude-desktop/data-storage.md), so you can pick up work you started on claude.ai and continue it against your organization's own inference provider.

Each import is a one-time copy. New activity on claude.ai after you import does not appear in Claude Desktop unless you import again, and importing from claude.ai again does not create duplicates.

To take your Claude Desktop data to a new device, see [Move your data to another device](#move-your-data-to-another-device).

## Automatic import of earlier third-party sessions

Claude Desktop can automatically copy into your history the Cowork, Chat, and Code sessions it stored on this computer under an earlier third-party configuration. In an organization managed from the [Enterprise Admin Console](https://claude.com/docs/third-party/claude-desktop/admin-console.md), this automatic copy is on unless it's turned off in your organization's settings. In any other deployment it runs only if your administrator turns it on.

Along with the sessions, the automatic copy brings over other things you had under the earlier configuration. Claude Desktop 5.1231.0 or later brings these items, and [earlier versions bring less](#if-the-automatic-copy-ran-on-an-earlier-version):

* **Projects**: your Cowork projects, with their descriptions, folders, and sidebar pins. New tasks use a project's instructions only after you accept them. A project's links aren't copied. Add them again.
* **Memory and instructions**: your Cowork memory, unless you paused it, and your global instructions. New tasks use them right away. Your **Instructions for Claude** (**Settings → General**) come over too. Instructions you already set under the new configuration are kept.
* **Scheduled tasks**: your scheduled tasks from Cowork and Code. Each stays on or off as it was. A task arrives with **Default model**, and a Cowork task arrives on **Manually approve**. Set the model again, and set the approval mode again where the app offers **Automatically approve**. Until you do, a run waits for you each time it needs an approval. A task starts with no runs, and its earlier runs are listed as ordinary sessions.
* **Uploaded plugins**: plugins you uploaded, unless your administrator has turned off plugin uploads ([`userPluginUploadsEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#userpluginuploadsenabled)). Each stays on or off as it was.
* **Saved skills**: skills you saved, unless your administrator has turned off skill creation ([`skillCreationEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#skillcreationenabled)).
* **Your organization's optional plugins**: the ones you had turned on are turned on again, if they come from your organization's plugins directory or from a marketplace hosted at the address of its gateway or bootstrap server. With Claude Desktop 2.42304.0 or later, plugins from other marketplaces, such as a git repository, are turned on again too, if your administrator offers the marketplace from the same repository or URL as before. On a computer where the copy already ran, they're turned on the first time the app starts on 2.42304.0 or later.
* **Artifacts**: your Cowork artifacts, with their earlier versions.

The copy runs once on each computer, in the background shortly after the app starts, and the sessions then appear in the sidebar. Your original sessions stay where they were, and sessions you already imported are skipped. The copy is listed under **Import history** in **Settings → Import & export**, where the **Remove** button deletes the copied sessions and the projects copied with them. The app doesn't copy them again later.

Copied sessions go back into custom groups of the same name in the sidebar, and Cowork sessions keep their connected folders. Sessions and scheduled tasks arrive unpinned. The copy doesn't bring connector sign-ins, files you attached to sessions, or **Always allow** choices. It also doesn't bring app preferences such as the model, per-tool permissions, and notifications. Set them up again as you need them.

Use the [import wizard](#open-the-import-wizard) for your claude.ai conversations and projects, and for any local sessions the automatic copy left out.

### If the automatic copy ran on an earlier version

If the copy ran on a Claude Desktop version before 5.1231.0, set up these items yourself:

* **Project descriptions**: enter them again on each project's page
* **Folders connected to Cowork sessions**: connect them again
* **Project folders outside the default location**: [add the original folder again](#add-the-original-folder-to-a-copied-project)

The first time the app starts on 5.1231.0 or later, it brings these items:

* **Sidebar pins of your projects and custom groups of your sessions**
* **Earlier versions of your artifacts**, if the automatic copy is still on
* **Your projects, scheduled tasks, and instructions**, if you had no earlier sessions and the automatic copy is still on. Before 5.1231.0, the app copies nothing for someone with no sessions. Projects and scheduled tasks that you made again under the new configuration appear twice. Delete the ones you don't need.

### Add the original folder to a copied project

If a copied project's folder shows **Empty folder** when you expand it under **Context** on the project's page, the copy didn't keep the original folder. The original folder and its files stay where they were. Add the original folder once for each of these projects.

Before Claude Desktop 5.1231.0, this happens to every project whose folder isn't directly inside the **Projects** folder of your Cowork files folder. Your Cowork files folder is `~/Claude` by default. To check, go to **Settings > Cowork** and read the path under **Cowork files**.

**1. Open the project**

Go to the **Projects** page and open the copied project.

**2. Add the original folder**

Next to **Context**, click **+**, select **Choose a folder**, then select **Choose a different folder** in the submenu. In the folder dialog, select the project's original folder.

**3. Remove the empty folder**

**Context** now lists both folders, which can have the same name. Click each folder to expand it. Click the **x** on the row of the one that shows **Empty folder**.

New tasks in the project now work in the original folder. Sessions that were copied with the project still use the empty folder. Start a new task to work with your files.

## Before you open the import wizard

* Your administrator has turned import on by setting [`claudeAiImport`](https://claude.com/docs/third-party/claude-desktop/configuration#claudeaiimport) with `enabled` set to `true` in the managed configuration. The import wizard is off by default; until then, **Settings → Import & export** has no **Import…** button and reports that import isn't enabled for this deployment. The [automatic import of earlier third-party sessions](#automatic-import-of-earlier-third-party-sessions) doesn't depend on this setting.
* If your administrator lists the claude.ai organizations you may import from, with `allowedOrganizationUuids` under [`claudeAiImport`](https://claude.com/docs/third-party/claude-desktop/configuration#claudeaiimport), you can import only by signing in to claude.ai, and only from a listed organization. A sign-in to any other organization or to a personal account is refused, and the wizard's options to import from a file or from earlier sessions on this computer are turned off. The [automatic import of earlier third-party sessions](#automatic-import-of-earlier-third-party-sessions) isn't affected by this list.
* Claude Desktop is installed and running in third-party mode. See [Installation and setup](https://claude.com/docs/third-party/claude-desktop/installation.md).
* To bring history over from a claude.ai Team or Enterprise workspace, an owner of that workspace has [enabled member data export](#enable-member-data-export-admins), which isn't possible in a HIPAA-ready organization. Personal claude.ai accounts can always export.

## Enable member data export (admins)

On Team and Enterprise workspaces, member data export is off by default.

> [!NOTE]
>
> In a [HIPAA-ready organization](https://support.claude.com/en/articles/13296973-hipaa-ready-enterprise-plans), member data export can't be turned on. Both ways to import claude.ai chats and projects in [step 1 of the import wizard](#step-1-claude-ai-chats-and-projects) need member data export, so neither works for members of that organization. If [`allowedOrganizationUuids`](https://claude.com/docs/third-party/claude-desktop/configuration#claudeaiimport) isn't set, they can still import Cowork and Claude Code sessions already on their computer in [step 2](#step-2-local-cowork-and-code-sessions).

To enable member data export, a workspace owner goes to [**Organization settings > Data and privacy**](https://claude.ai/admin-settings/data-privacy-controls) on claude.ai and turns on the **Allow members to export their own data** toggle.

![claude.ai organization settings, Data and privacy page, with the Allow members to export their own data toggle turned on and a confirmation toast reading Member data export enabled.](https://mintcdn.com/claude-ai/HpR2FaaZXZXkiUcV/images/third-party/import/import-admin-toggle.png?fit=max\&auto=format\&n=HpR2FaaZXZXkiUcV\&q=85\&s=f1f4696a2124cd36ee9a7366cb1c4772)

The member data export toggle in claude.ai organization settings. Only workspace owners see this control.

Members of the workspace can then export their own conversations. The toggle does not expose one member's data to another; each member can download only their own history.

## Open the import wizard

In Claude Desktop, go to **Settings → Import & export** and click **Import…** to open the **Import from Claude** wizard.

![Claude Desktop settings with Import and export selected and the Import from Claude wizard open on step 1, showing Sign in to claude.ai and Choose file buttons.](https://mintcdn.com/claude-ai/HpR2FaaZXZXkiUcV/images/third-party/import/import-wizard-start.png?fit=max\&auto=format\&n=HpR2FaaZXZXkiUcV\&q=85\&s=526562f1c9c0abd66e9b56d0328808db)

Step 1 of the import wizard, before a source is chosen.

The wizard has three steps: **Chats** (your claude.ai export), **Cowork & Code** (local sessions on this machine), and **Review**. Skip any step you don't need. A fourth step, **Duplicates**, appears after the import only when an imported project has the same name as one you already have. See [If a project already exists](#if-a-project-already-exists).

## Step 1: claude.ai chats and projects

You can pull your claude.ai history straight into the wizard by signing in, or download it from claude.ai yourself and choose the file.

> [tab] Sign in to claude.ai (recommended)
>
> Click **Sign in to claude.ai…**. Your browser opens to claude.ai; sign in if prompted, choose your organization if you belong to more than one, and click **Authorize**.
>
> ![claude.ai organization selector titled Select organization, listing one organization.](https://mintcdn.com/claude-ai/HpR2FaaZXZXkiUcV/images/third-party/import/import-consent-org.png?fit=max\&auto=format\&n=HpR2FaaZXZXkiUcV\&q=85\&s=1657a03028a7ceb3d173e71ba27f591d)
>
> The organization selector, shown if your claude.ai account belongs to more than one workspace.
>
> ![claude.ai authorization card reading Claude Desktop Import would like to connect to your Claude chat account, with an Authorize button.](https://mintcdn.com/claude-ai/HpR2FaaZXZXkiUcV/images/third-party/import/import-consent-authorize.png?fit=max\&auto=format\&n=HpR2FaaZXZXkiUcV\&q=85\&s=55be3501d41c9e61b49154db66b71d5b)
>
> The authorization prompt. The only permission granted is a one-time export of your own data.
>
> Back in Claude Desktop, click **Fetch export**. The wizard requests an export from claude.ai, downloads it, and shows what it found.
>
> ![Import from Claude wizard step 1 showing a claude.ai export row with the account email and a summary of 7 chats and 1 project.](https://mintcdn.com/claude-ai/HpR2FaaZXZXkiUcV/images/third-party/import/import-signed-in.png?fit=max\&auto=format\&n=HpR2FaaZXZXkiUcV\&q=85\&s=dafc4cbfffd685321442cbd72fd73993)
>
> The wizard after the export finishes downloading.

> [tab] Choose a downloaded file
>
> On claude.ai, go to **Settings → Privacy → Export data** and click **Export**. If you don't see **Export data**, ask a workspace owner to [enable member data export](#enable-member-data-export-admins).
>
> ![claude.ai settings Privacy page with the Export data subpage open, showing an Export button and a note that a download link will be sent by email.](https://mintcdn.com/claude-ai/HpR2FaaZXZXkiUcV/images/third-party/import/import-web-export.png?fit=max\&auto=format\&n=HpR2FaaZXZXkiUcV\&q=85\&s=1ed4aa5a08469420020d3ff83579c0de)
>
> The Export data page in claude.ai personal settings.
>
> claude.ai emails you a download link when the export is ready. The link expires after 24 hours.
>
> ![Email from Claude titled Your data is ready for download with a Download data button.](https://mintcdn.com/claude-ai/HpR2FaaZXZXkiUcV/images/third-party/import/import-email.png?fit=max\&auto=format\&n=HpR2FaaZXZXkiUcV\&q=85\&s=cf883e9c401401686568c77cb6ac45c1)
>
> The export-ready email.
>
> Download the `.zip`, then in the import wizard click **Choose file…** and select it.
>
> ![Import from Claude wizard step 1 showing a selected member-data zip file with a summary of 7 chats and 1 project.](https://mintcdn.com/claude-ai/HpR2FaaZXZXkiUcV/images/third-party/import/import-choose-file.png?fit=max\&auto=format\&n=HpR2FaaZXZXkiUcV\&q=85\&s=5cb868969ebed88801296f696796d0f1)
>
> Step 1 with a downloaded export selected.

Click **Continue**, or **Skip this step** if you only want to bring in local sessions.

## Step 2: local Cowork and Code sessions

The wizard scans this machine for Cowork and Claude Code sessions from an earlier Claude Desktop install and lists what it finds. Choose how far back to include, and add any other folder that holds sessions (for example, a backup or a folder copied from another machine). On Windows, the folder has to be on a local disk. The wizard can't import one from a network share or a mapped network drive, so copy it to the computer first.

![Import from Claude wizard step 2, Cowork and Code, listing 5 local sessions with a time-range selector and an option to add another location.](https://mintcdn.com/claude-ai/RVrsc-fMoqOV1t9C/images/third-party/import/import-local-sessions.png?fit=max\&auto=format\&n=RVrsc-fMoqOV1t9C\&q=85\&s=24f96c7b665e4a82fa8f552c20c60312)

Local sessions found on this machine.

Sessions are copied, not moved. Your original history stays where it is.

If you add the same folder again, the wizard skips the sessions it marks as already imported and copies the rest. A session that changed after you imported it is copied again as a separate session, and a project can arrive a second time with a number after its name, such as **Northwind (1)**. On Claude Desktop versions before 3.1623.0, the wizard copies every session again. To undo an import, go to **Settings → Import & export** and click **Remove** next to it under **Import history**.

## Step 3: review and import

The **Review** step summarizes what will be added. Click **Import** to copy everything into your local session store.

![Import from Claude wizard step 3 showing a claude.ai export summary of 7 chats and 1 project alongside 5 local Cowork and Code sessions, with an Import button.](https://mintcdn.com/claude-ai/HpR2FaaZXZXkiUcV/images/third-party/import/import-review.png?fit=max\&auto=format\&n=HpR2FaaZXZXkiUcV\&q=85\&s=c7939485c7185afbf1ef7518a94db2d6)

The review summary before import.

![Import from Claude wizard success screen showing a checkmark and the number of sessions imported.](https://mintcdn.com/claude-ai/RVrsc-fMoqOV1t9C/images/third-party/import/import-success.png?fit=max\&auto=format\&n=RVrsc-fMoqOV1t9C\&q=85\&s=4c7be49e3961f082808af10edc50eb56)

Import complete. Imported chats appear in the sidebar and imported projects appear on the Projects page.

## If a project already exists

When an imported project has the same name as a project already in Claude Desktop, the wizard adds a **Duplicates** step after the import finishes. This happens, for example, when you set up **Northwind** on this machine and then bring over history from another machine that also has a Northwind project. The step lists each match with two choices.

![Import from Claude wizard step 4, Duplicates, headed These projects already exist, listing five Northwind projects each with Merge into existing and Keep separate buttons and a Continue button.](https://mintcdn.com/claude-ai/XDpDaIQ3J0Amhn8h/images/third-party/import/import-duplicates.png?fit=max\&auto=format\&n=XDpDaIQ3J0Amhn8h\&q=85\&s=798f75d5a508ebcb7082373b5cf95d84)

The Duplicates step, listing imported projects that match ones you already have.

* **Merge into existing** moves the imported chats and sessions into your existing project and removes the duplicate. Folders you attached to the duplicate move with them. If your existing project has no instructions of its own, the imported project's instructions are shown there for you to review and accept. Later imports from the same source go into the existing project as well, except from a folder you added, where the wizard asks again. For a [Claude Desktop export](#move-your-data-to-another-device), the wizard also asks again unless you click **Import as my own** each time.
* **Keep separate** leaves both projects in place. The imported one keeps a numbered name, such as **Northwind (1)**, and Claude Desktop stops offering to merge it.

The **Projects** page offers the same two choices, in a row under the duplicate project's card and at the top of the duplicate project's own page. Decide there if your history was brought over automatically when you signed in, so you never saw the wizard, or if you closed the wizard before choosing.

## Continue an imported conversation

Open any imported conversation from the sidebar and keep chatting. The first time you send a message in an imported session, Claude Desktop asks you to confirm before it continues. The reply then comes from your configured inference provider, not from claude.ai.

* A session from this app's earlier third-party configuration on this computer shows a **Continue this conversation?** prompt. Click **Continue** to send your message.
* Any other imported conversation or session shows a **Resume imported session?** prompt. Click **Trust and resume** to continue.

![An imported conversation open in Cowork with a yellow Resume imported session card offering Go back and Trust and resume buttons.](https://mintcdn.com/claude-ai/HpR2FaaZXZXkiUcV/images/third-party/import/import-trust-resume.png?fit=max\&auto=format\&n=HpR2FaaZXZXkiUcV\&q=85\&s=806d0d2018d7fc0f10afb71035b1f807)

The trust prompt shown the first time you resume a conversation imported from claude.ai.

## Make an imported project folder readable in Chat

When an import brings over a project, it puts a folder on the project. In Chat, Claude can't read that folder until you add it to the project again. Add the folder once for each imported project.

**1. Open the project**

Go to the **Projects** page and open the imported project.

**2. Note the folder path**

Next to **Context**, click **+**, then select **Choose a folder**. Under **Recent**, find the project's folder, which is dimmed and can't be selected, and note the path shown under its name.

**3. Add the folder again**

Select **Choose a different folder**. In the folder dialog, go to the path you noted and select the project's folder.

**4. Start a new conversation**

Start a new conversation in the project. In the new conversation, Claude can read the files in the folder.

Importing the project again doesn't make its folder readable. If you remove the import under **Import history** in **Settings > Import & export**, or archive the project, and then import from claude.ai again, the new project uses the same folder. Add the folder to the new project again.

Your administrator can also limit which folders Claude reads. See [Project folders in Chat](https://claude.com/docs/third-party/claude-desktop/chat.md#project-folders-in-chat).

## Move your data to another device

There are two ways to take your work to a new device. Your administrator [copies your data](https://claude.com/docs/third-party/claude-desktop/data-storage.md#move-a-user-to-a-new-device), or you export it to a zip file and import the file on the new device. Ask your administrator which way your organization uses. For an export, they must first [turn on export and import](https://claude.com/docs/third-party/claude-desktop/data-storage.md#turn-on-export-and-import). Your data stays on the old device, so keep that device until you finish the move.

For an export, both devices need Claude Desktop 4.23118.0 or later, the same operating system (macOS, Windows, or Linux), and the same organization. If either device runs an earlier version, update it first. Otherwise, the export moves only sessions, their output files, and project names.

### What a Claude Desktop export moves

**Moves:**

* Chats and Cowork tasks
* Their attached files and output files. If a session has more than 100 MB of either, those files don't move.
* Memory, including project memory. If you paused memory on the old device, it's in the file but isn't imported.
* Some app preferences, such as keep-awake settings and prompt suggestions

**Moves, but needs a step from you:**

* Projects. Accept each project's instructions on the project's page.
* The files of each project whose folder is in the default location, `~/Claude/Projects`, if they total under 100 MB and 10,000 items. To use them in Chat, [add the folder to the project again](#make-an-imported-project-folder-readable-in-chat). Hidden files and symbolic links don't move, and some files arrive under another name, such as `CLAUDE.md.txt`.
* Code sessions and Code scheduled tasks. [Copy and trust their folders](#import-your-data-on-the-new-device) before you import.
* Skills you saved, plugins you uploaded, and scheduled tasks. [Turn on the ones you want](#turn-on-imported-plugins-skills-and-scheduled-tasks).
* Local MCP servers that you added, if your organization allows them. [Enter the values of their environment variables again](#set-up-imported-local-mcp-servers).

**Doesn't move:**

* Other folders that your projects, Cowork tasks, and Cowork scheduled tasks use. Copy them yourself, then choose them again, or ask your administrator to [copy your data](https://claude.com/docs/third-party/claude-desktop/data-storage.md#copy-the-data-to-the-new-device).
* The settings **Global instructions** (**Settings > Cowork**) and **Instructions for Claude** (**Settings > General**). Copy their text to the new device yourself.
* Artifacts
* Sign-ins, saved API keys, connectors, and tool permissions such as **Always allow** and **Blocked**
* Desktop extensions, other plugins and marketplaces, plugin settings, other app preferences such as language, theme, and notifications, environment variables for Code sessions, and the values of environment variables for the local MCP servers that you added
* Plugins that you uploaded in the **Code** tab on a version before 4.23118.0. Upload them again on the new device.
* On Windows, Code sessions and Code scheduled tasks whose folder is on a mapped network drive
* Claude Code sessions that you started in a terminal, and Claude Code's own settings and plugins

### Export your data from the old device

> [!WARNING]
>
> The zip file isn't encrypted. Anyone who opens it can read your data, including any passwords or API keys written in it. Keep the file private, and delete every copy when you no longer need it.

1. Go to **Settings > Import & export** and click **Export…**.
2. Select how far back to include sessions, then click **Export**.
3. Choose where to save the zip file.
4. Check the last screen, which lists what the export left out.
5. Copy the zip file to the new device in a way that your organization allows.

![Export your data dialog with the date ranges Last 30 days, Last 90 days, and Everything, a count of 10 sessions, a list headed Export will include, a paragraph on what is not included, and Cancel and Export buttons.](https://mintcdn.com/claude-ai/5RBVEK3ZkxHd5OHc/images/third-party/import/export-dialog.png?fit=max\&auto=format\&n=5RBVEK3ZkxHd5OHc\&q=85\&s=27457ab6a32130509d3e3289fe6d1f94)

The export dialog, with the date range and what the export includes.

If the export shows an error or leaves out something that you need, see [Problems when you move to another device](#problems-when-you-move-to-another-device).

### Import your data on the new device

Set up Claude Desktop on the new device first. The import adds to the data there and replaces nothing. If you import the same file again, you don't get duplicates. If you export again, a session that changed on the old device since the last export arrives as a separate session.

1. If you use the **Code** tab, copy the folders of your Code sessions and Code scheduled tasks to the same paths on the new device, or to the same place under your new home folder if its path changed. Then open each folder in the **Code** tab and click **Trust workspace**.
2. Go to **Settings > Import & export**, click **Import…**, click **Choose file…**, and select the zip file.
3. Continue to the **Review** step and click **Import**.
4. When Claude Desktop asks whether the file is your own export, click **Import as my own**. Click it only for a file that you made yourself. **Import sessions only** imports the sessions, and only the projects and attached files that they use.
5. If the file has local MCP servers, a second dialog lists up to five of them with their commands. If you click **Add**, Claude Desktop tries to start all the listed servers right away, so click it only if you recognize every command. If a message then says that a server couldn't start, close it and finish the import. If you click **Don’t add**, the rest of the import continues.
6. Note the folders that the last screen lists. If it lists **Local MCP servers not imported yet**, import the same file again. If it lists **Folders with Code sessions not imported yet**, repeat step 1 for those folders, then import the same file again.
7. Finish the setup:
   * Accept each project's instructions.
   * Copy your folders, and add them again under **Context** in each project.
   * [Turn on the plugins, skills, and scheduled tasks that you want](#turn-on-imported-plugins-skills-and-scheduled-tasks).
   * [Set up your local MCP servers](#set-up-imported-local-mcp-servers).
   * Reconnect your connectors.

If the import shows an error, or something is missing afterward, see [Problems when you move to another device](#problems-when-you-move-to-another-device).

### Turn on imported plugins, skills, and scheduled tasks

Plugins, skills, and scheduled tasks from an export file are turned off, even if they were on before. The import's last screen names the ones that were on. Before you turn on a scheduled task, turn it off on the old device, or it runs on both devices.

Turn on the ones you want:

* **Plugins**: go to **Customize > Plugins**. Enter any keys or settings the plugin needs.
* **Skills**: go to **Customize > Skills**
* **Cowork scheduled tasks**: go to **Scheduled** in Cowork. If a task used folders or files, choose them again.
* **Code scheduled tasks**: go to **Routines** in the **Code** tab

### Set up imported local MCP servers

The programs that the servers run don't move, and each server's command keeps the paths of the old device. Install the programs at the same paths, or change the paths in the config file. Tools that you blocked on the old device aren't blocked on the new one. To block them again, go to **Customize > Connectors**.

The export leaves the values of these servers' environment variables empty. Until you enter the values, a server might not work, or might run without a limit that you set in a variable. To enter the values or change a path:

1. Go to **Settings > Developer** and click **Edit config** to find the config file.
2. Quit Claude Desktop. If you edit the file while the app is open, the app can overwrite your changes.
3. Open the file in a text editor, make your changes, and save it. The values are in the same file on the old device.
4. Open Claude Desktop again.

## What a claude.ai import includes

For an export file from another device, see [What a Claude Desktop export moves](#what-a-claude-desktop-export-moves).

* **Your data only.** An export contains your own conversations, projects, and memory. Other workspace members' content is not included.
* **Chats and projects come over.** Each imported project appears on the **Projects** page. If the project has custom instructions, Claude Desktop shows them in the project for you to review and accept before they take effect. In Chat, Claude can't read a folder that the import put on a project until you [add the folder to the project again](#make-an-imported-project-folder-readable-in-chat).
* **Artifacts come over as files.** For artifacts Claude created in a conversation, and files Claude wrote with its file-creation tool, the import saves the final version as one of the imported conversation's output files. Earlier versions aren't kept. Past a size limit, the rest of a conversation's artifact content isn't imported, and the conversation says so.
* **Project knowledge files and conversation attachments do not.** A member's own export never includes the contents of files uploaded to a project's knowledge or attached to a conversation. This is a security policy on claude.ai, and it applies to both the **Sign in to claude.ai** and **Choose a downloaded file** paths. Imported chats keep the messages that referenced an attachment, but not the file itself. The only export that includes file contents is an organization-level export, which only a workspace owner can request.
* **One-time copy.** Imported history does not stay in sync with claude.ai. Run the import again to pick up newer conversations; existing imports are matched and skipped, so you won't get duplicates.
* **Download links expire.** The email link from claude.ai is valid for 24 hours. Request a new export if it lapses.

## Troubleshoot an import or export

For an export file from another device, see [Problems when you move to another device](#problems-when-you-move-to-another-device).

Claude Desktop runs each claude.ai import through the Claude CLI binary, the [helper program](https://claude.com/docs/third-party/claude-desktop/installation.md#endpoint-security-software) that also runs your conversations. Unless your organization deploys the [offline installer](https://claude.com/docs/third-party/claude-desktop/installation.md#offline-installation), Claude Desktop downloads the version of the binary it needs separately from the app, when you start a new conversation or task. If this computer doesn't have that version when you click **Import**, Claude Desktop 4.23118.0 or later tries to download it first, and the wizard shows **Downloading the program that converts your chats…** while you wait.

### The import can’t start until a one-time download finishes

The wizard shows this message when this computer has no version of the Claude CLI binary that can import a claude.ai export, and the download isn't finished. If you sign in to fetch the export, the message can appear right after you click **Fetch export**, under **Couldn’t fetch your export**. A running download continues after the message appears. Running the import again retries a failed download. Wait a few minutes, then run the import again.

If the message comes back, ask your administrator to follow [Cowork workspace or Claude CLI fails to download](https://claude.com/docs/third-party/claude-desktop/installation.md#cowork-workspace-or-claude-cli-fails-to-download) and to leave any earlier version of the binary in place.

### Import failed with a code under the message

When an import fails and the wizard has no specific message for the cause, it shows a code, such as `IMPORTER_EXIT`, with **Import failed**, **Your claude.ai export didn’t import**, or **Couldn’t import this export**. If you can import only by signing in, the message asks you to sign in and fetch the export again. On Claude Desktop versions before 4.23118.0, the wizard shows no code, and if you can choose a file, it shows [That doesn’t look like a claude.ai export](#that-doesn%E2%80%99t-look-like-a-claude-ai-export) for these failures.

Your claude.ai export can still be valid. If you import with **Choose file…**, use each `.zip` file as you downloaded it, not renamed or compressed again. On Windows, keep each file's full path under 260 characters, for example by moving it to your Downloads folder.

If you signed in to fetch the export and the wizard still shows **Import**, click it again without closing the wizard. Closing the wizard deletes the fetched export. There's a limit on how often you can fetch an export. In any other case, run the import again from **Settings > Import & export**.

If the import still fails, go to **Help > Troubleshooting > Generate Diagnostic Report** before you quit Claude Desktop, and click **Export to file**. Review [what the report contains](https://claude.com/docs/third-party/claude-desktop/installation.md#troubleshooting), then send your administrator the report's `.zip` file and the code, if the wizard shows one. Your administrator can pass them to your Anthropic representative.

### That doesn’t look like a claude.ai export

Choose the `.zip` file of your [claude.ai export](#step-1-claude-ai-chats-and-projects) as you downloaded it. If the export came as more than one `.zip` file, choose all of them together.

On Claude Desktop versions before 4.23118.0, the message can also appear after you click **Import** on the **Review** step. Your claude.ai export can still be valid. Close the wizard, send any message in a new conversation or task, and wait for the reply, so the import can run on the current version of the Claude CLI binary. Closing the wizard deletes an export that you fetched by signing in, so fetch it again. Then follow the steps in [Import failed with a code under the message](#import-failed-with-a-code-under-the-message). These versions show no code.

### Importing a claude.ai export needs a newer version of this app

On Claude Desktop versions before 4.23118.0, the wizard shows this message, under **Update Claude to import from claude.ai**, when this computer has only an earlier version of the Claude CLI binary that can't import a claude.ai export. You don't need to update or reinstall Claude Desktop. To download the current version of the binary, follow these steps:

**1. Start a new conversation or task**

Close the wizard. Send any message in a new conversation or task, not in an existing one.

**2. Wait for Claude's reply**

The reply can be slow while Claude Desktop downloads the binary.

**3. Open the import wizard again**

Go to **Settings > Import & export** and click **Import…** to open the wizard. The **Chats** step shows its import options in place of the message.

If the message is still there, ask your administrator to follow [Cowork workspace or Claude CLI fails to download](https://claude.com/docs/third-party/claude-desktop/installation.md#cowork-workspace-or-claude-cli-fails-to-download) and to leave the earlier version of the binary in place, because your conversations run on it until the download succeeds.

### Problems when you move to another device

If a [move to another device](#move-your-data-to-another-device) goes wrong, find the message or the problem that you see:

* **Settings > Import & export has no Export… button.** Ask your administrator to [turn on export and import](https://claude.com/docs/third-party/claude-desktop/data-storage.md#turn-on-export-and-import).
* **This export is over the import limit of 20 GB or 5,000,000 files.** If the dialog offers **Shorten date range**, click it, select a shorter range, and click **Export**. If it doesn't, delete sessions from the last 30 days that you no longer need and export again. To move all your sessions, ask your administrator to [copy your data](https://claude.com/docs/third-party/claude-desktop/data-storage.md#copy-the-data-to-the-new-device).
* **The export stopped before it finished, and no file was saved.** Click **Try again**. If it stops again, ask your administrator to [copy your data](https://claude.com/docs/third-party/claude-desktop/data-storage.md#copy-the-data-to-the-new-device).
* **The export's last screen lists items that you need.** On Windows, close other programs and export again, because the export can leave out a file that another program has open. If the items are still listed, ask your administrator to [copy your data](https://claude.com/docs/third-party/claude-desktop/data-storage.md#copy-the-data-to-the-new-device).
* **Couldn’t read that file. Choose a different zip.** On Windows, if you chose the file from a network path such as `\\server\share`, copy the file to a local folder on the new device, or choose it from a mapped network drive such as `Z:\`. Otherwise, copy the file from the old device again, or export again.
* **That export was made in another organization. Choose an export made in this organization.** Ask your administrator to check that both devices are in the same organization.
* **Only your sessions were imported.** Import the same file again, and click **Import as my own** when Claude Desktop asks. If it doesn't ask, update both devices to Claude Desktop 4.23118.0 or later and export again.
* **Sessions that you imported before are missing their attached files.** An export from a version before 4.23118.0 has no attached files, and a later import doesn't add files to a session that's already there. Under **Import history** in **Settings > Import & export**, remove the earlier import, then import the new file. This also deletes the projects that the earlier import made and anything that you added to those sessions since. A session that isn't in the new file doesn't come back.
* **A Code session is missing.** [Copy and trust its folder](#import-your-data-on-the-new-device), then import the same file again and click **Import as my own**. On the last screen, Claude Desktop 5.1231.0 and later list the folders that you still need to copy and trust, under **Folders with Code sessions not imported yet**. If the last screen lists the folder under **Folders with Code sessions that can’t be imported**, or on Windows the folder is on a mapped network drive, the session doesn't move. Ask your administrator to [copy your data](https://claude.com/docs/third-party/claude-desktop/data-storage.md#copy-the-data-to-the-new-device).
* **A Code scheduled task is missing.** On Windows, if its folder is on a mapped network drive, it doesn't move. Ask your administrator to [copy your data](https://claude.com/docs/third-party/claude-desktop/data-storage.md#copy-the-data-to-the-new-device), or create the task again. Otherwise, [copy its folder and trust it](#import-your-data-on-the-new-device), then import the file again. If the task is still missing, create it again.
