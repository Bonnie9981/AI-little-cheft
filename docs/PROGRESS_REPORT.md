# Little Chef 復刻｜專案進度匯報

更新日期：2026 年 11 月 17 日  
Repository：https://github.com/Bonnie9981/AI-little-cheft  
目前階段：研究與規格整理（Research Only）

## 一、專案目標
將《Little Chef: Cozy Cooking》製作成桌面瀏覽器與手機橫向可玩的忠實網頁復刻，正式語言為台灣繁體中文（zh-TW）。保留原作溫暖可愛的視覺感受，但以自行重繪素材為主。目標是完整涵蓋場景、食譜、互動、成就及額外內容。

主要流程：
主選單 → My Room → Student Dorm / Cafe / Bistro → 三個主廚房皆 100% → Rat Level

My Room 是樞紐空間，不是第四個主廚房。

**目前尚未開始正式遊戲實作。** 這是刻意的工作順序：先完成規則研究與驗證，再進入開發。

## 二、目前進度概覽
以下是主觀工作估計，不是已通過驗收的完成率：

| 項目 | 估計 | 說明 |
|---|---:|---|
| 場景與主要流程 | 100% | 主場景關係與解鎖方向已整理 |
| Student Dorm 食譜 | 95% | 48 Good / 29 Bad候選與公式列齊全；配方仍未實機驗證 |
| Cafe 食譜 | 95% | 71 Good / 41 Bad候選與公式列齊全；狀態與版本衝突待驗證 |
| Bistro 食譜 | 90% | 84 Good / 39 Bad候選與公式列齊全；部分配方和交易順序待驗證 |
| Rat Level | 85% | 9 Good / 12 Bad slot列齊；密碼與狀態衝突待驗證 |
| 解鎖流程 | 85% | 主線已整理；Cafe To-Do完整內容與Bistro任務列仍缺 |
| 成就 | 95% | 清單大致齊全，觸發條件仍需驗證 |
| 物理互動規格 | 70% | 已有輸入、物件狀態、設備與驗收規格；原作係數未知 |
| 台灣繁中詞庫 | 90% | 312筆命名配方已有候選譯名；校對、雙關與UI長度待完成 |
| 資料庫驗證 | 45% | 四場景公式表與名稱數量對齊；來源逐筆綁定及狀態驗證未完成 |

百分比不可直接相加為整體完成率。「有配方線索」不等於「已確認」。

## 三、已完成的規劃
- 確認復刻範圍、平台方向與繁體中文要求。
- 整理主選單、My Room、三個主廚房與 Rat Level 的流程。
- 規劃食譜、物件狀態、設備、加工規則、老鼠交易、成就與解鎖資料庫。
- 規劃 IndexedDB 本機存檔、localStorage 偏好設定及 JSON 匯出／匯入。
- 將物理互動與食譜判定分離。
- 開始整理官方更新與社群攻略，標記版本差異與可信度。
- 確認正式遊戲素材授權不能由 prototype 素材授權推論，因此採自行重繪方向。

## 四、時間線
| 日期 | 事件 |
|---|---|
| 2026/07/12 | 官方推出 Bistro 第三關 |
| 2026/08/26 | 官方 hotfix 修正 Shredded Cheese 錯誤變成 Pizza |
| 2026/09/11 | v1.1 更新，修正成就、文字、物件與食譜書等問題，並涉及 Goulash、Tomato Cocktail |
| 2026/11/16 | 整理研究與規格狀態；重新確認 GitHub；刪除根目錄測試空白檔；成功建立 README；準備上傳研究文件 |

## 五、下一階段工作
### 第 1 階段：完成全場景食譜資料庫
整理 Student Dorm、Cafe、Bistro、Rat Level 全部食譜；記錄輸入、加工狀態、設備、順序／溫度條件、輸出結果、版本與來源可信度。優先釐清互相矛盾或受版本影響的配方。

### 第 2 階段：補完互動與關卡規則
整理拖曳、投擲、碰撞、切割、混合、烹煮、加工狀態、老鼠交易、隱藏物件、任務及 Rat Level 完整通關條件。

### 第 3 階段：本地化、QA 與 Critic
完成台灣繁中詞庫；為食譜、互動、成就、解鎖與存檔建立驗收案例；由 Critic 獨立檢查遺漏、矛盾、錯誤假設與授權風險。

### 第 4 階段：正式開發
只有前面研究、資料庫、QA 與 Critic 審查達到可接受標準後，才開始遊戲實作。

## 六、工作方法
1. **先證據、後定案：** 優先採官方資訊；官方沒有說明時，再用多個玩家來源交叉核對。
2. **記錄物件狀態：** 配方可能取決於材料加工、設備、溫度與操作順序。
3. **注意版本差異：** 每筆資料保留版本資訊。
4. **系統拆分：** 物理、食譜、任務、成就與存檔各自管理。
5. **不把推測寫成事實：** 未確認項目標示待驗證。
6. **先避免返工：** 不急著做可玩空殼，優先確保規則正確。

## 七、GitHub 狀態
Repository：Bonnie9981/AI-little-cheft，公開，預設分支 main。

本輪重新測試後，GitHub 寫入已成功：
- 刪除根目錄測試空白檔「？」；commit：86413423339f303e1536947c5441d9d395ecff9f
- 建立 README.md；commit：26433ba4a95a3b3b996e536f6be161cba497c401

