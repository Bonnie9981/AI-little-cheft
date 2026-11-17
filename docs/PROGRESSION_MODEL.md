# Progression & Unlock State Model

Updated: 2026-11-16  
Target: 1.0 / v1.1. This is a state model, not a claim that all hidden conditions are fully known.

## 1. Global structure

Main Menu
- Letter button → Peanut Butter unlock (saved)
- Credits → 12 hidden rats → Credits To You
- Logo “c” → Is This Logo Taken?
- My Room (hub)
  - Student Dorm (Level 1)
    - Cafe Job (Level 2)
      - Bistro (Level 3)
        - Rat Level (secret level)

- My Room is the hub and is not a fourth main kitchen.
- The three main kitchens are Student Dorm, Cafe Job, and Bistro.
- Official 1.0 announcement says the secret Rat Level is unlocked after all three main kitchens reach 100%.
- The 1.0 completion route states that each kitchen has its own recipe and task ledger. Both Good and Bad tabs must be audited; exact percentage arithmetic is still not available.

## 2. Room state

Each room should have separate progress fields:

- discovered_good_recipe_ids
- discovered_bad_recipe_ids
- completed_todo_ids
- unlocked_item_ids
- completed_puzzle_ids
- achievement_flags
- scene_interaction_states
- room_completion_percent (derived from confirmed game rules, not hardcoded to recipe count only)

Do not use a single is_complete flag to represent all progress.

## 3. Student Dorm → Cafe Job

Known six Student Dorm To-Do tasks from the 1.0 completion route:
1. Cook eight pasta dishes using Pasta or Ramen as one input.
2. Borrow Shane's Cheese: find D2 key, unlock Shane's cabinet, then use Cheese in a Good dish (e.g. Grilled Cheese).
3. Play all three cassettes: play Red and Green separately, combine Red + Green into Remix, then play Remix.
4. Make Coffee: clean dishes, put utensils away to reveal Coffee Maker, place it on the gas stove and brew.
5. Water Basil: wet Sponge under the tap and use it on the plant, or leave the faucet running until it reaches Basil.
6. Cook new dishes: discover 40 total Good + Bad dishes.

Room completion uses both recipe tabs and the task ledger. The 1.0 completion guide explicitly says to inspect both recipe tabs and finish state-changing / non-food recipes; exact counter arithmetic still needs in-game verification.

Additional achievements: I Smell Cheese, Squeaky Clean, Flooded, A Lot to the Right, Fruit Samurai, To Infinity.

## 4. Cafe Job → Bistro

Known Cafe tasks / unlock actions:
- Clean the kitchen.
- Trade Cheese with the mouse by the Blue Teapot.
- Complete 8 orders (official v3.0ea To-Do).
- Set the kitchen on fire using Burnt Panini cooked a second time.
- Complete recipe discovery and the required Level 2 To-Do list.
- Mouse trade: torn paper goes to phone; dial 21931; pick up handset and wait for call completion; unlock Avocado and Lettuce.
- Complete orders to earn Coins; Coin can be used for Security Card and other recipes.
- Photo + Coin → Security Card → open Safe → discover Void Bagel.
- Additional achievements: Fair Trade, What's The Emergency, Aw That's Hot, Nothing Nowhere.

At least four Level 2 task categories are known (clean, rat trade, 8 orders, fire). The exact task count and wording remain unverified. The Japanese guide's phrase “8 tasks added” may refer to the 8-order target rather than eight separate To-Do rows.

Open question:
- Does Cafe 100% require all 71 Good + 41 Bad recipes, all To-Do tasks, or both?

## 5. Bistro → Rat Level

Bistro known To-Do / progression interactions:
- Clean the kitchen with the Cloth (explicitly shown as the first Bistro To-Do in the Japanese Level 3 walkthrough).
- Trade with the rat (explicitly shown as the next Bistro To-Do; offer Cheese to start the request chain).

