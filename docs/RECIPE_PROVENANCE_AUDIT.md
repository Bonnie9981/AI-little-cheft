# Recipe Provenance Audit — 333 Candidate Rows

Updated: 2026-11-17  
Source inventory: [RECIPE_INVENTORY.md](RECIPE_INVENTORY.md)  
Status: **Audit baseline created; row-level formula provenance is NOT complete.**

## Audit result

The 333-name candidate inventory now has row-level source formula/action references for 332 rows. The remaining Clutter candidate has a trigger hint in SRC-024 but no reproducible formula or action mapping. Source references establish that a guide lists a formula or action; they do not establish correctness or in-game verification. Conflicted classifications and slot alternatives remain explicitly flagged.

| Room | Good | Bad | Total | Name-list source family | Formula provenance |
|---|---:|---:|---:|---|---|
| Student Dorm | 48 | 29 | 77 | SRC-019 | 77 rows source-listed; not in-game verified |
| Cafe Job | 71 | 41 | 112 | SRC-020 | 112 rows source-listed; duplicate Coffee Cake entry deduplicated; not in-game verified |
| Bistro | 83 | 40 | 123 | SRC-015, SRC-016, SRC-018, SRC-038, SRC-050 | 121 source-listed; 1 classification conflict; 1 unmapped (Clutter) |
| Rat Level | 9 | 12 | 21 | SRC-017, SRC-050, SRC-052 | 21 slot inputs source-listed; four slots retain explicit candidate conflicts; not in-game verified |
| **Total** | **211** | **122** | **333** — | **332 rows have source formula/action references; Clutter remains unmapped; none are in-game verified** |

Name source IDs identify the source family from which a candidate name/list was transcribed or reconciled. They do not mean the formula is confirmed by that source. Formula source IDs are deliberately UNMAPPED until an exact per-recipe formula citation is assigned. Do not mark a formula verified based on a room-level source alone.

## Row-level register

