-- Show the employees with the highest salary 
-- in each department from the salary table.

SELECT
    *,
    ROUND(1.0 * salary / SUM(salary) OVER (PARTITION BY department) * 100) AS salary_proc
FROM salary
ORDER BY id_employee;
