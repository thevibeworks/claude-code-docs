> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Import history from claude.ai

> Bring conversations, projects, and local Cowork and Code sessions into Claude Desktop on 3P from a claude.ai workspace or an earlier install

Import brings a copy of your claude.ai conversations and projects into Claude Desktop on third-party (3P), along with any Cowork and Claude Code sessions already on this machine from an earlier install. Everything lands in the local session store described in [User identity and local data](/docs/third-party/claude-desktop/data-storage), so you can pick up work you started on claude.ai and continue it against your organization's own inference provider.

Each import is a one-time copy. New activity on claude.ai after you import does not appear in Claude Desktop unless you import again, and re-running the import does not create duplicates.

## Automatic import of earlier third-party sessions

Claude Desktop can automatically copy into your history the Cowork, Chat, and Code sessions it stored on this computer under an earlier third-party configuration. In an organization managed from the [Enterprise Admin Console](/docs/third-party/claude-desktop/admin-console), this automatic copy is on unless it's turned off in your organization's settings. In any other deployment it runs only if your administrator turns it on.

Along with the sessions, the automatic copy brings over other things you had under the earlier configuration:

* **Projects**: your Cowork projects. New tasks use a project's instructions only after you accept them.
* **Memory and instructions**: your Cowork memory and global instructions. New tasks use them right away. Your **Instructions for Claude** (**Settings → General**) come over too. Instructions you already set under the new configuration are kept.
* **Scheduled tasks**: your scheduled tasks from Cowork and Code. Each stays on or off as it was.
* **Uploaded plugins**: plugins you uploaded, unless your administrator has turned off plugin uploads ([`userPluginUploadsEnabled`](/docs/third-party/claude-desktop/configuration#userpluginuploadsenabled)). Each stays on or off as it was.
* **Saved skills**: skills you saved, unless your administrator has turned off skill creation ([`skillCreationEnabled`](/docs/third-party/claude-desktop/configuration#skillcreationenabled)).
* **Your organization's optional plugins**: the ones you had turned on are turned on again, if they come from your organization's plugins directory or from a marketplace hosted at the address of its gateway or bootstrap server. With Claude Desktop 2.42304.0 or later, plugins from other marketplaces, such as a git repository, are turned on again too, if your administrator offers the marketplace from the same repository or URL as before. On a computer where the copy already ran, they're turned on the first time the app starts on 2.42304.0 or later.
* **Artifacts**: your Cowork artifacts.

The copy runs once on each computer, in the background shortly after the app starts, and the sessions then appear in the sidebar. Your original sessions stay where they were, and sessions you already imported are skipped. The copy is listed under **Import history** in **Settings → Import & export**, where the **Remove** button deletes the copied sessions and the projects copied with them. The app doesn't copy them again later.

Use the [import wizard](#open-the-import-wizard) for your claude.ai conversations and projects, and for any local sessions the automatic copy left out.

## Before you open the import wizard

* Your administrator has turned import on by setting [`claudeAiImport`](/docs/third-party/claude-desktop/configuration#claudeaiimport) with `enabled` set to `true` in the managed configuration. The import wizard is off by default; until then, **Settings → Import & export** has no **Import…** button and reports that import isn't enabled for this deployment. The [automatic import of earlier third-party sessions](#automatic-import-of-earlier-third-party-sessions) doesn't depend on this setting.
* If your administrator lists the claude.ai organizations you may import from, with `allowedOrganizationUuids` under [`claudeAiImport`](/docs/third-party/claude-desktop/configuration#claudeaiimport), you can import only by signing in to claude.ai, and only from a listed organization. A sign-in to any other organization or to a personal account is refused, and the wizard's options to import from a file or from earlier sessions on this computer are turned off. The [automatic import of earlier third-party sessions](#automatic-import-of-earlier-third-party-sessions) isn't affected by this list.
* Claude Desktop is installed and running in third-party mode. See [Installation and setup](/docs/third-party/claude-desktop/installation).
* To bring history over from a claude.ai Team or Enterprise workspace, an owner of that workspace has enabled member data export (next section). Personal claude.ai accounts can always export.

## Enable member data export (admins)

On Team and Enterprise workspaces, member data export is off by default. A workspace owner enables it on claude.ai under **Settings → Organization → Data and privacy → Allow members to export their own data**.

![claude.ai organization settings, Data and privacy page, with the Allow members to export their own data toggle turned on and a confirmation toast reading Member data export enabled.](https://mintcdn.com/claude-ai/HpR2FaaZXZXkiUcV/images/third-party/import/import-admin-toggle.png?fit=max\&auto=format\&n=HpR2FaaZXZXkiUcV\&q=85\&s=f1f4696a2124cd36ee9a7366cb1c4772)

Members of the workspace can then export their own conversations. The toggle does not expose one member's data to another; each member can download only their own history.

## Open the import wizard

In Claude Desktop, go to **Settings → Import & export** and click **Import…** to open the **Import from Claude** wizard.

![Claude Desktop settings with Import and export selected and the Import from Claude wizard open on step 1, showing Sign in to claude.ai and Choose file buttons.](https://mintcdn.com/claude-ai/HpR2FaaZXZXkiUcV/images/third-party/import/import-wizard-start.png?fit=max\&auto=format\&n=HpR2FaaZXZXkiUcV\&q=85\&s=526562f1c9c0abd66e9b56d0328808db)

The wizard has three steps: **Chats** (your claude.ai export), **Cowork & Code** (local sessions on this machine), and **Review**. Skip any step you don't need. A fourth step, **Duplicates**, appears after the import only when an imported project has the same name as one you already have. See [If a project already exists](#if-a-project-already-exists).

## Step 1: claude.ai chats and projects

You can pull your claude.ai history straight into the wizard by signing in, or download it from claude.ai yourself and choose the file.

**Sign in to claude.ai (recommended)**

Click **Sign in to claude.ai…**. Your browser opens to claude.ai; sign in if prompted, choose your organization if you belong to more than one, and click **Authorize**.

![claude.ai organization selector titled Select organization, listing one organization.](https://mintcdn.com/claude-ai/HpR2FaaZXZXkiUcV/images/third-party/import/import-consent-org.png?fit=max\&auto=format\&n=HpR2FaaZXZXkiUcV\&q=85\&s=1657a03028a7ceb3d173e71ba27f591d)

![claude.ai authorization card reading Claude Desktop Import would like to connect to your Claude chat account, with an Authorize button.](https://mintcdn.com/claude-ai/HpR2FaaZXZXkiUcV/images/third-party/import/import-consent-authorize.png?fit=max\&auto=format\&n=HpR2FaaZXZXkiUcV\&q=85\&s=55be3501d41c9e61b49154db66b71d5b)

Back in Claude Desktop, click **Fetch export**. The wizard requests an export from claude.ai, downloads it, and shows what it found.

![Import from Claude wizard step 1 showing a claude.ai export row with the account email and a summary of 7 chats and 1 project.](https://mintcdn.com/claude-ai/HpR2FaaZXZXkiUcV/images/third-party/import/import-signed-in.png?fit=max\&auto=format\&n=HpR2FaaZXZXkiUcV\&q=85\&s=dafc4cbfffd685321442cbd72fd73993)

**Choose a downloaded file**

On claude.ai, go to **Settings → Privacy → Export data** and click **Export**. If you don't see **Export data**, ask a workspace owner to [enable member data export](#enable-member-data-export-admins).

![claude.ai settings Privacy page with the Export data subpage open, showing an Export button and a note that a download link will be sent by email.](https://mintcdn.com/claude-ai/HpR2FaaZXZXkiUcV/images/third-party/import/import-web-export.png?fit=max\&auto=format\&n=HpR2FaaZXZXkiUcV\&q=85\&s=1ed4aa5a08469420020d3ff83579c0de)

claude.ai emails you a download link when the export is ready. The link expires after 24 hours.

![Email from Claude titled Your data is ready for download with a Download data button.](https://mintcdn.com/claude-ai/HpR2FaaZXZXkiUcV/images/third-party/import/import-email.png?fit=max\&auto=format\&n=HpR2FaaZXZXkiUcV\&q=85\&s=cf883e9c401401686568c77cb6ac45c1)

Download the `.zip`, then in the import wizard click **Choose file…** and select it.

![Import from Claude wizard step 1 showing a selected member-data zip file with a summary of 7 chats and 1 project.](https://mintcdn.com/claude-ai/HpR2FaaZXZXkiUcV/images/third-party/import/import-choose-file.png?fit=max\&auto=format\&n=HpR2FaaZXZXkiUcV\&q=85\&s=5cb868969ebed88801296f696796d0f1)

Click **Continue**, or **Skip this step** if you only want to bring in local sessions.

## Step 2: local Cowork and Code sessions

The wizard scans this machine for Cowork and Claude Code sessions from an earlier Claude Desktop install and lists what it finds. Choose how far back to include, and add any other folder that holds sessions (for example, a backup or a folder copied from another machine).

![Import from Claude wizard step 2, Cowork and Code, listing 5 local sessions with a time-range selector and an option to add another location.](https://mintcdn.com/claude-ai/HpR2FaaZXZXkiUcV/images/third-party/import/import-local-sessions.png?fit=max\&auto=format\&n=HpR2FaaZXZXkiUcV\&q=85\&s=e17511922a814b0355cb540688a5c949)

Sessions are copied, not moved. Your original history stays where it is.

## Step 3: review and import

The **Review** step summarizes what will be added. Click **Import** to copy everything into your local session store.

![Import from Claude wizard step 3 showing a claude.ai export summary of 7 chats and 1 project alongside 5 local Cowork and Code sessions, with an Import button.](https://mintcdn.com/claude-ai/HpR2FaaZXZXkiUcV/images/third-party/import/import-review.png?fit=max\&auto=format\&n=HpR2FaaZXZXkiUcV\&q=85\&s=c7939485c7185afbf1ef7518a94db2d6)

![Import from Claude wizard success screen showing a checkmark and the number of sessions imported, with a note that re-running import will not create duplicates.](https://mintcdn.com/claude-ai/XDpDaIQ3J0Amhn8h/images/third-party/import/import-success.png?fit=max\&auto=format\&n=XDpDaIQ3J0Amhn8h\&q=85\&s=f0a01a38e52d841b66c4215f9cda2db4)

## If a project already exists

When an imported project has the same name as a project already in Claude Desktop, the wizard adds a **Duplicates** step after the import finishes. This happens, for example, when you set up **Northwind** on this machine and then bring over history from another machine that also has a Northwind project. The step lists each match with two choices.

![Import from Claude wizard step 4, Duplicates, headed These projects already exist, listing five Northwind projects each with Merge into existing and Keep separate buttons and a Continue button.](https://mintcdn.com/claude-ai/XDpDaIQ3J0Amhn8h/images/third-party/import/import-duplicates.png?fit=max\&auto=format\&n=XDpDaIQ3J0Amhn8h\&q=85\&s=798f75d5a508ebcb7082373b5cf95d84)

* **Merge into existing** moves the imported chats and sessions into your existing project and removes the duplicate. Folders you attached to the duplicate move with them. If your existing project has no instructions of its own, the imported project's instructions are shown there for you to review and accept. Later imports from the same source land in the existing project as well.
* **Keep separate** leaves both projects in place. The imported one keeps a numbered name, such as **Northwind (1)**, and Claude Desktop stops offering to merge it.

The **Projects** page offers the same two choices, in a row under the duplicate project's card and at the top of the duplicate project's own page. Decide there if your history was brought over automatically when you signed in, so you never saw the wizard, or if you closed the wizard before choosing.

## Continue an imported conversation

Open any imported conversation from the sidebar and keep chatting. The first time you send a message in an imported session, Claude Desktop asks you to confirm before it continues. The reply then comes from your configured inference provider, not from claude.ai.

* A session from this app's earlier third-party configuration on this computer shows a **Continue this conversation?** prompt. Click **Continue** to send your message.
* Any other imported conversation or session shows a **Resume imported session?** prompt. Click **Trust and resume** to continue.

![An imported conversation open in Cowork with a yellow Resume imported session card offering Go back and Trust and resume buttons.](https://mintcdn.com/claude-ai/HpR2FaaZXZXkiUcV/images/third-party/import/import-trust-resume.png?fit=max\&auto=format\&n=HpR2FaaZXZXkiUcV\&q=85\&s=806d0d2018d7fc0f10afb71035b1f807)

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

Your administrator can also limit which folders Claude reads. See [Project folders in Chat](/docs/third-party/claude-desktop/chat#project-folders-in-chat).

## Export sessions to move them to another device

When your administrator also sets `exportEnabled` to `true` under `claudeAiImport`, **Settings → Import & export** offers **Export…**, which writes this computer's chats, Cowork tasks, and Code sessions (not terminal Claude Code sessions) to a zip file. On the other device, open the import wizard and select that zip with **Choose file…**; the wizard lists its sessions in the [Cowork & Code step](#step-2-local-cowork-and-code-sessions). The export is a one-time snapshot, not a sync, and the zip contains full conversation content, so handle it as sensitive data.

The zip includes sessions, project names, and each session's output files when they total 100 MB or less. It leaves out project instructions, memory, scheduled tasks, skills, plugins, and attached files. To move those, your administrator can [copy your data to the new device](/docs/third-party/claude-desktop/data-storage#move-a-user-to-a-new-device). Sign-ins and connector connections don't move either way.

## What is and isn't included

* **Your data only.** An export contains your own conversations, projects, and memory. Other workspace members' content is not included.
* **Chats and projects come over.** Each imported project appears on the **Projects** page. If the project has custom instructions, Claude Desktop shows them in the project for you to review and accept before they take effect. In Chat, Claude can't read a folder that the import put on a project until you [add the folder to the project again](#make-an-imported-project-folder-readable-in-chat).
* **Artifacts come over as files.** For artifacts Claude created in a conversation, and files Claude wrote with its file-creation tool, the import saves the final version as one of the imported conversation's output files. Earlier versions aren't kept. Past a size limit, the rest of a conversation's artifact content isn't imported, and the conversation says so.
* **Project knowledge files and conversation attachments do not.** A member's own export never includes the contents of files uploaded to a project's knowledge or attached to a conversation. This is a security policy on claude.ai, and it applies to both the **Sign in to claude.ai** and **Choose a downloaded file** paths. Imported chats keep the messages that referenced an attachment, but not the file itself. The only export that includes file contents is an organization-level export, which only a workspace owner can request.
* **One-time copy.** Imported history does not stay in sync with claude.ai. Run the import again to pick up newer conversations; existing imports are matched and skipped, so you won't get duplicates.
* **Download links expire.** The email link from claude.ai is valid for 24 hours. Request a new export if it lapses.
