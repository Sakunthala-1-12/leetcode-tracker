# Last updated: 7/27/2026, 3:06:38 PM
1class Solution(object):
2    def uniquePaths(self, m, n):
3        dp = [1] * n
4
5        for _ in range(m - 1):
6            for j in range(1, n):
7                dp[j] += dp[j - 1]
8
9        return dp[-1]
10        