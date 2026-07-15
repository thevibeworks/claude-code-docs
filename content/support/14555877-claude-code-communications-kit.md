# Claude Code communications kit

This kit covers launch communications, a twenty-message "tips and tricks" drip campaign, and a quick-reference FAQ for the questions you’ll get asked most. Each message links out to a docs page developers can go deeper on.

## How to use this kit

Three parts, in the order you’ll need them. **Part 1** is your launch announcement—one primary message in email and Slack formats, with swap-in variants for an executive-sponsored send and pilot groups. **Part 2** provides twenty drip-campaign messages packaged as ready-to-paste Slack/Teams posts. **Part 3** is a quick-reference FAQ and link directory.

**Treat everything in this kit as draft copy, not finished copy.** Rewrite each message in your org’s voice, swap the example tasks for real bugs and modules from your own codebase, and replace the [bracketed placeholders] before sending. The announcements that actually drive adoption are the ones that read like someone at your company wrote them.

---

## Part 1: Launch communications

One announcement in two formats, plus two optional variants. Pick whichever fits your rollout and rewrite it from there.

### 1.1 Before you send

| **Item**                                                                                                                     | **Why it matters**                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **`#claude-code` channel created** and linked in the message                                                                 | Gives questions one place to land                                                   |
| **Install command tested** on at least one machine in your environment                                                       | Catches proxy/firewall issues before 200 people hit them                            |
| **Security/data-handling link** ready — [Data Usage](https://code.claude.com/docs/en/data-usage) or your internal equivalent | “Where does my code go?” will be the first reply                                    |
| **One concrete first task** chosen — a real bug or file in *your* codebase                                                   | Generic examples don’t convert; “fix the flaky test in `auth_test.go`” does         |
| **A named owner** for the channel for the first 48 hours                                                                     | Unanswered launch-day questions kill momentum                                       |
| **A C-suite sponsor** lined up to send (or co-sign) the announcement                                                         | Exec-sent launches consistently see higher first-week adoption than admin-sent ones |

### 1.2 The announcement

Use this as your standard org-wide rollout message. It covers what Claude Code is, gives a two-minute install, hands readers one concrete task to try, and answers “where does my code go?” before anyone has to ask.

**Email**

- **Subject:** Claude Code is live for [Engineering / your team]Team —As of today you have access to **Claude Code** — an AI coding agent that runs in your terminal, reads your actual codebase, and works through real tasks end-to-end: debugging, refactors, tests, PRs. It’s not autocomplete and it’s not a chat window. It edits files, runs your commands, and asks permission before anything risky.**Get running in two minutes:**```
curl -fsSL https://claude.ai/install.sh | bash
cd <your-repo>
claude
```

Then run `/init` once — Claude reads your project and writes a `CLAUDE.md` with your build commands and conventions, so you stop re-explaining the basics.Then try one of these on the repo you’re already in:

- *“The test in [file] is flaky — figure out why and fix it”*

- *“Walk me through how [module] handles [X]”*

- *“Look at my working diff and tell me what’s risky before I push”*

**Where your code goes.** Claude Code runs in your terminal and talks directly to Anthropic’s API — no third-party servers in the loop. It asks before editing files or running commands. Under our Enterprise agreement, Anthropic does not use your code or prompts to train its models. Details: **[Data Usage](https://code.claude.com/docs/en/data-usage)** · **[Security](https://code.claude.com/docs/en/security)****Where to go with questions:** `#claude-code`. [Owner name] is watching it this week.— [Name]**P.S.** Prefer your editor? There’s a **[VS Code extension](https://code.claude.com/docs/en/vs-code)** and **[JetBrains plugin](https://code.claude.com/docs/en/jetbrains)** — same agent, no terminal.

**Slack / Teams**

- 🚀 **Claude Code is live for [team]**AI coding agent, runs in your terminal, reads your repo, does real work — bugs, refactors, tests, PRs. Asks before it touches anything.```
curl -fsSL https://claude.ai/install.sh | bash
cd <your-repo>
claude
```

**First thing to try** → run `/init`, then: *“the test in [file] is flaky — figure out why and fix it.”*🔒 Runs in your terminal, talks only to Anthropic’s API. Under our Enterprise plan your code and prompts aren’t used to train models. **[Data usage →](https://code.claude.com/docs/en/data-usage)**📚 **[Quickstart](https://code.claude.com/docs/en/quickstart)** · **[VS Code](https://code.claude.com/docs/en/vs-code)** · **[Free 1-hr course](https://anthropic.skilljar.com/claude-code-in-action)**Questions → this thread. [Owner] is on point.

### 1.3 Variant: Executive sponsor send

**Send this from your sponsoring C-suite executive**—CTO, CIO, or SVP Engineering — under their name and from their account. Launches that go out under an exec’s name consistently see higher open rates and faster first-week activation than the same message from an admin or tooling team. It signals a company priority rather than an optional experiment.

This version is deliberately stripped to **one ask**: install it and run it on one real task. No feature tour, no FAQ. The exec’s job is to make the ask land that day; 1.2 and `#claude-code` handle the how.

**Email**

| **Subject:** One thing I’d like every engineer to try this week<br>Team —<br>We’ve turned on **Claude Code** for all of engineering. It’s an AI agent that works directly in your terminal, on your actual codebase — and the early results from teams already using it are strong enough that I want everyone on it this week.<br>I’m asking for ten minutes:

```
curl -fsSL https://claude.ai/install.sh | bash
cd <your-repo>
claude
```

<br>Then hand it one real task — the bug you’ve been putting off, or *“walk me through how [module] works.”*<br>That’s the whole ask. [Owner name] and team are in `#claude-code` for anything you hit along the way.<br>— [Exec Name]
[Title]<br> |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

**Slack / Teams**

| 📣 **From [Exec Name]: one thing to try this week**<br>We’ve turned on **Claude Code** for all of engineering. Early results are strong enough that I’m asking everyone to give it ten minutes on real work this week.<br>

```
curl -fsSL https://claude.ai/install.sh | bash
cd <your-repo>
claude
```

<br>→ hand it one real task.<br>That’s it. Questions → `#claude-code`.<br> |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### 1.4 Variant: Pilot / early-access group

Use for a phased rollout. Send to the pilot cohort only.

| **Subject:** You’re in the Claude Code pilot<br>[Name / team] —<br>You’re in the first wave of Claude Code at [company]. We picked this group because you’ll put it on real problems and tell us the truth about it.<br>**The ask:** use it on at least one real task this week, then drop a note in `#claude-code-pilot` — what worked, what was annoying, what surprised you. That feedback decides how we roll it out to everyone else.<br>*[Continue with “Get running in two minutes” from 1.2]*<br>**One extra thing for pilots:** on your first multi-file change, hit **Shift+Tab** until you see “plan.” Claude will lay out exactly what it intends to do before it touches a file — it’s the fastest way to calibrate how much to trust it.<br> |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### 1.5 Champion recruitment DM

After launch, DM the two or three people who are most active in `#claude-code`.

| Hey [name] — your `#claude-code` posts are doing more for adoption than my announcement did. A couple of people told me your [thread / screenshot] was why they actually tried it.<br>Want to make that semi-official? Low lift — mostly keep posting what you’re posting, plus first crack at new features and a direct line to the Anthropic team. I can share a short playbook for that if you’re in.<br> |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

---

## Part 2: Tips and tricks campaign

Twenty ready-to-paste Slack/Teams messages designed to drive feature activation after launch. Each follows the same pattern: a hook, the payoff, a **“try it now”** prompt, and a docs link. Drip them one or two a week in `#claude-code`, or pick the five that match your team’s gaps. They stand alone—no required order.

Copy the message body from each table below directly into Slack or Teams. Replace [bracketed placeholders] before sending.

### 2.1 Getting started

**Message 1 — Choosing the right model**

| 🎯 **Tip: Match the model to the moment**<br>Using Opus to fix a typo? Burning compute. Using Haiku for a 12-file refactor? Asking for a re-do.<br>Claude Code runs on the same models as the Claude app—and you can switch mid-session. **Sonnet** is the workhorse default for everyday feature work, bugs, tests, and reviews. Reach for **Opus** on large refactors, gnarly debugging, or anything high-stakes. Drop to **Haiku** for quick questions, formatting, and mechanical edits where speed wins.<br>**Try it now:** type `/model` in your session and pick Sonnet if you haven’t already—it’s the right default for most tasks.<br>📖 **[Model configuration](https://code.claude.com/docs/en/model-config)**<br> |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

*Quick reference:*

| **Model**                      | **Best for**                                                                          |
| ------------------------------ | ------------------------------------------------------------------------------------- |
| Opus                           | Large-scale refactors, complex debugging, architecture decisions, high-stakes changes |
| Sonnet *(recommended default)* | Everyday feature work, bug fixes, tests, documentation, code review                   |
| Haiku                          | Quick questions, formatting, mechanical edits, rapid iteration                        |

**Message 2 — Quick wins to try first**

| 🚀 **Tip: Three things to try in your first 10 minutes**<br>Installed Claude Code but not sure what to actually ask it? Start with the stuff that’s been bugging you all week.<br>     Fix something annoying — *“the test in [file] is flaky — figure out why”*<br>Get oriented in code you didn’t write — *“walk me through how [module] works”*<br>Sanity-check before you push — *“look at my working diff and tell me what looks risky”*<br>None of these need setup. Just `cd` into your repo and run `claude`.<br>**Try it now:** pick the bug you’ve been avoiding and paste the error message in. That’s it.<br>📖 **[Quickstart](https://code.claude.com/docs/en/quickstart)**<br> |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

### 2.2 Project memory

**Message 3 — /init and CLAUDE.md**

| 📁 **Tip: Stop re-explaining your repo every session**<br>Telling Claude “we use pnpm, not npm” for the fifth time? There’s a one-time fix for that.<br>Run `/init` once per repo. Claude reads your project structure and writes a `CLAUDE.md` file — your build commands, architecture, conventions. Every future session in that repo starts from this file automatically. Keep it under two screens. It’s a cheat sheet, not documentation.<br>**Try it now:** open your main repo, run `claude`, type `/init`. Thirty seconds, pays off every session after.<br>📖 **[CLAUDE.md and project memory](https://code.claude.com/docs/en/memory)**<br> |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

**Message 4 — @-references**

| 📎 **Tip: Stop pasting file contents into the chat**<br>Copying 200 lines of a component into your prompt so Claude can “see” it? You don’t have to.<br>Type `@` then a file path — Claude pulls the file directly into context. Works for whole directories too.<br>*> the styles in @src/components/Button.tsx look off, check against @docs/design-system.md*<br>**Try it now:** type `@` then Tab — autocomplete shows you every file in reach.<br>📖 **[Referencing files](https://code.claude.com/docs/en/common-workflows#reference-files-and-directories)**<br> |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

**Message 5 — Memory — “remember that…”**

| 🧠 **Tip: Teach Claude your team’s quirks once**<br>Claude just suggested deploying from `main` — but you deploy from `release`. Don’t correct it again next week.<br>When Claude misses something it should’ve known about your project, just say it out loud: *“remember that we deploy from the release branch, not main.”* Claude saves the fact to auto memory and starts every future session knowing it.<br>**Try it now:** next time you correct Claude on a project detail, prefix it with *“remember that…”* instead.<br>📖 **[Memory and CLAUDE.md](https://code.claude.com/docs/en/memory)**<br> |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### 2.3 Control and safety

**Message 6 — Permission modes**

| 🛡️ **Tip: One keystroke between “look but don’t touch” and “just do it”**<br>Sometimes you want Claude to ask before every edit. Sometimes you just want it to ship. You shouldn’t have to pick one forever.<br>**Shift+Tab** cycles through how much leash Claude gets — **default** (asks before risky stuff), **acceptEdits** (file edits and common filesystem commands like mkdir/mv/cp flow through; still checks before other shell commands), **plan** (proposes, you approve before anything changes). Plan mode is the trust-builder—start there for anything touching multiple files.<br>**Try it now:** on your next refactor, hit Shift+Tab until you see “plan”, then describe the change. You’ll get a full proposal before a single file moves.<br>📖 **[Permission modes](https://code.claude.com/docs/en/permissions)**<br> |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

*Quick reference (the three you’ll use most — see **[docs](https://code.claude.com/docs/en/permissions)** for the full list):*

| **plan**                                             | **default**                                | **acceptEdits**                                                                                                    |
| ---------------------------------------------------- | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| Claude proposes, you approve before anything changes | Claude asks before risky edits or commands | File edits and common filesystem Bash commands go through without asking; still checks before other shell commands |

**Message 7 — Checkpointing and /rewind**

| ⏪ **Tip: There’s an undo button for the whole conversation**<br>Claude went down the wrong path three turns ago and now you’re untangling spaghetti? You don’t have to fix forward.<br>`/rewind` rolls back to an earlier point in the conversation — including the file changes Claude made along the way. Checkpointing is automatic; you don’t set anything up.<br>**Try it now:** hit **Esc** twice to open the rewind menu, or type `/rewind`. Pick the point before things went sideways.<br>📖 **[Checkpointing](https://code.claude.com/docs/en/checkpointing)**<br> |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### 2.4 Connect Your Tools

**Message 8 — MCP connectors**

| 🔌 **Tip: Let Claude read your issue tracker so you don’t have to paste tickets**<br>Copy-pasting Jira tickets into the terminal feels like a step backward. It is.<br>One config file (`.mcp.json` at your project root) wires Claude into GitHub, Jira, Linear, or whatever tracker you use. Then *“what’s the top-priority issue assigned to me?”* and *“go ahead and fix it”* happen in the same conversation. Wire up your issue tracker first — it’s the highest-leverage connector.<br>**Try it now:** ask Claude *“set up an MCP connector for [GitHub/Jira/Linear] in this repo”* — it’ll write the config for you.<br>📖 **[MCP connectors](https://code.claude.com/docs/en/mcp)**<br> |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

**Message 9 — IDE integrations**

| 💻 **Tip: You don’t have to leave your editor**<br>Terminal not your thing? The same agent runs inside VS Code and JetBrains.<br>VS Code extension and JetBrains plugin available now — same model, same features, embedded in your editor. No alt-tabbing to the terminal.<br>**Try it now:** search “Claude Code” in your editor’s extension marketplace and hit install. You’ll be running in under a minute.<br>📖 **[VS Code extension](https://code.claude.com/docs/en/vs-code)**<br> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### 2.5 Automate Your Workflows

**Message 10 — Slash commands and skills**

| ⚡ **Tip: Turn that prompt you keep retyping into a command**<br>Typed “summarize what I worked on today from git log, format it for standup” three times this week? That’s a slash command waiting to happen.<br>A `SKILL.md` file in `.claude/skills/<name>/` becomes a reusable prompt—type /name to run it. The rule of thumb: make one the second time you type a multi-step prompt you’ve typed before. Easiest path? Ask Claude to make it for you.<br>**Try it now:** type *“make me a /standup skill that summarizes what I worked on today from git log”* — then run `/standup` tomorrow morning.<br>📖 **[Skills](https://code.claude.com/docs/en/skills)**<br> |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

**Message 11 — Hooks**

| 🔔 **Tip: Get pinged when your refactor finishes — go get coffee**<br>Sitting at your desk watching Claude work through a long task? You’ve got better things to do for those eight minutes.<br>Hooks are shell commands that fire on Claude Code events. A `Stop` hook that sends a desktop notification means you can kick off a long refactor, walk away, and get pinged the moment it’s done.<br>**Try it now:** ask Claude *“add a Stop hook that sends a desktop notification when you finish”* — it’ll write the script and wire it up.<br>📖 **[Hooks guide](https://code.claude.com/docs/en/hooks-guide)**<br> |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

**Message 12 — Subagents**

| 🤖 **Tip: Big tasks get parallelized**<br>Ever notice some tasks finish faster than the math says they should? That’s subagents.<br>For large jobs — multi-file refactors, broad codebase searches — Claude can spin up specialized subagents that work in parallel without cluttering your main conversation. It’ll often do this on its own, and you can also define your own custom subagents for repeat workflows.<br>**Try it now:** on your next big refactor, just describe the whole job at once instead of file-by-file: *“update every API call in src/ to use the new client”*. Watch it parallelize.<br>📖 **[Subagents](https://code.claude.com/docs/en/sub-agents)**<br> |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

### 2.6 Day-to-day dev

**Message 13 — Effort levels**

| 🧩 **Tip: Give Claude permission to actually think about the hard ones**<br>Got a bug that’s defeated you twice? Don’t ask for a fast answer — ask for a careful one.<br>`/effort max` pushes reasoning depth to the top of the scale. Claude takes longer, explores more branches, and the answer is more likely to hold up under scrutiny. Team and Enterprise plans already default to high, so max is the step up. Save it for the problems where being wrong costs you an afternoon.<br>**Try it now:** type `/effort max ` before describing your hardest open bug. Then go refill your water while it works.<br>📖 **[Effort levels](https://code.claude.com/docs/en/model-config#adjust-effort-level)**<br> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

**Message 14 — Screenshots and images**

| 📸 **Tip: Stop describing the error dialog — just show it**<br>Typing out “there’s a red box that says something about a null reference and it’s pointing at line 47-ish”? Screenshot it.<br>Drag a screenshot straight into the terminal and Claude sees it — error dialogs, UI mockups, whiteboard photos, Figma exports. **Ctrl+V** pastes from clipboard (use Ctrl+V on macOS too — not Cmd+V).<br>**Try it now:** next time something visual breaks, screenshot it and paste it right into the prompt. Then just type *“what’s wrong here?”*<br>📖 **[Working with images](https://code.claude.com/docs/en/common-workflows#work-with-images)**<br> |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

**Message 15 — Git workflows**

| 🌿 **Tip: Hand off the whole git ceremony**<br>The fix took 5 minutes. The commit message, branch, and PR description took 15. That ratio is wrong.<br>Claude handles the full git flow — commits with conventional messages, branches, PRs with proper summaries. One ask: *“fix the off-by-one, commit with a conventional commit message, and open a PR.”* Reviewing someone else’s work? Paste the PR URL and ask Claude to walk you through the diff.<br>**Try it now:** after your next fix, instead of switching to your git client, just type *“commit this with a good message and open a PR”*.<br>📖 **[Creating pull requests](https://code.claude.com/docs/en/common-workflows#create-pull-requests)**<br> |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

**Message 16 — Background tasks**

| ⏱️ **Tip: Don’t block on the test suite — keep talking**<br>Full test suite takes 4 minutes? That’s 4 minutes you could spend planning the next change.<br>Long-running commands — builds, test suites, dev servers — can run in the background while you keep working with Claude. You just have to ask for it explicitly.<br>**Try it now:** instead of *“run the tests”*, say *“run the tests in the background”*. Then keep going: *“while that runs, walk me through the auth module.”*<br>📖 **[Background commands](https://code.claude.com/docs/en/interactive-mode#background-bash-commands)**<br> |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### 2.7 Share and scale

**Message 17 — Plugins**

| 📦 **Tip: Someone probably already built that skill**<br>About to spend an hour building a `/deploy` command? Check if it already exists.<br>Skills get bundled and shared as plugins. `/plugin` browses what’s available and installs in one step. Five minutes of browsing can save an hour of building.<br>**Try it now:** type `/plugin` right now and scroll through. You’ll find at least one thing you didn’t know you wanted.<br>📖 **[Plugins](https://code.claude.com/docs/en/plugins)**<br> |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

**Message 18 — Keyboard shortcuts**

| ⌨️ **Tip: Five shortcuts that pay rent every day**<br>If you only learn five things, make it these — they each save a click dozens of times a day.<br>**Shift+Tab** → cycle permission modes · **@** then Tab → autocomplete file paths · **/** then pause → see every command · **Ctrl+C** → stop mid-task · **Esc** twice → open rewind menu<br>**Try it now:** right now, hit `/` and pause. That’s your full command list. Anything you didn’t know about?<br>📖 **[Interactive mode and shortcuts](https://code.claude.com/docs/en/interactive-mode)**<br> |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### 2.8 Security and admin

**Message 19 — Security architecture**

| 🔐 **Tip: The answer to “is this safe?” — for the next time you’re asked**<br>Someone on your team is going to ask “wait, where does my code go?” Here’s the short version you can paste.<br>Permission-first by design. Every file edit, shell command, and external call is gated by your approval. The CLI runs in your terminal and talks directly to Anthropic’s API — no third-party servers — with optional OS-level sandboxing for shell commands. Under our Enterprise plan, Anthropic does not use your code or prompts to train its models.<br>**Try it now:** save these two links for the next time the question comes up — they answer most security-review questions.<br>📖 **[Security and permissions](https://code.claude.com/docs/en/security)** · **[Data usage](https://code.claude.com/docs/en/data-usage)**<br> |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

**Message 20 — Best practices**

| ✅ **Tip: The 4 habits that separate “tried it once” from “use it daily”**<br>Most people who bounce off Claude Code skipped one of these. Most people who stick did all four in week one.<br>     Start in plan mode for anything touching multiple files.<br>Run `/init` early — context compounds.<br>Review diffs before committing — Claude can be confidently wrong.<br>Verify changes that touch critical paths; treat it like a sharp junior, not an oracle.<br>**Try it now:** if you’ve only done one or two of these, pick the one you’re missing and do it on your next task. Post what changed in `#claude-code`.<br>📖 **[Best practices](https://code.claude.com/docs/en/best-practices)**<br> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

---

## Part 3: Quick reference

### 3.1 FAQ responses

One-line Slack replies for the questions you’ll get asked most.

| **Question**                             | **Response**                                                                                                                                                                                                                                            |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| “Does it work in VS Code?”               | Yes — VS Code extension and JetBrains plugin. Same features, embedded in your editor. **[Docs →](https://code.claude.com/docs/en/vs-code)**                                                                                                             |
| “Do I have to configure anything first?” | No — install, then `claude` in any repo. Run `/init` once and you’re set. **[Quickstart →](https://code.claude.com/docs/en/quickstart)**                                                                                                                |
| “Where does my code go?”                 | The CLI runs in your terminal and sends context to Anthropic’s API for inference — no third-party servers. Under our Enterprise plan, your code and prompts aren’t used to train models. **[Data Usage →](https://code.claude.com/docs/en/data-usage)** |
| “Can it see my whole repo?”              | It reads what you give it access to. File reads inside your working directory don’t prompt; permission prompts gate edits, shell commands, and anything outside that directory. **[Permissions →](https://code.claude.com/docs/en/permissions)**        |
| “How is this different from Copilot?”    | Copilot autocompletes lines. Claude Code is an agent — reads files, runs commands, makes multi-file edits. **[Overview →](https://code.claude.com/docs/en/overview)**                                                                                   |
| “What should I try first?”               | A bug you’ve been putting off because it’s tedious. *“the test in [file] is flaky — figure out why.”* **[Quickstart →](https://code.claude.com/docs/en/quickstart)**                                                                                    |

### 3.2 Prompt templates

| **Task**             | **Prompt**                                                                    |
| -------------------- | ----------------------------------------------------------------------------- |
| Fix a bug            | *“the tests in [file] are failing — figure out why and fix it”*               |
| Understand code      | *“walk me through how [module] works, then tell me where the entry point is”* |
| Safe refactor        | *“refactor [module] to [goal] — use plan mode so I can review first”*         |
| Write tests          | *“write tests for [file] that cover the edge cases around [scenario]”*        |
| Review before commit | *“look at my working diff and tell me what looks risky”*                      |
| Open a PR            | *“fix [issue], write a conventional commit, and open a PR with a summary”*    |
| Make a skill         | *“make me a /ship skill that runs tests and lint before commit”*              |
| Debug a stack trace  | *“here’s the stack trace — find the root cause, don’t just paper over it”*    |

---

## Appendix: Verified links reference

| **Resource**                        | **URL**                                                                                                  |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Claude Code docs (home)             | **[code.claude.com/docs](https://code.claude.com/docs)**                                                 |
| Quickstart & install                | **[code.claude.com/docs/en/quickstart](https://code.claude.com/docs/en/quickstart)**                     |
| Claude Code in Action (free course) | **[anthropic.skilljar.com/claude-code-in-action](https://anthropic.skilljar.com/claude-code-in-action)** |
| VS Code extension                   | **[code.claude.com/docs/en/vs-code](https://code.claude.com/docs/en/vs-code)**                           |
| JetBrains plugin                    | **[code.claude.com/docs/en/jetbrains](https://code.claude.com/docs/en/jetbrains)**                       |
| CLAUDE.md & memory                  | **[code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory)**                             |
| Permission modes                    | **[code.claude.com/docs/en/permission-modes](https://code.claude.com/docs/en/permission-modes)**         |
| MCP connectors                      | **[code.claude.com/docs/en/mcp](https://code.claude.com/docs/en/mcp)**                                   |
| Skills                              | **[code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills)**                             |
| Hooks                               | **[code.claude.com/docs/en/hooks-guide](https://code.claude.com/docs/en/hooks-guide)**                   |
| Subagents                           | **[code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents)**                     |
| Plugins                             | **[code.claude.com/docs/en/plugins](https://code.claude.com/docs/en/plugins)**                           |
| Checkpointing                       | **[code.claude.com/docs/en/checkpointing](https://code.claude.com/docs/en/checkpointing)**               |
| Model configuration                 | **[code.claude.com/docs/en/model-config](https://code.claude.com/docs/en/model-config)**                 |
| Common workflows                    | **[code.claude.com/docs/en/common-workflows](https://code.claude.com/docs/en/common-workflows)**         |
| Interactive mode & shortcuts        | **[code.claude.com/docs/en/interactive-mode](https://code.claude.com/docs/en/interactive-mode)**         |
| Security                            | **[code.claude.com/docs/en/security](https://code.claude.com/docs/en/security)**                         |
| Data usage                          | **[code.claude.com/docs/en/data-usage](https://code.claude.com/docs/en/data-usage)**                     |
| Best practices                      | **[code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices)**             |

Claude Code ships frequently—verify version-specific details against **[code.claude.com/docs](https://code.claude.com/docs)** before distributing internally.