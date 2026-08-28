> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Work with your GitHub repositories

> Claude Tag works with your GitHub repositories from Slack: answer questions in-thread, subscribe to pull requests, and hand back chores as draft pull requests.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

## How GitHub prompts work

This page is for engineers and anyone else with questions a repository can answer. Claude works with the GitHub repositories an admin granted for the channel. It reads the code to answer questions, watches pull requests you name, and hands back changes as draft pull requests.

Each prompt below is a Slack message. Paste it in the channel or thread where the question lives. Claude clones the repository into an isolated workspace, posts progress in that thread, and delivers the result there too.

Name the repository in the first message. A session starts with no repositories checked out and clones one when the request names it. Anything Claude opens on GitHub is authored by the Claude GitHub App, so it appears in your review queue like any other pull request.

<Note>An admin [grants a repository to the channels that need it](/docs/claude-tag/admins/attach-to-scope), and questions about the code work only in those channels. By default anyone in those channels can ask, and an admin can [restrict who can use Claude](/docs/claude-tag/admins/restrict-access#control-who-can-invoke-claude-tag).</Note>

## Check the channel's connections

Check that the channel has the connection below. Ask `@Claude what can you access from this channel?` and the reply also lists which repositories the channel can reach. An admin can [add a connection](/docs/claude-tag/admins/add-connections) the channel is missing.

| Connection | Examples | Why it matters here                                                |
| :--------- | :------- | :----------------------------------------------------------------- |
| Code       | GitHub   | Required. Reads granted repositories and opens draft pull requests |

The GitHub connection is what lets Claude clone a repository. For GitLab, an admin [connects it with an access token](/docs/claude-tag/admins/connections/gitlab), and Claude reads projects, manages issues, and comments on merge requests through the GitLab API.

If Claude replies that a repository isn't configured, the repository wasn't granted for this channel. An admin can [verify GitHub access](/docs/claude-tag/admins/configure-github#verify-github-access). After the grant changes, start a fresh thread and name the repository in the first message.

## Prompts to paste

### Answer a repository question without interrupting the author

A question about how the code behaves arrives in the channel, and the person who wrote it is away. Claude clones the repository, reads the code, and posts the answer in the thread.

```text wrap theme={null}
@Claude in acme/data-pipeline, how does the export retry logic decide when to give up? Name the files involved.
```

Asking for the files involved attaches proof to the answer, so anyone in the thread can open them and check.

Investigation questions work the same way: when a behavior last changed, in which commit, and who to ask about it.

```text wrap theme={null}
@Claude in acme/data-pipeline, did the export retry behavior change recently? Find the commit that changed it, when it landed, and who wrote it.
```

The clone carries the repository's full commit history, so history questions get answered from the same checkout as code questions. If the repository keeps a `CODEOWNERS` file, questions about who owns a path read from it too.

### Stop refreshing a pull request

Your work is blocked on a pull request a teammate opened, and the only way to know it moved is to keep checking the page. Claude subscribes to the pull request and posts in the thread when it updates, whether Claude opened it or a person did.

```text wrap theme={null}
@Claude subscribe to PR #519 in acme/data-pipeline, the schema migration. When CI finishes or a review arrives, post here, and tag me if anything failed.
```

Claude reads the pull request's workflow runs and logs, so the post says whether checks passed or failed. To list or cancel a subscription later, see [Manage standing work](/docs/claude-tag/users/proactivity#manage-standing-work). Because the prompt asks for a tag only on failure, passing runs post to the thread without notifying you.

### Hand off the change you keep postponing

Small, well-understood changes sit on the list for weeks because they never become urgent. Docs drift from the code, a config key keeps its old name, a dependency stays a version behind. Describe one in a message, and it comes back as a draft pull request linked to the thread.

```text wrap theme={null}
@Claude in acme/data-pipeline, the CSV export docs still describe the old date format. Update them to match the code and open a draft PR. Done means CI is green and the PR links back here.
```

Writing a [definition of done](/docs/claude-tag/users/good-habits#give-every-task-a-definition-of-done) into the task lets the session check its own work. The change comes back as a draft pull request in your review queue, opened under Claude's own GitHub identity.

### Triage a suspected bug where the report arrives

A report arrives in the feedback channel, and nobody knows yet whether it's a bug. Claude investigates the repository and either explains the behavior or opens a draft fix.

```text wrap theme={null}
@Claude a user reports that exports drop rows with empty dates. In acme/data-pipeline, is that a bug or intended behavior? If it's a bug, open a draft PR with a fix; if it's intended, explain here what the code does.
```

For the full arc from a bug report to green CI, including a standing watch that triages a bug channel, see [Fix bugs](/docs/claude-tag/users/use-cases/fix-bugs). Because the prompt asks for either a fix or an explanation, the thread gets an answer even when the behavior turns out to be intended.

### Hand off a change and follow its pull request in one message

You can combine the earlier recipes in a single message. The prompt below hands off a change, sets the definition of done, and asks Claude to subscribe to the pull request it opens.

```text wrap theme={null}
@Claude in acme/data-pipeline, the deprecation warnings in the export module still reference the removed legacy-dates option. Remove the stale warnings and open a draft PR. Done means CI is green and the PR links back here. Then subscribe to your own PR, and when CI finishes or a review arrives, post here and tag me if anything failed.
```

Claude opens the draft and then follows it the way it follows any pull request, because subscriptions work the same whether Claude opened the pull request or a person did. CI results and review activity arrive as posts in the thread, so you open GitHub only to review the finished change.

### Act on review comments and CI failures

Claude can watch a pull request and address CI failures, review comments, and change requests as they come in, until the pull request is ready to merge. You approve and merge.

```text wrap theme={null}
@Claude watch your PR #562 in acme/data-pipeline. When CI fails, fix it and push. When a review comment arrives, address it and push. Post here after each push saying what changed and why. Done means CI is green and every comment is addressed. I do the approving and merging.
```

<Warning>If you don't want Claude to approve or merge pull requests, turn on branch protection rules that restrict who can merge. These rules apply to Claude too. Also write "I do the approving and merging" into the task, as the example does. The task wording states your intent, but it's an instruction Claude can lose track of, not a control. The branch protection rule is what enforces it.</Warning>

Ask for a post after each push so you can follow the pull request from the thread instead of opening GitHub.

## Repository instructions in CLAUDE.md

If your repository has conventions Claude should follow, such as file layout, pull request labels, or dependencies to install, add them to a `CLAUDE.md` file at the repository root. When Claude clones the repository into a session, its `CLAUDE.md`, `.claude/CLAUDE.md`, and `.claude/rules/*.md` files load on the next turn, so the guidance arrives without further prompting. Skills in the repository's `.claude/skills/` folder also load, so Claude can use them in sessions that have the repository. Anyone with repository write access can edit these files, and they reach every session that works in that repository, from any channel.

Each session runs in an isolated sandbox with a standard set of preinstalled tools. Two threads are two sessions with two separate sandboxes. If the repository needs a tool that the standard set doesn't include, such as a language runtime or a database client, add the install commands to `CLAUDE.md`, and Claude [runs them when its work needs them](/docs/claude-tag/admins/configure-github#install-project-dependencies).

<Note>A `CLAUDE.md` is guidance rather than a gate. If a pull request must carry a label or pass a check, make that a repository rule. For where `CLAUDE.md` sits among channel memory, channel instructions, and skills, see [Teach Claude something that sticks](/docs/claude-tag/users/good-habits#teach-claude-something-that-sticks).</Note>

## Related resources

<CardGroup cols={2}>
  <Card title="Fix bugs" href="/docs/claude-tag/users/use-cases/fix-bugs" horizontal arrow>
    The full arc from a bug report to a draft pull request and green CI
  </Card>

  <Card title="Set up routines" href="/docs/claude-tag/users/proactivity" horizontal arrow>
    Pull request subscriptions and other standing work
  </Card>
</CardGroup>
