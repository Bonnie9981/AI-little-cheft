# Little Chef 復刻｜時間線與里程碑

更新日期：2026-11-16  
Repository：https://github.com/Bonnie9981/AI-little-cheft

本文件分成原作遊戲版本時間線、本專案工作時間線、下一階段里程碑。已發生與預計工作分開標示；沒有可靠日期的工作不虛構日曆日期。

## A. 原作遊戲版本時間線（已發生）

| 日期 | 事件 | 備註 |
|---|---|---|
| 2026-03-16 | 《Little Chef: Cozy Cooking》開始 Early Access | Steam 商店資訊 |
| 2026-07-12 | Bistro（Level 3）推出 | 官方 Level 3 更新資訊 |
| 2026-08-26 | 1.0 正式版推出；完成 Level 1、2、3 各 100% 可解鎖額外驚喜內容 | 官方 1.0 公告 |
| 2026-08-26 | Shredded Cheese 錯誤輸出修正 hotfix | 不可把舊 bug 行為當正確配方 |
| 2026-08-27 起 | 社群攻略陸續補入 Bistro 新食譜與 Rat Level 線索 | 玩家攻略，不等於官方規格 |
| 2026-09-11 | v1.1：修正 Coioioin 成就、四處英文拼字、Level 1 重複罐子、食譜書設定按鈕；修正 Goulash 與 Tomato Cocktail 食譜書資料；改善 Rat cursor 與密碼鎖點擊區 | 官方 changelog |
| 2026-09-25 | Steam Trading Cards 上線 | Steam 商店近期公告 |

## B. 本專案工作時間線（已發生）

| 日期 | 工作事件 | 產出／狀態 |
|---|---|---|
| 2026-11-16 | 確認專案目標與研究先行原則 | Research Only；未開始遊戲實作 |
| 2026-11-16 | 確認 GitHub Repository 與 main 分支 | Bonnie9981/AI-little-cheft |
| 2026-11-16 | 清理使用者指定的測試空白檔「？」 | 已刪除；沒有擴大刪除其他內容 |
| 2026-11-16 | 建立 README.md | 已推送 |
| 2026-11-16 | 建立內部交接與進度報告 | docs/INTERNAL_HANDOFF.md、docs/PROGRESS_REPORT.md 已推送 |
| 2026-11-16 | 補查 Bistro 配方與 Rat Level 冷熱條件 | 增加社群配方候選；保留未驗證標記 |
| 2026-11-16 | 建立工作日誌與時間線 | 本文件及 docs/WORK_JOURNAL.md |

## C. 下一階段里程碑（預定，尚未完成）

### M1｜完成全場景食譜資料庫
- Student Dorm、Cafe、Bistro、Rat Level 分開建檔。
- 每筆記錄材料、數量、加工狀態、設備、溫度、順序、輸出、Good/Bad/特殊分類。
- 記錄版本、來源 URL、證據級別、驗證狀態、繁中名稱。
- 優先處理 Bistro Goulash、Tomato Cocktail、Risotto、Focaccia、Shredded Cheese，以及 Rat Level Eggshell/Leaf 分歧。
- 完成條件：每筆食譜有來源與狀態；未知項明確標記，不以猜測填滿。

### M2｜完成場景互動與解鎖規格
- 物件狀態機、設備操作、老鼠交易、電話／安全卡、磁鐵、酒瓶排序、剪繩、Mixer、隱藏物件、場景完成條件。
- 完成條件：主要互動有前置條件、操作步驟、結果、失敗情況與來源。

### M3｜完成台灣繁體中文本地化資料
- 統一食材、設備、菜名、成就、提示與 UI 術語。
- 避免簡體字、簡體詞彙及不自然直譯。
- 完成條件：所有資料庫條目有 zh-TW 名稱；術語表通過校對。

### M4｜QA 測試規格
- 食譜正確／錯誤組合、狀態條件、設備、冷熱爐、解鎖、成就、存檔／讀檔、JSON 匯出匯入、桌機與手機橫向操作。
- 完成條件：每個核心系統有可重複執行的驗收案例與預期結果。

### M5｜Critic 獨立審查
- 檢查資料遺漏、來源衝突、過時版本、錯誤推論、版權風險、行動裝置可用性。
- 完成條件：重大問題已修正或列為明確接受的限制；使用者可檢查審查結果。

### M6｜正式開發
- 只有 M1–M5 達到可接受標準後才啟動。
- 候選技術方案：TypeScript + Phaser/Canvas + Matter.js + IndexedDB；這是本專案提案，非原作內部技術。
- 完成條件：依已驗收規格分階段實作，並保留回歸測試。

## D. 依賴關係
M1 食譜資料庫、M2 互動與解鎖、M3 zh-TW 本地化 → M4 QA → M5 Critic → M6 正式開發。

M1 與 M2 可部分平行研究；QA 需要足夠穩定的規格；Critic 必須在開發前完成。

## E. 時間管理原則
- 不虛構已完成日期或預估工時。
- 若要排日曆時程，先估算各里程碑工作量，再依使用者可投入時間排程。
- 每次更新保留「原定／實際／偏差／原因」欄位。
- 任何版本更新都要回頭檢查受影響的配方與成就，不只新增版本號。


## 2026-11-16｜本輪研究里程碑
- Student Dorm：新增 1.0攻略的 48 Good / 29 Bad、24個場景物件、至少6項 To-Do；完成新舊配方差異登記。
- Cafe Job：新增 1.0攻略的 71 Good / 41 Bad、37個場景物件；釐清電話完整互動與訂單 coin；Cafe 8個訂單目標與 Level2 To-Do數量仍分開記錄。
- Bistro：整理 76 Good / 31 Bad 候選與六個留言補充配方；新增 recipe conflict register。
- Rat Level：修正設備模型為通電罐頭式 cooker，電力強弱決定相同材料的不同輸出；三位數密碼仍待實際 note畫面。
- 版本基準：以 1.0（2026-08-26）及 v1.1（2026-09-11）為主要目標版本；Early Access配方需標註版本，不混成同一份資料。
- Research Only持續；目前尚未完成完整 Bistro rat request順序、七國料理對照、所有 recipe逐筆驗證、完整物理互動矩陣、繁中詞典、QA與Critic。


## 2026-11-16｜Bistro recipe count revision
- 7/14 Bistro Guide：76 Good / 31 Bad（EA baseline）。
- 8/27追加：7 Good + 2 Bad；9/10玩家通關記錄再補 Clutter（Bad candidate）。
- 1.0候選總量推算 83 Good / 34 Bad；尚未有官方 counter畫面確認，禁止當成最終定案。


## 2026-11-16｜Bistro rat trade evidence
- Developer confirms Cheese starts the extractor-hood rat quest; each requested dish is shown as a drawing and trades for a new ingredient.
- First reward recorded as Tomato; later gifts include Apple, Olive, Garlic.
- Seven country dishes create seven magnets; only Mochi/Japan is currently named by a readable source. Other six remain unresolved.
- Heart note marks the rat quest complete; not an extra recipe request.