| Candidate ID | Room | Type | Recipe name | Candidate/list source IDs | Formula source IDs | Formula audit status |
|---|---|---|---|---|---|---|
| SD-G-001 | Student Dorm | Good | Baked Banana | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-002 | Student Dorm | Good | Banana Bread | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-003 | Student Dorm | Good | Beans on Toast | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-004 | Student Dorm | Good | Boiled Eggs | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-005 | Student Dorm | Good | Coffee | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-006 | Student Dorm | Good | Savory Sandwich | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-007 | Student Dorm | Good | Cheesy Ramen | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-008 | Student Dorm | Good | Chili Sin Carne | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-009 | Student Dorm | Good | Warm Beans | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-010 | Student Dorm | Good | Plain Ramen | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-011 | Student Dorm | Good | French Toast | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-012 | Student Dorm | Good | Fries | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-013 | Student Dorm | Good | Grilled Cheese | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-014 | Student Dorm | Good | Hot Milk | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-015 | Student Dorm | Good | Mac and Cheese | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-016 | Student Dorm | Good | Mashed Potatoes | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-017 | Student Dorm | Good | Omelette | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-018 | Student Dorm | Good | Pasta A La Carbonara | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-019 | Student Dorm | Good | Pasta | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-020 | Student Dorm | Good | PB&J | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-021 | Student Dorm | Good | PB&J Sandwich | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-022 | Student Dorm | Good | Pesto | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-023 | Student Dorm | Good | Ramen | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-024 | Student Dorm | Good | English Breakfast | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-025 | Student Dorm | Good | Scrambled Eggs | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-026 | Student Dorm | Good | Decent Protein Shake | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-027 | Student Dorm | Good | Sweet Sandwich | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-028 | Student Dorm | Good | Red Pasta | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-029 | Student Dorm | Good | Tomato Soup | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-030 | Student Dorm | Good | Toast | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-031 | Student Dorm | Good | Baked Potato | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-032 | Student Dorm | Good | Creamy Tomato Soup | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-033 | Student Dorm | Good | Cheese Dip | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-034 | Student Dorm | Good | Cheese Fondue | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-035 | Student Dorm | Good | Pasta E Fagioli | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-036 | Student Dorm | Good | Milk and Pasta | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-037 | Student Dorm | Good | Green Pasta | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-038 | Student Dorm | Good | Cheese Pasta | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-039 | Student Dorm | Good | Egg Pasta | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-040 | Student Dorm | Good | Good Protein Shake | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-041 | Student Dorm | Good | Peanuts | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-042 | Student Dorm | Good | Banana Pancake | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-043 | Student Dorm | Good | Smoothie | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-044 | Student Dorm | Good | Cheese Jamwich | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-045 | Student Dorm | Good | Banana Milk | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-046 | Student Dorm | Good | Potato Bread | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-047 | Student Dorm | Good | Hash Brown | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-G-048 | Student Dorm | Good | Tomato/Egg Stir Fry | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-B-001 | Student Dorm | Bad | Mystery Meal | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-B-002 | Student Dorm | Bad | Horrible Sandwich | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-B-003 | Student Dorm | Bad | Beany Mess | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-B-004 | Student Dorm | Bad | Carb Overload | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-B-005 | Student Dorm | Bad | Carb Sandwich | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-B-006 | Student Dorm | Bad | Tomato Mess | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-B-007 | Student Dorm | Bad | Bad Protein Shake | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-B-008 | Student Dorm | Bad | SpongeMan | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-B-009 | Student Dorm | Bad | Bad Ramen | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-B-010 | Student Dorm | Bad | Basta | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-B-011 | Student Dorm | Bad | Pre Workout Disaster | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-B-012 | Student Dorm | Bad | Sponge Sandwich | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-B-013 | Student Dorm | Bad | Remix | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-B-014 | Student Dorm | Bad | Musical Dish | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-B-015 | Student Dorm | Bad | Katana | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-B-016 | Student Dorm | Bad | Canned Food | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-B-017 | Student Dorm | Bad | Terrible Smoothie | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-B-018 | Student Dorm | Bad | Breadless Sandwich | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-B-019 | Student Dorm | Bad | Nothing | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-B-020 | Student Dorm | Bad | Tape Spaghetti | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-B-021 | Student Dorm | Bad | Heavy Metal | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-B-022 | Student Dorm | Bad | Iron Ingot | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-B-023 | Student Dorm | Bad | Secret Sauce | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-B-024 | Student Dorm | Bad | Food Monster | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-B-025 | Student Dorm | Bad | Mold | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-B-026 | Student Dorm | Bad | Burnt Toast | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-B-027 | Student Dorm | Bad | Soggy Toast | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-B-028 | Student Dorm | Bad | Frankenstein's Toast | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| SD-B-029 | Student Dorm | Bad | Milk Bread | SRC-019 | SRC-019 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-001 | Cafe Job | Good | Tea | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-002 | Cafe Job | Good | Chai Latte | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-003 | Cafe Job | Good | Panini | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-004 | Cafe Job | Good | Savory Panini | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-005 | Cafe Job | Good | Black Coffee | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-006 | Cafe Job | Good | Chocolate Spread | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-007 | Cafe Job | Good | Chocolate Cake | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-008 | Cafe Job | Good | Coffee Cake | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-009 | Cafe Job | Good | Cupcake | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-010 | Cafe Job | Good | To Go Drink | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-011 | Cafe Job | Good | Tres Leches | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-012 | Cafe Job | Good | Marble Cake | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-013 | Cafe Job | Good | Cake Pop | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-014 | Cafe Job | Good | Cafe au Lait | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-015 | Cafe Job | Good | Espresso Shot | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-016 | Cafe Job | Good | Babyccino | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-017 | Cafe Job | Good | Tiramisu | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-018 | Cafe Job | Good | Jam | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-019 | Cafe Job | Good | Sweet Bagel | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-020 | Cafe Job | Good | Avocado Brownies | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-021 | Cafe Job | Good | Savory Croissant | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-022 | Cafe Job | Good | Sweet Croissant | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-023 | Cafe Job | Good | Berry Tea | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-024 | Cafe Job | Good | Chocolate Covered Strawberries | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-025 | Cafe Job | Good | Mug Cake | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-026 | Cafe Job | Good | Grilled Lettuce | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-027 | Cafe Job | Good | Salad | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-028 | Cafe Job | Good | Mug Bread | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-029 | Cafe Job | Good | Avocado Milk | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-030 | Cafe Job | Good | Green Smoothie | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-031 | Cafe Job | Good | Strawberry Cake | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-032 | Cafe Job | Good | Neapolitan Cake | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-033 | Cafe Job | Good | Strawberry Tiramisu | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-034 | Cafe Job | Good | Strawberry Cake Parfait | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-035 | Cafe Job | Good | Hot Cocoa | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-036 | Cafe Job | Good | Latte | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-037 | Cafe Job | Good | Pink Donut | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-038 | Cafe Job | Good | Mozzarella | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-039 | Cafe Job | Good | Chocolate Bomb | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-040 | Cafe Job | Good | Brownies | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-041 | Cafe Job | Good | Chocolate Donut | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-042 | Cafe Job | Good | Guacamole | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-043 | Cafe Job | Good | Cheese and Berries | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-044 | Cafe Job | Good | Strawberry Cheesecake | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-045 | Cafe Job | Good | Pain Au Chocolat | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-046 | Cafe Job | Good | Canned Bread | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-047 | Cafe Job | Good | Croutons | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-048 | Cafe Job | Good | Tea Donut | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-049 | Cafe Job | Good | Chocolate Cheesecake | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-050 | Cafe Job | Good | Milk Bread | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-051 | Cafe Job | Good | Bento Box | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-052 | Cafe Job | Good | Strawberry Milkshake | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-053 | Cafe Job | Good | Oven Cheese | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-054 | Cafe Job | Good | Sweet Panini | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-055 | Cafe Job | Good | Cheese Bun | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-056 | Cafe Job | Good | Tea Cake | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-057 | Cafe Job | Good | Double Espresso | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-058 | Cafe Job | Good | Choco Berry Donut | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-059 | Cafe Job | Good | Cheesecake | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-060 | Cafe Job | Good | Cake Donut | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-061 | Cafe Job | Good | Savory Bagel | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-062 | Cafe Job | Good | Fusion Tea | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-063 | Cafe Job | Good | Canned Coffee | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-064 | Cafe Job | Good | Cronut | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-065 | Cafe Job | Good | Jelly Filled Donut | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-066 | Cafe Job | Good | Mocha | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-067 | Cafe Job | Good | Victoria Sponge Cake | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-068 | Cafe Job | Good | Dirty Chai Latte | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-069 | Cafe Job | Good | Strawberry Latte | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-070 | Cafe Job | Good | Choco Chai Latte | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-G-071 | Cafe Job | Good | To Go Box | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-001 | Cafe Job | Bad | Paper Cup | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-002 | Cafe Job | Bad | Terrible Bagel | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-003 | Cafe Job | Bad | Ew Panini | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-004 | Cafe Job | Bad | Is It Cake | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-005 | Cafe Job | Bad | Spilled Coffee | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-006 | Cafe Job | Bad | Mug Boy | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-007 | Cafe Job | Bad | Bad Milkshake | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-008 | Cafe Job | Bad | Specialty Espresso | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-009 | Cafe Job | Bad | Flavored Coffee | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-010 | Cafe Job | Bad | Flat Croissant | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-011 | Cafe Job | Bad | Terrible Spread | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-012 | Cafe Job | Bad | Cup Tower | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-013 | Cafe Job | Bad | Disaster Dish | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-014 | Cafe Job | Bad | Don't Donut | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-015 | Cafe Job | Bad | Painting | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-016 | Cafe Job | Bad | Painted Mug | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-017 | Cafe Job | Bad | Awful Tea | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-018 | Cafe Job | Bad | Hot Air | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-019 | Cafe Job | Bad | Paper Plane | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-020 | Cafe Job | Bad | Menu | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-021 | Cafe Job | Bad | Dollar | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-022 | Cafe Job | Bad | Healthy Cake | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-023 | Cafe Job | Bad | Food Drawing | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-024 | Cafe Job | Bad | Thermos | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-025 | Cafe Job | Bad | Breadception | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-026 | Cafe Job | Bad | Paper Cup Phone | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-027 | Cafe Job | Bad | Healthy Donut | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-028 | Cafe Job | Bad | Tea Strainer | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-029 | Cafe Job | Bad | Cups Game | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-030 | Cafe Job | Bad | Chocolate Coins | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-031 | Cafe Job | Bad | Mended Mug | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-032 | Cafe Job | Bad | Poison | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-033 | Cafe Job | Bad | Strawberry Horror | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-034 | Cafe Job | Bad | Counterfeit Money | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-035 | Cafe Job | Bad | Heart Attack | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-036 | Cafe Job | Bad | Drawing | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-037 | Cafe Job | Bad | Edible Money | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-038 | Cafe Job | Bad | Paper Trash | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-039 | Cafe Job | Bad | Security Card | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-040 | Cafe Job | Bad | Burnt Panini | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| CA-B-041 | Cafe Job | Bad | Void Bagel | SRC-020 | SRC-020 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-001 | Bistro | Good | Yeast | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-002 | Bistro | Good | Flat Bread | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-003 | Bistro | Good | Salami | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-004 | Bistro | Good | Mochi | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-005 | Bistro | Good | Tomato Cheese Appetizer | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-006 | Bistro | Good | Mulled Wine | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-007 | Bistro | Good | Dough | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-008 | Bistro | Good | Blue Cheese | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-009 | Bistro | Good | Mushroom Pie | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-010 | Bistro | Good | Salami Rose | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-011 | Bistro | Good | Fresh Bread | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-012 | Bistro | Good | Sausage Roll | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-013 | Bistro | Good | Baked Apple | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-014 | Bistro | Good | Beer | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-015 | Bistro | Good | Khachapuri | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-016 | Bistro | Good | Stuffed Tomato | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-017 | Bistro | Good | Red Wine | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-018 | Bistro | Good | Tomato Mozzarella Sandwich | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-019 | Bistro | Good | Bread Soup | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-020 | Bistro | Good | Apple Pie | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-021 | Bistro | Good | Beef Wellington | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-022 | Bistro | Good | Garlic Powder | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-023 | Bistro | Good | Meat Sandwich | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-024 | Bistro | Good | Apple Cider | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-025 | Bistro | Good | Garlic Bread | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-026 | Bistro | Good | Kombucha | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-027 | Bistro | Good | Goulash | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-028 | Bistro | Good | Pumpkin Seeds | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-029 | Bistro | Good | Mushroom Soup | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-030 | Bistro | Good | Apple Mochi | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-031 | Bistro | Good | Risotto | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-032 | Bistro | Good | Croque Monster | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-033 | Bistro | Good | Pumpkin Soup | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-034 | Bistro | Good | Tomato Juice | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-035 | Bistro | Good | White Wine | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-036 | Bistro | Good | Pumpkin Bread | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-037 | Bistro | Good | Hamburger | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-038 | Bistro | Good | Apple Sauce | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-039 | Bistro | Good | Olive Oil | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-040 | Bistro | Good | Rosé | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-041 | Bistro | Good | Pizza Dough | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050; SRC-058 | SRC-015; SRC-018; SRC-058 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-042 | Bistro | Good | Vegan Sandwich | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-043 | Bistro | Good | Pumpkin Fries | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-044 | Bistro | Good | Meatloaf | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-045 | Bistro | Good | Pizza | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-046 | Bistro | Good | Tomato Cocktail | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-047 | Bistro | Good | Italian Rice Balls | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-048 | Bistro | Good | Schnitzel | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-049 | Bistro | Good | Meat Lover Pizza | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-050 | Bistro | Good | Pumpkin Pie | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-051 | Bistro | Good | Fried Apple Rings | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-052 | Bistro | Good | Bread Sticks | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-053 | Bistro | Good | Fungi Pizza | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-054 | Bistro | Good | Beef Katsu Sando | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-055 | Bistro | Good | Meatballs | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-056 | Bistro | Good | Fried Mushroom | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-057 | Bistro | Good | Charcuterie Board | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-058 | Bistro | Good | Pepperoni Pizza | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-059 | Bistro | Good | Steak | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-060 | Bistro | Good | Stick Bread | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-061 | Bistro | Good | Meatball Sandwich | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-062 | Bistro | Good | Pizza Speciale | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-063 | Bistro | Good | Focaccia | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-064 | Bistro | Good | Cheeseburger | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-065 | Bistro | Good | Aioli | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-066 | Bistro | Good | Fried Rice | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-067 | Bistro | Good | Pizza Rolls | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-068 | Bistro | Good | Stuffed Olives | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-069 | Bistro | Good | Wine Barrel | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-070 | Bistro | Good | Mozzarella Sticks | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-071 | Bistro | Good | Fried Olives | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-072 | Bistro | Good | Rice Paper | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-073 | Bistro | Good | Sake | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-074 | Bistro | Good | Tomato Rice | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-075 | Bistro | Good | Roasted Veggies | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-076 | Bistro | Good | Cheesy Bread | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-077 | Bistro | Good | Boiled Rice | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-078 | Bistro | Good | Roasted Mushrooms | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-079 | Bistro | Good | Shredded Cheese | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-080 | Bistro | Good | Meat Skewers | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-081 | Bistro | Good | Leftover Pizza | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-082 | Bistro | Good | Minced Garlic | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-G-083 | Bistro | Good | Mini Pizzas | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-B-040 | Bistro | Bad | Crazy Calzone | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050; SRC-024 | SRC-050 | COUNTER_ALIGNED_CANDIDATE_NOT_VERIFIED |
| BI-B-001 | Bistro | Bad | Endless Possibilities | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-B-002 | Bistro | Bad | Fungus | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-B-003 | Bistro | Bad | Pink Pencil | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-B-004 | Bistro | Bad | Yeast Monster | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-B-005 | Bistro | Bad | Cookbook | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-B-006 | Bistro | Bad | Ghost | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-B-007 | Bistro | Bad | Wine Glass | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-B-008 | Bistro | Bad | Toothpick | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-B-009 | Bistro | Bad | Corkscrew | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-B-010 | Bistro | Bad | Table Cloth | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-B-011 | Bistro | Bad | Scissors | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-B-012 | Bistro | Bad | Red 40 | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-B-013 | Bistro | Bad | Compass | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-B-014 | Bistro | Bad | Bad Pastry | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-B-015 | Bistro | Bad | Cheese Cloth | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-B-016 | Bistro | Bad | Sketchbook | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-B-017 | Bistro | Bad | Bad Meatloaf | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-B-018 | Bistro | Bad | Pumpkin Friend | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-B-019 | Bistro | Bad | Food Sketch | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-B-020 | Bistro | Bad | Cheese Grater | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-B-021 | Bistro | Bad | Jack O Lantern | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-B-022 | Bistro | Bad | Origami | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-B-023 | Bistro | Bad | Barely Edible | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-B-024 | Bistro | Bad | Paper Snowflake | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-B-025 | Bistro | Bad | Fried Balls | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-B-026 | Bistro | Bad | Drum Sticks | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-B-027 | Bistro | Bad | Definitely Not Wine | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-B-028 | Bistro | Bad | Paper Towel | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-B-029 | Bistro | Bad | Instant Calories | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-B-030 | Bistro | Bad | Pencil Sharpener | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-B-031 | Bistro | Bad | Oil Paint | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-B-032 | Bistro | Bad | Big Magnet | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-B-033 | Bistro | Bad | Boo Tomato | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-B-034 | Bistro | Bad | Clutter | SRC-015; SRC-016; SRC-018; SRC-024; SRC-038; SRC-050 | UNMAPPED | TRIGGER_HINT_ONLY |
| BI-B-035 | Bistro | Bad | Breadless Burger | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-B-036 | Bistro | Bad | Vampire Defense Kit | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-B-037 | Bistro | Bad | Bread and Wine | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-B-038 | Bistro | Bad | Sorrow Sandwich | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| BI-B-039 | Bistro | Bad | Risky Rice Pudding | SRC-015; SRC-016; SRC-018; SRC-038; SRC-050 | SRC-050 | SOURCE_LISTED_NOT_VERIFIED |
| RL-G-001 | Rat Level | Good | Low/OFF #1: Cheese | SRC-017; SRC-050; SRC-052 | SRC-017; SRC-050; SRC-052 | SOURCE_LISTED_NOT_VERIFIED |
| RL-G-002 | Rat Level | Good | Low/OFF #2: Cheese + Cheese | SRC-017; SRC-050; SRC-052 | SRC-017; SRC-050; SRC-052 | SOURCE_LISTED_NOT_VERIFIED |
| RL-G-003 | Rat Level | Good | Low/OFF #3: Cheese + Paper | SRC-017; SRC-050; SRC-052 | SRC-017; SRC-050; SRC-052 | SOURCE_LISTED_NOT_VERIFIED |
| RL-G-004 | Rat Level | Good | Low/OFF #4: Cheese + Pencil | SRC-017; SRC-050; SRC-052 | SRC-017; SRC-050; SRC-052 | SOURCE_LISTED_NOT_VERIFIED |
| RL-G-005 | Rat Level | Good | Low/OFF #5: Cheese + Eggshell OR Leaf (conflict) | SRC-017; SRC-050; SRC-052 | SRC-017; SRC-050; SRC-052 | CONFLICTED |
| RL-G-006 | Rat Level | Good | High/ON #1: Cheese | SRC-017; SRC-050; SRC-052 | SRC-017; SRC-050; SRC-052 | SOURCE_LISTED_NOT_VERIFIED |
| RL-G-007 | Rat Level | Good | High/ON #2: Cheese + Cheese | SRC-017; SRC-050; SRC-052 | SRC-017; SRC-050; SRC-052 | SOURCE_LISTED_NOT_VERIFIED |
| RL-G-008 | Rat Level | Good | High/ON #3: Cheese + Paper | SRC-017; SRC-050; SRC-052 | SRC-017; SRC-050; SRC-052 | SOURCE_LISTED_NOT_VERIFIED |
| RL-G-009 | Rat Level | Good | High/ON #4: Cheese + Pencil | SRC-017; SRC-050; SRC-052 | SRC-017; SRC-050; SRC-052 | SOURCE_LISTED_NOT_VERIFIED |
| RL-B-001 | Rat Level | Bad | Empty cooker (low/off or high/on; test both) | SRC-017; SRC-050; SRC-052 | SRC-017; SRC-050; SRC-052 | SOURCE_LISTED_NOT_VERIFIED |
| RL-B-002 | Rat Level | Bad | Leaf | SRC-017; SRC-050; SRC-052 | SRC-017; SRC-050; SRC-052 | SOURCE_LISTED_NOT_VERIFIED |
| RL-B-003 | Rat Level | Bad | Paperclip + Paper | SRC-017; SRC-050; SRC-052 | SRC-017; SRC-050; SRC-052 | SOURCE_LISTED_NOT_VERIFIED |
| RL-B-004 | Rat Level | Bad | Egg + Pencil OR Eggshell + Pencil (conflict) | SRC-017; SRC-050; SRC-052 | SRC-017; SRC-050; SRC-052 | CONFLICTED |
| RL-B-005 | Rat Level | Bad | Leaf + Pencil | SRC-017; SRC-050; SRC-052 | SRC-017; SRC-050; SRC-052 | SOURCE_LISTED_NOT_VERIFIED |
| RL-B-006 | Rat Level | Bad | Paperclip + Pasta | SRC-017; SRC-050; SRC-052 | SRC-017; SRC-050; SRC-052 | CONFLICTED |
| RL-B-007 | Rat Level | Bad | Eggshell + Paper | SRC-017; SRC-050; SRC-052 | SRC-017; SRC-050; SRC-052 | CONFLICTED |
| RL-B-008 | Rat Level | Bad | Paperclip | SRC-017; SRC-050; SRC-052 | SRC-017; SRC-050; SRC-052 | SOURCE_LISTED_NOT_VERIFIED |
| RL-B-009 | Rat Level | Bad | Paper | SRC-017; SRC-050; SRC-052 | SRC-017; SRC-050; SRC-052 | SOURCE_LISTED_NOT_VERIFIED |
| RL-B-010 | Rat Level | Bad | Eggshell | SRC-017; SRC-050; SRC-052 | SRC-017; SRC-050; SRC-052 | SOURCE_LISTED_NOT_VERIFIED |
| RL-B-011 | Rat Level | Bad | Pencil | SRC-017; SRC-050; SRC-052 | SRC-017; SRC-050; SRC-052 | SOURCE_LISTED_NOT_VERIFIED |
| RL-B-012 | Rat Level | Bad | Pencil + Paper | SRC-017; SRC-050; SRC-052 | SRC-017; SRC-050; SRC-052 | SOURCE_LISTED_NOT_VERIFIED |