Other Bistro completion interactions:
- Unlock Scissors by placing empty Mixer jar in Cooking Pot.
- Reveal hidden Mixer switch beneath plant leaves; repair / activate fuse box in planter.
- Use Mixer to create processed ingredients.
- Offer Cheese to rat behind extractor-hood door; follow recipe drawings to receive new ingredients.
- Complete seven country dishes and collect seven magnets for Going Global.
- Sort five wine bottles by label height, shortest to tallest.
- Cut hanging ropes with Scissors.
- Run Mixer second and third times after grinding Pumpkin/Tomato/Meat to make a mess for Messing Around.
- Complete all rat requests until the heart / thank-you note for Best Friends.
- Discover all required Good and Bad recipes.

Official 1.0 gate:
- Rat Level unlocks only after Student Dorm, Cafe Job, and Bistro are all at 100%.

Open questions:
- Does Bistro 100% require all 84 Good + 39 Bad candidate recipes, all rat requests, and all puzzles?
- What are the seven country dish names and the exact order of rat requests / rewards?

## 6. Rat Level completion

Known puzzle sequence:
1. Click picture / portrait to reveal anti-gravity switch.
2. Activate anti-gravity to float objects and expose note in planter.
3. Click wine bottle label to reveal keypad.
4. Enter the three-digit code from the planter note.
5. Unlock cooker power control.
6. Use Electric Can Cooker with max two ingredients and low/high power states.
7. Discover 9 Good slots and 12 Bad slots (candidate count).
8. Complete Rat Level to 100% for Little Rat.

Open questions:
- Exact three-digit code.
- Whether OFF maps to low and ON maps to high.
- Rat Level Eggshell/Leaf and Egg/Pencil/Pasta recipe slot conflicts.
- Whether the blue switch / red-marked toss area mentioned in one player report is an optional interaction or unrelated; official achievement text and multiple player guides only require the same coin face three times in a row.

## 7. My Room and post-game

Known:
- Unpack box / open boxes for Unpacked.
- Picture frame interaction for Tilted.
- Sort books for Bookworm.
- Put 15 Post-it notes on wall simultaneously for Post A Lot.
- Save 20 Coins in Piggy Bank to unlock paintbrush; customize wallpaper, wood type, and poster frames.
- After completing the main game, a birthday cake and letter from Mom may appear; candles can be interacted with.

Open questions:
- Exact trigger for birthday cake / letter (all three main kitchens vs Rat Level vs all To-Do tasks).
- Whether birthday cake and candle state persist after exiting.
- Exact book sorting order.

## 8. Completion semantics

Keep these distinct:
- Recipe completion: Good and Bad recipe discovery.
- To-Do completion: task list.
- Puzzle completion: hidden mechanisms and item unlocks.
- Room completion: displayed 0–100% level progress.
- Achievement completion: 26 Steam-like achievements.
- Secret-level completion: Rat Level 100%.

The 1.0 completion route says each kitchen has a separate recipe and task ledger, and specifically advises checking both recipe tabs. Treat both Good and Bad recipes plus the room's To-Do / task ledger as required components of room completion, while keeping the exact percent formula configurable until verified from live counters.


## Cafe Job task ledger — known entries (not yet proven exhaustive)

Official v3.0ea patch notes add **one To-Do: complete 8 orders**. They do not state that eight To-Do rows were added. Later v5.1ea patch notes require finishing the Level 2 To-Do list before entering Level 3. The 1.0 completion route and player walkthroughs also show the fire interaction as a Cafe progression blocker. The exact full Level 2 To-Do list is not recovered from the current readable sources.
Confirmed Cafe To-Do entries:
1. Complete 8 orders — explicitly named by v3.0ea.
2. Set the kitchen on fire — explicitly named in the 1.0 walkthrough as a Level 2 To-Do; cook Panini, then cook Burnt Panini a second time.

