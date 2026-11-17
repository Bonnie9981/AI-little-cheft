# Little Chef 復刻｜內部工作紀錄（交接版）

更新日期：2026-11-17  
Repository：https://github.com/Bonnie9981/AI-little-cheft  
分支：main  
階段：Research Only，尚未開始正式遊戲實作。

## 0. 不可違反的專案原則
1. 目標是《Little Chef: Cozy Cooking》的忠實網頁復刻，不是只做相似料理遊戲。
2. 正式語言：台灣繁體中文（zh-TW）。
3. 美術：保留原作溫暖、可愛、柔和的感覺，但以自行重繪素材為主；不可假設正式遊戲素材可自由使用。
4. 內容目標：完整場景、食譜、互動、成就、隱藏內容與額外關卡。
5. 存檔：瀏覽器本機存檔，規劃 JSON 匯出／匯入。
6. **在研究、資料庫、食譜驗證、機制規格、QA 驗收與 Critic 審查完成前，不開始正式開發。**
7. 使用者已要求主動繼續，不要每一步都要求批准。
8. 只使用 Bonnie9981/AI-little-cheft，不要誤動 AI-Animation-Studio。

## 1. GitHub 狀態（2026-11-17 最新）
- Repository 公開，default branch main，ID 1460048753。
- GitHub App 安裝涵蓋 all repositories；此 Repository 列在安裝清單，metadata 顯示 push=true。
- ChatGPT GitHub 專屬權限顯示 Allow all actions。
- 之前 create_file 曾回傳 403，但本輪再次嘗試已成功：
  - 刪除根目錄測試空白檔「？」（檔案內容只有換行），刪除 commit：86413423279f303e1536947c5441d9d395ecff9f
  - 建立 README.md 成功，commit：26433ba4a95a3b3b996e536f6be161cba497c401
- 因此不能再說 GitHub 寫入完全不可用；現在應繼續將研究文件推送至此 repo。
- 測試檔「？」已刪除；不要再刪其他使用者檔案，除非使用者明確要求。

## 2. 主要場景與流程
Main Menu → My Room → Student Dorm / Cafe / Bistro → 三個主廚房皆 100% → Rat Level
- My Room 是樞紐空間，不是第四個主廚房。
- Rat Level 是三個主廚房完成後解鎖的額外內容。
- 平台：桌面瀏覽器、手機橫向。
- 核心操作：拖曳、投擲、碰撞、切割、混合、烹煮、物件狀態變化。
- 物理模擬與食譜判定分離。
- 候選技術可考慮 TypeScript + Phaser/Canvas + Matter.js + IndexedDB；這只是本專案方案，不是原作技術的事實。

## 3. 規格與資料庫方向
已規劃資料實體：
Items、ItemStates、Recipes、RecipeInputs、RecipeOutputs、RecipeConditions、Equipment、ProcessingRules、Interactions、UnlockConditions、Achievements、RatTrades、SceneTasks、AssetRegistry、TranslationDictionary、ResearchEvidence、RecipeEvidence。

每筆食譜至少記錄：場景、輸入物件與數量、加工狀態／前置處理、設備、溫度、順序或位置條件、輸出物件、Good/Bad/特殊分類、適用版本、來源可信度、驗證狀態及 zh-TW 名稱描述。

存檔規劃：IndexedDB 作主要存檔，localStorage 放偏好設定；支援 JSON 匯出／匯入。

## 4. 官方研究證據（既有搜尋 refs）
- Steam 商店頁：AppID 3376500；宣傳資料提及 300+ recipes、約 3 小時、三個主廚房及物理互動。refs：turn149834search8、turn149834search10、turn287487search10。
- 官方公告：三個主廚房皆 100% 後解鎖 Rat Level。refs：turn298030search8、turn298030search0。
- Bistro 第三關發布日期 2026-07-12。ref：turn388216search5。
- v1.1（2026-09-11）修正 Coioioin、文字、重複罐子、食譜書設定，並涉及 Goulash、Tomato Cocktail。refs：turn287487search0、turn287487search1、turn388216search7。
- 2026-08-26 hotfix 修正 Shredded Cheese 錯誤變成 Pizza。refs：turn298030search8、turn298030search0、turn345624view3。
- 開發者說明 Bistro 老鼠：抽油煙機可疑門後；用 Cheese 觸發；老鼠顯示菜餚圖示，完成指定菜餚交換食材。refs：turn388216search6、turn298030search11。
- Prototype sprite pack CC0 只適用該 prototype pack，不代表正式遊戲素材可自由使用。ref：turn149834search0。

## 5. 玩家攻略線索與未解疑點
玩家攻略只能標為 community-reported / unverified，不能當官方定論。

### Bistro
已見食譜線索包括：
Fried Mushrooms（Mushrooms + Flour + Olive Oil）、Charcuterie Board（Cheese + Olives + Salami）、Pepperoni Pizza（Pizza + Salami）、Steak（Meat + Olive Oil）、Stick Bread（Wooden Spoon + Bread Dough）、Meatball Sandwich（Bread + Ground Meat）、Pizza Speciale（Pizza + Mushrooms + Salami）、Focaccia（Bread Dough + Olives + Olive Oil）、Cheeseburger（Bread + Cheese + Ground Meat）、Aioli（Garlic + Olive Oil）、Fried Rice（Olive Oil + Rice + Mushrooms）、Pizza Rolls（Pizza Dough + Salami + Cheese）、Stuffed Olives（Olives + Cheese）、Wine Barrel（Wine + Wooden Spoon）、Mozzarella Sticks（Cheese + Flour + Olive Oil）、Fried Olives（Olives + Flour + Olive Oil）、Rice Paper（Rice + Newspaper）、Sake（Rice + Wine）、Tomato Rice（Tomato + Rice）、Roasted Veggies（Mushroom + Tomato + Pumpkin）、Cheesy Bread（Cheese + Bread）、Boiled Rice（Rice）、Roasted Mushrooms（Mushrooms）、Meat Skewers（Meat + Wooden Spoon）、Leftover Pizza（Slice of Pizza）、Mini Pizzas（Pizza + Scissors）、Paper Towel（Newspaper + Cloth）、Pencil Sharpener（Any Pencil + Scissors）、Oil Paint（Olive Oil + Any Pencil）、Crazy Calzone（Pizza + Pizza Dough）、Breadless Burger（Ground Meat + Cheese + Tomato）、Vampire Defense Kit（Garlic + Wooden Spoon）、Bread and Wine（Wine + Bread）、Sorrow Sandwich（Bread + Flour）、Risky Rice Pudding（Rice + Flour）、Boo Tomato（Tomato）。

加工物件線索：Ground Meat、Ground Tomato、Ground Pumpkin、Ground Apple、Shredded Cheese、Minced Garlic。設備線索：mixer、cooking pot、oven。食材含 Flour、Rice、Bread Dough、Meat、Salami、Tomato、Pumpkin、Garlic、Mushroom、Apple、Olive、Wine、Yeast、Cheese；Apple、Olive、Garlic 為老鼠獎勵解鎖。

重要疑點：
- Goulash 的玩家配方回報互相矛盾；v1.1 有官方更新線索，必須重新驗證條件與版本。
- Risotto 線索：Rice + Mushroom + Cheese。
- Focaccia 線索：Bread Dough + Olives + Olive Oil。
- Shredded Cheese 曾有 bug，須依修正後版本記錄。
- Bistro 資料不可宣稱已完整。

### Cafe / Student Dorm / Rat Level
- Student Dorm 與 Cafe 的舊攻略已有大量食譜線索，但總數曾不一致；需重新計數、逐條驗證。
- Cafe Tiramisu 有配方差異：舊資料 Cake + Coffee + Milk；新資料 Cake + filled espresso cup + Milk，需標記版本與狀態。
- Espresso Shot 需將小白杯放在 espresso machine 出液口下；Double Espresso 要保留杯子再操作一次。
- Cafe 老鼠、Security Card（照片 + Coin）、電話／便條紙解鎖 Avocado／Lettuce 等互動需整理成流程。
- Rat Level 冷／熱烤箱可能產生不同結果；三位數密碼線索：點肖像啟動反重力、漂浮物提示花盆紙條、酒瓶標籤開啟密碼輸入、輸入後開爐。需重新驗證。
- Rat Level 配方仍有 Egg/Eggshell、Leaf 等衝突，不可定稿。

## 6. 成就線索（26 項）
Unpacked, Squeaky Clean, Flooded, Tilted, Fair Trade, To Infinity, I Smell Cheese, A Lot to the Right, Level 1, Post A Lot, What's The Emergency, Cut The Rope, Aw That's Hot, Best Friends, Fruit Samurai, Is This Logo Taken?, Level 2, Going Global, Bookworm, Credits To You, Level 3, Messing Around, Wine About It, Little Rat, Coioioin, Nothing Nowhere。
Nothing Nowhere 的攻略線索為製作 VOID BAGEL（可能需要三個 Bagels），仍應驗證。成就 refs：turn388216search0、turn388216search9。

## 7. 粗略工作估計（非驗收）
- 場景／主流程 100%
- Student Dorm 食譜 90%
- Cafe 食譜 90%
- Bistro 食譜 85%
- Rat Level 85%
- 解鎖流程 90%
- 成就 95%
- 物理互動 45%
- zh-TW 詞庫 55%
- 資料庫驗證 25%

這些是主觀估計，不代表 QA 完成。尤其配方線索未必等於已驗證配方。

## 8. 時間線
- 2026-07-12：Bistro 第三關推出。
- 2026-08-26：hotfix 修正 Shredded Cheese bug。
- 2026-09-11：v1.1 更新，含成就／文字／物件／食譜相關修正。
- 2026-11-16：整理研究交接；確認 Repository；刪除測試空白檔「？」；成功建立 README；準備推送研究文件。

## 9. 下一步工作
1. 完成所有場景食譜統一格式、逐條來源與版本核驗；優先解決 Bistro Goulash、Tomato Cocktail、Shredded Cheese、Rat Level 冷熱配方。
2. 補齊拖曳、投擲、碰撞、切割、液體、攪拌、烹煮、加工狀態規格；不臆測物理係數，以可觀察行為設計驗收。
3. 完成老鼠交易、隱藏物件、場景任務、成就、解鎖流程。
4. 完成台灣繁中術語表。
5. 建立食譜／互動／成就／解鎖／存檔 QA 案例。
6. 由 Critic 獨立找錯與挑戰假設。
7. 以上通過後才開始正式遊戲實作。

