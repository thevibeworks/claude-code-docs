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

**Note:** Employees signing in to Claude for Intune with "Continue with Microsoft" does not grant this consent; an Entra admin has to grant it.

If employees are signed out within a few seconds of signing in, this step has most likely not been completed. After granting admin consent, ask them to delete Claude for Intune, reinstall it, and sign in again.

To require app protection at sign-in, target the Conditional Access rule at “All resources” with Grant = Require app protection policy. A rule that names only Office 365 or Claude SSO does not cover Claude for Intune. Microsoft Authenticator must be installed on the device.

## Add Claude for Intune in the Microsoft Intune admin center

### 1. Add Claude for Intune to your managed apps and make it available to BYOD devices.

1. In the Microsoft Intune admin center, select “Apps” from the left side navigation panel:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700192269/ce2bf95a18aba11042da50f4c1ad/dda0f9a2-d585-4b09-ae4f-a1ff70b1e010?expires=1792044000&amp;signature=19877fd7c9267bb5edb4cf7d859ecdbf90e5d24e7dd93b06b1e846d27e8c5310&amp;req=dicnFsh3n4NZUPMW3nq%2BgeEhD2I1c%2Fvi9FV9%2FRCGJ8F%2BbG70hSiisXiES26N%0AZ8jvVtb4twvevx9POKHTDAERmqQ%3D%0A)

2. Under Platforms, select “iOS/iPadOS”:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700195036/b70c6c0bdeff5f2b72568ef4943b/67cc834c-5e91-42da-9d3b-1f32c8dd8c05?expires=1792044000&amp;signature=1aa67a4192b6e1cfa092c4400132c275a242cbb8af01ad02a6f4ba4cc72c5b85&amp;req=dicnFsh3mIFcX%2FMW3nq%2BgfGOegmD3ywb6%2F9K0uXwHwo7Olj88Gqqx1cPkSR7%0AvOWsi%2BKoBpCj5Wis7g9SxT9b7EE%3D%0A)

3. Click “+ Create.” For the App type, select the “iOS store app,” and click the “Select” button on the bottom:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700195791/9a01290b4189e6a39c473af0a448/cfed06da-f35a-4b22-b687-286ea48864c1?expires=1792044000&amp;signature=77dcfe25617b68f0b8f22daf023be201220bdf5a860446207f008a847ad4c6a4&amp;req=dicnFsh3mIZWWPMW3nq%2BgbjlrI2ZS5IwX3Rw34L3DNb6PageVZ%2BqQoINl7Zs%0Amglet5kjrVug9YGlc%2F7iRdQUnxA%3D%0A)

4. Search “Claude for Intune” and click the “Select" button on the bottom.

5. In **App Information**, set **Minimum operating system** to iOS 18, then click the “Next” button:

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700196458/588327ab209e9524c45111a244a1/258697c2-2f82-471b-9104-2bccb1b01614?expires=1792044000&amp;signature=38d77d7e2e89794b6184bfd312ae365e70fdc278b59606dff4ba40506af057ab&amp;req=dicnFsh3m4VaUfMW3nq%2BgRCtAWs2Bzv7ON%2FLUUaTNb5lmwEUjWN2VCqZ%2Fzk1%0AGHMbadv09VmOp1pLnP5kFt4Ur4E%3D%0A)

6. For **Assignments**, add a group of users to make it available in their device’s Company Portal:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700197715/bf5aa327b41f994fdafe04869300/f4c6c9cf-51df-4d75-bf8a-b144d11dd380?expires=1792044000&amp;signature=f557fbedf802369db81a4d7b047cf0dca987257f5c2376b6882328cee5dd2433&amp;req=dicnFsh3moZeXPMW3nq%2BgWgNNUH7GckSM%2FOW8V8G8eeWPtk1CtFqRlz5oz3h%0AxIF%2F6hIhQo%2BM4Q%2B2%2BbsEE3Ja5Ro%3D%0A)

7. Click “Next,” review and create.

