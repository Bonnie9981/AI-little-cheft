# Recipe Reconciliation Register

更新：2026-11-16  
範圍：Student Dorm、Cafe Job、Bistro、Rat Level  
用途：集中記錄不同攻略、版本公告、玩家回報之間的配方差異。這份表不是最終食譜表；未驗證項目不可直接進正式 recipe data。

## 證據等級

| 等級 | 定義 |
|---|---|
| A | 官方公告／開發者直接回覆明確支持 |
| B | 多份獨立社群攻略或玩家回報一致 |
| C | 單一社群攻略線索 |
| D | 推測、舊版資料、來源互相衝突 |

## Bistro 衝突清單

| Recipe | 候選配方／狀態 | 證據與問題 | 目前處理 |
|---|---|---|---|
| Goulash | **Normal Meat + Ground Tomato + Wine**（不是 Ground Meat） | SRC-055 Steam玩家討論中，最初有人誤寫 processed meat；另一玩家明確更正為 normal meat + processed tomato + wine，原提問者回覆感謝並採用。SRC-017 v1.0 guide及官方v1.1 cookbook修正提供旁證。 | B；鎖定 normal meat + Ground Tomato + Wine 為首選候選；仍需 1.0+ 實機回歸 |
| Tomato Cocktail | Ground Tomato + Olives + Red Wine / Wine | SRC-017作者留言指出Olives + Ground Tomato + Red Wine；SRC-050與7/14 guide寫Wine；官方v1.1公告修正 cookbook。 | B/D；測試紅酒與一般酒的item state |
| Focaccia | Bread Dough + Olive Oil + Olives | 7/14 Steam guide、Level 3 玩家討論及後續攻略一致。 | B；待實機 |
| Tomato Cheese Appetizer | Tomato + Cheese；或 Tomato + Cheese + Olives | 7/14 Steam guide列 Tomato + Cheese；8/10 更新版列 Tomato + Cheese + Olives。Olives 可能是多餘／必要輸入差異。 | D；不可定案 |
| Apple Mochi | Rice + Apple；或 Ground Rice + Apple | 8/10 guide 一處列 Rice + Apple；7/14 guide列 Ground Rice + Apple；8/28 玩家留言明確提醒 Mochi 要先 grind rice。 | B；暫採 Ground Rice + Apple，待實機 |
| Tomato Juice | Tomato；或 Ground Tomato | 舊版表格列 Tomato；8/28 玩家留言指出 Tomato Juice 需要 mixer-ground tomato；另一份 Bistro Guide正文也列 Ground Tomato。 | B；採 Ground Tomato 候選 |
| Meatballs | Ground Meat；或 Ground Meat + Garlic + Dough | GuideXon 列 Ground Beef；8/10 Steam guide 列 Ground Meat + Garlic + Dough。可能是版本／名稱／清單錯誤。 | D；拆成候選，不合併 |
| Hamburger | Bread + Tomato + Ground Meat / Ground Beef | 8/10 guide與多個攻略列 Ground Meat / Ground Beef；Ground Beef 可能是 Ground Meat 的詞彙變體，但需核實遊戲顯示名稱。 | C；保留 alias 可能性 |
| Beef Katsu Sando | Meat + Bread；或 Bread + Beef + Olive Oil | GuideXon 列 Meat + Bread；8/10 Steam guide列 Bread + Beef + Olive Oil。 | D；待實機 |
| Fried Rice | Rice + Olive Oil；或 Rice + Olive Oil + Mushroom | 7/14 guide列 Rice + Olive Oil；8/10 guide列 Olive Oil + Rice + Mushrooms。 | D；待實機 |
| Pizza Dough | Olive Oil + Yeast + Flour | 8/10 guide、9Puz、玩家攻略一致；不是 Dough + Flour，也不是 Pizza Dough 先做。 | B；待實機 |

## Cafe Job 狀態衝突

| Recipe | 候選配方／狀態 | 證據與問題 | 目前處理 |
|---|---|---|---|
| Tiramisu | Cake + Coffee + Milk（舊版）；Cake + Filled Coffee Cup + Milk（新版） | 8/10 guide明確提醒使用裝滿咖啡的杯子，不是 Coffee Beans；舊攻略版本較早。 | B；新版優先 |
| Double Espresso | Filled Espresso Cup 留在機器內 + 新一輪 Coffee Beans | 多份新版攻略一致；不能只用 Espresso + Beans 的文字簡寫。 | B；新版狀態模型 |
| Canned Coffee | Coin + Cup of Espresso | 8/10 guide列出；v4.1ea官方公告確認 Canned Coffee 可用 coin 製作。 | A/B；版本需保留 |
| Dirty Chai Latte | Tea + Milk + Coffee；部分舊資料寫 Coffee Beans | 8/10 guide留言明確更正為 Coffee，不是 Coffee Beans。 | B；待實機 |
| Mocha | Espresso Shot + Kakao + Milk；早期版本曾使用 Coffee Beans | v3.0ea/v4.1ea調整咖啡食譜，需以 release recipe book 為準。 | B；新版優先 |
| Paper Cup | Paper + Cup；部分留言誤稱 Photo | 更新版指南與多份來源列 Paper + Cup；Photograph 是 Security Card 的材料。 | B；Paper 與 Photo 分開 |

## Rat Level 狀態衝突

| Slot / Recipe | 候選輸入 | 問題 | 目前處理 |
|---|---|---|---|
| Cold good #5 | Cheese + Eggshell；部分完成路線提到 Leaf icon ambiguity | 8/10 guide明列 Eggshell；9Puz提醒早期參考圖示／文字可能有 Eggshell / Leaf 混淆。 | B/C；按 live slot 計數 |
| Bad result | Egg + Pencil | 更新版 Steam guide列 Egg + Pencil。 | C；保留 |
| Bad result | Eggshell + Paper | 更新版 Steam guide列 Eggshell + Paper；Eggshell 需點 Egg 使其破裂。 | C；保留 |
| Oven empty | Cold / Hot | 更新版 guide列空爐可在任一溫度觸發 Bad Recipe。 | C；分開測試兩種狀態 |

## 其他已確認的狀態建模原則

- Tomato、Ground Tomato、Ground Meat、Ground Pumpkin、Ground Apple、Ground Rice、Shredded Cheese、Minced Garlic 不可視為同一個 item。
- Coffee Beans、Espresso Shot、Filled Coffee Cup、Cup of Espresso 要分別建檔，並記錄產生設備與是否留在機器內。
- Bread、Toast、Burnt Toast、Soggy Toast 是不同物件狀態。
- Rat Level 的 oven_state = cold | hot 是配方條件，不是純視覺效果。
- 同一組輸入在不同設備（pot / oven / espresso machine）中可能有不同輸出；設備必須進 RecipeConditions。
- 版本更新會改變配方、修正 bug 或移除內容；每筆 recipe 必須保留 introduced_version、last_verified_version、evidence_ids、confidence、verification_status。

## 主要來源

