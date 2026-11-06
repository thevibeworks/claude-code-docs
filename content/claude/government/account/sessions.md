> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Sessions

> See every place you are signed in to Claude for Government, sign any of them out, and check how long sessions last and what ends them.

> **Who this is for:** Anyone with a Claude for Government account.

A session is created each time you sign in, whether that is in a web browser or in one of the Claude applications. The **Sessions** tab lists your active sessions and lets you sign out of any of them remotely.

## What each row shows

Each row is one active sign-in, and shows which kind of application it is for, how it was established, and when it started. The one you are using right now is labeled **this session**. These are some of the ways a session is established:

* **Single sign-on** means you authenticated through your agency's identity provider.
* **Device pairing** means a sign-in from a Claude application was approved in a browser, linking that application to your account.
* **Email link** means a one-time link was sent to your inbox and followed to sign in. Only Primary Owners and tenant administrators can [sign in this way](https://claude.com/docs/government/tenant-admin/identity-and-access.md#emailed-sign-in-link).

## What is not shown

The list does not include IP addresses, locations, device names, or browser details. You can tell a browser session from an application session and you can see when each one started, but you cannot tell two browser sessions apart by device.

## How long sessions last

Sessions expire after a period of inactivity, and using a session extends it. Your agency or organization sets the idle timeout, which is 24 hours unless they have changed it. After about that long without use, that browser tab or application prompts you to sign in again the next time it tries to do anything.

Your agency or organization can set a maximum session length in addition to the idle timeout. When a session reaches that length, it expires even if you have been using it the whole time, and the browser tab or application prompts you to sign in again. Sessions that expire either way drop off this list automatically.

Sessions can also end early, for example in these ways:

* You sign one out from this page.
* You use the **Sign out** button in the page footer, which ends the session you are currently using.
* An administrator signs you out everywhere, which ends every session you have.
* Your agency moves you to another organization, which ends the sessions you already have.
* An administrator deactivates your account or your organization, which immediately invalidates every session you have.

You can have up to six active sessions in each Claude application, such as Claude Desktop. You can also have up to three browser sessions in total. If a new sign-in goes over one of these limits, Claude for Government ends your session of the same kind that expires soonest.

## Signing out of other sessions

* To end one session, select **Sign out** on its row.
* To end everything except the one you are using, select **Sign out *N* other sessions** below the list.

Neither of these affects the session you are currently using, and there is no confirmation prompt; the session is revoked as soon as you select the button.

### What actually happens when you sign out another session

The other browser or application is not sent a live message, but the very next thing it tries to do (load a page, send a message, or refresh) will be refused and it will be returned to the sign-in screen. A request that was already in flight at the instant you revoked may finish, but nothing new can start.

Signing out another session from this page does not touch your agency's single sign-on session, so if the person at that other computer tries to sign back in, the identity provider may still let them straight through without re-entering a password. If that is a concern (for example, you left a shared computer signed in), sign the session out here first, then contact your agency's identity team to end the single sign-on session.

## If you see a session you don't recognize

Sign it out from here right away. You can use **Sign out *N* other sessions** if you want to be certain you have cleared everything. If an unrecognized session reappears after you have done so, or anything else about the list looks wrong, report it to your organization's administrator so they can investigate through your agency's identity system.
