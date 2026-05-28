---
name: mining
description: Where diamonds spawn in Minecraft 1.20.
---

Diamond ore generation peaks at **y ≈ -58** in Minecraft 1.18+. The
pre-1.18 advice of y=11 is obsolete.

Below y=0, the ore is almost always `deepslate_diamond_ore`, not
`diamond_ore` — search for both names.

An **iron_pickaxe is required** — diamond ore mined with a
stone_pickaxe or weaker drops nothing. Craft the iron_pickaxe (3
iron_ingot + 2 sticks at a placed crafting_table) before mining
diamond. A diamond_pickaxe is not required.

**To descend quickly**, call `go_near` with your current x/z and a
deep y (e.g. `{"pos": {"x": <x>, "y": -55, "z": <z>}}`) — the
pathfinder digs straight down in one action. Don't `mine_block`
stone repeatedly to descend; it wastes turns and pickaxe durability.

After exhausting a vein, **relocate** — `go_near` to a position 30+
blocks away horizontally at the same y before searching again.
Diamond veins do not cluster; tunneling the same corridor repeatedly
wastes turns.

(This skill is intentionally minimal. It's an example of what
attaching a skill does — it puts these facts in the agent's context.
Edit this file to add more, or write strategy directly in your
AGENT['system'] prompt.)
