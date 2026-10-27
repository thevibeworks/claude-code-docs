---
title: What happens when you rotate, disable, or delete your encryption key
url: https://platform.claude.com/docs/en/manage-claude/cmek-key-lifecycle
description: What each action on your key does to your data, how soon, and whether you can undo it.
---

With customer-managed encryption keys (CMEK), your key lives in your key management service (KMS), and Claude keeps a record that points to it. Deleting the key and deleting the record are different actions.

## What each action does

<Frame>
  ![Key states: attaching is one-way, a disabled key can be re-enabled, and Anthropic can't recover data once the key is deleted.](https://platform.claude.com/docs/images/cmek/key-states.svg)
</Frame>

| Action                                                                              | What happens                                                                                                                                                                                                                                                                                                                     | Can you undo it?                                                                                                                                          |
| ----------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Attach the key to a workspace (on Claude Enterprise, add it to the organization)    | Your key protects data written [after it takes effect](https://platform.claude.com/docs/en/manage-claude/cmek-how-it-works#when-your-key-takes-effect). On Claude Platform, attaching also locks the workspace’s [data retention setting](https://platform.claude.com/docs/en/manage-claude/cmek-data-retention#data-retention). | No. The key can’t be removed or replaced.                                                                                                                 |
| Rotate the key material within the same key                                         | You rotate it in your KMS, on your own schedule. Rotation needs no action in Claude.                                                                                                                                                                                                                                             | Nothing to undo. Keep earlier key versions enabled.                                                                                                       |
| Disable the key, or remove (revoke) Anthropic’s access to it                        | The change can take up to 1 hour to apply, and requests in flight during that hour might still succeed. After that, Claude can’t read or write the data the key protects, and requests fail.                                                                                                                                     | Re-enable the key or restore Anthropic’s access. [Two limits apply](https://platform.claude.com/docs/en/manage-claude/cmek-key-lifecycle#restore-access). |
| Delete the key in your KMS, schedule it for deletion, or destroy its key material   | Anthropic can’t recover the data the key protects.                                                                                                                                                                                                                                                                               | Not by Anthropic. It keeps no copy of your key.                                                                                                           |
| Delete the key’s record in Claude (**Delete encryption key** in the Claude Console) | You can do this only while no workspace, including an archived one, uses the key.                                                                                                                                                                                                                                                | No.                                                                                                                                                       |

## What disabling does, and what comes back

While the key is disabled, Messages API requests in a workspace that uses it return [a 400 error with the code `cmek_key_disabled`](https://platform.claude.com/docs/en/manage-claude/cmek-troubleshooting#cmek-key-disabled).

Re-enabling the key, or restoring Anthropic’s access to it, brings back access to the data the key protects. Two limits apply. Requests that failed while the key was disabled aren’t retried. Disabling the key doesn’t pause retention periods.

## If Anthropic can’t reach your key

Requests that store data under your key fail while Anthropic can’t reach it, for example during an outage of your KMS. On Claude Enterprise, these requests include messages in chat and in voice mode.

On the Messages API, these requests return a 503 error with the code `cmek_key_unreachable`, and you can retry them. The Message Batches API retries them for you until your key is available or the batch expires.

## Change keys or stop using CMEK

A workspace or organization can’t switch to a different key or go back to having none. On Claude Platform, you can create a new workspace with a different key, or with no key, and move your traffic to it. On Claude Enterprise, there’s no way to change keys or stop using CMEK within the organization.
