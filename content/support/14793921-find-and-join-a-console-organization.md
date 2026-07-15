# Find and join a Console organization

Organization discovery lets you find and join your company’s existing Console organization when you start the sign-up flow with a business email address. Instead of creating a personal account, you can request to join—or be added automatically—depending on your organization’s configuration.

**Note:** Organization discovery only applies to organization accounts on the Console, not individual accounts, and must be enabled by an Admin before the capability is available. It’s unavailable for organizations that have single sign-on (SSO) enabled. If your organization uses SSO, your existing provisioning settings remain in effect.

## Admin setup

### Enable discoverability

Admins can manage organization discovery from identity and access settings.

**To enable discoverability:**

1. Log in as an Admin.

2. Navigate to **[Organization settings > Identity and access](http://platform.claude.com/settings/identity)**.

3. Your organization’s domains are listed at the top of the page.

4. Find the domain you want people to search for and click the toggle under **Discoverable**.

5. Find **New member approval** under **Authentication** and choose either “Approve automatically” or “Require admin approval.”

### Configure allowed domains

Admins can specify which email domains are allowed to discover and join the organization by clicking “Add domain” under **Domains** on the identity and access settings page. The organization owner’s domain appears on the **Domains** list automatically. Admins can configure additional allowed domains by adding them to the list, verifying them, and toggling **Discoverable** on. Personal email domains (like Gmail) and .edu domains can’t be added to the list.

### Choose an approval mode

Admins select how join requests are handled:

- **Approve automatically:** People are added to the organization automatically when they ask to join. They can immediately access the workspaces and resources their role permits.

- **Require admin approval:** An admin reviews and approves each join request individually. People aren’t added to the organization until an admin approves the request.

---

## How to find and join an organization

When someone signs up for the Console with a business email address that matches a discoverable organization, they’ll see the option to join during the signup flow. They can choose to join or continue with a personal account.

- If the organization uses “Approve automatically” to handle join requests, they’re added to the Console organization immediately.

- If the organization uses “Require admin approval” for join requests, a request is sent to the admin for review. The requester can choose to continue with a personal account until the request is approved or denied.

If multiple organizations share the same email domain and are all discoverable, the requester sees all of them and can choose which one to join.

---

## Other ways to join an organization

In addition to organization discovery, there are a few other ways to join a Console organization:

- **Email invitation:** An Admin or existing member of the organization may send you an email invitation to join.

- **Admin invitation:** An Admin can add you directly from **[Organization settings > Members](https://platform.claude.com/settings/members)**.

---

## SSO and organization discovery

Organization discovery isn’t available for Console organizations with single sign-on enabled. If your organization uses SSO, the feature doesn’t apply—your existing provisioning settings (including any just-in-time provisioning) remain unchanged. To enable organization discovery, SSO must be turned off first.