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