接下來會把內部交接與進度匯報文件放入 docs/。

## 八、目前判斷
最值得投入的不是先做角色動畫或菜單，而是把食譜和互動規則整理成有來源、能追溯、能測試的資料庫。遊戲的難點還包括加工狀態、設備、冷熱條件、順序、老鼠交易、關卡解鎖與版本修正。若太早開發，可能因規則錯誤而重做。

因此建議繼續維持 Research Only。下一個重要里程碑是：**完成全場景食譜與機制資料庫的證據核對，並通過 QA 與 Critic 審查。**

---
*本報告中的百分比是工作估計，不是驗收結果；未確認資料須在正式開發前再次核對。*


## 本輪新增（2026-11-16）
- 新增工作日誌與時間線兩份文件。
- Bistro 配方補入多筆社群候選，但全部仍標記未實機驗證。
- 重新確認官方版本節點：Early Access 2026-03-16、Bistro 2026-07-12、1.0 2026-08-26、v1.1 2026-09-11、Steam Trading Cards 2026-09-25。
- 下一優先事項：釐清 Goulash／Tomato Cocktail 的修正後配方、補齊 Bistro 食譜，接著完成 Rat Level 冷熱條件。


## 最新研究修正（2026-11-16）
- Goulash 候選配方更正為一般 Meat + Ground Tomato + Wine；先前的 Ground Meat 說法是玩家討論中的誤報。
- Tomato Cocktail 候選配方為 Olives + Wine + Ground Tomato。
- 兩者均有官方 v1.1 cookbook 修正背景，但精確配方仍以社群來源為線索，尚未實機驗證。
- 追加 Bistro 食譜候選：Mushroom Soup、Apple Mochi、Croque Monster、Pumpkin Soup、Tomato Juice、White Wine、Pumpkin Bread、Hamburger、Apple Sauce、Olive Oil、Rosé、Vegan Sandwich、Pumpkin Fries、Meatloaf、Pizza、Italian Rice Balls、Schnitzel、Meat Lover Pizza。


## 2026-11-16｜追加研究進展
- 新增第二份 Steam Bistro Guide（ID 3764982550），與先前攻略交叉支持 Goulash、Tomato Cocktail、Focaccia 等配方；同時補出多筆 Good/Bad Recipes 候選。
- 找到 2026-09-02 Rat Level 完成路線指南，整理冷爐五項、熱爐四項、反重力與密碼操作，以及 26 項成就觸發位置。
- Student Dorm 48 good / 29 bad 的數量線索來自搜尋摘要，原頁未能開啟，暫不視為已核實。
- 研究仍處於 Research Only；下一個可驗收交付物是 Bistro 配方矩陣、Rat Level 狀態機與 Student Dorm/Cafe 全量計數表。


## 2026-11-16｜Cafe 與 Student Dorm 研究補充
- 取得 Steam 2026-08-10 更新版攻略搜尋索引，已補出 Cafe Job 的完整 Good/Bad Recipe 候選清單與前置互動。
- 重要更正：Tiramisu 使用 Cake + Filled Coffee Cup + Milk；Double Espresso 需把已裝滿的杯子留在機器中，等待咖啡豆恢復後再操作。
- 新版新增 Canned Coffee = Coin + Cup of Espresso；Mocha、Strawberry Latte、Dirty Chai Latte 亦有明確咖啡／茶狀態差異。
- Student Dorm 新版另列 Tomato/Egg Stir Fry。
- 目前 Cafe 資料已比前一輪完整，但尚未完成逐條計數、來源比對與 QA，仍不能標記為完成。


## Rat Level 與 Bistro 研究補充（2026-11-16）
- Rat Level 冷爐 5 項、熱爐 4 項的 Good Recipes 已有更新版攻略明確列出；Bad Recipes 也有 12 類輸入線索，含 Eggshell 的取得方式。
- Rat Level 的第五個冷爐圖示仍有 Eggshell／Leaf 來源衝突，會用 slot 計數作為驗證依據。
- 可直接讀取的 Bistro Guide 列出 76 項 Good、31 項 Bad；留言補充 6 個配方，並明確確認 Goulash 使用 Ground Tomato。
- Bistro 仍有配方衝突：Tomato Cheese Appetizer 是否需 Olives、Apple Mochi 是否需 Ground Rice，列入待驗證清單。


## Cafe 經濟與 My Room 支線（2026-11-16）
- 開發者確認 Cafe 訂單紙會要求製作特定料理，完成後給予 tip coin；取下已完成訂單後，稍後會有新訂單。
- v3.0ea 更新新增 8 orders To Do、18 道 Cafe 食譜、espresso machine、提示系統與 25 個電話號碼。
- Safe 需要 keycard；攻略線索為 Photo + Coin。Void Bagel 由三個 Bagel 在 oven 製作，再於 Safe 取得。
- My Room 裝飾可能與 Cafe 訂單硬幣連動：日文攻略稱存入 20 枚硬幣後可取得畫筆，解鎖更多房間裝飾；仍需補官方／獨立來源。


