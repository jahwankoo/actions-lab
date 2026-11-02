"""Run the lab 2 tests and print a score. Exit code 0 only if every test passes.

Used by .github/workflows/lab2-autograder.yml. You can also run it on your computer:
    python labs/lab2_autograder/grade.py
"""
from __future__ import annotations

import os
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

HERE = Path(__file__).resolve().parent


def run_tests(report: Path) -> int:
    cmd = [sys.executable, "-m", "pytest", str(HERE), "-q", "--tb=short", f"--junitxml={report}"]
    return subprocess.run(cmd, cwd=HERE).returncode


def read_report(report: Path) -> list[tuple[str, bool]]:
    root = ET.parse(report).getroot()
    results = []
    for case in root.iter("testcase"):
        failed = any(child.tag in {"failure", "error"} for child in case)
        results.append((case.get("name", "?"), not failed))
    return results


def summary(results: list[tuple[str, bool]]) -> str:
    passed = sum(ok for _, ok in results)
    lines = [f"## Score: {passed} / {len(results)}", "", "| Test | Result |", "| --- | --- |"]
    lines += [f"| {name} | {'pass' if ok else 'FAIL'} |" for name, ok in results]
    return "\n".join(lines) + "\n"


def main() -> int:
    report = HERE / "junit.xml"
    code = run_tests(report)
    if not report.exists():
        print("pytest produced no report (syntax error in solution.py?)", file=sys.stderr)
        return 1
    results = read_report(report)
    text = summary(results)
    print(text)
    target = os.environ.get("GITHUB_STEP_SUMMARY")
    if target:
        with open(target, "a", encoding="utf-8") as fh:
            fh.write(text)
    return 0 if code == 0 and results and all(ok for _, ok in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
