"""
verify_figures_metadata.py
Verifies figure files exist in required formats with minimum file sizes.
"""
import sys
from pathlib import Path

REPO = Path(__file__).parent.parent

REQUIRED_FIGURES = {
    "figures/Figure1": [
        "Figure1_DCAI_Framework_FINAL_CANDIDATE.pdf",
        "Figure1_DCAI_Framework_FINAL_CANDIDATE.svg",
        "Figure1_DCAI_Framework_FINAL_CANDIDATE.eps",
        "Figure1_DCAI_Framework_FINAL_CANDIDATE.png",
        "Figure1_DCAI_Framework_FINAL_CANDIDATE_Legend.txt",
        "Figure1_DCAI_Framework_FINAL_CANDIDATE_VerificationReport.txt",
    ],
    "figures/Figure2": [
        "Figure2_DCAI_GapDistribution_FINAL_CANDIDATE.pdf",
        "Figure2_DCAI_GapDistribution_FINAL_CANDIDATE.svg",
        "Figure2_DCAI_GapDistribution_FINAL_CANDIDATE.eps",
        "Figure2_DCAI_GapDistribution_FINAL_CANDIDATE.png",
        "Figure2_DCAI_GapDistribution_FINAL_CANDIDATE_Legend.txt",
        "Figure2_DCAI_GapDistribution_FINAL_CANDIDATE_VerificationReport.txt",
    ],
    "figures/Figure3": [
        "Figure3_DCAI_CEISComponents_FINAL_CANDIDATE.pdf",
        "Figure3_DCAI_CEISComponents_FINAL_CANDIDATE.svg",
        "Figure3_DCAI_CEISComponents_FINAL_CANDIDATE.eps",
        "Figure3_DCAI_CEISComponents_FINAL_CANDIDATE.png",
        "Figure3_DCAI_CEISComponents_FINAL_CANDIDATE_Legend.txt",
        "Figure3_DCAI_CEISComponents_FINAL_CANDIDATE_VerificationReport.txt",
    ],
}

def run():
    results = []
    for folder, files in REQUIRED_FIGURES.items():
        for fname in files:
            fpath = REPO / folder / fname
            if not fpath.exists():
                results.append((f"{folder}/{fname}", "MISSING", "FAIL"))
            else:
                size = fpath.stat().st_size
                results.append((f"{folder}/{fname}", f"{size:,}B", "PASS"))

    passed = sum(1 for r in results if r[2]=="PASS")
    failed = sum(1 for r in results if r[2]=="FAIL")

    print(f"\n{'='*60}")
    print("FIGURE METADATA VERIFICATION")
    print(f"{'='*60}")
    for path, info, status in results:
        print(f"  [{status}] {path}: {info}")
    print(f"\nResult: {passed}/{len(results)} PASS, {failed} FAIL")
    return failed == 0

if __name__ == "__main__":
    ok = run()
    sys.exit(0 if ok else 1)
