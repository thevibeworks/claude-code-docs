> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# A first finite-element model: a clamped steel ruler bends and vibrates

> Split a 300 mm steel ruler clamped at one end into 4 beam elements and check its bending under 1 N and its first 3 vibration modes against beam theory.

![Three plots: the ruler bent under 1 N, tip 0.800 mm down as theory says; its first 3 mode shapes at 27.18, 170.53, and 480.62 Hz over theory; and frequency errors falling from 2 to 16 elements.](https://mintcdn.com/claude-ai/F2QP9ubtYgT0edFI/images/claude-science/example-gallery/eng-beam-full-light.webp?fit=max\&auto=format\&n=F2QP9ubtYgT0edFI\&q=85\&s=f7c1012ed8af806d3ec445c6973cf630)

The numbers in your session might differ from this picture and from the summary in [Reference analysis](#reference-analysis).

## Prompt

Copy the prompt and paste it into a new session in [Claude Science](/docs/claude-science/overview.md). By default, Claude asks with a [permission card](/docs/claude-science/core-concepts.md#permission-cards) before it runs code or installs packages.

```text Prompt wrap theme={null}
I'm learning the finite-element method. Model a steel ruler clamped at one end: length 300 mm, width 25 mm, thickness 3 mm, E = 200 GPa, density 7850 kg/m³. Split it into 4 standard 2-node beam elements (cubic shape functions, consistent mass matrix) and write the matrices yourself with numpy. First hang 1 N (about 100 g) on the free end: beam theory says the tip drops PL³/(3EI) = 0.800 mm. Check that you get it, and draw the bent ruler over the theory curve. Then let the ruler vibrate: plot its first 3 mode shapes, each labeled with its frequency. Theory gives 27.18, 170.33 and 476.93 Hz; finite-element frequencies land slightly above and get closer with more elements, so show that in a small table for 2, 4, 8 and 16 elements. Give each frequency to 2 decimals, and its error in % worked out from the unrounded frequencies. Explain each step as you would to an undergraduate.
```

## Reference analysis

A 300 mm steel ruler clamped at one end is cut into 4 beam elements: under 1 N its tip drops 0.800 mm, exactly as beam theory says. Its first 3 vibration modes come out at 27.18, 170.53, and 480.62 Hz against 27.18, 170.33, and 476.93 Hz in theory, and 16 elements bring all 3 within 0.004%.

## Data

This example doesn't download any data.
