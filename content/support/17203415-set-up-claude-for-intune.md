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

To confirm it worked, in the Microsoft Entra admin center go to Enterprise applications, open "Claude for Intune (Public)", and select Permissions. "Microsoft Mobile Application Management" should be listed on the "Admin consent" tab. If it isn't, select "Grant admin consent" on that page.

**Note:** Employees signing in to Claude for Intune with "Continue with Microsoft" does not grant this consent; an Entra admin has to grant it.

If employees are signed out within a few seconds of signing in, this step has most likely not been completed. After granting admin consent, ask them to delete Claude for Intune, reinstall it, and sign in again.

To require app protection at sign-in, target the Conditional Access rule at "All resources" with Grant = Require app protection policy. A rule that names only Office 365 or Claude SSO does not cover Claude for Intune. Microsoft Authenticator must be installed on the device.

## Add Claude for Intune in the Microsoft Intune admin center

### 1. Install Claude for Intune on employees’ devices

How employees get Claude for Intune depends on how their iPhone or iPad is managed:

- **Personal devices not enrolled in Intune (app protection only):** You don’t need to add or assign the app in Intune. Employees install Claude for Intune from the App Store (it appears there as "**[Claude Intune](https://apps.apple.com/us/app/claude-intune/id6812855318)**") and sign in with "Continue with Microsoft." Your app-protection policy (step 2) applies after they sign in.

  - Optional: to also list it in Company Portal, add it as an iOS store app and assign the user group as "Available with or without enrollment."

- **Devices enrolled with Apple User Enrollment:** Employees install Claude for Intune from the App Store themselves. Intune can’t install an app added as an "iOS store app" on these devices, and Company Portal shows "This device needs to be managed before you can install apps."

- **Company-owned devices enrolled in Intune:** Add Claude for Intune as an iOS store app and assign it to a user or device group using the steps below. Employees install it from Company Portal, or you can make the assignment Required to push it to their devices.

To add Claude for Intune for enrolled company-owned devices:

1. In the Microsoft Intune admin center, select "Apps" from the left side navigation panel:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700192269/ce2bf95a18aba11042da50f4c1ad/dda0f9a2-d585-4b09-ae4f-a1ff70b1e010?expires=1792941300&amp;signature=41e800d21e32080f188eb08131bb0b70ab07a1a775c957f51a21a14fdde0ec31&amp;req=dicnFsh3n4NZUPMW1HO4ze7khjPY5mpjAMLV2Uu0R4Vo55ZLQUTcSj793pdY%0AHyPK%0A)

2. Under Platforms, select "iOS/iPadOS":

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700195036/b70c6c0bdeff5f2b72568ef4943b/67cc834c-5e91-42da-9d3b-1f32c8dd8c05?expires=1792941300&amp;signature=733ecc43716da8ec023903eb3f6eee8581fb062e37e50f641d92b8d9a1f46687&amp;req=dicnFsh3mIFcX%2FMW1HO4zeH1oU%2FutXKXQ7hR7Wh%2Bi72%2FMqC8dN1JmBdnxT0O%0A8H%2Be%0A)

3. Click "+ Create." For the App type, select the "iOS store app," and click the "Select" button on the bottom:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700195791/9a01290b4189e6a39c473af0a448/cfed06da-f35a-4b22-b687-286ea48864c1?expires=1792941300&amp;signature=92a00344778ba2ba7ed9cc8a120273f8e9c36734ae8b5c2d205187a365500cd5&amp;req=dicnFsh3mIZWWPMW1HO4zTni3cQgZp8v2SRx6amjj9HGM%2FnOWbgAkYE7I9Lg%0Alxyl%0A)

4. Search "Claude for Intune" and click the "Select" button on the bottom.

5. In **App Information**, set **Minimum operating system** to iOS 18, then click the "Next" button:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700196458/588327ab209e9524c45111a244a1/258697c2-2f82-471b-9104-2bccb1b01614?expires=1792941300&amp;signature=fc8fcace520a3b33771eb6e6b29786ce4f3244d2f91017e6d2eaf21af8f45ae6&amp;req=dicnFsh3m4VaUfMW1HO4zbxl5YpeczMtDNNSLAHCCFpuovuEp4gxaNHlBFiX%0Ap9FV%0A)

6. For **Assignments**, add the groups that should get the app: under Required to install it automatically, or under Available for enrolled devices so employees can install it from Company Portal. You can use user groups or device groups.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2741107114/8f15b0d179a54c2ca4effaad8577/55bed25a-4b20-47b0-9e89-7f8adc86c04f?expires=1792941300&amp;signature=791fc7fe5e2e14c398ef4b9d211c056ab44cc337247d0fbedb47812dbaaf6324&amp;req=dicjF8h%2BmoBeXfMW1HO4zYaZMeq1ffKdmN%2B6UXepdg8MFUW990yT0TTnHzSq%0AfynB%0A)

7. Click "Next," review and create.