## 10. 工作方法與目前判斷
- Evidence-first：先官方，缺漏時用多個玩家來源交叉比對。
- State-aware：把加工狀態、設備、溫度、順序納入食譜。
- Version-aware：每筆資料標記版本。
- Separation of concerns：物理、配方、任務、成就、存檔分開。
- No false completion：不把推測寫成事實，不把失敗的上傳說成成功。
- User final decision：沿用使用者已確認的範圍與方向。

目前最大風險不是畫面，而是規則資料庫的錯漏。應先完成可追溯、可驗證、可測試的全場景資料庫，避免過早開發造成返工。


## 12. 2026-11-16 研究補充與更正
- 新找到 Steam Guide ID 3713640352，搜尋索引標示更新至 2026-08-10，包含 Bistro 配方章節；但頁面快取正文曾顯示 2026-04-25，版本日期衝突。故該指南僅作社群線索，不升級為官方證據。
- 新增 Bistro 候選：Beef Wellington、Garlic Powder、Meat Sandwich、Apple Cider、Garlic Bread、Kombucha、Goulash（Meat + Wine + Ground Tomato）、Pumpkin Seeds 等。
- 官方 v1.1 確認修正 Goulash 與 Tomato Cocktail 的 cookbook 資料，但 changelog 沒有直接公開精確組合；Tomato Cocktail 配方仍待查。
- Rat Level 冷爐／熱爐配方必須以烤箱狀態作條件；Eggshell/Leaf 線索衝突保留待驗證。
- 詳細決策紀錄見 docs/WORK_JOURNAL.md；遊戲與專案時間線見 docs/PROJECT_TIMELINE.md。


## 13. 2026-11-16｜Goulash 與 Tomato Cocktail 交叉核對更新
- Steam 社群討論串「Assistance with Level 3」中，玩家先把 Goulash 誤報為 processed meat + tomato + wine，後續回覆更正：應為一般 Meat + processed Tomato/Ground Tomato + Wine；同一串另確認 Risotto = Rice + Mushroom + Cheese、Focaccia = Bread Dough + Olives + Olive Oil。ref：turn706207search7。
- Bistro 攻略搜尋索引明確列出 Tomato Cocktail = Olives + Wine + Ground Tomato；同一份索引也列出 Mushroom Soup = Mushroom + Garlic、Apple Mochi = Rice + Apple、Croque Monster = Bread + Cheese + Meat、Pumpkin Soup = Ground Pumpkin + Garlic、Tomato Juice = Tomato、White Wine = Wine + White Pencil、Pumpkin Bread = Pumpkin + Bread、Hamburger = Bread + Tomato + Ground Meat、Apple Sauce = Ground Apple、Olive Oil = Olive、Rosé = Wine + Pink Pencil、Vegan Sandwich = Bread + Pumpkin + Tomato、Pumpkin Fries = Pumpkin + Olive Oil、Meatloaf = Meat + Ground Meat、Pizza = Pizza Dough + Ground Tomato + Cheese、Italian Rice Balls = Cheese + Rice + Olive Oil、Schnitzel = Flour + Meat + Olive Oil、Meat Lover Pizza = Pizza + Meat + Salami。ref：turn706207search10。
- v1.1 官方 changelog 只確認修正 Goulash 與 Tomato Cocktail 的 cookbook 資料，並未列出配方；社群來源現在補足候選配方，但狀態仍應是 community-confirmed / pending in-game verification。ref：turn706207search1。
- 重要狀態更正：Goulash 的 Ground Tomato 是加工後番茄，不是 Ground Meat；Ground Meat 用於其他料理。Tomato Cocktail 同樣需要 Ground Tomato。


## 14. 2026-11-16｜新來源交叉核對與 Bistro 擴充
- 新找到 Pixel Questing 的 Student Dorm walkthrough 搜尋結果，摘要列出 Chapter 1 有 48 good recipes、29 bad recipes；但頁面本次無法直接開啟（cache miss），因此數量只作待核實線索。ref：turn798867search0。
- Steam 社群最新 Bistro Guide（Guide ID 3764982550）提供另一份較完整的配方表，明確列出 Goulash = Meat + Ground Tomato + Wine、Tomato Cocktail = Ground Tomato + Olives + Wine、Focaccia = Bread Dough + Olive Oil + Olives，並補入多筆 Bistro 食譜。ref：turn970635search2。
- 這份 Bistro Guide 同時提供 Bad Recipes 線索：Endless Possibilities（空鍋）、Fungus、Pink Pencil、Yeast Monster、Cookbook、Ghost、Wine Glass、Toothpick、Corkscrew、Table Cloth、Scissors（空 Mixer）、Red 40、Compass、Bad Pastry、Cheese Cloth、Sketchbook、Bad Meatloaf、Pumpkin Friend、Food Sketch、Cheese Grater、Jack O Lantern、Origami、Barely Edible、Paper Snowflake、Fried Balls、Drum Sticks、Definitely Not Wine、Paper Towel、Instant Calories、Pencil Sharpener、Oil Paint。
- 注意同一指南部分條目有拼字、用料與其他指南不一致（例如 Tomato Cheese Appetizer 是否需 Olives、Apple Mochi 是否使用 Ground Rice、Hamburger 是否使用 Ground Beef），因此配方要保留來源欄，不可直接視為全部定案。
- 9Puz 2026-09-02 完成路線指南詳細說明 Rat Level 的反重力／密碼／冷熱爐順序，以及 Eggshell/Leaf 第五項衝突；並整理 26 成就的觸發位置。ref：turn970635search0。
- 9Puz 指南特別強調「狀態視為材料」：例如 Bread / Toast / Burnt Toast / Soggy Toast、Coffee Beans / Filled Espresso Cup、整顆食材 / Mixer 輸出、Rat Level 冷爐 / 熱爐結果都要分開記錄。ref：turn970635search0。
- 新增來源：Steam v1.1 changelog（SteamDB mirror）確認 2026-09-11 修正 Goulash 與 Tomato Cocktail cookbook entries；沒有列出配方細節。ref：turn798867search15。
- 新增流程線索：Bistro 的剪刀可透過把 Mixer jar 放入 pot 取得；剪刀靠近植物葉片可找到 Blender switch。ref：turn970635search2。


## 15. 2026-11-16｜Cafe Job 與 Student Dorm 全量攻略線索補充
- Steam Guide ID 3713640352 的搜尋索引目前可取得完整更新版（索引標示 2026-08-10），包含 Chapter 1、2、3、4 的完整清單；但直接開啟頁面時會顯示舊版快取，需保留此版本不一致註記。refs：turn191035search0、turn191035search1。
- Chapter 2 Cafe Job 新版攻略補充重要前置：Paper Cup = Paper + Cup；Strawberry Cake = Cake + Strawberry；Chocolate Cake = Cake + Chocolate；Panini = Dough；Photo 需點擊牆上相框使照片掉落；Cheese 給藍色 kettle 的老鼠後，紙片自動放到電話，依便利貼號碼撥號解鎖 Avocado 與 Lettuce。
- Tiramisu 新版配方為 Cake + Filled Coffee Cup + Milk，並明確提醒要用已裝咖啡的杯子，不是 Coffee Beans。Double Espresso 需將已裝滿的杯子留在機器內，等咖啡豆補充後再次操作。
- 新版另列 Canned Coffee = Coin + Cup of Espresso；Mocha = Espresso Shot + Kakao + Milk；Strawberry Latte = Espresso Shot + Milk + Strawberry；Dirty Chai Latte = Tea + Milk + Coffee。這些與舊版文字有差異，保留版本證據。
- Chapter 2 Good Recipes 清單涵蓋 Tea、Savory Panini、Chocolate Spread、Marble Cake、Avocado Brownies、Cafe au Lait、Cronut、Tiramisu、Jelly Filled Donut、Espresso Shot、Babyccino、Berry Tea、Black Coffee、Chocolate Covered Strawberries、Mug Cake、Jam、Latte、Cupcake、Grilled Lettuce、Neapolitan Cake、Salad、Mug Bread、Green Smoothie、Strawberry Cake Parfait、Mocha、Pink Donut、Brownies、Victoria Sponge Cake、Mozzarella、Chocolate Donut、Cheese and Berries、Cake Pop、Chai Latte、Guacamole、Strawberry Cheesecake、Pain Au Chocolat、Canned Bread、Hot Cocoa、Crouton、Sweet Croissant、Tea Donut、Avocado Milk、Chocolate Cheesecake、Milk Bread、Bento Box、Savory Croissant、Strawberry Milkshake、Oven Cheese、To Go Drink、Dirty Chai Latte、Sweet Panini、Strawberry Latte、Cheese Bun、Coffee Cake、Panini、Sweet Bagel、Strawberry Cake、Choco Chai Latte、Tea Cake、To Go Box、Chocolate Bomb、Double Espresso、Choco Berry Donut、Cheesecake、Cake Donut、Savory Bagel、Fusion Tea、Strawberry Tiramisu、Tres Leches、Canned Coffee。
- Chapter 2 Bad Recipes 新版清單包含 Security Card、Healthy Cake、Drawing、Paper Cup、Breadception、Thermos、Don't Donut、Edible Money、Painted Mug、Paper Plane、Dollar、Paper Cup Phone、Menu、Is It Cake、Ew Panini、Healthy Donut、Mug Boy、Paper Trash、Painting、Food Drawing、Tea Strainer、Cups Game、Chocolate Coins、Mended Mug、Poison、Strawberry Horror、Counterfeit Money、Heart Attack、Disaster Dish、Hot Air、Terrible Spread、Specialty Espresso、Flavored Coffee、Cup Tower、Bad Milkshake、Awful Tea、Flat Croissant、Terrible Bagel、Spilled Coffee、Void Bagel。
- Student Dorm 新版補充 Tomato/Egg Stir Fry = Can of Tomatoes + Egg。
- 注意 Chapter 2 的同名材料與加工物件不可混為一談：Coffee Beans、Espresso Shot、Filled Coffee Cup、Cup of Espresso 需分別建檔；Paper、Paper Cup、Cup of Espresso 亦是不同物件。
- Treyex 2026-04-27 的早期攻略提供 Chapter 1 與 Chapter 2 的另一份交叉線索，但內容較早、較簡化，不能覆蓋 8/10 更新版。ref：turn603364search0。


