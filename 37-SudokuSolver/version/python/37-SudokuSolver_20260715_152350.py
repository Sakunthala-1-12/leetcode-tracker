# Last updated: 7/15/2026, 3:23:50 PM
1class Solution(object):
2    def combinationSum2(self, candidates, target):
3        candidates.sort()
4        result = []
5
6        def backtrack(start, path, remaining):
7            if remaining == 0:
8                result.append(path[:])
9                return
10
11            for i in range(start, len(candidates)):
12                if i > start and candidates[i] == candidates[i - 1]:
13                    continue
14
15                if candidates[i] > remaining:
16                    break
17
18                path.append(candidates[i])
19                backtrack(i + 1, path, remaining - candidates[i])
20                path.pop()
21
22        backtrack(0, [], target)
23        return result
24        