> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# A first X-ray diffraction pattern: why silicon shows 6 peaks and salt 9

> Simulate the X-ray powder patterns of silicon and table salt and label every peak with Bragg's law.

<div className="example-gallery-page">
  <Frame>
    <img className="block dark:hidden" src="https://mintcdn.com/claude-ai/F2QP9ubtYgT0edFI/images/claude-science/example-gallery/mat-xrd-full-light.webp?fit=max&auto=format&n=F2QP9ubtYgT0edFI&q=85&s=6d56de735b8fe6c1fd456f7259fc7d4d" alt="Simulated X-ray diffraction patterns: silicon has 6 labeled peaks, with 200, 222, and 420 marked absent; rock salt has 9." width="1600" height="980" data-path="images/claude-science/example-gallery/mat-xrd-full-light.webp" />

    <img className="hidden dark:block" src="https://mintcdn.com/claude-ai/F2QP9ubtYgT0edFI/images/claude-science/example-gallery/mat-xrd-full-dark.webp?fit=max&auto=format&n=F2QP9ubtYgT0edFI&q=85&s=ce7e07ffd94f457100ac376aa7a18fab" alt="Simulated X-ray diffraction patterns: silicon has 6 labeled peaks, with 200, 222, and 420 marked absent; rock salt has 9." width="1600" height="980" data-path="images/claude-science/example-gallery/mat-xrd-full-dark.webp" />
  </Frame>
</div>

The numbers in your session might differ from this picture and from the summary in [Reference analysis](#reference-analysis).

## Prompt

Copy the prompt and paste it into a new session in [Claude Science](/docs/claude-science/overview). By default, Claude asks with a [permission card](/docs/claude-science/core-concepts#permission-cards) before it runs code or installs packages.

```text Prompt wrap theme={null}
X-ray diffraction is how we know where the atoms sit in a crystal. Simulate the powder diffraction patterns of silicon (diamond structure, a = 5.4311 Å) and rock salt (NaCl, a = 5.6402 Å) with pymatgen, for copper Kα₁ X-rays (wavelength="CuKa1", λ = 1.54056 Å) and angles 2θ up to 90°. Nothing needs downloading. Label every peak with its Miller indices hkl, and check each angle by hand with Bragg's law, λ = 2d sin θ, where d = a/√(h²+k²+l²). Both crystals share a face-centered cubic lattice, which allows 9 reflections in this range, yet silicon shows only 6: show that its 2-atom basis cancels 200, 222 and 420. In salt the all-odd peaks (111, 311, 331) are weak because Na and Cl scatter out of phase: show that too. Leave out other salts and what-ifs such as Na and Cl scattering equally, and round every number once, from its full-precision value. Put both patterns in 1 figure. Explain each step as you would to an undergraduate.
```

## Reference analysis

Simulates the X-ray powder patterns of silicon and table salt and labels every peak with Bragg's law. Both share a face-centered cubic lattice, yet below 2θ = 90° salt shows 9 peaks and silicon 6, because silicon's 2-atom basis cancels the 200, 222, and 420 reflections.

## Data

This example doesn't download any data.
