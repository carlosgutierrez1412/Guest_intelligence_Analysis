
SELECT *
FROM (
    SELECT
        item_type,
        item_name,
        SUM(quantity) AS total_units_sold,
        RANK() OVER (PARTITION BY item_type ORDER BY SUM(quantity) DESC) AS item_rank
    FROM raw_balaji_sales
    GROUP BY item_type, item_name
) ranked_items
WHERE item_rank <= 3;
