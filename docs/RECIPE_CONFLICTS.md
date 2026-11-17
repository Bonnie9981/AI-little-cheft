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
| Goulash | Meat + Ground Tomato + Wine | Steam Bistro Guide 正文列出此配方，作者留言也特別更正 Ground Tomato；v1.1 官方只確認修正 cookbook，沒有列配方。 | B；保留 Ground Tomato 狀態，待實機 |
| Tomato Cocktail | Ground Tomato + Olives + Wine | 8/10 Steam guide 與 7/14 Bistro guide 一致；v1.1 官方確認修正 cookbook，但未公開配方。 | B；待實機 |
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

- Official v3.0ea says 8 To-Do entries were added; one is completing 8 orders. Japanese player notes confirm illustrated order slips, tip coins, and that completing a dish checks the corresponding order.
- The complete names/order of all 8 Cafe To-Do entries have not yet been recovered. Do not equate “8 orders” with “8 To-Do entries”; keep these as separate counters until verified.


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
| Bad | Big Magnet | Magnet received from rat reward | Community guide lists it as new |
| Bad | Boo Tomato | Tomato | Community guide lists it as new |
| Bad | Clutter | Trigger unknown; description suggests spontaneous mess | 1.0 player reports this as final Bad recipe; do not assume Mixer until verified |

The 1.0 player walkthrough reports approximately 10 Bistro additions. The 8/10 Steam Guide lists 7 Good + 2 Bad; the 9/10 completion report adds Clutter as a final Bad entry. This is a coherent 7+3 candidate set, but the exact in-game counter should be checked before treating the count as final.

## Rat Level achievement interaction