## Bistro source mapping pass — SRC-050

A targeted comparison against the readable Bistro recipe list in Steam Guide SRC-050 has now populated formula-source IDs for exact name matches. **121 Bistro candidate rows** are marked `SOURCE_LISTED_NOT_VERIFIED`: this means SRC-050 explicitly lists a formula/action for that named entry; it does not mean the formula was independently corroborated or reproduced in-game. The source guide places some entries under Good and others under Bad, so classification is audited separately. Candidate rows not found in the corresponding source section remain UNMAPPED. Known opposite-section matches are flagged CLASSIFICATION_CONFLICT rather than silently accepted.

Important source boundary: SRC-050 is a community guide, its author warns some formulas may be wrong, and its body was last updated in August 2026. The official v1.1 fixes and later player corrections remain relevant. Use RECIPE_CONFLICTS.md for conflicts and QA_TEST_PLAN.md for test designs.

## Student Dorm / Cafe source mapping pass — SRC-019 / SRC-020

A row-level name/formula pass was completed against the directly opened Pixel Questing chapter guides. **Student Dorm and Cafe candidate rows are now mapped to SRC-019 / SRC-020 wherever the guide explicitly lists a formula or interaction.** These statuses mean the source lists the candidate; they do not mean this project has reproduced the result in-game. The Cafe guide lists Coffee Cake twice in its Good Recipes numbering; the duplicate is treated as one unique candidate, not two recipes. Version, item-state, appliance, and cross-source conflicts remain separate validation work.