## 官方版本與解鎖條件修正（2026-11-16）
- **重要修正：** 官方 v5.1ea 明確要求先完成 Level 2 的 To-Do list 才能進入 Level 3；「把 Cafe 燒起來」不能單獨當作充分解鎖條件。
- My Room 有正式裝飾與存檔系統：20 Coin 解鎖畫筆，可調整 wallpaper、wood type、poster frame；另有書本排列與主選單 logo 成就。
- v4.0ea 移除 Master Chef / Master of Disaster，最終成就清單以 26 項為準。
- v4.1ea 調整 Coin 重生與 Canned Coffee 配方；v5.4ea 加入 Bistro 提示與食譜書清除 new stars 功能。
- 目前需補完 Level 2 To-Do 完整項目與 My Room 可互動物件清單。


## Level 2 To-Do 與 Bistro 解鎖流程（2026-11-16）
- 官方 v5.1ea 要求完成 Level 2 To-Do 才能進 Level 3；日文玩家通關紀錄進一步描述清理 Cafe、老鼠交易、完成訂單、火災與滅火等流程。
- To-Do 至少包括 Clean the kitchen、Trade with the rat、Complete 8 orders、Set the kitchen on fire；完整 UI 任務清單仍待核實。
- Bistro rat 位於抽油煙機，先給 Cheese 後依序製作便條上的料理換取新食材；七國料理會收集七個磁鐵。
- Mixer 修復點在右側花盆電路板；食材加工狀態會直接改變食譜結果。
- Wine About It 要將五瓶酒按標籤正確排序；Messing Around 與 Mixer 超載有關。


## 物理互動與七國料理（2026-11-16）
- 官方資料確認核心互動包含拖曳、拋擲、輕放、混合與破壞；所有物件都有重量與運動表現。
- Steam 功能列表包含 Mouse Only 與 Touch Only 操作模式，將以共用輸入層支援桌面與手機橫向。
- 物理規格尚未完成；原作的質量、摩擦、彈性等精確係數沒有可靠公開資料，復刻版會以可調參數校準，不冒稱原作係數。
- 七國料理僅能確定其中一項 Mochi；其餘六項仍待查，Bistro 任務線尚未完成。


## Student Dorm 1.0 To-Do 補完（2026-11-16）
- 找到 2026-10-09 全攻略，確認 Student Dorm 48 Good / 29 Bad，並列出 24 個場景物件。
- To-Do 至少 6 項：8 道 pasta dishes、借用 Shane's Cheese、播放三卷磁帶、清洗整理餐具以解鎖 coffee maker、澆灌 basil、累積 40 道 good + bad dishes。
- 新攻略對 Beans on Toast、French Toast、Savory Sandwich、Tomato Soup、Pasta Carbonara 等配方提供了比 8/10 指南更細的狀態／替代配方，已列入衝突表，尚未實機驗證。
- 章節解鎖條件需同時完成所有 Good Recipes 與 To-Do；Bad Recipes 是否可選尚未獲官方證實。


## Cafe Job 1.0 數量與配方衝突（2026-11-16）
- Pixel Questing 2026-11-09攻略列出 Cafe 71 Good / 41 Bad、37 個場景物件；Good 清單有 Coffee Cake 重複列，去重後為 71 種。
- 新攻略對 Tiramisu、Babycino、Hot Cocoa、Latte、Canned Coffee、Dirty Chai Latte、To Go Drink、Bento Box 等配方與 8/10 Steam Guide／官方版本資料有衝突，已加入 Recipe Reconciliation Register。
- 21931電話流程需撥號後拿起 handset 並等待對方說完，開發者於 Steam 討論確認。
- Cafe完整To-Do列數仍待查；官方v3.0ea只確認新增一項「完成8張訂單」，v1.0另有火災任務。不可把8張訂單誤認成8個任務。


## Cafe To-Do 數量校正（2026-11-16）
- 官方 v3.0ea 原文只確認一項 To-Do：「complete 8 orders」；日文攻略「ToDo list新增8件」語意不明，不能視為八個獨立任務。
- 已將 order target = 8 與 Level 2 To-Do task count = unknown 分開記錄。
- Bistro 解鎖流程目前只確認清潔、老鼠交易、火災／滅火、訂單等任務類型；完整 UI 清單仍待實機畫面或影片。


## Rat Level 設備模型修正（2026-11-16）
- 新增 1.0 玩家完整攻略指出 Rat Level 是通電罐頭式 cooker，近似微波爐；酒瓶謎題解開後可切換電力強／弱，同一配方產生不同結果。
- 復刻規格將採 ElectricCanCooker 與 power_level = low/high，不再把它當一般烤箱溫度。
- 9項 Good Recipes 仍可按攻略 OFF 5項、ON 4項分類，但 ON/OFF 與 low/high映射尚待實機確認。
- 花盆 note的三位數密碼未在可讀文字來源披露，明確列為待取得畫面，不猜測。


## Bistro 1.0 新增內容與 Coioioin 修正（2026-11-16）
- 1.0 玩家通關記錄指出 Bistro 新增約 10 道料理：已知 7 Good、2 Bad；另有 Clutter作為最後一個 Bad候選，製作條件仍未知。
- Coioioin不是單純隨機連續拋三次：先按藍色開關，再投擲紅框硬幣。
- 1.0通關後 My Room會出現生日蛋糕與媽媽的信，蛋糕蠟燭可互動。
- Set the kitchen on fire To-Do有玩家回報顯示不同步；需分離 task、achievement與 Steam sync狀態。


