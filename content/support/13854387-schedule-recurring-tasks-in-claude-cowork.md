# Schedule recurring tasks in Claude Cowork

Scheduled tasks allow you to delegate work to Claude Cowork by creating tasks that run automatically on a recurring basis, or on demand. Instead of starting each task from scratch, you describe it once and Claude handles it on your schedule—delivering finished outputs like reports, briefings, and summaries every time.

## Availability

Scheduled tasks are available on all paid plans (Pro, Max, Ultra, Team, and Enterprise), in Claude Cowork and in the new Claude experience.

Claude Cowork is available on desktop on all paid plans (Pro, Max, Ultra, Team, and Enterprise). On web and mobile, it's available on Pro, Max, Ultra, and Team plans (in beta on Team), and on Enterprise plans when an owner enables it.

The new Claude experience, which combines chat and Cowork, is rolling out to Pro, Max, and Ultra plans. On Team plans (in beta) and Enterprise plans, it's available where **Chat and Cowork unified** is turned on. If your message box no longer shows "Chat" and "Cowork" options, you have the new experience, and some steps in this article may look different. Learn more in **[Claude Cowork and chat are one Claude](https://support.claude.com/en/articles/16761823)**.

---

## What scheduled tasks can do

Scheduled tasks have access to the same capabilities as regular Cowork tasks, including connected tools, skills, and installed plugins. Common uses include:

- **Daily briefings:** Summarize Slack messages, emails, or calendar events from the past 24 hours.

- **Weekly reports:** Compile data from Google Drive, spreadsheets, or connected tools into a formatted summary.

- **Recurring research:** Track topics, competitors, or industry news on a regular cadence.

- **File organization:** Periodically sort, clean up, or process files in a designated folder.

- **Team updates:** Generate status updates or standup summaries from project management tools.

## How scheduled tasks work

When you create a scheduled task, Claude saves your prompt as the task's instructions and runs them at the cadence you choose. Tasks can search Slack, query files, run web research, generate reports, and more—using any connectors and plugins you've set up in Cowork.

Each scheduled task runs as its own Cowork session. You can review the results when they're ready, just like any other task.

Scheduled tasks run remotely, so they run on their cadence even when your computer is asleep or the Claude Desktop app is closed. Review upcoming and past runs by clicking "Scheduled" in the left sidebar on any surface.

**Note:** Scheduled tasks use the built-in schedule options and work with your connectors and the files saved to your Claude account. On Pro, Max, and Ultra plans, scheduled tasks you created before October 6 that run on your computer keep running there.

For Team and Enterprise organizations, admins control Cowork access through the admin toggle. For more details, see **[Use Claude Cowork on Team and Enterprise plans](https://support.claude.com/en/articles/13455879)**.

---

## Create a scheduled task

### In the new Claude experience

If your message box doesn’t show “Chat” and “Cowork” options, you have the new Claude experience. Create a scheduled task from any conversation:

1. Describe the task and how often it should run, for example, "Every Monday at 9 AM, summarize last week's messages in my team's Slack channels."

2. Answer any questions Claude asks about the schedule or the task.

3. Review the task name, schedule, and instructions Claude proposes, then click "Schedule."

### In Claude Cowork

There are two ways to create a scheduled task in Cowork:

**Create with Claude**

1. Click “Scheduled” in the left sidebar to land on the **Scheduled tasks** page.

2. Click “New task” in the upper right, then choose "Create with Claude."

3. This creates a new task auto-filled with a prompt asking Claude to create a scheduled task.

4. Claude may ask you questions with **[multiple choice responses](https://support.claude.com/en/articles/13641943-visual-and-interactive-content#h_6bd6fbd2c3)** before creating the scheduled task.

5. Once Claude has all the necessary information, it will output the name of the task it’s creating, the schedule it will follow, and what the task actually does.

6. You can explicitly confirm you want to schedule the task when prompted by Claude by clicking “Schedule."

7. Claude will create and schedule your task, and it will be added to the **Scheduled tasks** page.

**Set up manually**

1. Click “Scheduled” in the left sidebar to land on the **Scheduled tasks** page.

2. Click “New task” in the upper right, then choose “Set up manually.”

3. In the **Create scheduled task** modal, enter the following information:

  1. Task name

  2. The prompt describing what your task does

  3. The approval mode

  4. How frequently the task will run (hourly, daily, weekly, on weekdays, or manually)

  5. The model you want to use (optional)

  6. Which folder Claude should work in (optional)

    1. **Note:** If a scheduled task requires local files or apps, it will only run locally.

4. Click “Save” to add a new task to the **Scheduled tasks** page.

## Manage your scheduled tasks

To view and manage all your scheduled tasks, click “Scheduled” in the left sidebar. From here you can:

- View all the scheduled tasks you’ve created

- Review upcoming and past runs

- Click into individual tasks to manually edit the instructions or cadence

- Pause a scheduled task

- Resume a paused task

- Delete a scheduled task

- Run a task on demand