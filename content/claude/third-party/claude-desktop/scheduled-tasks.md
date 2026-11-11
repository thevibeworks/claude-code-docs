> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Scheduled tasks in Claude Desktop on 3P

> What scheduled tasks in Claude Desktop on 3P need in order to run, what users are told when a run is late or fails, and the keys that control them

A scheduled task is a prompt that a user saves with a schedule, such as every weekday at 8:00 AM, on the **Scheduled** page in Cowork or the **Routines** page in Code. Claude Desktop on third-party (3P) runs the prompt in a new session at each scheduled time, even when the user is away.

Scheduled tasks run locally, in Claude Desktop on the user's device, which must be awake with the app open.

## What a scheduled task needs to run

A run needs each of the following:

* **The device is awake and Claude Desktop is open**: a task that misses its time runs once after the device wakes or the app opens. If it missed several times, it runs for the latest one only, and the task's **History** shows the earlier ones as one **Skipped** entry. A recurring task's missed time more than seven days old doesn't run and isn't listed.
* **The device can reach your inference provider**: while the device has no network connection, the run waits. If your provider or gateway doesn't answer, or returns a server error such as 500, 503, or 529, before Claude starts to respond, Claude Desktop starts the run again up to eight times over three to four hours, stopping at the task's next scheduled time. The user is notified of the first failure and of the final outcome. Claude Desktop doesn't retry a 401, 403, or 429 response, or a failure after Claude starts to respond.
* **The user is signed in**: where users sign in to your gateway, inference provider, or bootstrap server, runs wait while the sign-in has expired. Claude Desktop notifies the user to sign in again, and the runs start after that.
* **The task's connectors are signed in**: otherwise the run continues without the connector, and its notification reads **Reconnect** or **Couldn’t use**, followed by the connector's name
* **Each step that asks for approval gets an answer**: otherwise the run waits at the prompt, and the user is notified. In Cowork, an unanswered prompt delays the task's next scheduled run by up to two hours. When a new run starts, Claude Desktop declines the prompt, and the earlier run goes on without that step and reports **Scheduled task skipped a step**. In Code, Claude Desktop denies a prompt that goes unanswered for about 48 minutes, and the run stops.

### Keep the device awake and the app open

The user goes to **Settings > This computer > System** and turns on two toggles:

* **Keep computer awake**: while Claude Desktop is open, the device doesn't go to sleep when idle. Closing a laptop's lid still puts it to sleep.
* **Run on startup**: Claude Desktop opens when the user logs in to the device

## Approvals that last across runs

Each run is a new session, so an approval for that run alone ends with it. For a task to finish unattended, the user answers each prompt once with the option that lasts:

* **Connector tools**: the user chooses **Allow for all scheduled runs** in Cowork or **Always allow** in Code, or **Allow for 7 days**, for example, under your [time limit](https://claude.com/docs/third-party/claude-desktop/configuration.md#tool-approvals-on-scheduled-tasks). A tool that your [`toolPolicy`](https://claude.com/docs/third-party/claude-desktop/configuration#tool-permissions-for-managed-mcp-servers) sets to `"ask"` has no such option, so each run in which Claude calls the tool waits for the user.
* **Built-in tools**: a lasting approval can also cover a shell command, a file path, or a website. It has no time limit.
* **File deletion in Cowork**: the prompt that asks before Claude deletes files in a folder offers **Allow for 30 days**, or for the number of days in your time limit. The approval covers that folder and its subfolders until the date shown. It's offered only for a folder chosen on the task itself, and not when the task's permission mode is [**Automatically approve**](https://claude.com/docs/third-party/claude-desktop/configuration.md#automodeenabled).

The task's page lists these approvals under **Always allowed**, where the user can remove them.

## Where users see what ran

Users can see how each task's latest run went without opening the run:

* **Sidebar**: each Cowork task that is turned on has its own row, marked when its latest run failed, is waiting for the user, is unread, or is running
* **Scheduled and Routines pages, and each task's page**: the status of the latest run, such as **Last run failed, will try again**, **Needs input**, **Waiting for you to sign in**, or **Didn’t run**
* **Notifications**: unless the user has turned them off, Claude Desktop sends a desktop notification when a run finishes, fails, waits for the user, or can't start

For a support request, the [diagnostic report](https://claude.com/docs/third-party/claude-desktop/installation.md#troubleshooting) has a **Scheduled tasks** section.

## Configuration keys for scheduled tasks

These keys control scheduled tasks for your organization:

* [`scheduledTasksEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#scheduledtasksenabled): turns scheduled tasks on or off in Cowork and Code
* [`keepAwakeEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#keepawakeenabled): allows keep-awake, or blocks it and hides its toggles
* [`mcpScheduledTaskApprovalLifetimeDays`](https://claude.com/docs/third-party/claude-desktop/configuration#mcpscheduledtaskapprovallifetimedays): sets how many days a task's approvals of connector tools and file deletion hold, and `0` turns those off. While it's unset, [`mcpPersistentAlwaysAllowEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#mcppersistentalwaysallowenabled) decides whether prompts offer them. [Some approvals aren't covered](https://claude.com/docs/third-party/claude-desktop/configuration.md#tool-approvals-on-scheduled-tasks).
