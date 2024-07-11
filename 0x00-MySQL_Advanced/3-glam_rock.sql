-- lists all bands with Glam rock as their main style, ranked by their longevity
-- drop the view if it exists
DROP VIEW IF EXISTS bands;

-- create the view with desired ranking
CREATE VIEW bands AS
SELECT band_name,
	CASE
		WHEN split IS NOT NULL THEN 2022 - formed
		ELSE 2022 - formed
	END AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;

-- display view
SELECT * FROM bands;