## Bistro 配方數量分期校正（2026-11-16）
- 7/14 Bistro Guide正文逐行核算為 76 Good / 31 Bad，屬 EA baseline。
- 8/27更新新增 7 Good + 2 Bad；9/10正式版玩家另記錄 Clutter為新增 Bad。
- 目前 1.0候選總量為 84 Good / 39 Bad（123 total），但這是跨來源推算，仍待遊戲內 cookbook counter確認。


## Bistro Rat Trade 與七國料理（2026-11-16）
- 開發者確認：給抽油煙機後方老鼠 Cheese啟動交易；之後依照老鼠展示的料理圖製作，即可換取新食材。
- 玩家通關記錄確認首次獎勵為 Tomato；後續還有 Apple、Olive、Garlic等獎勵支線。
- Going Global需完成 7道國家料理並收集 7個磁鐵；目前只確認日本料理 Mochi，其餘六道仍待圖片／實機確認。
- 老鼠顯示愛心是所有交易完成的感謝訊息，不是新的料理請求。


## zh-TW 詞彙基準（2026-11-16）
- 已建立 docs/ZH_TW_GLOSSARY.md，涵蓋主要 UI、食材、Student Dorm/Cafe/Bistro料理與成就。
- 台灣用語基準：起司、馬鈴薯、可頌、吐司、披薩、果昔、調理機；「美味料理／怪奇料理」為 Good/Bad分類暫定譯名。
- 官方 Steam不支援繁體中文，因此本專案需自行在地化，不可直接複製簡體中文攻略翻譯。
- Rat Level、所有 Bad Recipes、My Room與完整劇情文本仍未完成詞彙校對。


## Bistro／Rat Level 最後一輪線索（2026-11-16）
- Wine About It 的玩家解法為依五瓶酒的標籤高度由短到長排列；實際瓶身順序仍待畫面確認。
- Rat Level冷爐第五項存在 Leaf／Eggshell衝突；Bad slots另有 Egg／Eggshell、Pasta／Paperclip組合衝突。
- Coioioin的新版玩家提示是先按藍色開關，再投擲紅色區域硬幣；仍需在遊戲內確認是否還需要三次同面。


## 全關卡 Recipe Inventory（2026-11-16）
- 已建立 docs/RECIPE_INVENTORY.md。
- 目前候選總量 327：212 Good、121 Bad。
- Student Dorm 48/29、Cafe 71/41、Bistro 84/39（推算）、Rat Level 9/12。
- 327與官方「over 300 recipes」相符，但尚未由遊戲內 cookbook counter驗證；仍需逐筆補配方、狀態、設備、來源、信心與繁中名稱。


## Student Dorm / Cafe 配方公式初稿（2026-11-16）
- 新增 docs/RECIPE_FORMULA_DRAFT.md，整理 Student Dorm 77筆、Cafe 112筆候選公式，共189筆。
- 已標出配方狀態、設備依賴與來源衝突；尚未實機驗證，不能標記為完成。
- Bistro與 Rat Level公式矩陣尚未完成。


## Bistro / Rat Level 配方矩陣（2026-11-16）
- 新增 docs/RECIPE_FORMULA_BISTRO_RAT.md，整理 Bistro 83 Good / 34 Bad候選與 Rat Level 9 Good / 12 Bad slots。
- 四個房間現在都有候選 recipe names與初步 formula drafts。
- Bistro來源衝突、Rat Level power state與slot差異仍未完成實機驗證。


## 官方配方歷史補充（2026-11-16）
- v2.9ea移除一個重複 Chocolate Spread。
- v2.9ea允許 Tiramisu多種有效輸入：Cake + Coffee + Dough 或 Cake + Coffee + Milk。
- v2.9ea新增 Savory Sandwich的 Bread + Cheese + Tomato Sauce組合。
- 這些是 Early Access官方規則，已與 1.0候選配方分開記錄。


## 料理設備與輸入規則（2026-11-16）
- 已找到明確攻略說明：最多放入三種材料，再點擊設備烹調；Student Dorm用 Cooking Pot，Cafe用 Microwave Oven。
- Bistro需 Cooking Pot + Mixer；Rat Level為低／高電力的 Electric Can Cooker。
- 非食材道具也可投入設備形成 Bad Recipes，因此資料模型必須區分 Ingredient、Tool、Clue、Container與Interactable。
- 材料消耗、輸入順序、設備暫存等仍待實機驗證。


## 互動與物理規格（2026-11-16）
- 新增 docs/INTERACTION_SPEC.md，整理桌面／手機輸入、物件分類、狀態轉換、設備互動、各關卡 puzzle chain與 acceptance tests。
- 已有可觀察互動規格，但原作物理係數、材料消耗、輸入順序、設備暫存與物件位置存檔仍未知。
- 復刻版物理參數會標註為本專案調校值，不冒稱原作數值。


## QA Test Plan（2026-11-16）
- 新增 docs/QA_TEST_PLAN.md，包含 recipe、physics、四個房間、My Room、26成就、zh-TW、responsive與save/load驗收。
- 這是測試設計，不是測試通過紀錄。
- 主要 blockers：Cafe完整To-Do、七國料理與rat順序、Rat code/power mapping、D級配方衝突、327候選數量確認。


## Rat Level 材料數量例外（2026-11-16）
- 新增 1.0玩家攻略指出 Rat Level每次只使用兩種材料；已從通用三材料規則中排除，單獨建模 max_inputs = 2。


