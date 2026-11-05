> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Claude for Government changelog

> Release notes for Claude for Government

**2026.11.05.1**

* (breaking) Changed what Claude Desktop opens for members who have **Chat in Claude Desktop**, **Cowork in Claude Desktop**, and **Code in Claude Desktop** all off and no **Claude Desktop home** chosen (**Separate settings** counts as none): Claude Desktop 1.52386.0 or later keeps Cowork on for them until November 9, 2026, 00:00 UTC (November 8 in US time zones, 7 PM Eastern); from then they may be asked to restart, after which it has nothing to open for them, and earlier versions keep Cowork on.
* Changed seating for new members: group mappings now apply at first sign-in for members your directory has already synced with that email, and if the mapped or **New members start here** seat tier is full, a member who signs in gets no seat and directory sync (SCIM) doesn't add or re-enable the member.
* Changed imports from Claude for Government Web into Claude Desktop to leave out uploaded files whose names end in `.wfm`, which a network filter may block: the chats and projects that held them still import, without those files.
* Added a notice to **Claude Desktop home** in the Admin Console: from November 10, 2026, on Claude Desktop 4.29.0 or later, turning off **Chat in Claude Desktop** or **Advanced file analysis in Chat** has no effect for members who have Cowork.
* Added **New members start here** to Anthropic-managed seat tiers: while it is on, new members in no mapped group start on that tier or get no seat.

**2026.11.04.1**

* Changed the pages after the U.S. Government notice: a second click by a member already signed in, and a sign-in with no page to return to, now open the member's start page in the Admin Console.
* Changed the Admin Console's confirmation for adding a group mapping to warn that members already on an Anthropic-managed seat tier who are not in a mapped group may be moved to a different seat tier when a group is first mapped to it, and to give the group's size as "this group has N members".
* Changed the API to end a long response when the client stops reading it for 30 seconds.

**2026.11.03.1**

* Fixed the most-used links to Claude for Government Web pages, such as saved chats, showing "Page not found" in the Admin Console: they now lead to the Admin Console's start page.
* Fixed the setup wizards' Seat tiers step telling a tenant admin who belongs to no organization that Anthropic manages the organization's seat tiers when the organization can edit them.
* (breaking) Changed the Admin Console's Group mappings page to refuse a seat tier that allows no models or has a \$0 spend limit, because the group's members could not have used Claude for Government; a mapping that already points at such a seat tier stays.
* Changed the minimum version of the Claude Code command-line tool that the gateway accepts to 2.1.274: members on an older version are asked to update before they can send messages.
* Changed how Claude Desktop and Claude Code connect to web search: Claude Desktop asks members with web search on to relaunch once after this release, and after **Sign out everywhere** a relaunch brings web search back; if a firewall or secure web gateway rule allows web search by URL path, add your Claude for Government address followed by `/gateway-api/mcp/web-search` to that rule.
* Changed active user counts on the Analytics page and in the Organization Analytics connector to count a member only when Claude answered at least one of their requests in the period: opening Claude Desktop without sending a message no longer counts, and past periods are counted the same way.
* Improved how quickly directory sync (SCIM) creates accounts for new members and restores members who return, in tenants with a large directory.
* Added a confirmation on the Config pages before a save turns off Chat, Advanced file analysis, or Cowork in Claude Desktop for members who have them.
* Added a confirmation before a save changes or replaces a connected identity provider on the tenant portal's Identity and access page and in the setup wizard.

**Claude Desktop 4.16336.0**

2026-11-03

