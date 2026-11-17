# Little Chef 復刻｜工作日誌與決策紀錄

更新日期：2026-11-16  
用途：供專案負責人檢查我做過哪些判斷、依據、疑慮與修正。這是整理後的工作紀錄，不是逐字私人思考過程。

## 2026-11-16｜重新接手 GitHub 專案
**觀察**
- 使用者要求研究成果保存到 Bonnie9981/AI-little-cheft。
- 前次寫入曾回傳 403，但重新嘗試後 create_file 已成功。
- 根目錄存在名為「？」的測試檔，讀取後確認內容只有換行。

**行動**
- 刪除使用者指定的測試空白檔。
- 建立 README.md、內部交接與進度匯報。
- 重新讀取 GitHub 根目錄與 docs 目錄，確認檔案實際存在。

**判斷**
- 不應再把寫入失敗歸咎於使用者未開權限；應以當下實際 API 回應為準。
- 只刪除使用者明確指定的測試檔，不擴大清理範圍。
- 後續以 GitHub 作為專案主紀錄，不只依賴聊天上下文。

## 2026-11-16｜釐清工作日誌需求
**觀察**
- 使用者要一份供我延續工作的內部紀錄，以及一份給使用者閱讀的進度與時間線。
- 使用者特別補充希望看到「我的內心獨白」。

**行動**
- 將可提供的版本定義為工作日誌／決策紀錄：記錄觀察、證據、疑點、選擇、風險與下一步。
- 不宣稱能逐字輸出私人思考過程；以可審查、可追溯的理由說明代替。

**判斷**
- 對專案負責人真正有用的是能追蹤「為什麼做這個決定、根據什麼、還有什麼不確定」的紀錄。
- 工作日誌和進度報告應分開：前者偏決策脈絡，後者偏交付狀態。

## 2026-11-16｜重新查證 Bistro 配方
**觀察**
- 先前 Bistro 清單存在缺漏；部分配方來自社群攻略，不是官方配方表。
- 新搜尋找到 Steam Guide ID 3713640352，搜尋索引顯示內容更新至 2026-08-10，並提供 Bistro 章節配方。
- 但 Steam 頁面不同快取版本顯示的更新日期不一致；某次頁面正文顯示 2026-04-25，與搜尋索引的 2026-08-10 不同。

**行動**
- 補入社群指南列出的候選配方：Beef Wellington、Garlic Powder、Meat Sandwich、Apple Cider、Garlic Bread、Kombucha、Goulash、Pumpkin Seeds 等。
- 每筆仍標記 community-reported，不提升為 verified。
- 將 Goulash 的 Meat + Wine + Ground Tomato 記為候選線索。
- 將 Tomato Cocktail 精確組合列為待查，不自行猜配方。

**判斷**
- 同一 Steam Guide 的搜尋摘要與頁面快取不一致，不能假裝已完整讀取同一版本。應保留 URL、抓取日期與證據級別，並找其他來源交叉核對。
- v1.1「修正食譜書資料」不等於該組合從未改變，也不等於所有社群配方都正確。
- 食譜資料模型必須記錄材料加工狀態，例如 Ground Tomato，而不是只記 Tomato。

## 2026-11-16｜Rat Level 狀態建模
**觀察**
- 社群攻略指出 Rat Level 有冷爐與熱爐兩套結果；相同材料組合可能因烤箱狀態不同而產生不同結果。
- Eggshell 與 Leaf 的第五個冷爐配方線索存在衝突。

**行動**
- 將 oven temperature/state 納入 RecipeConditions。
- 將 Eggshell/Leaf 記為待驗證候選，不硬選其一。
- 記錄反重力開關、花盆紙條、酒瓶標籤、三位數密碼、開啟爐火的解鎖順序。

**判斷**
- 若資料庫只儲存「材料 A + 材料 B」，會遺失此關最重要的狀態條件。
- 後續 QA 應測試同一組合在冷爐與熱爐下的輸出差異。

## 目前總體判斷
1. 研究內容已累積不少，但目前仍有相當比例是攻略線索，不能把研究進度等同實機驗證。
2. 最大返工風險在配方狀態、解鎖前置條件、版本差異與隱藏互動。
3. 我傾向先把食譜資料庫做成可追溯的結構化資料，再進入視覺與互動實作。
4. 不應為了看起來有進展而過早做不完整 Demo；這會讓後續規則改動成本變高。
5. 下一個研究優先序：Bistro 缺漏與官方修正項 → Rat Level 冷熱配方 → Student Dorm/Cafe 全量清點 → 互動與物理規格 → QA → Critic。

## 日誌更新規則
每次有明確研究進展時，追加日期、觀察、來源、行動、判斷、未解問題與下一步。若發現先前結論錯誤，保留修正紀錄，不直接抹掉舊判斷。


## 2026-11-16｜Goulash／Tomato Cocktail 配方交叉核對
**觀察**
- 先前已知 Goulash 配方存在 Meat／Ground Meat 與 Tomato／Ground Tomato 的混淆。
- 新找到的玩家討論串中，最初回報把「processed meat」與番茄混淆，後續玩家明確更正為一般 Meat + processed Tomato + Wine；並確認 Risotto 與 Focaccia。
- 更新版 Bistro 攻略索引列出 Tomato Cocktail = Olives + Wine + Ground Tomato，且列出更多先前清單漏掉的菜餚。

**行動**
- 將 Goulash 候選修正為 Meat + Ground Tomato + Wine。
- 將 Tomato Cocktail 候選補為 Olives + Wine + Ground Tomato。
- 補列 Mushroom Soup、Apple Mochi、Croque Monster、Pumpkin Soup、Tomato Juice、White Wine、Pumpkin Bread、Hamburger、Apple Sauce、Olive Oil、Rosé、Vegan Sandwich、Pumpkin Fries、Meatloaf、Pizza、Italian Rice Balls、Schnitzel、Meat Lover Pizza。
- 保留來源等級為社群攻略／玩家回報，等待遊戲實測或更多獨立來源。

**判斷**
- 這次查證修正了一個很容易造成資料庫錯誤的核心混淆：Ground Meat 和 Ground Tomato 不是可互換的狀態。
- 這也驗證 RecipeInputs 必須包含 item_state / processing_state，而不是只有 ingredient_id。
- 官方 v1.1 修正 cookbook 的公告提供版本證據，但配方本身仍由社群討論與指南提供候選組合。


## 2026-11-16｜擴充來源：Bistro Guide 與 Rat Level 完成路線
**觀察**
- 新找到 Steam 社群 Bistro Guide（ID 3764982550），包含 Good Recipes、Bad Recipes、Blender Switch、Secret Achievements 等完整章節摘要。
- 新找到 9Puz 於 2026-09-02 發布的完成路線指南，整理三主廚房、Rat Level、26 項成就及狀態錯誤排查。
- Pixel Questing 搜尋摘要聲稱 Student Dorm 有 48 good recipes、29 bad recipes，但原頁本次無法直接開啟。

**行動**
- 將新 Bistro Guide 的食譜與壞食譜納入候選資料集，來源欄標為 community guide。
- 將剪刀解鎖線索（Mixer jar 放入 pot）與 Blender switch（剪刀靠近植物葉片）補入互動研究。
- 將 Rat Level 冷熱爐、反重力、花盆密碼、酒瓶標籤與冷爐五項／熱爐四項的狀態差異納入測試設計。
- 將狀態建模擴充到 Toast、Burnt Toast、Soggy Toast、Filled Espresso Cup、Mixer outputs、oven temperature。
- Student Dorm 48 good / 29 bad 先記為待核實數字，不當作完成計數。

**判斷**
- Bistro 的第二份攻略與先前 8/10 指南對多個關鍵配方相互支持，尤其 Goulash、Tomato Cocktail、Focaccia；可提升為「多來源社群支持」，仍不是官方配方證明。
- 來源之間對某些配方仍有分歧（例如是否需要 Olives、是否要先 Ground Rice、Ground Beef 或一般 Meat），必須將「配方組合」與「加工狀態」分欄，逐項保留證據。
- Rat Level 不應用翻譯後的菜名做唯一識別；用 slot index、inputs、temperature state 與 output state 較可靠。

**下一步**
- 建立 Bistro recipe matrix，逐項比對 Guide 3713640352、Guide 3764982550、9Puz、Steam 討論與官方 changelog。
- 對 48/29 數字與 Cafe 配方數找可直接讀取的來源。
- 完成 Rat Level slot-by-slot 的冷熱表及 puzzle state machine。


## 2026-11-16｜Cafe Job 版本差異與完整食譜線索
**觀察**
- 新版 Steam Guide 搜尋索引取得 Chapter 2 完整 Good/Bad Recipes，並明確標示更新至 2026-08-10。
- 同一 Guide 直接開啟頁面顯示舊版快取，與搜尋索引版本不一致；故本次採搜尋索引內容作研究線索，並保留版本不確定性。
- 新版清單明確指出 Tiramisu 使用 Filled Coffee Cup，不是 Coffee Beans；Double Espresso 也依賴機器內已裝滿的杯子。
- 新增 Canned Coffee = Coin + Cup of Espresso；Mocha 與 Strawberry Latte 使用 Espresso Shot；Dirty Chai Latte 使用 Coffee 而非 Coffee Beans。

**行動**
- 將 Cafe 前置製作補入：Paper Cup、Strawberry Cake、Chocolate Cake、Panini、Photo。
- 將 Cheese → Cafe rat → 紙片進電話 → 依便利貼號碼撥號 → 解鎖 Avocado/Lettuce 的流程拆成明確任務節點。
- 把 Coffee Beans、Espresso Shot、Filled Coffee Cup、Cup of Espresso 拆成獨立 item/state。
- 把 Paper、Paper Cup、Cup of Espresso 拆成獨立物件。
- 補入 Canned Coffee、Mocha、Strawberry Latte、Dirty Chai Latte 等配方的新版候選資料。
- 補入 Student Dorm 的 Tomato/Egg Stir Fry 新配方。

**判斷**
- Cafe 的主要資料風險不是食材組合，而是咖啡設備狀態：豆子、萃取中的杯子、已裝滿的杯子會觸發不同配方。
- 若只將 Espresso 當成一種材料，會無法還原 Tiramisu、Double Espresso、Canned Coffee 等流程。
- 8/10 指南比 4/25 舊版增加了更新後的 Bistro 與 Cafe 修正，但頁面快取不同步，應以來源日期與具體段落做證據追蹤，不可只看頁面顯示日期。

