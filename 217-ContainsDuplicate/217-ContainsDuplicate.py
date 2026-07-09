# Last updated: 7/9/2026, 10:10:39 AM
class Solution:
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
        