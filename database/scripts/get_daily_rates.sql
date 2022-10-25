SELECT p.day, ROUND(AVG(p.price),2) AS average_price
FROM prices p
WHERE p.orig_code = %s
AND p.dest_code = %s
AND p.day >= %s
AND p.day <= %s
GROUP BY p.day