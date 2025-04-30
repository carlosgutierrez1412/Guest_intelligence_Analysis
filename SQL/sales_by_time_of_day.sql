
SELECT
    time_of_sale,
    COUNT(*) AS transactions,
    SUM(transaction_amount) AS total_revenue,
    SUM(quantity) AS total_units_sold
FROM raw_balaji_sales
GROUP BY time_of_sale
ORDER BY total_revenue DESC;
