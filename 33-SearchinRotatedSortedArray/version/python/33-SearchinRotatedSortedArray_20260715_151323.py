# Last updated: 7/15/2026, 3:13:23 PM
1class Solution(object):
2    def search(self, nums, target):
3        left = 0
4        right = len(nums) - 1
5
6        while left <= right:
7            mid = (left + right) // 2
8
9            if nums[mid] == target:
10                return mid
11
12            # Left half is sorted
13            if nums[left] <= nums[mid]:
14                if nums[left] <= target < nums[mid]:
15                    right = mid - 1
16                else:
17                    left = mid + 1
18            # Right half is sorted
19            else:
20                if nums[mid] < target <= nums[right]:
21                    left = mid + 1
22                else:
23                    right = mid - 1
24
25        return -1
26        