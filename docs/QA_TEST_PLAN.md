# QA Test Plan — Little Chef: Cozy Cooking Recreation

Updated: 2026-11-17  
Status: Test design only; implementation has not started.  
Target: 1.0 release behavior with zh-TW localization, desktop and mobile landscape.

## 1. Release acceptance gates

A release candidate cannot pass until:

- All 333 current candidate recipe entries are reconciled against the 1.0 cookbook count. The 333 total is a cross-source estimate, not an official counter.
- Every recipe record has exact input set(s), item states, appliance, room, version, evidence, confidence, and verification status.
- Every Good and Bad recipe is discoverable and recorded exactly once; duplicate source rows do not create duplicate recipe IDs.
- All room unlock tasks and puzzle chains pass.
- All 26 achievements have a trigger test and persistence test.
- Save/load preserves all confirmed progression and customization.
- zh-TW contains no Simplified Chinese glyphs or Mainland-only terminology; no text overflows.
- Desktop mouse and mobile landscape touch controls both pass.
- Critic review has no unresolved P0 or P1 blocker.

## 2. Recipe engine tests

| ID | Test | Expected result |
|---|---|---|
| REC-001 | Submit one-input recipe | Correct recipe resolves for matching room/appliance/state |
| REC-002 | Submit two-input recipe | Correct recipe resolves |
| REC-003 | Submit three-input recipe | Correct recipe resolves |
| REC-004 | Submit four inputs | Rejected or handled according to verified game behavior; never silently truncate |
| REC-005 | Submit same ingredients in different order | Same output only if order-independence is verified |
| REC-006 | Submit raw vs processed item | Different result where recipe requires Ground/Minced/Shredded state |
| REC-007 | Submit same inputs to wrong appliance | No unintended recipe |
| REC-008 | Submit valid alternative input set | All confirmed alternatives unlock the same recipe |
| REC-009 | Submit a Bad Recipe | Correct Bad entry unlocks; Good entry must not unlock |
| REC-010 | Submit duplicate recipe | Cookbook count increments once only |
| REC-011 | Submit unknown combination | No false-positive recipe; item handling matches verified behavior |
| REC-012 | Submit a recipe from another room | Room restriction is respected if present |
| REC-013 | Process item twice | Output matches observed state transition; no accidental alias |
| REC-014 | Save/reload after recipe unlock | Recipe remains discovered and counter remains correct |

Parameterized recipe suite:
- Run one positive test for every candidate recipe in docs/RECIPE_INVENTORY.md.
- Run one negative test for every D-level conflict in docs/RECIPE_CONFLICTS.md.
- Record exact item IDs and state IDs, not localized labels alone.

## 3. Physics and input tests

| ID | Test | Expected result |
|---|---|---|
| PHY-001 | Mouse grab / drag / release | Item follows pointer and falls naturally |
| PHY-002 | Touch grab / drag / release | Same behavior as mouse |
| PHY-003 | Fast release / toss | Release velocity produces a stronger impulse than gentle place |
| PHY-004 | Gentle place | Item settles without an exaggerated impulse |
| PHY-005 | Item-item collision | No tunneling at expected gameplay speeds |
| PHY-006 | Stack objects | Objects can rest and remain stable |
| PHY-007 | Put ingredient in pot | Ingredient enters container and can be cooked |
| PHY-008 | Toss Banana then cut mid-air | Fruit Samurai condition is detected only while airborne |
| PHY-009 | Cut hanging ropes | Scissors interact with each target rope |
| PHY-010 | Flood room | Water level increases and reaches the correct flood threshold |
| PHY-011 | Wet sponge | Sponge state changes and can water Basil |
| PHY-012 | Mixer processing | Raw ingredient transforms into correct processed state |
| PHY-013 | Mixer overload | Repeated blending reaches Messing Around condition |
| PHY-014 | Mobile drag near screen edge | Item remains reachable; scene does not scroll unexpectedly |
| PHY-015 | Rotate / sort objects | Rotation and alignment interactions are stable |

