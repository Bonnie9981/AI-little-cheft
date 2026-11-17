# Item & State Inventory

Updated: 2026-11-16  
Purpose: normalize all known objects and processed states before creating machine-readable recipe records. English keys are stable research identifiers; zh-TW labels come from docs/ZH_TW_GLOSSARY.md.

## Item categories

- Ingredient: can be used as a cooking input.
- ProcessedIngredient: output of a tool or appliance.
- Tool: performs cutting, mixing, sorting, or puzzle interactions.
- Container: holds or transforms items.
- Appliance: accepts inputs and executes recipes.
- Clue: reveals a hint, number, or task.
- PuzzleInteractable: switch, lock, phone, safe, order slip, or other stateful object.
- Environment: sink, plant, shelf, cabinet, wall, rope, or room feature.
- Character: mouse / rat that issues requests and trades items.
- Decoration: object used for customization or achievement but not normally a recipe input.

## Student Dorm

| Key | Category | zh-TW | Known states / notes | Capabilities |
|---|---|---|---|---|
| banana | Ingredient | 香蕉 | whole; airborne; cut | drag, toss, cut, cook |
| pasta | Ingredient | 義大利麵 | raw; cooked | drag, toss, cook |
| strawberry_jam | Ingredient | 草莓果醬 | jar; portion | drag, combine, cook |
| coffee_maker | Appliance | 咖啡機 | hidden; revealed; placed on stove; brewed | reveal, place, activate |
| peanut_butter | Ingredient | 花生醬 | hidden until main-menu letter button; unlocked flag persists | drag, combine, cook |
| canned_beans | Ingredient | 罐裝豆子 | sealed; opened/available | drag, combine, cook |
| cassette_player | Appliance | 卡帶播放器 | closed; open; playing | click, open, play |
| cassette_red | Clue/Item | 紅色卡帶 | inserted; playing | drag, insert, play |
| cassette_green | Clue/Item | 綠色卡帶 | inserted; playing | drag, insert, play |
| cassette_pink | Clue/Item | 粉紅卡帶 | hidden in player; inserted; playing | reveal, drag, insert, play |
| pbj_jar | ProcessedIngredient | PB&J 罐 | appears after making PB&J | drag, combine |
| toaster | Appliance | 烤麵包機 | idle; bread inserted; toast; burnt toast | insert, toggle, eject |
| milk | Ingredient | 牛奶 | cold; hot (if state exists) | drag, combine, cook |
| bread | Ingredient | 麵包 | raw; wet; toasted; burnt; soggy | drag, wet, toast, cook |
| potato | Ingredient | 馬鈴薯 | whole; removed from net sack | drag, cut, cook |
| egg | Ingredient | 雞蛋 | whole; cracked; eggshell | drag, crack, cook |
| protein_powder | Ingredient | 蛋白粉 | tub; portion | drag, combine |
| pink_glass_jar | Ingredient/Container | 粉紅玻璃罐 | sealed; open; used in Bad Recipes | drag, combine |
| ramen | Ingredient | 拉麵 | dry; cooked | drag, combine, cook |
| canned_tomato | Ingredient | 番茄罐頭 | sealed; open; contents | drag, combine, cook |
| cheese | Ingredient | 起司 | wheel; portion | drag, combine, cook |
| chef_knife | Tool | 廚師刀 | on rack; picked up | drag, cut |
| bread_knife | Tool | 麵包刀 | on rack; picked up | drag, cut |
| butter_knife | Tool | 牛油刀 | on rack; picked up | drag, cut |
| sponge | Tool | 海綿 | dry; wet; soggy | drag, wet, clean, water |
| orange_glass_jar | Ingredient/Container | 橘色玻璃罐 | sealed; open; used in Bad Recipes | drag, combine |
| green_glass_jar | Ingredient/Container | 綠色玻璃罐 | sealed; open; used in Bad Recipes | drag, combine |
| basil_plant | Environment/Ingredient | 羅勒盆栽 | wilted; watered; harvestable leaf | water, harvest |
| basil_leaf | Ingredient | 羅勒葉 | harvested; pesto input | drag, combine, cook |
| cooking_pot | Appliance/Container | 鍋子 | empty; loaded; cooking; cleared | accept 1–3 inputs, activate |
| sink_tap | Environment | 水槽水龍頭 | off; running; overflowing | toggle, flood |
| dirty_dishes | Environment | 髒碗盤 | dirty; clean | clean |
| utensils | Tool/Environment | 餐具 | scattered; arranged | drag, place |
| wall_tile_key | PuzzleInteractable | 磁磚鑰匙 | hidden at D2; revealed | click, drag |
| shane_locker | PuzzleInteractable | Shane 的置物櫃 | locked; unlocked | unlock |
| main_menu_letter | Clue | 主選單信件 | unread; button pressed | click, reveal |
| locker_set | PuzzleInteractable | 其他三個置物櫃 | closed; opened | click, reveal |

