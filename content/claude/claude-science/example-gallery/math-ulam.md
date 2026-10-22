> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# The Ulam spiral: are the primes' diagonal streaks real?

> Compare the share of primes per diagonal on Ulam's 1963 spiral of 1 to 40,401 against as many random odd numbers.

![Primes up to 40,401 on Ulam's spiral, with primes of n² + n + 41 in orange along 2 rays; as many random odd numbers, with no streaks; and histograms of each diagonal's share, wider for the primes.](https://mintcdn.com/claude-ai/F2QP9ubtYgT0edFI/images/claude-science/example-gallery/math-ulam-full-light.webp?fit=max\&auto=format\&n=F2QP9ubtYgT0edFI\&q=85\&s=140ca573e05d853818df9ab149c1f064)

The numbers in your session might differ from this picture and from the summary in [Reference analysis](#reference-analysis).

## Prompt

Copy the prompt and paste it into a new session in [Claude Science](/docs/claude-science/overview.md). By default, Claude asks with a [permission card](/docs/claude-science/core-concepts.md#permission-cards) before it runs code or installs packages.

```text Prompt wrap theme={null}
In 1963 the mathematician Stanisław Ulam, doodling during a long and boring talk, wrote the whole numbers in a square spiral and circled the primes. Recreate his picture. Find all primes up to 40,401 (= 201 × 201) with a sieve of Eratosthenes, and check that 1,229 of them are below 10,000. Write 1, 2, 3, … in a square spiral starting from the center, and mark the primes.

Are the diagonal streaks real, or is my eye fooling me? Draw the same picture with the same number of randomly chosen odd numbers. For every diagonal of odd numbers at least 100 cells long, in both directions, compute the share of marked cells, and compare its standard deviation and range in the 2 pictures.

Then highlight the numbers n² + n + 41 (Euler's polynomial). On this spiral about the first 40 values wind around the center, and from then on they run along 2 straight diagonals. How many of the first 100 are prime, and how many would you expect from typical odd numbers of that size? The first one that is not prime is n = 40, which gives 41 × 41. Which diagonals are rich in primes is predicted by a conjecture of Hardy and Littlewood (1923) that is still unproven: mention it, and describe the rich and poor diagonals without accounting for them. Walk me through your method at undergraduate level.
```

## Reference analysis

Yes. On Ulam's 1963 spiral of 1 to 40,401, the share of primes per diagonal runs from 0 to 48%, against roughly 11 to 32% for as many random odd numbers. Over the 202 diagonals of at least 100 cells that spread is about 2.3 times the random one, so the streaks are real. The sieve finds 4,236 primes, 1,229 of them below 10,000, as published. Euler's n² + n + 41 traces the 2 richest streaks (over 70% prime along its 2 rays, each one half of a diagonal, running outward from the diagonal's cell nearest the center): prime for n = 0 to 39, and for 86 of its first 100 values, where typical odd numbers of that size would give about 29 of 100.

## Data

This example doesn't download any data.

Reference: M. L. Stein, S. M. Ulam and M. B. Wells, 'A visual display of some properties of the distribution of primes', American Mathematical Monthly 71, 516–520 (1964)
