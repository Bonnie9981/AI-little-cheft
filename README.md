# Little Chef 網頁復刻

台灣繁體中文（zh-TW）的《Little Chef: Cozy Cooking》忠實網頁復刻研究專案。

**Research Only**

**目前不開始遊戲實作。** 必須先完成全場景食譜、互動機制、解鎖、成就、zh-TW 詞彙、QA 與 Critic 審查。

## 目標與版本基準

- 目標版本：1.0（2026-08-26）＋ v1.1（2026-09-11）修正。
- 語言：台灣繁體中文（zh-TW）。原作 Steam 目前不支援繁體中文，因此本專案需自行在地化。
- 平台：桌面瀏覽器、手機橫向。
- 美術：自行重繪，不直接使用未確認授權的正式遊戲素材。
- 研究原則：官方／實機證據優先；玩家攻略只作候選，衝突必須保留，不可自行猜定。

## 研究文件

| 文件 | 用途 |
|---|---|
| [INTERNAL_HANDOFF](docs/INTERNAL_HANDOFF.md) | 完整研究交接、技術決策與風險 |
| [PROGRESS_REPORT](docs/PROGRESS_REPORT.md) | 專案進度匯報 |
| [CRITIC_REVIEW](docs/CRITIC_REVIEW.md) | 獨立審查與開工 Gate |
| [PROJECT_TIMELINE](docs/PROJECT_TIMELINE.md) | 原作版本時間線與專案時間線 |
| [WORK_JOURNAL](docs/WORK_JOURNAL.md) | 可稽核的研究日誌、判斷與下一步 |
| [SOURCE_REGISTER](docs/SOURCE_REGISTER.md) | SRC-001…SRC-057來源登錄與證據層級 |
| [RECIPE_INVENTORY](docs/RECIPE_INVENTORY.md) | 四個房間的候選配方名稱與數量 |
| [RECIPE_FORMULA_DRAFT](docs/RECIPE_FORMULA_DRAFT.md) | Student Dorm / Cafe 配方公式初稿 |
| [RECIPE_FORMULA_BISTRO_RAT](docs/RECIPE_FORMULA_BISTRO_RAT.md) | Bistro / Rat Level 配方公式初稿 |
| [RECIPE_CONFLICTS](docs/RECIPE_CONFLICTS.md) | 配方衝突、版本差異與未驗證項目 |
| [ZH_TW_GLOSSARY](docs/ZH_TW_GLOSSARY.md) | 台灣繁體中文 UI、食材、料理與成就詞彙 |
| [INTERACTION_SPEC](docs/INTERACTION_SPEC.md) | 物件、物理、輸入、設備與解謎互動規格 |
| [QA_TEST_PLAN](docs/QA_TEST_PLAN.md) | 145項測試案例：配方、物理、解鎖、成就、存檔與多裝置驗收 |
| [ITEM_STATE_INVENTORY](docs/ITEM_STATE_INVENTORY.md) | 四個房間的物件、加工狀態與互動能力 |
| [ACHIEVEMENT_MATRIX](docs/ACHIEVEMENT_MATRIX.md) | 1.0正式26項成就與觸發條件 |
| [PROGRESSION_MODEL](docs/PROGRESSION_MODEL.md) | 房間進度、To-Do與解鎖狀態模型 |
| [ZH_TW_RECIPE_TRANSLATIONS](docs/ZH_TW_RECIPE_TRANSLATIONS.md) | 全312筆命名配方的台灣繁中候選譯名 |

## 目前研究盤點

目前候選清單合計 **333 筆**（212 Good + 121 Bad），與原作「300+ recipes」相符，但這是跨來源推算，尚未由遊戲內 cookbook counter 完整驗證。

| 場景 | Good | Bad | 狀態 |
|---|---:|---:|---|
| Student Dorm | 48 | 29 | 來源清單已整理，公式仍需逐筆驗證 |
| Cafe Job | 71 | 41 | 來源清單已整理，版本衝突待處理 |
| Bistro | 84 | 39 | 由 76/31 guide list + 6項 July discoveries + 10項 post-launch additions 推算 |
| Rat Level | 9 | 12 | 以 slot 記錄，Eggshell/Leaf 等衝突未定 |

## 尚未通過的研究 Gate

1. Cafe Level 2完整To-Do列數與全部任務名稱；已確認「完成8張訂單」是一項任務，另有火災任務線索。
2. Bistro 七國料理完整名單與老鼠交易順序／獎勵。
3. Rat Level 三位數密碼、power OFF/ON 與 low/high 對應。
4. 所有 D 級配方衝突、Rat Level密碼與1.0 cookbook counter。
5. 333 筆配方的逐筆來源ID、版本、狀態、設備、信心與驗證狀態。
6. 完整 zh-TW 校對、QA acceptance tests 與 Critic review。

## 自動推進與開工判定

- 使用者說「繼續」或要求自動推進時，視為授權在當前工作階段連續進行研究、交叉查證、文件更新、QA補齊及Critic複審；不應每完成一小項就停下來詢問。
- ChatGPT無法在對話回合結束後自行於背景持續執行；但每次收到延續指示，應從GitHub最新狀態接手，不要求使用者重述背景。
- 「Ready for CEO Approval」的門檻：核心遊戲循環、場景與解鎖、互動／物理、食譜資料結構、任務／成就、繁中詞彙、錯誤與例外、QA驗收規格均有可執行規格；所有未知項目須明確標記、隔離成可替換資料或列出實機驗證步驟，不得偽裝成已知；Critic不得留有未處置的P1。
- 不要求把無法從公開來源取得的隱藏數值硬猜出來。若某個未知不阻礙基礎系統開發，必須提出明確的暫定策略及驗證點；若會直接影響核心玩法正確性，則仍列為開工阻塞。
- 只有達到上述門檻並完成CEO審核後，才開始正式遊戲實作。

**目前仍未達到 Ready for CEO Approval。**


## 食譜來源追溯稽核

已建立 [RECIPE_PROVENANCE_AUDIT.md](docs/RECIPE_PROVENANCE_AUDIT.md)，逐筆列出333個候選食譜名稱與候選ID，並明確區分「名稱清單來源」與「配方公式來源」。目前333筆公式來源尚未逐筆映射，因此這份文件是稽核基線，不代表追溯完成；此項仍是開工前P1。


## Bistro 進度鏈最新研究

SRC-057已將抽油煙機老鼠的食材交易鏈與七國料理磁鐵鏈拆開記錄。Cheese → Tomato與Japan = Mochi有圖文證據；Apple Mochi及可疑料理不計入七國磁鐵。完整交易順序及其他六國仍未確認，詳見 [PROGRESSION_MODEL](docs/PROGRESSION_MODEL.md) 與 [RECIPE_CONFLICTS](docs/RECIPE_CONFLICTS.md)。