**下一步**
- 將 Cafe 所有 Good/Bad Recipes 逐筆轉為表格，標示設備、加工狀態、可替代材料與版本。
- 釐清 Cafe 的訂單／Coin 發放、Photo、Safe、Security Card、Void Bagel 等完整任務鏈。
- 對 Student Dorm 新配方與舊配方做差異表，補上 1.0 後是否仍存在的證據。


## 2026-11-16｜Rat Level bad recipes 與 Bistro 衝突項盤點
**觀察**
- 更新版 Steam Guide 索引明列 Rat Level 冷爐五項、熱爐四項與 Bad Recipes 清單。
- Eggshell 取得方式是多次點擊 Egg 使其裂開；Bad Recipe 清單中 Egg + Pencil 與 Eggshell + Paper 分屬不同項目。
- 9Puz 仍提示第五個冷爐圖示有 Eggshell / Leaf 文字衝突，代表不能只憑翻譯菜名定義 slot。
- 可直接讀取的 Bistro Guide 正文列出 76 Good Recipes、31 Bad Recipes；作者留言確認 Goulash 需要 Ground Tomato。
- Bistro 來源仍有 Tomato Cheese Appetizer（含不含 Olives）、Apple Mochi（Rice 或 Ground Rice）等差異。

**行動**
- 將 Rat Level Good Recipes 按 oven_state 分開建模；Bad Recipes 按 exact inputs / item state 建立。
- 將 Eggshell 作為 Egg 的獨立可取得 item state，不能把 Egg 與 Eggshell 合併。
- 將 Bistro Tomato Cheese Appetizer、Apple Mochi 等衝突配方加入 RecipeEvidence conflict queue。
- 將作者留言作為配方交叉證據，並保留它是社群作者回覆而非官方資料的來源層級。

**判斷**
- Rat Level 的第五個冷爐項目與 Eggshell/Leaf 衝突，最可靠的處理方式是以 slot 是否完成為判斷，而不是在資料庫裡提前猜測。
- 來源清單可用來建立初始候選，但只有逐條成功解鎖或有多個獨立一致來源，才可提高 confidence。
- Bistro 的 Good/Bad 數量仍需和更新版 8/10 清單逐條比對；單一 7/14 指南不是最新完整資料。

**下一步**
- 建立 Bistro 的 recipe reconciliation 表：recipe_id、guide_7_14、guide_8_10、player_comment、official_patch、candidate_inputs、state、confidence、status。
- 將 Rat Level 13 項 Bad Recipes 做成逐項 QA，不將「空爐冷／熱」合併成錯誤的單一狀態。
- 繼續查詢 Student Dorm / Cafe 的成就和任務流程，尤其订单、coins、安全箱、火警與相框。


## 2026-11-16｜Cafe 訂單經濟、電話與 Safe 依賴鏈
**觀察**
- 開發者直接回覆 Steam 玩家：Cafe 牆上的圖像訂單完成後會給 tip coin；已完成的訂單可以從牆上取下，之後會再出現新訂單。
- v3.0ea 官方更新新增訂單系統與 To Do「complete 8 orders」，同時新增 18 道 Cafe 食譜、espresso machine、提示系統與 25 個電話號碼。
- 開發者另確認 Safe 需要先製作 keycard；玩家攻略具體列為 Photo + Coin。
- Pixel Questing 搜尋摘要補出 Safe 位於相框後、Void Bagel 由三個 Bagel 在烤箱製作，完成後在 Safe 內取得。
- 日文玩家攻略指出 Cafe 累積硬幣可用於 My Room 裝飾；20 枚硬幣可解鎖畫筆。

**行動**
- 將訂單拆成 OrderTicket、OrderCompletion、TipCoin、ToDoCounter 四個概念。
- 將電話解鎖 Avocado/Lettuce 記成 puzzle chain，而非單一解鎖按鈕。
- 將 Safe 的依賴鏈記成 Photo → Security Card（Photo + Coin）→ Safe unlock → Void Bagel discovery。
- 把「做出三個 Bagel 丟進 oven」與「在 Safe 找到 Void Bagel」拆成 recipe discovery 與 item reveal 兩個步驟。
- 把 My Room 裝飾與 Cafe 訂單收入連結列入支線研究。

**判斷**
- Cafe 的經濟循環至少同時服務食譜、Safe 解鎖、8 orders To Do 與 My Room 裝飾；不能只把 Coin 當作一個食譜材料。
- 25 個電話號碼與電話互動可能有彩蛋／隱藏用途；不能只保留 Avocado/Lettuce 那一個號碼。
- Coin 來源與消耗需要單獨設計；若實作成無限生成，會破壞版本中的經濟限制與裝飾解鎖。

**下一步**
- 查明 25 個電話號碼各自功能與版本變更。
- 查明 8 orders To Do 的完成條件、訂單刷新與 coin 累積上限／重複規則。
- 整理 My Room 裝飾物、可互動家具、存檔欄位。


## 2026-11-16｜修正 Bistro 解鎖條件與版本差異
**觀察**
- 先前資料把 Bistro 開啟簡化為「把 Cafe 燒起來」。但官方 v5.1ea 公告明確指出：進入 Level 3 前必須先完成 Level 2 的 To-Do list，並有一項新增食譜。
- v4.0ea 官方 My Room 更新列出裝飾系統、20 Coin 畫筆解鎖、存檔自訂項目、書本排列成就、主選單 logo 成就與舊成就移除。
- v4.1ea 說明 Coin 掉落後會重生、Canned Coffee 也能用 Coin 製作。
- v5.4ea 加入 Level 3 食譜提示與一鍵清除 new stars。

**行動**
- 將解鎖規格從「fire event → Bistro」修正為「Level 2 To-Do complete → Level 3 available」。
- 保留 fire event 為 Cafe 互動／成就與可能的 To-Do 項目，但不再把它視為單獨充分條件。
- 在版本時間線補入 v4.0ea、v4.1ea、v5.1ea、v5.4ea 與 1.0、v1.1。
- 將 My Room customization、coin bank、20 Coin paintbrush、post-it、book arrangement、saved decor state 納入 My Room 規格。
- 移除 Master Chef / Master of Disaster 這兩個已刪除成就，不把它們放入 26 成就清單。

**判斷**
- 對忠實復刻而言，Early Access 的章節入口條件不能只憑舊攻略；官方版本公告應優先。
- Bistro 入口需要 To-Do 任務系統，不能只用一個布林值「Cafe burned」。
- My Room 不只是選關畫面，而有存檔的個人化狀態與成就任務。

**下一步**
- 取得 Level 2 To-Do 的完整項目表，確認 8 orders、rat trade、fire、電話、訂購、其他互動的依賴關係。
- 建立 My Room 的可互動物件、裝飾項目、unlock thresholds、save fields 表。


## 2026-11-16｜補完 Level 2 To-Do 與 Bistro rat 任務線
**觀察**
- 日文玩家 2026-09-09 的 Level 3 通關紀錄詳細描述了 Level 2 To-Do 的完成順序：清理 Cafe、Trade with rat、處理料理與訂單、製作 Burnt Panini、再次烹煮引發火災、撲滅火災，完成剩餘訂單後回到 My Room 解鎖 Bistro。
- 這與官方 v5.1ea「完成 Level 2 To-Do 才能進 Level 3」完全一致。
- Bistro rat 位於抽油煙機；第一次給 Cheese 會開啟任務線，後續每次製作便條圖示料理可換新食材。
- 七國料理會使磁鐵貼在抽油煙機，全部完成取得 Going Global。
- Mixer 修復點在右側花盆電路板；Apple 可分 whole / crushed 狀態，對應 Baked Apple / Apple Sauce。

**行動**
- 把 Bistro unlock 條件改成 Level 2 To-Do completion，不再只寫火災。
- To-Do 至少列出 Clean the kitchen、Trade with the rat、Complete 8 orders、Set the kitchen on fire；由於完整 UI 清單尚未直接讀取，標註至少。
- 將 fire state machine 拆為 Panini → Burnt Panini → fire → break alarm glass ×3 → press exposed button → fire extinguished。
- 將 Bistro rat trades 記成有序任務節點；每張 note 需對應指定 recipe / reward ingredient。
- 把七國料理、磁鐵與成就獨立成一張關聯表。
- 把 Mixer repair、ground produce、overload achievement、five-wine sorting 加入互動流程規格。
- 將 25 個電話號碼與電話彩蛋列為支線，不與 21931 的主要食材訂購號碼混淆。

**判斷**
- Level 2 To-Do 是多任務條件，不是一個單獨事件。使用者要求忠實復刻，因此任務系統必須保存各 task 的狀態與完成順序。
- Bistro 的老鼠不是一次性的食材商店，而是分階段的任務發布者；每次 reward 解鎖新的 recipe branch。
- Mixer 不只是烹煮前處理器，亦是關卡 puzzle / achievement 的核心互動物件。

**下一步**
- 找出完整七國料理對照表、每個 rat request 的 recipe 與 reward。
- 將 To-Do 的所有項目逐一列出並建立可測試條件。
- 查證 My Room 的 20 Coin 裝飾、Piggy Bank 任務是否也是 Level 2 To-Do 的獨立支線。


## 2026-11-16｜物理互動規格與七國料理資訊缺口
**觀察**
- 官方 Steam 商店與新聞稿清楚描述拖曳、拋擲、輕放、混合、碰撞／破壞等物理互動；所有物件有重量與運動表現。
- SteamDB 功能列表包含 Mouse Only Option 與 Touch Only Option，證明原作有滑鼠與觸控輸入模式。
- Student Dorm 有明確依賴物理的成就：把物件拋到畫面上方、香蕉空中切割、放水淹沒廚房、茶盒排列。
- Bistro 的七國料理清單尚未找到完整文字來源，只能確認其中一個日本料理 Mochi，其他六項不可憑菜名推測。

**行動**
- 將物理規格拆成 pointer/touch grab、drag、throw/release impulse、collision、stacking、breakable、water buoyancy、container insertion、cutting、machine processing。
- 將滑鼠／觸控設計成共用的 interaction abstraction，桌面與手機橫向使用同一套物件狀態和碰撞邏輯。
- 將每個物理任務改寫成可觀察 QA：物件越過畫面上界、香蕉切割時處於空中、液面到達指定區域、茶盒圖案連續。
- 將七國料理對照表列為高優先未解問題，不用七個「看起來像異國料理」的名稱湊數。