The September 1.0 player walkthrough says the fire task may fail to register even after the fire starts; the player repeated the fire interaction and then completed remaining orders before Level 3 unlocked. This is a possible task-registration bug, not proof of an extra To-Do row. The exact total Level 2 To-Do count is not recovered. Keep these two confirmed entries separate from phone stock / 21931 call, order Coins, Espresso Cup, Safe, and fire-alarm extinguishing interactions, whose exact relationship to separate To-Do rows is not proven.


## Bistro rat trades vs. country magnets (SRC-054 / SRC-057)

Model these as separate progression tracks with a dependency edge, not as one counter:

1. **Rat trade track:** find the suspicious extractor-hood door → offer Cheese (same starter as Cafe rat) → Tomato is awarded → later hood notes show a dish illustration → cook the depicted dish → receive the next ingredient. Developer confirms this interaction pattern (SRC-054); first-hand EA walkthrough confirms Cheese → Tomato and the note-driven loop (SRC-057).
2. **Country-magnet track:** cook each of seven country dishes → a magnet attaches to the extractor hood → all seven award Going Global. Only Japan = Mochi is textually and visually identified. Apple Mochi is explicitly not the Japan magnet dish; suspicious recipes do not count (SRC-057).
3. **Dependency:** the rat trade chain supplies special ingredients needed by later Bistro recipes, including Apple, Olives, and Garlic according to the 1.0 route (SRC-018/SRC-050). The available sources do not establish that every rat trade directly awards a country magnet.

**Unknowns remain explicit:** full rat request order/reward mapping; all six other country dish mappings; whether final 1.0 retained the same trade count/counter. The 76/76 cookbook counter visible in the 2026-09-09 EA screenshot is a historical snapshot only, not the final 1.0 total.


## Rat Level: planter code evidence boundary (SRC-024)

The 2026-09-10 Japanese 1.0 walkthrough screenshot after the wine-bottle puzzle shows the cooker power control and a yellow note by the planter. The available screenshot makes two '3' digits visible, but does not reliably expose a complete three-digit code; the article text does not transcribe the code. Do not infer 333 or any other code from the partial image. The progression remains: reveal anti-gravity → expose/read planter note → reveal keypad under wine label → enter the exact three-digit clue → unlock adjustable strong/weak output. Strong/weak changes results for the same two ingredients; the mapping to UI OFF/ON labels remains unverified.


## Student Dorm To-Do list: screenshot-backed candidate (SRC-065)
A separately authored October 9 walkthrough includes a legible To-Do screenshot. The six visible tasks are:
1. Cook pasta dishes (0/8)
2. “Borrow” Shane's cheese
3. Play all cassettes (0/3)
4. Make coffee
5. Water the basil
6. Cook new dishes (0/40)

The screenshot visibly displays 0/8, 0/3 and 0/40. The guide states that Chapter 2 unlock requires all Good recipes plus all To-Do tasks. This is third-party 1.0-era walkthrough evidence, not a test run by this project. SD-017 is the acceptance test; exact counter increment rules and unlock behavior remain unexecuted.


## Rat Level source comparison: fifth cold slot and Pasta Bad slots (SRC-066 / SRC-067)
- SRC-067 (Aug 27 Steam guide) lists Cheese + Eggshell as the fifth cold Good candidate and separately lists Pasta + Paperclip among Bad results.
- SRC-066 (v1.0 Chinese guide) lists Cheese + Leaf as the fifth cold Good candidate; it also lists Pasta alone as one Bad slot and another Pasta + Paperclip combination.
- SRC-018's 1.0 walkthrough lists Eggshell for the fifth cold Good candidate and Paperclip + Pasta in its Bad sweep, while noting Eggshell/Leaf uncertainty.
- Keep the cold fifth Good slot and Pasta Bad slots as explicit conflicts until tested in the target client. RAT-024 and RAT-025 are the acceptance tests. RAT-026 captures the keypad reveal sequence without assuming the numeric code.