No original mass, friction, elasticity, drag stiffness, or impulse constants are known. Test for behavior and feel; document recreation parameters separately.

## 4. Student Dorm tests

| ID | Test | Expected result |
|---|---|---|
| STD-001 | Solve D2 wall tile puzzle | Key appears |
| STD-002 | Drag key to Shane's lock | Cheese and canned tomatoes become available |
| STD-003 | Open all remaining lockers | All hidden ingredients / items become available |
| STD-004 | Clean dishes | Squeaky Clean triggers |
| STD-005 | Place utensils correctly | Coffee Maker is revealed |
| STD-006 | Brew Coffee | Coffee task completes |
| STD-007 | Play Red and Green cassettes | Both count |
| STD-008 | Combine tapes into Remix and play it | Cassette task completes |
| STD-009 | Make 8 pasta / ramen dishes | Pasta task counter reaches 8 |
| STD-010 | Water Basil with wet sponge | Basil revives |
| STD-011 | Flood room | Flooded triggers |
| STD-012 | Throw item high | To Infinity triggers |
| STD-013 | Align tea boxes | A Lot to the Right triggers |
| STD-014 | Cut Banana mid-air | Fruit Samurai triggers |
| STD-015 | Reach 40 Good + Bad dishes | Cook-new-dishes task completes |
| STD-016 | Complete the Student Dorm Good + Bad recipe tabs and all six To-Do tasks | Student Dorm reaches 100% and Cafe Job unlocks |

The 1.0 completion route says both Good and Bad recipe tabs matter to room completion. Verify the live 100% counter and ensure both tabs plus all six To-Do tasks are complete before marking Student Dorm done.

## 5. Cafe Job tests

| ID | Test | Expected result |
|---|---|---|
| CAF-001 | Offer Cheese to mouse | Torn paper is revealed |
| CAF-002 | Put paper near phone | Phone clue becomes usable |
| CAF-003 | Dial 21931 | Call begins |
| CAF-004 | Pick up handset and wait | Avocado / Lettuce order unlock completes |
| CAF-005 | Complete one order slip | Tip Coin is awarded |
| CAF-006 | Remove completed order slip | New order can appear after delay |
| CAF-007 | Complete 8 orders | Order target counter reaches 8 |
| CAF-008 | Save 20 Coins in Piggy Bank | Paintbrush unlocks in My Room |
| CAF-009 | Use paintbrush | Wallpaper, wood type, poster frame changes save |
| CAF-010 | Photo + Coin | Security Card is created |
| CAF-011 | Use Security Card on Safe | Safe opens |
| CAF-012 | Make three Bagels and cook them | Void Bagel discovery / Nothing Nowhere chain works |
| CAF-013 | Panini → Burnt Panini → recook | Fire starts |
| CAF-014 | Break alarm glass three times | Fire button becomes available |
| CAF-015 | Press exposed button | Fire extinguishes |
| CAF-016 | Complete all Level 2 To-Do | Bistro unlocks |

Confirmed Cafe To-Do candidates: complete 8 orders (official v3.0ea) and set the kitchen on fire (1.0 walkthrough). Clean the kitchen and Trade with the rat are Bistro To-Do entries, not Cafe tasks. The full Cafe task count and whether phone / Safe / Espresso Cup are separate To-Do rows remain unverified. Test cases CAF-001 through CAF-016 cover known actions only; add missing rows after the in-game UI is recovered.

## 6. Bistro tests

