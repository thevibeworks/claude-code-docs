> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Run tasks in the background with Dispatch

> Assign work to a Dispatch agent that plans, runs, and reports on tasks while you do something else, on this computer or from your phone.

Dispatch is a long-running agent in Cowork that takes high-level instructions and carries them out in the background. You describe an outcome in a single conversation; the Dispatch agent breaks it into tasks, runs each one as a separate Cowork or Code session, and surfaces the results in the sidebar when they finish.

Unlike a normal Cowork chat, you don't watch each step. Dispatch is for work you want to start and come back to later.

## Prerequisites

Dispatch requires a Pro or Max plan and the latest Claude Desktop app on macOS or Windows.

## Start a Dispatch task

The Dispatch agent appears as **Dispatch** in the left sidebar. Selecting it opens a single conversation with the agent.

<Steps>
  <Step title="Open Dispatch from the sidebar">
    Select **Dispatch** in the left side panel.
  </Step>

  <Step title="Describe the outcome">
    Tell the agent what you want done, the same way you'd brief a colleague. For
    example: "Summarize the open Linear issues tagged reliability and draft a
    status update for the team channel."
  </Step>

  <Step title="Let Dispatch plan and run">
    The agent decides how to split the work and starts one or more child tasks.
    Each child task appears under the Dispatch group in the sidebar with its own
    status.
  </Step>
</Steps>

You converse with one Dispatch agent, but it can run many child tasks beneath that conversation. Child tasks don't spawn further children of their own.

## How Dispatch routes work

The Dispatch agent routes each child task to the surface that fits it.

| Task type      | Runs in                                                                                | Examples                                   |
| -------------- | -------------------------------------------------------------------------------------- | ------------------------------------------ |
| Coding work    | Code, against a workspace you've already set up                                        | Fix a bug, open a pull request, run tests  |
| Knowledge work | Cowork, in the [project](/docs/cowork/guide/projects) you specify (or your default project) | Research, write a document, organize files |

When starting a task, you can tell the agent which Code workspace or Cowork project to use. If you don't, it lists what's available and chooses.

## Track task status

Each child task shows its current state in the sidebar. Select any task to open its full transcript, the steps Claude took, and any files it produced.

| State           | Meaning                                                    |
| --------------- | ---------------------------------------------------------- |
| Running         | Claude is actively working on the task                     |
| Awaiting input  | The task needs information from you before it can continue |
| Awaiting answer | The task asked you a question and is waiting for a reply   |
| Completed       | The task finished                                          |
| Error           | The task stopped because something went wrong              |
| Archived        | You marked the task as done and set it aside               |

## Approve actions Dispatch needs

When a child task needs permission to take an action (such as running a command or writing a file outside its workspace), the prompt is forwarded to you. If you don't respond within ten minutes, the request is automatically denied and the task continues without that action.

Permission prompts behave the same as in a normal Cowork session.

## Continue from a finished task

Select any child task in the sidebar to open its session. You can read the transcript, send follow-up messages, or ask the Dispatch agent to start a new task that builds on the result.

## Assign tasks from your phone

When Claude Desktop is running, your computer registers as a Dispatch host. From the Claude mobile app, you can start a Dispatch conversation that runs on your desktop, then check results from either device.

<Steps>
  <Step title="Keep your desktop ready">
    Leave Claude Desktop open with your computer awake and online.
  </Step>

  <Step title="Open Dispatch on mobile">
    In the Claude mobile app, open Dispatch and describe the task. The work runs
    on your desktop.
  </Step>

  <Step title="Review on either device">
    Progress and results appear in the Dispatch sidebar on desktop and in the
    mobile app.
  </Step>
</Steps>

## Related

* [Organize work with projects](/docs/cowork/guide/projects) for the project context Dispatch routes knowledge work into
* [Cowork overview](/docs/cowork/overview) for how Dispatch fits alongside sessions and projects
