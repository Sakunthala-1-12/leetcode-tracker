-- Last updated: 7/9/2026, 10:10:59 AM
# Write your MySQL query statement below
SELECT e.Name AS Employee
FROM Employee e
JOIN Employee m
ON e.ManagerId = m.Id
WHERE e.Salary > m.Salary;