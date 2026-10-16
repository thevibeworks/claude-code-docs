> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Genetic drift in a bottle: Buri's 107 fruit-fly populations

> Simulate 107 bottles of 16 fruit flies drifting by chance alone and compare them with Peter Buri's real bottles (1956).

<div className="example-gallery-page">
  <Frame>
    <img className="block dark:hidden" src="https://mintcdn.com/claude-ai/F2QP9ubtYgT0edFI/images/claude-science/example-gallery/bio-drift-full-light.webp?fit=max&auto=format&n=F2QP9ubtYgT0edFI&q=85&s=2e5d4d7b916e451a8f4d3fcdbcdb7dd9" alt="Three panels: 107 simulated allele-frequency paths over 19 generations, histograms at generations 1, 5, 10, and 19, and 20,000 replays at 16 and 9 breeding flies against Buri's 58." width="1600" height="706" data-path="images/claude-science/example-gallery/bio-drift-full-light.webp" />

    <img className="hidden dark:block" src="https://mintcdn.com/claude-ai/F2QP9ubtYgT0edFI/images/claude-science/example-gallery/bio-drift-full-dark.webp?fit=max&auto=format&n=F2QP9ubtYgT0edFI&q=85&s=781269cad496388cf0a1e54ab0d7af64" alt="Three panels: 107 simulated allele-frequency paths over 19 generations, histograms at generations 1, 5, 10, and 19, and 20,000 replays at 16 and 9 breeding flies against Buri's 58." width="1600" height="706" data-path="images/claude-science/example-gallery/bio-drift-full-dark.webp" />
  </Frame>
</div>

The numbers in your session might differ from this picture and from the summary in [Reference analysis](#reference-analysis).

## Prompt

Copy the prompt and paste it into a new session in [Claude Science](/docs/claude-science/overview). By default, Claude asks with a [permission card](/docs/claude-science/core-concepts#permission-cards) before it runs code or installs packages.

```text Prompt wrap theme={null}
In a 1956 paper, Peter Buri described keeping 107 bottles of fruit flies for 19 generations, restarting each bottle every generation with 8 males and 8 females picked at random. Every founder carried one copy each of two neutral eye-color alleles, bw and bw75, so bw75 started at a frequency of 0.5 in every bottle.

Simulate this with random sampling only: no selection, no mutation. Plot the bw75 frequency in all 107 populations over time, and draw histograms of the 107 frequencies at generations 1, 5, 10 and 19. Under each, print how many bottles are at 0, below 1/3, between 1/3 and 2/3, above 2/3, and at 1, and describe the change using only these 5 counts.

By generation 19, Buri found bw75 lost in 30 bottles and fixed in 28. Repeat your simulated experiment 1,000 times: how often does chance alone give that many? What population size would match his result? Compare it with Buri's own estimate for these bottles, about 9 breeding flies (2Ne = 17.86). Buri wrote that the causes are not known, but that unequal numbers of offspring per fly, down to sterility, are certainly part of it. This simulation does not test that, so report it as his view, in 1 or 2 sentences, and add no other causes. Explain each step as you would to an undergraduate.
```

## Reference analysis

107 simulated bottles of 16 fruit flies drift by chance alone: on average 25 lose or fix an allele in 19 generations (27 in the run pictured), but in Peter Buri's real bottles (1956) the count reached 58. A breeding population of about 9 gives 57, in line with Buri's own estimate (2Ne = 17.86): the textbook lesson of effective population size. Along the way the 107 frequencies, counted at generations 1, 5, 10, and 19, drain from the middle third into the outer thirds and from there into the 2 ends, 0 and 1, which no bottle leaves.

## Data

This example doesn't download any data.

Reference: Buri P., 'Gene frequency in small populations of mutant Drosophila', Evolution 10:367–402 (1956)
