# Governing AI for Climate Action
## Reproducibility Package — npj Climate Action

This repository contains the reproducibility package for the manuscript:

**"Governing AI for Climate Action: Cross-National Evidence from Digital–Climate Policy Alignment Gaps"**

Submitted to *npj Climate Action* (Springer Nature).
Submission ID: baaefced-0bbb-4a9c-a9b3-2ae230158e7b

Corresponding author: Seungjin Kim (d.eng.kim@stud.assist.ac.kr)
Affiliation: Institute for Industrial Policy Studies (IPS), Seoul, Republic of Korea
ORCID: https://orcid.org/0009-0007-6876-0777

---

## Research overview

This study introduces the **Digital–Climate Alignment Gap** — the difference between how rapidly countries are institutionalising AI capacity and how comprehensively they are integrating AI implications into their climate and energy governance frameworks.

The study does not model AI energy demand or carbon emissions. It measures **policy-document alignment** and **institutional visibility** between national AI strategies and climate–energy governance documents across 75 countries.

### Core measures

| Measure | Definition |
|---------|-----------|
| **ACI** | AI Capacity Institutionalisation — extent to which a country has formally institutionalised AI as a strategic, industrial and infrastructure policy priority |
| **CEIS** | Climate–Energy Integration Score — extent to which AI-related energy and climate implications are integrated into climate–energy governance documents |
| **Alignment Gap** | ACI% − CEIS% (percentage points) |

### Key finding

Across all 71 plotted country rows, ACI exceeds CEIS — the alignment gap is **positive in 71/71 cases**. Among 25 confirmed-tier countries, the mean gap is **58.3 percentage points** (median: 62.5 pp; range: 16.7–91.7 pp), indicating that AI governance is systematically outpacing climate–energy governance integration.

---

## Confirmed-tier results (n = 25)

| Statistic | Value |
|-----------|-------|
| Positive alignment gaps | 25/25 |
| Mean gap | 58.3 pp |
| Median gap | 62.5 pp |
| Range | 16.7–91.7 pp |

### 75-country checkpoint

- 75-country checkpoint
- 71 plotted rows (4 data-pending excluded: EGY, RWA, ROU, BGR)
- 71/71 plotted rows show positive ACI−CEIS gaps
- Checkpoint-only rows (n=46) provide directional support; not used in principal analysis

---

## CEIS component prevalence (confirmed-tier, n = 25)

| Component | Description | Prevalence |
|-----------|-------------|-----------|
| CEI-1 | AI/digital evidence in NDCs or LT-LEDS | 4.0% (1/25) — BRA only |
| CEI-2 | AI strategy links to energy/climate targets | 0.0% (0/25) |
| CEI-3 | Data-centre/AI energy-efficiency mandate | 40.0% (10/25) |
| CEI-4 | Carbon pricing on AI/data-centre operations | 0.0% (0/25) |
| CEI-5 | Cross-ministerial AI–climate coordination | 44.0% (11/25) |
| CEI-6 | Mandatory carbon reporting for AI/data centres | 80.0% (20/25) |

*CEI-3 and CEI-5: sensitivity values excluding CHN/ARE = 34.8% and 39.1% respectively.*

---

## Index formulas

```
ACI% = (ACI-1 + ACI-2 + ACI-3 + ACI-4) / 8 × 100
CEIS% = (CEI-1 + CEI-2 + CEI-3 + CEI-4 + CEI-5 + CEI-6) / 12 × 100
Gap (pp) = ACI% − CEIS%
```

ACI-1 and ACI-2 are ordinal (0, 1, 2, 3); ACI-3 and ACI-4 are binary (0/1).
CEI-3 is ordinal (0, 1, 2); all other CEIS components are binary (0/1).

---

## Repository contents

| Directory/File | Contents |
|---------------|---------|
| `data/` | Confirmed-tier and checkpoint datasets |
| `code/` | Reproducibility and verification scripts |
| `figures/` | Figure source files |
| `tables/` | Table source files |
| `supplementary_information/` | Supplementary materials |
| `availability/` | Data and code availability statements |
| `qc_reports/` | Quality control reports |
| `release_notes/` | Release and version notes |

---

## Submission history

| Journal | Status |
|---------|--------|
| *Nature Sustainability* (NATSUSTAIN-26054138) | Editorial decline without external review |
| *npj Climate Action* (baaefced-0bbb-4a9c-a9b3-2ae230158e7b) | **Under review** |

---

## License

See LICENSE file for terms of use.

## Citation

See CITATION.cff for citation information.