## 16. 2026-11-16｜Rat Level 完整配方線索與成就細節
- 2026-08-10 Steam Guide 搜尋索引補出 Rat Level (Chapter 4) Good Recipes：冷爐 Cheese、Cheese+Cheese、Cheese+Paper、Cheese+Pencil、Cheese+Eggshell；熱爐 Cheese、Cheese+Cheese、Cheese+Paper、Cheese+Pencil。ref：turn523039search0。
- 同一來源列出 Bad Recipes：空爐（冷或熱皆可）、Leaf、Paperclip+Paper、Egg+Pencil、Leaf+Pencil、Paperclip+Pasta（Pasta 來自項鍊）、Eggshell+Paper、Paperclip、Paper、Eggshell、Pencil、Pencil+Paper。Eggshell 需反覆點擊 Egg 使其裂開後取得。ref：turn523039search0。
- 9Puz 2026-09-02 指南補充：Rat Level 反重力與密碼操作順序；冷熱狀態作為配方條件；Eggshell / Leaf 第五個冷爐圖示存在來源衝突，建議以即時 cookbook slot 是否更新作驗證。ref：turn970635search0。
- Rat Level 的成就 Coioioin：點擊烤箱旁的硬幣，直到連續三次落在相同面；Little Rat：完成 Rat Level 100%。ref：turn523039search0。
- Bistro 指南可直接開啟正文（Steam Guide 3764982550），其 Good Recipes 76 條（逐行清單）與 Bad Recipes 31 條，並有留言補充 Crazy Calzone、Breadless Burger、Vampire Defense Kit、Bread and Wine、Sorrow Sandwich、Risky Rice Pudding。ref：turn851401view0。
- Bistro 指南作者留言確認 Goulash 需要 Ground Tomato。ref：turn851401view0（lines 293-297）；食譜清單亦列 Tomato Cocktail = Ground Tomato + Olives + Wine、Focaccia = Bread Dough + Olive Oil + Olives。ref：turn851401view0（lines 117-153）。
- 需要避免錯誤：該 Bistro 指南把 Tomato Cheese Appetizer 寫 Tomato + Cheese，另一份更新版攻略寫 Tomato + Cheese + Olives；此配方保留衝突，不可硬定。
- Bistro 指南的 Apple Mochi = Ground Rice + Apple，但 8/10 更新版另一處寫 Rice + Apple；社群留言也指出需先磨碎 Rice。故候選以 Ground Rice + Apple 為較強版本線索，待實測。
- Bistro 指南將 Hamburger 列為 Ground Beef + Bread + Tomato；8/10 指南的 Hamburger 也列 Bread + Tomato + Ground Meat。這與部分普通 Meat / Ground Meat 分支必須分開記錄。


## 17. 2026-11-16｜Cafe 訂單、電話與安全箱流程補證
- Pixel Questing Chapter 2 搜尋索引提供 Cafe 食材清單、電話解鎖流程、訂單硬幣、Security Card、Safe 與 Void Bagel 步驟；原頁本輪無法直接開啟（cache miss），因此作為攻略線索。ref：turn810315search0。
- Cafe 缺少的食材清單會提示訂購 Avocado 與 Lettuce；老鼠交出的紙片補足電話號碼，攻略記載號碼 21931。這個數字屬於可變版本／攻略線索，正式資料庫不應硬編碼成跨版本常數，應記錄為場景 puzzle clue。
- 開發者在 Steam 討論中確認：牆上訂單紙會畫出需製作的料理；完成該料理即可得到 tip coin；完成一張訂單後可將紙條取下，過一段時間會出現新訂單。ref：turn810315search2。
- 開發者在 Steam 討論中確認 Safe 需要先製作 keycard；keycard 通常包含 photo 與 metal/computer chip。玩家攻略具體列為 Photo + Coin。ref：turn810315search4。
- Pixel Questing 攻略記載 Safe 在相框後方；先取得 Photo，再與 Coin 組成 Security Card，將卡片插入／刷過 Safe 卡槽開啟。Void Bagel 需 Bagel x3 放入 oven，之後可在 Safe 中取得。ref：turn810315search0。
- Café Update v3.0ea（2026-04-23）新增 Hint System、espresso machine、18 道 Café 食譜、rolling pin、三個 shelf、order tickets/tips、To Do「complete 8 orders」、25 個電話號碼等。ref：turn810315search5。
- 訂單系統除了賺 Coin，還有 8 orders 的 To Do 任務；需把「完成訂單數」與「累積 Coin」分開記錄。ref：turn810315search5。
- 2026-06-08 更新後，Student Dorm 和 Cafe 各新增一道食譜；Student Dorm 新增 Tomato/Egg Stir Fry。ref：turn798867search11。
- Cafe My Room 裝飾線索：咖啡廳杯中硬幣投入存錢筒；完成訂單取得硬幣；存入 20 枚後 My Room 出現畫筆，可調整牆紙、桌面木色、海報框。ref：turn810315search6。需進一步查證 20 枚是否為最終版本要求。
- 1.0 官方成就總數 26；官方 Steam 成就統計亦列出全部 26 名稱與描述。ref：turn648764search9。


## 18. 2026-11-16｜官方版本依賴鏈修正與 My Room 更新
- 官方 v5.1ea（2026-07-14）明確寫出：要進入 Level 3，必須先到 Level 2 完成 To-Do list；同時 Level 2 新增一項食譜。這比「只要把 Cafe 燒起來即可進 Bistro」更完整，後者只能視為必要互動之一，不可視為充分條件。ref：turn227999search0。
- v5.1ea 同時加入 fuse box hint、食譜書中的 Level 3 提示，並修正 ToDo 因交易老鼠而顯示 -1、老鼠任務重複啟動等問題。ref：turn227999search0。
- 目前解鎖規格應記錄：Level 2 完成 To-Do list → Level 3 可進入；To-Do 中可能包含訂單、老鼠交易、火警等項目，需依正式版實機／完整攻略核對清單。不要把「燒廚房」當作單一充分條件。
- 官方 v4.0ea My Room Update（2026-06-07）新增 Level 2 存錢筒，存入 20 coins 解鎖 Level 0 畫筆；可改 wallpaper、wood type、poster frames，並會保存自訂設定。新增書本排列成就、Level 1/2 完成獎盃、主選單 logo 成就、兩個菜單資料夾、新的 Level 1 Good dish；刪除 Cookie Jar、Pencils、Jelly Box，移除 Master Chef / Master of Disaster 成就。ref：turn302948search0。
- v4.1ea（2026-06-10）完成存錢筒後會出現 happy post-it；Coin 掉落後會重生；Canned Coffee 可用 coin 製作；修正多項提示。ref：turn227999search1。
- v5.4ea（2026-07-30）新增一鍵清除食譜書 new stars、Level 3 音效與更多食譜提示。ref：turn227999search1。
- 官方 1.0 公告（2026-08-26）確認 Level 1、2、3 都達到 100% 才會找到額外驚喜內容；Rat Level 是 1.0 後的第四個隱藏內容層，不是一般第四主廚房。ref：turn227999search1。
- v1.1（2026-09-11）修正 Coioioin、四個英文拼字、Level 1 重複 jar、食譜書 settings button、Goulash/Tomato Cocktail cookbook entries，並改善 Rat Level number lock 點擊區。ref：turn302948search14。
- 官方 1.0 後 Steam 語言列表只列 English、German、Simplified Chinese；沒有 Traditional Chinese。復刻的 zh-TW 是本專案新增在地化。ref：turn227999search2。


## 19. 2026-11-16｜Level 2 To-Do 清單與 Bistro 解鎖完整線索
- 日文玩家完整通關紀錄（2026-09-09）明確記載：Level 3 解鎖條件是完成 Level 2 所有 To-Do；實際流程先清理 Cafe、與抽油煙機內老鼠交易、完成國際料理／其他任務、製作 Burnt Panini 並再次烹煮引發火災、撲滅火災，最後完成剩餘訂單；返回 My Room 後收到遺產通知並解鎖 Bistro。ref：turn727664search0。
- Level 2 To-Do 項目可確定至少包含 Clean the kitchen、Trade with the rat、Complete 8 orders、Set the kitchen on fire；需保留「至少」標記，因攻略文字未以完整可複製清單呈現所有項目。refs：turn786170search0、turn727664search0。
- Cafe 火災流程：Panini 先進烤箱成 Burnt Panini，再把 Burnt Panini 再次烹煮引發火災；之後點擊警報玻璃三次打破，再按下露出的按鈕撲滅。refs：turn523039search0、turn727664search0。
- Bistro rat 在抽油煙機內；先給 Cheese，之後每次老鼠出示畫有料理的便條，完成該料理即可換取新食材；日文攻略指出最初 Cheese 交易會解鎖 Tomato，後續逐步解鎖 Apple、Olive、Garlic 等。refs：turn727664search0、turn798867search8。
- 七國料理／磁鐵：完成 7 種國際料理後磁鐵會貼在抽油煙機上，取得 Going Global。具體每個國家料理和食譜對應仍需逐項整理，不能只把七個磁鐵當成純裝飾。ref：turn727664search0。
- Mixer 是 Bistro 的重要工具，需修復右側花盆中的 electrical panel 才能使用；將 Apple 放入會變成 Crushed Apple，煮出 Apple Sauce；整顆 Apple 則可做 Baked Apple。Mixer 超載／失控可取得 Messing Around。ref：turn727664search0。
- Pizza Dough 由三種材料組成；Wine 有五瓶，其中四種由 Wine + 顏色製作，五瓶需按標籤順序排列取得 Wine About It。ref：turn727664search0。
- Level 2 的 25 個電話號碼是 Café Update 新增內容；日文玩家記錄逐一撥打後，多數為聲音／語音彩蛋，666 也有特別效果。需建立 PhoneEasterEggs 資料表，但不應影響主線電話解鎖。ref：turn786170search0。
- Cafe Update 另有 To-Do「完成 8 張訂單」；官方 3.0ea 公告確認。ref：turn810315search5。


