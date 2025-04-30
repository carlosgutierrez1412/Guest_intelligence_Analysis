
SELECT
    [date],
    SUM(transaction_amount) AS total_revenue,
    SUM(quantity) AS total_units_sold
FROM raw_balaji_sales
GROUP BY [date]
ORDER BY [date];
