
SELECT
    transaction_type,
    COUNT(*) AS transaction_count,
    SUM(transaction_amount) AS total_revenue
FROM raw_balaji_sales
WHERE transaction_type IS NOT NULL
GROUP BY transaction_type
ORDER BY total_revenue DESC;
