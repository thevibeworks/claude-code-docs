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

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700192269/ce2bf95a18aba11042da50f4c1ad/dda0f9a2-d585-4b09-ae4f-a1ff70b1e010?expires=1791615600&amp;signature=75a1bab47bac1cb27749c9682dd140d4e435bbcb81994083317965c7f0212120&amp;req=dicnFsh3n4NZUPMW1HO4ze7khjDX425mAMLV2Uu0R4WadiagPvspfYBAXVvk%0AGZm8%0A)

2. Under Platforms, select “iOS/iPadOS”:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700195036/b70c6c0bdeff5f2b72568ef4943b/67cc834c-5e91-42da-9d3b-1f32c8dd8c05?expires=1791615600&amp;signature=a0e824ebf418e7741dcb057d4fd52c8e11206c126fc91b3b7d95e8df0e6e2efd&amp;req=dicnFsh3mIFcX%2FMW1HO4zeH1oUzhsHaSQ7hR7Wh%2Bi70XfXTH%2FjiPOV1EZyb3%0AfnX9%0A)

3. Click “+ Create.” For the App type, select the “iOS store app,” and click the “Select” button on the bottom:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700195791/9a01290b4189e6a39c473af0a448/cfed06da-f35a-4b22-b687-286ea48864c1?expires=1791615600&amp;signature=431a2263f8eb3155b7d9b2592c20acafc8bd1fc5c5a1a7098eed5c98ed9bd85d&amp;req=dicnFsh3mIZWWPMW1HO4zTni3ccvY5sq2SRx6amjj9GEQKSM%2B98C2a3HDkhs%0A63XC%0A)

4. Search “Claude for Intune” and click the “Select" button on the bottom.

5. In **App Information**, set **Minimum operating system** to iOS 18, then click the “Next” button:

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700196458/588327ab209e9524c45111a244a1/258697c2-2f82-471b-9104-2bccb1b01614?expires=1791615600&amp;signature=270275182b1248a002b98b7229d05e42e564319d0cd6b3bca85a65ecab2f1881&amp;req=dicnFsh3m4VaUfMW1HO4zbxl5YlRdjcoDNNSLAHCCFqqa%2BfielZVaYUAxMm4%0ABWBK%0A)

6. For **Assignments**, add a group of users to make it available in their device’s Company Portal:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700197715/bf5aa327b41f994fdafe04869300/f4c6c9cf-51df-4d75-bf8a-b144d11dd380?expires=1791615600&amp;signature=88d1214abada1938409b0b9dc343ab58a046a342e7fc022317ecdf5038f61fed&amp;req=dicnFsh3moZeXPMW1HO4zeVx8DQf4CmLoVYQxJ7ndH5a6YgQLWz4CzM9JA9j%0AG1jO%0A)

7. Click “Next,” review and create.

8. Users have to download the app from Company Portal on their devices for access.

### 2. Apply an app-protection policy to Claude for Intune.

1. In the Microsoft Intune admin center, select “Apps” from the left side navigation panel:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700190760/9f6412fe68632cffee29826f7d30/42fdeb30-64af-4089-a976-5094bb6b8292?expires=1791615600&amp;signature=e79c2ffd3eb76054e313e963dcd16fe1d76c8ab2997178dbcb6a1b1bc8b73d8b&amp;req=dicnFsh3nYZZWfMW1HO4zQwrZIsEUtc6LtTCoSp4D6oaTgGHTCTHpvLG7jux%0AV7CE%0A)

2. Under **Manage apps**, select “Protection”:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700200858/a7ddd4265aeb6d61a7a096297cd5/fc9a1fe2-3d0e-4038-9b2c-f96bd19e4020?expires=1791615600&amp;signature=98cdacd79dea7982232f07a2b495658b8a3d3fdfbfb68ddc4bcffcb0ba4e162f&amp;req=dicnFst%2BnYlaUfMW1HO4zeBHXB479PjrnJWY0xu8hzKArMxoTl9BbG%2B%2FbL4m%0Adb8V%0A)

3. Click “+ Create” and then select “iOS/iPadOS”:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700201382/6240e257b2b498b5fa5ac1111561/11ef4f59-aba1-4d2b-ac58-9aec1dd60a4d?expires=1791615600&amp;signature=2f30ba5d13250427b71aff8c653fa48b90c4524274bc2479fa9d9662f2786e1b&amp;req=dicnFst%2BnIJXW%2FMW1HO4zc89y0pQA39IV2VWh%2B9zzEpEUlC0WhXibP8Qv1ka%0ANOJp%0A)

4. Enter Name in the **Basics** tab, then click “Next” to **Apps**. Set **Target policy to** “Selected apps.” Click “+ Select custom apps”:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700201929/2edf45cedc0bc03204f86d01a49e/4d96c12d-962b-43f6-8b3f-668e3247d4c1?expires=1791615600&amp;signature=6df65508730bc74c27ef98b363bb2d7f939d0cc2e1c22bd585cfb502a9aa2c45&amp;req=dicnFst%2BnIhdUPMW1HO4zVmMRJASUjgOKETwku7gMsvFV829FMRiywJpXr7E%0A6Q%2BA%0A)

5. Type in the bundle ID `com.anthropic.claudeforintune`. Select it so it appears under **Selected Apps** before clicking “Select”:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700202816/3565aea2d1b9c22a5f8d105825c5/3de6d241-6259-463e-a503-a6ca9f2095e0?expires=1791615600&amp;signature=603be70f237c1c6a288a2ae65128e7f45dd205bccc10fa1e4f591b19d4e6991d&amp;req=dicnFst%2Bn4leX%2FMW1HO4zf6tYiIuya9x12LT9vQL0W5SPqgIR7UPSDdWRdDH%0AwTAl%0A)

6. In Apps, confirm the bundle ID now appears under **Custom apps** before clicking “Next”:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700203780/24ed354ef0de87bf0a0c1bc129a1/46eed662-f488-48ee-a4d1-8a9a76079884?expires=1791615600&amp;signature=aa3523f2148a49bfe990c372360ddace9e20f133b074e744bb04400239a52c88&amp;req=dicnFst%2BnoZXWfMW1HO4zQd95NSM2s3Z8F6Cfy2R7u%2FXHRTNKpBf8we%2FCStd%0AdXdS%0A)

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