8. If you assigned the app as Required, it installs automatically; if Available, employees install it from Company Portal.

### 2. Apply an app-protection policy to Claude for Intune

1. In the Microsoft Intune admin center, select "Apps" from the left side navigation panel:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700190760/9f6412fe68632cffee29826f7d30/42fdeb30-64af-4089-a976-5094bb6b8292?expires=1792941300&amp;signature=56dd5760215d72a0da938691543a6856c57994e0f7b88c1062d5cf7c2301685a&amp;req=dicnFsh3nYZZWfMW1HO4zQwrZIgLV9M%2FLtTCoSp4D6oqSZxyDhhyWkaJqlo1%0AG6Vp%0A)

2. Under **Manage apps**, select "Protection":

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700200858/a7ddd4265aeb6d61a7a096297cd5/fc9a1fe2-3d0e-4038-9b2c-f96bd19e4020?expires=1792941300&amp;signature=2ab7fc7cf1bae68926706effb7337228b75178333f0cbee89dde94089ddfaacd&amp;req=dicnFst%2BnYlaUfMW1HO4zeBHXB008fzunJWY0xu8hzLfQdO8Fv2G8aZmbV3K%0Apzl7%0A)

3. Click "+ Create" and then select "iOS/iPadOS":

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700201382/6240e257b2b498b5fa5ac1111561/11ef4f59-aba1-4d2b-ac58-9aec1dd60a4d?expires=1792941300&amp;signature=e315db124f3ef4d6f3a1aaa83c51846585c2838a11dba8ee90c540e2ee11f219&amp;req=dicnFst%2BnIJXW%2FMW1HO4zc89y0lfBntNV2VWh%2B9zzEo%2FMgPRTl6t6f2wcslM%0AZY8l%0A)

4. Enter Name in the **Basics** tab, then click "Next" to **Apps**. Set **Target policy to** "Selected apps." Click "+ Select custom apps":

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700201929/2edf45cedc0bc03204f86d01a49e/4d96c12d-962b-43f6-8b3f-668e3247d4c1?expires=1792941300&amp;signature=7287eb38948487c657da4dffc96e07c55ce258857039029db17e76c1607f030a&amp;req=dicnFst%2BnIhdUPMW1HO4zVmMRJMdVzwLKETwku7gMssBfWEcjHwT4DqEdSxD%0AU7sB%0A)

5. Type in the bundle ID `com.anthropic.claudeforintune`. Select it so it appears under **Selected Apps** before clicking "Select":

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700202816/3565aea2d1b9c22a5f8d105825c5/3de6d241-6259-463e-a503-a6ca9f2095e0?expires=1792941300&amp;signature=6b7d2dc3053c6224bd07870c8041182f30ccbb7119655aef2a0d5e0c5df1b996&amp;req=dicnFst%2Bn4leX%2FMW1HO4zf6tYiEhzKt012LT9vQL0W4KC9pWkJqlDTInx4kl%0AJVln%0A)

6. In Apps, confirm the bundle ID now appears under **Custom apps** before clicking "Next":

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700203780/24ed354ef0de87bf0a0c1bc129a1/46eed662-f488-48ee-a4d1-8a9a76079884?expires=1792941300&amp;signature=55f3344c94f02a99aec8b8a3acabc9ffa92bd5e48dcb6bc238faef53be213653&amp;req=dicnFst%2BnoZXWfMW1HO4zQd95NeD38nc8F6Cfy2R7u9qwdrj06%2By2aseU5gN%0Aek5K%0A)

7. Configure the Data protection, Access requirements, and Conditional launch settings as needed.

8. In the **Assignments** tab, assign the policy to a user group that includes everyone who will use Claude for Intune—app-protection policies can only target user groups, not device groups. Make sure it also applies to unmanaged devices: don't limit it to Intune-managed devices with the device-type setting or an assignment filter, or employees on personal phones get signed out right after signing in*.*

9. Review and create.

10. The app only becomes "managed" after the user signs in with org credentials post-install (may require a restart).

## Tell employees which app to install

Claude for Intune and the standard Claude app are separate apps. Your Intune app-protection policies apply to Claude for Intune.

Wherever your organization requires Intune protection, tell employees on managed or employee-owned iPhones and iPads to install **[Claude for Intune](https://apps.apple.com/us/app/claude-intune/id6812855318)**, not the standard Claude app.

## Before Microsoft lists Claude for Intune as a protected app

Claude for Intune doesn't yet appear in Microsoft's list of protected apps, so you can't search for it when you create an app-protection policy. Until it's listed, add it to your policy by entering its bundle ID manually:

1. Follow the steps in **[Apply an app-protection policy to Claude for Intune](#h_5fda0300e8).**

2. When you select apps, choose "Select custom apps" and enter the bundle ID `com.anthropic.claudeforintune`.

After Microsoft adds Claude for Intune to its protected apps list, you'll select it from the list of public apps instead of using "Select custom apps."