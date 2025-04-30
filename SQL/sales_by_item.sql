
SELECT
    item_name,
    SUM(quantity) AS total_units_sold,
    SUM(transaction_amount) AS total_revenue,
    ROUND(AVG(item_price), 2) AS avg_price
FROM raw_balaji_sales
GROUP BY item_name
ORDER BY total_units_sold DESC;
