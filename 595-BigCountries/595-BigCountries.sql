-- Last updated: 7/9/2026, 10:09:50 AM
# Write your MySQL query statement 
SELECT name, population, area
FROM World
WHERE area >= 3000000
   OR population >= 25000000;