## Source Register（2026-11-16）
- 新增 docs/SOURCE_REGISTER.md，整理 SRC-001至SRC-030，涵蓋官方版本、開發者回覆、食譜攻略、玩家通關紀錄與台灣繁中詞彙。
- 已建立證據優先級與搜尋摘要／快取限制註記。
- 下一步需把 327個候選 recipe逐筆連結到 SRC IDs。


## Student Dorm / Cafe 配方修正（2026-11-16）
- 已根據 Steam cached guide與 developer replies校正公式草稿。
- Developer確認 Smoothie包含 Peanut Butter；Good Protein Shake = Milk + Peanut Butter + Protein Powder。
- Cafe主要配方已校正：Babyccino、Latte、Hot Cocoa、Avocado Milk、Strawberry Cheesecake、Chocolate Bomb、Canned Bread等。
- Steam Guide 3713640352目前已從公開頁面移除，但搜尋索引仍有內容；已標記為 cached community evidence。
- 10/9與11/9 Pixel Questing仍與Steam guide存在配方差異，已加入衝突表。


## Peanut Butter 隱藏食材（2026-11-16）
- Developer確認：按下主選單信件中的按鈕即可解鎖 Peanut Butter，不需真的加入願望清單；解鎖會保存到存檔。
- 已列為 Student Dorm食譜的前置條件，不能依賴外部 Steam Wishlist。


## Item / ItemState Inventory（2026-11-16）
- 新增 docs/ITEM_STATE_INVENTORY.md，列出四個房間的物件分類、狀態與互動能力。
- 已拆分所有關鍵加工狀態，為後續 machine-readable recipe records打底。
- Student Dorm其他三個locker內容、Cafe部分道具、材料消耗與物件位置存檔仍待查。


## Student Dorm / Achievement 定位補充（2026-11-16）
- D2是 Shane locker key；右側另一個 tile是 mouse hole。給洞口 Cheese觸發 I Smell Cheese，與locker unlock無關。
- A Lot to the Right的茶盒在上層架、Jam右側。
- 補入成就流程：Fair Trade（Cafe老鼠）、What's The Emergency（911）、Aw That's Hot（Burnt Panini再烹煮）、Nothing Nowhere（三個Bagel）、Messing Around（Mixer第二、三次運作造成混亂）。


## Achievement Matrix（2026-11-16）
- 新增 docs/ACHIEVEMENT_MATRIX.md，完整列出 1.0的26項成就與觸發候選。
- 已排除 v4.0移除的 Early Access成就 Master of Disaster。
- 未解項目：100%精確條件、Bookworm排序、Going Global七道菜、Coioioin觸發細節。


## Student Dorm To-Do 完整清單（2026-11-16）
- 1.0攻略確認六項：8道Pasta/Ramen料理、Borrow Shane's Cheese、播放Red/Green/Remix三卷卡帶、Make Coffee、Water Basil、Cook New Dishes累積40道Good+Bad料理。
- 清洗碗盤與收好餐具是Make Coffee前置，不是獨立To-Do。
- 9Puz指出每個房間都有recipe/task ledger，Student Dorm需完成Good與Bad兩個recipe tabs及全部tasks。
- Flooded約50%水位時會提示；Bookworm需讓書背波浪線連續。


## Cafe To-Do範圍更新（2026-11-16）
- 已確認 Cafe To-Do中有「完成8張訂單」；1.0攻略另列火災任務。清理與老鼠交易是必要進度互動，但其是否為獨立To-Do row仍未確認。
- 21931電話、Coins、Espresso Cup、Safe與fire alarm是其他100% blockers，是否為獨立To-Do row仍待確認。


## zh-TW 配方名稱字典（2026-11-16）
- 新增 docs/ZH_TW_RECIPE_TRANSLATIONS.md，完成312筆命名配方的台灣繁中候選譯名。
- Rat Level 21個符號槽位保留slot標示，不自行命名。
- 翻譯覆蓋已完整；雙關、罕見料理、畫面長度與母語校對仍待完成。


## 2026-11-17｜Cafe To-Do 與 Coioioin 證據校正
- 官方v3.0ea的正確解讀是新增一項To-Do：「完成8張訂單」；Cafe完整To-Do列數仍未知。
- 目前能具體命名的任務候選：清理廚房、Blue Teapot老鼠交易、完成8張訂單、讓廚房起火；其餘4項仍待找回。
- 1.0路線明確要求完成 Cafe To-Do 才能進 Bistro；不能把火災單獨視為完整條件。
- Coioioin Steam成就說明及兩則玩家回報支持「同一面連續三次」；另有藍色開關／紅色目標區說法，列為待核對的額外條件，不先寫死。
- 來源：官方 v5.1ea更新紀錄、Steam成就頁、Steam coin discussion、9Puz 1.0 route。


## 2026-11-17｜Cafe To-Do 數量再校正（重要更正）
- 回查 SteamDB 保存的官方 v3.0ea patch notes（2026-04-23），原文只有「New Todo: complete 8 orders」：這是**一項任務，目標為完成8張訂單**，不是新增8個任務。
- v5.1ea（2026-07-14）另外要求完成 Level 2 To-Do list 才能進 Level 3。
- 1.0攻略確認火災互動也是Level 2 To-Do；清理廚房與老鼠交易屬必要進度互動，但目前未能證明它們在UI中各自是獨立To-Do。
- 已撤回「Cafe共有8個To-Do、已知4個」的錯誤說法。完整任務列數與其他任務名稱仍待找回。
- 來源：SteamDB v3.0ea patch notes、官方 v5.1ea、9Puz 1.0 completion route。


