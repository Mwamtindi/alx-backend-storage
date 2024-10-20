-- Task: Rank country origins of bands based on the number of non-unique fans
-- This script retrieves and orders band origins by their fan count in descending order.

SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
