# Last updated: 7/15/2026, 3:22:01 PM
1class Solution(object):
2    def combinationSum(self, candidates, target):
3        result = []
4
5        def backtrack(start, path, total):
6            if total == target:
7                result.append(path[:])
8                return
9            if total > target:
10                return
11
12            for i in range(start, len(candidates)):
13                path.append(candidates[i])
14                backtrack(i, path, total + candidates[i])
15                path.pop()
16
17        backtrack(0, [], 0)
18        return result
19        