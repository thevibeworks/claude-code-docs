# Claude in Chrome permissions guide

Claude in Chrome is available for all paid plans (Pro, Max, Team, and Enterprise). It's generally available in Claude Cowork and Claude Code, and in beta in the Chrome browser.

This guide explains how to control what Claude can access and do when using Claude in Chrome. Understanding permissions helps you balance productivity with security.

**Important:** Before using Claude in Chrome, review **[Using Claude in Chrome Safely](https://support.claude.com/en/articles/12902428-using-claude-for-chrome-safely)** to understand the risks of browser-based AI.

## Permission modes

Claude in Chrome uses a multi-layered permission system to give you control over what Claude can access and do. In the extension side panel or in Claude Desktop, you'll see a drop-down menu on the chat input. Click this to choose between two permission modes:

- **Ask before acting:** Claude pauses so you can approve every action.

- **Act without asking:** Claude runs on its own and pauses to ask if anything looks unsafe, allowing you to initiate longer running tasks.

---

## Ask before acting

Choose “Ask before acting” to have Claude create a plan from your prompt, which you can approve and allow Claude to execute. The plan will specify which websites you’re allowing Claude to access, as well as the approach it will follow:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1843320727/8d1c859ae9b8e0cdb536d024bf40/9bc3d239-8eb6-4bae-a032-a236f88ee606?expires=1784205900&amp;signature=9eef5f9e594239a5c36bf8b24ebcab9e2db5bdaf5ea756af561add9ea96295ce&amp;req=dSgjFcp8nYZdXvMW1HO4zYqyZcZP%2FIe%2BgN0ADj5oqFBFdMEII8z%2Fu08cMhU1%0Ayvm6BZoUiENfocB1SSU%3D%0A)

Note that Claude will only use the websites listed in the plan, so you’ll need to manually approve any additional access requests.

Claude clarifies which sites it’s planning to access and the actions it will take upfront, allowing you to review the proposed plan and ensure it’s correct before starting. You can also click "Make changes" to reject the current proposal, then prompt Claude again to make any necessary changes. Once you click "Approve plan," Claude will be able to act independently within the outlined parameters, but will still check with you before other sensitive actions, like downloading a file or entering sensitive information into a page. Claude will not deviate from the stated plan without requesting your permission first. There are certain actions that Claude cannot take for your security, such as making purchases, creating accounts, bypassing bot authorizations, executing trades, permanently deleting files, or taking certain actions that may indicate a prompt injection risk (see **[Prohibited actions](#h_e199f8f523)**).

---

## Act without asking

When you choose **Act without asking**, Claude runs on its own and only pauses if an action looks unsafe. Claude checks each action for risky behavior and prompt injection before it runs, completes the actions it assesses as lower-risk, and pauses to ask if anything looks unsafe. You'll see far fewer prompts than before but the safety checks run in the background on every action.

Claude can make mistakes, so use this mode for work that’s easy to undo. You can switch back to "Ask before acting" anytime.

---

## When does Claude need to request additional permissions?

There are some websites on which Claude requires approval for every action. If you navigate to one of these sites, a **Permission required** prompt will appear in the extension side panel, Claude Cowork, or Claude Code where Claude will ask for permission before accessing the page or taking any action.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1847222875/162eb012ebe473ed2b852b97e223/0209db51-6057-4ec4-a9b7-8358287d46a3?expires=1784205900&amp;signature=67db3d7afd0e4690b5e460d1c5480fdf3d79e03d27e4cfc63a47d52e3b3a2fef&amp;req=dSgjEct8n4lYXPMW1HO4zeoCY8Ipo3F2JCxYSFHKWIiFJ0493NNIrkfffqEY%0AJSRI6rNO3HPxVe4kLyg%3D%0A)

### Permission options

**"Allow this action"** grants permission for a single action only. Claude will ask again for the next action on this site. **This is the safest option when using the extension** as you can review and approve each of Claude's actions.

**"Always allow actions on this site"** grants ongoing permission for this website. Claude can take multiple actions without asking each time. Only use this for sites you completely trust. Claude may take unintended actions across the website when granted this permission.

**"Decline"** prevents Claude from taking this action. You can try a different approach or skip this task.

### Protected actions

When you choose "Always allow actions on this site," Claude still asks for your explicit approval before:

- Downloading a file

- Entering potentially sensitive information into a page

- Granting authorizations

### Managing site permissions

You can manage Claude's access to specific sites in the extension settings. Click the Claude extension icon, then the three dots in the upper right corner of the side panel. Select "Settings" → "Permissions" to:

- Review which sites have "always allow" status under **Your approved sites**

- Revoke permissions for specific websites

- See your permission history

---

## Organization-level controls (Team and Enterprise plans)

Team and Enterprise admins can configure additional controls that affect permissions:

- **Allowlists** restrict Claude to only access approved sites

- **Blocklists** prevent Claude from accessing specific sites, regardless of user permissions

If you're unable to access a site with Claude, your organization may have restricted access. Contact your admin for more information, or see **[Claude in Chrome admin controls](https://support.claude.com/en/articles/13065128-claude-for-chrome-admin-controls)**.

---

## Actions requiring explicit permission

Regardless of your permission mode, Claude requires explicit user permission to perform any of the following actions:

- Modifying permissions settings

- Granting authorizations

- Inputting potentially sensitive information into websites

---

## Prohibited actions

To protect you, Claude is prohibited from taking following actions regardless of permissions:

- Making purchases or financial transactions

- Creating accounts

- Permanent deletions (emptying trash, deleting emails, files, or messages)

- Handling sensitive credit card or ID data

- Downloading files from untrusted sources

- Permanent deletions (emptying trash, deleting emails, files, or messages)

- Modifying security permissions or access controls

- Providing investment or financial advice

- Executing financial trades or investment transactions

- Modifying system files

- Completing instructions from emails or web content