## 2026-11-17｜Bistro To-Do 與國際料理線索補強
- 日本玩家 2026-09-09 Level 3 walkthrough明確展示 Bistro To-Do前兩項：「Clean the kitchen」與「Trade with the rat」；用 Cloth清潔，給抽油煙機老鼠 Cheese後得到 Tomato，後續依便條圖製作料理換新食材。
- Going Global：七道國際料理會在抽油煙機上逐一吸附磁鐵；目前文字仍只明確辨識日本料理 Mochi，其餘六道需從圖片或遊戲畫面確認。
- Coioioin：Steam官方成就描述與多份玩家指南均只寫同一面連續三次，先以點擊爐旁硬幣作主要測試；藍開關／紅色投擲區說法暫列低信心支線。
- 來源：日本玩家 Level 3攻略、Steam achievement page、9Puz、Steam guide。


## 2026-11-17｜本輪研究交付盤點
- 配方名稱候選：333筆（212 Good + 121 Bad）。
- 公式表目前列數：Student Dorm 77、Cafe 112、Bistro 123、Rat Level 21，合計333列；這代表每個候選名稱都有公式或狀態候選，不代表公式已實機驗證。
- 台灣繁中命名表：312筆命名料理；Rat Level 21格使用slot標籤而非杜撰菜名。
- Student Dorm六項To-Do已由1.0攻略列出；Cafe完整To-Do仍未找回，已修正「8 orders」誤讀；Bistro至少可讀到清潔與老鼠交易兩項。
- QA與Critic尚未通過；Research Only維持。


## 2026-11-17｜配方／翻譯資料完整性稽核
- 以程式逐條比對Inventory、Formula Draft與zh-TW Translation Dictionary。
- 333個候選條目全部有對應公式列：Student Dorm 77、Cafe 112、Bistro 123、Rat Level 21。
- 312筆命名料理全部有繁中譯名：Student Dorm 77、Cafe 112、Bistro 123；無缺漏、無重複key。
- Rat Level 21格是符號slot，不杜撰菜名。
- 修正Sausage Roll主鍵一致性與English Breakfast缺少譯名。
- 注意：這是資料列完整性檢查，不是遊戲內配方驗證。


## Cafe To-Do 的 1.0 玩家實際流程補充（2026-11-17）
- 日本玩家 1.0通關記錄顯示：先完成「Set the kitchen on fire」，再清完剩餘訂單，回 My Room後才解鎖 Bistro。
- 該玩家遇到火災已發生但To-Do未勾選的狀況，重做火災互動後才繼續；應視為任務登錄bug候選。
- 目前 Cafe明確可命名的To-Do為「Complete 8 orders」與「Set the kitchen on fire」；完整總列數仍未由UI畫面證實。
- Bistro To-Do則已確認「Clean the kitchen」與「Trade with the rat」，不可把這兩項錯放到Cafe。


## 2026-11-17｜本輪交付數量與剩餘研究閘門
- 公式表完整列出333筆候選：Student Dorm 77、Cafe 112、Bistro 123、Rat Level 21 slots。
- 繁中翻譯表列出312筆命名料理及21個Rat Level符號slot；與Inventory逐條對齊，無缺漏或重複key。
- QA目前88個唯一測試案例；來源登錄SRC-001至SRC-046，共46筆來源。
- 尚未完成的關鍵研究閘門：Cafe完整To-Do UI列數與名稱、Bistro七國料理其餘六項、Rat Level三位數密碼與OFF/ON對應low/high、Clutter觸發條件、全部D級配方衝突的實機驗證、完整物理行為校準。
- 這些是明確未完成項目；沒有把候選配方數量或文件列數冒充成遊戲內驗證。


## 2026-11-17｜Student Dorm 配方證據重審（最新狀態）
- Clutter 的 Cloth + Wooden Spoon 候選已撤回；目前只確認菜名存在，精確觸發條件未知。
- Smoothie：開發者確認 Peanut Butter 是其中一項材料，但未給出完整公式；1.0攻略另列 Strawberry Jam + Banana + Milk。兩條候選並存。
- Good Protein Shake：Milk + Peanut Butter + Protein Powder 有開發者明確確認；Banana alternate僅作低信心候選。
- Pasta A La Carbonara：Pasta + Egg + Cheese 與 Pasta + Egg + Milk 仍衝突。
- PB&J Sandwich：保留原料直做與 PB&J Jar + Bread 等替代路徑。
- 上述只更新證據分級，沒有新增遊戲內驗證。研究仍為 Research Only。


## 2026-11-17｜Coioioin觸發方式重新開放為雙路線待驗證
- 日文1.0第一手攻略明確提供「按藍框開關 → 將硬幣投進紅框」路線，並說這不是單純靠同面連續三次的隨機機率；作者另回報Steam成就需重啟後才同步。
- 這與Steam官方成就描述及較早玩家指南的「同面三次／反覆點硬幣」說法衝突。先前將藍開關降為低信心支線的結論撤回。
- QA新增RAT-011（藍開關／紅框投幣）與RAT-012（Steam重啟同步）；RAT-008保留舊路線。兩條觸發方式都未實機驗證，不能定案。
- QA案例數由88增至90；Research Only維持。


