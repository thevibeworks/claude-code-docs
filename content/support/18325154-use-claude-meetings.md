# Use Claude Meetings

Claude Meetings, now in beta, lets you add Claude to a Google Meet call as a visible participant. It takes the notes, answers questions, and builds artifacts, such as docs, whiteboards, and slides, live during the call. This article shows you how to add Claude to a call, work with it during the call, and find everything afterward.

Claude Meetings is rolling out in beta on Team and Enterprise plans in Claude and Claude Desktop. While it's in beta, it isn't available to some organizations, including those with zero data retention (ZDR), HIPAA-ready configuration, or customer-managed encryption keys (CMEK).

On Team plans, Claude Meetings is on by default, and an owner can turn it off. On Enterprise plans, an owner turns it on for all or part of the organization. To turn it on for part of the organization, an owner uses custom roles. Learn more about **[managing custom roles](https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans)**.

## Add Claude to a call

**Important:** Before you add Claude or turn on auto-join, make sure everyone on your call is okay with being transcribed.

1. Go to **[Meetings](https://claude.ai/meetings)** in Claude.

2. Connect your Google Calendar. An owner must enable Google Calendar for your organization first.

3. Select a meeting on your calendar.

4. Click "Add Claude."

Claude joins a meeting when someone adds it or has auto-join on. To change your auto-join setting, go to **[Settings > Capabilities](https://claude.ai/meetings#settings/capabilities) > Meetings > Auto-join**. You can add Claude to all your meetings or all your meetings except one-on-ones. Owners can't set auto-join for you.

Claude usually joins without having to ask. If it does ask, the host can let it in. If the host declines, Claude doesn't try that call again unless someone adds it, and you'll see that it was declined.

## During the call

- To ask Claude something, say "Claude" and then ask your question, or type it in the Meet chat. By default, Claude answers in writing in the Meet chat.

- To build something together, say "Claude, make a doc" or "Claude, make a whiteboard." Anyone on your team can ask, and Claude attaches each one to the meeting page. You can add as many as you like, and all artifact types are supported.

- Claude can use your connected tools during the call, like sending a Slack message. It uses each person's connected tools with that person's permission. It asks the first time, and a yes applies going forward. For now, when someone asks out loud, Claude asks each time to confirm who's speaking. When Claude needs your approval, the request appears in the Meet chat when possible. If it needs to confirm your Claude account, the request appears on the meeting page.

- To see what Claude is doing, look at its tile in the call. It's live and shows Claude's current state.

- To pause Claude, ask it to stop listening or use the meeting page. To resume, use the meeting page.

- To have Claude leave, ask it to leave, or select "Remove Claude" on the meeting page. If you add Claude again, it returns to the same meeting page. Claude can stay for up to eight hours and warns you before it leaves.

- To open the meeting page, select the link Claude posts in the Meet chat when it joins. The page has the live transcript, the chat, and everything Claude has made.

**Note:** Anything Claude posts in the Meet chat is visible to everyone on the call. The chat on the Claude meeting page is internal to the organization so outside guests can't see it.

## After the call

After the meeting, the meeting page has the notes, including a summary and any action items, along with the transcript and everything you made. People from your organization on the invite get a recap email with a link to it.

People from your organization on the invite can see the notes and edit what Claude made, and the meeting page can be shared with others in your organization.

The calendar in **Meetings** shows your past and upcoming meetings, so you can go back to any meeting Claude joined or add Claude to the next one.

After the meeting, in a regular chat, you can ask Claude about past meetings you have access to.

## Calls with outside guests

On Team plans, Claude can join calls with outside guests by default, and an owner can turn this off. On Enterprise plans, an owner must allow it first.

### When outside guests aren't allowed

By default, Claude is set to stay out of calls when someone from outside your organization is invited, and to leave if someone from outside, including another company's notetaker bot, joins partway through.

### When outside guests are allowed

An owner can allow Claude on calls with outside guests. On calls with outside guests, Claude listens and takes notes, and posts its notice in the call's chat but doesn't reply there. What guests say is included in the notes and transcript. Live docs, whiteboards, and chat are on the meeting page, and guests don't get that page or the recap email. Each person also has their own **Meetings with external guests** setting in **[Settings > Capabilities](https://claude.ai/meetings#settings/capabilities) > Meetings**.

## Manage Claude Meetings as an owner

Owners and Primary Owners manage Claude Meetings in **[Organization settings > Products > Claude Meetings (beta)](https://claude.ai/admin-settings/meetings)**. On Enterprise plans, a custom role with Owner access can also open this page.

- **Claude Meetings:** Off (the default on Enterprise plans), on for roles that include Meetings, or on for everyone (the default on Team plans).

- **Meetings with external guests:** Internal meetings only (the default on Enterprise plans) or allowed (the default on Team plans).

- **Members' connectors in meetings:** Controls whether Claude can use members' connected tools during meetings.

On Enterprise plans, you can also control access by custom role with the **Claude Meetings** and **Meetings with external guests** capabilities.

## Privacy and your data

When Claude joins, it appears as a participant and posts a notice in the call's chat. It saves a transcript, summary, and screen descriptions, not audio.

## Pricing

Notes, transcripts, and answers that don't use your connected tools are included on Team and Enterprise plans. Docs and whiteboards made in a meeting are free through February 10, 2027. Using your connected tools counts toward your own usage and can lead to charges for your organization.