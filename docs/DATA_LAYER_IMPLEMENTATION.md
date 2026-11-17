# Data Layer Implementation Report

Updated: 2026-11-17  
Status: **Data layer v0.1 committed; not game implementation complete**

## Delivered

- `data/recipe.schema.json`: JSON Schema contract for recipe candidate records.
- `data/recipes.candidates.json`: all 333 inventory candidates imported with stable IDs, room, Good/Bad class, provenance pointer, power-state slot where applicable, status, and disabled flag.
- Candidate formula/action text imported from `docs/RECIPE_FORMULA_DRAFT.md` and `docs/RECIPE_FORMULA_BISTRO_RAT.md`: **312 / 333**.
- The remaining **21 / 333** are Rat Level symbolic slots. They remain slot-based and have no fabricated formula.
- `app/index.html`: browser data browser with text search (name and candidate formula), room filter, Good/Bad filter, formula display, and status.
- `scripts/validate_recipes.py`: dependency-free static dataset validator.
- `tests/test_recipe_dataset.py`: unittest entry point.
- `data/README.md`: local preview and validation instructions.

## Static checks performed against the committed JSON

| Check | Result |
|---|---:|
| Total records | 333 |
| Unique IDs | 333 |
| Unique room + class + name keys | 333 |
| Formula/action text imported | 312 |
| No formula text (Rat Level slots) | 21 |
| Candidate records accidentally enabled | 0 |
| Room/class counts | All 8 groups match inventory |

The structural check was executed against the JSON fetched from the committed `main` branch. The Python validator and unittest were committed, but were **not executed in this environment**; a local Python run is still required.

## Known limitations / next work

1. The 312 formula strings are source text, not normalized ingredient IDs or item states. Alternative variants and conflicts are intentionally preserved in the source text.
2. All 333 rows remain disabled. No recipe is marked verified in-game.
3. Rat Level needs direct evidence for the 21 symbol/slot candidates, including power-state behavior.
4. The HTML preview requires an HTTP server from the repository root; it is not deployed as a public website.
5. No original game assets, physics, scene interactions, progression, save system, or playable recreation have been implemented yet.

## Safety rule

Never promote a formula to executable status merely because it appears in a walkthrough. A future normalization pass must map each ingredient to an item key and state, record appliance/conditions/version/evidence, resolve or preserve conflicts, and pass QA before enabling it.


## Follow-up implementation: lossless formula variants

Updated: 2026-11-17

- Matched **312 / 312** available candidate formula rows to their exact source document and Markdown line locator.
- Added `sourceEvidence`, `formulaCandidates`, and `normalization` fields to each matched recipe.
- Split explicit `OR` alternatives into separate raw candidate variants where present; preserved each variant's original wording.
- Marked **97** records for manual review due to alternatives, conflicts, actions, or ambiguous conditions. The other **215** have simple text splits only; they are not declared semantically normalized.
- Updated the browser UI to display formula text, source links, and review state.
- Updated JSON Schema and static validator to cover these fields and source-locator requirements.
- Re-fetched the committed dataset and checked 333 rows, 333 unique IDs, 312 source locators, 312 formula candidate sets, and all records disabled. These checks passed.
- The Python validator itself has not yet been run in a Python runtime; the above are direct structural checks against GitHub's committed JSON.
