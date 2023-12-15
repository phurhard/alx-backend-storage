-- This script returns the list of bands origin ordered by thier number of fans
-- We'll need to first find the origins, and add all thefans of each origin

CREATE VIEW fans_origin AS
SELECT origin, fans FROM metal_bands
WHERE 
SELECT origin, fans AS nb_fans FROM metal_bands ORDER BY nb_fans 