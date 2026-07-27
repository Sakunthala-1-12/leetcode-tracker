# Last updated: 7/27/2026, 3:18:33 PM
1class Solution(object):
2    def removeDuplicates(self, nums):
3        if len(nums) <= 2:
4            return len(nums)
5
6        k = 2
7
8        for i in range(2, len(nums)):
9            if nums[i] != nums[k - 2]:
10                nums[k] = nums[i]
11                k += 1
12
13        return k