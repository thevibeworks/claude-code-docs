> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy with Enterprise Admin Console

> Manage your organization's Claude Desktop 3P configuration centrally with the Enterprise Admin Console, hosted by Anthropic

<Note>
  The Enterprise Admin Console for Desktop 3P is in beta. Contact your Anthropic representative to have an organization provisioned.
</Note>

With the Enterprise Admin Console, Anthropic hosts your organization's [Claude Desktop 3P](/docs/third-party/claude-desktop/overview) configuration, and your administrators manage it centrally instead of pushing files to each device. You sign in to the console in a browser and choose your inference provider, the app's settings, and which groups of users get which settings, rather than authoring an [MDM](/docs/third-party/claude-desktop/mdm) profile or running a [bootstrap server](/docs/third-party/claude-desktop/bootstrap). Your users sign in to Claude Desktop once with their work account, through your single sign-on if you connect it. The app then downloads the settings that apply to them and sends every model request to your provider.

Prompts, responses, and files go to your inference provider, as they do with MDM or a bootstrap server. Anthropic holds your user list and the settings you save. If you turn on usage analytics, Anthropic also holds token and session counts from your users' apps. Anthropic never holds provider credentials. For the full list of what Anthropic stores, see [Where your data goes](#where-your-data-goes).

## How it works

