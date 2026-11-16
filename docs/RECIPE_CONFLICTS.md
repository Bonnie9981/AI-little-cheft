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
