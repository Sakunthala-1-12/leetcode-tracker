# Last updated: 7/9/2026, 10:12:37 AM
class Solution:
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x = x // 10

        # For even and odd length numbers
        return x == reversed_half or x == reversed_half // 10

        