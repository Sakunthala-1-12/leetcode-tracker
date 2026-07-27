# Last updated: 7/27/2026, 3:15:28 PM
1class Solution(object):
2    def subsets(self, nums):
3        result = []
4
5        def backtrack(index, path):
6            result.append(path[:])
7
8            for i in range(index, len(nums)):
9                path.append(nums[i])
10                backtrack(i + 1, path)
11                path.pop()
12
13        backtrack(0, [])
14        return result