* (breaking) Changed Code sessions on Linux hosts where AppArmor stops the sandbox, such as Ubuntu 24.04 over SSH, on Claude Desktop 4.16336.0 or later. Shell commands that failed now run unsandboxed, so **Allowed network hosts** and **Allowed workspace folders** don't limit them. An AppArmor profile for bubblewrap on the host restores the sandbox.
* (breaking) If your agency allows SSH remote sessions from Windows devices, read the changes to them in the [v4.16336.0 entry](https://claude.com/docs/cowork/changelog.md#v4-16336-0) of the Claude Desktop changelog. Setting `sshTransport` on a device has no effect in Claude for Government.
* Changed sessions on Claude Desktop 4.16336.0 or later to ignore cross-certificates between old and renewed private root CAs in the certificate store. Where a proxy's or gateway's issuing CA names one by serial number, requests can fail with `UNABLE_TO_GET_ISSUER_CERT_LOCALLY`: add that issuing CA to the store.
* Changed a project's page under the [**Standard** home](https://claude.com/docs/third-party/claude-desktop/unified-claude.md#what-users-see-with-unified-claude) on Claude Desktop 4.16336.0 or later: it no longer offers a choice of Chat or Cowork. A message sent there starts a Cowork session, or a Chat conversation on a device that can't run Cowork.
* Fixed the notice "Code has been disabled by your organization's administrator." appearing on its own at launch for members who have Chat on, and Cowork and Code off, in Claude Desktop; this needs Claude Desktop 4.16336.0 or later.

**2026.11.02.3**

* Fixed **Reset usage limits** being refused for seven days after a member moved off an Anthropic-managed seat tier.
* Fixed the seat tier delete dialog refusing a name with a doubled space when typed as shown, and closing on Escape or a click outside while the deletion was still running.
* Added confirmations in the Admin Console before saves that can change members' access or seat tiers: turning a product off, setting a \$0 spend cap, some seat tier changes, adding a group-to-seat-tier mapping or a provisioning rule for a directory group, and changing a directory group's priority.

**2026.11.02.2**

* Improved sign-in speed for existing members while a directory sync restores a deactivated member.

**2026.11.02.1**

* Removed browser access to Claude for Government Web, including its sign-in page and saved links to chats: your agency's Claude for Government address now opens the web portal.
* Updated directory sync: a seat tier or role set by an admin against a group mapping usually returns to the mapped value sooner, except a primary owner role; if the mapped seat tier has no free seat, the member stays on the tier an admin set, and a member waiting for a seat can take the seat they left.
* Improved how quickly changes to routing rules and group mappings take effect for members in tenants that sync a large directory with SCIM.

**2026.10.30.1**

* Changed **Claude Desktop home** under Config to ask in more cases before a save or a reset turns on Chat, Advanced file analysis, or Cowork.

**2026.10.28.1**

* Fixed directory sync not moving a member to another organization when one of their groups is mapped there to a self-managed seat tier with no seat limit; members it left behind move at the next directory sync that includes them.

**Claude Desktop 4.29.0**

2026-10-27

* (breaking) Changed hooks on Windows devices without Git for Windows, on Claude Code 2.1.309 or later, which Claude Desktop 4.29.0 bundles. On such a device, a hook that checks a tool call blocks the call when PowerShell runs it and its command ends with a program that exits with code 2. By default it also blocks the call when it names PowerShell as its shell and fails. To change a hook, see [Hooks on Windows devices without Git for Windows](https://claude.com/docs/third-party/claude-desktop/extensions.md#hooks-on-windows-devices-without-git-for-windows).
* (breaking) Changed Claude Desktop 4.29.0 or later for members who have **Cowork in Claude Desktop** on and no **Claude Desktop home** chosen, which is the default (**Separate settings** counts as none). At their first launch after 12:00 PM Pacific Time on November 10, 2026, they get the [**Standard** home](https://claude.com/docs/third-party/claude-desktop/unified-claude.md#what-users-see-with-unified-claude). The app turns Chat on for them, and Advanced file analysis where **Shell commands** is on, even where **Chat in Claude Desktop** or **Advanced file analysis in Chat** is off or locked off. From then on, members whose settings give them Cowork also have Chat. To keep Advanced file analysis off, choose **Chat only** as their [**Claude Desktop home**](https://claude.com/docs/government/config/settings.md#claude-desktop-home). Where **Chat in Claude Desktop** or **Code in Claude Desktop** is on, you can instead turn [**Cowork in Claude Desktop**](https://claude.com/docs/government/config/settings.md#cowork-in-claude-desktop) off. To keep Chat off too, choose **Off** as their home, which leaves them Code only.
* Changed the Microsoft 365 connector: after a device updates to Claude Desktop 4.29.0 or later, members who were connected to Microsoft 365 sign in to it again, once.

**2026.10.23.2**

* Changed directory sync (SCIM) to use your directory group order when choosing a seat tier: a member in several mapped groups gets the tier of the highest group, so some members may change seat tier.
* Fixed new directory groups sometimes taking priority over existing ones: new groups now go to the bottom of the list.

**2026.10.23.1**

* Improved links and search on the Config page: the setting you open is outlined, and a link moves keyboard focus to it.

**2026.10.22.1**

* Added the **Check for updates on releases.claude.com** setting under Config > Compliance and telemetry for networks that block `api.anthropic.com`; it is off by default and needs Claude Desktop 1.26832.0 or later.

**2026.10.21.2**

* Changed directory sync (SCIM) so existing members can move to their provisioning rule's organization without signing in first; the move signs them out and resets their role and seat tier.

**2026.10.21.1**

* Fixed the tenant portal's Identity and access page so that it says its SCIM details couldn't load instead of looking as if SCIM had never been set up.
* (breaking) Changed **Claude Desktop home** where a setting enforced at a higher level conflicts with the choice: members on Claude Desktop 1.52386.0 or later may lose Chat, Advanced file analysis or Cowork after a required relaunch.
* Changed Claude Desktop for members who have **Chat in Claude Desktop** on, **Cowork in Claude Desktop** off, and no **Claude Desktop home** chosen: from November 9, 2026 (UTC), they may be asked to relaunch and then see the new home screen, still without Cowork.
* Changed the Code tab in Claude Desktop to ask the member before each command Claude runs in its Terminal panel, even in bypass-permissions or Auto mode, while **Blocked shell commands** lists any command.
* Improved directory sync (SCIM) so that one tenant's very large sync no longer holds up directory changes in other tenants.
* Added a **Chat only** choice to the **Claude Desktop home** setting on the Config pages, which gives members Chat without Advanced file analysis or Cowork; with this choice the new home screen shows on Claude Desktop 2.2553.0 or later.

**Claude Desktop 3.1623.0**

2026-10-20

* (breaking) Changed **Let members add their own connectors** on Claude Desktop 3.1623.0 or later: with the switch off, which is the default, local MCP servers from plugins you upload may not start. If one no longer starts after the update, check whether the switch is on under **Config > Integrations**.
* (breaking) Changed SSH remote sessions on Claude Desktop 3.1623.0 or later: where your agency allows specific hosts with [`sshHostAllowlist`](https://claude.com/docs/third-party/claude-desktop/configuration#sshhostallowlist) in Claude Code's managed settings on the device, each `ProxyJump` host, and the host in a `ProxyCommand` written `ssh -W %h:%p host`, must be on that list too. The error on a refused session names the host to add; add each by its `HostName`, as [Jump hosts and the allowlist](https://claude.com/docs/third-party/claude-desktop/ssh-remote-sessions.md#jump-hosts-and-the-allowlist) describes.
* (breaking) If your agency allows SSH remote sessions, read the other breaking changes to them in the [v3.1623.0 entry](https://claude.com/docs/cowork/changelog.md#v3-1623-0) of the Claude Desktop changelog. Those described there as "where claude.ai admin settings apply" do not change anything for Claude for Government.
* Added nested sessions to Code sessions: Claude can start a task in a separate session, which reports back to the original session. Each nested session counts against the member's spend limits. To stop them, turn off **Code in Claude Desktop** under **Config > Product availability**, which also turns off all Code sessions.

**2026.10.18.1**

* Changed the scope bar dropdown on the Config pages to list **A directory group** before any group has synced.
* Changed the browser page at the end of app sign-in to tell a member with no seat that an administrator has to assign one.

**Claude Code 2.1.302**

2026-10-16

* Changed unattended runs of the Claude Code command-line tool, such as `claude -p`, where **Auto mode** is set to **Allowed**: on Claude Code 2.1.302 or later they start in Auto mode only when Auto mode is chosen for them.

**Claude Desktop 2.42304.0**

2026-10-15

* Changed **Advanced file analysis in Chat** on Claude Desktop 2.42304.0 or later: the commands Claude runs for it can now reach the hosts on your **Allowed network hosts** list.

**Claude Code 2.1.299**

2026-10-14

* Changed **Managed hooks** on Windows devices without Git for Windows: on Claude Code 2.1.299 or later, a managed hook written as a Bash command that checks a tool call or a permission request blocks that action when the command fails.

**2026.10.14.2**

* Added **Callback port** and **Callback host** to the **OAuth (pre-registered app)** option for connectors under Config > Integrations, for sign-in providers that accept the redirect only on a registered port or host; the Compliance API records both.

**2026.10.14.1**

* Fixed sign-in sending some tenants' members to a page that does not exist when single sign-on had never been connected: sign-in now shows a message instead, and the tenant portal's Identity and access page shows single sign-on as Not configured.
* Fixed the seat tier form losing what was typed in Name and Sort order when a save was refused.
* Changed the Compliance API to return only the most recent 30 days of activity; requests reaching further back succeed and return only events from the last 30 days.
* Changed the error for a chat or token-count request that is over the size limit for a single request: it is now a 413 `request_too_large` error whose "Request too large" message says to start a new conversation or send fewer or smaller attachments.
* Changed the tenant Config page to make a tenant admin choose whether organizations may set their own value the first time they set **Telemetry endpoint**, **Telemetry headers**, or **Connectors**; **Connectors** didn't offer this choice before.
* Added a **Default model** setting to seat tiers, with an **Always start with the default model** option that needs Claude Desktop 2.110.0 or later; seat tier create and update activities from the Compliance API include both settings.
* Added the **Scheduled tasks** setting under Config > Product availability, on by default; turning it off stops scheduled tasks in Cowork and Code on Claude Desktop 2.110.0 or later.

**Claude Desktop 2.37337.1**

2026-10-13

* Changed `disableDeploymentModeChooser` from recommended to required: check that the configuration profile that sets `bootstrapUrl` also sets it to true (see [Deploy to your fleet](https://claude.com/docs/government/deploy-desktop/configure.md#deploy-to-your-fleet)).

**2026.10.07.1**

* Improved screen reader support for the seat tier picker on the Admin Console's Users page.
* Changed usage limits, spend caps and usage pages to count requests with long prompts at a model's higher price for them, where a model has one.
* Added the **Terminal panel tools** setting under Integrations, which lets Claude run commands in the Code tab's Terminal panel and open, list or stop its tabs; it is on by default and off while Shell commands is off.

**2026.10.02.1**

* Changed the tenant portal's Seats and Billing pages and its billing-account picker to list billing accounts A to Z by name.
* Added an **Open Claude Desktop** button to the Account tab of the web portal: it opens Claude Desktop on the member's computer, and shows for members who have a seat tier and have Claude Desktop turned on.

**2026.10.01.1**

* Added a **New members start here** option to self-managed seat tiers, so you can pick the tier new members start on.

**2026.09.30.1**

* Fixed the Config page describing an empty **Restart deadline for configuration changes** as 1 hour; an empty field uses Claude Desktop's default, which is 24 hours on up-to-date versions.
* Changed the Config page's Product availability rows to read "Coming soon" for a product Anthropic has not yet made available to your tenant, instead of showing a switch that could be turned on without effect.
* Changed Claude Desktop's Claude for Government Web import banner so that it can come back a few days after a member skips it, until they run the import or have skipped it a few times; this needs Claude Desktop 2.16120.0 or later.
* Improved the User email addresses pages in the organization portal and the tenant portal: a list of more than 450 addresses is shown in parts of up to 450, each with its own Copy button.
* Added the `People.Read`, `Team.ReadBasic.All` and `Channel.ReadBasic.All` permissions to the Microsoft 365 connector's **Read access** list under Config > Integrations, which let Claude search for people and list a member's teams and channels; they require Claude Desktop 1.32885.1 or later.

**2026.09.29.1**

* Changed directory sync so that a member who leaves a group mapped to a self-managed seat tier with no seat limit keeps that seat tier until another group's mapping or an admin moves them.
* Added the ability for tenant administrators to grant and remove the Primary Owner role in an organization that doesn't manage its own billing account.
* Added a **Copy user email addresses** button to the tenant portal's Organizations page: it opens a page where tenant admins can copy the email addresses of everyone in the tenant who has not been deactivated, all together or one organization at a time.
* Added **Move up**, **Move down**, **Move to top**, and **Move to bottom** to each sign-in rule, provisioning rule, and directory group row in the tenant portal, so they can be reordered without dragging.

**2026.09.25.1**

* Added the **Block reads outside workspace folders** setting under Sessions and access, which stops Claude's file tools in a Claude Desktop Code session from reading outside its project folder and the Allowed workspace folders.

**2026.09.24.2**

* Fixed the keyboard focus outline on scrollable tables in the Admin Console being hard to see.
* Improved Plugins, Connectors, and Analytics in the Admin Console so that a failed load shows one consistent notice with a Try again button.
* Added the **Show the Claude for Government Web import banner** setting under Config > Appearance: for organizations linked to Claude for Government Web, Claude Desktop 2.9939.2 or later shows members a banner inviting them to bring over their chats and projects.

**2026.09.24.1**

* Fixed the person search on the Compare config page so you can change or clear the person after picking one.
* Added **Role** and **Seat tier** filters to the Users page, so you can find an organization's Owners without paging through everyone.
* Added an email to a tenant's admins when Anthropic staff change the tenant's registered domains, listing the domains before and after the change.

**2026.09.22.1**

* Fixed members whose browser sign-in is refused, for example because their account was deactivated, seeing an "Invalid redirect uri" error instead of the page that explains why they can't sign in.
* Changed web sign-in for tenant administrators and Primary Owners: the **Choose sign-in** page is gone, **Email me a sign-in link** is now under the form where you enter your work email, and **Continue** takes you straight to single sign-on when your tenant has it set up.
* Changed sign-in for Claude Desktop: signing in right after another app sign-in in the same browser now goes through your identity provider, and you may be asked which account to use.
* Changed the model picker in Claude Desktop: a model that needs a newer version of the app no longer appears until the app is updated.
* Updated the device sign-in approval page to name the application that asked to sign in and to warn when the request came from a different network address than your browser.
* Updated the **Require approval for each command** and **Require approval for each fetch** help text on the Config page: with these settings off, Chat and Cowork fetch pages and run shell commands without asking, which for Chat's shell commands is new since Claude Desktop 2.110.0.
* Improved what a browser sign-in shows when it expires or is not completed: a page that says what happened and where to sign in again, instead of a line of error text.
* Improved how the Admin Console handles brief faults: a page, or part of one, that can't load now says so and offers a way to try again.
* Added a confirmation step before revoking a SCIM token, deleting a connector or removing a group mapping in the Admin Console.
* Added the **Let members add their own connectors** setting under Config > Integrations at the tenant, organization, and group levels, off by default; turning it on lets members add connectors of their own in Claude Desktop.
* Added a **Copy user email addresses** button to the Users page: it opens a page where organization owners and tenant admins can copy the email addresses of everyone in an organization who has not been deactivated, separated by commas or, for Outlook, by semicolons.

**2026.09.16.1**

* Fixed members not being reactivated after they are re-enabled in your identity provider.
* Changed SCIM provisioning to reject requests to deactivate an organization's primary owner or a tenant's last admin until ownership is transferred or another admin is added.
* Changed SCIM provisioning to return an error that says what to do first when an identity provider deactivates or changes the email address of a member who is not yet linked to their directory entry.
* Changed sign-in for accounts outside any organization that still held a Primary Owner role without being a tenant admin: they now sign in like any other member.
* Changed sign-in: a network that starts sign-ins unusually fast is briefly told to try again.
* Added a check of the Issuer against what your identity provider publishes when you save OIDC single sign-on.
* Added a Test sign-in button to the Single sign-on settings on the tenant portal's Identity and access page, so a tenant admin can check their own sign-in through their identity provider.
* Added **Sign out everywhere** to each member's row menu on the Users page, which ends all of that member's sessions; the Compliance API records it as `user.sessions_revoked`.
* Added the option to enforce settings whose values are hidden after saving, such as Telemetry headers, from the Admin Console.
* Added the **Claude Desktop home** setting on the Config page, which sets Chat, Advanced file analysis, and Cowork in Claude Desktop together. It needs Claude Desktop 1.52386.0 or later.

**2026.09.15.1**

* Fixed directory provisioning (SCIM) rejecting some of the user updates that Microsoft Entra ID sends by default.
* Changed what removing a tenant admin does for someone who is not yet in an organization: they can no longer request an emailed sign-in link and are placed by the sign-in routing rules at their next single sign-on, like any other member.
* Changed where Claude Desktop looks for Anthropic's published model catalog (model names, descriptions and effort options): starting with the first Claude Desktop release that supports the setting, the app asks your Claude for Government host for it instead of `downloads.claude.ai`, and keeps using the catalog it already has when the host has no copy.
* Improved how service updates are applied so that answers still being generated when an update begins have longer to finish.
* Added more checks of your identity provider's signing certificate when you save SAML single sign-on.
* Added the "Let members create skills" setting under Config > Integrations, on by default: turning it off stops members from creating or uploading skills of their own in Claude Desktop.

**2026.09.11.1**

* (breaking) Changed the **Telemetry endpoint** setting on the Config page to check its host name more strictly when you save; an address that is already saved stays until the setting is next changed.
* Changed plugin uploads to ask for the Runs code confirmation when a plugin's `settings.json` sets anything other than its default agent or a `$schema` reference, such as a status line.
* Added tenant-level Compliance API keys: tenant administrators can create, list, and revoke them on the tenant portal's **Compliance API keys** page under Settings, and a tenant-level key returns the events of every organization in the tenant together with tenant-level activity.
* Improved accessibility in the Admin Console for people who use the operating system's reduce motion setting or a screen reader.

**2026.09.10.1**

* Fixed importing Claude for Government Web chats into Claude Desktop failing with "This account doesn't match your organization" for members of tenants that use directory provisioning (SCIM) now but did not on Claude for Government Web.
* Added the "Let members add plugin marketplaces" and "Let members add their own plugins" settings under Config > Integrations at the tenant, organization, and group levels, both off by default: members on Claude Desktop 1.37937.0 or later can no longer add plugin marketplaces or their own plugins unless an admin turns these on, while marketplaces and plugins they already added keep working.
* Changed the "Claude Code" and "Claude for Microsoft 365" switches under Config > Product availability so that turning a product off takes effect at once for members already signed in to it, instead of waiting for the product to re-read its settings; a member who signs in to Claude for Microsoft 365 while it is off is now told so on the sign-in page.
* Added the "IPv6 in the sandbox" setting under Config > Access and models at the tenant, organization, and group levels, off by default: when it is on, Claude Desktop on macOS and Windows lets tools in its sandbox reach IPv6-only hosts during Cowork tasks, which takes effect once a Claude Desktop release that supports the setting is available.

**2026.09.09.1**

* Changed how the "Telemetry headers" setting and your connectors are delivered to Claude Desktop, ahead of Claude Desktop retiring the older formats: nothing changes in your settings or for members, and the notice about deprecated configuration fields that Claude Desktop 1.40609.0 or later can show no longer lists them.

**2026.09.08.1**

* Fixed web fetch failing in Claude Desktop's Code sessions on networks that block `api.anthropic.com`: sessions no longer contact that host before fetching a page, which takes effect on Claude Desktop 1.37937.0 or later after a restart.
* Fixed the sign-in page Claude Desktop opens in the browser showing an error instead of a field to enter the code when it is opened without a code or with an expired one.

**2026.09.04.1**

* Changed the limit on a member's active app sign-ins from 3 shared across the Claude apps to 6 in each app: a new sign-in over the limit now signs out the one closest to expiring instead of the oldest.

**2026.09.03.1**

* Fixed Admin Console pages sometimes loading part light and part dark when your computer is set to dark mode, which made some text hard to read.
* Improved the Admin Console for tenant admins who manage several organizations: every page shows which organization or tenant your changes apply to.

**2026.09.02.1**

* Fixed the Sessions page under Account showing every app sign-in as "Desktop app": each sign-in now names its app, or reads "Claude app" when the app is not known.
* (breaking) Changed the "Telemetry endpoint" setting under Config > Compliance and telemetry to refuse an address products can't use, such as one with a password or a `?` query; an address you already saved is checked only when you next change the setting.
* (breaking) Changed the "Telemetry resource attributes" setting under Config > Compliance and telemetry to refuse a value longer than 255 bytes, where a space or an accented letter counts as three or more bytes; values you already saved are checked only when you next change the setting.
* (breaking) Changed the "Advanced file analysis in Chat" setting under Config > Product availability to apply only on Claude Desktop 1.14271.0 or later; on 1.13576.0, the only earlier version with this feature, it is off until the app is updated.

**2026.08.28.1**

* Improved screen reader and keyboard support in the Admin Console: actions such as revoking a key or saving seats now announce their result, and keyboard focus returns to the control you used instead of being lost.
* Changed the main button on the sign-in pages to a dark button with a white label so it is easier to read; the page an emailed sign-in link opens now announces its result to screen readers.
* Added the "Restart deadline for configuration changes" setting under Config > Compliance and telemetry: it sets how long members can keep working after a settings change before Claude Desktop requires the restart that applies it, and takes effect on Claude Desktop 1.40609.0 or later.
* Added a search box to the Config page that finds a setting by its name or description and takes you to it.

**2026.08.26.1**

* Fixed members on the default 24-hour "Session idle timeout" being signed out a day after signing in even when they had kept using Claude; the timeout now counts from a member's last activity.
* Improved screen reader support in the Admin Console: dialog options, repeated buttons, and usage meters are announced with distinct names, every page has its own browser title, and the setup wizards move keyboard focus to the new step's heading when you change steps.
* Changed the "Session idle timeout" setting so a tenant admin can set it as high as 96 hours (5,760 minutes), with larger values refused; a value above 24 hours saved earlier, which was ignored until this release, now applies, and the 24-hour default is unchanged.
* Added connector management to the Group configuration pages: tenant admins and organization owners can add, override, or remove connectors for one directory group instead of only for the whole tenant or organization, and these changes appear as new activity types in the Compliance API feed.

**2026.08.25.2**

* Fixed adding a plugin or marketplace under Config > Integrations > Plugins failing with "Something went wrong" for all but the smallest zip files.
* Added text alternatives to the charts on the Admin Console's Analytics page: screen readers announce each chart by name and can read its plotted values as a table.

**2026.08.25.1**

* Fixed the "By product" table on the Analytics page counting Claude for Microsoft 365 activity as "Unknown".

**2026.08.24.1**

* Fixed Admin Console pages cutting off setting names, values, and buttons at high browser zoom or in narrow windows; content now wraps instead of scrolling sideways.
* Added two settings under Config > Compliance and telemetry: "Application event level (Claude Desktop)" chooses how much of Claude Desktop's application event log goes to your telemetry collector, and "Telemetry resource attributes (Claude Desktop)" adds your own labels to every record.