Anthropic creates a Claude Enterprise organization for your deployment and invites a Primary Owner. Your administrators sign in to that organization at [claude.ai](https://claude.ai) and open **Organization settings**. There they add users and groups, connect single sign-on, assign administrator roles, and edit the Claude Desktop configuration for the whole organization and for individual groups.

On each device, the user signs in to Claude Desktop once. The app recognizes that the account belongs to a third-party deployment, downloads the configuration that applies to that user, and asks the user to restart. After the restart, the app runs in third-party mode. It sends model requests to your inference provider, as it does with MDM or bootstrap delivery.

While the app runs, it re-checks the configuration on a timer. When you save a change, the app downloads it at the next check and asks the user to relaunch, as described under [Configuration updates](#configuration-updates). You don't push an MDM profile or run a bootstrap server.

Users are provisioned a Claude account only to sign in to Claude Desktop and receive their settings. They sign in with their work email address, through your single sign-on if you connect it.

## Where your data goes

Anthropic stores your organization's user accounts and the configuration you save, and delivers that configuration to users' apps. If you turn on usage analytics, Anthropic also stores the token and session counts that users' apps report. As with MDM or bootstrap delivery, prompts and model responses go to your inference provider and conversations stay on the device.

| Data                                                                                          | Does Anthropic store it?                                                                                                                                                                                                                                                                                                                                                                                                                   |
| --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Prompts, model responses, and tool inputs and outputs                                         | **No.** They go to your inference provider, and tool calls go to the connectors you configure. Data handling at the provider depends on the provider, as described under [Data handling by provider](/docs/third-party/claude-desktop/overview#data-handling-by-provider).                                                                                                                                                                      |
| Conversation history, projects, memory, and uploaded files                                    | **No.** They stay on the device.                                                                                                                                                                                                                                                                                                                                                                                                           |
| Provider credentials, API keys, bearer tokens, and MCP secrets                                | **No.** They stay on the device, and the console refuses to save them.                                                                                                                                                                                                                                                                                                                                                                     |
| Plugin and skill content                                                                      | **No.** It stays in your own repositories or on devices. The console stores marketplace locations and installation settings, not content.                                                                                                                                                                                                                                                                                                  |
| OpenTelemetry export, if you configure a collector                                            | **No.** It goes to your collector only.                                                                                                                                                                                                                                                                                                                                                                                                    |
| User accounts (name and work email), group membership, and administrator roles                | **Yes.**                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Single sign-on and SCIM connection settings, if you use them                                  | **Yes.**                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| The configuration your administrators save, organization-wide and per group                   | **Yes.** Anthropic delivers it to users' apps. It contains no credentials.                                                                                                                                                                                                                                                                                                                                                                 |
| Essential telemetry (crash and error reports) and non-essential telemetry (product analytics) | **Yes**, unless you turn them off on the **Telemetry & updates** page. Neither contains prompt or response content. [Telemetry and egress](/docs/third-party/claude-desktop/telemetry) describes what each category contains.                                                                                                                                                                                                                   |
| Usage analytics: session, token, and estimated-cost counts per user, conversation, and model  | **Yes**, if you turn on the **Report desktop usage to this organization** switch on the **Telemetry & updates** page. The switch is off by default. Users' apps report new counts only while the switch is on, and turning the switch off doesn't delete counts that Anthropic has already received. The counts contain no prompt, response, or file content. [Usage analytics](#usage-analytics) lists exactly what each report contains. |

The app contacts `api.anthropic.com` at every launch to check the user's sign-in and download the configuration. While the app runs, it contacts `api.anthropic.com` again every 10 minutes by default to check for configuration changes. The app contacts `claude.ai` when the user signs in. Both hosts are in addition to the hosts listed on [Telemetry and egress](/docs/third-party/claude-desktop/telemetry). While usage analytics is on, the app also sends its token and session counts to `api.anthropic.com` every few minutes during use and when it quits, so usage analytics needs no additional firewall entry.

## Get set up

Contact your Anthropic representative to have an organization provisioned for your deployment. The Primary Owner receives an email invitation, signs in at [claude.ai](https://claude.ai), and finds an empty organization to configure.

If your company already has a Claude organization that has verified your email domain, usually a Claude Enterprise organization, name that organization's Primary Owner as the Primary Owner of the new one too. The new organization then appears as an additional organization alongside your existing one and uses the existing organization's single sign-on connection, SCIM directory, and verified domains. Your existing organization is not changed. If no existing organization has verified the email domain of the person you name, the new organization starts with its own sign-in settings.

## Connect your identity provider

Set up single sign-on before inviting users, as described in [Set up single sign-on](https://support.claude.com/en/articles/13132885-set-up-single-sign-on-sso). Users then sign in to Claude Desktop through your identity provider, and you can provision them with SCIM. Single sign-on is recommended rather than required. Without it, invited users sign in with their work email address through the standard Claude sign-in, such as a sign-in link emailed to them.

A new organization starts set to **Invite only**, so only people you invite can join. For a pilot, keep that setting and invite the people you want. For a wider rollout, let people join automatically the first time they sign in through your identity provider (just-in-time provisioning), or sync them from your identity provider's directory with SCIM, as described in [Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195-set-up-jit-or-scim-provisioning).

When the new organization shares your existing organization's single sign-on connection, as described under [Get set up](#get-set-up), you still choose, separately for each organization, how people join it and which groups from your identity provider it uses. Groups synced from your identity provider through SCIM appear among the organization's groups and can carry their own settings, as described under [Per-group permission policies](#per-group-permission-policies).

The Claude sign-in is separate from the sign-in to your inference provider or gateway, and the app never sends Claude account credentials or tokens to your provider. Users sign in to Claude once to receive their settings. They then authenticate to your provider the same way they do with MDM or bootstrap delivery.

## Configure Claude Desktop

Sign in at [claude.ai](https://claude.ai), switch to the organization, and open **Organization settings**. The **Desktop 3P** section in the left navigation has one page per settings area, listed under [What you can configure](#what-you-can-configure). Each field sets one of the documented [configuration keys](/docs/third-party/claude-desktop/configuration), and the console checks values as you type and again when you click **Save changes**.

<Note>
  Save the **Connection** page, where you choose your inference provider, before the other pages. The console doesn't accept **Save changes** on any other page until a connection is saved. A user who signs in to Claude Desktop and clicks **Restart** before a connection is saved stays in standard Claude Desktop instead of switching to your configuration. After you save the connection, ask those users to quit and reopen Claude Desktop, then restart when prompted.
</Note>

### Start from an existing configuration file

If you already deploy Claude Desktop with an MDM profile, a bootstrap server, or a configuration built in the app, upload that configuration instead of entering each setting again. On the **Connection** page, click **Import configuration…**, then choose a `.json` file or paste the JSON. The console reads JSON in any of these forms:

* The file that Claude Desktop saves from **Developer → Configure Third-Party Inference… → Export → JSON config**, on macOS or Windows. Export it on the workstation where you built the configuration. On a device whose MDM profile or registry policy sets the Claude Desktop configuration, that window is read-only and doesn't offer this export.
* The JSON that your bootstrap server returns.
* A macOS `.mobileconfig` profile converted to JSON with `plutil -convert json -o config.json YourProfile.mobileconfig`.
* A Linux `/etc/claude-desktop/managed-settings.json` file.

For a Windows fleet, use the JSON config export, because the console doesn't read `.reg` files or registry policy.

The console fills in the matching settings and lists anything in the file that it can't store, such as credentials, bootstrap keys, and values that are set automatically from your organization, like the display name. It then shows every change against the saved configuration, and replaces the configuration when you click **Replace configuration**. If the connection in the file can't be stored, for example because it relies on an API key or token in the file, the console keeps your saved connection instead.

Before the users of an existing fleet sign in, prepare their devices:

* **MDM or bootstrap fleets:** remove the Claude Desktop configuration profile or registry policy, including a profile or policy that carries only bootstrap keys. A device that keeps one uses that configuration and ignores the admin console. A profile that sets only the [app-behavior keys](/docs/third-party/claude-desktop/mdm#update-keys-and-managed-precedence) can stay.
* **Machines configured in the app:** a device set up from the [in-app configuration window](/docs/third-party/claude-desktop/in-app-configuration) with **Apply Changes** stays in its local third-party configuration. Return it to standard Claude Desktop first. To do that, sign out in the app and choose the Anthropic sign-in option on the sign-in screen, as described under [Single-machine setup](/docs/third-party/claude-desktop/installation#single-machine-setup).

Users then sign in as described under [Onboard users](#onboard-users). Conversations from the earlier configuration stay on the device. To let users bring those conversations into the app's history, turn on **Claude.ai data import** on the **Connectors** page, which sets the [`claudeAiImport`](/docs/third-party/claude-desktop/configuration#claudeaiimport) key. Users then open **Settings → Import & export** in the app, and the earlier sessions appear in the [Cowork & Code step of the import wizard](/docs/third-party/claude-desktop/import#step-2-local-cowork-and-code-sessions).

### What you can configure

From the console you can set the same [configuration keys](/docs/third-party/claude-desktop/configuration) that MDM and bootstrap delivery support, apart from the items listed under [Limitations](#limitations). The **Desktop 3P** section of the left navigation has these pages:

| Page                    | What you configure there                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Connection**          | The inference provider ([gateway](/docs/third-party/claude-desktop/gateway), [Amazon Bedrock](/docs/third-party/claude-desktop/bedrock), [Bedrock Mantle](/docs/third-party/claude-desktop/mantle), [Google Cloud's Agent Platform](/docs/third-party/claude-desktop/vertex), or [Microsoft Foundry](/docs/third-party/claude-desktop/foundry)), its endpoint, region, or project, how users authenticate to it, custom request headers, and, under **Models**, the model list, default model, model discovery, and cost-estimate rates. **Desktop sign-in** on this page holds the **Require this organization in Claude Desktop** switch described under [Users in more than one Claude organization](#users-in-more-than-one-claude-organization). |
| **Workspace**           | Whether Chat, Cowork, and Code are each available, the folders and network hosts the app may use, permission modes and built-in tool policy, whether users may add their own skills and plugins, and organization instructions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Connectors**          | Managed MCP servers, including the [built-in connectors](/docs/third-party/claude-desktop/built-in-connectors), whether users may add their own MCP servers, desktop extension policy, and [**Claude.ai data import**](/docs/third-party/claude-desktop/import)                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Telemetry & updates** | Which telemetry categories go to Anthropic, whether users' apps report [usage analytics](#usage-analytics) to your organization, OpenTelemetry export to your collector, update policy, the [configuration relaunch window](#configuration-updates), and the configuration re-check interval                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Limits**              | A per-user token limit and its window                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Appearance**          | Banner text and colors, end-user attribution, and whether the app shows feature announcements and configuration deprecation warnings                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Plugins**             | The [plugin marketplaces](#plugin-marketplaces) that users' apps fetch, and how each one installs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

The console stores no API keys, tokens, or secrets, and refuses them anywhere in the configuration, including in request headers and MCP server settings. Users authenticate to your provider with an interactive sign-in, a cloud credential profile, or a [credential helper](/docs/third-party/claude-desktop/credential-helper) on the device, and a managed MCP server that needs a secret takes the path of a helper script that exists at the same path on every device.

Most of these settings can also differ per group of users, on the **Permission policies** page under **People**, as described under [Per-group permission policies](#per-group-permission-policies).

### Localhost base URLs

The **Gateway base URL**, **Bedrock base URL**, and **Vertex AI base URL** fields on the **Connection** page take an `https://` URL. They also accept an address on the device itself (`localhost`, `127.0.0.1`, or `[::1]`) over `https://` or `http://`, for example `http://localhost:4000`. Use a localhost address only when your organization runs a proxy or tunnel to your provider on every device in the deployment, because Claude Desktop sends model requests to whatever program answers at that address on each device.

A localhost address in these fields requires Claude Desktop 1.52386.0 or later on every device, so update your devices before you save a localhost address. With a localhost address saved, a user on an earlier release who signs in for the first time stays in standard Claude Desktop instead of switching to your configuration. A device on an earlier release that already runs your configuration loses its connection to your provider the next time the app starts, until the device updates or you remove the localhost address.

### Per-group permission policies

The **Permission policies** page, under **People** in the left navigation, applies different settings to users in specific groups. You can add policies after you save the organization-wide settings on the **Connection** page, and each group can have one policy. Click **Add permission policy**, pick a group, and set only the settings that should differ. Every other setting comes from the organization-wide settings.

A policy can, for example, turn Chat, Cowork, and Code on or off, narrow the model list and the managed MCP servers to a subset by name, and change built-in tool settings, network allowlists, telemetry, token limits, and the banner. The inference connection (the provider, its endpoint, and how users authenticate to it) is organization-wide, and a policy can't add models or managed MCP servers that the organization-wide settings don't define.

Policies are ranked in the order shown on the page, and you drag them to change the ranking. When a user belongs to several listed groups, most settings, including the model list, come from the highest-ranked of their policies that sets them, and lower-ranked policies fill in only what the higher ones leave unset. Managed MCP servers combine instead, so the user keeps every server that any of their policies selects. The OpenTelemetry settings and the token limit each come from one policy only, the highest-ranked policy that sets any part of them. Lower-ranked policies' values for them are ignored, and any part that policy leaves unset keeps the organization-wide value.

For example, if the Traders policy (ranked first) turns Code off and selects the wiki server, and the Analysts policy (ranked second) sets a token limit and selects the tickets server, a user in both groups has Code off, the Analysts token limit, and both servers. Everything these policies leave unset comes from the organization-wide settings, and a user in no listed group gets the organization-wide settings unchanged. Groups are managed on the **Groups** page under **People**, including groups synced from your identity provider.

### Plugin marketplaces

On the **Plugins** page under Desktop 3P, list the [plugin marketplaces](/docs/third-party/claude-desktop/extensions#plugin-marketplaces-admin) that users' apps should fetch. The marketplaces you add are git repositories, or a `marketplace.json` file and plugin archives on an HTTPS origin you control. The **Add marketplace** menu also offers Anthropic's public plugin marketplaces under **Curated by Anthropic**. The app does not add the Anthropic marketplaces on its own in third-party mode.

### Telemetry defaults

The telemetry categories, keys, and egress hosts on [Telemetry and egress](/docs/third-party/claude-desktop/telemetry) apply unchanged. Essential and non-essential telemetry are on until you turn them off on the **Telemetry & updates** page. The app attributes crash reports and product analytics to your organization automatically, and also attributes product analytics to the signed-in user's Claude account. An OpenTelemetry collector that you configure on the same page must use an `https://` endpoint.

### Usage analytics

Usage analytics lets your administrators see how much each user uses Chat, Cowork, and Code in Claude Desktop. Usage analytics is off by default. A member with the Owner or Primary Owner role can turn it on: open **Organization settings**, go to the **Telemetry & updates** page under **Desktop 3P**, and turn on the **Report desktop usage to this organization** switch. If your organization needs HIPAA compliance, don't turn on the switch.

Claude Desktop 1.46388.1 and later report usage. While the switch is on, each user's app counts its Chat, Cowork, and Code activity. The app sends the counts to Anthropic every few minutes during use and when it quits. A running app starts or stops reporting at its next configuration check (every 10 minutes by default), without a relaunch. Anthropic stores the counts for your organization and ties each report to the user's Claude account.

The counts appear on the **Desktop usage** page. To open the page, click **Analytics** in the user menu on claude.ai, or **Desktop usage** under **Desktop 3P** in **Organization settings**. The page includes the following:

* Sessions and tokens for Chat, Cowork, and Code (the page labels Code **Claude Code**).
* A daily chart.
* A chart of tokens by model.
* A **Team** table with one row for each member who reported usage that month. Each row shows the member's name and email from your member list, their sessions, their tokens, and their last active day.

Click a member's row in the **Team** table to show only that member's sessions and tokens. When the month's reports include cost estimates, switch the control at the top of the page from **Tokens** to **Cost** to show estimated cost in US dollars instead of tokens. Estimated cost and the chart of tokens by model cover the whole organization, and the page doesn't show them while a single member is selected.

To download a CSV file, click the **Export** button above the **Team** table. The file has one row for each member who matches the table's search, including the member's input, output, cache read, and cache write tokens and, when the month has estimates, their estimated cost.

Members with the Primary Owner, Owner, or Admin role can open the **Desktop usage** page. Members whose role from the **Admin roles** page includes the **Analytics** permission can also open the page.

Each report contains only the following:

| Data                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Example                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------- |
| A session count: one for each Chat, Cowork, or Code conversation                                                                                                                                                                                                                                                                                                                                                                                                         | `1`                                                        |
| Token counts for each conversation and model: input, output, cache read, and cache write                                                                                                                                                                                                                                                                                                                                                                                 | `1300` input tokens                                        |
| An estimated cost in US dollars for each conversation and model. The app calculates the estimate on the device, at Anthropic list prices or at the rates you set under **Models** on the **Connection** page, and labels which it used (`list` or `managed`). A model ID that the app can't match to a Claude model (such as a gateway alias) has no estimate unless you [set a rate](/docs/third-party/claude-desktop/configuration#inferencemodelpricing) for that exact ID | `0.0133`, `list`                                           |
| The tab the activity happened in                                                                                                                                                                                                                                                                                                                                                                                                                                         | `cowork`                                                   |
| The model identifier, exactly as your provider or configuration identifies the model. For Amazon Bedrock, the identifier can be an inference profile ARN, which includes your AWS region and account ID. Claude Desktop 1.52386.0 and later mask the account ID before sending. For Google Cloud, the identifier can be a resource path that includes your project ID                                                                                                    | `claude-sonnet-4-5`                                        |
| The date and time of the counted activity                                                                                                                                                                                                                                                                                                                                                                                                                                | `2026-08-27T21:00:01Z`                                     |
| A random identifier for the conversation                                                                                                                                                                                                                                                                                                                                                                                                                                 | `local_c34fa9b2-…`                                         |
| A random identifier for the app installation. Crash reports and product analytics carry the same identifier                                                                                                                                                                                                                                                                                                                                                              | `49819623-…`                                               |
| The app version, the operating system type and version, the processor architecture, and a fixed product label                                                                                                                                                                                                                                                                                                                                                            | `1.49585.0`, `darwin`, `24.6.0`, `arm64`, `claude-desktop` |

The reports never contain prompts, responses, file names or contents, tool names, tool inputs or outputs, folder or project names, connector names, or host names.

When you turn off the **Report desktop usage to this organization** switch on the **Telemetry & updates** page under **Desktop 3P** in **Organization settings**, users' apps stop reporting at their next configuration check and discard any counts they haven't sent. Turning the switch off doesn't delete counts that Anthropic has already received. While the switch is off, the **Desktop usage** page shows a notice instead of the counts. If you remove a user from the organization, your totals still include the user's counts, shown without a name or email.

## Onboard users

Before the first user signs in, confirm the following:

* You hold the Owner or Primary Owner role in the new organization
* You have saved a configuration that includes the inference provider, as described under [Configure Claude Desktop](#configure-claude-desktop)
* Single sign-on is connected, if you use it, and the users you want on this deployment are invited or provisioned, as described under [Connect your identity provider](#connect-your-identity-provider)
* Devices run the latest Claude Desktop release, installed as described in [Installation and setup](/docs/third-party/claude-desktop/installation)
* Devices carry no MDM-delivered Claude Desktop configuration. If a managed profile or registry policy sets any key other than the [app-behavior keys](/docs/third-party/claude-desktop/mdm#update-keys-and-managed-precedence) (the update, configuration re-check, relaunch window, and network proxy keys), the app uses that configuration and ignores the configuration from the admin console.
* Devices can reach `api.anthropic.com` at every launch and while the app runs, and `claude.ai` when users sign in, in addition to the hosts on [Telemetry and egress](/docs/third-party/claude-desktop/telemetry)

A device picks up the configuration from the admin console the first time the user signs in to Claude in the app. Walk through it on a test device first.

<Steps>
  <Step title="Sign in to Claude">
    Open Claude Desktop and sign in on the standard sign-in screen with your work email address, through your organization's single sign-on if you use it.
  </Step>

  <Step title="Restart when prompted">
    The app shows a dialog titled with your organization's name that reads "Your organization's Claude settings have changed. Restart to apply them." You can't dismiss the dialog. Click **Restart**, and the app relaunches in third-party mode with your configuration. An account that also belongs to another Claude organization sees a **Switch and restart** prompt instead, as described under [Users in more than one Claude organization](#users-in-more-than-one-claude-organization).
  </Step>

  <Step title="Sign in to the inference provider">
    If your connection uses an interactive sign-in, sign in to your inference provider or gateway next, as with MDM or bootstrap delivery.
  </Step>

  <Step title="Check the result">
    The account menu at the bottom of the sidebar shows your organization's name and an **Inference configuration** item marked **Managed by your organization**, and **Settings → Privacy** names your inference provider.
  </Step>
</Steps>

If something looks wrong, **Help → Troubleshooting → Generate Diagnostic Report** produces a report that shows where the app read its configuration from. You can share it with your Anthropic representative.

### Users in more than one Claude organization

A user's Claude account can belong to your deployment's organization and to other Claude organizations, and the user can move between them in Claude Desktop. When such a user signs in, the app opens in their other organization and asks whether to switch to yours, with **Switch and restart** and **Not now** buttons. A user who chooses **Not now** isn't asked again on that device and can switch later by choosing your organization from the account menu. Each move into or out of your organization restarts the app, because third-party mode runs as a separate app configuration. To go back, the user chooses **Sign out** and signs in to Claude again after the restart. From Claude Desktop 1.49585.0, they can instead pick their other organization from the account menu, which also restarts the app and asks them to sign in.

To remove the choice, turn on **Require this organization in Claude Desktop** under **Desktop sign-in** on the **Connection** page. Members who also belong to another organization are then switched to yours the next time Claude Desktop starts or they sign in, and can't choose to stay. Browsers are not affected.

### Configuration updates

From Claude Desktop 1.46388.1, a running app checks for a changed configuration about every 10 minutes, and after the device wakes. When it finds a change, it shows a **Relaunch Claude Desktop** card in the sidebar and gives the user 24 hours to relaunch. When the window ends, the app requires a restart and restarts itself after 2 minutes of inactivity. Earlier releases check about every 30 minutes and allow 1 hour.

To change the window, set **Configuration relaunch window** on the **Telemetry & updates** page. The window can be 0 to 336 hours, and 0 requires the restart as soon as the app sees the change. The setting applies to Claude Desktop 1.46388.1 and later. Earlier releases always allow 1 hour.

An app that isn't running picks up the change at its next launch. Connection and credential settings never change in a running session.

If a setting is changed that affects where users' apps connect or sign in, or what can run on their devices (including when permission policies are added, removed, or reordered), Owners receive an email alert with the identity of the administrator who made the change.

## Remove users or return to MDM

A user returns a device to standard Claude Desktop by choosing **Sign out** from the account menu. The app relaunches signed out.

When you remove a user from the organization, Anthropic revokes their Claude Desktop sign-in to that organization. A running app isn't interrupted. At its next launch the app can no longer download the organization's configuration. It shows either the sign-in screen, where **Or sign in with Claude.ai** returns the device to standard Claude Desktop, or a **Restart required** prompt whose **Restart** button does the same.

To return a whole fleet to [MDM](/docs/third-party/claude-desktop/mdm) or [bootstrap](/docs/third-party/claude-desktop/bootstrap) delivery, deploy the configuration profile or registry policy again. The device-managed configuration takes precedence over the configuration from the admin console from the app's next launch. From Claude Desktop 1.46388.1, a running app also notices the profile or policy at its next configuration re-check and asks the user to relaunch. Conversations created under the admin console's configuration stay on the device but no longer appear in the app's history after the switch. Users can bring them into the app's history from **Settings → Import & export** in the app, as described at the end of [Start from an existing configuration file](#start-from-an-existing-configuration-file), after you set the [`claudeAiImport`](/docs/third-party/claude-desktop/configuration#claudeaiimport) key with `enabled` set to `true` in the profile or policy you deploy.

## Manage the configuration with the Admin API

The configuration that the admin console edits is also available as one JSON document through the Admin API. You can keep it in version control and apply it from a pipeline.

Requests authenticate with an Admin API key that the organization's Primary Owner creates. Sign in at [claude.ai](https://claude.ai), switch to your Claude Desktop deployment's organization, and open **Organization settings → API**. Click **Create key**, name the key, and select the `read:desktop_config` scope to read the configuration and `write:desktop_config` to replace it. Only that organization's **Create key** dialog lists these two scopes. A key that reads and writes needs both scopes. Copy the key when it's shown, because you can't view it again.

Pass the key in the `x-api-key` header. The key determines the organization, so there is no organization ID in the path. The examples read the key from the `ANTHROPIC_ADMIN_KEY` environment variable.

### Read the configuration

```bash theme={null}
curl -sS --fail-with-body https://api.anthropic.com/v1/organizations/desktop_config \
  -H "x-api-key: $ANTHROPIC_ADMIN_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -o desktop-config.json.tmp \
  && mv desktop-config.json.tmp desktop-config.json
```

On an error status, curl exits non-zero before the `mv`, so your saved copy is kept and the error message is in `desktop-config.json.tmp`. `--fail-with-body` needs curl 7.76 or later. With an older curl, use `--fail`, which discards the error message. A read returns `404` until a configuration has been saved, on the **Connection** page of the console or by a first write through this API.

The response has these fields:

| Field            | Contents                                                                                                                                                                                                                                                                                                       |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `config`         | The organization-wide configuration as nested JSON, in the v2 format described under [Response schema](/docs/third-party/claude-desktop/bootstrap#response-schema) for bootstrap servers. Stored header values appear as a placeholder, as described under [Replace the configuration](#replace-the-configuration). |
| `status`         | `active` or `disabled`. A `disabled` configuration isn't served to users' apps, as the warning under [Replace the configuration](#replace-the-configuration) describes.                                                                                                                                        |
| `group_settings` | An object whose `entries` list holds the [per-group permission policies](#per-group-permission-policies) in rank order, highest first, each with a `group_id` and its `config`. A `group_id` that matches no group is accepted and applies to nobody until a group with that ID exists.                        |
| `version`        | An integer that increases with every change.                                                                                                                                                                                                                                                                   |
| `checksum`       | A digest of `config` and `group_settings` as returned. It leaves out `status`, so compare `version` to detect changes.                                                                                                                                                                                         |
| `updated_at`     | The time of the last change.                                                                                                                                                                                                                                                                                   |

### Replace the configuration

A write replaces the whole document and accepts only `config`, `status`, `group_settings`, and `expected_version`. Send `config`, `status`, and `group_settings` together, even the parts you are not changing. Sending `version`, `checksum`, or `updated_at` returns `400`. The `jq` line below keeps only the accepted fields, sets `expected_version`, and fails if `desktop-config.json` has no `version`.

Set `expected_version` to the `version` you read, or to `0` for a first write when nothing has been saved. The write is then refused with `409` if anyone changed the configuration after you read it. Without `expected_version`, the last writer wins. Sending `update.json` unedited returns `200` without creating a new version.

```bash theme={null}
jq -e 'select(.version != null) | {config, status, group_settings, expected_version: .version}' \
  desktop-config.json > update.json
# Edit update.json, then:
curl -sS --fail-with-body -X POST https://api.anthropic.com/v1/organizations/desktop_config \
  -H "x-api-key: $ANTHROPIC_ADMIN_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d @update.json
```

On an error status, curl prints the error body and exits non-zero (curl 7.76 or later, as under [Read the configuration](#read-the-configuration)). The response to a successful write is the stored document in the same shape as a read.

Header values you save are never returned. In every `headers` or `customHeaders` map, including the request headers for your provider, OpenTelemetry export, and managed MCP servers, each stored value reads as the placeholder `[stored on server - enter a new value to replace]`. Sending the placeholder back keeps the stored value. A write that sends the placeholder is refused with `400` in two cases: nothing is stored under that header name yet (a first write, or a renamed header or server), or the same write changes where those headers are sent, for example with a new `baseUrl`. Send the actual header values in those cases.

A write goes through the same checks as a save in the admin console. Users' apps pick up the change as described under [Configuration updates](#configuration-updates). Owners receive the email alert described there when a write changes where users' apps connect or sign in, what can run on their devices, or the `status`. In place of an administrator, the alert names the key by its ID (`apikey_…`).

<Warning>
  Setting `status` to `disabled` stops serving the configuration to users' apps, as if none had been saved. A running app isn't interrupted. At its next launch it shows a **Restart required** prompt whose **Restart** button returns the device to standard Claude Desktop, signed out. New sign-ins also stay in standard Claude Desktop. The admin console has no control for `status`, so only another API write can set it back to `active`. After that, users who clicked **Restart** sign in again as described under [Onboard users](#onboard-users).
</Warning>

### Admin API errors

| Status | Meaning                                                                                                                                                                                                                                                       |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `400`  | The server refused the document. The message names the field and the rule, for example `config.inference.baseUrl: must not embed credentials in the URL`. Nothing is stored.                                                                                  |
| `401`  | The key in `x-api-key` is unknown, deleted, disabled, or expired.                                                                                                                                                                                             |
| `403`  | The key lacks the scope the request needs, or isn't an organization-level key. For a missing scope, the message lists the scopes the key has and the one required.                                                                                            |
| `404`  | The key was created in an organization other than your Claude Desktop deployment's, the `x-api-key` header is missing or its key is malformed, or (on a read) no configuration has been saved yet.                                                            |
| `409`  | `expected_version` is not the current version. Read the configuration again and reapply your change.                                                                                                                                                          |
| `429`  | Admin API requests share a per-organization limit of 100 requests per minute, as described under [Rate limits](https://platform.claude.com/docs/en/manage-claude/user-management#rate-limits). Retry after the number of seconds in the `retry-after` header. |

## Limitations

* The [Claude API](/docs/third-party/claude-desktop/claude-api) is not available as the inference provider with the admin console.
* If a device can't reach `api.anthropic.com` at launch, the app opens with a **Configuration sync issue** warning and can't connect to your inference provider until it downloads the configuration. It keeps retrying in the background and loads the configuration when a retry succeeds, without a relaunch. Quitting and reopening the app retries immediately. An app that is already running keeps working if the connection to Anthropic drops.
* Bootstrap keys and settings that only make sense on the device, such as disabling claude.ai sign-in, are not available in the console.
