SELECT
    [date],
    time_of_sale,
    SUM(transaction_amount) AS revenue,
    SUM(quantity) AS units_sold,
    COUNT(*) AS transactions
FROM raw_balaji_sales
GROUP BY [date], time_of_sale
ORDER BY [date], time_of_sale;
