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

## Keystone Week 1 Focus
This step of the project focuses on:

- Loading CSV data using Pandas
- Inspecting the dataset with `.head()`, `.info()`, and `.shape`
- Exploring categorical and numeric columns
- Finding missing values and data type issues
- Renaming columns 
- Converting date columns to datetime format
- Establishing a clean GitHub repository

No final conclusions are drawn at this stage. The emphasis is on **process, structure, and understanding the data**.

---


## Requirements
All required Python packages are listed in `requirements.txt`.