## 20. 2026-11-16｜物理互動、輸入方式與七國料理待查
- 官方 Steam 商店描述明確定義核心互動：drag、toss、combine、gently place ingredients into pots/ovens/pans；所有物件都有 weight、motion、personality，並可 throw、mix、match、break。ref：turn832030search0。
- 官方新聞稿補充：三個廚房各自是 puzzle sandbox；每個 cabinet/shelf 都可能藏有食材；物件可以被拖曳、拋擲、放置，正確組合可解鎖 good/bad recipes。ref：turn832030search3。
- SteamDB 功能列表顯示 Mouse Only Option、Touch Only Option；本專案的手機橫向操作不是憑空擴充，原作已有觸控操作支援。ref：turn227999search2。
- Student Dorm 的物理／環境任務：水槽可持續放水使廚房淹水約半個房間；香蕉需在空中被切開取得 Fruit Samurai；物件需拋到螢幕上方取得 To Infinity；茶盒可旋轉／排列對齊。refs：turn832030search11、turn970635search0。
- Bistro 七國料理的確切七道菜名未能從文字來源完整確認。日文玩家通關紀錄只明確舉出 Mochi 作為日本料理，並說有七國料理、製作後磁鐵會貼在抽油煙機；不可擅自把七個看似異國料理的菜名當成官方七國清單。ref：turn672179search0。
- 官方 store listing 只保證 over 300 recipes，不保證每個攻略清單的計數完全一致；資料庫需按遊戲實際 cookbook 記錄，而不是只採用指南合計。ref：turn832030search0。
- 復刻物理模組應先定義可觀察行為與驗收，不虛構原作數值：pointer/touch grab、drag joint、release impulse、collision、stacking、breakable objects、water buoyancy、container insertion、cutting action、machine processing。所有係數留在本專案可調參數中，並標註為復刻設計值而非原作反編譯值。


## 21. 2026-11-16｜Student Dorm 1.0 路線與 To-Do 詳細補充
- Pixel Questing 2026-10-09 Chapter 1 guide明列 Student Dorm 有 48 Good / 29 Bad，並提供完整 24 項場景物件清單、48 Good、29 Bad 與 To-Do。ref：turn673517search0。
- Shane locker 解鎖：粉紅便條提示 D,2；杯子上方磁磚有 1 B C [空格] E；盆栽後方顯示 3；反覆點擊 D2 磁磚取得 key，拖到 Shane 紅鎖，解鎖 Cheese 與 canned tomato。其餘三個 locker 亦需打開。
- Student Dorm To-Do 至少 6 項：①使用 Ramen/Pasta 作材料完成 8 道 pasta dishes；②借用 Shane's Cheese（開鎖後製作一道含 cheese 的 good dish）；③播放所有磁帶（red、green、合成 Remix 後也要播放）；④Make Coffee（洗碗、放好餐具、發現 coffee maker、放上 gas stove）；⑤Water the basil（濕海綿碰枯萎 basil）；⑥Cook new dishes（累積 40 道 good + bad）。完成所有 Good Recipes 與 To-Do 才解鎖 Chapter 2；攻略作者表示 Bad Recipes 似乎可選，但未有官方證實。ref：turn673517search0。
- Student Dorm 新版配方差異：Beans on Toast = Beans + Toast；French Toast 可用 Toast 或 Bread + Milk + Egg；Savory Sandwich 可用 Bread + Egg 或 Bread + Cheese + Tomato；Tomato Soup = Tomato + Toast；Pasta A La Carbonara = Pasta + Egg + Milk；PB&J Sandwich 可用 Peanut Butter + Jam + Bread / Toast 或 PB&J jar + Bread；Smoothie = Strawberry Jam + Banana + Milk；Tomato Egg Stir Fry = Tomato + Egg。ref：turn673517search0。
- Student Dorm 食材／互動物件共 24 項：Banana、Pasta、Strawberry Jam、Coffee Maker、Peanut Butter、Canned Beans、Cassette Player、PBJ jar（合成後生成）、Toaster、Milk、Bread、Potatoes、Eggs、Protein Powder、Pink Glass Jar、Ramen、Canned Tomato、Cheese、three kitchen knives、Sponge、Orange Glass Jar、Green Glass Jar、Potted Basil、Cooking Pot。ref：turn673517search0。
- 9Puz 1.0 completion guide強調各房間各自有 recipe/task ledger；100% 不等於只完成配方。Room achievements、main menu、credits 都是獨立。ref：turn673517search1。


## 22. 2026-11-16｜Cafe Job 1.0 完整攻略與配方總量
- Pixel Questing 2026-11-09 Chapter 2 guide明列 71 Good / 41 Bad，共 112 條；場景物件 37 項（含合成後產生物件與 missing ingredient checklist 的隱藏解鎖項）。ref：turn513227search0。
- 這份指南列出 71 Good、41 Bad；Good 清單中 Coffee Cake 重複列兩次，因此原始逐條列舉 72 行但去重後為 71 種名稱。這個重複是指南本身的重複列，不可變成兩個 recipe ID。
- Cafe 物件包含 Espresso Machine、Dough、Orders、Tip Jar、Microwave Oven、Missing Ingredients Checklist、Telephone、Fire Alarm button、Lettuce、Cheese、Avocado、Paper、Milk、Chalks、Mouse Mug、Small White Cup、Paper Cup、Green Mug、Plain Cake、Strawberry Cake、Chocolate Cake、Croissants、Bagels、Paninis、Chalkboard、Strawberries、Paper Cups、Chocolate Syrup、Berry Jam、Photoframe、Blue Teapot、Strawberry Tea Leaves、Tea Leaves、Coffee Beans、Kakao、Piggy Bank、Metal Lid。
- 這份 11/9 指南提供的部分配方與 8/10 Steam Guide 有衝突：Tiramisu = Cheese + Plain Cake + Coffee Beans；Babycino = Espresso Shot + Milk 或單獨 Milk；Hot Cocoa = Espresso Shot + Milk + Kakao；Latte = Espresso Shot + Milk；Canned Coffee = Metal Lid + Coffee Beans；Dirty Chai Latte = Espresso Shot + Tea Leaves + Milk；To Go Drink = Paper Cup + Kakao；Bento Box = Metal Lid + Avocado。需逐項保留為新候選，不可直接覆蓋 8/10 指南與官方更新。
- 11/9 guide的 Cafe 41 Bad list包含 Paper Cup、Terrible Bagel、Ew Panini、Is It Cake、Spilled Coffee、Mug Boy、Bad Milkshake、Specialty Espresso、Flavored Coffee、Flat Croissant、Terrible Spread、Cup Tower、Disaster Dish、Don't Donut、Painting、Painted Mug、Awful Tea、Hot Air、Paper Plane、Menu、Dollar、Healthy Cake、Food Drawing、Thermos、Breadception、Paper Cup Phone、Healthy Donut、Tea Strainer、Cups Game、Chocolate Coins、Mended Mug、Poison、Strawberry Horror、Counterfeit Money、Heart Attack、Drawing、Edible Money、Paper Trash、Security Card、Burnt Panini、Void Bagel。
- Pixel Questing 11/9 guide說明：缺料 checklist 位於 microwave 左側；老鼠由 Blue Teapot 出現，給 Cheese 取得 torn paper；號碼 21931；撥號後必須拿起 handset 完成通話才會訂購 Avocado/Lettuce（開發者於 8/19 Steam討論確認）。refs：turn513227search0、turn408211search6。
- Cafe order slips 在 microwave 右側，以圖像顯示料理；製作對應料理完成訂單取得 Coin；Coin 可解鎖部分 Bad Recipes。ref：turn513227search0。
- Cafe v3.0ea 新增一項 To-Do「complete 8 orders」（完成8張訂單）、18道食譜、espresso machine、25個電話號碼、訂單與tip coins；日文玩家確認25號碼逐一撥打後多為音效／語音彩蛋。refs：turn810315search5、turn194117search0。
- 11/9指南的 Tiramisu、Canned Coffee 等配方與官方後續更新不一致，官方 v4.1ea 明確允許 Canned Coffee 用 Coin；8/10 guide和9/2 9Puz更支持 Espresso cup 狀態。release 資料優先保留 8/10 + official patch evidence，11/9 guide作為衝突候選。refs：turn227999search1、turn302948search14、turn749693search1。


## 23. 2026-11-16｜Cafe To-Do 數量語意校正
- 官方 v3.0ea 公告原文是單數「New Todo: complete 8 orders」，明確表示一項 To-Do 目標是完成 8 張訂單；不是已證明有 8 個獨立 To-Do 條目。ref：turn545252search0。
- 日文玩家把同一更新描述為「ToDoリスト、8件追加」，語意可能是 To-Do 內新增 8 個訂單計數／條目，與官方 patch note不完全一致。ref：turn194117search0。
- 1.0解鎖 Bistro 的 Level 2 To-Do 至少包括 Clean the kitchen、Trade with the rat、Set the kitchen on fire、完成訂單；其中「完成訂單」可能對應 v3.0ea 的 8 orders 任務，但完整清單與任務數仍未被可讀文字來源確認。ref：turn727664search0。
- 因此文件中不再把「8 To-Do entries」當作確定事實；需拆分為 order_completion_target = 8 與 level2_todo_task_count = unknown。


## 24. 2026-11-16｜Rat Level 設備名稱與電力狀態修正
- 2026-09-10 日文玩家完整成就攻略明確描述 Rat Level 的設備是「通電的罐頭」式調理器，近似微波爐；解開酒瓶機關後，可切換電力輸出「強／弱」，同一組材料會因電力強弱產生不同結果。ref：turn680263search4、turn680263search6。
- 因此前文「cold/hot oven」應視為攻略用語簡化；正式復刻規格改用 appliance = ElectricCanCooker，power_level = low | high。RecipeCondition 不應使用一般 oven temperature。
- 更新版 Steam Guide將九項 Good Recipes分為 OFF（5項）與 ON（4項），可對應 low/high電力狀態，但仍需以遊戲畫面與機器指示燈核對 low/high的映射。ref：turn970896search1。
- Rat Level 目前可確定的 puzzle chain：點擊畫面／圖片顯示 anti-gravity switch → 啟動後物件浮起並露出花盆內 note → 點擊酒瓶 label使其掀起並露出 keypad → 輸入 note提示的三位數 → 解鎖 cooker power control。確切三位數字未在可讀文字來源中披露，必須由 note 圖片／遊戲內實際畫面取得；不要猜碼。ref：turn970896search1。
- Recipe matrix應以 power_level 分別記錄 low/high；bad recipes亦需標記電力狀態，空設備在任一狀態均可測試。Eggshell / Leaf的冷爐圖示衝突仍保留。ref：turn970896search1。


