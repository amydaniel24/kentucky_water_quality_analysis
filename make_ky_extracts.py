import pandas as pd
from pathlib import Path

project_root = Path(__file__).parent
full_data = project_root / "datasets" / "SDWA_dataset"  # local full dataset (ignored by git)
out_folder = project_root / "datasets" / "SDWA_ky"
out_folder.mkdir(parents=True, exist_ok=True)

violations_path = full_data / "SDWA_VIOLATIONS_ENFORCEMENT.csv"
systems_path = full_data / "SDWA_PUB_WATER_SYSTEMS.csv"
codes_path = full_data / "SDWA_REF_CODE_VALUES.csv"

print("Loading systems...")
systems = pd.read_csv(systems_path, low_memory=False)
systems_ky = systems[systems["STATE_CODE"] == "KY"].copy()

print("Saving ky_pub_water_systems.csv")
systems_ky.to_csv(out_folder / "ky_pub_water_systems.csv", index=False)

print("Loading violations (this can take a bit)...")
# Read violations in chunks so we do not blow up memory
chunks = pd.read_csv(violations_path, low_memory=False, chunksize=200000)

ky_pwsids = set(systems_ky["PWSID"].astype(str))

ky_chunks = []
for chunk in chunks:
    chunk["PWSID"] = chunk["PWSID"].astype(str)
    ky_chunk = chunk[chunk["PWSID"].isin(ky_pwsids)]
    if not ky_chunk.empty:
        ky_chunks.append(ky_chunk)

violations_ky = pd.concat(ky_chunks, ignore_index=True)

print("Saving ky_violations_enforcement.csv")
violations_ky.to_csv(out_folder / "ky_violations_enforcement.csv", index=False)

print("Loading code values...")
codes = pd.read_csv(codes_path, low_memory=False)
contaminants = codes[codes["VALUE_TYPE"] == "CONTAMINANT_CODE"].copy()

print("Saving ref_contaminant_codes.csv")
contaminants.to_csv(out_folder / "ref_contaminant_codes.csv", index=False)

print("Done. KY extracts are in datasets/SDWA_ky/")
