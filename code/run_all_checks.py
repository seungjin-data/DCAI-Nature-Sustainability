"""
run_all_checks.py
Master reproducibility check runner for DCAI Nature Sustainability.
Runs all verification scripts and writes final QC report.
"""
import sys, subprocess
from pathlib import Path
from datetime import datetime

REPO = Path(__file__).parent.parent
QC = REPO / "qc_reports"
QC.mkdir(exist_ok=True)

SCRIPTS = [
    ("verify_locked_numbers.py",  "Locked numerical claims"),
    ("verify_source_data.py",     "Source data files"),
    ("verify_figures_metadata.py","Figure file metadata"),
    ("build_manifest.py",         "File manifest and checksums"),
]

def run():
    report_lines = [
        "DCAI Nature Sustainability — Reproducibility Verification Report",
        "="*65,
        f"Generated: {datetime.now().isoformat()}",
        f"Repository: https://github.com/seungjin-data/DCAI-Nature-Sustainability",
        "",
    ]

    all_passed = True
    for script, label in SCRIPTS:
        script_path = REPO / "code" / script
        print(f"\nRunning: {script}")
        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True, text=True
        )
        passed = result.returncode == 0
        if not passed:
            all_passed = False
        status = "PASS" if passed else "FAIL"
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        report_lines.append(f"[{status}] {label} ({script})")
        report_lines.append(result.stdout)

    report_lines.append("")
    report_lines.append("="*65)
    final = "ALL CHECKS PASSED" if all_passed else "CHECKS FAILED"
    report_lines.append(final)

    report_path = QC / "DCAI_Reproducibility_VerificationReport.txt"
    with open(report_path, "w") as f:
        f.write("\n".join(report_lines))

    print(f"\n{'='*65}")
    print(final)
    print(f"Report: {report_path.relative_to(REPO)}")
    return all_passed

if __name__ == "__main__":
    ok = run()
    sys.exit(0 if ok else 1)
