-- There's a connection log - logs. 
-- Calculate the duration of each connection in days. 
-- There are only two statuses: start and end.

select t1.id,
       CAST(julianday(t2.action_date) - julianday(t1.action_date) AS INTEGER) AS duration
from logs t1
join logs t2 on t2.id = t1.id
where t1.status = 'start' and t2.status = 'end';
