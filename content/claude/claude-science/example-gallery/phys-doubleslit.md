> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# The double slit, one electron at a time

> Rebuild the picture of Tonomura's 1989 experiment with an ideal double slit: each electron lands as 1 random dot, yet fringes 10.7 µm apart build up.

![Dots after 10 to 100,000 electrons build up into fringes; a histogram fit gives a spacing of 10.706 ± 0.003 µm against λL/d = 10.711 µm, and a smooth curve shows no fringes when the slit is known.](https://mintcdn.com/claude-ai/F2QP9ubtYgT0edFI/images/claude-science/example-gallery/phys-doubleslit-full-light.webp?fit=max\&auto=format\&n=F2QP9ubtYgT0edFI\&q=85\&s=d33485dbb10e2b0e60ce7127967ae21c)

The numbers in your session might differ from this picture and from the summary in [Reference analysis](#reference-analysis).

## Prompt

Copy the prompt and paste it into a new session in [Claude Science](/docs/claude-science/overview). By default, Claude asks with a [permission card](/docs/claude-science/core-concepts#permission-cards) before it runs code or installs packages.

```text Prompt wrap theme={null}
In 1989 Akira Tonomura's team at Hitachi sent electrons one at a time past an electron biprism, the electron version of a double slit, and filmed an interference pattern building up dot by dot. Recreate that with an ideal double slit. Say nothing else about the 1989 experiment.

Take electrons accelerated through 50 kV (work out their de Broglie wavelength, with relativity), 2 slits 0.1 µm wide and 0.5 µm apart, and a screen 1 m away (check that d²/λL ≈ 0.05, so the simple far-field formula holds). Compute the probability of landing at each position on the screen. Then draw random hits from it, one electron at a time, and show the screen from −60 to 60 µm after 10, 100, 1,000, 10,000 and 100,000 electrons, noting on the figure how many hits land outside.

Fit the final pattern to measure the fringe spacing, and give it with its error bar: how many error bars from λL/d? Then show that the fringes vanish if we know which slit each electron went through. Explain each step as you would to an undergraduate.
```

## Reference analysis

Each electron lands as 1 random dot, yet fringes 10.7 µm apart build up. Rebuilds the picture of Tonomura's 1989 experiment with an ideal double slit: 50 kV electrons (de Broglie wavelength 5.355 pm, 2.4% shorter than without relativity), 2 slits 0.1 µm wide and 0.5 µm apart, a screen at 1 m. 10 electrons look random, 100 hint at bands, by 1,000 the fringes are plain, and at 100,000 a fit gives 10.71 µm, good to about 0.003 µm, matching λL/d = 10.711 µm. If we know which slit each electron went through, the fringes vanish and only the broad single-slit envelope is left.

## Data

This example doesn't download any data.

Reference: A. Tonomura, J. Endo, T. Matsuda, T. Kawasaki & H. Ezawa, 'Demonstration of single-electron buildup of an interference pattern', American Journal of Physics 57, 117–120 (1989)
