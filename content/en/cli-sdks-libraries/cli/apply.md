---
title: Manage resources as code with ant apply
url: https://platform.claude.com/docs/en/cli-sdks-libraries/cli/apply
description: Declare agents, environments, skills, memory stores, and deployments as files in your repository and keep the API's resources in sync with them using ant apply.
---

`ant apply` creates and updates Claude API resources from files: agents, environments, skills, memory stores, and deployments. They live in your repository and change through the same review as your code. You describe each resource in a file, run `ant apply`, and approve the plan it shows. Then you commit the `claude-lock.json` it writes, so the next run updates the same resources instead of creating new ones.

To install and authenticate the CLI, see the [CLI quickstart](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/quickstart). `ant apply` requires CLI version 1.30.0 or later.

## Apply your first agent

Write the agent as a Markdown file under `agents/` and apply it:

<MultiFileExample language="cli" label="CLI">
  ```bash CLI
  ant apply agents/summarizer.md
  ```

  <File filename="agents/summarizer.md">
    ```markdown
    ---
    name: Summarizer
    model: claude-opus-5
    tools:
      - type: agent_toolset_20260401
    ---

    You are a helpful assistant that writes concise summaries.
    ```
  </File>
</MultiFileExample>

The frontmatter holds the agent's configuration (the fields from [Define your agent](https://platform.claude.com/docs/en/managed-agents/agent-setup)) and the body is its system prompt. `ant apply` [infers](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/apply#kind-inference) that the file is an agent from its path, here the `agents/` directory.

In an interactive terminal, `ant apply` prints the plan and waits for your approval:

```text Output wrap
First apply  ./claude-lock.json does not exist yet and will be created

Resources will be created with
  credentials   API key (--api-key / ANTHROPIC_API_KEY)
  host          api.anthropic.com
  organization  1b0c2a4d-6c1f-4f0e-9a57-2e8d1c3b4a5f
  workspace     wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ

Preview  ./claude-lock.json (new)

± Name                    Plan
+ ./agents/summarizer.md  create

Resources  + 1 to create

Apply these changes? (y)es / (n)o / (d)etails y

Apply  ./claude-lock.json

± Name                    Status
+ ./agents/summarizer.md  created    agent_011CYm1BLqPXpQRk5khsSXrs

Resources  + 1 created

State written to ./claude-lock.json
```

Answer `d` to see details first: the fields of each new resource, or a field-by-field diff of each update. `--dry-run` prints that detailed plan and exits without changing anything.

To change the agent, edit the file and run `ant apply` again. The plan then shows an update instead of a create.

## Commit claude-lock.json

The first `ant apply` writes `claude-lock.json`, the lockfile, in the directory you run it from, so run it from the repository root. It records the ID of the resource each file created and the organization and workspace the resources live in:

```json claude-lock.json
{
  "version": 1,
  "origin": {
    "base_url": "https://api.anthropic.com",
    "organization_id": "1b0c2a4d-6c1f-4f0e-9a57-2e8d1c3b4a5f",
    "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
  },
  "resources": {
    "./agents/summarizer.md": {
      "kind": "agent",
      "id": "agent_011CYm1BLqPXpQRk5khsSXrs",
      "version": "1",
      "hash": "d23251c8d99b3613a64f3f8d87f5fad4",
      "remote_hash": "1b771bee5bdbf600a5ad972fdac32d94"
    }
  }
}
```

Commit it with your files. It's how the next run, on your machine or in CI, finds these resources instead of creating them again, and it's where you read an agent's ID to [start a session](https://platform.claude.com/docs/en/managed-agents/sessions). The two hashes fingerprint what was last sent and what the API returned. That's how a later run notices an edited file, or a resource changed outside these files.

## Grow it into a project

You can declaratively define the other resources as files as well. A file holds the request body you would send to that kind's create endpoint:

