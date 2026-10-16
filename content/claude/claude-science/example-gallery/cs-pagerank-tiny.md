> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# PageRank on a web of 11 pages: why 1 good link beats 6 weak ones

> Follow a random surfer on Wikipedia's 11-page example until the numbers settle, and reproduce all 11 published values to 0.1 point.

<div className="example-gallery-page">
  <Frame>
    <img className="block dark:hidden" src="https://mintcdn.com/claude-ai/F2QP9ubtYgT0edFI/images/claude-science/example-gallery/cs-pagerank-tiny-full-light.webp?fit=max&auto=format&n=F2QP9ubtYgT0edFI&q=85&s=44bf56115d462e279420a8cfb04b1499" alt="Three panels: the 11-page web as circles sized by PageRank, the 11 shares settling to B 38.4%, C 34.3%, and E 8.1%, and bars showing that C's one link brings 32.7 points while E's six bring 6.5." width="1600" height="594" data-path="images/claude-science/example-gallery/cs-pagerank-tiny-full-light.webp" />

    <img className="hidden dark:block" src="https://mintcdn.com/claude-ai/F2QP9ubtYgT0edFI/images/claude-science/example-gallery/cs-pagerank-tiny-full-dark.webp?fit=max&auto=format&n=F2QP9ubtYgT0edFI&q=85&s=e857b5662f0295df70aaea333313232b" alt="Three panels: the 11-page web as circles sized by PageRank, the 11 shares settling to B 38.4%, C 34.3%, and E 8.1%, and bars showing that C's one link brings 32.7 points while E's six bring 6.5." width="1600" height="594" data-path="images/claude-science/example-gallery/cs-pagerank-tiny-full-dark.webp" />
  </Frame>
</div>

The numbers in your session might differ from this picture and from the summary in [Reference analysis](#reference-analysis).

## Prompt

Copy the prompt and paste it into a new session in [Claude Science](/docs/claude-science/overview). By default, Claude asks with a [permission card](/docs/claude-science/core-concepts#permission-cards) before it runs code or installs packages.

```text Prompt wrap theme={null}
PageRank is the idea that launched Google (Brin & Page, 1998): a page matters if pages that matter link to it. Here is a tiny web of 11 pages, A to K, where B→C means that page B links to page C:

B→C, C→B, D→A, D→B, E→B, E→D, E→F, F→B, F→E, G→B, G→E, H→B, H→E, I→B, I→E, J→E, K→E

Imagine a surfer who follows a random link on the current page 85 % of the time and jumps to a random page the rest of the time. From a page with no links, the surfer always jumps to a random page. Start with the surfer equally likely to be on any page, and repeat that step until the share of time spent on each page stops changing. That share is the page's PageRank.

Draw the web as circles with area proportional to PageRank, each letter inside its circle, C and E in color, no other labels, and plot how the 11 numbers settle. This is the example drawn in Wikipedia's PageRank article; its values are B 38.4 %, C 34.3 %, E 8.1 %, D and F 3.9 %, A 3.3 %, G to K 1.6 %. Then compare each page's PageRank with its share of the 17 links. C has 1 incoming link, but it is B's only link, and ranks 2nd; E has 6, all from low-ranked pages, and gets 8.1 %. Show how many points each link brings to C and to E. Explain each step as you would to an undergraduate.
```

## Reference analysis

Page C has 1 incoming link and ranks 2nd (34.3%); page E has 6 and gets 8.1%. Follows a random surfer on Wikipedia's 11-page example until the numbers settle, and reproduces all 11 published values to 0.1 point (B 38.4%, C 34.3%, E 8.1%, …). C's link is B's only link and brings 32.7 points; E's 6 links come from low-ranked pages and bring 6.5 points together; every page also gets the same 1.6-point floor. Draws the web as circles with area proportional to PageRank and shows the 11 numbers settling: every page is within 0.1 point of its final value after 29 steps.

## Data

This example doesn't download any data.

Example web after [PageRanks-Example.svg](https://commons.wikimedia.org/wiki/File:PageRanks-Example.svg) by 345Kai and Stannered (Wikimedia Commons, public domain).

Reference: S. Brin & L. Page, 'The anatomy of a large-scale hypertextual Web search engine', Computer Networks and ISDN Systems 30, 107–117 (1998)
