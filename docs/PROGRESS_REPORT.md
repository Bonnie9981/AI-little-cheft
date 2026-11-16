# Little Chef 復刻｜專案進度匯報

更新日期：2026 年 11 月 16 日  
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
| Student Dorm 食譜 | 90% | 尚需逐條驗證與統一格式 |
| Cafe 食譜 | 90% | 尚需核對狀態條件及版本差異 |
| Bistro 食譜 | 85% | 有大量線索，但部分仍是玩家回報 |
| Rat Level | 85% | 冷／熱狀態、密碼與配方仍需確認 |
| 解鎖流程 | 90% | 主流程已整理，細節需補測 |
| 成就 | 95% | 清單大致齊全，觸發條件仍需驗證 |
| 物理互動規格 | 45% | 需補成可測試規格 |
| 台灣繁中詞庫 | 55% | 語言方向已確立，完整詞庫未完成 |
| 資料庫驗證 | 25% | schema 已規劃，尚未完成全量校驗 |

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
- 刪除根目錄測試空白檔「？」；commit：86413423279f303e1536947c5441d9d395ecff9f
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
