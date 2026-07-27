# Last updated: 7/27/2026, 3:11:44 PM
1class Solution(object):
2    def climbStairs(self, n):
3        if n <= 2:
4            return n
5
6        a, b = 1, 2
7
8        for _ in range(3, n + 1):
9            a, b = b, a + b
10
11        return b