**判斷**
- 原作物理手感是核心特色，不是裝飾動畫；如果只做拖放配方表，復刻會失去遊戲核心。
- 原作數值（質量、摩擦、彈性、重力、拖曳阻尼）沒有可靠公開資料，不能聲稱複製原始係數；本專案需做可調且經 QA 校準的近似模型。
- 七國料理是明確成就與支線條件，若未整理清楚，Bistro 任務線仍不能宣告完成。

**下一步**
- 尋找七國料理的遊戲截圖／完整通關影片或不同語言攻略，逐一確認磁鐵與料理對應。
- 建立物件互動矩陣，列出每個物件可被拖曳、拋擲、切割、碰撞、放入容器、加工、破壞的能力。
- 明確定義手機橫向手勢與觸控命中區。


## 2026-11-16｜Student Dorm 1.0 To-Do 與食譜更新差異
**觀察**
- 找到 Pixel Questing 2026-10-09 的 Chapter 1 全攻略，明列 48 Good / 29 Bad、24 個場景物件、完整 To-Do 和配方表。
- To-Do 至少包含 8 道 pasta dishes、借用 Shane's Cheese、播放 red/green/Remix 三卷磁帶、清洗與整理餐具以解鎖 coffee maker、澆灌 basil、累積 40 道新料理。
- 新版配方與 8/10 Steam guide存在多項差異：Beans on Toast、French Toast、Savory Sandwich、Tomato Soup、Pasta Carbonara、PB&J Sandwich 等。
- 指南指出所有 Good Recipes 與 To-Do 完成後才能進 Chapter 2；Bad Recipes 可能非必需，但這是作者推測。

**行動**
- 將 Student Dorm To-Do 拆成可獨立計數的 6 個任務狀態。
- 將 24 個場景物件納入 Item / Interactable inventory。
- 在 RecipeEvidence 登記所有新舊配方差異，不以單一攻略覆蓋舊資料。
- 將 Shane locker puzzle（D2）做成可重現的 tile-grid state machine。
- 將 coffee maker 的出現條件拆成 dirty dishes cleaned → utensils placed → machine revealed → stove interaction。
- 將 basil 的 watering path 同時支援 wet sponge 與 flood height 兩種方式；Flooded achievement 另記。

**判斷**
- Student Dorm 的主線解鎖不只看食譜數量，還依賴 6 類任務；若只做 cookbook，章節不會前進。
- 新版攻略對配方有可觀察狀態細節，但仍是單一社群來源；所有變更需先標記 candidate，不要覆蓋多來源證據。
- 「Bad recipes 似乎 optional」不能當作遊戲規則；需用 1.0 實際流程或官方資料確認。

**下一步**
- 把 48 Good / 29 Bad 逐筆對照 Steam 8/10 guide，標記每項配方的 recipe-state、替代輸入與來源版本。
- 尋找 Student Dorm To-Do 是否確實只有 6 項，及 Bad Recipes 是否會影響 100%。
- 確認三個 locker 的位置、內容與解鎖方式。


## 2026-11-16｜Cafe Job 1.0 配方總量與新版攻略衝突
**觀察**
- 找到 Pixel Questing 2026-11-09 Chapter 2 全攻略，列出 71 Good / 41 Bad，場景物件 37 項。
- Good list 有 Coffee Cake 重複列兩次；去重後 71 個名稱。
- 新攻略與 8/10 Steam guide有明顯差異：Tiramisu、Babyccino、Hot Cocoa、Latte、Canned Coffee、Dirty Chai Latte、To Go Drink、Bento Box 等。
- 官方 v4.1ea說明 Canned Coffee 可以使用 Coin；9/2 9Puz與 8/10 Steam guide都明確把 Espresso cup state用於咖啡配方。

**行動**
- 將 Cafe 候選總數更新為 71 Good / 41 Bad（以 11/9攻略為新來源，待遊戲內 counter 確認）。
- 將 Coffee Cake duplicate標記為 source duplicate，不建立第二筆。
- 將新指南的配方逐項加入 RecipeEvidence conflict queue。
- 將 21931電話號碼的完整互動補上「撥號後拿起 handset 並等對方講完」的開發者確認條件。
- 將 Coin 與 OrderTicket分開建模：訂單完成生成 Coin；Coin可以作為 recipe input與解鎖資源。
- 保留官方 v4.1ea、8/10 Steam guide、9/2 9Puz作為較高優先級的 release evidence。

**判斷**
- Cafe 的 Good/Bad recipe總數目前有新資料支持，但仍需與遊戲內 recipe folder counter核對。
- 11/9攻略可能混用不同設備與不同版本配方；不可只因日期較新就取代官方 patch與多來源一致的配方。
- Tiramisu 的 11/9版本 Cheese + Plain Cake + Coffee Beans 與 8/10版本 Filled Coffee Cup + Cake + Milk差異巨大，屬高優先實機測試。

**下一步**
- 建立 Cafe 71/41逐條清單與來源對照，清除重複 Coffee Cake。
- 對 Tiramisu、Babyccino、Hot Cocoa、Latte、Canned Coffee、Dirty Chai Latte、To Go Drink、Bento Box做逐個狀態與設備測試。
- 取得 Cafe 8個 ToDo的完整任務名稱與順序，不能把「8 orders」誤當成「8個 ToDo條目」。


## 2026-11-16｜Cafe To-Do 數量語意重新核對
**觀察**
- 官方 v3.0ea 寫的是單一 To-Do：「complete 8 orders」。
- 日文玩家將其描述為「ToDo list新增8件」，可能是指八張訂單的計數，而非八個獨立任務條目。
- Level 2 解鎖攻略確定包含清潔、老鼠交易、火災／滅火、訂單等任務，但未提供完整 UI 清單。

**行動**
- 修正 handoff / progress 的語意：只確認 order target = 8；To-Do task count = unknown。
- 保留 4 個可確定的任務類型作最低集合，不再聲稱全部八個 task name 已找齊。

**判斷**
- 以官方 patch note為優先來源；社群翻譯中「8件」不可直接解讀為八個獨立任務。
- 完成 8 orders 應是 Level 2 To-Do 的一個計數型目標，需與訂單票數／Coin發放機制整合。

**下一步**
- 尋找遊戲內 To-Do UI 截圖或 1.0 實機影片，確認 Level 2 任務總數、每項文字與完成條件。


## 2026-11-16｜Rat Level 的「冷熱爐」模型修正為電力高低
**觀察**
- 日文玩家 2026-09-10 的 1.0 完成攻略指出，Rat Level 的烹調設備是通電罐頭，類似微波爐；酒瓶機關解鎖後可調整電力輸出強／弱，同一配方因電力不同產生不同料理。
- 8/10 Steam Guide將食譜分成 oven OFF / ON；這是社群攻略對設備狀態的簡寫，未必代表一般烤箱的冷／熱溫度。

**行動**
- 將 Rat Level 設備改名為 ElectricCanCooker。
- 將 RecipeCondition從 oven_temperature 改為 power_level = low | high。
- 將 OFF/ON來源記錄成 source_state，等待與遊戲內控制開關映射核對。
- 三位數密碼只記錄為 planter note clue，沒有文字來源就不猜實際數字。

**判斷**
- 復刻若把 Rat Level做成普通烤箱，會錯失最重要的機制：同樣輸入受電力輸出狀態影響。
- 目前 low/high與 OFF/ON 的映射仍需實機畫面驗證，不能直接假設 ON=high。
- Rat Level 的設備名稱、狀態與 puzzle gate要分開建模。

**下一步**
- 找到 planter note的圖片／清晰畫面，辨識三位數密碼。
- 確認 power toggle UI、兩種狀態下的食譜 counter、是否有 power-off / power-on 兩種結果。


## 2026-11-16｜Bistro 1.0 追加食譜與 Rat Level 成就觸發
**觀察**
- 1.0 玩家 9/10 通關記錄稱 Bistro 新增約 10 項食譜，最後 Good Recipe 是 Mini Pizzas，最後 Bad Recipe 是 Clutter。
- 8/10 Steam guide已列出 7 Good + 2 Bad新增食譜；結合 9/10記錄，可推測 Clutter是第 10 項、第三個 Bad Recipe。
- Clutter描述提及「物件自己變亂」，但尚未找到確切製作條件。
- Coioioin的玩家實測流程不是純隨機：先按藍色開關，再投擲紅色區域的硬幣。
- 1.0玩家報告遊戲內取得 Coioioin後，重啟遊戲才同步Steam achievement。
- 1.0通關後 My Room會出現生日蛋糕與媽媽的信，蛋糕可開關蠟燭。
- Set the kitchen on fire To-Do在某些1.0存檔可能顯示未完成，重做一次點火後才更新。

**行動**
- 把 Bistro 新增食譜列為 7 Good + 3 Bad候選，Clutter狀態設為 unresolved。
- 把 Coioioin改成「藍色開關 → 投幣」互動鏈，不用隨機連續拋三次的假設。
- 把 birthday cake、letter、candle toggle加入 My Room post-game interactables。
- 將 To-Do completion、achievement unlock、Steam sync拆成不同狀態。

**判斷**
- 1.0的 Clutter是新增 Bad Recipe，不應只把 Messing Around當成achievement而忽略 cookbook entry。
- Coioioin有明確機關條件，若復刻成純隨機機率，會不忠實。
- My Room在主線結束後仍有可互動內容，不能在三個廚房100%時直接視為靜態結局畫面。

**下一步**
- 找出 Clutter的觸發條件與是否由 Mixer mess直接產生。
- 查明生日蛋糕信件的解鎖門檻與存檔狀態。
- 核對 1.0 Bistro 10個新增 recipe在實際 counter中的分佈。


## 2026-11-16｜Bistro 76/31 是 EA baseline，不是 1.0 總量
**觀察**
- 直接打開 7/14 Bistro Guide正文，逐行核算確為 76 Good / 31 Bad。
- 8/10更新版 Steam Guide明列 8/27新增 7 Good + 2 Bad。
- 9/10正式版玩家通關記錄另確認 Clutter為最後一個 Bad recipe，並表示 Level3新增約10個配方。

