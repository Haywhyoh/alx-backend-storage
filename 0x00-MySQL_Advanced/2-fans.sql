-- a SQL script that ranks country origins of bands
-- ordered by the number of (non-unique) fans
SELECT DISTINCT `origin`, SUM(fans) AS `n_fans` FROM `metal_bands`
GROUP BY `origin`
ORDER BY `n_fans` DESC;
