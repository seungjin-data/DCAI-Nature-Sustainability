"""
run_all_checks.py
Master reproducibility runner for DCAI npj Climate Action.
Execution order: reproduce → verify → manifest

Step 1: Reproduce figures from source data
Step 2: Verify locked numerical claims against source data
Step 3: Verify source data file integrity
Step 4: Verify figure file metadata
Step 5: Build file manifest and checksums
"""
import sys, subprocess
from pathlib import Path
from datetime import datetime

REPO = Path(__file__).parent.parent
QC   = REPO / "qc_reports"
QC.mkdir(exist_ok=True)

SCRIPTS = [
    ("reproduce_figure2.py",      "Reproduce Figure 2 from source data"),
    ("reproduce_figure3.py",      "Reproduce Figure 3 from source data"),
    ("verify_reproduction.py",    "Verify reproduction outputs"),
    ("verify_locked_numbers.py",  "Verify locked numerical claims"),
    ("verify_source_data.py",     "Verify source data file integrity"),
    ("verify_figures_metadata.py","Verify figure file metadata"),
    ("build_manifest.py",         "Build manifest and checksums"),
]

def run():
    report = [
        "DCAI npj Climate Action — Reproducibility Verification Report",
        "="*65,
        f"Generated : {datetime.now().isoformat()}",
        f"Repository: https://github.com/seungjin-data/DCAI-npj-Climate-Action",
        f"Branch    : final-candidate",
        "",
        "Execution order:",
        "  1. Reproduce figures from source data",
        "  2. Verify reproduction outputs",
        "  3. Verify locked numerical claims",
        "  4. Verify source data integrity",
        "  5. Verify figure file metadata",
        "  6. Build manifest and checksums",
        "",
    ]

    all_passed = True
    for script, label in SCRIPTS:
        script_path = REPO / "code" / script
        print(f"\n{'─'*60}")
        print(f"Running: {script}")
        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True, text=True
        )
        passed = result.returncode == 0
        if not passed:
            all_passed = False
        status = "PASS" if passed else "FAIL"
        print(result.stdout)
        if result.stderr and result.returncode != 0:
            print("STDERR:", result.stderr[:200])
        report.append(f"[{status}] {label}")
        if result.stdout.strip():
            report.append(result.stdout.strip())
        report.append("")

    report += ["="*65, "ALL CHECKS PASSED" if all_passed else "CHECKS FAILED"]

    report_path = QC / "DCAI_Reproducibility_VerificationReport.txt"
    with open(report_path, "w") as f:
        f.write("\n".join(report))

    final = "ALL CHECKS PASSED" if all_passed else "CHECKS FAILED"
    print(f"\n{'='*65}")
    print(final)
    print(f"Report saved: {report_path.relative_to(REPO)}")
    return all_passed

if __name__ == "__main__":
    ok = run()
    sys.exit(0 if ok else 1)
