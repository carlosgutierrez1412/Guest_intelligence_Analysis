
SELECT
    [date],
    COUNT(*) AS num_orders,
    SUM(transaction_amount) AS total_revenue,
    ROUND(SUM(transaction_amount) * 1.0 / COUNT(*), 2) AS avg_order_value
FROM raw_balaji_sales
GROUP BY [date]
ORDER BY [date];