## 25. 2026-11-16｜Bistro 1.0 新增食譜與 Coioioin 真正觸發方式
- 日文玩家 2026-09-10 的 1.0 全成就通關記錄指出：正式版 Bistro 追加食譜合計約 10 項；最後一項 Good Recipe 是 Mini Pizzas，最後一項 Bad Recipe 是 Clutter。此數量是玩家通關觀察，仍需對照遊戲內 cookbook counter。ref：turn384561search0。
- 8/10 Steam Guide 的 8/27 新增項目列出 7 Good：Boiled Rice、Roasted Mushrooms、Shredded Cheese、Meat Skewers、Leftover Pizza、Minced Garlic、Mini Pizzas；以及 2 Bad：Big Magnet、Boo Tomato。9/10 玩家通關另確認 Clutter，推測為第三個新增 Bad Recipe。refs：turn970896search1、turn384561search0。
- Clutter 描述為「有時東西會自己變得凌亂」；可能與 Mixer mess／Messing Around有關，但目前沒有可讀來源明確說明輸入條件。記錄為 candidate，不要硬寫成 mixer recipe。
- Coioioin主要規格依Steam官方成就文字：同一面連續三次。Steam guide與9Puz均描述點擊爐旁硬幣反覆嘗試即可。另有藍開關／紅框投擲區說法，但目前缺乏交叉支持，不要當成必要前置。ref：turn982769search1、turn208555search0、turn982769search2。
- 同一攻略指出遊戲內取得 Coioioin 後，部分玩家需關閉並重新啟動遊戲，Steam achievement才會同步；此為 Steam同步 bug 線索，不是遊戲內解鎖條件。ref：turn384561search1。
- 1.0 通關後 My Room 出現生日蛋糕與媽媽的信；蛋糕可互動點亮／吹熄蠟燭。此為主線完成後的 hub內容，需存檔並保留 candle state。ref：turn384561search1。
- Level 2 To-Do 的 Set the kitchen on fire 在 1.0 玩家記錄中可能出現完成但未顯示的 bug；玩家再次點火後才更新。應把 task state與Steam achievement state分開，並設計重試／同步機制。ref：turn384561search1。


## 26. 2026-11-16｜Bistro 食譜總量分期重算（重要）
- 直接開啟的 7/14 Bistro Guide正文可逐行核算為 76 Good / 31 Bad；這是 Bistro 初始 EA guide baseline，不應當成 1.0 最終數量。ref：turn349496view0（Good lines 91-166；Bad lines 170-200）。
- 8/10更新版 Steam Guide在「New Recipes as of 08/27/2026」列出 7 Good：Boiled Rice、Roasted Mushrooms、Shredded Cheese、Meat Skewers、Leftover Pizza、Minced Garlic、Mini Pizzas；另列 2 Bad：Big Magnet、Boo Tomato。ref：turn970896search1。
- 9/10正式版玩家通關報告指出 Bistro追加食譜約 10 項，最後 Good為 Mini Pizzas、最後 Bad為 Clutter。將 Clutter視為第三個新增 Bad候選。ref：turn384561search0。
- 因此目前最合理的 1.0候選總量是 **83 Good / 34 Bad（117 total）**，由 76/31 baseline + 7/2 於 8/27新增 + Clutter 1項推導。這是跨來源推算，必須以 1.0遊戲內 cookbook counter核對，不能標為官方確定數字。
- 這個分期模型能解釋 7/14指南沒有 Big Magnet、Boo Tomato、Clutter，而 8/27後的指南與 9/10玩家通關紀錄有新增內容；後續 recipe DB必須保留 introduced_version / source_date。


## 27. 2026-11-16｜Bistro Rat Trade 任務鏈與 Going Global 證據
- 開發者 2026-07-16 直接回覆：Bistro rat在抽油煙機上方的可疑門後；先用 Level 2 Cafe 的交易物 Cheese啟動任務；之後老鼠會展示一道料理的圖畫，製作該料理即可換取一項新食材。ref：turn489309search0。
- 日文玩家 2026-09-09 實際紀錄：首次給 Cheese後取得 Tomato；後續抽油煙機會出現圖畫便條，製作圖示料理可逐次取得新食材。ref：turn974375search1。
- 9Puz 1.0路線確認老鼠贈品支線包含 Apple、Olive、Garlic；缺少這些物件時，先解交易鏈，不要誤判成食譜公式錯誤。ref：turn974375search0。
- 日文玩家明確指出 Bistro有 7個國家的料理，製作後磁鐵會貼在抽油煙機；日本料理例子是 Mochi。完成全部七道料理取得 Going Global。其餘六道的國家／料理名稱目前沒有可靠文字來源，不能用「看起來像異國料理」自行湊滿。ref：turn489309search1。
- Steam玩家討論顯示老鼠在所有請求完成後會展示愛心圖示；開發者／玩家確認這是感謝訊息，代表不再需要提供額外料理，不是新的 Meat Lover Pizza request。ref：turn489309search3。
- Bistro rat trade應建模為有序任務狀態：hidden_door_found → cheese_offered → first_reward_tomato → request_note_shown → requested_recipe_made → ingredient_reward → repeat_until_heart_note → best_friends_unlocked。七國磁鐵另外用 magnet_collection_count 0..7記錄。


## 28. 2026-11-16｜zh-TW 在地化詞典第一版
- 新增 docs/ZH_TW_GLOSSARY.md，確立台灣用語：起司、馬鈴薯、可頌、吐司、披薩、果昔、調理機；Good/Bad Recipes暫定「美味料理／怪奇料理」。
- 官方 Steam Traditional Chinese頁面明確顯示「不支援繁體中文」，現有官方語言只有 English、German、Simplified Chinese；本專案 zh-TW屬新增在地化。ref：turn420164search5。
- 使用者要求台灣繁體中文，因此不直接沿用簡體攻略的「芝士、土豆、牛角包、耗子」等詞。
- 料理專名第一版候選：Focaccia=佛卡夏、Goulash=古拉什（匈牙利燉肉）、Croque Monsieur=法式熱三明治、Schnitzel=炸肉排、Mochi=日式麻糬、Kombucha=康普茶。
- 目前 glossary只涵蓋已整理的主要 UI、食材、Student Dorm/Cafe/Bistro recipe與成就；仍需補齊所有 Bad Recipes、Rat Level描述、My Room物件、道具與劇情文本。


## 29. 2026-11-16｜Wine About It 與 Rat Level slot 的可操作驗證
- Steam玩家在 Level 3 討論中指出 Wine About It 的五瓶酒排序依「瓶身標籤高度由短到長」排列，不是依酒色或名稱猜測。ref：turn241221search6。
- 這可轉成穩定的 puzzle rule：取得五瓶酒後，依 label_height ascending 排列；實際五瓶的順序仍需以遊戲畫面確認。
- 1.0簡體中文成就攻略列 Rat Level冷爐第五個 Good slot為 Cheese + Leaf；8/10英文攻略列 Cheese + Eggshell；需保留 live slot測試分支。ref：turn553799search0、turn839723search0。
- 同一中文攻略列 Rat Level Bad slot：Eggshell + Pencil、Pasta單獨、Pasta + Paper；英文攻略列 Egg + Pencil、Paperclip + Pasta。這些差異需逐項測試，不可合併為同一 recipe。
- Coioioin：9/10玩家說先按藍色開關再拋紅色區域硬幣；8/10指南與舊攻略只說連續三次同面，故機關觸發為較新的 1.0 evidence。ref：turn384561search1。


## 30. 2026-11-16｜全關卡 recipe inventory 第一版
- 新增 docs/RECIPE_INVENTORY.md，統一記錄各房間候選配方名稱與數量。
- 目前候選總量：Student Dorm 48 Good / 29 Bad；Cafe 71 / 41；Bistro 83 / 34（由 76/31 EA baseline + 7/2新配方 + Clutter推算）；Rat Level 9 Good / 12 Bad slot。
- 合計 211 Good + 116 Bad = 327 candidate entries，與官方商店「over 300 recipes」相符，但這只是來源交叉推算，不是遊戲內 cookbook counter驗證。
- Cafe 來源的 Good list將 Coffee Cake重複列兩次；inventory去重為一個 recipe ID，保留來源報告的71總數。
- 下一步不是再增加一份散文清單，而是逐筆補齊 formula、processed state、appliance、source、confidence、verification status與zh-TW。


## 31. 2026-11-16｜Student Dorm / Cafe formula matrix 第一版
- 新增 docs/RECIPE_FORMULA_DRAFT.md，將 Student Dorm 48 Good + 29 Bad、Cafe 71 Good + 41 Bad逐筆整理為候選公式／動作。
- 其中已標出關鍵狀態與設備：Toast/Burnt Toast/Soggy Toast、Coffee Beans/Espresso Shot/Filled Coffee Cup/Cup of Espresso、Microwave Oven與 Espresso Machine。
- 來源衝突直接在 formula draft標記，並連結 docs/RECIPE_CONFLICTS.md；未驗證配方不能當正式資料。
- 下一階段將同樣方式整理 Bistro 83/34候選與 Rat Level 9/12 slots，再轉成結構化 recipe records。


## 32. 2026-11-16｜Bistro / Rat Level formula matrix 第一版
- 新增 docs/RECIPE_FORMULA_BISTRO_RAT.md，整理 Bistro 83 Good / 34 Bad候選與 Rat Level 9 Good / 12 Bad slots。
- Bistro formula draft涵蓋 76/31 EA baseline、8/27新增 7 Good + 2 Bad，以及 1.0 Clutter候選。
- Rat Level用 Electric Can Cooker與 power_level low/high建模；Eggshell/Leaf、Egg/Pencil、Pasta相關 slot仍標註衝突。
- 目前四個房間都有候選名稱清單與部分公式矩陣；下一步需補每筆 recipe的 source IDs、version、confidence與 verification status。


## 33. 2026-11-16｜官方 v2.9 配方調整補證
- 官方 v2.9ea（2026-03-19）移除重複的其中一個 Chocolate Spread，避免兩個同名材料混淆。
- 官方 v2.9ea允許 Tiramisu更多配方：Cake + Coffee + Dough，或 Cake + Coffee + Milk；應記為當時版本的兩種有效組合。
- 官方 v2.9ea另新增 Savory Sandwich配方 Bread + Cheese + Tomato Sauce。
- 這些是 Early Access版本的官方變更，必須保留 version range；不能直接覆蓋 1.0候選配方。
- ref：turn521540search2。


