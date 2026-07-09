# Last updated: 7/9/2026, 10:11:59 AM
class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k