# Digital–Climate Alignment Gap
## Reproducibility Package — Nature Sustainability

This repository contains the reproducibility package for the manuscript:

**"The Digital–Climate Alignment Gap: Measuring the Misalignment Between National AI Governance and Climate–Energy Integration Across 75 Countries"**

Submitted to *Nature Sustainability*.

---

## Research overview

This study introduces the **Digital–Climate Alignment Gap** — the difference between how rapidly countries are institutionalizing AI capacity and how comprehensively they are integrating AI considerations into their climate and energy governance frameworks.

The study does not model AI energy demand or carbon emissions. It measures **policy-document alignment** and **institutional visibility** between national AI strategies and climate–energy governance documents across 75 countries.

### Core measures

| Measure | Definition |
|---------|-----------|
| **ACI** | AI Capacity Institutionalization — extent to which a country has established institutional frameworks for AI development |
| **CEIS** | Climate–Energy Integration Score — extent to which AI considerations are integrated into climate and energy governance documents |
| **Alignment Gap** | ACI − CEIS |

### Key finding

Across all 71 plotted country rows, ACI exceeds CEIS — the alignment gap is **positive in 71/71 cases**. Among 25 confirmed-tier countries, the mean gap is **58.3 percentage points** (range: 16.7–91.7 pp), indicating that AI governance is systematically outpacing climate–energy governance integration worldwide.

---

## Confirmed-tier results (n = 25)

| Statistic | Value |
|-----------|-------|
| Positive alignment gaps | 25/25 |
| Mean gap | 58.3 pp |
| Median gap | 62.5 pp |
| Range | 16.7–91.7 pp |

### Broader checkpoint (n = 75)

- 75-country checkpoint
- 71 plotted rows (4 data-pending excluded: EGY, RWA, ROU, BGR)
- 71/71 plotted rows show positive ACI−CEIS gaps

---

## CEIS component prevalence (confirmed-tier, n = 25)

Components are grouped by CEIS function, not numeric order.

| Function | Component | Description | n | % |
|----------|-----------|-------------|---|---|
| Strategic alignment | CEI-1 | AI/digital in NDC or LT-LEDS | 1/25 | 4% |
| Strategic alignment | CEI-2 | AI strategy: energy/climate targets | 0/25 | 0% |
| Strategic alignment | CEI-4 | AI/data-centre carbon pricing | 0/25 | 0% |
| Implementation | CEI-3 | Data-centre energy efficiency mandate | 10/25 | 40% |
| Implementation | CEI-5 | AI–climate coordination | 11/25 | 44% |
| Reporting visibility | CEI-6 | Mandatory carbon reporting | 20/25 | 80% |

Sensitivity analysis excluding CHN and ARE (n = 23): CEI-3 = 34.8%, CEI-5 = 39.1%

---

## Figures

| Figure | Content |
|--------|---------|
| **Figure 1** | Conceptual framework: ACI/CEIS measurement structure and confirmed-tier alignment gap |
| **Figure 2** | 75-country checkpoint → 71 plotted rows → 71/71 positive ACI−CEIS gaps |
| **Figure 3** | CEIS component diagnostic: sparse strategic alignment, partial implementation/coordination, common reporting visibility |

---

## Repository structure

```
DCAI-Nature-Sustainability/
├── data/
│   ├── source_data/             # SourceData for Figures and Tables
│   └── supplementary_tables/    # Integrated supplementary tables
├── figures/
│   ├── Figure1/                 # PDF, SVG, EPS, PNG, Legend, VerificationReport
│   ├── Figure2/                 # PDF, SVG, EPS, PNG, Legend, VerificationReport
│   └── Figure3/                 # PDF, SVG, EPS, PNG, Legend, VerificationReport
├── tables/
│   ├── main_tables/
│   └── supplementary_tables/
├── supplementary_information/
├── code/                        # Reproducibility verification scripts
├── qc_reports/                  # QC outputs, manifest, checksums
├── availability/                # Data and Code Availability statements
└── release_notes/
```

---

## Reproducibility check

```bash
pip install -r requirements.txt
python code/run_all_checks.py
```

Expected output: `ALL CHECKS PASSED`

The script verifies locked numerical claims, source data integrity, figure file metadata, and generates the file manifest with SHA256 checksums.

---

## Data and code availability

Source data supporting the figures and tables are provided in `data/source_data/`.
Upon publication, this repository will be archived with a persistent DOI.
The final release tag, commit hash, and archival DOI will be inserted before publication.
