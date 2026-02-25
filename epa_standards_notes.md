# EPA Drinking Water Standards (MCLs)

## What This Dataset Represents

This dataset contains the U.S. Environmental Protection Agency’s Maximum Contaminant Levels (MCLs) for regulated drinking water contaminants. MCLs are legal limits that public water systems must meet under the Safe Drinking Water Act.

These standards are designed to protect public health by setting maximum allowable levels for substances known to cause health problems when exposure occurs over time.

---

## Why This Data Is Included in the Project

My primary dataset shows drinking water violations in Kentucky, including if a violation is flagged as health based. However, that flag alone does not explain what contaminant was involved or why it matters.

This EPA standards dataset adds important context by showing

- Which contaminants are regulated
- What levels are considered unsafe
- The general health risks associated with those contaminants

By including this dataset, I can move beyond counting violations and begin connecting water quality violations to real public health concerns.

---

## Data Source

The data was compiled from the U.S. Environmental Protection Agency’s Drinking Water Regulations and Contaminants tables.

Source:
<https://www.epa.gov/sdwa/drinking-water-regulations-and-contaminants>

The EPA provides this information in a published table rather than a direct CSV download. The table was manually copied, lightly cleaned to remove explanatory text, and saved as a CSV for analysis purposes.

---

## How This Will Be Used Later

In the next phases of this project, this dataset will be used to:

- Provide health context for contaminants found in violation records
- Compare regulated standards to observed violations
- Support future expansion using CDC or FDA health outcome data

At this stage, the dataset is included for planning, documentation, and conceptual design.
