# Last updated: 7/28/2026, 3:07:45 PM
1class Solution(object):
2    def isScramble(self, s1, s2):
3        memo = {}
4
5        def dfs(a, b):
6            if (a, b) in memo:
7                return memo[(a, b)]
8
9            if a == b:
10                return True
11
12            if sorted(a) != sorted(b):
13                return False
14
15            n = len(a)
16
17            for i in range(1, n):
18                if dfs(a[:i], b[:i]) and dfs(a[i:], b[i:]):
19                    memo[(a, b)] = True
20                    return True
21
22                if dfs(a[:i], b[n-i:]) and dfs(a[i:], b[:n-i]):
23                    memo[(a, b)] = True
24                    return True
25
26            memo[(a, b)] = False
27            return False
28
29        return dfs(s1, s2)
30        