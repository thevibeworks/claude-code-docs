# Schedule recurring tasks in Claude Cowork

Scheduled tasks allow you to delegate work to Claude Cowork by creating tasks that run automatically on a recurring basis, or on demand. Instead of starting each task from scratch, you describe it once and Claude handles it on your schedule—delivering finished outputs like reports, briefings, and summaries every time.

Scheduled tasks are available in Cowork for all paid plans (Pro, Max, Team, Enterprise).

Claude Cowork is in beta on web and mobile, and rolling out over the next several weeks starting with the Max plan, with more plans to follow.

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

**Note:** Scheduled tasks use the built-in schedule options and work with your connectors and the files saved to your Claude account. They can't be tied to a folder on your computer.

For Team and Enterprise organizations, admins control Cowork access through the admin toggle. For more details, see **[Use Claude Cowork on Team and Enterprise plans](https://support.claude.com/en/articles/13455879)**.

---

## Create a scheduled task

There are two ways to create a scheduled task:

### Create with Claude

1. Click “Scheduled” in the left sidebar to land on the **Scheduled tasks** page.

2. Click “New task” in the upper right, then choose "Create with Claude."

3. This creates a new task auto-filled with a prompt asking Claude to create a scheduled task.

4. Claude may ask you questions with **[multiple choice responses](https://support.claude.com/en/articles/13641943-visual-and-interactive-content#h_6bd6fbd2c3)** before creating the scheduled task.

5. Once Claude has all the necessary information, it will output the name of the task it’s creating, the schedule it will follow, and what the task actually does.

6. You can explicitly confirm you want to schedule the task when prompted by Claude by clicking “Schedule":

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2104085399/4dda7e6f76026fd827db0b9323a9/f20635bf-15e7-4978-a213-5b9f67e9fb9a?expires=1784348100&amp;signature=2f35a9f5fa72046eb13f2645e21e3bcf11b1f76160ae22aae4aae4a7bfb1b682&amp;req=diEnEsl2mIJWUPMW1HO4zeLJBkHn%2B%2BKGPx%2FSrZI7l8ycxLK7iDbHgR%2BfYCUH%0Ao8v2%0A)

7. Claude will create and schedule your task, and it will be added to the **Scheduled tasks** page.

### Set up manually

1. Click “Scheduled” in the left sidebar to land on the **Scheduled tasks** page.

2. Click “New task” in the upper right, then choose “Set up manually.”

3. In the **Create scheduled task** modal, enter the following information:

  1. Task name

  2. The prompt describing what your task does

  3. The approval mode

  4. How frequently the task will run (hourly, daily, weekly, on weekdays, or manually)

  5. The model you want to use [optional]

  6. Which folder Claude should work in [optional]

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