**行動**
- 將 76/31標記為 7/14 EA baseline。
- 1.0候選總量調整為 83 Good / 34 Bad，計算為 76+7 Good、31+2+1 Bad。
- 將 Clutter列為 1.0新增 Bad候選；formula仍 unresolved。
- 更新 timeline與 progress，避免再把 76/31寫成最終 Bistro 數量。

**判斷**
- 這是目前最能解釋來源日期差異的分期模型，但 83/34仍屬跨來源推算，不是官方確認。
- 必須在實機或可讀 cookbook counter取得總量後，才能將此數字標為 verified。

**下一步**
- 找到 1.0 cookbook counter截圖或影片，確認 Bistro Good/Bad總量。
- 逐筆比對 7/14 baseline與 8/27新增項目，檢查是否有被刪除／替換的舊 recipe。


## 2026-11-16｜Bistro Rat Trade 任務鏈查證
**觀察**
- 開發者 Steam 回覆直接說明：先找到抽油煙機可疑門，給 Cheese啟動任務；之後老鼠展示料理圖，完成料理換取新食材。
- 日文玩家通關紀錄確認首次 Cheese交易取得 Tomato；後續依序有圖畫便條與新食材獎勵。
- 9Puz指出 Apple、Olive、Garlic等支線材料需要從 mouse-gift chain取得。
- Going Global有 7道國家料理；Mochi是已明確辨識的日本料理，其他六道沒有可讀文字來源。
- 老鼠完成所有請求後顯示愛心，玩家確認這是 thank-you note，不是額外食譜請求。

**行動**
- 將 rat trade改為狀態機，不做成一次性商店。
- 將 first reward tomato、後續 Apple/Olive/Garlic gift、request note與 heart completion分別記錄。
- 七國料理與 rat request分開建表；magnet collection count 0..7。
- 將愛心圖示定義為任務完成回饋，不觸發新 request。

**判斷**
- 這條任務線同時負責解鎖材料、成就 Best Friends與七國磁鐵；不能用 recipe count替代。
- 目前只知道 Mochi屬日本料理，其他六道必須有圖片／實機證據才可定案。

**下一步**
- 追查老鼠每張 request note對應的 recipe與 reward ingredient。
- 找到七個 magnet的圖案／國旗或對應菜名；沒有證據的六項保持 unknown。
- 確認最後愛心是否所有交易都完成，以及是否同時解鎖 Best Friends。


## 2026-11-16｜建立台灣繁體中文詞彙基準
**觀察**
- 官方 Steam繁中頁面仍標示不支援繁體中文，只有英文、德文、簡體中文。
- Simplified Chinese攻略有一批可參考譯名，但包含「芝士、土豆、耗子」等非台灣用語。
- 台灣烘焙／餐飲來源支持佛卡夏、法式熱三明治、古拉什等譯法；遊戲本身的料理名稱需兼顧台灣理解與原作玩笑。

**行動**
- 建立 docs/ZH_TW_GLOSSARY.md。
- 將 Good/Bad Recipes暫譯為「美味料理／怪奇料理」。
- 採用「起司、馬鈴薯、可頌、吐司、披薩、果昔、調理機」等台灣常用詞。
- 對少見專名採「音譯＋短說明」，並保留英文 key。

**判斷**
- 不能只做簡繁轉換；簡體指南的料理名稱有錯誤或不符合台灣用語。
- 每個加工狀態都要有獨立詞條，避免 Ground Tomato與 Tomato都顯示成番茄。
- 本版只是 glossary draft，待全量 recipe inventory完成後還要統一用字、字數與 UI寬度。

**下一步**
- 補齊所有 Bad Recipe、Rat Level與 My Room詞彙。
- 校對中文 recipe names與英文食材名的對應，尤其 Goulash、Khachapuri、Meatloaf、Clutter等。
- 建立 zh-TW QA：無簡體字、無中國大陸詞彙、無重複譯名、UI不溢位。


## 2026-11-16｜1.0 簡體中文成就攻略交叉核對
**觀察**
- 找到 2026-09-01 更新的 1.0 全成就中文攻略；作者明確提醒遊戲更新可能改變配方。
- 該攻略補出 Clutter = Cloth + Spoon候選，並把 Rat冷爐第五項列為 Cheese + Leaf；這與 8/10英文攻略的 Eggshell衝突。
- Rat bad slot也有差異：Eggshell + Pencil vs Egg + Pencil；Pasta單獨、Pasta + Paper vs Paperclip + Pasta。
- Bistro另有多筆配方差異：Mochi、Apple Mochi、Kombucha、Tomato Juice、Fried Rice、Sake、Meatballs、Beef Katsu Sando、Yeast Monster、Cookbook、Bad Meatloaf、Food Sketch、Fried Balls、Vampire Defense Kit。

**行動**
- 將以上差異逐項加入 RECIPE_CONFLICTS.md。
- Clutter暫採 Cloth + Wooden Spoon候選，不標 verified。
- Rat冷爐 #5與Bad #4/#6/#7保留分支，等待實機 slot counter驗證。
- Kombucha以多份英文攻略及玩家討論支持的 Mushroom + Yeast為優先候選，但保留中文社群反例。

**判斷**
- 1.0中文攻略對名稱翻譯有幫助，但作者聲明資料可能因更新失效，不能把它視為比官方 patch或多個獨立玩家回報更高的證據。
- 現在的主要瓶頸已不是缺少配方名字，而是不同版本／攻略對加工狀態和額外輸入的差異。

**下一步**
- 將 Bistro所有 117個候選逐筆標註 evidence/confidence/introduced version。
- 將 Rat Level 21-22個候選 slot逐項做 QA測試。
- 將中文攻略的譯名轉成台灣用語，但不直接照搬簡體配方結論。


## 2026-11-16｜Wine About It 與 Rat Level slot 測試規則
**觀察**
- Steam玩家指出五瓶酒按瓶身標籤高度由短到長排列即可完成 Wine About It。
- 1.0中文攻略與8/10英文攻略對 Rat冷爐第五個Good slot、Egg/Pencil、Pasta相關Bad slots存在差異。
- 1.0日文玩家提供 Coioioin 藍色開關後投幣的操作提示。

**行動**
- 將 Wine About It改為 label_height ascending的排序 puzzle，保留五瓶酒實際位置待畫面確認。
- Rat Level slot按來源分支記錄，不將 Leaf與Eggshell或Egg與Eggshell合併。
- 將 Coioioin的藍色開關列為新版優先驗證步驟。

**判斷**
- Wine排序規則已從模糊「看標籤」收斂為可測試的高度排序。
- Rat Level仍是資料最不穩定的區域；翻譯與圖示名稱不能代替輸入／輸出驗證。

**下一步**
- 取得五瓶酒畫面並記錄實際 label height順序。
- 用每個 Rat slot的計數器驗證 Leaf/Eggshell與Egg/Eggshell差異。
- 確認 Coioioin按藍色開關後是否可直接觸發，或是否仍需同面三次。


## 2026-11-16｜建立全關卡 recipe inventory
**觀察**
- Student Dorm、Cafe、Bistro、Rat Level的 recipe候選已能形成一份跨關卡總表。
- 來源總量推算為327：211 Good、116 Bad；與官方商店「over 300 recipes」一致。
- Cafe來源清單重複列出 Coffee Cake，已在 inventory去重。

**行動**
- 建立 docs/RECIPE_INVENTORY.md，列出各關卡所有候選 recipe名稱與計數。
- 將 Bistro 83/34明確標為推算值，Rat Level以slot而非翻譯名稱記錄。
- 將 recipe names與 formulas分開：inventory管清單與計數，conflict register管配方爭議。

**判斷**
- 327是目前可解釋官方「300+」的工作估計，不是官方精確總數。
- 下一階段需從 name inventory轉成結構化 recipe records；只列名稱不足以開工。

**下一步**
- 每筆補齊 inputs、processed states、appliance、power/heat condition、source、confidence、version、zh-TW。
- 對所有 D級配方建立最小化實機測試方案。
- 產生正式 Recipe DB draft前，先完成三主廚房與 Rat Level的來源對照。


## 2026-11-16｜Student Dorm / Cafe 配方矩陣
**觀察**
- 目前兩個章節的 Good/Bad清單已完整到可逐筆整理；來源包含 10/9與11/9攻略及 8/10 Steam guide。
- 兩個章節存在若干加工狀態與替代配方衝突，特別是 Beans on Toast、French Toast、Tomato Soup、Carbonara、Tiramisu、Canned Coffee、Dirty Chai Latte。

**行動**
- 建立 docs/RECIPE_FORMULA_DRAFT.md，整理 189筆 Student Dorm/Cafe候選公式。
- 為每筆保留來源語境，標示替代／衝突項。
- 將設備與狀態作為公式條件，而不是把所有輸入當一般物品。

**判斷**
- 這份表可作為資料整理基礎，但仍未達 implementation-ready：缺少逐筆 source id、version range、confidence、verification status與 item IDs。
- 公式表中「any unrelated ingredient」只能作條件描述，不能直接轉成硬編碼組合。

**下一步**
- 整理 Bistro 83/34候選公式，特別是新舊版本差異。
- 整理 Rat Level電力狀態與 21個 slot。
- 把公式表轉成 machine-readable schema前，先完成 item/state dictionary。


## 2026-11-16｜Bistro / Rat Level formula matrix
**觀察**
- Bistro 76/31 baseline與10個 post-launch additions可整理成83 Good / 34 Bad候選。
- Rat Level有9 Good slots（5 low/off +4 high/on）及12 Bad slots，標題為符號，需以slot索引識別。
- 多個 Bistro recipe仍有來源衝突，尤其 Mochi、Kombucha、Tomato Juice、Fried Rice、Sake、Meatballs、Beef Katsu Sando與Bad recipe families。

**行動**
- 建立 docs/RECIPE_FORMULA_BISTRO_RAT.md，逐筆整理候選輸入與狀態。
- 將 rat puzzle chain、power levels、wine sorting、rat trade、mixer repair與 scissors解鎖流程納入同一份規格。
- 保留三位數密碼未知，不猜測。

**判斷**
- 目前已完成四房間 recipe name inventory與初步 formula drafts；但尚未完成 machine-readable records、完整來源鏈、QA。
- Rat Level需用slot counter驗證，而不是翻譯圖示標題。

