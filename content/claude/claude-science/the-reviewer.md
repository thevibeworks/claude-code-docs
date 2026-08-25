> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# The reviewer

> A built-in verification step that independently re-reads Claude's recent responses, the approved plan, saved artifacts, and the execution record, then checks whether its claims match what ran.

The reviewer is a built-in verification step that independently re-reads Claude's recent responses, the approved plan, saved artifacts, and the execution record, then checks whether Claude's claims match what actually ran. It runs automatically after responses and periodically during long work, and you can trigger it any time with **Request review**. Automatic review is on by default on Max, Team, and Enterprise plans; on the Pro plan it starts off, and you can turn it on per session.

## Examples of what the reviewer checks

* A result reported as computed when nothing ran.
* A value in the response that contradicts the file it came from.
* A citation that doesn't support the claim attributed to it.
* A reference whose DOI resolves to a different article.
* An approved plan step that wasn't completed.
* A conclusion not supported by the method used.

This isn't a complete list. The reviewer checks whether claims match the record; it doesn't re-run analyses. It can flag a conclusion that doesn't follow from the method that was run, but it doesn't judge whether that method was the right choice for your research question. Go to Settings > Specialists to customize the Reviewer or create your own specialist to perform additional reviews and judgments customized to the way you work.

## How Claude responds to findings

If the reviewer finds something, a **Reviewer · N findings** card appears in the conversation. Each finding shows the claim, the evidence, and a link into the transcript. Claude reads the findings and addresses them in its next message, either by correcting the work or by explaining why the finding doesn't apply. You can open the reviewer's full reasoning from the card.

## Adding your own review criteria

In **Settings** > **Specialists**, open **Reviewer** and add checks in the **Instructions** field. Your criteria are added to every review; they can't remove or weaken built-in checks.

## Controls

Auto-review is a per-session toggle in the session settings menu. It starts on for Max, Team, and Enterprise plans and off for the Pro plan. Reviews run against your plan's usage.