## 2026-11-17｜Bistro 磁鐵配方與狀態依賴補充
- 9Puz 1.0 route明確寫出 Big Magnet：將老鼠交易獲得的 Magnet 放入料理設備烹調；8/10 Steam guide的描述較簡略，仍需用 Bad Recipe counter驗證。
- Compass = Scissors + country Magnet；建議先讓磁鐵登記至 Going Global，再把磁鐵投入配方。
- 復刻資料需區分收到磁鐵、登記國家磁鐵、消耗磁鐵製作 Compass / Big Magnet三種狀態。
- 以上是候選規則補充，未新增遊戲內驗證。


## 2026-11-17｜Bistro 磁鐵依賴 QA 擴充
- QA新增BIS-019：Country Magnet登記後才測Compass，分離磁鐵持有與Going Global登記狀態。
- QA新增BIS-020：比較老鼠獎勵Magnet直接使用與放入料理設備後是否觸發Big Magnet。
- QA於本輪新增BIS-023至BIS-026與CAF-017後，經逐列統計為102個唯一測試案例；均為測試設計，尚非遊戲內執行結果。Research Only維持。


## 2026-11-17｜SRC-017版本錯置更正與Bistro衝突撤回
- 直接檢查Steam Guide ID 3686619896後確認它是v4.0 EA（3/17發布、6/8更新），配方以v3.0 EA為基準，只含Student Dorm/Cafe，沒有Bistro或Rat Level。先前稱它為9/1簡中1.0指南的記錄撤回。
- Steam Guide ID 3713640352雖有8/10全遊戲搜尋索引，但直接開啟頁面仍是4/25 EA內容且已被下架；其8/10 Bistro/Rat Level資料只算快取線索。
- RECIPE_CONFLICTS已撤回所有錯誤歸因SRC-017的Bistro/Rat Level配方：Clutter Cloth + Wooden Spoon、Rat Leaf、Eggshell + Pencil、Pasta-only/Pasta+Paper等。
- Bistro其餘配方衝突只保留可追溯至7/14、8/10快取、9/2 9Puz及獨立玩家討論的候選。研究仍為Research Only。


## 2026-11-17｜SRC-023版本範圍更正
- 日本Level 3攻略雖於2026-09-09刊出，但作者明確說文章內容是2026-07-13的Early Access Level 3更新，不是1.0完整版本攻略。
- 因此其中的Bistro To-Do、老鼠交易、七國料理、Mixer與Wine puzzle保留為EA第一手歷史證據；是否延續至1.0須由SRC-024及其他正式版來源交叉確認。
- 七國料理段落只明確命名日本的Mochi，其餘六道仍未有可讀文字證據，不從料理名稱猜國籍。


## 2026-11-17｜追加研究輪次：Rat Level 來源交叉核對
- 重新直接讀取 9Puz 1.0 完整攻略，不再只依賴搜尋摘要。補強 Rat Level 反重力→花盆密碼→酒瓶標籤鍵盤→冷／熱 cooker 的完整解謎順序。
- 冷態 Good 五槽、熱態 Good 四槽及兩材料上限已取得可讀文字支持；Eggshell/Leaf、Egg/Eggshell + Pencil、Pasta相關 Bad slot仍保留衝突。
- 9Puz確認 Big Magnet候選動作是烹調老鼠獎勵磁鐵；Compass需先登記 Going Global，再以Scissors + country Magnet製作。
- Steam Guide ID 3713640352的瑞典語頁面目前可直接讀取完整文字正文，雖仍顯示已移除提示；已將來源可讀性註記更新，不再簡化稱為只有搜尋摘要。
- 本輪沒有取得花盆密碼的實際數字，也沒有取得除 Japan = Mochi 以外的六國料理配對；兩者仍是阻塞項，未以推測填補。


## 2026-11-17｜新增官方 v1.1 版本校正
- 新增 SRC-049：官方 v1.1 修正 Coioioin Steam同步、Level 1重複罐子、Goulash與Tomato Cocktail cookbook配方，並改善 Rat cursor / number-lock 點擊區域。
- 因此 Goulash、Tomato Cocktail 及 Rat密碼鎖互動列為版本敏感項；舊版指南不得直接視為現行正確。
- 本輪確認七國磁鐵由老鼠任務取得，但目前可讀文字仍只公開 Japan = Mochi；其他六國料理名稱、花盆密碼數字仍未取得可直接引用的文字證據。
- 研究狀態仍為進行中；本輪更新不是完成宣告。


## 2026-11-17｜完整配方指南全文與版本敏感配方
- 新增SRC-050：Steam Guide ID 3713640352全文可讀，取得三個主廚房與Rat Level的大量候選配方及流程資料。
- 指南列出Goulash候選 Meat + Wine + Ground Tomato；Tomato Cocktail候選 Olives + Wine + Ground Tomato。但官方v1.1明確修正兩筆cookbook recipe，故目前只能標為舊版候選。
- 指南留言指出Dirty Chai Latte應使用Coffee（非Coffee Beans），Tomato Juice應使用Ground Tomato（非整顆Tomato）；留言與指南正文有衝突，已新增獨立QA，不直接覆寫。
- QA新增BIS-023至BIS-026，專門核對上述四項版本／留言衝突。
- 七國料理對應與Rat密碼數字仍未取得可讀文字證據；維持UNKNOWN。


