-- Last updated: 7/9/2026, 10:10:56 AM
# Write your MySQL query statement below
SELECT c.Name AS Customers
FROM Customers c
LEFT JOIN Orders o
ON c.Id = o.CustomerId
WHERE o.Id IS NULL;