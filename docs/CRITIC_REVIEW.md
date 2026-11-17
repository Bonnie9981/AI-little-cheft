# Critic Review — Little Chef Recreation

審查日期：2026-11-17  
審查輪次：Round 1（文件／來源一致性初審）  
範圍：README、Recipe Inventory、配方草稿與衝突表、Source Register、Item State Inventory、Interaction Spec、Progression Model、Achievement Matrix、zh-TW 詞彙、QA、Internal Handoff。  
結論：**正式全內容實作 Gate：FAIL（Research Only 維持）**。

## 1. 盤點結果

| 項目 | 目前數量／狀態 | 審查判定 |
|---|---:|---|
| 候選配方 | 333（212 Good + 121 Bad） | 跨來源推算，非官方 counter |
| 有名稱配方 | 312 | 有候選繁中譯名，仍待逐筆來源追溯 |
| Rat Level | 21 個符號槽位（9 Good + 12 Bad） | 不應虛構料理名稱 |
| 成就 | 26 | 矩陣列數完整；部分觸發細節仍是候選 |
| QA | 129 個唯一 ID | 僅為測試設計，未執行 |
| 來源 | SRC-001 至 SRC-051 | 有重複來源以不同研究用途編號的情況，應避免把來源數量當獨立證據數 |

## 2. 重大阻塞（P1）

### P1-01｜Bistro 老鼠請求鏈不完整
開發者只確認：抽油煙機門後找到老鼠、用 Cafe 同樣的 Cheese 啟動、依老鼠圖示料理換取新食材。現有可讀資料沒有完整逐步請求順序與每一步獎勵對照。  
**影響：** 無法可靠重建 Best Friends、特殊食材解鎖及七國磁鐵流程。  
**下一步：** 取得 1.0 實機畫面／玩家逐步影片／原始 request note 圖片，逐張記錄 dish、reward、順序、是否一次性。

### P1-02｜七國料理只確認一組
目前可讀文字只明確指出 Japan = Mochi；其他六道料理未有可靠文字證據。Apple Mochi 明確不是日本國料理磁鐵那道。  
**影響：** Going Global 的完整內容與七國料理資料無法定案。  
**下一步：** 取得七張料理請求便條或磁鐵解鎖畫面，禁止從菜名推測國籍。

### P1-03｜Cafe To-Do 未完整
目前明確可引用的任務為「完成 8 張訂單」與「Set the kitchen on fire」。電話、Safe、訂單幣、espresso等是流程互動，但目前不能證明各自是獨立 To-Do row；總列數未知。  
**影響：** Level 2 100% 與 Bistro unlock gate 的完整條件仍不確定。  
**下一步：** 取得完整 1.0 To-Do list 截圖／實機逐項勾選紀錄，分開任務列與解鎖前置互動。

### P1-04｜Rat Level 解謎缺數字與電力映射
反重力→花盆便條→酒瓶標籤→數字鍵盤的流程已知，但三位數字未在可讀文字中公開。冷／熱或 low/high 有來源支持，OFF/ON 對應尚未有清楚截圖或實機紀錄。  
**影響：** 無法重建完整密碼解鎖與四／五個 Good slot 的精確狀態映射。  
**下一步：** 取得花盆便條、電源控制器和爐具指示燈同一版本的截圖；以遊戲 counter 確認 OFF/ON 對應。

### P1-05｜333 筆配方缺逐筆證據鏈
目前配方總數及房間分類可盤點，但仍有部分配方只在房間級來源段落、舊版攻略或玩家留言中出現，未達每筆都具備來源 ID、版本、輸入狀態、設備、信心與驗證狀態的要求。  
**影響：** 無法安全把全部配方匯入正式 recipe database。  
**下一步：** 建立逐筆欄位稽核表；沒有來源的候選降級為 UNKNOWN，不得標 verified。

### P1-06｜核心 QA 尚未實際執行
目前有 127 個唯一 QA 測試 ID，但全部仍是測試設計，沒有本專案遊戲客戶端的 pass/fail、截圖、版本號與存檔重載結果。  
**影響：** 任何配方與互動都不能標為 verified_in_game；核心流程尚無實測回歸證據。  
**下一步：** 取得可執行遊戲的測試環境，先跑所有 P1 解鎖流程、每房間代表性 Good/Bad 配方、Rat Level 狀態測試，再擴至全表。

## 3. 次要問題（P2）

- Goulash、Tomato Cocktail 的 1.0 輸入候選已有 SRC-017 支持；v1.1 官方修正後的現行行為仍需回歸測試，但不再阻止建立候選資料。

- Coioioin 有「連續同面三次」與藍框開關／紅框目標兩種玩家描述；官方成就文字支持前者，需以 1.0+ 實機為準。
- QA 的 127 項是規格案例，尚無任何一項可宣稱已實際執行；需要執行紀錄、截圖／影片、版本號與 pass/fail。
- zh-TW 字典目前是候選版；仍需母語校對、菜名專名核對、按鈕長度與窄螢幕溢位檢查。
- Source Register 有相同 URL 被多個 SRC ID 重複引用的情況；後續需區分「來源文件」與「來源用途／claim」，避免重複計算獨立證據。
- README 的來源範圍曾落後至 SRC-046，已修正為 SRC-051；Cafe 測試編號 CAFE-027 已修正為 CAF-017。

