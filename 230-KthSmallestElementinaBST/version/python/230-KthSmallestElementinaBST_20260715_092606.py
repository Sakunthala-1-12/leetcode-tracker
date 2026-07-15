# Last updated: 7/15/2026, 9:26:06 AM
1class Solution(object):
2    def isPowerOfTwo(self, n):
3        if n <= 0:
4            return False
5
6        while n % 2 == 0:
7            n //= 2
8
9        return n == 1
10        