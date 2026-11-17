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
| [SOURCE_REGISTER](docs/SOURCE_REGISTER.md) | SRC-001…SRC-052來源登錄與證據層級 |
| [RECIPE_INVENTORY](docs/RECIPE_INVENTORY.md) | 四個房間的候選配方名稱與數量 |
| [RECIPE_FORMULA_DRAFT](docs/RECIPE_FORMULA_DRAFT.md) | Student Dorm / Cafe 配方公式初稿 |
| [RECIPE_FORMULA_BISTRO_RAT](docs/RECIPE_FORMULA_BISTRO_RAT.md) | Bistro / Rat Level 配方公式初稿 |
| [RECIPE_CONFLICTS](docs/RECIPE_CONFLICTS.md) | 配方衝突、版本差異與未驗證項目 |
| [ZH_TW_GLOSSARY](docs/ZH_TW_GLOSSARY.md) | 台灣繁體中文 UI、食材、料理與成就詞彙 |
| [INTERACTION_SPEC](docs/INTERACTION_SPEC.md) | 物件、物理、輸入、設備與解謎互動規格 |
| [QA_TEST_PLAN](docs/QA_TEST_PLAN.md) | 127項測試案例：配方、物理、解鎖、成就、存檔與多裝置驗收 |
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

**完成上述研究與 Critic Gate 前，不開始正式實作。**