## 4. 已通過的結構性檢查

- 26 項成就矩陣的列數與官方 26 項總數一致。
- 333 = 212 Good + 121 Bad；312 個命名食譜 + 21 個 Rat Level 符號槽位，分類沒有把 Rat Level 圖示錯譯成菜名。
- QA 表格有 129 個唯一測試 ID，沒有重複 ID。
- 物件狀態模型已明確區分 whole/ground、Coffee Beans/filled cup、Bread/Toast/Burnt/Soggy、Rat cooker state 等重要狀態。
- Bistro Pizza Dough = Olive Oil + Yeast + Flour 由 7/14 Steam Bistro Guide 與 9/2 9Puz 1.0 route 交叉支持；屬 B 級候選，非實機驗證。
- SRC-017 1.0 guide 現已重新分類並直接讀取，提供 Goulash / Tomato Cocktail 的實際輸入候選與 Rat Level slot variants；v1.1 官方修正的當前回歸測試仍保留。

## 5. 開工 Gate 建議

**正式全內容實作：不通過。**  
**可考慮的低風險準備工作（需 CEO 明確批准）：** recipe schema、來源追溯欄位、存檔 schema、通用拖曳／輸入抽象的技術 spike；不得先做完整關卡、正式配方表或宣稱忠實復刻。

最終開工前至少要：
1. 完成 P1-01 至 P1-06 的研究，或由 CEO 明確接受逐項未知風險。
2. 333 筆資料逐筆有來源／版本／信心／驗證狀態。
3. QA 不只設計，核心解鎖與配方案例要有執行紀錄。
4. zh-TW 核心 UI 與完整料理名單通過校對。
5. Critic Round 2 無未接受的 P1 blocker。

---
此文件為 Round 1 文件審查；不是最終通過聲明。


## Round 1 Addendum — Rat Level image inspection (2026-11-17)
- Directly opened embedded screenshots from the Japanese 1.0 completion walkthrough. Images show the Rat Level cooker, control panel, number-note area, and a red-framed coin target; this strengthens spatial/interaction evidence beyond text extraction.
- The visible note digits differ across screenshots/states and do not establish a reliable universal three-digit code. Do not concatenate partial visible digits into a guessed code.
- The walkthrough text supports two inputs per attempt and strong/weak power changing outputs. The screenshots do not conclusively map cooker OFF/ON to strong/weak.
- A blue-framed switch and red-framed coin target are visible in the Coioioin screenshots. Official achievement text remains “same side three times in a row”; whether the switch/target is an alternative shortcut or a required interaction still needs live testing.
- This does not clear P1-01, P1-02, or P1-04.


## Round 1 Addendum — SRC-017 v1.0 guide reclassification (2026-11-17)
- The previous assessment of SRC-017 was wrong: the actual Steam page title is a v1.0 all-achievements guide updated Sep 8, 2026. Its body retains a “v4.0 ea” legacy section but includes full Bistro and Rat Level sections. This supersedes the earlier statement that it had no Bistro/Rat Level content.
- It adds 1.0 candidates for Rat Level: cold Good #5 Cheese + Leaf; Bad #4 Eggshell + Pencil; Bad #6 Pasta alone; Bad #7 Pasta + Paper. These conflict with SRC-050; QA now tests each branch (RAT-016 to RAT-019).
- It gives a candidate Clutter formula Cloth + Wooden Spoon, and several additional Bistro formula conflicts; QA expanded to BIS-041 through BIS-047. QA now has 129 unique test IDs, all designed but not executed.
- Goulash and Tomato Cocktail are no longer treated as formula-unknown P1 blockers: SRC-017 and comments provide actual 1.0 candidates. Current v1.1 behavior still needs regression verification because the official patch note says the cookbook was fixed without restating formulas.
- P1 blockers remain: rat request sequence/reward order, six unnamed country dishes, Cafe To-Do completeness, Rat Level numeric code and OFF/ON mapping, per-recipe source coverage, and executed QA.


## Round 1 Addendum — corrected gate after SRC-017 recovery
- P1-06 is now actual QA execution, not Goulash/Tomato Cocktail formula discovery. The 1.0 Chinese guide provides current candidates; only v1.1 regression remains.
- QA count is 129 unique test IDs, all unexecuted.


## Round 1 Addendum — SRC-052 independent Rat Level cross-check
- Added SRC-052, an independent Steam guide dated 2026-08-27. It corroborates the Rat Level puzzle sequence and most slot formulas.
- Eggshell is now the preferred candidate for cold Good #5; Eggshell + Pencil for Bad #4; Paperclip + Pasta for Bad #6; Eggshell + Paper for Bad #7. SRC-017 manual variants remain in QA as alternatives.
- Coioioin repeated coin-click route is supported by SRC-052 and official achievement wording; Japanese blue-switch/red-target remains a second method to test.
- The actual numeric code and OFF/ON-to-weak/strong mapping remain unresolved. Source register now reaches SRC-052; QA remains 127 designed, unexecuted tests.


## Round 1 Addendum — further recipe-conflict coverage
- Added two more conflict tests: BIS-048 for whole vs Ground Rice in Mochi, and BIS-049 for the three competing Yeast Monster combinations. QA now has 129 unique designed test IDs; none are claimed executed.
