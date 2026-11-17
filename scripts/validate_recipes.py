#!/usr/bin/env python3
"""Static integrity checks for the Little Chef research dataset (stdlib only)."""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "recipes.candidates.json"

EXPECTED = {
    ("Student Dorm", "Good"): 48, ("Student Dorm", "Bad"): 29,
    ("Cafe Job", "Good"): 71, ("Cafe Job", "Bad"): 41,
    ("Bistro", "Good"): 83, ("Bistro", "Bad"): 40,
    ("Rat Level", "Good"): 9, ("Rat Level", "Bad"): 12,
}

def validate():
    db = json.loads(DATA.read_text(encoding="utf-8"))
    errors, warnings = [], []
    rows = db.get("recipes", [])
    ids = [r.get("id") for r in rows]
    if len(ids) != len(set(ids)):
        errors.append("duplicate recipe IDs")
    keys = [(r.get("room"), r.get("kind"), r.get("name")) for r in rows]
    if len(keys) != len(set(keys)):
        errors.append("duplicate room/kind/name records")
    actual = {}
    for r in rows:
        key = (r.get("room"), r.get("kind"))
        actual[key] = actual.get(key, 0) + 1
        required = ("id", "room", "kind", "name", "status", "enabled", "inputs", "outputs", "evidence")
        for field in required:
            if field not in r:
                errors.append(f"{r.get('id', '<no id>')}: missing {field}")
        if r.get("enabled") is not False:
            errors.append(f"{r.get('id')}: candidate must remain disabled")
        if r.get("kind") not in ("Good", "Bad"):
            errors.append(f"{r.get('id')}: invalid Good/Bad classification")
        if not r.get("evidence"):
            errors.append(f"{r.get('id')}: missing provenance pointer")
        if r.get("candidateFormula") and r.get("status") != "SOURCE_LISTED_NOT_VERIFIED":
            errors.append(f"{r.get('id')}: formula/status mismatch")
    for key, count in EXPECTED.items():
        if actual.get(key, 0) != count:
            errors.append(f"{key}: expected {count}, got {actual.get(key, 0)}")
    if len(rows) != 333:
        errors.append(f"expected 333 rows, got {len(rows)}")
    formula_count = sum(bool(r.get("candidateFormula")) for r in rows)
    no_formula = [r["id"] for r in rows if not r.get("candidateFormula")]
    if formula_count != db.get("importedFormulaRows"):
        errors.append("importedFormulaRows does not match actual formula fields")
    if len(no_formula) != 21:
        warnings.append(f"{len(no_formula)} records lack candidate formula text; expected 21 Rat Level slots")
    print(f"Records: {len(rows)} | unique IDs: {len(set(ids))} | formula text imported: {formula_count}")
    print("Room/type counts:")
    for key in EXPECTED:
        print(f"  {key[0]} / {key[1]}: {actual.get(key, 0)}")
    print(f"Disabled candidates: {sum(r.get('enabled') is False for r in rows)}")
    print(f"Records without formula text: {len(no_formula)}")
    for warning in warnings:
        print("WARNING:", warning)
    for error in errors:
        print("ERROR:", error)
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(validate())