**下一步**
- 為327個候選recipe補上source_id、source_date、version、confidence、verification_status。
- 對D級配方列最少測試集，避免大量隨機組合。
- 完成七國料理、rat request順序與 wine label高度對照。


## 2026-11-16｜官方 v2.9ea 配方歷史
**觀察**
- 官方 v2.9ea（3/19）移除其中一個重複 Chocolate Spread。
- 官方 v2.9ea允許 Tiramisu多種有效配方：Cake + Coffee + Dough，或 Cake + Coffee + Milk。
- 官方 v2.9ea新增 Savory Sandwich的 Bread + Cheese + Tomato Sauce配方。

**行動**
- 將以上資訊加入 Recipe Conflict Register，標記為官方 Early Access歷史。
- 將 Tiramisu記錄為多個可接受配方候選，而非單一固定配方。
- 將 Savory Sandwich的 Tomato Sauce與 raw Tomato分開記錄。

**判斷**
- 遊戲內可能存在「一個 recipe多種有效 input set」的設計；recipe schema需支援 alternate_input_sets。
- 配方歷史不能被最新配方覆蓋，因為研究目標需保留版本差異。

**下一步**
- 對照 1.0 recipe book確認 Tiramisu最終有效輸入集合。
- 確認 Chocolate Spread只有一個item ID，避免把早期重複物件帶進復刻版。


## 2026-11-16｜確認三材料上限與章節設備差異
**觀察**
- Pixel Questing Chapter 1 guide說明最多拖入三種材料，再點擊烹調設備；Chapter 1是 Cooking Pot，Chapter 2是 Microwave Oven。
- Bistro有 pot與Mixer；Rat Level使用通電罐頭式 cooker。
- 非食材物件也會被投入設備，形成大量 Bad Recipes。

**行動**
- 將共同烹調流程寫成 1..3 inputs → drop into appliance → activate → evaluate conditions → output/cookbook update。
- 章節設備分開建模，保留 Toaster、Coffee Maker、Espresso Machine、Mixer等獨立機器。
- 將「是否消耗材料」「輸入順序」「設備內暫存」列為實機待測，不做假設。

**判斷**
- Recipe evaluator必須依設備與章節分派；不能只用 ingredient set做全域配方查詢。
- 非食材物件是玩法核心之一，Item schema需有 category與interactable capabilities，不可只建立 Ingredient表。

**下一步**
- 建立每個 Item的 capability matrix：drag、throw、cut、mix、cook、burn、wet、break、container_insert。
- 測試1/2/3材料上限、順序是否影響結果、材料是否消耗與可否重複使用。


## 2026-11-16｜互動與物理規格整理
**觀察**
- 官方資料、攻略與成就說明已足以定義大部分可觀察互動。
- 物理手感是核心，不只是動畫；但沒有原作 mass/friction/bounce數值。
- 手機觸控與桌面滑鼠都需使用同一互動抽象層。

**行動**
- 建立 docs/INTERACTION_SPEC.md。
- 拆分 Item、Tool、Container、Appliance、Clue、PuzzleInteractable、Environment、Character類別。
- 整理 Item state、appliance conditions、puzzle chains與acceptance tests。
- 將未知的材料消耗、順序、設備暫存、save object positions列為 open questions。

**判斷**
- 物理系統可以開始做設計規格，但在 recipe資料和QA未完成前仍不能開始實作。
- 所有 numeric physics values都屬復刻版調校值，不能宣稱還原原作內部係數。

**下一步**
- 完成 QA test catalog，涵蓋每個任務、配方、成就、存檔與輸入裝置。
- 針對每個未解問題設計最小測試組。
- 由 Critic審查資料完整度與風險。


## 2026-11-16｜建立 QA acceptance test plan
**觀察**
- 已有足夠證據將大部分已知流程轉成可測試條件；主要阻塞集中在少數未解任務與配方衝突。
- 桌面／觸控、recipe state、appliance、unlock flow、achievement、save與zh-TW都需要獨立驗收。

**行動**
- 建立 docs/QA_TEST_PLAN.md。
- 將每個關卡的任務、配方、成就與物理互動拆成 test case。
- 將未查明內容保留為明確 blockers，不用推測填補。

**判斷**
- QA設計已能開始，但不能執行；沒有遊戲實作或實機畫面時，不可聲稱任何測試 PASS。
- Recipe data的完整性是最大的前置風險；Critic需先檢查數量、版本與衝突管理。

**下一步**
- 完成 Cafe To-Do、七國料理、Rat code、recipe conflicts。
- 寫出 Critic review並列 P0/P1 blockers。
- 只有研究與 Critic gate通過後才進 implementation。


## 2026-11-16｜Rat Level 兩材料上限
- 新增日文 1.0通關攻略明確指出 Rat Level每次只用兩種材料。
- 修正互動規格：主廚房通用最多三材料；Rat Level cooker獨立 max_inputs = 2。
- QA新增 Rat Level第三材料拒絕／不接受測試，避免錯誤沿用主廚房規則。


## 2026-11-16｜建立 Source Register
**觀察**
- 目前研究來源跨官方 patch、開發者回覆、Steam guide、Pixel Questing、9Puz、日文玩家筆記與台灣餐飲詞彙來源。
- 部分頁面只有搜尋索引可讀，部分攻略有版本衝突；需要可稽核來源清單。

**行動**
- 建立 docs/SOURCE_REGISTER.md，編號 SRC-001至SRC-030。
- 定義 evidence hierarchy與來源限制。
- 後續資料表將以 SRC IDs取代散落在文字中的模糊來源描述。

**判斷**
- Source Register可避免後續配方修改時失去版本依據。
- 搜尋摘要只作線索，不能寫成直接讀取正文的結論。

**下一步**
- 將 recipe inventory/formula draft逐筆對應 SRC IDs。
- 為每個來源增加具體段落／comment位置，優先補足未直接開啟的Steam guide與9Puz。


## 2026-11-16｜Steam cached guide與開發者配方回覆校正
**觀察**
- Steam Guide 3713640352已從公開社群頁面移除，但搜尋索引仍可讀取完整內容與留言。
- Developer確認 Smoothie需要 Peanut Butter；另一則 developer reply明確確認 Good Protein Shake使用 Milk + Peanut Butter + Protein Powder，不是 Egg。
- 8/10 Steam guide對 Cafe多筆配方比 11/9 Pixel Questing更具體，尤其 Babyccino、Latte、Hot Cocoa、Avocado Milk、Strawberry Cheesecake、Chocolate Bomb、Canned Bread等。
- 11/9 Pixel Questing對多項Cafe Bad Recipes有不同輸入組合，不能因日期較新就直接覆蓋。

**行動**
- 更新 RECIPE_FORMULA_DRAFT.md的 Student Dorm與Cafe公式。
- 將 Smoothie、Sweet Sandwich、Carbonara、Tomato Soup、Beans on Toast、Tiramisu、Latte、Hot Cocoa、Avocado Milk等差異加入 RECIPE_CONFLICTS。
- Source Register新增 SRC-031 / SRC-032並註記Steam guide已被移除、只剩索引快取。

**判斷**
- Developer reply是特定配方的強證據，但日期較早；若 1.0指南有相反公式，仍需做版本核對。
- 目前資料應採「候選＋版本＋證據」而不是單一權威答案；這能避免將早期EA公式誤套到1.0。

**下一步**
- 把 189筆 Student Dorm/Cafe formula逐筆加上SRC IDs與confidence。
- 對 11/9 Pixel Questing與 cached Steam guide不同的Bad Recipes做最小化測試。
- 進一步確認 1.0 Smoothie與Sweet Sandwich最終配方。


## 2026-11-16｜Peanut Butter 隱藏解鎖查證
- Developer確認主選單信件的按鈕會解鎖 Peanut Butter，不需要真的 wishlist；解鎖後食材生成並寫入 save file。
- 將其列為主選單 → Student Dorm的前置狀態，不呼叫外部Steam wishlist。
- QA新增：首次按下信件按鈕後生成 Peanut Butter；重載後仍保留。


## 2026-11-16｜Item / ItemState inventory
**觀察**
- Recipe公式已顯示多個配方依賴加工狀態，而非只有原始食材名稱。
- 非食材工具、容器、線索、環境物件都能參與配方或解謎。
- 四個房間的物件清單可建立第一版，但仍有未辨識的場景道具。

**行動**
- 建立 docs/ITEM_STATE_INVENTORY.md。
- 分類 Ingredient、ProcessedIngredient、Tool、Container、Appliance、Clue、PuzzleInteractable、Environment、Character、Decoration。
- 將所有加工狀態獨立列出，並把未知的物件位置存檔與材料消耗列為待測。

**判斷**
- Recipe DB必須引用 item_id與state_id，不可用中文顯示名稱當唯一 key。
- 物件能力需由 capability matrix控制，避免把所有物品都當成可切割／可烹調。

**下一步**
- 補齊 Cafe未列物件、三個locker內容與所有場景隱藏道具。
- 建立 item-to-recipe references，確保每個 ingredient都被 recipe使用或標記為puzzle-only。
- 把 ItemState與RecipeConditions合併成可驗證資料規格。


## 2026-11-16｜Student Dorm mouse hole / tea boxes 與成就定位
**觀察**
- Developer確認 D2是 Shane locker key tile；右側另一格是 mouse hole，兩者不同。
- Developer確認把 Cheese拿到 mouse hole前即可解 I Smell Cheese；這與 Shane locker unlock無關。
- Developer確認 tea boxes位於上層架、Jam右側，藤蔓圖案需排列成連續圖樣。
- 9Puz成就表補足 Fair Trade、What's The Emergency、Aw That's Hot、Nothing Nowhere等位置與觸發。

**行動**
- 將 D2 key與 mouse hole拆成兩個 PuzzleInteractable。
- 將 A Lot to the Right位置寫入 Student Dorm場景資料。
- 將 Cafe 911、三 Bagel Void Bagel、Panini fire、Bistro Mixer二三次運作等成就觸發補入 QA。

**判斷**
- 場景中外觀相近的牆磚可能是不同互動點；不能只用 tile grid index推斷整面牆的功能。
- Achievement與recipe unlock有重疊但不完全相同，需分開保存觸發狀態。