| ID | Test | Expected result |
|---|---|---|
| BIS-001 | Put empty Mixer jar in Cooking Pot | Scissors appear |
| BIS-002 | Bring Scissors near plant leaves | Hidden Mixer switch is revealed |
| BIS-003 | Repair / activate fuse box | Mixer becomes usable |
| BIS-004 | Process Tomato | Ground Tomato state appears |
| BIS-005 | Process Meat | Ground Meat state appears |
| BIS-006 | Process Rice | Ground Rice state appears |
| BIS-007 | Process Pumpkin / Apple / Garlic / Cheese | Correct states appear |
| BIS-008 | Offer Cheese to rat | First rat request starts; Tomato reward expected |
| BIS-009 | Complete each rat drawing request | Correct ingredient reward and next request |
| BIS-010 | Finish rat requests | Heart thank-you note / Best Friends |
| BIS-011 | Complete seven country dishes | Seven magnets and Going Global |
| BIS-012 | Sort five wines by label height | Wine About It |
| BIS-013 | Cut hanging ropes | Cut The Rope |
| BIS-014 | Repeatedly use Mixer | Messing Around |
| BIS-015 | Unlock all 84 Good / 39 Bad candidates | Compare with verified 1.0 cookbook counter |
| BIS-016 | Complete Bistro “Clean the kitchen” task using Cloth | To-Do row updates; clean state persists |
| BIS-017 | Complete Bistro “Trade with the rat” task by offering Cheese and completing the first request | To-Do row updates; Tomato reward and next drawing appear |
| BIS-018 | Investigate Clutter without assuming a recipe formula | Record exact interaction / inputs that unlock it; if unavailable, leave trigger unknown and block recipe implementation |
| BIS-019 | Receive a country Magnet, register it for Going Global, then combine it with Scissors | Compass is discovered only after the magnet's registration state; verify whether consuming it affects the magnet ledger |
| BIS-020 | Test rat-reward Magnet directly and after cooking it in the station | Big Magnet candidate resolves; compare the Bad Recipe counter and retain the successful state |

The seven country dishes are not fully identified; BIS-011 remains blocked until the list is recovered.

## 7. Rat Level tests

| ID | Test | Expected result |
|---|---|---|
| RAT-001 | Click portrait / picture | Anti-gravity switch appears |
| RAT-002 | Activate anti-gravity | Objects float and planter note is revealed |
| RAT-003 | Click wine bottle label | Keypad is revealed |
| RAT-004 | Enter three-digit clue from planter note | Power control unlocks |
| RAT-005 | Test low power | Five Good slot candidates resolve |
| RAT-006 | Test high power | Four Good slot candidates resolve |
| RAT-007 | Test every Bad slot | Twelve Bad candidates are reconciled |
| RAT-008 | Click coin repeatedly until same face lands three times consecutively | Legacy/official-description route is tested and result recorded |
| RAT-011 | Press blue-frame switch, then toss coin into red-frame target | Japanese 1.0 first-hand route is tested; record in-game unlock separately from Steam unlock |
| RAT-012 | After in-game Coioioin unlock, close and relaunch game / Steam client | Verify delayed Steam achievement synchronization without confusing it with the gameplay trigger |
| RAT-009 | Complete all Rat recipes | Little Rat / Rat Level completion triggers |

The numeric code is unknown from readable text sources. Do not invent a code. Eggshell/Leaf and Egg/Pencil/Pasta slot variants must be resolved before RAT-005 through RAT-007 pass.

## 8. My Room and achievements

- Verify Unpacked after all moving boxes are opened.
- Verify Tilted after the picture frame falls.
- Verify Post A Lot with 15 Post-it notes at the same time.
- Verify Bookworm with correct book arrangement.
- Verify Is This Logo Taken? by dragging the “c” from the main menu logo.
- Verify Credits To You by finding all 12 rats in credits; progress must persist.
- Verify all 26 achievement triggers and Steam-like unlock state.
- Verify 20-Coin paintbrush, wallpaper, wood type, poster frames, and persistence.
- Verify post-game birthday cake, letter, and candle interaction.

## 9. Localization tests

- All UI strings, recipes, items, achievements, tasks, clues, and descriptions use zh-TW.
- No Simplified Chinese glyphs or Mainland-only terms remain.
- Taiwan terminology uses 起司、馬鈴薯、吐司、可頌、披薩、果昔、調理機.
- Processed states are not collapsed (番茄 / 絞碎番茄; 肉 / 絞碎肉; 米 / 磨碎米).
- Long names fit recipe cards, buttons, book entries, and mobile layout.
- Recipe English keys remain available in debug / research mode.
- Test punctuation, full-width symbols, line wrapping, and fallback fonts.

