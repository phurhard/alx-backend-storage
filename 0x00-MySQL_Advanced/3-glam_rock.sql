-- This script lists all bands with glam rock as theri main style
-- ranked by their longevity

SELECT band_name, COALESCE(split, 2022) - formed AS lifespan
FROM metal_bands GROUP BY style='Glam rock' ORDER BY lifespan DESC;
-- WHERE style=Glam rock;
