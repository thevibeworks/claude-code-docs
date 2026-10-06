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

## Get your organization ready

### 1. Ask Anthropic to enable Microsoft sign-in

Before employees can sign in to Claude for Intune, Anthropic needs to enable Microsoft sign-in for your organization's email domains. Contact your Anthropic account team or support, and tell them which email domains your employees use to sign in.

### 2. Register Claude for Intune in your Entra tenant

If you want to use Conditional Access with Claude for Intune, the app has to be registered in your Microsoft Entra tenant first. Until it is, Claude for Intune doesn't appear in the list of apps you can select in a Conditional Access policy.

Claude for Intune is registered the first time someone who is authorized to consent on behalf of the organization signs in with Microsoft. Choose one of these options:

- **Have a user sign in.** Go to claude.ai and select “Continue with Microsoft.” One successful sign-in is enough.

- **Grant admin consent.** A tenant admin opens the following URL, replacing {organization} with your tenant ID or domain: `https://login.microsoftonline.com/{organization}/adminconsent?client_id=bb747f0e-002b-4882-9960-916fe00a2b90`

After either option, Claude for Intune appears in Microsoft Entra and your Conditional Access admin can target it in a policy.

To require app protection at sign-in, target the Conditional Access rule at “All resources” with Grant = Require app protection policy. A rule that names only Office 365 or Claude SSO does not cover Claude for Intune. Microsoft Authenticator must be installed on the device.

## Add Claude for Intune in the Microsoft Intune admin center

### 1. Add Claude for Intune to your managed apps and make it available to BYOD devices.

1. In the Microsoft Intune admin center, select “Apps” from the left side navigation panel:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700192269/ce2bf95a18aba11042da50f4c1ad/dda0f9a2-d585-4b09-ae4f-a1ff70b1e010?expires=1791331200&amp;signature=c93194253030935d6cef0265d7cfa8e47b6648f8f42ad251e3dcf1695cc23bfd&amp;req=dicnFsh3n4NZUPMW3nq%2BgeEhD2I1cPjl8Vd9%2FRCGJ8Gamb4Qcqn8VgqErgJQ%0AW44mTzHmEtAo%2BkqBxeJhz1Ud7pI%3D%0A)

2. Under Platforms, select “iOS/iPadOS”:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700195036/b70c6c0bdeff5f2b72568ef4943b/67cc834c-5e91-42da-9d3b-1f32c8dd8c05?expires=1791331200&amp;signature=475f226637877204ed99229d5e3e8266a8e494ef8bbec22abffb8b455daf9630&amp;req=dicnFsh3mIFcX%2FMW3nq%2BgfGOegmD3C8c7v1K0uXwHwqK9t8oM%2BA%2FS%2BbHDTH7%0A9TJhkBOAnvEyXedIaRdsjqtP8gc%3D%0A)

3. Click “+ Create.” For the App type, select the “iOS store app,” and click the “Select” button on the bottom:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700195791/9a01290b4189e6a39c473af0a448/cfed06da-f35a-4b22-b687-286ea48864c1?expires=1791331200&amp;signature=b06042929ab45e62444cdb622ae40072c6bc8efd9680b9f7344fb6b75ef13b3d&amp;req=dicnFsh3mIZWWPMW3nq%2BgbjlrI2ZSJE3WnZw34L3DNZ%2Fw4idLifCshZcICDp%0Ap1fPk5GyLNcOC8N%2BE5PvWRhJeEg%3D%0A)

4. Search “Claude for Intune” and click the “Select" button on the bottom.

5. In **App Information**, set **Minimum operating system** to iOS 18, then click the “Next” button:

  ![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700196458/588327ab209e9524c45111a244a1/258697c2-2f82-471b-9104-2bccb1b01614?expires=1791331200&amp;signature=9d6db51f7901dda45df326fe883322daa4dd847d387e66eccb55059510ed7ee8&amp;req=dicnFsh3m4VaUfMW3nq%2BgRCtAWs2BDj8Pd3LUUaTNb7gq%2BHvJoWdCvKLVESq%0AExErmx5K7OLIi8xa%2BIBR5kie%2F7w%3D%0A)

