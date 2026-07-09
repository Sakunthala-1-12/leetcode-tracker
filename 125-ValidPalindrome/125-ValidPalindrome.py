# Last updated: 7/9/2026, 10:11:31 AM
class Solution:
    def isPalindrome(self, s):
        filtered = ""

        for ch in s:
            if ch.isalnum():
                filtered += ch.lower()

        return filtered == filtered[::-1]        