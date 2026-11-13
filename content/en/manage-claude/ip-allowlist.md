---
title: IP allowlisting
url: https://platform.claude.com/docs/en/manage-claude/ip-allowlist
description: Secure your organization by limiting access to specific IP addresses that you trust.
featureMetadata:
  status: beta
---

IP allowlisting protects your organization by only allowing [covered requests](https://platform.claude.com/docs/en/manage-claude/ip-allowlist#where-the-allowlist-applies) to come from specific IP ranges. This means that if an API key is leaked, it is much harder for an attacker to use the key. This can prevent data leaks and reduce the likelihood of being charged for abusive use.

An allowlist limits where a key works, but not for how long. You should also set a short [key expiration](https://platform.claude.com/docs/en/manage-claude/authentication#key-expiration), or move to [Workload Identity Federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation) to stop using static keys. This is safer than allowlisting alone.

<Note>
  IP allowlisting is available in beta under your agreement with Anthropic, such as the [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms) and the [Service Specific Terms](https://www.anthropic.com/legal/service-specific-terms). Settings and behavior can change during the beta.
</Note>

## How it works

An organization admin or owner sets up a list of IP ranges in settings. This list of ranges covers your entire organization. For each covered request, Anthropic compares the request’s public IP address with your list, and denies it if it is not allowed.

* **API requests** to [covered endpoints](https://platform.claude.com/docs/en/manage-claude/ip-allowlist#where-the-allowlist-applies) from an address outside the list are rejected. For example, the Messages API returns a 403 `permission_error` with the message `Your IP address isn't in this organization's allowed range.`
* **People** who connect from a disallowed address see a page titled **Your current network can’t access this organization**. Organization admins are also blocked, but you can optionally [give admins a way back in](https://platform.claude.com/docs/en/manage-claude/ip-allowlist#avoid-locking-yourself-out) to avoid lockout, in which case they can access only the allowlist settings.

## Claude Platform organizations

### Where the allowlist applies

* **The Claude Console:** UI access is restricted.
* **The following Claude API endpoints:** [Messages](https://platform.claude.com/docs/en/api/messages), [Message Batches](https://platform.claude.com/docs/en/build-with-claude/batch-processing), [Token Counting](https://platform.claude.com/docs/en/build-with-claude/token-counting), [Models](https://platform.claude.com/docs/en/api/models/list), [Files](https://platform.claude.com/docs/en/build-with-claude/files), and [Skills](https://platform.claude.com/docs/en/build-with-claude/skills-guide), with an API key or a Workload Identity Federation token.
* **The following Claude Managed Agents endpoints:** [Agents](https://platform.claude.com/docs/en/managed-agents/agent-setup), [Sessions](https://platform.claude.com/docs/en/managed-agents/sessions), [Environments](https://platform.claude.com/docs/en/managed-agents/environments), [Vaults](https://platform.claude.com/docs/en/managed-agents/vaults), and [Memory stores](https://platform.claude.com/docs/en/managed-agents/memory), with an API key or a Workload Identity Federation token.
* **The following organization APIs:** The [Admin API](https://platform.claude.com/docs/en/manage-claude/admin-api) and the [Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api), with a [key that covers only this organization](https://platform.claude.com/docs/en/manage-claude/admin-api-keys#which-key-do-you-need).

See also [Limitations](https://platform.claude.com/docs/en/manage-claude/ip-allowlist#limitations).

## Claude Enterprise organizations

A Claude Enterprise organization has its own IP allowlist, which only allows access to the [apps that it covers](https://platform.claude.com/docs/en/manage-claude/ip-allowlist#apps-that-the-allowlist-covers) from specific IP ranges. This means that if a user’s sign-in is stolen, it is much harder for an attacker to use it. This list covers your entire organization, owners included. Owners and primary owners can set it up. Before you [turn on the allowlist](https://platform.claude.com/docs/en/manage-claude/ip-allowlist#turn-on-the-allowlist), read [Avoid locking yourself out](https://platform.claude.com/docs/en/manage-claude/ip-allowlist#avoid-locking-yourself-out).

### Apps that the allowlist covers

Users outside the list lose access to your organization in:

* Claude in a browser, the desktop apps, and the mobile apps
* [Claude Code](https://code.claude.com/docs/en/overview), when users sign in with their Claude account
* Claude in Chrome, the [Office add-ins](https://claude.com/docs/office-agents/overview), [Cowork](https://claude.com/docs/cowork/overview), and Remote Tools

This includes connectors and artifacts in these apps, except artifacts that a user shared outside the organization. For Claude Science, see [Identity and access in the Claude Science admin controls](https://claude.com/docs/claude-science/admin-controls#identity-and-access).

The allowlist also covers the [Admin API](https://platform.claude.com/docs/en/manage-claude/admin-api) and the [Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api), with a [key that covers only this organization](https://platform.claude.com/docs/en/manage-claude/admin-api-keys#which-key-do-you-need).

See also [Limitations](https://platform.claude.com/docs/en/manage-claude/ip-allowlist#limitations).

### What users can expect

On the web and in the desktop apps, blocked users see a page titled **Your current network can’t access this organization**. Owners are also blocked, but you can optionally [give owners a way back in](https://platform.claude.com/docs/en/manage-claude/ip-allowlist#avoid-locking-yourself-out) to avoid lockout, in which case they can access only the allowlist settings. In Claude Code, blocked users see a 403 API error with the message `Your IP address isn't in this organization's allowed range.`

* **Other accounts:** Blocked users can still sign in and use other organizations or a personal account.
* **Remote users:** Phones on mobile data, home Wi-Fi, and laptops off the VPN are blocked until they connect through a listed network.
* **Proxies:** Some features connect through `bridge.claudeusercontent.com`: Claude in Chrome, Cowork, Remote Tools, and [work across apps](https://claude.com/docs/office-agents/work-across-apps) in the Office add-ins. If your proxy sends that host out through a different address from `claude.ai` and `api.anthropic.com`, list that address too.

## Limitations

* **Claude Platform:** The allowlist covers requests to the [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview) endpoints, not the agents themselves. It doesn’t apply to any networking in the Claude Managed Agents runtime. The allowlist doesn’t apply to [Claude in Amazon Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock), [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws), [Claude Models on Google Cloud](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/overview), or [Claude in Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry).
* **Claude Enterprise:** Claude Design, Claude in Slack, and Claude Academy aren’t covered. If Claude is working on a task in a chat when a user is blocked, the task can continue for up to 24 hours. The user can’t open or control that chat from outside the list.

## Turn on the allowlist

<Steps>
  <Step title="Turn on the toggle">
    Go to your organization’s settings page:

    * **Claude Platform:** The [Security](https://platform.claude.com/settings/identity) page in the Claude Console
    * **Claude Enterprise:** [claude.ai > Organization settings > Organization and access](https://claude.ai/admin-settings/organization#ip-allowlist)

    Turn on the **IP allowlist** toggle. Nothing changes until you save.
  </Step>

  <Step title="Add your ranges and save">
    Click **Add entry** (Claude Console) or **Add IP range** (claude.ai), enter one or more addresses or ranges, separated by commas, and press Enter. List each network that your servers, CI, and users connect from, including the one you’re connecting from. Anthropic recommends making sure the **Allow admins to access this settings page from any IP address** (Claude Console) or **Allow owners to access this settings page from any IP address** (claude.ai) checkbox is selected to [avoid lockout](https://platform.claude.com/docs/en/manage-claude/ip-allowlist#avoid-locking-yourself-out). Then click **Save** and confirm.
  </Step>

  <Step title="Check your traffic">
    Changes can take up to 15 minutes to apply. Watch your applications for 403 `permission_error` responses, including jobs that run only daily or weekly, and add any address that you missed. In a Claude Enterprise organization, ask users on each network to confirm that they can still open Claude. There, changes can take longer to reach connections that are already open, the Office add-ins, and Remote Tools.
  </Step>
</Steps>

### Entry format

* **Format:** You can allowlist IPv4 or IPv6 addresses. Each entry can be a single address (`203.0.113.5`) or a CIDR range (`203.0.113.0/24`, `2001:db8::/32`) no broader than `/8` for IPv4 or `/32` for IPv6. The list holds up to 1,000 entries.
* **Public addresses only:** List the addresses that your traffic leaves your network from, not private ranges such as `10.0.0.0/8`. If you add a shared proxy address, note that an attacker with a leaked key or a stolen sign-in could potentially use it through the proxy.

## Avoid locking yourself out

When you save, the settings page checks your current address against the list to make sure you aren’t about to lock yourself out. But it does not check your servers, your teammates, or the address you might connect from tomorrow.

* **Make sure to list every network first:** Include data centers, CI systems, offices, VPNs, proxies, and the workers of any [self-hosted sandboxes](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes), with their public IPv4 and IPv6 addresses. Note that home and mobile addresses can often change without notice.
* **Keep a way back in:** Anthropic recommends selecting the **Allow admins to access this settings page from any IP address** (Claude Console) or **Allow owners to access this settings page from any IP address** (claude.ai) checkbox. Then an admin (an owner in claude.ai) can fix the list from anywhere. The downside is that an attacker who compromises an admin’s or owner’s session could update the allowlist from a remote location. If you [set up the Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api-access) for your organization, its [Activity Feed](https://platform.claude.com/docs/en/manage-claude/compliance-activity-feed) records changes to the allowlist, so you can audit them.

### If you are locked out

In a Claude Enterprise organization, admins can’t change the list, so “admin or owner” in these steps means an owner or primary owner.

1. **Reconnect from a listed network:** Connect to your office network or VPN, and then click **Try again**. If there is no **Try again** button, reload the page.
2. **Ask another admin or owner:** An admin or owner on a listed network can add your address.
3. **Fix the list from where you are:** If you are an admin or owner and the checkbox under [Keep a way back in](https://platform.claude.com/docs/en/manage-claude/ip-allowlist#avoid-locking-yourself-out) is selected, you can still reach the settings page. Open the Claude Console or Claude in a browser and click **Open IP allowlist**, or go to the [Security](https://platform.claude.com/settings/identity) page ([Organization and access](https://claude.ai/admin-settings/organization#ip-allowlist) in claude.ai). Click **Add it** to add your current address, or turn off the allowlist, and then click **Save** and confirm. Access can take up to 15 minutes to return.
4. **Contact Anthropic:** If no admin or owner can reach the page, ask [Anthropic support](https://support.claude.com) to turn off the allowlist.
