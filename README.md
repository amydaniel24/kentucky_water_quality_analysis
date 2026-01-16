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

## Keystone Week 1 Focus (Loading + Cleaning)
Week 1 focused on getting the SDWA data into a workable state:
- Loaded CSVs with Pandas
- Looked at structure with `.head()`, `.info()`, `.shape()`
- Looked at categorical and numeric columns
- Checked missing values and data type issues
- Renamed key columns 
- Converted date fields to datetime
- Verified Kentucky only records using PWSID/state matching
- Setup GitHub repo structure

---

## Keystone Week 2 Focus (EDA + Early Visualizations)
Week 2 focused on exploratory questions and visuals:
- Which violation categories are most common in Kentucky?
- How many violations are health based vs not health based?
- How have violations changed over time?

Visuals:
- Bar chart: violation category counts
- Bar chart: health-based vs non health-based
- Line chart: violations over time by year

---

## Keystone Week 4 Focus (Advanced Visualizations + Visual Integrity)
Week 4 focused on polishing visuals and applying ethical visualization principles:
- Improved labels and titles
- Added context and limitations
- Added a distribution chart (boxplot) and a relationship chart (scatterplot)
- Created a `save_plot()` helper and saved exported charts to the `plots/` folder

Polished visuals:
- **Comparison:** violation category counts and percent view
- **Pattern:** violations over time (line chart)
- **Distribution:** noncompliance duration days by health based flag (boxplot, capped at 95th percentile and labeled)
- **Relationship:** contaminant frequency vs percent flagged as health based (scatterplot)

---

## Requirements
All required Python packages are listed in `requirements.txt`.