* An [environment](https://platform.claude.com/docs/en/managed-agents/environments) is a YAML file in `environments/`.
* A [memory store](https://platform.claude.com/docs/en/managed-agents/memory) is a YAML file in `memory_stores/`.
* A [deployment](https://platform.claude.com/docs/en/managed-agents/scheduled-deployments) is a Markdown file in `deployments/`: the frontmatter is the request body and the prose becomes the message that starts each session.
* A [skill](https://platform.claude.com/docs/en/managed-agents/skills) is a directory with a `SKILL.md` at its root, conventionally under `skills/`, uploaded as one bundle.

Any resource except a skill can be written as YAML, JSON, or Markdown. In Markdown, the frontmatter is the body and the prose fills the kind's text field: an agent's `system`, an environment's or memory store's `description`, a deployment's first message.

Resources refer to each other by path. Wherever the API expects another resource's ID, write the relative path to that resource's file instead. In this project, the reviewer agent lists `../skills/pr-summary` under `skills`, the lead agent lists `./reviewer.md` in its roster, and the deployment names its agent, environment, and memory store by path. `ant apply` creates them in dependency order and fills in the real IDs. Apply the whole directory:

<MultiFileExample language="cli" label="CLI">
  ```bash CLI
  ant apply .
  ```

  <File filename="agents/reviewer.md">
    ```markdown
    ---
    name: Code reviewer
    model: claude-opus-5
    tools:
      - type: agent_toolset_20260401
    skills:
      - ../skills/pr-summary
    ---

    You review pull requests for correctness, security, and readability.
    ```
  </File>

  <File filename="agents/lead.md">
    ```markdown
    ---
    name: Engineering lead
    model: claude-opus-5
    multiagent:
      type: coordinator
      agents:
        - ./reviewer.md
    ---

    You coordinate engineering work. Delegate code review to the reviewer.
    ```
  </File>

  <File filename="skills/pr-summary/SKILL.md">
    ```markdown
    ---
    name: pr-summary
    description: Summarize a pull request's changes and risks in the team's review format.
    ---

    # PR summary

    List what changed, why, and anything a reviewer should look at closely, in three short sections.
    ```
  </File>

  <File filename="environments/cloud.yaml">
    ```yaml
    name: review-env
    description: Cloud container with unrestricted networking for review sessions.
    config:
      type: cloud
      networking:
        type: unrestricted
    ```
  </File>

  <File filename="memory_stores/review-notes.yaml">
    ```yaml
    name: Review notes
    description: Recurring issues and house-style decisions the reviewer has recorded between runs.
    ```
  </File>

  <File filename="deployments/nightly.md">
    ```markdown
    ---
    name: Nightly review
    agent: ../agents/reviewer.md # the API's agent field: sent as {type: agent, id, version}
    environment_id: ../environments/cloud.yaml # sent as the environment's ID
    resources:
      - path: ../memory_stores/review-notes.yaml
        access: read_write
    schedule:
      type: cron
      expression: "0 3 * * *"
      timezone: America/Los_Angeles
    ---

    Review any open pull requests. Start with the oldest.
    ```
  </File>
</MultiFileExample>

`claude-lock.json` then has an entry for every file in the project.

Relative paths are how these files point at each other. `ant apply` pins agent and skill references to the version it just applied, so editing `reviewer.md` or the skill updates everything that references them in the same run. A path also works inside an object, as in the deployment's `resources` entry, where the other keys such as `access` are kept.

To point at a resource these files don't manage, write its ID (`agent_...`, `skill_...`) instead. Anything else, such as `{type: anthropic, skill_id: xlsx}`, is sent to the API as written. A skill reference can also be a GitHub URL of the form `https://github.com/<owner>/<repo>/tree/<branch>/<dir>`, for example a directory of Anthropic's open-source [skills repository](https://github.com/anthropics/skills): `ant apply` downloads and uploads that directory, pinned to the resolved commit until you run with `--upgrade` (set `GITHUB_TOKEN` for a private repository).

### How ant apply infers a file's kind

When `ant apply` walks a directory, it determines each file's kind from the first of these that matches:

1. A top-level `type` field in the file.
2. The directory the file is directly in: `agents/`, `environments/`, `memory_stores/`, or `deployments/`.
3. A file name that starts with the kind, such as `environment_staging.md`.

It skips files that match none of these, such as READMEs and CI configuration, unless you name them on the command line. A named Markdown file that matches none is treated as an agent, and a named YAML or JSON file that matches none is an error.

## Edit and reapply

Running `ant apply` with no arguments reconciles every file the lockfile tracks. At a terminal, it also lists untracked resource files under the lockfile's directory and offers to add them. Deleting a field from a file clears it on the resource if the API allows that field to be cleared. A field you never set, or one the API can't clear, keeps its current value.

If a resource was edited, archived, or deleted outside these files (in the Claude Console, for example), the plan ends with `This plan cannot be applied:` and the reason. The command then exits with `refusing to apply`. Pass `--force` to overwrite the edit or create a replacement.

Deleting a file leaves its resource in place with a warning, and `--prune` removes it (archiving it, or deleting it for a skill). Renaming a file therefore declares a new resource and leaves the old one in place until you prune.

`ant apply` can't adopt a resource you created in the Console or with `ant beta:agents create`. Only what's in the lockfile is managed, and applying a file that describes an existing agent creates a second one. If you downloaded your agent from the Console with **Export as code**, the download includes its own `claude-lock.json`, so applying it updates the resources you built there.

## Run ant apply in CI

Without a terminal, `ant apply` prints the plan and stops with `cannot ask for confirmation without a terminal; re-run with --yes to apply, or --dry-run to see the plan only`. Set up CI as follows:

* Run `ant apply --yes .` on your default branch after merge, naming the project directory. A bare `ant apply --yes` reconciles only files the lockfile already tracks and skips a newly added one.
* On pull requests, run `ant apply --dry-run .` to print the plan for reviewers. It's informational only and exits 0 even when the plan is blocked.
* Commit the updated `claude-lock.json` at the end of the job, even when the apply step failed partway, because a partial apply still records what it created.
* Run one apply at a time, because nothing locks the lockfile.
* Authenticate with [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation) rather than a stored API key, as an identity that reaches the organization and workspace recorded in `claude-lock.json`. `ant apply` refuses credentials that resolve to any other organization or workspace.

For a complete GitHub Actions workflow, see the [CI example in the CLI README](https://github.com/anthropics/anthropic-cli#in-ci).

## Flags

| Flag                 | Effect                                                                                                                                                                                                                |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--dry-run`          | Print the plan and exit without applying or writing the lockfile. Exits 0 even when the plan is blocked.                                                                                                              |
| `--yes`              | Apply without asking for confirmation. Required when there's no terminal.                                                                                                                                             |
| `--force`            | Apply even where a resource was changed, archived, or deleted outside these files.                                                                                                                                    |
| `--prune`            | Remove resources that are in the lockfile but no longer declared in a file.                                                                                                                                           |
| `--upgrade`          | Re-resolve skills referenced by GitHub URL, which otherwise stay pinned to the commit recorded in the lockfile.                                                                                                       |
| `--lock-file <path>` | Use this lockfile instead of searching upward from the current directory. Keep one for each organization or workspace: `ant apply` refuses a lockfile whose organization or workspace doesn't match your credentials. |
| `--verbose`, `-v`    | Show unchanged resources and full field values in the plan.                                                                                                                                                           |

## Next steps

<CardGroup cols={3}>
  <Card title="Start a session" icon="terminal" href="https://platform.claude.com/docs/en/managed-agents/sessions">
    Run the agents you applied, from the CLI or an SDK
  </Card>

  <Card title="Scheduled deployments" icon="clock" href="https://platform.claude.com/docs/en/managed-agents/scheduled-deployments">
    Deployment fields, run history, and pausing
  </Card>

  <Card title="CLI scripting and automation" icon="code" href="https://platform.claude.com/docs/en/cli-sdks-libraries/cli/scripting">
    Scripting patterns and use from Claude Code
  </Card>
</CardGroup>
