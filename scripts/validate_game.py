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
assert all(r.get("enabled") is False and r.get("status") not in {"VERIFIED", "GAME_VERIFIED"} for r in CATALOG["recipes"]), "catalog candidates must remain disabled and unverified"
assert all(r.get("verified") is False for r in RUNTIME["recipes"]), "runtime candidates must stay unverified"
assert all(r.get("id") and r.get("room") and r.get("kind") in {"Good", "Bad"} for r in RUNTIME["recipes"])

# Gameplay integrity: progress must come from actual game events, not a task-complete shortcut.
for required in ("function cook()", "function complete(i)", "function save()", "function renderTasks()"):
    assert required in HTML, f"missing core gameplay function: {required}"
assert "data-puzzle" not in HTML, "task panel must not expose a progress-grant button"
assert "function advancePuzzle" not in HTML, "task progress must not be granted by checking a task"
assert '<button id="story">🕵️ 故事線索</button>' in HTML, "story journal entry point must exist"
assert "故事線索 · 已解鎖" in HTML, "story journal must show progressive chapter unlocks"
assert "21931" in HTML and "拿起聽筒" in HTML, "Cafe phone deduction must preserve the full call sequence in story journal"
assert "data.noteDigitsRevealed" in HTML and "data.phoneDialed" in HTML and "data.handsetPicked" in HTML and "data.phoneDone" in HTML, "Cafe call must require note reading, dialing, handset pickup and completed wait"
assert "data.requestPictureRead" in HTML and "請求圖" in HTML, "Bistro rat request must be inspected before trade cooking"
assert "data.countryMagnets" in HTML and "Japan" in HTML and "Mochi" in HTML, "country magnet progress must be separate and only known mapping represented"
assert "其餘六國仍待來源核對" in HTML, "unknown country mappings must remain unresolved"
assert "data.ratClueRead" in HTML and "data.wineLabelInspected" in HTML and "data.enteredCode" in HTML, "Rat Level keypad must require note clue before label-revealed keypad"
assert "setTimeout(()=>{if(current==='cafe'&&data.handsetPicked&&!data.phoneDone)" in HTML, "Cafe call must complete after handset wait, not immediately on dialing"
assert "七國磁鐵是另一條獨立收集線" in HTML, "Bistro rat trades and country magnet storyline must remain separate"
assert "其餘六格仍待來源核對" in HTML, "unknown country recipes must not be invented in narrative"
assert "畫像後方藏著反重力開關" in HTML and "酒瓶標籤又揭開鍵盤" in HTML, "Rat Level deduction chain must be represented"
assert "data.ending" in HTML and "生日蛋糕" in HTML and "媽媽留下的信" in HTML, "post-game birthday cake and mother's letter must appear after the ending"
assert "const bistroDishName=current==='bistro'" in HTML, "Bistro trade fallback must be defined before Good recipe evaluation"
assert "bistroDishName===tradeRecipes[stage-1]" in HTML, "Bistro staged trade must accept its explicitly modeled candidate dish"
assert "match?match.name:bistroDishName" in HTML, "Bistro trade message must support fallback dishes without a runtime recipe match"
assert "完成老鼠四段交易料理" in HTML, "Bistro trade task label must match its actual completion condition"
assert "pot.length<(current==='rat'?2:3)" in HTML, "Rat Level must enforce its two-input limit during drag/drop"
assert "if(current==='rat'&&!data.powerUnlocked)" in HTML, "Rat cooking must require the keypad power unlock"
assert "action==='power'||action==='empty')&&current!=='rat'" in HTML, "Rat-only controls must reject use in other rooms"
assert "$('devicePower').classList.toggle('hidden',current!=='rat')" in HTML, "Rat-only controls must be hidden outside Rat Level"
assert "$('deviceMixer').classList.toggle('hidden',current!=='bistro')" in HTML, "Mixer control must be scoped to Bistro"
assert not re.search(r"Math\.min\((?:9|12)\s*[,)]", HTML), "rat recipe totals must come from unique recipe discoveries"

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
        check = subprocess.run([node, "--check", script_path], capture_output=True, text=True)
        if check.returncode:
            raise AssertionError("JavaScript syntax error:\\n" + check.stderr)
    finally:
        Path(script_path).unlink(missing_ok=True)
else:
    print("WARN: Node.js unavailable; JavaScript syntax check skipped")

print("PASS: candidate data integrity, anti-shortcut progression checks, and available JS syntax check")
