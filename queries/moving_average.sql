-- Write a query that will add a moving_average column
-- with a moving average to the income table. 
-- Round the result to integers.

-- The moving average in this problem will be 
-- the sum of the current, previous, 
-- and next days divided by 3, that is:
--  for 2025-01-02, the moving average will be
-- equal to the sum of the income values ​​for 
-- the previous date (2025-01-01), 
-- the current date (2025-01-02), 
-- and the following date (2025-01-03);
--  for 2025-01-03, the moving average will be 
--  equal to the sum of the income values ​​for 
--  the previous date (2025-01-02), 
--  the current date (2025-01-03), 
--  and the following date (2025-01-04), and so on.

SELECT
    date_id,
    income,
    ROUND(AVG(income) OVER (
        ORDER BY date_id
        ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
        )
    ) AS moving_average
FROM income;