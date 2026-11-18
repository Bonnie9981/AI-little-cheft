import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
html = (root / "game.html").read_text(encoding="utf-8")
runtime = json.loads((root / "data/recipe-runtime.json").read_text(encoding="utf-8"))
catalog = json.loads((root / "data/recipe-catalog.json").read_text(encoding="utf-8"))

assert len(catalog["recipes"]) == 333, "candidate catalog count changed"
ids = [r["id"] for r in runtime["recipes"]]
assert len(ids) == len(set(ids)), "duplicate runtime recipe IDs"
assert len(runtime["recipes"]) == 333, "runtime recipe count changed"
assert "function advancePuzzle(i)" in html
assert "function cook()" in html
assert "function save()" in html
assert "data-puzzle" in html
assert "function complete(i)" in html
assert "data.ratGood" in html and "data.ratBad" in html
assert "Math.min(9" not in html and "Math.min(12" not in html, "rat counters must not be granted by a puzzle button"
assert "data.pasta||0)>=8" in html or "data.pasta||0) >= 8" in html, "dorm pasta gate missing"
print("PASS: 333 candidate rows, unique runtime IDs, core progression hooks and anti-cheat guards")
