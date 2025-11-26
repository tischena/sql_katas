-- Write a query that will add a cumulative total column,
-- cumulative_sum, to the income table.
-- Assume that the table does not contain rows 
-- with the same dates.

select *, SUM(income) OVER(ORDER BY date_id) AS cumulative_sum
from income;