6. For **Assignments**, add a group of users to make it available in their device’s Company Portal:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700197715/bf5aa327b41f994fdafe04869300/f4c6c9cf-51df-4d75-bf8a-b144d11dd380?expires=1791331200&amp;signature=7d9c1758bff663967ed5b4bffbe92f349abe7232d8954e5277c15edae40770e4&amp;req=dicnFsh3moZeXPMW3nq%2BgWgNNUH7GsoVNvGW8V8G8eeoAvXA%2B3RgvdA3xzHr%0AabohPvHkF5QkMzqy27SYV8UqCts%3D%0A)

7. Click “Next,” review and create.

8. Users have to download the app from Company Portal on their devices for access.

### 2. Apply an app-protection policy to Claude for Intune.

1. In the Microsoft Intune admin center, select “Apps” from the left side navigation panel:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700190760/9f6412fe68632cffee29826f7d30/42fdeb30-64af-4089-a976-5094bb6b8292?expires=1791331200&amp;signature=a95094d74a17718765586cce3e11e7e68e26c947f93bc089097cf2b19b36814c&amp;req=dicnFsh3nYZZWfMW3nq%2BgcnP38ikpDPj%2B89v3OwcHgzjKCgufoupOtoRm%2BoE%0A8ZCQrmRzP84BX0ztc5ezH2Wsud0%3D%0A)

2. Under **Manage apps**, select “Protection”:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700200858/a7ddd4265aeb6d61a7a096297cd5/fc9a1fe2-3d0e-4038-9b2c-f96bd19e4020?expires=1791331200&amp;signature=94e9979cc7fa93e9954eaa4d24711e69a8f1e24e30ac6fd7f7b92a5ee1c7ff37&amp;req=dicnFst%2BnYlaUfMW3nq%2BgVfUh4EkSa460IKc5VZwMObfawOku0keZNOC5wM0%0AWs%2B0ckLqXJArhxiA1Z%2BHAzStJFY%3D%0A)

3. Click “+ Create” and then select “iOS/iPadOS”:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700201382/6240e257b2b498b5fa5ac1111561/11ef4f59-aba1-4d2b-ac58-9aec1dd60a4d?expires=1791331200&amp;signature=881f62d5fb45fa79c8e1326357f83c5260fe8499fa6108c23ceb596776d8223c&amp;req=dicnFst%2BnIJXW%2FMW3nq%2Bgcl7Oct5X3YY4JLbLzCpE1u%2BTy%2BnRa0G%2FF8BsDKr%0AytAYYHLSvAhMVINxjE2%2BZin43%2BM%3D%0A)

4. Enter Name in the **Basics** tab, then click “Next” to **Apps**. Set **Target policy to** “Selected apps.” Click “+ Select custom apps”:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700201929/2edf45cedc0bc03204f86d01a49e/4d96c12d-962b-43f6-8b3f-668e3247d4c1?expires=1791331200&amp;signature=8e3180a60ad7b4cc2bf438557ad9645698774cb00f0f50a5ba4319fa63019df0&amp;req=dicnFst%2BnIhdUPMW3nq%2BgR4ZYiD6iQlDWIlJt4FTeswz24irPWt1Hctrr5CR%0Aru26wgj7Ha3zjiL207zqOVssdT0%3D%0A)

5. Type in the bundle ID `com.anthropic.claudeforintune`. Select it so it appears under **Selected Apps** before clicking “Select”:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700202816/3565aea2d1b9c22a5f8d105825c5/3de6d241-6259-463e-a503-a6ca9f2095e0?expires=1791331200&amp;signature=03ee93a3a5e62f71c3a5a2d95627f21f4302bcc1d21fd4d2c7c19945161d78d9&amp;req=dicnFst%2Bn4leX%2FMW3nq%2BgXDRvmM1OvnUPRtfeK8rUbpfoSgyXrNY1qEM8pNP%0AixgioVQd3vzqS%2FqQoT6fjHbl5ow%3D%0A)

6. In Apps, confirm the bundle ID now appears under **Custom apps** before clicking “Next”:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2700203780/24ed354ef0de87bf0a0c1bc129a1/46eed662-f488-48ee-a4d1-8a9a76079884?expires=1791331200&amp;signature=15185da780fb48c9e8e56c4bfd24eab2e727a3a8528256552d3fde19c70927f5&amp;req=dicnFst%2BnoZXWfMW3nq%2Bge%2BjBE5lQ45CVLPrU6V7f5OcajN0W26T1YbWjBaw%0AI5flU%2BfaYKvbEHsNZiv41uoY%2FZ8%3D%0A)

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