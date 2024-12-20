-- Task: Rank country origins of metal bands, ordered by the number of non-unique fans
SELECT origin, 
       SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin               -- Group by country of origin
ORDER BY nb_fans DESC;     -- Order by the total number of fans, in descending order
