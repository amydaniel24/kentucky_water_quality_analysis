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

