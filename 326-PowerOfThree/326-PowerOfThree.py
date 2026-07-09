# Last updated: 7/9/2026, 10:10:18 AM
class Solution:
    def isPowerOfThree(self, n):
        if n <= 0:
            return False

        while n % 3 == 0:
            n //= 3

        return n == 1