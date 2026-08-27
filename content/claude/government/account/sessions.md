> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Sessions

> Use this page to see every place you are currently signed in to Claude for Government and to sign out of any of them remotely.

> **Who this is for:** Anyone with a Claude for Government account.

Use this page to see every place you are currently signed in to Claude for Government and to sign out of any of them remotely.

A session is created each time you sign in, whether that is in a web browser or in the Claude desktop application. This page lists your active sessions so you can confirm that nothing unexpected has access to your account, and clean up after yourself on a computer you no longer have.

## What each row shows

Each row is one active sign-in. The one you are using right now is labeled **this session** and always appears at the top of the list; the rest are ordered with the most recent first.

* **Client** tells you which kind of application the sign-in is for. It shows **Browser** for a web sign-in, or **Desktop app** for the Claude application installed on a computer.
* **via …** tells you how that session was established. **Single sign-on** means you authenticated through your agency's identity provider. **Device pairing** means a code shown in the desktop application was entered and approved in a browser, linking that application to your account. **Email link** means a one-time link was sent to your inbox and followed to sign in.
* **Signed in** tells you when the session started. The time is shown in your local time zone along with a relative hint such as "2 days ago".

## What is not shown

To limit how much information about your devices is held in the system, the list deliberately does not include IP addresses, locations, device names, or browser details. You can tell a browser session from a desktop session and you can see when each one started, but you cannot tell two browser sessions apart by device. When in doubt, sign out anything you cannot positively account for; signing back in is quick.

## How long sessions last

Sessions expire after a period of inactivity, and using a session extends it. Once you have been inactive for longer than the idle timeout, that browser tab or desktop application prompts you to sign in again the next time it tries to do anything. Your agency or organization sets the idle timeout, which is 24 hours unless they have changed it.

Your agency or organization can set a maximum session length in addition to the idle timeout. When a session reaches that length, it expires even if you have been using it the whole time, and the browser tab or desktop application prompts you to sign in again. Sessions that expire either way drop off this list automatically.

Sessions can also end early in three ways: you sign one out from this page, you use the **Sign out** button in the page footer to end the session you are currently using, or an administrator deactivates your account or your organization, which immediately invalidates every session you have.

## Signing out of other sessions

<Note>
  These controls only appear when you have sessions besides the one you are using. If this is your only sign-in, the list shows just the current session and no sign-out buttons.
</Note>

* To end one session, select **Sign out** on its row.
* To end everything except the one you are using, select **Sign out *N* other sessions** below the list.

Neither of these affects the session you are currently using, and there is no confirmation prompt; the session is revoked as soon as you select the button. To sign out of the session you are using right now, use the **Sign out** button in the page footer instead.

### What actually happens when you sign out another session

The sign-out is recorded the moment you select the button. The other browser or desktop application is not sent a live message, but the very next thing it tries to do (load a page, send a message, or refresh) will be refused and it will be returned to the sign-in screen. In practice this means the other session is cut off within seconds of any activity. A request that was already in flight at the instant you revoked may finish, but nothing new can start.

Signing out another session from this page does not touch your agency's single sign-on session, so if the person at that other computer tries to sign back in, the identity provider may still let them straight through without re-entering a password. If that is a concern (for example, you left a shared computer signed in), sign the session out here first, then contact your agency's identity team to end the single sign-on session, or change your directory password.

<Tip>
  Signing out here versus signing out from the footer behave differently at the identity provider. The footer **Sign out** ends both your Claude for Government session and your single sign-on session, so you will be asked for credentials the next time you visit. The per-row **Sign out** on this page ends only the Claude for Government session and leaves single sign-on alone.
</Tip>

## If you see a session you don't recognize

Sign it out from here right away. You can use **Sign out *N* other sessions** if you want to be certain you have cleared everything. If an unrecognized session reappears after you have done so, or anything else about the list looks wrong, report it to your organization's administrator so they can investigate through your agency's identity system.
