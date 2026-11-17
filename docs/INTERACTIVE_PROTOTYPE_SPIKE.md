# Interactive Prototype Spike

Updated: 2026-11-17

## Purpose

Turn the interaction research into a tangible, testable browser prototype without pretending unknown recipe rules are known. This is a technical spike, not the full game and not a faithful physics claim.

## Implemented

- Responsive kitchen work area, desktop and narrow/mobile layouts.
- Pointer Events for mouse and touch drag.
- Release velocity sampling and a tunable gravity / damping loop.
- Simple floor and side-boundary bounce.
- Six sample food objects (Bread, Banana, Tomato, Cheese, Egg, Milk).
- A Cooking Pot drop zone with a hard maximum of three objects.
- Explicit Raw / Processed demonstration state, kept separate per object.
- Local save/load of prototype objects, positions, states and pot membership.
- Operation log and scene reset.

## Deliberate limits

- No recipe output is generated. Candidate formulas remain disabled until their inputs, item states, appliance and conditions are verified.
- No claim of original-game mass, friction, bounce, drag stiffness or toss constants. The current physics is only a tunable placeholder.
- No character AI, room progression, puzzle chain, To-Do ledger or achievements in this spike.
- The sample objects are a small interaction test set, not the full item inventory.

## Run locally

From the repository root:

```bash
python -m http.server 8000
```

Open `http://localhost:8000/prototype/`. Do not open via `file://`, because the browser's local-storage and relative-path behavior differs.

## Test status

- JavaScript syntax parsed successfully after fetching the committed page.
- Static feature checks confirmed Pointer Events, gravity loop, and localStorage snapshot code are present.
- Browser rendering, real touch-device behavior, and end-to-end interaction tests remain unexecuted.
- Test cases PRO-001 through PRO-009 are listed in `docs/QA_TEST_PLAN.md`.
