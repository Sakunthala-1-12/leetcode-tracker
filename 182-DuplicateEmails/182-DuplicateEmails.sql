-- Last updated: 7/9/2026, 10:10:57 AM
# Write your MySQL query statement below
SELECT Email
FROM Person
GROUP BY Email
HAVING COUNT(*) > 1;