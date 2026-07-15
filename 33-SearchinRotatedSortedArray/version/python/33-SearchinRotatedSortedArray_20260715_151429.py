# Last updated: 7/15/2026, 3:14:29 PM
1class Solution(object):
2    def searchRange(self, nums, target):
3        def findFirst():
4            left, right = 0, len(nums) - 1
5            ans = -1
6            while left <= right:
7                mid = (left + right) // 2
8                if nums[mid] == target:
9                    ans = mid
10                    right = mid - 1
11                elif nums[mid] < target:
12                    left = mid + 1
13                else:
14                    right = mid - 1
15            return ans
16
17        def findLast():
18            left, right = 0, len(nums) - 1
19            ans = -1
20            while left <= right:
21                mid = (left + right) // 2
22                if nums[mid] == target:
23                    ans = mid
24                    left = mid + 1
25                elif nums[mid] < target:
26                    left = mid + 1
27                else:
28                    right = mid - 1
29            return ans
30
31        return [findFirst(), findLast()]
32        