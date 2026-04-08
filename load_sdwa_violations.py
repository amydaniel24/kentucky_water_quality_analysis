from pathlib import Path
from getpass import getpass
import csv
import mysql.connector


csv_path = Path(r"C:\Users\opiej\da_august\kentucky_water_quality_analysis\datasets\SDWA_ky\ky_violations_import_small.csv")


if not csv_path.exists():
    raise FileNotFoundError(f"Could not find file: {csv_path}")

print(f"Using file: {csv_path}")


connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Abc123doe",
    database="ky_water_quality"
)

cursor = connection.cursor()


cursor.execute("TRUNCATE TABLE sdwa_violations;")
connection.commit()
print("Cleared sdwa_violations table.")


insert_sql = """
INSERT INTO sdwa_violations (
    pwsid,
    violation_id,
    noncompl_begin_date,
    noncompl_end_date,
    violation_code,
    violation_category,
    is_health_based,
    contaminant_code
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""


batch = []
batch_size = 5000
total_loaded = 0

with csv_path.open("r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        pwsid = row["PWSID"].strip() if row["PWSID"] else None
        violation_id = row["VIOLATION_ID"].strip() if row["VIOLATION_ID"] else None
        noncompl_begin_date = row["NON_COMPL_PER_BEGIN_DATE"].strip() if row["NON_COMPL_PER_BEGIN_DATE"] else None
        noncompl_end_date = row["NON_COMPL_PER_END_DATE"].strip() if row["NON_COMPL_PER_END_DATE"] else None
        violation_code = row["VIOLATION_CODE"].strip() if row["VIOLATION_CODE"] else None
        violation_category = row["VIOLATION_CATEGORY_CODE"].strip() if row["VIOLATION_CATEGORY_CODE"] else None
        is_health_based = row["IS_HEALTH_BASED_IND"].strip() if row["IS_HEALTH_BASED_IND"] else None
        contaminant_code = row["CONTAMINANT_CODE"].strip() if row["CONTAMINANT_CODE"] else None

        batch.append((
            pwsid,
            violation_id,
            noncompl_begin_date,
            noncompl_end_date,
            violation_code,
            violation_category,
            is_health_based,
            contaminant_code
        ))

        if len(batch) >= batch_size:
            cursor.executemany(insert_sql, batch)
            connection.commit()
            total_loaded += len(batch)
            print(f"Loaded {total_loaded:,} rows...")
            batch.clear()

    if batch:
        cursor.executemany(insert_sql, batch)
        connection.commit()
        total_loaded += len(batch)
        print(f"Loaded {total_loaded:,} rows...")

# final check with fingers firmly crossed 
cursor.execute("SELECT COUNT(*) FROM sdwa_violations;")
final_count = cursor.fetchone()[0]
print(f"Final row count in sdwa_violations: {final_count:,}")

cursor.close()
connection.close()
print("Done.")