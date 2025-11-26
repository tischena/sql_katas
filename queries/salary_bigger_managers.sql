-- Show employees whose salaries are higher than 
-- their managers' in the employee_salary table.
-- Managers also have an employee number, id_employee,
-- in this table.

SELECT s1.id_employee, s1.salary, s1.id_manager
FROM employee_salary s1
INNER JOIN employee_salary s2 ON s1.id_manager = s2.id_employee
WHERE s1.salary > s2.salary;
