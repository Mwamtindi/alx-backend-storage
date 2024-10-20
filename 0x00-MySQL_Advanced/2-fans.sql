-- Task: Rank country origins of bands based on the number of non-unique fans
-- This script retrieves and orders band origins by their fan count in descending order.

-- Select origin and the sum of fans for each origin
-- SQL keywords are in uppercase, and the script is commented as per the task requirements.

SELECT origin, SUM(nb_fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