## 10. Responsive and performance tests

- Desktop: 16:9 and 16:10 windows; mouse interaction.
- Mobile: landscape phone and tablet; touch interaction.
- Test smallest supported viewport, safe areas, browser address-bar resize, and device rotation.
- No essential object is hidden under HUD, cookbook, or To-Do list.
- Drag operations remain responsive at target frame rate.
- Save/load works after refresh, tab close, and offline restart.
- JSON export/import round-trip preserves all confirmed progress.

## 11. Blockers before implementation

1. Complete Cafe Level 2 To-Do list.
2. Identify all seven country dishes and the full rat request / reward sequence.
3. Verify Rat Level code and power-state mapping.
4. Resolve all D-level recipe conflicts, especially Bistro and Rat Level.
5. Confirm 1.0 cookbook counters and the 333 candidate total.
6. Finish zh-TW glossary and review every string.
7. Critic review must accept data completeness, architecture, UX, and QA gates.



## Rat Level two-input exception

Rat Level cooking attempts use at most two ingredients according to the 1.0 player completion guide. Add a dedicated test: a third ingredient must not be accepted by the Rat Level cooker unless a later in-game test contradicts this. Do not apply the main-kitchen three-input assumption to Rat Level.


## Main Menu hidden ingredient tests

- Click the button in the main-menu letter; Peanut Butter appears in the Student Dorm.
- Do not require a Steam Wishlist API or external account connection.
- Save/reload; Peanut Butter unlock remains persisted.
- Verify PB&J, Peanuts, Smoothie, and Good Protein Shake use the unlocked item according to the final recipe evidence.


## Additional achievement location tests

- Student Dorm: D2 tile reveals Shane's key; the separate tile to the right reveals the mouse hole. Cheese held at the mouse hole triggers I Smell Cheese.
- Student Dorm: tea boxes on the top shelf directly right of Jam align into one continuous vine pattern for A Lot to the Right.
- Cafe: dial 911 and pick up handset for What's The Emergency.
- Cafe: Panini → Burnt Panini → recook Burnt Panini for Aw That's Hot.
- Cafe: cook three Bagels together, then use Security Card on Safe to discover Void Bagel for Nothing Nowhere.
- Cafe: give Cheese to mouse near Blue Teapot for Fair Trade.
- Bistro: grind Pumpkin/Tomato/Meat, then run Mixer second and third times to make a large mess for Messing Around; Cloth cleans it afterward.


## Achievement matrix reference

Use docs/ACHIEVEMENT_MATRIX.md as the canonical list of the 26 target achievements. Do not implement the removed Early Access Master of Disaster achievement.


## Student Dorm To-Do exact test list (1.0 route)

- Cook eight dishes with Pasta or Ramen as an ingredient.
- Unlock Shane's cabinet and use Cheese in a Good dish.
- Play Red cassette, Green cassette, combine them into Remix, and play Remix.
- Clean dishes, arrange utensils, reveal Coffee Maker, place it on stove, and brew Coffee.
- Water Basil with wet Sponge or running faucet.
- Discover 40 total Good + Bad dishes.
- Verify both Good and Bad recipe tabs plus all six tasks are required for Student Dorm 100%.


## Cafe To-Do ledger correction

- Official v3.0ea notes add one Level 2 To-Do: “complete 8 orders”. This is one task with an eight-order target, not eight separate tasks.
- v5.1ea says the Level 2 To-Do list must be completed before Level 3 can be played.
- The 1.0 route identifies the fire interaction as a Level 2 To-Do; cleaning and rat trade are confirmed progression actions but their exact To-Do UI labels are not recovered.
- Do not assume a total number of Cafe To-Do rows. Verify the complete live To-Do panel before marking coverage complete.
- Verify Level 3 remains locked until the actual Level 2 To-Do panel is complete.

