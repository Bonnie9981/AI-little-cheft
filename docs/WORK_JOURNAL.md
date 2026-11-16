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
