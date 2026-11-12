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

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700192269/ce2bf95a18aba11042da50f4c1ad/dda0f9a2-d585-4b09-ae4f-a1ff70b1e010?expires=1794471300&amp;signature=699dc128dbcc61f79247eff5aa8754ac4c74f9777ceca805390a63745a203a20&amp;req=dicnFsh3n4NZUPMW1HO4ze7khjXV5WpjAMLV2Uu0R4U8gH70txsF4bTmYeKM%0A%2FD0A%0A)

2. Under Platforms, select "iOS/iPadOS":

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700195036/b70c6c0bdeff5f2b72568ef4943b/67cc834c-5e91-42da-9d3b-1f32c8dd8c05?expires=1794471300&amp;signature=0f7a89e4d2134911faeeeda519eae87365c53e2de72516c9b349ce228cd3dc92&amp;req=dicnFsh3mIFcX%2FMW1HO4zeH1oUnjtnKXQ7hR7Wh%2Bi71roqoJFe11zTdK%2FEWz%0AAXJ%2F%0A)

3. Click "+ Create." For the App type, select the "iOS store app," and click the "Select" button on the bottom:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700195791/9a01290b4189e6a39c473af0a448/cfed06da-f35a-4b22-b687-286ea48864c1?expires=1794471300&amp;signature=06db8e06702813b511da66fb6de8276e08da07492b007977f4c12e5474800e9b&amp;req=dicnFsh3mIZWWPMW1HO4zTni3cItZZ8v2SRx6amjj9FWZIsaKtMGmZJHyyfn%0A1HMu%0A)

4. Search "Claude for Intune" and click the "Select" button on the bottom.

5. In **App Information**, set **Minimum operating system** to iOS 18, then click the "Next" button:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700196458/588327ab209e9524c45111a244a1/258697c2-2f82-471b-9104-2bccb1b01614?expires=1794471300&amp;signature=35dfa063c507e7790919e8d869ff0bf4885f5654eedc11255419e44d0b34d3f7&amp;req=dicnFsh3m4VaUfMW1HO4zbxl5YxTcDMtDNNSLAHCCFrupA6KJ7WayAgkrSis%0AWUxe%0A)

6. For **Assignments**, add the groups that should get the app: under Required to install it automatically, or under Available for enrolled devices so employees can install it from Company Portal. You can use user groups or device groups.

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2741107114/8f15b0d179a54c2ca4effaad8577/55bed25a-4b20-47b0-9e89-7f8adc86c04f?expires=1794471300&amp;signature=8f25a33cea632e4a27a37a5189552aca8a7a8a9fdc2a411464678a303a5406a9&amp;req=dicjF8h%2BmoBeXfMW1HO4zYaZMey4fvKdmN%2B6UXepdg9KARbpnKNojrLd6Y9Q%0Ar5D%2B%0A)

7. Click "Next," review and create.

8. If you assigned the app as Required, it installs automatically; if Available, employees install it from Company Portal.

### 2. Apply an app-protection policy to Claude for Intune

1. In the Microsoft Intune admin center, select "Apps" from the left side navigation panel:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700190760/9f6412fe68632cffee29826f7d30/42fdeb30-64af-4089-a976-5094bb6b8292?expires=1794471300&amp;signature=487003293ccdcd0186f40ea004fdedaeb84cbe7eafc8b957a6bca75723986b65&amp;req=dicnFsh3nYZZWfMW1HO4zQwrZI4GVNM%2FLtTCoSp4D6r7Oo8zrfP7ba%2BDRGXh%0AGiIv%0A)

2. Under **Manage apps**, select "Protection":

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700200858/a7ddd4265aeb6d61a7a096297cd5/fc9a1fe2-3d0e-4038-9b2c-f96bd19e4020?expires=1794471300&amp;signature=4b5ea4a84cc4a8da9e0af2583799963499078a5cfd7a4fdcb28a7d67a92ab972&amp;req=dicnFst%2BnYlaUfMW1HO4zeBHXBs58vzunJWY0xu8hzI29428dWsOY%2FWwCHKq%0AT68Y%0A)

3. Click "+ Create" and then select "iOS/iPadOS":

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700201382/6240e257b2b498b5fa5ac1111561/11ef4f59-aba1-4d2b-ac58-9aec1dd60a4d?expires=1794471300&amp;signature=80e8c406c6ba5a897ea782659eb27401e09b5f238d4a90d749845000f98fef3f&amp;req=dicnFst%2BnIJXW%2FMW1HO4zc89y09SBXtNV2VWh%2B9zzEoe5DbQGqHoTxE40d3y%0AaA%2FH%0A)

4. Enter Name in the **Basics** tab, then click "Next" to **Apps**. Set **Target policy to** "Selected apps." Click "+ Select custom apps":

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700201929/2edf45cedc0bc03204f86d01a49e/4d96c12d-962b-43f6-8b3f-668e3247d4c1?expires=1794471300&amp;signature=5223a6a4f61ff963be88f2c034a51a428f7645bd370bd98a2c8852aac5ccdc6f&amp;req=dicnFst%2BnIhdUPMW1HO4zVmMRJUQVDwLKETwku7gMst%2F%2FSXie6dS3RJMEK0g%0A1Q51%0A)

5. Type in the bundle ID `com.anthropic.claudeforintune`. Select it so it appears under **Selected Apps** before clicking "Select":

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700202816/3565aea2d1b9c22a5f8d105825c5/3de6d241-6259-463e-a503-a6ca9f2095e0?expires=1794471300&amp;signature=2ddae7ccb16d094bb6faf8fe0cc5f8d8e07ad87a8b336b8df8fc6001657bd768&amp;req=dicnFst%2Bn4leX%2FMW1HO4zf6tYicsz6t012LT9vQL0W5NCU2y%2B%2BcvofUdq%2F5N%0ADG1r%0A)

6. In Apps, confirm the bundle ID now appears under **Custom apps** before clicking "Next":

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700203780/24ed354ef0de87bf0a0c1bc129a1/46eed662-f488-48ee-a4d1-8a9a76079884?expires=1794471300&amp;signature=7cf0120c75ce3f69016118c2b1c4d3a381494cb9f944fb02ae21d85d92c3e9bc&amp;req=dicnFst%2BnoZXWfMW1HO4zQd95NGO3Mnc8F6Cfy2R7u%2FVFdYC%2BVoYvObKLLpz%0AQQr9%0A)

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