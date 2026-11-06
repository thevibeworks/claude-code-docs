# Use Personal Finance in Claude

Personal Finance lets you link your bank, credit card, loan, and investment accounts to Claude, so you can see your balances and spending on one page and ask Claude questions about your own money. This article shows you how to set up Personal Finance, link and unlink banks, and see what Claude can access.

This feature is in beta on Pro, Max, and Ultra plans in the US only. It’s available on Claude, Claude Desktop, Claude for iOS, and Claude for Android, and it isn’t available on Free, Team, or Enterprise plans. We’re rolling it out gradually, so you might not see it yet.

Personal Finance can only read your accounts. It can’t move, manage, or invest your money. Claude uses Plaid, a network that connects apps to banks. With Plaid, you can authenticate your financial account, so Claude doesn't ask for or see your bank password. Learn more in **[How your data is used](#h_6b21c7ac44)**.

**Note:** Claude is AI and can make mistakes. Learn more in **[How Claude answers questions about your money](#h_b6a51ba950)**.

## What you can do in Personal Finance

- **See your money on one page.** Widgets show your spending, cash flow, accounts, subscriptions, upcoming bills, and short insights from Claude. You can add, edit, remove, and reorder them.

- **Ask Claude.** Type a question on the Personal Finance page, select a suggested question, or ask in a regular chat. For example, “Where did my money go last month?” or “Which subscriptions am I paying for?”

## Set up Personal Finance and link your bank

Follow these steps to set up Personal Finance and share your accounts with Claude:

1. Open Claude on the web, Claude Desktop, or the mobile app.

2. Open “Personal Finance” in the side menu. If you don’t see it, hover over **More**.

3. Select “Get started.”

4. Choose your goals, or skip them.

5. Select “Continue.”

6. Select “Link accounts with Plaid.”

7. On “Connect Plaid to Claude,” review what Claude will be able to access.

8. Select “Continue.”

9. In Plaid, choose your bank, sign in to it, and choose the accounts that you want to share.

10. Back in Claude, wait for your accounts to show, then select “Link another account” or “Done.”

**Note:** Plaid opens in a new window (web), in your default browser (Claude Desktop), inside the app (iOS), or in a browser tab (Android). Finish within 10 minutes, then return to Claude right away. Transactions can take a few minutes to sync.

## Link another bank

You can link up to 16 banks. When you reach the limit, you’ll need to unlink a bank before you can link another one.

- **Web and Claude Desktop:** Click “Link another account” at the top of the page.

- **iOS and Android:** Tap the gear icon in the top right of the page, then tap “Link another account.”

To add an account at a linked bank, link the bank again and share every account you want Claude to read.

## If Claude says the bank is already linked

Choose one of these options:

- **Switch to the new link:** The new sign-in replaces the old one, and Claude reads only the accounts you shared this time. Choose this to add an account or fix a bank.

- **Keep it as it is:** Claude keeps your existing link and doesn’t link anything new.

- **Keep both:** Choose this for a second login at the same bank, such as a joint or business account. If an account is in both logins, Claude counts it once when your bank shows it the same way under each login. If your bank shows it differently, it may be counted twice in your totals.

## What Claude can access

For the accounts you choose to share, Claude can read:

- Bank names

- Account names, types, and last four digits

- Balances and credit limits

- Up to 24 months of transactions, including the amount, date, merchant, category, and your bank’s description

**Account numbers:** Plaid gives Claude only the last few digits of each account number (usually four). If your bank writes a full number into an account’s name or a transaction’s description, Claude may see it there.

**Investments, loans, and cards:** Claude reads balances and credit limits, not holdings, trades, rates, or terms. Plaid’s own screens may also ask for your consent to share investment, credit, and loan data. Today, Claude reads only the kinds of data listed above.

## How your data is used

- **Your permission:** By connecting Plaid, you’re giving your permission to share certain data with Claude. The list is in the **[What Claude can access](#h_fa85d6ccb2)** section above.

- **Your bank login:** Claude uses Plaid to connect to your bank. You sign in through Plaid, so Claude doesn't ask for or see your bank password.

- **How Claude uses your financial data:** We use this data to respond to your requests. When you chat with Claude in the Personal Finance hub, those conversations aren't used to train our models. For anything you share with Claude outside the hub, your privacy settings apply. The data appears in your conversation and stays in your chat history until you delete the chat, subject to our data retention practices. The service providers that host Claude for us also handle bank data. Plaid handles it under its own terms and privacy policy.

- **How to stop:** Unlink a bank, and Claude stops reading it (see **[Unlink a bank](#h_8c27edcfa3)**). You can also disconnect Claude at **[my.plaid.com](https://my.plaid.com)**.

For more information, see the **[Anthropic Privacy Policy](https://www.anthropic.com/legal/privacy)** and the **[Plaid Privacy Policy](https://plaid.com/legal/#end-user-privacy-policy)**. Learn more about our **[data handling and retention](https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data)**.

## How Claude answers questions about your money

- **What Claude reads:** Claude uses Plaid to read your bank account balances and transactions. It uses that data to answer your questions about your money.

- **Personal Finance can only read your accounts.** It can’t move, manage, or invest your money.

- **Claude is AI and can make mistakes.** Check important figures against your bank’s own app or statements. Learn more about **[incorrect or misleading responses](https://support.claude.com/en/articles/8525154-claude-is-providing-incorrect-or-misleading-responses-what-s-going-on)**.

- **A figure can differ from your bank’s.** Balances can be a day or two old. An account you link through two logins may be counted twice. While Claude can’t read a bank, the page’s spending figures leave that bank out, so a budget can show more money left than you have.

Personal Finance helps you understand your money, and it isn't designed to give investment advice.

## Use your accounts in chats

- Claude reads your linked accounts without asking each time, unless you change that (see **Turn Plaid off or on for chats** below). It asks before it links or unlinks a bank in a chat.

- Once Claude has used your accounts in a chat, it's designed not to save anything from that chat to memory or search that chat later. It also leaves it out of your monthly recap, including the title. In that chat, Claude can still show text and tables and make plain text files, such as .csv files. It may not be able to run code or work with Word, Excel, PowerPoint, or PDF files.

- Claude asks before it publishes an artifact from a chat that used your linked accounts. The artifact may include data from your bank accounts. It stays until you delete it, even if you delete the chat.

- A shared chat link shows your messages and Claude’s replies, including any figures from your accounts. It can also show a chart or artifact that Claude made.

- Artifacts can read the linked accounts of the person who opens them, if that person has Personal Finance and allows Plaid. Any figures in an artifact, including saved ones, are shown to everyone who opens it.

## Turn Plaid off or on for chats

- **Web and Claude Desktop:** Click “+” in the message box, click “Connectors,” then switch Plaid off or on.

- **iOS and Android:** Tap “+” next to the message box, then “Connectors,” then “Plaid.” Under “All tools” (on Android, “Set all tools”), choose “Blocked” to turn Plaid off or “Always allow” to turn it back on. With “Needs approval,” Claude asks before each read, unless the chat is set to "Automatically approve." Your choice also applies to new chats.

## Sign in again to a bank

Banks sometimes end Claude’s access. The bank then shows “Sign-in expired” or “Claude’s access to this bank has ended.” To restore access:

1. Navigate to **[Personal Finance](https://claude.ai/personal-finance)**.

2. Open your linked accounts. On the web and Claude Desktop, click the three-dot menu (“...”) at the top of the page, then click “Manage linked accounts.” On iOS and Android, tap the gear icon.

3. Select “Sign in again” on the bank.

4. Sign in with the same bank login you used to link it.

When it works, you see “Claude can read [bank] again” and your dashboard stays as it was.

## Unlink a bank

Follow these steps to unlink a bank:

1. Navigate to **[Personal Finance](https://claude.ai/personal-finance)**.

2. Open your linked accounts. On the web and Claude Desktop, click the three-dot menu (“...”) at the top of the page, then click “Manage linked accounts.” On iOS and Android, tap the gear icon.

3. Select “Unlink” on the bank. On iOS and Android, tap the bank first to open it.

4. Select "Unlink" again to confirm.

When you unlink a bank:

- Claude stops reading your accounts at this bank.

- Every account you linked with that bank login is unlinked. You can’t unlink a single account.

- What Claude already said stays in your chats, and in any artifacts or shared links until you remove them. You can link the bank again later.

**Important:** If it’s your last linked bank, your dashboard resets too. Your widgets, their settings (such as budgets), and your setup answers are deleted, and this can’t be undone.

## Stop using Personal Finance

To stop using Personal Finance, unlink every bank:

1. Navigate to **[Personal Finance](https://claude.ai/personal-finance)**.

2. On the web and Claude Desktop, click the three-dot menu (“...”) at the top of the page, then click “Manage linked accounts.” On iOS and Android, tap the gear icon.

3. Select “Unlink all banks.”

You can also disconnect Claude at **[my.plaid.com](https://my.plaid.com)**, Plaid’s own site for your connections. Learn more in **[Plaid’s steps](https://support-my.plaid.com/hc/en-us/articles/4420193428503-How-do-I-disconnect-my-financial-accounts-from-an-app)**.

If you lose a device, log it out. Learn more about **[managing your active sessions](https://support.claude.com/en/articles/13124001-managing-your-active-sessions)**.

## If your plan ends or you delete your account

When your paid plan ends, you can’t open Personal Finance, and Claude can’t read your accounts in chats. Your banks stay linked until you unlink them.

- **Before your plan ends:** Unlink your banks if you don’t plan to come back.

- **If you subscribe again:** Your banks and dashboard are as you left them. A bank may ask you to sign in again.

- **If you move to a Team or Enterprise organization:** Claude unlinks your banks when you start the move.

## Unlink your banks after your plan has ended

1. On the web, click “Customize” in the sidebar (some accounts see “Plugins” instead).

2. Click “Connectors.”

3. If “Plaid” is listed, open it, click the button that starts with “Unlink,” and confirm.

4. If “Plaid” isn’t listed, disconnect Claude at **[my.plaid.com](https://my.plaid.com)** or contact Support. Learn more in **[Plaid’s steps](https://support-my.plaid.com/hc/en-us/articles/4420193428503-How-do-I-disconnect-my-financial-accounts-from-an-app)**.

## If you plan to delete your Claude account

When you delete your account, Claude unlinks your banks automatically. This happens after the deletion is processed.

## Current limitations

- You can link US banks only.

- Claude can’t use your linked accounts in scheduled tasks, Cowork tasks, or Claude Code, and may not be able to use them in a project.

- Personal Finance isn’t available in Claude Duet.

- Data exports don’t yet include your saved Personal Finance dashboard.

## Troubleshooting

| **What you see**                                         | **What to do**                                                                                                                                                                                                                                                                                                                                                                                            |
| -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| No “Personal Finance” in the sidebar or side menu        | Check your plan, use your personal account (not a Team or Enterprise account), and update the app. Outside the US, or on a VPN that connects from another country, Personal Finance doesn’t appear until you’re back (your banks stay linked). It may also not be on for your account yet.                                                                                                                |
| “Nothing new was linked.” or “[Bank] is already linked.” | Claude found no new account. To add one, link the bank again, and in Plaid share that account and every other account you want Claude to read.                                                                                                                                                                                                                                                            |
| A link from Claude Desktop or Android fails              | Finish in the browser that Claude opened, and don’t reload Plaid’s page. From Claude Desktop, that browser must be signed in to Claude with the same account.                                                                                                                                                                                                                                             |
| You linked a bank, but it isn’t in your linked accounts  | Wait a minute or two, then open Personal Finance again. If the bank still isn’t there, Claude didn’t save it. Link the bank again, finish within 10 minutes, don’t close Plaid yourself, and return to Claude right away.                                                                                                                                                                                 |
| Transactions are missing                                 | A new bank can take a few minutes to sync. If the bank asks for a new sign-in, select “Sign in again.” If nothing has loaded a day after you linked the bank, link it again (if Claude asks, choose “Switch to the new link”) or wait for the bank.                                                                                                                                                       |
| “Claude can’t read this bank.”                           | Don’t unlink it first. Link the bank again with “Link another account.” If Claude asks, choose “Switch to the new link” (or “Keep both” if that isn’t offered). If the old entry is still listed afterward, unlink it then. The one exception: if you already have 16 banks, unlink this bank first, then link it again.                                                                                  |
| Claude doesn’t use your accounts in a chat               | On iOS or Android, update the app. Then ask Claude to use your linked accounts, and **[check that Plaid is on](#h_78c4f737c1)**. You can also start a new chat outside of a project: a chat that already ran code or made files, or that started from an artifact, can’t use your accounts. If it still doesn’t work in the app, go to claude.ai in a browser and start a new chat with the same account. |

## Get help

On the web, click your initials or name in the lower left corner, then click “Get help.” Learn **[how to get support](https://support.claude.com/en/articles/9015913-how-to-get-support)**.

**Important:** Don’t share your bank login or full account numbers with anyone, including Support.