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
- The exact 100% formula is not fully specified in readable official text.

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

Bistro known interactions:
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
- Whether Coioioin needs only three matching coin faces or the blue switch + red toss interaction.

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

At least four task entries are supported by official update notes and 1.0 player walkthroughs:
1. Clean the kitchen.
2. Trade with the rat by the Blue Teapot (offer Cheese).
3. Complete 8 orders (official v3.0ea added this To-Do).
4. Set the kitchen on fire (Burnt Panini cooked a second time).

Other progression blockers noted by the 1.0 route include phone stock / 21931 call, collecting order Coins, obtaining an Espresso Cup, opening the Safe, and completing the fire-alarm interaction. These may be subtasks, puzzle gates, or additional ledger entries; do not count them as To-Do rows until the actual UI is seen.