## Cafe Job

| Key | Category | zh-TW | Known states / notes | Capabilities |
|---|---|---|---|---|
| microwave_oven | Appliance | 微波爐 | idle; loaded; active; burnt | accept 1–3 inputs, activate |
| espresso_machine | Appliance | 義式咖啡機 | idle; loaded; brewing | insert cup, brew |
| coffee_beans | Ingredient | 咖啡豆 | raw; replenished after extraction | drag, combine, brew |
| espresso_shot | ProcessedIngredient | 濃縮咖啡 | extracted; cup served | combine |
| filled_coffee_cup | Container/ProcessedIngredient | 裝滿咖啡的杯子 | empty; filled; left in machine | fill, combine, re-extract |
| cup_of_espresso | Container/ProcessedIngredient | 濃縮咖啡杯 | filled; used for Canned Coffee | combine |
| dough | Ingredient | 麵糰 | raw; panini bread / baked state | drag, cook |
| plain_cake | Ingredient | 原味蛋糕 | plain; combined | drag, combine |
| chocolate_spread | Ingredient | 巧克力抹醬 | tub; portion | drag, combine |
| kakao | Ingredient | 可可粉 | tub; portion | drag, combine |
| lettuce | Ingredient | 生菜 | whole; cooked / grilled | drag, cook |
| avocado | Ingredient | 酪梨 | whole; processed | drag, combine, cook |
| paper | Ingredient/Clue | 紙張 | flat; torn; folded | drag, combine, fold |
| paper_cup | Container/ProcessedIngredient | 紙杯 | formed from Paper + Cup | combine, fill |
| small_white_cup | Container | 小白杯 | empty; under espresso spout; filled | place, fill |
| green_mug | Container | 綠色馬克杯 | empty; combined | drag, combine |
| white_mouse_mug | Container | 白色老鼠馬克杯 | empty; combined | drag, combine |
| strawberry | Ingredient | 草莓 | whole; jam / tea input | drag, combine, cook |
| jam | ProcessedIngredient | 果醬 | strawberry processed | combine |
| croissant | Ingredient | 可頌 | plain; heated | drag, combine, cook |
| bagel | Ingredient | 貝果 | plain; cooked | drag, combine, cook |
| panini | Ingredient/ProcessedIngredient | 帕尼尼 | dough; cooked; burnt | drag, combine, cook |
| chalk_red | Tool/Clue | 紅色粉筆 | unused; used | draw, combine |
| chalk_green | Tool/Clue | 綠色粉筆 | unused; used | draw, combine |
| chalk_pink | Tool/Clue | 粉紅粉筆 | unused; used | draw, combine |
| tea_leaves | Ingredient | 茶葉 | loose; brewed | drag, combine |
| strawberry_tea | ProcessedIngredient | 草莓茶 | brewed | combine |
| blue_teapot | Container/Character trigger | 藍色茶壺 | mouse hidden; mouse revealed | offer Cheese |
| mouse_rat | Character | 老鼠 | hidden; requesting; trading | request, reward |
| order_slip | PuzzleInteractable | 訂單紙條 | new; completed; removed | click, reveal |
| tip_coin | Currency | 小費硬幣 | available; collected; spent | drag, spend |
| tip_jar | Container | 小費罐 | 0..20 coins | store, unlock |
| telephone | PuzzleInteractable | 電話 | idle; number entered; ringing; call active; completed | dial, lift handset |
| torn_note | Clue | 撕下的紙條 | hidden; placed by phone | reveal, place |
| photo_frame | PuzzleInteractable | 相框 | photo mounted; photo dropped | click, reveal |
| photo | Clue/Ingredient | 照片 | found; used in Security Card | drag, combine |
| security_card | ProcessedIngredient/Key | 門禁卡 | created from Photo + Coin | drag, unlock |
| safe | PuzzleInteractable/Container | 保險箱 | locked; unlocked; opened | unlock, reveal |
| metal_lid | Tool/Ingredient | 金屬蓋 | loose; combined | drag, combine |
| fire_alarm | PuzzleInteractable | 火警警報器 | intact glass; broken; button revealed | click, break, press |
| piggy_bank | Container | 存錢筒 | 0..20 coins; completed; post-it | store, unlock |
| paintbrush | Tool | 畫筆 | locked; unlocked | customize |
| wall_poster | Decoration | 海報框 | frame variants | customize |
| wallpaper | Decoration | 壁紙 | selected variant | customize |
| wood_type | Decoration | 木紋樣式 | selected variant | customize |

