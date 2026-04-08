ALTER TABLE sdwa_violations
ADD CONSTRAINT fk_sdwa_violations_pwsid
FOREIGN KEY (pwsid)
REFERENCES public_water_systems(pwsid);


