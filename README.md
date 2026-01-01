# Kentucky Water Quality Analysis

## Project Overview
This project is being developed to look at what kinds of violations are occurring in Kentucky’s drinking water systems using the **EPA Safe Drinking Water Act (SDWA) violations** government dataset for public water systems.

This repository is currently focusing on data loading, inspection, cleaning, and project setup.

---

## Data Sources
**Primary Source**
- EPA Safe Drinking Water Act (SDWA) Violations and Enforcement Dataset

The original EPA SDWA dataset includes multiple large CSV files covering violations, public water systems, site visits, service areas, and reference tables at the national level.

---

## Important Data Handling Decision

### What Went Wrong
When I downloaded the SDWA data, I included the **full national dataset**, which contains very large CSV files. One of the files was over **4 GB** in size.

This caused several issues:
- GitHub does not allow files larger than 2 GB
- Git pushes failed even after removing the files 
- Git history continued to look at the large files from the past and would not allow me to push.

---

### How I Fixed It
I made the executive desicion to extract only Kentucky data and have Git track that instead of the full SDWA dataset:

1. **Ignored the full raw dataset**
   - The full SDWA dataset is excluded using `.gitignore`
   - This prevents accidental commits

2. **Created Kentucky-only extracts**
   - A script (`make_ky_extracts.py`) was written to:
     - Load the raw SDWA data locally
     - Filter records to **Kentucky only**
     - Create smaller CSV files

3. **Stored only extracted data in the repository**
   - The repository includes only the following data files:
     - `ky_violations_enforcement.csv`
     - `ky_pub_water_systems.csv`
     - `ref_contaminant_codes.csv`

4. **Reset the Git history**
   - The repository history was reset to change the past and begin with a clean slate.
   - I was finally able to push again.

This was something that I did in my previous position. We would pull data or columns or rows that we needed to analyze and leave the rest of the data behind.


### Data Included in This Repository
- `ky_violations_enforcement.csv`
- `ky_pub_water_systems.csv`
- `ref_contaminant_codes.csv`

---

## Project Structure

kentucky_water_quality_analysis/
│
├── datasets/
│ └── SDWA_ky/
│ ├── ky_violations_enforcement.csv
│ ├── ky_pub_water_systems.csv
│ └── ref_contaminant_codes.csv
│
├── notebooks/
│ └── keystone_water_ky.ipynb
│
├── make_ky_extracts.py
├── README.md
├── requirements.txt
└── .gitignore


---


---

## Keystone Project – Week 1 Focus
Week 1 focused on getting the data into a usable state.

Key tasks included:
- Loading CSV data using Pandas
- Inspecting dataset size, structure, and data types
- Exploring categorical and numeric columns
- Assessing missing data
- Renaming columns for clarity
- Converting date fields to datetime format
- Verifying that all violation records were Kentucky-only
- Establishing a clean and functional GitHub repository

No conclusions were drawn at this stage. The emphasis was on understanding the data for later analysis.

---

## Keystone Project – Week 2 Focus (EDA + Visualizations)
Week 2 expanded on the initial setup by performing exploratory data analysis (EDA) and creating early visualizations to identify patterns and guide the project’s direction.

Key tasks included:
- Continuing data cleaning and validation
- Grouping and aggregating data to explore violation categories and trends
- Examining health based versus non health based violations
- Exploring severity indicators and noncompliance timelines
- Creating multiple types of visualizations:
  - Bar charts for comparison
  - A line chart to examine changes over time
  - Distribution plots (histogram and boxplot) to assess severity and spread
- Saving visualizations to a dedicated `plots/` folder

This exploratory work led to a focused analysis question for future stages of the project:

## Emerging Analysis Question

Based on the EDA done so far, the main question for this project is:

**Which contaminants appear most frequently in Kentucky drinking water violations?**


The next steps will involve linking violations to contaminants and looking at their potential impact on public health.

---

## Requirements
All required Python packages for this project are listed in `requirements.txt`.