**下一步**
- 核對 26成就每項觸發與所屬場景。
- 查明 Student Dorm其他三個 locker/cupboard內容與打開方式。


## 2026-11-16｜建立 26項 Achievement Matrix
- 新增 docs/ACHIEVEMENT_MATRIX.md，列出所有1.0成就與觸發候選。
- 將 Early Access已移除的 Master of Disaster排除於1.0目標之外。
- 對 Level 1/2/3/ Rat Level 100%標記描述已知、精確完成條件未知。
- 剩餘未解：Bookworm順序、七國菜名、Coioioin條件、100%是否需所有Bad Recipes。


## 2026-11-16｜Student Dorm六項To-Do與100% ledger修正
**觀察**
- 9Puz 1.0 completion route提供完整六項Student Dorm To-Do：8 pasta dishes、Borrow Shane's Cheese、Play All Cassettes、Make Coffee、Water Basil、Cook New Dishes 40 Good+Bad。
- 這修正了先前把「清洗碗盤」獨立當成一項To-Do的錯誤；清洗與餐具歸位是Make Coffee前置。
- 9Puz明確表示每個房間各有recipe與task ledger，並提醒Student Dorm需檢查Good/Bad兩個recipe tabs。
- Flooded約淹至50%時遊戲會提示；Bookworm需要讓書背的波浪線連續。

**行動**
- 更新 PROGRESSION_MODEL、INTERACTION_SPEC、QA_TEST_PLAN。
- 將六項任務完整寫入progression和QA。
- 修正 room completion規則：Good+Bad recipe tabs與To-Do ledger均須完成；精確百分比公式仍待live counter驗證。

**判斷**
- Student Dorm To-Do已從「部分推測」提升為 1.0 walkthrough完整候選清單。
- 不能把任務前置互動誤當成獨立task，也不能把Bad Recipes視為可忽略。

**下一步**
- 取得Cafe完整task ledger與Bistro task ledger。
- 核對每個房間的Good/Bad總數與100% counter。
- 更新成就矩陣的Bookworm排序說明。


## 2026-11-16｜Cafe To-Do範圍收斂
- 將 Cafe已知task entries整理為至少四項：清理廚房、與Blue Teapot老鼠交易、完成8張訂單、讓廚房起火。
- 官方v3.0ea明確新增 Complete 8 orders To-Do；1.0 walkthrough提及電話stock、訂單Coins、Espresso Cup、Safe、fire alarm等100% blockers，但未證明它們是獨立task rows。
- 更新 progression model與QA：Cafe任務已有候選清單，但不宣稱已完整。


## 2026-11-16｜Bistro 84/39與全遊戲333筆候選總量修正
**觀察**
- 9Puz 1.0 completion route明確列出 Crazy Calzone = Pizza + Pizza Dough。
- Steam 7/17玩家留言補出五個Bad recipes：Breadless Burger、Vampire Defense Kit、Bread and Wine、Sorrow Sandwich、Risky Rice Pudding。
- 這六項不在7/14 guide主清單，因此原先把76/31當作完整EA baseline的推算漏掉了。

**行動**
- Bistro Good由83修正為84；Bad由34修正為39。
- 全遊戲候選總量由327修正為333（212 Good +121 Bad）。
- 更新 inventory、Bistro formula draft、conflict register、README、progress report、progression與QA。

**判斷**
- 84/39是目前更完整的跨來源候選清單；仍不是官方counter，不能標為verified。
- July 17玩家留言是配方發現，不一定是遊戲版本更新；來源時間需保留，不能把它誤寫成patch date。

**下一步**
- 逐筆把Bistro 123項候選對應SRC IDs與版本。
- 用1.0 cookbook counter確認Bistro Good/Bad數量。
- 重新核對其他房間是否也有未列入攻略主清單、但在留言中發現的recipe。


## 2026-11-16｜完成312筆命名配方 zh-TW候選翻譯
- 建立 docs/ZH_TW_RECIPE_TRANSLATIONS.md，涵蓋Student Dorm 48+29、Cafe 71+41、Bistro 84+39，共312筆命名配方。
- Rat Level 21 slots使用低／高電力與slot序號，不將符號猜成料理名。
- 翻譯覆蓋已完成，仍需最後台灣用語審校、雙關校正、畫面長度與手機排版測試。


## 2026-11-17｜Cafe八項To-Do與Coioioin衝突校正

**觀察**
- 官方 v3.0ea說 Level 2新增8個To-Do entries；先前把「8項To-Do」誤讀成「完成8張訂單」的8個任務，必須修正。
- 1.0攻略可明確辨識的Cafe任務候選至少四項：Clean kitchen、rat trade、complete 8 orders、set kitchen on fire。其餘四項尚未從來源中找回。
- 9Puz及Steam成就頁／玩家討論支持Coioioin為同一面硬幣連續出現三次；藍色開關與紅色目標區的另一說法未能獲得同等程度交叉支持。

**行動**
- PROGRESSION_MODEL改為8個Cafe task rows，其中4個已知、4個待查；明確區分8 orders與8 To-Do entries。
- 更新INTERACTION_SPEC、QA_TEST_PLAN、PROGRESS_REPORT的Coioioin證據優先順序。

**判斷**
- Cafe To-Do是目前Level 3解鎖的主要未完成資料缺口。
- 不把「完成火災」當成唯一解鎖條件；必須完成整份To-Do ledger。
- Coioioin以Steam成就文字作主要規格，藍開關路線保留為候選。

**下一步**
- 專查Cafe其餘四項To-Do的名稱與觸發步驟。
- 找到Bistro七國料理圖像／完整鼠交易清單。
- 逐項核對333候選配方的公式與狀態，尤其Bistro與Rat Level。


## 2026-11-17｜撤回Cafe「八項To-Do」錯誤推論

**觀察**
- SteamDB保存的官方 v3.0ea patch notes明確寫的是「New Todo: complete 8 orders」。
- 這句話表示新增一個任務，其目標是完成8張訂單；不能解讀成Cafe有8個任務。
- v5.1ea要求完成Level 2 To-Do list才可進Level 3，但沒有在該條更新紀錄列出完整任務名稱。
- 1.0攻略可確認火災互動是Level 2 To-Do；清理廚房與老鼠交易是必要進度互動，但UI任務歸屬尚不確定。

**行動**
- 撤回「8個Cafe To-Do entries、其中4項已知」的前一版說法。
- 改為：明確確認一項「Complete 8 orders」；火災任務由1.0攻略支持；其他清理、老鼠、電話等先當進度互動，不擅自歸類。
- 更新PROGRESSION_MODEL與QA_TEST_PLAN。

**判斷**
- 這個更正很重要：復刻不能把錯誤的任務數量做成硬編碼。
- Level 3解鎖依賴完整Cafe To-Do，但完整清單目前仍未取得。

**下一步**
- 搜尋Cafe 1.0實際To-Do面板的完整畫面／錄影。
- 找出Bistro七國料理與老鼠交易完整順序。
- 完成Rat Level電力與配方衝突的證據分級。


## 2026-11-17｜Bistro To-Do與Rat trade第一段確認

**觀察**
- 日本玩家 2026-09-09 Level 3攻略的To-Do段落直接列出「Clean the kitchen」及「Trade with the rat」。
- 清潔使用 Cloth；老鼠在 Range Hood，給 Cheese後先獲得 Tomato，之後會持續從抽油煙機送出料理圖，完成指定料理即可交換新食材。
- 七國料理完成時，磁鐵會吸附在 Range Hood；七項完成後取得 Going Global。可讀文字只辨識 Mochi/Japan，其他國家料理沒有文字名。
- Steam成就說明Coioioin是同一面連續三次；Steam指南也說點擊爐旁硬幣即可，藍開關／紅區說法目前缺乏交叉支持。

**行動**
- 將 Bistro清潔與老鼠交易列為已知To-Do / progression interactions。
- Rat trade流程明確分成request_shown → dish_completed → ingredient_rewarded。
- Coioioin測試優先順序改為直接點擊硬幣連續三次同面；藍開關路線只作fallback研究。

**下一步**
- 找出其餘六個國際料理及完整rat request順序。
- 確認Bistro To-Do其餘項目與Level 3的100%條件。


## 2026-11-17｜Cafe / Coioioin 文件一致性稽核
- 掃描README、Progression、QA、Progress Report、Achievement Matrix與Interaction Spec後，發現舊的進度段落仍殘留「新增8個Cafe To-Do」錯誤句，以及QA將藍開關寫成主要測試。
- 已改為：官方v3.0ea新增一項「完成8張訂單」；Cafe完整To-Do列數未知。Coioioin主測試為點擊硬幣連續三次同面，藍開關僅保留備援研究。
- 此次是文件一致性修正，沒有新增遊戲內實測結果。


## 2026-11-17｜Internal handoff / conflict register同步Coioioin更正
- 全repo稽核找到INTERNAL_HANDOFF與RECIPE_CONFLICTS仍將藍開關寫成主要Coioioin條件。
- 已修正為Steam官方成就敘述與多份攻略共同支持的「點擊爐旁硬幣，同一面連續三次」；藍開關／紅色目標區保留為低信心線索。


## 2026-11-17｜全文件搜尋：清除Cafe任務數量殘留誤述
- 全文件搜尋發現INTERNAL_HANDOFF早期段落、QA與RECIPE_CONFLICTS仍有「八個Cafe To-Do」或「四項已確認」的舊說法。
- 已修正：官方v3.0ea只明確命名一項「完成8張訂單」；火災任務由1.0攻略支持；清潔與老鼠交易為必要進度互動，但UI是否列為To-Do未確認。
- Cafe任務總列數不再猜測，等待可讀的實際To-Do畫面或影片。


## 2026-11-17｜Cafe To-Do來源矛盾補登
- SteamDB保存的官方v3.0ea原文寫單數「New Todo: complete 8 orders」；日本4/24攻略卻概述「ToDo list、8件追加」。
- 兩者有語意／計數衝突，不能單憑日本攻略把Cafe任務列數寫成8，也不能把官方更新條目推成最終版本完整清單。
- 9/10日文1.0玩家又回報Set the kitchen on fire可能已做但To-Do未勾選，代表任務狀態可能有同步問題。
- 已在RECIPE_CONFLICTS與SOURCE_REGISTER記錄此差異；規格採不硬編碼總列數，等遊戲內To-Do UI或完整影片確認。


