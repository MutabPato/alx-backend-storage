-- ranks country origins of bands, ordered by the number of (non-unique) fans
-- drop the view if it exists
DROP VIEW IF EXISTS fans;

-- create the view with desired ranking
CREATE VIEW fans AS 
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;

-- display view
SELECT * FROM fans;
