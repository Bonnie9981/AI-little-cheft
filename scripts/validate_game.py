import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "game.html").read_text(encoding="utf-8")
RUNTIME = json.loads((ROOT / "data/recipe-runtime.json").read_text(encoding="utf-8"))
CATALOG = json.loads((ROOT / "data/recipe-catalog.json").read_text(encoding="utf-8"))

# Dataset integrity: candidates are not silently promoted to verified recipes.
assert len(CATALOG["recipes"]) == 333, "candidate catalog must retain 333 rows"
assert len(RUNTIME["recipes"]) == 333, "runtime must retain 333 rows"
ids = [r["id"] for r in RUNTIME["recipes"]]
assert len(ids) == len(set(ids)), "duplicate runtime recipe IDs"
assert all(r.get("enabled") is False and "VERIFIED" not in r.get("status", "") for r in CATALOG["recipes"]), "catalog candidates must remain disabled and unverified"
assert all(r.get("verified") is False for r in RUNTIME["recipes"]), "runtime candidates must stay unverified"
assert all(r.get("id") and r.get("room") and r.get("kind") in {"Good", "Bad"} for r in RUNTIME["recipes"])

# Gameplay integrity: progress must come from actual game events, not a task-complete shortcut.
for required in ("function cook()", "function complete(i)", "function save()", "function renderTasks()"):
    assert required in HTML, f"missing core gameplay function: {required}"
assert "data-puzzle" not in HTML, "task panel must not expose a progress-grant button"
assert "function advancePuzzle" not in HTML, "task progress must not be granted by checking a task"
assert "Math.min(9" not in HTML and "Math.min(12" not in HTML, "rat recipe totals must come from unique recipe discoveries"

# Parse the inline game script with Node when available; this catches syntax errors
# that text-based assertions cannot detect.
node = shutil.which("node")
if node:
    scripts = re.findall(r"<script>(.*?)</script>", HTML, flags=re.S)
    assert scripts, "inline game script not found"
    with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8", delete=False) as f:
        f.write("\n".join(scripts))
        script_path = f.name
    try:
        subprocess.run([node, "--check", script_path], check=True, capture_output=True, text=True)
    finally:
        Path(script_path).unlink(missing_ok=True)
else:
    print("WARN: Node.js unavailable; JavaScript syntax check skipped")

print("PASS: candidate data integrity, anti-shortcut progression checks, and available JS syntax check")
