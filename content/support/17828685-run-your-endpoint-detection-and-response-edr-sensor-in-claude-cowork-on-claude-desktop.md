# Run your endpoint detection and response \(EDR\) sensor in Claude Cowork on Claude Desktop

When Claude Cowork runs on a user's computer, either on its own or as part of the new unified Claude experience that brings chat and Cowork together, it runs shell commands and code in an isolated virtual machine (VM). The endpoint detection and response (EDR) sensor already on that computer can't see inside the VM. This article shows IT and security admins how to run the sensor inside the VM, so activity in the VM reports to the console your security team already uses.

Running an EDR sensor in Cowork is available in beta for Team and Enterprise plans. It’s available for Claude Desktop on macOS and Windows, and for Claude Desktop connected to Amazon Bedrock, Google Cloud Vertex AI, or Microsoft Foundry.

**Important:** This covers only the VM on the user's computer. Cowork sessions in the cloud run on Anthropic's servers, and you can't install a sensor there.

## How it works

1. Each time the Cowork VM starts, Claude Desktop copies your vendor's sensor package into the VM and checks its signature against the approved key of the vendor you named.

2. If the signature is valid, Claude runs the vendor's install script inside the VM, at most once per VM start. If the setting isn't set, nothing is installed.

3. The sensor connects to your vendor's cloud and reports activity, the same way it does from the rest of the computer. The sensor can send telemetry and data out of the VM, outside the Cowork network allowlist.

The VM starts the first time something needs it, usually when a user opens Cowork, and runs until Claude quits or the user signs out.

## Supported vendors

Claude Desktop only installs a sensor package signed with the key of an approved EDR vendor.

Approved vendors:

- CrowdStrike

- Evoke Security

- Neo

- Palo Alto Networks

- Pluto Security

- SentinelOne

- Tanium

If your vendor isn't listed, ask them to apply using the form in **[For EDR vendors](#h_ae012dc926)** below. If you have an Anthropic account team, let them know you need it.

## Before you start

You'll need:

- **macOS:** Claude Desktop 4.4212.0 or later

- **Windows:** The .msix build of Claude Desktop, 4.4212.0 or later, on Windows 10 or 11 with hardware virtualization and the Virtual Machine Platform feature turned on

- **Device management:** An MDM tool for macOS, or a way to set registry policy on Windows, such as Group Policy or Intune

Then follow your EDR vendor's setup guidance. Each vendor provides its own files and instructions.

## Frequently asked questions

### Does the integration cover Cowork sessions in the cloud?

No. Some Cowork tasks run in a cloud VM that Anthropic hosts, and your EDR sensor can't be installed there. The integration covers only the local VM on the user's computer.

### What can the sensor see?

The sensor can see activity and content inside the VM, which can include prompts, files, and Claude's responses. It sends data to your EDR vendor. Anthropic doesn't receive or control that data.

### Does the integration cost extra?

Anthropic doesn't charge extra for the integration during the beta. Your EDR vendor may charge for the sensor, so contact them for pricing details.

### What happens if I remove the MDM settings?

Removing the settings doesn't remove a sensor that's already installed. Claude stops running the package at later VM starts.

### How do sensor updates work?

Your vendor maintains the package. The signature covers only the package file, not updates the sensor downloads later. Signatures expire within two years, so you'll deploy a re-signed package from your vendor.

## For EDR vendors

If you're an EDR vendor and want your sensor to run in the Cowork VM, **[apply to join the integration](https://forms.gle/9CPwYUcdXoRVtqWE9)**.

## Terms

Your organization chooses the security vendor. Your organization uses the EDR Software under its own agreement with that vendor.

The EDR Software is a Third Party Feature under your agreement with Anthropic. It is not part of Anthropic's Services.

The EDR Software can see activity and content inside the virtual machine. This can include prompts, files and Claude's responses. It sends data to the vendor. Anthropic does not receive or control that data, and the vendor does not handle it on Anthropic's behalf.

Your organization is responsible for the EDR Software. This includes testing it before you deploy it and again after any update to Claude or to the EDR Software. Anthropic is not responsible for claims that arise from a failure to test.

Your organization is responsible for claims that arise from the EDR Software, as described in your agreement with Anthropic.