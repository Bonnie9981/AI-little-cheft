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
    keys = [(r.get("room"), r.get("kind"), r.get("name")) for r in rows]
    if len(ids) != len(set(ids)): errors.append("duplicate recipe IDs")
    if len(keys) != len(set(keys)): errors.append("duplicate room/kind/name records")
    actual = {}
    for r in rows:
        key = (r.get("room"), r.get("kind"))
        actual[key] = actual.get(key, 0) + 1
        for field in ("id", "room", "kind", "name", "status", "enabled", "inputs", "outputs", "evidence"):
            if field not in r: errors.append(f"{r.get('id', '<no id>')}: missing {field}")
        if r.get("enabled") is not False: errors.append(f"{r.get('id')}: candidate must remain disabled")
        if r.get("kind") not in ("Good", "Bad"): errors.append(f"{r.get('id')}: invalid Good/Bad classification")
        if not r.get("evidence"): errors.append(f"{r.get('id')}: missing inventory provenance")
        if r.get("candidateFormula") and r.get("status") != "SOURCE_LISTED_NOT_VERIFIED":
            errors.append(f"{r.get('id')}: formula/status mismatch")
        if r.get("candidateFormula") and not r.get("sourceEvidence"):
            errors.append(f"{r.get('id')}: formula missing exact source locator")
        for candidate in r.get("formulaCandidates", []):
            if not candidate.get("raw") or not isinstance(candidate.get("terms"), list):
                errors.append(f"{r.get('id')}: malformed formula candidate")
        if r.get("normalization", {}).get("normalized") and r.get("normalization", {}).get("reviewRequired"):
            errors.append(f"{r.get('id')}: normalized while review is still required")
    for key, count in EXPECTED.items():
        if actual.get(key, 0) != count: errors.append(f"{key}: expected {count}, got {actual.get(key, 0)}")
    if len(rows) != 333: errors.append(f"expected 333 rows, got {len(rows)}")
    formula_count = sum(bool(r.get("candidateFormula")) for r in rows)
    if formula_count != db.get("importedFormulaRows"): errors.append("importedFormulaRows mismatch")
    source_count = sum(bool(r.get("sourceEvidence")) for r in rows)
    review_count = sum(bool(r.get("normalization", {}).get("reviewRequired")) for r in rows)
    missing_formula = [r["id"] for r in rows if not r.get("candidateFormula")]
    if len(missing_formula) != 21: warnings.append(f"{len(missing_formula)} records have no formula text")
    print(f"Records: {len(rows)} | unique IDs: {len(set(ids))} | formula text: {formula_count}")
    print(f"Exact formula source locators: {source_count} | manual review required: {review_count}")
    print(f"Disabled candidates: {sum(r.get('enabled') is False for r in rows)}")
    print("Room/type counts:")
    for key in EXPECTED: print(f"  {key[0]} / {key[1]}: {actual.get(key, 0)}")
    for warning in warnings: print("WARNING:", warning)
    for error in errors: print("ERROR:", error)
    return 1 if errors else 0

if __name__ == "__main__": sys.exit(validate())
