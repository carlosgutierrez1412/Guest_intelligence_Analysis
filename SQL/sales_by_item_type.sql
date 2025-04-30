
SELECT
    item_type,
    SUM(quantity) AS total_units_sold,
    SUM(transaction_amount) AS total_revenue
FROM raw_balaji_sales
GROUP BY item_type
ORDER BY total_revenue DESC;
