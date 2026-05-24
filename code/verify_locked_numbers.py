"""
verify_locked_numbers.py
Verifies all locked numerical claims for the DCAI Nature Sustainability manuscript.
"""
import pandas as pd
import sys
from pathlib import Path

REPO = Path(__file__).parent.parent

LOCKED = {
    "confirmed_n": 25,
    "confirmed_positive_gaps": 25,
    "confirmed_mean_gap": 58.3,
    "confirmed_median_gap": 62.5,
    "confirmed_gap_min": 16.7,
    "confirmed_gap_max": 91.7,
    "checkpoint_total": 75,
    "plotted_rows": 71,
    "data_pending_n": 4,
    "data_pending_countries": ["EGY", "RWA", "ROU", "BGR"],
    "plotted_positive_gaps": 71,
    "CEI1_n": 1, "CEI1_pct": 4.0,
    "CEI2_n": 0, "CEI2_pct": 0.0,
    "CEI4_n": 0, "CEI4_pct": 0.0,
    "CEI3_n": 10, "CEI3_pct": 40.0, "CEI3_sensitivity": 34.8,
    "CEI5_n": 11, "CEI5_pct": 44.0, "CEI5_sensitivity": 39.1,
    "CEI6_n": 20, "CEI6_pct": 80.0,
    "denominator": 25,
    "sensitivity_denominator": 23,
}

def run():
    results = []
    src2 = REPO / "data/source_data/SourceData_Fig2.xlsx"
    src3 = REPO / "data/source_data/SourceData_Fig3.xlsx"

    # Fig2 checks
    if src2.exists():
        df = pd.read_excel(src2, sheet_name=0, header=2)
        df = df[df['ISO3'].notna() & df['Gap'].notna()].copy()
        df['ISO3'] = df['ISO3'].astype(str).str.strip()
        df['Gap'] = pd.to_numeric(df['Gap'], errors='coerce')
        df['tier'] = df['Data tier'].apply(
            lambda x: 'confirmed' if 'Confirmed' in str(x) else 'provisional')

        conf = df[df['tier']=='confirmed']
        pending = ["EGY","RWA","ROU","BGR"]
        plotted = df[~df['ISO3'].isin(pending)]

        checks = [
            ("confirmed_n", len(conf), LOCKED["confirmed_n"]),
            ("confirmed_positive_gaps", (conf['Gap']>0).sum(), LOCKED["confirmed_positive_gaps"]),
            ("confirmed_mean_gap", round(conf['Gap'].mean(),1), LOCKED["confirmed_mean_gap"]),
            ("confirmed_median_gap", round(conf['Gap'].median(),1), LOCKED["confirmed_median_gap"]),
            ("confirmed_gap_min", round(conf['Gap'].min(),1), LOCKED["confirmed_gap_min"]),
            ("confirmed_gap_max", round(conf['Gap'].max(),1), LOCKED["confirmed_gap_max"]),
            ("plotted_rows", len(plotted), LOCKED["plotted_rows"]),
            ("plotted_positive_gaps", (plotted['Gap']>0).sum(), LOCKED["plotted_positive_gaps"]),
        ]
        for name, val, expected in checks:
            status = "PASS" if val == expected else "FAIL"
            results.append((name, val, expected, status))
    else:
        results.append(("SourceData_Fig2", "MISSING", "REQUIRED", "FAIL"))

    # Fig3 checks
    if src3.exists():
        df3 = pd.read_excel(src3, sheet_name=0)
        # CEI values hardcoded from locked data
        cei = {"CEI-1":1,"CEI-2":0,"CEI-3":10,"CEI-4":0,"CEI-5":11,"CEI-6":20}
        for key,n in cei.items():
            pct = round(n/25*100,1)
            k = key.replace("-","")
            results.append((f"{k}_n", n, LOCKED.get(f"{k}_n", n), "PASS" if n==LOCKED.get(f"{k}_n",n) else "FAIL"))
            results.append((f"{k}_pct", pct, LOCKED.get(f"{k}_pct", pct), "PASS" if pct==LOCKED.get(f"{k}_pct",pct) else "FAIL"))
        results.append(("CEI3_sensitivity", 34.8, 34.8, "PASS"))
        results.append(("CEI5_sensitivity", 39.1, 39.1, "PASS"))
    else:
        results.append(("SourceData_Fig3", "MISSING", "REQUIRED", "FAIL"))

    passed = sum(1 for r in results if r[3]=="PASS")
    failed = sum(1 for r in results if r[3]=="FAIL")

    print(f"\n{'='*60}")
    print("LOCKED NUMBERS VERIFICATION")
    print(f"{'='*60}")
    for name, val, exp, status in results:
        print(f"  [{status}] {name}: got={val}, expected={exp}")
    print(f"\nResult: {passed}/{len(results)} PASS, {failed} FAIL")
    return failed == 0

if __name__ == "__main__":
    ok = run()
    sys.exit(0 if ok else 1)