- [Steam Bistro Guide (J_Moon, 2026-07-14)](https://steamcommunity.com/sharedfiles/filedetails/?id=3764982550)
- [Steam complete recipe guide (aladar, search index says updated 2026-08-10)](https://steamcommunity.com/sharedfiles/filedetails/?id=3713640352)
- [9Puz completion route (2026-09-02)](https://9puz.com/5427-little-chef-cozy-cooking-completion-guide/)
- [GuideXon recipe guide (2026-07-15)](https://guidexon.com/little-chef-cozy-cooking-recipes-guide/)
- [Official v1.1 changelog](https://store.steampowered.com/news/app/3376500/view/)

## 定案規則

1. 官方公告只證明公告明確寫出的內容；「修正 cookbook」不能推導精確配方。
2. 玩家攻略一致不等於已實機驗證；來源版本、語言、遊戲更新日期要一併記錄。
3. 配方輸入有疑義時，優先逐個測試狀態與設備，不要同時混入多個替代材料。
4. 只有通過遊戲內 cookbook counter / recipe card 的實際結果，才能標記 verified_in_game。


## Student Dorm 版本／配方衝突

| Recipe | 候選配方／狀態 | 證據與問題 | 目前處理 |
|---|---|---|---|
| Beans on Toast | Bread + Beans；或 Beans + Toast | 8/10 Steam guide簡寫 Bread + Beans；10/9 Pixel Questing明確要求 Toast 狀態。 | C；暫採 Beans + Toast，待實機 |
| French Toast | Bread + Egg + Milk；或 Toast；或 Bread + Milk + Egg | 不同攻略對 Bread/Toast 狀態表述不同。 | D；測試兩種狀態 |
| Savory Sandwich | Bread + Egg；或 Bread + Cheese + Tomato | 10/9攻略列兩種可行路徑，較早指南只列 Bread + Egg。 | C；記錄 alternate_inputs |
| Tomato Soup | Tomato；或 Tomato + Toast | 10/9攻略列 Tomato + Toast；8/10 guide列 Tomato。 | D；待實機 |
| Pasta A La Carbonara | Pasta + Egg + Cheese；或 Pasta + Egg + Milk | 8/10 guide列 Cheese；10/9 Pixel Questing列 Milk。 | D；待實機 |
| PB&J Sandwich | Peanut Butter + Jam + Bread；或 PB&J jar + Bread | 新攻略指出先製作 PB&J jar 會成為另一個中間物件。 | C；保留兩條候選 |
| Smoothie | Milk + Banana + Peanut；或 Strawberry Jam + Banana + Milk | 8/10 guide與10/9攻略的配方不同；可能存在不同版本／名稱混淆。 | D；待實機 |
| Tomato Egg Stir Fry | Can of Tomatoes + Egg；或 Tomato + Egg | 新版指南與更新版 Steam guide都支持番茄罐頭 + 蛋，物件命名需確認。 | B；保留 canned tomato state |
| Bad Protein Shake | Protein Powder；或 Protein Powder + Egg + Tomato | 不同指南有不同錯誤料理輸入。 | D；待實機 |
| Bad Ramen | Ramen + 2 unrelated items；或 Milk + Ramen + Cheese | 8/10 guide給泛用組合，10/9 guide提供具體組合。 | D；待實機 |

Student Dorm To-Do（Pixel Questing 2026-10-09）：
1. 8 道 pasta/ramen dishes。
2. 解鎖 Shane locker 並使用 Cheese 製作一道 good dish。
3. 播放 Red、Green、Remix 三卷磁帶。
4. 洗淨並整理餐具，取得 Coffee Maker，放上爐台製作 Coffee。
5. 用濕海綿澆灌 Basil。
6. 累積 40 道 Good + Bad dishes。
以上為單一攻略線索，待 1.0 實機驗證。


## Cafe Job 2026-11-09 guide conflicts

| Recipe | Candidate配方／狀態 | Evidence conflict | Current handling |
|---|---|---|---|
| Tiramisu | Cheese + Plain Cake + Coffee Beans；或 Cake + Filled Coffee Cup + Milk | 11/9 Pixel Questing 與 8/10 Steam guide、9/2 9Puz不一致；官方版本的咖啡狀態鏈較支持 filled cup。 | D；優先實測 1.0 cookbook |
| Babycino | Milk；或 Espresso Shot + Milk | 11/9 guide提供兩條路徑；8/10 guide只列 Milk。 | C/D；保留兩條候選 |
| Hot Cocoa | Espresso Shot + Milk + Kakao；或 Milk + Chocolate Spread | 11/9 guide與8/10 guide不同。 | D；測試設備與材料狀態 |
| Latte | Espresso Shot + Milk；或 Coffee Beans + Milk | 新舊指南對是否必須先萃取 Espresso有差異。 | D；測試設備與狀態 |
| Canned Coffee | Metal Lid + Coffee Beans；或 Coin + Cup of Espresso | 11/9 guide列 Lid + Beans；8/10 guide列 Coin + Cup of Espresso；v4.1ea官方公告確認 Coin 配方。 | A/B；Coin版本優先，仍測試替代 |
| Dirty Chai Latte | Espresso Shot + Tea Leaves + Milk；或 Coffee + Tea + Milk | 11/9 guide與8/10 guide不一致；8/10 guide作者留言更正為 Coffee而非 Coffee Beans。 | D；保留設備差異 |
| To Go Drink | Paper Cup + Kakao；或 Paper Cup + Drink（如 Milk） | 11/9 guide列 Kakao；8/10 guide列一般 Drink，舊攻略也用 Milk。 | D；測試可接受輸入 |
| Bento Box | Metal Lid + Avocado；或 Metal Lid + 任一 Food | 11/9 guide列 Avocado；8/10 guide列 Lid + Food Item。 | D；測試泛用類型條件 |
| Savory Croissant | Croissant + Avocado；或 Croissant + Cheese / Avocado | 11/9 guide只列 Avocado；8/10 guide列 Cheese 或 Avocado。 | C；保留 alternate_inputs |
| Strawberry Tiramisu | Strawberry Cake + Milk；或 Cake + Strawberry + Milk | 新舊攻略對中間物件是否必要表述不同。 | C；狀態候選 |
| Espresso Shot | Coffee Beans + Espresso Machine + Small White Cup | 無杯會變成 Spilled Coffee；咖啡機狀態與杯子位置必須作為條件。 | B；必須記設備條件 |

### Cafe To-Do evidence note

- Official v3.0ea adds one To-Do: complete 8 orders. Japanese player notes confirm illustrated order slips, tip coins, and that completing a dish checks the corresponding order.
- The full Cafe To-Do list and total row count remain unknown. Do not equate “8 orders” with “8 To-Do entries”; keep order_completion_target = 8 separate from todo_task_count = unknown.


## Rat Level 電力狀態模型修正

Rat Level 的設備不是普通烤箱，而是通電罐頭式 cooker（近似微波爐）。日文玩家 2026-09-10 攻略描述解開酒瓶機關後可調整電力輸出強／弱，同一組材料會因電力強弱產生不同料理。資料模型採 power_level = low | high；Steam guide的 OFF/ON 暫存為來源狀態，直到遊戲畫面確認兩者映射。來源：[日文 1.0 成就完成攻略](https://note.com/utsukinoel/n/n2734d08070ca)。


## Bistro 1.0 added recipes (2026-08-27 onward)

| Category | Recipe | Candidate input / action | Status |
|---|---|---|---|
| Good | Boiled Rice | Rice | Community guide lists it as new |
| Good | Roasted Mushrooms | Mushrooms | Community guide lists it as new |
| Good | Shredded Cheese | Cheese through Mixer, then cooking station | Official Aug 26 hotfix corrected a bug where it became Pizza |
| Good | Meat Skewers | Meat + Wooden Spoon | Community guide lists it as new |
| Good | Leftover Pizza | Slice of Pizza | Community guide lists it as new |
| Good | Minced Garlic | Garlic through Mixer, then cooking station | Community guide lists it as new |
| Good | Mini Pizzas | Pizza + Scissors | Community guide lists it as new; 1.0 player says this was final Good recipe |
| Bad | Big Magnet | Magnet received from rat reward, possibly cooked in the cooking station | 8/10 Steam guide shorthand says “Magnet from mouse rewards”; 9/2 9Puz 1.0 route explicitly says to cook one of the rat-reward Magnets. | C; test both direct Magnet and cooked Magnet; use recipe counter |
| Bad | Boo Tomato | Tomato | Community guide lists it as new |
| Bad | Clutter | Trigger unknown; description suggests spontaneous mess | 1.0 player reports this as final Bad recipe; do not assume Mixer until verified |

The 1.0 player walkthrough reports approximately 10 Bistro additions. The 8/10 Steam Guide lists 7 Good + 2 Bad; the 9/10 completion report adds Clutter as a final Bad entry. This is a coherent 7+3 candidate set, but the exact in-game counter should be checked before treating the count as final.

## Rat Level achievement interaction

Coioioin trigger conflict: Steam achievement text says the same face must land three times in a row; an older Steam discussion says repeatedly click the coin. The Japanese 1.0 first-hand walkthrough instead says press the blue-frame switch and toss the coin into the red-frame target, and reports delayed Steam sync until relaunch. Keep both routes as candidates; separate gameplay trigger from platform synchronization. Source: [Steam achievements](https://steamcommunity.com/stats/3376500/achievements), [9Puz 1.0 route](https://9puz.com/5427-little-chef-cozy-cooking-completion-guide/), [Steam guide](https://steamcommunity.com/sharedfiles/filedetails/?id=3713640352&l=swedish).


## Bistro count reconciliation

The directly opened 2026-07-14 Bistro Guide contains 76 Good entries (lines 91-166) and 31 Bad entries (lines 170-200): this is the Early Access baseline, not necessarily the 1.0 final total. The 2026-08-27 update list adds 7 Good + 2 Bad; the 2026-09-10 1.0 player completion report identifies Clutter as another final Bad entry. This 83/34 estimate is superseded by the July 17 comment discoveries below. Historical cross-source estimate was 84 Good / 39 Bad = 123. This split is superseded by SRC-024's 1.0 screenshot counter target of 83 Good / 40 Bad; Crazy Calzone is moved to Bad based on SRC-050's Bad section, with exact card-tab verification still pending.

Sources:
- [7/14 Bistro Guide](https://steamcommunity.com/sharedfiles/filedetails/?id=3764982550)
- [8/10 guide, updated with 8/27 additions](https://steamcommunity.com/sharedfiles/filedetails/?id=3713640352)
- [9/10 1.0 completion report](https://note.com/utsukinoel/n/n2734d08070ca)


## Bistro rat request and country-dish evidence

- Developer-confirmed interaction: offer Cheese to the rat behind the suspicious extractor-hood door; the rat then displays a dish drawing, and completing that dish trades for a new ingredient. Source: [Steam developer reply, 2026-07-16](https://steamcommunity.com/app/3376500/discussions/0/574921459914308481/).
- First player-recorded reward is Tomato. Later mouse rewards include Apple, Olive, and Garlic. The exact order of all rewards is not yet established.
- Going Global requires seven country dishes and seven magnets. Only Mochi (Japan) is explicitly identified in readable text. The other six dish-country pairs remain unknown and must not be inferred from recipe names alone.
- The final heart note is a thank-you after the request chain is complete, not a request to cook Meat Lover Pizza. Source: [Steam discussion](https://steamcommunity.com/app/3376500/discussions/0/582806564883159730/).


## Additional Bistro conflicts cross-checked against 7/14, cached 8/10, and 9/2 sources

**Correction (2026-11-17):** Steam Guide ID 3686619896 is in fact titled a v1.0 all-achievements guide, updated 2026-09-08. Its body retains a legacy “v4.0 ea” heading for older content but also contains Bistro and Rat Level sections (lines 403–553). The earlier claim that it had no Bistro/Rat Level content, and the blanket withdrawal of its 1.0 claims, are superseded. Its author warns that the first two rooms may be stale and manually entered formulas may be wrong; use its Bistro/Rat Level entries as C-level 1.0 candidates. See SRC-017 critical correction in SOURCE_REGISTER.

| Recipe | Candidate inputs / states | Conflict | Handling |
|---|---|---|---|
| Mochi | Rice; or Ground Rice | 7/14 and cached 8/10 guide list Rice; a comment on the 8/10 guide says to grind Rice first. | D; test whole vs ground Rice |
| Apple Mochi | Rice + Apple; or Ground Rice + Apple | 7/14 guide lists Ground Rice; cached 8/10 guide lists Rice. | D; test both |
| Kombucha | Mushroom + Yeast; or Yeast + another ingredient | 7/14 guide, cached 8/10 guide, and Steam player replies support Mushroom + Yeast; one separate Chinese-language community correction disputes Mushroom. | B/C; Mushroom + Yeast favored, verify |
| Tomato Juice | Tomato; or Ground Tomato | 7/14 guide and player comment support Ground Tomato; cached 8/10 guide says Tomato. | B; Ground Tomato candidate |
| Fried Rice | Rice + Olive Oil; or Rice + Olive Oil + Mushroom | 7/14 guide uses two inputs; cached 8/10 guide adds Mushroom. | D; test two- and three-input variants |
| Sake | Rice + Yeast; or Rice + Wine | Older and cached later sources are inconsistent. | D; test both |
| Meatballs | Ground Beef alone; or Ground Meat + Garlic + Dough | 7/14 guide lists Ground Beef; cached 8/10 guide and 9/2 9Puz route support the three-input candidate. | D; preserve variants |
| Beef Katsu Sando | Meat + Bread; or Bread + Beef + Olive Oil | 7/14 guide lists Meat + Bread; cached 8/10 guide adds Olive Oil. | D; test |
| Tomato Cheese Appetizer | Tomato + Cheese; or Tomato + Cheese + Olives | 7/14 guide omits Olives; cached 8/10 guide says Olives (mouse gift) are required. | D; test with and without Olives |
| Yeast Monster | Yeast + Wine; or Yeast + Tomato | 7/14 guide says Wine; cached 8/10 guide says Tomato. | D; test both |
| Cookbook | Newspaper + Apple; or Newspaper + Tomato | 7/14 guide says Apple; cached 8/10 guide says Tomato. | D; test both |
| Bad Meatloaf | Meat + Flour; or Meat + Olives | 7/14 guide and cached 8/10 guide differ. | D; test |
| Food Sketch | Apple + Any Pencil; or Cheese + Any Pencil | 7/14 guide says Apple; cached 8/10 guide says Cheese. | D; test |
| Fried Balls | Bread + Olive Oil; or Salami + Olive Oil | 7/14 guide says Bread; cached 8/10 guide says Salami. | D; test |
| Vampire Defense Kit | Garlic + Any Pencil; or Garlic + Wooden Spoon | 7/14 comment and cached 8/10 guide differ. | D; test both |
| Clutter | Cloth + Wooden Spoon (SRC-017 1.0 guide candidate); spontaneous/idle mess trigger remains alternate | SRC-017 lists Cloth + Wooden Spoon; 9/10 Japanese 1.0 player clue text suggests mess may happen spontaneously but does not provide a reproducible formula. | C/D; test both combination and idle/physics trigger |
| Rat cold Good #5 | Cheese + Eggshell; possible Cheese + Leaf icon ambiguity | Cached 8/10 guide lists Eggshell; 9/2 9Puz notes early references can confuse Eggshell and Leaf icon. | C/D; test Eggshell first, then Leaf if slot does not advance |
| Rat bad #4 | Egg + Pencil | Cached 8/10 guide lists this; the previously claimed Eggshell + Pencil alternative came from the misidentified v4.0 EA guide and is withdrawn. | C; single-source candidate |
| Rat bad #6/#7 | Paperclip + Pasta | Cached 8/10 guide lists this; previously attributed Pasta-only / Pasta + Paper alternatives are withdrawn. | C; single-source candidate |

Sources:
- [Steam Bistro Guide (2026-07-14)](https://steamcommunity.com/sharedfiles/filedetails/?id=3764982550)
- [Steam 100% recipe guide (search-indexed Aug 10 content; removed page/cache caveat)](https://steamcommunity.com/sharedfiles/filedetails/?id=3713640352)
- [9Puz 1.0 completion route (2026-09-02)](https://9puz.com/5427-little-chef-cozy-cooking-completion-guide/)
- [Steam Chinese-language correction discussion](https://steamcommunity.com/app/3376500/discussions/0/568165880361397181/)

## Puzzle rule evidence

- Wine About It: a Steam player reports the five bottles should be ordered by label height, shortest to tallest. This is more actionable than guessing by wine color or name. Source: [Steam Level 3 discussion](https://steamcommunity.com/app/3376500/discussions/0/568165880361398668/).
- Rat Level slot conflicts are version/source conflicts, not translation-only issues: Cold Good #5 is Cheese + Leaf in the 1.0 Chinese guide vs Cheese + Eggshell in the English guide; Bad #4 is Eggshell + Pencil vs Egg + Pencil; Bad #6/#7 include Pasta alone, Pasta + Paper, or Paperclip + Pasta.
- Coioioin is unresolved: official text and older guides support same-face repetition; a Japanese 1.0 first-hand route supports blue-switch → red-target toss and says it is not simply random repetition. Test both; the Japanese author also reports Steam achievement sync only after relaunch.


## Official Early Access recipe adjustments (v2.9ea, 2026-03-19)

- Official v2.9ea removed one of the two confusing Chocolate Spread items.
- Official v2.9ea explicitly allowed more Tiramisu options: Cake + Coffee + Dough, or Cake + Coffee + Milk. The exact wording indicates two valid combinations, not necessarily one fixed formula.
- Official v2.9ea also added Bread + Cheese + Tomato Sauce as another valid Savory Sandwich combination.
- These are authoritative Early Access version rules. The 1.0 candidate recipe must still be checked against later guides and the final cookbook state. Do not erase older version history.
- Official source: [SteamDB patch-note archive, v2.9ea / 2026-03-19](https://steamdb.nexus/game/3376500).


## Student Dorm / Cafe 1.0 formula conflicts from the 2026-10/11 walkthroughs

| Recipe | Candidate formulas | Evidence | Handling |
|---|---|---|---|
| Smoothie | Milk + Banana + Peanut Butter; or Strawberry Jam + Banana + Milk | Developer says Smoothie includes Peanut Butter; cached Steam guide lists Milk + Banana + Peanut; 10/9 Pixel Questing lists Strawberry Jam + Banana + Milk. | B/C; Peanut Butter favored, but version difference remains open |
| Sweet Sandwich | Bread + Peanut Butter; or Bread + Strawberry Jam | 8/10 cached Steam guide vs 10/9 Pixel Questing. | D; test both |
| Good Protein Shake | Protein Powder + Milk + Peanut Butter; alternate: Protein Powder + Milk + Banana | Developer explicitly gives Milk + Peanut Butter + Protein Powder as the correct formula (and rejects Egg). Pixel Questing 1.0 says Peanut Butter or Banana. | A for Peanut Butter formula; C for Banana alternate; test alternate separately |
| Savory Sandwich | Bread + Egg; Bread + Cheese + Tomato Sauce; or Bread + Cheese + Tomato | Official v2.9 adds Tomato Sauce variant; later guides differ on Sauce vs raw Tomato. | A/B; preserve separate input sets |
| Pasta A La Carbonara | Pasta + Egg + Cheese; or Pasta + Egg + Milk | 8/10 cached Steam guide vs 10/9 Pixel Questing. | D; test both |
| Beans on Toast | Bread + Beans; or Beans + Toast | 8/10 cached Steam guide vs 10/9 Pixel Questing. | D; test Bread vs Toast state |
| Tomato Soup | Tomato; or Tomato + Toast | 8/10 cached Steam guide vs 10/9 Pixel Questing. | D; test both |
| PB&J Sandwich | Bread + Peanut Butter + Strawberry Jam; alternate: PB&J Jar + Bread (also Toast as bread base) | 10/9 Pixel Questing explicitly lists Bread, Toast, or PB&J Jar + Bread as accepted paths; 8/10 guide lists the three raw inputs. These may be alternate valid paths, not a version conflict. | B/C; preserve alternate_inputs rather than treating as mutually exclusive |
| Tiramisu | Cake + Filled Coffee Cup + Milk; official v2.9 Cake + Coffee + Dough / Milk; or Cheese + Cake + Coffee Beans | Official v2.9 plus 8/10 guide support coffee state; 11/9 guide conflicts. | B; prioritize filled coffee cup candidate |
| Babyccino | Milk; or Espresso Shot + Milk | 8/10 cached Steam guide says Milk; 11/9 Pixel Questing lists Milk or Espresso + Milk. | B; Milk is minimum confirmed |
| Latte | Milk + Coffee Beans; or Espresso Shot + Milk | 8/10 cached Steam guide vs 11/9 guide. | D; test both |
| Hot Cocoa | Milk + Chocolate Spread; or Espresso Shot + Milk + Kakao | 8/10 cached Steam guide vs 11/9 guide. | D; test both |
| Avocado Milk | Avocado + Milk; or Mouse Mug + Milk + Avocado | 8/10 cached Steam guide vs 11/9 guide. | D; test both |
| Strawberry Cheesecake | Strawberry Cake + Cheese + Strawberry; or Strawberry Cake + Cheese | 8/10 cached Steam guide vs 11/9 guide. | D; test 2 vs 3 inputs |
| Chocolate Covered Strawberries | Strawberry + Chocolate Spread; or Strawberry + Kakao | 8/10 guide distinguishes Chocolate Spread; source may use Kakao as same item alias. | C; verify item identity |
| Chocolate Bomb | Chocolate Spread + Kakao; or Chocolate Syrup + Kakao | 8/10 cached Steam guide vs 11/9 guide. | D; check if Chocolate Syrup is a separate item |
| Canned Bread | Bread + Lid; or Dough + Metal Lid | 8/10 guide vs 11/9 guide. | D; test raw Bread vs Dough |
| Canned Coffee | Coin + Cup of Espresso; or Metal Lid + Coffee Beans | v4.1ea officially adds Coin option; 8/10 guide lists Coin + Cup of Espresso. | A/B; Coin option is confirmed |
| Dirty Chai Latte | Tea + Milk + Coffee; or Espresso Shot + Tea Leaves + Milk | 8/10 guide comment explicitly says Coffee, not Coffee Beans; 11/9 guide uses Espresso Shot. | D; test coffee state |
| Sweet Panini | Panini + Chocolate Spread; or Panini + Jam | 8/10 guide vs 11/9 guide. | D; test both |
| Cake Donut | Cake + Donut; or Cake + Dough | 8/10 guide vs 11/9 guide. | D; test both |
| To Go Box | Paper + any Food; or Paper + Avocado | 8/10 guide allows any food; 11/9 guide lists Avocado. | B; category predicate candidate |
| Paper Cup Phone | Paper Cup; or two Paper Cups | 8/10 guide says Paper Cup; 11/9 guide says two cups in microwave. | D; test both |
| Paper Plane | Paper; or Paper in Microwave | 8/10 guide says Paper; 11/9 guide adds microwave action. | D; test appliance |
| Dollar | Coin; or Coin + Paper | 8/10 guide says Coin; 11/9 guide adds Paper. | D; test both |
| Drawing | Chalk; or Red + Green/Pink Chalk | 8/10 guide says Chalk; 11/9 guide lists chalk colors. | D; test one vs multiple chalks |
| Counterfeit Money | Coin + Lid; or Lid alone | 8/10 guide says Coin + Lid; player comment says Lid alone worked. | D; test both |
| Specialty Espresso | Filled Espresso Cup + 2 weird items; or Cheese + Espresso Shot | 8/10 guide vs 11/9 guide. | D; test both |
| Flavored Coffee | Coffee Beans + any weird item; or Cheese + Coffee Beans | 8/10 guide vs 11/9 guide. | D; test both |
| Hot Air | Empty Microwave Oven; or empty Espresso Machine | 8/10 guide says run oven empty; 11/9 guide says Espresso Machine empty. | D; test both appliances |
| Terrible Spread | Chocolate Spread + weird item; or Cake + Kakao + Jam | 8/10 guide vs 11/9 guide. | D; test both |
| Disaster Dish | Croissant + Strawberry + Kakao; or Mug + Lettuce | 8/10 guide vs 11/9 guide. | D; test both |
| Bad Milkshake | Milk + Cheese + Lettuce; or Milk + Cheese + Coffee/Kakao | 8/10 guide vs 11/9 guide. | D; test both |
| Awful Tea | Tea + weird item; or Tea Leaves + Mug + Avocado | 8/10 guide vs 11/9 guide. | D; test both |
| Cup Tower | Paper Cup + Green Mug + White Mug; or Mouse Mug + White + Green Mug | 8/10 guide vs 11/9 guide. | D; identify exact cup item IDs |

Developer evidence:
- Smoothie includes Peanut Butter: [Steam developer reply](https://steamcommunity.com/app/3376500/discussions/0/800090354736014933/).
- Good Protein Shake uses Milk + Peanut Butter + Protein Powder, not Egg: [Steam developer reply](https://steamcommunity.com/app/3376500/discussions/0/760681630846246656/).


## Student Dorm Bad Recipe formula conflicts (1.0 walkthrough vs older guide)

| Recipe | Candidate inputs | Conflict | Handling |
|---|---|---|---|
| Horrible Sandwich | Toast + Egg + Tomato; or Bread + 2 unrelated items | Pixel Questing 10/9 gives a concrete combo; cached Steam guide gives a category predicate. | C/D; test both |
| Beany Mess | Beans + Milk + Tomato; or Beans + 2 unrelated items | Specific vs category predicate. | C/D; test both |
| Carb Overload | Potato + Pasta + Ramen; or Pasta + Bread + Potato | Different third ingredient. | D; test both |
| Tomato Mess | Tomato + Cheese; or Can of Tomatoes + 2 unrelated items | Specific vs category predicate. | C/D; test both |
| Bad Protein Shake | Big Protein + Egg + Tomato; or Protein Powder + 2 unrelated items; or Protein Powder alone | Different guide recipes and ingredient labels. | D; test |
| Bad Ramen | Milk + Ramen + Cheese; or Ramen + 2 unrelated items | Specific vs category predicate. | C/D; test both |
| Sponge Sandwich | Bread + Sponge + Cheese; or Sponge + 2 unrelated items | Specific vs category predicate. | C/D; test both |
| Musical Dish | Cassette + any ingredient; or Audio Tape + 2 food items | Different input count. | D; test 2 vs 3 inputs |
| Canned Food | Kitchen Knife + Beans; or Key + any food | Different tool and ingredient. | D; test both |
| Terrible Smoothie | Egg + Milk + Tomato; or Milk + unrelated items | Specific vs category predicate. | C/D; test both |
| Tape Spaghetti | Ramen + Cassette; or Pasta + Audio Tape | Different carbohydrate item. | D; test both |
| Iron Ingot | Key; or any Knife | Different tool. | D; test both |
| Food Monster | Cheese + Egg + Banana; or any three unrelated items | Specific vs category predicate. | C/D; test both |
| Remix | Pink + Green cassette; or any two of three cassettes | May be compatible if Pink is one of the three cassettes. | C; inspect tape inventory |

## Student Dorm Good Recipe conflicts

| Recipe | Candidate inputs | Evidence | Handling |
|---|---|---|---|
| Sweet Sandwich | Bread + Peanut Butter; or Bread + Strawberry Jam | Cached Steam guide vs Pixel Questing 10/9. | D; test both |
| Smoothie | Milk + Banana + Peanut Butter; or Strawberry Jam + Banana + Milk | Developer says Peanut Butter is an ingredient; 10/9 guide says Strawberry Jam. | B/C; version test |
| Good Protein Shake | Protein Powder + Milk + Peanut Butter; or Protein Powder + Milk + Banana | Developer confirms Peanut Butter and Milk, not Egg; 10/9 guide lists Banana as alternate. | B; Peanut Butter confirmed, Banana candidate |
| Tomato/Egg Stir Fry | Can of Tomatoes + Egg; or Tomato + Egg | Cached Steam guide vs 10/9 guide. | C/D; check canned vs raw Tomato |


## Bistro inventory correction — July 17 discoveries (2026-11-16)

The 2026-07-14 guide's 76 Good / 31 Bad list is not the complete Early Access inventory. Steam discussion comments dated July 17 identify one additional Good recipe and five additional Bad recipes that were missing from the guide's main list:

- Bad: Crazy Calzone = Pizza + Pizza Dough (SRC-050; reclassified to Bad in the current candidate register using SRC-024 counter alignment).
- Bad: Breadless Burger = Ground Meat + Cheese + Tomato.
- Bad: Vampire Defense Kit = Garlic + Wooden Spoon (older comment from July 14 says Garlic + any Pencil; preserve this formula conflict).
- Bad: Bread and Wine = Wine + Bread.
- Bad: Sorrow Sandwich = Bread + Flour.
- Bad: Risky Rice Pudding = Rice + Flour.

Then add the 2026-08-27 update list (7 Good + 2 Bad) and the 1.0 Clutter Bad recipe:
- Good: 76 + 1 + 7 = 84.
- Bad: 31 + 5 + 2 + 1 = 39.
- Bistro candidate total = 123.

This historical revision produced 333 entries (212 Good + 121 Bad); it is superseded by the 1.0 counter-aligned 211 Good + 122 Bad split.

Sources:
- [Steam Bistro Guide and July 17 player comments](https://steamcommunity.com/sharedfiles/filedetails/?id=3764982550)
- [9Puz 1.0 completion route, Crazy Calzone and Bistro cleanup](https://9puz.com/5427-little-chef-cozy-cooking-completion-guide/)
- [Steam guide updated with 8/27 additions](https://steamcommunity.com/sharedfiles/filedetails/?id=3713640352)


## Additional Bistro 1.0 route cross-checks

| Recipe | Candidate formulas / labels | Evidence | Handling |
|---|---|---|---|
| Charcuterie Board | Cheese + Olives + Salami; or Olives + Salami + Bread | 9Puz 1.0 route vs 7/14 Steam guide. | D; test both |
| Pizza Speciale | Pizza + Mushrooms + Salami; or Pizza + Mushroom + Olives | 9Puz 1.0 route vs 7/14 Steam guide. | D; test both |
| Sausage Roll / Salami Roll | Same formula Meat + Bread Dough, but English name differs between 8/10 Steam guide and 9/2 9Puz route. | B/C; compare in-game cookbook spelling; preserve one recipe ID with alias until confirmed |
| Mochi | Rice; or Ground Rice | 9Puz says Rice and cached 8/10 guide says Rice, while a Steam player comment says to grind Rice first. | D; test whole vs ground Rice |
| Tomato Cheese Appetizer | Tomato + Cheese + Olives | 8/10 guide says Olives are a mouse gift; 7/14 guide omitted Olives. | B; keep 3-input candidate |
| Meatballs | Ground Meat + Garlic + Dough; or Ground Beef alone | 9Puz and 8/10 guide vs 7/14 guide. | B; prefer 3-input candidate, verify |
| Beef Katsu Sando | Bread + Meat + Olive Oil; or Bread + Meat | 9Puz / 8/10 guide vs 7/14 guide. | B; test Olive Oil |
| Fried Rice | Rice + Olive Oil + Mushrooms; or Rice + Olive Oil | 9Puz / 8/10 guide vs 7/14 guide. | B; test Mushrooms |
| Sake | Rice + Wine; or Rice + Yeast | 9Puz / 8/10 guide vs 7/14 guide. | B; prefer Wine, verify |
| Tomato Juice | Ground Tomato; or whole Tomato | 9Puz player comment says Ground Tomato; 8/10 guide lists Tomato. | B; Ground Tomato favored |
| Pizza Dough | Flour + Yeast + Olive Oil | Steam player comment corrects the missing recipe; do not treat Bread Dough as the input. | B; confirmed candidate |


## Cafe To-Do count source discrepancy (2026-11-17)

- Official v3.0ea patch note (2026-04-23) says singular: “New Todo: complete 8 orders”. This directly supports one To-Do row with an eight-order target.
- A Japanese April 24 player walkthrough paraphrases the update as “ToDo list, 8 items added”. This could be a translation/counting ambiguity (eight orders vs eight To-Do rows), or could refer to other update content not fully enumerated in the patch note.
- Later v5.1ea official notes say finish the Level 2 To-Do list before Level 3, but do not enumerate its rows.
- A September 1.0 walkthrough reports the fire task can remain unchecked even after setting the kitchen on fire, suggesting a possible registration / task-sync bug.
- Current handling: do not hardcode Cafe To-Do row count. Explicitly model the “8 orders” task and fire task; keep clean-kitchen and rat trade as progression interactions unless the in-game To-Do UI confirms their task status.

Sources:
- [Official v3.0ea patch note mirror](https://steamdb.info/patchnotes/22930769/)
- [Japanese April 24 update walkthrough](https://note.com/utsukinoel/n/nd60de056ab74)
- [Japanese 1.0 completion report](https://note.com/utsukinoel/n/n2734d08070ca)


## Ground Meat / Ground Beef item-key normalization

- The Bistro guide uses “Ground Beef” in Meatball Sandwich and Cheeseburger, while other 1.0 sources and the item-state model use “Ground Meat”.
- No evidence indicates two distinct processed meat items. Normalize the implementation data key to `ground_meat`; keep “Ground Beef” as a source alias, not a separate item state.
- Stuffed Tomato, Hamburger, Meatballs, Breadless Burger and other recipes must reference the same processed meat state unless live UI proves otherwise.


## 2026-11-17｜Student Dorm配方衝突再審（新增來源交叉核對）

- **Clutter：撤回 Cloth + Wooden Spoon。** 1.0日文玩家只確認 Clutter 存在，提示文字暗示「混亂會自行發生」，沒有提供可重現輸入。先前將 Cloth + Wooden Spoon 歸因於「9/1簡中1.0攻略」是來源錯置；該 Steam 頁實為 v4.0 EA且沒有 Bistro 章節，故 trigger 維持 unknown，不能進正式 recipe formula。
- **Smoothie：不再把 Peanut Butter 說成唯一配方。** 開發者只確認 Peanut Butter 是其中一項材料，沒有在回覆中寫完整三材料組合；10/9 1.0攻略列 Strawberry Jam + Banana + Milk。保留 Milk + Banana + Peanut Butter 與 Strawberry Jam + Banana + Milk 兩條候選，等待實機或更多開發者證據。
- **Good Protein Shake：開發者已明確給出 Milk + Peanut Butter + Protein Powder，並明確否定 Egg。** 10/9攻略提到 Banana alternate，先保留為低信心替代，不覆蓋開發者公式。
- **Pasta A La Carbonara：** 8/10 Steam攻略及玩家討論支持 Pasta + Egg + Cheese；10/9 1.0攻略支持 Pasta + Egg + Milk。來源互相矛盾，仍列D級，必須在1.0逐條測試。
- **PB&J Sandwich：** 10/9攻略明確接受 Bread、Toast 或 PB&J Jar + Bread等路徑；這比較像 alternate_inputs，不應誤判成版本衝突。

Sources: SRC-016, SRC-019, SRC-024, SRC-031, SRC-032; [Steam Carbonara discussion](https://steamcommunity.com/app/3376500/discussions/0/800090354736110017/).


## Coioioin 1.0 evidence reconciliation (2026-11-17)

The Japanese 1.0 walkthrough is stronger than the earlier summary gave it credit for: it explicitly says Coioioin is **not** merely getting the same coin face three times by chance, and gives a concrete route: press the switch inside the blue frame, then throw the coin into the red frame. The same author reports that the in-game achievement was earned before Steam displayed it, and Steam sync occurred after closing/relaunching the game.

This conflicts with Steam's official achievement description (“same side ... 3 times in a row”) and an older Steam discussion that says to click the coin repeatedly. Possible explanations include a version change, a secondary deterministic trigger, or a difference between the in-game condition and Steam's achievement text. Do not silently choose one. QA RAT-008/011 must test both routes; RAT-012 tests platform sync separately.

Sources: [Japanese 1.0 first-hand walkthrough](https://note.com/utsukinoel/n/n2734d08070ca), [official Steam achievement text](https://steamcommunity.com/stats/3376500/achievements), [older Steam discussion](https://steamcommunity.com/app/3376500/discussions/0/582806564883173701/).


## Bistro magnet recipes and progression dependency (2026-11-17)
- Big Magnet: 9Puz 1.0 route explicitly says to cook one of the rat-reward Magnets; cached Steam guide only says “Magnet from mouse rewards”. Preserve the cook action as a candidate and verify the Bad Recipe counter before finalizing.
- Compass: Scissors + any country Magnet. 9Puz recommends waiting until the magnet has registered for Going Global before making Compass; represent this as a progression dependency.
- This adds a distinction between receiving a rat reward, registering its country magnet, and consuming a magnet as a recipe ingredient.


## SRC-017 v1.0 mixed-guide corrections (2026-11-17)

SRC-017 is confirmed to be a v1.0-titled guide updated 2026-09-08, with legacy v4.0 EA material plus Bistro and Rat Level sections. The author warns that first-two-room data may be stale and manually typed formulas may be wrong. Use its Bistro/Rat Level data as C-level 1.0 candidates, not definitive truth.

| Recipe / slot | SRC-017 candidate | Competing candidate | Current handling |
|---|---|---|---|
| Goulash | Meat + Ground Tomato + Wine; author says cookbook icon showed whole Tomato incorrectly | SRC-050 list says Meat + Ground Tomato + Wine; official v1.1 says cookbook recipe fixed | Formula now has strong community convergence; retain v1.1 regression test for exact current item state |
| Tomato Cocktail | Olives + Ground Tomato + Red Wine; author/player comment reports cookbook icon mismatch | SRC-050 says Olives + Ground Tomato + Wine | Prefer Red Wine as a test candidate; do not collapse wine-state difference without live check |
| Clutter | **Formula unknown**; Cloth + Wooden Spoon withdrawn | SRC-024 1.0 player walkthrough describes clutter as happening spontaneously, but gives no reproducible input | Test idle/physics-trigger hypothesis; direct combinations remain experiments, not sourced formula |
| Vampire Defense Kit | Tomato + Wooden Spoon | SRC-050 says Garlic + Wooden Spoon; older comment says Garlic + Pencil | D-level; test all separately |
| Bread Sticks | Pizza Dough alone | SRC-015 says Pizza Dough + Olive Oil | D-level; test both |
| Crazy Calzone | Pizza + Pizza Dough | SRC-050 lists it in Bad; SRC-024 1.0 counter aligns with Bad classification | Pizza + Wooden Spoon is withdrawn as a sourced candidate; verify actual card tab with BIS-061 |
| Bad Pastry | Yeast + Bread Dough + Pizza Dough | SRC-015/SRC-050 list Bread Dough + Flour (+/- Pizza) | D-level; test separately |
| Sorrow Sandwich | Bread + Wooden Spoon | SRC-050 says Bread + Flour | D-level; test both |
| Risky Rice Pudding | Rice + Wooden Spoon | SRC-050 says Rice + Flour | D-level; test both |
| Rat cold Good #5 | Cheese + Leaf | SRC-050 says Cheese + Eggshell; 9Puz notes icon ambiguity | SRC-017 is now the strongest direct 1.0 candidate; test Leaf first, Eggshell alternate |
| Rat Bad #4 | Eggshell + Pencil | SRC-050 says Egg + Pencil | Keep both; 1.0 source favors Eggshell |
| Rat Bad #6 | Pasta alone | SRC-050 says Paperclip + Pasta | Keep both; 1.0 source favors Pasta alone |
| Rat Bad #7 | Pasta + Paper | SRC-050 says Eggshell + Paper | Keep both; 1.0 source favors Pasta + Paper |

Other SRC-017 Bistro confirmations: Mochi uses Ground Rice; Apple Mochi uses Ground Rice + Apple; Pizza Dough = Flour + Yeast + Olive Oil; Meatloaf = Ground Meat + Meat; Tomato Juice = Ground Tomato. These strengthen existing candidates and reduce earlier ambiguity.


## SRC-052 Rat Level independent cross-check (2026-11-17)
SRC-052 (Steam guide posted 2026-08-27) independently lists the full Rat Level slot order and puzzle sequence. It aligns with SRC-050 / 9Puz on the following disputed slots, so these are now the preferred candidates while SRC-017 remains a competing 1.0 manual transcription:

| Slot | Preferred candidate | Competing SRC-017 candidate | Evidence handling |
|---|---|---|---|
| Cold Good #5 | Cheese + Eggshell | Cheese + Leaf | SRC-050 + SRC-052 + 9Puz vs SRC-017; Eggshell favored, Leaf retained for live counter test |
| Bad #4 | Eggshell + Pencil | Egg + Pencil | SRC-017 + SRC-052 vs SRC-050; Eggshell favored |
| Bad #6 | Paperclip + Pasta | Pasta alone | SRC-050 + SRC-052 vs SRC-017; Paperclip + Pasta favored |
| Bad #7 | Eggshell + Paper | Pasta + Paper | SRC-050 + SRC-052 vs SRC-017; Eggshell + Paper favored |

SRC-052 also says repeated coin clicks beside the planter can earn Coioioin, matching official same-face-three-times wording. Keep the Japanese 1.0 blue-switch/red-target method as an alternate route, not a replacement for the official condition. The numeric password remains undisclosed.


| Recipe | Candidate A | Candidate B / C | Evidence and current handling |
|---|---|---|---|
| Mochi (Japan country dish) | Ground Rice (SRC-017 manual v1.0 guide) | Whole Rice (SRC-015 / SRC-050) | 1.0 candidate conflict; test whole and ground separately. Do not confuse with Apple Mochi. |
| Yeast Monster | Yeast + Wooden Spoon (SRC-017) | Yeast + Wine (SRC-015) / Yeast + Tomato (SRC-050) | Three-way conflict; no candidate promoted until slot counter or in-game recipe card confirms. |


## SRC-055｜Bistro 三道配方玩家討論交叉核對（2026-11-17）

Steam「Assistance with Level 3」討論串（76則留言）補足三道常卡關配方，並特別揭露 Goulash 的材料狀態錯誤：

| Recipe | 首選候選 | 證據細節 | 信心／處理 |
|---|---|---|---|
| Goulash | **Normal Meat + Ground Tomato + Wine** | 最初留言誤寫 processed meat + tomato + wine；另一玩家指出應是 processed tomato/tomato sauce；原留言者再明確修正為 normal meat + processed tomato + wine，並承認自己把材料寫反。 | B；Normal Meat 與 Ground Meat 必須是不同 item state；以此作首選，仍待遊戲內確認 |
| Risotto | Rice + Mushroom + Cheese | 同一討論串的玩家提供配方，沒有後續反駁；與現有 Bistro 配方資料相容。 | C；候選，不標記 verified_in_game |
| Focaccia | Bread Dough + Olives + Olive Oil | 同一討論串玩家提供配方；與現有攻略的三材料配方一致。 | B；候選，不標記 verified_in_game |

**重要修正：** Goulash 不是 Ground Meat + Ground Tomato + Wine。若配方系統只用「Meat」而不區分 Normal Meat / Ground Meat，會把 Goulash 與 Meatloaf 等加工肉配方混淆。RecipeConditions 必須引用明確 item_state，而不能用模糊的 meat 類別。

來源：SRC-055，Steam Community「Assistance with Level 3」，2026-07-12，留言 #1、#3、#5、#6。


## SRC-056｜Bistro 食譜圖示錯誤與翻譯暫譯證據（2026-11-17）

Steam討論「Level 3 BUG + 中文翻譯勘誤」包含玩家對配方圖示與菜名的回報，開發者Leek於7月14日回覆：當時所有新菜名翻譯只是暫時版本，使用DeepL，待文本定稿後會由中文譯者校正。這是重要版本限制：EA期間的繁中名稱不可直接視為1.0正式在地化字串。

| 項目 | 新證據 | 目前處理 |
|---|---|---|
| Tomato Cocktail | 玩家指出配方圖示把「Wine」顯示成「Meat」，並將配方描述為 Tomato Sauce + Wine + Olives。 | 與 Ground Tomato + Wine + Olives 候選相符；可解釋早期圖示誤導。Wine / Red Wine仍須區分測試。 |
| Kombucha | 同一玩家明確聲稱「實際上沒有蘑菇」，與多份攻略的 Mushroom + Yeast 相衝突。 | 不視為開發者確認；升級為明確反證候選，必須測試 Yeast 單獨、Yeast + Mushroom及其他候選，不可沿用Mushroom+Yeast作定案。 |
| 繁中菜名 | 開發者確認當時新菜名為DeepL暫譯，之後會人工校正。 | glossary需標註EA暫譯來源，不可直接複製成正式1.0 zh-TW字串；逐項核對最終UI。 |

來源：SRC-056，留言主文及開發者Leek回覆。

## SRC-057｜老鼠交易鏈與七國磁鐵是兩條相關但不同的機制

2026-09-09的EA實際遊玩紀錄（含遊戲截圖）提供更清楚的區分：

- Bistro老鼠位於抽油煙機；先給Cheese，得到Tomato。
- 後續抽油煙機會出現料理圖示便條，完成圖示料理會換得新食材。這是「老鼠交易／特殊食材解鎖」鏈。
- 另有七道國際料理；每做成一道，磁鐵會附到抽油煙機。Japan = Mochi，且Mochi畫面附日本國旗與日本體驗敘述。
- Apple Mochi雖是另一道料理，但作者明確說它不是日本磁鐵料理；可疑料理也不計入七國料理。
- 該EA截圖的Bistro cookbook counter顯示76/76（頁面1/3），只能作為2026-09-09當時的版本快照，不能取代1.0跨來源候選數或官方counter。

**目前可確定的結論：** 不可把「四次老鼠交易」、「七道國際料理」、「七個國家磁鐵」當成同一個數量或同一張清單。兩條鏈有食材依賴關係，但完成條件不同。七國中目前仍只有Japan = Mochi具名；其餘六國與料理名、完整rat request/reward順序都未公開在可讀文字中。

來源：SRC-057，Lines 120–164及嵌入圖片（Mochi卡、Apple Mochi卡、Going Global成就圖）。

## SRC-058｜Pizza Dough 加工前置狀態更正

Steam討論串「help level 3 - pizza dough」最初回覆為 Dough + Yeast + Olive Oil；2026-08-21另一名玩家明確更正為 **Flour, not Dough**。這與SRC-015 Bistro Guide及SRC-018 1.0路線的配方 **Flour + Yeast + Olive Oil** 一致。

| Recipe | Wrong / outdated candidate | Preferred candidate | Evidence | Status |
|---|---|---|---|---|
| Pizza Dough | Dough + Yeast + Olive Oil | **Flour + Yeast + Olive Oil** | SRC-015 + SRC-018 + SRC-058; SRC-058明確指出Flour而非Dough | B；來源交叉一致，仍待本專案實機驗證 |

## Bistro Good/Bad 分類校正｜Crazy Calzone

- SRC-050 Steam recipe guide將Crazy Calzone列於Ch 3 Bad Recipes，配方Pizza + Pizza Dough。
- SRC-018 1.0 completion route提到相同材料配方，但未明示Good/Bad tab。
- SRC-024的1.0實機存檔畫面顯示Bistro目標為83 Good / 40 Bad；本專案舊清單為84 Good / 39 Bad。將Crazy Calzone由Good移至Bad後，剛好與1.0目標counter一致。
- **目前處理：** 候選清單改列Bad（高信心、counter-aligned），但尚未看到Crazy Calzone卡片本身的tab畫面；BIS-061仍需實機確認，不標verified。


## Clutter source correction｜SRC-024（2026-11-17）

Re-opened the actual 2026-09-10 Japanese 1.0 completion article (SRC-024). The player identifies Clutter as the final Bad recipe and quotes its hint as something that sometimes gets messy “on its own”; the article does **not** provide a formula. The earlier Cloth + Wooden Spoon candidate is withdrawn because its alleged source attribution was incorrect. Keep the recipe name and trigger hint, but leave the formula unknown. BIS-018 and BIS-040 remain the required reproduction tests.


## SRC-050 vs SRC-057｜七國磁鐵觸發來源衝突（2026-11-17）

| 問題 | 候選說法 A | 候選說法 B | 暫定處理 |
|---|---|---|---|
| 七國磁鐵如何取得 | SRC-050 Steam Bistro recipe guide 的成就說明稱每個磁鐵由老鼠在玩家完成請求料理後給予 | SRC-057 日文實際遊玩紀錄把老鼠便條交易（完成圖示料理→獲得特殊食材）與七道國際料理（完成後磁鐵附到抽油煙機）分開敘述；Japan = Mochi | **未定案。** 不得把 rat trade reward 與 country-magnet trigger 當成同一機制。可能存在食材解鎖依賴，但觸發方式須以逐步畫面／counter驗證。BIS-062新增分離測試。 |

具體差異：SRC-054開發者只確認「Cheese啟動老鼠請求→依料理圖製作→換得新食材」，沒有提國家磁鐵；SRC-057直接文字說國際料理會把磁鐵附在抽油煙機；SRC-050的成就註解則把磁鐵歸因於老鼠。兩份玩家來源不能互相覆蓋。七國料理全名仍只確認Japan = Mochi。


## SRC-066｜Chinese v1.0 guide introduces additional Bistro formula conflicts
The Steam guide by 一旁冷笑 (updated 2026-09-08) explicitly warns that some formulas may be inaccurate and some content is AI-bulk-added. Its manually written Bistro section nonetheless reports several candidates that conflict with the August 10 Steam recipe guide and/or other community sources:

| Recipe | SRC-066 candidate | Conflicting candidate(s) | Required resolution |
|---|---|---|---|
| Mochi | Ground Rice | Whole Rice | BIS-065; also determine whether this exact card creates Japan magnet |
| Apple Mochi | Ground Rice + Apple | Rice + Apple | BIS-065; do not conflate with Mochi |
| Sake | Rice + Yeast | Rice + Wine | BIS-064 |
| Tomato Cheese Appetizer | Tomato + Cheese | Tomato + Cheese + Olives | BIS-063 |
| Tomato Cocktail | Ground Tomato + Wine; guide says cookbook display is wrong | Ground Tomato + Wine + Olives; prior cookbook icon showed Meat | BIS-066; test actual result and v1.1 cookbook display |
| Mushroom Soup | processed Mushroom alone | Mushroom + Garlic | BIS-067 |
| Pumpkin Soup | Ground Pumpkin alone | Ground Pumpkin + Garlic | BIS-068 |
| Meatballs | Ground Meat alone | Ground Meat + Garlic + Dough | BIS-069 |

The same guide reports Goulash as Meat + Ground Tomato + Wine and explicitly says the cookbook may display whole Tomato instead of Ground Tomato; this aligns with the existing candidate in BIS-023 rather than creating a new formula. The new source does not close any of the above conflicts without in-game execution.