## 34. 2026-11-16｜料理設備共通互動規則
- Pixel Questing Chapter 1 guide明確寫出：最多拖入三種材料到烹調設備，再點擊設備執行料理；Chapter 1使用 Cooking Pot，Chapter 2使用 Microwave Oven。ref：turn420164search4。
- 這是目前最清楚的通用 recipe interaction規則：ingredient_count 1..3，drop into appliance → activate/click appliance → evaluate recipe conditions → produce output / update cookbook。
- 章節設備候選：Student Dorm = Cooking Pot（另有 Toaster、Coffee Maker）；Cafe = Microwave Oven（另有 Espresso Machine）；Bistro = Cooking Pot + Mixer；Rat Level = Electric Can Cooker（低／高電力）。
- 不是所有可移動物件都是食材；道具、紙張、餐具、工具、磁鐵、鑰匙等也可被投入設備或組合成 Bad Recipes。
- 料理設備不能共用一個無條件的 recipe evaluator；同一材料組合需同時檢查 chapter、appliance、item state、power/temperature、recipe version。
- 目前尚未找到官方明確說明材料是否每次都被消耗、是否可在設備中保留、配方輸入順序是否完全不影響結果；這些列為實機測試項，不先寫死。


## 35. 2026-11-16｜互動／物理規格第一版
- 新增 docs/INTERACTION_SPEC.md，整合四房間互動鏈、桌面／觸控輸入、物件分類、加工狀態、設備條件與 QA acceptance tests。
- 明確區分 observed evidence與 implementation choice；沒有公開的原作物理係數不會被假裝成已知。
- 目前可驗收的互動包含 drag/toss/gentle place、最多三材料設備操作、切割、淹水、澆水、整理、調理機加工、訂單、電話、保險箱、鼠鼠交易、酒瓶排序與 Rat Level power states。
- 仍待確認：材料消耗、輸入順序、設備暫存、精確 Rat code、save是否保存物件位置。


## 36. 2026-11-16｜QA acceptance test plan 第一版
- 新增 docs/QA_TEST_PLAN.md，涵蓋 Recipe Engine、物理互動、Student Dorm、Cafe、Bistro、Rat Level、My Room、26成就、zh-TW、桌面／手機橫向與存檔。
- QA test cases已把未解資料轉成明確 blocker：Cafe To-Do完整清單、七國料理與rat reward順序、Rat Level密碼／power mapping、D級配方衝突、327候選數量核對。
- QA計畫目前是 test design，不是已通過測試；實作前仍需完成研究資料與 Critic review。


## 37. 2026-11-16｜Rat Level 材料數上限例外
- 1.0日文玩家完整成就攻略明確說明 Rat Level每次只使用兩種材料；其 cooker是通電罐頭，電力強弱改變結果。ref：turn908932search5。
- 因此主廚房通用最多三種材料的規則不能套用 Rat Level；Rat Level Electric Can Cooker需設 max_inputs = 2。


## 38. 2026-11-16｜來源登錄表與證據層級
- 新增 docs/SOURCE_REGISTER.md，將官方公告、開發者回覆、攻略、玩家討論與台灣繁中術語來源編號 SRC-001..SRC-030。
- 已定義 evidence hierarchy：實機／官方／開發者 > 多來源玩家一致 > 單一攻略 > 舊版／衝突／推測。
- 搜尋摘要與無法直接開啟的頁面明確記錄限制；不把搜尋索引當作已完整讀取正文。
- 後續 recipe records需引用 SRC IDs，並標註 source date/version。


## 39. 2026-11-16｜Student Dorm / Cafe 配方再次校正
- 8/10 Steam recipe guide完整搜尋索引（目前原頁被移除）提供比 11/9 Pixel Questing更細的 Cafe formula set；已將公式草稿校正並把兩份來源差異加入 RECIPE_CONFLICTS。
- Developer直接確認 Smoothie包含 Peanut Butter；另一位 developer確認 Good Protein Shake = Milk + Peanut Butter + Protein Powder（不是 Egg）。refs：turn307019search0、turn307019search7。
- Cafe重要校正：Babyccino=Milk、Black Coffee=Coffee Beans、Latte=Milk+Coffee Beans、Hot Cocoa=Milk+Chocolate Spread、Avocado Milk=Avocado+Milk、Strawberry Cheesecake需第三個 Strawberry、Chocolate Bomb=Chocolate Spread+Kakao、Canned Bread=Bread+Lid。
- Student Dorm重要衝突：Smoothie（Peanut Butter vs Strawberry Jam）、Sweet Sandwich（Peanut Butter vs Strawberry Jam）、Carbonara（Cheese vs Milk）、Tomato Soup（Tomato vs Tomato+Toast）、Beans on Toast（Bread vs Toast）等。
- Steam Guide ID 3713640352已被移除公開頁面，搜尋索引仍保留內容；將其視為 cached community evidence，不當作可即時讀取的官方來源。
- 新增 SRC-031 Smoothie developer reply、SRC-032 Good Protein Shake developer reply；Source Register已更新。


## 40. 2026-11-16｜Peanut Butter 隱藏食材解鎖
- Developer於 Steam討論確認：主選單信件下方的按鈕會解鎖 Peanut Butter；不需要真的將遊戲加入願望清單。按下按鈕後 Peanut Butter會生成在場景中，且此解鎖會保存到 save file。ref：turn307019search7。
- 這個解鎖是 Student Dorm多道料理的前置：PB&J、Peanuts、Smoothie、Good Protein Shake等。
- 不要實作成 Steam Wishlist API；只需本地化的信件互動與永久 save flag。


## 41. 2026-11-16｜Item / ItemState inventory 第一版
- 新增 docs/ITEM_STATE_INVENTORY.md，按 Student Dorm、Cafe、Bistro、Rat Level分別列出已知物件、分類、zh-TW候選、狀態與能力。
- 明確拆開所有高風險狀態：Ground Tomato/Meat/Rice/Pumpkin/Apple、Minced Garlic、Shredded Cheese、Bread/Toast/Burnt/Soggy、Egg/Eggshell、Coffee Beans/Espresso/Filled Cup、Paper/Paper Cup/Photo、Rat power low/high。
- 尚待補完：Student Dorm其他三個locker內容、Cafe chalkboard/checklist等物件、材料消耗規則、物件位置是否存檔、Bistro/Rat Level全部物件能力。


## 42. 2026-11-16｜Student Dorm mouse hole 與成就位置修正
- 開發者確認 D2磁磚是 Shane locker key；右側另一個磁磚是 mouse hole，兩者不同。mouse hole與解鎖locker無關；解鎖後把 Cheese拿到洞口前即可取得 I Smell Cheese。refs：turn765577search4、turn765577search5。
- 開發者確認 A Lot to the Right的茶盒位於 Student Dorm上層架，Jam右側，為藤蔓圖案的堆疊盒子；需把圖案排列成連續圖樣。ref：turn765577search10。
- 9Puz完整成就表確認：Fair Trade在 Cafe（藍色茶壺旁的老鼠，給 Cheese）；What's The Emergency需撥 911並拿起電話；Aw That's Hot是 Panini烤焦後再烹煮；Nothing Nowhere是三個 Bagel一起烹煮，配方在 Safe開啟後取得。ref：turn765577search1。
- 9Puz與Steam指南補充 Messing Around：先研磨 Pumpkin/Tomato/Meat，再讓 Mixer第二次、第三次運作造成大混亂，之後可用 Cloth清理。ref：turn275853search2。
- Tea boxes位置與 D2/mouse hole分離已加入 Interaction Spec與 QA；避免把鼠洞當成 locker key tile。


## 43. 2026-11-16｜26項成就矩陣
- 新增 docs/ACHIEVEMENT_MATRIX.md，整理 1.0／v1.1的26項成就、所屬場景、觸發候選與證據信心。
- 已特別區分 I Smell Cheese（Student Dorm mouse hole）、Fair Trade（Cafe Blue Teapot rat）、Best Friends（Bistro rat trades）。
- Master of Disaster為早期EA成就，v4.0移除，不列入1.0的26項。
- 仍需確認：100%是否要求Good+Bad全配方、Bookworm書本排序、Going Global七道菜完整名單、Coioioin藍色開關與三次同面是否兼容。


## 44. 2026-11-16｜Student Dorm 六項 To-Do 完整查證與100%規則
- 9Puz 2026-09-02 1.0 completion route完整列出 Student Dorm六項 To-Do：
  1. 用 Pasta或Ramen作為材料完成8道料理。
  2. Borrow Shane's Cheese：D2拿key開locker，並用Cheese完成一道Good dish。
  3. Play All Cassettes：播放Red、Green，組合成Remix，再播放Remix。
  4. Make Coffee：清潔碗盤、收好餐具、顯示Coffee Maker、放上瓦斯爐沖煮。
  5. Water Basil：濕海綿澆水或開水龍頭。
  6. Cook New Dishes：累積完成40道Good + Bad料理。
- 9Puz明確說每個廚房各有自己的 recipe/task ledger，且Student Dorm below 100%需檢查Good與Bad兩個tab；Good+Bad recipes與全部To-Do都影響room completion。
- 因此修正先前錯誤：Clean Dishes是Make Coffee任務的前置，不是獨立To-Do；D2 key也不是獨立To-Do，而是Borrow Shane's Cheese任務的一部分。
- 9Puz另指出Flooded約淹到房間50%時會跳成就提示可關水；Bookworm是讓書背上的波浪圖案連成一條線。
- ref：turn973369search0、turn973369search2。


## 45. 2026-11-16｜Cafe To-Do已知項目整理
- **此處舊結論已被2026-11-17來源校正取代：** Clean the kitchen與Trade with the rat屬Bistro To-Do；Cafe可明確命名的To-Do為Complete 8 orders與Set the kitchen on fire。不要沿用「Cafe至少四項」的錯誤分類。
- 1.0 walkthrough另外指出 Cafe未達100%時需檢查電話stock/21931、訂單Coins、Espresso Cup、Safe與fire alarm；這些可能是任務子步驟或額外ledger rows，尚未證明是獨立To-Do。
- 因此不再稱 Cafe To-Do「完全未知」；目前為至少4項已知，完整總數仍待遊戲UI。


