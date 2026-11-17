# Little Chef data layer

## Static validation

Requires Python 3.9+ and no third-party packages.

```bash
python scripts/validate_recipes.py
python -m unittest discover -s tests
```

The 333-row candidate dataset imports 312 candidate formula/action strings from the two formula-draft documents. The 21 Rat Level rows remain slot-based and have no normalized formula text. All rows remain disabled because source-listed formulas are not equivalent to in-game verification.

## Browser preview

Serve the repository root with any static HTTP server, then open `/app/`. For example:

```bash
python -m http.server 8000
```

Open `http://localhost:8000/app/`. The page fetches `/data/recipes.candidates.json`; opening the HTML as `file://` will not work because browsers block local fetch requests.