## 2026-11-17｜Cafe電話事件狀態補證
- 新增SRC-051：開發者直接確認Cafe電話輸入後，必須拿起話筒並等通話對白結束，Avocado與Lettuce才會生成。
- 這補上Level 2一個容易被誤判為配方問題的事件觸發條件；QA新增CAF-017。
- 玩家討論串出現的電話號碼不視為通用常數，仍應讀取遊戲內便條。


## 2026-11-17｜Critic 初審結果
- 已檢查專案主要規格文件與交叉一致性；26項成就矩陣完整，333筆候選盤點、312筆命名翻譯與21個Rat符號槽位的分類邏輯一致；QA目前132個唯一測試ID，均為設計案例，尚未執行。
- 修正README來源範圍與Cafe QA ID命名。
- Bistro Pizza Dough = Olive Oil + Yeast + Flour取得兩份獨立指南支持；Goulash、Tomato Cocktail仍受官方v1.1修正影響，精確新配方未知。
- 初審不通過正式全內容開發 Gate。主要阻塞：七國料理／老鼠請求順序、Cafe完整To-Do、Rat密碼與電力映射、逐筆配方來源追溯、D級衝突與實機QA。
- Research Only維持；Critic初審不是最終審查，待研究資料補齊後再做第二輪。


## 2026-11-17｜Rat Level 截圖審查補充
- 已檢視日文 1.0通關文的Rat Level嵌入截圖，確認場景包含電器罐、控制面板、數字便條區與紅框投幣目標；截圖不足以還原通用三位數密碼或OFF/ON與強弱電力映射。
- 藍框開關與紅框投幣目標可見，但官方成就條件仍是同面連續三次；操作關係留待實機驗證。


## 2026-11-17｜SRC-017 1.0指南重新審查
- 修正先前來源判讀：Steam Guide ID 3686619896頁面標題為v1.0全成就指南（9/8更新），雖保留v4.0 EA舊章節，正文仍含Bistro與Rat Level。先前稱其不含第三關的結論撤回。
- 新增Rat Level候選：冷Good #5 = Cheese + Leaf；Bad #4 = Eggshell + Pencil；Bad #6 = Pasta；Bad #7 = Pasta + Paper。與SRC-050快取指南衝突，新增RAT-016至RAT-019逐項測試。
- Clutter新增1.0指南候選 Cloth + Wooden Spoon；新增Bistro配方衝突測試BIS-041至BIS-047。
- Goulash與Tomato Cocktail已取得1.0候選配方，不再列為完全未知；v1.1後仍需回歸驗證。
- QA總數更新為132個唯一案例，均為設計，尚未實際執行。


## 2026-11-17｜新增 SRC-052 Rat Level 交叉證據
- 新增第二份獨立Rat Level攻略SRC-052，完整列出9 Good / 12 Bad槽位與解謎順序。
- SRC-050、SRC-052、9Puz三方支持Cold Good #5 = Cheese + Eggshell；Bad #4 = Eggshell + Pencil；Bad #6 = Paperclip + Pasta；Bad #7 = Eggshell + Paper。SRC-017 1.0手打指南的Leaf／Pasta變體保留為對照，不再優先。
- Coioioin重複點擊硬幣符合官方成就文字；藍開關／紅框投幣仍作替代路徑。三位數密碼未公開，仍未知。
- 來源登錄擴至SRC-052，QA維持129個唯一測試案例。


## 2026-11-17｜新增 Mochi 與 Yeast Monster 配方衝突
- SRC-017 1.0手打指南將日本Mochi列為Ground Rice；SRC-015/SRC-050列為whole Rice，已加入配方衝突表與BIS-048。
- Yeast Monster在SRC-017（Yeast+Wooden Spoon）、SRC-015（Yeast+Wine）、SRC-050（Yeast+Tomato）三份候選間衝突，新增BIS-049。
- QA總數由127增為132個唯一測試ID，均尚未實際執行。


## 2026-11-17｜Bistro / Cafe 任務鏈再核對
- 重新逐行讀取SRC-023日文Level 3通關文與SRC-047 1.0完整路線：Bistro To-Do起始順序為Clean the kitchen → Trade with the rat；老鼠初次收Cheese後給Tomato，後續依抽油煙機便條料理換取食材。
- 9Puz補強工具依賴：空Mixer容器煮出Scissors、Scissors找出隱藏Mixer開關並剪斷吊掛食材繩；老鼠請求提供特殊食材與七國磁鐵；五瓶酒需依標籤排序。
- 七國菜仍只有Japan=Mochi有文字證據，其他六道不能猜。Cafe To-Do已確認包含Set the kitchen on fire，Burnt Panini再次烹煮觸發火災；完整任務清單仍缺。
- Critic P1仍未清除；QA 132項均未實機執行。


## 2026-11-17｜Bistro老鼠贈品鏈補證
- SRC-050完整指南註記：Olives是Tomato Cheese Appetizer所需的老鼠贈品、Apple是Baked Apple的老鼠贈品、Garlic是Pumpkin Soup的老鼠贈品；SRC-023確認初次Cheese→Tomato及便條料理換食材機制。
- 這補足了部分受限食材清單，但仍沒有每張請求便條的順序與獎勵對照，P1-01未解除。QA新增BIS-050至BIS-052，總數132個唯一ID，均未執行。