## Bistro

| Key | Category | zh-TW | Known states / notes | Capabilities |
|---|---|---|---|---|
| flour | Ingredient | 麵粉 | raw | drag, combine, cook |
| rice | Ingredient | 米 | raw; ground | drag, process, cook |
| bread_dough | Ingredient/ProcessedIngredient | 麵包麵糰 | formed | drag, combine, cook |
| meat | Ingredient | 肉 | raw; ground (some guides label the same state Ground Beef) | drag, process, cook |
| salami | Ingredient | 義式臘腸 | raw/processed | drag, combine |
| tomato | Ingredient | 番茄 | whole; ground | drag, process, cook |
| pumpkin | Ingredient | 南瓜 | whole; ground | drag, process, cook |
| garlic | Ingredient | 大蒜 | whole; minced / powdered | drag, process, cook |
| mushroom | Ingredient | 蘑菇 | whole | drag, combine, cook |
| apple | Ingredient | 蘋果 | whole; ground | drag, process, cook |
| olives | Ingredient | 橄欖 | whole; oil / stuffed | drag, process, cook |
| wine | Ingredient | 葡萄酒 | bottle; label revealed; colored variants | drag, sort, combine |
| yeast | Ingredient | 酵母 | jar; used | drag, combine |
| cheese | Ingredient | 起司 | wheel; shredded | drag, process, cook |
| mixer | Appliance | 調理機 | off; powered; processing; overloaded | accept ingredient, process |
| cooking_pot_bistro | Appliance | 小館鍋子 | empty; loaded; cooking | accept 1–3 inputs, activate |
| scissors | Tool | 剪刀 | hidden; unlocked | cut, reveal |
| wooden_spoon | Tool | 木匙 | available | stir, combine, tool input |
| pencil_red | Tool | 紅色鉛筆 | available | color wine, combine |
| pencil_white | Tool | 白色鉛筆 | available | color wine, combine |
| pencil_pink | Tool | 粉紅鉛筆 | available | color wine, combine |
| newspaper | Clue/Ingredient | 報紙 | flat; combined | drag, combine |
| cloth | Tool/Ingredient | 抹布 | dry; used to clean Mixer mess | drag, clean, combine |
| magnet | Tool/Reward | 磁鐵 | received from mouse; used in compass | drag, combine |
| extractor_hood_door | PuzzleInteractable | 抽油煙機暗門 | hidden; opened | click, reveal |
| planter_fuse_box | PuzzleInteractable | 花盆電路盒 | hidden; repaired | click, repair |
| mixer_switch | PuzzleInteractable | 調理機開關 | hidden under leaves; revealed; on | reveal, toggle |
| hanging_rope | Environment | 懸掛繩索 | intact; cut | cut |
| wine_bottle_set | PuzzleInteractable | 五瓶酒 | labels; sorted by label height | drag, sort |
| mouse_rat_bistro | Character | 小館老鼠 | hidden; requesting; trading; heart note | request, reward |