## 2026-11-17｜333筆配方名稱／公式列／繁中譯名交叉稽核
**檢查方法**
- 將RECIPE_INVENTORY的各房間Good/Bad名稱逐條與兩份RECIPE_FORMULA文件比對。
- 將六個命名料理分類逐條與ZH_TW_RECIPE_TRANSLATIONS比對；Rat Level 21格維持符號slot，不列為菜名。

**結果**
- 配方名稱與公式列完全對齊：Student Dorm 48+29、Cafe 71+41、Bistro 84+39、Rat Level 9+12，總計333列；未發現缺列或多列。
- 312筆命名料理與繁中翻譯表完全對齊：Student Dorm 77、Cafe 112、Bistro 123；無缺漏、無重複key。
- Rat Level 21格是slot條件而非料理名稱，故不加入命名翻譯。

**修正**
- 發現Bistro公式表曾以「Sausage Roll (9Puz calls it Salami Roll)」作主鍵，與inventory不同；已統一主鍵為Sausage Roll，別名留在衝突登錄。
- 發現English Breakfast譯名缺列，補入「英式早餐」，並去除重複列。

**限制**
- 此次只證明名稱清單、公式列與翻譯列數量一致；不代表每個材料公式已實機驗證。


## 2026-11-17｜Cafe與Bistro To-Do場景歸屬再校正
- 日本1.0玩家記錄顯示Cafe的「Set the kitchen on fire」完成後，還要清完剩餘訂單，回My Room才解鎖Bistro；玩家曾遇到火災已發生但To-Do未登錄，重做一次才更新。
- Bistro的To-Do面板則另有「Clean the kitchen」與「Trade with the rat」兩項，先清潔，再餵Cheese啟動老鼠交易。
- 因此把場景歸屬分清：Cafe明確To-Do候選為Complete 8 orders、Set the kitchen on fire；Bistro至少Clean the kitchen、Trade with the rat。Cafe完整列數仍未知。
- QA新增火災任務狀態與Steam achievement分離、重試登錄測試。


## 2026-11-17｜Bistro QA cases補齊
- QA_TEST_PLAN新增BIS-016至BIS-018：Bistro清潔To-Do、老鼠交易To-Do、Clutter觸發探索。
- QA test case總數由85增加到88，ID唯一且無重複。
- Clutter只確認1.0存在，觸發條件沒有可靠文字證據；QA不得先把Mixer mess或其他任意組合當成公式。


## 2026-11-17｜Ground Meat / Ground Beef狀態key統一
- 稽核Bistro公式表與ItemState inventory，發現Steam 8/10 guide在Meatball Sandwich、Cheeseburger使用Ground Beef，而其他來源用Ground Meat。
- 未找到證據證明是兩種不同加工物；因此統一使用ground_meat state，Ground Beef只作來源別名。
- ITEM_STATE_INVENTORY與RECIPE_CONFLICTS已補充說明，避免把同一加工狀態錯建成兩種食材。


## 2026-11-17｜本輪研究稽核收束與下一輪優先順序
**已完成**
- 333筆候選公式列與Inventory名稱逐條對齊；312筆命名料理翻譯與Inventory逐條對齊，Rat Level 21個slot不翻譯成假菜名。
- QA達88個唯一測試案例；來源登錄達46筆。
- 修正Cafe / Bistro To-Do場景歸屬：Cafe目前明確有Complete 8 orders、Set the kitchen on fire；Bistro至少有Clean the kitchen、Trade with the rat。
- Coioioin以官方描述和多個玩家指南採「同一面連續三次」，藍開關／紅色目標區不作必要條件。
- Ground Beef統一為Ground Meat狀態別名；Clutter配方觸發維持Unknown。

**本輪未能從公開可讀來源解決**
- Cafe完整To-Do UI列數及其餘任務名稱。
- Going Global七道國際料理中除Mochi以外的六道。
- Rat Level花盆便條三位數密碼與OFF/ON對應low/high。
- Clutter的具體觸發方式。
- 若干D級配方公式與加工狀態衝突；需遊戲內實際cookbook counter / recipe card驗證。

**下一輪工作**
1. 針對Steam影片、玩家截圖與1.0攻略圖片找Cafe To-Do完整畫面、Bistro磁鐵便條及Rat Level密碼圖。
2. 逐筆將333筆公式綁定SRC ID、版本與信心等級，建立可追溯資料表。
3. 針對高風險衝突建立最小測試組合，不用無限制亂試。
4. 完成物理互動 acceptance spec與存檔狀態表。
5. 進行Critic review；P0/P1清零前維持Research Only。


## 2026-11-17｜Student Dorm配方證據重審：Clutter與Smoothie等

**觀察**
- 再讀1.0 Pixel Questing全文與Steam開發者討論後，發現先前的衝突表把「Smoothie包含Peanut Butter」擴大解讀成完整公式已被確認，證據其實只支持其中一項材料。
- Pixel Questing 1.0列出Smoothie = Strawberry Jam + Banana + Milk；Steam舊版攻略列Milk + Banana + Peanut，開發者只回覆Peanut Butter是Smoothie的其中一項材料。兩者不能直接互相排除。
- Good Protein Shake則不同：開發者明確更正為Milk + Peanut Butter + Protein Powder，並指出Egg是錯的。1.0攻略另提Banana alternate，保留低信心測試。
- Carbonara仍有 Cheese / Milk 分歧；PB&J Sandwich的PB&J Jar + Bread是可用的中間物件路徑。
- Clutter：日文1.0玩家確認菜名與提示語，但沒有精確觸發公式；簡中攻略的Cloth + Wooden Spoon目前缺乏獨立佐證。

**行動**
- RECIPE_CONFLICTS修正上述四組配方的證據等級與候選描述。
- 將Clutter從Cloth + Wooden Spoon候選撤回為Unknown，QA仍要求先找出可重現觸發條件。

**決策**
- 只把開發者明確給出的完整公式列為A級公式；僅確認某項材料，不等於完整配方已確認。
- 同一菜名若有多條來源支持的輸入路徑，優先建模alternate_inputs，而不是直接假設版本差異。

**下一步**
- 搜尋可讀的遊戲畫面／錄影以確認Smoothie與Carbonara的實際recipe card。
- 對Bistro七國料理與Rat Level密碼繼續做影像來源檢索。


## 2026-11-17｜Coioioin重新定級：藍開關／紅框是1.0第一手流程

**新證據**
- 重新讀取2026-09-10日文1.0通關文章後，確認作者不是只隨口提及藍色開關：文章明確寫「按藍框內開關，再把硬幣投進紅框」，並表示這不是單純連續三次同面或1/8隨機機率。
- 作者另指出遊戲內已取得成就，但Steam未立即同步；關閉並重新啟動遊戲後才出現在Steam。
- 這與Steam官方成就文字「同一面連續三次」及8/26玩家「反覆點硬幣」說法存在真實衝突。

**修正**
- 撤回先前「藍開關只有低信心、可忽略」的判斷，也撤回「只需點硬幣直到同面三次」的單一路線。
- Coioioin改列兩種待測觸發候選：A. 反覆點硬幣；B. 按藍框開關後投進紅框。
- QA新增兩條路線測試與一條Steam重新啟動同步測試；遊戲內成就與Steam平台同步分成兩個狀態。

**來源**
- 日文1.0第一手攻略：https://note.com/utsukinoel/n/n2734d08070ca
- Steam官方成就：https://steamcommunity.com/stats/3376500/achievements
- Steam玩家討論：https://steamcommunity.com/app/3376500/discussions/0/582806564883173701/


## 2026-11-17｜Bistro Magnet／Compass依賴補充
- 9Puz 1.0 route指出 Big Magnet 需要把老鼠交易取得的 Magnet 放進料理設備烹調；8/10 Steam guide只簡寫為「Magnet from mouse rewards」，未說清是否要再烹調。
- Compass = Scissors + 任一 country Magnet；9Puz提醒先確認該磁鐵已登記到 Going Global，再製作 Compass。
- 因此將 `magnet_inventory`、`country_magnet_registered`、`big_magnet_recipe` 分成不同狀態，避免把收到獎勵直接視為食譜已完成。
- Big Magnet 仍是候選公式，待實機 cookbook counter 驗證。


## 2026-11-17｜來源版本錯置更正：SRC-017不是1.0指南

**發現**
- 直接打開 Steam Guide ID 3686619896 後，頁面標題為「v4.0EA《Little Chef...》全成就指南」，頁面明確寫配方以 v3.0 EA 為基準，發布日期 2026-03-17、更新日期 2026-06-08。
- 該頁可讀內容只涵蓋 Student Dorm 與 Cafe，沒有 Bistro 或 Rat Level；因此此前把它描述為「2026-09-01簡中1.0指南」並引用其 Bistro/Rat Level公式，是來源錯置。
- Steam Guide ID 3713640352 的搜尋索引顯示8/10全遊戲內容，但直接開啟葡萄牙語頁面仍是4/25 EA版本，且指南已被Steam移除。8/10後的Bistro/Rat Level資料只能當快取搜尋線索，不能稱為直接檢視原文。

**修正**
- SOURCE_REGISTER將SRC-017改為v4.0 EA、3/17發布、6/8更新，並撤回其Bistro/Rat Level支持範圍。
- RECIPE_CONFLICTS移除所有錯誤歸因給「9/1簡中1.0指南」的配方候選：Clutter的Cloth + Wooden Spoon、Rat冷槽Leaf、Eggshell + Pencil、Pasta-only/Pasta+Paper等不再作為證據。
- Bistro剩餘衝突只保留能追溯至7/14 Bistro Guide、8/10 Steam Guide快取、9/2 9Puz或玩家留言的候選；Clutter保持Unknown。

**決策**
- 來源的標題、日期、遊戲版本與實際可讀章節必須逐項核對；搜尋摘要不能推翻頁面本身的版本聲明。
- 舊EA指南可用於早期Student Dorm/Cafe線索，但不可被升格為1.0/Bistro/Rat Level依據。


## 2026-11-17｜SRC-023文章日期與遊戲版本分離
- 再讀日本Level 3攻略搜尋全文後，發現文章雖於9/9發布，作者明確說內容是7/13 Early Access Level 3更新期間；不能因發布日期在1.0之後就把它當成1.0實測。
- SRC-023改標為EA-era first-hand source；Bistro To-Do、老鼠交易、Mixer、Wine與七國料理的流程線索保留，但需再用1.0資料確認。
- 七國料理仍只可確認Japan = Mochi；其餘六項未能從文字來源確認。