## Coioioin conflicting interaction test

- Primary candidate: click / flip the coin until the same face lands three times consecutively, matching the Steam achievement description.
- Alternate report: press a blue switch and toss the coin into a red-marked area.
- QA must test the plain coin interaction first, then the switch / target-area route only if the achievement does not trigger. Do not hardcode the switch as a prerequisite without evidence.


## Bistro To-Do / rat sequence tests

- Confirm the first Bistro To-Do is “Clean the kitchen” and can be completed with the Cloth.
- Confirm the next To-Do is “Trade with the rat”; offer Cheese at the extractor-hood door.
- Verify the rat shows one illustrated dish request at a time and awards a new ingredient after the requested dish is cooked.
- Keep Bistro task ledger, rat-trade sequence, country-magnet collection, and Best Friends achievement as separate state variables until the live UI proves their exact coupling.


## Cafe fire-task registration / retry test

- Complete the fire sequence by cooking Panini, then cooking the Burnt Panini again.
- Verify the Level 2 To-Do row updates independently of the Aw That's Hot Steam achievement.
- If the fire row remains unchecked, repeat the fire interaction once and verify whether the task registers; record this as a bug-compatibility case rather than a normal success path.
- After extinguishing the fire, complete remaining orders and verify the Level 3 unlock gate.



## Coioioin evidence conflict (2026-11-17)
- Steam achievement text says same face three times consecutively; an older Steam discussion says click the coin repeatedly.
- A Japanese 1.0 first-hand walkthrough explicitly says this is not merely random same-face repetition: press the blue-frame switch, then throw the coin into the red-frame area. The author also reports the Steam achievement appeared only after closing/relaunching the game.
- QA must test both interaction routes and keep gameplay unlock state separate from Steam sync. Do not hardcode either route as final until the interaction is observed.


## Rat quest persistence and counter regression tests (SRC-048)

| ID | Test | Expected result |
|---|---|---|
| BIS-021 | Save/reload or leave/re-enter Bistro after the rat displays a request | Current request index and already-claimed rewards persist; quest does not restart |
| BIS-022 | Re-interact with the rat after claiming a reward, including after reload | No duplicate reward; next request appears once; To-Do counter never displays a negative value |
| RAT-013 | Run the five cold Good candidates in documented order and inspect the live counter after each | Each valid result advances exactly one distinct slot; Eggshell/Leaf alternative is only tested if the expected slot does not advance |
| RAT-014 | Compare cooker OFF/ON states with Japanese guide's weak/strong power states | Record the actual mapping; do not assume OFF=low or ON=high |
| RAT-015 | Attempt to add a third ingredient to Rat Level cooker | Third input is rejected or cannot affect result; document if live behavior contradicts the two-input rule |

SRC-048 confirms that the original EA build had a rat-trade To-Do counter bug (-1) and a quest-restart bug, both listed as fixed in v5.1ea. These are regression-compatibility tests, not claims that the current 1.0 build still contains the bugs.


## Version-sensitive Bistro formula regression (SRC-049 / SRC-050)
| ID | Test | Expected evidence |
|---|---|---|
| BIS-023 | In current v1.1+ client, test Meat + Wine + Ground Tomato for Goulash | Record exact output card, cookbook registration, and save/reload persistence; old guide candidate is not accepted as final until confirmed |
| BIS-024 | In current v1.1+ client, test Olives + Wine + Ground Tomato for Tomato Cocktail | Record exact output card, cookbook registration, and save/reload persistence; old guide candidate is not accepted as final until confirmed |
| BIS-025 | Compare Tomato Juice using whole Tomato vs Ground Tomato | Determine which state registers the intended cookbook slot; preserve both attempts and outputs |
| BIS-026 | Compare Dirty Chai Latte using Tea + Milk + Coffee vs Tea + Milk + Coffee Beans | Confirm exact object identity/state and resulting card; community comment correction is not sufficient alone |