8. Users have to download the app from Company Portal on their devices for access.

### 2. Apply an app-protection policy to Claude for Intune.

1. In the Microsoft Intune admin center, select “Apps” from the left side navigation panel:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700190760/9f6412fe68632cffee29826f7d30/42fdeb30-64af-4089-a976-5094bb6b8292?expires=1792044000&amp;signature=00eb258f39e1c7124330be66464d2dcce971dcd30f8ddaca2c2867c982003bfb&amp;req=dicnFsh3nYZZWfMW3nq%2BgcnP38ikpzDk%2Fs1v3OwcHgzeDXlHq1SjcAcFuum3%0Ai5alWnFkPyu3pTq1b6QGkEsHf7A%3D%0A)

2. Under **Manage apps**, select “Protection”:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700200858/a7ddd4265aeb6d61a7a096297cd5/fc9a1fe2-3d0e-4038-9b2c-f96bd19e4020?expires=1792044000&amp;signature=88d9d7aadfbb57aaa402475c1ecb3f8805030bc9555546ce6bd4bdfddade53f0&amp;req=dicnFst%2BnYlaUfMW3nq%2BgVfUh4EkSq091YCc5VZwMOasQa4YdPzSpCPNEwWo%0AZZlEbCV6kVTPVCGOuVDJ57tKNdI%3D%0A)

3. Click “+ Create” and then select “iOS/iPadOS”:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700201382/6240e257b2b498b5fa5ac1111561/11ef4f59-aba1-4d2b-ac58-9aec1dd60a4d?expires=1792044000&amp;signature=592824a0987b8bf9d52843ab68efb488d3df678fbecede525172b49fcdf03c9c&amp;req=dicnFst%2BnIJXW%2FMW3nq%2Bgcl7Oct5XHUf5ZDbLzCpE1st9T7auVcE3OFJsIQI%0A%2Fo3g%2F8LT35bwuaEfaUzq%2BooUxTs%3D%0A)

4. Enter Name in the **Basics** tab, then click “Next” to **Apps**. Set **Target policy to** “Selected apps.” Click “+ Select custom apps”:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700201929/2edf45cedc0bc03204f86d01a49e/4d96c12d-962b-43f6-8b3f-668e3247d4c1?expires=1792044000&amp;signature=49bb5fd49bc7356ac0c7fc545147dcf0684e3b57201bf600028bd2e2da9b41eb&amp;req=dicnFst%2BnIhdUPMW3nq%2BgR4ZYiD6igpEXYtJt4FTesx1pAUQfm2PjmKj3zVd%0A4OeV4aojHX6ErA6xxikOvQUBRKI%3D%0A)

5. Type in the bundle ID `com.anthropic.claudeforintune`. Select it so it appears under **Selected Apps** before clicking “Select”:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700202816/3565aea2d1b9c22a5f8d105825c5/3de6d241-6259-463e-a503-a6ca9f2095e0?expires=1792044000&amp;signature=b1359697b29145990beb82720a8980755808ef6ff035dcdec3bf0600b27c7e69&amp;req=dicnFst%2Bn4leX%2FMW3nq%2BgXDRvmM1OfrTOBlfeK8rUbrvl6owfyaCYo8aT0Lj%0ACNzA3al9HWA57991MBzDE0LUcQw%3D%0A)

6. In Apps, confirm the bundle ID now appears under **Custom apps** before clicking “Next”:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700203780/24ed354ef0de87bf0a0c1bc129a1/46eed662-f488-48ee-a4d1-8a9a76079884?expires=1792044000&amp;signature=b42a75e740fdab6fd7d2f6c2190d2b0bb036c026f08425620cd6b7766e629dd0&amp;req=dicnFst%2BnoZXWfMW3nq%2Bge%2BjBE5lQI1FUbHrU6V7f5MKvFsHovN1m5GQRVge%0AJFRB6GabhugcBcl00ZNOrC8PV2Y%3D%0A)

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