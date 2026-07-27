# Last updated: 7/27/2026, 3:18:58 PM
1class Solution(object):
2    def search(self, nums, target):
3        left, right = 0, len(nums) - 1
4
5        while left <= right:
6            mid = (left + right) // 2
7
8            if nums[mid] == target:
9                return True
10
11            if nums[left] == nums[mid] == nums[right]:
12                left += 1
13                right -= 1
14            elif nums[left] <= nums[mid]:
15                if nums[left] <= target < nums[mid]:
16                    right = mid - 1
17                else:
18                    left = mid + 1
19            else:
20                if nums[mid] < target <= nums[right]:
21                    left = mid + 1
22                else:
23                    right = mid - 1
24
25        return False