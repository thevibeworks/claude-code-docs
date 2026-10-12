# Set up Claude for Intune

Claude for Intune is a managed version of Claude for iOS for organizations that use Microsoft Intune. This article explains how Intune admins add Claude for Intune in the Microsoft Intune admin center and which app to tell employees to install.

## What is Claude for Intune?

Claude for Intune is built for organizations that manage mobile devices with Microsoft Intune, including organizations that let employees work from personal iPhones and iPads.

- Claude for Intune is a separate app from the standard Claude app. Both are listed on the App Store.

- IT teams can apply Intune app-protection policies to Claude for Intune on company-owned and employee-owned iPhones and iPads.

- It signs in with Microsoft only.

- It supports Intune app-protection policies and Microsoft Entra Conditional Access.

## Requirements

Before you set up Claude for Intune, check that you meet these requirements:

- You have an Enterprise plan.

- Your organization uses Microsoft Intune, and you have access to the Microsoft Intune admin center.

- Employees sign in to Claude for Intune with Microsoft. Other sign-in methods aren't available in Claude for Intune.

- You’re using iOS or iPadOS version 18.0 or later.

- Anthropic has enabled Microsoft sign-in for your organization's email domains.

- If you use Conditional Access, Claude for Intune is registered in your Microsoft Entra tenant.

- An admin in your Microsoft Entra tenant has granted admin consent for Claude for Intune. This is required for every organization.

## Get your organization ready

### 1. Ask Anthropic to enable Microsoft sign-in

Before employees can sign in to Claude for Intune, Anthropic needs to enable Microsoft sign-in for your organization's email domains. Contact your Anthropic account team or support, and tell them which email domains your employees use to sign in.

### 2. Register Claude for Intune in your Entra tenant

Before employees can sign in, an admin in your Microsoft Entra tenant needs to grant admin consent for Claude for Intune. This is required for every organization. It approves the permission Claude for Intune uses to work with Microsoft Intune app protection, and it registers the app in your tenant so you can select it in a Conditional Access policy.

**Grant admin consent.** A tenant admin opens the following URL, replacing {organization} with your tenant ID or domain: `https://login.microsoftonline.com/{organization}/adminconsent?client_id=bb747f0e-002b-4882-9960-916fe00a2b90`

To confirm it worked, in the Microsoft Entra admin center go to Enterprise applications, open "Claude for Intune (Public)", and select "Permissions." **Microsoft Mobile Application Management** should be listed on the "Admin consent" tab. If it isn't, select "Grant admin consent" on that page.

**Note:** Signing in at claude.ai with "Continue with Microsoft" does not grant this consent.

If employees are signed out within a few seconds of signing in, this step has most likely not been completed. After granting admin consent, ask them to delete Claude for Intune, reinstall it, and sign in again.

To require app protection at sign-in, target the Conditional Access rule at “All resources” with Grant = Require app protection policy. A rule that names only Office 365 or Claude SSO does not cover Claude for Intune. Microsoft Authenticator must be installed on the device.

## Add Claude for Intune in the Microsoft Intune admin center

### 1. Add Claude for Intune to your managed apps and make it available to BYOD devices.

1. In the Microsoft Intune admin center, select “Apps” from the left side navigation panel:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700192269/ce2bf95a18aba11042da50f4c1ad/dda0f9a2-d585-4b09-ae4f-a1ff70b1e010?expires=1791837000&amp;signature=2da883f300832e1b529254bc4dd216e6eebe4d2b13124bfdccd6779f31e7e7cf&amp;req=dicnFsh3n4NZUPMW1HO4ze7khjDZ4WxgAMLV2Uu0R4UMtzolbLt1cWA8PYZt%0AA3v4%0A)

2. Under Platforms, select “iOS/iPadOS”:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700195036/b70c6c0bdeff5f2b72568ef4943b/67cc834c-5e91-42da-9d3b-1f32c8dd8c05?expires=1791837000&amp;signature=bbc42974736d08672a7f4dd7b9fc802bc4ade44027c1faf9431c3efe7ddcef31&amp;req=dicnFsh3mIFcX%2FMW1HO4zeH1oUzvsnSUQ7hR7Wh%2Bi70mXpbSeh6Ef9zMtU%2BT%0AHRb%2F%0A)

3. Click “+ Create.” For the App type, select the “iOS store app,” and click the “Select” button on the bottom:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700195791/9a01290b4189e6a39c473af0a448/cfed06da-f35a-4b22-b687-286ea48864c1?expires=1791837000&amp;signature=11931bd9c0be877f1d75dac20d44f0a66d2adaefd04f9a211f0e8d3664d87975&amp;req=dicnFsh3mIZWWPMW1HO4zTni3cchYZks2SRx6amjj9F7gmb0xMqc0dHdru7I%0AFfJ9%0A)

4. Search “Claude for Intune” and click the “Select" button on the bottom.

5. In **App Information**, set **Minimum operating system** to iOS 18, then click the “Next” button:

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700196458/588327ab209e9524c45111a244a1/258697c2-2f82-471b-9104-2bccb1b01614?expires=1791837000&amp;signature=7d52f86e05697a0b5e92561f4c82bc4d8a47eed20c86c6e71be091ad2986a45d&amp;req=dicnFsh3m4VaUfMW1HO4zbxl5YlfdDUuDNNSLAHCCFpUpaI8ZRiVK9%2Fxg9O%2B%0AhBrC%0A)

