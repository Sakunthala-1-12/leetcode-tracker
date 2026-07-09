# Last updated: 7/9/2026, 10:12:46 AM
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums = sorted(nums1 + nums2)
        n = len(nums)
        mid = n // 2

        if n % 2 == 0:
            return (nums[mid - 1] + nums[mid]) / 2.0  # Note the 2.0 for float division
        else:
            return nums[mid]

