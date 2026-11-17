# Gemini 1.0 Walkthrough Integration Audit

Updated: 2026-11-17
Input: [Gemini Help.md](Gemini%20Help.md)
Status: **Integrated as secondary walkthrough evidence; not promoted wholesale to verified game data.**

## Executive decision

The Gemini report is useful because it supplies timestamped observations from three 1.0 walkthroughs. It is not safe to import its recipe tables as authoritative: the report itself contains incomplete inputs, alternate formulas, inconsistent counts, and claims that directly conflict with the existing 1.0 candidate ledger and earlier versioned sources.

**Decision:** promote only narrow, directly observable mechanics as walkthrough-supported candidates. Keep all recipe formulas in SOURCE_LISTED_NOT_VERIFIED / conflict status until an exact recipe card or repeatable in-game result is available. Do not overwrite the 333-row inventory or its room splits based on the Gemini report.

## 1. Findings to integrate now

| Area | Gemini observation | Existing project alignment | Decision |
|---|---|---|---|
| Bistro rat | Cheese starts the trade; Tomato, Apple, Garlic, Pumpkin appear across early requests | Developer reply supports Cheese-started recipe-picture trade; existing notes support Tomato first | Add timestamped sequence as a candidate, not a complete verified chain |
| Bistro rat extra request | Mushroom Soup after four trades; two Olive variants and Pizza request follow | Earlier notes describe Olive reward branch but not this exact trigger | Add as distinct post-four-trade candidate; do not merge with ordinary chain |
| Bistro friendship | Pizza is associated with Best Friends | Existing project already models rat friendship | Supports a Pizza-trigger candidate; test exact recipe state and timing |
| Bistro countries | Going Global says Unlock seven countries; seven country magnets collected | Existing project tracks seven magnets; only Japan/Mochi independently named | Accept wording/count as walkthrough lead; six unnamed dishes unresolved |
| Rat Level | Code 725; 9 special recipes; OFF/ON state-dependent results | Existing project has 9 Good + 12 Bad slot candidates and unresolved power-state mapping | Add 725 as strong walkthrough lead; do not collapse 21 slots to 9 |
| Cafe phone | Cheese to mouse reveals 21931; call supplies Avocado and Lettuce | Existing interaction plan includes 21931 and handset wait | Corroborating lead; retain call/handset as separate steps |
| Cafe fire | Burnt Panini re-heated in panini machine starts fire | Existing Cafe tests already model this chain | Corroborating lead |
| Cafe safe | Three Bagels produce Void Bagel | Existing QA already has this candidate chain | Corroborating lead; correct mistaken donuts interpretation |
| Cafe emergency | 911 triggers Emergency | Existing achievement research includes Emergency | Corroborating lead; keep Poison Control negative test separate |
| Cafe orders | 12 orders unlock Paintbrush | Existing research has a 20-Coin Paintbrush route from another guide | Conflict: do not encode either as final reward rule until reconciled |

## 2. Conflicts that must remain open

| Topic | Gemini report | Existing 1.0 ledger / earlier evidence | Required handling |
|---|---|---|---|
| Bistro cookbook count | 80 Good + 40 Bad = 120 | Inventory/provenance ledger: 83 Good + 40 Bad = 123; global save screenshot shows 333 total, not per-room splits | **Do not change counts.** Need direct Bistro Good/Bad tab counts |
| Rat Level cookbook count | 9 total special recipes | Inventory/provenance: 9 Good + 12 Bad = 21 candidate slots | Interpret 9 as 9 special/Good recipes only unless evidence proves otherwise; preserve 12 Bad slots |
| Student Dorm To-Do | 5 tasks | Earlier 1.0 walkthrough source lists 6, including cleaning dishes / Coffee Maker and 40 dishes | **Do not remove tasks.** Inspect full task panel |
| Cafe Paintbrush | 12 orders | Earlier guide: save 20 Coins in Piggy Bank | Keep two independent trigger hypotheses; test order count, coin count, and reward timing |
| Rat reward order | Four early rewards: Tomato, Apple, Garlic, Pumpkin; later Mushroom Soup -> Olives | Existing notes also mention Olive as rat reward, but no full ordered chain | Record exact sequence and separate optional branch |
| Seven countries | General seven-magnet rule; no six names | Existing research names Japan/Mochi only | Keep six country-recipe mappings unresolved |
| Rat Level ninth formula | Egg and Pencil plus another unclear Pencil combination | Existing 9 Good / 12 Bad slot model has distinct uncertain inputs | Do not use ambiguous row as a machine-readable formula |
| Bistro formula rows | Placeholders such as third meat/flour, tool/metal, vegetable, all pencils; alternate recipes | Existing conflict register records exact competing formulas | Do not bulk-import; incomplete rows are not executable |

