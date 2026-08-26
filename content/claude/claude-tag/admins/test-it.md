> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# See Claude Tag work

> Run Claude Tag's first tasks in a pilot channel before any connection exists. See copy-paste prompts that run on Slack content alone, per-connection checks, and what to do if a step fails.

export const BetaNote = () => <Info>Claude Tag is in public beta. Features and behavior described here may change before general availability.</Info>;

<BetaNote />

<div className="tm-stepbar">
  <a className="tm-stepbar-seg tm-done" href="/docs/docs/claude-tag/admins/pair-workspace">1 · Pair workspace</a>
  <a className="tm-stepbar-seg tm-done" href="/docs/docs/claude-tag/admins/add-connections">2 · Give access</a>
  <a className="tm-stepbar-seg tm-done" href="/docs/docs/claude-tag/admins/configure-github">3 · Connect GitHub</a>
  <a className="tm-stepbar-seg tm-done" href="/docs/docs/claude-tag/admins/set-spend-limit">4 · Spend limit</a>
  <a className="tm-stepbar-seg tm-current" href="/docs/docs/claude-tag/admins/test-it">5 · See it work</a>
</div>

<div className="tm-stepmeta">
  <div className="tm-stepmeta-row"><span className="tm-stepmeta-label">Role you need</span><span>Anyone in the pilot channel can run the prompts; you'll want Owner access handy to fix anything they surface</span></div>
  <div className="tm-stepmeta-row"><span className="tm-stepmeta-label">Before this step</span><span>Workspace paired and a <a href="/docs/docs/claude-tag/admins/set-spend-limit">spend limit</a> set</span></div>
  <div className="tm-stepmeta-row"><span className="tm-stepmeta-label">Do I need this?</span><span><span className="tm-meta-pill tm-meta-pill-req">Required</span>The only way to know the setup holds together before rolling out to more channels.</span></div>
</div>

Claude starts taking work the moment the workspace is paired, with or without connections. This step has two parts: tasks that run on the channel's own content, then a check for each connection you added.

## Run tasks that need no connections

Add Claude to the pilot channel:

```text wrap theme={null}
/invite @Claude
```

Then paste the recap task. It uses only the channel's history, so it confirms the app install, the scope, and the session machinery before any connection is in play.

```text wrap theme={null}
@Claude summarize what this channel decided this week and list any open questions
```

**Passed when:** an "is thinking…" line appears under the message, Claude posts its work in the thread, and delivers a summary.

The recap proves the setup; the prompts below preview the work your channels can hand Claude before anything is connected. Each links to a use case page with the full setup.

Roll up the channel's open requests, the one-off version of [Triage requests](/docs/claude-tag/users/use-cases/triage-requests):

```text wrap theme={null}
@Claude post a summary of this week's requests in this channel: how many, top themes, and anything still unrouted
```

Turn a settled discussion into a document, from [Turn threads into docs and tickets](/docs/claude-tag/users/use-cases/create-artifacts):

```text wrap theme={null}
@Claude turn this thread into a one-page decision doc: what we decided, the options we rejected, and why.
```

Ask for a personalized menu of next tasks, from the [prompt library](/docs/claude-tag/users/prompt-library):

```text wrap theme={null}
@Claude learn what you can about my role from this workspace, then tell me three tasks you could take off my plate this week.
```

## Test the connections you added

If you skipped connections during setup, you're done; come back to this section after you [add a connection](/docs/claude-tag/admins/add-connections). For each connection, run a task in a new thread.

<Steps>
  <Step title="Ask what the channel can reach">
    ```text wrap theme={null}
    @Claude what can you access from this channel?
    ```

    Claude replies with the systems available there.
  </Step>

  <Step title="Ask for data from the connection">
    Pick one connection and ask for something a read-only credential can do, like the latest items from an issue tracker or a single row count from a warehouse.

    ```text wrap theme={null}
    @Claude pull the five most recent items from our issue tracker and post them here
    ```

    For a GitHub repository grant, ask about pull request state:

    ```text wrap theme={null}
    @Claude list the open pull requests in your-org/your-repo and who each one is waiting on
    ```
  </Step>

  <Step title="Check the service's own audit log">
    Confirm the action appears in that service's audit log under the service account you provisioned. That entry proves the credential chain end to end and is the trail your security team reads later.
  </Step>
</Steps>

**Passed when:** the connection responds, and the action shows in that service's audit log under your service account.

## If a test fails

Most first-task failures trace to one of three causes, in order of likelihood:

* **No response at all**: the channel isn't covered by any scope you've configured. Check the workspace appears under **Claude Tag's access** on the **Slack** tab in admin settings.
* **Claude responds but can't reach a service you connected**: Claude isn't told about a connection added after the thread started. Ask it to use the service by name, or start a fresh thread, before investigating anything else.
* **An error message**: the message text names what's missing (a connection, [a host on the allowlist](/docs/claude-tag/admins/add-connections#add-a-domain), or a permission). Fix that piece and try again.

## Related resources

* [Getting started for users](/docs/claude-tag/users/getting-started): what to send the first people in
* [Use case library](/docs/claude-tag/users/use-cases): tasks to hand the pilot channel, with the prompts to paste
* [Prompt library](/docs/claude-tag/users/prompt-library): every prompt on one page, each with why it works
