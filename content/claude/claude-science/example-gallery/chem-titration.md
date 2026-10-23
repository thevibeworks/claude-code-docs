> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# A titration curve from the full equilibrium: which indicator finds the equivalence point?

> Solve the full equilibrium for 25.0 mL of 0.100 M acetic acid as 0.100 M NaOH is added, without the usual shortcuts.

![Left: acetic acid's titration curve, with pH 2.88 at the start, 4.76 half-way, and 8.73 at equivalence. Right: acetic acid and HCl with the methyl orange and phenolphthalein ranges shaded: for acetic acid, methyl orange turns 17.4 mL too early.](https://mintcdn.com/claude-ai/F2QP9ubtYgT0edFI/images/claude-science/example-gallery/chem-titration-full-light.webp?fit=max\&auto=format\&n=F2QP9ubtYgT0edFI\&q=85\&s=37e8dfb5f136ac8d3872d9cd328d04be)

The numbers in your session might differ from this picture and from the summary in [Reference analysis](#reference-analysis).

## Prompt

Copy the prompt and paste it into a new session in [Claude Science](https://claude.com/docs/claude-science/overview.md). By default, Claude asks with a [permission card](https://claude.com/docs/claude-science/core-concepts.md#permission-cards) before it runs code or installs packages.

```text Prompt wrap theme={null}
I'm titrating 25.0 mL of 0.100 M acetic acid (pKa 4.76) with 0.100 M NaOH. Compute the pH after each addition of base, from 0 to 50 mL, by solving the full equilibrium (mass balance, charge balance, Kw = 1.0 × 10⁻¹⁴) without the usual shortcuts (no Henderson–Hasselbalch, no 'x is small'), using concentrations, at 25 °C. Plot the titration curve and mark the starting point, the half-equivalence point and the equivalence point. Show that the acid alone sets the start, pH = pKa half-way, and acetate acting as a weak base sets the equivalence point.

Add the curve for 0.100 M HCl, and shade the color-change ranges of methyl orange (pH 3.1–4.4) and phenolphthalein (pH 8.3–10.0). Give the pH of both curves at 24.95 and 25.05 mL to show how steep each jump is. Which indicator works for which acid? If I picked the wrong one, how far off would my endpoint be, in mL (endpoint = completed color change)? Explain each step as you would to an undergraduate.
```

## Reference analysis

With acetic acid, phenolphthalein turns within 0.05 mL of the 25.00 mL equivalence point; methyl orange has fully turned at 7.6 mL, 17.4 mL too early. Methyl orange works for HCl (0.02 mL early). The reason: from 24.95 to 25.05 mL the pH runs from 4.0 to 10.0 for HCl but from 7.5 to 10.0 for acetic acid, entirely above methyl orange's range. Solving the full equilibrium for 25.0 mL of 0.100 M acetic acid as 0.100 M NaOH is added, without the usual shortcuts, using concentrations, at 25 °C, gives pH 2.88 at the start, 4.76 = pKa at the half-way point, and 8.73 at the equivalence point.

## Data

This example doesn't download any data.
