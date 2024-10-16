-- SQL script that lists all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, (2022 - formed) AS lifespan FROM metal_bands
WHERE style = 'Glam rock' AND split IS NOT NULL
order BY lifespan DESC;