Coioioin primary trigger: click the coin beside the cooker until the same face lands three times in a row, matching the official Steam achievement text and multiple guides. A separate player report mentions a blue switch / red-marked toss area, but it is not corroborated and should not supersede the official description. Source: [Steam achievements](https://steamcommunity.com/stats/3376500/achievements), [9Puz 1.0 route](https://9puz.com/5427-little-chef-cozy-cooking-completion-guide/), [Steam guide](https://steamcommunity.com/sharedfiles/filedetails/?id=3713640352&l=swedish).


## Bistro count reconciliation

The directly opened 2026-07-14 Bistro Guide contains 76 Good entries (lines 91-166) and 31 Bad entries (lines 170-200): this is the Early Access baseline, not necessarily the 1.0 final total. The 2026-08-27 update list adds 7 Good + 2 Bad; the 2026-09-10 1.0 player completion report identifies Clutter as another final Bad entry. This 83/34 estimate is superseded by the July 17 comment discoveries below. Current cross-source candidate total: 84 Good / 39 Bad = 123. This remains a derived estimate until a 1.0 cookbook counter is verified.

Sources:
- [7/14 Bistro Guide](https://steamcommunity.com/sharedfiles/filedetails/?id=3764982550)
- [8/10 guide, updated with 8/27 additions](https://steamcommunity.com/sharedfiles/filedetails/?id=3713640352)
- [9/10 1.0 completion report](https://note.com/utsukinoel/n/n2734d08070ca)


## Bistro rat request and country-dish evidence

- Developer-confirmed interaction: offer Cheese to the rat behind the suspicious extractor-hood door; the rat then displays a dish drawing, and completing that dish trades for a new ingredient. Source: [Steam developer reply, 2026-07-16](https://steamcommunity.com/app/3376500/discussions/0/574921459914308481/).
- First player-recorded reward is Tomato. Later mouse rewards include Apple, Olive, and Garlic. The exact order of all rewards is not yet established.
- Going Global requires seven country dishes and seven magnets. Only Mochi (Japan) is explicitly identified in readable text. The other six dish-country pairs remain unknown and must not be inferred from recipe names alone.
- The final heart note is a thank-you after the request chain is complete, not a request to cook Meat Lover Pizza. Source: [Steam discussion](https://steamcommunity.com/app/3376500/discussions/0/582806564883159730/).


## Additional 1.0 Bistro conflicts from the Simplified Chinese 1.0 guide

The 2026-09-01 community guide is useful as a later-version cross-check, but its author explicitly warns that updates may change recipes. It also includes several formula claims that conflict with other guides, so these remain candidates.

| Recipe | Candidate inputs / states | Conflict | Handling |
|---|---|---|---|
| Mochi | Rice; or Ground Rice | 7/14 guide says Rice; 8/10 guide says Rice; 9/1 Chinese guide says rice flour. | D; test whole vs processed Rice |
| Apple Mochi | Rice + Apple; or Ground Rice + Apple | 7/14 guide says Ground Rice; 8/10 guide says Rice; 9/1 Chinese guide says rice flour + Apple. | B/C; Ground Rice candidate, test |
| Kombucha | Mushroom + Yeast; or Yeast + another ingredient | 7/14 guide, 8/10 guide, and Steam player replies repeatedly support Mushroom + Yeast; one Chinese community correction says it does not use Mushroom. | B; Mushroom + Yeast favored, verify |
| Tomato Juice | Tomato; or Ground Tomato | 7/14 guide and player comment support Ground Tomato; 8/10 guide says Tomato. | B; Ground Tomato candidate |
| Fried Rice | Rice + Olive Oil; or Rice + Olive Oil + Mushroom | 7/14 guide uses two inputs; 8/10 guide adds Mushroom. | D; test two- and three-input variants |
| Sake | Rice + Yeast; or Rice + Wine | Older and later sources are inconsistent. | D; test both |
| Meatballs | Ground Beef alone; or Ground Meat + Garlic + Dough | 7/14 guide lists Ground Beef; 8/10 guide lists three inputs; 9/1 guide uses Ground Meat. | D; preserve variants |
| Beef Katsu Sando | Meat + Bread; or Bread + Beef + Olive Oil | 7/14 guide lists Meat + Bread; 8/10 guide adds Olive Oil. | D; test |
| Tomato Cheese Appetizer | Tomato + Cheese; or Tomato + Cheese + Olives | 7/14 guide omits Olives; 8/10 guide says Olives (mouse gift) are required. | D; test with and without Olives |
| Yeast Monster | Yeast + Wine; or Yeast + Tomato | 7/14 guide says Wine; 8/10 guide says Tomato. | D; test both |
| Cookbook | Newspaper + Apple; or Newspaper + Tomato | 7/14 guide says Apple; 8/10 guide says Tomato. | D; test both |
| Bad Meatloaf | Meat + Flour; or Meat + Olives | 7/14 guide and later guide differ. | D; test |
| Food Sketch | Apple + Any Pencil; or Cheese + Any Pencil | 7/14 guide says Apple; later guide says Cheese. | D; test |
| Fried Balls | Bread + Olive Oil; or Salami + Olive Oil | 7/14 guide says Bread; 8/10 guide says Salami. | D; test |
| Vampire Defense Kit | Garlic + Any Pencil; Garlic + Wooden Spoon; or Tomato + Spoon | 7/14 comment, 8/10 guide, and 9/1 Chinese guide differ. | D; test |
| Clutter | Cloth + Wooden Spoon | 9/1 Chinese guide gives this formula; 9/10 Japanese guide confirms Clutter exists but does not list inputs. | C; best current candidate |
| Rat cold Good slot #5 | Cheese + Eggshell; or Cheese + Leaf | 8/10 guide says Eggshell; 9/1 Chinese guide says Leaf; 9/10 Japanese guide does not resolve. | D; test both and inspect live slot |
| Rat bad slot #4 | Egg + Pencil; or Eggshell + Pencil | 8/10 guide says Egg; 9/1 Chinese guide says Eggshell. | D; test both |
| Rat bad slot #6/#7 | Pasta alone; Pasta + Paper; or Paperclip + Pasta | 8/10 guide lists Paperclip + Pasta; 9/1 Chinese guide lists Pasta alone and an additional Pasta + Paper candidate. | D; test all separately |

Sources:
- [Simplified Chinese 1.0 achievement guide (updated 2026-09-01)](https://steamcommunity.com/sharedfiles/filedetails/?id=3686619896)
- [Steam Bistro recipe discussion (July 12 onward)](https://steamcommunity.com/app/3376500/discussions/0/568165880361398668/)
- [Steam 8/10 recipe guide](https://steamcommunity.com/sharedfiles/filedetails/?id=3713640352)
- [Steam 7/14 Bistro guide](https://steamcommunity.com/sharedfiles/filedetails/?id=3764982550)


## Puzzle rule evidence

- Wine About It: a Steam player reports the five bottles should be ordered by label height, shortest to tallest. This is more actionable than guessing by wine color or name. Source: [Steam Level 3 discussion](https://steamcommunity.com/app/3376500/discussions/0/568165880361398668/).
- Rat Level slot conflicts are version/source conflicts, not translation-only issues: Cold Good #5 is Cheese + Leaf in the 1.0 Chinese guide vs Cheese + Eggshell in the English guide; Bad #4 is Eggshell + Pencil vs Egg + Pencil; Bad #6/#7 include Pasta alone, Pasta + Paper, or Paperclip + Pasta.
- Coioioin has a 1.0 player report of pressing the blue switch before tossing the coin; keep the older three-same-side achievement description, but test whether the switch modifies the coin outcome.


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
| Good Protein Shake | Protein Powder + Milk + Peanut Butter; or Protein Powder + Milk + Banana | Developer explicitly corrects Milk (not Egg); 10/9 guide lists Peanut Butter or Banana. | B; Peanut Butter is confirmed, Banana alternate unverified |
| Savory Sandwich | Bread + Egg; Bread + Cheese + Tomato Sauce; or Bread + Cheese + Tomato | Official v2.9 adds Tomato Sauce variant; later guides differ on Sauce vs raw Tomato. | A/B; preserve separate input sets |
| Pasta A La Carbonara | Pasta + Egg + Cheese; or Pasta + Egg + Milk | 8/10 cached Steam guide vs 10/9 Pixel Questing. | D; test both |
| Beans on Toast | Bread + Beans; or Beans + Toast | 8/10 cached Steam guide vs 10/9 Pixel Questing. | D; test Bread vs Toast state |
| Tomato Soup | Tomato; or Tomato + Toast | 8/10 cached Steam guide vs 10/9 Pixel Questing. | D; test both |
| PB&J Sandwich | Bread + Peanut Butter + Jam; or PB&J jar + Bread | 10/9 guide adds PB&J jar intermediate; 8/10 guide uses three inputs. | C; test both |
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

- Good: Crazy Calzone = Pizza + Pizza Dough.
- Bad: Breadless Burger = Ground Meat + Cheese + Tomato.
- Bad: Vampire Defense Kit = Garlic + Wooden Spoon (older comment from July 14 says Garlic + any Pencil; preserve this formula conflict).
- Bad: Bread and Wine = Wine + Bread.
- Bad: Sorrow Sandwich = Bread + Flour.
- Bad: Risky Rice Pudding = Rice + Flour.

Then add the 2026-08-27 update list (7 Good + 2 Bad) and the 1.0 Clutter Bad recipe:
- Good: 76 + 1 + 7 = 84.
- Bad: 31 + 5 + 2 + 1 = 39.
- Bistro candidate total = 123.

This revises the all-room candidate register to 333 entries: 212 Good + 121 Bad. This is a stronger cross-source estimate, still not an official in-game counter.

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
| Mochi | Rice; or Ground Rice | 9Puz says Rice, 8/10 guide says Rice, but Steam player comment says grind Rice first and 9/1 Chinese guide says rice flour. | D; test whole vs ground Rice |
| Tomato Cheese Appetizer | Tomato + Cheese + Olives | 8/10 guide says Olives are a mouse gift; 7/14 guide omitted Olives. | B; keep 3-input candidate |
| Meatballs | Ground Meat + Garlic + Dough; or Ground Beef alone | 9Puz and 8/10 guide vs 7/14 guide. | B; prefer 3-input candidate, verify |
| Beef Katsu Sando | Bread + Meat + Olive Oil; or Bread + Meat | 9Puz / 8/10 guide vs 7/14 guide. | B; test Olive Oil |
| Fried Rice | Rice + Olive Oil + Mushrooms; or Rice + Olive Oil | 9Puz / 8/10 guide vs 7/14 guide. | B; test Mushrooms |
| Sake | Rice + Wine; or Rice + Yeast | 9Puz / 8/10 guide vs 7/14 guide. | B; prefer Wine, verify |
| Tomato Juice | Ground Tomato; or whole Tomato | 9Puz player comment says Ground Tomato; 8/10 guide lists Tomato. | B; Ground Tomato favored |
| Pizza Dough | Flour + Yeast + Olive Oil | Steam player comment corrects the missing recipe; do not treat Bread Dough as the input. | B; confirmed candidate |
