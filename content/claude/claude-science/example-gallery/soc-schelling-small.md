> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Schelling's segregation model: ask for 30% same-color neighbors, end up with 75%

> Ask for 30% same-color neighbors, end up with about 75%: the textbook computer version of Thomas Schelling's 1971 idea.

![A random board of blue and orange households (49% of neighbors alike), the same board settled into one-color patches (75%), and a curve of the share alike at the end against the demand, 51.3% to 99.6%.](https://mintcdn.com/claude-ai/F2QP9ubtYgT0edFI/images/claude-science/example-gallery/soc-schelling-small-full-light.webp?fit=max\&auto=format\&n=F2QP9ubtYgT0edFI\&q=85\&s=9150fb06019e6cb83311d70c1493c396)

The numbers in your session might differ from this picture and from the summary in [Reference analysis](#reference-analysis).

## Prompt

Copy the prompt and paste it into a new session in [Claude Science](https://claude.com/docs/claude-science/overview.md). By default, Claude asks with a [permission card](https://claude.com/docs/claude-science/core-concepts.md#permission-cards) before it runs code or installs packages.

```text Prompt wrap theme={null}
In 1971 the economist Thomas Schelling showed, with chips on a checkerboard, that a city can segregate sharply even when nobody asks for more than an even mix. Recreate the textbook computer version, which segregates at even milder demands. Fill a 50 × 50 grid at random with 1,125 blue and 1,125 orange households, leaving 250 cells empty. A household is content if at least 30 % of its occupied neighboring cells (the 8 around it, fewer at the edges) hold its own color. With 8 occupied neighbors, that means at least 3 of its own color, so it accepts 5 of the other. Each discontent household moves to a random empty cell; repeat until everyone is content. Show the grid before and after and measure the average share of like-colored neighbors: it starts near 50 %. Where does it end? How many points is that above the random board, and how many above the 30 % they asked for?

Then replace the 30 % by 10 %, 20 %, up to 70 % and plot what households get against what they ask for. Judge each result against the random board's 50 %, not against the demand: 10 % and 20 % stay within 10 points of it, the largest jump (about 18 points) is from 20 % to 30 %, and separation is nearly total from 60 %. Allow 500 rounds. Title each figure with what it shows. Give changes between thresholds in percentage points rather than in words like "half" or "triple". Explain each step as you would to an undergraduate.
```

## Reference analysis

Ask for 30% same-color neighbors, end up with about 75%. On a 50 × 50 grid filled at random with 1,125 blue and 1,125 orange households and 250 empty cells (about 50% of neighbors alike), only about 18% of households are discontent. Yet once each discontent one has moved to a random empty cell (roughly 1,000 moves in 10 to 20 rounds), the board is a patchwork of 1-color neighborhoods. Redone for demands of 10% to 70%, 20 random boards each: 10% leaves the random board as it is (51%), 20% lifts it to 57%, 50% gives 88% (about 7 like neighbors for each unlike one), and separation is nearly total from 60% (98% at 60%, 99.6% at 70%). The textbook computer version of Thomas Schelling's 1971 idea.

## Data

This example doesn't download any data.

Reference: T. C. Schelling, 'Dynamic models of segregation', Journal of Mathematical Sociology 1(2), 143–186 (1971)
