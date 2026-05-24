# Digital–Climate Alignment Gap reproducibility package

This repository contains the reproducibility package for the DCAI Nature Sustainability manuscript.
It is separate from the CEE submission repository and contains no CEE submission materials.

## Manuscript

**Title:** The Digital–Climate Alignment Gap: National AI Governance and Climate–Energy Integration Across 75 Countries

**Target journal:** Nature Sustainability

**Status:** FINAL_CANDIDATE — under peer review (private repository)

## Core measures

- **ACI** — AI Capacity Institutionalization
- **CEIS** — Climate–Energy Integration Score
- **Digital–Climate Alignment Gap** = ACI − CEIS

> This study measures policy-document alignment and institutional visibility between national AI strategies and climate–energy documents. It does not model AI energy demand or emissions.

## Locked numerical claims

### Confirmed-tier (n = 25)
- 25/25 positive ACI−CEIS gaps
- Mean gap = 58.3 percentage points
- Median gap = 62.5 percentage points
- Range = 16.7–91.7 percentage points

### Broader checkpoint
- 75-country checkpoint
- 71 plotted rows (4 data-pending not plotted: EGY, RWA, ROU, BGR)
- 71/71 plotted rows positive ACI−CEIS gaps

### CEIS components (confirmed-tier n = 25)
| Component | n | % | Note |
|-----------|---|---|------|
| CEI-1 | 1/25 | 4% | |
| CEI-2 | 0/25 | 0% | |
| CEI-4 | 0/25 | 0% | |
| CEI-3 | 10/25 | 40% | Sensitivity excl. CHN/ARE = 34.8% |
| CEI-5 | 11/25 | 44% | Sensitivity excl. CHN/ARE = 39.1% |
| CEI-6 | 20/25 | 80% | |

## Figures

| Figure | Role |
|--------|------|
| Figure 1 | Conceptual framework and confirmed-tier Digital–Climate Alignment Gap |
| Figure 2 | 75-country checkpoint → 71 plotted rows → 71/71 positive ACI−CEIS gaps |
| Figure 3 | CEIS component diagnostic: sparse strategic alignment, partial implementation/coordination, common reporting visibility |

## Repository structure

```
DCAI_NatureSustainability/
├── README.md
├── CITATION.cff
├── LICENSE
├── requirements.txt
├── environment.yml
├── data/
│   ├── source_data/          # SourceData_Fig2, Fig3, Table1, Table2
│   └── supplementary_tables/ # Integrated supplementary tables
├── figures/
│   ├── Figure1/              # PDF, SVG, EPS, PNG, Legend, VR
│   ├── Figure2/              # PDF, SVG, EPS, PNG, Legend, VR
│   └── Figure3/              # PDF, SVG, EPS, PNG, Legend, VR
├── tables/
│   ├── main_tables/
│   └── supplementary_tables/
├── supplementary_information/
├── code/                     # Verification and manifest scripts
├── qc_reports/               # Generated QC outputs
├── availability/             # Data and Code Availability statements
└── release_notes/
```

The package supports verification of:
- ACI, CEIS, and Digital–Climate Alignment Gap
- Source data integrity
- Main figures and figure metadata
- Main tables and supplementary tables
- Supplementary information
- Locked numerical claims
- File manifests and checksums

## Reproducibility check

```bash
pip install -r requirements.txt
python code/run_all_checks.py
```

Expected output: `ALL CHECKS PASSED`

## Availability

This repository is private during peer review.
Upon acceptance or final publication-stage release, the repository will be made publicly available or archived with a persistent DOI.

**Note:** This repository is separate from the CEE submission repository (`AI_Infrastructure_Governance`) and contains DCAI reproducibility materials only.
