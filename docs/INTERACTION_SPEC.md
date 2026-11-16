# Interaction & Physics Specification

Updated: 2026-11-16  
Scope: Research specification for the 1.0-style Web recreation.  
Important distinction: “Observed” means supported by source or player evidence. “Implementation choice” means a proposed way to reproduce the behavior, not a claim about the original engine.

## 1. Evidence-backed interaction model

| Behavior | Evidence | Status |
|---|---|---|
| Drag objects | Official store and 1.0 press release | Observed |
| Toss / throw objects | Official store and 1.0 press release | Observed |
| Gently place objects | Official 1.0 press release | Observed |
| Combine ingredients | Official store and press release | Observed |
| Put up to three ingredients into an appliance, then activate it | Pixel Questing Chapter 1 guide | Community-confirmed; verify in each room |
| Objects have weight and motion | Official store / press release | Observed |
| Objects react dynamically to movement | Official 1.0 press release | Observed |
| Cut a banana while airborne | Achievement / Student Dorm walkthrough | Observed |
| Cut hanging ropes with scissors | Bistro guide | Observed |
| Flood kitchen with running tap | Achievement / Student Dorm walkthrough | Observed |
| Water basil with wet sponge or rising water | Student Dorm walkthrough | Observed |
| Sort tea boxes / book spines | Achievement guides | Observed |
| Mix / grind ingredients | Bistro guide and recipes | Observed |
| Overload Mixer until kitchen becomes chaotic | Bistro achievement guide | Observed |
| Sort five wine bottles by label height, shortest to tallest | Steam player discussion | Community-confirmed |
| Power-state changes alter Rat Level recipes | 1.0 player walkthrough | Community-confirmed |

## 2. Input abstraction

Use one shared interaction layer for desktop mouse and mobile touch.

| Input | Desktop | Mobile landscape | Expected behavior |
|---|---|---|---|
| Grab | Left mouse down | One-finger touch | Pick up movable item |
| Drag | Mouse move while held | Finger move while held | Move item with pointer constraint |
| Release | Mouse up | Lift finger | Item falls / settles under physics |
| Toss | Release with pointer velocity | Release with swipe velocity | Apply impulse based on drag velocity |
| Gentle place | Short, low-velocity release | Short, low-velocity release | Avoid large impulse |
| Click / activate | Left click | Tap | Activate appliance or interactable |
| Multi-select | Not assumed | Not assumed | Do not invent unless verified |

The exact toss scaling, drag stiffness, and input thresholds are implementation parameters to tune; no original numeric values are known.

## 3. Object categories

| Category | Examples | Typical capabilities |
|---|---|---|
| Ingredient | Bread, Meat, Tomato, Cheese, Rice, Milk | Drag, toss, combine, cook, process |
| Processed ingredient | Ground Tomato, Ground Meat, Ground Rice, Minced Garlic | Combine, cook |
| Tool | Knife, Scissors, Wooden Spoon, Magnet, Pencil | Drag, toss, cut, stir, reveal, combine |
| Container | Cup, Mug, Paper Cup, Pot, Bottle, Jar | Hold, fill, empty, insert, combine |
| Appliance | Cooking Pot, Toaster, Microwave Oven, Espresso Machine, Mixer, Electric Can Cooker | Accept inputs, activate, change state, output |
| Clue | Note, Photo, Label, Newspaper, Order Slip | Click, read, reveal, dial, sort |
| Puzzle interactable | Keypad, Switch, Fuse Box, Safe, Lock, Phone | Click, toggle, press, unlock, dial |
| Environment | Sink, Faucet, Shelf, Cabinet, Plant, Hanging Rope | Toggle, reveal, flood, water, cut |
| Character | Mouse / Rat | Show request, exchange item, progress quest |

A movable object is not automatically an ingredient. Non-food items are central to Bad Recipes and puzzle interactions.

## 4. Item state model

Use separate item IDs or explicit states for:

- Raw / processed: Tomato → Ground Tomato; Meat → Ground Meat; Rice → Ground Rice; Pumpkin → Ground Pumpkin; Apple → Ground Apple; Garlic → Minced Garlic; Cheese → Shredded Cheese.
- Bread: Bread → Toast → Burnt Toast; Bread / Toast can become wet → Soggy Toast.
- Coffee: Coffee Beans → Espresso Shot → Filled Coffee Cup / Cup of Espresso; double extraction is a separate state / result.
- Panini: Panini → Burnt Panini.
- Egg: Egg → Eggshell.
- Container: empty → filled; closed → open; intact → broken.
- Environment: dry → wet / flooded.
- Puzzle: locked → unlocked; switch off → on; power low → high.
- Wine: unlabelled / hidden label → revealed label; bottle order position.

Never collapse raw and processed states into the same item.

## 5. Appliance model

