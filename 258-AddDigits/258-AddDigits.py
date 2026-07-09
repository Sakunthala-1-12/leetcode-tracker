# Last updated: 7/9/2026, 10:10:26 AM
class Solution:
    def addDigits(self, num):
        while num >= 10:
            total = 0

            while num > 0:
                total += num % 10
                num //= 10

            num = total

        return num