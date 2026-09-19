> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Built-in browser and Claude in Chrome

> Configuring Claude in Chrome and the built-in browser in Cowork and Code for Claude Desktop 3P

In Claude Desktop on third-party (3P), Claude can work with web pages in Cowork and Code sessions through Claude in Chrome or through the built-in browser. [Claude in Chrome](#claude-in-chrome) lets Claude work in the user's own Google Chrome or Microsoft Edge and is available to organizations managed from the [Enterprise Admin Console](/docs/third-party/claude-desktop/admin-console). The [built-in browser](#built-in-browser) is a pane inside Claude Desktop that any deployment can turn on with the [`builtinBrowserEnabled`](/docs/third-party/claude-desktop/configuration#builtinbrowserenabled) key, and three related keys control which sites Claude can open in it. This page explains how to configure both for Claude Desktop on 3P and how they work there. To learn how to use them, see [Use the built-in browser in Claude Cowork](https://support.claude.com/en/articles/16607400-use-the-built-in-browser-in-claude-cowork) and [Get started with Claude in Chrome](https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome).

## Claude in Chrome

[Claude in Chrome](https://claude.com/chrome) is Anthropic's browser extension. It lets Claude work in the user's own Google Chrome or Microsoft Edge, with the tabs and sign-ins the user already has there. In Claude Desktop on 3P, it is available only to organizations managed from the [Enterprise Admin Console](/docs/third-party/claude-desktop/admin-console), because it relies on the work-account sign-in to Claude Desktop that only those organizations use. When the configuration comes from MDM, a local file, or a bootstrap server, use the [built-in browser](#built-in-browser) instead.

When Claude in Chrome is on, Claude can open and work in tabs in the user's browser during Cowork and Code sessions. Model requests still go to your inference provider.

### Turn on Claude in Chrome

In **Organization settings** on claude.ai, open the **Claude in Chrome** page and turn on the **Enable for your team** switch. On the same page, choose whether Claude in Chrome works on every site except the ones you block, or only on the sites you allow. Then add sites with the **Add websites** button. These site permissions are the same ones the built-in browser uses for your organization.

Claude in Chrome also needs the **Allow user-added MCP servers** switch on the **Connectors** page under **Desktop 3P** in **Organization settings** to stay on. While that switch is off, Claude Desktop doesn't connect to Claude in Chrome.

### Set up Claude in Chrome on a device

Users install [Claude in Chrome](https://claude.com/chrome) from the Chrome Web Store in Google Chrome or Microsoft Edge on macOS or Windows, or you deploy the extension to them with Chrome's management policies, as described under [Permissions required to install Claude in Chrome](https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome). Each user signs in to the extension with the same work account they use in Claude Desktop. Claude Desktop then connects to the extension automatically, and Claude can use that browser in the user's Cowork and Code sessions.

## Built-in browser

When the built-in browser is on, Cowork and Code sessions show a **Browser** pane where users can open and sign in to any site. In the pane, Claude can open pages, read them, click, type, fill in forms, take screenshots, and run JavaScript on a page.

Before Claude acts on a site, Claude Desktop asks the user to approve it. **Allow once** covers that page, and **Always allow** saves the site on the device until the user revokes it in **Settings**. After a user approves a site, Claude can read and interact with its pages as the user sees them, including pages behind the user's sign-in on that site.

Pages load directly from the user's device, so your network's proxy, firewall, and DNS filtering apply to them. Sign-ins and cookies from the pane stay in the app's own browser storage on the device, separate from the user's other browsers. Cowork sessions keep them until the user clicks **Clear browsing data** in the pane's menu. Code sessions clear them when the app quits, unless the user sets **Keep cookies** in the pane's menu to **Shared** or **Per session**.

### Turn on the built-in browser

The built-in browser is off by default. Set [`builtinBrowserEnabled`](/docs/third-party/claude-desktop/configuration#builtinbrowserenabled) to `true` in your managed configuration, under **Built-in browser** in the **Capabilities** section of the [in-app configuration window](/docs/third-party/claude-desktop/in-app-configuration). The change takes effect after Claude Desktop restarts.

Also allow `releases.claude.com` through your firewall, because Claude Desktop contacts it for the [site safety check](#site-safety-check). If the app can't complete a check, users can keep browsing the site, but Claude can't read or act on it.

If your devices use a [bootstrap server](/docs/third-party/claude-desktop/bootstrap), set the key in the configuration the server returns, because a value set only on the device leaves the browser off. If you manage the app from the Enterprise Admin Console, [turn it on from the console](#manage-the-built-in-browser-from-the-enterprise-admin-console) instead.

### Restrict which sites Claude can open

[`builtinBrowserDefaultDomainPolicy`](/docs/third-party/claude-desktop/configuration#builtinbrowserdefaultdomainpolicy) decides whether Claude can open every site except the ones you block, or only the sites you allow.

| Value            | Behavior                                                                                                                                                  |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Unset or `allow` | Claude can open every site except the entries in [`builtinBrowserBlockedDomains`](/docs/third-party/claude-desktop/configuration#builtinbrowserblockeddomains) |
| `block`          | Claude can open only the entries in [`builtinBrowserAllowedDomains`](/docs/third-party/claude-desktop/configuration#builtinbrowseralloweddomains)              |

For example, this configuration lets Claude open only a documentation site and a wiki:

```json theme={null}
{
  "builtinBrowserEnabled": true,
  "builtinBrowserDefaultDomainPolicy": "block",
  "builtinBrowserAllowedDomains": ["docs.example.com", "wiki.example.com", "*.wiki.example.com"]
}
```

If you use `block`, also list the hosts that your allowed sites load scripts, images, and data from, because every page in the pane loads content only from sites the policy allows. To keep the default `allow` policy and block specific sites instead, list them in `builtinBrowserBlockedDomains`, for example `["example.com", "*.example.org"]`. A hostname entry also covers its `www.` form but no other subdomain, and a `*.` wildcard covers every subdomain but not the bare domain. The [configuration reference](/docs/third-party/claude-desktop/configuration#builtinbrowseralloweddomains) lists the full entry format.

The site policy restricts Claude, not the user. A user can still type a blocked site's address and open the page. The pane then shows the banner "This site is blocked by your organization's policy" and Claude's tools stay off on that page. The page loads content only from its own site and from sites the policy allows, so under `block` it often renders incompletely.

If [`coworkEgressAllowedHosts`](/docs/third-party/claude-desktop/configuration#coworkegressallowedhosts) lists specific hosts, Claude can open only sites on that list in the built-in browser, even when the browser's own site lists allow more.

The example is plain JSON, which is the form a [bootstrap server](/docs/third-party/claude-desktop/bootstrap) response and the Linux managed file use. For a macOS profile or the Windows registry, encode the same values as the [Value types](/docs/third-party/claude-desktop/configuration#value-types) section describes.

### Manage the built-in browser from the Enterprise Admin Console

If you manage the app from the [Enterprise Admin Console](/docs/third-party/claude-desktop/admin-console), you control the built-in browser from the console instead of with these keys. In **Organization settings** on claude.ai, open the **Capabilities** page in the **Desktop 3P** section. Under **Built-in browser**, turn on the **Allow the built-in browser** switch. The change takes effect when users restart Claude Desktop. Also allow `releases.claude.com` through your firewall, because Claude Desktop contacts it for the [site safety check](#site-safety-check).

Once the switch is on, **Browser site permissions** appears below it. Click the **Manage site permissions** button to choose whether Claude can act on every site except the ones you block, or only on the sites you allow, and add those sites in the same dialog. These are the same site permissions [Claude in Chrome](#claude-in-chrome) uses, and changes to them apply without a restart.

## Site safety check

Claude in Chrome and the built-in browser both check public website addresses against Anthropic's site safety list. Anthropic retains basic Claude in Chrome safety check logs, containing the user's account ID, IP address, timestamp of the request, and their OS/Chrome version. No URL, page content, prompt content, or anything else about the request is stored. For the built-in browser, the account ID is empty unless your organization uses the Enterprise Admin Console, because only a console-managed app sends the check as a signed-in user.

## Related

* [`builtinBrowserEnabled` in the configuration reference](/docs/third-party/claude-desktop/configuration#builtinbrowserenabled)
* [Web search and web fetch](/docs/third-party/claude-desktop/web-tools)
* [Telemetry and egress](/docs/third-party/claude-desktop/telemetry)
* [Deploy with Enterprise Admin Console](/docs/third-party/claude-desktop/admin-console)
