Title: Schedule recurring tasks in Claude Cowork

URL Source: https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork

Markdown Content:
# Schedule recurring tasks in Claude Cowork | Claude Help Center

[Skip to main content](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork#main-content)

[![Image 1: Claude Help Center](https://downloads.intercomcdn.com/i/o/lupk8zyo/787776/ade321b9d8ff06050cb06ac0049d/d7ef4b66df4ff3851b5de741185c97ab.png)](https://support.claude.com/en/)

[API Docs](https://docs.claude.com/en/docs/intro)[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)[How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support)

English

[API Docs](https://docs.claude.com/en/docs/intro)[Release Notes](https://support.claude.com/en/articles/12138966-release-notes)[How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support)

English

Search for articles... 

1.   [All Collections](https://support.claude.com/en/) 
2.   [Claude](https://support.claude.com/en/collections/4078531-claude) 
3.   [Features and capabilities](https://support.claude.com/en/collections/18031719-features-and-capabilities) 
4.   Schedule recurring tasks in Claude Cowork

# Schedule recurring tasks in Claude Cowork

April 9, 2026

Table of contents

[What scheduled tasks can do](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork#h_e398cc7af0)[How scheduled tasks work](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork#h_2d97bb4e5d)[Create a scheduled task](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork#h_0baecef079)[Manage your scheduled tasks](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork#h_ed497a2a81)

Scheduled tasks allow you to delegate work to Claude Cowork by creating tasks that run automatically on a recurring basis, or on demand. Instead of starting each task from scratch, you describe it once and Claude handles it on your schedule—delivering finished outputs like reports, briefings, and summaries every time.

Scheduled tasks are available in Cowork on Claude Desktop for all paid plans (Pro, Max, Team, Enterprise).

## What scheduled tasks can do

Scheduled tasks have access to the same capabilities as regular Cowork tasks, including connected tools, skills, and installed plugins. Common uses include:

*   **Daily briefings:** Summarize Slack messages, emails, or calendar events from the past 24 hours. 
*   **Weekly reports:** Compile data from Google Drive, spreadsheets, or connected tools into a formatted summary. 
*   **Recurring research:** Track topics, competitors, or industry news on a regular cadence. 
*   **File organization:** Periodically sort, clean up, or process files in a designated folder. 
*   **Team updates:** Generate status updates or standup summaries from project management tools. 

## How scheduled tasks work

When you create a scheduled task, Claude saves your prompt as the task's instructions and runs them at the cadence you choose. Tasks can search Slack, query files, run web research, generate reports, and more—using any connectors and plugins you've set up in Cowork.

Each scheduled task runs as its own Cowork session. You can review the results when they're ready, just like any other task.

**Important:** Scheduled tasks only run while your computer is awake and the Claude Desktop app is open. If your computer is asleep or the app is closed when a task is scheduled to run, Cowork will skip the task, then run it automatically once your computer wakes up or you open the desktop app again. When Cowork re-runs a skipped task, you will see a notification letting you know. Skipped runs also appear in the task’s history.

For Team and Enterprise organizations, admins control Cowork access through the admin toggle. For more details, see **[Cowork for Team and Enterprise plans](https://support.claude.com/en/articles/13455879)**.

* * *

## Create a scheduled task

There are two ways to create a scheduled task:

### From any task using the /schedule Skill

1.   Open Cowork and click “+ New task” in the upper left corner to start a new task. 
2.   Enter your prompt in the chat input, then click "Let's go" to start the task. 
3.   Alternatively, open an existing task. 
4.   Type "/schedule" in the chat input. 
5.   This launches a Skill to create a scheduled task that can be run on demand or automatically on an interval. 
6.   Add any other required details about the task you’re trying to create in the chat input and send the message. 
7.   Claude may ask you questions with **[multiple choice responses](https://support.claude.com/en/articles/13641943-visual-and-interactive-content#h_6bd6fbd2c3)** before creating the scheduled task. 
8.   Once Claude has all the necessary information, it will output the name of the task it’s creating, the schedule it will follow, and what the task actually does. 
9.   You can explicitly confirm you want to schedule the task when prompted by Claude by clicking “Schedule":  [![Image 2](https://downloads.intercomcdn.com/i/o/lupk8zyo/2104085399/4dda7e6f76026fd827db0b9323a9/f20635bf-15e7-4978-a213-5b9f67e9fb9a?expires=1781626500&signature=11e2a5766fde9f183a878df39cf15645f56383864c668135761d56235cd26c27&req=diEnEsl2mIJWUPMW1HO4zeLJBkTi%2FeyCPx%2FSrZI7l8ysyHB6980kLOT7dNgq%0AWjLA%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2104085399/4dda7e6f76026fd827db0b9323a9/f20635bf-15e7-4978-a213-5b9f67e9fb9a?expires=1781626500&signature=11e2a5766fde9f183a878df39cf15645f56383864c668135761d56235cd26c27&req=diEnEsl2mIJWUPMW1HO4zeLJBkTi%2FeyCPx%2FSrZI7l8ysyHB6980kLOT7dNgq%0AWjLA%0A)  
10.   Claude will create and schedule your task, and it will be added to the “Scheduled tasks” page. 

### From the “Scheduled tasks” page

1.   Click “Scheduled” in the left sidebar. 
2.   Click “+ New task” in the upper right. 
3.   In the **Create scheduled task** modal, enter the following information: 

    1.   Task name 
    2.   Description of the task 
    3.   The prompt describing what your task does. 

        1.   **Note:** Type "/" to include plugins and Skills. 

    4.   How frequently the task will run (hourly, daily, weekly, on weekdays, or manually) 
    5.   The model you want to use [optional] 
    6.   Which folder Claude should work in [optional] 

4.   Click “Save” to add a new task to the **Scheduled tasks** page. 

## Manage your scheduled tasks

To view and manage all your scheduled tasks, click “Scheduled” in the left sidebar. From here you can:

*   View all the scheduled tasks you’ve created 
*   Review upcoming and past runs 
*   Click into individual tasks to manually edit the instructions or cadence 
*   Pause a scheduled task 
*   Resume a paused task 
*   Delete a scheduled task 
*   Run a task on demand 

* * *

Related Articles

[Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)[Use Claude Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)[Use Claude Cowork on Team and Enterprise plans](https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans)[Assign tasks from anywhere in Claude Cowork](https://support.claude.com/en/articles/13947068-assign-tasks-from-anywhere-in-claude-cowork)[Organize your tasks with projects in Claude Cowork](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork)

Did this answer your question?

😞😐😃

Table of contents

[What scheduled tasks can do](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork#h_e398cc7af0)[How scheduled tasks work](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork#h_2d97bb4e5d)[Create a scheduled task](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork#h_0baecef079)[Manage your scheduled tasks](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork#h_ed497a2a81)

[![Image 3: Claude Help Center](https://downloads.intercomcdn.com/i/o/487548/17213f6a445c8e6e874b1f4b/fad85208982e639d11b9108df895a293.png)](https://support.claude.com/en/)

*   [Product](https://www.anthropic.com/product)
*   [Research](https://www.anthropic.com/research)
*   [Company](https://www.anthropic.com/company)
*   [News](https://www.anthropic.com/news)
*   [Careers](https://www.anthropic.com/careers)

*   [Terms of Service - Consumer](https://www.anthropic.com/terms)
*   [Terms of Service - Commercial](https://www.anthropic.com/legal/commercial-terms)
*   [Privacy Policy](https://www.anthropic.com/privacy)
*   [Usage Policy](https://www.anthropic.com/aup)
*   [Responsible Disclosure Policy](https://www.anthropic.com/responsible-disclosure-policy)
*   [Compliance](https://trust.anthropic.com/)
