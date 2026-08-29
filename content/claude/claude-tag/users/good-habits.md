> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Good habits for working with Claude Tag

> Name the outcome, give every task a definition of done, and pick the right channel. See how to write tasks Claude can finish and how to keep many threads reviewable.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

Tasks should have a verifiable end state. Claude runs each one in its own thread, and a thread closes when someone can confirm the work is done. A task without that end state produces an open-ended report, and the thread stays open while you decide what to do with it.

The habits here are for anyone who tags Claude in from Slack.

## Work in the open

Claude is most useful when the work is somewhere the team can see, steer, and build on. A few mindsets make that the default rather than something you remember to do.

* **Work in public.** Assume everyone in the channel can read the thread, including its checklist and results. Anything your team writes down, like decisions, conventions, and postmortems, is context Claude can use. Knowledge that lives in DMs or was only said aloud is invisible to it. Put anything personal in a DM instead.
* **Share control.** Replying in a thread someone else started is how work moves. Redirect the approach, add what the requester didn't know, or pick up the result and run with it.
* **Grant broad access.** A channel with more connections (the tools an admin linked for this channel, like GitHub or Drive) produces more useful results, because Claude can join more sources together. The connections are scoped to the agent's identity, so granting them to a channel does not expose anyone's personal data.
* **Give Claude the destination, not the route.** State the outcome you want and let Claude work out the steps; the [definition of done](#give-every-task-a-definition-of-done) below makes that concrete.
* **Tolerate the mess.** A first draft posted in the thread is more useful than a polished one in a DM. The thread is the workspace, not the deliverable.

### Mentioning people who aren't in the channel

Claude can't add anyone to a channel, and it doesn't decide whether a mentioned person is notified. Slack's prompt to invite or notify someone who isn't in the channel appears only for messages you type yourself; it never applies to messages Claude posts. Slack delivers Claude's mention the way it delivers any app-posted message. In a public channel, the person is notified in their Activity view even though they haven't joined. In a private channel, they aren't notified and can't see the message until someone invites them. If you want someone to follow a thread Claude is working in, invite them yourself.

## Write tasks that close

The phrasing of a task determines whether it has a verifiable end state, what form the result takes, and how Claude responds while working on it.

### Name the outcome, not the activity

A task like "post the project status and tag me when it's up" has an end state Claude can verify; "look at this" does not, and invites an open-ended report. Put the verifiable outcome in the first sentence of the task.

### How much detail to give

Claude [reads the thread you tag it in, can search the workspace's public channels, and works with the channel's connections](/docs/claude-tag/users/getting-started#what-claude-can-see). If the background for your task is already in a thread, channel, or connected tool, link to it and state the outcome you want in one sentence. You don't need to restate the background.

```text wrap theme={null}
@Claude take over the bug in the thread linked above. Fix it and open a draft PR.
```

When a mistake would be costly to undo, give Claude more detail. Write the detail as constraints: name the rules the change must respect, the checks that count as verification, and what the work must not touch.

```text wrap theme={null}
@Claude migrate the export config to the new schema. Hard rules: no behavior change, don't touch the billing module, and every old config key keeps working as an alias. Done means the full test suite passes, not only the export tests.
```

<Warning>Constraints in a task steer Claude but don't restrict Claude from performing a specific action. Anything you type to Claude goes into its working context, where it can be forgotten or overridden. If there are actions Claude must not take, enforce them outside the conversation, with controls like repository permissions, branch protection rules, and required checks.</Warning>

### Give every task a definition of done

Starting a thread costs one sentence. Closing it costs your attention, because you read the output, decide whether it's right, and reply.

Without a stated end condition, Claude can't declare the thread finished and you can't stop checking it. The end condition you write determines who can close the thread, and the table matches each kind of condition to who closes it.

| End condition                  | Who closes it      | Example                                               |
| :----------------------------- | :----------------- | :---------------------------------------------------- |
| An objective check passes      | Claude, on its own | "Done when CI is green"                               |
| You approve a prepared result  | You, one click     | "Draft the status memo and post it here for approval" |
| You choose between options     | You, one word      | "Research approaches A and B and recommend one"       |
| No verifiable condition exists | No one             | Reframe it as a question instead of a task            |

Two refinements make the table work in practice:

* **The condition must be observable by Claude.** "Done when CI is green" requires access to CI. If the proof lives in a system the channel isn't connected to, change the condition to one you close yourself.
* **Spell out everything the condition includes.** "Babysit this PR until it merges" can produce a merge the moment approvals arrive, before open review comments are addressed. If the full condition is approvals present, comments resolved, and your final go-ahead, write all three into the task.

For tasks Claude closes itself, ask it to attach proof, such as the source link, the chart, the test output, or the diff. You read the proof, not the transcript.

For long-running work, make getting the deliverable somewhere durable part of the definition. Post the file to the thread, push the branch, or open the draft pull request as it goes. See [what survives between replies](/docs/claude-tag/concepts/how-it-works#what-survives-between-replies).

Calibrate over time. Check everything it produces in a new channel at first, and widen what it closes on its own as its output holds up under review.

### Say which decisions come back to you

Tell Claude which decisions it can make on its own and which ones it must bring to you before acting. If you don't, Claude judges each case itself. It may make a change you wanted to see first, or stop to ask so often that it spends most of the task waiting for your replies.

```text wrap theme={null}
@Claude update the retry logic the way this thread decided. Handle test failures and lint yourself. Come back to me before changing any public interface, and for anything you're not sure is in scope.
```

<Warning>These instructions steer Claude but don't restrict Claude from deciding on its own. A decision that must come back to you needs an enforced control too, such as branch protection for merges.</Warning>

Once you've seen and verified Claude's output over several tasks, you can let it make more decisions without checking in, the same way you widen [what it closes on its own](#give-every-task-a-definition-of-done).

### Specify the output format for anything recurring

A monitor or digest that posts on a schedule posts to the channel repeatedly, so spell out the shape you want each post to take. Say how long each item should be, give it the status legend to use, and tell it what to leave out, so the channel can read every post at a glance.

```text wrap theme={null}
@Claude every 6 hours, check #alerts and post one line per item: 🔴 needs a person, 🟡 watch, 🟢 fine. Skip 🟢 unless something changed.
```

Once a post matches the format you want, you can also point at it directly: "use the format from your 9am post going forward."

### Steer Claude Tag explicitly

Claude adapts to instructions, but it won't guess that you want it to. Tell it how to behave in this channel and ask it to remember. That works in both directions, whether you want more structure or less noise:

```text wrap theme={null}
@Claude remember for this channel: always format reports as a table, and ask before posting anything longer than a screen.
```

```text wrap theme={null}
@Claude remember for this channel: keep replies to three sentences unless someone asks for detail.
```

Verify what stuck by asking what it remembers about the channel. See [What Claude Tag remembers](/docs/claude-tag/users/memory).

## Work in the right place

Where you start a thread determines what Claude can reach, who else can pick the work up, and which standing conventions apply.

### Start a new thread for a new task

Each thread runs its own session, and the session carries the whole conversation into every reply. Keep follow-ups on the same task in the same thread, where Claude already has the context.

Start a new thread for each new task. The fresh session begins with full room for the work, picks up any configuration changes made since the old thread began, and keeps each piece of work reviewable on its own. A thread that accumulates many tasks eventually [grows past what one session can hold](/docs/claude-tag/users/troubleshooting#this-conversation-is-too-long-for-me-to-process).

### Pick the right surface

Channel access belongs to the channel, and DM access belongs to you. A channel can also be yours alone. Create one with just you and Claude in it, and it works the same way a team channel does. The table compares the three surfaces.

|                   | A team channel                             | Your own channel                                                                    | A DM                                                                                                   |
| :---------------- | :----------------------------------------- | :---------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------- |
| Access            | The channel's connections, set by an admin | The channel's connections, set by an admin                                          | Your own claude.ai connectors                                                                          |
| Memory            | Channel memory the team builds             | Channel memory you build                                                            | Outside channel and workspace memory                                                                   |
| Who sees the work | Everyone in the channel                    | You, plus anyone you invite                                                         | You                                                                                                    |
| Billing           | The organization                           | The organization                                                                    | Your seat                                                                                              |
| Best for          | Shared work the team should see and steer  | Your own questions, digests, and follow-ups, kept where a teammate can pick them up | Personal tasks on your own connections, or data that shouldn't run through a shared channel connection |

[Routines](/docs/claude-tag/users/proactivity) belong to a channel too. You set standing work up in the channel where it should post, and it runs with that channel's connections. [Work from your own channel](/docs/claude-tag/users/use-cases/your-own-channel) shows what a channel of your own is good for.

A DM can still answer questions about a public channel when the answer should stay private. Name the channel in the DM, as in `summarize the last week of #product-feedback`. Claude's Slack search covers public channels in this workspace from a DM the same as from a channel, so the DM advantage is privacy of the answer, not broader reach. Workspace search is unavailable in [channels that include guests](/docs/claude-tag/admins/restrict-access#restrict-guest-channels), so ask from a DM or from a channel without guests.

Reading a public channel's full history, rather than what search finds, needs Claude to be a member of that channel. If it says it can't read a public channel, `/invite @Claude` from inside that channel adds it.

A private channel is readable only from inside it. Inviting Claude lets it work in that channel, but Claude can't read the private channel's messages from any other channel or DM. To ask about a private channel, ask in that channel.

Channels in a different workspace and Slack Connect channels stay out of reach.

When more than one surface would work, prefer a channel. Work that happens there compounds, because Claude can draw on it in later threads and teammates can find it, redirect it, or build on it.

If Claude says it can't reach something in a channel, the channel likely wasn't granted that access. See [How agent identity works](/docs/claude-tag/concepts/agent-identity).

### Teach Claude something that sticks

When Claude gets something wrong, or learns something worth keeping, where you put the fix decides who else benefits and whether you can do it yourself.

| You want Claude to know                                                                   | Put it in                                                                                                                      | Who can write it                                                                                                                   | Reaches                                               |
| :---------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------- |
| How this channel should behave: format, tone, when to respond                             | [**Channel memory**](/docs/claude-tag/users/memory) (say it and ask Claude to remember)                                             | Anyone in the channel                                                                                                              | This channel (or workspace, from a public channel)    |
| Conventions and setup for one repository: file layout, PR labels, dependencies to install | **`CLAUDE.md`** at the repo root ([loaded when the repo is](/docs/claude-tag/admins/configure-github#what-loads-from-a-repository)) | Anyone with repo write                                                                                                             | Any session that works in that repo, from any channel |
| Standing rules for this channel that outrank memory                                       | The [**Configure** page](#configure-claude-for-a-channel), in the **Channel instructions** field                               | Channel members, unless an admin has [restricted it](/docs/claude-tag/admins/attach-to-scope#restrict-who-can-set-channel-instructions) | This channel                                          |
| How to use a tool correctly, or follow a specific process, org-wide                       | [**A skill**](/docs/claude-tag/admins/skills-repo) in your org's plugin marketplace                                                 | An organization Owner adds it; anyone can ask Claude to open a PR proposing the change                                             | Every channel under the scope it's attached to        |
| Standing rules across many channels                                                       | [**Custom instructions**](/docs/claude-tag/admins/attach-to-scope#add-custom-instructions) on a workspace or organization scope     | An organization Owner, in the console                                                                                              | Every session in that scope                           |

The first three are yours to write. Skills and wider-scope custom instructions are attached by an Owner, but you can still ask Claude to draft a skill change as a pull request for an admin to review:

```text wrap theme={null}
@Claude that worked. Open a PR to the skills repo so this query pattern is part of the Datadog skill.
```

See [the admin guide to a skills repository](/docs/claude-tag/admins/skills-repo) for what that setup gives you.

A `CLAUDE.md` carries setup as well as conventions. Sessions run in a sandbox with a standard set of preinstalled tools. If the repository needs more, such as a language runtime or a database client, put the install commands in `CLAUDE.md`, and Claude [runs them when its work needs them](/docs/claude-tag/admins/configure-github#install-project-dependencies).

A `CLAUDE.md` is guidance; a required status check is a gate. If a pull request must carry a label or pass a check, make that a repository rule rather than a memory note or a skill. The same goes for review: to require an approval from someone other than the person who asked Claude for the change, see [Require a second approval on Claude's pull requests](/docs/claude-tag/admins/configure-github#require-a-second-approval-on-claude%E2%80%99s-pull-requests).

### Configure Claude for a channel

The **Configure** link in the footer of any Claude reply in a channel opens a page where you tailor how Claude behaves in that channel. You can also send [`@Claude !configure`](/docs/claude-tag/users/commands#get-the-link-to-configure-a-channel) in the channel, and Claude replies with a link to the same page. The page is on claude.ai, so you need to be signed in to your Claude organization to edit it, and an admin can [restrict editing](/docs/claude-tag/admins/attach-to-scope#restrict-who-can-set-channel-instructions) so the page is read-only for members.

The **Respond automatically** toggle on that page controls whether Claude replies in the channel without an @-mention. See [Turn automatic replies on or off](/docs/claude-tag/users/when-claude-responds#turn-automatic-replies-on-or-off) for what the setting does and the other places you can change it.

Use the **Channel instructions** field on that page to write standing guidance Claude reads in every new session in the channel: the channel's purpose, its conventions, the tone replies should take, and anything Claude should do or avoid there. Channel instructions outrank channel memory and sit alongside any instructions an admin has set for the workspace or organization. Save the field and the change applies to new sessions started in the channel.

The page's **Tools and access** tab shows **Connections**, the services Claude can reach from this channel, along with any allowed domains. You can see those lists but not change them on this page. The same tab's **Plugins** card lists the channel's plugins, and you can add plugins there unless an admin has restricted editing to admins. If an Owner has made you a [channel manager](/docs/claude-tag/admins/restrict-access#delegate-channel-setup-to-channel-managers) for the channel, the tab also has access bundle and repository cards you can edit.

## Keep thread count and review rate matched

Claude runs as many threads as you start. Your capacity to review them doesn't scale the same way, because every thread that needs your judgment routes through you serially. Three conventions keep the queue manageable:

* **One channel per project.** Threads and the project's working context stay in one place, and a glance at the channel shows the project's state.
* **Batch your reviews.** Several threads in one sitting costs less than the same number spread across the day, because each return is a context reload.
* **Mark closed threads.** React ✅ to anything you consider done, and tell your digest routine to skip them.

## Related resources

* [Use case library](/docs/claude-tag/users/use-cases): the full setups these habits make reliable
* [What Claude Tag remembers](/docs/claude-tag/users/memory): make corrections stick
