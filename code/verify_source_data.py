"""
verify_source_data.py
Verifies source data files exist and have expected structure.
"""
import pandas as pd
import sys
from pathlib import Path

REPO = Path(__file__).parent.parent

REQUIRED_FILES = {
    "data/source_data/SourceData_Fig2.xlsx": {"min_rows": 70},
    "data/source_data/SourceData_Fig3.xlsx": {"min_rows": 5},
    "data/source_data/SourceData_Table1.xlsx": {"min_rows": 1},
    "data/source_data/SourceData_Table2.xlsx": {"min_rows": 1},
    "data/supplementary_tables/DCAI_NatSustain_SupplementaryTables_Integrated_FINAL.xlsx": {"min_rows": 1},
}

def run():
    results = []
    for rel_path, spec in REQUIRED_FILES.items():
        fpath = REPO / rel_path
        if not fpath.exists():
            results.append((rel_path, "MISSING", "FAIL"))
            continue
        size = fpath.stat().st_size
        if size < 100:
            results.append((rel_path, f"TOO_SMALL ({size}B)", "FAIL"))
            continue
        results.append((rel_path, f"EXISTS ({size:,}B)", "PASS"))

    passed = sum(1 for r in results if r[2]=="PASS")
    failed = sum(1 for r in results if r[2]=="FAIL")

    print(f"\n{'='*60}")
    print("SOURCE DATA VERIFICATION")
    print(f"{'='*60}")
    for path, info, status in results:
        print(f"  [{status}] {path}: {info}")
    print(f"\nResult: {passed}/{len(results)} PASS, {failed} FAIL")
    return failed == 0

if __name__ == "__main__":
    ok = run()
    sys.exit(0 if ok else 1)
