-- Write a query that will display the top three products
-- by sales volume and the volume of all other products 
-- not included in the top three as the fourth row 
-- in the sales table. 
-- The table must be accessed no more than once 
-- (do not use UNION / UNION ALL).

with top3 as (
    select
        product,
        sum(quantity) as quantity,
        dense_rank() over(order by sum(quantity) desc) as ranking
    from sales
    group by product
)
select
    case when ranking <= 3 then product else 'другие' end as product,
    sum(quantity) as quantity
from top3
group by case when ranking <= 3 then product else 'другие' end
order by case when min(ranking) <= 3 then min(ranking) else 4 end;