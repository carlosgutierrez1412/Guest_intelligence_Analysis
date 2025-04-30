SELECT
    order_id,
    [date],
    transaction_amount,
    CASE
        WHEN transaction_amount < 50 THEN 'Low'
        WHEN transaction_amount BETWEEN 50 AND 100 THEN 'Medium'
        ELSE 'High'
    END AS revenue_tier
FROM raw_balaji_sales;
