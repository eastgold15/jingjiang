"""Grade all eval runs against their assertions."""
import json
import os
import re
from pathlib import Path

WORKSPACE = Path(r"D:\Users\boer\Desktop\jingjiang\jingjiang-theme-workspace\iteration-1")

def count_occurrences(text: str, pattern: str, is_regex: bool = False) -> int:
    if is_regex:
        return len(re.findall(pattern, text))
    return text.count(pattern)

def check_assertion(assertion: dict, text: str) -> dict:
    check_type = assertion["check"]
    value = assertion["value"]

    if check_type == "file_contains":
        passed = value in text
        evidence = f"Found '{value}'" if passed else f"Missing '{value}'"
    elif check_type == "file_contains_regex":
        matches = re.findall(value, text)
        passed = len(matches) > 0
        evidence = f"Found '{value}' (matches: {matches})" if passed else f"No match for '{value}'"
    elif check_type == "file_count_min":
        min_count = assertion.get("min_count", 1)
        count = text.count(value)
        passed = count >= min_count
        evidence = f"Found {count} occurrences of '{value}', need >= {min_count}"
    elif check_type == "file_line_count_regex":
        min_count = assertion.get("min_count", 1)
        lines = text.split('\n')
        count = sum(1 for line in lines if re.match(value, line))
        passed = count >= min_count
        evidence = f"Found {count} lines matching '{value}', need >= {min_count}"
    else:
        passed = False
        evidence = f"Unknown check type: {check_type}"

    return {
        "text": assertion.get("name", assertion.get("description", "unknown")),
        "passed": passed,
        "evidence": evidence
    }

def grade_run(eval_dir: Path, run_type: str, metadata: dict):
    result_file = eval_dir / run_type / "outputs" / "result.md"
    grading_file = eval_dir / run_type / "grading.json"

    if not result_file.exists():
        print(f"  No result file at {result_file}")
        return

    text = result_file.read_text(encoding="utf-8")
    assertions = metadata.get("assertions", [])

    results = [check_assertion(a, text) for a in assertions]
    passed_count = sum(1 for r in results if r["passed"])
    total_count = len(results)

    grading = {
        "run_type": run_type,
        "passed": passed_count,
        "total": total_count,
        "expectations": results
    }

    grading_file.write_text(json.dumps(grading, ensure_ascii=False, indent=2))
    print(f"  {run_type}: {passed_count}/{total_count} passed")

def main():
    # Process each eval directory
    for eval_dir in sorted(WORKSPACE.glob("eval-*")):
        if not eval_dir.is_dir():
            continue

        # Read metadata
        meta_file = eval_dir / "eval_metadata.json"
        if not meta_file.exists():
            print(f"No metadata at {meta_file}, skipping")
            continue

        metadata = json.loads(meta_file.read_text(encoding="utf-8"))
        eval_name = metadata.get("eval_name", eval_dir.name)
        print(f"\n=== {eval_name} ===")

        for run_type in ["with_skill", "without_skill"]:
            grade_run(eval_dir, run_type, metadata)

if __name__ == "__main__":
    main()