## Rat Level

| Key | Category | zh-TW | Known states / notes | Capabilities |
|---|---|---|---|---|
| cheese | Ingredient | 起司 | raw | drag, combine, cook |
| paper | Ingredient | 紙張 | flat | drag, combine, cook |
| pencil | Tool/Ingredient | 鉛筆 | available | drag, combine, cook |
| leaf | Ingredient | 葉子 | available | drag, combine, cook |
| egg | Ingredient | 雞蛋 | whole; cracked; eggshell | click, crack |
| eggshell | Ingredient | 蛋殼 | created by clicking Egg multiple times | drag, combine, cook |
| pasta | Ingredient | 通心粉 | from necklace | drag, combine, cook |
| paperclip | Tool/Ingredient | 迴紋針 | available | drag, combine, cook |
| coin | Currency/Ingredient | 硬幣 | tossable; red-marked zone | drag, toss |
| portrait | PuzzleInteractable | 肖像畫 | clicked; anti-gravity switch revealed | click, reveal |
| anti_gravity_switch | PuzzleInteractable | 反重力開關 | off; on | toggle |
| planter_note | Clue | 花盆便條 | hidden; revealed; read | click, read |
| wine_bottle_label | PuzzleInteractable | 酒瓶標籤 | attached; lifted; keypad revealed | click, reveal |
| number_keypad | PuzzleInteractable | 數字鍵盤 | locked; code entered; unlocked | input, unlock |
| electric_can_cooker | Appliance | 通電罐頭鍋 | power low/high; max 2 ingredients | accept 2 inputs, activate |
| blue_switch | PuzzleInteractable | 藍色開關 | reported by one player as off; pressed; not confirmed as Coioioin prerequisite | optional investigation only |
| red_coin_zone | PuzzleInteractable | 紅色投幣區 | reported by one player; not corroborated as required for Coioioin | optional investigation only |

## Required state separation

- Tomato vs Ground Tomato.
- Meat vs Ground Meat.
- Rice vs Ground Rice.
- Pumpkin vs Ground Pumpkin.
- Apple vs Ground Apple.
- Garlic vs Minced Garlic vs Garlic Powder.
- Cheese vs Shredded Cheese.
- Bread vs Toast vs Burnt Toast vs Soggy Toast.
- Egg vs Eggshell.
- Coffee Beans vs Espresso Shot vs Filled Coffee Cup vs Cup of Espresso.
- Paper vs Paper Cup vs Photo.
- Raw Dough vs Bread Dough vs Panini.
- Wine bottle base vs Red Wine vs White Wine vs Rosé vs label-revealed bottle.
- Rat cooker power low vs high.
- Locked vs unlocked puzzle state.

## Unresolved inventory questions

- Exact contents and unlock conditions of the three Student Dorm lockers besides Shane's.
- Whether every recipe input is consumed after cooking.
- Whether item positions persist in save files.
- Exact object count and capabilities for Bistro and Rat Level.
- Whether some processed outputs are both recipe results and reusable ingredients.


## Student Dorm To-Do state additions
- To-Do task 1: pasta_dish_counter = 0..8 (Pasta or Ramen appears as one ingredient).
- To-Do task 2: shane_cheese_borrowed; D2 key unlock is prerequisite; use Cheese in a Good recipe to complete.
- To-Do task 3: red_cassette_played, green_cassette_played, remix_created, remix_played.
- To-Do task 4: dishes_cleaned, utensils_arranged, coffee_maker_revealed, coffee_brewed.
- To-Do task 5: basil_watered.
- To-Do task 6: new_dish_counter = 0..40 across Good + Bad discoveries.
- The mouse hole is a separate tile to the right of D2; Cheese held at the hole triggers I Smell Cheese, not the Shane locker task.