## 2026-11-17｜重新取得 9Puz 1.0 全文與 Steam Guide 正文：Rat Level 規格收斂

**新取得的可讀證據**
- 直接開啟 9Puz 2026-09-02 1.0 completion route，取得完整正文；Rat Level明確寫出：先操作右上角老鼠肖像顯示反重力控制，開啟後讀取花盆便條三位數密碼，再掀開酒瓶標籤露出鍵盤，輸入密碼後才可使用 cooker。
- 9Puz列出冷態 Good 五槽：Cheese、Cheese+Cheese、Cheese+Paper、Cheese+Pencil、Cheese+Eggshell；熱態 Good 四槽：Cheese、Cheese+Cheese、Cheese+Paper、Cheese+Pencil。這與 Steam Guide 的 OFF/ON 清單一致，但 Eggshell/Leaf仍需保留槽位核對。
- 9Puz將 Rat Level Bad recipes 的 Egg/Pencil 與 Eggshell/Pencil列為社群來源有差異的候選；Pasta相關槽位也有不同攻略版本差異。不得把不同來源列出的候選合併成同一配方。
- 9Puz補充 Big Magnet應將老鼠交易取得的 Magnet 放入料理設備烹調；Compass需使用已登記 Going Global 的 country Magnet + Scissors。
- 9Puz說明 Rat cooker每次最多兩種材料；同一材料組合需依冷／熱狀態分別計數。

**來源可讀性更正**
- Steam Guide ID 3713640352雖顯示已遭移除，但瑞典語頁面目前可直接讀到完整正文，包括作者標示的 2026-08-10版本內容、Bistro清單與Rat Level OFF/ON slot清單。此證據高於僅有搜尋摘要，但仍屬社群攻略；嵌入圖片未完整轉成文字，不能宣稱所有圖片線索已檢視。
- 更新 SOURCE_REGISTER：新增 SRC-047（9Puz直接可讀全文），並修正 SRC-016的可讀性註記。

**仍未解決**
- 9Puz只告訴讀者從花盆便條讀取三位數密碼，沒有在可讀正文寫出數字；不能猜碼。
- 9/9 EA文章與9/2 1.0路線都只以文字命名 Japan = Mochi；其他六個國家／料理對應仍需圖片證據。
- Rat Level OFF/ON 與日文攻略 low/high 的映射仍未由明確畫面證實。
- Bistro老鼠的完整請求料理順序與七國料理配對仍未完整取得。

**決策與下一步**
- 將 Rat Level 的可讀公式清單視為 C 級候選，按 live slot counter設計最小驗證；保持 oven_state 與 power_level 分開，直到確認 OFF/ON ↔ low/high。
- 下一輪集中取得 9Puz／Steam guide 的原始嵌入圖片或影片截圖，尤其花盆便條、七國磁鐵與老鼠 request note；若圖片仍無法讀取，明確保留 Unknown。


## 2026-11-17｜官方 v5.1ea 老鼠任務狀態修正補證
**新證據**
- 直接開啟 Steam 官方 All News 頁面，v5.1ea（2026-07-14）Fixes明確列出：修正「Trade with the rat」To-Do顯示 -1，以及防止 rat quest 再次開始。
- 同一更新再次說明進入 Level 3前必須完成 Level 2 To-Do list；不代表完整 Cafe任務列數已公開。

**規格影響**
- Bistro rat quest需保存單一持續任務狀態與已完成 request index；重載／重進場景不得重置為初始請求，也不得重複發放同一獎勵。
- To-Do顯示計數與 rat quest progression state需分離；UI計數不能直接當作任務真實狀態來源，以免重現 -1 顯示錯誤。
- 建議資料欄位：quest_started、request_index、request_completed、reward_claimed、quest_completed；每次交易採冪等處理（同一 request 不可重複領獎）。這是復刻版設計決策，不宣稱原作內部程式碼如此實作。

**限制**
- 官方更新只證明曾修正計數顯示與重複啟動 bug；完整老鼠 request 菜單、每一步料理順序、七國磁鐵與一般食材獎勵的精確先後仍未取得。

來源：SRC-048。


## 2026-11-17｜v1.1 官方修正與 1.0 攻略交叉查證

**新增來源 SRC-049（官方 v1.1，2026-09-11）**
- Coioioin Steam成就同步曾有問題，v1.1明確修正；QA需區分遊戲內觸發與Steam端同步，並以更新後行為為準。
- Level 1有重複罐子問題，v1.1修正；早期攻略或截圖若出現重複 jar，不能當作正式版物件配置。
- Goulash與Tomato Cocktail cookbook配方曾需修正；這兩筆列為高風險配方，必須以v1.1後遊戲內結果／最新版來源為準，不能僅照抄8/10 Steam guide。
- Rat cursor與密碼鎖點擊區域於v1.1改善；若舊攻略點擊座標不準，優先考慮版本差異，不先判定操作錯誤。

**本輪其他交叉結果**
- 1.0 9Puz攻略把Rat Level冷／熱槽位及解謎流程列出，但花盆密碼數字本身未在文字中公布；維持UNKNOWN。
- 日文1.0通關記錄確認Bistro先清潔，再與老鼠交易；Cheese換Tomato，後續依請求圖料理取得食材。它只公開Japan = Mochi，沒有文字列出其他六國菜名。
- Steam攻略列出Going Global由老鼠任務取得七個country magnets，但七國料理的完整對應沒有在文字中列明；不可把Bistro一般食譜自行分類成國家菜。

**新增待辦**
- 對Goulash、Tomato Cocktail建立v1.1後專項核驗。
- 取得Steam攻略與日文攻略的嵌入圖片原始圖像，嘗試辨識七國菜名、老鼠便條與Rat密碼線索；若圖像解析不到，保留未知，不用猜測補完。


## 2026-11-17｜完整讀取 Steam 100% 配方指南正文（SRC-050）
**本輪取得**
- 直接讀取 Steam Guide ID 3713640352 全文，不再只依賴搜尋摘要；正文涵蓋 Student Dorm、Cafe、Bistro、Rat Level候選配方、關卡流程與成就提示。Steam頁面顯示已移除／不相容，但正文仍可讀。
- Bistro配方候選明列：Goulash = Meat + Wine + Ground Tomato；Tomato Cocktail = Olives + Wine + Ground Tomato；兩者均受官方v1.1「修正 cookbook配方」影響，不能未經遊戲驗證就宣告最終正確。
- 指南註明七國磁鐵由老鼠依請求料理發放，但未在可讀文字中列出完整七國對應；Rat Level密碼只說讀取花盆便條，未提供數字。
- 指南留言提供兩項具體勘誤：Dirty Chai Latte應為 Tea + Milk + Coffee（不是Coffee Beans）；Tomato Juice使用Ground Tomato（不是整顆Tomato）。兩者目前屬社群留言修正，需列為候選並保留證據等級。

**版本與品質判斷**
- 指南正文自述配方表基準為2026-08-10，另有08-27新增項；頁面最後更新日期顯示09-02。它不是官方配方表，且頁面目前被標記removed/incompatible。
- 這份來源適合建立完整候選表與QA測項，不適合單獨作為最終權威。SRC-049官方v1.1修正說明優先於該指南的舊配方。

**新增QA要求**
- 在目前v1.1或更新版本客戶端，分別測試Goulash與Tomato Cocktail，記錄實際輸入物件狀態（特別是Ground Tomato）、輸出卡片、是否新增食譜，以及重開遊戲後是否保留。不得只以真實世界食譜或舊指南定案。

來源：SRC-050、SRC-049。


## 2026-11-17｜Cafe電話解鎖觸發條件補證（SRC-051）
- 找到開發者 Crazydvd 在 Steam 討論串的直接回覆：Level 2輸入電話號碼後，必須拿起話筒並等對方講完，才能離開電話；之後 Avocado 與 Lettuce 才會生成。
- 這是重要的事件觸發條件，不只是「輸入正確號碼」；復刻規格需把 dial_completed、receiver_picked_up、call_dialogue_finished、stock_spawned視為有順序的狀態，離開電話過早不可誤判成配方或存檔錯誤。
- 討論串玩家提及21931與27937兩組號碼，但開發者只確認操作順序，沒有確認兩組號碼皆為通用答案；號碼仍以當前存檔內便條為準。
- QA新增CAF-017，測試輸入後未接聽、接聽但未等講完、完整聽完三種情況。

來源：SRC-051。


## 2026-11-17｜Critic 初審後追加：Rat Level 原始截圖檢查
- 直接開啟日文 1.0通關文的Rat Level嵌入截圖。畫面可見電器罐、控制面板、數字便條與紅框投幣目標，支持場景互動物件位置；但不同截圖的便條顯示不同數字狀態，不能將局部數字誤當完整通用密碼。
- 作者文字支持每次最多兩材料、解鎖後強／弱電力切換、相同材料因電力不同產生不同料理；OFF/ON對應仍沒有足夠圖像證據。
- Coioioin的藍框開關與紅框投幣目標在圖像中可見；官方成就條件是同面連續三次，兩者是否為捷徑／必要條件仍待實機驗證。
- 本輪未取得七國其餘六道菜名或完整 rat request index；不以推測填補。


## 2026-11-17｜Critic發現後補齊 Bistro 配方衝突 QA
- 初審發現 Bistro 配方衝突表已有多筆 D 級變體，但 QA 未逐項覆蓋。新增 BIS-027 至 BIS-040：Tomato Cheese Appetizer、Apple Mochi、Meatballs、Beef Katsu Sando、Fried Rice、Sake、Yeast Monster、Cookbook、Bad Meatloaf、Food Sketch、Fried Balls、Charcuterie Board、Pizza Speciale、Clutter。
- QA總數由102增至116個唯一案例；仍全部屬測試設計，未聲稱已執行。


## 2026-11-17｜QA補齊 Mochi / Yeast Monster 衝突
- 將Mochi whole Rice vs Ground Rice與Yeast Monster三種候選配方轉為BIS-048、BIS-049。
- 配方衝突表與Bistro/Rat配方文件同步補註；QA總數129，均為待執行設計。