## 46. 2026-11-16｜Bistro 配方總量再校正：Crazy Calzone與五項Bad Recipes
- 發現 7/14 Bistro Guide的主清單並不完整；7/17 Steam玩家留言補出：
  - Good：Crazy Calzone = Pizza + Pizza Dough。
  - Bad：Breadless Burger = Ground Meat + Cheese + Tomato；Vampire Defense Kit = Garlic + Wooden Spoon（另有 Garlic + any Pencil衝突）；Bread and Wine = Wine + Bread；Sorrow Sandwich = Bread + Flour；Risky Rice Pudding = Rice + Flour。
- 因此7/14 guide list 76/31不能直接當成EA完整基線；修正為 77 Good / 36 Bad候選，再加 8/27的7 Good +2 Bad，以及Clutter 1 Bad。
- 最新 Bistro候選總量為 **84 Good / 39 Bad（123 total）**。
- 最新全遊戲候選總量為 **333筆：212 Good +121 Bad**（Student Dorm 48/29、Cafe 71/41、Bistro 84/39、Rat Level 9/12）。
- 333仍是多來源候選總量，尚未由1.0遊戲內 cookbook counter驗證。已更新 RECIPE_INVENTORY、RECIPE_FORMULA_BISTRO_RAT、README、PROGRESS_REPORT、PROGRESSION_MODEL與QA。
- refs：turn443888search0、turn443888search1、turn443888search2。


## 47. 2026-11-16｜312筆配方 zh-TW候選譯名
- 新增 docs/ZH_TW_RECIPE_TRANSLATIONS.md，涵蓋 Student Dorm 77、Cafe 112、Bistro 123，共312筆有名稱的配方。
- Rat Level另列9 Good +12 Bad共21個符號槽位，不自行替外星符號命名。
- 台灣繁中候選已完整覆蓋所有命名配方；雙關、罕見料理與部分壞料理仍標記暫定，最終需UI截圖與母語校對。


## 2026-11-17｜Coioioin 1.0 trigger conflict — supersedes earlier single-route notes
- Official Steam achievement text: same coin face lands three times in a row.
- Older Steam player guide/discussion: repeatedly click the coin beside the cooker until the achievement appears.
- Japanese 1.0 first-hand guide (2026-09-10) explicitly says the achievement is not simply random same-face repetition; press the switch in the blue frame, then throw the coin into the red frame. The author reports Steam unlock sync occurred only after closing and relaunching the game.
- Current decision: neither route is final. QA must test both; gameplay trigger and Steam synchronization are separate states. This section supersedes earlier handoff notes that dismissed the blue-switch route as low-confidence or made same-face repetition the only required trigger.
Source: https://note.com/utsukinoel/n/n2734d08070ca ; https://steamcommunity.com/stats/3376500/achievements ; https://steamcommunity.com/app/3376500/discussions/0/582806564883173701/


## 2026-11-17｜重要來源版本更正（supersedes SRC-017 references above）
- Steam Guide ID 3686619896 is **v4.0 EA**, posted 2026-03-17 and updated 2026-06-08. It explicitly says its recipes are based on v3.0 EA and its readable contents cover Student Dorm and Cafe only. It is not a 1.0 source and contains no Bistro/Rat Level section.
- Steam Guide ID 3713640352 search snippets expose later Aug 10 full-game content, but the directly opened removed PT-BR page still shows Apr 25 EA text. Later Bistro/Rat Level material is cached search-index evidence only.
- All claims formerly attributed to a “2026-09-01 Simplified Chinese 1.0 guide” are withdrawn unless independently supported elsewhere. In particular, do not use SRC-017 for Clutter, Rat Level Leaf/Eggshell conflicts, or Bistro recipes.


## 2026-11-17｜SRC-023版本範圍補充
- Japanese Level 3 article published Sep 9 explicitly states it covers the July 13 Early Access Level 3 update. Treat it as EA-era first-hand evidence, not a 1.0 guide solely because of its publication date.
- Its seven-country cuisine section names only Japan = Mochi. Keep the other six country-dish names unknown until an image or 1.0 gameplay source identifies them.


## 2026-11-17｜Critic 初審與研究 Gate 判定
- 本輪對照 README、Recipe Inventory、兩份配方草稿、Conflict Register、Item State Inventory、Interaction Spec、Progression Model、Achievement Matrix、zh-TW 字典、QA 與來源登錄。
- 結構盤點：候選食譜 333（212 Good + 121 Bad），其中命名食譜 312、Rat Level 符號槽位 21；成就矩陣 26 項；QA 表格 102 個唯一測試 ID（設計數，不代表已執行）。
- 發現並修正 README 的來源範圍仍寫 SRC-001…SRC-046；目前來源登錄至 SRC-051。修正 Cafe QA 編號 CAFE-027 為 CAF-017，使其與 CAF-001…CAF-016 命名一致。
- Bistro 配方交叉查核：Pizza Dough = Olive Oil + Yeast + Flour 在 7/14 Steam Bistro Guide 與 9/2 9Puz 1.0 route 一致；列 B 級候選，未宣稱實機驗證。Goulash 與 Tomato Cocktail 仍因 v1.1 官方修正未披露精確新配方而保留 blocker。
- 研究 Gate 尚未通過：七國菜完整名單／老鼠交易順序、Cafe完整To-Do、Rat Level三位數密碼與OFF/ON映射、333筆逐筆證據追溯、D級配方衝突、實機QA及繁中最後校對。
- 初審結論：沒有發現需要推翻整體資料模型的致命架構錯誤；但目前不符合「全內容忠實復刻」正式開發門檻。可以在 CEO 額外批准下先做不依賴未知內容的資料層／工具原型，但不得把這視為完整遊戲實作批准。依既定規則，仍維持 Research Only。


## 2026-11-17｜Critic補強：Bistro D級配方測試覆蓋
- 將配方衝突表中14項未充分覆蓋的 Bistro 候選變體轉成獨立QA：BIS-027至BIS-040。
- QA總數更新為116個唯一測試ID。這補足測試設計覆蓋，不代表已取得遊戲內答案。


## 2026-11-17｜重大來源更正：SRC-017實為v1.0混合版指南
- 重新從Steam遊戲指南索引點入SRC-017，確認頁面標題為v1.0全成就指南，更新日期2026-09-08。正文保留舊「v4.0 ea」章節，但後續明確有Bistro（家常小館）及Rat Level（耗子餐廳）內容。先前判定它不含Bistro/Rat Level是錯誤，已撤回。
- 這份指南的作者提醒前兩關未更新、手動配方可能錯誤；故Bistro/Rat Level資料列為1.0社群候選，不視為官方或實機驗證。
- 新增重要候選：Mochi=Ground Rice；Apple Mochi=Ground Rice+Apple；Goulash=Meat+Ground Tomato+Wine；Tomato Cocktail=Olives+Ground Tomato+Red Wine；Clutter=Cloth+Wooden Spoon。
- Rat Level候選修正：冷Good #5偏向Cheese+Leaf；Bad #4 Eggshell+Pencil；Bad #6 Pasta；Bad #7 Pasta+Paper。與SRC-050快取攻略衝突，必須在QA中保留對照。
- 新增配方衝突：Vampire Defense Kit（Tomato+Spoon vs Garlic+Spoon）、Bread Sticks（Pizza Dough vs Pizza Dough+Olive Oil）、Crazy Calzone（Pizza+Spoon vs Pizza+Pizza Dough）、Bad Pastry、Sorrow Sandwich、Risky Rice Pudding等。
- 因此Goulash/Tomato Cocktail不再列為完全無配方的P1 blocker；已取得1.0候選與圖鑑圖示錯誤線索，但v1.1後仍需回歸驗證。七國菜名及老鼠完整請求順序仍未解。


## 2026-11-17｜SRC-017 1.0指南重新分類後的 QA 對照
- QA新增RAT-016至RAT-019，以及BIS-041至BIS-047；與先前BIS-027至BIS-040一併納入後，QA共有140個唯一ID。
- README、Critic與進度報告已同步此數量。這些仍是測試設計，不是實際執行結果。


## 2026-11-17｜Critic Gate更新
- SRC-017恢復為有效的1.0 Bistro/Rat Level候選來源後，Goulash/Tomato Cocktail不再是「無配方」P1 blocker；v1.1+僅保留回歸驗證。
- Critic P1-06改為「核心QA尚未實際執行」：140個QA ID全部仍是設計，沒有本專案遊戲客戶端的pass/fail紀錄。


## 2026-11-17｜SRC-052 Rat Level第二份獨立指南
- 新增SRC-052：Steam 2026-08-27 Mouse Recipes guide，獨立列出Rat Level 9 Good / 12 Bad槽位及反重力、花盆密碼、酒標鎖、調整爐具流程。
- 它與SRC-050及9Puz一致：Cold Good #5 Cheese+Eggshell；Bad #4 Eggshell+Pencil；Bad #6 Paperclip+Pasta；Bad #7 Eggshell+Paper。與SRC-017手打指南不同，現以多來源一致者作優先候選，保留SRC-017做替代測試。
- Coioioin重複點擊硬幣說法與官方成就文字一致；日文藍開關／紅目標仍列替代方法。密碼數字仍未取得。
- QA仍為140個唯一ID；RAT-016至RAT-019的測試順序更新為先測多來源支持的Eggshell / Paperclip組合，再測SRC-017替代。


## 2026-11-17｜Bistro配方衝突測試擴充至129項
- BIS-048驗證Mochi使用whole Rice或Ground Rice；這道菜同時是已知Japan country dish，必須與Apple Mochi分開。
- BIS-049驗證Yeast Monster的三種來源候選：Yeast+Wooden Spoon、Yeast+Wine、Yeast+Tomato。
- QA總數140個唯一ID，仍未取得遊戲內執行紀錄。


## 2026-11-17｜Bistro / Cafe progression evidence re-check
- SRC-023完整日文1.0攻略可讀文字確認Bistro To-Do先Clean the kitchen，再Trade with the rat；初次給抽油煙機老鼠Cheese，取得Tomato；後續抽油煙機便條畫出料理，完成後取得新食材。尚無完整逐步菜色／獎勵清單。
- SRC-047 9Puz完整1.0路線補充：空Mixer容器煮出Scissors；Scissors找出隱藏Mixer開關並剪斷吊掛食材繩；老鼠請求解鎖特殊食材與七國磁鐵；五瓶酒按標籤排序。
- 七國料理只有Japan=Mochi可由文字確認；其餘六道不可從菜名推測。Cafe To-Do確認包含Set the kitchen on fire，Burnt Panini需再次烹煮觸發火災，但完整任務列仍未取得。
- QA最新140個唯一ID，全部仍是測試設計，未有遊戲客戶端實際執行紀錄。


