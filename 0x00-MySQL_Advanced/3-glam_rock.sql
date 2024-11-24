-- SQL script that lists all bands with Glam rock as their main style, ranked by their longevity
-- Column names must be: band_name and lifespan (in years)
-- use attributes formed and split for computing the lifespan

SELECT band_name, 
       -- Compute lifespan by subtracting 'formed' from 'split' (or 2022 if no 'split')
       CASE 
           WHEN split IS NULL THEN 2022 - formed  -- If the band has not split, use 2022
           ELSE split - formed                    -- If the band has split, calculate based on the split year
       END AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'  -- Filter only bands with 'Glam rock' in their style
ORDER BY lifespan DESC;  
