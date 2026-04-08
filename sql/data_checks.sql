-- Check for orphan pwsid values
SELECT COUNT(*) 
FROM sdwa_violations v
LEFT JOIN public_water_systems p
ON v.pwsid = p.pwsid
WHERE p.pwsid IS NULL;

-- Check contaminant matches
SELECT COUNT(*)
FROM sdwa_violations v
LEFT JOIN contaminants c
ON v.contaminant_code = c.contaminant_code
WHERE c.contaminant_code IS NULL;