> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Usage

> Use this page to see how much of your Claude allowance you have used and when it refreshes.

> **Who this is for:** Anyone with a Claude for Government account.

Use this page to see how much of your Claude allowance you have used and when it refreshes.

Check this page if Claude tells you that you have reached a limit, or if you simply want to see how much headroom you have left before you start a large piece of work.

Claude Desktop does not show how much of your allowance you have used. To check, sign in to the web portal in your browser and open the **Usage** tab.

## How limits work

Your seat tier (the allowance package an administrator has assigned to you) gives you two rolling windows that run at the same time:

* The **5-hour window** limits how much you can use in a short burst.
* The **7-day window** limits how much you can use across a whole week.

Each window shows a progress bar, a percentage from 0% to 100%, and the time it next resets. The bar will never show more than 100% even if your last message pushed you slightly past the line. Both windows refill automatically on their own schedules, so you never need to do anything to get your allowance back.

Usage is not counted in messages. Each message to Claude consumes an amount of your allowance proportional to how much work it takes to answer, so a short question uses very little while a long conversation or a request that produces a lot of output uses more. That is why the page shows a percentage rather than a message count.

If a request to Claude fails because of a problem on the service side, the allowance it would have used is given back to you automatically. If you cancel or close a response while it is still being written, that message still counts against your allowance.

## When a limit fills up

If **either** window reaches 100%, your Claude access pauses until that window resets. While paused you can still sign in, browse the portal, and review past conversations, but you cannot send new messages.

When this happens, you will see a banner at the top of this page telling you which limit you have hit and when it will clear, and the **Usage** tab in the navigation is marked with a pulsing indicator so you can spot it from anywhere in the account area. If both windows happen to be full at the same time, the banner names the one that resets later, since that is the one actually holding you.

<Note>
  The paused banner and the navigation indicator only appear while a limit is actually at 100%. Once the window resets, both disappear on their own.
</Note>

The page also shows your seat tier name in the top right, so you can tell at a glance which allowance you are on. Below the windows there is a **How do these limits work?** link that expands a short plain-language summary, which can be useful when walking a colleague through the page.

<Tip>
  This page shows your personal limits only. If you are on a self-managed seat tier, your organization also draws from a shared credit balance. If that balance runs out or your organization reaches a spend cap your tenant administrator set, Claude will tell you that your organization is out of credits rather than that you have reached a limit, and nothing on this page will look full. A spent balance is resolved by Anthropic adding credits to the account. A reached spend cap clears when the rolling window moves forward or when a tenant administrator raises the cap.
</Tip>

## Reading the reset times

Each window can be in one of three states, and the text beneath its label tells you which:

* **Resets …** means the window is running. You will see a countdown such as "in 2 hr" if the reset is less than a day away, or a date and time if it is further out. Hover over the text to see the other format. Reset times always land on the top of an hour; the clock starts from the hour in which you sent your first message in the window, so your 5-hour window always ends on a round hour rather than at an odd number of minutes.
* **Starts when a message is sent** means you have not used anything in this window yet. The window has no timer at all until you send your first message, at which point the countdown starts and the percentage begins to climb.
* **Resets on next request** means the window's time has already passed but you have not sent anything since. The display may still show the old percentage, but the very next message you send will clear it to 0% and start a fresh window. You are not actually limited in this state even if the bar looks full.

## Keeping the numbers current

The **Last updated** line at the bottom tells you when these figures were fetched. The page does not refresh on its own while you have it open, so if you have been using Claude in another tab or in the desktop application, the numbers here can fall behind. Select the refresh icon next to **Last updated** to pull the latest figures, or simply leave the page and come back.

## If you keep hitting limits

Your organization owner can move you to a seat tier with a larger allowance. The tiers that are available, and what each one includes, are defined by your agency, so ask your administrator which options exist.

When an administrator changes your seat tier, the usage you have already accumulated in each window carries over; what changes is the size of the allowance it is measured against. This means the percentages on this page will jump the moment the change is made: moving to a larger tier makes the same usage a smaller share of the new allowance, so the bars drop, while moving to a smaller tier makes them rise and can put you straight into a paused state if you had already used more than the new tier allows. The windows still reset at the same times they would have before.

Separately from changing your tier, an administrator can also reset your usage windows, which clears both bars to 0% immediately. This is a distinct action that an administrator takes deliberately; it does not happen automatically as part of a tier change.

## If the page says "No seat tier assigned"

<Note>
  This message replaces the whole page and only appears when you do not have a seat. If you can see the progress bars, this does not apply to you.
</Note>

You do not have a seat yet, so there is no allowance to show and you cannot send messages to Claude. Ask your organization owner to assign you one. Once they do, this page will show your limits straight away without you needing to sign out and back in.
