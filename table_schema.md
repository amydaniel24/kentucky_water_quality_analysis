# Table Schema (Conceptual Design)

This document outlines the main tables I plan to use in my  project and how they connect to each other. This is based on the datasets I am currently working with and will guide how I build the database later.

---

## Table 1: Public Water Systems

**What this table represents:**  
Each row represents a public water system in Kentucky.

**Primary Key:**
- pwsid

**Why this matters:**  
Violations are issued to water systems. This table allows me to identify which systems are responsible for violations and look for patterns over time.

---

## Table 2: SDWA Violations

**What this table represents:**  
Each row represents a violation recorded under the Safe Drinking Water Act.

**Primary Key:**
- violation_id

**Foreign Keys:**
- pwsid → Public Water Systems(pwsid)
- contaminant_name → Contaminants(contaminant_name)

**Why this matters:**  
This is the main dataset I am analyzing. It shows when violations occur, what contaminant is involved, and whether the violation is health based.

---

## Table 3: Contaminants

**What this table represents:**  
Each row represents a regulated drinking water contaminant.

**Primary Key:**
- contaminant_name

**Why this matters:**  
This table helps standardize contaminant names and acts as the link between violations and EPA standards.

---

## Table 4: EPA Drinking Water Standards (MCLs)

**What this table represents:**  
Each row represents an EPA regulatory standard for a contaminant.

**Primary Key:**
- contaminant_name

**Why this matters:**  
This table provides the health context behind violations by showing what levels are considered unsafe and what the potential health effects are.

---

# Relationships Between Tables

## Public Water Systems → Violations
- One system can have many violations
- Connected by: pwsid

## Contaminants → Violations
- One contaminant can appear in many violations
- Connected by: contaminant_name

## Contaminants → EPA Standards
- Each contaminant has one associated EPA standard
- Connected by: contaminant_name

---

# Notes and Assumptions

- Contaminant names will need to be cleaned and standardized before joining datasets.
- Some contaminants use abbreviations (like TTHM and HAA5) and may require mapping to full names.
- The EPA standards dataset does not include contaminant codes, so joins will be based on text fields.

---

# Why This Structure Works

This structure allows me to:
- Track which contaminants are most frequently involved in violations
- Identify which violations are considered health-based
- Add regulatory and health context using EPA standards
- Prepare for future expansion using CDC or FDA health data