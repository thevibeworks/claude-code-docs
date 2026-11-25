---
title: Link your Claude organization button
url: https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-button
description: Add the button that sends a customer from your product to Claude's approval page to start Linked billing.
featureMetadata:
  status: beta
  betaHeader: user-profiles-billing-2026-10-01
  supportedModels:
    - claude-fable-5-2
    - claude-mythos-5-2
    - claude-fable-5-1
    - claude-mythos-5-1
    - claude-fable-5
    - claude-mythos-5
    - claude-mythos-preview
    - claude-opus-5-5
    - claude-opus-5
    - claude-sonnet-5-5
    - claude-sonnet-5
    - claude-haiku-5-5
    - claude-haiku-4-5-20251001
    - claude-opus-4-8
    - claude-opus-4-7
    - claude-opus-4-6
    - claude-sonnet-4-6
    - claude-opus-4-5-20251101
    - claude-sonnet-4-5-20250929
  supportedPlatforms:
    Claude API:
      availability: beta
      note: Only requests that send `billing_policy` need the beta header.
---

<Warning>
  Claude Platform OAuth is a Beta Service: prerelease software provided under your agreement with Anthropic, such as the [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms), and the [Service Specific Terms](https://www.anthropic.com/legal/service-specific-terms). Endpoints, parameters, and behavior can change during the beta. It might not be suitable for production use.
</Warning>

This page lists the HTML, CSS, colors, sizes, and logo of the **Link your Claude organization** button for [Linked billing](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing).

<Frame caption="The button in light and dark">
  ![Link your Claude organization button, light and dark, with the Claude logo before its words](https://platform.claude.com/docs/images/claude-link-button.svg)
</Frame>

## HTML and CSS

The only parts of the button’s look that you may change are its size and whether you use the light or the dark button. The font, the colors, and the logo’s size compared with the words stay as [Colors and sizes](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-button#colors) shows them.

The button’s CSS and HTML fit into your page like this:

* **CSS:** The `<style>` block from **Button CSS** goes in your page’s `<head>`. If your Content Security Policy doesn’t allow inline styles, its rules go in your style sheet instead.
* **HTML:** The `<a>` element from **Sample HTML** goes where the button appears. It holds the logo, so the button needs no Anthropic host in your Content Security Policy.
* **Route:** The element’s `href`, `/claude/billing/link` in the sample, points to your back end’s [route that starts the approval](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-and-bill-a-customer#send-them-to-approve).
* **Dark button:** The `claude-button-dark` class, added beside `claude-button` on the element, gives the dark button.
* **Size:** To resize the button, change only the `font-size` line in **Button CSS**, not the size inside the `font` line.

For how you may use the Claude name and logo, see the [Linked Billing Beta Terms](https://www.anthropic.com/legal/linked-billing-terms).

<Accordion title="Button CSS">
  ```html claude-button.html
  <style>
    /* Each size is written as calc(Nem / 14), where N is its size in pixels
       when the text is 14 pixels. To make the button larger, change only font-size. */
    .claude-button {
      --claude-button-fill: #FFFFFF;
      --claude-button-fill-hover: #F5F4ED;
      --claude-button-text: #141413;
      --claude-button-border: #87867F;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: calc(10em / 14);
      box-sizing: border-box;
      min-height: calc(40em / 14);
      padding: calc(8em / 14) calc(12em / 14);
      border: 1px solid var(--claude-button-border);
      border-radius: calc(8em / 14);
      background: var(--claude-button-fill);
      font: 500 0.875rem/1.4286 ui-sans-serif, system-ui, -apple-system, "Segoe UI",
        Roboto, "Helvetica Neue", Arial, sans-serif;
      font-size: 0.875rem;
      letter-spacing: normal;
      text-transform: none;
      cursor: pointer;
    }
    .claude-button-dark {
      --claude-button-fill: #141413;
      --claude-button-fill-hover: #262624;
      --claude-button-text: #FAF9F5;
      --claude-button-border: #73726C;
    }
    .claude-button,
    .claude-button:link,
    .claude-button:visited,
    .claude-button:hover,
    .claude-button:focus,
    .claude-button:active {
      color: var(--claude-button-text);
      text-decoration: none;
    }
    .claude-button:hover {
      background: var(--claude-button-fill-hover);
    }
    .claude-button:focus-visible {
      outline: 2px solid var(--claude-button-text);
      outline-offset: 2px;
      box-shadow: 0 0 0 2px var(--claude-button-fill);
    }
    .claude-button svg {
      flex: none;
      width: calc(20em / 14);
      height: calc(20em / 14);
    }
    .claude-button path {
      fill: #D97757;
      stroke: none;
    }
  </style>
  ```
</Accordion>

<Accordion title="Sample HTML">
  ```html link-your-claude-organization.html
  <a class="claude-button" href="/claude/billing/link">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true">
      <path fill="#D97757" d="M11.376 24L10.776 23.544L10.44 22.8L10.776 21.312L11.16 19.392L11.472 17.856L11.76 15.96
        L11.928 15.336L11.904 15.288L11.784 15.312L10.344 17.28L8.16 20.232L6.432 22.056
        L6.024 22.224L5.304 21.864L5.376 21.192L5.784 20.616L8.16 17.568L9.6 15.672L10.536 14.592
        L10.512 14.448H10.464L4.128 18.576L3 18.72L2.496 18.264L2.568 17.52L2.808 17.28L4.704 15.96
        L9.432 13.32L9.504 13.08L9.432 12.96H9.192L8.4 12.912L5.712 12.84L3.384 12.744L1.104 12.624
        L0.528 12.504L0 11.784L0.048 11.424L0.528 11.112L1.224 11.16L2.736 11.28L5.016 11.424
        L6.672 11.52L9.12 11.784H9.504L9.552 11.616L9.432 11.52L9.336 11.424L6.96 9.84L4.416 8.16
        L3.072 7.176L2.352 6.672L1.992 6.216L1.848 5.208L2.496 4.488L3.384 4.56L3.6 4.608
        L4.488 5.304L6.384 6.768L8.88 8.616L9.24 8.904L9.408 8.808V8.736L9.24 8.472L7.896 6.024
        L6.456 3.528L5.808 2.496L5.64 1.872C5.576 1.656 5.544 1.416 5.544 1.152L6.288 0.144001
        L6.696 0L7.704 0.144001L8.112 0.504001L8.736 1.92L9.72 4.152L11.28 7.176L11.736 8.088
        L11.976 8.904L12.072 9.168H12.24V9.024L12.36 7.296L12.6 5.208L12.84 2.52L12.912 1.752
        L13.296 0.840001L14.04 0.360001L14.616 0.624001L15.096 1.32L15.024 1.752L14.76 3.6
        L14.184 6.504L13.824 8.472H14.04L14.28 8.208L15.264 6.912L16.92 4.848L17.64 4.032
        L18.504 3.12L19.056 2.688H20.088L20.832 3.816L20.496 4.992L19.44 6.336L18.552 7.464
        L17.28 9.168L16.512 10.536L16.584 10.632H16.752L19.608 10.008L21.168 9.744L22.992 9.432
        L23.832 9.816L23.928 10.2L23.592 11.016L21.624 11.496L19.32 11.952L15.888 12.768
        L15.84 12.792L15.888 12.864L17.424 13.008L18.096 13.056H19.728L22.752 13.272L23.544 13.8
        L24 14.424L23.928 14.928L22.704 15.528L21.072 15.144L17.232 14.232L15.936 13.92H15.744
        V14.016L16.848 15.096L18.84 16.896L21.36 19.224L21.48 19.8L21.168 20.28L20.832 20.232
        L18.624 18.552L17.76 17.808L15.84 16.2H15.72V16.368L16.152 17.016L18.504 20.544
        L18.624 21.624L18.456 21.96L17.832 22.176L17.184 22.056L15.792 20.136L14.376 17.952
        L13.224 16.008L13.104 16.104L12.408 23.352L12.096 23.712L11.376 24Z"/>
    </svg>
    Link your Claude organization
  </a>
  ```
</Accordion>

If your route needs a form submission, such as a `POST`, use a `<button type="submit" class="claude-button">` inside a form in place of the `<a>` element. It holds the same logo and words. The form’s action is your route, and the same styles apply.

A rule in your own style sheet, such as one for `.nav a`, can override the button’s styles. The button then doesn’t match the picture and the tables in [Colors and sizes](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-button#colors). To keep its design, write such a rule so that it skips elements with the `claude-button` class.

## Colors and sizes

| Part | Light button | Dark button |
| ----- | ----- | ----- |
| Background | `#FFFFFF` | `#141413` |
| Text | `#141413` | `#FAF9F5` |
| Border | `#87867F` | `#73726C` |
| Background on hover | `#F5F4ED` | `#262624` |
| Logo | `#D97757` | `#D97757` |

At the default font size of 14 pixels, on a page whose root font size is 16 pixels, the button has these sizes:

| Part | Size |
| ----- | ----- |
| Height | 40 pixels |
| Padding | 8 pixels above and below, 12 pixels at the sides |
| Corner radius | 8 pixels |
| Border | 1 pixel |
| Logo | 20 by 20 pixels |
| Gap between the logo and the words | 10 pixels |
| Text | 14 pixels, weight 500, in the system’s sans-serif font |
| Focus outline | 2 pixels in the text color, 2 pixels out from the button, with a 2-pixel ring in the fill color around the button |

Every size except the border and the focus outline scales with the button’s font size.

## Logo file

For a button built without HTML, such as in a mobile or desktop app, the logo is the following file, `claude-logo.svg`. That button takes the colors and sizes in [Colors and sizes](https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/link-button#colors), scaled together as that section describes if you change its size. As in the sample HTML, hide the logo from screen readers in that button too, because the words already name it.

<Accordion title="claude-logo.svg">
  <File filename="claude-logo.svg" size="sm">
    ```xml
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
      <path fill="#D97757"
        d="M11.376 24L10.776 23.544L10.44 22.8L10.776 21.312L11.16 19.392L11.472 17.856L11.76 15.96
          L11.928 15.336L11.904 15.288L11.784 15.312L10.344 17.28L8.16 20.232L6.432 22.056
          L6.024 22.224L5.304 21.864L5.376 21.192L5.784 20.616L8.16 17.568L9.6 15.672L10.536 14.592
          L10.512 14.448H10.464L4.128 18.576L3 18.72L2.496 18.264L2.568 17.52L2.808 17.28L4.704 15.96
          L9.432 13.32L9.504 13.08L9.432 12.96H9.192L8.4 12.912L5.712 12.84L3.384 12.744L1.104 12.624
          L0.528 12.504L0 11.784L0.048 11.424L0.528 11.112L1.224 11.16L2.736 11.28L5.016 11.424
          L6.672 11.52L9.12 11.784H9.504L9.552 11.616L9.432 11.52L9.336 11.424L6.96 9.84L4.416 8.16
          L3.072 7.176L2.352 6.672L1.992 6.216L1.848 5.208L2.496 4.488L3.384 4.56L3.6 4.608
          L4.488 5.304L6.384 6.768L8.88 8.616L9.24 8.904L9.408 8.808V8.736L9.24 8.472L7.896 6.024
          L6.456 3.528L5.808 2.496L5.64 1.872C5.576 1.656 5.544 1.416 5.544 1.152L6.288 0.144001
          L6.696 0L7.704 0.144001L8.112 0.504001L8.736 1.92L9.72 4.152L11.28 7.176L11.736 8.088
          L11.976 8.904L12.072 9.168H12.24V9.024L12.36 7.296L12.6 5.208L12.84 2.52L12.912 1.752
          L13.296 0.840001L14.04 0.360001L14.616 0.624001L15.096 1.32L15.024 1.752L14.76 3.6
          L14.184 6.504L13.824 8.472H14.04L14.28 8.208L15.264 6.912L16.92 4.848L17.64 4.032
          L18.504 3.12L19.056 2.688H20.088L20.832 3.816L20.496 4.992L19.44 6.336L18.552 7.464
          L17.28 9.168L16.512 10.536L16.584 10.632H16.752L19.608 10.008L21.168 9.744L22.992 9.432
          L23.832 9.816L23.928 10.2L23.592 11.016L21.624 11.496L19.32 11.952L15.888 12.768
          L15.84 12.792L15.888 12.864L17.424 13.008L18.096 13.056H19.728L22.752 13.272L23.544 13.8
          L24 14.424L23.928 14.928L22.704 15.528L21.072 15.144L17.232 14.232L15.936 13.92H15.744
          V14.016L16.848 15.096L18.84 16.896L21.36 19.224L21.48 19.8L21.168 20.28L20.832 20.232
          L18.624 18.552L17.76 17.808L15.84 16.2H15.72V16.368L16.152 17.016L18.504 20.544
          L18.624 21.624L18.456 21.96L17.832 22.176L17.184 22.056L15.792 20.136L14.376 17.952
          L13.224 16.008L13.104 16.104L12.408 23.352L12.096 23.712L11.376 24Z"/>
    </svg>
    ```
  </File>
</Accordion>

## Next steps

<CardGroup cols={2}>
  <Card title="What your customers see" icon="browser" href="https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/what-your-customers-see">
    The approval page, spend caps, and emails that your customers see, so that you can support them
  </Card>

  <Card title="Test and publish your app" icon="rocket" href="https://platform.claude.com/docs/en/manage-claude/oauth-apps/linked-billing/test-and-publish">
    Add test users, publish your app, and change or delete it
  </Card>
</CardGroup>
