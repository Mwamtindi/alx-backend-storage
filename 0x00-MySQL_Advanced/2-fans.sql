-- Task: Rank country origins of bands based on the number of non-unique fans
-- This script retrieves and orders band origins by their fan count in desc ord

-- Select origin and the sum of fans for each origin
-- SQL keywords are in uppercase, the script is commented as per the task req.

SELECT origin, COUNT(DISTINCT b_name) as nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
