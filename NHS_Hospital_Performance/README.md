# NHS Hospital Performance & Patient Outcomes Tracker

## Project Overview
This project provides an interactive Power BI dashboard to assess hospital performance across NHS trusts using Standardised Hospital Mortality Index (SHMI) data. The analysis identifies clinical outcome trends, highlights hospitals with significantly higher-than-expected mortality, and benchmarks quality ratings across time and geography.

## Data Sources
- **SHMI (Standardised Hospital Mortality Index)**: Cleaned dataset containing observed and expected death counts, mortality index scores, case mix, and mortality bands
- **CQC Ratings**: Official Care Quality Commission ratings for NHS hospitals
- **Admissions**: Cleaned dataset detailing yearly hospital admissions
- **Hospital Lookup**: Mapping table for matching hospital codes to full names and regions

Each dataset has been cleaned and joined to ensure consistency and accurate analysis across time and hospital entities.

## Dashboard Sections

### 1. **Overview**
- High-level KPIs: % Outstanding and Satisfactory Hospitals, Mortality Ratio (%), Total Reporting Hospitals
- Donut chart showing distribution of quality ratings

### 2. **Hospital Rankings**
- Tables ranking hospitals with highest and lowest mortality ratios
- Color-coded for immediate visual contrast (green = better, red = worse)
- Summary table showing hospital quality by region and type

### 3. **Trends Over Time**
- Tracks mortality ratio and number of hospitals reporting annually
- Satisfactory and good/outstanding rating percentages over time
- Highlights recovery or decline in hospital performance

### 4. **Geographic Analysis**
- Map showing hospital performance by region with quality-coded bubbles
- Scatterplot comparing mortality vs % of good/outstanding ratings by region
- Bar chart showing average mortality ratio by region

### 5. **Clinical Outcomes Analysis**
- Scatterplot of observed vs expected deaths
- Mortality Index trends over time by band (10 = high, 30 = low)
- KPIs: % hospitals in high mortality, avg index for Band 10

## Key Findings

- **National mortality ratio is stable (~100%)**, indicating average performance overall.
- However, **34.6% of hospitals fall into the high mortality band**, showing disparities in care outcomes.
- **Top-performing hospitals** have mortality ratios as low as 73%, while the worst reach 116%.
- **London outperforms other regions** with the lowest average mortality ratio and highest % of good ratings.
- **West Midlands shows consistently poor outcomes**, both in ratings and mortality index.
- Mortality index scores across bands remain relatively stable, suggesting systemic differences between high- and low-performing hospitals.

## Tools Used
- **Power BI** for dashboard development and data modeling
- **DAX** for measure creation and ratio calculations
- **Power Query** for data cleaning and type adjustments

---

*This project is part of my Data Analyst Portfolio and demonstrates my skills in data storytelling, dashboard design, healthcare analytics, and advanced Power BI modeling.*

## Author
Gabriele Vertullo
