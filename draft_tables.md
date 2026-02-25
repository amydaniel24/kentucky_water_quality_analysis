# Draft Table Structure

This document outlines the main tables I expect this project to use and how they relate to each other. This is a planning step meant to clarify structure before building a database.

---

## Table 1: Public Water Systems

**What this table represents:**  
Each row represents a public water system operating in Kentucky.

**Why it matters:**  
Violations are issued to systems, not directly to people. This table provides the system level context.

**Likely columns:**

- pwsid (public water system ID)
- system_name
- county
- system_type
- population_served
- primary_water_source

---

## Table 2: Drinking Water Violations

**What this table represents:**  
Each row represents a violation issued to a public water system under the Safe Drinking Water Act.

**Why it matters:**  
This is the core table used to understand how often systems violate standards and whether those violations are health based.

**Likely columns:**

- violation_id
- pwsid (links to Public Water Systems)
- contaminant_code
- violation_category
- health_based_flag
- violation_date
- compliance_status

---

## Table 3: Contaminants Reference

**What this table represents:**  
Each row represents a regulated contaminant and its identifying information.

**Why it matters:**  
Violation records use contaminant codes. This table explains what those codes mean.

**Likely columns:**

- contaminant_code
- contaminant_name
- contaminant_group
- contaminant_description

---

## Table 4: EPA Drinking Water Standards (MCLs)

**What this table represents:**  
Each row represents an EPA established maximum contaminant level for a regulated substance.

**Why it matters:**  
This table provides health context by showing what levels are considered unsafe and why a contaminant poses a risk.

**Likely columns:**

- contaminant_name
- mcl_value
- unit_of_measure
- health_effect_description
- regulatory_status

---

## How These Tables Relate

- Each public water system can have many violations.
- Each violation is linked to one contaminant.
- Each contaminant may have one associated EPA standard.
- EPA standards help explain why a violation is considered a health risk.

---

## Why This Structure Supports My Questions

This structure allows me to:

- Identify what contaminants are most commonly involved in violations
- Understand whether violations are health based or not
- Add health context by connecting violations to EPA safety standards
- Prepare for future expansion using CDC or FDA health outcome data
