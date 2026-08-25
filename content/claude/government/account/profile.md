> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Account

> Use this page to confirm that you are signed in as the right person and to see what access you have been given.

> **Who this is for:** Anyone with a Claude for Government account.

Use this page to confirm that you are signed in as the right person and to see what access you have been given.

The **Account** tab is the landing page of the user area. It shows the basics of your account in one place: your name and avatar at the top, followed by four fields that describe your access. Everything on this page is read-only. The values come from your agency's identity system and from settings that an administrator controls, so this page is for checking your details rather than changing them.

## What you'll see

| Field            | What it means                                                                                                                                                                                                                                                                                                                                                                          | Where it comes from                                                  |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Email**        | The address you sign in with. It is the unique identifier for your account, and notifications such as sign-in links are sent to it.                                                                                                                                                                                                                                                    | Your agency's identity provider.                                     |
| **Organization** | The organization you belong to within your agency's tenant. A tenant is your agency's overall space in Claude for Government, and it can contain several organizations (for example, one per bureau or office). Your organization determines which administrators manage your access and which usage pool your activity draws from.                                                    | Set when your account was created or when directory sync placed you. |
| **Role**         | What you are allowed to manage. **User** means you can use Claude but do not administer anything. **Owner** means you can manage your organization's users, seats, and settings. **Primary Owner** is the same as Owner with a few additional safeguards: a primary owner cannot be removed by other owners, and each organization can have at most three of them.                     | Assigned by an organization owner or by directory sync.              |
| **Seat tier**    | The allowance you have been given. A seat tier is a named package that sets two things for you: how much Claude usage you get (shown on the [Usage](/docs/government/account/usage) tab) and which Claude models you are allowed to use. The tiers themselves, their names, and what each one includes are defined by your agency, so the name you see here is specific to your deployment. | Assigned to you by an organization owner.                            |

The name and avatar at the top come from your agency's directory. The avatar is generated from your name; you cannot upload a custom picture.

## How to change these details

None of these fields can be edited on this page. Where to go instead depends on the field:

* **Name or email.** These are owned by your agency's identity provider or directory. Update them there, and the change flows into Claude for Government automatically the next time you sign in or the next time directory sync runs. You do not need to do anything inside Claude for Government.
* **Organization.** Users cannot move themselves between organizations. If you have been placed in the wrong organization, ask your organization's owner or a tenant administrator to move you.
* **Role.** An organization owner can promote or demote users between **User** and **Owner** in the administrative area. Ask your organization's owner if your role needs to change.
* **Seat tier.** An organization owner assigns and changes seat tiers from the administrative area. See the next section if yours is missing.

<Tip>
  If you are helping a colleague troubleshoot, ask them to read out this page. It tells you in one screen which organization they are in, what role they hold, and whether they have a seat, which is usually enough to diagnose a "Claude is not working for me" report.
</Tip>

## If your seat tier says "No seat assigned"

<Note>
  This section only appears when you do not have a seat tier. If a tier name is shown in the Seat tier field, you can skip this section.
</Note>

Without a seat tier you can sign in and see the portal, but you cannot send any messages to Claude, and the [Usage](/docs/government/account/usage) tab will show "No seat tier assigned" instead of your allowance. This is the expected state for a brand-new account that has not yet been given a seat, or for an account whose seat was deliberately removed.

Ask your organization's owner to assign you a seat. Once they do, the tier name appears here immediately and you can start using Claude straight away without signing out and back in.

> **For organization owners:** When you view your own profile with no seat, the page links you straight to **Admin → Users** so you can assign yourself one. Being an owner does not give you a seat by itself, because administrative access and Claude usage are granted separately. If your organization has no seats at all yet and nobody in it holds a seat, members without a seat tier are seated automatically when its first seats are allocated, Primary Owners first.
