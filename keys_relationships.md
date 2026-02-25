# Keys + Relationships

This document defines the primary keys and foreign keys I plan to use in my database design. This is a planning step before building the ERD and database.

---

## Table: Public Water Systems

**Primary key (PK):**

- pwsid

**Notes:**

- pwsid is the system identifier used across the SDWA data and is the best “main ID” for a water system.

---

## Table: Drinking Water Violations

**Primary key (PK):**

- violation_id

**Foreign keys (FKs):**

- pwsid → Public Water Systems(pwsid)
- contaminant_code → Contaminants Reference(contaminant_code)

**Notes:**

- One system can have many violations.
- Each violation is tied to one main contaminant code (based on the dataset field).

---

## Table: Contaminants Reference

**Primary key (PK):**

- contaminant_code

**Notes:**

- This table exists to translate contaminant codes into names and descriptions.

---

## Table: EPA Drinking Water Standards (MCLs)

**Primary key (PK):**

- contaminant_name (tentative)

**Possible alternate key:**

- contaminant_code (if the standards dataset includes a matching code)

**Notes:**

- If the standards file uses contaminant names only, I will link on contaminant_name.
- If it includes an EPA contaminant code, I will use that instead (more reliable than text matching).

---

# Relationships Summary

## 1) Public Water Systems → Violations

- **Type:** One to Many (1 system has many violations)
- **Link:** pwsid

## 2) Contaminants Reference → Violations

- **Type:** One to Many (1 contaminant can appear in many violations)
- **Link:** contaminant_code

## 3) Standards (MCLs) → Contaminants Reference

- **Type:** One to One or One to Many (depends on the standards file)
- **Link (tentative):** contaminant_name

---

# Risks / Things I Will Verify

- Confirm whether the EPA standards file has contaminant codes or only names.
- Confirm whether contaminant_name strings match cleanly or need standardization.
- Decide whether the standards table should be split (example: some contaminants have multiple rules/units).

## Quick Reality Check (from my datasets)

- pwsid exists in both ky_pub_water_systems.csv and ky_violations_enforcement.csv
- contaminant_code exists in ky_violations_enforcement.csv and is defined in ref_contaminant_codes.csv
- EPA standards file: (I will confirm whether it includes contaminant_code or only contaminant_name)
