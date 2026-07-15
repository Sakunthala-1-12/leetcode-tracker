# Last updated: 7/15/2026, 3:09:50 PM
1class Solution(object):
2    def nextPermutation(self, nums):
3        i = len(nums) - 2
4
5        while i >= 0 and nums[i] >= nums[i + 1]:
6            i -= 1
7
8        if i >= 0:
9            j = len(nums) - 1
10            while nums[j] <= nums[i]:
11                j -= 1
12            nums[i], nums[j] = nums[j], nums[i]
13
14        left = i + 1
15        right = len(nums) - 1
16
17        while left < right:
18            nums[left], nums[right] = nums[right], nums[left]
19            left += 1
20            right -= 1
21        