## Rat Level source mapping pass — SRC-017 / SRC-050 / SRC-052

All 21 Rat Level slots now have source references for their listed input combinations. Four rows are explicitly marked CONFLICTED because the sources disagree over Eggshell vs Leaf, Egg vs Eggshell, Paperclip + Pasta vs Pasta alone, or Eggshell + Paper vs Pasta + Paper. These are not resolved by choosing a majority without a live counter test.

## Completion criteria for this audit

For each row, replace UNMAPPED only after recording:
1. Exact source ID(s) and direct evidence location (page/line/comment/image timestamp) supporting the formula or trigger.
2. Game version/date and item states, including processed vs unprocessed variants and appliance conditions.
3. Independent corroboration or an explicit conflict record.
4. Verification status: community_candidate, conflicted, verified_in_game, or not_reproducible.

The 333 rows are candidate names, not an official in-game total. The source family is a provenance starting point, not proof that the row is correct. This audit does not close the recipe-traceability P1 and does not authorize implementation.


## 1.0 Bistro counter alignment (SRC-024)

SRC-024's 2026-09-10 screenshot shows 76/83 Good and 37/40 Bad. The candidate inventory previously had 84 Good / 39 Bad. SRC-050 explicitly lists Crazy Calzone under Bad Recipes, so the audit reclassifies candidate BI-B-040 as Bad, yielding 83 Good / 40 Bad. This is counter-aligned and source-supported, but not yet direct card-tab verification; status remains COUNTER_ALIGNED_CANDIDATE_NOT_VERIFIED. No recipe formula is newly marked verified.
