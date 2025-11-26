-- There's a simple sales log - log_sales.
-- Find the most frequently sold product(s) for each date.

WITH count_table AS (
    SELECT 
        date_id,
        product,
        COUNT(*) OVER (PARTITION BY date_id, product) AS product_count
    FROM log_sales
),
     rank_table AS(
    SELECT
         distinct date_id, 
         product,
         product_count,
         dense_rank() over(partition by date_id order by product_count desc) as ranking
FROM count_table
     )
SELECT 
     date_id,
     product
    FROM rank_table
    where ranking = 1
    ;