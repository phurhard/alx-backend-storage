-- This script returns the list of bands origin ordered by thier number of fans
-- We'll need to first find the origins, and add all thefans of each origin

SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands GROUP BY origin ORDER BY nb_fans DESC;
