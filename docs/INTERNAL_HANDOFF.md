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
