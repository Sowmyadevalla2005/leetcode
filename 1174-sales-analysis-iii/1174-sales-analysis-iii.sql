SELECT p.product_id, p.product_name
FROM Product p
JOIN Sales s ON p.product_id = s.product_id
WHERE p.product_id NOT IN (
    SELECT s2.product_id
    FROM Sales s2
    WHERE s2.sale_date < '2019-01-01' OR s2.sale_date > '2019-03-31'
)
GROUP BY p.product_id, p.product_name;
