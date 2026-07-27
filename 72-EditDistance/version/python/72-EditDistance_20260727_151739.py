# Last updated: 7/27/2026, 3:17:39 PM
1class Solution(object):
2    def minDistance(self, word1, word2):
3        m, n = len(word1), len(word2)
4
5        dp = [[0] * (n + 1) for _ in range(m + 1)]
6
7        for i in range(m + 1):
8            dp[i][0] = i
9        for j in range(n + 1):
10            dp[0][j] = j
11
12        for i in range(1, m + 1):
13            for j in range(1, n + 1):
14                if word1[i - 1] == word2[j - 1]:
15                    dp[i][j] = dp[i - 1][j - 1]
16                else:
17                    dp[i][j] = 1 + min(
18                        dp[i - 1][j],      # Delete
19                        dp[i][j - 1],      # Insert
20                        dp[i - 1][j - 1]   # Replace
21                    )
22
23        return dp[m][n]