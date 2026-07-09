# Last updated: 7/9/2026, 10:10:31 AM
class Solution:
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)