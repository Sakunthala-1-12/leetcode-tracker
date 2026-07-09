# Last updated: 7/9/2026, 10:11:13 AM
class Solution:
    def titleToNumber(self, columnTitle):
        result = 0

        for ch in columnTitle:
            result = result * 26 + (ord(ch) - ord('A') + 1)

        return result