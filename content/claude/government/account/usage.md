> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Usage

> Check how much of your Claude allowance you have used and when it resets, and what to do when you hit a usage limit or your organization runs out of credits.

> **Who this is for:** Anyone with a Claude for Government account.

To check how much of your Claude allowance you have used, sign in to the [web portal](https://claude.com/docs/government/account/overview.md) in your browser and open the **Usage** tab.

> [!NOTE]
>
> In Claude Desktop 4.23118.0 or later, you can also go to **Settings > Usage**. Under **Your usage limits**, **Current session** is your 5-hour window and **Weekly limit · All models** is your 7-day window.

## How limits work

Your seat tier (the allowance package an administrator has assigned to you) gives you two windows that run at the same time:

* The **5-hour window** limits how much you can use in a short burst.
* The **7-day window** limits how much you can use across a whole week.

Both windows refill automatically on their own schedules, so you never need to do anything to get your allowance back.

Usage is not counted in messages. Each message to Claude consumes an amount of your allowance proportional to how much work it takes to answer, so a short question uses very little while a long conversation or a request that produces a lot of output uses more.

If you cancel or close a response while it is still being written, that message still counts against your allowance. If a request fails because of a problem on the service side before Claude starts responding, the allowance it would have used is given back to you automatically.

## When a limit fills up

If **either** window reaches 100%, your Claude access pauses until that window resets. While paused you can still sign in and browse the portal, but you cannot send new messages. While a limit is full, a dot marks the **Usage** tab.

This page shows your personal limits only. If you are on a [self-managed seat tier](https://claude.com/docs/government/org-admin/seat-tiers.md), your organization also draws from a shared credit balance. If that balance runs out or your organization reaches a spend cap your tenant administrator set, you cannot send new messages even though nothing on this page looks full.

In either case, tell your organization owner. A spent balance is resolved by Anthropic adding credits to the account. A reached spend cap clears when the cap resets or when a tenant administrator raises it.

## Reading the reset times

The text beneath each window's label shows its state:

* **Resets …** means the window is running.
* **Starts when a message is sent** means you have not used anything in this window yet.
* **Resets on next request** means the window's time has already passed but you have not sent anything since. You are not actually limited in this state even if the bar looks full.

The page does not refresh on its own while you have it open. Select the refresh icon next to **Last updated** to pull the latest figures.

## If you keep hitting limits

Your organization owner can move you to a seat tier with a larger allowance. When an administrator changes your seat tier, the usage you have already accumulated in each window carries over; what changes is the size of the allowance it is measured against. On a self-managed seat tier, your organization owner can also [reset your usage limits](https://claude.com/docs/government/org-admin/users.md#reset-usage-limits).

## If the page says "No seat tier assigned"

You do not have a seat yet, so there is no allowance to show and you cannot send messages to Claude. Ask your organization owner to assign you one.
