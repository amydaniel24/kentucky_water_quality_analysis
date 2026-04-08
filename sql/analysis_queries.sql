-- Top water systems by violations
SELECT 
    v.pwsid,
    p.system_name,
    COUNT(*) AS violation_count
FROM sdwa_violations v
JOIN public_water_systems p
ON v.pwsid = p.pwsid
GROUP BY v.pwsid, p.system_name
ORDER BY violation_count DESC
LIMIT 10;

-- Top contaminants in violations
SELECT 
    v.contaminant_code,
    c.contaminant_name,
    COUNT(*) AS violation_count
FROM sdwa_violations v
JOIN contaminants c
ON v.contaminant_code = c.contaminant_code
GROUP BY v.contaminant_code, c.contaminant_name
ORDER BY violation_count DESC
LIMIT 10;

-- Most common contaminants in Kentucky violations

SELECT 
    v.contaminant_code,
    c.contaminant_name,
    COUNT(*) AS violation_count
FROM sdwa_violations v
JOIN contaminants c
ON v.contaminant_code = c.contaminant_code
GROUP BY v.contaminant_code, c.contaminant_name
ORDER BY violation_count DESC
LIMIT 10;