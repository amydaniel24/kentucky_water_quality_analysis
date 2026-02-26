# Connecting SDWA Violations to EPA Drinking Water Standards

## Why This Matters

The main question I am trying to answer with this project is: what is in Kentucky’s drinking water, and how does it affect public health.

The SDWA violations dataset tells me when water systems break the rules, but it does not clearly explain what those rules mean in terms of health. To add that context, I brought in a second dataset from the EPA that lists **Maximum Contaminant Levels (MCLs)** and known health effects for common drinking water contaminants.

This allows me to stop just counting violations and begin explaining why violations matter.

---

## Datasets Used

### 1. SDWA Violations and Enforcement (Kentucky Only)

This dataset contains records of drinking water violations for public water systems in Kentucky. Key fields include:

- Contaminant name
- Violation type
- Health based flag
- Violation dates

This dataset answers the question:  

Which contaminants are showing up in violations and how often?

---

### 2. EPA Drinking Water Maximum Contaminant Levels (MCLs)

This dataset provides EPA regulatory standards for drinking water contaminants, including:

- Contaminant name
- Maximum allowable level (MCL or Treatment Technique)
- Known or potential health effects
- Common sources of contamination

This dataset answers the question:  

What health risks are associated with these contaminants and how are they regulated?

---

## How the Datasets Connect

The two datasets overlap at the contaminant level.

Many contaminants in the SDWA violations dataset appear by name in the EPA standards table including:

- Cryptosporidium
- Giardia lamblia
- Turbidity
- Lead
- Arsenic
- Total Coliforms

Some contaminants use abbreviations or slightly different wording (for example, **TTHM** and **HAA5**). These differences are common in real world data and will be handled by cleaning and mapping contaminant names before joining the datasets.

---

## Planned Join Strategy  

The datasets will be connected using a cleaned contaminant name field.

Steps:

1. Standardize contaminant names (lowercase, trimmed text)
2. Map abbreviated names (such as TTHM and HAA5) to their full EPA standard names
3. Join the datasets so each violation record can be paired with:
   - Its EPA regulatory limit
   - Known health effects
   - Common contamination sources

This approach allows violations to be interpreted in a health and regulatory context instead of standing alone as raw counts.

---

## How This Supports the Overall Story

By combining these datasets I can begin answering more meaningful questions such as:

- Which contaminants are most commonly violating EPA standards in Kentucky?
- Which violations are associated with known long term health risks?
- Are some contaminants repeatedly flagged without resolution?

This connection lays the groundwork for later analysis and helps turn compliance data into a clearer public health story.

---

## Notes and Limitations

- The EPA standards dataset does not contain measured contaminant levels for individual water systems, only regulatory limits.
- Health based flags in the SDWA data indicate regulatory concern not confirmed illness.
- Future work may include adding CDC or FDA health outcome data to better connect violations to real world disease trends.
