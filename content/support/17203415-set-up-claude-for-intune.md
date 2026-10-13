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

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700192269/ce2bf95a18aba11042da50f4c1ad/dda0f9a2-d585-4b09-ae4f-a1ff70b1e010?expires=1791877500&amp;signature=10aef7e8e4b7a79801106d27d4881443b51398ebffc3d2d69510039f6a67a15f&amp;req=dicnFsh3n4NZUPMW1HO4ze7khjDZ5WxlAMLV2Uu0R4Ug2gD41yfvpwnQQnN2%0AQxbG%0A)

2. Under Platforms, select “iOS/iPadOS”:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700195036/b70c6c0bdeff5f2b72568ef4943b/67cc834c-5e91-42da-9d3b-1f32c8dd8c05?expires=1791877500&amp;signature=fb79e7d95be916a357f983e270286d881cfb74e527b2ec7b8e4c62f2ec2bec39&amp;req=dicnFsh3mIFcX%2FMW1HO4zeH1oUzvtnSRQ7hR7Wh%2Bi73SXWpm8JjuDKSacDf2%0AcCB6%0A)

3. Click “+ Create.” For the App type, select the “iOS store app,” and click the “Select” button on the bottom:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700195791/9a01290b4189e6a39c473af0a448/cfed06da-f35a-4b22-b687-286ea48864c1?expires=1791877500&amp;signature=7fbb96b61fe7f7e14af6b86d2cc12af2c9130d9dd6ce1799a5a10d4c7fded426&amp;req=dicnFsh3mIZWWPMW1HO4zTni3cchZZkp2SRx6amjj9FWMR%2BhdQ91iL6mL3yZ%0Aau0l%0A)

4. Search “Claude for Intune” and click the “Select" button on the bottom.

5. In **App Information**, set **Minimum operating system** to iOS 18, then click the “Next” button:

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700196458/588327ab209e9524c45111a244a1/258697c2-2f82-471b-9104-2bccb1b01614?expires=1791877500&amp;signature=8e46094e5dd8c20110704149fa399922f3d0b6e7bfaccad022bff6c5c7145d80&amp;req=dicnFsh3m4VaUfMW1HO4zbxl5YlfcDUrDNNSLAHCCFp9qqpaCnkvhYhvRvnw%0Ay0DB%0A)

6. For **Assignments**, add a group of users to make it available in their device’s Company Portal:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700197715/bf5aa327b41f994fdafe04869300/f4c6c9cf-51df-4d75-bf8a-b144d11dd380?expires=1791877500&amp;signature=235526dd97283b4f7421d7b80aaf0390efdac455033bf5076461e763a390d40a&amp;req=dicnFsh3moZeXPMW1HO4zeVx8DQR5iuIoVYQxJ7ndH7Nd%2BxMzCYq88hG%2FyZ8%0ArVuv%0A)

7. Click “Next,” review and create.

8. Users have to download the app from Company Portal on their devices for access.

### 2. Apply an app-protection policy to Claude for Intune.

1. In the Microsoft Intune admin center, select “Apps” from the left side navigation panel:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700190760/9f6412fe68632cffee29826f7d30/42fdeb30-64af-4089-a976-5094bb6b8292?expires=1791877500&amp;signature=e0627426f70addd54a99d87e46a15ed10ce389813b979724fd20efa8f352bbb4&amp;req=dicnFsh3nYZZWfMW1HO4zQwrZIsKVNU5LtTCoSp4D6rxBhVDp%2BKM%2BWN1melL%0A96ds%0A)

2. Under **Manage apps**, select “Protection”:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700200858/a7ddd4265aeb6d61a7a096297cd5/fc9a1fe2-3d0e-4038-9b2c-f96bd19e4020?expires=1791877500&amp;signature=5e5af701c83c42928dd8f01387693cd947ef35fe04dc055f4601106c4311f110&amp;req=dicnFst%2BnYlaUfMW1HO4zeBHXB418vronJWY0xu8hzLEywntMg%2FwrhGgLPu3%0A4jdR%0A)

3. Click “+ Create” and then select “iOS/iPadOS”:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700201382/6240e257b2b498b5fa5ac1111561/11ef4f59-aba1-4d2b-ac58-9aec1dd60a4d?expires=1791877500&amp;signature=28d6469bc7799e3d7f02becda7d9aca2380bdc073d2b442a02a2822458872782&amp;req=dicnFst%2BnIJXW%2FMW1HO4zc89y0peBX1LV2VWh%2B9zzEorgwtCw%2Fw0Fd8Xoh6j%0AJk9F%0A)

4. Enter Name in the **Basics** tab, then click “Next” to **Apps**. Set **Target policy to** “Selected apps.” Click “+ Select custom apps”:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700201929/2edf45cedc0bc03204f86d01a49e/4d96c12d-962b-43f6-8b3f-668e3247d4c1?expires=1791877500&amp;signature=7967b8c9b1ad4758031b3bd599e78347216993bef8f371f81d5df18b7f1574ac&amp;req=dicnFst%2BnIhdUPMW1HO4zVmMRJAcVDoNKETwku7gMsvKcjgPTbwhSKeGhB6T%0A7nnm%0A)

5. Type in the bundle ID `com.anthropic.claudeforintune`. Select it so it appears under **Selected Apps** before clicking “Select”:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700202816/3565aea2d1b9c22a5f8d105825c5/3de6d241-6259-463e-a503-a6ca9f2095e0?expires=1791877500&amp;signature=fb5fb503bd453f8d9bba24cd99672f0a1e2574a97d307473ab92e19f6069bbd0&amp;req=dicnFst%2Bn4leX%2FMW1HO4zf6tYiIgz61y12LT9vQL0W4D4tfGK%2BQIaiIiv27C%0AE4Gl%0A)

6. In Apps, confirm the bundle ID now appears under **Custom apps** before clicking “Next”:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700203780/24ed354ef0de87bf0a0c1bc129a1/46eed662-f488-48ee-a4d1-8a9a76079884?expires=1791877500&amp;signature=20e4f7b3220159b35c40600ad218bb5516ade9546e5d07b00032225f73461a05&amp;req=dicnFst%2BnoZXWfMW1HO4zQd95NSC3M%2Fa8F6Cfy2R7u%2BLrMzgee7yXnah1Pt9%0AtaCS%0A)

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