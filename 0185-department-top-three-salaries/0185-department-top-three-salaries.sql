# Write your MySQL query statement below
SELECT
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM Employee e
JOIN Department d
    ON e.departmentId = d.id
WHERE e.salary IN (
    SELECT salary
    FROM (
        SELECT DISTINCT salary
        FROM Employee e2
        WHERE e2.departmentId = e.departmentId
        ORDER BY salary DESC
        LIMIT 3
    ) AS top_salaries
);