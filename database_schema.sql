DROP DATABASE IF EXISTS ky_water_quality;
CREATE DATABASE ky_water_quality;
USE ky_water_quality;

CREATE TABLE public_water_systems (
    pwsid VARCHAR(20) PRIMARY KEY,
    system_name VARCHAR(255),
    county VARCHAR(100),
    system_type VARCHAR(100),
    population_served INT,
    primary_water_source VARCHAR(100)
);

CREATE TABLE contaminants (
    contaminant_name VARCHAR(150) PRIMARY KEY
);

CREATE TABLE epa_standards (
    contaminant_name VARCHAR(150) PRIMARY KEY,
    mcl VARCHAR(50),
    mcl_or_tt VARCHAR(50),
    health_effect TEXT,
    source_of_contaminant TEXT,
    CONSTRAINT fk_epa_standards_contaminant
        FOREIGN KEY (contaminant_name)
        REFERENCES contaminants(contaminant_name)
);

CREATE TABLE sdwa_violations (
    violation_id VARCHAR(50) PRIMARY KEY,
    pwsid VARCHAR(20),
    contaminant_name VARCHAR(150),
    violation_category VARCHAR(50),
    is_health_based VARCHAR(10),
    noncompl_begin DATE,
    noncompl_end DATE,
    duration_days INT,
    violation_year INT,
    CONSTRAINT fk_sdwa_violations_pwsid
        FOREIGN KEY (pwsid)
        REFERENCES public_water_systems(pwsid),
    CONSTRAINT fk_sdwa_violations_contaminant
        FOREIGN KEY (contaminant_name)
        REFERENCES contaminants(contaminant_name)
);

TRUNCATE TABLE sdwa_violations;

SELECT COUNT(*) FROM sdwa_violations;

SELECT * FROM sdwa_violations LIMIT 10;