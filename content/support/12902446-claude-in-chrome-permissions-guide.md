Title: Claude in Chrome Permissions Guide

URL Source: https://support.claude.com/en/articles/12902446-claude-in-chrome-permissions-guide

Markdown Content:
This guide explains how to control what Claude can access and do when using Claude in Chrome. Understanding permissions helps you balance productivity with security.

## Permission Modes

Claude in Chrome uses a multi-layered permission system to give you control over what Claude can access and do. When you first open the extension, you'll see a drop-down menu on the chat input. Click this to choose between two permission modes:

[![Image 1](https://downloads.intercomcdn.com/i/o/lupk8zyo/1843322018/f8c0ae21b449f32e71696c76a17a/7656f295-e802-4a72-9e60-94611501f920?expires=1781694900&signature=1a56c9d2eef2e2aa2e2e79dd7107f506757d5b5234eed44b65de65bbc0a6f3f1&req=dSgjFcp8n4FeUfMW1HO4zQ5tySYK%2FHy%2BhD0gAzkS2hxxzp6TrY4zo4nM5RtY%0AoHXv9tPNU4rx43hWB74%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1843322018/f8c0ae21b449f32e71696c76a17a/7656f295-e802-4a72-9e60-94611501f920?expires=1781694900&signature=1a56c9d2eef2e2aa2e2e79dd7107f506757d5b5234eed44b65de65bbc0a6f3f1&req=dSgjFcp8n4FeUfMW1HO4zQ5tySYK%2FHy%2BhD0gAzkS2hxxzp6TrY4zo4nM5RtY%0AoHXv9tPNU4rx43hWB74%3D%0A)

## Ask before acting

Choose “Ask before acting” to have Claude create a plan from your prompt, which you can approve and allow Claude to execute. The plan will specify which websites you’re allowing Claude to access, as well as the approach it will follow:

[![Image 2](https://downloads.intercomcdn.com/i/o/lupk8zyo/1843320727/8d1c859ae9b8e0cdb536d024bf40/9bc3d239-8eb6-4bae-a032-a236f88ee606?expires=1781694900&signature=f848ab25f8c324fb978151a42ed219b329adaeef2c588be173af221cc5311019&req=dSgjFcp8nYZdXvMW1HO4zYqyZcNL9Ya%2BgN0ADj5oqFARzChlezZMOAKh9fgw%0A1hEfMUAYpXd8IcnTw8k%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1843320727/8d1c859ae9b8e0cdb536d024bf40/9bc3d239-8eb6-4bae-a032-a236f88ee606?expires=1781694900&signature=f848ab25f8c324fb978151a42ed219b329adaeef2c588be173af221cc5311019&req=dSgjFcp8nYZdXvMW1HO4zYqyZcNL9Ya%2BgN0ADj5oqFARzChlezZMOAKh9fgw%0A1hEfMUAYpXd8IcnTw8k%3D%0A)

Note that Claude will only use the websites listed in the plan, so you’ll need to manually approve any additional access requests.

Claude clarifies which sites it’s planning to access and the actions it will take upfront, allowing you to review the proposed plan and ensure it’s correct before starting. You can also click “Make changes” to reject the current proposal, then prompt Claude again to make any necessary changes. Once you click “Approve plan,” Claude will be able to act independently within the outlined parameters, but will still check with you before taking certain irreversible actions, like making a purchase, creating an account, or downloading a file. Claude will not deviate from the stated plan without requesting your permission first. There are certain actions that Claude cannot take for your security, such as bypassing bot authorizations, executing trades, permanently deleting files, or taking certain actions that may indicate a prompt injection risk (see [Prohibited Actions](https://support.claude.com/en/articles/12902446-claude-in-chrome-permissions-guide#h_e199f8f523)).

## Act without asking

"Act without asking" is a **high-risk mode** that allows Claude to operate with near-complete autonomy on the internet. Even in this mode, Claude should ask before:

However, due to the nature of LLMs, we can't guarantee that Claude will request permission to take these actions, so exercise caution when using this mode.

Only allow Claude in Chrome to act without asking when:

You remain fully responsible for all actions Claude takes when using this mode.

## When does Claude need to request additional permissions?

There are some websites on which Claude requires approval for every action. If you navigate to one of these sites, a **Permission required** prompt will appear in the extension side panel where Claude will ask for permission before accessing the page or taking any action.

[![Image 3](https://downloads.intercomcdn.com/i/o/lupk8zyo/1847222875/162eb012ebe473ed2b852b97e223/0209db51-6057-4ec4-a9b7-8358287d46a3?expires=1781694900&signature=b5a0553941b8bb153f8549903ad5ac65d0d4d7c9824547febecab42c2d863edb&req=dSgjEct8n4lYXPMW1HO4zeoCY8ctqnB2JCxYSFHKWIgnNek%2Bc0tegoq9Od4r%0Anoe9ZL1mnkcNn2EBJtA%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/1847222875/162eb012ebe473ed2b852b97e223/0209db51-6057-4ec4-a9b7-8358287d46a3?expires=1781694900&signature=b5a0553941b8bb153f8549903ad5ac65d0d4d7c9824547febecab42c2d863edb&req=dSgjEct8n4lYXPMW1HO4zeoCY8ctqnB2JCxYSFHKWIgnNek%2Bc0tegoq9Od4r%0Anoe9ZL1mnkcNn2EBJtA%3D%0A)

### Permission options

**"Allow this action"** grants permission for a single action only. Claude will ask again for the next action on this site. **This is the safest option when using the extension** as you can review and approve each of Claude's actions.

**"Always allow actions on this site"** grants ongoing permission for this website. Claude can take multiple actions without asking each time. Only use this for sites you completely trust. Claude may take unintended actions across the website when granted this permission.

**"Decline"** prevents Claude from taking this action. You can try a different approach or skip this task.

### Protected actions

When you choose "Always allow actions on this site," Claude still asks for your explicit approval before:

### Managing site permissions

You can manage Claude's access to specific sites in the extension settings. Click the Claude extension icon, then the three dots in the upper right corner of the side panel. Select "Settings" → "Permissions" to:

## Organization-level controls (Team and Enterprise plans)

Team and Enterprise admins can configure additional controls that affect permissions:

If you're unable to access a site with Claude, your organization may have restricted access. Contact your admin for more information, or see [Claude in Chrome Admin Controls](https://support.claude.com/en/articles/13065128-claude-for-chrome-admin-controls).

## Actions Requiring Explicit Permission

Regardless of your permission mode, Claude requires explicit user permission to perform any of the following actions:

## Prohibited Actions

To protect you, Claude is prohibited from taking following actions regardless of permissions:

* * *

Related Articles

[Get started with Claude in Chrome](https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome)[Claude in Chrome Troubleshooting](https://support.claude.com/en/articles/12902405-claude-in-chrome-troubleshooting)[Using Claude in Chrome safely](https://support.claude.com/en/articles/12902428-using-claude-in-chrome-safely)[Claude in Chrome admin controls](https://support.claude.com/en/articles/13065128-claude-in-chrome-admin-controls)[Use Claude Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)