## 3. Evidence-quality audit

The report says its tables are verified from complete video transcripts and operation sequences, but the content does not support treating every row as complete:
- Some recipes have missing ingredients or placeholder labels rather than reproducible item IDs.
- Several entries list alternatives without proving whether they are true alternatives, state variants, or separate outputs.
- Some outputs are described as all X or a vague category, which cannot be implemented deterministically.
- A timestamp plus a player's spoken interpretation is useful evidence, but is not equivalent to a visible recipe card / counter or independent reproduction.
- The report's own uncertainty notes (unnamed countries, unclear ninth Rat Level recipe, skipped unlock steps) contradict a blanket complete verified formula claim.

Confidence labels in the source document are therefore not copied into project verification status.

## 4. Data integrity decisions

1. Keep the current global candidate denominator at **333** and room split at **77 / 112 / 123 / 21** until direct per-room counters or card tabs supersede them.
2. Keep all 333 entries as candidate records, not verified recipes.
3. Keep **332 source-referenced rows + 1 Clutter trigger-only row** as the provenance baseline; Gemini does not repair row-level source-ID mapping.
4. Preserve recipe states as distinct inputs (raw / processed / cooked; appliance and power state).
5. Separate cookbook recipes from non-food discoveries/tools such as Magnet, Big Magnet, Compass, Scissors, and other hidden objects.
6. Do not mix task completion, achievement unlock, Steam achievement sync, and room completion into one boolean.

## 5. Static QA performed

| Check | Result |
|---|---|
| Gemini source file present in repository | PASS |
| Three source video URLs identified | PASS |
| Timestamped mechanic observations extracted | PASS |
| Cross-check against current room totals | PASS — conflicts detected and preserved |
| Cross-check against existing To-Do candidates | PASS — Student Dorm count conflict detected |
| Cross-check against Cafe Paintbrush rule | PASS — 12 orders vs 20 Coins conflict detected |
| Exact, executable import of all Gemini recipe rows | **FAIL / intentionally blocked** — incomplete and ambiguous formula rows |
| In-game execution QA | NOT RUN — no game binary/runtime available in this work session |

This is a static document/data audit, not a claim that game behavior has been executed.

## 6. Research stop rule and implementation boundary

The following are no longer allowed to block all implementation preparation: identifying all seven country dishes; resolving every optional/Bad recipe; finding a perfect physical-physics coefficient match; resolving every recipe row with a vague input in secondary guides.

**Implementation-ready boundary:** data schema, item-state model, room shell, input abstraction, save model, cookbook UI shell, and recipe engine scaffolding may be built with explicit verification flags and disabled/unresolved recipes. Only recipe outputs with exact inputs, room, appliance, state, version and provenance may be enabled as active game rules.

Before a recipe becomes executable, require exact item IDs and states; room and appliance; ordered/unordered input rule if relevant; version scope; source IDs and evidence location; resolved conflict status or separately represented alternatives; one positive and one negative QA case.

Before declaring the research gate passed, require 333 candidate identities reconciled; no duplicate IDs or silently double-counted names; all room task lists reconciled against 1.0 panels; all P0/P1 contradictions resolved or isolated behind non-blocking flags; Critic approval for the selected implementation scope.

## 7. Verdict

**Gemini report: useful secondary evidence, not an authoritative replacement for the current database.**

Broad research collection can stop expanding. The next work should be reconciliation and implementation preparation in parallel, not another indefinite search for every possible recipe. Current project status: **Research Only / implementation preparation permitted / full gameplay implementation not yet approved**.