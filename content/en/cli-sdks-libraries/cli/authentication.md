---
title: CLI authentication options
url: https://platform.claude.com/docs/en/cli-sdks-libraries/cli/authentication
description: Authenticate the ant CLI with interactive login, API keys, named profiles, and Workload Identity Federation.
---

The `ant` CLI supports several credential sources. The [CLI quickstart](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/quickstart#authentication) covers the one-command login (`ant auth login`). This page covers every option in full.

## Interactive login

`ant auth login` lets you call the API without creating or managing an API key. It opens a browser-based OAuth flow against the Claude Console and stores the resulting credentials under `$ANTHROPIC_CONFIG_DIR` (see [Configuration directory](https://platform.claude.com/docs/en/manage-claude/wif-reference#configuration-directory) for the OS-specific default). On a remote host or in any environment without a local browser, pass `--no-browser` to print the authorize URL and paste the returned code back into the terminal.

```bash CLI
ant auth login

# On a remote host without a browser:
ant auth login --no-browser

# Bind to a specific workspace and skip the browser picker:
ant auth login --workspace-id wrkspc_01...

# If the profile that you name with --profile doesn't exist,
# the login creates it.
ant auth login --profile work
```

The CLI stores each login under a profile. The first time you log in under a profile, you select a [workspace](https://platform.claude.com/docs/en/manage-claude/workspaces) in the browser. If you belong to more than one Claude Console organization, you select the organization first. The issued token is [scoped to that workspace](https://platform.claude.com/docs/en/manage-claude/workspaces#api-keys-and-resource-scoping), so the CLI can only see resources that belong to it. Pass `--workspace-id` to bind directly to a workspace and skip the workspace picker.

The profile keeps that organization and workspace for its later logins. To work in another organization or workspace, log in under a new profile (see [Switch between workspaces](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/authentication#switch-between-workspaces)).

Interactive login is intended for local development and scripting on your own machine. For non-interactive workloads such as CI, servers, and containers, use [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation) instead.

Login writes credentials to `credentials/<profile>.json`. The first login for a profile also creates `configs/<profile>.json`.

A login that names a profile, with `--profile` or `ANTHROPIC_PROFILE`, makes that profile the [active profile](https://platform.claude.com/docs/en/manage-claude/wif-reference#active-profile). Any command that doesn’t name a profile, a login included, uses the active profile. Until you make another profile active, that’s `default`.

To remove the active profile’s stored credentials, run `ant auth logout`. The profile keeps its organization and workspace. To clear every profile, those settings included, run `ant auth logout --all`.

## Admin access

By default, `ant auth login` requests a workspace-scoped token. To manage the resources documented on the [Admin API](https://platform.claude.com/docs/en/manage-claude/admin-api) page, request the `org:admin` scope under a dedicated profile. The login makes that profile active, so the example ends by switching back to your day-to-day profile:

```bash CLI
ant auth login --profile admin --scope "org:admin"

# Print a bearer token for Authorization headers:
ant auth print-credentials --profile admin --access-token

# Switch back to your day-to-day profile, the one that was active
# before the login, such as default:
ant profile activate default
```

Anthropic grants the `org:admin` scope only to users and service accounts with the admin role. The issued token has organization-wide access, and any workspace binding on the profile does not constrain it. Keep the admin profile separate from your day-to-day profile so routine commands never run with elevated access.

## API key

The CLI also reads your API key from the `ANTHROPIC_API_KEY` environment variable. Get a key from the [Claude Console](https://platform.claude.com/settings/keys).

<Tabs>
  <Tab title="zsh">
    ```bash
    echo 'export ANTHROPIC_API_KEY=sk-ant-api03-...' >> ~/.zshrc
    source ~/.zshrc
    ```
  </Tab>

  <Tab title="bash">
    ```bash
    echo 'export ANTHROPIC_API_KEY=sk-ant-api03-...' >> ~/.bashrc
    source ~/.bashrc
    ```
  </Tab>

  <Tab title="Windows">
    ```powershell
    setx ANTHROPIC_API_KEY "sk-ant-api03-..."
    ```

    Open a new terminal for the change to take effect.
  </Tab>
</Tabs>

To override the key for a single run, pass [`--api-key-stdin`](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/using#global-flags) and pipe the key to the command. To point at a different API host, set `ANTHROPIC_BASE_URL` or pass `--base-url`.

If you are using a [personal or service account key](https://platform.claude.com/docs/en/manage-claude/authentication#key-types) that isn’t scoped to a workspace, you must [specify the workspace](https://platform.claude.com/docs/en/manage-claude/authentication#select-a-workspace) to run your command in. Do this by setting an `ANTHROPIC_WORKSPACE_ID` environment variable, which the CLI reads automatically, or by using the [`--workspace-id` flag](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/using#global-flags). The value must be a `wrkspc_...` ID.

```bash CLI
ant messages create \
  --workspace-id wrkspc_01... \
  --model claude-opus-5-5 \
  --max-tokens 1024 \
  --message '{role: user, content: "Hello, Claude"}'
```

## Claude Models on Google Cloud (Anthropic managed)

To call [Claude Models on Google Cloud (Anthropic managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed), the CLI uses Google Application Default Credentials instead of `ant auth login` or an API key. To set up the CLI, follow these steps:

1. **Set up the credentials:** See [Authentication on Claude Models on Google Cloud (Anthropic managed)](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed#authentication).
2. **Set your project ID and workspace ID:** Pass `--google-cloud-project` and `--google-cloud-workspace-id`, or set `ANTHROPIC_GOOGLE_CLOUD_PROJECT` and `ANTHROPIC_GOOGLE_CLOUD_WORKSPACE_ID`. For the other settings and their defaults, see [Project, location, and workspace resolution](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed#project-location-and-workspace-resolution).
3. **Leave competing settings unset:** An API key, an authentication token, a configuration profile, or Anthropic’s federation variables can take precedence over these settings. Before you run a command, check [which settings to leave unset](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed#credential-precedence).
4. **Confirm that the CLI uses these settings:** Run `ant auth status` and check that the `Google Cloud` row is marked `(active)`. If you set them with flags, pass the same flags to `ant auth status`.

## Check authentication status

`ant auth status` prints the credential source the CLI selected (API key environment variable, OAuth login, federation, Google Cloud, or profile), the active profile, the workspace the active token is bound to, and the configuration directory paths. Use it to diagnose why a workload picked the wrong credential or workspace.

```bash CLI
ant auth status
```

```text
Active profile:  default
Config dir:      ~/.config/anthropic
Profile config:  ~/.config/anthropic/configs/default.json
Credentials:     ~/.config/anthropic/credentials/default.json

Credentials
  (active) * Profile (user_oauth) [via active_config]       sk-ant-oat01-EXA...
...

Workspace
  (active) * Workspace                                      wrkspc_01... (Engineering)
```

Read the `(active)` rows to see which credential source and workspace won. The command reports status rather than performing a health check, so don’t script against the exit status. For the full ordering of credential sources, see [Credential precedence](https://platform.claude.com/docs/en/manage-claude/wif-reference#credential-precedence).

## Switch between workspaces

An interactive-login token is bound to a single workspace. To use the CLI against more than one workspace, log in to each under its own named profile, then switch between them:

```bash CLI
# 1. Create the profile (interactive; pick the other workspace in the
#    browser, or pass --workspace-id to skip the picker):
# ant auth login --profile other-ws

# 2. The login made other-ws active. Switch back to your day-to-day
#    profile, such as default:
ant profile activate default

# 3. Use other-ws for one command; later commands still use default:
ant --profile other-ws models list
ANTHROPIC_PROFILE=other-ws ant models list
```

Run [`ant auth status`](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/authentication#check-authentication-status) to confirm which profile and workspace are active.

<Note>
  An `ANTHROPIC_API_KEY` or `ANTHROPIC_AUTH_TOKEN` in your environment takes precedence over every profile (see [Credential precedence](https://platform.claude.com/docs/en/manage-claude/wif-reference#credential-precedence)). Until you unset it, API requests use that credential, whichever profile you select, and `ant` prints a message to stderr that says so.
</Note>

## Manage profiles

The `ant profile` subcommands inspect and edit profile state directly:

```bash CLI
ant profile list
ant profile get --profile other-ws
ant profile set workspace_id wrkspc_01... --profile other-ws
```

The writable keys for `ant profile set` are `workspace_id`, `base_url`, `organization_id`, `scope`, `client_id`, and `console_url`. Setting `workspace_id` records the target workspace in the profile config but does not rebind credentials that were already issued; run `ant auth login` again under that profile to mint a token for the new workspace.

For the profile file schema and the federation block, see [Profile configuration file](https://platform.claude.com/docs/en/manage-claude/wif-reference#profile-configuration-file). For Workload Identity Federation, see [Authentication](https://platform.claude.com/docs/en/manage-claude/authentication) and the [WIF reference](https://platform.claude.com/docs/en/manage-claude/wif-reference).

## Next steps

<CardGroup cols={3}>
  <Card title="Using the CLI" icon="terminal" href="https://platform.claude.com/docs/en/cli-sdks-libraries/cli/using">
    Command structure, output formats, GJSON transforms, and request bodies
  </Card>

  <Card title="CLI scripting and automation" icon="code" href="https://platform.claude.com/docs/en/cli-sdks-libraries/cli/scripting">
    Version control for API resources, scripting patterns, and use from Claude Code
  </Card>

  <Card title="Workload Identity Federation" icon="cloud" href="https://platform.claude.com/docs/en/manage-claude/workload-identity-federation">
    Non-interactive authentication for CI, servers, and containers
  </Card>
</CardGroup>
