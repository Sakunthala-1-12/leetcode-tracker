# Last updated: 7/20/2026, 10:14:34 AM
1class Solution(object):
2    def isMatch(self, s, p):
3        m = len(s)
4        n = len(p)
5
6        dp = [[False] * (n + 1) for _ in range(m + 1)]
7        dp[0][0] = True
8
9        for j in range(1, n + 1):
10            if p[j - 1] == '*':
11                dp[0][j] = dp[0][j - 1]
12
13        for i in range(1, m + 1):
14            for j in range(1, n + 1):
15                if p[j - 1] == s[i - 1] or p[j - 1] == '?':
16                    dp[i][j] = dp[i - 1][j - 1]
17                elif p[j - 1] == '*':
18                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
19
20        return dp[m][n]