SELECT p.day,
       CASE
           WHEN COUNT(p.price) >= 3 THEN ROUND(AVG(p.price), 0)
           WHEN COUNT(p.price) < 3 THEN NULL
       END AS average_price
FROM prices p
WHERE p.orig_code = %(origin)s
AND p.dest_code = %(destination)s
AND p.day >= %(date_from)s
AND p.day <= %(date_to)s
GROUP BY p.day

UNION ALL

SELECT p.day,
       CASE
           WHEN COUNT(p.price) >= 3 THEN ROUND(AVG(p.price), 0)
           WHEN COUNT(p.price) < 3 THEN NULL
       END AS average_price
FROM ports r
JOIN prices p
ON r.code = p.dest_code
WHERE p.orig_code = %(origin)s
AND r.parent_slug = %(destination)s
AND p.day >= %(date_from)s
AND p.day <= %(date_to)s
GROUP BY p.day
HAVING COUNT(p.price) >= 3

UNION ALL

SELECT p.day,
       CASE
           WHEN COUNT(p.price) >= 3 THEN ROUND(AVG(p.price), 0)
           WHEN COUNT(p.price) < 3 THEN NULL
       END AS average_price
FROM ports r
JOIN prices p
ON r.code = p.orig_code
WHERE p.dest_code = %(destination)s
AND r.parent_slug = %(origin)s
AND p.day >= %(date_from)s
AND p.day <= %(date_to)s
GROUP BY p.day
HAVING COUNT(p.price) >= 3

UNION ALL

SELECT p.day,
       CASE
           WHEN COUNT(p.price) >= 3 THEN ROUND(AVG(p.price), 0)
           WHEN COUNT(p.price) < 3 THEN NULL
       END AS average_price
FROM ports o
JOIN prices p
ON o.code = p.orig_code
JOIN ports d
ON p.dest_code = d.code
WHERE o.parent_slug = %(origin)s
AND d.parent_slug = %(destination)s
AND p.day >= %(date_from)s
AND p.day <= %(date_to)s
GROUP BY p.day 
HAVING COUNT(p.price) >= 3