6. For **Assignments**, add a group of users to make it available in their device’s Company Portal:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700197715/bf5aa327b41f994fdafe04869300/f4c6c9cf-51df-4d75-bf8a-b144d11dd380?expires=1791837000&amp;signature=ea3b863c180e2c03cd242240851b973c10f5c70e96bee2d7b4451ef2df6e5498&amp;req=dicnFsh3moZeXPMW1HO4zeVx8DQR4iuNoVYQxJ7ndH4ISFihbeeYsmlj%2FMeN%0AyYkF%0A)

7. Click “Next,” review and create.

8. Users have to download the app from Company Portal on their devices for access.

### 2. Apply an app-protection policy to Claude for Intune.

1. In the Microsoft Intune admin center, select “Apps” from the left side navigation panel:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700190760/9f6412fe68632cffee29826f7d30/42fdeb30-64af-4089-a976-5094bb6b8292?expires=1791837000&amp;signature=3146782097aed4a68100b22cc566cb10ba8a8ffb63a38ec8336d9da4d0c4c07a&amp;req=dicnFsh3nYZZWfMW1HO4zQwrZIsKUNU8LtTCoSp4D6o%2FV38GjHw0k14orAuo%0AWUuC%0A)

2. Under **Manage apps**, select “Protection”:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700200858/a7ddd4265aeb6d61a7a096297cd5/fc9a1fe2-3d0e-4038-9b2c-f96bd19e4020?expires=1791837000&amp;signature=9f4ae3846a695186f957f25d65b05aea7941097bc9710dae9ba88baa0a0d8271&amp;req=dicnFst%2BnYlaUfMW1HO4zeBHXB419vrtnJWY0xu8hzJGYtK6qE01HbwsLlZR%0A6SSU%0A)

3. Click “+ Create” and then select “iOS/iPadOS”:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700201382/6240e257b2b498b5fa5ac1111561/11ef4f59-aba1-4d2b-ac58-9aec1dd60a4d?expires=1791837000&amp;signature=43df1421e80ae9899b7e5646fb72d8d1bebb56f308c8982ce6a063cce0cd32e2&amp;req=dicnFst%2BnIJXW%2FMW1HO4zc89y0peAX1OV2VWh%2B9zzEqJR%2BBDNXqafrI6cBdg%0AfTlR%0A)

4. Enter Name in the **Basics** tab, then click “Next” to **Apps**. Set **Target policy to** “Selected apps.” Click “+ Select custom apps”:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700201929/2edf45cedc0bc03204f86d01a49e/4d96c12d-962b-43f6-8b3f-668e3247d4c1?expires=1791837000&amp;signature=d0f9c6237d4b02785b3f6c03b4ece9883fe6462ed11ee969f6c5c5ceecb76fa5&amp;req=dicnFst%2BnIhdUPMW1HO4zVmMRJAcUDoIKETwku7gMsvLpbaSz2NZWo3loRzX%0APqE%2B%0A)

5. Type in the bundle ID `com.anthropic.claudeforintune`. Select it so it appears under **Selected Apps** before clicking “Select”:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700202816/3565aea2d1b9c22a5f8d105825c5/3de6d241-6259-463e-a503-a6ca9f2095e0?expires=1791837000&amp;signature=5c1c233bba2094d80baf20a86666bb2b163ce90800743f0675e52559dc0236d7&amp;req=dicnFst%2Bn4leX%2FMW1HO4zf6tYiIgy61312LT9vQL0W71DtWjD0LhcnGLynZn%0AKu7a%0A)

6. In Apps, confirm the bundle ID now appears under **Custom apps** before clicking “Next”:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700203780/24ed354ef0de87bf0a0c1bc129a1/46eed662-f488-48ee-a4d1-8a9a76079884?expires=1791837000&amp;signature=1bd9a98b2c524c21121778528c52b122654c7dd037b37a5954cb05787df0ce84&amp;req=dicnFst%2BnoZXWfMW1HO4zQd95NSC2M%2Ff8F6Cfy2R7u8u8nXxw%2FQjLClILzQk%0AZ9AE%0A)

7. Configure the Data protection, Access requirements, and Conditional launch settings as needed.

8. In the **Assignments** tab, add a user group to assign the policy to them.

9. Review and create.

10. The app only becomes "managed" after the user signs in with org credentials post-install (may require a restart).

## Tell employees which app to install

Claude for Intune and the standard Claude app are separate apps. Your Intune app-protection policies apply to Claude for Intune.

Wherever your organization requires Intune protection, tell employees on managed or employee-owned iPhones and iPads to install **[Claude for Intune](https://apps.apple.com/us/app/claude-intune/id6812855318)**, not the standard Claude app.

## Before Microsoft lists Claude for Intune as a protected app

Claude for Intune doesn't yet appear in Microsoft's list of protected apps, so you can't search for it when you create an app-protection policy. Until it's listed, add it to your policy by entering its bundle ID manually:

1. Follow the steps in **[Apply an app-protection policy to Claude for Intune](#h_5fda0300e8).**

2. When you select apps, choose “Select custom apps” and enter the bundle ID `com.anthropic.claudeforintune`.

After Microsoft adds Claude for Intune to its protected apps list, you'll select it from the list of public apps instead of using “Select custom apps.”