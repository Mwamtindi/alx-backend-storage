-- Task: List all Glam rock bands ranked by their longevity
-- This script retrieves Glam rock bands, calculates their lifespan, and ranks them by longevity in desc order.

-- Select band_name and lifespan of Glam rock bands
SELECT band_name, 
       CASE 
         WHEN split IS NULL THEN 2022 - formed 
         ELSE split - formed 
       END AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
