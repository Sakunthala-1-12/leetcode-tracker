# Last updated: 7/9/2026, 10:10:38 AM
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        seen = {}

        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True

            seen[num] = i

        return False