# Little Chef 復刻｜內部工作紀錄（交接版）

更新日期：2026-11-16  
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

## 1. GitHub 狀態（2026-11-16 最新）
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