| Room | Main appliance | Additional devices | Conditions |
|---|---|---|---|
| Student Dorm | Cooking Pot | Toaster, Coffee Maker, Sink/Faucet | Pot activation; toast state; coffee setup task |
| Cafe Job | Microwave Oven | Espresso Machine, phone, safe | Microwave activation; espresso cup placement; order tickets |
| Bistro | Cooking Pot | Mixer / Blender | Mixer power switch; ground outputs; rat trades |
| Rat Level | Electric Can Cooker (descriptive name) | Power control, keypad, anti-gravity switch | Low/high power state; recipe slot state |

Rat Level is not modeled as a conventional oven. A 1.0 player guide describes a powered tin-can cooker with strong/weak output; Steam guide uses OFF/ON labels. Exact mapping remains to be verified.

## 6. Puzzle / environment interaction chains

### Student Dorm
- Shane locker: click wall tile repeatedly at D2 → reveal key → drag key to red lock → unlock Cheese and canned tomatoes.
- Sink: wet sponge → clean dishes → place utensils in correct spots → reveal Coffee Maker.
- Basil: wet sponge or rising tap water → water Basil.
- Cassette player: play Red and Green tapes; combine them into Remix and play Remix.
- Flooded: leave tap running until the kitchen is flooded.
- Fruit Samurai: toss Banana, cut it while airborne.
- Tea box sorting: align box designs.

### Cafe Job
- Mouse / Blue Teapot: offer Cheese → receive torn paper → place paper by phone → dial 21931 → pick up handset and finish call → order Avocado and Lettuce.
- Order slips: match illustrated dish → complete order → receive tip Coin; remove completed slip, wait for replacement.
- Safe: Photo + Coin → Security Card → open Safe → discover Void Bagel.
- Fire: Panini → Burnt Panini → cook Burnt Panini again → fire; break alarm glass three times → press exposed button to extinguish.
- My Room: save 20 Coins in Piggy Bank → unlock paintbrush → customize wallpaper, wood type, poster frames.

### Bistro
- Scissors: place empty Mixer jar into Cooking Pot.
- Hidden Mixer switch: bring Scissors near plant leaves.
- Mixer power: repair / interact with fuse box in planter.
- Rat trade: find extractor-hood door → offer Cheese → follow drawing requests → trade for ingredients.
- Wine About It: sort five bottles by label height, shortest to tallest.
- Going Global: complete seven country dishes; only Mochi/Japan is currently identified by readable text.
- Cut The Rope: cut hanging objects / ropes with Scissors.
- Messing Around: continue using Mixer until the kitchen becomes chaotic.

### Rat Level
- Click picture / portrait to reveal anti-gravity switch.
- Activate anti-gravity; floating objects expose a note in planter.
- Click wine bottle label to expose keypad.
- Enter the three-digit code from planter note.
- Unlock cooker power control; test low and high power.
- Coioioin: 1.0 player report says press blue switch, then toss coin into red-marked area; verify if three matching faces are also required.

## 7. Physics implementation requirements

Proposed modules (implementation design, not original internal architecture):

- Rigidbody / mass: movable objects with mass and gravity.
- Collision: item-item, item-environment, item-container collisions.
- PointerConstraint: stable drag under mouse/touch.
- ThrowImpulse: convert pointer velocity into release impulse.
- Stack / Rest: allow objects to settle and stack.
- Breakable: break or transform on appropriate collisions / actions.
- Water: faucet source, liquid fill level, buoyancy / wet states.
- Cutting: knife/scissors interaction with target object; airborne cut condition.
- Processing: Mixer transforms raw ingredient into processed state.
- ApplianceInput: accept 1–3 items, evaluate recipe conditions, produce output.
- PuzzleInteractable: switches, locks, keypad, phone, safe, labels, order slips.

No original physics coefficients are public. All numeric values must be tuned against observable feel and stored as recreation parameters, never represented as copied original values.

## 8. Acceptance tests

- Mouse and touch can both grab, drag, release, and toss the same item.
- A gently placed item does not receive the same impulse as a fast toss.
- An item dropped into the wrong appliance does not silently produce a recipe unless a matching condition exists.
- Appliance accepts up to three candidate inputs; a fourth input is rejected or handled according to later verification.
- Ground Tomato and raw Tomato produce distinct recipe outcomes where evidence says so.
- Coffee Beans, Espresso Shot, and Filled Coffee Cup remain distinct.
- Toast, Burnt Toast, and Soggy Toast remain distinct.
- Banana can be thrown and cut mid-air.
- Tap can flood the Student Dorm and the flood state triggers the correct achievement / task.
- Mixer can process ingredients and become chaotic after repeated activation.
- Rat cooker recipes differ by power state.
- UI remains usable in mobile landscape without losing drag precision or covering key scene objects.
- Save/reload preserves unlocked rooms, recipe discovery, tasks, achievements, coin balance, and room customization. Whether object positions persist remains an explicit design decision until verified.

## 9. Open questions

- Does every appliance consume inputs on successful and unsuccessful combinations?
- Does ingredient order matter?
- Is the three-item limit global or appliance-specific?
- Are items allowed to remain inside an appliance between activations?
- What exact physical properties differ among objects?
- What is the exact Rat Level three-digit code and OFF/ON-to-low/high mapping?
- Are object positions saved, or only progress / customization?