## 2026-11-17｜Bistro mouse-gated ingredients
- SRC-050完整Steam攻略標註Olives（Tomato Cheese Appetizer）、Apple（Baked Apple）、Garlic（Pumpkin Soup）為老鼠贈品；SRC-023確認初次Cheese→Tomato與後續便條料理換食材。
- 這些只確認部分受限食材，不能推導完整請求順序；P1-01仍未清除。新增BIS-050..052，QA總數140，仍全是未執行測試設計。


## 2026-11-17｜Bistro To-Do screenshot transcription
- SRC-023內嵌截圖顯示EA Bistro To-Do五項依序為Clean the kitchen、Trade with the rat (0/4)、Get the mixer to work、Cook new ingredients (0/6)、Make pizza dough。截圖下方註記被裁切，疑似提到最後一項隨1.0推出。
- 這只能證明EA畫面有4次老鼠交易與6項新食材料理計數；不能直接當成1.0清單，也不可與Cafe Level 2 To-Do混淆。
- 新增BIS-053..055驗證1.0是否保留任務項目與兩個計數；QA目前140個唯一ID，尚未執行。


## 2026-11-17｜Cafe To-Do version history
- SRC-023 2026/03/28日文EA攻略截圖可辨識Cafe任務：Order missing ingredients、Restock the cakes (0/2)、Make drinks (0/10)、Cook new dishes (0/60)，且明示More coming soon；當時作者稱Cafe與To-Do尚未完成。
- 官方v3.0ea 2026/04/23新增To-Do「complete 8 orders」；2026/09日文Level 3攻略記錄Level 2 To-Do「Set the kitchen on fire」為Level 3解鎖條件。
- 以上不能直接拼成最終1.0完整清單；新增CAF-018..022做版本比對。QA目前140個唯一ID，仍未執行。


## 2026-11-17｜SRC-053 official Cafe To-Do addition
- 新增SRC-053：SteamDB鏡像官方v3.0ea changelog，2026/04/23新增Cafe To-Do「complete 8 orders」。這與3月Cafe截圖四項舊任務及9月「Set the kitchen on fire」線索形成版本演進證據；但未能直接證明最終1.0完整任務列。
- README與Critic來源範圍同步至SRC-053；QA維持140個唯一ID。


## 2026-11-17｜自動推進工作方式與開工門檻
- CEO要求助手不要每次找到一小段資料就停下來。每次收到「繼續」或延續指示，直接讀取最新repo狀態並連續執行研究、交叉驗證、文件更新、QA與Critic；不要要求CEO重複背景。
- 不可聲稱能在對話回合結束後背景自主運作；實際可行方式是在每個工作回合內盡可能完成連續工作，並留下可接手的repo狀態。
- Ready for CEO Approval標準已寫入README：核心循環、progression、互動物理、recipe data、任務成就、zh-TW、例外及QA規格可實作；未解未知有隔離策略／實機驗證步驟；Critic沒有未處置P1。CEO核准前不得進正式遊戲實作。
- 本次新增SRC-054開發者對Bistro rat交易機制說明；來源登錄現至SRC-054。QA 140個唯一ID仍未執行。專案維持Research Only。


## 2026-11-17｜SRC-055 Bistro 配方狀態修正
- Steam 76-comment thread補充Goulash、Risotto、Focaccia。Goulash最終候選為Normal Meat + Ground Tomato + Wine（不是Ground Meat）；留言串有明確更正與原提問者回應。
- Risotto = Rice + Mushroom + Cheese（C級單一討論串）；Focaccia = Bread Dough + Olives + Olive Oil（與既有攻略交叉一致，B級）。全部維持community_candidate，沒有標記實機驗證。
- 配方資料必須將normal_meat與ground_meat分成獨立item key。QA維持140個設計案例，仍無實際執行紀錄。


## 2026-11-17｜SRC-056 繁中暫譯與Bistro配方圖示
- 開發者Leek於2026-07-14表示新料理名稱當時使用DeepL暫譯，待文字定稿後再交中文譯者修正。EA繁中名稱不可視為1.0最終字串。
- 玩家指出Tomato Cocktail配方圖示把Wine誤顯示為Meat，配方描述為Tomato Sauce + Wine + Olives；此證據支持圖示可能錯誤，不可只靠圖示抄配方。
- 同一玩家指出Kombucha沒有Mushroom，與多份攻略衝突；此為C級玩家反證，非開發者確認。保留Yeast alone / Yeast + Mushroom等候選，待實機測試。
- QA仍140個設計ID，未執行。

## 2026-11-17｜333筆配方追溯基線與QA更新
- 新增RECIPE_PROVENANCE_AUDIT.md：333筆候選食譜各自有Candidate ID，名稱來源映射至房間來源家族；公式來源欄目前全部UNMAPPED / NOT_AUDITED，不能宣稱完成逐筆追溯。
- QA新增BIS-056 Kombucha、BIS-057 Risotto、BIS-058 Focaccia，並修正BIS-023 Goulash為Normal Meat + Ground Tomato + Wine。QA共143個唯一設計ID，均未實機執行。
- SRC-056指出EA新菜名為DeepL暫譯，Tomato Cocktail曾有錯誤圖示；Kombucha配方有玩家反證，待實機驗證。


## 2026-11-17｜本回合最新狀態快照
- Source Register最新至SRC-056。
- QA計數以實際ID逐列重新統計：143個唯一ID（REC 14、PHY 15、STD 16、CAF 22、BIS 58、RAT 18），沒有重複ID；全部是設計，0執行。
- RECIPE_PROVENANCE_AUDIT.md含333個候選名稱列（SD 77、CA 112、BI 123、RL 21）；name source family已映射，formula_source_ids仍全部UNMAPPED / NOT_AUDITED。
- README、PROGRESS_REPORT、CRITIC_REVIEW、INTERNAL_HANDOFF、QA_TEST_PLAN已同步本輪最新計數。專案仍Research Only，Critic Round 1 FAIL。


## 2026-11-17｜SRC-057 Bistro雙軌進度補充
- 老鼠交易鏈：抽油煙機找到老鼠→給Cheese→Tomato→後續依便條圖示料理換取新食材。開發者說明見SRC-054，EA實機圖文見SRC-057。
- 七國磁鐵鏈：七道國際料理完成後各附磁鐵；只有Japan = Mochi有可讀文字與日本國旗截圖。Apple Mochi不是該磁鐵料理；可疑料理不計入。
- 76/76 cookbook counter僅是2026-09-09 EA截圖，非1.0最終數量。
- BIS-059/060新增磁鐵與Mochi/Apple Mochi排除測試；QA 145 unique，0 executed。完整交易獎勵映射與其他六國仍未知。


## 2026-11-17｜SRC-058 Pizza Dough與Crazy Calzone
- Pizza Dough首選配方修正為Flour + Yeast + Olive Oil；SRC-058明確糾正Dough不是Flour，且SRC-015/SRC-018交叉支持。
- Bistro provenance：121/123列有公式來源或動作來源線索；Clutter仍未映射，Crazy Calzone的Good/Bad分類有來源衝突。
- QA新增BIS-061核對Crazy Calzone實際tab；總數146個唯一設計ID，0執行。

## 2026-11-17｜SRC-058後驗證快照
- Source Register：SRC-058。
- QA：146個唯一ID，分布REC14 / PHY15 / STD16 / CAF22 / BIS61 / RAT18；0執行。
- Bistro provenance audit：121/123列有對應區段的來源公式／動作；Crazy Calzone列為CLASSIFICATION_CONFLICT，Clutter列為UNMAPPED。不要把來源映射當成實機驗證。
- Pizza Dough：Flour + Yeast + Olive Oil（SRC-015/018/058）。
- Crazy Calzone：SRC-050列Bad，SRC-018流程提及但未明示tab；待實機記錄tab，BIS-061。
- Bistro rat trades與七國磁鐵是兩條不同但互相依賴的進度鏈；只確認Cheese→Tomato與Japan=Mochi。
- 目前仍Research Only，Critic Gate FAIL。


## 2026-11-17｜四場景來源映射最新快照
- 333列候選中，332列已具備逐筆來源公式／動作引用；僅Bistro Clutter仍UNMAPPED。
- Student Dorm 77/77（SRC-019）；Cafe 112/112（SRC-020，Coffee Cake重複已去重）；Bistro 121/123對應分類來源列，Crazy Calzone分類衝突1列、Clutter未映射1列；Rat Level 21/21來源列，其中4個slot保留候選衝突。
- Source Register至SRC-058；QA 146 unique，0 executed。來源引用不等於實機驗證。Research Only / Critic FAIL。


## Clutter correction (SRC-024)
- The 1.0 Japanese walkthrough identifies Clutter as a final Bad recipe and quotes a hint suggesting clutter happens spontaneously; it gives no formula.
- Withdraw Cloth + Wooden Spoon as a sourced recipe. BI-B-034 references SRC-024 for the trigger hint only; formula remains UNMAPPED / TRIGGER_HINT_ONLY. BIS-018 and BIS-040 must test the spontaneous/physics trigger.


## 2026-11-17｜Bistro 1.0 counter correction
- SRC-024 1.0 screenshots show Bistro target counters 83 Good / 40 Bad (save progress 76/83 and 37/40).
- SRC-050 places Crazy Calzone under Bad Recipes. Reclassifying it from Good to Bad makes the Bistro inventory 83/40, matching the screenshot. It is marked counter-aligned candidate, not direct card-tab verified; keep BIS-061.
- Global candidate split is now 211 Good + 122 Bad = 333. Do not keep using old 212/121 or 84/39 counts as current.


## 2026-11-17｜候選計數修正後快照
- Bistro：83 Good / 40 Bad；全遊戲：211 Good / 122 Bad，共333候選。
- Crazy Calzone已改列Bad，與SRC-050 Bad Recipes章節及SRC-024 1.0 counter吻合；仍須BIS-061實機確認tab。
- Clutter僅有SRC-024自發混亂提示，公式仍未知。
