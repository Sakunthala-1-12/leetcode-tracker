# Last updated: 7/27/2026, 2:49:36 PM
1class Solution(object):
2    def permute(self, nums):
3        result = []
4
5        def backtrack(path, remaining):
6            if not remaining:
7                result.append(path)
8                return
9
10            for i in range(len(remaining)):
11                backtrack(path + [remaining[i]], remaining[:i] + remaining[i + 1:])
12
13        backtrack([], nums)
14        return result